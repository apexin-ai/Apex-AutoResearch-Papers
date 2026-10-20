# Research conversation: [Round 1 审稿请求]: ## 审稿任务 — Reviewer 1（方法与实验严谨性） ### Venue 信息 - **目标 venue**: EMNLP 2026 Main Conference Long Paper (via A

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 88
- **Recorded user turns:** 3
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-1/8cd9d2a1-e826-42f8-a029-f5ea0e7f221c.jsonl`
- **Structured JSON:** [`aca03514a18f56104c53.json`](../../sessions/ac/aca03514a18f56104c53.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T06:48:35.709Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T06:48:35.709Z",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "content": "[Round 1 审稿请求]:\n## 审稿任务 — Reviewer 1（方法与实验严谨性）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026 Main Conference Long Paper (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references/appendix\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind，禁止 self-identification\n- **附录规则**: 双栏格式，不计页数，reviewers 可选择是否阅读\n\n### 论文路径\n`projects/faith-evidence-ie/docs/paper/main.tex`（sections 在 `sections/` 子目录）\n\n### 你的审查侧重：方法与实验严谨性\n\n请重点审查以下方面：\n\n1. **方法设计**\n   - Task formulation (§3.1) 是否合理？Evidence-grounded DocRE 的形式化定义是否严谨？\n   - CED scoring function (§3.4) 设计是否合理？NLI-based 对比打分的假设是否成立？\n   - EDCR metric (§3.5) 的定义和解释是否存在漏洞？\n\n2. **实验设计与统计可靠性**\n   - \"85+ configurations\" 的声称是否可验证？\n   - 主要 claim 的统计支撑是否充分？（seed 数量、variance 报告、显著性检验）\n   - Baseline 选择是否公平？是否遗漏关键 baseline？\n   - Evaluation protocol 是否标准？只使用 dev set 是否构成重大局限？\n\n3. **Claims 与证据对齐**\n   - 三个核心 finding（decoupling spectrum、scale-dependent tax、RSFT effectiveness）是否都有充分的实验支撑？\n   - Claim 的强度是否与证据匹配？是否存在过度声称（overclaim）？\n   - 因果性 vs 相关性：论文的因果推断是否合理？\n\n4. **消融与分析完整性**\n   - RSFT ablation（CED vs flat-NLI, k=1 vs k=3）是否充分？\n   - GRPO/DPO 的配置空间是否充分探索？（例如不同 KL 系数、不同 LoRA rank）\n   - Scale analysis 只有 3-4 个数据点，non-monotonic pattern 的 claim 是否 over-interpreted？\n\n5. **可复现性**\n   - Hyperparameters 是否完整报告？\n   - 数据处理 pipeline 是否可复现？\n\n请按 ARR 审稿标准输出完整审稿意见（Strengths / Weaknesses / Questions / Missing References / Overall Assessment）。评分使用 EMNLP 2026 标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit。"
}
```

---

### Runtime record

_source line 2 · 2026-05-18T06:48:35.712Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T06:48:35.712Z",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c"
}
```

---

## Round 1

79 recorded events

### User

_source line 3 · 2026-05-18T06:48:35.750Z_

[Round 1 审稿请求]:
## 审稿任务 — Reviewer 1（方法与实验严谨性）

### Venue 信息
- **目标 venue**: EMNLP 2026 Main Conference Long Paper (via ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **页数限制**: 正文 8 页 + unlimited references/appendix
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind，禁止 self-identification
- **附录规则**: 双栏格式，不计页数，reviewers 可选择是否阅读

### 论文路径
`projects/faith-evidence-ie/docs/paper/main.tex`（sections 在 `sections/` 子目录）

### 你的审查侧重：方法与实验严谨性

请重点审查以下方面：

1. **方法设计**
   - Task formulation (§3.1) 是否合理？Evidence-grounded DocRE 的形式化定义是否严谨？
   - CED scoring function (§3.4) 设计是否合理？NLI-based 对比打分的假设是否成立？
   - EDCR metric (§3.5) 的定义和解释是否存在漏洞？

2. **实验设计与统计可靠性**
   - "85+ configurations" 的声称是否可验证？
   - 主要 claim 的统计支撑是否充分？（seed 数量、variance 报告、显著性检验）
   - Baseline 选择是否公平？是否遗漏关键 baseline？
   - Evaluation protocol 是否标准？只使用 dev set 是否构成重大局限？

3. **Claims 与证据对齐**
   - 三个核心 finding（decoupling spectrum、scale-dependent tax、RSFT effectiveness）是否都有充分的实验支撑？
   - Claim 的强度是否与证据匹配？是否存在过度声称（overclaim）？
   - 因果性 vs 相关性：论文的因果推断是否合理？

4. **消融与分析完整性**
   - RSFT ablation（CED vs flat-NLI, k=1 vs k=3）是否充分？
   - GRPO/DPO 的配置空间是否充分探索？（例如不同 KL 系数、不同 LoRA rank）
   - Scale analysis 只有 3-4 个数据点，non-monotonic pattern 的 claim 是否 over-interpreted？

5. **可复现性**
   - Hyperparameters 是否完整报告？
   - 数据处理 pipeline 是否可复现？

请按 ARR 审稿标准输出完整审稿意见（Strengths / Weaknesses / Questions / Missing References / Overall Assessment）。评分使用 EMNLP 2026 标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "0a44f185-fd13-4055-9f0d-42066ab2771a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T06:48:35.749Z_

```json
{
  "parentUuid": "0a44f185-fd13-4055-9f0d-42066ab2771a",
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
  "uuid": "83cfc553-bb77-4b2e-ac89-ec7887811ead",
  "timestamp": "2026-05-18T06:48:35.749Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T06:48:35.750Z_

```json
{
  "parentUuid": "83cfc553-bb77-4b2e-ac89-ec7887811ead",
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
  "uuid": "b2638257-046d-425e-83c4-0e8d6a22b3e5",
  "timestamp": "2026-05-18T06:48:35.750Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-18T06:48:35.750Z_

```json
{
  "parentUuid": "b2638257-046d-425e-83c4-0e8d6a22b3e5",
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
  "uuid": "a8d2292e-cc4f-4e68-8dd6-d0ea09c825c5",
  "timestamp": "2026-05-18T06:48:35.750Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-18T06:48:35.750Z_

```json
{
  "parentUuid": "a8d2292e-cc4f-4e68-8dd6-d0ea09c825c5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e0fa6722-cb6b-44c0-950b-dbb5e50d3288",
  "timestamp": "2026-05-18T06:48:35.750Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
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
  "aiTitle": "Review evidence-grounded information extraction paper",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c"
}
```

---

### Assistant

_source line 9 · 2026-05-18T06:48:40.714Z_

<details><summary>Logged reasoning block</summary>

```text
The user (Review Director) is asking me to perform a thorough review of a paper as Reviewer 1, focusing on method and experimental rigor. Let me start by:

1. First, loading the review-reviewer-session-start skill as instructed
2. Reading the paper materials
3. Searching for ARR/EMNLP 2026 reviewer guidelines
4. Conducting the review

Let me begin by reading the skill file and the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0fa6722-cb6b-44c0-950b-dbb5e50d3288",
  "isSidechain": false,
  "requestId": "req_011Cb9b2mHXzsoCkbWPxkm2r",
  "type": "assistant",
  "uuid": "95536f1c-beba-4cee-8338-29adce10a6f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NzX3VaEbzkkEzptyuLHed",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15788,
      "cache_read_input_tokens": 11447,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15788,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 15788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15788
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-18T06:48:41.156Z_

我将开始 Round 1 审稿。先加载 session start skill 并读取论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95536f1c-beba-4cee-8338-29adce10a6f9",
  "isSidechain": false,
  "requestId": "req_011Cb9b2mHXzsoCkbWPxkm2r",
  "type": "assistant",
  "uuid": "32435dc5-0612-4b57-8830-bce87a1fb713",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NzX3VaEbzkkEzptyuLHed",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15788,
      "cache_read_input_tokens": 11447,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15788,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 15788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15788
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-18T06:48:42.236Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JfXKwzaiyRQYc7R3Lwm2fb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32435dc5-0612-4b57-8830-bce87a1fb713",
  "isSidechain": false,
  "requestId": "req_011Cb9b2mHXzsoCkbWPxkm2r",
  "type": "assistant",
  "uuid": "3515c16b-010f-4318-a8d0-6090ecd79eed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NzX3VaEbzkkEzptyuLHed",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15788,
      "cache_read_input_tokens": 11447,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15788,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 15788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15788
          },
          "type": "message"
        }
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

_source line 12 · 2026-05-18T06:48:42.446Z_

<details><summary>↩ Tool result · `toolu_01DjeGZmh23QH1WqnKqRWfYo`</summary>

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
15	\usepackage{xcolor}
16	\usepackage{multirow}
17	\usepackage{subcaption}
18	
19	\graphicspath{{../../figures/paper/}}
20	
21	\title{Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction}
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
33	\input{sections/analysis}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f379902b-4ebc-457c-8479-96a0ddfa7740",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "578fa580-8d8d-4cbc-a534-e26f3fc64224",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{subcaption}\n\n\\graphicspath{{../../figures/paper/}}\n\n\\title{Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/analysis}\n\\input{sections/conclusion}\n\\input{sections/limitations}\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  },
  "sourceToolAssistantUUID": "f379902b-4ebc-457c-8479-96a0ddfa7740",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T06:48:42.250Z_

<details><summary>↩ Tool result · reported error · `toolu_01JfXKwzaiyRQYc7R3Lwm2fb`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3515c16b-010f-4318-a8d0-6090ecd79eed",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "2dad551e-9031-4723-aa49-719593c70871",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957.",
  "sourceToolAssistantUUID": "3515c16b-010f-4318-a8d0-6090ecd79eed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T06:48:42.439Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DjeGZmh23QH1WqnKqRWfYo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dad551e-9031-4723-aa49-719593c70871",
  "isSidechain": false,
  "requestId": "req_011Cb9b2mHXzsoCkbWPxkm2r",
  "type": "assistant",
  "uuid": "f379902b-4ebc-457c-8479-96a0ddfa7740",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NzX3VaEbzkkEzptyuLHed",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15788,
      "cache_read_input_tokens": 11447,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15788,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 15788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15788
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-18T06:48:45.167Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Dexr5i5cohKUt5WchtdG9C`</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "578fa580-8d8d-4cbc-a534-e26f3fc64224",
  "isSidechain": false,
  "requestId": "req_011Cb9b3G4eWDyWnS3rTHjdc",
  "type": "assistant",
  "uuid": "0b6ac394-5ea8-4967-a1fb-d2211b6ff307",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1L5jXgrgpkn41FXuaoiUv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 821,
      "cache_read_input_tokens": 27235,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 821,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 27235,
          "cache_creation_input_tokens": 821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 821
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-18T06:48:45.199Z_

<details><summary>↩ Tool result · `toolu_01Dexr5i5cohKUt5WchtdG9C`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b6ac394-5ea8-4967-a1fb-d2211b6ff307",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "b4f9bb01-7354-42f9-9e18-6f98fc2e5b33",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
    ],
    "durationMs": 26,
    "numFiles": 9,
    "truncated": false
  },
  "sourceToolAssistantUUID": "0b6ac394-5ea8-4967-a1fb-d2211b6ff307",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T06:48:45.794Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01EMFqB8qhsw5aACbH744amj`</summary>

```json
{
  "pattern": "**/docs/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4f9bb01-7354-42f9-9e18-6f98fc2e5b33",
  "isSidechain": false,
  "requestId": "req_011Cb9b3G4eWDyWnS3rTHjdc",
  "type": "assistant",
  "uuid": "c300fb44-d5cb-4bb3-8d83-c5ae9fa3a7a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1L5jXgrgpkn41FXuaoiUv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 821,
      "cache_read_input_tokens": 27235,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 821,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 27235,
          "cache_creation_input_tokens": 821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 821
          },
          "type": "message"
        }
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

_source line 18 · 2026-05-18T06:48:45.824Z_

<details><summary>↩ Tool result · `toolu_01EMFqB8qhsw5aACbH744amj`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c300fb44-d5cb-4bb3-8d83-c5ae9fa3a7a2",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "5c3e97cd-bb78-4192-bb7c-ac225d3fecac",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
    ],
    "durationMs": 27,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "c300fb44-d5cb-4bb3-8d83-c5ae9fa3a7a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-18T06:48:48.931Z_

现在并行读取所有论文 section 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c3e97cd-bb78-4192-bb7c-ac225d3fecac",
  "isSidechain": false,
  "requestId": "req_011Cb9b3WYJAvj1CA56wvEuf",
  "type": "assistant",
  "uuid": "df2b18f9-d012-420f-959c-78cdb0e4cb90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175uQP8vQqP2vH4FRDuCkXq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 28056,
      "output_tokens": 756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 756,
          "cache_read_input_tokens": 28056,
          "cache_creation_input_tokens": 629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 629
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-18T06:48:49.371Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HYT8Lfo5cL69Z41o3VXQTL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df2b18f9-d012-420f-959c-78cdb0e4cb90",
  "isSidechain": false,
  "requestId": "req_011Cb9b3WYJAvj1CA56wvEuf",
  "type": "assistant",
  "uuid": "19287f56-8792-49da-83f6-94291a00399d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175uQP8vQqP2vH4FRDuCkXq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 28056,
      "output_tokens": 756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 756,
          "cache_read_input_tokens": 28056,
          "cache_creation_input_tokens": 629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 629
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-18T06:48:49.385Z_

<details><summary>↩ Tool result · `toolu_01HYT8Lfo5cL69Z41o3VXQTL`</summary>

```text
1	\begin{abstract}
2	
3	Large Language Model (LLM) based Document-level Relation Extraction (DocRE) methods now match or exceed encoder baselines in extraction accuracy, yet they produce bare relation triplets without identifying the sentences that support each prediction.
4	In deployment contexts such as clinical knowledge bases and legal due-diligence systems, users cannot verify predictions without manually locating textual evidence across multi-page documents.
5	Encoder-based evidence methods (SAIS, DREEAM) can produce supporting sentences but trail LLM approaches in accuracy. The community therefore faces a gap between extractive precision and output verifiability.
6	
7	We formalize evidence-grounded DocRE as a structured generation task and conduct a systematic comparison of three post-training optimization paradigms: Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), and Rejection Sampling Fine-Tuning (RSFT).
8	Our study spans 85+ experimental configurations across four model scales (1.7B to 8B parameters), two model families, and two datasets.
9	We introduce the Evidence-Decoupling Ratio (EDCR) diagnostic and a Contrastive Evidence Discrimination (CED) scoring function for sample selection.
10	
11	Three findings emerge.
12	First, RL optimization pressure correlates with evidence-extraction decoupling severity: GRPO causes catastrophic decoupling, DPO shows gradual degradation, and RSFT preserves stable joint performance.
13	Second, the cost of evidence production is scale-dependent and non-monotonic: at 1.7B parameters evidence provides a +8pp Ign-F1 benefit, at 4B it imposes a $-$7.5pp penalty, and at 8B the cost approaches zero.
14	Third, RSFT with CED scoring is the only effective route: it achieves +4.92pp Ign-F1 over supervised fine-tuning at 4B scale (four-seed mean), and our 1.7B RSFT model (50.50 Ign-F1) matches 8B SFT performance (50.51).
15	
16	\end{abstract}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19287f56-8792-49da-83f6-94291a00399d",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "06a94c01-28ee-4cd5-a0d1-3acc99bf85df",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\n\nLarge Language Model (LLM) based Document-level Relation Extraction (DocRE) methods now match or exceed encoder baselines in extraction accuracy, yet they produce bare relation triplets without identifying the sentences that support each prediction.\nIn deployment contexts such as clinical knowledge bases and legal due-diligence systems, users cannot verify predictions without manually locating textual evidence across multi-page documents.\nEncoder-based evidence methods (SAIS, DREEAM) can produce supporting sentences but trail LLM approaches in accuracy. The community therefore faces a gap between extractive precision and output verifiability.\n\nWe formalize evidence-grounded DocRE as a structured generation task and conduct a systematic comparison of three post-training optimization paradigms: Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), and Rejection Sampling Fine-Tuning (RSFT).\nOur study spans 85+ experimental configurations across four model scales (1.7B to 8B parameters), two model families, and two datasets.\nWe introduce the Evidence-Decoupling Ratio (EDCR) diagnostic and a Contrastive Evidence Discrimination (CED) scoring function for sample selection.\n\nThree findings emerge.\nFirst, RL optimization pressure correlates with evidence-extraction decoupling severity: GRPO causes catastrophic decoupling, DPO shows gradual degradation, and RSFT preserves stable joint performance.\nSecond, the cost of evidence production is scale-dependent and non-monotonic: at 1.7B parameters evidence provides a +8pp Ign-F1 benefit, at 4B it imposes a $-$7.5pp penalty, and at 8B the cost approaches zero.\nThird, RSFT with CED scoring is the only effective route: it achieves +4.92pp Ign-F1 over supervised fine-tuning at 4B scale (four-seed mean), and our 1.7B RSFT model (50.50 Ign-F1) matches 8B SFT performance (50.51).\n\n\\end{abstract}\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  },
  "sourceToolAssistantUUID": "19287f56-8792-49da-83f6-94291a00399d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T06:48:53.823Z_

<details><summary>↩ Tool result · `toolu_01KiuJGxD69vt5EGoCiXtX6K`</summary>

```text
1	@inproceedings{autore2024,
2	  title     = {{AutoRE}: Document-Level Relation Extraction with Large Language Models},
3	  author    = {{Anonymous}},
4	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
5	  year      = {2024},
6	  url       = {https://arxiv.org/abs/2403.14888}
7	}
8	
9	@inproceedings{chen2025docksrag,
10	  title     = {{DocKS-RAG}: Optimizing Document-Level Relation Extraction through {LLM}-Enhanced Hybrid Prompt Tuning},
11	  author    = {Xu and others},
12	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
13	  year      = {2025},
14	  url       = {https://proceedings.mlr.press/v267/xu25am.html}
15	}
16	
17	@article{dai2025r1re,
18	  title   = {{R1-RE}: Cross-Domain Relation Extraction with {RLVR}},
19	  author  = {Dai, Runpeng and Zheng, Tong and others},
20	  journal = {arXiv preprint arXiv:2507.04642},
21	  year    = {2025},
22	  url     = {https://arxiv.org/abs/2507.04642}
23	}
24	
25	@inproceedings{gao2023scaling,
26	  title     = {Scaling Laws for Reward Model Overoptimization},
27	  author    = {Gao, Leo and Schulman, John and Hilton, Jacob},
28	  booktitle = {Proceedings of the 40th International Conference on Machine Learning},
29	  year      = {2023},
30	  url       = {https://arxiv.org/abs/2210.10760}
31	}
32	
33	@inproceedings{hu2022lora,
34	  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},
35	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
36	  booktitle = {International Conference on Learning Representations},
37	  year      = {2022},
38	  url       = {https://arxiv.org/abs/2106.09685}
39	}
40	
41	@article{jin2025rl_panacea,
42	  title   = {{RL} Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for {LLMs}},
43	  author  = {Jin, Hangzhan and others},
44	  journal = {arXiv preprint arXiv:2508.16546},
45	  year    = {2025},
46	  url     = {https://arxiv.org/abs/2508.16546}
47	}
48	
49	@inproceedings{ma2023dreeam,
50	  title     = {{DREEAM}: Guiding Attention with Evidence for Improving Document-Level Relation Extraction},
51	  author    = {Ma, Youmi and Wang, An and Okazaki, Naoaki},
52	  booktitle = {Findings of the Association for Computational Linguistics: EACL 2023},
53	  year      = {2023},
54	  url       = {https://arxiv.org/abs/2302.08675}
55	}
56	
57	@inproceedings{moskovitz2024constrained,
58	  title     = {Confronting Reward Model Overoptimization with Constrained {RLHF}},
59	  author    = {Moskovitz, Ted and Singh, Aaditya K. and Strouse, DJ and Sandholm, Tuomas and Salakhutdinov, Ruslan and Dragan, Anca D. and McAleer, Stephen},
60	  booktitle = {International Conference on Learning Representations},
61	  year      = {2024},
62	  url       = {https://openreview.net/forum?id=gkfUvn0fLU}
63	}
64	
65	@inproceedings{rafailov2023direct,
66	  title     = {Direct Preference Optimization: Your Language Model is Secretly a Reward Model},
67	  author    = {Rafailov, Rafael and Sharma, Archit and Mitchell, Eric and Ermon, Stefano and Manning, Christopher D. and Finn, Chelsea},
68	  booktitle = {Advances in Neural Information Processing Systems},
69	  year      = {2023},
70	  url       = {https://arxiv.org/abs/2305.18290}
71	}
72	
73	@article{shao2024deepseekmath,
74	  title   = {{DeepSeekMath}: Pushing the Limits of Mathematical Reasoning in Open Language Models},
75	  author  = {Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Bi, Xiao and Zhang, Haowei and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},
76	  journal = {arXiv preprint arXiv:2402.03300},
77	  year    = {2024},
78	  url     = {https://arxiv.org/abs/2402.03300}
79	}
80	
81	@inproceedings{tan2022redocred,
82	  title     = {Revisiting {DocRED}: Addressing the False Negative Problem in Relation Extraction},
83	  author    = {Tan, Qingyu and Xu, Lu and Bing, Lidong and Ng, Hwee Tou and Aljunied, Sharifah Mahani},
84	  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
85	  year      = {2022},
86	  url       = {https://aclanthology.org/2022.emnlp-main.580/}
87	}
88	
89	@inproceedings{wan2024genres,
90	  title     = {{GenRES}: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models},
91	  author    = {Jiang, Pengcheng and Lin, Jiacheng and Wang, Zifeng and Sun, Jimeng and Han, Jiawei},
92	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},
93	  year      = {2024},
94	  url       = {https://aclanthology.org/2024.naacl-long.155/}
95	}
96	
97	@inproceedings{xiao2022sais,
98	  title     = {{SAIS}: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction},
99	  author    = {Xiao, Yuxin and Zhang, Zecheng and Mao, Yuning and Yang, Carl and Han, Jiawei},
100	  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics},
101	  year      = {2022},
102	  url       = {https://aclanthology.org/2022.naacl-main.171/}
103	}
104	
105	@inproceedings{xie2022eider,
106	  title     = {{EIDER}: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion},
107	  author    = {Xie, Yiqing and Shen, Jiaming and Li, Sha and Mao, Yuning and Han, Jiawei},
108	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},
109	  year      = {2022},
110	  url       = {https://arxiv.org/abs/2106.08657}
111	}
112	
113	@article{xu2024lmrc,
114	  title   = {{LMRC}: {LLM} with Relation Classifier for Document-Level Relation Extraction},
115	  author  = {Li, Xingzuo and Chen, Kehai and Long, Yunfei and Zhang, Min},
116	  journal = {arXiv preprint arXiv:2408.13889},
117	  year    = {2024},
118	  url     = {https://arxiv.org/abs/2408.13889}
119	}
120	
121	@inproceedings{yao2019docred,
122	  title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},
123	  author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},
124	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
125	  year      = {2019},
126	  url       = {https://aclanthology.org/P19-1074/}
127	}
128	
129	@inproceedings{zelikman2022star,
130	  title     = {{STaR}: Bootstrapping Reasoning With Reasoning},
131	  author    = {Zelikman, Eric and Wu, Yuhuai and Mu, Jesse and Goodman, Noah D.},
132	  booktitle = {Advances in Neural Information Processing Systems},
133	  year      = {2022},
134	  url       = {https://arxiv.org/abs/2203.14465}
135	}
136	
137	@inproceedings{zhao2025egrpo,
138	  title     = {{E-GRPO}: Entity-Aware Reward for Group Relative Policy Optimization},
139	  author    = {{Anonymous}},
140	  booktitle = {International Conference on Learning Representations},
141	  year      = {2026},
142	  url       = {https://arxiv.org/abs/2510.24694}
143	}
144	
145	@article{dong2023raft,
146	  title   = {{RAFT}: Reward r{A}nked {F}ine{T}uning for Generative Foundation Model Alignment},
147	  author  = {Dong, Hanze and Xiong, Wei and Goyal, Deepanshu and Zhang, Yihan and Chow, Winnie and Pan, Rui and Diao, Shizhe and Zhang, Jipeng and Shum, Kashun and Zhang, Tong},
148	  journal = {Transactions on Machine Learning Research},
149	  year    = {2023},
150	  url     = {https://arxiv.org/abs/2304.06767}
151	}
152	
153	@article{ito2025mogrpo,
154	  title   = {{MO-GRPO}: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems},
155	  author  = {Ito, Taishu and others},
156	  journal = {arXiv preprint arXiv:2509.22047},
157	  year    = {2025},
158	  url     = {https://arxiv.org/abs/2509.22047}
159	}
160	
161	@inproceedings{li2025drift,
162	  title     = {Drift: Enhancing {LLM} Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference},
163	  author    = {Li, Jiazheng and Yan, Hanqi and He, Yulan},
164	  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics},
165	  year      = {2025},
166	  url       = {https://aclanthology.org/2025.acl-long.340/}
167	}
168	
169	@article{liu2026gdpo,
170	  title   = {{GDPO}: Group Reward-Decoupled Normalization Policy Optimization for Multi-Reward {RL} Optimization},
171	  author  = {Liu, Shih-Yang and others},
172	  journal = {arXiv preprint arXiv:2601.05242},
173	  year    = {2026},
174	  url     = {https://arxiv.org/abs/2601.05242}
175	}
176	
177	@inproceedings{liu2025drgrpo,
178	  title     = {Understanding {R1}-Zero-Like Training: A Critical Perspective},
179	  author    = {Liu, Zichen and others},
180	  booktitle = {Conference on Language Modeling},
181	  year      = {2025},
182	  url       = {https://arxiv.org/abs/2503.20783}
183	}
184	
185	@article{yu2025dapo,
186	  title   = {{DAPO}: An Open-Source {LLM} Reinforcement Learning System at Scale},
187	  author  = {Yu, Qiying and others},
188	  journal = {arXiv preprint arXiv:2503.14476},
189	  year    = {2025},
190	  url     = {https://arxiv.org/abs/2503.14476}
191	}
192	
193	@inproceedings{zhang2024infuse,
194	  title     = {Fine-Grained Natural Language Inference Based Faithfulness Evaluation for Diverse Summarisation Tasks},
195	  author    = {Zhang, Huajian and Xu, Yumo and Perez-Beltrachini, Laura},
196	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics},
197	  year      = {2024},
198	  url       = {https://aclanthology.org/2024.eacl-long.102/}
199	}
200	
201	@article{chen2025dragrpo,
202	  title   = {{DRA-GRPO}: Exploring Diversity-Aware Reward Adjustment for {R1}-Zero-Like Training of {LLMs}},
203	  author  = {Chen, Xiwen and others},
204	  journal = {arXiv preprint arXiv:2505.09655},
205	  year    = {2025},
206	  url     = {https://arxiv.org/abs/2505.09655}
207	}
208	
209	@article{hu2025reinforcepp,
210	  title   = {{REINFORCE++}: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization},
211	  author  = {Hu, Yifan},
212	  journal = {arXiv preprint arXiv:2501.03262},
213	  year    = {2025},
214	  url     = {https://arxiv.org/abs/2501.03262}
215	}
216	
217	@inproceedings{wang2025rear,
218	  title     = {{REAR}: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support},
219	  author    = {Wang, Yutao and others},
220	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},
221	  year      = {2025}
222	}
223	
224	@article{wang2025relprior,
225	  title   = {{RelPrior}: Relation as a Prior for {LLM}-based Document-Level Relation Extraction},
226	  author  = {Wang, Yuxuan and others},
227	  journal = {arXiv preprint arXiv:2511.08143},
228	  year    = {2025},
229	  url     = {https://arxiv.org/abs/2511.08143}
230	}
231	
232	@article{zhang2025glidre,
233	  title   = {{GLiDRE}: Generalist Lightweight Model for Document-level Relation Extraction},
234	  author  = {Zhang, Xiao and others},
235	  journal = {arXiv preprint arXiv:2508.00757},
236	  year    = {2025},
237	  url     = {https://arxiv.org/abs/2508.00757}
238	}
239	
240	@inproceedings{tang2025rsftppo,
241	  title     = {Rejection Sampling Based Fine Tuning Secretly Performs {PPO}},
242	  author    = {Tang, Yunhao and others},
243	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
244	  year      = {2025},
245	  url       = {https://openreview.net/forum?id=yQ2UivKlir}
246	}
247	
248	@article{wang2025rullm,
249	  title   = {{Ru-LLM}: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction},
250	  author  = {Wang, Chenghao and others},
251	  journal = {NLPCC 2025},
252	  year    = {2025}
253	}
254	
255	@inproceedings{zhou2021atlop,
256	  title     = {Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling},
257	  author    = {Zhou, Wenxuan and Huang, Kevin and Ma, Tengyu and Huang, Jing},
258	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
259	  year      = {2021},
260	  url       = {https://arxiv.org/abs/2010.11304}
261	}
262	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86d19ec7-cb21-4a73-8198-c52f2ef4329e",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "09b5eb8b-5c70-45eb-b3fa-80867e4713be",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib",
      "content": "@inproceedings{autore2024,\n  title     = {{AutoRE}: Document-Level Relation Extraction with Large Language Models},\n  author    = {{Anonymous}},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2403.14888}\n}\n\n@inproceedings{chen2025docksrag,\n  title     = {{DocKS-RAG}: Optimizing Document-Level Relation Extraction through {LLM}-Enhanced Hybrid Prompt Tuning},\n  author    = {Xu and others},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},\n  year      = {2025},\n  url       = {https://proceedings.mlr.press/v267/xu25am.html}\n}\n\n@article{dai2025r1re,\n  title   = {{R1-RE}: Cross-Domain Relation Extraction with {RLVR}},\n  author  = {Dai, Runpeng and Zheng, Tong and others},\n  journal = {arXiv preprint arXiv:2507.04642},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2507.04642}\n}\n\n@inproceedings{gao2023scaling,\n  title     = {Scaling Laws for Reward Model Overoptimization},\n  author    = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2210.10760}\n}\n\n@inproceedings{hu2022lora,\n  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2106.09685}\n}\n\n@article{jin2025rl_panacea,\n  title   = {{RL} Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for {LLMs}},\n  author  = {Jin, Hangzhan and others},\n  journal = {arXiv preprint arXiv:2508.16546},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2508.16546}\n}\n\n@inproceedings{ma2023dreeam,\n  title     = {{DREEAM}: Guiding Attention with Evidence for Improving Document-Level Relation Extraction},\n  author    = {Ma, Youmi and Wang, An and Okazaki, Naoaki},\n  booktitle = {Findings of the Association for Computational Linguistics: EACL 2023},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2302.08675}\n}\n\n@inproceedings{moskovitz2024constrained,\n  title     = {Confronting Reward Model Overoptimization with Constrained {RLHF}},\n  author    = {Moskovitz, Ted and Singh, Aaditya K. and Strouse, DJ and Sandholm, Tuomas and Salakhutdinov, Ruslan and Dragan, Anca D. and McAleer, Stephen},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://openreview.net/forum?id=gkfUvn0fLU}\n}\n\n@inproceedings{rafailov2023direct,\n  title     = {Direct Preference Optimization: Your Language Model is Secretly a Reward Model},\n  author    = {Rafailov, Rafael and Sharma, Archit and Mitchell, Eric and Ermon, Stefano and Manning, Christopher D. and Finn, Chelsea},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2305.18290}\n}\n\n@article{shao2024deepseekmath,\n  title   = {{DeepSeekMath}: Pushing the Limits of Mathematical Reasoning in Open Language Models},\n  author  = {Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Bi, Xiao and Zhang, Haowei and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},\n  journal = {arXiv preprint arXiv:2402.03300},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2402.03300}\n}\n\n@inproceedings{tan2022redocred,\n  title     = {Revisiting {DocRED}: Addressing the False Negative Problem in Relation Extraction},\n  author    = {Tan, Qingyu and Xu, Lu and Bing, Lidong and Ng, Hwee Tou and Aljunied, Sharifah Mahani},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year      = {2022},\n  url       = {https://aclanthology.org/2022.emnlp-main.580/}\n}\n\n@inproceedings{wan2024genres,\n  title     = {{GenRES}: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models},\n  author    = {Jiang, Pengcheng and Lin, Jiacheng and Wang, Zifeng and Sun, Jimeng and Han, Jiawei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n  year      = {2024},\n  url       = {https://aclanthology.org/2024.naacl-long.155/}\n}\n\n@inproceedings{xiao2022sais,\n  title     = {{SAIS}: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction},\n  author    = {Xiao, Yuxin and Zhang, Zecheng and Mao, Yuning and Yang, Carl and Han, Jiawei},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics},\n  year      = {2022},\n  url       = {https://aclanthology.org/2022.naacl-main.171/}\n}\n\n@inproceedings{xie2022eider,\n  title     = {{EIDER}: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion},\n  author    = {Xie, Yiqing and Shen, Jiaming and Li, Sha and Mao, Yuning and Han, Jiawei},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2106.08657}\n}\n\n@article{xu2024lmrc,\n  title   = {{LMRC}: {LLM} with Relation Classifier for Document-Level Relation Extraction},\n  author  = {Li, Xingzuo and Chen, Kehai and Long, Yunfei and Zhang, Min},\n  journal = {arXiv preprint arXiv:2408.13889},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2408.13889}\n}\n\n@inproceedings{yao2019docred,\n  title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n  author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n  year      = {2019},\n  url       = {https://aclanthology.org/P19-1074/}\n}\n\n@inproceedings{zelikman2022star,\n  title     = {{STaR}: Bootstrapping Reasoning With Reasoning},\n  author    = {Zelikman, Eric and Wu, Yuhuai and Mu, Jesse and Goodman, Noah D.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2203.14465}\n}\n\n@inproceedings{zhao2025egrpo,\n  title     = {{E-GRPO}: Entity-Aware Reward for Group Relative Policy Optimization},\n  author    = {{Anonymous}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2510.24694}\n}\n\n@article{dong2023raft,\n  title   = {{RAFT}: Reward r{A}nked {F}ine{T}uning for Generative Foundation Model Alignment},\n  author  = {Dong, Hanze and Xiong, Wei and Goyal, Deepanshu and Zhang, Yihan and Chow, Winnie and Pan, Rui and Diao, Shizhe and Zhang, Jipeng and Shum, Kashun and Zhang, Tong},\n  journal = {Transactions on Machine Learning Research},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2304.06767}\n}\n\n@article{ito2025mogrpo,\n  title   = {{MO-GRPO}: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems},\n  author  = {Ito, Taishu and others},\n  journal = {arXiv preprint arXiv:2509.22047},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2509.22047}\n}\n\n@inproceedings{li2025drift,\n  title     = {Drift: Enhancing {LLM} Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference},\n  author    = {Li, Jiazheng and Yan, Hanqi and He, Yulan},\n  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics},\n  year      = {2025},\n  url       = {https://aclanthology.org/2025.acl-long.340/}\n}\n\n@article{liu2026gdpo,\n  title   = {{GDPO}: Group Reward-Decoupled Normalization Policy Optimization for Multi-Reward {RL} Optimization},\n  author  = {Liu, Shih-Yang and others},\n  journal = {arXiv preprint arXiv:2601.05242},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2601.05242}\n}\n\n@inproceedings{liu2025drgrpo,\n  title     = {Understanding {R1}-Zero-Like Training: A Critical Perspective},\n  author    = {Liu, Zichen and others},\n  booktitle = {Conference on Language Modeling},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2503.20783}\n}\n\n@article{yu2025dapo,\n  title   = {{DAPO}: An Open-Source {LLM} Reinforcement Learning System at Scale},\n  author  = {Yu, Qiying and others},\n  journal = {arXiv preprint arXiv:2503.14476},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2503.14476}\n}\n\n@inproceedings{zhang2024infuse,\n  title     = {Fine-Grained Natural Language Inference Based Faithfulness Evaluation for Diverse Summarisation Tasks},\n  author    = {Zhang, Huajian and Xu, Yumo and Perez-Beltrachini, Laura},\n  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics},\n  year      = {2024},\n  url       = {https://aclanthology.org/2024.eacl-long.102/}\n}\n\n@article{chen2025dragrpo,\n  title   = {{DRA-GRPO}: Exploring Diversity-Aware Reward Adjustment for {R1}-Zero-Like Training of {LLMs}},\n  author  = {Chen, Xiwen and others},\n  journal = {arXiv preprint arXiv:2505.09655},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2505.09655}\n}\n\n@article{hu2025reinforcepp,\n  title   = {{REINFORCE++}: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization},\n  author  = {Hu, Yifan},\n  journal = {arXiv preprint arXiv:2501.03262},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2501.03262}\n}\n\n@inproceedings{wang2025rear,\n  title     = {{REAR}: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support},\n  author    = {Wang, Yutao and others},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year      = {2025}\n}\n\n@article{wang2025relprior,\n  title   = {{RelPrior}: Relation as a Prior for {LLM}-based Document-Level Relation Extraction},\n  author  = {Wang, Yuxuan and others},\n  journal = {arXiv preprint arXiv:2511.08143},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2511.08143}\n}\n\n@article{zhang2025glidre,\n  title   = {{GLiDRE}: Generalist Lightweight Model for Document-level Relation Extraction},\n  author  = {Zhang, Xiao and others},\n  journal = {arXiv preprint arXiv:2508.00757},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2508.00757}\n}\n\n@inproceedings{tang2025rsftppo,\n  title     = {Rejection Sampling Based Fine Tuning Secretly Performs {PPO}},\n  author    = {Tang, Yunhao and others},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},\n  year      = {2025},\n  url       = {https://openreview.net/forum?id=yQ2UivKlir}\n}\n\n@article{wang2025rullm,\n  title   = {{Ru-LLM}: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction},\n  author  = {Wang, Chenghao and others},\n  journal = {NLPCC 2025},\n  year    = {2025}\n}\n\n@inproceedings{zhou2021atlop,\n  title     = {Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling},\n  author    = {Zhou, Wenxuan and Huang, Kevin and Ma, Tengyu and Huang, Jing},\n  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2010.11304}\n}\n",
      "numLines": 262,
      "startLine": 1,
      "totalLines": 262
    }
  },
  "sourceToolAssistantUUID": "86d19ec7-cb21-4a73-8198-c52f2ef4329e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T06:48:49.880Z_

<details open><summary>🔧 Tool call — Read · `toolu_015car5H7zyxb6zUr4x1JEEE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06a94c01-28ee-4cd5-a0d1-3acc99bf85df",
  "isSidechain": false,
  "requestId": "req_011Cb9b3WYJAvj1CA56wvEuf",
  "type": "assistant",
  "uuid": "26be3def-0590-4ceb-8106-cf4c1c091015",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175uQP8vQqP2vH4FRDuCkXq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 28056,
      "output_tokens": 756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 756,
          "cache_read_input_tokens": 28056,
          "cache_creation_input_tokens": 629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 629
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-18T06:48:49.886Z_

<details><summary>↩ Tool result · `toolu_015car5H7zyxb6zUr4x1JEEE`</summary>

```text
1	\section{Introduction}
2	
3	Document-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \citet{zhou2021atlop} long dominated.
4	Recent LLM-based approaches have closed this gap: \citet{autore2024} fine-tune LLMs with structured decomposition for end-to-end extraction, \citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
5	These methods approach or surpass encoder baselines on DocRED \citep{yao2019docred} and Re-DocRED \citep{tan2022redocred} in extraction accuracy.
6	Yet every one of them outputs bare relation triplets $(e_h, r, e_t)$ without any indication of \emph{which sentences} in the document support each prediction.
7	In deployment contexts where predictions feed into clinical knowledge bases, legal due-diligence pipelines, or financial compliance systems, end users cannot verify a prediction without manually locating its textual basis across a multi-page document.
8	
9	The absence of verifiable evidence creates a practical bottleneck.
10	Relation extraction outputs are consumed downstream by knowledge graph construction and human decision workflows.
11	When a system predicts that a drug interacts with a gene, or that a contract clause implies a liability, practitioners must trace each prediction back to source text before acting on it.
12	Without machine-generated evidence, this verification requires exhaustive manual review of the input document for every predicted relation.
13	Encoder-based methods have partially addressed this need: \citet{xiao2022sais} introduce sentence-level evidence supervision as an auxiliary signal, and \citet{ma2023dreeam} extend this with dynamic evidence retrieval through memory attention.
14	Both improve extraction quality \emph{and} produce evidence annotations.
15	However, encoder methods now trail LLM-based approaches in extraction accuracy, and their evidence mechanisms (binary sentence classification) do not transfer to generative architectures.
16	The community therefore faces a gap: the most accurate extractors provide no evidence, while the evidence-capable methods are no longer competitive.
17	
18	This gap reflects a deeper structural difference between evidence in encoder and generative frameworks.
19	In SAIS and DREEAM, evidence retrieval is a binary classification task (does sentence $s_i$ support relation $r$?) that serves as auxiliary supervision.
20	The evidence signal \emph{regularizes} the encoder and improves extraction.
21	In LLM-based DocRE, evidence-grounded extraction requires the model to \emph{generate} complete evidence sentences as part of its output sequence, substantially increasing output length and decoding complexity.
22	Evidence production in this setting is not an auxiliary signal but an additional generation burden that competes with the extraction objective for model capacity.
23	Whether this generation cost necessarily harms extraction, or whether the interaction is more nuanced, remains an open question: the answer may depend on model scale and optimization strategy.
24	This uncertainty motivates a systematic investigation of how evidence production interacts with extraction quality across model scales and optimization paradigms.
25	
26	We formalize evidence-grounded DocRE as a structured generation task for LLMs and conduct a systematic comparison of three post-training optimization paradigms: online reinforcement learning via Group Relative Policy Optimization (GRPO; \citealt{shao2024deepseekmath}), offline preference optimization via Direct Preference Optimization (DPO; \citealt{rafailov2023direct}), and offline reinforcement learning via Rejection Sampling Fine-Tuning (RSFT, building on STaR; \citealt{zelikman2022star}).
27	Our experiments across 85+ configurations, spanning four model scales (1.7B to 8B), two model families, and two datasets, reveal three principal findings.
28	\textbf{First}, we identify a \emph{decoupling spectrum}: the strength of RL optimization pressure correlates with the severity of evidence-extraction decoupling.
29	GRPO with Quantized Low-Rank Adaptation (QLoRA; \citealt{hu2022lora}) produces catastrophic decoupling where extraction accuracy collapses to near zero; GRPO with full-precision training shows mild decoupling; DPO exhibits gradual degradation; and RSFT maintains stable joint performance.
30	QLoRA acts as a catastrophic amplifier of the underlying optimization conflict rather than its root cause.
31	\textbf{Second}, we discover a \emph{scale-dependent evidence tax}: the cost of jointly producing evidence and relations follows a non-monotonic pattern across model scales.
32	At 1.7B parameters, evidence generation provides an implicit regularization benefit of +8 percentage points (pp) in Ign-F1; at 4B, it imposes a $-$7.5pp penalty; at 8B, the tax approaches zero.
33	This non-linear pattern overturns the naive assumption that evidence generation uniformly harms extraction.
34	\textbf{Third}, RSFT with Natural Language Inference (NLI) based Contrastive Evidence Discrimination (CED) scoring emerges as the only effective optimization route.
35	By selecting high-quality training samples through output filtering rather than applying gradient-based optimization pressure, RSFT sidesteps the multi-objective competition that destabilizes RL and preference methods.
36	
37	Our contributions are as follows:
38	\begin{enumerate}
39	    \item We formalize \textbf{evidence-grounded document-level relation extraction} as a generation task for LLMs and conduct the first \textbf{comprehensive empirical study} spanning 85+ experiments across four model scales, two model families, two datasets (DocRED, Re-DocRED), and three optimization paradigms.
40	
41	    \item We characterize a \textbf{decoupling spectrum} across optimization paradigms: RL optimization pressure correlates with evidence-extraction decoupling severity (GRPO catastrophic $\rightarrow$ DPO gradual $\rightarrow$ RSFT none). We introduce the Evidence-Decoupling Ratio (EDCR), a diagnostic that quantifies the degree of misalignment between extraction and evidence capabilities, capturing this relationship with method-level $\rho = -0.965$.
42	
43	    \item We identify a \textbf{scale-dependent evidence tax}: a non-monotonic cost pattern across 1.7B, 4B, and 8B parameters that overturns the assumption that evidence production uniformly degrades extraction quality.
44	
45	    \item We establish \textbf{RSFT with NLI-based CED scoring} as an effective solution, achieving +4.92pp Ign-F1 over SFT at 4B scale (four-seed mean). Our 1.7B RSFT model (50.50 Ign-F1) matches 8B SFT performance (50.51), enabling deployment-efficient evidence-grounded extraction at reduced computational cost.
46	\end{enumerate}
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26be3def-0590-4ceb-8106-cf4c1c091015",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "307c66d0-885a-4efa-b1eb-823b242c2c87",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\nDocument-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \\citet{zhou2021atlop} long dominated.\nRecent LLM-based approaches have closed this gap: \\citet{autore2024} fine-tune LLMs with structured decomposition for end-to-end extraction, \\citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \\citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.\nThese methods approach or surpass encoder baselines on DocRED \\citep{yao2019docred} and Re-DocRED \\citep{tan2022redocred} in extraction accuracy.\nYet every one of them outputs bare relation triplets $(e_h, r, e_t)$ without any indication of \\emph{which sentences} in the document support each prediction.\nIn deployment contexts where predictions feed into clinical knowledge bases, legal due-diligence pipelines, or financial compliance systems, end users cannot verify a prediction without manually locating its textual basis across a multi-page document.\n\nThe absence of verifiable evidence creates a practical bottleneck.\nRelation extraction outputs are consumed downstream by knowledge graph construction and human decision workflows.\nWhen a system predicts that a drug interacts with a gene, or that a contract clause implies a liability, practitioners must trace each prediction back to source text before acting on it.\nWithout machine-generated evidence, this verification requires exhaustive manual review of the input document for every predicted relation.\nEncoder-based methods have partially addressed this need: \\citet{xiao2022sais} introduce sentence-level evidence supervision as an auxiliary signal, and \\citet{ma2023dreeam} extend this with dynamic evidence retrieval through memory attention.\nBoth improve extraction quality \\emph{and} produce evidence annotations.\nHowever, encoder methods now trail LLM-based approaches in extraction accuracy, and their evidence mechanisms (binary sentence classification) do not transfer to generative architectures.\nThe community therefore faces a gap: the most accurate extractors provide no evidence, while the evidence-capable methods are no longer competitive.\n\nThis gap reflects a deeper structural difference between evidence in encoder and generative frameworks.\nIn SAIS and DREEAM, evidence retrieval is a binary classification task (does sentence $s_i$ support relation $r$?) that serves as auxiliary supervision.\nThe evidence signal \\emph{regularizes} the encoder and improves extraction.\nIn LLM-based DocRE, evidence-grounded extraction requires the model to \\emph{generate} complete evidence sentences as part of its output sequence, substantially increasing output length and decoding complexity.\nEvidence production in this setting is not an auxiliary signal but an additional generation burden that competes with the extraction objective for model capacity.\nWhether this generation cost necessarily harms extraction, or whether the interaction is more nuanced, remains an open question: the answer may depend on model scale and optimization strategy.\nThis uncertainty motivates a systematic investigation of how evidence production interacts with extraction quality across model scales and optimization paradigms.\n\nWe formalize evidence-grounded DocRE as a structured generation task for LLMs and conduct a systematic comparison of three post-training optimization paradigms: online reinforcement learning via Group Relative Policy Optimization (GRPO; \\citealt{shao2024deepseekmath}), offline preference optimization via Direct Preference Optimization (DPO; \\citealt{rafailov2023direct}), and offline reinforcement learning via Rejection Sampling Fine-Tuning (RSFT, building on STaR; \\citealt{zelikman2022star}).\nOur experiments across 85+ configurations, spanning four model scales (1.7B to 8B), two model families, and two datasets, reveal three principal findings.\n\\textbf{First}, we identify a \\emph{decoupling spectrum}: the strength of RL optimization pressure correlates with the severity of evidence-extraction decoupling.\nGRPO with Quantized Low-Rank Adaptation (QLoRA; \\citealt{hu2022lora}) produces catastrophic decoupling where extraction accuracy collapses to near zero; GRPO with full-precision training shows mild decoupling; DPO exhibits gradual degradation; and RSFT maintains stable joint performance.\nQLoRA acts as a catastrophic amplifier of the underlying optimization conflict rather than its root cause.\n\\textbf{Second}, we discover a \\emph{scale-dependent evidence tax}: the cost of jointly producing evidence and relations follows a non-monotonic pattern across model scales.\nAt 1.7B parameters, evidence generation provides an implicit regularization benefit of +8 percentage points (pp) in Ign-F1; at 4B, it imposes a $-$7.5pp penalty; at 8B, the tax approaches zero.\nThis non-linear pattern overturns the naive assumption that evidence generation uniformly harms extraction.\n\\textbf{Third}, RSFT with Natural Language Inference (NLI) based Contrastive Evidence Discrimination (CED) scoring emerges as the only effective optimization route.\nBy selecting high-quality training samples through output filtering rather than applying gradient-based optimization pressure, RSFT sidesteps the multi-objective competition that destabilizes RL and preference methods.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item We formalize \\textbf{evidence-grounded document-level relation extraction} as a generation task for LLMs and conduct the first \\textbf{comprehensive empirical study} spanning 85+ experiments across four model scales, two model families, two datasets (DocRED, Re-DocRED), and three optimization paradigms.\n\n    \\item We characterize a \\textbf{decoupling spectrum} across optimization paradigms: RL optimization pressure correlates with evidence-extraction decoupling severity (GRPO catastrophic $\\rightarrow$ DPO gradual $\\rightarrow$ RSFT none). We introduce the Evidence-Decoupling Ratio (EDCR), a diagnostic that quantifies the degree of misalignment between extraction and evidence capabilities, capturing this relationship with method-level $\\rho = -0.965$.\n\n    \\item We identify a \\textbf{scale-dependent evidence tax}: a non-monotonic cost pattern across 1.7B, 4B, and 8B parameters that overturns the assumption that evidence production uniformly degrades extraction quality.\n\n    \\item We establish \\textbf{RSFT with NLI-based CED scoring} as an effective solution, achieving +4.92pp Ign-F1 over SFT at 4B scale (four-seed mean). Our 1.7B RSFT model (50.50 Ign-F1) matches 8B SFT performance (50.51), enabling deployment-efficient evidence-grounded extraction at reduced computational cost.\n\\end{enumerate}\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  },
  "sourceToolAssistantUUID": "26be3def-0590-4ceb-8106-cf4c1c091015",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T06:48:50.352Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DA7x9F25L1dQtnen1dMDGs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "307c66d0-885a-4efa-b1eb-823b242c2c87",
  "isSidechain": false,
  "requestId": "req_011Cb9b3WYJAvj1CA56wvEuf",
  "type": "assistant",
  "uuid": "0354beca-abbc-4122-994f-d0e071afbc67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175uQP8vQqP2vH4FRDuCkXq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 28056,
      "output_tokens": 756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 756,
          "cache_read_input_tokens": 28056,
          "cache_creation_input_tokens": 629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 629
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-18T06:48:50.360Z_

<details><summary>↩ Tool result · `toolu_01DA7x9F25L1dQtnen1dMDGs`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Document-level relation extraction (DocRE) requires reasoning across sentence boundaries to identify relations between entity pairs.
5	DocRED \citep{yao2019docred} established the first large-scale benchmark for this task, catalyzing a line of encoder-based methods that treat DocRE as classification over entity pair representations.
6	ATLOP \citep{zhou2021atlop} introduced adaptive thresholding for multi-label prediction and localized context pooling for entity representations.
7	A parallel thread incorporates sentence-level evidence into these architectures.
8	SAIS \citep{xiao2022sais} introduced evidence supervision as an auxiliary training signal and showed that joint evidence prediction improves extraction through data augmentation and ensemble inference.
9	DREEAM \citep{ma2023dreeam} extended this approach with dynamic memory-based evidence retrieval that guides attention to supporting sentences.
10	EIDER \citep{xie2022eider} jointly trains an evidence extractor and fuses evidence representations into the relation classifier.
11	In all three systems, evidence identification is binary sentence classification over a fixed candidate set, a formulation that adds no output complexity.
12	Recent work has recast DocRE for large language models.
13	AutoRE \citep{autore2024} fine-tunes LLMs with QLoRA using a relation-head-facts decomposition; \citet{xu2024lmrc} frame extraction as multi-choice reading comprehension; RelPrior \citep{wang2025relprior} uses relation priors to guide LLM-based extraction; GLiDRE \citep{zhang2025glidre} presents a generalist lightweight approach; Ru-LLM \citep{wang2025rullm} incorporates logical rule constraints; and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
14	These methods match or surpass encoder baselines but produce bare triplets without evidence.
15	The critical distinction lies in computational nature: in SAIS and DREEAM, evidence retrieval is classification that regularizes the encoder without increasing output length; in LLM-based DocRE, evidence requires additional output tokens per triple, imposing costs that depend on model capacity and optimization strategy.
16	Whether this cost is inevitable or can be mitigated is the central question of our work.
17	
18	Group Relative Policy Optimization (GRPO; \citealt{shao2024deepseekmath}) computes advantages within groups of sampled outputs, eliminating the separate value network.
19	Subsequent work addresses failure modes at scale: DAPO \citep{yu2025dapo} prevents entropy collapse, Dr.\ GRPO \citep{liu2025drgrpo} corrects length bias, REINFORCE++ \citep{hu2025reinforcepp} stabilizes critic-free optimization, and DRA-GRPO \citep{chen2025dragrpo} mitigates diversity-quality inconsistency through sub-modular reward weighting.
20	In multi-objective settings, GDPO \citep{liu2026gdpo} and MO-GRPO \citep{ito2025mogrpo} decouple per-reward normalization and variance-based weighting respectively, both directly relevant to our setting where extraction and evidence quality constitute competing signals.
21	Applications to structured IE include E-GRPO \citep{zhao2025egrpo} for entity-aware rewards, R1-RE \citep{dai2025r1re} for cross-domain relation extraction, and REAR \citep{wang2025rear} for event argument extraction.
22	Direct Preference Optimization \citep{rafailov2023direct} reformulates RLHF as implicit reward maximization.
23	Recent analyses argue RL fine-tuning does not cause catastrophic forgetting \citep{jin2025rl_panacea}; our decoupling spectrum addresses a distinct phenomenon where extraction and evidence compete within a single task.
24	Reward overoptimization \citep{gao2023scaling} and constrained RLHF \citep{moskovitz2024constrained} are directly relevant: our spectrum reveals a new instance where evidence rewards crowd out extraction quality, compounded by QLoRA's constrained parameter space.
25	
26	Evidence faithfulness evaluation has received increasing attention in the broader NLP literature.
27	\citet{li2025drift} propose a dual-reward probabilistic inference framework that improves both accuracy and faithfulness of LLM-generated rationales through controllable generation at inference time.
28	\citet{zhang2024infuse} introduce INFUSE, a fine-grained NLI-based faithfulness metric that evaluates summarization across diverse task types by decomposing premises and hypotheses.
29	Our CED scoring function builds on similar NLI-based principles but targets a different task: discriminating whether predicted evidence sentences genuinely entail the associated relation triple, rather than evaluating free-form rationales or summaries.
30	
31	\citet{zelikman2022star} introduced STaR, an iterative self-improvement method that trains language models on their own correct outputs and bootstraps with rationale augmentation for initially incorrect problems.
32	\citet{dong2023raft} generalize this principle with RAFT, which uses a reward model to rank and filter training samples for alignment fine-tuning.
33	Recent analysis shows that rejection sampling fine-tuning implicitly performs PPO-like optimization \citep{tang2025rsftppo}, providing theoretical grounding for its effectiveness.
34	Our RSFT procedure is a single-round variant: the model samples multiple candidate outputs per input, a quality filter selects the best response, and the model trains on the filtered set without iteration.
35	The contribution of RSFT in our setting is not the self-training framework, which is well-established, but its application to evidence-grounded DocRE with CED/NLI scoring as a domain-specific quality filter.
36	This application reveals a structural advantage of discrete output selection over gradient-based optimization for multi-output tasks.
37	Because RSFT selects complete outputs rather than differentiating through a reward signal, it cannot exploit the extraction-evidence trade-off that GRPO and DPO discover through gradient updates.
38	The filtering mechanism inherently preserves joint quality: it retains outputs that are simultaneously good at extraction and evidence production, rather than allowing one objective to dominate the other.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0354beca-abbc-4122-994f-d0e071afbc67",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "60afe5e4-37cf-4cc1-9123-933dadb22120",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\nDocument-level relation extraction (DocRE) requires reasoning across sentence boundaries to identify relations between entity pairs.\nDocRED \\citep{yao2019docred} established the first large-scale benchmark for this task, catalyzing a line of encoder-based methods that treat DocRE as classification over entity pair representations.\nATLOP \\citep{zhou2021atlop} introduced adaptive thresholding for multi-label prediction and localized context pooling for entity representations.\nA parallel thread incorporates sentence-level evidence into these architectures.\nSAIS \\citep{xiao2022sais} introduced evidence supervision as an auxiliary training signal and showed that joint evidence prediction improves extraction through data augmentation and ensemble inference.\nDREEAM \\citep{ma2023dreeam} extended this approach with dynamic memory-based evidence retrieval that guides attention to supporting sentences.\nEIDER \\citep{xie2022eider} jointly trains an evidence extractor and fuses evidence representations into the relation classifier.\nIn all three systems, evidence identification is binary sentence classification over a fixed candidate set, a formulation that adds no output complexity.\nRecent work has recast DocRE for large language models.\nAutoRE \\citep{autore2024} fine-tunes LLMs with QLoRA using a relation-head-facts decomposition; \\citet{xu2024lmrc} frame extraction as multi-choice reading comprehension; RelPrior \\citep{wang2025relprior} uses relation priors to guide LLM-based extraction; GLiDRE \\citep{zhang2025glidre} presents a generalist lightweight approach; Ru-LLM \\citep{wang2025rullm} incorporates logical rule constraints; and \\citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.\nThese methods match or surpass encoder baselines but produce bare triplets without evidence.\nThe critical distinction lies in computational nature: in SAIS and DREEAM, evidence retrieval is classification that regularizes the encoder without increasing output length; in LLM-based DocRE, evidence requires additional output tokens per triple, imposing costs that depend on model capacity and optimization strategy.\nWhether this cost is inevitable or can be mitigated is the central question of our work.\n\nGroup Relative Policy Optimization (GRPO; \\citealt{shao2024deepseekmath}) computes advantages within groups of sampled outputs, eliminating the separate value network.\nSubsequent work addresses failure modes at scale: DAPO \\citep{yu2025dapo} prevents entropy collapse, Dr.\\ GRPO \\citep{liu2025drgrpo} corrects length bias, REINFORCE++ \\citep{hu2025reinforcepp} stabilizes critic-free optimization, and DRA-GRPO \\citep{chen2025dragrpo} mitigates diversity-quality inconsistency through sub-modular reward weighting.\nIn multi-objective settings, GDPO \\citep{liu2026gdpo} and MO-GRPO \\citep{ito2025mogrpo} decouple per-reward normalization and variance-based weighting respectively, both directly relevant to our setting where extraction and evidence quality constitute competing signals.\nApplications to structured IE include E-GRPO \\citep{zhao2025egrpo} for entity-aware rewards, R1-RE \\citep{dai2025r1re} for cross-domain relation extraction, and REAR \\citep{wang2025rear} for event argument extraction.\nDirect Preference Optimization \\citep{rafailov2023direct} reformulates RLHF as implicit reward maximization.\nRecent analyses argue RL fine-tuning does not cause catastrophic forgetting \\citep{jin2025rl_panacea}; our decoupling spectrum addresses a distinct phenomenon where extraction and evidence compete within a single task.\nReward overoptimization \\citep{gao2023scaling} and constrained RLHF \\citep{moskovitz2024constrained} are directly relevant: our spectrum reveals a new instance where evidence rewards crowd out extraction quality, compounded by QLoRA's constrained parameter space.\n\nEvidence faithfulness evaluation has received increasing attention in the broader NLP literature.\n\\citet{li2025drift} propose a dual-reward probabilistic inference framework that improves both accuracy and faithfulness of LLM-generated rationales through controllable generation at inference time.\n\\citet{zhang2024infuse} introduce INFUSE, a fine-grained NLI-based faithfulness metric that evaluates summarization across diverse task types by decomposing premises and hypotheses.\nOur CED scoring function builds on similar NLI-based principles but targets a different task: discriminating whether predicted evidence sentences genuinely entail the associated relation triple, rather than evaluating free-form rationales or summaries.\n\n\\citet{zelikman2022star} introduced STaR, an iterative self-improvement method that trains language models on their own correct outputs and bootstraps with rationale augmentation for initially incorrect problems.\n\\citet{dong2023raft} generalize this principle with RAFT, which uses a reward model to rank and filter training samples for alignment fine-tuning.\nRecent analysis shows that rejection sampling fine-tuning implicitly performs PPO-like optimization \\citep{tang2025rsftppo}, providing theoretical grounding for its effectiveness.\nOur RSFT procedure is a single-round variant: the model samples multiple candidate outputs per input, a quality filter selects the best response, and the model trains on the filtered set without iteration.\nThe contribution of RSFT in our setting is not the self-training framework, which is well-established, but its application to evidence-grounded DocRE with CED/NLI scoring as a domain-specific quality filter.\nThis application reveals a structural advantage of discrete output selection over gradient-based optimization for multi-output tasks.\nBecause RSFT selects complete outputs rather than differentiating through a reward signal, it cannot exploit the extraction-evidence trade-off that GRPO and DPO discover through gradient updates.\nThe filtering mechanism inherently preserves joint quality: it retains outputs that are simultaneously good at extraction and evidence production, rather than allowing one objective to dominate the other.\n",
      "numLines": 39,
      "startLine": 1,
      "totalLines": 39
    }
  },
  "sourceToolAssistantUUID": "0354beca-abbc-4122-994f-d0e071afbc67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T06:48:50.822Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ERFnJYgbq6fGebbRXd5BFB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60afe5e4-37cf-4cc1-9123-933dadb22120",
  "isSidechain": false,
  "requestId": "req_011Cb9b3WYJAvj1CA56wvEuf",
  "type": "assistant",
  "uuid": "0407ce9a-0847-4159-8c4f-2a79ab814c79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175uQP8vQqP2vH4FRDuCkXq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 28056,
      "output_tokens": 756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 756,
          "cache_read_input_tokens": 28056,
          "cache_creation_input_tokens": 629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 629
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-18T06:48:50.826Z_

<details><summary>↩ Tool result · `toolu_01ERFnJYgbq6fGebbRXd5BFB`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}
5	\label{sec:task}
6	
7	Given a document $D = \{s_1, \ldots, s_n\}$ consisting of $n$ sentences and a set of entities $\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \in \mathcal{E} \times \mathcal{E}$, a relation $r \in \mathcal{R} \cup \{\texttt{NA}\}$ together with a set of supporting evidence sentences $E \subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support.
8	
9	In our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\citep{xiao2022sais} and DREEAM~\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sentences. This scale-dependent cost is the central phenomenon we investigate.
10	
11	
12	\subsection{Supervised Fine-Tuning Baseline}
13	\label{sec:sft}
14	
15	We fine-tune all models with LoRA~\citep{hu2022lora} at rank $r{=}64$ and scaling factor $\alpha{=}128$, applied to attention projection matrices. The training data consists of DocRED~\citep{yao2019docred} training documents converted to the structured output format described above, where each example maps a document and its entity set to the complete set of relation triples with evidence annotations. We also train a \emph{no-evidence} variant under identical configuration but with evidence references removed from the output format, producing only \texttt{(head, relation, tail)}. This variant serves as an upper bound on extraction performance by eliminating the generation cost of evidence, and allows direct measurement of the evidence tax at each model scale. Detailed hyperparameters (learning rate, batch size, number of epochs) are reported in the Appendix.
16	
17	
18	\subsection{Optimization Paradigms}
19	\label{sec:paradigms}
20	
21	We evaluate three post-SFT optimization paradigms that differ in how they incorporate quality signals from the CED scoring function (\S\ref{sec:ced}).
22	
23	\paragraph{GRPO.}
24	Group Relative Policy Optimization~\citep{shao2024deepseekmath} is an online RL method that eliminates the need for a separate value network by computing advantages within groups of sampled outputs. For each training document, the policy generates $G$ candidate responses, which are scored by CED. The advantage of each response is computed relative to the group mean, and the policy is updated to increase the probability of above-average outputs. We test two configurations: QLoRA with $G{=}4$ groups under 4-bit quantization, and bf16 full-precision LoRA with $G{=}8$. Because GRPO applies gradient updates that directly optimize the reward signal, evidence quality and extraction accuracy compete for gradient capacity. We analyze this multi-objective tension in Section~\ref{sec:spectrum}.
25	
26	\paragraph{DPO.}
27	Direct Preference Optimization~\citep{rafailov2023direct} reformulates RLHF as a classification problem over preference pairs, without explicit reward models. We construct preference data from the SFT model's sampled outputs: for each document, the response with the highest CED score is labeled as preferred and the lowest-scoring response as rejected. DPO then adjusts the policy to increase the log-probability ratio between preferred and rejected completions. We train for 1 and 3 epochs to observe the temporal dynamics of evidence-extraction trade-offs under implicit optimization.
28	
29	\paragraph{RSFT.}
30	Rejection Sampling Fine-Tuning is a single-round variant of iterative self-improvement methods such as STaR~\citep{zelikman2022star}. The procedure is straightforward: the SFT model generates $N{=}8$ candidate outputs per training document, each candidate is scored by CED, and only the top-$k{=}1$ response is retained as training data. From 24,216 candidate outputs, this selection yields 9,042 training examples (37.3\% acceptance rate). Unlike GRPO and DPO, RSFT does not apply gradient-based optimization pressure toward a reward signal. Instead, it improves training data quality through filtering: the model trains on its own best outputs rather than all outputs. This distinction is critical because discrete selection over complete outputs cannot exploit the extraction-evidence trade-off that gradient methods find. The contribution of RSFT in our setting is not the framework itself, which is well-established, but its application to evidence-grounded DocRE with CED as a domain-specific quality filter.
31	
32	
33	\subsection{Contrastive Evidence Discrimination}
34	\label{sec:ced}
35	
36	CED is a scoring function that evaluates the faithfulness of predicted evidence sentences to their associated relation triples. It builds on Natural Language Inference (NLI) to measure whether evidence actually entails the predicted relation, rather than merely co-occurring with the relevant entities.
37	
38	For a predicted triple $(e_h, r, e_t)$ with evidence sentences $E$, CED constructs a positive NLI pair: the premise is the concatenation of sentences in $E$, and the hypothesis is a natural-language verbalization of the relation (e.g., ``$e_h$ has relation $r$ with $e_t$''). An NLI model (\texttt{cross-encoder/nli-deberta-v3-base}) produces an entailment probability $p^+$ for this pair. The contrastive component introduces hard negatives drawn from the same document. For each triple, we collect sentences that mention $e_h$ or $e_t$ but are not in the predicted evidence set. These entity-sharing distractors serve as negative premises, and the NLI model scores each to obtain $p^-_1, \ldots, p^-_m$. The CED score for a single triple is:
39	\begin{equation}
40	\text{CED}(e_h, r, e_t, E) = p^+ - \max_j \, p^-_j
41	\label{eq:ced}
42	\end{equation}
43	This formulation forces the scoring function to distinguish sentences that genuinely support the relation from sentences that merely mention the same entities. A high CED score indicates that the evidence provides relation-specific support beyond entity co-occurrence.
44	
45	The document-level CED score aggregates over all predicted triples, weighted by extraction correctness: triples that match ground-truth relations contribute their CED scores, while incorrect triples receive zero credit. This coupling ensures that CED rewards both faithful evidence and accurate extraction jointly.
46	
47	We also evaluate a \emph{flat-NLI} baseline that uses only the positive entailment score $p^+$ without the contrastive term. In our experiments (Section~\ref{sec:spectrum}), CED and flat-NLI produce comparable RSFT outcomes (mean Rel-F1 difference of 0.02pp across available seeds), and both outperform random selection and no-scoring baselines. We adopt CED as the default because the contrastive formulation provides interpretable per-triple discrimination scores that flat-NLI lacks.
48	
49	
50	\subsection{Evidence-Decoupling Ratio}
51	\label{sec:edcr}
52	
53	We introduce the Evidence-Decoupling Ratio (EDCR) as a diagnostic metric that quantifies the degree of misalignment between a model's extraction and evidence capabilities. EDCR is not a training component; it serves purely as an analytical tool for comparing optimization methods.
54	
55	EDCR is defined as:
56	\begin{equation}
57	\text{EDCR} = \frac{\text{Evi-Recall}_{\text{TP}}}{\text{Rel-Recall}}
58	\label{eq:edcr}
59	\end{equation}
60	where $\text{Evi-Recall}_{\text{TP}}$ is evidence sentence recall computed only over correctly predicted triples (true positives), and $\text{Rel-Recall}$ is overall relation extraction recall. The numerator captures evidence quality on the subset of triples the model gets right; the denominator captures how many triples the model identifies in total.
61	
62	The intuition is as follows. A model that correctly identifies a few triples and provides excellent evidence for them, but misses most triples entirely, will have high $\text{Evi-Recall}_{\text{TP}}$ and low $\text{Rel-Recall}$, yielding a high EDCR. This pattern signals that evidence quality has decoupled from extraction capability: the model produces faithful evidence only within a narrow comfort zone.
63	
64	EDCR operates at two diagnostic levels. At the method level, comparing EDCR across optimization paradigms reveals a strong negative correlation with Rel-F1 (Spearman $\rho{=}{-}0.965$): methods with higher EDCR produce worse extraction, confirming that elevated EDCR signals problematic decoupling. At the per-relation level, computing EDCR for individual relation types reveals variation that is independent of Evi-F1 ($\rho{=}{-}0.064$, $p{=}0.58$). This independence means EDCR captures relation-specific extraction-evidence misalignment that aggregate evidence metrics miss. The SFT baseline EDCR (0.6982) reflects the inherent cost of evidence generation; EDCR values substantially exceeding this level (e.g., GRPO QLoRA at 0.9876) indicate RL-induced decoupling beyond what evidence production alone explains, while values below the baseline (e.g., RSFT at 0.6503) reflect improved co-optimization.
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0407ce9a-0847-4159-8c4f-2a79ab814c79",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "f230f94c-1156-477b-a576-de43b7d7dfdc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}\n\\label{sec:task}\n\nGiven a document $D = \\{s_1, \\ldots, s_n\\}$ consisting of $n$ sentences and a set of entities $\\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \\in \\mathcal{E} \\times \\mathcal{E}$, a relation $r \\in \\mathcal{R} \\cup \\{\\texttt{NA}\\}$ together with a set of supporting evidence sentences $E \\subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support.\n\nIn our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \\texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\\citep{xiao2022sais} and DREEAM~\\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sentences. This scale-dependent cost is the central phenomenon we investigate.\n\n\n\\subsection{Supervised Fine-Tuning Baseline}\n\\label{sec:sft}\n\nWe fine-tune all models with LoRA~\\citep{hu2022lora} at rank $r{=}64$ and scaling factor $\\alpha{=}128$, applied to attention projection matrices. The training data consists of DocRED~\\citep{yao2019docred} training documents converted to the structured output format described above, where each example maps a document and its entity set to the complete set of relation triples with evidence annotations. We also train a \\emph{no-evidence} variant under identical configuration but with evidence references removed from the output format, producing only \\texttt{(head, relation, tail)}. This variant serves as an upper bound on extraction performance by eliminating the generation cost of evidence, and allows direct measurement of the evidence tax at each model scale. Detailed hyperparameters (learning rate, batch size, number of epochs) are reported in the Appendix.\n\n\n\\subsection{Optimization Paradigms}\n\\label{sec:paradigms}\n\nWe evaluate three post-SFT optimization paradigms that differ in how they incorporate quality signals from the CED scoring function (\\S\\ref{sec:ced}).\n\n\\paragraph{GRPO.}\nGroup Relative Policy Optimization~\\citep{shao2024deepseekmath} is an online RL method that eliminates the need for a separate value network by computing advantages within groups of sampled outputs. For each training document, the policy generates $G$ candidate responses, which are scored by CED. The advantage of each response is computed relative to the group mean, and the policy is updated to increase the probability of above-average outputs. We test two configurations: QLoRA with $G{=}4$ groups under 4-bit quantization, and bf16 full-precision LoRA with $G{=}8$. Because GRPO applies gradient updates that directly optimize the reward signal, evidence quality and extraction accuracy compete for gradient capacity. We analyze this multi-objective tension in Section~\\ref{sec:spectrum}.\n\n\\paragraph{DPO.}\nDirect Preference Optimization~\\citep{rafailov2023direct} reformulates RLHF as a classification problem over preference pairs, without explicit reward models. We construct preference data from the SFT model's sampled outputs: for each document, the response with the highest CED score is labeled as preferred and the lowest-scoring response as rejected. DPO then adjusts the policy to increase the log-probability ratio between preferred and rejected completions. We train for 1 and 3 epochs to observe the temporal dynamics of evidence-extraction trade-offs under implicit optimization.\n\n\\paragraph{RSFT.}\nRejection Sampling Fine-Tuning is a single-round variant of iterative self-improvement methods such as STaR~\\citep{zelikman2022star}. The procedure is straightforward: the SFT model generates $N{=}8$ candidate outputs per training document, each candidate is scored by CED, and only the top-$k{=}1$ response is retained as training data. From 24,216 candidate outputs, this selection yields 9,042 training examples (37.3\\% acceptance rate). Unlike GRPO and DPO, RSFT does not apply gradient-based optimization pressure toward a reward signal. Instead, it improves training data quality through filtering: the model trains on its own best outputs rather than all outputs. This distinction is critical because discrete selection over complete outputs cannot exploit the extraction-evidence trade-off that gradient methods find. The contribution of RSFT in our setting is not the framework itself, which is well-established, but its application to evidence-grounded DocRE with CED as a domain-specific quality filter.\n\n\n\\subsection{Contrastive Evidence Discrimination}\n\\label{sec:ced}\n\nCED is a scoring function that evaluates the faithfulness of predicted evidence sentences to their associated relation triples. It builds on Natural Language Inference (NLI) to measure whether evidence actually entails the predicted relation, rather than merely co-occurring with the relevant entities.\n\nFor a predicted triple $(e_h, r, e_t)$ with evidence sentences $E$, CED constructs a positive NLI pair: the premise is the concatenation of sentences in $E$, and the hypothesis is a natural-language verbalization of the relation (e.g., ``$e_h$ has relation $r$ with $e_t$''). An NLI model (\\texttt{cross-encoder/nli-deberta-v3-base}) produces an entailment probability $p^+$ for this pair. The contrastive component introduces hard negatives drawn from the same document. For each triple, we collect sentences that mention $e_h$ or $e_t$ but are not in the predicted evidence set. These entity-sharing distractors serve as negative premises, and the NLI model scores each to obtain $p^-_1, \\ldots, p^-_m$. The CED score for a single triple is:\n\\begin{equation}\n\\text{CED}(e_h, r, e_t, E) = p^+ - \\max_j \\, p^-_j\n\\label{eq:ced}\n\\end{equation}\nThis formulation forces the scoring function to distinguish sentences that genuinely support the relation from sentences that merely mention the same entities. A high CED score indicates that the evidence provides relation-specific support beyond entity co-occurrence.\n\nThe document-level CED score aggregates over all predicted triples, weighted by extraction correctness: triples that match ground-truth relations contribute their CED scores, while incorrect triples receive zero credit. This coupling ensures that CED rewards both faithful evidence and accurate extraction jointly.\n\nWe also evaluate a \\emph{flat-NLI} baseline that uses only the positive entailment score $p^+$ without the contrastive term. In our experiments (Section~\\ref{sec:spectrum}), CED and flat-NLI produce comparable RSFT outcomes (mean Rel-F1 difference of 0.02pp across available seeds), and both outperform random selection and no-scoring baselines. We adopt CED as the default because the contrastive formulation provides interpretable per-triple discrimination scores that flat-NLI lacks.\n\n\n\\subsection{Evidence-Decoupling Ratio}\n\\label{sec:edcr}\n\nWe introduce the Evidence-Decoupling Ratio (EDCR) as a diagnostic metric that quantifies the degree of misalignment between a model's extraction and evidence capabilities. EDCR is not a training component; it serves purely as an analytical tool for comparing optimization methods.\n\nEDCR is defined as:\n\\begin{equation}\n\\text{EDCR} = \\frac{\\text{Evi-Recall}_{\\text{TP}}}{\\text{Rel-Recall}}\n\\label{eq:edcr}\n\\end{equation}\nwhere $\\text{Evi-Recall}_{\\text{TP}}$ is evidence sentence recall computed only over correctly predicted triples (true positives), and $\\text{Rel-Recall}$ is overall relation extraction recall. The numerator captures evidence quality on the subset of triples the model gets right; the denominator captures how many triples the model identifies in total.\n\nThe intuition is as follows. A model that correctly identifies a few triples and provides excellent evidence for them, but misses most triples entirely, will have high $\\text{Evi-Recall}_{\\text{TP}}$ and low $\\text{Rel-Recall}$, yielding a high EDCR. This pattern signals that evidence quality has decoupled from extraction capability: the model produces faithful evidence only within a narrow comfort zone.\n\nEDCR operates at two diagnostic levels. At the method level, comparing EDCR across optimization paradigms reveals a strong negative correlation with Rel-F1 (Spearman $\\rho{=}{-}0.965$): methods with higher EDCR produce worse extraction, confirming that elevated EDCR signals problematic decoupling. At the per-relation level, computing EDCR for individual relation types reveals variation that is independent of Evi-F1 ($\\rho{=}{-}0.064$, $p{=}0.58$). This independence means EDCR captures relation-specific extraction-evidence misalignment that aggregate evidence metrics miss. The SFT baseline EDCR (0.6982) reflects the inherent cost of evidence generation; EDCR values substantially exceeding this level (e.g., GRPO QLoRA at 0.9876) indicate RL-induced decoupling beyond what evidence production alone explains, while values below the baseline (e.g., RSFT at 0.6503) reflect improved co-optimization.\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  },
  "sourceToolAssistantUUID": "0407ce9a-0847-4159-8c4f-2a79ab814c79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T06:48:51.292Z_

<details open><summary>🔧 Tool call — Read · `toolu_0193xWZhiSZevvuYYbMT8vJW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f230f94c-1156-477b-a576-de43b7d7dfdc",
  "isSidechain": false,
  "requestId": "req_011Cb9b3WYJAvj1CA56wvEuf",
  "type": "assistant",
  "uuid": "cefe4685-ca99-4d0a-8d88-e3c77ac2e86b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175uQP8vQqP2vH4FRDuCkXq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 28056,
      "output_tokens": 756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 756,
          "cache_read_input_tokens": 28056,
          "cache_creation_input_tokens": 629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 629
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-18T06:48:51.299Z_

<details><summary>↩ Tool result · `toolu_0193xWZhiSZevvuYYbMT8vJW`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Dataset.}
8	We conduct experiments on DocRED~\citep{yao2019docred}, a large-scale document-level relation extraction benchmark containing 3,053 training and 998 development documents spanning 96 relation types. Each document requires identifying relational triples across multiple sentences and grounding each triple with supporting evidence sentences. We use Re-DocRED~\citep{tan2022redocred} for cross-dataset generalization evaluation.
9	
10	\paragraph{Models.}
11	Our primary model is Qwen3-4B. To study scale effects, we additionally train Qwen3-1.7B and Qwen3-8B under identical configurations. We include LLaMA-3.1-8B as a cross-family validation point.
12	
13	\paragraph{Training.}
14	All models use LoRA~\citep{hu2022lora} with rank $r{=}64$ and $\alpha{=}128$ over a structured output format that jointly produces relation triples and evidence sentences. For RSFT, we sample $N{=}8$ candidate outputs per document and select the top-$k{=}1$ response ranked by CED scoring (\S\ref{sec:ced}), which combines NLI-based evidence faithfulness with extraction accuracy. GRPO experiments use group sizes $G{=}4$ (QLoRA, 4-bit) and $G{=}8$ (bf16 full-precision LoRA). DPO constructs preference pairs from CED-ranked outputs.
15	
16	\paragraph{Metrics.}
17	We report five metrics. \textbf{Ign-F1} is the primary DocRED metric that ignores triples appearing in the training set, matching the official leaderboard protocol. \textbf{Rel-F1} measures relation extraction F1 on all triples. \textbf{Evi-F1 (TP-only)} measures evidence sentence F1 conditioned on correctly predicted triples, reflecting evidence quality independent of extraction errors. \textbf{Evi-F1 (joint)} includes false-positive and false-negative triples in the denominator following the DREEAM protocol~\citep{ma2023dreeam}, enabling cross-method evidence comparison. \textbf{EDCR} (Evidence-Decoupling Ratio) is our proposed diagnostic: the ratio of evidence recall on correctly-predicted triples to overall extraction recall, where values substantially exceeding the SFT baseline indicate RL-induced decoupling. All primary results use the development set; test set submission is pending.
18	
19	
20	\subsection{Main Results}
21	\label{sec:main_results}
22	
23	Table~\ref{tab:main} presents the primary comparison between SFT, no-evidence SFT, and RSFT CED on Qwen3-4B. The SFT baseline achieves 39.74 Ign-F1 with joint evidence generation. Removing evidence from the output format entirely (no-evidence SFT) improves extraction to 47.21 Ign-F1, a 7.47-point gap that quantifies the \emph{evidence tax} at the 4B scale. RSFT CED achieves a four-seed mean of 44.66 Ign-F1 (+4.92 over SFT, standard deviation 0.49) while maintaining evidence quality (Evi-F1 81.15 vs.\ 79.86 for SFT). The EDCR decreases from 0.6982 to 0.6503, confirming tighter coupling between extraction and evidence capabilities. Per-seed results appear in Appendix~\ref{sec:ablation_full}.
24	
25	The remaining gap to the no-evidence upper bound (2.09 points) represents the residual cost of producing structured evidence, a cost that shrinks at larger scales as we show in Section~\ref{sec:scaling}.
26	
27	\begin{table}[t]
28	\centering
29	\caption{Main results on DocRED dev set (Qwen3-4B). RSFT reports four-seed mean $\pm$ std. Best Ign-F1 in \textbf{bold}; best among evidence-generating methods \underline{underlined}. Per-seed breakdown in Appendix Table~\ref{tab:ablation_full}.}
30	\label{tab:main}
31	\small
32	\resizebox{\columnwidth}{!}{%
33	\begin{tabular}{lcccc}
34	\toprule
35	\textbf{Method} & \textbf{Ign-F1} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
36	\midrule
37	SFT baseline & 39.74 & 0.4049 & 79.86 & 0.6982 \\
38	SFT no-evidence & \textbf{47.21} & \textbf{0.4876} & -- & -- \\
39	RSFT CED & \underline{44.66{\scriptsize$\pm$0.49}} & \underline{0.4563} & 81.15 & 0.6503 \\
40	\bottomrule
41	\end{tabular}%
42	}
43	\end{table}
44	
45	
46	\subsection{Evidence-Extraction Decoupling Spectrum}
47	\label{sec:spectrum}
48	
49	Different RL algorithms produce qualitatively different failure modes when applied to joint evidence-and-extraction generation. We organize these outcomes along a \emph{decoupling spectrum} ranging from catastrophic collapse to mild perturbation, shown in Table~\ref{tab:spectrum} (visualized in Figure~\ref{fig:spectrum}, Appendix).
50	
51	\paragraph{GRPO QLoRA: catastrophic collapse.}
52	Under QLoRA quantization ($G{=}4$), GRPO drives Rel-F1 to 0.0138 (near zero extraction) while Evi-F1 rises to 85.04 and EDCR reaches 0.9876. The model learns to produce well-formed evidence sentences but loses the ability to predict correct relation triples. This extreme decoupling occurs because 4-bit quantization constrains the effective parameter space, forcing the reward signal to optimize whichever sub-task yields easier gradient progress. Evidence sentence generation, being closer to extractive summarization, wins this competition.
53	
54	\paragraph{GRPO bf16: mild, non-monotonic.}
55	Full-precision GRPO ($G{=}8$) avoids catastrophe. Its training trajectory shows non-monotonic Rel-F1 fluctuation (0.434 at step 30, 0.428 at step 50, 0.434 at step 70, 0.455 at step 100), stabilizing near the SFT baseline. The best checkpoint achieves Rel-F1 0.4549 with Evi-F1 80.86 and EDCR 0.6318. The decoupling is mild: bf16 precision preserves enough capacity for both sub-tasks to improve jointly, though the non-monotonic trajectory suggests fragile optimization dynamics that require careful checkpoint selection.
56	
57	\paragraph{DPO: gradual decay.}
58	DPO preference learning shows a progressive pattern. At 1 epoch, Rel-F1 remains at 0.4034 with Evi-F1 80.88 and EDCR 0.7139. Extended training (3 epochs) degrades extraction to 0.3429 while evidence improves to 84.03\footnote{DPO 3-epoch results use the pre-D076 evaluation protocol; included for trend analysis.}, with EDCR rising to 0.7294. Unlike GRPO's sudden collapse, DPO gradually trades extraction quality for evidence quality as training progresses.
59	
60	\paragraph{RSFT: no decoupling.}
61	RSFT avoids the decoupling problem entirely. By selecting high-quality complete outputs (jointly good extraction and evidence) rather than applying gradient-based reward maximization, RSFT maintains both capabilities simultaneously (mean Rel-F1 0.4563, Evi-F1 81.15, EDCR 0.6503). The key insight is that rejection sampling operates on discrete outputs rather than differentiable reward signals, so it cannot exploit the extraction-evidence trade-off that gradient methods find.
62	
63	\begin{table}[t]
64	\centering
65	\caption{Evidence-extraction decoupling across RL paradigms (Qwen3-4B). Severity indicates the degree of extraction collapse relative to evidence improvement.}
66	\label{tab:spectrum}
67	\small
68	\resizebox{\columnwidth}{!}{%
69	\begin{tabular}{llcccc}
70	\toprule
71	\textbf{Paradigm} & \textbf{Config} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} & \textbf{Severity} \\
72	\midrule
73	GRPO & QLoRA $G{=}4$ & 0.0138 & 85.04 & 0.9876 & Catastrophic \\
74	GRPO & bf16 $G{=}8$ & 0.4549 & 80.86 & 0.6318 & Mild \\
75	DPO & bf16 1ep & 0.4034 & 80.88 & 0.7139 & Gradual \\
76	DPO & bf16 3ep$^\dagger$ & 0.3429 & 84.03 & 0.7294 & Gradual \\
77	\midrule
78	SFT & baseline & 0.4049 & 79.86 & 0.6982 & None \\
79	RSFT & CED (mean) & 0.4563 & 81.15 & 0.6503 & None \\
80	\bottomrule
81	\end{tabular}%
82	}
83	\vspace{-2mm}
84	{\raggedright\footnotesize $^\dagger$Pre-D076 evaluation protocol.\par}
85	\end{table}
86	
87	
88	\subsection{Scale-Dependent Evidence Tax}
89	\label{sec:scaling}
90	
91	The evidence tax, defined as the Ign-F1 difference between no-evidence and joint-evidence SFT, varies non-monotonically across model scales. Table~\ref{tab:scaling} presents this analysis across four models (Figure~\ref{fig:scaling} in Appendix).
92	
93	At the 4B scale, the evidence tax is severe: $-7.47$ points. Generating evidence sentences alongside relation triples consumes capacity that would otherwise improve extraction. At 8B, the tax nearly vanishes ($-0.28$ points for Qwen3-8B, $-0.68$ for LLaMA-3.1-8B), indicating that 8B-class models have sufficient capacity to handle both tasks simultaneously. The most surprising result appears at 1.7B: instead of paying a larger tax, the smallest model \emph{benefits} from evidence generation (+8.04 points). On a fair evaluation subset that controls for output format effects (see Appendix), this benefit is +6.2 points. We hypothesize that for small models, the evidence generation task provides implicit regularization, forcing the model to attend to supporting context rather than memorizing surface-level patterns.
94	
95	RSFT improves all scales. The gain is +2.64 for 1.7B, +4.92 for 4B, and +3.82 for 8B, confirming that CED-based selection generalizes across model capacities. The 4B model benefits most because it has the largest evidence tax to recover from. A striking consequence of this pattern is that 1.7B RSFT achieves 50.50 Ign-F1, nearly matching 8B SFT at 50.51. CED-based rejection sampling enables a 1.7B model to rival a 4.7$\times$ larger model on evidence-grounded extraction, with direct implications for deployment cost: practitioners can substitute a small model with RSFT for a large model with vanilla SFT at comparable accuracy.
96	
97	\begin{table}[t]
98	\centering
99	\caption{Scale-dependent evidence tax and RSFT gain. Evidence tax = SFT with evidence minus SFT no-evidence (positive means evidence helps). All results on DocRED dev set Ign-F1.}
100	\label{tab:scaling}
101	\small
102	\resizebox{\columnwidth}{!}{%
103	\begin{tabular}{lccccc}
104	\toprule
105	\textbf{Model} & \textbf{SFT w/ evi} & \textbf{No-evi} & \textbf{RSFT} & \textbf{Evi Tax} & \textbf{RSFT Gain} \\
106	\midrule
107	Qwen3-1.7B & 47.86 & 39.82 & 50.50 & +8.04 & +2.64 \\
108	Qwen3-4B & 39.74 & 47.21 & 44.66 & $-$7.47 & +4.92 \\
109	Qwen3-8B & 50.51 & 50.79 & \textbf{54.33} & $-$0.28 & +3.82 \\
110	LLaMA-3.1-8B & 53.84 & 54.52 & 55.58 & $-$0.68 & +1.74 \\
111	\bottomrule
112	\end{tabular}%
113	}
114	\end{table}
115	
116	
117	\subsection{Evidence Strategy Comparison}
118	\label{sec:evidence_strategy}
119	
120	We compare joint generation against post-hoc retrieval, using Evi-F1 (joint) with the DREEAM-protocol denominator~\citep{ma2023dreeam} for fair cross-strategy comparison. Post-hoc BM25 retrieval (entity-constrained, $k{=}2$ sentences per triple) achieves higher Rel-F1 (0.4876) by avoiding the evidence tax, but produces lower Evi-F1 (joint) of 0.347 with EDCR 0.766. RSFT CED (s43) reaches Evi-F1 (joint) 0.361 with EDCR 0.654, a 1.4-point evidence advantage and 0.112 EDCR reduction. CED reranking at inference time (selecting the best of $N{=}8$ outputs by CED score) achieves Rel-F1 0.4864 and Evi-F1 81.88 (TP-only), approaching no-evidence extraction quality while preserving evidence. Joint training produces more faithful evidence grounded in the extraction reasoning rather than retrieved post-hoc; inference-time reranking complements this by recovering extraction accuracy.
121	
122	
123	\subsection{Generalization}
124	\label{sec:generalization}
125	
126	Cross-architecture validation on LLaMA-3.1-8B confirms the scaling patterns: the evidence tax at 8B is near zero ($-0.68$ points), and RSFT CED yields +1.74 Ign-F1 gain. The RSFT improvement transfers consistently across datasets: on Re-DocRED~\citep{tan2022redocred}, RSFT achieves 41.45 Ign-F1 (+4.86pp over SFT baseline 36.59), closely matching the +4.92pp gain on DocRED. Evidence quality remains stable (Evi-F1 81.82 vs.\ 81.70 for SFT) with improved coupling (EDCR 0.6210 vs.\ 0.6674). Our best joint Evi-F1 (0.36, DREEAM-protocol denominator) falls below supervised DREEAM (54.01\%~\citep{ma2023dreeam}), a gap driven by extraction performance rather than evidence quality (TP-only Evi-F1 exceeds 80\%). Full results appear in Appendix~\ref{sec:generalization_full}.
127	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cefe4685-ca99-4d0a-8d88-e3c77ac2e86b",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "8dbe88c8-fd9c-416d-bb29-dc6811fbff6f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Dataset.}\nWe conduct experiments on DocRED~\\citep{yao2019docred}, a large-scale document-level relation extraction benchmark containing 3,053 training and 998 development documents spanning 96 relation types. Each document requires identifying relational triples across multiple sentences and grounding each triple with supporting evidence sentences. We use Re-DocRED~\\citep{tan2022redocred} for cross-dataset generalization evaluation.\n\n\\paragraph{Models.}\nOur primary model is Qwen3-4B. To study scale effects, we additionally train Qwen3-1.7B and Qwen3-8B under identical configurations. We include LLaMA-3.1-8B as a cross-family validation point.\n\n\\paragraph{Training.}\nAll models use LoRA~\\citep{hu2022lora} with rank $r{=}64$ and $\\alpha{=}128$ over a structured output format that jointly produces relation triples and evidence sentences. For RSFT, we sample $N{=}8$ candidate outputs per document and select the top-$k{=}1$ response ranked by CED scoring (\\S\\ref{sec:ced}), which combines NLI-based evidence faithfulness with extraction accuracy. GRPO experiments use group sizes $G{=}4$ (QLoRA, 4-bit) and $G{=}8$ (bf16 full-precision LoRA). DPO constructs preference pairs from CED-ranked outputs.\n\n\\paragraph{Metrics.}\nWe report five metrics. \\textbf{Ign-F1} is the primary DocRED metric that ignores triples appearing in the training set, matching the official leaderboard protocol. \\textbf{Rel-F1} measures relation extraction F1 on all triples. \\textbf{Evi-F1 (TP-only)} measures evidence sentence F1 conditioned on correctly predicted triples, reflecting evidence quality independent of extraction errors. \\textbf{Evi-F1 (joint)} includes false-positive and false-negative triples in the denominator following the DREEAM protocol~\\citep{ma2023dreeam}, enabling cross-method evidence comparison. \\textbf{EDCR} (Evidence-Decoupling Ratio) is our proposed diagnostic: the ratio of evidence recall on correctly-predicted triples to overall extraction recall, where values substantially exceeding the SFT baseline indicate RL-induced decoupling. All primary results use the development set; test set submission is pending.\n\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main} presents the primary comparison between SFT, no-evidence SFT, and RSFT CED on Qwen3-4B. The SFT baseline achieves 39.74 Ign-F1 with joint evidence generation. Removing evidence from the output format entirely (no-evidence SFT) improves extraction to 47.21 Ign-F1, a 7.47-point gap that quantifies the \\emph{evidence tax} at the 4B scale. RSFT CED achieves a four-seed mean of 44.66 Ign-F1 (+4.92 over SFT, standard deviation 0.49) while maintaining evidence quality (Evi-F1 81.15 vs.\\ 79.86 for SFT). The EDCR decreases from 0.6982 to 0.6503, confirming tighter coupling between extraction and evidence capabilities. Per-seed results appear in Appendix~\\ref{sec:ablation_full}.\n\nThe remaining gap to the no-evidence upper bound (2.09 points) represents the residual cost of producing structured evidence, a cost that shrinks at larger scales as we show in Section~\\ref{sec:scaling}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results on DocRED dev set (Qwen3-4B). RSFT reports four-seed mean $\\pm$ std. Best Ign-F1 in \\textbf{bold}; best among evidence-generating methods \\underline{underlined}. Per-seed breakdown in Appendix Table~\\ref{tab:ablation_full}.}\n\\label{tab:main}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Ign-F1} & \\textbf{Rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\nSFT baseline & 39.74 & 0.4049 & 79.86 & 0.6982 \\\\\nSFT no-evidence & \\textbf{47.21} & \\textbf{0.4876} & -- & -- \\\\\nRSFT CED & \\underline{44.66{\\scriptsize$\\pm$0.49}} & \\underline{0.4563} & 81.15 & 0.6503 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\n\\subsection{Evidence-Extraction Decoupling Spectrum}\n\\label{sec:spectrum}\n\nDifferent RL algorithms produce qualitatively different failure modes when applied to joint evidence-and-extraction generation. We organize these outcomes along a \\emph{decoupling spectrum} ranging from catastrophic collapse to mild perturbation, shown in Table~\\ref{tab:spectrum} (visualized in Figure~\\ref{fig:spectrum}, Appendix).\n\n\\paragraph{GRPO QLoRA: catastrophic collapse.}\nUnder QLoRA quantization ($G{=}4$), GRPO drives Rel-F1 to 0.0138 (near zero extraction) while Evi-F1 rises to 85.04 and EDCR reaches 0.9876. The model learns to produce well-formed evidence sentences but loses the ability to predict correct relation triples. This extreme decoupling occurs because 4-bit quantization constrains the effective parameter space, forcing the reward signal to optimize whichever sub-task yields easier gradient progress. Evidence sentence generation, being closer to extractive summarization, wins this competition.\n\n\\paragraph{GRPO bf16: mild, non-monotonic.}\nFull-precision GRPO ($G{=}8$) avoids catastrophe. Its training trajectory shows non-monotonic Rel-F1 fluctuation (0.434 at step 30, 0.428 at step 50, 0.434 at step 70, 0.455 at step 100), stabilizing near the SFT baseline. The best checkpoint achieves Rel-F1 0.4549 with Evi-F1 80.86 and EDCR 0.6318. The decoupling is mild: bf16 precision preserves enough capacity for both sub-tasks to improve jointly, though the non-monotonic trajectory suggests fragile optimization dynamics that require careful checkpoint selection.\n\n\\paragraph{DPO: gradual decay.}\nDPO preference learning shows a progressive pattern. At 1 epoch, Rel-F1 remains at 0.4034 with Evi-F1 80.88 and EDCR 0.7139. Extended training (3 epochs) degrades extraction to 0.3429 while evidence improves to 84.03\\footnote{DPO 3-epoch results use the pre-D076 evaluation protocol; included for trend analysis.}, with EDCR rising to 0.7294. Unlike GRPO's sudden collapse, DPO gradually trades extraction quality for evidence quality as training progresses.\n\n\\paragraph{RSFT: no decoupling.}\nRSFT avoids the decoupling problem entirely. By selecting high-quality complete outputs (jointly good extraction and evidence) rather than applying gradient-based reward maximization, RSFT maintains both capabilities simultaneously (mean Rel-F1 0.4563, Evi-F1 81.15, EDCR 0.6503). The key insight is that rejection sampling operates on discrete outputs rather than differentiable reward signals, so it cannot exploit the extraction-evidence trade-off that gradient methods find.\n\n\\begin{table}[t]\n\\centering\n\\caption{Evidence-extraction decoupling across RL paradigms (Qwen3-4B). Severity indicates the degree of extraction collapse relative to evidence improvement.}\n\\label{tab:spectrum}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Paradigm} & \\textbf{Config} & \\textbf{Rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} & \\textbf{Severity} \\\\\n\\midrule\nGRPO & QLoRA $G{=}4$ & 0.0138 & 85.04 & 0.9876 & Catastrophic \\\\\nGRPO & bf16 $G{=}8$ & 0.4549 & 80.86 & 0.6318 & Mild \\\\\nDPO & bf16 1ep & 0.4034 & 80.88 & 0.7139 & Gradual \\\\\nDPO & bf16 3ep$^\\dagger$ & 0.3429 & 84.03 & 0.7294 & Gradual \\\\\n\\midrule\nSFT & baseline & 0.4049 & 79.86 & 0.6982 & None \\\\\nRSFT & CED (mean) & 0.4563 & 81.15 & 0.6503 & None \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\vspace{-2mm}\n{\\raggedright\\footnotesize $^\\dagger$Pre-D076 evaluation protocol.\\par}\n\\end{table}\n\n\n\\subsection{Scale-Dependent Evidence Tax}\n\\label{sec:scaling}\n\nThe evidence tax, defined as the Ign-F1 difference between no-evidence and joint-evidence SFT, varies non-monotonically across model scales. Table~\\ref{tab:scaling} presents this analysis across four models (Figure~\\ref{fig:scaling} in Appendix).\n\nAt the 4B scale, the evidence tax is severe: $-7.47$ points. Generating evidence sentences alongside relation triples consumes capacity that would otherwise improve extraction. At 8B, the tax nearly vanishes ($-0.28$ points for Qwen3-8B, $-0.68$ for LLaMA-3.1-8B), indicating that 8B-class models have sufficient capacity to handle both tasks simultaneously. The most surprising result appears at 1.7B: instead of paying a larger tax, the smallest model \\emph{benefits} from evidence generation (+8.04 points). On a fair evaluation subset that controls for output format effects (see Appendix), this benefit is +6.2 points. We hypothesize that for small models, the evidence generation task provides implicit regularization, forcing the model to attend to supporting context rather than memorizing surface-level patterns.\n\nRSFT improves all scales. The gain is +2.64 for 1.7B, +4.92 for 4B, and +3.82 for 8B, confirming that CED-based selection generalizes across model capacities. The 4B model benefits most because it has the largest evidence tax to recover from. A striking consequence of this pattern is that 1.7B RSFT achieves 50.50 Ign-F1, nearly matching 8B SFT at 50.51. CED-based rejection sampling enables a 1.7B model to rival a 4.7$\\times$ larger model on evidence-grounded extraction, with direct implications for deployment cost: practitioners can substitute a small model with RSFT for a large model with vanilla SFT at comparable accuracy.\n\n\\begin{table}[t]\n\\centering\n\\caption{Scale-dependent evidence tax and RSFT gain. Evidence tax = SFT with evidence minus SFT no-evidence (positive means evidence helps). All results on DocRED dev set Ign-F1.}\n\\label{tab:scaling}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{SFT w/ evi} & \\textbf{No-evi} & \\textbf{RSFT} & \\textbf{Evi Tax} & \\textbf{RSFT Gain} \\\\\n\\midrule\nQwen3-1.7B & 47.86 & 39.82 & 50.50 & +8.04 & +2.64 \\\\\nQwen3-4B & 39.74 & 47.21 & 44.66 & $-$7.47 & +4.92 \\\\\nQwen3-8B & 50.51 & 50.79 & \\textbf{54.33} & $-$0.28 & +3.82 \\\\\nLLaMA-3.1-8B & 53.84 & 54.52 & 55.58 & $-$0.68 & +1.74 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\n\\subsection{Evidence Strategy Comparison}\n\\label{sec:evidence_strategy}\n\nWe compare joint generation against post-hoc retrieval, using Evi-F1 (joint) with the DREEAM-protocol denominator~\\citep{ma2023dreeam} for fair cross-strategy comparison. Post-hoc BM25 retrieval (entity-constrained, $k{=}2$ sentences per triple) achieves higher Rel-F1 (0.4876) by avoiding the evidence tax, but produces lower Evi-F1 (joint) of 0.347 with EDCR 0.766. RSFT CED (s43) reaches Evi-F1 (joint) 0.361 with EDCR 0.654, a 1.4-point evidence advantage and 0.112 EDCR reduction. CED reranking at inference time (selecting the best of $N{=}8$ outputs by CED score) achieves Rel-F1 0.4864 and Evi-F1 81.88 (TP-only), approaching no-evidence extraction quality while preserving evidence. Joint training produces more faithful evidence grounded in the extraction reasoning rather than retrieved post-hoc; inference-time reranking complements this by recovering extraction accuracy.\n\n\n\\subsection{Generalization}\n\\label{sec:generalization}\n\nCross-architecture validation on LLaMA-3.1-8B confirms the scaling patterns: the evidence tax at 8B is near zero ($-0.68$ points), and RSFT CED yields +1.74 Ign-F1 gain. The RSFT improvement transfers consistently across datasets: on Re-DocRED~\\citep{tan2022redocred}, RSFT achieves 41.45 Ign-F1 (+4.86pp over SFT baseline 36.59), closely matching the +4.92pp gain on DocRED. Evidence quality remains stable (Evi-F1 81.82 vs.\\ 81.70 for SFT) with improved coupling (EDCR 0.6210 vs.\\ 0.6674). Our best joint Evi-F1 (0.36, DREEAM-protocol denominator) falls below supervised DREEAM (54.01\\%~\\citep{ma2023dreeam}), a gap driven by extraction performance rather than evidence quality (TP-only Evi-F1 exceeds 80\\%). Full results appear in Appendix~\\ref{sec:generalization_full}.\n",
      "numLines": 127,
      "startLine": 1,
      "totalLines": 127
    }
  },
  "sourceToolAssistantUUID": "cefe4685-ca99-4d0a-8d88-e3c77ac2e86b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T06:48:51.769Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XGwEEvJRj6TxaC6xqTNhWF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dbe88c8-fd9c-416d-bb29-dc6811fbff6f",
  "isSidechain": false,
  "requestId": "req_011Cb9b3WYJAvj1CA56wvEuf",
  "type": "assistant",
  "uuid": "a39f003f-9516-4577-9eca-6adde6d13b95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175uQP8vQqP2vH4FRDuCkXq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 28056,
      "output_tokens": 756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 756,
          "cache_read_input_tokens": 28056,
          "cache_creation_input_tokens": 629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 629
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-18T06:48:51.780Z_

<details><summary>↩ Tool result · `toolu_01XGwEEvJRj6TxaC6xqTNhWF`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\paragraph{EDCR as a diagnostic.}
5	EDCR (\S\ref{sec:edcr}) correlates strongly with extraction quality at the method level: Spearman $\rho = -0.965$ between EDCR and Rel-F1 (Table~\ref{tab:spectrum}), with GRPO QLoRA at 0.9876, SFT at 0.6982, and RSFT at 0.6503. At the per-relation level, EDCR correlates with Rel-F1 ($\rho = -0.793$) but is independent of Evi-F1 ($\rho = -0.064$), confirming extraction-evidence decoupling across relation types (Appendix~\ref{sec:edcr_per_relation}). RSFT avoids decoupling because discrete output selection prevents trading extraction for evidence quality (Appendix~\ref{sec:rsft_theory}). We provide qualitative examples of these phenomena in Appendix~\ref{sec:qualitative}.
6	
7	\paragraph{CED granularity.}
8	CED operates effectively at the response level for both RSFT selection and inference-time reranking, but fails at sentence-level granularity: filtering individual evidence sentences by NLI score reduces Evi-F1 by 7.7pp (Recall $-$20pp), as it disrupts co-reference chains across evidence sentences. This suggests that evidence quality is a holistic response property rather than a per-sentence attribute.
9	
10	\paragraph{Ablation.}
11	CED and flat-NLI produce comparable performance (Rel-F1 0.4563 vs.\ 0.4561); stricter selection ($k{=}1$) outperforms $k{=}3$ by 1.02 Ign-F1 despite 2.96$\times$ fewer examples (Appendix~\ref{sec:ablation_full}).
12	
13	\paragraph{Practical implications.}
14	Our findings suggest three guidelines for practitioners seeking evidence-grounded IE: (1) avoid online RL for multi-objective generation tasks where capability coupling matters; (2) prefer RSFT with strict selection ($k{=}1$) over training data quantity; (3) consider CED reranking at inference for deployment scenarios requiring both high extraction accuracy and evidence quality.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a39f003f-9516-4577-9eca-6adde6d13b95",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "4b54b95d-fb2b-41fe-b1ad-5098e55e7c2f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex",
      "content": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{EDCR as a diagnostic.}\nEDCR (\\S\\ref{sec:edcr}) correlates strongly with extraction quality at the method level: Spearman $\\rho = -0.965$ between EDCR and Rel-F1 (Table~\\ref{tab:spectrum}), with GRPO QLoRA at 0.9876, SFT at 0.6982, and RSFT at 0.6503. At the per-relation level, EDCR correlates with Rel-F1 ($\\rho = -0.793$) but is independent of Evi-F1 ($\\rho = -0.064$), confirming extraction-evidence decoupling across relation types (Appendix~\\ref{sec:edcr_per_relation}). RSFT avoids decoupling because discrete output selection prevents trading extraction for evidence quality (Appendix~\\ref{sec:rsft_theory}). We provide qualitative examples of these phenomena in Appendix~\\ref{sec:qualitative}.\n\n\\paragraph{CED granularity.}\nCED operates effectively at the response level for both RSFT selection and inference-time reranking, but fails at sentence-level granularity: filtering individual evidence sentences by NLI score reduces Evi-F1 by 7.7pp (Recall $-$20pp), as it disrupts co-reference chains across evidence sentences. This suggests that evidence quality is a holistic response property rather than a per-sentence attribute.\n\n\\paragraph{Ablation.}\nCED and flat-NLI produce comparable performance (Rel-F1 0.4563 vs.\\ 0.4561); stricter selection ($k{=}1$) outperforms $k{=}3$ by 1.02 Ign-F1 despite 2.96$\\times$ fewer examples (Appendix~\\ref{sec:ablation_full}).\n\n\\paragraph{Practical implications.}\nOur findings suggest three guidelines for practitioners seeking evidence-grounded IE: (1) avoid online RL for multi-objective generation tasks where capability coupling matters; (2) prefer RSFT with strict selection ($k{=}1$) over training data quantity; (3) consider CED reranking at inference for deployment scenarios requiring both high extraction accuracy and evidence quality.\n",
      "numLines": 15,
      "startLine": 1,
      "totalLines": 15
    }
  },
  "sourceToolAssistantUUID": "a39f003f-9516-4577-9eca-6adde6d13b95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T06:48:52.211Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TxguBJoRqfAgV8fFA9FD4U`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b54b95d-fb2b-41fe-b1ad-5098e55e7c2f",
  "isSidechain": false,
  "requestId": "req_011Cb9b3WYJAvj1CA56wvEuf",
  "type": "assistant",
  "uuid": "a59da9e4-a7c4-4e68-b11d-ebdb82d9e5bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175uQP8vQqP2vH4FRDuCkXq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 28056,
      "output_tokens": 756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 756,
          "cache_read_input_tokens": 28056,
          "cache_creation_input_tokens": 629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 629
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-18T06:48:52.217Z_

<details><summary>↩ Tool result · `toolu_01TxguBJoRqfAgV8fFA9FD4U`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We formalize evidence-grounded document-level relation extraction as a structured generation task for LLMs and compare three post-training paradigms across 85+ configurations. RL optimization pressure correlates with evidence-extraction decoupling severity (GRPO catastrophic, DPO gradual, RSFT none; EDCR $\rho = -0.965$), and the cost of joint evidence production follows a non-monotonic pattern across scales (+8pp at 1.7B, $-$7.5pp at 4B, near zero at 8B). RSFT with CED scoring yields +4.92pp Ign-F1 at 4B (four-seed mean); our 1.7B RSFT model (50.50 Ign-F1) matches 8B SFT (50.51) at a fraction of the cost.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a59da9e4-a7c4-4e68-b11d-ebdb82d9e5bb",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "571f91e9-2241-4757-b0c9-2fb59e31e22a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe formalize evidence-grounded document-level relation extraction as a structured generation task for LLMs and compare three post-training paradigms across 85+ configurations. RL optimization pressure correlates with evidence-extraction decoupling severity (GRPO catastrophic, DPO gradual, RSFT none; EDCR $\\rho = -0.965$), and the cost of joint evidence production follows a non-monotonic pattern across scales (+8pp at 1.7B, $-$7.5pp at 4B, near zero at 8B). RSFT with CED scoring yields +4.92pp Ign-F1 at 4B (four-seed mean); our 1.7B RSFT model (50.50 Ign-F1) matches 8B SFT (50.51) at a fraction of the cost.\n",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 5
    }
  },
  "sourceToolAssistantUUID": "a59da9e4-a7c4-4e68-b11d-ebdb82d9e5bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T06:48:53.156Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WQVLfj3Zv7QGzLwLuu9VDm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "571f91e9-2241-4757-b0c9-2fb59e31e22a",
  "isSidechain": false,
  "requestId": "req_011Cb9b3WYJAvj1CA56wvEuf",
  "type": "assistant",
  "uuid": "64b781b0-9838-401b-9758-529533e3559a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175uQP8vQqP2vH4FRDuCkXq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 28056,
      "output_tokens": 756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 756,
          "cache_read_input_tokens": 28056,
          "cache_creation_input_tokens": 629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 629
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-18T06:48:53.162Z_

<details><summary>↩ Tool result · `toolu_01WQVLfj3Zv7QGzLwLuu9VDm`</summary>

```text
1	\section{Limitations}
2	
3	All results use the DocRED development set; test set submission is pending. Exact-match F1 penalizes surface-form-different entity mentions~\citep{wan2024genres}, likely underestimating absolute extraction capability, though relative comparisons remain valid.
4	
5	We evaluate one algorithm per RL family (GRPO, DPO); other algorithms may yield different results. CED scoring depends on an external NLI model, and the RSFT ablation uses limited seeds (four for CED, two for flat-NLI). The evidence tax pattern observed up to 8B may not extrapolate to larger scales. At 1.7B scale, 44.4\% of outputs exhibit repetitive patterns (vs.\ negligible at 4B+); small models may require decoding-time interventions (e.g., repetition penalty) for reliable deployment.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64b781b0-9838-401b-9758-529533e3559a",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "50d7ab4b-22b4-493e-a0d4-581e4c387b13",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex",
      "content": "\\section{Limitations}\n\nAll results use the DocRED development set; test set submission is pending. Exact-match F1 penalizes surface-form-different entity mentions~\\citep{wan2024genres}, likely underestimating absolute extraction capability, though relative comparisons remain valid.\n\nWe evaluate one algorithm per RL family (GRPO, DPO); other algorithms may yield different results. CED scoring depends on an external NLI model, and the RSFT ablation uses limited seeds (four for CED, two for flat-NLI). The evidence tax pattern observed up to 8B may not extrapolate to larger scales. At 1.7B scale, 44.4\\% of outputs exhibit repetitive patterns (vs.\\ negligible at 4B+); small models may require decoding-time interventions (e.g., repetition penalty) for reliable deployment.\n",
      "numLines": 6,
      "startLine": 1,
      "totalLines": 6
    }
  },
  "sourceToolAssistantUUID": "64b781b0-9838-401b-9758-529533e3559a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T06:48:53.629Z_

<details open><summary>🔧 Tool call — Read · `toolu_012H7YbDTQnh7LauwDqaHqRK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50d7ab4b-22b4-493e-a0d4-581e4c387b13",
  "isSidechain": false,
  "requestId": "req_011Cb9b3WYJAvj1CA56wvEuf",
  "type": "assistant",
  "uuid": "b4a87065-545a-40f7-96f6-852ca512f9b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175uQP8vQqP2vH4FRDuCkXq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 28056,
      "output_tokens": 756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 756,
          "cache_read_input_tokens": 28056,
          "cache_creation_input_tokens": 629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 629
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-18T06:48:53.635Z_

<details><summary>↩ Tool result · `toolu_012H7YbDTQnh7LauwDqaHqRK`</summary>

```text
1	\section{Training Hyperparameters}
2	\label{sec:hyperparams}
3	
4	Table~\ref{tab:hyperparams} lists the hyperparameters for all training configurations. All methods use LoRA with rank $r{=}64$ and $\alpha{=}128$ applied to attention projections. SFT and RSFT share the same optimizer settings; RSFT differs only in data construction (top-1 CED-selected outputs from $N{=}8$ candidates). GRPO and DPO use lower learning rates to stabilize post-SFT optimization.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Training hyperparameters for all optimization paradigms. All experiments use Qwen3-4B as the base model with LoRA adaptation. A dash indicates that the parameter is not applicable to the given method.}
9	\label{tab:hyperparams}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	\textbf{Parameter} & \textbf{SFT} & \textbf{RSFT} & \textbf{GRPO QLoRA} & \textbf{GRPO bf16} & \textbf{DPO} \\
14	\midrule
15	Base model & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B \\
16	LoRA rank $r$ & 64 & 64 & 64 & 64 & 64 \\
17	LoRA $\alpha$ & 128 & 128 & 128 & 128 & 128 \\
18	Learning rate & 2e-5 & 2e-5 & 5e-6 & 5e-6 & 5e-7 \\
19	Batch size (effective) & 16 & 16 & 4 & 8 & 4 \\
20	Epochs & 3 & 3 & -- & -- & 1, 3\textsuperscript{$\star$} \\
21	Max steps & -- & -- & 100 & 100 & -- \\
22	Gradient accumulation & 4 & 4 & 16 & 4 & 4 \\
23	Max new tokens & 1024 & 1024 & 1024 & 1024 & 1024 \\
24	Quantization & -- & -- & NF4 4-bit & bf16 & bf16 \\
25	Group size $G$ & -- & -- & 4 & 8 & -- \\
26	KL coefficient & -- & -- & 0.01 & 0.01 & -- \\
27	$\beta$ (DPO) & -- & -- & -- & -- & 0.1 \\
28	Candidates $N$ & -- & 8 & -- & -- & 8 \\
29	Top-$k$ selection & -- & 1 & -- & -- & -- \\
30	Training samples & 3,053 & 2,718 & 3,053 & 3,053 & 3,053 \\
31	Scoring function & -- & CED & CED & CED & CED \\
32	\bottomrule
33	\end{tabular}
34	\vspace{1mm}
35	{\raggedright\footnotesize \textsuperscript{$\star$}DPO is trained for both 1 and 3 epochs to observe temporal dynamics of the evidence-extraction trade-off (Section~\ref{sec:spectrum}).\par}
36	\end{table*}
37	
38	
39	\section{Full Ablation Results}
40	\label{sec:ablation_full}
41	
42	Table~\ref{tab:ablation_full} reports the complete RSFT ablation across scoring functions, top-$k$ values, and random seeds. RSFT CED $k{=}1$ achieves a mean Ign-F1 of 44.66 with low variance across four seeds (standard deviation 0.49), confirming the robustness of the improvement over the SFT baseline (39.74). Increasing $k$ to 3 slightly degrades performance (43.64 Ign-F1), consistent with the intuition that stricter selection yields higher-quality training data. The flat-NLI scoring variant produces comparable Rel-F1 (mean 0.4561 vs.\ 0.4563 for CED, a difference of 0.02pp). Both CED and flat-NLI improve substantially over the SFT baseline while maintaining or improving Evi-F1, confirming that the RSFT gains are driven by quality-based data selection rather than by the specific contrastive formulation.
43	
44	\paragraph{NLI scoring comparison.} Across all available seeds, CED RSFT achieves mean Rel-F1 of 0.4563 (seeds 42, 43, 44, 45: range 0.4514--0.4621), and flat-NLI RSFT achieves mean Rel-F1 of 0.4561 (seeds 42, 43: range 0.4535--0.4586). The 0.02pp difference suggests comparable performance: CED's contrastive design does not substantially outperform simpler NLI scoring for RSFT data selection. We adopt CED as the default because its contrastive formulation produces per-triple discrimination scores that support interpretable error analysis.
45	
46	\paragraph{Top-$k$ selection.} Best-of-8 ($k{=}1$) yields mean Ign-F1 44.66 and Rel-F1 0.4563, while top-3-of-8 ($k{=}3$) produces 43.64 and 0.4454. The selected training data confirms the quality gap: $k{=}1$ data has mean extraction F1 of 0.6157 and mean CED of 0.6683, versus 0.5761 and 0.6205 for $k{=}3$. Despite $k{=}3$ providing 2.96$\times$ more training examples, the additional lower-ranked samples introduce noise that degrades final performance.
47	
48	\begin{table}[t]
49	\centering
50	\caption{Full RSFT ablation on DocRED dev set (Qwen3-4B). CED and flat-NLI denote the scoring function used for candidate selection. Best Ign-F1 among evidence-generating methods in \textbf{bold}.}
51	\label{tab:ablation_full}
52	\small
53	\resizebox{\columnwidth}{!}{%
54	\begin{tabular}{lcccc}
55	\toprule
56	\textbf{Configuration} & \textbf{Ign-F1} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
57	\midrule
58	SFT baseline & 39.74 & 0.4049 & 79.86 & 0.6982 \\
59	SFT no-evidence & \textbf{47.21} & 0.4876 & -- & -- \\
60	\midrule
61	RSFT CED $k{=}1$ (s42) & 44.23 & 0.4517 & 81.74 & 0.6569 \\
62	RSFT CED $k{=}1$ (s43) & 45.12 & 0.4601 & 80.63 & 0.6542 \\
63	RSFT CED $k{=}1$ (s44) & 45.11 & 0.4621 & 80.50 & 0.6350 \\
64	RSFT CED $k{=}1$ (s45) & 44.16 & 0.4514 & 81.74 & 0.6550 \\
65	RSFT CED $k{=}1$ (mean) & 44.66 & 0.4563 & 81.15 & 0.6503 \\
66	\midrule
67	RSFT CED $k{=}3$ & 43.64 & 0.4454 & 80.88 & 0.6635 \\
68	\midrule
69	RSFT flat-NLI (s42) & -- & 0.4535 & 80.43 & 0.6431 \\
70	RSFT flat-NLI (s43) & -- & 0.4586 & 81.58 & 0.6505 \\
71	RSFT flat-NLI (mean) & -- & 0.4561 & 81.01 & 0.6468 \\
72	\bottomrule
73	\end{tabular}%
74	}
75	\end{table}
76	
77	
78	\section{Scaling Details}
79	\label{sec:scaling_details}
80	
81	Table~\ref{tab:cross_detail} supplements Table~\ref{tab:scaling} in the main text with per-scale Rel-F1 and Evi-F1 breakdowns. At 1.7B, RSFT improves Rel-F1 from 0.4945 to 0.5219 (+0.0274) while achieving Evi-F1 83.09 and EDCR 0.6297. The 4B model shows the same pattern at a larger magnitude: Rel-F1 increases from 0.4049 to 0.4563 (+0.0514, four-seed mean). For 8B, RSFT brings Rel-F1 from 0.5262 to 0.5606 with Evi-F1 of 80.52 and EDCR 0.6377, confirming tight coupling between extraction and evidence at this scale.
82	
83	\begin{table}[t]
84	\centering
85	\caption{Detailed Rel-F1 and Evi-F1 across model scales on DocRED dev set. SFT columns show the joint-evidence baseline; RSFT columns show CED $k{=}1$ four-seed mean for 4B, single seed for other scales.}
86	\label{tab:cross_detail}
87	\small
88	\resizebox{\columnwidth}{!}{%
89	\begin{tabular}{lccccc}
90	\toprule
91	\textbf{Model} & \textbf{SFT Rel-F1} & \textbf{SFT Evi-F1} & \textbf{RSFT Rel-F1} & \textbf{RSFT Evi-F1} & \textbf{RSFT EDCR} \\
92	\midrule
93	Qwen3-1.7B & 0.4945 & 83.16 & 0.5219 & 83.09 & 0.6297 \\
94	Qwen3-4B & 0.4049 & 79.86 & 0.4563 & 81.15 & 0.6503 \\
95	Qwen3-8B & 0.5262 & 81.88 & 0.5606 & 80.52 & 0.6377 \\
96	LLaMA-3.1-8B & 0.5514 & 81.51 & 0.5674 & 82.14 & 0.6128 \\
97	\bottomrule
98	\end{tabular}%
99	}
100	\end{table}
101	
102	
103	\section{Why RSFT Avoids Decoupling}
104	\label{sec:rsft_theory}
105	
106	The structural difference between selection and optimization explains why RSFT does not exhibit the decoupling observed in gradient-based methods. GRPO and DPO update model parameters through gradients that optimize a reward signal. When two sub-tasks (extraction and evidence) compete for gradient capacity, the optimizer can discover and exploit the trade-off between them, improving one at the expense of the other. RSFT operates differently: it selects complete outputs and trains on them with standard supervised loss. Because the selection is discrete (accept or reject a full response), there is no gradient pathway through which the model can learn to sacrifice extraction for evidence quality. Only outputs where both extraction and evidence are jointly strong survive the CED filter. This property is not specific to RSFT's design but is a structural consequence of discrete selection over complete outputs: any selection-based method that filters on a joint quality criterion will inherit the same coupling guarantee. The implication for practitioners is direct: when optimizing for multiple coupled generation objectives, selection-based methods preserve inter-objective balance that gradient-based methods disrupt.
107	
108	
109	\section{Decoupling Spectrum Visualization}
110	\label{sec:spectrum_viz}
111	
112	\begin{figure}[t]
113	\centering
114	\includegraphics[width=\columnwidth]{fig_spectrum.pdf}
115	\caption{Decoupling spectrum visualization. Each method is plotted by Rel-F1 (x-axis) and Evi-F1 (y-axis). Arrows indicate training progression for DPO (1ep$\to$3ep) and GRPO bf16 trajectory. Ideal methods occupy the upper-right quadrant; decoupled methods drift toward the upper-left.}
116	\label{fig:spectrum}
117	\end{figure}
118	
119	
120	\section{Evidence Tax Visualization}
121	\label{sec:scaling_viz}
122	
123	\begin{figure}[t]
124	\centering
125	\includegraphics[width=\columnwidth]{fig_scaling.pdf}
126	\caption{Evidence tax across model scales. Bar heights show Ign-F1 for each training configuration. The gap between no-evidence and SFT bars reverses direction between 1.7B and 4B, revealing the non-monotonic nature of the evidence tax. RSFT consistently narrows the gap toward the no-evidence upper bound.}
127	\label{fig:scaling}
128	\end{figure}
129	
130	
131	\section{Full Generalization Results}
132	\label{sec:generalization_full}
133	
134	\paragraph{Cross-family transfer.}
135	LLaMA-3.1-8B confirms the scaling patterns observed with Qwen3. Its SFT baseline achieves 53.84 Ign-F1 (Rel-F1 0.5514, Evi-F1 81.51), and the no-evidence variant reaches 54.52 Ign-F1 (Rel-F1 0.5624). The evidence tax of $-0.68$ points mirrors the near-zero tax seen for Qwen3-8B ($-0.28$), supporting our claim that 8B-class models absorb the cost of joint evidence generation regardless of architecture family. RSFT CED improves LLaMA to 55.58 Ign-F1 (Rel-F1 0.5674, Evi-F1 82.14, EDCR 0.6128), a +1.74 point gain consistent with the pattern at the 8B scale (Qwen3-8B: +3.82). A second seed (s43: 56.19 Ign-F1, EDCR 0.6073) confirms robustness.
136	
137	\paragraph{Cross-dataset robustness.}
138	On Re-DocRED~\citep{tan2022redocred}, the SFT baseline achieves 36.59 Ign-F1 (Evi-F1 81.70, EDCR 0.6674). RSFT CED improves this to 41.45 Ign-F1 (Evi-F1 81.82, EDCR 0.6210), a +4.86pp gain that closely matches the +4.92pp improvement on DocRED. This consistency across datasets with different annotation protocols confirms that RSFT's benefit generalizes beyond training-set-specific artifacts. Evidence quality remains stable across datasets (Evi-F1 81.82 vs.\ 81.15 on DocRED), and the EDCR reduction ($-0.046$) mirrors the DocRED pattern, further supporting the robustness of CED-based selection.
139	
140	\paragraph{Comparison to supervised methods.}
141	Our best joint Evi-F1 of approximately 0.36 (using the DREEAM-protocol denominator) falls below the supervised DREEAM result of 54.01\%~\citep{ma2023dreeam}. This gap stems primarily from extraction performance rather than evidence quality: our TP-only Evi-F1 exceeds 80\%, indicating that when the model correctly identifies a triple, it produces high-quality evidence. The overall joint Evi-F1 is diluted by false-positive and false-negative triples in the denominator. Closing this gap requires improving the base extraction capability of LLM-based methods, an orthogonal direction to the evidence faithfulness problem we address. Our contribution is demonstrating that LLMs can generate grounded evidence jointly with extraction, and that RSFT maintains this capability under optimization pressure where RL methods fail.
142	
143	
144	\section{GRPO Training Dynamics}
145	\label{sec:grpo_dynamics}
146	
147	\begin{figure*}[t]
148	\centering
149	\includegraphics[width=\linewidth]{fig_grpo_dynamics.pdf}
150	\caption{Training dynamics of GRPO under different configurations. (a)~Relation F1 across checkpoints: G=4 QLoRA suffers catastrophic collapse at step~10, while G=8 bf16 remains stable. (b)~Evidence F1 stays intact for G=8 bf16, confirming the generation mechanism itself does not fail. (c)~Evidence-Decoupling Ratio (EDCR) reveals near-total decoupling in G=4 QLoRA (extraction collapses to Rel-F1 0.014), while G=8 bf16 maintains healthy ratios.}
151	\label{fig:grpo_dynamics}
152	\end{figure*}
153	
154	
155	\section{Per-Relation EDCR Distribution}
156	\label{sec:edcr_per_relation}
157	
158	Computing EDCR for each of the 76 relation types with $\geq$5 evaluation samples reveals that per-relation EDCR correlates strongly with per-relation Rel-F1 ($\rho = -0.793$, $p < 0.001$), confirming its utility as a difficulty indicator. However, per-relation EDCR is statistically independent of Evi-F1 ($\rho = -0.064$, $p = 0.58$), and Evi-F1 itself shows no association with Rel-F1 ($\rho = -0.013$, $p = 0.91$). These null correlations establish that evidence quality and extraction ability are fully decoupled across relation types. Extreme cases illustrate the diagnostic power: \texttt{date\_of\_birth} has EDCR $= 0.118$ (highly faithful, with extraction and evidence tightly coupled), while \texttt{head\_of\_government} reaches $0.956$ (highly decoupled). Method-level EDCR serves as a horizontal comparison tool across optimization paradigms, while per-relation EDCR enables vertical diagnosis of which relation types suffer from extraction-evidence misalignment.
159	
160	\begin{figure}[t]
161	\centering
162	\includegraphics[width=\linewidth]{fig_edcr_relations.pdf}
163	\caption{Per-relation EDCR distribution across 93 relation types. Red bars indicate relations with EDCR $\geq$ 0.70 (severe decoupling), green bars indicate EDCR $<$ 0.30 (healthy evidence grounding). Seven relation types exhibit EDCR = 1.0, indicating complete evidence decoupling.}
164	\label{fig:edcr_relations}
165	\end{figure}
166	
167	
168	\section{Qualitative Analysis}
169	\label{sec:qualitative}
170	
171	We present representative examples illustrating three phenomena: evidence quality differences between SFT and RSFT, GRPO format gaming under catastrophic collapse, and per-relation EDCR diagnostics.
172	
173	\paragraph{Case 1: Evidence quality.}
174	Table~\ref{tab:case_evidence} compares evidence citations from SFT and RSFT on three documents. SFT tends to cite many sentences indiscriminately, including distractors unrelated to the target triple, while RSFT selects precisely the gold evidence sentences. For \emph{America's Sweetheart}, SFT cites 6 sentences (precision 0.17) whereas RSFT cites only the single correct sentence (precision 1.00). The pattern is consistent: SFT achieves evidence precision of 0.00--0.20 across these examples, while RSFT achieves 1.00 in all three cases.
175	
176	\begin{table}[t]
177	\centering
178	\caption{Evidence citation comparison between SFT and RSFT. Precision measures the fraction of cited sentences that match gold evidence.}
179	\label{tab:case_evidence}
180	\small
181	\resizebox{\columnwidth}{!}{%
182	\begin{tabular}{llccc}
183	\toprule
184	\textbf{Document} & \textbf{Triple} & \textbf{SFT Prec.} & \textbf{RSFT Prec.} & \textbf{SFT \#Cited} \\
185	\midrule
186	Oleg Tinkov & (Oleg Tinkov, country of citizenship, Russia) & 0.00 & 1.00 & 3 \\
187	America's Sweetheart & (record label, country, United States) & 0.17 & 1.00 & 6 \\
188	Jade (Mortal Kombat) & (Jade, present in work, Mortal Kombat) & 0.20 & 1.00 & 5 \\
189	\bottomrule
190	\end{tabular}%
191	}
192	\end{table}
193	
194	\paragraph{Case 2: GRPO format gaming.}
195	Under catastrophic collapse (GRPO QLoRA $G{=}4$), the model abandons the DocRED 96-type relation ontology and generates free-text relation labels. On the document \emph{Something to Believe In}, the model produces 35 predicted triples with relations such as ``is a'', ``honor'', and ``location'', none of which belong to the target ontology. All 35 predictions are incorrect. Similarly, for \emph{J\'{o}zef Pi\l{}sudski Monument}, 28 predictions use non-standard relations with 0 correct matches. The model retains the structural format of triple-with-evidence output but fills it with fabricated relation types. The model produces well-formed evidence for these non-existent relations.
196	
197	\paragraph{Case 3: EDCR diagnostics.}
198	Per-relation EDCR identifies specific relation types where extraction and evidence are misaligned. For \texttt{date\_of\_birth} (EDCR $= 0.118$), the model's evidence consistently matches gold annotations: both extraction and evidence point to the same biographical sentence. In contrast, \texttt{notable\_work} (EDCR $= 0.941$) exhibits severe decoupling: the model cites sentence [0] (a general introduction) instead of the gold evidence sentence [3] (which contains the actual work attribution). High-EDCR relations tend to involve indirect or multi-hop reasoning where surface-level context misleads the evidence generator.
199	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4a87065-545a-40f7-96f6-852ca512f9b5",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "9697fa61-6fe4-451a-9af4-95928d73d8a0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Training Hyperparameters}\n\\label{sec:hyperparams}\n\nTable~\\ref{tab:hyperparams} lists the hyperparameters for all training configurations. All methods use LoRA with rank $r{=}64$ and $\\alpha{=}128$ applied to attention projections. SFT and RSFT share the same optimizer settings; RSFT differs only in data construction (top-1 CED-selected outputs from $N{=}8$ candidates). GRPO and DPO use lower learning rates to stabilize post-SFT optimization.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Training hyperparameters for all optimization paradigms. All experiments use Qwen3-4B as the base model with LoRA adaptation. A dash indicates that the parameter is not applicable to the given method.}\n\\label{tab:hyperparams}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Parameter} & \\textbf{SFT} & \\textbf{RSFT} & \\textbf{GRPO QLoRA} & \\textbf{GRPO bf16} & \\textbf{DPO} \\\\\n\\midrule\nBase model & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B \\\\\nLoRA rank $r$ & 64 & 64 & 64 & 64 & 64 \\\\\nLoRA $\\alpha$ & 128 & 128 & 128 & 128 & 128 \\\\\nLearning rate & 2e-5 & 2e-5 & 5e-6 & 5e-6 & 5e-7 \\\\\nBatch size (effective) & 16 & 16 & 4 & 8 & 4 \\\\\nEpochs & 3 & 3 & -- & -- & 1, 3\\textsuperscript{$\\star$} \\\\\nMax steps & -- & -- & 100 & 100 & -- \\\\\nGradient accumulation & 4 & 4 & 16 & 4 & 4 \\\\\nMax new tokens & 1024 & 1024 & 1024 & 1024 & 1024 \\\\\nQuantization & -- & -- & NF4 4-bit & bf16 & bf16 \\\\\nGroup size $G$ & -- & -- & 4 & 8 & -- \\\\\nKL coefficient & -- & -- & 0.01 & 0.01 & -- \\\\\n$\\beta$ (DPO) & -- & -- & -- & -- & 0.1 \\\\\nCandidates $N$ & -- & 8 & -- & -- & 8 \\\\\nTop-$k$ selection & -- & 1 & -- & -- & -- \\\\\nTraining samples & 3,053 & 2,718 & 3,053 & 3,053 & 3,053 \\\\\nScoring function & -- & CED & CED & CED & CED \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1mm}\n{\\raggedright\\footnotesize \\textsuperscript{$\\star$}DPO is trained for both 1 and 3 epochs to observe temporal dynamics of the evidence-extraction trade-off (Section~\\ref{sec:spectrum}).\\par}\n\\end{table*}\n\n\n\\section{Full Ablation Results}\n\\label{sec:ablation_full}\n\nTable~\\ref{tab:ablation_full} reports the complete RSFT ablation across scoring functions, top-$k$ values, and random seeds. RSFT CED $k{=}1$ achieves a mean Ign-F1 of 44.66 with low variance across four seeds (standard deviation 0.49), confirming the robustness of the improvement over the SFT baseline (39.74). Increasing $k$ to 3 slightly degrades performance (43.64 Ign-F1), consistent with the intuition that stricter selection yields higher-quality training data. The flat-NLI scoring variant produces comparable Rel-F1 (mean 0.4561 vs.\\ 0.4563 for CED, a difference of 0.02pp). Both CED and flat-NLI improve substantially over the SFT baseline while maintaining or improving Evi-F1, confirming that the RSFT gains are driven by quality-based data selection rather than by the specific contrastive formulation.\n\n\\paragraph{NLI scoring comparison.} Across all available seeds, CED RSFT achieves mean Rel-F1 of 0.4563 (seeds 42, 43, 44, 45: range 0.4514--0.4621), and flat-NLI RSFT achieves mean Rel-F1 of 0.4561 (seeds 42, 43: range 0.4535--0.4586). The 0.02pp difference suggests comparable performance: CED's contrastive design does not substantially outperform simpler NLI scoring for RSFT data selection. We adopt CED as the default because its contrastive formulation produces per-triple discrimination scores that support interpretable error analysis.\n\n\\paragraph{Top-$k$ selection.} Best-of-8 ($k{=}1$) yields mean Ign-F1 44.66 and Rel-F1 0.4563, while top-3-of-8 ($k{=}3$) produces 43.64 and 0.4454. The selected training data confirms the quality gap: $k{=}1$ data has mean extraction F1 of 0.6157 and mean CED of 0.6683, versus 0.5761 and 0.6205 for $k{=}3$. Despite $k{=}3$ providing 2.96$\\times$ more training examples, the additional lower-ranked samples introduce noise that degrades final performance.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full RSFT ablation on DocRED dev set (Qwen3-4B). CED and flat-NLI denote the scoring function used for candidate selection. Best Ign-F1 among evidence-generating methods in \\textbf{bold}.}\n\\label{tab:ablation_full}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Configuration} & \\textbf{Ign-F1} & \\textbf{Rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\nSFT baseline & 39.74 & 0.4049 & 79.86 & 0.6982 \\\\\nSFT no-evidence & \\textbf{47.21} & 0.4876 & -- & -- \\\\\n\\midrule\nRSFT CED $k{=}1$ (s42) & 44.23 & 0.4517 & 81.74 & 0.6569 \\\\\nRSFT CED $k{=}1$ (s43) & 45.12 & 0.4601 & 80.63 & 0.6542 \\\\\nRSFT CED $k{=}1$ (s44) & 45.11 & 0.4621 & 80.50 & 0.6350 \\\\\nRSFT CED $k{=}1$ (s45) & 44.16 & 0.4514 & 81.74 & 0.6550 \\\\\nRSFT CED $k{=}1$ (mean) & 44.66 & 0.4563 & 81.15 & 0.6503 \\\\\n\\midrule\nRSFT CED $k{=}3$ & 43.64 & 0.4454 & 80.88 & 0.6635 \\\\\n\\midrule\nRSFT flat-NLI (s42) & -- & 0.4535 & 80.43 & 0.6431 \\\\\nRSFT flat-NLI (s43) & -- & 0.4586 & 81.58 & 0.6505 \\\\\nRSFT flat-NLI (mean) & -- & 0.4561 & 81.01 & 0.6468 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\n\\section{Scaling Details}\n\\label{sec:scaling_details}\n\nTable~\\ref{tab:cross_detail} supplements Table~\\ref{tab:scaling} in the main text with per-scale Rel-F1 and Evi-F1 breakdowns. At 1.7B, RSFT improves Rel-F1 from 0.4945 to 0.5219 (+0.0274) while achieving Evi-F1 83.09 and EDCR 0.6297. The 4B model shows the same pattern at a larger magnitude: Rel-F1 increases from 0.4049 to 0.4563 (+0.0514, four-seed mean). For 8B, RSFT brings Rel-F1 from 0.5262 to 0.5606 with Evi-F1 of 80.52 and EDCR 0.6377, confirming tight coupling between extraction and evidence at this scale.\n\n\\begin{table}[t]\n\\centering\n\\caption{Detailed Rel-F1 and Evi-F1 across model scales on DocRED dev set. SFT columns show the joint-evidence baseline; RSFT columns show CED $k{=}1$ four-seed mean for 4B, single seed for other scales.}\n\\label{tab:cross_detail}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{SFT Rel-F1} & \\textbf{SFT Evi-F1} & \\textbf{RSFT Rel-F1} & \\textbf{RSFT Evi-F1} & \\textbf{RSFT EDCR} \\\\\n\\midrule\nQwen3-1.7B & 0.4945 & 83.16 & 0.5219 & 83.09 & 0.6297 \\\\\nQwen3-4B & 0.4049 & 79.86 & 0.4563 & 81.15 & 0.6503 \\\\\nQwen3-8B & 0.5262 & 81.88 & 0.5606 & 80.52 & 0.6377 \\\\\nLLaMA-3.1-8B & 0.5514 & 81.51 & 0.5674 & 82.14 & 0.6128 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\n\\section{Why RSFT Avoids Decoupling}\n\\label{sec:rsft_theory}\n\nThe structural difference between selection and optimization explains why RSFT does not exhibit the decoupling observed in gradient-based methods. GRPO and DPO update model parameters through gradients that optimize a reward signal. When two sub-tasks (extraction and evidence) compete for gradient capacity, the optimizer can discover and exploit the trade-off between them, improving one at the expense of the other. RSFT operates differently: it selects complete outputs and trains on them with standard supervised loss. Because the selection is discrete (accept or reject a full response), there is no gradient pathway through which the model can learn to sacrifice extraction for evidence quality. Only outputs where both extraction and evidence are jointly strong survive the CED filter. This property is not specific to RSFT's design but is a structural consequence of discrete selection over complete outputs: any selection-based method that filters on a joint quality criterion will inherit the same coupling guarantee. The implication for practitioners is direct: when optimizing for multiple coupled generation objectives, selection-based methods preserve inter-objective balance that gradient-based methods disrupt.\n\n\n\\section{Decoupling Spectrum Visualization}\n\\label{sec:spectrum_viz}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_spectrum.pdf}\n\\caption{Decoupling spectrum visualization. Each method is plotted by Rel-F1 (x-axis) and Evi-F1 (y-axis). Arrows indicate training progression for DPO (1ep$\\to$3ep) and GRPO bf16 trajectory. Ideal methods occupy the upper-right quadrant; decoupled methods drift toward the upper-left.}\n\\label{fig:spectrum}\n\\end{figure}\n\n\n\\section{Evidence Tax Visualization}\n\\label{sec:scaling_viz}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_scaling.pdf}\n\\caption{Evidence tax across model scales. Bar heights show Ign-F1 for each training configuration. The gap between no-evidence and SFT bars reverses direction between 1.7B and 4B, revealing the non-monotonic nature of the evidence tax. RSFT consistently narrows the gap toward the no-evidence upper bound.}\n\\label{fig:scaling}\n\\end{figure}\n\n\n\\section{Full Generalization Results}\n\\label{sec:generalization_full}\n\n\\paragraph{Cross-family transfer.}\nLLaMA-3.1-8B confirms the scaling patterns observed with Qwen3. Its SFT baseline achieves 53.84 Ign-F1 (Rel-F1 0.5514, Evi-F1 81.51), and the no-evidence variant reaches 54.52 Ign-F1 (Rel-F1 0.5624). The evidence tax of $-0.68$ points mirrors the near-zero tax seen for Qwen3-8B ($-0.28$), supporting our claim that 8B-class models absorb the cost of joint evidence generation regardless of architecture family. RSFT CED improves LLaMA to 55.58 Ign-F1 (Rel-F1 0.5674, Evi-F1 82.14, EDCR 0.6128), a +1.74 point gain consistent with the pattern at the 8B scale (Qwen3-8B: +3.82). A second seed (s43: 56.19 Ign-F1, EDCR 0.6073) confirms robustness.\n\n\\paragraph{Cross-dataset robustness.}\nOn Re-DocRED~\\citep{tan2022redocred}, the SFT baseline achieves 36.59 Ign-F1 (Evi-F1 81.70, EDCR 0.6674). RSFT CED improves this to 41.45 Ign-F1 (Evi-F1 81.82, EDCR 0.6210), a +4.86pp gain that closely matches the +4.92pp improvement on DocRED. This consistency across datasets with different annotation protocols confirms that RSFT's benefit generalizes beyond training-set-specific artifacts. Evidence quality remains stable across datasets (Evi-F1 81.82 vs.\\ 81.15 on DocRED), and the EDCR reduction ($-0.046$) mirrors the DocRED pattern, further supporting the robustness of CED-based selection.\n\n\\paragraph{Comparison to supervised methods.}\nOur best joint Evi-F1 of approximately 0.36 (using the DREEAM-protocol denominator) falls below the supervised DREEAM result of 54.01\\%~\\citep{ma2023dreeam}. This gap stems primarily from extraction performance rather than evidence quality: our TP-only Evi-F1 exceeds 80\\%, indicating that when the model correctly identifies a triple, it produces high-quality evidence. The overall joint Evi-F1 is diluted by false-positive and false-negative triples in the denominator. Closing this gap requires improving the base extraction capability of LLM-based methods, an orthogonal direction to the evidence faithfulness problem we address. Our contribution is demonstrating that LLMs can generate grounded evidence jointly with extraction, and that RSFT maintains this capability under optimization pressure where RL methods fail.\n\n\n\\section{GRPO Training Dynamics}\n\\label{sec:grpo_dynamics}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_grpo_dynamics.pdf}\n\\caption{Training dynamics of GRPO under different configurations. (a)~Relation F1 across checkpoints: G=4 QLoRA suffers catastrophic collapse at step~10, while G=8 bf16 remains stable. (b)~Evidence F1 stays intact for G=8 bf16, confirming the generation mechanism itself does not fail. (c)~Evidence-Decoupling Ratio (EDCR) reveals near-total decoupling in G=4 QLoRA (extraction collapses to Rel-F1 0.014), while G=8 bf16 maintains healthy ratios.}\n\\label{fig:grpo_dynamics}\n\\end{figure*}\n\n\n\\section{Per-Relation EDCR Distribution}\n\\label{sec:edcr_per_relation}\n\nComputing EDCR for each of the 76 relation types with $\\geq$5 evaluation samples reveals that per-relation EDCR correlates strongly with per-relation Rel-F1 ($\\rho = -0.793$, $p < 0.001$), confirming its utility as a difficulty indicator. However, per-relation EDCR is statistically independent of Evi-F1 ($\\rho = -0.064$, $p = 0.58$), and Evi-F1 itself shows no association with Rel-F1 ($\\rho = -0.013$, $p = 0.91$). These null correlations establish that evidence quality and extraction ability are fully decoupled across relation types. Extreme cases illustrate the diagnostic power: \\texttt{date\\_of\\_birth} has EDCR $= 0.118$ (highly faithful, with extraction and evidence tightly coupled), while \\texttt{head\\_of\\_government} reaches $0.956$ (highly decoupled). Method-level EDCR serves as a horizontal comparison tool across optimization paradigms, while per-relation EDCR enables vertical diagnosis of which relation types suffer from extraction-evidence misalignment.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_edcr_relations.pdf}\n\\caption{Per-relation EDCR distribution across 93 relation types. Red bars indicate relations with EDCR $\\geq$ 0.70 (severe decoupling), green bars indicate EDCR $<$ 0.30 (healthy evidence grounding). Seven relation types exhibit EDCR = 1.0, indicating complete evidence decoupling.}\n\\label{fig:edcr_relations}\n\\end{figure}\n\n\n\\section{Qualitative Analysis}\n\\label{sec:qualitative}\n\nWe present representative examples illustrating three phenomena: evidence quality differences between SFT and RSFT, GRPO format gaming under catastrophic collapse, and per-relation EDCR diagnostics.\n\n\\paragraph{Case 1: Evidence quality.}\nTable~\\ref{tab:case_evidence} compares evidence citations from SFT and RSFT on three documents. SFT tends to cite many sentences indiscriminately, including distractors unrelated to the target triple, while RSFT selects precisely the gold evidence sentences. For \\emph{America's Sweetheart}, SFT cites 6 sentences (precision 0.17) whereas RSFT cites only the single correct sentence (precision 1.00). The pattern is consistent: SFT achieves evidence precision of 0.00--0.20 across these examples, while RSFT achieves 1.00 in all three cases.\n\n\\begin{table}[t]\n\\centering\n\\caption{Evidence citation comparison between SFT and RSFT. Precision measures the fraction of cited sentences that match gold evidence.}\n\\label{tab:case_evidence}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Document} & \\textbf{Triple} & \\textbf{SFT Prec.} & \\textbf{RSFT Prec.} & \\textbf{SFT \\#Cited} \\\\\n\\midrule\nOleg Tinkov & (Oleg Tinkov, country of citizenship, Russia) & 0.00 & 1.00 & 3 \\\\\nAmerica's Sweetheart & (record label, country, United States) & 0.17 & 1.00 & 6 \\\\\nJade (Mortal Kombat) & (Jade, present in work, Mortal Kombat) & 0.20 & 1.00 & 5 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\paragraph{Case 2: GRPO format gaming.}\nUnder catastrophic collapse (GRPO QLoRA $G{=}4$), the model abandons the DocRED 96-type relation ontology and generates free-text relation labels. On the document \\emph{Something to Believe In}, the model produces 35 predicted triples with relations such as ``is a'', ``honor'', and ``location'', none of which belong to the target ontology. All 35 predictions are incorrect. Similarly, for \\emph{J\\'{o}zef Pi\\l{}sudski Monument}, 28 predictions use non-standard relations with 0 correct matches. The model retains the structural format of triple-with-evidence output but fills it with fabricated relation types. The model produces well-formed evidence for these non-existent relations.\n\n\\paragraph{Case 3: EDCR diagnostics.}\nPer-relation EDCR identifies specific relation types where extraction and evidence are misaligned. For \\texttt{date\\_of\\_birth} (EDCR $= 0.118$), the model's evidence consistently matches gold annotations: both extraction and evidence point to the same biographical sentence. In contrast, \\texttt{notable\\_work} (EDCR $= 0.941$) exhibits severe decoupling: the model cites sentence [0] (a general introduction) instead of the gold evidence sentence [3] (which contains the actual work attribution). High-EDCR relations tend to involve indirect or multi-hop reasoning where surface-level context misleads the evidence generator.\n",
      "numLines": 199,
      "startLine": 1,
      "totalLines": 199
    }
  },
  "sourceToolAssistantUUID": "b4a87065-545a-40f7-96f6-852ca512f9b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T06:48:53.818Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KiuJGxD69vt5EGoCiXtX6K`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9697fa61-6fe4-451a-9af4-95928d73d8a0",
  "isSidechain": false,
  "requestId": "req_011Cb9b3WYJAvj1CA56wvEuf",
  "type": "assistant",
  "uuid": "86d19ec7-cb21-4a73-8198-c52f2ef4329e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175uQP8vQqP2vH4FRDuCkXq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 28056,
      "output_tokens": 756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 756,
          "cache_read_input_tokens": 28056,
          "cache_creation_input_tokens": 629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 629
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-18T06:48:53.878Z_

```json
{
  "parentUuid": "09b5eb8b-5c70-45eb-b3fa-80867e4713be",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fbc86b11-ad8e-4d53-a8ab-9b7c7336a0a0",
  "timestamp": "2026-05-18T06:48:53.878Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
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
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 1（方法与实验严谨性）  ### Venue 信息 - **目标 venue**: EMNLP 2026 Main Conference Long Paper (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **页数限制**: 正文 8 页 + unlimited refere…",
  "leafUuid": "fbc86b11-ad8e-4d53-a8ab-9b7c7336a0a0",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Review evidence-grounded information extraction paper",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c"
}
```

---

### Assistant

_source line 43 · 2026-05-18T06:48:57.311Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the paper. Let me search for ARR/EMNLP 2026 reviewer guidelines to get the official review form criteria.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbc86b11-ad8e-4d53-a8ab-9b7c7336a0a0",
  "isSidechain": false,
  "requestId": "req_011Cb9b46wzvp9eytUeAhc7f",
  "type": "assistant",
  "uuid": "af91d057-9a6f-4407-ad76-52d42926cf7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013F5YeC7PtTQ4uTvPxLiY7U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23468,
      "cache_read_input_tokens": 28685,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 154,
          "cache_read_input_tokens": 28685,
          "cache_creation_input_tokens": 23468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23468
          },
          "type": "message"
        }
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

_source line 44 · 2026-05-18T06:48:57.835Z_

论文已全部读完。现在搜索 ARR 官方 review form 标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af91d057-9a6f-4407-ad76-52d42926cf7b",
  "isSidechain": false,
  "requestId": "req_011Cb9b46wzvp9eytUeAhc7f",
  "type": "assistant",
  "uuid": "40809e47-66ea-4c6a-95f8-e813c8de1925",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013F5YeC7PtTQ4uTvPxLiY7U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23468,
      "cache_read_input_tokens": 28685,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 154,
          "cache_read_input_tokens": 28685,
          "cache_creation_input_tokens": 23468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23468
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-18T06:48:58.325Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UWKjbVqxQbhRJST4U7Gpnr`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40809e47-66ea-4c6a-95f8-e813c8de1925",
  "isSidechain": false,
  "requestId": "req_011Cb9b46wzvp9eytUeAhc7f",
  "type": "assistant",
  "uuid": "fadc96cd-ea5b-42e5-bf15-1e6fa0116744",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013F5YeC7PtTQ4uTvPxLiY7U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23468,
      "cache_read_input_tokens": 28685,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 154,
          "cache_read_input_tokens": 28685,
          "cache_creation_input_tokens": 23468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23468
          },
          "type": "message"
        }
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

_source line 46 · 2026-05-18T06:48:58.331Z_

<details><summary>↩ Tool result · `toolu_01UWKjbVqxQbhRJST4U7Gpnr`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fadc96cd-ea5b-42e5-bf15-1e6fa0116744",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "93658a48-7197-45e7-9227-666367fd52fe",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "fadc96cd-ea5b-42e5-bf15-1e6fa0116744",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-18T06:49:02.184Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Rc9evCupopwDqZS66QkT1`</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93658a48-7197-45e7-9227-666367fd52fe",
  "isSidechain": false,
  "requestId": "req_011Cb9b4S3TNAkXcEhAxjnmn",
  "type": "assistant",
  "uuid": "0a5857b1-ddc4-43f4-98e8-a65a45ffc9ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01STC3B4VkdCuYaWwo4GPfec",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 52153,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 681,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 121,
          "cache_read_input_tokens": 52153,
          "cache_creation_input_tokens": 681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 681
          },
          "type": "message"
        }
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

_source line 48 · 2026-05-18T06:49:02.470Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WSYeMRAW6wCx1rvVMYktzG`</summary>

```json
{
  "query": "EMNLP 2026 ARR review form dimensions soundness novelty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a5857b1-ddc4-43f4-98e8-a65a45ffc9ba",
  "isSidechain": false,
  "requestId": "req_011Cb9b4S3TNAkXcEhAxjnmn",
  "type": "assistant",
  "uuid": "d46e214f-4879-4105-bcdb-2491efc0896c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01STC3B4VkdCuYaWwo4GPfec",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 52153,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 681,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 121,
          "cache_read_input_tokens": 52153,
          "cache_creation_input_tokens": 681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 681
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-18T06:49:08.582Z_

<details><summary>↩ Tool result · `toolu_01WSYeMRAW6wCx1rvVMYktzG`</summary>

```text
Web search results for query: "EMNLP 2026 ARR review form dimensions soundness novelty"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Surviving ARR May Meta-Review & Deciding on EMNLP 2025: A Tactical and Honest Guide | CSPaper Forum","url":"https://forum.cspaper.org/topic/113/surviving-arr-may-meta-review-deciding-on-emnlp-2025-a-tactical-and-honest-guide"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/authors.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/authors.md"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"TrustNLP","url":"https://trustnlpworkshop.github.io/"}]

Based on the search results, here's what I found about the ARR review form dimensions for EMNLP 2026:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

Regarding the specific dimensions:

**Soundness**: Reviewers evaluate whether the paper is sufficiently sound and thorough, whether it clearly states scientific claims and provides adequate support for them, and consider the depth and/or breadth of research questions investigated, technical soundness of experiments, and methodological validity of evaluation.

**Novelty**: While novelty is mentioned as a consideration in the review process, the overall assessment score is a composite score reflecting assessment of soundness, excitement, and also other factors like novelty and impact. Additionally, the main criteria for Findings are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

The review form also includes considerations for reproducibility, asking whether there is enough information in the paper for a reader to reproduce the main results, use results presented in the paper in future work, or build upon this work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d46e214f-4879-4105-bcdb-2491efc0896c",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "a8290c9f-fa82-4b0a-be6b-73474cad4224",
  "toolUseResult": {
    "query": "EMNLP 2026 ARR review form dimensions soundness novelty",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ef84TZCVeq71FTegzTGAs5",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "ARR Reviewer Guidelines",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "Review Form",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "Surviving ARR May Meta-Review & Deciding on EMNLP 2025: A Tactical and Honest Guide | CSPaper Forum",
            "url": "https://forum.cspaper.org/topic/113/surviving-arr-may-meta-review-deciding-on-emnlp-2025-a-tactical-and-honest-guide"
          },
          {
            "title": "EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview",
            "url": "https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "aclrollingreview/authors.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/authors.md"
          },
          {
            "title": "LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)",
            "url": "https://linguistlist.org/issues/37/972/"
          },
          {
            "title": "TrustNLP",
            "url": "https://trustnlpworkshop.github.io/"
          }
        ]
      },
      "Based on the search results, here's what I found about the ARR review form dimensions for EMNLP 2026:\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\n\nRegarding the specific dimensions:\n\n**Soundness**: Reviewers evaluate whether the paper is sufficiently sound and thorough, whether it clearly states scientific claims and provides adequate support for them, and consider the depth and/or breadth of research questions investigated, technical soundness of experiments, and methodological validity of evaluation.\n\n**Novelty**: While novelty is mentioned as a consideration in the review process, the overall assessment score is a composite score reflecting assessment of soundness, excitement, and also other factors like novelty and impact. Additionally, the main criteria for Findings are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.\n\nThe review form also includes considerations for reproducibility, asking whether there is enough information in the paper for a reader to reproduce the main results, use results presented in the paper in future work, or build upon this work."
    ],
    "durationSeconds": 6.109426151999997
  },
  "sourceToolAssistantUUID": "d46e214f-4879-4105-bcdb-2491efc0896c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-18T06:49:09.920Z_

<details><summary>↩ Tool result · `toolu_013Rc9evCupopwDqZS66QkT1`</summary>

```text
Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the web search results, here's information about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scores and Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Recommendation Scoring

The review form uses the following overall recommendation scale:

- 5 = Consider for Award: This paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers). Outstanding papers should be either fascinating, controversial, surprising, impressive, or potentially field-changing.

- 2 = Resubmit next cycle: The paper needs substantial revisions that can be completed by the next ARR cycle.

- 1.5 = Resubmit after next cycle: The paper needs substantial revisions that cannot be completed by the next ARR cycle.

- 1 = Do not resubmit: The paper has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language).

## Key Review Form Elements

The review form also includes sections on:

- Limitations and societal impacts: Authors should adequately discuss the limitations and potential positive and negative societal impacts of their work, with constructive suggestions for improvement if needed.

- Ethical issues and ethics review: Reviewers should describe any ethical issues and whether the paper should receive an in-depth ethics review.

- Reproducibility: Whether there is enough information for a reader to reproduce the main results or build upon the work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a5857b1-ddc4-43f4-98e8-a65a45ffc9ba",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "b974d47c-f0a9-47c3-a663-d42653c683df",
  "toolUseResult": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_011Z9gMyWZ8VFCDU2qWHLqiC",
        "content": [
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "aclrollingreview/cfp.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"
          },
          {
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "ACLRollingReview (@ReviewAcl) / Posts / X",
            "url": "https://x.com/ReviewAcl"
          },
          {
            "title": "aclrollingreview/reviewing.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"
          }
        ]
      },
      "Based on the web search results, here's information about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:\n\n## Reviewer Scores and Criteria\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.\n\n## Overall Recommendation Scoring\n\nThe review form uses the following overall recommendation scale:\n\n- 5 = Consider for Award: This paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers). Outstanding papers should be either fascinating, controversial, surprising, impressive, or potentially field-changing.\n\n- 2 = Resubmit next cycle: The paper needs substantial revisions that can be completed by the next ARR cycle.\n\n- 1.5 = Resubmit after next cycle: The paper needs substantial revisions that cannot be completed by the next ARR cycle.\n\n- 1 = Do not resubmit: The paper has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language).\n\n## Key Review Form Elements\n\nThe review form also includes sections on:\n\n- Limitations and societal impacts: Authors should adequately discuss the limitations and potential positive and negative societal impacts of their work, with constructive suggestions for improvement if needed.\n\n- Ethical issues and ethics review: Reviewers should describe any ethical issues and whether the paper should receive an in-depth ethics review.\n\n- Reproducibility: Whether there is enough information for a reader to reproduce the main results or build upon the work."
    ],
    "durationSeconds": 7.729837447000001
  },
  "sourceToolAssistantUUID": "0a5857b1-ddc4-43f4-98e8-a65a45ffc9ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-18T06:49:12.674Z_

<details><summary>Logged reasoning block</summary>

```text
Let me fetch the actual ARR review form page to get the exact scoring dimensions and scales.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b974d47c-f0a9-47c3-a663-d42653c683df",
  "isSidechain": false,
  "requestId": "req_011Cb9b5HMqpJ6HaFhwEBapc",
  "type": "assistant",
  "uuid": "b42b69c6-11bf-4689-bfbb-9f27d4aaeb92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrBYu9GVLNnyMAyznaa128",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 787,
      "cache_creation_input_tokens": 1021,
      "cache_read_input_tokens": 52834,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1021,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 787,
          "output_tokens": 110,
          "cache_read_input_tokens": 52834,
          "cache_creation_input_tokens": 1021,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1021
          },
          "type": "message"
        }
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

_source line 52 · 2026-05-18T06:49:12.892Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014aFp8kV3HXGWtub6QEYUPH`</summary>

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
  "parentUuid": "b42b69c6-11bf-4689-bfbb-9f27d4aaeb92",
  "isSidechain": false,
  "requestId": "req_011Cb9b5HMqpJ6HaFhwEBapc",
  "type": "assistant",
  "uuid": "c4bf56f6-ccd9-446e-b8b6-1eecc178108e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrBYu9GVLNnyMAyznaa128",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 787,
      "cache_creation_input_tokens": 1021,
      "cache_read_input_tokens": 52834,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1021,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 787,
          "output_tokens": 110,
          "cache_read_input_tokens": 52834,
          "cache_creation_input_tokens": 1021,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1021
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-18T06:49:12.897Z_

<details><summary>↩ Tool result · `toolu_014aFp8kV3HXGWtub6QEYUPH`</summary>

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
  "parentUuid": "c4bf56f6-ccd9-446e-b8b6-1eecc178108e",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "ebfdea68-8e85-4994-a6ae-cbae974bd2e9",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "c4bf56f6-ccd9-446e-b8b6-1eecc178108e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-18T06:49:16.772Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018PYuwsYo89gvs1UJ67mtZW`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 etc.), and the description of each score level. Include soundness, excitement, overall assessment, reproducibility, and any other scored dimensions. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebfdea68-8e85-4994-a6ae-cbae974bd2e9",
  "isSidechain": false,
  "requestId": "req_011Cb9b5WEkAkwpWrsCw5GH8",
  "type": "assistant",
  "uuid": "1bc56df2-9817-446c-b64f-5cf0224e6489",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApZbkfHZqKJzL9YJGRn7fo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 53855,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 235,
          "cache_read_input_tokens": 53855,
          "cache_creation_input_tokens": 1415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1415
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-18T06:49:18.031Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MQ2CJW74KfUiCXts4jYvQK`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, how to assess soundness, excitement, novelty, significance, and any specific instructions about scoring. Include all rubric details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bc56df2-9817-446c-b64f-5cf0224e6489",
  "isSidechain": false,
  "requestId": "req_011Cb9b5WEkAkwpWrsCw5GH8",
  "type": "assistant",
  "uuid": "cc88cca2-47db-4ccf-9b8c-e5863aaa9127",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApZbkfHZqKJzL9YJGRn7fo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 53855,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 235,
          "cache_read_input_tokens": 53855,
          "cache_creation_input_tokens": 1415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1415
          },
          "type": "message"
        }
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

_source line 56 · 2026-05-18T06:49:25.135Z_

<details><summary>↩ Tool result · `toolu_01MQ2CJW74KfUiCXts4jYvQK`</summary>

```text
# ARR Reviewer Guidelines Summary

## Core Evaluation Dimensions

ARR reviewers assess papers using three primary scores:

1. **Soundness**: Technical correctness and methodological rigor. Per guidelines, "The _soundness_ scores must be justified by the text of the review." Low soundness scores require explicit justification in the review text.

2. **Excitement**: Personal interest and engagement with the work. This reflects subjective preferences independent of technical quality and "do not necessarily come with explicit reasons."

3. **Overall Assessment**: Composite recommendation reflecting soundness, excitement, novelty, and potential impact. Papers must be "sufficiently sound and reproducible" for acceptance consideration.

## Key Evaluation Principles

**Adjust Expectations**: Reviewers should read papers twice—first for research question and contribution scope, then for technical depth. This prevents bias toward prototype papers in one's subfield.

**Be Specific**: Criticism must cite concrete issues. Generic statements like "missing relevant references" should instead name specific works.

**Avoid Common Biases**: Guidelines flag 17 heuristics (H1-H17) that lead to problematic rejections, including dismissing "unsurprising" results, rejecting negative findings, or demanding unnecessarily complex solutions.

**Check NLP-Specific Issues**: Reviewers should identify methodological problems (M1-M5), artifact sourcing concerns (T1-T2), experimental issues (R1-R5), and general problems (G1-G5).

## Special Requirements

- Justify all scores with review text
- Maintain professional, neutral tone
- Address author responses substantively during discussion
- For resubmissions, focus on whether previous concerns were adequately addressed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc88cca2-47db-4ccf-9b8c-e5863aaa9127",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "a95828e5-879b-45e6-9c1e-630e4fbbbd16",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Reviewer Guidelines Summary\n\n## Core Evaluation Dimensions\n\nARR reviewers assess papers using three primary scores:\n\n1. **Soundness**: Technical correctness and methodological rigor. Per guidelines, \"The _soundness_ scores must be justified by the text of the review.\" Low soundness scores require explicit justification in the review text.\n\n2. **Excitement**: Personal interest and engagement with the work. This reflects subjective preferences independent of technical quality and \"do not necessarily come with explicit reasons.\"\n\n3. **Overall Assessment**: Composite recommendation reflecting soundness, excitement, novelty, and potential impact. Papers must be \"sufficiently sound and reproducible\" for acceptance consideration.\n\n## Key Evaluation Principles\n\n**Adjust Expectations**: Reviewers should read papers twice—first for research question and contribution scope, then for technical depth. This prevents bias toward prototype papers in one's subfield.\n\n**Be Specific**: Criticism must cite concrete issues. Generic statements like \"missing relevant references\" should instead name specific works.\n\n**Avoid Common Biases**: Guidelines flag 17 heuristics (H1-H17) that lead to problematic rejections, including dismissing \"unsurprising\" results, rejecting negative findings, or demanding unnecessarily complex solutions.\n\n**Check NLP-Specific Issues**: Reviewers should identify methodological problems (M1-M5), artifact sourcing concerns (T1-T2), experimental issues (R1-R5), and general problems (G1-G5).\n\n## Special Requirements\n\n- Justify all scores with review text\n- Maintain professional, neutral tone\n- Address author responses substantively during discussion\n- For resubmissions, focus on whether previous concerns were adequately addressed",
    "durationMs": 7102,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "cc88cca2-47db-4ccf-9b8c-e5863aaa9127",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 57_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 1（方法与实验严谨性）  ### Venue 信息 - **目标 venue**: EMNLP 2026 Main Conference Long Paper (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **页数限制**: 正文 8 页 + unlimited refere…",
  "leafUuid": "a95828e5-879b-45e6-9c1e-630e4fbbbd16",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Review evidence-grounded information extraction paper",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c"
}
```

---

### Tool result

_source line 59 · 2026-05-18T06:49:27.062Z_

<details><summary>↩ Tool result · `toolu_018PYuwsYo89gvs1UJ67mtZW`</summary>

```text
# ARR Review Form Scoring Dimensions

## 1. Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. Soundness
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. Excitement
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 4. Overall Assessment
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award: Could be considered for an outstanding paper award."
- **4.5**: "Borderline Award"
- **4**: "Conference: Could be accepted to an *ACL conference."
- **3.5**: "Borderline Conference"
- **3**: "Findings: Could be accepted to the Findings of the ACL."
- **2.5**: "Borderline Findings"
- **2**: "Resubmit next cycle: Needs substantial revisions."
- **1.5**: "Resubmit after next cycle: Needs substantial revisions that cannot be completed quickly."
- **1**: "Do not resubmit: Paper must be fully redone or lacks relevance."

## 5. Reproducibility
Scale: 1-5
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results, but there may be some variation."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results."
- **1**: "They would not be able to reproduce the results no matter how hard they tried."

## 6. Datasets
Scale: 1-5
- **5**: "Enabling: Newly released datasets should affect research project choices."
- **4**: "Useful: I would recommend the new datasets to other researchers."
- **3**: "Potentially useful: Someone might find the new datasets useful."
- **2**: "Documentary: Useful for studying reported research."
- **1**: "No usable datasets submitted."

## 7. Software
Scale: 1-5
- **5**: "Enabling: Newly released software should affect research project choices."
- **4**: "Useful: I would recommend the new software to other researchers."
- **3**: "Potentially useful: Someone might find the new software useful."
- **2**: "Documentary: Useful for studying reported research."
- **1**: "No usable software released."

## 8. Knowledge of Author Identity
Scale: 1-5
- **5**: "I know/can guess at least one author's name from submission violations."
- **4**: "I know/can guess at least one author's name from preprints."
- **3**: "I know/can guess at least one author's name from submission contents."
- **2**: "I know/can guess from social media or informal communication."
- **1**: "I do not have even an educated guess about author identity."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bc56df2-9817-446c-b64f-5cf0224e6489",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "225e1c58-1ce0-4874-9ac2-5c3953092912",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Review Form Scoring Dimensions\n\n## 1. Reviewer Confidence\nScale: 1-5\n- **5**: \"Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work.\"\n- **4**: \"Quite sure. I tried to check the important points carefully.\"\n- **3**: \"Pretty sure, but there's a chance I missed something.\"\n- **2**: \"Willing to defend my evaluation, but it is fairly likely that I missed some details.\"\n- **1**: \"Not my area, or paper is very hard to understand.\"\n\n## 2. Soundness\nScale: 1-5 (with half-point increments)\n- **5**: \"Excellent: This study is one of the most thorough I have seen, given its type.\"\n- **4**: \"Strong: This study provides sufficient support for all of its claims.\"\n- **3**: \"Acceptable: This study provides sufficient support for its main claims.\"\n- **2**: \"Poor: Some of the main claims are not sufficiently supported.\"\n- **1**: \"Major Issues: This study is not yet sufficiently thorough to warrant publication.\"\n\n## 3. Excitement\nScale: 1-5 (with half-point increments)\n- **5**: \"Highly Exciting: I would recommend this paper to others and/or attend its presentation.\"\n- **4**: \"Exciting: I would mention this paper to others and/or make an effort to attend.\"\n- **3**: \"Interesting: I might mention some points of this paper to others.\"\n- **2**: \"Potentially Interesting: this paper does not resonate with me.\"\n- **1**: \"Not Exciting: this paper does not resonate with me, and I don't think it would with others.\"\n\n## 4. Overall Assessment\nScale: 1-5 (with half-point increments)\n- **5**: \"Consider for Award: Could be considered for an outstanding paper award.\"\n- **4.5**: \"Borderline Award\"\n- **4**: \"Conference: Could be accepted to an *ACL conference.\"\n- **3.5**: \"Borderline Conference\"\n- **3**: \"Findings: Could be accepted to the Findings of the ACL.\"\n- **2.5**: \"Borderline Findings\"\n- **2**: \"Resubmit next cycle: Needs substantial revisions.\"\n- **1.5**: \"Resubmit after next cycle: Needs substantial revisions that cannot be completed quickly.\"\n- **1**: \"Do not resubmit: Paper must be fully redone or lacks relevance.\"\n\n## 5. Reproducibility\nScale: 1-5\n- **5**: \"They could easily reproduce the results.\"\n- **4**: \"They could mostly reproduce the results, but there may be some variation.\"\n- **3**: \"They could reproduce the results with some difficulty.\"\n- **2**: \"They would be hard pressed to reproduce the results.\"\n- **1**: \"They would not be able to reproduce the results no matter how hard they tried.\"\n\n## 6. Datasets\nScale: 1-5\n- **5**: \"Enabling: Newly released datasets should affect research project choices.\"\n- **4**: \"Useful: I would recommend the new datasets to other researchers.\"\n- **3**: \"Potentially useful: Someone might find the new datasets useful.\"\n- **2**: \"Documentary: Useful for studying reported research.\"\n- **1**: \"No usable datasets submitted.\"\n\n## 7. Software\nScale: 1-5\n- **5**: \"Enabling: Newly released software should affect research project choices.\"\n- **4**: \"Useful: I would recommend the new software to other researchers.\"\n- **3**: \"Potentially useful: Someone might find the new software useful.\"\n- **2**: \"Documentary: Useful for studying reported research.\"\n- **1**: \"No usable software released.\"\n\n## 8. Knowledge of Author Identity\nScale: 1-5\n- **5**: \"I know/can guess at least one author's name from submission violations.\"\n- **4**: \"I know/can guess at least one author's name from preprints.\"\n- **3**: \"I know/can guess at least one author's name from submission contents.\"\n- **2**: \"I know/can guess from social media or informal communication.\"\n- **1**: \"I do not have even an educated guess about author identity.\"",
    "durationMs": 10286,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "1bc56df2-9817-446c-b64f-5cf0224e6489",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-18T06:50:39.353Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of:
1. The complete paper content
2. The ARR review form dimensions and scoring scales
3. The reviewer guidelines

Let me now conduct my thorough review focusing on method and experimental rigor as directed. Let me organize my findings.

Key areas to review per Director's instructions:
1. Method design (task formulation, CED scoring, EDCR metric)
2. Experimental design & statistical reliability
3. Claims vs evidence alignment
4. Ablation & analysis completeness
5. Reproducibility

Let me now carefully analyze each area:

### 1. Method Design


The task formulation is standard—given a document with sentences and entities, predict triples with supporting evidence. The output format is clearly specified, and the distinction from encoder-based approaches is well-explained, though the formalization glosses over how entity mentions are disambiguated during generation, which could be problematic. For the CED scoring metric, I'm looking at how it's defined and whether the calculation properly captures what it claims to measure.

The CED design uses contrastive NLI scoring, which is reasonable but relies on the assumption that NLI entailment probability actually reflects evidence faithfulness—it's a proxy rather than a direct measure. There's a real issue with hard negative selection: if multiple valid evidence sets exist, some "negative" sentences might actually be valid evidence. Additionally, CED is coupled with extraction correctness since only correct triples contribute to the score, making it less of a pure evidence quality metric. The paper even acknowledges that CED and flat-NLI are nearly identical with only a 0.02 percentage point difference, which somewhat undermines the value of the contrastive formulation.

For EDCR, the metric is defined as Evi-Recall_TP divided by Rel-Recall, which supposedly indicates whether the model produces good evidence for the few correct triples it does extract. But there's a critical flaw: when Rel-Recall becomes very small, EDCR can become artificially inflated. In the extreme case like GRPO QLoRA where Rel-F1 is only 0.0138, getting a ratio approaching 1.0 is almost tautological—if you only extract a handful of correct triples and provide evidence for them, the ratio will naturally be high, which doesn't meaningfully demonstrate "decoupling." The Spearman correlation of -0.965 is also concerning because it's computed over just 6 data points.

Looking at the per-relation EDCR analysis, the correlation with Evi-F1 is essentially zero (ρ = -0.064, p = 0.58), which the paper frames as evidence of full decoupling across relation types. But that's an overstatement—a lack of correlation doesn't prove independence.

On the experimental design side, the "85+ configurations" claim doesn't quite add up. The paper lists 4 model scales across 2 families, but Qwen3 actually has 3 scales while LLaMA has only 1, giving 4 total configurations. The methods count needs clarification too.

The method variants span SFT, GRPO with different quantization approaches, DPO at different epochs, and RSFT with various CED parameters—roughly 9 distinct methods. With 4 models, 2 datasets, and multiple seeds (4 for some RSFT variants, 2 for others, unspecified for the rest), the math could reach 72+ base configurations, potentially hitting 85+ with seeds. But the paper doesn't transparently lay out the full experiment matrix, making the claim hard to verify.

Looking at the statistical rigor: RSFT CED k=1 has solid support with 4 seeds (44.66 ± 0.49), but flat-NLI only uses 2 seeds, which isn't enough for confidence. The SFT baseline is the real problem—it's apparently a single run with no variance reported, so the claimed +4.92pp improvement can't be properly assessed for significance. GRPO and DPO also appear to be single runs. No significance tests are applied anywhere, and the 1.7B and 8B results are explicitly single-seed runs. The paper compares against SFT, SFT no-evidence, GRPO, DPO, and RSFT, but skips encoder-based methods entirely.

The evaluation is limited to the dev set only—test results are still pending. For a paper claiming to explore "85+ configurations," having zero test set validation substantially undermines the empirical claims, even though the authors acknowledge this limitation. The GRPO QLoRA collapse is striking, but the explanation remains incomplete.

The quantization hypothesis lacks controlled ablation—you'd need to isolate quantization from group size and other variables to actually prove it's the culprit. The "spectrum" itself only has 6 points and mixes multiple factors together. There's also a methodological issue: DPO at 3 epochs uses a different evaluation protocol than the 1-epoch baseline, so comparing their trends is problematic.

For the scale-dependent evidence tax claim, the evidence is thin—just three Qwen3 scales plus one LLaMA point. The non-monotonic pattern they're describing needs more data points to be convincing.  At 1.7B specifically, the +8pp gain could simply reflect that evidence generation forces more structured outputs and reduces the repetitive patterns the paper itself documents, rather than supporting their implicit regularization hypothesis. The "fair evaluation subset" showing +6.2pp gets mentioned but never explained.

The RSFT effectiveness claim is their strongest with 4-seed support at 4B, though the "1.7B RSFT matches 8B SFT" comparison still needs scrutiny.

Now looking at the ablations and analysis gaps: the CED versus flat-NLI difference is negligible at 0.02pp, so the choice between them doesn't matter empirically despite the paper's framing around interpretability. The k=1 versus k=3 comparison only tests CED with a single seed for k=3, and they're missing key baselines like random selection or training on all outputs without filtering.

For the optimization configurations, GRPO only compares two setups that vary quantization and group size simultaneously, making it impossible to isolate which factor drives the difference. DPO only explores β=0.1 with no sensitivity analysis, and neither method tests different LoRA ranks or KL coefficients. The scale analysis relies on just three Qwen3 points plus one LLaMA point, and the LLaMA result doesn't cleanly align with the others, so claiming a non-monotonic pattern from this sparse data feels premature.

Reproducibility looks reasonable with hyperparameters in the appendix, though the data processing pipeline description is incomplete.

Now I'm noticing several presentation issues: Table 1 mixes decimal and percentage formats inconsistently, the paper claims to address "Scaling" but only tests 3-4 scale points, some bibliography entries are incomplete or anonymous, and there's a citation to a July 2025 arXiv paper that seems oddly recent.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "225e1c58-1ce0-4874-9ac2-5c3953092912",
  "isSidechain": false,
  "requestId": "req_011Cb9b6YdtHwfmcfKLPHzTg",
  "type": "assistant",
  "uuid": "c89fce88-38ae-4074-aa8c-1f4140f2ae95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCSS8HaJMcPfjnuo586qEM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 410,
      "cache_creation_input_tokens": 1273,
      "cache_read_input_tokens": 55270,
      "output_tokens": 2774,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1273,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 410,
          "output_tokens": 2774,
          "cache_read_input_tokens": 55270,
          "cache_creation_input_tokens": 1273,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1273
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-18T06:50:39.498Z_

已获取 ARR 官方 review form 完整评分标准。现在开始撰写审稿意见。

我先验证几个关键引用的真实性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c89fce88-38ae-4074-aa8c-1f4140f2ae95",
  "isSidechain": false,
  "requestId": "req_011Cb9b6YdtHwfmcfKLPHzTg",
  "type": "assistant",
  "uuid": "30bc0528-c923-41c9-ab4c-cdf94b47f8d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCSS8HaJMcPfjnuo586qEM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 410,
      "cache_creation_input_tokens": 1273,
      "cache_read_input_tokens": 55270,
      "output_tokens": 2774,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1273,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 410,
          "output_tokens": 2774,
          "cache_read_input_tokens": 55270,
          "cache_creation_input_tokens": 1273,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1273
          },
          "type": "message"
        }
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

_source line 62 · 2026-05-18T06:50:39.789Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Kgc8PhyX4s7QAoeBseXJXp`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__verify_references",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30bc0528-c923-41c9-ab4c-cdf94b47f8d1",
  "isSidechain": false,
  "requestId": "req_011Cb9b6YdtHwfmcfKLPHzTg",
  "type": "assistant",
  "uuid": "60b81ffe-34cd-4efc-92f4-2de8088dddf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCSS8HaJMcPfjnuo586qEM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 410,
      "cache_creation_input_tokens": 1273,
      "cache_read_input_tokens": 55270,
      "output_tokens": 2774,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1273,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 410,
          "output_tokens": 2774,
          "cache_read_input_tokens": 55270,
          "cache_creation_input_tokens": 1273,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1273
          },
          "type": "message"
        }
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

_source line 63 · 2026-05-18T06:50:39.799Z_

<details><summary>↩ Tool result · `toolu_01Kgc8PhyX4s7QAoeBseXJXp`</summary>

````text
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
  "parentUuid": "60b81ffe-34cd-4efc-92f4-2de8088dddf4",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "958bd8ae-2f60-42ea-89e9-0c4eb676fee5",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__verify_references"
    ],
    "query": "select:mcp__agent-ml-research__verify_references",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "60b81ffe-34cd-4efc-92f4-2de8088dddf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-18T06:50:42.925Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_0135yNDVLHnhVCk3K5nGosCH`</summary>

```json
{
  "paper_dir": "projects/faith-evidence-ie/docs/paper",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "958bd8ae-2f60-42ea-89e9-0c4eb676fee5",
  "isSidechain": false,
  "requestId": "req_011Cb9bBun1mgPSCWuQi3hUK",
  "type": "assistant",
  "uuid": "5ab06013-4189-424c-ba9e-5a0c636e9cac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UqG58Ao6u1fSQSz6KngmRi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3547,
      "cache_read_input_tokens": 56543,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3547,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 56543,
          "cache_creation_input_tokens": 3547,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3547
          },
          "type": "message"
        }
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

_source line 65 · 2026-05-18T06:50:42.963Z_

<details><summary>↩ Tool result · `toolu_0135yNDVLHnhVCk3K5nGosCH`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"目录不存在: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/projects/faith-evidence-ie/docs/paper\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ab06013-4189-424c-ba9e-5a0c636e9cac",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "ed66939d-d713-4b95-9dca-9ee92065b476",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"目录不存在: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/projects/faith-evidence-ie/docs/paper\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"目录不存在: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/projects/faith-evidence-ie/docs/paper\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "5ab06013-4189-424c-ba9e-5a0c636e9cac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 66 · 2026-05-18T06:50:42.977Z_

```json
{
  "parentUuid": "ed66939d-d713-4b95-9dca-9ee92065b476",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f4eafbf8-9fa6-45f0-952c-f15bc20371d2",
  "timestamp": "2026-05-18T06:50:42.977Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 67_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 1（方法与实验严谨性）  ### Venue 信息 - **目标 venue**: EMNLP 2026 Main Conference Long Paper (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **页数限制**: 正文 8 页 + unlimited refere…",
  "leafUuid": "f4eafbf8-9fa6-45f0-952c-f15bc20371d2",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c"
}
```

---

### Runtime record

_source line 68_

```json
{
  "type": "ai-title",
  "aiTitle": "Review evidence-grounded information extraction paper",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c"
}
```

---

### Tool call

_source line 69 · 2026-05-18T06:50:45.591Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01WuMTE7RsN1P1KhN1wnJ2r6`</summary>

```json
{
  "paper_dir": "docs/paper",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4eafbf8-9fa6-45f0-952c-f15bc20371d2",
  "isSidechain": false,
  "requestId": "req_011Cb9bC9AR9QX6vH2k5Vk8V",
  "type": "assistant",
  "uuid": "f3bdcc85-a04d-4a1f-9884-806000416bbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01246ZmPQ3N9pa6spgJDr8nQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 288,
      "cache_read_input_tokens": 60090,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 60090,
          "cache_creation_input_tokens": 288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 288
          },
          "type": "message"
        }
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

_source line 70 · 2026-05-18T06:51:16.356Z_

<details><summary>↩ Tool result · `toolu_01WuMTE7RsN1P1KhN1wnJ2r6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 40, \"total_citations\": 54, \"unique_cited_keys\": 33, \"orphan_bib\": 7, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 22, \"online_not_found\": 13, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [\"APA:83\", \"Aho:72\", \"Ando2005\", \"Chandra:81\", \"Gusfield:97\", \"andrew2007scalable\", \"rasooli-tetrault-2015\"], \"missing_bib\": [], \"orphan_count\": 7, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"autore2024\", \"type\": \"inproceedings\", \"title\": \"AutoRE: Document-Level Relation Extraction with Large Language Models\", \"authors\": \"Anonymous\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"chen2025docksrag\", \"type\": \"inproceedings\", \"title\": \"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning\", \"authors\": \"Xu and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the 42nd International Conference on Machine Learning\"}, {\"key\": \"dai2025r1re\", \"type\": \"article\", \"title\": \"R1-RE: Cross-Domain Relation Extraction with RLVR\", \"authors\": \"Dai, Runpeng and Zheng, Tong and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2507.04642\"}, {\"key\": \"gao2023scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling Laws for Reward Model Overoptimization\", \"authors\": \"Gao, Leo and Schulman, John and Hilton, Jacob\", \"year\": \"2023\", \"venue\": \"Proceedings of the 40th International Conference on Machine Learning\"}, {\"key\": \"hu2022lora\", \"type\": \"inproceedings\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"authors\": \"Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"jin2025rl_panacea\", \"type\": \"article\", \"title\": \"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs\", \"authors\": \"Jin, Hangzhan and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.16546\"}, {\"key\": \"ma2023dreeam\", \"type\": \"inproceedings\", \"title\": \"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\", \"authors\": \"Ma, Youmi and Wang, An and Okazaki, Naoaki\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: EACL 2023\"}, {\"key\": \"moskovitz2024constrained\", \"type\": \"inproceedings\", \"title\": \"Confronting Reward Model Overoptimization with Constrained RLHF\", \"authors\": \"Moskovitz, Ted and Singh, Aaditya K. and Strouse, DJ and Sandholm, Tuomas and Sa...\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"rafailov2023direct\", \"type\": \"inproceedings\", \"title\": \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\", \"authors\": \"Rafailov, Rafael and Sharma, Archit and Mitchell, Eric and Ermon, Stefano and Ma...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"shao2024deepseekmath\", \"type\": \"article\", \"title\": \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\", \"authors\": \"Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao an...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.03300\"}, {\"key\": \"tan2022redocred\", \"type\": \"inproceedings\", \"title\": \"Revisiting DocRED: Addressing the False Negative Problem in Relation Extraction\", \"authors\": \"Tan, Qingyu and Xu, Lu and Bing, Lidong and Ng, Hwee Tou and Aljunied, Sharifah ...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"wan2024genres\", \"type\": \"inproceedings\", \"title\": \"GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models\", \"authors\": \"Jiang, Pengcheng and Lin, Jiacheng and Wang, Zifeng and Sun, Jimeng and Han, Jia...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"xiao2022sais\", \"type\": \"inproceedings\", \"title\": \"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction\", \"authors\": \"Xiao, Yuxin and Zhang, Zecheng and Mao, Yuning and Yang, Carl and Han, Jiawei\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"xie2022eider\", \"type\": \"inproceedings\", \"title\": \"EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\", \"authors\": \"Xie, Yiqing and Shen, Jiaming and Li, Sha and Mao, Yuning and Han, Jiawei\", \"year\": \"2022\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2022\"}, {\"key\": \"xu2024lmrc\", \"type\": \"article\", \"title\": \"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\", \"authors\": \"Li, Xingzuo and Chen, Kehai and Long, Yunfei and Zhang, Min\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2408.13889\"}, {\"key\": \"yao2019docred\", \"type\": \"inproceedings\", \"title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"authors\": \"Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zheng...\", \"year\": \"2019\", \"venue\": \"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"zelikman2022star\", \"type\": \"inproceedings\", \"title\": \"STaR: Bootstrapping Reasoning With Reasoning\", \"authors\": \"Zelikman, Eric and Wu, Yuhuai and Mu, Jesse and Goodman, Noah D.\", \"year\": \"2022\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"zhao2025egrpo\", \"type\": \"inproceedings\", \"title\": \"E-GRPO: Entity-Aware Reward for Group Relative Policy Optimization\", \"authors\": \"Anonymous\", \"year\": \"2026\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"dong2023raft\", \"type\": \"article\", \"title\": \"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\", \"authors\": \"Dong, Hanze and Xiong, Wei and Goyal, Deepanshu and Zhang, Yihan and Chow, Winni...\", \"year\": \"2023\", \"venue\": \"Transactions on Machine Learning Research\"}, {\"key\": \"ito2025mogrpo\", \"type\": \"article\", \"title\": \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\", \"authors\": \"Ito, Taishu and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2509.22047\"}, {\"key\": \"li2025drift\", \"type\": \"inproceedings\", \"title\": \"Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference\", \"authors\": \"Li, Jiazheng and Yan, Hanqi and He, Yulan\", \"year\": \"2025\", \"venue\": \"Proceedings of the 63rd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"liu2026gdpo\", \"type\": \"article\", \"title\": \"GDPO: Group Reward-Decoupled Normalization Policy Optimization for Multi-Reward RL Optimization\", \"authors\": \"Liu, Shih-Yang and others\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2601.05242\"}, {\"key\": \"liu2025drgrpo\", \"type\": \"inproceedings\", \"title\": \"Understanding R1-Zero-Like Training: A Critical Perspective\", \"authors\": \"Liu, Zichen and others\", \"year\": \"2025\", \"venue\": \"Conference on Language Modeling\"}, {\"key\": \"yu2025dapo\", \"type\": \"article\", \"title\": \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\", \"authors\": \"Yu, Qiying and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.14476\"}, {\"key\": \"zhang2024infuse\", \"type\": \"inproceedings\", \"title\": \"Fine-Grained Natural Language Inference Based Faithfulness Evaluation for Diverse Summarisation Tasks\", \"authors\": \"Zhang, Huajian and Xu, Yumo and Perez-Beltrachini, Laura\", \"year\": \"2024\", \"venue\": \"Proceedings of the 18th Conference of the European Chapter of the Association fo...\"}, {\"key\": \"chen2025dragrpo\", \"type\": \"article\", \"title\": \"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\", \"authors\": \"Chen, Xiwen and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.09655\"}, {\"key\": \"hu2025reinforcepp\", \"type\": \"article\", \"title\": \"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\", \"authors\": \"Hu, Yifan\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2501.03262\"}, {\"key\": \"wang2025rear\", \"type\": \"inproceedings\", \"title\": \"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\", \"authors\": \"Wang, Yutao and others\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2025\"}, {\"key\": \"wang2025relprior\", \"type\": \"article\", \"title\": \"RelPrior: Relation as a Prior for LLM-based Document-Level Relation Extraction\", \"authors\": \"Wang, Yuxuan and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.08143\"}, {\"key\": \"zhang2025glidre\", \"type\": \"article\", \"title\": \"GLiDRE: Generalist Lightweight Model for Document-level Relation Extraction\", \"authors\": \"Zhang, Xiao and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.00757\"}, {\"key\": \"tang2025rsftppo\", \"type\": \"inproceedings\", \"title\": \"Rejection Sampling Based Fine Tuning Secretly Performs PPO\", \"authors\": \"Tang, Yunhao and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the 42nd International Conference on Machine Learning\"}, {\"key\": \"wang2025rullm\", \"type\": \"article\", \"title\": \"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\", \"authors\": \"Wang, Chenghao and others\", \"year\": \"2025\", \"venue\": \"NLPCC 2025\"}, {\"key\": \"zhou2021atlop\", \"type\": \"inproceedings\", \"title\": \"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling\", \"authors\": \"Zhou, Wenxuan and Huang, Kevin and Ma, Tengyu and Huang, Jing\", \"year\": \"2021\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"Aho:72\", \"type\": \"book\", \"title\": \"The Theory of Parsing, Translation and Compiling\", \"authors\": \"Alfred V. Aho and Jeffrey D. Ullman\", \"year\": \"1972\", \"venue\": \"\"}, {\"key\": \"APA:83\", \"type\": \"book\", \"title\": \"Publications Manual\", \"authors\": \"American Psychological Association\", \"year\": \"1983\", \"venue\": \"\"}, {\"key\": \"Chandra:81\", \"type\": \"article\", \"title\": \"Alternation\", \"authors\": \"Ashok K. Chandra and Dexter C. Kozen and Larry J. Stockmeyer\", \"year\": \"1981\", \"venue\": \"Journal of the Association for Computing Machinery\"}, {\"key\": \"andrew2007scalable\", \"type\": \"inproceedings\", \"title\": \"Scalable training of L1-regularized log-linear models\", \"authors\": \"Andrew, Galen and Gao, Jianfeng\", \"year\": \"2007\", \"venue\": \"Proceedings of the 24th International Conference on Machine Learning\"}, {\"key\": \"Gusfield:97\", \"type\": \"book\", \"title\": \"Algorithms on Strings, Trees and Sequences\", \"authors\": \"Dan Gusfield\", \"year\": \"1997\", \"venue\": \"\"}, {\"key\": \"rasooli-tetrault-2015\", \"type\": \"article\", \"title\": \"Yara Parser: A Fast and Accurate Dependency Parser\", \"authors\": \"Mohammad Sadegh Rasooli and Joel R. Tetreault\", \"year\": \"2015\", \"venue\": \"Computing Research Repository\"}, {\"key\": \"Ando2005\", \"type\": \"article\", \"title\": \"A Framework for Learning Predictive Structures from Multiple Tasks and Unlabeled Data\", \"authors\": \"Ando, Rie Kubota and Zhang, Tong\", \"year\": \"2005\", \"venue\": \"Journal of Machine Learning Research\"}], \"tex_citations\": [{\"key\": \"zhou2021atlop\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"citet\"}, {\"key\": \"autore2024\", \"file\": \"sections/introduction.tex\", \"line\": 4, \"command\": \"citet\"}, {\"key\": \"xu2024lmrc\", \"file\": \"sections/introduction.tex\", \"line\": 4, \"command\": \"citet\"}, {\"key\": \"chen2025docksrag\", \"file\": \"sections/introduction.tex\", \"line\": 4, \"command\": \"citet\"}, {\"key\": \"yao2019docred\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"citep\"}, {\"key\": \"tan2022redocred\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"citep\"}, {\"key\": \"xiao2022sais\", \"file\": \"sections/introduction.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"ma2023dreeam\", \"file\": \"sections/introduction.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"yao2019docred\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"citep\"}, {\"key\": \"zhou2021atlop\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"xiao2022sais\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"ma2023dreeam\", \"file\": \"sections/related_work.tex\", \"line\": 9, \"command\": \"citep\"}, {\"key\": \"xie2022eider\", \"file\": \"sections/related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"autore2024\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"xu2024lmrc\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"wang2025relprior\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"zhang2025glidre\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"wang2025rullm\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"chen2025docksrag\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"yu2025dapo\", \"file\": \"sections/related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"liu2025drgrpo\", \"file\": \"sections/related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"hu2025reinforcepp\", \"file\": \"sections/related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"chen2025dragrpo\", \"file\": \"sections/related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"liu2026gdpo\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"citep\"}, {\"key\": \"ito2025mogrpo\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"citep\"}, {\"key\": \"zhao2025egrpo\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citep\"}, {\"key\": \"dai2025r1re\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citep\"}, {\"key\": \"wang2025rear\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citep\"}, {\"key\": \"rafailov2023direct\", \"file\": \"sections/related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"jin2025rl_panacea\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"citep\"}, {\"key\": \"gao2023scaling\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"citep\"}, {\"key\": \"moskovitz2024constrained\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"citep\"}, {\"key\": \"li2025drift\", \"file\": \"sections/related_work.tex\", \"line\": 27, \"command\": \"citet\"}, {\"key\": \"zhang2024infuse\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"citet\"}, {\"key\": \"zelikman2022star\", \"file\": \"sections/related_work.tex\", \"line\": 31, \"command\": \"citet\"}, {\"key\": \"dong2023raft\", \"file\": \"sections/related_work.tex\", \"line\": 32, \"command\": \"citet\"}, {\"key\": \"tang2025rsftppo\", \"file\": \"sections/related_work.tex\", \"line\": 33, \"command\": \"citep\"}, {\"key\": \"xiao2022sais\", \"file\": \"sections/method.tex\", \"line\": 9, \"command\": \"citep\"}, {\"key\": \"ma2023dreeam\", \"file\": \"sections/method.tex\", \"line\": 9, \"command\": \"citep\"}, {\"key\": \"hu2022lora\", \"file\": \"sections/method.tex\", \"line\": 15, \"command\": \"citep\"}, {\"key\": \"yao2019docred\", \"file\": \"sections/method.tex\", \"line\": 15, \"command\": \"citep\"}, {\"key\": \"shao2024deepseekmath\", \"file\": \"sections/method.tex\", \"line\": 24, \"command\": \"citep\"}, {\"key\": \"rafailov2023direct\", \"file\": \"sections/method.tex\", \"line\": 27, \"command\": \"citep\"}, {\"key\": \"zelikman2022star\", \"file\": \"sections/method.tex\", \"line\": 30, \"command\": \"citep\"}, {\"key\": \"yao2019docred\", \"file\": \"sections/experiments.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"tan2022redocred\", \"file\": \"sections/experiments.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"hu2022lora\", \"file\": \"sections/experiments.tex\", \"line\": 14, \"command\": \"citep\"}, {\"key\": \"ma2023dreeam\", \"file\": \"sections/experiments.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"ma2023dreeam\", \"file\": \"sections/experiments.tex\", \"line\": 120, \"command\": \"citep\"}, {\"key\": \"tan2022redocred\", \"file\": \"sections/experiments.tex\", \"line\": 126, \"command\": \"citep\"}, {\"key\": \"ma2023dreeam\", \"file\": \"sections/experiments.tex\", \"line\": 126, \"command\": \"citep\"}, {\"key\": \"wan2024genres\", \"file\": \"sections/limitations.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"tan2022redocred\", \"file\": \"sections/appendix.tex\", \"line\": 138, \"command\": \"citep\"}, {\"key\": \"ma2023dreeam\", \"file\": \"sections/appendix.tex\", \"line\": 141, \"command\": \"citep\"}], \"online_verification\": [{\"key\": \"autore2024\", \"title\": \"AutoRE: Document-Level Relation Extraction with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"AutoRE: Document-Level Relation Extraction with Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=anonymous vs api=xue\"], \"note\": \"\"}, {\"key\": \"chen2025docksrag\", \"title\": \"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning\", \"status\": \"not_found\", \"confidence\": 0.305, \"matched_title\": \"Retrieval-Augmented Generation with Graphs (GraphRAG)\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\"}, {\"key\": \"dai2025r1re\", \"title\": \"R1-RE: Cross-Domain Relation Extraction with RLVR\", \"status\": \"not_found\", \"confidence\": 0.362, \"matched_title\": \"MR-UIE: multi-perspective reasoning with reinforcement learning for universal information extraction\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.36 below threshold 0.82\"}, {\"key\": \"gao2023scaling\", \"title\": \"Scaling Laws for Reward Model Overoptimization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scaling Laws for Reward Model Overoptimization\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hu2022lora\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jin2025rl_panacea\", \"title\": \"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs\", \"status\": \"not_found\", \"confidence\": 0.497, \"matched_title\": \"Visual Reasoning through Tool-supervised Reinforcement Learning\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.50 below threshold 0.82\"}, {\"key\": \"ma2023dreeam\", \"title\": \"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"moskovitz2024constrained\", \"title\": \"Confronting Reward Model Overoptimization with Constrained RLHF\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confronting Reward Model Overoptimization with Constrained RLHF\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"rafailov2023direct\", \"title\": \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shao2024deepseekmath\", \"title\": \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\", \"status\": \"not_found\", \"confidence\": 0.465, \"matched_title\": \"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.46 below threshold 0.82\"}, {\"key\": \"tan2022redocred\", \"title\": \"Revisiting DocRED: Addressing the False Negative Problem in Relation Extraction\", \"status\": \"verified\", \"confidence\": 0.981, \"matched_title\": \"Revisiting DocRED - Addressing the False Negative Problem in Relation Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wan2024genres\", \"title\": \"GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiao2022sais\", \"title\": \"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie2022eider\", \"title\": \"EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xu2024lmrc\", \"title\": \"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\", \"status\": \"verified\", \"confidence\": 0.957, \"matched_title\": \"LLM with Relation Classifier for Document-Level Relation Extraction\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yao2019docred\", \"title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zelikman2022star\", \"title\": \"STaR: Bootstrapping Reasoning With Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"STaR: Bootstrapping Reasoning With Reasoning\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhao2025egrpo\", \"title\": \"E-GRPO: Entity-Aware Reward for Group Relative Policy Optimization\", \"status\": \"not_found\", \"confidence\": 0.283, \"matched_title\": \"Instruction Tuning for Large Language Models: A Survey\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.28 below threshold 0.82\"}, {\"key\": \"dong2023raft\", \"title\": \"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ito2025mogrpo\", \"title\": \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\", \"status\": \"not_found\", \"confidence\": 0.231, \"matched_title\": \"Reasoning on a Budget: Miniaturizing DeepSeek R1 with SFT-GRPO Alignment for Instruction-Tuned LLMs\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.23 below threshold 0.82\"}, {\"key\": \"li2025drift\", \"title\": \"Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liu2026gdpo\", \"title\": \"GDPO: Group Reward-Decoupled Normalization Policy Optimization for Multi-Reward RL Optimization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liu2025drgrpo\", \"title\": \"Understanding R1-Zero-Like Training: A Critical Perspective\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Understanding R1-Zero-Like Training: A Critical Perspective\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yu2025dapo\", \"title\": \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\", \"status\": \"not_found\", \"confidence\": 0.31, \"matched_title\": \"OpenRLHF: A Ray-based Easy-to-use, Scalable and High-performance RLHF Framework\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.31 below threshold 0.82\"}, {\"key\": \"zhang2024infuse\", \"title\": \"Fine-Grained Natural Language Inference Based Faithfulness Evaluation for Diverse Summarisation Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Fine-Grained Natural Language Inference Based Faithfulness Evaluation for Diverse Summarisation Tasks\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2025dragrpo\", \"title\": \"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\", \"status\": \"not_found\", \"confidence\": 0.488, \"matched_title\": \"MMR-GRPO: Accelerating GRPO-Style Training through Diversity-Aware Reward Reweighting\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.49 below threshold 0.82\"}, {\"key\": \"hu2025reinforcepp\", \"title\": \"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=hu vs api=jian\"], \"note\": \"\"}, {\"key\": \"wang2025rear\", \"title\": \"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=wang vs api=luo\"], \"note\": \"\"}, {\"key\": \"wang2025relprior\", \"title\": \"RelPrior: Relation as a Prior for LLM-based Document-Level Relation Extraction\", \"status\": \"mismatch\", \"confidence\": 0.829, \"matched_title\": \"Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=wang vs api=pi\"], \"note\": \"\"}, {\"key\": \"zhang2025glidre\", \"title\": \"GLiDRE: Generalist Lightweight Model for Document-level Relation Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=zhang vs api=armingaud\"], \"note\": \"\"}, {\"key\": \"tang2025rsftppo\", \"title\": \"Rejection Sampling Based Fine Tuning Secretly Performs PPO\", \"status\": \"not_found\", \"confidence\": 0.262, \"matched_title\": \"A Comprehensive Overview of Large Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.26 below threshold 0.82\"}, {\"key\": \"wang2025rullm\", \"title\": \"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\", \"status\": \"not_found\", \"confidence\": 0.444, \"matched_title\": \"Automation and machine learning augmented by large language models in a catalysis study\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.44 below threshold 0.82\"}, {\"key\": \"zhou2021atlop\", \"title\": \"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"Aho:72\", \"title\": \"The Theory of Parsing, Translation and Compiling\", \"status\": \"verified\", \"confidence\": 0.99, \"matched_title\": \"The Theory of Parsing, Translation, and Compiling\", \"matched_year\": \"1972\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"APA:83\", \"title\": \"Publications Manual\", \"status\": \"not_found\", \"confidence\": 0.456, \"matched_title\": \"Publication Manual of the American Psychological Association\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.46 below threshold 0.82\"}, {\"key\": \"Chandra:81\", \"title\": \"Alternation\", \"status\": \"not_found\", \"confidence\": 0.222, \"matched_title\": \"Dispersion and Absorption in Dielectrics I. Alternating Current Characteristics\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.22 below threshold 0.82\"}, {\"key\": \"andrew2007scalable\", \"title\": \"Scalable training of L1-regularized log-linear models\", \"status\": \"not_found\", \"confidence\": 0.422, \"matched_title\": \"Discriminative Log-Linear Grammars with Latent Variables\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.42 below threshold 0.82\"}, {\"key\": \"Gusfield:97\", \"title\": \"Algorithms on Strings, Trees and Sequences\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Algorithms on Strings, Trees and Sequences\", \"matched_year\": \"1997\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"rasooli-tetrault-2015\", \"title\": \"Yara Parser: A Fast and Accurate Dependency Parser\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Yara Parser: A Fast and Accurate Dependency Parser\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"Ando2005\", \"title\": \"A Framework for Learning Predictive Structures from Multiple Tasks and Unlabeled Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Framework for Learning Predictive Structures from Multiple Tasks and Unlabeled Data\", \"matched_year\": \"2005\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3bdcc85-a04d-4a1f-9884-806000416bbc",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "564b57b5-4c90-4398-b4ac-7511a3d51f49",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 40, \\\"total_citations\\\": 54, \\\"unique_cited_keys\\\": 33, \\\"orphan_bib\\\": 7, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 22, \\\"online_not_found\\\": 13, \\\"online_mismatch\\\": 5}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [\\\"APA:83\\\", \\\"Aho:72\\\", \\\"Ando2005\\\", \\\"Chandra:81\\\", \\\"Gusfield:97\\\", \\\"andrew2007scalable\\\", \\\"rasooli-tetrault-2015\\\"], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 7, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"autore2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"AutoRE: Document-Level Relation Extraction with Large Language Models\\\", \\\"authors\\\": \\\"Anonymous\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"chen2025docksrag\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning\\\", \\\"authors\\\": \\\"Xu and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 42nd International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"dai2025r1re\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"R1-RE: Cross-Domain Relation Extraction with RLVR\\\", \\\"authors\\\": \\\"Dai, Runpeng and Zheng, Tong and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2507.04642\\\"}, {\\\"key\\\": \\\"gao2023scaling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scaling Laws for Reward Model Overoptimization\\\", \\\"authors\\\": \\\"Gao, Leo and Schulman, John and Hilton, Jacob\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 40th International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"hu2022lora\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LoRA: Low-Rank Adaptation of Large Language Models\\\", \\\"authors\\\": \\\"Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li,...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"jin2025rl_panacea\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs\\\", \\\"authors\\\": \\\"Jin, Hangzhan and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.16546\\\"}, {\\\"key\\\": \\\"ma2023dreeam\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\\\", \\\"authors\\\": \\\"Ma, Youmi and Wang, An and Okazaki, Naoaki\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: EACL 2023\\\"}, {\\\"key\\\": \\\"moskovitz2024constrained\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\", \\\"authors\\\": \\\"Moskovitz, Ted and Singh, Aaditya K. and Strouse, DJ and Sandholm, Tuomas and Sa...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"rafailov2023direct\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\\\", \\\"authors\\\": \\\"Rafailov, Rafael and Sharma, Archit and Mitchell, Eric and Ermon, Stefano and Ma...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"shao2024deepseekmath\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\", \\\"authors\\\": \\\"Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao an...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2402.03300\\\"}, {\\\"key\\\": \\\"tan2022redocred\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Revisiting DocRED: Addressing the False Negative Problem in Relation Extraction\\\", \\\"authors\\\": \\\"Tan, Qingyu and Xu, Lu and Bing, Lidong and Ng, Hwee Tou and Aljunied, Sharifah ...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"wan2024genres\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models\\\", \\\"authors\\\": \\\"Jiang, Pengcheng and Lin, Jiacheng and Wang, Zifeng and Sun, Jimeng and Han, Jia...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"xiao2022sais\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction\\\", \\\"authors\\\": \\\"Xiao, Yuxin and Zhang, Zecheng and Mao, Yuning and Yang, Carl and Han, Jiawei\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"xie2022eider\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\\\", \\\"authors\\\": \\\"Xie, Yiqing and Shen, Jiaming and Li, Sha and Mao, Yuning and Han, Jiawei\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2022\\\"}, {\\\"key\\\": \\\"xu2024lmrc\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\\\", \\\"authors\\\": \\\"Li, Xingzuo and Chen, Kehai and Long, Yunfei and Zhang, Min\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2408.13889\\\"}, {\\\"key\\\": \\\"yao2019docred\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\\\", \\\"authors\\\": \\\"Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zheng...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"zelikman2022star\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"STaR: Bootstrapping Reasoning With Reasoning\\\", \\\"authors\\\": \\\"Zelikman, Eric and Wu, Yuhuai and Mu, Jesse and Goodman, Noah D.\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"zhao2025egrpo\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"E-GRPO: Entity-Aware Reward for Group Relative Policy Optimization\\\", \\\"authors\\\": \\\"Anonymous\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"dong2023raft\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\\\", \\\"authors\\\": \\\"Dong, Hanze and Xiong, Wei and Goyal, Deepanshu and Zhang, Yihan and Chow, Winni...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Transactions on Machine Learning Research\\\"}, {\\\"key\\\": \\\"ito2025mogrpo\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\", \\\"authors\\\": \\\"Ito, Taishu and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2509.22047\\\"}, {\\\"key\\\": \\\"li2025drift\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference\\\", \\\"authors\\\": \\\"Li, Jiazheng and Yan, Hanqi and He, Yulan\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 63rd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"liu2026gdpo\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"GDPO: Group Reward-Decoupled Normalization Policy Optimization for Multi-Reward RL Optimization\\\", \\\"authors\\\": \\\"Liu, Shih-Yang and others\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2601.05242\\\"}, {\\\"key\\\": \\\"liu2025drgrpo\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Understanding R1-Zero-Like Training: A Critical Perspective\\\", \\\"authors\\\": \\\"Liu, Zichen and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Conference on Language Modeling\\\"}, {\\\"key\\\": \\\"yu2025dapo\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\", \\\"authors\\\": \\\"Yu, Qiying and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.14476\\\"}, {\\\"key\\\": \\\"zhang2024infuse\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Fine-Grained Natural Language Inference Based Faithfulness Evaluation for Diverse Summarisation Tasks\\\", \\\"authors\\\": \\\"Zhang, Huajian and Xu, Yumo and Perez-Beltrachini, Laura\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 18th Conference of the European Chapter of the Association fo...\\\"}, {\\\"key\\\": \\\"chen2025dragrpo\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\\\", \\\"authors\\\": \\\"Chen, Xiwen and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2505.09655\\\"}, {\\\"key\\\": \\\"hu2025reinforcepp\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\\\", \\\"authors\\\": \\\"Hu, Yifan\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2501.03262\\\"}, {\\\"key\\\": \\\"wang2025rear\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\\\", \\\"authors\\\": \\\"Wang, Yutao and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: EMNLP 2025\\\"}, {\\\"key\\\": \\\"wang2025relprior\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"RelPrior: Relation as a Prior for LLM-based Document-Level Relation Extraction\\\", \\\"authors\\\": \\\"Wang, Yuxuan and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2511.08143\\\"}, {\\\"key\\\": \\\"zhang2025glidre\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"GLiDRE: Generalist Lightweight Model for Document-level Relation Extraction\\\", \\\"authors\\\": \\\"Zhang, Xiao and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.00757\\\"}, {\\\"key\\\": \\\"tang2025rsftppo\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Rejection Sampling Based Fine Tuning Secretly Performs PPO\\\", \\\"authors\\\": \\\"Tang, Yunhao and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 42nd International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"wang2025rullm\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\\\", \\\"authors\\\": \\\"Wang, Chenghao and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NLPCC 2025\\\"}, {\\\"key\\\": \\\"zhou2021atlop\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling\\\", \\\"authors\\\": \\\"Zhou, Wenxuan and Huang, Kevin and Ma, Tengyu and Huang, Jing\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"Aho:72\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"The Theory of Parsing, Translation and Compiling\\\", \\\"authors\\\": \\\"Alfred V. Aho and Jeffrey D. Ullman\\\", \\\"year\\\": \\\"1972\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"APA:83\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Publications Manual\\\", \\\"authors\\\": \\\"American Psychological Association\\\", \\\"year\\\": \\\"1983\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"Chandra:81\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Alternation\\\", \\\"authors\\\": \\\"Ashok K. Chandra and Dexter C. Kozen and Larry J. Stockmeyer\\\", \\\"year\\\": \\\"1981\\\", \\\"venue\\\": \\\"Journal of the Association for Computing Machinery\\\"}, {\\\"key\\\": \\\"andrew2007scalable\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scalable training of L1-regularized log-linear models\\\", \\\"authors\\\": \\\"Andrew, Galen and Gao, Jianfeng\\\", \\\"year\\\": \\\"2007\\\", \\\"venue\\\": \\\"Proceedings of the 24th International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"Gusfield:97\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Algorithms on Strings, Trees and Sequences\\\", \\\"authors\\\": \\\"Dan Gusfield\\\", \\\"year\\\": \\\"1997\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"rasooli-tetrault-2015\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Yara Parser: A Fast and Accurate Dependency Parser\\\", \\\"authors\\\": \\\"Mohammad Sadegh Rasooli and Joel R. Tetreault\\\", \\\"year\\\": \\\"2015\\\", \\\"venue\\\": \\\"Computing Research Repository\\\"}, {\\\"key\\\": \\\"Ando2005\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Framework for Learning Predictive Structures from Multiple Tasks and Unlabeled Data\\\", \\\"authors\\\": \\\"Ando, Rie Kubota and Zhang, Tong\\\", \\\"year\\\": \\\"2005\\\", \\\"venue\\\": \\\"Journal of Machine Learning Research\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"zhou2021atlop\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"autore2024\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"xu2024lmrc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"chen2025docksrag\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"yao2019docred\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"tan2022redocred\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"xiao2022sais\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"ma2023dreeam\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"yao2019docred\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zhou2021atlop\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"xiao2022sais\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ma2023dreeam\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"xie2022eider\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"autore2024\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"xu2024lmrc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wang2025relprior\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zhang2025glidre\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wang2025rullm\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"chen2025docksrag\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"yu2025dapo\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"liu2025drgrpo\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hu2025reinforcepp\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"chen2025dragrpo\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"liu2026gdpo\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ito2025mogrpo\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zhao2025egrpo\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"dai2025r1re\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wang2025rear\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"rafailov2023direct\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"jin2025rl_panacea\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gao2023scaling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"moskovitz2024constrained\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"li2025drift\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"zhang2024infuse\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"zelikman2022star\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 31, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"dong2023raft\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 32, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"tang2025rsftppo\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"xiao2022sais\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ma2023dreeam\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hu2022lora\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"yao2019docred\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"shao2024deepseekmath\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"rafailov2023direct\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zelikman2022star\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"yao2019docred\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"tan2022redocred\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hu2022lora\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ma2023dreeam\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ma2023dreeam\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 120, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"tan2022redocred\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 126, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ma2023dreeam\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 126, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wan2024genres\\\", \\\"file\\\": \\\"sections/limitations.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"tan2022redocred\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 138, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ma2023dreeam\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 141, \\\"command\\\": \\\"citep\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"autore2024\\\", \\\"title\\\": \\\"AutoRE: Document-Level Relation Extraction with Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"AutoRE: Document-Level Relation Extraction with Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=anonymous vs api=xue\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2025docksrag\\\", \\\"title\\\": \\\"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.305, \\\"matched_title\\\": \\\"Retrieval-Augmented Generation with Graphs (GraphRAG)\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.30 below threshold 0.82\\\"}, {\\\"key\\\": \\\"dai2025r1re\\\", \\\"title\\\": \\\"R1-RE: Cross-Domain Relation Extraction with RLVR\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.362, \\\"matched_title\\\": \\\"MR-UIE: multi-perspective reasoning with reinforcement learning for universal information extraction\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.36 below threshold 0.82\\\"}, {\\\"key\\\": \\\"gao2023scaling\\\", \\\"title\\\": \\\"Scaling Laws for Reward Model Overoptimization\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scaling Laws for Reward Model Overoptimization\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hu2022lora\\\", \\\"title\\\": \\\"LoRA: Low-Rank Adaptation of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LoRA: Low-Rank Adaptation of Large Language Models\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"jin2025rl_panacea\\\", \\\"title\\\": \\\"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.497, \\\"matched_title\\\": \\\"Visual Reasoning through Tool-supervised Reinforcement Learning\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.50 below threshold 0.82\\\"}, {\\\"key\\\": \\\"ma2023dreeam\\\", \\\"title\\\": \\\"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"moskovitz2024constrained\\\", \\\"title\\\": \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"rafailov2023direct\\\", \\\"title\\\": \\\"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"shao2024deepseekmath\\\", \\\"title\\\": \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.465, \\\"matched_title\\\": \\\"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.46 below threshold 0.82\\\"}, {\\\"key\\\": \\\"tan2022redocred\\\", \\\"title\\\": \\\"Revisiting DocRED: Addressing the False Negative Problem in Relation Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.981, \\\"matched_title\\\": \\\"Revisiting DocRED - Addressing the False Negative Problem in Relation Extraction\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wan2024genres\\\", \\\"title\\\": \\\"GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xiao2022sais\\\", \\\"title\\\": \\\"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xie2022eider\\\", \\\"title\\\": \\\"EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xu2024lmrc\\\", \\\"title\\\": \\\"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.957, \\\"matched_title\\\": \\\"LLM with Relation Classifier for Document-Level Relation Extraction\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yao2019docred\\\", \\\"title\\\": \\\"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zelikman2022star\\\", \\\"title\\\": \\\"STaR: Bootstrapping Reasoning With Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"STaR: Bootstrapping Reasoning With Reasoning\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhao2025egrpo\\\", \\\"title\\\": \\\"E-GRPO: Entity-Aware Reward for Group Relative Policy Optimization\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.283, \\\"matched_title\\\": \\\"Instruction Tuning for Large Language Models: A Survey\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.28 below threshold 0.82\\\"}, {\\\"key\\\": \\\"dong2023raft\\\", \\\"title\\\": \\\"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ito2025mogrpo\\\", \\\"title\\\": \\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.231, \\\"matched_title\\\": \\\"Reasoning on a Budget: Miniaturizing DeepSeek R1 with SFT-GRPO Alignment for Instruction-Tuned LLMs\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.23 below threshold 0.82\\\"}, {\\\"key\\\": \\\"li2025drift\\\", \\\"title\\\": \\\"Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"liu2026gdpo\\\", \\\"title\\\": \\\"GDPO: Group Reward-Decoupled Normalization Policy Optimization for Multi-Reward RL Optimization\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"liu2025drgrpo\\\", \\\"title\\\": \\\"Understanding R1-Zero-Like Training: A Critical Perspective\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding R1-Zero-Like Training: A Critical Perspective\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yu2025dapo\\\", \\\"title\\\": \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.31, \\\"matched_title\\\": \\\"OpenRLHF: A Ray-based Easy-to-use, Scalable and High-performance RLHF Framework\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.31 below threshold 0.82\\\"}, {\\\"key\\\": \\\"zhang2024infuse\\\", \\\"title\\\": \\\"Fine-Grained Natural Language Inference Based Faithfulness Evaluation for Diverse Summarisation Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Fine-Grained Natural Language Inference Based Faithfulness Evaluation for Diverse Summarisation Tasks\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2025dragrpo\\\", \\\"title\\\": \\\"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.488, \\\"matched_title\\\": \\\"MMR-GRPO: Accelerating GRPO-Style Training through Diversity-Aware Reward Reweighting\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.49 below threshold 0.82\\\"}, {\\\"key\\\": \\\"hu2025reinforcepp\\\", \\\"title\\\": \\\"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=hu vs api=jian\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025rear\\\", \\\"title\\\": \\\"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=wang vs api=luo\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025relprior\\\", \\\"title\\\": \\\"RelPrior: Relation as a Prior for LLM-based Document-Level Relation Extraction\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 0.829, \\\"matched_title\\\": \\\"Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=wang vs api=pi\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2025glidre\\\", \\\"title\\\": \\\"GLiDRE: Generalist Lightweight Model for Document-level Relation Extraction\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=zhang vs api=armingaud\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tang2025rsftppo\\\", \\\"title\\\": \\\"Rejection Sampling Based Fine Tuning Secretly Performs PPO\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.262, \\\"matched_title\\\": \\\"A Comprehensive Overview of Large Language Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.26 below threshold 0.82\\\"}, {\\\"key\\\": \\\"wang2025rullm\\\", \\\"title\\\": \\\"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.444, \\\"matched_title\\\": \\\"Automation and machine learning augmented by large language models in a catalysis study\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.44 below threshold 0.82\\\"}, {\\\"key\\\": \\\"zhou2021atlop\\\", \\\"title\\\": \\\"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"Aho:72\\\", \\\"title\\\": \\\"The Theory of Parsing, Translation and Compiling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.99, \\\"matched_title\\\": \\\"The Theory of Parsing, Translation, and Compiling\\\", \\\"matched_year\\\": \\\"1972\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"APA:83\\\", \\\"title\\\": \\\"Publications Manual\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.456, \\\"matched_title\\\": \\\"Publication Manual of the American Psychological Association\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.46 below threshold 0.82\\\"}, {\\\"key\\\": \\\"Chandra:81\\\", \\\"title\\\": \\\"Alternation\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.222, \\\"matched_title\\\": \\\"Dispersion and Absorption in Dielectrics I. Alternating Current Characteristics\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.22 below threshold 0.82\\\"}, {\\\"key\\\": \\\"andrew2007scalable\\\", \\\"title\\\": \\\"Scalable training of L1-regularized log-linear models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.422, \\\"matched_title\\\": \\\"Discriminative Log-Linear Grammars with Latent Variables\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.42 below threshold 0.82\\\"}, {\\\"key\\\": \\\"Gusfield:97\\\", \\\"title\\\": \\\"Algorithms on Strings, Trees and Sequences\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Algorithms on Strings, Trees and Sequences\\\", \\\"matched_year\\\": \\\"1997\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"rasooli-tetrault-2015\\\", \\\"title\\\": \\\"Yara Parser: A Fast and Accurate Dependency Parser\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Yara Parser: A Fast and Accurate Dependency Parser\\\", \\\"matched_year\\\": \\\"2015\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"Ando2005\\\", \\\"title\\\": \\\"A Framework for Learning Predictive Structures from Multiple Tasks and Unlabeled Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Framework for Learning Predictive Structures from Multiple Tasks and Unlabeled Data\\\", \\\"matched_year\\\": \\\"2005\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 40, \"total_citations\": 54, \"unique_cited_keys\": 33, \"orphan_bib\": 7, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 22, \"online_not_found\": 13, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [\"APA:83\", \"Aho:72\", \"Ando2005\", \"Chandra:81\", \"Gusfield:97\", \"andrew2007scalable\", \"rasooli-tetrault-2015\"], \"missing_bib\": [], \"orphan_count\": 7, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"autore2024\", \"type\": \"inproceedings\", \"title\": \"AutoRE: Document-Level Relation Extraction with Large Language Models\", \"authors\": \"Anonymous\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"chen2025docksrag\", \"type\": \"inproceedings\", \"title\": \"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning\", \"authors\": \"Xu and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the 42nd International Conference on Machine Learning\"}, {\"key\": \"dai2025r1re\", \"type\": \"article\", \"title\": \"R1-RE: Cross-Domain Relation Extraction with RLVR\", \"authors\": \"Dai, Runpeng and Zheng, Tong and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2507.04642\"}, {\"key\": \"gao2023scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling Laws for Reward Model Overoptimization\", \"authors\": \"Gao, Leo and Schulman, John and Hilton, Jacob\", \"year\": \"2023\", \"venue\": \"Proceedings of the 40th International Conference on Machine Learning\"}, {\"key\": \"hu2022lora\", \"type\": \"inproceedings\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"authors\": \"Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"jin2025rl_panacea\", \"type\": \"article\", \"title\": \"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs\", \"authors\": \"Jin, Hangzhan and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.16546\"}, {\"key\": \"ma2023dreeam\", \"type\": \"inproceedings\", \"title\": \"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\", \"authors\": \"Ma, Youmi and Wang, An and Okazaki, Naoaki\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: EACL 2023\"}, {\"key\": \"moskovitz2024constrained\", \"type\": \"inproceedings\", \"title\": \"Confronting Reward Model Overoptimization with Constrained RLHF\", \"authors\": \"Moskovitz, Ted and Singh, Aaditya K. and Strouse, DJ and Sandholm, Tuomas and Sa...\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"rafailov2023direct\", \"type\": \"inproceedings\", \"title\": \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\", \"authors\": \"Rafailov, Rafael and Sharma, Archit and Mitchell, Eric and Ermon, Stefano and Ma...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"shao2024deepseekmath\", \"type\": \"article\", \"title\": \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\", \"authors\": \"Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao an...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.03300\"}, {\"key\": \"tan2022redocred\", \"type\": \"inproceedings\", \"title\": \"Revisiting DocRED: Addressing the False Negative Problem in Relation Extraction\", \"authors\": \"Tan, Qingyu and Xu, Lu and Bing, Lidong and Ng, Hwee Tou and Aljunied, Sharifah ...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"wan2024genres\", \"type\": \"inproceedings\", \"title\": \"GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models\", \"authors\": \"Jiang, Pengcheng and Lin, Jiacheng and Wang, Zifeng and Sun, Jimeng and Han, Jia...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"xiao2022sais\", \"type\": \"inproceedings\", \"title\": \"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction\", \"authors\": \"Xiao, Yuxin and Zhang, Zecheng and Mao, Yuning and Yang, Carl and Han, Jiawei\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"xie2022eider\", \"type\": \"inproceedings\", \"title\": \"EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\", \"authors\": \"Xie, Yiqing and Shen, Jiaming and Li, Sha and Mao, Yuning and Han, Jiawei\", \"year\": \"2022\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2022\"}, {\"key\": \"xu2024lmrc\", \"type\": \"article\", \"title\": \"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\", \"authors\": \"Li, Xingzuo and Chen, Kehai and Long, Yunfei and Zhang, Min\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2408.13889\"}, {\"key\": \"yao2019docred\", \"type\": \"inproceedings\", \"title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"authors\": \"Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zheng...\", \"year\": \"2019\", \"venue\": \"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"zelikman2022star\", \"type\": \"inproceedings\", \"title\": \"STaR: Bootstrapping Reasoning With Reasoning\", \"authors\": \"Zelikman, Eric and Wu, Yuhuai and Mu, Jesse and Goodman, Noah D.\", \"year\": \"2022\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"zhao2025egrpo\", \"type\": \"inproceedings\", \"title\": \"E-GRPO: Entity-Aware Reward for Group Relative Policy Optimization\", \"authors\": \"Anonymous\", \"year\": \"2026\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"dong2023raft\", \"type\": \"article\", \"title\": \"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\", \"authors\": \"Dong, Hanze and Xiong, Wei and Goyal, Deepanshu and Zhang, Yihan and Chow, Winni...\", \"year\": \"2023\", \"venue\": \"Transactions on Machine Learning Research\"}, {\"key\": \"ito2025mogrpo\", \"type\": \"article\", \"title\": \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\", \"authors\": \"Ito, Taishu and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2509.22047\"}, {\"key\": \"li2025drift\", \"type\": \"inproceedings\", \"title\": \"Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference\", \"authors\": \"Li, Jiazheng and Yan, Hanqi and He, Yulan\", \"year\": \"2025\", \"venue\": \"Proceedings of the 63rd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"liu2026gdpo\", \"type\": \"article\", \"title\": \"GDPO: Group Reward-Decoupled Normalization Policy Optimization for Multi-Reward RL Optimization\", \"authors\": \"Liu, Shih-Yang and others\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2601.05242\"}, {\"key\": \"liu2025drgrpo\", \"type\": \"inproceedings\", \"title\": \"Understanding R1-Zero-Like Training: A Critical Perspective\", \"authors\": \"Liu, Zichen and others\", \"year\": \"2025\", \"venue\": \"Conference on Language Modeling\"}, {\"key\": \"yu2025dapo\", \"type\": \"article\", \"title\": \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\", \"authors\": \"Yu, Qiying and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.14476\"}, {\"key\": \"zhang2024infuse\", \"type\": \"inproceedings\", \"title\": \"Fine-Grained Natural Language Inference Based Faithfulness Evaluation for Diverse Summarisation Tasks\", \"authors\": \"Zhang, Huajian and Xu, Yumo and Perez-Beltrachini, Laura\", \"year\": \"2024\", \"venue\": \"Proceedings of the 18th Conference of the European Chapter of the Association fo...\"}, {\"key\": \"chen2025dragrpo\", \"type\": \"article\", \"title\": \"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\", \"authors\": \"Chen, Xiwen and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.09655\"}, {\"key\": \"hu2025reinforcepp\", \"type\": \"article\", \"title\": \"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\", \"authors\": \"Hu, Yifan\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2501.03262\"}, {\"key\": \"wang2025rear\", \"type\": \"inproceedings\", \"title\": \"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\", \"authors\": \"Wang, Yutao and others\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2025\"}, {\"key\": \"wang2025relprior\", \"type\": \"article\", \"title\": \"RelPrior: Relation as a Prior for LLM-based Document-Level Relation Extraction\", \"authors\": \"Wang, Yuxuan and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.08143\"}, {\"key\": \"zhang2025glidre\", \"type\": \"article\", \"title\": \"GLiDRE: Generalist Lightweight Model for Document-level Relation Extraction\", \"authors\": \"Zhang, Xiao and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.00757\"}, {\"key\": \"tang2025rsftppo\", \"type\": \"inproceedings\", \"title\": \"Rejection Sampling Based Fine Tuning Secretly Performs PPO\", \"authors\": \"Tang, Yunhao and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the 42nd International Conference on Machine Learning\"}, {\"key\": \"wang2025rullm\", \"type\": \"article\", \"title\": \"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\", \"authors\": \"Wang, Chenghao and others\", \"year\": \"2025\", \"venue\": \"NLPCC 2025\"}, {\"key\": \"zhou2021atlop\", \"type\": \"inproceedings\", \"title\": \"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling\", \"authors\": \"Zhou, Wenxuan and Huang, Kevin and Ma, Tengyu and Huang, Jing\", \"year\": \"2021\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"Aho:72\", \"type\": \"book\", \"title\": \"The Theory of Parsing, Translation and Compiling\", \"authors\": \"Alfred V. Aho and Jeffrey D. Ullman\", \"year\": \"1972\", \"venue\": \"\"}, {\"key\": \"APA:83\", \"type\": \"book\", \"title\": \"Publications Manual\", \"authors\": \"American Psychological Association\", \"year\": \"1983\", \"venue\": \"\"}, {\"key\": \"Chandra:81\", \"type\": \"article\", \"title\": \"Alternation\", \"authors\": \"Ashok K. Chandra and Dexter C. Kozen and Larry J. Stockmeyer\", \"year\": \"1981\", \"venue\": \"Journal of the Association for Computing Machinery\"}, {\"key\": \"andrew2007scalable\", \"type\": \"inproceedings\", \"title\": \"Scalable training of L1-regularized log-linear models\", \"authors\": \"Andrew, Galen and Gao, Jianfeng\", \"year\": \"2007\", \"venue\": \"Proceedings of the 24th International Conference on Machine Learning\"}, {\"key\": \"Gusfield:97\", \"type\": \"book\", \"title\": \"Algorithms on Strings, Trees and Sequences\", \"authors\": \"Dan Gusfield\", \"year\": \"1997\", \"venue\": \"\"}, {\"key\": \"rasooli-tetrault-2015\", \"type\": \"article\", \"title\": \"Yara Parser: A Fast and Accurate Dependency Parser\", \"authors\": \"Mohammad Sadegh Rasooli and Joel R. Tetreault\", \"year\": \"2015\", \"venue\": \"Computing Research Repository\"}, {\"key\": \"Ando2005\", \"type\": \"article\", \"title\": \"A Framework for Learning Predictive Structures from Multiple Tasks and Unlabeled Data\", \"authors\": \"Ando, Rie Kubota and Zhang, Tong\", \"year\": \"2005\", \"venue\": \"Journal of Machine Learning Research\"}], \"tex_citations\": [{\"key\": \"zhou2021atlop\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"citet\"}, {\"key\": \"autore2024\", \"file\": \"sections/introduction.tex\", \"line\": 4, \"command\": \"citet\"}, {\"key\": \"xu2024lmrc\", \"file\": \"sections/introduction.tex\", \"line\": 4, \"command\": \"citet\"}, {\"key\": \"chen2025docksrag\", \"file\": \"sections/introduction.tex\", \"line\": 4, \"command\": \"citet\"}, {\"key\": \"yao2019docred\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"citep\"}, {\"key\": \"tan2022redocred\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"citep\"}, {\"key\": \"xiao2022sais\", \"file\": \"sections/introduction.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"ma2023dreeam\", \"file\": \"sections/introduction.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"yao2019docred\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"citep\"}, {\"key\": \"zhou2021atlop\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"xiao2022sais\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"ma2023dreeam\", \"file\": \"sections/related_work.tex\", \"line\": 9, \"command\": \"citep\"}, {\"key\": \"xie2022eider\", \"file\": \"sections/related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"autore2024\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"xu2024lmrc\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"wang2025relprior\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"zhang2025glidre\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"wang2025rullm\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"chen2025docksrag\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"yu2025dapo\", \"file\": \"sections/related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"liu2025drgrpo\", \"file\": \"sections/related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"hu2025reinforcepp\", \"file\": \"sections/related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"chen2025dragrpo\", \"file\": \"sections/related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"liu2026gdpo\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"citep\"}, {\"key\": \"ito2025mogrpo\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"citep\"}, {\"key\": \"zhao2025egrpo\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citep\"}, {\"key\": \"dai2025r1re\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citep\"}, {\"key\": \"wang2025rear\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citep\"}, {\"key\": \"rafailov2023direct\", \"file\": \"sections/related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"jin2025rl_panacea\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"citep\"}, {\"key\": \"gao2023scaling\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"citep\"}, {\"key\": \"moskovitz2024constrained\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"citep\"}, {\"key\": \"li2025drift\", \"file\": \"sections/related_work.tex\", \"line\": 27, \"command\": \"citet\"}, {\"key\": \"zhang2024infuse\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"citet\"}, {\"key\": \"zelikman2022star\", \"file\": \"sections/related_work.tex\", \"line\": 31, \"command\": \"citet\"}, {\"key\": \"dong2023raft\", \"file\": \"sections/related_work.tex\", \"line\": 32, \"command\": \"citet\"}, {\"key\": \"tang2025rsftppo\", \"file\": \"sections/related_work.tex\", \"line\": 33, \"command\": \"citep\"}, {\"key\": \"xiao2022sais\", \"file\": \"sections/method.tex\", \"line\": 9, \"command\": \"citep\"}, {\"key\": \"ma2023dreeam\", \"file\": \"sections/method.tex\", \"line\": 9, \"command\": \"citep\"}, {\"key\": \"hu2022lora\", \"file\": \"sections/method.tex\", \"line\": 15, \"command\": \"citep\"}, {\"key\": \"yao2019docred\", \"file\": \"sections/method.tex\", \"line\": 15, \"command\": \"citep\"}, {\"key\": \"shao2024deepseekmath\", \"file\": \"sections/method.tex\", \"line\": 24, \"command\": \"citep\"}, {\"key\": \"rafailov2023direct\", \"file\": \"sections/method.tex\", \"line\": 27, \"command\": \"citep\"}, {\"key\": \"zelikman2022star\", \"file\": \"sections/method.tex\", \"line\": 30, \"command\": \"citep\"}, {\"key\": \"yao2019docred\", \"file\": \"sections/experiments.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"tan2022redocred\", \"file\": \"sections/experiments.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"hu2022lora\", \"file\": \"sections/experiments.tex\", \"line\": 14, \"command\": \"citep\"}, {\"key\": \"ma2023dreeam\", \"file\": \"sections/experiments.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"ma2023dreeam\", \"file\": \"sections/experiments.tex\", \"line\": 120, \"command\": \"citep\"}, {\"key\": \"tan2022redocred\", \"file\": \"sections/experiments.tex\", \"line\": 126, \"command\": \"citep\"}, {\"key\": \"ma2023dreeam\", \"file\": \"sections/experiments.tex\", \"line\": 126, \"command\": \"citep\"}, {\"key\": \"wan2024genres\", \"file\": \"sections/limitations.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"tan2022redocred\", \"file\": \"sections/appendix.tex\", \"line\": 138, \"command\": \"citep\"}, {\"key\": \"ma2023dreeam\", \"file\": \"sections/appendix.tex\", \"line\": 141, \"command\": \"citep\"}], \"online_verification\": [{\"key\": \"autore2024\", \"title\": \"AutoRE: Document-Level Relation Extraction with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"AutoRE: Document-Level Relation Extraction with Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=anonymous vs api=xue\"], \"note\": \"\"}, {\"key\": \"chen2025docksrag\", \"title\": \"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning\", \"status\": \"not_found\", \"confidence\": 0.305, \"matched_title\": \"Retrieval-Augmented Generation with Graphs (GraphRAG)\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\"}, {\"key\": \"dai2025r1re\", \"title\": \"R1-RE: Cross-Domain Relation Extraction with RLVR\", \"status\": \"not_found\", \"confidence\": 0.362, \"matched_title\": \"MR-UIE: multi-perspective reasoning with reinforcement learning for universal information extraction\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.36 below threshold 0.82\"}, {\"key\": \"gao2023scaling\", \"title\": \"Scaling Laws for Reward Model Overoptimization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scaling Laws for Reward Model Overoptimization\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hu2022lora\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jin2025rl_panacea\", \"title\": \"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs\", \"status\": \"not_found\", \"confidence\": 0.497, \"matched_title\": \"Visual Reasoning through Tool-supervised Reinforcement Learning\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.50 below threshold 0.82\"}, {\"key\": \"ma2023dreeam\", \"title\": \"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"moskovitz2024constrained\", \"title\": \"Confronting Reward Model Overoptimization with Constrained RLHF\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confronting Reward Model Overoptimization with Constrained RLHF\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"rafailov2023direct\", \"title\": \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shao2024deepseekmath\", \"title\": \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\", \"status\": \"not_found\", \"confidence\": 0.465, \"matched_title\": \"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.46 below threshold 0.82\"}, {\"key\": \"tan2022redocred\", \"title\": \"Revisiting DocRED: Addressing the False Negative Problem in Relation Extraction\", \"status\": \"verified\", \"confidence\": 0.981, \"matched_title\": \"Revisiting DocRED - Addressing the False Negative Problem in Relation Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wan2024genres\", \"title\": \"GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiao2022sais\", \"title\": \"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie2022eider\", \"title\": \"EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xu2024lmrc\", \"title\": \"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\", \"status\": \"verified\", \"confidence\": 0.957, \"matched_title\": \"LLM with Relation Classifier for Document-Level Relation Extraction\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yao2019docred\", \"title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zelikman2022star\", \"title\": \"STaR: Bootstrapping Reasoning With Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"STaR: Bootstrapping Reasoning With Reasoning\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhao2025egrpo\", \"title\": \"E-GRPO: Entity-Aware Reward for Group Relative Policy Optimization\", \"status\": \"not_found\", \"confidence\": 0.283, \"matched_title\": \"Instruction Tuning for Large Language Models: A Survey\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.28 below threshold 0.82\"}, {\"key\": \"dong2023raft\", \"title\": \"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ito2025mogrpo\", \"title\": \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\", \"status\": \"not_found\", \"confidence\": 0.231, \"matched_title\": \"Reasoning on a Budget: Miniaturizing DeepSeek R1 with SFT-GRPO Alignment for Instruction-Tuned LLMs\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.23 below threshold 0.82\"}, {\"key\": \"li2025drift\", \"title\": \"Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liu2026gdpo\", \"title\": \"GDPO: Group Reward-Decoupled Normalization Policy Optimization for Multi-Reward RL Optimization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liu2025drgrpo\", \"title\": \"Understanding R1-Zero-Like Training: A Critical Perspective\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Understanding R1-Zero-Like Training: A Critical Perspective\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yu2025dapo\", \"title\": \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\", \"status\": \"not_found\", \"confidence\": 0.31, \"matched_title\": \"OpenRLHF: A Ray-based Easy-to-use, Scalable and High-performance RLHF Framework\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.31 below threshold 0.82\"}, {\"key\": \"zhang2024infuse\", \"title\": \"Fine-Grained Natural Language Inference Based Faithfulness Evaluation for Diverse Summarisation Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Fine-Grained Natural Language Inference Based Faithfulness Evaluation for Diverse Summarisation Tasks\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2025dragrpo\", \"title\": \"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\", \"status\": \"not_found\", \"confidence\": 0.488, \"matched_title\": \"MMR-GRPO: Accelerating GRPO-Style Training through Diversity-Aware Reward Reweighting\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.49 below threshold 0.82\"}, {\"key\": \"hu2025reinforcepp\", \"title\": \"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=hu vs api=jian\"], \"note\": \"\"}, {\"key\": \"wang2025rear\", \"title\": \"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=wang vs api=luo\"], \"note\": \"\"}, {\"key\": \"wang2025relprior\", \"title\": \"RelPrior: Relation as a Prior for LLM-based Document-Level Relation Extraction\", \"status\": \"mismatch\", \"confidence\": 0.829, \"matched_title\": \"Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=wang vs api=pi\"], \"note\": \"\"}, {\"key\": \"zhang2025glidre\", \"title\": \"GLiDRE: Generalist Lightweight Model for Document-level Relation Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=zhang vs api=armingaud\"], \"note\": \"\"}, {\"key\": \"tang2025rsftppo\", \"title\": \"Rejection Sampling Based Fine Tuning Secretly Performs PPO\", \"status\": \"not_found\", \"confidence\": 0.262, \"matched_title\": \"A Comprehensive Overview of Large Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.26 below threshold 0.82\"}, {\"key\": \"wang2025rullm\", \"title\": \"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\", \"status\": \"not_found\", \"confidence\": 0.444, \"matched_title\": \"Automation and machine learning augmented by large language models in a catalysis study\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.44 below threshold 0.82\"}, {\"key\": \"zhou2021atlop\", \"title\": \"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"Aho:72\", \"title\": \"The Theory of Parsing, Translation and Compiling\", \"status\": \"verified\", \"confidence\": 0.99, \"matched_title\": \"The Theory of Parsing, Translation, and Compiling\", \"matched_year\": \"1972\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"APA:83\", \"title\": \"Publications Manual\", \"status\": \"not_found\", \"confidence\": 0.456, \"matched_title\": \"Publication Manual of the American Psychological Association\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.46 below threshold 0.82\"}, {\"key\": \"Chandra:81\", \"title\": \"Alternation\", \"status\": \"not_found\", \"confidence\": 0.222, \"matched_title\": \"Dispersion and Absorption in Dielectrics I. Alternating Current Characteristics\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.22 below threshold 0.82\"}, {\"key\": \"andrew2007scalable\", \"title\": \"Scalable training of L1-regularized log-linear models\", \"status\": \"not_found\", \"confidence\": 0.422, \"matched_title\": \"Discriminative Log-Linear Grammars with Latent Variables\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.42 below threshold 0.82\"}, {\"key\": \"Gusfield:97\", \"title\": \"Algorithms on Strings, Trees and Sequences\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Algorithms on Strings, Trees and Sequences\", \"matched_year\": \"1997\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"rasooli-tetrault-2015\", \"title\": \"Yara Parser: A Fast and Accurate Dependency Parser\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Yara Parser: A Fast and Accurate Dependency Parser\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"Ando2005\", \"title\": \"A Framework for Learning Predictive Structures from Multiple Tasks and Unlabeled Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Framework for Learning Predictive Structures from Multiple Tasks and Unlabeled Data\", \"matched_year\": \"2005\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f3bdcc85-a04d-4a1f-9884-806000416bbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 71_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 1（方法与实验严谨性）  ### Venue 信息 - **目标 venue**: EMNLP 2026 Main Conference Long Paper (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **页数限制**: 正文 8 页 + unlimited refere…",
  "leafUuid": "564b57b5-4c90-4398-b4ac-7511a3d51f49",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c"
}
```

---

### Runtime record

_source line 72_

```json
{
  "type": "ai-title",
  "aiTitle": "Review evidence-grounded information extraction paper",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c"
}
```

---

### Assistant

_source line 73 · 2026-05-18T06:51:23.649Z_

<details><summary>Logged reasoning block</summary>

```text
Good, reference verification is done. I noted several issues:
1. 7 orphan bib entries (template artifacts like Aho:72, APA:83, etc.) - not a big deal
2. 5 author mismatches in bib entries (autore2024, hu2025reinforcepp, wang2025rear, wang2025relprior, zhang2025glidre) - some have wrong first authors
3. Several entries not found in OpenAlex (could be very recent preprints)

Now let me compile the full review. I have all the information I need.

Let me now write the comprehensive review and post it to the Director.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "564b57b5-4c90-4398-b4ac-7511a3d51f49",
  "isSidechain": false,
  "requestId": "req_011Cb9bEc1GHL6oTip6ooPbf",
  "type": "assistant",
  "uuid": "dd890558-4896-4435-af19-ca7d945bd84c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VziRnUJi53e2mMvzPaJUue",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11515,
      "cache_read_input_tokens": 60378,
      "output_tokens": 279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11515,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 279,
          "cache_read_input_tokens": 60378,
          "cache_creation_input_tokens": 11515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11515
          },
          "type": "message"
        }
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

_source line 74 · 2026-05-18T06:51:24.249Z_

引用验证完成。现在撰写完整审稿意见并提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd890558-4896-4435-af19-ca7d945bd84c",
  "isSidechain": false,
  "requestId": "req_011Cb9bEc1GHL6oTip6ooPbf",
  "type": "assistant",
  "uuid": "7709f9e6-e017-4757-9b03-48f0f003e0f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VziRnUJi53e2mMvzPaJUue",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11515,
      "cache_read_input_tokens": 60378,
      "output_tokens": 279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11515,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 279,
          "cache_read_input_tokens": 60378,
          "cache_creation_input_tokens": 11515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11515
          },
          "type": "message"
        }
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

_source line 75 · 2026-05-18T06:51:24.985Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01H9S5cP8NRJLpsnfMTPYQzq`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7709f9e6-e017-4757-9b03-48f0f003e0f9",
  "isSidechain": false,
  "requestId": "req_011Cb9bEc1GHL6oTip6ooPbf",
  "type": "assistant",
  "uuid": "71618ba7-0e4c-4f3e-a478-b3f837a6b498",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VziRnUJi53e2mMvzPaJUue",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11515,
      "cache_read_input_tokens": 60378,
      "output_tokens": 279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11515,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 279,
          "cache_read_input_tokens": 60378,
          "cache_creation_input_tokens": 11515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11515
          },
          "type": "message"
        }
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

_source line 76 · 2026-05-18T06:51:24.988Z_

<details><summary>↩ Tool result · `toolu_01H9S5cP8NRJLpsnfMTPYQzq`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__review_reviewer_post_to_director"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71618ba7-0e4c-4f3e-a478-b3f837a6b498",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "7e6f8876-62ba-40dd-a286-ac1e09e55fb2",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__review_reviewer_post_to_director"
    ],
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "71618ba7-0e4c-4f3e-a478-b3f837a6b498",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-18T06:53:43.116Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01JbhANiaunytRDkzMA95fNJ`</summary>

```json
{
  "text": "## Reviewer 1 审稿意见 — 方法与实验严谨性\n\n**论文**: \"Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\"\n**目标 Venue**: EMNLP 2026 Main Conference Long Paper (ARR May 2026 cycle)\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 研究问题有价值、实验覆盖面广，但核心 claim 的统计支撑不足，多个关键实验存在混淆变量，且全部结果仅在 dev set 上报告，距离 Main Conference 的标准有明显差距。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心 claim（decoupling spectrum、non-monotonic scaling）的实验设计存在混淆变量，统计检验缺失，EDCR 方法级相关性仅基于 6 个数据点 |\n| Excitement | 3.5/5 | 研究问题（LLM 时代 DocRE 的证据可验证性 vs 抽取精度权衡）切中实际需求，decoupling spectrum 概念有启发性 |\n| Overall Assessment | 3.0/5 | 适合 Findings；需补充统计检验、解混淆 GRPO 实验、增加 test set 结果方可达 Conference 水平 |\n| Reproducibility | 3/5 | 超参数基本报告完整，但 prompt template、entity mention 处理细节缺失；NLI 模型指定但 CED 聚合公式的细节不完整 |\n| Reviewer Confidence | 4/5 | 熟悉 DocRE、RL alignment、NLI-based evaluation 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] GRPO 实验存在严重混淆变量，无法支撑 decoupling spectrum 的因果推断\n\n- 具体位置：§4.3 Table 2；§3.3 GRPO paragraph\n- 问题：GRPO QLoRA (G=4, 4-bit) 与 GRPO bf16 (G=8, full-precision) 同时改变了**两个变量**：量化精度和 group size。论文将 catastrophic collapse 归因于\"4-bit quantization constrains the effective parameter space\"（§4.3 第二段），但无法排除 G=4 vs G=8 的影响。需要至少两个额外实验点：GRPO QLoRA G=8 和 GRPO bf16 G=4，才能解耦 quantization 和 group size 的效果。\n- 为什么影响接收：Decoupling spectrum 是论文的第一核心贡献（Contribution 2），如果 GRPO catastrophic collapse 的归因不成立，整个 spectrum 叙事的因果链就断了。论文在 Introduction 第 29-30 行明确声称\"QLoRA acts as a catastrophic amplifier of the underlying optimization conflict rather than its root cause\"，这是一个因果性 claim，但实验设计无法支撑。\n- 建议修改方向：补充 GRPO bf16 G=4 和 GRPO QLoRA G=8 实验；或将因果性表述降级为观察性表述（\"we observe that the combination of QLoRA and smaller group size correlates with...\"）。\n\n**N2** [critical] 全部结果仅在 dev set 上报告，test set 结果缺失\n\n- 具体位置：§4.1 Metrics 段最后一句 \"All primary results use the development set; test set submission is pending\"；Limitations §7 第一句\n- 问题：对于一篇声称\"85+ experimental configurations\"的系统性实证研究，没有任何 test set 结果是严重缺陷。DocRED test set 有公开 leaderboard（CodaLab），提交并获取结果是标准做法。Dev set 可能导致超参数间接过拟合，尤其在多轮实验迭代中。\n- 为什么影响接收：ARR soundness 标准要求\"sufficient support for all of its claims\"。论文在 Abstract 和 Introduction 中的数字（+4.92pp, 50.50 vs 50.51 等）全部基于 dev set，不能视为最终性能指标。审稿人无法判断这些结论是否在 test set 上成立。\n- 建议修改方向：至少对 main results（Table 1 的 SFT / RSFT CED）和 scaling results（Table 3）提交 DocRED test set 评估。如果 test set 结果与 dev set 有较大偏差，需要更新叙事。\n\n**N3** [critical] SFT baseline 缺少多 seed 方差，+4.92pp 改进缺乏统计显著性检验\n\n- 具体位置：Table 1；§4.2 第一段\n- 问题：RSFT CED 报告了 4-seed 均值 44.66±0.49，但 SFT baseline 仅有单 seed 结果 (39.74)。没有 SFT 的方差估计，无法判断 +4.92pp 的改进是否统计显著。假设 SFT 方差与 RSFT 类似（~0.49），+4.92pp 很可能显著；但 SFT 可能有更大方差（因为没有 CED 筛选的稳定化效果）。论文全文没有进行任何统计显著性检验（t-test、bootstrap、paired permutation test）。\n- 为什么影响接收：这是论文的核心数字（出现在 Abstract、Introduction Contribution 4、Conclusion），如果不具备统计意义，所有下游结论都不可靠。\n- 建议修改方向：(1) 对 SFT baseline 补充至少 3 个 seed 的结果；(2) 对所有主要对比进行 paired bootstrap 或 t-test；(3) 报告 p-value 和 confidence interval。\n\n**N4** [critical] \"Non-monotonic\" scaling pattern 仅基于 3 个数据点，over-interpreted\n\n- 具体位置：§4.4 Table 3；Introduction 第 31-33 行；Abstract 第 13 行\n- 问题：Scale-dependent evidence tax 的 non-monotonic claim 基于 Qwen3 的 3 个规模点（1.7B: +8.04, 4B: -7.47, 8B: -0.28）。3 个点无法区分 non-monotonic pattern 与噪声或单点异常。特别是 1.7B 的 +8.04pp \"benefit\" 有严重的替代解释：论文自己在 Limitations 中承认\"44.4% of outputs exhibit repetitive patterns\"（§7 第 5 句），说明 1.7B 模型的 no-evidence 输出质量可能因 repetition 而被人为压低，evidence generation 的\"benefit\"可能仅仅是因为它迫使模型产生更长、更结构化的输出从而减少重复。此外，Abstract 中声称的\"+8pp Ign-F1 benefit\"在正文 §4.4 中被修正为\"On a fair evaluation subset... this benefit is +6.2 points\"，但这个 fair subset 的细节几乎没有交代。\n- 为什么影响接收：Scale-dependent evidence tax 是 Contribution 3，也是论文标题中\"Scaling\"一词的核心支撑。如果 non-monotonic claim 不成立，论文的独特贡献大幅缩水。\n- 建议修改方向：(1) 增加至少 1 个中间规模点（如 Qwen3-2.5B 或其他 ~3B 模型）验证 non-monotonicity；(2) 详细报告 1.7B \"fair evaluation subset\" 的构建方法和完整结果；(3) 对 1.7B 的 repetition 问题做 controlled analysis（如加 repetition penalty 后重新测 no-evidence baseline）；(4) 或将 claim 降级为\"observed pattern across three scales\"而非\"non-monotonic\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] EDCR 方法级相关性 (ρ=-0.965) 仅基于 6 个数据点，统计意义存疑\n\n- 具体位置：§3.5 第 64 行；§6 Analysis 第一段；Table 2\n- 问题：Table 2 共 6 行（GRPO QLoRA, GRPO bf16, DPO 1ep, DPO 3ep, SFT, RSFT），Spearman ρ=-0.965 在 n=6 时 critical value at α=0.05 约为 0.886，因此虽然统计显著但 power 极低，且结果对单个点高度敏感。GRPO QLoRA 是一个极端 outlier（EDCR=0.9876, Rel-F1=0.0138），移除该点后相关性可能大幅下降。此外，DPO 3-epoch 使用了\"pre-D076 evaluation protocol\"（Table 2 footnote），与其他行不在同一评估标准下，进一步削弱相关性分析的可比性。\n- 建议：(1) 报告去掉 GRPO QLoRA outlier 后的相关性；(2) 要么统一评估 protocol，要么将 DPO 3ep 从相关性计算中移除并标注清楚；(3) 考虑增加更多实验配置（如不同 KL coefficient 的 GRPO、不同 β 的 DPO）来增强样本量。\n\n**W2** [warning] \"1.7B RSFT matches 8B SFT\" claim 基于单 seed，差异仅 0.01pp\n\n- 具体位置：§4.4 Table 3 最后一句；Introduction Contribution 4；Abstract 第 14 行\n- 问题：1.7B RSFT (50.50) vs 8B SFT (50.51) 差异 0.01pp，两者均为单 seed 结果（Table 8 caption：\"single seed for other scales\"）。在没有方差估计的情况下，声称\"matches\"在统计上没有意义。任何合理的 seed variance 都远超 0.01pp。这个 claim 在 Abstract 和 Introduction 中被重复强调，但证据极弱。\n- 建议：补充 1.7B RSFT 和 8B SFT 各 3-4 seeds 的结果，报告 confidence interval；或将 claim 改为\"approaches\"而非\"matches\"。\n\n**W3** [warning] CED 与 flat-NLI 差异仅 0.02pp，contrastive component 的贡献未被证明\n\n- 具体位置：§3.4 最后一段；§6 Ablation 段；Appendix Table 6\n- 问题：CED (Rel-F1 0.4563) vs flat-NLI (0.4561)，差异 0.02pp，且 flat-NLI 仅有 2 seeds（Appendix §8）。论文承认\"CED and flat-NLI produce comparable RSFT outcomes\"但仍将 CED 作为默认选择，理由是\"interpretable per-triple discrimination scores\"。然而论文没有任何实验展示这种 interpretability 带来的实际价值。CED 的 contrastive component 增加了方法复杂度但没有带来可测量的改进，这削弱了 CED 作为方法贡献的意义。\n- 建议：(1) flat-NLI 补充到 4 seeds 以做公平对比；(2) 如果差异仍不显著，诚实报告 contrastive component 可能不是必要的；(3) 或提供 case study 展示 CED 的 per-triple discrimination 在实际 error analysis 中如何优于 flat-NLI。\n\n**W4** [warning] Baseline 对比不完整，缺少关键参照系\n\n- 具体位置：§4.2 Table 1；§4.6 最后一段\n- 问题：(1) 缺少与 encoder-based evidence methods (SAIS, DREEAM, EIDER) 在相同 evaluation protocol 下的直接对比。论文在 §4.6 提到 DREEAM 的 joint Evi-F1 为 54.01%，而本文最佳为 ~36%，但这个对比被放在 Appendix 中一笔带过。(2) 缺少与其他 LLM-based DocRE 方法（AutoRE、LMRC 等，均在 Related Work 中讨论）的抽取性能对比。(3) Post-hoc evidence 仅测试了 BM25，没有测试更强的 learned retriever。\n- 建议：在 main results 中增加 SAIS/DREEAM 的数字作为参照（即使不同 protocol，也应在 Table 中注明并讨论差距来源）；增加至少一个 LLM-based DocRE baseline 的抽取性能对比。\n\n**W5** [warning] RSFT ablation 缺少 random selection baseline\n\n- 具体位置：§6 Ablation 段；Appendix §8\n- 问题：RSFT 消融比较了 CED vs flat-NLI 和 k=1 vs k=3，但缺少一个关键 baseline：random selection（从 8 个 candidate 中随机选 1 个作为训练数据）。没有这个 baseline，无法确定 RSFT 的改进是来自\"quality-based selection\"还是简单的\"data augmentation + selection\"效应（即使随机选择也可能因为 sampling diversity 带来改进）。\n- 建议：增加 random-k=1 baseline；如果 random 也有不错的改进，那 CED scoring 的贡献需要重新评估。\n\n**W6** [warning] GRPO/DPO 超参数探索不足\n\n- 具体位置：§3.3；Appendix Table 5\n- 问题：GRPO 仅测试 KL=0.01，DPO 仅测试 β=0.1。在 RL/preference optimization 文献中，KL 系数和 β 对 reward hacking 和 performance tradeoff 有显著影响（Gao et al., 2023; Moskovitz et al., 2024 均被论文引用）。如果 GRPO 在更大 KL penalty 下不 collapse，或 DPO 在更小 β 下不 degrade，decoupling spectrum 的结论需要修改。\n- 建议：至少对 GRPO 测试 KL ∈ {0.001, 0.01, 0.1} 和 DPO 测试 β ∈ {0.01, 0.1, 0.5}，或承认当前结论受限于特定超参数设置。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 1 格式不一致：Rel-F1 使用小数 (0.4049)，Evi-F1 使用百分比 (79.86)，EDCR 使用小数 (0.6982)。全表应统一。\n- Appendix 中有 7 个 orphan bib entries（Aho:72, APA:83, Ando2005, Chandra:81, Gusfield:97, andrew2007scalable, rasooli-tetrault-2015），疑似 ACL 模板遗留，应清理。\n- 引用 `autore2024` 的作者标注为 \"Anonymous\"，但该论文已正式发表（ACL 2024 System Demos），第一作者为 Xue 等人，应更新。类似地，`zhao2025egrpo`（E-GRPO）也标注 Anonymous。\n- 引用 `wang2025relprior`、`zhang2025glidre`、`hu2025reinforcepp`、`wang2025rear` 的第一作者与 OpenAlex 记录不匹配，需核实。\n- Appendix §14 Figure 4 caption 说\"93 relation types\"，但正文 §14 第一句说\"76 relation types with ≥5 evaluation samples\"，而 §4.1 说 DocRED 有 96 relation types。三个数字互相矛盾。\n- §4.3 DPO 3-epoch 的脚注提到\"pre-D076 evaluation protocol\"，未解释 D076 是什么。内部编号不应出现在投稿论文中。\n- §4.4 提到\"fair evaluation subset\"但未给出构建方法、样本量和完整结果。\n- RSFT 的 training samples 为 2,718（Table 5），但 §3.3 说\"9,042 training examples (37.3% acceptance rate)\"，数字不一致（9,042 × 37.3% ≠ 2,718；24,216 → 9,042 是 ~37.3%，但 Table 5 报告 2,718 training samples）。需要解释 9,042 candidates 如何变成 2,718 training samples。\n\n---\n\n## 主要优势\n\n1. **研究问题重要且定位精准**：LLM-based DocRE 缺乏 evidence grounding 是一个真实的实用性瓶颈，论文清晰地识别了 encoder-based evidence methods（SAIS/DREEAM）与 LLM-based extraction accuracy 之间的 gap（§1 第 16 行），问题动机有说服力。\n\n2. **实验覆盖面广**：跨 4 个模型规模、2 个模型家族、2 个数据集、3 种优化范式的系统性比较在 DocRE 文献中确实罕见。即使个别实验的统计严谨性不足，这种横向覆盖本身也有参考价值。\n\n3. **Decoupling spectrum 概念有启发性**：将 GRPO/DPO/RSFT 按 decoupling 严重程度排序的视角（Table 2）直观且有助于理解多目标生成任务中不同优化策略的行为差异。如果混淆变量问题得到修复，这将是一个有洞察力的贡献。\n\n4. **RSFT 效果稳定**：4-seed 结果方差较低（±0.49），跨数据集（DocRED +4.92pp, Re-DocRED +4.86pp）和跨模型家族（LLaMA +1.74pp）的改进模式一致（§4.6），说明 rejection sampling approach 的鲁棒性。\n\n5. **写作质量较好**：论文叙事结构清晰（问题→形式化→方法→实验→分析），Related Work 做了有效的 positioning（§2 区分了 encoder-based evidence 与 LLM-based generation 的结构性差异），不是简单的论文罗列。\n\n---\n\n## 缺失引用\n\n- **KGC/知识图谱补全视角**：论文讨论了 DocRE 但未引用知识图谱构建相关工作，考虑到 Introduction 明确提到\"knowledge graph construction\"作为下游应用。\n- **Multi-task learning / auxiliary loss 文献**：Evidence generation 作为辅助任务与 extraction 竞争 capacity 的分析框架，应引用 multi-task learning 的经典分析（如 Ruder 2017, Fifty et al. 2021 \"Efficiently Identifying Task Groupings for Multi-Task Learning\"）。\n- **Chain-of-thought / rationale generation**：Evidence generation 在概念上类似 CoT rationale generation，相关的 faithful reasoning 文献（如 Lanham et al. 2023 \"Measuring Faithfulness in Chain-of-Thought Reasoning\"）可以丰富讨论。\n\n---\n\n## 总结\n\n论文提出了一个有价值的研究问题，实验覆盖面令人印象深刻。但在方法论严谨性上有明显短板：核心实验存在未解耦的混淆变量（N1），全部结果缺少 test set 验证（N2），主要 claim 缺乏统计检验（N3），scaling claim 的数据点不足（N4）。这些问题的共同效果是：论文的 claim 强度系统性地超过了实验证据的支撑力度。如果能补充 test set 结果、解耦 GRPO 实验、增加统计检验，本文有潜力达到 Conference 水平。当前状态建议 Findings。",
  "reviewer_id": "1",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e6f8876-62ba-40dd-a286-ac1e09e55fb2",
  "isSidechain": false,
  "requestId": "req_011Cb9bFF4DF2LTJ6tQmsyLF",
  "type": "assistant",
  "uuid": "12652bf8-9b77-4a9f-a81f-73aa3d96765d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013y7Gc3SuZ4S5GExCmtdHTj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 71893,
      "output_tokens": 5998,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 592,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5998,
          "cache_read_input_tokens": 71893,
          "cache_creation_input_tokens": 592,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 592
          },
          "type": "message"
        }
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

_source line 78 · 2026-05-18T06:53:47.615Z_

<details><summary>↩ Tool result · `toolu_01JbhANiaunytRDkzMA95fNJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12652bf8-9b77-4a9f-a81f-73aa3d96765d",
  "isSidechain": false,
  "promptId": "ed82a757-9a1f-46c9-8a5a-57b2b3f883a8",
  "type": "user",
  "uuid": "84ca439b-c1ca-489f-af76-2a3b1618a182",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "12652bf8-9b77-4a9f-a81f-73aa3d96765d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "Review evidence-grounded information extraction paper",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c"
}
```

---

### Runtime record

_source line 80 · 2026-05-18T06:55:06.757Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T06:55:06.757Z",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "content": "[Round 1 审稿请求]:\n## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 2 审稿意见 — Round 1\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验规模可观，scale-dependent evidence tax 是有价值的发现，但核心诊断指标 EDCR 存在定义循环性，CED 的独立贡献被自身消融实验否定，且存在关键数据不一致。\n\n## Must-Fix 问题\n\n**N1** [critical] EDCR 与 Rel-F1 的相关性存在定义循环\n\n- EDCR = Evi-Recall_TP / Rel-Recall。当 Rel-Recall 极低时（如 GRPO QLoRA Rel-F1=0.0138），EDCR 机械性趋近 1.0，与 evidence 质量无关。论文报告 EDCR 与 Rel-F1 的 Spearman ρ = -0.965，但 Rel-Recall 本身是 Rel-F1 的组成部分，这一相关性部分由定义构造而非经验发现。\n- 建议：(1) 报告 p 值；(2) 提供 EDCR 相对于简单替代指标的增量诊断价值；(3) 对分母效应做敏感性分析。\n\n**N2** [critical] CED 与 flat-NLI 几乎无差异，削弱方法贡献\n\n- CED 和 flat-NLI 的 Rel-F1 差距仅 0.02pp。论文承认 \"CED's contrastive design does not substantially outperform simpler NLI scoring\"，但仍将 CED 作为独立贡献。消融否定了 CED 的量化优势。\n- 建议：将 CED 降级为可选评分函数，将贡献定位为 \"NLI-based quality filtering for RSFT\"。\n\n**N3** [critical] RSFT 训练数据量存在明确的数值矛盾\n\n- Section 3.3 说 \"9,042 training examples (37.3% acceptance rate)\"，Appendix Table 4 说 \"Training samples: 2,718\"。9,042 vs 2,718 有 3.3 倍差距且不可调和。\n- 建议：检查并统一这两个数字。\n\n**N4** [critical] 仅 Dev Set 结果，无 Test Set 提交\n\n- 所有实验均在 DocRED dev set 上报告，test set 提交为 \"pending\"。\n\n## Should-Fix 问题\n\n**W1** [warning] 指标格式严重不一致\n- Ign-F1 百分比格式（39.74），Rel-F1 小数格式（0.4049），Evi-F1 百分比（79.86）。\n\n**W2** [warning] 引用数量偏低且多条 bib 条目不完整\n- 32 篇引用（EMNLP long paper 通常 40-60 篇），15/32 条 \"and others\"，2 条 Anonymous。\n\n**W3** [warning] 1.7B Evidence Benefit 的解释缺乏充分支撑\n- \"implicit regularization\" 解释是推测性的，无实验支撑；\"fair evaluation subset\" 未详细定义。\n\n**W4** [warning] Multi-seed 覆盖不均匀\n- 4B 有 4-seed，1.7B/8B/LLaMA 为单 seed 或 2 seed。\n\n**W5** [warning] Related Work 缺少重要相关方向\n- 缺少 multi-task learning / task interference 文献、self-consistency 范式、与 encoder-based 方法的直接数值比较。\n\n**W6** [warning] \"pre-D076 evaluation protocol\" 未解释\n\n## 缺失引用\n1. Standley et al. (2020) \"Which Tasks Should Be Learned Together in Multi-Task Learning?\"\n2. Yu et al. (2020) \"Gradient Surgery for Multi-Task Learning\"\n3. Wang et al. (2023) \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\"\n\n## 主要优势\n1. 实验规模和系统性\n2. Scale-dependent evidence tax 是有意思的发现\n3. 问题定义有价值\n4. Decoupling spectrum 的诊断价值\n5. 写作质量整体良好\n6. RSFT \"discrete selection avoids gradient-based trade-off\" 洞察有一般性意义"
}
```

---

### Runtime record

_source line 81 · 2026-05-18T06:55:06.758Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T06:55:06.758Z",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c"
}
```

---

## Round 2

2 recorded events

### User

_source line 82 · 2026-05-18T06:55:06.747Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84ca439b-c1ca-489f-af76-2a3b1618a182",
  "isSidechain": false,
  "promptId": "c2b0b06b-7f60-47a7-bf5b-c3cbb11dcf24",
  "type": "user",
  "isMeta": true,
  "uuid": "305e3a9d-0933-4945-85cf-a9943ce5c285",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 83 · 2026-05-18T06:55:06.747Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "305e3a9d-0933-4945-85cf-a9943ce5c285",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "cc121cff-1032-4468-b83b-3de0fdd66d91",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "6410a6f0-4a9c-4369-b20a-2bdbc6ca8ae5",
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

5 recorded events

### User

_source line 84 · 2026-05-18T06:55:06.841Z_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

# Reviewer 2 审稿意见 — Round 1

**Overall**: 3.0 (Findings)
**一句话总结**: 实验规模可观，scale-dependent evidence tax 是有价值的发现，但核心诊断指标 EDCR 存在定义循环性，CED 的独立贡献被自身消融实验否定，且存在关键数据不一致。

## Must-Fix 问题

**N1** [critical] EDCR 与 Rel-F1 的相关性存在定义循环

- EDCR = Evi-Recall_TP / Rel-Recall。当 Rel-Recall 极低时（如 GRPO QLoRA Rel-F1=0.0138），EDCR 机械性趋近 1.0，与 evidence 质量无关。论文报告 EDCR 与 Rel-F1 的 Spearman ρ = -0.965，但 Rel-Recall 本身是 Rel-F1 的组成部分，这一相关性部分由定义构造而非经验发现。
- 建议：(1) 报告 p 值；(2) 提供 EDCR 相对于简单替代指标的增量诊断价值；(3) 对分母效应做敏感性分析。

**N2** [critical] CED 与 flat-NLI 几乎无差异，削弱方法贡献

- CED 和 flat-NLI 的 Rel-F1 差距仅 0.02pp。论文承认 "CED's contrastive design does not substantially outperform simpler NLI scoring"，但仍将 CED 作为独立贡献。消融否定了 CED 的量化优势。
- 建议：将 CED 降级为可选评分函数，将贡献定位为 "NLI-based quality filtering for RSFT"。

**N3** [critical] RSFT 训练数据量存在明确的数值矛盾

- Section 3.3 说 "9,042 training examples (37.3% acceptance rate)"，Appendix Table 4 说 "Training samples: 2,718"。9,042 vs 2,718 有 3.3 倍差距且不可调和。
- 建议：检查并统一这两个数字。

**N4** [critical] 仅 Dev Set 结果，无 Test Set 提交

- 所有实验均在 DocRED dev set 上报告，test set 提交为 "pending"。

## Should-Fix 问题

**W1** [warning] 指标格式严重不一致
- Ign-F1 百分比格式（39.74），Rel-F1 小数格式（0.4049），Evi-F1 百分比（79.86）。

**W2** [warning] 引用数量偏低且多条 bib 条目不完整
- 32 篇引用（EMNLP long paper 通常 40-60 篇），15/32 条 "and others"，2 条 Anonymous。

**W3** [warning] 1.7B Evidence Benefit 的解释缺乏充分支撑
- "implicit regularization" 解释是推测性的，无实验支撑；"fair evaluation subset" 未详细定义。

**W4** [warning] Multi-seed 覆盖不均匀
- 4B 有 4-seed，1.7B/8B/LLaMA 为单 seed 或 2 seed。

**W5** [warning] Related Work 缺少重要相关方向
- 缺少 multi-task learning / task interference 文献、self-consistency 范式、与 encoder-based 方法的直接数值比较。

**W6** [warning] "pre-D076 evaluation protocol" 未解释

## 缺失引用
1. Standley et al. (2020) "Which Tasks Should Be Learned Together in Multi-Task Learning?"
2. Yu et al. (2020) "Gradient Surgery for Multi-Task Learning"
3. Wang et al. (2023) "Self-Consistency Improves Chain of Thought Reasoning in Language Models"

## 主要优势
1. 实验规模和系统性
2. Scale-dependent evidence tax 是有意思的发现
3. 问题定义有价值
4. Decoupling spectrum 的诊断价值
5. 写作质量整体良好
6. RSFT "discrete selection avoids gradient-based trade-off" 洞察有一般性意义

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc121cff-1032-4468-b83b-3de0fdd66d91",
  "isSidechain": false,
  "promptId": "c2b0b06b-7f60-47a7-bf5b-c3cbb11dcf24",
  "type": "user",
  "uuid": "d2e79d4a-1149-4444-8bdf-7874c7d4d2e1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-18T06:55:33.041Z_

<details><summary>Logged reasoning block</summary>

```text
The Review Director is asking me to respond to Reviewer 2's review point by point, using [AGREE] or [REBUT] format with evidence from the paper.

Let me go through each issue carefully.

**R2-N1**: EDCR definitional circularity with Rel-F1
- I raised a similar concern in my own review (W1) about the 6 data points and the GRPO QLoRA outlier. R2 makes a stronger point about definitional circularity: since EDCR has Rel-Recall in the denominator, and Rel-F1 is a function of Rel-Recall and Rel-Precision, there IS a mathematical relationship baked into the correlation. 

This is a valid point I should AGREE with.

**R2-N2**: CED vs flat-NLI no difference
- I raised this as W3 in my review. I agree with this point.

**R2-N3**: RSFT training data numerical contradiction (9,042 vs 2,718)
- I flagged this in my minor issues. Let me think about this more carefully. The paper states 9,042 training examples from 24,216 candidates with a 37.3% acceptance rate, but I need to trace through the math to see where the 2,718 figure comes from and whether there's actually a contradiction or just different stages of the pipeline being described. The numbers still don't add up—9,042 is roughly 3× the 2,718 or 3,053 figures, which contradicts the k=1 claim. Maybe 9,042 counts individual triples while 2,718 counts documents, but the text uses "training examples" for both, so the discrepancy remains real. Moving on to the other issues: I agree with the dev-set-only concern, the metric format inconsistency, and the incomplete bibliography with orphan entries.

For the remaining points, I'm seeing valid critiques about the 1.7B evidence benefit lacking explanation, uneven multi-seed coverage across model sizes, missing related work on multi-task learning and chain-of-thought approaches, and the unexplained "pre-D076" notation. The citation count of 32 is on the low side for an EMNLP long paper, though that alone isn't disqualifying. I also notice the missing references to Standley et al. and Yu et al.

—these are reasonable additions to strengthen the related work section. Now I'll draft my response.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2e79d4a-1149-4444-8bdf-7874c7d4d2e1",
  "isSidechain": false,
  "requestId": "req_011Cb9bXbQmR3zrKsaNKnxtz",
  "type": "assistant",
  "uuid": "38c857cf-a1e6-4485-a053-ff1b4fe58a45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYCSCbRvkadPKjv8n2GNub",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1396,
      "cache_read_input_tokens": 78559,
      "output_tokens": 4527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1396,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4527,
          "cache_read_input_tokens": 78559,
          "cache_creation_input_tokens": 1396,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1396
          },
          "type": "message"
        }
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

_source line 86 · 2026-05-18T06:55:33.042Z_

逐条回应 Reviewer 2 的审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38c857cf-a1e6-4485-a053-ff1b4fe58a45",
  "isSidechain": false,
  "requestId": "req_011Cb9bXbQmR3zrKsaNKnxtz",
  "type": "assistant",
  "uuid": "846f0fbf-706d-4996-9d5d-c8f58ba39bcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYCSCbRvkadPKjv8n2GNub",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1396,
      "cache_read_input_tokens": 78559,
      "output_tokens": 4527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1396,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4527,
          "cache_read_input_tokens": 78559,
          "cache_creation_input_tokens": 1396,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1396
          },
          "type": "message"
        }
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

_source line 87 · 2026-05-18T06:56:42.032Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_011Dzxu8Ks9MdeSqfj2tefEd`</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: EDCR 与 Rel-F1 的定义循环性**\n\n同意，且我认为 R2 在此点上的分析比我自己的审稿更精确。我在 R1-W1 中指出了 n=6 样本量和 GRPO QLoRA outlier 的问题，但 R2 抓住了更根本的缺陷：EDCR 的分母包含 Rel-Recall，而 Rel-F1 本身是 Rel-Recall 和 Rel-Precision 的调和平均。ρ=-0.965 的相关性在数学上被定义关系部分预设了，不完全是经验发现。\n\n补充证据：§3.5 第 62-63 行的 EDCR 解释案例恰好说明了这个问题。论文说\"A model that correctly identifies a few triples and provides excellent evidence for them, but misses most triples entirely, will have high Evi-Recall_TP and low Rel-Recall, yielding a high EDCR\"。这本质上是在说：当 Rel-Recall 低时 EDCR 高。而 Rel-Recall 低自然对应 Rel-F1 低（在 precision 不极端变化的情况下）。因此 EDCR 与 Rel-F1 的负相关性部分是 tautological 的。\n\n进一步地，论文在 §6 声称 per-relation EDCR 与 Evi-F1 独立（ρ=-0.064, p=0.58），将此作为\"evidence quality and extraction ability are fully decoupled across relation types\"的证据（Appendix §14）。但\"不显著相关\"不等于\"fully decoupled\"，这是一个经典的\"absence of evidence ≠ evidence of absence\"错误，尤其在 76 个 relation types 中可能存在 power 不足的情况。\n\nR2 的三条建议（报告 p 值、增量诊断价值、敏感性分析）均合理。我补充建议：作者应在去除 GRPO QLoRA 极端点后重新计算相关性，并展示 EDCR 相对于更简单替代指标（如 Evi-F1 - Rel-F1 差值）是否提供额外诊断信息。\n\n**[AGREE] R2-N2: CED 与 flat-NLI 几乎无差异**\n\n完全同意，与我的 R1-W3 一致。论文的消融数据（Appendix §8）自己否定了 CED contrastive component 的量化贡献：CED Rel-F1 0.4563 vs flat-NLI 0.4561，差距 0.02pp。flat-NLI 仅有 2 seeds，但即便如此，0.02pp 的差距在任何合理的 variance 下都不可能显著。\n\nR2 的建议（将贡献定位为 \"NLI-based quality filtering for RSFT\"）比论文当前的表述更准确。论文在 §3.4 最后一段承认了这一点（\"CED and flat-NLI produce comparable RSFT outcomes\"），但 Introduction Contribution 列表仍然将 CED 作为独立贡献（Contribution 4: \"RSFT with NLI-based CED scoring\"）。叙事与数据之间存在张力。\n\n补充：§6 Analysis 的 \"CED granularity\" 段提到 sentence-level CED filtering 失败（Evi-F1 下降 7.7pp），这虽然是有趣的负面发现，但并不证明 CED 优于 flat-NLI，只说明 evidence 质量是 response-level 属性。这个发现对 CED 和 flat-NLI 同样适用。\n\n**[AGREE] R2-N3: RSFT 训练数据量数值矛盾**\n\n同意。我在小问题中也标记了这个不一致。详细分析矛盾：\n\n- §3.3 RSFT 段（method.tex 第 30 行）：N=8 candidates per document, top-k=1, \"From 24,216 candidate outputs, this selection yields 9,042 training examples (37.3% acceptance rate)\"\n- Appendix Table 5（appendix.tex 第 30 行）：Training samples = 2,718\n- DocRED 有 3,053 training documents（§4.1）\n\n数学核实：\n- 24,216 / 8 = 3,027 documents（与 3,053 接近，可能有些文档生成失败）\n- k=1 selection：应产生 ≤3,027 examples（每文档最多 1 个）\n- 9,042 / 3,027 ≈ 3.0，暗示实际使用了 k=3 而非 k=1\n- 2,718 < 3,027，可能是加了额外的 quality threshold 过滤\n\n这三个数字（9,042 / 2,718 / k=1 from 3,053 docs）互相矛盾，且无法通过合理解释调和。至少存在一处错误。这不仅是格式问题，它影响可复现性：研究者无法确定 RSFT 的实际训练数据规模。\n\n**[AGREE] R2-N4: 仅 Dev Set 结果**\n\n完全同意，与我的 R1-N2 一致。不再赘述。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 指标格式不一致**\n\n同意。我在小问题中也指出了这一点。Table 1 中 Ign-F1 = 39.74（百分比）、Rel-F1 = 0.4049（小数）、Evi-F1 = 79.86（百分比）混用确实造成阅读困难。补充一点：这种不一致贯穿全文，不仅限于 Table 1——Table 2、Table 3、Appendix Tables 均存在同样问题。\n\n**[AGREE] R2-W2: 引用数量偏低且 bib 条目不完整**\n\n部分同意。引用验证结果显示：33 unique cited keys，其中 7 条 orphan entries（ACL 模板遗留），5 条作者信息与 OpenAlex 不匹配（autore2024 标注 Anonymous 但实际第一作者为 Xue；wang2025relprior 第一作者应为 Pi 而非 Wang；zhang2025glidre 第一作者应为 Armingaud 而非 Zhang；hu2025reinforcepp 第一作者应为 Jian 而非 Hu；wang2025rear 第一作者应为 Luo 而非 Wang）。这些作者错误是实质性问题，需要修正。\n\n关于引用数量，33 篇确实偏低但不算致命——关键在于覆盖度而非数量。我在 R1 审稿中也指出了缺失的相关方向（multi-task learning、CoT faithful reasoning），R2 的缺失引用建议（Standley et al. 2020, Yu et al. 2020, Wang et al. 2023）合理。\n\n**[AGREE] R2-W3: 1.7B Evidence Benefit 解释缺乏支撑**\n\n强烈同意。这与我的 R1-N4 核心观点一致。\"Implicit regularization\" 是一个未经检验的假说（§4.4 第 93 行：\"We hypothesize that...\"），论文没有提供任何实验来区分 regularization 效应和 repetition-reduction 效应。Limitations 承认 1.7B 有 44.4% repetitive outputs（§7），这是一个已知的严重干扰因素。\"Fair evaluation subset\" 在 §4.4 中仅一句提及（\"On a fair evaluation subset that controls for output format effects, this benefit is +6.2 points\"），无任何细节。\n\n**[AGREE] R2-W4: Multi-seed 覆盖不均匀**\n\n同意。Appendix Table 8 caption 明确说\"single seed for other scales\"。4B 有 4 seeds，但 1.7B、8B、LLaMA-8B 均为单 seed。这意味着 Table 3 的 scaling analysis（论文 Contribution 3）中，4 行数据有 3 行基于单次实验。特别是 1.7B RSFT (50.50) 和 8B SFT (50.51) 的\"matches\"claim（我在 R1-W2 中详细分析）完全无统计意义。\n\n**[AGREE] R2-W5: Related Work 缺少重要相关方向**\n\n同意。论文的核心发现（evidence 和 extraction 在 gradient-based optimization 下竞争 capacity）本质上是一个 multi-task learning / task interference 问题，但 Related Work 没有引用 MTL 文献。这是一个显著遗漏，因为 MTL 文献中关于 task gradient conflict 的分析（如 R2 推荐的 Yu et al. 2020 \"Gradient Surgery\"）直接解释了为什么 GRPO/DPO 出现 decoupling 而 RSFT 不会。\n\n我在 R1 缺失引用中也指出了类似问题，补充推荐了 Ruder (2017) 和 Fifty et al. (2021) 作为 MTL 基础文献，以及 Lanham et al. (2023) 作为 faithful reasoning 文献。\n\n**[AGREE] R2-W6: \"pre-D076 evaluation protocol\" 未解释**\n\n同意，与我的小问题一致。Table 2 脚注中的 \"D076\" 是内部实验编号，在投稿论文中不应出现。更重要的是，DPO 3-epoch 使用了不同的 evaluation protocol 但被纳入了 decoupling spectrum 的相关性分析（Table 2），这污染了 ρ=-0.965 的计算。如果该数据点不可比，应从 spectrum 分析中移除或单独标注。\n\n---\n\n### 关于 R2 缺失引用的补充\n\nR2 推荐的三篇引用均合理：\n1. Standley et al. (2020) \"Which Tasks Should Be Learned Together\" — 直接相关于 evidence 和 extraction 作为两个 task 的 grouping/interference 分析\n2. Yu et al. (2020) \"Gradient Surgery\" — 解释了为什么 gradient-based methods (GRPO/DPO) 在多目标下失败而 selection-based methods (RSFT) 不会\n3. Wang et al. (2023) \"Self-Consistency\" — RSFT 的 sample-and-select 策略与 self-consistency 的 sample-and-vote 在概念上相近\n\n---\n\n### R1 与 R2 评分对比\n\n| 维度 | R1 | R2 | 差异说明 |\n|------|----|----|----------|\n| Soundness | 2.5 | 2.5 | 一致 |\n| Excitement | 3.5 | 3.0 | R1 认为问题定位稍好，但差异不大 |\n| Overall | 3.0 | 3.0 | 一致：Findings |\n| Reproducibility | 3 | 2.5 | R2 因数据不一致 (N3) 打分更低，合理 |\n\n**总体判断**：R2 的审稿与 R1 在核心问题上高度一致（dev-set-only、统计不足、CED 贡献存疑）。R2 在 EDCR 定义循环性（N1）和数据不一致（N3）上的分析比 R1 更尖锐。两份审稿共同指向同一个结论：论文 claim 强度系统性超过证据支撑力度，当前状态适合 Findings。",
  "reviewer_id": "1",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "846f0fbf-706d-4996-9d5d-c8f58ba39bcc",
  "isSidechain": false,
  "requestId": "req_011Cb9bXbQmR3zrKsaNKnxtz",
  "type": "assistant",
  "uuid": "33cdfd9b-d4c9-4be8-9d78-e08185e4bd80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYCSCbRvkadPKjv8n2GNub",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1396,
      "cache_read_input_tokens": 78559,
      "output_tokens": 4527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1396,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4527,
          "cache_read_input_tokens": 78559,
          "cache_creation_input_tokens": 1396,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1396
          },
          "type": "message"
        }
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

_source line 88 · 2026-05-18T06:56:46.152Z_

<details><summary>↩ Tool result · `toolu_011Dzxu8Ks9MdeSqfj2tefEd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33cdfd9b-d4c9-4be8-9d78-e08185e4bd80",
  "isSidechain": false,
  "promptId": "c2b0b06b-7f60-47a7-bf5b-c3cbb11dcf24",
  "type": "user",
  "uuid": "e265bac8-66b4-42cf-ad05-b99f89ca2d9b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "33cdfd9b-d4c9-4be8-9d78-e08185e4bd80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_reviewer_1_e5053957",
  "sessionId": "8cd9d2a1-e826-42f8-a029-f5ea0e7f221c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
