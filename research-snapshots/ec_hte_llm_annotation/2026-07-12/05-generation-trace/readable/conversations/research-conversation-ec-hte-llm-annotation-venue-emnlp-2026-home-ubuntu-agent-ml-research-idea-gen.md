# Research conversation: 项目：ec_hte_llm_annotation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotat

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 110
- **Recorded user turns:** 1
- **Tool calls:** 34
- **Original source:** `logs/chats/exported-trajectories/account-2/929445b7-1f7a-4e7b-9fef-acd3294376fb.jsonl`
- **Structured JSON:** [`d361167c669cfe1d7f33.json`](../../sessions/d3/d361167c669cfe1d7f33.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-25T16:32:07.736Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T16:32:07.736Z",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "content": "项目：ec_hte_llm_annotation\nVenue：emnlp-2026\n论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper\n\nPhase 1 确定性检查结果：\n源码检查: passed=True, 0 critical, 30 warning\n一致性检查: 0 critical, 48 warning\n编译: ✅, 页数: 32\n内部信息: 0 critical, 0 warning\n\n━━━ 用户自定义规则（作为额外检查项）━━━\n## 用户自定义规则（必须遵守）\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section\n- **[EMNLP 2026]** abstract 不要超过 200 words\n\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n请将以上规则逐条作为额外审计维度检查。违反的规则用 dimension `[写作规则]` 或 `[审稿规则]` 标记，severity 按实际影响判定。\n\n请按照你的角色指令执行内容结构审计。"
}
```

---

### Runtime record

_source line 2 · 2026-05-25T16:32:07.739Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T16:32:07.739Z",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

## Round 1

108 recorded events

### User

_source line 3 · 2026-05-25T16:32:07.770Z_

项目：ec_hte_llm_annotation
Venue：emnlp-2026
论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper

Phase 1 确定性检查结果：
源码检查: passed=True, 0 critical, 30 warning
一致性检查: 0 critical, 48 warning
编译: ✅, 页数: 32
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
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "598957a6-fb61-4bfa-a29f-69b712b4b3be",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-25T16:32:07.769Z_

```json
{
  "parentUuid": "598957a6-fb61-4bfa-a29f-69b712b4b3be",
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
  "uuid": "62cbc571-13d1-48f3-8169-df9b478cff20",
  "timestamp": "2026-05-25T16:32:07.769Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-25T16:32:07.770Z_

```json
{
  "parentUuid": "62cbc571-13d1-48f3-8169-df9b478cff20",
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
  "uuid": "7f5816b0-ea82-40cc-a4e0-86c73f5a4170",
  "timestamp": "2026-05-25T16:32:07.770Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-25T16:32:07.770Z_

```json
{
  "parentUuid": "7f5816b0-ea82-40cc-a4e0-86c73f5a4170",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "409cad68-18d3-4482-ad43-1eca10fcdd36",
  "timestamp": "2026-05-25T16:32:07.770Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
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
  "aiTitle": "Review EMNLP 2026 paper compliance and structure",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

### Assistant

_source line 8 · 2026-05-25T16:32:11.884Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the required skill files and the paper's .tex files. I'll read the two skill files and discover the paper directory structure in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "409cad68-18d3-4482-ad43-1eca10fcdd36",
  "isSidechain": false,
  "requestId": "req_011CbPcC4djmokc9Abqp5GoA",
  "type": "assistant",
  "uuid": "3a5f64ed-6484-4722-8eab-64751e9d722c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5peDF9zHeJEoseLvLS4K9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27012,
      "cache_read_input_tokens": 11846,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 296,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27012
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-25T16:32:12.496Z_

开始执行内容结构审计。先加载审计标准和论文源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a5f64ed-6484-4722-8eab-64751e9d722c",
  "isSidechain": false,
  "requestId": "req_011CbPcC4djmokc9Abqp5GoA",
  "type": "assistant",
  "uuid": "dbd3df28-66ef-4bfe-9368-bd3a0ecd86fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5peDF9zHeJEoseLvLS4K9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27012,
      "cache_read_input_tokens": 11846,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 296,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27012
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-25T16:32:13.020Z_

<details open><summary>🔧 Tool call — Read · `toolu_012L7mRAfsRT1sjfTribscAC`</summary>

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
  "parentUuid": "dbd3df28-66ef-4bfe-9368-bd3a0ecd86fe",
  "isSidechain": false,
  "requestId": "req_011CbPcC4djmokc9Abqp5GoA",
  "type": "assistant",
  "uuid": "26b07bb0-52ee-4295-95ad-7801a29bd122",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5peDF9zHeJEoseLvLS4K9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27012,
      "cache_read_input_tokens": 11846,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 296,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27012
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-25T16:32:14.305Z_

<details><summary>↩ Tool result · `toolu_01TSq66VwXPGD5g1xcqzGsha`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fec34f8b-2f2b-4f4c-b3b4-35b2f0c5b52e",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "e8b8db16-8c99-4ae2-9e9d-71feaaff9fc1",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/checklist.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex"
    ],
    "durationMs": 7,
    "numFiles": 13,
    "truncated": false
  },
  "sourceToolAssistantUUID": "fec34f8b-2f2b-4f4c-b3b4-35b2f0c5b52e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T16:32:13.038Z_

<details><summary>↩ Tool result · `toolu_012L7mRAfsRT1sjfTribscAC`</summary>

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
  "parentUuid": "26b07bb0-52ee-4295-95ad-7801a29bd122",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "9fe173e0-3961-40b6-9d52-f59f546e2cb2",
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
  "sourceToolAssistantUUID": "26b07bb0-52ee-4295-95ad-7801a29bd122",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 13 · 2026-05-25T16:32:13.493Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HKxUC7ayysobMjCps8pwrk`</summary>

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
  "parentUuid": "9fe173e0-3961-40b6-9d52-f59f546e2cb2",
  "isSidechain": false,
  "requestId": "req_011CbPcC4djmokc9Abqp5GoA",
  "type": "assistant",
  "uuid": "39cfb923-a72c-404b-8c91-bd025e814102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5peDF9zHeJEoseLvLS4K9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27012,
      "cache_read_input_tokens": 11846,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 296,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27012
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-25T16:32:13.501Z_

<details><summary>↩ Tool result · `toolu_01HKxUC7ayysobMjCps8pwrk`</summary>

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
  "parentUuid": "39cfb923-a72c-404b-8c91-bd025e814102",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "be98c229-684c-49ce-91d4-9f6971b2098f",
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
  "sourceToolAssistantUUID": "39cfb923-a72c-404b-8c91-bd025e814102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 15 · 2026-05-25T16:32:14.293Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TSq66VwXPGD5g1xcqzGsha`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be98c229-684c-49ce-91d4-9f6971b2098f",
  "isSidechain": false,
  "requestId": "req_011CbPcC4djmokc9Abqp5GoA",
  "type": "assistant",
  "uuid": "fec34f8b-2f2b-4f4c-b3b4-35b2f0c5b52e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5peDF9zHeJEoseLvLS4K9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27012,
      "cache_read_input_tokens": 11846,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 296,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27012
          },
          "type": "message"
        }
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
  "lastPrompt": "项目：ec_hte_llm_annotation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 30 warning 一致性检查…",
  "leafUuid": "e8b8db16-8c99-4ae2-9e9d-71feaaff9fc1",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP 2026 paper compliance and structure",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

### Assistant

_source line 18 · 2026-05-25T16:32:17.255Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read all the .tex files. Let me read them in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8b8db16-8c99-4ae2-9e9d-71feaaff9fc1",
  "isSidechain": false,
  "requestId": "req_011CbPcCYVJ11TR53k96opLE",
  "type": "assistant",
  "uuid": "d40ac7c3-ca63-4fbe-8d78-900dcbcf4714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ya9ZTuvVZrZFRCAzFdmvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 38858,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 38858,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-25T16:32:17.772Z_

审计标准已加载。现在读取所有 .tex 源码文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d40ac7c3-ca63-4fbe-8d78-900dcbcf4714",
  "isSidechain": false,
  "requestId": "req_011CbPcCYVJ11TR53k96opLE",
  "type": "assistant",
  "uuid": "e7a90c8d-080a-4fd2-a4ca-98c8b87fc17c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ya9ZTuvVZrZFRCAzFdmvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 38858,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 38858,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-25T16:32:18.340Z_

<details open><summary>🔧 Tool call — Read · `toolu_012Qo9pBtqCog3sP1XQCUdKP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7a90c8d-080a-4fd2-a4ca-98c8b87fc17c",
  "isSidechain": false,
  "requestId": "req_011CbPcCYVJ11TR53k96opLE",
  "type": "assistant",
  "uuid": "f82dbfb0-8337-4687-84c8-f57e9127fcc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ya9ZTuvVZrZFRCAzFdmvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 38858,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 38858,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-25T16:32:24.742Z_

<details><summary>↩ Tool result · `toolu_01Q87AZaEtDQLTUhhBQ2cfq9`</summary>

```text
1	\section*{Responsible NLP Research Checklist}
2	
3	\paragraph{A. Did you describe the limitations of your work?}
4	Yes. Section ``Limitations'' discusses seven specific limitations: expert budget thresholds, RMSE tradeoff at small sample sizes, baseline classifier quality, plug-in standard error approximation, symmetric misclassification assumption, additive CATE structure, and known subgroup structure requirement.
5	
6	\paragraph{B. Did you discuss any potential risks of your work?}
7	Yes. The method corrects bias in treatment effect estimates used for resource allocation decisions. We explicitly discuss conditions under which EC-HTE should \textit{not} be applied (low error heterogeneity, insufficient expert budget), preventing misuse of stratified correction where global correction is more appropriate.
8	
9	\paragraph{C. Do the abstract and introduction summarize the paper's main claims?}
10	Yes. The abstract states all five contributions with specific quantitative results. The introduction provides detailed context and a numbered contribution list.
11	
12	\paragraph{D1. Did you describe the experimental setup, including hyperparameter search?}
13	Yes. Section~\ref{sec:bias_mechanism} specifies all DGP parameters, Monte Carlo configurations, and method variants. Appendix~\ref{app:dgp} provides the complete data generating process specification. The hierarchical Bayesian estimator uses a $\text{Gamma}(3, 1)$ hyperprior with sensitivity analysis (Appendix~\ref{app:mcmc}).
14	
15	\paragraph{D2. Did you report error bars or statistical significance?}
16	Yes. All results are averaged over 100 Monte Carlo runs. We report 95\% CI coverage as a primary metric. RMSE captures both bias and variance. We do not use the term ``significant'' without formal testing.
17	
18	\paragraph{D3. Did you include the number of parameters and computational budget?}
19	Yes. Main experiments use empirical Bayes point estimates ($<$5ms per subgroup); MCMC validation (4 chains $\times$ 4000 iterations) confirms agreement (Appendix~\ref{app:mcmc}). The number of estimated parameters scales as $O(K \cdot J^2)$ where $K$ is subgroups and $J$ is effect-modifier levels.
20	
21	\paragraph{D4. Did you report the number and range of hyperparameters searched?}
22	Yes. Hyperprior sensitivity analysis covers $0.5\times$ to $2\times$ scaling of the $\text{Gamma}(3,1)$ concentration prior (Appendix~\ref{app:mcmc}). No other hyperparameters are tuned.
23	
24	\paragraph{E1. Did you use or create scientific artifacts?}
25	Yes. We use the TweetEval sentiment corpus for semi-synthetic experiments. Yes. Our experimental code and synthetic data generation scripts are publicly available (see footnote on page 1).
26	
27	\paragraph{E2. Did you discuss the license or terms for use and/or distribution of any artifacts?}
28	The TweetEval corpus is publicly available under its original license. Our code is publicly available under an open-source license (see footnote on page 1).
29	
30	\paragraph{E3. Did you discuss if your use of existing artifact(s) was consistent with their intended use?}
31	Yes. TweetEval is a benchmark for tweet classification. We use it as a source of realistic text features for semi-synthetic CATE experiments, which is consistent with its role as a research benchmark.
32	
33	\paragraph{F1. Did you include the full text of instructions given to participants?}
34	Not applicable. No human participants were involved in this study. Expert labels in the semi-synthetic experiments are simulated from known ground truth.
35	
36	\paragraph{F2. Did you report information about how you recruited participants?}
37	Not applicable.
38	
39	\paragraph{F3. Did you discuss if and how consent was obtained?}
40	Not applicable.
41	
42	\paragraph{F4. Were the individuals in the dataset informed about the data collection?}
43	The TweetEval corpus is a pre-existing public dataset. No new data was collected from individuals.
44	
45	\paragraph{G. Did you discuss whether and how your work could be misused?}
46	The primary risk is applying EC-HTE when its assumptions are violated (asymmetric misclassification, unknown subgroup structure). We provide a computable diagnostic criterion that guards against inappropriate application and discuss boundary conditions explicitly.
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fa92f87-744a-4348-9388-136b97a89e21",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "076510e1-606a-49d7-b6ae-d290528ce00f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/checklist.tex",
      "content": "\\section*{Responsible NLP Research Checklist}\n\n\\paragraph{A. Did you describe the limitations of your work?}\nYes. Section ``Limitations'' discusses seven specific limitations: expert budget thresholds, RMSE tradeoff at small sample sizes, baseline classifier quality, plug-in standard error approximation, symmetric misclassification assumption, additive CATE structure, and known subgroup structure requirement.\n\n\\paragraph{B. Did you discuss any potential risks of your work?}\nYes. The method corrects bias in treatment effect estimates used for resource allocation decisions. We explicitly discuss conditions under which EC-HTE should \\textit{not} be applied (low error heterogeneity, insufficient expert budget), preventing misuse of stratified correction where global correction is more appropriate.\n\n\\paragraph{C. Do the abstract and introduction summarize the paper's main claims?}\nYes. The abstract states all five contributions with specific quantitative results. The introduction provides detailed context and a numbered contribution list.\n\n\\paragraph{D1. Did you describe the experimental setup, including hyperparameter search?}\nYes. Section~\\ref{sec:bias_mechanism} specifies all DGP parameters, Monte Carlo configurations, and method variants. Appendix~\\ref{app:dgp} provides the complete data generating process specification. The hierarchical Bayesian estimator uses a $\\text{Gamma}(3, 1)$ hyperprior with sensitivity analysis (Appendix~\\ref{app:mcmc}).\n\n\\paragraph{D2. Did you report error bars or statistical significance?}\nYes. All results are averaged over 100 Monte Carlo runs. We report 95\\% CI coverage as a primary metric. RMSE captures both bias and variance. We do not use the term ``significant'' without formal testing.\n\n\\paragraph{D3. Did you include the number of parameters and computational budget?}\nYes. Main experiments use empirical Bayes point estimates ($<$5ms per subgroup); MCMC validation (4 chains $\\times$ 4000 iterations) confirms agreement (Appendix~\\ref{app:mcmc}). The number of estimated parameters scales as $O(K \\cdot J^2)$ where $K$ is subgroups and $J$ is effect-modifier levels.\n\n\\paragraph{D4. Did you report the number and range of hyperparameters searched?}\nYes. Hyperprior sensitivity analysis covers $0.5\\times$ to $2\\times$ scaling of the $\\text{Gamma}(3,1)$ concentration prior (Appendix~\\ref{app:mcmc}). No other hyperparameters are tuned.\n\n\\paragraph{E1. Did you use or create scientific artifacts?}\nYes. We use the TweetEval sentiment corpus for semi-synthetic experiments. Yes. Our experimental code and synthetic data generation scripts are publicly available (see footnote on page 1).\n\n\\paragraph{E2. Did you discuss the license or terms for use and/or distribution of any artifacts?}\nThe TweetEval corpus is publicly available under its original license. Our code is publicly available under an open-source license (see footnote on page 1).\n\n\\paragraph{E3. Did you discuss if your use of existing artifact(s) was consistent with their intended use?}\nYes. TweetEval is a benchmark for tweet classification. We use it as a source of realistic text features for semi-synthetic CATE experiments, which is consistent with its role as a research benchmark.\n\n\\paragraph{F1. Did you include the full text of instructions given to participants?}\nNot applicable. No human participants were involved in this study. Expert labels in the semi-synthetic experiments are simulated from known ground truth.\n\n\\paragraph{F2. Did you report information about how you recruited participants?}\nNot applicable.\n\n\\paragraph{F3. Did you discuss if and how consent was obtained?}\nNot applicable.\n\n\\paragraph{F4. Were the individuals in the dataset informed about the data collection?}\nThe TweetEval corpus is a pre-existing public dataset. No new data was collected from individuals.\n\n\\paragraph{G. Did you discuss whether and how your work could be misused?}\nThe primary risk is applying EC-HTE when its assumptions are violated (asymmetric misclassification, unknown subgroup structure). We provide a computable diagnostic criterion that guards against inappropriate application and discuss boundary conditions explicitly.\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  },
  "sourceToolAssistantUUID": "1fa92f87-744a-4348-9388-136b97a89e21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T16:32:18.346Z_

<details><summary>↩ Tool result · `toolu_012Qo9pBtqCog3sP1XQCUdKP`</summary>

```text
1	\begin{abstract}
2	Standard confusion-matrix correction for noisy annotations assumes uniform error rates.
3	When this assumption fails---as it routinely does with large language model (LLM) classifiers, whose error rates vary by up to $5\times$ across subgroups---correction can reverse estimated effect signs.
4	We derive an exact bias identity: global correction introduces subgroup-level bias $\delta_s \cdot \Delta\tau / (1 - 2\bar{\pi})$ under symmetric errors (generalizing to a full-matrix form for arbitrary asymmetric confusion matrices; Remark~\ref{rem:asymmetric}), verified at $R^2 \geq 0.97$ on synthetic grids ($R^2 = 0.975$ in aggregate across 11 real LLM confusion matrices; per-model range $0.76$--$0.99$).
5	The identity predicts that global correction reverses conditional average treatment effect (CATE) sign in 14.9\% of configurations where the true effect is small ($\tau(0) = 0.03$) and amplifies bias in all eight real LLMs tested; a $\Delta\tau$-free diagnostic corollary flags harmful correction from error rates alone, without estimating treatment effects.
6	We characterize when per-subgroup correction is beneficial ($\Delta\pi > 0.15$, $n_{\text{expert}} \geq 250$, $K \leq 4$) versus when global correction should be retained, and implement one such correction via hierarchical Bayesian estimation, reducing $|\text{bias}|$ by $7.4\times$ under extreme heterogeneity\footnote{Code and data are available at \url{https://anonymous.4open.science/r/ec_hte_llm_annotation-4CC8/}.}.
7	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f82dbfb0-8337-4687-84c8-f57e9127fcc0",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "2d3cc8bf-2c95-43c0-820b-ad038c316e28",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nStandard confusion-matrix correction for noisy annotations assumes uniform error rates.\nWhen this assumption fails---as it routinely does with large language model (LLM) classifiers, whose error rates vary by up to $5\\times$ across subgroups---correction can reverse estimated effect signs.\nWe derive an exact bias identity: global correction introduces subgroup-level bias $\\delta_s \\cdot \\Delta\\tau / (1 - 2\\bar{\\pi})$ under symmetric errors (generalizing to a full-matrix form for arbitrary asymmetric confusion matrices; Remark~\\ref{rem:asymmetric}), verified at $R^2 \\geq 0.97$ on synthetic grids ($R^2 = 0.975$ in aggregate across 11 real LLM confusion matrices; per-model range $0.76$--$0.99$).\nThe identity predicts that global correction reverses conditional average treatment effect (CATE) sign in 14.9\\% of configurations where the true effect is small ($\\tau(0) = 0.03$) and amplifies bias in all eight real LLMs tested; a $\\Delta\\tau$-free diagnostic corollary flags harmful correction from error rates alone, without estimating treatment effects.\nWe characterize when per-subgroup correction is beneficial ($\\Delta\\pi > 0.15$, $n_{\\text{expert}} \\geq 250$, $K \\leq 4$) versus when global correction should be retained, and implement one such correction via hierarchical Bayesian estimation, reducing $|\\text{bias}|$ by $7.4\\times$ under extreme heterogeneity\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/ec_hte_llm_annotation-4CC8/}.}.\n\\end{abstract}",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  },
  "sourceToolAssistantUUID": "f82dbfb0-8337-4687-84c8-f57e9127fcc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T16:32:18.741Z_

<details open><summary>🔧 Tool call — Read · `toolu_011gygkaTGA7s4Ft63H9UWSt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d3cc8bf-2c95-43c0-820b-ad038c316e28",
  "isSidechain": false,
  "requestId": "req_011CbPcCYVJ11TR53k96opLE",
  "type": "assistant",
  "uuid": "c19a00d3-adae-4fd7-8c7c-c7b89a0af516",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ya9ZTuvVZrZFRCAzFdmvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 38858,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 38858,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-25T16:32:18.746Z_

<details><summary>↩ Tool result · `toolu_011gygkaTGA7s4Ft63H9UWSt`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Consider estimating whether a content moderation policy reduces hate speech differently across demographic groups, using GPT-4 to classify thousands of posts.
5	After standard confusion-matrix correction, the analysis concludes the policy \emph{increases} hate speech among younger users---but the true effect is protective.
6	This sign reversal is not an edge case.
7	
8	Large language models (LLMs) now routinely replace human annotators in computational social science, producing labels for sentiment, hate speech, stance, and political discourse at costs orders of magnitude below manual coding~\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,tan2024llm}.
9	When these labels serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, the standard correction protocol\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.} is straightforward: validate a sample against expert annotations, estimate a confusion matrix, and apply its inverse uniformly to correct conditional average treatment effect (CATE) estimates.
10	Yet LLM annotations are not uniformly accurate: \citet{ashwin2025bias} document error rates varying by up to 5$\times$ across demographic subgroups; in our pilot, GPT-4.1 error rates range from 10.2\% to 20.0\% across text-feature subgroups ($\Delta\pi = 0.098$).
11	
12	We show that when error rates vary across subgroups, this standard correction can make things worse.
13	In 14.9\% of our synthetic configurations (across a grid of $\Delta\pi$ and $\tau(0)$ values; $\tau(0) = 0.03$), global correction reverses the sign of estimated CATE---a protective treatment ($\tau = +0.03$) appears harmful ($\hat{\tau} = -0.059$)---rising to 31\% at $\tau(0) = 0.01$ (Figure~\ref{fig:sign_reversal}); all eight real LLMs tested amplify bias under global correction, while our per-subgroup correction (EC-HTE; Section~\ref{sec:method}) eliminates sign reversal in the primary $K{=}2$ setting.
14	Global correction amplifies subgroup-level bias by up to 2.86$\times$ ($K{=}2$) and 2.41$\times$ ($K{=}4$); the classical Frazis--Loewenstein attenuation correction~\cite{frazis2003estimating} \emph{increases} bias by up to 2.9$\times$.
15	The mechanism is over-correction: pooled correction calibrated for the average error rate introduces substantial bias in low-error subgroups where the naive estimator is nearly unbiased.
16	
17	We derive an exact bias identity explaining when and why (Theorem~\ref{thm:bias_identity}), verified at $R^2 \geq 0.97$ on synthetic grids.
18	The per-subgroup correction prescribed by the identity reduces $|\text{bias}|$ by $7.4\times$ under extreme heterogeneity; the advantage is conditional on sufficient $\Delta\pi$ and expert budget.
19	
20	Existing corrections---prediction-powered inference (PPI)~\cite{angelopoulos2023ppi}, design-based supervised learning (DSL)~\cite{egami2023dsl}, prediction-powered conditional inference (PPCI)~\cite{sui2026ppci}, arm-specific PPI~\cite{mozer2026ppi}, ForestIV~\cite{bu2023forestiv}---assume homogeneous prediction error; none addresses effect modifier misclassification (Section~\ref{sec:related}).
21	
22	\begin{figure*}[t]
23	\centering
24	\includegraphics[width=\textwidth]{figures/fig1_sign_reversal.pdf}
25	\caption{CATE sign reversal under global correction ($K{=}2$, $\tau(0) = 0.03$). (A) Naive vs.\ global-corrected CATE; red triangles mark sign reversals (7.5\% of subgroup estimates). (B) Extreme case: true $\tau = +0.03$, estimated $\hat{\tau} = -0.059$. (C) 14.9\% of configurations exhibit sign reversal; all 8 real LLMs amplify bias; EC-HTE: 0\% reversal.}
26	\label{fig:sign_reversal}
27	\end{figure*}
28	
29	\begin{figure*}[!t]
30	\centering
31	\includegraphics[width=\textwidth]{figures/fig_combined_overview.pdf}
32	\caption{Overview. (a)~LLM classifiers exhibit heterogeneous error rates across subgroups (up to $5\times$). (b)~Global correction over/under-corrects, introducing bias $\delta_s \cdot \Delta\tau / (1{-}2\bar{\pi})$ that can reverse CATE sign. (c)~\textit{Top (rose):} standard pipeline applies a pooled confusion matrix uniformly; \textit{bottom (teal):} EC-HTE estimates per-subgroup matrices via hierarchical Bayes, applies stratified inversion with a $\kappa$-guard, and propagates uncertainty into CausalForestDML. (d)~Key results across eight LLMs and four NLP tasks.}
33	\label{fig:overview}
34	\label{fig:method_overview}
35	\end{figure*}
36	
37	Our contributions are:
38	\begin{itemize}
39	    \item An exact bias identity (Theorem~\ref{thm:bias_identity}): global correction introduces subgroup-level bias $\delta_s \cdot \Delta\tau / (1-2\bar{\pi})$, explaining when and why it reverses CATE sign; verified at $R^2 \geq 0.97$ ($R^2 = 0.975$ across 11 LLM--dataset combinations). The identity yields a $\Delta\tau$-free diagnostic (Proposition~\ref{prop:debiasing_hurts}) predicting when correction increases bias from error rates alone.
40	    \item Empirical operating guidelines: per-subgroup correction outperforms global correction when $\Delta\pi > 0.15$, $n_{\text{expert}} \geq 250$, and $K \leq 4$ subgroups; outside this envelope, the diagnostic guides practitioners to retain standard correction.
41	    \item One concrete instantiation: hierarchical Bayesian confusion matrix estimation (EC-HTE), verified for DIM, CausalForestDML, and R-learner, and composable with PPCI for joint covariate/outcome error.
42	\end{itemize}
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c19a00d3-adae-4fd7-8c7c-c7b89a0af516",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "51fb8f14-2c4b-4d72-a9b7-a8f1d065fbef",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\nConsider estimating whether a content moderation policy reduces hate speech differently across demographic groups, using GPT-4 to classify thousands of posts.\nAfter standard confusion-matrix correction, the analysis concludes the policy \\emph{increases} hate speech among younger users---but the true effect is protective.\nThis sign reversal is not an edge case.\n\nLarge language models (LLMs) now routinely replace human annotators in computational social science, producing labels for sentiment, hate speech, stance, and political discourse at costs orders of magnitude below manual coding~\\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,tan2024llm}.\nWhen these labels serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, the standard correction protocol\\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.} is straightforward: validate a sample against expert annotations, estimate a confusion matrix, and apply its inverse uniformly to correct conditional average treatment effect (CATE) estimates.\nYet LLM annotations are not uniformly accurate: \\citet{ashwin2025bias} document error rates varying by up to 5$\\times$ across demographic subgroups; in our pilot, GPT-4.1 error rates range from 10.2\\% to 20.0\\% across text-feature subgroups ($\\Delta\\pi = 0.098$).\n\nWe show that when error rates vary across subgroups, this standard correction can make things worse.\nIn 14.9\\% of our synthetic configurations (across a grid of $\\Delta\\pi$ and $\\tau(0)$ values; $\\tau(0) = 0.03$), global correction reverses the sign of estimated CATE---a protective treatment ($\\tau = +0.03$) appears harmful ($\\hat{\\tau} = -0.059$)---rising to 31\\% at $\\tau(0) = 0.01$ (Figure~\\ref{fig:sign_reversal}); all eight real LLMs tested amplify bias under global correction, while our per-subgroup correction (EC-HTE; Section~\\ref{sec:method}) eliminates sign reversal in the primary $K{=}2$ setting.\nGlobal correction amplifies subgroup-level bias by up to 2.86$\\times$ ($K{=}2$) and 2.41$\\times$ ($K{=}4$); the classical Frazis--Loewenstein attenuation correction~\\cite{frazis2003estimating} \\emph{increases} bias by up to 2.9$\\times$.\nThe mechanism is over-correction: pooled correction calibrated for the average error rate introduces substantial bias in low-error subgroups where the naive estimator is nearly unbiased.\n\nWe derive an exact bias identity explaining when and why (Theorem~\\ref{thm:bias_identity}), verified at $R^2 \\geq 0.97$ on synthetic grids.\nThe per-subgroup correction prescribed by the identity reduces $|\\text{bias}|$ by $7.4\\times$ under extreme heterogeneity; the advantage is conditional on sufficient $\\Delta\\pi$ and expert budget.\n\nExisting corrections---prediction-powered inference (PPI)~\\cite{angelopoulos2023ppi}, design-based supervised learning (DSL)~\\cite{egami2023dsl}, prediction-powered conditional inference (PPCI)~\\cite{sui2026ppci}, arm-specific PPI~\\cite{mozer2026ppi}, ForestIV~\\cite{bu2023forestiv}---assume homogeneous prediction error; none addresses effect modifier misclassification (Section~\\ref{sec:related}).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_sign_reversal.pdf}\n\\caption{CATE sign reversal under global correction ($K{=}2$, $\\tau(0) = 0.03$). (A) Naive vs.\\ global-corrected CATE; red triangles mark sign reversals (7.5\\% of subgroup estimates). (B) Extreme case: true $\\tau = +0.03$, estimated $\\hat{\\tau} = -0.059$. (C) 14.9\\% of configurations exhibit sign reversal; all 8 real LLMs amplify bias; EC-HTE: 0\\% reversal.}\n\\label{fig:sign_reversal}\n\\end{figure*}\n\n\\begin{figure*}[!t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig_combined_overview.pdf}\n\\caption{Overview. (a)~LLM classifiers exhibit heterogeneous error rates across subgroups (up to $5\\times$). (b)~Global correction over/under-corrects, introducing bias $\\delta_s \\cdot \\Delta\\tau / (1{-}2\\bar{\\pi})$ that can reverse CATE sign. (c)~\\textit{Top (rose):} standard pipeline applies a pooled confusion matrix uniformly; \\textit{bottom (teal):} EC-HTE estimates per-subgroup matrices via hierarchical Bayes, applies stratified inversion with a $\\kappa$-guard, and propagates uncertainty into CausalForestDML. (d)~Key results across eight LLMs and four NLP tasks.}\n\\label{fig:overview}\n\\label{fig:method_overview}\n\\end{figure*}\n\nOur contributions are:\n\\begin{itemize}\n    \\item An exact bias identity (Theorem~\\ref{thm:bias_identity}): global correction introduces subgroup-level bias $\\delta_s \\cdot \\Delta\\tau / (1-2\\bar{\\pi})$, explaining when and why it reverses CATE sign; verified at $R^2 \\geq 0.97$ ($R^2 = 0.975$ across 11 LLM--dataset combinations). The identity yields a $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}) predicting when correction increases bias from error rates alone.\n    \\item Empirical operating guidelines: per-subgroup correction outperforms global correction when $\\Delta\\pi > 0.15$, $n_{\\text{expert}} \\geq 250$, and $K \\leq 4$ subgroups; outside this envelope, the diagnostic guides practitioners to retain standard correction.\n    \\item One concrete instantiation: hierarchical Bayesian confusion matrix estimation (EC-HTE), verified for DIM, CausalForestDML, and R-learner, and composable with PPCI for joint covariate/outcome error.\n\\end{itemize}\n",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  },
  "sourceToolAssistantUUID": "c19a00d3-adae-4fd7-8c7c-c7b89a0af516",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T16:32:19.216Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LKPb5XjGCNkKxdk4FQ1oyh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51fb8f14-2c4b-4d72-a9b7-a8f1d065fbef",
  "isSidechain": false,
  "requestId": "req_011CbPcCYVJ11TR53k96opLE",
  "type": "assistant",
  "uuid": "537c6c90-a72c-45c7-bc68-17315a5ad2c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ya9ZTuvVZrZFRCAzFdmvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 38858,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 38858,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-25T16:32:19.221Z_

<details><summary>↩ Tool result · `toolu_01LKPb5XjGCNkKxdk4FQ1oyh`</summary>

```text
1	\section{Correction Prescribed by the Identity}
2	\label{sec:method}
3	
4	Theorem~\ref{thm:bias_identity} identifies per-subgroup misclassification deviation as the bias source; the natural correction is per-subgroup confusion matrix inversion.
5	This correction (EC-HTE) proceeds in three stages: estimate per-subgroup confusion matrices via hierarchical Bayes, invert them to correct observed outcome moments, and propagate correction uncertainty into downstream causal estimators.
6	The complete procedure is summarized in Algorithm~\ref{alg:echte} (Appendix~\ref{app:algorithm}) and illustrated in Figure~\ref{fig:method_overview}.
7	
8	\subsection{Hierarchical Bayes Confusion Matrix Estimation}
9	
10	We place a Dirichlet-Multinomial hierarchical model over the confusion matrices $\{C_s\}_{s=1}^K$.
11	The model estimates the full $J \times J$ confusion matrix per subgroup and does not require symmetric error rates~(A2); (A2) simplifies only the diagnostic (Proposition~\ref{prop:debiasing_hurts}).
12	For each subgroup $s$, row $j$ of $C_s$ has a Dirichlet prior centered at the global pooled confusion matrix $\hat{C}_{\text{global}}$: $\text{Dir}(\alpha_0 \cdot \hat{C}_{\text{global},j})$, where $\hat{C}_{\text{global},j}$ is the $j$-th row of the pooled CM and $\alpha_0 > 0$ is a shared concentration parameter estimated via empirical Bayes (marginal likelihood maximization).
13	We place a $\mathrm{Gamma}(3, 1)$ hyperprior on $\alpha_0$, robust to $2\times$ perturbation (Appendix~\ref{app:hyperprior}).
14	Large $\alpha_0$ pulls estimates toward $\hat{C}_{\text{global}}$; small $\alpha_0$ allows subgroup-specific rates to dominate---partial pooling borrows strength while preserving heterogeneity.
15	
16	Posterior inference uses empirical Bayes optimization ($<$5ms; Markov chain Monte Carlo (MCMC) alternative in Appendix~\ref{app:mcmc}).
17	The key design choice is hierarchical partial pooling rather than independent per-subgroup estimation: when expert labels are scarce relative to the number of subgroups ($n_{\text{expert}} / K < 100$), per-subgroup MLE suffers high variance from small cell counts, while global pooling discards the heterogeneity that Theorem~\ref{thm:bias_identity} identifies as the bias source.
18	HB estimation outperforms stratified MLE in 87.5\% of configurations (Section~\ref{sec:ec_hte_eval}) by adaptively interpolating between these extremes; below $n_{\text{expert}} \times P(Z_{\text{minority}}) / K < 25$, stratified MLE is preferred.
19	
20	\subsection{Subgroup-Stratified Correction}
21	
22	Given posterior mean confusion matrices $\hat{C}_s$, we correct observed outcome moments per subgroup by matrix inversion:
23	\begin{equation}
24	\tilde{\boldsymbol{\mu}}_s = \hat{C}_s^{-1} \cdot \hat{\boldsymbol{\mu}}_s,
25	\end{equation}
26	where $\hat{\boldsymbol{\mu}}_s = [\hat{\tau}_{\text{obs}}(0, s),\, \hat{\tau}_{\text{obs}}(1, s)]^\top$ collects the observed conditional outcome moments in subgroup $s$.
27	Invertibility requires $\pi_s \neq 0.5$ (A4); Laplace smoothing and a $\kappa$-guard ($\kappa(\hat{C}_s) > 100 \to$ fallback to $\bar{C}^{-1}$; threshold ablation in Appendix~\ref{app:kappa_ablation}) ensure finite-sample stability.
28	All 13 tested LLM--dataset combinations fall in $\kappa \in (1.25, 3]$ with coverage $\geq$93\% (Appendix~\ref{app:kappa_analysis}).
29	
30	Global correction applies $\bar{C}^{-1}$ uniformly, introducing the $\delta_s \cdot \Delta\tau$ bias of Theorem~\ref{thm:bias_identity}; subgroup-stratified correction eliminates this at the cost of higher variance (Appendix~\ref{sec:budget}).
31	
32	\subsection{Downstream Integration}
33	
34	Corrected covariates are fed into CausalForestDML~\cite{wager2018causal} with honest splitting; bias corrections propagate as weighted averages of per-subgroup corrections ($R^2 > 0.97$ across 520 configurations; Appendix~\ref{app:bootstrap_se}).
35	Standard errors are adjusted via $\text{se}_{\text{corrected},i} = \sqrt{\text{diag}(\hat{C}_{S_i}^{-1}\, \text{diag}(\text{se}_i^2)\, \hat{C}_{S_i}^{-\top})}$; below $n_{\text{expert}}/K < 50$, a bootstrap ($B{=}100$) maintains $\geq$95\% coverage (Appendix~\ref{app:bootstrap_se}).
36	
37	\paragraph{Diagnostic criterion.}
38	Proposition~\ref{prop:debiasing_hurts} provides a $\Delta\tau$-free diagnostic: global correction harms subgroup $s$ iff $|\delta_s| / ((1-2\bar{\pi}) \cdot \pi_s) > 1$, computable from per-subgroup error rates alone (AUC~$= 0.86$; Section~\ref{sec:diagnostic}).
39	
40	\paragraph{Composition with PPCI.}
41	EC-HTE corrects covariate misclassification; PPCI~\cite{sui2026ppci} corrects outcome-side error. Under both error types, composition reduces $|\text{bias}|$ from 0.179 to 0.007, valid when error sources are independent (Appendix~\ref{sec:ppci}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "537c6c90-a72c-45c7-bc68-17315a5ad2c0",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "9f905d12-a638-4fd2-bce0-7f4453079110",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex",
      "content": "\\section{Correction Prescribed by the Identity}\n\\label{sec:method}\n\nTheorem~\\ref{thm:bias_identity} identifies per-subgroup misclassification deviation as the bias source; the natural correction is per-subgroup confusion matrix inversion.\nThis correction (EC-HTE) proceeds in three stages: estimate per-subgroup confusion matrices via hierarchical Bayes, invert them to correct observed outcome moments, and propagate correction uncertainty into downstream causal estimators.\nThe complete procedure is summarized in Algorithm~\\ref{alg:echte} (Appendix~\\ref{app:algorithm}) and illustrated in Figure~\\ref{fig:method_overview}.\n\n\\subsection{Hierarchical Bayes Confusion Matrix Estimation}\n\nWe place a Dirichlet-Multinomial hierarchical model over the confusion matrices $\\{C_s\\}_{s=1}^K$.\nThe model estimates the full $J \\times J$ confusion matrix per subgroup and does not require symmetric error rates~(A2); (A2) simplifies only the diagnostic (Proposition~\\ref{prop:debiasing_hurts}).\nFor each subgroup $s$, row $j$ of $C_s$ has a Dirichlet prior centered at the global pooled confusion matrix $\\hat{C}_{\\text{global}}$: $\\text{Dir}(\\alpha_0 \\cdot \\hat{C}_{\\text{global},j})$, where $\\hat{C}_{\\text{global},j}$ is the $j$-th row of the pooled CM and $\\alpha_0 > 0$ is a shared concentration parameter estimated via empirical Bayes (marginal likelihood maximization).\nWe place a $\\mathrm{Gamma}(3, 1)$ hyperprior on $\\alpha_0$, robust to $2\\times$ perturbation (Appendix~\\ref{app:hyperprior}).\nLarge $\\alpha_0$ pulls estimates toward $\\hat{C}_{\\text{global}}$; small $\\alpha_0$ allows subgroup-specific rates to dominate---partial pooling borrows strength while preserving heterogeneity.\n\nPosterior inference uses empirical Bayes optimization ($<$5ms; Markov chain Monte Carlo (MCMC) alternative in Appendix~\\ref{app:mcmc}).\nThe key design choice is hierarchical partial pooling rather than independent per-subgroup estimation: when expert labels are scarce relative to the number of subgroups ($n_{\\text{expert}} / K < 100$), per-subgroup MLE suffers high variance from small cell counts, while global pooling discards the heterogeneity that Theorem~\\ref{thm:bias_identity} identifies as the bias source.\nHB estimation outperforms stratified MLE in 87.5\\% of configurations (Section~\\ref{sec:ec_hte_eval}) by adaptively interpolating between these extremes; below $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K < 25$, stratified MLE is preferred.\n\n\\subsection{Subgroup-Stratified Correction}\n\nGiven posterior mean confusion matrices $\\hat{C}_s$, we correct observed outcome moments per subgroup by matrix inversion:\n\\begin{equation}\n\\tilde{\\boldsymbol{\\mu}}_s = \\hat{C}_s^{-1} \\cdot \\hat{\\boldsymbol{\\mu}}_s,\n\\end{equation}\nwhere $\\hat{\\boldsymbol{\\mu}}_s = [\\hat{\\tau}_{\\text{obs}}(0, s),\\, \\hat{\\tau}_{\\text{obs}}(1, s)]^\\top$ collects the observed conditional outcome moments in subgroup $s$.\nInvertibility requires $\\pi_s \\neq 0.5$ (A4); Laplace smoothing and a $\\kappa$-guard ($\\kappa(\\hat{C}_s) > 100 \\to$ fallback to $\\bar{C}^{-1}$; threshold ablation in Appendix~\\ref{app:kappa_ablation}) ensure finite-sample stability.\nAll 13 tested LLM--dataset combinations fall in $\\kappa \\in (1.25, 3]$ with coverage $\\geq$93\\% (Appendix~\\ref{app:kappa_analysis}).\n\nGlobal correction applies $\\bar{C}^{-1}$ uniformly, introducing the $\\delta_s \\cdot \\Delta\\tau$ bias of Theorem~\\ref{thm:bias_identity}; subgroup-stratified correction eliminates this at the cost of higher variance (Appendix~\\ref{sec:budget}).\n\n\\subsection{Downstream Integration}\n\nCorrected covariates are fed into CausalForestDML~\\cite{wager2018causal} with honest splitting; bias corrections propagate as weighted averages of per-subgroup corrections ($R^2 > 0.97$ across 520 configurations; Appendix~\\ref{app:bootstrap_se}).\nStandard errors are adjusted via $\\text{se}_{\\text{corrected},i} = \\sqrt{\\text{diag}(\\hat{C}_{S_i}^{-1}\\, \\text{diag}(\\text{se}_i^2)\\, \\hat{C}_{S_i}^{-\\top})}$; below $n_{\\text{expert}}/K < 50$, a bootstrap ($B{=}100$) maintains $\\geq$95\\% coverage (Appendix~\\ref{app:bootstrap_se}).\n\n\\paragraph{Diagnostic criterion.}\nProposition~\\ref{prop:debiasing_hurts} provides a $\\Delta\\tau$-free diagnostic: global correction harms subgroup $s$ iff $|\\delta_s| / ((1-2\\bar{\\pi}) \\cdot \\pi_s) > 1$, computable from per-subgroup error rates alone (AUC~$= 0.86$; Section~\\ref{sec:diagnostic}).\n\n\\paragraph{Composition with PPCI.}\nEC-HTE corrects covariate misclassification; PPCI~\\cite{sui2026ppci} corrects outcome-side error. Under both error types, composition reduces $|\\text{bias}|$ from 0.179 to 0.007, valid when error sources are independent (Appendix~\\ref{sec:ppci}).",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
    }
  },
  "sourceToolAssistantUUID": "537c6c90-a72c-45c7-bc68-17315a5ad2c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-25T16:32:20.458Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XwmxDQAogBqWt32FVPMKhr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f905d12-a638-4fd2-bce0-7f4453079110",
  "isSidechain": false,
  "requestId": "req_011CbPcCYVJ11TR53k96opLE",
  "type": "assistant",
  "uuid": "c2b88592-3f43-4c6d-81dd-68f0e04fe1b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ya9ZTuvVZrZFRCAzFdmvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 38858,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 38858,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-25T16:32:20.478Z_

<details><summary>↩ Tool result · `toolu_01XwmxDQAogBqWt32FVPMKhr`</summary>

```text
1	\section{Experiments}
2	
3	\begin{figure}[t]
4	\centering
5	\includegraphics[width=\columnwidth]{figures/fig4_budget_compact.pdf}
6	\caption{RMSE vs.\ expert budget under extreme heterogeneity. Crossover at $n{=}250$ ($K{=}2$) and $n{=}1000$ ($K{=}4$, $\Delta\tau{=}0.3$); under the Table~\ref{tab:main_results} DGP, $K{=}4$ crossover is lower ($n{\approx}500$). Shaded bands: $\pm 1$ SD. Full grid in Appendix~\ref{app:budget}.}
7	\label{fig:budget_compact}
8	\end{figure}
9	
10	\subsection{Setup}
11	
12	We test on synthetic ($N{=}5{,}000$, $K \in \{2, 4\}$, controlled $\Delta\tau$ and $\Delta\pi$, 100 Monte Carlo (MC) runs) and semi-synthetic data-generating processes (DGPs) spanning four NLP tasks---sentiment analysis (TweetEval~\cite{barbieri2020tweeteval}, $K{=}4$), hate speech detection (CivilComments, $K{=}4$), stance detection ($K{=}5$; Appendix~\ref{app:stance}), and topic classification (AG News, $K{=}4$; Appendix~\ref{app:agnews})---with full specifications in Appendix~\ref{app:dgp}.
13	
14	We compare: (1) \textit{Naive} (no correction), (2) \textit{Global} (pooled confusion matrix, equivalent to PPI/DSL~\cite{angelopoulos2023ppi,egami2023dsl} with homogeneous error), (3) \textit{Stratified MLE} (per-subgroup DSL without shrinkage), (4) \textit{HB EC-HTE} (per-subgroup correction), (5) \textit{PPCI}~\cite{sui2026ppci}, and (6) \textit{EC-HTE+PPCI}.
15	For CausalForest~\cite{wager2018causal}, we compare naive, global, and EC-HTE variants.
16	Primary metrics are $|\text{bias}|$, root mean squared error (RMSE), and 95\% confidence interval (CI) coverage, averaged across subgroups and 100 MC runs.
17	Robustness validations cover eight conditions including asymmetric errors, subgroup misspecification, and treatment-dependent misclassification (all $\geq$89.5\% coverage; Appendices~\ref{app:hatespeech}--\ref{app:treatment_dep}).
18	Semi-synthetic evaluation uses empirical confusion matrices from 11 LLM--dataset combinations (eight LLMs across two datasets; Appendix~\ref{app:realcm_bias}; semi-real CM validation in Appendix~\ref{app:semireal}; open-source LLM validation in Appendix~\ref{app:multilm_opensource}).
19	
20	\subsection{Empirical Validation of the Bias Identity}
21	\label{sec:bias_mechanism}
22	
23	\begin{figure*}[t]
24	\centering
25	\includegraphics[width=\textwidth]{figures/fig2_heatmap.pdf}
26	\caption{Bias amplification under global correction ($K{=}2$). (a)~High-error subgroup ($\pi_s > \bar{\pi}$): correction always reduces bias. (b)~Low-error subgroup ($\pi_s < \bar{\pi}$): correction \emph{increases} bias when $\Delta\pi > 0.12$ (hatched), reaching $2.86\times$.}
27	\label{fig:heatmap}
28	\end{figure*}
29	
30	We verify Theorem~\ref{thm:bias_identity} on a $K{=}2$ grid (520 configurations, $\Delta\pi \in [0, 0.25]$, $\Delta\tau \in (0, 0.50]$) and a $K{=}4$ grid (Appendix~\ref{app:dgp}).
31	Regressing observed subgroup bias on $\delta_s \cdot \Delta\tau / (1{-}2\bar{\pi})$ yields $R^2 = 0.994$ ($K{=}2$) and $0.97$ ($K{=}4$); residual variance reflects MC noise ($R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$; Appendix~\ref{app:classimbalance}).
32	Global correction worsens bias in 50\% of $K{=}2$ configurations (260/520, excluding $\Delta\pi{=}0$), with amplification reaching 2.86$\times$ ($K{=}2$) and 2.41$\times$ ($K{=}4$); Figure~\ref{fig:heatmap} visualizes the amplification surface.
33	Global correction also reverses the sign of estimated CATE in 14.9\% of configurations at $\tau(0) = 0.03$, with all eight real LLMs amplifying bias; EC-HTE eliminates sign reversal (Figure~\ref{fig:sign_reversal}; Appendix~\ref{app:policy_reversal}).
34	Cross-task validation on stance detection ($K{=}5$, Appendix~\ref{app:stance}) confirms sign reversal (13.3\% $\to$ 3.3\%) and reveals limitations when FNR${}>0.50$.
35	On CivilComments hate speech detection (Appendix~\ref{app:civilcomments}), the bias identity changes the substantive NLP conclusion: global correction suggests demographic-group moderation effects are uniformly small, while EC-HTE reveals a 3.2$\times$ effect-size gap between identity subgroups---consistent with known annotation disparities~\cite{borkan2019nuanced} (Appendix~\ref{app:hatespeech}).
36	Researchers using global correction would miss this differential impact entirely.
37	
38	\subsection{Correction Evaluation}
39	\label{sec:ec_hte_eval}
40	
41	Table~\ref{tab:main_results} presents the main results.
42	In the $K{=}2$ extreme row, global correction \emph{increases} $|\text{bias}|$ relative to naive (0.059 vs.\ 0.058), confirming Theorem~\ref{thm:bias_identity}; F-L corrections fare worse (0.122--0.168).
43	HB EC-HTE reduces $|\text{bias}|$ from 0.059 to 0.008 (7.4$\times$); relative to stratified MLE (0.012), the advantage is 1.5$\times$ with lower RMSE from partial pooling. At $K{=}4$, bias reduces from 0.056 to 0.012 (4.7$\times$), maintaining near-nominal coverage (0.94--0.96).
44	Under moderate heterogeneity ($\Delta\pi \leq 0.10$), methods converge ($p > 0.05$; Table~\ref{tab:main_supp}).
45	EC-HTE requires $n_{\text{expert}} \geq 250$ ($K{=}2$) or $\geq 500$ ($K{=}4$); below this, RMSE exceeds global (Figure~\ref{fig:budget_compact}; HB vs.\ stratified MLE budget sensitivity in Appendix~\ref{app:budget_sensitivity}; $K{=}8$ analysis in Appendix~\ref{app:k8_subgroups}).
46	
47	\paragraph{CausalForest.}
48	CausalForest~\cite{wager2018causal} with a noisy $\hat{Z}$ inherits the same $M_{\text{global}}^{-1} M_s$ structure.
49	EC-HTE reduces $|\text{bias}|$ from 0.191 to 0.039 (4.9$\times$) with coverage 0.90 ($K{=}4$, $n{=}500$; oracle coverage decomposition in Appendix~\ref{app:cf_oracle}); R-learner yields comparable reduction (89\%, Appendix~\ref{app:rlearner}), confirming the bias arises from the confusion matrix structure, not the downstream estimator.
50	
51	\paragraph{PPCI composition.}
52	When both the effect modifier and the outcome are LLM-annotated, EC-HTE (covariate correction) composes with PPCI~\cite{sui2026ppci} (outcome correction).
53	Under joint misclassification, EC-HTE+PPCI reduces $|\text{bias}|$ from 0.179 (naive) to 0.007, compared to 0.092 for PPCI alone and 0.064 for EC-HTE alone, with coverage $\geq$94\% (Appendix~\ref{sec:ppci}).
54	The composition is valid when covariate and outcome errors are independent; practitioners should verify this when both variables are LLM-annotated.
55	
56	\begin{table}[t]
57	\centering
58	\caption{Main results (extreme heterogeneity). Metrics averaged over subgroups, $z$-levels, 100 MC runs. Bold: lowest $|\text{bias}|$. $^\dagger$RMSE exceeds Global. F-L Scalar/Per-sub.: \citet{frazis2003estimating}. Moderate/TweetEval in Table~\ref{tab:main_supp}; MC SEs $\leq 0.005$ (Appendix~\ref{app:mcse}).\protect\footnotemark}
59	\label{tab:main_results}
60	\resizebox{\columnwidth}{!}{%
61	\begin{tabular}{ll ccc}
62	\toprule
63	Configuration & Method & $|\text{Bias}|$ & RMSE & 95\% CI Cov. \\
64	\midrule
65	\multirow{6}{*}{\shortstack[l]{DIM\\$K{=}2$, $n{=}250$}}
66	 & Naive & 0.058 & 0.090 & 0.82 \\
67	 & Global & 0.059 & 0.099 & 0.87 \\
68	 & F-L Scalar & 0.122 & 0.159 & 0.68 \\
69	 & F-L Per-sub. & 0.168 & 0.220 & 0.65 \\
70	 & Strat.\ MLE & 0.012 & 0.094 & 0.95 \\
71	 & HB EC-HTE & \textbf{0.008} & 0.089 & 0.94 \\
72	\midrule
73	\multirow{4}{*}{\shortstack[l]{DIM\\$K{=}4$, $n{=}500$}}
74	 & Naive & 0.062 & 0.113 & 0.88 \\
75	 & Global & 0.056 & 0.125 & 0.91 \\
76	 & Strat.\ MLE & \textbf{0.010} & 0.127$^\dagger$ & 0.95 \\
77	 & HB EC-HTE & 0.012 & 0.120 & 0.96 \\
78	\midrule
79	\multirow{3}{*}{\shortstack[l]{CausalForest\\$K{=}4$, $n{=}500$}}
80	 & Naive & 0.208 & 0.231 & 0.44 \\
81	 & Global & 0.191 & 0.244 & 0.58 \\
82	 & EC-HTE Forest & \textbf{0.039} & 0.180 & 0.90 \\
83	\bottomrule
84	\end{tabular}}
85	\footnotetext{CausalForest plug-in SE achieves 93.8\% aggregate coverage; a bootstrap procedure ($B{=}100$) recovers $\geq$95\% coverage at all budgets tested (Appendix~\ref{app:bootstrap_se}).}
86	\end{table}
87	
88	\subsection{Diagnostic and Operating Conditions}
89	\label{sec:diagnostic}
90	
91	Theorem~\ref{thm:bias_identity} operates on the full matrix residual $B_s = M_{\text{global}}^{-1} M_s - I$; the scalar diagnostic below is its (A2)-simplified form.
92	Proposition~\ref{prop:debiasing_hurts} provides a $\Delta\tau$-free diagnostic: global correction increases bias in subgroup $s$ iff $|\delta_s| / ((1-2\bar{\pi}) \cdot \pi_s) > 1$, computable from a pilot sample without estimating treatment effects (AUC $= 0.86$ symmetric, $0.96$ asymmetric; ROC curves in Appendix~\ref{app:roc}; screening details in Appendix~\ref{app:screening}).
93	Under relaxed screening, 79\% of real LLM--dataset pairs show RMSE improvement with coverage $\geq$93\% (Appendix~\ref{app:screening}).
94	
95	\paragraph{Operating conditions.}
96	EC-HTE requires: (i)~$\Delta\pi > 0.15$, (ii)~$n_{\text{expert}} \geq 250$ for $K{=}2$, (iii)~FNR${}<0.50$, (iv)~$K \leq 4$, and (v)~$n_{\text{expert}} \geq 500$ under asymmetric errors (FPR$\neq$FNR); when unmet, global correction is preferable (Appendix~\ref{app:k8_subgroups}).
97	Robustness checks (noisy labels, confounded treatment assignment (Appendix~\ref{app:confounded_dgp}), joint assumption violations) appear in Appendices~\ref{app:robustness}--\ref{app:multilm}.
98	Across 11 real LLM--dataset combinations (eight LLMs including GPT-4.1, Claude 3.5, Gemini 2.5 Flash, and five open-source models; Appendix~\ref{app:multilm_opensource}), the bias identity achieves aggregate $R^2 = 0.975$ (per-model range 0.76--0.99), and EC-HTE improves RMSE over global correction in 79\% of screening configurations with coverage $\geq$93\%.
99	
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2b88592-3f43-4c6d-81dd-68f0e04fe1b1",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "85e96cc3-929a-4c77-955b-0ec4764afe33",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_budget_compact.pdf}\n\\caption{RMSE vs.\\ expert budget under extreme heterogeneity. Crossover at $n{=}250$ ($K{=}2$) and $n{=}1000$ ($K{=}4$, $\\Delta\\tau{=}0.3$); under the Table~\\ref{tab:main_results} DGP, $K{=}4$ crossover is lower ($n{\\approx}500$). Shaded bands: $\\pm 1$ SD. Full grid in Appendix~\\ref{app:budget}.}\n\\label{fig:budget_compact}\n\\end{figure}\n\n\\subsection{Setup}\n\nWe test on synthetic ($N{=}5{,}000$, $K \\in \\{2, 4\\}$, controlled $\\Delta\\tau$ and $\\Delta\\pi$, 100 Monte Carlo (MC) runs) and semi-synthetic data-generating processes (DGPs) spanning four NLP tasks---sentiment analysis (TweetEval~\\cite{barbieri2020tweeteval}, $K{=}4$), hate speech detection (CivilComments, $K{=}4$), stance detection ($K{=}5$; Appendix~\\ref{app:stance}), and topic classification (AG News, $K{=}4$; Appendix~\\ref{app:agnews})---with full specifications in Appendix~\\ref{app:dgp}.\n\nWe compare: (1) \\textit{Naive} (no correction), (2) \\textit{Global} (pooled confusion matrix, equivalent to PPI/DSL~\\cite{angelopoulos2023ppi,egami2023dsl} with homogeneous error), (3) \\textit{Stratified MLE} (per-subgroup DSL without shrinkage), (4) \\textit{HB EC-HTE} (per-subgroup correction), (5) \\textit{PPCI}~\\cite{sui2026ppci}, and (6) \\textit{EC-HTE+PPCI}.\nFor CausalForest~\\cite{wager2018causal}, we compare naive, global, and EC-HTE variants.\nPrimary metrics are $|\\text{bias}|$, root mean squared error (RMSE), and 95\\% confidence interval (CI) coverage, averaged across subgroups and 100 MC runs.\nRobustness validations cover eight conditions including asymmetric errors, subgroup misspecification, and treatment-dependent misclassification (all $\\geq$89.5\\% coverage; Appendices~\\ref{app:hatespeech}--\\ref{app:treatment_dep}).\nSemi-synthetic evaluation uses empirical confusion matrices from 11 LLM--dataset combinations (eight LLMs across two datasets; Appendix~\\ref{app:realcm_bias}; semi-real CM validation in Appendix~\\ref{app:semireal}; open-source LLM validation in Appendix~\\ref{app:multilm_opensource}).\n\n\\subsection{Empirical Validation of the Bias Identity}\n\\label{sec:bias_mechanism}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig2_heatmap.pdf}\n\\caption{Bias amplification under global correction ($K{=}2$). (a)~High-error subgroup ($\\pi_s > \\bar{\\pi}$): correction always reduces bias. (b)~Low-error subgroup ($\\pi_s < \\bar{\\pi}$): correction \\emph{increases} bias when $\\Delta\\pi > 0.12$ (hatched), reaching $2.86\\times$.}\n\\label{fig:heatmap}\n\\end{figure*}\n\nWe verify Theorem~\\ref{thm:bias_identity} on a $K{=}2$ grid (520 configurations, $\\Delta\\pi \\in [0, 0.25]$, $\\Delta\\tau \\in (0, 0.50]$) and a $K{=}4$ grid (Appendix~\\ref{app:dgp}).\nRegressing observed subgroup bias on $\\delta_s \\cdot \\Delta\\tau / (1{-}2\\bar{\\pi})$ yields $R^2 = 0.994$ ($K{=}2$) and $0.97$ ($K{=}4$); residual variance reflects MC noise ($R^2 \\geq 0.976$ even at $P(Z{=}1) = 0.1$; Appendix~\\ref{app:classimbalance}).\nGlobal correction worsens bias in 50\\% of $K{=}2$ configurations (260/520, excluding $\\Delta\\pi{=}0$), with amplification reaching 2.86$\\times$ ($K{=}2$) and 2.41$\\times$ ($K{=}4$); Figure~\\ref{fig:heatmap} visualizes the amplification surface.\nGlobal correction also reverses the sign of estimated CATE in 14.9\\% of configurations at $\\tau(0) = 0.03$, with all eight real LLMs amplifying bias; EC-HTE eliminates sign reversal (Figure~\\ref{fig:sign_reversal}; Appendix~\\ref{app:policy_reversal}).\nCross-task validation on stance detection ($K{=}5$, Appendix~\\ref{app:stance}) confirms sign reversal (13.3\\% $\\to$ 3.3\\%) and reveals limitations when FNR${}>0.50$.\nOn CivilComments hate speech detection (Appendix~\\ref{app:civilcomments}), the bias identity changes the substantive NLP conclusion: global correction suggests demographic-group moderation effects are uniformly small, while EC-HTE reveals a 3.2$\\times$ effect-size gap between identity subgroups---consistent with known annotation disparities~\\cite{borkan2019nuanced} (Appendix~\\ref{app:hatespeech}).\nResearchers using global correction would miss this differential impact entirely.\n\n\\subsection{Correction Evaluation}\n\\label{sec:ec_hte_eval}\n\nTable~\\ref{tab:main_results} presents the main results.\nIn the $K{=}2$ extreme row, global correction \\emph{increases} $|\\text{bias}|$ relative to naive (0.059 vs.\\ 0.058), confirming Theorem~\\ref{thm:bias_identity}; F-L corrections fare worse (0.122--0.168).\nHB EC-HTE reduces $|\\text{bias}|$ from 0.059 to 0.008 (7.4$\\times$); relative to stratified MLE (0.012), the advantage is 1.5$\\times$ with lower RMSE from partial pooling. At $K{=}4$, bias reduces from 0.056 to 0.012 (4.7$\\times$), maintaining near-nominal coverage (0.94--0.96).\nUnder moderate heterogeneity ($\\Delta\\pi \\leq 0.10$), methods converge ($p > 0.05$; Table~\\ref{tab:main_supp}).\nEC-HTE requires $n_{\\text{expert}} \\geq 250$ ($K{=}2$) or $\\geq 500$ ($K{=}4$); below this, RMSE exceeds global (Figure~\\ref{fig:budget_compact}; HB vs.\\ stratified MLE budget sensitivity in Appendix~\\ref{app:budget_sensitivity}; $K{=}8$ analysis in Appendix~\\ref{app:k8_subgroups}).\n\n\\paragraph{CausalForest.}\nCausalForest~\\cite{wager2018causal} with a noisy $\\hat{Z}$ inherits the same $M_{\\text{global}}^{-1} M_s$ structure.\nEC-HTE reduces $|\\text{bias}|$ from 0.191 to 0.039 (4.9$\\times$) with coverage 0.90 ($K{=}4$, $n{=}500$; oracle coverage decomposition in Appendix~\\ref{app:cf_oracle}); R-learner yields comparable reduction (89\\%, Appendix~\\ref{app:rlearner}), confirming the bias arises from the confusion matrix structure, not the downstream estimator.\n\n\\paragraph{PPCI composition.}\nWhen both the effect modifier and the outcome are LLM-annotated, EC-HTE (covariate correction) composes with PPCI~\\cite{sui2026ppci} (outcome correction).\nUnder joint misclassification, EC-HTE+PPCI reduces $|\\text{bias}|$ from 0.179 (naive) to 0.007, compared to 0.092 for PPCI alone and 0.064 for EC-HTE alone, with coverage $\\geq$94\\% (Appendix~\\ref{sec:ppci}).\nThe composition is valid when covariate and outcome errors are independent; practitioners should verify this when both variables are LLM-annotated.\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results (extreme heterogeneity). Metrics averaged over subgroups, $z$-levels, 100 MC runs. Bold: lowest $|\\text{bias}|$. $^\\dagger$RMSE exceeds Global. F-L Scalar/Per-sub.: \\citet{frazis2003estimating}. Moderate/TweetEval in Table~\\ref{tab:main_supp}; MC SEs $\\leq 0.005$ (Appendix~\\ref{app:mcse}).\\protect\\footnotemark}\n\\label{tab:main_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll ccc}\n\\toprule\nConfiguration & Method & $|\\text{Bias}|$ & RMSE & 95\\% CI Cov. \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{DIM\\\\$K{=}2$, $n{=}250$}}\n & Naive & 0.058 & 0.090 & 0.82 \\\\\n & Global & 0.059 & 0.099 & 0.87 \\\\\n & F-L Scalar & 0.122 & 0.159 & 0.68 \\\\\n & F-L Per-sub. & 0.168 & 0.220 & 0.65 \\\\\n & Strat.\\ MLE & 0.012 & 0.094 & 0.95 \\\\\n & HB EC-HTE & \\textbf{0.008} & 0.089 & 0.94 \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{DIM\\\\$K{=}4$, $n{=}500$}}\n & Naive & 0.062 & 0.113 & 0.88 \\\\\n & Global & 0.056 & 0.125 & 0.91 \\\\\n & Strat.\\ MLE & \\textbf{0.010} & 0.127$^\\dagger$ & 0.95 \\\\\n & HB EC-HTE & 0.012 & 0.120 & 0.96 \\\\\n\\midrule\n\\multirow{3}{*}{\\shortstack[l]{CausalForest\\\\$K{=}4$, $n{=}500$}}\n & Naive & 0.208 & 0.231 & 0.44 \\\\\n & Global & 0.191 & 0.244 & 0.58 \\\\\n & EC-HTE Forest & \\textbf{0.039} & 0.180 & 0.90 \\\\\n\\bottomrule\n\\end{tabular}}\n\\footnotetext{CausalForest plug-in SE achieves 93.8\\% aggregate coverage; a bootstrap procedure ($B{=}100$) recovers $\\geq$95\\% coverage at all budgets tested (Appendix~\\ref{app:bootstrap_se}).}\n\\end{table}\n\n\\subsection{Diagnostic and Operating Conditions}\n\\label{sec:diagnostic}\n\nTheorem~\\ref{thm:bias_identity} operates on the full matrix residual $B_s = M_{\\text{global}}^{-1} M_s - I$; the scalar diagnostic below is its (A2)-simplified form.\nProposition~\\ref{prop:debiasing_hurts} provides a $\\Delta\\tau$-free diagnostic: global correction increases bias in subgroup $s$ iff $|\\delta_s| / ((1-2\\bar{\\pi}) \\cdot \\pi_s) > 1$, computable from a pilot sample without estimating treatment effects (AUC $= 0.86$ symmetric, $0.96$ asymmetric; ROC curves in Appendix~\\ref{app:roc}; screening details in Appendix~\\ref{app:screening}).\nUnder relaxed screening, 79\\% of real LLM--dataset pairs show RMSE improvement with coverage $\\geq$93\\% (Appendix~\\ref{app:screening}).\n\n\\paragraph{Operating conditions.}\nEC-HTE requires: (i)~$\\Delta\\pi > 0.15$, (ii)~$n_{\\text{expert}} \\geq 250$ for $K{=}2$, (iii)~FNR${}<0.50$, (iv)~$K \\leq 4$, and (v)~$n_{\\text{expert}} \\geq 500$ under asymmetric errors (FPR$\\neq$FNR); when unmet, global correction is preferable (Appendix~\\ref{app:k8_subgroups}).\nRobustness checks (noisy labels, confounded treatment assignment (Appendix~\\ref{app:confounded_dgp}), joint assumption violations) appear in Appendices~\\ref{app:robustness}--\\ref{app:multilm}.\nAcross 11 real LLM--dataset combinations (eight LLMs including GPT-4.1, Claude 3.5, Gemini 2.5 Flash, and five open-source models; Appendix~\\ref{app:multilm_opensource}), the bias identity achieves aggregate $R^2 = 0.975$ (per-model range 0.76--0.99), and EC-HTE improves RMSE over global correction in 79\\% of screening configurations with coverage $\\geq$93\\%.\n\n",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 100
    }
  },
  "sourceToolAssistantUUID": "c2b88592-3f43-4c6d-81dd-68f0e04fe1b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-25T16:32:20.614Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QWoZ31joqTMymuaLvgkCsv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85e96cc3-929a-4c77-955b-0ec4764afe33",
  "isSidechain": false,
  "requestId": "req_011CbPcCYVJ11TR53k96opLE",
  "type": "assistant",
  "uuid": "dce49730-b414-4827-b9cb-ba5f0199fc01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ya9ZTuvVZrZFRCAzFdmvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 38858,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 38858,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-25T16:32:20.624Z_

<details><summary>↩ Tool result · `toolu_01QWoZ31joqTMymuaLvgkCsv`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	Classical measurement error correction can amplify MSE under misspecification~\cite{fuller1987measurement,carroll2006measurement}; \citet{frazis2003estimating} derive scalar attenuation for homogeneous errors, which Theorem~\ref{thm:bias_identity} generalizes to heterogeneous settings.
5	HTE estimators~\cite{athey2016recursive,wager2018causal,chernozhukov2018dml} assume error-free covariates; LLM error rates vary by up to $5\times$ across subgroups~\cite{ashwin2025bias}.
6	PPI~\cite{angelopoulos2023ppi}, DSL~\cite{egami2023dsl}, PPCI~\cite{sui2026ppci}, and ForestIV~\cite{bu2023forestiv} correct population-level or outcome-side error assuming homogeneous prediction quality; none addresses effect modifier misclassification.
7	Extended discussion appears in Appendix~\ref{app:related}.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dce49730-b414-4827-b9cb-ba5f0199fc01",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "3459384d-d1ec-47b3-adb2-831e98af2285",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\nClassical measurement error correction can amplify MSE under misspecification~\\cite{fuller1987measurement,carroll2006measurement}; \\citet{frazis2003estimating} derive scalar attenuation for homogeneous errors, which Theorem~\\ref{thm:bias_identity} generalizes to heterogeneous settings.\nHTE estimators~\\cite{athey2016recursive,wager2018causal,chernozhukov2018dml} assume error-free covariates; LLM error rates vary by up to $5\\times$ across subgroups~\\cite{ashwin2025bias}.\nPPI~\\cite{angelopoulos2023ppi}, DSL~\\cite{egami2023dsl}, PPCI~\\cite{sui2026ppci}, and ForestIV~\\cite{bu2023forestiv} correct population-level or outcome-side error assuming homogeneous prediction quality; none addresses effect modifier misclassification.\nExtended discussion appears in Appendix~\\ref{app:related}.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "dce49730-b414-4827-b9cb-ba5f0199fc01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-25T16:32:21.106Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Mp3RNfNhaouxrMEBZNAqpm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3459384d-d1ec-47b3-adb2-831e98af2285",
  "isSidechain": false,
  "requestId": "req_011CbPcCYVJ11TR53k96opLE",
  "type": "assistant",
  "uuid": "049bfcb2-c6e6-4a64-be14-257c1c4fc426",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ya9ZTuvVZrZFRCAzFdmvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 38858,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 38858,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-25T16:32:21.111Z_

<details><summary>↩ Tool result · `toolu_01Mp3RNfNhaouxrMEBZNAqpm`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Standard confusion-matrix correction can reverse causal conclusions when misclassification rates vary across subgroups.
4	We derived an exact bias identity ($R^2 \geq 0.97$) that yields a diagnostic for flagging harmful correction and prescribes per-subgroup correction when $\Delta\pi > 0.15$ and $n_{\text{expert}} \geq 250$, validated across 11 LLM--dataset combinations spanning eight LLMs and four NLP tasks.
5	For practitioners, we recommend a three-step protocol: (1)~estimate per-subgroup error rates from a pilot sample; (2)~apply the diagnostic (Proposition~\ref{prop:debiasing_hurts}) to identify subgroups where global correction would increase bias; (3)~if $\Delta\pi > 0.15$ and the expert budget exceeds 250 labels, apply per-subgroup correction via EC-HTE.
6	When these conditions are not met, global correction remains appropriate---the diagnostic explicitly guards against inappropriate application.
7	The framework is task-agnostic and composes with prediction-powered inference.
8	
9	More broadly, as LLM annotation becomes standard practice in computational social science, the gap between average accuracy and subgroup-level reliability will grow with the diversity of populations studied.
10	Our bias identity provides a principled lens for auditing any pipeline that feeds machine-generated labels into downstream causal analysis; complementarity with LLM calibration is explored in Appendix~\ref{app:calibration}.
11	The identity applies beyond NLP to any setting where a noisy classifier defines treatment effect heterogeneity.
12	Future directions include continuous covariates, larger $K$, and joint covariate--outcome correction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "049bfcb2-c6e6-4a64-be14-257c1c4fc426",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "54c709e6-453b-428c-a45b-0b7cf17ea2cf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nStandard confusion-matrix correction can reverse causal conclusions when misclassification rates vary across subgroups.\nWe derived an exact bias identity ($R^2 \\geq 0.97$) that yields a diagnostic for flagging harmful correction and prescribes per-subgroup correction when $\\Delta\\pi > 0.15$ and $n_{\\text{expert}} \\geq 250$, validated across 11 LLM--dataset combinations spanning eight LLMs and four NLP tasks.\nFor practitioners, we recommend a three-step protocol: (1)~estimate per-subgroup error rates from a pilot sample; (2)~apply the diagnostic (Proposition~\\ref{prop:debiasing_hurts}) to identify subgroups where global correction would increase bias; (3)~if $\\Delta\\pi > 0.15$ and the expert budget exceeds 250 labels, apply per-subgroup correction via EC-HTE.\nWhen these conditions are not met, global correction remains appropriate---the diagnostic explicitly guards against inappropriate application.\nThe framework is task-agnostic and composes with prediction-powered inference.\n\nMore broadly, as LLM annotation becomes standard practice in computational social science, the gap between average accuracy and subgroup-level reliability will grow with the diversity of populations studied.\nOur bias identity provides a principled lens for auditing any pipeline that feeds machine-generated labels into downstream causal analysis; complementarity with LLM calibration is explored in Appendix~\\ref{app:calibration}.\nThe identity applies beyond NLP to any setting where a noisy classifier defines treatment effect heterogeneity.\nFuture directions include continuous covariates, larger $K$, and joint covariate--outcome correction.",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  },
  "sourceToolAssistantUUID": "049bfcb2-c6e6-4a64-be14-257c1c4fc426",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-25T16:32:21.577Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HvR8pY1mePfv9HG3FJH7sZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54c709e6-453b-428c-a45b-0b7cf17ea2cf",
  "isSidechain": false,
  "requestId": "req_011CbPcCYVJ11TR53k96opLE",
  "type": "assistant",
  "uuid": "aa0b0265-7b51-433a-8655-395754c42eed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ya9ZTuvVZrZFRCAzFdmvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 38858,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 38858,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-25T16:32:21.581Z_

<details><summary>↩ Tool result · `toolu_01HvR8pY1mePfv9HG3FJH7sZ`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Per-subgroup correction requires sufficient expert labels ($n_{\text{expert}} \geq 250$ for $K{=}2$, $\geq 500$ for $K{=}4$) and moderate classifier accuracy ($\text{FPR}_s, \text{FNR}_s < 0.5$); at $K{=}8$, RMSE exceeds global correction under fixed expert budget (Appendix~\ref{app:k8_subgroups}).
5	Assumption~(A3) requires balanced effect modifier prevalence; under class imbalance ($P(Z{=}1) = 0.1$), the identity remains exact ($R^2 \geq 0.976$) but EC-HTE's RMSE advantage narrows (ratio 1.06--1.68; Appendix~\ref{app:classimbalance}).
6	Assumption~(A1)---conditional independence of misclassification and potential outcomes---is not empirically testable; sensitivity analysis shows robustness up to $\gamma_T \leq 0.05$ for treatment-dependent misclassification (coverage $\geq$89.7\%; Appendix~\ref{app:treatment_dep}).
7	Ground-truth subgroup CATEs are unavailable in public datasets---classic causal inference benchmarks lack the LLM annotation step that creates the measurement error we address---so all evaluations use synthetic CATE injection on real text features and real LLM annotations (Appendices~\ref{app:dgp},~\ref{app:multilm}).
8	When LLMs annotate both the effect modifier and the outcome variable, covariate-side and outcome-side misclassification errors may be correlated, violating the independence structure assumed by combining EC-HTE with post-prediction causal inference (PPCI) frameworks~\cite{sui2026ppci}; practitioners should verify error independence or apply joint correction when both variables are LLM-annotated.
9	
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa0b0265-7b51-433a-8655-395754c42eed",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "2919d467-d7b1-4229-8e2a-80d0b78f1d88",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex",
      "content": "\\section*{Limitations}\n\\label{sec:limitations}\n\nPer-subgroup correction requires sufficient expert labels ($n_{\\text{expert}} \\geq 250$ for $K{=}2$, $\\geq 500$ for $K{=}4$) and moderate classifier accuracy ($\\text{FPR}_s, \\text{FNR}_s < 0.5$); at $K{=}8$, RMSE exceeds global correction under fixed expert budget (Appendix~\\ref{app:k8_subgroups}).\nAssumption~(A3) requires balanced effect modifier prevalence; under class imbalance ($P(Z{=}1) = 0.1$), the identity remains exact ($R^2 \\geq 0.976$) but EC-HTE's RMSE advantage narrows (ratio 1.06--1.68; Appendix~\\ref{app:classimbalance}).\nAssumption~(A1)---conditional independence of misclassification and potential outcomes---is not empirically testable; sensitivity analysis shows robustness up to $\\gamma_T \\leq 0.05$ for treatment-dependent misclassification (coverage $\\geq$89.7\\%; Appendix~\\ref{app:treatment_dep}).\nGround-truth subgroup CATEs are unavailable in public datasets---classic causal inference benchmarks lack the LLM annotation step that creates the measurement error we address---so all evaluations use synthetic CATE injection on real text features and real LLM annotations (Appendices~\\ref{app:dgp},~\\ref{app:multilm}).\nWhen LLMs annotate both the effect modifier and the outcome variable, covariate-side and outcome-side misclassification errors may be correlated, violating the independence structure assumed by combining EC-HTE with post-prediction causal inference (PPCI) frameworks~\\cite{sui2026ppci}; practitioners should verify error independence or apply joint correction when both variables are LLM-annotated.\n\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "aa0b0265-7b51-433a-8655-395754c42eed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-25T16:32:22.055Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KBPB3rC8mWnsnp8UALoxH5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2919d467-d7b1-4229-8e2a-80d0b78f1d88",
  "isSidechain": false,
  "requestId": "req_011CbPcCYVJ11TR53k96opLE",
  "type": "assistant",
  "uuid": "d9548461-7665-482e-b027-daf8bb7a4747",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ya9ZTuvVZrZFRCAzFdmvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 38858,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 38858,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-25T16:32:22.062Z_

<details><summary>↩ Tool result · `toolu_01KBPB3rC8mWnsnp8UALoxH5`</summary>

```text
1	% Requires preamble: \usepackage{amsthm,amsmath,amssymb}
2	% and: \newtheorem{theorem}{Theorem}
3	%      \newtheorem{corollary}[theorem]{Corollary}
4	%      \newtheorem{proposition}[theorem]{Proposition}
5	
6	\section{Bias Decomposition: When Debiasing Hurts}
7	\label{sec:theory}
8	
9	We formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.
10	Consider estimating the conditional average treatment effect (CATE) $\tau(z) = \mathbb{E}[Y(1) - Y(0) \mid Z = z]$, where $Z \in \{0, 1\}$ is a binary effect modifier observed only through a noisy annotation $\hat{Z}$.
11	The population consists of $K$ subgroups $S \in \{1, \ldots, K\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \times 2$ confusion matrix $C_s$ with symmetric error rate $\pi_s = P(\hat{Z} \neq Z \mid S{=}s)$.
12	Standard practice estimates a single confusion matrix $\bar{C} = \sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\bar{\pi} = \sum_s w_s \pi_s$.
13	We show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.
14	
15	We state five assumptions maintained throughout.
16	%
17	\begin{itemize}
18	\item[\textbf{(A1)}] \textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.
19	\item[\textbf{(A2)}] \textit{Symmetric misclassification (expository simplification):} $P(\hat{Z}{=}1 \mid Z{=}0, S{=}s) = P(\hat{Z}{=}0 \mid Z{=}1, S{=}s) = \pi_s$ for all $s$. Used only to reduce $[B_s]_{z,1}$ to the scalar $\pm\delta_s/(1{-}2\bar{\pi})$; the product-form identity holds for arbitrary asymmetric matrices without~(A2) (Remark~\ref{rem:asymmetric}).
20	\item[\textbf{(A3)}] \textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.
21	\item[\textbf{(A4)}] \textit{Non-degeneracy:} $\pi_s \neq 0.5$ for all $s$, ensuring each $C_s$ is invertible.
22	\item[\textbf{(A5)}] \textit{Homogeneous treatment effects across subgroups:} $\tau(z, s) = \tau(z)$ for all $s$, so $\Delta\tau = \tau(1) - \tau(0)$ is a scalar (relaxed to subgroup-specific $\Delta\tau_s$ in Proposition~\ref{prop:a5_relaxation}).
23	\end{itemize}
24	
25	Under (A2)--(A3), the Bayesian mixing matrix $M_s$ (entries $M_s[\hat{z}, z] = P(Z{=}z \mid \hat{Z}{=}\hat{z}, S{=}s)$) coincides with $C_s$.
26	The global mixing matrix is $M_{\text{global}} = \sum_s w_s M_s$.
27	
28	\begin{theorem}[Bias Decomposition Identity]
29	\label{thm:bias_identity}
30	Under \textnormal{(A1)--(A5)}, the bias of global correction in subgroup $s$ at effect-modifier level $z$ is
31	\begin{align}
32	\mathrm{bias}_{\mathrm{global}}(z{=}0, s) &= +\frac{\delta_s \cdot \Delta\tau}{1 - 2\bar{\pi}}, \label{eq:bias_z0} \\
33	\mathrm{bias}_{\mathrm{global}}(z{=}1, s) &= -\frac{\delta_s \cdot \Delta\tau}{1 - 2\bar{\pi}}, \label{eq:bias_z1}
34	\end{align}
35	where $\delta_s = \pi_s - \bar{\pi}$ is the subgroup deviation from the pooled error rate and $\Delta\tau = \tau(1) - \tau(0)$ is the CATE heterogeneity.
36	\end{theorem}
37	
38	Bias vanishes when either $\delta_s = 0$ (homogeneous errors) or $\Delta\tau = 0$ (no effect heterogeneity), and arises only through their interaction; $1/(1 - 2\bar{\pi})$ amplifies via matrix inversion.
39	The identity is correction-layer: it characterizes bias introduced by the correction step itself, trading attenuation from label noise for a new bias from error-rate heterogeneity. Propagation to downstream estimators is verified empirically (Section~\ref{sec:bias_mechanism}).
40	
41	\paragraph{Numerical example ($K{=}2$).}
42	Suppose two subgroups with $\pi_A = 0.05$, $\pi_B = 0.25$, giving $\bar{\pi} = 0.15$, and true CATEs $\tau(0) = 0.10$, $\tau(1) = 0.30$, so $\Delta\tau = 0.20$.
43	For subgroup $A$: $\delta_A = 0.05 - 0.15 = -0.10$, bias $= -0.10 \times 0.20 / 0.70 = -0.029$---global correction \emph{creates} bias in a subgroup where the naive estimator is nearly unbiased ($\pi_A = 0.05$).
44	For subgroup $B$: $\delta_B = +0.10$, bias $= +0.029$, partially offsetting attenuation. The opposite signs illustrate why aggregate metrics can mask subgroup-level harm.
45	
46	\paragraph{Proof sketch.}
47	Global correction applies $M_{\text{global}}^{-1}$ to the subgroup-specific observed CATE $\tau_{\text{obs}}(\cdot, s) = M_s \cdot \tau_{\text{true}}$, yielding bias $(M_{\text{global}}^{-1} M_s - I) \cdot \tau_{\text{true}}$.
48	Direct computation shows $M_{\text{global}}^{-1} M_s - I = \frac{\delta_s}{1-2\bar{\pi}} \bigl[\begin{smallmatrix} -1 & 1 \\ 1 & -1 \end{smallmatrix}\bigr]$.
49	Applying this matrix to $[\tau(0),\, \tau(1)]^\top$ produces the product form.
50	The full derivation appears in Appendix~\ref{app:derivation}.
51	Unlike Frazis--Loewenstein scalar attenuation~\citep{frazis2003estimating}, which uniformly shrinks estimates toward zero ($K{=}1$: $\delta_s \equiv 0$ recovers $\hat{\beta} = (1-2\pi)\beta$), the product form reveals that correction can \emph{reverse} bias sign across subgroups---a qualitatively new phenomenon from error-rate heterogeneity invisible to any global-scalar analysis (F-L increases $|\text{bias}|$ to $0.122$, $2.1\times$ naive; Table~\ref{tab:main_results}).
52	
53	\begin{remark}
54	\label{rem:asymmetric}
55	Theorem~\ref{thm:bias_identity} does not require assumption~(A2).
56	For arbitrary asymmetric confusion matrices where the false positive rate ($\mathrm{FPR}_s$) and false negative rate ($\mathrm{FNR}_s$) may differ,
57	the product form $\mathrm{bias}(z, s) = \Delta\tau \cdot [B_s]_{z,1}$ holds exactly,
58	where $B_s = M_{\mathrm{global}}^{-1} M_s - I$, because $B_s \mathbf{1} = \mathbf{0}$
59	follows from stochasticity of $M_s$ and $M_{\mathrm{global}}$ alone.
60	Assumption~(A2) simplifies $[B_s]_{z,1}$ to the scalar
61	$\pm \delta_s / (1 - 2\bar{\pi})$ but is not necessary for the product structure.
62	Under asymmetric errors, the scalar diagnostic (Proposition~\ref{prop:debiasing_hurts}) remains effective with $\pi_s = (\mathrm{FPR}_s + \mathrm{FNR}_s)/2$: the screening criterion achieves per-subgroup AUC $= 0.96$ across 48 asymmetric configurations (FPR/FNR ratios 1:5 to 5:1) and correctly identifies all harmed subgroups across 8 semi-real LLM confusion matrices (32 subgroups; Appendix~\ref{app:asymmetric}); end-to-end validation with asymmetric CMs appears in Appendix~\ref{app:asymmetric_endtoend}.
63	The criterion's validity extends beyond the symmetric case because the threshold $|\delta_s|/((1{-}2\bar{\pi})\pi_s) > 1$ is equivalent to $|B_s|/|D_s| > 1$ whenever subgroups have heterogeneous overall error rates.
64	\end{remark}
65	
66	\begin{proposition}[Exact Identity under Heterogeneous Treatment Effects]
67	\label{prop:a5_relaxation}
68	When $\tau(z, s)$ varies across subgroups (relaxing A5), the bias identity remains exact:
69	\begin{align}
70	\mathrm{bias}_{\mathrm{global}}(z{=}0, s) &= +\frac{\delta_s \cdot \Delta\tau_s}{1 - 2\bar{\pi}}, \label{eq:hetero_z0} \\
71	\mathrm{bias}_{\mathrm{global}}(z{=}1, s) &= -\frac{\delta_s \cdot \Delta\tau_s}{1 - 2\bar{\pi}}, \label{eq:hetero_z1}
72	\end{align}
73	where $\Delta\tau_s = \tau_s(1) - \tau_s(0)$ is the subgroup-specific CATE heterogeneity.
74	\end{proposition}
75	
76	\begin{corollary}[Aggregate Bias]
77	\label{cor:aggregate_bias}
78	The population-weighted aggregate bias is $\mathrm{Cov}_w(\pi_s, \Delta\tau_s) / (1 - 2\bar{\pi})$.
79	\end{corollary}
80	
81	The proof is immediate: $B_s$ depends only on confusion matrices, so the diagnostic extends unchanged and EC-HTE maintains $\geq$93\% coverage under both correlation signs (Appendix~\ref{app:a5_violation}).
82	
83	The identity extends to $K > 2$ with $J$ effect-modifier levels (Corollary~\ref{cor:multiclass}, Appendix~\ref{app:multiclass}).
84	Under class imbalance (relaxing A3), the identity remains exact with modified coefficients: $R^2 \geq 0.976$ and coverage $\geq$90\% even at $P(Z{=}1) = 0.1$ for $K{=}2$, though EC-HTE's RMSE ratio relative to global correction increases to 1.06--1.68 as imbalance grows (Appendix~\ref{app:classimbalance}).
85	Empirical verification yields $R^2 = 0.994$ ($K{=}2$) and $0.97$ ($K{=}4$; Section~\ref{sec:bias_mechanism}).
86	
87	\paragraph{Sensitivity to (A1).}
88	Assumption~(A1) is not empirically testable; if misclassification correlates with potential outcomes, Theorem~\ref{thm:bias_identity} gains an $O(\gamma)$ perturbation.
89	At $\gamma_T = 0.10$, coverage degrades to 75\% (Appendix~\ref{app:treatment_dep}); sensitivity analysis for outcome-dependent misclassification appears in Appendix~\ref{app:a1_sensitivity}. Sensitivity frameworks~\cite{lash2009applying,dorn2022sharp,cinelli2020making} can bound this.
90	
91	\paragraph{Finite-sample remainder.}
92	With estimated $\hat{C}_s = C_s + E_s$, $\|E_s\| = O_p(n_{\text{expert}}^{-1/2})$, the remainder is $R_n = O_p(n_{\text{expert}}^{-1/2} \cdot \kappa(C_s)^2)$, where the squared condition number arises from the Neumann expansion $\hat{C}_s^{-1} = C_s^{-1} - C_s^{-1} E_s C_s^{-1} + O(\|E_s\|^2)$, motivating the $\kappa$-guard in Section~\ref{sec:method}.
93	
94	\begin{proposition}[Debiasing Can Increase Bias]
95	\label{prop:debiasing_hurts}
96	Under \textnormal{(A1)--(A5)}, global correction produces larger absolute bias than the naive estimator ($|\mathrm{bias}_{\mathrm{global}}| > |\mathrm{bias}_{\mathrm{naive}}|$) in subgroup $s$ if and only if
97	\begin{equation}
98	\frac{|\delta_s|}{(1 - 2\bar{\pi}) \cdot \pi_s} > 1.
99	\label{eq:hurts_condition}
100	\end{equation}
101	\end{proposition}
102	
103	\medskip
104	Equation~\eqref{eq:hurts_condition} partitions subgroups into two regimes:
105	\begin{itemize}
106	    \item \textit{High-error} ($\pi_s > \bar{\pi}$): the condition reduces to $\pi_s > 0.5$, excluded by~(A4); global correction always reduces bias.
107	    \item \textit{Low-error} ($\pi_s < \bar{\pi}$): the condition holds whenever $\pi_s < \bar{\pi} / (2(1 - \bar{\pi}))$---easily satisfied: when $\bar{\pi} = 0.15$, any subgroup with $\pi_s < 0.088$ is harmed by global correction.
108	\end{itemize}
109	The mechanism is over-correction: for subgroups with near-zero misclassification ($\pi_s \approx 0$), the naive estimator is nearly unbiased, yet global inversion calibrated for $\bar{\pi}$ creates substantial bias---debiasing is worse than doing nothing, and can reverse bias sign across subgroups (proof in Appendix~\ref{app:debiasing_hurts}).
110	
111	In our experiments (Section~\ref{sec:bias_mechanism}), global correction increases bias in 50\% of $K{=}2$ configurations (260/520), with amplification reaching $2.86\times$ ($K{=}2$) and $2.41\times$ ($K{=}4$); Figure~\ref{fig:heatmap} visualizes the full parameter grid.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9548461-7665-482e-b027-daf8bb7a4747",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "66eeaadb-aab0-449d-abfb-f84a1605ddeb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
      "content": "% Requires preamble: \\usepackage{amsthm,amsmath,amssymb}\n% and: \\newtheorem{theorem}{Theorem}\n%      \\newtheorem{corollary}[theorem]{Corollary}\n%      \\newtheorem{proposition}[theorem]{Proposition}\n\n\\section{Bias Decomposition: When Debiasing Hurts}\n\\label{sec:theory}\n\nWe formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.\nConsider estimating the conditional average treatment effect (CATE) $\\tau(z) = \\mathbb{E}[Y(1) - Y(0) \\mid Z = z]$, where $Z \\in \\{0, 1\\}$ is a binary effect modifier observed only through a noisy annotation $\\hat{Z}$.\nThe population consists of $K$ subgroups $S \\in \\{1, \\ldots, K\\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \\times 2$ confusion matrix $C_s$ with symmetric error rate $\\pi_s = P(\\hat{Z} \\neq Z \\mid S{=}s)$.\nStandard practice estimates a single confusion matrix $\\bar{C} = \\sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\\bar{\\pi} = \\sum_s w_s \\pi_s$.\nWe show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.\n\nWe state five assumptions maintained throughout.\n%\n\\begin{itemize}\n\\item[\\textbf{(A1)}] \\textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.\n\\item[\\textbf{(A2)}] \\textit{Symmetric misclassification (expository simplification):} $P(\\hat{Z}{=}1 \\mid Z{=}0, S{=}s) = P(\\hat{Z}{=}0 \\mid Z{=}1, S{=}s) = \\pi_s$ for all $s$. Used only to reduce $[B_s]_{z,1}$ to the scalar $\\pm\\delta_s/(1{-}2\\bar{\\pi})$; the product-form identity holds for arbitrary asymmetric matrices without~(A2) (Remark~\\ref{rem:asymmetric}).\n\\item[\\textbf{(A3)}] \\textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.\n\\item[\\textbf{(A4)}] \\textit{Non-degeneracy:} $\\pi_s \\neq 0.5$ for all $s$, ensuring each $C_s$ is invertible.\n\\item[\\textbf{(A5)}] \\textit{Homogeneous treatment effects across subgroups:} $\\tau(z, s) = \\tau(z)$ for all $s$, so $\\Delta\\tau = \\tau(1) - \\tau(0)$ is a scalar (relaxed to subgroup-specific $\\Delta\\tau_s$ in Proposition~\\ref{prop:a5_relaxation}).\n\\end{itemize}\n\nUnder (A2)--(A3), the Bayesian mixing matrix $M_s$ (entries $M_s[\\hat{z}, z] = P(Z{=}z \\mid \\hat{Z}{=}\\hat{z}, S{=}s)$) coincides with $C_s$.\nThe global mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s$.\n\n\\begin{theorem}[Bias Decomposition Identity]\n\\label{thm:bias_identity}\nUnder \\textnormal{(A1)--(A5)}, the bias of global correction in subgroup $s$ at effect-modifier level $z$ is\n\\begin{align}\n\\mathrm{bias}_{\\mathrm{global}}(z{=}0, s) &= +\\frac{\\delta_s \\cdot \\Delta\\tau}{1 - 2\\bar{\\pi}}, \\label{eq:bias_z0} \\\\\n\\mathrm{bias}_{\\mathrm{global}}(z{=}1, s) &= -\\frac{\\delta_s \\cdot \\Delta\\tau}{1 - 2\\bar{\\pi}}, \\label{eq:bias_z1}\n\\end{align}\nwhere $\\delta_s = \\pi_s - \\bar{\\pi}$ is the subgroup deviation from the pooled error rate and $\\Delta\\tau = \\tau(1) - \\tau(0)$ is the CATE heterogeneity.\n\\end{theorem}\n\nBias vanishes when either $\\delta_s = 0$ (homogeneous errors) or $\\Delta\\tau = 0$ (no effect heterogeneity), and arises only through their interaction; $1/(1 - 2\\bar{\\pi})$ amplifies via matrix inversion.\nThe identity is correction-layer: it characterizes bias introduced by the correction step itself, trading attenuation from label noise for a new bias from error-rate heterogeneity. Propagation to downstream estimators is verified empirically (Section~\\ref{sec:bias_mechanism}).\n\n\\paragraph{Numerical example ($K{=}2$).}\nSuppose two subgroups with $\\pi_A = 0.05$, $\\pi_B = 0.25$, giving $\\bar{\\pi} = 0.15$, and true CATEs $\\tau(0) = 0.10$, $\\tau(1) = 0.30$, so $\\Delta\\tau = 0.20$.\nFor subgroup $A$: $\\delta_A = 0.05 - 0.15 = -0.10$, bias $= -0.10 \\times 0.20 / 0.70 = -0.029$---global correction \\emph{creates} bias in a subgroup where the naive estimator is nearly unbiased ($\\pi_A = 0.05$).\nFor subgroup $B$: $\\delta_B = +0.10$, bias $= +0.029$, partially offsetting attenuation. The opposite signs illustrate why aggregate metrics can mask subgroup-level harm.\n\n\\paragraph{Proof sketch.}\nGlobal correction applies $M_{\\text{global}}^{-1}$ to the subgroup-specific observed CATE $\\tau_{\\text{obs}}(\\cdot, s) = M_s \\cdot \\tau_{\\text{true}}$, yielding bias $(M_{\\text{global}}^{-1} M_s - I) \\cdot \\tau_{\\text{true}}$.\nDirect computation shows $M_{\\text{global}}^{-1} M_s - I = \\frac{\\delta_s}{1-2\\bar{\\pi}} \\bigl[\\begin{smallmatrix} -1 & 1 \\\\ 1 & -1 \\end{smallmatrix}\\bigr]$.\nApplying this matrix to $[\\tau(0),\\, \\tau(1)]^\\top$ produces the product form.\nThe full derivation appears in Appendix~\\ref{app:derivation}.\nUnlike Frazis--Loewenstein scalar attenuation~\\citep{frazis2003estimating}, which uniformly shrinks estimates toward zero ($K{=}1$: $\\delta_s \\equiv 0$ recovers $\\hat{\\beta} = (1-2\\pi)\\beta$), the product form reveals that correction can \\emph{reverse} bias sign across subgroups---a qualitatively new phenomenon from error-rate heterogeneity invisible to any global-scalar analysis (F-L increases $|\\text{bias}|$ to $0.122$, $2.1\\times$ naive; Table~\\ref{tab:main_results}).\n\n\\begin{remark}\n\\label{rem:asymmetric}\nTheorem~\\ref{thm:bias_identity} does not require assumption~(A2).\nFor arbitrary asymmetric confusion matrices where the false positive rate ($\\mathrm{FPR}_s$) and false negative rate ($\\mathrm{FNR}_s$) may differ,\nthe product form $\\mathrm{bias}(z, s) = \\Delta\\tau \\cdot [B_s]_{z,1}$ holds exactly,\nwhere $B_s = M_{\\mathrm{global}}^{-1} M_s - I$, because $B_s \\mathbf{1} = \\mathbf{0}$\nfollows from stochasticity of $M_s$ and $M_{\\mathrm{global}}$ alone.\nAssumption~(A2) simplifies $[B_s]_{z,1}$ to the scalar\n$\\pm \\delta_s / (1 - 2\\bar{\\pi})$ but is not necessary for the product structure.\nUnder asymmetric errors, the scalar diagnostic (Proposition~\\ref{prop:debiasing_hurts}) remains effective with $\\pi_s = (\\mathrm{FPR}_s + \\mathrm{FNR}_s)/2$: the screening criterion achieves per-subgroup AUC $= 0.96$ across 48 asymmetric configurations (FPR/FNR ratios 1:5 to 5:1) and correctly identifies all harmed subgroups across 8 semi-real LLM confusion matrices (32 subgroups; Appendix~\\ref{app:asymmetric}); end-to-end validation with asymmetric CMs appears in Appendix~\\ref{app:asymmetric_endtoend}.\nThe criterion's validity extends beyond the symmetric case because the threshold $|\\delta_s|/((1{-}2\\bar{\\pi})\\pi_s) > 1$ is equivalent to $|B_s|/|D_s| > 1$ whenever subgroups have heterogeneous overall error rates.\n\\end{remark}\n\n\\begin{proposition}[Exact Identity under Heterogeneous Treatment Effects]\n\\label{prop:a5_relaxation}\nWhen $\\tau(z, s)$ varies across subgroups (relaxing A5), the bias identity remains exact:\n\\begin{align}\n\\mathrm{bias}_{\\mathrm{global}}(z{=}0, s) &= +\\frac{\\delta_s \\cdot \\Delta\\tau_s}{1 - 2\\bar{\\pi}}, \\label{eq:hetero_z0} \\\\\n\\mathrm{bias}_{\\mathrm{global}}(z{=}1, s) &= -\\frac{\\delta_s \\cdot \\Delta\\tau_s}{1 - 2\\bar{\\pi}}, \\label{eq:hetero_z1}\n\\end{align}\nwhere $\\Delta\\tau_s = \\tau_s(1) - \\tau_s(0)$ is the subgroup-specific CATE heterogeneity.\n\\end{proposition}\n\n\\begin{corollary}[Aggregate Bias]\n\\label{cor:aggregate_bias}\nThe population-weighted aggregate bias is $\\mathrm{Cov}_w(\\pi_s, \\Delta\\tau_s) / (1 - 2\\bar{\\pi})$.\n\\end{corollary}\n\nThe proof is immediate: $B_s$ depends only on confusion matrices, so the diagnostic extends unchanged and EC-HTE maintains $\\geq$93\\% coverage under both correlation signs (Appendix~\\ref{app:a5_violation}).\n\nThe identity extends to $K > 2$ with $J$ effect-modifier levels (Corollary~\\ref{cor:multiclass}, Appendix~\\ref{app:multiclass}).\nUnder class imbalance (relaxing A3), the identity remains exact with modified coefficients: $R^2 \\geq 0.976$ and coverage $\\geq$90\\% even at $P(Z{=}1) = 0.1$ for $K{=}2$, though EC-HTE's RMSE ratio relative to global correction increases to 1.06--1.68 as imbalance grows (Appendix~\\ref{app:classimbalance}).\nEmpirical verification yields $R^2 = 0.994$ ($K{=}2$) and $0.97$ ($K{=}4$; Section~\\ref{sec:bias_mechanism}).\n\n\\paragraph{Sensitivity to (A1).}\nAssumption~(A1) is not empirically testable; if misclassification correlates with potential outcomes, Theorem~\\ref{thm:bias_identity} gains an $O(\\gamma)$ perturbation.\nAt $\\gamma_T = 0.10$, coverage degrades to 75\\% (Appendix~\\ref{app:treatment_dep}); sensitivity analysis for outcome-dependent misclassification appears in Appendix~\\ref{app:a1_sensitivity}. Sensitivity frameworks~\\cite{lash2009applying,dorn2022sharp,cinelli2020making} can bound this.\n\n\\paragraph{Finite-sample remainder.}\nWith estimated $\\hat{C}_s = C_s + E_s$, $\\|E_s\\| = O_p(n_{\\text{expert}}^{-1/2})$, the remainder is $R_n = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\kappa(C_s)^2)$, where the squared condition number arises from the Neumann expansion $\\hat{C}_s^{-1} = C_s^{-1} - C_s^{-1} E_s C_s^{-1} + O(\\|E_s\\|^2)$, motivating the $\\kappa$-guard in Section~\\ref{sec:method}.\n\n\\begin{proposition}[Debiasing Can Increase Bias]\n\\label{prop:debiasing_hurts}\nUnder \\textnormal{(A1)--(A5)}, global correction produces larger absolute bias than the naive estimator ($|\\mathrm{bias}_{\\mathrm{global}}| > |\\mathrm{bias}_{\\mathrm{naive}}|$) in subgroup $s$ if and only if\n\\begin{equation}\n\\frac{|\\delta_s|}{(1 - 2\\bar{\\pi}) \\cdot \\pi_s} > 1.\n\\label{eq:hurts_condition}\n\\end{equation}\n\\end{proposition}\n\n\\medskip\nEquation~\\eqref{eq:hurts_condition} partitions subgroups into two regimes:\n\\begin{itemize}\n    \\item \\textit{High-error} ($\\pi_s > \\bar{\\pi}$): the condition reduces to $\\pi_s > 0.5$, excluded by~(A4); global correction always reduces bias.\n    \\item \\textit{Low-error} ($\\pi_s < \\bar{\\pi}$): the condition holds whenever $\\pi_s < \\bar{\\pi} / (2(1 - \\bar{\\pi}))$---easily satisfied: when $\\bar{\\pi} = 0.15$, any subgroup with $\\pi_s < 0.088$ is harmed by global correction.\n\\end{itemize}\nThe mechanism is over-correction: for subgroups with near-zero misclassification ($\\pi_s \\approx 0$), the naive estimator is nearly unbiased, yet global inversion calibrated for $\\bar{\\pi}$ creates substantial bias---debiasing is worse than doing nothing, and can reverse bias sign across subgroups (proof in Appendix~\\ref{app:debiasing_hurts}).\n\nIn our experiments (Section~\\ref{sec:bias_mechanism}), global correction increases bias in 50\\% of $K{=}2$ configurations (260/520), with amplification reaching $2.86\\times$ ($K{=}2$) and $2.41\\times$ ($K{=}4$); Figure~\\ref{fig:heatmap} visualizes the full parameter grid.",
      "numLines": 111,
      "startLine": 1,
      "totalLines": 111
    }
  },
  "sourceToolAssistantUUID": "d9548461-7665-482e-b027-daf8bb7a4747",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-25T16:32:22.535Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BGGNjD1CkZAoPf2TPuwq8B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66eeaadb-aab0-449d-abfb-f84a1605ddeb",
  "isSidechain": false,
  "requestId": "req_011CbPcCYVJ11TR53k96opLE",
  "type": "assistant",
  "uuid": "687ec719-314e-430a-9da8-d5dcab67e040",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ya9ZTuvVZrZFRCAzFdmvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 38858,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 38858,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-25T16:32:22.544Z_

<details><summary>↩ Tool result · `toolu_01BGGNjD1CkZAoPf2TPuwq8B`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{makecell}
15	\usepackage{enumitem}
16	\usepackage{algorithm}
17	\usepackage{algpseudocode}
18	
19	\newtheorem{theorem}{Theorem}
20	\newtheorem{corollary}[theorem]{Corollary}
21	\newtheorem{proposition}[theorem]{Proposition}
22	\newtheorem{remark}[theorem]{Remark}
23	
24	\title{When Debiasing Hurts: An Exact Bias Identity\\for LLM-Annotated Treatment Effects}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	
35	\input{related_work}
36	
37	\input{theory}
38	
39	\input{method}
40	
41	\input{experiments}
42	
43	\input{conclusion}
44	
45	\input{limitations}
46	
47	\bibliography{references}
48	
49	\appendix
50	\input{appendix}
51	
52	%\input{checklist}
53	
54	\end{document}
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "687ec719-314e-430a-9da8-d5dcab67e040",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "6d636ce0-81b4-4fde-b647-d6aac77a0541",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{makecell}\n\\usepackage{enumitem}\n\\usepackage{algorithm}\n\\usepackage{algpseudocode}\n\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{corollary}[theorem]{Corollary}\n\\newtheorem{proposition}[theorem]{Proposition}\n\\newtheorem{remark}[theorem]{Remark}\n\n\\title{When Debiasing Hurts: An Exact Bias Identity\\\\for LLM-Annotated Treatment Effects}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{theory}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{conclusion}\n\n\\input{limitations}\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix}\n\n%\\input{checklist}\n\n\\end{document}\n",
      "numLines": 55,
      "startLine": 1,
      "totalLines": 55
    }
  },
  "sourceToolAssistantUUID": "687ec719-314e-430a-9da8-d5dcab67e040",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-25T16:32:23.077Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FiCAoWqufMe2U1gKGqByfx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d636ce0-81b4-4fde-b647-d6aac77a0541",
  "isSidechain": false,
  "requestId": "req_011CbPcCYVJ11TR53k96opLE",
  "type": "assistant",
  "uuid": "b5ddb718-f493-4a52-b543-105bac622813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ya9ZTuvVZrZFRCAzFdmvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 38858,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 38858,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-25T16:32:23.378Z_

<details><summary>↩ Tool result · reported error · `toolu_01FiCAoWqufMe2U1gKGqByfx`</summary>

```text
File content (42881 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5ddb718-f493-4a52-b543-105bac622813",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "770dd9b5-f05b-45c6-acad-930562bdb341",
  "toolUseResult": "Error: File content (42881 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "b5ddb718-f493-4a52-b543-105bac622813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-25T16:32:23.998Z_

<details open><summary>🔧 Tool call — Read · `toolu_0183ig8v78MDVgPYPGPuAExQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "770dd9b5-f05b-45c6-acad-930562bdb341",
  "isSidechain": false,
  "requestId": "req_011CbPcCYVJ11TR53k96opLE",
  "type": "assistant",
  "uuid": "4859cc74-6349-43bc-8877-1e2ca868f13c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ya9ZTuvVZrZFRCAzFdmvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 38858,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 38858,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-25T16:32:24.004Z_

<details><summary>↩ Tool result · `toolu_0183ig8v78MDVgPYPGPuAExQ`</summary>

```text
1	\subsection{Topic Classification: AG News Cross-Task Validation}
2	\label{app:agnews}
3	
4	To validate generalization beyond sentiment and toxicity, we extend the semi-synthetic evaluation to topic classification using AG News~\cite{zhang2015character}, binarized as Business/World ($Z{=}1$) vs.\ Sports/Sci-Tech ($Z{=}0$).
5	Confusion matrices are calibrated to match empirical LLM accuracy levels on AG News (${\sim}80\%$; \citealt{etaiwi2025comparative}), with per-subgroup error rates derived from reported per-class metrics; Business$\to$World is the dominant confusion direction.
6	Subgroups ($K{=}4$) are defined by article length $\times$ vocabulary complexity, with per-subgroup error rates reflecting text difficulty ($\bar{\pi} = 0.173$, $\Delta\pi = 0.19$).
7	CATE heterogeneity ranges from $\Delta\tau{=}0.10$ (short, simple) to $\Delta\tau{=}0.60$ (long, complex), with 100 MC replications.
8	
9	Table~\ref{tab:agnews_results} reports the main results.
10	EC-HTE reduces $|\text{bias}|$ by $1.9\times$ at $n_{\text{expert}}{=}1{,}000$ (0.015 vs.\ 0.028) with 94.9\% coverage.
11	At $n_{\text{expert}}{=}250$, EC-HTE incurs higher variance than global correction ($\text{RMSE}{=}0.182$ vs.\ $0.115$), consistent with the expert-budget operating condition ($n_{\text{expert}}/K{=}62.5$, near the threshold).
12	The asymmetric bias identity achieves $R^2 = 0.95$ ($0.93$--$0.97$ per budget level), confirming the product-form structure on a task with inherently asymmetric confusion matrices ($\text{FPR} \neq \text{FNR}$); the symmetric scalar approximation does not hold ($R^2 < 0$), consistent with Remark~\ref{rem:asymmetric} in Section~\ref{sec:theory}.
13	
14	\begin{table}[h]
15	\centering
16	\caption{AG News topic classification ($K{=}4$, $\Delta\pi{=}0.19$). Metrics averaged over subgroups, $z$-levels, 100 MC runs. Bold: lowest $|\text{bias}|$.}
17	\label{tab:agnews_results}
18	\small
19	\begin{tabular}{ll cccc}
20	\toprule
21	$n_{\text{expert}}$ & Method & $|\text{Bias}|$ & RMSE & 95\% CI Cov. & Asym.\ $R^2$ \\
22	\midrule
23	\multirow{4}{*}{250}
24	 & Naive & 0.067 & 0.109 & 0.84 & --- \\
25	 & Global & \textbf{0.027} & 0.115 & 0.94 & 0.93 \\
26	 & Strat.\ MLE & 0.034 & 0.181 & 0.89 & --- \\
27	 & HB EC-HTE & 0.035 & 0.182 & 0.89 & --- \\
28	\midrule
29	\multirow{4}{*}{500}
30	 & Naive & 0.067 & 0.109 & 0.84 & --- \\
31	 & Global & 0.028 & 0.110 & 0.94 & 0.96 \\
32	 & Strat.\ MLE & \textbf{0.022} & 0.147 & 0.92 & --- \\
33	 & HB EC-HTE & 0.022 & 0.147 & 0.92 & --- \\
34	\midrule
35	\multirow{4}{*}{1{,}000}
36	 & Naive & 0.067 & 0.109 & 0.84 & --- \\
37	 & Global & 0.028 & 0.109 & 0.94 & 0.97 \\
38	 & Strat.\ MLE & \textbf{0.015} & 0.126 & 0.95 & --- \\
39	 & HB EC-HTE & 0.015 & 0.126 & 0.95 & --- \\
40	\bottomrule
41	\end{tabular}
42	\end{table}
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4859cc74-6349-43bc-8877-1e2ca868f13c",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "8dd85220-186c-42d9-8f8b-e4e831fcbfc2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex",
      "content": "\\subsection{Topic Classification: AG News Cross-Task Validation}\n\\label{app:agnews}\n\nTo validate generalization beyond sentiment and toxicity, we extend the semi-synthetic evaluation to topic classification using AG News~\\cite{zhang2015character}, binarized as Business/World ($Z{=}1$) vs.\\ Sports/Sci-Tech ($Z{=}0$).\nConfusion matrices are calibrated to match empirical LLM accuracy levels on AG News (${\\sim}80\\%$; \\citealt{etaiwi2025comparative}), with per-subgroup error rates derived from reported per-class metrics; Business$\\to$World is the dominant confusion direction.\nSubgroups ($K{=}4$) are defined by article length $\\times$ vocabulary complexity, with per-subgroup error rates reflecting text difficulty ($\\bar{\\pi} = 0.173$, $\\Delta\\pi = 0.19$).\nCATE heterogeneity ranges from $\\Delta\\tau{=}0.10$ (short, simple) to $\\Delta\\tau{=}0.60$ (long, complex), with 100 MC replications.\n\nTable~\\ref{tab:agnews_results} reports the main results.\nEC-HTE reduces $|\\text{bias}|$ by $1.9\\times$ at $n_{\\text{expert}}{=}1{,}000$ (0.015 vs.\\ 0.028) with 94.9\\% coverage.\nAt $n_{\\text{expert}}{=}250$, EC-HTE incurs higher variance than global correction ($\\text{RMSE}{=}0.182$ vs.\\ $0.115$), consistent with the expert-budget operating condition ($n_{\\text{expert}}/K{=}62.5$, near the threshold).\nThe asymmetric bias identity achieves $R^2 = 0.95$ ($0.93$--$0.97$ per budget level), confirming the product-form structure on a task with inherently asymmetric confusion matrices ($\\text{FPR} \\neq \\text{FNR}$); the symmetric scalar approximation does not hold ($R^2 < 0$), consistent with Remark~\\ref{rem:asymmetric} in Section~\\ref{sec:theory}.\n\n\\begin{table}[h]\n\\centering\n\\caption{AG News topic classification ($K{=}4$, $\\Delta\\pi{=}0.19$). Metrics averaged over subgroups, $z$-levels, 100 MC runs. Bold: lowest $|\\text{bias}|$.}\n\\label{tab:agnews_results}\n\\small\n\\begin{tabular}{ll cccc}\n\\toprule\n$n_{\\text{expert}}$ & Method & $|\\text{Bias}|$ & RMSE & 95\\% CI Cov. & Asym.\\ $R^2$ \\\\\n\\midrule\n\\multirow{4}{*}{250}\n & Naive & 0.067 & 0.109 & 0.84 & --- \\\\\n & Global & \\textbf{0.027} & 0.115 & 0.94 & 0.93 \\\\\n & Strat.\\ MLE & 0.034 & 0.181 & 0.89 & --- \\\\\n & HB EC-HTE & 0.035 & 0.182 & 0.89 & --- \\\\\n\\midrule\n\\multirow{4}{*}{500}\n & Naive & 0.067 & 0.109 & 0.84 & --- \\\\\n & Global & 0.028 & 0.110 & 0.94 & 0.96 \\\\\n & Strat.\\ MLE & \\textbf{0.022} & 0.147 & 0.92 & --- \\\\\n & HB EC-HTE & 0.022 & 0.147 & 0.92 & --- \\\\\n\\midrule\n\\multirow{4}{*}{1{,}000}\n & Naive & 0.067 & 0.109 & 0.84 & --- \\\\\n & Global & 0.028 & 0.109 & 0.94 & 0.97 \\\\\n & Strat.\\ MLE & \\textbf{0.015} & 0.126 & 0.95 & --- \\\\\n & HB EC-HTE & 0.015 & 0.126 & 0.95 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  },
  "sourceToolAssistantUUID": "4859cc74-6349-43bc-8877-1e2ca868f13c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-25T16:32:24.409Z_

<details open><summary>🔧 Tool call — Read · `toolu_018do4eZ9pT93fYkwJtm7iqw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dd85220-186c-42d9-8f8b-e4e831fcbfc2",
  "isSidechain": false,
  "requestId": "req_011CbPcCYVJ11TR53k96opLE",
  "type": "assistant",
  "uuid": "2e742d4f-601c-436b-a885-484d9c800f0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ya9ZTuvVZrZFRCAzFdmvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 38858,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 38858,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
          },
          "type": "message"
        }
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

_source line 44 · 2026-05-25T16:32:24.416Z_

<details><summary>↩ Tool result · `toolu_018do4eZ9pT93fYkwJtm7iqw`</summary>

```text
1	\subsection{Stance Detection: Cross-Task Sign Reversal Validation}
2	\label{app:stance}
3	
4	To test whether global correction introduces sign reversals beyond sentiment and toxicity, we extend the semi-synthetic evaluation to stance detection using TweetEval~\cite{barbieri2020tweeteval}.
5	The binary label is \emph{favor} ($Z{=}1$) vs.\ \emph{not-favor} ($Z{=}0$) toward five stance targets (Atheism, Climate Change, Feminist Movement, Hillary Clinton, Abortion), yielding $K{=}5$ subgroups with $n{=}300$ each.
6	CATE heterogeneity is $\tau(\text{favor}){=}0.20$, $\tau(\text{not-favor}){=}0.05$, with 200 MC replications.
7	GPT-4o annotations are from the real API; GPT-4o-mini and GPT-3.5-Turbo use simulated error profiles (FPR/FNR scaling $+$ additive shift; see Appendix~\ref{app:dgp}).
8	
9	Table~\ref{tab:stance_signrev} reports subgroups with sign reversal or $\kappa > 3$.
10	Global correction produces sign reversals in 4/30 subgroup-$z$ combinations (13.3\%); EC-HTE reduces this to 1/30 (3.3\%); the remaining reversal occurs in an ill-conditioned subgroup ($\kappa{=}15.0$, GPT-3.5-Turbo Climate Change) that violates the operating conditions of Section~\ref{sec:ec_hte_eval}.
11	Global correction amplifies bias in 15/30 cases (50\%).
12	
13	The stance task exposes an operating-conditions limitation: GPT-3.5-Turbo achieves FNR ${>}\,0.50$ on all five targets, violating the classifier quality precondition and producing $\kappa$ values up to 15.0 (Climate Change) vs.\ 4.6 (Hillary Clinton)---a ${\sim}10{\times}$ range within the same LLM.
14	This $\kappa$ heterogeneity inflates correction variance; EC-HTE preserves sign correctness but at the cost of higher variance when $\kappa \gg 3$.
15	Mean RMSE: naive${=}0.116$, global${=}0.272$, EC-HTE${=}0.271$; correction reduces sign reversals but does not improve overall RMSE at $K{=}5$, $n{=}300$ per subgroup---consistent with the operating-conditions threshold ($n_{\text{expert}} \geq 250$ for $K{=}2$; Section~\ref{sec:diagnostic}).
16	Practitioners should verify per-subgroup FNR before applying correction.
17	
18	\begin{table}[h]
19	\centering
20	\caption{Stance detection: subgroups with sign reversal or $\kappa > 3$. \checkmark\ indicates at least one $z$-level affected. GPT-4o-mini and GPT-3.5-Turbo use simulated error profiles.}
21	\label{tab:stance_signrev}
22	\small
23	\begin{tabular}{llcccc}
24	\toprule
25	LLM & Target & $\kappa$ & \makecell{Sign Rev\\(Global)} & \makecell{Sign Rev\\(EC-HTE)} & \makecell{Bias Amp\\(Global)} \\
26	\midrule
27	GPT-4o & Fem.\ Mov.\ & 1.79 & \checkmark & --- & \checkmark \\
28	GPT-4o & Hillary C.\ & 1.86 & \checkmark & --- & \checkmark \\
29	\midrule
30	GPT-3.5-T & Atheism & 7.21 & --- & --- & --- \\
31	GPT-3.5-T & Climate Ch.\ & 15.01 & --- & \checkmark & \checkmark \\
32	GPT-3.5-T & Fem.\ Mov.\ & 3.28 & \checkmark & --- & \checkmark \\
33	GPT-3.5-T & Hillary C.\ & 4.60 & \checkmark & --- & \checkmark \\
34	GPT-3.5-T & Abortion & 14.17 & --- & --- & \checkmark \\
35	\bottomrule
36	\end{tabular}
37	\end{table}
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e742d4f-601c-436b-a885-484d9c800f0b",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "89980387-0335-4169-8cec-c86ab2b34787",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex",
      "content": "\\subsection{Stance Detection: Cross-Task Sign Reversal Validation}\n\\label{app:stance}\n\nTo test whether global correction introduces sign reversals beyond sentiment and toxicity, we extend the semi-synthetic evaluation to stance detection using TweetEval~\\cite{barbieri2020tweeteval}.\nThe binary label is \\emph{favor} ($Z{=}1$) vs.\\ \\emph{not-favor} ($Z{=}0$) toward five stance targets (Atheism, Climate Change, Feminist Movement, Hillary Clinton, Abortion), yielding $K{=}5$ subgroups with $n{=}300$ each.\nCATE heterogeneity is $\\tau(\\text{favor}){=}0.20$, $\\tau(\\text{not-favor}){=}0.05$, with 200 MC replications.\nGPT-4o annotations are from the real API; GPT-4o-mini and GPT-3.5-Turbo use simulated error profiles (FPR/FNR scaling $+$ additive shift; see Appendix~\\ref{app:dgp}).\n\nTable~\\ref{tab:stance_signrev} reports subgroups with sign reversal or $\\kappa > 3$.\nGlobal correction produces sign reversals in 4/30 subgroup-$z$ combinations (13.3\\%); EC-HTE reduces this to 1/30 (3.3\\%); the remaining reversal occurs in an ill-conditioned subgroup ($\\kappa{=}15.0$, GPT-3.5-Turbo Climate Change) that violates the operating conditions of Section~\\ref{sec:ec_hte_eval}.\nGlobal correction amplifies bias in 15/30 cases (50\\%).\n\nThe stance task exposes an operating-conditions limitation: GPT-3.5-Turbo achieves FNR ${>}\\,0.50$ on all five targets, violating the classifier quality precondition and producing $\\kappa$ values up to 15.0 (Climate Change) vs.\\ 4.6 (Hillary Clinton)---a ${\\sim}10{\\times}$ range within the same LLM.\nThis $\\kappa$ heterogeneity inflates correction variance; EC-HTE preserves sign correctness but at the cost of higher variance when $\\kappa \\gg 3$.\nMean RMSE: naive${=}0.116$, global${=}0.272$, EC-HTE${=}0.271$; correction reduces sign reversals but does not improve overall RMSE at $K{=}5$, $n{=}300$ per subgroup---consistent with the operating-conditions threshold ($n_{\\text{expert}} \\geq 250$ for $K{=}2$; Section~\\ref{sec:diagnostic}).\nPractitioners should verify per-subgroup FNR before applying correction.\n\n\\begin{table}[h]\n\\centering\n\\caption{Stance detection: subgroups with sign reversal or $\\kappa > 3$. \\checkmark\\ indicates at least one $z$-level affected. GPT-4o-mini and GPT-3.5-Turbo use simulated error profiles.}\n\\label{tab:stance_signrev}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nLLM & Target & $\\kappa$ & \\makecell{Sign Rev\\\\(Global)} & \\makecell{Sign Rev\\\\(EC-HTE)} & \\makecell{Bias Amp\\\\(Global)} \\\\\n\\midrule\nGPT-4o & Fem.\\ Mov.\\ & 1.79 & \\checkmark & --- & \\checkmark \\\\\nGPT-4o & Hillary C.\\ & 1.86 & \\checkmark & --- & \\checkmark \\\\\n\\midrule\nGPT-3.5-T & Atheism & 7.21 & --- & --- & --- \\\\\nGPT-3.5-T & Climate Ch.\\ & 15.01 & --- & \\checkmark & \\checkmark \\\\\nGPT-3.5-T & Fem.\\ Mov.\\ & 3.28 & \\checkmark & --- & \\checkmark \\\\\nGPT-3.5-T & Hillary C.\\ & 4.60 & \\checkmark & --- & \\checkmark \\\\\nGPT-3.5-T & Abortion & 14.17 & --- & --- & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 38,
      "startLine": 1,
      "totalLines": 38
    }
  },
  "sourceToolAssistantUUID": "2e742d4f-601c-436b-a885-484d9c800f0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-25T16:32:24.736Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q87AZaEtDQLTUhhBQ2cfq9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89980387-0335-4169-8cec-c86ab2b34787",
  "isSidechain": false,
  "requestId": "req_011CbPcCYVJ11TR53k96opLE",
  "type": "assistant",
  "uuid": "1fa92f87-744a-4348-9388-136b97a89e21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ya9ZTuvVZrZFRCAzFdmvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 38858,
      "output_tokens": 1021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1021,
          "cache_read_input_tokens": 38858,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
          },
          "type": "message"
        }
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

_source line 46 · 2026-05-25T16:32:24.819Z_

```json
{
  "parentUuid": "076510e1-606a-49d7-b6ae-d290528ce00f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "25994a47-f2b5-45c2-b6d7-bee7a70e9565",
  "timestamp": "2026-05-25T16:32:24.819Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：ec_hte_llm_annotation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 30 warning 一致性检查…",
  "leafUuid": "25994a47-f2b5-45c2-b6d7-bee7a70e9565",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP 2026 paper compliance and structure",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

### Assistant

_source line 49 · 2026-05-25T16:32:28.656Z_

<details><summary>Logged reasoning block</summary>

```text
The appendix.tex file is too large to read at once. Let me read it in parts to get the full picture. Let me also run some searches for specific patterns (em-dashes, AI-style words, etc.) in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25994a47-f2b5-45c2-b6d7-bee7a70e9565",
  "isSidechain": false,
  "requestId": "req_011CbPcDKGq8enHTT1RnXJRk",
  "type": "assistant",
  "uuid": "d94e7fa2-c0e0-4808-84d2-c3459d2c441d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8ceeeDArF1QRByncUCJ6j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 57560,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 57560,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1301,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 57560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 57560
          },
          "type": "message"
        }
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

_source line 50 · 2026-05-25T16:32:29.043Z_

Now let me read the appendix in parts and run pattern searches for AI-style markers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d94e7fa2-c0e0-4808-84d2-c3459d2c441d",
  "isSidechain": false,
  "requestId": "req_011CbPcDKGq8enHTT1RnXJRk",
  "type": "assistant",
  "uuid": "9173e548-7214-440d-9181-dde75741c609",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8ceeeDArF1QRByncUCJ6j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 57560,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 57560,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1301,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 57560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 57560
          },
          "type": "message"
        }
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

_source line 51 · 2026-05-25T16:32:30.993Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Uymj12BiVPyU6zMD8XDVvL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9173e548-7214-440d-9181-dde75741c609",
  "isSidechain": false,
  "requestId": "req_011CbPcDKGq8enHTT1RnXJRk",
  "type": "assistant",
  "uuid": "e2a1fd7e-5865-447f-94a8-67171fb5aed8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8ceeeDArF1QRByncUCJ6j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 57560,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 57560,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1301,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 57560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 57560
          },
          "type": "message"
        }
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

_source line 52 · 2026-05-25T16:32:42.827Z_

<details><summary>↩ Tool result · `toolu_01VRy6wKcBVfV2q2bWYZ3i1U`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d5d342b-3d89-4bf8-889d-96b5fd766178",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "03e86a88-1934-4815-b310-f3f2b60dedac",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "3d5d342b-3d89-4bf8-889d-96b5fd766178",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-25T16:32:31.263Z_

<details><summary>↩ Tool result · `toolu_01Uymj12BiVPyU6zMD8XDVvL`</summary>

```text
1	\section{EC-HTE Procedure}
2	\label{app:algorithm}
3	
4	\begin{algorithm}[t]
5	\caption{EC-HTE: Error-Corrected Heterogeneous Treatment Effects}
6	\label{alg:echte}
7	\begin{algorithmic}[1]
8	\Require Observations $\{(Y_i, W_i, \hat{Z}_i, X_i)\}_{i=1}^N$; expert labels $\{Z_j^*\}_{j=1}^{n_{\text{expert}}}$; subgroup map $S: \mathcal{X} \to \{1,\ldots,K\}$
9	\Ensure Corrected CATE estimates $\hat{\tau}(z)$ with variance-adjusted CIs
10	\Statex
11	\State \textbf{Preconditions:} verify $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ and $\max_s(\text{FPR}_s, \text{FNR}_s) < 0.5$; if either fails, use global correction
12	\Statex
13	\State \textbf{Step 1: Estimate per-subgroup confusion matrices (HB)}
14	\State $\alpha_0 \gets \arg\max_{\alpha} \prod_{s=1}^{K} p(\text{data}_s \mid \alpha, \hat{C}_{\text{global}})$ \Comment{empirical Bayes}
15	\For{$s = 1, \ldots, K$}
16	    \State $C_s[j,\cdot] \sim \mathrm{Dir}(\alpha_0 \cdot \hat{C}_{\text{global},j})$
17	    \State $\hat{C}_s[j,k] \gets \frac{n_{s,jk} + \alpha_0 \cdot \hat{C}_{\text{global},j,k}}{n_{s,j\cdot} + \alpha_0}$ \Comment{posterior mean}
18	\EndFor
19	\Statex
20	\State \textbf{Step 2: Correct observed outcome moments}
21	\For{$s = 1, \ldots, K$}
22	    \If{$\kappa(\hat{C}_s) > 100$} $\hat{C}_s \gets \bar{C}$ \Comment{singularity guard}
23	    \EndIf
24	    \State $\tilde{\boldsymbol{\mu}}_s \gets \hat{C}_s^{-1} \hat{\boldsymbol{\mu}}_s$
25	\EndFor
26	\Statex
27	\State \textbf{Step 3: CausalForestDML with variance-adjusted SEs}
28	\State Train CausalForest (honest splitting) on corrected outcome moments $\tilde{\boldsymbol{\mu}}_s$
29	\State $\mathrm{se}_{\mathrm{adj},i} \gets \sqrt{\mathrm{diag}(\hat{C}_{S_i}^{-1}\, \mathrm{diag}(\mathrm{se}_i^2)\, \hat{C}_{S_i}^{-\top})}$
30	\State \Return $\hat{\tau}(z)$ with 95\% CIs from $\mathrm{se}_{\mathrm{adj}}$
31	\end{algorithmic}
32	\end{algorithm}
33	
34	\subsection{Condition Number Guard Ablation}
35	\label{app:kappa_ablation}
36	
37	The singularity guard in Algorithm~\ref{alg:echte} (line~6) falls back to global correction when $\kappa(\hat{C}_s) > 100$.
38	We verify that this threshold is not load-bearing by sweeping $\kappa \in \{10, 25, 50, 100, 200, 500, 1000\}$ under the standard DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs).
39	Across all configurations, the maximum observed condition number is $\kappa_{\max} = 1.89$ (mean 1.45, p99 1.89), providing a $53{\times}$ safety margin below the $\kappa{=}100$ threshold.
40	Consequently, the guard never triggers at any tested threshold, and all $\kappa$ values produce identical RMSE (HB: 0.076, Global: 0.077) and zero numerical instability.
41	In a stress test with near-random labeling ($\pi_s \approx 0.4$--$0.5$, $n_{\text{expert}}{=}50$), the maximum condition number reaches 1{,}125, correctly triggering the $\kappa{=}100$ guard and preventing catastrophic inversion.
42	The adaptive formula $\kappa_{\text{adapt}} = 10 \sqrt{n_{\text{expert}} / K}$ recovers $\kappa{=}100$ for this regime and scales naturally with the estimation precision.
43	
44	\section{Full Proof of Theorem~\ref{thm:bias_identity}}
45	\label{app:derivation}
46	
47	\paragraph{Setup.}
48	Under assumptions (A1)--(A4), the observed CATE in subgroup $s$ at effect-modifier level $z$ is
49	\begin{equation}
50	\tau_{\text{obs}}(z, s) = \sum_{z'} M_s[z, z'] \cdot \tau(z'),
51	\end{equation}
52	where $M_s[z, z'] = P(Z{=}z' \mid \hat{Z}{=}z, S{=}s)$ is the mixing matrix.
53	Under (A2)--(A3), $M_s = \bigl[\begin{smallmatrix} 1-\pi_s & \pi_s \\ \pi_s & 1-\pi_s \end{smallmatrix}\bigr]$.
54	
55	\paragraph{Global correction.}
56	The pooled mixing matrix is $M_{\text{global}} = \sum_s w_s M_s = \bigl[\begin{smallmatrix} 1-\bar{\pi} & \bar{\pi} \\ \bar{\pi} & 1-\bar{\pi} \end{smallmatrix}\bigr]$, with $\bar{\pi} = \sum_s w_s \pi_s$.
57	
58	Global correction applies $M_{\text{global}}^{-1}$ to $\tau_{\text{obs}}(\cdot, s)$:
59	\begin{equation}
60	\hat{\tau}_{\text{global}}(z, s) = [M_{\text{global}}^{-1} M_s \cdot \boldsymbol{\tau}]_z,
61	\end{equation}
62	where $\boldsymbol{\tau} = [\tau(0), \tau(1)]^\top$.
63	
64	\paragraph{Bias computation.}
65	The bias is $\hat{\tau}_{\text{global}}(z, s) - \tau(z) = [(M_{\text{global}}^{-1} M_s - I) \boldsymbol{\tau}]_z$.
66	
67	Direct computation gives:
68	\begin{equation}
69	M_{\text{global}}^{-1} = \frac{1}{1 - 2\bar{\pi}} \begin{bmatrix} 1-\bar{\pi} & -\bar{\pi} \\ -\bar{\pi} & 1-\bar{\pi} \end{bmatrix}.
70	\end{equation}
71	Multiplying by $M_s$:
72	\begin{equation}
73	\resizebox{.88\columnwidth}{!}{$\displaystyle
74	M_{\text{global}}^{-1} M_s = \frac{1}{1-2\bar{\pi}} \begin{bmatrix} (1{-}\bar{\pi})(1{-}\pi_s) - \bar{\pi}\pi_s & (1{-}\bar{\pi})\pi_s - \bar{\pi}(1{-}\pi_s) \\ -\bar{\pi}(1{-}\pi_s) + (1{-}\bar{\pi})\pi_s & -\bar{\pi}\pi_s + (1{-}\bar{\pi})(1{-}\pi_s) \end{bmatrix}.
75	$}
76	\end{equation}
77	
78	Define $\delta_s = \pi_s - \bar{\pi}$. Substituting $\pi_s = \bar{\pi} + \delta_s$:
79	\begin{equation}
80	M_{\text{global}}^{-1} M_s - I = \frac{\delta_s}{1-2\bar{\pi}} \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}.
81	\end{equation}
82	
83	To verify: the $(1,1)$ entry of $M_{\text{global}}^{-1} M_s$ is
84	{\small
85	\begin{align}
86	&\frac{(1{-}\bar{\pi})(1{-}\bar{\pi}{-}\delta_s) - \bar{\pi}(\bar{\pi}{+}\delta_s)}{1-2\bar{\pi}} \nonumber\\
87	&= \frac{(1{-}\bar{\pi})^2 - (1{-}\bar{\pi})\delta_s - \bar{\pi}^2 - \bar{\pi}\delta_s}{1-2\bar{\pi}} \nonumber\\
88	&= \frac{1 - 2\bar{\pi} - \delta_s}{1-2\bar{\pi}} = 1 - \frac{\delta_s}{1-2\bar{\pi}}.
89	\end{align}
90	}
91	
92	Applying $(M_{\text{global}}^{-1} M_s - I)$ to $\boldsymbol{\tau}$:
93	{\small
94	\begin{align}
95	\text{bias}(z{=}0, s) &= \tfrac{\delta_s}{1-2\bar{\pi}}(-\tau(0) + \tau(1)) = +\tfrac{\delta_s \cdot \Delta\tau}{1-2\bar{\pi}}, \\
96	\text{bias}(z{=}1, s) &= \tfrac{\delta_s}{1-2\bar{\pi}}(\tau(0) - \tau(1)) = -\tfrac{\delta_s \cdot \Delta\tau}{1-2\bar{\pi}},
97	\end{align}
98	}
99	where $\Delta\tau = \tau(1) - \tau(0)$. \qed
100	
101	\paragraph{Finite-sample remainder.}
102	When $\hat{C}_s = C_s + E_s$ with $\|E_s\| = O_p(n_{\text{expert}}^{-1/2})$ (central limit theorem), the estimated correction $\hat{M}_{\text{global}}^{-1} \hat{M}_s$ deviates from its population counterpart by
103	$\|\hat{M}_{\text{global}}^{-1} \hat{M}_s - M_{\text{global}}^{-1} M_s\| \leq \kappa(M_{\text{global}})^2 \cdot O_p(n_{\text{expert}}^{-1/2})$,
104	where $\kappa(M) = \|M\| \cdot \|M^{-1}\|$ is the condition number~\citep{stewart1990matrix}; the squared exponent arises because the first-order perturbation of $M^{-1}$ introduces one factor of $\|M^{-1}\|$, and the product $M_{\text{global}}^{-1} M_s$ introduces a second (see the Neumann expansion in Section~\ref{sec:theory}).
105	This motivates the $\kappa > 100$ singularity guard in Section~\ref{sec:method}.
106	
107	\section{Multi-class Extension and Proof}
108	\label{app:multiclass}
109	
110	\begin{corollary}[Multi-class Extension]
111	\label{cor:multiclass}
112	For $K > 2$ subgroups with $J$ effect-modifier levels and uniform off-diagonal misclassification (misclassified observations from class $j$ are distributed equally among the remaining $J{-}1$ classes), the subgroup bias of global correction generalizes to
113	\begin{equation}
114	\mathrm{bias}_{\mathrm{global}}(z, s) = \sum_{j=1}^{J} \bigl(\bar{\pi}_j - \pi_{s,j}\bigr) \cdot \bigl(\tau(j) - \bar{\tau}\bigr) \cdot g(\bar{\pi}),
115	\label{eq:multiclass}
116	\end{equation}
117	where $g(\bar{\pi})$ collects the matrix-inversion amplification terms.\footnote{For $J=3$ with symmetric misclassification (off-diagonal errors uniform), $g(\bar{\pi}) = 1/(1 - 3\bar{\pi}/2)$, generalizing the $J{=}2$ factor $1/(1-2\bar{\pi})$. In general, $g(\bar{\pi}) = 1/(1 - J\bar{\pi}/(J-1))$.}
118	The essential structure, $\sum_s w_s (\bar{\pi}_j - \pi_{s,j}) = 0$, ensures that bias redistributes across subgroups rather than vanishing in aggregate.
119	\end{corollary}
120	
121	\paragraph{Proof.}
122	For $K > 2$ subgroups with $J$ effect-modifier levels, the subgroup-specific mixing matrix $M_s$ is $J \times J$ with entries $M_s[j, j'] = P(Z{=}j' \mid \hat{Z}{=}j, S{=}s)$.
123	The global mixing matrix is $M_{\text{global}} = \sum_s w_s M_s$.
124	
125	The bias of global correction in subgroup $s$ at level $z$ is:
126	\begin{equation}
127	\text{bias}_{\text{global}}(z, s) = [(M_{\text{global}}^{-1} M_s - I) \boldsymbol{\tau}]_z.
128	\end{equation}
129	
130	Write $M_s = M_{\text{global}} + \Delta_s$ where $\Delta_s = M_s - M_{\text{global}}$ satisfies $\sum_s w_s \Delta_s = 0$.
131	Then $M_{\text{global}}^{-1} M_s = I + M_{\text{global}}^{-1} \Delta_s$, so:
132	\begin{equation}
133	\text{bias}_{\text{global}}(z, s) = [M_{\text{global}}^{-1} \Delta_s \cdot \boldsymbol{\tau}]_z.
134	\end{equation}
135	
136	For symmetric misclassification with per-class error rates $\pi_{s,j}$ and pooled rates $\bar{\pi}_j$, the entries of $\Delta_s$ have the form $\Delta_s[j,j'] = (\bar{\pi}_j - \pi_{s,j}) \cdot h(j, j')$ for a function $h$ determined by the off-diagonal redistribution pattern.
137	Expanding the matrix-vector product and collecting terms yields:
138	\begin{equation}
139	\text{bias}_{\text{global}}(z, s) = \sum_{j=1}^{J} (\bar{\pi}_j - \pi_{s,j}) \cdot (\tau(j) - \bar{\tau}) \cdot g(\bar{\pi}),
140	\end{equation}
141	where $g(\bar{\pi})$ collects the matrix-inversion amplification terms and $\bar{\tau} = \sum_j P(Z{=}j) \tau(j)$.
142	
143	The essential structure $\sum_s w_s (\bar{\pi}_j - \pi_{s,j}) = 0$ ensures that the weighted bias across subgroups sums to zero: global correction redistributes bias rather than creating or eliminating it in aggregate.
144	For non-uniform off-diagonal entries, the scalar amplification $g(\bar{\pi})$ generalizes to a cell-specific matrix; the product structure $B_s \cdot \Delta\tau$ persists but a closed-form amplification factor does not. \qed
145	
146	\section{Proof of Proposition~\ref{prop:debiasing_hurts}}
147	\label{app:debiasing_hurts}
148	
149	The naive estimator has bias $\tau_{\text{obs}}(z,s) - \tau(z)$.
150	Under (A2)--(A3), $\tau_{\text{obs}}(0,s) = (1-\pi_s)\tau(0) + \pi_s\tau(1)$, so $\text{bias}_{\text{naive}}(0,s) = \pi_s \cdot \Delta\tau$.
151	
152	Global correction produces larger absolute bias when $|\text{bias}_{\text{global}}(0,s)| > |\text{bias}_{\text{naive}}(0,s)|$:
153	\begin{equation}
154	\frac{|\delta_s| \cdot |\Delta\tau|}{|1-2\bar{\pi}|} > \pi_s \cdot |\Delta\tau|.
155	\end{equation}
156	Since $\Delta\tau \neq 0$ (otherwise both biases are zero), dividing through gives:
157	\begin{equation}
158	\frac{|\delta_s|}{(1-2\bar{\pi}) \cdot \pi_s} > 1,
159	\end{equation}
160	where we use $1-2\bar{\pi} > 0$ from (A4).
161	
162	For high-error subgroups ($\pi_s > \bar{\pi}$, so $\delta_s > 0$): the condition becomes $(\pi_s - \bar{\pi}) / ((1-2\bar{\pi})\pi_s) > 1$, which simplifies to $\pi_s(1 - 1 + 2\bar{\pi}) > \bar{\pi}$, i.e., $2\bar{\pi}\pi_s > \bar{\pi}$, i.e., $\pi_s > 0.5$.
163	This is excluded by (A4), so global correction always reduces bias in high-error subgroups.
164	
165	For low-error subgroups ($\pi_s < \bar{\pi}$, so $\delta_s < 0$): the condition becomes $(\bar{\pi} - \pi_s) / ((1-2\bar{\pi})\pi_s) > 1$, which gives $\pi_s < \bar{\pi} / (1 - 2\bar{\pi} + 1) = \bar{\pi} / (2(1-\bar{\pi}))$.
166	When $\bar{\pi} = 0.15$, any subgroup with $\pi_s < 0.088$ experiences increased bias from global correction. \qed
167	
168	\paragraph{Extension to asymmetric misclassification.}
169	Proposition~\ref{prop:debiasing_hurts} assumes symmetric error rates (A2).
170	Under asymmetric misclassification ($\mathrm{FPR}_s \neq \mathrm{FNR}_s$) with balanced $Z$ (A3), the naive bias becomes $\mathrm{bias}_{\mathrm{naive}}(0,s) = \mathrm{FNR}_s \cdot \Delta\tau / (1 - \mathrm{FPR}_s + \mathrm{FNR}_s)$, involving both error rates and a normalization denominator; the global correction bias depends on the full $2 \times 2$ structure of $B_s = M_{\mathrm{global}}^{-1} M_s - I$ (Remark~\ref{rem:asymmetric} in Section~\ref{sec:theory}).
171	A sufficient condition for global correction to increase bias is
172	\begin{equation}
173	\max_{i,j}|[B_s]_{i,j}| > \max(\mathrm{FPR}_s, \mathrm{FNR}_s),
174	\end{equation}
175	which reduces to Equation~\eqref{eq:hurts_condition} when $\mathrm{FPR}_s = \mathrm{FNR}_s = \pi_s$.
176	In the asymmetric experiments (Appendix~\ref{app:asymmetric}), the scalar diagnostic achieves per-subgroup AUC $= 0.96$ when applied with $\pi_s = (\mathrm{FPR}_s + \mathrm{FNR}_s)/2$ (48 asymmetric configurations, FPR/FNR ratios 1:5 to 5:1), and AUC $= 1.00$ on 8 semi-real LLM confusion matrices, confirming that the symmetric simplification preserves diagnostic validity under practical asymmetry.
177	
178	\section{Semi-Synthetic Data Generating Process}
179	\label{app:dgp}
180	
181	\paragraph{Synthetic DGP (Sections~\ref{sec:bias_mechanism}--\ref{sec:diagnostic} and Appendix~\ref{sec:budget}).}
182	We generate $N = 5000$ observations.
183	Each observation belongs to one of $K \in \{2, 4\}$ subgroups $S \in \{1, \ldots, K\}$ with equal weights $w_s = 1/K$.
184	The binary effect modifier $Z \in \{0, 1\}$ is drawn with $P(Z{=}1) = 0.5$.
185	Treatment assignment is $T \sim \text{Bernoulli}(0.5)$, independent of $Z$ and $S$.
186	
187	The outcome is generated as:
188	\begin{equation}
189	Y = \tau(Z) \cdot T + \eta, \quad \eta \sim \mathcal{N}(0, 1),
190	\end{equation}
191	where the CATE function is $\tau(z) = \bar{\tau} + \Delta\tau \cdot (z - 0.5)$ with $\bar{\tau} = 0.5$.
192	The CATE heterogeneity $\Delta\tau \in \{0, 0.2, 0.5, 1.0\}$ controls the strength of treatment effect variation across levels of $Z$.
193	
194	Misclassification is symmetric: $\hat{Z} \neq Z$ with probability $\pi_s$ depending on subgroup.
195	For $K{=}2$: $\pi_1 = \bar{\pi} - \Delta_c/2$, $\pi_2 = \bar{\pi} + \Delta_c/2$, with $\bar{\pi} \in \{0.1, 0.2\}$ and $\Delta_c \in \{0, 0.05, 0.1, 0.15\}$.
196	For $K{=}4$, extreme regime: $\pi \in \{0.05, 0.10, 0.15, 0.25\}$; moderate regime: $\pi \in \{0.08, 0.12, 0.16, 0.20\}$.
197	
198	Expert labels are drawn as a simple random sample of size $n_{\text{expert}} \in \{50, 100, 250, 500, 1000, 2000\}$ from the full dataset, with true $Z$ observed for these observations.
199	
200	\paragraph{Semi-synthetic DGP (Section~\ref{sec:ec_hte_eval}).}
201	We sample $N = 5000$ tweets from the TweetEval sentiment corpus ($N_{\text{pool}} = 57{,}899$).
202	Subgroups are defined by crossing \texttt{has\_hashtag} $\times$ \texttt{text\_length\_bin} (short/medium/long), yielding $K = 4$ subgroups with empirical sizes: $S_0 \approx 38\%$, $S_1 \approx 38\%$, $S_2 \approx 12\%$, $S_3 \approx 12\%$.
203	Misclassification rates in the extreme regime are $\pi_{S_0} = 0.05$, $\pi_{S_1} = 0.10$, $\pi_{S_2} = 0.15$, $\pi_{S_3} = 0.25$, reflecting empirical evidence that hashtag-heavy text degrades LLM classifier accuracy.
204	The outcome DGP follows the same structure as the synthetic case, with CATE injected onto the real text-derived subgroup structure.
205	
206	\paragraph{PPCI DGPs (Appendix~\ref{sec:ppci}).}
207	Four DGPs isolate error types: (A) covariate error only ($\sigma_{\text{outcome}} = 0$), (B) outcome error only ($\sigma_{\text{outcome}} = 0.5$), (C) both errors ($\sigma_{\text{outcome}} = 0.5$), (D) no error ($\sigma_{\text{outcome}} = 0$).
208	Outcome-side error is additive Gaussian noise on $Y$.
209	
210	\paragraph{CausalForestDML hyperparameters.}
211	All CausalForest experiments use \texttt{econml.dml.CausalForestDML} with honest splitting, $n_{\text{estimators}} = 48$, $\texttt{min\_samples\_leaf} = 20$, \texttt{model\_y} = \texttt{LassoCV}(cv=3), and \texttt{model\_t} = \texttt{LogisticRegressionCV}.
212	These defaults were held constant across all configurations; no hyperparameter tuning was performed.
213	
214	% [Promoted to main text — Figure~\ref{fig:heatmap}]
215	
216	\section{Extended Related Work}
217	\label{app:related}
218	
219	\paragraph{Measurement error details.}
220	\citet{fuller1987measurement} establish the foundational theory showing that naive regression with mismeasured covariates yields attenuated coefficient estimates.
221	\citet{carroll2006measurement} extend this to nonlinear models.
222	\citet{gustafson2003measurement} develops Bayesian treatments modeling measurement jointly with outcomes.
223	\citet{hu2008nonparametric} provide nonparametric identification using repeated measurements or instruments.
224	
225	\paragraph{Annotation model extensions.}
226	Beyond the foundational \citet{dawid1979maximum} model, \citet{passonneau2014benefits} incorporate item difficulty, \citet{hovy2013learning} learn annotator competence, and \citet{paun2018comparing} introduce hierarchical priors sharing information across annotators with varying expertise.
227	
228	\paragraph{PPI extensions and text-as-data methods.}
229	\citet{zrnic2024cross} extend PPI via cross-prediction; their active inference framework~\citep{zrnic2024active} achieves $>$80\% expert budget savings through adaptive allocation, complementary to our fixed-budget analysis.
230	\citet{grimmer2022text} provide methodological guidance for text-as-data pipelines.
231	\citet{audinet2025benchmarking} systematically benchmark DSL and PPI methods for LLM-based parameter estimation, finding that debiasing can increase MSE when prediction error is heterogeneous---a population-level analogue of the subgroup-conditional bias amplification we formalize in Theorem~\ref{thm:bias_identity}.
232	
233	\paragraph{Treatment vs.\ effect-modifier misclassification.}
234	\citet{imai2010causal} study treatment misclassification where errors change which arm a unit is assigned to, requiring instrumental variables or partial identification because the fundamental treated-vs-control contrast is corrupted.
235	Our problem preserves the treatment contrast ($T$ is observed correctly) but corrupts the heterogeneity structure ($\hat{Z} \neq Z$).
236	The ATE remains identified; only conditional effects are biased, which makes exact correction through confusion matrix inversion feasible.
237	\citet{knox2020administrative} demonstrate how racial misclassification in administrative records biases causal estimates; \citet{blette2024assessing} handle missing (not misclassified) effect modifier data in cluster-RCTs via multiple imputation---a complementary problem to our confusion-matrix correction setting.
238	
239	\paragraph{Econometrics of binary misclassification.}
240	\citet{bound2001measurement} survey measurement error in survey data, establishing that binary misclassification attenuates regression coefficients.
241	\citet{frazis2003estimating} derive exact bias formulas for OLS with a misclassified binary regressor, showing attenuation proportional to the misclassification rate---analogous to our Theorem~\ref{thm:bias_identity} but restricted to average effects without subgroup heterogeneity.
242	\citet{black2000racial} demonstrate that racial misclassification in administrative data can substantially bias estimates of racial disparities.
243	\citet{mahajan2006identification} and \citet{lewbel2007estimation} develop instrumental variable approaches to identify models with misclassified binary regressors, requiring exclusion restrictions unavailable when the mismeasured variable is an LLM annotation.
244	Our setting differs in three respects: (i) the mismeasured variable is an effect modifier indexing the CATE function, not a standard regressor; (ii) misclassification rates vary across subgroups, creating the $\delta_s \times \Delta\tau$ product amplification absent from homogeneous-error analyses; and (iii) expert labels provide a direct calibration sample, enabling confusion matrix estimation without instruments.
245	
246	\section{MCMC Convergence Diagnostics}
247	\label{app:mcmc}
248	
249	Main experiments use empirical Bayes point estimates ($<$5ms per subgroup).
250	This appendix reports MCMC validation (4 chains, 4000 iterations, 2000 warmup) confirming EB and full posterior agreement within simulation error.
251	Main experiments (Table~\ref{tab:main_results}) use a Dirichlet prior centered on $\hat{C}_{\text{global}}$ with concentration $\alpha_0$ estimated via empirical Bayes (marginal likelihood).
252	Appendix robustness experiments use a fixed Dirichlet prior ($\alpha{=}3$); since fixed-$\alpha$ partial pooling is weakly dominated by the adaptive variant, these results are conservative.
253	All runs achieve $\hat{R} < 1.0034$ and ESS $> 1618$, confirming convergence with substantial margin.
254	
255	\begin{table}[h]
256	\centering
257	\small
258	\begin{tabular}{lcc}
259	\toprule
260	Diagnostic & Threshold & Achieved \\
261	\midrule
262	$\hat{R}$ (max across all params) & $< 1.01$ & $< 1.0034$ \\
263	ESS (min across all params) & $> 845$ & $> 1618$ \\
264	Divergent transitions & $= 0$ & $0$ \\
265	Singularity guard triggers & --- & extreme/$n{=}50$ only \\
266	\bottomrule
267	\end{tabular}
268	\caption{MCMC convergence diagnostics for the hierarchical Bayesian estimator. All configurations satisfy convergence criteria with substantial margin.}
269	\label{tab:mcmc}
270	\end{table}
271	
272	\subsection{Hyperprior Sensitivity}
273	\label{app:hyperprior}
274	
275	We sweep the $\text{Gamma}(a_0, b_0)$ hyperprior on the concentration parameter $\alpha_0$ across 15 configurations ($a_0 \in \{1, 2, 3, 4, 5\}$, $b_0 \in \{0.5, 1.0, 2.0\}$) under the standard synthetic DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs).
276	
277	\begin{table}[h]
278	\centering
279	\caption{Hyperprior sensitivity summary. RMSE and coverage across 15 $(a_0, b_0)$ configurations. The default $\text{Gamma}(3, 1)$ ranks 8th of 15 by RMSE; the best configuration $\text{Gamma}(1, 0.5)$ yields only 1.9\% improvement. Excluding extreme configurations ($a_0 \cdot b_0 > 8$), RMSE varies by $<$6\%.}
280	\label{tab:hyperprior_sweep}
281	\small
282	\begin{tabular}{lc}
283	\toprule
284	Metric & Value \\
285	\midrule
286	Default $\text{Gamma}(3, 1)$ RMSE & 0.0841 \\
287	Best $\text{Gamma}(1, 0.5)$ RMSE & 0.0825 \\
288	RMSE range (reasonable configs) & 6.0\% \\
289	RMSE range (all 15 configs) & 17.3\% \\
290	Coverage range & 0.925--0.938 \\
291	Default rank & 8 / 15 \\
292	\bottomrule
293	\end{tabular}
294	\end{table}
295	
296	Scaling the $\text{Gamma}(3, 1)$ hyperprior by factors of $0.5\times$ to $2\times$ produces $<$1\% RMSE variation for $K{=}2$ and $\sim$4--5\% for $K{=}4$.
297	Coverage remains invariant across the sensitivity range ($\Delta < 1.3$pp).
298	These results confirm that the hierarchical estimator is robust to prior specification within a reasonable range; the default $\text{Gamma}(3, 1)$ is near-median, and no configuration achieves more than 1.9\% RMSE improvement over the default.
299	
300	\section{Diagnostic ROC Curves}
301	\label{app:roc}
302	
303	\begin{figure}[t]
304	\centering
305	\includegraphics[width=\columnwidth]{figures/fig4_roc.png}
306	\caption{ROC curves for the $\Delta\tau$-free diagnostic (Proposition~\ref{prop:debiasing_hurts}): $|\delta_s|/((1{-}2\bar\pi)\cdot\pi_s)>1$. (A)~Setting-level ROC (AUC $= 0.89$), compared with the $|\Delta\pi \times \Delta\tau|$ product (AUC $= 0.89$) and $\mathrm{CV}(\pi_s)$ (AUC $= 0.97$). (B)~Subgroup-level ROC: the $\Delta\pi$-only condition (AUC $= 0.86$) substantially outperforms the $|\Delta\pi \times \Delta\tau|$ product (AUC $= 0.73$). The $\Delta\tau$-free diagnostic depends only on estimable misclassification rates, breaking the circular dependency that would arise if CATE heterogeneity were required.}
307	\label{fig:roc}
308	\end{figure}
309	
310	\paragraph{Cost-asymmetric diagnostic thresholds.}
311	In practice, the cost of a false negative (failing to detect that global correction increases bias) exceeds the cost of a false positive (unnecessarily applying EC-HTE when global correction would suffice), because the former propagates systematic bias into CATE estimates while the latter only incurs additional estimation variance.
312	Practitioners in high-stakes settings (e.g., policy evaluation where CATE estimates inform resource allocation) should lower the diagnostic threshold to favor recall over precision, accepting more false positives to minimize the risk of undetected bias amplification.
313	
314	\section{Expert Budget Crossover Curves}
315	\label{app:budget}
316	\label{sec:budget}
317	
318	The crossover point at which EC-HTE achieves lower RMSE than global correction depends on the DGP: $n_{\text{expert}} = 250$ for $K{=}2$/extreme and $n_{\text{expert}} = 1000$ for $K{=}4$/extreme under $\Delta\tau{=}0.3$ (Figure~\ref{fig:budget}); under the Table~\ref{tab:main_results} DGP, the $K{=}4$ crossover occurs at $n_{\text{expert}} \approx 500$.
319	Under moderate heterogeneity ($K{=}2$), EC-HTE never achieves lower RMSE than global at any budget.
320	HB partial pooling improves over stratified MLE in 21 of 24 configurations, with the two estimators converging by $n_{\text{expert}} \geq 1000$.
321	
322	\begin{figure*}[t]
323	\centering
324	\includegraphics[width=\textwidth]{figures/fig3_budget.pdf}
325	\caption{RMSE vs.\ expert budget ($n_{\text{expert}}$) across four regime$\times K$ combinations. Dashed vertical lines mark crossover points where EC-HTE achieves lower RMSE than global correction: $n{=}250$ ($K{=}2$, extreme), $n{=}1000$ ($K{=}4$, extreme). Under moderate heterogeneity ($K{=}2$), global correction dominates at all budgets. Shaded bands show $\pm 1$ SD across subgroups within each configuration.}
326	\label{fig:budget}
327	\end{figure*}
328	
329	\subsection{Budget Sensitivity: HB vs.\ Stratified MLE}
330	\label{app:budget_sensitivity}
331	
332	Hierarchical Bayes (HB) partial pooling borrows strength across subgroups, which should matter most when per-subgroup expert labels are scarce.
333	We sweep $n_{\text{expert}} \in \{25, 50, 75, 100, 150, 250\}$ under extreme heterogeneity ($\Delta\tau{=}0.3$, 100 MC runs, $N{=}5{,}000$).
334	Table~\ref{tab:budget_sensitivity} reports aggregate RMSE for global correction, stratified MLE, and HB EC-HTE.
335	
336	\begin{table}[h]
337	\centering
338	\caption{RMSE across expert budgets under extreme heterogeneity.
339	HB crossover (first budget where HB $<$ MLE) occurs at approximately 10 expert labels per subgroup-cell:
340	$n_{\text{expert}}{=}50$ for $K{=}2$ and $n_{\text{expert}}{=}75$ for $K{=}4$.}
341	\label{tab:budget_sensitivity}
342	\small
343	\begin{tabular}{crrrrc}
344	\toprule
345	$K$ & $n_{\text{expert}}$ & Global & Strat.\ MLE & HB EC-HTE & HB vs.\ MLE \\
346	\midrule
347	2 & 25 & \textbf{0.101} & 0.256 & 0.269 & $+4.9\%$ \\
348	2 & 50 & \textbf{0.088} & 0.275 & 0.231 & $\mathbf{-16.1\%}$ \\
349	2 & 75 & 0.084 & 0.091 & \textbf{0.089} & $-1.9\%$ \\
350	2 & 100 & 0.083 & 0.085 & \textbf{0.084} & $-0.8\%$ \\
351	2 & 150 & 0.081 & 0.077 & \textbf{0.077} & $-0.4\%$ \\
352	2 & 250 & 0.080 & 0.075 & \textbf{0.074} & $-0.1\%$ \\
353	\midrule
354	4 & 25 & \textbf{0.129} & 0.401 & 0.612 & $+52.5\%$ \\
355	4 & 50 & \textbf{0.117} & 0.380 & 0.470 & $+23.8\%$ \\
356	4 & 75 & \textbf{0.112} & 0.221 & 0.211 & $\mathbf{-4.4\%}$ \\
357	4 & 100 & \textbf{0.112} & 0.215 & 0.212 & $-1.3\%$ \\
358	4 & 150 & \textbf{0.109} & 0.157 & 0.152 & $-3.6\%$ \\
359	4 & 250 & \textbf{0.108} & 0.127 & 0.126 & $-1.0\%$ \\
360	\bottomrule
361	\end{tabular}
362	\end{table}
363	
364	Three regimes emerge.
365	At very low budgets ($n_{\text{expert}} < 50$ for $K{=}2$, $< 75$ for $K{=}4$), per-subgroup counts are insufficient for reliable confusion matrix estimation; global pooling dominates because the variance cost of stratification overwhelms any bias reduction.
366	HB degrades substantially in this regime because the Gibbs posterior, while better regularized than MLE, still cannot overcome the fundamental sample-size constraint with $\sim$6--12 labels per subgroup.
367	At moderate budgets ($n_{\text{expert}} = 50$--$250$ for $K{=}2$, $75$--$250$ for $K{=}4$), HB partial pooling provides consistent RMSE improvement over stratified MLE ($-0.4\%$ to $-16.1\%$), with the largest gains near the crossover point.
368	At high budgets ($n_{\text{expert}} \geq 250$), both estimators converge as subgroup-level data becomes sufficient for reliable MLE; the HB advantage diminishes to $< 1\%$.
369	Coverage remains $\geq 0.88$ for both methods across all budget levels.
370	
371	\subsection{Scalability to $K{=}8$ Subgroups}
372	\label{app:k8_subgroups}
373	
374	We test EC-HTE at $K{=}8$ to identify the scalability boundary of hierarchical Bayesian partial pooling under fixed expert budget.
375	
376	\paragraph{Setup.}
377	$N{=}5{,}000$, $K{=}8$ (equal-weight subgroups), $n_{\text{expert}}{=}250$ (${\approx}31$ labels per subgroup), 100 MC replications.
378	Misclassification rates are uniformly spread: $\pi_s \in \{0.05, 0.09, 0.13, 0.18, 0.22, 0.26, 0.30, 0.35\}$.
379	Treatment effects depend on $Z$ (not subgroup): $\tau(Z{=}0){=}0$, $\tau(Z{=}1){=}0.3$.
380	
381	\begin{table}[h]
382	\centering
383	\caption{EC-HTE at $K{=}8$ ($n_{\text{expert}}{=}250$, ${\approx}31$ labels/subgroup, 100 MC).}
384	\label{tab:k8_subgroups}
385	\small
386	\begin{tabular}{lccc}
387	\toprule
388	Method & Coverage & RMSE & $|\text{Bias}|$ \\
389	\midrule
390	Oracle       & 0.944 & 0.113 & 0.090 \\
391	Global       & 0.951 & 0.168 & 0.135 \\
392	HB EC-HTE    & 0.956 & 0.340 & 0.183 \\
393	Strat MLE    & 0.953 & 0.638 & 0.219 \\
394	Naive        & 0.913 & 0.133 & 0.107 \\
395	\bottomrule
396	\end{tabular}
397	\end{table}
398	
399	All CM-aware methods achieve nominal coverage at $K{=}8$: HB EC-HTE 95.6\%, Strat MLE 95.3\%, Global 95.1\%.
400	HB partial pooling achieves a 47\% RMSE reduction over stratified MLE (0.340 vs.\ 0.638), confirming that hierarchical shrinkage provides substantial regularization.
401	However, HB RMSE (0.340) exceeds global correction (0.168), indicating that ${\approx}31$ expert labels per subgroup are insufficient for per-subgroup CM estimation to outweigh variance inflation.
402	
403	\paragraph{Per-subgroup breakdown.}
404	Table~\ref{tab:k8_per_subgroup} decomposes RMSE by subgroup.
405	
406	\begin{table}[h]
407	\centering
408	\caption{Per-subgroup RMSE at $K{=}8$. HB improvement over MLE is largest in high-$\pi$ subgroups but does not close the gap with Global.}
409	\label{tab:k8_per_subgroup}
410	\small
411	\begin{tabular}{cccccc}
412	\toprule
413	Subgroup & $\pi_s$ & HB RMSE & MLE RMSE & Global RMSE & HB Cov \\
414	\midrule
415	$s_0$ & 0.050 & 0.136 & 0.134 & \textbf{0.181} & 0.950 \\
416	$s_1$ & 0.093 & 0.133 & 0.132 & \textbf{0.154} & 0.970 \\
417	$s_2$ & 0.136 & 0.154 & 0.154 & 0.161 & 0.975 \\
418	$s_3$ & 0.179 & 0.178 & 0.182 & \textbf{0.159} & 0.945 \\
419	$s_4$ & 0.221 & 0.263 & 0.343 & \textbf{0.163} & 0.940 \\
420	$s_5$ & 0.264 & 0.421 & 0.711 & \textbf{0.164} & 0.965 \\
421	$s_6$ & 0.307 & 0.634 & 1.375 & \textbf{0.177} & 0.940 \\
422	$s_7$ & 0.350 & 0.432 & 0.809 & \textbf{0.183} & 0.960 \\
423	\bottomrule
424	\end{tabular}
425	\end{table}
426	
427	RMSE degradation is concentrated in high-$\pi$ subgroups ($s_4$--$s_7$, $\pi \geq 0.22$), where confusion matrix inversion amplifies estimation noise ($r = 0.87$, $p = 0.005$ for correlation between $\pi_s$ and HB RMSE).
428	Low-error subgroups ($s_0$--$s_1$) benefit from stratification, with HB RMSE 14--25\% below global correction.
429	HB partial pooling reduces MLE RMSE by 24--54\% in the high-$\pi$ regime ($s_4$--$s_7$), confirming that hierarchical shrinkage provides meaningful regularization even when per-subgroup labels are scarce.
430	Coverage remains $\geq$0.94 across all subgroups for HB EC-HTE, indicating that variance inflation does not compromise inference validity.
431	Adaptive shrinkage---increasing the prior strength for high-$\pi$ subgroups where CM estimation is least reliable---is a natural extension that may close the RMSE gap with global correction at larger $K$.
432	
433	We explored adaptive shrinkage ($\alpha{=}10$ for high-$\pi$ subgroups vs.\ default $\alpha{=}3$), which reduces aggregate RMSE from 0.340 to 0.216 (35\% improvement) by attenuating estimation noise in high-$\pi$ subgroups.
434	However, RMSE remains 30\% above global correction (0.166), confirming that the bottleneck is per-subgroup sample size (${\sim}$31 expert labels) rather than the shrinkage method itself.
435	This establishes $K{=}8$ at $n_{\text{expert}}{=}250$ as a boundary condition: all correction methods provide valid inference (coverage $\geq$94\%), but per-subgroup stratification requires proportionally larger expert budgets---approximately $n_{\text{expert}} \geq 500$ (${\approx}60$ labels/subgroup)---to achieve RMSE parity with global correction.
436	
437	\section{Asymmetric Misclassification Extension}
438	\label{app:asymmetric}
439	
440	Assumption~(A2) imposes symmetric misclassification ($\text{FPR}_s = \text{FNR}_s = \pi_s$), which simplifies the bias decomposition but is not necessary for it.
441	Real LLM annotators typically exhibit asymmetric confusion patterns; we show here that the product structure generalizes.
442	
443	\paragraph{General bias formula.}
444	For asymmetric confusion matrices $C_s = \bigl(\begin{smallmatrix} 1{-}\text{FPR}_s & \text{FPR}_s \\ \text{FNR}_s & 1{-}\text{FNR}_s \end{smallmatrix}\bigr)$, define the mixing matrix $M_s$ via Bayesian inversion and the residual matrix $B_s = M_{\text{global}}^{-1} M_s - I$.
445	Since both $M_s$ and $M_{\text{global}}$ are row-stochastic, $B_s \mathbf{1} = \mathbf{0}$.
446	Decomposing $\boldsymbol{\tau} = \tau(0)\mathbf{1} + \Delta\tau \, \mathbf{e}_1$ gives:
447	\begin{equation}
448	\text{bias}(z, s) = \Delta\tau \cdot [B_s]_{z,1},
449	\end{equation}
450	where $[B_s]_{z,1}$ depends only on $\{\text{FPR}_k, \text{FNR}_k, w_k\}$, not on $\Delta\tau$.
451	Under~(A2), this reduces to $\delta_s \Delta\tau / (1 - 2\bar{\pi})$ (Theorem~\ref{thm:bias_identity}).
452	
453	\paragraph{Empirical validation.}
454	We test three asymmetric configurations ($K{=}2$, $n_{\text{expert}}{=}250$, 100 MC runs each): \emph{Cross} (FPR/FNR = 0.10/0.20 vs.\ 0.25/0.10), \emph{Co-directional} (0.05/0.15 vs.\ 0.20/0.30), and \emph{Extreme} (0.03/0.25 vs.\ 0.30/0.05).
455	Regressing analytic predictions on MC bias yields $R^2 = 0.991$ across all configurations, confirming the product structure under asymmetry.
456	Table~\ref{tab:asymmetric} reports correction performance averaged over subgroups, $z$-levels, and $\Delta\tau \in \{0.1, \ldots, 0.5\}$.
457	In these three selected high-disparity configurations, EC-HTE reduces $|\text{bias}|$ from 0.025 (global) to 0.006, a $4\times$ improvement, with lower RMSE (0.033 vs.\ 0.040) and substantially better coverage (0.90 vs.\ 0.78); however, this advantage does not generalize across all asymmetric settings (see below).
458	
459	\begin{table}[t]
460	\centering
461	\caption{Asymmetric misclassification results ($K{=}2$, $n_{\text{expert}}{=}250$, 100 MC runs). Values averaged over subgroups, $z$-levels, and $\Delta\tau$.}
462	\label{tab:asymmetric}
463	\small
464	\begin{tabular}{l ccc}
465	\toprule
466	Method & $|\text{Bias}| \downarrow$ & RMSE $\downarrow$ & Coverage $\uparrow$ \\
467	\midrule
468	Naive & 0.047 & 0.053 & 0.48 \\
469	Global & 0.025 & 0.040 & 0.78 \\
470	HB EC-HTE & \textbf{0.006} & \textbf{0.033} & \textbf{0.90} \\
471	\bottomrule
472	\end{tabular}
473	\end{table}
474	
475	\paragraph{Comprehensive grid evaluation (48 configurations).}
476	
477	To assess robustness beyond the three configurations above, we evaluate the product structure and correction methods across a factorial grid of 6 FPR/FNR ratios $\times$ 4 $\Delta\pi$ levels $\times$ 2 subgroup counts ($K \in \{2, 4\}$), yielding 48 configurations with 100 MC runs each ($n_{\text{expert}} = 250$).
478	
479	Table~\ref{tab:asym_r2_grid} reports $R^2$ between analytic predictions and MC bias.
480	The product structure holds reliably at $\Delta\pi \geq 0.10$ ($R^2 > 0.73$ across all ratios and $K$ values); at $\Delta\pi = 0.05$, $R^2$ degrades for extreme ratios (e.g., $\leq 0.21$ at 2:1 and 5:1, $K{=}2$) because both predicted and observed biases approach zero, making the regression ill-conditioned rather than indicating structural failure.
481	
482	\begin{table}[h]
483	\centering
484	\caption{$R^2$ of bias identity predictions under asymmetric misclassification (100 MC runs per cell). Product structure holds at $\Delta\pi \geq 0.10$; low $R^2$ at $\Delta\pi = 0.05$ reflects near-zero bias magnitudes.}
485	\label{tab:asym_r2_grid}
486	\small
487	\begin{tabular}{l cccc}
488	\toprule
489	& \multicolumn{4}{c}{$\Delta\pi$} \\
490	\cmidrule(lr){2-5}
491	FPR:FNR & 0.05 & 0.10 & 0.15 & 0.20 \\
492	\midrule
493	\multicolumn{5}{l}{\emph{$K = 2$}} \\
494	1:2 & 0.84 & 0.92 & 0.97 & 0.98 \\
495	1:3 & 0.82 & 0.92 & 0.94 & 0.96 \\
496	1:5 & 0.73 & 0.90 & 0.95 & 0.96 \\
497	2:1 & 0.21 & 0.90 & 0.94 & 0.96 \\
498	3:1 & 0.50 & 0.91 & 0.97 & 0.99 \\
499	5:1 & 0.05 & 0.83 & 0.97 & 0.98 \\
500	\midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2a1fd7e-5865-447f-94a8-67171fb5aed8",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "5ecd7ede-b4e0-4bc7-95bd-b5ccff490180",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
      "content": "\\section{EC-HTE Procedure}\n\\label{app:algorithm}\n\n\\begin{algorithm}[t]\n\\caption{EC-HTE: Error-Corrected Heterogeneous Treatment Effects}\n\\label{alg:echte}\n\\begin{algorithmic}[1]\n\\Require Observations $\\{(Y_i, W_i, \\hat{Z}_i, X_i)\\}_{i=1}^N$; expert labels $\\{Z_j^*\\}_{j=1}^{n_{\\text{expert}}}$; subgroup map $S: \\mathcal{X} \\to \\{1,\\ldots,K\\}$\n\\Ensure Corrected CATE estimates $\\hat{\\tau}(z)$ with variance-adjusted CIs\n\\Statex\n\\State \\textbf{Preconditions:} verify $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$ and $\\max_s(\\text{FPR}_s, \\text{FNR}_s) < 0.5$; if either fails, use global correction\n\\Statex\n\\State \\textbf{Step 1: Estimate per-subgroup confusion matrices (HB)}\n\\State $\\alpha_0 \\gets \\arg\\max_{\\alpha} \\prod_{s=1}^{K} p(\\text{data}_s \\mid \\alpha, \\hat{C}_{\\text{global}})$ \\Comment{empirical Bayes}\n\\For{$s = 1, \\ldots, K$}\n    \\State $C_s[j,\\cdot] \\sim \\mathrm{Dir}(\\alpha_0 \\cdot \\hat{C}_{\\text{global},j})$\n    \\State $\\hat{C}_s[j,k] \\gets \\frac{n_{s,jk} + \\alpha_0 \\cdot \\hat{C}_{\\text{global},j,k}}{n_{s,j\\cdot} + \\alpha_0}$ \\Comment{posterior mean}\n\\EndFor\n\\Statex\n\\State \\textbf{Step 2: Correct observed outcome moments}\n\\For{$s = 1, \\ldots, K$}\n    \\If{$\\kappa(\\hat{C}_s) > 100$} $\\hat{C}_s \\gets \\bar{C}$ \\Comment{singularity guard}\n    \\EndIf\n    \\State $\\tilde{\\boldsymbol{\\mu}}_s \\gets \\hat{C}_s^{-1} \\hat{\\boldsymbol{\\mu}}_s$\n\\EndFor\n\\Statex\n\\State \\textbf{Step 3: CausalForestDML with variance-adjusted SEs}\n\\State Train CausalForest (honest splitting) on corrected outcome moments $\\tilde{\\boldsymbol{\\mu}}_s$\n\\State $\\mathrm{se}_{\\mathrm{adj},i} \\gets \\sqrt{\\mathrm{diag}(\\hat{C}_{S_i}^{-1}\\, \\mathrm{diag}(\\mathrm{se}_i^2)\\, \\hat{C}_{S_i}^{-\\top})}$\n\\State \\Return $\\hat{\\tau}(z)$ with 95\\% CIs from $\\mathrm{se}_{\\mathrm{adj}}$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\subsection{Condition Number Guard Ablation}\n\\label{app:kappa_ablation}\n\nThe singularity guard in Algorithm~\\ref{alg:echte} (line~6) falls back to global correction when $\\kappa(\\hat{C}_s) > 100$.\nWe verify that this threshold is not load-bearing by sweeping $\\kappa \\in \\{10, 25, 50, 100, 200, 500, 1000\\}$ under the standard DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs).\nAcross all configurations, the maximum observed condition number is $\\kappa_{\\max} = 1.89$ (mean 1.45, p99 1.89), providing a $53{\\times}$ safety margin below the $\\kappa{=}100$ threshold.\nConsequently, the guard never triggers at any tested threshold, and all $\\kappa$ values produce identical RMSE (HB: 0.076, Global: 0.077) and zero numerical instability.\nIn a stress test with near-random labeling ($\\pi_s \\approx 0.4$--$0.5$, $n_{\\text{expert}}{=}50$), the maximum condition number reaches 1{,}125, correctly triggering the $\\kappa{=}100$ guard and preventing catastrophic inversion.\nThe adaptive formula $\\kappa_{\\text{adapt}} = 10 \\sqrt{n_{\\text{expert}} / K}$ recovers $\\kappa{=}100$ for this regime and scales naturally with the estimation precision.\n\n\\section{Full Proof of Theorem~\\ref{thm:bias_identity}}\n\\label{app:derivation}\n\n\\paragraph{Setup.}\nUnder assumptions (A1)--(A4), the observed CATE in subgroup $s$ at effect-modifier level $z$ is\n\\begin{equation}\n\\tau_{\\text{obs}}(z, s) = \\sum_{z'} M_s[z, z'] \\cdot \\tau(z'),\n\\end{equation}\nwhere $M_s[z, z'] = P(Z{=}z' \\mid \\hat{Z}{=}z, S{=}s)$ is the mixing matrix.\nUnder (A2)--(A3), $M_s = \\bigl[\\begin{smallmatrix} 1-\\pi_s & \\pi_s \\\\ \\pi_s & 1-\\pi_s \\end{smallmatrix}\\bigr]$.\n\n\\paragraph{Global correction.}\nThe pooled mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s = \\bigl[\\begin{smallmatrix} 1-\\bar{\\pi} & \\bar{\\pi} \\\\ \\bar{\\pi} & 1-\\bar{\\pi} \\end{smallmatrix}\\bigr]$, with $\\bar{\\pi} = \\sum_s w_s \\pi_s$.\n\nGlobal correction applies $M_{\\text{global}}^{-1}$ to $\\tau_{\\text{obs}}(\\cdot, s)$:\n\\begin{equation}\n\\hat{\\tau}_{\\text{global}}(z, s) = [M_{\\text{global}}^{-1} M_s \\cdot \\boldsymbol{\\tau}]_z,\n\\end{equation}\nwhere $\\boldsymbol{\\tau} = [\\tau(0), \\tau(1)]^\\top$.\n\n\\paragraph{Bias computation.}\nThe bias is $\\hat{\\tau}_{\\text{global}}(z, s) - \\tau(z) = [(M_{\\text{global}}^{-1} M_s - I) \\boldsymbol{\\tau}]_z$.\n\nDirect computation gives:\n\\begin{equation}\nM_{\\text{global}}^{-1} = \\frac{1}{1 - 2\\bar{\\pi}} \\begin{bmatrix} 1-\\bar{\\pi} & -\\bar{\\pi} \\\\ -\\bar{\\pi} & 1-\\bar{\\pi} \\end{bmatrix}.\n\\end{equation}\nMultiplying by $M_s$:\n\\begin{equation}\n\\resizebox{.88\\columnwidth}{!}{$\\displaystyle\nM_{\\text{global}}^{-1} M_s = \\frac{1}{1-2\\bar{\\pi}} \\begin{bmatrix} (1{-}\\bar{\\pi})(1{-}\\pi_s) - \\bar{\\pi}\\pi_s & (1{-}\\bar{\\pi})\\pi_s - \\bar{\\pi}(1{-}\\pi_s) \\\\ -\\bar{\\pi}(1{-}\\pi_s) + (1{-}\\bar{\\pi})\\pi_s & -\\bar{\\pi}\\pi_s + (1{-}\\bar{\\pi})(1{-}\\pi_s) \\end{bmatrix}.\n$}\n\\end{equation}\n\nDefine $\\delta_s = \\pi_s - \\bar{\\pi}$. Substituting $\\pi_s = \\bar{\\pi} + \\delta_s$:\n\\begin{equation}\nM_{\\text{global}}^{-1} M_s - I = \\frac{\\delta_s}{1-2\\bar{\\pi}} \\begin{bmatrix} -1 & 1 \\\\ 1 & -1 \\end{bmatrix}.\n\\end{equation}\n\nTo verify: the $(1,1)$ entry of $M_{\\text{global}}^{-1} M_s$ is\n{\\small\n\\begin{align}\n&\\frac{(1{-}\\bar{\\pi})(1{-}\\bar{\\pi}{-}\\delta_s) - \\bar{\\pi}(\\bar{\\pi}{+}\\delta_s)}{1-2\\bar{\\pi}} \\nonumber\\\\\n&= \\frac{(1{-}\\bar{\\pi})^2 - (1{-}\\bar{\\pi})\\delta_s - \\bar{\\pi}^2 - \\bar{\\pi}\\delta_s}{1-2\\bar{\\pi}} \\nonumber\\\\\n&= \\frac{1 - 2\\bar{\\pi} - \\delta_s}{1-2\\bar{\\pi}} = 1 - \\frac{\\delta_s}{1-2\\bar{\\pi}}.\n\\end{align}\n}\n\nApplying $(M_{\\text{global}}^{-1} M_s - I)$ to $\\boldsymbol{\\tau}$:\n{\\small\n\\begin{align}\n\\text{bias}(z{=}0, s) &= \\tfrac{\\delta_s}{1-2\\bar{\\pi}}(-\\tau(0) + \\tau(1)) = +\\tfrac{\\delta_s \\cdot \\Delta\\tau}{1-2\\bar{\\pi}}, \\\\\n\\text{bias}(z{=}1, s) &= \\tfrac{\\delta_s}{1-2\\bar{\\pi}}(\\tau(0) - \\tau(1)) = -\\tfrac{\\delta_s \\cdot \\Delta\\tau}{1-2\\bar{\\pi}},\n\\end{align}\n}\nwhere $\\Delta\\tau = \\tau(1) - \\tau(0)$. \\qed\n\n\\paragraph{Finite-sample remainder.}\nWhen $\\hat{C}_s = C_s + E_s$ with $\\|E_s\\| = O_p(n_{\\text{expert}}^{-1/2})$ (central limit theorem), the estimated correction $\\hat{M}_{\\text{global}}^{-1} \\hat{M}_s$ deviates from its population counterpart by\n$\\|\\hat{M}_{\\text{global}}^{-1} \\hat{M}_s - M_{\\text{global}}^{-1} M_s\\| \\leq \\kappa(M_{\\text{global}})^2 \\cdot O_p(n_{\\text{expert}}^{-1/2})$,\nwhere $\\kappa(M) = \\|M\\| \\cdot \\|M^{-1}\\|$ is the condition number~\\citep{stewart1990matrix}; the squared exponent arises because the first-order perturbation of $M^{-1}$ introduces one factor of $\\|M^{-1}\\|$, and the product $M_{\\text{global}}^{-1} M_s$ introduces a second (see the Neumann expansion in Section~\\ref{sec:theory}).\nThis motivates the $\\kappa > 100$ singularity guard in Section~\\ref{sec:method}.\n\n\\section{Multi-class Extension and Proof}\n\\label{app:multiclass}\n\n\\begin{corollary}[Multi-class Extension]\n\\label{cor:multiclass}\nFor $K > 2$ subgroups with $J$ effect-modifier levels and uniform off-diagonal misclassification (misclassified observations from class $j$ are distributed equally among the remaining $J{-}1$ classes), the subgroup bias of global correction generalizes to\n\\begin{equation}\n\\mathrm{bias}_{\\mathrm{global}}(z, s) = \\sum_{j=1}^{J} \\bigl(\\bar{\\pi}_j - \\pi_{s,j}\\bigr) \\cdot \\bigl(\\tau(j) - \\bar{\\tau}\\bigr) \\cdot g(\\bar{\\pi}),\n\\label{eq:multiclass}\n\\end{equation}\nwhere $g(\\bar{\\pi})$ collects the matrix-inversion amplification terms.\\footnote{For $J=3$ with symmetric misclassification (off-diagonal errors uniform), $g(\\bar{\\pi}) = 1/(1 - 3\\bar{\\pi}/2)$, generalizing the $J{=}2$ factor $1/(1-2\\bar{\\pi})$. In general, $g(\\bar{\\pi}) = 1/(1 - J\\bar{\\pi}/(J-1))$.}\nThe essential structure, $\\sum_s w_s (\\bar{\\pi}_j - \\pi_{s,j}) = 0$, ensures that bias redistributes across subgroups rather than vanishing in aggregate.\n\\end{corollary}\n\n\\paragraph{Proof.}\nFor $K > 2$ subgroups with $J$ effect-modifier levels, the subgroup-specific mixing matrix $M_s$ is $J \\times J$ with entries $M_s[j, j'] = P(Z{=}j' \\mid \\hat{Z}{=}j, S{=}s)$.\nThe global mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s$.\n\nThe bias of global correction in subgroup $s$ at level $z$ is:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = [(M_{\\text{global}}^{-1} M_s - I) \\boldsymbol{\\tau}]_z.\n\\end{equation}\n\nWrite $M_s = M_{\\text{global}} + \\Delta_s$ where $\\Delta_s = M_s - M_{\\text{global}}$ satisfies $\\sum_s w_s \\Delta_s = 0$.\nThen $M_{\\text{global}}^{-1} M_s = I + M_{\\text{global}}^{-1} \\Delta_s$, so:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = [M_{\\text{global}}^{-1} \\Delta_s \\cdot \\boldsymbol{\\tau}]_z.\n\\end{equation}\n\nFor symmetric misclassification with per-class error rates $\\pi_{s,j}$ and pooled rates $\\bar{\\pi}_j$, the entries of $\\Delta_s$ have the form $\\Delta_s[j,j'] = (\\bar{\\pi}_j - \\pi_{s,j}) \\cdot h(j, j')$ for a function $h$ determined by the off-diagonal redistribution pattern.\nExpanding the matrix-vector product and collecting terms yields:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = \\sum_{j=1}^{J} (\\bar{\\pi}_j - \\pi_{s,j}) \\cdot (\\tau(j) - \\bar{\\tau}) \\cdot g(\\bar{\\pi}),\n\\end{equation}\nwhere $g(\\bar{\\pi})$ collects the matrix-inversion amplification terms and $\\bar{\\tau} = \\sum_j P(Z{=}j) \\tau(j)$.\n\nThe essential structure $\\sum_s w_s (\\bar{\\pi}_j - \\pi_{s,j}) = 0$ ensures that the weighted bias across subgroups sums to zero: global correction redistributes bias rather than creating or eliminating it in aggregate.\nFor non-uniform off-diagonal entries, the scalar amplification $g(\\bar{\\pi})$ generalizes to a cell-specific matrix; the product structure $B_s \\cdot \\Delta\\tau$ persists but a closed-form amplification factor does not. \\qed\n\n\\section{Proof of Proposition~\\ref{prop:debiasing_hurts}}\n\\label{app:debiasing_hurts}\n\nThe naive estimator has bias $\\tau_{\\text{obs}}(z,s) - \\tau(z)$.\nUnder (A2)--(A3), $\\tau_{\\text{obs}}(0,s) = (1-\\pi_s)\\tau(0) + \\pi_s\\tau(1)$, so $\\text{bias}_{\\text{naive}}(0,s) = \\pi_s \\cdot \\Delta\\tau$.\n\nGlobal correction produces larger absolute bias when $|\\text{bias}_{\\text{global}}(0,s)| > |\\text{bias}_{\\text{naive}}(0,s)|$:\n\\begin{equation}\n\\frac{|\\delta_s| \\cdot |\\Delta\\tau|}{|1-2\\bar{\\pi}|} > \\pi_s \\cdot |\\Delta\\tau|.\n\\end{equation}\nSince $\\Delta\\tau \\neq 0$ (otherwise both biases are zero), dividing through gives:\n\\begin{equation}\n\\frac{|\\delta_s|}{(1-2\\bar{\\pi}) \\cdot \\pi_s} > 1,\n\\end{equation}\nwhere we use $1-2\\bar{\\pi} > 0$ from (A4).\n\nFor high-error subgroups ($\\pi_s > \\bar{\\pi}$, so $\\delta_s > 0$): the condition becomes $(\\pi_s - \\bar{\\pi}) / ((1-2\\bar{\\pi})\\pi_s) > 1$, which simplifies to $\\pi_s(1 - 1 + 2\\bar{\\pi}) > \\bar{\\pi}$, i.e., $2\\bar{\\pi}\\pi_s > \\bar{\\pi}$, i.e., $\\pi_s > 0.5$.\nThis is excluded by (A4), so global correction always reduces bias in high-error subgroups.\n\nFor low-error subgroups ($\\pi_s < \\bar{\\pi}$, so $\\delta_s < 0$): the condition becomes $(\\bar{\\pi} - \\pi_s) / ((1-2\\bar{\\pi})\\pi_s) > 1$, which gives $\\pi_s < \\bar{\\pi} / (1 - 2\\bar{\\pi} + 1) = \\bar{\\pi} / (2(1-\\bar{\\pi}))$.\nWhen $\\bar{\\pi} = 0.15$, any subgroup with $\\pi_s < 0.088$ experiences increased bias from global correction. \\qed\n\n\\paragraph{Extension to asymmetric misclassification.}\nProposition~\\ref{prop:debiasing_hurts} assumes symmetric error rates (A2).\nUnder asymmetric misclassification ($\\mathrm{FPR}_s \\neq \\mathrm{FNR}_s$) with balanced $Z$ (A3), the naive bias becomes $\\mathrm{bias}_{\\mathrm{naive}}(0,s) = \\mathrm{FNR}_s \\cdot \\Delta\\tau / (1 - \\mathrm{FPR}_s + \\mathrm{FNR}_s)$, involving both error rates and a normalization denominator; the global correction bias depends on the full $2 \\times 2$ structure of $B_s = M_{\\mathrm{global}}^{-1} M_s - I$ (Remark~\\ref{rem:asymmetric} in Section~\\ref{sec:theory}).\nA sufficient condition for global correction to increase bias is\n\\begin{equation}\n\\max_{i,j}|[B_s]_{i,j}| > \\max(\\mathrm{FPR}_s, \\mathrm{FNR}_s),\n\\end{equation}\nwhich reduces to Equation~\\eqref{eq:hurts_condition} when $\\mathrm{FPR}_s = \\mathrm{FNR}_s = \\pi_s$.\nIn the asymmetric experiments (Appendix~\\ref{app:asymmetric}), the scalar diagnostic achieves per-subgroup AUC $= 0.96$ when applied with $\\pi_s = (\\mathrm{FPR}_s + \\mathrm{FNR}_s)/2$ (48 asymmetric configurations, FPR/FNR ratios 1:5 to 5:1), and AUC $= 1.00$ on 8 semi-real LLM confusion matrices, confirming that the symmetric simplification preserves diagnostic validity under practical asymmetry.\n\n\\section{Semi-Synthetic Data Generating Process}\n\\label{app:dgp}\n\n\\paragraph{Synthetic DGP (Sections~\\ref{sec:bias_mechanism}--\\ref{sec:diagnostic} and Appendix~\\ref{sec:budget}).}\nWe generate $N = 5000$ observations.\nEach observation belongs to one of $K \\in \\{2, 4\\}$ subgroups $S \\in \\{1, \\ldots, K\\}$ with equal weights $w_s = 1/K$.\nThe binary effect modifier $Z \\in \\{0, 1\\}$ is drawn with $P(Z{=}1) = 0.5$.\nTreatment assignment is $T \\sim \\text{Bernoulli}(0.5)$, independent of $Z$ and $S$.\n\nThe outcome is generated as:\n\\begin{equation}\nY = \\tau(Z) \\cdot T + \\eta, \\quad \\eta \\sim \\mathcal{N}(0, 1),\n\\end{equation}\nwhere the CATE function is $\\tau(z) = \\bar{\\tau} + \\Delta\\tau \\cdot (z - 0.5)$ with $\\bar{\\tau} = 0.5$.\nThe CATE heterogeneity $\\Delta\\tau \\in \\{0, 0.2, 0.5, 1.0\\}$ controls the strength of treatment effect variation across levels of $Z$.\n\nMisclassification is symmetric: $\\hat{Z} \\neq Z$ with probability $\\pi_s$ depending on subgroup.\nFor $K{=}2$: $\\pi_1 = \\bar{\\pi} - \\Delta_c/2$, $\\pi_2 = \\bar{\\pi} + \\Delta_c/2$, with $\\bar{\\pi} \\in \\{0.1, 0.2\\}$ and $\\Delta_c \\in \\{0, 0.05, 0.1, 0.15\\}$.\nFor $K{=}4$, extreme regime: $\\pi \\in \\{0.05, 0.10, 0.15, 0.25\\}$; moderate regime: $\\pi \\in \\{0.08, 0.12, 0.16, 0.20\\}$.\n\nExpert labels are drawn as a simple random sample of size $n_{\\text{expert}} \\in \\{50, 100, 250, 500, 1000, 2000\\}$ from the full dataset, with true $Z$ observed for these observations.\n\n\\paragraph{Semi-synthetic DGP (Section~\\ref{sec:ec_hte_eval}).}\nWe sample $N = 5000$ tweets from the TweetEval sentiment corpus ($N_{\\text{pool}} = 57{,}899$).\nSubgroups are defined by crossing \\texttt{has\\_hashtag} $\\times$ \\texttt{text\\_length\\_bin} (short/medium/long), yielding $K = 4$ subgroups with empirical sizes: $S_0 \\approx 38\\%$, $S_1 \\approx 38\\%$, $S_2 \\approx 12\\%$, $S_3 \\approx 12\\%$.\nMisclassification rates in the extreme regime are $\\pi_{S_0} = 0.05$, $\\pi_{S_1} = 0.10$, $\\pi_{S_2} = 0.15$, $\\pi_{S_3} = 0.25$, reflecting empirical evidence that hashtag-heavy text degrades LLM classifier accuracy.\nThe outcome DGP follows the same structure as the synthetic case, with CATE injected onto the real text-derived subgroup structure.\n\n\\paragraph{PPCI DGPs (Appendix~\\ref{sec:ppci}).}\nFour DGPs isolate error types: (A) covariate error only ($\\sigma_{\\text{outcome}} = 0$), (B) outcome error only ($\\sigma_{\\text{outcome}} = 0.5$), (C) both errors ($\\sigma_{\\text{outcome}} = 0.5$), (D) no error ($\\sigma_{\\text{outcome}} = 0$).\nOutcome-side error is additive Gaussian noise on $Y$.\n\n\\paragraph{CausalForestDML hyperparameters.}\nAll CausalForest experiments use \\texttt{econml.dml.CausalForestDML} with honest splitting, $n_{\\text{estimators}} = 48$, $\\texttt{min\\_samples\\_leaf} = 20$, \\texttt{model\\_y} = \\texttt{LassoCV}(cv=3), and \\texttt{model\\_t} = \\texttt{LogisticRegressionCV}.\nThese defaults were held constant across all configurations; no hyperparameter tuning was performed.\n\n% [Promoted to main text — Figure~\\ref{fig:heatmap}]\n\n\\section{Extended Related Work}\n\\label{app:related}\n\n\\paragraph{Measurement error details.}\n\\citet{fuller1987measurement} establish the foundational theory showing that naive regression with mismeasured covariates yields attenuated coefficient estimates.\n\\citet{carroll2006measurement} extend this to nonlinear models.\n\\citet{gustafson2003measurement} develops Bayesian treatments modeling measurement jointly with outcomes.\n\\citet{hu2008nonparametric} provide nonparametric identification using repeated measurements or instruments.\n\n\\paragraph{Annotation model extensions.}\nBeyond the foundational \\citet{dawid1979maximum} model, \\citet{passonneau2014benefits} incorporate item difficulty, \\citet{hovy2013learning} learn annotator competence, and \\citet{paun2018comparing} introduce hierarchical priors sharing information across annotators with varying expertise.\n\n\\paragraph{PPI extensions and text-as-data methods.}\n\\citet{zrnic2024cross} extend PPI via cross-prediction; their active inference framework~\\citep{zrnic2024active} achieves $>$80\\% expert budget savings through adaptive allocation, complementary to our fixed-budget analysis.\n\\citet{grimmer2022text} provide methodological guidance for text-as-data pipelines.\n\\citet{audinet2025benchmarking} systematically benchmark DSL and PPI methods for LLM-based parameter estimation, finding that debiasing can increase MSE when prediction error is heterogeneous---a population-level analogue of the subgroup-conditional bias amplification we formalize in Theorem~\\ref{thm:bias_identity}.\n\n\\paragraph{Treatment vs.\\ effect-modifier misclassification.}\n\\citet{imai2010causal} study treatment misclassification where errors change which arm a unit is assigned to, requiring instrumental variables or partial identification because the fundamental treated-vs-control contrast is corrupted.\nOur problem preserves the treatment contrast ($T$ is observed correctly) but corrupts the heterogeneity structure ($\\hat{Z} \\neq Z$).\nThe ATE remains identified; only conditional effects are biased, which makes exact correction through confusion matrix inversion feasible.\n\\citet{knox2020administrative} demonstrate how racial misclassification in administrative records biases causal estimates; \\citet{blette2024assessing} handle missing (not misclassified) effect modifier data in cluster-RCTs via multiple imputation---a complementary problem to our confusion-matrix correction setting.\n\n\\paragraph{Econometrics of binary misclassification.}\n\\citet{bound2001measurement} survey measurement error in survey data, establishing that binary misclassification attenuates regression coefficients.\n\\citet{frazis2003estimating} derive exact bias formulas for OLS with a misclassified binary regressor, showing attenuation proportional to the misclassification rate---analogous to our Theorem~\\ref{thm:bias_identity} but restricted to average effects without subgroup heterogeneity.\n\\citet{black2000racial} demonstrate that racial misclassification in administrative data can substantially bias estimates of racial disparities.\n\\citet{mahajan2006identification} and \\citet{lewbel2007estimation} develop instrumental variable approaches to identify models with misclassified binary regressors, requiring exclusion restrictions unavailable when the mismeasured variable is an LLM annotation.\nOur setting differs in three respects: (i) the mismeasured variable is an effect modifier indexing the CATE function, not a standard regressor; (ii) misclassification rates vary across subgroups, creating the $\\delta_s \\times \\Delta\\tau$ product amplification absent from homogeneous-error analyses; and (iii) expert labels provide a direct calibration sample, enabling confusion matrix estimation without instruments.\n\n\\section{MCMC Convergence Diagnostics}\n\\label{app:mcmc}\n\nMain experiments use empirical Bayes point estimates ($<$5ms per subgroup).\nThis appendix reports MCMC validation (4 chains, 4000 iterations, 2000 warmup) confirming EB and full posterior agreement within simulation error.\nMain experiments (Table~\\ref{tab:main_results}) use a Dirichlet prior centered on $\\hat{C}_{\\text{global}}$ with concentration $\\alpha_0$ estimated via empirical Bayes (marginal likelihood).\nAppendix robustness experiments use a fixed Dirichlet prior ($\\alpha{=}3$); since fixed-$\\alpha$ partial pooling is weakly dominated by the adaptive variant, these results are conservative.\nAll runs achieve $\\hat{R} < 1.0034$ and ESS $> 1618$, confirming convergence with substantial margin.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nDiagnostic & Threshold & Achieved \\\\\n\\midrule\n$\\hat{R}$ (max across all params) & $< 1.01$ & $< 1.0034$ \\\\\nESS (min across all params) & $> 845$ & $> 1618$ \\\\\nDivergent transitions & $= 0$ & $0$ \\\\\nSingularity guard triggers & --- & extreme/$n{=}50$ only \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{MCMC convergence diagnostics for the hierarchical Bayesian estimator. All configurations satisfy convergence criteria with substantial margin.}\n\\label{tab:mcmc}\n\\end{table}\n\n\\subsection{Hyperprior Sensitivity}\n\\label{app:hyperprior}\n\nWe sweep the $\\text{Gamma}(a_0, b_0)$ hyperprior on the concentration parameter $\\alpha_0$ across 15 configurations ($a_0 \\in \\{1, 2, 3, 4, 5\\}$, $b_0 \\in \\{0.5, 1.0, 2.0\\}$) under the standard synthetic DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs).\n\n\\begin{table}[h]\n\\centering\n\\caption{Hyperprior sensitivity summary. RMSE and coverage across 15 $(a_0, b_0)$ configurations. The default $\\text{Gamma}(3, 1)$ ranks 8th of 15 by RMSE; the best configuration $\\text{Gamma}(1, 0.5)$ yields only 1.9\\% improvement. Excluding extreme configurations ($a_0 \\cdot b_0 > 8$), RMSE varies by $<$6\\%.}\n\\label{tab:hyperprior_sweep}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nDefault $\\text{Gamma}(3, 1)$ RMSE & 0.0841 \\\\\nBest $\\text{Gamma}(1, 0.5)$ RMSE & 0.0825 \\\\\nRMSE range (reasonable configs) & 6.0\\% \\\\\nRMSE range (all 15 configs) & 17.3\\% \\\\\nCoverage range & 0.925--0.938 \\\\\nDefault rank & 8 / 15 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nScaling the $\\text{Gamma}(3, 1)$ hyperprior by factors of $0.5\\times$ to $2\\times$ produces $<$1\\% RMSE variation for $K{=}2$ and $\\sim$4--5\\% for $K{=}4$.\nCoverage remains invariant across the sensitivity range ($\\Delta < 1.3$pp).\nThese results confirm that the hierarchical estimator is robust to prior specification within a reasonable range; the default $\\text{Gamma}(3, 1)$ is near-median, and no configuration achieves more than 1.9\\% RMSE improvement over the default.\n\n\\section{Diagnostic ROC Curves}\n\\label{app:roc}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_roc.png}\n\\caption{ROC curves for the $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}): $|\\delta_s|/((1{-}2\\bar\\pi)\\cdot\\pi_s)>1$. (A)~Setting-level ROC (AUC $= 0.89$), compared with the $|\\Delta\\pi \\times \\Delta\\tau|$ product (AUC $= 0.89$) and $\\mathrm{CV}(\\pi_s)$ (AUC $= 0.97$). (B)~Subgroup-level ROC: the $\\Delta\\pi$-only condition (AUC $= 0.86$) substantially outperforms the $|\\Delta\\pi \\times \\Delta\\tau|$ product (AUC $= 0.73$). The $\\Delta\\tau$-free diagnostic depends only on estimable misclassification rates, breaking the circular dependency that would arise if CATE heterogeneity were required.}\n\\label{fig:roc}\n\\end{figure}\n\n\\paragraph{Cost-asymmetric diagnostic thresholds.}\nIn practice, the cost of a false negative (failing to detect that global correction increases bias) exceeds the cost of a false positive (unnecessarily applying EC-HTE when global correction would suffice), because the former propagates systematic bias into CATE estimates while the latter only incurs additional estimation variance.\nPractitioners in high-stakes settings (e.g., policy evaluation where CATE estimates inform resource allocation) should lower the diagnostic threshold to favor recall over precision, accepting more false positives to minimize the risk of undetected bias amplification.\n\n\\section{Expert Budget Crossover Curves}\n\\label{app:budget}\n\\label{sec:budget}\n\nThe crossover point at which EC-HTE achieves lower RMSE than global correction depends on the DGP: $n_{\\text{expert}} = 250$ for $K{=}2$/extreme and $n_{\\text{expert}} = 1000$ for $K{=}4$/extreme under $\\Delta\\tau{=}0.3$ (Figure~\\ref{fig:budget}); under the Table~\\ref{tab:main_results} DGP, the $K{=}4$ crossover occurs at $n_{\\text{expert}} \\approx 500$.\nUnder moderate heterogeneity ($K{=}2$), EC-HTE never achieves lower RMSE than global at any budget.\nHB partial pooling improves over stratified MLE in 21 of 24 configurations, with the two estimators converging by $n_{\\text{expert}} \\geq 1000$.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig3_budget.pdf}\n\\caption{RMSE vs.\\ expert budget ($n_{\\text{expert}}$) across four regime$\\times K$ combinations. Dashed vertical lines mark crossover points where EC-HTE achieves lower RMSE than global correction: $n{=}250$ ($K{=}2$, extreme), $n{=}1000$ ($K{=}4$, extreme). Under moderate heterogeneity ($K{=}2$), global correction dominates at all budgets. Shaded bands show $\\pm 1$ SD across subgroups within each configuration.}\n\\label{fig:budget}\n\\end{figure*}\n\n\\subsection{Budget Sensitivity: HB vs.\\ Stratified MLE}\n\\label{app:budget_sensitivity}\n\nHierarchical Bayes (HB) partial pooling borrows strength across subgroups, which should matter most when per-subgroup expert labels are scarce.\nWe sweep $n_{\\text{expert}} \\in \\{25, 50, 75, 100, 150, 250\\}$ under extreme heterogeneity ($\\Delta\\tau{=}0.3$, 100 MC runs, $N{=}5{,}000$).\nTable~\\ref{tab:budget_sensitivity} reports aggregate RMSE for global correction, stratified MLE, and HB EC-HTE.\n\n\\begin{table}[h]\n\\centering\n\\caption{RMSE across expert budgets under extreme heterogeneity.\nHB crossover (first budget where HB $<$ MLE) occurs at approximately 10 expert labels per subgroup-cell:\n$n_{\\text{expert}}{=}50$ for $K{=}2$ and $n_{\\text{expert}}{=}75$ for $K{=}4$.}\n\\label{tab:budget_sensitivity}\n\\small\n\\begin{tabular}{crrrrc}\n\\toprule\n$K$ & $n_{\\text{expert}}$ & Global & Strat.\\ MLE & HB EC-HTE & HB vs.\\ MLE \\\\\n\\midrule\n2 & 25 & \\textbf{0.101} & 0.256 & 0.269 & $+4.9\\%$ \\\\\n2 & 50 & \\textbf{0.088} & 0.275 & 0.231 & $\\mathbf{-16.1\\%}$ \\\\\n2 & 75 & 0.084 & 0.091 & \\textbf{0.089} & $-1.9\\%$ \\\\\n2 & 100 & 0.083 & 0.085 & \\textbf{0.084} & $-0.8\\%$ \\\\\n2 & 150 & 0.081 & 0.077 & \\textbf{0.077} & $-0.4\\%$ \\\\\n2 & 250 & 0.080 & 0.075 & \\textbf{0.074} & $-0.1\\%$ \\\\\n\\midrule\n4 & 25 & \\textbf{0.129} & 0.401 & 0.612 & $+52.5\\%$ \\\\\n4 & 50 & \\textbf{0.117} & 0.380 & 0.470 & $+23.8\\%$ \\\\\n4 & 75 & \\textbf{0.112} & 0.221 & 0.211 & $\\mathbf{-4.4\\%}$ \\\\\n4 & 100 & \\textbf{0.112} & 0.215 & 0.212 & $-1.3\\%$ \\\\\n4 & 150 & \\textbf{0.109} & 0.157 & 0.152 & $-3.6\\%$ \\\\\n4 & 250 & \\textbf{0.108} & 0.127 & 0.126 & $-1.0\\%$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree regimes emerge.\nAt very low budgets ($n_{\\text{expert}} < 50$ for $K{=}2$, $< 75$ for $K{=}4$), per-subgroup counts are insufficient for reliable confusion matrix estimation; global pooling dominates because the variance cost of stratification overwhelms any bias reduction.\nHB degrades substantially in this regime because the Gibbs posterior, while better regularized than MLE, still cannot overcome the fundamental sample-size constraint with $\\sim$6--12 labels per subgroup.\nAt moderate budgets ($n_{\\text{expert}} = 50$--$250$ for $K{=}2$, $75$--$250$ for $K{=}4$), HB partial pooling provides consistent RMSE improvement over stratified MLE ($-0.4\\%$ to $-16.1\\%$), with the largest gains near the crossover point.\nAt high budgets ($n_{\\text{expert}} \\geq 250$), both estimators converge as subgroup-level data becomes sufficient for reliable MLE; the HB advantage diminishes to $< 1\\%$.\nCoverage remains $\\geq 0.88$ for both methods across all budget levels.\n\n\\subsection{Scalability to $K{=}8$ Subgroups}\n\\label{app:k8_subgroups}\n\nWe test EC-HTE at $K{=}8$ to identify the scalability boundary of hierarchical Bayesian partial pooling under fixed expert budget.\n\n\\paragraph{Setup.}\n$N{=}5{,}000$, $K{=}8$ (equal-weight subgroups), $n_{\\text{expert}}{=}250$ (${\\approx}31$ labels per subgroup), 100 MC replications.\nMisclassification rates are uniformly spread: $\\pi_s \\in \\{0.05, 0.09, 0.13, 0.18, 0.22, 0.26, 0.30, 0.35\\}$.\nTreatment effects depend on $Z$ (not subgroup): $\\tau(Z{=}0){=}0$, $\\tau(Z{=}1){=}0.3$.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE at $K{=}8$ ($n_{\\text{expert}}{=}250$, ${\\approx}31$ labels/subgroup, 100 MC).}\n\\label{tab:k8_subgroups}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Coverage & RMSE & $|\\text{Bias}|$ \\\\\n\\midrule\nOracle       & 0.944 & 0.113 & 0.090 \\\\\nGlobal       & 0.951 & 0.168 & 0.135 \\\\\nHB EC-HTE    & 0.956 & 0.340 & 0.183 \\\\\nStrat MLE    & 0.953 & 0.638 & 0.219 \\\\\nNaive        & 0.913 & 0.133 & 0.107 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll CM-aware methods achieve nominal coverage at $K{=}8$: HB EC-HTE 95.6\\%, Strat MLE 95.3\\%, Global 95.1\\%.\nHB partial pooling achieves a 47\\% RMSE reduction over stratified MLE (0.340 vs.\\ 0.638), confirming that hierarchical shrinkage provides substantial regularization.\nHowever, HB RMSE (0.340) exceeds global correction (0.168), indicating that ${\\approx}31$ expert labels per subgroup are insufficient for per-subgroup CM estimation to outweigh variance inflation.\n\n\\paragraph{Per-subgroup breakdown.}\nTable~\\ref{tab:k8_per_subgroup} decomposes RMSE by subgroup.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-subgroup RMSE at $K{=}8$. HB improvement over MLE is largest in high-$\\pi$ subgroups but does not close the gap with Global.}\n\\label{tab:k8_per_subgroup}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\nSubgroup & $\\pi_s$ & HB RMSE & MLE RMSE & Global RMSE & HB Cov \\\\\n\\midrule\n$s_0$ & 0.050 & 0.136 & 0.134 & \\textbf{0.181} & 0.950 \\\\\n$s_1$ & 0.093 & 0.133 & 0.132 & \\textbf{0.154} & 0.970 \\\\\n$s_2$ & 0.136 & 0.154 & 0.154 & 0.161 & 0.975 \\\\\n$s_3$ & 0.179 & 0.178 & 0.182 & \\textbf{0.159} & 0.945 \\\\\n$s_4$ & 0.221 & 0.263 & 0.343 & \\textbf{0.163} & 0.940 \\\\\n$s_5$ & 0.264 & 0.421 & 0.711 & \\textbf{0.164} & 0.965 \\\\\n$s_6$ & 0.307 & 0.634 & 1.375 & \\textbf{0.177} & 0.940 \\\\\n$s_7$ & 0.350 & 0.432 & 0.809 & \\textbf{0.183} & 0.960 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRMSE degradation is concentrated in high-$\\pi$ subgroups ($s_4$--$s_7$, $\\pi \\geq 0.22$), where confusion matrix inversion amplifies estimation noise ($r = 0.87$, $p = 0.005$ for correlation between $\\pi_s$ and HB RMSE).\nLow-error subgroups ($s_0$--$s_1$) benefit from stratification, with HB RMSE 14--25\\% below global correction.\nHB partial pooling reduces MLE RMSE by 24--54\\% in the high-$\\pi$ regime ($s_4$--$s_7$), confirming that hierarchical shrinkage provides meaningful regularization even when per-subgroup labels are scarce.\nCoverage remains $\\geq$0.94 across all subgroups for HB EC-HTE, indicating that variance inflation does not compromise inference validity.\nAdaptive shrinkage---increasing the prior strength for high-$\\pi$ subgroups where CM estimation is least reliable---is a natural extension that may close the RMSE gap with global correction at larger $K$.\n\nWe explored adaptive shrinkage ($\\alpha{=}10$ for high-$\\pi$ subgroups vs.\\ default $\\alpha{=}3$), which reduces aggregate RMSE from 0.340 to 0.216 (35\\% improvement) by attenuating estimation noise in high-$\\pi$ subgroups.\nHowever, RMSE remains 30\\% above global correction (0.166), confirming that the bottleneck is per-subgroup sample size (${\\sim}$31 expert labels) rather than the shrinkage method itself.\nThis establishes $K{=}8$ at $n_{\\text{expert}}{=}250$ as a boundary condition: all correction methods provide valid inference (coverage $\\geq$94\\%), but per-subgroup stratification requires proportionally larger expert budgets---approximately $n_{\\text{expert}} \\geq 500$ (${\\approx}60$ labels/subgroup)---to achieve RMSE parity with global correction.\n\n\\section{Asymmetric Misclassification Extension}\n\\label{app:asymmetric}\n\nAssumption~(A2) imposes symmetric misclassification ($\\text{FPR}_s = \\text{FNR}_s = \\pi_s$), which simplifies the bias decomposition but is not necessary for it.\nReal LLM annotators typically exhibit asymmetric confusion patterns; we show here that the product structure generalizes.\n\n\\paragraph{General bias formula.}\nFor asymmetric confusion matrices $C_s = \\bigl(\\begin{smallmatrix} 1{-}\\text{FPR}_s & \\text{FPR}_s \\\\ \\text{FNR}_s & 1{-}\\text{FNR}_s \\end{smallmatrix}\\bigr)$, define the mixing matrix $M_s$ via Bayesian inversion and the residual matrix $B_s = M_{\\text{global}}^{-1} M_s - I$.\nSince both $M_s$ and $M_{\\text{global}}$ are row-stochastic, $B_s \\mathbf{1} = \\mathbf{0}$.\nDecomposing $\\boldsymbol{\\tau} = \\tau(0)\\mathbf{1} + \\Delta\\tau \\, \\mathbf{e}_1$ gives:\n\\begin{equation}\n\\text{bias}(z, s) = \\Delta\\tau \\cdot [B_s]_{z,1},\n\\end{equation}\nwhere $[B_s]_{z,1}$ depends only on $\\{\\text{FPR}_k, \\text{FNR}_k, w_k\\}$, not on $\\Delta\\tau$.\nUnder~(A2), this reduces to $\\delta_s \\Delta\\tau / (1 - 2\\bar{\\pi})$ (Theorem~\\ref{thm:bias_identity}).\n\n\\paragraph{Empirical validation.}\nWe test three asymmetric configurations ($K{=}2$, $n_{\\text{expert}}{=}250$, 100 MC runs each): \\emph{Cross} (FPR/FNR = 0.10/0.20 vs.\\ 0.25/0.10), \\emph{Co-directional} (0.05/0.15 vs.\\ 0.20/0.30), and \\emph{Extreme} (0.03/0.25 vs.\\ 0.30/0.05).\nRegressing analytic predictions on MC bias yields $R^2 = 0.991$ across all configurations, confirming the product structure under asymmetry.\nTable~\\ref{tab:asymmetric} reports correction performance averaged over subgroups, $z$-levels, and $\\Delta\\tau \\in \\{0.1, \\ldots, 0.5\\}$.\nIn these three selected high-disparity configurations, EC-HTE reduces $|\\text{bias}|$ from 0.025 (global) to 0.006, a $4\\times$ improvement, with lower RMSE (0.033 vs.\\ 0.040) and substantially better coverage (0.90 vs.\\ 0.78); however, this advantage does not generalize across all asymmetric settings (see below).\n\n\\begin{table}[t]\n\\centering\n\\caption{Asymmetric misclassification results ($K{=}2$, $n_{\\text{expert}}{=}250$, 100 MC runs). Values averaged over subgroups, $z$-levels, and $\\Delta\\tau$.}\n\\label{tab:asymmetric}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\nMethod & $|\\text{Bias}| \\downarrow$ & RMSE $\\downarrow$ & Coverage $\\uparrow$ \\\\\n\\midrule\nNaive & 0.047 & 0.053 & 0.48 \\\\\nGlobal & 0.025 & 0.040 & 0.78 \\\\\nHB EC-HTE & \\textbf{0.006} & \\textbf{0.033} & \\textbf{0.90} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Comprehensive grid evaluation (48 configurations).}\n\nTo assess robustness beyond the three configurations above, we evaluate the product structure and correction methods across a factorial grid of 6 FPR/FNR ratios $\\times$ 4 $\\Delta\\pi$ levels $\\times$ 2 subgroup counts ($K \\in \\{2, 4\\}$), yielding 48 configurations with 100 MC runs each ($n_{\\text{expert}} = 250$).\n\nTable~\\ref{tab:asym_r2_grid} reports $R^2$ between analytic predictions and MC bias.\nThe product structure holds reliably at $\\Delta\\pi \\geq 0.10$ ($R^2 > 0.73$ across all ratios and $K$ values); at $\\Delta\\pi = 0.05$, $R^2$ degrades for extreme ratios (e.g., $\\leq 0.21$ at 2:1 and 5:1, $K{=}2$) because both predicted and observed biases approach zero, making the regression ill-conditioned rather than indicating structural failure.\n\n\\begin{table}[h]\n\\centering\n\\caption{$R^2$ of bias identity predictions under asymmetric misclassification (100 MC runs per cell). Product structure holds at $\\Delta\\pi \\geq 0.10$; low $R^2$ at $\\Delta\\pi = 0.05$ reflects near-zero bias magnitudes.}\n\\label{tab:asym_r2_grid}\n\\small\n\\begin{tabular}{l cccc}\n\\toprule\n& \\multicolumn{4}{c}{$\\Delta\\pi$} \\\\\n\\cmidrule(lr){2-5}\nFPR:FNR & 0.05 & 0.10 & 0.15 & 0.20 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{$K = 2$}} \\\\\n1:2 & 0.84 & 0.92 & 0.97 & 0.98 \\\\\n1:3 & 0.82 & 0.92 & 0.94 & 0.96 \\\\\n1:5 & 0.73 & 0.90 & 0.95 & 0.96 \\\\\n2:1 & 0.21 & 0.90 & 0.94 & 0.96 \\\\\n3:1 & 0.50 & 0.91 & 0.97 & 0.99 \\\\\n5:1 & 0.05 & 0.83 & 0.97 & 0.98 \\\\\n\\midrule",
      "numLines": 500,
      "startLine": 1,
      "totalLines": 1630
    }
  },
  "sourceToolAssistantUUID": "e2a1fd7e-5865-447f-94a8-67171fb5aed8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-25T16:32:32.059Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011k9gPMRv7kqRTmD8bAQnwq`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
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
  "parentUuid": "5ecd7ede-b4e0-4bc7-95bd-b5ccff490180",
  "isSidechain": false,
  "requestId": "req_011CbPcDKGq8enHTT1RnXJRk",
  "type": "assistant",
  "uuid": "5c19e93f-2a23-4540-b955-fb2f843ea734",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8ceeeDArF1QRByncUCJ6j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 57560,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 57560,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1301,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 57560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 57560
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-25T16:32:32.097Z_

<details><summary>↩ Tool result · `toolu_011k9gPMRv7kqRTmD8bAQnwq`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:214:% [Promoted to main text — Figure~\ref{fig:heatmap}]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c19e93f-2a23-4540-b955-fb2f843ea734",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "f4b67e1f-b117-4182-bcf9-59dc38470684",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:214:% [Promoted to main text — Figure~\\ref{fig:heatmap}]",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "5c19e93f-2a23-4540-b955-fb2f843ea734",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-25T16:32:32.924Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WPStG8Kvx5yj1r1uXSvcku`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
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
  "parentUuid": "f4b67e1f-b117-4182-bcf9-59dc38470684",
  "isSidechain": false,
  "requestId": "req_011CbPcDKGq8enHTT1RnXJRk",
  "type": "assistant",
  "uuid": "dc40d743-6ce2-4519-9be6-091267d5f78d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8ceeeDArF1QRByncUCJ6j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 57560,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 57560,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1301,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 57560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 57560
          },
          "type": "message"
        }
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

_source line 57 · 2026-05-25T16:32:32.943Z_

<details><summary>↩ Tool result · `toolu_01WPStG8Kvx5yj1r1uXSvcku`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc40d743-6ce2-4519-9be6-091267d5f78d",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "397cc40f-1cc4-47f1-867e-ab80227b511a",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "dc40d743-6ce2-4519-9be6-091267d5f78d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-25T16:32:34.329Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SLkH18CWHGyrAX7rp1sNFR`</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
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
  "parentUuid": "397cc40f-1cc4-47f1-867e-ab80227b511a",
  "isSidechain": false,
  "requestId": "req_011CbPcDKGq8enHTT1RnXJRk",
  "type": "assistant",
  "uuid": "78b6f79a-389d-4f47-a4d9-0115d81c7dbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8ceeeDArF1QRByncUCJ6j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 57560,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 57560,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1301,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 57560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 57560
          },
          "type": "message"
        }
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

_source line 59 · 2026-05-25T16:32:34.345Z_

<details><summary>↩ Tool result · `toolu_01SLkH18CWHGyrAX7rp1sNFR`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:12:We test on synthetic ($N{=}5{,}000$, $K \in \{2, 4\}$, controlled $\Delta\tau$ and $\Delta\pi$, 100 Monte Carlo (MC) runs) and semi-synthetic data-generating processes (DGPs) spanning four NLP tasks---sentiment analysis (TweetEval~\cite{barbieri2020tweeteval}, $K{=}4$), hate speech detection (CivilComments, $K{=}4$), stance detection ($K{=}5$; Appendix~\ref{app:stance}), and topic classification (AG News, $K{=}4$; Appendix~\ref{app:agnews})---with full specifications in Appendix~\ref{app:dgp}.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:35:On CivilComments hate speech detection (Appendix~\ref{app:civilcomments}), the bias identity changes the substantive NLP conclusion: global correction suggests demographic-group moderation effects are uniformly small, while EC-HTE reveals a 3.2$\times$ effect-size gap between identity subgroups---consistent with known annotation disparities~\cite{borkan2019nuanced} (Appendix~\ref{app:hatespeech}).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:13:The stance task exposes an operating-conditions limitation: GPT-3.5-Turbo achieves FNR ${>}\,0.50$ on all five targets, violating the classifier quality precondition and producing $\kappa$ values up to 15.0 (Climate Change) vs.\ 4.6 (Hillary Clinton)---a ${\sim}10{\times}$ range within the same LLM.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:15:Mean RMSE: naive${=}0.116$, global${=}0.272$, EC-HTE${=}0.271$; correction reduces sign reversals but does not improve overall RMSE at $K{=}5$, $n{=}300$ per subgroup---consistent with the operating-conditions threshold ($n_{\text{expert}} \geq 250$ for $K{=}2$; Section~\ref{sec:diagnostic}).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:27:GPT-4o & Fem.\ Mov.\ & 1.79 & \checkmark & --- & \checkmark \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:28:GPT-4o & Hillary C.\ & 1.86 & \checkmark & --- & \checkmark \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:30:GPT-3.5-T & Atheism & 7.21 & --- & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:31:GPT-3.5-T & Climate Ch.\ & 15.01 & --- & \checkmark & \checkmark \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:32:GPT-3.5-T & Fem.\ Mov.\ & 3.28 & \checkmark & --- & \checkmark \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:33:GPT-3.5-T & Hillary C.\ & 4.60 & \checkmark & --- & \checkmark \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:34:GPT-3.5-T & Abortion & 14.17 & --- & --- & \checkmark \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex:6:When these conditions are not met, global correction remains appropriate---the diagnostic explicitly guards against inappropriate application.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex:14:Large $\alpha_0$ pulls estimates toward $\hat{C}_{\text{global}}$; small $\alpha_0$ allows subgroup-specific rates to dominate---partial pooling borrows strength while preserving heterogeneity.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex:43:For subgroup $A$: $\delta_A = 0.05 - 0.15 = -0.10$, bias $= -0.10 \times 0.20 / 0.70 = -0.029$---global correction \emph{creates} bias in a subgroup where the naive estimator is nearly unbiased ($\pi_A = 0.05$).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex:51:Unlike Frazis--Loewenstein scalar attenuation~\citep{frazis2003estimating}, which uniformly shrinks estimates toward zero ($K{=}1$: $\delta_s \equiv 0$ recovers $\hat{\beta} = (1-2\pi)\beta$), the product form reveals that correction can \emph{reverse} bias sign across subgroups---a qualitatively new phenomenon from error-rate heterogeneity invisible to any global-scalar analysis (F-L increases $|\text{bias}|$ to $0.122$, $2.1\times$ naive; Table~\ref{tab:main_results}).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex:107:    \item \textit{Low-error} ($\pi_s < \bar{\pi}$): the condition holds whenever $\pi_s < \bar{\pi} / (2(1 - \bar{\pi}))$---easily satisfied: when $\bar{\pi} = 0.15$, any subgroup with $\pi_s < 0.088$ is harmed by global correction.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex:109:The mechanism is over-correction: for subgroups with near-zero misclassification ($\pi_s \approx 0$), the naive estimator is nearly unbiased, yet global inversion calibrated for $\bar{\pi}$ creates substantial bias---debiasing is worse than doing nothing, and can reverse bias sign across subgroups (proof in Appendix~\ref{app:debiasing_hurts}).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex:6:Assumption~(A1)---conditional independence of misclassification and potential outcomes---is not empirically testable; sensitivity analysis shows robustness up to $\gamma_T \leq 0.05$ for treatment-dependent misclassification (coverage $\geq$89.7\%; Appendix~\ref{app:treatment_dep}).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex:7:Ground-truth subgroup CATEs are unavailable in public datasets---classic causal inference benchmarks lack the LLM annotation step that creates the measurement error we address---so all evaluations use synthetic CATE injection on real text features and real LLM annotations (Appendices~\ref{app:dgp},~\ref{app:multilm}).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:24: & Naive & 0.067 & 0.109 & 0.84 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:26: & Strat.\ MLE & 0.034 & 0.181 & 0.89 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:27: & HB EC-HTE & 0.035 & 0.182 & 0.89 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:30: & Naive & 0.067 & 0.109 & 0.84 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:32: & Strat.\ MLE & \textbf{0.022} & 0.147 & 0.92 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:33: & HB EC-HTE & 0.022 & 0.147 & 0.92 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:36: & Naive & 0.067 & 0.109 & 0.84 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:38: & Strat.\ MLE & \textbf{0.015} & 0.126 & 0.95 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:39: & HB EC-HTE & 0.015 & 0.126 & 0.95 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex:3:When this assumption fails---as it routinely does with large language model (LLM) classifiers, whose error rates vary by up to $5\times$ across subgroups---correction can reverse estimated effect signs.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:231:\citet{audinet2025benchmarking} systematically benchmark DSL and PPI methods for LLM-based parameter estimation, finding that debiasing can increase MSE when prediction error is heterogeneous---a population-level analogue of the subgroup-conditional bias amplification we formalize in Theorem~\ref{thm:bias_identity}.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:237:\citet{knox2020administrative} demonstrate how racial misclassification in administrative records biases causal estimates; \citet{blette2024assessing} handle missing (not misclassified) effect modifier data in cluster-RCTs via multiple imputation---a complementary problem to our confusion-matrix correction setting.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:241:\citet{frazis2003estimating} derive exact bias formulas for OLS with a misclassified binary regressor, showing attenuation proportional to the misclassification rate---analogous to our Theorem~\ref{thm:bias_identity} but restricted to average effects without subgroup heterogeneity.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:265:Singularity guard triggers & --- & extreme/$n{=}50$ only \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:431:Adaptive shrinkage---increasing the prior strength for high-$\pi$ subgroups where CM estimation is least reliable---is a natural extension that may close the RMSE gap with global correction at larger $K$.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:435:This establishes $K{=}8$ at $n_{\text{expert}}{=}250$ as a boundary condition: all correction methods provide valid inference (coverage $\geq$94\%), but per-subgroup stratification requires proportionally larger expert budgets---approximately $n_{\text{expert}} \geq 500$ (${\approx}60$ labels/subgroup)---to achieve RMSE parity with global correction.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:608:Since covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:684:Mistral-7B & 0.802 & 0.134 & 0/4 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:693:Global correction achieves comparable or lower RMSE than HB at all budgets under these moderate $\Delta\pi$ values, and the $K{=}4$ RMSE crossover never occurs---confirming the budget guidelines in Appendix~\ref{sec:budget}.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:709:\textit{Average} & --- & \textit{0.714} & \textit{0.939} & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1012:All three models exhibit $\Delta\pi > 0.05$, with overall heterogeneity $\Delta\pi \in [0.113, 0.160]$---comparable to the $\Delta\pi \in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\ref{app:multilm_opensource}).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1069:\multicolumn{2}{l}{All (pooled)} & 0.975 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1109:No combination passes all three conditions; the bottleneck is $\kappa(C_s) \leq 1.25$, which requires $\mathrm{FPR}_s + \mathrm{FNR}_s \lesssim 0.20$ for all subgroups---a threshold no current LLM achieves uniformly.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1118:The diagnostic (Proposition~\ref{prop:debiasing_hurts}) degrades on real LLM confusion matrices (pooled AUC $= 0.63$) because the failure mode is systematic: subgroups where the true CATE heterogeneity $\tau_s \approx 0$ are hurt by global correction (since $\delta_s \neq 0$ still introduces bias), yet these subgroups produce low diagnostic scores---the diagnostic ranks them as safe precisely when they are most vulnerable to overcorrection.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1125:We recommend the following practical protocol: (i) estimate per-subgroup confusion matrices from expert labels; (ii) compute $\max_s \mathrm{score}(s)$; (iii) if $> 1$, the diagnostic reliably identifies which subgroups are harmed by global correction---apply EC-HTE; (iv) if $\leq 1$, the diagnostic is unreliable and practitioners should either default to EC-HTE as a conservative choice or evaluate correction strategies using held-out expert labels.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1154:All 13 real LLM--dataset combinations ($K{=}4$) have $\kappa \in [1.88, 2.99]$---none reaches $\kappa \leq 1.25$, because no current LLM achieves $\mathrm{FPR}_s + \mathrm{FNR}_s < 0.20$ uniformly across subgroups.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1157:At $n_{\text{expert}}{=}500$, EC-HTE also achieves competitive RMSE in the $\kappa \leq 2$ bin (ratio 1.01) and bias win rate of 75\%; at $n_{\text{expert}}{=}250$, the variance cost of per-subgroup estimation dominates, and Global achieves lower RMSE---consistent with the bias-variance tradeoff documented in the main text (Section~\ref{sec:ec_hte_eval}).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1191:Under $K{=}2$ extreme heterogeneity ($\pi{=}[0.05, 0.25]$, $n_{\text{expert}}{=}250$, $n_{\text{estimators}}{=}200$, 20 MC runs), EC-HTE plug-in SE achieves 93.8\% aggregate coverage---close to the 94--96\% oracle coverage (Table~\ref{tab:cf_oracle}).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1196:A \emph{full} bootstrap---resampling all $N$ observations and re-estimating both the confusion matrix and CausalForest per bootstrap replicate ($B{=}100$, $n_{\text{estimators}}{=}200$, 20 MC runs)---confirms that plug-in SE is already near-nominal under standard hyperparameters.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1246:For practical deployment, we recommend $n_{\text{expert}} \geq 50$: bootstrap maintains nominal coverage (98.8\%) with moderate SE inflation (2.9$\times$), and plug-in SE achieves 97.5\%---close to nominal without bootstrap overhead.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1297:Second, EC-HTE with true $C_s$ achieves 91--94\% coverage---a 0--5pp gap from oracle (configuration-dependent), reflecting $M^{-1}$ SE propagation asymmetry across DGPs rather than confusion matrix estimation error.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1349:The predicted aggregate bias is therefore exactly zero, and the observed aggregate bias across 100 MC runs is $< 0.003$ (residual MC noise), confirming that subgroup-level biases---which reach $|\delta_s \cdot \Delta\tau|/(1-2\bar{\pi}) = 0.071$---cancel perfectly in aggregate.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1390:This scenario arises when LLM accuracy varies with treatment status---e.g., treated texts may be systematically harder to classify.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1585:When the true treatment effect is small, global correction can reverse the sign of estimated CATE---concluding a beneficial treatment is harmful---creating a \emph{policy reversal zone}.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1599:0.02 & 21.6 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1602:0.07 & 1.6  & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1603:$\geq$0.10 & 0 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex:5:After standard confusion-matrix correction, the analysis concludes the policy \emph{increases} hate speech among younger users---but the true effect is protective.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex:20:Existing corrections---prediction-powered inference (PPI)~\cite{angelopoulos2023ppi}, design-based supervised learning (DSL)~\cite{egami2023dsl}, prediction-powered conditional inference (PPCI)~\cite{sui2026ppci}, arm-specific PPI~\cite{mozer2026ppi}, ForestIV~\cite{bu2023forestiv}---assume homogeneous prediction error; none addresses effect modifier misclassification (Section~\ref{sec:related}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78b6f79a-389d-4f47-a4d9-0115d81c7dbb",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "b766b554-24d0-47d4-81f8-1179f93b881c",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:12:We test on synthetic ($N{=}5{,}000$, $K \\in \\{2, 4\\}$, controlled $\\Delta\\tau$ and $\\Delta\\pi$, 100 Monte Carlo (MC) runs) and semi-synthetic data-generating processes (DGPs) spanning four NLP tasks---sentiment analysis (TweetEval~\\cite{barbieri2020tweeteval}, $K{=}4$), hate speech detection (CivilComments, $K{=}4$), stance detection ($K{=}5$; Appendix~\\ref{app:stance}), and topic classification (AG News, $K{=}4$; Appendix~\\ref{app:agnews})---with full specifications in Appendix~\\ref{app:dgp}.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:35:On CivilComments hate speech detection (Appendix~\\ref{app:civilcomments}), the bias identity changes the substantive NLP conclusion: global correction suggests demographic-group moderation effects are uniformly small, while EC-HTE reveals a 3.2$\\times$ effect-size gap between identity subgroups---consistent with known annotation disparities~\\cite{borkan2019nuanced} (Appendix~\\ref{app:hatespeech}).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:13:The stance task exposes an operating-conditions limitation: GPT-3.5-Turbo achieves FNR ${>}\\,0.50$ on all five targets, violating the classifier quality precondition and producing $\\kappa$ values up to 15.0 (Climate Change) vs.\\ 4.6 (Hillary Clinton)---a ${\\sim}10{\\times}$ range within the same LLM.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:15:Mean RMSE: naive${=}0.116$, global${=}0.272$, EC-HTE${=}0.271$; correction reduces sign reversals but does not improve overall RMSE at $K{=}5$, $n{=}300$ per subgroup---consistent with the operating-conditions threshold ($n_{\\text{expert}} \\geq 250$ for $K{=}2$; Section~\\ref{sec:diagnostic}).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:27:GPT-4o & Fem.\\ Mov.\\ & 1.79 & \\checkmark & --- & \\checkmark \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:28:GPT-4o & Hillary C.\\ & 1.86 & \\checkmark & --- & \\checkmark \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:30:GPT-3.5-T & Atheism & 7.21 & --- & --- & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:31:GPT-3.5-T & Climate Ch.\\ & 15.01 & --- & \\checkmark & \\checkmark \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:32:GPT-3.5-T & Fem.\\ Mov.\\ & 3.28 & \\checkmark & --- & \\checkmark \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:33:GPT-3.5-T & Hillary C.\\ & 4.60 & \\checkmark & --- & \\checkmark \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex:34:GPT-3.5-T & Abortion & 14.17 & --- & --- & \\checkmark \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex:6:When these conditions are not met, global correction remains appropriate---the diagnostic explicitly guards against inappropriate application.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex:14:Large $\\alpha_0$ pulls estimates toward $\\hat{C}_{\\text{global}}$; small $\\alpha_0$ allows subgroup-specific rates to dominate---partial pooling borrows strength while preserving heterogeneity.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex:43:For subgroup $A$: $\\delta_A = 0.05 - 0.15 = -0.10$, bias $= -0.10 \\times 0.20 / 0.70 = -0.029$---global correction \\emph{creates} bias in a subgroup where the naive estimator is nearly unbiased ($\\pi_A = 0.05$).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex:51:Unlike Frazis--Loewenstein scalar attenuation~\\citep{frazis2003estimating}, which uniformly shrinks estimates toward zero ($K{=}1$: $\\delta_s \\equiv 0$ recovers $\\hat{\\beta} = (1-2\\pi)\\beta$), the product form reveals that correction can \\emph{reverse} bias sign across subgroups---a qualitatively new phenomenon from error-rate heterogeneity invisible to any global-scalar analysis (F-L increases $|\\text{bias}|$ to $0.122$, $2.1\\times$ naive; Table~\\ref{tab:main_results}).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex:107:    \\item \\textit{Low-error} ($\\pi_s < \\bar{\\pi}$): the condition holds whenever $\\pi_s < \\bar{\\pi} / (2(1 - \\bar{\\pi}))$---easily satisfied: when $\\bar{\\pi} = 0.15$, any subgroup with $\\pi_s < 0.088$ is harmed by global correction.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex:109:The mechanism is over-correction: for subgroups with near-zero misclassification ($\\pi_s \\approx 0$), the naive estimator is nearly unbiased, yet global inversion calibrated for $\\bar{\\pi}$ creates substantial bias---debiasing is worse than doing nothing, and can reverse bias sign across subgroups (proof in Appendix~\\ref{app:debiasing_hurts}).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex:6:Assumption~(A1)---conditional independence of misclassification and potential outcomes---is not empirically testable; sensitivity analysis shows robustness up to $\\gamma_T \\leq 0.05$ for treatment-dependent misclassification (coverage $\\geq$89.7\\%; Appendix~\\ref{app:treatment_dep}).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex:7:Ground-truth subgroup CATEs are unavailable in public datasets---classic causal inference benchmarks lack the LLM annotation step that creates the measurement error we address---so all evaluations use synthetic CATE injection on real text features and real LLM annotations (Appendices~\\ref{app:dgp},~\\ref{app:multilm}).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:24: & Naive & 0.067 & 0.109 & 0.84 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:26: & Strat.\\ MLE & 0.034 & 0.181 & 0.89 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:27: & HB EC-HTE & 0.035 & 0.182 & 0.89 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:30: & Naive & 0.067 & 0.109 & 0.84 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:32: & Strat.\\ MLE & \\textbf{0.022} & 0.147 & 0.92 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:33: & HB EC-HTE & 0.022 & 0.147 & 0.92 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:36: & Naive & 0.067 & 0.109 & 0.84 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:38: & Strat.\\ MLE & \\textbf{0.015} & 0.126 & 0.95 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex:39: & HB EC-HTE & 0.015 & 0.126 & 0.95 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex:3:When this assumption fails---as it routinely does with large language model (LLM) classifiers, whose error rates vary by up to $5\\times$ across subgroups---correction can reverse estimated effect signs.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:231:\\citet{audinet2025benchmarking} systematically benchmark DSL and PPI methods for LLM-based parameter estimation, finding that debiasing can increase MSE when prediction error is heterogeneous---a population-level analogue of the subgroup-conditional bias amplification we formalize in Theorem~\\ref{thm:bias_identity}.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:237:\\citet{knox2020administrative} demonstrate how racial misclassification in administrative records biases causal estimates; \\citet{blette2024assessing} handle missing (not misclassified) effect modifier data in cluster-RCTs via multiple imputation---a complementary problem to our confusion-matrix correction setting.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:241:\\citet{frazis2003estimating} derive exact bias formulas for OLS with a misclassified binary regressor, showing attenuation proportional to the misclassification rate---analogous to our Theorem~\\ref{thm:bias_identity} but restricted to average effects without subgroup heterogeneity.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:265:Singularity guard triggers & --- & extreme/$n{=}50$ only \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:431:Adaptive shrinkage---increasing the prior strength for high-$\\pi$ subgroups where CM estimation is least reliable---is a natural extension that may close the RMSE gap with global correction at larger $K$.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:435:This establishes $K{=}8$ at $n_{\\text{expert}}{=}250$ as a boundary condition: all correction methods provide valid inference (coverage $\\geq$94\\%), but per-subgroup stratification requires proportionally larger expert budgets---approximately $n_{\\text{expert}} \\geq 500$ (${\\approx}60$ labels/subgroup)---to achieve RMSE parity with global correction.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:608:Since covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:684:Mistral-7B & 0.802 & 0.134 & 0/4 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:693:Global correction achieves comparable or lower RMSE than HB at all budgets under these moderate $\\Delta\\pi$ values, and the $K{=}4$ RMSE crossover never occurs---confirming the budget guidelines in Appendix~\\ref{sec:budget}.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:709:\\textit{Average} & --- & \\textit{0.714} & \\textit{0.939} & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1012:All three models exhibit $\\Delta\\pi > 0.05$, with overall heterogeneity $\\Delta\\pi \\in [0.113, 0.160]$---comparable to the $\\Delta\\pi \\in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\\ref{app:multilm_opensource}).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1069:\\multicolumn{2}{l}{All (pooled)} & 0.975 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1109:No combination passes all three conditions; the bottleneck is $\\kappa(C_s) \\leq 1.25$, which requires $\\mathrm{FPR}_s + \\mathrm{FNR}_s \\lesssim 0.20$ for all subgroups---a threshold no current LLM achieves uniformly.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1118:The diagnostic (Proposition~\\ref{prop:debiasing_hurts}) degrades on real LLM confusion matrices (pooled AUC $= 0.63$) because the failure mode is systematic: subgroups where the true CATE heterogeneity $\\tau_s \\approx 0$ are hurt by global correction (since $\\delta_s \\neq 0$ still introduces bias), yet these subgroups produce low diagnostic scores---the diagnostic ranks them as safe precisely when they are most vulnerable to overcorrection.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1125:We recommend the following practical protocol: (i) estimate per-subgroup confusion matrices from expert labels; (ii) compute $\\max_s \\mathrm{score}(s)$; (iii) if $> 1$, the diagnostic reliably identifies which subgroups are harmed by global correction---apply EC-HTE; (iv) if $\\leq 1$, the diagnostic is unreliable and practitioners should either default to EC-HTE as a conservative choice or evaluate correction strategies using held-out expert labels.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1154:All 13 real LLM--dataset combinations ($K{=}4$) have $\\kappa \\in [1.88, 2.99]$---none reaches $\\kappa \\leq 1.25$, because no current LLM achieves $\\mathrm{FPR}_s + \\mathrm{FNR}_s < 0.20$ uniformly across subgroups.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1157:At $n_{\\text{expert}}{=}500$, EC-HTE also achieves competitive RMSE in the $\\kappa \\leq 2$ bin (ratio 1.01) and bias win rate of 75\\%; at $n_{\\text{expert}}{=}250$, the variance cost of per-subgroup estimation dominates, and Global achieves lower RMSE---consistent with the bias-variance tradeoff documented in the main text (Section~\\ref{sec:ec_hte_eval}).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1191:Under $K{=}2$ extreme heterogeneity ($\\pi{=}[0.05, 0.25]$, $n_{\\text{expert}}{=}250$, $n_{\\text{estimators}}{=}200$, 20 MC runs), EC-HTE plug-in SE achieves 93.8\\% aggregate coverage---close to the 94--96\\% oracle coverage (Table~\\ref{tab:cf_oracle}).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1196:A \\emph{full} bootstrap---resampling all $N$ observations and re-estimating both the confusion matrix and CausalForest per bootstrap replicate ($B{=}100$, $n_{\\text{estimators}}{=}200$, 20 MC runs)---confirms that plug-in SE is already near-nominal under standard hyperparameters.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1246:For practical deployment, we recommend $n_{\\text{expert}} \\geq 50$: bootstrap maintains nominal coverage (98.8\\%) with moderate SE inflation (2.9$\\times$), and plug-in SE achieves 97.5\\%---close to nominal without bootstrap overhead.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1297:Second, EC-HTE with true $C_s$ achieves 91--94\\% coverage---a 0--5pp gap from oracle (configuration-dependent), reflecting $M^{-1}$ SE propagation asymmetry across DGPs rather than confusion matrix estimation error.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1349:The predicted aggregate bias is therefore exactly zero, and the observed aggregate bias across 100 MC runs is $< 0.003$ (residual MC noise), confirming that subgroup-level biases---which reach $|\\delta_s \\cdot \\Delta\\tau|/(1-2\\bar{\\pi}) = 0.071$---cancel perfectly in aggregate.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1390:This scenario arises when LLM accuracy varies with treatment status---e.g., treated texts may be systematically harder to classify.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1585:When the true treatment effect is small, global correction can reverse the sign of estimated CATE---concluding a beneficial treatment is harmful---creating a \\emph{policy reversal zone}.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1599:0.02 & 21.6 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1602:0.07 & 1.6  & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1603:$\\geq$0.10 & 0 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex:5:After standard confusion-matrix correction, the analysis concludes the policy \\emph{increases} hate speech among younger users---but the true effect is protective.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex:13:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex:20:Existing corrections---prediction-powered inference (PPI)~\\cite{angelopoulos2023ppi}, design-based supervised learning (DSL)~\\cite{egami2023dsl}, prediction-powered conditional inference (PPCI)~\\cite{sui2026ppci}, arm-specific PPI~\\cite{mozer2026ppi}, ForestIV~\\cite{bu2023forestiv}---assume homogeneous prediction error; none addresses effect modifier misclassification (Section~\\ref{sec:related}).",
    "numLines": 59
  },
  "sourceToolAssistantUUID": "78b6f79a-389d-4f47-a4d9-0115d81c7dbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-25T16:32:36.753Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SgiwA65cC9uz2QJsgMHNQQ`</summary>

```json
{
  "pattern": "(it is worth noting|notably|importantly|furthermore|moreover|additionally|delve|leverage|utilize|a myriad|a plethora|in the realm of)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b766b554-24d0-47d4-81f8-1179f93b881c",
  "isSidechain": false,
  "requestId": "req_011CbPcDKGq8enHTT1RnXJRk",
  "type": "assistant",
  "uuid": "cf67edf3-6eba-4298-8ff7-b2f3504ebc56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8ceeeDArF1QRByncUCJ6j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 57560,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 57560,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1301,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 57560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 57560
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-25T16:32:36.781Z_

<details><summary>↩ Tool result · `toolu_01SgiwA65cC9uz2QJsgMHNQQ`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf67edf3-6eba-4298-8ff7-b2f3504ebc56",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "74358ef7-2b50-46c3-ad1b-56f25fa558bc",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "cf67edf3-6eba-4298-8ff7-b2f3504ebc56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-25T16:32:38.745Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015f7ntzptB8dad85C9TJ95p`</summary>

```json
{
  "pattern": "ing,|ing\\.|, (demonstrating|highlighting|showcasing|enabling|allowing|suggesting|indicating|providing|offering|representing)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
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
  "parentUuid": "74358ef7-2b50-46c3-ad1b-56f25fa558bc",
  "isSidechain": false,
  "requestId": "req_011CbPcDKGq8enHTT1RnXJRk",
  "type": "assistant",
  "uuid": "bc19609d-80b2-4189-9104-d1dc9e240068",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8ceeeDArF1QRByncUCJ6j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 57560,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 57560,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1301,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 57560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 57560
          },
          "type": "message"
        }
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

_source line 63 · 2026-05-25T16:32:38.763Z_

<details><summary>↩ Tool result · `toolu_015f7ntzptB8dad85C9TJ95p`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:43:HB EC-HTE reduces $|\text{bias}|$ from 0.059 to 0.008 (7.4$\times$); relative to stratified MLE (0.012), the advantage is 1.5$\times$ with lower RMSE from partial pooling. At $K{=}4$, bias reduces from 0.056 to 0.012 (4.7$\times$), maintaining near-nominal coverage (0.94--0.96).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:93:Under relaxed screening, 79\% of real LLM--dataset pairs show RMSE improvement with coverage $\geq$93\% (Appendix~\ref{app:screening}).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/checklist.tex:16:Yes. All results are averaged over 100 Monte Carlo runs. We report 95\% CI coverage as a primary metric. RMSE captures both bias and variance. We do not use the term ``significant'' without formal testing.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex:89:At $\gamma_T = 0.10$, coverage degrades to 75\% (Appendix~\ref{app:treatment_dep}); sensitivity analysis for outcome-dependent misclassification appears in Appendix~\ref{app:a1_sensitivity}. Sensitivity frameworks~\cite{lash2009applying,dorn2022sharp,cinelli2020making} can bound this.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex:109:The mechanism is over-correction: for subgroups with near-zero misclassification ($\pi_s \approx 0$), the naive estimator is nearly unbiased, yet global inversion calibrated for $\bar{\pi}$ creates substantial bias---debiasing is worse than doing nothing, and can reverse bias sign across subgroups (proof in Appendix~\ref{app:debiasing_hurts}).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:39:Across all configurations, the maximum observed condition number is $\kappa_{\max} = 1.89$ (mean 1.45, p99 1.89), providing a $53{\times}$ safety margin below the $\kappa{=}100$ threshold.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:211:All CausalForest experiments use \texttt{econml.dml.CausalForestDML} with honest splitting, $n_{\text{estimators}} = 48$, $\texttt{min\_samples\_leaf} = 20$, \texttt{model\_y} = \texttt{LassoCV}(cv=3), and \texttt{model\_t} = \texttt{LogisticRegressionCV}.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:237:\citet{knox2020administrative} demonstrate how racial misclassification in administrative records biases causal estimates; \citet{blette2024assessing} handle missing (not misclassified) effect modifier data in cluster-RCTs via multiple imputation---a complementary problem to our confusion-matrix correction setting.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:244:Our setting differs in three respects: (i) the mismeasured variable is an effect modifier indexing the CATE function, not a standard regressor; (ii) misclassification rates vary across subgroups, creating the $\delta_s \times \Delta\tau$ product amplification absent from homogeneous-error analyses; and (iii) expert labels provide a direct calibration sample, enabling confusion matrix estimation without instruments.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:401:However, HB RMSE (0.340) exceeds global correction (0.168), indicating that ${\approx}31$ expert labels per subgroup are insufficient for per-subgroup CM estimation to outweigh variance inflation.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:430:Coverage remains $\geq$0.94 across all subgroups for HB EC-HTE, indicating that variance inflation does not compromise inference validity.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:618:Per-subgroup misclassification rates range from 0.266 to 0.383, confirming heterogeneity ($\Delta\pi = 0.117$) in a real annotation setting.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:619:At the error-type level, FPR ranges from 8.5\% to 21.3\% across text-feature subgroups, demonstrating that subgroup-varying misclassification is not an artifact of synthetic design but arises naturally in real NLP annotation tasks.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:637:Spearman rank correlations of per-subgroup error rates across all six subgroups range from $\rho = 0.82$ to $1.00$, indicating that the subgroup error structure is consistent across architectures.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:864:For a $2 \times 2$ symmetric confusion matrix, $\kappa = 1/|1-2\pi|$; $\kappa > 100$ corresponds to $\pi \in (0.495, 0.505)$, so the guard triggers only when the classifier performs within $0.5\%$ of random guessing.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:990:Applied to our setting, PPI treats the LLM-annotated effect modifier as the ML prediction and the expert labels as the gold standard.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1013:GPT-4o-mini and GPT-3.5-turbo show pronounced FPR/FNR asymmetry (e.g., GPT-4o-mini FPR $\in [0.42, 0.61]$ vs.\ FNR $\in [0.05, 0.16]$), indicating systematic over-prediction of toxicity; their FPR approaches 0.5, placing them in the ill-conditioned regime where confusion matrix inversion amplifies noise (consistent with the classifier quality threshold discussed in the Limitations section).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1122:When $\max_s \mathrm{score}(s) \leq 1$, global correction may or may not hurt depending on unobservable $\Delta\tau$; the diagnostic achieves AUC only 0.0--0.67 across the remaining 7 combinations (4 of 7 have AUC $< 0.5$, indicating anti-prediction).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1383:All correction methods (Global, Stratified MLE, HB) maintain $\geq$90\% coverage, indicating that moderate (A1) violations do not catastrophically degrade confusion-matrix-based correction.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1457:Global coverage (93.0\%) falls below the correction methods (95.0\%), consistent with the cost of ignoring subgroup-level error heterogeneity even in the confounded setting.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1516:Both F-L variants produce \emph{higher} bias and RMSE than the naive estimator (F-L per-subgroup $|\text{bias}|{=}0.112$ vs.\ naive $0.062$), demonstrating that scalar attenuation cannot substitute for confusion matrix inversion under subgroup-heterogeneous misclassification.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1579:Calibrated + EC-HTE achieves the highest coverage (96.5\%), demonstrating that calibration and EC-HTE address complementary error sources: calibration reduces per-subgroup $\pi_s$ while EC-HTE corrects the residual $\delta_s$-driven bias from heterogeneity that persists post-calibration.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1629:The authors used AI-based writing assistants, including Claude, for limited support during manuscript preparation, including grammar polishing, wording suggestions, LaTeX editing, and code/debugging assistance. The tools were not used to generate the core research ideas, experimental design, methodological decisions, data analysis, or scientific conclusions. All AI-assisted text, code suggestions, and references were manually reviewed and edited by the authors.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex:9:When these labels serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, the standard correction protocol\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.} is straightforward: validate a sample against expert annotations, estimate a confusion matrix, and apply its inverse uniformly to correct conditional average treatment effect (CATE) estimates.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex:13:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc19609d-80b2-4189-9104-d1dc9e240068",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "0d6e0073-c82e-4e9f-a680-0db1c40238f4",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:43:HB EC-HTE reduces $|\\text{bias}|$ from 0.059 to 0.008 (7.4$\\times$); relative to stratified MLE (0.012), the advantage is 1.5$\\times$ with lower RMSE from partial pooling. At $K{=}4$, bias reduces from 0.056 to 0.012 (4.7$\\times$), maintaining near-nominal coverage (0.94--0.96).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:93:Under relaxed screening, 79\\% of real LLM--dataset pairs show RMSE improvement with coverage $\\geq$93\\% (Appendix~\\ref{app:screening}).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/checklist.tex:16:Yes. All results are averaged over 100 Monte Carlo runs. We report 95\\% CI coverage as a primary metric. RMSE captures both bias and variance. We do not use the term ``significant'' without formal testing.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex:89:At $\\gamma_T = 0.10$, coverage degrades to 75\\% (Appendix~\\ref{app:treatment_dep}); sensitivity analysis for outcome-dependent misclassification appears in Appendix~\\ref{app:a1_sensitivity}. Sensitivity frameworks~\\cite{lash2009applying,dorn2022sharp,cinelli2020making} can bound this.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex:109:The mechanism is over-correction: for subgroups with near-zero misclassification ($\\pi_s \\approx 0$), the naive estimator is nearly unbiased, yet global inversion calibrated for $\\bar{\\pi}$ creates substantial bias---debiasing is worse than doing nothing, and can reverse bias sign across subgroups (proof in Appendix~\\ref{app:debiasing_hurts}).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:39:Across all configurations, the maximum observed condition number is $\\kappa_{\\max} = 1.89$ (mean 1.45, p99 1.89), providing a $53{\\times}$ safety margin below the $\\kappa{=}100$ threshold.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:211:All CausalForest experiments use \\texttt{econml.dml.CausalForestDML} with honest splitting, $n_{\\text{estimators}} = 48$, $\\texttt{min\\_samples\\_leaf} = 20$, \\texttt{model\\_y} = \\texttt{LassoCV}(cv=3), and \\texttt{model\\_t} = \\texttt{LogisticRegressionCV}.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:237:\\citet{knox2020administrative} demonstrate how racial misclassification in administrative records biases causal estimates; \\citet{blette2024assessing} handle missing (not misclassified) effect modifier data in cluster-RCTs via multiple imputation---a complementary problem to our confusion-matrix correction setting.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:244:Our setting differs in three respects: (i) the mismeasured variable is an effect modifier indexing the CATE function, not a standard regressor; (ii) misclassification rates vary across subgroups, creating the $\\delta_s \\times \\Delta\\tau$ product amplification absent from homogeneous-error analyses; and (iii) expert labels provide a direct calibration sample, enabling confusion matrix estimation without instruments.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:401:However, HB RMSE (0.340) exceeds global correction (0.168), indicating that ${\\approx}31$ expert labels per subgroup are insufficient for per-subgroup CM estimation to outweigh variance inflation.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:430:Coverage remains $\\geq$0.94 across all subgroups for HB EC-HTE, indicating that variance inflation does not compromise inference validity.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:618:Per-subgroup misclassification rates range from 0.266 to 0.383, confirming heterogeneity ($\\Delta\\pi = 0.117$) in a real annotation setting.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:619:At the error-type level, FPR ranges from 8.5\\% to 21.3\\% across text-feature subgroups, demonstrating that subgroup-varying misclassification is not an artifact of synthetic design but arises naturally in real NLP annotation tasks.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:637:Spearman rank correlations of per-subgroup error rates across all six subgroups range from $\\rho = 0.82$ to $1.00$, indicating that the subgroup error structure is consistent across architectures.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:864:For a $2 \\times 2$ symmetric confusion matrix, $\\kappa = 1/|1-2\\pi|$; $\\kappa > 100$ corresponds to $\\pi \\in (0.495, 0.505)$, so the guard triggers only when the classifier performs within $0.5\\%$ of random guessing.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:990:Applied to our setting, PPI treats the LLM-annotated effect modifier as the ML prediction and the expert labels as the gold standard.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1013:GPT-4o-mini and GPT-3.5-turbo show pronounced FPR/FNR asymmetry (e.g., GPT-4o-mini FPR $\\in [0.42, 0.61]$ vs.\\ FNR $\\in [0.05, 0.16]$), indicating systematic over-prediction of toxicity; their FPR approaches 0.5, placing them in the ill-conditioned regime where confusion matrix inversion amplifies noise (consistent with the classifier quality threshold discussed in the Limitations section).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1122:When $\\max_s \\mathrm{score}(s) \\leq 1$, global correction may or may not hurt depending on unobservable $\\Delta\\tau$; the diagnostic achieves AUC only 0.0--0.67 across the remaining 7 combinations (4 of 7 have AUC $< 0.5$, indicating anti-prediction).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1383:All correction methods (Global, Stratified MLE, HB) maintain $\\geq$90\\% coverage, indicating that moderate (A1) violations do not catastrophically degrade confusion-matrix-based correction.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1457:Global coverage (93.0\\%) falls below the correction methods (95.0\\%), consistent with the cost of ignoring subgroup-level error heterogeneity even in the confounded setting.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1516:Both F-L variants produce \\emph{higher} bias and RMSE than the naive estimator (F-L per-subgroup $|\\text{bias}|{=}0.112$ vs.\\ naive $0.062$), demonstrating that scalar attenuation cannot substitute for confusion matrix inversion under subgroup-heterogeneous misclassification.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1579:Calibrated + EC-HTE achieves the highest coverage (96.5\\%), demonstrating that calibration and EC-HTE address complementary error sources: calibration reduces per-subgroup $\\pi_s$ while EC-HTE corrects the residual $\\delta_s$-driven bias from heterogeneity that persists post-calibration.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1629:The authors used AI-based writing assistants, including Claude, for limited support during manuscript preparation, including grammar polishing, wording suggestions, LaTeX editing, and code/debugging assistance. The tools were not used to generate the core research ideas, experimental design, methodological decisions, data analysis, or scientific conclusions. All AI-assisted text, code suggestions, and references were manually reviewed and edited by the authors.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex:9:When these labels serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, the standard correction protocol\\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.} is straightforward: validate a sample against expert annotations, estimate a confusion matrix, and apply its inverse uniformly to correct conditional average treatment effect (CATE) estimates.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex:13:[Omitted long matching line]",
    "numLines": 25
  },
  "sourceToolAssistantUUID": "bc19609d-80b2-4189-9104-d1dc9e240068",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-25T16:32:42.510Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01FVisYnH9xv41ii75d1boka`</summary>

```json
{
  "pattern": "significantly",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d6e0073-c82e-4e9f-a680-0db1c40238f4",
  "isSidechain": false,
  "requestId": "req_011CbPcDKGq8enHTT1RnXJRk",
  "type": "assistant",
  "uuid": "b703210d-b6d0-4b74-b7b7-51e2c88c0327",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8ceeeDArF1QRByncUCJ6j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 57560,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 57560,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1301,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 57560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 57560
          },
          "type": "message"
        }
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

_source line 65 · 2026-05-25T16:32:42.524Z_

<details><summary>↩ Tool result · `toolu_01FVisYnH9xv41ii75d1boka`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:802:In the semi-synthetic TweetEval experiment, HB EC-HTE does not significantly improve over global ($p = 0.395$), consistent with moderate $\Delta\pi$ and unbalanced subgroup sizes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b703210d-b6d0-4b74-b7b7-51e2c88c0327",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "12601544-cf32-40b5-acf8-48664be4569c",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:802:In the semi-synthetic TweetEval experiment, HB EC-HTE does not significantly improve over global ($p = 0.395$), consistent with moderate $\\Delta\\pi$ and unbalanced subgroup sizes.",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "b703210d-b6d0-4b74-b7b7-51e2c88c0327",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-25T16:32:42.798Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01VRy6wKcBVfV2q2bWYZ3i1U`</summary>

```json
{
  "pattern": "state.of.the.art|SOTA|groundbreaking|revolutionary|novel",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12601544-cf32-40b5-acf8-48664be4569c",
  "isSidechain": false,
  "requestId": "req_011CbPcDKGq8enHTT1RnXJRk",
  "type": "assistant",
  "uuid": "3d5d342b-3d89-4bf8-889d-96b5fd766178",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8ceeeDArF1QRByncUCJ6j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 57560,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 57560,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1301,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 57560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 57560
          },
          "type": "message"
        }
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

_source line 67_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：ec_hte_llm_annotation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 30 warning 一致性检查…",
  "leafUuid": "03e86a88-1934-4815-b310-f3f2b60dedac",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

### Runtime record

_source line 68_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP 2026 paper compliance and structure",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

### Assistant

_source line 69 · 2026-05-25T16:32:46.645Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now read the remaining parts of the appendix.tex that I haven't seen yet (offset 500 onwards) to catch any remaining issues. And let me count words in the abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03e86a88-1934-4815-b310-f3f2b60dedac",
  "isSidechain": false,
  "requestId": "req_011CbPcEeTmU7i2gGd5UFjUb",
  "type": "assistant",
  "uuid": "ac8381d6-79d5-482e-a1b1-032edecdd6a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMYjfbJ1D1kP7Wyuksir86",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25426,
      "cache_read_input_tokens": 69406,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 69406,
          "cache_creation_input_tokens": 25426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25426
          },
          "type": "message"
        }
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

_source line 70 · 2026-05-25T16:32:47.213Z_

Let me count the abstract words and read more of the appendix for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac8381d6-79d5-482e-a1b1-032edecdd6a8",
  "isSidechain": false,
  "requestId": "req_011CbPcEeTmU7i2gGd5UFjUb",
  "type": "assistant",
  "uuid": "137d3f8a-7f9a-4a12-bb53-bca4f9553ff9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMYjfbJ1D1kP7Wyuksir86",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25426,
      "cache_read_input_tokens": 69406,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 69406,
          "cache_creation_input_tokens": 25426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25426
          },
          "type": "message"
        }
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

_source line 71 · 2026-05-25T16:32:49.109Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UcK48524YnB9VWiwGZSqdC`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper && cat abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/\\\\//g' | wc -w",
  "description": "Count abstract word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "137d3f8a-7f9a-4a12-bb53-bca4f9553ff9",
  "isSidechain": false,
  "requestId": "req_011CbPcEeTmU7i2gGd5UFjUb",
  "type": "assistant",
  "uuid": "da30ccf5-95fc-40af-be30-b5ecc7d13061",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMYjfbJ1D1kP7Wyuksir86",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25426,
      "cache_read_input_tokens": 69406,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 69406,
          "cache_creation_input_tokens": 25426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25426
          },
          "type": "message"
        }
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

_source line 72 · 2026-05-25T16:32:50.981Z_

<details><summary>↩ Tool result · `toolu_01QDqCptW8H6CghKoTueDaBy`</summary>

```text
1:\section{EC-HTE Procedure}
34:\subsection{Condition Number Guard Ablation}
44:\section{Full Proof of Theorem~\ref{thm:bias_identity}}
107:\section{Multi-class Extension and Proof}
146:\section{Proof of Proposition~\ref{prop:debiasing_hurts}}
178:\section{Semi-Synthetic Data Generating Process}
216:\section{Extended Related Work}
246:\section{MCMC Convergence Diagnostics}
272:\subsection{Hyperprior Sensitivity}
300:\section{Diagnostic ROC Curves}
314:\section{Expert Budget Crossover Curves}
329:\subsection{Budget Sensitivity: HB vs.\ Stratified MLE}
371:\subsection{Scalability to $K{=}8$ Subgroups}
437:\section{Asymmetric Misclassification Extension}
534:\section{Supplementary Main Results}
561:\section{PPCI Complementarity Results}
611:\section{Real-Data Case Study: Hate Speech Detection}
632:\section{Cross-Model Consistency}
664:\section{Open-Source Multi-LLM Validation}
725:\section{Robustness to Subgroup Misspecification}
759:\section{Monte Carlo Standard Errors}
805:\section{Semi-Real Confusion Matrix Validation}
884:\section{Robustness: Estimator Choice and Treatment Effect Specification}
938:\section{Robustness to Class Imbalance}
986:\section{Comparison with PPI Correction}
1002:\section{Civil Comments Validation}
1037:\section{Bias Identity Validation with Real Confusion Matrices}
1074:\section{Applicability Screening with Real LLM Confusion Matrices}
1127:\subsection{$\kappa$ Stratification Analysis}
1181:\section{Plug-in Standard Error Validation}
1253:\subsection{CausalForest Oracle Coverage Decomposition}
1300:\section{Robustness to Assumption Violations}
1303:\subsection{Assumption (A5): Subgroup-Specific Treatment Effects}
1354:\subsection{Assumption (A1): Sensitivity to Outcome-Dependent Misclassification}
1386:\subsection{Assumption (A1): Treatment-Dependent Misclassification}
1423:\subsection{Extension to Confounded Treatment Assignment}
1488:\subsection{Empirical Comparison with Frazis--Loewenstein Correction}
1521:\subsection{End-to-End Validation with Asymmetric Confusion Matrices}
1551:\subsection{Complementarity with LLM Calibration}
1582:\subsection{Policy Reversal Zone Analysis}
1626:\section*{Use of AI Assistants}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d81ce67c-e08e-4c51-a6c4-a429feab51e4",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "12c19716-d2d0-44e1-b33b-fe7efbb1f5d6",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1:\\section{EC-HTE Procedure}\n34:\\subsection{Condition Number Guard Ablation}\n44:\\section{Full Proof of Theorem~\\ref{thm:bias_identity}}\n107:\\section{Multi-class Extension and Proof}\n146:\\section{Proof of Proposition~\\ref{prop:debiasing_hurts}}\n178:\\section{Semi-Synthetic Data Generating Process}\n216:\\section{Extended Related Work}\n246:\\section{MCMC Convergence Diagnostics}\n272:\\subsection{Hyperprior Sensitivity}\n300:\\section{Diagnostic ROC Curves}\n314:\\section{Expert Budget Crossover Curves}\n329:\\subsection{Budget Sensitivity: HB vs.\\ Stratified MLE}\n371:\\subsection{Scalability to $K{=}8$ Subgroups}\n437:\\section{Asymmetric Misclassification Extension}\n534:\\section{Supplementary Main Results}\n561:\\section{PPCI Complementarity Results}\n611:\\section{Real-Data Case Study: Hate Speech Detection}\n632:\\section{Cross-Model Consistency}\n664:\\section{Open-Source Multi-LLM Validation}\n725:\\section{Robustness to Subgroup Misspecification}\n759:\\section{Monte Carlo Standard Errors}\n805:\\section{Semi-Real Confusion Matrix Validation}\n884:\\section{Robustness: Estimator Choice and Treatment Effect Specification}\n938:\\section{Robustness to Class Imbalance}\n986:\\section{Comparison with PPI Correction}\n1002:\\section{Civil Comments Validation}\n1037:\\section{Bias Identity Validation with Real Confusion Matrices}\n1074:\\section{Applicability Screening with Real LLM Confusion Matrices}\n1127:\\subsection{$\\kappa$ Stratification Analysis}\n1181:\\section{Plug-in Standard Error Validation}\n1253:\\subsection{CausalForest Oracle Coverage Decomposition}\n1300:\\section{Robustness to Assumption Violations}\n1303:\\subsection{Assumption (A5): Subgroup-Specific Treatment Effects}\n1354:\\subsection{Assumption (A1): Sensitivity to Outcome-Dependent Misclassification}\n1386:\\subsection{Assumption (A1): Treatment-Dependent Misclassification}\n1423:\\subsection{Extension to Confounded Treatment Assignment}\n1488:\\subsection{Empirical Comparison with Frazis--Loewenstein Correction}\n1521:\\subsection{End-to-End Validation with Asymmetric Confusion Matrices}\n1551:\\subsection{Complementarity with LLM Calibration}\n1582:\\subsection{Policy Reversal Zone Analysis}\n1626:\\section*{Use of AI Assistants}",
    "numLines": 41
  },
  "sourceToolAssistantUUID": "d81ce67c-e08e-4c51-a6c4-a429feab51e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-25T16:32:49.290Z_

<details><summary>↩ Tool result · `toolu_01UcK48524YnB9VWiwGZSqdC`</summary>

```text
176
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da30ccf5-95fc-40af-be30-b5ecc7d13061",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "495cdf57-65e6-4d69-bf97-779f867bbe4b",
  "toolUseResult": {
    "stdout": "176",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "da30ccf5-95fc-40af-be30-b5ecc7d13061",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-25T16:32:50.066Z_

<details open><summary>🔧 Tool call — Read · `toolu_018UeP5M7qmvqVotptrD7ncw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "495cdf57-65e6-4d69-bf97-779f867bbe4b",
  "isSidechain": false,
  "requestId": "req_011CbPcEeTmU7i2gGd5UFjUb",
  "type": "assistant",
  "uuid": "aa58e9a6-7301-48dc-a0eb-71cbb0a82009",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMYjfbJ1D1kP7Wyuksir86",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25426,
      "cache_read_input_tokens": 69406,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 69406,
          "cache_creation_input_tokens": 25426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25426
          },
          "type": "message"
        }
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

_source line 75 · 2026-05-25T16:32:50.334Z_

<details><summary>↩ Tool result · `toolu_018UeP5M7qmvqVotptrD7ncw`</summary>

```text
500	\midrule
501	\multicolumn{5}{l}{\emph{$K = 4$}} \\
502	1:2 & 0.68 & 0.86 & 0.91 & 0.96 \\
503	1:3 & 0.70 & 0.85 & 0.94 & 0.95 \\
504	1:5 & 0.69 & 0.84 & 0.90 & 0.93 \\
505	2:1 & 0.63 & 0.79 & 0.86 & 0.93 \\
506	3:1 & 0.50 & 0.78 & 0.88 & 0.92 \\
507	5:1 & 0.50 & 0.73 & 0.84 & 0.89 \\
508	\bottomrule
509	\end{tabular}
510	\end{table}
511	
512	Table~\ref{tab:asym_method_grid} compares correction methods averaged over all 48 configurations.
513	EC-HTE does not outperform global correction: its RMSE exceeds Global in every configuration (0.125 vs.\ 0.109 overall).
514	Estimating the full asymmetric $J{\times}J$ confusion matrix requires twice the parameters (FPR and FNR separately per subgroup), shifting the bias-variance tradeoff toward higher variance at $n_{\text{expert}} = 250$.
515	We recommend $n_{\text{expert}} \geq 500$ for asymmetric settings to provide sufficient per-subgroup samples for stable CM estimation.
516	
517	\begin{table}[h]
518	\centering
519	\caption{Method comparison under asymmetric misclassification (48 configurations, 100 MC runs). EC-HTE does not outperform global correction at $n_{\text{expert}}{=}250$ due to increased parameter estimation variance.}
520	\label{tab:asym_method_grid}
521	\small
522	\begin{tabular}{l ccc}
523	\toprule
524	Method & $|\text{Bias}| \downarrow$ & RMSE $\downarrow$ & Coverage $\uparrow$ \\
525	\midrule
526	Oracle & 0.058 & 0.072 & 0.946 \\
527	Naive & 0.080 & 0.096 & 0.830 \\
528	Global & 0.088 & 0.109 & 0.931 \\
529	EC-HTE (HB) & 0.098 & 0.125 & 0.920 \\
530	\bottomrule
531	\end{tabular}
532	\end{table}
533	
534	\section{Supplementary Main Results}
535	\label{app:main_supp}
536	
537	\begin{table}[t]
538	\centering
539	\caption{Additional configurations from the main experiment. $|\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and 100 MC runs. $^\dagger$RMSE exceeds Global.}
540	\label{tab:main_supp}
541	\small
542	\begin{tabular}{ll ccc}
543	\toprule
544	Configuration & Method & $|\text{Bias}|$ & RMSE & Cov. \\
545	\midrule
546	\multirow{4}{*}{\shortstack[l]{Synthetic DIM\\$K{=}2$, moderate, $n{=}250$}}
547	 & Naive & 0.018 & 0.064 & 0.95 \\
548	 & Global & 0.009 & 0.074 & 0.96 \\
549	 & Strat.\ MLE & \textbf{0.005} & 0.075$^\dagger$ & 0.97 \\
550	 & HB EC-HTE & \textbf{0.005} & 0.075$^\dagger$ & 0.97 \\
551	\midrule
552	\multirow{4}{*}{\shortstack[l]{Semi-synthetic\\TweetEval, extreme, $n{=}250$}}
553	 & Naive & 0.027 & 0.103 & 0.93 \\
554	 & Global & \textbf{0.023} & 0.124 & 0.92 \\
555	 & Strat.\ MLE & 0.032 & 0.248$^\dagger$ & 0.91 \\
556	 & HB EC-HTE & 0.027 & 0.225$^\dagger$ & 0.91 \\
557	\bottomrule
558	\end{tabular}
559	\end{table}
560	
561	\section{PPCI Complementarity Results}
562	\label{app:ppci}
563	\label{sec:ppci}
564	
565	EC-HTE composes with PPCI~\cite{sui2026ppci} for settings where both covariate misclassification and outcome model error are present: EC-HTE+PPCI reduces $|\text{bias}|$ from 0.179 to 0.007 ($z{=}0$, DGP~C), and the corrected pseudo-outcomes are compatible with other CATE estimators (R-learner bias reduction: 89\%; Appendix~\ref{app:rlearner}).
566	
567	\begin{table*}[t]
568	\centering
569	\caption{PPCI complementarity experiment ($K{=}2$, extreme, $n_{\text{expert}}{=}250$). DGP~A: covariate error only; B: outcome error only ($\sigma{=}0.5$); C: both errors; D: no error. Values are $|\text{bias}|$ and RMSE averaged over two subgroups. $^\star$EC-HTE+PPCI achieves near-zero bias when both error types are present.}
570	\label{tab:ppci}
571	\small
572	\begin{tabular}{ll cccc}
573	\toprule
574	DGP & Method & $|\text{Bias}|_{z=0}$ & $|\text{Bias}|_{z=1}$ & RMSE$_{z=0}$ & RMSE$_{z=1}$ \\
575	\midrule
576	\multirow{5}{*}{A: Covariate}
577	 & Naive & 0.053 & 0.063 & 0.087 & 0.093 \\
578	 & Global & 0.063 & 0.055 & 0.101 & 0.102 \\
579	 & EC-HTE & 0.017 & \textbf{0.013} & 0.097 & 0.108 \\
580	 & PPCI & \textbf{0.015} & 0.020 & 0.162 & 0.168 \\
581	 & EC-HTE+PPCI & 0.017 & \textbf{0.013} & 0.097 & 0.108 \\
582	\midrule
583	\multirow{5}{*}{B: Outcome}
584	 & Naive & 0.189 & 0.197 & 0.206 & 0.212 \\
585	 & Global & 0.185 & 0.208 & 0.204 & 0.228 \\
586	 & EC-HTE & 0.181 & 0.215 & 0.202 & 0.237 \\
587	 & PPCI & 0.015 & \textbf{0.020} & 0.171 & 0.176 \\
588	 & EC-HTE+PPCI & \textbf{0.012} & 0.023 & 0.171 & 0.186 \\
589	\midrule
590	\multirow{5}{*}{C: Both}
591	 & Naive & 0.251 & 0.135 & 0.267 & 0.155 \\
592	 & Global & 0.182 & 0.209 & 0.233 & 0.235 \\
593	 & EC-HTE & 0.179 & 0.216 & 0.224 & 0.262 \\
594	 & PPCI & 0.017 & 0.007 & 0.241 & 0.232 \\
595	 & EC-HTE+PPCI$^\star$ & \textbf{0.007} & \textbf{0.008} & 0.209 & 0.223 \\
596	\midrule
597	\multirow{5}{*}{D: None}
598	 & Naive & \textbf{0.007} & 0.003 & 0.060 & 0.065 \\
599	 & Global & 0.010 & \textbf{0.002} & 0.061 & 0.071 \\
600	 & EC-HTE & 0.013 & 0.007 & 0.062 & 0.079 \\
601	 & PPCI & \textbf{0.007} & \textbf{0.003} & 0.060 & 0.065 \\
602	 & EC-HTE+PPCI & 0.013 & 0.007 & 0.062 & 0.079 \\
603	\bottomrule
604	\end{tabular}
605	\end{table*}
606	
607	The complementarity of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).
608	Since covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.
609	Under covariate error only, PPCI adds nothing; under no error, all methods perform equivalently.
610	
611	\section{Real-Data Case Study: Hate Speech Detection}
612	\label{app:hatespeech}
613	
614	We apply EC-HTE to the UC Berkeley Measuring Hate Speech corpus~\cite{kennedy2020constructing}, annotating 2{,}496 comments for dehumanization using GPT-4.1.
615	Four text-feature subgroups are defined by crossing platform (Reddit/Gab vs.\ Twitter/YouTube) and text length (above/below median), yielding balanced groups ($n \approx 624$ each).
616	
617	\paragraph{Positive finding: real-world heterogeneity.}
618	Per-subgroup misclassification rates range from 0.266 to 0.383, confirming heterogeneity ($\Delta\pi = 0.117$) in a real annotation setting.
619	At the error-type level, FPR ranges from 8.5\% to 21.3\% across text-feature subgroups, demonstrating that subgroup-varying misclassification is not an artifact of synthetic design but arises naturally in real NLP annotation tasks.
620	
621	\paragraph{Boundary condition: statistical power at extreme FNR.}
622	Correction results are inconclusive: all corrected confidence intervals contain zero, and point estimate differences between methods are not statistically significant.
623	The high baseline FNR (53.3\%) amplifies variance through matrix inversion (variance amplification factor up to 15.7$\times$), rendering the comparison underpowered.
624	When $P(\hat{Z}{=}1 \mid Z{=}1) \approx 0.5$, the confusion matrix approaches singularity, and inversion amplifies estimation noise regardless of stratification strategy.
625	This complements the expert budget threshold identified in Appendix~\ref{sec:budget}: EC-HTE requires \emph{both} sufficient expert labels \emph{and} sufficient baseline classifier quality.
626	
627	\paragraph{Diagnostic connection.}
628	The diagnostic criterion ($\Delta\pi \times \Delta\tau$, Section~\ref{sec:diagnostic}) identifies when correction is worthwhile under moderate baseline accuracy.
629	This case study illustrates that even when $\Delta\pi$ is large, extreme baseline error renders correction underpowered rather than beneficial.
630	A practical prerequisite is that the per-subgroup confusion matrix condition number $\kappa(\hat{C}_s)$ remain moderate; when $\kappa > 50$, as observed here, practitioners should prioritize improving annotation quality before applying any matrix-inversion-based correction.
631	
632	\section{Cross-Model Consistency}
633	\label{app:multilm}
634	
635	We evaluate whether misclassification heterogeneity is model-specific by annotating 500 TweetEval sentiment tweets with six OpenAI models spanning three generations.
636	Six text-feature subgroups are defined by crossing hashtag presence and text length.
637	Spearman rank correlations of per-subgroup error rates across all six subgroups range from $\rho = 0.82$ to $1.00$, indicating that the subgroup error structure is consistent across architectures.
638	Two subgroups with $n \leq 6$ exhibit zero misclassification across all models; excluding these yields four-point correlations that are directionally consistent but underpowered.%
639	\footnote{The filtered $\Delta\pi$ values in Table~\ref{tab:multilm} serve as a robustness check independent of rank-order testing: all six models exceed $\Delta\pi > 0.05$ on the four retained subgroups.}
640	
641	\begin{table}[t]
642	\centering
643	\caption{Effective misclassification heterogeneity ($\Delta\pi$) across six OpenAI models on TweetEval sentiment (500 tweets, filtered to 4 subgroups with $n \geq 10$).}
644	\label{tab:multilm}
645	\small
646	\begin{tabular}{lcc}
647	\toprule
648	Model & Effective $\Delta\pi$ & $> 0.05$? \\
649	\midrule
650	GPT-3.5-Turbo & 0.198 & \checkmark \\
651	GPT-4-Turbo & 0.149 & \checkmark \\
652	GPT-4o-mini & 0.136 & \checkmark \\
653	GPT-5.4 & 0.114 & \checkmark \\
654	GPT-4.1 & 0.098 & \checkmark \\
655	GPT-4o & 0.080 & \checkmark \\
656	\bottomrule
657	\end{tabular}
658	\end{table}
659	
660	All six models exhibit effective $\Delta\pi > 0.05$ on the four retained subgroups (Table~\ref{tab:multilm}), and 5 of 6 share the same worst subgroup (\texttt{True\_medium}: tweets with hashtags and medium text length).
661	Newer models reduce absolute error rates but do not eliminate subgroup heterogeneity: GPT-5.4 achieves $\Delta\pi = 0.114$ compared to GPT-3.5-Turbo's $0.198$.
662	These results were obtained with a single API provider; open-source model validation appears in Appendix~\ref{app:multilm_opensource}.
663	
664	\section{Open-Source Multi-LLM Validation}
665	\label{app:multilm_opensource}
666	
667	We evaluate four open-source LLMs (7B--9B parameter range) on 490 TweetEval sentiment tweets with $K{=}4$ subgroups defined by crossing hashtag presence and text length.
668	Table~\ref{tab:multilm_cm} reports the confusion matrix heterogeneity profile.
669	All four models exhibit $\Delta\pi > 0.05$, confirming that subgroup-heterogeneous misclassification is not specific to proprietary APIs.
670	Subgroup error rankings are consistent across architectures: \texttt{True\_short} (short tweets with hashtags) has the lowest $\pi_s$ in 3 of 4 models, while \texttt{False\_medium} (medium tweets without hashtags) has the highest.
671	
672	\begin{table}[t]
673	\centering
674	\caption{Confusion matrix heterogeneity across four open-source LLMs ($K{=}4$, $N{=}490$ TweetEval tweets). $\Delta\pi$: max--min per-subgroup misclassification rate. Prop.~5: number of subgroups where the $\Delta\tau$-free diagnostic (Proposition~\ref{prop:debiasing_hurts}) triggers.}
675	\label{tab:multilm_cm}
676	\small
677	\begin{tabular}{lcccl}
678	\toprule
679	Model & Acc.\ & $\Delta\pi$ & Prop.~5 & Strongest \\
680	\midrule
681	Llama-3.1-8B & 0.755 & 0.141 & 1/4 & True\_short \\
682	Qwen-2.5-7B & 0.798 & 0.165 & 1/4 & True\_short \\
683	Gemma-2-9B & 0.763 & 0.125 & 4/4 & True\_medium \\
684	Mistral-7B & 0.802 & 0.134 & 0/4 & --- \\
685	\bottomrule
686	\end{tabular}
687	\end{table}
688	
689	\paragraph{Semi-synthetic budget sweep.}
690	We run the full EC-HTE pipeline with $K{=}2$ subgroups and $\Delta\tau{=}0.3$, using each model's empirical confusion matrices.
691	Table~\ref{tab:multilm_budget} reports coverage and RMSE crossover points.
692	EC-HTE restores near-nominal coverage from 0.714 (naive average) to 0.939 ($+$22.5 percentage points) at $n_{\text{expert}}{=}1{,}000$, consistent across all four models.
693	Global correction achieves comparable or lower RMSE than HB at all budgets under these moderate $\Delta\pi$ values, and the $K{=}4$ RMSE crossover never occurs---confirming the budget guidelines in Appendix~\ref{sec:budget}.
694	
695	\begin{table}[t]
696	\centering
697	\caption{Semi-synthetic budget sweep ($K{=}2$, $\Delta\tau{=}0.3$, 50 MC runs; see Appendix~\ref{app:mcse} for MC tier justification). Coverage at selected expert budgets; RMSE crossover denotes the minimum expert budget at which HB EC-HTE achieves lower RMSE than the naive (uncorrected) estimator.}
698	\label{tab:multilm_budget}
699	\small
700	\begin{tabular}{lcccc}
701	\toprule
702	Model & $\Delta\pi_{K{=}2}$ & Naive Cov.\ & HB Cov.\ ($n{=}1000$) & Crossover \\
703	\midrule
704	Llama-3.1-8B & 0.051 & 0.675 & 0.940 & $n{=}1000$ \\
705	Qwen-2.5-7B & 0.080 & 0.715 & 0.925 & $n{=}1000$ \\
706	Gemma-2-9B & 0.100 & 0.705 & 0.945 & $n{=}1000$ \\
707	Mistral-7B & 0.070 & 0.760 & 0.945 & $n{=}1000$ \\
708	\midrule
709	\textit{Average} & --- & \textit{0.714} & \textit{0.939} & --- \\
710	\bottomrule
711	\end{tabular}
712	\end{table}
713	
714	\paragraph{Gemma boundary case.}
715	Gemma-2-9B triggers the Proposition~\ref{prop:debiasing_hurts} diagnostic in all four $K{=}4$ subgroups due to extreme FPR--FNR asymmetry (\texttt{False\_medium} FNR $= 0.437$).
716	At small budgets ($K{=}4$, $n{=}100$), EC-HTE RMSE reaches 1.229 ($3.1\times$ naive), illustrating the budget guideline from Appendix~\ref{sec:budget}: when per-subgroup cell counts fall below 25, the variance cost of stratified correction dominates.
717	At $n \geq 500$, EC-HTE coverage recovers to $>$0.90, consistent with the synthetic experiments.
718	
719	\paragraph{Heterogeneous-$\tau$ DGP.}
720	To assess whether the constant-$\tau$ DGP understates EC-HTE's advantage, we run a supplementary experiment using Llama's empirical confusion matrices with heterogeneous treatment effects across subgroups ($\Delta\tau \in [0.1, 0.6]$, $K{=}2$, 50 MC runs).
721	EC-HTE achieves lower $|\text{bias}|$ than global correction at all budgets ($n{=}500$: 0.010 vs.\ 0.031, a 68\% reduction).
722	In the high-$\Delta\tau$ subgroup (\texttt{True\_short}, $\Delta\tau{=}0.6$), EC-HTE also achieves lower RMSE ($n{=}1{,}000$: 0.212 vs.\ 0.258, 18\% improvement), confirming that the RMSE advantage concentrates in subgroups where correction is most needed.
723	Aggregate RMSE remains comparable to global correction because low-$\Delta\tau$ subgroups incur stratification variance without commensurate bias reduction, consistent with the budget guidelines in Appendix~\ref{sec:budget}.
724	
725	\section{Robustness to Subgroup Misspecification}
726	\label{app:robustness}
727	
728	EC-HTE requires pre-defined subgroup labels, which may be noisy in practice.
729	We test robustness by randomly flipping each observation's subgroup assignment with probability $p_{\text{flip}} \in \{0, 0.10, 0.25, 0.50\}$, across $K \in \{2, 4\}$ (extreme regime, $n_{\text{expert}} = 500$, $\Delta\tau = 0.3$, 100 MC runs).
730	
731	\begin{table}[t]
732	\centering
733	\caption{95\% CI coverage under subgroup misspecification noise. EC-HTE maintains near-nominal coverage across all noise levels.}
734	\label{tab:robustness}
735	\small
736	\begin{tabular}{lcccc}
737	\toprule
738	& \multicolumn{4}{c}{$p_{\text{flip}}$} \\
739	\cmidrule(lr){2-5}
740	Method & 0.00 & 0.10 & 0.25 & 0.50 \\
741	\midrule
742	\multicolumn{5}{l}{\textit{$K{=}2$, extreme}} \\
743	\quad Naive & 0.875 & 0.877 & 0.890 & 0.897 \\
744	\quad Global & 0.925 & 0.935 & 0.932 & 0.945 \\
745	\quad HB EC-HTE & 0.958 & 0.948 & 0.950 & 0.945 \\
746	\midrule
747	\multicolumn{5}{l}{\textit{$K{=}4$, extreme}} \\
748	\quad Naive & 0.904 & 0.916 & 0.909 & 0.919 \\
749	\quad Global & 0.930 & 0.953 & 0.948 & 0.944 \\
750	\quad HB EC-HTE & 0.956 & 0.958 & 0.960 & 0.946 \\
751	\bottomrule
752	\end{tabular}
753	\end{table}
754	
755	EC-HTE maintains coverage $\geq 0.945$ across all configurations (Table~\ref{tab:robustness}), while the naive estimator is systematically below nominal (0.875--0.919).
756	At $p_{\text{flip}} = 0.50$, subgroup structure is effectively destroyed; EC-HTE converges to global correction (coverage and RMSE within 0.1\%), confirming that hierarchical Bayesian shrinkage provides a built-in safety mechanism.
757	For $K{=}4$ at $p_{\text{flip}} = 0.50$, a small residual RMSE gap persists ($p < 0.01$), reflecting the variance cost of estimating four confusion matrices even when they carry no signal.
758	
759	\section{Monte Carlo Standard Errors}
760	\label{app:mcse}
761	
762	All main-text and most appendix experiments use 100 independent Monte Carlo replications per configuration; computationally intensive analyses (R-learner, multiplicative DGP, budget sweeps) use 50, and bootstrap experiments use 20 due to the $B{\times}$CF cost per seed.
763	The median RMSE variation between 50-seed and 100-seed estimates is below 3.2\%, confirming that 50-run results are stable.
764	We report Monte Carlo standard errors to assess whether observed differences between methods are statistically reliable.
765	For exp-001 (synthetic DGP, no per-seed pairing across methods), we use conservative two-sample $z$-tests on the 100-run means.
766	For exp-003 (semi-synthetic TweetEval, shared seeds across methods), we use paired $t$-tests, which are more powerful because they control for seed-level variation.
767	
768	Table~\ref{tab:mcse} reports paired comparisons for representative configurations.
769	Of 1{,}020 total pairwise comparisons across all configurations, 742 (72.7\%) are statistically significant at $\alpha = 0.05$.
770	
771	\begin{table}[t]
772	\centering
773	\caption{Paired comparisons for representative configurations. $\Delta$ = method A $-$ method B (negative favors A for $|\text{bias}|$). Two-sample $z$-tests for synthetic (exp-001); paired $t$-tests for semi-synthetic (exp-003). Bold $p$-values indicate significance at $\alpha = 0.05$.}
774	\label{tab:mcse}
775	\small
776	\begin{tabular}{llrr}
777	\toprule
778	Configuration & Comparison & $\Delta$ & $p$ \\
779	\midrule
780	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Global ($|\text{bias}|$)}} \\
781	\quad $K{=}2$/ext/$n{=}500$ & & $-0.046$ & $\mathbf{<0.001}$ \\
782	\quad $K{=}4$/ext/$n{=}500$ & & $-0.078$ & $\mathbf{<0.001}$ \\
783	\quad $K{=}4$/mod/$n{=}250$ & & $-0.017$ & $0.288$ \\
784	\quad TweetEval/ext/$n{=}250$ & & $+0.001$ & $0.395$ \\
785	\midrule
786	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Global (RMSE)}} \\
787	\quad $K{=}2$/ext/$n{=}500$ & & $+0.015$ & $0.179$ \\
788	\quad $K{=}4$/ext/$n{=}500$ & & $+0.048$ & $\mathbf{0.011}$ \\
789	\midrule
790	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Naive ($|\text{bias}|$)}} \\
791	\quad $K{=}2$/ext/$n{=}500$ & & $-0.089$ & $\mathbf{<0.001}$ \\
792	\quad $K{=}4$/ext/$n{=}500$ & & $-0.113$ & $\mathbf{<0.001}$ \\
793	\quad $K{=}4$/mod/$n{=}250$ & & $-0.031$ & $\mathbf{0.038}$ \\
794	\quad TweetEval/ext/$n{=}250$ & & $+0.005$ & $\mathbf{0.030}$ \\
795	\bottomrule
796	\end{tabular}
797	\end{table}
798	
799	Under extreme heterogeneity, HB EC-HTE's bias advantage over global correction is highly significant ($p < 0.001$ for both $K{=}2$ and $K{=}4$).
800	The RMSE penalty of stratification is not significant at $K{=}2$ ($p = 0.179$) but reaches significance at $K{=}4$ ($p = 0.011$), consistent with the higher variance cost of estimating four confusion matrices.
801	Under moderate heterogeneity ($K{=}4$, $n{=}250$), the bias difference between HB and global is not significant ($p = 0.288$), confirming that EC-HTE's advantage requires sufficient error heterogeneity.
802	In the semi-synthetic TweetEval experiment, HB EC-HTE does not significantly improve over global ($p = 0.395$), consistent with moderate $\Delta\pi$ and unbalanced subgroup sizes.
803	The HB vs.\ naive comparison in TweetEval is significant ($p = 0.030$) but favors naive, reflecting the variance cost of stratification when bias reduction is marginal.
804	
805	\section{Semi-Real Confusion Matrix Validation}
806	\label{app:semireal}
807	
808	We test EC-HTE with empirical asymmetric confusion matrices from the GPT-4.1 TweetEval pilot.
809	Four text-feature subgroups ($K{=}4$) retain the real per-subgroup FPR and FNR from pilot annotations (Table~\ref{tab:semireal_cm}); CATE heterogeneity is injected synthetically ($\tau(z{=}0,s) = 0.3 + 0.1s$, $\tau(z{=}1,s) = 0.8 - 0.15s$).
810	$N{=}5{,}000$, $P(Z{=}1){=}0.18$, 100 MC seeds per $n_{\text{expert}}$ level.
811	
812	\begin{table}[t]
813	\centering
814	\caption{Empirical confusion matrices from GPT-4.1 TweetEval pilot.
815	S0 exhibits FNR $= 0.526$, approaching chance-level classification.}
816	\label{tab:semireal_cm}
817	\small
818	\begin{tabular}{lcccc}
819	\toprule
820	Subgroup & Weight & FPR & FNR & $\kappa(\hat{C}_s)$ \\
821	\midrule
822	S0 & 0.38 & 0.054 & 0.526 & high \\
823	S1 & 0.22 & 0.101 & 0.300 & moderate \\
824	S2 & 0.14 & 0.143 & 0.308 & moderate \\
825	S3 & 0.25 & 0.194 & 0.222 & low \\
826	\bottomrule
827	\end{tabular}
828	\end{table}
829	
830	\begin{table}[t]
831	\centering
832	\caption{Semi-real confusion matrix results. RMSE and coverage averaged over subgroups and $z$-levels (100 MC runs). HB EC-HTE underperforms global at all budgets; S0's near-chance FNR drives the failure.}
833	\label{tab:semireal}
834	\small
835	\begin{tabular}{llcc}
836	\toprule
837	$n_{\text{expert}}$ & Method & RMSE $\downarrow$ & Coverage $\uparrow$ \\
838	\midrule
839	\multirow{4}{*}{100}
840	 & Oracle & 0.101 & 0.957 \\
841	 & Naive & 0.123 & 0.879 \\
842	 & Global & 0.263 & 0.885 \\
843	 & HB EC-HTE & 0.784 & 0.744 \\
844	\midrule
845	\multirow{4}{*}{250}
846	 & Oracle & 0.101 & 0.957 \\
847	 & Naive & 0.123 & 0.879 \\
848	 & Global & 0.232 & 0.909 \\
849	 & HB EC-HTE & 0.411 & 0.834 \\
850	\midrule
851	\multirow{4}{*}{500}
852	 & Oracle & 0.101 & 0.957 \\
853	 & Naive & 0.123 & 0.879 \\
854	 & Global & 0.196 & 0.922 \\
855	 & HB EC-HTE & 0.260 & 0.890 \\
856	\bottomrule
857	\end{tabular}
858	\end{table}
859	
860	HB EC-HTE produces higher RMSE and lower coverage than global correction at all expert budgets (Table~\ref{tab:semireal}).
861	The root cause is S0's FNR $= 0.526$: when a confusion matrix row approaches a uniform distribution ($P(\hat{Z}{=}1 \mid Z{=}1) \approx 0.5$), inversion amplifies estimation noise regardless of the expert budget.
862	This converges with the hate speech case study (Appendix~\ref{app:hatespeech}, FNR $= 53.3$\%) and confirms that EC-HTE requires \emph{both} sufficient expert labels \emph{and} sufficient baseline classifier quality per subgroup.
863	The singularity guard ($\kappa > 100$, Section~\ref{sec:method}) mitigates catastrophic failure by falling back to global correction for near-degenerate subgroups, but does not recover the bias reduction that motivates stratification.
864	For a $2 \times 2$ symmetric confusion matrix, $\kappa = 1/|1-2\pi|$; $\kappa > 100$ corresponds to $\pi \in (0.495, 0.505)$, so the guard triggers only when the classifier performs within $0.5\%$ of random guessing.
865	At $n_{\text{expert}} = 500$, HB EC-HTE narrows the gap (RMSE 0.260 vs.\ 0.196) as confusion matrix estimates stabilize for the three well-classified subgroups, but the S0 bottleneck persists.
866	
867	A second semi-real experiment using GPT-3.5-Turbo confusion matrices (worst-subgroup FPR $= 0.39$, FNR $= 0.21$) yields similar results: HB RMSE exceeds global by 1.3--3.5$\times$ at all budgets.
868	Here the failure stems from high false-positive rates compounded by class imbalance ($P(Z{=}1) = 0.18$), which leaves insufficient expert observations in the positive class for reliable per-subgroup confusion matrix estimation.
869	Together, these experiments identify three applicability conditions for EC-HTE: (1)~sufficient effective expert budget ($n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$), (2)~no near-chance subgroup error rate ($\max(\text{FPR}_s, \text{FNR}_s) < 0.5$), and (3)~adequate class balance in the effect modifier.
870	
871	\paragraph{Diagnostic rule.}
872	A logistic regression over all 368 semi-real experiment--budget cells (dependent variable: HB EC-HTE $<$ Global RMSE) identifies two sufficient statistics: the worst-subgroup confusion matrix condition number $\kappa(\hat{M}_s) \leq 1.25$ and the effective minority-class expert count $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$.
873	When both conditions hold, HB outperforms global in 93.3\% of cells; when either is violated, global is preferred in 94.7\% of cells.
874	Both exp-015 ($\kappa = 2.38$, effective $n = 2.5$) and exp-016 ($\kappa = 1.55$, effective $n = 2.5$) violate both conditions, and the diagnostic correctly predicts 100\% of their failure cells.
875	Subgroup-average metrics can mask cell-level heterogeneity: in exp-015, HB EC-HTE substantially reduces bias for the three well-classified subgroups (S1--S3) but amplifies variance in the near-degenerate subgroup (S0, FNR $= 0.526$), and the S0 penalty dominates the aggregate RMSE.
876	
877	\begin{figure}[t]
878	\centering
879	\includegraphics[width=\columnwidth]{figures/applicability_frontier.pdf}
880	\caption{Applicability frontier of EC-HTE. Green region: EC-HTE reduces bias vs.\ global correction. Yellow: comparable performance. Red: EC-HTE underperforms. Dashed lines mark the expert budget threshold ($n_{\text{expert}}/K = 25$) and classifier quality threshold (worst-subgroup error rate $= 0.5$). Red diamonds show semi-real experiments with actual GPT-4.1 and GPT-3.5-Turbo confusion matrices.}
881	\label{fig:applicability}
882	\end{figure}
883	
884	\section{Robustness: Estimator Choice and Treatment Effect Specification}
885	\label{app:rlearner}
886	
887	We verify that EC-HTE's corrected pseudo-outcomes are compatible with downstream estimators beyond CausalForest by replacing it with the R-learner~\citep{nie2021quasi}.
888	The experiment uses $K{=}2$, extreme heterogeneity, $n_{\text{expert}} = 500$, and 50 MC seeds; the R-learner uses 5-fold cross-fitting with gradient-boosted trees as the base learner.
889	
890	\begin{table}[t]
891	\centering
892	\caption{R-learner vs.\ CausalForest with EC-HTE correction ($K{=}2$, extreme, $n{=}500$). $|\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and seeds.}
893	\label{tab:rlearner}
894	\small
895	\begin{tabular}{llccc}
896	\toprule
897	Estimator & Correction & $|\text{Bias}|$ & RMSE & Cov. \\
898	\midrule
899	\multirow{4}{*}{R-learner}
900	 & Oracle & 0.006 & 0.056 & 0.94 \\
901	 & Naive & 0.121 & 0.139 & 0.47 \\
902	 & Global & 0.098 & 0.123 & 0.72 \\
903	 & EC-HTE & \textbf{0.013} & 0.080 & 0.92 \\
904	\midrule
905	\multirow{2}{*}{CausalForest}
906	 & Naive & 0.058 & 0.090 & 0.82 \\
907	 & EC-HTE & \textbf{0.010} & 0.093 & 0.95 \\
908	\bottomrule
909	\end{tabular}
910	\end{table}
911	
912	EC-HTE reduces R-learner $|\text{bias}|$ by 89\% (0.121 $\to$ 0.013) and restores coverage from 0.47 to 0.92 (Table~\ref{tab:rlearner}).
913	The bias reduction and coverage gains are comparable to those achieved with CausalForest, confirming that EC-HTE is compatible with a range of HTE estimators.
914	
915	\paragraph{Multiplicative treatment effects.}
916	We further test robustness to the functional form of treatment effects by replacing the additive DGP with a multiplicative specification: $Y(1) = Y(0) \times \exp(\tau(Z))$, using $K{=}2$, extreme heterogeneity, $n_{\text{expert}} = 500$, and 50 MC seeds.
917	
918	\begin{table}[t]
919	\centering
920	\caption{Multiplicative DGP results ($K{=}2$, extreme, $n{=}500$, 50 seeds). EC-HTE achieves comparable bias reduction and nominal coverage under non-additive treatment effects.}
921	\label{tab:multiplicative}
922	\small
923	\begin{tabular}{lccc}
924	\toprule
925	Method & $|\text{Bias}|$ & RMSE & Cov. \\
926	\midrule
927	Oracle & 0.003 & 0.038 & 0.96 \\
928	Naive & 0.135 & 0.142 & 0.44 \\
929	Global & 0.110 & 0.124 & 0.54 \\
930	EC-HTE & \textbf{0.054} & 0.068 & 0.955 \\
931	\bottomrule
932	\end{tabular}
933	\end{table}
934	
935	EC-HTE reduces RMSE by 52\% relative to naive (0.068 vs.\ 0.142) and restores coverage to the nominal level (0.955; Table~\ref{tab:multiplicative}).
936	EC-HTE's bias correction operates at the confusion matrix level, independent of the downstream CATE estimator and functional form of treatment effects.
937	
938	\section{Robustness to Class Imbalance}
939	\label{app:classimbalance}
940	
941	Assumption (A3) requires $P(Z{=}1) = 0.5$, but real-world effect modifiers are often imbalanced.
942	We sweep $P(Z{=}1) \in \{0.1, 0.2, 0.3, 0.4, 0.5\}$ with $K \in \{2,4\}$, extreme misclassification heterogeneity, $n_{\text{expert}}{=}250$, and 100 MC seeds (Table~\ref{tab:pz1_sweep}).
943	
944	\begin{table}[t]
945	\centering
946	\caption{Robustness to class imbalance ($n_{\text{expert}}{=}250$, extreme heterogeneity). R$^2$: Theorem~\ref{thm:bias_identity} fit. Ratio: HB/Global RMSE ($<1$ = HB wins). Cov.: HB EC-HTE 95\% CI coverage.}
947	\label{tab:pz1_sweep}
948	\small
949	\begin{tabular}{cc ccc}
950	\toprule
951	$P(Z{=}1)$ & $K$ & R$^2$ & Ratio & Cov. \\
952	\midrule
953	0.1 & 2 & 0.998 & 0.92 & 0.94 \\
954	0.2 & 2 & 0.989 & 0.76 & 0.94 \\
955	0.3 & 2 & 0.994 & 0.78 & 0.94 \\
956	0.4 & 2 & 0.995 & 0.87 & 0.94 \\
957	0.5 & 2 & 0.995 & 0.86 & 0.93 \\
958	\midrule
959	0.1 & 4 & 0.984 & 1.54 & 0.92 \\
960	0.2 & 4 & 0.976 & 1.68 & 0.93 \\
961	0.3 & 4 & 0.985 & 1.12 & 0.92 \\
962	0.4 & 4 & 0.984 & 1.08 & 0.93 \\
963	0.5 & 4 & 0.992 & 1.06 & 0.92 \\
964	\bottomrule
965	\end{tabular}
966	\end{table}
967	
968	Theorem~\ref{thm:bias_identity}'s product form remains accurate across all imbalance levels: $R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$, confirming that the bias identity derives from confusion matrix structure rather than class balance.
969	For $K{=}2$, EC-HTE outperforms global correction at all $P(Z{=}1)$ levels (RMSE ratio 0.76--0.92), degrading gracefully under severe imbalance.
970	For $K{=}4$, EC-HTE underperforms global at $n_{\text{expert}}{=}250$ (ratio 1.06--1.68), consistent with the budget threshold $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$: at $P(Z{=}1){=}0.1$, $K{=}4$, each subgroup receives only ${\sim}6$ minority-class labels.
971	The gap narrows as $P(Z{=}1)$ increases (1.54 $\to$ 1.06), and coverage remains stable at 0.92--0.94 across all configurations.
972	
973	\paragraph{Explicit form under relaxed (A3).}
974	When $P(Z{=}0) = p_0 \neq 0.5$, the mixing matrix $M_s$ no longer coincides with the confusion matrix $C_s$.
975	By Bayes' rule, for symmetric misclassification (A2):
976	\begin{equation}
977	M_s = \begin{bmatrix} \frac{(1-\pi_s) p_0}{(1-\pi_s) p_0 + \pi_s p_1} & \frac{\pi_s p_1}{(1-\pi_s) p_0 + \pi_s p_1} \\[4pt]
978	\frac{\pi_s p_0}{\pi_s p_0 + (1-\pi_s) p_1} & \frac{(1-\pi_s) p_1}{\pi_s p_0 + (1-\pi_s) p_1}
979	\end{bmatrix},
980	\label{eq:ms_imbalanced}
981	\end{equation}
982	where $p_1 = 1 - p_0$.
983	The bias identity $\mathrm{bias}(z, s) = [(M_{\mathrm{global}}^{-1} M_s - I) \boldsymbol{\tau}]_z$ holds exactly for any $p_0$ because $B_s = M_{\mathrm{global}}^{-1} M_s - I$ satisfies $B_s \mathbf{1} = \mathbf{0}$ by stochasticity, so the bias reduces to $\Delta\tau \cdot [B_s]_{z,1}$ regardless of class balance.
984	The class imbalance modifies $[B_s]_{z,1}$ through the Bayesian normalization in \eqref{eq:ms_imbalanced} but preserves the product-form structure; the high $R^2$ values in Table~\ref{tab:pz1_sweep} confirm this empirically.
985	
986	\section{Comparison with PPI Correction}
987	\label{app:ppi_comparison}
988	
989	PPI~\cite{angelopoulos2023ppi} constructs confidence intervals by combining a large set of ML predictions with a smaller set of gold-standard labels, using the gold labels to debias the ML-based estimator.
990	Applied to our setting, PPI treats the LLM-annotated effect modifier as the ML prediction and the expert labels as the gold standard.
991	Two variants arise naturally: \emph{PPI-global} pools all expert labels to estimate a single rectifier (analogous to our Global baseline), and \emph{PPI-subgroup} estimates per-subgroup rectifiers (analogous to Stratified MLE).
992	
993	Under the confusion-matrix parameterization we adopt, DSL's measurement error correction reduces to confusion matrix inversion.
994	Pooled DSL applies a single estimated confusion matrix to all subgroups, producing the same corrected label distribution as our Global baseline; per-subgroup DSL estimates a separate confusion matrix for each subgroup and inverts it independently, equivalent to our Stratified MLE.
995	EC-HTE's contribution over both PPI-subgroup and per-subgroup DSL is hierarchical partial pooling: rather than estimating each subgroup's confusion matrix in isolation, EC-HTE places a shared prior across subgroups, borrowing strength to reduce variance while preserving subgroup-specific bias correction.
996	This mechanism is outside both the PPI and DSL frameworks.
997	
998	The key difference between PPI and confusion-matrix inversion is that PPI does not invert the confusion matrix; instead, it uses the gold labels to directly debias the estimand.
999	This avoids the matrix inversion step that can amplify noise at small $n_{\text{expert}}$, but it also means PPI cannot exploit the structure of the misclassification process to reduce bias.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa58e9a6-7301-48dc-a0eb-71cbb0a82009",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "fdb29562-597c-47f7-a8ef-3a00ebd6bfa4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
      "content": "\\midrule\n\\multicolumn{5}{l}{\\emph{$K = 4$}} \\\\\n1:2 & 0.68 & 0.86 & 0.91 & 0.96 \\\\\n1:3 & 0.70 & 0.85 & 0.94 & 0.95 \\\\\n1:5 & 0.69 & 0.84 & 0.90 & 0.93 \\\\\n2:1 & 0.63 & 0.79 & 0.86 & 0.93 \\\\\n3:1 & 0.50 & 0.78 & 0.88 & 0.92 \\\\\n5:1 & 0.50 & 0.73 & 0.84 & 0.89 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:asym_method_grid} compares correction methods averaged over all 48 configurations.\nEC-HTE does not outperform global correction: its RMSE exceeds Global in every configuration (0.125 vs.\\ 0.109 overall).\nEstimating the full asymmetric $J{\\times}J$ confusion matrix requires twice the parameters (FPR and FNR separately per subgroup), shifting the bias-variance tradeoff toward higher variance at $n_{\\text{expert}} = 250$.\nWe recommend $n_{\\text{expert}} \\geq 500$ for asymmetric settings to provide sufficient per-subgroup samples for stable CM estimation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Method comparison under asymmetric misclassification (48 configurations, 100 MC runs). EC-HTE does not outperform global correction at $n_{\\text{expert}}{=}250$ due to increased parameter estimation variance.}\n\\label{tab:asym_method_grid}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\nMethod & $|\\text{Bias}| \\downarrow$ & RMSE $\\downarrow$ & Coverage $\\uparrow$ \\\\\n\\midrule\nOracle & 0.058 & 0.072 & 0.946 \\\\\nNaive & 0.080 & 0.096 & 0.830 \\\\\nGlobal & 0.088 & 0.109 & 0.931 \\\\\nEC-HTE (HB) & 0.098 & 0.125 & 0.920 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Supplementary Main Results}\n\\label{app:main_supp}\n\n\\begin{table}[t]\n\\centering\n\\caption{Additional configurations from the main experiment. $|\\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and 100 MC runs. $^\\dagger$RMSE exceeds Global.}\n\\label{tab:main_supp}\n\\small\n\\begin{tabular}{ll ccc}\n\\toprule\nConfiguration & Method & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Synthetic DIM\\\\$K{=}2$, moderate, $n{=}250$}}\n & Naive & 0.018 & 0.064 & 0.95 \\\\\n & Global & 0.009 & 0.074 & 0.96 \\\\\n & Strat.\\ MLE & \\textbf{0.005} & 0.075$^\\dagger$ & 0.97 \\\\\n & HB EC-HTE & \\textbf{0.005} & 0.075$^\\dagger$ & 0.97 \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Semi-synthetic\\\\TweetEval, extreme, $n{=}250$}}\n & Naive & 0.027 & 0.103 & 0.93 \\\\\n & Global & \\textbf{0.023} & 0.124 & 0.92 \\\\\n & Strat.\\ MLE & 0.032 & 0.248$^\\dagger$ & 0.91 \\\\\n & HB EC-HTE & 0.027 & 0.225$^\\dagger$ & 0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{PPCI Complementarity Results}\n\\label{app:ppci}\n\\label{sec:ppci}\n\nEC-HTE composes with PPCI~\\cite{sui2026ppci} for settings where both covariate misclassification and outcome model error are present: EC-HTE+PPCI reduces $|\\text{bias}|$ from 0.179 to 0.007 ($z{=}0$, DGP~C), and the corrected pseudo-outcomes are compatible with other CATE estimators (R-learner bias reduction: 89\\%; Appendix~\\ref{app:rlearner}).\n\n\\begin{table*}[t]\n\\centering\n\\caption{PPCI complementarity experiment ($K{=}2$, extreme, $n_{\\text{expert}}{=}250$). DGP~A: covariate error only; B: outcome error only ($\\sigma{=}0.5$); C: both errors; D: no error. Values are $|\\text{bias}|$ and RMSE averaged over two subgroups. $^\\star$EC-HTE+PPCI achieves near-zero bias when both error types are present.}\n\\label{tab:ppci}\n\\small\n\\begin{tabular}{ll cccc}\n\\toprule\nDGP & Method & $|\\text{Bias}|_{z=0}$ & $|\\text{Bias}|_{z=1}$ & RMSE$_{z=0}$ & RMSE$_{z=1}$ \\\\\n\\midrule\n\\multirow{5}{*}{A: Covariate}\n & Naive & 0.053 & 0.063 & 0.087 & 0.093 \\\\\n & Global & 0.063 & 0.055 & 0.101 & 0.102 \\\\\n & EC-HTE & 0.017 & \\textbf{0.013} & 0.097 & 0.108 \\\\\n & PPCI & \\textbf{0.015} & 0.020 & 0.162 & 0.168 \\\\\n & EC-HTE+PPCI & 0.017 & \\textbf{0.013} & 0.097 & 0.108 \\\\\n\\midrule\n\\multirow{5}{*}{B: Outcome}\n & Naive & 0.189 & 0.197 & 0.206 & 0.212 \\\\\n & Global & 0.185 & 0.208 & 0.204 & 0.228 \\\\\n & EC-HTE & 0.181 & 0.215 & 0.202 & 0.237 \\\\\n & PPCI & 0.015 & \\textbf{0.020} & 0.171 & 0.176 \\\\\n & EC-HTE+PPCI & \\textbf{0.012} & 0.023 & 0.171 & 0.186 \\\\\n\\midrule\n\\multirow{5}{*}{C: Both}\n & Naive & 0.251 & 0.135 & 0.267 & 0.155 \\\\\n & Global & 0.182 & 0.209 & 0.233 & 0.235 \\\\\n & EC-HTE & 0.179 & 0.216 & 0.224 & 0.262 \\\\\n & PPCI & 0.017 & 0.007 & 0.241 & 0.232 \\\\\n & EC-HTE+PPCI$^\\star$ & \\textbf{0.007} & \\textbf{0.008} & 0.209 & 0.223 \\\\\n\\midrule\n\\multirow{5}{*}{D: None}\n & Naive & \\textbf{0.007} & 0.003 & 0.060 & 0.065 \\\\\n & Global & 0.010 & \\textbf{0.002} & 0.061 & 0.071 \\\\\n & EC-HTE & 0.013 & 0.007 & 0.062 & 0.079 \\\\\n & PPCI & \\textbf{0.007} & \\textbf{0.003} & 0.060 & 0.065 \\\\\n & EC-HTE+PPCI & 0.013 & 0.007 & 0.062 & 0.079 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe complementarity of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).\nSince covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.\nUnder covariate error only, PPCI adds nothing; under no error, all methods perform equivalently.\n\n\\section{Real-Data Case Study: Hate Speech Detection}\n\\label{app:hatespeech}\n\nWe apply EC-HTE to the UC Berkeley Measuring Hate Speech corpus~\\cite{kennedy2020constructing}, annotating 2{,}496 comments for dehumanization using GPT-4.1.\nFour text-feature subgroups are defined by crossing platform (Reddit/Gab vs.\\ Twitter/YouTube) and text length (above/below median), yielding balanced groups ($n \\approx 624$ each).\n\n\\paragraph{Positive finding: real-world heterogeneity.}\nPer-subgroup misclassification rates range from 0.266 to 0.383, confirming heterogeneity ($\\Delta\\pi = 0.117$) in a real annotation setting.\nAt the error-type level, FPR ranges from 8.5\\% to 21.3\\% across text-feature subgroups, demonstrating that subgroup-varying misclassification is not an artifact of synthetic design but arises naturally in real NLP annotation tasks.\n\n\\paragraph{Boundary condition: statistical power at extreme FNR.}\nCorrection results are inconclusive: all corrected confidence intervals contain zero, and point estimate differences between methods are not statistically significant.\nThe high baseline FNR (53.3\\%) amplifies variance through matrix inversion (variance amplification factor up to 15.7$\\times$), rendering the comparison underpowered.\nWhen $P(\\hat{Z}{=}1 \\mid Z{=}1) \\approx 0.5$, the confusion matrix approaches singularity, and inversion amplifies estimation noise regardless of stratification strategy.\nThis complements the expert budget threshold identified in Appendix~\\ref{sec:budget}: EC-HTE requires \\emph{both} sufficient expert labels \\emph{and} sufficient baseline classifier quality.\n\n\\paragraph{Diagnostic connection.}\nThe diagnostic criterion ($\\Delta\\pi \\times \\Delta\\tau$, Section~\\ref{sec:diagnostic}) identifies when correction is worthwhile under moderate baseline accuracy.\nThis case study illustrates that even when $\\Delta\\pi$ is large, extreme baseline error renders correction underpowered rather than beneficial.\nA practical prerequisite is that the per-subgroup confusion matrix condition number $\\kappa(\\hat{C}_s)$ remain moderate; when $\\kappa > 50$, as observed here, practitioners should prioritize improving annotation quality before applying any matrix-inversion-based correction.\n\n\\section{Cross-Model Consistency}\n\\label{app:multilm}\n\nWe evaluate whether misclassification heterogeneity is model-specific by annotating 500 TweetEval sentiment tweets with six OpenAI models spanning three generations.\nSix text-feature subgroups are defined by crossing hashtag presence and text length.\nSpearman rank correlations of per-subgroup error rates across all six subgroups range from $\\rho = 0.82$ to $1.00$, indicating that the subgroup error structure is consistent across architectures.\nTwo subgroups with $n \\leq 6$ exhibit zero misclassification across all models; excluding these yields four-point correlations that are directionally consistent but underpowered.%\n\\footnote{The filtered $\\Delta\\pi$ values in Table~\\ref{tab:multilm} serve as a robustness check independent of rank-order testing: all six models exceed $\\Delta\\pi > 0.05$ on the four retained subgroups.}\n\n\\begin{table}[t]\n\\centering\n\\caption{Effective misclassification heterogeneity ($\\Delta\\pi$) across six OpenAI models on TweetEval sentiment (500 tweets, filtered to 4 subgroups with $n \\geq 10$).}\n\\label{tab:multilm}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nModel & Effective $\\Delta\\pi$ & $> 0.05$? \\\\\n\\midrule\nGPT-3.5-Turbo & 0.198 & \\checkmark \\\\\nGPT-4-Turbo & 0.149 & \\checkmark \\\\\nGPT-4o-mini & 0.136 & \\checkmark \\\\\nGPT-5.4 & 0.114 & \\checkmark \\\\\nGPT-4.1 & 0.098 & \\checkmark \\\\\nGPT-4o & 0.080 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll six models exhibit effective $\\Delta\\pi > 0.05$ on the four retained subgroups (Table~\\ref{tab:multilm}), and 5 of 6 share the same worst subgroup (\\texttt{True\\_medium}: tweets with hashtags and medium text length).\nNewer models reduce absolute error rates but do not eliminate subgroup heterogeneity: GPT-5.4 achieves $\\Delta\\pi = 0.114$ compared to GPT-3.5-Turbo's $0.198$.\nThese results were obtained with a single API provider; open-source model validation appears in Appendix~\\ref{app:multilm_opensource}.\n\n\\section{Open-Source Multi-LLM Validation}\n\\label{app:multilm_opensource}\n\nWe evaluate four open-source LLMs (7B--9B parameter range) on 490 TweetEval sentiment tweets with $K{=}4$ subgroups defined by crossing hashtag presence and text length.\nTable~\\ref{tab:multilm_cm} reports the confusion matrix heterogeneity profile.\nAll four models exhibit $\\Delta\\pi > 0.05$, confirming that subgroup-heterogeneous misclassification is not specific to proprietary APIs.\nSubgroup error rankings are consistent across architectures: \\texttt{True\\_short} (short tweets with hashtags) has the lowest $\\pi_s$ in 3 of 4 models, while \\texttt{False\\_medium} (medium tweets without hashtags) has the highest.\n\n\\begin{table}[t]\n\\centering\n\\caption{Confusion matrix heterogeneity across four open-source LLMs ($K{=}4$, $N{=}490$ TweetEval tweets). $\\Delta\\pi$: max--min per-subgroup misclassification rate. Prop.~5: number of subgroups where the $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}) triggers.}\n\\label{tab:multilm_cm}\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\nModel & Acc.\\ & $\\Delta\\pi$ & Prop.~5 & Strongest \\\\\n\\midrule\nLlama-3.1-8B & 0.755 & 0.141 & 1/4 & True\\_short \\\\\nQwen-2.5-7B & 0.798 & 0.165 & 1/4 & True\\_short \\\\\nGemma-2-9B & 0.763 & 0.125 & 4/4 & True\\_medium \\\\\nMistral-7B & 0.802 & 0.134 & 0/4 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Semi-synthetic budget sweep.}\nWe run the full EC-HTE pipeline with $K{=}2$ subgroups and $\\Delta\\tau{=}0.3$, using each model's empirical confusion matrices.\nTable~\\ref{tab:multilm_budget} reports coverage and RMSE crossover points.\nEC-HTE restores near-nominal coverage from 0.714 (naive average) to 0.939 ($+$22.5 percentage points) at $n_{\\text{expert}}{=}1{,}000$, consistent across all four models.\nGlobal correction achieves comparable or lower RMSE than HB at all budgets under these moderate $\\Delta\\pi$ values, and the $K{=}4$ RMSE crossover never occurs---confirming the budget guidelines in Appendix~\\ref{sec:budget}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-synthetic budget sweep ($K{=}2$, $\\Delta\\tau{=}0.3$, 50 MC runs; see Appendix~\\ref{app:mcse} for MC tier justification). Coverage at selected expert budgets; RMSE crossover denotes the minimum expert budget at which HB EC-HTE achieves lower RMSE than the naive (uncorrected) estimator.}\n\\label{tab:multilm_budget}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nModel & $\\Delta\\pi_{K{=}2}$ & Naive Cov.\\ & HB Cov.\\ ($n{=}1000$) & Crossover \\\\\n\\midrule\nLlama-3.1-8B & 0.051 & 0.675 & 0.940 & $n{=}1000$ \\\\\nQwen-2.5-7B & 0.080 & 0.715 & 0.925 & $n{=}1000$ \\\\\nGemma-2-9B & 0.100 & 0.705 & 0.945 & $n{=}1000$ \\\\\nMistral-7B & 0.070 & 0.760 & 0.945 & $n{=}1000$ \\\\\n\\midrule\n\\textit{Average} & --- & \\textit{0.714} & \\textit{0.939} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gemma boundary case.}\nGemma-2-9B triggers the Proposition~\\ref{prop:debiasing_hurts} diagnostic in all four $K{=}4$ subgroups due to extreme FPR--FNR asymmetry (\\texttt{False\\_medium} FNR $= 0.437$).\nAt small budgets ($K{=}4$, $n{=}100$), EC-HTE RMSE reaches 1.229 ($3.1\\times$ naive), illustrating the budget guideline from Appendix~\\ref{sec:budget}: when per-subgroup cell counts fall below 25, the variance cost of stratified correction dominates.\nAt $n \\geq 500$, EC-HTE coverage recovers to $>$0.90, consistent with the synthetic experiments.\n\n\\paragraph{Heterogeneous-$\\tau$ DGP.}\nTo assess whether the constant-$\\tau$ DGP understates EC-HTE's advantage, we run a supplementary experiment using Llama's empirical confusion matrices with heterogeneous treatment effects across subgroups ($\\Delta\\tau \\in [0.1, 0.6]$, $K{=}2$, 50 MC runs).\nEC-HTE achieves lower $|\\text{bias}|$ than global correction at all budgets ($n{=}500$: 0.010 vs.\\ 0.031, a 68\\% reduction).\nIn the high-$\\Delta\\tau$ subgroup (\\texttt{True\\_short}, $\\Delta\\tau{=}0.6$), EC-HTE also achieves lower RMSE ($n{=}1{,}000$: 0.212 vs.\\ 0.258, 18\\% improvement), confirming that the RMSE advantage concentrates in subgroups where correction is most needed.\nAggregate RMSE remains comparable to global correction because low-$\\Delta\\tau$ subgroups incur stratification variance without commensurate bias reduction, consistent with the budget guidelines in Appendix~\\ref{sec:budget}.\n\n\\section{Robustness to Subgroup Misspecification}\n\\label{app:robustness}\n\nEC-HTE requires pre-defined subgroup labels, which may be noisy in practice.\nWe test robustness by randomly flipping each observation's subgroup assignment with probability $p_{\\text{flip}} \\in \\{0, 0.10, 0.25, 0.50\\}$, across $K \\in \\{2, 4\\}$ (extreme regime, $n_{\\text{expert}} = 500$, $\\Delta\\tau = 0.3$, 100 MC runs).\n\n\\begin{table}[t]\n\\centering\n\\caption{95\\% CI coverage under subgroup misspecification noise. EC-HTE maintains near-nominal coverage across all noise levels.}\n\\label{tab:robustness}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{4}{c}{$p_{\\text{flip}}$} \\\\\n\\cmidrule(lr){2-5}\nMethod & 0.00 & 0.10 & 0.25 & 0.50 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$K{=}2$, extreme}} \\\\\n\\quad Naive & 0.875 & 0.877 & 0.890 & 0.897 \\\\\n\\quad Global & 0.925 & 0.935 & 0.932 & 0.945 \\\\\n\\quad HB EC-HTE & 0.958 & 0.948 & 0.950 & 0.945 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$K{=}4$, extreme}} \\\\\n\\quad Naive & 0.904 & 0.916 & 0.909 & 0.919 \\\\\n\\quad Global & 0.930 & 0.953 & 0.948 & 0.944 \\\\\n\\quad HB EC-HTE & 0.956 & 0.958 & 0.960 & 0.946 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains coverage $\\geq 0.945$ across all configurations (Table~\\ref{tab:robustness}), while the naive estimator is systematically below nominal (0.875--0.919).\nAt $p_{\\text{flip}} = 0.50$, subgroup structure is effectively destroyed; EC-HTE converges to global correction (coverage and RMSE within 0.1\\%), confirming that hierarchical Bayesian shrinkage provides a built-in safety mechanism.\nFor $K{=}4$ at $p_{\\text{flip}} = 0.50$, a small residual RMSE gap persists ($p < 0.01$), reflecting the variance cost of estimating four confusion matrices even when they carry no signal.\n\n\\section{Monte Carlo Standard Errors}\n\\label{app:mcse}\n\nAll main-text and most appendix experiments use 100 independent Monte Carlo replications per configuration; computationally intensive analyses (R-learner, multiplicative DGP, budget sweeps) use 50, and bootstrap experiments use 20 due to the $B{\\times}$CF cost per seed.\nThe median RMSE variation between 50-seed and 100-seed estimates is below 3.2\\%, confirming that 50-run results are stable.\nWe report Monte Carlo standard errors to assess whether observed differences between methods are statistically reliable.\nFor exp-001 (synthetic DGP, no per-seed pairing across methods), we use conservative two-sample $z$-tests on the 100-run means.\nFor exp-003 (semi-synthetic TweetEval, shared seeds across methods), we use paired $t$-tests, which are more powerful because they control for seed-level variation.\n\nTable~\\ref{tab:mcse} reports paired comparisons for representative configurations.\nOf 1{,}020 total pairwise comparisons across all configurations, 742 (72.7\\%) are statistically significant at $\\alpha = 0.05$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Paired comparisons for representative configurations. $\\Delta$ = method A $-$ method B (negative favors A for $|\\text{bias}|$). Two-sample $z$-tests for synthetic (exp-001); paired $t$-tests for semi-synthetic (exp-003). Bold $p$-values indicate significance at $\\alpha = 0.05$.}\n\\label{tab:mcse}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nConfiguration & Comparison & $\\Delta$ & $p$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Global ($|\\text{bias}|$)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $-0.046$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $-0.078$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/mod/$n{=}250$ & & $-0.017$ & $0.288$ \\\\\n\\quad TweetEval/ext/$n{=}250$ & & $+0.001$ & $0.395$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Global (RMSE)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $+0.015$ & $0.179$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $+0.048$ & $\\mathbf{0.011}$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Naive ($|\\text{bias}|$)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $-0.089$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $-0.113$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/mod/$n{=}250$ & & $-0.031$ & $\\mathbf{0.038}$ \\\\\n\\quad TweetEval/ext/$n{=}250$ & & $+0.005$ & $\\mathbf{0.030}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder extreme heterogeneity, HB EC-HTE's bias advantage over global correction is highly significant ($p < 0.001$ for both $K{=}2$ and $K{=}4$).\nThe RMSE penalty of stratification is not significant at $K{=}2$ ($p = 0.179$) but reaches significance at $K{=}4$ ($p = 0.011$), consistent with the higher variance cost of estimating four confusion matrices.\nUnder moderate heterogeneity ($K{=}4$, $n{=}250$), the bias difference between HB and global is not significant ($p = 0.288$), confirming that EC-HTE's advantage requires sufficient error heterogeneity.\nIn the semi-synthetic TweetEval experiment, HB EC-HTE does not significantly improve over global ($p = 0.395$), consistent with moderate $\\Delta\\pi$ and unbalanced subgroup sizes.\nThe HB vs.\\ naive comparison in TweetEval is significant ($p = 0.030$) but favors naive, reflecting the variance cost of stratification when bias reduction is marginal.\n\n\\section{Semi-Real Confusion Matrix Validation}\n\\label{app:semireal}\n\nWe test EC-HTE with empirical asymmetric confusion matrices from the GPT-4.1 TweetEval pilot.\nFour text-feature subgroups ($K{=}4$) retain the real per-subgroup FPR and FNR from pilot annotations (Table~\\ref{tab:semireal_cm}); CATE heterogeneity is injected synthetically ($\\tau(z{=}0,s) = 0.3 + 0.1s$, $\\tau(z{=}1,s) = 0.8 - 0.15s$).\n$N{=}5{,}000$, $P(Z{=}1){=}0.18$, 100 MC seeds per $n_{\\text{expert}}$ level.\n\n\\begin{table}[t]\n\\centering\n\\caption{Empirical confusion matrices from GPT-4.1 TweetEval pilot.\nS0 exhibits FNR $= 0.526$, approaching chance-level classification.}\n\\label{tab:semireal_cm}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSubgroup & Weight & FPR & FNR & $\\kappa(\\hat{C}_s)$ \\\\\n\\midrule\nS0 & 0.38 & 0.054 & 0.526 & high \\\\\nS1 & 0.22 & 0.101 & 0.300 & moderate \\\\\nS2 & 0.14 & 0.143 & 0.308 & moderate \\\\\nS3 & 0.25 & 0.194 & 0.222 & low \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-real confusion matrix results. RMSE and coverage averaged over subgroups and $z$-levels (100 MC runs). HB EC-HTE underperforms global at all budgets; S0's near-chance FNR drives the failure.}\n\\label{tab:semireal}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n$n_{\\text{expert}}$ & Method & RMSE $\\downarrow$ & Coverage $\\uparrow$ \\\\\n\\midrule\n\\multirow{4}{*}{100}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.263 & 0.885 \\\\\n & HB EC-HTE & 0.784 & 0.744 \\\\\n\\midrule\n\\multirow{4}{*}{250}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.232 & 0.909 \\\\\n & HB EC-HTE & 0.411 & 0.834 \\\\\n\\midrule\n\\multirow{4}{*}{500}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.196 & 0.922 \\\\\n & HB EC-HTE & 0.260 & 0.890 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHB EC-HTE produces higher RMSE and lower coverage than global correction at all expert budgets (Table~\\ref{tab:semireal}).\nThe root cause is S0's FNR $= 0.526$: when a confusion matrix row approaches a uniform distribution ($P(\\hat{Z}{=}1 \\mid Z{=}1) \\approx 0.5$), inversion amplifies estimation noise regardless of the expert budget.\nThis converges with the hate speech case study (Appendix~\\ref{app:hatespeech}, FNR $= 53.3$\\%) and confirms that EC-HTE requires \\emph{both} sufficient expert labels \\emph{and} sufficient baseline classifier quality per subgroup.\nThe singularity guard ($\\kappa > 100$, Section~\\ref{sec:method}) mitigates catastrophic failure by falling back to global correction for near-degenerate subgroups, but does not recover the bias reduction that motivates stratification.\nFor a $2 \\times 2$ symmetric confusion matrix, $\\kappa = 1/|1-2\\pi|$; $\\kappa > 100$ corresponds to $\\pi \\in (0.495, 0.505)$, so the guard triggers only when the classifier performs within $0.5\\%$ of random guessing.\nAt $n_{\\text{expert}} = 500$, HB EC-HTE narrows the gap (RMSE 0.260 vs.\\ 0.196) as confusion matrix estimates stabilize for the three well-classified subgroups, but the S0 bottleneck persists.\n\nA second semi-real experiment using GPT-3.5-Turbo confusion matrices (worst-subgroup FPR $= 0.39$, FNR $= 0.21$) yields similar results: HB RMSE exceeds global by 1.3--3.5$\\times$ at all budgets.\nHere the failure stems from high false-positive rates compounded by class imbalance ($P(Z{=}1) = 0.18$), which leaves insufficient expert observations in the positive class for reliable per-subgroup confusion matrix estimation.\nTogether, these experiments identify three applicability conditions for EC-HTE: (1)~sufficient effective expert budget ($n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$), (2)~no near-chance subgroup error rate ($\\max(\\text{FPR}_s, \\text{FNR}_s) < 0.5$), and (3)~adequate class balance in the effect modifier.\n\n\\paragraph{Diagnostic rule.}\nA logistic regression over all 368 semi-real experiment--budget cells (dependent variable: HB EC-HTE $<$ Global RMSE) identifies two sufficient statistics: the worst-subgroup confusion matrix condition number $\\kappa(\\hat{M}_s) \\leq 1.25$ and the effective minority-class expert count $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$.\nWhen both conditions hold, HB outperforms global in 93.3\\% of cells; when either is violated, global is preferred in 94.7\\% of cells.\nBoth exp-015 ($\\kappa = 2.38$, effective $n = 2.5$) and exp-016 ($\\kappa = 1.55$, effective $n = 2.5$) violate both conditions, and the diagnostic correctly predicts 100\\% of their failure cells.\nSubgroup-average metrics can mask cell-level heterogeneity: in exp-015, HB EC-HTE substantially reduces bias for the three well-classified subgroups (S1--S3) but amplifies variance in the near-degenerate subgroup (S0, FNR $= 0.526$), and the S0 penalty dominates the aggregate RMSE.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/applicability_frontier.pdf}\n\\caption{Applicability frontier of EC-HTE. Green region: EC-HTE reduces bias vs.\\ global correction. Yellow: comparable performance. Red: EC-HTE underperforms. Dashed lines mark the expert budget threshold ($n_{\\text{expert}}/K = 25$) and classifier quality threshold (worst-subgroup error rate $= 0.5$). Red diamonds show semi-real experiments with actual GPT-4.1 and GPT-3.5-Turbo confusion matrices.}\n\\label{fig:applicability}\n\\end{figure}\n\n\\section{Robustness: Estimator Choice and Treatment Effect Specification}\n\\label{app:rlearner}\n\nWe verify that EC-HTE's corrected pseudo-outcomes are compatible with downstream estimators beyond CausalForest by replacing it with the R-learner~\\citep{nie2021quasi}.\nThe experiment uses $K{=}2$, extreme heterogeneity, $n_{\\text{expert}} = 500$, and 50 MC seeds; the R-learner uses 5-fold cross-fitting with gradient-boosted trees as the base learner.\n\n\\begin{table}[t]\n\\centering\n\\caption{R-learner vs.\\ CausalForest with EC-HTE correction ($K{=}2$, extreme, $n{=}500$). $|\\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and seeds.}\n\\label{tab:rlearner}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nEstimator & Correction & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\n\\multirow{4}{*}{R-learner}\n & Oracle & 0.006 & 0.056 & 0.94 \\\\\n & Naive & 0.121 & 0.139 & 0.47 \\\\\n & Global & 0.098 & 0.123 & 0.72 \\\\\n & EC-HTE & \\textbf{0.013} & 0.080 & 0.92 \\\\\n\\midrule\n\\multirow{2}{*}{CausalForest}\n & Naive & 0.058 & 0.090 & 0.82 \\\\\n & EC-HTE & \\textbf{0.010} & 0.093 & 0.95 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE reduces R-learner $|\\text{bias}|$ by 89\\% (0.121 $\\to$ 0.013) and restores coverage from 0.47 to 0.92 (Table~\\ref{tab:rlearner}).\nThe bias reduction and coverage gains are comparable to those achieved with CausalForest, confirming that EC-HTE is compatible with a range of HTE estimators.\n\n\\paragraph{Multiplicative treatment effects.}\nWe further test robustness to the functional form of treatment effects by replacing the additive DGP with a multiplicative specification: $Y(1) = Y(0) \\times \\exp(\\tau(Z))$, using $K{=}2$, extreme heterogeneity, $n_{\\text{expert}} = 500$, and 50 MC seeds.\n\n\\begin{table}[t]\n\\centering\n\\caption{Multiplicative DGP results ($K{=}2$, extreme, $n{=}500$, 50 seeds). EC-HTE achieves comparable bias reduction and nominal coverage under non-additive treatment effects.}\n\\label{tab:multiplicative}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\nOracle & 0.003 & 0.038 & 0.96 \\\\\nNaive & 0.135 & 0.142 & 0.44 \\\\\nGlobal & 0.110 & 0.124 & 0.54 \\\\\nEC-HTE & \\textbf{0.054} & 0.068 & 0.955 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE reduces RMSE by 52\\% relative to naive (0.068 vs.\\ 0.142) and restores coverage to the nominal level (0.955; Table~\\ref{tab:multiplicative}).\nEC-HTE's bias correction operates at the confusion matrix level, independent of the downstream CATE estimator and functional form of treatment effects.\n\n\\section{Robustness to Class Imbalance}\n\\label{app:classimbalance}\n\nAssumption (A3) requires $P(Z{=}1) = 0.5$, but real-world effect modifiers are often imbalanced.\nWe sweep $P(Z{=}1) \\in \\{0.1, 0.2, 0.3, 0.4, 0.5\\}$ with $K \\in \\{2,4\\}$, extreme misclassification heterogeneity, $n_{\\text{expert}}{=}250$, and 100 MC seeds (Table~\\ref{tab:pz1_sweep}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Robustness to class imbalance ($n_{\\text{expert}}{=}250$, extreme heterogeneity). R$^2$: Theorem~\\ref{thm:bias_identity} fit. Ratio: HB/Global RMSE ($<1$ = HB wins). Cov.: HB EC-HTE 95\\% CI coverage.}\n\\label{tab:pz1_sweep}\n\\small\n\\begin{tabular}{cc ccc}\n\\toprule\n$P(Z{=}1)$ & $K$ & R$^2$ & Ratio & Cov. \\\\\n\\midrule\n0.1 & 2 & 0.998 & 0.92 & 0.94 \\\\\n0.2 & 2 & 0.989 & 0.76 & 0.94 \\\\\n0.3 & 2 & 0.994 & 0.78 & 0.94 \\\\\n0.4 & 2 & 0.995 & 0.87 & 0.94 \\\\\n0.5 & 2 & 0.995 & 0.86 & 0.93 \\\\\n\\midrule\n0.1 & 4 & 0.984 & 1.54 & 0.92 \\\\\n0.2 & 4 & 0.976 & 1.68 & 0.93 \\\\\n0.3 & 4 & 0.985 & 1.12 & 0.92 \\\\\n0.4 & 4 & 0.984 & 1.08 & 0.93 \\\\\n0.5 & 4 & 0.992 & 1.06 & 0.92 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTheorem~\\ref{thm:bias_identity}'s product form remains accurate across all imbalance levels: $R^2 \\geq 0.976$ even at $P(Z{=}1) = 0.1$, confirming that the bias identity derives from confusion matrix structure rather than class balance.\nFor $K{=}2$, EC-HTE outperforms global correction at all $P(Z{=}1)$ levels (RMSE ratio 0.76--0.92), degrading gracefully under severe imbalance.\nFor $K{=}4$, EC-HTE underperforms global at $n_{\\text{expert}}{=}250$ (ratio 1.06--1.68), consistent with the budget threshold $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$: at $P(Z{=}1){=}0.1$, $K{=}4$, each subgroup receives only ${\\sim}6$ minority-class labels.\nThe gap narrows as $P(Z{=}1)$ increases (1.54 $\\to$ 1.06), and coverage remains stable at 0.92--0.94 across all configurations.\n\n\\paragraph{Explicit form under relaxed (A3).}\nWhen $P(Z{=}0) = p_0 \\neq 0.5$, the mixing matrix $M_s$ no longer coincides with the confusion matrix $C_s$.\nBy Bayes' rule, for symmetric misclassification (A2):\n\\begin{equation}\nM_s = \\begin{bmatrix} \\frac{(1-\\pi_s) p_0}{(1-\\pi_s) p_0 + \\pi_s p_1} & \\frac{\\pi_s p_1}{(1-\\pi_s) p_0 + \\pi_s p_1} \\\\[4pt]\n\\frac{\\pi_s p_0}{\\pi_s p_0 + (1-\\pi_s) p_1} & \\frac{(1-\\pi_s) p_1}{\\pi_s p_0 + (1-\\pi_s) p_1}\n\\end{bmatrix},\n\\label{eq:ms_imbalanced}\n\\end{equation}\nwhere $p_1 = 1 - p_0$.\nThe bias identity $\\mathrm{bias}(z, s) = [(M_{\\mathrm{global}}^{-1} M_s - I) \\boldsymbol{\\tau}]_z$ holds exactly for any $p_0$ because $B_s = M_{\\mathrm{global}}^{-1} M_s - I$ satisfies $B_s \\mathbf{1} = \\mathbf{0}$ by stochasticity, so the bias reduces to $\\Delta\\tau \\cdot [B_s]_{z,1}$ regardless of class balance.\nThe class imbalance modifies $[B_s]_{z,1}$ through the Bayesian normalization in \\eqref{eq:ms_imbalanced} but preserves the product-form structure; the high $R^2$ values in Table~\\ref{tab:pz1_sweep} confirm this empirically.\n\n\\section{Comparison with PPI Correction}\n\\label{app:ppi_comparison}\n\nPPI~\\cite{angelopoulos2023ppi} constructs confidence intervals by combining a large set of ML predictions with a smaller set of gold-standard labels, using the gold labels to debias the ML-based estimator.\nApplied to our setting, PPI treats the LLM-annotated effect modifier as the ML prediction and the expert labels as the gold standard.\nTwo variants arise naturally: \\emph{PPI-global} pools all expert labels to estimate a single rectifier (analogous to our Global baseline), and \\emph{PPI-subgroup} estimates per-subgroup rectifiers (analogous to Stratified MLE).\n\nUnder the confusion-matrix parameterization we adopt, DSL's measurement error correction reduces to confusion matrix inversion.\nPooled DSL applies a single estimated confusion matrix to all subgroups, producing the same corrected label distribution as our Global baseline; per-subgroup DSL estimates a separate confusion matrix for each subgroup and inverts it independently, equivalent to our Stratified MLE.\nEC-HTE's contribution over both PPI-subgroup and per-subgroup DSL is hierarchical partial pooling: rather than estimating each subgroup's confusion matrix in isolation, EC-HTE places a shared prior across subgroups, borrowing strength to reduce variance while preserving subgroup-specific bias correction.\nThis mechanism is outside both the PPI and DSL frameworks.\n\nThe key difference between PPI and confusion-matrix inversion is that PPI does not invert the confusion matrix; instead, it uses the gold labels to directly debias the estimand.\nThis avoids the matrix inversion step that can amplify noise at small $n_{\\text{expert}}$, but it also means PPI cannot exploit the structure of the misclassification process to reduce bias.",
      "numLines": 500,
      "startLine": 500,
      "totalLines": 1630
    }
  },
  "sourceToolAssistantUUID": "aa58e9a6-7301-48dc-a0eb-71cbb0a82009",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-25T16:32:50.967Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01QDqCptW8H6CghKoTueDaBy`</summary>

```json
{
  "pattern": "\\\\section|\\\\subsection",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdb29562-597c-47f7-a8ef-3a00ebd6bfa4",
  "isSidechain": false,
  "requestId": "req_011CbPcEeTmU7i2gGd5UFjUb",
  "type": "assistant",
  "uuid": "d81ce67c-e08e-4c51-a6c4-a429feab51e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMYjfbJ1D1kP7Wyuksir86",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25426,
      "cache_read_input_tokens": 69406,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 69406,
          "cache_creation_input_tokens": 25426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25426
          },
          "type": "message"
        }
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

_source line 77 · 2026-05-25T16:32:51.033Z_

```json
{
  "parentUuid": "12c19716-d2d0-44e1-b33b-fe7efbb1f5d6",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "212cf807-76cf-417d-9760-bf50a94f82a7",
  "timestamp": "2026-05-25T16:32:51.033Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 78_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：ec_hte_llm_annotation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 30 warning 一致性检查…",
  "leafUuid": "212cf807-76cf-417d-9760-bf50a94f82a7",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP 2026 paper compliance and structure",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

### Assistant

_source line 80 · 2026-05-25T16:32:54.167Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the remaining parts of the appendix that I haven't covered.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "212cf807-76cf-417d-9760-bf50a94f82a7",
  "isSidechain": false,
  "requestId": "req_011CbPcFFNjSa24twjLviGeX",
  "type": "assistant",
  "uuid": "4857ddc1-3504-4b31-bbea-f08a40a5983a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EFQbeqxoVg739BzVABhTik",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14613,
      "cache_read_input_tokens": 94832,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14613,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 94832,
          "cache_creation_input_tokens": 14613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14613
          },
          "type": "message"
        }
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

_source line 81 · 2026-05-25T16:32:54.684Z_

Let me read the remaining parts of the appendix that I haven't seen yet.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4857ddc1-3504-4b31-bbea-f08a40a5983a",
  "isSidechain": false,
  "requestId": "req_011CbPcFFNjSa24twjLviGeX",
  "type": "assistant",
  "uuid": "0bada938-b92d-4a7a-86c1-4ac444946e84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EFQbeqxoVg739BzVABhTik",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14613,
      "cache_read_input_tokens": 94832,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14613,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 94832,
          "cache_creation_input_tokens": 14613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14613
          },
          "type": "message"
        }
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

_source line 82 · 2026-05-25T16:32:56.360Z_

<details open><summary>🔧 Tool call — Read · `toolu_015wqhi4Ggvai4CL2q5hVvkK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 1000,
  "limit": 650
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bada938-b92d-4a7a-86c1-4ac444946e84",
  "isSidechain": false,
  "requestId": "req_011CbPcFFNjSa24twjLviGeX",
  "type": "assistant",
  "uuid": "284961bd-dff8-4d81-a40b-21884cd87c13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EFQbeqxoVg739BzVABhTik",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14613,
      "cache_read_input_tokens": 94832,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14613,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 94832,
          "cache_creation_input_tokens": 14613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14613
          },
          "type": "message"
        }
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

_source line 83 · 2026-05-25T16:32:56.652Z_

<details><summary>↩ Tool result · `toolu_015wqhi4Ggvai4CL2q5hVvkK`</summary>

```text
1000	PPI-global inherits the same $\Delta\pi \times \Delta\tau$ bias amplification as Global correction (Theorem~\ref{thm:bias_identity}), confirming that the ``debiasing hurts'' mechanism operates regardless of the inference framework.
1001	
1002	\section{Civil Comments Validation}
1003	\label{app:civilcomments}
1004	
1005	To verify that subgroup-heterogeneous misclassification generalizes beyond TweetEval, we annotate $N{=}3{,}000$ stratified samples (30\% toxic) from Civil Comments~\cite{borkan2019nuanced}, a toxicity detection dataset.
1006	Subgroups are defined by \texttt{text\_length\_bin} $\times$ \texttt{has\_question} ($K{=}4$): S0 (long, no question, 38.8\%), S1 (long, question, 11.4\%), S2 (short, no question, 33.7\%), S3 (short, question, 16.1\%).
1007	Subgroup features were chosen a priori based on observable text properties; no feature search was performed.
1008	Three proprietary LLMs annotate each sample via an OpenAI-compatible API, yielding 800--900 valid annotations per model.
1009	
1010	Table~\ref{tab:civil_cm} reports per-subgroup FPR and FNR.
1011	We define $\Delta\pi = \max_s \pi_s - \min_s \pi_s$, where $\pi_s$ is the overall misclassification rate for subgroup $s$.
1012	All three models exhibit $\Delta\pi > 0.05$, with overall heterogeneity $\Delta\pi \in [0.113, 0.160]$---comparable to the $\Delta\pi \in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\ref{app:multilm_opensource}).
1013	GPT-4o-mini and GPT-3.5-turbo show pronounced FPR/FNR asymmetry (e.g., GPT-4o-mini FPR $\in [0.42, 0.61]$ vs.\ FNR $\in [0.05, 0.16]$), indicating systematic over-prediction of toxicity; their FPR approaches 0.5, placing them in the ill-conditioned regime where confusion matrix inversion amplifies noise (consistent with the classifier quality threshold discussed in the Limitations section).
1014	The consistent presence of $\Delta\pi$ heterogeneity across two NLP tasks, eight LLMs spanning open-source (7B--9B) and proprietary families, and two distinct subgroup definitions confirms that this phenomenon is a structural property of LLM annotation rather than an artifact of a specific dataset or model.
1015	
1016	\begin{table}[h]
1017	\centering
1018	\caption{Per-subgroup misclassification rates on Civil Comments ($K{=}4$). $\Delta$ denotes max $-$ min across subgroups.}
1019	\label{tab:civil_cm}
1020	\small
1021	\begin{tabular}{llccccc}
1022	\toprule
1023	Model & Metric & S0 & S1 & S2 & S3 & $\Delta$ \\
1024	\midrule
1025	GPT-4o & FPR & 0.249 & 0.157 & 0.213 & 0.341 & 0.184 \\
1026	       & FNR & 0.160 & 0.263 & 0.308 & 0.328 & 0.168 \\
1027	\midrule
1028	GPT-4o-mini & FPR & 0.517 & 0.541 & 0.419 & 0.610 & 0.191 \\
1029	            & FNR & 0.052 & 0.105 & 0.074 & 0.160 & 0.108 \\
1030	\midrule
1031	GPT-3.5-turbo & FPR & 0.400 & 0.473 & 0.374 & 0.468 & 0.099 \\
1032	              & FNR & 0.139 & 0.211 & 0.173 & 0.240 & 0.101 \\
1033	\bottomrule
1034	\end{tabular}
1035	\end{table}
1036	
1037	\section{Bias Identity Validation with Real Confusion Matrices}
1038	\label{app:realcm_bias}
1039	
1040	Theorem~\ref{thm:bias_identity} is derived under symmetric misclassification (A2); real LLM confusion matrices are asymmetric (FPR $\neq$ FNR).
1041	We verify that the generalized identity $\mathrm{bias}(z,s) = \Delta\tau \cdot [B_s]_{z,1}$ (Remark~\ref{rem:asymmetric}) holds under real annotation error structures by running semi-synthetic simulations ($N{=}5{,}000$, $K{=}4$, $\Delta\tau{=}0.30$, 100 MC runs) with confusion matrices drawn from 11 LLM--dataset combinations: eight models on TweetEval (GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, GPT-3.5-turbo, Qwen2.5-7B, Mistral-7B, Gemma-2-9B) and three on Civil Comments (GPT-4o, GPT-4o-mini, GPT-3.5-turbo).
1042	
1043	Table~\ref{tab:realcm_r2} reports per-model $R^2$ from regressing observed subgroup bias on the predicted value $\Delta\tau \cdot [B_s]_{z,1}$.
1044	The aggregate $R^2 = 0.975$; 10 of 11 combinations achieve $R^2 \geq 0.92$.
1045	The single outlier (GPT-4o-mini on Civil Comments, $R^2{=}0.76$) has near-homogeneous subgroup error rates ($\max|[B_s]_{z,1}| = 0.089$), so predicted biases are small and Monte Carlo noise dominates the regression.
1046	$R^2$ correlates strongly with $\max|[B_s]_{z,1}|$: models with more heterogeneous per-subgroup error rates produce larger bias signals that are easier to verify empirically.
1047	
1048	\begin{table}[h]
1049	\centering
1050	\caption{Bias identity $R^2$ with real LLM confusion matrices ($K{=}4$, 100 MC runs).}
1051	\label{tab:realcm_r2}
1052	\small
1053	\begin{tabular}{llcc}
1054	\toprule
1055	Model & Dataset & $R^2$ & $\max|[B_s]_{z,1}|$ \\
1056	\midrule
1057	GPT-4-turbo  & TweetEval & 0.993 & 0.328 \\
1058	Qwen2.5-7B   & TweetEval & 0.990 & 0.272 \\
1059	Mistral-7B   & TweetEval & 0.990 & 0.242 \\
1060	Gemma-2-9B   & TweetEval & 0.982 & 0.185 \\
1061	GPT-4o       & Civil Comments & 0.979 & 0.198 \\
1062	GPT-4o       & TweetEval & 0.975 & 0.240 \\
1063	GPT-4.1      & TweetEval & 0.969 & 0.139 \\
1064	GPT-3.5-turbo & TweetEval & 0.948 & 0.087 \\
1065	GPT-3.5-turbo & Civil Comments & 0.935 & 0.170 \\
1066	GPT-4o-mini  & TweetEval & 0.929 & 0.170 \\
1067	GPT-4o-mini  & Civil Comments & 0.756 & 0.089 \\
1068	\midrule
1069	\multicolumn{2}{l}{All (pooled)} & 0.975 & --- \\
1070	\bottomrule
1071	\end{tabular}
1072	\end{table}
1073	
1074	\section{Applicability Screening with Real LLM Confusion Matrices}
1075	\label{app:screening}
1076	
1077	We apply the diagnostic conditions from Proposition~\ref{prop:debiasing_hurts} and Section~\ref{sec:method} to 16 LLM--dataset--$K$ combinations spanning eight LLMs (three open-source, five proprietary) across TweetEval and Civil Comments.
1078	Table~\ref{tab:screening} summarizes which conditions each combination satisfies.
1079	
1080	\begin{table}[h]
1081	\centering
1082	\caption{Diagnostic screening of 16 LLM--dataset--$K$ combinations. Columns report whether all subgroups satisfy each condition. Budget assumes $n_{\text{expert}}{=}500$.}
1083	\label{tab:screening}
1084	\small
1085	\begin{tabular}{llccccc}
1086	\toprule
1087	Model & Dataset & $K$ & $\kappa{\leq}1.25$ & $\max{\leq}0.5$ & Budget & Pass all \\
1088	\midrule
1089	Gemma-2-9B   & TweetEval & 2 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1090	Llama-3.1-8B & TweetEval & 2 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1091	Mistral-7B   & TweetEval & 2 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1092	Qwen2.5-7B   & TweetEval & 2 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1093	Gemma-2-9B   & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1094	Llama-3.1-8B & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1095	Mistral-7B   & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1096	Qwen2.5-7B   & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1097	GPT-3.5-turbo & CivilComm. & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1098	GPT-3.5-turbo & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1099	GPT-4-turbo  & TweetEval & 4 & {\small$\times$} & {\small$\times$} & {\small$\checkmark$} & {\small$\times$} \\
1100	GPT-4.1      & TweetEval & 4 & {\small$\times$} & {\small$\times$} & {\small$\checkmark$} & {\small$\times$} \\
1101	GPT-4o       & CivilComm. & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1102	GPT-4o       & TweetEval & 4 & {\small$\times$} & {\small$\times$} & {\small$\checkmark$} & {\small$\times$} \\
1103	GPT-4o-mini  & CivilComm. & 4 & {\small$\times$} & {\small$\times$} & {\small$\checkmark$} & {\small$\times$} \\
1104	GPT-4o-mini  & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1105	\bottomrule
1106	\end{tabular}
1107	\end{table}
1108	
1109	No combination passes all three conditions; the bottleneck is $\kappa(C_s) \leq 1.25$, which requires $\mathrm{FPR}_s + \mathrm{FNR}_s \lesssim 0.20$ for all subgroups---a threshold no current LLM achieves uniformly.
1110	The closest are Qwen2.5-7B True\_short ($\kappa{=}1.23$) and Mistral-7B True\_short ($\kappa{=}1.27$).
1111	
1112	Under a relaxed ``oracle screening'' that excludes near-degenerate subgroups ($\max(\mathrm{FPR}_s, \mathrm{FNR}_s) \geq 0.4$), we run semi-synthetic CATE estimation ($N{=}5{,}000$, $\Delta\tau{=}0.3$, 100 MC runs, $n_{\text{expert}} \in \{250, 500\}$) with each LLM's real per-subgroup confusion matrix.
1113	EC-HTE (HB) achieves lower RMSE than global correction in 41 of 52 comparisons (79\%) and lower RMSE than stratified MLE in 52 of 52 comparisons (100\%).
1114	The four open-source LLMs on TweetEval show the strongest EC-HTE advantage (32/32 comparisons, RMSE reduction 0.001--0.008), while GPT-3.5-turbo/TweetEval (high FPR asymmetry, $\mathrm{FPR}_{\max}{=}0.39$) and GPT-4o/Civil Comments (low minority prevalence $P(Z{=}1){=}0.3$) show degradation.
1115	The diagnostic correctly identifies the strict applicability regime; under relaxed conditions excluding near-degenerate subgroups, EC-HTE improves RMSE in 79\% of comparisons.
1116	
1117	\paragraph{Diagnostic Applicability Analysis.}
1118	The diagnostic (Proposition~\ref{prop:debiasing_hurts}) degrades on real LLM confusion matrices (pooled AUC $= 0.63$) because the failure mode is systematic: subgroups where the true CATE heterogeneity $\tau_s \approx 0$ are hurt by global correction (since $\delta_s \neq 0$ still introduces bias), yet these subgroups produce low diagnostic scores---the diagnostic ranks them as safe precisely when they are most vulnerable to overcorrection.
1119	
1120	A simple meta-criterion recovers reliability: compute $\max_s |\delta_s| / ((1 - 2\bar{\pi}) \cdot \pi_s)$ across subgroups.
1121	When $\max_s \mathrm{score}(s) > 1$, at least one subgroup is definitively harmed by global correction, and the diagnostic achieves AUC $\geq 0.75$ across all 5 model--dataset combinations satisfying this condition (AUC range: 0.75--1.0).
1122	When $\max_s \mathrm{score}(s) \leq 1$, global correction may or may not hurt depending on unobservable $\Delta\tau$; the diagnostic achieves AUC only 0.0--0.67 across the remaining 7 combinations (4 of 7 have AUC $< 0.5$, indicating anti-prediction).
1123	This threshold perfectly separates reliable from unreliable diagnostic regimes across all 16 real LLM--dataset combinations evaluated.
1124	
1125	We recommend the following practical protocol: (i) estimate per-subgroup confusion matrices from expert labels; (ii) compute $\max_s \mathrm{score}(s)$; (iii) if $> 1$, the diagnostic reliably identifies which subgroups are harmed by global correction---apply EC-HTE; (iv) if $\leq 1$, the diagnostic is unreliable and practitioners should either default to EC-HTE as a conservative choice or evaluate correction strategies using held-out expert labels.
1126	
1127	\subsection{$\kappa$ Stratification Analysis}
1128	\label{app:kappa_analysis}
1129	
1130	The condition number $\kappa(\hat{C}_s) = 1/|1 - \mathrm{FPR}_s - \mathrm{FNR}_s|$ quantifies confusion matrix invertibility and governs the bias-variance tradeoff of per-subgroup correction.
1131	The $\kappa \leq 1.25$ threshold identified in the diagnostic rule (Section~\ref{sec:budget}) is a \emph{sufficient condition} for strongest bias reduction, not a necessary condition: EC-HTE maintains calibrated inference across a substantially wider $\kappa$ range.
1132	
1133	\paragraph{Synthetic data.}
1134	Across all 520 synthetic configurations ($K{=}2$, $\pi_s \in [0.025, 0.275]$), the maximum per-config $\kappa$ falls in $[1.43, 2.22]$; none reaches $\kappa \leq 1.25$ because the pooled rate $\bar{\pi}{=}0.15$ sets a floor of $\kappa{=}1/(1{-}2 \cdot 0.15){=}1.43$.
1135	Table~\ref{tab:kappa_synth} shows a two-bin stratification at $\kappa{=}2$: EC-HTE achieves zero analytic bias in both bins, while global correction harms at least one subgroup in 100\% of $\kappa > 2$ configurations.
1136	Monte Carlo validation ($K{=}2$, $n_{\text{expert}}{=}500$) confirms EC-HTE dominance at $\kappa{=}2.0$: 86\% bias reduction, 10\% lower RMSE, and 95.5\% coverage vs.\ 88.3\% for Global.
1137	
1138	\begin{table}[h]
1139	\centering
1140	\caption{Synthetic $\kappa$ stratification ($K{=}2$, 520 configs). ``Debiasing hurts'' = global correction increases $|\text{bias}|$ for $\geq$1 subgroup.}
1141	\label{tab:kappa_synth}
1142	\small
1143	\begin{tabular}{lcccc}
1144	\toprule
1145	$\kappa$ bin & $n$ & EC-HTE bias & Debiasing hurts & Global $|\text{bias}|/|\text{bias}_{\text{naive}}|$ \\
1146	\midrule
1147	$\leq 2.0$ & 420 & 0 (exact) & 35.0\% & 0.152 \\
1148	$> 2.0$    & 100 & 0 (exact) & 100\% & 0.326 \\
1149	\bottomrule
1150	\end{tabular}
1151	\end{table}
1152	
1153	\paragraph{Real LLM confusion matrices.}
1154	All 13 real LLM--dataset combinations ($K{=}4$) have $\kappa \in [1.88, 2.99]$---none reaches $\kappa \leq 1.25$, because no current LLM achieves $\mathrm{FPR}_s + \mathrm{FNR}_s < 0.20$ uniformly across subgroups.
1155	Table~\ref{tab:kappa_real} reports performance stratified by $\kappa$ bin and expert budget.
1156	The key finding is that EC-HTE maintains calibrated coverage ($\geq$93\%) across all $\kappa$ bins at $n_{\text{expert}} \geq 250$, compared to 86--91\% for Global.
1157	At $n_{\text{expert}}{=}500$, EC-HTE also achieves competitive RMSE in the $\kappa \leq 2$ bin (ratio 1.01) and bias win rate of 75\%; at $n_{\text{expert}}{=}250$, the variance cost of per-subgroup estimation dominates, and Global achieves lower RMSE---consistent with the bias-variance tradeoff documented in the main text (Section~\ref{sec:ec_hte_eval}).
1158	
1159	\begin{table}[h]
1160	\centering
1161	\caption{Real LLM $\kappa$ stratification ($K{=}4$, MC validation). Ratios = EC-HTE / Global; values $<1$ favor EC-HTE. Coverage is EC-HTE absolute; Global coverage ranges 0.86--0.91 across bins.}
1162	\label{tab:kappa_real}
1163	\small
1164	\begin{tabular}{llcccc}
1165	\toprule
1166	$\kappa$ bin & $n_{\text{expert}}$ & Bias ratio & RMSE ratio & Bias win & Cov.\ (EC-HTE) \\
1167	\midrule
1168	\multirow{2}{*}{$\leq 2.0$ ($n{=}4$)}
1169	 & 500 & 0.99 & 1.01 & 75\% & 0.943 \\
1170	 & 250 & 1.09 & 1.13 & 0\%  & 0.932 \\
1171	\midrule
1172	\multirow{2}{*}{$> 2.0$ ($n{=}9$)}
1173	 & 500 & 1.11 & 1.22 & 22\% & 0.949 \\
1174	 & 250 & 1.26 & 1.43 & 0\%  & 0.940 \\
1175	\bottomrule
1176	\end{tabular}
1177	\end{table}
1178	
1179	The three-tier $\kappa$ structure is thus: (i)~$\kappa > 100$: near-random classification, singularity guard triggers automatic fallback to global correction; (ii)~$\kappa \leq 1.25$: strongest theoretical regime with guaranteed bias reduction and coverage; (iii)~$\kappa \in (1.25, {\sim}3]$: the practical operating range for current LLMs, where EC-HTE provides calibrated inference (coverage $\geq$93\%) and achieves RMSE gains when expert budget is sufficient ($n_{\text{expert}} \geq 500$).
1180	
1181	\section{Plug-in Standard Error Validation}
1182	\label{app:bootstrap_se}
1183	
1184	A natural concern is whether the plug-in standard error adequately captures estimation uncertainty, particularly the additional variance introduced by confusion matrix estimation.
1185	We verify this for the difference-in-means (DIM) estimator via Monte Carlo simulation ($K{=}2$, $n_{\text{expert}} \in \{50, 100, 250, 500\}$, 50 replications per budget level).
1186	At each budget, we compute the plug-in 95\% confidence interval and record empirical coverage.
1187	Across all expert budgets, the plug-in SE yields coverage $\geq 0.96$ (0.970, 0.960, 0.970, 0.970 for $n_{\text{expert}} = 50, 100, 250, 500$), confirming that the analytic variance estimate is well-calibrated for the DIM estimator.
1188	This self-calibration arises because the same noise in $\hat{M}^{-1}$ that inflates point-estimate variance also inflates the plug-in SE, producing conservative intervals that maintain nominal coverage.
1189	
1190	\paragraph{CausalForestDML.}
1191	Under $K{=}2$ extreme heterogeneity ($\pi{=}[0.05, 0.25]$, $n_{\text{expert}}{=}250$, $n_{\text{estimators}}{=}200$, 20 MC runs), EC-HTE plug-in SE achieves 93.8\% aggregate coverage---close to the 94--96\% oracle coverage (Table~\ref{tab:cf_oracle}).
1192	The high-error subgroup ($s_1$, $\pi{=}0.25$) shows slightly lower plug-in coverage (92.5\%) than the low-error subgroup ($s_0$: 95.0\%), reflecting the larger $M^{-1}$ amplification of estimation uncertainty in subgroups with higher misclassification rates.
1193	By contrast, the DIM plug-in SE achieves $\geq$95\% coverage in the same DGP, confirming that the analytic confusion matrix propagation formula is adequate for simpler estimators.
1194	
1195	\paragraph{Full bootstrap SE.}
1196	A \emph{full} bootstrap---resampling all $N$ observations and re-estimating both the confusion matrix and CausalForest per bootstrap replicate ($B{=}100$, $n_{\text{estimators}}{=}200$, 20 MC runs)---confirms that plug-in SE is already near-nominal under standard hyperparameters.
1197	Under $K{=}2$ extreme heterogeneity ($\pi{=}[0.05, 0.25]$, $n_{\text{expert}}{=}250$), plug-in SE achieves 93.8\% aggregate coverage; the full bootstrap improves this to exactly 95.0\% ($+$1.2pp).
1198	Table~\ref{tab:bootstrap_se} reports per-subgroup results.
1199	
1200	\begin{table}[h]
1201	\centering
1202	\caption{CausalForest coverage: plug-in SE vs.\ full bootstrap SE ($B{=}100$, $n_{\text{estimators}}{=}200$, 20 MC runs). Bootstrap SE is ${\sim}1.15\times$ plug-in.}
1203	\label{tab:bootstrap_se}
1204	\small
1205	\begin{tabular}{lccccc}
1206	\toprule
1207	Subgroup & Plugin Cov. & Boot.\ Cov. & Oracle Cov. & Plugin SE & Boot.\ SE \\
1208	\midrule
1209	$s_0$ ($\pi{=}0.05$) & 0.950 & 0.925 & 0.925 & 0.059 & 0.063 \\
1210	$s_1$ ($\pi{=}0.25$) & 0.925 & \textbf{0.975} & 0.875 & 0.087 & 0.103 \\
1211	\midrule
1212	Aggregate & 0.938 & \textbf{0.950} & 0.900 & 0.073 & 0.083 \\
1213	\bottomrule
1214	\end{tabular}
1215	\end{table}
1216	
1217	The high-error subgroup ($s_1$) benefits most: coverage rises from 92.5\% to 97.5\% ($+$5.0pp), because the bootstrap captures the additional variance from $M^{-1}$ amplification.
1218	Oracle coverage (90.0\%) is consistent with the 94\% reported in the oracle decomposition (Table~\ref{tab:cf_oracle}), with the difference attributable to MC sampling noise at 20 runs.
1219	The computational cost is substantial ($B \times$ CF fits per MC run), but the approach is straightforward when exact nominal coverage is required.
1220	
1221	\paragraph{Bootstrap coverage across expert budgets.}
1222	Table~\ref{tab:bootstrap_small_n} extends the analysis to $n_{\text{expert}} \in \{25, 50, 75, 100, 200\}$ using the DIM estimator with Centered EB confusion matrix estimation ($K{=}2$ extreme, $\pi{=}[0.05, 0.25]$, 20 MC runs, $B{=}100$).
1223	Bootstrap SE maintains $\geq$95\% coverage across all expert budgets, including $n_{\text{expert}}{=}25$ (${\approx}12$ labels per subgroup).
1224	Plug-in SE is already near-nominal ($\geq$91.2\%) at all budgets tested.
1225	
1226	\begin{table}[h]
1227	\centering
1228	\caption{HB EC-HTE coverage across expert budgets: plug-in vs.\ bootstrap SE (DIM, $K{=}2$ extreme, 20 MC, $B{=}100$).}
1229	\label{tab:bootstrap_small_n}
1230	\small
1231	\begin{tabular}{lcccc}
1232	\toprule
1233	$n_{\text{expert}}$ & Plugin Cov. & Boot.\ Cov. & SE Ratio & $|\text{Bias}|$ \\
1234	\midrule
1235	25 & 0.925 & \textbf{1.000} & 2.86 & 0.079 \\
1236	50 & 0.975 & 0.988 & 2.93 & 0.067 \\
1237	75 & 0.912 & \textbf{0.975} & 2.59 & 0.065 \\
1238	100 & 0.963 & 0.963 & 1.52 & 0.060 \\
1239	200 & 0.963 & 0.950 & 1.17 & 0.061 \\
1240	\bottomrule
1241	\end{tabular}
1242	\end{table}
1243	
1244	At small $n_{\text{expert}}$, bootstrap SE inflates confidence intervals by $2{-}3\times$ relative to plug-in (SE ratio column), guaranteeing nominal coverage but reducing statistical power.
1245	At $n_{\text{expert}} \geq 100$, the SE ratio converges to ${\sim}1.2{-}1.5\times$, and plug-in SE alone achieves $\geq$96\% coverage.
1246	For practical deployment, we recommend $n_{\text{expert}} \geq 50$: bootstrap maintains nominal coverage (98.8\%) with moderate SE inflation (2.9$\times$), and plug-in SE achieves 97.5\%---close to nominal without bootstrap overhead.
1247	
1248	\paragraph{Finite-sample remainder.}
1249	By first-order matrix perturbation, $\hat{C}_s^{-1} = C_s^{-1} - C_s^{-1} E_s C_s^{-1} + O(\|E_s\|^2)$, where $E_s = \hat{C}_s - C_s$ satisfies $\|E_s\| = O_p(n_{\text{expert}}^{-1/2})$.
1250	The remainder in the corrected CATE is therefore $R_n = O_p(n_{\text{expert}}^{-1/2} \cdot \|C_s^{-1}\|^2) = O_p(n_{\text{expert}}^{-1/2} \cdot \kappa(C_s)^2)$, since $\|C_s^{-1}\| = O(\kappa(C_s))$ for stochastic matrices (where $\|C_s\| = 1$).
1251	This motivates the $\kappa > 100$ singularity guard (Section~\ref{sec:method}).
1252	
1253	\subsection{CausalForest Oracle Coverage Decomposition}
1254	\label{app:cf_oracle}
1255	
1256	To isolate the source of CausalForest under-coverage, we compare six estimation strategies that progressively remove sources of uncertainty: (1)~Oracle (true $Z$, no correction), (2)~EC-HTE with true $C_s$, (3)~EC-HTE with estimated $\hat{C}_s$ (HB), (4)~Global with true $\bar{C}$, (5)~Global with estimated $\hat{\bar{C}}$, and (6)~Naive.
1257	Table~\ref{tab:cf_oracle} reports coverage, $|\text{bias}|$, and RMSE across three DGP configurations (100 MC runs each).
1258	
1259	\begin{table}[h]
1260	\centering
1261	\caption{CausalForest oracle coverage decomposition. Coverage averaged over subgroups and $z$-levels.}
1262	\label{tab:cf_oracle}
1263	\small
1264	\begin{tabular}{ll ccc}
1265	\toprule
1266	DGP & Method & Cov.\ (\%) & $|\text{Bias}|$ & RMSE \\
1267	\midrule
1268	\multirow{6}{*}{\shortstack[l]{$K{=}4$, extreme\\$n{=}500$}}
1269	 & Oracle (true $Z$)       & 94.5 & 0.006 & 0.078 \\
1270	 & EC-HTE true $C_s$       & 92.5 & 0.008 & 0.114 \\
1271	 & EC-HTE est.\ $\hat{C}_s$ & 93.1 & 0.015 & 0.121 \\
1272	 & Global true $\bar{C}$   & 91.3 & 0.037 & 0.110 \\
1273	 & Global est.\ $\hat{\bar{C}}$ & 91.1 & 0.038 & 0.111 \\
1274	 & Naive                    & 88.3 & 0.045 & 0.095 \\
1275	\midrule
1276	\multirow{6}{*}{\shortstack[l]{$K{=}2$, extreme\\$n{=}250$}}
1277	 & Oracle (true $Z$)       & 94.0 & 0.002 & 0.056 \\
1278	 & EC-HTE true $C_s$       & 94.0 & 0.003 & 0.073 \\
1279	 & EC-HTE est.\ $\hat{C}_s$ & 92.5 & 0.004 & 0.079 \\
1280	 & Global true $\bar{C}$   & 88.5 & 0.045 & 0.083 \\
1281	 & Global est.\ $\hat{\bar{C}}$ & 88.3 & 0.045 & 0.085 \\
1282	 & Naive                    & 82.8 & 0.046 & 0.077 \\
1283	\midrule
1284	\multirow{6}{*}{\shortstack[l]{$K{=}2$, MF2 DGP\\$\tau{=}(0.10,0.40)$}}
1285	 & Oracle (true $Z$)       & 96.0 & 0.077 & 0.091 \\
1286	 & EC-HTE true $C_s$       & 91.3 & 0.103 & 0.112 \\
1287	 & EC-HTE est.\ $\hat{C}_s$ & 92.3 & 0.100 & 0.111 \\
1288	 & Global true $\bar{C}$   & 95.0 & 0.107 & 0.114 \\
1289	 & Global est.\ $\hat{\bar{C}}$ & 94.3 & 0.105 & 0.114 \\
1290	 & Naive                    & 77.3 & 0.120 & 0.125 \\
1291	\bottomrule
1292	\end{tabular}
1293	\end{table}
1294	
1295	Three findings emerge.
1296	First, oracle coverage is 94--96\% across all DGPs, confirming that CausalForest plug-in SE is well-calibrated when labels are correct.
1297	Second, EC-HTE with true $C_s$ achieves 91--94\% coverage---a 0--5pp gap from oracle (configuration-dependent), reflecting $M^{-1}$ SE propagation asymmetry across DGPs rather than confusion matrix estimation error.
1298	Third, the gap between true and estimated $C_s$ is ${\leq}$1.5pp ($K{=}2$) and $<$1pp ($K{=}4$), confirming that CM estimation uncertainty contributes negligibly at $n_{\text{expert}} \geq 250$.
1299	
1300	\section{Robustness to Assumption Violations}
1301	\label{app:a5_violation}
1302	
1303	\subsection{Assumption (A5): Subgroup-Specific Treatment Effects}
1304	
1305	\begin{corollary}[Subgroup-Specific Treatment Effect Heterogeneity]
1306	\label{cor:a5_relaxation}
1307	When $\Delta\tau$ varies across subgroups ($\Delta\tau_s = \tau_s(1) - \tau_s(0)$), the bias of global correction in subgroup $s$ at level $z{=}0$ is $+\delta_s \cdot \Delta\tau_s / (1 - 2\bar{\pi})$, and at level $z{=}1$ is $-\delta_s \cdot \Delta\tau_s / (1 - 2\bar{\pi})$.
1308	\end{corollary}
1309	The proof follows directly from Theorem~\ref{thm:bias_identity} with $\tau_s$ replacing $\tau$.
1310	
1311	Our main analysis assumes that subgroup misclassification rates $\delta_s$ and subgroup CATE magnitudes $\Delta\tau_s$ are independent (Assumption A5).
1312	In practice, both may depend on text features that define subgroups, introducing correlation.
1313	We test robustness under two configurations with the DIM estimator ($K{=}2$, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 50 MC replications, $\pi = [0.05, 0.25]$):
1314	\emph{aligned} (positive $\delta_s$--$\Delta\tau_s$ correlation: high-error S1 has the larger treatment effect, $\Delta\tau = [0.30, 0.70]$) and
1315	\emph{adversarial} (negative correlation: high-error S1 has the smaller effect, $\Delta\tau = [0.70, 0.30]$).
1316	
1317	\begin{table}[h]
1318	\centering
1319	\caption{Coverage and $|\text{bias}|$ under A5 violation ($K{=}2$, $n_{\text{expert}}{=}250$, 50 MC). Target coverage: 0.95.}
1320	\label{tab:a5_violation}
1321	\small
1322	\begin{tabular}{llcccc}
1323	\toprule
1324	Config & Method & S0 cov & S1 cov & S0 $|\text{bias}|$ & S1 $|\text{bias}|$ \\
1325	\midrule
1326	\multirow{4}{*}{Aligned}
1327	 & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\
1328	 & Naive         & 0.93 & 0.25 & 0.022 & 0.174 \\
1329	 & Global        & 0.93 & 0.82 & 0.036 & 0.094 \\
1330	 & EC-HTE (EB)   & 0.95 & 0.95 & 0.005 & 0.017 \\
1331	\midrule
1332	\multirow{4}{*}{Adversarial}
1333	 & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\
1334	 & Naive         & 0.90 & 0.78 & 0.042 & 0.074 \\
1335	 & Global        & 0.74 & 0.93 & 0.098 & 0.040 \\
1336	 & EC-HTE (EB)   & 0.94 & 0.96 & 0.002 & 0.007 \\
1337	\bottomrule
1338	\end{tabular}
1339	\end{table}
1340	
1341	In the aligned configuration, the $\delta_s \times \Delta\tau_s$ product is maximized in the high-error subgroup, causing naive S1 coverage to collapse to 0.25.
1342	Global correction improves S1 but cannot fully correct without subgroup-specific error rates.
1343	In the adversarial configuration, global correction overcorrects the low-error subgroup (S0 coverage 0.74).
1344	EC-HTE (EB) maintains $\geq 0.94$ coverage across both subgroups in both configurations, with bias comparable to the oracle.
1345	Results at $n_{\text{expert}}{=}500$ are consistent (all EC-HTE coverages $\in [0.93, 0.99]$).
1346	
1347	\paragraph{Empirical validation of Corollary~\ref{cor:aggregate_bias}.}
1348	Under the main grid (520 configurations, A5 holds), $\Delta\tau_s$ is constant across subgroups, so $\mathrm{Cov}_w(\pi_s, \Delta\tau_s) = 0$ for every configuration.
1349	The predicted aggregate bias is therefore exactly zero, and the observed aggregate bias across 100 MC runs is $< 0.003$ (residual MC noise), confirming that subgroup-level biases---which reach $|\delta_s \cdot \Delta\tau|/(1-2\bar{\pi}) = 0.071$---cancel perfectly in aggregate.
1350	This explains why aggregate metrics fail to detect global correction's bias problem.
1351	Under A5 violation, the covariance is nonzero: $\mathrm{Cov}_w(\pi_s, \Delta\tau_s) = +0.020$ (aligned) and $-0.020$ (adversarial), yielding predicted aggregate biases of $\pm 0.029$.
1352	Per-subgroup biases computed from Proposition~\ref{prop:a5_relaxation} ($\delta_s \cdot \Delta\tau_s / (1{-}2\bar{\pi})$) match the MC-observed values in Table~\ref{tab:a5_violation} (signed residuals $< 0.005$).
1353	
1354	\subsection{Assumption (A1): Sensitivity to Outcome-Dependent Misclassification}
1355	\label{app:a1_sensitivity}
1356	
1357	We assess EC-HTE's robustness when misclassification depends on potential outcomes, violating~(A1).
1358	We modify the synthetic DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$) so that misclassification probability becomes outcome-dependent: $P(\hat{Z}{\neq}Z \mid Z, S, Y) = \mathrm{clamp}(\pi_s + \gamma \cdot (Y - \mu_Y)/\sigma_Y,\, 0,\, 1)$, where $\gamma \in \{0, 0.05, 0.10, 0.15, 0.20\}$ controls the strength of violation.
1359	Table~\ref{tab:a1_sensitivity} reports results averaged over 100 MC runs.
1360	
1361	\begin{table}[h]
1362	\centering
1363	\caption{Sensitivity to Assumption~(A1) violation. Coverage and $|\text{bias}|$ under outcome-dependent misclassification ($\gamma > 0$).}
1364	\label{tab:a1_sensitivity}
1365	\small
1366	\resizebox{\columnwidth}{!}{%
1367	\begin{tabular}{lccc ccc}
1368	\toprule
1369	& \multicolumn{3}{c}{Coverage (\%)} & \multicolumn{3}{c}{$|\text{Bias}|$} \\
1370	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
1371	$\gamma$ & EC-HTE & Global & Naive & EC-HTE & Global & Naive \\
1372	\midrule
1373	0.00 & 95.5 & 92.7 & 87.7 & 0.060 & 0.065 & 0.061 \\
1374	0.05 & 95.5 & 93.5 & 83.8 & 0.059 & 0.064 & 0.064 \\
1375	0.10 & 95.3 & 93.8 & 83.5 & 0.063 & 0.064 & 0.067 \\
1376	0.15 & 94.8 & 94.3 & 79.2 & 0.065 & 0.064 & 0.070 \\
1377	0.20 & 93.5 & 94.0 & 79.5 & 0.068 & 0.063 & 0.073 \\
1378	\bottomrule
1379	\end{tabular}}
1380	\end{table}
1381	
1382	EC-HTE maintains near-nominal coverage ($\geq$93.5\%) across the full $\gamma$ range, with $|\text{bias}|$ increasing only 13.7\% from $\gamma{=}0$ to $\gamma{=}0.2$.
1383	All correction methods (Global, Stratified MLE, HB) maintain $\geq$90\% coverage, indicating that moderate (A1) violations do not catastrophically degrade confusion-matrix-based correction.
1384	The naive estimator degrades most rapidly (coverage $-$8.2pp), consistent with outcome-dependent misclassification compounding the uncorrected label noise.
1385	
1386	\subsection{Assumption (A1): Treatment-Dependent Misclassification}
1387	\label{app:treatment_dep}
1388	
1389	We extend the (A1) sensitivity analysis to the treatment-dependent case, where misclassification probability depends on treatment assignment $T$: $P(\hat{Z}{\neq}Z \mid Z, S, T) = \mathrm{clamp}(\pi_s + \gamma_T \cdot (2T - 1),\, 0,\, 1)$, with $\gamma_T \in \{0, 0.05, 0.10, 0.15, 0.20\}$.
1390	This scenario arises when LLM accuracy varies with treatment status---e.g., treated texts may be systematically harder to classify.
1391	Setup: $K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs.
1392	
1393	\begin{table}[h]
1394	\centering
1395	\caption{Sensitivity to treatment-dependent misclassification ($\gamma_T$). EC-HTE maintains $\geq$89.7\% coverage at $\gamma_T \leq 0.05$.}
1396	\label{tab:treatment_dep}
1397	\small
1398	\begin{tabular}{lcc}
1399	\toprule
1400	$\gamma_T$ & EC-HTE Coverage & EC-HTE RMSE \\
1401	\midrule
1402	0.00 & 0.945 & 0.075 \\
1403	0.05 & 0.897 & 0.092 \\
1404	0.10 & 0.750 & 0.133 \\
1405	0.15 & 0.525 & 0.177 \\
1406	0.20 & 0.370 & 0.224 \\
1407	\bottomrule
1408	\end{tabular}
1409	\end{table}
1410	
1411	EC-HTE is robust to small treatment-dependent violations ($\gamma_T \leq 0.05$), maintaining $\geq$89.7\% coverage with modest RMSE increase (0.075 to 0.092).
1412	At $\gamma_T = 0.10$, coverage drops to 75.0\%, establishing this as the approximate breakeven point.
1413	The degradation is steeper than for outcome-dependent violations (Table~\ref{tab:a1_sensitivity}), because treatment-dependent errors directly contaminate the treatment arm contrast.
1414	Figure~\ref{fig:treatment_dep} visualizes the coverage and RMSE trajectories.
1415	
1416	\begin{figure}[h]
1417	\centering
1418	\includegraphics[width=\columnwidth]{figures/treatment_dep_misclass.pdf}
1419	\caption{EC-HTE coverage and RMSE under treatment-dependent misclassification. Dashed line: 90\% coverage threshold. Breakeven at $\gamma_T \approx 0.10$.}
1420	\label{fig:treatment_dep}
1421	\end{figure}
1422	
1423	\subsection{Extension to Confounded Treatment Assignment}
1424	\label{app:confounded_dgp}
1425	
1426	EC-HTE's confusion matrix correction operates on estimated CATEs regardless of how those estimates are produced.
1427	To verify compatibility with observational (non-RCT) designs, we pair EC-HTE with an inverse probability weighted difference-in-means (IPW-DIM) estimator under confounded treatment assignment.
1428	
1429	\paragraph{DGP.}
1430	$N{=}5{,}000$, $K{=}2$, $\pi = [0.05, 0.25]$, $n_{\text{expert}}{=}250$, 100 MC replications.
1431	A covariate $X \sim \mathcal{N}(0,1)$ confounds both treatment and outcome:
1432	$T \sim \text{Bernoulli}(\sigma(\beta X))$ with $\beta{=}0.5$ (moderate confounding; propensity range $[0.38, 0.62]$),
1433	$Y = 1 + 0.5 Z + 0.3 X + \tau(Z) \cdot T + \eta$, $\eta \sim \mathcal{N}(0,1)$.
1434	Treatment effects are $\tau(Z{=}0){=}0$, $\tau(Z{=}1){=}0.3$.
1435	The IPW-DIM estimator uses \emph{oracle propensity} $e(X) = \sigma(\beta X)$, with propensity scores clipped to $[0.05, 0.95]$.
1436	
1437	\begin{table}[h]
1438	\centering
1439	\caption{EC-HTE under confounded treatment assignment (IPW-DIM with oracle propensity, $\beta{=}0.5$, 100 MC).}
1440	\label{tab:confounded_dgp}
1441	\small
1442	\begin{tabular}{lccc}
1443	\toprule
1444	Method & Coverage & RMSE & $|\text{Bias}|$ \\
1445	\midrule
1446	Oracle (true $Z$ + IPW) & 0.943 & 0.061 & 0.048 \\
1447	HB EC-HTE              & 0.950 & 0.086 & 0.068 \\
1448	Global                  & 0.930 & 0.087 & 0.071 \\
1449	Strat MLE               & 0.950 & 0.087 & 0.069 \\
1450	Naive                   & 0.863 & 0.083 & 0.066 \\
1451	\bottomrule
1452	\end{tabular}
1453	\end{table}
1454	
1455	EC-HTE achieves 95.0\% coverage, within 0.7pp of the oracle (94.3\%), confirming that confusion matrix correction and propensity weighting compose without interference.
1456	The improvement is most pronounced in the high-error subgroup ($\pi{=}0.25$): EC-HTE coverage is 96.0\% vs.\ naive 78.5\% ($+$17.5pp).
1457	Global coverage (93.0\%) falls below the correction methods (95.0\%), consistent with the cost of ignoring subgroup-level error heterogeneity even in the confounded setting.
1458	
1459	\paragraph{Sensitivity to confounding strength and propensity estimation.}
1460	We sweep $\beta \in \{0.25, 0.5, 1.0, 2.0\}$ and compare oracle propensity ($e(X) = \sigma(\beta X)$) with estimated propensity (logistic regression fit on $(X, T)$), yielding 8 configurations (100 MC each).
1461	Table~\ref{tab:confounded_sweep} reports HB EC-HTE and naive coverage.
1462	
1463	\begin{table}[h]
1464	\centering
1465	\caption{EC-HTE coverage across confounding strengths and propensity sources. The logistic regression propensity model is correctly specified; propensity misspecification is a complementary concern addressed by the IPW literature.}
1466	\label{tab:confounded_sweep}
1467	\small
1468	\begin{tabular}{cccc}
1469	\toprule
1470	$\beta$ & Propensity & HB Coverage & Naive Coverage \\
1471	\midrule
1472	0.25 & Oracle    & 0.963 & 0.848 \\
1473	0.25 & Estimated & 0.973 & 0.845 \\
1474	0.50 & Oracle    & 0.950 & 0.863 \\
1475	0.50 & Estimated & 0.958 & 0.858 \\
1476	1.00 & Oracle    & 0.958 & 0.898 \\
1477	1.00 & Estimated & 0.960 & 0.883 \\
1478	2.00 & Oracle    & 0.945 & 0.858 \\
1479	2.00 & Estimated & 0.948 & 0.858 \\
1480	\bottomrule
1481	\end{tabular}
1482	\end{table}
1483	
1484	EC-HTE maintains coverage $\geq$94.5\% across all 8 configurations, including strong confounding ($\beta{=}2.0$, propensity range $[0.12, 0.88]$).
1485	The oracle--estimated gap is $\leq$1pp, confirming that propensity estimation error does not meaningfully degrade EC-HTE when the propensity model is correctly specified.
1486	This validates that EC-HTE is robust to confounded treatment assignment when the propensity model is correctly specified.
1487	
1488	\subsection{Empirical Comparison with Frazis--Loewenstein Correction}
1489	\label{app:fl_comparison}
1490	
1491	We empirically compare EC-HTE's confusion matrix inversion against the scalar attenuation correction of \citet{frazis2003estimating} (F-L).
1492	The F-L correction rescales the observed estimate as $\hat{\tau}_{\text{FL}} = \hat{\tau}_{\text{obs}} / (1 - 2\bar{\pi})$, where $\bar{\pi}$ is the (global or per-subgroup) misclassification rate.
1493	We test two variants: F-L \emph{scalar} (single global $\bar{\pi}$) and F-L \emph{per-subgroup} ($\pi_s$-specific rescaling).
1494	Setup: $K{=}2$, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, $\pi{=}[0.05, 0.25]$ (extreme heterogeneity), $\tau(z{=}0){=}0$, $\tau(z{=}1){=}0.3$, 100 MC runs.
1495	This DGP uses smaller treatment effects ($\bar{\tau}{=}0.15$, $\Delta\tau{=}0.3$) than the main experiments (Table~\ref{tab:main_results}: $\bar{\tau}{=}0.5$), chosen to isolate the F-L comparison without conflating correction quality with treatment effect magnitude.
1496	
1497	\begin{table}[h]
1498	\centering
1499	\caption{F-L correction vs.\ EC-HTE under heterogeneous misclassification ($\Delta\pi{=}0.20$, $\bar{\tau}{=}0.15$). $|\text{Bias}|$ is unsigned and averaged across subgroups and $z$-levels; the Oracle floor (0.045) reflects finite-sample estimation noise. Both F-L variants produce \emph{higher} aggregate bias than the uncorrected estimator.}
1500	\label{tab:fl_comparison}
1501	\small
1502	\begin{tabular}{lccc}
1503	\toprule
1504	Method & $|\text{Bias}|$ & RMSE & Coverage \\
1505	\midrule
1506	Oracle         & 0.045 & 0.056 & 0.943 \\
1507	Naive          & 0.062 & 0.077 & 0.858 \\
1508	Global (CM inv)& 0.064 & 0.081 & 0.938 \\
1509	HB EC-HTE      & 0.064 & 0.086 & \textbf{0.953} \\
1510	F-L Scalar     & 0.091 & 0.116 & 0.850 \\
1511	F-L Per-Subgroup & 0.112 & 0.158 & 0.838 \\
1512	\bottomrule
1513	\end{tabular}
1514	\end{table}
1515	
1516	Both F-L variants produce \emph{higher} bias and RMSE than the naive estimator (F-L per-subgroup $|\text{bias}|{=}0.112$ vs.\ naive $0.062$), demonstrating that scalar attenuation cannot substitute for confusion matrix inversion under subgroup-heterogeneous misclassification.
1517	The per-subgroup bias direction reveals the mechanism: F-L scalar over-corrects the low-error subgroup ($s_0$: mean bias ${=}+0.073$ vs.\ naive $+0.005$, a $14.6\times$ amplification), while F-L per-subgroup dramatically over-corrects the high-error subgroup ($s_1$: mean bias ${=}+0.160$).
1518	EC-HTE achieves near-zero \emph{signed} per-subgroup bias ($s_0{:}\,{+}0.006$, $s_1{:}\,{+}0.001$) with nominal coverage (95.3\%); the aggregate unsigned $|\text{bias}|{=}0.064$ in Table~\ref{tab:fl_comparison} includes irreducible finite-sample noise (Oracle floor $= 0.045$).
1519	The root cause is structural: F-L's $1/(1{-}2\pi)$ scaling amplifies each $z$-level estimate independently, whereas CM inversion simultaneously redistributes the cross-contamination between misclassified and correctly classified observations.
1520	
1521	\subsection{End-to-End Validation with Asymmetric Confusion Matrices}
1522	\label{app:asymmetric_endtoend}
1523	
1524	We validate EC-HTE under strongly asymmetric confusion matrices ($\text{FPR}/\text{FNR}$ ratio up to $7{:}1$), simulating the error profile of GPT-4.1 on Civil Comments.
1525	Setup: $K{=}2$, $N{=}5{,}000$, $n_{\text{expert}}{=}250$; $s_0$: $\text{FPR}{=}0.05$, $\text{FNR}{=}0.02$ (low error); $s_1$: $\text{FPR}{=}0.38$, $\text{FNR}{=}0.054$ ($7{:}1$ ratio); 100 MC runs.
1526	We compare EC-HTE using the full $2{\times}2$ asymmetric CM (Remark~\ref{rem:asymmetric}) against the symmetric assumption ($\text{FPR}{=}\text{FNR}{=}\pi_s$).
1527	
1528	\begin{table}[h]
1529	\centering
1530	\caption{EC-HTE under asymmetric misclassification ($\text{FPR}/\text{FNR}$ up to $7{:}1$). The asymmetric formula improves coverage by $+1.5$pp and RMSE by $11.5\%$.}
1531	\label{tab:asymmetric_endtoend}
1532	\small
1533	\begin{tabular}{lccc}
1534	\toprule
1535	Method & $|\text{Bias}|$ & RMSE & Coverage \\
1536	\midrule
1537	Oracle              & 0.045 & 0.056 & 0.943 \\
1538	EC-HTE (asymmetric) & 0.057 & 0.074 & \textbf{0.945} \\
1539	Naive               & 0.059 & 0.073 & 0.870 \\
1540	Global (asymmetric) & 0.061 & 0.076 & 0.915 \\
1541	EC-HTE (symmetric)  & 0.062 & 0.083 & 0.930 \\
1542	Global (symmetric)  & 0.063 & 0.078 & 0.915 \\
1543	\bottomrule
1544	\end{tabular}
1545	\end{table}
1546	
1547	EC-HTE with the asymmetric formula achieves 94.5\% coverage versus 93.0\% under the symmetric assumption ($+1.5$pp), with RMSE improved from 0.083 to 0.074 ($-11.5\%$).
1548	The improvement concentrates in the high-error subgroup ($s_1$): asymmetric coverage is 93.0\% vs.\ symmetric 91.0\%.
1549	Practitioners should estimate full $2 \times 2$ confusion matrices rather than assuming symmetric misclassification, particularly when FPR and FNR differ substantially.
1550	
1551	\subsection{Complementarity with LLM Calibration}
1552	\label{app:calibration}
1553	
1554	Temperature or Platt scaling~\cite{guo2017calibration} can reduce per-subgroup misclassification rates, but does not eliminate heterogeneity $\Delta\pi$.
1555	We simulate calibration by shrinking per-subgroup rates from $\pi{=}[0.05, 0.25]$ ($\Delta\pi{=}0.20$) to $\pi{=}[0.08, 0.15]$ ($\Delta\pi{=}0.07$), testing whether EC-HTE remains necessary post-calibration.
1556	Setup: $K{=}2$, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs.
1557	
1558	\begin{table}[h]
1559	\centering
1560	\caption{Calibration reduces $\Delta\pi$ but does not eliminate it; EC-HTE corrects the residual bias. Best coverage is achieved by combining both.}
1561	\label{tab:calibration}
1562	\small
1563	\begin{tabular}{lccc}
1564	\toprule
1565	Method & $|\text{Bias}|$ & RMSE & Coverage \\
1566	\midrule
1567	Oracle                    & 0.043 & 0.053 & 0.963 \\
1568	Calibrated + EC-HTE       & 0.055 & 0.069 & \textbf{0.965} \\
1569	Calibrated + Global       & 0.055 & 0.068 & 0.963 \\
1570	Calibrated + Naive        & 0.051 & 0.064 & 0.913 \\
1571	Uncalibrated + EC-HTE     & 0.064 & 0.084 & 0.938 \\
1572	Uncalibrated + Global     & 0.069 & 0.085 & 0.920 \\
1573	Uncalibrated + Naive      & 0.063 & 0.079 & 0.840 \\
1574	\bottomrule
1575	\end{tabular}
1576	\end{table}
1577	
1578	Calibration alone improves naive coverage from 84.0\% to 91.3\% but does not reach the nominal 95\%.
1579	Calibrated + EC-HTE achieves the highest coverage (96.5\%), demonstrating that calibration and EC-HTE address complementary error sources: calibration reduces per-subgroup $\pi_s$ while EC-HTE corrects the residual $\delta_s$-driven bias from heterogeneity that persists post-calibration.
1580	Propensity estimation robustness under model misspecification is a complementary concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior.
1581	
1582	\subsection{Policy Reversal Zone Analysis}
1583	\label{app:policy_reversal}
1584	
1585	When the true treatment effect is small, global correction can reverse the sign of estimated CATE---concluding a beneficial treatment is harmful---creating a \emph{policy reversal zone}.
1586	We sweep $\tau(0) \in \{0.01, 0.02, 0.03, 0.05, 0.07, 0.10\}$ under the standard DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs; $\Delta\tau{=}0.30$).
1587	
1588	\begin{table}[h]
1589	\centering
1590	\caption{Policy reversal zone: fraction of configurations where global correction reverses the sign of estimated CATE.
1591	The naive estimator produces zero sign reversals across all $\tau(0)$ values; EC-HTE also achieves 0\% reversal.}
1592	\label{tab:policy_reversal}
1593	\small
1594	\begin{tabular}{ccc}
1595	\toprule
1596	$\tau(0)$ & Global reversal \% & Most extreme $\hat{\tau}_{\text{global}}$ \\
1597	\midrule
1598	0.01 & 31.0 & $-0.079$ \\
1599	0.02 & 21.6 & --- \\
1600	0.03 & 14.9 & $-0.059$ \\
1601	0.05 & 6.1  & $-0.039$ \\
1602	0.07 & 1.6  & --- \\
1603	$\geq$0.10 & 0 & --- \\
1604	\bottomrule
1605	\end{tabular}
1606	\end{table}
1607	
1608	The reversal rate increases monotonically as $\tau(0)$ decreases: at $\tau(0) = 0.01$, 31\% of configurations yield sign reversal, with the most extreme case estimating $\hat{\tau} = -0.079$ when the true effect is $\tau = +0.01$.
1609	The critical threshold is $\tau(0) < 0.089$, matching the closed-form prediction from Theorem~\ref{thm:bias_identity}: $|\delta_{\max} \cdot \Delta\tau_{\max}| / (1 - 2\bar{\pi}) = 0.125 \times 0.50 / 0.70 = 0.089$.
1610	The most dangerous combination ($\tau(0) = 0.01$, $\delta_{\text{misclass}} = 0.19$) reaches 42.9\% reversal rate.
1611	The naive estimator produces zero sign reversals across all $\tau(0)$ values, confirming that reversal is an artifact of global correction, not inherent estimation noise.
1612	
1613	Figure~\ref{fig:policy_reversal} visualizes the reversal zone across the $\Delta\pi \times \tau(0)$ parameter space.
1614	
1615	\begin{figure}[h]
1616	\centering
1617	\includegraphics[width=\columnwidth]{figures/policy_reversal_zone.pdf}
1618	\caption{Policy reversal zone: sign-reversal rate as a function of $\tau(0)$ and $\Delta\pi$. Shaded region marks configurations where global correction reverses the CATE sign, directing policy toward the wrong subgroups.}
1619	\label{fig:policy_reversal}
1620	\end{figure}
1621	
1622	\input{appendix_stance}
1623	
1624	\input{appendix_agnews}
1625	
1626	\section*{Use of AI Assistants}
1627	\label{app:ai-assistants}
1628	
1629	The authors used AI-based writing assistants, including Claude, for limited support during manuscript preparation, including grammar polishing, wording suggestions, LaTeX editing, and code/debugging assistance. The tools were not used to generate the core research ideas, experimental design, methodological decisions, data analysis, or scientific conclusions. All AI-assisted text, code suggestions, and references were manually reviewed and edited by the authors.
1630	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "284961bd-dff8-4d81-a40b-21884cd87c13",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "eeeb42db-891a-496e-a168-b13bc506157f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
      "content": "PPI-global inherits the same $\\Delta\\pi \\times \\Delta\\tau$ bias amplification as Global correction (Theorem~\\ref{thm:bias_identity}), confirming that the ``debiasing hurts'' mechanism operates regardless of the inference framework.\n\n\\section{Civil Comments Validation}\n\\label{app:civilcomments}\n\nTo verify that subgroup-heterogeneous misclassification generalizes beyond TweetEval, we annotate $N{=}3{,}000$ stratified samples (30\\% toxic) from Civil Comments~\\cite{borkan2019nuanced}, a toxicity detection dataset.\nSubgroups are defined by \\texttt{text\\_length\\_bin} $\\times$ \\texttt{has\\_question} ($K{=}4$): S0 (long, no question, 38.8\\%), S1 (long, question, 11.4\\%), S2 (short, no question, 33.7\\%), S3 (short, question, 16.1\\%).\nSubgroup features were chosen a priori based on observable text properties; no feature search was performed.\nThree proprietary LLMs annotate each sample via an OpenAI-compatible API, yielding 800--900 valid annotations per model.\n\nTable~\\ref{tab:civil_cm} reports per-subgroup FPR and FNR.\nWe define $\\Delta\\pi = \\max_s \\pi_s - \\min_s \\pi_s$, where $\\pi_s$ is the overall misclassification rate for subgroup $s$.\nAll three models exhibit $\\Delta\\pi > 0.05$, with overall heterogeneity $\\Delta\\pi \\in [0.113, 0.160]$---comparable to the $\\Delta\\pi \\in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\\ref{app:multilm_opensource}).\nGPT-4o-mini and GPT-3.5-turbo show pronounced FPR/FNR asymmetry (e.g., GPT-4o-mini FPR $\\in [0.42, 0.61]$ vs.\\ FNR $\\in [0.05, 0.16]$), indicating systematic over-prediction of toxicity; their FPR approaches 0.5, placing them in the ill-conditioned regime where confusion matrix inversion amplifies noise (consistent with the classifier quality threshold discussed in the Limitations section).\nThe consistent presence of $\\Delta\\pi$ heterogeneity across two NLP tasks, eight LLMs spanning open-source (7B--9B) and proprietary families, and two distinct subgroup definitions confirms that this phenomenon is a structural property of LLM annotation rather than an artifact of a specific dataset or model.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-subgroup misclassification rates on Civil Comments ($K{=}4$). $\\Delta$ denotes max $-$ min across subgroups.}\n\\label{tab:civil_cm}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Metric & S0 & S1 & S2 & S3 & $\\Delta$ \\\\\n\\midrule\nGPT-4o & FPR & 0.249 & 0.157 & 0.213 & 0.341 & 0.184 \\\\\n       & FNR & 0.160 & 0.263 & 0.308 & 0.328 & 0.168 \\\\\n\\midrule\nGPT-4o-mini & FPR & 0.517 & 0.541 & 0.419 & 0.610 & 0.191 \\\\\n            & FNR & 0.052 & 0.105 & 0.074 & 0.160 & 0.108 \\\\\n\\midrule\nGPT-3.5-turbo & FPR & 0.400 & 0.473 & 0.374 & 0.468 & 0.099 \\\\\n              & FNR & 0.139 & 0.211 & 0.173 & 0.240 & 0.101 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Bias Identity Validation with Real Confusion Matrices}\n\\label{app:realcm_bias}\n\nTheorem~\\ref{thm:bias_identity} is derived under symmetric misclassification (A2); real LLM confusion matrices are asymmetric (FPR $\\neq$ FNR).\nWe verify that the generalized identity $\\mathrm{bias}(z,s) = \\Delta\\tau \\cdot [B_s]_{z,1}$ (Remark~\\ref{rem:asymmetric}) holds under real annotation error structures by running semi-synthetic simulations ($N{=}5{,}000$, $K{=}4$, $\\Delta\\tau{=}0.30$, 100 MC runs) with confusion matrices drawn from 11 LLM--dataset combinations: eight models on TweetEval (GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, GPT-3.5-turbo, Qwen2.5-7B, Mistral-7B, Gemma-2-9B) and three on Civil Comments (GPT-4o, GPT-4o-mini, GPT-3.5-turbo).\n\nTable~\\ref{tab:realcm_r2} reports per-model $R^2$ from regressing observed subgroup bias on the predicted value $\\Delta\\tau \\cdot [B_s]_{z,1}$.\nThe aggregate $R^2 = 0.975$; 10 of 11 combinations achieve $R^2 \\geq 0.92$.\nThe single outlier (GPT-4o-mini on Civil Comments, $R^2{=}0.76$) has near-homogeneous subgroup error rates ($\\max|[B_s]_{z,1}| = 0.089$), so predicted biases are small and Monte Carlo noise dominates the regression.\n$R^2$ correlates strongly with $\\max|[B_s]_{z,1}|$: models with more heterogeneous per-subgroup error rates produce larger bias signals that are easier to verify empirically.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bias identity $R^2$ with real LLM confusion matrices ($K{=}4$, 100 MC runs).}\n\\label{tab:realcm_r2}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nModel & Dataset & $R^2$ & $\\max|[B_s]_{z,1}|$ \\\\\n\\midrule\nGPT-4-turbo  & TweetEval & 0.993 & 0.328 \\\\\nQwen2.5-7B   & TweetEval & 0.990 & 0.272 \\\\\nMistral-7B   & TweetEval & 0.990 & 0.242 \\\\\nGemma-2-9B   & TweetEval & 0.982 & 0.185 \\\\\nGPT-4o       & Civil Comments & 0.979 & 0.198 \\\\\nGPT-4o       & TweetEval & 0.975 & 0.240 \\\\\nGPT-4.1      & TweetEval & 0.969 & 0.139 \\\\\nGPT-3.5-turbo & TweetEval & 0.948 & 0.087 \\\\\nGPT-3.5-turbo & Civil Comments & 0.935 & 0.170 \\\\\nGPT-4o-mini  & TweetEval & 0.929 & 0.170 \\\\\nGPT-4o-mini  & Civil Comments & 0.756 & 0.089 \\\\\n\\midrule\n\\multicolumn{2}{l}{All (pooled)} & 0.975 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Applicability Screening with Real LLM Confusion Matrices}\n\\label{app:screening}\n\nWe apply the diagnostic conditions from Proposition~\\ref{prop:debiasing_hurts} and Section~\\ref{sec:method} to 16 LLM--dataset--$K$ combinations spanning eight LLMs (three open-source, five proprietary) across TweetEval and Civil Comments.\nTable~\\ref{tab:screening} summarizes which conditions each combination satisfies.\n\n\\begin{table}[h]\n\\centering\n\\caption{Diagnostic screening of 16 LLM--dataset--$K$ combinations. Columns report whether all subgroups satisfy each condition. Budget assumes $n_{\\text{expert}}{=}500$.}\n\\label{tab:screening}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Dataset & $K$ & $\\kappa{\\leq}1.25$ & $\\max{\\leq}0.5$ & Budget & Pass all \\\\\n\\midrule\nGemma-2-9B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nLlama-3.1-8B & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nMistral-7B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nQwen2.5-7B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGemma-2-9B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nLlama-3.1-8B & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nMistral-7B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nQwen2.5-7B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-3.5-turbo & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-3.5-turbo & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4-turbo  & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4.1      & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o       & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o       & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o-mini  & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o-mini  & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNo combination passes all three conditions; the bottleneck is $\\kappa(C_s) \\leq 1.25$, which requires $\\mathrm{FPR}_s + \\mathrm{FNR}_s \\lesssim 0.20$ for all subgroups---a threshold no current LLM achieves uniformly.\nThe closest are Qwen2.5-7B True\\_short ($\\kappa{=}1.23$) and Mistral-7B True\\_short ($\\kappa{=}1.27$).\n\nUnder a relaxed ``oracle screening'' that excludes near-degenerate subgroups ($\\max(\\mathrm{FPR}_s, \\mathrm{FNR}_s) \\geq 0.4$), we run semi-synthetic CATE estimation ($N{=}5{,}000$, $\\Delta\\tau{=}0.3$, 100 MC runs, $n_{\\text{expert}} \\in \\{250, 500\\}$) with each LLM's real per-subgroup confusion matrix.\nEC-HTE (HB) achieves lower RMSE than global correction in 41 of 52 comparisons (79\\%) and lower RMSE than stratified MLE in 52 of 52 comparisons (100\\%).\nThe four open-source LLMs on TweetEval show the strongest EC-HTE advantage (32/32 comparisons, RMSE reduction 0.001--0.008), while GPT-3.5-turbo/TweetEval (high FPR asymmetry, $\\mathrm{FPR}_{\\max}{=}0.39$) and GPT-4o/Civil Comments (low minority prevalence $P(Z{=}1){=}0.3$) show degradation.\nThe diagnostic correctly identifies the strict applicability regime; under relaxed conditions excluding near-degenerate subgroups, EC-HTE improves RMSE in 79\\% of comparisons.\n\n\\paragraph{Diagnostic Applicability Analysis.}\nThe diagnostic (Proposition~\\ref{prop:debiasing_hurts}) degrades on real LLM confusion matrices (pooled AUC $= 0.63$) because the failure mode is systematic: subgroups where the true CATE heterogeneity $\\tau_s \\approx 0$ are hurt by global correction (since $\\delta_s \\neq 0$ still introduces bias), yet these subgroups produce low diagnostic scores---the diagnostic ranks them as safe precisely when they are most vulnerable to overcorrection.\n\nA simple meta-criterion recovers reliability: compute $\\max_s |\\delta_s| / ((1 - 2\\bar{\\pi}) \\cdot \\pi_s)$ across subgroups.\nWhen $\\max_s \\mathrm{score}(s) > 1$, at least one subgroup is definitively harmed by global correction, and the diagnostic achieves AUC $\\geq 0.75$ across all 5 model--dataset combinations satisfying this condition (AUC range: 0.75--1.0).\nWhen $\\max_s \\mathrm{score}(s) \\leq 1$, global correction may or may not hurt depending on unobservable $\\Delta\\tau$; the diagnostic achieves AUC only 0.0--0.67 across the remaining 7 combinations (4 of 7 have AUC $< 0.5$, indicating anti-prediction).\nThis threshold perfectly separates reliable from unreliable diagnostic regimes across all 16 real LLM--dataset combinations evaluated.\n\nWe recommend the following practical protocol: (i) estimate per-subgroup confusion matrices from expert labels; (ii) compute $\\max_s \\mathrm{score}(s)$; (iii) if $> 1$, the diagnostic reliably identifies which subgroups are harmed by global correction---apply EC-HTE; (iv) if $\\leq 1$, the diagnostic is unreliable and practitioners should either default to EC-HTE as a conservative choice or evaluate correction strategies using held-out expert labels.\n\n\\subsection{$\\kappa$ Stratification Analysis}\n\\label{app:kappa_analysis}\n\nThe condition number $\\kappa(\\hat{C}_s) = 1/|1 - \\mathrm{FPR}_s - \\mathrm{FNR}_s|$ quantifies confusion matrix invertibility and governs the bias-variance tradeoff of per-subgroup correction.\nThe $\\kappa \\leq 1.25$ threshold identified in the diagnostic rule (Section~\\ref{sec:budget}) is a \\emph{sufficient condition} for strongest bias reduction, not a necessary condition: EC-HTE maintains calibrated inference across a substantially wider $\\kappa$ range.\n\n\\paragraph{Synthetic data.}\nAcross all 520 synthetic configurations ($K{=}2$, $\\pi_s \\in [0.025, 0.275]$), the maximum per-config $\\kappa$ falls in $[1.43, 2.22]$; none reaches $\\kappa \\leq 1.25$ because the pooled rate $\\bar{\\pi}{=}0.15$ sets a floor of $\\kappa{=}1/(1{-}2 \\cdot 0.15){=}1.43$.\nTable~\\ref{tab:kappa_synth} shows a two-bin stratification at $\\kappa{=}2$: EC-HTE achieves zero analytic bias in both bins, while global correction harms at least one subgroup in 100\\% of $\\kappa > 2$ configurations.\nMonte Carlo validation ($K{=}2$, $n_{\\text{expert}}{=}500$) confirms EC-HTE dominance at $\\kappa{=}2.0$: 86\\% bias reduction, 10\\% lower RMSE, and 95.5\\% coverage vs.\\ 88.3\\% for Global.\n\n\\begin{table}[h]\n\\centering\n\\caption{Synthetic $\\kappa$ stratification ($K{=}2$, 520 configs). ``Debiasing hurts'' = global correction increases $|\\text{bias}|$ for $\\geq$1 subgroup.}\n\\label{tab:kappa_synth}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\kappa$ bin & $n$ & EC-HTE bias & Debiasing hurts & Global $|\\text{bias}|/|\\text{bias}_{\\text{naive}}|$ \\\\\n\\midrule\n$\\leq 2.0$ & 420 & 0 (exact) & 35.0\\% & 0.152 \\\\\n$> 2.0$    & 100 & 0 (exact) & 100\\% & 0.326 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Real LLM confusion matrices.}\nAll 13 real LLM--dataset combinations ($K{=}4$) have $\\kappa \\in [1.88, 2.99]$---none reaches $\\kappa \\leq 1.25$, because no current LLM achieves $\\mathrm{FPR}_s + \\mathrm{FNR}_s < 0.20$ uniformly across subgroups.\nTable~\\ref{tab:kappa_real} reports performance stratified by $\\kappa$ bin and expert budget.\nThe key finding is that EC-HTE maintains calibrated coverage ($\\geq$93\\%) across all $\\kappa$ bins at $n_{\\text{expert}} \\geq 250$, compared to 86--91\\% for Global.\nAt $n_{\\text{expert}}{=}500$, EC-HTE also achieves competitive RMSE in the $\\kappa \\leq 2$ bin (ratio 1.01) and bias win rate of 75\\%; at $n_{\\text{expert}}{=}250$, the variance cost of per-subgroup estimation dominates, and Global achieves lower RMSE---consistent with the bias-variance tradeoff documented in the main text (Section~\\ref{sec:ec_hte_eval}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Real LLM $\\kappa$ stratification ($K{=}4$, MC validation). Ratios = EC-HTE / Global; values $<1$ favor EC-HTE. Coverage is EC-HTE absolute; Global coverage ranges 0.86--0.91 across bins.}\n\\label{tab:kappa_real}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n$\\kappa$ bin & $n_{\\text{expert}}$ & Bias ratio & RMSE ratio & Bias win & Cov.\\ (EC-HTE) \\\\\n\\midrule\n\\multirow{2}{*}{$\\leq 2.0$ ($n{=}4$)}\n & 500 & 0.99 & 1.01 & 75\\% & 0.943 \\\\\n & 250 & 1.09 & 1.13 & 0\\%  & 0.932 \\\\\n\\midrule\n\\multirow{2}{*}{$> 2.0$ ($n{=}9$)}\n & 500 & 1.11 & 1.22 & 22\\% & 0.949 \\\\\n & 250 & 1.26 & 1.43 & 0\\%  & 0.940 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe three-tier $\\kappa$ structure is thus: (i)~$\\kappa > 100$: near-random classification, singularity guard triggers automatic fallback to global correction; (ii)~$\\kappa \\leq 1.25$: strongest theoretical regime with guaranteed bias reduction and coverage; (iii)~$\\kappa \\in (1.25, {\\sim}3]$: the practical operating range for current LLMs, where EC-HTE provides calibrated inference (coverage $\\geq$93\\%) and achieves RMSE gains when expert budget is sufficient ($n_{\\text{expert}} \\geq 500$).\n\n\\section{Plug-in Standard Error Validation}\n\\label{app:bootstrap_se}\n\nA natural concern is whether the plug-in standard error adequately captures estimation uncertainty, particularly the additional variance introduced by confusion matrix estimation.\nWe verify this for the difference-in-means (DIM) estimator via Monte Carlo simulation ($K{=}2$, $n_{\\text{expert}} \\in \\{50, 100, 250, 500\\}$, 50 replications per budget level).\nAt each budget, we compute the plug-in 95\\% confidence interval and record empirical coverage.\nAcross all expert budgets, the plug-in SE yields coverage $\\geq 0.96$ (0.970, 0.960, 0.970, 0.970 for $n_{\\text{expert}} = 50, 100, 250, 500$), confirming that the analytic variance estimate is well-calibrated for the DIM estimator.\nThis self-calibration arises because the same noise in $\\hat{M}^{-1}$ that inflates point-estimate variance also inflates the plug-in SE, producing conservative intervals that maintain nominal coverage.\n\n\\paragraph{CausalForestDML.}\nUnder $K{=}2$ extreme heterogeneity ($\\pi{=}[0.05, 0.25]$, $n_{\\text{expert}}{=}250$, $n_{\\text{estimators}}{=}200$, 20 MC runs), EC-HTE plug-in SE achieves 93.8\\% aggregate coverage---close to the 94--96\\% oracle coverage (Table~\\ref{tab:cf_oracle}).\nThe high-error subgroup ($s_1$, $\\pi{=}0.25$) shows slightly lower plug-in coverage (92.5\\%) than the low-error subgroup ($s_0$: 95.0\\%), reflecting the larger $M^{-1}$ amplification of estimation uncertainty in subgroups with higher misclassification rates.\nBy contrast, the DIM plug-in SE achieves $\\geq$95\\% coverage in the same DGP, confirming that the analytic confusion matrix propagation formula is adequate for simpler estimators.\n\n\\paragraph{Full bootstrap SE.}\nA \\emph{full} bootstrap---resampling all $N$ observations and re-estimating both the confusion matrix and CausalForest per bootstrap replicate ($B{=}100$, $n_{\\text{estimators}}{=}200$, 20 MC runs)---confirms that plug-in SE is already near-nominal under standard hyperparameters.\nUnder $K{=}2$ extreme heterogeneity ($\\pi{=}[0.05, 0.25]$, $n_{\\text{expert}}{=}250$), plug-in SE achieves 93.8\\% aggregate coverage; the full bootstrap improves this to exactly 95.0\\% ($+$1.2pp).\nTable~\\ref{tab:bootstrap_se} reports per-subgroup results.\n\n\\begin{table}[h]\n\\centering\n\\caption{CausalForest coverage: plug-in SE vs.\\ full bootstrap SE ($B{=}100$, $n_{\\text{estimators}}{=}200$, 20 MC runs). Bootstrap SE is ${\\sim}1.15\\times$ plug-in.}\n\\label{tab:bootstrap_se}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nSubgroup & Plugin Cov. & Boot.\\ Cov. & Oracle Cov. & Plugin SE & Boot.\\ SE \\\\\n\\midrule\n$s_0$ ($\\pi{=}0.05$) & 0.950 & 0.925 & 0.925 & 0.059 & 0.063 \\\\\n$s_1$ ($\\pi{=}0.25$) & 0.925 & \\textbf{0.975} & 0.875 & 0.087 & 0.103 \\\\\n\\midrule\nAggregate & 0.938 & \\textbf{0.950} & 0.900 & 0.073 & 0.083 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe high-error subgroup ($s_1$) benefits most: coverage rises from 92.5\\% to 97.5\\% ($+$5.0pp), because the bootstrap captures the additional variance from $M^{-1}$ amplification.\nOracle coverage (90.0\\%) is consistent with the 94\\% reported in the oracle decomposition (Table~\\ref{tab:cf_oracle}), with the difference attributable to MC sampling noise at 20 runs.\nThe computational cost is substantial ($B \\times$ CF fits per MC run), but the approach is straightforward when exact nominal coverage is required.\n\n\\paragraph{Bootstrap coverage across expert budgets.}\nTable~\\ref{tab:bootstrap_small_n} extends the analysis to $n_{\\text{expert}} \\in \\{25, 50, 75, 100, 200\\}$ using the DIM estimator with Centered EB confusion matrix estimation ($K{=}2$ extreme, $\\pi{=}[0.05, 0.25]$, 20 MC runs, $B{=}100$).\nBootstrap SE maintains $\\geq$95\\% coverage across all expert budgets, including $n_{\\text{expert}}{=}25$ (${\\approx}12$ labels per subgroup).\nPlug-in SE is already near-nominal ($\\geq$91.2\\%) at all budgets tested.\n\n\\begin{table}[h]\n\\centering\n\\caption{HB EC-HTE coverage across expert budgets: plug-in vs.\\ bootstrap SE (DIM, $K{=}2$ extreme, 20 MC, $B{=}100$).}\n\\label{tab:bootstrap_small_n}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$n_{\\text{expert}}$ & Plugin Cov. & Boot.\\ Cov. & SE Ratio & $|\\text{Bias}|$ \\\\\n\\midrule\n25 & 0.925 & \\textbf{1.000} & 2.86 & 0.079 \\\\\n50 & 0.975 & 0.988 & 2.93 & 0.067 \\\\\n75 & 0.912 & \\textbf{0.975} & 2.59 & 0.065 \\\\\n100 & 0.963 & 0.963 & 1.52 & 0.060 \\\\\n200 & 0.963 & 0.950 & 1.17 & 0.061 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt small $n_{\\text{expert}}$, bootstrap SE inflates confidence intervals by $2{-}3\\times$ relative to plug-in (SE ratio column), guaranteeing nominal coverage but reducing statistical power.\nAt $n_{\\text{expert}} \\geq 100$, the SE ratio converges to ${\\sim}1.2{-}1.5\\times$, and plug-in SE alone achieves $\\geq$96\\% coverage.\nFor practical deployment, we recommend $n_{\\text{expert}} \\geq 50$: bootstrap maintains nominal coverage (98.8\\%) with moderate SE inflation (2.9$\\times$), and plug-in SE achieves 97.5\\%---close to nominal without bootstrap overhead.\n\n\\paragraph{Finite-sample remainder.}\nBy first-order matrix perturbation, $\\hat{C}_s^{-1} = C_s^{-1} - C_s^{-1} E_s C_s^{-1} + O(\\|E_s\\|^2)$, where $E_s = \\hat{C}_s - C_s$ satisfies $\\|E_s\\| = O_p(n_{\\text{expert}}^{-1/2})$.\nThe remainder in the corrected CATE is therefore $R_n = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\|C_s^{-1}\\|^2) = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\kappa(C_s)^2)$, since $\\|C_s^{-1}\\| = O(\\kappa(C_s))$ for stochastic matrices (where $\\|C_s\\| = 1$).\nThis motivates the $\\kappa > 100$ singularity guard (Section~\\ref{sec:method}).\n\n\\subsection{CausalForest Oracle Coverage Decomposition}\n\\label{app:cf_oracle}\n\nTo isolate the source of CausalForest under-coverage, we compare six estimation strategies that progressively remove sources of uncertainty: (1)~Oracle (true $Z$, no correction), (2)~EC-HTE with true $C_s$, (3)~EC-HTE with estimated $\\hat{C}_s$ (HB), (4)~Global with true $\\bar{C}$, (5)~Global with estimated $\\hat{\\bar{C}}$, and (6)~Naive.\nTable~\\ref{tab:cf_oracle} reports coverage, $|\\text{bias}|$, and RMSE across three DGP configurations (100 MC runs each).\n\n\\begin{table}[h]\n\\centering\n\\caption{CausalForest oracle coverage decomposition. Coverage averaged over subgroups and $z$-levels.}\n\\label{tab:cf_oracle}\n\\small\n\\begin{tabular}{ll ccc}\n\\toprule\nDGP & Method & Cov.\\ (\\%) & $|\\text{Bias}|$ & RMSE \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}4$, extreme\\\\$n{=}500$}}\n & Oracle (true $Z$)       & 94.5 & 0.006 & 0.078 \\\\\n & EC-HTE true $C_s$       & 92.5 & 0.008 & 0.114 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 93.1 & 0.015 & 0.121 \\\\\n & Global true $\\bar{C}$   & 91.3 & 0.037 & 0.110 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 91.1 & 0.038 & 0.111 \\\\\n & Naive                    & 88.3 & 0.045 & 0.095 \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}2$, extreme\\\\$n{=}250$}}\n & Oracle (true $Z$)       & 94.0 & 0.002 & 0.056 \\\\\n & EC-HTE true $C_s$       & 94.0 & 0.003 & 0.073 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 92.5 & 0.004 & 0.079 \\\\\n & Global true $\\bar{C}$   & 88.5 & 0.045 & 0.083 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 88.3 & 0.045 & 0.085 \\\\\n & Naive                    & 82.8 & 0.046 & 0.077 \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}2$, MF2 DGP\\\\$\\tau{=}(0.10,0.40)$}}\n & Oracle (true $Z$)       & 96.0 & 0.077 & 0.091 \\\\\n & EC-HTE true $C_s$       & 91.3 & 0.103 & 0.112 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 92.3 & 0.100 & 0.111 \\\\\n & Global true $\\bar{C}$   & 95.0 & 0.107 & 0.114 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 94.3 & 0.105 & 0.114 \\\\\n & Naive                    & 77.3 & 0.120 & 0.125 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree findings emerge.\nFirst, oracle coverage is 94--96\\% across all DGPs, confirming that CausalForest plug-in SE is well-calibrated when labels are correct.\nSecond, EC-HTE with true $C_s$ achieves 91--94\\% coverage---a 0--5pp gap from oracle (configuration-dependent), reflecting $M^{-1}$ SE propagation asymmetry across DGPs rather than confusion matrix estimation error.\nThird, the gap between true and estimated $C_s$ is ${\\leq}$1.5pp ($K{=}2$) and $<$1pp ($K{=}4$), confirming that CM estimation uncertainty contributes negligibly at $n_{\\text{expert}} \\geq 250$.\n\n\\section{Robustness to Assumption Violations}\n\\label{app:a5_violation}\n\n\\subsection{Assumption (A5): Subgroup-Specific Treatment Effects}\n\n\\begin{corollary}[Subgroup-Specific Treatment Effect Heterogeneity]\n\\label{cor:a5_relaxation}\nWhen $\\Delta\\tau$ varies across subgroups ($\\Delta\\tau_s = \\tau_s(1) - \\tau_s(0)$), the bias of global correction in subgroup $s$ at level $z{=}0$ is $+\\delta_s \\cdot \\Delta\\tau_s / (1 - 2\\bar{\\pi})$, and at level $z{=}1$ is $-\\delta_s \\cdot \\Delta\\tau_s / (1 - 2\\bar{\\pi})$.\n\\end{corollary}\nThe proof follows directly from Theorem~\\ref{thm:bias_identity} with $\\tau_s$ replacing $\\tau$.\n\nOur main analysis assumes that subgroup misclassification rates $\\delta_s$ and subgroup CATE magnitudes $\\Delta\\tau_s$ are independent (Assumption A5).\nIn practice, both may depend on text features that define subgroups, introducing correlation.\nWe test robustness under two configurations with the DIM estimator ($K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 50 MC replications, $\\pi = [0.05, 0.25]$):\n\\emph{aligned} (positive $\\delta_s$--$\\Delta\\tau_s$ correlation: high-error S1 has the larger treatment effect, $\\Delta\\tau = [0.30, 0.70]$) and\n\\emph{adversarial} (negative correlation: high-error S1 has the smaller effect, $\\Delta\\tau = [0.70, 0.30]$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Coverage and $|\\text{bias}|$ under A5 violation ($K{=}2$, $n_{\\text{expert}}{=}250$, 50 MC). Target coverage: 0.95.}\n\\label{tab:a5_violation}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nConfig & Method & S0 cov & S1 cov & S0 $|\\text{bias}|$ & S1 $|\\text{bias}|$ \\\\\n\\midrule\n\\multirow{4}{*}{Aligned}\n & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\\\\n & Naive         & 0.93 & 0.25 & 0.022 & 0.174 \\\\\n & Global        & 0.93 & 0.82 & 0.036 & 0.094 \\\\\n & EC-HTE (EB)   & 0.95 & 0.95 & 0.005 & 0.017 \\\\\n\\midrule\n\\multirow{4}{*}{Adversarial}\n & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\\\\n & Naive         & 0.90 & 0.78 & 0.042 & 0.074 \\\\\n & Global        & 0.74 & 0.93 & 0.098 & 0.040 \\\\\n & EC-HTE (EB)   & 0.94 & 0.96 & 0.002 & 0.007 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn the aligned configuration, the $\\delta_s \\times \\Delta\\tau_s$ product is maximized in the high-error subgroup, causing naive S1 coverage to collapse to 0.25.\nGlobal correction improves S1 but cannot fully correct without subgroup-specific error rates.\nIn the adversarial configuration, global correction overcorrects the low-error subgroup (S0 coverage 0.74).\nEC-HTE (EB) maintains $\\geq 0.94$ coverage across both subgroups in both configurations, with bias comparable to the oracle.\nResults at $n_{\\text{expert}}{=}500$ are consistent (all EC-HTE coverages $\\in [0.93, 0.99]$).\n\n\\paragraph{Empirical validation of Corollary~\\ref{cor:aggregate_bias}.}\nUnder the main grid (520 configurations, A5 holds), $\\Delta\\tau_s$ is constant across subgroups, so $\\mathrm{Cov}_w(\\pi_s, \\Delta\\tau_s) = 0$ for every configuration.\nThe predicted aggregate bias is therefore exactly zero, and the observed aggregate bias across 100 MC runs is $< 0.003$ (residual MC noise), confirming that subgroup-level biases---which reach $|\\delta_s \\cdot \\Delta\\tau|/(1-2\\bar{\\pi}) = 0.071$---cancel perfectly in aggregate.\nThis explains why aggregate metrics fail to detect global correction's bias problem.\nUnder A5 violation, the covariance is nonzero: $\\mathrm{Cov}_w(\\pi_s, \\Delta\\tau_s) = +0.020$ (aligned) and $-0.020$ (adversarial), yielding predicted aggregate biases of $\\pm 0.029$.\nPer-subgroup biases computed from Proposition~\\ref{prop:a5_relaxation} ($\\delta_s \\cdot \\Delta\\tau_s / (1{-}2\\bar{\\pi})$) match the MC-observed values in Table~\\ref{tab:a5_violation} (signed residuals $< 0.005$).\n\n\\subsection{Assumption (A1): Sensitivity to Outcome-Dependent Misclassification}\n\\label{app:a1_sensitivity}\n\nWe assess EC-HTE's robustness when misclassification depends on potential outcomes, violating~(A1).\nWe modify the synthetic DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$) so that misclassification probability becomes outcome-dependent: $P(\\hat{Z}{\\neq}Z \\mid Z, S, Y) = \\mathrm{clamp}(\\pi_s + \\gamma \\cdot (Y - \\mu_Y)/\\sigma_Y,\\, 0,\\, 1)$, where $\\gamma \\in \\{0, 0.05, 0.10, 0.15, 0.20\\}$ controls the strength of violation.\nTable~\\ref{tab:a1_sensitivity} reports results averaged over 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{Sensitivity to Assumption~(A1) violation. Coverage and $|\\text{bias}|$ under outcome-dependent misclassification ($\\gamma > 0$).}\n\\label{tab:a1_sensitivity}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc ccc}\n\\toprule\n& \\multicolumn{3}{c}{Coverage (\\%)} & \\multicolumn{3}{c}{$|\\text{Bias}|$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n$\\gamma$ & EC-HTE & Global & Naive & EC-HTE & Global & Naive \\\\\n\\midrule\n0.00 & 95.5 & 92.7 & 87.7 & 0.060 & 0.065 & 0.061 \\\\\n0.05 & 95.5 & 93.5 & 83.8 & 0.059 & 0.064 & 0.064 \\\\\n0.10 & 95.3 & 93.8 & 83.5 & 0.063 & 0.064 & 0.067 \\\\\n0.15 & 94.8 & 94.3 & 79.2 & 0.065 & 0.064 & 0.070 \\\\\n0.20 & 93.5 & 94.0 & 79.5 & 0.068 & 0.063 & 0.073 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nEC-HTE maintains near-nominal coverage ($\\geq$93.5\\%) across the full $\\gamma$ range, with $|\\text{bias}|$ increasing only 13.7\\% from $\\gamma{=}0$ to $\\gamma{=}0.2$.\nAll correction methods (Global, Stratified MLE, HB) maintain $\\geq$90\\% coverage, indicating that moderate (A1) violations do not catastrophically degrade confusion-matrix-based correction.\nThe naive estimator degrades most rapidly (coverage $-$8.2pp), consistent with outcome-dependent misclassification compounding the uncorrected label noise.\n\n\\subsection{Assumption (A1): Treatment-Dependent Misclassification}\n\\label{app:treatment_dep}\n\nWe extend the (A1) sensitivity analysis to the treatment-dependent case, where misclassification probability depends on treatment assignment $T$: $P(\\hat{Z}{\\neq}Z \\mid Z, S, T) = \\mathrm{clamp}(\\pi_s + \\gamma_T \\cdot (2T - 1),\\, 0,\\, 1)$, with $\\gamma_T \\in \\{0, 0.05, 0.10, 0.15, 0.20\\}$.\nThis scenario arises when LLM accuracy varies with treatment status---e.g., treated texts may be systematically harder to classify.\nSetup: $K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{Sensitivity to treatment-dependent misclassification ($\\gamma_T$). EC-HTE maintains $\\geq$89.7\\% coverage at $\\gamma_T \\leq 0.05$.}\n\\label{tab:treatment_dep}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n$\\gamma_T$ & EC-HTE Coverage & EC-HTE RMSE \\\\\n\\midrule\n0.00 & 0.945 & 0.075 \\\\\n0.05 & 0.897 & 0.092 \\\\\n0.10 & 0.750 & 0.133 \\\\\n0.15 & 0.525 & 0.177 \\\\\n0.20 & 0.370 & 0.224 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE is robust to small treatment-dependent violations ($\\gamma_T \\leq 0.05$), maintaining $\\geq$89.7\\% coverage with modest RMSE increase (0.075 to 0.092).\nAt $\\gamma_T = 0.10$, coverage drops to 75.0\\%, establishing this as the approximate breakeven point.\nThe degradation is steeper than for outcome-dependent violations (Table~\\ref{tab:a1_sensitivity}), because treatment-dependent errors directly contaminate the treatment arm contrast.\nFigure~\\ref{fig:treatment_dep} visualizes the coverage and RMSE trajectories.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/treatment_dep_misclass.pdf}\n\\caption{EC-HTE coverage and RMSE under treatment-dependent misclassification. Dashed line: 90\\% coverage threshold. Breakeven at $\\gamma_T \\approx 0.10$.}\n\\label{fig:treatment_dep}\n\\end{figure}\n\n\\subsection{Extension to Confounded Treatment Assignment}\n\\label{app:confounded_dgp}\n\nEC-HTE's confusion matrix correction operates on estimated CATEs regardless of how those estimates are produced.\nTo verify compatibility with observational (non-RCT) designs, we pair EC-HTE with an inverse probability weighted difference-in-means (IPW-DIM) estimator under confounded treatment assignment.\n\n\\paragraph{DGP.}\n$N{=}5{,}000$, $K{=}2$, $\\pi = [0.05, 0.25]$, $n_{\\text{expert}}{=}250$, 100 MC replications.\nA covariate $X \\sim \\mathcal{N}(0,1)$ confounds both treatment and outcome:\n$T \\sim \\text{Bernoulli}(\\sigma(\\beta X))$ with $\\beta{=}0.5$ (moderate confounding; propensity range $[0.38, 0.62]$),\n$Y = 1 + 0.5 Z + 0.3 X + \\tau(Z) \\cdot T + \\eta$, $\\eta \\sim \\mathcal{N}(0,1)$.\nTreatment effects are $\\tau(Z{=}0){=}0$, $\\tau(Z{=}1){=}0.3$.\nThe IPW-DIM estimator uses \\emph{oracle propensity} $e(X) = \\sigma(\\beta X)$, with propensity scores clipped to $[0.05, 0.95]$.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE under confounded treatment assignment (IPW-DIM with oracle propensity, $\\beta{=}0.5$, 100 MC).}\n\\label{tab:confounded_dgp}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Coverage & RMSE & $|\\text{Bias}|$ \\\\\n\\midrule\nOracle (true $Z$ + IPW) & 0.943 & 0.061 & 0.048 \\\\\nHB EC-HTE              & 0.950 & 0.086 & 0.068 \\\\\nGlobal                  & 0.930 & 0.087 & 0.071 \\\\\nStrat MLE               & 0.950 & 0.087 & 0.069 \\\\\nNaive                   & 0.863 & 0.083 & 0.066 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE achieves 95.0\\% coverage, within 0.7pp of the oracle (94.3\\%), confirming that confusion matrix correction and propensity weighting compose without interference.\nThe improvement is most pronounced in the high-error subgroup ($\\pi{=}0.25$): EC-HTE coverage is 96.0\\% vs.\\ naive 78.5\\% ($+$17.5pp).\nGlobal coverage (93.0\\%) falls below the correction methods (95.0\\%), consistent with the cost of ignoring subgroup-level error heterogeneity even in the confounded setting.\n\n\\paragraph{Sensitivity to confounding strength and propensity estimation.}\nWe sweep $\\beta \\in \\{0.25, 0.5, 1.0, 2.0\\}$ and compare oracle propensity ($e(X) = \\sigma(\\beta X)$) with estimated propensity (logistic regression fit on $(X, T)$), yielding 8 configurations (100 MC each).\nTable~\\ref{tab:confounded_sweep} reports HB EC-HTE and naive coverage.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE coverage across confounding strengths and propensity sources. The logistic regression propensity model is correctly specified; propensity misspecification is a complementary concern addressed by the IPW literature.}\n\\label{tab:confounded_sweep}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n$\\beta$ & Propensity & HB Coverage & Naive Coverage \\\\\n\\midrule\n0.25 & Oracle    & 0.963 & 0.848 \\\\\n0.25 & Estimated & 0.973 & 0.845 \\\\\n0.50 & Oracle    & 0.950 & 0.863 \\\\\n0.50 & Estimated & 0.958 & 0.858 \\\\\n1.00 & Oracle    & 0.958 & 0.898 \\\\\n1.00 & Estimated & 0.960 & 0.883 \\\\\n2.00 & Oracle    & 0.945 & 0.858 \\\\\n2.00 & Estimated & 0.948 & 0.858 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains coverage $\\geq$94.5\\% across all 8 configurations, including strong confounding ($\\beta{=}2.0$, propensity range $[0.12, 0.88]$).\nThe oracle--estimated gap is $\\leq$1pp, confirming that propensity estimation error does not meaningfully degrade EC-HTE when the propensity model is correctly specified.\nThis validates that EC-HTE is robust to confounded treatment assignment when the propensity model is correctly specified.\n\n\\subsection{Empirical Comparison with Frazis--Loewenstein Correction}\n\\label{app:fl_comparison}\n\nWe empirically compare EC-HTE's confusion matrix inversion against the scalar attenuation correction of \\citet{frazis2003estimating} (F-L).\nThe F-L correction rescales the observed estimate as $\\hat{\\tau}_{\\text{FL}} = \\hat{\\tau}_{\\text{obs}} / (1 - 2\\bar{\\pi})$, where $\\bar{\\pi}$ is the (global or per-subgroup) misclassification rate.\nWe test two variants: F-L \\emph{scalar} (single global $\\bar{\\pi}$) and F-L \\emph{per-subgroup} ($\\pi_s$-specific rescaling).\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, $\\pi{=}[0.05, 0.25]$ (extreme heterogeneity), $\\tau(z{=}0){=}0$, $\\tau(z{=}1){=}0.3$, 100 MC runs.\nThis DGP uses smaller treatment effects ($\\bar{\\tau}{=}0.15$, $\\Delta\\tau{=}0.3$) than the main experiments (Table~\\ref{tab:main_results}: $\\bar{\\tau}{=}0.5$), chosen to isolate the F-L comparison without conflating correction quality with treatment effect magnitude.\n\n\\begin{table}[h]\n\\centering\n\\caption{F-L correction vs.\\ EC-HTE under heterogeneous misclassification ($\\Delta\\pi{=}0.20$, $\\bar{\\tau}{=}0.15$). $|\\text{Bias}|$ is unsigned and averaged across subgroups and $z$-levels; the Oracle floor (0.045) reflects finite-sample estimation noise. Both F-L variants produce \\emph{higher} aggregate bias than the uncorrected estimator.}\n\\label{tab:fl_comparison}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle         & 0.045 & 0.056 & 0.943 \\\\\nNaive          & 0.062 & 0.077 & 0.858 \\\\\nGlobal (CM inv)& 0.064 & 0.081 & 0.938 \\\\\nHB EC-HTE      & 0.064 & 0.086 & \\textbf{0.953} \\\\\nF-L Scalar     & 0.091 & 0.116 & 0.850 \\\\\nF-L Per-Subgroup & 0.112 & 0.158 & 0.838 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth F-L variants produce \\emph{higher} bias and RMSE than the naive estimator (F-L per-subgroup $|\\text{bias}|{=}0.112$ vs.\\ naive $0.062$), demonstrating that scalar attenuation cannot substitute for confusion matrix inversion under subgroup-heterogeneous misclassification.\nThe per-subgroup bias direction reveals the mechanism: F-L scalar over-corrects the low-error subgroup ($s_0$: mean bias ${=}+0.073$ vs.\\ naive $+0.005$, a $14.6\\times$ amplification), while F-L per-subgroup dramatically over-corrects the high-error subgroup ($s_1$: mean bias ${=}+0.160$).\nEC-HTE achieves near-zero \\emph{signed} per-subgroup bias ($s_0{:}\\,{+}0.006$, $s_1{:}\\,{+}0.001$) with nominal coverage (95.3\\%); the aggregate unsigned $|\\text{bias}|{=}0.064$ in Table~\\ref{tab:fl_comparison} includes irreducible finite-sample noise (Oracle floor $= 0.045$).\nThe root cause is structural: F-L's $1/(1{-}2\\pi)$ scaling amplifies each $z$-level estimate independently, whereas CM inversion simultaneously redistributes the cross-contamination between misclassified and correctly classified observations.\n\n\\subsection{End-to-End Validation with Asymmetric Confusion Matrices}\n\\label{app:asymmetric_endtoend}\n\nWe validate EC-HTE under strongly asymmetric confusion matrices ($\\text{FPR}/\\text{FNR}$ ratio up to $7{:}1$), simulating the error profile of GPT-4.1 on Civil Comments.\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$; $s_0$: $\\text{FPR}{=}0.05$, $\\text{FNR}{=}0.02$ (low error); $s_1$: $\\text{FPR}{=}0.38$, $\\text{FNR}{=}0.054$ ($7{:}1$ ratio); 100 MC runs.\nWe compare EC-HTE using the full $2{\\times}2$ asymmetric CM (Remark~\\ref{rem:asymmetric}) against the symmetric assumption ($\\text{FPR}{=}\\text{FNR}{=}\\pi_s$).\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE under asymmetric misclassification ($\\text{FPR}/\\text{FNR}$ up to $7{:}1$). The asymmetric formula improves coverage by $+1.5$pp and RMSE by $11.5\\%$.}\n\\label{tab:asymmetric_endtoend}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle              & 0.045 & 0.056 & 0.943 \\\\\nEC-HTE (asymmetric) & 0.057 & 0.074 & \\textbf{0.945} \\\\\nNaive               & 0.059 & 0.073 & 0.870 \\\\\nGlobal (asymmetric) & 0.061 & 0.076 & 0.915 \\\\\nEC-HTE (symmetric)  & 0.062 & 0.083 & 0.930 \\\\\nGlobal (symmetric)  & 0.063 & 0.078 & 0.915 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE with the asymmetric formula achieves 94.5\\% coverage versus 93.0\\% under the symmetric assumption ($+1.5$pp), with RMSE improved from 0.083 to 0.074 ($-11.5\\%$).\nThe improvement concentrates in the high-error subgroup ($s_1$): asymmetric coverage is 93.0\\% vs.\\ symmetric 91.0\\%.\nPractitioners should estimate full $2 \\times 2$ confusion matrices rather than assuming symmetric misclassification, particularly when FPR and FNR differ substantially.\n\n\\subsection{Complementarity with LLM Calibration}\n\\label{app:calibration}\n\nTemperature or Platt scaling~\\cite{guo2017calibration} can reduce per-subgroup misclassification rates, but does not eliminate heterogeneity $\\Delta\\pi$.\nWe simulate calibration by shrinking per-subgroup rates from $\\pi{=}[0.05, 0.25]$ ($\\Delta\\pi{=}0.20$) to $\\pi{=}[0.08, 0.15]$ ($\\Delta\\pi{=}0.07$), testing whether EC-HTE remains necessary post-calibration.\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{Calibration reduces $\\Delta\\pi$ but does not eliminate it; EC-HTE corrects the residual bias. Best coverage is achieved by combining both.}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle                    & 0.043 & 0.053 & 0.963 \\\\\nCalibrated + EC-HTE       & 0.055 & 0.069 & \\textbf{0.965} \\\\\nCalibrated + Global       & 0.055 & 0.068 & 0.963 \\\\\nCalibrated + Naive        & 0.051 & 0.064 & 0.913 \\\\\nUncalibrated + EC-HTE     & 0.064 & 0.084 & 0.938 \\\\\nUncalibrated + Global     & 0.069 & 0.085 & 0.920 \\\\\nUncalibrated + Naive      & 0.063 & 0.079 & 0.840 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCalibration alone improves naive coverage from 84.0\\% to 91.3\\% but does not reach the nominal 95\\%.\nCalibrated + EC-HTE achieves the highest coverage (96.5\\%), demonstrating that calibration and EC-HTE address complementary error sources: calibration reduces per-subgroup $\\pi_s$ while EC-HTE corrects the residual $\\delta_s$-driven bias from heterogeneity that persists post-calibration.\nPropensity estimation robustness under model misspecification is a complementary concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior.\n\n\\subsection{Policy Reversal Zone Analysis}\n\\label{app:policy_reversal}\n\nWhen the true treatment effect is small, global correction can reverse the sign of estimated CATE---concluding a beneficial treatment is harmful---creating a \\emph{policy reversal zone}.\nWe sweep $\\tau(0) \\in \\{0.01, 0.02, 0.03, 0.05, 0.07, 0.10\\}$ under the standard DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs; $\\Delta\\tau{=}0.30$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Policy reversal zone: fraction of configurations where global correction reverses the sign of estimated CATE.\nThe naive estimator produces zero sign reversals across all $\\tau(0)$ values; EC-HTE also achieves 0\\% reversal.}\n\\label{tab:policy_reversal}\n\\small\n\\begin{tabular}{ccc}\n\\toprule\n$\\tau(0)$ & Global reversal \\% & Most extreme $\\hat{\\tau}_{\\text{global}}$ \\\\\n\\midrule\n0.01 & 31.0 & $-0.079$ \\\\\n0.02 & 21.6 & --- \\\\\n0.03 & 14.9 & $-0.059$ \\\\\n0.05 & 6.1  & $-0.039$ \\\\\n0.07 & 1.6  & --- \\\\\n$\\geq$0.10 & 0 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe reversal rate increases monotonically as $\\tau(0)$ decreases: at $\\tau(0) = 0.01$, 31\\% of configurations yield sign reversal, with the most extreme case estimating $\\hat{\\tau} = -0.079$ when the true effect is $\\tau = +0.01$.\nThe critical threshold is $\\tau(0) < 0.089$, matching the closed-form prediction from Theorem~\\ref{thm:bias_identity}: $|\\delta_{\\max} \\cdot \\Delta\\tau_{\\max}| / (1 - 2\\bar{\\pi}) = 0.125 \\times 0.50 / 0.70 = 0.089$.\nThe most dangerous combination ($\\tau(0) = 0.01$, $\\delta_{\\text{misclass}} = 0.19$) reaches 42.9\\% reversal rate.\nThe naive estimator produces zero sign reversals across all $\\tau(0)$ values, confirming that reversal is an artifact of global correction, not inherent estimation noise.\n\nFigure~\\ref{fig:policy_reversal} visualizes the reversal zone across the $\\Delta\\pi \\times \\tau(0)$ parameter space.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/policy_reversal_zone.pdf}\n\\caption{Policy reversal zone: sign-reversal rate as a function of $\\tau(0)$ and $\\Delta\\pi$. Shaded region marks configurations where global correction reverses the CATE sign, directing policy toward the wrong subgroups.}\n\\label{fig:policy_reversal}\n\\end{figure}\n\n\\input{appendix_stance}\n\n\\input{appendix_agnews}\n\n\\section*{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nThe authors used AI-based writing assistants, including Claude, for limited support during manuscript preparation, including grammar polishing, wording suggestions, LaTeX editing, and code/debugging assistance. The tools were not used to generate the core research ideas, experimental design, methodological decisions, data analysis, or scientific conclusions. All AI-assisted text, code suggestions, and references were manually reviewed and edited by the authors.\n",
      "numLines": 631,
      "startLine": 1000,
      "totalLines": 1630
    }
  },
  "sourceToolAssistantUUID": "284961bd-dff8-4d81-a40b-21884cd87c13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 84_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：ec_hte_llm_annotation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 30 warning 一致性检查…",
  "leafUuid": "eeeb42db-891a-496e-a168-b13bc506157f",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

### Runtime record

_source line 85_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP 2026 paper compliance and structure",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

### Assistant

_source line 86 · 2026-05-25T16:36:02.778Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the content. Let me do the comprehensive content audit.

Let me think through each audit dimension systematically.

## 1. 叙事一致性 (CRITICAL)

### Abstract 的"问题" == Intro 的"问题"？
Abstract: "Standard confusion-matrix correction for noisy annotations assumes uniform error rates. When this assumption fails---as it routinely does with LLM classifiers... correction can reverse estimated effect signs."
Intro: "We show that when error rates vary across subgroups, this standard correction can make things worse."
→ Consistent: both focus on heterogeneous error rates causing global correction to fail.


### Intro contributions align with what the methods section actually delivers. The theoretical result on bias, empirical guidelines, and the heterogeneous-bias effect-heterogeneity method all map to their respective sections, so the narrative holds together.

The method's design choice—computing confusion matrices per subgroup—directly addresses the gap identified in the intro: existing work assumes homogeneous prediction error, but this approach captures how effect modifier misclassification creates bias. Theorem 1 pinpoints per-subgroup misclassification as the bias source, which justifies this estimation strategy.

The experiments validate each claimed contribution: bias identity through the R² verification, operating guidelines through diagnostic analysis, and the correction method through its empirical performance. The conclusion ties back to these results—high R² values confirm the bias mechanism, the diagnostic thresholds (Δπ > 0.15, n_expert ≥ 250) emerge from the experiments, and the findings generalize across 11 LLM-dataset combinations while composing with other methods.

Now checking the abstract structure: it covers the problem (uniform error rate assumption), method (exact bias identity with hierarchical Bayesian correction), results (7.4× bias reduction), and significance (characterizing when per-subgroup correction helps). The word count is around 176 after removing LaTeX formatting, which fits within the EMNLP limit.

For the introduction, I'm verifying the five-paragraph flow: background on LLMs replacing annotators, the problem when error rates vary across subgroups, derivation of the exact bias identity, limitations of existing homogeneous-error approaches, and the contributions. The gap between problem and solution could be more explicit, but it's reasonably woven through.

The Related Work section appears quite brief—just a single paragraph so far.

Now I'm checking whether the contributions align with the paper's structure: the exact bias identity from Theorem 1, empirical operating guidelines from the experiments, and the HB EC-HTE method. I'm also scanning for orphan sections that don't directly support these contributions.

The title and abstract seem well-aligned with what's actually tested—eight LLMs across multiple NLP tasks—though I notice the main text emphasizes sentiment and hate speech while stance detection and topic classification appear only in the appendix. I should verify that the claims about "significantly" improved performance are properly supported by the experimental results. The abstract distinguishes between synthetic grid results (R² ≥ 0.97) and real LLM results (R² = 0.975 aggregate, with per-model range 0.76–0.99), so the claims are properly qualified. Let me verify what experiments.tex actually reports for the R² values. The individual metrics like bias and RMSE don't have explicit error bars, though the budget figure does show ±1 SD bands and Monte Carlo standard errors are reported in the appendix as ≤0.005. For baselines, they've included a solid range of comparisons—naive and global approaches, recent methods like PPI and DSL, classical techniques like Frazis-Loewenstein, and appropriate downstream estimators. The ablations examine the pooling method (HB vs. Stratified MLE) and the κ-guard threshold.

Beyond that, they're also testing hyperprior sensitivity, sweeping across different budget levels and subgroup counts (K=2, 4, 8), exploring both symmetric and asymmetric misclassification, varying class imbalance, and checking robustness to treatment-dependent misclassification and subgroup misspecification—quite thorough coverage. For reproducibility, they've documented the CausalForest hyperparameters, fully specified the data generation process, ran 100 Monte Carlo iterations for the main results with 50 or 20 for expensive experiments, provided code via an anonymous link, and detailed the MCMC setup with 4 chains of 4000 iterations each.

On notation, they're using $\pi_s$ consistently for misclassification rates, $\delta_s$ for deviations from the mean, and $\Delta\tau$ for treatment effect differences, though I'm double-checking how $\Delta\pi$ is being used—it appears to represent the range of per-subgroup misclassification heterogeneity. The compute details are sparse though—they mention sub-5 millisecond estimation times but don't specify GPU hours or full pipeline training time, which would be worth noting even if the simulation-based approach makes it less critical.

Looking at the notation more carefully, $\Delta\pi$ seems to be the observed quantity (max minus min across subgroups), while $\Delta_c$ is the DGP parameter controlling heterogeneity in the simulations. For the binary case they're equivalent, but the distinction between the parameter used in data generation versus the empirical measure could be clearer. I'm noticing that EC-HTE gets used throughout without being properly defined upfront. The acronym appears in the method section as "This correction (EC-HTE)" but the full expansion—Error-Corrected Heterogeneous Treatment Effects—only shows up in the algorithm caption in the appendix. The abstract and introduction reference it without spelling it out, which creates a readability gap since readers encounter the term before getting a formal definition.

Looking at the section transitions, there's an abrupt jump from the introduction into related work with no bridging language, and another disconnect between related work and theory. The theory-to-method transition works better since the theorem naturally motivates the correction approach, but the earlier handoffs feel disjointed.

The related work section is quite brief at seven lines, which might seem rushed but is understandable given space constraints. There's no separate discussion section—the conclusion just summarizes the experimental findings without deeper interpretation, which is typical for ML conference papers.

For the limitations, the paper acknowledges five main constraints: the need for substantial expert labeling budgets, the balanced effect modifier assumption, the untestable conditional independence assumption, the lack of real ground-truth conditional average treatment effects, and potential correlation between covariate and outcome errors. This covers the key practical and theoretical vulnerabilities, though it's presented densely in a single paragraph.

I'm checking whether the limitations section appears only once in the main text and not duplicated in the appendix—confirmed, there's exactly one limitations section. Now I'm looking at the writing style to identify any AI-like patterns, starting with checking for em-dashes.

The Unicode em-dash in the appendix is just a comment, so that's not a concern. But there are quite a few LaTeX em-dashes scattered throughout the paper—I'm counting them across the main text files to see if this is an issue that needs addressing.

Looking at the distribution, I see around 15 em-dashes total across abstract, introduction, theory, method, experiments, conclusion, and limitations. Some of these are in technical contexts where they work fine, but many are explanatory dashes that read like AI-generated text. I should flag these for potential revision.

I also checked for en-dashes and didn't find any, which is good. For the participial phrases ending in "-ing," most seem legitimate, though a couple in the appendix have that characteristic AI style where they're used to wrap up explanations.

The filler words I was looking for—"notably," "importantly," "furthermore," "leverage," and similar—don't appear to be present, which is a positive sign. Paragraph lengths look reasonable too, no obvious over-segmentation.

Now checking for internal experiment references that shouldn't be visible. The main text is clean, but the appendix has some experiment IDs like exp-001, exp-003, exp-015, and exp-016 mentioned in the Monte Carlo section. Let me verify exactly where those appear.

Looking at the appendix, these experiment identifiers do show up with context explaining what they are, but the naming convention "exp-001" style still reads like internal registry IDs rather than descriptive labels. That's worth flagging.

There's also a LaTeX comment in the source at line 214 that says "Promoted to main text" with a figure reference. It's just a comment so it won't render in the PDF, but if the source file gets submitted to reviewers, they'd see this editorial note, which reveals internal process.

For EMNLP requirements, the abstract comes in around 176 words after removing LaTeX markup, so that's within the 200-word limit. And there's a dedicated Limitations section in the main text, which satisfies that requirement.

The ARR checklist is in a separate file but commented out in main.tex, so it won't appear in the compiled PDF. That's actually correct per the rules—the checklist goes in the OpenReview submission form, not in the paper itself.

Now I'm checking the page count. The paper is 32 pages total, which includes the appendix and references. EMNLP allows 8 pages for the main text plus unlimited references and a mandatory limitations section, so even with ~24 pages of appendix, this should be within bounds. Since Phase 1 already confirmed the paper compiled successfully, the main text is presumably within the 8-page limit.

Let me summarize what I've found so far.

I haven't identified any critical issues—the narrative holds together quite consistently. But there are several warning-level concerns: the main text relies heavily on em-dashes (around 15 instances), which is a common AI writing marker. The EC-HTE acronym is never formally defined in the main text, only in an appendix caption. There are internal experiment IDs scattered in the appendix that shouldn't be there. The appendix also uses a lot of participial constructions like "demonstrating that" and "indicating that," which reads like AI output. The Related Work section is extremely brief at just 7 lines—understandable given space constraints, but it borders on a simplistic "A did X, B did Y" structure.

At the info level, I'm noticing the abstract mentions "four NLP tasks" but I need to verify that claim against what's actually in the paper. The R² claims are consistent across the abstract, intro, conclusion, and theory sections—all pointing to values around 0.97 or higher depending on the setup. Now I'm tracing how each contribution maps to the actual sections: the exact bias identity from Theorem 1 shows up in theory with the R² verification in experiments 5.1 and the diagnostic tool in 5.3, while the empirical guidelines for per-subgroup correction appear to be cut off mid-sentence. The R-learner results being relegated to the appendix could be a concern for reviewers since the contribution explicitly claims verification across all three methods. I'm also noticing a discrepancy in the LLM count—the abstract claims "all eight real LLMs tested," but when I look at the actual experimental setup, I'm seeing 6 OpenAI models in the cross-model consistency analysis and 4 open-source models separately, which doesn't quite align with that framing. The abstract also highlights strong performance metrics ($R^2 = 0.975$ aggregate, per-model range $0.76$--$0.99$) that should probably be more prominent. Looking at the actual model counts across the tables, I'm seeing a discrepancy—the paper claims eight LLMs but the bias identity validation table shows 8 models tested on TweetEval plus 3 on Civil Comments, which totals 11 model-dataset combinations, not eight. The breakdown doesn't match the stated claim. So the actual experimental results show 9 models total—5 from OpenAI (GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, GPT-3.5-turbo) and 4 open-source ones (Llama-3.1-8B, Qwen-2.5-7B, Gemma-2-9B, Mistral-7B)—but the introduction claims Claude 3.5 and Gemini 2.5 Flash were tested, and neither of those appear anywhere in the actual results tables. There's also GPT-5.4 showing up in one table but missing from others. This looks like a significant discrepancy between what the intro promises and what the data actually contains. I'm seeing a discrepancy—the actual table lists 8 distinct models (GPT-4-turbo, Qwen2.5-7B, Mistral-7B, Gemma-2-9B, GPT-4o, GPT-4.1, GPT-3.5-turbo, GPT-4o-mini), but none of them are Claude 3.5 or Gemini 2.5 Flash as claimed in the text. The intro's description doesn't match what's actually in the results. I'm noticing a critical discrepancy—the introduction mentions Claude 3.5 and Gemini 2.5 Flash as part of the eight models tested, but neither of these appear anywhere in the actual results tables. Looking at the cross-model consistency data, I see GPT-5.4 mentioned there too, which doesn't show up in the bias validation results, so there's definitely some inconsistency between what the intro claims and what the data actually contains.

I'm also catching another issue: the paper claims to test five open-source models, but I'm only finding four—Llama-3.1-8B, Qwen-2.5-7B, Gemma-2-9B, and Mistral-7B. So there's a mismatch between the stated methodology and what's actually presented in the results.

Let me verify the other claims too. The "11 LLM-dataset combinations" checks out—8 on TweetEval plus 3 on Civil Comments. And the "four NLP tasks" appears consistently across the conclusion and experiments section, though the abstract doesn't explicitly state this number.

I'm noticing a discrepancy with the open-source models count: the intro claims "five open-source models" but the validation appendix only tests four. That's an inconsistency worth noting.

For the R-learner contribution mentioned in the main text, the results are relegated to the appendix showing 89% bias reduction, but that's acceptable for a contribution claim even if the detailed results aren't in the main paper.

I'm also spotting that the method overview figure has duplicate labels in LaTeX, which suggests it may have been renamed or reorganized at some point. And the EMNLP checklist is properly commented out rather than included in the PDF, which aligns with their submission requirements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eeeb42db-891a-496e-a168-b13bc506157f",
  "isSidechain": false,
  "requestId": "req_011CbPcFfQbgXbdqSt8L7ktd",
  "type": "assistant",
  "uuid": "826ffc39-c8c5-4af3-b000-dadc147d075a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012aUkDFPRG527aEhzZmZQF6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19078,
      "cache_read_input_tokens": 109445,
      "output_tokens": 9315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19078,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9315,
          "cache_read_input_tokens": 109445,
          "cache_creation_input_tokens": 19078,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19078
          },
          "type": "message"
        }
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

_source line 87 · 2026-05-25T16:36:02.781Z_

Now I have all the content needed. Let me run a few final checks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "826ffc39-c8c5-4af3-b000-dadc147d075a",
  "isSidechain": false,
  "requestId": "req_011CbPcFfQbgXbdqSt8L7ktd",
  "type": "assistant",
  "uuid": "220c11cc-466c-45df-8de4-42d75dbbd77e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012aUkDFPRG527aEhzZmZQF6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19078,
      "cache_read_input_tokens": 109445,
      "output_tokens": 9315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19078,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9315,
          "cache_read_input_tokens": 109445,
          "cache_creation_input_tokens": 19078,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19078
          },
          "type": "message"
        }
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

_source line 88 · 2026-05-25T16:36:02.783Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Vf5WuVfGNobkE9kHeYnGEu`</summary>

```json
{
  "pattern": "Claude 3\\.5|Gemini 2\\.5",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
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
  "parentUuid": "220c11cc-466c-45df-8de4-42d75dbbd77e",
  "isSidechain": false,
  "requestId": "req_011CbPcFfQbgXbdqSt8L7ktd",
  "type": "assistant",
  "uuid": "5d496c03-4275-423a-baa7-93cc9ce1f022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012aUkDFPRG527aEhzZmZQF6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19078,
      "cache_read_input_tokens": 109445,
      "output_tokens": 9315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19078,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9315,
          "cache_read_input_tokens": 109445,
          "cache_creation_input_tokens": 19078,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19078
          },
          "type": "message"
        }
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

_source line 89 · 2026-05-25T16:36:05.421Z_

<details><summary>↩ Tool result · `toolu_01UjGCK3kDnSzo7KMBSTkDYd`</summary>

```text
13:[Omitted long matching line]
25:\caption{CATE sign reversal under global correction ($K{=}2$, $\tau(0) = 0.03$). (A) Naive vs.\ global-corrected CATE; red triangles mark sign reversals (7.5\% of subgroup estimates). (B) Extreme case: true $\tau = +0.03$, estimated $\hat{\tau} = -0.059$. (C) 14.9\% of configurations exhibit sign reversal; all 8 real LLMs amplify bias; EC-HTE: 0\% reversal.}
32:[Omitted long matching line]
41:    \item One concrete instantiation: hierarchical Bayesian confusion matrix estimation (EC-HTE), verified for DIM, CausalForestDML, and R-learner, and composable with PPCI for joint covariate/outcome error.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a18da82a-e9eb-4c99-ac1a-99e712e64e70",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "fe51b234-c0e8-45a8-8daa-64091abf6dd4",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "13:[Omitted long matching line]\n25:\\caption{CATE sign reversal under global correction ($K{=}2$, $\\tau(0) = 0.03$). (A) Naive vs.\\ global-corrected CATE; red triangles mark sign reversals (7.5\\% of subgroup estimates). (B) Extreme case: true $\\tau = +0.03$, estimated $\\hat{\\tau} = -0.059$. (C) 14.9\\% of configurations exhibit sign reversal; all 8 real LLMs amplify bias; EC-HTE: 0\\% reversal.}\n32:[Omitted long matching line]\n41:    \\item One concrete instantiation: hierarchical Bayesian confusion matrix estimation (EC-HTE), verified for DIM, CausalForestDML, and R-learner, and composable with PPCI for joint covariate/outcome error.",
    "numLines": 4
  },
  "sourceToolAssistantUUID": "a18da82a-e9eb-4c99-ac1a-99e712e64e70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-25T16:36:02.813Z_

<details><summary>↩ Tool result · `toolu_01Vf5WuVfGNobkE9kHeYnGEu`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:98:Across 11 real LLM--dataset combinations (eight LLMs including GPT-4.1, Claude 3.5, Gemini 2.5 Flash, and five open-source models; Appendix~\ref{app:multilm_opensource}), the bias identity achieves aggregate $R^2 = 0.975$ (per-model range 0.76--0.99), and EC-HTE improves RMSE over global correction in 79\% of screening configurations with coverage $\geq$93\%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d496c03-4275-423a-baa7-93cc9ce1f022",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "b4decab6-0fc7-4dc9-acb9-2cb494033012",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:98:Across 11 real LLM--dataset combinations (eight LLMs including GPT-4.1, Claude 3.5, Gemini 2.5 Flash, and five open-source models; Appendix~\\ref{app:multilm_opensource}), the bias identity achieves aggregate $R^2 = 0.975$ (per-model range 0.76--0.99), and EC-HTE improves RMSE over global correction in 79\\% of screening configurations with coverage $\\geq$93\\%.",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "5d496c03-4275-423a-baa7-93cc9ce1f022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-25T16:36:03.293Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01MMATUjywthGVCoCcGTnr3W`</summary>

```json
{
  "pattern": "open.source",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
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
  "parentUuid": "b4decab6-0fc7-4dc9-acb9-2cb494033012",
  "isSidechain": false,
  "requestId": "req_011CbPcFfQbgXbdqSt8L7ktd",
  "type": "assistant",
  "uuid": "ff62e385-24cc-45ca-8276-ebfac5142705",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012aUkDFPRG527aEhzZmZQF6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19078,
      "cache_read_input_tokens": 109445,
      "output_tokens": 9315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19078,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9315,
          "cache_read_input_tokens": 109445,
          "cache_creation_input_tokens": 19078,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19078
          },
          "type": "message"
        }
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

_source line 92 · 2026-05-25T16:36:03.310Z_

<details><summary>↩ Tool result · `toolu_01MMATUjywthGVCoCcGTnr3W`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:18:Semi-synthetic evaluation uses empirical confusion matrices from 11 LLM--dataset combinations (eight LLMs across two datasets; Appendix~\ref{app:realcm_bias}; semi-real CM validation in Appendix~\ref{app:semireal}; open-source LLM validation in Appendix~\ref{app:multilm_opensource}).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:98:Across 11 real LLM--dataset combinations (eight LLMs including GPT-4.1, Claude 3.5, Gemini 2.5 Flash, and five open-source models; Appendix~\ref{app:multilm_opensource}), the bias identity achieves aggregate $R^2 = 0.975$ (per-model range 0.76--0.99), and EC-HTE improves RMSE over global correction in 79\% of screening configurations with coverage $\geq$93\%.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/checklist.tex:28:The TweetEval corpus is publicly available under its original license. Our code is publicly available under an open-source license (see footnote on page 1).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:662:These results were obtained with a single API provider; open-source model validation appears in Appendix~\ref{app:multilm_opensource}.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:667:We evaluate four open-source LLMs (7B--9B parameter range) on 490 TweetEval sentiment tweets with $K{=}4$ subgroups defined by crossing hashtag presence and text length.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:674:\caption{Confusion matrix heterogeneity across four open-source LLMs ($K{=}4$, $N{=}490$ TweetEval tweets). $\Delta\pi$: max--min per-subgroup misclassification rate. Prop.~5: number of subgroups where the $\Delta\tau$-free diagnostic (Proposition~\ref{prop:debiasing_hurts}) triggers.}
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1012:All three models exhibit $\Delta\pi > 0.05$, with overall heterogeneity $\Delta\pi \in [0.113, 0.160]$---comparable to the $\Delta\pi \in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\ref{app:multilm_opensource}).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1014:The consistent presence of $\Delta\pi$ heterogeneity across two NLP tasks, eight LLMs spanning open-source (7B--9B) and proprietary families, and two distinct subgroup definitions confirms that this phenomenon is a structural property of LLM annotation rather than an artifact of a specific dataset or model.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1077:We apply the diagnostic conditions from Proposition~\ref{prop:debiasing_hurts} and Section~\ref{sec:method} to 16 LLM--dataset--$K$ combinations spanning eight LLMs (three open-source, five proprietary) across TweetEval and Civil Comments.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1114:The four open-source LLMs on TweetEval show the strongest EC-HTE advantage (32/32 comparisons, RMSE reduction 0.001--0.008), while GPT-3.5-turbo/TweetEval (high FPR asymmetry, $\mathrm{FPR}_{\max}{=}0.39$) and GPT-4o/Civil Comments (low minority prevalence $P(Z{=}1){=}0.3$) show degradation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff62e385-24cc-45ca-8276-ebfac5142705",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "1c544558-99d0-48bb-a4d9-b69e2eca582c",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:18:Semi-synthetic evaluation uses empirical confusion matrices from 11 LLM--dataset combinations (eight LLMs across two datasets; Appendix~\\ref{app:realcm_bias}; semi-real CM validation in Appendix~\\ref{app:semireal}; open-source LLM validation in Appendix~\\ref{app:multilm_opensource}).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:98:Across 11 real LLM--dataset combinations (eight LLMs including GPT-4.1, Claude 3.5, Gemini 2.5 Flash, and five open-source models; Appendix~\\ref{app:multilm_opensource}), the bias identity achieves aggregate $R^2 = 0.975$ (per-model range 0.76--0.99), and EC-HTE improves RMSE over global correction in 79\\% of screening configurations with coverage $\\geq$93\\%.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/checklist.tex:28:The TweetEval corpus is publicly available under its original license. Our code is publicly available under an open-source license (see footnote on page 1).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:662:These results were obtained with a single API provider; open-source model validation appears in Appendix~\\ref{app:multilm_opensource}.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:667:We evaluate four open-source LLMs (7B--9B parameter range) on 490 TweetEval sentiment tweets with $K{=}4$ subgroups defined by crossing hashtag presence and text length.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:674:\\caption{Confusion matrix heterogeneity across four open-source LLMs ($K{=}4$, $N{=}490$ TweetEval tweets). $\\Delta\\pi$: max--min per-subgroup misclassification rate. Prop.~5: number of subgroups where the $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}) triggers.}\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1012:All three models exhibit $\\Delta\\pi > 0.05$, with overall heterogeneity $\\Delta\\pi \\in [0.113, 0.160]$---comparable to the $\\Delta\\pi \\in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\\ref{app:multilm_opensource}).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1014:The consistent presence of $\\Delta\\pi$ heterogeneity across two NLP tasks, eight LLMs spanning open-source (7B--9B) and proprietary families, and two distinct subgroup definitions confirms that this phenomenon is a structural property of LLM annotation rather than an artifact of a specific dataset or model.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1077:We apply the diagnostic conditions from Proposition~\\ref{prop:debiasing_hurts} and Section~\\ref{sec:method} to 16 LLM--dataset--$K$ combinations spanning eight LLMs (three open-source, five proprietary) across TweetEval and Civil Comments.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1114:The four open-source LLMs on TweetEval show the strongest EC-HTE advantage (32/32 comparisons, RMSE reduction 0.001--0.008), while GPT-3.5-turbo/TweetEval (high FPR asymmetry, $\\mathrm{FPR}_{\\max}{=}0.39$) and GPT-4o/Civil Comments (low minority prevalence $P(Z{=}1){=}0.3$) show degradation.",
    "numLines": 10
  },
  "sourceToolAssistantUUID": "ff62e385-24cc-45ca-8276-ebfac5142705",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-25T16:36:04.733Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0152EFZfRbyNkfvzeeZjehtU`</summary>

```json
{
  "pattern": "exp-0[0-9]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
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
  "parentUuid": "1c544558-99d0-48bb-a4d9-b69e2eca582c",
  "isSidechain": false,
  "requestId": "req_011CbPcFfQbgXbdqSt8L7ktd",
  "type": "assistant",
  "uuid": "e20af339-aaff-4ec4-a09e-b8199b36c761",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012aUkDFPRG527aEhzZmZQF6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19078,
      "cache_read_input_tokens": 109445,
      "output_tokens": 9315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19078,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9315,
          "cache_read_input_tokens": 109445,
          "cache_creation_input_tokens": 19078,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19078
          },
          "type": "message"
        }
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

_source line 94 · 2026-05-25T16:36:04.762Z_

<details><summary>↩ Tool result · `toolu_0152EFZfRbyNkfvzeeZjehtU`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:765:For exp-001 (synthetic DGP, no per-seed pairing across methods), we use conservative two-sample $z$-tests on the 100-run means.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:766:For exp-003 (semi-synthetic TweetEval, shared seeds across methods), we use paired $t$-tests, which are more powerful because they control for seed-level variation.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:773:\caption{Paired comparisons for representative configurations. $\Delta$ = method A $-$ method B (negative favors A for $|\text{bias}|$). Two-sample $z$-tests for synthetic (exp-001); paired $t$-tests for semi-synthetic (exp-003). Bold $p$-values indicate significance at $\alpha = 0.05$.}
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:874:Both exp-015 ($\kappa = 2.38$, effective $n = 2.5$) and exp-016 ($\kappa = 1.55$, effective $n = 2.5$) violate both conditions, and the diagnostic correctly predicts 100\% of their failure cells.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:875:Subgroup-average metrics can mask cell-level heterogeneity: in exp-015, HB EC-HTE substantially reduces bias for the three well-classified subgroups (S1--S3) but amplifies variance in the near-degenerate subgroup (S0, FNR $= 0.526$), and the S0 penalty dominates the aggregate RMSE.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e20af339-aaff-4ec4-a09e-b8199b36c761",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "fc972bf8-940b-4075-b5e5-bdd05040864d",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:765:For exp-001 (synthetic DGP, no per-seed pairing across methods), we use conservative two-sample $z$-tests on the 100-run means.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:766:For exp-003 (semi-synthetic TweetEval, shared seeds across methods), we use paired $t$-tests, which are more powerful because they control for seed-level variation.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:773:\\caption{Paired comparisons for representative configurations. $\\Delta$ = method A $-$ method B (negative favors A for $|\\text{bias}|$). Two-sample $z$-tests for synthetic (exp-001); paired $t$-tests for semi-synthetic (exp-003). Bold $p$-values indicate significance at $\\alpha = 0.05$.}\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:874:Both exp-015 ($\\kappa = 2.38$, effective $n = 2.5$) and exp-016 ($\\kappa = 1.55$, effective $n = 2.5$) violate both conditions, and the diagnostic correctly predicts 100\\% of their failure cells.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:875:Subgroup-average metrics can mask cell-level heterogeneity: in exp-015, HB EC-HTE substantially reduces bias for the three well-classified subgroups (S1--S3) but amplifies variance in the near-degenerate subgroup (S0, FNR $= 0.526$), and the S0 penalty dominates the aggregate RMSE.",
    "numLines": 5
  },
  "sourceToolAssistantUUID": "e20af339-aaff-4ec4-a09e-b8199b36c761",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-25T16:36:05.404Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01UjGCK3kDnSzo7KMBSTkDYd`</summary>

```json
{
  "pattern": "EC-HTE",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc972bf8-940b-4075-b5e5-bdd05040864d",
  "isSidechain": false,
  "requestId": "req_011CbPcFfQbgXbdqSt8L7ktd",
  "type": "assistant",
  "uuid": "a18da82a-e9eb-4c99-ac1a-99e712e64e70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012aUkDFPRG527aEhzZmZQF6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19078,
      "cache_read_input_tokens": 109445,
      "output_tokens": 9315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19078,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9315,
          "cache_read_input_tokens": 109445,
          "cache_creation_input_tokens": 19078,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19078
          },
          "type": "message"
        }
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

_source line 96_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：ec_hte_llm_annotation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 30 warning 一致性检查…",
  "leafUuid": "fe51b234-c0e8-45a8-8daa-64091abf6dd4",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

### Runtime record

_source line 97_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP 2026 paper compliance and structure",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

### Assistant

_source line 98 · 2026-05-25T16:36:24.825Z_

<details><summary>Logged reasoning block</summary>

```text
Now I've confirmed my findings. Let me verify the exact model count:

From the appendix screening table (tab:screening, line 1077): "eight LLMs (three open-source, five proprietary)". The screening table lists:
- Open-source: Gemma-2-9B, Llama-3.1-8B, Mistral-7B, Qwen2.5-7B = **4** open-source (not 3)
- Proprietary: GPT-3.5-turbo, GPT-4-turbo, GPT-4.1, GPT-4o, GPT-4o-mini = **5** proprietary (all OpenAI)


There's a discrepancy here—the text claims three open-source models but the screening table clearly shows four distinct ones, each appearing across different configurations.

More critically, the paper mentions Claude 3.5 and Gemini 2.5 Flash as part of the 8 LLMs tested, yet neither model appears anywhere in the actual results tables. Looking at the bias identity validation table, I can confirm 8 models were tested on TweetEval but only 3 on Civil Comments, which suggests the paper's claims about model coverage don't align with what's actually reported.

The open-source model count is also inconsistent—the paper claims five open-source models but only four are actually used (Llama, Qwen, Gemma, Mistral), and the appendix contradicts itself by saying three. These discrepancies between the stated methodology and the actual results are serious data integrity issues that would immediately concern any reviewer.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe51b234-c0e8-45a8-8daa-64091abf6dd4",
  "isSidechain": false,
  "requestId": "req_011CbPcVahU1bZAti8N875Nk",
  "type": "assistant",
  "uuid": "2f691192-b404-492e-b8ce-30dcfd911e32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JS96RvGfHfHupwNw8qovbc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11520,
      "cache_read_input_tokens": 128523,
      "output_tokens": 1043,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1043,
          "cache_read_input_tokens": 128523,
          "cache_creation_input_tokens": 11520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11520
          },
          "type": "message"
        }
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

_source line 99 · 2026-05-25T16:36:24.828Z_

I've identified a critical issue - the experiments section names specific LLMs not present in any results table. Let me verify one more thing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f691192-b404-492e-b8ce-30dcfd911e32",
  "isSidechain": false,
  "requestId": "req_011CbPcVahU1bZAti8N875Nk",
  "type": "assistant",
  "uuid": "e35412b2-fffb-4071-8a5a-3b98fcc00c65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JS96RvGfHfHupwNw8qovbc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11520,
      "cache_read_input_tokens": 128523,
      "output_tokens": 1043,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1043,
          "cache_read_input_tokens": 128523,
          "cache_creation_input_tokens": 11520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11520
          },
          "type": "message"
        }
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

_source line 100 · 2026-05-25T16:36:26.617Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01GC8Rfa5yZVFhSQabB9EgPL`</summary>

```json
{
  "pattern": "GPT-5\\.4|GPT5",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
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
  "parentUuid": "e35412b2-fffb-4071-8a5a-3b98fcc00c65",
  "isSidechain": false,
  "requestId": "req_011CbPcVahU1bZAti8N875Nk",
  "type": "assistant",
  "uuid": "99fb38e4-7fb9-4c10-afe3-25aa3ce5a9dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JS96RvGfHfHupwNw8qovbc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11520,
      "cache_read_input_tokens": 128523,
      "output_tokens": 1043,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1043,
          "cache_read_input_tokens": 128523,
          "cache_creation_input_tokens": 11520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11520
          },
          "type": "message"
        }
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

_source line 101 · 2026-05-25T16:36:27.758Z_

<details><summary>↩ Tool result · `toolu_01R5KnbVjnGsN4fUUS1j1j3b`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:18:Semi-synthetic evaluation uses empirical confusion matrices from 11 LLM--dataset combinations (eight LLMs across two datasets; Appendix~\ref{app:realcm_bias}; semi-real CM validation in Appendix~\ref{app:semireal}; open-source LLM validation in Appendix~\ref{app:multilm_opensource}).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:98:Across 11 real LLM--dataset combinations (eight LLMs including GPT-4.1, Claude 3.5, Gemini 2.5 Flash, and five open-source models; Appendix~\ref{app:multilm_opensource}), the bias identity achieves aggregate $R^2 = 0.975$ (per-model range 0.76--0.99), and EC-HTE improves RMSE over global correction in 79\% of screening configurations with coverage $\geq$93\%.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex:4:We derived an exact bias identity ($R^2 \geq 0.97$) that yields a diagnostic for flagging harmful correction and prescribes per-subgroup correction when $\Delta\pi > 0.15$ and $n_{\text{expert}} \geq 250$, validated across 11 LLM--dataset combinations spanning eight LLMs and four NLP tasks.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:667:We evaluate four open-source LLMs (7B--9B parameter range) on 490 TweetEval sentiment tweets with $K{=}4$ subgroups defined by crossing hashtag presence and text length.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:674:\caption{Confusion matrix heterogeneity across four open-source LLMs ($K{=}4$, $N{=}490$ TweetEval tweets). $\Delta\pi$: max--min per-subgroup misclassification rate. Prop.~5: number of subgroups where the $\Delta\tau$-free diagnostic (Proposition~\ref{prop:debiasing_hurts}) triggers.}
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1012:All three models exhibit $\Delta\pi > 0.05$, with overall heterogeneity $\Delta\pi \in [0.113, 0.160]$---comparable to the $\Delta\pi \in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\ref{app:multilm_opensource}).
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1014:The consistent presence of $\Delta\pi$ heterogeneity across two NLP tasks, eight LLMs spanning open-source (7B--9B) and proprietary families, and two distinct subgroup definitions confirms that this phenomenon is a structural property of LLM annotation rather than an artifact of a specific dataset or model.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1077:We apply the diagnostic conditions from Proposition~\ref{prop:debiasing_hurts} and Section~\ref{sec:method} to 16 LLM--dataset--$K$ combinations spanning eight LLMs (three open-source, five proprietary) across TweetEval and Civil Comments.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1114:The four open-source LLMs on TweetEval show the strongest EC-HTE advantage (32/32 comparisons, RMSE reduction 0.001--0.008), while GPT-3.5-turbo/TweetEval (high FPR asymmetry, $\mathrm{FPR}_{\max}{=}0.39$) and GPT-4o/Civil Comments (low minority prevalence $P(Z{=}1){=}0.3$) show degradation.
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex:32:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "461eea56-5eb4-4759-b526-842b41882568",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "f60aa6df-4ddd-4f28-91e6-e5f91a1d6e4d",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:18:Semi-synthetic evaluation uses empirical confusion matrices from 11 LLM--dataset combinations (eight LLMs across two datasets; Appendix~\\ref{app:realcm_bias}; semi-real CM validation in Appendix~\\ref{app:semireal}; open-source LLM validation in Appendix~\\ref{app:multilm_opensource}).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:98:Across 11 real LLM--dataset combinations (eight LLMs including GPT-4.1, Claude 3.5, Gemini 2.5 Flash, and five open-source models; Appendix~\\ref{app:multilm_opensource}), the bias identity achieves aggregate $R^2 = 0.975$ (per-model range 0.76--0.99), and EC-HTE improves RMSE over global correction in 79\\% of screening configurations with coverage $\\geq$93\\%.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex:4:We derived an exact bias identity ($R^2 \\geq 0.97$) that yields a diagnostic for flagging harmful correction and prescribes per-subgroup correction when $\\Delta\\pi > 0.15$ and $n_{\\text{expert}} \\geq 250$, validated across 11 LLM--dataset combinations spanning eight LLMs and four NLP tasks.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:667:We evaluate four open-source LLMs (7B--9B parameter range) on 490 TweetEval sentiment tweets with $K{=}4$ subgroups defined by crossing hashtag presence and text length.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:674:\\caption{Confusion matrix heterogeneity across four open-source LLMs ($K{=}4$, $N{=}490$ TweetEval tweets). $\\Delta\\pi$: max--min per-subgroup misclassification rate. Prop.~5: number of subgroups where the $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}) triggers.}\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1012:All three models exhibit $\\Delta\\pi > 0.05$, with overall heterogeneity $\\Delta\\pi \\in [0.113, 0.160]$---comparable to the $\\Delta\\pi \\in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\\ref{app:multilm_opensource}).\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1014:The consistent presence of $\\Delta\\pi$ heterogeneity across two NLP tasks, eight LLMs spanning open-source (7B--9B) and proprietary families, and two distinct subgroup definitions confirms that this phenomenon is a structural property of LLM annotation rather than an artifact of a specific dataset or model.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1077:We apply the diagnostic conditions from Proposition~\\ref{prop:debiasing_hurts} and Section~\\ref{sec:method} to 16 LLM--dataset--$K$ combinations spanning eight LLMs (three open-source, five proprietary) across TweetEval and Civil Comments.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:1114:The four open-source LLMs on TweetEval show the strongest EC-HTE advantage (32/32 comparisons, RMSE reduction 0.001--0.008), while GPT-3.5-turbo/TweetEval (high FPR asymmetry, $\\mathrm{FPR}_{\\max}{=}0.39$) and GPT-4o/Civil Comments (low minority prevalence $P(Z{=}1){=}0.3$) show degradation.\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex:32:[Omitted long matching line]",
    "numLines": 10
  },
  "sourceToolAssistantUUID": "461eea56-5eb4-4759-b526-842b41882568",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-25T16:36:26.641Z_

<details><summary>↩ Tool result · `toolu_01GC8Rfa5yZVFhSQabB9EgPL`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:653:GPT-5.4 & 0.114 & \checkmark \\
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:661:Newer models reduce absolute error rates but do not eliminate subgroup heterogeneity: GPT-5.4 achieves $\Delta\pi = 0.114$ compared to GPT-3.5-Turbo's $0.198$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99fb38e4-7fb9-4c10-afe3-25aa3ce5a9dc",
  "isSidechain": false,
  "promptId": "4d8b4271-6d2a-42a6-95d5-0ed157e45c15",
  "type": "user",
  "uuid": "b1e47272-c41d-40d9-b275-d753cb69953f",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:653:GPT-5.4 & 0.114 & \\checkmark \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex:661:Newer models reduce absolute error rates but do not eliminate subgroup heterogeneity: GPT-5.4 achieves $\\Delta\\pi = 0.114$ compared to GPT-3.5-Turbo's $0.198$.",
    "numLines": 2
  },
  "sourceToolAssistantUUID": "99fb38e4-7fb9-4c10-afe3-25aa3ce5a9dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-25T16:36:27.734Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01R5KnbVjnGsN4fUUS1j1j3b`</summary>

```json
{
  "pattern": "eight LLMs|five open-source|three open-source|four open-source",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
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
  "parentUuid": "b1e47272-c41d-40d9-b275-d753cb69953f",
  "isSidechain": false,
  "requestId": "req_011CbPcVahU1bZAti8N875Nk",
  "type": "assistant",
  "uuid": "461eea56-5eb4-4759-b526-842b41882568",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JS96RvGfHfHupwNw8qovbc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11520,
      "cache_read_input_tokens": 128523,
      "output_tokens": 1043,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1043,
          "cache_read_input_tokens": 128523,
          "cache_creation_input_tokens": 11520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11520
          },
          "type": "message"
        }
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

_source line 104 · 2026-05-25T16:36:27.810Z_

```json
{
  "parentUuid": "f60aa6df-4ddd-4f28-91e6-e5f91a1d6e4d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d9892cc3-6039-4c81-867d-181dc2269d06",
  "timestamp": "2026-05-25T16:36:27.810Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 105 · 2026-05-25T16:37:04.629Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have full clarity. Let me compile:

LLM count issues:
1. experiments.tex:98 says "eight LLMs including GPT-4.1, Claude 3.5, Gemini 2.5 Flash, and five open-source models"
   - Claude 3.5 and Gemini 2.5 Flash appear NOWHERE in any results table
   - "five open-source models" but appendix consistently says "four open-source LLMs" (Llama, Qwen, Gemma, Mistral)
   - The actual 8 models in tab:realcm_r2 are: GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, GPT-3.5-turbo (5 proprietary) + Qwen2.5-7B, Mistral-7B, Gemma-2-9B (3 open-source) =

Wait, I need to recount more carefully. Looking at tab:realcm_r2, I see 8 models total, but when I check tab:multilm_cm for the open-source subset, it lists Llama-3.1-8B alongside Qwen, Gemma, and Mistral—so Llama appears in one table but not the other, which creates another inconsistency in how the models are being reported across different sections. I'm recounting the model breakdown more carefully—there are actually 5 proprietary models (the GPT variants) and 3 open-source ones (Qwen, Mistral, Gemma), which adds up to 8 total in the R² table, but Llama is conspicuously absent despite being part of the open-source evaluation elsewhere. The model counts are inconsistent across different tables depending on which models are included. I'm spotting a pattern of inconsistencies across the document—the model counts keep shifting depending on where I look. The screening section claims three open-source models but the table actually shows four, and there's a broader mismatch between what the text says about which models were used versus what the experimental results actually contain. Claude 3.5 and Gemini 2.5 Flash are mentioned but have no corresponding data, which suggests these descriptions weren't updated when the experiments changed.

Looking at the actual models that appear in the results tables, I'm finding ten total: six proprietary models (GPT-3.5-Turbo, GPT-4-Turbo, GPT-4o-mini, GPT-5.4, GPT-4.1, GPT-4o) and four open-source ones (Llama-3.1-8B, Qwen-2.5-7B, Gemma-2-9B, Mistral-7B). GPT-5.4 shows up in the cross-model consistency table but not in the bias validation results, which means it was selectively used for certain experiments. The named models in the introduction don't match what's actually in the data—there's no Claude or Gemini anywhere in the experimental results.

Now I'm doing a final count of em-dashes across the main text files to get a precise sense of the document's formatting patterns. Scanning through abstract, introduction, theory, method, experiments, conclusion, and limitations sections, I'm tallying roughly sixteen em-dashes total in the main text, with the theory section containing the most.

I should also note that the appendix has significantly more occurrences, so I'll document both the main text and appendix findings in my final audit report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9892cc3-6039-4c81-867d-181dc2269d06",
  "isSidechain": false,
  "requestId": "req_011CbPcXEJgfF4ZgERaxLrYj",
  "type": "assistant",
  "uuid": "175eeee2-1a84-43b3-83e2-1e05b1a4ed9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKshC4cPS3iQog7UjaPTqT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2586,
      "cache_read_input_tokens": 140043,
      "output_tokens": 3918,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2586,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3918,
          "cache_read_input_tokens": 140043,
          "cache_creation_input_tokens": 2586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2586
          },
          "type": "message"
        }
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

_source line 106 · 2026-05-25T16:37:54.836Z_

审计完成。以下是结构化输出。

```
[CONTENT_AUDIT_START]
- [critical] [叙事一致性] experiments.tex:98 声称 "eight LLMs including GPT-4.1, Claude 3.5, Gemini 2.5 Flash, and five open-source models"，但全文无任何 Claude 3.5 或 Gemini 2.5 Flash 的实验结果。tab:realcm_r2 的 8 个模型全部是 OpenAI（GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, GPT-3.5-turbo）和开源模型（Qwen2.5-7B, Mistral-7B, Gemma-2-9B）。论文正文明确列举了不存在于任何结果表中的模型名，审稿人核对会立即发现。
- [critical] [叙事一致性] experiments.tex:98 称 "five open-source models"，但 appendix tab:multilm_cm 明确标注 "four open-source LLMs"（Llama-3.1-8B, Qwen-2.5-7B, Gemma-2-9B, Mistral-7B），appendix.tex:1077 又称 "three open-source"。同一论文内对开源模型数量有三种不同说法（3/4/5），数据一致性严重不足。
- [critical] [叙事一致性] introduction.tex:32 fig_combined_overview 的 caption 提到 "Key results across eight LLMs and four NLP tasks"，conclusion.tex:4 也说 "eight LLMs and four NLP tasks"。如果 "eight LLMs" 的具体列表与 experiments.tex:98 的列表一致（含 Claude/Gemini），则 Intro、Figure caption、Conclusion 均与实际实验结果不匹配。
- [warning] [去AI] 主文件（abstract/intro/theory/method/experiments/conclusion/limitations）共约 16 处 LaTeX em-dash（---），是最显著的 AI 写作标志。审稿人敏感。例：abstract.tex:3 "fails---as it routinely does"，introduction.tex:5 "increases hate speech...---but the true effect"，theory.tex:109 "---debiasing is worse than doing nothing"。应全部改为逗号、括号或拆分句子。
- [warning] [去AI] appendix.tex 另有约 30 处 em-dash（---），密度更高。虽然 appendix 审稿人阅读较粗，但累积效应仍会强化 AI 生成印象。
- [warning] [术语一致性] "EC-HTE" 缩写在正文中从未展开定义。introduction.tex:13 首次使用 "(EC-HTE; Section 5)"，method.tex:5 再次使用 "This correction (EC-HTE)"，但均未给出全称。全称 "Error-Corrected Heterogeneous Treatment Effects" 仅出现在 appendix Algorithm 1 的 caption 中。按照写作规范，首次使用缩写必须展开。
- [warning] [内部信息残留] appendix.tex:765-766 使用内部实验编号 "exp-001"、"exp-003"，appendix.tex:874-875 使用 "exp-015"、"exp-016"。这些是内部 registry ID，应使用描述性名称（如 "the synthetic DGP experiment"、"the semi-real GPT-4.1 experiment"）。
- [warning] [去AI] appendix.tex 多处使用 participial -ing 结尾：619 "demonstrating that subgroup-varying misclassification..."、637 "indicating that the subgroup error structure..."、1579 "demonstrating that calibration and EC-HTE address..."。应改为独立句子。
- [warning] [章节结构] related_work.tex 仅 7 行（1 个段落），本质为 "A did X; B did Y; C did Z" 堆砌结构，缺乏主题归纳和定位分析。虽然空间紧张且 appendix 有扩展版，但主文的 Related Work 过于薄弱，审稿人可能标注 "insufficient positioning"。
- [warning] [符号一致性] DGP 描述（appendix.tex:195）使用 $\Delta_c$ 表示错误率差异（"$\Delta_c \in \{0, 0.05, 0.1, 0.15\}$"），而正文通篇使用 $\Delta\pi$ 表示同一概念。同一量用两个不同符号，增加混乱。
- [warning] [内部信息残留] appendix.tex:214 有 LaTeX 注释 "% [Promoted to main text — Figure~\ref{fig:heatmap}]"。虽不会渲染，但会议投稿要求提交源码时审稿人可见，暴露内部编辑流程。
- [info] [贡献-范围对齐] Contribution 3（introduction.tex:41）声称 EC-HTE "verified for DIM, CausalForestDML, and R-learner"，但 R-learner 结果仅在 appendix（tab:rlearner），主文无任何 R-learner 数据。虽合规，但审稿人可能认为主文未充分支撑此贡献项。
- [info] [叙事一致性] Abstract 和 Conclusion 均提 "four NLP tasks"，但主文实验仅详述 sentiment（TweetEval）和 hate speech（CivilComments）；stance 和 AG News 整体在 appendix。叙事暗示四个任务权重相当，实际两个是主力、两个是补充验证。
- [info] [可复现性] 论文未报告总计算量（GPU-hours / 总 wall-clock time）。虽然主要是 Monte Carlo 模拟而非深度学习训练，但 checklist 要求报告 computational budget，当前仅提及 "<5ms per subgroup" 的 EB 估计时间。
- [info] [章节过渡] Introduction 末尾的 contribution list 后直接切入 Related Work，无过渡句。Theory section 末尾同样无显式过渡到 Method。段落间逻辑关系靠读者自行推断。
- [info] [可复现性] Semi-synthetic 实验依赖特定 LLM API 版本（GPT-4.1、GPT-4o-mini 等）的真实标注结果，这些 API 版本可能被厂商弃用。论文未讨论如何保障长期可复现性（如是否保存了原始标注结果）。
- [info] [Claim强度] abstract.tex:4 "verified at R² ≥ 0.97" 对应 synthetic grids（K=2: 0.994, K=4: 0.97），但同句括号内补充 real LLM R² = 0.975（per-model 0.76-0.99）。个别模型低至 0.76 与 "≥ 0.97" 形成微妙张力；虽然句法上 ≥ 0.97 仅指 synthetic，但读者可能误读为全部 ≥ 0.97。
- [info] [符号一致性] fig_combined_overview 使用了两个 \label：\label{fig:overview} 和 \label{fig:method_overview}（introduction.tex:33-34）。method.tex:6 引用 fig:method_overview。双 label 不影响编译但显示图可能经历重命名，且 fig:overview 可能成为未引用的孤儿 label。
[CONTENT_AUDIT_END]
```

[AUDIT_DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "175eeee2-1a84-43b3-83e2-1e05b1a4ed9d",
  "isSidechain": false,
  "requestId": "req_011CbPcXEJgfF4ZgERaxLrYj",
  "type": "assistant",
  "uuid": "cfe3ec4b-1c63-4592-89ca-e82ebb2ca3df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/paper_audit_content_6f3a74bb",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKshC4cPS3iQog7UjaPTqT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2586,
      "cache_read_input_tokens": 140043,
      "output_tokens": 3918,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2586,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3918,
          "cache_read_input_tokens": 140043,
          "cache_creation_input_tokens": 2586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2586
          },
          "type": "message"
        }
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

_source line 107_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：ec_hte_llm_annotation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 30 warning 一致性检查…",
  "leafUuid": "cfe3ec4b-1c63-4592-89ca-e82ebb2ca3df",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

### Runtime record

_source line 108_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP 2026 paper compliance and structure",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

### Runtime record

_source line 109_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：ec_hte_llm_annotation Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 30 warning 一致性检查…",
  "leafUuid": "cfe3ec4b-1c63-4592-89ca-e82ebb2ca3df",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---

### Runtime record

_source line 110_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP 2026 paper compliance and structure",
  "sessionId": "929445b7-1f7a-4e7b-9fef-acd3294376fb"
}
```

---
