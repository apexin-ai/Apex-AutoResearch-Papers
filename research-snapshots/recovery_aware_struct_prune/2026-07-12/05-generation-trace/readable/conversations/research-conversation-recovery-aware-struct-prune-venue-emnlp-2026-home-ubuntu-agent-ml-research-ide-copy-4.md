# Research conversation: 项目：recovery_aware_struct_prune Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 90
- **Recorded user turns:** 1
- **Tool calls:** 28
- **Original source:** `logs/chats/exported-trajectories/account-1/7498c864-bfb8-423d-b165-a88bcbf00033.jsonl`
- **Structured JSON:** [`5c4cd6252b1f7408ca0d.json`](../../sessions/5c/5c4cd6252b1f7408ca0d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-25T09:07:24.421Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T09:07:24.421Z",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "content": "项目：recovery_aware_struct_prune\nVenue：emnlp-2026\n论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper\n\nPhase 1 确定性检查结果：\n源码检查: passed=False, 7 critical, 19 warning\n一致性检查: 0 critical, 0 warning\n编译: ✅, 页数: 16\n内部信息: 0 critical, 0 warning\n\n━━━ 用户自定义规则（作为额外检查项）━━━\n## 用户自定义规则（必须遵守）\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section\n- **[EMNLP 2026]** abstract 不要超过 200 words\n\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n请将以上规则逐条作为额外审计维度检查。违反的规则用 dimension `[写作规则]` 或 `[审稿规则]` 标记，severity 按实际影响判定。\n\n请按照你的角色指令执行内容结构审计。"
}
```

---

### Runtime record

_source line 2 · 2026-05-25T09:07:24.425Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T09:07:24.425Z",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033"
}
```

---

## Round 1

88 recorded events

### User

_source line 3 · 2026-05-25T09:07:24.459Z_

项目：recovery_aware_struct_prune
Venue：emnlp-2026
论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper

Phase 1 确定性检查结果：
源码检查: passed=False, 7 critical, 19 warning
一致性检查: 0 critical, 0 warning
编译: ✅, 页数: 16
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
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "b76761b8-7bbc-4fc5-acba-a8f0b4201280",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-25T09:07:24.458Z_

```json
{
  "parentUuid": "b76761b8-7bbc-4fc5-acba-a8f0b4201280",
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
  "uuid": "46fef501-fc9d-447a-a638-e854f3735fe7",
  "timestamp": "2026-05-25T09:07:24.458Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-25T09:07:24.458Z_

```json
{
  "parentUuid": "46fef501-fc9d-447a-a638-e854f3735fe7",
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
  "uuid": "c50c3354-58e4-4a83-a3cc-b66f7f9bfce9",
  "timestamp": "2026-05-25T09:07:24.458Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-25T09:07:24.458Z_

```json
{
  "parentUuid": "c50c3354-58e4-4a83-a3cc-b66f7f9bfce9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5ee8036b-e0ea-40da-8943-446b2532b17a",
  "timestamp": "2026-05-25T09:07:24.458Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
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
  "aiTitle": "Recovery-aware structural pruning paper review",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033"
}
```

---

### Assistant

_source line 8 · 2026-05-25T09:07:29.626Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a content structure audit on the paper for the `recovery_aware_struct_prune` project. Let me follow the execution flow:

1. Read the two skill files for audit standards
2. Read all .tex files in the paper directory
3. Audit across all dimensions
4. Output structured findings

Let me start by reading the skill files and finding the .tex files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ee8036b-e0ea-40da-8943-446b2532b17a",
  "isSidechain": false,
  "requestId": "req_011CbP2H82K1n9raJLSfsaAM",
  "type": "assistant",
  "uuid": "23375b63-c4e5-4575-b712-ee3904b65673",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nrki1FRd9uarpnHb9Ckwm1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26956,
      "cache_read_input_tokens": 11846,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 353,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26956
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-25T09:07:30.060Z_

开始执行内容结构审计。先加载审计标准和论文源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23375b63-c4e5-4575-b712-ee3904b65673",
  "isSidechain": false,
  "requestId": "req_011CbP2H82K1n9raJLSfsaAM",
  "type": "assistant",
  "uuid": "7029122e-8e3e-4351-8b61-e812e685d153",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nrki1FRd9uarpnHb9Ckwm1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26956,
      "cache_read_input_tokens": 11846,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 353,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26956
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-25T09:07:30.612Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E5LksHy1FbrqF59BgqnTz6`</summary>

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
  "parentUuid": "7029122e-8e3e-4351-8b61-e812e685d153",
  "isSidechain": false,
  "requestId": "req_011CbP2H82K1n9raJLSfsaAM",
  "type": "assistant",
  "uuid": "5b63a0bc-9d8e-4d40-b18c-a824fd1d7173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nrki1FRd9uarpnHb9Ckwm1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26956,
      "cache_read_input_tokens": 11846,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 353,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26956
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-25T09:07:31.734Z_

<details><summary>↩ Tool result · `toolu_01KgqMU7buvJsnts37UiLYiy`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/_deprecated/table2_recovery.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/_deprecated/table5_inference.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/_deprecated/table1_postprune.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fda138fa-cfad-4d91-9c43-436b6358e65e",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "c6ca1c3f-9f2d-430b-91fa-5a5ea26bf92c",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/_deprecated/table2_recovery.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/_deprecated/table5_inference.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/_deprecated/table1_postprune.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/ethics.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex"
    ],
    "durationMs": 12,
    "numFiles": 25,
    "truncated": false
  },
  "sourceToolAssistantUUID": "fda138fa-cfad-4d91-9c43-436b6358e65e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T09:07:30.624Z_

<details><summary>↩ Tool result · `toolu_01E5LksHy1FbrqF59BgqnTz6`</summary>

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
  "parentUuid": "5b63a0bc-9d8e-4d40-b18c-a824fd1d7173",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "47e7fe05-d9a8-4767-8ef3-631cfd8da981",
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
  "sourceToolAssistantUUID": "5b63a0bc-9d8e-4d40-b18c-a824fd1d7173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 13 · 2026-05-25T09:07:31.131Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VytQ4SkhrhjGgNsb4SQ6GT`</summary>

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
  "parentUuid": "47e7fe05-d9a8-4767-8ef3-631cfd8da981",
  "isSidechain": false,
  "requestId": "req_011CbP2H82K1n9raJLSfsaAM",
  "type": "assistant",
  "uuid": "a569ebf5-a8e3-4f79-9f84-6ff230c9a20d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nrki1FRd9uarpnHb9Ckwm1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26956,
      "cache_read_input_tokens": 11846,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 353,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26956
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-25T09:07:31.138Z_

<details><summary>↩ Tool result · `toolu_01VytQ4SkhrhjGgNsb4SQ6GT`</summary>

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
  "parentUuid": "a569ebf5-a8e3-4f79-9f84-6ff230c9a20d",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "1fac7169-1d95-476c-b133-6d348b9672d8",
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
  "sourceToolAssistantUUID": "a569ebf5-a8e3-4f79-9f84-6ff230c9a20d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 15 · 2026-05-25T09:07:31.717Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KgqMU7buvJsnts37UiLYiy`</summary>

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
  "parentUuid": "1fac7169-1d95-476c-b133-6d348b9672d8",
  "isSidechain": false,
  "requestId": "req_011CbP2H82K1n9raJLSfsaAM",
  "type": "assistant",
  "uuid": "fda138fa-cfad-4d91-9c43-436b6358e65e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nrki1FRd9uarpnHb9Ckwm1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26956,
      "cache_read_input_tokens": 11846,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 353,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26956
          },
          "type": "message"
        }
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
  "lastPrompt": "项目：recovery_aware_struct_prune Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 7 critical,…",
  "leafUuid": "c6ca1c3f-9f2d-430b-91fa-5a5ea26bf92c",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Recovery-aware structural pruning paper review",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033"
}
```

---

### Assistant

_source line 18 · 2026-05-25T09:07:35.084Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read all the main .tex files (excluding backup and deprecated). Let me read them all in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6ca1c3f-9f2d-430b-91fa-5a5ea26bf92c",
  "isSidechain": false,
  "requestId": "req_011CbP2Hf1t7i6JT7iNF7KWc",
  "type": "assistant",
  "uuid": "38fe62f5-aaa2-4355-a873-1cb598bc002d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBhgTD9Gn7USQxSLgKGD5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12668,
      "cache_read_input_tokens": 38802,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 38802,
          "cache_creation_input_tokens": 12668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12668
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-25T09:07:35.585Z_

读取所有主要 .tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38fe62f5-aaa2-4355-a873-1cb598bc002d",
  "isSidechain": false,
  "requestId": "req_011CbP2Hf1t7i6JT7iNF7KWc",
  "type": "assistant",
  "uuid": "915a7d41-d625-4f6b-9a93-d716a3247683",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBhgTD9Gn7USQxSLgKGD5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12668,
      "cache_read_input_tokens": 38802,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 38802,
          "cache_creation_input_tokens": 12668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12668
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-25T09:07:36.082Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JwsckcJWK4ktWouGSAGzJu`</summary>

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
  "parentUuid": "915a7d41-d625-4f6b-9a93-d716a3247683",
  "isSidechain": false,
  "requestId": "req_011CbP2Hf1t7i6JT7iNF7KWc",
  "type": "assistant",
  "uuid": "bdd6f0c7-069b-4dc7-a1c1-c6a93501c746",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBhgTD9Gn7USQxSLgKGD5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12668,
      "cache_read_input_tokens": 38802,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 38802,
          "cache_creation_input_tokens": 12668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12668
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-25T09:07:40.885Z_

<details><summary>↩ Tool result · `toolu_01S4VNBQ3WKXZT7Rz1M8KmDW`</summary>

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
25	\title{How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM}
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
  "parentUuid": "f906d88a-3e97-4e93-b493-c0495a22c7f0",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "fc6724a7-7fcb-4041-b3c9-73d962f45a6a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{siunitx}\n\\usepackage{algorithm}\n\\usepackage[noend]{algpseudocode}\n\\usepackage{enumitem}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\n\\newcommand{\\rasp}{\\textsc{Rasp}}\n\n\\title{How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{conclusion}\n\n\\section*{Limitations}\n\\input{limitations}\n\n\\section*{Ethics Statement}\n\\input{ethics}\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 54,
      "startLine": 1,
      "totalLines": 54
    }
  },
  "sourceToolAssistantUUID": "f906d88a-3e97-4e93-b493-c0495a22c7f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T09:07:36.086Z_

<details><summary>↩ Tool result · `toolu_01JwsckcJWK4ktWouGSAGzJu`</summary>

```text
1	Structured pruning compresses reasoning Large Language Models (LLMs) by removing redundant components from their feed-forward sub-layers, but the pruned model requires recovery training---typically Supervised Fine-Tuning (SFT) or Reinforcement Learning with Verifiable Rewards (RLVR)---to restore reasoning capabilities.
2	RLVR is widely assumed to be the superior recovery paradigm, yet our results suggest this advantage is attributable to the pruning criterion rather than an inherent property of RL\@.
3	We propose Recovery-Aware Structured Pruning (\rasp{}), a parameterized scoring function that balances gradient importance with representational diversity measured via Centered Kernel Alignment (CKA).
4	Across four pruning criteria applied to a 7B reasoning model, we identify a \emph{recovery capacity spectrum}: diversity-preserving criteria sustain active RL training, while importance-dominated criteria exhibit reward collapse.
5	Despite this stark divergence in training dynamics, SFT and GRPO yield near-identical downstream accuracy at moderate sparsity---a phenomenon we term \emph{reward-accuracy decoupling}.
6	These findings hold across three benchmarks, with preliminary cross-scale and cross-model evidence.\footnote{Code and data available at \url{https://github.com/anonymous-nlp-2026/recovery_aware_struct_prune}.}
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdd6f0c7-069b-4dc7-a1c1-c6a93501c746",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "e8a2ae66-ae05-4cde-8979-34103d8cb68c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex",
      "content": "Structured pruning compresses reasoning Large Language Models (LLMs) by removing redundant components from their feed-forward sub-layers, but the pruned model requires recovery training---typically Supervised Fine-Tuning (SFT) or Reinforcement Learning with Verifiable Rewards (RLVR)---to restore reasoning capabilities.\nRLVR is widely assumed to be the superior recovery paradigm, yet our results suggest this advantage is attributable to the pruning criterion rather than an inherent property of RL\\@.\nWe propose Recovery-Aware Structured Pruning (\\rasp{}), a parameterized scoring function that balances gradient importance with representational diversity measured via Centered Kernel Alignment (CKA).\nAcross four pruning criteria applied to a 7B reasoning model, we identify a \\emph{recovery capacity spectrum}: diversity-preserving criteria sustain active RL training, while importance-dominated criteria exhibit reward collapse.\nDespite this stark divergence in training dynamics, SFT and GRPO yield near-identical downstream accuracy at moderate sparsity---a phenomenon we term \\emph{reward-accuracy decoupling}.\nThese findings hold across three benchmarks, with preliminary cross-scale and cross-model evidence.\\footnote{Code and data available at \\url{https://github.com/anonymous-nlp-2026/recovery_aware_struct_prune}.}\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  },
  "sourceToolAssistantUUID": "bdd6f0c7-069b-4dc7-a1c1-c6a93501c746",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T09:07:36.558Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GqoW2UR2gBw15Fp9F1vjJp`</summary>

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
  "parentUuid": "e8a2ae66-ae05-4cde-8979-34103d8cb68c",
  "isSidechain": false,
  "requestId": "req_011CbP2Hf1t7i6JT7iNF7KWc",
  "type": "assistant",
  "uuid": "a86f7187-5270-4879-9f7c-4ad6f52115c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBhgTD9Gn7USQxSLgKGD5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12668,
      "cache_read_input_tokens": 38802,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 38802,
          "cache_creation_input_tokens": 12668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12668
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-25T09:07:36.563Z_

<details><summary>↩ Tool result · `toolu_01GqoW2UR2gBw15Fp9F1vjJp`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Reasoning Large Language Models can be compressed through structured pruning, but the pruned model must recover its reasoning capabilities through fine-tuning.
5	The dominant assumption is that the recovery paradigm (SFT versus RLVR) determines recovery quality: \citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, substantially outperforming SFT.
6	Our results suggest that this hierarchy is attributable to suboptimal pruning rather than a fundamental property of RL\@.
7	When pruning preserves representational diversity, the choice of recovery paradigm has minimal effect on downstream accuracy within 20--25\% fine-grained MLP sparsity on Qwen2.5-family models: at 20\% sparsity, mean $|\Delta(\text{GRPO}-\text{SFT})| {=} 0.54$\,pp across the four fine-grained criteria (max $0.61$\,pp); including dose-response variations, MBPP, and MATH-500, the maximum observed difference is $1.8$\,pp.
8	The pruning criterion---not the recovery paradigm---appears to be the primary determinant of post-pruning reasoning quality.
9	Since RL optimizes reward as a proxy for task performance, one would expect reward improvements to translate into accuracy gains---making their divergence noteworthy.
10	
11	This divergence is surprising because RL and SFT impose fundamentally different demands on model representations: RL compresses incorrect paths while SFT expands correct ones~\citep{rlsqueezes2026}. Yet existing structured pruning methods for reasoning LLMs~\citep{graspprune2026,resp2025,llmpruner2023,bonsai2025} optimize for post-pruning quality without examining how the criterion shapes downstream RL recovery.
12	No prior work has compared multiple pruning criteria under RL or investigated whether the ``RLVR $>$ SFT'' advantage persists across pruning strategies.
13	We note that \citet{selfhealing2025} evaluate unstructured magnitude pruning retaining 96.5\% of dense parameters; our findings concern fine-grained structural pruning where entire channel groups are removed, and the two settings may impose different demands on RL recovery.
14	
15	\begin{figure}[t]
16	\centering
17	\includegraphics[width=\columnwidth]{figures/paper/fig1_dose_response.pdf}
18	\caption{Dose-response curve for the CKA diversity coefficient $\alpha$ at 20\% MLP channel sparsity on GSM8K ($N{=}1{,}319$). Recovery accuracy follows an inverted-U, peaking at $\alpha{=}2.0$ (66.11\%). SFT and GRPO curves nearly overlap ($|\Delta| \leq 1.14$\,pp at every point), illustrating reward-accuracy decoupling: the pruning criterion, not the recovery paradigm, determines outcome at this sparsity level.}
19	\label{fig:dose_response}
20	\end{figure}
21	
22	We present a controlled comparison on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} at 20\% MLP channel sparsity, varying the balance between gradient importance and CKA-based representational diversity~\citep{kornblith2019cka} via a coefficient $\alpha$ in the pruning score (Figure~\ref{fig:dose_response}).
23	The dose-response curve reveals an inverted-U: recovery peaks at $\alpha{=}2.0$ (66.11\% GRPO on GSM8K~\citep{cobbe2021gsm8k}), where importance and diversity reach optimal balance.
24	Under GRPO~\citep{shao2024grpo} training, four criteria produce a \textbf{recovery capacity spectrum}---a gradient in the pruned model's ability to regain reasoning through post-hoc training---ranging from active learning (CKA-only, peak reward 4.4$\times$ Standard) through stagnation (Random) to reward collapse (\rasp{} at $\alpha{=}1.0$), that tracks preserved representational diversity rather than gradient importance.
25	A depth pruning baseline (ShortGPT;~\citealp{shortgpt2024}) is the only method with $|\Delta| > 1$\,pp on GSM8K ($-$1.36\,pp), suggesting that pruning granularity interacts with RL trainability.
26	
27	Our contributions are:
28	\begin{enumerate}[nosep,leftmargin=*]
29	    \item \textbf{Reward-accuracy decoupling.} At 20--25\% sparsity, GRPO and SFT produce near-identical accuracy across all four fine-grained criteria (mean $|\Delta| {=} 0.54$\,pp; max $1.8$\,pp including dose-response, MBPP, MATH-500). At 15\%, GRPO amplifies the CKA-guided advantage ($+$1.51\,pp), but this exception reinforces the main pattern (\S\ref{sec:decoupling}).
30	    \item \textbf{Recovery capacity spectrum.} We propose Recovery-Aware Structured Pruning (\rasp{}), combining gradient importance with CKA-based diversity via $\alpha$. Dose-response reveals an inverted-U peaking at $\alpha{=}2.0$ (66.11\% on GSM8K). Four criteria produce qualitatively distinct GRPO dynamics---from active learning to reward collapse---tracking preserved diversity. Preliminary evidence at 1.5B and across Qwen2.5-family models (\S\ref{sec:scoring}, \S\ref{sec:recovery_gradient}, \S\ref{sec:extended_analysis}).
31	\end{enumerate}
32	
33	\begin{figure*}[t]
34	\centering
35	\includegraphics[width=\textwidth]{figures/paper/fig1_method_framework.pdf}
36	\caption{Overview of our pruning comparison framework. \textbf{Left}: structural analysis computes importance $I(h)$ and CKA-based overlap $F(h)$ scores, which four scoring criteria combine differently (Eqs.~\ref{eq:standard}--\ref{eq:cka_only}). \textbf{Center}: ranked structures are removed up to the target sparsity, subject to per-layer capacity floors. \textbf{Right}: all pruned models undergo identical two-stage recovery (SFT warmup $\to$ GRPO). \textbf{Bottom}: the resulting recovery capacity spectrum, from active learning (CKA-only) to reward collapse (\rasp{} at $\alpha{=}1.0$), tracks preserved representational diversity rather than gradient importance.}
37	\label{fig:method_framework}
38	\end{figure*}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a86f7187-5270-4879-9f7c-4ad6f52115c0",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "5d14efe3-6f5c-4e34-8bfe-37a7952821c1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\nReasoning Large Language Models can be compressed through structured pruning, but the pruned model must recover its reasoning capabilities through fine-tuning.\nThe dominant assumption is that the recovery paradigm (SFT versus RLVR) determines recovery quality: \\citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, substantially outperforming SFT.\nOur results suggest that this hierarchy is attributable to suboptimal pruning rather than a fundamental property of RL\\@.\nWhen pruning preserves representational diversity, the choice of recovery paradigm has minimal effect on downstream accuracy within 20--25\\% fine-grained MLP sparsity on Qwen2.5-family models: at 20\\% sparsity, mean $|\\Delta(\\text{GRPO}-\\text{SFT})| {=} 0.54$\\,pp across the four fine-grained criteria (max $0.61$\\,pp); including dose-response variations, MBPP, and MATH-500, the maximum observed difference is $1.8$\\,pp.\nThe pruning criterion---not the recovery paradigm---appears to be the primary determinant of post-pruning reasoning quality.\nSince RL optimizes reward as a proxy for task performance, one would expect reward improvements to translate into accuracy gains---making their divergence noteworthy.\n\nThis divergence is surprising because RL and SFT impose fundamentally different demands on model representations: RL compresses incorrect paths while SFT expands correct ones~\\citep{rlsqueezes2026}. Yet existing structured pruning methods for reasoning LLMs~\\citep{graspprune2026,resp2025,llmpruner2023,bonsai2025} optimize for post-pruning quality without examining how the criterion shapes downstream RL recovery.\nNo prior work has compared multiple pruning criteria under RL or investigated whether the ``RLVR $>$ SFT'' advantage persists across pruning strategies.\nWe note that \\citet{selfhealing2025} evaluate unstructured magnitude pruning retaining 96.5\\% of dense parameters; our findings concern fine-grained structural pruning where entire channel groups are removed, and the two settings may impose different demands on RL recovery.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig1_dose_response.pdf}\n\\caption{Dose-response curve for the CKA diversity coefficient $\\alpha$ at 20\\% MLP channel sparsity on GSM8K ($N{=}1{,}319$). Recovery accuracy follows an inverted-U, peaking at $\\alpha{=}2.0$ (66.11\\%). SFT and GRPO curves nearly overlap ($|\\Delta| \\leq 1.14$\\,pp at every point), illustrating reward-accuracy decoupling: the pruning criterion, not the recovery paradigm, determines outcome at this sparsity level.}\n\\label{fig:dose_response}\n\\end{figure}\n\nWe present a controlled comparison on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} at 20\\% MLP channel sparsity, varying the balance between gradient importance and CKA-based representational diversity~\\citep{kornblith2019cka} via a coefficient $\\alpha$ in the pruning score (Figure~\\ref{fig:dose_response}).\nThe dose-response curve reveals an inverted-U: recovery peaks at $\\alpha{=}2.0$ (66.11\\% GRPO on GSM8K~\\citep{cobbe2021gsm8k}), where importance and diversity reach optimal balance.\nUnder GRPO~\\citep{shao2024grpo} training, four criteria produce a \\textbf{recovery capacity spectrum}---a gradient in the pruned model's ability to regain reasoning through post-hoc training---ranging from active learning (CKA-only, peak reward 4.4$\\times$ Standard) through stagnation (Random) to reward collapse (\\rasp{} at $\\alpha{=}1.0$), that tracks preserved representational diversity rather than gradient importance.\nA depth pruning baseline (ShortGPT;~\\citealp{shortgpt2024}) is the only method with $|\\Delta| > 1$\\,pp on GSM8K ($-$1.36\\,pp), suggesting that pruning granularity interacts with RL trainability.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Reward-accuracy decoupling.} At 20--25\\% sparsity, GRPO and SFT produce near-identical accuracy across all four fine-grained criteria (mean $|\\Delta| {=} 0.54$\\,pp; max $1.8$\\,pp including dose-response, MBPP, MATH-500). At 15\\%, GRPO amplifies the CKA-guided advantage ($+$1.51\\,pp), but this exception reinforces the main pattern (\\S\\ref{sec:decoupling}).\n    \\item \\textbf{Recovery capacity spectrum.} We propose Recovery-Aware Structured Pruning (\\rasp{}), combining gradient importance with CKA-based diversity via $\\alpha$. Dose-response reveals an inverted-U peaking at $\\alpha{=}2.0$ (66.11\\% on GSM8K). Four criteria produce qualitatively distinct GRPO dynamics---from active learning to reward collapse---tracking preserved diversity. Preliminary evidence at 1.5B and across Qwen2.5-family models (\\S\\ref{sec:scoring}, \\S\\ref{sec:recovery_gradient}, \\S\\ref{sec:extended_analysis}).\n\\end{enumerate}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig1_method_framework.pdf}\n\\caption{Overview of our pruning comparison framework. \\textbf{Left}: structural analysis computes importance $I(h)$ and CKA-based overlap $F(h)$ scores, which four scoring criteria combine differently (Eqs.~\\ref{eq:standard}--\\ref{eq:cka_only}). \\textbf{Center}: ranked structures are removed up to the target sparsity, subject to per-layer capacity floors. \\textbf{Right}: all pruned models undergo identical two-stage recovery (SFT warmup $\\to$ GRPO). \\textbf{Bottom}: the resulting recovery capacity spectrum, from active learning (CKA-only) to reward collapse (\\rasp{} at $\\alpha{=}1.0$), tracks preserved representational diversity rather than gradient importance.}\n\\label{fig:method_framework}\n\\end{figure*}\n",
      "numLines": 39,
      "startLine": 1,
      "totalLines": 39
    }
  },
  "sourceToolAssistantUUID": "a86f7187-5270-4879-9f7c-4ad6f52115c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T09:07:37.032Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EBktMP96Hobnh5Ju3rbZBC`</summary>

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
  "parentUuid": "5d14efe3-6f5c-4e34-8bfe-37a7952821c1",
  "isSidechain": false,
  "requestId": "req_011CbP2Hf1t7i6JT7iNF7KWc",
  "type": "assistant",
  "uuid": "44c7846e-94c8-4ada-a64b-27ef786dfb9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBhgTD9Gn7USQxSLgKGD5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12668,
      "cache_read_input_tokens": 38802,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 38802,
          "cache_creation_input_tokens": 12668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12668
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-25T09:07:37.036Z_

<details><summary>↩ Tool result · `toolu_01EBktMP96Hobnh5Ju3rbZBC`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Structured pruning of LLMs.}
5	Width pruning methods (LLM-Pruner~\citep{llmpruner2023}, Bonsai~\citep{bonsai2025}, GRASPrune~\citep{graspprune2026}) remove attention heads or MLP channels while preserving dense computation.
6	Depth pruning~\citep{shortgpt2024,slicegpt2024,yang2024laco} removes entire layers but causes severe reasoning degradation~\citep{shrestha2026layerpruninglimits}; \citet{doingmore2026} revisit the trade-off under test-time scaling.
7	For reasoning models, RESP~\citep{resp2025}, RAC~\citep{rac2025}, and SSGR~\citep{ssgr2025} refine calibration data but retain gradient-based importance as the scoring criterion; \citet{llms2lrms2026} confirm width pruning is more robust than depth pruning for reasoning but do not study RLVR recovery.
8	A separate line uses functional structure to guide pruning: FANG~\citep{fang_2025} clusters FFN neurons by activation, FuncNet~\citep{funcnet_2025} decomposes LLMs via independent component analysis, and MPruner~\citep{mpruner2024} applies inter-layer CKA~\citep{kornblith2019cka} for depth pruning in CNNs.
9	We differ in both granularity and objective: \emph{intra-layer} CKA between individual structures, optimizing for RL recovery capacity rather than immediate accuracy.
10	
11	\paragraph{Pruning-aware recovery.}
12	\citet{selfhealing2025} show that RLVR restores pruned reasoning models to near-original accuracy, outperforming SFT, but evaluate only importance-based unstructured pruning at low sparsity (96.5\% retention).
13	Under fine-grained structural pruning at 20--25\% sparsity, our controlled experiments indicate that this advantage diminishes when pruning preserves representational diversity, suggesting the effect is attributable to the pruning criterion rather than to RL itself.
14	Other work optimizes complementary axes: post-pruning scaling ($P^2$~Law;~\citealp{p2law2025}), recovery data selection (PASER;~\citealp{paser2025}), joint pruning-tuning (PAT;~\citealp{pat2025}), post-hoc attention compensation (RestoreLCC;~\citealp{restorelcc_2025}), iterative prune-tune loops~\citep{boiling_frog_2026}, post-RLVR compression (OPSD;~\citealp{opsd2026}), and rollout pruning during RLVR~\citep{xu2026arrol}---but none study which \emph{pruning criterion} enables RL-based recovery.
15	The Lottery Ticket Hypothesis~\citep{frankle2019lth} asks which subnetworks train effectively from scratch; our recovery capacity spectrum poses the analogous question for post-pruning recovery.
16	While LTH concerns pruning at initialization seeking sparse subnetworks that train from scratch, our setting involves post-training structured pruning followed by recovery; the analogy is conceptual (pruning strategy affects trainability) rather than technical.
17	Concurrent work benchmarks reasoning model compression~\citep{li2025reasoning_compression} and studies whether pruning can improve reasoning efficiency~\citep{canpruning2025}, but neither isolates the pruning criterion's effect on RL recovery.
18	
19	\paragraph{RLVR training dynamics.}
20	\citet{rlsqueezes2026} show that RLVR \emph{compresses} incorrect reasoning trajectories while SFT \emph{expands} correct ones, predicting RL--SFT complementarity.
21	Our results qualify this prediction: the asymmetry manifests as a recovery capacity difference (the spectrum), but the expected accuracy gap is not observed when pruning preserves representational diversity ($|\Delta| \leq 1.8$\,pp across GSM8K, MBPP, and MATH-500; \S\ref{sec:decoupling}).
22	RL instability is well studied in the RL from Human Feedback (RLHF) context~\citep{gao2023overoptimization,dong2025rlplus,shah2025comedy}; \citet{mukherjee2025rlsubnetworks} find that RL fine-tuning updates only 5--30\% of parameters, raising the question of whether pruning criteria interact with this active subnetwork.
23	We connect these observations to structural pruning: the pruning criterion appears to shape susceptibility to RL collapse, while accuracy remains largely insensitive to the recovery paradigm at 20--25\% sparsity within our experimental scope.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44c7846e-94c8-4ada-a64b-27ef786dfb9b",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "6dcd7a3e-56e6-4b65-b162-f16e3226fc5f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Structured pruning of LLMs.}\nWidth pruning methods (LLM-Pruner~\\citep{llmpruner2023}, Bonsai~\\citep{bonsai2025}, GRASPrune~\\citep{graspprune2026}) remove attention heads or MLP channels while preserving dense computation.\nDepth pruning~\\citep{shortgpt2024,slicegpt2024,yang2024laco} removes entire layers but causes severe reasoning degradation~\\citep{shrestha2026layerpruninglimits}; \\citet{doingmore2026} revisit the trade-off under test-time scaling.\nFor reasoning models, RESP~\\citep{resp2025}, RAC~\\citep{rac2025}, and SSGR~\\citep{ssgr2025} refine calibration data but retain gradient-based importance as the scoring criterion; \\citet{llms2lrms2026} confirm width pruning is more robust than depth pruning for reasoning but do not study RLVR recovery.\nA separate line uses functional structure to guide pruning: FANG~\\citep{fang_2025} clusters FFN neurons by activation, FuncNet~\\citep{funcnet_2025} decomposes LLMs via independent component analysis, and MPruner~\\citep{mpruner2024} applies inter-layer CKA~\\citep{kornblith2019cka} for depth pruning in CNNs.\nWe differ in both granularity and objective: \\emph{intra-layer} CKA between individual structures, optimizing for RL recovery capacity rather than immediate accuracy.\n\n\\paragraph{Pruning-aware recovery.}\n\\citet{selfhealing2025} show that RLVR restores pruned reasoning models to near-original accuracy, outperforming SFT, but evaluate only importance-based unstructured pruning at low sparsity (96.5\\% retention).\nUnder fine-grained structural pruning at 20--25\\% sparsity, our controlled experiments indicate that this advantage diminishes when pruning preserves representational diversity, suggesting the effect is attributable to the pruning criterion rather than to RL itself.\nOther work optimizes complementary axes: post-pruning scaling ($P^2$~Law;~\\citealp{p2law2025}), recovery data selection (PASER;~\\citealp{paser2025}), joint pruning-tuning (PAT;~\\citealp{pat2025}), post-hoc attention compensation (RestoreLCC;~\\citealp{restorelcc_2025}), iterative prune-tune loops~\\citep{boiling_frog_2026}, post-RLVR compression (OPSD;~\\citealp{opsd2026}), and rollout pruning during RLVR~\\citep{xu2026arrol}---but none study which \\emph{pruning criterion} enables RL-based recovery.\nThe Lottery Ticket Hypothesis~\\citep{frankle2019lth} asks which subnetworks train effectively from scratch; our recovery capacity spectrum poses the analogous question for post-pruning recovery.\nWhile LTH concerns pruning at initialization seeking sparse subnetworks that train from scratch, our setting involves post-training structured pruning followed by recovery; the analogy is conceptual (pruning strategy affects trainability) rather than technical.\nConcurrent work benchmarks reasoning model compression~\\citep{li2025reasoning_compression} and studies whether pruning can improve reasoning efficiency~\\citep{canpruning2025}, but neither isolates the pruning criterion's effect on RL recovery.\n\n\\paragraph{RLVR training dynamics.}\n\\citet{rlsqueezes2026} show that RLVR \\emph{compresses} incorrect reasoning trajectories while SFT \\emph{expands} correct ones, predicting RL--SFT complementarity.\nOur results qualify this prediction: the asymmetry manifests as a recovery capacity difference (the spectrum), but the expected accuracy gap is not observed when pruning preserves representational diversity ($|\\Delta| \\leq 1.8$\\,pp across GSM8K, MBPP, and MATH-500; \\S\\ref{sec:decoupling}).\nRL instability is well studied in the RL from Human Feedback (RLHF) context~\\citep{gao2023overoptimization,dong2025rlplus,shah2025comedy}; \\citet{mukherjee2025rlsubnetworks} find that RL fine-tuning updates only 5--30\\% of parameters, raising the question of whether pruning criteria interact with this active subnetwork.\nWe connect these observations to structural pruning: the pruning criterion appears to shape susceptibility to RL collapse, while accuracy remains largely insensitive to the recovery paradigm at 20--25\\% sparsity within our experimental scope.\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  },
  "sourceToolAssistantUUID": "44c7846e-94c8-4ada-a64b-27ef786dfb9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-25T09:07:37.497Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L35cWzNu27TM9V4S3KeMSd`</summary>

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
  "parentUuid": "6dcd7a3e-56e6-4b65-b162-f16e3226fc5f",
  "isSidechain": false,
  "requestId": "req_011CbP2Hf1t7i6JT7iNF7KWc",
  "type": "assistant",
  "uuid": "b369768b-507f-40f3-971e-ce97a6b09723",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBhgTD9Gn7USQxSLgKGD5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12668,
      "cache_read_input_tokens": 38802,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 38802,
          "cache_creation_input_tokens": 12668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12668
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-25T09:07:37.501Z_

<details><summary>↩ Tool result · `toolu_01L35cWzNu27TM9V4S3KeMSd`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	To isolate how the pruning criterion affects post-RLVR recovery, we hold everything else constant: a shared structural analysis computes importance and functional overlap scores for all prunable structures, four scoring criteria combine these scores differently to select structures for removal, and an identical two-stage recovery pipeline is applied to every pruned model.
5	The only variable across conditions is which structures are removed (Figure~\ref{fig:method_framework}).
6	
7	\subsection{Preliminaries and Notation}
8	\label{sec:prelim}
9	
10	\paragraph{Structured pruning.}
11	Given a pretrained transformer $\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units (attention heads or MLP channels) to reduce model size while maintaining hardware-friendly dense computation.
12	We denote the set of prunable structures as $\mathcal{H} = \{h_1, h_2, \ldots, h_N\}$.
13	In this work, we focus exclusively on MLP channel group pruning; the formalism below covers attention heads for completeness, but all experiments remove only MLP groups.
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
30	Given a calibration set $\mathcal{D}_\text{cal} = \{(x_j, y_j)\}_{j=1}^{M}$ with $M{=}512$ randomly sampled examples, we compute activations and gradients on the concatenated sequences $(x_j, y_j)$.
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
42	We measure functional overlap using linear Centered Kernel Alignment (CKA;~\citealp{kornblith2019cka}), which quantifies similarity between two sets of representations invariant to orthogonal transformations and isotropic scaling.
43	Given activation matrices $\mathbf{X}, \mathbf{Y} \in \mathbb{R}^{n \times d}$ collected over $n$ calibration examples, linear CKA is:
44	\begin{equation}
45	    \text{CKA}(\mathbf{X}, \mathbf{Y}) = \frac{\text{HSIC}(\mathbf{X}, \mathbf{Y})}{\sqrt{\text{HSIC}(\mathbf{X}, \mathbf{X}) \cdot \text{HSIC}(\mathbf{Y}, \mathbf{Y})}},
46	    \label{eq:cka}
47	\end{equation}
48	where HSIC is the Hilbert-Schmidt Independence Criterion, $\text{HSIC}(\mathbf{X}, \mathbf{Y}) = \frac{1}{(n-1)^2} \operatorname{tr}(\mathbf{K} \mathbf{H} \mathbf{L} \mathbf{H})$, with $\mathbf{K} = \mathbf{X}\mathbf{X}^\top$, $\mathbf{L} = \mathbf{Y}\mathbf{Y}^\top$, and $\mathbf{H} = \mathbf{I}_n - \frac{1}{n}\mathbf{1}\mathbf{1}^\top$.
49	
50	For a GQA group $g_i$ in layer $\ell$, we form its representation by concatenating its constituent Q head activations: $\mathbf{X}_{g_i} = [\mathbf{a}_{q_1}; \ldots; \mathbf{a}_{q_G}] \in \mathbb{R}^{n \times Gd_h}$.
51	The functional overlap of $g_i$ is the mean pairwise CKA with other groups in the same layer:
52	\begin{equation}
53	    F(g_i) = \frac{1}{|\mathcal{G}_\ell| - 1} \sum_{\substack{g_j \in \mathcal{G}_\ell \\ j \neq i}} \text{CKA}(\mathbf{X}_{g_i}, \mathbf{X}_{g_j}).
54	    \label{eq:overlap}
55	\end{equation}
56	We apply the same intra-layer CKA overlap to MLP channel groups, partitioning each MLP intermediate dimension into equal-sized groups.
57	Unlike prior work that uses inter-layer CKA to identify globally redundant layers for depth pruning~\citep{mpruner2024,lachance2022cka}, we use \emph{intra-layer} CKA between individual structures to measure per-structure functional redundancy.
58	Computing all pairwise CKA scores adds minimal overhead ($O(L \cdot k^2)$, $k \le 28$; $<$2 min on one GPU).
59	
60	\paragraph{CKA reliability.}
61	Our intra-layer use between structures of identical dimensionality avoids sensitivities identified for cross-layer comparisons~\citep{davari2023cka,klabunde_similarity_survey_2023}; rankings are stable across calibration sizes (Spearman $\rho \geq 0.964$; Appendix~\ref{sec:appendix_cka_stability}).
62	
63	\subsection{Pruning Scoring Criteria}
64	\label{sec:scoring}
65	
66	We compare four scoring criteria that combine importance $I(h)$ and functional overlap $F(h)$ in different ways.
67	All four methods use the same per-layer capacity floor (${\ge}$40\% of MLP groups per layer must be retained, chosen to prevent any single layer from becoming a throughput bottleneck; ablation over $\tau \in \{0.3, 0.4, 0.5, 0.6\}$ in Appendix~\ref{sec:appendix_floor}) and global ranking procedure: structures are sorted by score, and the lowest-scoring structures are pruned up to the target sparsity ratio, skipping any candidate whose removal would violate the layer floor.
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
78	\rasp{} is a parameterized family of scoring functions indexed by $\alpha$, which controls the trade-off between gradient importance and diversity preservation:
79	\begin{equation}
80	    S_\text{rasp}(h) = I(h) \times \big(1 - F(h)\big)^\alpha,
81	    \label{eq:score}
82	\end{equation}
83	where $\alpha{=}0$ reduces to Standard (pure importance) and larger $\alpha$ increasingly favors diversity.
84	Dose-response analysis (\S\ref{sec:sparsity_cliff}) reveals that $\alpha{=}1.0$ yields suboptimal results---exhibiting reward collapse under GRPO due to insufficient diversity weighting---while $\alpha{=}2.0$ achieves peak recovery.
85	The multiplicative form ensures that structures with zero importance are automatically pruned ($S{=}0$) regardless of overlap; an additive alternative $\beta I(h) + (1{-}\beta)(1{-}F(h))$ would retain zero-importance structures if their overlap is low.
86	Structures with high importance \emph{and} low overlap receive the highest scores and are retained; those with high overlap are penalized and pruned preferentially.
87	At the empirically optimal $\alpha{=}2.0$, the diversity term $(1{-}F(h))^2$ dominates the score, making \rasp{} at $\alpha{=}2.0$ effectively CKA-guided with importance as a secondary filter (\S\ref{sec:sparsity_cliff}).
88	Nevertheless, \rasp{} at $\alpha{=}2.0$ outperforms CKA-only under both recovery paradigms (GRPO: 66.11\% vs.\ 64.39\%, $+$1.72\,pp; SFT: 64.97\% vs.\ 63.91\%, $+$1.06\,pp; Table~\ref{tab:alpha}), indicating that importance filtering provides complementary signal beyond diversity preservation alone.
89	
90	
91	\paragraph{CKA-only (overlap-only).}
92	CKA-only scoring disregards gradient importance, ranking structures by functional overlap alone.
93	Structures with the highest mean pairwise CKA similarity to other structures in their layer are removed first:
94	\begin{equation}
95	    S_\text{cka}(h) = 1 - F(h).
96	    \label{eq:cka_only}
97	\end{equation}
98	This criterion preserves all representationally unique structures regardless of their gradient importance, removing only those whose function is redundant with retained structures.
99	$S_\text{cka}$ corresponds to the limit $\alpha \to \infty$ in Eq.~\ref{eq:score}.
100	
101	\paragraph{Random.}
102	Structures are selected uniformly at random for removal, subject to the per-layer capacity floor.
103	This baseline controls for the effect of any informed scoring criterion.
104	
105	The four criteria span a spectrum from pure gradient importance (Standard) to pure representational diversity preservation (CKA-only), with \rasp{} at $\alpha{=}2.0$ as a diversity-dominant interpolation and Random as an uninformed control.
106	The key distinction is that CKA-only retains \emph{functionally unique} structures regardless of gradient contribution: structures deemed ``unimportant'' by gradient metrics may provide non-redundant computational pathways that facilitate RL exploration~\citep{rlsqueezes2026}.
107	
108	\subsection{Two-Stage Recovery}
109	\label{sec:recovery}
110	
111	After pruning, all four models undergo identical two-stage recovery: (1)~a brief SFT warmup on chain-of-thought demonstrations restores end-of-sequence generation and format compliance (pruning disrupts termination behavior, making direct GRPO infeasible); (2)~GRPO with binary reward enables RL-based exploration, redistributing functionality across remaining structures~\citep{rlsqueezes2026}, in contrast to SFT which imitates fixed trajectories.
112	Details in Section~\ref{sec:exp_setup} and Appendix~\ref{sec:appendix_training}.
113	
114	\subsection{Recovery Capacity Diagnostics}
115	\label{sec:diagnostics}
116	
117	We define \textbf{recovery capacity} as the model's ability to benefit from post-pruning recovery training, operationalized as peak mean reward over the GRPO training horizon.
118	Four diagnostics (mean reward, zero-variance batch fraction ($f_0$), gradient norm, and Kullback--Leibler (KL) divergence) distinguish three regimes: \emph{active learning} (rising reward, low $f_0$), \emph{stagnation} (flat reward), and \emph{collapse} (declining reward, high $f_0$, vanishing gradients).
119	
120	The complete pruning comparison procedure is given in Algorithm~\ref{alg:rasp} (Appendix~\ref{sec:appendix_algo}).
121	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b369768b-507f-40f3-971e-ce97a6b09723",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "d8b9be99-222c-4679-b87e-91dc00f4358b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nTo isolate how the pruning criterion affects post-RLVR recovery, we hold everything else constant: a shared structural analysis computes importance and functional overlap scores for all prunable structures, four scoring criteria combine these scores differently to select structures for removal, and an identical two-stage recovery pipeline is applied to every pruned model.\nThe only variable across conditions is which structures are removed (Figure~\\ref{fig:method_framework}).\n\n\\subsection{Preliminaries and Notation}\n\\label{sec:prelim}\n\n\\paragraph{Structured pruning.}\nGiven a pretrained transformer $\\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units (attention heads or MLP channels) to reduce model size while maintaining hardware-friendly dense computation.\nWe denote the set of prunable structures as $\\mathcal{H} = \\{h_1, h_2, \\ldots, h_N\\}$.\nIn this work, we focus exclusively on MLP channel group pruning; the formalism below covers attention heads for completeness, but all experiments remove only MLP groups.\n\n\\paragraph{Grouped Query Attention (GQA).}\nIn GQA architectures~\\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads ($G = n_Q / n_{KV}$ per group).\nFor DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$, $G{=}7$), we treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit.\n\n\\paragraph{RLVR and GRPO.}\nReinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.\nWe use Group Relative Policy Optimization (GRPO;~\\citealp{shao2024grpo}) as the recovery algorithm.\n\n\\subsection{Structural Analysis}\n\\label{sec:structural_analysis}\n\nAll four pruning criteria share a common structural analysis stage that computes two scores per structure: \\emph{importance} $I(h)$ capturing the structure's contribution to reasoning, and \\emph{functional overlap} $F(h)$ measuring representational redundancy with other structures in the same layer.\n\n\\paragraph{Calibration data.}\nWe compute importance and overlap scores on chain-of-thought reasoning data from GSM8K~\\citep{cobbe2021gsm8k} training examples.\nGiven a calibration set $\\mathcal{D}_\\text{cal} = \\{(x_j, y_j)\\}_{j=1}^{M}$ with $M{=}512$ randomly sampled examples, we compute activations and gradients on the concatenated sequences $(x_j, y_j)$.\n\n\\paragraph{Structural importance.}\nFor each structure $h$ with activation $\\mathbf{a}_h$, we approximate the loss change from removal via first-order Taylor expansion ($\\Delta\\mathcal{L} \\approx -\\mathbf{a}_h^\\top \\nabla_{\\mathbf{a}_h}\\mathcal{L}$, dropping $O(\\|\\mathbf{a}_h\\|^2)$ terms) and aggregate over the calibration set:\n\\begin{equation}\n    I(h) = \\left| \\sum_{(x,y) \\in \\mathcal{D}_\\text{cal}} \\mathbf{a}_h(x, y)^\\top \\frac{\\partial \\mathcal{L}(x, y)}{\\partial \\mathbf{a}_h} \\right|,\n    \\label{eq:importance}\n\\end{equation}\nwhere $\\mathcal{L}$ is the language modeling loss over the reasoning trace.\nFor a GQA group $g$ containing Q heads $\\{q_1, \\ldots, q_G\\}$ and KV head $k$, we aggregate: $I(g) = \\sum_{i=1}^{G} I(q_i) + I(k)$.\n\n\\paragraph{Functional overlap via CKA.}\nWe measure functional overlap using linear Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}), which quantifies similarity between two sets of representations invariant to orthogonal transformations and isotropic scaling.\nGiven activation matrices $\\mathbf{X}, \\mathbf{Y} \\in \\mathbb{R}^{n \\times d}$ collected over $n$ calibration examples, linear CKA is:\n\\begin{equation}\n    \\text{CKA}(\\mathbf{X}, \\mathbf{Y}) = \\frac{\\text{HSIC}(\\mathbf{X}, \\mathbf{Y})}{\\sqrt{\\text{HSIC}(\\mathbf{X}, \\mathbf{X}) \\cdot \\text{HSIC}(\\mathbf{Y}, \\mathbf{Y})}},\n    \\label{eq:cka}\n\\end{equation}\nwhere HSIC is the Hilbert-Schmidt Independence Criterion, $\\text{HSIC}(\\mathbf{X}, \\mathbf{Y}) = \\frac{1}{(n-1)^2} \\operatorname{tr}(\\mathbf{K} \\mathbf{H} \\mathbf{L} \\mathbf{H})$, with $\\mathbf{K} = \\mathbf{X}\\mathbf{X}^\\top$, $\\mathbf{L} = \\mathbf{Y}\\mathbf{Y}^\\top$, and $\\mathbf{H} = \\mathbf{I}_n - \\frac{1}{n}\\mathbf{1}\\mathbf{1}^\\top$.\n\nFor a GQA group $g_i$ in layer $\\ell$, we form its representation by concatenating its constituent Q head activations: $\\mathbf{X}_{g_i} = [\\mathbf{a}_{q_1}; \\ldots; \\mathbf{a}_{q_G}] \\in \\mathbb{R}^{n \\times Gd_h}$.\nThe functional overlap of $g_i$ is the mean pairwise CKA with other groups in the same layer:\n\\begin{equation}\n    F(g_i) = \\frac{1}{|\\mathcal{G}_\\ell| - 1} \\sum_{\\substack{g_j \\in \\mathcal{G}_\\ell \\\\ j \\neq i}} \\text{CKA}(\\mathbf{X}_{g_i}, \\mathbf{X}_{g_j}).\n    \\label{eq:overlap}\n\\end{equation}\nWe apply the same intra-layer CKA overlap to MLP channel groups, partitioning each MLP intermediate dimension into equal-sized groups.\nUnlike prior work that uses inter-layer CKA to identify globally redundant layers for depth pruning~\\citep{mpruner2024,lachance2022cka}, we use \\emph{intra-layer} CKA between individual structures to measure per-structure functional redundancy.\nComputing all pairwise CKA scores adds minimal overhead ($O(L \\cdot k^2)$, $k \\le 28$; $<$2 min on one GPU).\n\n\\paragraph{CKA reliability.}\nOur intra-layer use between structures of identical dimensionality avoids sensitivities identified for cross-layer comparisons~\\citep{davari2023cka,klabunde_similarity_survey_2023}; rankings are stable across calibration sizes (Spearman $\\rho \\geq 0.964$; Appendix~\\ref{sec:appendix_cka_stability}).\n\n\\subsection{Pruning Scoring Criteria}\n\\label{sec:scoring}\n\nWe compare four scoring criteria that combine importance $I(h)$ and functional overlap $F(h)$ in different ways.\nAll four methods use the same per-layer capacity floor (${\\ge}$40\\% of MLP groups per layer must be retained, chosen to prevent any single layer from becoming a throughput bottleneck; ablation over $\\tau \\in \\{0.3, 0.4, 0.5, 0.6\\}$ in Appendix~\\ref{sec:appendix_floor}) and global ranking procedure: structures are sorted by score, and the lowest-scoring structures are pruned up to the target sparsity ratio, skipping any candidate whose removal would violate the layer floor.\n\n\\paragraph{Standard (importance-only).}\nFollowing LLM-Pruner~\\citep{llmpruner2023}, structures are ranked solely by importance:\n\\begin{equation}\n    S_\\text{std}(h) = I(h).\n    \\label{eq:standard}\n\\end{equation}\nThis is the industry-standard criterion that retains gradient-important structures and removes ``unimportant'' ones.\n\n\\paragraph{RASP (recovery-aware composite).}\n\\rasp{} is a parameterized family of scoring functions indexed by $\\alpha$, which controls the trade-off between gradient importance and diversity preservation:\n\\begin{equation}\n    S_\\text{rasp}(h) = I(h) \\times \\big(1 - F(h)\\big)^\\alpha,\n    \\label{eq:score}\n\\end{equation}\nwhere $\\alpha{=}0$ reduces to Standard (pure importance) and larger $\\alpha$ increasingly favors diversity.\nDose-response analysis (\\S\\ref{sec:sparsity_cliff}) reveals that $\\alpha{=}1.0$ yields suboptimal results---exhibiting reward collapse under GRPO due to insufficient diversity weighting---while $\\alpha{=}2.0$ achieves peak recovery.\nThe multiplicative form ensures that structures with zero importance are automatically pruned ($S{=}0$) regardless of overlap; an additive alternative $\\beta I(h) + (1{-}\\beta)(1{-}F(h))$ would retain zero-importance structures if their overlap is low.\nStructures with high importance \\emph{and} low overlap receive the highest scores and are retained; those with high overlap are penalized and pruned preferentially.\nAt the empirically optimal $\\alpha{=}2.0$, the diversity term $(1{-}F(h))^2$ dominates the score, making \\rasp{} at $\\alpha{=}2.0$ effectively CKA-guided with importance as a secondary filter (\\S\\ref{sec:sparsity_cliff}).\nNevertheless, \\rasp{} at $\\alpha{=}2.0$ outperforms CKA-only under both recovery paradigms (GRPO: 66.11\\% vs.\\ 64.39\\%, $+$1.72\\,pp; SFT: 64.97\\% vs.\\ 63.91\\%, $+$1.06\\,pp; Table~\\ref{tab:alpha}), indicating that importance filtering provides complementary signal beyond diversity preservation alone.\n\n\n\\paragraph{CKA-only (overlap-only).}\nCKA-only scoring disregards gradient importance, ranking structures by functional overlap alone.\nStructures with the highest mean pairwise CKA similarity to other structures in their layer are removed first:\n\\begin{equation}\n    S_\\text{cka}(h) = 1 - F(h).\n    \\label{eq:cka_only}\n\\end{equation}\nThis criterion preserves all representationally unique structures regardless of their gradient importance, removing only those whose function is redundant with retained structures.\n$S_\\text{cka}$ corresponds to the limit $\\alpha \\to \\infty$ in Eq.~\\ref{eq:score}.\n\n\\paragraph{Random.}\nStructures are selected uniformly at random for removal, subject to the per-layer capacity floor.\nThis baseline controls for the effect of any informed scoring criterion.\n\nThe four criteria span a spectrum from pure gradient importance (Standard) to pure representational diversity preservation (CKA-only), with \\rasp{} at $\\alpha{=}2.0$ as a diversity-dominant interpolation and Random as an uninformed control.\nThe key distinction is that CKA-only retains \\emph{functionally unique} structures regardless of gradient contribution: structures deemed ``unimportant'' by gradient metrics may provide non-redundant computational pathways that facilitate RL exploration~\\citep{rlsqueezes2026}.\n\n\\subsection{Two-Stage Recovery}\n\\label{sec:recovery}\n\nAfter pruning, all four models undergo identical two-stage recovery: (1)~a brief SFT warmup on chain-of-thought demonstrations restores end-of-sequence generation and format compliance (pruning disrupts termination behavior, making direct GRPO infeasible); (2)~GRPO with binary reward enables RL-based exploration, redistributing functionality across remaining structures~\\citep{rlsqueezes2026}, in contrast to SFT which imitates fixed trajectories.\nDetails in Section~\\ref{sec:exp_setup} and Appendix~\\ref{sec:appendix_training}.\n\n\\subsection{Recovery Capacity Diagnostics}\n\\label{sec:diagnostics}\n\nWe define \\textbf{recovery capacity} as the model's ability to benefit from post-pruning recovery training, operationalized as peak mean reward over the GRPO training horizon.\nFour diagnostics (mean reward, zero-variance batch fraction ($f_0$), gradient norm, and Kullback--Leibler (KL) divergence) distinguish three regimes: \\emph{active learning} (rising reward, low $f_0$), \\emph{stagnation} (flat reward), and \\emph{collapse} (declining reward, high $f_0$, vanishing gradients).\n\nThe complete pruning comparison procedure is given in Algorithm~\\ref{alg:rasp} (Appendix~\\ref{sec:appendix_algo}).\n",
      "numLines": 121,
      "startLine": 1,
      "totalLines": 121
    }
  },
  "sourceToolAssistantUUID": "b369768b-507f-40f3-971e-ce97a6b09723",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-25T09:07:38.440Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LbC4PrdTouYSWr6DYrBzyG`</summary>

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
  "parentUuid": "d8b9be99-222c-4679-b87e-91dc00f4358b",
  "isSidechain": false,
  "requestId": "req_011CbP2Hf1t7i6JT7iNF7KWc",
  "type": "assistant",
  "uuid": "e4f97e83-5d17-482e-a046-301a97b00c80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBhgTD9Gn7USQxSLgKGD5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12668,
      "cache_read_input_tokens": 38802,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 38802,
          "cache_creation_input_tokens": 12668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12668
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-25T09:07:38.445Z_

<details><summary>↩ Tool result · `toolu_01LbC4PrdTouYSWr6DYrBzyG`</summary>

```text
1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	\begin{figure*}[t]
6	    \centering
7	    \begin{minipage}[t]{0.38\textwidth}
8	        \centering
9	        \includegraphics[width=\textwidth]{figures/paper/fig2_reward_trajectories.pdf}
10	        \centerline{\small (a) Reward trajectories}
11	    \end{minipage}
12	    \hfill
13	    \begin{minipage}[t]{0.58\textwidth}
14	        \centering
15	        \includegraphics[width=\textwidth]{figures/paper/fig3_collapse_dynamics.pdf}
16	        \centerline{\small (b) $f_0$ and gradient norm diagnostics}
17	    \end{minipage}
18	    \caption{GRPO training dynamics for four pruning criteria (100 steps, $\beta{=}0.01$, $T{=}0.4$). (a)~Reward trajectories: CKA-only reaches 0.354 peak; Random oscillates (0.14--0.19); Standard peaks at 0.081; \rasp{} at $\alpha{=}1.0$ declines to 0.010. (b)~Left: $f_0$ (zero-variance batch fraction); CKA-only remains below 0.35 while Standard and \rasp{} at $\alpha{=}1.0$ persist in the collapse zone ($f_0 > 0.5$). Right: gradient norm; \rasp{} at $\alpha{=}1.0$ exhibits near-zero norms throughout; Standard shows a transient minimum at step 90.}
19	    \label{fig:training_dynamics}
20	\end{figure*}
21	
22	\subsection{Experimental Setup}
23	\label{sec:exp_setup}
24	
25	\input{tables/tab1_recovery_gradient}
26	
27	\paragraph{Base model and evaluation.}
28	We evaluate on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\citep{qwen2.5} with GQA~\citep{ainslie2023gqa} (Section~\ref{sec:prelim}).
29	Our primary benchmark is GSM8K~\citep{cobbe2021gsm8k} ($N{=}1{,}319$ grade-school math problems; exact-match accuracy).
30	The unpruned model achieves 90.83\% (greedy decoding).
31	
32	\paragraph{Pruning methods.}
33	We compare four pruning criteria at 20\% structured sparsity, all removing the same number of MLP channel groups (200 of 784 across 28 layers, ${\sim}$1.45B parameters) with identical per-layer capacity floors (${\ge}$40\% retention per layer):
34	\begin{enumerate}[nosep,leftmargin=*]
35	    \item \textbf{CKA-only}: structures ranked by functional overlap $F(h)$ alone (Eq.~\ref{eq:overlap}); the most redundant groups are removed regardless of gradient importance.
36	    \item \textbf{Random}: uniform random selection among eligible groups.  Uses TRL's default 512-token generation limit (vs.\ 1{,}024 for other methods), which may disadvantage its reward trajectory; we retain it as a conservative lower bound rather than a direct comparison point.
37	    \item \textbf{Standard}: Taylor-expansion importance $I(h)$ alone (Eq.~\ref{eq:importance}); the least important groups are removed, following LLM-Pruner~\citep{llmpruner2023}.
38	    \item \textbf{\rasp{}} ($\alpha{=}1.0$): the composite score $S(h) = I(h) \times (1 - F(h))^\alpha$ (Eq.~\ref{eq:score}), removing structures that are both low-importance and functionally redundant.
39	\end{enumerate}
40	
41	\paragraph{Recovery pipeline and hardware.}
42	Immediately after pruning (before any recovery), all four methods produce near-zero GSM8K accuracy ($<$2\%), as the pruned models fail to generate coherent reasoning chains or proper termination tokens.
43	All four methods then undergo matched two-stage recovery (Section~\ref{sec:recovery}): SFT warmup (2 epochs, 7{,}473 GSM8K examples, 37 min) followed by GRPO (lr $1{\times}10^{-6}$, $\beta{=}0.01$, $T{=}0.4$, 100 steps on 1{,}000 problems; full hyperparameters in Table~\ref{tab:hyperparams}, Appendix~\ref{sec:appendix_training}).
44	All methods use \texttt{max\_completion\_length}{$=$}1{,}024 except Random (TRL default 512), making it a conservative comparison point.
45	We repeat GRPO with 3 seeds for CKA-only, Standard, and Random (\rasp{} at $\alpha{=}1.0$ uses a single seed); CKA-only achieves 64.39\% $\pm$ 0.19\,pp, Standard 59.84\% $\pm$ 0.38\,pp (Welch's $t$, $p{=}0.0009$, $d{=}11.1$; Appendix~\ref{sec:appendix_seed}).
46	The ``Unpruned'' baseline in Table~\ref{tab:decoupling} uses the same SFT-warmup checkpoint; the 9.56\,pp gap from the pre-warmup 90.83\% reflects warmup on a reduced training set, not pruning loss.
47	All experiments run on 2$\times$ NVIDIA RTX PRO 6000 GPUs (94\,GB VRAM each).
48	
49	
50	\subsection{Recovery Capacity Spectrum}
51	\label{sec:recovery_gradient}
52	
53	Under GRPO training, the four pruning criteria produce a clear recovery capacity spectrum: CKA-only $\gg$ Random $\gg$ Standard $>$ \rasp{} at $\alpha{=}1.0$ (Table~\ref{tab:recovery_gradient}, Figure~\ref{fig:training_dynamics}).
54	The pruning criterion, rather than training configuration, determines whether the model learns, stagnates, or exhibits reward collapse.
55	
56	Among these configurations, only the diversity-maximizing criterion (CKA-only) sustains active learning: peak reward 0.354 with $f_0$ as low as 0.125 (Figure~\ref{fig:training_dynamics}b).
57	Random, under a shorter generation limit, stagnates (reward 0.14--0.19, min $f_0 = 0.300$); Standard exhibits borderline collapse ($f_0 \geq 0.50$, peak reward 0.081); \rasp{} at $\alpha{=}1.0$ exhibits complete reward collapse ($f_0 \geq 0.675$, reward declining to 0.010, with near-zero KL divergence indicating minimal policy movement; Appendix~\ref{sec:appendix_kl}).
58	The dose-response analysis (\S\ref{sec:sparsity_cliff}) confirms CKA weighting as the critical variable: increasing $\alpha$ from 1.0 to 2.0 shifts \rasp{} from reward collapse to peak recovery (66.11\% vs.\ 64.39\% for CKA-only on GSM8K).
59	
60	
61	\subsection{Reward-Accuracy Decoupling}
62	\label{sec:decoupling}
63	
64	\input{tables/tab2_decoupling}
65	
66	\begin{figure}[t]
67	    \centering
68	    \includegraphics[width=\columnwidth]{figures/paper/fig_sft_grpo_scatter.pdf}
69	    \caption{SFT vs.\ GRPO accuracy across all pruning criteria and sparsity levels on GSM8K ($N{=}1{,}319$). Points near the $y{=}x$ line indicate reward-accuracy decoupling: despite 4.4$\times$ peak reward gaps (Figure~\ref{fig:training_dynamics}a), GRPO yields minimal accuracy change ($|\Delta| \leq 1$\,pp for all fine-grained methods at 20--25\%). \rasp{} points correspond to $\alpha{=}1.0$.}
70	    \label{fig:sft_grpo_scatter}
71	\end{figure}
72	
73	Despite the 4.4$\times$ peak reward gap, GRPO produces minimal accuracy change (Figure~\ref{fig:sft_grpo_scatter}): all fine-grained methods at 20\% sparsity differ by $|\Delta| < 1$\,pp (CKA-only $+$0.48, Standard $+$0.55, Random $-$0.53, \rasp{} at $\alpha{=}1.0$ $-$0.61\,pp; Table~\ref{tab:decoupling}).
74	We term this \emph{reward-accuracy decoupling} (observed at 20--25\% fine-grained MLP sparsity): reward trajectory reflects the model's capacity to learn from RL signal, not downstream accuracy.
75	At 20\% sparsity, the four fine-grained criteria show mean $|\Delta| {=} 0.54$\,pp (max $0.61$\,pp); across the full $\alpha$ dose-response spectrum, $|\Delta|$ remains below $1.14$\,pp.
76	
77	The degree of decoupling varies with sparsity: at 15\%, GRPO amplifies the CKA-only advantage (SFT gap 5.69\,pp $\to$ GRPO gap 7.20\,pp); at 20--25\%, $|\Delta| < 1$\,pp without exception across all four fine-grained criteria (Tables~\ref{tab:decoupling},~\ref{tab:cross_sparsity}; Appendix~\ref{sec:appendix_cross_sparsity}); dose-response $\alpha$ variations remain below $1.14$\,pp (Table~\ref{tab:alpha}; MATH-500 within noise, Appendix~\ref{sec:appendix_math500}).
78	
79	Two One-Sided Tests (TOST) equivalence testing ($\varepsilon{=}2$\,pp, chosen as ${\approx}4\times$ cross-seed $\sigma$; $N{=}1{,}319$ paired examples) confirms statistical equivalence for 7/8 comparisons ($p{<}0.05$; margin justification and per-pair results in Appendix~\ref{sec:appendix_tost}), robust across seeds (0.37\,pp range; Appendix~\ref{sec:appendix_multiseed}) and extended training (300 steps; \S\ref{sec:extended_analysis}).
80	The endpoints of the spectrum generalize beyond GSM8K: on MATH-500~\citep{hendrycks2021math}, CKA-only and Standard both rank above \rasp{} and Random in SFT accuracy (27.4\%, 25.6\% vs.\ 21.6\%, 16.6\%), though the CKA-only--Standard gap narrows (1.8\,pp vs.\ 4.62\,pp on GSM8K; Appendix~\ref{sec:appendix_math500}).
81	This compression is consistent with two factors: MATH-500's higher intrinsic difficulty---the unpruned model achieves only 53.0\% (vs.\ 90.83\% on GSM8K)---and generation-length truncation at the 2{,}048-token evaluation limit, which affects over half of dense-model responses (Appendix~\ref{sec:appendix_math500}).
82	On MBPP~\citep{austin2021mbpp} all fine-grained GRPO $|\Delta| < 2$\,pp, though not statistically significant at this sample size (Appendix~\ref{sec:appendix_mbpp}).
83	\label{sec:ood}
84	ShortGPT~\citep{shortgpt2024} depth pruning is the sole exception: its GRPO delta is task-dependent ($-$1.36\,pp on GSM8K, $+$4.01\,pp on MBPP; Tables~\ref{tab:decoupling},~\ref{tab:mbpp}), unlike fine-grained methods ($|\Delta| \leq 1.8$\,pp).
85	This asymmetry may reflect differing sensitivity to sequential depth: multi-step mathematical reasoning (GSM8K) relies on extended chain-of-thought computation across layers, which layer removal directly disrupts, whereas the function-level code generation tasks in MBPP depend more on local pattern matching and may benefit from reduced overthinking in shorter networks.
86	
87	
88	\subsection{Additional Results}
89	\label{sec:additional_results}
90	
91	\paragraph{Post-SFT accuracy does not predict GRPO outcome.}
92	\label{sec:sft_gradient}
93	Under SFT alone the ordering is CKA-only $>$ \rasp{} at $\alpha{=}1.0$ $>$ Standard $>$ Random, yet the recovery capacity spectrum (Table~\ref{tab:recovery_gradient}) reverses the \rasp{} at $\alpha{=}1.0$/Standard ordering---Standard exhibits higher peak reward than \rasp{} despite lower SFT accuracy, indicating that the spectrum tracks structural properties rather than post-SFT accuracy.
94	
95	\paragraph{Dose-response and sparsity limits.}
96	\label{sec:sparsity_cliff}
97	The CKA coefficient $\alpha$ continuously modulates recovery capacity: on GSM8K, recovery follows an inverted-U across $\alpha \in \{0.5, 1.0, 2.0, 3.0, 4.0\}$, peaking at $\alpha{=}2.0$ (66.11\%; Figure~\ref{fig:dose_response}, Table~\ref{tab:alpha}) with $|\Delta| \leq 1.14$\,pp; \rasp{} at $\alpha{=}1.0$ exhibits reward collapse while \rasp{} at $\alpha{=}4.0$ recovers to 62.77\% (Appendix~\ref{sec:appendix_alpha}).
98	The pattern generalizes to MATH-500 ($\alpha{=}1.0$ worst at 23.0\%; higher-$\alpha$ cluster at 27.2--27.6\%; Table~\ref{tab:math500}).
99	All methods collapse at 30\% sparsity (Appendix~\ref{sec:appendix_sparsity_cliff}); pruning reduces parameters by 19\% and memory by ${\sim}$28\% (Appendix~\ref{sec:appendix_inference}).
100	
101	
102	\subsection{Extended Analysis}
103	\label{sec:extended_analysis}
104	
105	\begin{figure}[t]
106	    \centering
107	    \includegraphics[width=\columnwidth]{figures/paper/fig4_cka_heatmap.pdf}
108	    \caption{Layer-wise CKA similarity between dense and pruned representations (28 layers). CKA-only diverges most from the dense model ($\mu{=}0.62$) yet achieves the highest recovery; Standard ($\mu{=}0.90$), Random ($\mu{=}0.92$), and \rasp{} at $\alpha{=}1.0$ ($\mu{=}0.88$) preserve dense fidelity but exhibit reward collapse under RL.}
109	    \label{fig:cka_heatmap}
110	\end{figure}
111	
112	\paragraph{Representational diversity.}
113	CKA similarity between dense and pruned representations (Figure~\ref{fig:cka_heatmap}) shows that CKA-only diverges most from the dense model ($\mu{=}0.62$), while Standard ($\mu{=}0.90$), Random ($\mu{=}0.92$), and \rasp{} at $\alpha{=}1.0$ ($\mu{=}0.88$) cluster near 1.0---preserving dense fidelity retains redundant representations at the expense of diversity.
114	CKA-only concentrates pruning in early layers (L0--9, 72.5\% of removed groups; Appendix~\ref{sec:appendix_overlap},~\ref{sec:appendix_depth_first}), yielding 2.89$\times$ mean gradient magnitude versus Standard (55/56 layer groups $p{<}0.05$; Appendix~\ref{sec:appendix_gradient}).
115	On MATH-500, CKA-only truncates only 22\% of completions (mean 655 tokens) versus Standard's 44\% (mean 1{,}128 tokens), yet achieves equal or higher accuracy (Table~\ref{tab:math500}).
116	
117	\begin{figure}[t]
118	    \centering
119	    \includegraphics[width=\columnwidth]{figures/paper/fig5_extended_training.pdf}
120	    \caption{Extended GRPO training (300 steps, 3$\times$ budget). (a)~Standard reward: zero net gain (0.054$\to$0.056); CKA-only sustains a 5.5$\times$ gap. (b)~Standard $f_0$ remains in the collapse zone ($>$0.5); CKA-only stays below 0.30.}
121	    \label{fig:extended_training}
122	\end{figure}
123	
124	\paragraph{Extended training does not resolve collapse.}
125	Extending GRPO from 100 to 300 steps (Figure~\ref{fig:extended_training}; Appendix~\ref{sec:appendix_extended}), Standard shows no net improvement (reward 0.054--0.058, $f_0 > 0.5$ throughout), while CKA-only sustains a 5.5$\times$ gap (0.308 vs 0.056 at step 300), suggesting the gap is structural rather than a matter of training budget.
126	
127	\paragraph{Cross-scale and cross-model generalization.}
128	Preliminary evidence at 1.5B scale (Table~\ref{tab:cross_scale}; Appendix~\ref{sec:appendix_cross_scale}) preserves the three-method ordering.
129	On Qwen2.5-Math-7B, a different model within the Qwen2.5 family (Appendix~\ref{sec:appendix_cross_arch}), CKA-only recovers from 1.0\% post-prune to 51.50\% vs.\ Standard's 21.00\%.
130	
131	
132	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4f97e83-5d17-482e-a046-301a97b00c80",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "2417c1da-d5ba-4789-ae07-24eae854181f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex",
      "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\begin{figure*}[t]\n    \\centering\n    \\begin{minipage}[t]{0.38\\textwidth}\n        \\centering\n        \\includegraphics[width=\\textwidth]{figures/paper/fig2_reward_trajectories.pdf}\n        \\centerline{\\small (a) Reward trajectories}\n    \\end{minipage}\n    \\hfill\n    \\begin{minipage}[t]{0.58\\textwidth}\n        \\centering\n        \\includegraphics[width=\\textwidth]{figures/paper/fig3_collapse_dynamics.pdf}\n        \\centerline{\\small (b) $f_0$ and gradient norm diagnostics}\n    \\end{minipage}\n    \\caption{GRPO training dynamics for four pruning criteria (100 steps, $\\beta{=}0.01$, $T{=}0.4$). (a)~Reward trajectories: CKA-only reaches 0.354 peak; Random oscillates (0.14--0.19); Standard peaks at 0.081; \\rasp{} at $\\alpha{=}1.0$ declines to 0.010. (b)~Left: $f_0$ (zero-variance batch fraction); CKA-only remains below 0.35 while Standard and \\rasp{} at $\\alpha{=}1.0$ persist in the collapse zone ($f_0 > 0.5$). Right: gradient norm; \\rasp{} at $\\alpha{=}1.0$ exhibits near-zero norms throughout; Standard shows a transient minimum at step 90.}\n    \\label{fig:training_dynamics}\n\\end{figure*}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\input{tables/tab1_recovery_gradient}\n\n\\paragraph{Base model and evaluation.}\nWe evaluate on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\\citep{qwen2.5} with GQA~\\citep{ainslie2023gqa} (Section~\\ref{sec:prelim}).\nOur primary benchmark is GSM8K~\\citep{cobbe2021gsm8k} ($N{=}1{,}319$ grade-school math problems; exact-match accuracy).\nThe unpruned model achieves 90.83\\% (greedy decoding).\n\n\\paragraph{Pruning methods.}\nWe compare four pruning criteria at 20\\% structured sparsity, all removing the same number of MLP channel groups (200 of 784 across 28 layers, ${\\sim}$1.45B parameters) with identical per-layer capacity floors (${\\ge}$40\\% retention per layer):\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{CKA-only}: structures ranked by functional overlap $F(h)$ alone (Eq.~\\ref{eq:overlap}); the most redundant groups are removed regardless of gradient importance.\n    \\item \\textbf{Random}: uniform random selection among eligible groups.  Uses TRL's default 512-token generation limit (vs.\\ 1{,}024 for other methods), which may disadvantage its reward trajectory; we retain it as a conservative lower bound rather than a direct comparison point.\n    \\item \\textbf{Standard}: Taylor-expansion importance $I(h)$ alone (Eq.~\\ref{eq:importance}); the least important groups are removed, following LLM-Pruner~\\citep{llmpruner2023}.\n    \\item \\textbf{\\rasp{}} ($\\alpha{=}1.0$): the composite score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ (Eq.~\\ref{eq:score}), removing structures that are both low-importance and functionally redundant.\n\\end{enumerate}\n\n\\paragraph{Recovery pipeline and hardware.}\nImmediately after pruning (before any recovery), all four methods produce near-zero GSM8K accuracy ($<$2\\%), as the pruned models fail to generate coherent reasoning chains or proper termination tokens.\nAll four methods then undergo matched two-stage recovery (Section~\\ref{sec:recovery}): SFT warmup (2 epochs, 7{,}473 GSM8K examples, 37 min) followed by GRPO (lr $1{\\times}10^{-6}$, $\\beta{=}0.01$, $T{=}0.4$, 100 steps on 1{,}000 problems; full hyperparameters in Table~\\ref{tab:hyperparams}, Appendix~\\ref{sec:appendix_training}).\nAll methods use \\texttt{max\\_completion\\_length}{$=$}1{,}024 except Random (TRL default 512), making it a conservative comparison point.\nWe repeat GRPO with 3 seeds for CKA-only, Standard, and Random (\\rasp{} at $\\alpha{=}1.0$ uses a single seed); CKA-only achieves 64.39\\% $\\pm$ 0.19\\,pp, Standard 59.84\\% $\\pm$ 0.38\\,pp (Welch's $t$, $p{=}0.0009$, $d{=}11.1$; Appendix~\\ref{sec:appendix_seed}).\nThe ``Unpruned'' baseline in Table~\\ref{tab:decoupling} uses the same SFT-warmup checkpoint; the 9.56\\,pp gap from the pre-warmup 90.83\\% reflects warmup on a reduced training set, not pruning loss.\nAll experiments run on 2$\\times$ NVIDIA RTX PRO 6000 GPUs (94\\,GB VRAM each).\n\n\n\\subsection{Recovery Capacity Spectrum}\n\\label{sec:recovery_gradient}\n\nUnder GRPO training, the four pruning criteria produce a clear recovery capacity spectrum: CKA-only $\\gg$ Random $\\gg$ Standard $>$ \\rasp{} at $\\alpha{=}1.0$ (Table~\\ref{tab:recovery_gradient}, Figure~\\ref{fig:training_dynamics}).\nThe pruning criterion, rather than training configuration, determines whether the model learns, stagnates, or exhibits reward collapse.\n\nAmong these configurations, only the diversity-maximizing criterion (CKA-only) sustains active learning: peak reward 0.354 with $f_0$ as low as 0.125 (Figure~\\ref{fig:training_dynamics}b).\nRandom, under a shorter generation limit, stagnates (reward 0.14--0.19, min $f_0 = 0.300$); Standard exhibits borderline collapse ($f_0 \\geq 0.50$, peak reward 0.081); \\rasp{} at $\\alpha{=}1.0$ exhibits complete reward collapse ($f_0 \\geq 0.675$, reward declining to 0.010, with near-zero KL divergence indicating minimal policy movement; Appendix~\\ref{sec:appendix_kl}).\nThe dose-response analysis (\\S\\ref{sec:sparsity_cliff}) confirms CKA weighting as the critical variable: increasing $\\alpha$ from 1.0 to 2.0 shifts \\rasp{} from reward collapse to peak recovery (66.11\\% vs.\\ 64.39\\% for CKA-only on GSM8K).\n\n\n\\subsection{Reward-Accuracy Decoupling}\n\\label{sec:decoupling}\n\n\\input{tables/tab2_decoupling}\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=\\columnwidth]{figures/paper/fig_sft_grpo_scatter.pdf}\n    \\caption{SFT vs.\\ GRPO accuracy across all pruning criteria and sparsity levels on GSM8K ($N{=}1{,}319$). Points near the $y{=}x$ line indicate reward-accuracy decoupling: despite 4.4$\\times$ peak reward gaps (Figure~\\ref{fig:training_dynamics}a), GRPO yields minimal accuracy change ($|\\Delta| \\leq 1$\\,pp for all fine-grained methods at 20--25\\%). \\rasp{} points correspond to $\\alpha{=}1.0$.}\n    \\label{fig:sft_grpo_scatter}\n\\end{figure}\n\nDespite the 4.4$\\times$ peak reward gap, GRPO produces minimal accuracy change (Figure~\\ref{fig:sft_grpo_scatter}): all fine-grained methods at 20\\% sparsity differ by $|\\Delta| < 1$\\,pp (CKA-only $+$0.48, Standard $+$0.55, Random $-$0.53, \\rasp{} at $\\alpha{=}1.0$ $-$0.61\\,pp; Table~\\ref{tab:decoupling}).\nWe term this \\emph{reward-accuracy decoupling} (observed at 20--25\\% fine-grained MLP sparsity): reward trajectory reflects the model's capacity to learn from RL signal, not downstream accuracy.\nAt 20\\% sparsity, the four fine-grained criteria show mean $|\\Delta| {=} 0.54$\\,pp (max $0.61$\\,pp); across the full $\\alpha$ dose-response spectrum, $|\\Delta|$ remains below $1.14$\\,pp.\n\nThe degree of decoupling varies with sparsity: at 15\\%, GRPO amplifies the CKA-only advantage (SFT gap 5.69\\,pp $\\to$ GRPO gap 7.20\\,pp); at 20--25\\%, $|\\Delta| < 1$\\,pp without exception across all four fine-grained criteria (Tables~\\ref{tab:decoupling},~\\ref{tab:cross_sparsity}; Appendix~\\ref{sec:appendix_cross_sparsity}); dose-response $\\alpha$ variations remain below $1.14$\\,pp (Table~\\ref{tab:alpha}; MATH-500 within noise, Appendix~\\ref{sec:appendix_math500}).\n\nTwo One-Sided Tests (TOST) equivalence testing ($\\varepsilon{=}2$\\,pp, chosen as ${\\approx}4\\times$ cross-seed $\\sigma$; $N{=}1{,}319$ paired examples) confirms statistical equivalence for 7/8 comparisons ($p{<}0.05$; margin justification and per-pair results in Appendix~\\ref{sec:appendix_tost}), robust across seeds (0.37\\,pp range; Appendix~\\ref{sec:appendix_multiseed}) and extended training (300 steps; \\S\\ref{sec:extended_analysis}).\nThe endpoints of the spectrum generalize beyond GSM8K: on MATH-500~\\citep{hendrycks2021math}, CKA-only and Standard both rank above \\rasp{} and Random in SFT accuracy (27.4\\%, 25.6\\% vs.\\ 21.6\\%, 16.6\\%), though the CKA-only--Standard gap narrows (1.8\\,pp vs.\\ 4.62\\,pp on GSM8K; Appendix~\\ref{sec:appendix_math500}).\nThis compression is consistent with two factors: MATH-500's higher intrinsic difficulty---the unpruned model achieves only 53.0\\% (vs.\\ 90.83\\% on GSM8K)---and generation-length truncation at the 2{,}048-token evaluation limit, which affects over half of dense-model responses (Appendix~\\ref{sec:appendix_math500}).\nOn MBPP~\\citep{austin2021mbpp} all fine-grained GRPO $|\\Delta| < 2$\\,pp, though not statistically significant at this sample size (Appendix~\\ref{sec:appendix_mbpp}).\n\\label{sec:ood}\nShortGPT~\\citep{shortgpt2024} depth pruning is the sole exception: its GRPO delta is task-dependent ($-$1.36\\,pp on GSM8K, $+$4.01\\,pp on MBPP; Tables~\\ref{tab:decoupling},~\\ref{tab:mbpp}), unlike fine-grained methods ($|\\Delta| \\leq 1.8$\\,pp).\nThis asymmetry may reflect differing sensitivity to sequential depth: multi-step mathematical reasoning (GSM8K) relies on extended chain-of-thought computation across layers, which layer removal directly disrupts, whereas the function-level code generation tasks in MBPP depend more on local pattern matching and may benefit from reduced overthinking in shorter networks.\n\n\n\\subsection{Additional Results}\n\\label{sec:additional_results}\n\n\\paragraph{Post-SFT accuracy does not predict GRPO outcome.}\n\\label{sec:sft_gradient}\nUnder SFT alone the ordering is CKA-only $>$ \\rasp{} at $\\alpha{=}1.0$ $>$ Standard $>$ Random, yet the recovery capacity spectrum (Table~\\ref{tab:recovery_gradient}) reverses the \\rasp{} at $\\alpha{=}1.0$/Standard ordering---Standard exhibits higher peak reward than \\rasp{} despite lower SFT accuracy, indicating that the spectrum tracks structural properties rather than post-SFT accuracy.\n\n\\paragraph{Dose-response and sparsity limits.}\n\\label{sec:sparsity_cliff}\nThe CKA coefficient $\\alpha$ continuously modulates recovery capacity: on GSM8K, recovery follows an inverted-U across $\\alpha \\in \\{0.5, 1.0, 2.0, 3.0, 4.0\\}$, peaking at $\\alpha{=}2.0$ (66.11\\%; Figure~\\ref{fig:dose_response}, Table~\\ref{tab:alpha}) with $|\\Delta| \\leq 1.14$\\,pp; \\rasp{} at $\\alpha{=}1.0$ exhibits reward collapse while \\rasp{} at $\\alpha{=}4.0$ recovers to 62.77\\% (Appendix~\\ref{sec:appendix_alpha}).\nThe pattern generalizes to MATH-500 ($\\alpha{=}1.0$ worst at 23.0\\%; higher-$\\alpha$ cluster at 27.2--27.6\\%; Table~\\ref{tab:math500}).\nAll methods collapse at 30\\% sparsity (Appendix~\\ref{sec:appendix_sparsity_cliff}); pruning reduces parameters by 19\\% and memory by ${\\sim}$28\\% (Appendix~\\ref{sec:appendix_inference}).\n\n\n\\subsection{Extended Analysis}\n\\label{sec:extended_analysis}\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=\\columnwidth]{figures/paper/fig4_cka_heatmap.pdf}\n    \\caption{Layer-wise CKA similarity between dense and pruned representations (28 layers). CKA-only diverges most from the dense model ($\\mu{=}0.62$) yet achieves the highest recovery; Standard ($\\mu{=}0.90$), Random ($\\mu{=}0.92$), and \\rasp{} at $\\alpha{=}1.0$ ($\\mu{=}0.88$) preserve dense fidelity but exhibit reward collapse under RL.}\n    \\label{fig:cka_heatmap}\n\\end{figure}\n\n\\paragraph{Representational diversity.}\nCKA similarity between dense and pruned representations (Figure~\\ref{fig:cka_heatmap}) shows that CKA-only diverges most from the dense model ($\\mu{=}0.62$), while Standard ($\\mu{=}0.90$), Random ($\\mu{=}0.92$), and \\rasp{} at $\\alpha{=}1.0$ ($\\mu{=}0.88$) cluster near 1.0---preserving dense fidelity retains redundant representations at the expense of diversity.\nCKA-only concentrates pruning in early layers (L0--9, 72.5\\% of removed groups; Appendix~\\ref{sec:appendix_overlap},~\\ref{sec:appendix_depth_first}), yielding 2.89$\\times$ mean gradient magnitude versus Standard (55/56 layer groups $p{<}0.05$; Appendix~\\ref{sec:appendix_gradient}).\nOn MATH-500, CKA-only truncates only 22\\% of completions (mean 655 tokens) versus Standard's 44\\% (mean 1{,}128 tokens), yet achieves equal or higher accuracy (Table~\\ref{tab:math500}).\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=\\columnwidth]{figures/paper/fig5_extended_training.pdf}\n    \\caption{Extended GRPO training (300 steps, 3$\\times$ budget). (a)~Standard reward: zero net gain (0.054$\\to$0.056); CKA-only sustains a 5.5$\\times$ gap. (b)~Standard $f_0$ remains in the collapse zone ($>$0.5); CKA-only stays below 0.30.}\n    \\label{fig:extended_training}\n\\end{figure}\n\n\\paragraph{Extended training does not resolve collapse.}\nExtending GRPO from 100 to 300 steps (Figure~\\ref{fig:extended_training}; Appendix~\\ref{sec:appendix_extended}), Standard shows no net improvement (reward 0.054--0.058, $f_0 > 0.5$ throughout), while CKA-only sustains a 5.5$\\times$ gap (0.308 vs 0.056 at step 300), suggesting the gap is structural rather than a matter of training budget.\n\n\\paragraph{Cross-scale and cross-model generalization.}\nPreliminary evidence at 1.5B scale (Table~\\ref{tab:cross_scale}; Appendix~\\ref{sec:appendix_cross_scale}) preserves the three-method ordering.\nOn Qwen2.5-Math-7B, a different model within the Qwen2.5 family (Appendix~\\ref{sec:appendix_cross_arch}), CKA-only recovers from 1.0\\% post-prune to 51.50\\% vs.\\ Standard's 21.00\\%.\n\n\n",
      "numLines": 132,
      "startLine": 1,
      "totalLines": 132
    }
  },
  "sourceToolAssistantUUID": "e4f97e83-5d17-482e-a046-301a97b00c80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-25T09:07:38.918Z_

<details open><summary>🔧 Tool call — Read · `toolu_015WwH954BJ4Pc4CLAYyCwSe`</summary>

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
  "parentUuid": "2417c1da-d5ba-4789-ae07-24eae854181f",
  "isSidechain": false,
  "requestId": "req_011CbP2Hf1t7i6JT7iNF7KWc",
  "type": "assistant",
  "uuid": "06c289b2-a08c-4d0c-8d75-b40a46a2834a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBhgTD9Gn7USQxSLgKGD5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12668,
      "cache_read_input_tokens": 38802,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 38802,
          "cache_creation_input_tokens": 12668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12668
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-25T09:07:38.922Z_

<details><summary>↩ Tool result · `toolu_015WwH954BJ4Pc4CLAYyCwSe`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:conclusion}
3	
4	Whether RLVR outperforms SFT for recovering pruned reasoning models appears to depend on how the model was pruned.
5	Under diversity-preserving pruning at 20--25\% MLP sparsity on Qwen2.5-family models, the two paradigms produce near-identical accuracy (mean $|\Delta| {=} 0.54$\,pp; max $1.8$\,pp), yet the pruning criterion creates a 4.4$\times$ peak reward gap.
6	SFT warmup recovers the bulk of accuracy (from $<$2\% post-prune to 51--64\%); GRPO exposes structural capacity differences but contributes minimal additional accuracy, a pattern that persists at 300 steps (Appendix~\ref{sec:appendix_extended}).
7	The non-monotonic $\alpha$ dose-response argues against a layer-distribution confound.
8	
9	\paragraph{GRPO as diagnostic probe.}
10	The decoupling pattern suggests that GRPO may serve as a \emph{diagnostic probe} for pruning quality at moderate sparsity: reward trajectories appear to indicate whether the pruned architecture retains sufficient diversity for RL exploration---information not accessible through SFT, which converges to similar accuracy at 20--25\% MLP sparsity.
11	At 15\% sparsity, GRPO amplifies the CKA-guided advantage ($+$1.51\,pp), suggesting the transition boundary warrants future investigation.
12	
13	\paragraph{Implications.}
14	For deployment pipelines that include post-pruning RL, diversity-preserving criteria (CKA-only or high-$\alpha$ \rasp{}) should be preferred.
15	Our findings complement \citet{selfhealing2025}: while they demonstrate RLVR superiority for unstructured magnitude pruning at 96.5\% retention, within our experimental scope (20--25\% structured MLP sparsity on Qwen2.5-family models), this hierarchy dissolves under diversity-preserving pruning---the gap appears attributable to the pruning criterion rather than a fundamental property of RL recovery.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06c289b2-a08c-4d0c-8d75-b40a46a2834a",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "f6cdeee4-62ac-4c12-8d76-9c5630556d25",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:conclusion}\n\nWhether RLVR outperforms SFT for recovering pruned reasoning models appears to depend on how the model was pruned.\nUnder diversity-preserving pruning at 20--25\\% MLP sparsity on Qwen2.5-family models, the two paradigms produce near-identical accuracy (mean $|\\Delta| {=} 0.54$\\,pp; max $1.8$\\,pp), yet the pruning criterion creates a 4.4$\\times$ peak reward gap.\nSFT warmup recovers the bulk of accuracy (from $<$2\\% post-prune to 51--64\\%); GRPO exposes structural capacity differences but contributes minimal additional accuracy, a pattern that persists at 300 steps (Appendix~\\ref{sec:appendix_extended}).\nThe non-monotonic $\\alpha$ dose-response argues against a layer-distribution confound.\n\n\\paragraph{GRPO as diagnostic probe.}\nThe decoupling pattern suggests that GRPO may serve as a \\emph{diagnostic probe} for pruning quality at moderate sparsity: reward trajectories appear to indicate whether the pruned architecture retains sufficient diversity for RL exploration---information not accessible through SFT, which converges to similar accuracy at 20--25\\% MLP sparsity.\nAt 15\\% sparsity, GRPO amplifies the CKA-guided advantage ($+$1.51\\,pp), suggesting the transition boundary warrants future investigation.\n\n\\paragraph{Implications.}\nFor deployment pipelines that include post-pruning RL, diversity-preserving criteria (CKA-only or high-$\\alpha$ \\rasp{}) should be preferred.\nOur findings complement \\citet{selfhealing2025}: while they demonstrate RLVR superiority for unstructured magnitude pruning at 96.5\\% retention, within our experimental scope (20--25\\% structured MLP sparsity on Qwen2.5-family models), this hierarchy dissolves under diversity-preserving pruning---the gap appears attributable to the pruning criterion rather than a fundamental property of RL recovery.\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  },
  "sourceToolAssistantUUID": "06c289b2-a08c-4d0c-8d75-b40a46a2834a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-25T09:07:39.384Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NCyTZPRhh5gQby7c2WkZkG`</summary>

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
  "parentUuid": "f6cdeee4-62ac-4c12-8d76-9c5630556d25",
  "isSidechain": false,
  "requestId": "req_011CbP2Hf1t7i6JT7iNF7KWc",
  "type": "assistant",
  "uuid": "9912d8ad-69be-4590-8521-07937f66f766",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBhgTD9Gn7USQxSLgKGD5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12668,
      "cache_read_input_tokens": 38802,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 38802,
          "cache_creation_input_tokens": 12668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12668
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-25T09:07:39.388Z_

<details><summary>↩ Tool result · `toolu_01NCyTZPRhh5gQby7c2WkZkG`</summary>

```text
1	% Limitations --- required by ACL/EMNLP
2	
3	\paragraph{Architecture and scale.}
4	Our primary results are on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} with GQA ($G{=}7$).
5	Cross-model validation on Qwen2.5-Math-7B covers SFT recovery only ($N{=}200$); both models share the Qwen2.5 base architecture, so our cross-model evidence does not extend to different architecture families (e.g., LLaMA, Mistral).
6	Whether the spectrum generalizes across architecture families and scales (1B--70B) remains open.
7	
8	\paragraph{Diagnostic limitations.}
9	Reward-accuracy decoupling at 20--25\% sparsity means that recovery capacity, operationalized as peak reward, does not predict downstream accuracy improvements within our training horizon.
10	Recovery capacity captures the model's ability to sustain RL training without collapse, but practitioners seeking accuracy gains may require longer training, different reward formulations, or lower sparsity levels.
11	The per-layer capacity floor (40\% retention) was chosen heuristically; an ablation over $\tau \in \{0.3, 0.4, 0.5, 0.6\}$ (Appendix~\ref{sec:appendix_floor}) suggests moderate sensitivity, but a full search over continuous $\tau$ values was not performed.
12	
13	\paragraph{Inference efficiency.}
14	At 20\% sparsity, pruning reduces memory by ${\sim}$28\% and improves time-to-first-token, but inference throughput decreases by 19\% (72.0$\to$58.3 tok/s), likely because channel-group pruning creates irregular sparse patterns that current hardware cannot accelerate.
15	
16	\paragraph{Replication and scope.}
17	CKA-only, Standard, and Random are validated over 3 GRPO seeds; \rasp{} at $\alpha{=}1.0$ uses a single seed ($N{=}1$).
18	Random uses a 512-token generation limit (vs.\ 1{,}024 for other methods), preventing strict reward comparisons; its ranking should be interpreted as a conservative bound.
19	We evaluate on three benchmarks (GSM8K, MATH-500, MBPP) covering math reasoning and code generation; logical, commonsense, and multi-modal reasoning are not addressed.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9912d8ad-69be-4590-8521-07937f66f766",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "4d1db209-1e4c-4cb2-bcd8-b130567ed813",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex",
      "content": "% Limitations --- required by ACL/EMNLP\n\n\\paragraph{Architecture and scale.}\nOur primary results are on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} with GQA ($G{=}7$).\nCross-model validation on Qwen2.5-Math-7B covers SFT recovery only ($N{=}200$); both models share the Qwen2.5 base architecture, so our cross-model evidence does not extend to different architecture families (e.g., LLaMA, Mistral).\nWhether the spectrum generalizes across architecture families and scales (1B--70B) remains open.\n\n\\paragraph{Diagnostic limitations.}\nReward-accuracy decoupling at 20--25\\% sparsity means that recovery capacity, operationalized as peak reward, does not predict downstream accuracy improvements within our training horizon.\nRecovery capacity captures the model's ability to sustain RL training without collapse, but practitioners seeking accuracy gains may require longer training, different reward formulations, or lower sparsity levels.\nThe per-layer capacity floor (40\\% retention) was chosen heuristically; an ablation over $\\tau \\in \\{0.3, 0.4, 0.5, 0.6\\}$ (Appendix~\\ref{sec:appendix_floor}) suggests moderate sensitivity, but a full search over continuous $\\tau$ values was not performed.\n\n\\paragraph{Inference efficiency.}\nAt 20\\% sparsity, pruning reduces memory by ${\\sim}$28\\% and improves time-to-first-token, but inference throughput decreases by 19\\% (72.0$\\to$58.3 tok/s), likely because channel-group pruning creates irregular sparse patterns that current hardware cannot accelerate.\n\n\\paragraph{Replication and scope.}\nCKA-only, Standard, and Random are validated over 3 GRPO seeds; \\rasp{} at $\\alpha{=}1.0$ uses a single seed ($N{=}1$).\nRandom uses a 512-token generation limit (vs.\\ 1{,}024 for other methods), preventing strict reward comparisons; its ranking should be interpreted as a conservative bound.\nWe evaluate on three benchmarks (GSM8K, MATH-500, MBPP) covering math reasoning and code generation; logical, commonsense, and multi-modal reasoning are not addressed.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  },
  "sourceToolAssistantUUID": "9912d8ad-69be-4590-8521-07937f66f766",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-25T09:07:39.855Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E4zL2Qnkhr97N8qgw85PXJ`</summary>

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
  "parentUuid": "4d1db209-1e4c-4cb2-bcd8-b130567ed813",
  "isSidechain": false,
  "requestId": "req_011CbP2Hf1t7i6JT7iNF7KWc",
  "type": "assistant",
  "uuid": "84f6a149-db8a-475a-8434-91d9dd9357ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBhgTD9Gn7USQxSLgKGD5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12668,
      "cache_read_input_tokens": 38802,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 38802,
          "cache_creation_input_tokens": 12668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12668
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-25T09:07:39.860Z_

<details><summary>↩ Tool result · `toolu_01E4zL2Qnkhr97N8qgw85PXJ`</summary>

```text
1	This work uses publicly available models (DeepSeek-R1-Distill-Qwen, Qwen2.5-Math) and established benchmarks (GSM8K, MATH-500, MBPP); no private data or human subjects are involved.
2	Structured pruning reduces model size and inference memory, which can lower the computational cost and energy consumption of deploying large language models.
3	Our research focuses on the technical analysis of pruning criteria and their interaction with reinforcement learning recovery; we do not foresee direct negative societal impacts from this work.
4	All models and datasets used in this work are publicly available under permissive licenses: DeepSeek-R1-Distill-Qwen (MIT), Qwen2.5-Math (Apache 2.0), GSM8K (MIT), MATH (MIT), and MBPP (CC-BY-4.0).
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84f6a149-db8a-475a-8434-91d9dd9357ee",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "774670ea-b68d-4c3a-b53e-f30816eff13b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/ethics.tex",
      "content": "This work uses publicly available models (DeepSeek-R1-Distill-Qwen, Qwen2.5-Math) and established benchmarks (GSM8K, MATH-500, MBPP); no private data or human subjects are involved.\nStructured pruning reduces model size and inference memory, which can lower the computational cost and energy consumption of deploying large language models.\nOur research focuses on the technical analysis of pruning criteria and their interaction with reinforcement learning recovery; we do not foresee direct negative societal impacts from this work.\nAll models and datasets used in this work are publicly available under permissive licenses: DeepSeek-R1-Distill-Qwen (MIT), Qwen2.5-Math (Apache 2.0), GSM8K (MIT), MATH (MIT), and MBPP (CC-BY-4.0).\n",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 5
    }
  },
  "sourceToolAssistantUUID": "84f6a149-db8a-475a-8434-91d9dd9357ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-25T09:07:40.326Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QR9jGBRDLmtLkYR5iDqpR9`</summary>

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
  "parentUuid": "774670ea-b68d-4c3a-b53e-f30816eff13b",
  "isSidechain": false,
  "requestId": "req_011CbP2Hf1t7i6JT7iNF7KWc",
  "type": "assistant",
  "uuid": "612d9cc2-6fc0-44ff-8b2a-059d2da19e62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBhgTD9Gn7USQxSLgKGD5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12668,
      "cache_read_input_tokens": 38802,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 38802,
          "cache_creation_input_tokens": 12668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12668
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-25T09:07:40.331Z_

<details><summary>↩ Tool result · `toolu_01QR9jGBRDLmtLkYR5iDqpR9`</summary>

```text
1	\section{Training Details}
2	\label{sec:appendix_training}
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\caption{Hyperparameter details for SFT warmup and GRPO recovery stages. All methods share the same GRPO configuration; Random uses the TRL default generation limit (marked with $^\dagger$).}
8	\label{tab:hyperparams}
9	\resizebox{\columnwidth}{!}{%
10	\begin{tabular}{@{}lll@{}}
11	\toprule
12	Parameter & SFT & GRPO \\
13	\midrule
14	Learning rate & $2 \times 10^{-5}$ & $1 \times 10^{-6}$ \\
15	Batch size & 1 & 1 \\
16	Gradient accumulation & 8 & 1 \\
17	Max sequence length & 2{,}048 & -- \\
18	Max new tokens & -- & 1{,}024\,$^\dagger$512 \\
19	Optimizer & AdamW & AdamW \\
20	Epochs / Steps & 2 epochs & 100 steps \\
21	KL coefficient $\beta$ & -- & 0.01 \\
22	Sampling temperature & -- & 0.4 \\
23	Num generations per prompt & -- & 8 \\
24	Reward & -- & Binary (exact match) \\
25	Loss formulation & Cross-entropy & DAPO-style clipped \\
26	\texttt{reward\_desert\_patience} & -- & 50 \\
27	\bottomrule
28	\multicolumn{3}{l}{\footnotesize $^\dagger$Random uses TRL default of 512 tokens; all other methods use 1{,}024.} \\
29	\end{tabular}}
30	\end{table}
31	
32	\section{Algorithm}
33	\label{sec:appendix_algo}
34	
35	\begin{algorithm}[h]
36	\caption{Controlled Pruning Comparison Framework}
37	\label{alg:rasp}
38	\begin{algorithmic}[1]
39	\Require Model $\mathcal{M}$, calibration data $\mathcal{D}_\text{cal}$, target sparsity $s$, scoring criterion $\mathcal{C} \in \{\text{Std}, \text{RASP}, \text{CKA}, \text{Rand}\}$, layer floor $\tau$
40	\Ensure Pruned and recovered model $\mathcal{M}'$
41	\Statex \textit{\% Stage 1: Shared Structural Analysis}
42	\For{each structure $h \in \mathcal{H}$}
43	    \State Compute importance $I(h)$ via Eq.~\eqref{eq:importance}
44	    \State Collect activations $\mathbf{X}_h$ on $\mathcal{D}_\text{cal}$
45	\EndFor
46	\For{each layer $\ell = 1, \ldots, L$}
47	    \For{each structure $h_i$ in layer $\ell$}
48	        \State $F(h_i) \gets \frac{1}{|\mathcal{H}_\ell|-1} \sum_{j \neq i} \text{CKA}(\mathbf{X}_{h_i}, \mathbf{X}_{h_j})$
49	    \EndFor
50	\EndFor
51	\Statex \textit{\% Stage 2: Criterion-Specific Scoring}
52	\For{each structure $h \in \mathcal{H}$}
53	    \State $S(h) \gets \mathcal{C}(I(h), F(h))$ \hfill $\triangleright$ Eq.~\ref{eq:standard}, \ref{eq:score}, \ref{eq:cka_only}, or random
54	\EndFor
55	\State Sort $\mathcal{H}$ by $S(h)$ ascending; prune lowest up to $s$, subject to $\tau$
56	\Statex \textit{\% Stage 3: Two-Stage Recovery}
57	\State $\mathcal{M}_\text{warm} \gets \text{SFT}(\mathcal{M}_\text{pruned}, \mathcal{D}_\text{sft})$ \hfill $\triangleright$ restore EOS \& format
58	\State $\mathcal{M}' \gets \text{GRPO}(\mathcal{M}_\text{warm}, \mathcal{D}_\text{rlvr})$ \hfill $\triangleright$ recover reasoning
59	\State \Return $\mathcal{M}'$
60	\end{algorithmic}
61	\end{algorithm}
62	
63	\section{Inference Efficiency}
64	\label{sec:appendix_inference}
65	
66	\begin{table}[h]
67	\centering
68	\small
69	\caption{Inference characteristics at 20\% sparsity (single-GPU, no contention). Pruning reduces parameters by 19\% and memory by ${\sim}$28\%, with TTFT improving 18\%. Per-token throughput decreases 19\% (0.81$\times$) due to non-uniform layer widths from full-layer removal that current GPU kernels do not optimize.}
70	\label{tab:inference}
71	\resizebox{\columnwidth}{!}{%
72	\begin{tabular}{@{}lcccc@{}}
73	\toprule
74	Configuration & TPS\,(tok/s) & TTFT\,(ms) & Per-token\,(ms) & Params\,(B) \\
75	\midrule
76	Dense 7B & 72.0 & 20.1 & 13.9 & 7.62 \\
77	CKA-only 20\% & 58.3 & 16.4 & 16.7 & 6.16 \\
78	Standard 20\% & 58.2 & 16.4 & 16.7 & 6.16 \\
79	\bottomrule
80	\end{tabular}}
81	\end{table}
82	
83	All pruned models achieve ${\sim}$28\% memory reduction from structural parameter removal.
84	TTFT (time to first token) improves by 18\% (20.1$\to$16.4\,ms), reflecting faster prefill with fewer parameters.
85	Per-token throughput decreases by 19\% (72.0$\to$58.3 tok/s, or 13.9$\to$16.7\,ms per token), consistent with non-uniform layer widths creating computational bottlenecks that current GPU kernels do not optimize away.
86	CKA-only and Standard show identical throughput (58.3 vs 58.2 tok/s), confirming that the pruning criterion affects recovery capacity but not inference speed at matched sparsity.
87	
88	\section{CKA Coefficient $\alpha$ Ablation}
89	\label{sec:appendix_alpha}
90	
91	\input{tables/table3_alpha}
92	
93	On GSM8K, the dose-response curve across $\alpha \in \{0.5, 1.0, 2.0, 3.0, 4.0\}$ reveals an inverted-U pattern peaking at $\alpha{=}2.0$ (SFT 64.97\%, GRPO 66.11\%, $\Delta{=}{+}1.14$\,pp; Table~\ref{tab:alpha}).
94	At $\alpha{=}0.5$, importance still dominates; recovery is low (SFT 60.73\%, GRPO 61.18\%).
95	At $\alpha{=}1.0$ (\rasp{}), GRPO collapses (peak reward 0.061, accuracy 60.88\%, $\Delta{=}{-}0.61$\,pp).
96	$\alpha{=}3.0$ (SFT 64.14\%, GRPO 63.46\%, $\Delta{=}{-}0.68$\,pp) excludes a plateau hypothesis: accuracy drops 2.65\,pp from the $\alpha{=}2.0$ peak, confirming that the optimum is a true peak rather than a saturation regime.
97	At $\alpha{=}4.0$, CKA overlap dominates; the model recovers to 62.77\% GRPO accuracy (SFT 61.94\%, $\Delta{=}{+}0.83$\,pp) with active GRPO learning (reward 0.146$\to$0.256$\to$0.198).
98	Reward-accuracy decoupling holds at every $\alpha$ value: $|\Delta| \leq 1.14$\,pp across all five points.
99	
100	\section{Extended Training Dynamics}
101	\label{sec:appendix_extended}
102	
103	See Figure~\ref{fig:extended_training} in the main text for the 300-step extended training results.
104	At 300 steps, GSM8K accuracy: CKA-only 64.37\% (identical to 100-step seed 42), Standard 59.29\% (within 100-step seed variance of $\pm$0.38\,pp).
105	The unchanged accuracy despite rising CKA-only reward (0.308 at step 300 vs.\ 0.354 peak at step 100) directly demonstrates reward-accuracy decoupling at this training horizon.
106	
107	\section{MATH-500 Out-of-Distribution Evaluation}
108	\label{sec:appendix_math500}
109	
110	\input{tables/tab_math500}
111	
112	CKA-only and Standard both outperform \rasp{} and Random on MATH-500 (SFT: 27.4\%, 25.6\% vs.\ 21.6\%, 16.6\%; GRPO: 27.6\%, 27.0\% vs.\ 23.0\%, 15.0\%), consistent with GSM8K.
113	However, the CKA-only--Standard gap narrows substantially: from 4.6\,pp (GSM8K SFT) to 1.8\,pp (MATH-500 SFT) to 0.6\,pp (MATH-500 GRPO).
114	Middle-ranked methods also swap positions (Standard $>$ \rasp{} on MATH-500 vs.\ \rasp{} $>$ Standard on GSM8K).
115	This narrowing reflects two compounding factors: MATH-500's higher intrinsic difficulty (the unpruned model achieves only 53.0\% vs.\ 90.83\% on GSM8K) and generation-length truncation at the 2{,}048-token evaluation limit (over half of dense-model responses are truncated; Table~\ref{tab:math500}), both of which compress all pruned methods toward a performance floor and reduce inter-method differentiation (\S\ref{sec:ood}).
116	CKA-only also produces more efficient reasoning: only 22\% of completions are truncated at the 2{,}048-token limit (mean 655 tokens) versus Standard's 44\% (mean 1{,}128 tokens), indicating that the preserved structure enables shorter reasoning chains rather than longer ones.
117	The $\alpha$ dose-response effect is not statistically significant on MATH-500: SFT accuracy varies by ${\sim}$8\,pp across $\alpha$ values, but with stderr ${\approx}$2\,pp per point, attributable to high truncation rates at the 2048-token limit and floor effects at this difficulty level.
118	The inverted-U pattern is validated on GSM8K (Table~\ref{tab:alpha}); MATH-500 does not resolve the dose-response shape.
119	
120	\section{MBPP Code Generation}
121	\label{sec:appendix_mbpp}
122	
123	\input{tables/tab_mbpp}
124	
125	MBPP GRPO deltas are uniformly slightly positive across all fine-grained methods (mean $+$1.25\,pp), but none are statistically significant at this sample size ($N{=}374$; stderr ${\approx}1.7$\,pp).
126	This directional consistency may reflect a weak task-specific GRPO effect at the capability floor rather than a violation of reward-accuracy decoupling.
127	
128	\section{CKA Scoring Stability}
129	\label{sec:appendix_cka_stability}
130	
131	\input{tables/tab_cka_stability}
132	
133	CKA-based structure rankings are highly stable across calibration data volumes: Spearman $\rho$ between rankings from 256, 512, and 1024 calibration samples ranges from 0.964 to 0.979, indicating that the scoring criterion is not sensitive to calibration set size.
134	
135	\section{Gradient Signal Analysis}
136	\label{sec:appendix_gradient}
137	
138	We compare per-layer gradient magnitudes during early GRPO training ($N{=}200$ GSM8K calibration samples) across three pruning criteria using paired Wilcoxon signed-rank tests.
139	
140	\begin{table}[h]
141	\centering
142	\small
143	\caption{Pairwise gradient magnitude ratios during GRPO training. Ratio: mean gradient magnitude of method A divided by method B across 56 parameter groups (28 layers $\times$ 2 projections). Significant layers: count where paired Wilcoxon signed-rank $p{<}0.05$.}
144	\label{tab:gradient_flow}
145	\begin{tabular}{@{}lcc@{}}
146	\toprule
147	Comparison & Gradient Ratio & Sig.\ Layers \\
148	\midrule
149	CKA-only vs Standard & 2.89$\times$ & 55\,/\,56 \\
150	CKA-only vs \rasp{} & 2.26$\times$ & 56\,/\,56 \\
151	\rasp{} vs Standard & 1.28$\times$ & 45\,/\,56 \\
152	\bottomrule
153	\end{tabular}
154	\end{table}
155	
156	The gradient magnitude hierarchy (CKA-only $\gg$ \rasp{} $>$ Standard) mirrors the recovery capacity hierarchy (GSM8K: 64.39\% $>$ 60.88\% $>$ 59.84\%), with bootstrap 95\% CIs for all ratios excluding 1.0.
157	This is consistent with diversity preservation enabling stronger training signals during GRPO, though the evidence is correlational: an alternative explanation (that CKA-only retains more functional structure, producing higher initial loss and naturally larger gradients) cannot be ruled out.
158	
159	\section{Seed Reproducibility}
160	\label{sec:appendix_seed}
161	
162	CKA-only GSM8K accuracy across 3 GRPO seeds: 64.37\% (seed 42), 64.22\% (seed 123), 64.59\% (seed 456), yielding mean 64.39\% $\pm$ 0.19\,pp.
163	Standard: mean 59.84\% $\pm$ 0.38\,pp across the same 3 seeds.
164	See Table~\ref{tab:multiseed} for the full summary.
165	
166	\section{Sparsity Cliff at 30\%}
167	\label{sec:appendix_sparsity_cliff}
168	
169	\input{tables/table4_sparsity_cliff}
170	
171	All tested methods collapse at 30\% sparsity: Standard retains 4\% accuracy, CKA-only 1.6\%, and \rasp{} 0\%.
172	This capacity threshold, independent of pruning criterion, validates 20\% as the operating point and confirms that the recovery capacity spectrum reflects how methods allocate a limited pruning budget.
173	
174	\section{Multi-Seed GRPO Results}
175	\label{sec:appendix_multiseed}
176	
177	\begin{table}[h]
178	\centering
179	\small
180	\caption{Multi-seed GRPO results on GSM8K ($N{=}1{,}319$). CKA-only, Standard, and Random each trained with 3 GRPO seeds (42, 123, 456); pruning calibration and SFT are identical across all runs within each sparsity level.}
181	\label{tab:multiseed}
182	\begin{tabular}{@{}llccc@{}}
183	\toprule
184	Sparsity & Method & Mean Acc.\,(\%) & Std\,(pp) & Seeds \\
185	\midrule
186	\multirow{4}{*}{20\%} & CKA-only & 64.39 & 0.19 & 3 \\
187	 & Standard & 59.84 & 0.38 & 3 \\
188	 & \rasp{} & 60.88 & -- & 1 \\
189	 & Random & 50.72 & 0.15 & 3 \\
190	\midrule
191	\multirow{2}{*}{15\%} & CKA-only & 72.76 & 0.57 & 3 \\
192	 & Standard & 65.56 & 0.50 & 3 \\
193	\bottomrule
194	\end{tabular}
195	\end{table}
196	
197	At 20\% sparsity, the 4.55\,pp gap between CKA-only and Standard is robust across seeds, with non-overlapping ranges (CKA-only: 64.22--64.59\%, Standard: 59.44--60.20\%).
198	Standard shows a wider observed range across seeds (0.76\,pp vs 0.37\,pp), consistent with borderline-collapse dynamics where small perturbations produce larger outcome variation.
199	Random (3 seeds: 50.57\%, 50.72\%, 50.87\%; $\sigma{=}0.15$\,pp, observed range 0.30\,pp) converges in a narrow band with SFT accuracy seed-independent at 51.25\%.
200	All three seeds satisfy GRPO $\leq$ SFT ($\Delta{=}{-}0.68$, $-$0.53, $-$0.38\,pp), confirming that reward-accuracy decoupling is reproducible across seeds even for stagnating methods.
201	Note: Standard seed 42 was trained from a separately initialized SFT checkpoint (accuracy 59.21\% vs.\ 59.29\% for seeds 123/456; $\Delta = 0.08$\,pp).
202	At 15\% sparsity, the gap widens to 7.20\,pp (72.76\% vs 65.56\%, $t{\approx}16.4$, $p{<}0.001$), with non-overlapping ranges (CKA-only: 72.10--73.09\%, Standard: 65.13--65.43\%).
203	
204	\section{Cross-Sparsity Validation}
205	\label{sec:appendix_cross_sparsity}
206	
207	\begin{table}[h]
208	\centering
209	\small
210	\caption{Cross-sparsity validation on DeepSeek-R1-Distill-Qwen-7B. GSM8K accuracy ($N{=}1{,}319$) after SFT warmup and GRPO recovery. 15\% and 20\% GRPO values are mean over 3 seeds (see Tables~\ref{tab:decoupling},~\ref{tab:multiseed}). $^\ddagger$Single seed. Mean $|\Delta| \leq 1$\,pp across all conditions.}
211	\label{tab:cross_sparsity}
212	\begin{tabular}{@{}llccc@{}}
213	\toprule
214	Sparsity & Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
215	\midrule
216	\multirow{2}{*}{15\%} & CKA-only & 72.18 & \textbf{72.76{\scriptsize$\pm$0.57}} & $+$0.58 \\
217	 & Standard & 66.49 & 65.56{\scriptsize$\pm$0.50} & $-$0.93 \\
218	\midrule
219	\multirow{2}{*}{20\%} & CKA-only & 63.91 & 64.39 & $+$0.48 \\
220	 & Standard & 59.29 & 59.84 & $+$0.55 \\
221	\midrule
222	\multirow{2}{*}{25\%$^\ddagger$} & CKA-only & 60.12 & 59.59 & $-$0.53 \\
223	 & Standard & 50.87 & 51.86 & $+$0.99 \\
224	\midrule
225	30\% & All & \multicolumn{3}{c}{Collapse ($\leq$4\%; Table~\ref{tab:sparsity_cliff})} \\
226	\bottomrule
227	\end{tabular}
228	\end{table}
229	
230	At 15\% sparsity (3-seed mean), the CKA-only advantage widens to $+$7.20\,pp (72.76\% vs 65.56\%), compared to $+$4.55\,pp at 20\%.
231	CKA-only at 15\% (72.76\%) represents the highest mean accuracy across all experimental conditions, retaining 80.1\% of original dense model performance (90.83\%).
232	At 25\% sparsity (single seed), Standard's SFT accuracy decline accelerates ($-$7.20\,pp from 15\%$\to$20\%, $-$8.42\,pp from 20\%$\to$25\%), while CKA-only's decline decelerates ($-$8.27\,pp then $-$3.79\,pp).
233	Reward-accuracy decoupling is preserved ($|\Delta| \leq 1$\,pp for both methods) despite Standard's near-zero peak reward (0.008).
234	
235	\section{Cross-Scale Validation}
236	\label{sec:appendix_cross_scale}
237	
238	\input{tables/tab5_cross_scale}
239	
240	On DeepSeek-R1-Distill-Qwen-1.5B at 20\% sparsity, the three-method ordering is preserved (CKA-only 35.48\% $\gg$ \rasp{} 26.16\% $>$ Standard 22.29\%), with reward-accuracy decoupling confirmed at this scale ($|\Delta| < 1$\,pp: CKA-only $-$0.15, Standard $-$0.61\,pp).
241	
242	\section{Cross-Model Validation within Qwen2.5 Family}
243	\label{sec:appendix_cross_arch}
244	
245	\begin{table}[h]
246	\centering
247	\small
248	\caption{Cross-model validation on Qwen2.5-Math-7B~\citep{qwen2.5} (same Qwen2.5 architecture family) at 20\% structured sparsity. Accuracy evaluated on GSM8K ($N{=}200$). Post-SFT reports accuracy $\pm$ binomial standard error ($N{=}200$). EOS rate: fraction of generations that produce a valid end-of-sequence token.}
249	\label{tab:cross_arch}
250	\resizebox{\columnwidth}{!}{%
251	\begin{tabular}{@{}lccc@{}}
252	\toprule
253	Method & Post-Prune\,(\%) & Post-SFT\,(\%) & EOS Rate\,(\%) \\
254	\midrule
255	CKA-only & 1.0 & \textbf{51.50 $\pm$ 3.53} & 27.0 \\
256	Standard & 18.5 & 21.00 $\pm$ 2.88 & 36.5 \\
257	\bottomrule
258	\end{tabular}}
259	\end{table}
260	
261	CKA-only pruning causes near-total initial damage on Qwen2.5-Math-7B (1.0\% post-prune accuracy vs Standard's 18.5\%), yet SFT recovers CKA-only to 51.50\% while Standard remains at 21.00\%.
262	This post-prune accuracy reversal provides strong evidence that recovery capacity is shaped by preserved network structure rather than starting accuracy.
263	EOS rates remain below 40\% for both methods, indicating that SFT warmup is less effective on this architecture; GRPO validation is deferred to future work.\footnote{Preliminary GRPO evaluation yields 48.60\% (243/500), but 83.8\% of responses were truncated at 2048 tokens, precluding direct comparison with SFT results.}
264	
265	\section{Structural Overlap Analysis}
266	\label{sec:appendix_overlap}
267	
268	CKA-only and Standard pruning produce markedly different removal patterns across the 28 layers of DeepSeek-R1-Distill-Qwen-7B at 20\% sparsity.
269	CKA-only concentrates pruning in early layers (L0--9 account for 72.5\% of removed MLP groups), preserving nearly all structures in later layers (L16--27).
270	Standard distributes removals more uniformly, pruning substantial numbers of groups in late layers (L16--18, L22, L25--26).
271	
272	The methods share only partial overlap in which structures they remove.
273	65 MLP groups are pruned exclusively by CKA-only (retained by Standard), concentrated in L6--9 and L27; these are structures that gradient importance scores as important but CKA identifies as redundant with neighboring groups.
274	Conversely, 46+ groups are pruned exclusively by Standard (retained by CKA-only), concentrated in L16--18, L22, and L25--26; these are structures that gradient importance scores as unimportant but CKA identifies as representationally unique.
275	
276	This pattern is consistent with the layer-wise CKA similarity analysis (Figure~\ref{fig:cka_heatmap}): CKA-only's aggressive early-layer pruning disrupts dense representations (low diagonal CKA, $\mu{=}0.62$) but preserves diverse late-layer pathways, while Standard's uniform pruning maintains dense fidelity ($\mu{=}0.90$) at the cost of removing unique computational pathways in later layers.
277	
278	\section{KL Divergence During GRPO Training}
279	\label{sec:appendix_kl}
280	
281	Figure~\ref{fig:kl_divergence} shows the KL divergence between the evolving policy and the frozen reference model across GRPO training for all four pruning criteria.
282	
283	\begin{figure}[t]
284	    \centering
285	    \includegraphics[width=0.75\columnwidth]{figures/paper/fig_appendix_kl.pdf}
286	    \caption{KL divergence between the policy and reference model during GRPO training. RASP maintains near-zero KL ($<$0.001), consistent with minimal policy movement during collapse. Random shows the highest KL (${\sim}$0.004--0.005), indicating more policy exploration. CKA-only and Standard fall between these extremes.}
287	    \label{fig:kl_divergence}
288	\end{figure}
289	
290	\section{Depth-First Pruning Baseline}
291	\label{sec:appendix_depth_first}
292	
293	As a sanity check, we test whether CKA-only's advantage reflects mere layer-depth bias by constructing a depth-first baseline: synthetic importance scores force removal of late layers first (L18--27: 0.001, L10--17: 0.5, L0--9: 1.0), then standard pruning at 20\% sparsity.
294	Both SFT (${\sim}$10\%) and GRPO (${\sim}$8\%) accuracy are near chance (early-stopped at $N{\approx}50$--88 samples due to conclusive results), confirming that naive depth ordering cannot substitute for criterion-based structure selection.
295	This baseline operates at layer-level granularity (removing entire transformer blocks), unlike CKA-only/Standard/\rasp{} which prune at MLP channel group level; the granularity difference limits direct comparison with our main results and precludes using this baseline as evidence for the recovery capacity spectrum.
296	
297	\section{Per-Layer Capacity Floor Ablation}
298	\label{sec:appendix_floor}
299	
300	\begin{table}[h]
301	\centering
302	\small
303	\caption{Effect of per-layer capacity floor $\tau$ on CKA-only pruning at 20\% sparsity. GSM8K accuracy ($N{=}1{,}319$) after GRPO recovery (100 steps). Default $\tau{=}0.4$.}
304	\label{tab:floor_ablation}
305	\begin{tabular}{@{}lcc@{}}
306	\toprule
307	Floor $\tau$ & GRPO Acc.\,(\%) & $\Delta$ vs $\tau{=}0.4$\,(pp) \\
308	\midrule
309	0.3 & 65.05 & $+$0.68 \\
310	0.4 (default) & 64.37 & --- \\
311	0.5 & 61.71 & $-$2.66 \\
312	0.6 & 62.02 & $-$2.35 \\
313	\bottomrule
314	\end{tabular}
315	\end{table}
316	
317	The per-layer capacity floor $\tau$ sets the minimum fraction of MLP channel groups retained in each layer, preventing over-pruning of any single layer regardless of its importance score.
318	We ablate $\tau \in \{0.3, 0.4, 0.5, 0.6\}$ using CKA-only pruning at 20\% sparsity.
319	Lowering $\tau$ to 0.3 slightly improves accuracy ($+$0.68\,pp), while raising it to 0.5 or 0.6 causes a notable drop ($-$2.66 and $-$2.35\,pp respectively; the difference between 0.5 and 0.6 is not significant at 0.31\,pp $\ll$ stderr $\approx$ 1.3\,pp).
320	Over-constraining per-layer retention hurts global pruning quality by forcing removal of important structures in unconstrained layers.
321	
322	\section{TOST Equivalence Testing}
323	\label{sec:appendix_tost}
324	
325	To formally assess whether SFT and GRPO produce equivalent GSM8K accuracy, we apply Two One-Sided Tests (TOST) on $N{=}1{,}319$ paired per-example outcomes for CKA-only and Standard at 20\% sparsity across multiple GRPO seeds.
326	For each pair, $d_i = \mathbb{1}[\text{SFT correct}]_i - \mathbb{1}[\text{GRPO correct}]_i$, and we test $H_0$: $|\bar{d}| \geq \varepsilon$ against $H_A$: $|\bar{d}| < \varepsilon$.
327	
328	\begin{table}[h]
329	\centering
330	\small
331	\caption{TOST equivalence results ($\varepsilon{=}2$\,pp). All observed $|\Delta|{<}1$\,pp.}
332	\label{tab:tost}
333	\begin{tabular}{@{}llrr@{}}
334	\toprule
335	Criterion & GRPO seed & $\Delta$ (pp) & $p_\text{TOST}$ \\
336	\midrule
337	CKA-only & seed 42 & $-$0.45 & 0.008 \\
338	CKA-only & seed 123 & $-$0.30 & 0.005 \\
339	CKA-only & verify & $-$0.15 & 0.001 \\
340	CKA-only & seed 456 & $-$0.68 & 0.023 \\
341	\midrule
342	Standard & seed 123 & $-$0.68 & 0.020 \\
343	Standard & seed 456 & $-$0.99 & 0.069 \\
344	Standard & fair\_v2 & $-$0.23 & 0.010 \\
345	Standard & ext 300 & $-$0.08 & 0.007 \\
346	\bottomrule
347	\end{tabular}
348	\end{table}
349	
350	We select $\varepsilon{=}2$\,pp because it is approximately $4\times$ the observed cross-seed standard deviation ($\sigma{=}0.19$\,pp for CKA-only at 20\% sparsity), ensuring the margin reflects meaningful practical differences rather than measurement noise.
351	At $\varepsilon{=}2$\,pp, 7/8 comparisons reject the null ($p{<}0.05$); the remaining pair (Standard vs.\ seed 456, $\Delta{=}{-}0.99$\,pp) is borderline ($p{=}0.069$).
352	At $\varepsilon{=}3$\,pp, all 8/8 are significant ($p{<}0.002$).
353	At $\varepsilon{=}1$\,pp, statistical power is insufficient with binary outcomes at $N{=}1{,}319$.
354	
355	\section{Use of AI Assistants}
356	\label{sec:appendix_ai_assistants}
357	
358	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
359	\begin{itemize}[nosep,leftmargin=*]
360	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
361	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
362	    \item \textbf{Literature:} summarizing related papers to inform the related-work section.
363	\end{itemize}
364	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "612d9cc2-6fc0-44ff-8b2a-059d2da19e62",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "546602bf-3f64-49b5-aef9-0d62d5c35d51",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex",
      "content": "\\section{Training Details}\n\\label{sec:appendix_training}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Hyperparameter details for SFT warmup and GRPO recovery stages. All methods share the same GRPO configuration; Random uses the TRL default generation limit (marked with $^\\dagger$).}\n\\label{tab:hyperparams}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll@{}}\n\\toprule\nParameter & SFT & GRPO \\\\\n\\midrule\nLearning rate & $2 \\times 10^{-5}$ & $1 \\times 10^{-6}$ \\\\\nBatch size & 1 & 1 \\\\\nGradient accumulation & 8 & 1 \\\\\nMax sequence length & 2{,}048 & -- \\\\\nMax new tokens & -- & 1{,}024\\,$^\\dagger$512 \\\\\nOptimizer & AdamW & AdamW \\\\\nEpochs / Steps & 2 epochs & 100 steps \\\\\nKL coefficient $\\beta$ & -- & 0.01 \\\\\nSampling temperature & -- & 0.4 \\\\\nNum generations per prompt & -- & 8 \\\\\nReward & -- & Binary (exact match) \\\\\nLoss formulation & Cross-entropy & DAPO-style clipped \\\\\n\\texttt{reward\\_desert\\_patience} & -- & 50 \\\\\n\\bottomrule\n\\multicolumn{3}{l}{\\footnotesize $^\\dagger$Random uses TRL default of 512 tokens; all other methods use 1{,}024.} \\\\\n\\end{tabular}}\n\\end{table}\n\n\\section{Algorithm}\n\\label{sec:appendix_algo}\n\n\\begin{algorithm}[h]\n\\caption{Controlled Pruning Comparison Framework}\n\\label{alg:rasp}\n\\begin{algorithmic}[1]\n\\Require Model $\\mathcal{M}$, calibration data $\\mathcal{D}_\\text{cal}$, target sparsity $s$, scoring criterion $\\mathcal{C} \\in \\{\\text{Std}, \\text{RASP}, \\text{CKA}, \\text{Rand}\\}$, layer floor $\\tau$\n\\Ensure Pruned and recovered model $\\mathcal{M}'$\n\\Statex \\textit{\\% Stage 1: Shared Structural Analysis}\n\\For{each structure $h \\in \\mathcal{H}$}\n    \\State Compute importance $I(h)$ via Eq.~\\eqref{eq:importance}\n    \\State Collect activations $\\mathbf{X}_h$ on $\\mathcal{D}_\\text{cal}$\n\\EndFor\n\\For{each layer $\\ell = 1, \\ldots, L$}\n    \\For{each structure $h_i$ in layer $\\ell$}\n        \\State $F(h_i) \\gets \\frac{1}{|\\mathcal{H}_\\ell|-1} \\sum_{j \\neq i} \\text{CKA}(\\mathbf{X}_{h_i}, \\mathbf{X}_{h_j})$\n    \\EndFor\n\\EndFor\n\\Statex \\textit{\\% Stage 2: Criterion-Specific Scoring}\n\\For{each structure $h \\in \\mathcal{H}$}\n    \\State $S(h) \\gets \\mathcal{C}(I(h), F(h))$ \\hfill $\\triangleright$ Eq.~\\ref{eq:standard}, \\ref{eq:score}, \\ref{eq:cka_only}, or random\n\\EndFor\n\\State Sort $\\mathcal{H}$ by $S(h)$ ascending; prune lowest up to $s$, subject to $\\tau$\n\\Statex \\textit{\\% Stage 3: Two-Stage Recovery}\n\\State $\\mathcal{M}_\\text{warm} \\gets \\text{SFT}(\\mathcal{M}_\\text{pruned}, \\mathcal{D}_\\text{sft})$ \\hfill $\\triangleright$ restore EOS \\& format\n\\State $\\mathcal{M}' \\gets \\text{GRPO}(\\mathcal{M}_\\text{warm}, \\mathcal{D}_\\text{rlvr})$ \\hfill $\\triangleright$ recover reasoning\n\\State \\Return $\\mathcal{M}'$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\section{Inference Efficiency}\n\\label{sec:appendix_inference}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Inference characteristics at 20\\% sparsity (single-GPU, no contention). Pruning reduces parameters by 19\\% and memory by ${\\sim}$28\\%, with TTFT improving 18\\%. Per-token throughput decreases 19\\% (0.81$\\times$) due to non-uniform layer widths from full-layer removal that current GPU kernels do not optimize.}\n\\label{tab:inference}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nConfiguration & TPS\\,(tok/s) & TTFT\\,(ms) & Per-token\\,(ms) & Params\\,(B) \\\\\n\\midrule\nDense 7B & 72.0 & 20.1 & 13.9 & 7.62 \\\\\nCKA-only 20\\% & 58.3 & 16.4 & 16.7 & 6.16 \\\\\nStandard 20\\% & 58.2 & 16.4 & 16.7 & 6.16 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAll pruned models achieve ${\\sim}$28\\% memory reduction from structural parameter removal.\nTTFT (time to first token) improves by 18\\% (20.1$\\to$16.4\\,ms), reflecting faster prefill with fewer parameters.\nPer-token throughput decreases by 19\\% (72.0$\\to$58.3 tok/s, or 13.9$\\to$16.7\\,ms per token), consistent with non-uniform layer widths creating computational bottlenecks that current GPU kernels do not optimize away.\nCKA-only and Standard show identical throughput (58.3 vs 58.2 tok/s), confirming that the pruning criterion affects recovery capacity but not inference speed at matched sparsity.\n\n\\section{CKA Coefficient $\\alpha$ Ablation}\n\\label{sec:appendix_alpha}\n\n\\input{tables/table3_alpha}\n\nOn GSM8K, the dose-response curve across $\\alpha \\in \\{0.5, 1.0, 2.0, 3.0, 4.0\\}$ reveals an inverted-U pattern peaking at $\\alpha{=}2.0$ (SFT 64.97\\%, GRPO 66.11\\%, $\\Delta{=}{+}1.14$\\,pp; Table~\\ref{tab:alpha}).\nAt $\\alpha{=}0.5$, importance still dominates; recovery is low (SFT 60.73\\%, GRPO 61.18\\%).\nAt $\\alpha{=}1.0$ (\\rasp{}), GRPO collapses (peak reward 0.061, accuracy 60.88\\%, $\\Delta{=}{-}0.61$\\,pp).\n$\\alpha{=}3.0$ (SFT 64.14\\%, GRPO 63.46\\%, $\\Delta{=}{-}0.68$\\,pp) excludes a plateau hypothesis: accuracy drops 2.65\\,pp from the $\\alpha{=}2.0$ peak, confirming that the optimum is a true peak rather than a saturation regime.\nAt $\\alpha{=}4.0$, CKA overlap dominates; the model recovers to 62.77\\% GRPO accuracy (SFT 61.94\\%, $\\Delta{=}{+}0.83$\\,pp) with active GRPO learning (reward 0.146$\\to$0.256$\\to$0.198).\nReward-accuracy decoupling holds at every $\\alpha$ value: $|\\Delta| \\leq 1.14$\\,pp across all five points.\n\n\\section{Extended Training Dynamics}\n\\label{sec:appendix_extended}\n\nSee Figure~\\ref{fig:extended_training} in the main text for the 300-step extended training results.\nAt 300 steps, GSM8K accuracy: CKA-only 64.37\\% (identical to 100-step seed 42), Standard 59.29\\% (within 100-step seed variance of $\\pm$0.38\\,pp).\nThe unchanged accuracy despite rising CKA-only reward (0.308 at step 300 vs.\\ 0.354 peak at step 100) directly demonstrates reward-accuracy decoupling at this training horizon.\n\n\\section{MATH-500 Out-of-Distribution Evaluation}\n\\label{sec:appendix_math500}\n\n\\input{tables/tab_math500}\n\nCKA-only and Standard both outperform \\rasp{} and Random on MATH-500 (SFT: 27.4\\%, 25.6\\% vs.\\ 21.6\\%, 16.6\\%; GRPO: 27.6\\%, 27.0\\% vs.\\ 23.0\\%, 15.0\\%), consistent with GSM8K.\nHowever, the CKA-only--Standard gap narrows substantially: from 4.6\\,pp (GSM8K SFT) to 1.8\\,pp (MATH-500 SFT) to 0.6\\,pp (MATH-500 GRPO).\nMiddle-ranked methods also swap positions (Standard $>$ \\rasp{} on MATH-500 vs.\\ \\rasp{} $>$ Standard on GSM8K).\nThis narrowing reflects two compounding factors: MATH-500's higher intrinsic difficulty (the unpruned model achieves only 53.0\\% vs.\\ 90.83\\% on GSM8K) and generation-length truncation at the 2{,}048-token evaluation limit (over half of dense-model responses are truncated; Table~\\ref{tab:math500}), both of which compress all pruned methods toward a performance floor and reduce inter-method differentiation (\\S\\ref{sec:ood}).\nCKA-only also produces more efficient reasoning: only 22\\% of completions are truncated at the 2{,}048-token limit (mean 655 tokens) versus Standard's 44\\% (mean 1{,}128 tokens), indicating that the preserved structure enables shorter reasoning chains rather than longer ones.\nThe $\\alpha$ dose-response effect is not statistically significant on MATH-500: SFT accuracy varies by ${\\sim}$8\\,pp across $\\alpha$ values, but with stderr ${\\approx}$2\\,pp per point, attributable to high truncation rates at the 2048-token limit and floor effects at this difficulty level.\nThe inverted-U pattern is validated on GSM8K (Table~\\ref{tab:alpha}); MATH-500 does not resolve the dose-response shape.\n\n\\section{MBPP Code Generation}\n\\label{sec:appendix_mbpp}\n\n\\input{tables/tab_mbpp}\n\nMBPP GRPO deltas are uniformly slightly positive across all fine-grained methods (mean $+$1.25\\,pp), but none are statistically significant at this sample size ($N{=}374$; stderr ${\\approx}1.7$\\,pp).\nThis directional consistency may reflect a weak task-specific GRPO effect at the capability floor rather than a violation of reward-accuracy decoupling.\n\n\\section{CKA Scoring Stability}\n\\label{sec:appendix_cka_stability}\n\n\\input{tables/tab_cka_stability}\n\nCKA-based structure rankings are highly stable across calibration data volumes: Spearman $\\rho$ between rankings from 256, 512, and 1024 calibration samples ranges from 0.964 to 0.979, indicating that the scoring criterion is not sensitive to calibration set size.\n\n\\section{Gradient Signal Analysis}\n\\label{sec:appendix_gradient}\n\nWe compare per-layer gradient magnitudes during early GRPO training ($N{=}200$ GSM8K calibration samples) across three pruning criteria using paired Wilcoxon signed-rank tests.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise gradient magnitude ratios during GRPO training. Ratio: mean gradient magnitude of method A divided by method B across 56 parameter groups (28 layers $\\times$ 2 projections). Significant layers: count where paired Wilcoxon signed-rank $p{<}0.05$.}\n\\label{tab:gradient_flow}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nComparison & Gradient Ratio & Sig.\\ Layers \\\\\n\\midrule\nCKA-only vs Standard & 2.89$\\times$ & 55\\,/\\,56 \\\\\nCKA-only vs \\rasp{} & 2.26$\\times$ & 56\\,/\\,56 \\\\\n\\rasp{} vs Standard & 1.28$\\times$ & 45\\,/\\,56 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient magnitude hierarchy (CKA-only $\\gg$ \\rasp{} $>$ Standard) mirrors the recovery capacity hierarchy (GSM8K: 64.39\\% $>$ 60.88\\% $>$ 59.84\\%), with bootstrap 95\\% CIs for all ratios excluding 1.0.\nThis is consistent with diversity preservation enabling stronger training signals during GRPO, though the evidence is correlational: an alternative explanation (that CKA-only retains more functional structure, producing higher initial loss and naturally larger gradients) cannot be ruled out.\n\n\\section{Seed Reproducibility}\n\\label{sec:appendix_seed}\n\nCKA-only GSM8K accuracy across 3 GRPO seeds: 64.37\\% (seed 42), 64.22\\% (seed 123), 64.59\\% (seed 456), yielding mean 64.39\\% $\\pm$ 0.19\\,pp.\nStandard: mean 59.84\\% $\\pm$ 0.38\\,pp across the same 3 seeds.\nSee Table~\\ref{tab:multiseed} for the full summary.\n\n\\section{Sparsity Cliff at 30\\%}\n\\label{sec:appendix_sparsity_cliff}\n\n\\input{tables/table4_sparsity_cliff}\n\nAll tested methods collapse at 30\\% sparsity: Standard retains 4\\% accuracy, CKA-only 1.6\\%, and \\rasp{} 0\\%.\nThis capacity threshold, independent of pruning criterion, validates 20\\% as the operating point and confirms that the recovery capacity spectrum reflects how methods allocate a limited pruning budget.\n\n\\section{Multi-Seed GRPO Results}\n\\label{sec:appendix_multiseed}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Multi-seed GRPO results on GSM8K ($N{=}1{,}319$). CKA-only, Standard, and Random each trained with 3 GRPO seeds (42, 123, 456); pruning calibration and SFT are identical across all runs within each sparsity level.}\n\\label{tab:multiseed}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nSparsity & Method & Mean Acc.\\,(\\%) & Std\\,(pp) & Seeds \\\\\n\\midrule\n\\multirow{4}{*}{20\\%} & CKA-only & 64.39 & 0.19 & 3 \\\\\n & Standard & 59.84 & 0.38 & 3 \\\\\n & \\rasp{} & 60.88 & -- & 1 \\\\\n & Random & 50.72 & 0.15 & 3 \\\\\n\\midrule\n\\multirow{2}{*}{15\\%} & CKA-only & 72.76 & 0.57 & 3 \\\\\n & Standard & 65.56 & 0.50 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 20\\% sparsity, the 4.55\\,pp gap between CKA-only and Standard is robust across seeds, with non-overlapping ranges (CKA-only: 64.22--64.59\\%, Standard: 59.44--60.20\\%).\nStandard shows a wider observed range across seeds (0.76\\,pp vs 0.37\\,pp), consistent with borderline-collapse dynamics where small perturbations produce larger outcome variation.\nRandom (3 seeds: 50.57\\%, 50.72\\%, 50.87\\%; $\\sigma{=}0.15$\\,pp, observed range 0.30\\,pp) converges in a narrow band with SFT accuracy seed-independent at 51.25\\%.\nAll three seeds satisfy GRPO $\\leq$ SFT ($\\Delta{=}{-}0.68$, $-$0.53, $-$0.38\\,pp), confirming that reward-accuracy decoupling is reproducible across seeds even for stagnating methods.\nNote: Standard seed 42 was trained from a separately initialized SFT checkpoint (accuracy 59.21\\% vs.\\ 59.29\\% for seeds 123/456; $\\Delta = 0.08$\\,pp).\nAt 15\\% sparsity, the gap widens to 7.20\\,pp (72.76\\% vs 65.56\\%, $t{\\approx}16.4$, $p{<}0.001$), with non-overlapping ranges (CKA-only: 72.10--73.09\\%, Standard: 65.13--65.43\\%).\n\n\\section{Cross-Sparsity Validation}\n\\label{sec:appendix_cross_sparsity}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-sparsity validation on DeepSeek-R1-Distill-Qwen-7B. GSM8K accuracy ($N{=}1{,}319$) after SFT warmup and GRPO recovery. 15\\% and 20\\% GRPO values are mean over 3 seeds (see Tables~\\ref{tab:decoupling},~\\ref{tab:multiseed}). $^\\ddagger$Single seed. Mean $|\\Delta| \\leq 1$\\,pp across all conditions.}\n\\label{tab:cross_sparsity}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nSparsity & Method & SFT\\,(\\%) & GRPO\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\n\\multirow{2}{*}{15\\%} & CKA-only & 72.18 & \\textbf{72.76{\\scriptsize$\\pm$0.57}} & $+$0.58 \\\\\n & Standard & 66.49 & 65.56{\\scriptsize$\\pm$0.50} & $-$0.93 \\\\\n\\midrule\n\\multirow{2}{*}{20\\%} & CKA-only & 63.91 & 64.39 & $+$0.48 \\\\\n & Standard & 59.29 & 59.84 & $+$0.55 \\\\\n\\midrule\n\\multirow{2}{*}{25\\%$^\\ddagger$} & CKA-only & 60.12 & 59.59 & $-$0.53 \\\\\n & Standard & 50.87 & 51.86 & $+$0.99 \\\\\n\\midrule\n30\\% & All & \\multicolumn{3}{c}{Collapse ($\\leq$4\\%; Table~\\ref{tab:sparsity_cliff})} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 15\\% sparsity (3-seed mean), the CKA-only advantage widens to $+$7.20\\,pp (72.76\\% vs 65.56\\%), compared to $+$4.55\\,pp at 20\\%.\nCKA-only at 15\\% (72.76\\%) represents the highest mean accuracy across all experimental conditions, retaining 80.1\\% of original dense model performance (90.83\\%).\nAt 25\\% sparsity (single seed), Standard's SFT accuracy decline accelerates ($-$7.20\\,pp from 15\\%$\\to$20\\%, $-$8.42\\,pp from 20\\%$\\to$25\\%), while CKA-only's decline decelerates ($-$8.27\\,pp then $-$3.79\\,pp).\nReward-accuracy decoupling is preserved ($|\\Delta| \\leq 1$\\,pp for both methods) despite Standard's near-zero peak reward (0.008).\n\n\\section{Cross-Scale Validation}\n\\label{sec:appendix_cross_scale}\n\n\\input{tables/tab5_cross_scale}\n\nOn DeepSeek-R1-Distill-Qwen-1.5B at 20\\% sparsity, the three-method ordering is preserved (CKA-only 35.48\\% $\\gg$ \\rasp{} 26.16\\% $>$ Standard 22.29\\%), with reward-accuracy decoupling confirmed at this scale ($|\\Delta| < 1$\\,pp: CKA-only $-$0.15, Standard $-$0.61\\,pp).\n\n\\section{Cross-Model Validation within Qwen2.5 Family}\n\\label{sec:appendix_cross_arch}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model validation on Qwen2.5-Math-7B~\\citep{qwen2.5} (same Qwen2.5 architecture family) at 20\\% structured sparsity. Accuracy evaluated on GSM8K ($N{=}200$). Post-SFT reports accuracy $\\pm$ binomial standard error ($N{=}200$). EOS rate: fraction of generations that produce a valid end-of-sequence token.}\n\\label{tab:cross_arch}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & Post-Prune\\,(\\%) & Post-SFT\\,(\\%) & EOS Rate\\,(\\%) \\\\\n\\midrule\nCKA-only & 1.0 & \\textbf{51.50 $\\pm$ 3.53} & 27.0 \\\\\nStandard & 18.5 & 21.00 $\\pm$ 2.88 & 36.5 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nCKA-only pruning causes near-total initial damage on Qwen2.5-Math-7B (1.0\\% post-prune accuracy vs Standard's 18.5\\%), yet SFT recovers CKA-only to 51.50\\% while Standard remains at 21.00\\%.\nThis post-prune accuracy reversal provides strong evidence that recovery capacity is shaped by preserved network structure rather than starting accuracy.\nEOS rates remain below 40\\% for both methods, indicating that SFT warmup is less effective on this architecture; GRPO validation is deferred to future work.\\footnote{Preliminary GRPO evaluation yields 48.60\\% (243/500), but 83.8\\% of responses were truncated at 2048 tokens, precluding direct comparison with SFT results.}\n\n\\section{Structural Overlap Analysis}\n\\label{sec:appendix_overlap}\n\nCKA-only and Standard pruning produce markedly different removal patterns across the 28 layers of DeepSeek-R1-Distill-Qwen-7B at 20\\% sparsity.\nCKA-only concentrates pruning in early layers (L0--9 account for 72.5\\% of removed MLP groups), preserving nearly all structures in later layers (L16--27).\nStandard distributes removals more uniformly, pruning substantial numbers of groups in late layers (L16--18, L22, L25--26).\n\nThe methods share only partial overlap in which structures they remove.\n65 MLP groups are pruned exclusively by CKA-only (retained by Standard), concentrated in L6--9 and L27; these are structures that gradient importance scores as important but CKA identifies as redundant with neighboring groups.\nConversely, 46+ groups are pruned exclusively by Standard (retained by CKA-only), concentrated in L16--18, L22, and L25--26; these are structures that gradient importance scores as unimportant but CKA identifies as representationally unique.\n\nThis pattern is consistent with the layer-wise CKA similarity analysis (Figure~\\ref{fig:cka_heatmap}): CKA-only's aggressive early-layer pruning disrupts dense representations (low diagonal CKA, $\\mu{=}0.62$) but preserves diverse late-layer pathways, while Standard's uniform pruning maintains dense fidelity ($\\mu{=}0.90$) at the cost of removing unique computational pathways in later layers.\n\n\\section{KL Divergence During GRPO Training}\n\\label{sec:appendix_kl}\n\nFigure~\\ref{fig:kl_divergence} shows the KL divergence between the evolving policy and the frozen reference model across GRPO training for all four pruning criteria.\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=0.75\\columnwidth]{figures/paper/fig_appendix_kl.pdf}\n    \\caption{KL divergence between the policy and reference model during GRPO training. RASP maintains near-zero KL ($<$0.001), consistent with minimal policy movement during collapse. Random shows the highest KL (${\\sim}$0.004--0.005), indicating more policy exploration. CKA-only and Standard fall between these extremes.}\n    \\label{fig:kl_divergence}\n\\end{figure}\n\n\\section{Depth-First Pruning Baseline}\n\\label{sec:appendix_depth_first}\n\nAs a sanity check, we test whether CKA-only's advantage reflects mere layer-depth bias by constructing a depth-first baseline: synthetic importance scores force removal of late layers first (L18--27: 0.001, L10--17: 0.5, L0--9: 1.0), then standard pruning at 20\\% sparsity.\nBoth SFT (${\\sim}$10\\%) and GRPO (${\\sim}$8\\%) accuracy are near chance (early-stopped at $N{\\approx}50$--88 samples due to conclusive results), confirming that naive depth ordering cannot substitute for criterion-based structure selection.\nThis baseline operates at layer-level granularity (removing entire transformer blocks), unlike CKA-only/Standard/\\rasp{} which prune at MLP channel group level; the granularity difference limits direct comparison with our main results and precludes using this baseline as evidence for the recovery capacity spectrum.\n\n\\section{Per-Layer Capacity Floor Ablation}\n\\label{sec:appendix_floor}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Effect of per-layer capacity floor $\\tau$ on CKA-only pruning at 20\\% sparsity. GSM8K accuracy ($N{=}1{,}319$) after GRPO recovery (100 steps). Default $\\tau{=}0.4$.}\n\\label{tab:floor_ablation}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nFloor $\\tau$ & GRPO Acc.\\,(\\%) & $\\Delta$ vs $\\tau{=}0.4$\\,(pp) \\\\\n\\midrule\n0.3 & 65.05 & $+$0.68 \\\\\n0.4 (default) & 64.37 & --- \\\\\n0.5 & 61.71 & $-$2.66 \\\\\n0.6 & 62.02 & $-$2.35 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe per-layer capacity floor $\\tau$ sets the minimum fraction of MLP channel groups retained in each layer, preventing over-pruning of any single layer regardless of its importance score.\nWe ablate $\\tau \\in \\{0.3, 0.4, 0.5, 0.6\\}$ using CKA-only pruning at 20\\% sparsity.\nLowering $\\tau$ to 0.3 slightly improves accuracy ($+$0.68\\,pp), while raising it to 0.5 or 0.6 causes a notable drop ($-$2.66 and $-$2.35\\,pp respectively; the difference between 0.5 and 0.6 is not significant at 0.31\\,pp $\\ll$ stderr $\\approx$ 1.3\\,pp).\nOver-constraining per-layer retention hurts global pruning quality by forcing removal of important structures in unconstrained layers.\n\n\\section{TOST Equivalence Testing}\n\\label{sec:appendix_tost}\n\nTo formally assess whether SFT and GRPO produce equivalent GSM8K accuracy, we apply Two One-Sided Tests (TOST) on $N{=}1{,}319$ paired per-example outcomes for CKA-only and Standard at 20\\% sparsity across multiple GRPO seeds.\nFor each pair, $d_i = \\mathbb{1}[\\text{SFT correct}]_i - \\mathbb{1}[\\text{GRPO correct}]_i$, and we test $H_0$: $|\\bar{d}| \\geq \\varepsilon$ against $H_A$: $|\\bar{d}| < \\varepsilon$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST equivalence results ($\\varepsilon{=}2$\\,pp). All observed $|\\Delta|{<}1$\\,pp.}\n\\label{tab:tost}\n\\begin{tabular}{@{}llrr@{}}\n\\toprule\nCriterion & GRPO seed & $\\Delta$ (pp) & $p_\\text{TOST}$ \\\\\n\\midrule\nCKA-only & seed 42 & $-$0.45 & 0.008 \\\\\nCKA-only & seed 123 & $-$0.30 & 0.005 \\\\\nCKA-only & verify & $-$0.15 & 0.001 \\\\\nCKA-only & seed 456 & $-$0.68 & 0.023 \\\\\n\\midrule\nStandard & seed 123 & $-$0.68 & 0.020 \\\\\nStandard & seed 456 & $-$0.99 & 0.069 \\\\\nStandard & fair\\_v2 & $-$0.23 & 0.010 \\\\\nStandard & ext 300 & $-$0.08 & 0.007 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe select $\\varepsilon{=}2$\\,pp because it is approximately $4\\times$ the observed cross-seed standard deviation ($\\sigma{=}0.19$\\,pp for CKA-only at 20\\% sparsity), ensuring the margin reflects meaningful practical differences rather than measurement noise.\nAt $\\varepsilon{=}2$\\,pp, 7/8 comparisons reject the null ($p{<}0.05$); the remaining pair (Standard vs.\\ seed 456, $\\Delta{=}{-}0.99$\\,pp) is borderline ($p{=}0.069$).\nAt $\\varepsilon{=}3$\\,pp, all 8/8 are significant ($p{<}0.002$).\nAt $\\varepsilon{=}1$\\,pp, statistical power is insufficient with binary outcomes at $N{=}1{,}319$.\n\n\\section{Use of AI Assistants}\n\\label{sec:appendix_ai_assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \\LaTeX{}.\n    \\item \\textbf{Literature:} summarizing related papers to inform the related-work section.\n\\end{itemize}\n",
      "numLines": 364,
      "startLine": 1,
      "totalLines": 364
    }
  },
  "sourceToolAssistantUUID": "612d9cc2-6fc0-44ff-8b2a-059d2da19e62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-25T09:07:40.881Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S4VNBQ3WKXZT7Rz1M8KmDW`</summary>

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
  "parentUuid": "546602bf-3f64-49b5-aef9-0d62d5c35d51",
  "isSidechain": false,
  "requestId": "req_011CbP2Hf1t7i6JT7iNF7KWc",
  "type": "assistant",
  "uuid": "f906d88a-3e97-4e93-b493-c0495a22c7f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBhgTD9Gn7USQxSLgKGD5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12668,
      "cache_read_input_tokens": 38802,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 38802,
          "cache_creation_input_tokens": 12668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12668
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-25T09:07:40.965Z_

```json
{
  "parentUuid": "fc6724a7-7fcb-4041-b3c9-73d962f45a6a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "0b8b3b58-362e-44d7-9920-20c8c479a1e7",
  "timestamp": "2026-05-25T09:07:40.965Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
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
  "lastPrompt": "项目：recovery_aware_struct_prune Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 7 critical,…",
  "leafUuid": "0b8b3b58-362e-44d7-9920-20c8c479a1e7",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Recovery-aware structural pruning paper review",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033"
}
```

---

### Assistant

_source line 43 · 2026-05-25T09:07:43.796Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the table files to complete my understanding of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b8b3b58-362e-44d7-9920-20c8c479a1e7",
  "isSidechain": false,
  "requestId": "req_011CbP2JLMFZ4g28KD8TacJ1",
  "type": "assistant",
  "uuid": "ca5939b6-a276-42f5-abe7-c339a314cdb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGuX3YMnKKRRzGiML1r7ec",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23942,
      "cache_read_input_tokens": 51470,
      "output_tokens": 696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23942,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 696,
          "cache_read_input_tokens": 51470,
          "cache_creation_input_tokens": 23942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23942
          },
          "type": "message"
        }
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

_source line 44 · 2026-05-25T09:07:44.432Z_

读取表格文件以完成审计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca5939b6-a276-42f5-abe7-c339a314cdb1",
  "isSidechain": false,
  "requestId": "req_011CbP2JLMFZ4g28KD8TacJ1",
  "type": "assistant",
  "uuid": "80833bfa-6bb7-47be-9fa3-0f276a2faab3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGuX3YMnKKRRzGiML1r7ec",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23942,
      "cache_read_input_tokens": 51470,
      "output_tokens": 696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23942,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 696,
          "cache_read_input_tokens": 51470,
          "cache_creation_input_tokens": 23942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23942
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-25T09:07:46.119Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UFJSYUreKQGNM5i4jT7r1S`</summary>

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
  "parentUuid": "80833bfa-6bb7-47be-9fa3-0f276a2faab3",
  "isSidechain": false,
  "requestId": "req_011CbP2JLMFZ4g28KD8TacJ1",
  "type": "assistant",
  "uuid": "ea1acee0-404e-4e77-8209-f63065f9c0be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGuX3YMnKKRRzGiML1r7ec",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23942,
      "cache_read_input_tokens": 51470,
      "output_tokens": 696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23942,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 696,
          "cache_read_input_tokens": 51470,
          "cache_creation_input_tokens": 23942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23942
          },
          "type": "message"
        }
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

_source line 46 · 2026-05-25T09:07:51.370Z_

<details><summary>↩ Tool result · `toolu_011WNxyJnEb6Bo21W5ZAin2X`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\small
4	\caption{CKA scoring stability across calibration sizes. Spearman $\rho$ between structure rankings produced by different calibration set sizes. High correlation ($\rho \geq 0.964$) indicates that CKA-based scoring is robust to calibration data volume.}
5	\label{tab:cka_stability}
6	\begin{tabular}{@{}lcc@{}}
7	\toprule
8	Calibration Sizes & Spearman $\rho$ (min) & Spearman $\rho$ (mean) \\
9	\midrule
10	256 / 512 / 1024 & 0.964 & 0.979 \\
11	\bottomrule
12	\end{tabular}
13	\end{table}
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69750291-8645-4ee9-a31c-33615f20493d",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "58bae0a4-dfb4-4140-b7f0-84772c6eafe2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{CKA scoring stability across calibration sizes. Spearman $\\rho$ between structure rankings produced by different calibration set sizes. High correlation ($\\rho \\geq 0.964$) indicates that CKA-based scoring is robust to calibration data volume.}\n\\label{tab:cka_stability}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nCalibration Sizes & Spearman $\\rho$ (min) & Spearman $\\rho$ (mean) \\\\\n\\midrule\n256 / 512 / 1024 & 0.964 & 0.979 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  },
  "sourceToolAssistantUUID": "69750291-8645-4ee9-a31c-33615f20493d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-25T09:07:46.127Z_

<details><summary>↩ Tool result · `toolu_01UFJSYUreKQGNM5i4jT7r1S`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Recovery capacity spectrum at 20\% sparsity. $f_0$: zero-variance batch fraction. CKA-only sustains active learning; Random stagnates; Standard shows borderline collapse; \rasp{} exhibits full collapse. Best in \textbf{bold}.}
5	\label{tab:recovery_gradient}
6	\setlength{\tabcolsep}{5pt}
7	\begin{tabular}{@{}lccc@{}}
8	\toprule
9	Method & Peak Rew.\,$\uparrow$ & Mean Rew.\,$\uparrow$ & Min $f_0$\,$\downarrow$ \\
10	\midrule
11	CKA-only & \textbf{0.354} & \textbf{0.285} & \textbf{0.125} \\
12	Random & 0.190 & 0.164 & 0.300 \\
13	Standard & 0.081 & 0.050 & 0.500 \\
14	\rasp{} ($\alpha{=}1.0$) & 0.061 & 0.031 & 0.675 \\
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
  "parentUuid": "ea1acee0-404e-4e77-8209-f63065f9c0be",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "df162ca7-49fb-4a7e-9b43-bc686c6d6cd6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Recovery capacity spectrum at 20\\% sparsity. $f_0$: zero-variance batch fraction. CKA-only sustains active learning; Random stagnates; Standard shows borderline collapse; \\rasp{} exhibits full collapse. Best in \\textbf{bold}.}\n\\label{tab:recovery_gradient}\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & Peak Rew.\\,$\\uparrow$ & Mean Rew.\\,$\\uparrow$ & Min $f_0$\\,$\\downarrow$ \\\\\n\\midrule\nCKA-only & \\textbf{0.354} & \\textbf{0.285} & \\textbf{0.125} \\\\\nRandom & 0.190 & 0.164 & 0.300 \\\\\nStandard & 0.081 & 0.050 & 0.500 \\\\\n\\rasp{} ($\\alpha{=}1.0$) & 0.061 & 0.031 & 0.675 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  },
  "sourceToolAssistantUUID": "ea1acee0-404e-4e77-8209-f63065f9c0be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-25T09:07:47.094Z_

<details open><summary>🔧 Tool call — Read · `toolu_012V5pCSeGSEFpmTMZxVaQv1`</summary>

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
  "parentUuid": "df162ca7-49fb-4a7e-9b43-bc686c6d6cd6",
  "isSidechain": false,
  "requestId": "req_011CbP2JLMFZ4g28KD8TacJ1",
  "type": "assistant",
  "uuid": "72027e7a-b83a-42eb-887d-7a864e90a40e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGuX3YMnKKRRzGiML1r7ec",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23942,
      "cache_read_input_tokens": 51470,
      "output_tokens": 696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23942,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 696,
          "cache_read_input_tokens": 51470,
          "cache_creation_input_tokens": 23942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23942
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-25T09:07:47.098Z_

<details><summary>↩ Tool result · `toolu_012V5pCSeGSEFpmTMZxVaQv1`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Reward-accuracy decoupling on GSM8K ($N{=}1{,}319$, greedy decoding) at step 100. All pruned models at 20\% sparsity. Multi-seed (mean $\pm$ std) where available. Best in \textbf{bold}.}
5	\label{tab:decoupling}
6	\setlength{\tabcolsep}{4pt}
7	\begin{tabular}{@{}lcccc@{}}
8	\toprule
9	Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) & Peak Rew. \\
10	\midrule
11	Unpruned & \textbf{81.27} & \textbf{81.27} & $\phantom{-}$0.00 & \textbf{0.669} \\
12	CKA-only & 63.91 & 64.39{\scriptsize$\pm$0.19} & $+$0.48 & 0.354 \\
13	Standard & 59.29 & 59.84{\scriptsize$\pm$0.38} & $+$0.55 & 0.081 \\
14	\rasp{} ($\alpha{=}1.0$) & 61.49 & 60.88 & $-$0.61 & 0.061 \\
15	Random & 51.25 & 50.72{\scriptsize$\pm$0.15} & $-$0.53 & 0.190 \\
16	\midrule
17	ShortGPT & 44.73 & 43.37 & $-$1.36 & -- \\
18	\bottomrule
19	\end{tabular}
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72027e7a-b83a-42eb-887d-7a864e90a40e",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "226d9b60-ec0b-4301-97a9-e0251c2c9404",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Reward-accuracy decoupling on GSM8K ($N{=}1{,}319$, greedy decoding) at step 100. All pruned models at 20\\% sparsity. Multi-seed (mean $\\pm$ std) where available. Best in \\textbf{bold}.}\n\\label{tab:decoupling}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nMethod & SFT\\,(\\%) & GRPO\\,(\\%) & $\\Delta$\\,(pp) & Peak Rew. \\\\\n\\midrule\nUnpruned & \\textbf{81.27} & \\textbf{81.27} & $\\phantom{-}$0.00 & \\textbf{0.669} \\\\\nCKA-only & 63.91 & 64.39{\\scriptsize$\\pm$0.19} & $+$0.48 & 0.354 \\\\\nStandard & 59.29 & 59.84{\\scriptsize$\\pm$0.38} & $+$0.55 & 0.081 \\\\\n\\rasp{} ($\\alpha{=}1.0$) & 61.49 & 60.88 & $-$0.61 & 0.061 \\\\\nRandom & 51.25 & 50.72{\\scriptsize$\\pm$0.15} & $-$0.53 & 0.190 \\\\\n\\midrule\nShortGPT & 44.73 & 43.37 & $-$1.36 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  },
  "sourceToolAssistantUUID": "72027e7a-b83a-42eb-887d-7a864e90a40e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-25T09:07:47.577Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JYpvqYPB5htUsbwKiDK27r`</summary>

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
  "parentUuid": "226d9b60-ec0b-4301-97a9-e0251c2c9404",
  "isSidechain": false,
  "requestId": "req_011CbP2JLMFZ4g28KD8TacJ1",
  "type": "assistant",
  "uuid": "10f0a045-5284-47f6-a9d4-39e37f1ce6f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGuX3YMnKKRRzGiML1r7ec",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23942,
      "cache_read_input_tokens": 51470,
      "output_tokens": 696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23942,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 696,
          "cache_read_input_tokens": 51470,
          "cache_creation_input_tokens": 23942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23942
          },
          "type": "message"
        }
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

_source line 51 · 2026-05-25T09:07:47.581Z_

<details><summary>↩ Tool result · `toolu_01JYpvqYPB5htUsbwKiDK27r`</summary>

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
  "parentUuid": "10f0a045-5284-47f6-a9d4-39e37f1ce6f9",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "37bb47d3-8d10-487d-8f46-c2424ef6d217",
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
  "sourceToolAssistantUUID": "10f0a045-5284-47f6-a9d4-39e37f1ce6f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-25T09:07:48.517Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K8zzmgA3GehNVKNoV7Yazj`</summary>

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
  "parentUuid": "37bb47d3-8d10-487d-8f46-c2424ef6d217",
  "isSidechain": false,
  "requestId": "req_011CbP2JLMFZ4g28KD8TacJ1",
  "type": "assistant",
  "uuid": "687bb47a-0b15-43b0-aa15-b95aaa630022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGuX3YMnKKRRzGiML1r7ec",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23942,
      "cache_read_input_tokens": 51470,
      "output_tokens": 696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23942,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 696,
          "cache_read_input_tokens": 51470,
          "cache_creation_input_tokens": 23942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23942
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-25T09:07:48.522Z_

<details><summary>↩ Tool result · `toolu_01K8zzmgA3GehNVKNoV7Yazj`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\small
4	\caption{Cross-scale validation at 20\% sparsity. 7B: DeepSeek-R1-Distill-Qwen-7B (GSM8K mean over 3 seeds for CKA-only and Standard; see Table~\ref{tab:decoupling}). 1.5B: DeepSeek-R1-Distill-Qwen-1.5B (single seed). GSM8K accuracy ($N{=}1{,}319$). 7B reward = peak across 100 GRPO steps (cf.\ Table~\ref{tab:recovery_gradient}); 1.5B reward = mean across training steps.}
5	\label{tab:cross_scale}
6	\resizebox{\columnwidth}{!}{%
7	\begin{tabular}{@{}lcccc@{}}
8	\toprule
9	\multirow{2}{*}{Method} & \multicolumn{2}{c}{7B} & \multicolumn{2}{c}{1.5B} \\
10	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
11	 & Peak Rew. & GSM8K\,(\%) & Rew. & GSM8K\,(\%) \\
12	\midrule
13	CKA-only & \textbf{0.354} & \textbf{64.39} & \textbf{0.238} & \textbf{35.48} \\
14	Standard & 0.081 & 59.84 & 0.084 & 22.29 \\
15	\rasp{} ($\alpha{=}1.0$) & 0.061 & 60.88 & 0.099 & 26.16 \\
16	Random & 0.190 & -- & -- & -- \\
17	\bottomrule
18	\end{tabular}}
19	\end{table}
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "687bb47a-0b15-43b0-aa15-b95aaa630022",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "72fbe9ef-0915-4b05-9af9-91fd0073af51",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-scale validation at 20\\% sparsity. 7B: DeepSeek-R1-Distill-Qwen-7B (GSM8K mean over 3 seeds for CKA-only and Standard; see Table~\\ref{tab:decoupling}). 1.5B: DeepSeek-R1-Distill-Qwen-1.5B (single seed). GSM8K accuracy ($N{=}1{,}319$). 7B reward = peak across 100 GRPO steps (cf.\\ Table~\\ref{tab:recovery_gradient}); 1.5B reward = mean across training steps.}\n\\label{tab:cross_scale}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\multirow{2}{*}{Method} & \\multicolumn{2}{c}{7B} & \\multicolumn{2}{c}{1.5B} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n & Peak Rew. & GSM8K\\,(\\%) & Rew. & GSM8K\\,(\\%) \\\\\n\\midrule\nCKA-only & \\textbf{0.354} & \\textbf{64.39} & \\textbf{0.238} & \\textbf{35.48} \\\\\nStandard & 0.081 & 59.84 & 0.084 & 22.29 \\\\\n\\rasp{} ($\\alpha{=}1.0$) & 0.061 & 60.88 & 0.099 & 26.16 \\\\\nRandom & 0.190 & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  },
  "sourceToolAssistantUUID": "687bb47a-0b15-43b0-aa15-b95aaa630022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-25T09:07:49.566Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YXnR2zhr1tWirmLzkpW9c1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72fbe9ef-0915-4b05-9af9-91fd0073af51",
  "isSidechain": false,
  "requestId": "req_011CbP2JLMFZ4g28KD8TacJ1",
  "type": "assistant",
  "uuid": "b6936e83-c4fe-4b42-b774-2600415912c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGuX3YMnKKRRzGiML1r7ec",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23942,
      "cache_read_input_tokens": 51470,
      "output_tokens": 696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23942,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 696,
          "cache_read_input_tokens": 51470,
          "cache_creation_input_tokens": 23942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23942
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-25T09:07:49.573Z_

<details><summary>↩ Tool result · `toolu_01YXnR2zhr1tWirmLzkpW9c1`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\caption{Sparsity cliff at 30\% structured sparsity. All tested pruning criteria collapse, with near-zero accuracy and EOS generation rates below 6\%.}
4	\label{tab:sparsity_cliff}
5	\begin{tabular}{@{}lccc@{}}
6	\toprule
7	Method & $N$ & Acc.\,(\%) & EOS Rate\,(\%) \\
8	\midrule
9	Standard & 200 & 4 & 5.5 \\
10	\rasp{} ($\alpha{=}1.0$) & 200 & 0 & 3.0 \\
11	CKA-only & 500$^\dagger$ & 1.6 & --$^\dagger$ \\
12	\bottomrule
13	\multicolumn{4}{@{}l}{\footnotesize $^\dagger$Terminated early after collapse confirmed; 8/500 correct.}
14	\end{tabular}
15	\end{table}
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6936e83-c4fe-4b42-b774-2600415912c5",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "10e35459-2eae-446c-aa8f-fc31e3bfa8cd",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\caption{Sparsity cliff at 30\\% structured sparsity. All tested pruning criteria collapse, with near-zero accuracy and EOS generation rates below 6\\%.}\n\\label{tab:sparsity_cliff}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & $N$ & Acc.\\,(\\%) & EOS Rate\\,(\\%) \\\\\n\\midrule\nStandard & 200 & 4 & 5.5 \\\\\n\\rasp{} ($\\alpha{=}1.0$) & 200 & 0 & 3.0 \\\\\nCKA-only & 500$^\\dagger$ & 1.6 & --$^\\dagger$ \\\\\n\\bottomrule\n\\multicolumn{4}{@{}l}{\\footnotesize $^\\dagger$Terminated early after collapse confirmed; 8/500 correct.}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  },
  "sourceToolAssistantUUID": "b6936e83-c4fe-4b42-b774-2600415912c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-25T09:07:49.994Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SQEzkGSmjnFhC8ENdd8FMF`</summary>

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
  "parentUuid": "10e35459-2eae-446c-aa8f-fc31e3bfa8cd",
  "isSidechain": false,
  "requestId": "req_011CbP2JLMFZ4g28KD8TacJ1",
  "type": "assistant",
  "uuid": "4ba14811-d7bb-4ecd-af45-0e7fbf32fcc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGuX3YMnKKRRzGiML1r7ec",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23942,
      "cache_read_input_tokens": 51470,
      "output_tokens": 696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23942,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 696,
          "cache_read_input_tokens": 51470,
          "cache_creation_input_tokens": 23942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23942
          },
          "type": "message"
        }
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

_source line 57 · 2026-05-25T09:07:49.997Z_

<details><summary>↩ Tool result · `toolu_01SQEzkGSmjnFhC8ENdd8FMF`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\small
4	\caption{MATH-500 out-of-distribution evaluation ($N{=}500$, greedy decoding, \texttt{max\_new\_tokens=2048}). CKA-only and Standard both outperform \rasp{} and Random; the CKA-only--Standard GRPO gap is 0.6\,pp (vs.\ 4.62\,pp on GSM8K), consistent with difficulty and truncation compressing scores toward a floor. Best per section in \textbf{bold}.}
5	\label{tab:math500}
6	\begin{tabular}{@{}lccc@{}}
7	\toprule
8	Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	Dense & \multicolumn{3}{c}{53.0\,$^\dagger$} \\
11	\midrule
12	\multicolumn{4}{l}{\textit{20\% sparsity --- method comparison}} \\
13	CKA-only & \textbf{27.4} & \textbf{27.6} & $+$0.2 \\
14	Standard & 25.6 & 27.0 & $+$1.4 \\
15	\rasp{} ($\alpha{=}1.0$) & 21.6 & 23.0 & $+$1.4 \\
16	Random & 16.6 & 15.0 & $-$1.6 \\
17	\midrule
18	\multicolumn{4}{l}{\textit{20\% sparsity --- $\alpha$ dose-response}} \\
19	$\alpha{=}0.5$ & 26.8 & 26.8 & $+$0.0 \\
20	$\alpha{=}2.0$ & 25.6 & \textbf{27.4} & $+$1.8 \\
21	$\alpha{=}3.0$ & 23.6 & -- & -- \\
22	$\alpha{=}4.0$ & \textbf{27.8} & 27.2 & $-$0.6 \\
23	\midrule
24	\multicolumn{4}{l}{\textit{25\% sparsity}} \\
25	CKA-only & 18.8 & 17.6 & $-$1.2 \\
26	Standard & 15.4 & -- & -- \\
27	\bottomrule
28	\multicolumn{4}{p{0.85\columnwidth}}{\footnotesize $^\dagger$Over half of Dense responses truncated at 2048 tokens (73.6\% at 4096); all pruned models evaluated under the same constraint.}
29	\end{tabular}
30	\end{table}
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ba14811-d7bb-4ecd-af45-0e7fbf32fcc8",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "b1d40bab-1bfc-4ef5-b464-ac5ed8035377",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{MATH-500 out-of-distribution evaluation ($N{=}500$, greedy decoding, \\texttt{max\\_new\\_tokens=2048}). CKA-only and Standard both outperform \\rasp{} and Random; the CKA-only--Standard GRPO gap is 0.6\\,pp (vs.\\ 4.62\\,pp on GSM8K), consistent with difficulty and truncation compressing scores toward a floor. Best per section in \\textbf{bold}.}\n\\label{tab:math500}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & SFT\\,(\\%) & GRPO\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\nDense & \\multicolumn{3}{c}{53.0\\,$^\\dagger$} \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{20\\% sparsity --- method comparison}} \\\\\nCKA-only & \\textbf{27.4} & \\textbf{27.6} & $+$0.2 \\\\\nStandard & 25.6 & 27.0 & $+$1.4 \\\\\n\\rasp{} ($\\alpha{=}1.0$) & 21.6 & 23.0 & $+$1.4 \\\\\nRandom & 16.6 & 15.0 & $-$1.6 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{20\\% sparsity --- $\\alpha$ dose-response}} \\\\\n$\\alpha{=}0.5$ & 26.8 & 26.8 & $+$0.0 \\\\\n$\\alpha{=}2.0$ & 25.6 & \\textbf{27.4} & $+$1.8 \\\\\n$\\alpha{=}3.0$ & 23.6 & -- & -- \\\\\n$\\alpha{=}4.0$ & \\textbf{27.8} & 27.2 & $-$0.6 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{25\\% sparsity}} \\\\\nCKA-only & 18.8 & 17.6 & $-$1.2 \\\\\nStandard & 15.4 & -- & -- \\\\\n\\bottomrule\n\\multicolumn{4}{p{0.85\\columnwidth}}{\\footnotesize $^\\dagger$Over half of Dense responses truncated at 2048 tokens (73.6\\% at 4096); all pruned models evaluated under the same constraint.}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  },
  "sourceToolAssistantUUID": "4ba14811-d7bb-4ecd-af45-0e7fbf32fcc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-25T09:07:50.519Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DzbaSzyEqWWoqiN5o7CFr6`</summary>

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
  "parentUuid": "b1d40bab-1bfc-4ef5-b464-ac5ed8035377",
  "isSidechain": false,
  "requestId": "req_011CbP2JLMFZ4g28KD8TacJ1",
  "type": "assistant",
  "uuid": "7f8f9526-aac7-4293-84d2-f228cda35214",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGuX3YMnKKRRzGiML1r7ec",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23942,
      "cache_read_input_tokens": 51470,
      "output_tokens": 696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23942,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 696,
          "cache_read_input_tokens": 51470,
          "cache_creation_input_tokens": 23942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23942
          },
          "type": "message"
        }
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

_source line 59 · 2026-05-25T09:07:50.530Z_

<details><summary>↩ Tool result · `toolu_01DzbaSzyEqWWoqiN5o7CFr6`</summary>

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
14	\rasp{} ($\alpha{=}1.0$) 20\% & 11.76 & 13.10 & $+$1.34 \\
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
  "parentUuid": "7f8f9526-aac7-4293-84d2-f228cda35214",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "10fe3bc7-c6f0-4be1-b605-1df4bfccd2e1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{MBPP code generation accuracy ($N{=}374$, greedy decoding). All fine-grained pruning methods converge near a capability floor (${\\sim}$75\\% code capability loss vs Dense), limiting differentiation (${\\sim}$1\\,pp range, within stderr). ShortGPT shows a larger GRPO delta ($+$4.01\\,pp) but at the 95\\% CI boundary (stderr ${\\approx}$1.55\\,pp).}\n\\label{tab:mbpp}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & SFT\\,(\\%) & GRPO\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\nDense & -- & 53.48 & -- \\\\\n\\midrule\nCKA-only 20\\% & 12.83 & 14.17 & $+$1.34 \\\\\nStandard 20\\% & 12.03 & 13.10 & $+$1.07 \\\\\n\\rasp{} ($\\alpha{=}1.0$) 20\\% & 11.76 & 13.10 & $+$1.34 \\\\\n\\midrule\nShortGPT 20\\%$^\\dagger$ & 10.43 & 14.44 & $+$4.01 \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$Depth pruning; removes entire layers.}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  },
  "sourceToolAssistantUUID": "7f8f9526-aac7-4293-84d2-f228cda35214",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-25T09:07:51.333Z_

<details open><summary>🔧 Tool call — Read · `toolu_011WNxyJnEb6Bo21W5ZAin2X`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10fe3bc7-c6f0-4be1-b605-1df4bfccd2e1",
  "isSidechain": false,
  "requestId": "req_011CbP2JLMFZ4g28KD8TacJ1",
  "type": "assistant",
  "uuid": "69750291-8645-4ee9-a31c-33615f20493d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGuX3YMnKKRRzGiML1r7ec",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23942,
      "cache_read_input_tokens": 51470,
      "output_tokens": 696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23942,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 696,
          "cache_read_input_tokens": 51470,
          "cache_creation_input_tokens": 23942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23942
          },
          "type": "message"
        }
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
  "lastPrompt": "项目：recovery_aware_struct_prune Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 7 critical,…",
  "leafUuid": "58bae0a4-dfb4-4140-b7f0-84772c6eafe2",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Recovery-aware structural pruning paper review",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033"
}
```

---

### Assistant

_source line 63 · 2026-05-25T09:13:51.561Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the content. Let me perform the systematic audit across all dimensions.

Let me go through each audit dimension systematically:

### 1. 叙事一致性 (CRITICAL)

**Abstract 的"问题" == Intro 的"问题"?**
- Abstract: "Structured pruning compresses reasoning LLMs...but the pruned model requires recovery training...RLVR is widely assumed to be the superior recovery paradigm, yet our results suggest this advantage is attributable to the pruning criterion rather than an inherent property of RL"


- Intro: "The dominant assumption is that the recovery paradigm (SFT versus RLVR) determines recovery quality...Our results suggest that this hierarchy is attributable to suboptimal pruning rather than a fundamental property of RL"
- ✅ Consistent. Both frame the problem as: RLVR is assumed superior for recovery, but actually the pruning criterion matters more.

**Intro 的 "贡献列表" == Method 实际做了什么?**
- Contribution 1: Reward-accuracy decoupling → §4.3 (sec:decoupling), Table 2
- Contribution 2: Recovery capacity spectrum + RASP + dose-response → §3.3 (sec:scoring), §4.1 (sec:recovery_gradient), §4.4/5 (sec:additional_results, sec:extended_analysis)
- ✅ All contributions have corresponding sections.

**Method 的 "为什么这样设计" == Intro 的 "gap"?**
- Intro gap: "No prior work has compared multiple pruning criteria under RL or investigated whether the RLVR > SFT advantage persists across pruning strategies"
- Method design: Controlled comparison framework that isolates pruning criterion as the only variable
- ✅ Consistent.

**Experiments 验证的 == Intro 声称的贡献?**
- Claim 1 (decoupling): Verified in §4.3, Table 2, scatter plot, TOST testing
- Claim 2 (spectrum and dose-response): Verified across multiple pruning criteria and recovery paradigms in the main results and supplementary analyses
- ✅ Consistent.

**Conclusion 总结的 == Experiments 的结论?**
- Conclusion: "Under diversity-preserving pruning at 20-25% MLP sparsity on Qwen2.5-family models, the two paradigms produce near-identical accuracy (mean |Δ|=0.54pp; max 1.8pp), yet the pruning criterion creates a 4.4× peak reward gap."
- Experiments: This is exactly what was found.
- ✅ Consistent.

However, I'm noticing some potential scope misalignment: the Abstract mentions "four pruning criteria applied to a 7B reasoning model" but the experiments actually span multiple model sizes including 1.5B and cross-model evaluations, so the Abstract might be underselling the breadth of the work.

The Abstract does capture the core concepts though—"recovery capacity spectrum" and "reward-accuracy decoupling" are both central findings. The title accurately describes the paper's focus on how pruning criteria affect post-RLVR recovery in structured MLP pruning.

Looking at the Intro contributions, there's a slight structural difference: the Abstract essentially presents three key findings (the RASP scoring function, the recovery capacity spectrum, and reward-accuracy decoupling), but the Intro merges the first two into a single contribution. This is a minor organizational choice but worth noting.

Now examining the contributions more closely, I see the paper identifies two main findings: reward-accuracy decoupling at 20-25% sparsity where GRPO and SFT perform nearly identically, and the recovery capacity spectrum where RASP reveals an inverted-U pattern with four distinct criterion dynamics. These map well to the paper's core results.

But there's a potential tension in how the Abstract frames the RLVR advantage claim. It states that RLVR's superiority is attributable to the pruning criterion rather than an inherent property of RL, yet the main experiments at 20-25% sparsity show decoupling between SFT and GRPO—meaning the RLVR advantage actually disappears under certain conditions. The nuance is that it's not the criterion making RLVR better, but rather the criterion determining whether RLVR's advantage persists at all.

Looking deeper, the Abstract's framing seems slightly off. The experiments show the gap between GRPO and SFT stays small at 20-25% regardless of pruning criterion—Standard gives 0.55pp, RASP gives -0.61pp—so the real finding is that the gap is consistently small at this sparsity level, not that the criterion determines RLVR's advantage. The criterion matters more at 15% sparsity where GRPO amplifies the CKA advantage by 1.51pp.

The Abstract claims the prior RLVR advantage from other work comes from their pruning criterion rather than RL itself, and the paper's experiments support this—under better pruning, RLVR doesn't provide much benefit. But this is a different setting entirely (unstructured pruning at 96.5% retention), so the nuance gets lost. The body is more careful about this distinction, noting the hierarchy dissolves within their experimental scope, but the Abstract oversells the finding.

Wait, I'm noticing a logical tension here. If the experiments show SFT ≈ GRPO across all pruning criteria at 20-25% sparsity, then the pruning criterion isn't actually what determines whether RLVR outperforms SFT—the results are consistent regardless. So the Abstract's claim that the prior advantage is "attributable to the pruning criterion" doesn't quite align with what the experiments demonstrate.

The real difference seems to be the experimental setup itself: the prior work used unstructured magnitude pruning at much higher density (96.5% retention), while this work uses structured pruning at much lower density (20-25%). That's the actual distinction, not the criterion. The paper does acknowledge this in the Conclusion with hedging language about "within our experimental scope," but the Abstract oversimplifies the finding.

I'll note this as a concern rather than a major issue since the Abstract does use "suggest" to qualify the claim.

Now looking at the section structure, the Abstract lays out the problem and method clearly, but I need to check how the rest of the paper develops these points. The abstract continues with the technical details of RASP—how it balances gradient importance against representational diversity using Centered Kernel Alignment—and then presents the key empirical finding: across different pruning criteria, there's a spectrum of recovery capacity where diversity-preserving approaches maintain effective RL training while importance-focused ones collapse. The surprising result is that despite these dramatic differences in training behavior, both SFT and GRPO converge to nearly identical accuracy at moderate sparsity levels, which they call reward-accuracy decoupling. This pattern holds consistently across three benchmarks with some preliminary evidence of generalization across model scales and architectures. Supervised Fine-Tuning and Reinforcement Learning with Verifiable Rewards are both used to restore reasoning capabilities, though RLVR is commonly assumed superior—our findings suggest this advantage comes from the pruning criterion itself rather than an inherent property of RL. I'm proposing Recovery-Aware Structured Pruning, which uses a scoring function balancing gradient importance with representational diversity measured through Centered Kernel Alignment.

Testing this across four pruning criteria on a 7B reasoning model reveals a spectrum where diversity-preserving approaches sustain active RL training while importance-dominated ones suffer reward collapse. Interestingly, despite these stark differences in training dynamics, both SFT and GRPO achieve nearly identical downstream accuracy at moderate sparsity—a decoupling between reward signals and final performance that holds across three benchmarks. Continuing to count through the second sentence to verify the word total...

and then moving into the third point about our proposed method. We're introducing RASP, which combines gradient-based importance scoring with a diversity metric using Centered Kernel Alignment to create a more balanced pruning approach. The fourth sentence is starting to describe our experimental findings across different pruning strategies, showing that how well models recover after pruning depends heavily on whether the pruning method preserves representational diversity. I'm tallying up the word counts across these key findings—the abstract comes to around 153 words without the code availability note, well under the 200-word limit.

Now I'm mapping out how the introduction flows: it opens with background and the core problem that reasoning models need recovery after pruning, then pivots to why existing assumptions about recovery paradigms might be wrong. The second paragraph highlights the gap—that RL and SFT differ fundamentally but nobody's really examined how the optimization criterion affects recovery. Then Figure 1 shows the dose-response pattern, followed by our methodology and results, capped with the contributions. It's a tight structure that weaves the problem importance throughout rather than isolating it into its own section.

For related work, I'm organizing it thematically across three areas: how structured pruning works for LLMs, what recovery methods exist, and the dynamics of RL-based training. Each paragraph synthesizes multiple papers rather than listing them individually, which positions our work more clearly against what's come before.

On the contributions side, the first one about reward-accuracy decoupling is backed by Table 2, scatter plots, and statistical tests in section 4.3, with additional analysis in 4.4. The second contribution on recovery capacity and the RASP framework ties together the scoring methodology from 3.3 and the recovery gradient analysis from 4.1, supported by Table 1 and Figures 2-3, with the dose-response pattern showing up in the main results.

The title focuses on a single 7B model and structured MLP pruning specifically, which matches what we actually tested. The abstract mentions three benchmarks and preliminary evidence from smaller and different models, which all checks out against what's in the paper.

Now I'm verifying that the specific claims are backed up by the data. The "near-identical accuracy" language with mean differences around 0.54 percentage points and equivalence testing passing for most comparisons seems like a fair characterization. I see references to "substantially outperforming" but that's describing prior work, not our own results. The 4.55 percentage point gap between CKA-only and Standard pruning is consistent across different random seeds, and we have a Welch's t-test showing statistical significance at p=0.0009 for that comparison.

For the peak reward claim, I'm checking the numbers in Table 1 - CKA-only reaches 0.354 while Standard reaches 0.081, which gives us a ratio of about 4.37, so rounding to 4.4× is accurate.

Looking at the extended training results from Figure 5, the caption shows reward values of 0.308 versus 0.056 at step 300, which divides to exactly 5.5×.

The mean gradient magnitude comparison in the appendix confirms the 2.89× figure.

For the mean absolute delta across the four criteria at 20%, I'm calculating from Table 2's values of 0.48, 0.55, 0.61, and 0.53, which average to about 0.54 percentage points.

Now I'm verifying the claim about the maximum 1.8pp improvement across dose-response, MBPP, and MATH-500. The GSM8K deltas max out at 0.61pp, while the dose-response curve peaks at 1.14pp. MATH-500 shows the largest single improvement at 1.8pp when α=2.0. For MBPP, the standard approach gets 1.07pp, but I need to reconcile whether the 1.8pp claim is accurately capturing the maximum across all three benchmarks or if there's a specific configuration being referenced. Looking at the fine-grained results across all benchmarks, the maximum deviation is indeed 1.8pp from the MATH-500 dose-response condition at α=2.0, which aligns with the claim being made.

However, there's a credibility issue with the abstract's assertion that findings "hold across three benchmarks" — on MBPP and MATH-500, the results aren't statistically significant, so claiming they hold is overstated.

For experimental rigor, most conditions have multi-seed results providing error bars, but RASP at α=1.0 only has a single seed, which is a gap in the methodology.

The baselines are solid — they include established pruning criteria and recovery methods — though the paper frames this as a controlled study of different criteria rather than a full comparison with other end-to-end pruning pipelines, which is a reasonable design choice.

The ablations are comprehensive: they test the scoring balance parameter across a range, vary the layer floor threshold, explore different sparsity levels, check training duration effects, validate CKA calibration stability, and verify robustness across model scales, architectures, and benchmarks. This gives good confidence in the method's generalizability.

For reproducibility, the hyperparameters are documented in the appendix with learning rate, batch size, gradient accumulation, sequence length, optimizer choice, training duration, KL coefficient, temperature, generation count, reward formulation, and loss function all specified. Hardware details are clear—two RTX PRO 6000 GPUs with 94GB each—and the SFT warmup took 37 minutes. The calibration data comes from GSM8K with 512 samples, and code is available via anonymous GitHub. However, the full GRPO training time isn't explicitly reported, and while GPU-hours are tracked internally, they're not disclosed in the paper.

The paper includes both a limitations section and ethics statement as required. Regarding terminology, I'm verifying that key symbols like $I(h)$ for importance scores, $F(h)$ for functional overlap, $\alpha$ for CKA coefficients, and $S(h)$ for scoring variants are used consistently throughout. Core concepts like CKA (Centered Kernel Alignment), GRPO (Group Relative Policy Optimization), and RLVR (Reinforcement Learning with Verifiable Rewards) are all properly defined at their first mention.

I'm noticing a potential naming issue with RASP—while it's the proposed method, the α=1.0 variant actually performs poorly, which could be confusing since readers might associate the method name with suboptimal results. The paper does clarify this distinction, explaining that higher α values yield better performance, but the terminology could still create some ambiguity about which configuration represents the actual method.

Now I'm scanning through the LaTeX files for em-dash usage. I'm finding several instances where triple hyphens (---) are used to create em-dashes in the abstract and introduction sections, particularly in phrases like "recovery training---typically Supervised Fine-Tuning" and "The pruning criterion---not the recovery paradigm." I should continue checking for more of these throughout the document.

The Phase 1 source code check already flagged 7 critical and 19 warning issues, so these em-dashes have likely been caught. Since Phase 2 is supposed to focus on semantic-level issues rather than regex patterns, I'll note these but shift my attention to content quality. I'm checking for common filler words like "It is worth noting," "Notably," and "importantly," but they don't appear to be used excessively. The participial phrases I'm finding, like "ranging from active learning...through stagnation...to reward collapse," seem grammatically valid rather than stylistically problematic.

Now I'm looking at some borderline cases with participial endings—phrases like "suggesting that pruning granularity interacts with RL trainability" and "indicating that importance filtering provides complementary signal" appear in multiple sections. These aren't necessarily AI-generated patterns, but they do show up with some frequency. I'm also checking for overused vocabulary like "leverage," "delve into," and "utilize," which don't seem to be present. The paragraph lengths look reasonable overall, not fragmented or excessively padded.

For transitions between sections, there's a minor gap between the Introduction and Related Work where the contributions list just ends without an explicit bridge sentence, but the other transitions flow naturally—Related Work to Method has a clear setup, and the Experiments to Conclusion move works well with the "Whether RLVR outperforms SFT" opening. The Discussion and Conclusion section goes beyond just restating results; it introduces the "GRPO as diagnostic probe" framing and explores broader implications.

The limitations section is honest and substantive—it covers architectural constraints like being limited to Qwen2.5, diagnostic gaps where reward capacity doesn't predict accuracy, inference efficiency tradeoffs, and replication scope issues like single-seed runs and token limits. These aren't vague disclaimers but concrete boundaries on what the work can claim, though the explanation for why decoupling occurs at moderate sparsity could dig deeper into the underlying mechanisms. I'm checking for any internal information leakage in the document. The hardware specs and GitHub URL look fine, but I notice the TOST table has some suspicious seed labels like "verify" and "fair_v2" that sound like internal experiment names rather than neutral identifiers—those should probably be renamed to something more generic.

I also need to verify the page count against EMNLP 2026 requirements. The abstract is within the 200-word limit, but I should confirm whether the main text actually fits within 8 pages once I separate out the appendix and references.

The limitations section is correctly placed in the main text before the appendix, and there's no duplicate in the appendix itself. The paper also doesn't include a checklist in the PDF, which aligns with the requirement to submit that separately through OpenReview.

Let me scan through the appendix sections to make sure there's nothing else that shouldn't be there.

Now I'm noticing some specific content issues to flag. The abstract uses an em-dash in "recovery training---typically" which might have been flagged before, but there's also a semantic problem there. Looking at the TOST table more carefully, I'm seeing a discrepancy—the main text mentions three seeds (42, 123, 456) with specific percentages, but the table shows four CKA-only entries, which doesn't match up. So the sign convention differs between the two tables—the TOST table uses d = SFT - GRPO while Table 2 reports Δ = GRPO - SFT, which flips the sign. There's also a magnitude discrepancy: 0.48pp versus 0.45pp, likely because Table 2 averages across all three seeds while seed 42 alone shows 64.37% for GRPO compared to the reported 63.91% for SFT.

When I calculate the paired difference for seed 42 directly (64.37 - 63.91 = +0.46pp or -0.46pp depending on direction), it's close to the TOST value of -0.45pp. The small gap probably comes from how the paired calculation works—averaging the per-example binary differences rather than just subtracting overall accuracies—so this discrepancy is within rounding error.

Now I'm checking the "verify" entry where Δ = -0.15, which doesn't seem to match anything I've found so far.

Looking at the appendix, it mentions three GRPO seeds (42, 123, 456) with their specific accuracies, but this "verify" run appears to be a fourth seed entirely. For the Standard results, the TOST table references seed 123, seed 456, and other conditions like "fair_v2" and "ext 300", but it's missing Standard seed 42 from the reported three-seed average—instead showing these alternative conditions, which suggests some inconsistency in which runs are actually being compared.

The complication deepens because Standard seed 42 was trained from a different SFT checkpoint than seeds 123 and 456, making it not directly comparable in a paired test anyway. It looks like "fair_v2" might be a retrained version of seed 42 using the consistent SFT base, which would explain why it appears in the TOST table instead of the original seed 42. The real problem here is that these internal experiment labels—"verify," "fair_v2," "ext 300"—need to be clarified or properly renamed before publication, as it's unclear what they represent and why certain runs are substituted for others.

Now looking at the narrative consistency issue: the Abstract frames this work as challenging the "RLVR > SFT" finding from prior work, but the experiments actually show SFT and GRPO performing similarly at 20-25% sparsity regardless of the pruning criterion. The prior work's advantage came from a completely different experimental setup with unstructured pruning and 96.5% retention, so the settings don't actually overlap. The Abstract claims the advantage is "attributable to the pruning criterion," but the evidence doesn't directly demonstrate this since the conditions are fundamentally different. Though I notice the Abstract does use "suggest" to hedge, and the body text is appropriately cautious with language like "within our experimental scope."

Actually, stepping back: the paper's own Standard pruning results show GRPO only outperforming SFT by 0.55 percentage points at 20%, which is essentially equivalent. So even under importance-only pruning—the type selfhealing2025 likely used—RLVR still doesn't outperform SFT in this setting. This means the paper can't actually attribute the prior RLVR advantage to the pruning criterion, since that advantage disappears here regardless of which criterion is used. The original advantage must stem from something else entirely, like the specific task structure or model scale.

There's a real tension in the paper's narrative: it positions itself as showing that pruning criterion determines whether RLVR helps, but the data actually shows RLVR doesn't help at 20-25% structured sparsity no matter which criterion is used. The criterion affects training dynamics and spectrum, but not final accuracy—they're decoupled. This inconsistency between the framing and what the experiments actually demonstrate is something a reviewer would definitely flag.

Looking back at the introduction more carefully, the paper claims to explain why the RLVR advantage from prior work exists, attributing it to suboptimal pruning rather than a fundamental property of RL. But that doesn't hold up either—even with suboptimal pruning methods, RLVR and SFT perform similarly. The paper's actual finding is that the RLVR > SFT hierarchy from prior work simply doesn't materialize under structured pruning at these sparsity levels, regardless of which criterion is used.

The real issue is that the paper's framing around "how pruning criteria shape recovery" misses what the data actually shows: sparsity level and pruning approach matter far more than the specific criterion. At 15% there's some differentiation, but by 20-25% the criterion becomes almost irrelevant.

I'm reconsidering whether I'm being too critical here. The paper does establish that prior claims about RLVR superiority don't hold uniformly across sparsity levels, which is a valid contribution—but the causal chain between pruning criteria and recovery capacity isn't as direct as the title suggests.

The real insight is that at moderate structured sparsity, the criterion affects training dynamics without changing final accuracy, and the RLVR advantage appears setting-dependent rather than fundamental. I should frame this precisely rather than dismissing it, since the paper does acknowledge the experimental differences from prior work.

Let me now pull together the full set of critical findings.

I'm also going to scan through the tex files more carefully for em-dashes and AI-style language patterns to get a complete picture of the writing. I'm seeing em-dashes concentrated in the abstract, introduction, and method sections, which Phase 1 likely already caught. Now I'm checking for participial phrases ending sentences across the files—I'm finding several instances in introduction, method, and experiments where "-ing" constructions wrap up thoughts, like "suggesting that pruning granularity interacts with RL trainability" and "indicating that importance filtering provides complementary signal." I found about three instances of "-ing" participial endings that could be flagged. Now checking for filler language like "it is worth noting," "notably," "importantly," and "interestingly" — none of those appear, which is good. The paragraphs in the experiments section look appropriately sized, and I'm noticing the em-dashes are sometimes used for parenthetical asides where commas or actual parentheses would be clearer, like in appositive phrases.

Looking at the title, it's quite long at eighteen words — informative but potentially wordy. All figures are properly referenced, and the table captions include the necessary experimental details. One small gap is that the MBPP table doesn't include a Random baseline for comparison. Let me continue checking for any other issues I might have missed.

Scanning through the appendix, I don't see a dedicated Limitations section, which aligns with the requirements. Now I'm verifying that the scope claims in the title and abstract match what was actually tested — the abstract mentions three benchmarks (GSM8K, MATH-500, MBPP) which checks out.

I'm also noticing some problematic labels in the TOST table. Terms like "verify" and "fair_v2" appear to be internal experiment identifiers that shouldn't be in the final paper, and "ext 300" is too informal. These need cleaner names for publication.

Now checking the RASP terminology — it's used both as a family (parameterized by α) and as a specific instance (α=1.0), and I'm verifying the paper maintains this distinction consistently across the method section, experiments, and figures.

There's a structural problem though: the main comparison table shows RASP at α=1.0, which underperforms CKA-only, but the paper's actual best result is RASP at α=2.0 (66.11%), which beats CKA-only (64.39%). This best configuration only appears in the ablation table and dose-response figure, not in the primary results table, which could raise reviewer questions about why the proposed method's strongest performance isn't featured in the main comparison.

Looking at the contribution claims in the introduction, I see they mention specific performance gaps including dose-response effects across multiple benchmarks. Let me check if these numbers align with what's actually shown in the tables. 7.20pp, so the amplification is 7.20 - 5.69 = 1.51pp. ✅ That confirms it.

Now I'm putting together the full audit report. Let me think through one more thing though — the paper claims this 15% exception "reinforces" the main decoupling pattern, which seems counterintuitive at first. But the logic is that the CKA-guided advantage only emerges at lower sparsity levels, which actually supports the broader finding that decoupling holds across the main operating range of 20-25%. It's a reasonable argument, though the phrasing is a bit subtle.

I'm also recounting the abstract word-by-word to get a precise total. Looking at the full text from "Structured pruning compresses..." through the methods and results sections. I'm defining a scoring function that balances gradient importance with representational diversity using Centered Kernel Alignment. Across four pruning criteria on a 7B reasoning model, I'm seeing that diversity-preserving approaches maintain active RL training while importance-dominated ones lead to reward collapse. Interestingly, despite these different training dynamics, both SFT and GRPO achieve nearly identical downstream accuracy at moderate sparsity—what I'm calling reward-accuracy decoupling—and this pattern holds across three benchmarks with some preliminary evidence across different model scales.

Now I'm noticing a potential issue with the abstract's language. The phrasing "diversity-preserving criteria" and "importance-dominated criteria" uses plurals, but looking at the actual four pruning methods tested, only CKA-only really fits the diversity-preserving category, and the importance-dominated group seems similarly narrow. I should verify whether this plural framing accurately represents what the results actually show. a conceptual category rather than the specific four tested. That's fine.

Now let me check whether there are any orphan sections — areas of content that don't map back to the main contributions. Looking at what I've covered: the recovery capacity spectrum ties to Contribution 2, the reward-accuracy decoupling to Contribution 1, RASP's dose-response behavior to Contribution 2, the cross-sparsity experiments support both, extended training supports Contribution 2, and the cross-scale results at 1.5B support generalization claims.

The cross-model experiments with Qwen2.5-Math-7B also support generalization, the MATH-500 and MBPP benchmarks demonstrate decoupling across different domains, the CKA heatmap shows the representational diversity mechanism behind Contribution 2, and the ShortGPT comparison establishes where the decoupling effect breaks down. No orphan sections — everything connects back.

I should also verify the paper doesn't claim state-of-the-art anywhere; it frames itself as a controlled study instead, which is the right positioning. And checking the language around "significantly" — I see it used in the experiments section with proper statistical backing like p-values.

Now I'm auditing the TOST table in the appendix and noticing the labels contain internal experiment run names like "verify" and "fair_v2" that shouldn't be exposed in a final paper, along with "ext 300" which appears to reference extended training steps. These leak implementation details that should be cleaned up.

I'm also verifying the 4.4× peak reward improvement claim: dividing 0.354 by 0.081 gives 4.37, which does round to 4.4×, so that math checks out. satisfied with the verification. Now let me do one final check on Contribution 1 to make sure the reported numbers align with Table 2 — the mean absolute change should be 0.54pp with a max of 0.61pp across the four methods at 20% data. Computing the mean of the absolute values: 0.48, 0.55, 0.61, and 0.53 gives 0.5425, which rounds to 0.54pp, and the maximum is indeed 0.61pp, so that checks out.

For the broader claim about max 1.8pp including dose-response and the other benchmarks, I'm verifying that MATH-500 at α=2.0 reaches +1.8pp, MBPP peaks at 1.34pp, and dose-response maxes out around 1.14pp, confirming 1.8pp as the overall maximum across all comparisons. I'm noticing that α=2.0 and Standard are actually different pruning configurations—Standard uses α=0 (importance-only), so the matching 25.6% SFT values are just a coincidence. The numbers all check out. I'm also scanning the Discussion section to see if it just restates results, and it does repeat the key metrics like the mean and max improvements, though it also mentions the SFT warmup recovery claim.

The Discussion is fairly brief at three paragraphs—it could dig deeper into the mechanistic reasons for reward-accuracy decoupling, the theoretical implications for RL training, or how this connects to the lottery ticket hypothesis mentioned earlier. I'll note this as a minor gap. Now I'm checking whether the paper actually explains why this decoupling happens, and it seems to describe the phenomenon without providing a mechanistic explanation for it.

The closest the paper gets is suggesting that SFT warmup recovers most of the accessible accuracy and GRPO operates in a regime where reward gains don't translate to accuracy improvements because the model is already near capacity limits at this sparsity level. This reasoning is there implicitly but could be stated more directly. I'll flag this as a narrative issue worth noting.

Let me now organize all the findings into the final audit output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58bae0a4-dfb4-4140-b7f0-84772c6eafe2",
  "isSidechain": false,
  "requestId": "req_011CbP2K7EVGMk6uFXevFYwK",
  "type": "assistant",
  "uuid": "734a8bbb-b498-4a9b-90b2-6ea2b4bcea99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCiduudSvRHY9xNRcRKVQm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4322,
      "cache_read_input_tokens": 75412,
      "output_tokens": 19066,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 19066,
          "cache_read_input_tokens": 75412,
          "cache_creation_input_tokens": 4322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4322
          },
          "type": "message"
        }
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

_source line 64 · 2026-05-25T09:13:51.562Z_

现在进行逐维度深度审计。先用正则扫描补充 Phase 1 可能遗漏的 AI 风格问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "734a8bbb-b498-4a9b-90b2-6ea2b4bcea99",
  "isSidechain": false,
  "requestId": "req_011CbP2K7EVGMk6uFXevFYwK",
  "type": "assistant",
  "uuid": "6dfb7fbe-b8bc-498c-83a1-bbbda9f30ba6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCiduudSvRHY9xNRcRKVQm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4322,
      "cache_read_input_tokens": 75412,
      "output_tokens": 19066,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 19066,
          "cache_read_input_tokens": 75412,
          "cache_creation_input_tokens": 4322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4322
          },
          "type": "message"
        }
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

_source line 65 · 2026-05-25T09:13:53.746Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Qc1fkpQC9oGiHfquKz8YZW`</summary>

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
  "parentUuid": "6dfb7fbe-b8bc-498c-83a1-bbbda9f30ba6",
  "isSidechain": false,
  "requestId": "req_011CbP2K7EVGMk6uFXevFYwK",
  "type": "assistant",
  "uuid": "2f7f9fef-1da1-4195-a74e-7660512dccbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCiduudSvRHY9xNRcRKVQm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4322,
      "cache_read_input_tokens": 75412,
      "output_tokens": 19066,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 19066,
          "cache_read_input_tokens": 75412,
          "cache_creation_input_tokens": 4322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4322
          },
          "type": "message"
        }
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

_source line 66 · 2026-05-25T09:13:58.892Z_

<details><summary>↩ Tool result · `toolu_01LsuatT8Eo6HuL2Ney5znya`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:339:CKA-only & verify & $-$0.15 & 0.001 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:345:Standard & ext 300 & $-$0.08 & 0.007 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74c69d36-5989-405c-9653-c426ee364ba4",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "7d7e6028-312e-4dd9-9d7c-165b4c882b8a",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:339:CKA-only & verify & $-$0.15 & 0.001 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:345:Standard & ext 300 & $-$0.08 & 0.007 \\\\",
    "numLines": 2
  },
  "sourceToolAssistantUUID": "74c69d36-5989-405c-9653-c426ee364ba4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-25T09:13:53.769Z_

<details><summary>↩ Tool result · `toolu_01Qc1fkpQC9oGiHfquKz8YZW`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:81:This compression is consistent with two factors: MATH-500's higher intrinsic difficulty---the unpruned model achieves only 53.0\% (vs.\ 90.83\% on GSM8K)---and generation-length truncation at the 2{,}048-token evaluation limit, which affects over half of dense-model responses (Appendix~\ref{sec:appendix_math500}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:93:Under SFT alone the ordering is CKA-only $>$ \rasp{} at $\alpha{=}1.0$ $>$ Standard $>$ Random, yet the recovery capacity spectrum (Table~\ref{tab:recovery_gradient}) reverses the \rasp{} at $\alpha{=}1.0$/Standard ordering---Standard exhibits higher peak reward than \rasp{} despite lower SFT accuracy, indicating that the spectrum tracks structural properties rather than post-SFT accuracy.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:113:CKA similarity between dense and pruned representations (Figure~\ref{fig:cka_heatmap}) shows that CKA-only diverges most from the dense model ($\mu{=}0.62$), while Standard ($\mu{=}0.90$), Random ($\mu{=}0.92$), and \rasp{} at $\alpha{=}1.0$ ($\mu{=}0.88$) cluster near 1.0---preserving dense fidelity retains redundant representations at the expense of diversity.
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
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/_deprecated/table2_recovery.tex:11:CKA-only 20\% & \underline{63.91} & TBD & --- & \underline{0.354} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:84:Dose-response analysis (\S\ref{sec:sparsity_cliff}) reveals that $\alpha{=}1.0$ yields suboptimal results---exhibiting reward collapse under GRPO due to insufficient diversity weighting---while $\alpha{=}2.0$ achieves peak recovery.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex:1:% Limitations --- required by ACL/EMNLP
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex:1:Structured pruning compresses reasoning Large Language Models (LLMs) by removing redundant components from their feed-forward sub-layers, but the pruned model requires recovery training---typically Supervised Fine-Tuning (SFT) or Reinforcement Learning with Verifiable Rewards (RLVR)---to restore reasoning capabilities.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex:5:Despite this stark divergence in training dynamics, SFT and GRPO yield near-identical downstream accuracy at moderate sparsity---a phenomenon we term \emph{reward-accuracy decoupling}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:310:0.4 (default) & 64.37 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:359:The decoupling pattern suggests that GRPO may serve as a \emph{diagnostic probe} for pruning quality at moderate sparsity: reward trajectories appear to indicate whether the pruned architecture retains sufficient diversity for RL exploration---information not accessible through SFT, which converges to similar accuracy at 20--25\% MLP sparsity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:364:Our findings complement \citet{selfhealing2025}: while they demonstrate RLVR superiority for unstructured magnitude pruning at 96.5\% retention, within our experimental scope (20--25\% structured MLP sparsity on Qwen2.5-family models), this hierarchy dissolves under diversity-preserving pruning---the gap appears attributable to the pruning criterion rather than a fundamental property of RL recovery.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:8:The pruning criterion---not the recovery paradigm---appears to be the primary determinant of post-pruning reasoning quality.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:9:Since RL optimizes reward as a proxy for task performance, one would expect reward improvements to translate into accuracy gains---making their divergence noteworthy.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:24:Under GRPO~\citep{shao2024grpo} training, four criteria produce a \textbf{recovery capacity spectrum}---a gradient in the pruned model's ability to regain reasoning through post-hoc training---ranging from active learning (CKA-only, peak reward 4.4$\times$ Standard) through stagnation (Random) to reward collapse (\rasp{} at $\alpha{=}1.0$), that tracks preserved representational diversity rather than gradient importance.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:30:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f7f9fef-1da1-4195-a74e-7660512dccbc",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "0e21bef7-9c6c-4090-9e08-f96d2812530d",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:14:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:81:This compression is consistent with two factors: MATH-500's higher intrinsic difficulty---the unpruned model achieves only 53.0\\% (vs.\\ 90.83\\% on GSM8K)---and generation-length truncation at the 2{,}048-token evaluation limit, which affects over half of dense-model responses (Appendix~\\ref{sec:appendix_math500}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:93:Under SFT alone the ordering is CKA-only $>$ \\rasp{} at $\\alpha{=}1.0$ $>$ Standard $>$ Random, yet the recovery capacity spectrum (Table~\\ref{tab:recovery_gradient}) reverses the \\rasp{} at $\\alpha{=}1.0$/Standard ordering---Standard exhibits higher peak reward than \\rasp{} despite lower SFT accuracy, indicating that the spectrum tracks structural properties rather than post-SFT accuracy.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:113:CKA similarity between dense and pruned representations (Figure~\\ref{fig:cka_heatmap}) shows that CKA-only diverges most from the dense model ($\\mu{=}0.62$), while Standard ($\\mu{=}0.90$), Random ($\\mu{=}0.92$), and \\rasp{} at $\\alpha{=}1.0$ ($\\mu{=}0.88$) cluster near 1.0---preserving dense fidelity retains redundant representations at the expense of diversity.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:7:Structured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:11:ShortGPT~\\citep{shortgpt2024} and SliceGPT~\\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:25:This establishes RLVR as the preferred recovery paradigm for reasoning models, but Self-Healing treats the pruning method as a black box and tests only one compression ratio---it does not study whether the \\emph{choice} of what to prune affects how well RLVR can recover.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:28:PASER~\\citep{paser2025} optimizes which recovery \\emph{data} to use through manifold learning and capability-aware budget allocation---complementary to RASP, which optimizes which \\emph{structures} to prune for recoverability.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:39:This asymmetry provides the theoretical foundation for RASP---structures with high functional overlap are more amenable to RLVR's redistribution mechanism, as their function can be absorbed by similar retained structures during global policy optimization, whereas SFT's trajectory-imitation objective cannot achieve such redistribution.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:47:In contrast, RASP uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability under RLVR---a finer granularity (width vs.\\ depth pruning) optimizing for a different objective (post-recovery reasoning performance vs.\\ immediate accuracy preservation).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:5:The core insight is that structures with high functional overlap---those whose computations are redundant with other retained structures---are more recoverable under RLVR, because reinforcement learning can redistribute their function through global exploration~\\citep{rlsqueezes2026}.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:11:Given a pretrained transformer $\\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units---attention heads or MLP channels---to reduce model size while maintaining hardware-friendly dense computation.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:58:Unlike prior work that uses inter-layer CKA to identify globally redundant layers for depth pruning~\\citep{mpruner2024,lachance2024cka}, RASP uses \\emph{intra-layer} CKA between individual GQA groups to predict per-structure recoverability---a fundamentally different granularity and objective.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:78:The key distinction from standard pruning---which ranks solely by $I(h)$---is that RASP additionally down-weights protection of structures whose function overlaps with retained structures.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:93:Structures with high functional overlap $F(h)$ are precisely those whose function can be absorbed by similar retained structures through RLVR's global optimization---the theoretical basis for RASP's scoring criterion.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:4:Large language models with reasoning capabilities---such as those trained with Reinforcement Learning with Verifiable Rewards (RLVR)---achieve strong performance on mathematical and logical tasks but incur substantial deployment costs due to their parameter counts and the extended chain-of-thought traces they generate~\\citep{shao2024grpo}.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:11:No prior work has studied whether the \\emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning ability---or whether this pruning-recovery interaction differs when recovery uses SFT instead of RLVR.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:16:RLVR's recovery mechanism---global exploration across the policy space---can redistribute the function of a removed structure to other structures that perform similar computations.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:19:We hypothesize that functional redundancy, measured as intra-layer representational similarity via Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}), positively predicts RLVR recoverability but is a weaker predictor of SFT recoverability---since SFT's trajectory-imitation objective cannot redistribute function through global exploration.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:29:Unlike prior CKA-based pruning methods that use inter-layer similarity to identify globally redundant layers for depth pruning~\\citep{mpruner2024,lachance2024cka}, RASP uses intra-layer CKA between individual structures (attention head groups, MLP channels) to predict per-structure recoverability under a specific recovery paradigm---a finer granularity optimizing for a fundamentally different objective.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:31:This work extends the notion of trainability from the Lottery Ticket Hypothesis~\\citep{frankle2019lth}---which asks which subnetworks can be effectively trained---to what we term \\emph{paradigm-conditioned prunability}: the optimal set of structures to retain depends not only on the task but on the recovery paradigm, as RLVR and SFT impose fundamentally different requirements on the retained architecture.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex:12:\\multicolumn{4}{l}{\\textit{20\\% sparsity --- method comparison}} \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex:18:\\multicolumn{4}{l}{\\textit{20\\% sparsity --- $\\alpha$ dose-response}} \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/_deprecated/table2_recovery.tex:11:CKA-only 20\\% & \\underline{63.91} & TBD & --- & \\underline{0.354} \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:84:Dose-response analysis (\\S\\ref{sec:sparsity_cliff}) reveals that $\\alpha{=}1.0$ yields suboptimal results---exhibiting reward collapse under GRPO due to insufficient diversity weighting---while $\\alpha{=}2.0$ achieves peak recovery.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex:1:% Limitations --- required by ACL/EMNLP\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex:1:Structured pruning compresses reasoning Large Language Models (LLMs) by removing redundant components from their feed-forward sub-layers, but the pruned model requires recovery training---typically Supervised Fine-Tuning (SFT) or Reinforcement Learning with Verifiable Rewards (RLVR)---to restore reasoning capabilities.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex:5:Despite this stark divergence in training dynamics, SFT and GRPO yield near-identical downstream accuracy at moderate sparsity---a phenomenon we term \\emph{reward-accuracy decoupling}.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:310:0.4 (default) & 64.37 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:359:The decoupling pattern suggests that GRPO may serve as a \\emph{diagnostic probe} for pruning quality at moderate sparsity: reward trajectories appear to indicate whether the pruned architecture retains sufficient diversity for RL exploration---information not accessible through SFT, which converges to similar accuracy at 20--25\\% MLP sparsity.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:364:Our findings complement \\citet{selfhealing2025}: while they demonstrate RLVR superiority for unstructured magnitude pruning at 96.5\\% retention, within our experimental scope (20--25\\% structured MLP sparsity on Qwen2.5-family models), this hierarchy dissolves under diversity-preserving pruning---the gap appears attributable to the pruning criterion rather than a fundamental property of RL recovery.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:8:The pruning criterion---not the recovery paradigm---appears to be the primary determinant of post-pruning reasoning quality.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:9:Since RL optimizes reward as a proxy for task performance, one would expect reward improvements to translate into accuracy gains---making their divergence noteworthy.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:24:Under GRPO~\\citep{shao2024grpo} training, four criteria produce a \\textbf{recovery capacity spectrum}---a gradient in the pruned model's ability to regain reasoning through post-hoc training---ranging from active learning (CKA-only, peak reward 4.4$\\times$ Standard) through stagnation (Random) to reward collapse (\\rasp{} at $\\alpha{=}1.0$), that tracks preserved representational diversity rather than gradient importance.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:30:[Omitted long matching line]",
    "numLines": 35
  },
  "sourceToolAssistantUUID": "2f7f9fef-1da1-4195-a74e-7660512dccbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-25T09:13:55.786Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Xm1pFTauTh4Q857mYcc4G6`</summary>

```json
{
  "pattern": ", (suggesting|indicating|demonstrating|highlighting|showing|confirming|revealing|enabling|ensuring|allowing|making|resulting)",
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
  "parentUuid": "0e21bef7-9c6c-4090-9e08-f96d2812530d",
  "isSidechain": false,
  "requestId": "req_011CbP2K7EVGMk6uFXevFYwK",
  "type": "assistant",
  "uuid": "aa7fee54-2b6d-4a7b-b4e9-f31a9992eba1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCiduudSvRHY9xNRcRKVQm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4322,
      "cache_read_input_tokens": 75412,
      "output_tokens": 19066,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 19066,
          "cache_read_input_tokens": 75412,
          "cache_creation_input_tokens": 4322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4322
          },
          "type": "message"
        }
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

_source line 69 · 2026-05-25T09:13:55.803Z_

<details><summary>↩ Tool result · `toolu_01Xm1pFTauTh4Q857mYcc4G6`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:13:Under fine-grained structural pruning at 20--25\% sparsity, our controlled experiments indicate that this advantage diminishes when pruning preserves representational diversity, suggesting the effect is attributable to the pruning criterion rather than to RL itself.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:44:All methods use \texttt{max\_completion\_length}{$=$}1{,}024 except Random (TRL default 512), making it a conservative comparison point.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:93:Under SFT alone the ordering is CKA-only $>$ \rasp{} at $\alpha{=}1.0$ $>$ Standard $>$ Random, yet the recovery capacity spectrum (Table~\ref{tab:recovery_gradient}) reverses the \rasp{} at $\alpha{=}1.0$/Standard ordering---Standard exhibits higher peak reward than \rasp{} despite lower SFT accuracy, indicating that the spectrum tracks structural properties rather than post-SFT accuracy.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:125:Extending GRPO from 100 to 300 steps (Figure~\ref{fig:extended_training}; Appendix~\ref{sec:appendix_extended}), Standard shows no net improvement (reward 0.054--0.058, $f_0 > 0.5$ throughout), while CKA-only sustains a 5.5$\times$ gap (0.308 vs 0.056 at step 300), suggesting the gap is structural rather than a matter of training budget.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:16:\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, suggesting that \emph{which} structures are removed critically shapes recovery potential.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:9:This model represents a compelling testbed for our study: as a reasoning-specialized model, its performance depends critically on chain-of-thought capabilities that are acquired through reinforcement learning, making the interaction between structural pruning and RL-based recovery particularly salient.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:79:This is motivated by the finding that RLVR recovers through global exploration and path compression~\citep{rlsqueezes2026}, making high-overlap structures more amenable to functional redistribution than unique structures of equivalent importance.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:81:Attention GQA groups and MLP channel groups are scored jointly and ranked in a unified list, enabling cross-component pruning decisions.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:13:The absence is surprising given that RLVR and SFT impose fundamentally different functional demands on the retained architecture: \citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation, suggesting the optimal set of structures to retain should depend on the recovery paradigm.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:87:At the empirically optimal $\alpha{=}2.0$, the diversity term $(1{-}F(h))^2$ dominates the score, making \rasp{} at $\alpha{=}2.0$ effectively CKA-guided with importance as a secondary filter (\S\ref{sec:sparsity_cliff}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:88:Nevertheless, \rasp{} at $\alpha{=}2.0$ outperforms CKA-only under both recovery paradigms (GRPO: 66.11\% vs.\ 64.39\%, $+$1.72\,pp; SFT: 64.97\% vs.\ 63.91\%, $+$1.06\,pp; Table~\ref{tab:alpha}), indicating that importance filtering provides complementary signal beyond diversity preservation alone.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:111:After pruning, all four models undergo identical two-stage recovery: (1)~a brief SFT warmup on chain-of-thought demonstrations restores end-of-sequence generation and format compliance (pruning disrupts termination behavior, making direct GRPO infeasible); (2)~GRPO with binary reward enables RL-based exploration, redistributing functionality across remaining structures~\citep{rlsqueezes2026}, in contrast to SFT which imitates fixed trajectories.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:86:CKA-only and Standard show identical throughput (58.3 vs 58.2 tok/s), confirming that the pruning criterion affects recovery capacity but not inference speed at matched sparsity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:96:$\alpha{=}3.0$ (SFT 64.14\%, GRPO 63.46\%, $\Delta{=}{-}0.68$\,pp) excludes a plateau hypothesis: accuracy drops 2.65\,pp from the $\alpha{=}2.0$ peak, confirming that the optimum is a true peak rather than a saturation regime.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:116:CKA-only also produces more efficient reasoning: only 22\% of completions are truncated at the 2{,}048-token limit (mean 655 tokens) versus Standard's 44\% (mean 1{,}128 tokens), indicating that the preserved structure enables shorter reasoning chains rather than longer ones.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:133:CKA-based structure rankings are highly stable across calibration data volumes: Spearman $\rho$ between rankings from 256, 512, and 1024 calibration samples ranges from 0.964 to 0.979, indicating that the scoring criterion is not sensitive to calibration set size.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:200:All three seeds satisfy GRPO $\leq$ SFT ($\Delta{=}{-}0.68$, $-$0.53, $-$0.38\,pp), confirming that reward-accuracy decoupling is reproducible across seeds even for stagnating methods.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:263:EOS rates remain below 40\% for both methods, indicating that SFT warmup is less effective on this architecture; GRPO validation is deferred to future work.\footnote{Preliminary GRPO evaluation yields 48.60\% (243/500), but 83.8\% of responses were truncated at 2048 tokens, precluding direct comparison with SFT results.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:286:    \caption{KL divergence between the policy and reference model during GRPO training. RASP maintains near-zero KL ($<$0.001), consistent with minimal policy movement during collapse. Random shows the highest KL (${\sim}$0.004--0.005), indicating more policy exploration. CKA-only and Standard fall between these extremes.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:294:Both SFT (${\sim}$10\%) and GRPO (${\sim}$8\%) accuracy are near chance (early-stopped at $N{\approx}50$--88 samples due to conclusive results), confirming that naive depth ordering cannot substitute for criterion-based structure selection.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:350:We select $\varepsilon{=}2$\,pp because it is approximately $4\times$ the observed cross-seed standard deviation ($\sigma{=}0.19$\,pp for CKA-only at 20\% sparsity), ensuring the margin reflects meaningful practical differences rather than measurement noise.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:360:At 15\% sparsity, GRPO amplifies the CKA-guided advantage ($+$1.51\,pp), suggesting the transition boundary warrants future investigation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:25:A depth pruning baseline (ShortGPT;~\citealp{shortgpt2024}) is the only method with $|\Delta| > 1$\,pp on GSM8K ($-$1.36\,pp), suggesting that pruning granularity interacts with RL trainability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa7fee54-2b6d-4a7b-b4e9-f31a9992eba1",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "e34e8052-7f5c-4c8b-a246-43bf84261473",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex:13:Under fine-grained structural pruning at 20--25\\% sparsity, our controlled experiments indicate that this advantage diminishes when pruning preserves representational diversity, suggesting the effect is attributable to the pruning criterion rather than to RL itself.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:44:All methods use \\texttt{max\\_completion\\_length}{$=$}1{,}024 except Random (TRL default 512), making it a conservative comparison point.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:93:Under SFT alone the ordering is CKA-only $>$ \\rasp{} at $\\alpha{=}1.0$ $>$ Standard $>$ Random, yet the recovery capacity spectrum (Table~\\ref{tab:recovery_gradient}) reverses the \\rasp{} at $\\alpha{=}1.0$/Standard ordering---Standard exhibits higher peak reward than \\rasp{} despite lower SFT accuracy, indicating that the spectrum tracks structural properties rather than post-SFT accuracy.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex:125:Extending GRPO from 100 to 300 steps (Figure~\\ref{fig:extended_training}; Appendix~\\ref{sec:appendix_extended}), Standard shows no net improvement (reward 0.054--0.058, $f_0 > 0.5$ throughout), while CKA-only sustains a 5.5$\\times$ gap (0.308 vs 0.056 at step 300), suggesting the gap is structural rather than a matter of training budget.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/related_work.tex:16:\\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, suggesting that \\emph{which} structures are removed critically shapes recovery potential.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:9:This model represents a compelling testbed for our study: as a reasoning-specialized model, its performance depends critically on chain-of-thought capabilities that are acquired through reinforcement learning, making the interaction between structural pruning and RL-based recovery particularly salient.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:79:This is motivated by the finding that RLVR recovers through global exploration and path compression~\\citep{rlsqueezes2026}, making high-overlap structures more amenable to functional redistribution than unique structures of equivalent importance.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:81:Attention GQA groups and MLP channel groups are scored jointly and ranked in a unified list, enabling cross-component pruning decisions.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/introduction.tex:13:The absence is surprising given that RLVR and SFT impose fundamentally different functional demands on the retained architecture: \\citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation, suggesting the optimal set of structures to retain should depend on the recovery paradigm.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:87:At the empirically optimal $\\alpha{=}2.0$, the diversity term $(1{-}F(h))^2$ dominates the score, making \\rasp{} at $\\alpha{=}2.0$ effectively CKA-guided with importance as a secondary filter (\\S\\ref{sec:sparsity_cliff}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:88:Nevertheless, \\rasp{} at $\\alpha{=}2.0$ outperforms CKA-only under both recovery paradigms (GRPO: 66.11\\% vs.\\ 64.39\\%, $+$1.72\\,pp; SFT: 64.97\\% vs.\\ 63.91\\%, $+$1.06\\,pp; Table~\\ref{tab:alpha}), indicating that importance filtering provides complementary signal beyond diversity preservation alone.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex:111:After pruning, all four models undergo identical two-stage recovery: (1)~a brief SFT warmup on chain-of-thought demonstrations restores end-of-sequence generation and format compliance (pruning disrupts termination behavior, making direct GRPO infeasible); (2)~GRPO with binary reward enables RL-based exploration, redistributing functionality across remaining structures~\\citep{rlsqueezes2026}, in contrast to SFT which imitates fixed trajectories.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:86:CKA-only and Standard show identical throughput (58.3 vs 58.2 tok/s), confirming that the pruning criterion affects recovery capacity but not inference speed at matched sparsity.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:96:$\\alpha{=}3.0$ (SFT 64.14\\%, GRPO 63.46\\%, $\\Delta{=}{-}0.68$\\,pp) excludes a plateau hypothesis: accuracy drops 2.65\\,pp from the $\\alpha{=}2.0$ peak, confirming that the optimum is a true peak rather than a saturation regime.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:116:CKA-only also produces more efficient reasoning: only 22\\% of completions are truncated at the 2{,}048-token limit (mean 655 tokens) versus Standard's 44\\% (mean 1{,}128 tokens), indicating that the preserved structure enables shorter reasoning chains rather than longer ones.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:133:CKA-based structure rankings are highly stable across calibration data volumes: Spearman $\\rho$ between rankings from 256, 512, and 1024 calibration samples ranges from 0.964 to 0.979, indicating that the scoring criterion is not sensitive to calibration set size.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:200:All three seeds satisfy GRPO $\\leq$ SFT ($\\Delta{=}{-}0.68$, $-$0.53, $-$0.38\\,pp), confirming that reward-accuracy decoupling is reproducible across seeds even for stagnating methods.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:263:EOS rates remain below 40\\% for both methods, indicating that SFT warmup is less effective on this architecture; GRPO validation is deferred to future work.\\footnote{Preliminary GRPO evaluation yields 48.60\\% (243/500), but 83.8\\% of responses were truncated at 2048 tokens, precluding direct comparison with SFT results.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:286:    \\caption{KL divergence between the policy and reference model during GRPO training. RASP maintains near-zero KL ($<$0.001), consistent with minimal policy movement during collapse. Random shows the highest KL (${\\sim}$0.004--0.005), indicating more policy exploration. CKA-only and Standard fall between these extremes.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:294:Both SFT (${\\sim}$10\\%) and GRPO (${\\sim}$8\\%) accuracy are near chance (early-stopped at $N{\\approx}50$--88 samples due to conclusive results), confirming that naive depth ordering cannot substitute for criterion-based structure selection.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:350:We select $\\varepsilon{=}2$\\,pp because it is approximately $4\\times$ the observed cross-seed standard deviation ($\\sigma{=}0.19$\\,pp for CKA-only at 20\\% sparsity), ensuring the margin reflects meaningful practical differences rather than measurement noise.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex:360:At 15\\% sparsity, GRPO amplifies the CKA-guided advantage ($+$1.51\\,pp), suggesting the transition boundary warrants future investigation.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex:25:A depth pruning baseline (ShortGPT;~\\citealp{shortgpt2024}) is the only method with $|\\Delta| > 1$\\,pp on GSM8K ($-$1.36\\,pp), suggesting that pruning granularity interacts with RL trainability.",
    "numLines": 23
  },
  "sourceToolAssistantUUID": "aa7fee54-2b6d-4a7b-b4e9-f31a9992eba1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-25T09:13:58.100Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017TA5akcAqDYdR96KvKpjdn`</summary>

```json
{
  "pattern": "(it is worth noting|notably|importantly|furthermore|moreover|additionally|delve|leverage|utilize|a myriad|a plethora|in the realm of)",
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
  "parentUuid": "e34e8052-7f5c-4c8b-a246-43bf84261473",
  "isSidechain": false,
  "requestId": "req_011CbP2K7EVGMk6uFXevFYwK",
  "type": "assistant",
  "uuid": "5d267e5f-06ec-41f2-a33e-ce7a0f013668",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCiduudSvRHY9xNRcRKVQm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4322,
      "cache_read_input_tokens": 75412,
      "output_tokens": 19066,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 19066,
          "cache_read_input_tokens": 75412,
          "cache_creation_input_tokens": 4322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4322
          },
          "type": "message"
        }
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

_source line 71 · 2026-05-25T09:13:58.122Z_

<details><summary>↩ Tool result · `toolu_017TA5akcAqDYdR96KvKpjdn`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:48:\textbf{[Phase 2: We additionally compare SFT recovery using the same GSM8K training data to isolate the effect of the RL-based recovery signal.]}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:69:\textbf{[Phase 2: We additionally report perplexity on WikiText-2 and per-benchmark accuracy on MMLU, HumanEval, and LongBench.]}
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:78:The key distinction from standard pruning---which ranks solely by $I(h)$---is that RASP additionally down-weights protection of structures whose function overlaps with retained structures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d267e5f-06ec-41f2-a33e-ce7a0f013668",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "b17bc082-452f-4ada-9637-4e3e15c1b14c",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:48:\\textbf{[Phase 2: We additionally compare SFT recovery using the same GSM8K training data to isolate the effect of the RL-based recovery signal.]}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/experiments.tex:69:\\textbf{[Phase 2: We additionally report perplexity on WikiText-2 and per-benchmark accuracy on MMLU, HumanEval, and LongBench.]}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/backup/method.tex:78:The key distinction from standard pruning---which ranks solely by $I(h)$---is that RASP additionally down-weights protection of structures whose function overlaps with retained structures.",
    "numLines": 3
  },
  "sourceToolAssistantUUID": "5d267e5f-06ec-41f2-a33e-ce7a0f013668",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-25T09:13:58.861Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LsuatT8Eo6HuL2Ney5znya`</summary>

```json
{
  "pattern": "verify|fair_v2|ext.300",
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
  "parentUuid": "b17bc082-452f-4ada-9637-4e3e15c1b14c",
  "isSidechain": false,
  "requestId": "req_011CbP2K7EVGMk6uFXevFYwK",
  "type": "assistant",
  "uuid": "74c69d36-5989-405c-9653-c426ee364ba4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCiduudSvRHY9xNRcRKVQm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4322,
      "cache_read_input_tokens": 75412,
      "output_tokens": 19066,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 19066,
          "cache_read_input_tokens": 75412,
          "cache_creation_input_tokens": 4322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4322
          },
          "type": "message"
        }
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

_source line 73 · 2026-05-25T09:13:58.953Z_

```json
{
  "parentUuid": "7d7e6028-312e-4dd9-9d7c-165b4c882b8a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6174179f-7b8c-4c51-b5f1-0afa1174dff3",
  "timestamp": "2026-05-25T09:13:58.953Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
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
  "lastPrompt": "项目：recovery_aware_struct_prune Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 7 critical,…",
  "leafUuid": "6174179f-7b8c-4c51-b5f1-0afa1174dff3",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033"
}
```

---

### Runtime record

_source line 75_

```json
{
  "type": "ai-title",
  "aiTitle": "Recovery-aware structural pruning paper review",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033"
}
```

---

### Assistant

_source line 76 · 2026-05-25T09:14:02.540Z_

<details><summary>Logged reasoning block</summary>

```text
Let me also search for "fair_v2" which I saw in my earlier reading of the TOST table:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6174179f-7b8c-4c51-b5f1-0afa1174dff3",
  "isSidechain": false,
  "requestId": "req_011CbP2nCTXBErFYPbeoHx8T",
  "type": "assistant",
  "uuid": "dce89d4b-b173-479b-a5a4-c7d5307f0702",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBDEesYo1ZVv7RaKq5erU1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25911,
      "cache_read_input_tokens": 79734,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 79734,
          "cache_creation_input_tokens": 25911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25911
          },
          "type": "message"
        }
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

_source line 77 · 2026-05-25T09:14:03.569Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017gXHVzH4FrwHfbkKnCAKrt`</summary>

```json
{
  "pattern": "fair",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dce89d4b-b173-479b-a5a4-c7d5307f0702",
  "isSidechain": false,
  "requestId": "req_011CbP2nCTXBErFYPbeoHx8T",
  "type": "assistant",
  "uuid": "7a2f8659-2ebb-4ec6-914a-94f817802e4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBDEesYo1ZVv7RaKq5erU1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25911,
      "cache_read_input_tokens": 79734,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 79734,
          "cache_creation_input_tokens": 25911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25911
          },
          "type": "message"
        }
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

_source line 78 · 2026-05-25T09:14:03.585Z_

<details><summary>↩ Tool result · `toolu_017gXHVzH4FrwHfbkKnCAKrt`</summary>

```text
344:Standard & fair\_v2 & $-$0.23 & 0.010 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a2f8659-2ebb-4ec6-914a-94f817802e4e",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "dbd8b545-ce6e-41f5-9df0-2ebc47ce0a2a",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "344:Standard & fair\\_v2 & $-$0.23 & 0.010 \\\\",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "7a2f8659-2ebb-4ec6-914a-94f817802e4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-25T09:14:04.100Z_

<details><summary>↩ Tool result · `toolu_0156KrYAwKMSjqkYqhn8zZxE`</summary>

```text
325	To formally assess whether SFT and GRPO produce equivalent GSM8K accuracy, we apply Two One-Sided Tests (TOST) on $N{=}1{,}319$ paired per-example outcomes for CKA-only and Standard at 20\% sparsity across multiple GRPO seeds.
326	For each pair, $d_i = \mathbb{1}[\text{SFT correct}]_i - \mathbb{1}[\text{GRPO correct}]_i$, and we test $H_0$: $|\bar{d}| \geq \varepsilon$ against $H_A$: $|\bar{d}| < \varepsilon$.
327	
328	\begin{table}[h]
329	\centering
330	\small
331	\caption{TOST equivalence results ($\varepsilon{=}2$\,pp). All observed $|\Delta|{<}1$\,pp.}
332	\label{tab:tost}
333	\begin{tabular}{@{}llrr@{}}
334	\toprule
335	Criterion & GRPO seed & $\Delta$ (pp) & $p_\text{TOST}$ \\
336	\midrule
337	CKA-only & seed 42 & $-$0.45 & 0.008 \\
338	CKA-only & seed 123 & $-$0.30 & 0.005 \\
339	CKA-only & verify & $-$0.15 & 0.001 \\
340	CKA-only & seed 456 & $-$0.68 & 0.023 \\
341	\midrule
342	Standard & seed 123 & $-$0.68 & 0.020 \\
343	Standard & seed 456 & $-$0.99 & 0.069 \\
344	Standard & fair\_v2 & $-$0.23 & 0.010 \\
345	Standard & ext 300 & $-$0.08 & 0.007 \\
346	\bottomrule
347	\end{tabular}
348	\end{table}
349	
350	We select $\varepsilon{=}2$\,pp because it is approximately $4\times$ the observed cross-seed standard deviation ($\sigma{=}0.19$\,pp for CKA-only at 20\% sparsity), ensuring the margin reflects meaningful practical differences rather than measurement noise.
351	At $\varepsilon{=}2$\,pp, 7/8 comparisons reject the null ($p{<}0.05$); the remaining pair (Standard vs.\ seed 456, $\Delta{=}{-}0.99$\,pp) is borderline ($p{=}0.069$).
352	At $\varepsilon{=}3$\,pp, all 8/8 are significant ($p{<}0.002$).
353	At $\varepsilon{=}1$\,pp, statistical power is insufficient with binary outcomes at $N{=}1{,}319$.
354	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03f41767-b1fd-46af-a8bf-310f3f56b878",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "37a6e05d-12b3-4171-bca5-4230110a1fdd",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex",
      "content": "To formally assess whether SFT and GRPO produce equivalent GSM8K accuracy, we apply Two One-Sided Tests (TOST) on $N{=}1{,}319$ paired per-example outcomes for CKA-only and Standard at 20\\% sparsity across multiple GRPO seeds.\nFor each pair, $d_i = \\mathbb{1}[\\text{SFT correct}]_i - \\mathbb{1}[\\text{GRPO correct}]_i$, and we test $H_0$: $|\\bar{d}| \\geq \\varepsilon$ against $H_A$: $|\\bar{d}| < \\varepsilon$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST equivalence results ($\\varepsilon{=}2$\\,pp). All observed $|\\Delta|{<}1$\\,pp.}\n\\label{tab:tost}\n\\begin{tabular}{@{}llrr@{}}\n\\toprule\nCriterion & GRPO seed & $\\Delta$ (pp) & $p_\\text{TOST}$ \\\\\n\\midrule\nCKA-only & seed 42 & $-$0.45 & 0.008 \\\\\nCKA-only & seed 123 & $-$0.30 & 0.005 \\\\\nCKA-only & verify & $-$0.15 & 0.001 \\\\\nCKA-only & seed 456 & $-$0.68 & 0.023 \\\\\n\\midrule\nStandard & seed 123 & $-$0.68 & 0.020 \\\\\nStandard & seed 456 & $-$0.99 & 0.069 \\\\\nStandard & fair\\_v2 & $-$0.23 & 0.010 \\\\\nStandard & ext 300 & $-$0.08 & 0.007 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe select $\\varepsilon{=}2$\\,pp because it is approximately $4\\times$ the observed cross-seed standard deviation ($\\sigma{=}0.19$\\,pp for CKA-only at 20\\% sparsity), ensuring the margin reflects meaningful practical differences rather than measurement noise.\nAt $\\varepsilon{=}2$\\,pp, 7/8 comparisons reject the null ($p{<}0.05$); the remaining pair (Standard vs.\\ seed 456, $\\Delta{=}{-}0.99$\\,pp) is borderline ($p{=}0.069$).\nAt $\\varepsilon{=}3$\\,pp, all 8/8 are significant ($p{<}0.002$).\nAt $\\varepsilon{=}1$\\,pp, statistical power is insufficient with binary outcomes at $N{=}1{,}319$.\n",
      "numLines": 30,
      "startLine": 325,
      "totalLines": 375
    }
  },
  "sourceToolAssistantUUID": "03f41767-b1fd-46af-a8bf-310f3f56b878",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-25T09:14:04.085Z_

<details open><summary>🔧 Tool call — Read · `toolu_0156KrYAwKMSjqkYqhn8zZxE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex",
  "offset": 325,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbd8b545-ce6e-41f5-9df0-2ebc47ce0a2a",
  "isSidechain": false,
  "requestId": "req_011CbP2nCTXBErFYPbeoHx8T",
  "type": "assistant",
  "uuid": "03f41767-b1fd-46af-a8bf-310f3f56b878",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBDEesYo1ZVv7RaKq5erU1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25911,
      "cache_read_input_tokens": 79734,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 79734,
          "cache_creation_input_tokens": 25911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25911
          },
          "type": "message"
        }
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

_source line 81 · 2026-05-25T09:14:07.423Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check if the conclusion.tex content in the main text is duplicated in appendix.tex (I noticed the appendix has some "Discussion" text). Let me verify.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37a6e05d-12b3-4171-bca5-4230110a1fdd",
  "isSidechain": false,
  "requestId": "req_011CbP2nabHcaUbbnbrnTCv9",
  "type": "assistant",
  "uuid": "8d03dc74-fe04-40b7-87ce-ed105043a96b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JgTPkMg7SuzvRfvwJCtNJg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1162,
      "cache_read_input_tokens": 105645,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1162,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 200,
          "cache_read_input_tokens": 105645,
          "cache_creation_input_tokens": 1162,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1162
          },
          "type": "message"
        }
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

_source line 82 · 2026-05-25T09:14:07.935Z_

Now let me check if conclusion.tex and appendix.tex have duplicated Discussion content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d03dc74-fe04-40b7-87ce-ed105043a96b",
  "isSidechain": false,
  "requestId": "req_011CbP2nabHcaUbbnbrnTCv9",
  "type": "assistant",
  "uuid": "091cc019-5abe-467e-9133-446a00ba9201",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JgTPkMg7SuzvRfvwJCtNJg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1162,
      "cache_read_input_tokens": 105645,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1162,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 200,
          "cache_read_input_tokens": 105645,
          "cache_creation_input_tokens": 1162,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1162
          },
          "type": "message"
        }
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

_source line 83 · 2026-05-25T09:14:08.820Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XmrUCNNG7Z1v1LQtqYA67S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex",
  "offset": 355,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "091cc019-5abe-467e-9133-446a00ba9201",
  "isSidechain": false,
  "requestId": "req_011CbP2nabHcaUbbnbrnTCv9",
  "type": "assistant",
  "uuid": "2f41b2ac-031c-4614-9584-3d275d09a09b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JgTPkMg7SuzvRfvwJCtNJg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1162,
      "cache_read_input_tokens": 105645,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1162,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 200,
          "cache_read_input_tokens": 105645,
          "cache_creation_input_tokens": 1162,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1162
          },
          "type": "message"
        }
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

_source line 84 · 2026-05-25T09:14:08.849Z_

<details><summary>↩ Tool result · `toolu_01XmrUCNNG7Z1v1LQtqYA67S`</summary>

```text
355	\section{Discussion}
356	\label{sec:appendix_discussion}
357	
358	\paragraph{GRPO as diagnostic probe.}
359	The decoupling pattern suggests that GRPO may serve as a \emph{diagnostic probe} for pruning quality at moderate sparsity: reward trajectories appear to indicate whether the pruned architecture retains sufficient diversity for RL exploration---information not accessible through SFT, which converges to similar accuracy at 20--25\% MLP sparsity.
360	At 15\% sparsity, GRPO amplifies the CKA-guided advantage ($+$1.51\,pp), suggesting the transition boundary warrants future investigation.
361	
362	\paragraph{Implications.}
363	For deployment pipelines that include post-pruning RL, diversity-preserving criteria (CKA-only or high-$\alpha$ \rasp{}) should be preferred.
364	Our findings complement \citet{selfhealing2025}: while they demonstrate RLVR superiority for unstructured magnitude pruning at 96.5\% retention, within our experimental scope (20--25\% structured MLP sparsity on Qwen2.5-family models), this hierarchy dissolves under diversity-preserving pruning---the gap appears attributable to the pruning criterion rather than a fundamental property of RL recovery.
365	
366	\section{Use of AI Assistants}
367	\label{sec:appendix_ai_assistants}
368	
369	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f41b2ac-031c-4614-9584-3d275d09a09b",
  "isSidechain": false,
  "promptId": "6e39d0cd-0e33-4a06-88ac-9143d352ef66",
  "type": "user",
  "uuid": "73e22fdb-6cc7-4016-9562-d18d5545da26",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex",
      "content": "\\section{Discussion}\n\\label{sec:appendix_discussion}\n\n\\paragraph{GRPO as diagnostic probe.}\nThe decoupling pattern suggests that GRPO may serve as a \\emph{diagnostic probe} for pruning quality at moderate sparsity: reward trajectories appear to indicate whether the pruned architecture retains sufficient diversity for RL exploration---information not accessible through SFT, which converges to similar accuracy at 20--25\\% MLP sparsity.\nAt 15\\% sparsity, GRPO amplifies the CKA-guided advantage ($+$1.51\\,pp), suggesting the transition boundary warrants future investigation.\n\n\\paragraph{Implications.}\nFor deployment pipelines that include post-pruning RL, diversity-preserving criteria (CKA-only or high-$\\alpha$ \\rasp{}) should be preferred.\nOur findings complement \\citet{selfhealing2025}: while they demonstrate RLVR superiority for unstructured magnitude pruning at 96.5\\% retention, within our experimental scope (20--25\\% structured MLP sparsity on Qwen2.5-family models), this hierarchy dissolves under diversity-preserving pruning---the gap appears attributable to the pruning criterion rather than a fundamental property of RL recovery.\n\n\\section{Use of AI Assistants}\n\\label{sec:appendix_ai_assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:",
      "numLines": 15,
      "startLine": 355,
      "totalLines": 375
    }
  },
  "sourceToolAssistantUUID": "2f41b2ac-031c-4614-9584-3d275d09a09b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-25T09:14:59.559Z_

<details><summary>Logged reasoning block</summary>

````text
I found a significant issue: The Discussion section content in the appendix (lines 355-364) is a near-exact copy of the Discussion section in conclusion.tex (lines 9-15). This is duplicated content between the main text and appendix. Both the conclusion.tex and appendix.tex have the "GRPO as diagnostic probe" and "Implications" paragraphs with essentially identical text.

Let me compare:

**conclusion.tex:**
```


\paragraph{GRPO as diagnostic probe.}
The decoupling pattern suggests that GRPO may serve as a \emph{diagnostic probe} for pruning quality at moderate sparsity: reward trajectories appear to indicate whether the pruned architecture retains sufficient diversity for RL exploration---information not accessible through SFT, which converges to similar accuracy at 20--25\% MLP sparsity.
At 15\% sparsity, GRPO amplifies the CKA-guided advantage ($+$1.51\,pp), suggesting the transition boundary warrants future investigation.

\paragraph{Implications.}
For deployment pipelines that include post-pruning RL, diversity-preserving criteria (CKA-only or high-$\alpha$ \rasp{})
```

The text discusses how GRPO functions as a diagnostic tool for evaluating pruned models, revealing whether they maintain enough architectural diversity for effective reinforcement learning exploration—something SFT alone can't assess. At lower sparsity levels, GRPO shows measurable improvements from CKA-guided pruning, pointing to an interesting threshold worth exploring further. The implications section then begins addressing practical deployment considerations for systems that apply RL after pruning, emphasizing the importance of diversity-preserving selection methods. I'm noticing the Discussion section is duplicated identically between the main text and appendix, which is wasteful and looks unprofessional. Let me verify the paper's claims about RASP's reward collapse—checking whether the stated "reward declining to 0.010" aligns with Table 1's metrics showing peak reward of 0.061 and mean of 0.031. The text appears to be referring to the final reward value rather than peak or mean, so these are actually consistent.

Now I'm examining whether Table 2 should include RASP at α=2.0 (66.11%) instead of just α=1.0 (60.88%), since the optimal variant outperforms even CKA-only at 64.39%. The paper's choice to present the full spectrum first and then α tuning separately is defensible, though a reviewer might question why the best result isn't in the primary comparison.

I've got what I need now. Let me compile the audit findings organized by severity: three critical issues around narrative consistency and internal data leakage, plus a warning about em-dashes in the text files.

Now I'm identifying additional problems: the writing contains multiple participial phrases that feel AI-generated, RASP's strongest result is missing from the main comparison table while a weaker variant appears instead, the abstract overstates the generalizability across benchmarks when some results lack statistical significance, and there's a logical inconsistency where an exception is claimed to reinforce rather than contradict the main pattern. The conclusion section is also quite sparse at only three paragraphs.

Beyond that, there's no mechanistic explanation for why the decoupling phenomenon occurs, the dose-response ablation and cross-scale experiments rely on single seeds rather than multiple runs, the introduction doesn't have a dedicated paragraph establishing problem importance, the RASP naming creates confusion by labeling the worst-performing variant as the main method, and the limitations section violates the guideline of keeping it to roughly three points in a brief paragraph rather than four separate ones.

I'm also noticing the reproducibility section is incomplete—the total GPU hours for the full experiment suite aren't reported and the GRPO training time is missing, only the SFT warmup duration is given. There's no transition sentence connecting the introduction to the related work section either.

Wait, I should double-check whether the Discussion section is actually duplicated across both the main conclusion and the appendix. Looking at the structure, both files contain identical paragraphs on "GRPO as diagnostic probe" and "Implications"—this is definitely redundant content that needs to be consolidated.

Since both conclusion.tex and appendix.tex are included in the compiled PDF through main.tex, this duplication is a real problem that would stand out to reviewers. I need to remove one copy and keep the content only in the main Discussion and Conclusion section.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73e22fdb-6cc7-4016-9562-d18d5545da26",
  "isSidechain": false,
  "requestId": "req_011CbP2nvrgfvpBwon3yQ6Xv",
  "type": "assistant",
  "uuid": "2e6a6f75-27a5-47cc-a776-abb6d9f999ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQvyBEuEaQdNkorLy6Koji",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 589,
      "cache_read_input_tokens": 106807,
      "output_tokens": 5482,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 589,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5482,
          "cache_read_input_tokens": 106807,
          "cache_creation_input_tokens": 589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 589
          },
          "type": "message"
        }
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

_source line 86 · 2026-05-25T09:16:04.993Z_

审计完成。以下是完整的结构化 findings。

```
[CONTENT_AUDIT_START]

=== 叙事一致性（CRITICAL 级）===

- [critical] [叙事一致性] Abstract 第2句 "this advantage is attributable to the pruning criterion rather than an inherent property of RL" 与实验证据存在逻辑断裂。实验数据显示在 20-25% 结构化稀疏度下，SFT ≈ GRPO 对**所有四种 criterion 均成立**（包括 Standard 这种 importance-only criterion），因此不能归因于 "pruning criterion" 导致了先前工作中 RLVR 的优势。正确的因果表述应为：RLVR > SFT 的先验结论在不同设定下（结构化 vs 非结构化、稀疏度、模型规模）不成立，原因可能是设定差异而非 criterion 选择。Introduction 第6行和 Conclusion 的 Implications 段也有同样的归因问题。Body 中的 hedge ("within our experimental scope", "suggest") 部分缓解但不改变逻辑链缺陷。审稿人极可能追问 "if SFT≈GRPO for ALL criteria, how can you attribute the prior RLVR advantage to the criterion?"

- [critical] [叙事一致性] appendix.tex:355-364 的 "Discussion" section 与 conclusion.tex:9-15 的 "GRPO as diagnostic probe" 和 "Implications" 段落完全重复（逐字相同）。编译后 PDF 会出现两份一模一样的 Discussion 内容，分别在主文和附录。审稿人会立即注意到，且浪费宝贵页面空间。

- [critical] [内部信息残留] appendix.tex TOST 表 (Table tab:tost) 包含内部实验标签 "verify"（CKA-only 行）、"fair_v2" 和 "ext 300"（Standard 行）。这些不是标准 seed 编号，明显是内部实验管理系统的 run 名称。"fair_v2" 暗示存在 "fair_v1" 迭代，"verify" 暗示验证性重跑，"ext 300" 是缩写。应替换为描述性标签（如 "seed 789", "300-step variant"）或在表注中解释含义。同时，这些额外 run 未在 Multi-Seed Results section (Appendix §appendix_multiseed) 中报告，选择性纳入 TOST 但不纳入 mean±std 计算，有 cherry-picking 嫌疑。

=== 贡献-范围对齐 ===

- [warning] [贡献-范围对齐] RASP 的最优配置 α=2.0（66.11% GRPO, 超过 CKA-only 的 64.39%）未出现在主对比表 Table 2 (tab:decoupling) 中。Table 2 仅展示 RASP α=1.0（表现最差的配置，60.88%），导致论文"提出的方法"在最重要的表格中看起来不如 CKA-only baseline。α=2.0 的结果只出现在次要的 Table 3 (α ablation)。审稿人可能质疑为何不在 main table 展示 proposed method 的最佳变体。

=== Claim 强度匹配 ===

- [warning] [Claim强度] abstract.tex:6 "These findings hold across three benchmarks" 过强。MBPP 结果 "not statistically significant at this sample size" (experiments.tex:82)；MATH-500 dose-response "not statistically significant" (appendix.tex:117)。应改为 "with consistent directional trends across three benchmarks" 或类似限定表述。

- [warning] [Claim强度] introduction.tex:29 Contribution 1 称 15% sparsity 的 exception "reinforces the main pattern"。逻辑上，exception（15% 出现 GRPO > SFT）不能 "reinforce" decoupling pattern（GRPO ≈ SFT）。应改为 "delineates the boundary of" 或 "contextualizes"。

=== 去 AI 风格 ===

- [warning] [去AI] abstract.tex:1 "recovery training---typically...RLVR)---to restore" 使用 em-dash 作括注
- [warning] [去AI] abstract.tex:5 "at moderate sparsity---a phenomenon we term" em-dash 引出同位语
- [warning] [去AI] introduction.tex:8 "The pruning criterion---not the recovery paradigm---appears" 强调性 em-dash
- [warning] [去AI] introduction.tex:9 "translate into accuracy gains---making their divergence noteworthy" em-dash + -ing 结尾
- [warning] [去AI] introduction.tex:24 "recovery capacity spectrum---a gradient in the pruned model's ability" em-dash 引出解释
- [warning] [去AI] method.tex:84 "yields suboptimal results---exhibiting reward collapse" em-dash + -ing
- [warning] [去AI] experiments.tex:81 "MATH-500's higher intrinsic difficulty---the unpruned model achieves only 53.0%---and" 双 em-dash 括注
- [warning] [去AI] experiments.tex:93 "Standard ordering---Standard exhibits higher peak reward" em-dash
- [warning] [去AI] experiments.tex:113 "cluster near 1.0---preserving dense fidelity retains" em-dash + -ing
- [warning] [去AI] conclusion.tex:10 "exploration---information not accessible through SFT" em-dash
- [warning] [去AI] conclusion.tex:15 "under diversity-preserving pruning---the gap appears" em-dash
（主文共 11+ 处解释性 em-dash，全部应替换为逗号、括号或拆分为独立句）

- [warning] [去AI] 多处 -ing 分词短语结尾：introduction.tex:25 "suggesting that pruning granularity interacts"；method.tex:87 "making RASP at α=2.0 effectively CKA-guided"；method.tex:88 "indicating that importance filtering provides"；experiments.tex:93 "indicating that the spectrum tracks"；experiments.tex:125 "suggesting the gap is structural"；related_work.tex:13 "suggesting the effect is attributable"。共 6+ 处，应改写为独立句。

=== 叙事一致性（补充） ===

- [warning] [叙事一致性] Discussion/Conclusion 仅 3 段（~150 words），缺少对 decoupling 现象的机制性解释。论文报告了"SFT warmup recovers bulk accuracy"但未解释 WHY GRPO 在此之上无法进一步提升。Related Work 提到的 LTH 类比在 Discussion 中未展开。审稿人可能要求更深入的理论解读。

=== 实验严谨性 ===

- [warning] [实验严谨性] Dose-response α ablation (Table 3, 5 个 α 值) 使用 single seed，无 error bar。这是论文的核心实验之一（inverted-U 形态依赖单次观测）。同理 cross-scale 1.5B 和 25% sparsity 也为 single seed。论文在 Limitations 中承认了这一点，但 α ablation 的 inverted-U peak (α=2.0) 的可靠性直接影响 RASP 的核心 claim。

=== 符号/术语一致性 ===

- [info] [符号] RASP 命名可能造成混淆：RASP 是论文提出的方法（参数化家族），但主实验表 (Table 1, 2) 中 "RASP" 标签专指 α=1.0（表现最差的配置，展示 reward collapse）。读者可能误以为 proposed method 本身不 work。建议在表格中统一标为 "RASP (α=1.0)" 并在某处强调 RASP 最优配置为 α=2.0。

- [info] [符号] Table 2 中 "Unpruned" baseline 的注释（"9.56pp gap from pre-warmup 90.83% reflects warmup on a reduced training set"）隐含了一个重要的实验设计细节——SFT warmup 使用了子集数据导致 unpruned model 也降了 ~10pp。此信息对理解绝对数字很关键，但只在正文中一句话带过，可能被审稿人忽略。

=== 可复现性披露 ===

- [info] [可复现性] 缺少全实验 GPU-hours 总量。SFT warmup time 给出 (37min)，但 GRPO 100-step 和 300-step 的 wall time 未报告。Compute budget 对于可复现性和审稿人评估实验可行性很重要。

=== 章节结构 ===

- [info] [章节结构] Introduction 缺少独立的"问题重要性"段落。当前结构为：(1)背景+核心发现预告 → (2)gap → (3)方法概述 → (4)贡献列表。标准 5 段结构建议在 gap 段之前增加一段说明"为什么理解 pruning criterion 对 recovery 的影响很重要"（实际部署意义、模型压缩成本等）。

- [info] [章节过渡] Introduction 贡献列表之后直接接 Related Work，无过渡句。可在贡献列表后加一句 "The remainder of this paper is organized as follows:" 或类似引导。

=== 用户自定义规则检查 ===

- [info] [写作规则] Limitations 章节当前有 4 个 \paragraph 共 ~255 words，覆盖 4 个点。用户规则要求 "只需要写一小段，覆盖 3 个点左右"。建议合并 "Diagnostic limitations" 和 "Inference efficiency" 为一段，或删减其一，压缩到 3 个点。

- [info] [审稿规则] 正文页数需确认 ≤ 8 页（EMNLP 2026 limit）。Phase 1 报告编译 16 页总量，需核实 main text 部分（Section 1-5，不含 Limitations/Ethics/References/Appendix）是否在 8 页以内。如果主文超 8 页，为 critical。

[CONTENT_AUDIT_END]
```

**审计摘要**：3 个 critical，18 个 warning，7 个 info。

最严重的问题是**核心叙事的因果归因逻辑**：论文将 RLVR 先验优势归因于 "pruning criterion"，但实验数据显示 SFT≈GRPO 对所有 criterion 均成立（在 20-25% 稀疏度下），因此 criterion 不是解释变量。其次是附录 Discussion 与主文完全重复，以及 TOST 表中内部实验标签泄露。

[AUDIT_DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e6a6f75-27a5-47cc-a776-abb6d9f999ee",
  "isSidechain": false,
  "requestId": "req_011CbP2nvrgfvpBwon3yQ6Xv",
  "type": "assistant",
  "uuid": "8dc4da28-21d1-44ce-914b-c131f66d61f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/paper_audit_content_1d8e5d87",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQvyBEuEaQdNkorLy6Koji",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 589,
      "cache_read_input_tokens": 106807,
      "output_tokens": 5482,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 589,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5482,
          "cache_read_input_tokens": 106807,
          "cache_creation_input_tokens": 589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 589
          },
          "type": "message"
        }
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

_source line 87_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：recovery_aware_struct_prune Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 7 critical,…",
  "leafUuid": "8dc4da28-21d1-44ce-914b-c131f66d61f5",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033"
}
```

---

### Runtime record

_source line 88_

```json
{
  "type": "ai-title",
  "aiTitle": "Recovery-aware structural pruning paper review",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033"
}
```

---

### Runtime record

_source line 89_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：recovery_aware_struct_prune Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 7 critical,…",
  "leafUuid": "8dc4da28-21d1-44ce-914b-c131f66d61f5",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033"
}
```

---

### Runtime record

_source line 90_

```json
{
  "type": "ai-title",
  "aiTitle": "Recovery-aware structural pruning paper review",
  "sessionId": "7498c864-bfb8-423d-b165-a88bcbf00033"
}
```

---
