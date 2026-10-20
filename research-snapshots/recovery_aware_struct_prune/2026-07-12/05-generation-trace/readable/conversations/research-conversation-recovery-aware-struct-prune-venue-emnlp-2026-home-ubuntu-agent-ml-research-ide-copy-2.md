# Research conversation: 项目：recovery_aware_struct_prune Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 89
- **Recorded user turns:** 1
- **Tool calls:** 28
- **Original source:** `logs/chats/exported-trajectories/account-1/eb6dd8fa-dc16-4561-bba5-af5f73e15303.jsonl`
- **Structured JSON:** [`e635bce3d2d1924b75bc.json`](../../sessions/e6/e635bce3d2d1924b75bc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-23T04:05:23.806Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-23T04:05:23.806Z",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "content": "项目：recovery_aware_struct_prune\nVenue：emnlp-2026\n论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper\n\nPhase 1 确定性检查结果：\n源码检查: passed=False, 6 critical, 21 warning\n一致性检查: 0 critical, 0 warning\n编译: ✅, 页数: 15\n内部信息: 0 critical, 0 warning\n\n━━━ 用户自定义规则（作为额外检查项）━━━\n## 用户自定义规则（必须遵守）\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section\n\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n请将以上规则逐条作为额外审计维度检查。违反的规则用 dimension `[写作规则]` 或 `[审稿规则]` 标记，severity 按实际影响判定。\n\n请按照你的角色指令执行内容结构审计。"
}
```

---

### Runtime record

_source line 2 · 2026-05-23T04:05:23.811Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-23T04:05:23.811Z",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303"
}
```

---

## Round 1

87 recorded events

### User

_source line 3 · 2026-05-23T04:05:23.860Z_

项目：recovery_aware_struct_prune
Venue：emnlp-2026
论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper

Phase 1 确定性检查结果：
源码检查: passed=False, 6 critical, 21 warning
一致性检查: 0 critical, 0 warning
编译: ✅, 页数: 15
内部信息: 0 critical, 0 warning

━━━ 用户自定义规则（作为额外检查项）━━━
## 用户自定义规则（必须遵守）
### 写作规则

- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长
- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面
- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section

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
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "c733a956-cece-4479-a37b-886004795f24",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-23T04:05:23.860Z_

```json
{
  "parentUuid": "c733a956-cece-4479-a37b-886004795f24",
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
  "uuid": "73758b54-7434-4e09-b77c-f42a21b83e6c",
  "timestamp": "2026-05-23T04:05:23.860Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-23T04:05:23.860Z_

```json
{
  "parentUuid": "73758b54-7434-4e09-b77c-f42a21b83e6c",
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
  "uuid": "c8322584-389e-48d4-8d77-44e94c4e5c6c",
  "timestamp": "2026-05-23T04:05:23.860Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-23T04:05:23.860Z_

```json
{
  "parentUuid": "c8322584-389e-48d4-8d77-44e94c4e5c6c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0758355c-0dc7-4542-a8e0-569aaf282ec9",
  "timestamp": "2026-05-23T04:05:23.860Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
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
  "aiTitle": "Recovery-aware structured pruning paper audit",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303"
}
```

---

### Assistant

_source line 8 · 2026-05-23T04:05:28.857Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a content structure audit of the paper. Let me follow the execution flow:

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
  "parentUuid": "0758355c-0dc7-4542-a8e0-569aaf282ec9",
  "isSidechain": false,
  "requestId": "req_011CbJqdYP2vyfEKeAEiKnAp",
  "type": "assistant",
  "uuid": "e5bbbd27-0e57-4480-ad8f-d07438cca9d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3VjWdy2nCqyrXQXGwCc2W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26936,
      "cache_read_input_tokens": 11846,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26936
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-23T04:05:29.445Z_

开始执行内容结构审计。先加载审计标准和论文源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5bbbd27-0e57-4480-ad8f-d07438cca9d8",
  "isSidechain": false,
  "requestId": "req_011CbJqdYP2vyfEKeAEiKnAp",
  "type": "assistant",
  "uuid": "535591e2-84fd-49d2-8e37-4588cbb9356a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3VjWdy2nCqyrXQXGwCc2W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26936,
      "cache_read_input_tokens": 11846,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26936
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-23T04:05:30.417Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H6JhCJtbvKcK9k96iVpnph`</summary>

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
  "parentUuid": "535591e2-84fd-49d2-8e37-4588cbb9356a",
  "isSidechain": false,
  "requestId": "req_011CbJqdYP2vyfEKeAEiKnAp",
  "type": "assistant",
  "uuid": "a6706179-7b54-4f42-934f-720511b39ba6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3VjWdy2nCqyrXQXGwCc2W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26936,
      "cache_read_input_tokens": 11846,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26936
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-23T04:05:31.795Z_

<details><summary>↩ Tool result · `toolu_0126UmxoSU3AU8RP1muZQhen`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table2_recovery.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table5_inference.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table1_postprune.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fad79cea-c056-4f6a-9b3e-a2373930f687",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "d757302f-09ac-4fa3-9959-6808c3a110c1",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table2_recovery.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table5_inference.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table1_postprune.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/ethics.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex"
    ],
    "durationMs": 6,
    "numFiles": 25,
    "truncated": false
  },
  "sourceToolAssistantUUID": "fad79cea-c056-4f6a-9b3e-a2373930f687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T04:05:30.428Z_

<details><summary>↩ Tool result · `toolu_01H6JhCJtbvKcK9k96iVpnph`</summary>

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
  "parentUuid": "a6706179-7b54-4f42-934f-720511b39ba6",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "c0876b25-5271-4a93-99c4-5c495bbeb905",
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
  "sourceToolAssistantUUID": "a6706179-7b54-4f42-934f-720511b39ba6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 13 · 2026-05-23T04:05:31.632Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ATAfWNzrQxGkpuNnmvudfs`</summary>

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
  "parentUuid": "c0876b25-5271-4a93-99c4-5c495bbeb905",
  "isSidechain": false,
  "requestId": "req_011CbJqdYP2vyfEKeAEiKnAp",
  "type": "assistant",
  "uuid": "553b8253-9827-4c07-a657-6a4eba1ed65e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3VjWdy2nCqyrXQXGwCc2W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26936,
      "cache_read_input_tokens": 11846,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26936
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-23T04:05:31.638Z_

<details><summary>↩ Tool result · `toolu_01ATAfWNzrQxGkpuNnmvudfs`</summary>

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
  "parentUuid": "553b8253-9827-4c07-a657-6a4eba1ed65e",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "9964715b-f8bc-4a87-9f3d-03644d2520bf",
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
  "sourceToolAssistantUUID": "553b8253-9827-4c07-a657-6a4eba1ed65e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 15 · 2026-05-23T04:05:31.784Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0126UmxoSU3AU8RP1muZQhen`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9964715b-f8bc-4a87-9f3d-03644d2520bf",
  "isSidechain": false,
  "requestId": "req_011CbJqdYP2vyfEKeAEiKnAp",
  "type": "assistant",
  "uuid": "fad79cea-c056-4f6a-9b3e-a2373930f687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3VjWdy2nCqyrXQXGwCc2W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26936,
      "cache_read_input_tokens": 11846,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26936
          },
          "type": "message"
        }
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
  "lastPrompt": "项目：recovery_aware_struct_prune Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 6 critical,…",
  "leafUuid": "d757302f-09ac-4fa3-9959-6808c3a110c1",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Recovery-aware structured pruning paper audit",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303"
}
```

---

### Assistant

_source line 18 · 2026-05-23T04:05:34.347Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read all the main .tex files (not backup). Let me read them in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d757302f-09ac-4fa3-9959-6808c3a110c1",
  "isSidechain": false,
  "requestId": "req_011CbJqe8RAU8hhy9mDRfdxH",
  "type": "assistant",
  "uuid": "59a3abc5-98c2-4787-b8c0-a4c69f6a4a6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AikNj8BwKMU39MmHyboKMo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12647,
      "cache_read_input_tokens": 38782,
      "output_tokens": 801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 801,
          "cache_read_input_tokens": 38782,
          "cache_creation_input_tokens": 12647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12647
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-23T04:05:34.802Z_

读取所有正文 .tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59a3abc5-98c2-4787-b8c0-a4c69f6a4a6f",
  "isSidechain": false,
  "requestId": "req_011CbJqe8RAU8hhy9mDRfdxH",
  "type": "assistant",
  "uuid": "299047a5-c018-4986-bc4a-73ef5e6bd45b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AikNj8BwKMU39MmHyboKMo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12647,
      "cache_read_input_tokens": 38782,
      "output_tokens": 801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 801,
          "cache_read_input_tokens": 38782,
          "cache_creation_input_tokens": 12647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12647
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-23T04:05:35.381Z_

<details open><summary>🔧 Tool call — Read · `toolu_018EPmu41zmDcuw4VaoX2XWV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "299047a5-c018-4986-bc4a-73ef5e6bd45b",
  "isSidechain": false,
  "requestId": "req_011CbJqe8RAU8hhy9mDRfdxH",
  "type": "assistant",
  "uuid": "2f1abeb9-a37d-44b6-b601-fa85eacd6bb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AikNj8BwKMU39MmHyboKMo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12647,
      "cache_read_input_tokens": 38782,
      "output_tokens": 801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 801,
          "cache_read_input_tokens": 38782,
          "cache_creation_input_tokens": 12647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12647
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-23T04:05:40.602Z_

<details><summary>↩ Tool result · `toolu_01RGiy1HFWhi9Y8QgRXY263N`</summary>

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
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{siunitx}
17	\usepackage{algorithm}
18	\usepackage[noend]{algpseudocode}
19	\usepackage{enumitem}
20	\usepackage{xcolor}
21	\usepackage{hyperref}
22	
23	\newcommand{\rasp}{\textsc{Rasp}}
24	
25	\title{How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\begin{abstract}
33	\input{abstract}
34	\end{abstract}
35	
36	\input{introduction}
37	\input{related_work}
38	\input{method}
39	\input{experiments}
40	\input{conclusion}
41	
42	\section*{Limitations}
43	\input{limitations}
44	
45	\section*{Ethics Statement}
46	\input{ethics}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{appendix}
52	
53	\end{document}
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f622f46-21ab-453e-8b79-c8f3257c3625",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "cd927b6d-1ddd-4d9e-82b5-01d9710be747",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{siunitx}\n\\usepackage{algorithm}\n\\usepackage[noend]{algpseudocode}\n\\usepackage{enumitem}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\n\\newcommand{\\rasp}{\\textsc{Rasp}}\n\n\\title{How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{conclusion}\n\n\\section*{Limitations}\n\\input{limitations}\n\n\\section*{Ethics Statement}\n\\input{ethics}\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 54,
      "startLine": 1,
      "totalLines": 54
    }
  },
  "sourceToolAssistantUUID": "9f622f46-21ab-453e-8b79-c8f3257c3625",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T04:05:35.386Z_

<details><summary>↩ Tool result · `toolu_018EPmu41zmDcuw4VaoX2XWV`</summary>

```text
1	Fine-grained structured pruning of reasoning Large Language Models (LLMs)---removing MLP channel groups rather than entire layers---is typically followed by recovery training (SFT or RLVR) to restore reasoning capabilities.
2	RLVR is widely considered superior, yet we demonstrate that this hierarchy reflects suboptimal pruning rather than a fundamental property of RL: when pruning preserves representational diversity, recovery method choice becomes irrelevant (max $|\Delta(\text{GRPO}-\text{SFT})| {=} 1.34$\,pp across 4 fine-grained criteria and 3 sparsity levels on GSM8K and MBPP, with differences remaining within statistical noise on MATH-500), a phenomenon we term \emph{reward-accuracy decoupling}.
3	We propose Recovery-Aware Structured Pruning (\rasp{}), which balances gradient importance with CKA-based representational diversity via a coefficient $\alpha$.
4	A dose-response analysis across $\alpha \in \{0.5, 1.0, 2.0, 3.0, 4.0\}$ on DeepSeek-R1-Distill-Qwen-7B reveals an inverted-U: recovery peaks at $\alpha{=}2.0$ (66.11\% on GSM8K), the optimal balance of importance and diversity.
5	Under identical GRPO training, importance-dominated pruning ($\alpha{=}1.0$) collapses while diversity-preserving criteria achieve active learning (peak reward 4.4$\times$), forming a \emph{recovery capacity spectrum} that tracks preserved representational diversity.
6	Cross-scale (1.5B) and cross-architecture (Qwen2.5-Math-7B) experiments provide initial evidence for generality.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f1abeb9-a37d-44b6-b601-fa85eacd6bb1",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "14f69a8e-20b8-4a85-80a3-98b1968f8831",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex",
      "content": "Fine-grained structured pruning of reasoning Large Language Models (LLMs)---removing MLP channel groups rather than entire layers---is typically followed by recovery training (SFT or RLVR) to restore reasoning capabilities.\nRLVR is widely considered superior, yet we demonstrate that this hierarchy reflects suboptimal pruning rather than a fundamental property of RL: when pruning preserves representational diversity, recovery method choice becomes irrelevant (max $|\\Delta(\\text{GRPO}-\\text{SFT})| {=} 1.34$\\,pp across 4 fine-grained criteria and 3 sparsity levels on GSM8K and MBPP, with differences remaining within statistical noise on MATH-500), a phenomenon we term \\emph{reward-accuracy decoupling}.\nWe propose Recovery-Aware Structured Pruning (\\rasp{}), which balances gradient importance with CKA-based representational diversity via a coefficient $\\alpha$.\nA dose-response analysis across $\\alpha \\in \\{0.5, 1.0, 2.0, 3.0, 4.0\\}$ on DeepSeek-R1-Distill-Qwen-7B reveals an inverted-U: recovery peaks at $\\alpha{=}2.0$ (66.11\\% on GSM8K), the optimal balance of importance and diversity.\nUnder identical GRPO training, importance-dominated pruning ($\\alpha{=}1.0$) collapses while diversity-preserving criteria achieve active learning (peak reward 4.4$\\times$), forming a \\emph{recovery capacity spectrum} that tracks preserved representational diversity.\nCross-scale (1.5B) and cross-architecture (Qwen2.5-Math-7B) experiments provide initial evidence for generality.\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  },
  "sourceToolAssistantUUID": "2f1abeb9-a37d-44b6-b601-fa85eacd6bb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T04:05:36.351Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FPPwmE24KuRg74JQD8x7uY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14f69a8e-20b8-4a85-80a3-98b1968f8831",
  "isSidechain": false,
  "requestId": "req_011CbJqe8RAU8hhy9mDRfdxH",
  "type": "assistant",
  "uuid": "0c95e98b-9a89-44ca-9f7a-d1880f1c92d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AikNj8BwKMU39MmHyboKMo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12647,
      "cache_read_input_tokens": 38782,
      "output_tokens": 801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 801,
          "cache_read_input_tokens": 38782,
          "cache_creation_input_tokens": 12647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12647
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-23T04:05:36.355Z_

<details><summary>↩ Tool result · `toolu_01FPPwmE24KuRg74JQD8x7uY`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Reasoning Large Language Models can be compressed through structured pruning, but the pruned model must recover its reasoning capabilities through fine-tuning.
5	The dominant assumption is that the recovery paradigm---SFT versus RLVR---determines recovery quality: \citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, significantly outperforming SFT.
6	We show that this hierarchy is an artifact of suboptimal pruning.
7	When pruning preserves representational diversity, recovery method choice becomes irrelevant: mean $|\Delta(\text{GRPO}-\text{SFT})| {=} 0.54$\,pp (max $1.34$\,pp) across all fine-grained pruning criteria and sparsity levels on GSM8K and MBPP.
8	What determines recovery quality is not \emph{how} you train after pruning, but \emph{which structures} you remove during pruning.
9	
10	Existing structured pruning methods for reasoning LLMs~\citep{graspprune2026,resp2025,llmpruner2023,bonsai2025} optimize for post-pruning quality without studying how the criterion shapes downstream RL recovery.
11	\citet{rlsqueezes2026} show that RL and SFT impose fundamentally different demands on model representations---RL compresses incorrect paths while SFT expands correct ones---suggesting that pruning decisions should affect RL trainability.
12	Yet no prior work has compared multiple pruning criteria under RL or asked whether the ``RLVR $>$ SFT'' advantage persists across pruning strategies.
13	We note that \citet{selfhealing2025} evaluate unstructured magnitude pruning retaining 96.5\% of dense parameters; our findings concern fine-grained structural pruning where entire channel groups are removed, and the two settings may impose different demands on RL recovery.
14	
15	\begin{figure}[t]
16	\centering
17	\includegraphics[width=\columnwidth]{../figures/paper/fig1_dose_response.pdf}
18	\caption{Dose-response curve for the CKA diversity coefficient $\alpha$ at 20\% MLP channel sparsity on GSM8K ($N{=}1{,}319$). Recovery accuracy follows an inverted-U, peaking at $\alpha{=}2.0$ (66.11\%). SFT and GRPO curves nearly overlap ($|\Delta| \leq 1.14$\,pp at every point), visually demonstrating reward-accuracy decoupling: the pruning criterion---not the recovery paradigm---determines outcome.}
19	\label{fig:dose_response}
20	\end{figure}
21	
22	We present a controlled comparison on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} at 20\% MLP channel sparsity, varying the balance between gradient importance and CKA-based representational diversity~\citep{kornblith2019cka} via a coefficient $\alpha$ in the pruning score (Figure~\ref{fig:dose_response}).
23	The dose-response curve reveals an inverted-U: recovery peaks at $\alpha{=}2.0$ (66.11\% GRPO on GSM8K~\citep{cobbe2021gsm8k}), where importance and diversity reach optimal balance.
24	Under identical GRPO~\citep{shao2024grpo} training, four criteria produce a \textbf{recovery capacity spectrum}: CKA-only pruning achieves active learning (peak reward 4.4$\times$ Standard), Random stagnates, Standard (importance-only;~\citealp{llmpruner2023}) exhibits borderline collapse, and $\alpha{=}1.0$ collapses fully.
25	The ordering tracks preserved representational diversity, not gradient importance.
26	A depth pruning baseline (ShortGPT;~\citealp{shortgpt2024}) is the only method where GRPO actively degrades accuracy ($-$1.36\,pp), confirming that pruning granularity interacts with RL trainability.
27	
28	Our contributions are:
29	\begin{enumerate}[nosep,leftmargin=*]
30	    \item We discover \textbf{reward-accuracy decoupling}: mean $|\Delta(\text{GRPO}-\text{SFT})| {=} 0.54$\,pp (max $1.34$\,pp) across all fine-grained pruning criteria and sparsity levels on GSM8K and MBPP, a consistent empirical finding demonstrating that recovery method choice is secondary to pruning criterion quality. This decoupling is sparsity-dependent: at 15\%, GRPO amplifies the CKA-guided advantage ($+$1.51\,pp differential; $p{<}0.001$), while at 20--25\% it cannot improve upon SFT baselines (\S\ref{sec:decoupling}).
31	    \item We propose \textbf{Recovery-Aware Structured Pruning (\rasp{})} for fine-grained structural pruning, which balances gradient importance with CKA-based representational diversity via a coefficient $\alpha$. A dose-response analysis across $\alpha \in \{0.5, 1.0, 2.0, 3.0, 4.0\}$ reveals an inverted-U on GSM8K, peaking at $\alpha{=}2.0$ (66.11\%). Under identical GRPO training, four criteria produce a \textbf{recovery capacity spectrum} that tracks preserved diversity, validated across scales (1.5B) and architectures (Qwen2.5-Math-7B) (\S\ref{sec:scoring}, \S\ref{sec:recovery_gradient}, \S\ref{sec:extended_analysis}).
32	\end{enumerate}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c95e98b-9a89-44ca-9f7a-d1880f1c92d2",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "7ae75a70-0633-4ef3-9862-c50f4928ce0f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\nReasoning Large Language Models can be compressed through structured pruning, but the pruned model must recover its reasoning capabilities through fine-tuning.\nThe dominant assumption is that the recovery paradigm---SFT versus RLVR---determines recovery quality: \\citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, significantly outperforming SFT.\nWe show that this hierarchy is an artifact of suboptimal pruning.\nWhen pruning preserves representational diversity, recovery method choice becomes irrelevant: mean $|\\Delta(\\text{GRPO}-\\text{SFT})| {=} 0.54$\\,pp (max $1.34$\\,pp) across all fine-grained pruning criteria and sparsity levels on GSM8K and MBPP.\nWhat determines recovery quality is not \\emph{how} you train after pruning, but \\emph{which structures} you remove during pruning.\n\nExisting structured pruning methods for reasoning LLMs~\\citep{graspprune2026,resp2025,llmpruner2023,bonsai2025} optimize for post-pruning quality without studying how the criterion shapes downstream RL recovery.\n\\citet{rlsqueezes2026} show that RL and SFT impose fundamentally different demands on model representations---RL compresses incorrect paths while SFT expands correct ones---suggesting that pruning decisions should affect RL trainability.\nYet no prior work has compared multiple pruning criteria under RL or asked whether the ``RLVR $>$ SFT'' advantage persists across pruning strategies.\nWe note that \\citet{selfhealing2025} evaluate unstructured magnitude pruning retaining 96.5\\% of dense parameters; our findings concern fine-grained structural pruning where entire channel groups are removed, and the two settings may impose different demands on RL recovery.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../figures/paper/fig1_dose_response.pdf}\n\\caption{Dose-response curve for the CKA diversity coefficient $\\alpha$ at 20\\% MLP channel sparsity on GSM8K ($N{=}1{,}319$). Recovery accuracy follows an inverted-U, peaking at $\\alpha{=}2.0$ (66.11\\%). SFT and GRPO curves nearly overlap ($|\\Delta| \\leq 1.14$\\,pp at every point), visually demonstrating reward-accuracy decoupling: the pruning criterion---not the recovery paradigm---determines outcome.}\n\\label{fig:dose_response}\n\\end{figure}\n\nWe present a controlled comparison on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} at 20\\% MLP channel sparsity, varying the balance between gradient importance and CKA-based representational diversity~\\citep{kornblith2019cka} via a coefficient $\\alpha$ in the pruning score (Figure~\\ref{fig:dose_response}).\nThe dose-response curve reveals an inverted-U: recovery peaks at $\\alpha{=}2.0$ (66.11\\% GRPO on GSM8K~\\citep{cobbe2021gsm8k}), where importance and diversity reach optimal balance.\nUnder identical GRPO~\\citep{shao2024grpo} training, four criteria produce a \\textbf{recovery capacity spectrum}: CKA-only pruning achieves active learning (peak reward 4.4$\\times$ Standard), Random stagnates, Standard (importance-only;~\\citealp{llmpruner2023}) exhibits borderline collapse, and $\\alpha{=}1.0$ collapses fully.\nThe ordering tracks preserved representational diversity, not gradient importance.\nA depth pruning baseline (ShortGPT;~\\citealp{shortgpt2024}) is the only method where GRPO actively degrades accuracy ($-$1.36\\,pp), confirming that pruning granularity interacts with RL trainability.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We discover \\textbf{reward-accuracy decoupling}: mean $|\\Delta(\\text{GRPO}-\\text{SFT})| {=} 0.54$\\,pp (max $1.34$\\,pp) across all fine-grained pruning criteria and sparsity levels on GSM8K and MBPP, a consistent empirical finding demonstrating that recovery method choice is secondary to pruning criterion quality. This decoupling is sparsity-dependent: at 15\\%, GRPO amplifies the CKA-guided advantage ($+$1.51\\,pp differential; $p{<}0.001$), while at 20--25\\% it cannot improve upon SFT baselines (\\S\\ref{sec:decoupling}).\n    \\item We propose \\textbf{Recovery-Aware Structured Pruning (\\rasp{})} for fine-grained structural pruning, which balances gradient importance with CKA-based representational diversity via a coefficient $\\alpha$. A dose-response analysis across $\\alpha \\in \\{0.5, 1.0, 2.0, 3.0, 4.0\\}$ reveals an inverted-U on GSM8K, peaking at $\\alpha{=}2.0$ (66.11\\%). Under identical GRPO training, four criteria produce a \\textbf{recovery capacity spectrum} that tracks preserved diversity, validated across scales (1.5B) and architectures (Qwen2.5-Math-7B) (\\S\\ref{sec:scoring}, \\S\\ref{sec:recovery_gradient}, \\S\\ref{sec:extended_analysis}).\n\\end{enumerate}\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  },
  "sourceToolAssistantUUID": "0c95e98b-9a89-44ca-9f7a-d1880f1c92d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T04:05:36.828Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B24zU7DLvMDpXGRgJtW8R2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ae75a70-0633-4ef3-9862-c50f4928ce0f",
  "isSidechain": false,
  "requestId": "req_011CbJqe8RAU8hhy9mDRfdxH",
  "type": "assistant",
  "uuid": "bdcf9bb5-c1f5-45ad-88bc-65b4e785f0a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AikNj8BwKMU39MmHyboKMo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12647,
      "cache_read_input_tokens": 38782,
      "output_tokens": 801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 801,
          "cache_read_input_tokens": 38782,
          "cache_creation_input_tokens": 12647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12647
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-23T04:05:36.833Z_

<details><summary>↩ Tool result · `toolu_01B24zU7DLvMDpXGRgJtW8R2`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Structured pruning of LLMs.}
5	LLM-Pruner~\citep{llmpruner2023} introduced dependency-aware structural pruning for transformers; Bonsai~\citep{bonsai2025} achieves competitive results using only forward passes; GRASPrune~\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups.
6	ShortGPT~\citep{shortgpt2024}, SliceGPT~\citep{slicegpt2024}, and LaCo~\citep{yang2024laco} target depth pruning, though \citet{shrestha2026layerpruninglimits} show this causes severe reasoning degradation even when classification is preserved; Wanda~\citep{wanda2024} addresses unstructured sparsity; \citet{doingmore2026} revisit the structured-vs-unstructured trade-off under test-time scaling.
7	For reasoning models, RESP~\citep{resp2025} uses gradient-based importance on self-generated reasoning traces, RAC~\citep{rac2025} reconstructs chain-of-thought during pruning, SSGR~\citep{ssgr2025} uses self-generated calibration data, and \citet{llms2lrms2026} find width pruning more robust than depth pruning for reasoning but do not study RLVR recovery.
8	A parallel line recognizes that functional structure should guide pruning: FANG~\citep{fang_2025} groups FFN neurons by activation clusters, FuncNet~\citep{funcnet_2025} decomposes LLMs via ICA, and MPruner~\citep{mpruner2024} uses inter-layer CKA~\citep{kornblith2019cka} for depth pruning in CNNs.
9	Our work uses \emph{intra-layer} CKA between individual structures at a finer granularity, optimizing for RL recovery capacity rather than immediate accuracy preservation.
10	
11	\paragraph{Pruning-aware recovery.}
12	\citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, significantly outperforming SFT, but evaluate only importance-based pruning; our controlled experiments demonstrate that this RLVR${>}$SFT advantage vanishes under diversity-preserving pruning---it is a property of the pruning criterion, not of RL training itself.
13	We note that our experiments use different models and tasks than \citet{selfhealing2025}; the finding may not transfer to their exact setup.
14	$P^2$ Law~\citep{p2law2025} establishes scaling laws for post-training loss after pruning.
15	PASER~\citep{paser2025} optimizes recovery data selection, PAT~\citep{pat2025} jointly considers pruning and fine-tuning objectives, RestoreLCC~\citep{restorelcc_2025} contrastively probes critical attention heads for post-hoc compensation, \citet{boiling_frog_2026} adopt iterative prune-tune loops for gradual compression, and OPSD~\citep{opsd2026} compresses reasoning models \emph{after} RLVR (the reverse of our pipeline).
16	ARRoL~\citep{xu2026arrol} prunes rollouts during RLVR generation for training efficiency.
17	These approaches optimize complementary axes; our work isolates which \emph{pruning criterion} enables RL-based recovery.
18	The Lottery Ticket Hypothesis~\citep{frankle2019lth} asks which subnetworks train effectively from random initialization; our recovery capacity spectrum extends this to \emph{paradigm-conditioned trainability}, where the optimal subnetwork depends on the recovery paradigm (RLVR vs.\ SFT).
19	
20	\paragraph{RLVR training dynamics.}
21	\citet{rlsqueezes2026} show that RLVR \emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \emph{expands} correct ones via local imitation---predicting RL--SFT complementarity.
22	Our results qualify this prediction: the asymmetry manifests as a recovery capacity difference (the spectrum), but the expected accuracy complementarity disappears when pruning preserves representational diversity ($|\Delta| \leq 1.34$\,pp on GSM8K and MBPP; \S\ref{sec:decoupling}).
23	RL training instability has been studied in the RLHF context: \citet{gao2023overoptimization} characterize reward overoptimization, \citet{dong2025rlplus} document repetitive output collapse during extended RL training, and \citet{shah2025comedy} analyze compounding bias from reward estimation.
24	\citet{mukherjee2025rlsubnetworks} show that RL fine-tuning updates only 5--30\% of parameters, raising the question of whether pruning criteria interact with this active subnetwork.
25	Our work connects this instability literature to structural pruning, showing that the pruning criterion shapes susceptibility to RL collapse.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdcf9bb5-c1f5-45ad-88bc-65b4e785f0a4",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "6e63bd73-bfc9-4a91-b570-aebbf9ea86a7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Structured pruning of LLMs.}\nLLM-Pruner~\\citep{llmpruner2023} introduced dependency-aware structural pruning for transformers; Bonsai~\\citep{bonsai2025} achieves competitive results using only forward passes; GRASPrune~\\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups.\nShortGPT~\\citep{shortgpt2024}, SliceGPT~\\citep{slicegpt2024}, and LaCo~\\citep{yang2024laco} target depth pruning, though \\citet{shrestha2026layerpruninglimits} show this causes severe reasoning degradation even when classification is preserved; Wanda~\\citep{wanda2024} addresses unstructured sparsity; \\citet{doingmore2026} revisit the structured-vs-unstructured trade-off under test-time scaling.\nFor reasoning models, RESP~\\citep{resp2025} uses gradient-based importance on self-generated reasoning traces, RAC~\\citep{rac2025} reconstructs chain-of-thought during pruning, SSGR~\\citep{ssgr2025} uses self-generated calibration data, and \\citet{llms2lrms2026} find width pruning more robust than depth pruning for reasoning but do not study RLVR recovery.\nA parallel line recognizes that functional structure should guide pruning: FANG~\\citep{fang_2025} groups FFN neurons by activation clusters, FuncNet~\\citep{funcnet_2025} decomposes LLMs via ICA, and MPruner~\\citep{mpruner2024} uses inter-layer CKA~\\citep{kornblith2019cka} for depth pruning in CNNs.\nOur work uses \\emph{intra-layer} CKA between individual structures at a finer granularity, optimizing for RL recovery capacity rather than immediate accuracy preservation.\n\n\\paragraph{Pruning-aware recovery.}\n\\citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, significantly outperforming SFT, but evaluate only importance-based pruning; our controlled experiments demonstrate that this RLVR${>}$SFT advantage vanishes under diversity-preserving pruning---it is a property of the pruning criterion, not of RL training itself.\nWe note that our experiments use different models and tasks than \\citet{selfhealing2025}; the finding may not transfer to their exact setup.\n$P^2$ Law~\\citep{p2law2025} establishes scaling laws for post-training loss after pruning.\nPASER~\\citep{paser2025} optimizes recovery data selection, PAT~\\citep{pat2025} jointly considers pruning and fine-tuning objectives, RestoreLCC~\\citep{restorelcc_2025} contrastively probes critical attention heads for post-hoc compensation, \\citet{boiling_frog_2026} adopt iterative prune-tune loops for gradual compression, and OPSD~\\citep{opsd2026} compresses reasoning models \\emph{after} RLVR (the reverse of our pipeline).\nARRoL~\\citep{xu2026arrol} prunes rollouts during RLVR generation for training efficiency.\nThese approaches optimize complementary axes; our work isolates which \\emph{pruning criterion} enables RL-based recovery.\nThe Lottery Ticket Hypothesis~\\citep{frankle2019lth} asks which subnetworks train effectively from random initialization; our recovery capacity spectrum extends this to \\emph{paradigm-conditioned trainability}, where the optimal subnetwork depends on the recovery paradigm (RLVR vs.\\ SFT).\n\n\\paragraph{RLVR training dynamics.}\n\\citet{rlsqueezes2026} show that RLVR \\emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \\emph{expands} correct ones via local imitation---predicting RL--SFT complementarity.\nOur results qualify this prediction: the asymmetry manifests as a recovery capacity difference (the spectrum), but the expected accuracy complementarity disappears when pruning preserves representational diversity ($|\\Delta| \\leq 1.34$\\,pp on GSM8K and MBPP; \\S\\ref{sec:decoupling}).\nRL training instability has been studied in the RLHF context: \\citet{gao2023overoptimization} characterize reward overoptimization, \\citet{dong2025rlplus} document repetitive output collapse during extended RL training, and \\citet{shah2025comedy} analyze compounding bias from reward estimation.\n\\citet{mukherjee2025rlsubnetworks} show that RL fine-tuning updates only 5--30\\% of parameters, raising the question of whether pruning criteria interact with this active subnetwork.\nOur work connects this instability literature to structural pruning, showing that the pruning criterion shapes susceptibility to RL collapse.\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  },
  "sourceToolAssistantUUID": "bdcf9bb5-c1f5-45ad-88bc-65b4e785f0a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T04:05:37.306Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TQDRVxZijy9dxd4bhE3F5a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e63bd73-bfc9-4a91-b570-aebbf9ea86a7",
  "isSidechain": false,
  "requestId": "req_011CbJqe8RAU8hhy9mDRfdxH",
  "type": "assistant",
  "uuid": "f4eebc2a-d546-4a2b-9b9f-0887fa01228f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AikNj8BwKMU39MmHyboKMo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12647,
      "cache_read_input_tokens": 38782,
      "output_tokens": 801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 801,
          "cache_read_input_tokens": 38782,
          "cache_creation_input_tokens": 12647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12647
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-23T04:05:37.315Z_

<details><summary>↩ Tool result · `toolu_01TQDRVxZijy9dxd4bhE3F5a`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We design a controlled comparison framework to isolate the effect of pruning criterion on post-RLVR recovery capacity.
5	The framework consists of three components: (1) shared structural analysis that computes importance and functional overlap scores for all prunable structures, (2) four scoring criteria that combine these scores differently to select structures for removal, and (3) an identical two-stage recovery pipeline applied to all pruned models.
6	By varying only the scoring criterion while holding all other factors constant, we can attribute differences in GRPO training dynamics directly to the pruning decision.
7	
8	\subsection{Preliminaries and Notation}
9	\label{sec:prelim}
10	
11	\paragraph{Structured pruning.}
12	Given a pretrained transformer $\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units (attention heads or MLP channels) to reduce model size while maintaining hardware-friendly dense computation.
13	We denote the set of prunable structures as $\mathcal{H} = \{h_1, h_2, \ldots, h_N\}$.
14	
15	\paragraph{Grouped Query Attention (GQA).}
16	In GQA architectures~\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads ($G = n_Q / n_{KV}$ per group).
17	For DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$, $G{=}7$), we treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit.
18	
19	\paragraph{RLVR and GRPO.}
20	Reinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.
21	We use Group Relative Policy Optimization (GRPO;~\citealp{shao2024grpo}) as the recovery algorithm.
22	
23	\subsection{Structural Analysis}
24	\label{sec:structural_analysis}
25	
26	All four pruning criteria share a common structural analysis stage that computes two scores per structure: \emph{importance} $I(h)$ capturing the structure's contribution to reasoning, and \emph{functional overlap} $F(h)$ measuring representational redundancy with other structures in the same layer.
27	
28	\paragraph{Calibration data.}
29	We compute importance and overlap scores on chain-of-thought reasoning data from GSM8K~\citep{cobbe2021gsm8k} training examples.
30	Given a calibration set $\mathcal{D}_\text{cal} = \{(x_j, y_j)\}_{j=1}^{M}$, we compute activations and gradients on the concatenated sequences $(x_j, y_j)$.
31	
32	\paragraph{Structural importance.}
33	For each structure $h$ with activation $\mathbf{a}_h$, we approximate the loss change from removal via first-order Taylor expansion ($\Delta\mathcal{L} \approx -\mathbf{a}_h^\top \nabla_{\mathbf{a}_h}\mathcal{L}$, dropping $O(\|\mathbf{a}_h\|^2)$ terms) and aggregate over the calibration set:
34	\begin{equation}
35	    I(h) = \left| \sum_{(x,y) \in \mathcal{D}_\text{cal}} \mathbf{a}_h(x, y)^\top \frac{\partial \mathcal{L}(x, y)}{\partial \mathbf{a}_h} \right|,
36	    \label{eq:importance}
37	\end{equation}
38	where $\mathcal{L}$ is the language modeling loss over the reasoning trace.
39	For a GQA group $g$ containing Q heads $\{q_1, \ldots, q_G\}$ and KV head $k$, we aggregate: $I(g) = \sum_{i=1}^{G} I(q_i) + I(k)$.
40	
41	\paragraph{Functional overlap via CKA.}
42	We measure functional overlap using linear Centered Kernel Alignment (CKA;~\citealp{kornblith2019cka}), which quantifies similarity between two sets of representations invariant to invertible linear transformations.
43	Given activation matrices $\mathbf{X}, \mathbf{Y} \in \mathbb{R}^{n \times d}$ collected over $n$ calibration examples, linear CKA is:
44	\begin{equation}
45	    \text{CKA}(\mathbf{X}, \mathbf{Y}) = \frac{\text{HSIC}(\mathbf{X}, \mathbf{Y})}{\sqrt{\text{HSIC}(\mathbf{X}, \mathbf{X}) \cdot \text{HSIC}(\mathbf{Y}, \mathbf{Y})}},
46	    \label{eq:cka}
47	\end{equation}
48	where $\text{HSIC}(\mathbf{X}, \mathbf{Y}) = \frac{1}{(n-1)^2} \operatorname{tr}(\mathbf{K} \mathbf{H} \mathbf{L} \mathbf{H})$, with $\mathbf{K} = \mathbf{X}\mathbf{X}^\top$, $\mathbf{L} = \mathbf{Y}\mathbf{Y}^\top$, and $\mathbf{H} = \mathbf{I}_n - \frac{1}{n}\mathbf{1}\mathbf{1}^\top$.
49	
50	For a GQA group $g_i$ in layer $\ell$, we form its representation by concatenating its constituent Q head activations: $\mathbf{X}_{g_i} = [\mathbf{a}_{q_1}; \ldots; \mathbf{a}_{q_G}] \in \mathbb{R}^{n \times Gd_h}$.
51	The functional overlap of $g_i$ is the mean pairwise CKA with other groups in the same layer:
52	\begin{equation}
53	    F(g_i) = \frac{1}{|\mathcal{G}_\ell| - 1} \sum_{\substack{g_j \in \mathcal{G}_\ell \\ j \neq i}} \text{CKA}(\mathbf{X}_{g_i}, \mathbf{X}_{g_j}).
54	    \label{eq:overlap}
55	\end{equation}
56	We apply the same intra-layer CKA overlap to MLP channel groups, partitioning each MLP intermediate dimension into equal-sized groups.
57	Unlike prior work that uses inter-layer CKA to identify globally redundant layers for depth pruning~\citep{mpruner2024,lachance2022cka}, we use \emph{intra-layer} CKA between individual structures to measure per-structure functional redundancy.
58	Computing all pairwise CKA scores adds negligible overhead ($O(L \cdot k^2)$, $k \le 28$; $<$2 min on one GPU).
59	
60	\paragraph{CKA reliability.}
61	Our intra-layer use of linear CKA between structures of identical dimensionality avoids the kernel width and layer width sensitivities identified by \citet{davari2023cka,klabunde_similarity_survey_2023}; empirically, structure rankings are stable across calibration sizes (Spearman $\rho \geq 0.964$; Appendix~\ref{sec:appendix_cka_stability}).
62	
63	\subsection{Pruning Scoring Criteria}
64	\label{sec:scoring}
65	
66	We compare four scoring criteria that combine importance $I(h)$ and functional overlap $F(h)$ in different ways.
67	All four methods use the same per-layer capacity floor (${\ge}$40\% of MLP groups per layer must be retained, chosen to prevent any single layer from becoming a throughput bottleneck) and global ranking procedure: structures are sorted by score, and the lowest-scoring structures are pruned up to the target sparsity ratio, skipping any candidate whose removal would violate the layer floor.
68	
69	\paragraph{Standard (importance-only).}
70	Following LLM-Pruner~\citep{llmpruner2023}, structures are ranked solely by importance:
71	\begin{equation}
72	    S_\text{std}(h) = I(h).
73	    \label{eq:standard}
74	\end{equation}
75	This is the industry-standard criterion that retains gradient-important structures and removes ``unimportant'' ones.
76	
77	\paragraph{RASP (recovery-aware composite).}
78	The recovery-aware score combines importance and functional overlap:
79	\begin{equation}
80	    S_\text{rasp}(h) = I(h) \times \big(1 - F(h)\big)^\alpha,
81	    \label{eq:score}
82	\end{equation}
83	where $\alpha \ge 0$ controls the strength of the overlap penalty ($\alpha{=}0$ reduces to Standard).
84	Structures with high importance \emph{and} low overlap receive the highest scores and are retained; structures with high overlap are penalized and pruned preferentially, regardless of their importance.
85	
86	\paragraph{CKA-only (overlap-only).}
87	CKA-only scoring ignores gradient importance entirely, ranking structures by functional overlap alone.
88	Structures with the highest mean pairwise CKA similarity to other structures in their layer are removed first:
89	\begin{equation}
90	    S_\text{cka}(h) = 1 - F(h).
91	    \label{eq:cka_only}
92	\end{equation}
93	This criterion preserves all representationally unique structures regardless of their gradient importance, removing only those whose function is redundant with retained structures.
94	$S_\text{cka}$ corresponds to the limit $\alpha \to \infty$ in Eq.~\ref{eq:score}.
95	
96	\paragraph{Random.}
97	Structures are selected uniformly at random for removal, subject to the per-layer capacity floor.
98	This baseline controls for the effect of any informed scoring criterion.
99	
100	The four criteria span a spectrum from pure gradient importance (Standard) to pure representational diversity preservation (CKA-only), with RASP as a weighted interpolation and Random as an uninformed control.
101	The key distinction is that CKA-only protects \emph{functionally unique} structures regardless of gradient contribution: structures deemed ``unimportant'' by gradient metrics may provide non-redundant computational pathways essential for RL exploration~\citep{rlsqueezes2026}.
102	
103	\subsection{Two-Stage Recovery}
104	\label{sec:recovery}
105	
106	After pruning, all four models undergo an identical two-stage recovery pipeline. Any differences in GRPO training dynamics are therefore attributable to the pruning criterion alone.
107	
108	\paragraph{Stage 1: SFT warmup.}
109	Structured pruning disrupts the model's ability to generate end-of-sequence (EOS) tokens: in sampling mode, pruned models produce repetitive outputs without termination.
110	Since GRPO computes rewards only from completed generations, this EOS collapse makes direct RLVR recovery impossible.
111	We restore generation competence through a short SFT phase on chain-of-thought reasoning demonstrations with teacher forcing.
112	This stage is intentionally brief: its purpose is to restore the minimal capabilities (EOS generation, format compliance) needed for GRPO, not to recover full reasoning ability.
113	
114	\paragraph{Stage 2: GRPO alignment.}
115	With generation competence restored, we apply GRPO on mathematical reasoning problems with binary reward ($r{=}1$ if the final answer matches the ground truth, $r{=}0$ otherwise).
116	RLVR is preferred over extended SFT for reasoning recovery because of their fundamentally different training dynamics: \citet{rlsqueezes2026} show that RLVR \emph{compresses} incorrect reasoning trajectories while SFT \emph{expands} correct ones.
117	For a pruned model, RLVR can globally explore and redistribute functionality across remaining structures, while SFT is limited to imitating fixed trajectories through a reduced architecture.
118	The GRPO configuration (learning rate, KL coefficient, sampling temperature, loss formulation) is held constant across all four pruned models (Section~\ref{sec:exp_setup}).
119	
120	\subsection{Recovery Capacity Diagnostics}
121	\label{sec:diagnostics}
122	
123	We define \textbf{recovery capacity} as the model's ability to benefit from post-pruning recovery training, operationalized in our GRPO experiments as peak mean reward over the training horizon (Table~\ref{tab:recovery_gradient}).
124	We track four diagnostic measures---mean reward, zero-variance batch fraction ($f_0$), gradient norm, and KL divergence---to distinguish \emph{active learning} (rising reward, low $f_0$), \emph{stagnation} (flat reward), and \emph{collapse} (declining reward, high $f_0$, vanishing gradients).
125	
126	The complete pruning comparison procedure is given in Algorithm~\ref{alg:rasp} (Appendix~\ref{sec:appendix_algo}).
127	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4eebc2a-d546-4a2b-9b9f-0887fa01228f",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "d9dd7abd-46c3-440e-8701-3f5ccdfff5c5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nWe design a controlled comparison framework to isolate the effect of pruning criterion on post-RLVR recovery capacity.\nThe framework consists of three components: (1) shared structural analysis that computes importance and functional overlap scores for all prunable structures, (2) four scoring criteria that combine these scores differently to select structures for removal, and (3) an identical two-stage recovery pipeline applied to all pruned models.\nBy varying only the scoring criterion while holding all other factors constant, we can attribute differences in GRPO training dynamics directly to the pruning decision.\n\n\\subsection{Preliminaries and Notation}\n\\label{sec:prelim}\n\n\\paragraph{Structured pruning.}\nGiven a pretrained transformer $\\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units (attention heads or MLP channels) to reduce model size while maintaining hardware-friendly dense computation.\nWe denote the set of prunable structures as $\\mathcal{H} = \\{h_1, h_2, \\ldots, h_N\\}$.\n\n\\paragraph{Grouped Query Attention (GQA).}\nIn GQA architectures~\\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads ($G = n_Q / n_{KV}$ per group).\nFor DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$, $G{=}7$), we treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit.\n\n\\paragraph{RLVR and GRPO.}\nReinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.\nWe use Group Relative Policy Optimization (GRPO;~\\citealp{shao2024grpo}) as the recovery algorithm.\n\n\\subsection{Structural Analysis}\n\\label{sec:structural_analysis}\n\nAll four pruning criteria share a common structural analysis stage that computes two scores per structure: \\emph{importance} $I(h)$ capturing the structure's contribution to reasoning, and \\emph{functional overlap} $F(h)$ measuring representational redundancy with other structures in the same layer.\n\n\\paragraph{Calibration data.}\nWe compute importance and overlap scores on chain-of-thought reasoning data from GSM8K~\\citep{cobbe2021gsm8k} training examples.\nGiven a calibration set $\\mathcal{D}_\\text{cal} = \\{(x_j, y_j)\\}_{j=1}^{M}$, we compute activations and gradients on the concatenated sequences $(x_j, y_j)$.\n\n\\paragraph{Structural importance.}\nFor each structure $h$ with activation $\\mathbf{a}_h$, we approximate the loss change from removal via first-order Taylor expansion ($\\Delta\\mathcal{L} \\approx -\\mathbf{a}_h^\\top \\nabla_{\\mathbf{a}_h}\\mathcal{L}$, dropping $O(\\|\\mathbf{a}_h\\|^2)$ terms) and aggregate over the calibration set:\n\\begin{equation}\n    I(h) = \\left| \\sum_{(x,y) \\in \\mathcal{D}_\\text{cal}} \\mathbf{a}_h(x, y)^\\top \\frac{\\partial \\mathcal{L}(x, y)}{\\partial \\mathbf{a}_h} \\right|,\n    \\label{eq:importance}\n\\end{equation}\nwhere $\\mathcal{L}$ is the language modeling loss over the reasoning trace.\nFor a GQA group $g$ containing Q heads $\\{q_1, \\ldots, q_G\\}$ and KV head $k$, we aggregate: $I(g) = \\sum_{i=1}^{G} I(q_i) + I(k)$.\n\n\\paragraph{Functional overlap via CKA.}\nWe measure functional overlap using linear Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}), which quantifies similarity between two sets of representations invariant to invertible linear transformations.\nGiven activation matrices $\\mathbf{X}, \\mathbf{Y} \\in \\mathbb{R}^{n \\times d}$ collected over $n$ calibration examples, linear CKA is:\n\\begin{equation}\n    \\text{CKA}(\\mathbf{X}, \\mathbf{Y}) = \\frac{\\text{HSIC}(\\mathbf{X}, \\mathbf{Y})}{\\sqrt{\\text{HSIC}(\\mathbf{X}, \\mathbf{X}) \\cdot \\text{HSIC}(\\mathbf{Y}, \\mathbf{Y})}},\n    \\label{eq:cka}\n\\end{equation}\nwhere $\\text{HSIC}(\\mathbf{X}, \\mathbf{Y}) = \\frac{1}{(n-1)^2} \\operatorname{tr}(\\mathbf{K} \\mathbf{H} \\mathbf{L} \\mathbf{H})$, with $\\mathbf{K} = \\mathbf{X}\\mathbf{X}^\\top$, $\\mathbf{L} = \\mathbf{Y}\\mathbf{Y}^\\top$, and $\\mathbf{H} = \\mathbf{I}_n - \\frac{1}{n}\\mathbf{1}\\mathbf{1}^\\top$.\n\nFor a GQA group $g_i$ in layer $\\ell$, we form its representation by concatenating its constituent Q head activations: $\\mathbf{X}_{g_i} = [\\mathbf{a}_{q_1}; \\ldots; \\mathbf{a}_{q_G}] \\in \\mathbb{R}^{n \\times Gd_h}$.\nThe functional overlap of $g_i$ is the mean pairwise CKA with other groups in the same layer:\n\\begin{equation}\n    F(g_i) = \\frac{1}{|\\mathcal{G}_\\ell| - 1} \\sum_{\\substack{g_j \\in \\mathcal{G}_\\ell \\\\ j \\neq i}} \\text{CKA}(\\mathbf{X}_{g_i}, \\mathbf{X}_{g_j}).\n    \\label{eq:overlap}\n\\end{equation}\nWe apply the same intra-layer CKA overlap to MLP channel groups, partitioning each MLP intermediate dimension into equal-sized groups.\nUnlike prior work that uses inter-layer CKA to identify globally redundant layers for depth pruning~\\citep{mpruner2024,lachance2022cka}, we use \\emph{intra-layer} CKA between individual structures to measure per-structure functional redundancy.\nComputing all pairwise CKA scores adds negligible overhead ($O(L \\cdot k^2)$, $k \\le 28$; $<$2 min on one GPU).\n\n\\paragraph{CKA reliability.}\nOur intra-layer use of linear CKA between structures of identical dimensionality avoids the kernel width and layer width sensitivities identified by \\citet{davari2023cka,klabunde_similarity_survey_2023}; empirically, structure rankings are stable across calibration sizes (Spearman $\\rho \\geq 0.964$; Appendix~\\ref{sec:appendix_cka_stability}).\n\n\\subsection{Pruning Scoring Criteria}\n\\label{sec:scoring}\n\nWe compare four scoring criteria that combine importance $I(h)$ and functional overlap $F(h)$ in different ways.\nAll four methods use the same per-layer capacity floor (${\\ge}$40\\% of MLP groups per layer must be retained, chosen to prevent any single layer from becoming a throughput bottleneck) and global ranking procedure: structures are sorted by score, and the lowest-scoring structures are pruned up to the target sparsity ratio, skipping any candidate whose removal would violate the layer floor.\n\n\\paragraph{Standard (importance-only).}\nFollowing LLM-Pruner~\\citep{llmpruner2023}, structures are ranked solely by importance:\n\\begin{equation}\n    S_\\text{std}(h) = I(h).\n    \\label{eq:standard}\n\\end{equation}\nThis is the industry-standard criterion that retains gradient-important structures and removes ``unimportant'' ones.\n\n\\paragraph{RASP (recovery-aware composite).}\nThe recovery-aware score combines importance and functional overlap:\n\\begin{equation}\n    S_\\text{rasp}(h) = I(h) \\times \\big(1 - F(h)\\big)^\\alpha,\n    \\label{eq:score}\n\\end{equation}\nwhere $\\alpha \\ge 0$ controls the strength of the overlap penalty ($\\alpha{=}0$ reduces to Standard).\nStructures with high importance \\emph{and} low overlap receive the highest scores and are retained; structures with high overlap are penalized and pruned preferentially, regardless of their importance.\n\n\\paragraph{CKA-only (overlap-only).}\nCKA-only scoring ignores gradient importance entirely, ranking structures by functional overlap alone.\nStructures with the highest mean pairwise CKA similarity to other structures in their layer are removed first:\n\\begin{equation}\n    S_\\text{cka}(h) = 1 - F(h).\n    \\label{eq:cka_only}\n\\end{equation}\nThis criterion preserves all representationally unique structures regardless of their gradient importance, removing only those whose function is redundant with retained structures.\n$S_\\text{cka}$ corresponds to the limit $\\alpha \\to \\infty$ in Eq.~\\ref{eq:score}.\n\n\\paragraph{Random.}\nStructures are selected uniformly at random for removal, subject to the per-layer capacity floor.\nThis baseline controls for the effect of any informed scoring criterion.\n\nThe four criteria span a spectrum from pure gradient importance (Standard) to pure representational diversity preservation (CKA-only), with RASP as a weighted interpolation and Random as an uninformed control.\nThe key distinction is that CKA-only protects \\emph{functionally unique} structures regardless of gradient contribution: structures deemed ``unimportant'' by gradient metrics may provide non-redundant computational pathways essential for RL exploration~\\citep{rlsqueezes2026}.\n\n\\subsection{Two-Stage Recovery}\n\\label{sec:recovery}\n\nAfter pruning, all four models undergo an identical two-stage recovery pipeline. Any differences in GRPO training dynamics are therefore attributable to the pruning criterion alone.\n\n\\paragraph{Stage 1: SFT warmup.}\nStructured pruning disrupts the model's ability to generate end-of-sequence (EOS) tokens: in sampling mode, pruned models produce repetitive outputs without termination.\nSince GRPO computes rewards only from completed generations, this EOS collapse makes direct RLVR recovery impossible.\nWe restore generation competence through a short SFT phase on chain-of-thought reasoning demonstrations with teacher forcing.\nThis stage is intentionally brief: its purpose is to restore the minimal capabilities (EOS generation, format compliance) needed for GRPO, not to recover full reasoning ability.\n\n\\paragraph{Stage 2: GRPO alignment.}\nWith generation competence restored, we apply GRPO on mathematical reasoning problems with binary reward ($r{=}1$ if the final answer matches the ground truth, $r{=}0$ otherwise).\nRLVR is preferred over extended SFT for reasoning recovery because of their fundamentally different training dynamics: \\citet{rlsqueezes2026} show that RLVR \\emph{compresses} incorrect reasoning trajectories while SFT \\emph{expands} correct ones.\nFor a pruned model, RLVR can globally explore and redistribute functionality across remaining structures, while SFT is limited to imitating fixed trajectories through a reduced architecture.\nThe GRPO configuration (learning rate, KL coefficient, sampling temperature, loss formulation) is held constant across all four pruned models (Section~\\ref{sec:exp_setup}).\n\n\\subsection{Recovery Capacity Diagnostics}\n\\label{sec:diagnostics}\n\nWe define \\textbf{recovery capacity} as the model's ability to benefit from post-pruning recovery training, operationalized in our GRPO experiments as peak mean reward over the training horizon (Table~\\ref{tab:recovery_gradient}).\nWe track four diagnostic measures---mean reward, zero-variance batch fraction ($f_0$), gradient norm, and KL divergence---to distinguish \\emph{active learning} (rising reward, low $f_0$), \\emph{stagnation} (flat reward), and \\emph{collapse} (declining reward, high $f_0$, vanishing gradients).\n\nThe complete pruning comparison procedure is given in Algorithm~\\ref{alg:rasp} (Appendix~\\ref{sec:appendix_algo}).\n",
      "numLines": 127,
      "startLine": 1,
      "totalLines": 127
    }
  },
  "sourceToolAssistantUUID": "f4eebc2a-d546-4a2b-9b9f-0887fa01228f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T04:05:37.775Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QFuJFm4tdN7gLMM4CdN6Ce`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9dd7abd-46c3-440e-8701-3f5ccdfff5c5",
  "isSidechain": false,
  "requestId": "req_011CbJqe8RAU8hhy9mDRfdxH",
  "type": "assistant",
  "uuid": "ab867b27-9276-4a85-92cd-85023544aec9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AikNj8BwKMU39MmHyboKMo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12647,
      "cache_read_input_tokens": 38782,
      "output_tokens": 801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 801,
          "cache_read_input_tokens": 38782,
          "cache_creation_input_tokens": 12647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12647
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-23T04:05:37.780Z_

<details><summary>↩ Tool result · `toolu_01QFuJFm4tdN7gLMM4CdN6Ce`</summary>

```text
1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	\subsection{Experimental Setup}
6	\label{sec:exp_setup}
7	
8	\paragraph{Base model and evaluation.}
9	We evaluate on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\citep{qwen2.5} with GQA~\citep{ainslie2023gqa} (architecture details in Section~\ref{sec:prelim}).
10	Our primary benchmark is GSM8K~\citep{cobbe2021gsm8k}, a set of 1{,}319 grade-school math problems requiring multi-step arithmetic reasoning.
11	We report exact-match accuracy: the final numerical answer is extracted from the model's generation and compared against the ground truth.
12	For rapid iteration during development, we use a 100-problem subset ($N{=}100$); final results use the full test set ($N{=}1{,}319$).
13	The original unpruned model achieves 90.83\% on GSM8K (greedy decoding).
14	
15	\paragraph{Pruning methods.}
16	We compare four pruning criteria at 20\% structured sparsity, all removing the same number of MLP channel groups (200 of 784 across 28 layers, ${\sim}$1.45B parameters) with identical per-layer capacity floors (${\ge}$40\% retention per layer):
17	\begin{enumerate}[nosep,leftmargin=*]
18	    \item \textbf{CKA-only}: structures ranked by functional overlap $F(h)$ alone (Eq.~\ref{eq:overlap}); the most redundant groups are removed regardless of gradient importance.
19	    \item \textbf{Random}: uniform random selection among eligible groups.
20	    \item \textbf{Standard}: Taylor-expansion importance $I(h)$ alone (Eq.~\ref{eq:importance}); the least important groups are removed, following LLM-Pruner~\citep{llmpruner2023}.
21	    \item \textbf{\rasp{}} ($\alpha{=}1.0$): the composite score $S(h) = I(h) \times (1 - F(h))^\alpha$ (Eq.~\ref{eq:score}), removing structures that are both low-importance and functionally redundant.
22	\end{enumerate}
23	
24	\paragraph{Recovery pipeline and hardware.}
25	All four methods undergo matched two-stage recovery.
26	Stage~1 (SFT warmup): 2 epochs on 7{,}473 GSM8K chain-of-thought examples with teacher forcing (37 minutes), restoring EOS generation and basic format compliance.
27	Stage~2 (GRPO): Group Relative Policy Optimization~\citep{shao2024grpo} with learning rate $1{\times}10^{-6}$, maximum completion length 1{,}024 tokens, KL penalty coefficient $\beta{=}0.01$, sampling temperature 0.4, DAPO-style clipped loss, and binary reward ($r{=}1$ if correct, $r{=}0$ otherwise), trained for 100 steps on 1{,}000 GSM8K training problems.
28	All methods share identical GRPO hyperparameters, including \texttt{reward\_desert\_patience}{$=$}50.
29	Seeds vary at the GRPO stage; pruning calibration and SFT use identical configurations across all methods.
30	We repeat GRPO training with 3 random seeds for CKA-only, Standard, and Random (Table~\ref{tab:decoupling}).
31	CKA-only achieves 64.39\% $\pm$ 0.19\,pp (std across seeds), Standard 59.84\% $\pm$ 0.38\,pp; the 4.55\,pp gap is robust across seeds (Welch's $t$-test, $p{=}0.0009$, Cohen's $d{=}11.1$; 95\% CI for mean difference: $[3.62, 5.47]$\,pp), confirming that recovery capacity differences are structural rather than stochastic.
32	All experiments run on 2$\times$ NVIDIA RTX PRO 6000 GPUs (94\,GB VRAM each); pruning variants are trained in parallel on separate GPUs under identical wall-clock conditions.
33	
34	
35	\subsection{Recovery Capacity Spectrum}
36	\label{sec:recovery_gradient}
37	
38	\input{tables/tab1_recovery_gradient}
39	
40	\begin{figure}[t]
41	    \centering
42	    \includegraphics[width=\columnwidth]{figures/paper/fig2_reward_trajectories.pdf}
43	    \caption{GRPO reward trajectories for four pruning criteria and the unpruned model under identical training configuration ($\beta{=}0.01$, $T{=}0.4$, 100 steps). CKA-only reaches 0.354 peak reward with an observed recovery event at step 90. Random oscillates between 0.14 and 0.19 (training timed out at step 97; 9 steps shown). Standard peaks at 0.081 before borderline collapse. \rasp{} peaks at 0.061 (step 50) and declines to 0.010 by step 100.}
44	    \label{fig:reward_trajectories}
45	\end{figure}
46	
47	The central finding is that the pruning criterion determines post-RLVR recovery capacity.
48	Under controlled GRPO training with identical hyperparameters, the four pruning criteria produce qualitatively distinct training dynamics that form a clear recovery capacity spectrum: CKA-only $\gg$ Random $\gg$ Standard $>$ \rasp{}.
49	Table~\ref{tab:recovery_gradient} summarizes the key metrics, and Figure~\ref{fig:reward_trajectories} shows the reward trajectories over 100 GRPO steps.
50	
51	\begin{figure}[t]
52	    \centering
53	    \includegraphics[width=\columnwidth]{figures/paper/fig3_collapse_dynamics.pdf}
54	    \caption{Training dynamics diagnostics. (a)~$f_0$ (fraction of zero-variance batches): CKA-only stays below 0.35; Standard and \rasp{} remain in the collapse zone ($f_0 > 0.5$) throughout training. (b)~Gradient norm: Standard exhibits a transient minimum of 0.017 at step 90 before recovering to 2.41 at step 100; \rasp{} gradient norms remain predominantly near zero.}
55	    \label{fig:collapse_dynamics}
56	\end{figure}
57	
58	CKA-only pruning is the only method that produces active learning under GRPO.
59	Reward reaches a peak of 0.354 (mean 0.285) with $f_0$ as low as 0.125, including a recovery event at step 90 where reward rebounds from a transient perturbation.
60	Random pruning produces stagnation: reward oscillates between 0.142 and 0.190 with $f_0$ near 0.33.
61	
62	Standard pruning exhibits borderline collapse (Figure~\ref{fig:collapse_dynamics}): reward peaks at 0.081 (step 40) then oscillates near 0.05, with $f_0 \geq 0.500$ throughout---more than half of batches produce no learning signal.
63	\rasp{} produces full collapse: reward peaks at 0.061 (step 50) then declines to 0.010 by step 100, with $f_0 > 0.675$ and clipped ratio $>$ 90\%.
64	
65	The 5.8$\times$ peak reward gap (CKA-only 0.354 vs \rasp{} 0.061) arises from models pruned to identical parameter budgets with identical GRPO configurations; the only variable is which structures were removed.
66	
67	
68	\subsection{Reward-Accuracy Decoupling}
69	\label{sec:decoupling}
70	
71	\input{tables/tab2_decoupling}
72	
73	GRPO reward trajectory reflects training capacity---the model's ability to learn from RL signal---not downstream accuracy, a phenomenon we term \emph{reward-accuracy decoupling} (mean $|\Delta| {=} 0.54$\,pp, max $1.14$\,pp on GSM8K across all fine-grained criteria and sparsity levels).
74	At 20\% sparsity, accuracy changes are small across all pruned methods ($|\Delta| < 1$\,pp: CKA-only $+$0.48, Standard $+$0.55, Random $-$0.53, \rasp{} $-$0.61\,pp; Table~\ref{tab:decoupling}) despite the 4.4$\times$ peak reward gap.
75	
76	The degree of decoupling varies with sparsity.
77	At 15\% (3-seed GRPO), SFT establishes a 5.69\,pp gap between CKA-only and Standard (72.18\% vs 66.49\%; single SFT seed), which GRPO maintains or slightly amplifies to 7.20\,pp (72.76\% vs 65.56\%; Welch's $t$-test, $p{<}0.001$).
78	At 20\%, the differential GRPO contribution is negligible: SFT establishes a 4.62\,pp gap that GRPO preserves (4.55\,pp).
79	At 25\% (single seed), decoupling is most extreme: Standard's peak reward collapses to 0.008 yet accuracy changes by only $+$0.99\,pp (Appendix~\ref{sec:appendix_cross_sparsity}).
80	Across all four fine-grained pruning criteria and both sparsity levels tested (20\% and 25\%), $|\Delta| < 1$\,pp without exception on GSM8K (Tables~\ref{tab:decoupling},~\ref{tab:cross_sparsity}); on MATH-500, SFT--GRPO differences remain within statistical noise (all $|\Delta| < 2.5$\,pp with stderr ${\approx}$2\,pp per condition; Appendix~\ref{sec:appendix_math500}).
81	This pattern suggests that moderate structural damage (15\%) preserves enough capacity for GRPO to differentially benefit CKA-only pruning, while more aggressive pruning (20--25\%) exceeds the threshold where GRPO can improve upon SFT baselines.
82	
83	CKA-only GRPO accuracy is reproducible across three random seeds (64.22--64.58\%, observed range 0.36\,pp; Appendix~\ref{sec:appendix_multiseed}).
84	Extended training to 300 steps at 20\% confirms: accuracy remains unchanged (CKA-only 64.37\%$\to$64.37\%, Standard 59.44\%$\to$59.29\%; single seed).
85	The pruning-criterion ranking transfers to MATH-500~\citep{hendrycks2021math} (SFT: CKA-only 26.8\% vs Standard 25.8\% vs \rasp{} 21.2\% vs Random 14.4\%; Appendix~\ref{sec:appendix_math500}), and decoupling holds across HumanEval~\citep{chen2021humaneval} and MBPP~\citep{austin2021mbpp} (all fine-grained GRPO $|\Delta| < 2$\,pp; MBPP deltas are uniformly slightly positive but within stderr; Appendix~\ref{sec:appendix_mbpp}).
86	\label{sec:ood}
87	ShortGPT~\citep{shortgpt2024} depth pruning is the exception: GRPO interaction is task-dependent ($-$1.36\,pp on GSM8K, $+$4.01\,pp on MBPP; Tables~\ref{tab:decoupling},~\ref{tab:mbpp}), unlike the uniformly neutral deltas of fine-grained methods ($|\Delta| \leq 1.34$\,pp).
88	The cross-benchmark maximum comes from MBPP (Table~\ref{tab:mbpp}); the GSM8K maximum is $1.14$\,pp (Table~\ref{tab:alpha}).
89	
90	
91	\subsection{Additional Results}
92	\label{sec:additional_results}
93	
94	\paragraph{Post-SFT accuracy does not predict GRPO outcome.}
95	\label{sec:sft_gradient}
96	Under SFT alone, CKA-only (63.91\%) $>$ \rasp{} (61.49\%) $>$ Standard (59.29\%) $>$ Random (51.25\%), yet under GRPO the \rasp{}/Standard ordering reverses (peak 0.081 vs 0.061) and Random outperforms both in peak reward (0.190).
97	More strikingly, ShortGPT post-SFT (44.73\%) shows GRPO actively harming accuracy ($-$1.36\,pp), while unstructured pruning achieves the highest post-SFT accuracy (87.87\%) with GRPO accuracy 87.64\% ($\Delta{=}{-}0.23$\,pp), confirming that pruning criteria are irrelevant when structural damage is minimal (96.5\% dense retention).
98	Post-SFT accuracy does not monotonically determine GRPO recovery outcome; the recovery capacity spectrum is driven by structural properties of the pruned architecture, not residual SFT quality.
99	
100	\paragraph{Sparsity limits and dose-response.}
101	\label{sec:sparsity_cliff}
102	All methods collapse at 30\% sparsity, validating 20\% as the operating point (Appendix~\ref{sec:appendix_sparsity_cliff}).
103	Pruning reduces parameters by 19\% and memory by ${\sim}$28\% (Appendix~\ref{sec:appendix_inference}).
104	On GSM8K, the CKA coefficient $\alpha$ exhibits an inverted-U pattern in recovery accuracy across $\{0.5, 1.0, 2.0, 3.0, 4.0\}$, peaking at $\alpha{=}2.0$ (SFT 64.97\%, GRPO 66.11\%) with $|\Delta| \leq 1.14$\,pp at every point; $\alpha{=}1.0$ collapses (peak reward 0.061) while $\alpha{=}4.0$ recovers to 62.77\% (Appendix~\ref{sec:appendix_alpha}).
105	
106	
107	\subsection{Extended Analysis}
108	\label{sec:extended_analysis}
109	
110	\begin{figure}[t]
111	    \centering
112	    \includegraphics[width=\columnwidth]{figures/paper/fig4_cka_heatmap.pdf}
113	    \caption{Layer-wise CKA similarity between dense and pruned representations (28 layers). CKA-only diverges most from dense ($\mu{=}0.62$) yet recovers best; Standard ($\mu{=}0.90$), Random ($\mu{=}0.92$), and \rasp{} ($\mu{=}0.88$) preserve dense fidelity but collapse under RL.}
114	    \label{fig:cka_heatmap}
115	\end{figure}
116	
117	\input{tables/tab5_cross_scale}
118	
119	\paragraph{Representational diversity.}
120	CKA similarity between dense and pruned representations (Figure~\ref{fig:cka_heatmap}) shows CKA-only diverges most from the dense model ($\mu{=}0.62$), while Standard ($\mu{=}0.90$), Random ($\mu{=}0.92$), and \rasp{} ($\mu{=}0.88$) cluster near 1.0.
121	Gradient importance preserves dense fidelity at the cost of redundant representations that provide no exploration benefit during GRPO.
122	CKA-only concentrates pruning in early layers (L0--9, 72.5\% of removed groups) while Standard prunes uniformly, removing late-layer structures that are representationally unique (Appendix~\ref{sec:appendix_overlap}).
123	Gradient flow analysis corroborates this: CKA-only models exhibit 2.89$\times$ mean gradient magnitude versus Standard across 55/56 layer groups ($p{<}0.05$, Wilcoxon; Appendix~\ref{sec:appendix_gradient}), consistent with diversity preservation enabling stronger RL training signals.
124	
125	\paragraph{Extended training cannot rescue collapse.}
126	Extending GRPO from 100 to 300 steps (Figure~\ref{fig:extended_training}, Appendix~\ref{sec:appendix_extended}), Standard shows zero net improvement (reward 0.054--0.058, $f_0 > 0.5$ throughout), while CKA-only sustains a 5.5$\times$ gap (0.308 vs 0.056 at step 300). The gap is structural, not a matter of training budget.
127	
128	\paragraph{Cross-scale and cross-architecture generalization.}
129	On DeepSeek-R1-Distill-Qwen-1.5B at 20\% sparsity (Table~\ref{tab:cross_scale}), the three-method ordering is preserved (CKA-only 35.48\% $\gg$ \rasp{} 26.16\% $>$ Standard 22.29\%), with reward-accuracy decoupling confirmed at this scale ($|\Delta| < 1$\,pp: CKA-only $-$0.15, Standard $-$0.61\,pp).
130	On Qwen2.5-Math-7B at 20\% sparsity (Table~\ref{tab:cross_arch}, Appendix~\ref{sec:appendix_cross_arch}), CKA-only causes near-total initial damage (1.0\% vs Standard's 18.5\%) yet SFT recovers it to 51.50\% $\pm$ 3.53 while Standard remains at 21.00\% $\pm$ 2.88 ($N{=}200$)---confirming that recoverability is shaped by preserved structure, not starting accuracy.
131	GRPO validation on this architecture is deferred to future work.
132	
133	
134	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab867b27-9276-4a85-92cd-85023544aec9",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "f30963e6-9e6c-41cd-9888-b0c8ecfcee2c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex",
      "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Base model and evaluation.}\nWe evaluate on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\\citep{qwen2.5} with GQA~\\citep{ainslie2023gqa} (architecture details in Section~\\ref{sec:prelim}).\nOur primary benchmark is GSM8K~\\citep{cobbe2021gsm8k}, a set of 1{,}319 grade-school math problems requiring multi-step arithmetic reasoning.\nWe report exact-match accuracy: the final numerical answer is extracted from the model's generation and compared against the ground truth.\nFor rapid iteration during development, we use a 100-problem subset ($N{=}100$); final results use the full test set ($N{=}1{,}319$).\nThe original unpruned model achieves 90.83\\% on GSM8K (greedy decoding).\n\n\\paragraph{Pruning methods.}\nWe compare four pruning criteria at 20\\% structured sparsity, all removing the same number of MLP channel groups (200 of 784 across 28 layers, ${\\sim}$1.45B parameters) with identical per-layer capacity floors (${\\ge}$40\\% retention per layer):\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{CKA-only}: structures ranked by functional overlap $F(h)$ alone (Eq.~\\ref{eq:overlap}); the most redundant groups are removed regardless of gradient importance.\n    \\item \\textbf{Random}: uniform random selection among eligible groups.\n    \\item \\textbf{Standard}: Taylor-expansion importance $I(h)$ alone (Eq.~\\ref{eq:importance}); the least important groups are removed, following LLM-Pruner~\\citep{llmpruner2023}.\n    \\item \\textbf{\\rasp{}} ($\\alpha{=}1.0$): the composite score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ (Eq.~\\ref{eq:score}), removing structures that are both low-importance and functionally redundant.\n\\end{enumerate}\n\n\\paragraph{Recovery pipeline and hardware.}\nAll four methods undergo matched two-stage recovery.\nStage~1 (SFT warmup): 2 epochs on 7{,}473 GSM8K chain-of-thought examples with teacher forcing (37 minutes), restoring EOS generation and basic format compliance.\nStage~2 (GRPO): Group Relative Policy Optimization~\\citep{shao2024grpo} with learning rate $1{\\times}10^{-6}$, maximum completion length 1{,}024 tokens, KL penalty coefficient $\\beta{=}0.01$, sampling temperature 0.4, DAPO-style clipped loss, and binary reward ($r{=}1$ if correct, $r{=}0$ otherwise), trained for 100 steps on 1{,}000 GSM8K training problems.\nAll methods share identical GRPO hyperparameters, including \\texttt{reward\\_desert\\_patience}{$=$}50.\nSeeds vary at the GRPO stage; pruning calibration and SFT use identical configurations across all methods.\nWe repeat GRPO training with 3 random seeds for CKA-only, Standard, and Random (Table~\\ref{tab:decoupling}).\nCKA-only achieves 64.39\\% $\\pm$ 0.19\\,pp (std across seeds), Standard 59.84\\% $\\pm$ 0.38\\,pp; the 4.55\\,pp gap is robust across seeds (Welch's $t$-test, $p{=}0.0009$, Cohen's $d{=}11.1$; 95\\% CI for mean difference: $[3.62, 5.47]$\\,pp), confirming that recovery capacity differences are structural rather than stochastic.\nAll experiments run on 2$\\times$ NVIDIA RTX PRO 6000 GPUs (94\\,GB VRAM each); pruning variants are trained in parallel on separate GPUs under identical wall-clock conditions.\n\n\n\\subsection{Recovery Capacity Spectrum}\n\\label{sec:recovery_gradient}\n\n\\input{tables/tab1_recovery_gradient}\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=\\columnwidth]{figures/paper/fig2_reward_trajectories.pdf}\n    \\caption{GRPO reward trajectories for four pruning criteria and the unpruned model under identical training configuration ($\\beta{=}0.01$, $T{=}0.4$, 100 steps). CKA-only reaches 0.354 peak reward with an observed recovery event at step 90. Random oscillates between 0.14 and 0.19 (training timed out at step 97; 9 steps shown). Standard peaks at 0.081 before borderline collapse. \\rasp{} peaks at 0.061 (step 50) and declines to 0.010 by step 100.}\n    \\label{fig:reward_trajectories}\n\\end{figure}\n\nThe central finding is that the pruning criterion determines post-RLVR recovery capacity.\nUnder controlled GRPO training with identical hyperparameters, the four pruning criteria produce qualitatively distinct training dynamics that form a clear recovery capacity spectrum: CKA-only $\\gg$ Random $\\gg$ Standard $>$ \\rasp{}.\nTable~\\ref{tab:recovery_gradient} summarizes the key metrics, and Figure~\\ref{fig:reward_trajectories} shows the reward trajectories over 100 GRPO steps.\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=\\columnwidth]{figures/paper/fig3_collapse_dynamics.pdf}\n    \\caption{Training dynamics diagnostics. (a)~$f_0$ (fraction of zero-variance batches): CKA-only stays below 0.35; Standard and \\rasp{} remain in the collapse zone ($f_0 > 0.5$) throughout training. (b)~Gradient norm: Standard exhibits a transient minimum of 0.017 at step 90 before recovering to 2.41 at step 100; \\rasp{} gradient norms remain predominantly near zero.}\n    \\label{fig:collapse_dynamics}\n\\end{figure}\n\nCKA-only pruning is the only method that produces active learning under GRPO.\nReward reaches a peak of 0.354 (mean 0.285) with $f_0$ as low as 0.125, including a recovery event at step 90 where reward rebounds from a transient perturbation.\nRandom pruning produces stagnation: reward oscillates between 0.142 and 0.190 with $f_0$ near 0.33.\n\nStandard pruning exhibits borderline collapse (Figure~\\ref{fig:collapse_dynamics}): reward peaks at 0.081 (step 40) then oscillates near 0.05, with $f_0 \\geq 0.500$ throughout---more than half of batches produce no learning signal.\n\\rasp{} produces full collapse: reward peaks at 0.061 (step 50) then declines to 0.010 by step 100, with $f_0 > 0.675$ and clipped ratio $>$ 90\\%.\n\nThe 5.8$\\times$ peak reward gap (CKA-only 0.354 vs \\rasp{} 0.061) arises from models pruned to identical parameter budgets with identical GRPO configurations; the only variable is which structures were removed.\n\n\n\\subsection{Reward-Accuracy Decoupling}\n\\label{sec:decoupling}\n\n\\input{tables/tab2_decoupling}\n\nGRPO reward trajectory reflects training capacity---the model's ability to learn from RL signal---not downstream accuracy, a phenomenon we term \\emph{reward-accuracy decoupling} (mean $|\\Delta| {=} 0.54$\\,pp, max $1.14$\\,pp on GSM8K across all fine-grained criteria and sparsity levels).\nAt 20\\% sparsity, accuracy changes are small across all pruned methods ($|\\Delta| < 1$\\,pp: CKA-only $+$0.48, Standard $+$0.55, Random $-$0.53, \\rasp{} $-$0.61\\,pp; Table~\\ref{tab:decoupling}) despite the 4.4$\\times$ peak reward gap.\n\nThe degree of decoupling varies with sparsity.\nAt 15\\% (3-seed GRPO), SFT establishes a 5.69\\,pp gap between CKA-only and Standard (72.18\\% vs 66.49\\%; single SFT seed), which GRPO maintains or slightly amplifies to 7.20\\,pp (72.76\\% vs 65.56\\%; Welch's $t$-test, $p{<}0.001$).\nAt 20\\%, the differential GRPO contribution is negligible: SFT establishes a 4.62\\,pp gap that GRPO preserves (4.55\\,pp).\nAt 25\\% (single seed), decoupling is most extreme: Standard's peak reward collapses to 0.008 yet accuracy changes by only $+$0.99\\,pp (Appendix~\\ref{sec:appendix_cross_sparsity}).\nAcross all four fine-grained pruning criteria and both sparsity levels tested (20\\% and 25\\%), $|\\Delta| < 1$\\,pp without exception on GSM8K (Tables~\\ref{tab:decoupling},~\\ref{tab:cross_sparsity}); on MATH-500, SFT--GRPO differences remain within statistical noise (all $|\\Delta| < 2.5$\\,pp with stderr ${\\approx}$2\\,pp per condition; Appendix~\\ref{sec:appendix_math500}).\nThis pattern suggests that moderate structural damage (15\\%) preserves enough capacity for GRPO to differentially benefit CKA-only pruning, while more aggressive pruning (20--25\\%) exceeds the threshold where GRPO can improve upon SFT baselines.\n\nCKA-only GRPO accuracy is reproducible across three random seeds (64.22--64.58\\%, observed range 0.36\\,pp; Appendix~\\ref{sec:appendix_multiseed}).\nExtended training to 300 steps at 20\\% confirms: accuracy remains unchanged (CKA-only 64.37\\%$\\to$64.37\\%, Standard 59.44\\%$\\to$59.29\\%; single seed).\nThe pruning-criterion ranking transfers to MATH-500~\\citep{hendrycks2021math} (SFT: CKA-only 26.8\\% vs Standard 25.8\\% vs \\rasp{} 21.2\\% vs Random 14.4\\%; Appendix~\\ref{sec:appendix_math500}), and decoupling holds across HumanEval~\\citep{chen2021humaneval} and MBPP~\\citep{austin2021mbpp} (all fine-grained GRPO $|\\Delta| < 2$\\,pp; MBPP deltas are uniformly slightly positive but within stderr; Appendix~\\ref{sec:appendix_mbpp}).\n\\label{sec:ood}\nShortGPT~\\citep{shortgpt2024} depth pruning is the exception: GRPO interaction is task-dependent ($-$1.36\\,pp on GSM8K, $+$4.01\\,pp on MBPP; Tables~\\ref{tab:decoupling},~\\ref{tab:mbpp}), unlike the uniformly neutral deltas of fine-grained methods ($|\\Delta| \\leq 1.34$\\,pp).\nThe cross-benchmark maximum comes from MBPP (Table~\\ref{tab:mbpp}); the GSM8K maximum is $1.14$\\,pp (Table~\\ref{tab:alpha}).\n\n\n\\subsection{Additional Results}\n\\label{sec:additional_results}\n\n\\paragraph{Post-SFT accuracy does not predict GRPO outcome.}\n\\label{sec:sft_gradient}\nUnder SFT alone, CKA-only (63.91\\%) $>$ \\rasp{} (61.49\\%) $>$ Standard (59.29\\%) $>$ Random (51.25\\%), yet under GRPO the \\rasp{}/Standard ordering reverses (peak 0.081 vs 0.061) and Random outperforms both in peak reward (0.190).\nMore strikingly, ShortGPT post-SFT (44.73\\%) shows GRPO actively harming accuracy ($-$1.36\\,pp), while unstructured pruning achieves the highest post-SFT accuracy (87.87\\%) with GRPO accuracy 87.64\\% ($\\Delta{=}{-}0.23$\\,pp), confirming that pruning criteria are irrelevant when structural damage is minimal (96.5\\% dense retention).\nPost-SFT accuracy does not monotonically determine GRPO recovery outcome; the recovery capacity spectrum is driven by structural properties of the pruned architecture, not residual SFT quality.\n\n\\paragraph{Sparsity limits and dose-response.}\n\\label{sec:sparsity_cliff}\nAll methods collapse at 30\\% sparsity, validating 20\\% as the operating point (Appendix~\\ref{sec:appendix_sparsity_cliff}).\nPruning reduces parameters by 19\\% and memory by ${\\sim}$28\\% (Appendix~\\ref{sec:appendix_inference}).\nOn GSM8K, the CKA coefficient $\\alpha$ exhibits an inverted-U pattern in recovery accuracy across $\\{0.5, 1.0, 2.0, 3.0, 4.0\\}$, peaking at $\\alpha{=}2.0$ (SFT 64.97\\%, GRPO 66.11\\%) with $|\\Delta| \\leq 1.14$\\,pp at every point; $\\alpha{=}1.0$ collapses (peak reward 0.061) while $\\alpha{=}4.0$ recovers to 62.77\\% (Appendix~\\ref{sec:appendix_alpha}).\n\n\n\\subsection{Extended Analysis}\n\\label{sec:extended_analysis}\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=\\columnwidth]{figures/paper/fig4_cka_heatmap.pdf}\n    \\caption{Layer-wise CKA similarity between dense and pruned representations (28 layers). CKA-only diverges most from dense ($\\mu{=}0.62$) yet recovers best; Standard ($\\mu{=}0.90$), Random ($\\mu{=}0.92$), and \\rasp{} ($\\mu{=}0.88$) preserve dense fidelity but collapse under RL.}\n    \\label{fig:cka_heatmap}\n\\end{figure}\n\n\\input{tables/tab5_cross_scale}\n\n\\paragraph{Representational diversity.}\nCKA similarity between dense and pruned representations (Figure~\\ref{fig:cka_heatmap}) shows CKA-only diverges most from the dense model ($\\mu{=}0.62$), while Standard ($\\mu{=}0.90$), Random ($\\mu{=}0.92$), and \\rasp{} ($\\mu{=}0.88$) cluster near 1.0.\nGradient importance preserves dense fidelity at the cost of redundant representations that provide no exploration benefit during GRPO.\nCKA-only concentrates pruning in early layers (L0--9, 72.5\\% of removed groups) while Standard prunes uniformly, removing late-layer structures that are representationally unique (Appendix~\\ref{sec:appendix_overlap}).\nGradient flow analysis corroborates this: CKA-only models exhibit 2.89$\\times$ mean gradient magnitude versus Standard across 55/56 layer groups ($p{<}0.05$, Wilcoxon; Appendix~\\ref{sec:appendix_gradient}), consistent with diversity preservation enabling stronger RL training signals.\n\n\\paragraph{Extended training cannot rescue collapse.}\nExtending GRPO from 100 to 300 steps (Figure~\\ref{fig:extended_training}, Appendix~\\ref{sec:appendix_extended}), Standard shows zero net improvement (reward 0.054--0.058, $f_0 > 0.5$ throughout), while CKA-only sustains a 5.5$\\times$ gap (0.308 vs 0.056 at step 300). The gap is structural, not a matter of training budget.\n\n\\paragraph{Cross-scale and cross-architecture generalization.}\nOn DeepSeek-R1-Distill-Qwen-1.5B at 20\\% sparsity (Table~\\ref{tab:cross_scale}), the three-method ordering is preserved (CKA-only 35.48\\% $\\gg$ \\rasp{} 26.16\\% $>$ Standard 22.29\\%), with reward-accuracy decoupling confirmed at this scale ($|\\Delta| < 1$\\,pp: CKA-only $-$0.15, Standard $-$0.61\\,pp).\nOn Qwen2.5-Math-7B at 20\\% sparsity (Table~\\ref{tab:cross_arch}, Appendix~\\ref{sec:appendix_cross_arch}), CKA-only causes near-total initial damage (1.0\\% vs Standard's 18.5\\%) yet SFT recovers it to 51.50\\% $\\pm$ 3.53 while Standard remains at 21.00\\% $\\pm$ 2.88 ($N{=}200$)---confirming that recoverability is shaped by preserved structure, not starting accuracy.\nGRPO validation on this architecture is deferred to future work.\n\n\n",
      "numLines": 134,
      "startLine": 1,
      "totalLines": 134
    }
  },
  "sourceToolAssistantUUID": "ab867b27-9276-4a85-92cd-85023544aec9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T04:05:38.855Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GXT1xt9oQ1Jh4Rh7cFdg1e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f30963e6-9e6c-41cd-9888-b0c8ecfcee2c",
  "isSidechain": false,
  "requestId": "req_011CbJqe8RAU8hhy9mDRfdxH",
  "type": "assistant",
  "uuid": "029a7b93-5343-489b-b7f9-6497717761cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AikNj8BwKMU39MmHyboKMo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12647,
      "cache_read_input_tokens": 38782,
      "output_tokens": 801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 801,
          "cache_read_input_tokens": 38782,
          "cache_creation_input_tokens": 12647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12647
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-23T04:05:38.859Z_

<details><summary>↩ Tool result · `toolu_01GXT1xt9oQ1Jh4Rh7cFdg1e`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:conclusion}
3	
4	We show that the widely observed RLVR${>}$SFT hierarchy for pruned reasoning models reflects suboptimal fine-grained structural pruning rather than a fundamental property of RL: when pruning preserves representational diversity, recovery method choice becomes irrelevant (mean $|\Delta| {=} 0.54$\,pp, max $1.34$\,pp across all tested fine-grained conditions on GSM8K and MBPP).
5	Under identical GRPO training, CKA-only pruning enables active learning (peak reward 4.4$\times$ Standard), while importance-based methods collapse; extended training to 300 steps confirms this gap is structural.
6	We observe evidence consistent with representational diversity as a strong predictor of recovery capacity: CKA-only diverges most from the dense representation ($\mu{=}0.62$) yet recovers best, while collapsing methods preserve dense fidelity ($\mu{\geq}0.88$), though causal verification remains for future work.
7	Reward-accuracy decoupling is sparsity-dependent: at 15\%, GRPO amplifies the CKA-only advantage (5.69\,pp$\to$7.20\,pp), while at 20--25\% GRPO cannot improve upon SFT baselines, motivating reward trajectory as the appropriate diagnostic.
8	Cross-scale (1.5B) and cross-architecture (Qwen2.5-Math-7B) experiments provide initial evidence for generality.
9	Our findings are established for fine-grained structural pruning (MLP channel removal); \citet{selfhealing2025} study unstructured magnitude pruning retaining 96.5\% of parameters, and whether their RLVR${>}$SFT advantage similarly vanishes under diversity-preserving criteria in that setting remains open.
10	Recent work shows that RL fine-tuning updates only 5--30\% of parameters~\citep{mukherjee2025rlsubnetworks}; whether CKA-based pruning preferentially preserves structures within this active subnetwork---consistent with the Lottery Ticket Hypothesis~\citep{frankle2019lth}---is an open question that would provide a complementary mechanistic explanation.
11	
12	Code, pruning masks, and model checkpoints will be released upon acceptance.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "029a7b93-5343-489b-b7f9-6497717761cd",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "294a3e1c-f156-4d4b-a245-38077def9e21",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:conclusion}\n\nWe show that the widely observed RLVR${>}$SFT hierarchy for pruned reasoning models reflects suboptimal fine-grained structural pruning rather than a fundamental property of RL: when pruning preserves representational diversity, recovery method choice becomes irrelevant (mean $|\\Delta| {=} 0.54$\\,pp, max $1.34$\\,pp across all tested fine-grained conditions on GSM8K and MBPP).\nUnder identical GRPO training, CKA-only pruning enables active learning (peak reward 4.4$\\times$ Standard), while importance-based methods collapse; extended training to 300 steps confirms this gap is structural.\nWe observe evidence consistent with representational diversity as a strong predictor of recovery capacity: CKA-only diverges most from the dense representation ($\\mu{=}0.62$) yet recovers best, while collapsing methods preserve dense fidelity ($\\mu{\\geq}0.88$), though causal verification remains for future work.\nReward-accuracy decoupling is sparsity-dependent: at 15\\%, GRPO amplifies the CKA-only advantage (5.69\\,pp$\\to$7.20\\,pp), while at 20--25\\% GRPO cannot improve upon SFT baselines, motivating reward trajectory as the appropriate diagnostic.\nCross-scale (1.5B) and cross-architecture (Qwen2.5-Math-7B) experiments provide initial evidence for generality.\nOur findings are established for fine-grained structural pruning (MLP channel removal); \\citet{selfhealing2025} study unstructured magnitude pruning retaining 96.5\\% of parameters, and whether their RLVR${>}$SFT advantage similarly vanishes under diversity-preserving criteria in that setting remains open.\nRecent work shows that RL fine-tuning updates only 5--30\\% of parameters~\\citep{mukherjee2025rlsubnetworks}; whether CKA-based pruning preferentially preserves structures within this active subnetwork---consistent with the Lottery Ticket Hypothesis~\\citep{frankle2019lth}---is an open question that would provide a complementary mechanistic explanation.\n\nCode, pruning masks, and model checkpoints will be released upon acceptance.\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  },
  "sourceToolAssistantUUID": "029a7b93-5343-489b-b7f9-6497717761cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T04:05:39.190Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CwYZhckSQax9gvo9xoGN1K`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "294a3e1c-f156-4d4b-a245-38077def9e21",
  "isSidechain": false,
  "requestId": "req_011CbJqe8RAU8hhy9mDRfdxH",
  "type": "assistant",
  "uuid": "f9edc546-ab40-4846-a868-3fedef2b9231",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AikNj8BwKMU39MmHyboKMo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12647,
      "cache_read_input_tokens": 38782,
      "output_tokens": 801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 801,
          "cache_read_input_tokens": 38782,
          "cache_creation_input_tokens": 12647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12647
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-23T04:05:39.195Z_

<details><summary>↩ Tool result · `toolu_01CwYZhckSQax9gvo9xoGN1K`</summary>

```text
1	% Limitations — required by ACL/EMNLP
2	
3	\paragraph{Architecture and scale.}
4	Our primary results are on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} with GQA ($G{=}7$).
5	Cross-architecture validation on Qwen2.5-Math-7B covers SFT recovery only ($N{=}200$); both models share the Qwen2.5 base architecture, so our cross-architecture evidence does not extend to different architecture families (e.g., LLaMA, Mistral).
6	Whether the spectrum generalizes across architecture families and scales (1B--70B) remains open.
7	
8	\paragraph{Diagnostic limitations.}
9	Reward-accuracy decoupling at 20--25\% sparsity means that recovery capacity---operationalized as peak reward---does not predict downstream accuracy improvements within our training horizon.
10	Recovery capacity captures the model's ability to sustain RL training without collapse, but practitioners seeking accuracy gains may require longer training, different reward formulations, or lower sparsity levels.
11	The per-layer capacity floor (40\% retention) was chosen heuristically and not ablated; different floor values may shift the recovery capacity spectrum.
12	
13	\paragraph{Replication and scope.}
14	CKA-only, Standard, and Random are validated over 3 GRPO seeds; \rasp{} uses a single seed ($N{=}1$).
15	We evaluate on four benchmarks (GSM8K, MATH-500, HumanEval, MBPP) covering math reasoning and code generation; logical, commonsense, and multi-modal reasoning are not addressed.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9edc546-ab40-4846-a868-3fedef2b9231",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "68f79c87-2133-4167-9dd4-0d7f0ea77758",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex",
      "content": "% Limitations — required by ACL/EMNLP\n\n\\paragraph{Architecture and scale.}\nOur primary results are on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} with GQA ($G{=}7$).\nCross-architecture validation on Qwen2.5-Math-7B covers SFT recovery only ($N{=}200$); both models share the Qwen2.5 base architecture, so our cross-architecture evidence does not extend to different architecture families (e.g., LLaMA, Mistral).\nWhether the spectrum generalizes across architecture families and scales (1B--70B) remains open.\n\n\\paragraph{Diagnostic limitations.}\nReward-accuracy decoupling at 20--25\\% sparsity means that recovery capacity---operationalized as peak reward---does not predict downstream accuracy improvements within our training horizon.\nRecovery capacity captures the model's ability to sustain RL training without collapse, but practitioners seeking accuracy gains may require longer training, different reward formulations, or lower sparsity levels.\nThe per-layer capacity floor (40\\% retention) was chosen heuristically and not ablated; different floor values may shift the recovery capacity spectrum.\n\n\\paragraph{Replication and scope.}\nCKA-only, Standard, and Random are validated over 3 GRPO seeds; \\rasp{} uses a single seed ($N{=}1$).\nWe evaluate on four benchmarks (GSM8K, MATH-500, HumanEval, MBPP) covering math reasoning and code generation; logical, commonsense, and multi-modal reasoning are not addressed.\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  },
  "sourceToolAssistantUUID": "f9edc546-ab40-4846-a868-3fedef2b9231",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T04:05:39.663Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BKsyaxogxqC7iPLm58LLod`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68f79c87-2133-4167-9dd4-0d7f0ea77758",
  "isSidechain": false,
  "requestId": "req_011CbJqe8RAU8hhy9mDRfdxH",
  "type": "assistant",
  "uuid": "d5938a14-112f-46f0-b3fa-11804683895c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AikNj8BwKMU39MmHyboKMo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12647,
      "cache_read_input_tokens": 38782,
      "output_tokens": 801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 801,
          "cache_read_input_tokens": 38782,
          "cache_creation_input_tokens": 12647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12647
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-23T04:05:39.671Z_

<details><summary>↩ Tool result · `toolu_01BKsyaxogxqC7iPLm58LLod`</summary>

```text
1	\section{Training Details}
2	\label{sec:appendix_training}
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\caption{Hyperparameter details for SFT warmup and GRPO recovery stages.}
8	\label{tab:hyperparams}
9	\begin{tabular}{@{}lll@{}}
10	\toprule
11	Parameter & SFT & GRPO \\
12	\midrule
13	Learning rate & $2 \times 10^{-5}$ & $1 \times 10^{-6}$ \\
14	Batch size & 1 & 1 \\
15	Gradient accumulation & 8 & 1 \\
16	Max sequence length & 2{,}048 & -- \\
17	Max new tokens & -- & 1{,}024 \\
18	Optimizer & AdamW & AdamW \\
19	Epochs / Steps & 2 epochs & 100 steps \\
20	KL coefficient $\beta$ & -- & 0.01 \\
21	Sampling temperature & -- & 0.4 \\
22	Num generations per prompt & -- & 8 \\
23	Reward & -- & Binary (exact match) \\
24	Loss formulation & Cross-entropy & DAPO-style clipped \\
25	\texttt{reward\_desert\_patience} & -- & 50 \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	\section{Algorithm}
31	\label{sec:appendix_algo}
32	
33	\begin{algorithm}[h]
34	\caption{Controlled Pruning Comparison Framework}
35	\label{alg:rasp}
36	\begin{algorithmic}[1]
37	\Require Model $\mathcal{M}$, calibration data $\mathcal{D}_\text{cal}$, target sparsity $s$, scoring criterion $\mathcal{C} \in \{\text{Std}, \text{RASP}, \text{CKA}, \text{Rand}\}$, layer floor $\tau$
38	\Ensure Pruned and recovered model $\mathcal{M}'$
39	\Statex \textit{\% Stage 1: Shared Structural Analysis}
40	\For{each structure $h \in \mathcal{H}$}
41	    \State Compute importance $I(h)$ via Eq.~\eqref{eq:importance}
42	    \State Collect activations $\mathbf{X}_h$ on $\mathcal{D}_\text{cal}$
43	\EndFor
44	\For{each layer $\ell = 1, \ldots, L$}
45	    \For{each structure $h_i$ in layer $\ell$}
46	        \State $F(h_i) \gets \frac{1}{|\mathcal{H}_\ell|-1} \sum_{j \neq i} \text{CKA}(\mathbf{X}_{h_i}, \mathbf{X}_{h_j})$
47	    \EndFor
48	\EndFor
49	\Statex \textit{\% Stage 2: Criterion-Specific Scoring}
50	\For{each structure $h \in \mathcal{H}$}
51	    \State $S(h) \gets \mathcal{C}(I(h), F(h))$ \hfill $\triangleright$ Eq.~\ref{eq:standard}, \ref{eq:score}, \ref{eq:cka_only}, or random
52	\EndFor
53	\State Sort $\mathcal{H}$ by $S(h)$ ascending; prune lowest up to $s$, subject to $\tau$
54	\Statex \textit{\% Stage 3: Identical Two-Stage Recovery}
55	\State $\mathcal{M}_\text{warm} \gets \text{SFT}(\mathcal{M}_\text{pruned}, \mathcal{D}_\text{sft})$ \hfill $\triangleright$ restore EOS \& format
56	\State $\mathcal{M}' \gets \text{GRPO}(\mathcal{M}_\text{warm}, \mathcal{D}_\text{rlvr})$ \hfill $\triangleright$ recover reasoning
57	\State \Return $\mathcal{M}'$
58	\end{algorithmic}
59	\end{algorithm}
60	
61	\section{Inference Efficiency}
62	\label{sec:appendix_inference}
63	
64	\begin{table}[h]
65	\centering
66	\small
67	\caption{Inference characteristics at 20\% sparsity (clean v2 benchmark, single-GPU, no contention). Pruning reduces parameters by 19\% and memory by ${\sim}$28\%, with TTFT improving 18\%. Per-token throughput decreases 19\% (0.81$\times$) due to non-uniform layer widths from full-layer removal that current GPU kernels do not optimize.}
68	\label{tab:inference}
69	\begin{tabular}{@{}lcccc@{}}
70	\toprule
71	Configuration & TPS\,(tok/s) & TTFT\,(ms) & Per-token\,(ms) & Params\,(B) \\
72	\midrule
73	Dense 7B & 72.0 & 20.1 & 13.9 & 7.62 \\
74	CKA-only 20\% & 58.3 & 16.4 & 16.7 & 6.16 \\
75	Standard 20\% & 58.2 & 16.4 & 16.7 & 6.16 \\
76	\bottomrule
77	\end{tabular}
78	\end{table}
79	
80	All pruned models achieve ${\sim}$28\% memory reduction from structural parameter removal.
81	TTFT (time to first token) improves by 18\% (20.1$\to$16.4\,ms), reflecting faster prefill with fewer parameters.
82	Per-token throughput decreases by 19\% (72.0$\to$58.3 tok/s, or 13.9$\to$16.7\,ms per token), consistent with non-uniform layer widths creating computational bottlenecks that current GPU kernels do not optimize away.
83	CKA-only and Standard show identical throughput (58.3 vs 58.2 tok/s), confirming that the pruning criterion affects recovery capacity but not inference speed at matched sparsity.
84	
85	\section{CKA Coefficient $\alpha$ Ablation}
86	\label{sec:appendix_alpha}
87	
88	\input{tables/table3_alpha}
89	
90	On GSM8K, the dose-response curve across $\alpha \in \{0.5, 1.0, 2.0, 3.0, 4.0\}$ reveals an inverted-U pattern peaking at $\alpha{=}2.0$ (SFT 64.97\%, GRPO 66.11\%, $\Delta{=}{+}1.14$\,pp; Table~\ref{tab:alpha}).
91	At $\alpha{=}0.5$, importance still dominates; recovery is low (SFT 60.73\%, GRPO 61.18\%).
92	At $\alpha{=}1.0$ (\rasp{}), GRPO collapses (peak reward 0.061, accuracy 60.88\%, $\Delta{=}{-}0.61$\,pp).
93	$\alpha{=}3.0$ (SFT 64.14\%, GRPO 63.46\%, $\Delta{=}{-}0.68$\,pp) excludes a plateau hypothesis: accuracy drops 2.65\,pp from the $\alpha{=}2.0$ peak, confirming that the optimum is a true peak rather than a saturation regime.
94	At $\alpha{=}4.0$, CKA overlap dominates; the model recovers to 62.77\% GRPO accuracy (SFT 61.94\%, $\Delta{=}{+}0.83$\,pp) with active GRPO learning (reward 0.146$\to$0.256$\to$0.198).
95	Reward-accuracy decoupling holds at every $\alpha$ value: $|\Delta| \leq 1.14$\,pp across all five points.
96	
97	\section{Extended Training Dynamics}
98	\label{sec:appendix_extended}
99	
100	\begin{figure}[h]
101	    \centering
102	    \includegraphics[width=0.85\columnwidth]{figures/paper/fig5_extended_training.pdf}
103	    \caption{Extended GRPO training (300 steps, 3$\times$ original budget). (a)~Standard reward shows zero net gain (0.054$\to$0.056); CKA-only oscillates in the 0.22--0.44 range with a 5.5$\times$ gap at step 300. (b)~Standard $f_0$ remains in the collapse zone ($>$0.5); CKA-only stays below 0.30.}
104	    \label{fig:extended_training}
105	\end{figure}
106	
107	\section{MATH-500 Out-of-Distribution Evaluation}
108	\label{sec:appendix_math500}
109	
110	\input{tables/tab_math500}
111	
112	The method ordering CKA-only (26.8\%) $>$ Standard (25.8\%) $>$ \rasp{} (21.2\%) $>$ Random (14.4\%) on MATH-500 SFT is preserved from GSM8K (64.39\% $>$ 59.84\% $>$ 60.88\% $>$ 50.72\%), confirming that the recovery capacity spectrum generalizes across benchmarks.
113	The $\alpha$ dose-response effect is not statistically significant on MATH-500: SFT accuracy varies by ${\sim}$8\,pp across $\alpha$ values, but with stderr ${\approx}$2\,pp per point, attributable to high truncation rates at the 2048-token limit and floor effects at this difficulty level.
114	The inverted-U pattern is validated on GSM8K (Table~\ref{tab:alpha}); MATH-500 does not resolve the dose-response shape.
115	
116	\section{MBPP Code Generation}
117	\label{sec:appendix_mbpp}
118	
119	\input{tables/tab_mbpp}
120	
121	MBPP GRPO deltas are uniformly slightly positive across all fine-grained methods (mean $+$1.25\,pp), but none are statistically significant at this sample size ($N{=}374$; stderr ${\approx}1.7$\,pp).
122	This directional consistency may reflect a weak task-specific GRPO effect at the capability floor rather than a violation of reward-accuracy decoupling.
123	
124	\section{CKA Scoring Stability}
125	\label{sec:appendix_cka_stability}
126	
127	\input{tables/tab_cka_stability}
128	
129	CKA-based structure rankings are highly stable across calibration data volumes: Spearman $\rho$ between rankings from 256, 512, and 1024 calibration samples ranges from 0.964 to 0.979, indicating that the scoring criterion is not sensitive to calibration set size.
130	
131	\section{Gradient Signal Analysis}
132	\label{sec:appendix_gradient}
133	
134	We compare per-layer gradient magnitudes during early GRPO training ($N{=}200$ GSM8K calibration samples) across three pruning criteria using paired Wilcoxon signed-rank tests.
135	
136	\begin{table}[h]
137	\centering
138	\small
139	\caption{Pairwise gradient magnitude ratios during GRPO training. Ratio: mean gradient magnitude of method A divided by method B across 56 parameter groups (28 layers $\times$ 2 projections). Significant layers: count where paired Wilcoxon signed-rank $p{<}0.05$.}
140	\label{tab:gradient_flow}
141	\begin{tabular}{@{}lcc@{}}
142	\toprule
143	Comparison & Gradient Ratio & Sig.\ Layers \\
144	\midrule
145	CKA-only vs Standard & 2.89$\times$ & 55\,/\,56 \\
146	CKA-only vs \rasp{} & 2.26$\times$ & 56\,/\,56 \\
147	\rasp{} vs Standard & 1.28$\times$ & 45\,/\,56 \\
148	\bottomrule
149	\end{tabular}
150	\end{table}
151	
152	The gradient magnitude hierarchy (CKA-only $\gg$ \rasp{} $>$ Standard) mirrors the recovery capacity hierarchy (GSM8K: 64.39\% $>$ 60.88\% $>$ 59.84\%), with bootstrap 95\% CIs for all ratios excluding 1.0.
153	This is consistent with diversity preservation enabling stronger training signals during GRPO, though the evidence is correlational: an alternative explanation---that CKA-only retains more functional structure, producing higher initial loss and naturally larger gradients---cannot be ruled out.
154	
155	\section{Seed Reproducibility}
156	\label{sec:appendix_seed}
157	
158	CKA-only GSM8K accuracy across 3 GRPO seeds: 64.37\% (seed 42), 64.22\% (seed 123), 64.58\% (seed 456), yielding mean 64.39\% $\pm$ 0.19\,pp.
159	Standard: mean 59.84\% $\pm$ 0.38\,pp across the same 3 seeds.
160	See Table~\ref{tab:multiseed} for the full summary.
161	
162	\section{Sparsity Cliff at 30\%}
163	\label{sec:appendix_sparsity_cliff}
164	
165	\input{tables/table4_sparsity_cliff}
166	
167	All tested methods collapse at 30\% sparsity: Standard retains 4\% accuracy, \rasp{} and CKA-only reach 0\%.
168	This capacity threshold, independent of pruning criterion, validates 20\% as the operating point and confirms that the recovery capacity spectrum reflects how methods allocate a limited pruning budget.
169	
170	\section{Multi-Seed GRPO Results}
171	\label{sec:appendix_multiseed}
172	
173	\begin{table}[h]
174	\centering
175	\small
176	\caption{Multi-seed GRPO results on GSM8K ($N{=}1{,}319$). CKA-only, Standard, and Random each trained with 3 GRPO seeds (42, 123, 456); pruning calibration and SFT are identical across all runs within each sparsity level.}
177	\label{tab:multiseed}
178	\begin{tabular}{@{}llccc@{}}
179	\toprule
180	Sparsity & Method & Mean Acc.\,(\%) & Std\,(pp) & Seeds \\
181	\midrule
182	\multirow{4}{*}{20\%} & CKA-only & 64.39 & 0.19 & 3 \\
183	 & Standard & 59.84 & 0.38 & 3 \\
184	 & \rasp{} & 60.88 & -- & 1 \\
185	 & Random & 50.72 & 0.15 & 3 \\
186	\midrule
187	\multirow{2}{*}{15\%} & CKA-only & 72.76 & 0.57 & 3 \\
188	 & Standard & 65.56 & 0.50 & 3 \\
189	\bottomrule
190	\end{tabular}
191	\end{table}
192	
193	At 20\% sparsity, the 4.55\,pp gap between CKA-only and Standard is robust across seeds, with non-overlapping ranges (CKA-only: 64.22--64.58\%, Standard: 59.44--60.20\%).
194	Standard shows a wider observed range across seeds (0.76\,pp vs 0.36\,pp), consistent with borderline-collapse dynamics where small perturbations produce larger outcome variation.
195	Random (3 seeds: 50.57\%, 50.72\%, 50.87\%; $\sigma{=}0.15$\,pp, observed range 0.30\,pp) converges in a narrow band with SFT accuracy seed-independent at 51.25\%.
196	All three seeds satisfy GRPO $\leq$ SFT ($\Delta{=}{-}0.68$, $-$0.53, $-$0.38\,pp), confirming that reward-accuracy decoupling is reproducible across seeds even for stagnating methods.
197	Note: Standard seed 42 was trained from a separately initialized SFT checkpoint (accuracy 59.21\% vs.\ 59.29\% for seeds 123/456; $\Delta = 0.08$\,pp).
198	At 15\% sparsity, the gap widens to 7.20\,pp (72.76\% vs 65.56\%, $t{\approx}16.4$, $p{<}0.001$), with non-overlapping ranges (CKA-only: 72.10--73.09\%, Standard: 65.13--65.43\%).
199	
200	\section{Cross-Sparsity Validation}
201	\label{sec:appendix_cross_sparsity}
202	
203	\begin{table}[h]
204	\centering
205	\small
206	\caption{Cross-sparsity validation on DeepSeek-R1-Distill-Qwen-7B. GSM8K accuracy ($N{=}1{,}319$) after SFT warmup and GRPO recovery. 15\% and 20\% GRPO values are mean over 3 seeds (see Tables~\ref{tab:decoupling},~\ref{tab:multiseed}). $^\ddagger$Single seed. Mean $|\Delta| \leq 1$\,pp across all conditions.}
207	\label{tab:cross_sparsity}
208	\begin{tabular}{@{}llccc@{}}
209	\toprule
210	Sparsity & Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
211	\midrule
212	\multirow{2}{*}{15\%} & CKA-only & 72.18 & \textbf{72.76{\scriptsize$\pm$0.57}} & $+$0.58 \\
213	 & Standard & 66.49 & 65.56{\scriptsize$\pm$0.50} & $-$0.93 \\
214	\midrule
215	\multirow{2}{*}{20\%} & CKA-only & 63.91 & 64.39 & $+$0.48 \\
216	 & Standard & 59.29 & 59.84 & $+$0.55 \\
217	\midrule
218	\multirow{2}{*}{25\%$^\ddagger$} & CKA-only & 60.12 & 59.59 & $-$0.53 \\
219	 & Standard & 50.87 & 51.86 & $+$0.99 \\
220	\midrule
221	30\% & All & \multicolumn{3}{c}{Collapse ($\leq$4\%; Table~\ref{tab:sparsity_cliff})} \\
222	\bottomrule
223	\end{tabular}
224	\end{table}
225	
226	At 15\% sparsity (3-seed mean), the CKA-only advantage widens to $+$7.20\,pp (72.76\% vs 65.56\%), compared to $+$4.55\,pp at 20\%.
227	CKA-only at 15\% (72.76\%) represents the highest mean accuracy across all experimental conditions, retaining 80.1\% of original dense model performance (90.83\%).
228	At 25\% sparsity (single seed), Standard's SFT accuracy decline accelerates ($-$7.20\,pp from 15\%$\to$20\%, $-$8.42\,pp from 20\%$\to$25\%), while CKA-only's decline decelerates ($-$8.27\,pp then $-$3.79\,pp).
229	Reward-accuracy decoupling is preserved ($|\Delta| \leq 1$\,pp for both methods) despite Standard's near-zero peak reward (0.008).
230	
231	\section{Cross-Architecture Validation}
232	\label{sec:appendix_cross_arch}
233	
234	\begin{table}[h]
235	\centering
236	\small
237	\caption{Cross-architecture validation on Qwen2.5-Math-7B~\citep{qwen2.5} at 20\% structured sparsity. Accuracy evaluated on GSM8K ($N{=}200$). Post-SFT reports mean $\pm$ std over multiple SFT runs. EOS rate: fraction of generations that produce a valid end-of-sequence token.}
238	\label{tab:cross_arch}
239	\begin{tabular}{@{}lccc@{}}
240	\toprule
241	Method & Post-Prune\,(\%) & Post-SFT\,(\%) & EOS Rate\,(\%) \\
242	\midrule
243	CKA-only & 1.0 & \textbf{51.50 $\pm$ 3.53} & 27.0 \\
244	Standard & 18.5 & 21.00 $\pm$ 2.88 & 36.5 \\
245	\bottomrule
246	\end{tabular}
247	\end{table}
248	
249	CKA-only pruning causes near-total initial damage on Qwen2.5-Math-7B (1.0\% post-prune accuracy vs Standard's 18.5\%), yet SFT recovers CKA-only to 51.50\% while Standard remains at 21.00\%.
250	This post-prune accuracy reversal provides strong evidence that recovery capacity is shaped by preserved network structure rather than starting accuracy.
251	EOS rates remain below 40\% for both methods, indicating that SFT warmup is less effective on this architecture; GRPO validation is deferred to future work.\footnote{Preliminary GRPO evaluation yields 48.60\% (243/500), but 83.8\% of responses were truncated at 2048 tokens, precluding direct comparison with SFT results.}
252	
253	\section{Structural Overlap Analysis}
254	\label{sec:appendix_overlap}
255	
256	CKA-only and Standard pruning produce markedly different removal patterns across the 28 layers of DeepSeek-R1-Distill-Qwen-7B at 20\% sparsity.
257	CKA-only concentrates pruning in early layers (L0--9 account for 72.5\% of removed MLP groups), preserving nearly all structures in later layers (L16--27).
258	Standard distributes removals more uniformly, pruning substantial numbers of groups in late layers (L16--18, L22, L25--26).
259	
260	The methods share only partial overlap in which structures they remove.
261	65 MLP groups are pruned exclusively by CKA-only (retained by Standard), concentrated in L6--9 and L27---structures that gradient importance scores as important but CKA identifies as redundant with neighboring groups.
262	Conversely, 46+ groups are pruned exclusively by Standard (retained by CKA-only), concentrated in L16--18, L22, and L25--26---structures that gradient importance scores as unimportant but CKA identifies as representationally unique.
263	
264	This pattern is consistent with the CKA heatmap (Figure~\ref{fig:cka_heatmap}): CKA-only's aggressive early-layer pruning disrupts dense representations (low diagonal CKA, $\mu{=}0.62$) but preserves diverse late-layer pathways, while Standard's uniform pruning maintains dense fidelity ($\mu{=}0.90$) at the cost of removing unique computational pathways in later layers.
265	
266	\section{KL Divergence During GRPO Training}
267	\label{sec:appendix_kl}
268	
269	\begin{figure}[t]
270	    \centering
271	    \includegraphics[width=0.75\columnwidth]{figures/paper/fig_appendix_kl.pdf}
272	    \caption{KL divergence between the policy and reference model during GRPO training. RASP maintains near-zero KL ($<$0.001), consistent with minimal policy movement during collapse. Random shows the highest KL (${\sim}$0.004--0.005), indicating more policy exploration. CKA-only and Standard fall between these extremes.}
273	    \label{fig:kl_divergence}
274	\end{figure}
275	
276	\section{Depth-First Pruning Baseline}
277	\label{sec:appendix_depth_first}
278	
279	As a sanity check, we test whether CKA-only's advantage reflects mere layer-depth bias by constructing a depth-first baseline: synthetic importance scores force removal of late layers first (L18--27: 0.001, L10--17: 0.5, L0--9: 1.0), then standard pruning at 20\% sparsity.
280	Both SFT (${\sim}$10\%) and GRPO (${\sim}$8\%) accuracy are near chance (early-stopped at $N{\approx}50$--88 samples due to conclusive results), confirming that naive depth ordering cannot substitute for criterion-based structure selection.
281	This baseline operates at layer-level granularity (removing entire transformer blocks), unlike CKA-only/Standard/\rasp{} which prune at MLP channel group level; the granularity difference limits direct comparison with our main results and precludes using this baseline as evidence for the recovery capacity spectrum.
282	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5938a14-112f-46f0-b3fa-11804683895c",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "134d9415-bc7e-40e1-813b-1cd19d5de980",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex",
      "content": "\\section{Training Details}\n\\label{sec:appendix_training}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Hyperparameter details for SFT warmup and GRPO recovery stages.}\n\\label{tab:hyperparams}\n\\begin{tabular}{@{}lll@{}}\n\\toprule\nParameter & SFT & GRPO \\\\\n\\midrule\nLearning rate & $2 \\times 10^{-5}$ & $1 \\times 10^{-6}$ \\\\\nBatch size & 1 & 1 \\\\\nGradient accumulation & 8 & 1 \\\\\nMax sequence length & 2{,}048 & -- \\\\\nMax new tokens & -- & 1{,}024 \\\\\nOptimizer & AdamW & AdamW \\\\\nEpochs / Steps & 2 epochs & 100 steps \\\\\nKL coefficient $\\beta$ & -- & 0.01 \\\\\nSampling temperature & -- & 0.4 \\\\\nNum generations per prompt & -- & 8 \\\\\nReward & -- & Binary (exact match) \\\\\nLoss formulation & Cross-entropy & DAPO-style clipped \\\\\n\\texttt{reward\\_desert\\_patience} & -- & 50 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Algorithm}\n\\label{sec:appendix_algo}\n\n\\begin{algorithm}[h]\n\\caption{Controlled Pruning Comparison Framework}\n\\label{alg:rasp}\n\\begin{algorithmic}[1]\n\\Require Model $\\mathcal{M}$, calibration data $\\mathcal{D}_\\text{cal}$, target sparsity $s$, scoring criterion $\\mathcal{C} \\in \\{\\text{Std}, \\text{RASP}, \\text{CKA}, \\text{Rand}\\}$, layer floor $\\tau$\n\\Ensure Pruned and recovered model $\\mathcal{M}'$\n\\Statex \\textit{\\% Stage 1: Shared Structural Analysis}\n\\For{each structure $h \\in \\mathcal{H}$}\n    \\State Compute importance $I(h)$ via Eq.~\\eqref{eq:importance}\n    \\State Collect activations $\\mathbf{X}_h$ on $\\mathcal{D}_\\text{cal}$\n\\EndFor\n\\For{each layer $\\ell = 1, \\ldots, L$}\n    \\For{each structure $h_i$ in layer $\\ell$}\n        \\State $F(h_i) \\gets \\frac{1}{|\\mathcal{H}_\\ell|-1} \\sum_{j \\neq i} \\text{CKA}(\\mathbf{X}_{h_i}, \\mathbf{X}_{h_j})$\n    \\EndFor\n\\EndFor\n\\Statex \\textit{\\% Stage 2: Criterion-Specific Scoring}\n\\For{each structure $h \\in \\mathcal{H}$}\n    \\State $S(h) \\gets \\mathcal{C}(I(h), F(h))$ \\hfill $\\triangleright$ Eq.~\\ref{eq:standard}, \\ref{eq:score}, \\ref{eq:cka_only}, or random\n\\EndFor\n\\State Sort $\\mathcal{H}$ by $S(h)$ ascending; prune lowest up to $s$, subject to $\\tau$\n\\Statex \\textit{\\% Stage 3: Identical Two-Stage Recovery}\n\\State $\\mathcal{M}_\\text{warm} \\gets \\text{SFT}(\\mathcal{M}_\\text{pruned}, \\mathcal{D}_\\text{sft})$ \\hfill $\\triangleright$ restore EOS \\& format\n\\State $\\mathcal{M}' \\gets \\text{GRPO}(\\mathcal{M}_\\text{warm}, \\mathcal{D}_\\text{rlvr})$ \\hfill $\\triangleright$ recover reasoning\n\\State \\Return $\\mathcal{M}'$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\section{Inference Efficiency}\n\\label{sec:appendix_inference}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Inference characteristics at 20\\% sparsity (clean v2 benchmark, single-GPU, no contention). Pruning reduces parameters by 19\\% and memory by ${\\sim}$28\\%, with TTFT improving 18\\%. Per-token throughput decreases 19\\% (0.81$\\times$) due to non-uniform layer widths from full-layer removal that current GPU kernels do not optimize.}\n\\label{tab:inference}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nConfiguration & TPS\\,(tok/s) & TTFT\\,(ms) & Per-token\\,(ms) & Params\\,(B) \\\\\n\\midrule\nDense 7B & 72.0 & 20.1 & 13.9 & 7.62 \\\\\nCKA-only 20\\% & 58.3 & 16.4 & 16.7 & 6.16 \\\\\nStandard 20\\% & 58.2 & 16.4 & 16.7 & 6.16 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll pruned models achieve ${\\sim}$28\\% memory reduction from structural parameter removal.\nTTFT (time to first token) improves by 18\\% (20.1$\\to$16.4\\,ms), reflecting faster prefill with fewer parameters.\nPer-token throughput decreases by 19\\% (72.0$\\to$58.3 tok/s, or 13.9$\\to$16.7\\,ms per token), consistent with non-uniform layer widths creating computational bottlenecks that current GPU kernels do not optimize away.\nCKA-only and Standard show identical throughput (58.3 vs 58.2 tok/s), confirming that the pruning criterion affects recovery capacity but not inference speed at matched sparsity.\n\n\\section{CKA Coefficient $\\alpha$ Ablation}\n\\label{sec:appendix_alpha}\n\n\\input{tables/table3_alpha}\n\nOn GSM8K, the dose-response curve across $\\alpha \\in \\{0.5, 1.0, 2.0, 3.0, 4.0\\}$ reveals an inverted-U pattern peaking at $\\alpha{=}2.0$ (SFT 64.97\\%, GRPO 66.11\\%, $\\Delta{=}{+}1.14$\\,pp; Table~\\ref{tab:alpha}).\nAt $\\alpha{=}0.5$, importance still dominates; recovery is low (SFT 60.73\\%, GRPO 61.18\\%).\nAt $\\alpha{=}1.0$ (\\rasp{}), GRPO collapses (peak reward 0.061, accuracy 60.88\\%, $\\Delta{=}{-}0.61$\\,pp).\n$\\alpha{=}3.0$ (SFT 64.14\\%, GRPO 63.46\\%, $\\Delta{=}{-}0.68$\\,pp) excludes a plateau hypothesis: accuracy drops 2.65\\,pp from the $\\alpha{=}2.0$ peak, confirming that the optimum is a true peak rather than a saturation regime.\nAt $\\alpha{=}4.0$, CKA overlap dominates; the model recovers to 62.77\\% GRPO accuracy (SFT 61.94\\%, $\\Delta{=}{+}0.83$\\,pp) with active GRPO learning (reward 0.146$\\to$0.256$\\to$0.198).\nReward-accuracy decoupling holds at every $\\alpha$ value: $|\\Delta| \\leq 1.14$\\,pp across all five points.\n\n\\section{Extended Training Dynamics}\n\\label{sec:appendix_extended}\n\n\\begin{figure}[h]\n    \\centering\n    \\includegraphics[width=0.85\\columnwidth]{figures/paper/fig5_extended_training.pdf}\n    \\caption{Extended GRPO training (300 steps, 3$\\times$ original budget). (a)~Standard reward shows zero net gain (0.054$\\to$0.056); CKA-only oscillates in the 0.22--0.44 range with a 5.5$\\times$ gap at step 300. (b)~Standard $f_0$ remains in the collapse zone ($>$0.5); CKA-only stays below 0.30.}\n    \\label{fig:extended_training}\n\\end{figure}\n\n\\section{MATH-500 Out-of-Distribution Evaluation}\n\\label{sec:appendix_math500}\n\n\\input{tables/tab_math500}\n\nThe method ordering CKA-only (26.8\\%) $>$ Standard (25.8\\%) $>$ \\rasp{} (21.2\\%) $>$ Random (14.4\\%) on MATH-500 SFT is preserved from GSM8K (64.39\\% $>$ 59.84\\% $>$ 60.88\\% $>$ 50.72\\%), confirming that the recovery capacity spectrum generalizes across benchmarks.\nThe $\\alpha$ dose-response effect is not statistically significant on MATH-500: SFT accuracy varies by ${\\sim}$8\\,pp across $\\alpha$ values, but with stderr ${\\approx}$2\\,pp per point, attributable to high truncation rates at the 2048-token limit and floor effects at this difficulty level.\nThe inverted-U pattern is validated on GSM8K (Table~\\ref{tab:alpha}); MATH-500 does not resolve the dose-response shape.\n\n\\section{MBPP Code Generation}\n\\label{sec:appendix_mbpp}\n\n\\input{tables/tab_mbpp}\n\nMBPP GRPO deltas are uniformly slightly positive across all fine-grained methods (mean $+$1.25\\,pp), but none are statistically significant at this sample size ($N{=}374$; stderr ${\\approx}1.7$\\,pp).\nThis directional consistency may reflect a weak task-specific GRPO effect at the capability floor rather than a violation of reward-accuracy decoupling.\n\n\\section{CKA Scoring Stability}\n\\label{sec:appendix_cka_stability}\n\n\\input{tables/tab_cka_stability}\n\nCKA-based structure rankings are highly stable across calibration data volumes: Spearman $\\rho$ between rankings from 256, 512, and 1024 calibration samples ranges from 0.964 to 0.979, indicating that the scoring criterion is not sensitive to calibration set size.\n\n\\section{Gradient Signal Analysis}\n\\label{sec:appendix_gradient}\n\nWe compare per-layer gradient magnitudes during early GRPO training ($N{=}200$ GSM8K calibration samples) across three pruning criteria using paired Wilcoxon signed-rank tests.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise gradient magnitude ratios during GRPO training. Ratio: mean gradient magnitude of method A divided by method B across 56 parameter groups (28 layers $\\times$ 2 projections). Significant layers: count where paired Wilcoxon signed-rank $p{<}0.05$.}\n\\label{tab:gradient_flow}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nComparison & Gradient Ratio & Sig.\\ Layers \\\\\n\\midrule\nCKA-only vs Standard & 2.89$\\times$ & 55\\,/\\,56 \\\\\nCKA-only vs \\rasp{} & 2.26$\\times$ & 56\\,/\\,56 \\\\\n\\rasp{} vs Standard & 1.28$\\times$ & 45\\,/\\,56 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient magnitude hierarchy (CKA-only $\\gg$ \\rasp{} $>$ Standard) mirrors the recovery capacity hierarchy (GSM8K: 64.39\\% $>$ 60.88\\% $>$ 59.84\\%), with bootstrap 95\\% CIs for all ratios excluding 1.0.\nThis is consistent with diversity preservation enabling stronger training signals during GRPO, though the evidence is correlational: an alternative explanation---that CKA-only retains more functional structure, producing higher initial loss and naturally larger gradients---cannot be ruled out.\n\n\\section{Seed Reproducibility}\n\\label{sec:appendix_seed}\n\nCKA-only GSM8K accuracy across 3 GRPO seeds: 64.37\\% (seed 42), 64.22\\% (seed 123), 64.58\\% (seed 456), yielding mean 64.39\\% $\\pm$ 0.19\\,pp.\nStandard: mean 59.84\\% $\\pm$ 0.38\\,pp across the same 3 seeds.\nSee Table~\\ref{tab:multiseed} for the full summary.\n\n\\section{Sparsity Cliff at 30\\%}\n\\label{sec:appendix_sparsity_cliff}\n\n\\input{tables/table4_sparsity_cliff}\n\nAll tested methods collapse at 30\\% sparsity: Standard retains 4\\% accuracy, \\rasp{} and CKA-only reach 0\\%.\nThis capacity threshold, independent of pruning criterion, validates 20\\% as the operating point and confirms that the recovery capacity spectrum reflects how methods allocate a limited pruning budget.\n\n\\section{Multi-Seed GRPO Results}\n\\label{sec:appendix_multiseed}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Multi-seed GRPO results on GSM8K ($N{=}1{,}319$). CKA-only, Standard, and Random each trained with 3 GRPO seeds (42, 123, 456); pruning calibration and SFT are identical across all runs within each sparsity level.}\n\\label{tab:multiseed}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nSparsity & Method & Mean Acc.\\,(\\%) & Std\\,(pp) & Seeds \\\\\n\\midrule\n\\multirow{4}{*}{20\\%} & CKA-only & 64.39 & 0.19 & 3 \\\\\n & Standard & 59.84 & 0.38 & 3 \\\\\n & \\rasp{} & 60.88 & -- & 1 \\\\\n & Random & 50.72 & 0.15 & 3 \\\\\n\\midrule\n\\multirow{2}{*}{15\\%} & CKA-only & 72.76 & 0.57 & 3 \\\\\n & Standard & 65.56 & 0.50 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 20\\% sparsity, the 4.55\\,pp gap between CKA-only and Standard is robust across seeds, with non-overlapping ranges (CKA-only: 64.22--64.58\\%, Standard: 59.44--60.20\\%).\nStandard shows a wider observed range across seeds (0.76\\,pp vs 0.36\\,pp), consistent with borderline-collapse dynamics where small perturbations produce larger outcome variation.\nRandom (3 seeds: 50.57\\%, 50.72\\%, 50.87\\%; $\\sigma{=}0.15$\\,pp, observed range 0.30\\,pp) converges in a narrow band with SFT accuracy seed-independent at 51.25\\%.\nAll three seeds satisfy GRPO $\\leq$ SFT ($\\Delta{=}{-}0.68$, $-$0.53, $-$0.38\\,pp), confirming that reward-accuracy decoupling is reproducible across seeds even for stagnating methods.\nNote: Standard seed 42 was trained from a separately initialized SFT checkpoint (accuracy 59.21\\% vs.\\ 59.29\\% for seeds 123/456; $\\Delta = 0.08$\\,pp).\nAt 15\\% sparsity, the gap widens to 7.20\\,pp (72.76\\% vs 65.56\\%, $t{\\approx}16.4$, $p{<}0.001$), with non-overlapping ranges (CKA-only: 72.10--73.09\\%, Standard: 65.13--65.43\\%).\n\n\\section{Cross-Sparsity Validation}\n\\label{sec:appendix_cross_sparsity}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-sparsity validation on DeepSeek-R1-Distill-Qwen-7B. GSM8K accuracy ($N{=}1{,}319$) after SFT warmup and GRPO recovery. 15\\% and 20\\% GRPO values are mean over 3 seeds (see Tables~\\ref{tab:decoupling},~\\ref{tab:multiseed}). $^\\ddagger$Single seed. Mean $|\\Delta| \\leq 1$\\,pp across all conditions.}\n\\label{tab:cross_sparsity}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nSparsity & Method & SFT\\,(\\%) & GRPO\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\n\\multirow{2}{*}{15\\%} & CKA-only & 72.18 & \\textbf{72.76{\\scriptsize$\\pm$0.57}} & $+$0.58 \\\\\n & Standard & 66.49 & 65.56{\\scriptsize$\\pm$0.50} & $-$0.93 \\\\\n\\midrule\n\\multirow{2}{*}{20\\%} & CKA-only & 63.91 & 64.39 & $+$0.48 \\\\\n & Standard & 59.29 & 59.84 & $+$0.55 \\\\\n\\midrule\n\\multirow{2}{*}{25\\%$^\\ddagger$} & CKA-only & 60.12 & 59.59 & $-$0.53 \\\\\n & Standard & 50.87 & 51.86 & $+$0.99 \\\\\n\\midrule\n30\\% & All & \\multicolumn{3}{c}{Collapse ($\\leq$4\\%; Table~\\ref{tab:sparsity_cliff})} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 15\\% sparsity (3-seed mean), the CKA-only advantage widens to $+$7.20\\,pp (72.76\\% vs 65.56\\%), compared to $+$4.55\\,pp at 20\\%.\nCKA-only at 15\\% (72.76\\%) represents the highest mean accuracy across all experimental conditions, retaining 80.1\\% of original dense model performance (90.83\\%).\nAt 25\\% sparsity (single seed), Standard's SFT accuracy decline accelerates ($-$7.20\\,pp from 15\\%$\\to$20\\%, $-$8.42\\,pp from 20\\%$\\to$25\\%), while CKA-only's decline decelerates ($-$8.27\\,pp then $-$3.79\\,pp).\nReward-accuracy decoupling is preserved ($|\\Delta| \\leq 1$\\,pp for both methods) despite Standard's near-zero peak reward (0.008).\n\n\\section{Cross-Architecture Validation}\n\\label{sec:appendix_cross_arch}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-architecture validation on Qwen2.5-Math-7B~\\citep{qwen2.5} at 20\\% structured sparsity. Accuracy evaluated on GSM8K ($N{=}200$). Post-SFT reports mean $\\pm$ std over multiple SFT runs. EOS rate: fraction of generations that produce a valid end-of-sequence token.}\n\\label{tab:cross_arch}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & Post-Prune\\,(\\%) & Post-SFT\\,(\\%) & EOS Rate\\,(\\%) \\\\\n\\midrule\nCKA-only & 1.0 & \\textbf{51.50 $\\pm$ 3.53} & 27.0 \\\\\nStandard & 18.5 & 21.00 $\\pm$ 2.88 & 36.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCKA-only pruning causes near-total initial damage on Qwen2.5-Math-7B (1.0\\% post-prune accuracy vs Standard's 18.5\\%), yet SFT recovers CKA-only to 51.50\\% while Standard remains at 21.00\\%.\nThis post-prune accuracy reversal provides strong evidence that recovery capacity is shaped by preserved network structure rather than starting accuracy.\nEOS rates remain below 40\\% for both methods, indicating that SFT warmup is less effective on this architecture; GRPO validation is deferred to future work.\\footnote{Preliminary GRPO evaluation yields 48.60\\% (243/500), but 83.8\\% of responses were truncated at 2048 tokens, precluding direct comparison with SFT results.}\n\n\\section{Structural Overlap Analysis}\n\\label{sec:appendix_overlap}\n\nCKA-only and Standard pruning produce markedly different removal patterns across the 28 layers of DeepSeek-R1-Distill-Qwen-7B at 20\\% sparsity.\nCKA-only concentrates pruning in early layers (L0--9 account for 72.5\\% of removed MLP groups), preserving nearly all structures in later layers (L16--27).\nStandard distributes removals more uniformly, pruning substantial numbers of groups in late layers (L16--18, L22, L25--26).\n\nThe methods share only partial overlap in which structures they remove.\n65 MLP groups are pruned exclusively by CKA-only (retained by Standard), concentrated in L6--9 and L27---structures that gradient importance scores as important but CKA identifies as redundant with neighboring groups.\nConversely, 46+ groups are pruned exclusively by Standard (retained by CKA-only), concentrated in L16--18, L22, and L25--26---structures that gradient importance scores as unimportant but CKA identifies as representationally unique.\n\nThis pattern is consistent with the CKA heatmap (Figure~\\ref{fig:cka_heatmap}): CKA-only's aggressive early-layer pruning disrupts dense representations (low diagonal CKA, $\\mu{=}0.62$) but preserves diverse late-layer pathways, while Standard's uniform pruning maintains dense fidelity ($\\mu{=}0.90$) at the cost of removing unique computational pathways in later layers.\n\n\\section{KL Divergence During GRPO Training}\n\\label{sec:appendix_kl}\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=0.75\\columnwidth]{figures/paper/fig_appendix_kl.pdf}\n    \\caption{KL divergence between the policy and reference model during GRPO training. RASP maintains near-zero KL ($<$0.001), consistent with minimal policy movement during collapse. Random shows the highest KL (${\\sim}$0.004--0.005), indicating more policy exploration. CKA-only and Standard fall between these extremes.}\n    \\label{fig:kl_divergence}\n\\end{figure}\n\n\\section{Depth-First Pruning Baseline}\n\\label{sec:appendix_depth_first}\n\nAs a sanity check, we test whether CKA-only's advantage reflects mere layer-depth bias by constructing a depth-first baseline: synthetic importance scores force removal of late layers first (L18--27: 0.001, L10--17: 0.5, L0--9: 1.0), then standard pruning at 20\\% sparsity.\nBoth SFT (${\\sim}$10\\%) and GRPO (${\\sim}$8\\%) accuracy are near chance (early-stopped at $N{\\approx}50$--88 samples due to conclusive results), confirming that naive depth ordering cannot substitute for criterion-based structure selection.\nThis baseline operates at layer-level granularity (removing entire transformer blocks), unlike CKA-only/Standard/\\rasp{} which prune at MLP channel group level; the granularity difference limits direct comparison with our main results and precludes using this baseline as evidence for the recovery capacity spectrum.\n",
      "numLines": 282,
      "startLine": 1,
      "totalLines": 282
    }
  },
  "sourceToolAssistantUUID": "d5938a14-112f-46f0-b3fa-11804683895c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T04:05:40.133Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GyJpWARWdAP7cP7KeWoAWT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "134d9415-bc7e-40e1-813b-1cd19d5de980",
  "isSidechain": false,
  "requestId": "req_011CbJqe8RAU8hhy9mDRfdxH",
  "type": "assistant",
  "uuid": "50ed9c97-dbe1-446b-9594-03926a050b5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AikNj8BwKMU39MmHyboKMo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12647,
      "cache_read_input_tokens": 38782,
      "output_tokens": 801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 801,
          "cache_read_input_tokens": 38782,
          "cache_creation_input_tokens": 12647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12647
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-23T04:05:40.137Z_

<details><summary>↩ Tool result · `toolu_01GyJpWARWdAP7cP7KeWoAWT`</summary>

```text
1	This work uses publicly available models (DeepSeek-R1-Distill-Qwen, Qwen2.5-Math) and established benchmarks (GSM8K, MATH-500, HumanEval, MBPP); no private data or human subjects are involved.
2	Structured pruning reduces model size and inference memory, which can lower the computational cost and energy consumption of deploying large language models.
3	Our research focuses on the technical analysis of pruning criteria and their interaction with reinforcement learning recovery; we do not foresee direct negative societal impacts from this work.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50ed9c97-dbe1-446b-9594-03926a050b5e",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "7b8dec7f-b57d-4866-b99d-1474b75395f9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/ethics.tex",
      "content": "This work uses publicly available models (DeepSeek-R1-Distill-Qwen, Qwen2.5-Math) and established benchmarks (GSM8K, MATH-500, HumanEval, MBPP); no private data or human subjects are involved.\nStructured pruning reduces model size and inference memory, which can lower the computational cost and energy consumption of deploying large language models.\nOur research focuses on the technical analysis of pruning criteria and their interaction with reinforcement learning recovery; we do not foresee direct negative societal impacts from this work.\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  },
  "sourceToolAssistantUUID": "50ed9c97-dbe1-446b-9594-03926a050b5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T04:05:40.597Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RGiy1HFWhi9Y8QgRXY263N`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b8dec7f-b57d-4866-b99d-1474b75395f9",
  "isSidechain": false,
  "requestId": "req_011CbJqe8RAU8hhy9mDRfdxH",
  "type": "assistant",
  "uuid": "9f622f46-21ab-453e-8b79-c8f3257c3625",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AikNj8BwKMU39MmHyboKMo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12647,
      "cache_read_input_tokens": 38782,
      "output_tokens": 801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 801,
          "cache_read_input_tokens": 38782,
          "cache_creation_input_tokens": 12647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12647
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-23T04:05:40.661Z_

```json
{
  "parentUuid": "cd927b6d-1ddd-4d9e-82b5-01d9710be747",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "4387f81e-d058-4773-8777-1de8aebc9b92",
  "timestamp": "2026-05-23T04:05:40.661Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：recovery_aware_struct_prune Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 6 critical,…",
  "leafUuid": "4387f81e-d058-4773-8777-1de8aebc9b92",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Recovery-aware structured pruning paper audit",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303"
}
```

---

### Assistant

_source line 43 · 2026-05-23T04:05:46.045Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the .tex files. Let me also read the table files that are included in the main text to check for consistency.

Let me now systematically audit across all dimensions.

Let me also do some grep searches for AI style markers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4387f81e-d058-4773-8777-1de8aebc9b92",
  "isSidechain": false,
  "requestId": "req_011CbJqen5pSSL3REKMkD7G2",
  "type": "assistant",
  "uuid": "e161f7bc-d918-47e0-b294-62595670d043",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197ke3DA8XhqbHj96FqgcoL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21179,
      "cache_read_input_tokens": 51429,
      "output_tokens": 1038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21179,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1038,
          "cache_read_input_tokens": 51429,
          "cache_creation_input_tokens": 21179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21179
          },
          "type": "message"
        }
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

_source line 44 · 2026-05-23T04:05:46.055Z_

读取表格文件并进行正则扫描。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e161f7bc-d918-47e0-b294-62595670d043",
  "isSidechain": false,
  "requestId": "req_011CbJqen5pSSL3REKMkD7G2",
  "type": "assistant",
  "uuid": "14c2d51d-716f-478b-829c-fa99f4d516e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197ke3DA8XhqbHj96FqgcoL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21179,
      "cache_read_input_tokens": 51429,
      "output_tokens": 1038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21179,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1038,
          "cache_read_input_tokens": 51429,
          "cache_creation_input_tokens": 21179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21179
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-23T04:05:47.769Z_

<details open><summary>🔧 Tool call — Read · `toolu_019qe8LpW7h8P8ZZmY8ZfF1J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14c2d51d-716f-478b-829c-fa99f4d516e0",
  "isSidechain": false,
  "requestId": "req_011CbJqen5pSSL3REKMkD7G2",
  "type": "assistant",
  "uuid": "1bc060a9-ec61-42c9-925a-5418af8fa8c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197ke3DA8XhqbHj96FqgcoL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21179,
      "cache_read_input_tokens": 51429,
      "output_tokens": 1038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21179,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1038,
          "cache_read_input_tokens": 51429,
          "cache_creation_input_tokens": 21179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21179
          },
          "type": "message"
        }
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

_source line 46 · 2026-05-23T04:05:56.277Z_

<details><summary>↩ Tool result · `toolu_01QmEPTkf9dDK1Bh5eiaS7qq`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:6:ShortGPT~\citep{shortgpt2024}, SliceGPT~\citep{slicegpt2024}, and LaCo~\citep{yang2024laco} target depth pruning, though \citet{shrestha2026layerpruninglimits} show this causes severe reasoning degradation even when classification is preserved; Wanda~\citep{wanda2024} addresses unstructured sparsity; \citet{doingmore2026} revisit the structured-vs-unstructured trade-off under test-time scaling.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:7:For reasoning models, RESP~\citep{resp2025} uses gradient-based importance on self-generated reasoning traces, RAC~\citep{rac2025} reconstructs chain-of-thought during pruning, SSGR~\citep{ssgr2025} uses self-generated calibration data, and \citet{llms2lrms2026} find width pruning more robust than depth pruning for reasoning but do not study RLVR recovery.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:14:$P^2$ Law~\citep{p2law2025} establishes scaling laws for post-training loss after pruning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:23:RL training instability has been studied in the RLHF context: \citet{gao2023overoptimization} characterize reward overoptimization, \citet{dong2025rlplus} document repetitive output collapse during extended RL training, and \citet{shah2025comedy} analyze compounding bias from reward estimation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:25:Our work connects this instability literature to structural pruning, showing that the pruning criterion shapes susceptibility to RL collapse.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:10:Our primary benchmark is GSM8K~\citep{cobbe2021gsm8k}, a set of 1{,}319 grade-school math problems requiring multi-step arithmetic reasoning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:54:    \caption{Training dynamics diagnostics. (a)~$f_0$ (fraction of zero-variance batches): CKA-only stays below 0.35; Standard and \rasp{} remain in the collapse zone ($f_0 > 0.5$) throughout training. (b)~Gradient norm: Standard exhibits a transient minimum of 0.017 at step 90 before recovering to 2.41 at step 100; \rasp{} gradient norms remain predominantly near zero.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:81:This pattern suggests that moderate structural damage (15\%) preserves enough capacity for GRPO to differentially benefit CKA-only pruning, while more aggressive pruning (20--25\%) exceeds the threshold where GRPO can improve upon SFT baselines.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex:5:Under identical GRPO training, CKA-only pruning enables active learning (peak reward 4.4$\times$ Standard), while importance-based methods collapse; extended training to 300 steps confirms this gap is structural.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:11:ShortGPT~\citep{shortgpt2024} and SliceGPT~\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:13:For reasoning models specifically, RESP~\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\% on GSM8K at 40\% structured sparsity without any recovery training.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:15:RAC~\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:40:OPSD~\citep{opsd2026} proposes a post-RL compaction stage that further compresses reasoning traces after RLVR training, reinforcing the view that RLVR-trained models exhibit compressible internal structure.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:42:\paragraph{CKA-based pruning.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:43:CKA~\citep{kornblith2019cka} has been previously applied to pruning, but at a fundamentally different granularity and with a different objective.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:9:This model represents a compelling testbed for our study: as a reasoning-specialized model, its performance depends critically on chain-of-thought capabilities that are acquired through reinforcement learning, making the interaction between structural pruning and RL-based recovery particularly salient.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:12:We use 512 randomly sampled examples from the GSM8K training set~\citep{cobbe2021gsm8k} for all calibration-dependent operations, including importance scoring, CKA computation, and GRASPrune gate training.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:16:\textbf{[Phase 2: We extend evaluation to MMLU~\citep{hendrycks2021mmlu} for broad knowledge, HumanEval~\citep{chen2021humaneval} for code generation, and LongBench~\citep{bai2024longbench} for long-context understanding.]}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:22:\paragraph{Standard Importance-Only Pruning.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:48:\textbf{[Phase 2: We additionally compare SFT recovery using the same GSM8K training data to isolate the effect of the RL-based recovery signal.]}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:69:\textbf{[Phase 2: We additionally report perplexity on WikiText-2 and per-benchmark accuracy on MMLU, HumanEval, and LongBench.]}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:10:\paragraph{Structured pruning.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:26:RASP computes two complementary scores per structure: \emph{importance} $I(h)$ capturing the structure's contribution to reasoning, and \emph{functional overlap} $F(h)$ measuring the degree to which its function is recoverable from other structures.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:78:The key distinction from standard pruning---which ranks solely by $I(h)$---is that RASP additionally down-weights protection of structures whose function overlaps with retained structures.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:87:After pruning, we apply GRPO-based RLVR on mathematical reasoning data (GSM8K and MATH training sets) to recover the pruned model's reasoning ability.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:5:Structured pruning, which removes entire attention heads or MLP channels, offers a hardware-friendly path to compression by reducing both memory footprint and inference latency without requiring specialized sparse-computation support~\citep{llmpruner2023,graspprune2026}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:12:This gap becomes consequential at higher compression ratios (30--45\%), where the pruning method plausibly determines whether RLVR recovery can close the accuracy gap or hits a recovery ceiling.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex:4:\caption{MATH-500 out-of-distribution evaluation ($N{=}500$, greedy decoding, \texttt{max\_new\_tokens=2048}). The method ordering (CKA-only $>$ Standard $>$ Random) is preserved from GSM8K, confirming cross-benchmark consistency. $^\star$GRPO evaluation pending. Best SFT in \textbf{bold}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex:28:\multicolumn{4}{p{0.85\columnwidth}}{\footnotesize $^\dagger$Over half of Dense responses truncated at 2048 tokens (73.6\% at 4096); all pruned models evaluated under the same constraint. $^\ddagger$Evaluated with earlier answer extraction script; re-evaluation pending. $^\star$Pending; will be filled upon completion.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:11:\paragraph{Structured pruning.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:26:All four pruning criteria share a common structural analysis stage that computes two scores per structure: \emph{importance} $I(h)$ capturing the structure's contribution to reasoning, and \emph{functional overlap} $F(h)$ measuring representational redundancy with other structures in the same layer.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:106:After pruning, all four models undergo an identical two-stage recovery pipeline. Any differences in GRPO training dynamics are therefore attributable to the pruning criterion alone.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:111:We restore generation competence through a short SFT phase on chain-of-thought reasoning demonstrations with teacher forcing.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:123:We define \textbf{recovery capacity} as the model's ability to benefit from post-pruning recovery training, operationalized in our GRPO experiments as peak mean reward over the training horizon (Table~\ref{tab:recovery_gradient}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex:10:Recovery capacity captures the model's ability to sustain RL training without collapse, but practitioners seeking accuracy gains may require longer training, different reward formulations, or lower sparsity levels.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex:5:Under identical GRPO training, importance-dominated pruning ($\alpha{=}1.0$) collapses while diversity-preserving criteria achieve active learning (peak reward 4.4$\times$), forming a \emph{recovery capacity spectrum} that tracks preserved representational diversity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:102:    \includegraphics[width=0.85\columnwidth]{figures/paper/fig5_extended_training.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:122:This directional consistency may reflect a weak task-specific GRPO effect at the capability floor rather than a violation of reward-accuracy decoupling.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:139:\caption{Pairwise gradient magnitude ratios during GRPO training. Ratio: mean gradient magnitude of method A divided by method B across 56 parameter groups (28 layers $\times$ 2 projections). Significant layers: count where paired Wilcoxon signed-rank $p{<}0.05$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:272:    \caption{KL divergence between the policy and reference model during GRPO training. RASP maintains near-zero KL ($<$0.001), consistent with minimal policy movement during collapse. Random shows the highest KL (${\sim}$0.004--0.005), indicating more policy exploration. CKA-only and Standard fall between these extremes.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:4:Reasoning Large Language Models can be compressed through structured pruning, but the pruned model must recover its reasoning capabilities through fine-tuning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:6:We show that this hierarchy is an artifact of suboptimal pruning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:8:What determines recovery quality is not \emph{how} you train after pruning, but \emph{which structures} you remove during pruning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:24:Under identical GRPO~\citep{shao2024grpo} training, four criteria produce a \textbf{recovery capacity spectrum}: CKA-only pruning achieves active learning (peak reward 4.4$\times$ Standard), Random stagnates, Standard (importance-only;~\citealp{llmpruner2023}) exhibits borderline collapse, and $\alpha{=}1.0$ collapses fully.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:31:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf72888c-d36d-4639-9005-38fda399f235",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "fdc3984b-e9fd-4303-811c-29ff606bff8a",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:6:ShortGPT~\\citep{shortgpt2024}, SliceGPT~\\citep{slicegpt2024}, and LaCo~\\citep{yang2024laco} target depth pruning, though \\citet{shrestha2026layerpruninglimits} show this causes severe reasoning degradation even when classification is preserved; Wanda~\\citep{wanda2024} addresses unstructured sparsity; \\citet{doingmore2026} revisit the structured-vs-unstructured trade-off under test-time scaling.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:7:For reasoning models, RESP~\\citep{resp2025} uses gradient-based importance on self-generated reasoning traces, RAC~\\citep{rac2025} reconstructs chain-of-thought during pruning, SSGR~\\citep{ssgr2025} uses self-generated calibration data, and \\citet{llms2lrms2026} find width pruning more robust than depth pruning for reasoning but do not study RLVR recovery.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:14:$P^2$ Law~\\citep{p2law2025} establishes scaling laws for post-training loss after pruning.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:23:RL training instability has been studied in the RLHF context: \\citet{gao2023overoptimization} characterize reward overoptimization, \\citet{dong2025rlplus} document repetitive output collapse during extended RL training, and \\citet{shah2025comedy} analyze compounding bias from reward estimation.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:25:Our work connects this instability literature to structural pruning, showing that the pruning criterion shapes susceptibility to RL collapse.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:10:Our primary benchmark is GSM8K~\\citep{cobbe2021gsm8k}, a set of 1{,}319 grade-school math problems requiring multi-step arithmetic reasoning.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:54:    \\caption{Training dynamics diagnostics. (a)~$f_0$ (fraction of zero-variance batches): CKA-only stays below 0.35; Standard and \\rasp{} remain in the collapse zone ($f_0 > 0.5$) throughout training. (b)~Gradient norm: Standard exhibits a transient minimum of 0.017 at step 90 before recovering to 2.41 at step 100; \\rasp{} gradient norms remain predominantly near zero.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:81:This pattern suggests that moderate structural damage (15\\%) preserves enough capacity for GRPO to differentially benefit CKA-only pruning, while more aggressive pruning (20--25\\%) exceeds the threshold where GRPO can improve upon SFT baselines.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex:5:Under identical GRPO training, CKA-only pruning enables active learning (peak reward 4.4$\\times$ Standard), while importance-based methods collapse; extended training to 300 steps confirms this gap is structural.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:11:ShortGPT~\\citep{shortgpt2024} and SliceGPT~\\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:13:For reasoning models specifically, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\% on GSM8K at 40\\% structured sparsity without any recovery training.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:15:RAC~\\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:40:OPSD~\\citep{opsd2026} proposes a post-RL compaction stage that further compresses reasoning traces after RLVR training, reinforcing the view that RLVR-trained models exhibit compressible internal structure.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:42:\\paragraph{CKA-based pruning.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:43:CKA~\\citep{kornblith2019cka} has been previously applied to pruning, but at a fundamentally different granularity and with a different objective.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:9:This model represents a compelling testbed for our study: as a reasoning-specialized model, its performance depends critically on chain-of-thought capabilities that are acquired through reinforcement learning, making the interaction between structural pruning and RL-based recovery particularly salient.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:12:We use 512 randomly sampled examples from the GSM8K training set~\\citep{cobbe2021gsm8k} for all calibration-dependent operations, including importance scoring, CKA computation, and GRASPrune gate training.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:16:\\textbf{[Phase 2: We extend evaluation to MMLU~\\citep{hendrycks2021mmlu} for broad knowledge, HumanEval~\\citep{chen2021humaneval} for code generation, and LongBench~\\citep{bai2024longbench} for long-context understanding.]}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:22:\\paragraph{Standard Importance-Only Pruning.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:48:\\textbf{[Phase 2: We additionally compare SFT recovery using the same GSM8K training data to isolate the effect of the RL-based recovery signal.]}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:69:\\textbf{[Phase 2: We additionally report perplexity on WikiText-2 and per-benchmark accuracy on MMLU, HumanEval, and LongBench.]}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:10:\\paragraph{Structured pruning.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:26:RASP computes two complementary scores per structure: \\emph{importance} $I(h)$ capturing the structure's contribution to reasoning, and \\emph{functional overlap} $F(h)$ measuring the degree to which its function is recoverable from other structures.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:78:The key distinction from standard pruning---which ranks solely by $I(h)$---is that RASP additionally down-weights protection of structures whose function overlaps with retained structures.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:87:After pruning, we apply GRPO-based RLVR on mathematical reasoning data (GSM8K and MATH training sets) to recover the pruned model's reasoning ability.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:5:Structured pruning, which removes entire attention heads or MLP channels, offers a hardware-friendly path to compression by reducing both memory footprint and inference latency without requiring specialized sparse-computation support~\\citep{llmpruner2023,graspprune2026}.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:12:This gap becomes consequential at higher compression ratios (30--45\\%), where the pruning method plausibly determines whether RLVR recovery can close the accuracy gap or hits a recovery ceiling.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex:4:\\caption{MATH-500 out-of-distribution evaluation ($N{=}500$, greedy decoding, \\texttt{max\\_new\\_tokens=2048}). The method ordering (CKA-only $>$ Standard $>$ Random) is preserved from GSM8K, confirming cross-benchmark consistency. $^\\star$GRPO evaluation pending. Best SFT in \\textbf{bold}.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex:28:\\multicolumn{4}{p{0.85\\columnwidth}}{\\footnotesize $^\\dagger$Over half of Dense responses truncated at 2048 tokens (73.6\\% at 4096); all pruned models evaluated under the same constraint. $^\\ddagger$Evaluated with earlier answer extraction script; re-evaluation pending. $^\\star$Pending; will be filled upon completion.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:11:\\paragraph{Structured pruning.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:26:All four pruning criteria share a common structural analysis stage that computes two scores per structure: \\emph{importance} $I(h)$ capturing the structure's contribution to reasoning, and \\emph{functional overlap} $F(h)$ measuring representational redundancy with other structures in the same layer.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:106:After pruning, all four models undergo an identical two-stage recovery pipeline. Any differences in GRPO training dynamics are therefore attributable to the pruning criterion alone.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:111:We restore generation competence through a short SFT phase on chain-of-thought reasoning demonstrations with teacher forcing.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:123:We define \\textbf{recovery capacity} as the model's ability to benefit from post-pruning recovery training, operationalized in our GRPO experiments as peak mean reward over the training horizon (Table~\\ref{tab:recovery_gradient}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex:10:Recovery capacity captures the model's ability to sustain RL training without collapse, but practitioners seeking accuracy gains may require longer training, different reward formulations, or lower sparsity levels.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex:5:Under identical GRPO training, importance-dominated pruning ($\\alpha{=}1.0$) collapses while diversity-preserving criteria achieve active learning (peak reward 4.4$\\times$), forming a \\emph{recovery capacity spectrum} that tracks preserved representational diversity.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:102:    \\includegraphics[width=0.85\\columnwidth]{figures/paper/fig5_extended_training.pdf}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:122:This directional consistency may reflect a weak task-specific GRPO effect at the capability floor rather than a violation of reward-accuracy decoupling.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:139:\\caption{Pairwise gradient magnitude ratios during GRPO training. Ratio: mean gradient magnitude of method A divided by method B across 56 parameter groups (28 layers $\\times$ 2 projections). Significant layers: count where paired Wilcoxon signed-rank $p{<}0.05$.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:272:    \\caption{KL divergence between the policy and reference model during GRPO training. RASP maintains near-zero KL ($<$0.001), consistent with minimal policy movement during collapse. Random shows the highest KL (${\\sim}$0.004--0.005), indicating more policy exploration. CKA-only and Standard fall between these extremes.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:4:Reasoning Large Language Models can be compressed through structured pruning, but the pruned model must recover its reasoning capabilities through fine-tuning.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:6:We show that this hierarchy is an artifact of suboptimal pruning.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:8:What determines recovery quality is not \\emph{how} you train after pruning, but \\emph{which structures} you remove during pruning.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:24:Under identical GRPO~\\citep{shao2024grpo} training, four criteria produce a \\textbf{recovery capacity spectrum}: CKA-only pruning achieves active learning (peak reward 4.4$\\times$ Standard), Random stagnates, Standard (importance-only;~\\citealp{llmpruner2023}) exhibits borderline collapse, and $\\alpha{=}1.0$ collapses fully.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:31:[Omitted long matching line]",
    "numLines": 45
  },
  "sourceToolAssistantUUID": "bf72888c-d36d-4639-9005-38fda399f235",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-23T04:05:47.776Z_

<details><summary>↩ Tool result · `toolu_019qe8LpW7h8P8ZZmY8ZfF1J`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Recovery capacity spectrum: GRPO dynamics for four pruning criteria at 20\% sparsity under identical configuration (lr $1{\times}10^{-6}$, $\beta{=}0.01$, $T{=}0.4$, 100 steps). Peak reward = best across 100 training steps. $f_0$: fraction of training batches where all sampled completions receive identical reward (lower = healthier exploration). Best in \textbf{bold}.}
5	\label{tab:recovery_gradient}
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	Method & Peak Rew.\,$\uparrow$ & Mean Rew.\,$\uparrow$ & Min $f_0$\,$\downarrow$ & Behavior \\
9	\midrule
10	CKA-only & \textbf{0.354} & \textbf{0.285} & \textbf{0.125} & Active learning \\
11	Random & 0.190 & 0.164 & 0.300 & Stagnation \\
12	Standard & 0.081 & 0.050 & 0.500 & Borderline collapse \\
13	\rasp{}$^\ddagger$ & 0.061 & 0.031 & 0.675 & Full collapse \\
14	\bottomrule
15	\multicolumn{5}{l}{\footnotesize $^\ddagger$Single seed ($N{=}1$). CKA-only, Standard, and Random validated with 3 seeds (Table~\ref{tab:decoupling}).}
16	\end{tabular}
17	\end{table}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bc060a9-ec61-42c9-925a-5418af8fa8c2",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "45a3d41f-9ce1-4a70-b59d-26c47981b9ba",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Recovery capacity spectrum: GRPO dynamics for four pruning criteria at 20\\% sparsity under identical configuration (lr $1{\\times}10^{-6}$, $\\beta{=}0.01$, $T{=}0.4$, 100 steps). Peak reward = best across 100 training steps. $f_0$: fraction of training batches where all sampled completions receive identical reward (lower = healthier exploration). Best in \\textbf{bold}.}\n\\label{tab:recovery_gradient}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nMethod & Peak Rew.\\,$\\uparrow$ & Mean Rew.\\,$\\uparrow$ & Min $f_0$\\,$\\downarrow$ & Behavior \\\\\n\\midrule\nCKA-only & \\textbf{0.354} & \\textbf{0.285} & \\textbf{0.125} & Active learning \\\\\nRandom & 0.190 & 0.164 & 0.300 & Stagnation \\\\\nStandard & 0.081 & 0.050 & 0.500 & Borderline collapse \\\\\n\\rasp{}$^\\ddagger$ & 0.061 & 0.031 & 0.675 & Full collapse \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\ddagger$Single seed ($N{=}1$). CKA-only, Standard, and Random validated with 3 seeds (Table~\\ref{tab:decoupling}).}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  },
  "sourceToolAssistantUUID": "1bc060a9-ec61-42c9-925a-5418af8fa8c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-23T04:05:48.807Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FxEmqEBdHmYDNG5188hwBP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45a3d41f-9ce1-4a70-b59d-26c47981b9ba",
  "isSidechain": false,
  "requestId": "req_011CbJqen5pSSL3REKMkD7G2",
  "type": "assistant",
  "uuid": "6820df27-bd5a-43ff-8013-4e01956d191b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197ke3DA8XhqbHj96FqgcoL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21179,
      "cache_read_input_tokens": 51429,
      "output_tokens": 1038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21179,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1038,
          "cache_read_input_tokens": 51429,
          "cache_creation_input_tokens": 21179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21179
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-23T04:05:48.826Z_

<details><summary>↩ Tool result · `toolu_01FxEmqEBdHmYDNG5188hwBP`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{GRPO responsiveness on GSM8K ($N{=}1{,}319$, greedy decoding). All pruned models use the controlled v5 GRPO configuration (identical hyperparameters including \texttt{reward\_desert\_patience}{$=$}50), evaluated at step 100. CKA-only, Standard, and Random report mean $\pm$ std over 3 GRPO seeds; \rasp{} uses a single seed. Best in \textbf{bold}.}
5	\label{tab:decoupling}
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	Model & SFT Acc.\,(\%) & GRPO Acc.\,(\%) & $\Delta$\,(pp) & Peak Rew. \\
9	\midrule
10	Unpruned & \textbf{81.27} & \textbf{81.27} & $\phantom{-}$0.00 & \textbf{0.669} \\
11	CKA-only 20\% & 63.91 & 64.39{\scriptsize$\pm$0.19} & $+$0.48 & 0.354 \\
12	Standard 20\% & 59.29 & 59.84{\scriptsize$\pm$0.38} & $+$0.55 & 0.081 \\
13	\rasp{} 20\% & 61.49 & 60.88 & $-$0.61 & 0.061 \\
14	Random 20\% & 51.25 & 50.72{\scriptsize$\pm$0.15} & $-$0.53 & 0.190 \\
15	\midrule
16	ShortGPT 20\%$^\dagger$ & 44.73 & 43.37 & $-$1.36 & -- \\
17	\bottomrule
18	\multicolumn{5}{l}{\footnotesize $^\dagger$Depth pruning baseline~\citep{shortgpt2024}; removes entire layers.} \\
19	\end{tabular}
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6820df27-bd5a-43ff-8013-4e01956d191b",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "190d968d-9449-4c47-9127-f7a590d6e237",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{GRPO responsiveness on GSM8K ($N{=}1{,}319$, greedy decoding). All pruned models use the controlled v5 GRPO configuration (identical hyperparameters including \\texttt{reward\\_desert\\_patience}{$=$}50), evaluated at step 100. CKA-only, Standard, and Random report mean $\\pm$ std over 3 GRPO seeds; \\rasp{} uses a single seed. Best in \\textbf{bold}.}\n\\label{tab:decoupling}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & SFT Acc.\\,(\\%) & GRPO Acc.\\,(\\%) & $\\Delta$\\,(pp) & Peak Rew. \\\\\n\\midrule\nUnpruned & \\textbf{81.27} & \\textbf{81.27} & $\\phantom{-}$0.00 & \\textbf{0.669} \\\\\nCKA-only 20\\% & 63.91 & 64.39{\\scriptsize$\\pm$0.19} & $+$0.48 & 0.354 \\\\\nStandard 20\\% & 59.29 & 59.84{\\scriptsize$\\pm$0.38} & $+$0.55 & 0.081 \\\\\n\\rasp{} 20\\% & 61.49 & 60.88 & $-$0.61 & 0.061 \\\\\nRandom 20\\% & 51.25 & 50.72{\\scriptsize$\\pm$0.15} & $-$0.53 & 0.190 \\\\\n\\midrule\nShortGPT 20\\%$^\\dagger$ & 44.73 & 43.37 & $-$1.36 & -- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$Depth pruning baseline~\\citep{shortgpt2024}; removes entire layers.} \\\\\n\\end{tabular}\n\\end{table}\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  },
  "sourceToolAssistantUUID": "6820df27-bd5a-43ff-8013-4e01956d191b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-23T04:05:49.139Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GoE1ZKiePNwPde5e9W7wUJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "190d968d-9449-4c47-9127-f7a590d6e237",
  "isSidechain": false,
  "requestId": "req_011CbJqen5pSSL3REKMkD7G2",
  "type": "assistant",
  "uuid": "1e1bf581-1744-4e7d-bd6b-0c85a82bdc81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197ke3DA8XhqbHj96FqgcoL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21179,
      "cache_read_input_tokens": 51429,
      "output_tokens": 1038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21179,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1038,
          "cache_read_input_tokens": 51429,
          "cache_creation_input_tokens": 21179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21179
          },
          "type": "message"
        }
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

_source line 51 · 2026-05-23T04:05:49.151Z_

<details><summary>↩ Tool result · `toolu_01GoE1ZKiePNwPde5e9W7wUJ`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Cross-scale validation at 20\% sparsity. 7B: DeepSeek-R1-Distill-Qwen-7B (GSM8K mean over 3 seeds for CKA-only and Standard; see Table~\ref{tab:decoupling}). 1.5B: DeepSeek-R1-Distill-Qwen-1.5B (single seed). GSM8K accuracy ($N{=}1{,}319$). 7B reward = peak across 100 GRPO steps (cf.\ Table~\ref{tab:recovery_gradient}); 1.5B reward = mean across training steps.}
5	\label{tab:cross_scale}
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	\multirow{2}{*}{Method} & \multicolumn{2}{c}{7B} & \multicolumn{2}{c}{1.5B} \\
9	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
10	 & Peak Rew. & GSM8K\,(\%) & Rew. & GSM8K\,(\%) \\
11	\midrule
12	CKA-only & \textbf{0.354} & \textbf{64.39} & \textbf{0.238} & \textbf{35.48} \\
13	Standard & 0.081 & 59.84 & 0.084 & 22.29 \\
14	\rasp{} & 0.061 & 60.88 & 0.099 & 26.16 \\
15	Random & 0.190 & -- & -- & -- \\
16	\bottomrule
17	\end{tabular}
18	\end{table}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e1bf581-1744-4e7d-bd6b-0c85a82bdc81",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "8036e544-0faf-415f-ade2-40bcfde993f4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-scale validation at 20\\% sparsity. 7B: DeepSeek-R1-Distill-Qwen-7B (GSM8K mean over 3 seeds for CKA-only and Standard; see Table~\\ref{tab:decoupling}). 1.5B: DeepSeek-R1-Distill-Qwen-1.5B (single seed). GSM8K accuracy ($N{=}1{,}319$). 7B reward = peak across 100 GRPO steps (cf.\\ Table~\\ref{tab:recovery_gradient}); 1.5B reward = mean across training steps.}\n\\label{tab:cross_scale}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\multirow{2}{*}{Method} & \\multicolumn{2}{c}{7B} & \\multicolumn{2}{c}{1.5B} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n & Peak Rew. & GSM8K\\,(\\%) & Rew. & GSM8K\\,(\\%) \\\\\n\\midrule\nCKA-only & \\textbf{0.354} & \\textbf{64.39} & \\textbf{0.238} & \\textbf{35.48} \\\\\nStandard & 0.081 & 59.84 & 0.084 & 22.29 \\\\\n\\rasp{} & 0.061 & 60.88 & 0.099 & 26.16 \\\\\nRandom & 0.190 & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  },
  "sourceToolAssistantUUID": "1e1bf581-1744-4e7d-bd6b-0c85a82bdc81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-23T04:05:50.261Z_

<details open><summary>🔧 Tool call — Read · `toolu_011HZMEewJ3DwYBycoyVEkCT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8036e544-0faf-415f-ade2-40bcfde993f4",
  "isSidechain": false,
  "requestId": "req_011CbJqen5pSSL3REKMkD7G2",
  "type": "assistant",
  "uuid": "31a0b5f1-bae9-4624-846c-4116ac87e8e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197ke3DA8XhqbHj96FqgcoL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21179,
      "cache_read_input_tokens": 51429,
      "output_tokens": 1038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21179,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1038,
          "cache_read_input_tokens": 51429,
          "cache_creation_input_tokens": 21179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21179
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-23T04:05:50.269Z_

<details><summary>↩ Tool result · `toolu_011HZMEewJ3DwYBycoyVEkCT`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Dose-response analysis: effect of CKA coefficient $\alpha$ on GSM8K accuracy ($N{=}1{,}319$) at 20\% MLP channel sparsity. $\alpha{=}0$ reduces to Standard (importance-only); higher $\alpha$ weights representational diversity. Best in \textbf{bold}.}
5	\label{tab:alpha}
6	\begin{tabular}{@{}cccc@{}}
7	\toprule
8	$\alpha$ & SFT Acc.\,(\%) & GRPO Acc.\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	0.5 & 60.73 & 61.18 & $+$0.45 \\
11	1.0 & 61.49 & 60.88 & $-$0.61 \\
12	\textbf{2.0} & \textbf{64.97} & \textbf{66.11} & $+$1.14 \\
13	3.0 & 64.14 & 63.46 & $-$0.68 \\
14	4.0 & 61.94 & 62.77 & $+$0.83 \\
15	\bottomrule
16	\end{tabular}
17	\end{table}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31a0b5f1-bae9-4624-846c-4116ac87e8e4",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "5966b111-97a6-4c67-9a8d-0d100e9383cf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dose-response analysis: effect of CKA coefficient $\\alpha$ on GSM8K accuracy ($N{=}1{,}319$) at 20\\% MLP channel sparsity. $\\alpha{=}0$ reduces to Standard (importance-only); higher $\\alpha$ weights representational diversity. Best in \\textbf{bold}.}\n\\label{tab:alpha}\n\\begin{tabular}{@{}cccc@{}}\n\\toprule\n$\\alpha$ & SFT Acc.\\,(\\%) & GRPO Acc.\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\n0.5 & 60.73 & 61.18 & $+$0.45 \\\\\n1.0 & 61.49 & 60.88 & $-$0.61 \\\\\n\\textbf{2.0} & \\textbf{64.97} & \\textbf{66.11} & $+$1.14 \\\\\n3.0 & 64.14 & 63.46 & $-$0.68 \\\\\n4.0 & 61.94 & 62.77 & $+$0.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  },
  "sourceToolAssistantUUID": "31a0b5f1-bae9-4624-846c-4116ac87e8e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-23T04:05:52.092Z_

<details open><summary>🔧 Tool call — Grep · `toolu_014GADz1TrkQEVHNhwAzfkjU`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5966b111-97a6-4c67-9a8d-0d100e9383cf",
  "isSidechain": false,
  "requestId": "req_011CbJqen5pSSL3REKMkD7G2",
  "type": "assistant",
  "uuid": "e1833967-1d60-4c99-a82d-cfc65f19bba4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197ke3DA8XhqbHj96FqgcoL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21179,
      "cache_read_input_tokens": 51429,
      "output_tokens": 1038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21179,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1038,
          "cache_read_input_tokens": 51429,
          "cache_creation_input_tokens": 21179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21179
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-23T04:05:52.117Z_

<details><summary>↩ Tool result · `toolu_014GADz1TrkQEVHNhwAzfkjU`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex:1:% Limitations — required by ACL/EMNLP
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1833967-1d60-4c99-a82d-cfc65f19bba4",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "cbfd3239-572e-4f4c-9870-40a96c0ea0f9",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex:1:% Limitations — required by ACL/EMNLP",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "e1833967-1d60-4c99-a82d-cfc65f19bba4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-23T04:05:52.540Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01XKVcj2YDd7xVECu3qSc1vq`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbfd3239-572e-4f4c-9870-40a96c0ea0f9",
  "isSidechain": false,
  "requestId": "req_011CbJqen5pSSL3REKMkD7G2",
  "type": "assistant",
  "uuid": "cf1efada-f80e-481b-b3be-2c93e0482f6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197ke3DA8XhqbHj96FqgcoL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21179,
      "cache_read_input_tokens": 51429,
      "output_tokens": 1038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21179,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1038,
          "cache_read_input_tokens": 51429,
          "cache_creation_input_tokens": 21179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21179
          },
          "type": "message"
        }
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

_source line 57 · 2026-05-23T04:05:52.560Z_

<details><summary>↩ Tool result · `toolu_01XKVcj2YDd7xVECu3qSc1vq`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf1efada-f80e-481b-b3be-2c93e0482f6e",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "f6a3e57b-bc10-457a-bd2b-8118c8cd9ab4",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "cf1efada-f80e-481b-b3be-2c93e0482f6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-23T04:05:53.957Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01FLbvE6ekqfSNhryjXbXpWH`</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6a3e57b-bc10-457a-bd2b-8118c8cd9ab4",
  "isSidechain": false,
  "requestId": "req_011CbJqen5pSSL3REKMkD7G2",
  "type": "assistant",
  "uuid": "9580afe4-1ce5-4743-a58b-2691696f8b4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197ke3DA8XhqbHj96FqgcoL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21179,
      "cache_read_input_tokens": 51429,
      "output_tokens": 1038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21179,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1038,
          "cache_read_input_tokens": 51429,
          "cache_creation_input_tokens": 21179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21179
          },
          "type": "message"
        }
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

_source line 59 · 2026-05-23T04:05:53.970Z_

<details><summary>↩ Tool result · `toolu_01FLbvE6ekqfSNhryjXbXpWH`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:12:\citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, significantly outperforming SFT, but evaluate only importance-based pruning; our controlled experiments demonstrate that this RLVR${>}$SFT advantage vanishes under diversity-preserving pruning---it is a property of the pruning criterion, not of RL training itself.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:21:\citet{rlsqueezes2026} show that RLVR \emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \emph{expands} correct ones via local imitation---predicting RL--SFT complementarity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:62:Standard pruning exhibits borderline collapse (Figure~\ref{fig:collapse_dynamics}): reward peaks at 0.081 (step 40) then oscillates near 0.05, with $f_0 \geq 0.500$ throughout---more than half of batches produce no learning signal.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:73:GRPO reward trajectory reflects training capacity---the model's ability to learn from RL signal---not downstream accuracy, a phenomenon we term \emph{reward-accuracy decoupling} (mean $|\Delta| {=} 0.54$\,pp, max $1.14$\,pp on GSM8K across all fine-grained criteria and sparsity levels).
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:130:On Qwen2.5-Math-7B at 20\% sparsity (Table~\ref{tab:cross_arch}, Appendix~\ref{sec:appendix_cross_arch}), CKA-only causes near-total initial damage (1.0\% vs Standard's 18.5\%) yet SFT recovers it to 51.50\% $\pm$ 3.53 while Standard remains at 21.00\% $\pm$ 2.88 ($N{=}200$)---confirming that recoverability is shaped by preserved structure, not starting accuracy.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex:10:Recent work shows that RL fine-tuning updates only 5--30\% of parameters~\citep{mukherjee2025rlsubnetworks}; whether CKA-based pruning preferentially preserves structures within this active subnetwork---consistent with the Lottery Ticket Hypothesis~\citep{frankle2019lth}---is an open question that would provide a complementary mechanistic explanation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:7:Structured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:11:ShortGPT~\citep{shortgpt2024} and SliceGPT~\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:25:This establishes RLVR as the preferred recovery paradigm for reasoning models, but Self-Healing treats the pruning method as a black box and tests only one compression ratio---it does not study whether the \emph{choice} of what to prune affects how well RLVR can recover.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:28:PASER~\citep{paser2025} optimizes which recovery \emph{data} to use through manifold learning and capability-aware budget allocation---complementary to RASP, which optimizes which \emph{structures} to prune for recoverability.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:39:This asymmetry provides the theoretical foundation for RASP---structures with high functional overlap are more amenable to RLVR's redistribution mechanism, as their function can be absorbed by similar retained structures during global policy optimization, whereas SFT's trajectory-imitation objective cannot achieve such redistribution.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:47:In contrast, RASP uses \emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability under RLVR---a finer granularity (width vs.\ depth pruning) optimizing for a different objective (post-recovery reasoning performance vs.\ immediate accuracy preservation).
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:5:The core insight is that structures with high functional overlap---those whose computations are redundant with other retained structures---are more recoverable under RLVR, because reinforcement learning can redistribute their function through global exploration~\citep{rlsqueezes2026}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:11:Given a pretrained transformer $\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units---attention heads or MLP channels---to reduce model size while maintaining hardware-friendly dense computation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:58:Unlike prior work that uses inter-layer CKA to identify globally redundant layers for depth pruning~\citep{mpruner2024,lachance2024cka}, RASP uses \emph{intra-layer} CKA between individual GQA groups to predict per-structure recoverability---a fundamentally different granularity and objective.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:78:The key distinction from standard pruning---which ranks solely by $I(h)$---is that RASP additionally down-weights protection of structures whose function overlaps with retained structures.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:93:Structures with high functional overlap $F(h)$ are precisely those whose function can be absorbed by similar retained structures through RLVR's global optimization---the theoretical basis for RASP's scoring criterion.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:4:Large language models with reasoning capabilities---such as those trained with Reinforcement Learning with Verifiable Rewards (RLVR)---achieve strong performance on mathematical and logical tasks but incur substantial deployment costs due to their parameter counts and the extended chain-of-thought traces they generate~\citep{shao2024grpo}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:11:No prior work has studied whether the \emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning ability---or whether this pruning-recovery interaction differs when recovery uses SFT instead of RLVR.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:16:RLVR's recovery mechanism---global exploration across the policy space---can redistribute the function of a removed structure to other structures that perform similar computations.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:19:We hypothesize that functional redundancy, measured as intra-layer representational similarity via Centered Kernel Alignment (CKA;~\citealp{kornblith2019cka}), positively predicts RLVR recoverability but is a weaker predictor of SFT recoverability---since SFT's trajectory-imitation objective cannot redistribute function through global exploration.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:29:Unlike prior CKA-based pruning methods that use inter-layer similarity to identify globally redundant layers for depth pruning~\citep{mpruner2024,lachance2024cka}, RASP uses intra-layer CKA between individual structures (attention head groups, MLP channels) to predict per-structure recoverability under a specific recovery paradigm---a finer granularity optimizing for a fundamentally different objective.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:31:This work extends the notion of trainability from the Lottery Ticket Hypothesis~\citep{frankle2019lth}---which asks which subnetworks can be effectively trained---to what we term \emph{paradigm-conditioned prunability}: the optimal set of structures to retain depends not only on the task but on the recovery paradigm, as RLVR and SFT impose fundamentally different requirements on the retained architecture.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex:12:\multicolumn{4}{l}{\textit{20\% sparsity --- method comparison}} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex:18:\multicolumn{4}{l}{\textit{20\% sparsity --- $\alpha$ dose-response}} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table2_recovery.tex:11:CKA-only 20\% & \underline{63.91} & TBD & --- & \underline{0.354} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:124:We track four diagnostic measures---mean reward, zero-variance batch fraction ($f_0$), gradient norm, and KL divergence---to distinguish \emph{active learning} (rising reward, low $f_0$), \emph{stagnation} (flat reward), and \emph{collapse} (declining reward, high $f_0$, vanishing gradients).
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex:9:Reward-accuracy decoupling at 20--25\% sparsity means that recovery capacity---operationalized as peak reward---does not predict downstream accuracy improvements within our training horizon.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex:1:Fine-grained structured pruning of reasoning Large Language Models (LLMs)---removing MLP channel groups rather than entire layers---is typically followed by recovery training (SFT or RLVR) to restore reasoning capabilities.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:153:This is consistent with diversity preservation enabling stronger training signals during GRPO, though the evidence is correlational: an alternative explanation---that CKA-only retains more functional structure, producing higher initial loss and naturally larger gradients---cannot be ruled out.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:261:65 MLP groups are pruned exclusively by CKA-only (retained by Standard), concentrated in L6--9 and L27---structures that gradient importance scores as important but CKA identifies as redundant with neighboring groups.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:262:Conversely, 46+ groups are pruned exclusively by Standard (retained by CKA-only), concentrated in L16--18, L22, and L25--26---structures that gradient importance scores as unimportant but CKA identifies as representationally unique.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:5:The dominant assumption is that the recovery paradigm---SFT versus RLVR---determines recovery quality: \citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, significantly outperforming SFT.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:11:\citet{rlsqueezes2026} show that RL and SFT impose fundamentally different demands on model representations---RL compresses incorrect paths while SFT expands correct ones---suggesting that pruning decisions should affect RL trainability.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:18:\caption{Dose-response curve for the CKA diversity coefficient $\alpha$ at 20\% MLP channel sparsity on GSM8K ($N{=}1{,}319$). Recovery accuracy follows an inverted-U, peaking at $\alpha{=}2.0$ (66.11\%). SFT and GRPO curves nearly overlap ($|\Delta| \leq 1.14$\,pp at every point), visually demonstrating reward-accuracy decoupling: the pruning criterion---not the recovery paradigm---determines outcome.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9580afe4-1ce5-4743-a58b-2691696f8b4b",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "99c6d09e-dc12-47be-b90c-134c8d06bc0e",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:12:\\citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, significantly outperforming SFT, but evaluate only importance-based pruning; our controlled experiments demonstrate that this RLVR${>}$SFT advantage vanishes under diversity-preserving pruning---it is a property of the pruning criterion, not of RL training itself.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:21:\\citet{rlsqueezes2026} show that RLVR \\emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \\emph{expands} correct ones via local imitation---predicting RL--SFT complementarity.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:62:Standard pruning exhibits borderline collapse (Figure~\\ref{fig:collapse_dynamics}): reward peaks at 0.081 (step 40) then oscillates near 0.05, with $f_0 \\geq 0.500$ throughout---more than half of batches produce no learning signal.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:73:GRPO reward trajectory reflects training capacity---the model's ability to learn from RL signal---not downstream accuracy, a phenomenon we term \\emph{reward-accuracy decoupling} (mean $|\\Delta| {=} 0.54$\\,pp, max $1.14$\\,pp on GSM8K across all fine-grained criteria and sparsity levels).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:130:On Qwen2.5-Math-7B at 20\\% sparsity (Table~\\ref{tab:cross_arch}, Appendix~\\ref{sec:appendix_cross_arch}), CKA-only causes near-total initial damage (1.0\\% vs Standard's 18.5\\%) yet SFT recovers it to 51.50\\% $\\pm$ 3.53 while Standard remains at 21.00\\% $\\pm$ 2.88 ($N{=}200$)---confirming that recoverability is shaped by preserved structure, not starting accuracy.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex:10:Recent work shows that RL fine-tuning updates only 5--30\\% of parameters~\\citep{mukherjee2025rlsubnetworks}; whether CKA-based pruning preferentially preserves structures within this active subnetwork---consistent with the Lottery Ticket Hypothesis~\\citep{frankle2019lth}---is an open question that would provide a complementary mechanistic explanation.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:7:Structured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:11:ShortGPT~\\citep{shortgpt2024} and SliceGPT~\\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:25:This establishes RLVR as the preferred recovery paradigm for reasoning models, but Self-Healing treats the pruning method as a black box and tests only one compression ratio---it does not study whether the \\emph{choice} of what to prune affects how well RLVR can recover.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:28:PASER~\\citep{paser2025} optimizes which recovery \\emph{data} to use through manifold learning and capability-aware budget allocation---complementary to RASP, which optimizes which \\emph{structures} to prune for recoverability.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:39:This asymmetry provides the theoretical foundation for RASP---structures with high functional overlap are more amenable to RLVR's redistribution mechanism, as their function can be absorbed by similar retained structures during global policy optimization, whereas SFT's trajectory-imitation objective cannot achieve such redistribution.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:47:In contrast, RASP uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability under RLVR---a finer granularity (width vs.\\ depth pruning) optimizing for a different objective (post-recovery reasoning performance vs.\\ immediate accuracy preservation).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:5:The core insight is that structures with high functional overlap---those whose computations are redundant with other retained structures---are more recoverable under RLVR, because reinforcement learning can redistribute their function through global exploration~\\citep{rlsqueezes2026}.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:11:Given a pretrained transformer $\\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units---attention heads or MLP channels---to reduce model size while maintaining hardware-friendly dense computation.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:58:Unlike prior work that uses inter-layer CKA to identify globally redundant layers for depth pruning~\\citep{mpruner2024,lachance2024cka}, RASP uses \\emph{intra-layer} CKA between individual GQA groups to predict per-structure recoverability---a fundamentally different granularity and objective.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:78:The key distinction from standard pruning---which ranks solely by $I(h)$---is that RASP additionally down-weights protection of structures whose function overlaps with retained structures.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:93:Structures with high functional overlap $F(h)$ are precisely those whose function can be absorbed by similar retained structures through RLVR's global optimization---the theoretical basis for RASP's scoring criterion.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:4:Large language models with reasoning capabilities---such as those trained with Reinforcement Learning with Verifiable Rewards (RLVR)---achieve strong performance on mathematical and logical tasks but incur substantial deployment costs due to their parameter counts and the extended chain-of-thought traces they generate~\\citep{shao2024grpo}.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:11:No prior work has studied whether the \\emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning ability---or whether this pruning-recovery interaction differs when recovery uses SFT instead of RLVR.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:16:RLVR's recovery mechanism---global exploration across the policy space---can redistribute the function of a removed structure to other structures that perform similar computations.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:19:We hypothesize that functional redundancy, measured as intra-layer representational similarity via Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}), positively predicts RLVR recoverability but is a weaker predictor of SFT recoverability---since SFT's trajectory-imitation objective cannot redistribute function through global exploration.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:29:Unlike prior CKA-based pruning methods that use inter-layer similarity to identify globally redundant layers for depth pruning~\\citep{mpruner2024,lachance2024cka}, RASP uses intra-layer CKA between individual structures (attention head groups, MLP channels) to predict per-structure recoverability under a specific recovery paradigm---a finer granularity optimizing for a fundamentally different objective.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:31:This work extends the notion of trainability from the Lottery Ticket Hypothesis~\\citep{frankle2019lth}---which asks which subnetworks can be effectively trained---to what we term \\emph{paradigm-conditioned prunability}: the optimal set of structures to retain depends not only on the task but on the recovery paradigm, as RLVR and SFT impose fundamentally different requirements on the retained architecture.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex:12:\\multicolumn{4}{l}{\\textit{20\\% sparsity --- method comparison}} \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex:18:\\multicolumn{4}{l}{\\textit{20\\% sparsity --- $\\alpha$ dose-response}} \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table2_recovery.tex:11:CKA-only 20\\% & \\underline{63.91} & TBD & --- & \\underline{0.354} \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:124:We track four diagnostic measures---mean reward, zero-variance batch fraction ($f_0$), gradient norm, and KL divergence---to distinguish \\emph{active learning} (rising reward, low $f_0$), \\emph{stagnation} (flat reward), and \\emph{collapse} (declining reward, high $f_0$, vanishing gradients).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex:9:Reward-accuracy decoupling at 20--25\\% sparsity means that recovery capacity---operationalized as peak reward---does not predict downstream accuracy improvements within our training horizon.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex:1:Fine-grained structured pruning of reasoning Large Language Models (LLMs)---removing MLP channel groups rather than entire layers---is typically followed by recovery training (SFT or RLVR) to restore reasoning capabilities.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:153:This is consistent with diversity preservation enabling stronger training signals during GRPO, though the evidence is correlational: an alternative explanation---that CKA-only retains more functional structure, producing higher initial loss and naturally larger gradients---cannot be ruled out.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:261:65 MLP groups are pruned exclusively by CKA-only (retained by Standard), concentrated in L6--9 and L27---structures that gradient importance scores as important but CKA identifies as redundant with neighboring groups.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:262:Conversely, 46+ groups are pruned exclusively by Standard (retained by CKA-only), concentrated in L16--18, L22, and L25--26---structures that gradient importance scores as unimportant but CKA identifies as representationally unique.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:5:The dominant assumption is that the recovery paradigm---SFT versus RLVR---determines recovery quality: \\citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, significantly outperforming SFT.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:11:\\citet{rlsqueezes2026} show that RL and SFT impose fundamentally different demands on model representations---RL compresses incorrect paths while SFT expands correct ones---suggesting that pruning decisions should affect RL trainability.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:18:\\caption{Dose-response curve for the CKA diversity coefficient $\\alpha$ at 20\\% MLP channel sparsity on GSM8K ($N{=}1{,}319$). Recovery accuracy follows an inverted-U, peaking at $\\alpha{=}2.0$ (66.11\\%). SFT and GRPO curves nearly overlap ($|\\Delta| \\leq 1.14$\\,pp at every point), visually demonstrating reward-accuracy decoupling: the pruning criterion---not the recovery paradigm---determines outcome.}",
    "numLines": 35
  },
  "sourceToolAssistantUUID": "9580afe4-1ce5-4743-a58b-2691696f8b4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-23T04:05:56.257Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01QmEPTkf9dDK1Bh5eiaS7qq`</summary>

```json
{
  "pattern": "ing,|ing\\.|importantly|notably|it is worth noting|furthermore|moreover|additionally|delve|leverage|utilize|facilitate|a myriad|a plethora|paradigm shift",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99c6d09e-dc12-47be-b90c-134c8d06bc0e",
  "isSidechain": false,
  "requestId": "req_011CbJqen5pSSL3REKMkD7G2",
  "type": "assistant",
  "uuid": "bf72888c-d36d-4639-9005-38fda399f235",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197ke3DA8XhqbHj96FqgcoL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21179,
      "cache_read_input_tokens": 51429,
      "output_tokens": 1038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21179,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1038,
          "cache_read_input_tokens": 51429,
          "cache_creation_input_tokens": 21179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21179
          },
          "type": "message"
        }
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

_source line 61_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：recovery_aware_struct_prune Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 6 critical,…",
  "leafUuid": "fdc3984b-e9fd-4303-811c-29ff606bff8a",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Recovery-aware structured pruning paper audit",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303"
}
```

---

### Assistant

_source line 63 · 2026-05-23T04:08:33.580Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me analyze all the dimensions systematically. Let me also check for the backup tables and some additional patterns.

Let me also check a few more things - let me look at the tables that are mentioned in the backup directory and the MATH-500 and MBPP tables.

Let me now compile all my findings systematically.

## Audit Analysis

### 1. 叙事一致性

Let me trace through the story:

**Abstract's "problem"**: Fine-grained structured pruning is followed by recovery training. RLVR is considered superior, but this reflects suboptimal pruning, not fundamental RL property. 

When pruning preserves representational diversity, recovery method choice is irrelevant.

**Intro's "problem"**: Same - the dominant assumption that recovery paradigm (SFT vs RLVR) determines recovery quality. This is an artifact of suboptimal pruning. When pruning preserves representational diversity, method choice is irrelevant.

✅ Abstract problem == Intro problem

**Intro contributions**:
1. Reward-accuracy decoupling: mean |Δ(GRPO-SFT)| = 0.54pp across all fine-grained criteria and sparsity levels
2. RASP method with dose-response and recovery capacity spectrum

**Method**

:
I'm setting up a controlled comparison framework using four scoring criteria, implementing RASP scoring that combines importance weighting with representational overlap analysis, and designing a two-stage recovery pipeline with diagnostics to measure recovery capacity.

**Experiments verify**:
- Recovery capacity spectrum (Section 5.2)
- Reward-accuracy decoupling (Section 5.3)
- Dose-response analysis (Section 5.4)
- Cross-scale and cross-architecture (Section 5.5)

✅ Intro contributions align with Method and Experiments

**Conclusion summarizes**: 
- RLVR>SFT hierarchy reflects suboptimal pruning ✅
- When pruning preserves representational diversity, recovery method choice irrelevant ✅
- CKA-only enables active learning, importance-based collapse ✅
- Cross-scale and cross-architecture evidence ✅
- Representational diversity as predictor ✅

✅ Conclusion matches experiments

Now I'm checking the quantitative claims across the paper. The abstract mentions "peak reward 4.4×" but when I look at Table 1, the CKA-only peak is 0.354 versus Standard at 0.081, which gives 4.37× — that checks out. However, comparing CKA-only to RASP (0.354 vs 0.061) yields 5.8×, so the abstract's phrasing about importance-dominated pruning collapsing needs clarification on which baseline it's referencing. I'm trying to reconcile the numbers in the abstract and introduction. The abstract mentions "importance-dominated pruning (α=1.0) collapses while diversity-preserving criteria achieve active learning (peak reward 4.4×)" but I need to figure out what baseline that 4.4× refers to. The introduction explicitly states "peak reward 4.4× Standard," which would be CKA-only compared to the standard importance-only approach, but the abstract's mention of α=1.0 suggests it might be comparing against RASP instead, which would give 5.8×. Let me look more carefully at what the introduction actually says about the full spectrum of criteria to clarify which comparison is correct. as CKA vs α=1.0, which would be 5.8×. So the number is wrong if interpreting against α=1.0. If interpreting against Standard, it's 4.37× ≈ 4.4×.

The Conclusion also says "CKA-only pruning enables active learning (peak reward 4.4×)" — so there's an inconsistency in what the 4.4× refers to across different sections. The Abstract seems to compare diversity-preserving to importance-dominated (α=1.0), which should be 5.8×, but states 4.4× instead. This suggests the Abstract might be using the Standard baseline comparison rather than the α=1.0 comparison it describes.

Now I'm checking the max |Δ| claims between the Abstract and Intro sections to see if there are similar discrepancies in how the results are reported. At 15% sparsity, GRPO amplifies the CKA-guided advantage by 1.51 percentage points compared to SFT—the gap between CKA-only and Standard widens from 5.69 pp under SFT to 7.20 pp under GRPO.

The p<0.001 value technically applies to the overall GRPO gap rather than the differential itself, which is a subtle distinction in claim strength, though the framing is reasonable. Now I'm noticing there are quite a few em-dashes scattered throughout the LaTeX source file. I'm noticing several "-ing" constructions scattered throughout the document—"confirming that," "showing that," "indicating," "suggesting," "requiring"—that could signal AI writing, though some are acceptable in academic contexts. Now I'm reviewing the chapter structure: the abstract hits all four key points in about 180 words across seven sentences, and the introduction follows a solid five-paragraph arc covering background, the pruning-recovery assumption gap, and what prior work has missed.

The related work section is organized thematically rather than as a list of who-did-what, though some sentences pack multiple papers together in ways that border on enumeration. I'm checking whether each contribution aligns with its verification: the reward-accuracy decoupling claim is backed up in Section 5.3 with tables and cross-sparsity results, and I need to confirm that RASP plus dose-response findings are similarly grounded in the results. I need to verify the abstract's claim about maximum performance difference against the actual tables, particularly checking the MBPP results. The sparsity-dependent claim at 15% is problematic since the p-value indicates statistical significance for the overall gap, not specifically for how GRPO amplifies the advantage. On experimental rigor, I have good coverage with error bars across multiple seeds and standard baselines, but the ablations are limited—I've only tested the α parameter across five values, leaving other design choices like the per-layer floor threshold, SFT warmup duration, and calibration data size unexplored.

For reproducibility, the hardware and SFT timing are documented, but I'm missing GRPO training time and there's an inconsistency: the method section references a calibration set without specifying its size, while the experiments section mentions 512 examples but only in the appendix CKA stability discussion rather than the main text.

On terminology, $F(h)$ is defined as "functional overlap" that measures "representational redundancy"—both terms appear but with different emphasis. For RASP, it's consistently called "Recovery-Aware Structured Pruning," though there's some ambiguity about whether RASP specifically refers to the α=1.0 variant in experiments or the general parameterized formula in the method section.

The bigger issue is that RASP at α=1.0 is actually just one point on a spectrum where CKA-only represents α→∞ and Standard represents α=0, yet the paper lists them as separate methods in Table 1. This means when the paper claims "RASP collapses," it's specifically about the α=1.0 instantiation, not the broader RASP framework itself.

Now looking at the transitions between sections—there's no explicit bridge from Intro to Related Work or from Related Work to Method, though the flow from Method to Experiments feels natural. The Experiments section flows directly into Discussion and Conclusion without a jarring break. These implicit transitions are typical for ML papers.

For the Limitations section, I'm checking that it covers three substantive points: architectural and scale constraints, diagnostic limitations, and replication scope. The total length comes to roughly 150 words across three paragraphs, which aligns with the EMNLP guidelines.

Now I need to verify the page count against EMNLP 2026 requirements. The conference allows 8 pages for main text plus unlimited references, with limitations and ethics sections not counting toward that limit. So the core sections—abstract through conclusion—need to stay within 8 pages, while the full submission including appendix can reach 15 pages.

I also notice "v5" in the GRPO configuration description, which looks like an internal experiment label that should probably be removed or clarified to avoid appearing as residual internal information.

Now I'm checking for consistency across the reported numbers—the abstract mentions a max difference of 1.34 percentage points, but I'm seeing some variation in how these metrics are reported in different sections, particularly around the GSM8K results. Looking at the α parameter table, the maximum delta on GSM8K is 1.14 pp at α=2.0. For the main decoupling methods, RASP shows the largest effect at 0.61 pp, while the cross-sparsity results peak at 0.99 pp with the Standard method at 25% sparsity.

Now I'm checking the experiments section claim about "max 1.14 pp on GSM8K across all fine-grained criteria and sparsity levels" — the α table shows 1.14 at 20% sparsity, but I need to verify whether this maximum holds across all tested sparsity levels or if there are higher values at other sparsity points that I'm missing. I'm noticing a discrepancy between the reported means across benchmarks. Section 5.3 states the mean is 0.54 pp on GSM8K specifically, but the Introduction claims 0.54 pp across both GSM8K and MBPP combined—which doesn't add up if MBPP shows a mean around 1.25 pp. The cross-benchmark average should be higher than 0.54 pp, so either the Introduction is GSM8K-only or there's an inconsistency in how the metrics are being reported. I'm noticing the mean difference of 0.54 pp claimed across both benchmarks doesn't quite add up—if GSM8K alone is 0.54 and MBPP appears higher around 1.25, the combined mean should fall somewhere between them unless GSM8K has significantly more data points weighting the average down. Let me reconsider whether the 0.54 figure is actually computed across both benchmarks or if the phrasing in the introduction is ambiguous about what it's measuring.

The Discussion section merges with Conclusions and goes beyond just restating numbers—it interprets the hierarchy as reflecting suboptimal pruning choices rather than fundamental RL limitations, discusses representational diversity as a predictor, explains the sparsity dependence, and raises open questions about connections to the Lottery Ticket hypothesis. Though it does repeat some specific metrics like the 0.54 pp mean and peak reward improvements, the higher-level analysis adds substantive value.

Now checking the page count against EMNLP 2026's 8-page limit. The main text sections—abstract through conclusion—fit within that constraint at roughly 8 pages, with the appendix, references, and supplementary sections accounting for the remaining 7 pages in the 15-page compiled PDF. The breakdown looks reasonable.

I need to verify the 1.34 percentage point improvement claim on the MBPP benchmark and scan through the remaining tables for any placeholder text or incomplete entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdc3984b-e9fd-4303-811c-29ff606bff8a",
  "isSidechain": false,
  "requestId": "req_011CbJqfwokAQaue4LsNrBju",
  "type": "assistant",
  "uuid": "9f02f4c7-2993-48b7-b542-9befa6d4fad4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BoKcgFCn2u3C1LSq2Dcuv2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11363,
      "cache_read_input_tokens": 72608,
      "output_tokens": 7520,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11363,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7520,
          "cache_read_input_tokens": 72608,
          "cache_creation_input_tokens": 11363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11363
          },
          "type": "message"
        }
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

_source line 64 · 2026-05-23T04:08:33.581Z_

读取 MBPP 表和 MATH-500 表以验证数字一致性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f02f4c7-2993-48b7-b542-9befa6d4fad4",
  "isSidechain": false,
  "requestId": "req_011CbJqfwokAQaue4LsNrBju",
  "type": "assistant",
  "uuid": "3fc6fe81-fdc0-484a-85fc-0c62d6600b3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BoKcgFCn2u3C1LSq2Dcuv2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11363,
      "cache_read_input_tokens": 72608,
      "output_tokens": 7520,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11363,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7520,
          "cache_read_input_tokens": 72608,
          "cache_creation_input_tokens": 11363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11363
          },
          "type": "message"
        }
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

_source line 65 · 2026-05-23T04:08:34.540Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T6Vj74UADQLSmS4e7CbzwD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fc6fe81-fdc0-484a-85fc-0c62d6600b3b",
  "isSidechain": false,
  "requestId": "req_011CbJqfwokAQaue4LsNrBju",
  "type": "assistant",
  "uuid": "1c0d6dbc-f03d-45dc-845b-af68830c4a08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BoKcgFCn2u3C1LSq2Dcuv2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11363,
      "cache_read_input_tokens": 72608,
      "output_tokens": 7520,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11363,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7520,
          "cache_read_input_tokens": 72608,
          "cache_creation_input_tokens": 11363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11363
          },
          "type": "message"
        }
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

_source line 66 · 2026-05-23T04:08:38.173Z_

<details><summary>↩ Tool result · `toolu_01WZMkGueJPc7NLNPTXeTDoe`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:38:At this sparsity level, global importance ranking naturally concentrates pruning on MLP groups (attention GQA groups have uniformly higher importance), yielding \textbf{[TBD]} pruned MLP groups across 28 layers with all attention groups retained.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:46:Training is performed on the GSM8K training set with the following hyperparameters: learning rate \textbf{[TBD]}, $K{=}$\textbf{[TBD]} rollouts per prompt, KL coefficient $\beta{=}$\textbf{[TBD]}, batch size \textbf{[TBD]}, trained for \textbf{[TBD]} steps on 2$\times$ NVIDIA RTX PRO 6000 (96GB each).
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:23:The same structural property receives opposite treatment depending on whether one optimizes for immediate accuracy or post-recovery performance.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:35:    \item We conduct the most comprehensive study to date % TODO: 待实验完成后复核覆盖度是否支撑此 claim
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:37:    \item We systematically investigate whether the optimal pruning strategy changes depending on the recovery paradigm (RLVR vs.\ SFT), testing the hypothesis that functional redundancy predicts RLVR recoverability but not SFT recoverability.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex:4:\caption{MATH-500 out-of-distribution evaluation ($N{=}500$, greedy decoding, \texttt{max\_new\_tokens=2048}). The method ordering (CKA-only $>$ Standard $>$ Random) is preserved from GSM8K, confirming cross-benchmark consistency. $^\star$GRPO evaluation pending. Best SFT in \textbf{bold}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex:28:\multicolumn{4}{p{0.85\columnwidth}}{\footnotesize $^\dagger$Over half of Dense responses truncated at 2048 tokens (73.6\% at 4096); all pruned models evaluated under the same constraint. $^\ddagger$Evaluated with earlier answer extraction script; re-evaluation pending. $^\star$Pending; will be filled upon completion.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table2_recovery.tex:11:CKA-only 20\% & \underline{63.91} & TBD & --- & \underline{0.354} \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a6cf2f5-ffde-4b77-a7ea-d4785f449039",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "815fa6a3-583d-4d83-9cea-8d3b1e7bc8c3",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:38:At this sparsity level, global importance ranking naturally concentrates pruning on MLP groups (attention GQA groups have uniformly higher importance), yielding \\textbf{[TBD]} pruned MLP groups across 28 layers with all attention groups retained.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:46:Training is performed on the GSM8K training set with the following hyperparameters: learning rate \\textbf{[TBD]}, $K{=}$\\textbf{[TBD]} rollouts per prompt, KL coefficient $\\beta{=}$\\textbf{[TBD]}, batch size \\textbf{[TBD]}, trained for \\textbf{[TBD]} steps on 2$\\times$ NVIDIA RTX PRO 6000 (96GB each).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:23:The same structural property receives opposite treatment depending on whether one optimizes for immediate accuracy or post-recovery performance.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:35:    \\item We conduct the most comprehensive study to date % TODO: 待实验完成后复核覆盖度是否支撑此 claim\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:37:    \\item We systematically investigate whether the optimal pruning strategy changes depending on the recovery paradigm (RLVR vs.\\ SFT), testing the hypothesis that functional redundancy predicts RLVR recoverability but not SFT recoverability.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex:4:\\caption{MATH-500 out-of-distribution evaluation ($N{=}500$, greedy decoding, \\texttt{max\\_new\\_tokens=2048}). The method ordering (CKA-only $>$ Standard $>$ Random) is preserved from GSM8K, confirming cross-benchmark consistency. $^\\star$GRPO evaluation pending. Best SFT in \\textbf{bold}.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex:28:\\multicolumn{4}{p{0.85\\columnwidth}}{\\footnotesize $^\\dagger$Over half of Dense responses truncated at 2048 tokens (73.6\\% at 4096); all pruned models evaluated under the same constraint. $^\\ddagger$Evaluated with earlier answer extraction script; re-evaluation pending. $^\\star$Pending; will be filled upon completion.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table2_recovery.tex:11:CKA-only 20\\% & \\underline{63.91} & TBD & --- & \\underline{0.354} \\\\",
    "numLines": 8
  },
  "sourceToolAssistantUUID": "9a6cf2f5-ffde-4b77-a7ea-d4785f449039",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-23T04:08:34.551Z_

<details><summary>↩ Tool result · `toolu_01T6Vj74UADQLSmS4e7CbzwD`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\small
4	\caption{MBPP code generation accuracy ($N{=}374$, greedy decoding). All fine-grained pruning methods converge near a capability floor (${\sim}$75\% code capability loss vs Dense), limiting differentiation (${\sim}$1\,pp range, within stderr). ShortGPT shows a larger GRPO delta ($+$4.01\,pp) but at the 95\% CI boundary (stderr ${\approx}$1.55\,pp).}
5	\label{tab:mbpp}
6	\begin{tabular}{@{}lccc@{}}
7	\toprule
8	Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	Dense & -- & 53.48 & -- \\
11	\midrule
12	CKA-only 20\% & 12.83 & 14.17 & $+$1.34 \\
13	Standard 20\% & 12.03 & 13.10 & $+$1.07 \\
14	\rasp{} 20\% & 11.76 & 13.10 & $+$1.34 \\
15	\midrule
16	ShortGPT 20\%$^\dagger$ & 10.43 & 14.44 & $+$4.01 \\
17	\bottomrule
18	\multicolumn{4}{l}{\footnotesize $^\dagger$Depth pruning; removes entire layers.}
19	\end{tabular}
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c0d6dbc-f03d-45dc-845b-af68830c4a08",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "87dfc3c2-3c26-4c9c-8ac7-fe9dc82230f4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{MBPP code generation accuracy ($N{=}374$, greedy decoding). All fine-grained pruning methods converge near a capability floor (${\\sim}$75\\% code capability loss vs Dense), limiting differentiation (${\\sim}$1\\,pp range, within stderr). ShortGPT shows a larger GRPO delta ($+$4.01\\,pp) but at the 95\\% CI boundary (stderr ${\\approx}$1.55\\,pp).}\n\\label{tab:mbpp}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & SFT\\,(\\%) & GRPO\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\nDense & -- & 53.48 & -- \\\\\n\\midrule\nCKA-only 20\\% & 12.83 & 14.17 & $+$1.34 \\\\\nStandard 20\\% & 12.03 & 13.10 & $+$1.07 \\\\\n\\rasp{} 20\\% & 11.76 & 13.10 & $+$1.34 \\\\\n\\midrule\nShortGPT 20\\%$^\\dagger$ & 10.43 & 14.44 & $+$4.01 \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$Depth pruning; removes entire layers.}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  },
  "sourceToolAssistantUUID": "1c0d6dbc-f03d-45dc-845b-af68830c4a08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-23T04:08:35.553Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W9iNhE1Y5uhRCdN6AGmsEr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87dfc3c2-3c26-4c9c-8ac7-fe9dc82230f4",
  "isSidechain": false,
  "requestId": "req_011CbJqfwokAQaue4LsNrBju",
  "type": "assistant",
  "uuid": "f4333cdf-7abc-4f8a-a7c4-261dea18aaf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BoKcgFCn2u3C1LSq2Dcuv2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11363,
      "cache_read_input_tokens": 72608,
      "output_tokens": 7520,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11363,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7520,
          "cache_read_input_tokens": 72608,
          "cache_creation_input_tokens": 11363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11363
          },
          "type": "message"
        }
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

_source line 69 · 2026-05-23T04:08:35.558Z_

<details><summary>↩ Tool result · `toolu_01W9iNhE1Y5uhRCdN6AGmsEr`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\small
4	\caption{MATH-500 out-of-distribution evaluation ($N{=}500$, greedy decoding, \texttt{max\_new\_tokens=2048}). The method ordering (CKA-only $>$ Standard $>$ Random) is preserved from GSM8K, confirming cross-benchmark consistency. $^\star$GRPO evaluation pending. Best SFT in \textbf{bold}.}
5	\label{tab:math500}
6	\begin{tabular}{@{}lccc@{}}
7	\toprule
8	Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	Dense & \multicolumn{3}{c}{53.0\,$^\dagger$} \\
11	\midrule
12	\multicolumn{4}{l}{\textit{20\% sparsity --- method comparison}} \\
13	CKA-only & \textbf{26.8} & 29.2$^\ddagger$ & $+$2.4 \\
14	Standard & 25.8$^\ddagger$ & 26.4$^\ddagger$ & $+$0.6 \\
15	\rasp{} ($\alpha{=}1.0$) & 21.2 & --$^\star$ & -- \\
16	Random & 14.4 & --$^\star$ & -- \\
17	\midrule
18	\multicolumn{4}{l}{\textit{20\% sparsity --- $\alpha$ dose-response}} \\
19	$\alpha{=}0.5$ & 25.4 & --$^\star$ & -- \\
20	$\alpha{=}2.0$ & 24.0 & --$^\star$ & -- \\
21	$\alpha{=}3.0$ & 23.2 & --$^\star$ & -- \\
22	$\alpha{=}4.0$ & 26.6 & --$^\star$ & -- \\
23	\midrule
24	\multicolumn{4}{l}{\textit{25\% sparsity}} \\
25	CKA-only & 19.2 & 18.4 & $-$0.8 \\
26	Standard & 14.0 & 12.8 & $-$1.2 \\
27	\bottomrule
28	\multicolumn{4}{p{0.85\columnwidth}}{\footnotesize $^\dagger$Over half of Dense responses truncated at 2048 tokens (73.6\% at 4096); all pruned models evaluated under the same constraint. $^\ddagger$Evaluated with earlier answer extraction script; re-evaluation pending. $^\star$Pending; will be filled upon completion.}
29	\end{tabular}
30	\end{table}
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4333cdf-7abc-4f8a-a7c4-261dea18aaf9",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "235d1f7d-fef2-48de-be86-61b285a7b0f7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{MATH-500 out-of-distribution evaluation ($N{=}500$, greedy decoding, \\texttt{max\\_new\\_tokens=2048}). The method ordering (CKA-only $>$ Standard $>$ Random) is preserved from GSM8K, confirming cross-benchmark consistency. $^\\star$GRPO evaluation pending. Best SFT in \\textbf{bold}.}\n\\label{tab:math500}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & SFT\\,(\\%) & GRPO\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\nDense & \\multicolumn{3}{c}{53.0\\,$^\\dagger$} \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{20\\% sparsity --- method comparison}} \\\\\nCKA-only & \\textbf{26.8} & 29.2$^\\ddagger$ & $+$2.4 \\\\\nStandard & 25.8$^\\ddagger$ & 26.4$^\\ddagger$ & $+$0.6 \\\\\n\\rasp{} ($\\alpha{=}1.0$) & 21.2 & --$^\\star$ & -- \\\\\nRandom & 14.4 & --$^\\star$ & -- \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{20\\% sparsity --- $\\alpha$ dose-response}} \\\\\n$\\alpha{=}0.5$ & 25.4 & --$^\\star$ & -- \\\\\n$\\alpha{=}2.0$ & 24.0 & --$^\\star$ & -- \\\\\n$\\alpha{=}3.0$ & 23.2 & --$^\\star$ & -- \\\\\n$\\alpha{=}4.0$ & 26.6 & --$^\\star$ & -- \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{25\\% sparsity}} \\\\\nCKA-only & 19.2 & 18.4 & $-$0.8 \\\\\nStandard & 14.0 & 12.8 & $-$1.2 \\\\\n\\bottomrule\n\\multicolumn{4}{p{0.85\\columnwidth}}{\\footnotesize $^\\dagger$Over half of Dense responses truncated at 2048 tokens (73.6\\% at 4096); all pruned models evaluated under the same constraint. $^\\ddagger$Evaluated with earlier answer extraction script; re-evaluation pending. $^\\star$Pending; will be filled upon completion.}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  },
  "sourceToolAssistantUUID": "f4333cdf-7abc-4f8a-a7c4-261dea18aaf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-23T04:08:37.076Z_

<details open><summary>🔧 Tool call — Read · `toolu_016YeEN5AH2BgzrYFDjaetu9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table2_recovery.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "235d1f7d-fef2-48de-be86-61b285a7b0f7",
  "isSidechain": false,
  "requestId": "req_011CbJqfwokAQaue4LsNrBju",
  "type": "assistant",
  "uuid": "8c345448-7c53-40e4-ab54-1131d85f68e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BoKcgFCn2u3C1LSq2Dcuv2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11363,
      "cache_read_input_tokens": 72608,
      "output_tokens": 7520,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11363,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7520,
          "cache_read_input_tokens": 72608,
          "cache_creation_input_tokens": 11363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11363
          },
          "type": "message"
        }
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

_source line 71 · 2026-05-23T04:08:37.080Z_

<details><summary>↩ Tool result · `toolu_016YeEN5AH2BgzrYFDjaetu9`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Reward-accuracy decoupling on GSM8K ($N{=}1{,}319$, greedy decoding). SFT Acc: accuracy after SFT warmup. GRPO Acc: accuracy at the last stable checkpoint (step 100 for Unpruned, step 50 for Standard, step 5 for \rasp{}). $\Delta$: change from SFT to GRPO accuracy.}
5	\label{tab:decoupling}
6	\begin{tabular}{lcccc}
7	\toprule
8	Model & SFT Acc (\%) & GRPO Acc (\%) & $\Delta$ (pp) & Peak Reward \\
9	\midrule
10	Unpruned & \textbf{81.27} & \textbf{81.27} & $\phantom{-}$0.00 & \textbf{0.669} \\
11	CKA-only 20\% & \underline{63.91} & TBD & --- & \underline{0.354} \\
12	Standard 20\% & 59.29 & 58.91 & $-$0.38 & 0.081 \\
13	\rasp{} 20\% & 61.49 & 60.65 & $-$0.84 & 0.061 \\
14	\bottomrule
15	\end{tabular}
16	\end{table}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c345448-7c53-40e4-ab54-1131d85f68e2",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "858753db-073a-4a12-a941-26c89fe34ba7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table2_recovery.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Reward-accuracy decoupling on GSM8K ($N{=}1{,}319$, greedy decoding). SFT Acc: accuracy after SFT warmup. GRPO Acc: accuracy at the last stable checkpoint (step 100 for Unpruned, step 50 for Standard, step 5 for \\rasp{}). $\\Delta$: change from SFT to GRPO accuracy.}\n\\label{tab:decoupling}\n\\begin{tabular}{lcccc}\n\\toprule\nModel & SFT Acc (\\%) & GRPO Acc (\\%) & $\\Delta$ (pp) & Peak Reward \\\\\n\\midrule\nUnpruned & \\textbf{81.27} & \\textbf{81.27} & $\\phantom{-}$0.00 & \\textbf{0.669} \\\\\nCKA-only 20\\% & \\underline{63.91} & TBD & --- & \\underline{0.354} \\\\\nStandard 20\\% & 59.29 & 58.91 & $-$0.38 & 0.081 \\\\\n\\rasp{} 20\\% & 61.49 & 60.65 & $-$0.84 & 0.061 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  },
  "sourceToolAssistantUUID": "8c345448-7c53-40e4-ab54-1131d85f68e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-23T04:08:38.157Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WZMkGueJPc7NLNPTXeTDoe`</summary>

```json
{
  "pattern": "TBD|PLACEHOLDER|TODO|\\[If |XX\\.XX|pending",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "858753db-073a-4a12-a941-26c89fe34ba7",
  "isSidechain": false,
  "requestId": "req_011CbJqfwokAQaue4LsNrBju",
  "type": "assistant",
  "uuid": "9a6cf2f5-ffde-4b77-a7ea-d4785f449039",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BoKcgFCn2u3C1LSq2Dcuv2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11363,
      "cache_read_input_tokens": 72608,
      "output_tokens": 7520,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11363,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7520,
          "cache_read_input_tokens": 72608,
          "cache_creation_input_tokens": 11363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11363
          },
          "type": "message"
        }
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

_source line 73 · 2026-05-23T04:08:38.241Z_

```json
{
  "parentUuid": "815fa6a3-583d-4d83-9cea-8d3b1e7bc8c3",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a2852cf2-aa36-44e7-8f8b-c3f7c5b34c51",
  "timestamp": "2026-05-23T04:08:38.241Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 74_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：recovery_aware_struct_prune Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 6 critical,…",
  "leafUuid": "a2852cf2-aa36-44e7-8f8b-c3f7c5b34c51",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303"
}
```

---

### Runtime record

_source line 75_

```json
{
  "type": "ai-title",
  "aiTitle": "Recovery-aware structured pruning paper audit",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303"
}
```

---

### Assistant

_source line 76 · 2026-05-23T04:10:41.068Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to compile the full audit. Let me also check for the "v5" and "v2" internal labels more carefully.

Key findings so far:

### CRITICAL findings:

1. **MATH-500 table has "pending" / "--*" entries** - many GRPO values marked as pending. This means incomplete data is being presented. While the text says "SFT--GRPO differences remain within statistical noise" for MATH-500, the actual table has most GRPO values missing. This weakens the decoupling claim on MATH-500.


2. **Backup files contain stale data with TBD placeholders** - the recovery version shows outdated entries like "CKA-only 20% → TBD", indicating the working files haven't been fully synchronized.
3. **Em-dashes appear extensively throughout the main text** - at least 13 instances across the document, which is a notable stylistic pattern.
4. **The Abstract has an incomplete statement about pruning methods** - it mentions "importance-dominated pruning ($\alpha{=}1.0$) collapses while diversity-preserving criteria achieve active learning" but the sentence cuts off before explaining the peak reward comparison.

Now looking at the denominator issue more carefully - the 4.4× figure could be interpreted two different ways depending on what's being compared. If it's CKA-only against Standard, that's 0.354/0.081 = 4.37×, but if it's being compared to RASP with α=1.0, the ratio would be 0.354/0.061 = 5.8×, which creates ambiguity about which baseline is intended.

There's also an inconsistency with the mean delta values - the Intro claims "mean |Δ(GRPO-SFT)| = 0.54 pp across all benchmarks on GSM8K and MBPP" but this 0.54 figure appears to only apply to GSM8K specifically, while MBPP shows consistently larger deltas around 1.25 pp.

The MATH-500 table contains multiple pending entries that shouldn't be in a final submission, and there are internal version labels like "v5 GRPO configuration" and "v2 benchmark" scattered throughout that need to be removed. The max delta claim of 1.34 pp checks out against the MBPP table, though I need to verify what the experiments section actually states about this. I notice the paper claims HumanEval as one of the benchmarks tested, but I can't find any actual table or data for it—only references in the text saying the decoupling holds across HumanEval and MBPP. This looks like missing evidence to support that claim.

Now I'm checking the Conclusion's statement about mean |Δ| = 0.54 pp across all fine-grained conditions. Let me verify this by tallying up the actual values from GSM8K and MBPP—counting the deltas at different percentages and alpha values to see if they actually average to 0.54 pp. I'm verifying that the 0.54 mean refers specifically to the four main methods at 20% sparsity, which checks out mathematically. But the paper's claim about "all fine-grained criteria and sparsity levels" is ambiguous—it's unclear whether that includes the dose-response α variants or just the different sparsity percentages across the core methods. The mean of 0.54 appears to be specifically for the four methods at 20% sparsity on GSM8K, but it's being presented as if it covers all fine-grained criteria and sparsity levels across both GSM8K and MBPP, which would actually produce a different average. The larger deltas at 15% sparsity (CKA-only at +0.58, Standard at -0.93) suggest the characterization of this mean is overstated in scope.

When I look at the MBPP data separately, the deltas are substantially larger—CKA, Standard, and RASP all exceed 1 pp—which makes it impossible for a cross-benchmark mean including MBPP to equal 0.54. The GSM8K mean at 20% is 0.54, but the MBPP mean for the same three methods is 1.25, so claiming "mean 0.54 pp across GSM8K and MBPP" in the abstract is mathematically inconsistent with the actual data.

Let me reread the Abstract and Intro statements more carefully to see exactly what's being claimed. The Abstract only mentions the max value of 1.34 pp, which is fine. But the Intro's first contribution explicitly states "mean 0.54 pp" across both benchmarks, and that's where the discrepancy lies.

Looking at Section 5.3, it clarifies that 0.54 pp is the mean for GSM8K alone. Then the Conclusion repeats the cross-benchmark claim of mean 0.54 pp, which appears to be incorrectly applying the GSM8K-only figure to both benchmarks combined. This is a significant numerical inconsistency between what the Intro and Conclusion claim versus what the actual data shows.

There's also a naming issue with RASP itself—in the Method section it's presented as a general framework parameterized by α, but in Experiments, RASP specifically refers to α=1.0, while the optimal performance occurs at α=2.0. This creates confusion because the paper's proposed method underperforms at its default setting. The deeper issue is that RASP seems positioned as a controlled comparison framework rather than a practical method, yet the Abstract frames it as a proposed contribution, creating tension between what the paper actually contributes versus how it's presented. The issue is that RASP(α=2.0) only appears in the appendix ablation with a single seed at 20% sparsity, making it not directly comparable to CKA-only's more rigorous evaluation across three seeds. The main tables present CKA-only as the winner, but the paper's conclusion hinges on RASP(α=2.0) being superior—a result relegated to supplementary material without the same statistical rigor. This creates a disconnect between the primary evidence and the narrative conclusion, though it's more of a presentation choice than a fundamental flaw.

Looking at the critical issues more carefully: the mean improvement of 0.54 percentage points is claimed across both GSM8K and MBPP in the introduction and conclusion, but it's actually only from GSM8K—MBPP shows roughly 1.25 pp improvement. The MATH-500 table has seven incomplete GRPO entries marked as pending, and there are internal version labels scattered through the LaTeX files suggesting the paper may not be fully finalized. Most concerning is that HumanEval results are mentioned in the text as supporting the decoupling hypothesis, but no actual table or data for HumanEval is provided anywhere.

I'm also noticing that table2_recovery.tex exists in the directory but isn't actually referenced in the main document—the experiments section only pulls in tab1_recovery_gradient and tab2_decoupling, so the recovery table appears to be a stale backup file that can be ignored.

Now I'm flagging several issues that need attention: em-dashes appear throughout the non-backup files in over a dozen places, which is a strong indicator of AI-generated content. The abstract has a 4.4× comparison where the denominator is ambiguous—it's unclear whether it's comparing against Standard or RASP. There's also naming confusion around RASP since RASP(α=1.0) collapses in the main experiments but RASP(α=2.0) performs best in the appendix. The conclusion repeats specific numbers like μ=0.62 and μ≥0.88 instead of just referencing Figure 4. On the positive side, the limitations section is appropriately sized for EMNLP 2026 guidelines, there's no duplicate limitations section in the appendix, and while HumanEval is mentioned, the actual data appears to be missing.

I'm also catching internal version labels leaking into the paper—"v5" appears in Table 2's caption describing the GRPO configuration, and "v2" shows up in the appendix's inference table caption. Reviewers will flag these as internal terminology. I'm also double-checking the MBPP results to see if Random has any entries, and from what I can see in that table, it only shows CKA-only, Standard, RASP, and ShortGPT. The text claims that decoupling holds across both HumanEval and MBPP with all fine-grained GRPO deltas under 2 percentage points, but it only references an appendix for MBPP results—there's no corresponding HumanEval table or appendix section to back up that claim. I've checked through all the table files and can't find a HumanEval results table anywhere, which means this is a significant assertion without supporting evidence. Looking at GRPO implementations, `reward_desert_patience` doesn't appear to be a standard parameter name—it's likely custom to their framework—and leaving it undefined in the paper creates a readability problem. Now examining Contribution 1 more closely: the "+1.51 pp differential" represents the difference between GRPO's advantage over SFT with CKA guidance (7.20 pp) and SFT's advantage without it (5.69 pp), with the p-value coming from a Welch's t-test comparing the CKA-only condition.

The issue is that this p-value tests whether the GRPO gap itself is significant, not whether the 1.51 differential is statistically significant. Pairing the p-value with the differential misleadingly suggests the differential has statistical support when really only the overall gap does. I should compile my findings now, though I want to double-check the MATH-500 claim about differences staying within statistical noise.

Looking at the MATH-500 results across conditions, the maximum absolute difference is 2.4 percentage points in the CKA-only setup, which technically satisfies the stated threshold of less than 2.5 pp, but that threshold feels suspiciously tailored to just barely contain the actual maximum. More concerning is that the 2.4 pp GRPO improvement on MATH-500 CKA-only is actually larger than improvements seen on other benchmarks.

I'm also noticing that several MATH-500 GRPO values are marked with a dagger symbol indicating they were evaluated with an earlier answer extraction script that's pending re-evaluation, so these numbers haven't been fully validated yet. This undermines the reliability of the comparisons.

Now I'm going through the paper systematically to count em-dashes in the non-backup files and compile a complete audit of the findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2852cf2-aa36-44e7-8f8b-c3f7c5b34c51",
  "isSidechain": false,
  "requestId": "req_011CbJqssJhwFEQcEds9tFQn",
  "type": "assistant",
  "uuid": "1816a5ef-9d90-484f-b013-1bd111c47db7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAAJF9erhHAZRrzBHVJWXw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10174,
      "cache_read_input_tokens": 83971,
      "output_tokens": 6301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10174,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6301,
          "cache_read_input_tokens": 83971,
          "cache_creation_input_tokens": 10174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10174
          },
          "type": "message"
        }
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

_source line 77 · 2026-05-23T04:10:41.171Z_

现在检查 HumanEval 是否有数据支撑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1816a5ef-9d90-484f-b013-1bd111c47db7",
  "isSidechain": false,
  "requestId": "req_011CbJqssJhwFEQcEds9tFQn",
  "type": "assistant",
  "uuid": "f3ab2f08-ab84-4c06-92bb-fedd12dfb0c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAAJF9erhHAZRrzBHVJWXw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10174,
      "cache_read_input_tokens": 83971,
      "output_tokens": 6301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10174,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6301,
          "cache_read_input_tokens": 83971,
          "cache_creation_input_tokens": 10174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10174
          },
          "type": "message"
        }
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

_source line 78 · 2026-05-23T04:10:45.814Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017RgfXD6NbtTHwHBKSSEXAA`</summary>

```json
{
  "pattern": "HumanEval",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3ab2f08-ab84-4c06-92bb-fedd12dfb0c7",
  "isSidechain": false,
  "requestId": "req_011CbJqssJhwFEQcEds9tFQn",
  "type": "assistant",
  "uuid": "203f6e78-f59e-4e31-a5c7-8a89ac3ca35b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAAJF9erhHAZRrzBHVJWXw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10174,
      "cache_read_input_tokens": 83971,
      "output_tokens": 6301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10174,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6301,
          "cache_read_input_tokens": 83971,
          "cache_creation_input_tokens": 10174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10174
          },
          "type": "message"
        }
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

_source line 79 · 2026-05-23T04:10:46.829Z_

<details><summary>↩ Tool result · `toolu_01YTfSfJCWxU97pvbDNUjUY5`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07775fed-7b6f-4a31-95c8-5103d65efc03",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "8ab0c90c-9237-4487-a1dd-a44136040eac",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "07775fed-7b6f-4a31-95c8-5103d65efc03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-23T04:10:45.835Z_

<details><summary>↩ Tool result · `toolu_017RgfXD6NbtTHwHBKSSEXAA`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:85:The pruning-criterion ranking transfers to MATH-500~\citep{hendrycks2021math} (SFT: CKA-only 26.8\% vs Standard 25.8\% vs \rasp{} 21.2\% vs Random 14.4\%; Appendix~\ref{sec:appendix_math500}), and decoupling holds across HumanEval~\citep{chen2021humaneval} and MBPP~\citep{austin2021mbpp} (all fine-grained GRPO $|\Delta| < 2$\,pp; MBPP deltas are uniformly slightly positive but within stderr; Appendix~\ref{sec:appendix_mbpp}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:16:\textbf{[Phase 2: We extend evaluation to MMLU~\citep{hendrycks2021mmlu} for broad knowledge, HumanEval~\citep{chen2021humaneval} for code generation, and LongBench~\citep{bai2024longbench} for long-context understanding.]}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:69:\textbf{[Phase 2: We additionally report perplexity on WikiText-2 and per-benchmark accuracy on MMLU, HumanEval, and LongBench.]}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex:15:We evaluate on four benchmarks (GSM8K, MATH-500, HumanEval, MBPP) covering math reasoning and code generation; logical, commonsense, and multi-modal reasoning are not addressed.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/ethics.tex:1:This work uses publicly available models (DeepSeek-R1-Distill-Qwen, Qwen2.5-Math) and established benchmarks (GSM8K, MATH-500, HumanEval, MBPP); no private data or human subjects are involved.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "203f6e78-f59e-4e31-a5c7-8a89ac3ca35b",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "8ce07c6f-d594-4787-83df-22dd960b83d9",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:85:The pruning-criterion ranking transfers to MATH-500~\\citep{hendrycks2021math} (SFT: CKA-only 26.8\\% vs Standard 25.8\\% vs \\rasp{} 21.2\\% vs Random 14.4\\%; Appendix~\\ref{sec:appendix_math500}), and decoupling holds across HumanEval~\\citep{chen2021humaneval} and MBPP~\\citep{austin2021mbpp} (all fine-grained GRPO $|\\Delta| < 2$\\,pp; MBPP deltas are uniformly slightly positive but within stderr; Appendix~\\ref{sec:appendix_mbpp}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:16:\\textbf{[Phase 2: We extend evaluation to MMLU~\\citep{hendrycks2021mmlu} for broad knowledge, HumanEval~\\citep{chen2021humaneval} for code generation, and LongBench~\\citep{bai2024longbench} for long-context understanding.]}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:69:\\textbf{[Phase 2: We additionally report perplexity on WikiText-2 and per-benchmark accuracy on MMLU, HumanEval, and LongBench.]}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex:15:We evaluate on four benchmarks (GSM8K, MATH-500, HumanEval, MBPP) covering math reasoning and code generation; logical, commonsense, and multi-modal reasoning are not addressed.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/ethics.tex:1:This work uses publicly available models (DeepSeek-R1-Distill-Qwen, Qwen2.5-Math) and established benchmarks (GSM8K, MATH-500, HumanEval, MBPP); no private data or human subjects are involved.",
    "numLines": 5
  },
  "sourceToolAssistantUUID": "203f6e78-f59e-4e31-a5c7-8a89ac3ca35b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-23T04:10:46.324Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WDJoEL31Lcf4yXgVhVTkN4`</summary>

```json
{
  "pattern": "v5|v2 benchmark",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ce07c6f-d594-4787-83df-22dd960b83d9",
  "isSidechain": false,
  "requestId": "req_011CbJqssJhwFEQcEds9tFQn",
  "type": "assistant",
  "uuid": "bccb276b-af5a-42a2-a696-b96ee7f2d028",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAAJF9erhHAZRrzBHVJWXw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10174,
      "cache_read_input_tokens": 83971,
      "output_tokens": 6301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10174,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6301,
          "cache_read_input_tokens": 83971,
          "cache_creation_input_tokens": 10174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10174
          },
          "type": "message"
        }
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

_source line 82 · 2026-05-23T04:10:46.341Z_

<details><summary>↩ Tool result · `toolu_01WDJoEL31Lcf4yXgVhVTkN4`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table1_postprune.tex:4:\caption{Recovery capacity gradient under identical GRPO v5 configuration (20\% sparsity, $N{=}1{,}319$). Best Reward: peak mean reward over 100 GRPO steps. Final Reward: reward at step 100. Best \texttt{frac\_zero\_std}: lowest fraction of training batches with zero reward variance (lower is better, indicates more diverse learning signal).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex:4:\caption{GRPO responsiveness on GSM8K ($N{=}1{,}319$, greedy decoding). All pruned models use the controlled v5 GRPO configuration (identical hyperparameters including \texttt{reward\_desert\_patience}{$=$}50), evaluated at step 100. CKA-only, Standard, and Random report mean $\pm$ std over 3 GRPO seeds; \rasp{} uses a single seed. Best in \textbf{bold}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:67:\caption{Inference characteristics at 20\% sparsity (clean v2 benchmark, single-GPU, no contention). Pruning reduces parameters by 19\% and memory by ${\sim}$28\%, with TTFT improving 18\%. Per-token throughput decreases 19\% (0.81$\times$) due to non-uniform layer widths from full-layer removal that current GPU kernels do not optimize.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bccb276b-af5a-42a2-a696-b96ee7f2d028",
  "isSidechain": false,
  "promptId": "1c39c544-3c14-41e5-a835-3527587847c0",
  "type": "user",
  "uuid": "c6c2d56a-1f51-4f9f-b150-42788d7c7424",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table1_postprune.tex:4:\\caption{Recovery capacity gradient under identical GRPO v5 configuration (20\\% sparsity, $N{=}1{,}319$). Best Reward: peak mean reward over 100 GRPO steps. Final Reward: reward at step 100. Best \\texttt{frac\\_zero\\_std}: lowest fraction of training batches with zero reward variance (lower is better, indicates more diverse learning signal).}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex:4:\\caption{GRPO responsiveness on GSM8K ($N{=}1{,}319$, greedy decoding). All pruned models use the controlled v5 GRPO configuration (identical hyperparameters including \\texttt{reward\\_desert\\_patience}{$=$}50), evaluated at step 100. CKA-only, Standard, and Random report mean $\\pm$ std over 3 GRPO seeds; \\rasp{} uses a single seed. Best in \\textbf{bold}.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:67:\\caption{Inference characteristics at 20\\% sparsity (clean v2 benchmark, single-GPU, no contention). Pruning reduces parameters by 19\\% and memory by ${\\sim}$28\\%, with TTFT improving 18\\%. Per-token throughput decreases 19\\% (0.81$\\times$) due to non-uniform layer widths from full-layer removal that current GPU kernels do not optimize.}",
    "numLines": 3
  },
  "sourceToolAssistantUUID": "bccb276b-af5a-42a2-a696-b96ee7f2d028",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-23T04:10:46.813Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01YTfSfJCWxU97pvbDNUjUY5`</summary>

```json
{
  "pattern": "reward_desert_patience",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6c2d56a-1f51-4f9f-b150-42788d7c7424",
  "isSidechain": false,
  "requestId": "req_011CbJqssJhwFEQcEds9tFQn",
  "type": "assistant",
  "uuid": "07775fed-7b6f-4a31-95c8-5103d65efc03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAAJF9erhHAZRrzBHVJWXw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10174,
      "cache_read_input_tokens": 83971,
      "output_tokens": 6301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10174,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6301,
          "cache_read_input_tokens": 83971,
          "cache_creation_input_tokens": 10174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10174
          },
          "type": "message"
        }
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

_source line 84_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：recovery_aware_struct_prune Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 6 critical,…",
  "leafUuid": "8ab0c90c-9237-4487-a1dd-a44136040eac",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303"
}
```

---

### Runtime record

_source line 85_

```json
{
  "type": "ai-title",
  "aiTitle": "Recovery-aware structured pruning paper audit",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303"
}
```

---

### Assistant

_source line 86 · 2026-05-23T04:11:34.708Z_

<details><summary>Logged reasoning block</summary>

```text
Wait, `reward_desert_patience` is not found in the text? Let me check - the grep found no match. But I saw it in the tab2_decoupling.tex. Let me re-check.

Actually, the grep didn't match because it's looking for the literal string "reward_desert_patience" but in the tex file it's `\texttt{reward\_desert\_patience}` with escaped underscores. The grep should look for "reward.*desert.*patience" or just "desert".

Let me also note: `table1_postprune.tex` has "GRPO v5 configuration" - another internal label. 

So table1_postprune.tex is a stale backup that's not even included in the current experiments.tex. Looking at the version labels, "v5" shows up in the active tab2_decoupling.tex and the stale table1_postprune.tex, while "v2" appears in the active appendix.tex.

I also need to check on `\texttt{reward_desert_patience}` — it's in the active tab2_decoupling.tex table, and it's mentioned in experiments.tex line 28 as a hyperparameter set to 50, but there's no explanation of what it actually does. This parameter name looks internal and either needs a definition or should be removed entirely.

Let me now compile all the critical findings from this audit.

The first major issue is a narrative inconsistency: the intro and conclusion both claim "mean |Δ(GRPO-SFT)| = 0.54 pp across GSM8K and MBPP," but 0.54 is actually just the GSM8K average from Section 5.3. The MBPP results show a much higher mean difference around 1.25 pp when I look at the individual method deltas, so the cross-benchmark average should be significantly higher than 0.54.

The second critical finding involves the HumanEval contribution claim — it's stated in the experiments section but there's no actual data supporting it.

I'm also noticing some serious issues with incomplete and internal-only content: the MATH-500 table has multiple entries marked as "pending" with a note that they'll be filled upon completion, which shouldn't appear in a submitted paper. Additionally, there are version control labels and internal markers still embedded in the active tables.

Looking at the narrative consistency, the Abstract's claim about a 4.4× improvement is ambiguous about what it's being compared against—the context suggests it's comparing against RASP with α=1.0, which would actually yield a 5.8× improvement, not 4.4×. And the introduction's p<0.001 significance claim for the first contribution appears to be overstated. 我注意到 RASP(α=2.0) 是实验中表现最优的配置，但它没有出现在主要结果表中。同时，结论部分直接引用具体数值而不是指向相应的图表，这样的呈现方式不够严谨。另外，MATH-500 数据集中有些条目标记为待重新评估，这影响了数据的可信度。

关于写作规则和可复现性，Limitations 部分长度符合期刊要求，Appendix 也没有重复内容。不过 calibration 数据的具体数量在正文中没有明确说明，只在附录的 CKA 稳定性分析中提到了 256/512/1024 这些数值。此外，章节之间缺少显式的过渡句来引导读者。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ab0c90c-9237-4487-a1dd-a44136040eac",
  "isSidechain": false,
  "requestId": "req_011CbJr3MS8utsL9AQfXK9PP",
  "type": "assistant",
  "uuid": "7eabb6f6-331c-4b82-b9a5-71f53dcfff27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016T3yqxdmijuZ8CqQVNRMy8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7447,
      "cache_read_input_tokens": 94145,
      "output_tokens": 3941,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3941,
          "cache_read_input_tokens": 94145,
          "cache_creation_input_tokens": 7447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7447
          },
          "type": "message"
        }
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

_source line 87 · 2026-05-23T04:12:15.100Z_

审计完成。以下是结构化结果。

```
[CONTENT_AUDIT_START]
- [critical] [叙事一致性] Intro contribution 1 和 Conclusion 称 "mean |Δ(GRPO-SFT)| = 0.54 pp ... across GSM8K and MBPP"，但 Section 5.3 明确标注 0.54 是 "on GSM8K"。MBPP 表中三个 fine-grained 方法的 |Δ| 均值约 1.25 pp (CKA +1.34, Standard +1.07, RASP +1.34)，跨基准加权均值远高于 0.54。这是核心 claim 的数字不一致。
- [critical] [贡献-范围对齐] experiments.tex:85 声称 "decoupling holds across HumanEval and MBPP"，limitations.tex:15 和 ethics.tex:1 也列出 HumanEval 作为评测基准，但论文全文没有任何 HumanEval 表格或定量数据。声称覆盖四个 benchmark 但实际只展示三个。
- [critical] [内部信息残留] tab_math500.tex 有 7 个 GRPO 列标记 "--$^\star$"，脚注写 "Pending; will be filled upon completion"。提交论文包含未完成数据是 desk reject 风险。
- [critical] [内部信息残留] tab2_decoupling.tex:4（主表 Table 2 caption）包含 "controlled v5 GRPO configuration"；appendix.tex:67 包含 "clean v2 benchmark"。"v5"/"v2" 是内部实验版本编号，暴露内部工作流程。table1_postprune.tex:4 也有 "GRPO v5"（虽未被 \input 引用，仍存在于提交目录中）。
- [critical] [叙事一致性] Abstract 说 "importance-dominated pruning ($\alpha{=}1.0$) collapses while diversity-preserving criteria achieve active learning (peak reward 4.4$\times$)"。4.4× 实际是 CKA-only/Standard (0.354/0.081=4.37)，但句中紧跟 α=1.0 使读者自然理解为 CKA-only/RASP(α=1.0) (0.354/0.061=5.8×)。Intro:24 明确写 "4.4× Standard" 无歧义，但 Abstract 的比较基准模糊。
- [critical] [Claim 强度] introduction.tex:30 Contribution 1 写 "+1.51 pp differential; p<0.001"。p<0.001 来自 CKA-only vs Standard GRPO 总 gap 的 Welch's t 检验（72.76% vs 65.56%），不是检验 1.51 pp differential（即 GRPO 相比 SFT 放大的差值）本身是否显著。将 p 值与 differential 并列，暗示 differential 有统计显著性——实际上并未检验。
- [warning] [去AI] abstract.tex:1, introduction.tex:5/11/18, related_work.tex:12/21, method.tex:124, experiments.tex:62/73/130, conclusion.tex:10, limitations.tex:9, appendix.tex:153/261/262 共 15 处 em-dash (---)。em-dash 是最显著的 AI 写作标志，审稿人高度敏感，应全部替换为逗号、括号或拆分句子。
- [warning] [内部信息残留] experiments.tex:28 和 tab2_decoupling.tex:4 使用 \texttt{reward\_desert\_patience}=50 但从未定义此参数含义。这不是标准 GRPO 参数名，疑似内部代码变量名泄露。要么定义其含义，要么移除。
- [warning] [符号] RASP 命名双重含义：Method §3.3 中 RASP 是含 α 的通用框架（α=0 退化为 Standard，α→∞ 趋近 CKA-only），但 Experiments §5.1 中 RASP 特指 α=1.0（Table 1-2 中表现最差的配置）。RASP(α=2.0) 是最优配置但仅出现在 Appendix Table 3。论文"提出"的方法在主实验表中恰好是最差配置，叙事上令人困惑。
- [warning] [章节结构] conclusion.tex:6 直接写 μ=0.62 和 μ≥0.88 等数字，违反"Discussion 不应重复 Results 具体数字，应引用 Figure/Table 编号"的规范。应改为引用 Figure 4。
- [warning] [实验严谨性] tab_math500.tex 中 CKA-only SFT 25.8% 和 GRPO 26.4% 标记 $^\ddagger$ "Evaluated with earlier answer extraction script; re-evaluation pending"。数据来源不确定的结果不应出现在最终论文中。
- [warning] [可复现性] 正文和 Experiments 未明确说明 pruning calibration 使用的样本数量。experiments.tex:29 说 "calibration and SFT use identical configurations" 但未给出 M 值。Appendix CKA stability 节提到 256/512/1024 但未指明实际使用量。应在 §5.1 明确声明。
- [warning] [去AI] 多处 -ing 分词短语结尾：experiments.tex:130 "confirming that recoverability..."、related_work.tex:25 "showing that the pruning criterion..."、appendix.tex:272 "indicating more policy exploration"。属于 AI 写作典型标志，建议改写。
- [info] [章节过渡] Introduction 末尾（contribution 列表结束）直接跳到 Related Work，无过渡句；Related Work 末尾直接跳到 Method，同样无过渡。顶会论文通常在章节间有简短衔接。
- [info] [Limitations] Limitations 约 150 words，覆盖 3 个维度（架构/诊断/复制），符合 EMNLP 2026"只需要写一小段，覆盖 3 个点左右"的规则。✅
- [info] [写作规则] Appendix 无重复 Limitations section，仅正文有一个 \section*{Limitations}。符合 EMNLP 2026"一篇文章只能有一个 limitations section"规则。✅
- [info] [写作规则] ARR Responsible NLP Checklist 未出现在论文 PDF 中，符合"在 OpenReview submission form 里面填写"的规则。✅
- [info] [可复现性] GRPO 训练总时间/GPU hours 未在正文或 appendix 中报告。SFT 时间 37 min 已声明，但 GRPO 100 steps 的训练时长缺失。
- [info] [内部信息残留] tables/ 目录包含多个未被 \input 引用的遗留表格文件（table2_recovery.tex 含 "TBD"、table1_postprune.tex 含 "v5"、table5_inference.tex）。虽不影响编译输出，但若意外包含在提交包中可能引发问题。
[CONTENT_AUDIT_END]
```

[AUDIT_DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7eabb6f6-331c-4b82-b9a5-71f53dcfff27",
  "isSidechain": false,
  "requestId": "req_011CbJr3MS8utsL9AQfXK9PP",
  "type": "assistant",
  "uuid": "1501dc82-da74-4c9a-8d40-80c40164257c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016T3yqxdmijuZ8CqQVNRMy8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7447,
      "cache_read_input_tokens": 94145,
      "output_tokens": 3941,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3941,
          "cache_read_input_tokens": 94145,
          "cache_creation_input_tokens": 7447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7447
          },
          "type": "message"
        }
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
  "lastPrompt": "项目：recovery_aware_struct_prune Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 6 critical,…",
  "leafUuid": "1501dc82-da74-4c9a-8d40-80c40164257c",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303"
}
```

---

### Runtime record

_source line 89_

```json
{
  "type": "ai-title",
  "aiTitle": "Recovery-aware structured pruning paper audit",
  "sessionId": "eb6dd8fa-dc16-4561-bba5-af5f73e15303"
}
```

---
