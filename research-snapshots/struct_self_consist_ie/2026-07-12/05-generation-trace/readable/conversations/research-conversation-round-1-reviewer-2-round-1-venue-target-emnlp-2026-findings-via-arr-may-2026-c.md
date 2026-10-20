# Research conversation: [Round 1 审稿请求]: ## 审稿任务 — Reviewer 2 (Round 1) ### Venue 信息 - **Target**: EMNLP 2026 Findings (via ARR May 2026 cycle) -

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 96
- **Recorded user turns:** 3
- **Tool calls:** 27
- **Original source:** `logs/chats/exported-trajectories/account-3/56b1f119-65e5-496e-8301-345209a9bd74.jsonl`
- **Structured JSON:** [`c2553c0f4b987350b5f6.json`](../../sessions/c2/c2553c0f4b987350b5f6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T07:52:08.233Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T07:52:08.233Z",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "content": "[Round 1 审稿请求]:\n## 审稿任务 — Reviewer 2 (Round 1)\n\n### Venue 信息\n- **Target**: EMNLP 2026 Findings (via ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须，位于 Conclusion 后、References 前，不计页数\n- **附录**: 允许，不计页数\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`\n（各 section 在 `sections/` 子目录下）\n\n### 你的审查侧重：新颖性 + framing + related work 完整性 + 写作质量\n\n请重点评估以下方面：\n\n1. **新颖性与贡献**\n   - \"correlation-selection gap\" 作为概念贡献是否有足够新颖性？（注意：4/5 信号是 instance-level，定义上无法做 sample selection——这部分论证中有多少是 trivial/tautological 的？）\n   - 与 Nédellec et al. (2026) 的增量贡献是否充分论证？\n   - Soft Jaccard 作为方法贡献的新颖性如何？\n   - 三个 contribution 的每一个是否都有实质性新知识？\n\n2. **Framing 与 claim scope**\n   - 论文的核心 narrative 是否自洽？（Abstract → Introduction → Conclusion 的 claim 一致性）\n   - \"first multi-family comparison\" 的 claim 是否准确？scope 是否被恰当限定？\n   - Abstract 是否过于密集？是否首次阅读即可把握核心信息？\n   - RE 被标记为 \"preliminary\" 但在多处仍作为主要证据——framing 是否一致？\n\n3. **Related Work 完整性**\n   - 引用是否覆盖了该领域的核心文献？\n   - 是否遗漏了重要的相关工作？特别关注：\n     - LLM confidence/uncertainty estimation 领域的核心论文\n     - Self-consistency 的最新变体\n     - MBR decoding 在非 MT 领域的应用\n     - 结构化预测不确定性估计\n   - 与已有工作的对比定位是否公允（不过度贬低或忽略先前工作）？\n\n4. **写作质量**\n   - 术语使用是否一致？（confidence signal vs consistency signal; VC vs Voting Conf. 等）\n   - 论文整体组织结构是否清晰？\n   - 图表是否有效传达信息？caption 是否自足？\n   - Ethics Statement 的位置和内容是否符合 ACL 要求？\n   - Limitations section 是否诚实全面？\n\n5. **格式合规性**\n   - 是否符合 ACL 模板要求？\n   - 正文是否在 8 页内？\n   - 匿名性是否保持（无 self-citation 泄露）？\n   - 引用格式是否正确？\n\n请按 EMNLP 审稿标准给出完整审稿报告，包含：Summary、Strengths、Weaknesses (must-fix / should-fix / minor)、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T07:52:08.237Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T07:52:08.237Z",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74"
}
```

---

## Round 1

84 recorded events

### User

_source line 3 · 2026-05-15T07:52:08.272Z_

[Round 1 审稿请求]:
## 审稿任务 — Reviewer 2 (Round 1)

### Venue 信息
- **Target**: EMNLP 2026 Findings (via ARR May 2026 cycle)
- **Deadline**: 2026-05-25
- **页数限制**: 正文 8 页 + unlimited references
- **模板**: ACL format (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind
- **Limitations section**: 必须，位于 Conclusion 后、References 前，不计页数
- **附录**: 允许，不计页数

### 论文路径
`projects/struct_self_consist_ie/docs/paper/main.tex`
（各 section 在 `sections/` 子目录下）

### 你的审查侧重：新颖性 + framing + related work 完整性 + 写作质量

请重点评估以下方面：

1. **新颖性与贡献**
   - "correlation-selection gap" 作为概念贡献是否有足够新颖性？（注意：4/5 信号是 instance-level，定义上无法做 sample selection——这部分论证中有多少是 trivial/tautological 的？）
   - 与 Nédellec et al. (2026) 的增量贡献是否充分论证？
   - Soft Jaccard 作为方法贡献的新颖性如何？
   - 三个 contribution 的每一个是否都有实质性新知识？

2. **Framing 与 claim scope**
   - 论文的核心 narrative 是否自洽？（Abstract → Introduction → Conclusion 的 claim 一致性）
   - "first multi-family comparison" 的 claim 是否准确？scope 是否被恰当限定？
   - Abstract 是否过于密集？是否首次阅读即可把握核心信息？
   - RE 被标记为 "preliminary" 但在多处仍作为主要证据——framing 是否一致？

3. **Related Work 完整性**
   - 引用是否覆盖了该领域的核心文献？
   - 是否遗漏了重要的相关工作？特别关注：
     - LLM confidence/uncertainty estimation 领域的核心论文
     - Self-consistency 的最新变体
     - MBR decoding 在非 MT 领域的应用
     - 结构化预测不确定性估计
   - 与已有工作的对比定位是否公允（不过度贬低或忽略先前工作）？

4. **写作质量**
   - 术语使用是否一致？（confidence signal vs consistency signal; VC vs Voting Conf. 等）
   - 论文整体组织结构是否清晰？
   - 图表是否有效传达信息？caption 是否自足？
   - Ethics Statement 的位置和内容是否符合 ACL 要求？
   - Limitations section 是否诚实全面？

5. **格式合规性**
   - 是否符合 ACL 模板要求？
   - 正文是否在 8 页内？
   - 匿名性是否保持（无 self-citation 泄露）？
   - 引用格式是否正确？

请按 EMNLP 审稿标准给出完整审稿报告，包含：Summary、Strengths、Weaknesses (must-fix / should-fix / minor)、Questions、Missing References、Overall Assessment（评分 + 置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "06f2dfdc-ae3a-4381-8751-81df7633757f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T07:52:08.272Z_

```json
{
  "parentUuid": "06f2dfdc-ae3a-4381-8751-81df7633757f",
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
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
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
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "b154f18d-2c3f-4016-932c-a0f0281db764",
  "timestamp": "2026-05-15T07:52:08.272Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T07:52:08.272Z_

```json
{
  "parentUuid": "b154f18d-2c3f-4016-932c-a0f0281db764",
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
  "uuid": "5f440632-3a4e-4ae1-a543-98c43a834c67",
  "timestamp": "2026-05-15T07:52:08.272Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T07:52:08.272Z_

```json
{
  "parentUuid": "5f440632-3a4e-4ae1-a543-98c43a834c67",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "64a471a1-2873-4ba7-8100-6766aea5c5ba",
  "timestamp": "2026-05-15T07:52:08.272Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
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
  "aiTitle": "Review paper on structured self-consistency for IE",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74"
}
```

---

### Assistant

_source line 8 · 2026-05-15T07:52:11.138Z_

我开始审稿。首先加载 session start skill，然后读取论文和搜索 venue 审稿标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64a471a1-2873-4ba7-8100-6766aea5c5ba",
  "isSidechain": false,
  "requestId": "req_011Cb3zT43v6ApgA5tqB8tdB",
  "type": "assistant",
  "uuid": "8ac15ced-92d4-49e5-a60b-744efee84a85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016HSzz4umbTbbLcYHYXoq9d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14007,
      "cache_read_input_tokens": 11841,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14007,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 134,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14007
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-15T07:52:12.383Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MaMzVrSq8CQP7spkSwMwB1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ac15ced-92d4-49e5-a60b-744efee84a85",
  "isSidechain": false,
  "requestId": "req_011Cb3zT43v6ApgA5tqB8tdB",
  "type": "assistant",
  "uuid": "c458414e-8ddd-41b2-a219-6c1eb7d1a201",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016HSzz4umbTbbLcYHYXoq9d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14007,
      "cache_read_input_tokens": 11841,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14007,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 134,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14007
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-15T07:52:12.400Z_

<details><summary>↩ Tool result · reported error · `toolu_01MaMzVrSq8CQP7spkSwMwB1`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c458414e-8ddd-41b2-a219-6c1eb7d1a201",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "ad73cf00-8208-47c8-9b14-dda4e8613eb8",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5.",
  "sourceToolAssistantUUID": "c458414e-8ddd-41b2-a219-6c1eb7d1a201",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T07:52:14.327Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DzMVjMyeDdUKhbPLd3EqTS`</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad73cf00-8208-47c8-9b14-dda4e8613eb8",
  "isSidechain": false,
  "requestId": "req_011Cb3zTMrykv2117cF441hP",
  "type": "assistant",
  "uuid": "ef87b98a-abc0-4c76-b042-b7fde92dd77d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01439GEttbN8jx21jQSaVS25",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 214,
      "cache_read_input_tokens": 25848,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 214,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 99,
          "cache_read_input_tokens": 25848,
          "cache_creation_input_tokens": 214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 214
          },
          "type": "message"
        }
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

_source line 12 · 2026-05-15T07:52:14.358Z_

<details><summary>↩ Tool result · `toolu_01DzMVjMyeDdUKhbPLd3EqTS`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef87b98a-abc0-4c76-b042-b7fde92dd77d",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "251379ad-3086-4b02-a99f-c6a3459c7547",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 24,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "ef87b98a-abc0-4c76-b042-b7fde92dd77d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T07:52:16.662Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0146QpUwXYUn9stYDMicX3Bn`</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "251379ad-3086-4b02-a99f-c6a3459c7547",
  "isSidechain": false,
  "requestId": "req_011Cb3zTWU9dE5PTBB9QFazw",
  "type": "assistant",
  "uuid": "dfd6b0f8-c2e3-4b67-b648-a4bf4de51fb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EJSNUEETCgKmYD18bNRJo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 114,
      "cache_read_input_tokens": 26062,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 114,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 26062,
          "cache_creation_input_tokens": 114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 114
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-15T07:52:16.691Z_

<details><summary>↩ Tool result · `toolu_0146QpUwXYUn9stYDMicX3Bn`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfd6b0f8-c2e3-4b67-b648-a4bf4de51fb6",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "b9754d0b-a890-4e54-8333-c80006109af9",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 26,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "dfd6b0f8-c2e3-4b67-b648-a4bf4de51fb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-15T07:52:19.771Z_

Skill 文件不存在，直接进入审稿流程。先并行读取论文和搜索审稿标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9754d0b-a890-4e54-8333-c80006109af9",
  "isSidechain": false,
  "requestId": "req_011Cb3zTgRBr9qNoy2DdN8Np",
  "type": "assistant",
  "uuid": "8c7a9949-96b5-4186-b11c-450b1b533e0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYaZpxsxnQjBNgA2sLVNZA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 106,
      "cache_read_input_tokens": 26176,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 106,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 26176,
          "cache_creation_input_tokens": 106,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 106
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-15T07:52:21.090Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Kux9bo1ApDncpWaS63rgnZ`</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c7a9949-96b5-4186-b11c-450b1b533e0b",
  "isSidechain": false,
  "requestId": "req_011Cb3zTgRBr9qNoy2DdN8Np",
  "type": "assistant",
  "uuid": "835f7904-97d6-4dad-bc4f-0fb546828d31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYaZpxsxnQjBNgA2sLVNZA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 106,
      "cache_read_input_tokens": 26176,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 106,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 26176,
          "cache_creation_input_tokens": 106,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 106
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-15T07:52:21.094Z_

<details><summary>↩ Tool result · `toolu_01Kux9bo1ApDncpWaS63rgnZ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__pdf_to_images"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__review_reviewer_post_to_director"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__verify_references"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "835f7904-97d6-4dad-bc4f-0fb546828d31",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "c8ef8300-931a-461e-840a-939806400635",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "835f7904-97d6-4dad-bc4f-0fb546828d31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-15T07:52:24.713Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the tools loaded. Let me proceed with the review. I need to:

1. Read the paper (main.tex and section files)
2. Search for EMNLP/ACL ARR reviewer guidelines
3. Verify references

Let me start by reading the paper and searching for guidelines in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8ef8300-931a-461e-840a-939806400635",
  "isSidechain": false,
  "requestId": "req_011Cb3zU1HkathaB6umJ1g2N",
  "type": "assistant",
  "uuid": "b8f5f507-4ee0-40f5-9b1d-d53d8a8d9560",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QD7VrxzVefxi4zfkLHC6Qk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1662,
      "cache_read_input_tokens": 26282,
      "output_tokens": 445,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1662,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 445,
          "cache_read_input_tokens": 26282,
          "cache_creation_input_tokens": 1662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1662
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-15T07:52:25.327Z_

开始并行：读取论文主文件、搜索 ACL ARR 审稿标准、验证引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8f5f507-4ee0-40f5-9b1d-d53d8a8d9560",
  "isSidechain": false,
  "requestId": "req_011Cb3zU1HkathaB6umJ1g2N",
  "type": "assistant",
  "uuid": "a09984f5-420e-44a7-a344-7f99e1f0eb35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QD7VrxzVefxi4zfkLHC6Qk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1662,
      "cache_read_input_tokens": 26282,
      "output_tokens": 445,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1662,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 445,
          "cache_read_input_tokens": 26282,
          "cache_creation_input_tokens": 1662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1662
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-15T07:52:27.339Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C6VsUzciQPLgAEqqg77xC1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a09984f5-420e-44a7-a344-7f99e1f0eb35",
  "isSidechain": false,
  "requestId": "req_011Cb3zU1HkathaB6umJ1g2N",
  "type": "assistant",
  "uuid": "459830d4-00d3-4290-bc68-6a63cbaffc80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QD7VrxzVefxi4zfkLHC6Qk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1662,
      "cache_read_input_tokens": 26282,
      "output_tokens": 445,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1662,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 445,
          "cache_read_input_tokens": 26282,
          "cache_creation_input_tokens": 1662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1662
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-15T07:52:27.347Z_

<details><summary>↩ Tool result · `toolu_01C6VsUzciQPLgAEqqg77xC1`</summary>

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
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	No new human data was collected or annotated for this study.
42	
43	\bibliography{references}
44	
45	\appendix
46	\input{sections/appendix}
47	
48	\end{document}
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "459830d4-00d3-4290-bc68-6a63cbaffc80",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "9caccf58-ba5c-45e8-a361-c34fa8d56898",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\graphicspath{{figures/}}\n\n\\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\section*{Ethics Statement}\nAll experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).\nNo new human data was collected or annotated for this study.\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  },
  "sourceToolAssistantUUID": "459830d4-00d3-4290-bc68-6a63cbaffc80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T07:52:27.689Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mi4XE2ZjHJSG7ap5FiG1fr`</summary>

```json
{
  "query": "ACL ARR 2026 review form criteria scoring rubric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9caccf58-ba5c-45e8-a361-c34fa8d56898",
  "isSidechain": false,
  "requestId": "req_011Cb3zU1HkathaB6umJ1g2N",
  "type": "assistant",
  "uuid": "c88da60f-e0ec-4ed5-9bb2-7316e9f57b36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QD7VrxzVefxi4zfkLHC6Qk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1662,
      "cache_read_input_tokens": 26282,
      "output_tokens": 445,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1662,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 445,
          "cache_read_input_tokens": 26282,
          "cache_creation_input_tokens": 1662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1662
          },
          "type": "message"
        }
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

_source line 23 · 2026-05-15T07:52:28.233Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Uby37c8oD4rs1bBC7TLTBj`</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c88da60f-e0ec-4ed5-9bb2-7316e9f57b36",
  "isSidechain": false,
  "requestId": "req_011Cb3zU1HkathaB6umJ1g2N",
  "type": "assistant",
  "uuid": "37a62ab6-8de2-4eae-89e2-420b16f3a241",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QD7VrxzVefxi4zfkLHC6Qk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1662,
      "cache_read_input_tokens": 26282,
      "output_tokens": 445,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1662,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 445,
          "cache_read_input_tokens": 26282,
          "cache_creation_input_tokens": 1662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1662
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-15T07:52:28.265Z_

<details><summary>↩ Tool result · `toolu_01Uby37c8oD4rs1bBC7TLTBj`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37a62ab6-8de2-4eae-89e2-420b16f3a241",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "5d32cb20-8334-46a6-9546-7b766daece8b",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 27,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "37a62ab6-8de2-4eae-89e2-420b16f3a241",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T07:52:28.966Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01NviJqFKGPeWYJT8adV7XBz`</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d32cb20-8334-46a6-9546-7b766daece8b",
  "isSidechain": false,
  "requestId": "req_011Cb3zU1HkathaB6umJ1g2N",
  "type": "assistant",
  "uuid": "0e8728a3-eb18-494e-9bc6-20a56dc92898",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QD7VrxzVefxi4zfkLHC6Qk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1662,
      "cache_read_input_tokens": 26282,
      "output_tokens": 445,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1662,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 445,
          "cache_read_input_tokens": 26282,
          "cache_creation_input_tokens": 1662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1662
          },
          "type": "message"
        }
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2 (Round 1)  ### Venue 信息 - **Target**: EMNLP 2026 Findings (via ARR May 2026 cycle) - **Deadline**: 2026-05-25 - **页数限制**: 正文 8 页 + unlimited references - **模板**: A…",
  "leafUuid": "0e8728a3-eb18-494e-9bc6-20a56dc92898",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on structured self-consistency for IE",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74"
}
```

---

### Tool result

_source line 28 · 2026-05-15T07:52:35.228Z_

<details><summary>↩ Tool result · `toolu_01Mi4XE2ZjHJSG7ap5FiG1fr`</summary>

```text
Web search results for query: "ACL ARR 2026 review form criteria scoring rubric"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL ARR 2026 | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on my search results, here's information about the ACL ARR 2026 review form criteria and scoring rubric:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness and Excitement Scores

The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue, which is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact. Subjective preferences should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Overall Recommendation Rubric

The overall recommendation scores include:

- 5 = Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers).
- 2 = Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle.
- 1.5 = Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle.
- 1 = Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language).

## Key Evaluation Criteria

For Findings papers, the main criteria are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c88da60f-e0ec-4ed5-9bb2-7316e9f57b36",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "91fb15be-6358-4ccb-af1d-91406ebb80e4",
  "toolUseResult": {
    "query": "ACL ARR 2026 review form criteria scoring rubric",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X1f5zJyze7LM2Z42M2YJ1f",
        "content": [
          {
            "title": "Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "Main Conference - ACL 2026",
            "url": "https://2026.aclweb.org/calls/main_conference_papers/"
          },
          {
            "title": "ACL ARR 2026 | OpenReview",
            "url": "https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026"
          },
          {
            "title": "ACL ARR 2026 March | OpenReview",
            "url": "https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"
          },
          {
            "title": "Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/incentives2026"
          }
        ]
      },
      "Based on my search results, here's information about the ACL ARR 2026 review form criteria and scoring rubric:\n\n## Scoring System\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\n\n## Soundness and Excitement Scores\n\nThe Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue, which is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact. Subjective preferences should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.\n\n## Overall Recommendation Rubric\n\nThe overall recommendation scores include:\n\n- 5 = Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers).\n- 2 = Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle.\n- 1.5 = Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle.\n- 1 = Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language).\n\n## Key Evaluation Criteria\n\nFor Findings papers, the main criteria are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors."
    ],
    "durationSeconds": 7.533941651000001
  },
  "sourceToolAssistantUUID": "c88da60f-e0ec-4ed5-9bb2-7316e9f57b36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T07:53:31.536Z_

<details><summary>↩ Tool result · `toolu_01NviJqFKGPeWYJT8adV7XBz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 58, \"total_citations\": 84, \"unique_cited_keys\": 58, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 52, \"online_not_found\": 2, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"W-NUT Workshop at EMNLP 2017\"}, {\"key\": \"desai2020calibration\", \"type\": \"inproceedings\", \"title\": \"Calibration of Pre-trained Transformers\", \"authors\": \"Desai, Shrey and Durrett, Greg\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eikema2022sampling\", \"type\": \"inproceedings\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"authors\": \"Eikema, Bryan and Aziz, Wilker\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"fisch2021conformal\", \"type\": \"inproceedings\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"authors\": \"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\", \"year\": \"2021\", \"venue\": \"ICML 2021\"}, {\"key\": \"freitag2022high\", \"type\": \"article\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"authors\": \"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\", \"year\": \"2022\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"he2024uncertainty\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"authors\": \"He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2024\"}, {\"key\": \"fleiss1971agreement\", \"type\": \"article\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"authors\": \"Fleiss, Joseph L.\", \"year\": \"1971\", \"venue\": \"Psychological Bulletin\"}, {\"key\": \"gal2016dropout\", \"type\": \"inproceedings\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"authors\": \"Gal, Yarin and Ghahramani, Zoubin\", \"year\": \"2016\", \"venue\": \"ICML 2016\"}, {\"key\": \"geifman2017selective\", \"type\": \"inproceedings\", \"title\": \"Selective Classification for Deep Neural Networks\", \"authors\": \"Geifman, Yonatan and El-Yaniv, Ran\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"feng2025optimal\", \"type\": \"article\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"authors\": \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.12309\"}, {\"key\": \"geng2024confidence\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"guo2017calibration\", \"type\": \"inproceedings\", \"title\": \"On Calibration of Modern Neural Networks\", \"authors\": \"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\", \"year\": \"2017\", \"venue\": \"ICML 2017\"}, {\"key\": \"hobelsberger2025systematic\", \"type\": \"article\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"authors\": \"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.20460\"}, {\"key\": \"jaccard1901distribution\", \"type\": \"article\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"authors\": \"Jaccard, Paul\", \"year\": \"1901\", \"venue\": \"Bulletin de la Société Vaudoise des Sciences Naturelles\"}, {\"key\": \"josifoski2022genie\", \"type\": \"inproceedings\", \"title\": \"GenIE: Generative Information Extraction\", \"authors\": \"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kang2025selfcertainty\", \"type\": \"inproceedings\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"authors\": \"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"kim2024verifiner\", \"type\": \"inproceedings\", \"title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"authors\": \"Kim, Seoyeon and Seo, Kwangwook and Chae, Hyungjoo and Yeo, Jinyoung and Lee, Do...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"kim2026reasc\", \"type\": \"inproceedings\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"authors\": \"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\", \"year\": \"2026\", \"venue\": \"ACL 2026\"}, {\"key\": \"kossen2024semantic\", \"type\": \"article\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"authors\": \"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.15927\"}, {\"key\": \"li2025llms\", \"type\": \"article\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"authors\": \"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.04104\"}, {\"key\": \"kuhn2023semantic\", \"type\": \"inproceedings\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"authors\": \"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"malinin2021uncertainty\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"authors\": \"Malinin, Andrey and Gales, Mark\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"type\": \"inproceedings\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"authors\": \"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"li2023codeie\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lightman2024verify\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"luan2018scierc\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"authors\": \"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"manakul2023selfcheckgpt\", \"type\": \"inproceedings\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"authors\": \"Manakul, Potsawee and Liusie, Adian and Gales, Mark\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"nedellec2026consistency\", \"type\": \"article\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\", \"authors\": \"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\", \"year\": \"2026\", \"venue\": \"Genomics \\\\& Informatics\"}, {\"key\": \"oh2025latentsc\", \"type\": \"article\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"authors\": \"Oh, Jungsuk and Lee, Jay-Yoon\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.18395\"}, {\"key\": \"sainz2024gollie\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"shelmanov2021active\", \"type\": \"inproceedings\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"authors\": \"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 16th Conference of the European Chapter of the Association fo...\"}, {\"key\": \"snell2024scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"authors\": \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\", \"year\": \"2024\", \"venue\": \"ICLR 2025\"}, {\"key\": \"taubenfeld2025cisc\", \"type\": \"inproceedings\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"authors\": \"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"thirukovalluru2024atomic\", \"type\": \"inproceedings\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"authors\": \"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"tjongkimsang2003conll\", \"type\": \"inproceedings\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"authors\": \"Sang, Erik F. Tjong Kim and Meulder, Fien De\", \"year\": \"2003\", \"venue\": \"CoNLL 2003\"}, {\"key\": \"vashurin2025cocoa\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"authors\": \"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"wadhwa2023revisiting\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"wang2023instructuie\", \"type\": \"article\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"authors\": \"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.08085\"}, {\"key\": \"wang2023selfconsistency\", \"type\": \"inproceedings\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"authors\": \"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"wang2025make\", \"type\": \"inproceedings\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"authors\": \"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2025\"}, {\"key\": \"wang2024mathshepherd\", \"type\": \"inproceedings\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"authors\": \"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\", \"year\": \"2024\", \"venue\": \"ACL 2024\"}, {\"key\": \"wang2025rankedvoting\", \"type\": \"inproceedings\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"authors\": \"Wang, Weiqin and Wang, Yile and Huang, Hui\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"wen2025know\", \"type\": \"article\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"authors\": \"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\", \"year\": \"2025\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"willard2023guided\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, Rémi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"xia2025survey\", \"type\": \"inproceedings\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"authors\": \"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"xiao2019uncertainty\", \"type\": \"article\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"authors\": \"Xiao, Yijun and Wang, William Yang\", \"year\": \"2019\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"zhang2023ener\", \"type\": \"inproceedings\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"authors\": \"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2023\"}, {\"key\": \"zheng2024llamafactory\", \"type\": \"inproceedings\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"authors\": \"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"zhou2024uniner\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"xiong2024llm\", \"type\": \"inproceedings\", \"title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"authors\": \"Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Ju...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"muller2021understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"authors\": \"M\\\\\\\"uller, Mathias and Sennrich, Rico\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"ye2025uncertainty\", \"type\": \"inproceedings\", \"title\": \"Do LLMs Estimate Uncertainty Well in Instruction Following?\", \"authors\": \"Ye, Juyeon and Park, Jinheon and Kim, Seongjun and Yun, Se-Young\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}], \"tex_citations\": [{\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 4, \"command\": \"citealp\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/introduction.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/introduction.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/introduction.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"thirukovalluru2024atomic\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"manakul2023selfcheckgpt\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kim2026reasc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"wang2025rankedvoting\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"oh2025latentsc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"feng2025optimal\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"wang2025make\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"li2025llms\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"vashurin2025cocoa\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"zhou2024uniner\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"sainz2024gollie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"josifoski2022genie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"li2023codeie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wadhwa2023revisiting\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wang2023instructuie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"geng2024confidence\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"wen2025know\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xia2025survey\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"hobelsberger2025systematic\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xiong2024llm\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"ye2025uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"malinin2021uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 22, \"command\": \"citet\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"kossen2024semantic\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"citet\"}, {\"key\": \"kadavath2022language\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"he2024uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"citet\"}, {\"key\": \"guo2017calibration\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"desai2020calibration\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"gal2016dropout\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"xiao2019uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"shelmanov2021active\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"zhang2023ener\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"kim2024verifiner\", \"file\": \"sections/related_work.tex\", \"line\": 27, \"command\": \"citet\"}, {\"key\": \"fisch2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"angelopoulos2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"lightman2024verify\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"wang2024mathshepherd\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/related_work.tex\", \"line\": 29, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/related_work.tex\", \"line\": 29, \"command\": \"cite\"}, {\"key\": \"geifman2017selective\", \"file\": \"sections/related_work.tex\", \"line\": 30, \"command\": \"cite\"}, {\"key\": \"culotta2004confidence\", \"file\": \"sections/related_work.tex\", \"line\": 30, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/method.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fleiss1971agreement\", \"file\": \"sections/method.tex\", \"line\": 34, \"command\": \"citet\"}, {\"key\": \"jaccard1901distribution\", \"file\": \"sections/method.tex\", \"line\": 43, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/experiments.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/experiments.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"zheng2024llamafactory\", \"file\": \"sections/experiments.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/experiments.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/experiments.tex\", \"line\": 64, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/experiments.tex\", \"line\": 140, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/experiments.tex\", \"line\": 140, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/experiments.tex\", \"line\": 140, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/discussion.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/discussion.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/discussion.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/discussion.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/appendix.tex\", \"line\": 185, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/appendix.tex\", \"line\": 185, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/appendix.tex\", \"line\": 368, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"angelopoulos2021conformal\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"brown2024monkeys\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024usc\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Self-Consistency for Large Language Model Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021verifiers\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culotta2004confidence\", \"title\": \"Confidence Estimation for Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence estimation for information extraction\", \"matched_year\": \"2004\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"derczynski2017wnut\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"desai2020calibration\", \"title\": \"Calibration of Pre-trained Transformers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calibration of Pre-trained Transformers\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eikema2022sampling\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fisch2021conformal\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-shot Conformal Prediction with Auxiliary Tasks\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"freitag2022high\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"he2024uncertainty\", \"title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fleiss1971agreement\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring nominal scale agreement among many raters.\", \"matched_year\": \"1971\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gal2016dropout\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"geifman2017selective\", \"title\": \"Selective Classification for Deep Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Selective Classification for Deep Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feng2025optimal\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=feng vs api=austin\"], \"note\": \"\"}, {\"key\": \"geng2024confidence\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2017calibration\", \"title\": \"On Calibration of Modern Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Calibration of Modern Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hobelsberger2025systematic\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.236, \"matched_title\": \"A new criterion for assessing discriminant validity in variance-based structural equation modeling\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.24 below threshold 0.82\"}, {\"key\": \"jaccard1901distribution\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"matched_year\": \"1901\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"josifoski2022genie\", \"title\": \"GenIE: Generative Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GenIE: Generative Information Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2025selfcertainty\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2024verifiner\", \"title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2026reasc\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kossen2024semantic\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025llms\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuhn2023semantic\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"malinin2021uncertainty\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023codeie\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lightman2024verify\", \"title\": \"Let's Verify Step by Step\", \"status\": \"not_found\", \"confidence\": 0.246, \"matched_title\": \"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"luan2018scierc\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"manakul2023selfcheckgpt\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nedellec2026consistency\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oh2025latentsc\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sainz2024gollie\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shelmanov2021active\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"snell2024scaling\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=snell vs api=charlie\"], \"note\": \"\"}, {\"key\": \"taubenfeld2025cisc\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence Improves Self-Consistency in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thirukovalluru2024atomic\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tjongkimsang2003conll\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"matched_year\": \"2003\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vashurin2025cocoa\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa2023revisiting\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023instructuie\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023selfconsistency\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025make\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2024mathshepherd\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025rankedvoting\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wen2025know\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023guided\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2025survey\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiao2019uncertainty\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2023ener\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zheng2024llamafactory\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024uniner\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiong2024llm\", \"title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"muller2021understanding\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"matched_year\": \"2021\", \"mismatch_fields\": [\"first_author: bib=m\\\\\\\"uller vs api=müller\"], \"note\": \"\"}, {\"key\": \"ye2025uncertainty\", \"title\": \"Do LLMs Estimate Uncertainty Well in Instruction Following?\", \"status\": \"mismatch\", \"confidence\": 0.983, \"matched_title\": \"Do LLMs estimate uncertainty well in instruction-following?\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=ye vs api=heo\"], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e8728a3-eb18-494e-9bc6-20a56dc92898",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "76adfa82-48ec-4afb-9c3f-8e18bd3de14c",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 58, \\\"total_citations\\\": 84, \\\"unique_cited_keys\\\": 58, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 52, \\\"online_not_found\\\": 2, \\\"online_mismatch\\\": 4}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"authors\\\": \\\"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"ICLR 2021\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"authors\\\": \\\"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2407.21787\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"authors\\\": \\\"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint (ICML 2024 Workshop ICL)\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"authors\\\": \\\"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2110.14168\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"authors\\\": \\\"Culotta, Aron and McCallum, Andrew\\\", \\\"year\\\": \\\"2004\\\", \\\"venue\\\": \\\"HLT-NAACL 2004\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"authors\\\": \\\"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"W-NUT Workshop at EMNLP 2017\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"authors\\\": \\\"Desai, Shrey and Durrett, Greg\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"authors\\\": \\\"Eikema, Bryan and Aziz, Wilker\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Few-Shot Conformal Prediction with Auxiliary Tasks\\\", \\\"authors\\\": \\\"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"ICML 2021\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"authors\\\": \\\"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"he2024uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\\\", \\\"authors\\\": \\\"He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL 2024\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"authors\\\": \\\"Fleiss, Joseph L.\\\", \\\"year\\\": \\\"1971\\\", \\\"venue\\\": \\\"Psychological Bulletin\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"authors\\\": \\\"Gal, Yarin and Ghahramani, Zoubin\\\", \\\"year\\\": \\\"2016\\\", \\\"venue\\\": \\\"ICML 2016\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"authors\\\": \\\"Geifman, Yonatan and El-Yaniv, Ran\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"NeurIPS 2017\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2511.12309\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"authors\\\": \\\"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"authors\\\": \\\"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"ICML 2017\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"authors\\\": \\\"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2510.20460\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"authors\\\": \\\"Jaccard, Paul\\\", \\\"year\\\": \\\"1901\\\", \\\"venue\\\": \\\"Bulletin de la Société Vaudoise des Sciences Naturelles\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"authors\\\": \\\"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"authors\\\": \\\"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2207.05221\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"authors\\\": \\\"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"kim2024verifiner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Kim, Seoyeon and Seo, Kwangwook and Chae, Hyungjoo and Yeo, Jinyoung and Lee, Do...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"authors\\\": \\\"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"ACL 2026\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"authors\\\": \\\"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2406.15927\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"authors\\\": \\\"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.04104\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"authors\\\": \\\"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"authors\\\": \\\"Malinin, Andrey and Gales, Mark\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"authors\\\": \\\"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"NeurIPS 2017\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"authors\\\": \\\"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"authors\\\": \\\"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"authors\\\": \\\"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"authors\\\": \\\"Manakul, Potsawee and Liusie, Adian and Gales, Mark\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\\\", \\\"authors\\\": \\\"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Genomics \\\\\\\\& Informatics\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"authors\\\": \\\"Oh, Jungsuk and Lee, Jay-Yoon\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.18395\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"authors\\\": \\\"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"authors\\\": \\\"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 16th Conference of the European Chapter of the Association fo...\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"authors\\\": \\\"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2025\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"authors\\\": \\\"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"authors\\\": \\\"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"authors\\\": \\\"Sang, Erik F. Tjong Kim and Meulder, Fien De\\\", \\\"year\\\": \\\"2003\\\", \\\"venue\\\": \\\"CoNLL 2003\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"authors\\\": \\\"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"authors\\\": \\\"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"authors\\\": \\\"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2304.08085\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"authors\\\": \\\"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"authors\\\": \\\"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL 2025\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"authors\\\": \\\"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ACL 2024\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"authors\\\": \\\"Wang, Weiqin and Wang, Yile and Huang, Hui\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"authors\\\": \\\"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"authors\\\": \\\"Willard, Brandon T. and Louf, Rémi\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2307.09702\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"authors\\\": \\\"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"authors\\\": \\\"Xiao, Yijun and Wang, William Yang\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2023\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"authors\\\": \\\"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\\", \\\"authors\\\": \\\"Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Ju...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"authors\\\": \\\"M\\\\\\\\\\\\\\\"uller, Mathias and Sennrich, Rico\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"ye2025uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Do LLMs Estimate Uncertainty Well in Instruction Following?\\\", \\\"authors\\\": \\\"Ye, Juyeon and Park, Jinheon and Kim, Seongjun and Yun, Se-Young\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citealp\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"ye2025uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"he2024uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2024verifiner\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 34, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 43, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 64, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 140, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 140, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 140, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 185, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 185, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 368, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence estimation for information extraction\\\", \\\"matched_year\\\": \\\"2004\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"title\\\": \\\"Few-Shot Conformal Prediction with Auxiliary Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Few-shot Conformal Prediction with Auxiliary Tasks\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"he2024uncertainty\\\", \\\"title\\\": \\\"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"matched_year\\\": \\\"1971\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"matched_year\\\": \\\"2015\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=feng vs api=austin\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.236, \\\"matched_title\\\": \\\"A new criterion for assessing discriminant validity in variance-based structural equation modeling\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.24 below threshold 0.82\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"matched_year\\\": \\\"1901\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2024verifiner\\\", \\\"title\\\": \\\"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.246, \\\"matched_title\\\": \\\"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=snell vs api=charlie\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2003\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"title\\\": \\\"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=m\\\\\\\\\\\\\\\"uller vs api=müller\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ye2025uncertainty\\\", \\\"title\\\": \\\"Do LLMs Estimate Uncertainty Well in Instruction Following?\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 0.983, \\\"matched_title\\\": \\\"Do LLMs estimate uncertainty well in instruction-following?\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=ye vs api=heo\\\"], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 58, \"total_citations\": 84, \"unique_cited_keys\": 58, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 52, \"online_not_found\": 2, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"W-NUT Workshop at EMNLP 2017\"}, {\"key\": \"desai2020calibration\", \"type\": \"inproceedings\", \"title\": \"Calibration of Pre-trained Transformers\", \"authors\": \"Desai, Shrey and Durrett, Greg\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eikema2022sampling\", \"type\": \"inproceedings\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"authors\": \"Eikema, Bryan and Aziz, Wilker\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"fisch2021conformal\", \"type\": \"inproceedings\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"authors\": \"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\", \"year\": \"2021\", \"venue\": \"ICML 2021\"}, {\"key\": \"freitag2022high\", \"type\": \"article\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"authors\": \"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\", \"year\": \"2022\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"he2024uncertainty\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"authors\": \"He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2024\"}, {\"key\": \"fleiss1971agreement\", \"type\": \"article\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"authors\": \"Fleiss, Joseph L.\", \"year\": \"1971\", \"venue\": \"Psychological Bulletin\"}, {\"key\": \"gal2016dropout\", \"type\": \"inproceedings\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"authors\": \"Gal, Yarin and Ghahramani, Zoubin\", \"year\": \"2016\", \"venue\": \"ICML 2016\"}, {\"key\": \"geifman2017selective\", \"type\": \"inproceedings\", \"title\": \"Selective Classification for Deep Neural Networks\", \"authors\": \"Geifman, Yonatan and El-Yaniv, Ran\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"feng2025optimal\", \"type\": \"article\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"authors\": \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.12309\"}, {\"key\": \"geng2024confidence\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"guo2017calibration\", \"type\": \"inproceedings\", \"title\": \"On Calibration of Modern Neural Networks\", \"authors\": \"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\", \"year\": \"2017\", \"venue\": \"ICML 2017\"}, {\"key\": \"hobelsberger2025systematic\", \"type\": \"article\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"authors\": \"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.20460\"}, {\"key\": \"jaccard1901distribution\", \"type\": \"article\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"authors\": \"Jaccard, Paul\", \"year\": \"1901\", \"venue\": \"Bulletin de la Société Vaudoise des Sciences Naturelles\"}, {\"key\": \"josifoski2022genie\", \"type\": \"inproceedings\", \"title\": \"GenIE: Generative Information Extraction\", \"authors\": \"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kang2025selfcertainty\", \"type\": \"inproceedings\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"authors\": \"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"kim2024verifiner\", \"type\": \"inproceedings\", \"title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"authors\": \"Kim, Seoyeon and Seo, Kwangwook and Chae, Hyungjoo and Yeo, Jinyoung and Lee, Do...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"kim2026reasc\", \"type\": \"inproceedings\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"authors\": \"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\", \"year\": \"2026\", \"venue\": \"ACL 2026\"}, {\"key\": \"kossen2024semantic\", \"type\": \"article\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"authors\": \"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.15927\"}, {\"key\": \"li2025llms\", \"type\": \"article\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"authors\": \"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.04104\"}, {\"key\": \"kuhn2023semantic\", \"type\": \"inproceedings\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"authors\": \"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"malinin2021uncertainty\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"authors\": \"Malinin, Andrey and Gales, Mark\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"type\": \"inproceedings\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"authors\": \"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"li2023codeie\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lightman2024verify\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"luan2018scierc\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"authors\": \"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"manakul2023selfcheckgpt\", \"type\": \"inproceedings\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"authors\": \"Manakul, Potsawee and Liusie, Adian and Gales, Mark\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"nedellec2026consistency\", \"type\": \"article\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\", \"authors\": \"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\", \"year\": \"2026\", \"venue\": \"Genomics \\\\& Informatics\"}, {\"key\": \"oh2025latentsc\", \"type\": \"article\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"authors\": \"Oh, Jungsuk and Lee, Jay-Yoon\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.18395\"}, {\"key\": \"sainz2024gollie\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"shelmanov2021active\", \"type\": \"inproceedings\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"authors\": \"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 16th Conference of the European Chapter of the Association fo...\"}, {\"key\": \"snell2024scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"authors\": \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\", \"year\": \"2024\", \"venue\": \"ICLR 2025\"}, {\"key\": \"taubenfeld2025cisc\", \"type\": \"inproceedings\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"authors\": \"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"thirukovalluru2024atomic\", \"type\": \"inproceedings\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"authors\": \"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"tjongkimsang2003conll\", \"type\": \"inproceedings\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"authors\": \"Sang, Erik F. Tjong Kim and Meulder, Fien De\", \"year\": \"2003\", \"venue\": \"CoNLL 2003\"}, {\"key\": \"vashurin2025cocoa\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"authors\": \"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"wadhwa2023revisiting\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"wang2023instructuie\", \"type\": \"article\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"authors\": \"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.08085\"}, {\"key\": \"wang2023selfconsistency\", \"type\": \"inproceedings\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"authors\": \"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"wang2025make\", \"type\": \"inproceedings\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"authors\": \"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2025\"}, {\"key\": \"wang2024mathshepherd\", \"type\": \"inproceedings\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"authors\": \"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\", \"year\": \"2024\", \"venue\": \"ACL 2024\"}, {\"key\": \"wang2025rankedvoting\", \"type\": \"inproceedings\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"authors\": \"Wang, Weiqin and Wang, Yile and Huang, Hui\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"wen2025know\", \"type\": \"article\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"authors\": \"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\", \"year\": \"2025\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"willard2023guided\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, Rémi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"xia2025survey\", \"type\": \"inproceedings\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"authors\": \"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"xiao2019uncertainty\", \"type\": \"article\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"authors\": \"Xiao, Yijun and Wang, William Yang\", \"year\": \"2019\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"zhang2023ener\", \"type\": \"inproceedings\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"authors\": \"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2023\"}, {\"key\": \"zheng2024llamafactory\", \"type\": \"inproceedings\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"authors\": \"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"zhou2024uniner\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"xiong2024llm\", \"type\": \"inproceedings\", \"title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"authors\": \"Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Ju...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"muller2021understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"authors\": \"M\\\\\\\"uller, Mathias and Sennrich, Rico\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"ye2025uncertainty\", \"type\": \"inproceedings\", \"title\": \"Do LLMs Estimate Uncertainty Well in Instruction Following?\", \"authors\": \"Ye, Juyeon and Park, Jinheon and Kim, Seongjun and Yun, Se-Young\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}], \"tex_citations\": [{\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 4, \"command\": \"citealp\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/introduction.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/introduction.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/introduction.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"thirukovalluru2024atomic\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"manakul2023selfcheckgpt\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kim2026reasc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"wang2025rankedvoting\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"oh2025latentsc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"feng2025optimal\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"wang2025make\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"li2025llms\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"vashurin2025cocoa\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"zhou2024uniner\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"sainz2024gollie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"josifoski2022genie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"li2023codeie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wadhwa2023revisiting\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wang2023instructuie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"geng2024confidence\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"wen2025know\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xia2025survey\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"hobelsberger2025systematic\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xiong2024llm\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"ye2025uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"malinin2021uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 22, \"command\": \"citet\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"kossen2024semantic\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"citet\"}, {\"key\": \"kadavath2022language\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"he2024uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"citet\"}, {\"key\": \"guo2017calibration\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"desai2020calibration\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"gal2016dropout\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"xiao2019uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"shelmanov2021active\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"zhang2023ener\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"kim2024verifiner\", \"file\": \"sections/related_work.tex\", \"line\": 27, \"command\": \"citet\"}, {\"key\": \"fisch2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"angelopoulos2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"lightman2024verify\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"wang2024mathshepherd\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/related_work.tex\", \"line\": 29, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/related_work.tex\", \"line\": 29, \"command\": \"cite\"}, {\"key\": \"geifman2017selective\", \"file\": \"sections/related_work.tex\", \"line\": 30, \"command\": \"cite\"}, {\"key\": \"culotta2004confidence\", \"file\": \"sections/related_work.tex\", \"line\": 30, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/method.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fleiss1971agreement\", \"file\": \"sections/method.tex\", \"line\": 34, \"command\": \"citet\"}, {\"key\": \"jaccard1901distribution\", \"file\": \"sections/method.tex\", \"line\": 43, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/experiments.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/experiments.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"zheng2024llamafactory\", \"file\": \"sections/experiments.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/experiments.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/experiments.tex\", \"line\": 64, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/experiments.tex\", \"line\": 140, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/experiments.tex\", \"line\": 140, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/experiments.tex\", \"line\": 140, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/discussion.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/discussion.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/discussion.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/discussion.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/appendix.tex\", \"line\": 185, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/appendix.tex\", \"line\": 185, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/appendix.tex\", \"line\": 368, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"angelopoulos2021conformal\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"brown2024monkeys\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024usc\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Self-Consistency for Large Language Model Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021verifiers\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culotta2004confidence\", \"title\": \"Confidence Estimation for Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence estimation for information extraction\", \"matched_year\": \"2004\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"derczynski2017wnut\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"desai2020calibration\", \"title\": \"Calibration of Pre-trained Transformers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calibration of Pre-trained Transformers\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eikema2022sampling\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fisch2021conformal\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-shot Conformal Prediction with Auxiliary Tasks\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"freitag2022high\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"he2024uncertainty\", \"title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fleiss1971agreement\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring nominal scale agreement among many raters.\", \"matched_year\": \"1971\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gal2016dropout\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"geifman2017selective\", \"title\": \"Selective Classification for Deep Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Selective Classification for Deep Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feng2025optimal\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=feng vs api=austin\"], \"note\": \"\"}, {\"key\": \"geng2024confidence\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2017calibration\", \"title\": \"On Calibration of Modern Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Calibration of Modern Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hobelsberger2025systematic\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.236, \"matched_title\": \"A new criterion for assessing discriminant validity in variance-based structural equation modeling\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.24 below threshold 0.82\"}, {\"key\": \"jaccard1901distribution\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"matched_year\": \"1901\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"josifoski2022genie\", \"title\": \"GenIE: Generative Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GenIE: Generative Information Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2025selfcertainty\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2024verifiner\", \"title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2026reasc\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kossen2024semantic\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025llms\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuhn2023semantic\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"malinin2021uncertainty\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023codeie\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lightman2024verify\", \"title\": \"Let's Verify Step by Step\", \"status\": \"not_found\", \"confidence\": 0.246, \"matched_title\": \"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"luan2018scierc\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"manakul2023selfcheckgpt\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nedellec2026consistency\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oh2025latentsc\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sainz2024gollie\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shelmanov2021active\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"snell2024scaling\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=snell vs api=charlie\"], \"note\": \"\"}, {\"key\": \"taubenfeld2025cisc\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence Improves Self-Consistency in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thirukovalluru2024atomic\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tjongkimsang2003conll\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"matched_year\": \"2003\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vashurin2025cocoa\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa2023revisiting\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023instructuie\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023selfconsistency\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025make\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2024mathshepherd\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025rankedvoting\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wen2025know\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023guided\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2025survey\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiao2019uncertainty\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2023ener\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zheng2024llamafactory\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024uniner\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiong2024llm\", \"title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"muller2021understanding\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"matched_year\": \"2021\", \"mismatch_fields\": [\"first_author: bib=m\\\\\\\"uller vs api=müller\"], \"note\": \"\"}, {\"key\": \"ye2025uncertainty\", \"title\": \"Do LLMs Estimate Uncertainty Well in Instruction Following?\", \"status\": \"mismatch\", \"confidence\": 0.983, \"matched_title\": \"Do LLMs estimate uncertainty well in instruction-following?\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=ye vs api=heo\"], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "0e8728a3-eb18-494e-9bc6-20a56dc92898",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-15T07:53:31.544Z_

```json
{
  "parentUuid": "76adfa82-48ec-4afb-9c3f-8e18bd3de14c",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "bd130e9c-9365-4f95-91ef-3292c509be01",
  "timestamp": "2026-05-15T07:53:31.544Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2 (Round 1)  ### Venue 信息 - **Target**: EMNLP 2026 Findings (via ARR May 2026 cycle) - **Deadline**: 2026-05-25 - **页数限制**: 正文 8 页 + unlimited references - **模板**: A…",
  "leafUuid": "bd130e9c-9365-4f95-91ef-3292c509be01",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on structured self-consistency for IE",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74"
}
```

---

### Assistant

_source line 33 · 2026-05-15T07:53:35.940Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the main.tex structure. Now I need to read all the section files. Let me also fetch the ACL ARR review form page for exact criteria. The sections are in a `sections/` subdirectory. Let me find them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd130e9c-9365-4f95-91ef-3292c509be01",
  "isSidechain": false,
  "requestId": "req_011Cb3zZC52s4pfdi1C6L3WR",
  "type": "assistant",
  "uuid": "89a2b590-33c1-477d-9769-c8f434db55dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yUf9zAJUS27cFZTGzw55f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18563,
      "cache_read_input_tokens": 27944,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 27944,
          "cache_creation_input_tokens": 18563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18563
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-15T07:53:36.870Z_

引用验证完成，论文结构已确认。现在读取所有 section 文件并获取 ARR review form 的完整评分标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89a2b590-33c1-477d-9769-c8f434db55dc",
  "isSidechain": false,
  "requestId": "req_011Cb3zZC52s4pfdi1C6L3WR",
  "type": "assistant",
  "uuid": "1a1c1b4c-fdc0-4280-b283-b9c68d1e8d86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yUf9zAJUS27cFZTGzw55f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18563,
      "cache_read_input_tokens": 27944,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 27944,
          "cache_creation_input_tokens": 18563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18563
          },
          "type": "message"
        }
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

_source line 35 · 2026-05-15T07:53:38.439Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011NxRiEASRLGHMfeKJPiY7F`</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a1c1b4c-fdc0-4280-b283-b9c68d1e8d86",
  "isSidechain": false,
  "requestId": "req_011Cb3zZC52s4pfdi1C6L3WR",
  "type": "assistant",
  "uuid": "867bdf81-28ef-4b73-a45c-40aa64f1237c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yUf9zAJUS27cFZTGzw55f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18563,
      "cache_read_input_tokens": 27944,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 27944,
          "cache_creation_input_tokens": 18563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18563
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-15T07:53:38.655Z_

<details><summary>↩ Tool result · `toolu_01NvXctodaiwP5Y5TsLNFJoE`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "278ed66b-3b19-4535-a699-22ece47f9f15",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "400929c8-20ad-4d90-8d44-12014bcd80a2",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "278ed66b-3b19-4535-a699-22ece47f9f15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T07:53:38.473Z_

<details><summary>↩ Tool result · `toolu_011NxRiEASRLGHMfeKJPiY7F`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "867bdf81-28ef-4b73-a45c-40aa64f1237c",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "098cde0a-4b1d-4a5f-907e-b323687cee0c",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
    ],
    "durationMs": 25,
    "numFiles": 9,
    "truncated": false
  },
  "sourceToolAssistantUUID": "867bdf81-28ef-4b73-a45c-40aa64f1237c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T07:53:38.651Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NvXctodaiwP5Y5TsLNFJoE`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "098cde0a-4b1d-4a5f-907e-b323687cee0c",
  "isSidechain": false,
  "requestId": "req_011Cb3zZC52s4pfdi1C6L3WR",
  "type": "assistant",
  "uuid": "278ed66b-3b19-4535-a699-22ece47f9f15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yUf9zAJUS27cFZTGzw55f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18563,
      "cache_read_input_tokens": 27944,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 27944,
          "cache_creation_input_tokens": 18563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18563
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-15T07:53:40.890Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q38KC1qafMzaMhfHwZDhb2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "400929c8-20ad-4d90-8d44-12014bcd80a2",
  "isSidechain": false,
  "requestId": "req_011Cb3zZii275vg2J3MEsM7Y",
  "type": "assistant",
  "uuid": "e43d9348-fe2b-433f-822c-5173b28b7fef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019b8CkDYUCGKeLPnpSLUt2b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 46507,
      "output_tokens": 796,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 796,
          "cache_read_input_tokens": 46507,
          "cache_creation_input_tokens": 1189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1189
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-15T07:53:40.904Z_

<details><summary>↩ Tool result · `toolu_01Q38KC1qafMzaMhfHwZDhb2`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC, preliminary) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	For quality estimation, the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match), with ranking and classification favoring different signals across task complexity.
5	However, this strong estimation does not translate into selection gains: four of five signals are instance-level by construction, and log-probability---the only per-sample signal---also fails to outperform greedy decoding on SciERC ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
6	We term this the \textit{correlation-selection gap}.
7	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks---with consistent ordering direction across models but model-dependent magnitude; when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation.
8	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e43d9348-fe2b-433f-822c-5173b28b7fef",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "bfddebc9-b6c6-4283-bdd7-6fa2a2e4127c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nTest-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.\nWe systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC, preliminary) with two model families (Qwen3-8B, LLaMA-3.1-8B).\nFor quality estimation, the strongest signals achieve $\\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match), with ranking and classification favoring different signals across task complexity.\nHowever, this strong estimation does not translate into selection gains: four of five signals are instance-level by construction, and log-probability---the only per-sample signal---also fails to outperform greedy decoding on SciERC ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.\nWe term this the \\textit{correlation-selection gap}.\nSignal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks---with consistent ordering direction across models but model-dependent magnitude; when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation.\nThese results reframe consistency signals as quality estimators rather than output selectors for structured IE.\n\\end{abstract}\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "e43d9348-fe2b-433f-822c-5173b28b7fef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T07:53:41.387Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DmGTKx8BkU3Lmk3dhpaLLz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfddebc9-b6c6-4283-bdd7-6fa2a2e4127c",
  "isSidechain": false,
  "requestId": "req_011Cb3zZii275vg2J3MEsM7Y",
  "type": "assistant",
  "uuid": "39841f44-7812-45b4-a057-5ccf341729dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019b8CkDYUCGKeLPnpSLUt2b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 46507,
      "output_tokens": 796,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 796,
          "cache_read_input_tokens": 46507,
          "cache_creation_input_tokens": 1189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1189
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-15T07:53:41.391Z_

<details><summary>↩ Tool result · `toolu_01DmGTKx8BkU3Lmk3dhpaLLz`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
16	The most relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, leaving open several questions that motivate our work: (i)~whether structural matching improves on their surface-level approach (which they acknowledge ``overlooks semantically consistent outputs''), (ii)~whether quality estimation translates to best-of-$N$ selection, and (iii)~whether findings generalize across a difficulty gradient beyond a single domain.
17	No existing work compares confidence signals from multiple families---surface-level, structural consistency, and probabilistic---for both quality estimation and sample selection in generative structured IE.
18	
19	Our central finding is that consistency-based signals are effective quality estimators but poor sample selectors for structured IE.
20	Entity voting achieves $\rho{=}0.38$ on SciERC NER and exact match leads AUROC${=}0.75$, both practically useful for quality-aware routing.
21	Yet we find no statistically significant evidence that any signal surpasses greedy decoding on best-of-$N$ selection ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
22	We term this the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): instance-level signals predict \textit{which inputs} are hard, not \textit{which output} is best.
23	This gap is not obvious \textit{a priori}: minimum Bayes risk (MBR) decoding---selecting the sample maximizing expected utility against the candidate set---succeeds in machine translation \cite{eikema2022sampling, freitag2022high, muller2021understanding}.
24	Our consensus-proximity strategy (\S\ref{sec:evaluation}) instantiates MBR with structural utility functions; that this approach fails for IE is a non-trivial finding that we trace to the instance-level nature of structural utility (\S\ref{sec:discussion}).
25	
26	\begin{figure*}[t]
27	\centering
28	\includegraphics[width=\textwidth]{fig_overview}
29	\caption{The correlation-selection gap. Left: consistency signals (here entity voting) predict instance-level quality---high agreement correlates with high F1 ($\rho{\approx}0.38$, AUROC${\approx}0.69$). Right: the same instance-level signal assigns identical scores to all $N$ candidates from a given input, precluding sample selection; consensus-proximity selection (choosing the sample closest to the consensus output) does not recover per-sample discrimination. No signal significantly outperforms greedy on either task ($p{=}0.39$ for NER logprob; Table~\ref{tab:selection}).}
30	\label{fig:overview}
31	\end{figure*}
32	
33	We systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
34	
35	Our contributions are as follows:
36	\begin{enumerate}
37	    \item \textbf{A systematic multi-family comparison of confidence signals for generative IE.}
38	    We evaluate five signals from three families on quality estimation for NER and RE.
39	    Entity voting achieves the strongest $\rho{=}0.38$ while exact match leads AUROC${=}0.75$; signal rankings depend on both task complexity and evaluation metric, with structural signals leading rank correlation on complex schemas (SciERC) and surface signals leading on simpler tasks (CoNLL)---an ordering directionally consistent across model families, though with model-dependent magnitude.
40	
41	    \item \textbf{Identification of the correlation-selection gap.}
42	    Four of five signals are instance-level by construction, making selection failure expected; the empirical finding is that log-probability---the only per-sample signal---also fails ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom on SciERC, where output diversity is substantial (39--43\% unique outputs).
43	    We trace this to the instance-level nature of consistency signals and, for log-probability, to within-instance score compression under constrained decoding.
44	
45	    \item \textbf{Task-complexity boundary conditions.}
46	    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and when model capability is insufficient (WNUT-17, 52\% zero F1), inflated full-set correlations collapse on the conditional set---all signals converge toward weak or non-significant correlations once the zero/non-zero boundary is removed.
47	    While our NER findings are validated across three datasets of varying difficulty, our RE conclusions are based on a single benchmark (SciERC) and warrant further validation.
48	\end{enumerate}
49	
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39841f44-7812-45b4-a057-5ccf341729dd",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "26212e5c-f22f-42b2-880d-eb69e1d59462",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \\citealp{wang2023selfconsistency}).\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2024scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a fundamentally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \\textit{quality estimation} (which inputs does the model handle reliably?) and \\textit{sample selection} (which of $N$ outputs is best?).\nThese require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.\nSelf-consistency methods for discrete answers \\cite{wang2023selfconsistency, chen2024usc} and weighted variants \\cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\nThe most relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, leaving open several questions that motivate our work: (i)~whether structural matching improves on their surface-level approach (which they acknowledge ``overlooks semantically consistent outputs''), (ii)~whether quality estimation translates to best-of-$N$ selection, and (iii)~whether findings generalize across a difficulty gradient beyond a single domain.\nNo existing work compares confidence signals from multiple families---surface-level, structural consistency, and probabilistic---for both quality estimation and sample selection in generative structured IE.\n\nOur central finding is that consistency-based signals are effective quality estimators but poor sample selectors for structured IE.\nEntity voting achieves $\\rho{=}0.38$ on SciERC NER and exact match leads AUROC${=}0.75$, both practically useful for quality-aware routing.\nYet we find no statistically significant evidence that any signal surpasses greedy decoding on best-of-$N$ selection ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.\nWe term this the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): instance-level signals predict \\textit{which inputs} are hard, not \\textit{which output} is best.\nThis gap is not obvious \\textit{a priori}: minimum Bayes risk (MBR) decoding---selecting the sample maximizing expected utility against the candidate set---succeeds in machine translation \\cite{eikema2022sampling, freitag2022high, muller2021understanding}.\nOur consensus-proximity strategy (\\S\\ref{sec:evaluation}) instantiates MBR with structural utility functions; that this approach fails for IE is a non-trivial finding that we trace to the instance-level nature of structural utility (\\S\\ref{sec:discussion}).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. Left: consistency signals (here entity voting) predict instance-level quality---high agreement correlates with high F1 ($\\rho{\\approx}0.38$, AUROC${\\approx}0.69$). Right: the same instance-level signal assigns identical scores to all $N$ candidates from a given input, precluding sample selection; consensus-proximity selection (choosing the sample closest to the consensus output) does not recover per-sample discrimination. No signal significantly outperforms greedy on either task ($p{=}0.39$ for NER logprob; Table~\\ref{tab:selection}).}\n\\label{fig:overview}\n\\end{figure*}\n\nWe systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item \\textbf{A systematic multi-family comparison of confidence signals for generative IE.}\n    We evaluate five signals from three families on quality estimation for NER and RE.\n    Entity voting achieves the strongest $\\rho{=}0.38$ while exact match leads AUROC${=}0.75$; signal rankings depend on both task complexity and evaluation metric, with structural signals leading rank correlation on complex schemas (SciERC) and surface signals leading on simpler tasks (CoNLL)---an ordering directionally consistent across model families, though with model-dependent magnitude.\n\n    \\item \\textbf{Identification of the correlation-selection gap.}\n    Four of five signals are instance-level by construction, making selection failure expected; the empirical finding is that log-probability---the only per-sample signal---also fails ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom on SciERC, where output diversity is substantial (39--43\\% unique outputs).\n    We trace this to the instance-level nature of consistency signals and, for log-probability, to within-instance score compression under constrained decoding.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and when model capability is insufficient (WNUT-17, 52\\% zero F1), inflated full-set correlations collapse on the conditional set---all signals converge toward weak or non-significant correlations once the zero/non-zero boundary is removed.\n    While our NER findings are validated across three datasets of varying difficulty, our RE conclusions are based on a single benchmark (SciERC) and warrant further validation.\n\\end{enumerate}\n\n",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 50
    }
  },
  "sourceToolAssistantUUID": "39841f44-7812-45b4-a057-5ccf341729dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T07:53:41.856Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HR7Q2aa4Xb96SCUm6dTBw6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26212e5c-f22f-42b2-880d-eb69e1d59462",
  "isSidechain": false,
  "requestId": "req_011Cb3zZii275vg2J3MEsM7Y",
  "type": "assistant",
  "uuid": "f9c02b8f-179f-4b8c-8f8c-5c0e19ba64ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019b8CkDYUCGKeLPnpSLUt2b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 46507,
      "output_tokens": 796,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 796,
          "cache_read_input_tokens": 46507,
          "cache_creation_input_tokens": 1189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1189
          },
          "type": "message"
        }
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

_source line 44 · 2026-05-15T07:53:41.861Z_

<details><summary>↩ Tool result · `toolu_01HR7Q2aa4Xb96SCUm6dTBw6`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whether findings generalize across a difficulty gradient.
15	Our Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\S\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).
16	CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
17	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \cite{willard2023guided}.
18	
19	\paragraph{Uncertainty estimation and calibration.}
20	Several surveys cover confidence estimation \cite{geng2024confidence}, selective abstention \cite{wen2025know}, uncertainty quantification \cite{xia2025survey}, and their intersection with calibration \cite{hobelsberger2025systematic} for LLMs.
21	\citet{xiong2024llm} systematically evaluate confidence elicitation across prompting, sampling, and aggregation strategies, finding LLMs tend toward overconfidence; \citet{ye2025uncertainty} extend this to instruction-following settings where calibration degrades with task complexity.
22	\citet{malinin2021uncertainty} provide a broader treatment of uncertainty estimation in autoregressive models, distinguishing data and model uncertainty.
23	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; \citet{kossen2024semantic} distill semantic entropy into lightweight probes; P(True) \cite{kadavath2022language} queries model confidence directly; \citet{he2024uncertainty} survey uncertainty quantification specifically for LLMs, covering both white-box and black-box approaches; our structural signals instead measure agreement over output \textit{structure}.
24	Modern neural networks are often miscalibrated \cite{guo2017calibration, desai2020calibration}; our reliability diagrams extend calibration analysis to structured prediction.
25	Deep ensembles \cite{lakshminarayanan2017ensembles} and MC-dropout \cite{gal2016dropout} obtain uncertainty from model variation; our approach requires no model modification.
26	Prior NER uncertainty work \cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener} operates within discriminative paradigms, inapplicable to generative settings.
27	\citet{kim2024verifiner} propose VerifiNER, using LLMs to verify and refine NER outputs through multi-step reasoning, complementary to our unsupervised consistency approach.
28	Conformal prediction \cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \cite{cobbe2021verifiers, lightman2024verify} and reward models \cite{wang2024mathshepherd} learn per-sample scoring from labeled data.
29	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling} with structural utility functions; despite MBR's success in machine translation \cite{freitag2022high}, we find systematic utility-quality misalignment at the per-sample level for structured IE (\S\ref{sec:discussion}).
30	Selective prediction \cite{geifman2017selective} and confidence-based IE filtering \cite{culotta2004confidence} establish the broader framework; our contribution is characterizing which signals support quality estimation vs.\ sample selection for generative IE.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9c02b8f-179f-4b8c-8f8c-5c0e19ba64ce",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "97d865e7-8ca6-41ba-ab39-af766f97016c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency decoding \\cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.\nExtensions to free-form text use LLM-based comparison \\cite{chen2024usc}, atomic sub-claim decomposition \\cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \\cite{manakul2023selfcheckgpt}.\nFor test-time scaling, \\citet{snell2024scaling} characterize compute scaling laws and \\citet{brown2024monkeys} show best-of-$N$ gains across tasks.\nRecent reward-free selectors include confidence-weighted voting \\cite{taubenfeld2025cisc}, KL-based self-certainty \\cite{kang2025selfcertainty}, adaptive sampling \\cite{kim2026reasc}, ranked aggregation \\cite{wang2025rankedvoting}, and latent-space consistency \\cite{oh2025latentsc}.\nConcurrently, \\citet{feng2025optimal} and \\citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \\citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.\nAll of the above target reasoning/QA with discrete answers or specific aggregation strategies.\nOur work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).\n\n\\paragraph{Consistency for structured IE.}\n\\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.\nTheir work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whether findings generalize across a difficulty gradient.\nOur Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\\S\\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).\nCoCoA \\cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.\nOur evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \\cite{willard2023guided}.\n\n\\paragraph{Uncertainty estimation and calibration.}\nSeveral surveys cover confidence estimation \\cite{geng2024confidence}, selective abstention \\cite{wen2025know}, uncertainty quantification \\cite{xia2025survey}, and their intersection with calibration \\cite{hobelsberger2025systematic} for LLMs.\n\\citet{xiong2024llm} systematically evaluate confidence elicitation across prompting, sampling, and aggregation strategies, finding LLMs tend toward overconfidence; \\citet{ye2025uncertainty} extend this to instruction-following settings where calibration degrades with task complexity.\n\\citet{malinin2021uncertainty} provide a broader treatment of uncertainty estimation in autoregressive models, distinguishing data and model uncertainty.\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; \\citet{kossen2024semantic} distill semantic entropy into lightweight probes; P(True) \\cite{kadavath2022language} queries model confidence directly; \\citet{he2024uncertainty} survey uncertainty quantification specifically for LLMs, covering both white-box and black-box approaches; our structural signals instead measure agreement over output \\textit{structure}.\nModern neural networks are often miscalibrated \\cite{guo2017calibration, desai2020calibration}; our reliability diagrams extend calibration analysis to structured prediction.\nDeep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation; our approach requires no model modification.\nPrior NER uncertainty work \\cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener} operates within discriminative paradigms, inapplicable to generative settings.\n\\citet{kim2024verifiner} propose VerifiNER, using LLMs to verify and refine NER outputs through multi-step reasoning, complementary to our unsupervised consistency approach.\nConformal prediction \\cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \\cite{cobbe2021verifiers, lightman2024verify} and reward models \\cite{wang2024mathshepherd} learn per-sample scoring from labeled data.\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling} with structural utility functions; despite MBR's success in machine translation \\cite{freitag2022high}, we find systematic utility-quality misalignment at the per-sample level for structured IE (\\S\\ref{sec:discussion}).\nSelective prediction \\cite{geifman2017selective} and confidence-based IE filtering \\cite{culotta2004confidence} establish the broader framework; our contribution is characterizing which signals support quality estimation vs.\\ sample selection for generative IE.\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  },
  "sourceToolAssistantUUID": "f9c02b8f-179f-4b8c-8f8c-5c0e19ba64ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T07:53:43.310Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TeL5EY9vd28XZW318sXXbN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97d865e7-8ca6-41ba-ab39-af766f97016c",
  "isSidechain": false,
  "requestId": "req_011Cb3zZii275vg2J3MEsM7Y",
  "type": "assistant",
  "uuid": "c6101d18-de87-4a39-8805-7263237c64a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019b8CkDYUCGKeLPnpSLUt2b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 46507,
      "output_tokens": 796,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 796,
          "cache_read_input_tokens": 46507,
          "cache_creation_input_tokens": 1189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1189
          },
          "type": "message"
        }
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

_source line 46 · 2026-05-15T07:53:43.314Z_

<details><summary>↩ Tool result · `toolu_01TeL5EY9vd28XZW318sXXbN`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard, entity voting) and \textit{surface} (exact match, Fleiss' $\kappa$).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface, instance-level).}
28	The majority fraction---the proportion of samples producing the most common output:
29	\begin{equation}\label{eq:em}
30	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
31	\end{equation}
32	
33	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
34	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
35	\begin{equation}\label{eq:fk}
36	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
37	\end{equation}
38	where $\bar{P}$ is mean observed pairwise agreement and $\bar{P}_e$ is expected agreement under random assignment.
39	While FK assumes independent raters, temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns; empirically, temperature-sampled outputs exhibit slightly lower agreement than independent raters would predict (excess agreement $-$0.4\% to $-$4.0\%), indicating mild \textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.
40	Unlike structural signals, FK relies on exact string matching and does not tolerate surface variations.
41	
42	\paragraph{Soft Jaccard (structural, instance-level).}
43	Our core structural signal extends Jaccard similarity \cite{jaccard1901distribution} to extracted entity/relation sets.
44	For samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching via the Hungarian algorithm (maximizing total token-level IoU; zero-IoU pairs automatically receive zero weight), and define:
45	\begin{equation}\label{eq:sj}
46	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
47	\end{equation}
48	where $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.
49	We use $\max(|g_i|, |g_j|)$ rather than $|g_i \cup g_j|$ as the normalizer to penalize length asymmetry between samples.
50	The instance-level signal averages over all pairs:
51	\begin{equation}\label{eq:sj_instance}
52	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i<j} \text{SJ}(y_i, y_j)
53	\end{equation}
54	
55	\paragraph{Entity voting confidence (structural, instance-level).}
56	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
57	The instance-level confidence is the mean frequency:
58	\begin{equation}\label{eq:voting}
59	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
60	\end{equation}
61	When $E_\cup = \emptyset$ (no entity extracted by any sample), we set $c_{\text{vote}}(x) = 0$.\footnote{This occurs in $<$1\% of instances in our experiments (WNUT-17 only).}
62	
63	\subsection{Evaluation Framework}\label{sec:evaluation}
64	
65	\paragraph{Quality estimation.}
66	We measure rank correlation (Spearman $\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.
67	
68	\paragraph{Sample selection.}
69	We report best-of-$N$ F1: for each instance, the signal selects one sample.
70	Per-sample signals (logprob) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).
71	We compare against an \textit{oracle} (highest-F1 sample) and \textit{greedy} ($T{=}0$, $N{=}1$).
72	
73	\paragraph{Complementarity.}
74	High rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\S\ref{sec:selection_gap}).
75	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6101d18-de87-4a39-8805-7263237c64a6",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "f41cf733-de4d-4df7-906b-413e630ad43a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven a language model $\\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}.\nEach $y_i$ is an entity set (NER) or relation set (RE).\nA confidence signal $c$ serves two purposes: (a) \\textit{quality estimation}---predicting which instances the model handles reliably, and (b) \\textit{sample selection}---identifying the best output among $N$ candidates.\n\nA \\textbf{per-sample signal} scores each $y_i$ independently, $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$, enabling direct candidate ranking.\nAn \\textbf{instance-level signal} aggregates over all $N$ samples, $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$, producing a single score per input.\nThis asymmetry---between predicting \\textit{which inputs} are easy and selecting \\textit{which output} is best---is central to the correlation-selection gap we investigate.\nNotation is summarized in Appendix~\\ref{app:notation}.\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nWe use \\textit{confidence signal} as the umbrella term for all five measures.\nFour are \\textit{consistency signals}---computed from inter-sample agreement---spanning two families: \\textit{structural} (Soft Jaccard, entity voting) and \\textit{surface} (exact match, Fleiss' $\\kappa$).\nThe fifth, log-probability, is the sole \\textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nThe only per-sample signal.\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{<j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe majority fraction---the proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed pairwise agreement and $\\bar{P}_e$ is expected agreement under random assignment.\nWhile FK assumes independent raters, temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns; empirically, temperature-sampled outputs exhibit slightly lower agreement than independent raters would predict (excess agreement $-$0.4\\% to $-$4.0\\%), indicating mild \\textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.\nUnlike structural signals, FK relies on exact string matching and does not tolerate surface variations.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nOur core structural signal extends Jaccard similarity \\cite{jaccard1901distribution} to extracted entity/relation sets.\nFor samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching via the Hungarian algorithm (maximizing total token-level IoU; zero-IoU pairs automatically receive zero weight), and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.\nWe use $\\max(|g_i|, |g_j|)$ rather than $|g_i \\cup g_j|$ as the normalizer to penalize length asymmetry between samples.\nThe instance-level signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i<j} \\text{SJ}(y_i, y_j)\n\\end{equation}\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\nWhen $E_\\cup = \\emptyset$ (no entity extracted by any sample), we set $c_{\\text{vote}}(x) = 0$.\\footnote{This occurs in $<$1\\% of instances in our experiments (WNUT-17 only).}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nWe measure rank correlation (Spearman $\\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.\n\n\\paragraph{Sample selection.}\nWe report best-of-$N$ F1: for each instance, the signal selects one sample.\nPer-sample signals (logprob) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).\nWe compare against an \\textit{oracle} (highest-F1 sample) and \\textit{greedy} ($T{=}0$, $N{=}1$).\n\n\\paragraph{Complementarity.}\nHigh rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\\S\\ref{sec:selection_gap}).\n",
      "numLines": 75,
      "startLine": 1,
      "totalLines": 75
    }
  },
  "sourceToolAssistantUUID": "c6101d18-de87-4a39-8805-7263237c64a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T07:53:43.348Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NpKed61W8mirtX74RLaBa8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f41cf733-de4d-4df7-906b-413e630ad43a",
  "isSidechain": false,
  "requestId": "req_011Cb3zZii275vg2J3MEsM7Y",
  "type": "assistant",
  "uuid": "10fc0917-a7c6-477f-8294-51a4fd0d9554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019b8CkDYUCGKeLPnpSLUt2b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 46507,
      "output_tokens": 796,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 796,
          "cache_read_input_tokens": 46507,
          "cache_creation_input_tokens": 1189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1189
          },
          "type": "message"
        }
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

_source line 48 · 2026-05-15T07:53:43.355Z_

<details><summary>↩ Tool result · `toolu_01NpKed61W8mirtX74RLaBa8`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring cross-architecture comparisons (at 8B scale) reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$; $N{=}16$ results are averaged across seeds \{42, 123, 456\}.\textsuperscript{$\dagger$}}\label{fn:n16}\footnotetext{\textsuperscript{$\dagger$}$N{=}16$ experiments were run only for configurations where $N$-scaling analysis was prioritized: LLaMA CoNLL (3-seed robustness). Additional $N{=}16$ results appear in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
31	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
32	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
33	\midrule
34	\multicolumn{10}{l}{\textit{$N{=}8$}} \\
35	Voting Conf. & Structural & \textbf{.379} & .684 & \textbf{.350} & .693 & .424 & .789 & .426 & .709 \\
36	Soft Jaccard  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
37	Fleiss' $\kappa$ & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\
38	Exact Match  & Surface    & .295 & \textbf{.749} & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
39	Log-prob     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \textbf{.761} \\
40	\midrule
41	\multicolumn{10}{l}{\textit{$N{=}16$ (3-seed)}} \\
42	Voting Conf. & Structural & & & & & & & .458${\pm}$.003 & \\
43	Soft Jaccard  & Structural & & & & & & & \textbf{.463${\pm}$.007} & \\
44	Fleiss' $\kappa$ & Surface & & & & & & & .455${\pm}$.006 & \\
45	Exact Match  & Surface    & & & & & & & .460${\pm}$.008 & \\
46	Log-prob     & Model      & & & & & & & .310${\pm}$.005 & \\
47	\bottomrule
48	\end{tabular}
49	\end{table*}
50	
51	\begin{figure*}[t]
52	\centering
53	\includegraphics[width=\textwidth]{fig_signal_heatmap}
54	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while logprob RE collapses to near-zero ($\rho{=}0.011$).}
55	\label{fig:signal_heatmap}
56	\end{figure*}
57	
58	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
59	
60	\paragraph{Difficulty-dependent signal complementarity.}
61	On SciERC NER (complex schema, 6 types), structural signals lead: Voting achieves $\rho{=}0.379$ and SJ $\rho{=}0.360$, both outperforming surface ($\rho{\leq}0.295$) and logprob ($\rho{=}0.205$).
62	This advantage persists on RE (Voting $\rho{=}0.350$), though all signals weaken due to the 40\% zero-F1 floor effect.
63	Entity voting and SJ show moderate instance-level correlation (NER: $\rho{=}0.659$; RE: $\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\ span-level set overlap.
64	While the best $\rho{=}0.38$ (Voting) explains approximately 14\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\footnote{For context, semantic entropy achieves AUROC $\approx$ 0.75--0.85 on discrete-answer QA tasks \cite{kuhn2023semantic}; however, direct comparison is not meaningful: output spaces differ fundamentally (discrete answers vs.\ entity/relation sets), evaluation protocols are incompatible, and task difficulty distributions are unrelated. We cite this only to situate our AUROC scale.}
65	Pairwise bootstrap CIs confirm the SJ advantage over logprob ($\Delta\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\Delta\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\ref{tab:bootstrap_signal_ci}, Appendix~\ref{app:bootstrap_signal}).
66	
67	\paragraph{$\rho$--AUROC dissociation.}
68	Since $\rho$ measures monotonic rank association while AUROC measures threshold-invariant binary classification, dissociation between them is statistically expected.
69	The practical implication is that signal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\rho$ (0.295), making it preferred for binary quality triage, while structural signals ($\rho{\geq}0.36$) are better suited for fine-grained ranking.
70	On CoNLL with LLaMA, logprob leads AUROC (0.761) yet trails in $\rho$ (0.307), confirming that this pattern holds across datasets and motivating evaluation on both metrics.
71	
72	\paragraph{Signal rankings shift with task difficulty.}
73	On CoNLL (greedy F1${\approx}$0.91), EM leads ($\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and Voting.
74	When most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.
75	This crossover---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.
76	Cross-architecture stability is strong: SJ achieves $\rho{=}0.436$ (Qwen) vs.\ $0.431$ (LLaMA) on CoNLL ($\Delta{=}0.005$, within 3-seed $\sigma{\approx}0.007$).
77	On WNUT-17, where 52\% of instances receive zero F1, full-set correlations are misleading: voting achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.; Table~\ref{tab:wnut}).
78	Logprob exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$, AUROC${=}0.219$), indicating that higher model confidence associates with lower extraction quality on this noisy domain---further undermining logprob as a general-purpose IE quality signal.
79	On the conditional set, all signals collapse toward weak or non-significant correlations ($\rho{\leq}0.35$), with SJ achieving only $\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.
80	
81	\paragraph{Conditional filtering.}
82	Filtering to non-zero F1 instances reshuffles rankings (Figure~\ref{fig:signal_heatmap}, right).
83	EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while Voting and FK drop substantially (Voting NER: $0.379{\to}0.300$; FK NER: $0.267{\to}0.176$).
84	Logprob RE collapses to $\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.
85	This creates a natural complementarity: Voting and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
86	
87	%% ============================================================
88	\subsection{The Correlation-Selection Gap}
89	\label{sec:selection_gap}
90	
91	\begin{figure*}[t]
92	\centering
93	\includegraphics[width=\textwidth]{fig_selection_gap}
94	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER logprob, the best signal; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound.}
95	\label{fig:selection_gap}
96	\end{figure*}
97	
98	\begin{table}[t]
99	\centering
100	\small
101	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \textbf{bold}. EM selects the plurality output; despite a 42\% pairwise exact-match rate, EM selection underperforms greedy on both tasks.}
102	\label{tab:selection}
103	\begin{tabular}{lcc}
104	\toprule
105	Method & NER F1 & RE F1 \\
106	\midrule
107	Oracle & 0.776 & 0.585 \\
108	\midrule
109	Log-prob           & \textbf{0.650} & 0.395 \\
110	Soft Jaccard       & 0.645 & 0.386 \\
111	Exact Match        & 0.636 & 0.372 \\
112	Voting             & 0.634 & 0.359 \\
113	\midrule
114	Greedy ($T{=}0$)   & 0.644 & \textbf{0.404} \\
115	Random             & 0.608 & 0.354 \\
116	\bottomrule
117	\end{tabular}
118	\end{table}
119	
120	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
121	Four of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.
122	The non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.
123	We anchor this analysis on SciERC, where output diversity is substantial: only 11--18\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.
124	
125	\paragraph{No significant improvement over greedy.}
126	We exclude 22 instances with empty gold annotations, yielding $n{=}529$ for statistical analysis.
127	We evaluate statistical significance using instance-level paired bootstrap resampling ($B{=}10{,}000$, with replacement) over these instances, reporting 95\% percentile CIs.
128	The three random seeds (42, 123, 456) refer to independent inference runs; we average $\rho$ across seeds and report the bootstrap $p$-value of the paired difference (best signal vs.\ greedy).
129	On NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).
130	Logprob achieves the highest selection F1 (0.650, +0.6~pp), but this is not statistically significant ($p{=}0.39$; 95\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$; sign test: 61W/70L, win\%${=}$46.6\%).
131	On RE, the gap is complete: the best signal (logprob, 0.395) falls below greedy (0.404, $-0.9$\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.
132	TOST equivalence testing confirms that most signals are statistically indistinguishable from greedy: on NER, SJ and logprob are equivalent within ${\pm}2$~pp; on RE, EM and Voting fail equivalence even at ${\pm}5$~pp due to systematic underperformance (Table~\ref{tab:tost}, Appendix~\ref{app:diversity}).
133	Voting ($\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\textit{below} greedy.
134	The gap extends to CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}), though these cases are less informative for selection analysis: CoNLL exhibits a ceiling effect where 57--88\% of instances produce identical outputs across all $N$ samples (greedy F1 already ${\approx}$0.91--0.92), and WNUT-17 is dominated by the capability boundary (52\% zero F1; \S\ref{sec:qe_results}).
135	The SciERC results, where meaningful per-sample variance exists, provide the strongest evidence that instance-level signals cannot discriminate among diverse candidates.
136	
137	\paragraph{Quality estimation $\neq$ output selection.}
138	Instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best.
139	When per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.
140	This gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
141	
142	%% ============================================================
143	\subsection{Robustness}
144	\label{sec:robustness_main}
145	
146	Consistency-based signals show robust performance across $T{\in}\{0.7, 1.0\}$ (SJ NER $\Delta\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over logprob across all settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$; Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
147	NER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\rho{\approx}0.28$ for $N{=}16$.
148	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10fc0917-a7c6-477f-8294-51a4fd0d9554",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "a77998f1-e13e-441c-b8aa-37bcf2c05321",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, ensuring cross-architecture comparisons (at 8B scale) reflect architectural differences rather than training confounds.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). Best value per block and column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$; $N{=}16$ results are averaged across seeds \\{42, 123, 456\\}.\\textsuperscript{$\\dagger$}}\\label{fn:n16}\\footnotetext{\\textsuperscript{$\\dagger$}$N{=}16$ experiments were run only for configurations where $N$-scaling analysis was prioritized: LLaMA CoNLL (3-seed robustness). Additional $N{=}16$ results appear in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\n\\multicolumn{10}{l}{\\textit{$N{=}8$}} \\\\\nVoting Conf. & Structural & \\textbf{.379} & .684 & \\textbf{.350} & .693 & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .295 & \\textbf{.749} & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\midrule\n\\multicolumn{10}{l}{\\textit{$N{=}16$ (3-seed)}} \\\\\nVoting Conf. & Structural & & & & & & & .458${\\pm}$.003 & \\\\\nSoft Jaccard  & Structural & & & & & & & \\textbf{.463${\\pm}$.007} & \\\\\nFleiss' $\\kappa$ & Surface & & & & & & & .455${\\pm}$.006 & \\\\\nExact Match  & Surface    & & & & & & & .460${\\pm}$.008 & \\\\\nLog-prob     & Model      & & & & & & & .310${\\pm}$.005 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while logprob RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Difficulty-dependent signal complementarity.}\nOn SciERC NER (complex schema, 6 types), structural signals lead: Voting achieves $\\rho{=}0.379$ and SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and logprob ($\\rho{=}0.205$).\nThis advantage persists on RE (Voting $\\rho{=}0.350$), though all signals weaken due to the 40\\% zero-F1 floor effect.\nEntity voting and SJ show moderate instance-level correlation (NER: $\\rho{=}0.659$; RE: $\\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\\ span-level set overlap.\nWhile the best $\\rho{=}0.38$ (Voting) explains approximately 14\\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\\footnote{For context, semantic entropy achieves AUROC $\\approx$ 0.75--0.85 on discrete-answer QA tasks \\cite{kuhn2023semantic}; however, direct comparison is not meaningful: output spaces differ fundamentally (discrete answers vs.\\ entity/relation sets), evaluation protocols are incompatible, and task difficulty distributions are unrelated. We cite this only to situate our AUROC scale.}\nPairwise bootstrap CIs confirm the SJ advantage over logprob ($\\Delta\\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\\Delta\\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\\ref{tab:bootstrap_signal_ci}, Appendix~\\ref{app:bootstrap_signal}).\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nSince $\\rho$ measures monotonic rank association while AUROC measures threshold-invariant binary classification, dissociation between them is statistically expected.\nThe practical implication is that signal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\\rho$ (0.295), making it preferred for binary quality triage, while structural signals ($\\rho{\\geq}0.36$) are better suited for fine-grained ranking.\nOn CoNLL with LLaMA, logprob leads AUROC (0.761) yet trails in $\\rho$ (0.307), confirming that this pattern holds across datasets and motivating evaluation on both metrics.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${\\approx}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and Voting.\nWhen most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.\nThis crossover---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.\nCross-architecture stability is strong: SJ achieves $\\rho{=}0.436$ (Qwen) vs.\\ $0.431$ (LLaMA) on CoNLL ($\\Delta{=}0.005$, within 3-seed $\\sigma{\\approx}0.007$).\nOn WNUT-17, where 52\\% of instances receive zero F1, full-set correlations are misleading: voting achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.; Table~\\ref{tab:wnut}).\nLogprob exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$, AUROC${=}0.219$), indicating that higher model confidence associates with lower extraction quality on this noisy domain---further undermining logprob as a general-purpose IE quality signal.\nOn the conditional set, all signals collapse toward weak or non-significant correlations ($\\rho{\\leq}0.35$), with SJ achieving only $\\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.\n\n\\paragraph{Conditional filtering.}\nFiltering to non-zero F1 instances reshuffles rankings (Figure~\\ref{fig:signal_heatmap}, right).\nEM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while Voting and FK drop substantially (Voting NER: $0.379{\\to}0.300$; FK NER: $0.267{\\to}0.176$).\nLogprob RE collapses to $\\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.\nThis creates a natural complementarity: Voting and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER logprob, the best signal; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM selects the plurality output; despite a 42\\% pairwise exact-match rate, EM selection underperforms greedy on both tasks.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.776 & 0.585 \\\\\n\\midrule\nLog-prob           & \\textbf{0.650} & 0.395 \\\\\nSoft Jaccard       & 0.645 & 0.386 \\\\\nExact Match        & 0.636 & 0.372 \\\\\nVoting             & 0.634 & 0.359 \\\\\n\\midrule\nGreedy ($T{=}0$)   & 0.644 & \\textbf{0.404} \\\\\nRandom             & 0.608 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nFour of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.\nThe non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.\nWe anchor this analysis on SciERC, where output diversity is substantial: only 11--18\\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.\n\n\\paragraph{No significant improvement over greedy.}\nWe exclude 22 instances with empty gold annotations, yielding $n{=}529$ for statistical analysis.\nWe evaluate statistical significance using instance-level paired bootstrap resampling ($B{=}10{,}000$, with replacement) over these instances, reporting 95\\% percentile CIs.\nThe three random seeds (42, 123, 456) refer to independent inference runs; we average $\\rho$ across seeds and report the bootstrap $p$-value of the paired difference (best signal vs.\\ greedy).\nOn NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).\nLogprob achieves the highest selection F1 (0.650, +0.6~pp), but this is not statistically significant ($p{=}0.39$; 95\\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$; sign test: 61W/70L, win\\%${=}$46.6\\%).\nOn RE, the gap is complete: the best signal (logprob, 0.395) falls below greedy (0.404, $-0.9$\\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.\nTOST equivalence testing confirms that most signals are statistically indistinguishable from greedy: on NER, SJ and logprob are equivalent within ${\\pm}2$~pp; on RE, EM and Voting fail equivalence even at ${\\pm}5$~pp due to systematic underperformance (Table~\\ref{tab:tost}, Appendix~\\ref{app:diversity}).\nVoting ($\\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\\textit{below} greedy.\nThe gap extends to CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}), though these cases are less informative for selection analysis: CoNLL exhibits a ceiling effect where 57--88\\% of instances produce identical outputs across all $N$ samples (greedy F1 already ${\\approx}$0.91--0.92), and WNUT-17 is dominated by the capability boundary (52\\% zero F1; \\S\\ref{sec:qe_results}).\nThe SciERC results, where meaningful per-sample variance exists, provide the strongest evidence that instance-level signals cannot discriminate among diverse candidates.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency-based signals show robust performance across $T{\\in}\\{0.7, 1.0\\}$ (SJ NER $\\Delta\\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over logprob across all settings ($\\Delta\\rho{=}{+}0.135$ to ${+}0.175$; Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\nNER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\\rho{\\approx}0.28$ for $N{=}16$.\n",
      "numLines": 148,
      "startLine": 1,
      "totalLines": 148
    }
  },
  "sourceToolAssistantUUID": "10fc0917-a7c6-477f-8294-51a4fd0d9554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T07:53:44.250Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W2XAxx96SYXUeCPhtXkUVV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a77998f1-e13e-441c-b8aa-37bcf2c05321",
  "isSidechain": false,
  "requestId": "req_011Cb3zZii275vg2J3MEsM7Y",
  "type": "assistant",
  "uuid": "8077712f-2417-4d4b-9f6d-c8307981de6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019b8CkDYUCGKeLPnpSLUt2b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 46507,
      "output_tokens": 796,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 796,
          "cache_read_input_tokens": 46507,
          "cache_creation_input_tokens": 1189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1189
          },
          "type": "message"
        }
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

_source line 50 · 2026-05-15T07:53:44.255Z_

<details><summary>↩ Tool result · `toolu_01W2XAxx96SYXUeCPhtXkUVV`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), Voting and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists: two layers.}
9	\textit{Layer 1 (structural):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
10	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
11	\textit{Layer 2 (empirical):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
12	Under constrained decoding, logprob scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
13	In the non-tied 40\%, logprob selection significantly outperforms greedy ($+2.9$~pp, $p{=}0.01$), confirming the signal carries useful information but is resolution-limited.
14	The common root is that quality estimation ranks \textit{instances}, while sample selection requires ranking \textit{candidates within a single instance}---a finer granularity that neither instance-level aggregation nor token-level confidence provides.
15	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339; Appendix~\ref{app:calibration}) may compound this failure.
16	
17	\paragraph{Connection to MBR decoding.}
18	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
19	Despite MBR's success in machine translation \cite{freitag2022high}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
20	
21	\paragraph{Methodological implications.}
22	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.
23	Effective selection likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}; $N$-scaling analysis (Appendix~\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8077712f-2417-4d4b-9f6d-c8307981de6c",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "a87a2a75-827d-4f86-9d10-e00f3820fc9a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, entity voting provides the strongest rank correlation ($\\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$).\nSignal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), Voting and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.\nWhen model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\\ref{tab:wnut}).\n\n\\paragraph{Why the gap exists: two layers.}\n\\textit{Layer 1 (structural):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nConsensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\n\\textit{Layer 2 (empirical):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.\nUnder constrained decoding, logprob scores are severely compressed: 60\\% of instances have a within-sample range below 0.05, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$; Appendix~\\ref{app:logprob_ties}).\nIn the non-tied 40\\%, logprob selection significantly outperforms greedy ($+2.9$~pp, $p{=}0.01$), confirming the signal carries useful information but is resolution-limited.\nThe common root is that quality estimation ranks \\textit{instances}, while sample selection requires ranking \\textit{candidates within a single instance}---a finer granularity that neither instance-level aggregation nor token-level confidence provides.\nDiversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339; Appendix~\\ref{app:calibration}) may compound this failure.\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  },
  "sourceToolAssistantUUID": "8077712f-2417-4d4b-9f6d-c8307981de6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T07:53:44.308Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LaBQF38yHMw3nsai4XZ1Lu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a87a2a75-827d-4f86-9d10-e00f3820fc9a",
  "isSidechain": false,
  "requestId": "req_011Cb3zZii275vg2J3MEsM7Y",
  "type": "assistant",
  "uuid": "08727d1b-065a-410e-91eb-10a9469d89a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019b8CkDYUCGKeLPnpSLUt2b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 46507,
      "output_tokens": 796,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 796,
          "cache_read_input_tokens": 46507,
          "cache_creation_input_tokens": 1189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1189
          },
          "type": "message"
        }
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

_source line 52 · 2026-05-15T07:53:44.320Z_

<details><summary>↩ Tool result · `toolu_01LaBQF38yHMw3nsai4XZ1Lu`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides, to our knowledge, the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families across NER and RE tasks of varying difficulty, we disentangle quality estimation from sample selection---two objectives that prior work has conflated.
5	Consistency-based signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75).
6	Four of five signals are instance-level by construction and cannot rank candidates; log-probability, the only per-sample signal, also fails ($p{>}0.39$, 13--18~pp oracle headroom on SciERC), a disconnect we term the \textit{correlation-selection gap}.
7	Signal rankings depend on task difficulty---exact match leads on easy tasks, structural signals on hard tasks---with this ordering directionally consistent across model families, though magnitudes are model-dependent.
8	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
9	
10	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination.
11	Cross-task transfer beyond IE, scaling to larger models (70B+), and integration with conformal prediction are promising directions.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08727d1b-065a-410e-91eb-10a9469d89a7",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "047e1134-6236-40fd-b1da-5a3dfd3e34ce",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nThis work provides, to our knowledge, the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.\nBy comparing five signals from three families across NER and RE tasks of varying difficulty, we disentangle quality estimation from sample selection---two objectives that prior work has conflated.\nConsistency-based signals are effective quality estimators ($\\rho$ up to 0.38, AUROC up to 0.75).\nFour of five signals are instance-level by construction and cannot rank candidates; log-probability, the only per-sample signal, also fails ($p{>}0.39$, 13--18~pp oracle headroom on SciERC), a disconnect we term the \\textit{correlation-selection gap}.\nSignal rankings depend on task difficulty---exact match leads on easy tasks, structural signals on hard tasks---with this ordering directionally consistent across model families, though magnitudes are model-dependent.\nWhile our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.\n\nTrained verifiers or reward models could close the selection gap by learning per-sample quality discrimination.\nCross-task transfer beyond IE, scaling to larger models (70B+), and integration with conformal prediction are promising directions.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  },
  "sourceToolAssistantUUID": "08727d1b-065a-410e-91eb-10a9469d89a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T07:53:44.757Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H6vxUCKBnnLzpkmNjqo338`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "047e1134-6236-40fd-b1da-5a3dfd3e34ce",
  "isSidechain": false,
  "requestId": "req_011Cb3zZii275vg2J3MEsM7Y",
  "type": "assistant",
  "uuid": "36215409-d022-41a8-be08-d85b7e1ec553",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019b8CkDYUCGKeLPnpSLUt2b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 46507,
      "output_tokens": 796,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 796,
          "cache_read_input_tokens": 46507,
          "cache_creation_input_tokens": 1189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1189
          },
          "type": "message"
        }
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

_source line 54 · 2026-05-15T07:53:44.763Z_

<details><summary>↩ Tool result · `toolu_01H6vxUCKBnnLzpkmNjqo338`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.
17	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36215409-d022-41a8-be08-d85b7e1ec553",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "8789f49f-c3b1-4148-a128-55c3a40f570b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nRE selection failure persists even when restricting to non-zero F1 instances (Appendix~\\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nA 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\\sigma{\\leq}0.025$; Table~\\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses only unsupervised signals.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ and $N{=}16$.\nThe behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.\n\nOn CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\\rho{=}0.431$ vs.\\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nConstrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.\nFinally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  },
  "sourceToolAssistantUUID": "36215409-d022-41a8-be08-d85b7e1ec553",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T07:53:45.682Z_

<details open><summary>🔧 Tool call — Read · `toolu_019giCLx1wCcY74aZHXPourQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8789f49f-c3b1-4148-a128-55c3a40f570b",
  "isSidechain": false,
  "requestId": "req_011Cb3zZii275vg2J3MEsM7Y",
  "type": "assistant",
  "uuid": "198977fb-bec5-4cbd-8ff1-c11420ad6c6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019b8CkDYUCGKeLPnpSLUt2b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 46507,
      "output_tokens": 796,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 796,
          "cache_read_input_tokens": 46507,
          "cache_creation_input_tokens": 1189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1189
          },
          "type": "message"
        }
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

_source line 56 · 2026-05-15T07:53:45.955Z_

<details><summary>↩ Tool result · `toolu_019giCLx1wCcY74aZHXPourQ`</summary>

```text
1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-architecture transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-architecture} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm}0.008$ & --- \\
56	\quad Voting &  & $0.458{\pm}0.003$ & --- \\
57	\quad Logprob &  & $0.310{\pm}0.005$ & --- \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	\begin{figure}[t]
63	\centering
64	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
65	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. Logprob $T{=}0.7$ data unavailable.}
66	\label{fig:temperature_robustness}
67	\end{figure}
68	
69	\paragraph{Temperature sensitivity.}
70	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.
71	FK shows mixed behavior: NER $\rho$ drops by 0.054, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
72	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.360 vs.\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
73	
74	\paragraph{Sample size scaling.}
75	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.412{\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.052$.
76	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
77	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while logprob gains only $+0.003$ (Table~\ref{tab:quality_estimation}).
78	FK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.
79	Voting confidence $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while logprob is approximately $N$-invariant ($\Delta{\leq}0.021$).
80	SJ, EM, and voting confidence scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.
81	
82	\paragraph{Cross-architecture transfer.}
83	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.363$, FK $\rho{=}0.327$).
84	On CoNLL, the cross-architecture gap is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
85	At $N{=}16$, the structural-over-logprob advantage holds across all four tested settings: Qwen SciERC (Voting $\rho{=}0.411$ vs.\ logprob 0.259, $\Delta{=}{+}0.152$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ logprob 0.328, $\Delta{=}{+}0.135$), LLaMA SciERC (Voting $\rho{=}0.452$ vs.\ logprob 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.463{\pm}0.007$ vs.\ logprob $0.310{\pm}0.005$, $\Delta{=}{+}0.153$).
86	
87	\section{Calibration Analysis}\label{app:calibration}
88	
89	\begin{figure*}[t]
90	\centering
91	\includegraphics[width=\textwidth]{fig_reliability}
92	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
93	\label{fig:reliability}
94	\end{figure*}
95	
96	Reliability diagrams use 10 equal-width bins.
97	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
98	
99	\section{Additional Analyses}\label{app:additional}
100	
101	\paragraph{Per-relation diagnostic.}
102	RE signal degradation is relation-specific.
103	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
104	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
105	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
106	
107	\paragraph{Capability stratification.}
108	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
109	The SJ advantage over logprob remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
110	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
111	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
112	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
113	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: Voting reaches $\rho{=}0.630$, logprob $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
114	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
115	
116	\paragraph{Length vs.\ log-probability.}
117	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for logprob's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
118	
119	\begin{figure}[t]
120	\centering
121	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
122	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
123	\label{fig:length_logprob_scatter}
124	\end{figure}
125	
126	\paragraph{Evaluation circularity.}
127	Leave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
128	Evaluation circularity is negligible.
129	
130	\paragraph{Conditional filtering details.}
131	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
132	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while logprob drops to $\rho{=}{-}0.026$.
133	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
134	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
135	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
136	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
137	
138	\paragraph{WNUT-17 full signal analysis.}
139	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
140	Voting achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
141	Logprob shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
142	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
143	
144	\begin{table}[t]
145	\centering
146	\small
147	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). Logprob exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
148	\label{tab:wnut}
149	\begin{tabular}{lccccc}
150	\toprule
151	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
152	\midrule
153	Voting  & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
154	FK      & .125 & .001 & .555 & .169 & .002 \\
155	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
156	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
157	Logprob & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
158	\bottomrule
159	\end{tabular}
160	\end{table}
161	
162	\paragraph{Cross-configuration selection analysis.}
163	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
164	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), logprob achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
165	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
166	
167	\begin{table*}[t]
168	\centering
169	\small
170	\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). SJ: Soft Jaccard, FK: Fleiss' $\kappa$, EM: Exact Match, LP: Log-prob, VC: Voting Confidence. Best non-oracle signal per row in \textbf{bold}. No signal significantly outperforms greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
171	\label{tab:cross_selection}
172	\begin{tabular}{llccccccc}
173	\toprule
174	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
175	\midrule
176	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
177	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
178	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
179	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
180	\bottomrule
181	\end{tabular}
182	\end{table*}
183	
184	\paragraph{Diminishing returns of $N$-scaling.}
185	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2024scaling}.
186	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
187	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
188	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ logprob $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while logprob does not.
189	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
190	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
191	
192	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
193	
194	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
195	The SJ--logprob gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
196	The Voting--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
197	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
198	
199	\begin{table}[t]
200	\centering
201	\small
202	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
203	\label{tab:bootstrap_signal_ci}
204	\begin{tabular}{lcc}
205	\toprule
206	Signal & $\rho$ & 95\% CI \\
207	\midrule
208	Voting Conf. & +0.379 & [+0.299, +0.456] \\
209	Soft Jaccard & +0.360 & [+0.277, +0.437] \\
210	Exact Match & +0.295 & [+0.212, +0.371] \\
211	Fleiss' $\kappa$ & +0.267 & [+0.176, +0.354] \\
212	Log-prob & +0.205 & [+0.119, +0.291] \\
213	\bottomrule
214	\end{tabular}
215	
216	\vspace{0.5em}
217	
218	\begin{tabular}{lccc}
219	\toprule
220	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
221	\midrule
222	SJ $-$ Logprob & +0.155 & [+0.074, +0.234] & Yes \\
223	Voting $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
224	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
225	\bottomrule
226	\end{tabular}
227	
228	\smallskip
229	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
230	\end{table}
231	
232	\section{Diversity and Selection Analysis}\label{app:diversity}
233	
234	\paragraph{Output diversity quantification.}
235	Table~\ref{tab:diversity} summarizes output diversity across configurations.
236	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
237	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
238	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.
239	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
240	
241	\begin{table}[t]
242	\centering
243	\small
244	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
245	\label{tab:diversity}
246	\begin{tabular}{lcc}
247	\toprule
248	Config & Identical & Unique \\
249	\midrule
250	Qwen/SciERC & 11\% & 43\% \\
251	LLaMA/SciERC & 18\% & 39\% \\
252	Qwen/CoNLL & 57\% & --- \\
253	LLaMA/CoNLL & 88\% & --- \\
254	WNUT-17 & 55\% & --- \\
255	\bottomrule
256	\end{tabular}
257	\end{table}
258	
259	\paragraph{Oracle-improvable fraction.}
260	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
261	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
262	
263	\paragraph{Diversity-stratified selection gap.}
264	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, Voting) select at or below greedy, and logprob---the only per-sample signal---achieves merely $+$0.8~pp.
265	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and logprob captures only $+$2.0~pp.
266	This rules out insufficient diversity as an explanation for the correlation-selection gap.
267	
268	\paragraph{TOST equivalence testing.}
269	Table~\ref{tab:tost} reports two one-sided tests (TOST) results, testing whether each signal's selection F1 is equivalent to greedy within a bound $\delta$.
270	The $\delta$ values reflect practical significance: ${\pm}2$~pp represents a stringent equivalence threshold (smaller than typical inter-annotator disagreement on IE benchmarks), ${\pm}3$~pp a moderate threshold, and ${\pm}5$~pp a lenient bound.
271	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and logprob are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
272	On RE ($n{=}397$), the picture is starker: EM and Voting fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance (mean $\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
273	
274	\begin{table}[t]
275	\centering
276	\small
277	\caption{TOST equivalence testing: signals vs.\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ greedy).}
278	\label{tab:tost}
279	\begin{tabular}{l cccc cccc}
280	\toprule
281	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
282	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
283	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
284	\midrule
285	Log-prob & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
286	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
287	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
288	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
289	Voting & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
290	\bottomrule
291	\end{tabular}
292	\end{table}
293	
294	\section{Multi-Seed Stability}\label{app:multiseed}
295	
296	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC NER ($N{=}8$, $T{=}1.0$).
297	The signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals, confirming that our findings are robust to random seed variation.
298	LLaMA absolute values are systematically lower than Qwen, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
299	
300	\begin{table}[t]
301	\centering
302	\small
303	\caption{Multi-seed quality estimation on SciERC NER ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). Top: Spearman $\rho$; bottom: AUROC. Signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations ($\sigma{\leq}0.025$).}
304	\label{tab:multiseed}
305	\begin{tabular}{lccccc}
306	\toprule
307	& LP & FK & SJ & VC & EM \\
308	\midrule
309	\multicolumn{6}{l}{\textit{Spearman $\rho$ (mean $\pm\sigma$)}} \\
310	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
311	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
312	\midrule
313	\multicolumn{6}{l}{\textit{AUROC (mean $\pm\sigma$)}} \\
314	Qwen & .613${\pm}$.002 & .618${\pm}$.009 & .684${\pm}$.009 & .697${\pm}$.010 & .661${\pm}$.010 \\
315	LLaMA & .577${\pm}$.007 & .616${\pm}$.011 & .655${\pm}$.010 & .689${\pm}$.005 & .636${\pm}$.006 \\
316	\bottomrule
317	\end{tabular}
318	\end{table}
319	
320	\section{Training Configuration}\label{app:training}
321	
322	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure cross-architecture comparisons reflect architectural differences rather than training confounds.
323	
324	\begin{table}[t]
325	\centering
326	\small
327	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
328	\label{tab:training}
329	\begin{tabular}{ll}
330	\toprule
331	Parameter & Value \\
332	\midrule
333	LoRA rank / $\alpha$ & 32 / 64 \\
334	LoRA target & All linear modules \\
335	LoRA dropout & 0 \\
336	Optimizer & AdamW \\
337	Learning rate & 2e-4, cosine schedule \\
338	Warmup ratio & 0.1 \\
339	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
340	Epochs & 5 \\
341	Max sequence length & 2048 \\
342	Precision & bf16 \\
343	Gradient checkpointing & Enabled \\
344	Max gradient norm & 1.0 \\
345	Training seed & 42 \\
346	Framework & LLaMA Factory \\
347	\midrule
348	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
349	SciERC split & 1861 / 275 / 551 \\
350	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
351	& eval\_steps${=}$200, save\_limit${=}$5 \\
352	\bottomrule
353	\end{tabular}
354	\end{table}
355	
356	\paragraph{Prompt template.}
357	For NER, we use a structured prompt:
358	\begin{quote}
359	\small
360	\texttt{System:} You are an expert in Named Entity Recognition.\\
361	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
362	Text: \texttt{\{input\_text\}}\\
363	Entity types: \texttt{\{schema\_types\}}
364	\end{quote}
365	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
366	
367	\paragraph{Constrained decoding.}
368	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
369	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training did not explicitly disable thinking tokens (\texttt{enable\_thinking}); CoNLL and WNUT explicitly set this to false. Constrained decoding at inference time overrides any thinking behavior by enforcing JSON-only output.}
370	
371	\section{Log-Probability Score Compression}\label{app:logprob_ties}
372	
373	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}).
374	The median within-instance logprob range is only 0.041, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
375	At $\varepsilon{=}0.05$, 60.3\% of instances have a within-sample range below the threshold, leaving logprob unable to meaningfully distinguish candidates.
376	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over logprob for selection is one of score resolution, not information content.
377	
378	\begin{table}[t]
379	\centering
380	\small
381	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance logprob range ${<}\varepsilon$.}
382	\label{tab:logprob_ties}
383	\begin{tabular}{lc}
384	\toprule
385	$\varepsilon$ threshold & Tied instances (\%) \\
386	\midrule
387	0.01 & ${\sim}$24\% \\
388	0.05 & 60.3\% \\
389	0.1  & ${\sim}$84\% \\
390	0.5  & ${\sim}$99\% \\
391	\bottomrule
392	\end{tabular}
393	\end{table}
394	
395	\paragraph{Non-tied subset.}
396	Among instances with logprob range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\rho(\text{logprob}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
397	This confirms that logprob carries useful per-sample quality information but is resolution-limited under constrained decoding---the signal exists but is compressed below the discrimination threshold for most instances.
398	
399	\section{RE Conditional Selection}\label{app:re_conditional_selection}
400	
401	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
402	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
403	All five signals underperform greedy on both subsets.
404	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., Voting: $-0.10$~pp vs.\ $-0.03$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
405	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
406	
407	\begin{table}[t]
408	\centering
409	\small
410	\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
411	\label{tab:re_cond_selection}
412	\begin{tabular}{lcc}
413	\toprule
414	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
415	\midrule
416	Oracle & 0.585 & 0.757 \\
417	\midrule
418	Log-prob & 0.395 & 0.662 \\
419	Soft Jaccard & 0.386 & 0.654 \\
420	Exact Match & 0.372 & 0.646 \\
421	Voting & 0.359 & 0.637 \\
422	\midrule
423	Greedy & 0.404 & 0.674 \\
424	\bottomrule
425	\end{tabular}
426	\end{table}
427	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "198977fb-bec5-4cbd-8ff1-c11420ad6c6d",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "8fd6f23b-1095-4be0-b0c1-056091896937",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\n$c_{\\text{vote}}$ & Entity voting confidence \\\\\n$c_{\\text{lp}}$ & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-architecture transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Cross-architecture} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.463{\\pm}0.007$ & --- \\\\\n\\quad FK &  & $0.455{\\pm}0.006$ & --- \\\\\n\\quad EM &  & $0.460{\\pm}0.008$ & --- \\\\\n\\quad Voting &  & $0.458{\\pm}0.003$ & --- \\\\\n\\quad Logprob &  & $0.310{\\pm}0.005$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. Logprob $T{=}0.7$ data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.054, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.360 vs.\\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.052$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while logprob gains only $+0.003$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.\nVoting confidence $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while logprob is approximately $N$-invariant ($\\Delta{\\leq}0.021$).\nSJ, EM, and voting confidence scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.\n\n\\paragraph{Cross-architecture transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.363$, FK $\\rho{=}0.327$).\nOn CoNLL, the cross-architecture gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-logprob advantage holds across all four tested settings: Qwen SciERC (Voting $\\rho{=}0.411$ vs.\\ logprob 0.259, $\\Delta{=}{+}0.152$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ logprob 0.328, $\\Delta{=}{+}0.135$), LLaMA SciERC (Voting $\\rho{=}0.452$ vs.\\ logprob 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.463{\\pm}0.007$ vs.\\ logprob $0.310{\\pm}0.005$, $\\Delta{=}{+}0.153$).\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: Voting reaches $\\rho{=}0.630$, logprob $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for logprob's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while logprob drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17.\nVoting achieves $\\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\\rho{=}0.038$ ($p{=}0.49$).\nLogprob shows the reverse pattern: full-set $\\rho{=}{-}0.410$ but conditional $\\rho{=}0.350$, the highest among all signals on the conditional set.\nThis inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). Logprob exhibits strong negative full-set $\\rho$; its conditional $\\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}\n\\label{tab:wnut}\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & $\\rho$ & $p$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVoting  & .724 & ${<}$1e-112 & .913 & .038 & .487 \\\\\nFK      & .125 & .001 & .555 & .169 & .002 \\\\\nSJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\\\\nLogprob & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), logprob achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn CoNLL, 57--88\\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). SJ: Soft Jaccard, FK: Fleiss' $\\kappa$, EM: Exact Match, LP: Log-prob, VC: Voting Confidence. Best non-oracle signal per row in \\textbf{bold}. No signal significantly outperforms greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2024scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ logprob $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while logprob does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--logprob gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\nThe Voting--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVoting Conf. & +0.379 & [+0.299, +0.456] \\\\\nSoft Jaccard & +0.360 & [+0.277, +0.437] \\\\\nExact Match & +0.295 & [+0.212, +0.371] \\\\\nFleiss' $\\kappa$ & +0.267 & [+0.176, +0.354] \\\\\nLog-prob & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ Logprob & +0.155 & [+0.074, +0.234] & Yes \\\\\nVoting $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 57\\% (Qwen) to 88\\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, confirming the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, Voting) select at or below greedy, and logprob---the only per-sample signal---achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and logprob captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{TOST equivalence testing.}\nTable~\\ref{tab:tost} reports two one-sided tests (TOST) results, testing whether each signal's selection F1 is equivalent to greedy within a bound $\\delta$.\nThe $\\delta$ values reflect practical significance: ${\\pm}2$~pp represents a stringent equivalence threshold (smaller than typical inter-annotator disagreement on IE benchmarks), ${\\pm}3$~pp a moderate threshold, and ${\\pm}5$~pp a lenient bound.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and logprob are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$), the picture is starker: EM and Voting fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance (mean $\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ greedy).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLog-prob & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVoting & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC NER ($N{=}8$, $T{=}1.0$).\nThe signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals, confirming that our findings are robust to random seed variation.\nLLaMA absolute values are systematically lower than Qwen, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC NER ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). Top: Spearman $\\rho$; bottom: AUROC. Signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations ($\\sigma{\\leq}0.025$).}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .613${\\pm}$.002 & .618${\\pm}$.009 & .684${\\pm}$.009 & .697${\\pm}$.010 & .661${\\pm}$.010 \\\\\nLLaMA & .577${\\pm}$.007 & .616${\\pm}$.011 & .655${\\pm}$.010 & .689${\\pm}$.005 & .636${\\pm}$.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure cross-architecture comparisons reflect architectural differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training did not explicitly disable thinking tokens (\\texttt{enable\\_thinking}); CoNLL and WNUT explicitly set this to false. Constrained decoding at inference time overrides any thinking behavior by enforcing JSON-only output.}\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}).\nThe median within-instance logprob range is only 0.041, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nAt $\\varepsilon{=}0.05$, 60.3\\% of instances have a within-sample range below the threshold, leaving logprob unable to meaningfully distinguish candidates.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over logprob for selection is one of score resolution, not information content.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance logprob range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & ${\\sim}$24\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with logprob range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\\rho(\\text{logprob}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nThis confirms that logprob carries useful per-sample quality information but is resolution-limited under constrained decoding---the signal exists but is compressed below the discrimination threshold for most instances.\n\n\\section{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform greedy on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., Voting: $-0.10$~pp vs.\\ $-0.03$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLog-prob & 0.395 & 0.662 \\\\\nSoft Jaccard & 0.386 & 0.654 \\\\\nExact Match & 0.372 & 0.646 \\\\\nVoting & 0.359 & 0.637 \\\\\n\\midrule\nGreedy & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 427,
      "startLine": 1,
      "totalLines": 427
    }
  },
  "sourceToolAssistantUUID": "198977fb-bec5-4cbd-8ff1-c11420ad6c6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T07:53:47.216Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SrogjjwSXZSKTagCM8iALX`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc.), and the exact rubric descriptions for each score level. Include soundness, excitement, overall assessment, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fd6f23b-1095-4be0-b0c1-056091896937",
  "isSidechain": false,
  "requestId": "req_011Cb3zZii275vg2J3MEsM7Y",
  "type": "assistant",
  "uuid": "8cc49ea5-6a2a-47ba-815e-51f7ffdbd98a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019b8CkDYUCGKeLPnpSLUt2b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 46507,
      "output_tokens": 796,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 796,
          "cache_read_input_tokens": 46507,
          "cache_creation_input_tokens": 1189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1189
          },
          "type": "message"
        }
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

_source line 58_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2 (Round 1)  ### Venue 信息 - **Target**: EMNLP 2026 Findings (via ARR May 2026 cycle) - **Deadline**: 2026-05-25 - **页数限制**: 正文 8 页 + unlimited references - **模板**: A…",
  "leafUuid": "8cc49ea5-6a2a-47ba-815e-51f7ffdbd98a",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on structured self-consistency for IE",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74"
}
```

---

### Tool result

_source line 60 · 2026-05-15T07:53:52.388Z_

<details><summary>↩ Tool result · `toolu_01SrogjjwSXZSKTagCM8iALX`</summary>

```text
# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. Reviewer Confidence (1-5 Scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. Soundness (1-5 Scale with Half-Points)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. Excitement (1-5 Scale with Half-Points)
Ranges from "Highly Exciting" (5) through "Interesting" (3) to "Not Exciting" (1), emphasizing subjective assessment of innovation, impact, and relevance.

## 4. Overall Assessment (1-5 Scale with Half-Points)
- **5**: "Consider for Award"
- **4**: "Conference acceptance"
- **3**: "Findings publication"
- **2**: "Resubmit next cycle"
- **1**: "Do not resubmit"

## Additional Dimensions
- Reproducibility (1-5)
- Dataset Value (1-5)
- Software Value (1-5)
- Author Identity Knowledge (1-5)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8cc49ea5-6a2a-47ba-815e-51f7ffdbd98a",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "0458048f-6420-470b-a79e-d9bb70b45836",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Complete Scoring Dimensions\n\n## 1. Reviewer Confidence (1-5 Scale)\n- **5**: \"Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work.\"\n- **4**: \"Quite sure. I tried to check the important points carefully.\"\n- **3**: \"Pretty sure, but there's a chance I missed something.\"\n- **2**: \"Willing to defend my evaluation, but it is fairly likely that I missed some details.\"\n- **1**: \"Not my area, or paper is very hard to understand.\"\n\n## 2. Soundness (1-5 Scale with Half-Points)\n- **5**: \"Excellent: This study is one of the most thorough I have seen.\"\n- **4**: \"Strong: This study provides sufficient support for all of its claims.\"\n- **3**: \"Acceptable: This study provides sufficient support for its main claims.\"\n- **2**: \"Poor: Some of the main claims are not sufficiently supported.\"\n- **1**: \"Major Issues: This study is not yet sufficiently thorough to warrant publication.\"\n\n## 3. Excitement (1-5 Scale with Half-Points)\nRanges from \"Highly Exciting\" (5) through \"Interesting\" (3) to \"Not Exciting\" (1), emphasizing subjective assessment of innovation, impact, and relevance.\n\n## 4. Overall Assessment (1-5 Scale with Half-Points)\n- **5**: \"Consider for Award\"\n- **4**: \"Conference acceptance\"\n- **3**: \"Findings publication\"\n- **2**: \"Resubmit next cycle\"\n- **1**: \"Do not resubmit\"\n\n## Additional Dimensions\n- Reproducibility (1-5)\n- Dataset Value (1-5)\n- Software Value (1-5)\n- Author Identity Knowledge (1-5)",
    "durationMs": 5169,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "8cc49ea5-6a2a-47ba-815e-51f7ffdbd98a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 61 · 2026-05-15T07:53:52.392Z_

```json
{
  "parentUuid": "0458048f-6420-470b-a79e-d9bb70b45836",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a14299d1-1adb-4293-a80c-3546f25cb84b",
  "timestamp": "2026-05-15T07:53:52.392Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 62 · 2026-05-15T07:54:45.692Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the paper content and the ARR review form. Let me also check the references file for completeness and search for potentially missing references.

Let me compile my review. Let me think through each dimension carefully.

Key observations from reading:

**Paper Summary**: The paper compares 5 confidence signals (3 families: structural, surface, model-internal) for test-time scaling in generative IE (NER + RE). The central finding is the "correlation-selection gap": signals correlate with quality but can't select the best sample. 4/5 signals are instance-level by construction (can't distinguish samples), and logprob (per-sample) is compressed under constrained decoding.
 
**Novelty Assessment**: The core issue is whether the correlation-selection gap is actually a finding or just a tautology. Four of the five signals are instance-level by definition—they produce a single score per input regardless of how many samples are generated—so their inability to rank samples is definitional rather than empirical. The paper itself acknowledges this limitation. The only potentially non-trivial observation is logprob's failure, but that stems from constrained decoding compressing the probability distribution, which is a known technical constraint rather than a surprising discovery.

Comparing to Nédellec et al., this work adds structural matching via Soft Jaccard and a selection analysis framework, but I'm questioning whether these additions constitute a substantial enough advance. The Soft Jaccard metric itself is a contribution, though I need to assess whether the overall package moves the field forward meaningfully.

Looking at the three main contributions: the multi-family comparison is solid empirical work with somewhat expected findings, the correlation-selection gap partly collapses under scrutiny (it's tautological by design and partly an artifact of constrained decoding), and the task-complexity boundary is a useful but intuitive observation. The framing around being the "first multi-family comparison" also needs examination.

The abstract is extremely dense, cramming five signals, three families, specific metrics, three datasets, and two models into a tight space. There's also an inconsistency where RE is labeled "preliminary" yet dominates the results throughout the paper—Tables 1-2, Figures 1-3, and the discussion all rely heavily on it. The paper frames a negative finding (signals failing for selection) as a contribution, which could work if the result were surprising and well-characterized, but the tautological reasoning underlying the instance-level argument undermines this framing.

Looking at the related work, the paper cites 58 references with decent coverage of LLM confidence and uncertainty estimation, self-consistency variants, and relevant surveys. There are some gaps though—MBR gets discussed mainly through machine translation references when it could draw from summarization and dialogue work, and structured prediction uncertainty could be better represented.

I'm noticing a few missing citations that would strengthen the work: Lin et al.'s piece on confidence from consistency, and more from the selective prediction literature for structured tasks beyond Geifman 2017. The terminology around "confidence signal" versus "consistency signal" is defined but could be clearer—they use "confidence signal" as the umbrella term with "consistency signal" covering 4 of 5 approaches, which works but feels slightly imprecise.

There's also an inconsistency in how they abbreviate voting confidence across tables—some use "Voting Conf." and others use "VC"—which should be standardized. The paper itself is dense but well-structured with detailed, mostly self-contained figure captions. Format-wise it looks compliant with the ACL review template, includes the required limitations and ethics sections, though I can't verify the exact page count without compiling. A couple of references didn't show up in OpenAlex (hobelsberger2025systematic and lightman2024verify, though Lightman is definitely a known paper so that's likely an indexing gap), and there are a few reference mismatches to flag like feng2025optimal.

Now I'm settling on my scores: the experiments are rigorous and well-designed but the central correlation-selection gap feels somewhat tautological, which weakens the theoretical contribution. The findings are useful but not particularly exciting—the core negative result is partly definitional. Overall this lands at a 3 out of 5, with soundness at 3.5 and excitement at 2.5. I'm confident in this assessment given my familiarity with the area, and reproducibility looks solid with good experimental detail. Time to write the full review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a14299d1-1adb-4293-a80c-3546f25cb84b",
  "isSidechain": false,
  "requestId": "req_011Cb3zajC5HGH6VVgKKfP2B",
  "type": "assistant",
  "uuid": "bebdfe59-89fc-4c8d-89b7-c415383e1aae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuC6EDpPGqwp9zAsha1MwV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25129,
      "cache_read_input_tokens": 47696,
      "output_tokens": 2022,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2022,
          "cache_read_input_tokens": 47696,
          "cache_creation_input_tokens": 25129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25129
          },
          "type": "message"
        }
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

_source line 63 · 2026-05-15T07:54:45.700Z_

论文全文和 ARR 审稿标准已读完。现在搜索可能遗漏的相关工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bebdfe59-89fc-4c8d-89b7-c415383e1aae",
  "isSidechain": false,
  "requestId": "req_011Cb3zajC5HGH6VVgKKfP2B",
  "type": "assistant",
  "uuid": "e0291ce8-1710-406c-9c23-209089ad0fdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuC6EDpPGqwp9zAsha1MwV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25129,
      "cache_read_input_tokens": 47696,
      "output_tokens": 2022,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2022,
          "cache_read_input_tokens": 47696,
          "cache_creation_input_tokens": 25129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25129
          },
          "type": "message"
        }
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

_source line 64 · 2026-05-15T07:54:45.704Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AXxVQiykR1dxxPGb6ceZB1`</summary>

```json
{
  "query": "self-consistency structured prediction information extraction LLM confidence 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0291ce8-1710-406c-9c23-209089ad0fdf",
  "isSidechain": false,
  "requestId": "req_011Cb3zajC5HGH6VVgKKfP2B",
  "type": "assistant",
  "uuid": "0d7a8278-f156-4795-b151-bca1b370f9e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuC6EDpPGqwp9zAsha1MwV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25129,
      "cache_read_input_tokens": 47696,
      "output_tokens": 2022,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2022,
          "cache_read_input_tokens": 47696,
          "cache_creation_input_tokens": 25129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25129
          },
          "type": "message"
        }
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

_source line 65 · 2026-05-15T07:54:45.938Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QEgrrQwY9M48TdbqZVuw4E`</summary>

```json
{
  "query": "MBR decoding beyond machine translation NER relation extraction structured output 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d7a8278-f156-4795-b151-bca1b370f9e2",
  "isSidechain": false,
  "requestId": "req_011Cb3zajC5HGH6VVgKKfP2B",
  "type": "assistant",
  "uuid": "8693a1dd-85f8-4b04-aaea-50a6a8f95c64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuC6EDpPGqwp9zAsha1MwV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25129,
      "cache_read_input_tokens": 47696,
      "output_tokens": 2022,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2022,
          "cache_read_input_tokens": 47696,
          "cache_creation_input_tokens": 25129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25129
          },
          "type": "message"
        }
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

_source line 66 · 2026-05-15T07:54:46.469Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013L5BctuPFe5QEUbCnbiBYx`</summary>

```json
{
  "query": "\"best-of-N\" selection structured prediction information extraction LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8693a1dd-85f8-4b04-aaea-50a6a8f95c64",
  "isSidechain": false,
  "requestId": "req_011Cb3zajC5HGH6VVgKKfP2B",
  "type": "assistant",
  "uuid": "47a24c23-d6aa-47cc-9398-20dd82da71e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuC6EDpPGqwp9zAsha1MwV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25129,
      "cache_read_input_tokens": 47696,
      "output_tokens": 2022,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2022,
          "cache_read_input_tokens": 47696,
          "cache_creation_input_tokens": 25129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25129
          },
          "type": "message"
        }
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

_source line 67 · 2026-05-15T07:54:52.348Z_

<details><summary>↩ Tool result · `toolu_01AXxVQiykR1dxxPGb6ceZB1`</summary>

```text
Web search results for query: "self-consistency structured prediction information extraction LLM confidence 2025 2026"

Links: [{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/html/2502.06233v1"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://aclanthology.org/2025.findings-acl.1030.pdf"},{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/"},{"title":"Towards Reliable LLM Grading Through Self-Consistency and Selective Human Review: Higher Accuracy, Less Work","url":"https://www.mdpi.com/2504-4990/8/3/74"},{"title":"Frontiers | An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1609097/full"},{"title":"Confidence Improves Self-Consistency in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1030/"},{"title":"Stability Evaluation of Confidence Features Across Model and Data Variants in Large Language Models — Research and Science Today","url":"https://www.rstjournal.com/article/4.2026"},{"title":"[2502.06233] Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/abs/2502.06233"}]

I've completed the web search for your query on self-consistency, structured prediction, information extraction, and LLM confidence. Here are the key findings:

## Recent Research Highlights (2025-2026)

**Self-Consistency with Confidence Integration**

Reliability-Aware Adaptive Self-Consistency (ReASC) is an adaptive self-consistency framework that incorporates a self-certainty variant as a response-level reliability signal to guide evidence accumulation at inference time. Response-level reliability can be captured from model confidence signals during generation, which provide instance-specific information about how strongly the model supports a given response.

**Confidence-Informed Self-Consistency (CISC)**

When tested on nine models and four datasets, CISC outperforms self-consistency in nearly all configurations, reducing the required number of reasoning paths by over 40% on average. CISC performs a weighted majority vote based on confidence scores obtained directly from the model, and by prioritizing high-confidence paths, it can identify the correct answer with a significantly smaller sample size.

**Information Extraction Applications**

In structured prediction tasks, consistency should be measured at the semantic level, ignoring superficial variations in format or wording, with important implications for using self-consistency as a confidence filter and for designing reliable generative IE pipelines.

**Ongoing Challenges**

While some positive correlation between accuracy and consistency exists, it is model-dependent and varies with task complexity. Standard evaluation methods are poor predictors of success in distinguishing correct and incorrect answers to the same question, and the most calibrated confidence method proved to be the least effective for CISC.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d7a8278-f156-4795-b151-bca1b370f9e2",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "d76375e4-69d6-4043-b80b-66fd383835f8",
  "toolUseResult": {
    "query": "self-consistency structured prediction information extraction LLM confidence 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016dYNB41JMqN1H3mVG8qhc2",
        "content": [
          {
            "title": "Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning",
            "url": "https://arxiv.org/html/2601.02970v1"
          },
          {
            "title": "Confidence Improves Self-Consistency in LLMs",
            "url": "https://arxiv.org/html/2502.06233v1"
          },
          {
            "title": "Confidence Improves Self-Consistency in LLMs",
            "url": "https://aclanthology.org/2025.findings-acl.1030.pdf"
          },
          {
            "title": "Self-Consistency Sampling in LLMs",
            "url": "https://www.emergentmind.com/topics/self-consistency-sampling"
          },
          {
            "title": "Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/"
          },
          {
            "title": "Towards Reliable LLM Grading Through Self-Consistency and Selective Human Review: Higher Accuracy, Less Work",
            "url": "https://www.mdpi.com/2504-4990/8/3/74"
          },
          {
            "title": "Frontiers | An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability",
            "url": "https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1609097/full"
          },
          {
            "title": "Confidence Improves Self-Consistency in LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.1030/"
          },
          {
            "title": "Stability Evaluation of Confidence Features Across Model and Data Variants in Large Language Models — Research and Science Today",
            "url": "https://www.rstjournal.com/article/4.2026"
          },
          {
            "title": "[2502.06233] Confidence Improves Self-Consistency in LLMs",
            "url": "https://arxiv.org/abs/2502.06233"
          }
        ]
      },
      "I've completed the web search for your query on self-consistency, structured prediction, information extraction, and LLM confidence. Here are the key findings:\n\n## Recent Research Highlights (2025-2026)\n\n**Self-Consistency with Confidence Integration**\n\nReliability-Aware Adaptive Self-Consistency (ReASC) is an adaptive self-consistency framework that incorporates a self-certainty variant as a response-level reliability signal to guide evidence accumulation at inference time. Response-level reliability can be captured from model confidence signals during generation, which provide instance-specific information about how strongly the model supports a given response.\n\n**Confidence-Informed Self-Consistency (CISC)**\n\nWhen tested on nine models and four datasets, CISC outperforms self-consistency in nearly all configurations, reducing the required number of reasoning paths by over 40% on average. CISC performs a weighted majority vote based on confidence scores obtained directly from the model, and by prioritizing high-confidence paths, it can identify the correct answer with a significantly smaller sample size.\n\n**Information Extraction Applications**\n\nIn structured prediction tasks, consistency should be measured at the semantic level, ignoring superficial variations in format or wording, with important implications for using self-consistency as a confidence filter and for designing reliable generative IE pipelines.\n\n**Ongoing Challenges**\n\nWhile some positive correlation between accuracy and consistency exists, it is model-dependent and varies with task complexity. Standard evaluation methods are poor predictors of success in distinguishing correct and incorrect answers to the same question, and the most calibrated confidence method proved to be the least effective for CISC."
    ],
    "durationSeconds": 6.639459585000004
  },
  "sourceToolAssistantUUID": "0d7a8278-f156-4795-b151-bca1b370f9e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 68_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2 (Round 1)  ### Venue 信息 - **Target**: EMNLP 2026 Findings (via ARR May 2026 cycle) - **Deadline**: 2026-05-25 - **页数限制**: 正文 8 页 + unlimited references - **模板**: A…",
  "leafUuid": "d76375e4-69d6-4043-b80b-66fd383835f8",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on structured self-consistency for IE",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74"
}
```

---

### Tool result

_source line 70 · 2026-05-15T07:54:53.095Z_

<details><summary>↩ Tool result · `toolu_01QEgrrQwY9M48TdbqZVuw4E`</summary>

```text
Web search results for query: "MBR decoding beyond machine translation NER relation extraction structured output 2024 2025"

Links: [{"title":"[1911.09886] Effective Modeling of Encoder-Decoder Architecture for Joint Entity and Relation Extraction","url":"https://ar5iv.labs.arxiv.org/html/1911.09886"},{"title":"Effective Modeling of Encoder-Decoder Architecture for ...","url":"https://arxiv.org/pdf/1911.09886"},{"title":"Structured information extraction from scientific text with large language models | Nature Communications","url":"https://www.nature.com/articles/s41467-024-45563-x"},{"title":"Information Extraction: NER, Relations, and Structured Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/information-extraction"},{"title":"(PDF) Lattice Minimum Bayes-Risk Decoding for Statistical Machine Translation","url":"https://www.academia.edu/6354227/Lattice_Minimum_Bayes_Risk_Decoding_for_Statistical_Machine_Translation"},{"title":"Lattice Minimum Bayes-Risk Decoding for Statistical Machine Translation. | Request PDF","url":"https://www.researchgate.net/publication/221012583_Lattice_Minimum_Bayes-Risk_Decoding_for_Statistical_Machine_Translation"},{"title":"Foundation Models for Information Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-23190-2_5"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"Structured Language Generation Model: Loss Calibration and Formatted Decoding for Robust Structure Prediction and Knowledge Retrieval","url":"https://arxiv.org/html/2402.08971"},{"title":"Unveiling the Power of Source: Source-based Minimum Bayes Risk Decoding for Neural Machine Translation","url":"https://arxiv.org/html/2406.11632"}]

Based on the search results, I found relevant information about applications of MBR (Minimum Bayes-Risk) decoding and structured output tasks like NER and relation extraction. Here's what the research shows:

## MBR Decoding: Origins and Evolution

MBR decoding for statistical machine translation is a statistical approach that aims to minimize expected loss of translation errors under loss functions that measure translation performance. However, recent work has expanded its application beyond traditional machine translation.

## MBR Decoding Beyond Machine Translation

MBR decoding has been used in speech recognition, word alignment, and statistical machine translation. More recently, Minimum Bayes Risk decoding offers an alternative to maximum a posteriori decoding by seeking hypotheses with the highest expected utility with respect to a set of hypotheses called "support hypotheses".

A 2025 paper proposes source-based MBR (sMBR) decoding, which uses quasi-sources generated by paraphrasing or back-translation as "support hypotheses" and a QE metric as the utility function, marking the first work to solely use sources as support hypotheses in MBR decoding.

## Structured Output and Information Extraction

For NER and relation extraction with structured outputs, a recent framework (SLGM) reformulates structured prediction as a classification problem through reinforced input formatting with structural cues, loss design, and format-aware decoding that constrains generation to task-valid outputs. Formatted decoding is helpful for extracting the correct tagsets.

Additionally, records can be extracted from single sentences or entire paragraphs, and the output can be returned as simple English sentences or a more structured format such as a list of JSON objects.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8693a1dd-85f8-4b04-aaea-50a6a8f95c64",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "01c1e7f7-a56c-4af8-bb1c-39039dbab8da",
  "toolUseResult": {
    "query": "MBR decoding beyond machine translation NER relation extraction structured output 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Pg7yb9mh5W93UV7Fjp8pC5",
        "content": [
          {
            "title": "[1911.09886] Effective Modeling of Encoder-Decoder Architecture for Joint Entity and Relation Extraction",
            "url": "https://ar5iv.labs.arxiv.org/html/1911.09886"
          },
          {
            "title": "Effective Modeling of Encoder-Decoder Architecture for ...",
            "url": "https://arxiv.org/pdf/1911.09886"
          },
          {
            "title": "Structured information extraction from scientific text with large language models | Nature Communications",
            "url": "https://www.nature.com/articles/s41467-024-45563-x"
          },
          {
            "title": "Information Extraction: NER, Relations, and Structured Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer",
            "url": "https://mbrenndoerfer.com/writing/information-extraction"
          },
          {
            "title": "(PDF) Lattice Minimum Bayes-Risk Decoding for Statistical Machine Translation",
            "url": "https://www.academia.edu/6354227/Lattice_Minimum_Bayes_Risk_Decoding_for_Statistical_Machine_Translation"
          },
          {
            "title": "Lattice Minimum Bayes-Risk Decoding for Statistical Machine Translation. | Request PDF",
            "url": "https://www.researchgate.net/publication/221012583_Lattice_Minimum_Bayes-Risk_Decoding_for_Statistical_Machine_Translation"
          },
          {
            "title": "Foundation Models for Information Extraction | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-031-23190-2_5"
          },
          {
            "title": "A survey on cutting-edge relation extraction techniques based on language models",
            "url": "https://arxiv.org/html/2411.18157v1"
          },
          {
            "title": "Structured Language Generation Model: Loss Calibration and Formatted Decoding for Robust Structure Prediction and Knowledge Retrieval",
            "url": "https://arxiv.org/html/2402.08971"
          },
          {
            "title": "Unveiling the Power of Source: Source-based Minimum Bayes Risk Decoding for Neural Machine Translation",
            "url": "https://arxiv.org/html/2406.11632"
          }
        ]
      },
      "Based on the search results, I found relevant information about applications of MBR (Minimum Bayes-Risk) decoding and structured output tasks like NER and relation extraction. Here's what the research shows:\n\n## MBR Decoding: Origins and Evolution\n\nMBR decoding for statistical machine translation is a statistical approach that aims to minimize expected loss of translation errors under loss functions that measure translation performance. However, recent work has expanded its application beyond traditional machine translation.\n\n## MBR Decoding Beyond Machine Translation\n\nMBR decoding has been used in speech recognition, word alignment, and statistical machine translation. More recently, Minimum Bayes Risk decoding offers an alternative to maximum a posteriori decoding by seeking hypotheses with the highest expected utility with respect to a set of hypotheses called \"support hypotheses\".\n\nA 2025 paper proposes source-based MBR (sMBR) decoding, which uses quasi-sources generated by paraphrasing or back-translation as \"support hypotheses\" and a QE metric as the utility function, marking the first work to solely use sources as support hypotheses in MBR decoding.\n\n## Structured Output and Information Extraction\n\nFor NER and relation extraction with structured outputs, a recent framework (SLGM) reformulates structured prediction as a classification problem through reinforced input formatting with structural cues, loss design, and format-aware decoding that constrains generation to task-valid outputs. Formatted decoding is helpful for extracting the correct tagsets.\n\nAdditionally, records can be extracted from single sentences or entire paragraphs, and the output can be returned as simple English sentences or a more structured format such as a list of JSON objects."
    ],
    "durationSeconds": 7.153118543000018
  },
  "sourceToolAssistantUUID": "8693a1dd-85f8-4b04-aaea-50a6a8f95c64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-15T07:54:53.750Z_

<details><summary>↩ Tool result · `toolu_013L5BctuPFe5QEUbCnbiBYx`</summary>

```text
Web search results for query: ""best-of-N" selection structured prediction information extraction LLM 2025"

Links: [{"title":"Leveraging large language models for structured information extraction from pathology reports - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2153353925001075"},{"title":"Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Large language model driven transferable key information ...","url":"https://www.nature.com/articles/s41598-025-15627-z.pdf"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"Data+AI: LLM4Data and Data4LLM Guoliang Li Tsinghua University Beijing, China","url":"https://dbgroup.cs.tsinghua.edu.cn/ligl/papers/SIGMOD2025-Data+AI.pdf"},{"title":"End-to-End Structured Extraction with LLM – Part 1... - Databricks Community - 98396","url":"https://community.databricks.com/t5/technical-blog/end-to-end-structured-extraction-with-llm-part-1-batch-entity/ba-p/98396"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"StructEval: Benchmarking LLMs’ Capabilities to Generate Structural Outputs","url":"https://arxiv.org/html/2505.20139v1"},{"title":"arXiv:2505.18458v3 [cs.DB] 1 Jun 2025 1 A Survey of LLM × DATA","url":"https://arxiv.org/pdf/2505.18458"}]

I've completed the web search for your query on "best-of-N" selection structured prediction information extraction LLM 2025. Here's what the search results revealed:

## Key Findings:

The search results contain recent research on **structured information extraction with LLMs** from 2025, though they don't specifically focus on "best-of-N" selection methods. Here are the most relevant findings:

### Structured Information Extraction Advances:
Large language models offer efficient automated extraction through zero-shot prompting, requiring only natural language instructions without labeled data or training.

### Enhanced Reasoning Models:
Recent models include OpenAI's o1 and o3, Google's Gemini 2.0 Flash Thinking, and DeepSeek-R1, which come with significantly higher latency and costs due to extended runtime computation.

### LLM-Based Tools and Benchmarks:
Recent 2025 research includes "SLOT: Structuring the Output of Large Language Models" and "StructEval: Benchmarking LLMs' Capabilities to Generate Structural Outputs," which evaluate how well LLMs can generate structured data outputs in various formats.

### Information Extraction Applications:
LLMs have recently shown great promise for automated digitization and information extraction, greatly improving upon previous tools in terms of speed and accuracy.

**Note:** The search results focus on general structured information extraction rather than specifically addressing "best-of-N" selection as a technique for structured prediction. If you're looking for more specific research on best-of-N selection methods, I may need to conduct a more targeted search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47a24c23-d6aa-47cc-9398-20dd82da71e7",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "c62ea83a-b445-4d77-a13b-58c3af13e901",
  "toolUseResult": {
    "query": "\"best-of-N\" selection structured prediction information extraction LLM 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_014npJfZ8pG35xPK2b9Tw8Jz",
        "content": [
          {
            "title": "Leveraging large language models for structured information extraction from pathology reports - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S2153353925001075"
          },
          {
            "title": "Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"
          },
          {
            "title": "Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11704-024-40555-y"
          },
          {
            "title": "Large language model driven transferable key information ...",
            "url": "https://www.nature.com/articles/s41598-025-15627-z.pdf"
          },
          {
            "title": "SLOT: Structuring the Output of Large Language Models",
            "url": "https://aclanthology.org/2025.emnlp-industry.32.pdf"
          },
          {
            "title": "Data+AI: LLM4Data and Data4LLM Guoliang Li Tsinghua University Beijing, China",
            "url": "https://dbgroup.cs.tsinghua.edu.cn/ligl/papers/SIGMOD2025-Data+AI.pdf"
          },
          {
            "title": "End-to-End Structured Extraction with LLM – Part 1... - Databricks Community - 98396",
            "url": "https://community.databricks.com/t5/technical-blog/end-to-end-structured-extraction-with-llm-part-1-batch-entity/ba-p/98396"
          },
          {
            "title": "Benchmarking LLM-based Information Extraction Tools for ...",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"
          },
          {
            "title": "StructEval: Benchmarking LLMs’ Capabilities to Generate Structural Outputs",
            "url": "https://arxiv.org/html/2505.20139v1"
          },
          {
            "title": "arXiv:2505.18458v3 [cs.DB] 1 Jun 2025 1 A Survey of LLM × DATA",
            "url": "https://arxiv.org/pdf/2505.18458"
          }
        ]
      },
      "I've completed the web search for your query on \"best-of-N\" selection structured prediction information extraction LLM 2025. Here's what the search results revealed:\n\n## Key Findings:\n\nThe search results contain recent research on **structured information extraction with LLMs** from 2025, though they don't specifically focus on \"best-of-N\" selection methods. Here are the most relevant findings:\n\n### Structured Information Extraction Advances:\nLarge language models offer efficient automated extraction through zero-shot prompting, requiring only natural language instructions without labeled data or training.\n\n### Enhanced Reasoning Models:\nRecent models include OpenAI's o1 and o3, Google's Gemini 2.0 Flash Thinking, and DeepSeek-R1, which come with significantly higher latency and costs due to extended runtime computation.\n\n### LLM-Based Tools and Benchmarks:\nRecent 2025 research includes \"SLOT: Structuring the Output of Large Language Models\" and \"StructEval: Benchmarking LLMs' Capabilities to Generate Structural Outputs,\" which evaluate how well LLMs can generate structured data outputs in various formats.\n\n### Information Extraction Applications:\nLLMs have recently shown great promise for automated digitization and information extraction, greatly improving upon previous tools in terms of speed and accuracy.\n\n**Note:** The search results focus on general structured information extraction rather than specifically addressing \"best-of-N\" selection as a technique for structured prediction. If you're looking for more specific research on best-of-N selection methods, I may need to conduct a more targeted search."
    ],
    "durationSeconds": 7.277823613999994
  },
  "sourceToolAssistantUUID": "47a24c23-d6aa-47cc-9398-20dd82da71e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-15T07:54:56.990Z_

<details><summary>Logged reasoning block</summary>

```text
Let me also search for a few more specific potentially missing references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c62ea83a-b445-4d77-a13b-58c3af13e901",
  "isSidechain": false,
  "requestId": "req_011Cb3zfFcGt2KoZ1RUU8dZA",
  "type": "assistant",
  "uuid": "e0a4a870-750e-4cf8-b2c9-3aba5f27b863",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBuUnbByxnrSn9m4MuC4zy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4854,
      "cache_read_input_tokens": 72825,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 72825,
          "cache_creation_input_tokens": 4854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4854
          },
          "type": "message"
        }
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

_source line 73 · 2026-05-15T07:55:00.536Z_

搜索更多可能遗漏的核心文献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0a4a870-750e-4cf8-b2c9-3aba5f27b863",
  "isSidechain": false,
  "requestId": "req_011Cb3zfFcGt2KoZ1RUU8dZA",
  "type": "assistant",
  "uuid": "e4a12eab-5839-4a97-9c71-97d919db9efb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBuUnbByxnrSn9m4MuC4zy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4854,
      "cache_read_input_tokens": 72825,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 72825,
          "cache_creation_input_tokens": 4854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4854
          },
          "type": "message"
        }
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

_source line 74 · 2026-05-15T07:55:00.891Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XcsZkeVbYNUy9tsAXCo7tV`</summary>

```json
{
  "query": "Huang et al 2025 \"uncertainty quantification\" \"information extraction\" generative LLM NER"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4a12eab-5839-4a97-9c71-97d919db9efb",
  "isSidechain": false,
  "requestId": "req_011Cb3zfFcGt2KoZ1RUU8dZA",
  "type": "assistant",
  "uuid": "95f9e746-efc0-4e5d-822e-7d9a2b4ff5f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBuUnbByxnrSn9m4MuC4zy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4854,
      "cache_read_input_tokens": 72825,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 72825,
          "cache_creation_input_tokens": 4854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4854
          },
          "type": "message"
        }
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

_source line 75 · 2026-05-15T07:55:00.941Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F5Zczy2RpLtmPqT7ktEVmr`</summary>

```json
{
  "query": "\"test-time compute\" \"structured output\" selection verifier reward model NER 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95f9e746-efc0-4e5d-822e-7d9a2b4ff5f3",
  "isSidechain": false,
  "requestId": "req_011Cb3zfFcGt2KoZ1RUU8dZA",
  "type": "assistant",
  "uuid": "9d6abd4a-6b5e-4e10-84f5-302d45ed35bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBuUnbByxnrSn9m4MuC4zy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4854,
      "cache_read_input_tokens": 72825,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 72825,
          "cache_creation_input_tokens": 4854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4854
          },
          "type": "message"
        }
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

_source line 76 · 2026-05-15T07:55:07.389Z_

<details><summary>↩ Tool result · `toolu_01XcsZkeVbYNUy9tsAXCo7tV`</summary>

```text
Web search results for query: "Huang et al 2025 "uncertainty quantification" "information extraction" generative LLM NER"

Links: [{"title":"Uncertainty quantification by large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666827025001562"},{"title":"IUQ: Interrogative Uncertainty Quantification for Long-Form Large Language Model Generation","url":"https://arxiv.org/html/2604.15109"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Uncertainty Quantification for Hallucination Detection in Large Language Models: Foundations, Methodology, and Future Directions","url":"https://arxiv.org/html/2510.12040"},{"title":"A Survey of Uncertainty Estimation Methods on Large ...","url":"https://aclanthology.org/2025.findings-acl.1101.pdf"},{"title":"Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey","url":"https://arxiv.org/html/2503.15850v1"},{"title":"Uncertainty Quantification of Large Language Models through Multi-Dimensional Responses","url":"https://arxiv.org/html/2502.16820v2"},{"title":"Simple Yet Effective: An Information-Theoretic Approach to Multi-LLM Uncertainty Quantification - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12702469/"},{"title":"Uncertainty Quantification for LLM-Based Survey Simulations Chengpiao Huang∗","url":"https://arxiv.org/pdf/2502.17773v1"},{"title":"Uncertainty Quantification and Decomposition for LLM-based Recommendation | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714601"}]

I found several results related to your search query. Here's what I discovered:

## Key Findings

The search results reference multiple works by Huang et al. from 2025 related to uncertainty quantification in large language models, though I found limited specific information about a work directly combining all your specified keywords (uncertainty quantification, information extraction, generative LLM, and NER).

### Relevant 2025 Works by Huang et al.:

Huang et al. 2025 discusses how LLMs remain susceptible to hallucination, generating plausible answers that are factually incorrect. This appears in the context of work on uncertainty quantification methods.

Huang et al. 2025a has categorized types of hallucination in LLMs, distinguishing between factuality hallucinations and other types.

Additionally, prior surveys including Huang et al. 2025a focus on hallucination detection in the context of uncertainty quantification for LLMs.

### Related Research Areas:

Recent work on NER with LLMs includes ConsistNER, which aims toward instructive NER demonstrations for LLMs with consistency of ontology and context.

The search results show active research on uncertainty quantification in LLMs and information extraction tasks, but I did not find a single paper that explicitly combines all your specified keywords. If you're looking for a specific paper, I'd recommend checking the references in the survey papers on uncertainty quantification in LLMs that appeared in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95f9e746-efc0-4e5d-822e-7d9a2b4ff5f3",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "73310e05-ca37-4c11-956f-f2680360b352",
  "toolUseResult": {
    "query": "Huang et al 2025 \"uncertainty quantification\" \"information extraction\" generative LLM NER",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TGvEEEd3wxYseSbUwHgxoD",
        "content": [
          {
            "title": "Uncertainty quantification by large language models - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S2666827025001562"
          },
          {
            "title": "IUQ: Interrogative Uncertainty Quantification for Long-Form Large Language Model Generation",
            "url": "https://arxiv.org/html/2604.15109"
          },
          {
            "title": "Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11704-024-40555-y"
          },
          {
            "title": "Uncertainty Quantification for Hallucination Detection in Large Language Models: Foundations, Methodology, and Future Directions",
            "url": "https://arxiv.org/html/2510.12040"
          },
          {
            "title": "A Survey of Uncertainty Estimation Methods on Large ...",
            "url": "https://aclanthology.org/2025.findings-acl.1101.pdf"
          },
          {
            "title": "Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey",
            "url": "https://arxiv.org/html/2503.15850v1"
          },
          {
            "title": "Uncertainty Quantification of Large Language Models through Multi-Dimensional Responses",
            "url": "https://arxiv.org/html/2502.16820v2"
          },
          {
            "title": "Simple Yet Effective: An Information-Theoretic Approach to Multi-LLM Uncertainty Quantification - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12702469/"
          },
          {
            "title": "Uncertainty Quantification for LLM-Based Survey Simulations Chengpiao Huang∗",
            "url": "https://arxiv.org/pdf/2502.17773v1"
          },
          {
            "title": "Uncertainty Quantification and Decomposition for LLM-based Recommendation | Proceedings of the ACM on Web Conference 2025",
            "url": "https://dl.acm.org/doi/10.1145/3696410.3714601"
          }
        ]
      },
      "I found several results related to your search query. Here's what I discovered:\n\n## Key Findings\n\nThe search results reference multiple works by Huang et al. from 2025 related to uncertainty quantification in large language models, though I found limited specific information about a work directly combining all your specified keywords (uncertainty quantification, information extraction, generative LLM, and NER).\n\n### Relevant 2025 Works by Huang et al.:\n\nHuang et al. 2025 discusses how LLMs remain susceptible to hallucination, generating plausible answers that are factually incorrect. This appears in the context of work on uncertainty quantification methods.\n\nHuang et al. 2025a has categorized types of hallucination in LLMs, distinguishing between factuality hallucinations and other types.\n\nAdditionally, prior surveys including Huang et al. 2025a focus on hallucination detection in the context of uncertainty quantification for LLMs.\n\n### Related Research Areas:\n\nRecent work on NER with LLMs includes ConsistNER, which aims toward instructive NER demonstrations for LLMs with consistency of ontology and context.\n\nThe search results show active research on uncertainty quantification in LLMs and information extraction tasks, but I did not find a single paper that explicitly combines all your specified keywords. If you're looking for a specific paper, I'd recommend checking the references in the survey papers on uncertainty quantification in LLMs that appeared in these results."
    ],
    "durationSeconds": 6.49234103000001
  },
  "sourceToolAssistantUUID": "95f9e746-efc0-4e5d-822e-7d9a2b4ff5f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-15T07:55:09.460Z_

<details><summary>↩ Tool result · `toolu_01F5Zczy2RpLtmPqT7ktEVmr`</summary>

```text
Web search results for query: ""test-time compute" "structured output" selection verifier reward model NER 2025 2026"

Links: [{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview","url":"https://openreview.net/forum?id=4FWAwZtd2n"},{"title":"Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=A6Y7AqlzLW"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/html/2508.16665v3"},{"title":"Inference-Time Scaling of Verification: Self-Evolving Deep Research Agents via Test-Time Rubric-Guided Verification","url":"https://arxiv.org/html/2601.15808"},{"title":"2026-01-10 Parallel Test-Time Scaling for Latent Reasoning Models Runyang You1","url":"https://arxiv.org/pdf/2510.07745"},{"title":"Reward Model Generalization for Compute-Aware Test-Time Reasoning | OpenReview","url":"https://openreview.net/forum?id=xaTmmj47Iu"},{"title":"Optimizing Test-Time Compute for LLMs: A Meta-Reinforcement Learning Approach with Cumulative Regret Minimization - MarkTechPost","url":"https://www.marktechpost.com/2025/03/14/optimizing-test-time-compute-for-llms-a-meta-reinforcement-learning-approach-with-cumulative-regret-minimization/"},{"title":"AI Trends 2026: Test-Time Reasoning and the Rise of Reflective Agents","url":"https://huggingface.co/blog/aufklarer/ai-trends-2026-test-time-reasoning-reflective-agen"},{"title":"A Survey on Test-Time Scaling. This blog is based a comprehensive… | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/a-survey-on-test-time-scaling-04b1c1dadb9d"}]

I've found relevant research on test-time compute, structured output, verifier reward models, and related topics. Here are the key findings from your search:

## Test-Time Compute and Verification

Enabling LLMs to improve their outputs by using more test-time compute is a critical step towards building self-improving agents that can operate on open-ended natural language. Two primary mechanisms to scale test-time computation are: (1) searching against dense, process-based verifier reward models (PRMs); and (2) updating the model's distribution over a response adaptively.

## Process Reward Models and Verification

Process reward models (PRMs) are a promising approach for improving reasoning in large language models, providing feedback at each step of a multi-step reasoning trace, improving credit assignment over outcome reward models (ORMs) that only provide feedback at the final step. However, collecting dense, per-step human labels is not scalable, and training PRMs from automatically-labeled data has thus far led to limited gains.

## Recent Developments (2025-2026)

Verifiers serve as reward models that help score the candidate outputs from the decoding process to diligently explore the vast solution space and select the best outcome. VersaPRM augments the MMLU benchmark with synthetic CoT traces and counterfactual variants, expanding PRM training to general-domain tasks.

A trend is using reinforcement learning (RL) to train models to be more reflective and strategic; process reward models give the AI feedback on each step of its reasoning, not just the final result, encouraging it to stay on track and catch errors mid-way.

The search results show active research in this area throughout 2025-2026, with multiple approaches to improving test-time reasoning through verifiers, reward models, and structured output mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d6abd4a-6b5e-4e10-84f5-302d45ed35bb",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "ae92b2cc-dc78-4c69-ae6d-baf82bab79ec",
  "toolUseResult": {
    "query": "\"test-time compute\" \"structured output\" selection verifier reward model NER 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01J7wPTiyYijhetmAAonekkZ",
        "content": [
          {
            "title": "GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub",
            "url": "https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"
          },
          {
            "title": "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=4FWAwZtd2n"
          },
          {
            "title": "Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=A6Y7AqlzLW"
          },
          {
            "title": "Trust but Verify! A Survey on Verification Design for Test-time Scaling",
            "url": "https://arxiv.org/html/2508.16665v3"
          },
          {
            "title": "Inference-Time Scaling of Verification: Self-Evolving Deep Research Agents via Test-Time Rubric-Guided Verification",
            "url": "https://arxiv.org/html/2601.15808"
          },
          {
            "title": "2026-01-10 Parallel Test-Time Scaling for Latent Reasoning Models Runyang You1",
            "url": "https://arxiv.org/pdf/2510.07745"
          },
          {
            "title": "Reward Model Generalization for Compute-Aware Test-Time Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=xaTmmj47Iu"
          },
          {
            "title": "Optimizing Test-Time Compute for LLMs: A Meta-Reinforcement Learning Approach with Cumulative Regret Minimization - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/03/14/optimizing-test-time-compute-for-llms-a-meta-reinforcement-learning-approach-with-cumulative-regret-minimization/"
          },
          {
            "title": "AI Trends 2026: Test-Time Reasoning and the Rise of Reflective Agents",
            "url": "https://huggingface.co/blog/aufklarer/ai-trends-2026-test-time-reasoning-reflective-agen"
          },
          {
            "title": "A Survey on Test-Time Scaling. This blog is based a comprehensive… | by Yanan Chen | Medium",
            "url": "https://medium.com/@yananchen1116/a-survey-on-test-time-scaling-04b1c1dadb9d"
          }
        ]
      },
      "I've found relevant research on test-time compute, structured output, verifier reward models, and related topics. Here are the key findings from your search:\n\n## Test-Time Compute and Verification\n\nEnabling LLMs to improve their outputs by using more test-time compute is a critical step towards building self-improving agents that can operate on open-ended natural language. Two primary mechanisms to scale test-time computation are: (1) searching against dense, process-based verifier reward models (PRMs); and (2) updating the model's distribution over a response adaptively.\n\n## Process Reward Models and Verification\n\nProcess reward models (PRMs) are a promising approach for improving reasoning in large language models, providing feedback at each step of a multi-step reasoning trace, improving credit assignment over outcome reward models (ORMs) that only provide feedback at the final step. However, collecting dense, per-step human labels is not scalable, and training PRMs from automatically-labeled data has thus far led to limited gains.\n\n## Recent Developments (2025-2026)\n\nVerifiers serve as reward models that help score the candidate outputs from the decoding process to diligently explore the vast solution space and select the best outcome. VersaPRM augments the MMLU benchmark with synthetic CoT traces and counterfactual variants, expanding PRM training to general-domain tasks.\n\nA trend is using reinforcement learning (RL) to train models to be more reflective and strategic; process reward models give the AI feedback on each step of its reasoning, not just the final result, encouraging it to stay on track and catch errors mid-way.\n\nThe search results show active research in this area throughout 2025-2026, with multiple approaches to improving test-time reasoning through verifiers, reward models, and structured output mechanisms."
    ],
    "durationSeconds": 8.515352975000017
  },
  "sourceToolAssistantUUID": "9d6abd4a-6b5e-4e10-84f5-302d45ed35bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 78_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2 (Round 1)  ### Venue 信息 - **Target**: EMNLP 2026 Findings (via ARR May 2026 cycle) - **Deadline**: 2026-05-25 - **页数限制**: 正文 8 页 + unlimited references - **模板**: A…",
  "leafUuid": "ae92b2cc-dc78-4c69-ae6d-baf82bab79ec",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74"
}
```

---

### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on structured self-consistency for IE",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74"
}
```

---

### Assistant

_source line 80 · 2026-05-15T07:55:33.926Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to compile my comprehensive review. Let me also check if there's a specific paper on ConsistNER that might be missing from their related work, and check for the "Trust but Verify" survey on verification for test-time scaling.

Actually, let me now write the full review. I have all the information I need.

Let me structure the review following the ARR form and the Director's instructions.

Key findings from my analysis:

**Novelty concerns (my primary focus):**

1. **Correlation-selection gap tautology**: 4/5 signals are instance-level BY DEFINITION — they produce one score for all N samples. 

The core issue is that this isn't really a discovery—it's a mathematical inevitability given how these signals are constructed. The paper does acknowledge this limitation, but then treats it as a meaningful finding anyway. The only genuinely interesting result here is logprob's failure under constrained decoding, though even that breaks down in non-tied instances where logprob actually performs well.

2. **Incremental over Nédellec et al. (2026)**: The paper claims three novel extensions—structural matching, selection analysis, and difficulty gradient—but these feel like natural extensions rather than substantial innovations.

Looking at each one: soft Jaccard's improvement over EM is marginal even after correction, the selection analysis boils down to a tautology, and the difficulty gradient (harder tasks favor complex signals) is fairly intuitive. Soft Jaccard itself is just applying standard Hungarian matching and IoU to entity sets, which is reasonable engineering but not particularly novel.

When I scrutinize the three main contributions, the empirical comparison is solid but incremental given existing work, the selection analysis is partly circular, and the task-complexity boundary is a useful but unsurprising observation. The framing around being the "first multi-family comparison" is narrow enough to possibly hold, but it doesn't add much value, and the abstract is packed so densely it obscures rather than clarifies.

The abstract crams in signals, families, specific numbers, datasets, models, and the gap concept all in one paragraph, which makes it hard to parse. There's also an inconsistency where they label something preliminary but then use it extensively as evidence throughout.

The related work covers a decent range with 58 references and good organization, though there are some gaps—they miss a 2025 survey directly relevant to their verifier discussion, and they could strengthen coverage of MBR work beyond machine translation for structured tasks. The writing itself is generally solid and dense but clear, though there's a minor inconsistency between how they refer to voting confidence. The paper follows the ACL template properly with sections on limitations and ethics included.

Now I'm ready to write up the formal review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae92b2cc-dc78-4c69-ae6d-baf82bab79ec",
  "isSidechain": false,
  "requestId": "req_011Cb3zgQnxBfYNRAKdkHCqn",
  "type": "assistant",
  "uuid": "fde7441d-dcbf-4513-a2df-b3832279cf62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XvMNQmFb3XCmqjGA8eKv7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2122,
      "cache_read_input_tokens": 77679,
      "output_tokens": 7105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2122,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7105,
          "cache_read_input_tokens": 77679,
          "cache_creation_input_tokens": 2122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2122
          },
          "type": "message"
        }
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

_source line 81 · 2026-05-15T07:57:09.777Z_

所有材料已读完，引用已验证。现在撰写完整审稿报告。

---

## 总体评分
**Overall**: 3.0 / 5（Findings publication）
**一句话总结**: 实验设计严谨、统计分析到位的 empirical study，但核心概念贡献"correlation-selection gap"的新颖性因 4/5 信号在定义上就无法做 sample selection 而被大幅削弱——这是一个 tautological observation 被包装成 empirical finding 的 framing 问题。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验严谨（bootstrap CI、TOST、multi-seed），但核心 claim 中的 tautological 成分削弱了论证的 substantiveness |
| Excitement | 2.5/5 | 负面结果对实践有价值，但新颖性有限——核心发现部分来自定义而非实验 |
| Reproducibility | 4/5 | 训练细节、prompt template、超参数、统计测试均有详细描述，开源框架 |
| Confidence | 4/5 | 熟悉 self-consistency、uncertainty estimation、generative IE 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Correlation-selection gap 的核心论证存在 tautological 成分，新颖性不足

- 具体位置：Section 1 (L22–24), Section 5.3, Section 6 (Discussion "Why the gap exists: two layers")
- 问题：论文将"correlation-selection gap"作为三个 contribution 之一（C2），但 4/5 信号（EM、FK、SJ、Voting）是 **instance-level by definition**——它们对同一 input 的所有 N 个 sample 产生同一个分数。论文自己也承认："they cannot rank candidates **by construction**"（Section 5.3, L121; Discussion Layer 1）。这意味着这 4 个信号的"selection failure"不是实验发现，而是定义的逻辑后果。将一个 definitional impossibility 包装为"gap"并命名为 contribution，exaggerates the novelty。

  真正 non-trivial 的发现只有 logprob 的失败——但论文在 Appendix F 中也已解释：constrained decoding 造成 score compression（60% instances 的 within-instance range < 0.05），且在 non-tied subset 中 logprob **显著优于** greedy（+2.9 pp, p=0.01）。这说明 logprob 的 "failure" 是 constrained decoding 的 artifact，而非 confidence signal 的 intrinsic limitation。

  因此，"correlation-selection gap" 作为概念贡献被两头夹击：instance-level signals 的 failure 是 tautological；logprob 的 failure 是 constrained-decoding artifact。论文需要更诚实地 reframe：要么承认 "gap" 的主要来源是 signal 粒度的 category mismatch（而非经验发现），要么将 contribution 重心从 "gap identification" 转移到更有实质性的发现（如 logprob compression analysis 或 difficulty-dependent signal ranking）。

- 为什么影响接收：核心 contribution 的新颖性是 Findings 接收的底线要求。如果三个 contribution 中最突出的一个（C2，也是标题和 abstract 的主线）在很大程度上是 tautological，论文的整体价值大打折扣。
- 建议修改方向：(1) 在 Introduction 中明确区分"by-construction impossibility"（4 个 instance-level signals）和"empirical finding"（logprob failure + constrained decoding compression），不要将前者算作 contribution；(2) 将 C2 的重心转向 logprob score compression 的分析——这才是真正的 empirical contribution；(3) 考虑标题和 abstract 的 reframing，减少对 "gap" 的依赖。

---

**N2** [critical] 与 Nédellec et al. (2026) 的增量贡献论证不充分

- 具体位置：Section 1 (L16), Section 2 (L13–15), Table 5 (Appendix B, bootstrap CI)
- 问题：论文明确定位自己相对于 Nédellec et al. (2026) 的三个增量：(i) structural matching 优于 surface-level agreement；(ii) quality estimation 是否 translates to selection；(iii) difficulty gradient 泛化。但实际证据对这三个增量的支撑均偏弱：

  (i) **Structural matching 优势 marginal**：SJ vs EM 的 Δρ=+0.065 在 Bonferroni 校正后"would not survive"（Table 5 自述，Appendix B, footnote †）。在 conditional set 上，EM 反而在所有 4 个配置中排名第一（Appendix D, L133）。这意味着"structural matching improves on surface-level approach"这一 claim 只在特定条件下成立，且统计显著性 marginal。

  (ii) **Selection analysis** 的核心发现如 N1 所述，主要是 tautological。

  (iii) **Difficulty gradient** 的发现（harder tasks → structural signals better, easier tasks → EM better）在直觉上并不意外：当大多数 sample 近乎相同（CoNLL, 57–88% identical），binary agreement 自然最有效；当 output 结构复杂时，结构信号自然更好。这更像是 sanity check 而非 surprising finding。

- 为什么影响接收：如果与最直接的 prior work 的增量贡献不够 substantial，论文的 novelty 难以满足 venue 要求。
- 建议修改方向：更诚实地量化相对于 Nédellec et al. 的增量大小，特别是 SJ 的 marginal significance；或者找到 structural matching 在某些条件下有 clearly significant 优势的 setting（例如 conditional set 之外的条件组合）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 信息密度过高，首次阅读难以把握核心信息

- 具体位置：Abstract (L1–9)
- 问题：9 行 abstract 包含 5 个 signal 名称、3 个 family 名称、4 个数值指标（ρ=0.38, AUROC=0.75, p>0.39, 13–18 pp）、3 个数据集、2 个模型、"correlation-selection gap"概念、"instance-level by construction"的技术论证、conditional analysis、以及 reframing 结论。对于首次接触的读者，几乎不可能在一次阅读中提取核心 message。
- 建议：Abstract 应聚焦 1–2 个核心发现 + 高层 setup，将细节数字移入 Introduction。建议结构：problem → approach（一句话）→ key finding 1（quality estimation works）→ key finding 2（selection fails, with one concrete number）→ implication。

**W2** [warning] RE "preliminary" 标注与实际使用不一致

- 具体位置：Abstract L3 ("preliminary"), Introduction C1-C2, Table 1, Table 2, Figure 2-3, Discussion, Conclusion
- 问题：Abstract 将 RE 标注为"preliminary"，Conclusion L8 也说"RE conclusions rest on SciERC alone and warrant further validation"。但 RE 结果在论文中无处不在——Table 1 有 2 列 RE 数据，Table 2 有 RE F1，Figure 2-3 均展示 RE，Discussion 多处引用 RE 数据作为论证依据。如果 RE 真的是 preliminary，它不应该在主文中占据如此大的 weight；如果它足以作为主要证据，就不应该标注为 preliminary。
- 建议：要么 (a) 将 RE 结果整体移至 Appendix 并在正文中仅简要提及，要么 (b) 去掉 "preliminary" 标签并在 Limitations 中更详细地讨论 single-benchmark 的局限性。

**W3** [warning] Soft Jaccard 的方法论新颖性有限

- 具体位置：Section 3.2, Equation 5–6
- 问题：Soft Jaccard 本质上是 type-aware bipartite matching (Hungarian algorithm) + token-level IoU，这两者都是标准技术。将 Jaccard 扩展到 soft matching 在 information retrieval、image segmentation 等领域有广泛先例。论文将此作为 C1 的一部分（"our core structural signal"），但没有讨论与现有 soft set similarity measures 的关系，也没有说明为什么这个特定的 combination 对 IE 场景是非显然的。
- 建议：在 Method 或 Related Work 中讨论 soft set similarity 的已有工作（如 soft IoU in object detection），明确论文的技术贡献在于 **应用** 而非 **方法创新**。

**W4** [warning] "first multi-family comparison" claim 的 scope 需要更精确的限定

- 具体位置：Conclusion L1 ("the first multi-family comparison of confidence signals for test-time scaling in generative information extraction")
- 问题：Hobelsberger et al. (2025)、Geng et al. (2024)、Xia et al. (2025) 等 survey 论文已经比较了多个 family 的 confidence/uncertainty signal。论文的 "first" claim 依赖于限定语的叠加（"for test-time scaling" + "in generative IE"）。这种高度限定的 "first" claim 在形式上可能成立，但对读者的信息价值有限——尤其当 scope 如此窄时，"first" 更多反映了 niche 的窄度而非 contribution 的深度。
- 建议：要么去掉 "first"，要么明确说明此前的 multi-family comparison 存在于 QA/reasoning 领域（已引用），而在 generative IE 中确实缺失——将 gap 说清楚比宣称 "first" 更有说服力。

---

## 小问题（不影响接收）

- **术语不一致**：Table 1 和正文使用 "Voting Conf."，Table 4 (cross-selection) 使用 "VC"。Table 5 (TOST) 使用全称。建议统一为一种缩写并在首次出现时定义。

- **Ethics Statement 位置**：当前 Ethics Statement 在 `\bibliography` 之前（main.tex L39–41），这符合 ACL 格式。但内容仅两句话（公开数据集 + 无新数据收集），对于涉及 LLM 的工作可以考虑补充关于模型偏见或 extraction error 的潜在影响的简要讨论。

- **引用验证问题**：`hobelsberger2025systematic` 在 OpenAlex 中未找到（可能尚未索引）；`lightman2024verify`（"Let's Verify Step by Step"）同样未找到但已知是 ICLR 2024 论文。`feng2025optimal` 和 `ye2025uncertainty` 的 first author 字段与 API 记录不匹配，建议核查 bib 条目。

- **Figure 1 caption**：caption 中引用了 Table 2（"Table~\ref{tab:selection}"），这要求读者跳转参考，降低了 caption 的 self-containment。

- **Footnote 位置**（Table 1）：`\footnotetext` 紧跟 `\caption`，在某些 ACL 模板编译下可能显示异常，建议检查编译结果。

---

## Missing References

1. **"Trust but Verify! A Survey on Verification Design for Test-time Scaling"** (2025, arXiv:2508.16665) — 直接 survey 了 test-time scaling 中 verifier 的设计，与 Discussion 中"trained verifiers could close the selection gap"的建议直接相关。

2. **Uncertainty quantification surveys 缺乏 2025–2026 最新 survey**：论文引用了 Geng 2024、Wen 2025、Xia 2025 的 survey，但缺少 2025 下半年 / 2026 年的新 survey（如 "Uncertainty Quantification and Confidence Calibration in LLMs: A Survey" (arXiv:2503.15850)），考虑到领域快速发展，建议补充。

3. **Generative IE 领域**：缺少对 SLOT (EMNLP 2025 Industry) 等 structured output generation 工作的引用——虽然不是 confidence estimation，但属于 generative IE 的 constrained decoding 相关工作。

4. **MBR beyond MT**：Discussion 中声称 MBR "despite success in machine translation, fails here"，但缺乏对 MBR 在非 MT 任务（如 summarization、dialogue generation）中的引用，这些工作可以帮助 contextualize MBR 的 task-dependent 表现。

---

## 主要优势

- **统计分析的严谨性**：bootstrap CI、TOST equivalence testing、multi-seed stability、conditional filtering、diversity stratification——分析深度远超同类 empirical papers。这是论文最大的优势。

- **Negative result 的充分刻画**：logprob score compression analysis（Appendix F）和 diversity-stratified selection gap（Appendix E）排除了多个 alternative explanation，使得负面结论更可信。

- **实验设计的公平性**：两个模型使用相同训练配置（Table 7），三个数据集覆盖难度梯度，控制了多个混淆变量。

- **Limitations section 诚实且全面**：覆盖了 single RE benchmark、model scale、supervised verifier 缺失、constrained decoding 影响等多个实际局限。

- **Writing quality**：除 abstract 过密和术语不一致外，整体组织清晰，论证逻辑（特别是 quality estimation → selection gap → boundary conditions）层次分明。

---

现在将审稿报告发送给 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fde7441d-dcbf-4513-a2df-b3832279cf62",
  "isSidechain": false,
  "requestId": "req_011Cb3zgQnxBfYNRAKdkHCqn",
  "type": "assistant",
  "uuid": "0f000785-f66a-4527-91d4-4cbe993ebd26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XvMNQmFb3XCmqjGA8eKv7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2122,
      "cache_read_input_tokens": 77679,
      "output_tokens": 7105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2122,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7105,
          "cache_read_input_tokens": 77679,
          "cache_creation_input_tokens": 2122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2122
          },
          "type": "message"
        }
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

_source line 82 · 2026-05-15T07:57:36.805Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01GuZfPSWVNdNci8dNkxpHjo`</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 完整审稿报告\n\n### 审稿侧重：新颖性 + framing + related work 完整性 + 写作质量\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5（Findings publication）\n**一句话总结**: 实验设计严谨、统计分析到位的 empirical study，但核心概念贡献\"correlation-selection gap\"的新颖性因 4/5 信号在定义上就无法做 sample selection 而被大幅削弱——这是一个 tautological observation 被包装成 empirical finding 的 framing 问题。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验严谨（bootstrap CI、TOST、multi-seed），但核心 claim 中的 tautological 成分削弱了论证的 substantiveness |\n| Excitement | 2.5/5 | 负面结果对实践有价值，但新颖性有限——核心发现部分来自定义而非实验 |\n| Reproducibility | 4/5 | 训练细节、prompt template、超参数、统计测试均有详细描述 |\n| Confidence | 4/5 | 熟悉 self-consistency、uncertainty estimation、generative IE 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Correlation-selection gap 的核心论证存在 tautological 成分，新颖性不足\n\n- 具体位置：Section 1 (L22–24), Section 5.3, Section 6 (Discussion \"Why the gap exists: two layers\")\n- 问题：论文将\"correlation-selection gap\"作为三个 contribution 之一（C2），但 4/5 信号（EM、FK、SJ、Voting）是 instance-level by definition——它们对同一 input 的所有 N 个 sample 产生同一个分数。论文自己承认：\"they cannot rank candidates by construction\"（Section 5.3, L121; Discussion Layer 1）。这意味着这 4 个信号的\"selection failure\"不是实验发现，而是定义的逻辑后果。将一个 definitional impossibility 包装为\"gap\"并命名为 contribution，exaggerates the novelty。\n\n  真正 non-trivial 的发现只有 logprob 的失败——但 Appendix F 已解释：constrained decoding 造成 score compression（60% instances 的 within-instance range < 0.05），且在 non-tied subset 中 logprob 显著优于 greedy（+2.9 pp, p=0.01）。这说明 logprob 的\"failure\"是 constrained decoding 的 artifact，而非 confidence signal 的 intrinsic limitation。\n\n  因此，\"correlation-selection gap\"被两头夹击：instance-level signals 的 failure 是 tautological；logprob 的 failure 是 constrained-decoding artifact。\n\n- 为什么影响接收：核心 contribution 的新颖性是 Findings 接收的底线要求。\n- 建议修改方向：(1) 明确区分\"by-construction impossibility\"和\"empirical finding\"，不要将前者算作 contribution；(2) 将 C2 重心转向 logprob score compression 分析；(3) 考虑标题和 abstract 的 reframing。\n\n**N2** [critical] 与 Nédellec et al. (2026) 的增量贡献论证不充分\n\n- 具体位置：Section 1 (L16), Section 2 (L13–15), Table 5 (Appendix B)\n- 问题：三个增量均偏弱：(i) SJ vs EM 的 Δρ=+0.065 在 Bonferroni 校正后不显著（Table 5 自述），且 conditional set 上 EM 反而第一；(ii) selection analysis 如 N1 所述主要是 tautological；(iii) difficulty gradient 发现（harder→structural better, easier→EM better）在直觉上不意外。\n- 建议修改方向：更诚实地量化增量大小，或找到 structural matching 有 clearly significant 优势的 setting。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Abstract 信息密度过高\n- 9 行包含 5 个 signal、3 个 family、4 个数值指标、3 个数据集、2 个模型、gap 概念、technical arguments。首次阅读难以把握核心 message。\n- 建议聚焦 1–2 个核心发现，将细节数字移入 Introduction。\n\n**W2** [warning] RE \"preliminary\" 标注与实际使用不一致\n- Abstract 标注 \"preliminary\"，但 RE 结果在 Table 1（2 列）、Table 2、Figure 2–3、Discussion 中被大量使用作为主要论证。\n- 建议：要么移 RE 至 Appendix，要么去掉\"preliminary\"标签。\n\n**W3** [warning] Soft Jaccard 方法论新颖性有限\n- 本质是 Hungarian matching + token-level IoU，均为标准技术。缺少与 soft set similarity 已有工作（如 object detection 中的 soft IoU）的对比讨论。\n\n**W4** [warning] \"first multi-family comparison\" claim 过度依赖 scope 限定\n- \"first\" 依赖\"for test-time scaling\" + \"in generative IE\"的双重限定。建议去掉\"first\"或将 gap 描述清楚而非宣称优先权。\n\n---\n\n## 小问题（不影响接收）\n\n- 术语不一致：Table 1 用 \"Voting Conf.\"，Table 4 用 \"VC\"，建议统一。\n- Ethics Statement 仅两句话，可补充 LLM extraction error 的潜在影响。\n- 引用验证：`hobelsberger2025systematic` 和 `lightman2024verify` 在 OpenAlex 未找到（可能索引延迟）；`feng2025optimal` 和 `ye2025uncertainty` 的 first author 与 API 记录不匹配，建议核查 bib。\n- Figure 1 caption 引用了 Table 2，降低 self-containment。\n- Table 1 的 `\\footnotetext` 紧跟 `\\caption`，某些模板编译下可能显示异常。\n\n---\n\n## Missing References\n\n1. \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\" (2025, arXiv:2508.16665) — 与 Discussion 中 verifier 建议直接相关\n2. 2025–2026 最新 uncertainty quantification survey（如 arXiv:2503.15850）\n3. SLOT (EMNLP 2025 Industry) — structured output generation + constrained decoding 相关\n4. MBR 在非 MT 任务中的应用（summarization、dialogue）——帮助 contextualize MBR 的 task-dependent 表现\n\n---\n\n## 主要优势\n\n- 统计分析的严谨性：bootstrap CI、TOST、multi-seed、conditional filtering、diversity stratification 远超同类 empirical papers\n- Negative result 的充分刻画：logprob compression analysis 和 diversity-stratified gap 排除了多个 alternative explanations\n- 实验设计公平：两模型相同训练配置，三数据集覆盖难度梯度\n- Limitations section 诚实全面\n- 整体写作质量良好（除 abstract 过密和术语不一致外）",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f000785-f66a-4527-91d4-4cbe993ebd26",
  "isSidechain": false,
  "requestId": "req_011Cb3zgQnxBfYNRAKdkHCqn",
  "type": "assistant",
  "uuid": "5abf8f73-bc09-415a-9cf8-c462f24b0c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XvMNQmFb3XCmqjGA8eKv7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2122,
      "cache_read_input_tokens": 77679,
      "output_tokens": 7105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2122,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7105,
          "cache_read_input_tokens": 77679,
          "cache_creation_input_tokens": 2122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2122
          },
          "type": "message"
        }
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

_source line 83 · 2026-05-15T07:57:40.789Z_

<details><summary>↩ Tool result · `toolu_01GuZfPSWVNdNci8dNkxpHjo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5abf8f73-bc09-415a-9cf8-c462f24b0c06",
  "isSidechain": false,
  "promptId": "42b9f7c1-4125-4428-9bf3-9fff2daca6c1",
  "type": "user",
  "uuid": "404fe2df-4bb3-47e9-81e0-828341540155",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "5abf8f73-bc09-415a-9cf8-c462f24b0c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
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
  "type": "ai-title",
  "aiTitle": "Review paper on structured self-consistency for IE",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74"
}
```

---

### Runtime record

_source line 85 · 2026-05-15T07:58:20.961Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T07:58:20.961Z",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "content": "[Round 1 审稿请求]:\n## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**R1-N1** [critical] Constrained decoding 作为核心混淆变量未被隔离\n- 所有实验均使用 constrained decoding (vLLM + XGrammar)。论文承认 \"may compress per-sample diversity\"（Limitations §16），Appendix F 显示 60% instance logprob range < 0.05。论文无法区分 correlation-selection gap 是 structured IE 固有属性还是 constrained decoding 的人工产物。\n- 建议：添加 free-form decoding 消融，或在 title/abstract/conclusion 限定 scope。\n\n**R1-N2** [critical] Appendix F 的 non-tied subset 结果（logprob +2.9pp, p=0.01）实际削弱核心 claim\n- 在 non-tied 40% 中 logprob selection 显著优于 greedy，within-instance ρ 从 0.08 升到 0.39。更直接的解读是 logprob 在有 score resolution 时确实有效，gap 根因是 constrained decoding 的 score compression。\n- 建议：提升 non-tied analysis 至主文，重新组织 Discussion。\n\n### Reviewer 1 的 Should-Fix 问题\n\n**R1-W1** RE 结论仅基于 SciERC，abstract/contribution/conclusion 限定不一致\n**R1-W2** FK independence 假设 justification 不够严格，excess agreement 数据不全\n**R1-W3** \"Cross-architecture\" 用词过度（均为 8B decoder-only transformer）\n**R1-W4** TOST δ 选择缺乏外部锚点\n**R1-W5** Qwen3-8B thinking token 训练不一致（SciERC vs CoNLL/WNUT）\n\n### Reviewer 1 的 Minor 问题\n\n**R1-M1** Table 1 脚注格式可能渲染异常\n**R1-M2** SJ 全称首次出现时应统一\n**R1-M3** §4.2 脚注 semantic entropy 比较——如果 \"not meaningful\" 为何引用？\n**R1-M4** `he2024uncertainty` bib entry 与引用上下文不匹配\n**R1-M5** 部分引用在 OpenAlex 未找到\n\n### Reviewer 1 的 Questions\n\n1. Free-form decoding 下 logprob 是否可能成为有效 selector？\n2. Consensus-proximity = LOO-SJ 的证明？\n3. FK excess agreement 在哪个配置测量？\n4. WNUT-17 logprob 负相关的解释？\n\n### Reviewer 1 评分\nOverall 3/5, Soundness 3, Excitement 3.5, Reproducibility 4, Confidence 4\n\n---\n\n请对以上每个 N/W/M 和 Question 逐条给出 [AGREE] 或 [REBUT]。"
}
```

---

### Runtime record

_source line 86 · 2026-05-15T07:58:20.961Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T07:58:20.961Z",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74"
}
```

---

## Round 2

2 recorded events

### User

_source line 87 · 2026-05-15T07:58:20.950Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "404fe2df-4bb3-47e9-81e0-828341540155",
  "isSidechain": false,
  "promptId": "de2e5fbf-614b-41aa-9086-c34f54fe85db",
  "type": "user",
  "isMeta": true,
  "uuid": "618ddc95-f032-4c0d-b8ab-41c380dcf3fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 88 · 2026-05-15T07:58:20.951Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "618ddc95-f032-4c0d-b8ab-41c380dcf3fc",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "dd3f9471-5daa-4e2d-ba99-9622463f5ce7",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "24604346-5dd4-4c86-a78a-c7a9f61517e7",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---

## Round 3

8 recorded events

### User

_source line 89 · 2026-05-15T07:58:21.046Z_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

### Reviewer 1 的 Must-Fix 问题

**R1-N1** [critical] Constrained decoding 作为核心混淆变量未被隔离
- 所有实验均使用 constrained decoding (vLLM + XGrammar)。论文承认 "may compress per-sample diversity"（Limitations §16），Appendix F 显示 60% instance logprob range < 0.05。论文无法区分 correlation-selection gap 是 structured IE 固有属性还是 constrained decoding 的人工产物。
- 建议：添加 free-form decoding 消融，或在 title/abstract/conclusion 限定 scope。

**R1-N2** [critical] Appendix F 的 non-tied subset 结果（logprob +2.9pp, p=0.01）实际削弱核心 claim
- 在 non-tied 40% 中 logprob selection 显著优于 greedy，within-instance ρ 从 0.08 升到 0.39。更直接的解读是 logprob 在有 score resolution 时确实有效，gap 根因是 constrained decoding 的 score compression。
- 建议：提升 non-tied analysis 至主文，重新组织 Discussion。

### Reviewer 1 的 Should-Fix 问题

**R1-W1** RE 结论仅基于 SciERC，abstract/contribution/conclusion 限定不一致
**R1-W2** FK independence 假设 justification 不够严格，excess agreement 数据不全
**R1-W3** "Cross-architecture" 用词过度（均为 8B decoder-only transformer）
**R1-W4** TOST δ 选择缺乏外部锚点
**R1-W5** Qwen3-8B thinking token 训练不一致（SciERC vs CoNLL/WNUT）

### Reviewer 1 的 Minor 问题

**R1-M1** Table 1 脚注格式可能渲染异常
**R1-M2** SJ 全称首次出现时应统一
**R1-M3** §4.2 脚注 semantic entropy 比较——如果 "not meaningful" 为何引用？
**R1-M4** `he2024uncertainty` bib entry 与引用上下文不匹配
**R1-M5** 部分引用在 OpenAlex 未找到

### Reviewer 1 的 Questions

1. Free-form decoding 下 logprob 是否可能成为有效 selector？
2. Consensus-proximity = LOO-SJ 的证明？
3. FK excess agreement 在哪个配置测量？
4. WNUT-17 logprob 负相关的解释？

### Reviewer 1 评分
Overall 3/5, Soundness 3, Excitement 3.5, Reproducibility 4, Confidence 4

---

请对以上每个 N/W/M 和 Question 逐条给出 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd3f9471-5daa-4e2d-ba99-9622463f5ce7",
  "isSidechain": false,
  "promptId": "de2e5fbf-614b-41aa-9086-c34f54fe85db",
  "type": "user",
  "uuid": "6be6088b-7e8e-4207-9bec-bf3b57c8942b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 90 · 2026-05-15T07:58:21.046Z_

```json
{
  "parentUuid": "6be6088b-7e8e-4207-9bec-bf3b57c8942b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6eb2ad6f-89ae-4619-ae0d-ea40a43e5f80",
  "timestamp": "2026-05-15T07:58:21.046Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 91 · 2026-05-15T07:59:03.778Z_

<details><summary>Logged reasoning block</summary>

```text
The Director is asking me (Reviewer 2) to respond to Reviewer 1's review point by point, using [AGREE] or [REBUT] format. Let me go through each point carefully, drawing on my own reading of the paper.

Let me think through each point:

**R1-N1**: Constrained decoding as confounding variable
- R1 argues that constrained decoding may be the root cause of the correlation-selection gap, and the paper can't distinguish between "inherent to structured IE" vs "artifact of constrained decoding."
- My own review (N1) already identified this same issue — I noted that logprob's failure is a "constrained-decoding artifact." I should AGREE with this.


- The paper does acknowledge this in Limitations but doesn't run a free-form decoding ablation. That said, free-form decoding for structured IE introduces format errors, so it's not a clean ablation either—the paper uses constrained decoding specifically because it's the practical setting for generative IE.

**R1-N2**: Non-tied subset results undermine core claim
- R1 points out that in the non-tied 40%, logprob works (p=0.01, +2.9pp, within-instance ρ=0.39).
- This aligns perfectly with my N1 analysis, so I AGREE this undermines the "gap" claim.
- The paper buries this finding in the appendix rather than treating it as a central result.

**R1-W1**: RE conclusions limited to SciERC
- I raised the same issue about RE "preliminary" inconsistency, so I AGREE with this concern.

**R1-W2**: FK independence assumption justification
- The paper justifies the independence assumption in Section 3.2 by noting that temperature-based sampling provides sufficient response diversity, with empirical excess agreement ranging from −0.4% to −4.0%. R1 argues this justification lacks rigor and the excess agreement data is incomplete—no specification of which configuration these numbers come from or per-dataset breakdowns. This is a fair point that weakens the independence assumption.

**R1-W3**: "Cross-architecture" wording
- R1 correctly notes that both models are 8B decoder-only transformers, so calling this a "cross-architecture" comparison overstates the difference. While Qwen3 and LLaMA-3.1 differ in attention patterns, tokenizers, and training data, they're fundamentally the same architecture class. "Cross-model" or "cross-model-family" would be more precise terminology, and I AGREE this is a fair critique.

**R1-W4**: TOST δ choice lacks external anchor
- The paper's choice of δ for the equivalence test appears to lack grounding in external validation or prior work.

**R1-W5**: Qwen3-8B thinking token training inconsistency
- There's a potential confound in how thinking tokens were handled across datasets — SciERC didn't explicitly disable them while CoNLL and WNUT did, which could bias the SciERC results if thinking tokens were actually enabled during training.
- The paper notes that constrained decoding at inference overrides this behavior, but I'll partially agree the training inconsistency itself is still a valid concern worth addressing.

**R1-M1**: Table 1 footnote formatting — I raised this too, so I agree.

**R1-M2**: SJ full name consistency — I flagged the broader VC/Voting Conf. inconsistency as well, so I agree on this.

**R1-M3**: Semantic entropy footnote — the paper claims direct comparison isn't meaningful yet still cites the AUROC values to contextualize the results, which creates an awkward tension in the framing.

**R1-M4**: The `he2024uncertainty` citation appears to be mismatched — the bibliography entry describes a paper on sequential labeling uncertainty, but the text treats it as a survey of LLM uncertainty quantification, which doesn't align with what the paper actually covers.

**R1-M5**: I agree with the flagged citations that aren't found in OpenAlex.

**Questions:**

Q1: The question about free-form decoding logprob effectiveness is valid — it's genuinely difficult to test cleanly due to format errors.

Q2: The paper claims consensus-proximity equals LOO-SJ in Section 3.3 but doesn't provide the proof, only mentioning an empirical correlation in Appendix D. This equivalence needs mathematical justification.

Q3: The FK excess agreement configuration isn't specified in the paper, which is a fair point even though I didn't catch it in my own review.

Q4: Looking at the WNUT-17 logprob negative correlation mentioned in Section 4.2...

The paper's explanation is that higher model confidence correlates with lower extraction quality on this noisy domain, likely because the model becomes overconfident on familiar patterns that don't generalize to WNUT's novel entity types. This suggests the model is overfitting to patterns it's seen before rather than adapting to the domain shift.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6eb2ad6f-89ae-4619-ae0d-ea40a43e5f80",
  "isSidechain": false,
  "requestId": "req_011Cb3zvY1vCNKJcu8hHoaW8",
  "type": "assistant",
  "uuid": "e53ce1ee-36cf-4a66-8ec4-67bd229b6d39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X38UcyQqz3o5yMpYd8pvss",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 86976,
      "output_tokens": 5770,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5770,
          "cache_read_input_tokens": 86976,
          "cache_creation_input_tokens": 1060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1060
          },
          "type": "message"
        }
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

_source line 92 · 2026-05-15T08:00:09.155Z_

逐条回应 Reviewer 1 的审稿意见：

---

## Must-Fix

**[AGREE] R1-N1: Constrained decoding 作为核心混淆变量**

同意且认为这与我自己的 N1 高度一致。我的 N1 指出 logprob failure 本质上是 constrained decoding artifact（Appendix F: 60% instances within-instance range < 0.05，non-tied subset 中 logprob 显著有效 p=0.01）。R1 更进一步要求 free-form decoding 消融来隔离因果——这比我的建议（reframe contribution）更彻底。

补充一个 nuance：free-form decoding 消融并非 clean experiment，因为 free-form 输出会引入格式错误（缺少 JSON 结构、entity boundary 模糊等），需要额外的 post-processing，这本身又是一个混淆变量。但即便如此，论文至少应该在主文中承认 constrained decoding 是 gap 的可能 root cause 而非仅在 Limitations L16 一笔带过，并在 title/abstract 中限定 scope（如"under constrained decoding"）。当前的 framing 将 gap 呈现为 structured IE 的固有属性，证据不支持这一强 claim。

---

**[AGREE] R1-N2: Non-tied subset 结果削弱核心 claim**

完全同意。这是我 N1 的核心论据之一：Appendix F 的 non-tied analysis 显示 logprob 在有 score resolution 时有效（+2.9pp, p=0.01, within-instance ρ=0.08→0.39），这直接说明 gap 的根因是 score compression 而非 signal 本身的 intrinsic limitation。论文将这一关键发现埋在 Appendix 而非提升为主文核心发现，是一个 significant framing error。

如果重新组织，论文的 narrative 应该是："logprob carries useful per-sample quality information but is resolution-limited under constrained decoding"——这比"correlation-selection gap"更 accurate，也更有 actionable value（指向 constrained decoding 的改进方向而非笼统的 verifier 建议）。

---

## Should-Fix

**[AGREE] R1-W1: RE 结论限定不一致**

同意，与我的 W2 观点一致。Abstract 标注"preliminary"但 RE 数据在 Table 1（2 列）、Table 2、Figure 2–3、Discussion 中被大量使用。建议要么统一标注为 preliminary 并减少正文 weight，要么去掉 preliminary 标签并在 Limitations 中详细讨论 single-benchmark 局限。

---

**[AGREE with nuance] R1-W2: FK independence 假设 justification 不够严格**

部分同意。R1 的关注点——excess agreement 数据不全——是合理的：论文给出了 −0.4% to −4.0% 的范围（Section 3.2, L39），但未说明哪个 configuration、哪个 dataset 产生了这些数字。不过我认为 severity 偏低：(a) FK 不是论文的核心 contribution（Soft Jaccard 和 Entity Voting 才是重点 structural signals）；(b) 负值 excess agreement 实际上是对"FK 不会被 inter-sample dependence 人为抬高"这一核心担忧的有效回应——问题不在于 justification 方向错误，而在于不够完整。建议补充 per-dataset 的 excess agreement 数据即可，不需要重做分析。

---

**[AGREE] R1-W3: "Cross-architecture" 用词过度**

同意。Qwen3-8B 和 LLaMA-3.1-8B 虽然在 tokenizer、attention 实现、训练数据上有差异，但同属 8B decoder-only transformer。"Cross-architecture" 暗示了更大的结构差异（如 encoder-decoder vs decoder-only，或不同 scale）。"Cross-model-family" 更准确。论文 Appendix A 标题"Cross-architecture transfer"应改为"Cross-model transfer"。

---

**[AGREE with nuance] R1-W4: TOST δ 选择缺乏外部锚点**

同意核心关切。Appendix E (Table 6) 提供了 δ=±2pp/±3pp/±5pp 三个水平，论文仅说"±2pp represents a stringent equivalence threshold (smaller than typical inter-annotator disagreement on IE benchmarks)"但未引用具体 IAA 数据。不过我认为 severity 低于 R1 的评估：多水平 δ 本身构成了 sensitivity analysis，读者可以自行判断在哪个阈值下接受 equivalence。建议引用 IE benchmark 的 IAA 数据（如 SciERC 的 inter-annotator F1）作为锚点即可。

---

**[AGREE] R1-W5: Qwen3-8B thinking token 训练不一致**

同意这是一个有效关切。Appendix G 脚注承认 SciERC 训练未显式禁用 `enable_thinking`，而 CoNLL/WNUT 禁用了。虽然论文辩称"Constrained decoding at inference time overrides any thinking behavior by enforcing JSON-only output"，但这只解决了 inference-time 行为——**训练过程**中 thinking tokens 的 presence/absence 可能影响了 LoRA 权重的学习，尤其是 loss 计算中是否包含 thinking tokens 这一点未被讨论。SciERC 是论文最重要的 benchmark（selection gap 的主要证据来源），这一训练不一致需要更严肃的对待。建议至少在 Limitations 中讨论，或补充一个禁用 thinking 的 SciERC 重训结果。

---

## Minor

**[AGREE] R1-M1: Table 1 脚注格式**

同意，我也在 minor issues 中提到了这一点。

---

**[AGREE] R1-M2: SJ 全称首次出现应统一**

同意，与我提出的 VC/Voting Conf. 不一致问题属于同一类 terminology consistency 问题。

---

**[REBUT] R1-M3: Semantic entropy 比较脚注——"not meaningful" 为何引用**

不完全同意 R1 的批评。Section 4.2 脚注的意图是提供 AUROC scale 的参考坐标系（"We cite this only to situate our AUROC scale"），这在 empirical papers 中是常见做法——当读者不知道 0.749 的 AUROC 在绝对意义上是"好"还是"差"时，提供一个不同领域的近似锚点有合理价值。论文已明确标注了三个不可比因素（output spaces、evaluation protocols、task difficulty distributions）。

但我承认 R1 的担忧有一定道理：在快速阅读中，读者可能忽略 caveats 而错误地将 0.75 vs 0.75–0.85 解读为直接对比。建议将这个对比从脚注提升到正文 parenthetical 并缩短，或干脆删除——AUROC 0.749 本身已经足够有说服力，不需要外部锚点。

---

**[AGREE] R1-M4: `he2024uncertainty` bib entry 与引用上下文不匹配**

同意。Section 2 L23 将 `he2024uncertainty` 描述为"survey uncertainty quantification specifically for LLMs, covering both white-box and black-box approaches"，但实际论文是 "Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission"（NAACL 2024 Findings），这是一篇关于序列标注不确定性传播的方法论文，不是 survey。引用上下文与实际论文内容不匹配，应更正描述或替换为正确的 survey 论文。

---

**[AGREE] R1-M5: 部分引用在 OpenAlex 未找到**

同意，我也在 minor issues 中标注了 `hobelsberger2025systematic` 和 `lightman2024verify` 的验证问题。

---

## Questions 回应

**Q1: Free-form decoding 下 logprob 是否可能成为有效 selector？**

与 R1-N1 直接相关的核心问题。基于 Appendix F 的 non-tied subset evidence（ρ=0.39, p=0.01），我认为答案很可能是 yes——至少在 score resolution 不被压缩的条件下，logprob 已展示了有效的 per-sample discrimination。Free-form decoding 会移除 constrained decoding 的 score compression，但引入格式错误噪声。净效果不确定，但我同意 R1 这是论文应该回答的关键消融。

**Q2: Consensus-proximity = LOO-SJ 的证明？**

R1 要求的数学证明是合理的。Section 3.3 声称 equivalence 但未提供推导。Appendix D 仅报告了经验差异（Δρ=−0.014, max per-instance Δ=3.1×10⁻⁴），但经验近似不等于数学等价。如果这是 exact equivalence，应在 Appendix 中提供简短证明；如果是 approximate，应更正措辞为"approximately equivalent"。

**Q3: FK excess agreement 在哪个配置测量？**

有效问题。Section 3.2 给出 −0.4% to −4.0% 但未注明 configuration。此信息对评估 FK 可靠性至关重要——不同 dataset 的 diversity 差异很大（CoNLL 88% identical vs SciERC 11% identical），excess agreement 数值可能在这些极端之间差异显著。

**Q4: WNUT-17 logprob 负相关的解释？**

Section 4.2 L78 仅给出观察（"higher model confidence associates with lower extraction quality"）但缺乏机制解释。一个合理假说是 WNUT-17 的 novel/emerging entities 恰好出现在 model 不熟悉的 context 中，而 model 对这些 context 中的 high-confidence（但错误的）常见 entity 类型给出了高 logprob。另一种可能是 52% zero-F1 instances 恰好是 model 产生高 confidence 的 empty/trivial outputs 的情况。论文应在 Discussion 或 Appendix 中分析 logprob 与 zero-F1 instance 分布的关系来回答这个问题。

---

**总结**：R1 和我的审稿意见在核心问题上高度一致——constrained decoding 作为混淆变量（R1-N1/N2 ↔ 我的 N1）、RE scope 不一致（R1-W1 ↔ 我的 W2）、术语问题（R1-M1/M2 ↔ 我的 minor）。R1 在技术层面的分析（FK independence、thinking token、TOST δ）比我更深入，我在 framing/novelty 层面（tautological argument、incremental over Nédellec、abstract density）着力更多。两份审稿互补性强。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e53ce1ee-36cf-4a66-8ec4-67bd229b6d39",
  "isSidechain": false,
  "requestId": "req_011Cb3zvY1vCNKJcu8hHoaW8",
  "type": "assistant",
  "uuid": "3ae231f1-3cef-4b46-a614-6a7e5bd66711",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X38UcyQqz3o5yMpYd8pvss",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 86976,
      "output_tokens": 5770,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5770,
          "cache_read_input_tokens": 86976,
          "cache_creation_input_tokens": 1060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1060
          },
          "type": "message"
        }
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

_source line 93 · 2026-05-15T08:00:21.495Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01WEUaJRwDUT3RXvBQQMwK51`</summary>

```json
{
  "text": "## Reviewer 2 — 交叉回应 Reviewer 1\n\n### Must-Fix\n\n[AGREE] R1-N1: Constrained decoding 混淆变量 — 与我的 N1 高度一致。补充：free-form decoding 消融本身也非 clean experiment（格式错误），但论文至少应在 title/abstract 限定 scope（\"under constrained decoding\"），当前 framing 将 gap 呈现为 structured IE 固有属性，证据不支持。\n\n[AGREE] R1-N2: Non-tied subset 削弱核心 claim — 完全同意，这是我 N1 的核心论据之一。logprob 在有 score resolution 时有效（+2.9pp, p=0.01, ρ=0.39），说明 gap 根因是 score compression 而非 signal intrinsic limitation。论文应将此提升为主文核心发现。\n\n### Should-Fix\n\n[AGREE] R1-W1: RE scope 不一致 — 与我的 W2 一致\n[AGREE with nuance] R1-W2: FK independence — 关切有效但 severity 偏低（FK 非核心 contribution，负 excess agreement 回应了核心担忧）\n[AGREE] R1-W3: \"Cross-architecture\" 过度 — 应改为 \"cross-model-family\"\n[AGREE with nuance] R1-W4: TOST δ — 多水平 δ 已构成 sensitivity analysis，建议引用 IAA 数据即可\n[AGREE] R1-W5: Thinking token 训练不一致 — SciERC 是核心 benchmark，训练配置差异需严肃对待\n\n### Minor\n\n[AGREE] R1-M1, M2, M4, M5\n[REBUT] R1-M3: Semantic entropy 脚注意图合理（提供 AUROC scale 参考），但执行上可能误导快速读者，建议缩短或删除\n\n### Questions\n\nQ1: 基于 non-tied evidence，free-form 下 logprob 很可能有效，同意这是关键消融\nQ2: Consensus-proximity = LOO-SJ 需数学证明或更正为\"approximately equivalent\"\nQ3: FK excess agreement 应注明 configuration\nQ4: WNUT-17 logprob 负相关需机制解释（可能是 novel entities + overconfident familiar patterns）\n\n### 两份审稿的互补性\n\nR1 和 R2 在核心问题上高度一致（constrained decoding 混淆变量、RE scope、术语）。R1 技术层面更深（FK、thinking token、TOST δ），R2 在 framing/novelty 层面着力更多（tautological argument、incremental over Nédellec、abstract density）。两份审稿互补。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ae231f1-3cef-4b46-a614-6a7e5bd66711",
  "isSidechain": false,
  "requestId": "req_011Cb3zvY1vCNKJcu8hHoaW8",
  "type": "assistant",
  "uuid": "1eede721-d01a-47bc-b5e6-eb6541a02a5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X38UcyQqz3o5yMpYd8pvss",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 86976,
      "output_tokens": 5770,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5770,
          "cache_read_input_tokens": 86976,
          "cache_creation_input_tokens": 1060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1060
          },
          "type": "message"
        }
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

_source line 94_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见  以下是 Reviewer 1 的完整审稿意见。请逐条回应： - **[AGREE]** 同意并说明理由 - **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）  ---  ### Reviewer 1 的 Must-Fix 问题  **R1-N1**…",
  "leafUuid": "1eede721-d01a-47bc-b5e6-eb6541a02a5e",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74"
}
```

---

### Runtime record

_source line 95_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on structured self-consistency for IE",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74"
}
```

---

### Tool result

_source line 96 · 2026-05-15T08:00:25.803Z_

<details><summary>↩ Tool result · `toolu_01WEUaJRwDUT3RXvBQQMwK51`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1eede721-d01a-47bc-b5e6-eb6541a02a5e",
  "isSidechain": false,
  "promptId": "de2e5fbf-614b-41aa-9086-c34f54fe85db",
  "type": "user",
  "uuid": "9cc7a74f-b373-483d-8034-799b67034686",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "1eede721-d01a-47bc-b5e6-eb6541a02a5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "56b1f119-65e5-496e-8301-345209a9bd74",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
