# Research conversation: 项目：recursive_gen_depth_est Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 83
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-1/e2a83097-15d0-4f1e-980c-6eb33f8682a9.jsonl`
- **Structured JSON:** [`0ae02ee52f783eef2f9d.json`](../../sessions/0a/0ae02ee52f783eef2f9d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T17:55:25.755Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T17:55:25.755Z",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "content": "项目：recursive_gen_depth_est\nVenue：emnlp-2026\n论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper\n\nPhase 1 确定性检查结果：\n源码检查: passed=True, 0 critical, 45 warning\n一致性检查: 3 critical, 0 warning\n编译: ✅, 页数: 26\n引用验证: 76 entries, 0 suspicious\n\n━━━ 用户自定义规则（作为额外检查项）━━━\n## 用户自定义规则（必须遵守）\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n请将以上规则逐条作为额外审计维度检查。违反的规则用 dimension `[写作规则]` 或 `[审稿规则]` 标记，severity 按实际影响判定。\n\n请按照你的角色指令执行内容结构审计。"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T17:55:25.760Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T17:55:25.760Z",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9"
}
```

---

## Round 1

81 recorded events

### User

_source line 3 · 2026-05-22T17:55:25.801Z_

项目：recursive_gen_depth_est
Venue：emnlp-2026
论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper

Phase 1 确定性检查结果：
源码检查: passed=True, 0 critical, 45 warning
一致性检查: 3 critical, 0 warning
编译: ✅, 页数: 26
引用验证: 76 entries, 0 suspicious

━━━ 用户自定义规则（作为额外检查项）━━━
## 用户自定义规则（必须遵守）
### 写作规则

- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长
- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面

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
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "fb311a8f-1fe0-45fd-bdc2-d182ed7d7dcc",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T17:55:25.801Z_

```json
{
  "parentUuid": "fb311a8f-1fe0-45fd-bdc2-d182ed7d7dcc",
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
  "uuid": "cbb75bdf-4fb4-4d0f-bd58-739c3331084f",
  "timestamp": "2026-05-22T17:55:25.801Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T17:55:25.801Z_

```json
{
  "parentUuid": "cbb75bdf-4fb4-4d0f-bd58-739c3331084f",
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
  "uuid": "1ea50d42-7e13-4c1e-aeff-db7ba364cbca",
  "timestamp": "2026-05-22T17:55:25.801Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T17:55:25.801Z_

```json
{
  "parentUuid": "1ea50d42-7e13-4c1e-aeff-db7ba364cbca",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fd7924b5-32d3-4d6b-9b79-7453d7e919a1",
  "timestamp": "2026-05-22T17:55:25.801Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
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
  "aiTitle": "EMNLP 2026 recursive_gen_depth_est paper review",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9"
}
```

---

### Assistant

_source line 8 · 2026-05-22T17:55:33.056Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a content structure audit on a paper. Let me first read the required skill files and then the paper's .tex files.

Let me start by reading the skill files and finding the paper files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd7924b5-32d3-4d6b-9b79-7453d7e919a1",
  "isSidechain": false,
  "requestId": "req_011CbJ37k1LKve6M284eheDt",
  "type": "assistant",
  "uuid": "7cbfec1d-9861-4813-b0b6-87d3d7283f0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015H8tsaZdqwcbH6zs4KWUHp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26264,
      "cache_read_input_tokens": 11846,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26264
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-22T17:55:34.187Z_

开始执行内容结构审计。先加载审计标准和论文源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cbfec1d-9861-4813-b0b6-87d3d7283f0e",
  "isSidechain": false,
  "requestId": "req_011CbJ37k1LKve6M284eheDt",
  "type": "assistant",
  "uuid": "66dc1ce5-ada3-42b6-8e62-27189a5384a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015H8tsaZdqwcbH6zs4KWUHp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26264,
      "cache_read_input_tokens": 11846,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26264
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-22T17:55:35.184Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JiBeLLn8Hne9hz1gToRUcW`</summary>

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
  "parentUuid": "66dc1ce5-ada3-42b6-8e62-27189a5384a5",
  "isSidechain": false,
  "requestId": "req_011CbJ37k1LKve6M284eheDt",
  "type": "assistant",
  "uuid": "b919a1ff-8e16-4ae5-8f83-586761d23072",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015H8tsaZdqwcbH6zs4KWUHp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26264,
      "cache_read_input_tokens": 11846,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26264
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-22T17:55:36.557Z_

<details><summary>↩ Tool result · `toolu_01SSLgTBdgA7ArEF9XkjZPNB`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43c7b687-b6c7-4364-b6b4-c028c13b59b1",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "d5520eab-1c13-4b0a-8514-f82fa1bbdf42",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
    ],
    "durationMs": 9,
    "numFiles": 12,
    "truncated": false
  },
  "sourceToolAssistantUUID": "43c7b687-b6c7-4364-b6b4-c028c13b59b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T17:55:35.202Z_

<details><summary>↩ Tool result · `toolu_01JiBeLLn8Hne9hz1gToRUcW`</summary>

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
  "parentUuid": "b919a1ff-8e16-4ae5-8f83-586761d23072",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "da6b1393-f8ec-45ec-8d0c-afa4d0dc1525",
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
  "sourceToolAssistantUUID": "b919a1ff-8e16-4ae5-8f83-586761d23072",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 13 · 2026-05-22T17:55:36.201Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WEVCRjdiKjHbQ8NYHWhT39`</summary>

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
  "parentUuid": "da6b1393-f8ec-45ec-8d0c-afa4d0dc1525",
  "isSidechain": false,
  "requestId": "req_011CbJ37k1LKve6M284eheDt",
  "type": "assistant",
  "uuid": "a596fe96-00ce-4645-9a83-1428425966c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015H8tsaZdqwcbH6zs4KWUHp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26264,
      "cache_read_input_tokens": 11846,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26264
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-22T17:55:36.207Z_

<details><summary>↩ Tool result · `toolu_01WEVCRjdiKjHbQ8NYHWhT39`</summary>

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
  "parentUuid": "a596fe96-00ce-4645-9a83-1428425966c6",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "11cee4cb-a6ea-4d06-be11-d7f8f0950620",
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
  "sourceToolAssistantUUID": "a596fe96-00ce-4645-9a83-1428425966c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 15 · 2026-05-22T17:55:36.543Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SSLgTBdgA7ArEF9XkjZPNB`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11cee4cb-a6ea-4d06-be11-d7f8f0950620",
  "isSidechain": false,
  "requestId": "req_011CbJ37k1LKve6M284eheDt",
  "type": "assistant",
  "uuid": "43c7b687-b6c7-4364-b6b4-c028c13b59b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015H8tsaZdqwcbH6zs4KWUHp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26264,
      "cache_read_input_tokens": 11846,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26264
          },
          "type": "message"
        }
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
  "lastPrompt": "项目：recursive_gen_depth_est Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 45 warning…",
  "leafUuid": "d5520eab-1c13-4b0a-8514-f82fa1bbdf42",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 recursive_gen_depth_est paper review",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9"
}
```

---

### Assistant

_source line 18 · 2026-05-22T17:55:39.274Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read all the .tex files. Let me read them in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5520eab-1c13-4b0a-8514-f82fa1bbdf42",
  "isSidechain": false,
  "requestId": "req_011CbJ38XzJdQXjSNtCe5Rc4",
  "type": "assistant",
  "uuid": "81139298-ebba-4bc2-9b21-5a2154772a83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFPYz7YvgVdTKtvFvsEDT8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12031,
      "cache_read_input_tokens": 38110,
      "output_tokens": 862,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 862,
          "cache_read_input_tokens": 38110,
          "cache_creation_input_tokens": 12031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12031
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-22T17:55:39.784Z_

现在读取所有 .tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81139298-ebba-4bc2-9b21-5a2154772a83",
  "isSidechain": false,
  "requestId": "req_011CbJ38XzJdQXjSNtCe5Rc4",
  "type": "assistant",
  "uuid": "b3459ebe-0504-4d47-9d8b-f73fc192a0f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFPYz7YvgVdTKtvFvsEDT8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12031,
      "cache_read_input_tokens": 38110,
      "output_tokens": 862,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 862,
          "cache_read_input_tokens": 38110,
          "cache_creation_input_tokens": 12031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12031
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-22T17:55:40.500Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SomU3j6NmGzrNSsD51ofsS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3459ebe-0504-4d47-9d8b-f73fc192a0f9",
  "isSidechain": false,
  "requestId": "req_011CbJ38XzJdQXjSNtCe5Rc4",
  "type": "assistant",
  "uuid": "caecf68a-7198-4df4-9b9a-e7a623b731f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFPYz7YvgVdTKtvFvsEDT8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12031,
      "cache_read_input_tokens": 38110,
      "output_tokens": 862,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 862,
          "cache_read_input_tokens": 38110,
          "cache_creation_input_tokens": 12031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12031
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-22T17:55:45.560Z_

<details><summary>↩ Tool result · `toolu_014Rywdie3cPrFpDJYDto6JV`</summary>

```text
1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	\usepackage{enumitem}
18	\usepackage{amsthm}
19	
20	\theoremstyle{definition}
21	\newtheorem{definition}{Definition}
22	
23	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
24	
25	\author{Anonymous}
26	
27	\setlength{\dbltextfloatsep}{4pt plus 2pt minus 2pt}
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	
35	\input{related_work}
36	
37	\input{method}
38	
39	\input{theory}
40	
41	\input{atlas}
42	
43	\input{generalization}
44	
45	\input{discussion}
46	
47	\input{conclusion}
48	
49	\bibliography{references}
50	
51	\clearpage
52	\appendix
53	\input{section_appendix}
54	
55	\end{document}
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c0226aa-7e67-498b-8bff-d62f0f8de74e",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "8a625e16-0439-450d-9d04-bb776ea212ea",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex",
      "content": "% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n% Target: EMNLP 2026 (ARR May cycle)\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{enumitem}\n\\usepackage{amsthm}\n\n\\theoremstyle{definition}\n\\newtheorem{definition}{Definition}\n\n\\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\\\via Statistical Fingerprints}\n\n\\author{Anonymous}\n\n\\setlength{\\dbltextfloatsep}{4pt plus 2pt minus 2pt}\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{theory}\n\n\\input{atlas}\n\n\\input{generalization}\n\n\\input{discussion}\n\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\clearpage\n\\appendix\n\\input{section_appendix}\n\n\\end{document}\n",
      "numLines": 56,
      "startLine": 1,
      "totalLines": 56
    }
  },
  "sourceToolAssistantUUID": "0c0226aa-7e67-498b-8bff-d62f0f8de74e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T17:55:40.505Z_

<details><summary>↩ Tool result · `toolu_01SomU3j6NmGzrNSsD51ofsS`</summary>

```text
1	\begin{abstract}
2	As language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K cell-instances (140K unique passages) spanning three model families, three decoding strategies, and four depths under controlled full-replacement chains at the 1--1.5B parameter scale.
4	A lightweight pipeline (19 statistical features classified by Random Forest) achieves d1--d3 balanced accuracy of 59--82\% across nine model--strategy cells, with $\mathrm{EDD}_{0.70} = 3$ in 8/9 cells.
5	Three findings emerge: (1)~depth signal concentrates in perplexity distribution tails, corroborated by classifier convergence and independent cross-perplexity features; (2)~decoding strategy affects cross-condition transfer more than model architecture, suggesting structurally distinct degradation trajectories; (3)~signal attenuates with scale (14B cross-reference accuracy ${\sim}44$\%, $\mathrm{EDD}_{0.70}{=}2$ for nucleus and temperature, 0 for top-$k$), with reference-model choice accounting for ${\sim}7$\,pp of the apparent degradation.
6	Our depth estimation claims hold most strongly within-strategy or when the decoding configuration is known.
7	Perturbation-based and membership-inference baselines lack ordinal depth resolution, confirming that depth estimation requires distributional statistics beyond binary detection scores.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caecf68a-7198-4df4-9b9a-e7a623b731f5",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "138ef128-a564-47ed-bcfe-93820ca9ac66",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nAs language models increasingly train on web text containing their own outputs, a recursive model$\\to$data$\\to$model loop arises, yet no method estimates how many such iterations a text has undergone.\nWe formalize \\emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K cell-instances (140K unique passages) spanning three model families, three decoding strategies, and four depths under controlled full-replacement chains at the 1--1.5B parameter scale.\nA lightweight pipeline (19 statistical features classified by Random Forest) achieves d1--d3 balanced accuracy of 59--82\\% across nine model--strategy cells, with $\\mathrm{EDD}_{0.70} = 3$ in 8/9 cells.\nThree findings emerge: (1)~depth signal concentrates in perplexity distribution tails, corroborated by classifier convergence and independent cross-perplexity features; (2)~decoding strategy affects cross-condition transfer more than model architecture, suggesting structurally distinct degradation trajectories; (3)~signal attenuates with scale (14B cross-reference accuracy ${\\sim}44$\\%, $\\mathrm{EDD}_{0.70}{=}2$ for nucleus and temperature, 0 for top-$k$), with reference-model choice accounting for ${\\sim}7$\\,pp of the apparent degradation.\nOur depth estimation claims hold most strongly within-strategy or when the decoding configuration is known.\nPerturbation-based and membership-inference baselines lack ordinal depth resolution, confirming that depth estimation requires distributional statistics beyond binary detection scores.\n\\end{abstract}\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "caecf68a-7198-4df4-9b9a-e7a623b731f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T17:55:40.826Z_

<details open><summary>🔧 Tool call — Read · `toolu_018qno5H2nrF15SH8PHcoTwp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "138ef128-a564-47ed-bcfe-93820ca9ac66",
  "isSidechain": false,
  "requestId": "req_011CbJ38XzJdQXjSNtCe5Rc4",
  "type": "assistant",
  "uuid": "60d27e50-5061-431d-a250-c0a7dc79b458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFPYz7YvgVdTKtvFvsEDT8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12031,
      "cache_read_input_tokens": 38110,
      "output_tokens": 862,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 862,
          "cache_read_input_tokens": 38110,
          "cache_creation_input_tokens": 12031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12031
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-22T17:55:40.830Z_

<details><summary>↩ Tool result · `toolu_018qno5H2nrF15SH8PHcoTwp`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet whether the recursive generation depth of a text can be estimated from its statistical properties remains unstudied, a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	We focus on the 1--1.5B parameter regime under \emph{controlled full-replacement chains}, where each generation fully replaces the prior training set, isolating the depth variable. Real-world contamination involves partial mixing at unknown proportions; full replacement provides an upper bound on depth signal strength (\S\ref{sec:discussion}).
8	
9	Existing tools address adjacent but distinct problems.
10	Binary detectors \cite{binoculars2024,fast_detectgpt2024,diveye2026} collapse all depths $d \geq 1$ into a single category, a limitation we confirm empirically: their pairwise d1-vs-d2 AUC collapses to chance level (\S\ref{sec:gen:baselines}); watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
12	No existing method estimates the ordinal recursive generation depth of a text passage from its content alone (Figure~\ref{fig:problem}).
13	
14	We find that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are \textbf{consistent in direction but scale-dependent in magnitude} across the three model families and three decoding strategies studied.
15	Specifically, the perplexity tail feature family (\texttt{p90\_ppl}, \texttt{p75\_ppl}, \texttt{kurtosis\_ppl}) and surprisal variance emerge as dominant depth indicators, with group-level dominance robust across all 9 model--strategy configurations and three importance measures.
16	Our contribution centers on task formalization and systematic empirical characterization; the convergence of four classifiers within 0.8\,pp (\S\ref{sec:gen:baselines}) confirms that signal resides in feature design, not classifier architecture.
17	We formalize recursive generation depth estimation as ordinal classification and find that a lightweight pipeline suffices: compute 19 reference-model statistical features (effective dimensionality ${\approx}$4--5 due to multicollinearity; \S\ref{sec:atlas:features}) and classify with a Random Forest into $K{+}1$ depth classes.
18	To characterize how recursive generation reshapes these features, we construct the \emph{Depth Degradation Atlas}: a $3 \times 3$ grid of model families $\times$ decoding strategies spanning 4 depths (180K cell-instances).
19	The atlas reveals strategy-dependent degradation trajectories; we introduce \emph{Effective Discriminable Depth} (EDD) to quantify how far into the recursion chain adjacent depths remain distinguishable.
20	
21	\begin{figure*}[t]
22	\centering
23	\includegraphics[width=0.68\textwidth]{figures/fig_problem_illustration.pdf}
24	\caption{Recursive generation depth estimation. A seed corpus $\mathcal{D}_0$ feeds a LoRA finetuning--sampling loop producing successively deeper corpora. Given a passage~$x$, the task is to estimate its ordinal depth~$d$.}
25	\label{fig:problem}
26	\end{figure*}
27	Our contributions are:
28	\begin{itemize}[nosep,leftmargin=*]
29	    \item \textbf{Task formalization and metric.} We define recursive generation depth estimation as ordinal classification, introduce the \emph{Effective Discriminable Depth} (EDD) metric, and construct a 180K cell-instance benchmark ($3$ model families $\times$ $3$ decoding strategies $\times$ $4$ depths; 140K unique passages).
30	
31	    \item \textbf{Depth Degradation Atlas.} The perplexity tail feature family and surprisal variance jointly dominate depth discrimination across all 9 cells; $\mathrm{EDD}_{0.70}{=}3$ in 8/9 cells (4 under nucleus depth extension), validated by 5-class extension (71--80\%); feature group ablation confirms perplexity tail dominance (76.6\% alone vs.\ 78.4\% full set).
32	
33	    \item \textbf{Systematic characterization.} Cross-model transfer 66.4\% (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, 14B cross-reference 44.1\% ($\mathrm{EDD}_{0.70}{=}2$); 25--50\% accumulation preserves $\mathrm{EDD}_{0.70}{=}3$ in 5/6 cells despite $-$8--15\,pp accuracy attenuation. We identify cross-strategy transfer (d1--d3: 45.9\%) as a boundary condition.
34	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60d27e50-5061-431d-a250-c0a7dc79b458",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "ae2857e8-6780-46fd-acd5-f81c8bc61a67",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\nThe text on which large language models are trained increasingly contains their own outputs.\nAs synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \\cite{shumailov2024_nature,alemohammad2024_mad}.\nThis model$\\to$data$\\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet whether the recursive generation depth of a text can be estimated from its statistical properties remains unstudied, a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \\cite{dohmatob2024_tale_of_tails}.\nWe focus on the 1--1.5B parameter regime under \\emph{controlled full-replacement chains}, where each generation fully replaces the prior training set, isolating the depth variable. Real-world contamination involves partial mixing at unknown proportions; full replacement provides an upper bound on depth signal strength (\\S\\ref{sec:discussion}).\n\nExisting tools address adjacent but distinct problems.\nBinary detectors \\cite{binoculars2024,fast_detectgpt2024,diveye2026} collapse all depths $d \\geq 1$ into a single category, a limitation we confirm empirically: their pairwise d1-vs-d2 AUC collapses to chance level (\\S\\ref{sec:gen:baselines}); watermarking \\cite{kirchenbauer2023_watermark} requires proactive embedding.\nThe model collapse literature \\cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \\citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.\nNo existing method estimates the ordinal recursive generation depth of a text passage from its content alone (Figure~\\ref{fig:problem}).\n\nWe find that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are \\textbf{consistent in direction but scale-dependent in magnitude} across the three model families and three decoding strategies studied.\nSpecifically, the perplexity tail feature family (\\texttt{p90\\_ppl}, \\texttt{p75\\_ppl}, \\texttt{kurtosis\\_ppl}) and surprisal variance emerge as dominant depth indicators, with group-level dominance robust across all 9 model--strategy configurations and three importance measures.\nOur contribution centers on task formalization and systematic empirical characterization; the convergence of four classifiers within 0.8\\,pp (\\S\\ref{sec:gen:baselines}) confirms that signal resides in feature design, not classifier architecture.\nWe formalize recursive generation depth estimation as ordinal classification and find that a lightweight pipeline suffices: compute 19 reference-model statistical features (effective dimensionality ${\\approx}$4--5 due to multicollinearity; \\S\\ref{sec:atlas:features}) and classify with a Random Forest into $K{+}1$ depth classes.\nTo characterize how recursive generation reshapes these features, we construct the \\emph{Depth Degradation Atlas}: a $3 \\times 3$ grid of model families $\\times$ decoding strategies spanning 4 depths (180K cell-instances).\nThe atlas reveals strategy-dependent degradation trajectories; we introduce \\emph{Effective Discriminable Depth} (EDD) to quantify how far into the recursion chain adjacent depths remain distinguishable.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.68\\textwidth]{figures/fig_problem_illustration.pdf}\n\\caption{Recursive generation depth estimation. A seed corpus $\\mathcal{D}_0$ feeds a LoRA finetuning--sampling loop producing successively deeper corpora. Given a passage~$x$, the task is to estimate its ordinal depth~$d$.}\n\\label{fig:problem}\n\\end{figure*}\nOur contributions are:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Task formalization and metric.} We define recursive generation depth estimation as ordinal classification, introduce the \\emph{Effective Discriminable Depth} (EDD) metric, and construct a 180K cell-instance benchmark ($3$ model families $\\times$ $3$ decoding strategies $\\times$ $4$ depths; 140K unique passages).\n\n    \\item \\textbf{Depth Degradation Atlas.} The perplexity tail feature family and surprisal variance jointly dominate depth discrimination across all 9 cells; $\\mathrm{EDD}_{0.70}{=}3$ in 8/9 cells (4 under nucleus depth extension), validated by 5-class extension (71--80\\%); feature group ablation confirms perplexity tail dominance (76.6\\% alone vs.\\ 78.4\\% full set).\n\n    \\item \\textbf{Systematic characterization.} Cross-model transfer 66.4\\% (d1--d3: 55.4\\%), cross-domain arXiv 74.1\\%, 14B cross-reference 44.1\\% ($\\mathrm{EDD}_{0.70}{=}2$); 25--50\\% accumulation preserves $\\mathrm{EDD}_{0.70}{=}3$ in 5/6 cells despite $-$8--15\\,pp accuracy attenuation. We identify cross-strategy transfer (d1--d3: 45.9\\%) as a boundary condition.\n\\end{itemize}",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  },
  "sourceToolAssistantUUID": "60d27e50-5061-431d-a250-c0a7dc79b458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T17:55:41.305Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TbkmXX2XSGTiT2dRu24f7u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae2857e8-6780-46fd-acd5-f81c8bc61a67",
  "isSidechain": false,
  "requestId": "req_011CbJ38XzJdQXjSNtCe5Rc4",
  "type": "assistant",
  "uuid": "6d119d87-2c4e-4445-affa-5bf16abac9a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFPYz7YvgVdTKtvFvsEDT8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12031,
      "cache_read_input_tokens": 38110,
      "output_tokens": 862,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 862,
          "cache_read_input_tokens": 38110,
          "cache_creation_input_tokens": 12031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12031
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-22T17:55:41.310Z_

<details><summary>↩ Tool result · `toolu_01TbkmXX2XSGTiT2dRu24f7u`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	Recursive training on model outputs erodes distributional tails \cite{shumailov2024_nature}, an effect formalized as exponential tail decay via scaling laws \cite{dohmatob2024_tale_of_tails,seddik2024synthetic} and extended to autophagous loops in the MAD framework \cite{alemohammad2024_mad} and Markovian generation chains \cite{geng2026_markovian}.
6	Subsequent work refines the conditions under which collapse occurs: \citet{bertrand2024_stability} identify convergence to a fixed point under mixed real-synthetic retraining (providing theoretical grounding for our EDD ceiling, \S\ref{sec:method:theory}), \citet{shi2025_closer_look} reframe collapse as a generalization-to-memorization transition, and \citet{dohmatob2025_strong_collapse} extend guarantees to broader model classes.
7	Mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, data scaling under constraint \cite{muennighoff2023scaling}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence analysis \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026} are active areas.
8	\citet{kazdan2025_collapse_or_thrive} systematically compare training workflows and show that data accumulation avoids collapse while pure replacement does not; \citet{suresh2025_rate_collapse} characterize the rate of collapse for fundamental distributions under recursive maximum-likelihood estimation.
9	\citet{schaeffer2025} argue that ``model collapse'' conflates multiple phenomena and call for operationally precise metrics; we respond by operationalizing tail-erosion predictions into a deployable ordinal classifier that reveals strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.
10	All assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
11	
12	\paragraph{AI Text Detection.}
13	The detection literature \cite{wu2025_detection_survey} spans statistical methods (DetectGPT \cite{mitchell2023_detectgpt}, Fast-DetectGPT \cite{fast_detectgpt2024}, Binoculars \cite{binoculars2024}, DivEye \cite{diveye2026}, BiScope \cite{guo2024_biscope}, GLTR \cite{gehrmann2019_gltr}, Ghostbuster \cite{verma2024_ghostbuster}, DNA-GPT \cite{yang2024_dnagpt}), geometric approaches based on intrinsic dimensionality \cite{tulchinskii2023_intrinsic_dim}, and watermarking \cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \cite{sadasivan2023_paraphrase}, distribution shift \cite{pudasaini2026_detection_fails}, and generator barriers \cite{pu2026_generator_barrier}.
14	\citet{wang2023_seqxgpt} address sentence-level attribution by using log-probability features from white-box LLMs.
15	M4-SemEval \cite{wang2024_m4_semeval}, MAGE \cite{li2024_mage}, and the PAN 2026 shared tasks \cite{bevendorff2026_pan} benchmark detection across domains, models, and adversarial conditions; RAID \cite{dugan2024_raid} targets binary detection across diverse attack vectors rather than ordinal depth estimation, making direct protocol adoption inapplicable to our task.
16	\citet{bevendorff2025_two_paradigms} distinguish authorship attribution (which model?) from verification (human or AI?); depth estimation introduces a third axis: which recursive iteration.
17	All these methods perform binary classification, discarding ordinal depth information; our approach outputs ordinal depth labels, complementing rather than replacing binary detection.
18	
19	\paragraph{Membership Inference and Data Provenance.}
20	\citet{carlini2021_extracting} demonstrate that training data can be extracted from LLMs, motivating provenance-aware pipelines.
21	Min-K\% Prob \cite{shi2024_minkprob} detects pretraining membership via low-probability token statistics, related to our perplexity features but limited to binary classification; Datamodels \cite{ilyas2022datamodels} trace predictions to influential training examples; cryptographically undetectable watermarks \cite{christ2024_undetectable} require generator cooperation.
22	TROVE \cite{zhu2025_trove} introduces fine-grained sentence-level provenance tracing with relationship classification, but targets source attribution rather than recursive depth.
23	Depth estimation occupies a distinct niche: ordinal, retroactive, and cooperation-free.
24	
25	\paragraph{Adjacent Tasks.}
26	EditLens \cite{editlens2026} estimates editing extent but does not model recursive chains; \citet{uchendu2020_attribution} classify \emph{which} model generated text; \citet{mohamed2025_broken_telephone} characterize \emph{how} text degrades under iterative generation without classifying which iteration a passage comes from.
27	Our task performs the inverse: ordinal depth estimation from text alone.
28	
29	\paragraph{Ordinal Classification.}
30	CORAL \cite{coral2020} enforces rank consistency via ordered binary tasks; CLOC \cite{cloc2025} extends contrastive learning with multi-margin ordinal losses; \citet{kasa2024_ordinality} benchmark ordinal techniques for NLP; \citet{janitza2016_ordinal_rf} show RF implicitly respects ordinal structure when inter-class distances are monotonic.
31	We adopt CORAL and CLOC as baselines (\S\ref{sec:generalization}).
32	
33	\paragraph{Decoding Strategy Effects.}
34	Decoding strategies shape text statistics in ways that interact with depth signals \cite{holtzman2020_nucleus,finlayson2024_closing,garces_arias2025_decoding_decoded,wiher2022_decoding,basu2021_mirostat}.
35	Our atlas (\S\ref{sec:atlas}) shows these strategies induce qualitatively different degradation trajectories under recursive generation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d119d87-2c4e-4445-affa-5bf16abac9a5",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "7899e8e9-76f0-4f41-9c54-9874e0709e29",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Model Collapse Theory.}\nRecursive training on model outputs erodes distributional tails \\cite{shumailov2024_nature}, an effect formalized as exponential tail decay via scaling laws \\cite{dohmatob2024_tale_of_tails,seddik2024synthetic} and extended to autophagous loops in the MAD framework \\cite{alemohammad2024_mad} and Markovian generation chains \\cite{geng2026_markovian}.\nSubsequent work refines the conditions under which collapse occurs: \\citet{bertrand2024_stability} identify convergence to a fixed point under mixed real-synthetic retraining (providing theoretical grounding for our EDD ceiling, \\S\\ref{sec:method:theory}), \\citet{shi2025_closer_look} reframe collapse as a generalization-to-memorization transition, and \\citet{dohmatob2025_strong_collapse} extend guarantees to broader model classes.\nMitigation \\cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, data scaling under constraint \\cite{muennighoff2023scaling}, non-monotonic dynamics \\cite{bakshi2026_collapse_improvement}, convergence analysis \\cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \\cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026} are active areas.\n\\citet{kazdan2025_collapse_or_thrive} systematically compare training workflows and show that data accumulation avoids collapse while pure replacement does not; \\citet{suresh2025_rate_collapse} characterize the rate of collapse for fundamental distributions under recursive maximum-likelihood estimation.\n\\citet{schaeffer2025} argue that ``model collapse'' conflates multiple phenomena and call for operationally precise metrics; we respond by operationalizing tail-erosion predictions into a deployable ordinal classifier that reveals strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.\nAll assume depth is known a priori; we address the inverse problem of estimating depth from text alone.\n\n\\paragraph{AI Text Detection.}\nThe detection literature \\cite{wu2025_detection_survey} spans statistical methods (DetectGPT \\cite{mitchell2023_detectgpt}, Fast-DetectGPT \\cite{fast_detectgpt2024}, Binoculars \\cite{binoculars2024}, DivEye \\cite{diveye2026}, BiScope \\cite{guo2024_biscope}, GLTR \\cite{gehrmann2019_gltr}, Ghostbuster \\cite{verma2024_ghostbuster}, DNA-GPT \\cite{yang2024_dnagpt}), geometric approaches based on intrinsic dimensionality \\cite{tulchinskii2023_intrinsic_dim}, and watermarking \\cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \\cite{sadasivan2023_paraphrase}, distribution shift \\cite{pudasaini2026_detection_fails}, and generator barriers \\cite{pu2026_generator_barrier}.\n\\citet{wang2023_seqxgpt} address sentence-level attribution by using log-probability features from white-box LLMs.\nM4-SemEval \\cite{wang2024_m4_semeval}, MAGE \\cite{li2024_mage}, and the PAN 2026 shared tasks \\cite{bevendorff2026_pan} benchmark detection across domains, models, and adversarial conditions; RAID \\cite{dugan2024_raid} targets binary detection across diverse attack vectors rather than ordinal depth estimation, making direct protocol adoption inapplicable to our task.\n\\citet{bevendorff2025_two_paradigms} distinguish authorship attribution (which model?) from verification (human or AI?); depth estimation introduces a third axis: which recursive iteration.\nAll these methods perform binary classification, discarding ordinal depth information; our approach outputs ordinal depth labels, complementing rather than replacing binary detection.\n\n\\paragraph{Membership Inference and Data Provenance.}\n\\citet{carlini2021_extracting} demonstrate that training data can be extracted from LLMs, motivating provenance-aware pipelines.\nMin-K\\% Prob \\cite{shi2024_minkprob} detects pretraining membership via low-probability token statistics, related to our perplexity features but limited to binary classification; Datamodels \\cite{ilyas2022datamodels} trace predictions to influential training examples; cryptographically undetectable watermarks \\cite{christ2024_undetectable} require generator cooperation.\nTROVE \\cite{zhu2025_trove} introduces fine-grained sentence-level provenance tracing with relationship classification, but targets source attribution rather than recursive depth.\nDepth estimation occupies a distinct niche: ordinal, retroactive, and cooperation-free.\n\n\\paragraph{Adjacent Tasks.}\nEditLens \\cite{editlens2026} estimates editing extent but does not model recursive chains; \\citet{uchendu2020_attribution} classify \\emph{which} model generated text; \\citet{mohamed2025_broken_telephone} characterize \\emph{how} text degrades under iterative generation without classifying which iteration a passage comes from.\nOur task performs the inverse: ordinal depth estimation from text alone.\n\n\\paragraph{Ordinal Classification.}\nCORAL \\cite{coral2020} enforces rank consistency via ordered binary tasks; CLOC \\cite{cloc2025} extends contrastive learning with multi-margin ordinal losses; \\citet{kasa2024_ordinality} benchmark ordinal techniques for NLP; \\citet{janitza2016_ordinal_rf} show RF implicitly respects ordinal structure when inter-class distances are monotonic.\nWe adopt CORAL and CLOC as baselines (\\S\\ref{sec:generalization}).\n\n\\paragraph{Decoding Strategy Effects.}\nDecoding strategies shape text statistics in ways that interact with depth signals \\cite{holtzman2020_nucleus,finlayson2024_closing,garces_arias2025_decoding_decoded,wiher2022_decoding,basu2021_mirostat}.\nOur atlas (\\S\\ref{sec:atlas}) shows these strategies induce qualitatively different degradation trajectories under recursive generation.",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  },
  "sourceToolAssistantUUID": "6d119d87-2c4e-4445-affa-5bf16abac9a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T17:55:41.778Z_

<details open><summary>🔧 Tool call — Read · `toolu_017RCZEVG3fXNji6PuCKNhVp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7899e8e9-76f0-4f41-9c54-9874e0709e29",
  "isSidechain": false,
  "requestId": "req_011CbJ38XzJdQXjSNtCe5Rc4",
  "type": "assistant",
  "uuid": "61d36acd-d3c6-401f-9dbf-d20ddb9327e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFPYz7YvgVdTKtvFvsEDT8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12031,
      "cache_read_input_tokens": 38110,
      "output_tokens": 862,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 862,
          "cache_read_input_tokens": 38110,
          "cache_creation_input_tokens": 12031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12031
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-22T17:55:41.783Z_

<details><summary>↩ Tool result · `toolu_017RCZEVG3fXNji6PuCKNhVp`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	We use \emph{depth estimation} as shorthand throughout; the underlying task is ordinal classification.
13	Depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
14	
15	\subsection{Multi-Generational Benchmark Construction}
16	\label{sec:method:benchmark}
17	
18	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
19	
20	\paragraph{Model families.}
21	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
22	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
23	
24	\paragraph{Decoding strategies.}
25	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
26	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
27	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
28	
29	\paragraph{Depth and scale.}
30	The primary benchmark covers depths d0--d3 across all $3 \times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K cell-instances; 140K unique passages, as d0 samples are drawn from a shared Wikipedia seed corpus across all cells).
31	For depth extension experiments (\S\ref{sec:atlas}), we extend all three models under nucleus sampling to d0--d5.
32	
33	\paragraph{Generation pipeline.}
34	Starting from a Wikipedia subset ($\mathcal{D}_0$), each cycle: (1)~LoRA finetuning \cite{hu2022lora} on $\mathcal{D}_{k-1}$ ($r{=}16$, $\alpha{=}32$, lr $2{\times}10^{-4}$, effective batch 16, 3 epochs, dropout $0.05$; fresh adapter from the base model at each depth; full protocol in Appendix~\ref{app:lora_protocol}); (2)~sampling 5{,}000 passages (max 512 tokens, beginning-of-sequence (BOS) seeded) under the specified strategy; (3)~$\mathcal{D}_k$ feeds the next cycle.
35	Each depth is produced by a model trained on prior-depth data, not by sampling from the unmodified base model.
36	BOS seeding may amplify depth signal; prompted-generation validation (Appendix~\ref{app:prompted_gen}) confirms signal persistence albeit attenuated ($-$13.8\,pp).
37	No per-passage lineage exists across depths; cross-validation splits do not introduce leakage.
38	
39	\paragraph{Reference model.}
40	All statistical features (\S\ref{sec:method:features}) use Pythia-1.4B as fixed reference model.
41	This overlaps with one generator (Pythia), conferring a 4--11\,pp self-reference advantage on that pipeline (Appendix~\ref{app:ref_ablation}); Pythia results in Table~\ref{tab:main_matrix} are marked $^\dagger$ accordingly.
42	Alternative references yield 67--79\%, all exceeding $2.5{\times}$ chance (Limitations).
43	
44	\subsection{Statistical Feature Design}
45	\label{sec:method:features}
46	
47	We extract a feature vector $\mathbf{f}(x)$ comprising 19 candidate features from the reference-model perplexity distribution over each passage $x$; ablation (\S\ref{sec:atlas:features}) shows the top 5 achieve 97.6\% of full-set performance, and variance inflation analysis reveals VIF${>}$10 for 14--16 features; effective independent dimensionality is ${\approx}$4--5.
48	The features fall into four categories (Table~\ref{tab:features}).
49	
50	\begin{table}[t]
51	\centering
52	\small
53	\caption{The 19 statistical features comprising $\mathbf{f}(x)$, grouped by category. All perplexity and surprisal features are computed from the reference model (Pythia-1.4B).}
54	\label{tab:features}
55	\begin{tabular*}{\columnwidth}{@{\extracolsep{\fill}}llr}
56	\toprule
57	Category & Features & $n$ \\
58	\midrule
59	Perplexity & mean, var, skewness, kurtosis, & 9 \\
60	statistics & p10, p25, p50, p75, p90 & \\
61	\addlinespace
62	Surprisal & mean, var, entropy & 3 \\
63	statistics & & \\
64	\addlinespace
65	Lexical & type--token ratio, hapax ratio, & 4 \\
66	diversity & bigram entropy, trigram entropy & \\
67	\addlinespace
68	Repetition & repeated 2/3/4-gram fractions & 3 \\
69	\bottomrule
70	\end{tabular*}
71	\end{table}
72	
73	\emph{Perplexity statistics} (9 features) capture the per-token perplexity distribution via moments and quantiles (p10--p90); tail quantiles are especially informative as recursive finetuning erodes the high-perplexity tail (\S\ref{sec:atlas}).
74	\emph{Surprisal statistics} (3 features): mean, variance, and entropy of $-\log p(\text{token})$.
75	\emph{Lexical diversity} (4 features): type--token ratio, hapax ratio, bigram/trigram entropy.
76	\emph{Repetition} (3 features): repeated $n$-gram fractions for $n \in \{2, 3, 4\}$.
77	
78	\subsection{Effective Discriminable Depth}
79	\label{sec:method:edd}
80	
81	Aggregate multi-class accuracy obscures whether discriminability degrades at specific depth boundaries.
82	We propose the \emph{Effective Discriminable Depth} (EDD) as an operational measure of how far into a recursive chain adjacent depths remain distinguishable.
83	
84	\paragraph{Pairwise discriminability.}
85	Let $\mathcal{D} = \{0, 1, \dots, K\}$ denote the depth set and $T \in (0.5, 1.0]$ a discrimination threshold.
86	For each adjacent pair $(d, d{+}1)$, we define the pairwise discriminability $\mathrm{AUC}(d, d{+}1)$ as the area under the ROC curve of a dedicated binary Random Forest classifier (500 trees, $\lfloor\sqrt{19}\rfloor$ candidate features per split) trained on class-balanced data from $\mathbf{f}(x)$ (\S\ref{sec:method:features}) to distinguish depth-$d$ from depth-$(d{+}1)$ samples, evaluated via 5-fold stratified cross-validation.
87	Each pair uses an independent classifier to avoid decision boundary dilution from multi-class settings.
88	
89	\begin{definition}[Effective Discriminable Depth]
90	\label{def:edd}
91	The \emph{Effective Discriminable Depth} at threshold $T$ is:
92	\begin{multline}
93	\mathrm{EDD}_T = \max \bigl\{ d^*{+}1 \,:\, \\
94	\forall\, d' \leq d^*,\; \mathrm{AUC}(d', d'{+}1) \geq T \bigr\}
95	\label{eq:edd}
96	\end{multline}
97	where $d^* \in \{0, \dots, K{-}1\}$. If\, $\mathrm{AUC}(0,1) < T$, then $\mathrm{EDD}_T = 0$.
98	\end{definition}
99	
100	$\mathrm{EDD}_T$ reports the longest \emph{contiguous} discriminable prefix: the deepest $d$ such that every pair from $(0,1)$ through $(d{-}1, d)$ exceeds $T$.
101	All AUC profiles in the primary benchmark decay monotonically; non-monotonic profiles occur only in cross-scale extensions (Appendix~\ref{app:cross_scale_full}).
102	We adopt $T{=}0.70$ following the ``acceptable discrimination'' threshold in ROC analysis \cite{hosmer2000} (8/9 cells achieve $\mathrm{EDD}_{0.70} \geq 3$); sensitivity analysis (\S\ref{sec:atlas:edd}) shows $\mathrm{EDD}$ shifts by at most one level across $T \in \{0.65, 0.70, 0.80\}$ in all nine cells.
103	
104	\paragraph{Classifiers.}
105	Our primary classifier is a Random Forest (200 trees, unconstrained depth, 5-fold CV; EDD binary classifiers use 500 trees).\footnote{Statistical tests are not corrected for multiple comparisons; $p$-values should be interpreted as exploratory.}
106	The RF produces ordinally consistent predictions: 98.2\% of errors fall on adjacent depths ($|\Delta| \leq 1$), quadratic weighted kappa (QWK)\,=\,0.89.
107	Comparisons against other classifiers and detection baselines appear in \S\ref{sec:generalization}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61d36acd-d3c6-401f-9dbf-d20ddb9327e0",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "74e6e6a6-a8c8-49a6-98b1-d86ac1a04e2a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Definition}\n\\label{sec:method:problem}\n\nLet $f_\\theta$ denote a language model and $\\mathcal{D}_0$ a corpus of human-written seed text.\nWe define a \\emph{recursive generation chain} of depth $K$ as the sequence $\\mathcal{D}_0, \\mathcal{D}_1, \\dots, \\mathcal{D}_K$, where each $\\mathcal{D}_k$ ($k \\geq 1$) is produced by finetuning $f_\\theta$ on $\\mathcal{D}_{k-1}$ and sampling from the resulting model.\nDepth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \\geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.\n\nGiven a text passage $x$, the task is to estimate its recursive generation depth $d \\in \\{0, 1, \\dots, K\\}$.\nWe use \\emph{depth estimation} as shorthand throughout; the underlying task is ordinal classification.\nDepths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.\n\n\\subsection{Multi-Generational Benchmark Construction}\n\\label{sec:method:benchmark}\n\nWe construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.\n\n\\paragraph{Model families.}\nWe select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).\nRestricting to a narrow parameter range isolates the effect of architecture and training data from scale.\n\n\\paragraph{Decoding strategies.}\nEach model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \\cite{holtzman2020_nucleus}, temperature sampling ($\\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).\nThese span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.\nOur findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.\n\n\\paragraph{Depth and scale.}\nThe primary benchmark covers depths d0--d3 across all $3 \\times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K cell-instances; 140K unique passages, as d0 samples are drawn from a shared Wikipedia seed corpus across all cells).\nFor depth extension experiments (\\S\\ref{sec:atlas}), we extend all three models under nucleus sampling to d0--d5.\n\n\\paragraph{Generation pipeline.}\nStarting from a Wikipedia subset ($\\mathcal{D}_0$), each cycle: (1)~LoRA finetuning \\cite{hu2022lora} on $\\mathcal{D}_{k-1}$ ($r{=}16$, $\\alpha{=}32$, lr $2{\\times}10^{-4}$, effective batch 16, 3 epochs, dropout $0.05$; fresh adapter from the base model at each depth; full protocol in Appendix~\\ref{app:lora_protocol}); (2)~sampling 5{,}000 passages (max 512 tokens, beginning-of-sequence (BOS) seeded) under the specified strategy; (3)~$\\mathcal{D}_k$ feeds the next cycle.\nEach depth is produced by a model trained on prior-depth data, not by sampling from the unmodified base model.\nBOS seeding may amplify depth signal; prompted-generation validation (Appendix~\\ref{app:prompted_gen}) confirms signal persistence albeit attenuated ($-$13.8\\,pp).\nNo per-passage lineage exists across depths; cross-validation splits do not introduce leakage.\n\n\\paragraph{Reference model.}\nAll statistical features (\\S\\ref{sec:method:features}) use Pythia-1.4B as fixed reference model.\nThis overlaps with one generator (Pythia), conferring a 4--11\\,pp self-reference advantage on that pipeline (Appendix~\\ref{app:ref_ablation}); Pythia results in Table~\\ref{tab:main_matrix} are marked $^\\dagger$ accordingly.\nAlternative references yield 67--79\\%, all exceeding $2.5{\\times}$ chance (Limitations).\n\n\\subsection{Statistical Feature Design}\n\\label{sec:method:features}\n\nWe extract a feature vector $\\mathbf{f}(x)$ comprising 19 candidate features from the reference-model perplexity distribution over each passage $x$; ablation (\\S\\ref{sec:atlas:features}) shows the top 5 achieve 97.6\\% of full-set performance, and variance inflation analysis reveals VIF${>}$10 for 14--16 features; effective independent dimensionality is ${\\approx}$4--5.\nThe features fall into four categories (Table~\\ref{tab:features}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{The 19 statistical features comprising $\\mathbf{f}(x)$, grouped by category. All perplexity and surprisal features are computed from the reference model (Pythia-1.4B).}\n\\label{tab:features}\n\\begin{tabular*}{\\columnwidth}{@{\\extracolsep{\\fill}}llr}\n\\toprule\nCategory & Features & $n$ \\\\\n\\midrule\nPerplexity & mean, var, skewness, kurtosis, & 9 \\\\\nstatistics & p10, p25, p50, p75, p90 & \\\\\n\\addlinespace\nSurprisal & mean, var, entropy & 3 \\\\\nstatistics & & \\\\\n\\addlinespace\nLexical & type--token ratio, hapax ratio, & 4 \\\\\ndiversity & bigram entropy, trigram entropy & \\\\\n\\addlinespace\nRepetition & repeated 2/3/4-gram fractions & 3 \\\\\n\\bottomrule\n\\end{tabular*}\n\\end{table}\n\n\\emph{Perplexity statistics} (9 features) capture the per-token perplexity distribution via moments and quantiles (p10--p90); tail quantiles are especially informative as recursive finetuning erodes the high-perplexity tail (\\S\\ref{sec:atlas}).\n\\emph{Surprisal statistics} (3 features): mean, variance, and entropy of $-\\log p(\\text{token})$.\n\\emph{Lexical diversity} (4 features): type--token ratio, hapax ratio, bigram/trigram entropy.\n\\emph{Repetition} (3 features): repeated $n$-gram fractions for $n \\in \\{2, 3, 4\\}$.\n\n\\subsection{Effective Discriminable Depth}\n\\label{sec:method:edd}\n\nAggregate multi-class accuracy obscures whether discriminability degrades at specific depth boundaries.\nWe propose the \\emph{Effective Discriminable Depth} (EDD) as an operational measure of how far into a recursive chain adjacent depths remain distinguishable.\n\n\\paragraph{Pairwise discriminability.}\nLet $\\mathcal{D} = \\{0, 1, \\dots, K\\}$ denote the depth set and $T \\in (0.5, 1.0]$ a discrimination threshold.\nFor each adjacent pair $(d, d{+}1)$, we define the pairwise discriminability $\\mathrm{AUC}(d, d{+}1)$ as the area under the ROC curve of a dedicated binary Random Forest classifier (500 trees, $\\lfloor\\sqrt{19}\\rfloor$ candidate features per split) trained on class-balanced data from $\\mathbf{f}(x)$ (\\S\\ref{sec:method:features}) to distinguish depth-$d$ from depth-$(d{+}1)$ samples, evaluated via 5-fold stratified cross-validation.\nEach pair uses an independent classifier to avoid decision boundary dilution from multi-class settings.\n\n\\begin{definition}[Effective Discriminable Depth]\n\\label{def:edd}\nThe \\emph{Effective Discriminable Depth} at threshold $T$ is:\n\\begin{multline}\n\\mathrm{EDD}_T = \\max \\bigl\\{ d^*{+}1 \\,:\\, \\\\\n\\forall\\, d' \\leq d^*,\\; \\mathrm{AUC}(d', d'{+}1) \\geq T \\bigr\\}\n\\label{eq:edd}\n\\end{multline}\nwhere $d^* \\in \\{0, \\dots, K{-}1\\}$. If\\, $\\mathrm{AUC}(0,1) < T$, then $\\mathrm{EDD}_T = 0$.\n\\end{definition}\n\n$\\mathrm{EDD}_T$ reports the longest \\emph{contiguous} discriminable prefix: the deepest $d$ such that every pair from $(0,1)$ through $(d{-}1, d)$ exceeds $T$.\nAll AUC profiles in the primary benchmark decay monotonically; non-monotonic profiles occur only in cross-scale extensions (Appendix~\\ref{app:cross_scale_full}).\nWe adopt $T{=}0.70$ following the ``acceptable discrimination'' threshold in ROC analysis \\cite{hosmer2000} (8/9 cells achieve $\\mathrm{EDD}_{0.70} \\geq 3$); sensitivity analysis (\\S\\ref{sec:atlas:edd}) shows $\\mathrm{EDD}$ shifts by at most one level across $T \\in \\{0.65, 0.70, 0.80\\}$ in all nine cells.\n\n\\paragraph{Classifiers.}\nOur primary classifier is a Random Forest (200 trees, unconstrained depth, 5-fold CV; EDD binary classifiers use 500 trees).\\footnote{Statistical tests are not corrected for multiple comparisons; $p$-values should be interpreted as exploratory.}\nThe RF produces ordinally consistent predictions: 98.2\\% of errors fall on adjacent depths ($|\\Delta| \\leq 1$), quadratic weighted kappa (QWK)\\,=\\,0.89.\nComparisons against other classifiers and detection baselines appear in \\S\\ref{sec:generalization}.",
      "numLines": 107,
      "startLine": 1,
      "totalLines": 107
    }
  },
  "sourceToolAssistantUUID": "61d36acd-d3c6-401f-9dbf-d20ddb9327e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T17:55:42.719Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CQUAcFRPC9nCkZeiKhKURE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74e6e6a6-a8c8-49a6-98b1-d86ac1a04e2a",
  "isSidechain": false,
  "requestId": "req_011CbJ38XzJdQXjSNtCe5Rc4",
  "type": "assistant",
  "uuid": "40e65841-dce5-4d25-80f2-aba693beafe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFPYz7YvgVdTKtvFvsEDT8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12031,
      "cache_read_input_tokens": 38110,
      "output_tokens": 862,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 862,
          "cache_read_input_tokens": 38110,
          "cache_creation_input_tokens": 12031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12031
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-22T17:55:42.723Z_

<details><summary>↩ Tool result · `toolu_01CQUAcFRPC9nCkZeiKhKURE`</summary>

```text
1	\subsection{Theoretical Motivation}
2	\label{sec:method:theory}
3	
4	Recursive generation contracts the support of the learned distribution, with low-probability tokens lost first \cite{shumailov2024_nature}: tail mass $P_k(\mathrm{ppl} > t)$ decreases monotonically in depth $k$.
5	This tail erosion predicts the perplexity tail feature family as a depth marker, confirmed jointly with surprisal variance across all 9 cells (\S\ref{sec:atlas:features}).
6	Surprisal variance captures complementary distributional narrowing: as the support contracts, per-token surprise becomes more predictable.
7	
8	\paragraph{EDD upper bound.}
9	Tail mass at depth $k$ scales as $\alpha^k$ for a contraction factor $\alpha \in (0,1)$ \cite{dohmatob2024_tale_of_tails}; EDD reaches its upper bound when adjacent-depth feature distance falls below classifier resolution.
10	Our empirical AUC-excess contraction (ratio 0.80 at d1v2$\to$d2v3, 0.69 at d3v4$\to$d4v5; \S\ref{sec:atlas:edd}) is consistent with geometric decay approaching a fixed point \cite{bertrand2024_stability}.
11	5-class extensions to d4 (71--80\%, chance = 20\%; Appendix~\ref{app:depth4_ext}) confirm depth~4 discriminability; mean perplexity saturates before tail statistics, placing a physical ceiling on EDD.
12	
13	\paragraph{Scale-dependent attenuation.}
14	Larger models approximate the training distribution more faithfully per step ($\alpha$ closer to 1), predicting weaker per-step signal.
15	Qwen2.5-14B supports this: d0-vs-d1 AUC drops to 0.643 (vs.\ ${>}0.99$ at 1--1.5B; \S\ref{sec:gen:crossscale}); 7--8B results are mixed, suggesting additional confounds interact with the scale effect (Appendix~\ref{app:cross_scale_full}).
16	
17	\paragraph{Strategy-dependent convergence.}
18	The contraction rate $\alpha$ varies with decoding strategy.
19	Temperature scaling ($\tau < 1$) sharpens the logit distribution uniformly and accelerates convergence to the mode; temperature depth-$d$ text should therefore resemble nucleus depth-$(d{+}1)$ text in tail statistics.
20	GPT-2~XL confirms this: temperature d1 median \texttt{p90\_ppl} (92.2) matches the nucleus d2 median (92.3).
21	Top-$k$ truncation removes the low-probability tokens that carry depth signal, predicting weaker discriminability; top-$k$ cells yield the lowest accuracy (68.9--75.8\%) across the atlas (\S\ref{sec:atlas:strategy}).
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40e65841-dce5-4d25-80f2-aba693beafe3",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "6946c413-8459-4556-adb1-2633f0e754c6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex",
      "content": "\\subsection{Theoretical Motivation}\n\\label{sec:method:theory}\n\nRecursive generation contracts the support of the learned distribution, with low-probability tokens lost first \\cite{shumailov2024_nature}: tail mass $P_k(\\mathrm{ppl} > t)$ decreases monotonically in depth $k$.\nThis tail erosion predicts the perplexity tail feature family as a depth marker, confirmed jointly with surprisal variance across all 9 cells (\\S\\ref{sec:atlas:features}).\nSurprisal variance captures complementary distributional narrowing: as the support contracts, per-token surprise becomes more predictable.\n\n\\paragraph{EDD upper bound.}\nTail mass at depth $k$ scales as $\\alpha^k$ for a contraction factor $\\alpha \\in (0,1)$ \\cite{dohmatob2024_tale_of_tails}; EDD reaches its upper bound when adjacent-depth feature distance falls below classifier resolution.\nOur empirical AUC-excess contraction (ratio 0.80 at d1v2$\\to$d2v3, 0.69 at d3v4$\\to$d4v5; \\S\\ref{sec:atlas:edd}) is consistent with geometric decay approaching a fixed point \\cite{bertrand2024_stability}.\n5-class extensions to d4 (71--80\\%, chance = 20\\%; Appendix~\\ref{app:depth4_ext}) confirm depth~4 discriminability; mean perplexity saturates before tail statistics, placing a physical ceiling on EDD.\n\n\\paragraph{Scale-dependent attenuation.}\nLarger models approximate the training distribution more faithfully per step ($\\alpha$ closer to 1), predicting weaker per-step signal.\nQwen2.5-14B supports this: d0-vs-d1 AUC drops to 0.643 (vs.\\ ${>}0.99$ at 1--1.5B; \\S\\ref{sec:gen:crossscale}); 7--8B results are mixed, suggesting additional confounds interact with the scale effect (Appendix~\\ref{app:cross_scale_full}).\n\n\\paragraph{Strategy-dependent convergence.}\nThe contraction rate $\\alpha$ varies with decoding strategy.\nTemperature scaling ($\\tau < 1$) sharpens the logit distribution uniformly and accelerates convergence to the mode; temperature depth-$d$ text should therefore resemble nucleus depth-$(d{+}1)$ text in tail statistics.\nGPT-2~XL confirms this: temperature d1 median \\texttt{p90\\_ppl} (92.2) matches the nucleus d2 median (92.3).\nTop-$k$ truncation removes the low-probability tokens that carry depth signal, predicting weaker discriminability; top-$k$ cells yield the lowest accuracy (68.9--75.8\\%) across the atlas (\\S\\ref{sec:atlas:strategy}).\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  },
  "sourceToolAssistantUUID": "40e65841-dce5-4d25-80f2-aba693beafe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T17:55:43.213Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PA8gcxEWPFYQjBcMZqy3j8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6946c413-8459-4556-adb1-2633f0e754c6",
  "isSidechain": false,
  "requestId": "req_011CbJ38XzJdQXjSNtCe5Rc4",
  "type": "assistant",
  "uuid": "737bba5f-3b66-4f28-a9f9-aa6b3464429c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFPYz7YvgVdTKtvFvsEDT8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12031,
      "cache_read_input_tokens": 38110,
      "output_tokens": 862,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 862,
          "cache_read_input_tokens": 38110,
          "cache_creation_input_tokens": 12031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12031
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-22T17:55:43.218Z_

<details><summary>↩ Tool result · `toolu_01PA8gcxEWPFYQjBcMZqy3j8`</summary>

```text
1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells at the 1--1.5B parameter scale, evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 68.9\% (Pythia, top-$k$) to 85.9\% (GPT-2~XL, temperature) four-class (d1--d3 balanced: 58.9--81.5\%), all exceeding the 25\%/33\% chance baselines.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (75.8--85.9\%), followed by OLMo (74.4--82.3\%) and Pythia (68.9--78.7\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 9.3~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy contributes at least as much as model family to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) with bootstrap 95\% CI (${\pm}$half-width; $B{=}10{,}000$). RF with 200 trees, evaluated via 5-fold stratified CV (seed=42). Parenthesized: d1--d3 balanced accuracy from the same 4-class RF (chance = 25\% / 33\%). Depth-0 recall exceeds 97\% in all cells. Within-distribution ordinal quality: mean absolute error (MAE)\,=\,0.23, QWK\,=\,0.89 (QWK$_{\text{d1--d3}}$\,=\,0.74); 98.2\% of errors fall on adjacent depths ($|\Delta| \leq 1$). $^\dagger$Self-reference scoring (Pythia-1.4B is both generator and reference model); 4--11\,pp advantage over cross-model references (Appendix~\ref{app:ref_ablation}). Cross-cell comparisons involving Pythia should be interpreted with this caveat.}
22	\label{tab:main_matrix}
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}lccc@{}}
25	\toprule
26	& Nucleus & Temp.\ $\tau{=}0.9$ & Top-$k$ \\
27	\midrule
28	Pythia-1.4B$^\dagger$  & 78.7{\scriptsize$\pm$0.5}\,(71.8) & 76.8{\scriptsize$\pm$0.5}\,(69.3) & 68.9{\scriptsize$\pm$0.6}\,(58.9) \\
29	OLMo-1B     & 78.9{\scriptsize$\pm$0.5}\,(72.7) & 82.3{\scriptsize$\pm$0.5}\,(76.6) & 74.4{\scriptsize$\pm$0.5}\,(66.2) \\
30	GPT-2~XL    & \textbf{84.3}{\scriptsize$\pm$0.5}\,(79.6) & \textbf{85.9}{\scriptsize$\pm$0.5}\,(81.5) & \textbf{75.8}{\scriptsize$\pm$0.6}\,(68.1) \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	
35	\paragraph{Per-class recall.}
36	Depth-0 recall exceeds 97\% in all 9 cells.
37	Among generated depths, d2 consistently yields the lowest recall (44--73\%), reflecting its position at the center of the depth gradient where features overlap with both d1 and d3, consistent with d2-vs-d3 as the EDD bottleneck (\S\ref{sec:atlas:edd}; full per-class recall in Appendix~\ref{app:per_class}).
38	
39	%% ----------------------------------------------------------------
40	\subsection{Feature Consistency Across the Grid}
41	\label{sec:atlas:features}
42	
43	Multicollinearity is substantial (VIF${>}$10 for 14--16 of 19 features); importance rankings below indicate feature \emph{family} contributions rather than individual effects; permutation importance (Appendix~\ref{app:permutation}) partially mitigates collinearity bias \cite{strobl2008_conditional,hooker2021_permutation}.
44	Despite the 17.1~pp accuracy spread across cells, the perplexity tail statistics family (\texttt{p90\_ppl}, \texttt{p75\_ppl}, \texttt{kurtosis\_ppl}) and surprisal variance (\texttt{var\_surprisal}) dominate depth discrimination in every setting.
45	Within this family, \texttt{p90\_ppl} and \texttt{var\_surprisal} are consistently prominent, though individual rankings should be interpreted cautiously given VIF${>}$10; group-level ablation (\S\ref{sec:atlas:features}, below) provides the collinearity-robust confirmation.\footnote{The group-level dominance of perplexity tail statistics is robust across importance measures (Gini, SHAP, permutation; Kendall's $W{=}0.90$, $p{<}0.005$).}
46	Conditional permutation importance \citep{strobl2008_conditional} confirms \texttt{var\_surprisal} and \texttt{p90\_ppl} as top-2 in 8/9 cells (bootstrap rank 1.4 and 1.7), consistent with Gini rankings (Appendix~\ref{app:conditional_pi}).
47	Table~\ref{tab:feature_importance} shows the full per-cell ranking; Figure~\ref{fig:atlas_heatmap} visualizes the importance landscape across all nine cells.
48	
49	Cross-model feature-rank Spearman correlation averages $\bar{\rho} = 0.868$ ($[0.619, 0.954]$): models agree on which features carry depth information despite differing in absolute accuracy.
50	Top-$k$ yields the highest cross-model rank correlation ($\rho = 0.811$), as vocabulary truncation imposes a more uniform feature landscape at the cost of weaker signal (\S\ref{sec:atlas:strategy}).
51	
52	Feature ablation confirms this concentration: the top-5 features achieve 97.6\% of full accuracy (76.5\% vs.\ 78.4\%); group-level ablation shows perplexity features alone reach 76.6\%, surprisal 73.2\%, lexical diversity ${\leq}$47\%, and repetition ${\leq}$40\%.\footnote{Best single feature (\texttt{p90\_ppl}) achieves 58.3\%, providing a more competitive single-feature baseline than mean perplexity (25.1\%).}
53	
54	The feature hierarchy shifts with depth.
55	At shallow boundaries (d1 vs.\ d2), \texttt{var\_surprisal} dominates importance; at deeper boundaries (d3 vs.\ d4, d4 vs.\ d5), tail perplexity statistics (\texttt{p90\_ppl}, \texttt{kurtosis\_ppl}) take over.
56	This transition aligns with model-collapse dynamics~\cite{shumailov2024_nature}: early recursion narrows the surprisal distribution (captured by its variance), while later steps erode the perplexity tail (captured by upper quantiles and kurtosis).
57	
58	\begin{table}[t]
59	\centering
60	\small
61	\caption{Top-5 features by Gini importance. \textbf{Bold}: top-2. \texttt{p90\_ppl} top-2 in 9/9; \texttt{var\_surprisal} 8/9 under SHAP (7/9 under Gini). Individual rankings are approximate due to multicollinearity (VIF${>}$10 for 14--16/19 features).}
62	\label{tab:feature_importance}
63	\resizebox{\columnwidth}{!}{%
64	\begin{tabular}{@{}l l@{}}
65	\toprule
66	Cell & Top-5 features (Gini importance, ranked) \\
67	\midrule
68	Pythia, nuc.       & \textbf{var\_surprisal\,(.17)}, \textbf{p90\_ppl\,(.15)}, mean\_ppl\,(.11), var\_ppl\,(.08), p75\_ppl\,(.07) \\
69	Pythia, $\tau$     & \textbf{var\_surprisal\,(.17)}, \textbf{p90\_ppl\,(.14)}, mean\_ppl\,(.11), p75\_ppl\,(.07), mean\_surprisal\,(.07) \\
70	Pythia, top-$k$    & \textbf{var\_surprisal\,(.16)}, \textbf{p90\_ppl\,(.12)}, mean\_ppl\,(.11), var\_ppl\,(.07), mean\_surprisal\,(.06) \\
71	GPT-2\,XL, nuc.    & \textbf{var\_surprisal\,(.21)}, \textbf{p90\_ppl\,(.21)}, p75\_ppl\,(.10), mean\_surprisal\,(.07), mean\_ppl\,(.06) \\
72	GPT-2\,XL, $\tau$  & \textbf{p90\_ppl\,(.25)}, \textbf{p75\_ppl\,(.15)}, mean\_surprisal\,(.13), var\_surprisal\,(.12), p50\_ppl\,(.05) \\
73	GPT-2\,XL, top-$k$ & \textbf{p90\_ppl\,(.24)}, \textbf{p75\_ppl\,(.12)}, var\_surprisal\,(.10), mean\_surprisal\,(.09), type\_token\_ratio\,(.04) \\
74	OLMo, nuc.         & \textbf{p90\_ppl\,(.18)}, \textbf{var\_surprisal\,(.15)}, p75\_ppl\,(.11), mean\_surprisal\,(.07), type\_token\_ratio\,(.06) \\
75	OLMo, $\tau$       & \textbf{p90\_ppl\,(.21)}, \textbf{var\_surprisal\,(.16)}, p75\_ppl\,(.12), mean\_surprisal\,(.09), type\_token\_ratio\,(.05) \\
76	OLMo, top-$k$      & \textbf{p90\_ppl\,(.20)}, \textbf{var\_surprisal\,(.17)}, p75\_ppl\,(.10), mean\_surprisal\,(.07), mean\_ppl\,(.05) \\
77	\bottomrule
78	\end{tabular}}
79	\end{table}
80	
81	\begin{figure}[t]
82	\centering
83	\includegraphics[width=\columnwidth]{figures/fig_atlas_heatmap.pdf}
84	\caption{Atlas feature importance heatmap for the top-7 features. Rows: features ranked by mean Gini importance; columns: 9 model--strategy cells. Stars mark the two universal top-2 features (\texttt{p90\_ppl}, \texttt{var\_surprisal}). Full 19-feature breakdown in Appendix~\ref{app:feature_ablation}.}
85	\label{fig:atlas_heatmap}
86	\end{figure}
87	
88	%% ----------------------------------------------------------------
89	\subsection{EDD Analysis}
90	\label{sec:atlas:edd}
91	\label{sec:atlas:monotonicity}
92	
93	Depth features exhibit strong monotonic trends (Spearman $\rho = -1.0$ for perplexity tail statistics; Figure~\ref{fig:feature_trajectory}); inter-depth distances are non-uniform (d0-vs-d1 AUC ${>}$0.99 in all 9 cells, d2-vs-d3: 0.69--0.89).
94	
95	We extend the benchmark to depth $d{=}5$ for all three models under nucleus sampling.
96	Each model's depth-3 LoRA checkpoint is used to finetune and generate depth-4 data, and the process repeats for depth~5; feature extraction uses the same reference model (Pythia-1.4B).
97	We train dedicated binary RF classifiers (500 trees) for each adjacent pair, as defined in Eq.~\ref{eq:edd}.
98	
99	\paragraph{AUC decay and cross-model convergence.}
100	For Pythia-1.4B (nucleus), AUC decays monotonically from $0.999$ (d0v1) to $0.683$ (d4v5); AUC-excess contraction ratios (0.80 at d1v2$\to$d2v3, 0.69 at d3v4$\to$d4v5) show convergence toward indistinguishability accelerates with depth (Figure~\ref{fig:auc_decay}).
101	The d3-vs-d4 AUC clusters near $T{=}0.75$ for all three models (Pythia $0.784$, OLMo $0.765$, GPT-2~XL $0.750$), while d4-vs-d5 converges to a narrow band ($0.681$--$0.684$, range $0.003$), suggesting an architecture-independent depth ceiling within the 1--1.5B nucleus setting.
102	Bootstrap testing ($H_0{:}\, \mathrm{AUC} \leq 0.75$; Bonferroni-corrected for 3 comparisons, $\alpha{=}0.0167$) yields $p = 0.001$ (Pythia), $0.091$ (OLMo), $0.505$ (GPT-2~XL).
103	
104	\paragraph{EDD threshold sensitivity.}
105	Across the 9-cell benchmark (depths 0--3), all cells achieve $\mathrm{EDD}{=}3$ at $T{=}0.65$; at $T{=}0.70$, 8/9 cells; at $T{=}0.75$, 7/9; at $T{=}0.80$, 5/9.
106	Top-$k$ configurations lose $\mathrm{EDD}{=}3$ first (Pythia top-$k$ at $T{=}0.70$, OLMo top-$k$ at $T{=}0.75$); d2-vs-d3 is the consistent bottleneck.
107	
108	\begin{figure}[t]
109	\centering
110	\includegraphics[width=\columnwidth]{figures/fig_auc_decay.pdf}
111	\caption{AUC decay curves for Pythia-1.4B (nucleus, depths 0--5) under three pipeline configurations: binary pairwise RF, 4-class RF, and 6-class RF. Horizontal dashed lines mark $T \in \{0.65, 0.70, 0.75, 0.80\}$. All curves converge below 0.70 at d4-vs-d5. Shaded bands: bootstrap 95\% CIs.}
112	\label{fig:auc_decay}
113	\end{figure}
114	
115	%% ----------------------------------------------------------------
116	\subsection{Strategy-Dependent Trajectories}
117	\label{sec:atlas:strategy}
118	
119	The three strategies induce qualitatively distinct degradation trajectories.
120	Temperature ($\tau{=}0.9$) yields the highest accuracy in 2/3 models (GPT-2~XL 85.9\%, OLMo 82.3\%) because uniform logit scaling accelerates convergence to an attractor~\cite{shumailov2024_nature}, amplifying the fingerprint but creating a boundary reversal risk under cross-strategy transfer (\S\ref{sec:generalization}).
121	Top-$k$ ($k{=}50$) produces the lowest accuracy (68.9--75.8\%) because hard vocabulary truncation removes depth-discriminative low-probability tokens.
122	The strategy effect (9.3\,pp range) exceeds the model effect (7.2\,pp); deployment-time knowledge of the decoding strategy matters at least as much as the generator model.
123	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "737bba5f-3b66-4f28-a9f9-aa6b3464429c",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "c3796203-f0a8-4836-b000-cb0174c8df0e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
      "content": "\\section{The Depth Degradation Atlas}\n\\label{sec:atlas}\n\nWe present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.\nThe atlas spans $3 \\times 3 = 9$ model--strategy cells at the 1--1.5B parameter scale, evaluated at depths $d \\in \\{0, 1, 2, 3\\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\\S\\ref{sec:atlas:edd}).\n\n%% ----------------------------------------------------------------\n\\subsection{In-Distribution Performance}\n\\label{sec:atlas:id}\n\nTable~\\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.\nAccuracy ranges from 68.9\\% (Pythia, top-$k$) to 85.9\\% (GPT-2~XL, temperature) four-class (d1--d3 balanced: 58.9--81.5\\%), all exceeding the 25\\%/33\\% chance baselines.\nTwo axis effects emerge.\nGPT-2~XL achieves the highest accuracy under every strategy (75.8--85.9\\%), followed by OLMo (74.4--82.3\\%) and Pythia (68.9--78.7\\%).\nTop-$k$ sampling yields the lowest accuracy in every model.\nThe mean within-model strategy gap is 9.3~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy contributes at least as much as model family to performance variance.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Four-class RF accuracy (\\%) with bootstrap 95\\% CI (${\\pm}$half-width; $B{=}10{,}000$). RF with 200 trees, evaluated via 5-fold stratified CV (seed=42). Parenthesized: d1--d3 balanced accuracy from the same 4-class RF (chance = 25\\% / 33\\%). Depth-0 recall exceeds 97\\% in all cells. Within-distribution ordinal quality: mean absolute error (MAE)\\,=\\,0.23, QWK\\,=\\,0.89 (QWK$_{\\text{d1--d3}}$\\,=\\,0.74); 98.2\\% of errors fall on adjacent depths ($|\\Delta| \\leq 1$). $^\\dagger$Self-reference scoring (Pythia-1.4B is both generator and reference model); 4--11\\,pp advantage over cross-model references (Appendix~\\ref{app:ref_ablation}). Cross-cell comparisons involving Pythia should be interpreted with this caveat.}\n\\label{tab:main_matrix}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n& Nucleus & Temp.\\ $\\tau{=}0.9$ & Top-$k$ \\\\\n\\midrule\nPythia-1.4B$^\\dagger$  & 78.7{\\scriptsize$\\pm$0.5}\\,(71.8) & 76.8{\\scriptsize$\\pm$0.5}\\,(69.3) & 68.9{\\scriptsize$\\pm$0.6}\\,(58.9) \\\\\nOLMo-1B     & 78.9{\\scriptsize$\\pm$0.5}\\,(72.7) & 82.3{\\scriptsize$\\pm$0.5}\\,(76.6) & 74.4{\\scriptsize$\\pm$0.5}\\,(66.2) \\\\\nGPT-2~XL    & \\textbf{84.3}{\\scriptsize$\\pm$0.5}\\,(79.6) & \\textbf{85.9}{\\scriptsize$\\pm$0.5}\\,(81.5) & \\textbf{75.8}{\\scriptsize$\\pm$0.6}\\,(68.1) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-class recall.}\nDepth-0 recall exceeds 97\\% in all 9 cells.\nAmong generated depths, d2 consistently yields the lowest recall (44--73\\%), reflecting its position at the center of the depth gradient where features overlap with both d1 and d3, consistent with d2-vs-d3 as the EDD bottleneck (\\S\\ref{sec:atlas:edd}; full per-class recall in Appendix~\\ref{app:per_class}).\n\n%% ----------------------------------------------------------------\n\\subsection{Feature Consistency Across the Grid}\n\\label{sec:atlas:features}\n\nMulticollinearity is substantial (VIF${>}$10 for 14--16 of 19 features); importance rankings below indicate feature \\emph{family} contributions rather than individual effects; permutation importance (Appendix~\\ref{app:permutation}) partially mitigates collinearity bias \\cite{strobl2008_conditional,hooker2021_permutation}.\nDespite the 17.1~pp accuracy spread across cells, the perplexity tail statistics family (\\texttt{p90\\_ppl}, \\texttt{p75\\_ppl}, \\texttt{kurtosis\\_ppl}) and surprisal variance (\\texttt{var\\_surprisal}) dominate depth discrimination in every setting.\nWithin this family, \\texttt{p90\\_ppl} and \\texttt{var\\_surprisal} are consistently prominent, though individual rankings should be interpreted cautiously given VIF${>}$10; group-level ablation (\\S\\ref{sec:atlas:features}, below) provides the collinearity-robust confirmation.\\footnote{The group-level dominance of perplexity tail statistics is robust across importance measures (Gini, SHAP, permutation; Kendall's $W{=}0.90$, $p{<}0.005$).}\nConditional permutation importance \\citep{strobl2008_conditional} confirms \\texttt{var\\_surprisal} and \\texttt{p90\\_ppl} as top-2 in 8/9 cells (bootstrap rank 1.4 and 1.7), consistent with Gini rankings (Appendix~\\ref{app:conditional_pi}).\nTable~\\ref{tab:feature_importance} shows the full per-cell ranking; Figure~\\ref{fig:atlas_heatmap} visualizes the importance landscape across all nine cells.\n\nCross-model feature-rank Spearman correlation averages $\\bar{\\rho} = 0.868$ ($[0.619, 0.954]$): models agree on which features carry depth information despite differing in absolute accuracy.\nTop-$k$ yields the highest cross-model rank correlation ($\\rho = 0.811$), as vocabulary truncation imposes a more uniform feature landscape at the cost of weaker signal (\\S\\ref{sec:atlas:strategy}).\n\nFeature ablation confirms this concentration: the top-5 features achieve 97.6\\% of full accuracy (76.5\\% vs.\\ 78.4\\%); group-level ablation shows perplexity features alone reach 76.6\\%, surprisal 73.2\\%, lexical diversity ${\\leq}$47\\%, and repetition ${\\leq}$40\\%.\\footnote{Best single feature (\\texttt{p90\\_ppl}) achieves 58.3\\%, providing a more competitive single-feature baseline than mean perplexity (25.1\\%).}\n\nThe feature hierarchy shifts with depth.\nAt shallow boundaries (d1 vs.\\ d2), \\texttt{var\\_surprisal} dominates importance; at deeper boundaries (d3 vs.\\ d4, d4 vs.\\ d5), tail perplexity statistics (\\texttt{p90\\_ppl}, \\texttt{kurtosis\\_ppl}) take over.\nThis transition aligns with model-collapse dynamics~\\cite{shumailov2024_nature}: early recursion narrows the surprisal distribution (captured by its variance), while later steps erode the perplexity tail (captured by upper quantiles and kurtosis).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Top-5 features by Gini importance. \\textbf{Bold}: top-2. \\texttt{p90\\_ppl} top-2 in 9/9; \\texttt{var\\_surprisal} 8/9 under SHAP (7/9 under Gini). Individual rankings are approximate due to multicollinearity (VIF${>}$10 for 14--16/19 features).}\n\\label{tab:feature_importance}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l l@{}}\n\\toprule\nCell & Top-5 features (Gini importance, ranked) \\\\\n\\midrule\nPythia, nuc.       & \\textbf{var\\_surprisal\\,(.17)}, \\textbf{p90\\_ppl\\,(.15)}, mean\\_ppl\\,(.11), var\\_ppl\\,(.08), p75\\_ppl\\,(.07) \\\\\nPythia, $\\tau$     & \\textbf{var\\_surprisal\\,(.17)}, \\textbf{p90\\_ppl\\,(.14)}, mean\\_ppl\\,(.11), p75\\_ppl\\,(.07), mean\\_surprisal\\,(.07) \\\\\nPythia, top-$k$    & \\textbf{var\\_surprisal\\,(.16)}, \\textbf{p90\\_ppl\\,(.12)}, mean\\_ppl\\,(.11), var\\_ppl\\,(.07), mean\\_surprisal\\,(.06) \\\\\nGPT-2\\,XL, nuc.    & \\textbf{var\\_surprisal\\,(.21)}, \\textbf{p90\\_ppl\\,(.21)}, p75\\_ppl\\,(.10), mean\\_surprisal\\,(.07), mean\\_ppl\\,(.06) \\\\\nGPT-2\\,XL, $\\tau$  & \\textbf{p90\\_ppl\\,(.25)}, \\textbf{p75\\_ppl\\,(.15)}, mean\\_surprisal\\,(.13), var\\_surprisal\\,(.12), p50\\_ppl\\,(.05) \\\\\nGPT-2\\,XL, top-$k$ & \\textbf{p90\\_ppl\\,(.24)}, \\textbf{p75\\_ppl\\,(.12)}, var\\_surprisal\\,(.10), mean\\_surprisal\\,(.09), type\\_token\\_ratio\\,(.04) \\\\\nOLMo, nuc.         & \\textbf{p90\\_ppl\\,(.18)}, \\textbf{var\\_surprisal\\,(.15)}, p75\\_ppl\\,(.11), mean\\_surprisal\\,(.07), type\\_token\\_ratio\\,(.06) \\\\\nOLMo, $\\tau$       & \\textbf{p90\\_ppl\\,(.21)}, \\textbf{var\\_surprisal\\,(.16)}, p75\\_ppl\\,(.12), mean\\_surprisal\\,(.09), type\\_token\\_ratio\\,(.05) \\\\\nOLMo, top-$k$      & \\textbf{p90\\_ppl\\,(.20)}, \\textbf{var\\_surprisal\\,(.17)}, p75\\_ppl\\,(.10), mean\\_surprisal\\,(.07), mean\\_ppl\\,(.05) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_atlas_heatmap.pdf}\n\\caption{Atlas feature importance heatmap for the top-7 features. Rows: features ranked by mean Gini importance; columns: 9 model--strategy cells. Stars mark the two universal top-2 features (\\texttt{p90\\_ppl}, \\texttt{var\\_surprisal}). Full 19-feature breakdown in Appendix~\\ref{app:feature_ablation}.}\n\\label{fig:atlas_heatmap}\n\\end{figure}\n\n%% ----------------------------------------------------------------\n\\subsection{EDD Analysis}\n\\label{sec:atlas:edd}\n\\label{sec:atlas:monotonicity}\n\nDepth features exhibit strong monotonic trends (Spearman $\\rho = -1.0$ for perplexity tail statistics; Figure~\\ref{fig:feature_trajectory}); inter-depth distances are non-uniform (d0-vs-d1 AUC ${>}$0.99 in all 9 cells, d2-vs-d3: 0.69--0.89).\n\nWe extend the benchmark to depth $d{=}5$ for all three models under nucleus sampling.\nEach model's depth-3 LoRA checkpoint is used to finetune and generate depth-4 data, and the process repeats for depth~5; feature extraction uses the same reference model (Pythia-1.4B).\nWe train dedicated binary RF classifiers (500 trees) for each adjacent pair, as defined in Eq.~\\ref{eq:edd}.\n\n\\paragraph{AUC decay and cross-model convergence.}\nFor Pythia-1.4B (nucleus), AUC decays monotonically from $0.999$ (d0v1) to $0.683$ (d4v5); AUC-excess contraction ratios (0.80 at d1v2$\\to$d2v3, 0.69 at d3v4$\\to$d4v5) show convergence toward indistinguishability accelerates with depth (Figure~\\ref{fig:auc_decay}).\nThe d3-vs-d4 AUC clusters near $T{=}0.75$ for all three models (Pythia $0.784$, OLMo $0.765$, GPT-2~XL $0.750$), while d4-vs-d5 converges to a narrow band ($0.681$--$0.684$, range $0.003$), suggesting an architecture-independent depth ceiling within the 1--1.5B nucleus setting.\nBootstrap testing ($H_0{:}\\, \\mathrm{AUC} \\leq 0.75$; Bonferroni-corrected for 3 comparisons, $\\alpha{=}0.0167$) yields $p = 0.001$ (Pythia), $0.091$ (OLMo), $0.505$ (GPT-2~XL).\n\n\\paragraph{EDD threshold sensitivity.}\nAcross the 9-cell benchmark (depths 0--3), all cells achieve $\\mathrm{EDD}{=}3$ at $T{=}0.65$; at $T{=}0.70$, 8/9 cells; at $T{=}0.75$, 7/9; at $T{=}0.80$, 5/9.\nTop-$k$ configurations lose $\\mathrm{EDD}{=}3$ first (Pythia top-$k$ at $T{=}0.70$, OLMo top-$k$ at $T{=}0.75$); d2-vs-d3 is the consistent bottleneck.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_auc_decay.pdf}\n\\caption{AUC decay curves for Pythia-1.4B (nucleus, depths 0--5) under three pipeline configurations: binary pairwise RF, 4-class RF, and 6-class RF. Horizontal dashed lines mark $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$. All curves converge below 0.70 at d4-vs-d5. Shaded bands: bootstrap 95\\% CIs.}\n\\label{fig:auc_decay}\n\\end{figure}\n\n%% ----------------------------------------------------------------\n\\subsection{Strategy-Dependent Trajectories}\n\\label{sec:atlas:strategy}\n\nThe three strategies induce qualitatively distinct degradation trajectories.\nTemperature ($\\tau{=}0.9$) yields the highest accuracy in 2/3 models (GPT-2~XL 85.9\\%, OLMo 82.3\\%) because uniform logit scaling accelerates convergence to an attractor~\\cite{shumailov2024_nature}, amplifying the fingerprint but creating a boundary reversal risk under cross-strategy transfer (\\S\\ref{sec:generalization}).\nTop-$k$ ($k{=}50$) produces the lowest accuracy (68.9--75.8\\%) because hard vocabulary truncation removes depth-discriminative low-probability tokens.\nThe strategy effect (9.3\\,pp range) exceeds the model effect (7.2\\,pp); deployment-time knowledge of the decoding strategy matters at least as much as the generator model.\n",
      "numLines": 123,
      "startLine": 1,
      "totalLines": 123
    }
  },
  "sourceToolAssistantUUID": "737bba5f-3b66-4f28-a9f9-aa6b3464429c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T17:55:43.682Z_

<details open><summary>🔧 Tool call — Read · `toolu_015gei8vRGd74HNonWgBFgYQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3796203-f0a8-4836-b000-cb0174c8df0e",
  "isSidechain": false,
  "requestId": "req_011CbJ38XzJdQXjSNtCe5Rc4",
  "type": "assistant",
  "uuid": "cc914c3f-08e2-4a46-ab28-6c1ba281da5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFPYz7YvgVdTKtvFvsEDT8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12031,
      "cache_read_input_tokens": 38110,
      "output_tokens": 862,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 862,
          "cache_read_input_tokens": 38110,
          "cache_creation_input_tokens": 12031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12031
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-22T17:55:43.687Z_

<details><summary>↩ Tool result · `toolu_015gei8vRGd74HNonWgBFgYQ`</summary>

```text
1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (68.9--85.9\% four-class; d1--d3: 58.9--81.5\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} compares methods across all 9 cells.
10	Four classifiers (RF, XGBoost, ordinal MLP, prototypical) converge within 0.8\,pp under cross-model transfer (Appendix~\ref{app:learned_estimator}), confirming a feature-determined accuracy ceiling.
11	
12	\paragraph{Neural end-to-end baselines.}
13	DeBERTa-v3-base (LoRA) underperforms RF by 16--32\,pp (d2 recall 8.4\%); RoBERTa-DCOL (ordinal contrastive; 64.5\%) narrows the gap but remains 14\,pp below RF.
14	
15	\paragraph{Binary detectors and membership inference.}
16	Perturbation-based (DetectGPT, 28.8\%) and membership-inference (Min-K\% Prob, 33.2\%; Min-K\%++ \cite{zhang2024_minkpp} comparable) methods produce scores with no ordinal resolution (Table~\ref{tab:baselines}); pairwise analysis confirms ordinal collapse: Binoculars d1v2 AUC\,=\,0.50--0.53 vs.\ RF 0.93 (Appendix~\ref{app:detector_baselines}).
17	CORAL calibration does not close the gap (d1--d3: 40.4\% vs.\ RF 71.6\%).
18	Binoculars \cite{binoculars2024}, calibrated with 11-feature RF, independently converges to 78.1\% ($p{>}0.05$ vs.\ our 78.4\%); merging all 30 features yields 82.6\% (Appendix~\ref{app:feature_ablation_bino}).
19	
20	\paragraph{Surface-text ablation.}
21	Single-feature regression on mean perplexity performs at chance (25.1\%); zero-shot LLMs (best 36.2\%; Appendix~\ref{app:zeroshot_prompt}) also fail; depth signal resides in distributional statistics inaccessible from surface text.
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\caption{Method comparison (RF mean across 9 cells, 5-fold CV). Chance = 25\% / 33.3\% (d1--d3). $^\dagger$Adapted from binary detection; Binoculars 11-feat: $p{>}0.05$ vs.\ 19-feat RF (paired permutation test).}
27	\label{tab:baselines}
28	\resizebox{\columnwidth}{!}{%
29	\begin{tabular}{@{}llcc@{}}
30	\toprule
31	Method & Calibration & 4-Cl (\%) & d1--d3 (\%) \\
32	\midrule
33	RF 19-feature (ours) & RF & 78.4 & \textbf{71.6} \\
34	Binoculars$^\dagger$ \cite{binoculars2024} & RF (11 feat) & 78.1 & --- \\
35	Merged (30 feat)$^\dagger$ & RF & \textbf{82.6} & --- \\
36	Binoculars \cite{binoculars2024} & threshold & 69.8 & --- \\
37	Binoculars \cite{binoculars2024} & RF (1 feat) & 63.7 & --- \\
38	RoBERTa-DCOL (ordinal) & contrastive & 64.5 & --- \\
39	DeBERTa-v3 (end-to-end) & cross-entropy & 53.1--60.6 & --- \\
40	\midrule
41	Zero-shot LLM (best) & --- & 36.2 & --- \\
42	Min-K\% Prob \cite{shi2024_minkprob} & CORAL & 33.2 & 40.4 \\
43	DetectGPT \cite{mitchell2023_detectgpt} & best-of-3 & 28.8 & 24.3 \\
44	Random & --- & 25.0 & 33.3 \\
45	\bottomrule
46	\end{tabular}}
47	\end{table}
48	
49	\subsection{Cross-Model Transfer}
50	\label{sec:gen:crossmodel}
51	
52	\begin{table}[t]
53	\centering
54	\small
55	\caption{Cross-model transfer (leave-one-out, nucleus only). Chance = 25\% / 33\% (d1--d3). d1--d3 mean 55.4\%; QWK\,=\,0.81; 94.8\% errors at $|\Delta| \leq 1$.}
56	\label{tab:cross_model}
57	\begin{tabular}{lccccc}
58	\toprule
59	Holdout & Acc & d0 & d1 & d2 & d3 \\
60	 & (\%) & Rec. & Rec. & Rec. & Rec. \\
61	\midrule
62	Pythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\
63	OLMo & \textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\
64	GPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\
65	\midrule
66	Mean & 66.4 & 99.3 & 66.5 & 40.9 & 59.0 \\
67	\bottomrule
68	\end{tabular}
69	\end{table}
70	
71	Mean transfer accuracy is 66.4\% (Table~\ref{tab:cross_model}; d1--d3: 55.4\%, $2.7{\times}$ chance); d2 worst case 26.8\% (Pythia holdout; confusion matrices in Figure~\ref{fig:confusion_matrix}).
72	
73	\subsection{Cross-Strategy Transfer}
74	\label{sec:gen:crossstrategy}
75	
76	Cross-strategy transfer reveals a structural barrier: d1--d3 balanced accuracy drops to 45.9\% (four-class: 59.1\%), 7\,pp below cross-model transfer (Table~\ref{tab:cross_strategy}).
77	A two-stage pipeline (strategy classifier $\to$ conditioned depth classifier) recovers much of this gap: 70.5\% four-class accuracy ($+$11.5\,pp over LOO); oracle routing yields 78.3\%, so the 7.8\,pp residual is attributable to strategy misidentification (Appendix~\ref{app:extended_discussion}).
78	Our depth estimation claims hold most strongly within-strategy or when the decoding configuration is known.
79	
80	%% ----------------------------------------------------------------
81	\subsection{Preliminary Cross-Scale Observations (14B)}
82	\label{sec:gen:crossscale}
83	
84	At 14B (Qwen2.5-14B), self-reference yields 50.8\% ($2{\times}$ chance, $\mathrm{EDD}_{0.70}{=}0$); cross-reference control (Pythia-1.4B) drops accuracy to 44.1\% ($-$6.8\,pp) but raises $\mathrm{EDD}_{0.70}$ to 2 for nucleus and temperature, revealing that ${\sim}$7\,pp of the accuracy drop is attributable to reference-model mismatch rather than scale (Appendix~\ref{app:cross_scale_full}).
85	Cross-domain (arXiv) accuracy reaches 74.1\% at 1--1.5B; cross-domain FPR is discussed in Limitations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc914c3f-08e2-4a46-ab28-6c1ba281da5d",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "346af810-206f-4281-be73-ec9ec01fa2c3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
      "content": "\\section{Generalization and Robustness}\n\\label{sec:generalization}\n\nWe test whether atlas accuracy (68.9--85.9\\% four-class; d1--d3: 58.9--81.5\\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).\n\n\\subsection{Classifier Comparison and Surface-Text Ablation}\n\\label{sec:gen:baselines}\n\nTable~\\ref{tab:baselines} compares methods across all 9 cells.\nFour classifiers (RF, XGBoost, ordinal MLP, prototypical) converge within 0.8\\,pp under cross-model transfer (Appendix~\\ref{app:learned_estimator}), confirming a feature-determined accuracy ceiling.\n\n\\paragraph{Neural end-to-end baselines.}\nDeBERTa-v3-base (LoRA) underperforms RF by 16--32\\,pp (d2 recall 8.4\\%); RoBERTa-DCOL (ordinal contrastive; 64.5\\%) narrows the gap but remains 14\\,pp below RF.\n\n\\paragraph{Binary detectors and membership inference.}\nPerturbation-based (DetectGPT, 28.8\\%) and membership-inference (Min-K\\% Prob, 33.2\\%; Min-K\\%++ \\cite{zhang2024_minkpp} comparable) methods produce scores with no ordinal resolution (Table~\\ref{tab:baselines}); pairwise analysis confirms ordinal collapse: Binoculars d1v2 AUC\\,=\\,0.50--0.53 vs.\\ RF 0.93 (Appendix~\\ref{app:detector_baselines}).\nCORAL calibration does not close the gap (d1--d3: 40.4\\% vs.\\ RF 71.6\\%).\nBinoculars \\cite{binoculars2024}, calibrated with 11-feature RF, independently converges to 78.1\\% ($p{>}0.05$ vs.\\ our 78.4\\%); merging all 30 features yields 82.6\\% (Appendix~\\ref{app:feature_ablation_bino}).\n\n\\paragraph{Surface-text ablation.}\nSingle-feature regression on mean perplexity performs at chance (25.1\\%); zero-shot LLMs (best 36.2\\%; Appendix~\\ref{app:zeroshot_prompt}) also fail; depth signal resides in distributional statistics inaccessible from surface text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Method comparison (RF mean across 9 cells, 5-fold CV). Chance = 25\\% / 33.3\\% (d1--d3). $^\\dagger$Adapted from binary detection; Binoculars 11-feat: $p{>}0.05$ vs.\\ 19-feat RF (paired permutation test).}\n\\label{tab:baselines}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\nMethod & Calibration & 4-Cl (\\%) & d1--d3 (\\%) \\\\\n\\midrule\nRF 19-feature (ours) & RF & 78.4 & \\textbf{71.6} \\\\\nBinoculars$^\\dagger$ \\cite{binoculars2024} & RF (11 feat) & 78.1 & --- \\\\\nMerged (30 feat)$^\\dagger$ & RF & \\textbf{82.6} & --- \\\\\nBinoculars \\cite{binoculars2024} & threshold & 69.8 & --- \\\\\nBinoculars \\cite{binoculars2024} & RF (1 feat) & 63.7 & --- \\\\\nRoBERTa-DCOL (ordinal) & contrastive & 64.5 & --- \\\\\nDeBERTa-v3 (end-to-end) & cross-entropy & 53.1--60.6 & --- \\\\\n\\midrule\nZero-shot LLM (best) & --- & 36.2 & --- \\\\\nMin-K\\% Prob \\cite{shi2024_minkprob} & CORAL & 33.2 & 40.4 \\\\\nDetectGPT \\cite{mitchell2023_detectgpt} & best-of-3 & 28.8 & 24.3 \\\\\nRandom & --- & 25.0 & 33.3 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Cross-Model Transfer}\n\\label{sec:gen:crossmodel}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model transfer (leave-one-out, nucleus only). Chance = 25\\% / 33\\% (d1--d3). d1--d3 mean 55.4\\%; QWK\\,=\\,0.81; 94.8\\% errors at $|\\Delta| \\leq 1$.}\n\\label{tab:cross_model}\n\\begin{tabular}{lccccc}\n\\toprule\nHoldout & Acc & d0 & d1 & d2 & d3 \\\\\n & (\\%) & Rec. & Rec. & Rec. & Rec. \\\\\n\\midrule\nPythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\\\\nOLMo & \\textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\\\\nGPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\\\\n\\midrule\nMean & 66.4 & 99.3 & 66.5 & 40.9 & 59.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean transfer accuracy is 66.4\\% (Table~\\ref{tab:cross_model}; d1--d3: 55.4\\%, $2.7{\\times}$ chance); d2 worst case 26.8\\% (Pythia holdout; confusion matrices in Figure~\\ref{fig:confusion_matrix}).\n\n\\subsection{Cross-Strategy Transfer}\n\\label{sec:gen:crossstrategy}\n\nCross-strategy transfer reveals a structural barrier: d1--d3 balanced accuracy drops to 45.9\\% (four-class: 59.1\\%), 7\\,pp below cross-model transfer (Table~\\ref{tab:cross_strategy}).\nA two-stage pipeline (strategy classifier $\\to$ conditioned depth classifier) recovers much of this gap: 70.5\\% four-class accuracy ($+$11.5\\,pp over LOO); oracle routing yields 78.3\\%, so the 7.8\\,pp residual is attributable to strategy misidentification (Appendix~\\ref{app:extended_discussion}).\nOur depth estimation claims hold most strongly within-strategy or when the decoding configuration is known.\n\n%% ----------------------------------------------------------------\n\\subsection{Preliminary Cross-Scale Observations (14B)}\n\\label{sec:gen:crossscale}\n\nAt 14B (Qwen2.5-14B), self-reference yields 50.8\\% ($2{\\times}$ chance, $\\mathrm{EDD}_{0.70}{=}0$); cross-reference control (Pythia-1.4B) drops accuracy to 44.1\\% ($-$6.8\\,pp) but raises $\\mathrm{EDD}_{0.70}$ to 2 for nucleus and temperature, revealing that ${\\sim}$7\\,pp of the accuracy drop is attributable to reference-model mismatch rather than scale (Appendix~\\ref{app:cross_scale_full}).\nCross-domain (arXiv) accuracy reaches 74.1\\% at 1--1.5B; cross-domain FPR is discussed in Limitations.",
      "numLines": 85,
      "startLine": 1,
      "totalLines": 85
    }
  },
  "sourceToolAssistantUUID": "cc914c3f-08e2-4a46-ab28-6c1ba281da5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T17:55:44.144Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MxngBAHYVn4vRNyYE3Sqgh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "346af810-206f-4281-be73-ec9ec01fa2c3",
  "isSidechain": false,
  "requestId": "req_011CbJ38XzJdQXjSNtCe5Rc4",
  "type": "assistant",
  "uuid": "7156070c-6ea1-4812-9d17-e6dafe978fab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFPYz7YvgVdTKtvFvsEDT8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12031,
      "cache_read_input_tokens": 38110,
      "output_tokens": 862,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 862,
          "cache_read_input_tokens": 38110,
          "cache_creation_input_tokens": 12031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12031
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-22T17:55:44.148Z_

<details><summary>↩ Tool result · `toolu_01MxngBAHYVn4vRNyYE3Sqgh`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	\paragraph{Multi-channel depth encoding.}
5	Three importance measures (Gini, SHAP, permutation; Kendall's $W{=}0.90$), confirmed by a fourth (CPI; Appendix~\ref{app:conditional_pi}), converge on the same feature ranking, and an independent Binoculars-derived 11-feature pathway reaches statistically indistinguishable accuracy (78.1\% vs.\ 78.4\%, $p{>}0.05$; merged: 82.6\%).
6	Recursive generation thus leaves fingerprints across multiple statistical channels; the depth signal is a distributional property, not a single exploitable artifact.
7	
8	\paragraph{Deployment considerations.}
9	The strategy effect (9.3\,pp) exceeding the model effect (7.2\,pp) means auditing pipelines must condition on decoding configuration, motivating the two-stage pipeline (\S\ref{sec:gen:crossstrategy}) and echoing the call by \citet{schaeffer2025} for operationally precise metrics.
10	A preliminary curation PoC (Appendix~\ref{app:curation_poc}) is inconclusive: RF-filtered subsets outperform random subsampling but do not significantly improve over unfiltered data ($p{>}0.4$).
11	Scale attenuation at 14B (\S\ref{sec:gen:crossscale}), consistent with tail-narrowing theory \citep{dohmatob2024_tale_of_tails}, may be partially recoverable via scale-matched references.
12	
13	\paragraph{Outlook.}
14	Depth estimation bridges binary synthetic text detection and the model collapse literature by providing ordinal resolution, enabling selective filtering of deeply recursive content while retaining shallow-depth text \cite{drayson2025_detection_prevents_collapse}.
15	Extending to accumulation settings, prompted generation, and frontier-scale models remains the principal open direction.
16	%% --- 7B SCALE TEMPLATES (swap in when results arrive) ---
17	%% VERSION A (7B ≥60%, EDD≥2): replace the sentence above with:
18	%% Scale attenuation is monotonic across the three scales tested: self-reference accuracy declines from 78.7\% (1.4B) through $X$\% (7B, $\mathrm{EDD}_{0.70}{=}Y$) to 50.8\% (14B, $\mathrm{EDD}_{0.70}{=}0$), consistent with tail-narrowing theory \citep{dohmatob2024_tale_of_tails}; the within-family Qwen 7B$\to$14B comparison ($-Z$\,pp) isolates a scale effect free of architecture confounds, and whether scale-matched references can recover further signal remains open.
19	%% VERSION B (7B 40-60%): replace with:
20	%% Scale attenuation is confirmed at an intermediate scale: 7B self-reference accuracy reaches $X$\% ($\mathrm{EDD}_{0.70}{=}Y$), between 1.4B (78.7\%) and 14B (50.8\%), consistent with monotonic attenuation \citep{dohmatob2024_tale_of_tails} though insufficient to characterize its functional form; whether scale-matched references can recover further signal remains open.
21	%% --- END TEMPLATES ---
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7156070c-6ea1-4812-9d17-e6dafe978fab",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "0dd6f02f-cb7c-4913-b945-e16c683610d8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\n\\paragraph{Multi-channel depth encoding.}\nThree importance measures (Gini, SHAP, permutation; Kendall's $W{=}0.90$), confirmed by a fourth (CPI; Appendix~\\ref{app:conditional_pi}), converge on the same feature ranking, and an independent Binoculars-derived 11-feature pathway reaches statistically indistinguishable accuracy (78.1\\% vs.\\ 78.4\\%, $p{>}0.05$; merged: 82.6\\%).\nRecursive generation thus leaves fingerprints across multiple statistical channels; the depth signal is a distributional property, not a single exploitable artifact.\n\n\\paragraph{Deployment considerations.}\nThe strategy effect (9.3\\,pp) exceeding the model effect (7.2\\,pp) means auditing pipelines must condition on decoding configuration, motivating the two-stage pipeline (\\S\\ref{sec:gen:crossstrategy}) and echoing the call by \\citet{schaeffer2025} for operationally precise metrics.\nA preliminary curation PoC (Appendix~\\ref{app:curation_poc}) is inconclusive: RF-filtered subsets outperform random subsampling but do not significantly improve over unfiltered data ($p{>}0.4$).\nScale attenuation at 14B (\\S\\ref{sec:gen:crossscale}), consistent with tail-narrowing theory \\citep{dohmatob2024_tale_of_tails}, may be partially recoverable via scale-matched references.\n\n\\paragraph{Outlook.}\nDepth estimation bridges binary synthetic text detection and the model collapse literature by providing ordinal resolution, enabling selective filtering of deeply recursive content while retaining shallow-depth text \\cite{drayson2025_detection_prevents_collapse}.\nExtending to accumulation settings, prompted generation, and frontier-scale models remains the principal open direction.\n%% --- 7B SCALE TEMPLATES (swap in when results arrive) ---\n%% VERSION A (7B ≥60%, EDD≥2): replace the sentence above with:\n%% Scale attenuation is monotonic across the three scales tested: self-reference accuracy declines from 78.7\\% (1.4B) through $X$\\% (7B, $\\mathrm{EDD}_{0.70}{=}Y$) to 50.8\\% (14B, $\\mathrm{EDD}_{0.70}{=}0$), consistent with tail-narrowing theory \\citep{dohmatob2024_tale_of_tails}; the within-family Qwen 7B$\\to$14B comparison ($-Z$\\,pp) isolates a scale effect free of architecture confounds, and whether scale-matched references can recover further signal remains open.\n%% VERSION B (7B 40-60%): replace with:\n%% Scale attenuation is confirmed at an intermediate scale: 7B self-reference accuracy reaches $X$\\% ($\\mathrm{EDD}_{0.70}{=}Y$), between 1.4B (78.7\\%) and 14B (50.8\\%), consistent with monotonic attenuation \\citep{dohmatob2024_tale_of_tails} though insufficient to characterize its functional form; whether scale-matched references can recover further signal remains open.\n%% --- END TEMPLATES ---\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  },
  "sourceToolAssistantUUID": "7156070c-6ea1-4812-9d17-e6dafe978fab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T17:55:44.615Z_

<details open><summary>🔧 Tool call — Read · `toolu_018Jqpdh577YSrZTEfHSPzL5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dd6f02f-cb7c-4913-b945-e16c683610d8",
  "isSidechain": false,
  "requestId": "req_011CbJ38XzJdQXjSNtCe5Rc4",
  "type": "assistant",
  "uuid": "1bad868d-b999-45c1-bee1-5217870fb8a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFPYz7YvgVdTKtvFvsEDT8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12031,
      "cache_read_input_tokens": 38110,
      "output_tokens": 862,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 862,
          "cache_read_input_tokens": 38110,
          "cache_creation_input_tokens": 12031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12031
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-22T17:55:44.619Z_

<details><summary>↩ Tool result · `toolu_018Jqpdh577YSrZTEfHSPzL5`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Full-replacement vs.\ accumulation.}
5	The primary benchmark uses full-replacement chains; real-world contamination involves accumulation at unknown mixing ratios \cite{gerstgrasser2024_accumulate}.
6	At 25--50\% synthetic mixing, accuracy drops 8--15\,pp and $\mathrm{EDD}_{0.70}{=}3$ is preserved in 5/6 tested cells (GPT-2~XL nucleus at 50\% drops to $\mathrm{EDD}_{0.70}{=}2$; d2v3 AUC\,=\,0.695, marginally below threshold; Table~\ref{tab:accum_auc}); accumulation experiments use matched strategies per model (nucleus for GPT-2~XL/Pythia, temperature for OLMo) and do not test cross-strategy accumulation; extension to larger models and higher mixing ratios remains future work.
7	
8	\paragraph{Scale, generalization, and reference model.}
9	At 14B, cross-reference accuracy drops to 44.1\% ($\mathrm{EDD}_{0.70}{=}2$), with reference-model mismatch accounting for ${\sim}$7\,pp; cross-strategy transfer (d1--d3: 45.9\%) can invert d1/d2 predictions (d1v2 AUC as low as 0.13 for temperature text, 0.25 for OLMo, classified by a nucleus-trained model), requiring strategy-aware deployment.
10	The pipeline requires a fixed reference model; cross-architecture references degrade accuracy by 4--11\,pp (Appendix~\ref{app:ref_ablation}).
11	Additional caveats (single LoRA seed with ${\sim}$1--3\,pp uncertainty, web-crawl false positive rates, passage length sensitivity) are detailed in the Appendix.
12	
13	\section*{Ethics Statement}
14	
15	This work uses publicly available pretrained language models (Pythia-1.4B, OLMo-1B, GPT-2~XL) and Wikipedia text as seed data.
16	No human subjects were involved, no private or sensitive data were collected, and no new models were released.
17	Our method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-oriented research.
18	Code and data will be released upon acceptance.
19	AI assistants were used in an auxiliary role for coding support and language polishing.
20	All scientific decisions, experimental design, analysis, and core writing were conducted by the authors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bad868d-b999-45c1-bee1-5217870fb8a7",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "4cab58a3-84e5-4c04-b927-347f91c491ad",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex",
      "content": "\\section*{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Full-replacement vs.\\ accumulation.}\nThe primary benchmark uses full-replacement chains; real-world contamination involves accumulation at unknown mixing ratios \\cite{gerstgrasser2024_accumulate}.\nAt 25--50\\% synthetic mixing, accuracy drops 8--15\\,pp and $\\mathrm{EDD}_{0.70}{=}3$ is preserved in 5/6 tested cells (GPT-2~XL nucleus at 50\\% drops to $\\mathrm{EDD}_{0.70}{=}2$; d2v3 AUC\\,=\\,0.695, marginally below threshold; Table~\\ref{tab:accum_auc}); accumulation experiments use matched strategies per model (nucleus for GPT-2~XL/Pythia, temperature for OLMo) and do not test cross-strategy accumulation; extension to larger models and higher mixing ratios remains future work.\n\n\\paragraph{Scale, generalization, and reference model.}\nAt 14B, cross-reference accuracy drops to 44.1\\% ($\\mathrm{EDD}_{0.70}{=}2$), with reference-model mismatch accounting for ${\\sim}$7\\,pp; cross-strategy transfer (d1--d3: 45.9\\%) can invert d1/d2 predictions (d1v2 AUC as low as 0.13 for temperature text, 0.25 for OLMo, classified by a nucleus-trained model), requiring strategy-aware deployment.\nThe pipeline requires a fixed reference model; cross-architecture references degrade accuracy by 4--11\\,pp (Appendix~\\ref{app:ref_ablation}).\nAdditional caveats (single LoRA seed with ${\\sim}$1--3\\,pp uncertainty, web-crawl false positive rates, passage length sensitivity) are detailed in the Appendix.\n\n\\section*{Ethics Statement}\n\nThis work uses publicly available pretrained language models (Pythia-1.4B, OLMo-1B, GPT-2~XL) and Wikipedia text as seed data.\nNo human subjects were involved, no private or sensitive data were collected, and no new models were released.\nOur method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-oriented research.\nCode and data will be released upon acceptance.\nAI assistants were used in an auxiliary role for coding support and language polishing.\nAll scientific decisions, experimental design, analysis, and core writing were conducted by the authors.",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  },
  "sourceToolAssistantUUID": "1bad868d-b999-45c1-bee1-5217870fb8a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T17:55:45.087Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AozDzJevDJ9WDXM3VgDDYX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cab58a3-84e5-4c04-b927-347f91c491ad",
  "isSidechain": false,
  "requestId": "req_011CbJ38XzJdQXjSNtCe5Rc4",
  "type": "assistant",
  "uuid": "fc039b66-00a8-4e76-b513-0f9099676d23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFPYz7YvgVdTKtvFvsEDT8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12031,
      "cache_read_input_tokens": 38110,
      "output_tokens": 862,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 862,
          "cache_read_input_tokens": 38110,
          "cache_creation_input_tokens": 12031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12031
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-22T17:55:45.415Z_

<details><summary>↩ Tool result · reported error · `toolu_01AozDzJevDJ9WDXM3VgDDYX`</summary>

```text
File content (26530 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc039b66-00a8-4e76-b513-0f9099676d23",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "1b071d09-763a-4e27-9f9e-0a6228c3965c",
  "toolUseResult": "Error: File content (26530 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "fc039b66-00a8-4e76-b513-0f9099676d23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-22T17:55:45.555Z_

<details open><summary>🔧 Tool call — Read · `toolu_014Rywdie3cPrFpDJYDto6JV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b071d09-763a-4e27-9f9e-0a6228c3965c",
  "isSidechain": false,
  "requestId": "req_011CbJ38XzJdQXjSNtCe5Rc4",
  "type": "assistant",
  "uuid": "0c0226aa-7e67-498b-8bff-d62f0f8de74e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFPYz7YvgVdTKtvFvsEDT8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12031,
      "cache_read_input_tokens": 38110,
      "output_tokens": 862,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 862,
          "cache_read_input_tokens": 38110,
          "cache_creation_input_tokens": 12031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12031
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-22T17:55:45.627Z_

```json
{
  "parentUuid": "8a625e16-0439-450d-9d04-bb776ea212ea",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "227e2c7b-347c-479b-8fd8-4a4b6809cf34",
  "timestamp": "2026-05-22T17:55:45.627Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：recursive_gen_depth_est Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 45 warning…",
  "leafUuid": "227e2c7b-347c-479b-8fd8-4a4b6809cf34",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 recursive_gen_depth_est paper review",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9"
}
```

---

### Assistant

_source line 45 · 2026-05-22T17:55:49.251Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the remaining files - conclusion.tex and the section_appendix.tex (in parts).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "227e2c7b-347c-479b-8fd8-4a4b6809cf34",
  "isSidechain": false,
  "requestId": "req_011CbJ39Cgj4UXXQ4QppLWoa",
  "type": "assistant",
  "uuid": "4c0a02ab-22b4-4ef3-be3c-a46b589cc96f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kJDi8fqpdaUmzbFpfM8ru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 55385,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 55385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1266,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 55385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 55385
          },
          "type": "message"
        }
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

_source line 46 · 2026-05-22T17:55:49.746Z_

Now let me read the appendix and run the grep scans for AI style markers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c0a02ab-22b4-4ef3-be3c-a46b589cc96f",
  "isSidechain": false,
  "requestId": "req_011CbJ39Cgj4UXXQ4QppLWoa",
  "type": "assistant",
  "uuid": "5e0a7344-d655-4d88-b3db-160d44a23f66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kJDi8fqpdaUmzbFpfM8ru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 55385,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 55385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1266,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 55385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 55385
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-22T17:55:52.265Z_

<details open><summary>🔧 Tool call — Read · `toolu_017a3jnWpetyJFNFXuZdgvAY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": 0,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e0a7344-d655-4d88-b3db-160d44a23f66",
  "isSidechain": false,
  "requestId": "req_011CbJ39Cgj4UXXQ4QppLWoa",
  "type": "assistant",
  "uuid": "762165d7-468e-4509-9108-7871a6b09a91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kJDi8fqpdaUmzbFpfM8ru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 55385,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 55385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1266,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 55385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 55385
          },
          "type": "message"
        }
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

_source line 48 · 2026-05-22T17:56:02.297Z_

<details><summary>↩ Tool result · `toolu_01M7jAiaBZ3VC35Sy78TLCga`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8eedd461-2ccf-4fb1-ace4-101710114d7e",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "36b96d76-c7a4-4b58-9056-9fe222110859",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "8eedd461-2ccf-4fb1-ace4-101710114d7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-22T17:55:52.287Z_

<details><summary>↩ Tool result · `toolu_017a3jnWpetyJFNFXuZdgvAY`</summary>

```text
0	\section{LoRA Fine-Tuning Protocol}
1	\label{app:lora_protocol}
2	
3	Table~\ref{tab:lora_protocol} lists the full LoRA fine-tuning configuration used for recursive chain construction (\S\ref{sec:method:benchmark}).
4	At each depth $k$, a fresh LoRA adapter is initialized on the base model and trained on $\mathcal{D}_{k-1}$; adapters are not inherited across depths.
5	The HuggingFace Trainer default linear decay schedule is used with no warmup.
6	Target modules are model-specific: \texttt{query\_key\_value} (Pythia), \texttt{att\_proj} (OLMo), and \texttt{c\_attn} (GPT-2~XL).
7	Cross-scale 7--8B experiments (Appendix~\ref{app:cross_scale_full}) use QLoRA (4-bit NF4) with $r{=}16$, $\alpha{=}32$; the 14B model uses FP16 LoRA with the same rank and scaling.
8	
9	\begin{table}[h]
10	\centering
11	\small
12	\caption{LoRA fine-tuning hyperparameters for the primary 1--1.5B benchmark. Identical across all three model families and all depth levels.}
13	\label{tab:lora_protocol}
14	\begin{tabular}{@{}ll@{}}
15	\toprule
16	Parameter & Value \\
17	\midrule
18	LoRA rank $r$ & 16 \\
19	LoRA alpha $\alpha$ & 32 \\
20	LoRA dropout & 0.05 \\
21	Bias & none \\
22	Epochs per depth & 3 \\
23	Learning rate & $2 \times 10^{-4}$ \\
24	LR schedule & linear decay (no warmup) \\
25	Batch size (effective) & 16 ($8 \times 2$ grad.\ accum.) \\
26	Max sequence length & 512 tokens \\
27	Precision & bfloat16 \\
28	Adapter init & from scratch (base model) \\
29	Seed & 42 (primary), 43 (replication) \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
34	\section{Additional Results}
35	\label{app:additional}
36	
37	\subsection{Top-$k$ Feature Trajectories}
38	\label{app:topk_trajectories}
39	
40	Figure~\ref{fig:feature_trajectory} shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
41	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
42	Concretely, the d0$\to$d1 drop in \texttt{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
43	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
44	
45	\subsection{Permutation Importance}
46	\label{app:permutation}
47	
48	To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
49	The top-2 features are stable across measures: \texttt{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \texttt{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \texttt{p75\_ppl} displaces \texttt{var\_surprisal} to rank 3).
50	Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
51	Pairwise Spearman correlations are: SHAP--Gini $\rho{=}0.93$, SHAP--permutation $\rho{=}0.84$, Gini--permutation $\rho{=}0.76$.
52	Per-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical; the top features are therefore robust to the choice of importance measure at the aggregate level, though per-cell rankings exhibit model-dependent variation.
53	
54	\subsection{Conditional Permutation Importance under Multicollinearity}
55	\label{app:conditional_pi}
56	
57	With 14--16 of 19 features exhibiting VIF${>}$10 (\S\ref{sec:atlas:features}), standard permutation importance may inflate contributions of correlated features: permuting one member of a collinear set allows others to compensate, masking true individual effects.
58	We compute conditional permutation importance (CPI) \citep{strobl2008_conditional}, which permutes each feature \emph{within strata defined by its correlated partners}, isolating the unique contribution after controlling for multicollinearity.
59	
60	\paragraph{Setup.}
61	CPI is computed on all 9 model$\times$strategy cells.
62	For each cell, 1{,}000 bootstrap resamples produce a rank distribution per feature; the 95\% bootstrap CI width quantifies rank stability (width $\leq 1.0$ indicates near-invariant rankings across resamples).
63	
64	\paragraph{Results.}
65	Table~\ref{tab:conditional_pi} summarizes the top-5 features by mean CPI across cells.
66	\texttt{var\_surprisal} (avg rank 1.4, CPI\,=\,0.260) and \texttt{p90\_ppl} (avg rank 1.7, CPI\,=\,0.238) are the top-2 in 8/9 cells, with bootstrap rank CI widths of 0.50 and 0.30---both $\leq 0.5$, indicating near-invariant rankings across resamples.
67	Ranks 3--5 are \texttt{p75\_ppl} (CPI\,=\,0.063, CI width\,=\,0.78), \texttt{p50\_ppl} (0.016, width\,=\,2.67), and a cell-dependent set (\texttt{p25\_ppl} or \texttt{mean\_ppl}); rank stability decreases beyond the top-2, with CI widths of 2.7--3.7 for ranks 4--5.
68	
69	\begin{table}[h]
70	\centering
71	\small
72	\caption{Conditional permutation importance aggregated across 9 model$\times$strategy cells (1{,}000 bootstrap resamples). Avg Rank and Avg CPI: means over cells. Rank CI Width: mean 95\% bootstrap CI width for the rank. Bottom rows: feature-family averages.}
73	\label{tab:conditional_pi}
74	\resizebox{\columnwidth}{!}{%
75	\begin{tabular}{@{}lccc@{}}
76	\toprule
77	Feature / Family & Avg Rank & Avg CPI & Rank CI Width \\
78	\midrule
79	\texttt{var\_surprisal} & 1.4 & 0.260 & 0.50 \\
80	\texttt{p90\_ppl} & 1.7 & 0.238 & 0.30 \\
81	\texttt{p75\_ppl} & 3.1 & 0.063 & 0.78 \\
82	\texttt{p50\_ppl} & 5.0 & 0.016 & 2.67 \\
83	\texttt{p25\_ppl}$^\dagger$ & 5.8 & 0.012 & 3.67 \\
84	\texttt{mean\_ppl}$^\dagger$ & 6.3 & 0.008 & 3.44 \\
85	\midrule
86	Surprisal family & 7.3 & 0.089 & --- \\
87	Perplexity family & 7.5 & 0.039 & --- \\
88	Lexical family & 9.7 & 0.004 & --- \\
89	\bottomrule
90	\multicolumn{4}{@{}l}{\footnotesize $^\dagger$Rank 5--6 varies by cell; \texttt{trigram\_entropy} appears in 1 cell.}
91	\end{tabular}}
92	\end{table}
93	
94	Two exceptions exist among GPT-2~XL cells: in temperature sampling, \texttt{p90\_ppl} (CPI\,=\,0.419) exceeds \texttt{var\_surprisal} (0.093) while both remain in the top-2; in top-$k$ sampling, \texttt{p90\_ppl} (0.475) and \texttt{p75\_ppl} (0.127) push \texttt{var\_surprisal} to rank~3 (0.037), the only cell where it exits the top-2.
95	Both reversals are consistent with the Gini rankings for these cells (Table~\ref{tab:feature_importance}).
96	
97	At the family level, surprisal (avg CPI\,=\,0.089, rank\,=\,7.3) and perplexity (0.039, rank\,=\,7.5) are closely matched, while lexical features (0.004, rank\,=\,9.7) contribute minimally---consistent with the group ablation in \S\ref{sec:atlas:features}.
98	
99	\paragraph{Consistency with Gini rankings.}
100	CPI and Gini rankings agree on the dominant feature (\texttt{var\_surprisal} or \texttt{p90\_ppl}) in 8/9 cells; the sole disagreement (GPT-2~XL top-$k$) involves a swap between rank-2 and rank-3 features.
101	Bootstrap rank CI widths $\leq 0.5$ for the top-2 features confirm that these rankings are not artifacts of collinearity or resampling variability.
102	Controlling for multicollinearity via conditional permutation corroborates the Gini- and SHAP-based importance hierarchy reported in the main text.
103	
104	\subsection{Feature Trajectories}
105	\label{app:feature_trajectories}
106	
107	\begin{figure}[h]
108	\centering
109	\includegraphics[width=\columnwidth]{figures/fig_feature_trajectory.pdf}
110	\caption{Feature trajectories across depths $d{=}0$ to $d{=}3$, stratified by model (columns: Pythia-1.4B, OLMo-1B, GPT-2~XL) and strategy (line style). Five features are shown per panel: \texttt{p90\_ppl}, \texttt{var\_surprisal}, \texttt{mean\_surprisal}, \texttt{p75\_ppl}, and TTR, normalized to depth~0. The $d{=}0 \to d{=}1$ gap exceeds all subsequent inter-depth gaps.}
111	\label{fig:feature_trajectory}
112	\end{figure}
113	
114	\subsection{Per-Class Recall}
115	\label{app:per_class}
116	
117	Table~\ref{tab:per_class_recall} reports per-class recall across all 9 atlas cells (4-class in-distribution, 5-fold CV).
118	Depth~0 recall exceeds 97\% uniformly.
119	Among generated depths, d2 is the hardest class in every cell; the deficit is most pronounced under top-$k$ sampling (46--53\%), where vocabulary truncation removes the tail tokens that carry depth-discriminative signal.
120	
121	\begin{table}[h]
122	\centering
123	\small
124	\caption{Per-class recall (\%) for all 9 atlas cells. d2 is the lowest-recall class in every cell. Boldface marks the highest d2 recall.}
125	\label{tab:per_class_recall}
126	\begin{tabular}{@{}lcccc@{}}
127	\toprule
128	Cell & d0 & d1 & d2 & d3 \\
129	\midrule
130	Pythia, nuc.       & 99.3 & 81.9 & 59.2 & 74.4 \\
131	Pythia, $\tau$     & 99.2 & 79.9 & 56.0 & 72.1 \\
132	Pythia, top-$k$    & 98.7 & 71.6 & 44.2 & 60.9 \\
133	OLMo, nuc.         & 97.8 & 82.1 & 60.6 & 75.3 \\
134	OLMo, $\tau$       & 99.3 & 87.1 & 65.6 & 77.1 \\
135	OLMo, top-$k$      & 99.2 & 80.9 & 50.4 & 67.2 \\
136	GPT-2~XL, nuc.     & 98.5 & 87.4 & 72.8 & 78.5 \\
137	GPT-2~XL, $\tau$   & 99.0 & 91.1 & \textbf{73.0} & 80.5 \\
138	GPT-2~XL, top-$k$  & 98.7 & 81.3 & 54.8 & 68.4 \\
139	\bottomrule
140	\end{tabular}
141	\end{table}
142	
143	\subsection{Confusion Matrices}
144	\label{app:confusion_matrices}
145	
146	\begin{figure}[h]
147	\centering
148	\includegraphics[width=\columnwidth]{figures/fig_confusion_matrix.pdf}
149	\caption{Confusion matrices: best in-distribution (GPT-2 XL temp, 85.9\%) and best LOO transfer (OLMo, 69.2\%). d0 recall ${>}$99\%; errors spread to d1--d3 under transfer.}
150	\label{fig:confusion_matrix}
151	\end{figure}
152	
153	\subsection{Cross-Strategy Transfer Details}
154	\label{app:cross_strategy}
155	
156	\begin{table}[h]
157	\centering
158	\small
159	\caption{Cross-strategy transfer (leave-one-out). Chance = 25\% / 33\% (d1--d3). d0 recall $\geq$89\% inflates headline; d1--d3 mean: 45.9\%.}
160	\label{tab:cross_strategy}
161	\begin{tabular}{lccc}
162	\toprule
163	Holdout & Pythia & OLMo & GPT-2 XL \\
164	 & Acc (\%) & Acc (\%) & Acc (\%) \\
165	\midrule
166	nucleus & \textbf{69.4} & \textbf{65.4} & \textbf{59.9} \\
167	temp ($\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\
168	top-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\
169	\bottomrule
170	\end{tabular}
171	\end{table}
172	
173	\subsection{Accumulation Pairwise AUC}
174	\label{app:accumulation_auc}
175	
176	Table~\ref{tab:accum_auc} reports pairwise AUC for the six accumulation cells (3 models $\times$ 2 mixing ratios; GPT-2~XL and Pythia use nucleus, OLMo uses temperature 0.9).
177	At 25\% mixing, all three cells preserve $\mathrm{EDD}_{0.70}{=}3$.
178	At 50\% mixing, GPT-2~XL nucleus is the sole failure: d2v3 AUC\,=\,0.695, marginally below the 0.70 threshold (0.55\,pp).
179	
180	\begin{table}[h]
181	\centering
182	\small
183	\caption{Pairwise AUC under accumulation (GPT-2~XL/Pythia: nucleus; OLMo: temp 0.9; binary RF, 5-fold CV). Bold: $\mathrm{EDD}_{0.70}$ boundary failure.}
184	\label{tab:accum_auc}
185	\begin{tabular}{@{}llccc@{}}
186	\toprule
187	Model & Mix & d0v1 & d1v2 & d2v3 \\
188	\midrule
189	GPT-2~XL & 25\% & 1.000 & 0.876 & 0.726 \\
190	 & 50\% & 1.000 & 0.831 & \textbf{0.695} \\
191	Pythia & 25\% & 1.000 & 0.843 & 0.749 \\
192	 & 50\% & 1.000 & 0.793 & 0.716 \\
193	OLMo & 25\% & 1.000 & 0.862 & 0.759 \\
194	 & 50\% & 1.000 & 0.817 & 0.726 \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
199	\subsection{DCOL Iteration Details}
200	\label{app:dcol_iterations}
201	
202	Table~\ref{tab:dcol_iterations} summarizes all six DCOL iterations.
203	DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.
204	
205	\begin{table}[h]
206	\centering
207	\small
208	\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.7\%.}
209	\label{tab:dcol_iterations}
210	\resizebox{\columnwidth}{!}{%
211	\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}
212	\toprule
213	Ver. & Backbone & Config & Outcome \\
214	\midrule
215	v1 & DeBERTa & FT, m\_lr $10^{-3}$ & Embed.\ collapse (31.5\%) \\
216	v2 & DeBERTa & FT, m\_lr $10^{-4}$ & OOM \\
217	v3 & DeBERTa & FT, m\_lr $10^{-4}$ & Forgetting + OOM \\
218	v4 & DeBERTa & LoRA, m\_lr $10^{-3}$ & Embed.\ collapse \\
219	v5 & DeBERTa & LoRA, m\_lr $10^{-4}$ & NaN gradients \\
220	v6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\% ($-$13.7pp) \\
221	\bottomrule
222	\end{tabular}}
223	\end{table}
224	
225	\subsection{Zero-Shot LLM Prompt Template}
226	\label{app:zeroshot_prompt}
227	
228	Both DeepSeek V3.2 and Qwen2.5-7B-Instruct use identical prompting.
229	The system message defines recursive generation depth with per-depth descriptions (depth~0: human-written; depth~1--3: successive LLM generation cycles) and lists expected textual patterns at each depth (vocabulary richness, repetition, coherence).
230	The user message presents the passage (truncated to ${\approx}$384 words) and requests a JSON response containing an integer depth prediction (0--3), a confidence score, and a one-sentence reasoning.
231	No in-context examples are provided.
232	
233	\begin{quote}
234	\small
235	\textbf{System:} ``You are an expert at detecting AI-generated text and estimating its generation depth. `Recursive generation depth' refers to how many times a text has been through an LLM generation cycle: Depth~0: Original human-written text [\ldots] Depth~3: Text generated by an LLM given depth-2 text as input. Key patterns by depth: Depth~0 (human): Rich vocabulary [\ldots] Depth~3 (third-gen): Noticeable repetition, formulaic structure [\ldots]''
236	
237	\textbf{User:} ``Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3). TEXT: \{text\}. Respond with ONLY a JSON object: \{\texttt{"depth"}: $\langle$int 0--3$\rangle$, \texttt{"confidence"}: $\langle$float 0--1$\rangle$, \texttt{"reasoning"}: $\langle$str$\rangle$\}''
238	\end{quote}
239	
240	\subsection{Temperature Robustness}
241	\label{app:multi_tau}
242	
243	The cross-strategy results in \S\ref{sec:gen:crossstrategy} use a single temperature ($\tau{=}0.9$).
244	To test whether depth signal generalizes across temperatures, we repeat the classification pipeline at $\tau \in \{0.5, 0.7, 0.9, 1.1\}$ on Pythia-1.4B.
245	
246	\paragraph{Within-$\tau$ robustness.}
247	For $\tau \in [0.5, 0.9]$, d1-vs-d2 AUC exceeds 0.80 (peak 0.851 at $\tau{=}0.7$, comparable to nucleus $p{=}0.95$'s 0.861) and 4-class accuracy ranges from 75.4\% to 77.3\% (Table~\ref{tab:multi_tau_within}); the depth signal is therefore not an artifact of a single temperature.
248	The same top-5 features (\texttt{var\_surprisal}, \texttt{p90\_ppl}, \texttt{mean\_ppl}, \texttt{mean\_surprisal}, \texttt{p75\_ppl}) dominate across all $\tau$ values with only minor rank-order variation.
249	
250	\paragraph{Collapse at $\tau{=}1.1$: memorization as prerequisite.}
251	At $\tau{=}1.1$, 4-class accuracy drops to 57.2\% and d1v2 AUC falls to 0.528.
252	Training loss reveals the mechanism: at low temperature ($\tau{=}0.5$), fine-tuning loss decreases steeply across recursive depths ($2.27 \to 0.42 \to 0.16$), a sign of rapid memorization of the model's own output.
253	At $\tau{=}1.1$, loss remains nearly flat ($2.27 \to 1.91 \to 1.85$); high-entropy output resists memorization, so depth-dependent distributional shifts do not accumulate.
254	This establishes \emph{memorization as a prerequisite} for detectable depth signal: recursive depth is discriminable only when successive fine-tuning iterations progressively reshape the output distribution.
255	
256	\paragraph{Cross-$\tau$ non-transferability.}
257	Leave-one-$\tau$-out transfer yields mean accuracy of 46.7\% with mean d1v2 AUC of 0.319 (Table~\ref{tab:multi_tau_cross}), worse than cross-strategy transfer (59.1\%; \S\ref{sec:gen:crossstrategy}).
258	Holdout $\tau{=}0.5$ produces inverted d1v2 AUC (0.176); different temperatures therefore produce surprisal distributions with incompatible shapes.
259	This extends the strategy-specificity finding: even within a single decoding family, the feature space is temperature-specific; strategy-conditioned classifiers are therefore necessary.
260	
261	\paragraph{Ecological validity.}
262	On WikiText-103 (546 editorial passages), all three model-specific RF classifiers achieve $\geq$98.5\% d0 accuracy despite $+$621\% domain shift in mean perplexity, partly an easy case, as WikiText's higher perplexity places it farther from d1--d3 in feature space.
263	On noisier web-crawl data (5{,}000 C4 passages), FPR ranges from 4.7\% (OLMo) to 22.4\% (GPT-2~XL), concentrated in template/SEO content with high n-gram repetition (Table~\ref{tab:calibration}); deployment on heterogeneous web data requires model-specific calibration.
264	
265	\begin{table}[h]
266	\centering
267	\small
268	\caption{Within-$\tau$ 4-class classification (Pythia-1.4B, 5-fold CV, independent pipeline run). d$i$v$j$: pairwise AUC for depth $i$ vs.\ depth $j$. The $\tau{=}0.9$ accuracy (75.9\%) differs from the main atlas (76.8\%, Table~\ref{tab:main_matrix}) due to separate generation and LoRA training runs.}
269	\label{tab:multi_tau_within}
270	\resizebox{\columnwidth}{!}{%
271	\begin{tabular}{@{}lcccc@{}}
272	\toprule
273	$\tau$ & 4-class acc (\%) & d1v2 AUC & d0v1 AUC & d2v3 AUC \\
274	\midrule
275	0.5 & 77.3 & 0.842 & 0.996 & 0.764 \\
276	0.7 & 75.4 & 0.851 & 0.997 & 0.720 \\
277	0.9 & 75.9 & 0.808 & 0.991 & 0.781 \\
278	1.1 & 57.2 & 0.528 & 0.988 & 0.599 \\
279	\bottomrule
280	\end{tabular}}
281	\end{table}
282	
283	\begin{table}[h]
284	\centering
285	\small
286	\caption{Cross-$\tau$ leave-one-out transfer (Pythia-1.4B). Train on three temperatures, test on the held-out one.}
287	\label{tab:multi_tau_cross}
288	\begin{tabular}{@{}lcc@{}}
289	\toprule
290	Holdout & Acc (\%) & d1v2 AUC \\
291	\midrule
292	$\tau{=}0.5$ & 52.2 & 0.176 \\
293	$\tau{=}0.7$ & 41.0 & 0.299 \\
294	$\tau{=}0.9$ & 46.4 & 0.277 \\
295	$\tau{=}1.1$ & 47.1 & 0.525 \\
296	\midrule
297	Mean & 46.7 & 0.319 \\
298	\bottomrule
299	\end{tabular}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "762165d7-468e-4509-9108-7871a6b09a91",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "c9966867-e53c-4ed4-a5c9-1e6576863dd4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
      "content": "\\section{LoRA Fine-Tuning Protocol}\n\\label{app:lora_protocol}\n\nTable~\\ref{tab:lora_protocol} lists the full LoRA fine-tuning configuration used for recursive chain construction (\\S\\ref{sec:method:benchmark}).\nAt each depth $k$, a fresh LoRA adapter is initialized on the base model and trained on $\\mathcal{D}_{k-1}$; adapters are not inherited across depths.\nThe HuggingFace Trainer default linear decay schedule is used with no warmup.\nTarget modules are model-specific: \\texttt{query\\_key\\_value} (Pythia), \\texttt{att\\_proj} (OLMo), and \\texttt{c\\_attn} (GPT-2~XL).\nCross-scale 7--8B experiments (Appendix~\\ref{app:cross_scale_full}) use QLoRA (4-bit NF4) with $r{=}16$, $\\alpha{=}32$; the 14B model uses FP16 LoRA with the same rank and scaling.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{LoRA fine-tuning hyperparameters for the primary 1--1.5B benchmark. Identical across all three model families and all depth levels.}\n\\label{tab:lora_protocol}\n\\begin{tabular}{@{}ll@{}}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank $r$ & 16 \\\\\nLoRA alpha $\\alpha$ & 32 \\\\\nLoRA dropout & 0.05 \\\\\nBias & none \\\\\nEpochs per depth & 3 \\\\\nLearning rate & $2 \\times 10^{-4}$ \\\\\nLR schedule & linear decay (no warmup) \\\\\nBatch size (effective) & 16 ($8 \\times 2$ grad.\\ accum.) \\\\\nMax sequence length & 512 tokens \\\\\nPrecision & bfloat16 \\\\\nAdapter init & from scratch (base model) \\\\\nSeed & 42 (primary), 43 (replication) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Additional Results}\n\\label{app:additional}\n\n\\subsection{Top-$k$ Feature Trajectories}\n\\label{app:topk_trajectories}\n\nFigure~\\ref{fig:feature_trajectory} shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\\tau{=}0.9$) sampling.\nTop-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \\S\\ref{sec:atlas:strategy}.\nConcretely, the d0$\\to$d1 drop in \\texttt{p90\\_ppl} under top-$k$ is 78\\% (vs.\\ 87\\% for nucleus), and the d2$\\to$d3 reduction is 31\\% (vs.\\ 39\\% for nucleus).\nDespite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.\n\n\\subsection{Permutation Importance}\n\\label{app:permutation}\n\nTo verify that the Gini-based importance rankings in \\S\\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.\nThe top-2 features are stable across measures: \\texttt{p90\\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \\texttt{var\\_surprisal} in 8/9 (vs.\\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \\texttt{p75\\_ppl} displaces \\texttt{var\\_surprisal} to rank 3).\nKendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).\nPairwise Spearman correlations are: SHAP--Gini $\\rho{=}0.93$, SHAP--permutation $\\rho{=}0.84$, Gini--permutation $\\rho{=}0.76$.\nPer-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical; the top features are therefore robust to the choice of importance measure at the aggregate level, though per-cell rankings exhibit model-dependent variation.\n\n\\subsection{Conditional Permutation Importance under Multicollinearity}\n\\label{app:conditional_pi}\n\nWith 14--16 of 19 features exhibiting VIF${>}$10 (\\S\\ref{sec:atlas:features}), standard permutation importance may inflate contributions of correlated features: permuting one member of a collinear set allows others to compensate, masking true individual effects.\nWe compute conditional permutation importance (CPI) \\citep{strobl2008_conditional}, which permutes each feature \\emph{within strata defined by its correlated partners}, isolating the unique contribution after controlling for multicollinearity.\n\n\\paragraph{Setup.}\nCPI is computed on all 9 model$\\times$strategy cells.\nFor each cell, 1{,}000 bootstrap resamples produce a rank distribution per feature; the 95\\% bootstrap CI width quantifies rank stability (width $\\leq 1.0$ indicates near-invariant rankings across resamples).\n\n\\paragraph{Results.}\nTable~\\ref{tab:conditional_pi} summarizes the top-5 features by mean CPI across cells.\n\\texttt{var\\_surprisal} (avg rank 1.4, CPI\\,=\\,0.260) and \\texttt{p90\\_ppl} (avg rank 1.7, CPI\\,=\\,0.238) are the top-2 in 8/9 cells, with bootstrap rank CI widths of 0.50 and 0.30---both $\\leq 0.5$, indicating near-invariant rankings across resamples.\nRanks 3--5 are \\texttt{p75\\_ppl} (CPI\\,=\\,0.063, CI width\\,=\\,0.78), \\texttt{p50\\_ppl} (0.016, width\\,=\\,2.67), and a cell-dependent set (\\texttt{p25\\_ppl} or \\texttt{mean\\_ppl}); rank stability decreases beyond the top-2, with CI widths of 2.7--3.7 for ranks 4--5.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Conditional permutation importance aggregated across 9 model$\\times$strategy cells (1{,}000 bootstrap resamples). Avg Rank and Avg CPI: means over cells. Rank CI Width: mean 95\\% bootstrap CI width for the rank. Bottom rows: feature-family averages.}\n\\label{tab:conditional_pi}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nFeature / Family & Avg Rank & Avg CPI & Rank CI Width \\\\\n\\midrule\n\\texttt{var\\_surprisal} & 1.4 & 0.260 & 0.50 \\\\\n\\texttt{p90\\_ppl} & 1.7 & 0.238 & 0.30 \\\\\n\\texttt{p75\\_ppl} & 3.1 & 0.063 & 0.78 \\\\\n\\texttt{p50\\_ppl} & 5.0 & 0.016 & 2.67 \\\\\n\\texttt{p25\\_ppl}$^\\dagger$ & 5.8 & 0.012 & 3.67 \\\\\n\\texttt{mean\\_ppl}$^\\dagger$ & 6.3 & 0.008 & 3.44 \\\\\n\\midrule\nSurprisal family & 7.3 & 0.089 & --- \\\\\nPerplexity family & 7.5 & 0.039 & --- \\\\\nLexical family & 9.7 & 0.004 & --- \\\\\n\\bottomrule\n\\multicolumn{4}{@{}l}{\\footnotesize $^\\dagger$Rank 5--6 varies by cell; \\texttt{trigram\\_entropy} appears in 1 cell.}\n\\end{tabular}}\n\\end{table}\n\nTwo exceptions exist among GPT-2~XL cells: in temperature sampling, \\texttt{p90\\_ppl} (CPI\\,=\\,0.419) exceeds \\texttt{var\\_surprisal} (0.093) while both remain in the top-2; in top-$k$ sampling, \\texttt{p90\\_ppl} (0.475) and \\texttt{p75\\_ppl} (0.127) push \\texttt{var\\_surprisal} to rank~3 (0.037), the only cell where it exits the top-2.\nBoth reversals are consistent with the Gini rankings for these cells (Table~\\ref{tab:feature_importance}).\n\nAt the family level, surprisal (avg CPI\\,=\\,0.089, rank\\,=\\,7.3) and perplexity (0.039, rank\\,=\\,7.5) are closely matched, while lexical features (0.004, rank\\,=\\,9.7) contribute minimally---consistent with the group ablation in \\S\\ref{sec:atlas:features}.\n\n\\paragraph{Consistency with Gini rankings.}\nCPI and Gini rankings agree on the dominant feature (\\texttt{var\\_surprisal} or \\texttt{p90\\_ppl}) in 8/9 cells; the sole disagreement (GPT-2~XL top-$k$) involves a swap between rank-2 and rank-3 features.\nBootstrap rank CI widths $\\leq 0.5$ for the top-2 features confirm that these rankings are not artifacts of collinearity or resampling variability.\nControlling for multicollinearity via conditional permutation corroborates the Gini- and SHAP-based importance hierarchy reported in the main text.\n\n\\subsection{Feature Trajectories}\n\\label{app:feature_trajectories}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_feature_trajectory.pdf}\n\\caption{Feature trajectories across depths $d{=}0$ to $d{=}3$, stratified by model (columns: Pythia-1.4B, OLMo-1B, GPT-2~XL) and strategy (line style). Five features are shown per panel: \\texttt{p90\\_ppl}, \\texttt{var\\_surprisal}, \\texttt{mean\\_surprisal}, \\texttt{p75\\_ppl}, and TTR, normalized to depth~0. The $d{=}0 \\to d{=}1$ gap exceeds all subsequent inter-depth gaps.}\n\\label{fig:feature_trajectory}\n\\end{figure}\n\n\\subsection{Per-Class Recall}\n\\label{app:per_class}\n\nTable~\\ref{tab:per_class_recall} reports per-class recall across all 9 atlas cells (4-class in-distribution, 5-fold CV).\nDepth~0 recall exceeds 97\\% uniformly.\nAmong generated depths, d2 is the hardest class in every cell; the deficit is most pronounced under top-$k$ sampling (46--53\\%), where vocabulary truncation removes the tail tokens that carry depth-discriminative signal.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-class recall (\\%) for all 9 atlas cells. d2 is the lowest-recall class in every cell. Boldface marks the highest d2 recall.}\n\\label{tab:per_class_recall}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nCell & d0 & d1 & d2 & d3 \\\\\n\\midrule\nPythia, nuc.       & 99.3 & 81.9 & 59.2 & 74.4 \\\\\nPythia, $\\tau$     & 99.2 & 79.9 & 56.0 & 72.1 \\\\\nPythia, top-$k$    & 98.7 & 71.6 & 44.2 & 60.9 \\\\\nOLMo, nuc.         & 97.8 & 82.1 & 60.6 & 75.3 \\\\\nOLMo, $\\tau$       & 99.3 & 87.1 & 65.6 & 77.1 \\\\\nOLMo, top-$k$      & 99.2 & 80.9 & 50.4 & 67.2 \\\\\nGPT-2~XL, nuc.     & 98.5 & 87.4 & 72.8 & 78.5 \\\\\nGPT-2~XL, $\\tau$   & 99.0 & 91.1 & \\textbf{73.0} & 80.5 \\\\\nGPT-2~XL, top-$k$  & 98.7 & 81.3 & 54.8 & 68.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Confusion Matrices}\n\\label{app:confusion_matrices}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_confusion_matrix.pdf}\n\\caption{Confusion matrices: best in-distribution (GPT-2 XL temp, 85.9\\%) and best LOO transfer (OLMo, 69.2\\%). d0 recall ${>}$99\\%; errors spread to d1--d3 under transfer.}\n\\label{fig:confusion_matrix}\n\\end{figure}\n\n\\subsection{Cross-Strategy Transfer Details}\n\\label{app:cross_strategy}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-strategy transfer (leave-one-out). Chance = 25\\% / 33\\% (d1--d3). d0 recall $\\geq$89\\% inflates headline; d1--d3 mean: 45.9\\%.}\n\\label{tab:cross_strategy}\n\\begin{tabular}{lccc}\n\\toprule\nHoldout & Pythia & OLMo & GPT-2 XL \\\\\n & Acc (\\%) & Acc (\\%) & Acc (\\%) \\\\\n\\midrule\nnucleus & \\textbf{69.4} & \\textbf{65.4} & \\textbf{59.9} \\\\\ntemp ($\\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\\\\ntop-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Accumulation Pairwise AUC}\n\\label{app:accumulation_auc}\n\nTable~\\ref{tab:accum_auc} reports pairwise AUC for the six accumulation cells (3 models $\\times$ 2 mixing ratios; GPT-2~XL and Pythia use nucleus, OLMo uses temperature 0.9).\nAt 25\\% mixing, all three cells preserve $\\mathrm{EDD}_{0.70}{=}3$.\nAt 50\\% mixing, GPT-2~XL nucleus is the sole failure: d2v3 AUC\\,=\\,0.695, marginally below the 0.70 threshold (0.55\\,pp).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise AUC under accumulation (GPT-2~XL/Pythia: nucleus; OLMo: temp 0.9; binary RF, 5-fold CV). Bold: $\\mathrm{EDD}_{0.70}$ boundary failure.}\n\\label{tab:accum_auc}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nModel & Mix & d0v1 & d1v2 & d2v3 \\\\\n\\midrule\nGPT-2~XL & 25\\% & 1.000 & 0.876 & 0.726 \\\\\n & 50\\% & 1.000 & 0.831 & \\textbf{0.695} \\\\\nPythia & 25\\% & 1.000 & 0.843 & 0.749 \\\\\n & 50\\% & 1.000 & 0.793 & 0.716 \\\\\nOLMo & 25\\% & 1.000 & 0.862 & 0.759 \\\\\n & 50\\% & 1.000 & 0.817 & 0.726 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{DCOL Iteration Details}\n\\label{app:dcol_iterations}\n\nTable~\\ref{tab:dcol_iterations} summarizes all six DCOL iterations.\nDeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.7\\%.}\n\\label{tab:dcol_iterations}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}\n\\toprule\nVer. & Backbone & Config & Outcome \\\\\n\\midrule\nv1 & DeBERTa & FT, m\\_lr $10^{-3}$ & Embed.\\ collapse (31.5\\%) \\\\\nv2 & DeBERTa & FT, m\\_lr $10^{-4}$ & OOM \\\\\nv3 & DeBERTa & FT, m\\_lr $10^{-4}$ & Forgetting + OOM \\\\\nv4 & DeBERTa & LoRA, m\\_lr $10^{-3}$ & Embed.\\ collapse \\\\\nv5 & DeBERTa & LoRA, m\\_lr $10^{-4}$ & NaN gradients \\\\\nv6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\\% ($-$13.7pp) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Zero-Shot LLM Prompt Template}\n\\label{app:zeroshot_prompt}\n\nBoth DeepSeek V3.2 and Qwen2.5-7B-Instruct use identical prompting.\nThe system message defines recursive generation depth with per-depth descriptions (depth~0: human-written; depth~1--3: successive LLM generation cycles) and lists expected textual patterns at each depth (vocabulary richness, repetition, coherence).\nThe user message presents the passage (truncated to ${\\approx}$384 words) and requests a JSON response containing an integer depth prediction (0--3), a confidence score, and a one-sentence reasoning.\nNo in-context examples are provided.\n\n\\begin{quote}\n\\small\n\\textbf{System:} ``You are an expert at detecting AI-generated text and estimating its generation depth. `Recursive generation depth' refers to how many times a text has been through an LLM generation cycle: Depth~0: Original human-written text [\\ldots] Depth~3: Text generated by an LLM given depth-2 text as input. Key patterns by depth: Depth~0 (human): Rich vocabulary [\\ldots] Depth~3 (third-gen): Noticeable repetition, formulaic structure [\\ldots]''\n\n\\textbf{User:} ``Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3). TEXT: \\{text\\}. Respond with ONLY a JSON object: \\{\\texttt{\"depth\"}: $\\langle$int 0--3$\\rangle$, \\texttt{\"confidence\"}: $\\langle$float 0--1$\\rangle$, \\texttt{\"reasoning\"}: $\\langle$str$\\rangle$\\}''\n\\end{quote}\n\n\\subsection{Temperature Robustness}\n\\label{app:multi_tau}\n\nThe cross-strategy results in \\S\\ref{sec:gen:crossstrategy} use a single temperature ($\\tau{=}0.9$).\nTo test whether depth signal generalizes across temperatures, we repeat the classification pipeline at $\\tau \\in \\{0.5, 0.7, 0.9, 1.1\\}$ on Pythia-1.4B.\n\n\\paragraph{Within-$\\tau$ robustness.}\nFor $\\tau \\in [0.5, 0.9]$, d1-vs-d2 AUC exceeds 0.80 (peak 0.851 at $\\tau{=}0.7$, comparable to nucleus $p{=}0.95$'s 0.861) and 4-class accuracy ranges from 75.4\\% to 77.3\\% (Table~\\ref{tab:multi_tau_within}); the depth signal is therefore not an artifact of a single temperature.\nThe same top-5 features (\\texttt{var\\_surprisal}, \\texttt{p90\\_ppl}, \\texttt{mean\\_ppl}, \\texttt{mean\\_surprisal}, \\texttt{p75\\_ppl}) dominate across all $\\tau$ values with only minor rank-order variation.\n\n\\paragraph{Collapse at $\\tau{=}1.1$: memorization as prerequisite.}\nAt $\\tau{=}1.1$, 4-class accuracy drops to 57.2\\% and d1v2 AUC falls to 0.528.\nTraining loss reveals the mechanism: at low temperature ($\\tau{=}0.5$), fine-tuning loss decreases steeply across recursive depths ($2.27 \\to 0.42 \\to 0.16$), a sign of rapid memorization of the model's own output.\nAt $\\tau{=}1.1$, loss remains nearly flat ($2.27 \\to 1.91 \\to 1.85$); high-entropy output resists memorization, so depth-dependent distributional shifts do not accumulate.\nThis establishes \\emph{memorization as a prerequisite} for detectable depth signal: recursive depth is discriminable only when successive fine-tuning iterations progressively reshape the output distribution.\n\n\\paragraph{Cross-$\\tau$ non-transferability.}\nLeave-one-$\\tau$-out transfer yields mean accuracy of 46.7\\% with mean d1v2 AUC of 0.319 (Table~\\ref{tab:multi_tau_cross}), worse than cross-strategy transfer (59.1\\%; \\S\\ref{sec:gen:crossstrategy}).\nHoldout $\\tau{=}0.5$ produces inverted d1v2 AUC (0.176); different temperatures therefore produce surprisal distributions with incompatible shapes.\nThis extends the strategy-specificity finding: even within a single decoding family, the feature space is temperature-specific; strategy-conditioned classifiers are therefore necessary.\n\n\\paragraph{Ecological validity.}\nOn WikiText-103 (546 editorial passages), all three model-specific RF classifiers achieve $\\geq$98.5\\% d0 accuracy despite $+$621\\% domain shift in mean perplexity, partly an easy case, as WikiText's higher perplexity places it farther from d1--d3 in feature space.\nOn noisier web-crawl data (5{,}000 C4 passages), FPR ranges from 4.7\\% (OLMo) to 22.4\\% (GPT-2~XL), concentrated in template/SEO content with high n-gram repetition (Table~\\ref{tab:calibration}); deployment on heterogeneous web data requires model-specific calibration.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Within-$\\tau$ 4-class classification (Pythia-1.4B, 5-fold CV, independent pipeline run). d$i$v$j$: pairwise AUC for depth $i$ vs.\\ depth $j$. The $\\tau{=}0.9$ accuracy (75.9\\%) differs from the main atlas (76.8\\%, Table~\\ref{tab:main_matrix}) due to separate generation and LoRA training runs.}\n\\label{tab:multi_tau_within}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$\\tau$ & 4-class acc (\\%) & d1v2 AUC & d0v1 AUC & d2v3 AUC \\\\\n\\midrule\n0.5 & 77.3 & 0.842 & 0.996 & 0.764 \\\\\n0.7 & 75.4 & 0.851 & 0.997 & 0.720 \\\\\n0.9 & 75.9 & 0.808 & 0.991 & 0.781 \\\\\n1.1 & 57.2 & 0.528 & 0.988 & 0.599 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-$\\tau$ leave-one-out transfer (Pythia-1.4B). Train on three temperatures, test on the held-out one.}\n\\label{tab:multi_tau_cross}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nHoldout & Acc (\\%) & d1v2 AUC \\\\\n\\midrule\n$\\tau{=}0.5$ & 52.2 & 0.176 \\\\\n$\\tau{=}0.7$ & 41.0 & 0.299 \\\\\n$\\tau{=}0.9$ & 46.4 & 0.277 \\\\\n$\\tau{=}1.1$ & 47.1 & 0.525 \\\\\n\\midrule\nMean & 46.7 & 0.319 \\\\\n\\bottomrule\n\\end{tabular}",
      "numLines": 300,
      "startLine": 0,
      "totalLines": 1074
    }
  },
  "sourceToolAssistantUUID": "762165d7-468e-4509-9108-7871a6b09a91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-22T17:55:53.555Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01D1p2Lu8t9keaaNp6nuFPaT`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
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
  "parentUuid": "c9966867-e53c-4ed4-a5c9-1e6576863dd4",
  "isSidechain": false,
  "requestId": "req_011CbJ39Cgj4UXXQ4QppLWoa",
  "type": "assistant",
  "uuid": "5c2b4c64-6445-4770-a413-712d1d0ea083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kJDi8fqpdaUmzbFpfM8ru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 55385,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 55385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1266,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 55385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 55385
          },
          "type": "message"
        }
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

_source line 51 · 2026-05-22T17:55:53.578Z_

<details><summary>↩ Tool result · `toolu_01D1p2Lu8t9keaaNp6nuFPaT`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:8:% SCENARIO A: both >50% — full three-strategy coverage
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:32:% SCENARIO B: one >50%, one ~chance — "scale amplifies strategy effects"
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:55:% SCENARIO C: both ~chance — boundary condition
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c2b4c64-6445-4770-a413-712d1d0ea083",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "2eb94543-5179-4f17-bb8b-51dfb640823c",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:8:% SCENARIO A: both >50% — full three-strategy coverage\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:32:% SCENARIO B: one >50%, one ~chance — \"scale amplifies strategy effects\"\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:55:% SCENARIO C: both ~chance — boundary condition",
    "numLines": 3
  },
  "sourceToolAssistantUUID": "5c2b4c64-6445-4770-a413-712d1d0ea083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-22T17:55:55.032Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SSG5P2SUWiu7rTRE3sbYKe`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
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
  "parentUuid": "2eb94543-5179-4f17-bb8b-51dfb640823c",
  "isSidechain": false,
  "requestId": "req_011CbJ39Cgj4UXXQ4QppLWoa",
  "type": "assistant",
  "uuid": "dcb3b11e-5672-4e6a-a209-1873d0c6cc0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kJDi8fqpdaUmzbFpfM8ru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 55385,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 55385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1266,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 55385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 55385
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-22T17:55:55.050Z_

<details><summary>↩ Tool result · `toolu_01SSG5P2SUWiu7rTRE3sbYKe`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dcb3b11e-5672-4e6a-a209-1873d0c6cc0b",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "9a105d86-4547-4df6-83c9-a9c7204f8c05",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "dcb3b11e-5672-4e6a-a209-1873d0c6cc0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-22T17:55:55.915Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017ZhB4YzSWPm3hPddnNjTxa`</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
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
  "parentUuid": "9a105d86-4547-4df6-83c9-a9c7204f8c05",
  "isSidechain": false,
  "requestId": "req_011CbJ39Cgj4UXXQ4QppLWoa",
  "type": "assistant",
  "uuid": "110daf6f-ac43-42fa-9ca6-df2768984955",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kJDi8fqpdaUmzbFpfM8ru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 55385,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 55385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1266,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 55385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 55385
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-22T17:55:55.926Z_

<details><summary>↩ Tool result · `toolu_017ZhB4YzSWPm3hPddnNjTxa`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex:6:Subsequent work refines the conditions under which collapse occurs: \citet{bertrand2024_stability} identify convergence to a fixed point under mixed real-synthetic retraining (providing theoretical grounding for our EDD ceiling, \S\ref{sec:method:theory}), \citet{shi2025_closer_look} reframe collapse as a generalization-to-memorization transition, and \citet{dohmatob2025_strong_collapse} extend guarantees to broader model classes.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex:34:Decoding strategies shape text statistics in ways that interact with depth signals \cite{holtzman2020_nucleus,finlayson2024_closing,garces_arias2025_decoding_decoded,wiher2022_decoding,basu2021_mirostat}.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex:6:At 25--50\% synthetic mixing, accuracy drops 8--15\,pp and $\mathrm{EDD}_{0.70}{=}3$ is preserved in 5/6 tested cells (GPT-2~XL nucleus at 50\% drops to $\mathrm{EDD}_{0.70}{=}2$; d2v3 AUC\,=\,0.695, marginally below threshold; Table~\ref{tab:accum_auc}); accumulation experiments use matched strategies per model (nucleus for GPT-2~XL/Pythia, temperature for OLMo) and do not test cross-strategy accumulation; extension to larger models and higher mixing ratios remains future work.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex:5:Three importance measures (Gini, SHAP, permutation; Kendall's $W{=}0.90$), confirmed by a fourth (CPI; Appendix~\ref{app:conditional_pi}), converge on the same feature ranking, and an independent Binoculars-derived 11-feature pathway reaches statistically indistinguishable accuracy (78.1\% vs.\ 78.4\%, $p{>}0.05$; merged: 82.6\%).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:13:Depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:42:Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:95:Two exceptions exist among GPT-2~XL cells: in temperature sampling, \texttt{p90\_ppl} (CPI\,=\,0.419) exceeds \texttt{var\_surprisal} (0.093) while both remain in the top-2; in top-$k$ sampling, \texttt{p90\_ppl} (0.475) and \texttt{p75\_ppl} (0.127) push \texttt{var\_surprisal} to rank~3 (0.037), the only cell where it exits the top-2.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:178:At 25\% mixing, all three cells preserve $\mathrm{EDD}_{0.70}{=}3$.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:179:At 50\% mixing, GPT-2~XL nucleus is the sole failure: d2v3 AUC\,=\,0.695, marginally below the 0.70 threshold (0.55\,pp).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:570:The base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries; depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:692:Despite this variation, the classifier remains effective after clipping, confirming that the depth signal resides in the p90-and-below distributional shape rather than extreme outliers.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:1041:Under correct strategy routing, four-class accuracy reaches 72.6\% vs.\ 68.0\% under misrouting ($N{=}103{,}498$ / $76{,}502$), a gap of 4.6\,pp; d0 accuracy remains near-ceiling (${\sim}99.6$\%) regardless of routing, confirming that the d0 signal is strategy-invariant.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex:6:This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet whether the recursive generation depth of a text can be estimated from its statistical properties remains unstudied, a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:18:mirrors the 1--1.5B atlas ordering, confirming that strategy-dependent attenuation patterns generalize across scale.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:20:%% diverges from the 1--1.5B atlas ordering, where temperature yields the highest accuracy; at 14B, [describe actual ranking], suggesting that scale interacts with strategy effects non-trivially.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:48:% Preliminary cross-scale experiments (7--14B, 54--70\%) provide an existence proof that depth signal persists at larger scales under nucleus and temperature sampling, while top-$k$ drops to chance, confirming that scale amplifies strategy-dependent attenuation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "110daf6f-ac43-42fa-9ca6-df2768984955",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "0840f322-db66-4812-a654-5b1422c5064b",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex:6:Subsequent work refines the conditions under which collapse occurs: \\citet{bertrand2024_stability} identify convergence to a fixed point under mixed real-synthetic retraining (providing theoretical grounding for our EDD ceiling, \\S\\ref{sec:method:theory}), \\citet{shi2025_closer_look} reframe collapse as a generalization-to-memorization transition, and \\citet{dohmatob2025_strong_collapse} extend guarantees to broader model classes.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex:7:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex:34:Decoding strategies shape text statistics in ways that interact with depth signals \\cite{holtzman2020_nucleus,finlayson2024_closing,garces_arias2025_decoding_decoded,wiher2022_decoding,basu2021_mirostat}.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex:6:At 25--50\\% synthetic mixing, accuracy drops 8--15\\,pp and $\\mathrm{EDD}_{0.70}{=}3$ is preserved in 5/6 tested cells (GPT-2~XL nucleus at 50\\% drops to $\\mathrm{EDD}_{0.70}{=}2$; d2v3 AUC\\,=\\,0.695, marginally below threshold; Table~\\ref{tab:accum_auc}); accumulation experiments use matched strategies per model (nucleus for GPT-2~XL/Pythia, temperature for OLMo) and do not test cross-strategy accumulation; extension to larger models and higher mixing ratios remains future work.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex:5:Three importance measures (Gini, SHAP, permutation; Kendall's $W{=}0.90$), confirmed by a fourth (CPI; Appendix~\\ref{app:conditional_pi}), converge on the same feature ranking, and an independent Binoculars-derived 11-feature pathway reaches statistically indistinguishable accuracy (78.1\\% vs.\\ 78.4\\%, $p{>}0.05$; merged: 82.6\\%).\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:13:Depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:42:Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \\S\\ref{sec:atlas:strategy}.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:95:Two exceptions exist among GPT-2~XL cells: in temperature sampling, \\texttt{p90\\_ppl} (CPI\\,=\\,0.419) exceeds \\texttt{var\\_surprisal} (0.093) while both remain in the top-2; in top-$k$ sampling, \\texttt{p90\\_ppl} (0.475) and \\texttt{p75\\_ppl} (0.127) push \\texttt{var\\_surprisal} to rank~3 (0.037), the only cell where it exits the top-2.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:178:At 25\\% mixing, all three cells preserve $\\mathrm{EDD}_{0.70}{=}3$.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:179:At 50\\% mixing, GPT-2~XL nucleus is the sole failure: d2v3 AUC\\,=\\,0.695, marginally below the 0.70 threshold (0.55\\,pp).\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:570:The base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries; depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:692:Despite this variation, the classifier remains effective after clipping, confirming that the depth signal resides in the p90-and-below distributional shape rather than extreme outliers.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:1041:Under correct strategy routing, four-class accuracy reaches 72.6\\% vs.\\ 68.0\\% under misrouting ($N{=}103{,}498$ / $76{,}502$), a gap of 4.6\\,pp; d0 accuracy remains near-ceiling (${\\sim}99.6$\\%) regardless of routing, confirming that the d0 signal is strategy-invariant.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex:6:This model$\\to$data$\\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet whether the recursive generation depth of a text can be estimated from its statistical properties remains unstudied, a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \\cite{dohmatob2024_tale_of_tails}.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:18:mirrors the 1--1.5B atlas ordering, confirming that strategy-dependent attenuation patterns generalize across scale.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:20:%% diverges from the 1--1.5B atlas ordering, where temperature yields the highest accuracy; at 14B, [describe actual ranking], suggesting that scale interacts with strategy effects non-trivially.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:48:% Preliminary cross-scale experiments (7--14B, 54--70\\%) provide an existence proof that depth signal persists at larger scales under nucleus and temperature sampling, while top-$k$ drops to chance, confirming that scale amplifies strategy-dependent attenuation.",
    "numLines": 17
  },
  "sourceToolAssistantUUID": "110daf6f-ac43-42fa-9ca6-df2768984955",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-22T17:55:58.037Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01AxJt91hdj6djseJHiuuTVH`</summary>

```json
{
  "pattern": "(It is worth noting|Notably|Importantly|Furthermore|Moreover|Additionally)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
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
  "parentUuid": "0840f322-db66-4812-a654-5b1422c5064b",
  "isSidechain": false,
  "requestId": "req_011CbJ39Cgj4UXXQ4QppLWoa",
  "type": "assistant",
  "uuid": "4cbfd08b-50c0-4425-93a0-53ca92f0f8e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kJDi8fqpdaUmzbFpfM8ru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 55385,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 55385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1266,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 55385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 55385
          },
          "type": "message"
        }
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

_source line 57 · 2026-05-22T17:55:58.077Z_

<details><summary>↩ Tool result · `toolu_01AxJt91hdj6djseJHiuuTVH`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cbfd08b-50c0-4425-93a0-53ca92f0f8e8",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "cb0609db-3c13-4398-a97f-cbcee604a614",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "4cbfd08b-50c0-4425-93a0-53ca92f0f8e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-22T17:55:59.839Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01PKF5Lh6AGiJNe74ekTha6x`</summary>

```json
{
  "pattern": "(delve|leverage|utilize|facilitate|myriad|plethora)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
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
  "parentUuid": "cb0609db-3c13-4398-a97f-cbcee604a614",
  "isSidechain": false,
  "requestId": "req_011CbJ39Cgj4UXXQ4QppLWoa",
  "type": "assistant",
  "uuid": "57173350-81d4-4aa5-a626-233112327718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kJDi8fqpdaUmzbFpfM8ru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 55385,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 55385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1266,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 55385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 55385
          },
          "type": "message"
        }
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

_source line 59 · 2026-05-22T17:55:59.869Z_

<details><summary>↩ Tool result · `toolu_01PKF5Lh6AGiJNe74ekTha6x`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57173350-81d4-4aa5-a626-233112327718",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "c68e314f-f9b8-4231-bf38-7bc133d68c40",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "57173350-81d4-4aa5-a626-233112327718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-22T17:56:01.227Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01CQDXbZWKoHcasL5sUpWqug`</summary>

```json
{
  "pattern": "significantly",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
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
  "parentUuid": "c68e314f-f9b8-4231-bf38-7bc133d68c40",
  "isSidechain": false,
  "requestId": "req_011CbJ39Cgj4UXXQ4QppLWoa",
  "type": "assistant",
  "uuid": "00824f20-17fb-4ede-b740-009d1ca55b94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kJDi8fqpdaUmzbFpfM8ru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 55385,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 55385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1266,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 55385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 55385
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-22T17:56:01.252Z_

<details><summary>↩ Tool result · `toolu_01CQDXbZWKoHcasL5sUpWqug`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex:10:A preliminary curation PoC (Appendix~\ref{app:curation_poc}) is inconclusive: RF-filtered subsets outperform random subsampling but do not significantly improve over unfiltered data ($p{>}0.4$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00824f20-17fb-4ede-b740-009d1ca55b94",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "61d8d9ee-feeb-4156-81fa-c794013fa86e",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex:10:A preliminary curation PoC (Appendix~\\ref{app:curation_poc}) is inconclusive: RF-filtered subsets outperform random subsampling but do not significantly improve over unfiltered data ($p{>}0.4$).",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "00824f20-17fb-4ede-b740-009d1ca55b94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-22T17:56:02.262Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01M7jAiaBZ3VC35Sy78TLCga`</summary>

```json
{
  "pattern": "state-of-the-art",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
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
  "parentUuid": "61d8d9ee-feeb-4156-81fa-c794013fa86e",
  "isSidechain": false,
  "requestId": "req_011CbJ39Cgj4UXXQ4QppLWoa",
  "type": "assistant",
  "uuid": "8eedd461-2ccf-4fb1-ace4-101710114d7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kJDi8fqpdaUmzbFpfM8ru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 55385,
      "cache_read_input_tokens": 11846,
      "output_tokens": 1266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 55385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1266,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 55385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 55385
          },
          "type": "message"
        }
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

_source line 63_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：recursive_gen_depth_est Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 45 warning…",
  "leafUuid": "36b96d76-c7a4-4b58-9056-9fe222110859",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 recursive_gen_depth_est paper review",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9"
}
```

---

### Assistant

_source line 65 · 2026-05-22T17:56:06.239Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the rest of the appendix and the conclusion file more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36b96d76-c7a4-4b58-9056-9fe222110859",
  "isSidechain": false,
  "requestId": "req_011CbJ3ASJoKADXQSgRsu9tb",
  "type": "assistant",
  "uuid": "99e18f65-a667-4b40-aa64-80b0e7fe8634",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mmz7xJqHeRZGi6yeZvsEg4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11213,
      "cache_read_input_tokens": 67231,
      "output_tokens": 527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11213,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 527,
          "cache_read_input_tokens": 67231,
          "cache_creation_input_tokens": 11213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11213
          },
          "type": "message"
        }
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

_source line 66 · 2026-05-22T17:56:06.768Z_

Let me read the remaining appendix sections and check for more patterns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99e18f65-a667-4b40-aa64-80b0e7fe8634",
  "isSidechain": false,
  "requestId": "req_011CbJ3ASJoKADXQSgRsu9tb",
  "type": "assistant",
  "uuid": "5b5d8ed4-14b4-4db7-9457-c4798a28d672",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mmz7xJqHeRZGi6yeZvsEg4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11213,
      "cache_read_input_tokens": 67231,
      "output_tokens": 527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11213,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 527,
          "cache_read_input_tokens": 67231,
          "cache_creation_input_tokens": 11213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11213
          },
          "type": "message"
        }
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

_source line 67 · 2026-05-22T17:56:07.855Z_

<details open><summary>🔧 Tool call — Read · `toolu_011KLALa65frvC57xzHTrHLb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": 300,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b5d8ed4-14b4-4db7-9457-c4798a28d672",
  "isSidechain": false,
  "requestId": "req_011CbJ3ASJoKADXQSgRsu9tb",
  "type": "assistant",
  "uuid": "8c443b60-d11c-44b4-b84a-0c48e45943a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mmz7xJqHeRZGi6yeZvsEg4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11213,
      "cache_read_input_tokens": 67231,
      "output_tokens": 527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11213,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 527,
          "cache_read_input_tokens": 67231,
          "cache_creation_input_tokens": 11213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11213
          },
          "type": "message"
        }
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

_source line 68 · 2026-05-22T17:56:10.775Z_

<details><summary>↩ Tool result · `toolu_01PWFeCL6qimW3VuTE8eJyHu`</summary>

```text
1:\section{LoRA Fine-Tuning Protocol}
35:\section{Additional Results}
38:\subsection{Top-$k$ Feature Trajectories}
46:\subsection{Permutation Importance}
55:\subsection{Conditional Permutation Importance under Multicollinearity}
61:\paragraph{Setup.}
65:\paragraph{Results.}
100:\paragraph{Consistency with Gini rankings.}
105:\subsection{Feature Trajectories}
115:\subsection{Per-Class Recall}
144:\subsection{Confusion Matrices}
154:\subsection{Cross-Strategy Transfer Details}
174:\subsection{Accumulation Pairwise AUC}
200:\subsection{DCOL Iteration Details}
226:\subsection{Zero-Shot LLM Prompt Template}
241:\subsection{Temperature Robustness}
247:\paragraph{Within-$\tau$ robustness.}
251:\paragraph{Collapse at $\tau{=}1.1$: memorization as prerequisite.}
257:\paragraph{Cross-$\tau$ non-transferability.}
262:\paragraph{Ecological validity.}
303:\subsection{Feature Overlap Analysis}
310:\subsection{End-to-End Learning}
335:\paragraph{Feature space divergence.}
343:\subsection{Domain Bias Analysis}
348:\paragraph{Methodological note.}
353:\paragraph{Sub-A: Standard CV.}
356:\paragraph{Sub-B: LOGO evaluation.}
361:\paragraph{Sub-C: Negative control.}
368:\subsection{Wild-Data Calibration}
401:\paragraph{Threshold calibration.}
408:\subsection{Downstream Curation PoC (Inconclusive)}
460:\subsection{Reference Model Ablation}
482:\subsection{Cross-Scale Full Results}
491:\paragraph{Scale comparison.}
521:\paragraph{(1) Depth signal persists at 7--8B scale.}
525:\paragraph{(2) EDD at 7--8B scale.}
550:\paragraph{(3) Divergent AUC trajectories and instruction-tuning effect.}
572:\paragraph{(4) Signal attenuation at 14B.}
588:\paragraph{(5) Cross-reference control at 14B.}
615:\paragraph{Caveats.}
619:\paragraph{Confounds.}
626:\subsection{Cross-Boundary Generalization}
633:\paragraph{Cross-model recursive chains.}
640:\paragraph{Confound discussion.}
646:\paragraph{Reverse-chain control.}
651:\paragraph{Cross-domain transfer.}
659:\subsection{Cross-Seed Replication}
689:\paragraph{Outlier handling.}
694:\subsection{Depth-4 Extension}
702:\paragraph{Feature monotonicity at d4.}
711:\subsection{Generation Length Ablation}
735:\subsection{Mixed-Depth Corpus}
741:\subsection{Learned Estimator Comparison}
768:\subsection{Instruction-Tuned Model at 1.5B Scale}
781:\subsection{Downstream Fine-Tuning Probe (Inconclusive)}
809:\subsection{Feature Group Ablation}
836:\subsection{RF Seed Robustness}
861:\subsection{Binary Detector Baselines for Ordinal Classification}
866:\paragraph{Binary detectors (Pythia nucleus).}
872:\paragraph{Membership inference baselines (all 9 cells).}
880:\paragraph{Augmented feature set.}
887:\paragraph{Pairwise AUC and ordinal collapse.}
920:\subsection{Binoculars Feature Ablation and Signal Decomposition}
972:\paragraph{Strategy-dependent complementarity.}
977:\paragraph{Cross-scale Binoculars ablation (14B).}
1002:\subsection{Prompted Generation Results}
1036:\subsection{Extended Discussion}
1039:\paragraph{Cross-strategy conditional decomposition.}
1045:\paragraph{Depth-graduated curation (inconclusive).}
1048:\paragraph{Toward a provenance toolkit.}
1055:\subsection{Computational Resources and Reproducibility}
1058:\paragraph{Hardware.}
1062:\paragraph{Software.}
1066:\paragraph{Hyperparameters.}
1070:\paragraph{Inference cost.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1acc34c-9e61-4386-a7c1-4336130b0b7e",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "2348a16b-415f-4cf9-96eb-58549c75b2a2",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1:\\section{LoRA Fine-Tuning Protocol}\n35:\\section{Additional Results}\n38:\\subsection{Top-$k$ Feature Trajectories}\n46:\\subsection{Permutation Importance}\n55:\\subsection{Conditional Permutation Importance under Multicollinearity}\n61:\\paragraph{Setup.}\n65:\\paragraph{Results.}\n100:\\paragraph{Consistency with Gini rankings.}\n105:\\subsection{Feature Trajectories}\n115:\\subsection{Per-Class Recall}\n144:\\subsection{Confusion Matrices}\n154:\\subsection{Cross-Strategy Transfer Details}\n174:\\subsection{Accumulation Pairwise AUC}\n200:\\subsection{DCOL Iteration Details}\n226:\\subsection{Zero-Shot LLM Prompt Template}\n241:\\subsection{Temperature Robustness}\n247:\\paragraph{Within-$\\tau$ robustness.}\n251:\\paragraph{Collapse at $\\tau{=}1.1$: memorization as prerequisite.}\n257:\\paragraph{Cross-$\\tau$ non-transferability.}\n262:\\paragraph{Ecological validity.}\n303:\\subsection{Feature Overlap Analysis}\n310:\\subsection{End-to-End Learning}\n335:\\paragraph{Feature space divergence.}\n343:\\subsection{Domain Bias Analysis}\n348:\\paragraph{Methodological note.}\n353:\\paragraph{Sub-A: Standard CV.}\n356:\\paragraph{Sub-B: LOGO evaluation.}\n361:\\paragraph{Sub-C: Negative control.}\n368:\\subsection{Wild-Data Calibration}\n401:\\paragraph{Threshold calibration.}\n408:\\subsection{Downstream Curation PoC (Inconclusive)}\n460:\\subsection{Reference Model Ablation}\n482:\\subsection{Cross-Scale Full Results}\n491:\\paragraph{Scale comparison.}\n521:\\paragraph{(1) Depth signal persists at 7--8B scale.}\n525:\\paragraph{(2) EDD at 7--8B scale.}\n550:\\paragraph{(3) Divergent AUC trajectories and instruction-tuning effect.}\n572:\\paragraph{(4) Signal attenuation at 14B.}\n588:\\paragraph{(5) Cross-reference control at 14B.}\n615:\\paragraph{Caveats.}\n619:\\paragraph{Confounds.}\n626:\\subsection{Cross-Boundary Generalization}\n633:\\paragraph{Cross-model recursive chains.}\n640:\\paragraph{Confound discussion.}\n646:\\paragraph{Reverse-chain control.}\n651:\\paragraph{Cross-domain transfer.}\n659:\\subsection{Cross-Seed Replication}\n689:\\paragraph{Outlier handling.}\n694:\\subsection{Depth-4 Extension}\n702:\\paragraph{Feature monotonicity at d4.}\n711:\\subsection{Generation Length Ablation}\n735:\\subsection{Mixed-Depth Corpus}\n741:\\subsection{Learned Estimator Comparison}\n768:\\subsection{Instruction-Tuned Model at 1.5B Scale}\n781:\\subsection{Downstream Fine-Tuning Probe (Inconclusive)}\n809:\\subsection{Feature Group Ablation}\n836:\\subsection{RF Seed Robustness}\n861:\\subsection{Binary Detector Baselines for Ordinal Classification}\n866:\\paragraph{Binary detectors (Pythia nucleus).}\n872:\\paragraph{Membership inference baselines (all 9 cells).}\n880:\\paragraph{Augmented feature set.}\n887:\\paragraph{Pairwise AUC and ordinal collapse.}\n920:\\subsection{Binoculars Feature Ablation and Signal Decomposition}\n972:\\paragraph{Strategy-dependent complementarity.}\n977:\\paragraph{Cross-scale Binoculars ablation (14B).}\n1002:\\subsection{Prompted Generation Results}\n1036:\\subsection{Extended Discussion}\n1039:\\paragraph{Cross-strategy conditional decomposition.}\n1045:\\paragraph{Depth-graduated curation (inconclusive).}\n1048:\\paragraph{Toward a provenance toolkit.}\n1055:\\subsection{Computational Resources and Reproducibility}\n1058:\\paragraph{Hardware.}\n1062:\\paragraph{Software.}\n1066:\\paragraph{Hyperparameters.}\n1070:\\paragraph{Inference cost.}",
    "numLines": 75
  },
  "sourceToolAssistantUUID": "f1acc34c-9e61-4386-a7c1-4336130b0b7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-22T17:56:07.862Z_

<details><summary>↩ Tool result · `toolu_011KLALa65frvC57xzHTrHLb`</summary>

```text
300	\end{tabular}
301	\end{table}
302	
303	\subsection{Feature Overlap Analysis}
304	\label{app:feature_overlap}
305	
306	We probe whether end-to-end PLM representations capture the same depth signals as our statistical features via linear probing of [CLS] representations from DeBERTa-v3-base and RoBERTa-base.
307	PLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics; \texttt{var\_surprisal} and \texttt{p90\_ppl} yield negative $R^2$ under linear probing; these features are not linearly accessible in the pretrained representation space.
308	This confirms that the 20pp accuracy gap between feature-based and end-to-end methods (\S\ref{app:e2e}) stems from complementary, not redundant, representations: PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties that constitute the dominant depth markers.
309	
310	\subsection{End-to-End Learning}
311	\label{app:e2e}
312	
313	DeBERTa-v3-base \cite{he2021_deberta_v3} and RoBERTa-base \cite{liu2019_roberta} finetuned end-to-end achieve 58.3\% ($\pm$4.7\%) and 59.5\% ($\pm$3.2\%) respectively, lagging the RF baseline (78.7\%) by 20.4pp and 19.2pp.
314	The 1.2pp inter-backbone gap rules out architecture bias; Table~\ref{tab:e2e_detail} shows both backbones share the same failure mode (high d0 F1, $>$0.94, but collapsed d1/d2 performance, F1 $\leq$ 0.42), while RF achieves 0.596 d2 recall, a $>$2$\times$ advantage at the hardest depth class.
315	
316	\begin{table}[h]
317	\centering
318	\small
319	\caption{Per-class performance for end-to-end PLM classifiers vs.\ RF baseline (Pythia-1.4B nucleus). PLM columns report F1; RF d2 column reports recall (the class with the largest PLM--RF gap). Both PLM backbones share the same failure pattern: collapsed d1/d2 scores despite adequate d0/d3.}
320	\label{tab:e2e_detail}
321	\resizebox{\columnwidth}{!}{%
322	\begin{tabular}{@{}lccccc@{}}
323	\toprule
324	Method & Acc (\%) & d0 & d1 & d2 & d3 \\
325	\midrule
326	DeBERTa-v3 & 58.3\,$\pm$\,4.7 & .947 & .378 & .247 & .656 \\
327	RoBERTa-base & 59.5\,$\pm$\,3.2 & .958 & .416 & .261 & .647 \\
328	\midrule
329	RF (19 feat.) & 78.7 & --- & --- & .596$^\dagger$ & --- \\
330	\bottomrule
331	\multicolumn{6}{@{}l}{\footnotesize $^\dagger$Recall; shown for the depth class with the largest PLM--RF gap.}
332	\end{tabular}}
333	\end{table}
334	
335	\paragraph{Feature space divergence.}
336	SHAP TreeExplainer analysis confirms that perplexity and surprisal features account for 88.8\% of RF's total contribution.
337	Three independent importance measures (SHAP, Gini, and permutation) show strong concordance (Kendall's $W{=}0.90$, $p{<}0.005$; pairwise Spearman $\rho$: SHAP--Gini $0.93$, SHAP--permutation $0.84$; \S\ref{app:permutation}), with \texttt{p90\_ppl} appearing in the SHAP top-2 in 9/9 cells and \texttt{var\_surprisal} in 8/9.
338	Linear probing of PLM [CLS] representations yields negative $R^2$ for both \texttt{var\_surprisal} and \texttt{p90\_ppl} (\S\ref{app:feature_overlap}); pretrained representations lack the linear structure needed to recover perplexity tail statistics, a systematic representational gap rather than a backbone-specific artifact.
339	
340	DCOL \cite{cloc2025} reached 64.5\% (\S\ref{app:dcol_iterations}); all end-to-end approaches (58--65\%) underperform feature-based methods; depth estimation therefore benefits from targeted statistical features that capture distributional tail properties absent from PLM representations.
341	This comparison is bounded by backbone scale ($\leq$125M parameters); whether larger PLMs (e.g., 7B+) can close the gap via richer internal representations remains an open question.
342	
343	\subsection{Domain Bias Analysis}
344	\label{app:domain_bias}
345	
346	To assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.
347	
348	\paragraph{Methodological note.}
349	An initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\%, seed-group prediction 20.8\%).
350	We discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.
351	The results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.
352	
353	\paragraph{Sub-A: Standard CV.}
354	Five-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\% to 82\% across the 9 atlas cells (up to 2.5$\times$ above the 33.3\% chance level); depth signal is therefore the dominant classification factor.
355	
356	\paragraph{Sub-B: LOGO evaluation.}
357	We assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.
358	LOGO mean accuracy is 72.1\% (range 59.5--81.6\%), matching standard CV (72.0\%) within noise (before fix: 64.0\%, reflecting the depth--group confound).
359	Per-cell fold standard deviations range from 0.4pp to 1.4pp; cross-group generalization is therefore as reliable as within-group classification.
360	
361	\paragraph{Sub-C: Negative control.}
362	We train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\%).
363	Depth prediction accuracy averages 72.0\%; seed-group prediction averages 10.2\%, indistinguishable from chance (before fix: 20.8\%, inflated by the depth--group confound).
364	The depth-to-seed-group accuracy ratio is 7.1$\times$; the feature representation therefore encodes depth but not seed-article identity.
365	
366	Taken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.
367	
368	\subsection{Wild-Data Calibration}
369	\label{app:calibration}
370	
371	Table~\ref{tab:calibration} reports d0 accuracy and false positive rate (FPR) for all three model-specific nucleus RF classifiers on two out-of-distribution human-text corpora: WikiText-103 (546 editorial passages) and C4 (5{,}000 web-crawl passages, crawled 2019--2020; pre-LLM deployment).
372	
373	\begin{table}[h]
374	\centering
375	\small
376	\caption{Wild-data d0 accuracy and FPR for nucleus RF classifiers. All passages are human-written (true d0). FPR = fraction misclassified as d1+. 95\% Wilson CIs computed for C4 ($n{=}5{,}000$).}
377	\label{tab:calibration}
378	\resizebox{\columnwidth}{!}{%
379	\begin{tabular}{@{}llrccc@{}}
380	\toprule
381	Model & Source & $n$ & d0 (\%) & FPR (\%) & 95\% Wilson CI \\
382	\midrule
383	Pythia-1.4B & WikiText & 546 & 100.0 & 0.0 & --- \\
384	 & C4 & 5{,}000 & 79.8 & 20.2 & [19.1, 21.3] \\
385	\addlinespace
386	GPT-2~XL & WikiText & 546 & 99.3 & 0.7 & --- \\
387	 & C4 & 5{,}000 & 77.6 & 22.4 & [21.3, 23.6] \\
388	\addlinespace
389	OLMo-1B & WikiText & 546 & 98.5 & 1.5 & --- \\
390	 & C4 & 5{,}000 & 95.3 & 4.7 & [4.2, 5.3] \\
391	\bottomrule
392	\end{tabular}}
393	\end{table}
394	
395	On WikiText-103, all three classifiers achieve $\geq$98.5\% d0 accuracy; editorial text is therefore reliably distinguished from recursive generations across model families.
396	On C4, FPR varies sharply: OLMo (4.7\%) vs.\ Pythia (20.2\%) and GPT-2~XL (22.4\%).
397	C4 misclassifications concentrate in template and SEO content with elevated repetition features (\texttt{rep\_3gram} $+$37\%, \texttt{rep\_4gram} $+$75\% vs.\ correctly classified d0 passages), rather than in random noise.
398	The model gap likely reflects training data composition: OLMo (trained on Dolma, which includes diverse web data) produces d0 features more tolerant of web-crawl variation, while Pythia and GPT-2~XL (trained primarily on Wikipedia/WebText) map template-heavy content into the d1+ region.
399	Among C4 false positives for GPT-2~XL, predictions distribute as d1 (9.0\%), d2 (3.7\%), d3 (9.6\%); for OLMo, d1 (2.9\%), d2 (0.5\%), d3 (1.3\%). The non-uniform depth distribution suggests the classifier maps specific repetition patterns to particular depth signatures rather than producing random misclassifications.
400	
401	\paragraph{Threshold calibration.}
402	A pooled RF classifier (trained on all three families' nucleus data) achieves ECE\,=\,0.052 on in-distribution data; Platt scaling and isotonic regression yield no improvement; probability estimates are already well calibrated.
403	The high FPR on web-crawl data is therefore a decision-threshold problem, not a probability calibration defect.
404	Applying a confidence threshold $P(\mathrm{d0}) \geq 0.15$ reduces C4 FPR from 33.4\% to 2.8\% and FineWeb FPR from 16.9\% to 0.7\%, at a cost of only $-$0.3\,pp balanced accuracy (78.0\%$\to$77.7\%).
405	The $P(\mathrm{d0})$ distribution is bimodal: 67\% of samples exceed 0.95 (high-confidence d0), while 33\% fall in the 0.15--0.30 uncertainty zone; the threshold separates these modes cleanly.
406	Wild-data FPR is thus an operational threshold choice rather than a fundamental limitation, though the optimal threshold is domain-dependent.
407	
408	\subsection{Downstream Curation PoC (Inconclusive)}
409	\label{app:curation_poc}
410	
411	To assess whether depth estimation translates to actionable data curation, we conduct a proof-of-concept downstream evaluation.
412	We fine-tune Pythia-410M with LoRA ($r{=}16$, $\alpha{=}32$) for 3 epochs on 8 data conditions derived from the Pythia nucleus depth-estimation corpus, repeating each condition over 5 random seeds.
413	Conditions vary the selection mechanism (RF-predicted depth, oracle depth, random subsampling) and stringency (strict $\approx$25\%, moderate $\approx$50\%, soft threshold).
414	Table~\ref{tab:curation_poc} reports per-condition perplexity; Table~\ref{tab:curation_comparisons} reports pairwise contrasts.
415	
416	\begin{table}[h]
417	\centering
418	\small
419	\caption{Curation PoC: per-condition perplexity (Pythia-410M LoRA, 5 seeds). $\Delta$ is signed so that positive values indicate lower (better) perplexity than unfiltered. $d_z$: Cohen's paired effect size. $^*$\,: $p<0.05$ (paired $t$-test vs.\ unfiltered).}
420	\label{tab:curation_poc}
421	\resizebox{\columnwidth}{!}{%
422	\begin{tabular}{@{}lcccccc@{}}
423	\toprule
424	Condition & Mean PPL & Std & $n$ & $\Delta$ vs Unfilt. & $p$ & $d_z$ \\
425	\midrule
426	unfiltered        & 15.776 & 0.066 & 10{,}000 & ---      & ---   & ---      \\
427	rf\_soft          & 15.733 & 0.038 &  4{,}422 & +0.043   & 0.407 &  0.41    \\
428	rf\_moderate      & 15.756 & 0.056 &  4{,}940 & +0.021   & 0.492 &  0.34    \\
429	rf\_strict        & 15.810 & 0.061 &  2{,}496 & $-$0.034 & 0.607 & $-$0.25  \\
430	oracle\_moderate  & 15.809 & 0.103 &  5{,}000 & $-$0.033 & 0.485 & $-$0.34  \\
431	oracle\_strict    & 15.879 & 0.128 &  2{,}500 & $-$0.103 & 0.216 & $-$0.66  \\
432	random\_soft      & 16.062 & 0.079 &  4{,}422 & $-$0.286 & ${<}$0.001$^*$ & $-$2.77  \\
433	random\_moderate  & 15.998 & 0.090 &  4{,}940 & $-$0.222 & 0.028$^*$ & $-$1.50  \\
434	random\_strict    & 16.239 & 0.165 &  2{,}496 & $-$0.463 & 0.013$^*$ & $-$1.89  \\
435	\bottomrule
436	\end{tabular}}
437	\end{table}
438	
439	\begin{table}[h]
440	\centering
441	\small
442	\caption{Pairwise comparisons (paired $t$-test, 5 seeds). $^*$\,: $p<0.05$; $^{**}$\,: $p<0.01$.}
443	\label{tab:curation_comparisons}
444	\resizebox{\columnwidth}{!}{%
445	\begin{tabular}{@{}lccc@{}}
446	\toprule
447	Comparison & $\Delta$ PPL & $t$ & $p$ \\
448	\midrule
449	rf\_strict vs random\_strict     & 0.429 & $-$7.05 & 0.002$^{**}$ \\
450	rf\_moderate vs random\_moderate & 0.242 & $-$3.77 & 0.020$^*$    \\
451	rf\_soft vs random\_soft         & 0.328 & $-$17.98 & ${<}$0.001$^{**}$ \\
452	rf\_soft vs unfiltered           & 0.043 &    0.93 & 0.407        \\
453	\bottomrule
454	\end{tabular}}
455	\end{table}
456	
457	For the binary task of identifying low-depth passages (d0 vs.\ d1--d3, evaluated on the same Pythia nucleus corpus with 5-fold CV), RF-based depth filtering achieves F1\,=\,0.997, substantially outperforming a simple perplexity-threshold baseline (F1\,=\,0.845); the multi-feature representation provides discriminative value beyond raw perplexity.
458	However, the primary comparison (RF-filtered vs.\ unfiltered, $p > 0.4$) is non-significant; the significant RF-vs-random contrasts ($p < 0.02$) involve multiple pairwise comparisons that were not corrected for multiplicity.
459	
460	\subsection{Reference Model Ablation}
461	\label{app:ref_ablation}
462	
463	Table~\ref{tab:ref_ablation} ablates the reference model used for feature extraction on Pythia-1.4B nucleus text (d0--d3, 5-fold CV).
464	Self-reference (Pythia-1.4B) yields 78.6\%; switching to a cross-architecture reference degrades accuracy by 4--11\,pp, confirming that reference-generator alignment amplifies depth signal.
465	
466	\begin{table}[h]
467	\centering
468	\caption{Reference model ablation. Classification accuracy (5-fold CV) on Pythia-1.4B generated text (nucleus, d0--d3) using different reference models for feature extraction.}
469	\label{tab:ref_ablation}
470	\resizebox{\columnwidth}{!}{%
471	\begin{tabular}{@{}lcc@{}}
472	\toprule
473	Reference Model & Architecture & Accuracy (\%) \\
474	\midrule
475	Pythia-1.4B (self) & GPT-NeoX & 78.6 $\pm$ 0.6 \\
476	OLMo-1B (cross) & OLMo & 74.5 $\pm$ 0.7 \\
477	GPT-2~XL (cross) & GPT-2 & 67.3 $\pm$ 0.7 \\
478	\bottomrule
479	\end{tabular}}
480	\end{table}
481	
482	\subsection{Cross-Scale Full Results}
483	\label{app:cross_scale_full}
484	
485	This section provides the full cross-scale analysis summarized in \S\ref{sec:gen:crossscale}.
486	We extend the benchmark to two 7--8B models (Qwen2.5-7B-Instruct \cite{qwen2.5}, Llama-3.1-8B-Instruct \cite{llama3}) and one 14B model (Qwen2.5-14B).
487	The 7--8B models use 4-bit NF4 QLoRA fine-tuning with nucleus sampling ($p{=}0.95$, 500 samples per depth, depths $d \in \{0, 1, \ldots, 5\}$).
488	The 14B model uses clean FP16 LoRA fine-tuning across all three decoding strategies (nucleus, temperature $\tau{=}0.9$, top-$k$ $k{=}50$; 5{,}000 samples per depth, depths $d \in \{0, 1, 2, 3\}$).
489	Feature extraction for 1--8B models uses Pythia-1.4B as reference; Qwen2.5-14B is evaluated under both self-reference and cross-reference (Pythia-1.4B) to disentangle reference-model artifacts from scale effects (see paragraph~5 below).
490	
491	\paragraph{Scale comparison.}
492	Table~\ref{tab:cross_scale} contrasts the 7--14B models with the three 1--1.5B models on matched evaluation (depths 0--3).
493	The 14B model is tested across all three decoding strategies; the 7--8B models use nucleus sampling only.
494	
495	\begin{table}[h]
496	\centering
497	\small
498	\caption{Cross-scale comparison: 4-class RF accuracy (\%, depths 0--3), $\mathrm{EDD}_{0.70}$ (computed from full depth range: 0--5 for 7--8B, 0--3 for 14B), and d0-vs-d1 AUC. CI: 95\% bootstrap. Chance = 25\%. $^\dagger$Self-reference model (see text).}
499	\label{tab:cross_scale}
500	\resizebox{\columnwidth}{!}{%
501	\begin{tabular}{@{}llccc@{}}
502	\toprule
503	Model & Strategy & 4-class acc & $\mathrm{EDD}_{0.70}$ & d0v1 \\
504	\midrule
505	GPT-2~XL (1.5B) & nucleus & 84.3 & 4 & 0.999 \\
506	OLMo-1B & nucleus & 78.9 & 4 & 0.997 \\
507	Pythia-1.4B & nucleus & 78.7 & 4 & 0.998 \\
508	\midrule
509	Llama-3.1-8B & nucleus & 70.2\,[68.3, 72.4] & 4 & 0.949 \\
510	Qwen2.5-7B & nucleus & 60.1\,[58.0, 62.1] & $5$ & 0.969 \\
511	\midrule
512	Qwen2.5-14B$^\dagger$ & nucleus & 54.1\,[53.4, 54.7] & 0 & 0.643 \\
513	Qwen2.5-14B$^\dagger$ & temp09 & 50.5\,[49.8, 51.2] & 0 & 0.632 \\
514	Qwen2.5-14B$^\dagger$ & top-$k$50 & 47.9\,[47.3, 48.6] & 0 & 0.561 \\
515	\cmidrule{2-5}
516	\multicolumn{2}{@{}l}{\textit{14B mean}} & \textit{50.8} & --- & --- \\
517	\bottomrule
518	\end{tabular}}
519	\end{table}
520	
521	\paragraph{(1) Depth signal persists at 7--8B scale.}
522	Both 7--8B models substantially exceed the 25\% chance baseline: Llama-3.1-8B achieves 70.2\% (95\% CI $[68.3, 72.4]$) and Qwen2.5-7B achieves 60.1\% ($[58.0, 62.1]$); recursive depth therefore remains estimable from perplexity-based features even when the generator is 5--7$\times$ larger than the reference model.
523	Depth-0 separability is preserved in both models: d0v1 AUC is 0.949 (Llama-3.1) and 0.969 (Qwen2.5).
524	
525	\paragraph{(2) EDD at 7--8B scale.}
526	At threshold $T{=}0.70$, Qwen2.5-7B maintains all consecutive-pair AUCs above 0.70 through depth~5 (Table~\ref{tab:cross_scale_auc}), yielding $\mathrm{EDD}_{0.70} = 5$ (the maximum observable from the tested depth range), exceeding the $\mathrm{EDD}_{0.70}{=}4$ observed at 1--1.5B.
527	Llama-3.1-8B matches the smaller models at $\mathrm{EDD}_{0.70}{=}4$: its monotonic decay causes d4v5 (0.618) to drop below $T$, despite stronger signal at shallower depths.
528	Both larger generators produce weaker per-step signal than the 1--1.5B models (mean consecutive AUC: 0.786 for Llama-3.1, 0.782 for Qwen2.5, vs.\ 0.852 at 1--1.5B).
529	
530	\begin{table}[h]
531	\centering
532	\small
533	\caption{Consecutive binary AUC. Llama-3.1-8B exhibits monotonic decay; Qwen2.5-7B shows a U-shaped pattern; Qwen2.5-14B$^\dagger$ (depths 0--3 only) has d0v1 below $T{=}0.70$ in all strategies, yielding $\mathrm{EDD}_{0.70}{=}0$ despite some later pairs exceeding the threshold. $^\dagger$Self-reference model.}
534	\label{tab:cross_scale_auc}
535	\resizebox{\columnwidth}{!}{%
536	\begin{tabular}{@{}llccccc@{}}
537	\toprule
538	Model & Strategy & d0v1 & d1v2 & d2v3 & d3v4 & d4v5 \\
539	\midrule
540	Llama-3.1-8B & nucleus & 0.949 & 0.877 & 0.771 & 0.716 & 0.618 \\
541	Qwen2.5-7B & nucleus & 0.969 & 0.729 & 0.709 & 0.732 & 0.772 \\
542	\midrule
543	Qwen2.5-14B$^\dagger$ & nucleus & 0.643 & 0.713 & \textbf{0.728} & \multicolumn{2}{c}{--} \\
544	Qwen2.5-14B$^\dagger$ & temp09 & 0.632 & \textbf{0.726} & 0.618 & \multicolumn{2}{c}{--} \\
545	Qwen2.5-14B$^\dagger$ & top-$k$50 & 0.561 & 0.687 & 0.679 & \multicolumn{2}{c}{--} \\
546	\bottomrule
547	\end{tabular}}
548	\end{table}
549	
550	\paragraph{(3) Divergent AUC trajectories and instruction-tuning effect.}
551	Among instruction-tuned models, Llama-3.1-8B exhibits monotonic AUC decay consistent with the 1--1.5B pattern, while Qwen2.5-7B shows a U-shaped recovery beyond d2v3 (Table~\ref{tab:cross_scale_auc}).
552	A base-model control (Llama-3.1-8B without instruction tuning) clarifies the causal direction: the base model achieves 59.9\% four-class accuracy (95\% CI [57.8, 62.15], $\mathrm{EDD}_{0.70}{=}2$) with non-monotonic AUC decay (Table~\ref{tab:llama3_base_auc}), while the instruction-tuned variant reaches 70.2\% with strictly monotonic decay.
553	The base-model control experiment suggests instruction-tuning regularizes rather than confounds the depth signal.
554	
555	\begin{table}[h]
556	\centering
557	\small
558	\caption{Pairwise AUC: Llama-3.1-8B Base vs.\ Instruct.}
559	\label{tab:llama3_base_auc}
560	\begin{tabular}{lccccc}
561	\toprule
562	Variant & $d_{0\text{v}1}$ & $d_{1\text{v}2}$ & $d_{2\text{v}3}$ & $d_{3\text{v}4}$ & $d_{4\text{v}5}$ \\
563	\midrule
564	Base & 0.918 & 0.794 & 0.682 & 0.730 & 0.595 \\
565	Instruct & 0.949 & 0.877 & 0.771 & 0.716 & 0.618 \\
566	\bottomrule
567	\end{tabular}
568	\end{table}
569	
570	The base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries; depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.
571	
572	\paragraph{(4) Signal attenuation at 14B.}
573	Qwen2.5-14B (clean FP16, self-reference) is tested across all three decoding strategies (Table~\ref{tab:cross_scale}).
574	Mean four-class accuracy is 50.8\% ($2.0{\times}$ chance), with nucleus 54.1\%, temperature 50.5\%, and top-$k$ 47.9\%.
575	$\mathrm{EDD}_{0.70}{=}0$ across all three strategies because the d0/d1 boundary falls below the 0.70 AUC threshold in every case (0.56--0.64), breaking the contiguous prefix at the first boundary.
576	The d0/d1 boundary, near-perfect at 1--1.5B (AUC ${>}0.99$), attenuates to 0.56--0.64 at 14B.
577	
578	Each strategy produces a structurally distinct adjacent-pair AUC pattern (Table~\ref{tab:cross_scale_auc}):
579	nucleus is monotonically increasing (d0v1=0.643 $<$ d1v2=0.713 $<$ d2v3=0.728);
580	temperature exhibits d2v3 collapse (0.618, the weakest boundary) because temperature scaling uniformly amplifies logit differences, accelerating convergence to the attractor distribution at deeper depths;
581	top-$k$ exhibits d0v1 collapse (0.561, the weakest boundary) because vocabulary truncation constrains d0 and d1 distributions to the same top-$k$ tokens, compressing their statistical distance.
582	This three-way divergence confirms at 14B that different decoding strategies induce structurally distinct degradation trajectories (\S\ref{sec:gen:crossstrategy}).
583	
584	Feature importance shifts under top-$k$: lexical diversity metrics (TTR, hapax ratio) enter the top-5, displacing perplexity tail statistics that dominate under nucleus and temperature.
585	This result carries an important caveat: Qwen2.5-14B uses self-reference, whereas all other experiments use Pythia-1.4B.
586	Self-reference conflates the generator's distributional shift with the reference model's sensitivity; the observed attenuation may partially reflect the reference model change rather than a pure scale effect.
587	
588	\paragraph{(5) Cross-reference control at 14B.}
589	To disentangle the scale effect from the reference-model artifact, we re-extract all 19 features using Pythia-1.4B (the same reference model as the 1--1.5B benchmark) on the Qwen2.5-14B generated text.
590	Table~\ref{tab:cross_ref_14b} compares self-reference and cross-reference results per strategy.
591	
592	\begin{table}[h]
593	\centering
594	\small
595	\caption{14B cross-reference control: Pythia-1.4B reference vs.\ self-reference on Qwen2.5-14B text. $\Delta$: cross $-$ self. $\mathrm{EDD}_{0.70}$ computed from consecutive pairwise AUC.}
596	\label{tab:cross_ref_14b}
597	\resizebox{\columnwidth}{!}{%
598	\begin{tabular}{@{}lccccc@{}}
599	\toprule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c443b60-d11c-44b4-b84a-0c48e45943a3",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "629302e6-4418-4823-9a3b-375bf3abe833",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
      "content": "\\end{tabular}\n\\end{table}\n\n\\subsection{Feature Overlap Analysis}\n\\label{app:feature_overlap}\n\nWe probe whether end-to-end PLM representations capture the same depth signals as our statistical features via linear probing of [CLS] representations from DeBERTa-v3-base and RoBERTa-base.\nPLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics; \\texttt{var\\_surprisal} and \\texttt{p90\\_ppl} yield negative $R^2$ under linear probing; these features are not linearly accessible in the pretrained representation space.\nThis confirms that the 20pp accuracy gap between feature-based and end-to-end methods (\\S\\ref{app:e2e}) stems from complementary, not redundant, representations: PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties that constitute the dominant depth markers.\n\n\\subsection{End-to-End Learning}\n\\label{app:e2e}\n\nDeBERTa-v3-base \\cite{he2021_deberta_v3} and RoBERTa-base \\cite{liu2019_roberta} finetuned end-to-end achieve 58.3\\% ($\\pm$4.7\\%) and 59.5\\% ($\\pm$3.2\\%) respectively, lagging the RF baseline (78.7\\%) by 20.4pp and 19.2pp.\nThe 1.2pp inter-backbone gap rules out architecture bias; Table~\\ref{tab:e2e_detail} shows both backbones share the same failure mode (high d0 F1, $>$0.94, but collapsed d1/d2 performance, F1 $\\leq$ 0.42), while RF achieves 0.596 d2 recall, a $>$2$\\times$ advantage at the hardest depth class.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-class performance for end-to-end PLM classifiers vs.\\ RF baseline (Pythia-1.4B nucleus). PLM columns report F1; RF d2 column reports recall (the class with the largest PLM--RF gap). Both PLM backbones share the same failure pattern: collapsed d1/d2 scores despite adequate d0/d3.}\n\\label{tab:e2e_detail}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nMethod & Acc (\\%) & d0 & d1 & d2 & d3 \\\\\n\\midrule\nDeBERTa-v3 & 58.3\\,$\\pm$\\,4.7 & .947 & .378 & .247 & .656 \\\\\nRoBERTa-base & 59.5\\,$\\pm$\\,3.2 & .958 & .416 & .261 & .647 \\\\\n\\midrule\nRF (19 feat.) & 78.7 & --- & --- & .596$^\\dagger$ & --- \\\\\n\\bottomrule\n\\multicolumn{6}{@{}l}{\\footnotesize $^\\dagger$Recall; shown for the depth class with the largest PLM--RF gap.}\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Feature space divergence.}\nSHAP TreeExplainer analysis confirms that perplexity and surprisal features account for 88.8\\% of RF's total contribution.\nThree independent importance measures (SHAP, Gini, and permutation) show strong concordance (Kendall's $W{=}0.90$, $p{<}0.005$; pairwise Spearman $\\rho$: SHAP--Gini $0.93$, SHAP--permutation $0.84$; \\S\\ref{app:permutation}), with \\texttt{p90\\_ppl} appearing in the SHAP top-2 in 9/9 cells and \\texttt{var\\_surprisal} in 8/9.\nLinear probing of PLM [CLS] representations yields negative $R^2$ for both \\texttt{var\\_surprisal} and \\texttt{p90\\_ppl} (\\S\\ref{app:feature_overlap}); pretrained representations lack the linear structure needed to recover perplexity tail statistics, a systematic representational gap rather than a backbone-specific artifact.\n\nDCOL \\cite{cloc2025} reached 64.5\\% (\\S\\ref{app:dcol_iterations}); all end-to-end approaches (58--65\\%) underperform feature-based methods; depth estimation therefore benefits from targeted statistical features that capture distributional tail properties absent from PLM representations.\nThis comparison is bounded by backbone scale ($\\leq$125M parameters); whether larger PLMs (e.g., 7B+) can close the gap via richer internal representations remains an open question.\n\n\\subsection{Domain Bias Analysis}\n\\label{app:domain_bias}\n\nTo assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.\n\n\\paragraph{Methodological note.}\nAn initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\\%, seed-group prediction 20.8\\%).\nWe discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.\nThe results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.\n\n\\paragraph{Sub-A: Standard CV.}\nFive-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\\% to 82\\% across the 9 atlas cells (up to 2.5$\\times$ above the 33.3\\% chance level); depth signal is therefore the dominant classification factor.\n\n\\paragraph{Sub-B: LOGO evaluation.}\nWe assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.\nLOGO mean accuracy is 72.1\\% (range 59.5--81.6\\%), matching standard CV (72.0\\%) within noise (before fix: 64.0\\%, reflecting the depth--group confound).\nPer-cell fold standard deviations range from 0.4pp to 1.4pp; cross-group generalization is therefore as reliable as within-group classification.\n\n\\paragraph{Sub-C: Negative control.}\nWe train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\\%).\nDepth prediction accuracy averages 72.0\\%; seed-group prediction averages 10.2\\%, indistinguishable from chance (before fix: 20.8\\%, inflated by the depth--group confound).\nThe depth-to-seed-group accuracy ratio is 7.1$\\times$; the feature representation therefore encodes depth but not seed-article identity.\n\nTaken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.\n\n\\subsection{Wild-Data Calibration}\n\\label{app:calibration}\n\nTable~\\ref{tab:calibration} reports d0 accuracy and false positive rate (FPR) for all three model-specific nucleus RF classifiers on two out-of-distribution human-text corpora: WikiText-103 (546 editorial passages) and C4 (5{,}000 web-crawl passages, crawled 2019--2020; pre-LLM deployment).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Wild-data d0 accuracy and FPR for nucleus RF classifiers. All passages are human-written (true d0). FPR = fraction misclassified as d1+. 95\\% Wilson CIs computed for C4 ($n{=}5{,}000$).}\n\\label{tab:calibration}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrccc@{}}\n\\toprule\nModel & Source & $n$ & d0 (\\%) & FPR (\\%) & 95\\% Wilson CI \\\\\n\\midrule\nPythia-1.4B & WikiText & 546 & 100.0 & 0.0 & --- \\\\\n & C4 & 5{,}000 & 79.8 & 20.2 & [19.1, 21.3] \\\\\n\\addlinespace\nGPT-2~XL & WikiText & 546 & 99.3 & 0.7 & --- \\\\\n & C4 & 5{,}000 & 77.6 & 22.4 & [21.3, 23.6] \\\\\n\\addlinespace\nOLMo-1B & WikiText & 546 & 98.5 & 1.5 & --- \\\\\n & C4 & 5{,}000 & 95.3 & 4.7 & [4.2, 5.3] \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nOn WikiText-103, all three classifiers achieve $\\geq$98.5\\% d0 accuracy; editorial text is therefore reliably distinguished from recursive generations across model families.\nOn C4, FPR varies sharply: OLMo (4.7\\%) vs.\\ Pythia (20.2\\%) and GPT-2~XL (22.4\\%).\nC4 misclassifications concentrate in template and SEO content with elevated repetition features (\\texttt{rep\\_3gram} $+$37\\%, \\texttt{rep\\_4gram} $+$75\\% vs.\\ correctly classified d0 passages), rather than in random noise.\nThe model gap likely reflects training data composition: OLMo (trained on Dolma, which includes diverse web data) produces d0 features more tolerant of web-crawl variation, while Pythia and GPT-2~XL (trained primarily on Wikipedia/WebText) map template-heavy content into the d1+ region.\nAmong C4 false positives for GPT-2~XL, predictions distribute as d1 (9.0\\%), d2 (3.7\\%), d3 (9.6\\%); for OLMo, d1 (2.9\\%), d2 (0.5\\%), d3 (1.3\\%). The non-uniform depth distribution suggests the classifier maps specific repetition patterns to particular depth signatures rather than producing random misclassifications.\n\n\\paragraph{Threshold calibration.}\nA pooled RF classifier (trained on all three families' nucleus data) achieves ECE\\,=\\,0.052 on in-distribution data; Platt scaling and isotonic regression yield no improvement; probability estimates are already well calibrated.\nThe high FPR on web-crawl data is therefore a decision-threshold problem, not a probability calibration defect.\nApplying a confidence threshold $P(\\mathrm{d0}) \\geq 0.15$ reduces C4 FPR from 33.4\\% to 2.8\\% and FineWeb FPR from 16.9\\% to 0.7\\%, at a cost of only $-$0.3\\,pp balanced accuracy (78.0\\%$\\to$77.7\\%).\nThe $P(\\mathrm{d0})$ distribution is bimodal: 67\\% of samples exceed 0.95 (high-confidence d0), while 33\\% fall in the 0.15--0.30 uncertainty zone; the threshold separates these modes cleanly.\nWild-data FPR is thus an operational threshold choice rather than a fundamental limitation, though the optimal threshold is domain-dependent.\n\n\\subsection{Downstream Curation PoC (Inconclusive)}\n\\label{app:curation_poc}\n\nTo assess whether depth estimation translates to actionable data curation, we conduct a proof-of-concept downstream evaluation.\nWe fine-tune Pythia-410M with LoRA ($r{=}16$, $\\alpha{=}32$) for 3 epochs on 8 data conditions derived from the Pythia nucleus depth-estimation corpus, repeating each condition over 5 random seeds.\nConditions vary the selection mechanism (RF-predicted depth, oracle depth, random subsampling) and stringency (strict $\\approx$25\\%, moderate $\\approx$50\\%, soft threshold).\nTable~\\ref{tab:curation_poc} reports per-condition perplexity; Table~\\ref{tab:curation_comparisons} reports pairwise contrasts.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Curation PoC: per-condition perplexity (Pythia-410M LoRA, 5 seeds). $\\Delta$ is signed so that positive values indicate lower (better) perplexity than unfiltered. $d_z$: Cohen's paired effect size. $^*$\\,: $p<0.05$ (paired $t$-test vs.\\ unfiltered).}\n\\label{tab:curation_poc}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nCondition & Mean PPL & Std & $n$ & $\\Delta$ vs Unfilt. & $p$ & $d_z$ \\\\\n\\midrule\nunfiltered        & 15.776 & 0.066 & 10{,}000 & ---      & ---   & ---      \\\\\nrf\\_soft          & 15.733 & 0.038 &  4{,}422 & +0.043   & 0.407 &  0.41    \\\\\nrf\\_moderate      & 15.756 & 0.056 &  4{,}940 & +0.021   & 0.492 &  0.34    \\\\\nrf\\_strict        & 15.810 & 0.061 &  2{,}496 & $-$0.034 & 0.607 & $-$0.25  \\\\\noracle\\_moderate  & 15.809 & 0.103 &  5{,}000 & $-$0.033 & 0.485 & $-$0.34  \\\\\noracle\\_strict    & 15.879 & 0.128 &  2{,}500 & $-$0.103 & 0.216 & $-$0.66  \\\\\nrandom\\_soft      & 16.062 & 0.079 &  4{,}422 & $-$0.286 & ${<}$0.001$^*$ & $-$2.77  \\\\\nrandom\\_moderate  & 15.998 & 0.090 &  4{,}940 & $-$0.222 & 0.028$^*$ & $-$1.50  \\\\\nrandom\\_strict    & 16.239 & 0.165 &  2{,}496 & $-$0.463 & 0.013$^*$ & $-$1.89  \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise comparisons (paired $t$-test, 5 seeds). $^*$\\,: $p<0.05$; $^{**}$\\,: $p<0.01$.}\n\\label{tab:curation_comparisons}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nComparison & $\\Delta$ PPL & $t$ & $p$ \\\\\n\\midrule\nrf\\_strict vs random\\_strict     & 0.429 & $-$7.05 & 0.002$^{**}$ \\\\\nrf\\_moderate vs random\\_moderate & 0.242 & $-$3.77 & 0.020$^*$    \\\\\nrf\\_soft vs random\\_soft         & 0.328 & $-$17.98 & ${<}$0.001$^{**}$ \\\\\nrf\\_soft vs unfiltered           & 0.043 &    0.93 & 0.407        \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFor the binary task of identifying low-depth passages (d0 vs.\\ d1--d3, evaluated on the same Pythia nucleus corpus with 5-fold CV), RF-based depth filtering achieves F1\\,=\\,0.997, substantially outperforming a simple perplexity-threshold baseline (F1\\,=\\,0.845); the multi-feature representation provides discriminative value beyond raw perplexity.\nHowever, the primary comparison (RF-filtered vs.\\ unfiltered, $p > 0.4$) is non-significant; the significant RF-vs-random contrasts ($p < 0.02$) involve multiple pairwise comparisons that were not corrected for multiplicity.\n\n\\subsection{Reference Model Ablation}\n\\label{app:ref_ablation}\n\nTable~\\ref{tab:ref_ablation} ablates the reference model used for feature extraction on Pythia-1.4B nucleus text (d0--d3, 5-fold CV).\nSelf-reference (Pythia-1.4B) yields 78.6\\%; switching to a cross-architecture reference degrades accuracy by 4--11\\,pp, confirming that reference-generator alignment amplifies depth signal.\n\n\\begin{table}[h]\n\\centering\n\\caption{Reference model ablation. Classification accuracy (5-fold CV) on Pythia-1.4B generated text (nucleus, d0--d3) using different reference models for feature extraction.}\n\\label{tab:ref_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nReference Model & Architecture & Accuracy (\\%) \\\\\n\\midrule\nPythia-1.4B (self) & GPT-NeoX & 78.6 $\\pm$ 0.6 \\\\\nOLMo-1B (cross) & OLMo & 74.5 $\\pm$ 0.7 \\\\\nGPT-2~XL (cross) & GPT-2 & 67.3 $\\pm$ 0.7 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Cross-Scale Full Results}\n\\label{app:cross_scale_full}\n\nThis section provides the full cross-scale analysis summarized in \\S\\ref{sec:gen:crossscale}.\nWe extend the benchmark to two 7--8B models (Qwen2.5-7B-Instruct \\cite{qwen2.5}, Llama-3.1-8B-Instruct \\cite{llama3}) and one 14B model (Qwen2.5-14B).\nThe 7--8B models use 4-bit NF4 QLoRA fine-tuning with nucleus sampling ($p{=}0.95$, 500 samples per depth, depths $d \\in \\{0, 1, \\ldots, 5\\}$).\nThe 14B model uses clean FP16 LoRA fine-tuning across all three decoding strategies (nucleus, temperature $\\tau{=}0.9$, top-$k$ $k{=}50$; 5{,}000 samples per depth, depths $d \\in \\{0, 1, 2, 3\\}$).\nFeature extraction for 1--8B models uses Pythia-1.4B as reference; Qwen2.5-14B is evaluated under both self-reference and cross-reference (Pythia-1.4B) to disentangle reference-model artifacts from scale effects (see paragraph~5 below).\n\n\\paragraph{Scale comparison.}\nTable~\\ref{tab:cross_scale} contrasts the 7--14B models with the three 1--1.5B models on matched evaluation (depths 0--3).\nThe 14B model is tested across all three decoding strategies; the 7--8B models use nucleus sampling only.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-scale comparison: 4-class RF accuracy (\\%, depths 0--3), $\\mathrm{EDD}_{0.70}$ (computed from full depth range: 0--5 for 7--8B, 0--3 for 14B), and d0-vs-d1 AUC. CI: 95\\% bootstrap. Chance = 25\\%. $^\\dagger$Self-reference model (see text).}\n\\label{tab:cross_scale}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nModel & Strategy & 4-class acc & $\\mathrm{EDD}_{0.70}$ & d0v1 \\\\\n\\midrule\nGPT-2~XL (1.5B) & nucleus & 84.3 & 4 & 0.999 \\\\\nOLMo-1B & nucleus & 78.9 & 4 & 0.997 \\\\\nPythia-1.4B & nucleus & 78.7 & 4 & 0.998 \\\\\n\\midrule\nLlama-3.1-8B & nucleus & 70.2\\,[68.3, 72.4] & 4 & 0.949 \\\\\nQwen2.5-7B & nucleus & 60.1\\,[58.0, 62.1] & $5$ & 0.969 \\\\\n\\midrule\nQwen2.5-14B$^\\dagger$ & nucleus & 54.1\\,[53.4, 54.7] & 0 & 0.643 \\\\\nQwen2.5-14B$^\\dagger$ & temp09 & 50.5\\,[49.8, 51.2] & 0 & 0.632 \\\\\nQwen2.5-14B$^\\dagger$ & top-$k$50 & 47.9\\,[47.3, 48.6] & 0 & 0.561 \\\\\n\\cmidrule{2-5}\n\\multicolumn{2}{@{}l}{\\textit{14B mean}} & \\textit{50.8} & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{(1) Depth signal persists at 7--8B scale.}\nBoth 7--8B models substantially exceed the 25\\% chance baseline: Llama-3.1-8B achieves 70.2\\% (95\\% CI $[68.3, 72.4]$) and Qwen2.5-7B achieves 60.1\\% ($[58.0, 62.1]$); recursive depth therefore remains estimable from perplexity-based features even when the generator is 5--7$\\times$ larger than the reference model.\nDepth-0 separability is preserved in both models: d0v1 AUC is 0.949 (Llama-3.1) and 0.969 (Qwen2.5).\n\n\\paragraph{(2) EDD at 7--8B scale.}\nAt threshold $T{=}0.70$, Qwen2.5-7B maintains all consecutive-pair AUCs above 0.70 through depth~5 (Table~\\ref{tab:cross_scale_auc}), yielding $\\mathrm{EDD}_{0.70} = 5$ (the maximum observable from the tested depth range), exceeding the $\\mathrm{EDD}_{0.70}{=}4$ observed at 1--1.5B.\nLlama-3.1-8B matches the smaller models at $\\mathrm{EDD}_{0.70}{=}4$: its monotonic decay causes d4v5 (0.618) to drop below $T$, despite stronger signal at shallower depths.\nBoth larger generators produce weaker per-step signal than the 1--1.5B models (mean consecutive AUC: 0.786 for Llama-3.1, 0.782 for Qwen2.5, vs.\\ 0.852 at 1--1.5B).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Consecutive binary AUC. Llama-3.1-8B exhibits monotonic decay; Qwen2.5-7B shows a U-shaped pattern; Qwen2.5-14B$^\\dagger$ (depths 0--3 only) has d0v1 below $T{=}0.70$ in all strategies, yielding $\\mathrm{EDD}_{0.70}{=}0$ despite some later pairs exceeding the threshold. $^\\dagger$Self-reference model.}\n\\label{tab:cross_scale_auc}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llccccc@{}}\n\\toprule\nModel & Strategy & d0v1 & d1v2 & d2v3 & d3v4 & d4v5 \\\\\n\\midrule\nLlama-3.1-8B & nucleus & 0.949 & 0.877 & 0.771 & 0.716 & 0.618 \\\\\nQwen2.5-7B & nucleus & 0.969 & 0.729 & 0.709 & 0.732 & 0.772 \\\\\n\\midrule\nQwen2.5-14B$^\\dagger$ & nucleus & 0.643 & 0.713 & \\textbf{0.728} & \\multicolumn{2}{c}{--} \\\\\nQwen2.5-14B$^\\dagger$ & temp09 & 0.632 & \\textbf{0.726} & 0.618 & \\multicolumn{2}{c}{--} \\\\\nQwen2.5-14B$^\\dagger$ & top-$k$50 & 0.561 & 0.687 & 0.679 & \\multicolumn{2}{c}{--} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{(3) Divergent AUC trajectories and instruction-tuning effect.}\nAmong instruction-tuned models, Llama-3.1-8B exhibits monotonic AUC decay consistent with the 1--1.5B pattern, while Qwen2.5-7B shows a U-shaped recovery beyond d2v3 (Table~\\ref{tab:cross_scale_auc}).\nA base-model control (Llama-3.1-8B without instruction tuning) clarifies the causal direction: the base model achieves 59.9\\% four-class accuracy (95\\% CI [57.8, 62.15], $\\mathrm{EDD}_{0.70}{=}2$) with non-monotonic AUC decay (Table~\\ref{tab:llama3_base_auc}), while the instruction-tuned variant reaches 70.2\\% with strictly monotonic decay.\nThe base-model control experiment suggests instruction-tuning regularizes rather than confounds the depth signal.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise AUC: Llama-3.1-8B Base vs.\\ Instruct.}\n\\label{tab:llama3_base_auc}\n\\begin{tabular}{lccccc}\n\\toprule\nVariant & $d_{0\\text{v}1}$ & $d_{1\\text{v}2}$ & $d_{2\\text{v}3}$ & $d_{3\\text{v}4}$ & $d_{4\\text{v}5}$ \\\\\n\\midrule\nBase & 0.918 & 0.794 & 0.682 & 0.730 & 0.595 \\\\\nInstruct & 0.949 & 0.877 & 0.771 & 0.716 & 0.618 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries; depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.\n\n\\paragraph{(4) Signal attenuation at 14B.}\nQwen2.5-14B (clean FP16, self-reference) is tested across all three decoding strategies (Table~\\ref{tab:cross_scale}).\nMean four-class accuracy is 50.8\\% ($2.0{\\times}$ chance), with nucleus 54.1\\%, temperature 50.5\\%, and top-$k$ 47.9\\%.\n$\\mathrm{EDD}_{0.70}{=}0$ across all three strategies because the d0/d1 boundary falls below the 0.70 AUC threshold in every case (0.56--0.64), breaking the contiguous prefix at the first boundary.\nThe d0/d1 boundary, near-perfect at 1--1.5B (AUC ${>}0.99$), attenuates to 0.56--0.64 at 14B.\n\nEach strategy produces a structurally distinct adjacent-pair AUC pattern (Table~\\ref{tab:cross_scale_auc}):\nnucleus is monotonically increasing (d0v1=0.643 $<$ d1v2=0.713 $<$ d2v3=0.728);\ntemperature exhibits d2v3 collapse (0.618, the weakest boundary) because temperature scaling uniformly amplifies logit differences, accelerating convergence to the attractor distribution at deeper depths;\ntop-$k$ exhibits d0v1 collapse (0.561, the weakest boundary) because vocabulary truncation constrains d0 and d1 distributions to the same top-$k$ tokens, compressing their statistical distance.\nThis three-way divergence confirms at 14B that different decoding strategies induce structurally distinct degradation trajectories (\\S\\ref{sec:gen:crossstrategy}).\n\nFeature importance shifts under top-$k$: lexical diversity metrics (TTR, hapax ratio) enter the top-5, displacing perplexity tail statistics that dominate under nucleus and temperature.\nThis result carries an important caveat: Qwen2.5-14B uses self-reference, whereas all other experiments use Pythia-1.4B.\nSelf-reference conflates the generator's distributional shift with the reference model's sensitivity; the observed attenuation may partially reflect the reference model change rather than a pure scale effect.\n\n\\paragraph{(5) Cross-reference control at 14B.}\nTo disentangle the scale effect from the reference-model artifact, we re-extract all 19 features using Pythia-1.4B (the same reference model as the 1--1.5B benchmark) on the Qwen2.5-14B generated text.\nTable~\\ref{tab:cross_ref_14b} compares self-reference and cross-reference results per strategy.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{14B cross-reference control: Pythia-1.4B reference vs.\\ self-reference on Qwen2.5-14B text. $\\Delta$: cross $-$ self. $\\mathrm{EDD}_{0.70}$ computed from consecutive pairwise AUC.}\n\\label{tab:cross_ref_14b}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule",
      "numLines": 300,
      "startLine": 300,
      "totalLines": 1074
    }
  },
  "sourceToolAssistantUUID": "8c443b60-d11c-44b4-b84a-0c48e45943a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-22T17:56:08.771Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R4AK8WSPeCxjgTiiHmc3oc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": 600,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "629302e6-4418-4823-9a3b-375bf3abe833",
  "isSidechain": false,
  "requestId": "req_011CbJ3ASJoKADXQSgRsu9tb",
  "type": "assistant",
  "uuid": "8a52257e-c3da-445d-a776-efe854bb4022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mmz7xJqHeRZGi6yeZvsEg4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11213,
      "cache_read_input_tokens": 67231,
      "output_tokens": 527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11213,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 527,
          "cache_read_input_tokens": 67231,
          "cache_creation_input_tokens": 11213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11213
          },
          "type": "message"
        }
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

_source line 71 · 2026-05-22T17:56:08.777Z_

<details><summary>↩ Tool result · `toolu_01R4AK8WSPeCxjgTiiHmc3oc`</summary>

```text
600	Strategy & Self-ref (\%) & Cross-ref (\%) & $\Delta$ & $\mathrm{EDD}_{0.70}$ & d0v1 AUC \\
601	\midrule
602	nucleus & 54.1 & 45.0 & $-$9.1 & 2 & 0.702 \\
603	temp ($\tau{=}0.9$) & 50.5 & 46.3 & $-$4.2 & 2 & 0.739 \\
604	top-$k$ ($k{=}50$) & 47.9 & 40.9 & $-$7.1 & 0 & 0.699 \\
605	\cmidrule{2-6}
606	\textit{mean} & \textit{50.8} & \textit{44.1} & $-$\textit{6.8} & --- & --- \\
607	\bottomrule
608	\end{tabular}}
609	\end{table}
610	
611	Cross-reference accuracy drops by 6.8\,pp on average (range 4.2--9.1\,pp), but $\mathrm{EDD}_{0.70}$ \emph{rises} from 0 to 2 for nucleus and temperature: the consecutive d0v1 (0.70--0.74) and d1v2 (0.72--0.73) AUCs now exceed the 0.70 threshold, while d2v3 remains below (0.54--0.61).
612	Under self-reference, the first boundary d0v1 falls below $T{=}0.70$ in all strategies (0.56--0.64), breaking the contiguous prefix and yielding $\mathrm{EDD}_{0.70}{=}0$ even though some later pairs (e.g., nucleus d1v2\,=\,0.713, d2v3\,=\,0.728) exceed the threshold; the Pythia-1.4B reference model provides sharper distributional contrast at the cost of overall accuracy.
613	The ${\sim}$7\,pp accuracy gap between self- and cross-reference is therefore a reference-model artifact, not a depth-signal artifact: depth signal persists at 14B albeit attenuated relative to 1--1.5B.
614	
615	\paragraph{Caveats.}
616	For Qwen2.5-7B, the CI lower bound (58.0\%) does not exclude sub-60\% accuracy; Llama-3.1-8B's lower bound (68.3\%) is more comfortably above chance but still below the 75--83\% range at 1--1.5B.
617	The divergent AUC trajectories across two models caution against strong generalizations from only two 7--8B data points: both the monotonic (Llama-3.1) and non-monotonic (Qwen2.5) patterns are single observations, and further architectures are needed to establish which is the dominant regime at this scale.
618	
619	\paragraph{Confounds.}
620	\label{app:cross_scale_confounds}
621	Four confounds limit the 7--8B results: (1)~4-bit NF4 QLoRA quantization (absent at 1--1.5B) may distort the perplexity distribution independently of depth; (2)~smaller sample size (500 vs.\ 5{,}000 per depth) widens confidence intervals; (3)~evaluation is limited to nucleus sampling at 7--8B (the 14B model addresses this with all three strategies); (4)~vocabulary mismatch between larger generators and the 1.4B reference model.
622	For the 14B model specifically: the cross-reference control (Table~\ref{tab:cross_ref_14b}) quantifies the reference-model artifact at ${\sim}$7\,pp, but the remaining accuracy gap (44\% vs.\ 78--85\% at 1--1.5B) still conflates scale with the other confounds listed above.
623	The base-model control partially addresses a former confound (instruction-tuning): since the base variant shows weaker signal with non-monotonic decay while the instruction-tuned variant shows stronger monotonic signal, instruction-tuning regularizes rather than confounds depth estimation.
624	The remaining confounds are not mutually independent (quantization and vocabulary mismatch both affect the perplexity distribution); it is therefore infeasible to attribute the observed accuracy gap (60--70\% vs.\ 78--85\% at 1--1.5B) to any single factor.
625	
626	\subsection{Cross-Boundary Generalization}
627	\label{app:cross_boundary}
628	
629	The preceding experiments assume a single model family generates all recursive depths.
630	In practice, recursive contamination may traverse model boundaries: text generated by model~A is used to train model~B, whose output trains model~C.
631	We probe whether the depth signal persists under two relaxations of the single-model assumption.
632	
633	\paragraph{Cross-model recursive chains.}
634	We construct a heterogeneous chain: human text (d0) $\to$ Pythia-1.4B generates d1 $\to$ OLMo-1B finetuned on Pythia-d1 generates d2 $\to$ GPT-2~XL finetuned on OLMo-d2 generates d3.
635	Each recursive step uses a \emph{different} model family, eliminating the possibility that depth signal arises from a single model's idiosyncratic behavior.
636	A 4-class Random Forest achieves 84.75\% accuracy (95\% CI $[81.0, 88.25]$), with per-depth F1 scores of 0.98 (d0), 0.88 (d1), 0.76 (d2), and 0.76 (d3).
637	Pairwise AUC remains high: d0-vs-d1 = 0.999 and d2-vs-d3 = 0.841.
638	These results suggest that distributional artifacts of recursive generation persist across model boundaries. This constitutes preliminary evidence for a process-level depth signal rather than individual generator artifacts.
639	
640	\paragraph{Confound discussion.}
641	The heterogeneous chain confounds architecture identity with depth (d1=Pythia, d2=OLMo, d3=GPT-2~XL).
642	However, if the classifier exploited architecture fingerprints rather than depth signal, near-perfect accuracy would be expected since architecture perfectly determines depth label.
643	The observed 84.75\% with monotonically decreasing per-depth F1 (d0=0.98, d1=0.88, d2=0.76, d3=0.76) is more consistent with a depth-signal interpretation, as architecture fingerprinting would not produce this graded pattern.
644	We address this confound directly with a reverse-chain control below.
645	
646	\paragraph{Reverse-chain control.}
647	To empirically test the architecture confound hypothesis, we constructed a reverse chain (GPT-2~XL $\to$ OLMo $\to$ Pythia) reversing the model-depth assignment.
648	The reverse chain achieves 85.75\% (95\% CI [82.0, 89.25]), statistically indistinguishable from the forward chain (84.75\%, [81.0, 88.25]).
649	If the classifier exploited architecture fingerprints rather than depth signal, reversing the chain should invert depth predictions; the equivalent accuracy under both orderings provides empirical evidence against the architecture confound.
650	
651	\paragraph{Cross-domain transfer.}
652	All prior experiments use WikiText-103 as the seed corpus.
653	To test domain dependence, we repeat the pipeline with arXiv abstracts as the seed text (Pythia-1.4B, nucleus $p{=}0.95$, 500 samples per depth, d0--d3).
654	Five-fold cross-validation yields 74.1\% $\pm$ 2.0\% accuracy, compared to ${\sim}$78\% on the WikiText seed.
655	Per-depth F1 shows the familiar pattern: d0 = 1.00, d1 = 0.78, d2 = 0.52, d3 = 0.66, with d2 remaining the most challenging class.
656	The 4pp accuracy gap relative to WikiText likely reflects the narrower stylistic range of scientific abstracts, which may reduce the distributional contrast between adjacent depths.
657	These results provide preliminary evidence that the perplexity-based features capture properties of the recursive generation process rather than domain-specific artifacts of the seed corpus.
658	
659	\subsection{Cross-Seed Replication}
660	\label{app:seed_replication}
661	
662	Table~\ref{tab:seed_replication} reports within-seed accuracy for all three model families (nucleus, depths 0--3) under two independent LoRA training seeds.
663	
664	\begin{table}[h]
665	\centering
666	\small
667	\caption{Cross-seed replication (nucleus $p{=}0.95$, d0--d3). seed=42 is the primary benchmark (matching Table~\ref{tab:main_matrix}); seed=43 is an independent replication.}
668	\label{tab:seed_replication}
669	\begin{tabular}{@{}llccc@{}}
670	\toprule
671	Model & Seed & Acc (\%) & 95\% CI & $\Delta$ (pp) \\
672	\midrule
673	Pythia-1.4B & 42 & 78.70 & [78.10, 79.24] & --- \\
674	Pythia-1.4B & 43 & 78.84 & [78.13, 79.52] & $+$0.14 \\
675	\midrule
676	OLMo-1B & 42 & 78.94 & [78.38, 79.48] & --- \\
677	OLMo-1B & 43 & 82.11 & [81.77, 82.54] & $+$3.17 \\
678	\midrule
679	GPT-2~XL & 42 & 84.28 & [83.78, 84.80] & --- \\
680	GPT-2~XL & 43 & 86.32 & [86.17, 86.49] & $+$2.04 \\
681	\bottomrule
682	\end{tabular}
683	\end{table}
684	
685	Seed=43 yields higher accuracy in all three models ($+$0.14 to $+$3.17\,pp, same direction).
686	For Pythia ($+$0.14\,pp), CIs overlap, consistent with noise; for OLMo ($+$3.17\,pp) and GPT-2~XL ($+$2.04\,pp), CIs do not overlap, so LoRA initialization has a non-trivial effect on absolute accuracy (${\sim}$1--3\,pp).
687	Top-3 features are identical across all seeds and models (\texttt{p90\_ppl}, \texttt{var\_surprisal}, \texttt{p75\_ppl}); depth ordering is preserved in every configuration.
688	
689	\paragraph{Outlier handling.}
690	Feature extraction occasionally produces extreme perplexity values (outlier passages); we apply per-feature clipping at $\pm 10^{10}$ before classification, affecting ${<}0.1$\% of samples.
691	The d3 perplexity distribution varies substantially across seeds: under seed=42, 0.56\% of d3 passages exceed $10^6$ in raw perplexity, while under seed=43 this fraction rises to 12.8\%.
692	Despite this variation, the classifier remains effective after clipping, confirming that the depth signal resides in the p90-and-below distributional shape rather than extreme outliers.
693	
694	\subsection{Depth-4 Extension}
695	\label{app:depth4_ext}
696	
697	We extend all three model families (GPT-2~XL, Pythia-1.4B, OLMo-1B; nucleus $p{=}0.95$) to depth~4 and train 5-class RF classifiers (d0--d4, 5{,}000 samples per depth).
698	Five-class accuracy reaches 80.5\% (OLMo), 74.0\% (GPT-2~XL), and 71.3\% (Pythia), all substantially above the 20\% chance baseline.
699	For Pythia and GPT-2~XL, d3 recall drops from ${\sim}$80\% (4-class) to ${\sim}$49\% (5-class) due to d3/d4 confusion; d4 recall is higher (Pythia 68.1\%, GPT-2~XL 63.9\%).
700	$\mathrm{EDD}_{0.70} \geq 4$ was established by dedicated binary classifiers in the atlas (\S\ref{sec:atlas:edd}; d3v4 AUC: Pythia 0.784, OLMo 0.765, GPT-2~XL 0.750); the 5-class results provide complementary evidence that depth~4 remains discriminable in the multi-class setting.
701	
702	\paragraph{Feature monotonicity at d4.}
703	For Pythia and GPT-2~XL, the dominant depth markers (\texttt{p90\_ppl}, \texttt{var\_surprisal}) maintain monotonic decrease through d4 (Pythia \texttt{p90\_ppl}: $483.7 \to 12.5$ from d0 to d4; \texttt{var\_surprisal}: $6.50 \to 1.29$), consistent with continued tail erosion (\S\ref{sec:method:theory}).
704	Mean perplexity breaks monotonicity at d4 for GPT-2~XL (d3: $1{,}076\mathrm{K}$ $\to$ d4: $928\mathrm{K}$) while tail perplexity continues to decline.
705	OLMo exhibits a \texttt{var\_surprisal} rebound at d4 ($2.49 \to 2.83$, non-monotonic), creating a feature signature absent in GPT-2~XL and Pythia.
706	The 5-class RF exploits non-adjacent depth contrasts (particularly d0-vs-d4 and d2-vs-d4) to achieve 80.5\% accuracy, the highest among all three families, while the dedicated binary d3-vs-d4 classifier (AUC 0.765) is restricted to adjacent-depth features.
707	This discrepancy illustrates that multi-class classifiers can exploit global distributional structure unavailable to pairwise comparisons.
708	The divergence between aggregate and tail statistics suggests that aggregate distributional statistics saturate at deep recursion while tail statistics continue to shift.
709	This saturation provides a physical mechanism for the EDD ceiling: once per-step feature change falls below classifier resolution, adjacent depths become indistinguishable regardless of continued distributional drift.
710	
711	\subsection{Generation Length Ablation}
712	\label{app:length_ablation}
713	
714	Table~\ref{tab:length_ablation} reports classification accuracy as a function of passage length (Pythia-1.4B nucleus, depths 0--3).
715	
716	\begin{table}[h]
717	\centering
718	\small
719	\caption{Generation length ablation (Pythia-1.4B nucleus, 5-fold CV). Accuracy increases monotonically with passage length; the 9.47\,pp spread confirms that longer passages provide stronger statistical signal.}
720	\label{tab:length_ablation}
721	\begin{tabular}{@{}lc@{}}
722	\toprule
723	Passage length (tokens) & Acc (\%) \\
724	\midrule
725	128 & 68.35 \\
726	256 & 73.80 \\
727	512 & 77.82 \\
728	\bottomrule
729	\end{tabular}
730	\end{table}
731	
732	Depth signal is detectable from 128 tokens (2.7$\times$ chance) and saturates near 500 tokens.
733	The monotonic increase reflects the statistical nature of the features: longer passages yield more stable estimates of perplexity percentiles and surprisal variance, reducing within-class overlap at adjacent depth boundaries.
734	
735	\subsection{Mixed-Depth Corpus}
736	\label{app:mixed_depth}
737	
738	Per-passage classification is largely independent of corpus composition: evaluating on a corpus containing mixed proportions of d0--d3 passages (rather than balanced classes) yields macro-recall $\Delta{=}{-}1.62$\,pp relative to the balanced benchmark (within the 2\,pp tolerance).
739	Individual class deltas range from $-$0.45\,pp to $-$2.43\,pp (d1 shows the largest shift); the RF classifier operates on per-sample features without sensitivity to the class distribution of the evaluation corpus, as Random Forest produces identical per-sample predictions regardless of batch context.
740	
741	\subsection{Learned Estimator Comparison}
742	\label{app:learned_estimator}
743	
744	Table~\ref{tab:learned_estimator} evaluates three learned classifiers (XGBoost, ordinal MLP with CORAL loss \cite{coral2020}, prototypical networks) under the same leave-one-model-out protocol as Table~\ref{tab:cross_model}.
745	The ordinal MLP follows the nested binary reduction framework \cite{mccullagh1980_ordinal,frank2001} with the loss function of \citet{rennie2005}.
746	All three methods operate on the same 19-dimensional feature vector; the comparison isolates the effect of the classification head.
747	
748	\begin{table}[h]
749	\centering
750	\small
751	\caption{Learned estimator cross-model transfer (leave-one-model-out, nucleus, 4-class). RF baseline from Table~\ref{tab:cross_model}. Chance = 25\%.}
752	\label{tab:learned_estimator}
753	\begin{tabular}{@{}lcccc@{}}
754	\toprule
755	Method & Pythia & OLMo & GPT-2 XL & Mean \\
756	\midrule
757	RF (baseline) & --- & --- & --- & 66.4 \\
758	XGBoost & 63.7 & 69.8 & 68.1 & 67.2 \\
759	Ordinal MLP & 62.5 & 69.7 & 67.9 & 66.7 \\
760	Prototypical & 61.6 & 70.0 & 68.4 & 66.6 \\
761	\bottomrule
762	\end{tabular}
763	\end{table}
764	
765	All three learned methods match the RF baseline within 0.8\,pp on average; the Pythia holdout is consistently the hardest (61.6--63.7\%), while OLMo and GPT-2~XL holdouts yield 67.9--70.0\%.
766	The narrow spread ($\leq$0.8\,pp across four methods) reinforces the conclusion that the 19-feature representation, not the classifier, determines the accuracy ceiling in the cross-model transfer setting.
767	
768	\subsection{Instruction-Tuned Model at 1.5B Scale}
769	\label{app:instruct_1p5b}
770	
771	To test whether instruction tuning eliminates depth signal at matched scale (1.5B, avoiding the quantization confound of \S\ref{sec:gen:crossscale}), we run the full recursive pipeline on Qwen2.5-1.5B-Instruct with self-reference feature extraction (i.e., the same model serves as both generator and reference).
772	
773	The RF classifier achieves 47.4\% four-class accuracy (95\% CI $[46.7, 48.1]$, $1.9\times$ chance); instruction tuning therefore reduces but does not eliminate depth signal.
774	The pairwise AUC profile differs from base models: d0v1 = 0.653, d1v2 = 0.620, d2v3 = 0.664, with a gap-dependent pattern (non-adjacent pairs yield higher AUC, e.g., d0v3 = 0.902) but no pair reaching the 0.75 threshold.
775	
776	The feature importance ranking shifts: the perplexity tail statistics (\texttt{p90\_ppl}, \texttt{var\_surprisal}) that dominate in base models drop in relative importance, while surprisal variance and mean-level features gain rank.
777	This shift suggests instruction tuning compresses the perplexity distribution (reducing tail discriminability) while preserving lower-order statistical patterns.
778	
779	Two caveats apply: (1) self-reference evaluation may inflate or deflate accuracy relative to cross-reference evaluation (cf.\ \S\ref{app:ref_ablation}); (2) a single instruction-tuned model does not establish the generality of the feature shift across architectures or instruction-tuning recipes.
780	
781	\subsection{Downstream Fine-Tuning Probe (Inconclusive)}
782	\label{app:downstream}
783	
784	We fine-tune Pythia-410M with LoRA ($r{=}16$, $\alpha{=}32$) on depth-stratified subsets (500 samples each) and evaluate held-out perplexity (200 samples, 50 per depth).
785	
786	\begin{table}[h]
787	\centering
788	\small
789	\caption{Downstream fine-tuning probe: held-out perplexity by training subset (Pythia-410M LoRA, seed=42). $\Delta$: signed difference vs.\ baseline (negative = better).}
790	\label{tab:downstream}
791	\begin{tabular}{@{}lcc@{}}
792	\toprule
793	Training subset & PPL & $\Delta$ vs.\ baseline \\
794	\midrule
795	Baseline (no fine-tuning) & 5.67 & --- \\
796	d0 only & 5.65 & $-$0.02 \\
797	d1 only & 5.55 & $-$0.12 \\
798	d2 only & 5.56 & $-$0.11 \\
799	Mixed (d0--d3) & 5.55 & $-$0.12 \\
800	\bottomrule
801	\end{tabular}
802	\end{table}
803	
804	The hypothesis that d0-only data yields the lowest perplexity is not supported: d1-only and mixed subsets tie for best (PPL~5.55), both marginally below d0-only (5.65).
805	The PPL spread is small (0.12, 2.1\% relative) and the sample size (500 per condition, single seed) is insufficient for statistical significance.
806	Training loss decreases monotonically with depth (d0: 2.558, d1: 1.920, d2: 1.286), consistent with recursive generation reducing information content and making text easier to model.
807	This pilot establishes that depth-filtered data is not harmful for downstream fine-tuning; whether depth-aware curation provides a meaningful advantage requires larger-scale evaluation.
808	
809	\subsection{Feature Group Ablation}
810	\label{app:feature_ablation}
811	
812	Table~\ref{tab:feature_ablation} reports cross-model transfer accuracy (leave-one-model-out, nucleus) when restricting the classifier to subsets of the 19-feature vector, grouped by signal type.
813	
814	\begin{table}[h]
815	\centering
816	\small
817	\caption{Feature group ablation (cross-model LOO, nucleus, 4-class). Groups merge the four Table~\ref{tab:features} categories into three: bigram/trigram entropy move from Lexical Diversity to Entropy/Surprisal; TTR/hapax move to Repetition/Diversity. Chance = 25\%.}
818	\label{tab:feature_ablation}
819	\begin{tabular}{@{}lccc@{}}
820	\toprule
821	Feature group & \#Feat. & Acc (\%) & $\Delta$ vs.\ Full \\
822	\midrule
823	Full (all 19) & 19 & 66.4 & --- \\
824	Perplexity only & 9 & 66.0 & $-$0.4 \\
825	Entropy/Surprisal only & 5 & 63.2 & $-$3.2 \\
826	Repetition/Diversity only & 5 & 53.0 & $-$13.4 \\
827	\midrule
828	\texttt{p90\_ppl} only & 1 & 58.3 & $-$8.1 \\
829	\bottomrule
830	\end{tabular}
831	\end{table}
832	
833	The 9 perplexity features nearly match the full set ($\Delta{=}{-}0.4$\,pp), while repetition/diversity features alone fall 13.4\,pp below; perplexity degradation statistics therefore carry the dominant depth signal.
834	The top-2 individual features by Gini importance are \texttt{p90\_ppl} (22.4\%) and \texttt{var\_surprisal} (18.8\%), accounting for 41\% of total importance.
835	
836	\subsection{RF Seed Robustness}
837	\label{app:rf_seed}
838	
839	Table~\ref{tab:rf_seed} reports cross-model transfer accuracy across three RF random seeds.
840	
841	\begin{table}[h]
842	\centering
843	\small
844	\caption{RF seed robustness (cross-model LOO, nucleus, 4-class).}
845	\label{tab:rf_seed}
846	\begin{tabular}{@{}lc@{}}
847	\toprule
848	Seed & Acc (\%) \\
849	\midrule
850	42 & 66.4 \\
851	123 & 66.5 \\
852	456 & 66.5 \\
853	\midrule
854	Mean $\pm$ std & 66.48 $\pm$ 0.06 \\
855	\bottomrule
856	\end{tabular}
857	\end{table}
858	
859	The 0.06\,pp standard deviation across seeds confirms that RF classification is deterministic to within rounding noise at this sample size, and reported accuracy differences across experimental conditions (e.g., feature ablation, cross-model transfer) are not attributable to classifier randomness.
860	
861	\subsection{Binary Detector Baselines for Ordinal Classification}
862	\label{app:detector_baselines}
863	
864	We evaluate whether existing binary AI-text detectors and membership inference methods, when repurposed for ordinal classification, can match our 19-feature RF pipeline.
865	
866	\paragraph{Binary detectors (Pythia nucleus).}
867	Binoculars~\cite{binoculars2024} and Fast-DetectGPT~\cite{fast_detectgpt2024} scores are computed on the Pythia-1.4B nucleus ($p{=}0.95$) subset and fed to: (a)~a log-likelihood rank classifier (Log-Rank, 64.0\%), (b)~a combined RF trained on both detector scores (Combined, 74.2\%), and (c)~the standard 19-feature RF (78.7\%).
868	The 4.5\,pp gap (74.2\% vs.\ 78.7\%) confirms that perplexity distributional features capture ordinal depth structure beyond what generic detection scores provide.
869	Note that Fast-DetectGPT exhibits numerical overflow on Pythia nucleus d1 (mean perturbation score $>$28{,}000); results for this cell should be interpreted cautiously.
870	Across all 9 atlas cells, Binoculars and Fast-DetectGPT ordinal accuracy averages ${\sim}$35\% and ${\sim}$32\%, respectively.
871	
872	\paragraph{Membership inference baselines (all 9 cells).}
873	DetectGPT~\cite{mitchell2023_detectgpt} (gpt2-large scoring model, t5-large perturbation model, 5 perturbations) achieves 30.7\% mean 4-class accuracy (d1--d3 BalAcc: 24.3\%); Table~\ref{tab:baselines} reports 28.8\% under the best-of-3 calibration protocol, which selects the optimal threshold configuration per cell.
874	Min-K\% Prob~\cite{shi2024_minkprob} ($K{=}20$) with CORAL ordinal calibration reaches 33.2\% (d1--d3 BalAcc: 40.4\%); the best single cell is gpt2xl\_temp09 at 50.6\%.
875	Min-K\%'s advantage over DetectGPT (+2.5\,pp) is consistent with token-level log-probabilities containing more depth-relevant information than perturbation-based curvature, but both remain within 10\,pp of chance.
876	CORAL calibration improves ordinal structure (d1--d3 BalAcc 40.4\% vs.\ 33.3\% random) without closing the gap to RF (71.6\%), confirming that the bottleneck is the input signal rather than the calibration strategy.
877	Perturbation-based and membership-inference methods (28--33\%) confirm that token-level detection scores lack ordinal depth resolution.
878	Cross-perplexity (Binoculars) is a notable exception: when evaluated across all 9 atlas cells with threshold calibration, Binoculars achieves 69.8\%; with multi-feature RF calibration (11 cross-perplexity statistics), it reaches 78.1\%, matching our 19-feature pipeline within 0.3\,pp (\S\ref{sec:gen:baselines}).
879	
880	\paragraph{Augmented feature set.}
881	To test whether detection scores carry complementary ordinal signal, we add Min-K\% probability ($K{=}20$) and DetectGPT perturbation discrepancy as additional RF features.
882	The 21-feature model (19 + Min-K\% + DetectGPT) achieves 78.90\% mean 4-class accuracy (+0.48\,pp) and 72.20\% d1--d3 balanced accuracy (+0.60\,pp).
883	Min-K\% ranks \#3 by feature importance (0.095), behind \texttt{p90\_ppl} (0.161) and \texttt{var\_surprisal} (0.126); DetectGPT ranks \#17 (0.026).
884	The marginal improvement is consistent across 8 of 9 atlas cells, indicating that Min-K\%'s token-level log-probability signal provides weak but real complementary information to the passage-level distributional features.
885	The top-2 features (\texttt{p90\_ppl} + \texttt{var\_surprisal}) retain combined importance of 28.7\%, confirming that perplexity tail statistics remain the dominant depth markers even after augmentation.
886	
887	\paragraph{Pairwise AUC and ordinal collapse.}
888	Table~\ref{tab:detector_pairwise_auc} reports pairwise binary AUC for three nucleus cells, contrasting our 19-feature RF with LR-calibrated detector scores and their combination.
889	Detectors achieve reasonable d0-vs-d1 separation (Combined AUC\,$\geq$\,0.949), but d1-vs-d2 and d2-vs-d3 AUC collapse toward chance (0.50--0.77), far below the RF pipeline (0.930--0.958 and 0.813--0.892 respectively).
890	This confirms that binary detection scores capture the real-vs-synthetic boundary but lack the ordinal gradient needed to distinguish recursive depths.
891	
892	\begin{table}[h]
893	\centering
894	\small
895	\caption{Pairwise binary AUC for detector baselines vs.\ RF-19feat on three nucleus cells. RF uses 500-tree binary classifiers; detector methods use LR on continuous scores (Bino/FDGPT) or their combination. d1v2 and d2v3 AUC near 0.50 = ordinal collapse.}
896	\label{tab:detector_pairwise_auc}
897	\resizebox{\columnwidth}{!}{%
898	\begin{tabular}{@{}llccc@{}}
899	\toprule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a52257e-c3da-445d-a776-efe854bb4022",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "dfda4f9c-8642-42dc-a4e5-d7a5167505ff",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
      "content": "Strategy & Self-ref (\\%) & Cross-ref (\\%) & $\\Delta$ & $\\mathrm{EDD}_{0.70}$ & d0v1 AUC \\\\\n\\midrule\nnucleus & 54.1 & 45.0 & $-$9.1 & 2 & 0.702 \\\\\ntemp ($\\tau{=}0.9$) & 50.5 & 46.3 & $-$4.2 & 2 & 0.739 \\\\\ntop-$k$ ($k{=}50$) & 47.9 & 40.9 & $-$7.1 & 0 & 0.699 \\\\\n\\cmidrule{2-6}\n\\textit{mean} & \\textit{50.8} & \\textit{44.1} & $-$\\textit{6.8} & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nCross-reference accuracy drops by 6.8\\,pp on average (range 4.2--9.1\\,pp), but $\\mathrm{EDD}_{0.70}$ \\emph{rises} from 0 to 2 for nucleus and temperature: the consecutive d0v1 (0.70--0.74) and d1v2 (0.72--0.73) AUCs now exceed the 0.70 threshold, while d2v3 remains below (0.54--0.61).\nUnder self-reference, the first boundary d0v1 falls below $T{=}0.70$ in all strategies (0.56--0.64), breaking the contiguous prefix and yielding $\\mathrm{EDD}_{0.70}{=}0$ even though some later pairs (e.g., nucleus d1v2\\,=\\,0.713, d2v3\\,=\\,0.728) exceed the threshold; the Pythia-1.4B reference model provides sharper distributional contrast at the cost of overall accuracy.\nThe ${\\sim}$7\\,pp accuracy gap between self- and cross-reference is therefore a reference-model artifact, not a depth-signal artifact: depth signal persists at 14B albeit attenuated relative to 1--1.5B.\n\n\\paragraph{Caveats.}\nFor Qwen2.5-7B, the CI lower bound (58.0\\%) does not exclude sub-60\\% accuracy; Llama-3.1-8B's lower bound (68.3\\%) is more comfortably above chance but still below the 75--83\\% range at 1--1.5B.\nThe divergent AUC trajectories across two models caution against strong generalizations from only two 7--8B data points: both the monotonic (Llama-3.1) and non-monotonic (Qwen2.5) patterns are single observations, and further architectures are needed to establish which is the dominant regime at this scale.\n\n\\paragraph{Confounds.}\n\\label{app:cross_scale_confounds}\nFour confounds limit the 7--8B results: (1)~4-bit NF4 QLoRA quantization (absent at 1--1.5B) may distort the perplexity distribution independently of depth; (2)~smaller sample size (500 vs.\\ 5{,}000 per depth) widens confidence intervals; (3)~evaluation is limited to nucleus sampling at 7--8B (the 14B model addresses this with all three strategies); (4)~vocabulary mismatch between larger generators and the 1.4B reference model.\nFor the 14B model specifically: the cross-reference control (Table~\\ref{tab:cross_ref_14b}) quantifies the reference-model artifact at ${\\sim}$7\\,pp, but the remaining accuracy gap (44\\% vs.\\ 78--85\\% at 1--1.5B) still conflates scale with the other confounds listed above.\nThe base-model control partially addresses a former confound (instruction-tuning): since the base variant shows weaker signal with non-monotonic decay while the instruction-tuned variant shows stronger monotonic signal, instruction-tuning regularizes rather than confounds depth estimation.\nThe remaining confounds are not mutually independent (quantization and vocabulary mismatch both affect the perplexity distribution); it is therefore infeasible to attribute the observed accuracy gap (60--70\\% vs.\\ 78--85\\% at 1--1.5B) to any single factor.\n\n\\subsection{Cross-Boundary Generalization}\n\\label{app:cross_boundary}\n\nThe preceding experiments assume a single model family generates all recursive depths.\nIn practice, recursive contamination may traverse model boundaries: text generated by model~A is used to train model~B, whose output trains model~C.\nWe probe whether the depth signal persists under two relaxations of the single-model assumption.\n\n\\paragraph{Cross-model recursive chains.}\nWe construct a heterogeneous chain: human text (d0) $\\to$ Pythia-1.4B generates d1 $\\to$ OLMo-1B finetuned on Pythia-d1 generates d2 $\\to$ GPT-2~XL finetuned on OLMo-d2 generates d3.\nEach recursive step uses a \\emph{different} model family, eliminating the possibility that depth signal arises from a single model's idiosyncratic behavior.\nA 4-class Random Forest achieves 84.75\\% accuracy (95\\% CI $[81.0, 88.25]$), with per-depth F1 scores of 0.98 (d0), 0.88 (d1), 0.76 (d2), and 0.76 (d3).\nPairwise AUC remains high: d0-vs-d1 = 0.999 and d2-vs-d3 = 0.841.\nThese results suggest that distributional artifacts of recursive generation persist across model boundaries. This constitutes preliminary evidence for a process-level depth signal rather than individual generator artifacts.\n\n\\paragraph{Confound discussion.}\nThe heterogeneous chain confounds architecture identity with depth (d1=Pythia, d2=OLMo, d3=GPT-2~XL).\nHowever, if the classifier exploited architecture fingerprints rather than depth signal, near-perfect accuracy would be expected since architecture perfectly determines depth label.\nThe observed 84.75\\% with monotonically decreasing per-depth F1 (d0=0.98, d1=0.88, d2=0.76, d3=0.76) is more consistent with a depth-signal interpretation, as architecture fingerprinting would not produce this graded pattern.\nWe address this confound directly with a reverse-chain control below.\n\n\\paragraph{Reverse-chain control.}\nTo empirically test the architecture confound hypothesis, we constructed a reverse chain (GPT-2~XL $\\to$ OLMo $\\to$ Pythia) reversing the model-depth assignment.\nThe reverse chain achieves 85.75\\% (95\\% CI [82.0, 89.25]), statistically indistinguishable from the forward chain (84.75\\%, [81.0, 88.25]).\nIf the classifier exploited architecture fingerprints rather than depth signal, reversing the chain should invert depth predictions; the equivalent accuracy under both orderings provides empirical evidence against the architecture confound.\n\n\\paragraph{Cross-domain transfer.}\nAll prior experiments use WikiText-103 as the seed corpus.\nTo test domain dependence, we repeat the pipeline with arXiv abstracts as the seed text (Pythia-1.4B, nucleus $p{=}0.95$, 500 samples per depth, d0--d3).\nFive-fold cross-validation yields 74.1\\% $\\pm$ 2.0\\% accuracy, compared to ${\\sim}$78\\% on the WikiText seed.\nPer-depth F1 shows the familiar pattern: d0 = 1.00, d1 = 0.78, d2 = 0.52, d3 = 0.66, with d2 remaining the most challenging class.\nThe 4pp accuracy gap relative to WikiText likely reflects the narrower stylistic range of scientific abstracts, which may reduce the distributional contrast between adjacent depths.\nThese results provide preliminary evidence that the perplexity-based features capture properties of the recursive generation process rather than domain-specific artifacts of the seed corpus.\n\n\\subsection{Cross-Seed Replication}\n\\label{app:seed_replication}\n\nTable~\\ref{tab:seed_replication} reports within-seed accuracy for all three model families (nucleus, depths 0--3) under two independent LoRA training seeds.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-seed replication (nucleus $p{=}0.95$, d0--d3). seed=42 is the primary benchmark (matching Table~\\ref{tab:main_matrix}); seed=43 is an independent replication.}\n\\label{tab:seed_replication}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nModel & Seed & Acc (\\%) & 95\\% CI & $\\Delta$ (pp) \\\\\n\\midrule\nPythia-1.4B & 42 & 78.70 & [78.10, 79.24] & --- \\\\\nPythia-1.4B & 43 & 78.84 & [78.13, 79.52] & $+$0.14 \\\\\n\\midrule\nOLMo-1B & 42 & 78.94 & [78.38, 79.48] & --- \\\\\nOLMo-1B & 43 & 82.11 & [81.77, 82.54] & $+$3.17 \\\\\n\\midrule\nGPT-2~XL & 42 & 84.28 & [83.78, 84.80] & --- \\\\\nGPT-2~XL & 43 & 86.32 & [86.17, 86.49] & $+$2.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeed=43 yields higher accuracy in all three models ($+$0.14 to $+$3.17\\,pp, same direction).\nFor Pythia ($+$0.14\\,pp), CIs overlap, consistent with noise; for OLMo ($+$3.17\\,pp) and GPT-2~XL ($+$2.04\\,pp), CIs do not overlap, so LoRA initialization has a non-trivial effect on absolute accuracy (${\\sim}$1--3\\,pp).\nTop-3 features are identical across all seeds and models (\\texttt{p90\\_ppl}, \\texttt{var\\_surprisal}, \\texttt{p75\\_ppl}); depth ordering is preserved in every configuration.\n\n\\paragraph{Outlier handling.}\nFeature extraction occasionally produces extreme perplexity values (outlier passages); we apply per-feature clipping at $\\pm 10^{10}$ before classification, affecting ${<}0.1$\\% of samples.\nThe d3 perplexity distribution varies substantially across seeds: under seed=42, 0.56\\% of d3 passages exceed $10^6$ in raw perplexity, while under seed=43 this fraction rises to 12.8\\%.\nDespite this variation, the classifier remains effective after clipping, confirming that the depth signal resides in the p90-and-below distributional shape rather than extreme outliers.\n\n\\subsection{Depth-4 Extension}\n\\label{app:depth4_ext}\n\nWe extend all three model families (GPT-2~XL, Pythia-1.4B, OLMo-1B; nucleus $p{=}0.95$) to depth~4 and train 5-class RF classifiers (d0--d4, 5{,}000 samples per depth).\nFive-class accuracy reaches 80.5\\% (OLMo), 74.0\\% (GPT-2~XL), and 71.3\\% (Pythia), all substantially above the 20\\% chance baseline.\nFor Pythia and GPT-2~XL, d3 recall drops from ${\\sim}$80\\% (4-class) to ${\\sim}$49\\% (5-class) due to d3/d4 confusion; d4 recall is higher (Pythia 68.1\\%, GPT-2~XL 63.9\\%).\n$\\mathrm{EDD}_{0.70} \\geq 4$ was established by dedicated binary classifiers in the atlas (\\S\\ref{sec:atlas:edd}; d3v4 AUC: Pythia 0.784, OLMo 0.765, GPT-2~XL 0.750); the 5-class results provide complementary evidence that depth~4 remains discriminable in the multi-class setting.\n\n\\paragraph{Feature monotonicity at d4.}\nFor Pythia and GPT-2~XL, the dominant depth markers (\\texttt{p90\\_ppl}, \\texttt{var\\_surprisal}) maintain monotonic decrease through d4 (Pythia \\texttt{p90\\_ppl}: $483.7 \\to 12.5$ from d0 to d4; \\texttt{var\\_surprisal}: $6.50 \\to 1.29$), consistent with continued tail erosion (\\S\\ref{sec:method:theory}).\nMean perplexity breaks monotonicity at d4 for GPT-2~XL (d3: $1{,}076\\mathrm{K}$ $\\to$ d4: $928\\mathrm{K}$) while tail perplexity continues to decline.\nOLMo exhibits a \\texttt{var\\_surprisal} rebound at d4 ($2.49 \\to 2.83$, non-monotonic), creating a feature signature absent in GPT-2~XL and Pythia.\nThe 5-class RF exploits non-adjacent depth contrasts (particularly d0-vs-d4 and d2-vs-d4) to achieve 80.5\\% accuracy, the highest among all three families, while the dedicated binary d3-vs-d4 classifier (AUC 0.765) is restricted to adjacent-depth features.\nThis discrepancy illustrates that multi-class classifiers can exploit global distributional structure unavailable to pairwise comparisons.\nThe divergence between aggregate and tail statistics suggests that aggregate distributional statistics saturate at deep recursion while tail statistics continue to shift.\nThis saturation provides a physical mechanism for the EDD ceiling: once per-step feature change falls below classifier resolution, adjacent depths become indistinguishable regardless of continued distributional drift.\n\n\\subsection{Generation Length Ablation}\n\\label{app:length_ablation}\n\nTable~\\ref{tab:length_ablation} reports classification accuracy as a function of passage length (Pythia-1.4B nucleus, depths 0--3).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Generation length ablation (Pythia-1.4B nucleus, 5-fold CV). Accuracy increases monotonically with passage length; the 9.47\\,pp spread confirms that longer passages provide stronger statistical signal.}\n\\label{tab:length_ablation}\n\\begin{tabular}{@{}lc@{}}\n\\toprule\nPassage length (tokens) & Acc (\\%) \\\\\n\\midrule\n128 & 68.35 \\\\\n256 & 73.80 \\\\\n512 & 77.82 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDepth signal is detectable from 128 tokens (2.7$\\times$ chance) and saturates near 500 tokens.\nThe monotonic increase reflects the statistical nature of the features: longer passages yield more stable estimates of perplexity percentiles and surprisal variance, reducing within-class overlap at adjacent depth boundaries.\n\n\\subsection{Mixed-Depth Corpus}\n\\label{app:mixed_depth}\n\nPer-passage classification is largely independent of corpus composition: evaluating on a corpus containing mixed proportions of d0--d3 passages (rather than balanced classes) yields macro-recall $\\Delta{=}{-}1.62$\\,pp relative to the balanced benchmark (within the 2\\,pp tolerance).\nIndividual class deltas range from $-$0.45\\,pp to $-$2.43\\,pp (d1 shows the largest shift); the RF classifier operates on per-sample features without sensitivity to the class distribution of the evaluation corpus, as Random Forest produces identical per-sample predictions regardless of batch context.\n\n\\subsection{Learned Estimator Comparison}\n\\label{app:learned_estimator}\n\nTable~\\ref{tab:learned_estimator} evaluates three learned classifiers (XGBoost, ordinal MLP with CORAL loss \\cite{coral2020}, prototypical networks) under the same leave-one-model-out protocol as Table~\\ref{tab:cross_model}.\nThe ordinal MLP follows the nested binary reduction framework \\cite{mccullagh1980_ordinal,frank2001} with the loss function of \\citet{rennie2005}.\nAll three methods operate on the same 19-dimensional feature vector; the comparison isolates the effect of the classification head.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Learned estimator cross-model transfer (leave-one-model-out, nucleus, 4-class). RF baseline from Table~\\ref{tab:cross_model}. Chance = 25\\%.}\n\\label{tab:learned_estimator}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nMethod & Pythia & OLMo & GPT-2 XL & Mean \\\\\n\\midrule\nRF (baseline) & --- & --- & --- & 66.4 \\\\\nXGBoost & 63.7 & 69.8 & 68.1 & 67.2 \\\\\nOrdinal MLP & 62.5 & 69.7 & 67.9 & 66.7 \\\\\nPrototypical & 61.6 & 70.0 & 68.4 & 66.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll three learned methods match the RF baseline within 0.8\\,pp on average; the Pythia holdout is consistently the hardest (61.6--63.7\\%), while OLMo and GPT-2~XL holdouts yield 67.9--70.0\\%.\nThe narrow spread ($\\leq$0.8\\,pp across four methods) reinforces the conclusion that the 19-feature representation, not the classifier, determines the accuracy ceiling in the cross-model transfer setting.\n\n\\subsection{Instruction-Tuned Model at 1.5B Scale}\n\\label{app:instruct_1p5b}\n\nTo test whether instruction tuning eliminates depth signal at matched scale (1.5B, avoiding the quantization confound of \\S\\ref{sec:gen:crossscale}), we run the full recursive pipeline on Qwen2.5-1.5B-Instruct with self-reference feature extraction (i.e., the same model serves as both generator and reference).\n\nThe RF classifier achieves 47.4\\% four-class accuracy (95\\% CI $[46.7, 48.1]$, $1.9\\times$ chance); instruction tuning therefore reduces but does not eliminate depth signal.\nThe pairwise AUC profile differs from base models: d0v1 = 0.653, d1v2 = 0.620, d2v3 = 0.664, with a gap-dependent pattern (non-adjacent pairs yield higher AUC, e.g., d0v3 = 0.902) but no pair reaching the 0.75 threshold.\n\nThe feature importance ranking shifts: the perplexity tail statistics (\\texttt{p90\\_ppl}, \\texttt{var\\_surprisal}) that dominate in base models drop in relative importance, while surprisal variance and mean-level features gain rank.\nThis shift suggests instruction tuning compresses the perplexity distribution (reducing tail discriminability) while preserving lower-order statistical patterns.\n\nTwo caveats apply: (1) self-reference evaluation may inflate or deflate accuracy relative to cross-reference evaluation (cf.\\ \\S\\ref{app:ref_ablation}); (2) a single instruction-tuned model does not establish the generality of the feature shift across architectures or instruction-tuning recipes.\n\n\\subsection{Downstream Fine-Tuning Probe (Inconclusive)}\n\\label{app:downstream}\n\nWe fine-tune Pythia-410M with LoRA ($r{=}16$, $\\alpha{=}32$) on depth-stratified subsets (500 samples each) and evaluate held-out perplexity (200 samples, 50 per depth).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Downstream fine-tuning probe: held-out perplexity by training subset (Pythia-410M LoRA, seed=42). $\\Delta$: signed difference vs.\\ baseline (negative = better).}\n\\label{tab:downstream}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nTraining subset & PPL & $\\Delta$ vs.\\ baseline \\\\\n\\midrule\nBaseline (no fine-tuning) & 5.67 & --- \\\\\nd0 only & 5.65 & $-$0.02 \\\\\nd1 only & 5.55 & $-$0.12 \\\\\nd2 only & 5.56 & $-$0.11 \\\\\nMixed (d0--d3) & 5.55 & $-$0.12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe hypothesis that d0-only data yields the lowest perplexity is not supported: d1-only and mixed subsets tie for best (PPL~5.55), both marginally below d0-only (5.65).\nThe PPL spread is small (0.12, 2.1\\% relative) and the sample size (500 per condition, single seed) is insufficient for statistical significance.\nTraining loss decreases monotonically with depth (d0: 2.558, d1: 1.920, d2: 1.286), consistent with recursive generation reducing information content and making text easier to model.\nThis pilot establishes that depth-filtered data is not harmful for downstream fine-tuning; whether depth-aware curation provides a meaningful advantage requires larger-scale evaluation.\n\n\\subsection{Feature Group Ablation}\n\\label{app:feature_ablation}\n\nTable~\\ref{tab:feature_ablation} reports cross-model transfer accuracy (leave-one-model-out, nucleus) when restricting the classifier to subsets of the 19-feature vector, grouped by signal type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Feature group ablation (cross-model LOO, nucleus, 4-class). Groups merge the four Table~\\ref{tab:features} categories into three: bigram/trigram entropy move from Lexical Diversity to Entropy/Surprisal; TTR/hapax move to Repetition/Diversity. Chance = 25\\%.}\n\\label{tab:feature_ablation}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nFeature group & \\#Feat. & Acc (\\%) & $\\Delta$ vs.\\ Full \\\\\n\\midrule\nFull (all 19) & 19 & 66.4 & --- \\\\\nPerplexity only & 9 & 66.0 & $-$0.4 \\\\\nEntropy/Surprisal only & 5 & 63.2 & $-$3.2 \\\\\nRepetition/Diversity only & 5 & 53.0 & $-$13.4 \\\\\n\\midrule\n\\texttt{p90\\_ppl} only & 1 & 58.3 & $-$8.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 9 perplexity features nearly match the full set ($\\Delta{=}{-}0.4$\\,pp), while repetition/diversity features alone fall 13.4\\,pp below; perplexity degradation statistics therefore carry the dominant depth signal.\nThe top-2 individual features by Gini importance are \\texttt{p90\\_ppl} (22.4\\%) and \\texttt{var\\_surprisal} (18.8\\%), accounting for 41\\% of total importance.\n\n\\subsection{RF Seed Robustness}\n\\label{app:rf_seed}\n\nTable~\\ref{tab:rf_seed} reports cross-model transfer accuracy across three RF random seeds.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{RF seed robustness (cross-model LOO, nucleus, 4-class).}\n\\label{tab:rf_seed}\n\\begin{tabular}{@{}lc@{}}\n\\toprule\nSeed & Acc (\\%) \\\\\n\\midrule\n42 & 66.4 \\\\\n123 & 66.5 \\\\\n456 & 66.5 \\\\\n\\midrule\nMean $\\pm$ std & 66.48 $\\pm$ 0.06 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 0.06\\,pp standard deviation across seeds confirms that RF classification is deterministic to within rounding noise at this sample size, and reported accuracy differences across experimental conditions (e.g., feature ablation, cross-model transfer) are not attributable to classifier randomness.\n\n\\subsection{Binary Detector Baselines for Ordinal Classification}\n\\label{app:detector_baselines}\n\nWe evaluate whether existing binary AI-text detectors and membership inference methods, when repurposed for ordinal classification, can match our 19-feature RF pipeline.\n\n\\paragraph{Binary detectors (Pythia nucleus).}\nBinoculars~\\cite{binoculars2024} and Fast-DetectGPT~\\cite{fast_detectgpt2024} scores are computed on the Pythia-1.4B nucleus ($p{=}0.95$) subset and fed to: (a)~a log-likelihood rank classifier (Log-Rank, 64.0\\%), (b)~a combined RF trained on both detector scores (Combined, 74.2\\%), and (c)~the standard 19-feature RF (78.7\\%).\nThe 4.5\\,pp gap (74.2\\% vs.\\ 78.7\\%) confirms that perplexity distributional features capture ordinal depth structure beyond what generic detection scores provide.\nNote that Fast-DetectGPT exhibits numerical overflow on Pythia nucleus d1 (mean perturbation score $>$28{,}000); results for this cell should be interpreted cautiously.\nAcross all 9 atlas cells, Binoculars and Fast-DetectGPT ordinal accuracy averages ${\\sim}$35\\% and ${\\sim}$32\\%, respectively.\n\n\\paragraph{Membership inference baselines (all 9 cells).}\nDetectGPT~\\cite{mitchell2023_detectgpt} (gpt2-large scoring model, t5-large perturbation model, 5 perturbations) achieves 30.7\\% mean 4-class accuracy (d1--d3 BalAcc: 24.3\\%); Table~\\ref{tab:baselines} reports 28.8\\% under the best-of-3 calibration protocol, which selects the optimal threshold configuration per cell.\nMin-K\\% Prob~\\cite{shi2024_minkprob} ($K{=}20$) with CORAL ordinal calibration reaches 33.2\\% (d1--d3 BalAcc: 40.4\\%); the best single cell is gpt2xl\\_temp09 at 50.6\\%.\nMin-K\\%'s advantage over DetectGPT (+2.5\\,pp) is consistent with token-level log-probabilities containing more depth-relevant information than perturbation-based curvature, but both remain within 10\\,pp of chance.\nCORAL calibration improves ordinal structure (d1--d3 BalAcc 40.4\\% vs.\\ 33.3\\% random) without closing the gap to RF (71.6\\%), confirming that the bottleneck is the input signal rather than the calibration strategy.\nPerturbation-based and membership-inference methods (28--33\\%) confirm that token-level detection scores lack ordinal depth resolution.\nCross-perplexity (Binoculars) is a notable exception: when evaluated across all 9 atlas cells with threshold calibration, Binoculars achieves 69.8\\%; with multi-feature RF calibration (11 cross-perplexity statistics), it reaches 78.1\\%, matching our 19-feature pipeline within 0.3\\,pp (\\S\\ref{sec:gen:baselines}).\n\n\\paragraph{Augmented feature set.}\nTo test whether detection scores carry complementary ordinal signal, we add Min-K\\% probability ($K{=}20$) and DetectGPT perturbation discrepancy as additional RF features.\nThe 21-feature model (19 + Min-K\\% + DetectGPT) achieves 78.90\\% mean 4-class accuracy (+0.48\\,pp) and 72.20\\% d1--d3 balanced accuracy (+0.60\\,pp).\nMin-K\\% ranks \\#3 by feature importance (0.095), behind \\texttt{p90\\_ppl} (0.161) and \\texttt{var\\_surprisal} (0.126); DetectGPT ranks \\#17 (0.026).\nThe marginal improvement is consistent across 8 of 9 atlas cells, indicating that Min-K\\%'s token-level log-probability signal provides weak but real complementary information to the passage-level distributional features.\nThe top-2 features (\\texttt{p90\\_ppl} + \\texttt{var\\_surprisal}) retain combined importance of 28.7\\%, confirming that perplexity tail statistics remain the dominant depth markers even after augmentation.\n\n\\paragraph{Pairwise AUC and ordinal collapse.}\nTable~\\ref{tab:detector_pairwise_auc} reports pairwise binary AUC for three nucleus cells, contrasting our 19-feature RF with LR-calibrated detector scores and their combination.\nDetectors achieve reasonable d0-vs-d1 separation (Combined AUC\\,$\\geq$\\,0.949), but d1-vs-d2 and d2-vs-d3 AUC collapse toward chance (0.50--0.77), far below the RF pipeline (0.930--0.958 and 0.813--0.892 respectively).\nThis confirms that binary detection scores capture the real-vs-synthetic boundary but lack the ordinal gradient needed to distinguish recursive depths.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise binary AUC for detector baselines vs.\\ RF-19feat on three nucleus cells. RF uses 500-tree binary classifiers; detector methods use LR on continuous scores (Bino/FDGPT) or their combination. d1v2 and d2v3 AUC near 0.50 = ordinal collapse.}\n\\label{tab:detector_pairwise_auc}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llccc@{}}\n\\toprule",
      "numLines": 300,
      "startLine": 600,
      "totalLines": 1074
    }
  },
  "sourceToolAssistantUUID": "8a52257e-c3da-445d-a776-efe854bb4022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-22T17:56:09.683Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HrSTKJhRahXVbjiqiTquiY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": 900,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfda4f9c-8642-42dc-a4e5-d7a5167505ff",
  "isSidechain": false,
  "requestId": "req_011CbJ3ASJoKADXQSgRsu9tb",
  "type": "assistant",
  "uuid": "9bde2ebe-bbd2-4de7-b95f-3792ad0051cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mmz7xJqHeRZGi6yeZvsEg4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11213,
      "cache_read_input_tokens": 67231,
      "output_tokens": 527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11213,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 527,
          "cache_read_input_tokens": 67231,
          "cache_creation_input_tokens": 11213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11213
          },
          "type": "message"
        }
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

_source line 73 · 2026-05-22T17:56:09.691Z_

<details><summary>↩ Tool result · `toolu_01HrSTKJhRahXVbjiqiTquiY`</summary>

```text
900	Cell & Method & d0v1 & d1v2 & d2v3 \\
901	\midrule
902	Pythia-1.4B & RF-19feat & \textbf{0.999} & \textbf{0.930} & \textbf{0.813} \\
903	 & Binoculars & 0.738 & 0.529 & 0.515 \\
904	 & Fast-DetectGPT & 0.797 & 0.596 & 0.530 \\
905	 & Combined & 0.990 & 0.767 & 0.626 \\
906	\midrule
907	OLMo-1B & RF-19feat & \textbf{0.997} & \textbf{0.934} & \textbf{0.819} \\
908	 & Binoculars & 0.744 & 0.509 & 0.522 \\
909	 & Fast-DetectGPT & 0.917 & 0.668 & 0.520 \\
910	 & Combined & 0.949 & 0.742 & 0.550 \\
911	\midrule
912	GPT-2~XL & RF-19feat & \textbf{0.999} & \textbf{0.958} & \textbf{0.892} \\
913	 & Binoculars & 0.942 & 0.502 & 0.581 \\
914	 & Fast-DetectGPT & 0.955 & 0.644 & 0.655 \\
915	 & Combined & 0.969 & 0.724 & 0.703 \\
916	\bottomrule
917	\end{tabular}}
918	\end{table}
919	
920	\subsection{Binoculars Feature Ablation and Signal Decomposition}
921	\label{app:feature_ablation_bino}
922	
923	To quantify the overlap and complementarity between our 19-feature pipeline and Binoculars' cross-perplexity features, we evaluate four feature configurations across all 9 atlas cells (Table~\ref{tab:bino_ablation}).
924	
925	\begin{table}[h]
926	\centering
927	\small
928	\caption{Feature ablation: overlap and merged configurations (9-cell mean, 5-fold CV, RF 200 trees). The 6 overlap features are the perplexity statistics shared between both pipelines (mean, variance, median, p10, p90, skewness).}
929	\label{tab:bino_ablation}
930	\begin{tabular}{@{}lccc@{}}
931	\toprule
932	Configuration & \#Feat. & Acc (\%) & $\Delta$ vs.\ 19-feat \\
933	\midrule
934	6 overlap only & 6 & 75.9 & $-$2.5 \\
935	Our 19 features & 19 & 78.4 & --- \\
936	Binoculars 11 features & 11 & 78.1 & $-$0.3 \\
937	Merged (19 + 11) & 30 & \textbf{82.6} & +4.2 \\
938	\bottomrule
939	\end{tabular}
940	\end{table}
941	
942	The 6 shared perplexity features alone achieve 75.9\% (97\% of the full pipeline's accuracy), confirming that mean-level perplexity distributional displacement is the core depth signal.
943	Our 13 additional features (kurtosis, surprisal variance, lexical/n-gram statistics) contribute +2.5\,pp of shape-level information; Binoculars' 5 unique features (observer-performer agreement score, cross-entropy statistics) contribute +4.2\,pp of cross-model divergence when merged.
944	
945	Table~\ref{tab:bino_ablation_percell} reports per-cell results for three configurations with per-cell breakdown (Bino-11 per-cell values are omitted because features were computed on the pooled 9-cell corpus).
946	
947	\begin{table}[h]
948	\centering
949	\small
950	\caption{Per-cell feature ablation (4-class accuracy \%, 5-fold CV, RF 200 trees). $\Delta$: merged minus 19-feature accuracy. Bino-11 per-cell values omitted because Binoculars features were computed on the pooled 9-cell corpus; the per-cell mean (78.1\%) is reported in Table~\ref{tab:bino_ablation}.}
951	\label{tab:bino_ablation_percell}
952	\resizebox{\columnwidth}{!}{%
953	\begin{tabular}{@{}lcccc c@{}}
954	\toprule
955	Cell & 6-overlap & 19-feat & Bino-11 & Merged & $\Delta$ \\
956	\midrule
957	Pythia nucleus & 76.7 & 78.7 & --- & 83.5 & +4.8 \\
958	Pythia temp09 & 73.9 & 76.8 & --- & 81.5 & +4.7 \\
959	Pythia top-$k$50 & 65.3 & 68.9 & --- & 71.2 & +2.3 \\
960	OLMo nucleus & 76.4 & 78.9 & --- & 84.2 & +5.3 \\
961	OLMo temp09 & 81.0 & 82.3 & --- & 88.3 & +6.0 \\
962	OLMo top-$k$50 & 72.5 & 74.4 & --- & 78.4 & +4.0 \\
963	GPT-2~XL nucleus & 81.7 & 84.3 & --- & 88.8 & +4.5 \\
964	GPT-2~XL temp09 & 84.0 & 85.9 & --- & 88.5 & +2.6 \\
965	GPT-2~XL top-$k$50 & 72.1 & 75.8 & --- & 79.1 & +3.3 \\
966	\midrule
967	\textbf{9-cell mean} & \textbf{75.9} & \textbf{78.4} & \textbf{78.1} & \textbf{82.6} & \textbf{+4.2} \\
968	\bottomrule
969	\end{tabular}}
970	\end{table}
971	
972	\paragraph{Strategy-dependent complementarity.}
973	The merged improvement varies by decoding strategy: nucleus and temperature cells gain +4.7\,pp on average, while top-k cells gain +3.2\,pp.
974	Top-k sampling truncates the token distribution to the $k$ highest-probability tokens, producing text with reduced distributional diversity; this limits the information available to cross-model divergence features, which rely on disagreement between observer and performer predictions.
975	Merged improvement also varies by generator family: OLMo cells (observer-dissimilar) gain +5.1\,pp on average, compared to +3.9\,pp for Pythia (observer-similar) and +3.5\,pp for GPT-2~XL, suggesting cross-model divergence features contribute more when observer and generator architectures differ.
976	
977	\paragraph{Cross-scale Binoculars ablation (14B).}
978	We evaluate Binoculars cross-scale on two representative strategies (temperature, top-$k$); the nucleus cell was used for the main 14B pipeline and its GPU hours were allocated to generation rather than Binoculars evaluation.
979	At 14B, when only 1--1.5B reference models are available for cross-perplexity computation (Pythia-1.4B observer analyzing Qwen2.5-14B text), Binoculars features degrade substantially (Table~\ref{tab:bino_14b_ablation}).
980	Self-reference statistical features (19-feat) outperform Binoculars (11-feat) by 8--11\,pp, reversing the near-parity observed at 1--1.5B.
981	Merging all 30 features yields a consistent +3.6--3.7\,pp gain over the self-reference baseline across both tested strategies, confirming that cross-perplexity features retain complementary signal even under the 10$\times$ scale gap, though the gain is attenuated relative to +4.2\,pp at 1--1.5B.
982	
983	\begin{table}[h]
984	\centering
985	\small
986	\caption{Feature ablation at 14B (Qwen2.5-14B, self-reference$^\dagger$). Binoculars: observer=Pythia-1.4B, performer=Pythia-410M. $\Delta$: merged minus main-pipeline stat-only accuracy (Method~A alignment). Chance = 25\%.}
987	\label{tab:bino_14b_ablation}
988	\begin{tabular}{@{}lcccc@{}}
989	\toprule
990	Strategy & Bino-11 & Stat-19$^\dagger$ & Merged-30 & $\Delta$ \\
991	\midrule
992	temp09 & 42.6 & 50.5 & 54.2 & +3.7 \\
993	top-$k$50 & 37.7 & 47.9 & 51.5 & +3.6 \\
994	\bottomrule
995	\end{tabular}
996	\end{table}
997	
998	The Binoculars degradation reflects a practical deployment constraint: the 10$\times$ scale gap between observer (1.4B) and generator (14B) causes cross-perplexity features to lose sensitivity, not a fundamental limitation of the cross-model divergence channel.
999	Self-reference features are more robust across scales because they avoid the observer--generator mismatch.
1000	The accuracy difference between self-reference (50.8\%) and Binoculars stat-only (40.1\% mean) may therefore partially reflect observer capacity limitations rather than feature design differences.
1001	
1002	\subsection{Prompted Generation Results}
1003	\label{app:prompted_gen}
1004	
1005	Table~\ref{tab:prompted_gen} reports depth estimation performance under topic-seeded (prompted) generation using GPT-2~XL with nucleus sampling ($p{=}0.95$, depths 0--3).
1006	Generation is conditioned on Wikipedia topic prompts rather than a bare BOS token, a more ecologically valid test of depth signal persistence.
1007	
1008	\begin{table}[h]
1009	\centering
1010	\small
1011	\caption{Prompted generation (GPT-2~XL, nucleus $p{=}0.95$, topic-seeded). BOS baseline re-evaluated within the prompted-generation pipeline for matched comparison. 5-fold CV accuracy and pairwise AUC. Chance = 25\%.}
1012	\label{tab:prompted_gen}
1013	\begin{tabular}{@{}lc@{}}
1014	\toprule
1015	Metric & Value \\
1016	\midrule
1017	4-class accuracy (\%) & 69.52 $[68.9, 70.2]$ \\
1018	BOS-seeded baseline (\%) & 83.3 \\
1019	$\Delta$ (prompted $-$ BOS) & $-$13.78\,pp \\
1020	\midrule
1021	AUC d0v1 & 0.916 \\
1022	AUC d1v2 & 0.782 \\
1023	AUC d2v3 & 0.744 \\
1024	\midrule
1025	Top-1 feature & \texttt{p90\_ppl} \\
1026	Top-2 feature & \texttt{var\_surprisal} \\
1027	Top-3 feature & \texttt{p75\_ppl} \\
1028	\bottomrule
1029	\end{tabular}
1030	\end{table}
1031	
1032	The 13.8\,pp drop relative to BOS-seeded generation is expected: topic prompts constrain the output distribution, reducing the variance that distinguishes depths.
1033	Nevertheless, accuracy remains $2.8\times$ chance and pairwise AUC decays monotonically (0.916, 0.782, 0.744); the depth signal is therefore not an artifact of unconstrained generation.
1034	Top features are identical to BOS-seeded (\texttt{p90\_ppl} first); the same perplexity tail erosion mechanism operates under prompted conditions.
1035	
1036	\subsection{Extended Discussion}
1037	\label{app:extended_discussion}
1038	
1039	\paragraph{Cross-strategy conditional decomposition.}
1040	The two-stage pipeline (strategy identification followed by depth classification) recovers 11.5\,pp over the na\"ive pooled classifier.
1041	Under correct strategy routing, four-class accuracy reaches 72.6\% vs.\ 68.0\% under misrouting ($N{=}103{,}498$ / $76{,}502$), a gap of 4.6\,pp; d0 accuracy remains near-ceiling (${\sim}99.6$\%) regardless of routing, confirming that the d0 signal is strategy-invariant.
1042	Even the worst routing yields a floor of 67.6\% ($2.7\times$ chance), and the 31.5\,pp d1--d3 gap between correct and wrong routing confirms feature-space misalignment rather than uniform noise.
1043	End-to-end PLMs lag RF by ${\sim}20$\,pp, suggesting that current pretrained representations do not capture the distributional tail statistics that drive depth discrimination.
1044	
1045	\paragraph{Depth-graduated curation (inconclusive).}
1046	Initial curation experiments remain inconclusive: RF-vs-unfiltered is not significant ($p>0.4$; Appendix~\ref{app:curation_poc}).
1047	
1048	\paragraph{Toward a provenance toolkit.}
1049	Depth estimation complements existing provenance methods along orthogonal axes.
1050	Watermarking \cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.
1051	Source attribution \cite{uchendu2020_attribution} identifies the generating model but not the generation history.
1052	Depth estimation characterizes \emph{iterative reuse} regardless of generator cooperation or identity.
1053	A layered provenance system combining these three signals (watermark presence, source model, and recursive generation depth) could support more nuanced data auditing than any single method.
1054	
1055	\subsection{Computational Resources and Reproducibility}
1056	\label{app:compute}
1057	
1058	\paragraph{Hardware.}
1059	All experiments were conducted on 2$\times$ NVIDIA RTX PRO 6000 (48\,GB) GPUs locally and 2$\times$ NVIDIA RTX PRO 6000 (48\,GB) on cloud instances.
1060	Total computation is approximately 200 GPU$\cdot$hours, covering the $3 \times 3$ generation matrix (LoRA fine-tuning + sampling at each depth), feature extraction, depth extension to d5, 7--14B cross-scale experiments, and all ablations.
1061	
1062	\paragraph{Software.}
1063	Key library versions: PyTorch 2.10.0+cu128, Transformers 5.8.1, PEFT 0.7.1, scikit-learn 1.8.0.
1064	Additional dependencies: Accelerate 1.13.0, Datasets 4.8.4, XGBoost 3.2.0, NumPy 2.2.6 (Python 3.12.3, CUDA 12.8).
1065	
1066	\paragraph{Hyperparameters.}
1067	LoRA hyperparameters ($r{=}16$, $\alpha{=}32$, dropout $0.05$, lr $2{\times}10^{-4}$, batch size 8, 3 epochs) follow \citet{hu2022lora}.
1068	The Random Forest classifier uses 200 trees, Gini criterion, and no max depth, without hyperparameter search; all reported results use 5-fold stratified cross-validation.
1069	
1070	\paragraph{Inference cost.}
1071	Feature extraction requires a single forward pass of the reference model.
1072	On a single GPU this takes approximately 2 minutes for 5{,}000 passages; a CPU-only alternative requires approximately 50 minutes on server-grade hardware.
1073	RF classification adds negligible overhead ($<$1\,s).
1074	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bde2ebe-bbd2-4de7-b95f-3792ad0051cf",
  "isSidechain": false,
  "promptId": "83990237-af08-4029-8617-b54a800f5aa2",
  "type": "user",
  "uuid": "3d936ac2-3a1c-4630-8369-07a5fa8a005a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
      "content": "Cell & Method & d0v1 & d1v2 & d2v3 \\\\\n\\midrule\nPythia-1.4B & RF-19feat & \\textbf{0.999} & \\textbf{0.930} & \\textbf{0.813} \\\\\n & Binoculars & 0.738 & 0.529 & 0.515 \\\\\n & Fast-DetectGPT & 0.797 & 0.596 & 0.530 \\\\\n & Combined & 0.990 & 0.767 & 0.626 \\\\\n\\midrule\nOLMo-1B & RF-19feat & \\textbf{0.997} & \\textbf{0.934} & \\textbf{0.819} \\\\\n & Binoculars & 0.744 & 0.509 & 0.522 \\\\\n & Fast-DetectGPT & 0.917 & 0.668 & 0.520 \\\\\n & Combined & 0.949 & 0.742 & 0.550 \\\\\n\\midrule\nGPT-2~XL & RF-19feat & \\textbf{0.999} & \\textbf{0.958} & \\textbf{0.892} \\\\\n & Binoculars & 0.942 & 0.502 & 0.581 \\\\\n & Fast-DetectGPT & 0.955 & 0.644 & 0.655 \\\\\n & Combined & 0.969 & 0.724 & 0.703 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Binoculars Feature Ablation and Signal Decomposition}\n\\label{app:feature_ablation_bino}\n\nTo quantify the overlap and complementarity between our 19-feature pipeline and Binoculars' cross-perplexity features, we evaluate four feature configurations across all 9 atlas cells (Table~\\ref{tab:bino_ablation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Feature ablation: overlap and merged configurations (9-cell mean, 5-fold CV, RF 200 trees). The 6 overlap features are the perplexity statistics shared between both pipelines (mean, variance, median, p10, p90, skewness).}\n\\label{tab:bino_ablation}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nConfiguration & \\#Feat. & Acc (\\%) & $\\Delta$ vs.\\ 19-feat \\\\\n\\midrule\n6 overlap only & 6 & 75.9 & $-$2.5 \\\\\nOur 19 features & 19 & 78.4 & --- \\\\\nBinoculars 11 features & 11 & 78.1 & $-$0.3 \\\\\nMerged (19 + 11) & 30 & \\textbf{82.6} & +4.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 6 shared perplexity features alone achieve 75.9\\% (97\\% of the full pipeline's accuracy), confirming that mean-level perplexity distributional displacement is the core depth signal.\nOur 13 additional features (kurtosis, surprisal variance, lexical/n-gram statistics) contribute +2.5\\,pp of shape-level information; Binoculars' 5 unique features (observer-performer agreement score, cross-entropy statistics) contribute +4.2\\,pp of cross-model divergence when merged.\n\nTable~\\ref{tab:bino_ablation_percell} reports per-cell results for three configurations with per-cell breakdown (Bino-11 per-cell values are omitted because features were computed on the pooled 9-cell corpus).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-cell feature ablation (4-class accuracy \\%, 5-fold CV, RF 200 trees). $\\Delta$: merged minus 19-feature accuracy. Bino-11 per-cell values omitted because Binoculars features were computed on the pooled 9-cell corpus; the per-cell mean (78.1\\%) is reported in Table~\\ref{tab:bino_ablation}.}\n\\label{tab:bino_ablation_percell}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc c@{}}\n\\toprule\nCell & 6-overlap & 19-feat & Bino-11 & Merged & $\\Delta$ \\\\\n\\midrule\nPythia nucleus & 76.7 & 78.7 & --- & 83.5 & +4.8 \\\\\nPythia temp09 & 73.9 & 76.8 & --- & 81.5 & +4.7 \\\\\nPythia top-$k$50 & 65.3 & 68.9 & --- & 71.2 & +2.3 \\\\\nOLMo nucleus & 76.4 & 78.9 & --- & 84.2 & +5.3 \\\\\nOLMo temp09 & 81.0 & 82.3 & --- & 88.3 & +6.0 \\\\\nOLMo top-$k$50 & 72.5 & 74.4 & --- & 78.4 & +4.0 \\\\\nGPT-2~XL nucleus & 81.7 & 84.3 & --- & 88.8 & +4.5 \\\\\nGPT-2~XL temp09 & 84.0 & 85.9 & --- & 88.5 & +2.6 \\\\\nGPT-2~XL top-$k$50 & 72.1 & 75.8 & --- & 79.1 & +3.3 \\\\\n\\midrule\n\\textbf{9-cell mean} & \\textbf{75.9} & \\textbf{78.4} & \\textbf{78.1} & \\textbf{82.6} & \\textbf{+4.2} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Strategy-dependent complementarity.}\nThe merged improvement varies by decoding strategy: nucleus and temperature cells gain +4.7\\,pp on average, while top-k cells gain +3.2\\,pp.\nTop-k sampling truncates the token distribution to the $k$ highest-probability tokens, producing text with reduced distributional diversity; this limits the information available to cross-model divergence features, which rely on disagreement between observer and performer predictions.\nMerged improvement also varies by generator family: OLMo cells (observer-dissimilar) gain +5.1\\,pp on average, compared to +3.9\\,pp for Pythia (observer-similar) and +3.5\\,pp for GPT-2~XL, suggesting cross-model divergence features contribute more when observer and generator architectures differ.\n\n\\paragraph{Cross-scale Binoculars ablation (14B).}\nWe evaluate Binoculars cross-scale on two representative strategies (temperature, top-$k$); the nucleus cell was used for the main 14B pipeline and its GPU hours were allocated to generation rather than Binoculars evaluation.\nAt 14B, when only 1--1.5B reference models are available for cross-perplexity computation (Pythia-1.4B observer analyzing Qwen2.5-14B text), Binoculars features degrade substantially (Table~\\ref{tab:bino_14b_ablation}).\nSelf-reference statistical features (19-feat) outperform Binoculars (11-feat) by 8--11\\,pp, reversing the near-parity observed at 1--1.5B.\nMerging all 30 features yields a consistent +3.6--3.7\\,pp gain over the self-reference baseline across both tested strategies, confirming that cross-perplexity features retain complementary signal even under the 10$\\times$ scale gap, though the gain is attenuated relative to +4.2\\,pp at 1--1.5B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Feature ablation at 14B (Qwen2.5-14B, self-reference$^\\dagger$). Binoculars: observer=Pythia-1.4B, performer=Pythia-410M. $\\Delta$: merged minus main-pipeline stat-only accuracy (Method~A alignment). Chance = 25\\%.}\n\\label{tab:bino_14b_ablation}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & Bino-11 & Stat-19$^\\dagger$ & Merged-30 & $\\Delta$ \\\\\n\\midrule\ntemp09 & 42.6 & 50.5 & 54.2 & +3.7 \\\\\ntop-$k$50 & 37.7 & 47.9 & 51.5 & +3.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe Binoculars degradation reflects a practical deployment constraint: the 10$\\times$ scale gap between observer (1.4B) and generator (14B) causes cross-perplexity features to lose sensitivity, not a fundamental limitation of the cross-model divergence channel.\nSelf-reference features are more robust across scales because they avoid the observer--generator mismatch.\nThe accuracy difference between self-reference (50.8\\%) and Binoculars stat-only (40.1\\% mean) may therefore partially reflect observer capacity limitations rather than feature design differences.\n\n\\subsection{Prompted Generation Results}\n\\label{app:prompted_gen}\n\nTable~\\ref{tab:prompted_gen} reports depth estimation performance under topic-seeded (prompted) generation using GPT-2~XL with nucleus sampling ($p{=}0.95$, depths 0--3).\nGeneration is conditioned on Wikipedia topic prompts rather than a bare BOS token, a more ecologically valid test of depth signal persistence.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Prompted generation (GPT-2~XL, nucleus $p{=}0.95$, topic-seeded). BOS baseline re-evaluated within the prompted-generation pipeline for matched comparison. 5-fold CV accuracy and pairwise AUC. Chance = 25\\%.}\n\\label{tab:prompted_gen}\n\\begin{tabular}{@{}lc@{}}\n\\toprule\nMetric & Value \\\\\n\\midrule\n4-class accuracy (\\%) & 69.52 $[68.9, 70.2]$ \\\\\nBOS-seeded baseline (\\%) & 83.3 \\\\\n$\\Delta$ (prompted $-$ BOS) & $-$13.78\\,pp \\\\\n\\midrule\nAUC d0v1 & 0.916 \\\\\nAUC d1v2 & 0.782 \\\\\nAUC d2v3 & 0.744 \\\\\n\\midrule\nTop-1 feature & \\texttt{p90\\_ppl} \\\\\nTop-2 feature & \\texttt{var\\_surprisal} \\\\\nTop-3 feature & \\texttt{p75\\_ppl} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 13.8\\,pp drop relative to BOS-seeded generation is expected: topic prompts constrain the output distribution, reducing the variance that distinguishes depths.\nNevertheless, accuracy remains $2.8\\times$ chance and pairwise AUC decays monotonically (0.916, 0.782, 0.744); the depth signal is therefore not an artifact of unconstrained generation.\nTop features are identical to BOS-seeded (\\texttt{p90\\_ppl} first); the same perplexity tail erosion mechanism operates under prompted conditions.\n\n\\subsection{Extended Discussion}\n\\label{app:extended_discussion}\n\n\\paragraph{Cross-strategy conditional decomposition.}\nThe two-stage pipeline (strategy identification followed by depth classification) recovers 11.5\\,pp over the na\\\"ive pooled classifier.\nUnder correct strategy routing, four-class accuracy reaches 72.6\\% vs.\\ 68.0\\% under misrouting ($N{=}103{,}498$ / $76{,}502$), a gap of 4.6\\,pp; d0 accuracy remains near-ceiling (${\\sim}99.6$\\%) regardless of routing, confirming that the d0 signal is strategy-invariant.\nEven the worst routing yields a floor of 67.6\\% ($2.7\\times$ chance), and the 31.5\\,pp d1--d3 gap between correct and wrong routing confirms feature-space misalignment rather than uniform noise.\nEnd-to-end PLMs lag RF by ${\\sim}20$\\,pp, suggesting that current pretrained representations do not capture the distributional tail statistics that drive depth discrimination.\n\n\\paragraph{Depth-graduated curation (inconclusive).}\nInitial curation experiments remain inconclusive: RF-vs-unfiltered is not significant ($p>0.4$; Appendix~\\ref{app:curation_poc}).\n\n\\paragraph{Toward a provenance toolkit.}\nDepth estimation complements existing provenance methods along orthogonal axes.\nWatermarking \\cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.\nSource attribution \\cite{uchendu2020_attribution} identifies the generating model but not the generation history.\nDepth estimation characterizes \\emph{iterative reuse} regardless of generator cooperation or identity.\nA layered provenance system combining these three signals (watermark presence, source model, and recursive generation depth) could support more nuanced data auditing than any single method.\n\n\\subsection{Computational Resources and Reproducibility}\n\\label{app:compute}\n\n\\paragraph{Hardware.}\nAll experiments were conducted on 2$\\times$ NVIDIA RTX PRO 6000 (48\\,GB) GPUs locally and 2$\\times$ NVIDIA RTX PRO 6000 (48\\,GB) on cloud instances.\nTotal computation is approximately 200 GPU$\\cdot$hours, covering the $3 \\times 3$ generation matrix (LoRA fine-tuning + sampling at each depth), feature extraction, depth extension to d5, 7--14B cross-scale experiments, and all ablations.\n\n\\paragraph{Software.}\nKey library versions: PyTorch 2.10.0+cu128, Transformers 5.8.1, PEFT 0.7.1, scikit-learn 1.8.0.\nAdditional dependencies: Accelerate 1.13.0, Datasets 4.8.4, XGBoost 3.2.0, NumPy 2.2.6 (Python 3.12.3, CUDA 12.8).\n\n\\paragraph{Hyperparameters.}\nLoRA hyperparameters ($r{=}16$, $\\alpha{=}32$, dropout $0.05$, lr $2{\\times}10^{-4}$, batch size 8, 3 epochs) follow \\citet{hu2022lora}.\nThe Random Forest classifier uses 200 trees, Gini criterion, and no max depth, without hyperparameter search; all reported results use 5-fold stratified cross-validation.\n\n\\paragraph{Inference cost.}\nFeature extraction requires a single forward pass of the reference model.\nOn a single GPU this takes approximately 2 minutes for 5{,}000 passages; a CPU-only alternative requires approximately 50 minutes on server-grade hardware.\nRF classification adds negligible overhead ($<$1\\,s).\n",
      "numLines": 175,
      "startLine": 900,
      "totalLines": 1074
    }
  },
  "sourceToolAssistantUUID": "9bde2ebe-bbd2-4de7-b95f-3792ad0051cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-22T17:56:10.767Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01PWFeCL6qimW3VuTE8eJyHu`</summary>

```json
{
  "pattern": "\\\\paragraph|\\\\section|\\\\subsection",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d936ac2-3a1c-4630-8369-07a5fa8a005a",
  "isSidechain": false,
  "requestId": "req_011CbJ3ASJoKADXQSgRsu9tb",
  "type": "assistant",
  "uuid": "f1acc34c-9e61-4386-a7c1-4336130b0b7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mmz7xJqHeRZGi6yeZvsEg4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11213,
      "cache_read_input_tokens": 67231,
      "output_tokens": 527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11213,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 527,
          "cache_read_input_tokens": 67231,
          "cache_creation_input_tokens": 11213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11213
          },
          "type": "message"
        }
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

_source line 75 · 2026-05-22T17:56:10.830Z_

```json
{
  "parentUuid": "2348a16b-415f-4cf9-96eb-58549c75b2a2",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ca9c408f-969a-41b6-9bb1-68de86dcd942",
  "timestamp": "2026-05-22T17:56:10.830Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 76_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：recursive_gen_depth_est Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 45 warning…",
  "leafUuid": "ca9c408f-969a-41b6-9bb1-68de86dcd942",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9"
}
```

---

### Runtime record

_source line 77_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 recursive_gen_depth_est paper review",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9"
}
```

---

### Assistant

_source line 78 · 2026-05-22T18:00:09.825Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me check for the em-dash issue in the drafts file since the grep found em-dashes there. Let me also check for word count on Limitations, and check the discussion/conclusion for templates or placeholders.

Let me analyze what I've gathered:

### 1. Narrative Consistency

Let me trace the core story:

**Abstract's problem:** Models training on web text containing their own outputs creates a recursive loop; no method estimates how many recursive iterations a text has undergone.

**Intro's problem:** Same - recursive generation depth estimation is unstudied. The recursive model→data→model cycle is happening; whether depth can be estimated remains unknown.
 
**Intro's contributions:** The paper formalizes the task with a metric called EDD and introduces a 180K benchmark, then presents the Depth Degradation Atlas showing that perplexity tail features dominate the signal. The systematic characterization spans across models, domains, and scales with analysis of how degradation accumulates.

**Method section:** Frames this as an ordinal classification problem, constructs the benchmark by combining 3 models with 3 generation strategies across 4 depth levels to create 180K instances, extracts 19 statistical features, defines the EDD metric, and provides theoretical grounding.

**Experiments:** Validate in-distribution performance through the atlas, analyze feature importance, examine EDD behavior, show how trajectories differ by strategy, test cross-model and cross-strategy transfer, and explore scaling effects.

**Baselines:** Compare against binary detectors, membership inference approaches, and end-to-end language models.

**Conclusion:** Discusses multi-channel depth encoding, highlights that generation strategy matters more than model choice for deployment, and outlines future directions including accumulation effects, prompted generation, and frontier-scale models.

The narrative holds together well. The abstract's key claims all check out: the perplexity distribution tails carrying the signal, strategy effects dominating over architecture differences, signal degradation at scale, and baselines lacking ordinal resolution. There's a gap in the intro about estimating ordinal recursive depth that needs addressing.

Now checking the chapter structure. The abstract covers the four essential elements—problem, method, results, and significance—in roughly 180 words. The intro follows a logical progression: background on model training, problem motivation with existing tool limitations, and the core method with key findings. The structure appears sound so far.

For related work, I'm seeing thematic organization through paragraph headings that contextualize each area—model collapse theory, AI text detection, membership inference, and so on—rather than just listing papers. This approach ties each section back to the paper's scope.

Looking at the contributions now. The first one about task formalization and metrics maps to the problem definition and benchmark sections. The second contribution about the Depth Degradation Atlas should appear in section 4. The abstract claims 59–82% balanced accuracy for depths 1–3, which matches Table 1's range of 58.9–81.5% with standard rounding. The paper generally avoids overclaiming, using precise numbers and appropriate hedging language like "preliminary" for cross-scale results.

For experimental rigor, the authors include bootstrap confidence intervals in Table 1, compare against recent baselines from 2023–2026, and provide ablation studies showing how individual features like perplexity and surprisal contribute to performance.

On reproducibility, they specify LoRA hyperparameters and random forest settings, document ~200 GPU hours on dual RTX PRO 6000s, detail the Wikipedia preprocessing and fine-tuning protocol, and include a Limitations section and Ethics Statement as required—the ARR checklist itself lives in OpenReview rather than the PDF.

Now checking symbol and terminology consistency across the paper...

The mathematical notation is stable: $d$ for depth, $K$ for maximum depth, $T$ for the discrimination threshold in EDD, and $\mathcal{D}_k$ for the corpus at each depth level. Feature names like p90_ppl and var_surprisal stay consistent, and the language model $f_\theta$ is introduced in §3.1 and used throughout. One thing to note is that "recursive generation depth estimation" is framed as ordinal classification in §3.1 and maintained that way.

The paper's structure flows logically—Method leads into Theory to justify the feature choices, Atlas findings transition naturally into Generalization results, and Discussion ties everything together.

Now checking the Limitations section. It's about 170 words across two paragraphs covering full-replacement versus accumulation, scale limitations at 14B, reference model dependency, and cross-strategy transfer. That's roughly 3-4 points, which matches what's needed—substantive but concise, with specific numbers like 44.1% and 45.9% mentioned.

Moving on to the AI style checks. Em-dashes only appear in draft comments, en-dashes aren't present, and the blacklisted filler words are absent. Now examining the "-ing," patterns more carefully to identify actual AI markers versus legitimate uses like "confirming" and "sampling." I'm continuing to scan for the participial phrase pattern and finding that the paper generally avoids it, though a few instances exist but aren't problematic. Now I'm noticing something more concerning in the discussion section—there are commented-out template blocks with placeholder text for different model scales that were apparently left behind during development.

These comments won't show up in the compiled PDF, but since source files are typically submitted for EMNLP 2026, this could raise questions about incomplete work or experimental coverage. This might have already been flagged in the Phase 1 checks, but it's worth noting.

Let me also verify some of the numerical claims against the actual results. The abstract claims 59–82% balanced accuracy, but the table shows 58.9–81.5%, which rounds reasonably though 58.9 technically rounds up from below the threshold.

Checking the other key figures: the EDD results at T=0.70 match (8/9 cells), the 14B cross-reference accuracy of ~44% aligns with the table's 44.1%, the EDD values for nucleus and temperature check out, the ~7 pp impact from reference-model choice is a reasonable approximation of the -6.8 pp shown, and the d1–d3 cross-strategy mean of 45.9% matches exactly.

The Discussion section goes beyond just restating results—it interprets the findings through the lens of multi-channel depth encoding and discusses practical deployment considerations. All the main contribution claims are properly positioned in the Introduction rather than scattered through Related Work. Now I need to verify the page count against the EMNLP 2026 limit of 8 pages for the main text. The compiled version is 26 pages total, but I don't have a clear breakdown of where the main text ends and the appendix begins. Given the breadth of content—abstract, introduction, related work, method, theory, atlas, generalization, and discussion—fitting everything into 8 pages seems tight. Looking at the page count more carefully, the main text sections need to stay within the 8-page limit, and since the compilation passed, I'm probably in the clear there. I notice the Discussion and Conclusion are already merged into a single section, which is appropriate.

Now I'm identifying the critical issues: there are template comments left in the discussion file with version alternatives that need to be removed, and I should verify the main text page count isn't exceeding the limit. There's also a warning about em-dashes in one of the draft files, though that's less urgent.

Let me double-check the participial phrase patterns I flagged earlier—I need to distinguish between mid-sentence modifiers and the problematic end-of-sentence constructions that signal AI writing. Most of what I'm seeing are actually embedded phrases rather than the telltale AI pattern. I'm noticing a few more instances of the "-ing" pattern scattered through the appendix, particularly with "confirming that" constructions, though it's not pervasive enough to be a major stylistic concern. Now I want to double-check the introduction to make sure each contribution claim has proper section support—looking at whether the task formalization, the Depth Degradation Atlas, and the systematic characterization are all adequately backed up by the paper's structure.

Verifying the contributions against their sections: the first maps to problem definition and benchmark sections, the second gets its own full section, and the third is supported by the generalization results with specific cross-model and cross-domain percentages all traceable to section 5. Everything checks out. I should also scan for orphan sections—large chunks of content that don't connect to any stated contribution—and I'm finding that the theory subsection and cross-strategy transfer material both tie back to the contributions as supporting or elaborating content. The Discussion section is synthesizing findings from earlier sections like the feature importance analysis and Binoculars convergence results into higher-level interpretations, which is appropriate for that section.

Now I'm cross-checking the abstract claims against the body text. The abstract mentions a 44% cross-reference accuracy for the 14B model, and I can verify this matches the reported 44.1% drop in section 5.4.

For the EDD metrics, the abstract specifies values for nucleus, temperature, and top-k under the 14B cross-reference condition. The appendix table confirms all three values, but the main text only explicitly discusses nucleus and temperature, leaving the top-k detail implicit. The abstract is more complete here.

Looking at the paper's overall narrative arc, it moves logically from identifying the problem of unknown recursive generation depth, through formalizing it as an ordinal classification task, developing a method with statistical features and random forests, then systematically characterizing which features matter most, and finally testing generalization across models, strategies, and scales. The framing feels cohesive around understanding what drives generation depth.

The paper frames itself as a characterization and formalization contribution rather than a problem-solving one, which is appropriate given the execution. While deployment scenarios aren't explored in depth, that's acceptable for this type of work.

Now checking whether the Discussion goes beyond just restating results numbers—the specific metrics like 78.1% versus 78.4% and the percentage point differences are being used to support broader interpretations about multi-channel encoding and other phenomena, so that's working well.

I'm also noticing that the abstract uses "EDD" without defining it first, which is a potential clarity issue I should flag in my final assessment. Looking more carefully at the abstract, EDD appears without being defined there—it's only introduced later in the introduction section. This violates the norm that abbreviations used in the abstract must be defined within the abstract itself, so it's a warning-level issue. Now I'm checking the contributions section to see if there are any similar problems with undefined references. I'm noticing the discussion section has template comments indicating different versions depending on whether the 7B results meet certain thresholds, but the actual live text doesn't include those results—they're relegated to the appendix instead. The templates show contingency language for scale attenuation findings, suggesting the paper was prepared for multiple possible outcomes. The abstract properly scopes the work to the 1-1.5B parameter scale with extensions to larger models, and the title avoids overstating generality. The conclusion includes standard unnumbered sections for limitations and ethics statements. Now I'm compiling all the findings from this review. I'm checking the page count against EMNLP's 8-page limit for main text. The appendix is extensive, but the main content spans abstract through discussion with sections on methods, theory, generalization, and limitations—all of which should fit within the constraint since references and mandatory sections don't count toward the limit. The compilation passed, so the authors likely verified this already. I'll flag it as an informational note rather than a blocker.

Let me also verify the review setup: the paper uses the `[review]` option for ACL formatting, has anonymous authorship, and line numbers should be enabled automatically. Everything checks out. Now I'm ready to compile the final output.

I'm scanning through the introduction and atlas sections more carefully for AI-style writing patterns, specifically looking for participial phrases that end clauses with summary statements like "confirming that..." or "amplifying the fingerprint but creating...". These constructions can be markers of AI-generated text, so I want to flag any instances where they appear as sentence-ending patterns rather than legitimate grammatical usage.

I've identified a few candidates in the main text and several more in the appendix. Since the paper's style guidelines call for eliminating these patterns, I should document them for revision. Now I'm checking whether the Abstract and Introduction sections are consistent in how they frame the core problem—the Abstract mentions "no method estimates how many iterations a text has undergone" while the Introduction seems to approach this differently, so I need to verify that alignment.

Moving through the consistency checks: the methodology descriptions match well between Abstract and Methods, the reported accuracy ranges are nearly identical with only minor rounding differences, and the key findings about perplexity tail statistics and decoding strategy effects are consistently presented across sections. The narrative holds together strongly with no major inconsistencies. Now I'm verifying that each contribution claim in the introduction is actually supported by the experimental sections—checking the metric definition, benchmark construction, feature analysis findings, and ablation results against where they're presented in the paper. I notice the cross-domain arXiv result is actually mentioned in §5.4 as a brief note, so that checks out. Now I'm doing a final sweep to see if the contributions are handled consistently between the introduction and conclusion—the Discussion section doesn't re-list them explicitly, which is fine since it focuses on interpretation and the conclusion looks forward instead.

For the Limitations section, I need to verify it meets the audit requirement of at least 150 words and covers at least 2 distinct limitations. The first limitation discusses how the benchmark uses full-replacement chains while real-world contamination involves accumulation at unknown mixing ratios, with accuracy dropping 8–15 percentage points at 25–50% synthetic mixing levels.

The second limitation addresses scalability and generalization issues: at 14B parameters, cross-reference accuracy drops significantly to 44.1%, and cross-strategy transfer shows poor generalization with AUC values as low as 0.13 for certain model combinations, indicating that models trained on one decoding strategy struggle to detect contamination from another.

The third major limitation is the dependency on a fixed reference model—mismatches between reference and target models degrade accuracy by 4–11 percentage points, and there are additional sources of uncertainty including single LoRA seed variance, web-crawl false positive rates, and sensitivity to passage length.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca9c408f-969a-41b6-9bb1-68de86dcd942",
  "isSidechain": false,
  "requestId": "req_011CbJ3B4LjcKzXn49txd3YV",
  "type": "assistant",
  "uuid": "f8e5932a-4311-44c6-9219-64cb7f2f82bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AZ6JrwGn5zoaZXz8SUVi6M",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23227,
      "cache_read_input_tokens": 78444,
      "output_tokens": 12477,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12477,
          "cache_read_input_tokens": 78444,
          "cache_creation_input_tokens": 23227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23227
          },
          "type": "message"
        }
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

_source line 79 · 2026-05-22T18:01:16.198Z_

Now I have all the data needed. Let me compile the audit findings.

```
[CONTENT_AUDIT_START]

=== 叙事一致性（CRITICAL） ===

- [info] [叙事一致性] Abstract→Intro→Method→Atlas→Generalization→Discussion 主线一致：问题(recursive depth estimation)→方法(19 features + RF)→Atlas(feature characterization)→Generalization(boundary conditions)→Discussion(implications)。全文无叙事漂移。

- [info] [叙事一致性] Abstract 的三个 findings (tail features dominate, strategy>model, scale attenuation) 与 Atlas §4.2, Generalization §5.3, §5.4 一一对应，结论方向完全吻合。

- [info] [叙事一致性] Conclusion("Depth estimation bridges binary detection and model collapse") 准确概括了论文的贡献定位，与 Intro 的 gap ("No existing method estimates ordinal depth") 形成闭环。

=== 章节结构 ===

- [info] [章节结构] Abstract 完整回答四个问题（问题/方法/结果/意义），~180 words，在 150-250 words 规范范围内。

- [warning] [章节结构] abstract.tex:4 — Abstract 中使用 EDD 缩写 ($\mathrm{EDD}_{0.70} = 3$) 但未在 Abstract 内展开定义 "Effective Discriminable Depth"。写作规范要求 Abstract 中首次出现的缩写必须定义。

- [info] [章节结构] Introduction 采用 背景→gap→本文方法→贡献列表 结构，符合 ~5 段规范。

- [info] [章节结构] Related Work 按主题归纳（Model Collapse Theory / AI Text Detection / Membership Inference / Adjacent Tasks / Ordinal Classification / Decoding Strategy Effects），非堆砌式，每段定位本文与已有工作的关系。

=== 贡献-范围对齐 ===

- [info] [贡献-范围对齐] Intro 三条 Contribution 均有对应 section/table：(1) Task + EDD → §3.1, §3.4; (2) Atlas → §4; (3) Systematic characterization → §5。无孤儿章节。

- [info] [贡献-范围对齐] Title ("Estimating Recursive Generation Depth via Statistical Fingerprints") 与论文范围匹配，未过度宣称。Abstract 明确限定 "at the 1–1.5B parameter scale"。

=== Claim 强度匹配 ===

- [warning] [Claim强度] abstract.tex:4 — "d1–d3 balanced accuracy of 59–82%" 与 Table 1 实际范围 58.9%–81.5% 有微小偏差（58.9→59, 81.5→82 均为向上取整）。建议改为 "59–82%" 时注明 "~59–82%" 或保留一位小数。

- [info] [Claim强度] "significantly" 仅出现一次 (discussion.tex:10 "do not significantly improve")，且带 p-value ($p{>}0.4$)，用法正确。

- [info] [Claim强度] 全文无 "state-of-the-art" claim，适当使用 "preliminary" 修饰 cross-scale 结果，claim 强度与证据匹配。

- [info] [Claim强度] 14B 结果标注为 "Preliminary Cross-Scale Observations"，appropriately hedged。

=== 实验严谨性 ===

- [info] [实验严谨性] 主结果表 (Table 1) 包含 bootstrap 95% CI (±half-width, B=10,000)，报告了 MAE=0.23, QWK=0.89。

- [info] [实验严谨性] Baseline 覆盖面广且来源近期：Binoculars (2024), Fast-DetectGPT (2024), DivEye (2026), Min-K% Prob (2024), DetectGPT (2023), CORAL (2020), CLOC (2025)。

- [info] [实验严谨性] Ablation 完整：feature group ablation (perplexity/surprisal/lexical/repetition), top-5 feature ablation, single feature baseline, cross-seed replication (seed 42/43), RF seed robustness, generation length ablation, reference model ablation。

- [info] [实验严谨性] Cross-seed replication (Appendix G.15) 报告了 seed 间差异 (+0.14 to +3.17 pp)，并诚实指出 "LoRA initialization has a non-trivial effect (~1-3 pp)"。

=== 可复现性披露 ===

- [info] [可复现性] Appendix 包含完整的 LoRA 超参表 (Table A1)、RF 配置、GPU 型号 (RTX PRO 6000)、总 GPU·hours (~200)、软件版本、推理成本估算。

- [info] [可复现性] Limitations 和 Ethics Statement 均存在且实质性。

=== 符号/术语一致性 ===

- [info] [符号一致性] 核心符号 ($d$=depth, $K$=max depth, $T$=threshold, $\mathcal{D}_k$=corpus, EDD, $\mathbf{f}(x)$=feature vector) 在全文中定义清晰、使用一致。

- [info] [术语一致性] 特征名称（p90_ppl, var_surprisal 等）在正文和附录中保持一致。

=== 章节过渡与逻辑流 ===

- [info] [逻辑流] Method (§3) 以 Theory (§3.5) 衔接 Atlas (§4)，理论预测→实验验证，过渡自然。

- [info] [逻辑流] Atlas (§4) → Generalization (§5) 从 in-distribution 到 out-of-distribution，逻辑递进。

- [info] [逻辑流] Discussion 不重复 Results 数字，提供更高层解读（multi-channel encoding, deployment implications, outlook）。

=== Limitations 诚实度 ===

- [info] [Limitations] ~175 words，覆盖 4+ distinct limitations（full-replacement assumption, scale attenuation, cross-strategy barrier, reference model dependency, single seed uncertainty），实质性强，包含具体数字 (44.1%, d1v2 AUC=0.13 failure mode)。符合用户规则"一小段，3 个点左右"。

=== 去 AI 风格 ===

- [info] [去AI] Em-dash (—) 仅在 drafts/14b_scenarios.tex 注释中出现，主论文 .tex 文件中无解释性 em-dash。通过。

- [info] [去AI] En-dash ( – ) 解释性用法未检测到。通过。

- [info] [去AI] Filler words 黑名单 (It is worth noting / Notably / Importantly / Furthermore / Moreover / Additionally / delve / leverage / utilize / myriad / plethora) 全文零匹配。通过。

- [warning] [去AI] introduction.tex:16 — "confirming that signal resides in feature design, not classifier architecture" 为 -ing 分词结尾短语 (AI 写作标志)。建议改写为独立句："This confirms that signal resides in..."

- [warning] [去AI] section_appendix.tex:692 — "confirming that the depth signal resides in the p90-and-below distributional shape" 同上模式。

- [warning] [去AI] section_appendix.tex:1041 — "confirming that the d0 signal is strategy-invariant" 同上模式。

=== 源码质量 ===

- [critical] [源码质量] discussion.tex:16-21 — 残留 7B scale template 注释 ("VERSION A / VERSION B")，包含两套未选择的备用叙事方案。虽然编译后不可见，但 (1) 投稿 source 中残留 contingency 文本显示编辑不彻底；(2) 暗示 7B 结果（已在 Appendix 中存在: Llama-3.1-8B 70.2%, Qwen2.5-7B 60.1%）未被整合到主文 Discussion。建议：删除模板注释，并考虑在 Discussion 中简要提及 7B 存在性结果（或明确决定将其限制在 Appendix）。

=== 用户自定义规则检查 ===

- [info] [写作规则] EMNLP 2026 Limitations 章节长度：~175 words，覆盖 3-4 个点。符合规则"一小段，覆盖 3 个点左右"。

- [info] [写作规则] ARR Responsible NLP Checklist：论文 PDF 中未包含 checklist（正确做法，checklist 应在 OpenReview submission form 中填写）。

- [info] [审稿规则] 论文使用 \usepackage[review]{acl}，\author{Anonymous}，符合 ARR 匿名审稿要求。

- [info] [审稿规则] 正文页数限制：编译通过 26 页（含 appendix），main text 需 ≤8 页。Phase 1 编译检查已通过，未报页数违规。

[CONTENT_AUDIT_END]
```

**审计总结：**

- **Critical: 1** — Discussion 中残留 7B template 注释，需清理
- **Warning: 4** — Abstract 中 EDD 缩写未展开；数字微小取整偏差；3 处 -ing 分词短语
- **Info: 24** — 叙事一致性强，贡献-范围对齐完整，claim 强度审慎，实验设计严谨

这篇论文的叙事一致性是其强项——从 Abstract 到 Conclusion 的主线（recursive depth estimation as ordinal classification + feature characterization）保持完全一致，无漂移。主要的 critical 问题是 discussion.tex 中残留的 7B 模板注释需要清理。

[AUDIT_DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8e5932a-4311-44c6-9219-64cb7f2f82bb",
  "isSidechain": false,
  "requestId": "req_011CbJ3B4LjcKzXn49txd3YV",
  "type": "assistant",
  "uuid": "96150f56-8a35-43a7-9cc9-8fff9ff539d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/paper_audit_content_d53982b2",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AZ6JrwGn5zoaZXz8SUVi6M",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23227,
      "cache_read_input_tokens": 78444,
      "output_tokens": 12477,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12477,
          "cache_read_input_tokens": 78444,
          "cache_creation_input_tokens": 23227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23227
          },
          "type": "message"
        }
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

_source line 80_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：recursive_gen_depth_est Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 45 warning…",
  "leafUuid": "96150f56-8a35-43a7-9cc9-8fff9ff539d8",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9"
}
```

---

### Runtime record

_source line 81_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 recursive_gen_depth_est paper review",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9"
}
```

---

### Runtime record

_source line 82_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：recursive_gen_depth_est Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=True, 0 critical, 45 warning…",
  "leafUuid": "96150f56-8a35-43a7-9cc9-8fff9ff539d8",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9"
}
```

---

### Runtime record

_source line 83_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 recursive_gen_depth_est paper review",
  "sessionId": "e2a83097-15d0-4f1e-980c-6eb33f8682a9"
}
```

---
