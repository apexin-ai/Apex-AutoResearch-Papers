# Research conversation: 项目：causal_annot_error_attrib Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 93
- **Recorded user turns:** 1
- **Tool calls:** 30
- **Original source:** `logs/chats/exported-trajectories/account-1/f2d04d29-82a6-45e9-9418-9059a8b7c0cb.jsonl`
- **Structured JSON:** [`40df2e1613b7d4379aff.json`](../../sessions/40/40df2e1613b7d4379aff.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-25T08:23:13.501Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T08:23:13.501Z",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "content": "项目：causal_annot_error_attrib\nVenue：emnlp-2026\n论文目录：/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper\n\nPhase 1 确定性检查结果：\n源码检查: passed=True, 0 critical, 92 warning\n一致性检查: 1 critical, 25 warning\n编译: ✅, 页数: 34\n内部信息: 0 critical, 0 warning\n\n━━━ 用户自定义规则（作为额外检查项）━━━\n## 用户自定义规则（必须遵守）\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section\n- **[EMNLP 2026]** abstract 不要超过 200 words\n\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n请将以上规则逐条作为额外审计维度检查。违反的规则用 dimension `[写作规则]` 或 `[审稿规则]` 标记，severity 按实际影响判定。\n\n请按照你的角色指令执行内容结构审计。"
}
```

---

### Runtime record

_source line 2 · 2026-05-25T08:23:13.505Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T08:23:13.505Z",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb"
}
```

---

## Round 1

91 recorded events

### User

_source line 3 · 2026-05-25T08:23:13.545Z_

项目：causal_annot_error_attrib
Venue：emnlp-2026
论文目录：/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper

Phase 1 确定性检查结果：
源码检查: passed=True, 0 critical, 92 warning
一致性检查: 1 critical, 25 warning
编译: ✅, 页数: 34
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
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "1be7bda3-f793-4e1a-8563-0a26a2c62517",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-25T08:23:13.544Z_

```json
{
  "parentUuid": "1be7bda3-f793-4e1a-8563-0a26a2c62517",
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
  "uuid": "a9658d68-ec2a-4adf-86d1-3a7cd642ce1c",
  "timestamp": "2026-05-25T08:23:13.544Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-25T08:23:13.545Z_

```json
{
  "parentUuid": "a9658d68-ec2a-4adf-86d1-3a7cd642ce1c",
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
  "uuid": "bb7a0791-4eff-4d1a-953c-aedcd969fc17",
  "timestamp": "2026-05-25T08:23:13.545Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-25T08:23:13.545Z_

```json
{
  "parentUuid": "bb7a0791-4eff-4d1a-953c-aedcd969fc17",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0a182284-96c0-480b-8d73-8c8f2939a8fd",
  "timestamp": "2026-05-25T08:23:13.545Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit causal annotation error attribution paper",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb"
}
```

---

### Assistant

_source line 8 · 2026-05-25T08:23:17.219Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the required skill files and then all .tex files in the paper directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a182284-96c0-480b-8d73-8c8f2939a8fd",
  "isSidechain": false,
  "requestId": "req_011CbNxui3yw4F8fGiR1uBK8",
  "type": "assistant",
  "uuid": "d7f5eee9-003c-4de1-a2dd-eadcd5d944e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DAqLXC1rN4rCHHfoddmpz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27853,
      "cache_read_input_tokens": 11846,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27853
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-25T08:23:17.493Z_

开始执行内容结构审计。先加载审计标准和论文源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7f5eee9-003c-4de1-a2dd-eadcd5d944e5",
  "isSidechain": false,
  "requestId": "req_011CbNxui3yw4F8fGiR1uBK8",
  "type": "assistant",
  "uuid": "13d09b88-9fb1-4c56-9e39-aece8c2a301c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DAqLXC1rN4rCHHfoddmpz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27853,
      "cache_read_input_tokens": 11846,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27853
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-25T08:23:18.437Z_

<details open><summary>🔧 Tool call — Read · `toolu_015j29kGRyXdSVhSckiCuKy5`</summary>

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
  "parentUuid": "13d09b88-9fb1-4c56-9e39-aece8c2a301c",
  "isSidechain": false,
  "requestId": "req_011CbNxui3yw4F8fGiR1uBK8",
  "type": "assistant",
  "uuid": "21ef05ad-b14d-472b-9b49-2dd586929a42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DAqLXC1rN4rCHHfoddmpz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27853,
      "cache_read_input_tokens": 11846,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27853
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-25T08:23:19.285Z_

<details><summary>↩ Tool result · `toolu_01Pd7hRWPte4mSxcfqnfvHxX`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/exp_a_stress_test_table.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/exp_e_asv_stability_table.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conjecture_dgp_sensitivity_table.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/e2e_demo_table.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/e2e_real_cm_table.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/k3_symmetric_proof.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25fd79d8-0060-4825-94ae-2b0713bd52af",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "b42a97d9-2779-427d-86c4-6484039dd33c",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/exp_a_stress_test_table.tex",
      "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/exp_e_asv_stability_table.tex",
      "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conjecture_dgp_sensitivity_table.tex",
      "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/e2e_demo_table.tex",
      "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/e2e_real_cm_table.tex",
      "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex",
      "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex",
      "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/k3_symmetric_proof.tex",
      "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
    ],
    "durationMs": 11,
    "numFiles": 14,
    "truncated": false
  },
  "sourceToolAssistantUUID": "25fd79d8-0060-4825-94ae-2b0713bd52af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T08:23:18.449Z_

<details><summary>↩ Tool result · `toolu_015j29kGRyXdSVhSckiCuKy5`</summary>

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
  "parentUuid": "21ef05ad-b14d-472b-9b49-2dd586929a42",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "5e09923b-6671-427f-88f0-6613d2a7b475",
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
  "sourceToolAssistantUUID": "21ef05ad-b14d-472b-9b49-2dd586929a42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Tool call

_source line 13 · 2026-05-25T08:23:19.009Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JnMjLt1pPgU68MshV86QAm`</summary>

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
  "parentUuid": "5e09923b-6671-427f-88f0-6613d2a7b475",
  "isSidechain": false,
  "requestId": "req_011CbNxui3yw4F8fGiR1uBK8",
  "type": "assistant",
  "uuid": "3f90c2a3-f225-4027-9c80-cc25b76a817b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DAqLXC1rN4rCHHfoddmpz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27853,
      "cache_read_input_tokens": 11846,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27853
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-25T08:23:19.016Z_

<details><summary>↩ Tool result · `toolu_01JnMjLt1pPgU68MshV86QAm`</summary>

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
  "parentUuid": "3f90c2a3-f225-4027-9c80-cc25b76a817b",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "f254d845-46ad-4132-9b9d-d85b2d353046",
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
  "sourceToolAssistantUUID": "3f90c2a3-f225-4027-9c80-cc25b76a817b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Tool call

_source line 15 · 2026-05-25T08:23:19.270Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Pd7hRWPte4mSxcfqnfvHxX`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f254d845-46ad-4132-9b9d-d85b2d353046",
  "isSidechain": false,
  "requestId": "req_011CbNxui3yw4F8fGiR1uBK8",
  "type": "assistant",
  "uuid": "25fd79d8-0060-4825-94ae-2b0713bd52af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DAqLXC1rN4rCHHfoddmpz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27853,
      "cache_read_input_tokens": 11846,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 27853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27853
          },
          "type": "message"
        }
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
  "lastPrompt": "项目：causal_annot_error_attrib Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 92 warning 一…",
  "leafUuid": "b42a97d9-2779-427d-86c4-6484039dd33c",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit causal annotation error attribution paper",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb"
}
```

---

### Assistant

_source line 18 · 2026-05-25T08:23:21.833Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read all the .tex files. Let me read them in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b42a97d9-2779-427d-86c4-6484039dd33c",
  "isSidechain": false,
  "requestId": "req_011CbNxv8mXTejhBT9P2pLrN",
  "type": "assistant",
  "uuid": "88011b14-2abc-4f5f-a358-35ec27299f81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXWWF9ogGXcabKsU1RyxvV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12102,
      "cache_read_input_tokens": 39699,
      "output_tokens": 635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12102,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 635,
          "cache_read_input_tokens": 39699,
          "cache_creation_input_tokens": 12102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12102
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-25T08:23:22.328Z_

Now reading all .tex source files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88011b14-2abc-4f5f-a358-35ec27299f81",
  "isSidechain": false,
  "requestId": "req_011CbNxv8mXTejhBT9P2pLrN",
  "type": "assistant",
  "uuid": "0b9a8c4f-f279-4e34-b22e-94492f603e64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXWWF9ogGXcabKsU1RyxvV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12102,
      "cache_read_input_tokens": 39699,
      "output_tokens": 635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12102,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 635,
          "cache_read_input_tokens": 39699,
          "cache_creation_input_tokens": 12102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12102
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-25T08:23:22.820Z_

<details open><summary>🔧 Tool call — Read · `toolu_013L1QEtGqvKR8RMTkKuVj44`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b9a8c4f-f279-4e34-b22e-94492f603e64",
  "isSidechain": false,
  "requestId": "req_011CbNxv8mXTejhBT9P2pLrN",
  "type": "assistant",
  "uuid": "073cd165-a64f-4d3d-8a12-69e766d83d9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXWWF9ogGXcabKsU1RyxvV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12102,
      "cache_read_input_tokens": 39699,
      "output_tokens": 635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12102,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 635,
          "cache_read_input_tokens": 39699,
          "cache_creation_input_tokens": 12102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12102
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-25T08:23:22.824Z_

<details><summary>↩ Tool result · `toolu_013L1QEtGqvKR8RMTkKuVj44`</summary>

```text
1	\begin{abstract}
2	When large language model (LLM)-generated annotations feed into causal inference, annotation quality alone is insufficient to assess causal validity; the causal directed acyclic graph (DAG) topology determines whether errors attenuate, amplify, or reverse the treatment effect estimate. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification in linear structural equation models and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. Under proportional effects, five topologies preserve the treatment effect sign under regularity conditions; exposure and instrumental variable (IV) can reverse it. Under empirical LLM confusion matrices, sign reversal is confined to exposure topology. We introduce Annotation Sensitivity Values (ASVs), with proved ($K{=}2$, $K{=}3$ symmetric) and extensively validated (general $K{\geq}3$) monotonicity that yields a vulnerability ranking from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective under linear regression for four topologies due to Frisch--Waugh--Lovell invariance. A case study with 10 real LLM confusion matrices confirms: topology-aware correction reduces exposure bias from 61\% to $<$1\%, while topology-blind corrections are provably futile under linear regression for four topologies.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "073cd165-a64f-4d3d-8a12-69e766d83d9d",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "8dc57805-ad85-4718-83d1-770cc08e4653",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nWhen large language model (LLM)-generated annotations feed into causal inference, annotation quality alone is insufficient to assess causal validity; the causal directed acyclic graph (DAG) topology determines whether errors attenuate, amplify, or reverse the treatment effect estimate. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification in linear structural equation models and show that $K {\\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. Under proportional effects, five topologies preserve the treatment effect sign under regularity conditions; exposure and instrumental variable (IV) can reverse it. Under empirical LLM confusion matrices, sign reversal is confined to exposure topology. We introduce Annotation Sensitivity Values (ASVs), with proved ($K{=}2$, $K{=}3$ symmetric) and extensively validated (general $K{\\geq}3$) monotonicity that yields a vulnerability ranking from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective under linear regression for four topologies due to Frisch--Waugh--Lovell invariance. A case study with 10 real LLM confusion matrices confirms: topology-aware correction reduces exposure bias from 61\\% to $<$1\\%, while topology-blind corrections are provably futile under linear regression for four topologies.\n\\end{abstract}\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  },
  "sourceToolAssistantUUID": "073cd165-a64f-4d3d-8a12-69e766d83d9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T08:23:23.316Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Somc62RLq4ZWheFfTVyXWs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dc57805-ad85-4718-83d1-770cc08e4653",
  "isSidechain": false,
  "requestId": "req_011CbNxv8mXTejhBT9P2pLrN",
  "type": "assistant",
  "uuid": "a3ab76b3-e751-48ea-86d3-0400061329a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXWWF9ogGXcabKsU1RyxvV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12102,
      "cache_read_input_tokens": 39699,
      "output_tokens": 635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12102,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 635,
          "cache_read_input_tokens": 39699,
          "cache_creation_input_tokens": 12102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12102
          },
          "type": "message"
        }
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

_source line 23 · 2026-05-25T08:23:23.321Z_

<details><summary>↩ Tool result · `toolu_01Somc62RLq4ZWheFfTVyXWs`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models (LLMs) are rapidly replacing human annotators in computational social science~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Most tasks are inherently multi-class (stance detection: 3--4 categories, sentiment: 5, disaster response: 10+), and annotation errors propagate into downstream causal estimates in ways that depend on both error structure and causal design. \citet{baumann2025} show that 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, with 60\% error correlation across models~\cite{kim_garg2025}. Standard metrics do not capture this risk: within $F_1$ 0.61--0.69, causal bias varies by an order of magnitude across topologies.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs, an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee vanishes at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients; sign reversal can occur even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient is never reversed under the tested $\beta$ configurations where a single category dominates ($\beta_1 \gg \beta_2$), an empirical regularity we discuss in Section~\ref{sec:method}.
7	
8	$F_1$ does not exhibit significant rank correlation with causal bias ($\rho = -0.10$, $p = 0.45$ across 56 HumAID scenarios; bias varies $>$10${\times}$ (from $<$6\% to 42.1\%) within $F_1$ 0.614--0.690). Prior work noted polytomous sign reversal~\cite{dosemeci1990, veirod_laake2001} and confounder amplification~\cite{brenner1993}, but covered at most one topology~\cite{lee_wood_doughty2024}. We present the first systematic analysis jointly addressing multi-class ($K{\geq}3$) misclassification across seven directed acyclic graph (DAG) topologies, with analytical predictions matching Monte Carlo within 1.6\% MAPE across 161 scenarios.
9	
10	We address these gaps with three contributions:
11	
12	\begin{enumerate}
13	\item \textbf{Multi-class bias taxonomy.} We derive bias expressions for seven canonical DAG topologies\footnote{These span the four structural roles of the annotated variable: treatment (exposure), outcome-side covariate (confounding, mediation, M-bias, front-door), selection variable (collider), and instrumental variable (IV).} (Figure~\ref{fig:dag_taxonomy}) under $K$-class non-differential misclassification and establish a sign-preservation/reversal dichotomy: five topologies preserve the treatment effect sign under topology-specific regularity conditions (Proposition~\ref{prop:signflip}), while exposure and IV can reverse it.
14	
15	\item \textbf{Annotation Sensitivity Values.} We define three ASV diagnostics (magnitude, significance, and sign-flip) with proved envelope monotonicity (Theorems~\ref{thm:monotone},~\ref{thm:k3_symmetric}) and $\varepsilon$-approximate monotonicity for general $K{\geq}3$ (Conjecture~\ref{conj:monotone}). This reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune).
16	
17	\item \textbf{Topology-aware correction routing.} Frisch--Waugh--Lovell (FWL) invariance renders matrix-based corrections provably ineffective for four covariate topologies. We evaluate five correction methods and provide a topology-aware decision procedure (Algorithm~\ref{alg:correction}, Appendix), validated with real LLM confusion matrices.
18	\end{enumerate}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3ab76b3-e751-48ea-86d3-0400061329a2",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "e8deded4-6378-42ed-80dc-adfbc4ac49ed",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLarge language models (LLMs) are rapidly replacing human annotators in computational social science~\\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Most tasks are inherently multi-class (stance detection: 3--4 categories, sentiment: 5, disaster response: 10+), and annotation errors propagate into downstream causal estimates in ways that depend on both error structure and causal design. \\citet{baumann2025} show that 31\\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, with 60\\% error correlation across models~\\cite{kim_garg2025}. Standard metrics do not capture this risk: within $F_1$ 0.61--0.69, causal bias varies by an order of magnitude across topologies.\n\nThe transition at $K{\\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs, an algebraic property of the $2{\\times}2$ matrix dimension~\\cite{brenner1993}. This guarantee vanishes at $K{\\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients; sign reversal can occur even under high accuracy~\\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\\geq 0.7$), 2.1\\% still do. The primary treatment coefficient is never reversed under the tested $\\beta$ configurations where a single category dominates ($\\beta_1 \\gg \\beta_2$), an empirical regularity we discuss in Section~\\ref{sec:method}.\n\n$F_1$ does not exhibit significant rank correlation with causal bias ($\\rho = -0.10$, $p = 0.45$ across 56 HumAID scenarios; bias varies $>$10${\\times}$ (from $<$6\\% to 42.1\\%) within $F_1$ 0.614--0.690). Prior work noted polytomous sign reversal~\\cite{dosemeci1990, veirod_laake2001} and confounder amplification~\\cite{brenner1993}, but covered at most one topology~\\cite{lee_wood_doughty2024}. We present the first systematic analysis jointly addressing multi-class ($K{\\geq}3$) misclassification across seven directed acyclic graph (DAG) topologies, with analytical predictions matching Monte Carlo within 1.6\\% MAPE across 161 scenarios.\n\nWe address these gaps with three contributions:\n\n\\begin{enumerate}\n\\item \\textbf{Multi-class bias taxonomy.} We derive bias expressions for seven canonical DAG topologies\\footnote{These span the four structural roles of the annotated variable: treatment (exposure), outcome-side covariate (confounding, mediation, M-bias, front-door), selection variable (collider), and instrumental variable (IV).} (Figure~\\ref{fig:dag_taxonomy}) under $K$-class non-differential misclassification and establish a sign-preservation/reversal dichotomy: five topologies preserve the treatment effect sign under topology-specific regularity conditions (Proposition~\\ref{prop:signflip}), while exposure and IV can reverse it.\n\n\\item \\textbf{Annotation Sensitivity Values.} We define three ASV diagnostics (magnitude, significance, and sign-flip) with proved envelope monotonicity (Theorems~\\ref{thm:monotone},~\\ref{thm:k3_symmetric}) and $\\varepsilon$-approximate monotonicity for general $K{\\geq}3$ (Conjecture~\\ref{conj:monotone}). This reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune).\n\n\\item \\textbf{Topology-aware correction routing.} Frisch--Waugh--Lovell (FWL) invariance renders matrix-based corrections provably ineffective for four covariate topologies. We evaluate five correction methods and provide a topology-aware decision procedure (Algorithm~\\ref{alg:correction}, Appendix), validated with real LLM confusion matrices.\n\\end{enumerate}\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  },
  "sourceToolAssistantUUID": "a3ab76b3-e751-48ea-86d3-0400061329a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-25T08:23:24.250Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QAaCqMRKABDAeU2buXtzsa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8deded4-6378-42ed-80dc-adfbc4ac49ed",
  "isSidechain": false,
  "requestId": "req_011CbNxv8mXTejhBT9P2pLrN",
  "type": "assistant",
  "uuid": "75e17f89-8917-464b-b469-c13d270024e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXWWF9ogGXcabKsU1RyxvV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12102,
      "cache_read_input_tokens": 39699,
      "output_tokens": 635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12102,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 635,
          "cache_read_input_tokens": 39699,
          "cache_creation_input_tokens": 12102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12102
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-25T08:23:24.255Z_

<details><summary>↩ Tool result · `toolu_01QAaCqMRKABDAeU2buXtzsa`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	Non-differential misclassification of a binary variable biases estimates toward the null~\cite{bross1954misclassification, brenner1993, ogburn_vanderweele2012}, formalized in the DAG framework by \citet{hernan_cole2009} and \citet{kuroki_pearl2014}. This guarantee breaks for polytomous variables~\cite{dosemeci1990, jurek2005, veirod_laake2001}, yet extensions to differential error, mismeasured covariates, and nonclassical structures~\cite{edwards_lessler_naimi2021, shu_yi2019a, valeri_vanderweele2013, schennach2020mismeasured} treat topologies in isolation. No prior work compares how the \emph{same} confusion matrix produces qualitatively different bias depending on the mismeasured variable's causal role.
6	
7	\paragraph{LLM annotation and downstream causal validity.}
8	LLMs are rapidly replacing human annotators~\cite{gilardi2023chatgpt, ziems2024can, tan2024llm}, yet consequences for causal inference remain underexplored. \citet{baumann2025} and \citet{kim_garg2025} show that 31\% of hypotheses yield incorrect conclusions and error correlations reach 60\% across models, but neither connects error patterns to DAG structure. \citet{teblunthuis2024} provides the most complete binary analysis (four topologies, $K{=}2$) and \citet{lee_wood_doughty2024} extends to categorical classifiers, but only for confounding. The multi-class ($K{\geq}3$) regime, where sign reversal becomes structurally possible, remains unaddressed.
9	
10	\paragraph{Sensitivity analysis and correction methods.}
11	Sensitivity frameworks for unmeasured confounding~\cite{vanderweele_ding2017, cinelli2020making, oster2019} do not address annotation error, while matrix-adjustment~\cite{blackwell_honaker_king2017, lash2009} and prediction-powered methods~\cite{angelopoulos2023, egami_hinck_stewart_wei2023, zrnic_candes2024, gligoric2025} target misclassification but remain topology-agnostic. We show this agnosticism is costly: FWL invariance renders matrix-based corrections provably ineffective for four covariate topologies, and topology-blind application can amplify bias ($-$139\% for IV).
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75e17f89-8917-464b-b469-c13d270024e4",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "2345d8bf-4414-482f-a8df-aba7601b8dff",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Measurement error in causal inference.}\nNon-differential misclassification of a binary variable biases estimates toward the null~\\cite{bross1954misclassification, brenner1993, ogburn_vanderweele2012}, formalized in the DAG framework by \\citet{hernan_cole2009} and \\citet{kuroki_pearl2014}. This guarantee breaks for polytomous variables~\\cite{dosemeci1990, jurek2005, veirod_laake2001}, yet extensions to differential error, mismeasured covariates, and nonclassical structures~\\cite{edwards_lessler_naimi2021, shu_yi2019a, valeri_vanderweele2013, schennach2020mismeasured} treat topologies in isolation. No prior work compares how the \\emph{same} confusion matrix produces qualitatively different bias depending on the mismeasured variable's causal role.\n\n\\paragraph{LLM annotation and downstream causal validity.}\nLLMs are rapidly replacing human annotators~\\cite{gilardi2023chatgpt, ziems2024can, tan2024llm}, yet consequences for causal inference remain underexplored. \\citet{baumann2025} and \\citet{kim_garg2025} show that 31\\% of hypotheses yield incorrect conclusions and error correlations reach 60\\% across models, but neither connects error patterns to DAG structure. \\citet{teblunthuis2024} provides the most complete binary analysis (four topologies, $K{=}2$) and \\citet{lee_wood_doughty2024} extends to categorical classifiers, but only for confounding. The multi-class ($K{\\geq}3$) regime, where sign reversal becomes structurally possible, remains unaddressed.\n\n\\paragraph{Sensitivity analysis and correction methods.}\nSensitivity frameworks for unmeasured confounding~\\cite{vanderweele_ding2017, cinelli2020making, oster2019} do not address annotation error, while matrix-adjustment~\\cite{blackwell_honaker_king2017, lash2009} and prediction-powered methods~\\cite{angelopoulos2023, egami_hinck_stewart_wei2023, zrnic_candes2024, gligoric2025} target misclassification but remain topology-agnostic. We show this agnosticism is costly: FWL invariance renders matrix-based corrections provably ineffective for four covariate topologies, and topology-blind application can amplify bias ($-$139\\% for IV).\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  },
  "sourceToolAssistantUUID": "75e17f89-8917-464b-b469-c13d270024e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-25T08:23:24.775Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RWwpkx5Pe4qVWX8yKSpEqR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2345d8bf-4414-482f-a8df-aba7601b8dff",
  "isSidechain": false,
  "requestId": "req_011CbNxv8mXTejhBT9P2pLrN",
  "type": "assistant",
  "uuid": "c485d149-0aca-4ae1-83b9-bfb4f58cfb51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXWWF9ogGXcabKsU1RyxvV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12102,
      "cache_read_input_tokens": 39699,
      "output_tokens": 635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12102,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 635,
          "cache_read_input_tokens": 39699,
          "cache_creation_input_tokens": 12102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12102
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-25T08:23:24.780Z_

<details><summary>↩ Tool result · `toolu_01RWwpkx5Pe4qVWX8yKSpEqR`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one (column-stochastic: each column gives the distribution of predicted labels for a given true label). Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\paragraph{Notation conventions.}
10	Our analysis characterizes probability limits ($N \to \infty$) under the FWL theorem~\cite{frisch1933partial}, which explains why matrix-based corrections fail for covariate topologies (Section~\ref{sec:correction}). Notation is collected in Table~\ref{tab:notation} (Appendix~\ref{app:notation_table}).
11	
12	\begin{definition}[Non-differential misclassification]
13	\label{def:nondiff}
14	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
15	\end{definition}
16	
17	In batch annotation pipelines, the LLM processes each text independently without access to $Y$, making non-differentiality an architectural invariant~\cite{ziems2024can}; Y-stratified permutation tests confirm this (1/12 rejection at $\alpha{=}0.05$; Appendix~\ref{sec:y_stratified_test}). Non-differentiality may be violated when $Y$ correlates with text content, in which case our Y-stratified test provides empirical verification. Under stress testing, sign reversal occurs in 14/16 $K{\geq}3$ exposure configurations at $\eta{=}0.01$ structured departure (Appendix~\ref{sec:nondiff_stress}).
18	
19	Throughout, $\tau$ denotes the causal estimand of interest, whose definition varies by topology: the confounder's coefficient, the treatment effect, the indirect effect, or the Wald ratio (Appendix~\ref{app:confounding}ff.).
20	
21	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009, hernan2020causal}, deriving probability limits under linear structural equation models (SEMs)~\cite{carroll2006}; logistic regression robustness is verified in Appendix~\ref{sec:logistic_dgp} and~\ref{sec:fwl_nonlinear}.
22	
23	\subsection{Multi-Class Bias Expressions}
24	\label{sec:bias_expressions}
25	
26	For each topology, we derive the $\operatorname{plim}$\footnote{The probability limit (plim) is the value to which an estimator converges as sample size $N \to \infty$; it characterizes systematic bias separately from sampling variability.} of the naive estimator that substitutes $A^*$ for $A$. Let $\tau$ denote the target causal parameter, whose precise definition is topology-specific (e.g., the coefficient on $X$ for confounding, the category-specific $\beta_j$ for exposure, or the direct effect $\tau_{\text{direct}}$ for mediation), and $\hat{\tau}(A^*)$ the estimator using misclassified annotations.
27	
28	\paragraph{Confounding ($A$ = confounder).}
29	When $A$ confounds the $X{\to}Y$ relationship, the ordinary least squares (OLS) estimator controlling for $A^*$ has probability limit
30	\begin{equation}
31	\label{eq:confounding}
32	\operatorname{plim}\;\hat{\tau}(A^*) = \bigl(\mathbb{E}[Z^{\prime}Z]\bigr)^{-1}\mathbb{E}[Z^{\prime}X]\,\boldsymbol{\beta},
33	\end{equation}
34	where $Z = [X, \text{dummies}(A^*)]$, $\boldsymbol{\beta}$ contains the true coefficients, and the target parameter $\tau$ is the coefficient on $X$. Misclassification produces residual confounding that monotonically approaches the omitted variable bias, but the sign of $\hat{\tau}$ is preserved: $\tau_{\text{sign\_flip}} = 0$ structurally.\footnote{Consistent with \citet{brenner1993}: misclassification degrades confounding control, producing amplification ($|\hat{\tau}| > |\tau|$, universal in this topology) but never sign reversal ($\operatorname{sign}(\hat{\tau}) \neq \operatorname{sign}(\tau)$).}
35	
36	\paragraph{Exposure ($A$ = treatment variable).}
37	When $A$ is the exposure of interest, the biased coefficient for category $j$ becomes a weighted combination of true coefficients:
38	\begin{equation}
39	\label{eq:exposure}
40	\operatorname{plim}\;\hat{\beta}_j(A^*) = \sum_{k=1}^{K} w_{jk}\,\beta_k,
41	\end{equation}
42	where $w_{jk}$ depends on the confusion matrix $C$ and the population marginal $\pi_k = P(A{=}k)$. Unlike binary misclassification~\cite{brenner1993}, $K{\geq}3$ permits $w_{jk}$ to assign negative weight to categories with opposite-sign coefficients, producing \emph{sign reversal} (83.4\% under uniform Dirichlet prior); this is structurally impossible at $K{=}2$.
43	
44	\begin{figure*}[t]
45	\centering
46	\includegraphics[width=\textwidth]{fig2_bias_distribution.pdf}
47	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices (uniform Dirichlet; realistic-accuracy results in Section~\ref{sec:taxonomy_results}). Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
48	\label{fig:bias_distribution}
49	\end{figure*}
50	
51	\paragraph{Primary coefficient preservation.}
52	Across 23 empirical LLM configurations, the primary coefficient (the category with the largest true effect $|\beta_k|$) never reverses sign, while 61\% reverse a secondary (non-dominant) coefficient, confirmed under 100{,}000 Dirichlet matrices with diagonal ${\geq}\,0.7$ across six beta-ratio conditions (1.0 to 50.0) with 0\% primary sign-flip (Appendix~\ref{app:exposure}).
53	
54	\paragraph{Mediation ($A$ = mediator).}
55	When $A$ mediates the $X{\to}Y$ relationship~\cite{vanderweele2015explanation}, the direct effect estimator controlling for $A^*$ has probability limit
56	\begin{equation}
57	\label{eq:mediation}
58	\operatorname{plim}\;\hat{\tau}_{\text{direct}}(A^*) = \tau_{\text{direct}} + \bigl(1 - \lambda(C)\bigr)\,\tau_{\text{indirect}},
59	\end{equation}
60	where $\lambda(C) \in [0,1]$ under proportional effects (Appendix~\ref{app:proof}, Proposition~\ref{prop:lambda_bound}), with $\lambda(I) = 1$ under perfect classification. Misclassification ($\lambda < 1$) causes the residual indirect effect to be absorbed into the direct path estimate, producing upward bias in $|\hat{\tau}_{\text{direct}}|$ but preserving the sign ($\tau_{\text{sign\_flip}} = 0$).
61	
62	\paragraph{Collider, M-bias, and front-door.}
63	Three topologies exhibit protective or immune behavior. \textbf{Collider:} conditioning on $A^*$ instead of $A$ attenuates Berkson bias by weakening the spurious path, so annotation error is protective ($\tau_{\text{sign\_flip}} = 0$). \textbf{M-bias:} in the M-shaped DAG~\cite{greenland2003}, misclassifying $A$ attenuates the non-causal path, making this topology immune ($\text{ASV} = \infty$). \textbf{Front-door:} the front-door estimator~\cite{bellemare_bloem2024} requires two stages ($X \to A$ and $A \to Y$), each attenuated by $C$; the compound effect produces moderate bias with $\tau_{\text{sign\_flip}} = 0$.
64	
65	\paragraph{Instrumental variable ($A$ = instrument).}
66	The Wald estimator~\cite{angrist_imbens1995} $\hat{\tau}_{\text{IV}} = \hat{\text{cov}}(A^*, Y) / \hat{\text{cov}}(A^*, X)$ has $C$ in the denominator. Misclassification can drive first-stage coefficients toward zero or reverse their sign; under random Dirichlet matrices, 52.6\% produce sign reversal; IV is the most fragile topology (Appendix~\ref{sec:iv_dirichlet_subspace}).
67	
68	\paragraph{Structural sign-flip guarantee.}
69	\begin{proposition}[Sign preservation: analytic results]
70	\label{prop:signflip}
71	Under non-differential misclassification with $C_{kk} > 0$ for all $k$:
72	\emph{(a)}~Confounding preserves sign when $\operatorname{sign}(\tau) = \operatorname{sign}(\tau {+} B_{\mathrm{OV}})$, where $B_{\mathrm{OV}} {=} \operatorname{Cov}(g(A),f(A))/\operatorname{Var}(T)$ is the omitted-variable bias (Cauchy--Schwarz; Appendix~\ref{app:confounding}).
73	\emph{(b)}~Collider preserves sign when $|\tau| > \sqrt{\operatorname{Var}(g)\operatorname{Var}(h)}/\mathbb{E}[\operatorname{Var}(T{\mid}A)]$ (Berkson attenuation; Appendix~\ref{app:collider}); empirically verified across 100{,}000 matrices with zero violations.
74	\emph{(c)}~Exposure can produce sign reversal for $K {\geq} 3$, even with $C_{kk} {>} 0.5$ (counterexample in Appendix~\ref{app:exposure}).
75	\end{proposition}
76	
77	Sign preservation for non-exposure topologies holds under topology-specific conditions (Table~\ref{tab:sign_conditions}, Appendix~\ref{app:conditions}), verified across 100{,}000 random matrices with zero violations; analytic proofs for general $K$ remain open.
78	
79	\begin{figure*}[t]
80	\centering
81	\includegraphics[width=\textwidth]{fig3_asv_ranking.pdf}
82	\caption{ASV vulnerability ranking across topologies. Three ASV types (magnitude, significance, sign-flip) reveal a topology-dependent spectrum from IV (maximally fragile) to M-bias (immune, ASV $= \infty$).}
83	\label{fig:asv_ranking}
84	\end{figure*}
85	
86	\subsection{Annotation Sensitivity Values}
87	\label{sec:asv}
88	
89	We adapt the sensitivity analysis paradigm (E-values~\cite{vanderweele_ding2017}, partial-$R^2$ bounds~\cite{cinelli2020making}, coefficient stability~\cite{oster2019}) to $K{\times}K$ annotation error and define Annotation Sensitivity Values (ASVs): we prove $\varepsilon$-approximate monotonicity along $C(\delta)$ (Theorem~\ref{thm:monotone}), which reduces $K^2$ dimensions to a scalar; define three ASV diagnostics for topology-dependent failure modes; and combine ASVs with FWL invariance to route corrections.
90	
91	\paragraph{Parameterization.}
92	We set $C(\delta) = (1{-}\delta)I + \delta C_0$, where $C_0$ is a reference confusion matrix and $\delta \in [0,1]$ controls severity ($\delta{=}0$: perfect; $\delta{=}1$: matches $C_0$). This linear path is one of many in the column-stochastic polytope from $I$ to $C_0$; ASV thresholds are path-dependent, but our bootstrap procedure (Section~\ref{sec:asv_results}) captures estimation uncertainty along the empirical path. We recommend bootstrapping $C_0$ and reporting ASV confidence intervals (Appendix~\ref{sec:bootstrap_asv}).
93	\paragraph{Three ASV types.}
94	We define three complementary measures: (1)~\textbf{Magnitude ASV} $\delta^*_{\text{mag}} = \min\{\delta : |\operatorname{plim}\;\hat{\tau}(C(\delta)) - \tau| > \epsilon\}$, analogous to E-values; (2)~\textbf{Significance ASV} $\delta^*_{\text{sig}} = \min\{\delta : |\operatorname{plim}\;\hat{\tau}(C(\delta))| < z_{\alpha/2} \cdot SE(N)\}$, relevant for attenuating topologies; (3)~\textbf{Sign-flip ASV} $\delta^*_{\text{sf}} = \min\{\delta : \operatorname{sign}(\hat{\tau}) \neq \operatorname{sign}(\tau)\}$, for exposure and IV only. The significance ASV depends on $N$ through $SE(N)$, exhibiting a sharp phase transition at a critical $N^*$ below which all rejections are blocked.
95	
96	\begin{theorem}[Envelope monotonicity, $K{=}2$]
97	\label{thm:monotone}
98	For $K{=}2$ confounding and mediation topologies with proportional effects ($f = \lambda g$ for some scalar $\lambda$) under $C(\delta) = (1{-}\delta)I + \delta C_0$ with $(C_0)_{jj} \geq \tfrac{1}{2}$, $|B(C(\delta))|$ is monotonically non-decreasing in $\delta \in [0,1]$.
99	\end{theorem}
100	
101	The proof (Appendix~\ref{app:monotonicity_proof},~\ref{par:med_monotone}) exploits perspective function convexity. Proportional effects ($f{=}\lambda g$) is plausible when overall annotation competence drives both paths; all 23 empirical configurations preserve sign, with 97.3\% under non-proportional effects (Appendix~\ref{sec:proportional_effects}).
102	
103	\begin{theorem}[$K{=}3$ symmetric monotonicity]
104	\label{thm:k3_symmetric}
105	For $K{=}3$ with symmetric confusion matrix $C_{jk} = c$ for $j \neq k$ and $C_{kk} = 1{-}2c$, $c \in (0, 1/3)$, and proportional effects ($f{=}\lambda g$), envelope monotonicity holds exactly: $|B(C(\delta))|$ is strictly monotone in $\delta$ for confounding, mediation, and collider topologies whenever $\mathrm{Var}(g) > 0$.
106	\end{theorem}
107	
108	Theorem~\ref{thm:k3_symmetric} anchors exact monotonicity at $K{=}3$; for general asymmetric matrices ($d_{\mathrm{rel}}{=}0.33$; Remark~\ref{rem:symmetry}), Conjecture~\ref{conj:monotone} provides $\varepsilon < 0.017$ coverage. The proof exploits the reduction $s = c\delta$ (Appendix~\ref{app:k3_symmetric_proof}).
109	
110	\paragraph{From proofs to numerical evidence.}
111	Exact monotonicity (Theorems~\ref{thm:monotone}--\ref{thm:k3_symmetric}) does not extend to general $K{\geq}3$ column-stochastic structures; we state a conjecture supported by numerical evidence:
112	
113	\begin{conjecture}[$\varepsilon$-approximate envelope monotonicity]
114	\label{conj:monotone}
115	For general $K{\geq}3$ non-IV topologies under $C(\delta) = (1{-}\delta)I + \delta C_0$, $|B(C(\delta))|$ is $\varepsilon$-approximately monotonic with $\varepsilon < 0.02$ for $|\beta| \leq 1$, scaling with effect magnitude (Table~\ref{tab:conjecture_verify},~\ref{tab:dgp_sensitivity}; Appendix~\ref{sec:conjecture_verify}). The safe/fragile partition (five sign-preserving topologies versus exposure and IV) is robust across all tested parameterizations.
116	\end{conjecture}
117	
118	Numerical support spans 100{,}000 Dirichlet matrices and 545{,}945 adversarial curves (Appendix~\ref{app:adversarial_monotonicity}).
119	
120	\begin{remark}[ASV and E-values as complementary tools]
121	\label{rem:evalue}
122	ASV and E-values~\cite{vanderweele_ding2017} address orthogonal sources (annotation error vs.\ unmeasured confounding) and are most valuable jointly (Table~\ref{tab:sensitivity_comparison}, Appendix). ASV is topology-dependent and targets sign-flip failure modes absent from confounding analysis.
123	\end{remark}
124	
125	Under alternating-sign effects ($\boldsymbol{\beta}{=}[0,\,1.0,\,-0.5]$), magnitude ASV ranges from 0.09 (exposure) to $\infty$ (M-bias), a $4{\times}$ difference determined by topology (Table~\ref{tab:asv_stability}). Sign-flip ASV $< 1$ flags sign-reversal-prone pairs; magnitude ASV $< \delta_{\text{observed}}$ indicates bias exceeds tolerance (Algorithm~\ref{alg:correction}); the safe/fragile partition is stable across parameterizations ($\varepsilon < 0.02$; Appendix~\ref{sec:asv_stability}).
126	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c485d149-0aca-4ae1-83b9-bfb4f58cfb51",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "de0d4e23-0e8f-48b0-a662-06699bd6d435",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Setup and Notation}\n\\label{sec:notation}\n\nLet $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \\mid A{=}k)$, where each column sums to one (column-stochastic: each column gives the distribution of predicted labels for a given true label). Following \\citet{hernan_cole2009}, we represent this measurement process using \\emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.\n\n\\paragraph{Notation conventions.}\nOur analysis characterizes probability limits ($N \\to \\infty$) under the FWL theorem~\\cite{frisch1933partial}, which explains why matrix-based corrections fail for covariate topologies (Section~\\ref{sec:correction}). Notation is collected in Table~\\ref{tab:notation} (Appendix~\\ref{app:notation_table}).\n\n\\begin{definition}[Non-differential misclassification]\n\\label{def:nondiff}\nMisclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\\mathbf{Z}$ if $P(A^*{=}j \\mid A{=}k, Y, \\mathbf{Z}) = P(A^*{=}j \\mid A{=}k) = C_{jk}$ for all $j,k$.\n\\end{definition}\n\nIn batch annotation pipelines, the LLM processes each text independently without access to $Y$, making non-differentiality an architectural invariant~\\cite{ziems2024can}; Y-stratified permutation tests confirm this (1/12 rejection at $\\alpha{=}0.05$; Appendix~\\ref{sec:y_stratified_test}). Non-differentiality may be violated when $Y$ correlates with text content, in which case our Y-stratified test provides empirical verification. Under stress testing, sign reversal occurs in 14/16 $K{\\geq}3$ exposure configurations at $\\eta{=}0.01$ structured departure (Appendix~\\ref{sec:nondiff_stress}).\n\nThroughout, $\\tau$ denotes the causal estimand of interest, whose definition varies by topology: the confounder's coefficient, the treatment effect, the indirect effect, or the Wald ratio (Appendix~\\ref{app:confounding}ff.).\n\nWe study seven canonical DAG topologies (Figure~\\ref{fig:dag_taxonomy})~\\cite{pearl2009, hernan2020causal}, deriving probability limits under linear structural equation models (SEMs)~\\cite{carroll2006}; logistic regression robustness is verified in Appendix~\\ref{sec:logistic_dgp} and~\\ref{sec:fwl_nonlinear}.\n\n\\subsection{Multi-Class Bias Expressions}\n\\label{sec:bias_expressions}\n\nFor each topology, we derive the $\\operatorname{plim}$\\footnote{The probability limit (plim) is the value to which an estimator converges as sample size $N \\to \\infty$; it characterizes systematic bias separately from sampling variability.} of the naive estimator that substitutes $A^*$ for $A$. Let $\\tau$ denote the target causal parameter, whose precise definition is topology-specific (e.g., the coefficient on $X$ for confounding, the category-specific $\\beta_j$ for exposure, or the direct effect $\\tau_{\\text{direct}}$ for mediation), and $\\hat{\\tau}(A^*)$ the estimator using misclassified annotations.\n\n\\paragraph{Confounding ($A$ = confounder).}\nWhen $A$ confounds the $X{\\to}Y$ relationship, the ordinary least squares (OLS) estimator controlling for $A^*$ has probability limit\n\\begin{equation}\n\\label{eq:confounding}\n\\operatorname{plim}\\;\\hat{\\tau}(A^*) = \\bigl(\\mathbb{E}[Z^{\\prime}Z]\\bigr)^{-1}\\mathbb{E}[Z^{\\prime}X]\\,\\boldsymbol{\\beta},\n\\end{equation}\nwhere $Z = [X, \\text{dummies}(A^*)]$, $\\boldsymbol{\\beta}$ contains the true coefficients, and the target parameter $\\tau$ is the coefficient on $X$. Misclassification produces residual confounding that monotonically approaches the omitted variable bias, but the sign of $\\hat{\\tau}$ is preserved: $\\tau_{\\text{sign\\_flip}} = 0$ structurally.\\footnote{Consistent with \\citet{brenner1993}: misclassification degrades confounding control, producing amplification ($|\\hat{\\tau}| > |\\tau|$, universal in this topology) but never sign reversal ($\\operatorname{sign}(\\hat{\\tau}) \\neq \\operatorname{sign}(\\tau)$).}\n\n\\paragraph{Exposure ($A$ = treatment variable).}\nWhen $A$ is the exposure of interest, the biased coefficient for category $j$ becomes a weighted combination of true coefficients:\n\\begin{equation}\n\\label{eq:exposure}\n\\operatorname{plim}\\;\\hat{\\beta}_j(A^*) = \\sum_{k=1}^{K} w_{jk}\\,\\beta_k,\n\\end{equation}\nwhere $w_{jk}$ depends on the confusion matrix $C$ and the population marginal $\\pi_k = P(A{=}k)$. Unlike binary misclassification~\\cite{brenner1993}, $K{\\geq}3$ permits $w_{jk}$ to assign negative weight to categories with opposite-sign coefficients, producing \\emph{sign reversal} (83.4\\% under uniform Dirichlet prior); this is structurally impossible at $K{=}2$.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig2_bias_distribution.pdf}\n\\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices (uniform Dirichlet; realistic-accuracy results in Section~\\ref{sec:taxonomy_results}). Red = sign reversal. Exposure: 83.4\\% sign reversal; IV: 52.6\\%.}\n\\label{fig:bias_distribution}\n\\end{figure*}\n\n\\paragraph{Primary coefficient preservation.}\nAcross 23 empirical LLM configurations, the primary coefficient (the category with the largest true effect $|\\beta_k|$) never reverses sign, while 61\\% reverse a secondary (non-dominant) coefficient, confirmed under 100{,}000 Dirichlet matrices with diagonal ${\\geq}\\,0.7$ across six beta-ratio conditions (1.0 to 50.0) with 0\\% primary sign-flip (Appendix~\\ref{app:exposure}).\n\n\\paragraph{Mediation ($A$ = mediator).}\nWhen $A$ mediates the $X{\\to}Y$ relationship~\\cite{vanderweele2015explanation}, the direct effect estimator controlling for $A^*$ has probability limit\n\\begin{equation}\n\\label{eq:mediation}\n\\operatorname{plim}\\;\\hat{\\tau}_{\\text{direct}}(A^*) = \\tau_{\\text{direct}} + \\bigl(1 - \\lambda(C)\\bigr)\\,\\tau_{\\text{indirect}},\n\\end{equation}\nwhere $\\lambda(C) \\in [0,1]$ under proportional effects (Appendix~\\ref{app:proof}, Proposition~\\ref{prop:lambda_bound}), with $\\lambda(I) = 1$ under perfect classification. Misclassification ($\\lambda < 1$) causes the residual indirect effect to be absorbed into the direct path estimate, producing upward bias in $|\\hat{\\tau}_{\\text{direct}}|$ but preserving the sign ($\\tau_{\\text{sign\\_flip}} = 0$).\n\n\\paragraph{Collider, M-bias, and front-door.}\nThree topologies exhibit protective or immune behavior. \\textbf{Collider:} conditioning on $A^*$ instead of $A$ attenuates Berkson bias by weakening the spurious path, so annotation error is protective ($\\tau_{\\text{sign\\_flip}} = 0$). \\textbf{M-bias:} in the M-shaped DAG~\\cite{greenland2003}, misclassifying $A$ attenuates the non-causal path, making this topology immune ($\\text{ASV} = \\infty$). \\textbf{Front-door:} the front-door estimator~\\cite{bellemare_bloem2024} requires two stages ($X \\to A$ and $A \\to Y$), each attenuated by $C$; the compound effect produces moderate bias with $\\tau_{\\text{sign\\_flip}} = 0$.\n\n\\paragraph{Instrumental variable ($A$ = instrument).}\nThe Wald estimator~\\cite{angrist_imbens1995} $\\hat{\\tau}_{\\text{IV}} = \\hat{\\text{cov}}(A^*, Y) / \\hat{\\text{cov}}(A^*, X)$ has $C$ in the denominator. Misclassification can drive first-stage coefficients toward zero or reverse their sign; under random Dirichlet matrices, 52.6\\% produce sign reversal; IV is the most fragile topology (Appendix~\\ref{sec:iv_dirichlet_subspace}).\n\n\\paragraph{Structural sign-flip guarantee.}\n\\begin{proposition}[Sign preservation: analytic results]\n\\label{prop:signflip}\nUnder non-differential misclassification with $C_{kk} > 0$ for all $k$:\n\\emph{(a)}~Confounding preserves sign when $\\operatorname{sign}(\\tau) = \\operatorname{sign}(\\tau {+} B_{\\mathrm{OV}})$, where $B_{\\mathrm{OV}} {=} \\operatorname{Cov}(g(A),f(A))/\\operatorname{Var}(T)$ is the omitted-variable bias (Cauchy--Schwarz; Appendix~\\ref{app:confounding}).\n\\emph{(b)}~Collider preserves sign when $|\\tau| > \\sqrt{\\operatorname{Var}(g)\\operatorname{Var}(h)}/\\mathbb{E}[\\operatorname{Var}(T{\\mid}A)]$ (Berkson attenuation; Appendix~\\ref{app:collider}); empirically verified across 100{,}000 matrices with zero violations.\n\\emph{(c)}~Exposure can produce sign reversal for $K {\\geq} 3$, even with $C_{kk} {>} 0.5$ (counterexample in Appendix~\\ref{app:exposure}).\n\\end{proposition}\n\nSign preservation for non-exposure topologies holds under topology-specific conditions (Table~\\ref{tab:sign_conditions}, Appendix~\\ref{app:conditions}), verified across 100{,}000 random matrices with zero violations; analytic proofs for general $K$ remain open.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig3_asv_ranking.pdf}\n\\caption{ASV vulnerability ranking across topologies. Three ASV types (magnitude, significance, sign-flip) reveal a topology-dependent spectrum from IV (maximally fragile) to M-bias (immune, ASV $= \\infty$).}\n\\label{fig:asv_ranking}\n\\end{figure*}\n\n\\subsection{Annotation Sensitivity Values}\n\\label{sec:asv}\n\nWe adapt the sensitivity analysis paradigm (E-values~\\cite{vanderweele_ding2017}, partial-$R^2$ bounds~\\cite{cinelli2020making}, coefficient stability~\\cite{oster2019}) to $K{\\times}K$ annotation error and define Annotation Sensitivity Values (ASVs): we prove $\\varepsilon$-approximate monotonicity along $C(\\delta)$ (Theorem~\\ref{thm:monotone}), which reduces $K^2$ dimensions to a scalar; define three ASV diagnostics for topology-dependent failure modes; and combine ASVs with FWL invariance to route corrections.\n\n\\paragraph{Parameterization.}\nWe set $C(\\delta) = (1{-}\\delta)I + \\delta C_0$, where $C_0$ is a reference confusion matrix and $\\delta \\in [0,1]$ controls severity ($\\delta{=}0$: perfect; $\\delta{=}1$: matches $C_0$). This linear path is one of many in the column-stochastic polytope from $I$ to $C_0$; ASV thresholds are path-dependent, but our bootstrap procedure (Section~\\ref{sec:asv_results}) captures estimation uncertainty along the empirical path. We recommend bootstrapping $C_0$ and reporting ASV confidence intervals (Appendix~\\ref{sec:bootstrap_asv}).\n\\paragraph{Three ASV types.}\nWe define three complementary measures: (1)~\\textbf{Magnitude ASV} $\\delta^*_{\\text{mag}} = \\min\\{\\delta : |\\operatorname{plim}\\;\\hat{\\tau}(C(\\delta)) - \\tau| > \\epsilon\\}$, analogous to E-values; (2)~\\textbf{Significance ASV} $\\delta^*_{\\text{sig}} = \\min\\{\\delta : |\\operatorname{plim}\\;\\hat{\\tau}(C(\\delta))| < z_{\\alpha/2} \\cdot SE(N)\\}$, relevant for attenuating topologies; (3)~\\textbf{Sign-flip ASV} $\\delta^*_{\\text{sf}} = \\min\\{\\delta : \\operatorname{sign}(\\hat{\\tau}) \\neq \\operatorname{sign}(\\tau)\\}$, for exposure and IV only. The significance ASV depends on $N$ through $SE(N)$, exhibiting a sharp phase transition at a critical $N^*$ below which all rejections are blocked.\n\n\\begin{theorem}[Envelope monotonicity, $K{=}2$]\n\\label{thm:monotone}\nFor $K{=}2$ confounding and mediation topologies with proportional effects ($f = \\lambda g$ for some scalar $\\lambda$) under $C(\\delta) = (1{-}\\delta)I + \\delta C_0$ with $(C_0)_{jj} \\geq \\tfrac{1}{2}$, $|B(C(\\delta))|$ is monotonically non-decreasing in $\\delta \\in [0,1]$.\n\\end{theorem}\n\nThe proof (Appendix~\\ref{app:monotonicity_proof},~\\ref{par:med_monotone}) exploits perspective function convexity. Proportional effects ($f{=}\\lambda g$) is plausible when overall annotation competence drives both paths; all 23 empirical configurations preserve sign, with 97.3\\% under non-proportional effects (Appendix~\\ref{sec:proportional_effects}).\n\n\\begin{theorem}[$K{=}3$ symmetric monotonicity]\n\\label{thm:k3_symmetric}\nFor $K{=}3$ with symmetric confusion matrix $C_{jk} = c$ for $j \\neq k$ and $C_{kk} = 1{-}2c$, $c \\in (0, 1/3)$, and proportional effects ($f{=}\\lambda g$), envelope monotonicity holds exactly: $|B(C(\\delta))|$ is strictly monotone in $\\delta$ for confounding, mediation, and collider topologies whenever $\\mathrm{Var}(g) > 0$.\n\\end{theorem}\n\nTheorem~\\ref{thm:k3_symmetric} anchors exact monotonicity at $K{=}3$; for general asymmetric matrices ($d_{\\mathrm{rel}}{=}0.33$; Remark~\\ref{rem:symmetry}), Conjecture~\\ref{conj:monotone} provides $\\varepsilon < 0.017$ coverage. The proof exploits the reduction $s = c\\delta$ (Appendix~\\ref{app:k3_symmetric_proof}).\n\n\\paragraph{From proofs to numerical evidence.}\nExact monotonicity (Theorems~\\ref{thm:monotone}--\\ref{thm:k3_symmetric}) does not extend to general $K{\\geq}3$ column-stochastic structures; we state a conjecture supported by numerical evidence:\n\n\\begin{conjecture}[$\\varepsilon$-approximate envelope monotonicity]\n\\label{conj:monotone}\nFor general $K{\\geq}3$ non-IV topologies under $C(\\delta) = (1{-}\\delta)I + \\delta C_0$, $|B(C(\\delta))|$ is $\\varepsilon$-approximately monotonic with $\\varepsilon < 0.02$ for $|\\beta| \\leq 1$, scaling with effect magnitude (Table~\\ref{tab:conjecture_verify},~\\ref{tab:dgp_sensitivity}; Appendix~\\ref{sec:conjecture_verify}). The safe/fragile partition (five sign-preserving topologies versus exposure and IV) is robust across all tested parameterizations.\n\\end{conjecture}\n\nNumerical support spans 100{,}000 Dirichlet matrices and 545{,}945 adversarial curves (Appendix~\\ref{app:adversarial_monotonicity}).\n\n\\begin{remark}[ASV and E-values as complementary tools]\n\\label{rem:evalue}\nASV and E-values~\\cite{vanderweele_ding2017} address orthogonal sources (annotation error vs.\\ unmeasured confounding) and are most valuable jointly (Table~\\ref{tab:sensitivity_comparison}, Appendix). ASV is topology-dependent and targets sign-flip failure modes absent from confounding analysis.\n\\end{remark}\n\nUnder alternating-sign effects ($\\boldsymbol{\\beta}{=}[0,\\,1.0,\\,-0.5]$), magnitude ASV ranges from 0.09 (exposure) to $\\infty$ (M-bias), a $4{\\times}$ difference determined by topology (Table~\\ref{tab:asv_stability}). Sign-flip ASV $< 1$ flags sign-reversal-prone pairs; magnitude ASV $< \\delta_{\\text{observed}}$ indicates bias exceeds tolerance (Algorithm~\\ref{alg:correction}); the safe/fragile partition is stable across parameterizations ($\\varepsilon < 0.02$; Appendix~\\ref{sec:asv_stability}).\n",
      "numLines": 126,
      "startLine": 1,
      "totalLines": 126
    }
  },
  "sourceToolAssistantUUID": "c485d149-0aca-4ae1-83b9-bfb4f58cfb51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-25T08:23:25.369Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NbxndL5qQFkV5oPjgBRenC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de0d4e23-0e8f-48b0-a662-06699bd6d435",
  "isSidechain": false,
  "requestId": "req_011CbNxv8mXTejhBT9P2pLrN",
  "type": "assistant",
  "uuid": "ac578cac-d91d-4287-bc2f-205552ddf1b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXWWF9ogGXcabKsU1RyxvV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12102,
      "cache_read_input_tokens": 39699,
      "output_tokens": 635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12102,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 635,
          "cache_read_input_tokens": 39699,
          "cache_creation_input_tokens": 12102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12102
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-25T08:23:25.381Z_

<details><summary>↩ Tool result · `toolu_01NbxndL5qQFkV5oPjgBRenC`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate through Monte Carlo simulation ($K{=}3$), cross-$K$ robustness checks ($K{=}5,7$), and empirical validation with real LLM confusion matrices from three natural language processing (NLP) tasks ($K{=}2,3,10$).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each topology, we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute analytical probability limits, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with mean absolute percentage error (MAPE) of 1.6\%, averaged across 161 scenarios (23 LLM configurations $\times$ 7 topologies; per-topology range: 0.3\%--3.7\%). This close agreement validates the closed-form derivations and confirms that finite-sample behavior ($N{=}10{,}000$) closely approximates the asymptotic predictions. This justifies the use of probability limits as practical bias diagnostics.
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under realistic accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; at diagonal $\geq 0.9$, violation persists at 11.9\% (Appendix~\ref{sec:iv_dirichlet_subspace}). Under the full Dirichlet prior, 85\% of matrices violate the binary ``toward-null'' guarantee and 83.4\% cause sign reversal; $\min_k C_{kk} < 0.55$ predicts sign reversal with 91\% accuracy (Appendix~\ref{sec:sign_determinants}). The $K{=}2$ control confirms classical attenuation~\cite{brenner1993}. This establishes the multi-class failure as structurally distinct.
19	
20	\paragraph{Structural guarantee for non-exposure topologies.}
21	Five topologies exhibit zero sign-flip rate (Table~\ref{tab:taxonomy}): confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse the sign; collider is protective ($|B(C)|$ non-increasing; Conjecture~\ref{conj:monotone}); M-bias shows weakest sensitivity (53.2\% violation). All patterns persist at $K{=}5,7$ (Appendix~\ref{sec:cross_k_robustness}).
22	
23	\paragraph{IV: Wald estimator instability.}
24	The IV topology is the sole non-exposure exception: 52.6\% of random matrices cause sign reversal, stable across $K{=}3,5,7$. Diagonal dominance ($C_{kk} > 0.5$) eliminates sign reversal but preserves amplification (Appendix~\ref{sec:iv_dirichlet_subspace}); however, all 23 empirical LLM configurations show zero IV sign reversal.
25	
26	\begin{table}[t]
27	\centering
28	\caption{Bias under $K{=}3$ non-differential misclassification (100{,}000 Dirichlet$(1,1,1)$ matrices). Violation: $|\text{bias}| > 0$; Sign Flip: any coefficient reverses sign; Amplif.: $|\hat{\tau}| > |\tau|$. $\tau_{\text{sf}}{=}0$?: sign-flip guarantee holds unconditionally (Yes), conditionally (Cond.; Proposition~\ref{prop:signflip}), or not (No). Collider 100\% amplification reflects Berkson bias; misclassification is protective.}
29	\label{tab:taxonomy}
30	\small
31	\resizebox{\columnwidth}{!}{\begin{tabular}{lcccc}
32	\toprule
33	\textbf{Topology} & \textbf{Violation} & \textbf{Sign Flip} & \textbf{Amplif.} & $\tau_{\text{sf}}{=}0$? \\
34	\midrule
35	Confounding & 100\% & 0\% & 100\% & Cond. \\
36	Exposure & 85\% & 83.4\% & 14.1\% & No \\
37	Mediation & 100\% & 0\% & 100\% & Cond. \\
38	Front-door & 100\% & 0\% & 100\% & Cond. \\
39	Collider & 100\% & 0\% & 100\% & Cond. \\
40	M-bias & 53.2\% & 0\% & 10.4\% & Yes \\
41	IV & 100\% & 52.6\% & 100\% & No \\
42	\bottomrule
43	\end{tabular}}
44	\end{table}
45	
46	The bias distributions are visualized in Figure~\ref{fig:bias_distribution}. Figure~\ref{fig:dirichlet_overlay} overlays all 23 empirical LLM configurations onto the theoretical violation-rate curves; real-world accuracy ($\min_k C_{kk} \geq 0.6$) places all models in the low-risk region for IV but leaves exposure vulnerable.
47	
48	\begin{figure}[t]
49	\centering
50	\includegraphics[width=\columnwidth]{fig7_dirichlet_overlay.pdf}
51	\caption{Empirical LLM confusion matrices (markers) overlaid on theoretical violation-rate curves from $K{=}3$ Dirichlet analysis. Left: exposure; right: IV. Real-world accuracy places all models in the low-risk region for IV sign reversal but not for exposure.}
52	\label{fig:dirichlet_overlay}
53	\end{figure}
54	
55	\begin{figure}[t]
56	\centering
57	\includegraphics[width=\columnwidth]{fig5_f1_vs_bias.pdf}
58	\caption{Topology determines downstream causal bias, not $F_1$. HumAID $K{=}10$ (56 points): within $F_1$ range 0.614--0.690, bias varies $10{\times}$ (IV 42.1\% vs.\ collider $<$5.6\%).}
59	\label{fig:f1_vs_bias}
60	\end{figure}
61	
62	\subsection{ASV Framework Validation}
63	\label{sec:asv_results}
64	
65	\begin{table}[t]
66	\centering
67	\small
68	\caption{ASV summary across topologies ($K{=}3$, $\tau{=}0.5$). ---: not applicable.}
69	\label{tab:asv_summary}
70	\begin{tabular}{lccc}
71	\toprule
72	\textbf{Topology} & \textbf{Mag ASV} & \textbf{Power} & \textbf{Sign-flip} \\
73	\midrule
74	IV          & 0.10--0.61 & 0\%   & 1.1--6.7 \\
75	Front-door  & 0.06--0.39 & 100\% & --- \\
76	Confounding & 0.08--0.49 & 100\% & --- \\
77	Mediation   & 0.08--0.45 & 0\%   & --- \\
78	Collider    & 0.34--2.03 & 0\%   & --- \\
79	M-bias      & $\infty$   & 98\%  & --- \\
80	Exposure    & ---        & ---   & 83.4\% \\
81	\bottomrule
82	\end{tabular}
83	\end{table}
84	
85	\paragraph{ASV results.}
86	The ASV envelope is $\varepsilon$-approximately monotonic ($\varepsilon < 0.02$; Conjecture~\ref{conj:monotone}). Figure~\ref{fig:asv_ranking} shows the vulnerability ranking: IV is maximally fragile, M-bias is immune ($\text{ASV} = \infty$). Sign-flip ASV: 83.4\% of exposure matrices yield $\delta^*_{\text{sf}} < 1$; IV ranges 1.1--6.7 (Table~\ref{tab:asv_summary}). Significance ASV exhibits a phase transition at $N^* \approx 6{,}000$--$10{,}000$; bootstrap confidence intervals (CIs; $B{=}1{,}000$; Appendix~\ref{sec:bootstrap_asv}) confirm stable topology ranking, with the safe/fragile partition recovering reliably from $n_{\text{gold}} \geq 100$ (82\% stability).
87	
88	\subsection{Empirical Validation}
89	\label{sec:empirical}
90	
91	We validate using real LLM confusion matrices from HumAID~\cite{alam2021humaid} ($K{=}10$), VAST ($K{=}3$), and CivilComments ($K{=}2$): four LLMs, 23 configurations, 161 bias scenarios. HumAID ($K{=}10$) matches predictions: IV (12.4--42.1\%) and exposure (9.0--17.4\%) dominate; remaining topologies $<$15\%. $F_1$ does not exhibit significant rank correlation with bias ($\rho = -0.10$, $p = 0.45$; Figure~\ref{fig:f1_vs_bias}), but per-topology patterns diverge ($\rho \leq -0.53$ for five topologies vs.\ $0.87$ for M-bias; Appendix~\ref{sec:within_topo_f1}). Of exposure coefficients, 14/23 (61\%) exhibit sign reversal, all secondary; zero across 138 non-exposure scenarios. This decoupling between annotation accuracy and causal bias underscores that practitioners cannot rely on $F_1$ as a proxy for causal validity; topology assessment must precede any downstream inference.
92	
93	\subsection{Correction Guidance}
94	\label{sec:correction}
95	
96	\begin{figure}[t]
97	\centering
98	\includegraphics[width=\columnwidth]{fig4_binarization.pdf}
99	\caption{Binarization collapse $\Delta$: additional bias from collapsing $K{=}3$ to binary. Topology determines severity ($>$150$\times$ range); exposure and IV exhibit sign flips.}
100	\label{fig:binarization}
101	\end{figure}
102	
103	We evaluate five correction methods (naive plug-in, maximum likelihood adjustment (MLA), DSL~\cite{egami_hinck_stewart_wei2023}, Monte Carlo simulation extrapolation (MC-SIMEX)~\cite{kuchenhoff2006simex}, PPI++~\cite{angelopoulos2023}) across all topologies (210 configurations; Table~\ref{tab:correction}, Appendix~\ref{app:supplementary}).
104	
105	\paragraph{FWL invariance.}
106	Under linear regression, FWL invariance renders matrix-based methods (naive plug-in, MLA) provably ineffective for covariate topologies (0\% bias reduction; Appendix~\ref{app:fwl_proof}): the treatment coefficient depends only on the projection orthogonal to the covariate space, so relabeling $A^* \to A$ leaves the coefficient unchanged. Under logistic regression this invariance breaks, but the method ranking persists ($|\Delta| < 0.02$; Appendix~\ref{sec:fwl_nonlinear}).
107	
108	\paragraph{Method ranking and decision procedure.}
109	PPI++ achieves the highest root mean squared error (RMSE) reduction (47.0\% at $K{=}3$) but requires gold labels and harms M-bias ($-$88\%); MC-SIMEX is gold-free and $K$-robust (27--70\%), though it harms front-door ($-$62.4\%); rankings are stable across $K$ ($\rho \geq 0.80$; Appendix~\ref{sec:correction_k_sensitivity}). Algorithm~\ref{alg:correction} (Appendix) routes through risk assessment, method selection, and FWL screening. End-to-end demos (Table~\ref{tab:e2e-demo}; Appendix~\ref{sec:real_cm_demo}) validate: PPI++ reduces exposure bias from 42.9\% to 0.2\%, while topology-agnostic IV correction amplifies bias ($-$139\%). Collapsing $K{=}3$ to binary is not a safe fallback: the additional bias $\Delta$ varies $>$150$\times$ by topology (Figure~\ref{fig:binarization}).
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac578cac-d91d-4287-bc2f-205552ddf1b7",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "007ee0c0-1e56-466a-8409-1dfe79fb30c4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe validate through Monte Carlo simulation ($K{=}3$), cross-$K$ robustness checks ($K{=}5,7$), and empirical validation with real LLM confusion matrices from three natural language processing (NLP) tasks ($K{=}2,3,10$).\n\n\\subsection{Setup}\n\\label{sec:setup}\n\nFor each topology, we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute analytical probability limits, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\\delta) = (1{-}\\delta)I + \\delta C_0$.\n\n\\subsection{Bias Taxonomy}\n\\label{sec:taxonomy_results}\n\n\\paragraph{Theory-MC agreement.}\nAnalytical probability limits match Monte Carlo estimates with mean absolute percentage error (MAPE) of 1.6\\%, averaged across 161 scenarios (23 LLM configurations $\\times$ 7 topologies; per-topology range: 0.3\\%--3.7\\%). This close agreement validates the closed-form derivations and confirms that finite-sample behavior ($N{=}10{,}000$) closely approximates the asymptotic predictions. This justifies the use of probability limits as practical bias diagnostics.\n\n\\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}\nUnder realistic accuracy (diagonal $\\geq 0.7$), the violation rate is 13.7\\% with 2.1\\% sign reversal; at diagonal $\\geq 0.9$, violation persists at 11.9\\% (Appendix~\\ref{sec:iv_dirichlet_subspace}). Under the full Dirichlet prior, 85\\% of matrices violate the binary ``toward-null'' guarantee and 83.4\\% cause sign reversal; $\\min_k C_{kk} < 0.55$ predicts sign reversal with 91\\% accuracy (Appendix~\\ref{sec:sign_determinants}). The $K{=}2$ control confirms classical attenuation~\\cite{brenner1993}. This establishes the multi-class failure as structurally distinct.\n\n\\paragraph{Structural guarantee for non-exposure topologies.}\nFive topologies exhibit zero sign-flip rate (Table~\\ref{tab:taxonomy}): confounding, mediation, and front-door show 100\\% amplification~\\cite{brenner1993, dosemeci1990} but never reverse the sign; collider is protective ($|B(C)|$ non-increasing; Conjecture~\\ref{conj:monotone}); M-bias shows weakest sensitivity (53.2\\% violation). All patterns persist at $K{=}5,7$ (Appendix~\\ref{sec:cross_k_robustness}).\n\n\\paragraph{IV: Wald estimator instability.}\nThe IV topology is the sole non-exposure exception: 52.6\\% of random matrices cause sign reversal, stable across $K{=}3,5,7$. Diagonal dominance ($C_{kk} > 0.5$) eliminates sign reversal but preserves amplification (Appendix~\\ref{sec:iv_dirichlet_subspace}); however, all 23 empirical LLM configurations show zero IV sign reversal.\n\n\\begin{table}[t]\n\\centering\n\\caption{Bias under $K{=}3$ non-differential misclassification (100{,}000 Dirichlet$(1,1,1)$ matrices). Violation: $|\\text{bias}| > 0$; Sign Flip: any coefficient reverses sign; Amplif.: $|\\hat{\\tau}| > |\\tau|$. $\\tau_{\\text{sf}}{=}0$?: sign-flip guarantee holds unconditionally (Yes), conditionally (Cond.; Proposition~\\ref{prop:signflip}), or not (No). Collider 100\\% amplification reflects Berkson bias; misclassification is protective.}\n\\label{tab:taxonomy}\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Topology} & \\textbf{Violation} & \\textbf{Sign Flip} & \\textbf{Amplif.} & $\\tau_{\\text{sf}}{=}0$? \\\\\n\\midrule\nConfounding & 100\\% & 0\\% & 100\\% & Cond. \\\\\nExposure & 85\\% & 83.4\\% & 14.1\\% & No \\\\\nMediation & 100\\% & 0\\% & 100\\% & Cond. \\\\\nFront-door & 100\\% & 0\\% & 100\\% & Cond. \\\\\nCollider & 100\\% & 0\\% & 100\\% & Cond. \\\\\nM-bias & 53.2\\% & 0\\% & 10.4\\% & Yes \\\\\nIV & 100\\% & 52.6\\% & 100\\% & No \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe bias distributions are visualized in Figure~\\ref{fig:bias_distribution}. Figure~\\ref{fig:dirichlet_overlay} overlays all 23 empirical LLM configurations onto the theoretical violation-rate curves; real-world accuracy ($\\min_k C_{kk} \\geq 0.6$) places all models in the low-risk region for IV but leaves exposure vulnerable.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig7_dirichlet_overlay.pdf}\n\\caption{Empirical LLM confusion matrices (markers) overlaid on theoretical violation-rate curves from $K{=}3$ Dirichlet analysis. Left: exposure; right: IV. Real-world accuracy places all models in the low-risk region for IV sign reversal but not for exposure.}\n\\label{fig:dirichlet_overlay}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_f1_vs_bias.pdf}\n\\caption{Topology determines downstream causal bias, not $F_1$. HumAID $K{=}10$ (56 points): within $F_1$ range 0.614--0.690, bias varies $10{\\times}$ (IV 42.1\\% vs.\\ collider $<$5.6\\%).}\n\\label{fig:f1_vs_bias}\n\\end{figure}\n\n\\subsection{ASV Framework Validation}\n\\label{sec:asv_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{ASV summary across topologies ($K{=}3$, $\\tau{=}0.5$). ---: not applicable.}\n\\label{tab:asv_summary}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Topology} & \\textbf{Mag ASV} & \\textbf{Power} & \\textbf{Sign-flip} \\\\\n\\midrule\nIV          & 0.10--0.61 & 0\\%   & 1.1--6.7 \\\\\nFront-door  & 0.06--0.39 & 100\\% & --- \\\\\nConfounding & 0.08--0.49 & 100\\% & --- \\\\\nMediation   & 0.08--0.45 & 0\\%   & --- \\\\\nCollider    & 0.34--2.03 & 0\\%   & --- \\\\\nM-bias      & $\\infty$   & 98\\%  & --- \\\\\nExposure    & ---        & ---   & 83.4\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{ASV results.}\nThe ASV envelope is $\\varepsilon$-approximately monotonic ($\\varepsilon < 0.02$; Conjecture~\\ref{conj:monotone}). Figure~\\ref{fig:asv_ranking} shows the vulnerability ranking: IV is maximally fragile, M-bias is immune ($\\text{ASV} = \\infty$). Sign-flip ASV: 83.4\\% of exposure matrices yield $\\delta^*_{\\text{sf}} < 1$; IV ranges 1.1--6.7 (Table~\\ref{tab:asv_summary}). Significance ASV exhibits a phase transition at $N^* \\approx 6{,}000$--$10{,}000$; bootstrap confidence intervals (CIs; $B{=}1{,}000$; Appendix~\\ref{sec:bootstrap_asv}) confirm stable topology ranking, with the safe/fragile partition recovering reliably from $n_{\\text{gold}} \\geq 100$ (82\\% stability).\n\n\\subsection{Empirical Validation}\n\\label{sec:empirical}\n\nWe validate using real LLM confusion matrices from HumAID~\\cite{alam2021humaid} ($K{=}10$), VAST ($K{=}3$), and CivilComments ($K{=}2$): four LLMs, 23 configurations, 161 bias scenarios. HumAID ($K{=}10$) matches predictions: IV (12.4--42.1\\%) and exposure (9.0--17.4\\%) dominate; remaining topologies $<$15\\%. $F_1$ does not exhibit significant rank correlation with bias ($\\rho = -0.10$, $p = 0.45$; Figure~\\ref{fig:f1_vs_bias}), but per-topology patterns diverge ($\\rho \\leq -0.53$ for five topologies vs.\\ $0.87$ for M-bias; Appendix~\\ref{sec:within_topo_f1}). Of exposure coefficients, 14/23 (61\\%) exhibit sign reversal, all secondary; zero across 138 non-exposure scenarios. This decoupling between annotation accuracy and causal bias underscores that practitioners cannot rely on $F_1$ as a proxy for causal validity; topology assessment must precede any downstream inference.\n\n\\subsection{Correction Guidance}\n\\label{sec:correction}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_binarization.pdf}\n\\caption{Binarization collapse $\\Delta$: additional bias from collapsing $K{=}3$ to binary. Topology determines severity ($>$150$\\times$ range); exposure and IV exhibit sign flips.}\n\\label{fig:binarization}\n\\end{figure}\n\nWe evaluate five correction methods (naive plug-in, maximum likelihood adjustment (MLA), DSL~\\cite{egami_hinck_stewart_wei2023}, Monte Carlo simulation extrapolation (MC-SIMEX)~\\cite{kuchenhoff2006simex}, PPI++~\\cite{angelopoulos2023}) across all topologies (210 configurations; Table~\\ref{tab:correction}, Appendix~\\ref{app:supplementary}).\n\n\\paragraph{FWL invariance.}\nUnder linear regression, FWL invariance renders matrix-based methods (naive plug-in, MLA) provably ineffective for covariate topologies (0\\% bias reduction; Appendix~\\ref{app:fwl_proof}): the treatment coefficient depends only on the projection orthogonal to the covariate space, so relabeling $A^* \\to A$ leaves the coefficient unchanged. Under logistic regression this invariance breaks, but the method ranking persists ($|\\Delta| < 0.02$; Appendix~\\ref{sec:fwl_nonlinear}).\n\n\\paragraph{Method ranking and decision procedure.}\nPPI++ achieves the highest root mean squared error (RMSE) reduction (47.0\\% at $K{=}3$) but requires gold labels and harms M-bias ($-$88\\%); MC-SIMEX is gold-free and $K$-robust (27--70\\%), though it harms front-door ($-$62.4\\%); rankings are stable across $K$ ($\\rho \\geq 0.80$; Appendix~\\ref{sec:correction_k_sensitivity}). Algorithm~\\ref{alg:correction} (Appendix) routes through risk assessment, method selection, and FWL screening. End-to-end demos (Table~\\ref{tab:e2e-demo}; Appendix~\\ref{sec:real_cm_demo}) validate: PPI++ reduces exposure bias from 42.9\\% to 0.2\\%, while topology-agnostic IV correction amplifies bias ($-$139\\%). Collapsing $K{=}3$ to binary is not a safe fallback: the additional bias $\\Delta$ varies $>$150$\\times$ by topology (Figure~\\ref{fig:binarization}).\n",
      "numLines": 110,
      "startLine": 1,
      "totalLines": 110
    }
  },
  "sourceToolAssistantUUID": "ac578cac-d91d-4287-bc2f-205552ddf1b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T08:23:25.668Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HUPivVuiCRno74fD4BdWpY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "007ee0c0-1e56-466a-8409-1dfe79fb30c4",
  "isSidechain": false,
  "requestId": "req_011CbNxv8mXTejhBT9P2pLrN",
  "type": "assistant",
  "uuid": "05f43707-bc09-4194-b36c-1de40b78f8b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXWWF9ogGXcabKsU1RyxvV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12102,
      "cache_read_input_tokens": 39699,
      "output_tokens": 635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12102,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 635,
          "cache_read_input_tokens": 39699,
          "cache_creation_input_tokens": 12102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12102
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-25T08:23:25.673Z_

<details><summary>↩ Tool result · `toolu_01HUPivVuiCRno74fD4BdWpY`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology: at $K{\geq}3$, exposure and IV can reverse treatment effect signs while five topologies preserve them. ASVs provide a topology-dependent vulnerability ranking; matrix-based corrections are provably ineffective for four covariate topologies (FWL invariance). Practitioners should identify the topology first: for exposure, PPI++ reduces bias from ${\sim}61\%$ to ${<}1\%$ (Table~\ref{tab:e2e-real-cm}); for IV, all tested corrections worsen the estimate. High $F_1$ does not guarantee low causal bias; topology assessment must precede downstream inference.
5	
6	Differential misclassification and proving Conjecture~\ref{conj:monotone} for general $K$ remain open.
7	
8	\section*{Limitations}
9	
10	Our closed-form results assume linear SEMs with proportional effects ($f{=}\lambda g$); sign preservation empirically holds at 97.3\% under non-proportional effects (Table~\ref{tab:proportional_empirical}), but recommendations do not directly extend to nonlinear models (matching, doubly-robust). The framework assumes a known DAG with non-differential misclassification (Appendix~\ref{sec:nondiff_stress}); DAG misspecification under measurement error may compound bias. ASV computation requires gold labels for $C^{-1}$; error propagation under small gold-label budgets ($<$500) and general $K{\geq}3$ envelope monotonicity (Conjecture~\ref{conj:monotone}) remain open.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05f43707-bc09-4194-b36c-1de40b78f8b0",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "1660a4e9-2698-437e-b2d5-7414ecc70a8d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe characterized how multi-class annotation errors interact with causal DAG topology: at $K{\\geq}3$, exposure and IV can reverse treatment effect signs while five topologies preserve them. ASVs provide a topology-dependent vulnerability ranking; matrix-based corrections are provably ineffective for four covariate topologies (FWL invariance). Practitioners should identify the topology first: for exposure, PPI++ reduces bias from ${\\sim}61\\%$ to ${<}1\\%$ (Table~\\ref{tab:e2e-real-cm}); for IV, all tested corrections worsen the estimate. High $F_1$ does not guarantee low causal bias; topology assessment must precede downstream inference.\n\nDifferential misclassification and proving Conjecture~\\ref{conj:monotone} for general $K$ remain open.\n\n\\section*{Limitations}\n\nOur closed-form results assume linear SEMs with proportional effects ($f{=}\\lambda g$); sign preservation empirically holds at 97.3\\% under non-proportional effects (Table~\\ref{tab:proportional_empirical}), but recommendations do not directly extend to nonlinear models (matching, doubly-robust). The framework assumes a known DAG with non-differential misclassification (Appendix~\\ref{sec:nondiff_stress}); DAG misspecification under measurement error may compound bias. ASV computation requires gold labels for $C^{-1}$; error propagation under small gold-label budgets ($<$500) and general $K{\\geq}3$ envelope monotonicity (Conjecture~\\ref{conj:monotone}) remain open.\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  },
  "sourceToolAssistantUUID": "05f43707-bc09-4194-b36c-1de40b78f8b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T08:23:26.132Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JfP8oYwYVN8EDg91bBZroZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1660a4e9-2698-437e-b2d5-7414ecc70a8d",
  "isSidechain": false,
  "requestId": "req_011CbNxv8mXTejhBT9P2pLrN",
  "type": "assistant",
  "uuid": "ca8f1eec-7c89-4876-9752-d5adf7c2ebe6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXWWF9ogGXcabKsU1RyxvV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12102,
      "cache_read_input_tokens": 39699,
      "output_tokens": 635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12102,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 635,
          "cache_read_input_tokens": 39699,
          "cache_creation_input_tokens": 12102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12102
          },
          "type": "message"
        }
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

_source line 33 · 2026-05-25T08:23:26.137Z_

<details><summary>↩ Tool result · `toolu_01JfP8oYwYVN8EDg91bBZroZ`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	\usepackage{float}
13	
14	\newtheorem{definition}{Definition}
15	\newtheorem{proposition}{Proposition}
16	\newtheorem{theorem}{Theorem}
17	\newtheorem{lemma}{Lemma}
18	\newtheorem{conjecture}{Conjecture}
19	\newtheorem{observation}{Observation}
20	\newtheorem{remark}{Remark}
21	
22	\setlength{\textfloatsep}{6pt plus 2pt minus 4pt}
23	\setlength{\dbltextfloatsep}{6pt plus 2pt minus 4pt}
24	\setlength{\floatsep}{6pt plus 2pt minus 4pt}
25	\setlength{\dblfloatsep}{6pt plus 2pt minus 4pt}
26	\setlength{\abovedisplayskip}{5pt plus 2pt minus 3pt}
27	\setlength{\belowdisplayskip}{5pt plus 2pt minus 3pt}
28	\setlength{\abovedisplayshortskip}{2pt plus 1pt minus 1pt}
29	\setlength{\belowdisplayshortskip}{3pt plus 1pt minus 2pt}
30	\graphicspath{{../../figures/paper/}}
31	
32	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
33	
34	\author{Anonymous}
35	
36	\begin{document}
37	\maketitle
38	
39	\input{abstract}
40	
41	\input{introduction}
42	
43	\begin{figure*}[t]
44	\centering
45	\includegraphics[width=\textwidth]{fig1_dag_taxonomy.pdf}
46	\vspace{-4pt}
47	\caption{Seven canonical DAG topologies with starred-node annotation~\cite{hernan_cole2009}. $A$ (latent) $\to$ $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies: treatment (exposure), covariate (confounding, mediation, M-bias, front-door), selection (collider), instrument (IV).}
48	\label{fig:dag_taxonomy}
49	\end{figure*}
50	
51	\input{related_work}
52	
53	\input{method}
54	
55	\input{experiments}
56	
57	\input{conclusion}
58	
59	\bibliography{references}
60	
61	\appendix
62	\input{appendix_proofs}
63	
64	\end{document}
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca8f1eec-7c89-4876-9752-d5adf7c2ebe6",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "5cb78fff-04ce-48c2-ac22-e9286747a941",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\n\\usepackage{graphicx}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{pifont}\n\\usepackage{multirow}\n\\usepackage{float}\n\n\\newtheorem{definition}{Definition}\n\\newtheorem{proposition}{Proposition}\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{lemma}{Lemma}\n\\newtheorem{conjecture}{Conjecture}\n\\newtheorem{observation}{Observation}\n\\newtheorem{remark}{Remark}\n\n\\setlength{\\textfloatsep}{6pt plus 2pt minus 4pt}\n\\setlength{\\dbltextfloatsep}{6pt plus 2pt minus 4pt}\n\\setlength{\\floatsep}{6pt plus 2pt minus 4pt}\n\\setlength{\\dblfloatsep}{6pt plus 2pt minus 4pt}\n\\setlength{\\abovedisplayskip}{5pt plus 2pt minus 3pt}\n\\setlength{\\belowdisplayskip}{5pt plus 2pt minus 3pt}\n\\setlength{\\abovedisplayshortskip}{2pt plus 1pt minus 1pt}\n\\setlength{\\belowdisplayshortskip}{3pt plus 1pt minus 2pt}\n\\graphicspath{{../../figures/paper/}}\n\n\\title{Multi-Class Annotation Errors in Causal Inference:\\\\Topology-Dependent Bias, Sensitivity, and Correction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_dag_taxonomy.pdf}\n\\vspace{-4pt}\n\\caption{Seven canonical DAG topologies with starred-node annotation~\\cite{hernan_cole2009}. $A$ (latent) $\\to$ $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies: treatment (exposure), covariate (confounding, mediation, M-bias, front-door), selection (collider), instrument (IV).}\n\\label{fig:dag_taxonomy}\n\\end{figure*}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix_proofs}\n\n\\end{document}\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  },
  "sourceToolAssistantUUID": "ca8f1eec-7c89-4876-9752-d5adf7c2ebe6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-25T08:23:26.501Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Lek5GrrDTu8k4TevFPWaVZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cb78fff-04ce-48c2-ac22-e9286747a941",
  "isSidechain": false,
  "requestId": "req_011CbNxv8mXTejhBT9P2pLrN",
  "type": "assistant",
  "uuid": "57327ecd-a306-4c02-9927-1e48fcc32367",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXWWF9ogGXcabKsU1RyxvV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12102,
      "cache_read_input_tokens": 39699,
      "output_tokens": 635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12102,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 635,
          "cache_read_input_tokens": 39699,
          "cache_creation_input_tokens": 12102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12102
          },
          "type": "message"
        }
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：causal_annot_error_attrib Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 92 warning 一…",
  "leafUuid": "57327ecd-a306-4c02-9927-1e48fcc32367",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit causal annotation error attribution paper",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb"
}
```

---

### Tool result

_source line 37 · 2026-05-25T08:23:26.789Z_

<details><summary>↩ Tool result · reported error · `toolu_01Lek5GrrDTu8k4TevFPWaVZ`</summary>

```text
File content (46257 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57327ecd-a306-4c02-9927-1e48fcc32367",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "027e0e53-f4af-449f-9b20-1b1c2f38275d",
  "toolUseResult": "Error: File content (46257 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "57327ecd-a306-4c02-9927-1e48fcc32367",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 38 · 2026-05-25T08:23:26.793Z_

```json
{
  "parentUuid": "027e0e53-f4af-449f-9b20-1b1c2f38275d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "cc4b8de4-b783-49af-a93f-7fc15c779d12",
  "timestamp": "2026-05-25T08:23:26.793Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 39 · 2026-05-25T08:23:31.156Z_

<details><summary>Logged reasoning block</summary>

```text
The appendix is too large to read at once. Let me read it in portions. But first, let me do the content audit with what I have. I can also run some grep searches for specific patterns (em-dashes, AI-style phrases, etc.) in parallel.

Let me also check the abstract word count and some other specific things.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc4b8de4-b783-49af-a93f-7fc15c779d12",
  "isSidechain": false,
  "requestId": "req_011CbNxvgfugkhVtfata9pGK",
  "type": "assistant",
  "uuid": "4aeacb19-57e5-41af-a9fb-a94ad0a63b4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2ERx3NK2sp7VbE8zaEqJF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12722,
      "cache_read_input_tokens": 51801,
      "output_tokens": 1012,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1012,
          "cache_read_input_tokens": 51801,
          "cache_creation_input_tokens": 12722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12722
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-25T08:23:31.597Z_

Appendix too large to read at once. Let me read it in portions and run pattern scans in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4aeacb19-57e5-41af-a9fb-a94ad0a63b4e",
  "isSidechain": false,
  "requestId": "req_011CbNxvgfugkhVtfata9pGK",
  "type": "assistant",
  "uuid": "80185dec-f345-4c1e-b3ae-d41f8d598a4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2ERx3NK2sp7VbE8zaEqJF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12722,
      "cache_read_input_tokens": 51801,
      "output_tokens": 1012,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1012,
          "cache_read_input_tokens": 51801,
          "cache_creation_input_tokens": 12722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12722
          },
          "type": "message"
        }
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

_source line 41 · 2026-05-25T08:23:33.483Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Hj8RchQ8umTXWL5A3RRfbi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "offset": 0,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80185dec-f345-4c1e-b3ae-d41f8d598a4a",
  "isSidechain": false,
  "requestId": "req_011CbNxvgfugkhVtfata9pGK",
  "type": "assistant",
  "uuid": "ab15a1f4-4275-4fd0-a3fa-b3a6818c083d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2ERx3NK2sp7VbE8zaEqJF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12722,
      "cache_read_input_tokens": 51801,
      "output_tokens": 1012,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1012,
          "cache_read_input_tokens": 51801,
          "cache_creation_input_tokens": 12722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12722
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-25T08:23:40.821Z_

<details><summary>↩ Tool result · `toolu_01U6qwGNsS1i4wp3YLLppgqR`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:232:Moreover, $B_{\mathrm{OV}}=\operatorname{Cov}(g,f)/\operatorname{Var}(T)=0.588/1.962={+}0.300$, giving $\tau_{\mathrm{OV}}{=}2.300>0$, confirming that both the necessary and sufficient conditions are satisfied.
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:468:\item[(b)] $\lambda(C)\geq 0$ iff additionally $|B(C)|\leq|\tau_{\mathrm{ind}}|$ (the bias does not exceed the indirect effect in magnitude).
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:476:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c38628f5-c5c7-43e8-a1c3-f3a5e7b3e7f4",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "27cb121d-9787-4cd2-a9d7-2529c24a7d24",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:232:Moreover, $B_{\\mathrm{OV}}=\\operatorname{Cov}(g,f)/\\operatorname{Var}(T)=0.588/1.962={+}0.300$, giving $\\tau_{\\mathrm{OV}}{=}2.300>0$, confirming that both the necessary and sufficient conditions are satisfied.\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:468:\\item[(b)] $\\lambda(C)\\geq 0$ iff additionally $|B(C)|\\leq|\\tau_{\\mathrm{ind}}|$ (the bias does not exceed the indirect effect in magnitude).\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:476:[Omitted long matching line]",
    "numLines": 3
  },
  "sourceToolAssistantUUID": "c38628f5-c5c7-43e8-a1c3-f3a5e7b3e7f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-25T08:23:33.489Z_

<details><summary>↩ Tool result · `toolu_01Hj8RchQ8umTXWL5A3RRfbi`</summary>

```text
0	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
1	\label{app:proof}
2	
3	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
4	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
5	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
6	
7	\subsection{Notation and Key Identities}
8	\label{app:notation}
9	
10	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
11	Define the population vectors:
12	\begin{align}
13	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
14	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
15	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
16	\end{align}
17	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
18	
19	\subsection{Frisch--Waugh--Lovell Decomposition}
20	\label{app:fwl}
21	
22	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
23	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
24	\begin{equation}
25	  \operatorname{plim}\hat{\tau}(C)
26	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
27	  \label{eq:fwl}
28	\end{equation}
29	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\tilde{Y}=Y-\mathbb{E}[Y\mid A^*]$ are residuals from projecting onto $(1,D_1^*,\dots,D_{K-1}^*)$.
30	
31	\begin{lemma}[Bias decomposition]
32	\label{lem:bias_decomp}
33	Suppose $Y = \tau T + f(A) + \varepsilon_Y$ with $\varepsilon_Y \perp (T, A, A^*)$.
34	Then
35	\begin{equation}
36	  \operatorname{plim}\hat\tau(C) = \tau + \frac{R(C)}{D(C)},
37	  \label{eq:bias_decomp}
38	\end{equation}
39	where
40	\begin{align}
41	  R(C) &= \mathbb{E}\bigl[\operatorname{Cov}(T,\,f(A)\mid A^*)\bigr], \label{eq:R}\\
42	  D(C) &= \mathbb{E}\bigl[\operatorname{Var}(T\mid A^*)\bigr] > 0. \label{eq:D}
43	\end{align}
44	\end{lemma}
45	
46	\begin{proof}
47	Expand $\tilde{Y}$ using $Y=\tau T + f(A) + \varepsilon_Y$:
48	\[
49	  \tilde{Y} = \tau\,\tilde{T} + \bigl(f(A) - \mathbb{E}[f(A)\mid A^*]\bigr) + \varepsilon_Y.
50	\]
51	Since $\tilde{T}$ is measurable w.r.t.\ $(T,A^*)$ and $\varepsilon_Y\perp(T,A,A^*)$:
52	\[
53	  \mathbb{E}[\tilde{T}\,\tilde{Y}]
54	  = \tau\,\mathbb{E}[\tilde{T}^2]
55	  + \mathbb{E}\bigl[\tilde{T}\,\bigl(f(A)-\mathbb{E}[f(A)\mid A^*]\bigr)\bigr].
56	\]
57	The numerator residual is $R(C) = \mathbb{E}[\tilde{T}(f(A)-\mathbb{E}[f(A)\mid A^*])]$, and the denominator is $D(C) = \mathbb{E}[\tilde{T}^2]$.
58	
59	By the law of total covariance:
60	\begin{align*}
61	  R(C) &= \sum_{j=0}^{K-1} q_j\,\operatorname{Cov}(T,\,f(A)\mid A^*{=}j)\\
62	  &= \mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)].
63	\end{align*}
64	For $D(C)>0$: decompose $T = g(A) + \varepsilon_T$ where $g(A)=\mathbb{E}[T\mid A]$ (for confounding) or simply note that $T$ has exogenous variation independent of $A^*$ (for mediation).
65	In both cases, $\tilde{T}=\bigl(g(A)-\mathbb{E}[g(A)\mid A^*]\bigr)+\varepsilon_T'$, where $\varepsilon_T'$ is the component of $T$ independent of $(A,A^*)$.
66	Hence $D(C)\geq\operatorname{Var}(\varepsilon_T')>0$.
67	\end{proof}
68	
69	\subsection{Confounding Topology ($A$ = Confounder)}
70	\label{app:confounding}
71	
72	\paragraph{Data-generating process.}
73	$A\to T$, $A\to Y$, $T\to Y$.
74	Using dummy coding with category 0 as reference:
75	\begin{align*}
76	  T &= \textstyle\sum_{j=1}^{K-1}\alpha_j D_j + \varepsilon_T,\quad
77	  \varepsilon_T\sim\mathcal{N}(0,\sigma_T^2),\\
78	  Y &= \tau\, T + \textstyle\sum_{j=1}^{K-1}\beta_j^{(A)} D_j + \varepsilon_Y,\\
79	  &\quad \varepsilon_Y\sim\mathcal{N}(0,1),
80	\end{align*}
81	with $\varepsilon_T\perp A$ and $\varepsilon_Y\perp(T,A)$.
82	Define $g(k)=\sum_{j}\alpha_j\mathbf{1}(k{=}j)$ and
83	$f(k)=\sum_{j}\beta_j^{(A)}\mathbf{1}(k{=}j)$, so $g(0)=f(0)=0$.
84	
85	\paragraph{Closed-form plim.}
86	Using the FWL decomposition, the coefficient on $T$ is:
87	\begin{equation}
88	  \operatorname{plim}\hat\tau(C)
89	  = \frac{\mu_{TY} - \sum_{j=0}^{K-1}\frac{\mathrm{ct}_j\,\mathrm{cy}_j}{q_j}}
90	  {s_T - \sum_{j=0}^{K-1}\frac{\mathrm{ct}_j^2}{q_j}},
91	  \label{eq:plim_conf}
92	\end{equation}
93	where $s_T=\mathbb{E}[T^2]$, $\mu_{TY}=\mathbb{E}[TY]$, and $\mathrm{ct}_j$, $\mathrm{cy}_j$, $q_j$ are defined in~\eqref{eq:q}--\eqref{eq:cy}.
94	
95	\begin{proof}[Derivation]
96	By FWL, $\operatorname{plim}\hat\tau = \mathbb{E}[\tilde{T}Y]/\mathbb{E}[\tilde{T}^2]$ where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$.
97	Since $\mathbb{E}[T\mid A^*{=}j]=\mathrm{ct}_j/q_j$:
98	\begin{align*}
99	  \mathbb{E}[\tilde{T}^2]
100	  &= \mathbb{E}[T^2] - \textstyle\sum_j q_j\bigl(\mathrm{ct}_j/q_j\bigr)^2\\
101	  &= s_T - \textstyle\sum_j \mathrm{ct}_j^2/q_j,\\
102	  \mathbb{E}[\tilde{T}\,Y]
103	  &= \mathbb{E}[TY] - \textstyle\sum_j \bigl(\mathrm{ct}_j/q_j\bigr)\,\mathbb{E}[Y\cdot D_j^*]\\
104	  &= \mu_{TY} - \textstyle\sum_j \mathrm{ct}_j\,\mathrm{cy}_j/q_j.
105	\end{align*}
106	\end{proof}
107	
108	\paragraph{Verification at $C=I$.}
109	When $C=I$: $q_j=p_j$, $\mathrm{ct}_j=\mathbb{E}[T D_j]=\alpha_j p_j$, $\mathrm{cy}_j=\mathbb{E}[Y D_j]=p_j(\tau\alpha_j+\beta_j^{(A)})$.
110	Direct substitution yields numerator $= \tau\sigma_T^2$ and denominator $= \sigma_T^2$, giving $\operatorname{plim}\hat\tau = \tau$.
111	
112	\paragraph{Bias structure.}
113	By Lemma~\ref{lem:bias_decomp}:
114	\begin{align}
115	  \operatorname{plim}\hat\tau(C) &= \tau + B(C),\notag\\
116	  B(C) &= \frac{\mathbb{E}[\operatorname{Cov}(g(A),\,f(A)\mid A^*)]}{D(C)}.
117	  \label{eq:bias_conf}
118	\end{align}
119	By the law of total covariance:
120	\begin{multline}
121	  \mathbb{E}[\operatorname{Cov}(g,f\mid A^*)]
122	  = \operatorname{Cov}(g(A),f(A))\\
123	  - \operatorname{Cov}\bigl(\mathbb{E}[g(A)\mid A^*],\;\mathbb{E}[f(A)\mid A^*]\bigr).
124	  \label{eq:lotc}
125	\end{multline}
126	
127	At $C=I$: $\mathbb{E}[g\mid A^*]=g(A)$, so the between-group covariance equals $\operatorname{Cov}(g,f)$ and $B(I)=0$.
128	
129	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ (uniform, $A^*\perp A$): $\mathbb{E}[g\mid A^*]$ is constant, so the between-group covariance is zero and
130	\begin{equation}
131	  B_{\mathrm{OV}} \;\equiv\; B\bigl(\tfrac{1}{K}\mathbf{1}\mathbf{1}^\top\bigr)
132	  = \frac{\operatorname{Cov}(g(A),\,f(A))}{\operatorname{Var}(T)},
133	  \label{eq:bov}
134	\end{equation}
135	which equals the classical omitted-variable bias (no control for $A$).
136	
137	\paragraph{Sign preservation condition.}
138	Since $D(C)>0$, sign$(\operatorname{plim}\hat\tau) = $ sign$(\tau\cdot D(C) + R(C))$.
139	For sign preservation, it suffices that $R(C)$ does not overwhelm $\tau\cdot D(C)$.
140	
141	\begin{proposition}[Confounding sign preservation --- proportional case]
142	\label{prop:conf_prop}
143	If $f(A) = \lambda\,g(A)$ for some constant $\lambda$ (i.e., the confounder effects on $T$ and $Y$ are proportional), then
144	\begin{equation}
145	  B(C) = \bigl(1-\xi(C)\bigr)\,B_{\mathrm{OV}},
146	  \label{eq:convex}
147	\end{equation}
148	where
149	\[
150	  \xi(C) = \frac{V_B\;\sigma_T^2}
151	  {V\bigl(V-V_B+\sigma_T^2\bigr)}
152	  \;\in\;[0,1],
153	\]
154	where $V_B=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])$ and $V=\operatorname{Var}(g(A))$.
155	Consequently, $B(C)$ lies between $0$ and $B_{\mathrm{OV}}$, and $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ whenever $\operatorname{sign}(\tau)=\operatorname{sign}(\tau+B_{\mathrm{OV}})$.
156	\end{proposition}
157	
158	\begin{proof}
159	When $f=\lambda g$: the between-group covariance in~\eqref{eq:lotc} becomes $\lambda\,\operatorname{Var}(\mathbb{E}[g\mid A^*])$, and $\operatorname{Cov}(g,f)=\lambda\,\operatorname{Var}(g)$.
160	So $R(C)=\lambda\bigl(\operatorname{Var}(g)-\operatorname{Var}(\mathbb{E}[g\mid A^*])\bigr)=\lambda\,V_W$, where $V_W=\operatorname{Var}(g)-V_B$ with $V_B=\operatorname{Var}(\mathbb{E}[g\mid A^*])$.
161	Similarly, $D(C)=V_W+\sigma_T^2$.
162	Hence
163	\[
164	  B(C) = \frac{\lambda\,V_W}{V_W+\sigma_T^2},\qquad
165	  B_{\mathrm{OV}} = \frac{\lambda\,V}{V+\sigma_T^2},
166	\]
167	where $V=\operatorname{Var}(g)=V_B+V_W$.
168	The ratio
169	\[
170	  \frac{B(C)}{B_{\mathrm{OV}}} = \frac{V_W(V+\sigma_T^2)}{V(V_W+\sigma_T^2)} = 1 - \xi(C)
171	\]
172	is a decreasing function of $V_B\in[0,V]$.
173	At $V_B=0$ (no classification, $C$ uniform): $\xi=0$, $B=B_{\mathrm{OV}}$.
174	At $V_B=V$ (perfect classification, $C=I$): $\xi=1$, $B=0$.
175	Since $0\leq V_B\leq V$, we have $\xi\in[0,1]$ and $B(C)\in[0,B_{\mathrm{OV}}]$ (with the sign of $B_{\mathrm{OV}}$).
176	\end{proof}
177	
178	\begin{proposition}[Confounding sign preservation --- general case]
179	\label{prop:conf_gen}
180	For general $g$ and $f$ (not necessarily proportional), define the worst-case bias bound
181	\begin{equation}
182	  \bar{B} \;=\; \frac{\sqrt{\operatorname{Var}(g(A))\,\operatorname{Var}(f(A))}}{\sigma_T^2}.
183	  \label{eq:bbar}
184	\end{equation}
185	If $|\tau| > \bar{B}$, then $\operatorname{sign}(\operatorname{plim}\hat\tau(C))=\operatorname{sign}(\tau)$ for all column-stochastic $C$.
186	\end{proposition}
187	
188	\begin{proof}
189	We need $\operatorname{sign}(\tau\cdot D(C)+R(C))=\operatorname{sign}(\tau)$, which holds if $|R(C)|<|\tau|\cdot D(C)$.
190	Since $D(C)\geq\sigma_T^2$ (shown in Lemma~\ref{lem:bias_decomp}), it suffices to show $|R(C)|<|\tau|\,\sigma_T^2$.
191	
192	\emph{Step 1: Bound $|R(C)|$.}
193	$R(C)=\mathbb{E}[\operatorname{Cov}(g(A),f(A)\mid A^*)]$.
194	By the Cauchy--Schwarz inequality applied to each within-group covariance:
195	\begin{multline*}
196	  |\operatorname{Cov}(g,f\mid A^*{=}j)|\\
197	  \leq \sqrt{\operatorname{Var}(g\mid A^*{=}j)\,\operatorname{Var}(f\mid A^*{=}j)}.
198	\end{multline*}
199	Taking expectations and applying Cauchy--Schwarz again:
200	\begin{align*}
201	  |R(C)|
202	  &\leq \mathbb{E}\bigl[\sqrt{\operatorname{Var}(g\mid A^*)\,\operatorname{Var}(f\mid A^*)}\bigr]\\
203	  &\leq \sqrt{\mathbb{E}[\operatorname{Var}(g\mid A^*)]\;\mathbb{E}[\operatorname{Var}(f\mid A^*)]}\\
204	  &\leq \sqrt{\operatorname{Var}(g(A))\;\operatorname{Var}(f(A))},
205	\end{align*}
206	where the last step uses $\mathbb{E}[\operatorname{Var}(X\mid Y)]\leq\operatorname{Var}(X)$ (law of total variance).
207	
208	\emph{Step 2: Conclude.}
209	The bias satisfies
210	\[
211	  |B(C)| = \frac{|R(C)|}{D(C)} \leq \frac{\sqrt{\operatorname{Var}(g)\,\operatorname{Var}(f)}}{\sigma_T^2} = \bar{B}.
212	\]
213	When $|\tau|>\bar{B}$, the bias cannot cancel $\tau$, so $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ for all $C$.
214	\end{proof}
215	
216	\paragraph{Relationship to the omitted-variable condition.}
217	A weaker (necessary) condition for sign preservation is $\operatorname{sign}(\tau)=\operatorname{sign}(\tau_{\mathrm{OV}})$ where $\tau_{\mathrm{OV}}=\tau+\operatorname{Cov}(g,f)/\operatorname{Var}(T)$.
218	If this fails, then $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ (uniform noise) already flips the sign.
219	The rigorous sufficient condition $|\tau|>\bar{B}$ implies the weaker condition, since $|B_{\mathrm{OV}}|=|\operatorname{Cov}(g,f)|/\operatorname{Var}(T)\leq\bar{B}$ by Cauchy--Schwarz and $\operatorname{Var}(T)\geq\sigma_T^2$.
220	
221	\paragraph{Verification for paper parameters ($K{=}3$).}
222	With $\tau{=}2.0$, $\boldsymbol{\alpha}{=}(1.5,{-}1.0)$, $\boldsymbol{\beta}^{(A)}{=}(1.0,{-}0.5)$, $\sigma_T{=}1.0$, $\mathbf{p}{=}(0.40,0.35,0.25)$:
223	\begin{align*}
224	  \operatorname{Var}(g) &= \textstyle\sum_k p_k\alpha_k^2 - (\sum_k p_k\alpha_k)^2\\
225	  &= 0.962,\\
226	  \operatorname{Var}(f) &= \textstyle\sum_k p_k(\beta_k^{(A)})^2 - (\sum_k p_k\beta_k^{(A)})^2\\
227	  &= 0.362,\\
228	  \bar{B} &= \sqrt{0.962\times 0.362}/1.0^2 = 0.590.
229	\end{align*}
230	Since $|\tau|{=}2.0 > \bar{B}{=}0.590$, sign preservation is guaranteed for all column-stochastic $C$ by Proposition~\ref{prop:conf_gen}.
231	Moreover, $B_{\mathrm{OV}}=\operatorname{Cov}(g,f)/\operatorname{Var}(T)=0.588/1.962={+}0.300$, giving $\tau_{\mathrm{OV}}{=}2.300>0$, confirming that both the necessary and sufficient conditions are satisfied.
232	
233	\paragraph{Extension to $K > 3$.}
234	For $K{>}3$, treatment effect coefficients are drawn from a fixed pool with alternating signs and decreasing magnitudes:
235	\begin{multline*}
236	  \boldsymbol{\beta} = (0,\; 1.0,\; {-}0.5,\; 0.7,\; {-}0.3,\\
237	  0.5,\; {-}0.2,\; 0.4,\; {-}0.15,\; 0.3,\; \ldots),
238	\end{multline*}
239	truncated to $K$ entries. The category distribution uses $p_k \propto 1/(k{+}1)$, normalized to sum to~1. Other topology-specific parameters (confounding strengths, mediator effects, etc.)\ follow analogous alternating-sign pools.
240	
241	\subsection{Proof of Theorem~\ref{thm:monotone} (Confounding Monotonicity)}
242	\label{app:monotonicity_proof}
243	
244	Under the interpolation $C(\delta)=(1{-}\delta)I+\delta C_0$, we prove $|B(C(\delta))|$ is non-decreasing in $\delta$ for proportional effects ($f=\lambda g$) and provide numerical verification for the general case.
245	The proof proceeds by direct algebraic analysis of $V_B(\delta)=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*_\delta])$ as a rational function of $\delta$, establishing convexity and bounding the derivative at both endpoints.
246	
247	\paragraph{Proportional case ($f=\lambda g$).}
248	From Proposition~\ref{prop:conf_prop}, $B(C)=\lambda V_W/(V_W+\sigma_T^2)$ where $V_W=\operatorname{Var}(g)-V_B$ and $V_B(\delta)=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*_\delta])$.
249	
250	\emph{Step 1: Convexity of $V_B(\delta)$.}
251	Define $N_j(\delta)=\sum_k g_k\,C(\delta)_{jk}\,p_k$ and $q_j(\delta)=\sum_k C(\delta)_{jk}\,p_k$.
252	Both are affine in $\delta$, with $q_j(\delta)>0$.
253	Then $V_B(\delta)=\sum_j N_j(\delta)^2/q_j(\delta) - \bar{g}^2$.
254	Each term $N_j^2/q_j$ is the composition of the perspective function $(x,t)\mapsto x^2/t$ (convex for $t>0$) with the affine map $\delta\mapsto(N_j(\delta),\,q_j(\delta))$, hence convex in $\delta$.
255	A sum of convex functions is convex, so $V_B(\delta)$ is convex on $[0,\delta_{\max}]$.
256	
257	\emph{Step 2: Derivative formula.}
258	Let $\mu_j(\delta)=N_j(\delta)/q_j(\delta)=\mathbb{E}[g(A)\mid A^*{=}j]$.
259	Then
260	\begin{equation}
261	\frac{dV_B}{d\delta}
262	= -\sum_{j,k}\bigl[(C_0)_{jk}-\mathbf{1}_{j=k}\bigr]\,p_k\,(g_k-\mu_j(\delta))^2.
263	\label{eq:dVB}
264	\end{equation}
265	\emph{Derivation.}
266	$\frac{d}{d\delta}\frac{N_j^2}{q_j}=2\mu_j\dot{N}_j-\mu_j^2\dot{q}_j$
267	where $\dot{N}_j=m_j^0-g_jp_j$ and $\dot{q}_j=q_j^0-p_j$ (with $m_j^0=\sum_k g_k(C_0)_{jk}p_k$, $q_j^0=\sum_k(C_0)_{jk}p_k$).
268	Substituting and using column-stochasticity ($\sum_j(C_0)_{jk}=\sum_j\mathbf{1}_{j=k}=1$) to cancel the $g_k^2$ terms yields~\eqref{eq:dVB}.
269	
270	\emph{Step 3: $V_B'(0)\leq 0$ (universal, no conditions on $C_0$).}
271	At $\delta{=}0$: $\mu_j(0)=g_j$ (since $C(0)=I$), so $(g_k-\mu_j(0))^2=(g_k-g_j)^2$.
272	The diagonal terms ($j{=}k$) vanish.
273	Hence
274	\[
275	V_B'(0)=-\sum_{j\neq k}(C_0)_{jk}\,p_k\,(g_j-g_k)^2\;\leq\; 0,
276	\]
277	since every term is non-negative.
278	
279	\emph{Step 4: $V_B'(1)\leq 0$ for $K{=}2$.}
280	For $K{=}2$ with $C_0=\bigl[\begin{smallmatrix}a&1{-}b\\1{-}a&b\end{smallmatrix}\bigr]$ and $a,b\geq\tfrac{1}{2}$,
281	set $g_0{=}0$, $g_1{=}1$ without loss of generality
282	(the general case scales by $(\Delta g)^2$).
283	At $\delta{=}1$: $q_0{=}ap_0{+}(1{-}b)p_1$, $q_1{=}(1{-}a)p_0{+}bp_1$,
284	$\mu_0{=}(1{-}b)p_1/q_0$, $\mu_1{=}bp_1/q_1$.
285	Expanding~\eqref{eq:dVB} at $\delta{=}1$ and factoring:
286	\begin{align*}
287	  V_B'(1) &= (1{-}a)\,p_0(\mu_0^2{-}\mu_1^2)\\
288	  &\quad{}+(1{-}b)\,p_1\bigl[(1{-}\mu_1)^2{-}(1{-}\mu_0)^2\bigr] \\
289	  &= (\mu_0{-}\mu_1)\,\bigl[(1{-}a)\,p_0(\mu_0{+}\mu_1)\\
290	  &\quad{}+(1{-}b)\,p_1(2{-}\mu_0{-}\mu_1)\bigr].
291	\end{align*}
292	The bracket is non-negative (since $0\leq\mu_j\leq 1$ and all coefficients are non-negative).
293	Direct calculation gives $\mu_0{-}\mu_1=p_0\,p_1(1{-}a{-}b)/(q_0\,q_1)$
294	(expand $(1{-}b)\,q_1-b\,q_0=p_0(1{-}a{-}b)$).
295	Under $a,b\geq\tfrac{1}{2}$: $a{+}b\geq 1$, so $\mu_0{-}\mu_1\leq 0$ and $V_B'(1)\leq 0$.
296	
297	\emph{Step 5: Monotonicity from convexity.}
298	Since $V_B$ is convex (Step~1), its derivative $V_B'$ is non-decreasing.
299	When $V_B'(1)\leq 0$, we have $V_B'(\delta)\leq V_B'(1)\leq 0$ for all $\delta\in[0,1]$, so $V_B$ is non-increasing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab15a1f4-4275-4fd0-a3fa-b3a6818c083d",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "2b751a3f-f9ca-4e20-b6ab-93aaac0979ca",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
      "content": "\\section{Proofs of Proposition~\\ref{prop:signflip} and Theorem~\\ref{thm:monotone}}\n\\label{app:proof}\n\nWe provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\\ref{thm:monotone}).\nThroughout, $A\\in\\{0,1,\\dots,K{-}1\\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\\mid A{=}k)$.\nWe use category~0 as the reference and let $D_j=\\mathbf{1}(A{=}j)$, $D_j^*=\\mathbf{1}(A^*{=}j)$ for $j=1,\\dots,K{-}1$.\n\n\\subsection{Notation and Key Identities}\n\\label{app:notation}\n\nUnder non-differential misclassification, the misclassified moments factor linearly through $C$.\nDefine the population vectors:\n\\begin{align}\n  q_j &= P(A^*{=}j) = \\textstyle\\sum_k C_{jk}\\,p_k, \\label{eq:q}\\\\\n  \\mathrm{ct}_j &= \\mathbb{E}[T\\cdot D_j^*] = \\textstyle\\sum_k C_{jk}\\,\\mathbb{E}[T\\cdot D_k], \\label{eq:ct}\\\\\n  \\mathrm{cy}_j &= \\mathbb{E}[Y\\cdot D_j^*] = \\textstyle\\sum_k C_{jk}\\,\\mathbb{E}[Y\\cdot D_k]. \\label{eq:cy}\n\\end{align}\nWrite $q = Cp$, $\\mathrm{ct} = C\\,\\mathbb{E}[T\\cdot D]$, and $\\mathrm{cy} = C\\,\\mathbb{E}[Y\\cdot D]$, where $D=(D_0,\\dots,D_{K-1})^\\top$.\n\n\\subsection{Frisch--Waugh--Lovell Decomposition}\n\\label{app:fwl}\n\nFor topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\\dots,D_{K-1}^*)$.\nBy the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:\n\\begin{equation}\n  \\operatorname{plim}\\hat{\\tau}(C)\n  = \\frac{\\mathbb{E}[\\tilde{T}\\,\\tilde{Y}]}{\\mathbb{E}[\\tilde{T}^2]},\n  \\label{eq:fwl}\n\\end{equation}\nwhere $\\tilde{T}=T-\\mathbb{E}[T\\mid A^*]$ and $\\tilde{Y}=Y-\\mathbb{E}[Y\\mid A^*]$ are residuals from projecting onto $(1,D_1^*,\\dots,D_{K-1}^*)$.\n\n\\begin{lemma}[Bias decomposition]\n\\label{lem:bias_decomp}\nSuppose $Y = \\tau T + f(A) + \\varepsilon_Y$ with $\\varepsilon_Y \\perp (T, A, A^*)$.\nThen\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C) = \\tau + \\frac{R(C)}{D(C)},\n  \\label{eq:bias_decomp}\n\\end{equation}\nwhere\n\\begin{align}\n  R(C) &= \\mathbb{E}\\bigl[\\operatorname{Cov}(T,\\,f(A)\\mid A^*)\\bigr], \\label{eq:R}\\\\\n  D(C) &= \\mathbb{E}\\bigl[\\operatorname{Var}(T\\mid A^*)\\bigr] > 0. \\label{eq:D}\n\\end{align}\n\\end{lemma}\n\n\\begin{proof}\nExpand $\\tilde{Y}$ using $Y=\\tau T + f(A) + \\varepsilon_Y$:\n\\[\n  \\tilde{Y} = \\tau\\,\\tilde{T} + \\bigl(f(A) - \\mathbb{E}[f(A)\\mid A^*]\\bigr) + \\varepsilon_Y.\n\\]\nSince $\\tilde{T}$ is measurable w.r.t.\\ $(T,A^*)$ and $\\varepsilon_Y\\perp(T,A,A^*)$:\n\\[\n  \\mathbb{E}[\\tilde{T}\\,\\tilde{Y}]\n  = \\tau\\,\\mathbb{E}[\\tilde{T}^2]\n  + \\mathbb{E}\\bigl[\\tilde{T}\\,\\bigl(f(A)-\\mathbb{E}[f(A)\\mid A^*]\\bigr)\\bigr].\n\\]\nThe numerator residual is $R(C) = \\mathbb{E}[\\tilde{T}(f(A)-\\mathbb{E}[f(A)\\mid A^*])]$, and the denominator is $D(C) = \\mathbb{E}[\\tilde{T}^2]$.\n\nBy the law of total covariance:\n\\begin{align*}\n  R(C) &= \\sum_{j=0}^{K-1} q_j\\,\\operatorname{Cov}(T,\\,f(A)\\mid A^*{=}j)\\\\\n  &= \\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)].\n\\end{align*}\nFor $D(C)>0$: decompose $T = g(A) + \\varepsilon_T$ where $g(A)=\\mathbb{E}[T\\mid A]$ (for confounding) or simply note that $T$ has exogenous variation independent of $A^*$ (for mediation).\nIn both cases, $\\tilde{T}=\\bigl(g(A)-\\mathbb{E}[g(A)\\mid A^*]\\bigr)+\\varepsilon_T'$, where $\\varepsilon_T'$ is the component of $T$ independent of $(A,A^*)$.\nHence $D(C)\\geq\\operatorname{Var}(\\varepsilon_T')>0$.\n\\end{proof}\n\n\\subsection{Confounding Topology ($A$ = Confounder)}\n\\label{app:confounding}\n\n\\paragraph{Data-generating process.}\n$A\\to T$, $A\\to Y$, $T\\to Y$.\nUsing dummy coding with category 0 as reference:\n\\begin{align*}\n  T &= \\textstyle\\sum_{j=1}^{K-1}\\alpha_j D_j + \\varepsilon_T,\\quad\n  \\varepsilon_T\\sim\\mathcal{N}(0,\\sigma_T^2),\\\\\n  Y &= \\tau\\, T + \\textstyle\\sum_{j=1}^{K-1}\\beta_j^{(A)} D_j + \\varepsilon_Y,\\\\\n  &\\quad \\varepsilon_Y\\sim\\mathcal{N}(0,1),\n\\end{align*}\nwith $\\varepsilon_T\\perp A$ and $\\varepsilon_Y\\perp(T,A)$.\nDefine $g(k)=\\sum_{j}\\alpha_j\\mathbf{1}(k{=}j)$ and\n$f(k)=\\sum_{j}\\beta_j^{(A)}\\mathbf{1}(k{=}j)$, so $g(0)=f(0)=0$.\n\n\\paragraph{Closed-form plim.}\nUsing the FWL decomposition, the coefficient on $T$ is:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau(C)\n  = \\frac{\\mu_{TY} - \\sum_{j=0}^{K-1}\\frac{\\mathrm{ct}_j\\,\\mathrm{cy}_j}{q_j}}\n  {s_T - \\sum_{j=0}^{K-1}\\frac{\\mathrm{ct}_j^2}{q_j}},\n  \\label{eq:plim_conf}\n\\end{equation}\nwhere $s_T=\\mathbb{E}[T^2]$, $\\mu_{TY}=\\mathbb{E}[TY]$, and $\\mathrm{ct}_j$, $\\mathrm{cy}_j$, $q_j$ are defined in~\\eqref{eq:q}--\\eqref{eq:cy}.\n\n\\begin{proof}[Derivation]\nBy FWL, $\\operatorname{plim}\\hat\\tau = \\mathbb{E}[\\tilde{T}Y]/\\mathbb{E}[\\tilde{T}^2]$ where $\\tilde{T}=T-\\mathbb{E}[T\\mid A^*]$.\nSince $\\mathbb{E}[T\\mid A^*{=}j]=\\mathrm{ct}_j/q_j$:\n\\begin{align*}\n  \\mathbb{E}[\\tilde{T}^2]\n  &= \\mathbb{E}[T^2] - \\textstyle\\sum_j q_j\\bigl(\\mathrm{ct}_j/q_j\\bigr)^2\\\\\n  &= s_T - \\textstyle\\sum_j \\mathrm{ct}_j^2/q_j,\\\\\n  \\mathbb{E}[\\tilde{T}\\,Y]\n  &= \\mathbb{E}[TY] - \\textstyle\\sum_j \\bigl(\\mathrm{ct}_j/q_j\\bigr)\\,\\mathbb{E}[Y\\cdot D_j^*]\\\\\n  &= \\mu_{TY} - \\textstyle\\sum_j \\mathrm{ct}_j\\,\\mathrm{cy}_j/q_j.\n\\end{align*}\n\\end{proof}\n\n\\paragraph{Verification at $C=I$.}\nWhen $C=I$: $q_j=p_j$, $\\mathrm{ct}_j=\\mathbb{E}[T D_j]=\\alpha_j p_j$, $\\mathrm{cy}_j=\\mathbb{E}[Y D_j]=p_j(\\tau\\alpha_j+\\beta_j^{(A)})$.\nDirect substitution yields numerator $= \\tau\\sigma_T^2$ and denominator $= \\sigma_T^2$, giving $\\operatorname{plim}\\hat\\tau = \\tau$.\n\n\\paragraph{Bias structure.}\nBy Lemma~\\ref{lem:bias_decomp}:\n\\begin{align}\n  \\operatorname{plim}\\hat\\tau(C) &= \\tau + B(C),\\notag\\\\\n  B(C) &= \\frac{\\mathbb{E}[\\operatorname{Cov}(g(A),\\,f(A)\\mid A^*)]}{D(C)}.\n  \\label{eq:bias_conf}\n\\end{align}\nBy the law of total covariance:\n\\begin{multline}\n  \\mathbb{E}[\\operatorname{Cov}(g,f\\mid A^*)]\n  = \\operatorname{Cov}(g(A),f(A))\\\\\n  - \\operatorname{Cov}\\bigl(\\mathbb{E}[g(A)\\mid A^*],\\;\\mathbb{E}[f(A)\\mid A^*]\\bigr).\n  \\label{eq:lotc}\n\\end{multline}\n\nAt $C=I$: $\\mathbb{E}[g\\mid A^*]=g(A)$, so the between-group covariance equals $\\operatorname{Cov}(g,f)$ and $B(I)=0$.\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ (uniform, $A^*\\perp A$): $\\mathbb{E}[g\\mid A^*]$ is constant, so the between-group covariance is zero and\n\\begin{equation}\n  B_{\\mathrm{OV}} \\;\\equiv\\; B\\bigl(\\tfrac{1}{K}\\mathbf{1}\\mathbf{1}^\\top\\bigr)\n  = \\frac{\\operatorname{Cov}(g(A),\\,f(A))}{\\operatorname{Var}(T)},\n  \\label{eq:bov}\n\\end{equation}\nwhich equals the classical omitted-variable bias (no control for $A$).\n\n\\paragraph{Sign preservation condition.}\nSince $D(C)>0$, sign$(\\operatorname{plim}\\hat\\tau) = $ sign$(\\tau\\cdot D(C) + R(C))$.\nFor sign preservation, it suffices that $R(C)$ does not overwhelm $\\tau\\cdot D(C)$.\n\n\\begin{proposition}[Confounding sign preservation --- proportional case]\n\\label{prop:conf_prop}\nIf $f(A) = \\lambda\\,g(A)$ for some constant $\\lambda$ (i.e., the confounder effects on $T$ and $Y$ are proportional), then\n\\begin{equation}\n  B(C) = \\bigl(1-\\xi(C)\\bigr)\\,B_{\\mathrm{OV}},\n  \\label{eq:convex}\n\\end{equation}\nwhere\n\\[\n  \\xi(C) = \\frac{V_B\\;\\sigma_T^2}\n  {V\\bigl(V-V_B+\\sigma_T^2\\bigr)}\n  \\;\\in\\;[0,1],\n\\]\nwhere $V_B=\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])$ and $V=\\operatorname{Var}(g(A))$.\nConsequently, $B(C)$ lies between $0$ and $B_{\\mathrm{OV}}$, and $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau)=\\operatorname{sign}(\\tau)$ whenever $\\operatorname{sign}(\\tau)=\\operatorname{sign}(\\tau+B_{\\mathrm{OV}})$.\n\\end{proposition}\n\n\\begin{proof}\nWhen $f=\\lambda g$: the between-group covariance in~\\eqref{eq:lotc} becomes $\\lambda\\,\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])$, and $\\operatorname{Cov}(g,f)=\\lambda\\,\\operatorname{Var}(g)$.\nSo $R(C)=\\lambda\\bigl(\\operatorname{Var}(g)-\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])\\bigr)=\\lambda\\,V_W$, where $V_W=\\operatorname{Var}(g)-V_B$ with $V_B=\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])$.\nSimilarly, $D(C)=V_W+\\sigma_T^2$.\nHence\n\\[\n  B(C) = \\frac{\\lambda\\,V_W}{V_W+\\sigma_T^2},\\qquad\n  B_{\\mathrm{OV}} = \\frac{\\lambda\\,V}{V+\\sigma_T^2},\n\\]\nwhere $V=\\operatorname{Var}(g)=V_B+V_W$.\nThe ratio\n\\[\n  \\frac{B(C)}{B_{\\mathrm{OV}}} = \\frac{V_W(V+\\sigma_T^2)}{V(V_W+\\sigma_T^2)} = 1 - \\xi(C)\n\\]\nis a decreasing function of $V_B\\in[0,V]$.\nAt $V_B=0$ (no classification, $C$ uniform): $\\xi=0$, $B=B_{\\mathrm{OV}}$.\nAt $V_B=V$ (perfect classification, $C=I$): $\\xi=1$, $B=0$.\nSince $0\\leq V_B\\leq V$, we have $\\xi\\in[0,1]$ and $B(C)\\in[0,B_{\\mathrm{OV}}]$ (with the sign of $B_{\\mathrm{OV}}$).\n\\end{proof}\n\n\\begin{proposition}[Confounding sign preservation --- general case]\n\\label{prop:conf_gen}\nFor general $g$ and $f$ (not necessarily proportional), define the worst-case bias bound\n\\begin{equation}\n  \\bar{B} \\;=\\; \\frac{\\sqrt{\\operatorname{Var}(g(A))\\,\\operatorname{Var}(f(A))}}{\\sigma_T^2}.\n  \\label{eq:bbar}\n\\end{equation}\nIf $|\\tau| > \\bar{B}$, then $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau(C))=\\operatorname{sign}(\\tau)$ for all column-stochastic $C$.\n\\end{proposition}\n\n\\begin{proof}\nWe need $\\operatorname{sign}(\\tau\\cdot D(C)+R(C))=\\operatorname{sign}(\\tau)$, which holds if $|R(C)|<|\\tau|\\cdot D(C)$.\nSince $D(C)\\geq\\sigma_T^2$ (shown in Lemma~\\ref{lem:bias_decomp}), it suffices to show $|R(C)|<|\\tau|\\,\\sigma_T^2$.\n\n\\emph{Step 1: Bound $|R(C)|$.}\n$R(C)=\\mathbb{E}[\\operatorname{Cov}(g(A),f(A)\\mid A^*)]$.\nBy the Cauchy--Schwarz inequality applied to each within-group covariance:\n\\begin{multline*}\n  |\\operatorname{Cov}(g,f\\mid A^*{=}j)|\\\\\n  \\leq \\sqrt{\\operatorname{Var}(g\\mid A^*{=}j)\\,\\operatorname{Var}(f\\mid A^*{=}j)}.\n\\end{multline*}\nTaking expectations and applying Cauchy--Schwarz again:\n\\begin{align*}\n  |R(C)|\n  &\\leq \\mathbb{E}\\bigl[\\sqrt{\\operatorname{Var}(g\\mid A^*)\\,\\operatorname{Var}(f\\mid A^*)}\\bigr]\\\\\n  &\\leq \\sqrt{\\mathbb{E}[\\operatorname{Var}(g\\mid A^*)]\\;\\mathbb{E}[\\operatorname{Var}(f\\mid A^*)]}\\\\\n  &\\leq \\sqrt{\\operatorname{Var}(g(A))\\;\\operatorname{Var}(f(A))},\n\\end{align*}\nwhere the last step uses $\\mathbb{E}[\\operatorname{Var}(X\\mid Y)]\\leq\\operatorname{Var}(X)$ (law of total variance).\n\n\\emph{Step 2: Conclude.}\nThe bias satisfies\n\\[\n  |B(C)| = \\frac{|R(C)|}{D(C)} \\leq \\frac{\\sqrt{\\operatorname{Var}(g)\\,\\operatorname{Var}(f)}}{\\sigma_T^2} = \\bar{B}.\n\\]\nWhen $|\\tau|>\\bar{B}$, the bias cannot cancel $\\tau$, so $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau)=\\operatorname{sign}(\\tau)$ for all $C$.\n\\end{proof}\n\n\\paragraph{Relationship to the omitted-variable condition.}\nA weaker (necessary) condition for sign preservation is $\\operatorname{sign}(\\tau)=\\operatorname{sign}(\\tau_{\\mathrm{OV}})$ where $\\tau_{\\mathrm{OV}}=\\tau+\\operatorname{Cov}(g,f)/\\operatorname{Var}(T)$.\nIf this fails, then $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ (uniform noise) already flips the sign.\nThe rigorous sufficient condition $|\\tau|>\\bar{B}$ implies the weaker condition, since $|B_{\\mathrm{OV}}|=|\\operatorname{Cov}(g,f)|/\\operatorname{Var}(T)\\leq\\bar{B}$ by Cauchy--Schwarz and $\\operatorname{Var}(T)\\geq\\sigma_T^2$.\n\n\\paragraph{Verification for paper parameters ($K{=}3$).}\nWith $\\tau{=}2.0$, $\\boldsymbol{\\alpha}{=}(1.5,{-}1.0)$, $\\boldsymbol{\\beta}^{(A)}{=}(1.0,{-}0.5)$, $\\sigma_T{=}1.0$, $\\mathbf{p}{=}(0.40,0.35,0.25)$:\n\\begin{align*}\n  \\operatorname{Var}(g) &= \\textstyle\\sum_k p_k\\alpha_k^2 - (\\sum_k p_k\\alpha_k)^2\\\\\n  &= 0.962,\\\\\n  \\operatorname{Var}(f) &= \\textstyle\\sum_k p_k(\\beta_k^{(A)})^2 - (\\sum_k p_k\\beta_k^{(A)})^2\\\\\n  &= 0.362,\\\\\n  \\bar{B} &= \\sqrt{0.962\\times 0.362}/1.0^2 = 0.590.\n\\end{align*}\nSince $|\\tau|{=}2.0 > \\bar{B}{=}0.590$, sign preservation is guaranteed for all column-stochastic $C$ by Proposition~\\ref{prop:conf_gen}.\nMoreover, $B_{\\mathrm{OV}}=\\operatorname{Cov}(g,f)/\\operatorname{Var}(T)=0.588/1.962={+}0.300$, giving $\\tau_{\\mathrm{OV}}{=}2.300>0$, confirming that both the necessary and sufficient conditions are satisfied.\n\n\\paragraph{Extension to $K > 3$.}\nFor $K{>}3$, treatment effect coefficients are drawn from a fixed pool with alternating signs and decreasing magnitudes:\n\\begin{multline*}\n  \\boldsymbol{\\beta} = (0,\\; 1.0,\\; {-}0.5,\\; 0.7,\\; {-}0.3,\\\\\n  0.5,\\; {-}0.2,\\; 0.4,\\; {-}0.15,\\; 0.3,\\; \\ldots),\n\\end{multline*}\ntruncated to $K$ entries. The category distribution uses $p_k \\propto 1/(k{+}1)$, normalized to sum to~1. Other topology-specific parameters (confounding strengths, mediator effects, etc.)\\ follow analogous alternating-sign pools.\n\n\\subsection{Proof of Theorem~\\ref{thm:monotone} (Confounding Monotonicity)}\n\\label{app:monotonicity_proof}\n\nUnder the interpolation $C(\\delta)=(1{-}\\delta)I+\\delta C_0$, we prove $|B(C(\\delta))|$ is non-decreasing in $\\delta$ for proportional effects ($f=\\lambda g$) and provide numerical verification for the general case.\nThe proof proceeds by direct algebraic analysis of $V_B(\\delta)=\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*_\\delta])$ as a rational function of $\\delta$, establishing convexity and bounding the derivative at both endpoints.\n\n\\paragraph{Proportional case ($f=\\lambda g$).}\nFrom Proposition~\\ref{prop:conf_prop}, $B(C)=\\lambda V_W/(V_W+\\sigma_T^2)$ where $V_W=\\operatorname{Var}(g)-V_B$ and $V_B(\\delta)=\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*_\\delta])$.\n\n\\emph{Step 1: Convexity of $V_B(\\delta)$.}\nDefine $N_j(\\delta)=\\sum_k g_k\\,C(\\delta)_{jk}\\,p_k$ and $q_j(\\delta)=\\sum_k C(\\delta)_{jk}\\,p_k$.\nBoth are affine in $\\delta$, with $q_j(\\delta)>0$.\nThen $V_B(\\delta)=\\sum_j N_j(\\delta)^2/q_j(\\delta) - \\bar{g}^2$.\nEach term $N_j^2/q_j$ is the composition of the perspective function $(x,t)\\mapsto x^2/t$ (convex for $t>0$) with the affine map $\\delta\\mapsto(N_j(\\delta),\\,q_j(\\delta))$, hence convex in $\\delta$.\nA sum of convex functions is convex, so $V_B(\\delta)$ is convex on $[0,\\delta_{\\max}]$.\n\n\\emph{Step 2: Derivative formula.}\nLet $\\mu_j(\\delta)=N_j(\\delta)/q_j(\\delta)=\\mathbb{E}[g(A)\\mid A^*{=}j]$.\nThen\n\\begin{equation}\n\\frac{dV_B}{d\\delta}\n= -\\sum_{j,k}\\bigl[(C_0)_{jk}-\\mathbf{1}_{j=k}\\bigr]\\,p_k\\,(g_k-\\mu_j(\\delta))^2.\n\\label{eq:dVB}\n\\end{equation}\n\\emph{Derivation.}\n$\\frac{d}{d\\delta}\\frac{N_j^2}{q_j}=2\\mu_j\\dot{N}_j-\\mu_j^2\\dot{q}_j$\nwhere $\\dot{N}_j=m_j^0-g_jp_j$ and $\\dot{q}_j=q_j^0-p_j$ (with $m_j^0=\\sum_k g_k(C_0)_{jk}p_k$, $q_j^0=\\sum_k(C_0)_{jk}p_k$).\nSubstituting and using column-stochasticity ($\\sum_j(C_0)_{jk}=\\sum_j\\mathbf{1}_{j=k}=1$) to cancel the $g_k^2$ terms yields~\\eqref{eq:dVB}.\n\n\\emph{Step 3: $V_B'(0)\\leq 0$ (universal, no conditions on $C_0$).}\nAt $\\delta{=}0$: $\\mu_j(0)=g_j$ (since $C(0)=I$), so $(g_k-\\mu_j(0))^2=(g_k-g_j)^2$.\nThe diagonal terms ($j{=}k$) vanish.\nHence\n\\[\nV_B'(0)=-\\sum_{j\\neq k}(C_0)_{jk}\\,p_k\\,(g_j-g_k)^2\\;\\leq\\; 0,\n\\]\nsince every term is non-negative.\n\n\\emph{Step 4: $V_B'(1)\\leq 0$ for $K{=}2$.}\nFor $K{=}2$ with $C_0=\\bigl[\\begin{smallmatrix}a&1{-}b\\\\1{-}a&b\\end{smallmatrix}\\bigr]$ and $a,b\\geq\\tfrac{1}{2}$,\nset $g_0{=}0$, $g_1{=}1$ without loss of generality\n(the general case scales by $(\\Delta g)^2$).\nAt $\\delta{=}1$: $q_0{=}ap_0{+}(1{-}b)p_1$, $q_1{=}(1{-}a)p_0{+}bp_1$,\n$\\mu_0{=}(1{-}b)p_1/q_0$, $\\mu_1{=}bp_1/q_1$.\nExpanding~\\eqref{eq:dVB} at $\\delta{=}1$ and factoring:\n\\begin{align*}\n  V_B'(1) &= (1{-}a)\\,p_0(\\mu_0^2{-}\\mu_1^2)\\\\\n  &\\quad{}+(1{-}b)\\,p_1\\bigl[(1{-}\\mu_1)^2{-}(1{-}\\mu_0)^2\\bigr] \\\\\n  &= (\\mu_0{-}\\mu_1)\\,\\bigl[(1{-}a)\\,p_0(\\mu_0{+}\\mu_1)\\\\\n  &\\quad{}+(1{-}b)\\,p_1(2{-}\\mu_0{-}\\mu_1)\\bigr].\n\\end{align*}\nThe bracket is non-negative (since $0\\leq\\mu_j\\leq 1$ and all coefficients are non-negative).\nDirect calculation gives $\\mu_0{-}\\mu_1=p_0\\,p_1(1{-}a{-}b)/(q_0\\,q_1)$\n(expand $(1{-}b)\\,q_1-b\\,q_0=p_0(1{-}a{-}b)$).\nUnder $a,b\\geq\\tfrac{1}{2}$: $a{+}b\\geq 1$, so $\\mu_0{-}\\mu_1\\leq 0$ and $V_B'(1)\\leq 0$.\n\n\\emph{Step 5: Monotonicity from convexity.}\nSince $V_B$ is convex (Step~1), its derivative $V_B'$ is non-decreasing.\nWhen $V_B'(1)\\leq 0$, we have $V_B'(\\delta)\\leq V_B'(1)\\leq 0$ for all $\\delta\\in[0,1]$, so $V_B$ is non-increasing.",
      "numLines": 300,
      "startLine": 0,
      "totalLines": 1554
    }
  },
  "sourceToolAssistantUUID": "ab15a1f4-4275-4fd0-a3fa-b3a6818c083d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-25T08:23:34.456Z_

<details open><summary>🔧 Tool call — Read · `toolu_016HMhUAJJPpvhL6hnYZhf6N`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "offset": 300,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b751a3f-f9ca-4e20-b6ab-93aaac0979ca",
  "isSidechain": false,
  "requestId": "req_011CbNxvgfugkhVtfata9pGK",
  "type": "assistant",
  "uuid": "9ed558f4-0466-4602-b2d5-47d6f06b1e48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2ERx3NK2sp7VbE8zaEqJF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12722,
      "cache_read_input_tokens": 51801,
      "output_tokens": 1012,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1012,
          "cache_read_input_tokens": 51801,
          "cache_creation_input_tokens": 12722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12722
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-25T08:23:34.462Z_

<details><summary>↩ Tool result · `toolu_016HMhUAJJPpvhL6hnYZhf6N`</summary>

```text
300	When $V_B'(1)\leq 0$, we have $V_B'(\delta)\leq V_B'(1)\leq 0$ for all $\delta\in[0,1]$, so $V_B$ is non-increasing.
301	
302	\emph{Step 6: $|B(\delta)|$ is non-decreasing.}
303	$V_W(\delta)=\operatorname{Var}(g)-V_B(\delta)$ is non-decreasing (Step~5).
304	The function $h(x)=|\lambda|\,x/(x+\sigma_T^2)$ is strictly increasing for $x\geq 0$.
305	Hence $|B(\delta)|=h(V_W(\delta))$ is non-decreasing. \qed
306	
307	\paragraph{Condition on $C_0$.}
308	The proof requires $V_B'(1)\leq 0$, which is guaranteed for $K{=}2$ when $(C_0)_{jj}\geq\tfrac{1}{2}$ (Step~4).
309	For $K\geq 3$, $V_B'(1)\leq 0$ holds for all $g$ and $p$ if and only if a certain matrix $M-W$ (depending on $C_0$ and $p$) is negative semi-definite; simple diagonal thresholds are sufficient in practice but not universal.
310	Numerical verification across 20{,}000 random $(C_0,p,g)$ triples per $K\in\{3,5,7\}$ with $(C_0)_{jj}\geq 1/K$ finds worst-case $|B|$ step deviations $< 0.013$ (Table~\ref{tab:conjecture_verify}), confirming $\varepsilon$-approximate monotonicity.
311	A $K{=}2$ counterexample ($C_0$ the permutation matrix, $(C_0)_{jj}{=}0$) shows the diagonal condition is necessary: $V_B(\delta)=(\delta{-}\tfrac{1}{2})^2$ increases on $(\tfrac{1}{2},1]$.
312	
313	\paragraph{General case (non-proportional effects).}
314	$|B(C(\delta))|\leq\bar{B}(\delta)$ where $\bar{B}(\delta)=\sqrt{\mathbb{E}[\operatorname{Var}(g\mid A^*_\delta)]\,\mathbb{E}[\operatorname{Var}(f\mid A^*_\delta)]}\,/\,D(\delta)$ (Proposition~\ref{prop:conf_gen}).
315	By the same convexity argument, each $\mathbb{E}[\operatorname{Var}(\cdot\mid A^*_\delta)]$ is non-decreasing in $\delta$, and $D(\delta)=\mathbb{E}[\operatorname{Var}(T\mid A^*_\delta)]$ is non-decreasing.
316	Extended verification (20{,}000 random $C_0$ matrices, $K \in \{3,5,7\}$) reveals worst-case step deviations of 0.011 (confounding), confirming approximate tightness; a strict monotonicity proof for the general case remains open.
317	
318	\begin{remark}[Conditional exact monotonicity]
319	\label{rem:conditional_monotonicity}
320	Exact monotonicity ($V_B'(\delta) \leq 0$ for all $\delta$) holds under the \emph{component-wise diagonal dominance} condition:
321	\begin{equation}
322	  \alpha_j \geq \frac{q_j}{p_j + q_j} \quad \text{for all } j,
323	  \label{eq:dd_condition}
324	\end{equation}
325	where $\alpha_j = (C_0)_{jj}$ and $q_j = \sum_k (C_0)_{jk} p_k$. This condition requires that each class's classification accuracy exceeds a threshold determined by its spillover ratio $q_j/p_j$. The proof uses Cauchy--Schwarz on the endpoint derivative decomposition $V_B'(1) = \sum_j (p_j + q_j)\,e_j^2 - \sum_{j \neq k} (C_0)_{jk}\,p_k\,(g_j - g_k)^2$, where $e_j = g_j - \mu_j$ (full proof in supplementary material).
326	
327	For doubly stochastic $C_0$ with uniform $p$, condition~\eqref{eq:dd_condition} reduces to $\alpha_j \geq 1/2$, which for $K{=}2$ recovers the exact condition in Theorem~\ref{thm:monotone}. Numerical testing ($10^5$ random column-stochastic matrices with $\alpha_j \geq 0.5$) shows the condition holds in $99.3\%$ of cases; the $0.7\%$ violations arise predominantly under class imbalance with maximum step deviation $< 0.001$. When the condition fails, a quantitative bound $V_B'(1) \leq (1{-}c)^2 R_g^2$ (where $c = \min_j \alpha_j$ and $R_g = \max g_k - \min g_k$) ensures violations vanish as classifier accuracy improves.
328	\end{remark}
329	
330	\subsection{Mediation Topology ($A$ = Mediator)}
331	\label{app:mediation}
332	
333	\paragraph{Data-generating process.}
334	$T\to A\to Y$, $T\to Y$.
335	\begin{align*}
336	  T &\sim \operatorname{Bernoulli}(0.5),\\
337	  A\mid T &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\gamma}+\boldsymbol{\delta}\,T)\bigr),\\
338	  Y &= \tau_{\mathrm{dir}}\,T + f(A) + \varepsilon_Y.
339	\end{align*}
340	
341	\paragraph{Bias decomposition.}
342	By Lemma~\ref{lem:bias_decomp}, the direct-effect estimator satisfies:
343	\begin{equation}
344	  \operatorname{plim}\hat\tau_{\mathrm{dir}}(C) = \tau_{\mathrm{dir}} + \frac{\mathbb{E}[\operatorname{Cov}(T,\,f(A)\mid A^*)]}{D(C)}.
345	  \label{eq:med_bias}
346	\end{equation}
347	
348	The key structural difference from confounding: $T$ causes $A$, so the residual covariance $\operatorname{Cov}(T,f(A)\mid A^*)$ captures the indirect effect of $T$ on $Y$ through $A$ that is not absorbed by conditioning on $A^*$.
349	
350	\paragraph{Endpoint analysis.}
351	
352	At $C=I$ ($A^*{=}A$): conditioning on $A$ blocks the mediated path $T\to A\to Y$, so $\operatorname{Cov}(T,f(A)\mid A)=0$ and $\operatorname{plim}\hat\tau=\tau_{\mathrm{dir}}$.
353	
354	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ ($A^*\perp A$): no information about $A$ is used, and
355	\begin{align*}
356	  \mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)] &= \operatorname{Cov}(T,f(A)),\\
357	  D(C) &= \operatorname{Var}(T) = 0.25.
358	\end{align*}
359	The indirect effect is $\tau_{\mathrm{ind}}=\mathbb{E}[f(A)\mid T{=}1]-\mathbb{E}[f(A)\mid T{=}0]$, and
360	\[
361	  \operatorname{Cov}(T,f(A)) = 0.25\,\tau_{\mathrm{ind}}.
362	\]
363	Hence at $C$ uniform: $\operatorname{plim}\hat\tau = \tau_{\mathrm{dir}}+\tau_{\mathrm{ind}} = \tau_{\mathrm{total}}$.
364	
365	\paragraph{Numerical Verification (Mediation sign preservation).}
366	\label{find:med_sign}
367	$\operatorname{sign}(\operatorname{plim}\hat\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{dir}})$ whenever $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$, where $\tau_{\mathrm{total}}=\tau_{\mathrm{dir}}+\tau_{\mathrm{ind}}$.
368	This result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$; a closed-form proof for general $K$ remains open.
369	
370	\begin{proof}
371	Let $R(C)=\mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)]$ and $D(C)=\mathbb{E}[\operatorname{Var}(T\mid A^*)]>0$.
372	
373	\emph{Endpoints.}
374	At $C{=}I$: $f(A)$ is constant given $A{=}A^*$, so $R(I)=0$ and $B(I)=0$.
375	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$: $R=\operatorname{Cov}(T,f(A))=0.25\,\tau_{\mathrm{ind}}$ and $D=\operatorname{Var}(T)=0.25$, giving $B=\tau_{\mathrm{ind}}$.
376	
377	\emph{Within-group structure for binary $T$.}
378	Since $T\in\{0,1\}$, the within-$A^*$-group bias admits a revealing decomposition.
379	Let $p_j=P(T{=}1\mid A^*{=}j)$.
380	Then $\operatorname{Var}(T\mid A^*{=}j)=p_j(1{-}p_j)$ and
381	\begin{multline*}
382	  \operatorname{Cov}(T,f(A)\mid A^*{=}j)\\
383	  = p_j(1{-}p_j)\bigl[\mathbb{E}[f(A)\mid T{=}1,A^*{=}j]\\
384	  \quad{}-\mathbb{E}[f(A)\mid T{=}0,A^*{=}j]\bigr].
385	\end{multline*}
386	Define $\delta_j=\mathbb{E}[f(A)\mid T{=}1,A^*{=}j]-\mathbb{E}[f(A)\mid T{=}0,A^*{=}j]$ as the \emph{conditional indirect effect} in the $A^*{=}j$ subpopulation.
387	Then
388	\begin{align*}
389	  B(C)&=\frac{R(C)}{D(C)}
390	  =\frac{\sum_j q_j\,p_j(1{-}p_j)\,\delta_j}{\sum_j q_j\,p_j(1{-}p_j)}\\
391	  &=\textstyle\sum_j w_j\,\delta_j,
392	\end{align*}
393	a weighted average of the conditional indirect effects, with weights
394	$w_j=q_j p_j(1{-}p_j)\big/\!\sum_\ell q_\ell p_\ell(1{-}p_\ell)\geq 0$
395	summing to~1.
396	
397	At $C{=}I$: each $A^*{=}j$ group has $A{=}j$ a.s., so $\delta_j=f(j)-f(j)=0$ and $B=0$.
398	At $C$ uniform: $\delta_j=\tau_{\mathrm{ind}}$ for all $j$ and $B=\tau_{\mathrm{ind}}$.
399	
400	\emph{Sign preservation.}
401	When $\operatorname{Cov}(g(A),f(A))>0$ (the indirect effect reinforces the direct effect, i.e., $\tau_{\mathrm{dir}}$ and $\tau_{\mathrm{ind}}$ have the same sign), the bias $B(C)\geq 0$ cannot oppose $\tau_{\mathrm{dir}}$, so sign is preserved trivially.
402	
403	When $\tau_{\mathrm{dir}}$ and $\tau_{\mathrm{ind}}$ have opposite signs but $|\tau_{\mathrm{ind}}|<|\tau_{\mathrm{dir}}|$ (i.e., $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$), sign reversal requires some $|\delta_j|>|\tau_{\mathrm{dir}}|$ with the opposing sign.
404	Since each $\delta_j$ is a difference of weighted averages of $f$ values (with weights $P(A{=}k\mid T{=}t,A^*{=}j)$), and $B(C)$ is a convex combination of $\delta_j$, the bound $|B(C)|\leq\max_j|\delta_j|$ holds.
405	We verify numerically that $\max_j|\delta_j|\leq|\tau_{\mathrm{ind}}|$ for all 100{,}000 random $C$ matrices in our experiments, confirming sign preservation.
406	\end{proof}
407	
408	\paragraph{Verification for paper parameters ($K{=}3$).}
409	With $\tau_{\mathrm{dir}}{=}0.5$, $\boldsymbol{\gamma}{=}(0,0,0)$, $\boldsymbol{\delta}{=}(0,0.8,{-}0.6)$, $\boldsymbol{\beta}{=}(0,1.0,{-}0.5)$:
410	
411	$\tau_{\mathrm{ind}}=\mathbb{E}[f(A)\mid T{=}1]-\mathbb{E}[f(A)\mid T{=}0]=0.351$ (computed from the softmax class probabilities).
412	$\tau_{\mathrm{total}}=0.5+0.351=0.851>0$.
413	Since $\tau_{\mathrm{dir}}{>}0$ and $\tau_{\mathrm{total}}{>}0$, sign preservation holds for all $C$.
414	
415	\paragraph{Mediation monotonicity (proportional effects).}
416	\label{par:med_monotone}
417	
418	Under the interpolation $C(\delta)=(1{-}\delta)I+\delta C_0$, we prove $|B(C(\delta))|$ is non-decreasing in $\delta$ when the mediator's effect on $Y$ is proportional to its informativeness about $T$: $f(A)=\lambda\,g(A)$ for some scalar $\lambda$, where $g(k)=\mathbb{E}[T\mid A{=}k]$.
419	
420	\emph{Step 1: Decompose $T$ via the mediator.}
421	Define $g(A)=\mathbb{E}[T\mid A]$ and $\varepsilon_T = T - g(A)$.
422	By construction, $\mathbb{E}[\varepsilon_T\mid A]=0$.
423	By non-differential misclassification ($T\perp A^*\mid A$):
424	$\mathbb{E}[\varepsilon_T\mid A{=}k, A^*{=}j] = 0$,
425	so $\mathbb{E}[\varepsilon_T\mid A^*{=}j]=0$ and $\operatorname{Cov}(\varepsilon_T,\,g(A)\mid A^*{=}j)=0$ for every $j$.
426	
427	\emph{Step 2: Reduce the numerator.}
428	Since $f=\lambda g$:
429	\begin{align*}
430	  R(C) &= \lambda\,\mathbb{E}[\operatorname{Var}(g(A)\mid A^*)] = \lambda\,V_W.
431	\end{align*}
432	
433	\emph{Step 3: Constant additive term in denominator.}
434	\begin{align*}
435	  D(C) &= \mathbb{E}[\operatorname{Var}(T\mid A^*)]
436	       = V_W + \sigma_\varepsilon^2,
437	\end{align*}
438	where $\sigma_\varepsilon^2\equiv\mathbb{E}[\operatorname{Var}(\varepsilon_T\mid A^*)]$.
439	This is constant (independent of $C$):
440	$\mathbb{E}[\operatorname{Var}(\varepsilon_T\mid A^*)]
441	  = \sum_k p_k\,\operatorname{Var}(T\mid A{=}k)
442	  = \mathbb{E}[\operatorname{Var}(T\mid A)]$,
443	where the equality uses column-stochasticity: $\sum_j q_j\,P(A{=}k\mid A^*{=}j)=p_k$.
444	
445	\emph{Step 4: Closed form and monotonicity.}
446	$B(C) = \lambda\,V_W/(V_W+\sigma_\varepsilon^2)$,
447	structurally identical to confounding (Proposition~\ref{prop:conf_prop}) with $\sigma_\varepsilon^2$ playing the role of $\sigma_T^2$.
448	Since $V_B(\delta)$ is convex with $V_B'(0)\leq 0$ (same argument as \S\ref{app:monotonicity_proof}, Steps~1--3), $V_W(\delta)=V{-}V_B(\delta)$ is non-decreasing under the same conditions on $C_0$.
449	Since $h(x)=|\lambda|x/(x+\sigma_\varepsilon^2)$ is increasing, $|B(C(\delta))|$ is non-decreasing.
450	
451	\paragraph{Boundedness of the leakage coefficient.}
452	
453	The mediation bias~\eqref{eq:mediation} writes the residual indirect effect as $(1-\lambda(C))\,\tau_{\mathrm{ind}}$, which (for $\tau_{\mathrm{ind}}\neq 0$) implicitly defines
454	\begin{align}
455	\label{eq:lambda_def}
456	  \lambda(C) &\;:=\; 1-\frac{B(C)}{\tau_{\mathrm{ind}}},\\
457	  B(C)&\;\equiv\;\operatorname{plim}\hat{\tau}_{\mathrm{dir}}(A^*)-\tau_{\mathrm{dir}},\notag\\
458	  \tau_{\mathrm{ind}}&\;=\;\frac{\operatorname{Cov}(T,f(A))}{\operatorname{Var}(T)}.\notag
459	\end{align}
460	Substituting back into~\eqref{eq:mediation} gives the convex-combination form
461	$\operatorname{plim}\hat\tau_{\mathrm{dir}}(C)=\lambda(C)\,\tau_{\mathrm{dir}}+(1-\lambda(C))\,\tau_{\mathrm{total}}$, so $\lambda(C)$ is the weight placing the biased plim between $\tau_{\mathrm{dir}}$ (perfect classification) and $\tau_{\mathrm{total}}$ (no information).
462	
463	\begin{proposition}[Mediation leakage boundedness]
464	\label{prop:lambda_bound}
465	Let $\lambda(C)$ be defined by~\eqref{eq:lambda_def} with $\tau_{\mathrm{ind}}\neq 0$, and let $C$ be column-stochastic.
466	\begin{enumerate}
467	\item[(a)] $\lambda(C)\leq 1$ iff $\operatorname{sign}(B(C))=\operatorname{sign}(\tau_{\mathrm{ind}})$ (the bias points in the direction of the indirect effect; no overcorrection).
468	\item[(b)] $\lambda(C)\geq 0$ iff additionally $|B(C)|\leq|\tau_{\mathrm{ind}}|$ (the bias does not exceed the indirect effect in magnitude).
469	\end{enumerate}
470	Equivalently, $\lambda(C)\in[0,1]$ iff $\operatorname{plim}\hat\tau_{\mathrm{dir}}(C)\in[\min(\tau_{\mathrm{dir}},\tau_{\mathrm{total}}),\,\max(\tau_{\mathrm{dir}},\tau_{\mathrm{total}})]$.
471	
472	Under \emph{proportional effects} ($f(A)=\lambda_0\,g(A)$ with $g(k)=\mathbb{E}[T\mid A{=}k]$), both (a) and (b) hold for every $C$, so $\lambda(C)\in[0,1]$ unconditionally.
473	For \emph{general (non-proportional)} $f$, both (a) and (b) can fail because $\operatorname{Cov}(\mathbb{E}[g\mid A^*],\mathbb{E}[f\mid A^*])$ may differ in sign or magnitude from $\operatorname{Cov}(g,f)$ (a covariance-level analogue of Simpson's paradox under $A^*$ aggregation); the numerical verification below quantifies the empirical rate.
474	The endpoints $\lambda(I)=1$ and $\lambda(C)\to 0$ in the rank-one (uninformative) limit hold in all regimes.
475	
476	\emph{Sign preservation.} When $\lambda(C)\in[0,1]$, the convex-combination form gives $\operatorname{plim}\hat\tau_{\mathrm{dir}}(C)\in[\min(\tau_{\mathrm{dir}},\tau_{\mathrm{total}}),\,\max(\tau_{\mathrm{dir}},\tau_{\mathrm{total}})]$. If additionally $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$, both endpoints share the same sign, so $\operatorname{sign}(\operatorname{plim}\hat\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{dir}})$ for every~$C$. Under proportional effects, $\lambda(C)\in[0,1]$ is automatic (above), so sign preservation of $\hat\tau_{\mathrm{dir}}$ reduces to the single condition $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$.
477	\end{proposition}
478	
479	\begin{proof}
480	\emph{(a),(b).} With $\tau_{\mathrm{ind}}\neq 0$, $\lambda(C)\leq 1\iff B(C)/\tau_{\mathrm{ind}}\geq 0\iff \operatorname{sign}(B(C))=\operatorname{sign}(\tau_{\mathrm{ind}})$. Given (a), $\lambda(C)\geq 0\iff B(C)/\tau_{\mathrm{ind}}\leq 1\iff|B(C)|\leq|\tau_{\mathrm{ind}}|$.
481	
482	\emph{Proportional case.} Step~4 of the mediation derivation gives $B(C)=\lambda_0\,V_W(C)/(V_W(C)+\sigma_\varepsilon^2)$; the rank-one limit $V_W{\to}V$ yields $\tau_{\mathrm{ind}}=\lambda_0\,V/(V+\sigma_\varepsilon^2)$. Both quantities carry $\operatorname{sign}(\lambda_0)$, establishing~(a). The ratio
483	\[
484	  \frac{B(C)}{\tau_{\mathrm{ind}}}\;=\;\frac{V_W(C)\,(V+\sigma_\varepsilon^2)}{V\,(V_W(C)+\sigma_\varepsilon^2)}
485	\]
486	is monotone increasing in $V_W(C)\in[0,V]$ with range $[0,1]$ (its derivative in $V_W$ is $\sigma_\varepsilon^2(V+\sigma_\varepsilon^2)/[V(V_W+\sigma_\varepsilon^2)^2]>0$), establishing~(b). Hence $\lambda(C)\in[0,1]$ unconditionally.
487	
488	\emph{General case.} Substituting $\lambda(C)$ from~\eqref{eq:lambda_def} into~\eqref{eq:mediation} yields $\operatorname{plim}\hat\tau_{\mathrm{dir}}(C)=\lambda(C)\,\tau_{\mathrm{dir}}+(1{-}\lambda(C))\,\tau_{\mathrm{total}}$, so $\lambda(C)\in[0,1]$ iff $\operatorname{plim}\hat\tau_{\mathrm{dir}}(C)$ lies in the closed interval with endpoints $\tau_{\mathrm{dir}}$ and $\tau_{\mathrm{total}}$.
489	
490	\emph{Endpoints.} At $C{=}I$, $A^*{=}A$ a.s., $\mathbb{E}[T\mid A^*]=g(A)$, and FWL gives $\operatorname{plim}\hat\tau_{\mathrm{dir}}=\tau_{\mathrm{dir}}$, hence $B(I)=0$ and $\lambda(I)=1$. At any rank-one $C$ (rows identical), $A^*\perp A$ so $\mathbb{E}[T\mid A^*]$ is constant, the partial regression on $A^*$ has no effect, and $\operatorname{plim}\hat\tau_{\mathrm{dir}}=\operatorname{Cov}(Y,T)/\operatorname{Var}(T)=\tau_{\mathrm{total}}$, giving $B=\tau_{\mathrm{ind}}$ and $\lambda=0$.
491	\end{proof}
492	
493	\paragraph{Relation to the between-variance ratio.}
494	A natural \emph{diagnostic} closely related to $\lambda(C)$ is the between-variance ratio
495	\begin{equation}
496	\label{eq:vb_ratio}
497	  \lambda_V(C) \;:=\; \frac{V_B(C)}{V},
498	\end{equation}
499	where $V_B(C)=\operatorname{Var}\!\bigl(\mathbb{E}[g(A)\mid A^*]\bigr)$ and $V=\operatorname{Var}(g(A))$,
500	which satisfies $\lambda_V(C)\in[0,1]$ unconditionally by the law of total variance applied to $g(A)$. Under proportional effects, $\lambda$ and $\lambda_V$ agree at the endpoints and are related by
501	\begin{multline*}
502	  1-\lambda(C)\;=\;\frac{V_W(C)\,(V+\sigma_\varepsilon^2)}{V\,(V_W(C)+\sigma_\varepsilon^2)}\\
503	  =\;\bigl(1-\lambda_V(C)\bigr)\cdot\frac{V+\sigma_\varepsilon^2}{V_W(C)+\sigma_\varepsilon^2},
504	\end{multline*}
505	so they coincide in the limit $\sigma_\varepsilon^2\gg V$. They generally differ for non-proportional $f$. We use $\lambda$ throughout the main text because it parameterizes~\eqref{eq:mediation} directly; $\lambda_V$ remains a useful summary of the channel quality of $A^*$ as a proxy for $A$ (independent of the structural form of $f$).
506	
507	\paragraph{Numerical verification.}
508	For each $K\in\{3,5,7\}$ we draw $N{=}10{,}000$ configurations $(\pi,g,\sigma_\varepsilon^2,C)$ with $\pi\sim\operatorname{Dirichlet}(\mathbf{1})$, $g\sim\mathcal{N}(0,I_K)$, $\sigma_\varepsilon^2\sim\operatorname{Uniform}(0.1,2)$, columns of $C\sim\operatorname{Dirichlet}(\mathbf{1})$, and evaluate $\lambda(C)$ from~\eqref{eq:lambda_def} in two regimes for $f$:
509	\begin{itemize}\itemsep0pt
510	\item \textbf{Proportional} ($f=\lambda_0\,g$, $\lambda_0\sim\mathcal{N}(0,1)\!\setminus\!\{0\}$): $\lambda(C)\in[0,1]$ in all $30{,}000$ trials (pooled observed range $[1.2{\times}10^{-5},\,0.850]$; zero out-of-bounds), confirming the closed-form bound. Sign preservation of $\hat\tau_{\mathrm{dir}}$ therefore reduces to $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$.
511	\item \textbf{Non-proportional} ($f\sim\mathcal{N}(0,I_K)$ drawn independently of $g$, restricted to $|\tau_{\mathrm{ind}}|\geq 0.05$ to avoid the ill-conditioned regime where $\lambda{=}1{-}B/\tau_{\mathrm{ind}}$ diverges): $\lambda(C)$ exceeds $[0,1]$ in $\sim15$--$17\%$ of trials, illustrating that (a) and (b) are not automatic outside the proportional case.
512	\end{itemize}
513	The diagnostic $\lambda_V(C)$ lies in $[0,1]$ across all $30{,}000$ trials irrespective of regime, as guaranteed by the law of total variance.
514	Reproduction code and numerical results are included in the supplementary material.
515	
516	\subsection{Proof of Theorem~\ref{thm:k3_symmetric} ($K{=}3$ Symmetric Monotonicity)}
517	\label{app:k3_symmetric_proof}
518	
519	\input{k3_symmetric_proof.tex}
520	
521	\begin{remark}[Empirical symmetry of LLM confusion matrices]
522	\label{rem:symmetry}
523	Empirical $K{=}3$ confusion matrices from LLM stance detection deviate substantially from symmetry (median relative Frobenius distance $d_{\mathrm{rel}}{=}0.33$; range 0.30--0.38 across 10 VAST configurations). Theorem~\ref{thm:k3_symmetric} thus serves as a theoretical anchor establishing that exact monotonicity is achievable at $K{=}3$ under the strongest structural assumption; practical coverage for asymmetric matrices relies on the numerical evidence of Conjecture~\ref{conj:monotone} ($\varepsilon < 0.02$ across 545{,}945 adversarial curves including non-symmetric structures).
524	\end{remark}
525	
526	\subsection{Collider Topology ($A$ = Collider)}
527	\label{app:collider}
528	
529	\paragraph{Data-generating process.}
530	$T\to A\leftarrow Y$, $T\to Y$.
531	The treatment effect is unconfounded:
532	\begin{align*}
533	  T &\sim \mathcal{N}(0,1),\quad
534	  Y = \tau\,T + \varepsilon_Y,\\
535	  &\quad \varepsilon_Y\sim\mathcal{N}(0,1),\;\varepsilon_Y\perp T,\notag\\
536	  A\mid T,Y &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\\
537	  &\qquad\boldsymbol{\delta}_T\,T + \boldsymbol{\delta}_Y\,Y)\bigr).
538	\end{align*}
539	The collider $A$ is a common effect of $T$ and $Y$.
540	The no-control estimator (regressing $Y$ on $T$ alone) is consistent: $\operatorname{plim}\hat\tau_{\mathrm{nc}}=\tau$.
541	The researcher erroneously controls for $A^*$, inducing Berkson's bias.
542	
543	\paragraph{Bias decomposition.}
544	Unlike confounding, $\varepsilon_Y$ is not independent of $A$ (since $A$ depends on $Y=\tau T+\varepsilon_Y$), so Lemma~\ref{lem:bias_decomp} does not apply directly.
545	Instead, we derive the bias from the FWL identity~\eqref{eq:fwl}.
546	Writing $\tilde{Y}=\tau\tilde{T}+(\varepsilon_Y-\mathbb{E}[\varepsilon_Y\mid A^*])$ and noting that $\mathbb{E}[\tilde{T}\,\varepsilon_Y]=\mathbb{E}[\operatorname{Cov}(T,\varepsilon_Y\mid A^*)]$ (since $T\perp\varepsilon_Y$ unconditionally):
547	\begin{align}
548	  \operatorname{plim}\hat\tau(C) &= \tau + B(C),\notag\\
549	  B(C) &= \frac{\mathbb{E}[\operatorname{Cov}(T,\,\varepsilon_Y\mid A^*)]}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
550	  \label{eq:bias_col}
551	\end{align}
552	Under non-differential misclassification ($A^*\perp(T,\varepsilon_Y)\mid A$), define $g(k)=\mathbb{E}[T\mid A{=}k]$ and $h(k)=\mathbb{E}[\varepsilon_Y\mid A{=}k]$.
553	By the tower property, $\mathbb{E}[T\mid A^*]=\mathbb{E}[g(A)\mid A^*]$ and $\mathbb{E}[\varepsilon_Y\mid A^*]=\mathbb{E}[h(A)\mid A^*]$.
554	Since $\operatorname{Cov}(T,\varepsilon_Y)=0$, the law of total covariance gives:
555	\[
556	  B(C) = \frac{-\operatorname{Cov}\bigl(\mathbb{E}[g(A)\mid A^*],\;\mathbb{E}[h(A)\mid A^*]\bigr)}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
557	\]
558	
559	\paragraph{Endpoint analysis.}
560	At $C=I$ ($A^*{=}A$):
561	$B(I) = -\operatorname{Cov}(g(A),h(A))\,/\,\mathbb{E}[\operatorname{Var}(T\mid A)] = B_{\mathrm{Berkson}}$,
562	the full Berkson's bias from conditioning on the collider.
563	
564	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ ($A^*\perp A$):
565	$\mathbb{E}[g(A)\mid A^*]$ and $\mathbb{E}[h(A)\mid A^*]$ are constant, so $B=0$ and $\operatorname{plim}\hat\tau=\tau$.
566	
567	This is the structural reverse of confounding: misclassification attenuates the collider-induced bias toward zero, rather than growing bias from zero toward $B_{\mathrm{OV}}$.
568	
569	\begin{proposition}[Collider sign preservation --- proportional case]
570	\label{prop:col_prop}
571	If $h(A)=\lambda\,g(A)$ for some constant $\lambda$, then $|B(C)|\leq|B(I)|$ for all column-stochastic $C$, and $B(C)$ has the same sign as $B(I)$.
572	Consequently, $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ whenever $\operatorname{sign}(\tau)=\operatorname{sign}(\tau+B_{\mathrm{Berkson}})$.
573	\end{proposition}
574	
575	\begin{proof}
576	When $h=\lambda g$, the numerator becomes $-\lambda\,\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])$ and the denominator is $\operatorname{Var}(T)-\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])$.
577	Let $V^*=\operatorname{Var}(\mathbb{E}[g(A)\mid A^*])\in[0,V_g]$ where $V_g=\operatorname{Var}(g(A))$.
578	Then
579	\[
580	  |B(C)| = |\lambda|\,\frac{V^*}{\operatorname{Var}(T)-V^*}.
581	\]
582	The function $x\mapsto x/(a-x)$ is increasing on $[0,a)$.
583	With $a=\operatorname{Var}(T)>V_g\geq V^*$:
584	$|B(C)|\leq|\lambda|\,V_g/(\operatorname{Var}(T)-V_g)=|B(I)|$.
585	At $V^*{=}0$ (uniform $C$): $B{=}0$.  At $V^*{=}V_g$ ($C{=}I$): $B{=}B(I)$.
586	\end{proof}
587	
588	\begin{proposition}[Collider sign preservation --- general case]
589	\label{prop:col_gen}
590	Define
591	\begin{equation}
592	  \bar{B}_{\mathrm{col}} = \frac{\sqrt{\operatorname{Var}(g(A))\,\operatorname{Var}(h(A))}}{\mathbb{E}[\operatorname{Var}(T\mid A)]}.
593	  \label{eq:bbar_col}
594	\end{equation}
595	If $|\tau|>\bar{B}_{\mathrm{col}}$, then $\operatorname{sign}(\operatorname{plim}\hat\tau(C))=\operatorname{sign}(\tau)$ for all column-stochastic $C$.
596	\end{proposition}
597	
598	\begin{proof}
599	\emph{Step~1: Bound the numerator.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ed558f4-0466-4602-b2d5-47d6f06b1e48",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "608b8386-584e-4791-9651-59a28151017b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
      "content": "When $V_B'(1)\\leq 0$, we have $V_B'(\\delta)\\leq V_B'(1)\\leq 0$ for all $\\delta\\in[0,1]$, so $V_B$ is non-increasing.\n\n\\emph{Step 6: $|B(\\delta)|$ is non-decreasing.}\n$V_W(\\delta)=\\operatorname{Var}(g)-V_B(\\delta)$ is non-decreasing (Step~5).\nThe function $h(x)=|\\lambda|\\,x/(x+\\sigma_T^2)$ is strictly increasing for $x\\geq 0$.\nHence $|B(\\delta)|=h(V_W(\\delta))$ is non-decreasing. \\qed\n\n\\paragraph{Condition on $C_0$.}\nThe proof requires $V_B'(1)\\leq 0$, which is guaranteed for $K{=}2$ when $(C_0)_{jj}\\geq\\tfrac{1}{2}$ (Step~4).\nFor $K\\geq 3$, $V_B'(1)\\leq 0$ holds for all $g$ and $p$ if and only if a certain matrix $M-W$ (depending on $C_0$ and $p$) is negative semi-definite; simple diagonal thresholds are sufficient in practice but not universal.\nNumerical verification across 20{,}000 random $(C_0,p,g)$ triples per $K\\in\\{3,5,7\\}$ with $(C_0)_{jj}\\geq 1/K$ finds worst-case $|B|$ step deviations $< 0.013$ (Table~\\ref{tab:conjecture_verify}), confirming $\\varepsilon$-approximate monotonicity.\nA $K{=}2$ counterexample ($C_0$ the permutation matrix, $(C_0)_{jj}{=}0$) shows the diagonal condition is necessary: $V_B(\\delta)=(\\delta{-}\\tfrac{1}{2})^2$ increases on $(\\tfrac{1}{2},1]$.\n\n\\paragraph{General case (non-proportional effects).}\n$|B(C(\\delta))|\\leq\\bar{B}(\\delta)$ where $\\bar{B}(\\delta)=\\sqrt{\\mathbb{E}[\\operatorname{Var}(g\\mid A^*_\\delta)]\\,\\mathbb{E}[\\operatorname{Var}(f\\mid A^*_\\delta)]}\\,/\\,D(\\delta)$ (Proposition~\\ref{prop:conf_gen}).\nBy the same convexity argument, each $\\mathbb{E}[\\operatorname{Var}(\\cdot\\mid A^*_\\delta)]$ is non-decreasing in $\\delta$, and $D(\\delta)=\\mathbb{E}[\\operatorname{Var}(T\\mid A^*_\\delta)]$ is non-decreasing.\nExtended verification (20{,}000 random $C_0$ matrices, $K \\in \\{3,5,7\\}$) reveals worst-case step deviations of 0.011 (confounding), confirming approximate tightness; a strict monotonicity proof for the general case remains open.\n\n\\begin{remark}[Conditional exact monotonicity]\n\\label{rem:conditional_monotonicity}\nExact monotonicity ($V_B'(\\delta) \\leq 0$ for all $\\delta$) holds under the \\emph{component-wise diagonal dominance} condition:\n\\begin{equation}\n  \\alpha_j \\geq \\frac{q_j}{p_j + q_j} \\quad \\text{for all } j,\n  \\label{eq:dd_condition}\n\\end{equation}\nwhere $\\alpha_j = (C_0)_{jj}$ and $q_j = \\sum_k (C_0)_{jk} p_k$. This condition requires that each class's classification accuracy exceeds a threshold determined by its spillover ratio $q_j/p_j$. The proof uses Cauchy--Schwarz on the endpoint derivative decomposition $V_B'(1) = \\sum_j (p_j + q_j)\\,e_j^2 - \\sum_{j \\neq k} (C_0)_{jk}\\,p_k\\,(g_j - g_k)^2$, where $e_j = g_j - \\mu_j$ (full proof in supplementary material).\n\nFor doubly stochastic $C_0$ with uniform $p$, condition~\\eqref{eq:dd_condition} reduces to $\\alpha_j \\geq 1/2$, which for $K{=}2$ recovers the exact condition in Theorem~\\ref{thm:monotone}. Numerical testing ($10^5$ random column-stochastic matrices with $\\alpha_j \\geq 0.5$) shows the condition holds in $99.3\\%$ of cases; the $0.7\\%$ violations arise predominantly under class imbalance with maximum step deviation $< 0.001$. When the condition fails, a quantitative bound $V_B'(1) \\leq (1{-}c)^2 R_g^2$ (where $c = \\min_j \\alpha_j$ and $R_g = \\max g_k - \\min g_k$) ensures violations vanish as classifier accuracy improves.\n\\end{remark}\n\n\\subsection{Mediation Topology ($A$ = Mediator)}\n\\label{app:mediation}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\to Y$, $T\\to Y$.\n\\begin{align*}\n  T &\\sim \\operatorname{Bernoulli}(0.5),\\\\\n  A\\mid T &\\sim \\operatorname{Categorical}\\bigl(\\operatorname{softmax}(\\boldsymbol{\\gamma}+\\boldsymbol{\\delta}\\,T)\\bigr),\\\\\n  Y &= \\tau_{\\mathrm{dir}}\\,T + f(A) + \\varepsilon_Y.\n\\end{align*}\n\n\\paragraph{Bias decomposition.}\nBy Lemma~\\ref{lem:bias_decomp}, the direct-effect estimator satisfies:\n\\begin{equation}\n  \\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C) = \\tau_{\\mathrm{dir}} + \\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,f(A)\\mid A^*)]}{D(C)}.\n  \\label{eq:med_bias}\n\\end{equation}\n\nThe key structural difference from confounding: $T$ causes $A$, so the residual covariance $\\operatorname{Cov}(T,f(A)\\mid A^*)$ captures the indirect effect of $T$ on $Y$ through $A$ that is not absorbed by conditioning on $A^*$.\n\n\\paragraph{Endpoint analysis.}\n\nAt $C=I$ ($A^*{=}A$): conditioning on $A$ blocks the mediated path $T\\to A\\to Y$, so $\\operatorname{Cov}(T,f(A)\\mid A)=0$ and $\\operatorname{plim}\\hat\\tau=\\tau_{\\mathrm{dir}}$.\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ ($A^*\\perp A$): no information about $A$ is used, and\n\\begin{align*}\n  \\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)] &= \\operatorname{Cov}(T,f(A)),\\\\\n  D(C) &= \\operatorname{Var}(T) = 0.25.\n\\end{align*}\nThe indirect effect is $\\tau_{\\mathrm{ind}}=\\mathbb{E}[f(A)\\mid T{=}1]-\\mathbb{E}[f(A)\\mid T{=}0]$, and\n\\[\n  \\operatorname{Cov}(T,f(A)) = 0.25\\,\\tau_{\\mathrm{ind}}.\n\\]\nHence at $C$ uniform: $\\operatorname{plim}\\hat\\tau = \\tau_{\\mathrm{dir}}+\\tau_{\\mathrm{ind}} = \\tau_{\\mathrm{total}}$.\n\n\\paragraph{Numerical Verification (Mediation sign preservation).}\n\\label{find:med_sign}\n$\\operatorname{sign}(\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{dir}})$ whenever $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$, where $\\tau_{\\mathrm{total}}=\\tau_{\\mathrm{dir}}+\\tau_{\\mathrm{ind}}$.\nThis result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$; a closed-form proof for general $K$ remains open.\n\n\\begin{proof}\nLet $R(C)=\\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)]$ and $D(C)=\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]>0$.\n\n\\emph{Endpoints.}\nAt $C{=}I$: $f(A)$ is constant given $A{=}A^*$, so $R(I)=0$ and $B(I)=0$.\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$: $R=\\operatorname{Cov}(T,f(A))=0.25\\,\\tau_{\\mathrm{ind}}$ and $D=\\operatorname{Var}(T)=0.25$, giving $B=\\tau_{\\mathrm{ind}}$.\n\n\\emph{Within-group structure for binary $T$.}\nSince $T\\in\\{0,1\\}$, the within-$A^*$-group bias admits a revealing decomposition.\nLet $p_j=P(T{=}1\\mid A^*{=}j)$.\nThen $\\operatorname{Var}(T\\mid A^*{=}j)=p_j(1{-}p_j)$ and\n\\begin{multline*}\n  \\operatorname{Cov}(T,f(A)\\mid A^*{=}j)\\\\\n  = p_j(1{-}p_j)\\bigl[\\mathbb{E}[f(A)\\mid T{=}1,A^*{=}j]\\\\\n  \\quad{}-\\mathbb{E}[f(A)\\mid T{=}0,A^*{=}j]\\bigr].\n\\end{multline*}\nDefine $\\delta_j=\\mathbb{E}[f(A)\\mid T{=}1,A^*{=}j]-\\mathbb{E}[f(A)\\mid T{=}0,A^*{=}j]$ as the \\emph{conditional indirect effect} in the $A^*{=}j$ subpopulation.\nThen\n\\begin{align*}\n  B(C)&=\\frac{R(C)}{D(C)}\n  =\\frac{\\sum_j q_j\\,p_j(1{-}p_j)\\,\\delta_j}{\\sum_j q_j\\,p_j(1{-}p_j)}\\\\\n  &=\\textstyle\\sum_j w_j\\,\\delta_j,\n\\end{align*}\na weighted average of the conditional indirect effects, with weights\n$w_j=q_j p_j(1{-}p_j)\\big/\\!\\sum_\\ell q_\\ell p_\\ell(1{-}p_\\ell)\\geq 0$\nsumming to~1.\n\nAt $C{=}I$: each $A^*{=}j$ group has $A{=}j$ a.s., so $\\delta_j=f(j)-f(j)=0$ and $B=0$.\nAt $C$ uniform: $\\delta_j=\\tau_{\\mathrm{ind}}$ for all $j$ and $B=\\tau_{\\mathrm{ind}}$.\n\n\\emph{Sign preservation.}\nWhen $\\operatorname{Cov}(g(A),f(A))>0$ (the indirect effect reinforces the direct effect, i.e., $\\tau_{\\mathrm{dir}}$ and $\\tau_{\\mathrm{ind}}$ have the same sign), the bias $B(C)\\geq 0$ cannot oppose $\\tau_{\\mathrm{dir}}$, so sign is preserved trivially.\n\nWhen $\\tau_{\\mathrm{dir}}$ and $\\tau_{\\mathrm{ind}}$ have opposite signs but $|\\tau_{\\mathrm{ind}}|<|\\tau_{\\mathrm{dir}}|$ (i.e., $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$), sign reversal requires some $|\\delta_j|>|\\tau_{\\mathrm{dir}}|$ with the opposing sign.\nSince each $\\delta_j$ is a difference of weighted averages of $f$ values (with weights $P(A{=}k\\mid T{=}t,A^*{=}j)$), and $B(C)$ is a convex combination of $\\delta_j$, the bound $|B(C)|\\leq\\max_j|\\delta_j|$ holds.\nWe verify numerically that $\\max_j|\\delta_j|\\leq|\\tau_{\\mathrm{ind}}|$ for all 100{,}000 random $C$ matrices in our experiments, confirming sign preservation.\n\\end{proof}\n\n\\paragraph{Verification for paper parameters ($K{=}3$).}\nWith $\\tau_{\\mathrm{dir}}{=}0.5$, $\\boldsymbol{\\gamma}{=}(0,0,0)$, $\\boldsymbol{\\delta}{=}(0,0.8,{-}0.6)$, $\\boldsymbol{\\beta}{=}(0,1.0,{-}0.5)$:\n\n$\\tau_{\\mathrm{ind}}=\\mathbb{E}[f(A)\\mid T{=}1]-\\mathbb{E}[f(A)\\mid T{=}0]=0.351$ (computed from the softmax class probabilities).\n$\\tau_{\\mathrm{total}}=0.5+0.351=0.851>0$.\nSince $\\tau_{\\mathrm{dir}}{>}0$ and $\\tau_{\\mathrm{total}}{>}0$, sign preservation holds for all $C$.\n\n\\paragraph{Mediation monotonicity (proportional effects).}\n\\label{par:med_monotone}\n\nUnder the interpolation $C(\\delta)=(1{-}\\delta)I+\\delta C_0$, we prove $|B(C(\\delta))|$ is non-decreasing in $\\delta$ when the mediator's effect on $Y$ is proportional to its informativeness about $T$: $f(A)=\\lambda\\,g(A)$ for some scalar $\\lambda$, where $g(k)=\\mathbb{E}[T\\mid A{=}k]$.\n\n\\emph{Step 1: Decompose $T$ via the mediator.}\nDefine $g(A)=\\mathbb{E}[T\\mid A]$ and $\\varepsilon_T = T - g(A)$.\nBy construction, $\\mathbb{E}[\\varepsilon_T\\mid A]=0$.\nBy non-differential misclassification ($T\\perp A^*\\mid A$):\n$\\mathbb{E}[\\varepsilon_T\\mid A{=}k, A^*{=}j] = 0$,\nso $\\mathbb{E}[\\varepsilon_T\\mid A^*{=}j]=0$ and $\\operatorname{Cov}(\\varepsilon_T,\\,g(A)\\mid A^*{=}j)=0$ for every $j$.\n\n\\emph{Step 2: Reduce the numerator.}\nSince $f=\\lambda g$:\n\\begin{align*}\n  R(C) &= \\lambda\\,\\mathbb{E}[\\operatorname{Var}(g(A)\\mid A^*)] = \\lambda\\,V_W.\n\\end{align*}\n\n\\emph{Step 3: Constant additive term in denominator.}\n\\begin{align*}\n  D(C) &= \\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]\n       = V_W + \\sigma_\\varepsilon^2,\n\\end{align*}\nwhere $\\sigma_\\varepsilon^2\\equiv\\mathbb{E}[\\operatorname{Var}(\\varepsilon_T\\mid A^*)]$.\nThis is constant (independent of $C$):\n$\\mathbb{E}[\\operatorname{Var}(\\varepsilon_T\\mid A^*)]\n  = \\sum_k p_k\\,\\operatorname{Var}(T\\mid A{=}k)\n  = \\mathbb{E}[\\operatorname{Var}(T\\mid A)]$,\nwhere the equality uses column-stochasticity: $\\sum_j q_j\\,P(A{=}k\\mid A^*{=}j)=p_k$.\n\n\\emph{Step 4: Closed form and monotonicity.}\n$B(C) = \\lambda\\,V_W/(V_W+\\sigma_\\varepsilon^2)$,\nstructurally identical to confounding (Proposition~\\ref{prop:conf_prop}) with $\\sigma_\\varepsilon^2$ playing the role of $\\sigma_T^2$.\nSince $V_B(\\delta)$ is convex with $V_B'(0)\\leq 0$ (same argument as \\S\\ref{app:monotonicity_proof}, Steps~1--3), $V_W(\\delta)=V{-}V_B(\\delta)$ is non-decreasing under the same conditions on $C_0$.\nSince $h(x)=|\\lambda|x/(x+\\sigma_\\varepsilon^2)$ is increasing, $|B(C(\\delta))|$ is non-decreasing.\n\n\\paragraph{Boundedness of the leakage coefficient.}\n\nThe mediation bias~\\eqref{eq:mediation} writes the residual indirect effect as $(1-\\lambda(C))\\,\\tau_{\\mathrm{ind}}$, which (for $\\tau_{\\mathrm{ind}}\\neq 0$) implicitly defines\n\\begin{align}\n\\label{eq:lambda_def}\n  \\lambda(C) &\\;:=\\; 1-\\frac{B(C)}{\\tau_{\\mathrm{ind}}},\\\\\n  B(C)&\\;\\equiv\\;\\operatorname{plim}\\hat{\\tau}_{\\mathrm{dir}}(A^*)-\\tau_{\\mathrm{dir}},\\notag\\\\\n  \\tau_{\\mathrm{ind}}&\\;=\\;\\frac{\\operatorname{Cov}(T,f(A))}{\\operatorname{Var}(T)}.\\notag\n\\end{align}\nSubstituting back into~\\eqref{eq:mediation} gives the convex-combination form\n$\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C)=\\lambda(C)\\,\\tau_{\\mathrm{dir}}+(1-\\lambda(C))\\,\\tau_{\\mathrm{total}}$, so $\\lambda(C)$ is the weight placing the biased plim between $\\tau_{\\mathrm{dir}}$ (perfect classification) and $\\tau_{\\mathrm{total}}$ (no information).\n\n\\begin{proposition}[Mediation leakage boundedness]\n\\label{prop:lambda_bound}\nLet $\\lambda(C)$ be defined by~\\eqref{eq:lambda_def} with $\\tau_{\\mathrm{ind}}\\neq 0$, and let $C$ be column-stochastic.\n\\begin{enumerate}\n\\item[(a)] $\\lambda(C)\\leq 1$ iff $\\operatorname{sign}(B(C))=\\operatorname{sign}(\\tau_{\\mathrm{ind}})$ (the bias points in the direction of the indirect effect; no overcorrection).\n\\item[(b)] $\\lambda(C)\\geq 0$ iff additionally $|B(C)|\\leq|\\tau_{\\mathrm{ind}}|$ (the bias does not exceed the indirect effect in magnitude).\n\\end{enumerate}\nEquivalently, $\\lambda(C)\\in[0,1]$ iff $\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C)\\in[\\min(\\tau_{\\mathrm{dir}},\\tau_{\\mathrm{total}}),\\,\\max(\\tau_{\\mathrm{dir}},\\tau_{\\mathrm{total}})]$.\n\nUnder \\emph{proportional effects} ($f(A)=\\lambda_0\\,g(A)$ with $g(k)=\\mathbb{E}[T\\mid A{=}k]$), both (a) and (b) hold for every $C$, so $\\lambda(C)\\in[0,1]$ unconditionally.\nFor \\emph{general (non-proportional)} $f$, both (a) and (b) can fail because $\\operatorname{Cov}(\\mathbb{E}[g\\mid A^*],\\mathbb{E}[f\\mid A^*])$ may differ in sign or magnitude from $\\operatorname{Cov}(g,f)$ (a covariance-level analogue of Simpson's paradox under $A^*$ aggregation); the numerical verification below quantifies the empirical rate.\nThe endpoints $\\lambda(I)=1$ and $\\lambda(C)\\to 0$ in the rank-one (uninformative) limit hold in all regimes.\n\n\\emph{Sign preservation.} When $\\lambda(C)\\in[0,1]$, the convex-combination form gives $\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C)\\in[\\min(\\tau_{\\mathrm{dir}},\\tau_{\\mathrm{total}}),\\,\\max(\\tau_{\\mathrm{dir}},\\tau_{\\mathrm{total}})]$. If additionally $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$, both endpoints share the same sign, so $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{dir}})$ for every~$C$. Under proportional effects, $\\lambda(C)\\in[0,1]$ is automatic (above), so sign preservation of $\\hat\\tau_{\\mathrm{dir}}$ reduces to the single condition $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$.\n\\end{proposition}\n\n\\begin{proof}\n\\emph{(a),(b).} With $\\tau_{\\mathrm{ind}}\\neq 0$, $\\lambda(C)\\leq 1\\iff B(C)/\\tau_{\\mathrm{ind}}\\geq 0\\iff \\operatorname{sign}(B(C))=\\operatorname{sign}(\\tau_{\\mathrm{ind}})$. Given (a), $\\lambda(C)\\geq 0\\iff B(C)/\\tau_{\\mathrm{ind}}\\leq 1\\iff|B(C)|\\leq|\\tau_{\\mathrm{ind}}|$.\n\n\\emph{Proportional case.} Step~4 of the mediation derivation gives $B(C)=\\lambda_0\\,V_W(C)/(V_W(C)+\\sigma_\\varepsilon^2)$; the rank-one limit $V_W{\\to}V$ yields $\\tau_{\\mathrm{ind}}=\\lambda_0\\,V/(V+\\sigma_\\varepsilon^2)$. Both quantities carry $\\operatorname{sign}(\\lambda_0)$, establishing~(a). The ratio\n\\[\n  \\frac{B(C)}{\\tau_{\\mathrm{ind}}}\\;=\\;\\frac{V_W(C)\\,(V+\\sigma_\\varepsilon^2)}{V\\,(V_W(C)+\\sigma_\\varepsilon^2)}\n\\]\nis monotone increasing in $V_W(C)\\in[0,V]$ with range $[0,1]$ (its derivative in $V_W$ is $\\sigma_\\varepsilon^2(V+\\sigma_\\varepsilon^2)/[V(V_W+\\sigma_\\varepsilon^2)^2]>0$), establishing~(b). Hence $\\lambda(C)\\in[0,1]$ unconditionally.\n\n\\emph{General case.} Substituting $\\lambda(C)$ from~\\eqref{eq:lambda_def} into~\\eqref{eq:mediation} yields $\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C)=\\lambda(C)\\,\\tau_{\\mathrm{dir}}+(1{-}\\lambda(C))\\,\\tau_{\\mathrm{total}}$, so $\\lambda(C)\\in[0,1]$ iff $\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}(C)$ lies in the closed interval with endpoints $\\tau_{\\mathrm{dir}}$ and $\\tau_{\\mathrm{total}}$.\n\n\\emph{Endpoints.} At $C{=}I$, $A^*{=}A$ a.s., $\\mathbb{E}[T\\mid A^*]=g(A)$, and FWL gives $\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}=\\tau_{\\mathrm{dir}}$, hence $B(I)=0$ and $\\lambda(I)=1$. At any rank-one $C$ (rows identical), $A^*\\perp A$ so $\\mathbb{E}[T\\mid A^*]$ is constant, the partial regression on $A^*$ has no effect, and $\\operatorname{plim}\\hat\\tau_{\\mathrm{dir}}=\\operatorname{Cov}(Y,T)/\\operatorname{Var}(T)=\\tau_{\\mathrm{total}}$, giving $B=\\tau_{\\mathrm{ind}}$ and $\\lambda=0$.\n\\end{proof}\n\n\\paragraph{Relation to the between-variance ratio.}\nA natural \\emph{diagnostic} closely related to $\\lambda(C)$ is the between-variance ratio\n\\begin{equation}\n\\label{eq:vb_ratio}\n  \\lambda_V(C) \\;:=\\; \\frac{V_B(C)}{V},\n\\end{equation}\nwhere $V_B(C)=\\operatorname{Var}\\!\\bigl(\\mathbb{E}[g(A)\\mid A^*]\\bigr)$ and $V=\\operatorname{Var}(g(A))$,\nwhich satisfies $\\lambda_V(C)\\in[0,1]$ unconditionally by the law of total variance applied to $g(A)$. Under proportional effects, $\\lambda$ and $\\lambda_V$ agree at the endpoints and are related by\n\\begin{multline*}\n  1-\\lambda(C)\\;=\\;\\frac{V_W(C)\\,(V+\\sigma_\\varepsilon^2)}{V\\,(V_W(C)+\\sigma_\\varepsilon^2)}\\\\\n  =\\;\\bigl(1-\\lambda_V(C)\\bigr)\\cdot\\frac{V+\\sigma_\\varepsilon^2}{V_W(C)+\\sigma_\\varepsilon^2},\n\\end{multline*}\nso they coincide in the limit $\\sigma_\\varepsilon^2\\gg V$. They generally differ for non-proportional $f$. We use $\\lambda$ throughout the main text because it parameterizes~\\eqref{eq:mediation} directly; $\\lambda_V$ remains a useful summary of the channel quality of $A^*$ as a proxy for $A$ (independent of the structural form of $f$).\n\n\\paragraph{Numerical verification.}\nFor each $K\\in\\{3,5,7\\}$ we draw $N{=}10{,}000$ configurations $(\\pi,g,\\sigma_\\varepsilon^2,C)$ with $\\pi\\sim\\operatorname{Dirichlet}(\\mathbf{1})$, $g\\sim\\mathcal{N}(0,I_K)$, $\\sigma_\\varepsilon^2\\sim\\operatorname{Uniform}(0.1,2)$, columns of $C\\sim\\operatorname{Dirichlet}(\\mathbf{1})$, and evaluate $\\lambda(C)$ from~\\eqref{eq:lambda_def} in two regimes for $f$:\n\\begin{itemize}\\itemsep0pt\n\\item \\textbf{Proportional} ($f=\\lambda_0\\,g$, $\\lambda_0\\sim\\mathcal{N}(0,1)\\!\\setminus\\!\\{0\\}$): $\\lambda(C)\\in[0,1]$ in all $30{,}000$ trials (pooled observed range $[1.2{\\times}10^{-5},\\,0.850]$; zero out-of-bounds), confirming the closed-form bound. Sign preservation of $\\hat\\tau_{\\mathrm{dir}}$ therefore reduces to $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$.\n\\item \\textbf{Non-proportional} ($f\\sim\\mathcal{N}(0,I_K)$ drawn independently of $g$, restricted to $|\\tau_{\\mathrm{ind}}|\\geq 0.05$ to avoid the ill-conditioned regime where $\\lambda{=}1{-}B/\\tau_{\\mathrm{ind}}$ diverges): $\\lambda(C)$ exceeds $[0,1]$ in $\\sim15$--$17\\%$ of trials, illustrating that (a) and (b) are not automatic outside the proportional case.\n\\end{itemize}\nThe diagnostic $\\lambda_V(C)$ lies in $[0,1]$ across all $30{,}000$ trials irrespective of regime, as guaranteed by the law of total variance.\nReproduction code and numerical results are included in the supplementary material.\n\n\\subsection{Proof of Theorem~\\ref{thm:k3_symmetric} ($K{=}3$ Symmetric Monotonicity)}\n\\label{app:k3_symmetric_proof}\n\n\\input{k3_symmetric_proof.tex}\n\n\\begin{remark}[Empirical symmetry of LLM confusion matrices]\n\\label{rem:symmetry}\nEmpirical $K{=}3$ confusion matrices from LLM stance detection deviate substantially from symmetry (median relative Frobenius distance $d_{\\mathrm{rel}}{=}0.33$; range 0.30--0.38 across 10 VAST configurations). Theorem~\\ref{thm:k3_symmetric} thus serves as a theoretical anchor establishing that exact monotonicity is achievable at $K{=}3$ under the strongest structural assumption; practical coverage for asymmetric matrices relies on the numerical evidence of Conjecture~\\ref{conj:monotone} ($\\varepsilon < 0.02$ across 545{,}945 adversarial curves including non-symmetric structures).\n\\end{remark}\n\n\\subsection{Collider Topology ($A$ = Collider)}\n\\label{app:collider}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\leftarrow Y$, $T\\to Y$.\nThe treatment effect is unconfounded:\n\\begin{align*}\n  T &\\sim \\mathcal{N}(0,1),\\quad\n  Y = \\tau\\,T + \\varepsilon_Y,\\\\\n  &\\quad \\varepsilon_Y\\sim\\mathcal{N}(0,1),\\;\\varepsilon_Y\\perp T,\\notag\\\\\n  A\\mid T,Y &\\sim \\operatorname{Categorical}\\bigl(\\operatorname{softmax}(\\\\\n  &\\qquad\\boldsymbol{\\delta}_T\\,T + \\boldsymbol{\\delta}_Y\\,Y)\\bigr).\n\\end{align*}\nThe collider $A$ is a common effect of $T$ and $Y$.\nThe no-control estimator (regressing $Y$ on $T$ alone) is consistent: $\\operatorname{plim}\\hat\\tau_{\\mathrm{nc}}=\\tau$.\nThe researcher erroneously controls for $A^*$, inducing Berkson's bias.\n\n\\paragraph{Bias decomposition.}\nUnlike confounding, $\\varepsilon_Y$ is not independent of $A$ (since $A$ depends on $Y=\\tau T+\\varepsilon_Y$), so Lemma~\\ref{lem:bias_decomp} does not apply directly.\nInstead, we derive the bias from the FWL identity~\\eqref{eq:fwl}.\nWriting $\\tilde{Y}=\\tau\\tilde{T}+(\\varepsilon_Y-\\mathbb{E}[\\varepsilon_Y\\mid A^*])$ and noting that $\\mathbb{E}[\\tilde{T}\\,\\varepsilon_Y]=\\mathbb{E}[\\operatorname{Cov}(T,\\varepsilon_Y\\mid A^*)]$ (since $T\\perp\\varepsilon_Y$ unconditionally):\n\\begin{align}\n  \\operatorname{plim}\\hat\\tau(C) &= \\tau + B(C),\\notag\\\\\n  B(C) &= \\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,\\varepsilon_Y\\mid A^*)]}{\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]}.\n  \\label{eq:bias_col}\n\\end{align}\nUnder non-differential misclassification ($A^*\\perp(T,\\varepsilon_Y)\\mid A$), define $g(k)=\\mathbb{E}[T\\mid A{=}k]$ and $h(k)=\\mathbb{E}[\\varepsilon_Y\\mid A{=}k]$.\nBy the tower property, $\\mathbb{E}[T\\mid A^*]=\\mathbb{E}[g(A)\\mid A^*]$ and $\\mathbb{E}[\\varepsilon_Y\\mid A^*]=\\mathbb{E}[h(A)\\mid A^*]$.\nSince $\\operatorname{Cov}(T,\\varepsilon_Y)=0$, the law of total covariance gives:\n\\[\n  B(C) = \\frac{-\\operatorname{Cov}\\bigl(\\mathbb{E}[g(A)\\mid A^*],\\;\\mathbb{E}[h(A)\\mid A^*]\\bigr)}{\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]}.\n\\]\n\n\\paragraph{Endpoint analysis.}\nAt $C=I$ ($A^*{=}A$):\n$B(I) = -\\operatorname{Cov}(g(A),h(A))\\,/\\,\\mathbb{E}[\\operatorname{Var}(T\\mid A)] = B_{\\mathrm{Berkson}}$,\nthe full Berkson's bias from conditioning on the collider.\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$ ($A^*\\perp A$):\n$\\mathbb{E}[g(A)\\mid A^*]$ and $\\mathbb{E}[h(A)\\mid A^*]$ are constant, so $B=0$ and $\\operatorname{plim}\\hat\\tau=\\tau$.\n\nThis is the structural reverse of confounding: misclassification attenuates the collider-induced bias toward zero, rather than growing bias from zero toward $B_{\\mathrm{OV}}$.\n\n\\begin{proposition}[Collider sign preservation --- proportional case]\n\\label{prop:col_prop}\nIf $h(A)=\\lambda\\,g(A)$ for some constant $\\lambda$, then $|B(C)|\\leq|B(I)|$ for all column-stochastic $C$, and $B(C)$ has the same sign as $B(I)$.\nConsequently, $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau)=\\operatorname{sign}(\\tau)$ whenever $\\operatorname{sign}(\\tau)=\\operatorname{sign}(\\tau+B_{\\mathrm{Berkson}})$.\n\\end{proposition}\n\n\\begin{proof}\nWhen $h=\\lambda g$, the numerator becomes $-\\lambda\\,\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])$ and the denominator is $\\operatorname{Var}(T)-\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])$.\nLet $V^*=\\operatorname{Var}(\\mathbb{E}[g(A)\\mid A^*])\\in[0,V_g]$ where $V_g=\\operatorname{Var}(g(A))$.\nThen\n\\[\n  |B(C)| = |\\lambda|\\,\\frac{V^*}{\\operatorname{Var}(T)-V^*}.\n\\]\nThe function $x\\mapsto x/(a-x)$ is increasing on $[0,a)$.\nWith $a=\\operatorname{Var}(T)>V_g\\geq V^*$:\n$|B(C)|\\leq|\\lambda|\\,V_g/(\\operatorname{Var}(T)-V_g)=|B(I)|$.\nAt $V^*{=}0$ (uniform $C$): $B{=}0$.  At $V^*{=}V_g$ ($C{=}I$): $B{=}B(I)$.\n\\end{proof}\n\n\\begin{proposition}[Collider sign preservation --- general case]\n\\label{prop:col_gen}\nDefine\n\\begin{equation}\n  \\bar{B}_{\\mathrm{col}} = \\frac{\\sqrt{\\operatorname{Var}(g(A))\\,\\operatorname{Var}(h(A))}}{\\mathbb{E}[\\operatorname{Var}(T\\mid A)]}.\n  \\label{eq:bbar_col}\n\\end{equation}\nIf $|\\tau|>\\bar{B}_{\\mathrm{col}}$, then $\\operatorname{sign}(\\operatorname{plim}\\hat\\tau(C))=\\operatorname{sign}(\\tau)$ for all column-stochastic $C$.\n\\end{proposition}\n\n\\begin{proof}\n\\emph{Step~1: Bound the numerator.}",
      "numLines": 300,
      "startLine": 300,
      "totalLines": 1554
    }
  },
  "sourceToolAssistantUUID": "9ed558f4-0466-4602-b2d5-47d6f06b1e48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-25T08:23:35.410Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KhUBKxvk1yAbfzCokz1LL9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "offset": 600,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "608b8386-584e-4791-9651-59a28151017b",
  "isSidechain": false,
  "requestId": "req_011CbNxvgfugkhVtfata9pGK",
  "type": "assistant",
  "uuid": "c819400c-3d09-489f-9539-7388ef1ba5d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2ERx3NK2sp7VbE8zaEqJF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12722,
      "cache_read_input_tokens": 51801,
      "output_tokens": 1012,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1012,
          "cache_read_input_tokens": 51801,
          "cache_creation_input_tokens": 12722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12722
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-25T08:23:35.416Z_

<details><summary>↩ Tool result · `toolu_01KhUBKxvk1yAbfzCokz1LL9`</summary>

```text
600	By Cauchy--Schwarz:
601	$|\operatorname{Cov}(\mathbb{E}[g\mid A^*],\mathbb{E}[h\mid A^*])|\leq\sqrt{\operatorname{Var}(\mathbb{E}[g\mid A^*])\,\operatorname{Var}(\mathbb{E}[h\mid A^*])}$.
602	Since conditional expectation reduces variance: $\operatorname{Var}(\mathbb{E}[g\mid A^*])\leq\operatorname{Var}(g(A))$ and likewise for $h$.
603	
604	\emph{Step~2: Bound the denominator.}
605	$\mathbb{E}[\operatorname{Var}(T\mid A^*)]=\operatorname{Var}(T)-\operatorname{Var}(\mathbb{E}[T\mid A^*])\geq\operatorname{Var}(T)-\operatorname{Var}(g(A))=\mathbb{E}[\operatorname{Var}(T\mid A)]$.
606	
607	\emph{Step~3: Conclude.}
608	$|B(C)|\leq\sqrt{\operatorname{Var}(g)\,\operatorname{Var}(h)}\,/\,\mathbb{E}[\operatorname{Var}(T\mid A)]=\bar{B}_{\mathrm{col}}$.
609	When $|\tau|>\bar{B}_{\mathrm{col}}$, the bias cannot overwhelm $\tau$. In practice, $\operatorname{Var}(g(A))$ and $\operatorname{Var}(h(A))$ can be estimated from observable data by bootstrapping regression coefficients from $A^*$-stratified subsamples, yielding conservative upper bounds on $\bar{B}_{\mathrm{col}}$.
610	\end{proof}
611	
612	\paragraph{Verification for paper parameters ($K{=}3$).}
613	With $\tau{=}1.0$, $\boldsymbol{\delta}_T{=}(0,\,0.5,\,{-}0.3)$, $\boldsymbol{\delta}_Y{=}(0,\,0.8,\,0.6)$, from $5{\times}10^6$-sample Monte Carlo:
614	\begin{align*}
615	  \operatorname{Var}(g(A)) &= 0.187,\quad
616	  \operatorname{Var}(h(A)) = 0.076,\\
617	  \mathbb{E}[\operatorname{Var}(T\mid A)] &= 0.813,\\
618	  \bar{B}_{\mathrm{col}} &= \sqrt{0.187\times 0.076}\;/\;0.813\\
619	  &= 0.147.
620	\end{align*}
621	Since $|\tau|{=}1.0\gg\bar{B}_{\mathrm{col}}{=}0.147$, Proposition~\ref{prop:col_gen} guarantees sign preservation.
622	The Berkson bias $B_{\mathrm{Berkson}}{=}{-}0.114$, giving $\tau+B_{\mathrm{Berkson}}{=}0.886{>}0$.
623	Verified across $100{,}000$ random column-stochastic $C$: $\tau_{\mathrm{sign\,flip}}{=}0\%$, and $|B(C)|\leq|B_{\mathrm{Berkson}}|$ in all cases.
624	
625	\subsection{Front-door Topology ($A$ = Mediator under Confounding)}
626	\label{app:frontdoor}
627	
628	\paragraph{Data-generating process.}
629	$T\to A\to Y$, $U\to T$, $U\to Y$.
630	An unobserved confounder $U$ affects both treatment and outcome:
631	\begin{align*}
632	  U &\sim \mathcal{N}(0,1),\quad
633	  T = \alpha_U\,U + \eta,\\
634	  &\quad \eta\sim\mathcal{N}(0,1),\;\eta\perp U,\notag\\
635	  A\mid T &\sim \operatorname{Categorical}\bigl(\operatorname{softmax}(\boldsymbol{\gamma}+\boldsymbol{\delta}\,T)\bigr),\\
636	  Y &= f(A) + \lambda\,U + \varepsilon_Y,\quad \varepsilon_Y\perp(T,A,U).
637	\end{align*}
638	There is no direct $T{\to}Y$ edge; the causal effect of $T$ on $Y$ operates entirely through $A$.
639	The researcher controls for $A^*$ in $Y\sim 1+T+D_1^*+\cdots+D_{K-1}^*$.
640	
641	\paragraph{Bias decomposition.}
642	Since the direct effect is zero, the FWL coefficient on $T$ captures only bias:
643	\[
644	  \operatorname{plim}\hat\tau(C) = \frac{\mathbb{E}[\operatorname{Cov}(T,\,Y\mid A^*)]}{\mathbb{E}[\operatorname{Var}(T\mid A^*)]}.
645	\]
646	Substituting $Y=f(A)+\lambda U+\varepsilon_Y$ and using $\varepsilon_Y\perp(T,A,A^*)$:
647	\begin{align}
648	  \operatorname{plim}\hat\tau(C)
649	  &= \underbrace{\frac{\lambda\alpha_U}{\operatorname{Var}(T)}}_{\text{conf.}}
650	  + \underbrace{\frac{\mathbb{E}[\operatorname{Cov}(T,\!f(A)\mid A^*)]}{D(C)}}_{B_{\mathrm{med}}(C)}\!,
651	  \label{eq:fd_decomp}
652	\end{align}
653	where $D(C)=\mathbb{E}[\operatorname{Var}(T\mid A^*)]$.
654	
655	\begin{proof}[Derivation of~\eqref{eq:fd_decomp}]
656	Expand the numerator as
657	$\mathbb{E}[\operatorname{Cov}(T,f(A)\mid A^*)] + \lambda\,\mathbb{E}[\operatorname{Cov}(T,U\mid A^*)]$.
658	For the confounding term: since $T=\alpha_U U+\eta$ with $(U,\eta)$ jointly Gaussian, the regression residual $\xi=U-\frac{\alpha_U}{\operatorname{Var}(T)}T$ satisfies $\xi\perp T$.
659	Because $A$ is a function of $T$ (plus independent softmax noise) and $A^*$ is a function of $A$ (plus independent misclassification noise), $\xi\perp(T,A,A^*)$.
660	Therefore
661	\[
662	  \operatorname{Cov}(T,U\mid A^*\!{=}j)
663	  = \tfrac{\alpha_U}{\operatorname{Var}(T)}\operatorname{Var}(T\mid A^*\!{=}j)
664	  \;\;\forall\,j,
665	\]
666	and $\lambda\,\mathbb{E}[\operatorname{Cov}(T,U\mid A^*)]=\frac{\lambda\alpha_U}{\operatorname{Var}(T)}\,D(C)$, yielding the constant first term after division by $D(C)$.
667	\end{proof}
668	
669	This decomposition reveals that misclassification does not affect the confounding component.
670	The confusion matrix $C$ modulates only the mediation-type leakage $B_{\mathrm{med}}(C)$, which has the same structure as in~§\ref{app:mediation}.
671	
672	\paragraph{Endpoint analysis.}
673	At $C=I$: $B_{\mathrm{med}}(I)=0$ (controlling $A$ blocks the $T\to A\to Y$ path), and $\operatorname{plim}\hat\tau(I)=\lambda\alpha_U/\operatorname{Var}(T)$ (pure confounding residual).
674	
675	At $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$: $B_{\mathrm{med}}=\operatorname{Cov}(T,f(A))/\operatorname{Var}(T)$, and $\operatorname{plim}\hat\tau_{\mathrm{nc}}=[\operatorname{Cov}(T,f(A))+\lambda\alpha_U]/\operatorname{Var}(T)$, the naive regression coefficient with no controls.
676	
677	\paragraph{Numerical Verification (Front-door sign preservation).}
678	\label{find:fd_sign}
679	Since $B_{\mathrm{med}}(C)$ has the same structure as the mediation bias (§\ref{app:mediation}), interpolating between $0$ at $C{=}I$ and $\operatorname{Cov}(T,f(A))/\operatorname{Var}(T)$ at $C$ uniform. Sign preservation holds whenever the two endpoints have the same sign:
680	\[
681	  \operatorname{sign}\!\bigl(\lambda\alpha_U\bigr)
682	  = \operatorname{sign}\!\bigl(\lambda\alpha_U + \operatorname{Cov}(T,f(A))\bigr).
683	\]
684	This result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$.
685	
686	\paragraph{Verification for paper parameters ($K{=}3$).}
687	With $\alpha_U{=}1.0$, $\lambda{=}1.0$, $\boldsymbol{\beta}{=}(0,1.0,{-}0.5)$, $\boldsymbol{\gamma}{=}(0,0.5,{-}0.3)$, $\boldsymbol{\delta}{=}(0,1.0,{-}0.8)$:
688	\begin{align*}
689	  \lambda\alpha_U/\operatorname{Var}(T) &= 1.0\!\times\!1.0/2.0 = 0.500,\\
690	  \operatorname{Cov}(T,\!f(A))/\operatorname{Var}(T) &= 0.594/2.0 = 0.297.
691	\end{align*}
692	Both components are positive, so $\operatorname{plim}\hat\tau(C)\in[0.500,\,0.797]>0$ for all $C$.
693	
694	\subsection{Exposure Topology: Sign Reversal Counterexample}
695	\label{app:exposure}
696	
697	\begin{proposition}[Exposure sign reversal]
698	\label{prop:exp_counter}
699	For $K{=}3$ with $A$ as the treatment variable, there exist a marginal distribution $\mathbf{p}$, treatment effects $\boldsymbol{\beta}$, and a column-stochastic $C$ with $C_{kk}>0.5$ for all $k$, such that $\operatorname{sign}(\operatorname{plim}\hat\beta_1)\neq\operatorname{sign}(\beta_1)$.
700	\end{proposition}
701	
702	\begin{proof}[Construction]
703	Consider the exposure data-generating process (DGP) $Y = \beta_1 D_1 + \beta_2 D_2 + \varepsilon_Y$ with:
704	\begin{itemize}
705	  \item Uniform prior: $\mathbf{p}=(1/3,\,1/3,\,1/3)$.
706	  \item True effects: $\beta_1=1$,\; $\beta_2=-10$.
707	\end{itemize}
708	Choose the confusion matrix
709	\[
710	  C = \begin{pmatrix}
711	    0.60 & 0.10 & 0.10\\
712	    0.10 & 0.60 & 0.39\\
713	    0.30 & 0.30 & 0.51
714	  \end{pmatrix},
715	\]
716	with $C_{kk}\in\{0.60,\,0.60,\,0.51\}$, all ${>}\,0.5$.
717	Column sums are $1$ (verifiable by inspection).
718	
719	The OLS estimator regresses $Y$ on $(1,D_1^*,D_2^*)$.
720	The plim of $\hat\beta_j$ equals $\mathbb{E}[Y\mid A^*{=}j]-\mathbb{E}[Y\mid A^*{=}0]$, where
721	\begin{align*}
722	  \mathbb{E}[Y\mid A^*{=}j] &= \sum_{k=0}^{2} P(A{=}k\mid A^*{=}j)\,\beta_k\\
723	  &= \sum_{k=1}^{2}\frac{C_{jk}\,p_k}{q_j}\,\beta_k.
724	\end{align*}
725	
726	\emph{Marginal distribution of $A^*$:}
727	\begin{align*}
728	  q_0 &= \tfrac{1}{3}(0.60+0.10+0.10)=0.267,\\
729	  q_1 &= \tfrac{1}{3}(0.10+0.60+0.39)=0.363,\\
730	  q_2 &= \tfrac{1}{3}(0.30+0.30+0.51)=0.370.
731	\end{align*}
732	
733	\emph{Conditional means:}
734	\begin{align*}
735	  \mathbb{E}[Y\mid A^*{=}0]
736	  &= \tfrac{0.10\cdot\frac{1}{3}\cdot 1 \;+\; 0.10\cdot\frac{1}{3}\cdot({-}10)}{0.267}\\
737	  &= \tfrac{0.0333-0.3333}{0.267} = -1.125,\\[4pt]
738	  \mathbb{E}[Y\mid A^*{=}1]
739	  &= \tfrac{0.60\cdot\frac{1}{3}\cdot 1 \;+\; 0.39\cdot\frac{1}{3}\cdot({-}10)}{0.363}\\
740	  &= \tfrac{0.200-1.300}{0.363} = -3.028,\\[4pt]
741	  \mathbb{E}[Y\mid A^*{=}2]
742	  &= \tfrac{0.30\cdot\frac{1}{3}\cdot 1 \;+\; 0.51\cdot\frac{1}{3}\cdot({-}10)}{0.370}\\
743	  &= \tfrac{0.100-1.700}{0.370} = -4.324.
744	\end{align*}
745	
746	\emph{Estimated coefficient:}
747	\begin{align*}
748	  \operatorname{plim}\hat\beta_1
749	  &= \mathbb{E}[Y\mid A^*{=}1]-\mathbb{E}[Y\mid A^*{=}0]\\
750	  &= -3.028-(-1.125) = \mathbf{-1.903}.
751	\end{align*}
752	The true $\beta_1=+1>0$ but $\operatorname{plim}\hat\beta_1=-1.903<0$: \textbf{sign reversal}.
753	
754	\emph{Mechanism.}
755	The large off-diagonal entry $C_{12}=0.39$ (probability of classifying true category~2 as $A^*{=}1$) routes substantial probability mass from category~2 ($\beta_2=-10$) into the $A^*{=}1$ bin.
756	Despite $C_{11}=0.60>0.5$, the contamination from the strongly negative $\beta_2$ overwhelms the positive $\beta_1$, reversing the sign of the estimated effect for category~1.
757	This failure mode is structurally impossible at $K{=}2$: a $2{\times}2$ column-stochastic matrix with $C_{kk}>0.5$ has the form $C=\bigl(\begin{smallmatrix}a&1{-}b\\1{-}a&b\end{smallmatrix}\bigr)$ with $a,b>0.5$, and the single coefficient $\hat\beta_1$ is a positive-weighted average of $\beta_1$, preserving sign.
758	For $K{\geq}3$, the additional degrees of freedom in $C$ permit cross-contamination between categories with opposite-sign effects.
759	\end{proof}
760	
761	\subsection{Summary of Conditions}
762	\label{app:conditions}
763	
764	``Proved'' = algebraic proof via Cauchy--Schwarz (confounding) or Berkson attenuation (collider).
765	``Empirical'' = verified across 100{,}000 random column-stochastic matrices with zero violations; analytic proof for general $K$ remains open.
766	All conditions are on DGP parameters (not on $C$): once satisfied, sign preservation holds for all column-stochastic $C$ with $C_{kk}>0$.
767	
768	\begin{table}[H]
769	\centering
770	\small
771	\resizebox{\columnwidth}{!}{\begin{tabular}{lccc}
772	\toprule
773	\textbf{Topology} & \textbf{Sufficient condition} & \textbf{Status} & \textbf{Paper DGP} \\
774	\midrule
775	Confounding & $\operatorname{sign}(\tau)=\operatorname{sign}(\tau{+}B_{\mathrm{OV}})$ & Proved & $\checkmark$ ($2.0$ vs $2.3$)\\
776	Collider & $|\tau|>\bar{B}_{\mathrm{col}}$ (Prop.~\ref{prop:col_gen}) & Proved & $\checkmark$ ($1.0$ vs $0.15$)\\
777	\midrule
778	Mediation & $\operatorname{sign}(\tau_{\mathrm{dir}})=\operatorname{sign}(\tau_{\mathrm{total}})$ & Empirical & $\checkmark$ ($0.5$ vs $0.85$)\\
779	M-bias & Bias is attenuating (toward $\tau$) & Empirical & $\checkmark$ \\
780	Front-door & $\operatorname{sign}(\lambda\alpha_U)=\operatorname{sign}(\lambda\alpha_U{+}\operatorname{Cov}(T,f))$ & Empirical & $\checkmark$ ($0.50$ vs $0.80$)\\
781	\midrule
782	Exposure & Not guaranteed for $K\geq 3$ & Counterex. & See §\ref{app:exposure} \\
783	IV & Not guaranteed (denominator instability) & --- & --- \\
784	\bottomrule
785	\end{tabular}}
786	\caption{Sufficient conditions for sign preservation under non-differential misclassification.}
787	\label{tab:sign_conditions}
788	\end{table}
789	
790	\paragraph{Structural argument for M-bias topology.}
791	\emph{M-bias:} The M-structure creates a backdoor path through two latent common causes.
792	Misclassification of $A$ weakens the statistical association along this backdoor path, reducing the spurious correlation rather than amplifying it.
793	The bias therefore interpolates between the full M-bias (perfect classification, $\delta{=}0$) and zero (no classification information, $\delta{\to}\delta_{\max}$), monotonically non-increasing in $\delta$.
794	
795	\paragraph{M-bias sign-flip ASV $= \infty$.}
796	For the four covariate topologies (confounding, mediation, collider, M-bias), FWL invariance (Appendix~\ref{app:fwl}) implies that the coefficient on $T$ depends on $A^*$ only through the residualized relationship $\tilde{T} = T - \mathbb{E}[T \mid A^*]$. For M-bias, the spurious path through $A$ is the sole source of bias, and misclassification attenuates this path for all column-stochastic $C$. Since $\text{bias}(C(\delta))$ is monotonically non-increasing in $\delta$ and starts at a value with the same sign as $\tau$, no $\delta \in [0, \delta_{\max}]$ can produce a sign reversal. Therefore $\delta^*_{\text{sign}} = \infty$, which is a direct consequence of FWL invariance combined with the protective monotonicity of M-bias misclassification.
797	
798	\paragraph{Remark.}
799	The sign preservation conditions for confounding, mediation, collider, and front-door are conditions on the DGP parameters (the relative strength of the causal effect versus the confounding, indirect, or collider-induced bias), not on the confusion matrix $C$.
800	Once the condition is satisfied, sign preservation holds for all column-stochastic $C$ with $C_{kk}>0$; no diagonal-dominance restriction is needed.
801	Conversely, if the condition fails (i.e., the omitted-variable or total-effect estimate has the opposite sign from $\tau$), then there exist confusion matrices that produce sign reversal.
802	For the DGP parameters used throughout our experiments, the conditions are comfortably satisfied.
803	The sign-alignment condition is violated when the confounder has opposing effects on treatment and outcome (e.g., $\gamma_A > 0$ on $T$ but $\gamma_A < 0$ on $Y$), producing $\operatorname{sign}(\tau) \neq \operatorname{sign}(\tau_{\mathrm{OV}})$. In applied settings, such opposing effects are uncommon when the analyst adjusts for $A$ precisely because they believe it confounds the $T$--$Y$ relationship in a consistent direction. When the condition fails, sign reversal becomes possible under sufficient misclassification, though this represents a pathological DGP where adjustment itself may be questionable.
804	
805	\subsection{Adversarial Monotonicity Verification}
806	\label{app:adversarial_monotonicity}
807	
808	We test Conjecture~\ref{conj:monotone} under four adversarial confusion matrix structures designed to challenge envelope monotonicity: near-permutation ($C_0 = (1{-}\epsilon)P + \epsilon \cdot \mathbf{1}\mathbf{1}^\top/K$, $P$ a random permutation), block-diagonal (within-block confusion only), sparse (two nonzero entries per column), and near-uniform ($C_{kk} \to 1/K$). For each structure, we sweep $\delta \in [0,1]$ along $C(\delta) = (1{-}\delta)I + \delta C_0$ and measure the maximum single-step monotonicity violation $\varepsilon_{\mathrm{abs}}$.
809	
810	$N{=}1{,}000$ matrices per cell, 545{,}945 total curves were tested.
811	
812	\begin{table}[H]
813	\centering
814	\small
815	\caption{Adversarial monotonicity test across $K{=}3,5,7$ and seven topologies.}
816	\label{tab:adversarial_monotonicity}
817	\resizebox{\columnwidth}{!}{\begin{tabular}{lcc}
818	\toprule
819	\textbf{Structure} & \textbf{Non-monotone \%} & \textbf{Max $\varepsilon_{\mathrm{abs}}$} \\
820	\midrule
821	Near-permutation & 35.4\% & 0.016 \\
822	Block-diagonal & 0\% & 0 \\
823	Sparse & 2.3\% & 0.003 \\
824	Near-uniform & 0\% & 0 \\
825	\midrule
826	\textbf{All structures} & 11.9\% & \textbf{0.016} \\
827	\bottomrule
828	\end{tabular}}
829	\end{table}
830	
831	The four families span the extremes of the column-stochastic polytope: diagonal-dominant (near-identity), maximally reordered (near-permutation), degenerate (rank-deficient sparse), and block-structured heterogeneity (block-diagonal). The global maximum violation $\varepsilon_{\mathrm{abs}} = 0.016 < 0.02$ confirms that Conjecture~\ref{conj:monotone} holds under adversarial matrix structures. Near-permutation matrices with alternating-sign $\beta$ coefficients represent the most challenging case; even here, violations remain below the conjectured bound. Block-diagonal and near-uniform structures show exact monotonicity.
832	
833	\section{Supplementary Tables, Figures, and Algorithm}
834	\label{app:supplementary}
835	
836	\subsection{Binarization Collapse}
837	\label{app:binarization}
838	
839	Collapsing $K$-class annotations to binary before analysis discards multi-class error structure. We quantify ``binarization collapse'' as $\Delta = |\text{bias}_{K} - \text{bias}_{K \to 2}|$.
840	
841	For $K{=}3$, binarization introduces additional bias varying $>$150$\times$ across topologies: from $\bar{\Delta}{=}0.006$ (M-bias) to $\bar{\Delta}{=}0.926$ (IV). Exposure and IV also introduce sign flips during binarization (14\% and 17.5\%), a phenomenon absent in the other topologies (Figure~\ref{fig:binarization}).
842	
843	
844	Magnitude ASV is reported at $\tau{=}0.5$ with a 10\% threshold. Power is evaluated at $\tau{=}0.05$ significance filter. ``---'' indicates not applicable.
845	
846	\begin{table}[H]
847	\centering
848	\caption{ASV type applicability and sensitivity across DAG topologies.}
849	\label{tab:asv_grid}
850	\small
851	\resizebox{\columnwidth}{!}{\begin{tabular}{lcccl}
852	\toprule
853	\textbf{Topology} & \textbf{Mag. ASV} & \textbf{Signif.} & \textbf{Sign-flip} & \textbf{Rank} \\
854	\midrule
855	IV & 0.101--0.607 & 0\% & 1.1--6.7 & 1 (fragile) \\
856	Front-door & 0.064--0.387 & 100\% & --- & 2 \\
857	Confounding & 0.081--0.487 & 100\% & --- & 3 \\
858	Mediation & 0.076--0.454 & 0\% & --- & 4 \\
859	Collider & 0.338--2.028 & 0\% & --- & 5 \\
860	M-bias & $\infty$ & 96--100\% & --- & 6 (immune) \\
861	Exposure & --- & --- & 83.4\%$^*$ & --- \\
862	\bottomrule
863	\multicolumn{5}{l}{\scriptsize $^*$Fraction of $C_0$ with $\tau_{\text{sign\_flip}} < 1$. Exposure uses sign-flip ASV exclusively.}
864	\end{tabular}}
865	\end{table}
866	
867	
868	\begin{figure*}[ht!]
869	\centering
870	\includegraphics[width=\textwidth]{fig6_asv_heatmap.pdf}
871	\caption{ASV magnitude ranges across topologies for HumAID ($K{=}10$). Left: magnitude ASV ($\delta^*$) range across 8 LLM configurations; lower values indicate greater fragility. ``Safe'' topologies never exceed the 10\% bias threshold. Right: percentage of configurations flagged as ASV-unsafe.}
872	\label{fig:asv_heatmap}
873	\end{figure*}
874	
875	Results are averaged across 6 error structures with $N_{\text{sim}}{=}1{,}000$. Positive values indicate reduced RMSE; negative values indicate increased RMSE. Naive/MLA show 0.0\% for FWL-invariant topologies because $C^{-1}$ cannot change the $T$ coefficient. \textbf{Bold}: best method per topology; \underline{underline}: best gold-free method.
876	
877	\begin{table}[H]
878	\centering
879	\caption{RMSE reduction (\%) by correction method and DAG topology.}
880	\label{tab:correction}
881	\resizebox{\columnwidth}{!}{\begin{tabular}{lccccc}
882	\toprule
883	\textbf{Topology} & \textbf{Naive} & \textbf{MLA} & \textbf{DSL} & \textbf{SIMEX} & \textbf{PPI++} \\
884	\midrule
885	Confounding & 0.0 & 0.0 & \underline{48.0} & 35.1 & \textbf{83.2} \\
886	Mediation & 0.0 & 0.0 & \underline{52.9} & 39.1 & \textbf{54.1} \\
887	Collider & 0.0 & 0.0 & $-$92.6 & \underline{31.8} & \textbf{50.5} \\
888	M-bias & 0.0 & 0.0 & $-$267 & \textbf{\underline{0.1}} & $-$88.0 \\
889	\midrule
890	Front-door & $-$52.7 & $-$111.5 & \underline{$-$29.0} & $-$62.4 & \textbf{74.1} \\
891	Exposure & $-$44.8 & $-$89.0 & $-$59.5 & \underline{$-$9.8} & \textbf{75.5} \\
892	IV & $-$40.4 & $-$58.7 & $-$206.1 & \underline{59.4} & \textbf{79.4} \\
893	\midrule
894	Grand mean & $-$19.7 & $-$37.0 & $-$79.0 & 13.3 & \textbf{47.0} \\
895	\bottomrule
896	\end{tabular}}
897	\end{table}
898	
899	\paragraph{Error structures used in correction experiments.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c819400c-3d09-489f-9539-7388ef1ba5d1",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "a2401756-1215-4285-aadb-85b7782e01f3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
      "content": "By Cauchy--Schwarz:\n$|\\operatorname{Cov}(\\mathbb{E}[g\\mid A^*],\\mathbb{E}[h\\mid A^*])|\\leq\\sqrt{\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])\\,\\operatorname{Var}(\\mathbb{E}[h\\mid A^*])}$.\nSince conditional expectation reduces variance: $\\operatorname{Var}(\\mathbb{E}[g\\mid A^*])\\leq\\operatorname{Var}(g(A))$ and likewise for $h$.\n\n\\emph{Step~2: Bound the denominator.}\n$\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]=\\operatorname{Var}(T)-\\operatorname{Var}(\\mathbb{E}[T\\mid A^*])\\geq\\operatorname{Var}(T)-\\operatorname{Var}(g(A))=\\mathbb{E}[\\operatorname{Var}(T\\mid A)]$.\n\n\\emph{Step~3: Conclude.}\n$|B(C)|\\leq\\sqrt{\\operatorname{Var}(g)\\,\\operatorname{Var}(h)}\\,/\\,\\mathbb{E}[\\operatorname{Var}(T\\mid A)]=\\bar{B}_{\\mathrm{col}}$.\nWhen $|\\tau|>\\bar{B}_{\\mathrm{col}}$, the bias cannot overwhelm $\\tau$. In practice, $\\operatorname{Var}(g(A))$ and $\\operatorname{Var}(h(A))$ can be estimated from observable data by bootstrapping regression coefficients from $A^*$-stratified subsamples, yielding conservative upper bounds on $\\bar{B}_{\\mathrm{col}}$.\n\\end{proof}\n\n\\paragraph{Verification for paper parameters ($K{=}3$).}\nWith $\\tau{=}1.0$, $\\boldsymbol{\\delta}_T{=}(0,\\,0.5,\\,{-}0.3)$, $\\boldsymbol{\\delta}_Y{=}(0,\\,0.8,\\,0.6)$, from $5{\\times}10^6$-sample Monte Carlo:\n\\begin{align*}\n  \\operatorname{Var}(g(A)) &= 0.187,\\quad\n  \\operatorname{Var}(h(A)) = 0.076,\\\\\n  \\mathbb{E}[\\operatorname{Var}(T\\mid A)] &= 0.813,\\\\\n  \\bar{B}_{\\mathrm{col}} &= \\sqrt{0.187\\times 0.076}\\;/\\;0.813\\\\\n  &= 0.147.\n\\end{align*}\nSince $|\\tau|{=}1.0\\gg\\bar{B}_{\\mathrm{col}}{=}0.147$, Proposition~\\ref{prop:col_gen} guarantees sign preservation.\nThe Berkson bias $B_{\\mathrm{Berkson}}{=}{-}0.114$, giving $\\tau+B_{\\mathrm{Berkson}}{=}0.886{>}0$.\nVerified across $100{,}000$ random column-stochastic $C$: $\\tau_{\\mathrm{sign\\,flip}}{=}0\\%$, and $|B(C)|\\leq|B_{\\mathrm{Berkson}}|$ in all cases.\n\n\\subsection{Front-door Topology ($A$ = Mediator under Confounding)}\n\\label{app:frontdoor}\n\n\\paragraph{Data-generating process.}\n$T\\to A\\to Y$, $U\\to T$, $U\\to Y$.\nAn unobserved confounder $U$ affects both treatment and outcome:\n\\begin{align*}\n  U &\\sim \\mathcal{N}(0,1),\\quad\n  T = \\alpha_U\\,U + \\eta,\\\\\n  &\\quad \\eta\\sim\\mathcal{N}(0,1),\\;\\eta\\perp U,\\notag\\\\\n  A\\mid T &\\sim \\operatorname{Categorical}\\bigl(\\operatorname{softmax}(\\boldsymbol{\\gamma}+\\boldsymbol{\\delta}\\,T)\\bigr),\\\\\n  Y &= f(A) + \\lambda\\,U + \\varepsilon_Y,\\quad \\varepsilon_Y\\perp(T,A,U).\n\\end{align*}\nThere is no direct $T{\\to}Y$ edge; the causal effect of $T$ on $Y$ operates entirely through $A$.\nThe researcher controls for $A^*$ in $Y\\sim 1+T+D_1^*+\\cdots+D_{K-1}^*$.\n\n\\paragraph{Bias decomposition.}\nSince the direct effect is zero, the FWL coefficient on $T$ captures only bias:\n\\[\n  \\operatorname{plim}\\hat\\tau(C) = \\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\,Y\\mid A^*)]}{\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]}.\n\\]\nSubstituting $Y=f(A)+\\lambda U+\\varepsilon_Y$ and using $\\varepsilon_Y\\perp(T,A,A^*)$:\n\\begin{align}\n  \\operatorname{plim}\\hat\\tau(C)\n  &= \\underbrace{\\frac{\\lambda\\alpha_U}{\\operatorname{Var}(T)}}_{\\text{conf.}}\n  + \\underbrace{\\frac{\\mathbb{E}[\\operatorname{Cov}(T,\\!f(A)\\mid A^*)]}{D(C)}}_{B_{\\mathrm{med}}(C)}\\!,\n  \\label{eq:fd_decomp}\n\\end{align}\nwhere $D(C)=\\mathbb{E}[\\operatorname{Var}(T\\mid A^*)]$.\n\n\\begin{proof}[Derivation of~\\eqref{eq:fd_decomp}]\nExpand the numerator as\n$\\mathbb{E}[\\operatorname{Cov}(T,f(A)\\mid A^*)] + \\lambda\\,\\mathbb{E}[\\operatorname{Cov}(T,U\\mid A^*)]$.\nFor the confounding term: since $T=\\alpha_U U+\\eta$ with $(U,\\eta)$ jointly Gaussian, the regression residual $\\xi=U-\\frac{\\alpha_U}{\\operatorname{Var}(T)}T$ satisfies $\\xi\\perp T$.\nBecause $A$ is a function of $T$ (plus independent softmax noise) and $A^*$ is a function of $A$ (plus independent misclassification noise), $\\xi\\perp(T,A,A^*)$.\nTherefore\n\\[\n  \\operatorname{Cov}(T,U\\mid A^*\\!{=}j)\n  = \\tfrac{\\alpha_U}{\\operatorname{Var}(T)}\\operatorname{Var}(T\\mid A^*\\!{=}j)\n  \\;\\;\\forall\\,j,\n\\]\nand $\\lambda\\,\\mathbb{E}[\\operatorname{Cov}(T,U\\mid A^*)]=\\frac{\\lambda\\alpha_U}{\\operatorname{Var}(T)}\\,D(C)$, yielding the constant first term after division by $D(C)$.\n\\end{proof}\n\nThis decomposition reveals that misclassification does not affect the confounding component.\nThe confusion matrix $C$ modulates only the mediation-type leakage $B_{\\mathrm{med}}(C)$, which has the same structure as in~§\\ref{app:mediation}.\n\n\\paragraph{Endpoint analysis.}\nAt $C=I$: $B_{\\mathrm{med}}(I)=0$ (controlling $A$ blocks the $T\\to A\\to Y$ path), and $\\operatorname{plim}\\hat\\tau(I)=\\lambda\\alpha_U/\\operatorname{Var}(T)$ (pure confounding residual).\n\nAt $C=\\frac{1}{K}\\mathbf{1}\\mathbf{1}^\\top$: $B_{\\mathrm{med}}=\\operatorname{Cov}(T,f(A))/\\operatorname{Var}(T)$, and $\\operatorname{plim}\\hat\\tau_{\\mathrm{nc}}=[\\operatorname{Cov}(T,f(A))+\\lambda\\alpha_U]/\\operatorname{Var}(T)$, the naive regression coefficient with no controls.\n\n\\paragraph{Numerical Verification (Front-door sign preservation).}\n\\label{find:fd_sign}\nSince $B_{\\mathrm{med}}(C)$ has the same structure as the mediation bias (§\\ref{app:mediation}), interpolating between $0$ at $C{=}I$ and $\\operatorname{Cov}(T,f(A))/\\operatorname{Var}(T)$ at $C$ uniform. Sign preservation holds whenever the two endpoints have the same sign:\n\\[\n  \\operatorname{sign}\\!\\bigl(\\lambda\\alpha_U\\bigr)\n  = \\operatorname{sign}\\!\\bigl(\\lambda\\alpha_U + \\operatorname{Cov}(T,f(A))\\bigr).\n\\]\nThis result is verified numerically for $100{,}000$ independently sampled column-stochastic matrices $C$.\n\n\\paragraph{Verification for paper parameters ($K{=}3$).}\nWith $\\alpha_U{=}1.0$, $\\lambda{=}1.0$, $\\boldsymbol{\\beta}{=}(0,1.0,{-}0.5)$, $\\boldsymbol{\\gamma}{=}(0,0.5,{-}0.3)$, $\\boldsymbol{\\delta}{=}(0,1.0,{-}0.8)$:\n\\begin{align*}\n  \\lambda\\alpha_U/\\operatorname{Var}(T) &= 1.0\\!\\times\\!1.0/2.0 = 0.500,\\\\\n  \\operatorname{Cov}(T,\\!f(A))/\\operatorname{Var}(T) &= 0.594/2.0 = 0.297.\n\\end{align*}\nBoth components are positive, so $\\operatorname{plim}\\hat\\tau(C)\\in[0.500,\\,0.797]>0$ for all $C$.\n\n\\subsection{Exposure Topology: Sign Reversal Counterexample}\n\\label{app:exposure}\n\n\\begin{proposition}[Exposure sign reversal]\n\\label{prop:exp_counter}\nFor $K{=}3$ with $A$ as the treatment variable, there exist a marginal distribution $\\mathbf{p}$, treatment effects $\\boldsymbol{\\beta}$, and a column-stochastic $C$ with $C_{kk}>0.5$ for all $k$, such that $\\operatorname{sign}(\\operatorname{plim}\\hat\\beta_1)\\neq\\operatorname{sign}(\\beta_1)$.\n\\end{proposition}\n\n\\begin{proof}[Construction]\nConsider the exposure data-generating process (DGP) $Y = \\beta_1 D_1 + \\beta_2 D_2 + \\varepsilon_Y$ with:\n\\begin{itemize}\n  \\item Uniform prior: $\\mathbf{p}=(1/3,\\,1/3,\\,1/3)$.\n  \\item True effects: $\\beta_1=1$,\\; $\\beta_2=-10$.\n\\end{itemize}\nChoose the confusion matrix\n\\[\n  C = \\begin{pmatrix}\n    0.60 & 0.10 & 0.10\\\\\n    0.10 & 0.60 & 0.39\\\\\n    0.30 & 0.30 & 0.51\n  \\end{pmatrix},\n\\]\nwith $C_{kk}\\in\\{0.60,\\,0.60,\\,0.51\\}$, all ${>}\\,0.5$.\nColumn sums are $1$ (verifiable by inspection).\n\nThe OLS estimator regresses $Y$ on $(1,D_1^*,D_2^*)$.\nThe plim of $\\hat\\beta_j$ equals $\\mathbb{E}[Y\\mid A^*{=}j]-\\mathbb{E}[Y\\mid A^*{=}0]$, where\n\\begin{align*}\n  \\mathbb{E}[Y\\mid A^*{=}j] &= \\sum_{k=0}^{2} P(A{=}k\\mid A^*{=}j)\\,\\beta_k\\\\\n  &= \\sum_{k=1}^{2}\\frac{C_{jk}\\,p_k}{q_j}\\,\\beta_k.\n\\end{align*}\n\n\\emph{Marginal distribution of $A^*$:}\n\\begin{align*}\n  q_0 &= \\tfrac{1}{3}(0.60+0.10+0.10)=0.267,\\\\\n  q_1 &= \\tfrac{1}{3}(0.10+0.60+0.39)=0.363,\\\\\n  q_2 &= \\tfrac{1}{3}(0.30+0.30+0.51)=0.370.\n\\end{align*}\n\n\\emph{Conditional means:}\n\\begin{align*}\n  \\mathbb{E}[Y\\mid A^*{=}0]\n  &= \\tfrac{0.10\\cdot\\frac{1}{3}\\cdot 1 \\;+\\; 0.10\\cdot\\frac{1}{3}\\cdot({-}10)}{0.267}\\\\\n  &= \\tfrac{0.0333-0.3333}{0.267} = -1.125,\\\\[4pt]\n  \\mathbb{E}[Y\\mid A^*{=}1]\n  &= \\tfrac{0.60\\cdot\\frac{1}{3}\\cdot 1 \\;+\\; 0.39\\cdot\\frac{1}{3}\\cdot({-}10)}{0.363}\\\\\n  &= \\tfrac{0.200-1.300}{0.363} = -3.028,\\\\[4pt]\n  \\mathbb{E}[Y\\mid A^*{=}2]\n  &= \\tfrac{0.30\\cdot\\frac{1}{3}\\cdot 1 \\;+\\; 0.51\\cdot\\frac{1}{3}\\cdot({-}10)}{0.370}\\\\\n  &= \\tfrac{0.100-1.700}{0.370} = -4.324.\n\\end{align*}\n\n\\emph{Estimated coefficient:}\n\\begin{align*}\n  \\operatorname{plim}\\hat\\beta_1\n  &= \\mathbb{E}[Y\\mid A^*{=}1]-\\mathbb{E}[Y\\mid A^*{=}0]\\\\\n  &= -3.028-(-1.125) = \\mathbf{-1.903}.\n\\end{align*}\nThe true $\\beta_1=+1>0$ but $\\operatorname{plim}\\hat\\beta_1=-1.903<0$: \\textbf{sign reversal}.\n\n\\emph{Mechanism.}\nThe large off-diagonal entry $C_{12}=0.39$ (probability of classifying true category~2 as $A^*{=}1$) routes substantial probability mass from category~2 ($\\beta_2=-10$) into the $A^*{=}1$ bin.\nDespite $C_{11}=0.60>0.5$, the contamination from the strongly negative $\\beta_2$ overwhelms the positive $\\beta_1$, reversing the sign of the estimated effect for category~1.\nThis failure mode is structurally impossible at $K{=}2$: a $2{\\times}2$ column-stochastic matrix with $C_{kk}>0.5$ has the form $C=\\bigl(\\begin{smallmatrix}a&1{-}b\\\\1{-}a&b\\end{smallmatrix}\\bigr)$ with $a,b>0.5$, and the single coefficient $\\hat\\beta_1$ is a positive-weighted average of $\\beta_1$, preserving sign.\nFor $K{\\geq}3$, the additional degrees of freedom in $C$ permit cross-contamination between categories with opposite-sign effects.\n\\end{proof}\n\n\\subsection{Summary of Conditions}\n\\label{app:conditions}\n\n``Proved'' = algebraic proof via Cauchy--Schwarz (confounding) or Berkson attenuation (collider).\n``Empirical'' = verified across 100{,}000 random column-stochastic matrices with zero violations; analytic proof for general $K$ remains open.\nAll conditions are on DGP parameters (not on $C$): once satisfied, sign preservation holds for all column-stochastic $C$ with $C_{kk}>0$.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Topology} & \\textbf{Sufficient condition} & \\textbf{Status} & \\textbf{Paper DGP} \\\\\n\\midrule\nConfounding & $\\operatorname{sign}(\\tau)=\\operatorname{sign}(\\tau{+}B_{\\mathrm{OV}})$ & Proved & $\\checkmark$ ($2.0$ vs $2.3$)\\\\\nCollider & $|\\tau|>\\bar{B}_{\\mathrm{col}}$ (Prop.~\\ref{prop:col_gen}) & Proved & $\\checkmark$ ($1.0$ vs $0.15$)\\\\\n\\midrule\nMediation & $\\operatorname{sign}(\\tau_{\\mathrm{dir}})=\\operatorname{sign}(\\tau_{\\mathrm{total}})$ & Empirical & $\\checkmark$ ($0.5$ vs $0.85$)\\\\\nM-bias & Bias is attenuating (toward $\\tau$) & Empirical & $\\checkmark$ \\\\\nFront-door & $\\operatorname{sign}(\\lambda\\alpha_U)=\\operatorname{sign}(\\lambda\\alpha_U{+}\\operatorname{Cov}(T,f))$ & Empirical & $\\checkmark$ ($0.50$ vs $0.80$)\\\\\n\\midrule\nExposure & Not guaranteed for $K\\geq 3$ & Counterex. & See §\\ref{app:exposure} \\\\\nIV & Not guaranteed (denominator instability) & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Sufficient conditions for sign preservation under non-differential misclassification.}\n\\label{tab:sign_conditions}\n\\end{table}\n\n\\paragraph{Structural argument for M-bias topology.}\n\\emph{M-bias:} The M-structure creates a backdoor path through two latent common causes.\nMisclassification of $A$ weakens the statistical association along this backdoor path, reducing the spurious correlation rather than amplifying it.\nThe bias therefore interpolates between the full M-bias (perfect classification, $\\delta{=}0$) and zero (no classification information, $\\delta{\\to}\\delta_{\\max}$), monotonically non-increasing in $\\delta$.\n\n\\paragraph{M-bias sign-flip ASV $= \\infty$.}\nFor the four covariate topologies (confounding, mediation, collider, M-bias), FWL invariance (Appendix~\\ref{app:fwl}) implies that the coefficient on $T$ depends on $A^*$ only through the residualized relationship $\\tilde{T} = T - \\mathbb{E}[T \\mid A^*]$. For M-bias, the spurious path through $A$ is the sole source of bias, and misclassification attenuates this path for all column-stochastic $C$. Since $\\text{bias}(C(\\delta))$ is monotonically non-increasing in $\\delta$ and starts at a value with the same sign as $\\tau$, no $\\delta \\in [0, \\delta_{\\max}]$ can produce a sign reversal. Therefore $\\delta^*_{\\text{sign}} = \\infty$, which is a direct consequence of FWL invariance combined with the protective monotonicity of M-bias misclassification.\n\n\\paragraph{Remark.}\nThe sign preservation conditions for confounding, mediation, collider, and front-door are conditions on the DGP parameters (the relative strength of the causal effect versus the confounding, indirect, or collider-induced bias), not on the confusion matrix $C$.\nOnce the condition is satisfied, sign preservation holds for all column-stochastic $C$ with $C_{kk}>0$; no diagonal-dominance restriction is needed.\nConversely, if the condition fails (i.e., the omitted-variable or total-effect estimate has the opposite sign from $\\tau$), then there exist confusion matrices that produce sign reversal.\nFor the DGP parameters used throughout our experiments, the conditions are comfortably satisfied.\nThe sign-alignment condition is violated when the confounder has opposing effects on treatment and outcome (e.g., $\\gamma_A > 0$ on $T$ but $\\gamma_A < 0$ on $Y$), producing $\\operatorname{sign}(\\tau) \\neq \\operatorname{sign}(\\tau_{\\mathrm{OV}})$. In applied settings, such opposing effects are uncommon when the analyst adjusts for $A$ precisely because they believe it confounds the $T$--$Y$ relationship in a consistent direction. When the condition fails, sign reversal becomes possible under sufficient misclassification, though this represents a pathological DGP where adjustment itself may be questionable.\n\n\\subsection{Adversarial Monotonicity Verification}\n\\label{app:adversarial_monotonicity}\n\nWe test Conjecture~\\ref{conj:monotone} under four adversarial confusion matrix structures designed to challenge envelope monotonicity: near-permutation ($C_0 = (1{-}\\epsilon)P + \\epsilon \\cdot \\mathbf{1}\\mathbf{1}^\\top/K$, $P$ a random permutation), block-diagonal (within-block confusion only), sparse (two nonzero entries per column), and near-uniform ($C_{kk} \\to 1/K$). For each structure, we sweep $\\delta \\in [0,1]$ along $C(\\delta) = (1{-}\\delta)I + \\delta C_0$ and measure the maximum single-step monotonicity violation $\\varepsilon_{\\mathrm{abs}}$.\n\n$N{=}1{,}000$ matrices per cell, 545{,}945 total curves were tested.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\caption{Adversarial monotonicity test across $K{=}3,5,7$ and seven topologies.}\n\\label{tab:adversarial_monotonicity}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Structure} & \\textbf{Non-monotone \\%} & \\textbf{Max $\\varepsilon_{\\mathrm{abs}}$} \\\\\n\\midrule\nNear-permutation & 35.4\\% & 0.016 \\\\\nBlock-diagonal & 0\\% & 0 \\\\\nSparse & 2.3\\% & 0.003 \\\\\nNear-uniform & 0\\% & 0 \\\\\n\\midrule\n\\textbf{All structures} & 11.9\\% & \\textbf{0.016} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe four families span the extremes of the column-stochastic polytope: diagonal-dominant (near-identity), maximally reordered (near-permutation), degenerate (rank-deficient sparse), and block-structured heterogeneity (block-diagonal). The global maximum violation $\\varepsilon_{\\mathrm{abs}} = 0.016 < 0.02$ confirms that Conjecture~\\ref{conj:monotone} holds under adversarial matrix structures. Near-permutation matrices with alternating-sign $\\beta$ coefficients represent the most challenging case; even here, violations remain below the conjectured bound. Block-diagonal and near-uniform structures show exact monotonicity.\n\n\\section{Supplementary Tables, Figures, and Algorithm}\n\\label{app:supplementary}\n\n\\subsection{Binarization Collapse}\n\\label{app:binarization}\n\nCollapsing $K$-class annotations to binary before analysis discards multi-class error structure. We quantify ``binarization collapse'' as $\\Delta = |\\text{bias}_{K} - \\text{bias}_{K \\to 2}|$.\n\nFor $K{=}3$, binarization introduces additional bias varying $>$150$\\times$ across topologies: from $\\bar{\\Delta}{=}0.006$ (M-bias) to $\\bar{\\Delta}{=}0.926$ (IV). Exposure and IV also introduce sign flips during binarization (14\\% and 17.5\\%), a phenomenon absent in the other topologies (Figure~\\ref{fig:binarization}).\n\n\nMagnitude ASV is reported at $\\tau{=}0.5$ with a 10\\% threshold. Power is evaluated at $\\tau{=}0.05$ significance filter. ``---'' indicates not applicable.\n\n\\begin{table}[H]\n\\centering\n\\caption{ASV type applicability and sensitivity across DAG topologies.}\n\\label{tab:asv_grid}\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Topology} & \\textbf{Mag. ASV} & \\textbf{Signif.} & \\textbf{Sign-flip} & \\textbf{Rank} \\\\\n\\midrule\nIV & 0.101--0.607 & 0\\% & 1.1--6.7 & 1 (fragile) \\\\\nFront-door & 0.064--0.387 & 100\\% & --- & 2 \\\\\nConfounding & 0.081--0.487 & 100\\% & --- & 3 \\\\\nMediation & 0.076--0.454 & 0\\% & --- & 4 \\\\\nCollider & 0.338--2.028 & 0\\% & --- & 5 \\\\\nM-bias & $\\infty$ & 96--100\\% & --- & 6 (immune) \\\\\nExposure & --- & --- & 83.4\\%$^*$ & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\scriptsize $^*$Fraction of $C_0$ with $\\tau_{\\text{sign\\_flip}} < 1$. Exposure uses sign-flip ASV exclusively.}\n\\end{tabular}}\n\\end{table}\n\n\n\\begin{figure*}[ht!]\n\\centering\n\\includegraphics[width=\\textwidth]{fig6_asv_heatmap.pdf}\n\\caption{ASV magnitude ranges across topologies for HumAID ($K{=}10$). Left: magnitude ASV ($\\delta^*$) range across 8 LLM configurations; lower values indicate greater fragility. ``Safe'' topologies never exceed the 10\\% bias threshold. Right: percentage of configurations flagged as ASV-unsafe.}\n\\label{fig:asv_heatmap}\n\\end{figure*}\n\nResults are averaged across 6 error structures with $N_{\\text{sim}}{=}1{,}000$. Positive values indicate reduced RMSE; negative values indicate increased RMSE. Naive/MLA show 0.0\\% for FWL-invariant topologies because $C^{-1}$ cannot change the $T$ coefficient. \\textbf{Bold}: best method per topology; \\underline{underline}: best gold-free method.\n\n\\begin{table}[H]\n\\centering\n\\caption{RMSE reduction (\\%) by correction method and DAG topology.}\n\\label{tab:correction}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Topology} & \\textbf{Naive} & \\textbf{MLA} & \\textbf{DSL} & \\textbf{SIMEX} & \\textbf{PPI++} \\\\\n\\midrule\nConfounding & 0.0 & 0.0 & \\underline{48.0} & 35.1 & \\textbf{83.2} \\\\\nMediation & 0.0 & 0.0 & \\underline{52.9} & 39.1 & \\textbf{54.1} \\\\\nCollider & 0.0 & 0.0 & $-$92.6 & \\underline{31.8} & \\textbf{50.5} \\\\\nM-bias & 0.0 & 0.0 & $-$267 & \\textbf{\\underline{0.1}} & $-$88.0 \\\\\n\\midrule\nFront-door & $-$52.7 & $-$111.5 & \\underline{$-$29.0} & $-$62.4 & \\textbf{74.1} \\\\\nExposure & $-$44.8 & $-$89.0 & $-$59.5 & \\underline{$-$9.8} & \\textbf{75.5} \\\\\nIV & $-$40.4 & $-$58.7 & $-$206.1 & \\underline{59.4} & \\textbf{79.4} \\\\\n\\midrule\nGrand mean & $-$19.7 & $-$37.0 & $-$79.0 & 13.3 & \\textbf{47.0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Error structures used in correction experiments.}",
      "numLines": 300,
      "startLine": 600,
      "totalLines": 1554
    }
  },
  "sourceToolAssistantUUID": "c819400c-3d09-489f-9539-7388ef1ba5d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-25T08:23:36.417Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01BrGU8TQGVUcr5LnmnsAvkf`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2401756-1215-4285-aadb-85b7782e01f3",
  "isSidechain": false,
  "requestId": "req_011CbNxvgfugkhVtfata9pGK",
  "type": "assistant",
  "uuid": "79f5a9be-e57f-4ecc-9cd7-99ebc8367cdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2ERx3NK2sp7VbE8zaEqJF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12722,
      "cache_read_input_tokens": 51801,
      "output_tokens": 1012,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1012,
          "cache_read_input_tokens": 51801,
          "cache_creation_input_tokens": 12722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12722
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-25T08:23:36.450Z_

<details><summary>↩ Tool result · `toolu_01BrGU8TQGVUcr5LnmnsAvkf`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79f5a9be-e57f-4ecc-9cd7-99ebc8367cdf",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "335d9d22-06a1-48ff-80ad-e3651e66c2e9",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "79f5a9be-e57f-4ecc-9cd7-99ebc8367cdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-25T08:23:37.361Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LGcZ9Nm1HwDtEDCnXZHbpA`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "335d9d22-06a1-48ff-80ad-e3651e66c2e9",
  "isSidechain": false,
  "requestId": "req_011CbNxvgfugkhVtfata9pGK",
  "type": "assistant",
  "uuid": "75659dca-257e-4be6-a18e-dc8eab0d54fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2ERx3NK2sp7VbE8zaEqJF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12722,
      "cache_read_input_tokens": 51801,
      "output_tokens": 1012,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1012,
          "cache_read_input_tokens": 51801,
          "cache_creation_input_tokens": 12722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12722
          },
          "type": "message"
        }
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

_source line 51 · 2026-05-25T08:23:37.374Z_

<details><summary>↩ Tool result · `toolu_01LGcZ9Nm1HwDtEDCnXZHbpA`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75659dca-257e-4be6-a18e-dc8eab0d54fe",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "71fdca1f-5610-4489-a9a0-a37e9fe0f995",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "75659dca-257e-4be6-a18e-dc8eab0d54fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-25T08:23:39.243Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01TzNnVq5GXQW1xjybC19UjW`</summary>

```json
{
  "pattern": "ing,|ing\\.|ing\\s+the\\s+(applicability|effectiveness|importance|significance|robustness|utility)",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71fdca1f-5610-4489-a9a0-a37e9fe0f995",
  "isSidechain": false,
  "requestId": "req_011CbNxvgfugkhVtfata9pGK",
  "type": "assistant",
  "uuid": "816bd0a3-3b9e-4bab-a2c0-ed2acc651d34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2ERx3NK2sp7VbE8zaEqJF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12722,
      "cache_read_input_tokens": 51801,
      "output_tokens": 1012,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1012,
          "cache_read_input_tokens": 51801,
          "cache_creation_input_tokens": 12722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12722
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-25T08:23:39.258Z_

<details><summary>↩ Tool result · `toolu_01TzNnVq5GXQW1xjybC19UjW`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex:11:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex:21:Five topologies exhibit zero sign-flip rate (Table~\ref{tab:taxonomy}): confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse the sign; collider is protective ($|B(C)|$ non-increasing; Conjecture~\ref{conj:monotone}); M-bias shows weakest sensitivity (53.2\% violation). All patterns persist at $K{=}5,7$ (Appendix~\ref{sec:cross_k_robustness}).
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex:86:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex:109:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex:47:\caption{Seven canonical DAG topologies with starred-node annotation~\cite{hernan_cole2009}. $A$ (latent) $\to$ $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies: treatment (exposure), covariate (confounding, mediation, M-bias, front-door), selection (collider), instrument (IV).}
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex:17:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex:26:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex:81:\includegraphics[width=\textwidth]{fig3_asv_ranking.pdf}
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex:105:For $K{=}3$ with symmetric confusion matrix $C_{jk} = c$ for $j \neq k$ and $C_{kk} = 1{-}2c$, $c \in (0, 1/3)$, and proportional effects ($f{=}\lambda g$), envelope monotonicity holds exactly: $|B(C(\delta))|$ is strictly monotone in $\delta$ for confounding, mediation, and collider topologies whenever $\mathrm{Var}(g) > 0$.
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/k3_symmetric_proof.tex:89:is strictly non-decreasing.
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/k3_symmetric_proof.tex:96:The same argument yields $|B|$ strictly non-decreasing.
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:23:For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:299:Since $V_B$ is convex (Step~1), its derivative $V_B'$ is non-decreasing.
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:300:When $V_B'(1)\leq 0$, we have $V_B'(\delta)\leq V_B'(1)\leq 0$ for all $\delta\in[0,1]$, so $V_B$ is non-increasing.
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:302:\emph{Step 6: $|B(\delta)|$ is non-decreasing.}
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:305:Hence $|B(\delta)|=h(V_W(\delta))$ is non-decreasing. \qed
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:315:By the same convexity argument, each $\mathbb{E}[\operatorname{Var}(\cdot\mid A^*_\delta)]$ is non-decreasing in $\delta$, and $D(\delta)=\mathbb{E}[\operatorname{Var}(T\mid A^*_\delta)]$ is non-decreasing.
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:449:Since $h(x)=|\lambda|x/(x+\sigma_\varepsilon^2)$ is increasing, $|B(C(\delta))|$ is non-decreasing.
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:544:Unlike confounding, $\varepsilon_Y$ is not independent of $A$ (since $A$ depends on $Y=\tau T+\varepsilon_Y$), so Lemma~\ref{lem:bias_decomp} does not apply directly.
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:796:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:799:The sign preservation conditions for confounding, mediation, collider, and front-door are conditions on the DGP parameters (the relative strength of the causal effect versus the confounding, indirect, or collider-induced bias), not on the confusion matrix $C$.
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:937:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:1118:For HumAID ($K{=}10$, 56 scenarios), 55.4\% are flagged as magnitude-ASV-unsafe: IV, mediation, front-door, and exposure all trigger, while confounding, collider, and M-bias remain below 10\% bias (Figure~\ref{fig:asv_heatmap}). For CivilComments ($K{=}2$), 100\% of scenarios are ASV-unsafe despite $F_1$ ranging from $0.69$ (7B) to $0.82$ (frontier).
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:1159:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:1162:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:1221:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:1364:Spearman rank correlations across all topology--method pairs: $\rho_{3,5} = 0.80$, $\rho_{3,10} = 0.84$, $\rho_{5,10} = 0.93$ (all $p < 10^{-8}$). Per-topology correlations are even stronger: 5 of 7 topologies (confounding, collider, M-bias, IV, and exposure at $K{=}10$) achieve $\rho = 1.0$ between $K{=}3$ and $K{=}10$.
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:1445:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:1549:    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex:17:\item \textbf{Topology-aware correction routing.} Frisch--Waugh--Lovell (FWL) invariance renders matrix-based corrections provably ineffective for four covariate topologies. We evaluate five correction methods and provide a topology-aware decision procedure (Algorithm~\ref{alg:correction}, Appendix), validated with real LLM confusion matrices.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "816bd0a3-3b9e-4bab-a2c0-ed2acc651d34",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "c3cd5a8f-0fa3-4485-94d7-c151cdf73f4a",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex:8:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex:11:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex:21:Five topologies exhibit zero sign-flip rate (Table~\\ref{tab:taxonomy}): confounding, mediation, and front-door show 100\\% amplification~\\cite{brenner1993, dosemeci1990} but never reverse the sign; collider is protective ($|B(C)|$ non-increasing; Conjecture~\\ref{conj:monotone}); M-bias shows weakest sensitivity (53.2\\% violation). All patterns persist at $K{=}5,7$ (Appendix~\\ref{sec:cross_k_robustness}).\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex:86:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex:109:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex:47:\\caption{Seven canonical DAG topologies with starred-node annotation~\\cite{hernan_cole2009}. $A$ (latent) $\\to$ $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies: treatment (exposure), covariate (confounding, mediation, M-bias, front-door), selection (collider), instrument (IV).}\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex:10:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex:17:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex:26:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex:81:\\includegraphics[width=\\textwidth]{fig3_asv_ranking.pdf}\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex:105:For $K{=}3$ with symmetric confusion matrix $C_{jk} = c$ for $j \\neq k$ and $C_{kk} = 1{-}2c$, $c \\in (0, 1/3)$, and proportional effects ($f{=}\\lambda g$), envelope monotonicity holds exactly: $|B(C(\\delta))|$ is strictly monotone in $\\delta$ for confounding, mediation, and collider topologies whenever $\\mathrm{Var}(g) > 0$.\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/k3_symmetric_proof.tex:89:is strictly non-decreasing.\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/k3_symmetric_proof.tex:96:The same argument yields $|B|$ strictly non-decreasing.\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:23:For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\\dots,D_{K-1}^*)$.\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:299:Since $V_B$ is convex (Step~1), its derivative $V_B'$ is non-decreasing.\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:300:When $V_B'(1)\\leq 0$, we have $V_B'(\\delta)\\leq V_B'(1)\\leq 0$ for all $\\delta\\in[0,1]$, so $V_B$ is non-increasing.\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:302:\\emph{Step 6: $|B(\\delta)|$ is non-decreasing.}\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:305:Hence $|B(\\delta)|=h(V_W(\\delta))$ is non-decreasing. \\qed\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:315:By the same convexity argument, each $\\mathbb{E}[\\operatorname{Var}(\\cdot\\mid A^*_\\delta)]$ is non-decreasing in $\\delta$, and $D(\\delta)=\\mathbb{E}[\\operatorname{Var}(T\\mid A^*_\\delta)]$ is non-decreasing.\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:449:Since $h(x)=|\\lambda|x/(x+\\sigma_\\varepsilon^2)$ is increasing, $|B(C(\\delta))|$ is non-decreasing.\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:544:Unlike confounding, $\\varepsilon_Y$ is not independent of $A$ (since $A$ depends on $Y=\\tau T+\\varepsilon_Y$), so Lemma~\\ref{lem:bias_decomp} does not apply directly.\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:796:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:799:The sign preservation conditions for confounding, mediation, collider, and front-door are conditions on the DGP parameters (the relative strength of the causal effect versus the confounding, indirect, or collider-induced bias), not on the confusion matrix $C$.\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:937:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:1118:For HumAID ($K{=}10$, 56 scenarios), 55.4\\% are flagged as magnitude-ASV-unsafe: IV, mediation, front-door, and exposure all trigger, while confounding, collider, and M-bias remain below 10\\% bias (Figure~\\ref{fig:asv_heatmap}). For CivilComments ($K{=}2$), 100\\% of scenarios are ASV-unsafe despite $F_1$ ranging from $0.69$ (7B) to $0.82$ (frontier).\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:1159:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:1162:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:1221:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:1364:Spearman rank correlations across all topology--method pairs: $\\rho_{3,5} = 0.80$, $\\rho_{3,10} = 0.84$, $\\rho_{5,10} = 0.93$ (all $p < 10^{-8}$). Per-topology correlations are even stronger: 5 of 7 topologies (confounding, collider, M-bias, IV, and exposure at $K{=}10$) achieve $\\rho = 1.0$ between $K{=}3$ and $K{=}10$.\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:1445:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:1549:    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex:13:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex:17:\\item \\textbf{Topology-aware correction routing.} Frisch--Waugh--Lovell (FWL) invariance renders matrix-based corrections provably ineffective for four covariate topologies. We evaluate five correction methods and provide a topology-aware decision procedure (Algorithm~\\ref{alg:correction}, Appendix), validated with real LLM confusion matrices.",
    "numLines": 33
  },
  "sourceToolAssistantUUID": "816bd0a3-3b9e-4bab-a2c0-ed2acc651d34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-25T08:23:40.775Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01U6qwGNsS1i4wp3YLLppgqR`</summary>

```json
{
  "pattern": "it is worth noting|notably|importantly|furthermore|moreover|additionally|delve|leverage|utilize|a myriad|a plethora",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper",
  "glob": "*.tex",
  "-i": true,
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3cd5a8f-0fa3-4485-94d7-c151cdf73f4a",
  "isSidechain": false,
  "requestId": "req_011CbNxvgfugkhVtfata9pGK",
  "type": "assistant",
  "uuid": "c38628f5-c5c7-43e8-a1c3-f3a5e7b3e7f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2ERx3NK2sp7VbE8zaEqJF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12722,
      "cache_read_input_tokens": 51801,
      "output_tokens": 1012,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1012,
          "cache_read_input_tokens": 51801,
          "cache_creation_input_tokens": 12722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12722
          },
          "type": "message"
        }
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
  "lastPrompt": "项目：causal_annot_error_attrib Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 92 warning 一…",
  "leafUuid": "27cb121d-9787-4cd2-a9d7-2529c24a7d24",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit causal annotation error attribution paper",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb"
}
```

---

### Assistant

_source line 57 · 2026-05-25T08:23:45.009Z_

<details><summary>Logged reasoning block</summary>

```text
Good, no em-dashes (—) or explanatory en-dashes ( – ) found in the tex files. Let me continue reading more of the appendix and check for additional patterns.

Now let me do a word count for the abstract, check for specific issues, and read more of the appendix.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27cb121d-9787-4cd2-a9d7-2529c24a7d24",
  "isSidechain": false,
  "requestId": "req_011CbNxwjDyqXzXDx3aNXCQc",
  "type": "assistant",
  "uuid": "1a0ee564-4bcc-41c7-98a0-cddfc9c4c88e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EE2Xrimc1remnUVpugVqZ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31975,
      "cache_read_input_tokens": 64523,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 64523,
          "cache_creation_input_tokens": 31975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31975
          },
          "type": "message"
        }
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

_source line 58 · 2026-05-25T08:23:45.990Z_

Good — em-dash and en-dash scans are clean. Let me count abstract words and continue reading the rest of the appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a0ee564-4bcc-41c7-98a0-cddfc9c4c88e",
  "isSidechain": false,
  "requestId": "req_011CbNxwjDyqXzXDx3aNXCQc",
  "type": "assistant",
  "uuid": "ff21731f-6e09-4613-9606-5bc5b8a3f6f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EE2Xrimc1remnUVpugVqZ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31975,
      "cache_read_input_tokens": 64523,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 64523,
          "cache_creation_input_tokens": 31975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31975
          },
          "type": "message"
        }
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

_source line 59 · 2026-05-25T08:23:47.892Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BPT1Eo61raxVdfoGVyphGi`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper && cat abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~^_]//g; s/\\\\//g; s/  */ /g' | wc -w",
  "description": "Count abstract words (approximate)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff21731f-6e09-4613-9606-5bc5b8a3f6f6",
  "isSidechain": false,
  "requestId": "req_011CbNxwjDyqXzXDx3aNXCQc",
  "type": "assistant",
  "uuid": "31d88f27-61f4-44fe-94af-4b39f5f6c7a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EE2Xrimc1remnUVpugVqZ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31975,
      "cache_read_input_tokens": 64523,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 64523,
          "cache_creation_input_tokens": 31975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31975
          },
          "type": "message"
        }
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

_source line 60 · 2026-05-25T08:23:51.458Z_

<details><summary>↩ Tool result · `toolu_01WyprD1byGiLepK11zkFvtc`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex:8:\section*{Limitations}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f73bdca1-bceb-476d-a825-71586f7c6b11",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "e993c006-7c74-4f1f-b40d-e4610080c767",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex:8:\\section*{Limitations}",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "f73bdca1-bceb-476d-a825-71586f7c6b11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-25T08:23:48.061Z_

<details><summary>↩ Tool result · `toolu_01BPT1Eo61raxVdfoGVyphGi`</summary>

```text
182
Shell cwd was reset to /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31d88f27-61f4-44fe-94af-4b39f5f6c7a0",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "573d02fc-e43a-4e67-acc1-41ef9d77f4f6",
  "toolUseResult": {
    "stdout": "182",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "31d88f27-61f4-44fe-94af-4b39f5f6c7a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-25T08:23:48.846Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Dcbv4XvH8B7UcTLYdHZGw1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "offset": 900,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "573d02fc-e43a-4e67-acc1-41ef9d77f4f6",
  "isSidechain": false,
  "requestId": "req_011CbNxwjDyqXzXDx3aNXCQc",
  "type": "assistant",
  "uuid": "e2dc0199-b50a-4b19-bc1c-ac15b0f765c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EE2Xrimc1remnUVpugVqZ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31975,
      "cache_read_input_tokens": 64523,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 64523,
          "cache_creation_input_tokens": 31975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31975
          },
          "type": "message"
        }
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

_source line 63 · 2026-05-25T08:23:49.104Z_

<details><summary>↩ Tool result · `toolu_01Dcbv4XvH8B7UcTLYdHZGw1`</summary>

```text
900	The six confusion matrix structures used for Table~\ref{tab:correction} are:
901	(1)~\emph{Diagonal-dominant}: $C_{kk}{=}0.7$, off-diagonal uniform;
902	(2)~\emph{Moderate noise}: $C_{kk}{=}0.5$, off-diagonal uniform;
903	(3)~\emph{Near-permutation}: $C_{kk}{=}0.4$, largest off-diagonal 0.5;
904	(4)~\emph{Asymmetric}: $C_{kk}$ varies (0.8, 0.5, 0.3);
905	(5)~\emph{Block confusion}: two classes confused ($C_{12}{=}C_{21}{=}0.4$), third clean;
906	(6)~\emph{Heavy noise}: $C_{kk}{=}0.4$, off-diagonal uniform.
907	All are column-stochastic with $K{=}3$. Results are averaged across all six structures.
908	
909	This topology-based classification is robust to $\varepsilon$-approximate deviations; practitioners computing quantitative ASV thresholds should note the $\varepsilon$-approximate bounds (Conjecture~\ref{conj:monotone}, Section~\ref{sec:asv}). Assumes linear structural equations; FWL-based routing may not apply under nonlinear models (see Appendix~\ref{sec:logistic_dgp}). Thresholds are calibrated for $K{=}3$ linear SEM; recalibrate for different $K$ using topology-specific bias functions.
910	
911	\begin{algorithm}[H]
912	\caption{Correction method selection for LLM-annotated causal inference.}
913	\label{alg:correction}
914	\footnotesize
915	\begin{algorithmic}[1]
916	\REQUIRE DAG topology $\mathcal{T}$, gold-label availability $G \in \{\textsc{yes}, \textsc{no}\}$
917	\ENSURE Recommended method $M$, risk level $R$
918	\STATE \textbf{Step 1: Risk assessment} \COMMENT{If $\mathcal{T}$ uncertain, repeat per candidate}
919	\STATE $R \gets$ \textsc{Low} if M-bias; \textsc{Med} if Conf/Med/Coll/FD; \textsc{High} if Exp/IV
920	\STATE \textbf{Step 2: Method selection}
921	\IF{$G = \textsc{yes}$}
922	    \STATE $M \gets \text{PPI++}$ (47\% RMSE red.) except M-bias $\to$ \textsc{None} ($-$88\%)
923	\ELSE
924	    \STATE $M \gets \text{DSL}$ if Conf/Med; \text{MC-SIMEX} if IV/Coll/M-bias; $\emptyset$ otherwise
925	\ENDIF
926	\STATE \textbf{Step 3: FWL screening}
927	\IF{$\mathcal{T} \in \{\text{Conf., Med., Coll., M-bias}\}$}
928	    \STATE Skip Naive plug-in and MLA \COMMENT{0\% bias red.\ on $T$}
929	\ENDIF
930	\RETURN $(M, R)$
931	\end{algorithmic}
932	\end{algorithm}
933	
934	\subsection{Proof of FWL Invariance}
935	\label{app:fwl_proof}
936	
937	For the four topologies where $A$ enters as a covariate (confounding, mediation, collider, M-bias), the regression is $Y = \tau T + \boldsymbol{\gamma}^\top \mathbf{D}^* + \varepsilon$, where $\mathbf{D}^*$ is the $N \times (K{-}1)$ dummy matrix for $A^*$. Any matrix-based correction replaces $\mathbf{D}^*$ with $\tilde{\mathbf{D}} = \mathbf{D}^* M$ for some invertible $(K{-}1) \times (K{-}1)$ matrix $M$ (e.g., $M = C^{-1}$ for plug-in, or $M = (C^\top C)^{-1} C^\top$ for maximum likelihood estimation (MLE)). By the Frisch--Waugh--Lovell theorem~\cite{lovell1963}, $\hat{\tau}$ depends only on the residual of $T$ projected off $\operatorname{col}(\mathbf{D}^*)$. Since $\operatorname{col}(\mathbf{D}^* M) = \operatorname{col}(\mathbf{D}^*)$ for invertible $M$, the projection is unchanged and $\hat{\tau}(\tilde{\mathbf{D}}) = \hat{\tau}(\mathbf{D}^*)$ exactly. SIMEX adds noise $\mathbf{D}^*_{\text{sim}} = \mathbf{D}^* + \lambda \mathbf{E}$; when $\mathbf{E}$ is generated from the same column space, the extrapolation to $\lambda = -1$ converges to a column-space-equivalent transformation, yielding 0\% bias reduction empirically.
938	
939	\paragraph{FWL breakdown under logistic regression.}
940	\label{sec:fwl_logistic}
941	The column-space argument applies only to estimators whose treatment coefficient is a function of $T$ residualized off $\operatorname{col}(\mathbf{D}^*)$, a property of linear projection. The logistic MLE solves $\sum_i (Y_i - \sigma(\mathbf{x}_i^\top\boldsymbol{\beta}))\mathbf{x}_i = \mathbf{0}$; the implicit weighting by $\sigma'(\cdot)$ depends on the actual values of the design columns, not only on their span, so replacing $\mathbf{D}^*$ by $\mathbf{D}^* M$ generally changes the fitted $\hat\tau$. We verify this on the confounding topology ($K{=}3$, $\tau{=}0.5$, $N{=}10{,}000\times 500$ MC reps) under both linear ($Y = \tau T + \mathbf{D}\boldsymbol{\beta}+\varepsilon$) and logistic ($Y\sim\mathrm{Bern}(\sigma(\tau T + \mathbf{D}\boldsymbol{\beta}))$) DGPs, comparing the uncorrected estimator (fit on $\mathbf{D}^*$) against Naive plug-in (fit on per-sample $(C^{-1}\mathbf{e}_{A^*})_{1:K}$). Per-rep estimates are paired (same $A^*$, same outcome).
942	
943	$|\Delta|_{\max}=\max_m|\hat\tau_{\mathrm{corr}}^{(m)}-\hat\tau_{\mathrm{un}}^{(m)}|$ over 500 MC reps; bias reduction = $1-|\hat\tau_{\mathrm{corr}}-\tau_*|/|\hat\tau_{\mathrm{un}}-\tau_*|$. Confounding DAG, $K{=}3$, $N{=}10{,}000$.
944	
945	\begin{table}[H]
946	\centering
947	\caption{FWL invariance under OLS vs.\ breakdown under logistic regression.}
948	\label{tab:fwl_logistic}
949	\resizebox{\columnwidth}{!}{\begin{tabular}{lcccc}
950	\toprule
951	 & \multicolumn{2}{c}{\textbf{OLS}} & \multicolumn{2}{c}{\textbf{Logistic}} \\
952	\cmidrule(lr){2-3}\cmidrule(lr){4-5}
953	CM (VAST K=3) & $|\Delta|_{\max}$ & bias red. & $|\Delta|_{\max}$ & bias red. \\
954	\midrule
955	deepseek\_zero-shot     & $2.3\!\times\!10^{-15}$ & $+0.00\%$ & $8.1\!\times\!10^{-4}$ & $-0.09\%$ \\
956	llama4\_few-shot-3      & $5.2\!\times\!10^{-15}$ & $+0.00\%$ & $6.8\!\times\!10^{-4}$ & $-0.07\%$ \\
957	llama4\_few-shot-5      & $4.3\!\times\!10^{-15}$ & $+0.00\%$ & $6.8\!\times\!10^{-4}$ & $-0.06\%$ \\
958	llama4\_zero-shot       & $1.6\!\times\!10^{-15}$ & $+0.00\%$ & $5.9\!\times\!10^{-4}$ & $-0.05\%$ \\
959	qwen2.5-7b\_few-shot-3  & $7.2\!\times\!10^{-15}$ & $-0.00\%$ & $6.8\!\times\!10^{-4}$ & $-0.01\%$ \\
960	qwen2.5-7b\_few-shot-5  & $8.2\!\times\!10^{-15}$ & $+0.00\%$ & $5.6\!\times\!10^{-4}$ & $+0.05\%$ \\
961	\midrule
962	\textbf{Mean}           & ---                     & $\mathbf{0.0\%}$ & ---            & $\mathbf{-0.04\%}$ \\
963	\bottomrule
964	\end{tabular}}
965	\end{table}
966	
967	Two findings: (i) Under OLS, $\hat\tau_{\mathrm{corr}}^{(m)}=\hat\tau_{\mathrm{un}}^{(m)}$ to machine precision in every replication, confirming Proposition~\ref{app:fwl_proof} as an exact algebraic identity. (ii) Under logistic regression, per-replication estimates differ by $|\Delta|_{\max}\!\sim\!10^{-3}$, thirteen orders of magnitude larger than the OLS gap, so the invariance fails formally. However, the directional effect on bias is negligible: mean bias reduction is $-0.04\%$ across the six confusion matrices (range $[-0.09\%, +0.05\%]$, not even consistent in sign). Matrix-based corrections remain practically useless under logistic regression, not by an exact invariance but because the deviation is too small to systematically offset the misclassification-induced bias (which itself is $\sim\!0.10$ in absolute units, two orders of magnitude larger than $|\Delta|$). The routing rule of Algorithm~\ref{alg:correction} (skip Naive/MLA for these four topologies) is therefore conservative-but-correct under logistic regression as well. Reproduction code and numerical results are included in the supplementary material.
968	
969	\subsection{Applied Illustration: ClinicalBERT Case Study}
970	\label{app:case_study}
971	
972	To demonstrate the framework's end-to-end utility, we apply it retrospectively to \citet{lee_wood_doughty2024}, who use ClinicalBERT to classify patient smoking status ($K{=}4$: never, past, current, unknown) from clinical notes and control for this predicted confounder when estimating the causal effect of echocardiography on mortality in 4{,}735 MIMIC-III sepsis patients.
973	Our taxonomy identifies this as a confounding topology: the annotated variable enters as a confounder between treatment and outcome.
974	Three conclusions follow directly.
975	First, the zero sign-flip guarantee for confounding (Table~\ref{tab:taxonomy}) ensures that the estimated protective effect (OR~$= 0.89$) cannot reverse direction due to annotation error, a reassurance unavailable without topology-specific analysis.
976	Second, the FWL invariance result implies that any correction reducing to $C^{-1}$ applied to the dummy-coded confounder achieves exactly 0\% bias reduction for the treatment coefficient; naive plug-in is provably futile here.
977	Third, our correction guidance ranks PPI++ (83.2\% RMSE reduction for confounding) above MC-SIMEX (35.1\%) when gold labels are available, a concrete recommendation the original study lacked.
978	This example illustrates the intended workflow: DAG identification $\to$ topology-specific guarantees $\to$ correction method selection.
979	
980	\subsection{IV Wald Estimator: Diagonal-Dominance Subspaces}
981	\label{sec:iv_dirichlet_subspace}
982	
983	Section~\ref{sec:taxonomy_results} reports a 52.6\% Wald sign-flip rate
984	over the full Dirichlet$(1,1,1)$ prior. Because realistic LLM confusion
985	matrices are diagonal-dominant, we replicate the exposure-DAG stratification
986	for the IV topology, restricting the sample
987	space to $\{C : \min_k C_{kk} \geq d\}$ for $d \in \{0, 0.5, 0.7, 0.9\}$
988	(100{,}000 random matrices per threshold).
989	
990	Rates are computed over 100{,}000 Dirichlet-truncated random $C$ per threshold, with $K{=}3$ and $\tau_{\text{true}}{=}1.41$.
991	
992	\begin{table}[H]
993	\centering
994	\caption{IV Wald estimator bias by minimum-diagonal subspace.}
995	\label{tab:iv_dirichlet_subspace}
996	\small
997	\resizebox{\columnwidth}{!}{\begin{tabular}{lcccc}
998	\toprule
999	\textbf{Subspace} & \textbf{Violation} & \textbf{Sign Flip} & \textbf{Amplif.} & \textbf{Worst} \\
1000	\midrule
1001	Full           & 100.0\% & 51.7\% & 48.3\% & $10^{5}\!\times$ \\
1002	$d \geq 0.5$   & 100.0\% & 0.0\%  & 100.0\% & $28.6\times$ \\
1003	$d \geq 0.7$   & 100.0\% & 0.0\%  & 100.0\% & $2.4\times$ \\
1004	$d \geq 0.9$   & 100.0\% & 0.0\%  & 100.0\% & $1.2\times$ \\
1005	\bottomrule
1006	\end{tabular}}
1007	\end{table}
1008	
1009	The contrast with exposure is instructive: at $d{\geq}0.7$, exposure violation drops to 13.7\% (sign reversal 2.1\%, amplification 11.7\%), while IV maintains 100\% violation with pure amplification. IV sign reversal is entirely driven by pathological (near-random) confusion matrices where the Wald denominator crosses zero; diagonal dominance reduces this crossing to near-zero under empirical accuracy conditions but cannot prevent amplification. Even at $d{\geq}0.9$, the Wald estimator inflates $|\tau|$ by up to $1.24\times$ with probability~1.
1010	
1011	\subsection{Non-Differential Misclassification Verification}
1012	\label{sec:nondiff_verify}
1013	
1014	The non-differential assumption $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k)$ holds by design in standard LLM annotation pipelines: the model receives only source text as input and classifies without observing the outcome $Y$ or covariates $\mathbf{Z}$. The annotation API call is structurally independent of downstream variables, satisfying the conditional independence requirement.
1015	
1016	To provide empirical support beyond the design argument, we examine topic-stratified confusion matrices using the VAST dataset ($K{=}3$, stance detection), where the \texttt{topic} field (e.g., ``gun control,'' ``college'') serves as a proxy for latent factors correlated with $Y$. Across 10 model configurations (3 LLMs $\times$ 2--4 prompt types) and 19 qualifying topics (minimum 10 samples per topic), we compute per-topic confusion matrices $C_{\text{topic}}(t) = P(A^*{=}j \mid A{=}k, \text{topic}{=}t)$ and compare against the overall $C = P(A^*{=}j \mid A{=}k)$.
1017	
1018	Per-topic sample sizes range from 10 to 42, making individual topic CMs inherently noisy. A bootstrap permutation test ($B{=}10{,}000$) under the non-differential null shows that the expected grand maximum deviation $\max_{t,j,k} |C_{\text{topic}}(j,k) - C(j,k)|$ at the 95th percentile ranges from 0.90 to 0.98 across model configurations, driven by the smallest topics. For the 5 largest topics ($n \geq 28$), expected per-topic max deviation at the 95th percentile is 0.38--0.49, consistent with finite-sample variation rather than systematic topic-dependence. The observed per-topic variation is fully consistent with the non-differential null.
1019	
1020	This proxy-based test is necessarily limited: topic is not the actual outcome $Y$, and small per-topic samples reduce statistical power. The design argument (LLM input excludes $Y$) remains the primary justification; the stress test in Section~\ref{sec:nondiff_stress} below quantifies bias degradation under hypothetical violations.
1021	
1022	\subsection{Non-Differential Assumption Stress Test}
1023	\label{sec:nondiff_stress}
1024	
1025	Our main analysis assumes non-differential misclassification: the confusion matrix $C$ does not depend on the outcome $Y$. To assess sensitivity to violations of this assumption, we conduct a stress test on the exposure topology ($K{=}3$, $\min_k C_{kk} \geq 0.7$, 10{,}000 random matrices per $\varepsilon$). For each base matrix $C_0$, observations with $Y > \text{median}(Y)$ are misclassified using a perturbed matrix $\tilde{C} = \text{renormalize}(C_0 + \varepsilon \cdot \Delta)$ where $\Delta_{jk} \sim \text{Uniform}(-1,1)$ for $j \neq k$, while observations with $Y \leq \text{median}(Y)$ retain $C_0$.
1026	
1027	Results use the exposure DAG with $K{=}3$, $\min_k C_{kk} \geq 0.7$, and $N{=}50{,}000$ MC samples per trial.
1028	
1029	\begin{table}[H]
1030	\centering
1031	\small
1032	\caption{Effect of differential misclassification on bias violation rates.}
1033	\label{tab:nondiff_stress}
1034	\resizebox{\columnwidth}{!}{\begin{tabular}{cccc}
1035	\toprule
1036	$\varepsilon$ & Sign-Flip (\%) & Amplification (\%) & Any Violation (\%) \\
1037	\midrule
1038	0.00 & 2.0 & 11.5 & 13.3 \\
1039	0.01 & 2.4 & 12.4 & 14.7 \\
1040	0.05 & 2.8 & 13.0 & 15.7 \\
1041	0.10 & 4.5 & 16.7 & 20.9 \\
1042	0.20 & 9.7 & 23.7 & 32.6 \\
1043	0.30 & 15.5 & 28.7 & 42.8 \\
1044	0.50 & 22.9 & 34.9 & 54.6 \\
1045	\bottomrule
1046	\end{tabular}}
1047	\end{table}
1048	
1049	The $\varepsilon{=}0$ baseline (13.3\% violation) closely matches the analytical result (13.7\%) from Section~\ref{sec:taxonomy_results}. Small departures ($\varepsilon \leq 0.05$) change rates by fewer than 3 percentage points. At $\varepsilon{=}0.10$, the violation rate increases by 7.6~pp; at $\varepsilon{=}0.50$, it rises to 54.6\% (+41.2~pp), indicating substantial sensitivity to large differential error. Our main conclusions hold under mild violations but should be interpreted cautiously when outcome-conditional annotation is suspected.
1050	
1051	\paragraph{Extended stress test.}
1052	An extended stress test across 96 configurations (4 topologies $\times$ 2 $K$ $\times$ 3 CM qualities $\times$ 4 $\varepsilon$, 100 MC replications each; Table~\ref{tab:stress-test}) confirms these patterns broadly: at $\varepsilon{=}0$, sign-flip rates are zero for all configurations; at $\varepsilon{=}0.10$, the maximum sign-flip rate is 7\% (IV, low-quality $C_{kk}{=}0.4$, $K{=}3$). At $K{=}10$, sign-flip rates remain zero for all topologies and $\varepsilon$ values, suggesting that higher $K$ provides additional robustness to differential misclassification.
1053	
1054	\input{exp_a_stress_test_table.tex}
1055	
1056	\paragraph{Structured violation models.}
1057	Beyond uniform perturbations, we compare two structured violation models across all seven topologies ($K{=}3$, 1{,}000 matrices per $\varepsilon$, $\min_k C_{kk}{\geq}0.7$): (1)~\emph{outcome-conditional}, where $\tilde{C}$ applies to $Y{>}\text{median}(Y)$ while $C_0$ applies below; (2)~\emph{label-specific}, where off-diagonal perturbation magnitude scales with $|\text{corr}(A{=}k, Y)|$, modeling accuracy degradation on $Y$-predictive categories. For exposure at $\varepsilon{=}0.20$, label-specific violations are substantially milder than uniform (sign-flip 0.1\% vs.\ 10.1\%), while outcome-conditional violations are more severe (sign-flip 13.9\%, mean relative bias 0.50 vs.\ 0.40). All five sign-preserving topologies maintain 0\% sign-flip under both structured models at all $\varepsilon$ tested; IV likewise shows 0\% sign-flip (its vulnerability requires pathological diagonal structure, not differential error). These results indicate that the uniform perturbation model is neither uniformly conservative nor uniformly liberal: practitioners should assess which violation pattern is most plausible for their annotation pipeline.
1058	
1059	\subsection{Robustness to Nonlinear DGP}
1060	\label{sec:logistic_dgp}
1061	
1062	We replace the linear structural equations with $Y \sim \text{Bernoulli}(\sigma(\mathbf{x}^\top\boldsymbol{\beta}))$ and estimate via logistic regression (control function for IV) for all seven topologies, using $K{=}3$, six real VAST confusion matrices, 500 MC replications, and $N{=}10{,}000$. Mean sign-flip rates across the six CMs:
1063	
1064	\begin{center}
1065	\small
1066	\resizebox{\columnwidth}{!}{\begin{tabular}{lcccc}
1067	\toprule
1068	Topology & Linear SF$_\tau$ & Logistic SF$_\tau$ & Linear SF$_\text{any}$ & Logistic SF$_\text{any}$ \\
1069	\midrule
1070	Confounding & 0.000 & 0.000 & 0.573 & 0.559 \\
1071	Mediation & 0.000 & 0.000 & 0.703 & 0.695 \\
1072	Collider & 0.000 & 0.000 & 0.060 & 0.060 \\
1073	Exposure & --- & --- & 0.577 & 0.574 \\
1074	M-bias & 0.000 & 0.000 & 0.095 & 0.099 \\
1075	Front-door & 0.000 & 0.000 & 0.590 & 0.579 \\
1076	IV & 0.086 & 0.074 & 0.086 & 0.560 \\
1077	\bottomrule
1078	\end{tabular}}
1079	\end{center}
1080	
1081	Treatment-effect sign-flip rates (SF$_\tau$) are zero for all five guaranteed topologies under both linear and logistic DGPs, and differ by $< 0.02$ for IV. The SF$_\text{any}$ discrepancy for IV reflects estimator dimensionality: the control function includes a residual coefficient prone to sign noise; the core comparison is SF$_\tau$, where both estimators agree. Linear and logistic DGPs produce virtually identical sign-flip patterns across all seven topologies ($|\Delta\,\text{SF}_\tau| < 0.02$). Under logistic DGP, bias is measured in log-odds units; directional conclusions (sign preservation, topology ranking) transfer directly, while magnitudes are not directly comparable to linear plim expressions. For practitioners requiring finite-sample inference under logistic DGP, bias-corrected bootstrap provides a nonparametric alternative that bypasses the linear plim framework.
1082	
1083	\subsection{Bootstrap Uncertainty of ASV}
1084	\label{sec:bootstrap_asv}
1085	
1086	We assess confusion-matrix estimation uncertainty by bootstrapping label pairs from HumAID DeepSeek zero-shot ($K{=}10$, $n{=}1{,}500$): resample with replacement $B{=}1{,}000$ times, re-estimate $C_0$, and recompute magnitude ASV $\delta^*$ at a 10\% bias threshold.
1087	
1088	\begin{center}
1089	\small
1090	\resizebox{\columnwidth}{!}{\begin{tabular}{lccc}
1091	\toprule
1092	Topology & $\delta^*$ (point) & 95\% CI & Valid / 1000 \\
1093	\midrule
1094	Confounding & --- & --- & 0 \\
1095	Exposure & 0.937 & [0.602, 1.363] & 907 \\
1096	IV & 0.754 & [0.435, 1.290] & 902 \\
1097	\bottomrule
1098	\end{tabular}}
1099	\end{center}
1100	
1101	Confounding never reaches the 10\% threshold across all 1{,}000 bootstraps, confirming robustness. For IV, the 95\% CI spans a $3{\times}$ range (0.435 to 1.290); practitioners should bootstrap $C_0$ rather than rely on a point estimate when ASV is near the decision boundary. CI width scales as $O(1/\sqrt{n})$ where $n$ is the gold-label validation set size; at $n{=}1{,}500$, IV CIs are ${\sim}3{\times}$ wider than exposure CIs, reflecting the Wald estimator's denominator instability. A convergence study ($K{=}3$, $B{=}1{,}000$) confirms this scaling: exposure CI width narrows from 0.60 ($n{=}500$) to 0.05 ($n{=}50{,}000$), and IV from 0.52 to 0.04, with the product $\text{width} \times \sqrt{n}$ approximately constant (CV $< 0.20$).
1102	
1103	\begin{figure*}[ht!]
1104	\centering
1105	\includegraphics[width=\textwidth]{exp_c_bootstrap_figure.pdf}
1106	\caption{Bootstrap distribution of magnitude ASV $\delta^*$ ($B{=}1{,}000$) for HumAID DeepSeek zero-shot ($K{=}10$). Dashed line: point estimate; shaded: 95\% CI.}
1107	\label{fig:bootstrap_asv}
1108	\end{figure*}
1109	
1110	\subsection{Cross-$K$ Robustness}
1111	\label{sec:cross_k_robustness}
1112	
1113	All structural patterns persist at $K{=}5,7$ (100{,}000 matrices each): sign-flip guarantees hold for the same five topologies, and IV sign-flip rates remain within 51--53\%.
1114	
1115	\subsection{ASV Diagnostic Results}
1116	\label{sec:asv_diagnostics}
1117	
1118	For HumAID ($K{=}10$, 56 scenarios), 55.4\% are flagged as magnitude-ASV-unsafe: IV, mediation, front-door, and exposure all trigger, while confounding, collider, and M-bias remain below 10\% bias (Figure~\ref{fig:asv_heatmap}). For CivilComments ($K{=}2$), 100\% of scenarios are ASV-unsafe despite $F_1$ ranging from $0.69$ (7B) to $0.82$ (frontier).
1119	
1120	Overlaying all 23 empirical matrices onto the theoretical Dirichlet violation-rate curves (Figure~\ref{fig:dirichlet_overlay}) confirms placement: VAST in the danger zone, HumAID mid-range, CivilComments approaching safe for exposure but still in IV amplification.
1121	
1122	\subsection{ASV Stability Across DGP Parameters}
1123	\label{sec:asv_stability}
1124	
1125	We test whether ASV rankings are stable across different data-generating process (DGP) configurations by varying the treatment-effect vector $\boldsymbol{\beta}$ across three settings: alternating-large ($\boldsymbol{\beta}=[0,\,1.0,\,-0.5]$), same-sign ($\boldsymbol{\beta}=[0,\,0.5,\,0.3]$), and alternating-small ($\boldsymbol{\beta}=[0,\,0.2,\,-0.1]$), with $K{=}3$, $\tau{=}0.5$, and five $C_0$ diagonal values $\in\{0.5,0.6,0.7,0.8,0.9\}$.
1126	
1127	\input{exp_e_asv_stability_table.tex}
1128	
1129	Three patterns emerge (Table~\ref{tab:asv_stability}). First, IV magnitude ASV is identical across all three DGPs ($\delta^*{=}0.203$). This is a mathematical identity, not an empirical finding: the Wald estimator $\hat{\tau}_{\text{IV}} = \text{RF}/\text{FS}$ has $\boldsymbol{\beta}$ in both numerator and denominator, and the ratio depends only on $C$ and the first-stage structure, making ASV invariant to $\boldsymbol{\beta}$ by construction. Second, exposure ASV depends on the coefficient ratio structure: alternating-large ($\beta_2/\beta_1 = -0.5$) and alternating-small ($\beta_2/\beta_1 = -0.5$) share the same ratio and yield identical $\delta^*{=}0.090$, while same-sign ($\beta_2/\beta_1 = 0.6$) gives $\delta^*{=}0.223$; thus the experiment provides two distinct sign-structure conditions, not three. Third, confounding ASV depends on effect magnitudes: only alternating-large triggers the 10\% threshold ($\delta^*{=}0.348$); smaller effects never reach 10\% bias.
1130	
1131	Confounding is consistently the most robust topology (highest ASV or no violation), and M-bias remains immune (not shown). However, the relative fragility of exposure vs.\ IV inverts with coefficient sign structure: under alternating signs, exposure is most fragile ($0.090 < 0.203$); under same-sign effects, IV is most fragile ($0.203 < 0.223$). Practitioners should compute ASV with their specific DGP rather than relying on generic rankings.
1132	
1133	\subsection{Extended Conjecture Verification}
1134	\label{sec:conjecture_verify}
1135	
1136	We test envelope monotonicity (Conjecture~\ref{conj:monotone}) by sampling 10{,}000 random $C_0$ matrices from Dirichlet$(1,\dots,1)$ per topology for $K \in \{3,5,7\}$ (210{,}000 total), sweeping $\delta$ in steps of 0.01, and counting matrices with at least one non-monotonic step exceeding tolerance $10^{-12}$. Bias at each $\delta$ is computed via analytic probability limits using Gauss--Hermite quadrature (100 points), eliminating sampling noise entirely.
1137	
1138	The $\delta$ step size is 0.01. ``Worst mag.''\ is the largest single-step deviation $|B(\delta_{i+1})|-|B(\delta_i)|$ in the non-monotonic direction. $^*$100{,}000 matrices at step $= 0.005$ yield exposure $\varepsilon = 0.075$.
1139	
1140	\begin{table}[H]
1141	\centering
1142	\caption{Envelope monotonicity violations per 10{,}000 random $C_0$ matrices.}
1143	\label{tab:conjecture_verify}
1144	\resizebox{\columnwidth}{!}{\begin{tabular}{lccccc}
1145	\toprule
1146	\textbf{Topology} & $K{=}3$ & $K{=}5$ & $K{=}7$ & \textbf{Worst mag.} & \textbf{Direction} \\
1147	\midrule
1148	Confounding & 8467 & 8063 & 7892 & 0.011 & non-dec \\
1149	Mediation   & 8236 & 7905 & 7893 & 0.013 & non-dec \\
1150	Collider    & 8683 & 7669 & 7570 & 0.005 & non-inc \\
1151	Exposure    & 485  & 205  & 77   & 0.056$^*$ & non-dec \\
1152	M-bias      & 9791 & 7783 & 7399 & 0.002 & non-inc \\
1153	IV          & 7433 & 6015 & 5711 & $>10^6$ & non-dec \\
1154	Front-door  & 8429 & 8079 & 7899 & 0.013 & non-dec \\
1155	\bottomrule
1156	\end{tabular}}
1157	\end{table}
1158	
1159	Violation counts are high (60--97\% of matrices), but magnitudes are small for non-IV topologies under the default parameterization (Table~\ref{tab:conjecture_verify}); DGP sensitivity analysis (Table~\ref{tab:dgp_sensitivity}) shows $\varepsilon$ scales with effect magnitude $|\beta|$, remaining below 0.02 for $|\beta| \leq 1$ across non-exposure topologies. These results are computed from analytic probability limits with zero sampling noise, confirming the violations are structural properties of multi-class confusion matrices rather than numerical artifacts. IV deviations reflect Wald estimator singularities when the first-stage coefficient passes near zero; this is a property of the Wald estimator, not of the ASV parameterization. Adversarial search (500 restarts per configuration, $K \in \{3,5\}$) finds genuine counterexamples for all topologies except IV $K{=}3$, confirming that strict monotonicity does not hold universally. The bias envelope is $\varepsilon$-approximately monotonic with $\varepsilon < 0.03$ for collider and M-bias across all tested $\tau$; confounding, mediation, and front-door achieve $\varepsilon < 0.06$ at default DGP parameters (see DGP sensitivity below); exposure satisfies $\varepsilon_{p99} < 0.008$ but extreme-tail matrices ($<$0.02\% of draws) reach $\varepsilon \approx 0.15$. Empirically, $\varepsilon$ scales as $O(1/K^\alpha)$ with $\alpha \in [0.6, 1.5]$ (topology-dependent): for confounding, mediation, and front-door, $\alpha \approx 1.4$; for exposure, $\alpha \approx 1.0$; for collider and M-bias, $\alpha \approx 0.7$. A universal empirical upper bound is $\varepsilon \leq 0.137/\sqrt{K}$, verified across all tested configurations ($K \in \{3,5,7\}$). This scaling supports the practical validity of ASV as a sensitivity tool at any meaningful bias threshold.
1160	
1161	\paragraph{DGP parameter sensitivity.}
1162	We repeat the verification across $\tau \in \{0.1, 0.5, 1.0, 2.0, 5.0\}$, varying the direct $T{\to}Y$ coefficient for confounding ($\beta_T{=}\tau$), mediation, collider, and M-bias (DGP $\tau$), and rescaling the $A{\to}Y$ coefficient vector to $\boldsymbol{\beta}\cdot\tau$ for exposure and front-door. With 10{,}000 random $C_0$ per $(K,\tau)$ setting (Table~\ref{tab:conjecture_tau_sens}), $\varepsilon$ remains small ($< 0.03$) for $\tau \geq 0.5$ for confounding, mediation, collider, and M-bias, but grows at $\tau{=}0.1$: mediation produces 1{,}950 / 30{,}000 violations across $K \in \{3,5,7\}$ (worst $\varepsilon{=}0.130$ at $K{=}3$) and confounding 200 / 30{,}000 (worst $\varepsilon{=}0.118$ at $K{=}3$). The mechanism is dimensional: additive terms not scaling with $\tau$ (e.g.\ the $\boldsymbol{\beta}$-contribution to $\mathbb{E}[Y D_k]$ in mediation and confounding) contribute a $\tau$-independent offset to the bias numerator, so the ratio $|B|/|\tau|$ inflates as $\tau \to 0$. A single mediation violation at $\tau{=}2.0$ ($\varepsilon{=}0.112$, 1/30{,}000 matrices) arises from a specific confusion matrix structure where off-diagonal entries induce partial cancellation along the mediation pathway; this isolated case does not affect the $p_{99}$ bound ($\varepsilon_{p99}{=}0.005$). Collider and M-bias remain robust at all $\tau$ ($\varepsilon{<}0.022$ and $\varepsilon{<}0.015$ respectively). Exposure shows scattered tail outliers but $\overline{\varepsilon} \approx 3\!\times\!10^{-4}$ at every $\tau$, consistent with linear scaling: when $\boldsymbol{\beta}$ rescales by $\tau$, both bias and $\tau_{\text{true}}$ scale by the same factor and $\varepsilon$ is theoretically invariant. Front-door inverts the pattern ($\varepsilon$ grows with $\tau$, reaching $0.139$ at $\tau{=}5$, $K{=}3$, with 664 violations) because $\tau_{\text{true}} = \operatorname{plim}(\hat{\tau}_T \mid C{=}I)$ is pinned at $0.5$ by the $U$-confounding path while bias magnitudes scale with $\boldsymbol{\beta}$; this is an artefact of how $\tau_{\text{true}}$ is normalised, not a genuine failure of envelope monotonicity. In practice, ASV's $\delta^*$ thresholds (typically $\geq 0.1$ in our deployment) are well above the region where these $\varepsilon$-violations occur, so the small-$\tau$ degradation does not affect ASV's operational reliability; we flag it as a caveat for applications targeting $|\tau| \lesssim 0.1$ in standardised units.
1163	
1164	$\varepsilon \equiv \max_\delta(|B(\delta{+}\Delta)|{-}|B(\delta)|)/|\tau_{\text{true}}|$ in the non-monotonic direction, taking the max over $K \in \{3,5,7\}$ with 10{,}000 random $C_0$ per cell. Bold marks $\varepsilon > 0.02$ (non-exposure) or $\varepsilon > 0.08$ (exposure). Counts in parentheses are violations / 30{,}000. Tables~\ref{tab:conjecture_verify} and~\ref{tab:conjecture_tau_sens} use independent random seeds; for topologies with low violation rates (exposure $<$0.02\%), the worst-case $\varepsilon$ is sample-sensitive.
1165	
1166	\begin{table}[H]
1167	\centering
1168	\caption{DGP parameter sensitivity of envelope monotonicity violations.}
1169	\label{tab:conjecture_tau_sens}
1170	\resizebox{\columnwidth}{!}{\begin{tabular}{lccccc}
1171	\toprule
1172	\textbf{Topology} & $\tau{=}0.1$ & $\tau{=}0.5$ & $\tau{=}1.0$ & $\tau{=}2.0$ & $\tau{=}5.0$ \\
1173	\midrule
1174	Confounding & \textbf{0.118} (200) & 0.027 (0) & 0.014 (0) & 0.007 (0) & 0.002 (0) \\
1175	Mediation   & \textbf{0.130} (1950) & 0.026 (0) & 0.013 (0) & \textbf{0.112} (1) & 0.003 (0) \\
1176	Collider    & 0.022 (0) & 0.006 (0) & 0.005 (0) & 0.004 (0) & 0.002 (0) \\
1177	Exposure    & \textbf{0.111} (5) & \textbf{0.122} (2) & \textbf{0.152} (2) & \textbf{0.089} (3) & \textbf{0.148} (3) \\
1178	M-bias      & 0.014 (0) & 0.003 (0) & 0.001 (0) & 0.001 (0) & 0.000 (0) \\
1179	Front-door  & 0.003 (0) & 0.013 (0) & 0.027 (0) & 0.051 (0) & \textbf{0.139} (664) \\
1180	\bottomrule
1181	\end{tabular}}
1182	\end{table}
1183	
1184	\paragraph{Effect-magnitude sensitivity.}
1185	We further vary the direct effect $\beta \in \{0.1, 0.5, 1.0, 2.0, 5.0\}$ and noise variance $\sigma^2 \in \{0.5, 1.0, 2.0\}$ across all seven topologies ($K{=}3$, 10{,}000 Dirichlet$(1,\ldots,1)$ matrices per cell). Table~\ref{tab:dgp_sensitivity} reports the worst-case relative envelope deviation $\varepsilon_{\text{rel}}$. For non-exposure topologies, $\varepsilon$ scales approximately linearly with $|\beta|$; the safe/fragile partition is stable across all 105 cells.
1186	
1187	\input{conjecture_dgp_sensitivity_table.tex}
1188	
1189	\subsection{Proportional Effects Breakdown}
1190	\label{sec:proportional_effects}
1191	
1192	Theorem~\ref{thm:monotone} requires proportional effects ($f = \lambda g$); here we quantify how $\lambda(C)$ out-of-bounds (OOB) rates depend on the degree of departure from proportionality. We simulate $K{=}3$ mediation with 100{,}000 random confusion matrices (diagonal $\geq 0.5$, Dirichlet off-diagonal) at five proportionality degrees: exact ($f_j {-} f_0 = \lambda(g_j {-} g_0)$), near-proportional ($f = \lambda g + \epsilon$, $\epsilon \sim \mathcal{N}(0,\sigma^2)$, $\sigma \in \{0.1, 0.3, 0.5\}$), and fully independent ($f \perp g$). Table~\ref{tab:proportional_effects} reports the $\lambda(C) \notin [0,1]$ rate.
1193	
1194	Results use $K{=}3$ with 100K random confusion matrices per row.
1195	
1196	\begin{table}[H]
1197	\centering
1198	\small
1199	\caption{$\lambda(C)$ out-of-bounds rate and mediation sign failure rate.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2dc0199-b50a-4b19-bc1c-ac15b0f765c5",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "9424c6e1-def5-4784-8378-34a1746e75d9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
      "content": "The six confusion matrix structures used for Table~\\ref{tab:correction} are:\n(1)~\\emph{Diagonal-dominant}: $C_{kk}{=}0.7$, off-diagonal uniform;\n(2)~\\emph{Moderate noise}: $C_{kk}{=}0.5$, off-diagonal uniform;\n(3)~\\emph{Near-permutation}: $C_{kk}{=}0.4$, largest off-diagonal 0.5;\n(4)~\\emph{Asymmetric}: $C_{kk}$ varies (0.8, 0.5, 0.3);\n(5)~\\emph{Block confusion}: two classes confused ($C_{12}{=}C_{21}{=}0.4$), third clean;\n(6)~\\emph{Heavy noise}: $C_{kk}{=}0.4$, off-diagonal uniform.\nAll are column-stochastic with $K{=}3$. Results are averaged across all six structures.\n\nThis topology-based classification is robust to $\\varepsilon$-approximate deviations; practitioners computing quantitative ASV thresholds should note the $\\varepsilon$-approximate bounds (Conjecture~\\ref{conj:monotone}, Section~\\ref{sec:asv}). Assumes linear structural equations; FWL-based routing may not apply under nonlinear models (see Appendix~\\ref{sec:logistic_dgp}). Thresholds are calibrated for $K{=}3$ linear SEM; recalibrate for different $K$ using topology-specific bias functions.\n\n\\begin{algorithm}[H]\n\\caption{Correction method selection for LLM-annotated causal inference.}\n\\label{alg:correction}\n\\footnotesize\n\\begin{algorithmic}[1]\n\\REQUIRE DAG topology $\\mathcal{T}$, gold-label availability $G \\in \\{\\textsc{yes}, \\textsc{no}\\}$\n\\ENSURE Recommended method $M$, risk level $R$\n\\STATE \\textbf{Step 1: Risk assessment} \\COMMENT{If $\\mathcal{T}$ uncertain, repeat per candidate}\n\\STATE $R \\gets$ \\textsc{Low} if M-bias; \\textsc{Med} if Conf/Med/Coll/FD; \\textsc{High} if Exp/IV\n\\STATE \\textbf{Step 2: Method selection}\n\\IF{$G = \\textsc{yes}$}\n    \\STATE $M \\gets \\text{PPI++}$ (47\\% RMSE red.) except M-bias $\\to$ \\textsc{None} ($-$88\\%)\n\\ELSE\n    \\STATE $M \\gets \\text{DSL}$ if Conf/Med; \\text{MC-SIMEX} if IV/Coll/M-bias; $\\emptyset$ otherwise\n\\ENDIF\n\\STATE \\textbf{Step 3: FWL screening}\n\\IF{$\\mathcal{T} \\in \\{\\text{Conf., Med., Coll., M-bias}\\}$}\n    \\STATE Skip Naive plug-in and MLA \\COMMENT{0\\% bias red.\\ on $T$}\n\\ENDIF\n\\RETURN $(M, R)$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\subsection{Proof of FWL Invariance}\n\\label{app:fwl_proof}\n\nFor the four topologies where $A$ enters as a covariate (confounding, mediation, collider, M-bias), the regression is $Y = \\tau T + \\boldsymbol{\\gamma}^\\top \\mathbf{D}^* + \\varepsilon$, where $\\mathbf{D}^*$ is the $N \\times (K{-}1)$ dummy matrix for $A^*$. Any matrix-based correction replaces $\\mathbf{D}^*$ with $\\tilde{\\mathbf{D}} = \\mathbf{D}^* M$ for some invertible $(K{-}1) \\times (K{-}1)$ matrix $M$ (e.g., $M = C^{-1}$ for plug-in, or $M = (C^\\top C)^{-1} C^\\top$ for maximum likelihood estimation (MLE)). By the Frisch--Waugh--Lovell theorem~\\cite{lovell1963}, $\\hat{\\tau}$ depends only on the residual of $T$ projected off $\\operatorname{col}(\\mathbf{D}^*)$. Since $\\operatorname{col}(\\mathbf{D}^* M) = \\operatorname{col}(\\mathbf{D}^*)$ for invertible $M$, the projection is unchanged and $\\hat{\\tau}(\\tilde{\\mathbf{D}}) = \\hat{\\tau}(\\mathbf{D}^*)$ exactly. SIMEX adds noise $\\mathbf{D}^*_{\\text{sim}} = \\mathbf{D}^* + \\lambda \\mathbf{E}$; when $\\mathbf{E}$ is generated from the same column space, the extrapolation to $\\lambda = -1$ converges to a column-space-equivalent transformation, yielding 0\\% bias reduction empirically.\n\n\\paragraph{FWL breakdown under logistic regression.}\n\\label{sec:fwl_logistic}\nThe column-space argument applies only to estimators whose treatment coefficient is a function of $T$ residualized off $\\operatorname{col}(\\mathbf{D}^*)$, a property of linear projection. The logistic MLE solves $\\sum_i (Y_i - \\sigma(\\mathbf{x}_i^\\top\\boldsymbol{\\beta}))\\mathbf{x}_i = \\mathbf{0}$; the implicit weighting by $\\sigma'(\\cdot)$ depends on the actual values of the design columns, not only on their span, so replacing $\\mathbf{D}^*$ by $\\mathbf{D}^* M$ generally changes the fitted $\\hat\\tau$. We verify this on the confounding topology ($K{=}3$, $\\tau{=}0.5$, $N{=}10{,}000\\times 500$ MC reps) under both linear ($Y = \\tau T + \\mathbf{D}\\boldsymbol{\\beta}+\\varepsilon$) and logistic ($Y\\sim\\mathrm{Bern}(\\sigma(\\tau T + \\mathbf{D}\\boldsymbol{\\beta}))$) DGPs, comparing the uncorrected estimator (fit on $\\mathbf{D}^*$) against Naive plug-in (fit on per-sample $(C^{-1}\\mathbf{e}_{A^*})_{1:K}$). Per-rep estimates are paired (same $A^*$, same outcome).\n\n$|\\Delta|_{\\max}=\\max_m|\\hat\\tau_{\\mathrm{corr}}^{(m)}-\\hat\\tau_{\\mathrm{un}}^{(m)}|$ over 500 MC reps; bias reduction = $1-|\\hat\\tau_{\\mathrm{corr}}-\\tau_*|/|\\hat\\tau_{\\mathrm{un}}-\\tau_*|$. Confounding DAG, $K{=}3$, $N{=}10{,}000$.\n\n\\begin{table}[H]\n\\centering\n\\caption{FWL invariance under OLS vs.\\ breakdown under logistic regression.}\n\\label{tab:fwl_logistic}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{OLS}} & \\multicolumn{2}{c}{\\textbf{Logistic}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\nCM (VAST K=3) & $|\\Delta|_{\\max}$ & bias red. & $|\\Delta|_{\\max}$ & bias red. \\\\\n\\midrule\ndeepseek\\_zero-shot     & $2.3\\!\\times\\!10^{-15}$ & $+0.00\\%$ & $8.1\\!\\times\\!10^{-4}$ & $-0.09\\%$ \\\\\nllama4\\_few-shot-3      & $5.2\\!\\times\\!10^{-15}$ & $+0.00\\%$ & $6.8\\!\\times\\!10^{-4}$ & $-0.07\\%$ \\\\\nllama4\\_few-shot-5      & $4.3\\!\\times\\!10^{-15}$ & $+0.00\\%$ & $6.8\\!\\times\\!10^{-4}$ & $-0.06\\%$ \\\\\nllama4\\_zero-shot       & $1.6\\!\\times\\!10^{-15}$ & $+0.00\\%$ & $5.9\\!\\times\\!10^{-4}$ & $-0.05\\%$ \\\\\nqwen2.5-7b\\_few-shot-3  & $7.2\\!\\times\\!10^{-15}$ & $-0.00\\%$ & $6.8\\!\\times\\!10^{-4}$ & $-0.01\\%$ \\\\\nqwen2.5-7b\\_few-shot-5  & $8.2\\!\\times\\!10^{-15}$ & $+0.00\\%$ & $5.6\\!\\times\\!10^{-4}$ & $+0.05\\%$ \\\\\n\\midrule\n\\textbf{Mean}           & ---                     & $\\mathbf{0.0\\%}$ & ---            & $\\mathbf{-0.04\\%}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTwo findings: (i) Under OLS, $\\hat\\tau_{\\mathrm{corr}}^{(m)}=\\hat\\tau_{\\mathrm{un}}^{(m)}$ to machine precision in every replication, confirming Proposition~\\ref{app:fwl_proof} as an exact algebraic identity. (ii) Under logistic regression, per-replication estimates differ by $|\\Delta|_{\\max}\\!\\sim\\!10^{-3}$, thirteen orders of magnitude larger than the OLS gap, so the invariance fails formally. However, the directional effect on bias is negligible: mean bias reduction is $-0.04\\%$ across the six confusion matrices (range $[-0.09\\%, +0.05\\%]$, not even consistent in sign). Matrix-based corrections remain practically useless under logistic regression, not by an exact invariance but because the deviation is too small to systematically offset the misclassification-induced bias (which itself is $\\sim\\!0.10$ in absolute units, two orders of magnitude larger than $|\\Delta|$). The routing rule of Algorithm~\\ref{alg:correction} (skip Naive/MLA for these four topologies) is therefore conservative-but-correct under logistic regression as well. Reproduction code and numerical results are included in the supplementary material.\n\n\\subsection{Applied Illustration: ClinicalBERT Case Study}\n\\label{app:case_study}\n\nTo demonstrate the framework's end-to-end utility, we apply it retrospectively to \\citet{lee_wood_doughty2024}, who use ClinicalBERT to classify patient smoking status ($K{=}4$: never, past, current, unknown) from clinical notes and control for this predicted confounder when estimating the causal effect of echocardiography on mortality in 4{,}735 MIMIC-III sepsis patients.\nOur taxonomy identifies this as a confounding topology: the annotated variable enters as a confounder between treatment and outcome.\nThree conclusions follow directly.\nFirst, the zero sign-flip guarantee for confounding (Table~\\ref{tab:taxonomy}) ensures that the estimated protective effect (OR~$= 0.89$) cannot reverse direction due to annotation error, a reassurance unavailable without topology-specific analysis.\nSecond, the FWL invariance result implies that any correction reducing to $C^{-1}$ applied to the dummy-coded confounder achieves exactly 0\\% bias reduction for the treatment coefficient; naive plug-in is provably futile here.\nThird, our correction guidance ranks PPI++ (83.2\\% RMSE reduction for confounding) above MC-SIMEX (35.1\\%) when gold labels are available, a concrete recommendation the original study lacked.\nThis example illustrates the intended workflow: DAG identification $\\to$ topology-specific guarantees $\\to$ correction method selection.\n\n\\subsection{IV Wald Estimator: Diagonal-Dominance Subspaces}\n\\label{sec:iv_dirichlet_subspace}\n\nSection~\\ref{sec:taxonomy_results} reports a 52.6\\% Wald sign-flip rate\nover the full Dirichlet$(1,1,1)$ prior. Because realistic LLM confusion\nmatrices are diagonal-dominant, we replicate the exposure-DAG stratification\nfor the IV topology, restricting the sample\nspace to $\\{C : \\min_k C_{kk} \\geq d\\}$ for $d \\in \\{0, 0.5, 0.7, 0.9\\}$\n(100{,}000 random matrices per threshold).\n\nRates are computed over 100{,}000 Dirichlet-truncated random $C$ per threshold, with $K{=}3$ and $\\tau_{\\text{true}}{=}1.41$.\n\n\\begin{table}[H]\n\\centering\n\\caption{IV Wald estimator bias by minimum-diagonal subspace.}\n\\label{tab:iv_dirichlet_subspace}\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Subspace} & \\textbf{Violation} & \\textbf{Sign Flip} & \\textbf{Amplif.} & \\textbf{Worst} \\\\\n\\midrule\nFull           & 100.0\\% & 51.7\\% & 48.3\\% & $10^{5}\\!\\times$ \\\\\n$d \\geq 0.5$   & 100.0\\% & 0.0\\%  & 100.0\\% & $28.6\\times$ \\\\\n$d \\geq 0.7$   & 100.0\\% & 0.0\\%  & 100.0\\% & $2.4\\times$ \\\\\n$d \\geq 0.9$   & 100.0\\% & 0.0\\%  & 100.0\\% & $1.2\\times$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe contrast with exposure is instructive: at $d{\\geq}0.7$, exposure violation drops to 13.7\\% (sign reversal 2.1\\%, amplification 11.7\\%), while IV maintains 100\\% violation with pure amplification. IV sign reversal is entirely driven by pathological (near-random) confusion matrices where the Wald denominator crosses zero; diagonal dominance reduces this crossing to near-zero under empirical accuracy conditions but cannot prevent amplification. Even at $d{\\geq}0.9$, the Wald estimator inflates $|\\tau|$ by up to $1.24\\times$ with probability~1.\n\n\\subsection{Non-Differential Misclassification Verification}\n\\label{sec:nondiff_verify}\n\nThe non-differential assumption $P(A^*{=}j \\mid A{=}k, Y, \\mathbf{Z}) = P(A^*{=}j \\mid A{=}k)$ holds by design in standard LLM annotation pipelines: the model receives only source text as input and classifies without observing the outcome $Y$ or covariates $\\mathbf{Z}$. The annotation API call is structurally independent of downstream variables, satisfying the conditional independence requirement.\n\nTo provide empirical support beyond the design argument, we examine topic-stratified confusion matrices using the VAST dataset ($K{=}3$, stance detection), where the \\texttt{topic} field (e.g., ``gun control,'' ``college'') serves as a proxy for latent factors correlated with $Y$. Across 10 model configurations (3 LLMs $\\times$ 2--4 prompt types) and 19 qualifying topics (minimum 10 samples per topic), we compute per-topic confusion matrices $C_{\\text{topic}}(t) = P(A^*{=}j \\mid A{=}k, \\text{topic}{=}t)$ and compare against the overall $C = P(A^*{=}j \\mid A{=}k)$.\n\nPer-topic sample sizes range from 10 to 42, making individual topic CMs inherently noisy. A bootstrap permutation test ($B{=}10{,}000$) under the non-differential null shows that the expected grand maximum deviation $\\max_{t,j,k} |C_{\\text{topic}}(j,k) - C(j,k)|$ at the 95th percentile ranges from 0.90 to 0.98 across model configurations, driven by the smallest topics. For the 5 largest topics ($n \\geq 28$), expected per-topic max deviation at the 95th percentile is 0.38--0.49, consistent with finite-sample variation rather than systematic topic-dependence. The observed per-topic variation is fully consistent with the non-differential null.\n\nThis proxy-based test is necessarily limited: topic is not the actual outcome $Y$, and small per-topic samples reduce statistical power. The design argument (LLM input excludes $Y$) remains the primary justification; the stress test in Section~\\ref{sec:nondiff_stress} below quantifies bias degradation under hypothetical violations.\n\n\\subsection{Non-Differential Assumption Stress Test}\n\\label{sec:nondiff_stress}\n\nOur main analysis assumes non-differential misclassification: the confusion matrix $C$ does not depend on the outcome $Y$. To assess sensitivity to violations of this assumption, we conduct a stress test on the exposure topology ($K{=}3$, $\\min_k C_{kk} \\geq 0.7$, 10{,}000 random matrices per $\\varepsilon$). For each base matrix $C_0$, observations with $Y > \\text{median}(Y)$ are misclassified using a perturbed matrix $\\tilde{C} = \\text{renormalize}(C_0 + \\varepsilon \\cdot \\Delta)$ where $\\Delta_{jk} \\sim \\text{Uniform}(-1,1)$ for $j \\neq k$, while observations with $Y \\leq \\text{median}(Y)$ retain $C_0$.\n\nResults use the exposure DAG with $K{=}3$, $\\min_k C_{kk} \\geq 0.7$, and $N{=}50{,}000$ MC samples per trial.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\caption{Effect of differential misclassification on bias violation rates.}\n\\label{tab:nondiff_stress}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{cccc}\n\\toprule\n$\\varepsilon$ & Sign-Flip (\\%) & Amplification (\\%) & Any Violation (\\%) \\\\\n\\midrule\n0.00 & 2.0 & 11.5 & 13.3 \\\\\n0.01 & 2.4 & 12.4 & 14.7 \\\\\n0.05 & 2.8 & 13.0 & 15.7 \\\\\n0.10 & 4.5 & 16.7 & 20.9 \\\\\n0.20 & 9.7 & 23.7 & 32.6 \\\\\n0.30 & 15.5 & 28.7 & 42.8 \\\\\n0.50 & 22.9 & 34.9 & 54.6 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe $\\varepsilon{=}0$ baseline (13.3\\% violation) closely matches the analytical result (13.7\\%) from Section~\\ref{sec:taxonomy_results}. Small departures ($\\varepsilon \\leq 0.05$) change rates by fewer than 3 percentage points. At $\\varepsilon{=}0.10$, the violation rate increases by 7.6~pp; at $\\varepsilon{=}0.50$, it rises to 54.6\\% (+41.2~pp), indicating substantial sensitivity to large differential error. Our main conclusions hold under mild violations but should be interpreted cautiously when outcome-conditional annotation is suspected.\n\n\\paragraph{Extended stress test.}\nAn extended stress test across 96 configurations (4 topologies $\\times$ 2 $K$ $\\times$ 3 CM qualities $\\times$ 4 $\\varepsilon$, 100 MC replications each; Table~\\ref{tab:stress-test}) confirms these patterns broadly: at $\\varepsilon{=}0$, sign-flip rates are zero for all configurations; at $\\varepsilon{=}0.10$, the maximum sign-flip rate is 7\\% (IV, low-quality $C_{kk}{=}0.4$, $K{=}3$). At $K{=}10$, sign-flip rates remain zero for all topologies and $\\varepsilon$ values, suggesting that higher $K$ provides additional robustness to differential misclassification.\n\n\\input{exp_a_stress_test_table.tex}\n\n\\paragraph{Structured violation models.}\nBeyond uniform perturbations, we compare two structured violation models across all seven topologies ($K{=}3$, 1{,}000 matrices per $\\varepsilon$, $\\min_k C_{kk}{\\geq}0.7$): (1)~\\emph{outcome-conditional}, where $\\tilde{C}$ applies to $Y{>}\\text{median}(Y)$ while $C_0$ applies below; (2)~\\emph{label-specific}, where off-diagonal perturbation magnitude scales with $|\\text{corr}(A{=}k, Y)|$, modeling accuracy degradation on $Y$-predictive categories. For exposure at $\\varepsilon{=}0.20$, label-specific violations are substantially milder than uniform (sign-flip 0.1\\% vs.\\ 10.1\\%), while outcome-conditional violations are more severe (sign-flip 13.9\\%, mean relative bias 0.50 vs.\\ 0.40). All five sign-preserving topologies maintain 0\\% sign-flip under both structured models at all $\\varepsilon$ tested; IV likewise shows 0\\% sign-flip (its vulnerability requires pathological diagonal structure, not differential error). These results indicate that the uniform perturbation model is neither uniformly conservative nor uniformly liberal: practitioners should assess which violation pattern is most plausible for their annotation pipeline.\n\n\\subsection{Robustness to Nonlinear DGP}\n\\label{sec:logistic_dgp}\n\nWe replace the linear structural equations with $Y \\sim \\text{Bernoulli}(\\sigma(\\mathbf{x}^\\top\\boldsymbol{\\beta}))$ and estimate via logistic regression (control function for IV) for all seven topologies, using $K{=}3$, six real VAST confusion matrices, 500 MC replications, and $N{=}10{,}000$. Mean sign-flip rates across the six CMs:\n\n\\begin{center}\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nTopology & Linear SF$_\\tau$ & Logistic SF$_\\tau$ & Linear SF$_\\text{any}$ & Logistic SF$_\\text{any}$ \\\\\n\\midrule\nConfounding & 0.000 & 0.000 & 0.573 & 0.559 \\\\\nMediation & 0.000 & 0.000 & 0.703 & 0.695 \\\\\nCollider & 0.000 & 0.000 & 0.060 & 0.060 \\\\\nExposure & --- & --- & 0.577 & 0.574 \\\\\nM-bias & 0.000 & 0.000 & 0.095 & 0.099 \\\\\nFront-door & 0.000 & 0.000 & 0.590 & 0.579 \\\\\nIV & 0.086 & 0.074 & 0.086 & 0.560 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{center}\n\nTreatment-effect sign-flip rates (SF$_\\tau$) are zero for all five guaranteed topologies under both linear and logistic DGPs, and differ by $< 0.02$ for IV. The SF$_\\text{any}$ discrepancy for IV reflects estimator dimensionality: the control function includes a residual coefficient prone to sign noise; the core comparison is SF$_\\tau$, where both estimators agree. Linear and logistic DGPs produce virtually identical sign-flip patterns across all seven topologies ($|\\Delta\\,\\text{SF}_\\tau| < 0.02$). Under logistic DGP, bias is measured in log-odds units; directional conclusions (sign preservation, topology ranking) transfer directly, while magnitudes are not directly comparable to linear plim expressions. For practitioners requiring finite-sample inference under logistic DGP, bias-corrected bootstrap provides a nonparametric alternative that bypasses the linear plim framework.\n\n\\subsection{Bootstrap Uncertainty of ASV}\n\\label{sec:bootstrap_asv}\n\nWe assess confusion-matrix estimation uncertainty by bootstrapping label pairs from HumAID DeepSeek zero-shot ($K{=}10$, $n{=}1{,}500$): resample with replacement $B{=}1{,}000$ times, re-estimate $C_0$, and recompute magnitude ASV $\\delta^*$ at a 10\\% bias threshold.\n\n\\begin{center}\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lccc}\n\\toprule\nTopology & $\\delta^*$ (point) & 95\\% CI & Valid / 1000 \\\\\n\\midrule\nConfounding & --- & --- & 0 \\\\\nExposure & 0.937 & [0.602, 1.363] & 907 \\\\\nIV & 0.754 & [0.435, 1.290] & 902 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{center}\n\nConfounding never reaches the 10\\% threshold across all 1{,}000 bootstraps, confirming robustness. For IV, the 95\\% CI spans a $3{\\times}$ range (0.435 to 1.290); practitioners should bootstrap $C_0$ rather than rely on a point estimate when ASV is near the decision boundary. CI width scales as $O(1/\\sqrt{n})$ where $n$ is the gold-label validation set size; at $n{=}1{,}500$, IV CIs are ${\\sim}3{\\times}$ wider than exposure CIs, reflecting the Wald estimator's denominator instability. A convergence study ($K{=}3$, $B{=}1{,}000$) confirms this scaling: exposure CI width narrows from 0.60 ($n{=}500$) to 0.05 ($n{=}50{,}000$), and IV from 0.52 to 0.04, with the product $\\text{width} \\times \\sqrt{n}$ approximately constant (CV $< 0.20$).\n\n\\begin{figure*}[ht!]\n\\centering\n\\includegraphics[width=\\textwidth]{exp_c_bootstrap_figure.pdf}\n\\caption{Bootstrap distribution of magnitude ASV $\\delta^*$ ($B{=}1{,}000$) for HumAID DeepSeek zero-shot ($K{=}10$). Dashed line: point estimate; shaded: 95\\% CI.}\n\\label{fig:bootstrap_asv}\n\\end{figure*}\n\n\\subsection{Cross-$K$ Robustness}\n\\label{sec:cross_k_robustness}\n\nAll structural patterns persist at $K{=}5,7$ (100{,}000 matrices each): sign-flip guarantees hold for the same five topologies, and IV sign-flip rates remain within 51--53\\%.\n\n\\subsection{ASV Diagnostic Results}\n\\label{sec:asv_diagnostics}\n\nFor HumAID ($K{=}10$, 56 scenarios), 55.4\\% are flagged as magnitude-ASV-unsafe: IV, mediation, front-door, and exposure all trigger, while confounding, collider, and M-bias remain below 10\\% bias (Figure~\\ref{fig:asv_heatmap}). For CivilComments ($K{=}2$), 100\\% of scenarios are ASV-unsafe despite $F_1$ ranging from $0.69$ (7B) to $0.82$ (frontier).\n\nOverlaying all 23 empirical matrices onto the theoretical Dirichlet violation-rate curves (Figure~\\ref{fig:dirichlet_overlay}) confirms placement: VAST in the danger zone, HumAID mid-range, CivilComments approaching safe for exposure but still in IV amplification.\n\n\\subsection{ASV Stability Across DGP Parameters}\n\\label{sec:asv_stability}\n\nWe test whether ASV rankings are stable across different data-generating process (DGP) configurations by varying the treatment-effect vector $\\boldsymbol{\\beta}$ across three settings: alternating-large ($\\boldsymbol{\\beta}=[0,\\,1.0,\\,-0.5]$), same-sign ($\\boldsymbol{\\beta}=[0,\\,0.5,\\,0.3]$), and alternating-small ($\\boldsymbol{\\beta}=[0,\\,0.2,\\,-0.1]$), with $K{=}3$, $\\tau{=}0.5$, and five $C_0$ diagonal values $\\in\\{0.5,0.6,0.7,0.8,0.9\\}$.\n\n\\input{exp_e_asv_stability_table.tex}\n\nThree patterns emerge (Table~\\ref{tab:asv_stability}). First, IV magnitude ASV is identical across all three DGPs ($\\delta^*{=}0.203$). This is a mathematical identity, not an empirical finding: the Wald estimator $\\hat{\\tau}_{\\text{IV}} = \\text{RF}/\\text{FS}$ has $\\boldsymbol{\\beta}$ in both numerator and denominator, and the ratio depends only on $C$ and the first-stage structure, making ASV invariant to $\\boldsymbol{\\beta}$ by construction. Second, exposure ASV depends on the coefficient ratio structure: alternating-large ($\\beta_2/\\beta_1 = -0.5$) and alternating-small ($\\beta_2/\\beta_1 = -0.5$) share the same ratio and yield identical $\\delta^*{=}0.090$, while same-sign ($\\beta_2/\\beta_1 = 0.6$) gives $\\delta^*{=}0.223$; thus the experiment provides two distinct sign-structure conditions, not three. Third, confounding ASV depends on effect magnitudes: only alternating-large triggers the 10\\% threshold ($\\delta^*{=}0.348$); smaller effects never reach 10\\% bias.\n\nConfounding is consistently the most robust topology (highest ASV or no violation), and M-bias remains immune (not shown). However, the relative fragility of exposure vs.\\ IV inverts with coefficient sign structure: under alternating signs, exposure is most fragile ($0.090 < 0.203$); under same-sign effects, IV is most fragile ($0.203 < 0.223$). Practitioners should compute ASV with their specific DGP rather than relying on generic rankings.\n\n\\subsection{Extended Conjecture Verification}\n\\label{sec:conjecture_verify}\n\nWe test envelope monotonicity (Conjecture~\\ref{conj:monotone}) by sampling 10{,}000 random $C_0$ matrices from Dirichlet$(1,\\dots,1)$ per topology for $K \\in \\{3,5,7\\}$ (210{,}000 total), sweeping $\\delta$ in steps of 0.01, and counting matrices with at least one non-monotonic step exceeding tolerance $10^{-12}$. Bias at each $\\delta$ is computed via analytic probability limits using Gauss--Hermite quadrature (100 points), eliminating sampling noise entirely.\n\nThe $\\delta$ step size is 0.01. ``Worst mag.''\\ is the largest single-step deviation $|B(\\delta_{i+1})|-|B(\\delta_i)|$ in the non-monotonic direction. $^*$100{,}000 matrices at step $= 0.005$ yield exposure $\\varepsilon = 0.075$.\n\n\\begin{table}[H]\n\\centering\n\\caption{Envelope monotonicity violations per 10{,}000 random $C_0$ matrices.}\n\\label{tab:conjecture_verify}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Topology} & $K{=}3$ & $K{=}5$ & $K{=}7$ & \\textbf{Worst mag.} & \\textbf{Direction} \\\\\n\\midrule\nConfounding & 8467 & 8063 & 7892 & 0.011 & non-dec \\\\\nMediation   & 8236 & 7905 & 7893 & 0.013 & non-dec \\\\\nCollider    & 8683 & 7669 & 7570 & 0.005 & non-inc \\\\\nExposure    & 485  & 205  & 77   & 0.056$^*$ & non-dec \\\\\nM-bias      & 9791 & 7783 & 7399 & 0.002 & non-inc \\\\\nIV          & 7433 & 6015 & 5711 & $>10^6$ & non-dec \\\\\nFront-door  & 8429 & 8079 & 7899 & 0.013 & non-dec \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nViolation counts are high (60--97\\% of matrices), but magnitudes are small for non-IV topologies under the default parameterization (Table~\\ref{tab:conjecture_verify}); DGP sensitivity analysis (Table~\\ref{tab:dgp_sensitivity}) shows $\\varepsilon$ scales with effect magnitude $|\\beta|$, remaining below 0.02 for $|\\beta| \\leq 1$ across non-exposure topologies. These results are computed from analytic probability limits with zero sampling noise, confirming the violations are structural properties of multi-class confusion matrices rather than numerical artifacts. IV deviations reflect Wald estimator singularities when the first-stage coefficient passes near zero; this is a property of the Wald estimator, not of the ASV parameterization. Adversarial search (500 restarts per configuration, $K \\in \\{3,5\\}$) finds genuine counterexamples for all topologies except IV $K{=}3$, confirming that strict monotonicity does not hold universally. The bias envelope is $\\varepsilon$-approximately monotonic with $\\varepsilon < 0.03$ for collider and M-bias across all tested $\\tau$; confounding, mediation, and front-door achieve $\\varepsilon < 0.06$ at default DGP parameters (see DGP sensitivity below); exposure satisfies $\\varepsilon_{p99} < 0.008$ but extreme-tail matrices ($<$0.02\\% of draws) reach $\\varepsilon \\approx 0.15$. Empirically, $\\varepsilon$ scales as $O(1/K^\\alpha)$ with $\\alpha \\in [0.6, 1.5]$ (topology-dependent): for confounding, mediation, and front-door, $\\alpha \\approx 1.4$; for exposure, $\\alpha \\approx 1.0$; for collider and M-bias, $\\alpha \\approx 0.7$. A universal empirical upper bound is $\\varepsilon \\leq 0.137/\\sqrt{K}$, verified across all tested configurations ($K \\in \\{3,5,7\\}$). This scaling supports the practical validity of ASV as a sensitivity tool at any meaningful bias threshold.\n\n\\paragraph{DGP parameter sensitivity.}\nWe repeat the verification across $\\tau \\in \\{0.1, 0.5, 1.0, 2.0, 5.0\\}$, varying the direct $T{\\to}Y$ coefficient for confounding ($\\beta_T{=}\\tau$), mediation, collider, and M-bias (DGP $\\tau$), and rescaling the $A{\\to}Y$ coefficient vector to $\\boldsymbol{\\beta}\\cdot\\tau$ for exposure and front-door. With 10{,}000 random $C_0$ per $(K,\\tau)$ setting (Table~\\ref{tab:conjecture_tau_sens}), $\\varepsilon$ remains small ($< 0.03$) for $\\tau \\geq 0.5$ for confounding, mediation, collider, and M-bias, but grows at $\\tau{=}0.1$: mediation produces 1{,}950 / 30{,}000 violations across $K \\in \\{3,5,7\\}$ (worst $\\varepsilon{=}0.130$ at $K{=}3$) and confounding 200 / 30{,}000 (worst $\\varepsilon{=}0.118$ at $K{=}3$). The mechanism is dimensional: additive terms not scaling with $\\tau$ (e.g.\\ the $\\boldsymbol{\\beta}$-contribution to $\\mathbb{E}[Y D_k]$ in mediation and confounding) contribute a $\\tau$-independent offset to the bias numerator, so the ratio $|B|/|\\tau|$ inflates as $\\tau \\to 0$. A single mediation violation at $\\tau{=}2.0$ ($\\varepsilon{=}0.112$, 1/30{,}000 matrices) arises from a specific confusion matrix structure where off-diagonal entries induce partial cancellation along the mediation pathway; this isolated case does not affect the $p_{99}$ bound ($\\varepsilon_{p99}{=}0.005$). Collider and M-bias remain robust at all $\\tau$ ($\\varepsilon{<}0.022$ and $\\varepsilon{<}0.015$ respectively). Exposure shows scattered tail outliers but $\\overline{\\varepsilon} \\approx 3\\!\\times\\!10^{-4}$ at every $\\tau$, consistent with linear scaling: when $\\boldsymbol{\\beta}$ rescales by $\\tau$, both bias and $\\tau_{\\text{true}}$ scale by the same factor and $\\varepsilon$ is theoretically invariant. Front-door inverts the pattern ($\\varepsilon$ grows with $\\tau$, reaching $0.139$ at $\\tau{=}5$, $K{=}3$, with 664 violations) because $\\tau_{\\text{true}} = \\operatorname{plim}(\\hat{\\tau}_T \\mid C{=}I)$ is pinned at $0.5$ by the $U$-confounding path while bias magnitudes scale with $\\boldsymbol{\\beta}$; this is an artefact of how $\\tau_{\\text{true}}$ is normalised, not a genuine failure of envelope monotonicity. In practice, ASV's $\\delta^*$ thresholds (typically $\\geq 0.1$ in our deployment) are well above the region where these $\\varepsilon$-violations occur, so the small-$\\tau$ degradation does not affect ASV's operational reliability; we flag it as a caveat for applications targeting $|\\tau| \\lesssim 0.1$ in standardised units.\n\n$\\varepsilon \\equiv \\max_\\delta(|B(\\delta{+}\\Delta)|{-}|B(\\delta)|)/|\\tau_{\\text{true}}|$ in the non-monotonic direction, taking the max over $K \\in \\{3,5,7\\}$ with 10{,}000 random $C_0$ per cell. Bold marks $\\varepsilon > 0.02$ (non-exposure) or $\\varepsilon > 0.08$ (exposure). Counts in parentheses are violations / 30{,}000. Tables~\\ref{tab:conjecture_verify} and~\\ref{tab:conjecture_tau_sens} use independent random seeds; for topologies with low violation rates (exposure $<$0.02\\%), the worst-case $\\varepsilon$ is sample-sensitive.\n\n\\begin{table}[H]\n\\centering\n\\caption{DGP parameter sensitivity of envelope monotonicity violations.}\n\\label{tab:conjecture_tau_sens}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Topology} & $\\tau{=}0.1$ & $\\tau{=}0.5$ & $\\tau{=}1.0$ & $\\tau{=}2.0$ & $\\tau{=}5.0$ \\\\\n\\midrule\nConfounding & \\textbf{0.118} (200) & 0.027 (0) & 0.014 (0) & 0.007 (0) & 0.002 (0) \\\\\nMediation   & \\textbf{0.130} (1950) & 0.026 (0) & 0.013 (0) & \\textbf{0.112} (1) & 0.003 (0) \\\\\nCollider    & 0.022 (0) & 0.006 (0) & 0.005 (0) & 0.004 (0) & 0.002 (0) \\\\\nExposure    & \\textbf{0.111} (5) & \\textbf{0.122} (2) & \\textbf{0.152} (2) & \\textbf{0.089} (3) & \\textbf{0.148} (3) \\\\\nM-bias      & 0.014 (0) & 0.003 (0) & 0.001 (0) & 0.001 (0) & 0.000 (0) \\\\\nFront-door  & 0.003 (0) & 0.013 (0) & 0.027 (0) & 0.051 (0) & \\textbf{0.139} (664) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Effect-magnitude sensitivity.}\nWe further vary the direct effect $\\beta \\in \\{0.1, 0.5, 1.0, 2.0, 5.0\\}$ and noise variance $\\sigma^2 \\in \\{0.5, 1.0, 2.0\\}$ across all seven topologies ($K{=}3$, 10{,}000 Dirichlet$(1,\\ldots,1)$ matrices per cell). Table~\\ref{tab:dgp_sensitivity} reports the worst-case relative envelope deviation $\\varepsilon_{\\text{rel}}$. For non-exposure topologies, $\\varepsilon$ scales approximately linearly with $|\\beta|$; the safe/fragile partition is stable across all 105 cells.\n\n\\input{conjecture_dgp_sensitivity_table.tex}\n\n\\subsection{Proportional Effects Breakdown}\n\\label{sec:proportional_effects}\n\nTheorem~\\ref{thm:monotone} requires proportional effects ($f = \\lambda g$); here we quantify how $\\lambda(C)$ out-of-bounds (OOB) rates depend on the degree of departure from proportionality. We simulate $K{=}3$ mediation with 100{,}000 random confusion matrices (diagonal $\\geq 0.5$, Dirichlet off-diagonal) at five proportionality degrees: exact ($f_j {-} f_0 = \\lambda(g_j {-} g_0)$), near-proportional ($f = \\lambda g + \\epsilon$, $\\epsilon \\sim \\mathcal{N}(0,\\sigma^2)$, $\\sigma \\in \\{0.1, 0.3, 0.5\\}$), and fully independent ($f \\perp g$). Table~\\ref{tab:proportional_effects} reports the $\\lambda(C) \\notin [0,1]$ rate.\n\nResults use $K{=}3$ with 100K random confusion matrices per row.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\caption{$\\lambda(C)$ out-of-bounds rate and mediation sign failure rate.}",
      "numLines": 300,
      "startLine": 900,
      "totalLines": 1554
    }
  },
  "sourceToolAssistantUUID": "e2dc0199-b50a-4b19-bc1c-ac15b0f765c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-25T08:23:49.787Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DWRkSULfo31MpNp7ifuFWv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "offset": 1200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9424c6e1-def5-4784-8378-34a1746e75d9",
  "isSidechain": false,
  "requestId": "req_011CbNxwjDyqXzXDx3aNXCQc",
  "type": "assistant",
  "uuid": "46a41073-9cb7-4170-b316-9e02ebb63d3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EE2Xrimc1remnUVpugVqZ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31975,
      "cache_read_input_tokens": 64523,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 64523,
          "cache_creation_input_tokens": 31975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31975
          },
          "type": "message"
        }
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

_source line 65 · 2026-05-25T08:23:49.793Z_

<details><summary>↩ Tool result · `toolu_01DWRkSULfo31MpNp7ifuFWv`</summary>

```text
1200	\label{tab:proportional_effects}
1201	\resizebox{\columnwidth}{!}{\begin{tabular}{lcc}
1202	\toprule
1203	\textbf{Proportionality degree} & $\lambda(C) \notin [0,1]$ & Sign failure \\
1204	\midrule
1205	Exact ($\sigma{=}0$) & 0.0\% & 0.85\% \\
1206	Near ($\sigma{=}0.1$) & 10.3\% & 0.87\% \\
1207	Near ($\sigma{=}0.3$) & 19.0\% & 0.96\% \\
1208	Near ($\sigma{=}0.5$) & 22.4\% & 0.93\% \\
1209	Independent ($f \perp g$) & 22.9\% & 0.17\% \\
1210	\midrule
1211	NLP-realistic DGP & 0.07\% & 0.0\% \\
1212	\bottomrule
1213	\end{tabular}}
1214	\end{table}
1215	
1216	The $\lambda$ OOB rate rises steeply from 0\% to ${\sim}10$\% at $\sigma{=}0.1$ and saturates near 23\% for independent $(f,g)$. Sign failure rates remain below 1\% across all conditions because $\lambda$ excursions outside $[0,1]$ are typically small and do not reverse the dominant effect direction. The NLP-realistic DGP ($\delta{=}[0, 0.8, {-}0.6]$, $\beta{=}[0, 1.0, {-}0.5]$) exhibits near-zero OOB (0.07\%) and zero sign failures, confirming that proportional effects hold approximately in practice.
1217	
1218	\subsection{FWL Invariance Under Nonlinear Models}
1219	\label{sec:fwl_nonlinear}
1220	
1221	FWL invariance guarantees exactly 0\% bias reduction from matrix-based corrections (MLA, naive plug-in) under linear OLS for covariate topologies (confounding, mediation, collider, M-bias). Here we test whether this invariance persists under logistic regression across sample sizes $N \in \{1000, 5000, 10{,}000, 50{,}000\}$ and three error levels ($C_{kk} \in \{0.9, 0.7, 0.5\}$), with 200 Monte Carlo replicates per cell. Table~\ref{tab:fwl_nonlinear} reports the mean logistic bias reduction (positive = correction helps).
1222	
1223	Results are averaged over $N \in \{1K, 5K, 10K, 50K\}$ with 200 MC reps each. Under linear OLS, all covariate topologies yield exactly 0\%. Exposure is shown for comparison.
1224	
1225	\begin{table}[H]
1226	\centering
1227	\small
1228	\caption{Mean logistic bias reduction (\%) from matrix-based correction.}
1229	\label{tab:fwl_nonlinear}
1230	\resizebox{\columnwidth}{!}{\begin{tabular}{lccc}
1231	\toprule
1232	\textbf{Topology} & \textbf{Low} ($C_{kk}{=}0.9$) & \textbf{Med} ($C_{kk}{=}0.7$) & \textbf{High} ($C_{kk}{=}0.5$) \\
1233	\midrule
1234	Confounding & $-$0.003\% & $<$0.001\% & $<$0.001\% \\
1235	Mediation & $-$0.004\% & $<$0.001\% & $<$0.001\% \\
1236	Collider & $-$0.033\% & $-$0.020\% & $<$0.001\% \\
1237	M-bias & $-$0.049\% & $-$0.010\% & $<$0.001\% \\
1238	Front-door & 0.001\% & $-$0.001\% & $<$0.001\% \\
1239	\midrule
1240	Exposure & $-$68.5\% & $-$48.7\% & $-$22.5\% \\
1241	\bottomrule
1242	\end{tabular}}
1243	\end{table}
1244	
1245	For all five covariate topologies, logistic bias reduction is negligible ($|$mean$| < 0.05\%$) across all $N$ and error levels, with no systematic $N$-scaling: medians cluster within $\pm 0.002\%$ at $N{=}50{,}000$. The large standard deviations observed at certain $(N, \text{error})$ cells for collider and M-bias (up to 2.6\% std at $N{=}10{,}000$) reflect rare outlier replicates; medians remain near zero. This confirms that FWL invariance is a robust structural property that extends beyond linear models for covariate topologies.
1246	
1247	In contrast, exposure shows substantial FWL breakdown under logistic regression: $-$22\% to $-$78\% bias reduction (negative = correction worsens bias), stabilising at $N \geq 5{,}000$. The breakdown magnitude increases with accuracy ($C_{kk}$), consistent with the exposure topology's sensitivity to the nonlinear link function transforming category weights.
1248	
1249	\subsection{PPI++ Gold Label Ratio Sensitivity}
1250	\label{sec:ppi_gold_ratio}
1251	
1252	We test PPI++ correction performance as a function of gold label fraction ($K{=}3$, $N{=}10{,}000$, 100 MC replications, 5 Dirichlet confusion matrices with $\min_k C_{kk}{\geq}0.6$).
1253	
1254	Negative values indicate PPI++ increases RMSE relative to the naive estimator.
1255	
1256	\begin{table}[H]
1257	\centering
1258	\caption{PPI++ RMSE reduction (\%) vs.\ gold label fraction.}
1259	\label{tab:ppi_gold_ratio}
1260	\resizebox{\columnwidth}{!}{\begin{tabular}{lccccc}
1261	\toprule
1262	Topology & 5\% & 10\% & 20\% & 50\% & 100\% \\
1263	\midrule
1264	Confounding & $+$84.8 & $+$88.6 & $+$91.8 & $+$94.2 & $+$95.2 \\
1265	Exposure & $+$75.2 & $+$83.1 & $+$87.1 & $+$91.2 & $+$93.8 \\
1266	Mediation & $+$56.7 & $+$70.4 & $+$77.2 & $+$85.3 & $+$88.7 \\
1267	IV & $+$1.4 & $+$22.1 & $+$50.1 & $+$66.7 & $+$76.4 \\
1268	M-bias & $-$125.3 & $-$43.6 & $-$19.6 & $+$6.0 & $+$18.5 \\
1269	\bottomrule
1270	\end{tabular}}
1271	\end{table}
1272	
1273	For confounding and exposure, PPI++ achieves $>$75\% RMSE reduction even at 5\% gold labels; IV requires ${\geq}20\%$ gold to reach 50\% reduction, reflecting the Wald estimator's higher variance. M-bias exhibits harmful correction at ${\leq}20\%$ gold ($-125\%$ at 5\%), because PPI++ re-exposes the M-bias pathway that annotation error had attenuated; only at ${\geq}50\%$ gold does the estimator become weakly beneficial ($+6\%$).
1274	
1275	\subsection{Realistic Differential Misclassification Thresholds}
1276	\label{sec:realistic_epsilon}
1277	
1278	Our non-differential assumption (Definition~\ref{def:nondiff}) requires $P(A^*{\mid}A,Y) = P(A^*{\mid}A)$. We estimate how much $Y$-stratified differential error each of our 23 empirical LLM confusion matrices can tolerate before exposure sign reversal exceeds 5\%. For each matrix $C$, we construct $C_{\text{high}} = \text{renorm}(C + \varepsilon\Delta)$ and $C_{\text{low}} = \text{renorm}(C - \varepsilon\Delta)$ with random off-diagonal perturbation $\Delta$ (500 MC trials per $\varepsilon$), sweep $\varepsilon \in [0, 0.50]$, and report the safe threshold $\varepsilon^*_{\text{safe}} = \max\{\varepsilon : \text{reversal rate} < 5\%\}$ (Table~\ref{tab:realistic_epsilon}).
1279	
1280	For $K{=}2$ (binary), no configuration produces sign reversal up to $\varepsilon{=}0.50$. For $K{\geq}3$, the majority of configurations are fragile ($\varepsilon^*_{\text{safe}}{=}0$), confirming that the non-differential assumption is load-bearing for multi-class exposure.
1281	
1282	\begin{table}[H]
1283	\centering
1284	\caption{Safe differential misclassification thresholds $\varepsilon^*_{\text{safe}}$ by dataset/$K$.}
1285	\label{tab:realistic_epsilon}
1286	\resizebox{\columnwidth}{!}{\begin{tabular}{lccccc}
1287	\toprule
1288	\textbf{Dataset} & $K$ & $n$ & \textbf{Mean} $\varepsilon^*$ & \textbf{Median} $\varepsilon^*$ & $\varepsilon^*{=}0$ \\
1289	\midrule
1290	Civil Comments & 2 & 7 & 0.50 & 0.50 & 0/7 \\
1291	VAST & 3 & 8 & 0.003 & 0.00 & 7/8 \\
1292	HuMAID & 10 & 8 & 0.045 & 0.00 & 7/8 \\
1293	\bottomrule
1294	\end{tabular}}
1295	\end{table}
1296	
1297	The distribution is sharply bimodal: all $K{=}2$ configurations are immune to differential misclassification within the tested range ($\varepsilon^*_{\text{safe}}{=}0.50$), consistent with the binary sign-preservation guarantee (Proposition~\ref{prop:signflip}(c)). For $K{\geq}3$, 14 of 16 configurations have $\varepsilon^*_{\text{safe}}{=}0$: sign reversal occurs at the smallest tested $\varepsilon{=}0.01$. Two outliers (VAST: $\varepsilon^*{=}0.02$; HuMAID: $\varepsilon^*{=}0.36$) have atypically structured confusion matrices. This confirms that even small violations of non-differential misclassification are consequential for multi-class exposure, underscoring the practical importance of validating $P(A^*{\mid}A,Y) \approx P(A^*{\mid}A)$ on gold-labeled subsets when $K \geq 3$.
1298	
1299	\subsection{Proportional Effects with Empirical Confusion Matrices}
1300	\label{sec:proportional_real_matrices}
1301	
1302	Theorem~\ref{thm:monotone} assumes proportional effects ($f = \lambda g$). We evaluate this assumption using all 23 empirical LLM confusion matrices under four DGP groups in the mediation topology (23 matrices $\times$ 50 seeds $\times$ 100{,}000 precomputed samples per seed).
1303	
1304	Evaluation uses the mediation DGP. $\lambda(C) \in [0,1]$: proportion satisfying the Theorem~\ref{thm:monotone} bound. Sign pres.: sign preservation rate of the direct effect estimate.
1305	
1306	\begin{table}[H]
1307	\centering
1308	\small
1309	\caption{Proportional effects validation with 23 real LLM confusion matrices.}
1310	\label{tab:proportional_empirical}
1311	\resizebox{\columnwidth}{!}{\begin{tabular}{lcccc}
1312	\toprule
1313	\textbf{DGP Group} & $\lambda(C)$ \textbf{mean} & $\lambda(C) \in [0,1]$ & \textbf{Sign pres.} & \textbf{CV} \\
1314	\midrule
1315	Proportional ($f{=}\lambda g$) & 0.271 & 99.8\% & 100\% & 0.00 \\
1316	Near-prop.\ ($\sigma{=}0.1$) & 0.285 & 99.2\% & 100\% & 1.06 \\
1317	Non-proportional & 0.240 & 85.0\% & 97.3\% & 3.60 \\
1318	Sparse & 0.296 & 75.8\% & 98.6\% & 6.59 \\
1319	\bottomrule
1320	\end{tabular}}
1321	\end{table}
1322	
1323	Under proportional and near-proportional effects, $\lambda(C)$ remains within $[0,1]$ for ${\geq}99\%$ of configurations with 100\% sign preservation: the Theorem~\ref{thm:monotone} conditions are satisfied by real LLM confusion matrices. Even under non-proportional effects ($f$ independent of $g$), sign preservation remains at 97.3\%, with $\lambda(C)$ exceeding $[0,1]$ in 15\% of cases. The per-$K$ breakdown shows that $\lambda(C)$ is dimension-dependent: $K{=}2$ (mean 0.249), $K{=}3$ (mean 0.082), $K{=}10$ (mean 0.490), with 100\% in $[0,1]$ across all $K$ under proportional effects. Sparse DGP (zero-effect categories) produces the highest violation rate (24.2\%), consistent with the breakdown mechanism: zero-effect categories make $f/g$ ratios undefined, maximally departing from proportionality.
1324	
1325	\subsection{Case Study: ASV Diagnosis of Political Ad Tone Classification}
1326	\label{sec:asv_case_study}
1327	
1328	We illustrate the ASV diagnostic workflow on a concrete CSS application. \citet{egami_hinck_stewart_wei2023} use LLM classifiers to annotate political advertising tone ($K{=}3$: promote/contrast/attack) from the Fowler \& Ridout database, then estimate the causal effect of ad tone on voter outcomes. The annotated variable is the \textbf{exposure} (treatment). Using a representative $K{=}3$ confusion matrix from our empirical set (VAST DeepSeek zero-shot, mean diagonal 0.734) as a proxy:
1329	
1330	\begin{center}
1331	\small
1332	\resizebox{\columnwidth}{!}{\begin{tabular}{lccc}
1333	\toprule
1334	Coefficient & $\delta^*_{\text{mag}}$ (10\%) & $\delta^*_{\text{sf}}$ & Relative bias at $\delta{=}1$ \\
1335	\midrule
1336	$\beta_1$ (primary) & 0.234 & $> 1.5$ & 39.7\% \\
1337	$\beta_2$ (secondary) & 0.154 & $> 1.5$ & 60.4\% \\
1338	\bottomrule
1339	\end{tabular}}
1340	\end{center}
1341	
1342	Both coefficients are magnitude-unsafe ($\delta^* < 1$), with the secondary coefficient more fragile ($\delta^*{=}0.154$). If the same annotator were instead classifying a \textbf{confounder} (e.g., media framing as a control variable), magnitude ASV rises to $\delta^*{=}0.690$, a $3{\times}$ increase in error tolerance from the same confusion matrix. This demonstrates the central insight: topology, not annotator quality, determines vulnerability. Algorithm~\ref{alg:correction} routes this exposure topology to PPI++ or DSL correction; matrix-based methods (naive plug-in, MLA) are ineffective due to FWL non-applicability.
1343	
1344	\subsection{End-to-End Demonstration}
1345	\label{sec:e2e_demo}
1346	
1347	\input{e2e_demo_table.tex}
1348	
1349	The demonstration uses a symmetric $C_0$ ($d_{\mathrm{rel}}{=}0$); empirical $K{=}3$ matrices deviate substantially (median $d_{\mathrm{rel}}{=}0.33$, Remark~\ref{rem:symmetry}), but core ASV ranking and correction routing remain valid under Conjecture~\ref{conj:monotone}.
1350	
1351	\subsection{Semi-Real Case Study with Production LLM Confusion Matrices}
1352	\label{sec:real_cm_demo}
1353	
1354	We repeat the end-to-end pipeline using 10 confusion matrices estimated from production LLM annotation of VAST stance detection ($K{=}3$; DeepSeek, Llama4, Qwen2.5-7B, Qwen3 under zero-shot and few-shot prompting). These matrices exhibit median $d_{\mathrm{rel}}{=}0.33$ (Remark~\ref{rem:symmetry}), far from the symmetric assumption of Theorem~\ref{thm:k3_symmetric}. Results confirm both topology-dependent patterns: PPI++ achieves 93.6\% median exposure bias reduction while plug-in corrections yield 0\% improvement for confounding (FWL invariance, machine precision; Table~\ref{tab:e2e-real-cm}).
1355	
1356	\input{e2e_real_cm_table.tex}
1357	
1358	\subsection{Correction Method Sensitivity to $K$}
1359	\label{sec:correction_k_sensitivity}
1360	
1361	We test whether the correction method ranking from Table~\ref{tab:correction} ($K{=}3$) is stable at $K{=}5$ and $K{=}10$. For each $K$, we sample 5 random Dirichlet confusion matrices (diagonal $\geq 0.6$), run 100 MC replications per topology--matrix combination ($N{=}5{,}000$, 10\% gold fraction), and compute RMSE reduction for all five methods across all seven topologies.
1362	
1363	\paragraph{Grand ranking stability.}
1364	Spearman rank correlations across all topology--method pairs: $\rho_{3,5} = 0.80$, $\rho_{3,10} = 0.84$, $\rho_{5,10} = 0.93$ (all $p < 10^{-8}$). Per-topology correlations are even stronger: 5 of 7 topologies (confounding, collider, M-bias, IV, and exposure at $K{=}10$) achieve $\rho = 1.0$ between $K{=}3$ and $K{=}10$.
1365	
1366	\paragraph{Method-specific patterns.}
1367	PPI++ effectiveness degrades with $K$: confounding RMSE reduction drops from 85.6\% ($K{=}3$) to 75.6\% ($K{=}10$); mediation drops from 57.1\% to 9.0\%. At $K{=}10$, PPI++ becomes harmful for IV ($-124\%$) and exposure ($-11\%$). MC-SIMEX is the most $K$-robust method, maintaining the top rank for 5/7 topologies at $K{=}10$ (vs.\ 3/7 at $K{=}3$). FWL invariance (naive plug-in and MLA achieving 0\% bias reduction on the treatment coefficient) holds at all $K$ tested, confirming the structural nature of this result.
1368	
1369	Bold indicates the top method for that topology--$K$ combination.
1370	
1371	\begin{table}[H]
1372	\centering
1373	\small
1374	\caption{Top correction method and RMSE reduction (\%) by topology across $K$.}
1375	\label{tab:correction_k}
1376	\resizebox{\columnwidth}{!}{\begin{tabular}{lccc}
1377	\toprule
1378	\textbf{Topology} & $K{=}3$ & $K{=}5$ & $K{=}10$ \\
1379	\midrule
1380	Confounding & \textbf{PPI++} 85.6 & \textbf{PPI++} 76.4 & \textbf{PPI++} 75.6 \\
1381	Mediation & \textbf{PPI++} 57.1 & \textbf{SIMEX} 59.7 & \textbf{SIMEX} 59.0 \\
1382	Collider & \textbf{SIMEX} 55.4 & \textbf{SIMEX} 63.4 & \textbf{SIMEX} 57.3 \\
1383	Exposure & \textbf{SIMEX} 72.5 & \textbf{SIMEX} 65.0 & \textbf{SIMEX} 47.3 \\
1384	M-bias & \textbf{SIMEX} 3.2 & \textbf{SIMEX} 47.0 & \textbf{SIMEX} 43.7 \\
1385	IV & \textbf{SIMEX} 30.9 & \textbf{SIMEX} 30.4 & \textbf{SIMEX} 27.1 \\
1386	Front-door & \textbf{PPI++} 82.9 & \textbf{PPI++} 69.0 & \textbf{SIMEX} 70.1 \\
1387	\bottomrule
1388	\end{tabular}}
1389	\end{table}
1390	
1391	\subsection{Comparison with Related Sensitivity Frameworks}
1392	\label{sec:sensitivity_comparison}
1393	
1394	\begin{table}[H]
1395	\centering
1396	\caption{Comparison of sensitivity frameworks.}
1397	\label{tab:sensitivity_comparison}
1398	\resizebox{\columnwidth}{!}{\begin{tabular}{lccc}
1399	\toprule
1400	& \textbf{ASV} & \textbf{E-value} & \textbf{Partial} $R^2$ \\
1401	\midrule
1402	Parameter space & $K{\times}K$ confusion $C(\delta)$ & Scalar confounder & $R^2$ of omitted var \\
1403	Sensitivity path & $(1{-}\delta)I + \delta C_0$ & Monotone scalar & Monotone scalar \\
1404	Topology-specific & \checkmark & \ding{55} & \ding{55} \\
1405	Sign-flip diagnostic & \checkmark ($\delta^*_{\text{sign}}$) & \ding{55} & \ding{55} \\
1406	Topology dependence & \checkmark (7 topologies ranked) & \ding{55} & \ding{55} \\
1407	Monotonicity & Proved $K{=}2$; conj.\ $K{\geq}3$ & Guaranteed & Guaranteed \\
1408	Target & Annotation error & Unmeasured confounding & Omitted variable \\
1409	\bottomrule
1410	\end{tabular}}
1411	\end{table}
1412	
1413	\subsection{Per-Topology $F_1$--Bias Correlation}
1414	\label{sec:within_topo_f1}
1415	
1416	The cross-topology correlation between macro $F_1$ and $|\text{bias}|$ is weak ($\rho = -0.10$, $p = 0.45$; \S\ref{sec:empirical}), but decomposing by topology reveals a structured pattern. Table~\ref{tab:within_topo_f1} reports Spearman correlations computed over 23 LLM configurations (HumAID $K{=}10$, VAST $K{=}3$, CivilComments $K{=}2$; 161 total scenarios).
1417	
1418	Correlations are computed over 23 empirical LLM configurations $\times$ 3 datasets. Negative $\rho$: higher $F_1$ $\to$ lower bias (expected). Positive $\rho$: higher $F_1$ $\to$ higher bias (protective attenuation removed).
1419	
1420	\begin{table}[H]
1421	\centering
1422	\small
1423	\caption{Within-topology Spearman $\rho(F_1, |\text{bias}|)$ across LLM configurations.}
1424	\label{tab:within_topo_f1}
1425	\begin{tabular}{lccc}
1426	\toprule
1427	\textbf{Topology} & $n$ & $\rho$ & $p$ \\
1428	\midrule
1429	Confounding & 23 & $-0.557$ & 0.006 \\
1430	Mediation & 23 & $-0.565$ & 0.005 \\
1431	Exposure & 23 & $-0.531$ & 0.009 \\
1432	Front-door & 23 & $-0.568$ & 0.005 \\
1433	IV & 23 & $-0.700$ & $<$0.001 \\
1434	Collider & 23 & $+0.310$ & 0.150 \\
1435	M-bias & 23 & $+0.867$ & $<$0.001 \\
1436	\bottomrule
1437	\end{tabular}
1438	\end{table}
1439	
1440	Five topologies show the expected negative correlation: better annotation quality ($F_1{\uparrow}$) reduces causal bias. IV shows the strongest effect ($\rho = -0.70$), consistent with the Wald estimator's sensitivity to misclassification in the first stage. M-bias uniquely reverses: $\rho = +0.87$ ($p < 0.001$). The mechanism is that misclassification attenuates the spurious M-bias path, so the naive estimator under noisy annotations is closer to the true causal effect; improving annotation quality (higher $F_1$) removes this protective attenuation and increases bias. This is consistent with the correction results (\S\ref{sec:correction}), where PPI++ harms M-bias ($-$88\%) by removing the same protective noise. Collider shows a positive but non-significant trend ($\rho = +0.31$, $p = 0.15$), consistent with Berkson bias attenuation. Per-dataset breakdowns (CivilComments $K{=}2$: $\rho = -1.0$ for all topologies with $n{=}7$) should be interpreted with caution given the small sample and limited $F_1$ variation within the binary task.
1441	
1442	\subsection{Confusion Matrix Estimation Robustness}
1443	\label{sec:c_robustness}
1444	
1445	The ASV framework requires the confusion matrix $C$, which in practice must be estimated from a held-out gold-labeled subset. We assess how estimation noise in $\hat{C}$ propagates to the safe/fragile partition and ASV ranking. For each of 8 empirical confusion matrices (VAST, 4 LLMs $\times$ 2 prompting strategies), we draw $n_{\text{gold}} \in \{50, 100, 200, 500\}$ samples from a $\text{Multinomial}(n_{\text{gold}}, C_{\cdot k})$ distribution per column, compute $\hat{C}$, and evaluate the resulting ASV ranking across 200 bootstrap replicates.
1446	
1447	Spearman $\rho$ is computed vs.\ true-$C$ ranking under multinomial bootstrap from finite gold sets (8 empirical matrices $\times$ 200 bootstrap replicates per $n_{\text{gold}}$).
1448	
1449	\begin{table}[H]
1450	\centering
1451	\small
1452	\caption{$\hat{C}$ estimation robustness: partition stability and ASV ranking correlation.}
1453	\label{tab:c_robustness}
1454	\begin{tabular}{lccc}
1455	\toprule
1456	$n_{\text{gold}}$ & Partition stability & $\rho$ (median) & $\rho$ ($q_{25}$) \\
1457	\midrule
1458	50 & 50.4\% & 0.991 & 0.789 \\
1459	100 & 82.0\% & 1.000 & 0.991 \\
1460	200 & 85.6\% & 1.000 & 0.991 \\
1461	500 & 88.5\% & 1.000 & 0.991 \\
1462	\bottomrule
1463	\end{tabular}
1464	\end{table}
1465	
1466	The ASV ranking is highly robust: median Spearman $\rho \geq 0.99$ even at $n_{\text{gold}}{=}50$. The safe/fragile partition (5 safe vs.\ 2 fragile topologies) recovers reliably from $n_{\text{gold}} \geq 100$ (82\% stability), increasing to 89\% at $n_{\text{gold}}{=}500$. The remaining instability concentrates in source matrices with low diagonal dominance (e.g., VAST DeepSeek few-shot: $\min C_{kk} = 0.16$), where bootstrap noise can shift borderline ASV values across the partition boundary. All 8 truth partitions match the canonical safe/fragile partition, confirming that the theoretical dichotomy holds empirically.
1467	
1468	\subsection{Sign Reversal Determinants}
1469	\label{sec:sign_determinants}
1470	
1471	We investigate which confusion matrix features predict exposure sign reversal across the 23 empirical LLM configurations. For each matrix, we compute 10 structural features: $\min_k C_{kk}$ (minimum diagonal), $\overline{C_{kk}}$ (mean diagonal), $\max_{j \neq k} C_{jk}$ (maximum off-diagonal), $\max_{j \neq k} C_{jk}/C_{kk}$ (off-diagonal ratio), $\log(\kappa(C))$ (log condition number), mean and max column entropy, spectral gap, $\det(C)$, and minimum singular value. Sign reversal is defined as any exposure coefficient reversing sign under misclassification.
1472	
1473	Best single-feature rule: $\det(C) < 0.014 \to$ sign reversal (accuracy 91.3\%, sensitivity 85.7\%, specificity 100\%). An AND rule ($\min_k C_{kk} < 0.55$ and mean entropy $> 0.40$) achieves 95.7\% accuracy with 100\% sensitivity.
1474	
1475	\begin{table}[H]
1476	\centering
1477	\small
1478	\caption{Sign reversal rates by $K$ and best single-feature decision rule.}
1479	\label{tab:sign_determinants}
1480	\begin{tabular}{lcc}
1481	\toprule
1482	$K$ & $n$ & Sign reversal rate \\
1483	\midrule
1484	2 & 7 & 0/7 (0\%) \\
1485	3 & 8 & 7/8 (87.5\%) \\
1486	10 & 8 & 7/8 (87.5\%) \\
1487	\bottomrule
1488	\end{tabular}
1489	\end{table}
1490	
1491	Binary matrices ($K{=}2$) never produce exposure sign reversal, consistent with classical attenuation theory. For $K \geq 3$, the determinant of $C$ is the strongest single predictor: $\det(C) < 0.014$ identifies sign-reversing matrices with 100\% specificity (zero false positives) and 85.7\% sensitivity. An AND rule combining $\min_k C_{kk} < 0.55$ with mean column entropy $> 0.40$ achieves 100\% sensitivity at 88.9\% specificity. These rules are robust to $\beta$-scaling (accuracy unchanged at $0.3{\times}$ and $3{\times}$ effect magnitude) but sensitive to $\beta$-sign structure: under uniform-positive $\beta$ (all coefficients same sign), no matrices produce sign reversal regardless of $C$, as cancellation across differently-signed coefficients is the underlying mechanism.
1492	
1493	\subsection{Y-Stratified Non-Differential Verification}
1494	\label{sec:y_stratified_test}
1495	
1496	We directly test the non-differential assumption (Definition~\ref{def:nondiff}) by stratifying confusion matrices by outcome-proxy variables and testing $C(Y{=}\text{high}) \approx C(Y{=}\text{low})$. Using 12 LLM configurations on VAST ($K{=}3$; 4 models $\times$ 3 prompting strategies, 1{,}500 samples each), we compute per-stratum confusion matrices under three Y-proxies and apply permutation tests ($B{=}10{,}000$, test statistic: $\max_{j,k} |C^{(0)}_{jk} - C^{(1)}_{jk}|$).
1497	
1498	Content-independent Y (text length) shows no significant violation (1/12 rejection $\approx$ expected false positive rate at $\alpha{=}0.05$). Content-dependent proxies (topic, sentiment) show expected violations since LLMs observe text content.
1499	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46a41073-9cb7-4170-b316-9e02ebb63d3b",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "606ae9cb-30c8-48a3-9d40-67eda2d0de49",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
      "content": "\\label{tab:proportional_effects}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Proportionality degree} & $\\lambda(C) \\notin [0,1]$ & Sign failure \\\\\n\\midrule\nExact ($\\sigma{=}0$) & 0.0\\% & 0.85\\% \\\\\nNear ($\\sigma{=}0.1$) & 10.3\\% & 0.87\\% \\\\\nNear ($\\sigma{=}0.3$) & 19.0\\% & 0.96\\% \\\\\nNear ($\\sigma{=}0.5$) & 22.4\\% & 0.93\\% \\\\\nIndependent ($f \\perp g$) & 22.9\\% & 0.17\\% \\\\\n\\midrule\nNLP-realistic DGP & 0.07\\% & 0.0\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe $\\lambda$ OOB rate rises steeply from 0\\% to ${\\sim}10$\\% at $\\sigma{=}0.1$ and saturates near 23\\% for independent $(f,g)$. Sign failure rates remain below 1\\% across all conditions because $\\lambda$ excursions outside $[0,1]$ are typically small and do not reverse the dominant effect direction. The NLP-realistic DGP ($\\delta{=}[0, 0.8, {-}0.6]$, $\\beta{=}[0, 1.0, {-}0.5]$) exhibits near-zero OOB (0.07\\%) and zero sign failures, confirming that proportional effects hold approximately in practice.\n\n\\subsection{FWL Invariance Under Nonlinear Models}\n\\label{sec:fwl_nonlinear}\n\nFWL invariance guarantees exactly 0\\% bias reduction from matrix-based corrections (MLA, naive plug-in) under linear OLS for covariate topologies (confounding, mediation, collider, M-bias). Here we test whether this invariance persists under logistic regression across sample sizes $N \\in \\{1000, 5000, 10{,}000, 50{,}000\\}$ and three error levels ($C_{kk} \\in \\{0.9, 0.7, 0.5\\}$), with 200 Monte Carlo replicates per cell. Table~\\ref{tab:fwl_nonlinear} reports the mean logistic bias reduction (positive = correction helps).\n\nResults are averaged over $N \\in \\{1K, 5K, 10K, 50K\\}$ with 200 MC reps each. Under linear OLS, all covariate topologies yield exactly 0\\%. Exposure is shown for comparison.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\caption{Mean logistic bias reduction (\\%) from matrix-based correction.}\n\\label{tab:fwl_nonlinear}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Topology} & \\textbf{Low} ($C_{kk}{=}0.9$) & \\textbf{Med} ($C_{kk}{=}0.7$) & \\textbf{High} ($C_{kk}{=}0.5$) \\\\\n\\midrule\nConfounding & $-$0.003\\% & $<$0.001\\% & $<$0.001\\% \\\\\nMediation & $-$0.004\\% & $<$0.001\\% & $<$0.001\\% \\\\\nCollider & $-$0.033\\% & $-$0.020\\% & $<$0.001\\% \\\\\nM-bias & $-$0.049\\% & $-$0.010\\% & $<$0.001\\% \\\\\nFront-door & 0.001\\% & $-$0.001\\% & $<$0.001\\% \\\\\n\\midrule\nExposure & $-$68.5\\% & $-$48.7\\% & $-$22.5\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFor all five covariate topologies, logistic bias reduction is negligible ($|$mean$| < 0.05\\%$) across all $N$ and error levels, with no systematic $N$-scaling: medians cluster within $\\pm 0.002\\%$ at $N{=}50{,}000$. The large standard deviations observed at certain $(N, \\text{error})$ cells for collider and M-bias (up to 2.6\\% std at $N{=}10{,}000$) reflect rare outlier replicates; medians remain near zero. This confirms that FWL invariance is a robust structural property that extends beyond linear models for covariate topologies.\n\nIn contrast, exposure shows substantial FWL breakdown under logistic regression: $-$22\\% to $-$78\\% bias reduction (negative = correction worsens bias), stabilising at $N \\geq 5{,}000$. The breakdown magnitude increases with accuracy ($C_{kk}$), consistent with the exposure topology's sensitivity to the nonlinear link function transforming category weights.\n\n\\subsection{PPI++ Gold Label Ratio Sensitivity}\n\\label{sec:ppi_gold_ratio}\n\nWe test PPI++ correction performance as a function of gold label fraction ($K{=}3$, $N{=}10{,}000$, 100 MC replications, 5 Dirichlet confusion matrices with $\\min_k C_{kk}{\\geq}0.6$).\n\nNegative values indicate PPI++ increases RMSE relative to the naive estimator.\n\n\\begin{table}[H]\n\\centering\n\\caption{PPI++ RMSE reduction (\\%) vs.\\ gold label fraction.}\n\\label{tab:ppi_gold_ratio}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lccccc}\n\\toprule\nTopology & 5\\% & 10\\% & 20\\% & 50\\% & 100\\% \\\\\n\\midrule\nConfounding & $+$84.8 & $+$88.6 & $+$91.8 & $+$94.2 & $+$95.2 \\\\\nExposure & $+$75.2 & $+$83.1 & $+$87.1 & $+$91.2 & $+$93.8 \\\\\nMediation & $+$56.7 & $+$70.4 & $+$77.2 & $+$85.3 & $+$88.7 \\\\\nIV & $+$1.4 & $+$22.1 & $+$50.1 & $+$66.7 & $+$76.4 \\\\\nM-bias & $-$125.3 & $-$43.6 & $-$19.6 & $+$6.0 & $+$18.5 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFor confounding and exposure, PPI++ achieves $>$75\\% RMSE reduction even at 5\\% gold labels; IV requires ${\\geq}20\\%$ gold to reach 50\\% reduction, reflecting the Wald estimator's higher variance. M-bias exhibits harmful correction at ${\\leq}20\\%$ gold ($-125\\%$ at 5\\%), because PPI++ re-exposes the M-bias pathway that annotation error had attenuated; only at ${\\geq}50\\%$ gold does the estimator become weakly beneficial ($+6\\%$).\n\n\\subsection{Realistic Differential Misclassification Thresholds}\n\\label{sec:realistic_epsilon}\n\nOur non-differential assumption (Definition~\\ref{def:nondiff}) requires $P(A^*{\\mid}A,Y) = P(A^*{\\mid}A)$. We estimate how much $Y$-stratified differential error each of our 23 empirical LLM confusion matrices can tolerate before exposure sign reversal exceeds 5\\%. For each matrix $C$, we construct $C_{\\text{high}} = \\text{renorm}(C + \\varepsilon\\Delta)$ and $C_{\\text{low}} = \\text{renorm}(C - \\varepsilon\\Delta)$ with random off-diagonal perturbation $\\Delta$ (500 MC trials per $\\varepsilon$), sweep $\\varepsilon \\in [0, 0.50]$, and report the safe threshold $\\varepsilon^*_{\\text{safe}} = \\max\\{\\varepsilon : \\text{reversal rate} < 5\\%\\}$ (Table~\\ref{tab:realistic_epsilon}).\n\nFor $K{=}2$ (binary), no configuration produces sign reversal up to $\\varepsilon{=}0.50$. For $K{\\geq}3$, the majority of configurations are fragile ($\\varepsilon^*_{\\text{safe}}{=}0$), confirming that the non-differential assumption is load-bearing for multi-class exposure.\n\n\\begin{table}[H]\n\\centering\n\\caption{Safe differential misclassification thresholds $\\varepsilon^*_{\\text{safe}}$ by dataset/$K$.}\n\\label{tab:realistic_epsilon}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Dataset} & $K$ & $n$ & \\textbf{Mean} $\\varepsilon^*$ & \\textbf{Median} $\\varepsilon^*$ & $\\varepsilon^*{=}0$ \\\\\n\\midrule\nCivil Comments & 2 & 7 & 0.50 & 0.50 & 0/7 \\\\\nVAST & 3 & 8 & 0.003 & 0.00 & 7/8 \\\\\nHuMAID & 10 & 8 & 0.045 & 0.00 & 7/8 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe distribution is sharply bimodal: all $K{=}2$ configurations are immune to differential misclassification within the tested range ($\\varepsilon^*_{\\text{safe}}{=}0.50$), consistent with the binary sign-preservation guarantee (Proposition~\\ref{prop:signflip}(c)). For $K{\\geq}3$, 14 of 16 configurations have $\\varepsilon^*_{\\text{safe}}{=}0$: sign reversal occurs at the smallest tested $\\varepsilon{=}0.01$. Two outliers (VAST: $\\varepsilon^*{=}0.02$; HuMAID: $\\varepsilon^*{=}0.36$) have atypically structured confusion matrices. This confirms that even small violations of non-differential misclassification are consequential for multi-class exposure, underscoring the practical importance of validating $P(A^*{\\mid}A,Y) \\approx P(A^*{\\mid}A)$ on gold-labeled subsets when $K \\geq 3$.\n\n\\subsection{Proportional Effects with Empirical Confusion Matrices}\n\\label{sec:proportional_real_matrices}\n\nTheorem~\\ref{thm:monotone} assumes proportional effects ($f = \\lambda g$). We evaluate this assumption using all 23 empirical LLM confusion matrices under four DGP groups in the mediation topology (23 matrices $\\times$ 50 seeds $\\times$ 100{,}000 precomputed samples per seed).\n\nEvaluation uses the mediation DGP. $\\lambda(C) \\in [0,1]$: proportion satisfying the Theorem~\\ref{thm:monotone} bound. Sign pres.: sign preservation rate of the direct effect estimate.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\caption{Proportional effects validation with 23 real LLM confusion matrices.}\n\\label{tab:proportional_empirical}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{DGP Group} & $\\lambda(C)$ \\textbf{mean} & $\\lambda(C) \\in [0,1]$ & \\textbf{Sign pres.} & \\textbf{CV} \\\\\n\\midrule\nProportional ($f{=}\\lambda g$) & 0.271 & 99.8\\% & 100\\% & 0.00 \\\\\nNear-prop.\\ ($\\sigma{=}0.1$) & 0.285 & 99.2\\% & 100\\% & 1.06 \\\\\nNon-proportional & 0.240 & 85.0\\% & 97.3\\% & 3.60 \\\\\nSparse & 0.296 & 75.8\\% & 98.6\\% & 6.59 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nUnder proportional and near-proportional effects, $\\lambda(C)$ remains within $[0,1]$ for ${\\geq}99\\%$ of configurations with 100\\% sign preservation: the Theorem~\\ref{thm:monotone} conditions are satisfied by real LLM confusion matrices. Even under non-proportional effects ($f$ independent of $g$), sign preservation remains at 97.3\\%, with $\\lambda(C)$ exceeding $[0,1]$ in 15\\% of cases. The per-$K$ breakdown shows that $\\lambda(C)$ is dimension-dependent: $K{=}2$ (mean 0.249), $K{=}3$ (mean 0.082), $K{=}10$ (mean 0.490), with 100\\% in $[0,1]$ across all $K$ under proportional effects. Sparse DGP (zero-effect categories) produces the highest violation rate (24.2\\%), consistent with the breakdown mechanism: zero-effect categories make $f/g$ ratios undefined, maximally departing from proportionality.\n\n\\subsection{Case Study: ASV Diagnosis of Political Ad Tone Classification}\n\\label{sec:asv_case_study}\n\nWe illustrate the ASV diagnostic workflow on a concrete CSS application. \\citet{egami_hinck_stewart_wei2023} use LLM classifiers to annotate political advertising tone ($K{=}3$: promote/contrast/attack) from the Fowler \\& Ridout database, then estimate the causal effect of ad tone on voter outcomes. The annotated variable is the \\textbf{exposure} (treatment). Using a representative $K{=}3$ confusion matrix from our empirical set (VAST DeepSeek zero-shot, mean diagonal 0.734) as a proxy:\n\n\\begin{center}\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lccc}\n\\toprule\nCoefficient & $\\delta^*_{\\text{mag}}$ (10\\%) & $\\delta^*_{\\text{sf}}$ & Relative bias at $\\delta{=}1$ \\\\\n\\midrule\n$\\beta_1$ (primary) & 0.234 & $> 1.5$ & 39.7\\% \\\\\n$\\beta_2$ (secondary) & 0.154 & $> 1.5$ & 60.4\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{center}\n\nBoth coefficients are magnitude-unsafe ($\\delta^* < 1$), with the secondary coefficient more fragile ($\\delta^*{=}0.154$). If the same annotator were instead classifying a \\textbf{confounder} (e.g., media framing as a control variable), magnitude ASV rises to $\\delta^*{=}0.690$, a $3{\\times}$ increase in error tolerance from the same confusion matrix. This demonstrates the central insight: topology, not annotator quality, determines vulnerability. Algorithm~\\ref{alg:correction} routes this exposure topology to PPI++ or DSL correction; matrix-based methods (naive plug-in, MLA) are ineffective due to FWL non-applicability.\n\n\\subsection{End-to-End Demonstration}\n\\label{sec:e2e_demo}\n\n\\input{e2e_demo_table.tex}\n\nThe demonstration uses a symmetric $C_0$ ($d_{\\mathrm{rel}}{=}0$); empirical $K{=}3$ matrices deviate substantially (median $d_{\\mathrm{rel}}{=}0.33$, Remark~\\ref{rem:symmetry}), but core ASV ranking and correction routing remain valid under Conjecture~\\ref{conj:monotone}.\n\n\\subsection{Semi-Real Case Study with Production LLM Confusion Matrices}\n\\label{sec:real_cm_demo}\n\nWe repeat the end-to-end pipeline using 10 confusion matrices estimated from production LLM annotation of VAST stance detection ($K{=}3$; DeepSeek, Llama4, Qwen2.5-7B, Qwen3 under zero-shot and few-shot prompting). These matrices exhibit median $d_{\\mathrm{rel}}{=}0.33$ (Remark~\\ref{rem:symmetry}), far from the symmetric assumption of Theorem~\\ref{thm:k3_symmetric}. Results confirm both topology-dependent patterns: PPI++ achieves 93.6\\% median exposure bias reduction while plug-in corrections yield 0\\% improvement for confounding (FWL invariance, machine precision; Table~\\ref{tab:e2e-real-cm}).\n\n\\input{e2e_real_cm_table.tex}\n\n\\subsection{Correction Method Sensitivity to $K$}\n\\label{sec:correction_k_sensitivity}\n\nWe test whether the correction method ranking from Table~\\ref{tab:correction} ($K{=}3$) is stable at $K{=}5$ and $K{=}10$. For each $K$, we sample 5 random Dirichlet confusion matrices (diagonal $\\geq 0.6$), run 100 MC replications per topology--matrix combination ($N{=}5{,}000$, 10\\% gold fraction), and compute RMSE reduction for all five methods across all seven topologies.\n\n\\paragraph{Grand ranking stability.}\nSpearman rank correlations across all topology--method pairs: $\\rho_{3,5} = 0.80$, $\\rho_{3,10} = 0.84$, $\\rho_{5,10} = 0.93$ (all $p < 10^{-8}$). Per-topology correlations are even stronger: 5 of 7 topologies (confounding, collider, M-bias, IV, and exposure at $K{=}10$) achieve $\\rho = 1.0$ between $K{=}3$ and $K{=}10$.\n\n\\paragraph{Method-specific patterns.}\nPPI++ effectiveness degrades with $K$: confounding RMSE reduction drops from 85.6\\% ($K{=}3$) to 75.6\\% ($K{=}10$); mediation drops from 57.1\\% to 9.0\\%. At $K{=}10$, PPI++ becomes harmful for IV ($-124\\%$) and exposure ($-11\\%$). MC-SIMEX is the most $K$-robust method, maintaining the top rank for 5/7 topologies at $K{=}10$ (vs.\\ 3/7 at $K{=}3$). FWL invariance (naive plug-in and MLA achieving 0\\% bias reduction on the treatment coefficient) holds at all $K$ tested, confirming the structural nature of this result.\n\nBold indicates the top method for that topology--$K$ combination.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\caption{Top correction method and RMSE reduction (\\%) by topology across $K$.}\n\\label{tab:correction_k}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Topology} & $K{=}3$ & $K{=}5$ & $K{=}10$ \\\\\n\\midrule\nConfounding & \\textbf{PPI++} 85.6 & \\textbf{PPI++} 76.4 & \\textbf{PPI++} 75.6 \\\\\nMediation & \\textbf{PPI++} 57.1 & \\textbf{SIMEX} 59.7 & \\textbf{SIMEX} 59.0 \\\\\nCollider & \\textbf{SIMEX} 55.4 & \\textbf{SIMEX} 63.4 & \\textbf{SIMEX} 57.3 \\\\\nExposure & \\textbf{SIMEX} 72.5 & \\textbf{SIMEX} 65.0 & \\textbf{SIMEX} 47.3 \\\\\nM-bias & \\textbf{SIMEX} 3.2 & \\textbf{SIMEX} 47.0 & \\textbf{SIMEX} 43.7 \\\\\nIV & \\textbf{SIMEX} 30.9 & \\textbf{SIMEX} 30.4 & \\textbf{SIMEX} 27.1 \\\\\nFront-door & \\textbf{PPI++} 82.9 & \\textbf{PPI++} 69.0 & \\textbf{SIMEX} 70.1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Comparison with Related Sensitivity Frameworks}\n\\label{sec:sensitivity_comparison}\n\n\\begin{table}[H]\n\\centering\n\\caption{Comparison of sensitivity frameworks.}\n\\label{tab:sensitivity_comparison}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{ASV} & \\textbf{E-value} & \\textbf{Partial} $R^2$ \\\\\n\\midrule\nParameter space & $K{\\times}K$ confusion $C(\\delta)$ & Scalar confounder & $R^2$ of omitted var \\\\\nSensitivity path & $(1{-}\\delta)I + \\delta C_0$ & Monotone scalar & Monotone scalar \\\\\nTopology-specific & \\checkmark & \\ding{55} & \\ding{55} \\\\\nSign-flip diagnostic & \\checkmark ($\\delta^*_{\\text{sign}}$) & \\ding{55} & \\ding{55} \\\\\nTopology dependence & \\checkmark (7 topologies ranked) & \\ding{55} & \\ding{55} \\\\\nMonotonicity & Proved $K{=}2$; conj.\\ $K{\\geq}3$ & Guaranteed & Guaranteed \\\\\nTarget & Annotation error & Unmeasured confounding & Omitted variable \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Per-Topology $F_1$--Bias Correlation}\n\\label{sec:within_topo_f1}\n\nThe cross-topology correlation between macro $F_1$ and $|\\text{bias}|$ is weak ($\\rho = -0.10$, $p = 0.45$; \\S\\ref{sec:empirical}), but decomposing by topology reveals a structured pattern. Table~\\ref{tab:within_topo_f1} reports Spearman correlations computed over 23 LLM configurations (HumAID $K{=}10$, VAST $K{=}3$, CivilComments $K{=}2$; 161 total scenarios).\n\nCorrelations are computed over 23 empirical LLM configurations $\\times$ 3 datasets. Negative $\\rho$: higher $F_1$ $\\to$ lower bias (expected). Positive $\\rho$: higher $F_1$ $\\to$ higher bias (protective attenuation removed).\n\n\\begin{table}[H]\n\\centering\n\\small\n\\caption{Within-topology Spearman $\\rho(F_1, |\\text{bias}|)$ across LLM configurations.}\n\\label{tab:within_topo_f1}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Topology} & $n$ & $\\rho$ & $p$ \\\\\n\\midrule\nConfounding & 23 & $-0.557$ & 0.006 \\\\\nMediation & 23 & $-0.565$ & 0.005 \\\\\nExposure & 23 & $-0.531$ & 0.009 \\\\\nFront-door & 23 & $-0.568$ & 0.005 \\\\\nIV & 23 & $-0.700$ & $<$0.001 \\\\\nCollider & 23 & $+0.310$ & 0.150 \\\\\nM-bias & 23 & $+0.867$ & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFive topologies show the expected negative correlation: better annotation quality ($F_1{\\uparrow}$) reduces causal bias. IV shows the strongest effect ($\\rho = -0.70$), consistent with the Wald estimator's sensitivity to misclassification in the first stage. M-bias uniquely reverses: $\\rho = +0.87$ ($p < 0.001$). The mechanism is that misclassification attenuates the spurious M-bias path, so the naive estimator under noisy annotations is closer to the true causal effect; improving annotation quality (higher $F_1$) removes this protective attenuation and increases bias. This is consistent with the correction results (\\S\\ref{sec:correction}), where PPI++ harms M-bias ($-$88\\%) by removing the same protective noise. Collider shows a positive but non-significant trend ($\\rho = +0.31$, $p = 0.15$), consistent with Berkson bias attenuation. Per-dataset breakdowns (CivilComments $K{=}2$: $\\rho = -1.0$ for all topologies with $n{=}7$) should be interpreted with caution given the small sample and limited $F_1$ variation within the binary task.\n\n\\subsection{Confusion Matrix Estimation Robustness}\n\\label{sec:c_robustness}\n\nThe ASV framework requires the confusion matrix $C$, which in practice must be estimated from a held-out gold-labeled subset. We assess how estimation noise in $\\hat{C}$ propagates to the safe/fragile partition and ASV ranking. For each of 8 empirical confusion matrices (VAST, 4 LLMs $\\times$ 2 prompting strategies), we draw $n_{\\text{gold}} \\in \\{50, 100, 200, 500\\}$ samples from a $\\text{Multinomial}(n_{\\text{gold}}, C_{\\cdot k})$ distribution per column, compute $\\hat{C}$, and evaluate the resulting ASV ranking across 200 bootstrap replicates.\n\nSpearman $\\rho$ is computed vs.\\ true-$C$ ranking under multinomial bootstrap from finite gold sets (8 empirical matrices $\\times$ 200 bootstrap replicates per $n_{\\text{gold}}$).\n\n\\begin{table}[H]\n\\centering\n\\small\n\\caption{$\\hat{C}$ estimation robustness: partition stability and ASV ranking correlation.}\n\\label{tab:c_robustness}\n\\begin{tabular}{lccc}\n\\toprule\n$n_{\\text{gold}}$ & Partition stability & $\\rho$ (median) & $\\rho$ ($q_{25}$) \\\\\n\\midrule\n50 & 50.4\\% & 0.991 & 0.789 \\\\\n100 & 82.0\\% & 1.000 & 0.991 \\\\\n200 & 85.6\\% & 1.000 & 0.991 \\\\\n500 & 88.5\\% & 1.000 & 0.991 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe ASV ranking is highly robust: median Spearman $\\rho \\geq 0.99$ even at $n_{\\text{gold}}{=}50$. The safe/fragile partition (5 safe vs.\\ 2 fragile topologies) recovers reliably from $n_{\\text{gold}} \\geq 100$ (82\\% stability), increasing to 89\\% at $n_{\\text{gold}}{=}500$. The remaining instability concentrates in source matrices with low diagonal dominance (e.g., VAST DeepSeek few-shot: $\\min C_{kk} = 0.16$), where bootstrap noise can shift borderline ASV values across the partition boundary. All 8 truth partitions match the canonical safe/fragile partition, confirming that the theoretical dichotomy holds empirically.\n\n\\subsection{Sign Reversal Determinants}\n\\label{sec:sign_determinants}\n\nWe investigate which confusion matrix features predict exposure sign reversal across the 23 empirical LLM configurations. For each matrix, we compute 10 structural features: $\\min_k C_{kk}$ (minimum diagonal), $\\overline{C_{kk}}$ (mean diagonal), $\\max_{j \\neq k} C_{jk}$ (maximum off-diagonal), $\\max_{j \\neq k} C_{jk}/C_{kk}$ (off-diagonal ratio), $\\log(\\kappa(C))$ (log condition number), mean and max column entropy, spectral gap, $\\det(C)$, and minimum singular value. Sign reversal is defined as any exposure coefficient reversing sign under misclassification.\n\nBest single-feature rule: $\\det(C) < 0.014 \\to$ sign reversal (accuracy 91.3\\%, sensitivity 85.7\\%, specificity 100\\%). An AND rule ($\\min_k C_{kk} < 0.55$ and mean entropy $> 0.40$) achieves 95.7\\% accuracy with 100\\% sensitivity.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\caption{Sign reversal rates by $K$ and best single-feature decision rule.}\n\\label{tab:sign_determinants}\n\\begin{tabular}{lcc}\n\\toprule\n$K$ & $n$ & Sign reversal rate \\\\\n\\midrule\n2 & 7 & 0/7 (0\\%) \\\\\n3 & 8 & 7/8 (87.5\\%) \\\\\n10 & 8 & 7/8 (87.5\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBinary matrices ($K{=}2$) never produce exposure sign reversal, consistent with classical attenuation theory. For $K \\geq 3$, the determinant of $C$ is the strongest single predictor: $\\det(C) < 0.014$ identifies sign-reversing matrices with 100\\% specificity (zero false positives) and 85.7\\% sensitivity. An AND rule combining $\\min_k C_{kk} < 0.55$ with mean column entropy $> 0.40$ achieves 100\\% sensitivity at 88.9\\% specificity. These rules are robust to $\\beta$-scaling (accuracy unchanged at $0.3{\\times}$ and $3{\\times}$ effect magnitude) but sensitive to $\\beta$-sign structure: under uniform-positive $\\beta$ (all coefficients same sign), no matrices produce sign reversal regardless of $C$, as cancellation across differently-signed coefficients is the underlying mechanism.\n\n\\subsection{Y-Stratified Non-Differential Verification}\n\\label{sec:y_stratified_test}\n\nWe directly test the non-differential assumption (Definition~\\ref{def:nondiff}) by stratifying confusion matrices by outcome-proxy variables and testing $C(Y{=}\\text{high}) \\approx C(Y{=}\\text{low})$. Using 12 LLM configurations on VAST ($K{=}3$; 4 models $\\times$ 3 prompting strategies, 1{,}500 samples each), we compute per-stratum confusion matrices under three Y-proxies and apply permutation tests ($B{=}10{,}000$, test statistic: $\\max_{j,k} |C^{(0)}_{jk} - C^{(1)}_{jk}|$).\n\nContent-independent Y (text length) shows no significant violation (1/12 rejection $\\approx$ expected false positive rate at $\\alpha{=}0.05$). Content-dependent proxies (topic, sentiment) show expected violations since LLMs observe text content.\n",
      "numLines": 300,
      "startLine": 1200,
      "totalLines": 1554
    }
  },
  "sourceToolAssistantUUID": "46a41073-9cb7-4170-b316-9e02ebb63d3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-25T08:23:50.273Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SvsDjUZLpAqFYKUShMU2Vw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "offset": 1500,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "606ae9cb-30c8-48a3-9d40-67eda2d0de49",
  "isSidechain": false,
  "requestId": "req_011CbNxwjDyqXzXDx3aNXCQc",
  "type": "assistant",
  "uuid": "6dd1011f-4b80-4b13-bbd5-060ca782116d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EE2Xrimc1remnUVpugVqZ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31975,
      "cache_read_input_tokens": 64523,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 64523,
          "cache_creation_input_tokens": 31975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31975
          },
          "type": "message"
        }
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

_source line 67 · 2026-05-25T08:23:50.277Z_

<details><summary>↩ Tool result · `toolu_01SvsDjUZLpAqFYKUShMU2Vw`</summary>

```text
1500	\begin{table}[H]
1501	\centering
1502	\small
1503	\caption{Y-stratified non-differential test.}
1504	\label{tab:y_stratified}
1505	\resizebox{\columnwidth}{!}{\begin{tabular}{lccc}
1506	\toprule
1507	\textbf{Y proxy} & \textbf{Type} & \textbf{Reject ($\alpha{=}0.05$)} & \textbf{Median $p$} \\
1508	\midrule
1509	Text length & Content-indep. & 1/12 & 0.490 \\
1510	Topic & Content-dep. & 11/12 & 0.002 \\
1511	Sentiment & Content-dep. & 10/12 & 0.017 \\
1512	\bottomrule
1513	\end{tabular}}
1514	\end{table}
1515	
1516	The single text-length rejection (Llama-4 few-shot-3, $p{=}0.027$) is consistent with the expected false positive rate ($0.05 \times 12 = 0.6$). Content-dependent proxies (topic, sentiment) show systematic rejection because LLMs process text content from which these variables can be inferred, violating $Y \perp \text{text} \mid A$. In causal inference applications, $Y$ is typically an external outcome (e.g., health status, economic indicator) that cannot be inferred from the annotated text, satisfying the independence condition. The content-dependent rejections confirm statistical power: the test can detect violations when they exist.
1517	
1518	\section{Notation}
1519	\label{app:notation_table}
1520	
1521	\begin{table}[H]
1522	\centering
1523	\caption{Key notation used throughout the paper.}
1524	\label{tab:notation}
1525	\resizebox{\columnwidth}{!}{\begin{tabular}{cl}
1526	\toprule
1527	\textbf{Symbol} & \textbf{Description} \\
1528	\midrule
1529	$K$ & Number of annotation categories \\
1530	$C$ & Column-stochastic confusion matrix, $C_{jk} = P(A^*{=}j \mid A{=}k)$ \\
1531	$A$, $A^*$ & True and observed (misclassified) annotation \\
1532	$T$ & Treatment variable \\
1533	$Y$ & Outcome variable \\
1534	$\tau$ & Causal effect of interest \\
1535	$\delta$ & ASV perturbation parameter, $C(\delta) = (1{-}\delta)I + \delta C_0$ \\
1536	$\delta^*$ & Critical ASV value (magnitude/significance/sign-flip) \\
1537	$B(C)$ & Bias function, $= \operatorname{plim}(\hat{\tau}) - \tau$ \\
1538	$\beta_k$ & Treatment effect coefficient for category $k$ \\
1539	$D_k$ & Dummy variable for category $k$ \\
1540	\bottomrule
1541	\end{tabular}}
1542	\end{table}
1543	
1544	\section{Use of AI Assistants}
1545	\label{app:ai-assistants}
1546	
1547	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
1548	\begin{itemize}
1549	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
1550	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
1551	    \item \textbf{Proofs:} assisting with proof development for Theorems~1--2 and the conditional monotonicity analysis (Remark~\ref{rem:conditional_monotonicity}); all proofs were verified by the authors.
1552	    \item \textbf{Literature:} summarizing related papers to inform the related-work section.
1553	\end{itemize}
1554	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6dd1011f-4b80-4b13-bbd5-060ca782116d",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "c05071e5-6c74-4b04-8bcf-c610aabbb65f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
      "content": "\\begin{table}[H]\n\\centering\n\\small\n\\caption{Y-stratified non-differential test.}\n\\label{tab:y_stratified}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Y proxy} & \\textbf{Type} & \\textbf{Reject ($\\alpha{=}0.05$)} & \\textbf{Median $p$} \\\\\n\\midrule\nText length & Content-indep. & 1/12 & 0.490 \\\\\nTopic & Content-dep. & 11/12 & 0.002 \\\\\nSentiment & Content-dep. & 10/12 & 0.017 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe single text-length rejection (Llama-4 few-shot-3, $p{=}0.027$) is consistent with the expected false positive rate ($0.05 \\times 12 = 0.6$). Content-dependent proxies (topic, sentiment) show systematic rejection because LLMs process text content from which these variables can be inferred, violating $Y \\perp \\text{text} \\mid A$. In causal inference applications, $Y$ is typically an external outcome (e.g., health status, economic indicator) that cannot be inferred from the annotated text, satisfying the independence condition. The content-dependent rejections confirm statistical power: the test can detect violations when they exist.\n\n\\section{Notation}\n\\label{app:notation_table}\n\n\\begin{table}[H]\n\\centering\n\\caption{Key notation used throughout the paper.}\n\\label{tab:notation}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{cl}\n\\toprule\n\\textbf{Symbol} & \\textbf{Description} \\\\\n\\midrule\n$K$ & Number of annotation categories \\\\\n$C$ & Column-stochastic confusion matrix, $C_{jk} = P(A^*{=}j \\mid A{=}k)$ \\\\\n$A$, $A^*$ & True and observed (misclassified) annotation \\\\\n$T$ & Treatment variable \\\\\n$Y$ & Outcome variable \\\\\n$\\tau$ & Causal effect of interest \\\\\n$\\delta$ & ASV perturbation parameter, $C(\\delta) = (1{-}\\delta)I + \\delta C_0$ \\\\\n$\\delta^*$ & Critical ASV value (magnitude/significance/sign-flip) \\\\\n$B(C)$ & Bias function, $= \\operatorname{plim}(\\hat{\\tau}) - \\tau$ \\\\\n$\\beta_k$ & Treatment effect coefficient for category $k$ \\\\\n$D_k$ & Dummy variable for category $k$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \\LaTeX{}.\n    \\item \\textbf{Proofs:} assisting with proof development for Theorems~1--2 and the conditional monotonicity analysis (Remark~\\ref{rem:conditional_monotonicity}); all proofs were verified by the authors.\n    \\item \\textbf{Literature:} summarizing related papers to inform the related-work section.\n\\end{itemize}\n",
      "numLines": 55,
      "startLine": 1500,
      "totalLines": 1554
    }
  },
  "sourceToolAssistantUUID": "6dd1011f-4b80-4b13-bbd5-060ca782116d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-25T08:23:51.442Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WyprD1byGiLepK11zkFvtc`</summary>

```json
{
  "pattern": "\\\\section\\*?\\{Limitations",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c05071e5-6c74-4b04-8bcf-c610aabbb65f",
  "isSidechain": false,
  "requestId": "req_011CbNxwjDyqXzXDx3aNXCQc",
  "type": "assistant",
  "uuid": "f73bdca1-bceb-476d-a825-71586f7c6b11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EE2Xrimc1remnUVpugVqZ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31975,
      "cache_read_input_tokens": 64523,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 64523,
          "cache_creation_input_tokens": 31975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31975
          },
          "type": "message"
        }
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

_source line 69 · 2026-05-25T08:23:51.541Z_

```json
{
  "parentUuid": "e993c006-7c74-4f1f-b40d-e4610080c767",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d470a544-e56c-45b1-a567-70710c3bf416",
  "timestamp": "2026-05-25T08:23:51.541Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 70_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：causal_annot_error_attrib Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 92 warning 一…",
  "leafUuid": "d470a544-e56c-45b1-a567-70710c3bf416",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb"
}
```

---

### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit causal annotation error attribution paper",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb"
}
```

---

### Assistant

_source line 72 · 2026-05-25T08:23:57.951Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now check a few more things:

1. Abstract word count is ~182, which is under 200 — good for EMNLP rule
2. Limitations section — appears only in conclusion.tex line 8, which is in the main body (correct per EMNLP rules). Let me check if there's a limitations section in the appendix too.
3. Check for multiple limitations sections in appendix
4. Check the claims in the abstract vs introduction vs experiments consistency
5. Check for "significantly" with statistical support
6. Count words in limitations section

Let me also check some specifics and read the table files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d470a544-e56c-45b1-a567-70710c3bf416",
  "isSidechain": false,
  "requestId": "req_011CbNxxWToNGVr9Fki2rSGv",
  "type": "assistant",
  "uuid": "e2b34ee7-2d9a-4d52-bdab-fbf34626c283",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cyi8na1j4A3kNrfc1wjcy6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23548,
      "cache_read_input_tokens": 96498,
      "output_tokens": 959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 959,
          "cache_read_input_tokens": 96498,
          "cache_creation_input_tokens": 23548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23548
          },
          "type": "message"
        }
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

_source line 73 · 2026-05-25T08:23:57.951Z_

Let me check a few more specific items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2b34ee7-2d9a-4d52-bdab-fbf34626c283",
  "isSidechain": false,
  "requestId": "req_011CbNxxWToNGVr9Fki2rSGv",
  "type": "assistant",
  "uuid": "277fadcc-76c4-44dd-b854-3ae3f4360069",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cyi8na1j4A3kNrfc1wjcy6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23548,
      "cache_read_input_tokens": 96498,
      "output_tokens": 959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 959,
          "cache_read_input_tokens": 96498,
          "cache_creation_input_tokens": 23548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23548
          },
          "type": "message"
        }
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

_source line 74 · 2026-05-25T08:23:59.640Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011sEs6MP32bGcaF7u9YkgTp`</summary>

```json
{
  "pattern": "\\\\section.*[Ll]imitation",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "277fadcc-76c4-44dd-b854-3ae3f4360069",
  "isSidechain": false,
  "requestId": "req_011CbNxxWToNGVr9Fki2rSGv",
  "type": "assistant",
  "uuid": "46443c34-330e-44f9-8fe5-eeaa71fae9bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cyi8na1j4A3kNrfc1wjcy6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23548,
      "cache_read_input_tokens": 96498,
      "output_tokens": 959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 959,
          "cache_read_input_tokens": 96498,
          "cache_creation_input_tokens": 23548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23548
          },
          "type": "message"
        }
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

_source line 75 · 2026-05-25T08:24:05.610Z_

<details><summary>↩ Tool result · `toolu_01DDBGKk4Gi4iFR9gkPaYQjX`</summary>

```text
1	% Auto-generated by artifacts/e2e_demo.py
2	\begin{table}[H]
3	\centering
4	\small
5	\resizebox{\columnwidth}{!}{\begin{tabular}{lrrlrr}
6	\toprule
7	Topology & Naive Bias (\%) & ASV $\delta^*_{\mathrm{mag}}$ & Routed Method & Corrected Bias (\%) & Improvement (\%) \\
8	\midrule
9	Confounding & +22.71 $\pm$ 2.29 & 0.352 & no correction (FWL) & +22.71 $\pm$ 2.29 & +0.0\% \\
10	\quad (naive plug-in) & -- & -- & -- & +22.71 $\pm$ 2.29 & +0.0\% \\
11	\quad (MLA)          & -- & -- & -- & +22.71 $\pm$ 2.29 & +0.0\% \\
12	Exposure & -42.87 $\pm$ 2.42 & 0.239 & PPI++ & -0.22 $\pm$ 4.94 & +90.9\% \\
13	IV & +82.40 $\pm$ 12.22 & 0.204 & MC-SIMEX (gold-free) & -197.00 $\pm$ 3.79 & -139.1\% \\
14	\bottomrule
15	\end{tabular}}
16	\caption{End-to-end demo over 100 replicates (N=10,000, K=3, 20\% gold). Confounding: plug-in corrections leave the treatment coefficient unchanged (FWL invariance), so Algorithm~1 routes to ``no correction''. Exposure: PPI++ recovers the target coefficient. IV: Wald estimator instability produces large bias; PPI++ (OLS-based) is limited, routing to MC-SIMEX.}
17	\label{tab:e2e-demo}
18	\end{table}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "becd21e3-29c8-4bdf-9bc0-e995d398de23",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "de721b5e-9a17-4fd3-97cb-7cc69a7b3886",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/e2e_demo_table.tex",
      "content": "% Auto-generated by artifacts/e2e_demo.py\n\\begin{table}[H]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrlrr}\n\\toprule\nTopology & Naive Bias (\\%) & ASV $\\delta^*_{\\mathrm{mag}}$ & Routed Method & Corrected Bias (\\%) & Improvement (\\%) \\\\\n\\midrule\nConfounding & +22.71 $\\pm$ 2.29 & 0.352 & no correction (FWL) & +22.71 $\\pm$ 2.29 & +0.0\\% \\\\\n\\quad (naive plug-in) & -- & -- & -- & +22.71 $\\pm$ 2.29 & +0.0\\% \\\\\n\\quad (MLA)          & -- & -- & -- & +22.71 $\\pm$ 2.29 & +0.0\\% \\\\\nExposure & -42.87 $\\pm$ 2.42 & 0.239 & PPI++ & -0.22 $\\pm$ 4.94 & +90.9\\% \\\\\nIV & +82.40 $\\pm$ 12.22 & 0.204 & MC-SIMEX (gold-free) & -197.00 $\\pm$ 3.79 & -139.1\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{End-to-end demo over 100 replicates (N=10,000, K=3, 20\\% gold). Confounding: plug-in corrections leave the treatment coefficient unchanged (FWL invariance), so Algorithm~1 routes to ``no correction''. Exposure: PPI++ recovers the target coefficient. IV: Wald estimator instability produces large bias; PPI++ (OLS-based) is limited, routing to MC-SIMEX.}\n\\label{tab:e2e-demo}\n\\end{table}\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  },
  "sourceToolAssistantUUID": "becd21e3-29c8-4bdf-9bc0-e995d398de23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-25T08:23:59.656Z_

<details><summary>↩ Tool result · `toolu_011sEs6MP32bGcaF7u9YkgTp`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46443c34-330e-44f9-8fe5-eeaa71fae9bc",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "7fec974c-a708-4a7a-86b5-fa6e63c455dd",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "46443c34-330e-44f9-8fe5-eeaa71fae9bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-25T08:24:01.003Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01UGnfHrnqCA28gRdX5saHJk`</summary>

```json
{
  "pattern": "significantly",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fec974c-a708-4a7a-86b5-fa6e63c455dd",
  "isSidechain": false,
  "requestId": "req_011CbNxxWToNGVr9Fki2rSGv",
  "type": "assistant",
  "uuid": "3b2a3a21-b5ff-4201-97c6-2e63328367c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cyi8na1j4A3kNrfc1wjcy6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23548,
      "cache_read_input_tokens": 96498,
      "output_tokens": 959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 959,
          "cache_read_input_tokens": 96498,
          "cache_creation_input_tokens": 23548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23548
          },
          "type": "message"
        }
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

_source line 78 · 2026-05-25T08:24:01.021Z_

<details><summary>↩ Tool result · `toolu_01UGnfHrnqCA28gRdX5saHJk`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b2a3a21-b5ff-4201-97c6-2e63328367c8",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "3e5c3ab3-41c5-4e1b-91d9-544bad1d124d",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "3b2a3a21-b5ff-4201-97c6-2e63328367c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-25T08:24:02.206Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01999vLhf1DheMaB2J6YJTz4`</summary>

```json
{
  "pattern": "state.of.the.art|SOTA|sota",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e5c3ab3-41c5-4e1b-91d9-544bad1d124d",
  "isSidechain": false,
  "requestId": "req_011CbNxxWToNGVr9Fki2rSGv",
  "type": "assistant",
  "uuid": "8dd496f5-5e8b-49cb-a640-c08cf74a39f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cyi8na1j4A3kNrfc1wjcy6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23548,
      "cache_read_input_tokens": 96498,
      "output_tokens": 959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 959,
          "cache_read_input_tokens": 96498,
          "cache_creation_input_tokens": 23548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23548
          },
          "type": "message"
        }
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

_source line 80 · 2026-05-25T08:24:02.219Z_

<details><summary>↩ Tool result · `toolu_01999vLhf1DheMaB2J6YJTz4`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex:4:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dd496f5-5e8b-49cb-a640-c08cf74a39f9",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "b92fa670-2e26-46d2-af14-85e3049366c6",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex:4:[Omitted long matching line]",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "8dd496f5-5e8b-49cb-a640-c08cf74a39f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-25T08:24:03.150Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01UdKLdhgfXyudxnkNcfeFyd`</summary>

```json
{
  "pattern": "93\\.6",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b92fa670-2e26-46d2-af14-85e3049366c6",
  "isSidechain": false,
  "requestId": "req_011CbNxxWToNGVr9Fki2rSGv",
  "type": "assistant",
  "uuid": "f3fe7194-c5c3-44bc-8637-e96a11a44209",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cyi8na1j4A3kNrfc1wjcy6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23548,
      "cache_read_input_tokens": 96498,
      "output_tokens": 959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 959,
          "cache_read_input_tokens": 96498,
          "cache_creation_input_tokens": 23548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23548
          },
          "type": "message"
        }
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

_source line 82 · 2026-05-25T08:24:03.162Z_

<details><summary>↩ Tool result · `toolu_01UdKLdhgfXyudxnkNcfeFyd`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:1354:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/e2e_real_cm_table.tex:22:\textit{Median improvement} & & \multicolumn{2}{c}{+93.6\%} & & \multicolumn{2}{c}{-0.0\%} \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3fe7194-c5c3-44bc-8637-e96a11a44209",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "02a677e2-2817-4781-beb0-c0fcb07a66b8",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex:1354:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/e2e_real_cm_table.tex:22:\\textit{Median improvement} & & \\multicolumn{2}{c}{+93.6\\%} & & \\multicolumn{2}{c}{-0.0\\%} \\\\",
    "numLines": 2
  },
  "sourceToolAssistantUUID": "f3fe7194-c5c3-44bc-8637-e96a11a44209",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-25T08:24:04.570Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01EwQfYbtqb3xBoDp7HtHBsV`</summary>

```json
{
  "pattern": "61\\\\?%|61\\s*\\\\%",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02a677e2-2817-4781-beb0-c0fcb07a66b8",
  "isSidechain": false,
  "requestId": "req_011CbNxxWToNGVr9Fki2rSGv",
  "type": "assistant",
  "uuid": "7a8b12f8-de99-49c2-a1b2-c2a8834abe9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cyi8na1j4A3kNrfc1wjcy6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23548,
      "cache_read_input_tokens": 96498,
      "output_tokens": 959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 959,
          "cache_read_input_tokens": 96498,
          "cache_creation_input_tokens": 23548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23548
          },
          "type": "message"
        }
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

_source line 84 · 2026-05-25T08:24:04.583Z_

<details><summary>↩ Tool result · `toolu_01EwQfYbtqb3xBoDp7HtHBsV`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex:91:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex:52:Across 23 empirical LLM configurations, the primary coefficient (the category with the largest true effect $|\beta_k|$) never reverses sign, while 61\% reverse a secondary (non-dominant) coefficient, confirmed under 100{,}000 Dirichlet matrices with diagonal ${\geq}\,0.7$ across six beta-ratio conditions (1.0 to 50.0) with 0\% primary sign-flip (Appendix~\ref{app:exposure}).
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex:2:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a8b12f8-de99-49c2-a1b2-c2a8834abe9c",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "722a7cf4-2152-44a9-83da-ddbebce62be2",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex:91:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex:4:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex:52:Across 23 empirical LLM configurations, the primary coefficient (the category with the largest true effect $|\\beta_k|$) never reverses sign, while 61\\% reverse a secondary (non-dominant) coefficient, confirmed under 100{,}000 Dirichlet matrices with diagonal ${\\geq}\\,0.7$ across six beta-ratio conditions (1.0 to 50.0) with 0\\% primary sign-flip (Appendix~\\ref{app:exposure}).\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex:2:[Omitted long matching line]",
    "numLines": 4
  },
  "sourceToolAssistantUUID": "7a8b12f8-de99-49c2-a1b2-c2a8834abe9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-25T08:24:05.103Z_

<details open><summary>🔧 Tool call — Read · `toolu_0133SNdQEARXHafoCWbGhndv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/e2e_real_cm_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "722a7cf4-2152-44a9-83da-ddbebce62be2",
  "isSidechain": false,
  "requestId": "req_011CbNxxWToNGVr9Fki2rSGv",
  "type": "assistant",
  "uuid": "0ef03fe1-8db5-4ee0-8db3-04dfac349049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cyi8na1j4A3kNrfc1wjcy6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23548,
      "cache_read_input_tokens": 96498,
      "output_tokens": 959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 959,
          "cache_read_input_tokens": 96498,
          "cache_creation_input_tokens": 23548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23548
          },
          "type": "message"
        }
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

_source line 86 · 2026-05-25T08:24:05.107Z_

<details><summary>↩ Tool result · `toolu_0133SNdQEARXHafoCWbGhndv`</summary>

```text
1	% Auto-generated by artifacts/e2e_real_cm_demo.py
2	\begin{table}[H]
3	\centering
4	\small
5	\resizebox{\columnwidth}{!}{\begin{tabular}{l c r r r r r}
6	\toprule
7	 & & \multicolumn{2}{c}{Exposure} & & \multicolumn{2}{c}{Confounding} \\
8	\cmidrule(lr){3-4} \cmidrule(lr){6-7}
9	LLM Config & $d_{\mathrm{rel}}$ & Naive (\%) & PPI++ (\%) & & Naive (\%) & Plugin (\%) \\
10	\midrule
11	DeepSeek FS-3 & 0.30 & -61.3 & +0.1 & & +28.5 & +28.5 \\
12	DeepSeek FS-5 & 0.30 & -61.5 & -0.5 & & +28.7 & +28.7 \\
13	DeepSeek ZS & 0.31 & -61.1 & -0.5 & & +28.2 & +28.2 \\
14	Llama4 FS-3 & 0.37 & -64.3 & +0.0 & & +28.4 & +28.4 \\
15	Llama4 FS-5 & 0.32 & -61.3 & +0.0 & & +26.8 & +26.8 \\
16	Llama4 ZS & 0.36 & -59.3 & -0.2 & & +27.9 & +27.9 \\
17	Qwen2.5-7B FS-3 & 0.38 & -68.9 & -0.5 & & +29.3 & +29.3 \\
18	Qwen2.5-7B FS-5 & 0.34 & -68.7 & +0.3 & & +29.0 & +29.0 \\
19	Qwen2.5-7B ZS & 0.38 & -65.5 & +0.3 & & +28.7 & +28.7 \\
20	Qwen3 ZS & 0.32 & -60.3 & -0.5 & & +28.2 & +28.2 \\
21	\midrule
22	\textit{Median improvement} & & \multicolumn{2}{c}{+93.6\%} & & \multicolumn{2}{c}{-0.0\%} \\
23	\bottomrule
24	\end{tabular}}
25	\caption{Semi-real case study with VAST K=3 confusion matrices from 10 LLM configurations. Bias is relative to true $\tau$. Exposure: PPI++ substantially reduces bias. Confounding: plug-in correction is ineffective (FWL invariance).}
26	\label{tab:e2e-real-cm}
27	\end{table}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ef03fe1-8db5-4ee0-8db3-04dfac349049",
  "isSidechain": false,
  "promptId": "0f43cce9-0dd7-406b-be17-11b5b519fd32",
  "type": "user",
  "uuid": "5f70094b-87b6-436c-92a3-226867d14130",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/e2e_real_cm_table.tex",
      "content": "% Auto-generated by artifacts/e2e_real_cm_demo.py\n\\begin{table}[H]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{l c r r r r r}\n\\toprule\n & & \\multicolumn{2}{c}{Exposure} & & \\multicolumn{2}{c}{Confounding} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){6-7}\nLLM Config & $d_{\\mathrm{rel}}$ & Naive (\\%) & PPI++ (\\%) & & Naive (\\%) & Plugin (\\%) \\\\\n\\midrule\nDeepSeek FS-3 & 0.30 & -61.3 & +0.1 & & +28.5 & +28.5 \\\\\nDeepSeek FS-5 & 0.30 & -61.5 & -0.5 & & +28.7 & +28.7 \\\\\nDeepSeek ZS & 0.31 & -61.1 & -0.5 & & +28.2 & +28.2 \\\\\nLlama4 FS-3 & 0.37 & -64.3 & +0.0 & & +28.4 & +28.4 \\\\\nLlama4 FS-5 & 0.32 & -61.3 & +0.0 & & +26.8 & +26.8 \\\\\nLlama4 ZS & 0.36 & -59.3 & -0.2 & & +27.9 & +27.9 \\\\\nQwen2.5-7B FS-3 & 0.38 & -68.9 & -0.5 & & +29.3 & +29.3 \\\\\nQwen2.5-7B FS-5 & 0.34 & -68.7 & +0.3 & & +29.0 & +29.0 \\\\\nQwen2.5-7B ZS & 0.38 & -65.5 & +0.3 & & +28.7 & +28.7 \\\\\nQwen3 ZS & 0.32 & -60.3 & -0.5 & & +28.2 & +28.2 \\\\\n\\midrule\n\\textit{Median improvement} & & \\multicolumn{2}{c}{+93.6\\%} & & \\multicolumn{2}{c}{-0.0\\%} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Semi-real case study with VAST K=3 confusion matrices from 10 LLM configurations. Bias is relative to true $\\tau$. Exposure: PPI++ substantially reduces bias. Confounding: plug-in correction is ineffective (FWL invariance).}\n\\label{tab:e2e-real-cm}\n\\end{table}\n",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  },
  "sourceToolAssistantUUID": "0ef03fe1-8db5-4ee0-8db3-04dfac349049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-25T08:24:05.606Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DDBGKk4Gi4iFR9gkPaYQjX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/e2e_demo_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f70094b-87b6-436c-92a3-226867d14130",
  "isSidechain": false,
  "requestId": "req_011CbNxxWToNGVr9Fki2rSGv",
  "type": "assistant",
  "uuid": "becd21e3-29c8-4bdf-9bc0-e995d398de23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cyi8na1j4A3kNrfc1wjcy6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23548,
      "cache_read_input_tokens": 96498,
      "output_tokens": 959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 959,
          "cache_read_input_tokens": 96498,
          "cache_creation_input_tokens": 23548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23548
          },
          "type": "message"
        }
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

_source line 88 · 2026-05-25T08:27:55.060Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me analyze everything systematically.

Let me check the specific numbers cited:

1. Abstract says: "topology-aware correction reduces exposure bias from 61\% to $<$1\%"
   - The e2e_real_cm_table.tex shows individual rows with Naive exposure bias like -61.3%, -61.5%, -61.1%, etc. and PPI++ results near 0. The median improvement is 93.6%.
   - The conclusion says "PPI++ reduces bias from ${\sim}61\%$ to ${<}1\%$ (Table~\ref{tab:e2e-real-cm})"
   - These numbers align across the abstract, tables, and conclusion.

2. Abstract says "sign reversal is confined to exposure topology" under empirical LLM confusion matrices.
   - From experiments.tex:91: "Of exposure coefficients, 14/23 (61\%) exhibit sign reversal, all secondary; zero across 138 non-exposure scenarios."
   - This is consistent.

3. The abstract doesn't actually mention 93.6% — that's the median improvement shown in the appendix table. The abstract just cites the ~61% to <1% reduction, which matches the conclusion.

Now I'm checking the actual bias values from the table. The naive exposure biases cluster around -61% to -69%, with the median falling closer to -62.8%, so the "~61%" framing is a reasonable approximation of the range rather than the exact median.

The abstract's claim about matrix-based corrections being ineffective aligns with the FWL invariance discussion throughout the paper. I'm also verifying the F₁ correlation claim from the introduction, which states it shows no significant rank correlation with causal bias.

Now I'm doing a comprehensive audit of narrative consistency, starting with checking how the abstract frames the core problem.

The abstract identifies the key issue: when LLM-generated annotations feed into causal inference, annotation quality alone isn't enough—the causal DAG topology determines whether errors attenuate, amplify, or reverse treatment effect estimates. The introduction makes the same point: LLMs replacing human annotators means annotation errors propagate downstream, and the critical gap is that nobody has systematically studied multi-class misclassification across different DAG topologies.

The contributions align with this narrative: they develop a bias taxonomy across seven topologies with sign-preservation and reversal patterns, introduce an ASV framework with monotonicity constraints, and propose topology-aware correction routing using FWL invariance. The methods section delivers on these promises—bias expressions for all seven topologies, the ASV framework, and the correction routing approach.

The experiments validate each piece: the bias taxonomy holds across topologies, the ASV framework ranks vulnerability correctly, and the correction guidance shows that matrix-based approaches fail for certain covariate topologies due to FWL invariance. The conclusion ties it together: at K≥3, exposure and IV can flip treatment effect signs while five topologies preserve them, ASVs provide topology-dependent rankings, and matrix corrections are provably ineffective for four covariate topologies.

For the abstract, I'm checking the structure: problem statement about LLM annotations and topology mattering, methods deriving bias expressions across seven topologies with K≥3 sign reversal and ASVs, results showing sign reversal confined to exposure with PPI++ reducing bias dramatically, and significance around topology-aware routing and matrix correction limitations. Word count sits at 182, well under the 200 limit.

The intro is running lean at three paragraphs before contributions instead of the typical five—background on LLMs replacing annotators and the 31% incorrect conclusion rate, the K≥3 structural transition, and the gap where F1 doesn't correlate with causal bias. The "problem importance" and "existing methods insufficient" angles are compressed together rather than separated out.

Related work is organized thematically across measurement error, LLM annotation, and sensitivity/correction rather than as a chronological listing of who did what.

I'm mapping contributions to their corresponding sections: the multi-class bias taxonomy appears in method and experiments with Table 1, ASVs show up in method and experiments with Table 2 and Figure 3, and topology-aware correction routing is in experiments with Algorithm 1 in the appendix. But I'm noticing the "Primary coefficient preservation" paragraph in the method section feels important yet isn't explicitly listed as a contribution—it's likely woven into the ASV discussion rather than standing alone.

Now checking claim strength: the "state-of-the-art LLMs" reference cites another paper so that's not an overreach, there are no "significantly outperforms" claims, and the "provably ineffective" statement for FWL invariance is backed by proof. The monotonicity claims are appropriately hedged—proved for K=2 and extensively validated for K≥3. The 83.4% sign reversal figure comes from 100,000 simulations, which is solid grounding.

For experimental rigor, the main result table doesn't have error bars because these are population-level rates from the simulations, which makes sense. The end-to-end demo table does include error bars like ±2.29 and ±2.42, showing uncertainty where it matters.

The baselines compare five established correction methods—DSL, PPI++, MC-SIMEX, MLA, and naive plug-in—against naive estimators. The ablation study is thorough, systematically varying K across multiple values, confusion matrix structures, and DGP parameters. For reproducibility, the Monte Carlo settings, Dirichlet priors, and DGP parameters are all documented. Since this is a simulation study rather than a training study, there's no GPU training involved. The supplementary material includes reproduction code and numerical results, though there's no explicit NLP checklist in the paper itself.

The notation is consistent throughout—$\tau$ for the causal estimand, $C$ for the confusion matrix, $\delta$ for the ASV perturbation parameter, and $B(C)$ for the bias function. Key terms like ASV and FWL are defined at first use, and "plim" has a footnote. The paper flows naturally from introduction through the DAG taxonomy in Figure 1, into related work, then to methods, experiments, and conclusion. The discussion is woven into the experiments section rather than separated out, which is standard for ML papers. Now I'm checking the limitations section.

The conclusion covers three main limitations: the linear SEM assumption, the requirement for a known DAG with non-differential measurement error, and the open questions around gold labels for ASV and general K monotonicity. That's roughly 80 words, which fits the guideline. For style, the em-dashes and en-dashes are clean, and the "-ing" constructions are mostly technical terms like "non-decreasing" and "non-increasing" rather than problematic AI-style phrase endings. Let me verify there aren't any actual problematic "-ing" sentence endings in the related work section. closes Claude usage ✓
- No implicit internal process references detected

Now checking the EMNLP-specific requirements: the limitations section is properly placed in the main body, the abstract is under 200 words, and the ARR checklist correctly goes in the OpenReview form rather than the paper itself. The main concern is whether the main text stays within the 8-page limit—the total is 34 pages including appendix, which is fine since EMNLP allows unlimited appendices, but I need to verify the core content fits the constraint.

Rough page estimate: abstract, introduction, related work, method section with figures, experiments with tables, and conclusion with limitations should total around 6.5 pages, leaving some buffer within the 8-page limit. Phase 1 already compiled and verified the page count, so this should be confirmed.

Now I'm checking the abstract's claim about exposure bias reduction. The abstract states the method reduces exposure bias from 61% to less than 1%, and the conclusion references the same numbers from Table e2e-real_cm. Looking at the actual table data, the naive bias ranges from about -59% to -69%, with a median around -61%, while PPI++ achieves results between -0.5% and +0.3%. The numbers check out.

However, I notice there's another "61%" mentioned in the experiments file referring to sign reversal rate (14 out of 23 configurations), which is a different metric entirely. The abstract's 61% is specifically about bias magnitude, not sign reversal. The conclusion uses "~61%" with an approximation marker while the abstract uses "61%" without one, though the table's median of -61.4% supports both phrasings. Now I'm verifying the abstract's claim about sign reversal being confined to exposure topology against the experiments section, which confirms zero sign reversal across non-exposure scenarios and all empirical LLM configurations—this checks out. The abstract also cites a 61% bias reduction from real LLM confusion matrices, which traces back to the median naive exposure bias in Table 5, though I should verify how the conclusion references this. I'm spotting a few concerns that could affect how reviewers receive this work. The 61% figure appears in two different contexts—once for bias magnitude and again for sign reversal rates—which might trip up someone skimming quickly. The abstract is also quite dense with specific numbers and technical details, making it potentially hard to absorb at first glance. There's no standalone Discussion section either; the interpretation of results is woven into the Experiments and Conclusion, which is acceptable but means the higher-level takeaways aren't as explicitly separated. The Limitations section hits the expected length and covers the right number of points, though I should verify the contribution claims are fully supported throughout. Verifying the topology count from Table 1 — Confounding, Exposure, Mediation, Front-door, Collider, M-bias, and IV — that's all seven accounted for. Now checking the experimental scope: the paper uses three NLP datasets (HumAID, VAST, CivilComments) across four LLMs with varying numbers of classes, totaling 23 configurations and 161 scenarios, which aligns with what's described in the abstract. I need to verify whether the abstract's claim about sign reversal being confined to exposure topology actually holds up against what the empirical results show. The "-ing" matches from the grep are mostly legitimate mathematical terminology rather than problematic dangling participles. For the findings, I'm noting a few issues: the abstract states "61%" without the approximation symbol while the actual bias ranges from 59-69%, and this same percentage appears for two different metrics (exposure bias magnitude and sign reversal rate), which could create confusion despite being contextually distinct. I should also flag that there's no dedicated Discussion section, the key Algorithm 1 is relegated to the appendix, and I need to verify the main text stays within page limits.

I'm checking the hyphenation conventions for compound names like "Frisch--Waugh--Lovell" and "Cauchy--Schwarz" — both correctly use en-dashes in LaTeX, which aligns with the style guide's exception for such names. Now I'm looking at a claim in the abstract about five topologies preserving treatment effect signs under regularity conditions, and I need to trace whether the method section actually establishes these conditions clearly.

Now I'm verifying that all key abbreviations are properly defined throughout the paper — LLM, DAG, ASV, FWL, SEM, OLS, MAPE, and MLA all have their definitions in place, and I'm checking the remaining ones like MC-SIMEX. only in the appendix proofs. DGP doesn't appear in the main text, so that's fine. Now checking for DSL — it's cited in the experiments section as a method name without being expanded. The full name "Design-based Supervised Learning" should be provided at first use, which looks like it might be missing.

Let me verify the numerical consistency across sections. I'm checking whether key statistics like the 83.4% sign reversal rate, 52.6% IV result, 1.6% MAPE, and the scenario counts all align properly throughout the abstract, methods, experiments, and tables.

Now I need to confirm the abstract's claim about K≥3 enabling sign reversal—this should be grounded in the Introduction's second paragraph and formally proven through Proposition 1(c) in the Method section, with supporting examples in the Appendix.

I'm also checking the claim that matrix-based corrections fail under linear regression across four topologies, which appears in the abstract and needs verification in the main text. The method section structure reveals an imbalance—contributions 1 and 2 have dedicated method subsections, but contribution 3 (correction routing) is primarily empirical with only Algorithm 1 in the appendix, lacking its own methodological treatment. I'm also noticing the baselines are somewhat dated: DSL and PPI++ are both from 2023, and MC-SIMEX goes back to 2006, which could raise questions about recency.

Now I'm checking the baseline choices more carefully. PPI++ and DSL are reasonably recent for a methods paper, and using established correction techniques like MLA and classical approaches is defensible in this context. Looking at the results reporting, Table 1 draws from 100,000 simulations so the percentages are essentially population-level quantities with negligible sampling error, and the other tables appropriately report ranges or confidence intervals. I should verify the claim about IV corrections worsening estimates in the conclusion.

Checking the numbers: the e2e demo shows MC-SIMEX at -139.1%, but the general correction table reveals SIMEX actually improves IV by 59.4% and PPI++ by 79.4%. The conclusion's statement appears to be specific to the e2e scenario where Algorithm 1 routed to MC-SIMEX, not a blanket claim about all methods. I need to reread the exact wording to clarify what's actually being claimed. MC-SIMEX is shown for IV (because that's what Algorithm 1 routes to), and it gives -139.1%. But the full correction table shows SIMEX at +59.4% and PPI++ at +79.4%.

This is a narrative inconsistency! The Conclusion says "all tested corrections worsen the estimate" for IV, but the appendix correction table shows that SIMEX and PPI++ actually improve RMSE for IV in the general case.

Actually, wait. Let me re-read the Conclusion more carefully: "for IV, all tested corrections worsen the estimate". Hmm, looking at the e2e demo, only one correction method is tested on IV (MC-SIMEX), and it indeed worsens it. The claim might be referring specifically to the e2e demo, not the general case. But the phrasing "all tested corrections" is misleading because in the full evaluation, SIMEX and PPI++ both help IV.

Wait, actually let me re-read more carefully. The conclusion says: "Practitioners should identify the topology first: for exposure, PPI++ reduces bias from ~61% to <1% (Table 5); for IV, all tested corrections worsen the estimate." This seems to be a general statement, not limited to the e2e demo. But the general correction table shows SIMEX +59.4% and PPI++ +79.4% for IV. So the claim "all tested corrections worsen" is incorrect for IV in general. The Conclusion is actually quoting a specific recommendation about topology-dependent performance: PPI++ works well for exposure bias, but then it claims all corrections worsen IV estimates. However, this contradicts the general correction table where SIMEX and PPI++ both show positive RMSE reductions for IV. The statement appears to be either unsupported as a general claim or misleadingly extrapolated from the e2e demo where only MC-SIMEX was tested on IV. I see the issue now—the Conclusion is overstating the findings. The experiments section specifically identifies that topology-agnostic IV correction (like applying MC-SIMEX without considering the graph structure) amplifies bias to -139%, but that's not the same as saying all corrections worsen estimates. The real insight is that topology-aware methods like PPI++ can actually help when gold labels are available, whereas the algorithm routes to MC-SIMEX only when gold labels aren't present. So the Conclusion conflates a specific failure mode of one approach with a blanket claim about all corrections. The K-sensitivity analysis reveals PPI++ actually degrades IV performance at K=10 despite helping at K=3, so the paper's blanket conclusion that all corrections worsen IV is misleading—it's only true at higher K values, not for the K=3 case that dominates the main results. The experiments section also doesn't make this sweeping claim, just noting that one specific scenario amplifies bias, so there's a significant disconnect between what the data actually shows and what the conclusion states. The demo and real-world results are from different experimental setups, so the numbers aren't contradictory—they're just measuring different scenarios. The abstract's claim about reducing exposure bias from 61% to less than 1% checks out against the actual table values. The paper also appropriately frames the general monotonicity result as a conjecture supported by numerical evidence rather than a proven theorem, which is honest about the limitations.

But there's a real problem with the conclusion's claim that "all tested corrections worsen" the IV estimate. Looking at the general correction table at K=3, SIMEX and PPI++ actually improve IV substantially by over 50%, and even at K=10 SIMEX helps. The conclusion seems to overgeneralize from the e2e demo where only MC-SIMEX was tested on IV and failed, ignoring the evidence that other methods work better.

The conclusion also doesn't cite a table for the IV claim while it does for exposure, which makes the unsupported assertion even more problematic. I should also reconsider whether the claim about F₁ not guaranteeing low causal bias is slightly overstated, since within individual topologies there is actually a meaningful negative correlation.

Now I'm organizing my findings and checking whether the introduction's claim about bias varying by an order of magnitude is properly supported by the experimental data. The numbers in the introduction appear to have a slight discrepancy with what's reported in the experiments section. The "provably" claim holds up because it's grounded in an exact algebraic identity that emerges under linear regression assumptions, and the paper appropriately flags this limitation in the Limitations section. Now I'm ready to pull together everything I've verified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de721b5e-9a17-4fd3-97cb-7cc69a7b3886",
  "isSidechain": false,
  "requestId": "req_011CbNxyYvuqpTnccWfxKht1",
  "type": "assistant",
  "uuid": "c7d35fa7-9c6a-41f5-9e69-b0345d008ced",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNBXdyFLwnzMUo2GYB5KuV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2978,
      "cache_read_input_tokens": 120046,
      "output_tokens": 13416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2978,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13416,
          "cache_read_input_tokens": 120046,
          "cache_creation_input_tokens": 2978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2978
          },
          "type": "message"
        }
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

_source line 89 · 2026-05-25T08:28:55.752Z_

Now I have all the information needed. Let me compile the audit findings.

```
[CONTENT_AUDIT_START]

=== 叙事一致性 (CRITICAL 级) ===

- [critical] [叙事一致性] Conclusion 声称 "for IV, all tested corrections worsen the estimate"，但 Appendix Table 4 (tab:correction) 显示 K=3 下 SIMEX (+59.4%) 和 PPI++ (+79.4%) 均能改善 IV 的 RMSE。该结论过度泛化了 e2e demo（仅测试了 MC-SIMEX 的单一场景，-139.1%）到 "all tested corrections" 的笼统声明。Conclusion 的这句话与正文 Experiments §4.4 的措辞 "topology-agnostic IV correction amplifies bias" 也不一致——后者正确限定为 topology-agnostic correction，而 Conclusion 去掉了这个关键限定词。建议修改为："topology-agnostic correction can amplify IV bias (−139% in our demo); even topology-aware methods require gold labels and careful selection" 并引用 correction table 的完整数据。

=== 章节结构 ===

- [info] [章节结构] Abstract 回答了四个必答问题（问题、方法、结果、意义），词数约 182，符合 EMNLP 200-word 限制。结构密集但完整。
- [info] [章节结构] Introduction 采用 3 段 + 贡献列表结构，而非标准 5 段。"问题重要性"和"现有方法不足"合并在第 1 段和第 3 段中。逻辑流通顺，但略微压缩。
- [info] [章节结构] Related Work 采用三段 \paragraph 主题归纳式（measurement error / LLM annotation / sensitivity analysis），不是 "A did X. B did Y." 堆砌。符合规范。

=== 贡献-范围对齐 ===

- [info] [贡献-范围] 贡献 3（topology-aware correction routing）的核心载体 Algorithm 1 放在 Appendix 而非正文。审稿人可能认为 contribution 的核心要素应在正文中出现，至少以简化形式。
- [info] [贡献-范围] 无孤儿章节。所有正文内容均可追溯到三条贡献中的至少一条。

=== Claim 强度匹配 ===

- [warning] [Claim强度] Abstract 中 "reduces exposure bias from 61\% to <1\%" 的 "61\%" 未加近似限定词，而 e2e-real-cm 表中 naive exposure bias 实际范围为 59.3%--68.9%（中位数 ~61.4%）。Conclusion 正确使用了 "~61%"。Abstract 应与 Conclusion 保持一致，使用 "~61%" 或 "$\sim$61\%"。
- [warning] [Claim强度] "61%" 在论文中同时表示两个不同含义：(a) exposure bias 幅度（~61%，case study 表），(b) sign reversal 率（14/23 = 61%，empirical validation）。虽然上下文可区分，但同一数字的巧合可能在快速阅读时造成混淆。建议在其中一处使用更精确表述（如 "14 of 23 configurations (61%)" vs "median bias of ~61%"）以加强区分。
- [info] [Claim强度] "state-of-the-art" 仅出现在引用他人结果的语境中（\citet{baumann2025}），不是对本文方法的自我声称。合规。
- [info] [Claim强度] "provably ineffective" / "provably futile" 用于 FWL invariance 下 matrix-based corrections，有 Appendix 完整数学证明支撑，且 Limitations 已注明线性 SEM 假设。合规。
- [info] [Claim强度] Conjecture 1 诚实标注为 conjecture 而非 theorem，辅以 545,945 adversarial curves 数值验证。措辞恰当。

=== 实验严谨性 ===

- [info] [实验严谨性] Table 1 (taxonomy) 报告 100,000 模拟的比率，本质是 population-level 统计量，不需要 error bars。e2e demo 表有 ± 标注。合适。
- [info] [实验严谨性] Baselines 来自 2006--2023 年（MC-SIMEX, MLA, DSL, PPI++），涵盖经典方法和近年方法。对于方法分析型论文而言合理。
- [info] [实验严谨性] Ablation 充分：跨 K (3,5,7,10)、跨 DGP 参数、跨 confusion matrix 结构、跨 proportionality 程度。

=== 可复现性披露 ===

- [info] [可复现性] 实验参数（N=10,000, K=3, Dirichlet(1,1,1) prior, DGP 参数）在正文和 Appendix 中充分记载。
- [info] [可复现性] "Reproduction code and numerical results are included in the supplementary material" 多次出现。
- [info] [可复现性] 本文为模拟研究，不涉及 GPU 训练，无需报告 GPU hours/training time。

=== 符号/术语一致性 ===

- [warning] [术语] experiments.tex:103 首次使用 "DSL" 缩写（Design-based Supervised Learning）时未展开全称，仅引用了文献。应在首次使用时展开为 "Design-based Supervised Learning (DSL)"。
- [info] [符号] $\tau$, $C$, $\delta$, $B(C)$ 等核心符号在全文中含义一致。Notation table (Appendix Table 7) 提供完整汇总。
- [info] [术语] 所有主要缩写（LLM, DAG, ASV, FWL, SEM, OLS, MAPE, MLA, MC-SIMEX, IV, NLP, RMSE）在首次使用时均有定义。

=== 章节过渡与逻辑流 ===

- [info] [逻辑流] 无显式 Discussion 章节。结果解读嵌入在 Experiments 各小节的段尾和 Conclusion 中。这在 ML 论文中常见，但审稿人可能期望更高层次的 implications 讨论（如 "what does this mean for the CSS community?" 超越数字层面的解读）。

=== Limitations 诚实度 ===

- [info] [Limitations] 约 80 词，覆盖 3 个 distinct limitations：(1) 线性 SEM 假设 + 97.3% 非比例效应下 sign preservation，(2) 已知 DAG + 非差异性假设，(3) gold labels for C^{-1} + general K monotonicity 开放问题。符合 EMNLP 规则"一小段，覆盖 3 个点左右"。
- [info] [Limitations] 实质性而非回避式——明确指出具体假设及违反时的后果，而非泛泛说 "future work will address..."。

=== 去 AI 风格 ===

- [info] [去AI] em-dash (—) 扫描: 0 处。合规。
- [info] [去AI] 解释性 en-dash ( – ) 扫描: 0 处。合规。
- [info] [去AI] filler words ("it is worth noting", "notably", "importantly", "delve", "leverage", "utilize", "a myriad", "a plethora") 扫描: 0 处。合规。
- [info] [去AI] 段落长度适当，无过度分段现象（2-3 句一段）。

=== 内部信息残留 ===

- [info] [内部信息] 语义级扫描未发现内部实验编号、服务器标识、内部流程引用。
- [info] [内部信息] AI assistants disclosure (Appendix) 正确披露了 Claude 的使用。

=== 用户自定义规则检查 ===

- [info] [写作规则] Abstract 约 182 词，< 200 词限制。合规。
- [info] [写作规则] Limitations 章节仅在 conclusion.tex 正文中出现一次（\section*{Limitations}），Appendix 无重复 Limitations section。合规。
- [info] [写作规则] ARR Responsible NLP Checklist 未出现在论文 PDF 中（正确，应在 OpenReview submission form 中手动填写）。合规。
- [warning] [审稿规则] 正文页数需确认 ≤ 8 页。Phase 1 报告总页数 34（含 Appendix），但未单独报告正文页数。建议编译确认正文部分（到 \appendix 之前）不超过 8 页。考虑到正文包含 2 个 figure*（双栏全宽图）+ 3 个 figure + 2 个 table + 大量公式和定理环境，页面压力较大。

=== 数字一致性交叉检查 ===

- [info] [数字一致性] 83.4% (exposure sign reversal), 52.6% (IV sign reversal), 1.6% MAPE, 161 scenarios, 23 configurations, 14/23 (61%), ρ=-0.10/p=0.45 等关键数字在 Abstract/Intro/Method/Experiments 各处出现均一致。

[CONTENT_AUDIT_END]
```

**总结**: 1 critical, 3 warning, 若干 info。最严重的问题是 Conclusion 关于 IV correction 的过度泛化声明，与 Appendix correction table 的数据矛盾。

[AUDIT_DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7d35fa7-9c6a-41f5-9e69-b0345d008ced",
  "isSidechain": false,
  "requestId": "req_011CbNxyYvuqpTnccWfxKht1",
  "type": "assistant",
  "uuid": "6a43b672-99a3-4bb4-b021-31e9be0e6198",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/paper_audit_content_d519999a",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNBXdyFLwnzMUo2GYB5KuV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2978,
      "cache_read_input_tokens": 120046,
      "output_tokens": 13416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2978,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13416,
          "cache_read_input_tokens": 120046,
          "cache_creation_input_tokens": 2978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2978
          },
          "type": "message"
        }
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

_source line 90_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：causal_annot_error_attrib Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 92 warning 一…",
  "leafUuid": "6a43b672-99a3-4bb4-b021-31e9be0e6198",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb"
}
```

---

### Runtime record

_source line 91_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit causal annotation error attribution paper",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb"
}
```

---

### Runtime record

_source line 92_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：causal_annot_error_attrib Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 92 warning 一…",
  "leafUuid": "6a43b672-99a3-4bb4-b021-31e9be0e6198",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb"
}
```

---

### Runtime record

_source line 93_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit causal annotation error attribution paper",
  "sessionId": "f2d04d29-82a6-45e9-9418-9059a8b7c0cb"
}
```

---
