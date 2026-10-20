# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2 **你的审查侧重：新颖性 + 完整性** ### Venue 信息 - **目标**: EMNLP 2026（ARR May 2026 cycle）  — Part 1 of 2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-round-1-round-1-reviewer-2-venue-emnlp-2026-arr-may-2026-cycle-copy-2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/06/066bf1dd79521de681b2.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-18T09:56:31.842Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T09:56:31.842Z",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "content": "[Round 1 审稿请求]:\n## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性**\n\n### Venue 信息\n- **目标**: EMNLP 2026（ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n- **格式**: ACL 双栏模板，`\\usepackage[review]{acl}`，Long paper 8 页正文 + 无限制 references + Limitations/Ethics 不计页数\n- **匿名**: Double-blind\n- **附录**: 允许，不计页数，审稿人可选择是否阅读\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 论文路径\n- 主文件: `projects/gen-depth-contamination/docs/paper/main.tex`\n- 分节文件: introduction.tex, related_work.tex, method.tex, experiments_c1.tex, experiments_c3.tex, discussion.tex, conclusion.tex\n- 附录: appendix.tex, appendix_extended.tex\n- 表格: tables/ 目录下 6 个 .tex 文件\n\n### 审查重点（你的侧重）\n\n1. **新颖性评估**:\n   - 论文的核心贡献（generational depth estimation + K* discrimination boundary）相对现有工作的增量是否足够？\n   - 与最直接竞争者（如 Drayson et al. 2025 的 binary MGT detection + SIR filtering）相比，本文的 actionable output 在实践中是否真正不同？\n   - K*=2 的 \"one-wash laundering\" 发现是 positive result 还是 negative result？论文是否正确处理了这一点？\n   - 从 binary detection 到 ordinal depth estimation 的扩展是否有足够的技术深度？\n\n2. **论文定位与叙事**:\n   - 论文的身份是否清楚？（detection paper? measurement paper? curation paper?）\n   - Introduction 的故事线是否连贯？从问题到方法到贡献的逻辑链是否完整？\n   - Contribution list 的每条是否有对应 section/table 支撑？\n   - Abstract 是否在 30 秒内让审稿人判断出问题重要性、方法清晰度、贡献可信度？\n\n3. **Related Work 完整性**:\n   - 引用是否覆盖：model collapse 理论、synthetic text detection、data curation/selection、depth estimation 相关工作？\n   - 是否遗漏重要的近期工作（2024-2026）？\n   - Positioning 是否准确（与已有工作的关系和区别）？\n   - 引用密度是否达到 EMNLP 标准（通常 30-50+ references）？\n\n4. **写作质量**:\n   - 是否存在 AI 写作痕迹（em-dash、-ing phrases、过度分段、\"Furthermore/Moreover/Additionally\" 连用）？\n   - 专有名词和缩写是否首次出现时有定义？\n   - 图表信息密度是否足够？\n   - 主线统一性：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否讲同一个故事？\n\n5. **格式与合规**:\n   - Responsible NLP Research Checklist 是否需要？\n   - 匿名化是否彻底（包括 supplementary materials）？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary\n（2-3 句概述论文内容和主要贡献）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [severity: critical/major/minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有）\n\n## Overall Assessment\nScore: X.X\nConfidence: high/medium/low\n简要总评（2-3 句）\n```\n\n请独立审稿，严格客观。"
}
````

---


### Runtime record

_source line 2 · 2026-05-18T09:56:31.845Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T09:56:31.845Z",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


## Round 1

## Round 1

104 recorded events


### User

_source line 3 · 2026-05-18T09:56:31.879Z_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + 完整性**

### Venue 信息
- **目标**: EMNLP 2026（ARR May 2026 cycle）
- **Deadline**: 2026-05-25
- **格式**: ACL 双栏模板，`\usepackage[review]{acl}`，Long paper 8 页正文 + 无限制 references + Limitations/Ethics 不计页数
- **匿名**: Double-blind
- **附录**: 允许，不计页数，审稿人可选择是否阅读
- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

### 论文路径
- 主文件: `projects/gen-depth-contamination/docs/paper/main.tex`
- 分节文件: introduction.tex, related_work.tex, method.tex, experiments_c1.tex, experiments_c3.tex, discussion.tex, conclusion.tex
- 附录: appendix.tex, appendix_extended.tex
- 表格: tables/ 目录下 6 个 .tex 文件

### 审查重点（你的侧重）

1. **新颖性评估**:
   - 论文的核心贡献（generational depth estimation + K* discrimination boundary）相对现有工作的增量是否足够？
   - 与最直接竞争者（如 Drayson et al. 2025 的 binary MGT detection + SIR filtering）相比，本文的 actionable output 在实践中是否真正不同？
   - K*=2 的 "one-wash laundering" 发现是 positive result 还是 negative result？论文是否正确处理了这一点？
   - 从 binary detection 到 ordinal depth estimation 的扩展是否有足够的技术深度？

2. **论文定位与叙事**:
   - 论文的身份是否清楚？（detection paper? measurement paper? curation paper?）
   - Introduction 的故事线是否连贯？从问题到方法到贡献的逻辑链是否完整？
   - Contribution list 的每条是否有对应 section/table 支撑？
   - Abstract 是否在 30 秒内让审稿人判断出问题重要性、方法清晰度、贡献可信度？

3. **Related Work 完整性**:
   - 引用是否覆盖：model collapse 理论、synthetic text detection、data curation/selection、depth estimation 相关工作？
   - 是否遗漏重要的近期工作（2024-2026）？
   - Positioning 是否准确（与已有工作的关系和区别）？
   - 引用密度是否达到 EMNLP 标准（通常 30-50+ references）？

4. **写作质量**:
   - 是否存在 AI 写作痕迹（em-dash、-ing phrases、过度分段、"Furthermore/Moreover/Additionally" 连用）？
   - 专有名词和缩写是否首次出现时有定义？
   - 图表信息密度是否足够？
   - 主线统一性：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否讲同一个故事？

5. **格式与合规**:
   - Responsible NLP Research Checklist 是否需要？
   - 匿名化是否彻底（包括 supplementary materials）？

### 输出格式

请按以下结构输出审稿意见：

```
## Summary
（2-3 句概述论文内容和主要贡献）

## Strengths
S1. ...
S2. ...

## Weaknesses
W1. [severity: critical/major/minor] ...
W2. ...

## Questions
Q1. ...

## Missing References
（如有）

## Overall Assessment
Score: X.X
Confidence: high/medium/low
简要总评（2-3 句）
```

请独立审稿，严格客观。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "0929f3fd-1751-46e7-8eb1-2305ceb10e11",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-18T09:56:31.878Z_

```json
{
  "parentUuid": "0929f3fd-1751-46e7-8eb1-2305ceb10e11",
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
  "uuid": "f501b969-8580-4374-8abe-1682028579f2",
  "timestamp": "2026-05-18T09:56:31.878Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 5 · 2026-05-18T09:56:31.878Z_

```json
{
  "parentUuid": "f501b969-8580-4374-8abe-1682028579f2",
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
  "uuid": "c889bcb8-d236-4a05-b19a-caf965aff4b6",
  "timestamp": "2026-05-18T09:56:31.878Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 6 · 2026-05-18T09:56:31.878Z_

```json
{
  "parentUuid": "c889bcb8-d236-4a05-b19a-caf965aff4b6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "caaa9d42-ed2d-4062-b0a4-f25925c2fae4",
  "timestamp": "2026-05-18T09:56:31.878Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
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
  "aiTitle": "Review paper on generational depth contamination detection",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Assistant

_source line 8 · 2026-05-18T09:56:36.923Z_

我开始审稿。首先执行 session 启动初始化，然后搜索 EMNLP 2026 / ACL ARR 的 reviewer guidelines。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caaa9d42-ed2d-4062-b0a4-f25925c2fae4",
  "isSidechain": false,
  "requestId": "req_011Cb9qMyWeaP47mxMo1WvYu",
  "type": "assistant",
  "uuid": "621de07e-aa51-491b-9f1e-7f7efaac3929",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D6WVdp2Pdm22ekDksfxB7Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15715,
      "cache_read_input_tokens": 11841,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 174,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15715
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-18T09:56:38.002Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LbnHxSoS5zQdUkYwpMc6PB`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "621de07e-aa51-491b-9f1e-7f7efaac3929",
  "isSidechain": false,
  "requestId": "req_011Cb9qMyWeaP47mxMo1WvYu",
  "type": "assistant",
  "uuid": "bd123c4a-a94c-46b7-9250-bfb0b471755f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D6WVdp2Pdm22ekDksfxB7Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15715,
      "cache_read_input_tokens": 11841,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 174,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15715
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-18T09:56:38.008Z_

<details><summary>↩ Tool result · `toolu_01LbnHxSoS5zQdUkYwpMc6PB`</summary>

````text
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

```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

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
  "parentUuid": "bd123c4a-a94c-46b7-9250-bfb0b471755f",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "b0b941d4-8f6d-433b-862e-5620d833720f",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references",
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "bd123c4a-a94c-46b7-9250-bfb0b471755f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 11 · 2026-05-18T09:56:41.472Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by:
1. Searching for ACL ARR / EMNLP 2026 reviewer guidelines
2. Reading the main.tex file to understand the paper structure
3. Running verify_references to check citations

Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0b941d4-8f6d-433b-862e-5620d833720f",
  "isSidechain": false,
  "requestId": "req_011Cb9qNRxsbLbyZnCGrP5ZH",
  "type": "assistant",
  "uuid": "3ae2a706-477b-42a2-a915-8ade79ae316a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdvzEjcb97MVXRbejVJrc6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2171,
      "cache_read_input_tokens": 27556,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 339,
          "cache_read_input_tokens": 27556,
          "cache_creation_input_tokens": 2171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2171
          },
          "type": "message"
        }
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

_source line 12 · 2026-05-18T09:56:42.038Z_

开始并行执行：搜索 reviewer guidelines、阅读论文主文件、验证引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ae2a706-477b-42a2-a915-8ade79ae316a",
  "isSidechain": false,
  "requestId": "req_011Cb9qNRxsbLbyZnCGrP5ZH",
  "type": "assistant",
  "uuid": "0816a038-00c8-4c84-b369-ba19b36b1a7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdvzEjcb97MVXRbejVJrc6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2171,
      "cache_read_input_tokens": 27556,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 339,
          "cache_read_input_tokens": 27556,
          "cache_creation_input_tokens": 2171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2171
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-18T09:56:42.561Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C35hskBDofenV8THjF31He`</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0816a038-00c8-4c84-b369-ba19b36b1a7b",
  "isSidechain": false,
  "requestId": "req_011Cb9qNRxsbLbyZnCGrP5ZH",
  "type": "assistant",
  "uuid": "dbfc7f88-d81f-49ea-9ca7-65f8e56ab80f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdvzEjcb97MVXRbejVJrc6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2171,
      "cache_read_input_tokens": 27556,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 339,
          "cache_read_input_tokens": 27556,
          "cache_creation_input_tokens": 2171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2171
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-18T09:56:43.981Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bbvuac7UCrYre7rw1cgVbr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbfc7f88-d81f-49ea-9ca7-65f8e56ab80f",
  "isSidechain": false,
  "requestId": "req_011Cb9qNRxsbLbyZnCGrP5ZH",
  "type": "assistant",
  "uuid": "38cf8648-dc46-48fc-9914-ed6e413dfe7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdvzEjcb97MVXRbejVJrc6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2171,
      "cache_read_input_tokens": 27556,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 339,
          "cache_read_input_tokens": 27556,
          "cache_creation_input_tokens": 2171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2171
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-18T09:56:43.996Z_

<details><summary>↩ Tool result · `toolu_01Bbvuac7UCrYre7rw1cgVbr`</summary>

```text
1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	\usepackage[section]{placeins}
18	
19	\newcommand{\Kstar}{{K^*}}
20	\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
21	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
22	\newcommand{\auc}{\text{AUC}}
23	\newcommand{\jsd}{\text{JSD}}
24	
25	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	% === Abstract ===
33	\begin{abstract}
34	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
35	We measure the discrimination boundary $\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable) using 15 statistical features and an OBD-LightGBM classifier.
36	Across 9 model configurations (5 architecture families, 1B--14B), 3 source domains, and 4 decoding strategies, $\Kempirical \in \{1, 2, 3\}$ at $\theta{=}0.60$ (Cohen's $h{\approx}0.20$): general web text yields $\Kempirical{=}2$ as the dominant mode (8/9 configurations), while structured academic text (arXiv) yields $\Kempirical{=}3$, validated across five models and four architecture families.
37	A single generation pass suffices to render general web text indistinguishable from deeper synthetic content, a \emph{one-wash laundering} effect.
38	Generator-independent statistical features, computed via a fixed reference scorer, enable 80--92\% cross-model transfer among continuation-mode generators with scorer-invariant feature ordering ($\rho > 0.90$), and cross-scorer validation is consistent with $\Kempirical$ being governed by the generation process rather than the scoring model.
39	Downstream, domain-appropriate $\Kempirical$ correctly predicts optimal curation granularity: when contamination causes detectable quality loss, binary filtering minimizes degradation most effectively for web text.
40	\end{abstract}
41	
42	% === Section 1: Introduction ===
43	\input{introduction}
44	
45	% === Section 2: Related Work ===
46	\input{related_work}
47	
48	% === Section 3: Method ===
49	\input{method}
50	
51	% === Section 4: Experiments ===
52	\input{experiments_c1}
53	
54	% === Section 5: K*-Aware Data Filtering ===
55	\input{experiments_c3}
56	
57	% === Section 6: Discussion ===
58	\input{discussion}
59	
60	% === Section 7: Conclusion ===
61	\input{conclusion}
62	
63	% === Limitations (ACL required, unnumbered) ===
64	\clearpage
65	\section*{Limitations}
66	
67	Our findings are bounded by:
68	(1)~\emph{Scope}: model scale $\leq$14B (5 architecture families), English text (C4, Wikipedia, arXiv), four decoding strategies; arXiv $\Kempirical{=}3$ is confirmed with five models across four architecture families but with reduced sample size ($n{=}2{,}200$ per model).
69	(2)~\emph{Protocol}: prompt-chain (isolates text-intrinsic degradation); retrain-chain yields $\Kempirical{\geq}4$ (Pythia-1.4B LoRA; Appendix~\ref{sec:extended_limitations}), reflecting additional model-adaptation artifacts beyond text-level information loss.
70	(3)~\emph{Threshold}: $\Kempirical$ ranges from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; 8/9 configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (Mistral-7B: $\Kempirical{=}1$).
71	(4)~\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.002; cross-scorer validation drops this to $\Kempirical{=}1$ (Section~\ref{sec:transfer}). LLaMA-3.1-8B represents the most marginal $\Kempirical{=}2$ assignment, with the 1v2 CI lower bound within 0.3 percentage points of $\theta$.
72	(5)~\emph{Feature set}: the 15D features yield a feature-set-specific lower bound ($\Ktheory$ may be strictly higher); neural probe $\Kempirical$ is model-dependent ($3$ for Qwen, $2$ for Pythia/OLMo).
73	(6)~\emph{Segment length}: $\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \theta$); 512 tokens yields point estimate $\Kempirical{=}2$ but CI lower marginally below $\theta$ ($0.5979$), indicating the boundary weakens at longer generation lengths.
74	(7)~\emph{Curation applicability}: the filtering evaluation is validated on two architectures (Qwen2.5-1.5B-Instruct and Pythia-1.4B) with consistent strategy ordering (Appendix~\ref{sec:pythia_filtering}), though absolute improvement remains small and effect sizes diminish at lower contamination ratios (10--50\%; Appendix~\ref{sec:dose_response}).
75	Additional limitations (cross-model scoring sensitivity, feature ranking variability at the 1v2 boundary, structural composition confound analysis) appear in Appendix~\ref{sec:extended_limitations}.
76	
77	% === Ethics Statement (ACL required, unnumbered) ===
78	\section*{Ethics Statement}
79	
80	Generational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.
81	Our experiments use publicly available corpora (C4, Wikipedia, arXiv abstracts) and do not involve personally identifiable information.
82	A potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\auc \geq 0.96$ at 0v1) remains robust.
83	Code and generated corpora will be released upon acceptance to enable reproducibility.
84	
85	\bibliography{references}
86	
87	\input{appendix}
88	\input{appendix_extended}
89	
90	\end{document}
91	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38cf8648-dc46-48fc-9914-ed6e413dfe7f",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "94cd9331-ef23-4590-9dc4-175562bd524b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
      "content": "% EMNLP 2026 Main — ARR May 2026\n% Generational Depth Contamination\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\\usepackage[section]{placeins}\n\n\\newcommand{\\Kstar}{{K^*}}\n\\newcommand{\\Kempirical}{{K^*_{\\text{empirical}}}}\n\\newcommand{\\Ktheory}{{K^*_{\\text{theory}}}}\n\\newcommand{\\auc}{\\text{AUC}}\n\\newcommand{\\jsd}{\\text{JSD}}\n\n\\title{Generational Depth Estimation of Recursive Synthetic Text:\\\\Measuring the Discrimination Boundary}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% === Abstract ===\n\\begin{abstract}\nWeb-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.\nWe measure the discrimination boundary $\\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable) using 15 statistical features and an OBD-LightGBM classifier.\nAcross 9 model configurations (5 architecture families, 1B--14B), 3 source domains, and 4 decoding strategies, $\\Kempirical \\in \\{1, 2, 3\\}$ at $\\theta{=}0.60$ (Cohen's $h{\\approx}0.20$): general web text yields $\\Kempirical{=}2$ as the dominant mode (8/9 configurations), while structured academic text (arXiv) yields $\\Kempirical{=}3$, validated across five models and four architecture families.\nA single generation pass suffices to render general web text indistinguishable from deeper synthetic content, a \\emph{one-wash laundering} effect.\nGenerator-independent statistical features, computed via a fixed reference scorer, enable 80--92\\% cross-model transfer among continuation-mode generators with scorer-invariant feature ordering ($\\rho > 0.90$), and cross-scorer validation is consistent with $\\Kempirical$ being governed by the generation process rather than the scoring model.\nDownstream, domain-appropriate $\\Kempirical$ correctly predicts optimal curation granularity: when contamination causes detectable quality loss, binary filtering minimizes degradation most effectively for web text.\n\\end{abstract}\n\n% === Section 1: Introduction ===\n\\input{introduction}\n\n% === Section 2: Related Work ===\n\\input{related_work}\n\n% === Section 3: Method ===\n\\input{method}\n\n% === Section 4: Experiments ===\n\\input{experiments_c1}\n\n% === Section 5: K*-Aware Data Filtering ===\n\\input{experiments_c3}\n\n% === Section 6: Discussion ===\n\\input{discussion}\n\n% === Section 7: Conclusion ===\n\\input{conclusion}\n\n% === Limitations (ACL required, unnumbered) ===\n\\clearpage\n\\section*{Limitations}\n\nOur findings are bounded by:\n(1)~\\emph{Scope}: model scale $\\leq$14B (5 architecture families), English text (C4, Wikipedia, arXiv), four decoding strategies; arXiv $\\Kempirical{=}3$ is confirmed with five models across four architecture families but with reduced sample size ($n{=}2{,}200$ per model).\n(2)~\\emph{Protocol}: prompt-chain (isolates text-intrinsic degradation); retrain-chain yields $\\Kempirical{\\geq}4$ (Pythia-1.4B LoRA; Appendix~\\ref{sec:extended_limitations}), reflecting additional model-adaptation artifacts beyond text-level information loss.\n(3)~\\emph{Threshold}: $\\Kempirical$ ranges from 2--3 at $\\theta{=}0.55$ to 1 at $\\theta{=}0.70$; 8/9 configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (Mistral-7B: $\\Kempirical{=}1$).\n(4)~\\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.002; cross-scorer validation drops this to $\\Kempirical{=}1$ (Section~\\ref{sec:transfer}). LLaMA-3.1-8B represents the most marginal $\\Kempirical{=}2$ assignment, with the 1v2 CI lower bound within 0.3 percentage points of $\\theta$.\n(5)~\\emph{Feature set}: the 15D features yield a feature-set-specific lower bound ($\\Ktheory$ may be strictly higher); neural probe $\\Kempirical$ is model-dependent ($3$ for Qwen, $2$ for Pythia/OLMo).\n(6)~\\emph{Segment length}: $\\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \\theta$); 512 tokens yields point estimate $\\Kempirical{=}2$ but CI lower marginally below $\\theta$ ($0.5979$), indicating the boundary weakens at longer generation lengths.\n(7)~\\emph{Curation applicability}: the filtering evaluation is validated on two architectures (Qwen2.5-1.5B-Instruct and Pythia-1.4B) with consistent strategy ordering (Appendix~\\ref{sec:pythia_filtering}), though absolute improvement remains small and effect sizes diminish at lower contamination ratios (10--50\\%; Appendix~\\ref{sec:dose_response}).\nAdditional limitations (cross-model scoring sensitivity, feature ranking variability at the 1v2 boundary, structural composition confound analysis) appear in Appendix~\\ref{sec:extended_limitations}.\n\n% === Ethics Statement (ACL required, unnumbered) ===\n\\section*{Ethics Statement}\n\nGenerational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.\nOur experiments use publicly available corpora (C4, Wikipedia, arXiv abstracts) and do not involve personally identifiable information.\nA potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\\auc \\geq 0.96$ at 0v1) remains robust.\nCode and generated corpora will be released upon acceptance to enable reproducibility.\n\n\\bibliography{references}\n\n\\input{appendix}\n\\input{appendix_extended}\n\n\\end{document}\n",
      "numLines": 91,
      "startLine": 1,
      "totalLines": 91
    }
  },
  "sourceToolAssistantUUID": "38cf8648-dc46-48fc-9914-ed6e413dfe7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-18T09:56:44.416Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01MzbAtHiGEMVXVgxCfHhwSE`</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94cd9331-ef23-4590-9dc4-175562bd524b",
  "isSidechain": false,
  "requestId": "req_011Cb9qNRxsbLbyZnCGrP5ZH",
  "type": "assistant",
  "uuid": "8d6533a7-e940-440f-9bbb-db7ffb003529",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdvzEjcb97MVXRbejVJrc6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2171,
      "cache_read_input_tokens": 27556,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 339,
          "cache_read_input_tokens": 27556,
          "cache_creation_input_tokens": 2171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2171
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性**  ### Venue 信息 - **目标**: EMNLP 2026（ARR May 2026 cycle） - **Deadline**: 2026-05-25 - **格式**: ACL 双栏模板，`\\usepackage[review]{acl}`，Long…",
  "leafUuid": "8d6533a7-e940-440f-9bbb-db7ffb003529",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on generational depth contamination detection",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Tool result

_source line 19 · 2026-05-18T09:56:49.551Z_

<details><summary>↩ Tool result · `toolu_01C35hskBDofenV8THjF31He`</summary>

```text
Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, I found comprehensive information about ACL ARR 2026 reviewer guidelines and the review form criteria. Here's what I found:

## ARR Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

### Overall Assessment Scores

The review form includes scores ranging from 5 (Consider for Award - for papers potentially worthy of outstanding paper awards at *ACL conferences, up to top 2.5%) down to 1 (Do not resubmit - for papers that need to be fully redone or are not relevant to the *ACL community).

### Key Review Criteria Areas

The review form addresses several important areas:

1. **Ethics and Responsibility**: Reviewers are asked to review the ACL code of ethics and the ARR checklist submitted by authors, and to describe any ethical issues and the extent to which they have been acknowledged or addressed.

2. **Reproducibility**: Reviewers must assess whether there is enough information in the paper for readers to reproduce the main results, use results in future work, or build upon the work.

3. **Strengths and Weaknesses**: The form asks about major reasons to publish the paper (such as novel methodology, insightful empirical results, or theoretical analysis) and concerns about the paper that would favor prioritizing other high-quality papers.

4. **Excitement Factor**: Reviewers are asked to rate how exciting the paper is to them, considering factors like transformational insights, challenges to common assumptions, or impact on communities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbfc7f88-d81f-49ea-9ca7-65f8e56ab80f",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "27968bf3-effe-4eba-ab2e-3a2e65e1b655",
  "toolUseResult": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria",
    "results": [
      {
        "tool_use_id": "srvtoolu_01F4c9atiSVmqg5AVQ2pVngV",
        "content": [
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
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
            "title": "Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/incentives2026"
          },
          {
            "title": "Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
          },
          {
            "title": "aclrollingreview/cfp.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"
          },
          {
            "title": "aclrollingreview/reviewing.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about ACL ARR 2026 reviewer guidelines and the review form criteria. Here's what I found:\n\n## ARR Review Form Criteria\n\nThe main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.\n\n### Overall Assessment Scores\n\nThe review form includes scores ranging from 5 (Consider for Award - for papers potentially worthy of outstanding paper awards at *ACL conferences, up to top 2.5%) down to 1 (Do not resubmit - for papers that need to be fully redone or are not relevant to the *ACL community).\n\n### Key Review Criteria Areas\n\nThe review form addresses several important areas:\n\n1. **Ethics and Responsibility**: Reviewers are asked to review the ACL code of ethics and the ARR checklist submitted by authors, and to describe any ethical issues and the extent to which they have been acknowledged or addressed.\n\n2. **Reproducibility**: Reviewers must assess whether there is enough information in the paper for readers to reproduce the main results, use results in future work, or build upon the work.\n\n3. **Strengths and Weaknesses**: The form asks about major reasons to publish the paper (such as novel methodology, insightful empirical results, or theoretical analysis) and concerns about the paper that would favor prioritizing other high-quality papers.\n\n4. **Excitement Factor**: Reviewers are asked to rate how exciting the paper is to them, considering factors like transformational insights, challenges to common assumptions, or impact on communities."
    ],
    "durationSeconds": 6.986110652000002
  },
  "sourceToolAssistantUUID": "dbfc7f88-d81f-49ea-9ca7-65f8e56ab80f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 20 · 2026-05-18T09:57:17.553Z_

<details><summary>↩ Tool result · `toolu_01MzbAtHiGEMVXVgxCfHhwSE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 34, \"total_citations\": 53, \"unique_cited_keys\": 34, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 28, \"online_not_found\": 4, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"drayson2025\", \"type\": \"inproceedings\", \"title\": \"Machine-Generated Text Detection Prevents Language Model Collapse\", \"authors\": \"Drayson, George and Yilmaz, Emine and Lampos, Vasileios\", \"year\": \"2025\", \"venue\": \"Proceedings of EMNLP\"}, {\"key\": \"schaeffer2025position\", \"type\": \"inproceedings\", \"title\": \"Position: Model Collapse Does Not Mean What You Think\", \"authors\": \"Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi\", \"year\": \"2025\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"kazdan2025collapse\", \"type\": \"inproceedings\", \"title\": \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\", \"authors\": \"Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias ...\", \"year\": \"2025\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"mitchell2023detectgpt\", \"type\": \"inproceedings\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"authors\": \"Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher...\", \"year\": \"2023\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"basani2026diveye\", \"type\": \"article\", \"title\": \"DivEye: Diversity Boosts AI-Generated Text Detection\", \"authors\": \"Basani, Advik Raj and Chen, Pin-Yu\", \"year\": \"2026\", \"venue\": \"Transactions on Machine Learning Research\"}, {\"key\": \"zawalski2026codec\", \"type\": \"inproceedings\", \"title\": \"CoDeC: Detecting Data Contamination in LLMs via In-Context Learning\", \"authors\": \"Zawalski, Micha\\\\l and Boubdir, Meriem and Ba\\\\lazy, Klaudia and Nushi, Besmira an...\", \"year\": \"2026\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"zhang2024minkpp\", \"type\": \"inproceedings\", \"title\": \"Min-K\\\\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\", \"authors\": \"Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan\", \"year\": \"2024\", \"venue\": \"Proceedings of EMNLP\"}, {\"key\": \"shumailov2024collapse\", \"type\": \"article\", \"title\": \"AI Models Collapse When Trained on Recursively Generated Data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"alemohammad2024selfconsuming\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"dohmatob2024model\", \"type\": \"inproceedings\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kem...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"xie2023dsir\", \"type\": \"inproceedings\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"authors\": \"Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"tirumala2023d4\", \"type\": \"inproceedings\", \"title\": \"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\", \"authors\": \"Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"xie2023doremi\", \"type\": \"inproceedings\", \"title\": \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\", \"authors\": \"Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao a...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"hans2024binoculars\", \"type\": \"inproceedings\", \"title\": \"Spotting LLMs With Binoculars\", \"authors\": \"Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Ham...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"alain2017understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding Intermediate Layers Using Linear Classifier Probes\", \"authors\": \"Alain, Guillaume and Bengio, Yoshua\", \"year\": \"2017\", \"venue\": \"ICLR Workshop\"}, {\"key\": \"belinkov2022probing\", \"type\": \"article\", \"title\": \"Probing Classifiers: Promises, Shortcomings, and Advances\", \"authors\": \"Belinkov, Yonatan\", \"year\": \"2022\", \"venue\": \"Computational Linguistics\"}, {\"key\": \"bao2024fast\", \"type\": \"inproceedings\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"authors\": \"Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yu...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"frank2001ordinal\", \"type\": \"inproceedings\", \"title\": \"A Simple Approach to Ordinal Classification\", \"authors\": \"Frank, Eibe and Hall, Mark\", \"year\": \"2001\", \"venue\": \"Proceedings of ECML\"}, {\"key\": \"cheng2025beyond\", \"type\": \"inproceedings\", \"title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"authors\": \"Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM Web Conference (WWW)\"}, {\"key\": \"mehta2025beyond\", \"type\": \"article\", \"title\": \"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models\", \"authors\": \"Mehta, Sushant\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.17602\"}, {\"key\": \"sun2025aigt\", \"type\": \"inproceedings\", \"title\": \"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media\", \"authors\": \"Sun, Zhen and Zhang, Zongmin and Shen, Xinyue and Zhang, Ziyi and Liu, Yule and ...\", \"year\": \"2025\", \"venue\": \"Proceedings of ACL\"}, {\"key\": \"spennemann2025quantifying\", \"type\": \"article\", \"title\": \"Delving into: the Quantification of AI-Generated Content on the Internet (Synthetic Data)\", \"authors\": \"Spennemann, Dirk H. R.\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2504.08755\"}, {\"key\": \"dohmatob2025strong\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"wang2024semeval\", \"type\": \"inproceedings\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"authors\": \"Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov...\", \"year\": \"2024\", \"venue\": \"Proceedings of SemEval\"}, {\"key\": \"gerstgrasser2024model\", \"type\": \"inproceedings\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"authors\": \"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafae...\", \"year\": \"2024\", \"venue\": \"Proceedings of COLM\"}, {\"key\": \"guo2024curious\", \"type\": \"inproceedings\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"authors\": \"Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chloe\", \"year\": \"2024\", \"venue\": \"Findings of NAACL\"}, {\"key\": \"briesch2023selfconsuming\", \"type\": \"article\", \"title\": \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\", \"authors\": \"Briesch, Martin and Sobania, Dominik and Rothlauf, Franz\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2311.16822\"}, {\"key\": \"padmakumar2024writing\", \"type\": \"inproceedings\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"authors\": \"Padmakumar, Vishakh and He, He\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"krishna2023paraphrasing\", \"type\": \"inproceedings\", \"title\": \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\", \"authors\": \"Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and I...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"sadasivan2023detect\", \"type\": \"article\", \"title\": \"Can AI-Generated Text be Reliably Detected?\", \"authors\": \"Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, W...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2303.11156\"}, {\"key\": \"hao2025rewrite\", \"type\": \"inproceedings\", \"title\": \"Learning to Rewrite: Generalized LLM-Generated Text Detection\", \"authors\": \"Hao, Wei and Guan, Ran and Lu, Kangjie and Zhang, Shuai\", \"year\": \"2025\", \"venue\": \"Findings of ACL\"}, {\"key\": \"shi2025collapse\", \"type\": \"inproceedings\", \"title\": \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\", \"authors\": \"Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and ...\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"gambetta2024surplexity\", \"type\": \"article\", \"title\": \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\", \"authors\": \"Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2410.12341\"}, {\"key\": \"amin2025escaping\", \"type\": \"inproceedings\", \"title\": \"Escaping Collapse: The Strength of Weak Data for Large Language Model Training\", \"authors\": \"Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar a...\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems\"}], \"tex_citations\": [{\"key\": \"sun2025aigt\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"spennemann2025quantifying\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"shumailov2024collapse\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"dohmatob2024model\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"basani2026diveye\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"zhang2024minkpp\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"zawalski2026codec\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"shumailov2024collapse\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"alemohammad2024selfconsuming\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"schaeffer2025position\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"xie2023dsir\", \"file\": \"introduction.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"tirumala2023d4\", \"file\": \"introduction.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"drayson2025\", \"file\": \"introduction.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"shumailov2024collapse\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"alemohammad2024selfconsuming\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"dohmatob2024model\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"dohmatob2025strong\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"guo2024curious\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"padmakumar2024writing\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"briesch2023selfconsuming\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"schaeffer2025position\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"kazdan2025collapse\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gerstgrasser2024model\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"shi2025collapse\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"gambetta2024surplexity\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"amin2025escaping\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"kazdan2025collapse\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"mitchell2023detectgpt\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"bao2024fast\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"hans2024binoculars\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"basani2026diveye\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"zhang2024minkpp\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"cheng2025beyond\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"mehta2025beyond\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"wang2024semeval\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"sadasivan2023detect\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"krishna2023paraphrasing\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"hao2025rewrite\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"zawalski2026codec\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"xie2023dsir\", \"file\": \"related_work.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"tirumala2023d4\", \"file\": \"related_work.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"xie2023doremi\", \"file\": \"related_work.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"drayson2025\", \"file\": \"related_work.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"frank2001ordinal\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"alain2017understanding\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"belinkov2022probing\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"basani2026diveye\", \"file\": \"experiments_c1.tex\", \"line\": 167, \"command\": \"cite\"}, {\"key\": \"hans2024binoculars\", \"file\": \"experiments_c1.tex\", \"line\": 167, \"command\": \"cite\"}, {\"key\": \"drayson2025\", \"file\": \"experiments_c3.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"xie2023dsir\", \"file\": \"experiments_c3.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"shumailov2024collapse\", \"file\": \"experiments_c3.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"dohmatob2024model\", \"file\": \"experiments_c3.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"drayson2025\", \"file\": \"discussion.tex\", \"line\": 54, \"command\": \"citet\"}], \"online_verification\": [{\"key\": \"drayson2025\", \"title\": \"Machine-Generated Text Detection Prevents Language Model Collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Machine-generated text detection prevents language model collapse\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"schaeffer2025position\", \"title\": \"Position: Model Collapse Does Not Mean What You Think\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Position: Model Collapse Does Not Mean What You Think\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kazdan2025collapse\", \"title\": \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mitchell2023detectgpt\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"status\": \"not_found\", \"confidence\": 0.382, \"matched_title\": \"Regulating ChatGPT and other Large Generative AI Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.38 below threshold 0.82\"}, {\"key\": \"basani2026diveye\", \"title\": \"DivEye: Diversity Boosts AI-Generated Text Detection\", \"status\": \"not_found\", \"confidence\": 0.529, \"matched_title\": \"When AI Settles Down: Late-Stage Stability as a Signature of AI-Generated Text Detection\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.53 below threshold 0.82\"}, {\"key\": \"zawalski2026codec\", \"title\": \"CoDeC: Detecting Data Contamination in LLMs via In-Context Learning\", \"status\": \"not_found\", \"confidence\": 0.306, \"matched_title\": \"Factuality Challenges in the Era of Large Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.31 below threshold 0.82\"}, {\"key\": \"zhang2024minkpp\", \"title\": \"Min-K\\\\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shumailov2024collapse\", \"title\": \"AI Models Collapse When Trained on Recursively Generated Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"AI models collapse when trained on recursively generated data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"alemohammad2024selfconsuming\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Self-Consuming Generative Models go MAD\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=alemohammad vs api=casco-rodriguez\"], \"note\": \"\"}, {\"key\": \"dohmatob2024model\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie2023dsir\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Data Selection for Language Models via Importance Resampling\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tirumala2023d4\", \"title\": \"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie2023doremi\", \"title\": \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hans2024binoculars\", \"title\": \"Spotting LLMs With Binoculars\", \"status\": \"not_found\", \"confidence\": 0.552, \"matched_title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.55 below threshold 0.82\"}, {\"key\": \"alain2017understanding\", \"title\": \"Understanding Intermediate Layers Using Linear Classifier Probes\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Understanding intermediate layers using linear classifier probes\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"belinkov2022probing\", \"title\": \"Probing Classifiers: Promises, Shortcomings, and Advances\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Probing Classifiers: Promises, Shortcomings, and Advances\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bao2024fast\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"frank2001ordinal\", \"title\": \"A Simple Approach to Ordinal Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Simple Approach to Ordinal Classification\", \"matched_year\": \"2001\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cheng2025beyond\", \"title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mehta2025beyond\", \"title\": \"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=mehta vs api=sushant\"], \"note\": \"\"}, {\"key\": \"sun2025aigt\", \"title\": \"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"spennemann2025quantifying\", \"title\": \"Delving into: the Quantification of AI-Generated Content on the Internet (Synthetic Data)\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Delving into: the quantification of Ai-generated content on the internet (synthetic data)\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dohmatob2025strong\", \"title\": \"Strong Model Collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Strong Model Collapse\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2024semeval\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gerstgrasser2024model\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2024curious\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"briesch2023selfconsuming\", \"title\": \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"padmakumar2024writing\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"krishna2023paraphrasing\", \"title\": \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sadasivan2023detect\", \"title\": \"Can AI-Generated Text be Reliably Detected?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Can AI-Generated Text be Reliably Detected?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hao2025rewrite\", \"title\": \"Learning to Rewrite: Generalized LLM-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Learning to Rewrite: Generalized LLM-Generated Text Detection\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shi2025collapse\", \"title\": \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gambetta2024surplexity\", \"title\": \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"amin2025escaping\", \"title\": \"Escaping Collapse: The Strength of Weak Data for Large Language Model Training\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Escaping Collapse: The Strength of Weak Data for Large Language Model Training\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d6533a7-e940-440f-9bbb-db7ffb003529",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "b7e92992-4386-4197-bbee-6ffd1326cd50",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 34, \\\"total_citations\\\": 53, \\\"unique_cited_keys\\\": 34, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 28, \\\"online_not_found\\\": 4, \\\"online_mismatch\\\": 2}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"drayson2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Machine-Generated Text Detection Prevents Language Model Collapse\\\", \\\"authors\\\": \\\"Drayson, George and Yilmaz, Emine and Lampos, Vasileios\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of EMNLP\\\"}, {\\\"key\\\": \\\"schaeffer2025position\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Position: Model Collapse Does Not Mean What You Think\\\", \\\"authors\\\": \\\"Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of ICML\\\"}, {\\\"key\\\": \\\"kazdan2025collapse\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\", \\\"authors\\\": \\\"Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of ICML\\\"}, {\\\"key\\\": \\\"mitchell2023detectgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\", \\\"authors\\\": \\\"Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of ICML\\\"}, {\\\"key\\\": \\\"basani2026diveye\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"DivEye: Diversity Boosts AI-Generated Text Detection\\\", \\\"authors\\\": \\\"Basani, Advik Raj and Chen, Pin-Yu\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Transactions on Machine Learning Research\\\"}, {\\\"key\\\": \\\"zawalski2026codec\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CoDeC: Detecting Data Contamination in LLMs via In-Context Learning\\\", \\\"authors\\\": \\\"Zawalski, Micha\\\\\\\\l and Boubdir, Meriem and Ba\\\\\\\\lazy, Klaudia and Nushi, Besmira an...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Proceedings of ICLR\\\"}, {\\\"key\\\": \\\"zhang2024minkpp\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Min-K\\\\\\\\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\\\", \\\"authors\\\": \\\"Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of EMNLP\\\"}, {\\\"key\\\": \\\"shumailov2024collapse\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"AI Models Collapse When Trained on Recursively Generated Data\\\", \\\"authors\\\": \\\"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Nature\\\"}, {\\\"key\\\": \\\"alemohammad2024selfconsuming\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Consuming Generative Models Go MAD\\\", \\\"authors\\\": \\\"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of ICLR\\\"}, {\\\"key\\\": \\\"dohmatob2024model\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\", \\\"authors\\\": \\\"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kem...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of ICML\\\"}, {\\\"key\\\": \\\"xie2023dsir\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Data Selection for Language Models via Importance Resampling\\\", \\\"authors\\\": \\\"Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"tirumala2023d4\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\\\", \\\"authors\\\": \\\"Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"xie2023doremi\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\", \\\"authors\\\": \\\"Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao a...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"hans2024binoculars\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Spotting LLMs With Binoculars\\\", \\\"authors\\\": \\\"Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Ham...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of ICML\\\"}, {\\\"key\\\": \\\"alain2017understanding\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Understanding Intermediate Layers Using Linear Classifier Probes\\\", \\\"authors\\\": \\\"Alain, Guillaume and Bengio, Yoshua\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"ICLR Workshop\\\"}, {\\\"key\\\": \\\"belinkov2022probing\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Probing Classifiers: Promises, Shortcomings, and Advances\\\", \\\"authors\\\": \\\"Belinkov, Yonatan\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Computational Linguistics\\\"}, {\\\"key\\\": \\\"bao2024fast\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\", \\\"authors\\\": \\\"Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yu...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of ICLR\\\"}, {\\\"key\\\": \\\"frank2001ordinal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Simple Approach to Ordinal Classification\\\", \\\"authors\\\": \\\"Frank, Eibe and Hall, Mark\\\", \\\"year\\\": \\\"2001\\\", \\\"venue\\\": \\\"Proceedings of ECML\\\"}, {\\\"key\\\": \\\"cheng2025beyond\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\\\", \\\"authors\\\": \\\"Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the ACM Web Conference (WWW)\\\"}, {\\\"key\\\": \\\"mehta2025beyond\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models\\\", \\\"authors\\\": \\\"Mehta, Sushant\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2511.17602\\\"}, {\\\"key\\\": \\\"sun2025aigt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media\\\", \\\"authors\\\": \\\"Sun, Zhen and Zhang, Zongmin and Shen, Xinyue and Zhang, Ziyi and Liu, Yule and ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of ACL\\\"}, {\\\"key\\\": \\\"spennemann2025quantifying\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Delving into: the Quantification of AI-Generated Content on the Internet (Synthetic Data)\\\", \\\"authors\\\": \\\"Spennemann, Dirk H. R.\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2504.08755\\\"}, {\\\"key\\\": \\\"dohmatob2025strong\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Strong Model Collapse\\\", \\\"authors\\\": \\\"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of ICLR\\\"}, {\\\"key\\\": \\\"wang2024semeval\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\\\", \\\"authors\\\": \\\"Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of SemEval\\\"}, {\\\"key\\\": \\\"gerstgrasser2024model\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\", \\\"authors\\\": \\\"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafae...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of COLM\\\"}, {\\\"key\\\": \\\"guo2024curious\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\", \\\"authors\\\": \\\"Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chloe\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of NAACL\\\"}, {\\\"key\\\": \\\"briesch2023selfconsuming\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\", \\\"authors\\\": \\\"Briesch, Martin and Sobania, Dominik and Rothlauf, Franz\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2311.16822\\\"}, {\\\"key\\\": \\\"padmakumar2024writing\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Does Writing with Language Models Reduce Content Diversity?\\\", \\\"authors\\\": \\\"Padmakumar, Vishakh and He, He\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of ICLR\\\"}, {\\\"key\\\": \\\"krishna2023paraphrasing\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\\\", \\\"authors\\\": \\\"Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and I...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"sadasivan2023detect\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Can AI-Generated Text be Reliably Detected?\\\", \\\"authors\\\": \\\"Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, W...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2303.11156\\\"}, {\\\"key\\\": \\\"hao2025rewrite\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Learning to Rewrite: Generalized LLM-Generated Text Detection\\\", \\\"authors\\\": \\\"Hao, Wei and Guan, Ran and Lu, Kangjie and Zhang, Shuai\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of ACL\\\"}, {\\\"key\\\": \\\"shi2025collapse\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\", \\\"authors\\\": \\\"Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"gambetta2024surplexity\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\\\", \\\"authors\\\": \\\"Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2410.12341\\\"}, {\\\"key\\\": \\\"amin2025escaping\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Escaping Collapse: The Strength of Weak Data for Large Language Model Training\\\", \\\"authors\\\": \\\"Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar a...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"sun2025aigt\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"spennemann2025quantifying\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shumailov2024collapse\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dohmatob2024model\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"basani2026diveye\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2024minkpp\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zawalski2026codec\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shumailov2024collapse\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"alemohammad2024selfconsuming\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"schaeffer2025position\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xie2023dsir\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tirumala2023d4\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"drayson2025\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shumailov2024collapse\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"alemohammad2024selfconsuming\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dohmatob2024model\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dohmatob2025strong\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"guo2024curious\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"padmakumar2024writing\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"briesch2023selfconsuming\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"schaeffer2025position\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kazdan2025collapse\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gerstgrasser2024model\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shi2025collapse\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"gambetta2024surplexity\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"amin2025escaping\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"kazdan2025collapse\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"mitchell2023detectgpt\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"bao2024fast\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hans2024binoculars\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"basani2026diveye\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2024minkpp\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cheng2025beyond\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"mehta2025beyond\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2024semeval\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sadasivan2023detect\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"krishna2023paraphrasing\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hao2025rewrite\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zawalski2026codec\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xie2023dsir\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tirumala2023d4\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xie2023doremi\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"drayson2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"frank2001ordinal\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"alain2017understanding\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"belinkov2022probing\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"basani2026diveye\\\", \\\"file\\\": \\\"experiments_c1.tex\\\", \\\"line\\\": 167, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hans2024binoculars\\\", \\\"file\\\": \\\"experiments_c1.tex\\\", \\\"line\\\": 167, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"drayson2025\\\", \\\"file\\\": \\\"experiments_c3.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"xie2023dsir\\\", \\\"file\\\": \\\"experiments_c3.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"shumailov2024collapse\\\", \\\"file\\\": \\\"experiments_c3.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dohmatob2024model\\\", \\\"file\\\": \\\"experiments_c3.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"drayson2025\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 54, \\\"command\\\": \\\"citet\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"drayson2025\\\", \\\"title\\\": \\\"Machine-Generated Text Detection Prevents Language Model Collapse\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Machine-generated text detection prevents language model collapse\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"schaeffer2025position\\\", \\\"title\\\": \\\"Position: Model Collapse Does Not Mean What You Think\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Position: Model Collapse Does Not Mean What You Think\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kazdan2025collapse\\\", \\\"title\\\": \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mitchell2023detectgpt\\\", \\\"title\\\": \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.382, \\\"matched_title\\\": \\\"Regulating ChatGPT and other Large Generative AI Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.38 below threshold 0.82\\\"}, {\\\"key\\\": \\\"basani2026diveye\\\", \\\"title\\\": \\\"DivEye: Diversity Boosts AI-Generated Text Detection\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.529, \\\"matched_title\\\": \\\"When AI Settles Down: Late-Stage Stability as a Signature of AI-Generated Text Detection\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.53 below threshold 0.82\\\"}, {\\\"key\\\": \\\"zawalski2026codec\\\", \\\"title\\\": \\\"CoDeC: Detecting Data Contamination in LLMs via In-Context Learning\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.306, \\\"matched_title\\\": \\\"Factuality Challenges in the Era of Large Language Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.31 below threshold 0.82\\\"}, {\\\"key\\\": \\\"zhang2024minkpp\\\", \\\"title\\\": \\\"Min-K\\\\\\\\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"shumailov2024collapse\\\", \\\"title\\\": \\\"AI Models Collapse When Trained on Recursively Generated Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"AI models collapse when trained on recursively generated data\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"alemohammad2024selfconsuming\\\", \\\"title\\\": \\\"Self-Consuming Generative Models Go MAD\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Consuming Generative Models go MAD\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=alemohammad vs api=casco-rodriguez\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dohmatob2024model\\\", \\\"title\\\": \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xie2023dsir\\\", \\\"title\\\": \\\"Data Selection for Language Models via Importance Resampling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Data Selection for Language Models via Importance Resampling\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tirumala2023d4\\\", \\\"title\\\": \\\"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xie2023doremi\\\", \\\"title\\\": \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hans2024binoculars\\\", \\\"title\\\": \\\"Spotting LLMs With Binoculars\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.552, \\\"matched_title\\\": \\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.55 below threshold 0.82\\\"}, {\\\"key\\\": \\\"alain2017understanding\\\", \\\"title\\\": \\\"Understanding Intermediate Layers Using Linear Classifier Probes\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding intermediate layers using linear classifier probes\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"belinkov2022probing\\\", \\\"title\\\": \\\"Probing Classifiers: Promises, Shortcomings, and Advances\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Probing Classifiers: Promises, Shortcomings, and Advances\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"bao2024fast\\\", \\\"title\\\": \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"frank2001ordinal\\\", \\\"title\\\": \\\"A Simple Approach to Ordinal Classification\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Simple Approach to Ordinal Classification\\\", \\\"matched_year\\\": \\\"2001\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cheng2025beyond\\\", \\\"title\\\": \\\"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mehta2025beyond\\\", \\\"title\\\": \\\"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=mehta vs api=sushant\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sun2025aigt\\\", \\\"title\\\": \\\"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"spennemann2025quantifying\\\", \\\"title\\\": \\\"Delving into: the Quantification of AI-Generated Content on the Internet (Synthetic Data)\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Delving into: the quantification of Ai-generated content on the internet (synthetic data)\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dohmatob2025strong\\\", \\\"title\\\": \\\"Strong Model Collapse\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Strong Model Collapse\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2024semeval\\\", \\\"title\\\": \\\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gerstgrasser2024model\\\", \\\"title\\\": \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"guo2024curious\\\", \\\"title\\\": \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"briesch2023selfconsuming\\\", \\\"title\\\": \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"padmakumar2024writing\\\", \\\"title\\\": \\\"Does Writing with Language Models Reduce Content Diversity?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Does Writing with Language Models Reduce Content Diversity?\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"krishna2023paraphrasing\\\", \\\"title\\\": \\\"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sadasivan2023detect\\\", \\\"title\\\": \\\"Can AI-Generated Text be Reliably Detected?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Can AI-Generated Text be Reliably Detected?\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hao2025rewrite\\\", \\\"title\\\": \\\"Learning to Rewrite: Generalized LLM-Generated Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Learning to Rewrite: Generalized LLM-Generated Text Detection\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"shi2025collapse\\\", \\\"title\\\": \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gambetta2024surplexity\\\", \\\"title\\\": \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"amin2025escaping\\\", \\\"title\\\": \\\"Escaping Collapse: The Strength of Weak Data for Large Language Model Training\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Escaping Collapse: The Strength of Weak Data for Large Language Model Training\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 34, \"total_citations\": 53, \"unique_cited_keys\": 34, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 28, \"online_not_found\": 4, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"drayson2025\", \"type\": \"inproceedings\", \"title\": \"Machine-Generated Text Detection Prevents Language Model Collapse\", \"authors\": \"Drayson, George and Yilmaz, Emine and Lampos, Vasileios\", \"year\": \"2025\", \"venue\": \"Proceedings of EMNLP\"}, {\"key\": \"schaeffer2025position\", \"type\": \"inproceedings\", \"title\": \"Position: Model Collapse Does Not Mean What You Think\", \"authors\": \"Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi\", \"year\": \"2025\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"kazdan2025collapse\", \"type\": \"inproceedings\", \"title\": \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\", \"authors\": \"Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias ...\", \"year\": \"2025\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"mitchell2023detectgpt\", \"type\": \"inproceedings\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"authors\": \"Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher...\", \"year\": \"2023\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"basani2026diveye\", \"type\": \"article\", \"title\": \"DivEye: Diversity Boosts AI-Generated Text Detection\", \"authors\": \"Basani, Advik Raj and Chen, Pin-Yu\", \"year\": \"2026\", \"venue\": \"Transactions on Machine Learning Research\"}, {\"key\": \"zawalski2026codec\", \"type\": \"inproceedings\", \"title\": \"CoDeC: Detecting Data Contamination in LLMs via In-Context Learning\", \"authors\": \"Zawalski, Micha\\\\l and Boubdir, Meriem and Ba\\\\lazy, Klaudia and Nushi, Besmira an...\", \"year\": \"2026\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"zhang2024minkpp\", \"type\": \"inproceedings\", \"title\": \"Min-K\\\\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\", \"authors\": \"Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan\", \"year\": \"2024\", \"venue\": \"Proceedings of EMNLP\"}, {\"key\": \"shumailov2024collapse\", \"type\": \"article\", \"title\": \"AI Models Collapse When Trained on Recursively Generated Data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"alemohammad2024selfconsuming\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"dohmatob2024model\", \"type\": \"inproceedings\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kem...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"xie2023dsir\", \"type\": \"inproceedings\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"authors\": \"Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"tirumala2023d4\", \"type\": \"inproceedings\", \"title\": \"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\", \"authors\": \"Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"xie2023doremi\", \"type\": \"inproceedings\", \"title\": \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\", \"authors\": \"Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao a...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"hans2024binoculars\", \"type\": \"inproceedings\", \"title\": \"Spotting LLMs With Binoculars\", \"authors\": \"Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Ham...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"alain2017understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding Intermediate Layers Using Linear Classifier Probes\", \"authors\": \"Alain, Guillaume and Bengio, Yoshua\", \"year\": \"2017\", \"venue\": \"ICLR Workshop\"}, {\"key\": \"belinkov2022probing\", \"type\": \"article\", \"title\": \"Probing Classifiers: Promises, Shortcomings, and Advances\", \"authors\": \"Belinkov, Yonatan\", \"year\": \"2022\", \"venue\": \"Computational Linguistics\"}, {\"key\": \"bao2024fast\", \"type\": \"inproceedings\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"authors\": \"Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yu...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"frank2001ordinal\", \"type\": \"inproceedings\", \"title\": \"A Simple Approach to Ordinal Classification\", \"authors\": \"Frank, Eibe and Hall, Mark\", \"year\": \"2001\", \"venue\": \"Proceedings of ECML\"}, {\"key\": \"cheng2025beyond\", \"type\": \"inproceedings\", \"title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"authors\": \"Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM Web Conference (WWW)\"}, {\"key\": \"mehta2025beyond\", \"type\": \"article\", \"title\": \"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models\", \"authors\": \"Mehta, Sushant\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.17602\"}, {\"key\": \"sun2025aigt\", \"type\": \"inproceedings\", \"title\": \"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media\", \"authors\": \"Sun, Zhen and Zhang, Zongmin and Shen, Xinyue and Zhang, Ziyi and Liu, Yule and ...\", \"year\": \"2025\", \"venue\": \"Proceedings of ACL\"}, {\"key\": \"spennemann2025quantifying\", \"type\": \"article\", \"title\": \"Delving into: the Quantification of AI-Generated Content on the Internet (Synthetic Data)\", \"authors\": \"Spennemann, Dirk H. R.\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2504.08755\"}, {\"key\": \"dohmatob2025strong\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"wang2024semeval\", \"type\": \"inproceedings\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"authors\": \"Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov...\", \"year\": \"2024\", \"venue\": \"Proceedings of SemEval\"}, {\"key\": \"gerstgrasser2024model\", \"type\": \"inproceedings\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"authors\": \"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafae...\", \"year\": \"2024\", \"venue\": \"Proceedings of COLM\"}, {\"key\": \"guo2024curious\", \"type\": \"inproceedings\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"authors\": \"Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chloe\", \"year\": \"2024\", \"venue\": \"Findings of NAACL\"}, {\"key\": \"briesch2023selfconsuming\", \"type\": \"article\", \"title\": \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\", \"authors\": \"Briesch, Martin and Sobania, Dominik and Rothlauf, Franz\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2311.16822\"}, {\"key\": \"padmakumar2024writing\", \"type\": \"inproceedings\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"authors\": \"Padmakumar, Vishakh and He, He\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"krishna2023paraphrasing\", \"type\": \"inproceedings\", \"title\": \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\", \"authors\": \"Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and I...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"sadasivan2023detect\", \"type\": \"article\", \"title\": \"Can AI-Generated Text be Reliably Detected?\", \"authors\": \"Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, W...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2303.11156\"}, {\"key\": \"hao2025rewrite\", \"type\": \"inproceedings\", \"title\": \"Learning to Rewrite: Generalized LLM-Generated Text Detection\", \"authors\": \"Hao, Wei and Guan, Ran and Lu, Kangjie and Zhang, Shuai\", \"year\": \"2025\", \"venue\": \"Findings of ACL\"}, {\"key\": \"shi2025collapse\", \"type\": \"inproceedings\", \"title\": \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\", \"authors\": \"Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and ...\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"gambetta2024surplexity\", \"type\": \"article\", \"title\": \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\", \"authors\": \"Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2410.12341\"}, {\"key\": \"amin2025escaping\", \"type\": \"inproceedings\", \"title\": \"Escaping Collapse: The Strength of Weak Data for Large Language Model Training\", \"authors\": \"Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar a...\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems\"}], \"tex_citations\": [{\"key\": \"sun2025aigt\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"spennemann2025quantifying\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"shumailov2024collapse\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"dohmatob2024model\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"basani2026diveye\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"zhang2024minkpp\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"zawalski2026codec\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"shumailov2024collapse\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"alemohammad2024selfconsuming\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"schaeffer2025position\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"xie2023dsir\", \"file\": \"introduction.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"tirumala2023d4\", \"file\": \"introduction.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"drayson2025\", \"file\": \"introduction.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"shumailov2024collapse\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"alemohammad2024selfconsuming\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"dohmatob2024model\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"dohmatob2025strong\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"guo2024curious\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"padmakumar2024writing\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"briesch2023selfconsuming\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"schaeffer2025position\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"kazdan2025collapse\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gerstgrasser2024model\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"shi2025collapse\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"gambetta2024surplexity\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"amin2025escaping\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"kazdan2025collapse\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"mitchell2023detectgpt\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"bao2024fast\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"hans2024binoculars\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"basani2026diveye\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"zhang2024minkpp\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"cheng2025beyond\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"mehta2025beyond\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"wang2024semeval\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"sadasivan2023detect\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"krishna2023paraphrasing\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"hao2025rewrite\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"zawalski2026codec\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"xie2023dsir\", \"file\": \"related_work.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"tirumala2023d4\", \"file\": \"related_work.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"xie2023doremi\", \"file\": \"related_work.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"drayson2025\", \"file\": \"related_work.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"frank2001ordinal\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"alain2017understanding\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"belinkov2022probing\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"basani2026diveye\", \"file\": \"experiments_c1.tex\", \"line\": 167, \"command\": \"cite\"}, {\"key\": \"hans2024binoculars\", \"file\": \"experiments_c1.tex\", \"line\": 167, \"command\": \"cite\"}, {\"key\": \"drayson2025\", \"file\": \"experiments_c3.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"xie2023dsir\", \"file\": \"experiments_c3.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"shumailov2024collapse\", \"file\": \"experiments_c3.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"dohmatob2024model\", \"file\": \"experiments_c3.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"drayson2025\", \"file\": \"discussion.tex\", \"line\": 54, \"command\": \"citet\"}], \"online_verification\": [{\"key\": \"drayson2025\", \"title\": \"Machine-Generated Text Detection Prevents Language Model Collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Machine-generated text detection prevents language model collapse\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"schaeffer2025position\", \"title\": \"Position: Model Collapse Does Not Mean What You Think\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Position: Model Collapse Does Not Mean What You Think\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kazdan2025collapse\", \"title\": \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mitchell2023detectgpt\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"status\": \"not_found\", \"confidence\": 0.382, \"matched_title\": \"Regulating ChatGPT and other Large Generative AI Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.38 below threshold 0.82\"}, {\"key\": \"basani2026diveye\", \"title\": \"DivEye: Diversity Boosts AI-Generated Text Detection\", \"status\": \"not_found\", \"confidence\": 0.529, \"matched_title\": \"When AI Settles Down: Late-Stage Stability as a Signature of AI-Generated Text Detection\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.53 below threshold 0.82\"}, {\"key\": \"zawalski2026codec\", \"title\": \"CoDeC: Detecting Data Contamination in LLMs via In-Context Learning\", \"status\": \"not_found\", \"confidence\": 0.306, \"matched_title\": \"Factuality Challenges in the Era of Large Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.31 below threshold 0.82\"}, {\"key\": \"zhang2024minkpp\", \"title\": \"Min-K\\\\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shumailov2024collapse\", \"title\": \"AI Models Collapse When Trained on Recursively Generated Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"AI models collapse when trained on recursively generated data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"alemohammad2024selfconsuming\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Self-Consuming Generative Models go MAD\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=alemohammad vs api=casco-rodriguez\"], \"note\": \"\"}, {\"key\": \"dohmatob2024model\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie2023dsir\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Data Selection for Language Models via Importance Resampling\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tirumala2023d4\", \"title\": \"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie2023doremi\", \"title\": \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hans2024binoculars\", \"title\": \"Spotting LLMs With Binoculars\", \"status\": \"not_found\", \"confidence\": 0.552, \"matched_title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.55 below threshold 0.82\"}, {\"key\": \"alain2017understanding\", \"title\": \"Understanding Intermediate Layers Using Linear Classifier Probes\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Understanding intermediate layers using linear classifier probes\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"belinkov2022probing\", \"title\": \"Probing Classifiers: Promises, Shortcomings, and Advances\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Probing Classifiers: Promises, Shortcomings, and Advances\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bao2024fast\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"frank2001ordinal\", \"title\": \"A Simple Approach to Ordinal Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Simple Approach to Ordinal Classification\", \"matched_year\": \"2001\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cheng2025beyond\", \"title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mehta2025beyond\", \"title\": \"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=mehta vs api=sushant\"], \"note\": \"\"}, {\"key\": \"sun2025aigt\", \"title\": \"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"spennemann2025quantifying\", \"title\": \"Delving into: the Quantification of AI-Generated Content on the Internet (Synthetic Data)\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Delving into: the quantification of Ai-generated content on the internet (synthetic data)\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dohmatob2025strong\", \"title\": \"Strong Model Collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Strong Model Collapse\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2024semeval\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gerstgrasser2024model\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2024curious\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"briesch2023selfconsuming\", \"title\": \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"padmakumar2024writing\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"krishna2023paraphrasing\", \"title\": \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sadasivan2023detect\", \"title\": \"Can AI-Generated Text be Reliably Detected?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Can AI-Generated Text be Reliably Detected?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hao2025rewrite\", \"title\": \"Learning to Rewrite: Generalized LLM-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Learning to Rewrite: Generalized LLM-Generated Text Detection\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shi2025collapse\", \"title\": \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gambetta2024surplexity\", \"title\": \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"amin2025escaping\", \"title\": \"Escaping Collapse: The Strength of Weak Data for Large Language Model Training\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Escaping Collapse: The Strength of Weak Data for Large Language Model Training\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "8d6533a7-e940-440f-9bbb-db7ffb003529",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性**  ### Venue 信息 - **目标**: EMNLP 2026（ARR May 2026 cycle） - **Deadline**: 2026-05-25 - **格式**: ACL 双栏模板，`\\usepackage[review]{acl}`，Long…",
  "leafUuid": "b7e92992-4386-4197-bbee-6ffd1326cd50",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on generational depth contamination detection",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Assistant

_source line 23 · 2026-05-18T09:57:23.075Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the main.tex structure. Now I need to read all the section files to do a thorough review. Let me also fetch the ARR review form details. Let me read all the section files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7e92992-4386-4197-bbee-6ffd1326cd50",
  "isSidechain": false,
  "requestId": "req_011Cb9qRLp986cC7TnawwQyz",
  "type": "assistant",
  "uuid": "76303b65-e77a-406e-9272-9e90ad7b89c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112y4EvtQMpCoHwr4q9U1A4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13143,
      "cache_read_input_tokens": 29727,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 29727,
          "cache_creation_input_tokens": 13143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13143
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-18T09:57:23.104Z_

搜到 ARR review form 页面，继续获取详细评分标准，同时并行读取所有论文分节文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76303b65-e77a-406e-9272-9e90ad7b89c5",
  "isSidechain": false,
  "requestId": "req_011Cb9qRLp986cC7TnawwQyz",
  "type": "assistant",
  "uuid": "c2a2cc03-43a9-4182-afe2-a3dbeb1384a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112y4EvtQMpCoHwr4q9U1A4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13143,
      "cache_read_input_tokens": 29727,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 29727,
          "cache_creation_input_tokens": 13143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13143
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-18T09:57:25.013Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01C4j1nqEhJXha6CL6hZfouN`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other rated dimensions. List the exact score options for each."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2a2cc03-43a9-4182-afe2-a3dbeb1384a1",
  "isSidechain": false,
  "requestId": "req_011Cb9qRLp986cC7TnawwQyz",
  "type": "assistant",
  "uuid": "291cc234-5005-4a78-a28b-5fad1c8184f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112y4EvtQMpCoHwr4q9U1A4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13143,
      "cache_read_input_tokens": 29727,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 29727,
          "cache_creation_input_tokens": 13143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13143
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-18T09:57:29.671Z_

<details><summary>↩ Tool result · `toolu_011NH8K9yNXpPg432kgx6PV5`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We measure the generational depth discrimination boundary $\Kempirical$ for recursive synthetic text.
5	$\Kempirical \in \{1, 2, 3\}$ depends on source domain and model characteristics: general web text yields $\Kempirical{=}2$ across 8/9 configurations (5 families, 1B--14B; $p \leq 0.002$), with $\Kempirical{=}3$ for academic text, confirmed across five models and four architecture families.
6	Generator-independent features enable 80--92\% cross-model transfer ($\rho > 0.90$), making $\Kempirical$ measurement practical across generators.
7	As downstream validation, $\Kempirical{=}2$ supports binary filtering as the optimal granularity for web text: graduated depth weighting cannot exploit information that does not exist beyond the discrimination boundary.
8	$\Kempirical$ provides a representation-dependent lower bound on discriminable depth; the gap between $\Kempirical$ and the theoretical limit $\Ktheory$ remains open and may narrow with richer feature representations.
9	Future work includes scaling beyond 14B, additional structured domains, and retrain-chain $\Kstar$ characterization.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e620effc-90d1-49cf-970a-3ada639898c7",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "90d12d4d-e7de-4c26-aa59-c8c705b29968",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe measure the generational depth discrimination boundary $\\Kempirical$ for recursive synthetic text.\n$\\Kempirical \\in \\{1, 2, 3\\}$ depends on source domain and model characteristics: general web text yields $\\Kempirical{=}2$ across 8/9 configurations (5 families, 1B--14B; $p \\leq 0.002$), with $\\Kempirical{=}3$ for academic text, confirmed across five models and four architecture families.\nGenerator-independent features enable 80--92\\% cross-model transfer ($\\rho > 0.90$), making $\\Kempirical$ measurement practical across generators.\nAs downstream validation, $\\Kempirical{=}2$ supports binary filtering as the optimal granularity for web text: graduated depth weighting cannot exploit information that does not exist beyond the discrimination boundary.\n$\\Kempirical$ provides a representation-dependent lower bound on discriminable depth; the gap between $\\Kempirical$ and the theoretical limit $\\Ktheory$ remains open and may narrow with richer feature representations.\nFuture work includes scaling beyond 14B, additional structured domains, and retrain-chain $\\Kstar$ characterization.\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "e620effc-90d1-49cf-970a-3ada639898c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 27 · 2026-05-18T09:57:26.434Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YM4b7mex7MzZZP51YrDCjm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "291cc234-5005-4a78-a28b-5fad1c8184f8",
  "isSidechain": false,
  "requestId": "req_011Cb9qRLp986cC7TnawwQyz",
  "type": "assistant",
  "uuid": "12683f24-a5aa-4c57-a828-05a94cf8e21d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112y4EvtQMpCoHwr4q9U1A4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13143,
      "cache_read_input_tokens": 29727,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 29727,
          "cache_creation_input_tokens": 13143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13143
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-18T09:57:26.442Z_

<details><summary>↩ Tool result · `toolu_01YM4b7mex7MzZZP51YrDCjm`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.
9	
10	This gap cuts across multiple communities: binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}), membership inference~\cite{zawalski2026codec} addresses a different question, and the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool.
11	Data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} likewise ignore recursive depth.
12	No existing method estimates how many rounds of recursive generation a text has undergone.
13	
14	Knowing whether the discriminable depth is finite, and where it saturates, has direct practical consequences.
15	For data curation, the saturation point determines filtering granularity: if discrimination collapses at depth 2, graduated weighting beyond that boundary injects noise, and binary filtering becomes the principled choice.
16	Model collapse theory predicts monotonic quality degradation across generations, but existing analyses are population-level and provide no per-text measure of where degradation saturates.
17	$\Kempirical$ fills this gap by localizing the generation at which adjacent outputs become empirically indistinguishable.
18	
19	The Data Processing Inequality guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
20	We empirically measure $\Kempirical$ (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features computed via a fixed reference scorer (Section~\ref{sec:features}) and an Ordinal Binary Decomposition (OBD) LightGBM classifier.
21	We operationalize $\Kempirical$ as the deepest $k \geq 1$ where the pairwise $\auc_{k-1,k}$ exceeds $\theta = 0.60$ (Section~\ref{sec:formulation}).
22	
23	Our contributions:
24	\begin{enumerate}[label=(\alph*),nosep]
25	  \item \textbf{First empirical measurement of $\Kempirical$} across 9 model configurations (5 architecture families, 1B--14B), 3 source domains, and 4 decoding strategies at $\theta{=}0.60$ ($p \leq 0.002$; Section~\ref{sec:kstar_boundary}).
26	  Both supervised OBD and zero-shot frontier Large Language Models (LLMs) show no statistically significant difference beyond $\Kempirical$ (McNemar $p > 0.05$, $N{=}500$; Section~\ref{sec:why_kstar}).
27	  \item \textbf{Domain ordering invariance}: the hierarchy arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$) is preserved across six models spanning four architecture families, three scales (1B--14B), and four decoding strategies, with domain structural complexity as the primary factor governing $\Kempirical$ (Section~\ref{sec:cross_domain}).
28	  \item \textbf{Generator-independent features}: 15 scorer-derived statistical features enable 80--92\% cross-model transfer among continuation-mode generators ($\rho > 0.90$ feature ranking preservation), making $\Kempirical$ measurement practical without generator-specific training (Section~\ref{sec:transfer}).
29	\end{enumerate}
30	
31	\noindent As a downstream validation, $\Kempirical{=}2$ correctly predicts the strategy ordering for web-text filtering: binary curation minimizes degradation most effectively (MMLU $0.5941$ vs.\ base $0.6018$; Section~\ref{sec:filtering}).
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12683f24-a5aa-4c57-a828-05a94cf8e21d",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "830b943f-336a-4cf8-bad5-25514ecdd632",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.\nEstimates suggest that a substantial fraction of online text is machine-generated~\\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.\nWhen models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\\cite{shumailov2024collapse, dohmatob2024model}.\nThis degradation arises in both \\emph{retrain-chains} (iteratively training on model outputs) and \\emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\\ref{sec:extended_limitations}).\nYet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.\n\nThis gap cuts across multiple communities: binary detectors~\\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\\ref{sec:binary_confidence}), membership inference~\\cite{zawalski2026codec} addresses a different question, and the model collapse literature~\\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool.\nData selection methods~\\cite{xie2023dsir, tirumala2023d4, drayson2025} likewise ignore recursive depth.\nNo existing method estimates how many rounds of recursive generation a text has undergone.\n\nKnowing whether the discriminable depth is finite, and where it saturates, has direct practical consequences.\nFor data curation, the saturation point determines filtering granularity: if discrimination collapses at depth 2, graduated weighting beyond that boundary injects noise, and binary filtering becomes the principled choice.\nModel collapse theory predicts monotonic quality degradation across generations, but existing analyses are population-level and provide no per-text measure of where degradation saturates.\n$\\Kempirical$ fills this gap by localizing the generation at which adjacent outputs become empirically indistinguishable.\n\nThe Data Processing Inequality guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\\Kstar$.\nWe empirically measure $\\Kempirical$ (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features computed via a fixed reference scorer (Section~\\ref{sec:features}) and an Ordinal Binary Decomposition (OBD) LightGBM classifier.\nWe operationalize $\\Kempirical$ as the deepest $k \\geq 1$ where the pairwise $\\auc_{k-1,k}$ exceeds $\\theta = 0.60$ (Section~\\ref{sec:formulation}).\n\nOur contributions:\n\\begin{enumerate}[label=(\\alph*),nosep]\n  \\item \\textbf{First empirical measurement of $\\Kempirical$} across 9 model configurations (5 architecture families, 1B--14B), 3 source domains, and 4 decoding strategies at $\\theta{=}0.60$ ($p \\leq 0.002$; Section~\\ref{sec:kstar_boundary}).\n  Both supervised OBD and zero-shot frontier Large Language Models (LLMs) show no statistically significant difference beyond $\\Kempirical$ (McNemar $p > 0.05$, $N{=}500$; Section~\\ref{sec:why_kstar}).\n  \\item \\textbf{Domain ordering invariance}: the hierarchy arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $>$ Wikipedia ($\\Kempirical{=}1$) is preserved across six models spanning four architecture families, three scales (1B--14B), and four decoding strategies, with domain structural complexity as the primary factor governing $\\Kempirical$ (Section~\\ref{sec:cross_domain}).\n  \\item \\textbf{Generator-independent features}: 15 scorer-derived statistical features enable 80--92\\% cross-model transfer among continuation-mode generators ($\\rho > 0.90$ feature ranking preservation), making $\\Kempirical$ measurement practical without generator-specific training (Section~\\ref{sec:transfer}).\n\\end{enumerate}\n\n\\noindent As a downstream validation, $\\Kempirical{=}2$ correctly predicts the strategy ordering for web-text filtering: binary curation minimizes degradation most effectively (MMLU $0.5941$ vs.\\ base $0.6018$; Section~\\ref{sec:filtering}).\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  },
  "sourceToolAssistantUUID": "12683f24-a5aa-4c57-a828-05a94cf8e21d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 29 · 2026-05-18T09:57:26.916Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FQb6m5YhVyrgGsKpz43dgN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "830b943f-336a-4cf8-bad5-25514ecdd632",
  "isSidechain": false,
  "requestId": "req_011Cb9qRLp986cC7TnawwQyz",
  "type": "assistant",
  "uuid": "192c435c-2e23-4dc1-8146-6fa4ab223507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112y4EvtQMpCoHwr4q9U1A4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13143,
      "cache_read_input_tokens": 29727,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 29727,
          "cache_creation_input_tokens": 13143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13143
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-18T09:57:26.921Z_

<details><summary>↩ Tool result · `toolu_01FQb6m5YhVyrgGsKpz43dgN`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model}.
6	In the context of diffusion models, \citet{shi2025collapse} trace a generalization-to-memorization transition under iterative synthetic training.
7	\citet{gambetta2024surplexity} propose surplexity, a single surprisal-based collapse indicator; our 15-dimensional feature set captures richer distributional structure and enables cross-model transfer.
8	\citet{amin2025escaping} show that weak-data curation can mitigate collapse, connecting to our filtering evaluation (Section~\ref{sec:filtering}).
9	Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}, making $\Kempirical = 2$ a conservative lower bound.
10	This literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.
11	
12	\paragraph{Beyond binary detection.}
13	Binary detectors~\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate.
14	Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
15	None estimates recursive generation depth.
16	
17	\paragraph{Data selection and curation.}
18	DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling, a special case when $\Kstar = 1$.
19	
20	\paragraph{Ordinal classification and probing.}
21	Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "192c435c-2e23-4dc1-8146-6fa4ab223507",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "03499fa8-5e13-441d-aa4d-57b4f55dd05f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Model collapse and recursive degradation.}\nIterative training on model outputs causes tail-distribution degradation~\\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model}.\nIn the context of diffusion models, \\citet{shi2025collapse} trace a generalization-to-memorization transition under iterative synthetic training.\n\\citet{gambetta2024surplexity} propose surplexity, a single surprisal-based collapse indicator; our 15-dimensional feature set captures richer distributional structure and enables cross-model transfer.\n\\citet{amin2025escaping} show that weak-data curation can mitigate collapse, connecting to our filtering evaluation (Section~\\ref{sec:filtering}).\nOur prompt-chain operates in the replace regime~\\cite{kazdan2025collapse}, making $\\Kempirical = 2$ a conservative lower bound.\nThis literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.\n\n\\paragraph{Beyond binary detection.}\nBinary detectors~\\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate.\nRecent work extends beyond binary labels to collaboration degree~\\cite{cheng2025beyond}, contamination hierarchies~\\cite{mehta2025beyond}, and multigenerator benchmarks~\\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\\cite{hao2025rewrite}; CoDeC~\\cite{zawalski2026codec} addresses contamination via membership inference.\nNone estimates recursive generation depth.\n\n\\paragraph{Data selection and curation.}\nDSIR~\\cite{xie2023dsir}, D4~\\cite{tirumala2023d4}, and DoReMi~\\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\\cite{drayson2025} combined binary detection with importance resampling, a special case when $\\Kstar = 1$.\n\n\\paragraph{Ordinal classification and probing.}\nOur OBD classifier follows Frank \\& Hall's~\\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  },
  "sourceToolAssistantUUID": "192c435c-2e23-4dc1-8146-6fa4ab223507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 31 · 2026-05-18T09:57:27.875Z_

<details open><summary>🔧 Tool call — Read · `toolu_014hZdW6BiP6s1ZSxDvGC7m6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03499fa8-5e13-441d-aa4d-57b4f55dd05f",
  "isSidechain": false,
  "requestId": "req_011Cb9qRLp986cC7TnawwQyz",
  "type": "assistant",
  "uuid": "13d14e40-92ab-443f-a005-72118d0eb698",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112y4EvtQMpCoHwr4q9U1A4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13143,
      "cache_read_input_tokens": 29727,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 29727,
          "cache_creation_input_tokens": 13143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13143
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-18T09:57:27.881Z_

<details><summary>↩ Tool result · `toolu_014hZdW6BiP6s1ZSxDvGC7m6`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: the original signal degrades monotonically.
17	Together with Markov chain convergence, this guarantees a finite $\Ktheory$ beyond which adjacent generations are indistinguishable.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\{k \geq 1 : \auc_{k-1,k} > \theta\},
22	  \label{eq:kstar}
23	\end{equation}
24	where $\auc_{k-1,k}$ is the point-estimate pairwise AUC (Area Under the ROC Curve) and $\theta = 0.60$ is a small-effect-size threshold (Cohen's $h \approx 0.20$\footnote{$h = 2\arcsin\!\sqrt{0.60} - 2\arcsin\!\sqrt{0.50} \approx 0.2014$, a ``small'' effect size by Cohen's (1988) convention; we use this as a motivating analogy rather than a formal justification, since the permutation test and AUC gap (below) are the primary evidence.}; motivated below).
25	Bootstrap 95\% confidence intervals (CIs; 1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
26	
27	\paragraph{Threshold choice.}
28	$\theta{=}0.60$ is supported by three independent lines of evidence.
29	First, it corresponds to Cohen's $h \approx 0.20$, a conventional small-effect-size boundary.
30	Second, a 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\,0.55$ and $p < 0.002$ for all boundary comparisons, placing $\theta{=}0.60$ well above the empirical null.
31	Third, and most critically, the conclusion $\Kempirical{=}2$ is insensitive to the exact threshold: 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, creating a ${\sim}$5--11\,pp discontinuity that any $\theta \in [0.55, 0.65]$ would separate (Figure~\ref{fig:kstar_theta}; Appendix~\ref{sec:extended_limitations}).
32	Only at extremes does $\Kempirical$ shift: $\theta{=}0.55$ yields $\Kempirical{=}3$ for two Qwen configurations; $\theta{=}0.70$ yields $\Kempirical{=}1$ across all configurations.
33	The downstream filtering evaluation (Section~\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\theta$, avoiding circularity.
34	
35	\subsection{Features and Classifier}
36	\label{sec:features}
37	
38	Each document is characterized by a 15-dimensional feature vector spanning four groups: \emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).
39	All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
40	Self-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.
41	Removing self-BLEU reduces mean $\auc_{1v2}$ by $< 1$\,pp across all models (14D $\Kempirical = 2$ for all 4 configurations; bootstrap CIs in Table~\ref{tab:selfbleu_ablation}); in deployment where depth labels are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted with minimal performance loss.
42	Hand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.
43	
44	We use \emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\text{depth} > k \mid \mathbf{x})$ via LightGBM (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
45	OBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\auc$ (mean 0.6095 vs.\ 0.4883 for ordinal logistic regression).
46	
47	\subsection{Experimental Setup}
48	\label{sec:experimental_setup}
49	
50	We evaluate nine configurations spanning five architecture families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B, Qwen2.5-14B, Pythia-1.4B, OLMo-1B, LLaMA-3.1-8B, and Mistral-7B (all continuation except Qwen-rw).
51	Each uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).
52	Default decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.
53	Continuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.
54	Evaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\auc$ as primary metric.
55	
56	\begin{table}[t]
57	\centering
58	\small
59	\caption{Experimental configurations for depth-chain generation. \textbf{Config}: shorthand identifier; \textbf{Model}: architecture and parameter count; \textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}
60	\label{tab:setup}
61	\resizebox{\columnwidth}{!}{%
62	\begin{tabular}{llcc}
63	\toprule
64	\textbf{Config} & \textbf{Model} & \textbf{Mode} & $N$ \\
65	\midrule
66	Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\
67	Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\
68	Qwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\
69	Pythia    & Pythia-1.4B            & Continuation & 5{,}000 \\
70	OLMo      & OLMo-1B               & Continuation & 5{,}000 \\
71	Qwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\
72	Qwen-14B  & Qwen2.5-14B           & Continuation & 5{,}000 \\
73	LLaMA-8B  & LLaMA-3.1-8B          & Continuation & 5{,}000 \\
74	Mistral   & Mistral-7B            & Continuation & 5{,}000 \\
75	\bottomrule
76	\end{tabular}}
77	\end{table}
78	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13d14e40-92ab-443f-a005-72118d0eb698",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "dc79bfac-48be-486b-881d-06d736b19f85",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/pipeline.pdf}\n\\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}\n\\label{fig:pipeline}\n\\end{figure*}\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nA generation operator $G_\\delta$ (LLM + decoding strategy $\\delta$) produces successive generations $X \\to Y_1 \\to \\cdots \\to Y_K$, where $Y_k = G_\\delta(Y_{k-1})$ and $Y_0 \\triangleq X$ (Figure~\\ref{fig:pipeline}).\nThis sequence forms a Markov chain.\nBy the Data Processing Inequality, $I(X; Y_1) \\geq I(X; Y_2) \\geq \\cdots \\geq 0$: the original signal degrades monotonically.\nTogether with Markov chain convergence, this guarantees a finite $\\Ktheory$ beyond which adjacent generations are indistinguishable.\n\nWe define the operational lower bound:\n\\begin{equation}\n  \\Kempirical = \\max\\{k \\geq 1 : \\auc_{k-1,k} > \\theta\\},\n  \\label{eq:kstar}\n\\end{equation}\nwhere $\\auc_{k-1,k}$ is the point-estimate pairwise AUC (Area Under the ROC Curve) and $\\theta = 0.60$ is a small-effect-size threshold (Cohen's $h \\approx 0.20$\\footnote{$h = 2\\arcsin\\!\\sqrt{0.60} - 2\\arcsin\\!\\sqrt{0.50} \\approx 0.2014$, a ``small'' effect size by Cohen's (1988) convention; we use this as a motivating analogy rather than a formal justification, since the permutation test and AUC gap (below) are the primary evidence.}; motivated below).\nBootstrap 95\\% confidence intervals (CIs; 1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\\theta$ and non-boundary-pair CI upper bounds fall below $\\theta$ (Section~\\ref{sec:kstar_boundary}).\n\n\\paragraph{Threshold choice.}\n$\\theta{=}0.60$ is supported by three independent lines of evidence.\nFirst, it corresponds to Cohen's $h \\approx 0.20$, a conventional small-effect-size boundary.\nSecond, a 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\\,0.55$ and $p < 0.002$ for all boundary comparisons, placing $\\theta{=}0.60$ well above the empirical null.\nThird, and most critically, the conclusion $\\Kempirical{=}2$ is insensitive to the exact threshold: 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, creating a ${\\sim}$5--11\\,pp discontinuity that any $\\theta \\in [0.55, 0.65]$ would separate (Figure~\\ref{fig:kstar_theta}; Appendix~\\ref{sec:extended_limitations}).\nOnly at extremes does $\\Kempirical$ shift: $\\theta{=}0.55$ yields $\\Kempirical{=}3$ for two Qwen configurations; $\\theta{=}0.70$ yields $\\Kempirical{=}1$ across all configurations.\nThe downstream filtering evaluation (Section~\\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\\theta$, avoiding circularity.\n\n\\subsection{Features and Classifier}\n\\label{sec:features}\n\nEach document is characterized by a 15-dimensional feature vector spanning four groups: \\emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \\emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \\emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \\emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).\nAll features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\\ref{tab:s5_features}, Appendix).\nSelf-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \\#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.\nRemoving self-BLEU reduces mean $\\auc_{1v2}$ by $< 1$\\,pp across all models (14D $\\Kempirical = 2$ for all 4 configurations; bootstrap CIs in Table~\\ref{tab:selfbleu_ablation}); in deployment where depth labels are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted with minimal performance loss.\nHand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.\n\nWe use \\emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\\text{depth} > k \\mid \\mathbf{x})$ via LightGBM (hyperparameters in Table~\\ref{tab:s6_lgbm_params}).\nOBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\\auc$ (mean 0.6095 vs.\\ 0.4883 for ordinal logistic regression).\n\n\\subsection{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate nine configurations spanning five architecture families (Table~\\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B, Qwen2.5-14B, Pythia-1.4B, OLMo-1B, LLaMA-3.1-8B, and Mistral-7B (all continuation except Qwen-rw).\nEach uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).\nDefault decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.\nContinuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.\nEvaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\\auc$ as primary metric.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Experimental configurations for depth-chain generation. \\textbf{Config}: shorthand identifier; \\textbf{Model}: architecture and parameter count; \\textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}\n\\label{tab:setup}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Config} & \\textbf{Model} & \\textbf{Mode} & $N$ \\\\\n\\midrule\nQwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\\\\nQwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\\\\nQwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\\\\nPythia    & Pythia-1.4B            & Continuation & 5{,}000 \\\\\nOLMo      & OLMo-1B               & Continuation & 5{,}000 \\\\\nQwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\\\\nQwen-14B  & Qwen2.5-14B           & Continuation & 5{,}000 \\\\\nLLaMA-8B  & LLaMA-3.1-8B          & Continuation & 5{,}000 \\\\\nMistral   & Mistral-7B            & Continuation & 5{,}000 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 78,
      "startLine": 1,
      "totalLines": 78
    }
  },
  "sourceToolAssistantUUID": "13d14e40-92ab-443f-a005-72118d0eb698",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 33 · 2026-05-18T09:57:28.354Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G9F5MpWys54CqJDqbQUJ7G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc79bfac-48be-486b-881d-06d736b19f85",
  "isSidechain": false,
  "requestId": "req_011Cb9qRLp986cC7TnawwQyz",
  "type": "assistant",
  "uuid": "a0d8ec17-07b6-44f3-bd17-da983dbd31c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112y4EvtQMpCoHwr4q9U1A4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13143,
      "cache_read_input_tokens": 29727,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 29727,
          "cache_creation_input_tokens": 13143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13143
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-18T09:57:28.360Z_

<details><summary>↩ Tool result · `toolu_01G9F5MpWys54CqJDqbQUJ7G`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on nine model configurations spanning five architecture families:
5	Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, Qwen2.5-14B, LLaMA-3.1-8B, and Mistral-7B, all in continuation mode except where noted.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
7	
8	%% ====================================================================
9	\subsection{\texorpdfstring{$\Kempirical \leq 2$}{K*<=2} Across Model Configurations (C4)}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
17	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
18	\label{tab:kstar_ci}
19	\begin{tabular}{lcccccccccc}
20	\toprule
21	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
22	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
23	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
24	\midrule
25	0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\,.967] \\
26	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .6145 & [.605,\,.625]\rlap{$^*$} & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
27	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .5496 & [.540,\,.560] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
28	3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\
29	4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\
30	\bottomrule
31	\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\
32	\multicolumn{11}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}
33	\end{tabular}
34	\end{table*}
35	
36	\begin{figure}[t]
37	\centering
38	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
39	\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\theta = 0.60$.}
40	\label{fig:auc_decay}
41	\end{figure}
42	
43	Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical \leq 2$ across all 9 model configurations: 8/9 yield $\Kempirical{=}2$ (1v2 $\auc$ range: 0.6112--0.6955; all CI lower bounds $> \theta$; permutation $p < 0.001$), while Mistral-7B is the sole exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, below $\theta$; Section~\ref{sec:boundary_cases}).
44	LLaMA-3.1-8B yields $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123$, 95\% CI $[0.603, 0.622]$; borderline: 1/5 folds falls below $\theta$; Table~\ref{tab:kstar_ci_extended}).
45	All four decoding strategies likewise yield $\Kempirical{=}2$ (Table~\ref{tab:s2_decoding}).
46	The 1v2 spread due to generation mode ($\Delta = 8.4$\,pp within Qwen) exceeds the spread across models in continuation mode ($\Delta = 3.9$\,pp).
47	
48	\paragraph{Scale and instruction-tuning invariance.}
49	$\Kempirical{=}2$ persists from 1.5B through 14B: Qwen-14B (1v2 $\auc = 0.621$ $[0.612, 0.630]$), Qwen-7B ($0.6168$ $[0.608, 0.626]$), and LLaMA-3.1-8B ($0.6123$) all exceed $\theta$, despite progressively reduced 0v1 signal (0.960 at 14B, 0.964 at 7B, 0.923 at 8B vs.\ $> 0.99$ at $\leq$1.5B).
50	A base-vs.-instruct ablation at 1.5B likewise yields $\Kempirical = 2$ (1v2 $\auc = 0.626$), indicating the boundary is not an instruction-tuning artifact.
51	
52	\begin{figure}[t]
53	\centering
54	\includegraphics[width=\columnwidth]{figures/fig_kstar_theta.pdf}
55	\caption{$\Kempirical(\theta)$ sensitivity curve for six configurations. $\Kempirical$: maximum discriminable depth; $\theta$: AUC decision threshold. All configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (dashed line). At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
56	\label{fig:kstar_theta}
57	\end{figure}
58	
59	Figure~\ref{fig:kstar_theta} shows $\Kempirical$ as a function of $\theta$: web text $\Kempirical{=}2$ is stable across a 5\,pp window ($\theta \in [0.575, 0.625]$), with a gradual transition to $\Kempirical{=}3$ at $\theta{=}0.55$ (two Qwen configurations) and $\Kempirical{=}1$ at $\theta{=}0.70$.
60	The domain ordering (arXiv $>$ web $\geq$ cross-scorer) is preserved across the full $\theta$ range (Table~\ref{tab:theta_sensitivity}).
61	All four decoding strategies likewise yield $\Kempirical = 2$ at $\theta{=}0.60$ (1v2 $\auc \in [0.687, 0.704]$; Table~\ref{tab:s2_decoding}).
62	
63	%% ====================================================================
64	\subsection{Generator-Independent Transfer}
65	\label{sec:transfer}
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=0.85\columnwidth]{figures/fig3_transfer_heatmap.pdf}
70	\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\leftrightarrow$OLMo: 90--92\%; Qwen-rewrite$\to$continuation: 61--63\%.}
71	\label{fig:transfer_heatmap}
72	\end{figure}
73	
74	Continuation-mode classifiers transfer well across generators (Figure~\ref{fig:transfer_heatmap}; full matrix in Table~\ref{tab:s1_transfer}): Pythia$\leftrightarrow$OLMo retains 90--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\% (0v1 cross-model $\auc > 0.96$ for all pairs).
75	Qwen-rewrite classifiers transfer poorly (61--63\%), consistent with reliance on mode-specific artifacts rather than generalizable depth features.
76	
77	\paragraph{Cross-scorer validation.}
78	Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\ref{tab:crossscorer}).
79	Qwen-rewrite $\Kempirical$ remains 2 under all scorers; Qwen-continuation drops to 1 (1v2 $\auc$: $0.6112 \to 0.5923/0.5858$), consistent with its marginality under self-scoring.
80	Both alternative scorers agree on $\Kempirical$ per generation mode, indicating that $\Kempirical$ is governed by the generation process rather than the scorer.
81	For arXiv, cross-scoring with Pythia-1.4B preserves $\Kempirical{=}3$ for three of four generators (Qwen-1.5B, LLaMA-8B, Mistral-7B; 2v3 $\auc$ range: 0.608--0.632).
82	Qwen-7B exhibits a borderline decrease to $\Kempirical{=}2$ (2v3 $\auc = 0.599$ vs.\ $0.626$ self-scored, $\Delta = -2.7$\,pp; 3/5 folds above $\theta$), consistent with the Qwen family's scorer sensitivity observed on C4 and Wikipedia.
83	Bootstrap CIs (10{,}000 resamples) confirm $\Kempirical{=}3$ for Qwen-1.5B (CI lower $= 0.617$) and LLaMA-8B (CI lower $= 0.605$); for Mistral-7B (CI: $[0.593, 0.622]$) and Qwen-7B (CI: $[0.584, 0.613]$), the CI straddles $\theta$, indicating that their $\Kempirical{=}3$ assignment is sensitive to resampling variance (Table~\ref{tab:arxiv_crossscorer_ci}).
84	A three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair; $N{=}300$; Table~\ref{tab:anova_crossscorer}) confirms that Depth-Pair dominates variance ($\eta^2_p = 0.998$); Scorer is statistically significant ($p < .001$) but practically minor ($\eta^2_p = 0.192$), consistent with a detectable but small scorer influence on absolute discriminability.
85	
86	%% ====================================================================
87	\subsection{Feature Ordering and Generation Mode}
88	\label{sec:feature_degradation}
89	\label{sec:generation_mode}
90	
91	Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
92	The top-3 features (\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability; however, no single feature subset of size ${<}8$ reliably sustains $\Kempirical{=}2$ (Appendix~\ref{sec:feature_subset}).
93	Qwen-rewrite diverges (\texttt{freq\_entropy} dominates), consistent with its poor cross-model transfer (61--63\%).
94	Within Qwen, rewrite yields 1v2 $\auc = 0.6955$ vs.\ continuation's $0.6112$ ($\Delta = +8.4$\,pp); continuation mode is therefore recommended as the canonical condition.
95	
96	%% ====================================================================
97	\subsection{Neural Probe}
98	\label{sec:neural_probe}
99	
100	Replacing the 15D features with frozen encoder hidden states (MLP probe; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia and OLMo remain at $\Kempirical^{\text{neural}} = 2$ ($\auc_{2v3}$: 0.5963, 0.5892).
101	The Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\ref{sec:transfer}); the 15D features yield consistent $\Kempirical = 2$ across all families.
102	
103	\noindent\begin{minipage}{\columnwidth}
104	\centering
105	\footnotesize
106	\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $\Kempirical^{\text{neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}
107	\label{tab:neural_probe_crossmodel}
108	\resizebox{\columnwidth}{!}{%
109	\begin{tabular}{lccc}
110	\toprule
111	\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
112	\midrule
113	Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
114	Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
115	OLMo-1B    & 0.5892 & $[0.582,\,0.597]$ & 2 \\
116	\bottomrule
117	\end{tabular}}
118	\end{minipage}
119	
120	%% ====================================================================
121	\subsection{Cross-Domain Variation}
122	\label{sec:cross_domain}
123	
124	The preceding experiments use C4 (general web text).
125	To test whether $\Kempirical$ reflects domain structure or model identity, we evaluate on arXiv abstracts ($n{=}2{,}200$ per model) and Wikipedia ($n{=}5{,}000$ per model) across six model configurations spanning four architecture families (Table~\ref{tab:domain_kstar}).
126	
127	\paragraph{arXiv ($\Kempirical{=}3$): five-model cross-validation.}
128	All five domain-competent models yield $\Kempirical{=}3$ on arXiv, with boundary-pair $\auc$ (2v3) ranging from 0.6215 to 0.6545, all exceeding $\theta$.
129	The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4): formulaic features (LaTeX formatting, citation patterns, mathematical notation) degrade slowly under autoregressive generation and supply persistent depth signal across four architecture families and 1.4B--8B parameters.
130	OLMo-1B constitutes a capacity failure rather than a counter-example; its arXiv generations are entirely out-of-domain (0v1 JSD $= 0.33$, near-total information loss at the first step), yielding $\Kempirical{=}1$.
131	Mistral-7B provides the strongest domain-dependence evidence: $\Kempirical{=}1$ on C4 (Section~\ref{sec:boundary_cases}) but $\Kempirical{=}3$ on arXiv, confirming that domain structure alone can shift $\Kempirical$ by two levels within the same model.
132	
133	\paragraph{Wikipedia ($\Kempirical{=}1$): single-generation saturation.}
134	With scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield $\Kempirical{=}1$ on Wikipedia: 1v2 $\auc$ ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below $\theta$.
135	Wikipedia represents the simplest domain tested; its encyclopedic regularity provides minimal structural signal beyond the 0v1 boundary, and a single generation pass suffices for complete saturation.
136	A same-family scorer confound inflates the apparent $\Kempirical$ for Qwen generators: Qwen-1.5B scoring yields $\Kempirical{=}2$ (1v2 $\auc \approx 0.61$--$0.62$), but cross-family scoring reduces 1v2 by 2.4\,pp to below $\theta$ (Appendix~\ref{sec:wiki_domain}).
137	This +1 depth bias under same-family scoring is specific to Qwen generators on Wikipedia and does not affect C4 results (Section~\ref{sec:transfer}).
138	
139	\paragraph{Domain as the sole dominant factor.}
140	With the scorer confound controlled, the domain ordering is uniform across all tested models: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$).
141	Neither model scale (1B--14B), architecture family, nor decoding strategy alters this ordering, establishing source-domain structural complexity as the primary determinant of $\Kempirical$.
142	
143	\noindent\begin{minipage}{\columnwidth}
144	\centering
145	\footnotesize
146	\captionof{table}{Domain $\times$ Model $\Kempirical$ matrix (scorer-controlled). Wikipedia values use cross-family scorer (Pythia-1.4B). $^*$OLMo arXiv: capacity failure (out-of-domain generation). $^\dagger$Raw same-family scoring yields $\Kempirical{=}2$; controlled value shown (Appendix~\ref{sec:wiki_domain}).}
147	\label{tab:domain_kstar}
148	\resizebox{\columnwidth}{!}{%
149	\begin{tabular}{lccc}
150	\toprule
151	\textbf{Model} & \textbf{C4} & \textbf{arXiv} & \textbf{Wikipedia} \\
152	\midrule
153	Qwen-1.5B    & 2 & 3 & 1$^\dagger$ \\
154	Qwen-7B      & 2 & 3 & 1$^\dagger$ \\
155	Pythia-1.4B  & 2 & 3 & 1 \\
156	OLMo-1B      & 2 & 1$^*$ & 1 \\
157	LLaMA-3.1-8B & 2 & 3 & 1 \\
158	Mistral-7B   & 1 & 3 & 1 \\
159	\bottomrule
160	\end{tabular}}
161	\end{minipage}
162	
163	%% ====================================================================
164	\subsection{Binary Detector Confidence}
165	\label{sec:binary_confidence}
166	
167	Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.
168	The observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.
169	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0d8ec17-07b6-44f3-bd17-da983dbd31c0",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "19bf5a08-4a5a-4096-8d6c-972423397416",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate generational depth estimation on nine model configurations spanning five architecture families:\nPythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, Qwen2.5-14B, LLaMA-3.1-8B, and Mistral-7B, all in continuation mode except where noted.\nAll experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).\n\n%% ====================================================================\n\\subsection{\\texorpdfstring{$\\Kempirical \\leq 2$}{K*<=2} Across Model Configurations (C4)}\n\\label{sec:kstar_boundary}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Pairwise $\\auc$ for adjacent depth pairs with bootstrap 95\\% CIs and permutation $p$-values for boundary rows.\n$\\Kempirical = 2$ requires 1v2 $\\auc > \\theta{=}0.60$ and 2v3 $\\auc < \\theta$; CIs quantify boundary uncertainty.\nExtended results (all models) in Table~\\ref{tab:kstar_ci_extended}.}\n\\label{tab:kstar_ci}\n\\begin{tabular}{lcccccccccc}\n\\toprule\n & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\n & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n\\midrule\n0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\\,.967] \\\\\n1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6539 & [.645,\\,.663]\\rlap{$^*$} & .6145 & [.605,\\,.625]\\rlap{$^*$} & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} \\\\\n2v3 & .5893 & [.580,\\,.599] & .5514 & [.542,\\,.563] & .5496 & [.540,\\,.560] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] \\\\\n3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\\\\n4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\\\\n\\bottomrule\n\\multicolumn{11}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_auc_decay.pdf}\n\\caption{Pairwise $\\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\\theta = 0.60$.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:kstar_ci} and Figure~\\ref{fig:auc_decay} show $\\Kempirical \\leq 2$ across all 9 model configurations: 8/9 yield $\\Kempirical{=}2$ (1v2 $\\auc$ range: 0.6112--0.6955; all CI lower bounds $> \\theta$; permutation $p < 0.001$), while Mistral-7B is the sole exception ($\\Kempirical{=}1$; 1v2 $\\auc = 0.594$, below $\\theta$; Section~\\ref{sec:boundary_cases}).\nLLaMA-3.1-8B yields $\\Kempirical{=}2$ (0v1 $\\auc = 0.9225$, 1v2 $\\auc = 0.6123$, 95\\% CI $[0.603, 0.622]$; borderline: 1/5 folds falls below $\\theta$; Table~\\ref{tab:kstar_ci_extended}).\nAll four decoding strategies likewise yield $\\Kempirical{=}2$ (Table~\\ref{tab:s2_decoding}).\nThe 1v2 spread due to generation mode ($\\Delta = 8.4$\\,pp within Qwen) exceeds the spread across models in continuation mode ($\\Delta = 3.9$\\,pp).\n\n\\paragraph{Scale and instruction-tuning invariance.}\n$\\Kempirical{=}2$ persists from 1.5B through 14B: Qwen-14B (1v2 $\\auc = 0.621$ $[0.612, 0.630]$), Qwen-7B ($0.6168$ $[0.608, 0.626]$), and LLaMA-3.1-8B ($0.6123$) all exceed $\\theta$, despite progressively reduced 0v1 signal (0.960 at 14B, 0.964 at 7B, 0.923 at 8B vs.\\ $> 0.99$ at $\\leq$1.5B).\nA base-vs.-instruct ablation at 1.5B likewise yields $\\Kempirical = 2$ (1v2 $\\auc = 0.626$), indicating the boundary is not an instruction-tuning artifact.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_kstar_theta.pdf}\n\\caption{$\\Kempirical(\\theta)$ sensitivity curve for six configurations. $\\Kempirical$: maximum discriminable depth; $\\theta$: AUC decision threshold. All configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (dashed line). At $\\theta{=}0.70$, all drop to $\\Kempirical{=}1$.}\n\\label{fig:kstar_theta}\n\\end{figure}\n\nFigure~\\ref{fig:kstar_theta} shows $\\Kempirical$ as a function of $\\theta$: web text $\\Kempirical{=}2$ is stable across a 5\\,pp window ($\\theta \\in [0.575, 0.625]$), with a gradual transition to $\\Kempirical{=}3$ at $\\theta{=}0.55$ (two Qwen configurations) and $\\Kempirical{=}1$ at $\\theta{=}0.70$.\nThe domain ordering (arXiv $>$ web $\\geq$ cross-scorer) is preserved across the full $\\theta$ range (Table~\\ref{tab:theta_sensitivity}).\nAll four decoding strategies likewise yield $\\Kempirical = 2$ at $\\theta{=}0.60$ (1v2 $\\auc \\in [0.687, 0.704]$; Table~\\ref{tab:s2_decoding}).\n\n%% ====================================================================\n\\subsection{Generator-Independent Transfer}\n\\label{sec:transfer}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig3_transfer_heatmap.pdf}\n\\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\\leftrightarrow$OLMo: 90--92\\%; Qwen-rewrite$\\to$continuation: 61--63\\%.}\n\\label{fig:transfer_heatmap}\n\\end{figure}\n\nContinuation-mode classifiers transfer well across generators (Figure~\\ref{fig:transfer_heatmap}; full matrix in Table~\\ref{tab:s1_transfer}): Pythia$\\leftrightarrow$OLMo retains 90--92\\%, Qwen-cont$\\leftrightarrow$Pythia 84--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\% (0v1 cross-model $\\auc > 0.96$ for all pairs).\nQwen-rewrite classifiers transfer poorly (61--63\\%), consistent with reliance on mode-specific artifacts rather than generalizable depth features.\n\n\\paragraph{Cross-scorer validation.}\nReplacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\\ref{tab:crossscorer}).\nQwen-rewrite $\\Kempirical$ remains 2 under all scorers; Qwen-continuation drops to 1 (1v2 $\\auc$: $0.6112 \\to 0.5923/0.5858$), consistent with its marginality under self-scoring.\nBoth alternative scorers agree on $\\Kempirical$ per generation mode, indicating that $\\Kempirical$ is governed by the generation process rather than the scorer.\nFor arXiv, cross-scoring with Pythia-1.4B preserves $\\Kempirical{=}3$ for three of four generators (Qwen-1.5B, LLaMA-8B, Mistral-7B; 2v3 $\\auc$ range: 0.608--0.632).\nQwen-7B exhibits a borderline decrease to $\\Kempirical{=}2$ (2v3 $\\auc = 0.599$ vs.\\ $0.626$ self-scored, $\\Delta = -2.7$\\,pp; 3/5 folds above $\\theta$), consistent with the Qwen family's scorer sensitivity observed on C4 and Wikipedia.\nBootstrap CIs (10{,}000 resamples) confirm $\\Kempirical{=}3$ for Qwen-1.5B (CI lower $= 0.617$) and LLaMA-8B (CI lower $= 0.605$); for Mistral-7B (CI: $[0.593, 0.622]$) and Qwen-7B (CI: $[0.584, 0.613]$), the CI straddles $\\theta$, indicating that their $\\Kempirical{=}3$ assignment is sensitive to resampling variance (Table~\\ref{tab:arxiv_crossscorer_ci}).\nA three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair; $N{=}300$; Table~\\ref{tab:anova_crossscorer}) confirms that Depth-Pair dominates variance ($\\eta^2_p = 0.998$); Scorer is statistically significant ($p < .001$) but practically minor ($\\eta^2_p = 0.192$), consistent with a detectable but small scorer influence on absolute discriminability.\n\n%% ====================================================================\n\\subsection{Feature Ordering and Generation Mode}\n\\label{sec:feature_degradation}\n\\label{sec:generation_mode}\n\nAmong continuation-mode models, single-feature $\\auc$ rankings are highly correlated ($\\rho \\geq 0.85$; Table~\\ref{tab:top_features}).\nThe top-3 features (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}, \\texttt{surp\\_d2\\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability; however, no single feature subset of size ${<}8$ reliably sustains $\\Kempirical{=}2$ (Appendix~\\ref{sec:feature_subset}).\nQwen-rewrite diverges (\\texttt{freq\\_entropy} dominates), consistent with its poor cross-model transfer (61--63\\%).\nWithin Qwen, rewrite yields 1v2 $\\auc = 0.6955$ vs.\\ continuation's $0.6112$ ($\\Delta = +8.4$\\,pp); continuation mode is therefore recommended as the canonical condition.\n\n%% ====================================================================\n\\subsection{Neural Probe}\n\\label{sec:neural_probe}\n\nReplacing the 15D features with frozen encoder hidden states (MLP probe; Table~\\ref{tab:neural_probe_crossmodel}), Qwen achieves $\\Kempirical^{\\text{neural}} = 3$ (2v3 $\\auc = 0.6159$), while Pythia and OLMo remain at $\\Kempirical^{\\text{neural}} = 2$ ($\\auc_{2v3}$: 0.5963, 0.5892).\nThe Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\\ref{sec:transfer}); the 15D features yield consistent $\\Kempirical = 2$ across all families.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\\ $d{+}1$ text. $\\Kempirical^{\\text{neural}}$: maximum depth where AUC exceeds $\\theta = 0.60$.}\n\\label{tab:neural_probe_crossmodel}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & $\\Kempirical^{\\text{neural}}$ \\\\\n\\midrule\nQwen-1.5B  & 0.6159 & $[0.610,\\,0.622]$ & 3 \\\\\nPythia-1.4B & 0.5963 & $[0.589,\\,0.603]$ & 2 \\\\\nOLMo-1B    & 0.5892 & $[0.582,\\,0.597]$ & 2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Cross-Domain Variation}\n\\label{sec:cross_domain}\n\nThe preceding experiments use C4 (general web text).\nTo test whether $\\Kempirical$ reflects domain structure or model identity, we evaluate on arXiv abstracts ($n{=}2{,}200$ per model) and Wikipedia ($n{=}5{,}000$ per model) across six model configurations spanning four architecture families (Table~\\ref{tab:domain_kstar}).\n\n\\paragraph{arXiv ($\\Kempirical{=}3$): five-model cross-validation.}\nAll five domain-competent models yield $\\Kempirical{=}3$ on arXiv, with boundary-pair $\\auc$ (2v3) ranging from 0.6215 to 0.6545, all exceeding $\\theta$.\nThe elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\\ ${\\sim}0.01$ for C4): formulaic features (LaTeX formatting, citation patterns, mathematical notation) degrade slowly under autoregressive generation and supply persistent depth signal across four architecture families and 1.4B--8B parameters.\nOLMo-1B constitutes a capacity failure rather than a counter-example; its arXiv generations are entirely out-of-domain (0v1 JSD $= 0.33$, near-total information loss at the first step), yielding $\\Kempirical{=}1$.\nMistral-7B provides the strongest domain-dependence evidence: $\\Kempirical{=}1$ on C4 (Section~\\ref{sec:boundary_cases}) but $\\Kempirical{=}3$ on arXiv, confirming that domain structure alone can shift $\\Kempirical$ by two levels within the same model.\n\n\\paragraph{Wikipedia ($\\Kempirical{=}1$): single-generation saturation.}\nWith scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield $\\Kempirical{=}1$ on Wikipedia: 1v2 $\\auc$ ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below $\\theta$.\nWikipedia represents the simplest domain tested; its encyclopedic regularity provides minimal structural signal beyond the 0v1 boundary, and a single generation pass suffices for complete saturation.\nA same-family scorer confound inflates the apparent $\\Kempirical$ for Qwen generators: Qwen-1.5B scoring yields $\\Kempirical{=}2$ (1v2 $\\auc \\approx 0.61$--$0.62$), but cross-family scoring reduces 1v2 by 2.4\\,pp to below $\\theta$ (Appendix~\\ref{sec:wiki_domain}).\nThis +1 depth bias under same-family scoring is specific to Qwen generators on Wikipedia and does not affect C4 results (Section~\\ref{sec:transfer}).\n\n\\paragraph{Domain as the sole dominant factor.}\nWith the scorer confound controlled, the domain ordering is uniform across all tested models: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $>$ Wikipedia ($\\Kempirical{=}1$).\nNeither model scale (1B--14B), architecture family, nor decoding strategy alters this ordering, establishing source-domain structural complexity as the primary determinant of $\\Kempirical$.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Domain $\\times$ Model $\\Kempirical$ matrix (scorer-controlled). Wikipedia values use cross-family scorer (Pythia-1.4B). $^*$OLMo arXiv: capacity failure (out-of-domain generation). $^\\dagger$Raw same-family scoring yields $\\Kempirical{=}2$; controlled value shown (Appendix~\\ref{sec:wiki_domain}).}\n\\label{tab:domain_kstar}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{C4} & \\textbf{arXiv} & \\textbf{Wikipedia} \\\\\n\\midrule\nQwen-1.5B    & 2 & 3 & 1$^\\dagger$ \\\\\nQwen-7B      & 2 & 3 & 1$^\\dagger$ \\\\\nPythia-1.4B  & 2 & 3 & 1 \\\\\nOLMo-1B      & 2 & 1$^*$ & 1 \\\\\nLLaMA-3.1-8B & 2 & 3 & 1 \\\\\nMistral-7B   & 1 & 3 & 1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Binary Detector Confidence}\n\\label{sec:binary_confidence}\n\nBinary detectors (DivEye~\\cite{basani2026diveye}, Binoculars~\\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\\rho| = 0.06$--$0.46$; Table~\\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\\leq 0.199$ vs.\\ 0.167 baseline), pairwise $\\auc$ yields $\\Kempirical^{\\text{binary}} \\leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.\nThe observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.\n",
      "numLines": 169,
      "startLine": 1,
      "totalLines": 169
    }
  },
  "sourceToolAssistantUUID": "a0d8ec17-07b6-44f3-bd17-da983dbd31c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 35 · 2026-05-18T09:57:28.831Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SefoZpbwuZKk9xRPaSicn1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19bf5a08-4a5a-4096-8d6c-972423397416",
  "isSidechain": false,
  "requestId": "req_011Cb9qRLp986cC7TnawwQyz",
  "type": "assistant",
  "uuid": "73e922e0-04b9-4cd7-8370-932af1dedc12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112y4EvtQMpCoHwr4q9U1A4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13143,
      "cache_read_input_tokens": 29727,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 29727,
          "cache_creation_input_tokens": 13143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13143
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-18T09:57:28.836Z_

<details><summary>↩ Tool result · `toolu_01SefoZpbwuZKk9xRPaSicn1`</summary>

```text
1	\section{Application: \texorpdfstring{$\Kstar$}{K*}-Aware Data Filtering}
2	\label{sec:filtering}
3	
4	We test whether $\Kempirical$ has predictive value for curation strategy selection, using a single-model setup (Qwen2.5-1.5B-Instruct) as proof of concept.
5	$\Kempirical = 2$ predicts that binary curation should suffice, and that graduated performance should converge toward binary as the decay steepness increases.
6	We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} ($w = 1 - P(\text{synthetic})$ from 15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \cdot \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal} (retain above median), and (vi)~\textbf{DSIR}~\citep{xie2023dsir}.
7	We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU (a multitask language understanding benchmark) and HellaSwag (a commonsense reasoning benchmark) across 5 seeds (51 total runs: 5 base strategies $\times$ 5 seeds $+$ 5 graduated-$\alpha$ values $\times$ 5 seeds $+$ 1 base-model reference; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \exp(-\alpha \hat{d})$. Mean $\pm$ std over 5 seeds. Full $\alpha$ sweep in Appendix~\ref{sec:extended_limitations}.}
13	\label{tab:tab_filtering_main}
14	\resizebox{\columnwidth}{!}{\input{tables/tab_filtering_main}}
15	\end{table}
16	
17	Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
18	These effects are measured in a 100\% synthetic upper-bound setting; real-world contamination ratios are typically lower, and effect sizes would scale accordingly.
19	The strategy ordering is interpretable through $\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduated strategies assign weights to depths 2--5 based on near-random classifier outputs, injecting noise.
20	Graduated filtering converges monotonically toward binary: at $\alpha{=}0.9$, it matches binary-ours on HellaSwag exactly ($\Delta = 0$, $p_{\text{corr}} = 1.00$) but remains significantly worse on MMLU ($p_{\text{corr}} = 0.011$).
21	DSIR is indistinguishable from no-filter, confirming that depth-aware features are necessary for curation in recursively contaminated corpora (Figure~\ref{fig:filtering_strategies} in Appendix).
22	Binary filtering retains a consistent advantage across contamination levels (10--50\%), with effect sizes diminishing 3--6$\times$ relative to the 100\% setting; graduated weighting remains indistinguishable from no-filter at all tested ratios, confirming that depth assignments beyond $\Kempirical$ inject noise regardless of severity (Appendix~\ref{sec:dose_response}).
23	Cross-model replication on Pythia-1.4B confirms the binary $>$ graduated ordering (Appendix~\ref{sec:pythia_filtering}), consistent with $\Kempirical{=}2$ predicting binary filtering as optimal granularity.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73e922e0-04b9-4cd7-8370-932af1dedc12",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "59f7d2fd-3c7c-482d-856d-9ead101e4649",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex",
      "content": "\\section{Application: \\texorpdfstring{$\\Kstar$}{K*}-Aware Data Filtering}\n\\label{sec:filtering}\n\nWe test whether $\\Kempirical$ has predictive value for curation strategy selection, using a single-model setup (Qwen2.5-1.5B-Instruct) as proof of concept.\n$\\Kempirical = 2$ predicts that binary curation should suffice, and that graduated performance should converge toward binary as the decay steepness increases.\nWe compare six strategies on 30{,}000 documents (depths 0--5): (i)~\\textbf{no-filter}, (ii)~\\textbf{binary-ours} ($w = 1 - P(\\text{synthetic})$ from 15D LightGBM), (iii)~\\textbf{binary-Drayson}~\\citep{drayson2025}, (iv)~\\textbf{graduated} ($w = \\exp(-\\alpha \\cdot \\hat{d})$, $\\alpha \\in \\{0.1,\\ldots,0.9\\}$), (v)~\\textbf{surprisal} (retain above median), and (vi)~\\textbf{DSIR}~\\citep{xie2023dsir}.\nWe fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\\alpha_{\\text{LoRA}}{=}16$) for 3 epochs on MMLU (a multitask language understanding benchmark) and HellaSwag (a commonsense reasoning benchmark) across 5 seeds (51 total runs: 5 base strategies $\\times$ 5 seeds $+$ 5 graduated-$\\alpha$ values $\\times$ 5 seeds $+$ 1 base-model reference; this 100\\% synthetic setting is an upper bound~\\cite{shumailov2024collapse, dohmatob2024model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \\exp(-\\alpha \\hat{d})$. Mean $\\pm$ std over 5 seeds. Full $\\alpha$ sweep in Appendix~\\ref{sec:extended_limitations}.}\n\\label{tab:tab_filtering_main}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_filtering_main}}\n\\end{table}\n\nBinary-ours minimizes MMLU degradation most effectively (Table~\\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\\,pp (no-filter) to $-$0.77\\,pp (${\\sim}$50\\% reduction; $p_{\\text{corr}} < 0.05$ vs.\\ all alternatives).\nThese effects are measured in a 100\\% synthetic upper-bound setting; real-world contamination ratios are typically lower, and effect sizes would scale accordingly.\nThe strategy ordering is interpretable through $\\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduated strategies assign weights to depths 2--5 based on near-random classifier outputs, injecting noise.\nGraduated filtering converges monotonically toward binary: at $\\alpha{=}0.9$, it matches binary-ours on HellaSwag exactly ($\\Delta = 0$, $p_{\\text{corr}} = 1.00$) but remains significantly worse on MMLU ($p_{\\text{corr}} = 0.011$).\nDSIR is indistinguishable from no-filter, confirming that depth-aware features are necessary for curation in recursively contaminated corpora (Figure~\\ref{fig:filtering_strategies} in Appendix).\nBinary filtering retains a consistent advantage across contamination levels (10--50\\%), with effect sizes diminishing 3--6$\\times$ relative to the 100\\% setting; graduated weighting remains indistinguishable from no-filter at all tested ratios, confirming that depth assignments beyond $\\Kempirical$ inject noise regardless of severity (Appendix~\\ref{sec:dose_response}).\nCross-model replication on Pythia-1.4B confirms the binary $>$ graduated ordering (Appendix~\\ref{sec:pythia_filtering}), consistent with $\\Kempirical{=}2$ predicting binary filtering as optimal granularity.\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  },
  "sourceToolAssistantUUID": "73e922e0-04b9-4cd7-8370-932af1dedc12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 37 · 2026-05-18T09:57:29.306Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WN1yX5FF6a1qXSGQH2eBwo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59f7d2fd-3c7c-482d-856d-9ead101e4649",
  "isSidechain": false,
  "requestId": "req_011Cb9qRLp986cC7TnawwQyz",
  "type": "assistant",
  "uuid": "67b49fbc-68c6-4d7c-a941-982cc15136e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112y4EvtQMpCoHwr4q9U1A4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13143,
      "cache_read_input_tokens": 29727,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 29727,
          "cache_creation_input_tokens": 13143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13143
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-18T09:57:29.311Z_

<details><summary>↩ Tool result · `toolu_01WN1yX5FF6a1qXSGQH2eBwo`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	\label{sec:why_kstar}
4	\label{sec:one_wash}
5	\label{sec:negative_graduated}
6	\label{sec:repr_dependence}
7	\label{sec:boundary_cases}
8	\label{sec:length_confound}
9	
10	\begin{figure}[t]
11	\centering
12	\includegraphics[width=\columnwidth]{figures/fig_jsd_decay.pdf}
13	\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\Kempirical{=}2$; dashed purple: Mistral-7B ($\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\Kempirical{=}3$); dotted red: retrain-chain ($\Kempirical{\geq}4$). C4 models exhibit a sharp cliff ($\lambda \approx 2.2$--$3.5$), while arXiv decays gradually ($\lambda \approx 1.0$) and retrain-chain shows no cliff ($\lambda = 0.285$).}
14	\label{fig:jsd_decay}
15	\end{figure}
16	
17	\paragraph{One-wash laundering (web text).}
18	For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
19	A single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.
20	Converging evidence supports a data-intrinsic interpretation: OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 8--38\% (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).
21	
22	\paragraph{JSD decay and the discrimination boundary.}
23	Token-level Jensen-Shannon Divergence (JSD) between adjacent generations reveals two distinct decay regimes (Figure~\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\times$, median ${\sim}$15$\times$) followed by rapid convergence to a noise floor, while arXiv decays ${\sim}$3$\times$ slower ($\lambda \approx 1.0$ vs.\ $2.9$).
24	Cross-model consistency indicates that $G_\delta$ contraction rate is domain-governed; the retrain-chain profile ($\lambda = 0.285$, no sharp cliff) reflects model-adaptation artifacts rather than text-intrinsic loss (Appendix~\ref{sec:jsd_extended}).
25	
26	\paragraph{Graduated filtering failure.}
27	For web text, 2v3 $\auc < \theta$ across all model configurations, so depth assignments for $d \geq 2$ approximate random labels; graduated weighting injects noise, explaining convergence toward binary at high $\alpha$ (Appendix~\ref{sec:extended_limitations}).
28	The strategy ordering binary $>$ graduated aligns with the $\Kempirical{=}2$ prediction: graduated approaches cannot exploit depth information that does not exist beyond the discrimination boundary.
29	DSIR fails differently: bigram hashing captures domain shift but not depth-correlated signatures (pattern persists across 10--50\% contamination ratios; Appendix~\ref{sec:dose_response}).
30	
31	\paragraph{Representation and scorer dependence.}
32	$\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$, while Pythia and OLMo match the 15D boundary at $\Kempirical^{\text{neural}} = 2$ (Table~\ref{tab:neural_probe_crossmodel}); the 15D features trade one depth level for cross-model consistency (8/9 configurations $\Kempirical{\leq}2$).
33	$\Kempirical$ can also depend on scorer family: on Wikipedia, cross-family scoring reduces $\Kempirical$ from 2 to 1 ($\Delta = -2.4$\,pp; Appendix~\ref{sec:wiki_domain}), while on C4 it preserves feature rankings ($\rho > 0.90$) and $\Kempirical$ for 6/8 configurations (Section~\ref{sec:transfer}).
34	Scorer sensitivity is inversely related to domain structural complexity; we recommend cross-family validation for new domains.
35	
36	\paragraph{Domain dependence of $\Kempirical$.}
37	C4 web text yields $\Kempirical{=}2$ (8/9 configurations, 1B--14B), while arXiv yields $\Kempirical{=}3$ across five models and four architecture families (Section~\ref{sec:cross_domain}).
38	With scorer confound controlled, all six models yield $\Kempirical{=}1$ on Wikipedia (Appendix~\ref{sec:wiki_domain}), producing a uniform ordering governed by source-domain structural complexity: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$).
39	The sole C4 exception (Mistral-7B, $\Kempirical{=}1$) has $\Kempirical{=}3$ on arXiv, reinforcing the domain-governed interpretation (Appendix~\ref{sec:boundary_extended}).
40	
41	\paragraph{Prompt-chain vs.\ retrain-chain $\Kempirical$.}
42	Retrain-chain experiments (Pythia-1.4B LoRA) yield $\Kempirical{\geq}4$ (Table~\ref{tab:retrain_ci}), far exceeding prompt-chain $\Kempirical{=}2$; the former reflects model-adaptation artifacts rather than text-level information loss (Appendix~\ref{sec:extended_limitations}).
43	
44	
45	
46	\paragraph{Why $\Kempirical$ matters.}
47	$\Kempirical{=}2$ for web text is not a negative result but a precise measurement: it rules out both $\Kempirical{=}1$ (no depth signal beyond 0v1) and $\Kempirical{\geq}3$ (graduated tracking feasible), while arXiv $\Kempirical{=}3$ confirms the framework captures real domain-level variation rather than a methodological ceiling.
48	$\Kempirical$ thus serves as a diagnostic of domain structural complexity and is directly prescriptive for curation granularity.
49	
50	
51	
52	\paragraph{Practical implications.}
53	For web text ($\Kempirical{=}2$), graduated depth weighting injects noise beyond the boundary, validating binary filtering as optimal (Section~\ref{sec:filtering}); for arXiv ($\Kempirical{=}3$), an additional depth level carries discriminative signal.
54	Mixed-domain corpora thus require domain-stratified filtering, and $\Kempirical{=}2$ provides post-hoc grounding for the binary approach of \citet{drayson2025} (segment-length sensitivity in Table~\ref{tab:s11_length_ablation}).
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67b49fbc-68c6-4d7c-a941-982cc15136e0",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "370e3fbf-cb75-4eb2-a6b1-bba04f15300f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\\label{sec:why_kstar}\n\\label{sec:one_wash}\n\\label{sec:negative_graduated}\n\\label{sec:repr_dependence}\n\\label{sec:boundary_cases}\n\\label{sec:length_confound}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_jsd_decay.pdf}\n\\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\\Kempirical{=}2$; dashed purple: Mistral-7B ($\\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\\Kempirical{=}3$); dotted red: retrain-chain ($\\Kempirical{\\geq}4$). C4 models exhibit a sharp cliff ($\\lambda \\approx 2.2$--$3.5$), while arXiv decays gradually ($\\lambda \\approx 1.0$) and retrain-chain shows no cliff ($\\lambda = 0.285$).}\n\\label{fig:jsd_decay}\n\\end{figure}\n\n\\paragraph{One-wash laundering (web text).}\nFor general web text, $\\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\\auc \\geq 0.92$), 1v2 drops by ${\\sim}$30\\,pp, and 2v3 falls below $\\theta$.\nA single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.\nConverging evidence supports a data-intrinsic interpretation: OBD achieves 96\\% depth-0 recall but only 14--22\\% for depths 2--4; frontier LLMs show 8--38\\% (McNemar $p > 0.05$ vs.\\ OBD; Table~\\ref{tab:s3_llm_zeroshot}).\n\n\\paragraph{JSD decay and the discrimination boundary.}\nToken-level Jensen-Shannon Divergence (JSD) between adjacent generations reveals two distinct decay regimes (Figure~\\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\\times$, median ${\\sim}$15$\\times$) followed by rapid convergence to a noise floor, while arXiv decays ${\\sim}$3$\\times$ slower ($\\lambda \\approx 1.0$ vs.\\ $2.9$).\nCross-model consistency indicates that $G_\\delta$ contraction rate is domain-governed; the retrain-chain profile ($\\lambda = 0.285$, no sharp cliff) reflects model-adaptation artifacts rather than text-intrinsic loss (Appendix~\\ref{sec:jsd_extended}).\n\n\\paragraph{Graduated filtering failure.}\nFor web text, 2v3 $\\auc < \\theta$ across all model configurations, so depth assignments for $d \\geq 2$ approximate random labels; graduated weighting injects noise, explaining convergence toward binary at high $\\alpha$ (Appendix~\\ref{sec:extended_limitations}).\nThe strategy ordering binary $>$ graduated aligns with the $\\Kempirical{=}2$ prediction: graduated approaches cannot exploit depth information that does not exist beyond the discrimination boundary.\nDSIR fails differently: bigram hashing captures domain shift but not depth-correlated signatures (pattern persists across 10--50\\% contamination ratios; Appendix~\\ref{sec:dose_response}).\n\n\\paragraph{Representation and scorer dependence.}\n$\\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\\Kempirical^{\\text{neural}} = 3$, while Pythia and OLMo match the 15D boundary at $\\Kempirical^{\\text{neural}} = 2$ (Table~\\ref{tab:neural_probe_crossmodel}); the 15D features trade one depth level for cross-model consistency (8/9 configurations $\\Kempirical{\\leq}2$).\n$\\Kempirical$ can also depend on scorer family: on Wikipedia, cross-family scoring reduces $\\Kempirical$ from 2 to 1 ($\\Delta = -2.4$\\,pp; Appendix~\\ref{sec:wiki_domain}), while on C4 it preserves feature rankings ($\\rho > 0.90$) and $\\Kempirical$ for 6/8 configurations (Section~\\ref{sec:transfer}).\nScorer sensitivity is inversely related to domain structural complexity; we recommend cross-family validation for new domains.\n\n\\paragraph{Domain dependence of $\\Kempirical$.}\nC4 web text yields $\\Kempirical{=}2$ (8/9 configurations, 1B--14B), while arXiv yields $\\Kempirical{=}3$ across five models and four architecture families (Section~\\ref{sec:cross_domain}).\nWith scorer confound controlled, all six models yield $\\Kempirical{=}1$ on Wikipedia (Appendix~\\ref{sec:wiki_domain}), producing a uniform ordering governed by source-domain structural complexity: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $>$ Wikipedia ($\\Kempirical{=}1$).\nThe sole C4 exception (Mistral-7B, $\\Kempirical{=}1$) has $\\Kempirical{=}3$ on arXiv, reinforcing the domain-governed interpretation (Appendix~\\ref{sec:boundary_extended}).\n\n\\paragraph{Prompt-chain vs.\\ retrain-chain $\\Kempirical$.}\nRetrain-chain experiments (Pythia-1.4B LoRA) yield $\\Kempirical{\\geq}4$ (Table~\\ref{tab:retrain_ci}), far exceeding prompt-chain $\\Kempirical{=}2$; the former reflects model-adaptation artifacts rather than text-level information loss (Appendix~\\ref{sec:extended_limitations}).\n\n\n\n\\paragraph{Why $\\Kempirical$ matters.}\n$\\Kempirical{=}2$ for web text is not a negative result but a precise measurement: it rules out both $\\Kempirical{=}1$ (no depth signal beyond 0v1) and $\\Kempirical{\\geq}3$ (graduated tracking feasible), while arXiv $\\Kempirical{=}3$ confirms the framework captures real domain-level variation rather than a methodological ceiling.\n$\\Kempirical$ thus serves as a diagnostic of domain structural complexity and is directly prescriptive for curation granularity.\n\n\n\n\\paragraph{Practical implications.}\nFor web text ($\\Kempirical{=}2$), graduated depth weighting injects noise beyond the boundary, validating binary filtering as optimal (Section~\\ref{sec:filtering}); for arXiv ($\\Kempirical{=}3$), an additional depth level carries discriminative signal.\nMixed-domain corpora thus require domain-stratified filtering, and $\\Kempirical{=}2$ provides post-hoc grounding for the binary approach of \\citet{drayson2025} (segment-length sensitivity in Table~\\ref{tab:s11_length_ablation}).\n",
      "numLines": 55,
      "startLine": 1,
      "totalLines": 55
    }
  },
  "sourceToolAssistantUUID": "67b49fbc-68c6-4d7c-a941-982cc15136e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 39 · 2026-05-18T09:57:29.667Z_

<details open><summary>🔧 Tool call — Read · `toolu_011NH8K9yNXpPg432kgx6PV5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "370e3fbf-cb75-4eb2-a6b1-bba04f15300f",
  "isSidechain": false,
  "requestId": "req_011Cb9qRLp986cC7TnawwQyz",
  "type": "assistant",
  "uuid": "e620effc-90d1-49cf-970a-3ada639898c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112y4EvtQMpCoHwr4q9U1A4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13143,
      "cache_read_input_tokens": 29727,
      "output_tokens": 735,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 735,
          "cache_read_input_tokens": 29727,
          "cache_creation_input_tokens": 13143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13143
          },
          "type": "message"
        }
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

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性**  ### Venue 信息 - **目标**: EMNLP 2026（ARR May 2026 cycle） - **Deadline**: 2026-05-25 - **格式**: ACL 双栏模板，`\\usepackage[review]{acl}`，Long…",
  "leafUuid": "90d12d4d-e7de-4c26-aa59-c8c705b29968",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on generational depth contamination detection",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Tool result

_source line 42 · 2026-05-18T09:57:31.121Z_

<details><summary>↩ Tool result · `toolu_01C4j1nqEhJXha6CL6hZfouN`</summary>

```text
# ACL Rolling Review Form: Complete Scoring Dimensions

## 1. **Reviewer Confidence**
- 5 = Positive evaluation is correct; read carefully, familiar with related work
- 4 = Quite sure; checked important points carefully
- 3 = Pretty sure; good area knowledge but didn't check all details
- 2 = Willing to defend evaluation; likely missed some details
- 1 = Not expert area or paper very difficult to understand

## 2. **Soundness**
- 5 = Excellent; one of most thorough studies seen
- 4.5, 4 = Strong; sufficient support for claims
- 3.5, 3 = Acceptable; main claims supported, minor details need work
- 2.5, 2 = Poor; major technical/methodological problems
- 1.5, 1 = Major Issues; insufficient or irrelevant to ACL

## 3. **Excitement**
- 5 = Highly Exciting; would recommend to others
- 4.5, 4 = Exciting; would mention to colleagues
- 3.5, 3 = Interesting; might mention or attend presentation
- 2.5, 2 = Potentially Interesting; doesn't resonate personally
- 1.5, 1 = Not Exciting; not aligned with community

## 4. **Overall Assessment**
- 5 = Consider for Award (top 2.5%)
- 4.5 = Borderline Award
- 4 = Conference acceptance
- 3.5 = Borderline Conference
- 3 = Findings acceptance
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle
- 1.5 = Resubmit after next cycle
- 1 = Do not resubmit

## 5. **Reproducibility**
- 5 = Results easily reproducible
- 4 = Mostly reproducible with minor variations
- 3 = Reproducible with difficulty; underspecified parameters
- 2 = Hard to reproduce; unavailable data
- 1 = Cannot reproduce

## 6. **Datasets & Software**
Both rated 1-5 scale measuring value to broader research community
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "291cc234-5005-4a78-a28b-5fad1c8184f8",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "d1becda6-7a2d-4280-8325-0042fa393113",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form: Complete Scoring Dimensions\n\n## 1. **Reviewer Confidence**\n- 5 = Positive evaluation is correct; read carefully, familiar with related work\n- 4 = Quite sure; checked important points carefully\n- 3 = Pretty sure; good area knowledge but didn't check all details\n- 2 = Willing to defend evaluation; likely missed some details\n- 1 = Not expert area or paper very difficult to understand\n\n## 2. **Soundness**\n- 5 = Excellent; one of most thorough studies seen\n- 4.5, 4 = Strong; sufficient support for claims\n- 3.5, 3 = Acceptable; main claims supported, minor details need work\n- 2.5, 2 = Poor; major technical/methodological problems\n- 1.5, 1 = Major Issues; insufficient or irrelevant to ACL\n\n## 3. **Excitement**\n- 5 = Highly Exciting; would recommend to others\n- 4.5, 4 = Exciting; would mention to colleagues\n- 3.5, 3 = Interesting; might mention or attend presentation\n- 2.5, 2 = Potentially Interesting; doesn't resonate personally\n- 1.5, 1 = Not Exciting; not aligned with community\n\n## 4. **Overall Assessment**\n- 5 = Consider for Award (top 2.5%)\n- 4.5 = Borderline Award\n- 4 = Conference acceptance\n- 3.5 = Borderline Conference\n- 3 = Findings acceptance\n- 2.5 = Borderline Findings\n- 2 = Resubmit next cycle\n- 1.5 = Resubmit after next cycle\n- 1 = Do not resubmit\n\n## 5. **Reproducibility**\n- 5 = Results easily reproducible\n- 4 = Mostly reproducible with minor variations\n- 3 = Reproducible with difficulty; underspecified parameters\n- 2 = Hard to reproduce; unavailable data\n- 1 = Cannot reproduce\n\n## 6. **Datasets & Software**\nBoth rated 1-5 scale measuring value to broader research community",
    "durationMs": 6104,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "291cc234-5005-4a78-a28b-5fad1c8184f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 43 · 2026-05-18T09:57:31.130Z_

```json
{
  "parentUuid": "d1becda6-7a2d-4280-8325-0042fa393113",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "996a920d-fb1f-40d3-8d34-c8882e3f57ec",
  "timestamp": "2026-05-18T09:57:31.130Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 44 · 2026-05-18T09:57:34.893Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the appendix files and table files for a thorough review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "996a920d-fb1f-40d3-8d34-c8882e3f57ec",
  "isSidechain": false,
  "requestId": "req_011Cb9qSLs9frHhrSZSGCbqi",
  "type": "assistant",
  "uuid": "2891be66-ed92-4fd6-ae36-ca9c99bb8b21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VfxG7JyWRitavZy524FYK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 13741,
      "cache_creation_input_tokens": 1397,
      "cache_read_input_tokens": 42870,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1397,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 13741,
          "output_tokens": 293,
          "cache_read_input_tokens": 42870,
          "cache_creation_input_tokens": 1397,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1397
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-18T09:57:35.391Z_

继续读取附录和表格文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2891be66-ed92-4fd6-ae36-ca9c99bb8b21",
  "isSidechain": false,
  "requestId": "req_011Cb9qSLs9frHhrSZSGCbqi",
  "type": "assistant",
  "uuid": "f8e9193e-0833-4fd3-90cd-d3ee74f06c0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VfxG7JyWRitavZy524FYK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 13741,
      "cache_creation_input_tokens": 1397,
      "cache_read_input_tokens": 42870,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1397,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 13741,
          "output_tokens": 293,
          "cache_read_input_tokens": 42870,
          "cache_creation_input_tokens": 1397,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1397
          },
          "type": "message"
        }
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

_source line 46 · 2026-05-18T09:57:37.256Z_

<details open><summary>🔧 Tool call — Read · `toolu_014H6yWm7MuJ559Fnn72oxGX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8e9193e-0833-4fd3-90cd-d3ee74f06c0b",
  "isSidechain": false,
  "requestId": "req_011Cb9qSLs9frHhrSZSGCbqi",
  "type": "assistant",
  "uuid": "a186ca4e-9f2c-4fc7-b1c4-9243c7333e61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VfxG7JyWRitavZy524FYK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 13741,
      "cache_creation_input_tokens": 1397,
      "cache_read_input_tokens": 42870,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1397,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 13741,
          "output_tokens": 293,
          "cache_read_input_tokens": 42870,
          "cache_creation_input_tokens": 1397,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1397
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-18T09:57:38.205Z_

<details><summary>↩ Tool result · `toolu_0142QUXX3LZSEZJGzECAgYza`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba02b295-7b05-4ea2-be51-6b08377e9fdc",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "ffeca9ec-6915-40f3-a953-288812c96a91",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 8,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "ba02b295-7b05-4ea2-be51-6b08377e9fdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 48 · 2026-05-18T09:57:37.516Z_

<details><summary>↩ Tool result · `toolu_014H6yWm7MuJ559Fnn72oxGX`</summary>

```text
1	\appendix
2	\section{Supplementary Figures}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
7	\caption{Downstream performance of all filtering strategies (5 seeds, $\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}
8	\label{fig:filtering_strategies}
9	\end{figure}
10	
11	\begin{figure}[t]
12	  \centering
13	  \includegraphics[width=\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}
14	  \caption{Pairwise $\auc$ decay curves for five model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\Kempirical=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}
15	  \label{fig:s1_auc_decay_ci}
16	\end{figure}
17	
18	\section{Supplementary Tables}
19	
20	%%% Feature ranking table (moved from main text)
21	\begin{table}[t]
22	\centering
23	\small
24	\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
25	\label{tab:top_features}
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{cllll}
28	\toprule
29	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
30	\midrule
31	1 & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \texttt{freq\_entropy} & \textbf{\texttt{surp\_d1\_std}} \\
32	2 & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_std}} \\
33	3 & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_d2\_std}} \\
34	\bottomrule
35	\end{tabular}}
36	\end{table}
37	
38	%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)
39	\begin{table*}[t]
40	  \centering
41	  \caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}
42	  \label{tab:s1_transfer}
43	  \begin{tabular}{lcccc}
44	    \toprule
45	    \multirow{2}{*}{\textbf{Train Model}} & \multicolumn{4}{c}{\textbf{Test Model}} \\
46	    \cmidrule(lr){2-5}
47	    & Qwen-rw & Pythia & OLMo & Qwen-cont \\
48	    \midrule
49	    Qwen-rw   & \textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\
50	    Pythia    & 0.2718 & \textbf{0.3856} & 0.3531 & 0.3287 \\
51	    OLMo      & 0.2768 & 0.3450 & \textbf{0.3822} & 0.3244 \\
52	    Qwen-cont & 0.3440 & 0.3284 & 0.3112 & \textbf{0.3875} \\
53	    \bottomrule
54	  \end{tabular}
55	  \vspace{4pt}
56	
57	  \footnotesize
58	  \textit{Transfer retention} between models $A$ and $B$ is defined as $\frac{1}{2}\bigl(\frac{\mathrm{acc}(A \to B)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}} + \frac{\mathrm{acc}(B \to A)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}}\bigr)$.
59	  Notable pairs: Pythia$\leftrightarrow$OLMo 91--92\%, Qwen-cont$\leftrightarrow$Pythia 83--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\%, Qwen-rw$\to$Pythia/OLMo 61--63\%.
60	\end{table*}
61	
62	%%% Table S2: Decoding Ablation AUC (exp-003)
63	\begin{table*}[t]
64	  \centering
65	  \caption{Pairwise AUC with bootstrap 95\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\,vs.\,2 and 2\,vs.\,3 marks the empirical detectability boundary $\Kempirical=2$. Bottom rows report cross-configuration Spearman $\rho$ on per-feature discriminative-power rankings.}
66	  \label{tab:s2_decoding}
67	  \footnotesize
68	  \begin{tabular}{lcccc}
69	    \toprule
70	    \textbf{Depth Pair} & \textbf{Greedy} & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
71	    \midrule
72	    0 vs.\ 1 & $.980\;[.977,\,.982]$ & $.995\;[.993,\,.996]$ & $.988\;[.986,\,.990]$ & $.998\;[.998,\,.999]$ \\
73	    1 vs.\ 2 & $.689\;[.680,\,.698]$ & $.687\;[.677,\,.695]$ & $.689\;[.680,\,.697]$ & $.704\;[.695,\,.713]$ \\
74	    \cmidrule(lr){1-5}
75	    2 vs.\ 3 & $.561\;[.552,\,.571]$ & $.592\;[.582,\,.601]$\rlap{$^\dagger$} & $.590\;[.581,\,.600]$ & $.582\;[.572,\,.592]$ \\
76	    3 vs.\ 4 & $.540\;[.531,\,.550]$ & $.547\;[.537,\,.557]$ & $.539\;[.529,\,.549]$ & $.529\;[.519,\,.540]$ \\
77	    4 vs.\ 5 & $.514\;[.503,\,.524]$ & $.507\;[.496,\,.517]^{\ddagger}$ & $.535\;[.524,\,.545]$ & $.524\;[.513,\,.535]$ \\
78	    \midrule
79	    \multicolumn{5}{l}{\textbf{Cross-config feature Spearman $\rho$}} \\
80	    \midrule
81	    \multicolumn{2}{l}{Greedy vs.\ Nuc $p{=}0.9$} & 0.600 &
82	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}0.7$} & 0.782 \\
83	    \multicolumn{2}{l}{Greedy vs.\ $T{=}0.7$} & 0.914 &
84	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}1.2$} & 0.893 \\
85	    \multicolumn{2}{l}{Greedy vs.\ $T{=}1.2$} & 0.532 &
86	    \multicolumn{1}{l}{$T{=}0.7$ vs.\ $T{=}1.2$} & 0.668 \\
87	    \bottomrule
88	    \multicolumn{5}{l}{${}^{\dagger}$\,CI upper bound (0.601) marginally exceeds $\theta{=}0.60$ by 0.001.} \\
89	    \multicolumn{5}{l}{${}^{\ddagger}$\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}
90	  \end{tabular}
91	\end{table*}
92	
93	%%% Table S2b: Extended K* CI (all models including new additions)
94	\begin{table*}[t]
95	  \centering
96	  \footnotesize
97	  \caption{Extended pairwise $\auc$ with bootstrap 95\% CIs for all 9 model configurations.
98	  This table extends Table~\ref{tab:kstar_ci} in the main text with Qwen-base, Qwen-14B, LLaMA-8B, and Mistral-7B.
99	  8/9 yield $\Kempirical = 2$; Mistral-7B yields $\Kempirical = 1$ (1v2 $\auc < \theta$).}
100	  \label{tab:kstar_ci_extended}
101	  \resizebox{\textwidth}{!}{%
102	  \begin{tabular}{lcccccccccccccccccc}
103	    \toprule
104	     & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} & \multicolumn{2}{c}{Qwen-14B\rlap{$^\ddagger$}} & \multicolumn{2}{c}{Qwen-base} & \multicolumn{2}{c}{LLaMA-8B} & \multicolumn{2}{c}{Mistral-7B} \\
105	    \cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}\cmidrule(lr){12-13}\cmidrule(lr){14-15}\cmidrule(lr){16-17}\cmidrule(lr){18-19}
106	     & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
107	    \midrule
108	    0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\,.967] & .960 & [.956,\,.963] & .987 & [.985,\,.989] & .9225 & [.918,\,.927] & .930 & [.925,\,.935] \\
109	    1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .6145 & [.605,\,.625]\rlap{$^*$} & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} & .621 & [.612,\,.630]\rlap{$^*$} & .626 & [.617,\,.635]\rlap{$^*$} & .6123 & [.603,\,.622]\rlap{$^*$} & .594 & [.584,\,.603] \\
110	    2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .5496 & [.540,\,.560] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] & .549 & [.539,\,.559] & .550 & [.540,\,.560] & .5518 & [.542,\,.562] & .548 & [.538,\,.558] \\
111	    3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & & .524 & [.514,\,.535] & .529 & [.519,\,.540] & .5203 & [.510,\,.531] & .521 & \\
112	    4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & & .515 & [.505,\,.527] & .518 & [.508,\,.529] & .5089 & [.499,\,.519] & .510 & \\
113	    \bottomrule
114	    \multicolumn{19}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all boundary comparisons. Mistral-7B 1v2: $p = 0.001$ but $\auc < \theta$, hence $\Kempirical{=}1$.} \\
115	    \multicolumn{19}{l}{\footnotesize $^\ddagger$Qwen-7B: Qwen2.5-7B (fp16); Qwen-14B: Qwen2.5-14B; scorer: Qwen2.5-1.5B.}
116	  \end{tabular}}
117	
118	\end{table*}
119	
120	%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)
121	\begin{table*}[t]
122	  \centering
123	  \caption{LLM zero-shot depth classification: $5{\times}5$ confusion matrices
124	    (Exp-011). Both frontier LLMs achieve high binary detection accuracy
125	    (GPT-5.5: 0.8780; Claude Opus~4.6: 0.8818) but near-chance 5-class
126	    accuracy (${\sim}0.33$ vs.\ OBD-LightGBM baseline 0.386, evaluated on the full test set $N{=}5{,}000$). GPT-5.5
127	    strongly identifies depth-0 text (recall${=}0.7700$) but collapses on
128	    depth-4 (recall${=}0.0800$), misclassifying 50/100 depth-4 samples as
129	    depth-2. Claude Opus~4.6 shows more uniform errors across depths 1--4,
130	    with depth-4 recall (0.3700) substantially exceeding GPT-5.5.
131	    Per-depth recall comparison with OBD-LightGBM in Table~\ref{tab:s3c_perdepth}.}
132	  \label{tab:s3_llm_zeroshot}
133	
134	  \vspace{0.5em}
135	  \begin{subtable}{0.48\textwidth}
136	    \centering
137	    \caption{GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)}
138	    \label{tab:s3a_gpt55}
139	    \small
140	    \begin{tabular}{lcccccc}
141	      \toprule
142	      & \multicolumn{5}{c}{Predicted Depth} & \\
143	      \cmidrule(lr){2-6}
144	      True & 0 & 1 & 2 & 3 & 4 & Rec. \\
145	      \midrule
146	      0 & \textbf{77} & 18 &  4 &  0 &  1 & .770 \\
147	      1 &  9 & \textbf{19} & 36 & 24 & 12 & .190 \\
148	      2 &  8 & 10 & \textbf{38} & 35 &  9 & .380 \\
149	      3 & 10 & 16 & 35 & \textbf{24} & 15 & .240 \\
150	      4 & 11 & 13 & 50 & 18 &  \textbf{8} & .080 \\
151	      \bottomrule
152	    \end{tabular}
153	  \end{subtable}
154	  \hfill
155	  \begin{subtable}{0.48\textwidth}
156	    \centering
157	    \caption{Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)}
158	    \label{tab:s3b_claude}
159	    \small
160	    \begin{tabular}{lcccccc}
161	      \toprule
162	      & \multicolumn{5}{c}{Predicted Depth} & \\
163	      \cmidrule(lr){2-6}
164	      True & 0 & 1 & 2 & 3 & 4 & Rec. \\
165	      \midrule
166	      0 & \textbf{69} & 26 &  3 &  0 &  2 & .690 \\
167	      1 &  8 & \textbf{21} & 32 & 11 & 28 & .210 \\
168	      2 &  6 & 36 & \textbf{28} &  5 & 25 & .280 \\
169	      3 &  7 & 20 & 31 & \textbf{10} & 31 & .100 \\
170	      4 &  7 & 28 & 22 &  6 & \textbf{37} & .370 \\
171	      \bottomrule
172	    \end{tabular}
173	  \end{subtable}
174	\end{table*}
175	
176	\begin{table}[t]
177	  \centering
178	  \small
179	  \caption{Per-depth recall (\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\geq 2$, consistent with $\Kempirical = 2$.}
180	  \label{tab:s3c_perdepth}
181	  \resizebox{\columnwidth}{!}{%
182	  \begin{tabular}{lccccc}
183	    \toprule
184	    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\
185	    \midrule
186	    OBD-LightGBM & \textbf{96} & \textbf{39} & 14 & 19 & 22 \\
187	    GPT-5.5      & 77 & 19 & \textbf{38} & \textbf{24} &  8 \\
188	    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \textbf{37} \\
189	    \bottomrule
190	  \end{tabular}}
191	\end{table}
192	
193	%%% Table: Token Length and EOS Truncation Analysis
194	\begin{table*}[t]
195	  \centering
196	  \small
197	  \caption{Mean subword token count per depth and EOS truncation rate (\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend within any model; the 0v1 length asymmetry (human texts shorter) makes detection \emph{more conservative}, not inflated. See Section~\ref{sec:length_confound} for discussion.}
198	  \label{tab:token_length}
199	  \begin{tabular}{lcccccccc}
200	    \toprule
201	    & \multicolumn{6}{c}{\textbf{Mean Token Count}} & & \\
202	    \cmidrule(lr){2-7}
203	    \textbf{Model} & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 & Depth 5 & \textbf{EOS Trunc.\ (\%)} & \textbf{Severity} \\
204	    \midrule
205	    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\
206	    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\
207	    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negligible \\
208	    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Moderate \\
209	    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\
210	    \midrule
211	    \multicolumn{9}{l}{\textit{Decoding ablation (Qwen-rw 1.5B)}} \\
212	    \quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\
213	    \quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\
214	    \quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\
215	    \quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\
216	    \bottomrule
217	  \end{tabular}
218	
219	  \vspace{4pt}
220	  \footnotesize
221	  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.
222	\end{table*}
223	
224	%%% Table S4: Dataset Statistics
225	\begin{table}[t]
226	  \centering
227	  \small
228	  \caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}
229	  \label{tab:s4_dataset_stats}
230	  \resizebox{\columnwidth}{!}{%
231	  \begin{tabular}{clrl}
232	    \toprule
233	    \textbf{Depth} & \textbf{$N$ samples} & \textbf{Mean tokens} & \textbf{Source} \\
234	    \midrule
235	    0 & 5{,}000 & 147.8 & C4 validation (human) \\
236	    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\
237	    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\
238	    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\
239	    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
240	    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
241	    \midrule
242	    \multicolumn{2}{l}{Total} & \multicolumn{2}{l}{30{,}000 samples} \\
243	    \bottomrule
244	  \end{tabular}}
245	\end{table}
246	
247	%%% Table S5: Complete 15-D Feature Descriptions
248	\begin{table*}[t]
249	  \centering
250	  \caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}
251	  \label{tab:s5_features}
252	  \begin{tabular}{llp{0.45\textwidth}l}
253	    \toprule
254	    \textbf{Group} & \textbf{Feature} & \textbf{Description} & \textbf{Range} \\
255	    \midrule
256	    \multirow{9}{*}{\rotatebox[origin=c]{90}{\textsc{Surprisal}}}
257	    & \texttt{surp\_mean}   & Mean token surprisal $\frac{1}{T}\sum_t -\log p(x_t \mid x_{&lt;t})$ & $\mathbb{R}^+$ \\
258	    & \texttt{surp\_std}    & Standard deviation of token surprisal & $\mathbb{R}^+$ \\
259	    & \texttt{surp\_skew}   & Skewness of the surprisal distribution & $\mathbb{R}$ \\
260	    & \texttt{surp\_kurt}   & Excess kurtosis of the surprisal distribution & $\mathbb{R}$ \\
261	    & \texttt{surp\_d1\_mean} & Mean of first-order surprisal differences $\Delta s_t = s_{t+1} - s_t$ & $\mathbb{R}$ \\
262	    & \texttt{surp\_d1\_std}  & Std of first-order surprisal differences & $\mathbb{R}^+$ \\
263	    & \texttt{surp\_d1\_skew} & Skewness of first-order surprisal differences & $\mathbb{R}$ \\
264	    & \texttt{surp\_d2\_mean} & Mean of second-order differences $\Delta^2 s_t$ & $\mathbb{R}$ \\
265	    & \texttt{surp\_d2\_std}  & Std of second-order surprisal differences & $\mathbb{R}^+$ \\
266	    \midrule
267	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Lex}}}
268	    & \texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\
269	    & \texttt{hapax\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\
270	    & \texttt{self\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\
271	    \midrule
272	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Freq}}}
273	    & \texttt{freq\_kurtosis}  & Excess kurtosis of word frequency distribution & $\mathbb{R}$ \\
274	    & \texttt{freq\_entropy}   & Shannon entropy of word frequencies: $-\sum p_w \log_2 p_w$ & $\mathbb{R}^+$ \\
275	    & \texttt{low\_freq\_ratio} & Proportion of vocabulary with count $\leq 2$ & $[0, 1]$ \\
276	    \bottomrule
277	  \end{tabular}
278	\end{table*}
279	
280	%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap
281	\begin{table*}[t]
282	\begin{minipage}[t]{0.45\textwidth}
283	  \centering
284	  \small
285	  \captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \texttt{doc\_id} to prevent data leakage from the same seed document appearing in both train and test.}
286	  \label{tab:s6_lgbm_params}
287	  \begin{tabular}{ll}
288	    \toprule
289	    \textbf{Parameter} & \textbf{Value} \\
290	    \midrule
291	    \texttt{n\_estimators}      & 200 \\
292	    \texttt{learning\_rate}     & 0.05 \\
293	    \texttt{max\_depth}         & 6 \\
294	    \texttt{num\_leaves}        & 31 \\
295	    \texttt{verbose}            & $-1$ \\
296	    \texttt{n\_jobs}            & $-1$ (all cores) \\
297	    Cross-validation            & 5-fold GroupKFold \\
298	    Grouping key                & \texttt{doc\_id} \\
299	    Objective                   & Binary (per depth pair) \\
300	    \bottomrule
301	  \end{tabular}
302	\end{minipage}\hfill
303	\begin{minipage}[t]{0.52\textwidth}
304	  \centering
305	  \small
306	  \captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}
307	  \label{tab:s7_neural_probe}
308	  \resizebox{\textwidth}{!}{%
309	  \begin{tabular}{ll}
310	    \toprule
311	    \textbf{Component} & \textbf{Details} \\
312	    \midrule
313	    \multicolumn{2}{l}{\textit{Embedding extraction}} \\
314	    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\
315	    Representation    & Last hidden state, attention-masked avg pool \\
316	    Embedding dim     & 1536 / 2048 / 2048 \\
317	    Max sequence len   & 512 tokens \\
318	    \midrule
319	    \multicolumn{2}{l}{\textit{MLP classifier}} \\
320	    Architecture      & $d_{\text{emb}} \to 512 \to 256 \to 6$ \\
321	    Activations       & ReLU \\
322	    Dropout           & 0.1 (after each hidden layer) \\
323	    Output            & 6-class softmax \\
324	    \midrule
325	    \multicolumn{2}{l}{\textit{Training}} \\
326	    Optimizer         & Adam ($\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\
327	    Loss              & Cross-entropy \\
328	    Batch size        & 256 \\
329	    Max epochs        & 20 \\
330	    Early stopping    & Patience = 5 (validation loss) \\
331	    Cross-validation  & 5-fold GroupKFold \\
332	    \bottomrule
333	  \end{tabular}%
334	  }
335	\end{minipage}
336	\end{table*}
337	
338	%%% Table S8: Per-Model Bootstrap CI Results (exp-007)
339	\begin{table*}[t]
340	  \centering
341	  \footnotesize
342	  \caption{Pairwise AUC with bootstrap 95\% confidence intervals for four model-mode configurations (Exp-007, 1{,}000 bootstrap resamples). The horizontal rule separates depth pairs above and below the detectability threshold $\theta = 0.60$. Permutation $p$-values test $H_0\colon \auc = 0.50$. All pairs are significant at $p < 0.01$ except OLMo 3\,vs.\,4 ($p = 0.064$) and 4\,vs.\,5 ($p = 0.232$), consistent with convergence to chance at deeper generations.}
343	  \label{tab:s8_cv_folds}
344	  \begin{tabular}{lcccc}
345	    \toprule
346	    \textbf{Depth Pair} & \textbf{Qwen-rewrite} & \textbf{Pythia-1.4B} & \textbf{OLMo-1B} & \textbf{Qwen-cont} \\
347	    \midrule
348	    0 vs.\ 1
349	      & $.996\;[.995,\,.997]$
350	      & $.993\;[.992,\,.994]$
351	      & $.997\;[.996,\,.998]$
352	      & $.997\;[.996,\,.998]$ \\
353	    1 vs.\ 2
354	      & $.696\;[.686,\,.704]$
355	      & $.654\;[.645,\,.663]$
356	      & $.615\;[.605,\,.625]$
357	      & $.611\;[.602,\,.621]$ \\
358	    \cmidrule(lr){1-5}
359	    2 vs.\ 3
360	      & $.589\;[.580,\,.599]$
361	      & $.551\;[.542,\,.563]$
362	      & $.550\;[.540,\,.560]$
363	      & $.561\;[.551,\,.571]$ \\
364	    3 vs.\ 4
365	      & $.544\;[.533,\,.555]$
366	      & $.515\;[.504,\,.526]$
367	      & $.509\;[.497,\,.520]^{\dagger}$
368	      & $.541\;[.531,\,.551]$ \\
369	    4 vs.\ 5
370	      & $.534\;[.524,\,.545]$
371	      & $.514\;[.502,\,.525]$
372	      & $.505\;[.493,\,.515]^{\ddagger}$
373	      & $.514\;[.504,\,.526]$ \\
374	    \bottomrule
375	  \end{tabular}
376	
377	  \vspace{4pt}
378	  \footnotesize
379	  Each cell: AUC $[95\%$ CI$]$. CI from 1{,}000 bootstrap resamples; $p$-values from 500-resample permutation test.
380	  ${}^{\dagger}$\,$p = 0.064$;\; ${}^{\ddagger}$\,$p = 0.232$;\; all other pairs $p < 0.01$.
381	\end{table*}
382	
383	%%% Table S9: Binary Detector Spearman ρ (exp-012)
384	\begin{table*}[t]
385	  \centering
386	  \small
387	  \caption{Spearman rank correlation ($\rho$) between binary detector confidence scores and true generational depth, and 6-class depth classification accuracy (Exp-012). Three metrics: log-PPL from the reference model (DivEye), log-PPL from the observer model, and PPL ratio (Binoculars; observer: Pythia-1.4B, performer: OLMo-1B). Random baseline for 6-class accuracy: 0.167. While statistically significant, correlations are driven by the 0v1 boundary; confidence scores do not monotonically track depth beyond generation~1. Qwen-rewrite exhibits reversed sign ($\rho > 0$), indicating that generation mode alters the direction of binary confidence's relationship with depth.}
388	  \label{tab:s9_binary_spearman}
389	  \begin{tabular}{lcccc}
390	    \toprule
391	    & \textbf{Qwen-rw} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} \\
392	    \midrule
393	    \multicolumn{5}{l}{\textit{Spearman $\rho$ with true depth}} \\
394	    \quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\
395	    \quad log-PPL (observer) & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\
396	    \quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\
397	    \midrule
398	    \multicolumn{5}{l}{\textit{Classification}} \\
399	    \quad 6-class accuracy    & 0.199    & 0.130    & 0.127    & 0.183 \\
400	    \midrule
401	    \multicolumn{5}{l}{Random baseline: 0.167 \quad $\Kempirical^{\text{binary}} = 1$ \quad $\Kempirical^{\text{OBD}} = 2$} \\
402	    \bottomrule
403	  \end{tabular}
404	\end{table*}
405	
406	%%% Table S10: Pythia Decoding Ablation (exp-020)
407	\begin{table*}[t]
408	  \centering
409	  \small
410	  \caption{Pairwise $\auc$ with bootstrap 95\% CIs across depth pairs for Pythia-1.4B under four decoding configurations (Exp-020; 10{,}000 bootstrap resamples). Complements Table~\ref{tab:s2_decoding} (Qwen-rewrite) with a second model family. $^\dagger$Greedy decoding triggers repetition collapse in Pythia-1.4B (4-gram repeat rate: $d_0{=}0.01 \to d_1{=}0.72$), inflating 0v1 and 1v2 AUC via lexical degeneracy rather than depth-discriminative features.}
411	  \label{tab:s10_pythia_decoding}
412	  \begin{tabular}{lcccc}
413	    \toprule
414	    \textbf{Depth Pair} & \textbf{Greedy}$^\dagger$ & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
415	    \midrule
416	    0 vs.\ 1 & .9992 & .9948 & .9965 & .9933 \\
417	    1 vs.\ 2 & .8838 & .6770 & .7265 & .6172 \\
418	    \cmidrule(lr){1-5}
419	    2 vs.\ 3 & .5342 & .5549 & .5941 & .5226 \\
420	    3 vs.\ 4 & .5228 & .5299 & .5698 & .5170 \\
421	    4 vs.\ 5 & .5162 & .5013 & .5284 & .5051 \\
422	    \midrule
423	    $\Kempirical$ & 2 & 2 & 2 & 2 \\
424	    \bottomrule
425	  \end{tabular}
426	\end{table*}
427	
428	%%% Table S11: Length Ablation (exp-021)
429	\begin{table*}[t]
430	  \centering
431	  \small
432	  \caption{Pairwise $\auc$ across depth pairs for three segment lengths (Exp-021; Qwen2.5-1.5B base, continuation mode). $\Kempirical{=}2$ is confirmed for 128 and 256 tokens; 512 tokens yields point estimate $\Kempirical{=}2$ but the 1v2 bootstrap CI lower bound falls marginally below $\theta$.}
433	  \label{tab:s11_length_ablation}
434	  \begin{tabular}{lccc}
435	    \toprule
436	    \textbf{Depth Pair} & \textbf{128 tokens} & \textbf{256 tokens} & \textbf{512 tokens} \\
437	    \midrule
438	    0 vs.\ 1 & .9948 & .9956 & .9961 \\
439	    1 vs.\ 2 & .6219 & .6282 & .6073$^\dagger$ \\
440	    \cmidrule(lr){1-4}
441	    2 vs.\ 3 & .5531 & .5609 & .5482 \\
442	    3 vs.\ 4 & .5218 & .5305 & .5196 \\
443	    4 vs.\ 5 & .5104 & .5142 & .5078 \\
444	    \midrule
445	    $\Kempirical$ & 2 & 2 & 2$^\dagger$ \\
446	    \bottomrule
447	    \multicolumn{4}{l}{\footnotesize $^\dagger$CI $[0.5979,\,0.6166]$; lower bound ${<}\theta{=}0.60$.}
448	  \end{tabular}
449	\end{table*}
450	
451	%%% Table S12: Domain Ablation
452	\begin{table*}[t]
453	  \centering
454	  \small
455	  \caption{Pairwise $\auc$ across depth pairs for three text domains (Qwen2.5-1.5B base, continuation mode). Tests generalization of $\Kempirical{=}2$ beyond C4 web text to structured and technical domains. Same-family scoring (Qwen-1.5B); cross-family controlled values in Table~\ref{tab:wiki_domain}.}
456	  \label{tab:s12_domain_ablation}
457	  \begin{tabular}{lccc}
458	    \toprule
459	    \textbf{Depth Pair} & \textbf{C4 (web)} & \textbf{Wikipedia} & \textbf{arXiv} \\
460	    \midrule
461	    0 vs.\ 1 & .9971 & .996 & .9984 \\
462	    1 vs.\ 2 & .6112 & .6193 & .8580 \\
463	    \cmidrule(lr){1-4}
464	    2 vs.\ 3 & .5609 & .556 & .6427 \\
465	    3 vs.\ 4 & .5409 & .528 & .5813 \\
466	    4 vs.\ 5 & .5141 & .509 & .5346 \\
467	    \midrule
468	    $\Kempirical$ & 2 & 2 & 3 \\
469	    \bottomrule
470	  \end{tabular}
471	\end{table*}
472	
473	%%% Table S13: Scorer Sensitivity Analysis
474	\begin{table*}[t]
475	  \centering
476	  \small
477	  \caption{Scorer sensitivity: $\Kempirical$ under self-scoring vs.\ cross-scoring. Self-scorer uses the generator's own model family for feature extraction; cross-scorer uses alternative models (Pythia-1.4B, OLMo-1B). $\Kempirical$ agreement across scorer conditions indicates the boundary is governed by the generation process. Cross-scoring reduces $\Kempirical$ only for the most marginal self-scorer condition (Qwen-continuation).}
478	  \label{tab:s13_scorer_sensitivity}
479	  \begin{tabular}{lccccc}
480	    \toprule
481	    & & \multicolumn{3}{c}{\textbf{Scorer}} & \\
482	    \cmidrule(lr){3-5}
483	    \textbf{Generator} & \textbf{Mode} & \textbf{Self} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Agreement} \\
484	    \midrule
485	    Qwen-1.5B-Instruct & Rewrite      & 2 (.696) & 2 & 2 & \checkmark \\
486	    Qwen-1.5B-Instruct & Continuation & 2 (.611) & 1 & 1 & $\times$ \\
487	    Qwen-1.5B (base)   & Continuation & 2 (.626) & 2 & 2 & \checkmark \\
488	    Pythia-1.4B         & Continuation & 2 (.654) & 2 & 2 & \checkmark \\
489	    OLMo-1B             & Continuation & 2 (.615) & 2 & 2 & \checkmark \\
490	    Qwen-7B             & Continuation & 2 (.618) & 2 & 2 & \checkmark \\
491	    Mistral-7B          & Continuation & 1 (.594) & 1 & 1 & \checkmark \\
492	    \bottomrule
493	  \end{tabular}
494	\end{table*}
495	
496	\clearpage
497	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a186ca4e-9f2c-4fc7-b1c4-9243c7333e61",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "978fa1fc-b74f-4244-9840-ffddd2257b1f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
      "content": "\\appendix\n\\section{Supplementary Figures}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_filtering_strategies.pdf}\n\\caption{Downstream performance of all filtering strategies (5 seeds, $\\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}\n\\label{fig:filtering_strategies}\n\\end{figure}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}\n  \\caption{Pairwise $\\auc$ decay curves for five model-mode configurations with bootstrap 95\\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\\Kempirical=2$ boundary where $\\auc$ drops below $\\theta=0.60$. This figure complements Figure~\\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}\n  \\label{fig:s1_auc_decay_ci}\n\\end{figure}\n\n\\section{Supplementary Tables}\n\n%%% Feature ranking table (moved from main text)\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Top-3 features by single-feature $\\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}\n\\label{tab:top_features}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{cllll}\n\\toprule\nRank & Pythia & OLMo & Qwen-rw & Qwen-cont \\\\\n\\midrule\n1 & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_std}} & \\texttt{freq\\_entropy} & \\textbf{\\texttt{surp\\_d1\\_std}} \\\\\n2 & \\textbf{\\texttt{surp\\_d2\\_std}} & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_std}} & \\textbf{\\texttt{surp\\_std}} \\\\\n3 & \\textbf{\\texttt{surp\\_std}} & \\textbf{\\texttt{surp\\_d2\\_std}} & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_d2\\_std}} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}\n  \\label{tab:s1_transfer}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\multirow{2}{*}{\\textbf{Train Model}} & \\multicolumn{4}{c}{\\textbf{Test Model}} \\\\\n    \\cmidrule(lr){2-5}\n    & Qwen-rw & Pythia & OLMo & Qwen-cont \\\\\n    \\midrule\n    Qwen-rw   & \\textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\\\\n    Pythia    & 0.2718 & \\textbf{0.3856} & 0.3531 & 0.3287 \\\\\n    OLMo      & 0.2768 & 0.3450 & \\textbf{0.3822} & 0.3244 \\\\\n    Qwen-cont & 0.3440 & 0.3284 & 0.3112 & \\textbf{0.3875} \\\\\n    \\bottomrule\n  \\end{tabular}\n  \\vspace{4pt}\n\n  \\footnotesize\n  \\textit{Transfer retention} between models $A$ and $B$ is defined as $\\frac{1}{2}\\bigl(\\frac{\\mathrm{acc}(A \\to B)}{\\sqrt{\\mathrm{acc}(A \\to A) \\cdot \\mathrm{acc}(B \\to B)}} + \\frac{\\mathrm{acc}(B \\to A)}{\\sqrt{\\mathrm{acc}(A \\to A) \\cdot \\mathrm{acc}(B \\to B)}}\\bigr)$.\n  Notable pairs: Pythia$\\leftrightarrow$OLMo 91--92\\%, Qwen-cont$\\leftrightarrow$Pythia 83--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\%, Qwen-rw$\\to$Pythia/OLMo 61--63\\%.\n\\end{table*}\n\n%%% Table S2: Decoding Ablation AUC (exp-003)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Pairwise AUC with bootstrap 95\\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\\,vs.\\,2 and 2\\,vs.\\,3 marks the empirical detectability boundary $\\Kempirical=2$. Bottom rows report cross-configuration Spearman $\\rho$ on per-feature discriminative-power rankings.}\n  \\label{tab:s2_decoding}\n  \\footnotesize\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Greedy} & \\textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \\textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \\textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\\\\n    \\midrule\n    0 vs.\\ 1 & $.980\\;[.977,\\,.982]$ & $.995\\;[.993,\\,.996]$ & $.988\\;[.986,\\,.990]$ & $.998\\;[.998,\\,.999]$ \\\\\n    1 vs.\\ 2 & $.689\\;[.680,\\,.698]$ & $.687\\;[.677,\\,.695]$ & $.689\\;[.680,\\,.697]$ & $.704\\;[.695,\\,.713]$ \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3 & $.561\\;[.552,\\,.571]$ & $.592\\;[.582,\\,.601]$\\rlap{$^\\dagger$} & $.590\\;[.581,\\,.600]$ & $.582\\;[.572,\\,.592]$ \\\\\n    3 vs.\\ 4 & $.540\\;[.531,\\,.550]$ & $.547\\;[.537,\\,.557]$ & $.539\\;[.529,\\,.549]$ & $.529\\;[.519,\\,.540]$ \\\\\n    4 vs.\\ 5 & $.514\\;[.503,\\,.524]$ & $.507\\;[.496,\\,.517]^{\\ddagger}$ & $.535\\;[.524,\\,.545]$ & $.524\\;[.513,\\,.535]$ \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textbf{Cross-config feature Spearman $\\rho$}} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Greedy vs.\\ Nuc $p{=}0.9$} & 0.600 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}0.7$} & 0.782 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}0.7$} & 0.914 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}1.2$} & 0.893 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}1.2$} & 0.532 &\n    \\multicolumn{1}{l}{$T{=}0.7$ vs.\\ $T{=}1.2$} & 0.668 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{${}^{\\dagger}$\\,CI upper bound (0.601) marginally exceeds $\\theta{=}0.60$ by 0.001.} \\\\\n    \\multicolumn{5}{l}{${}^{\\ddagger}$\\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S2b: Extended K* CI (all models including new additions)\n\\begin{table*}[t]\n  \\centering\n  \\footnotesize\n  \\caption{Extended pairwise $\\auc$ with bootstrap 95\\% CIs for all 9 model configurations.\n  This table extends Table~\\ref{tab:kstar_ci} in the main text with Qwen-base, Qwen-14B, LLaMA-8B, and Mistral-7B.\n  8/9 yield $\\Kempirical = 2$; Mistral-7B yields $\\Kempirical = 1$ (1v2 $\\auc < \\theta$).}\n  \\label{tab:kstar_ci_extended}\n  \\resizebox{\\textwidth}{!}{%\n  \\begin{tabular}{lcccccccccccccccccc}\n    \\toprule\n     & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} & \\multicolumn{2}{c}{Qwen-14B\\rlap{$^\\ddagger$}} & \\multicolumn{2}{c}{Qwen-base} & \\multicolumn{2}{c}{LLaMA-8B} & \\multicolumn{2}{c}{Mistral-7B} \\\\\n    \\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\\cmidrule(lr){12-13}\\cmidrule(lr){14-15}\\cmidrule(lr){16-17}\\cmidrule(lr){18-19}\n     & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n    \\midrule\n    0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\\,.967] & .960 & [.956,\\,.963] & .987 & [.985,\\,.989] & .9225 & [.918,\\,.927] & .930 & [.925,\\,.935] \\\\\n    1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6539 & [.645,\\,.663]\\rlap{$^*$} & .6145 & [.605,\\,.625]\\rlap{$^*$} & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} & .621 & [.612,\\,.630]\\rlap{$^*$} & .626 & [.617,\\,.635]\\rlap{$^*$} & .6123 & [.603,\\,.622]\\rlap{$^*$} & .594 & [.584,\\,.603] \\\\\n    2v3 & .5893 & [.580,\\,.599] & .5514 & [.542,\\,.563] & .5496 & [.540,\\,.560] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] & .549 & [.539,\\,.559] & .550 & [.540,\\,.560] & .5518 & [.542,\\,.562] & .548 & [.538,\\,.558] \\\\\n    3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & & .524 & [.514,\\,.535] & .529 & [.519,\\,.540] & .5203 & [.510,\\,.531] & .521 & \\\\\n    4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & & .515 & [.505,\\,.527] & .518 & [.508,\\,.529] & .5089 & [.499,\\,.519] & .510 & \\\\\n    \\bottomrule\n    \\multicolumn{19}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all boundary comparisons. Mistral-7B 1v2: $p = 0.001$ but $\\auc < \\theta$, hence $\\Kempirical{=}1$.} \\\\\n    \\multicolumn{19}{l}{\\footnotesize $^\\ddagger$Qwen-7B: Qwen2.5-7B (fp16); Qwen-14B: Qwen2.5-14B; scorer: Qwen2.5-1.5B.}\n  \\end{tabular}}\n\n\\end{table*}\n\n%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)\n\\begin{table*}[t]\n  \\centering\n  \\caption{LLM zero-shot depth classification: $5{\\times}5$ confusion matrices\n    (Exp-011). Both frontier LLMs achieve high binary detection accuracy\n    (GPT-5.5: 0.8780; Claude Opus~4.6: 0.8818) but near-chance 5-class\n    accuracy (${\\sim}0.33$ vs.\\ OBD-LightGBM baseline 0.386, evaluated on the full test set $N{=}5{,}000$). GPT-5.5\n    strongly identifies depth-0 text (recall${=}0.7700$) but collapses on\n    depth-4 (recall${=}0.0800$), misclassifying 50/100 depth-4 samples as\n    depth-2. Claude Opus~4.6 shows more uniform errors across depths 1--4,\n    with depth-4 recall (0.3700) substantially exceeding GPT-5.5.\n    Per-depth recall comparison with OBD-LightGBM in Table~\\ref{tab:s3c_perdepth}.}\n  \\label{tab:s3_llm_zeroshot}\n\n  \\vspace{0.5em}\n  \\begin{subtable}{0.48\\textwidth}\n    \\centering\n    \\caption{GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)}\n    \\label{tab:s3a_gpt55}\n    \\small\n    \\begin{tabular}{lcccccc}\n      \\toprule\n      & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n      \\cmidrule(lr){2-6}\n      True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n      \\midrule\n      0 & \\textbf{77} & 18 &  4 &  0 &  1 & .770 \\\\\n      1 &  9 & \\textbf{19} & 36 & 24 & 12 & .190 \\\\\n      2 &  8 & 10 & \\textbf{38} & 35 &  9 & .380 \\\\\n      3 & 10 & 16 & 35 & \\textbf{24} & 15 & .240 \\\\\n      4 & 11 & 13 & 50 & 18 &  \\textbf{8} & .080 \\\\\n      \\bottomrule\n    \\end{tabular}\n  \\end{subtable}\n  \\hfill\n  \\begin{subtable}{0.48\\textwidth}\n    \\centering\n    \\caption{Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)}\n    \\label{tab:s3b_claude}\n    \\small\n    \\begin{tabular}{lcccccc}\n      \\toprule\n      & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n      \\cmidrule(lr){2-6}\n      True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n      \\midrule\n      0 & \\textbf{69} & 26 &  3 &  0 &  2 & .690 \\\\\n      1 &  8 & \\textbf{21} & 32 & 11 & 28 & .210 \\\\\n      2 &  6 & 36 & \\textbf{28} &  5 & 25 & .280 \\\\\n      3 &  7 & 20 & 31 & \\textbf{10} & 31 & .100 \\\\\n      4 &  7 & 28 & 22 &  6 & \\textbf{37} & .370 \\\\\n      \\bottomrule\n    \\end{tabular}\n  \\end{subtable}\n\\end{table*}\n\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Per-depth recall (\\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\\geq 2$, consistent with $\\Kempirical = 2$.}\n  \\label{tab:s3c_perdepth}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lccccc}\n    \\toprule\n    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\\\\n    \\midrule\n    OBD-LightGBM & \\textbf{96} & \\textbf{39} & 14 & 19 & 22 \\\\\n    GPT-5.5      & 77 & 19 & \\textbf{38} & \\textbf{24} &  8 \\\\\n    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \\textbf{37} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table: Token Length and EOS Truncation Analysis\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Mean subword token count per depth and EOS truncation rate (\\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend within any model; the 0v1 length asymmetry (human texts shorter) makes detection \\emph{more conservative}, not inflated. See Section~\\ref{sec:length_confound} for discussion.}\n  \\label{tab:token_length}\n  \\begin{tabular}{lcccccccc}\n    \\toprule\n    & \\multicolumn{6}{c}{\\textbf{Mean Token Count}} & & \\\\\n    \\cmidrule(lr){2-7}\n    \\textbf{Model} & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 & Depth 5 & \\textbf{EOS Trunc.\\ (\\%)} & \\textbf{Severity} \\\\\n    \\midrule\n    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\\\\n    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\\\\n    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negligible \\\\\n    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Moderate \\\\\n    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\\\\n    \\midrule\n    \\multicolumn{9}{l}{\\textit{Decoding ablation (Qwen-rw 1.5B)}} \\\\\n    \\quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\\\\n    \\quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\\\\n    \\quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\\\\n    \\quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\\\\n    \\bottomrule\n  \\end{tabular}\n\n  \\vspace{4pt}\n  \\footnotesize\n  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.\n\\end{table*}\n\n%%% Table S4: Dataset Statistics\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}\n  \\label{tab:s4_dataset_stats}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{clrl}\n    \\toprule\n    \\textbf{Depth} & \\textbf{$N$ samples} & \\textbf{Mean tokens} & \\textbf{Source} \\\\\n    \\midrule\n    0 & 5{,}000 & 147.8 & C4 validation (human) \\\\\n    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\\\\n    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\\\\n    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\\\\n    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Total} & \\multicolumn{2}{l}{30{,}000 samples} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S5: Complete 15-D Feature Descriptions\n\\begin{table*}[t]\n  \\centering\n  \\caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}\n  \\label{tab:s5_features}\n  \\begin{tabular}{llp{0.45\\textwidth}l}\n    \\toprule\n    \\textbf{Group} & \\textbf{Feature} & \\textbf{Description} & \\textbf{Range} \\\\\n    \\midrule\n    \\multirow{9}{*}{\\rotatebox[origin=c]{90}{\\textsc{Surprisal}}}\n    & \\texttt{surp\\_mean}   & Mean token surprisal $\\frac{1}{T}\\sum_t -\\log p(x_t \\mid x_{&lt;t})$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_std}    & Standard deviation of token surprisal & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_skew}   & Skewness of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_kurt}   & Excess kurtosis of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_mean} & Mean of first-order surprisal differences $\\Delta s_t = s_{t+1} - s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_std}  & Std of first-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_d1\\_skew} & Skewness of first-order surprisal differences & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_mean} & Mean of second-order differences $\\Delta^2 s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_std}  & Std of second-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Lex}}}\n    & \\texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\\\\n    & \\texttt{hapax\\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\\\\n    & \\texttt{self\\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Freq}}}\n    & \\texttt{freq\\_kurtosis}  & Excess kurtosis of word frequency distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{freq\\_entropy}   & Shannon entropy of word frequencies: $-\\sum p_w \\log_2 p_w$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{low\\_freq\\_ratio} & Proportion of vocabulary with count $\\leq 2$ & $[0, 1]$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap\n\\begin{table*}[t]\n\\begin{minipage}[t]{0.45\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \\texttt{doc\\_id} to prevent data leakage from the same seed document appearing in both train and test.}\n  \\label{tab:s6_lgbm_params}\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Parameter} & \\textbf{Value} \\\\\n    \\midrule\n    \\texttt{n\\_estimators}      & 200 \\\\\n    \\texttt{learning\\_rate}     & 0.05 \\\\\n    \\texttt{max\\_depth}         & 6 \\\\\n    \\texttt{num\\_leaves}        & 31 \\\\\n    \\texttt{verbose}            & $-1$ \\\\\n    \\texttt{n\\_jobs}            & $-1$ (all cores) \\\\\n    Cross-validation            & 5-fold GroupKFold \\\\\n    Grouping key                & \\texttt{doc\\_id} \\\\\n    Objective                   & Binary (per depth pair) \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{minipage}\\hfill\n\\begin{minipage}[t]{0.52\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}\n  \\label{tab:s7_neural_probe}\n  \\resizebox{\\textwidth}{!}{%\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Component} & \\textbf{Details} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Embedding extraction}} \\\\\n    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\\\\n    Representation    & Last hidden state, attention-masked avg pool \\\\\n    Embedding dim     & 1536 / 2048 / 2048 \\\\\n    Max sequence len   & 512 tokens \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{MLP classifier}} \\\\\n    Architecture      & $d_{\\text{emb}} \\to 512 \\to 256 \\to 6$ \\\\\n    Activations       & ReLU \\\\\n    Dropout           & 0.1 (after each hidden layer) \\\\\n    Output            & 6-class softmax \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Training}} \\\\\n    Optimizer         & Adam ($\\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\\\\n    Loss              & Cross-entropy \\\\\n    Batch size        & 256 \\\\\n    Max epochs        & 20 \\\\\n    Early stopping    & Patience = 5 (validation loss) \\\\\n    Cross-validation  & 5-fold GroupKFold \\\\\n    \\bottomrule\n  \\end{tabular}%\n  }\n\\end{minipage}\n\\end{table*}\n\n%%% Table S8: Per-Model Bootstrap CI Results (exp-007)\n\\begin{table*}[t]\n  \\centering\n  \\footnotesize\n  \\caption{Pairwise AUC with bootstrap 95\\% confidence intervals for four model-mode configurations (Exp-007, 1{,}000 bootstrap resamples). The horizontal rule separates depth pairs above and below the detectability threshold $\\theta = 0.60$. Permutation $p$-values test $H_0\\colon \\auc = 0.50$. All pairs are significant at $p < 0.01$ except OLMo 3\\,vs.\\,4 ($p = 0.064$) and 4\\,vs.\\,5 ($p = 0.232$), consistent with convergence to chance at deeper generations.}\n  \\label{tab:s8_cv_folds}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Qwen-rewrite} & \\textbf{Pythia-1.4B} & \\textbf{OLMo-1B} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    0 vs.\\ 1\n      & $.996\\;[.995,\\,.997]$\n      & $.993\\;[.992,\\,.994]$\n      & $.997\\;[.996,\\,.998]$\n      & $.997\\;[.996,\\,.998]$ \\\\\n    1 vs.\\ 2\n      & $.696\\;[.686,\\,.704]$\n      & $.654\\;[.645,\\,.663]$\n      & $.615\\;[.605,\\,.625]$\n      & $.611\\;[.602,\\,.621]$ \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3\n      & $.589\\;[.580,\\,.599]$\n      & $.551\\;[.542,\\,.563]$\n      & $.550\\;[.540,\\,.560]$\n      & $.561\\;[.551,\\,.571]$ \\\\\n    3 vs.\\ 4\n      & $.544\\;[.533,\\,.555]$\n      & $.515\\;[.504,\\,.526]$\n      & $.509\\;[.497,\\,.520]^{\\dagger}$\n      & $.541\\;[.531,\\,.551]$ \\\\\n    4 vs.\\ 5\n      & $.534\\;[.524,\\,.545]$\n      & $.514\\;[.502,\\,.525]$\n      & $.505\\;[.493,\\,.515]^{\\ddagger}$\n      & $.514\\;[.504,\\,.526]$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\n  \\vspace{4pt}\n  \\footnotesize\n  Each cell: AUC $[95\\%$ CI$]$. CI from 1{,}000 bootstrap resamples; $p$-values from 500-resample permutation test.\n  ${}^{\\dagger}$\\,$p = 0.064$;\\; ${}^{\\ddagger}$\\,$p = 0.232$;\\; all other pairs $p < 0.01$.\n\\end{table*}\n\n%%% Table S9: Binary Detector Spearman ρ (exp-012)\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Spearman rank correlation ($\\rho$) between binary detector confidence scores and true generational depth, and 6-class depth classification accuracy (Exp-012). Three metrics: log-PPL from the reference model (DivEye), log-PPL from the observer model, and PPL ratio (Binoculars; observer: Pythia-1.4B, performer: OLMo-1B). Random baseline for 6-class accuracy: 0.167. While statistically significant, correlations are driven by the 0v1 boundary; confidence scores do not monotonically track depth beyond generation~1. Qwen-rewrite exhibits reversed sign ($\\rho > 0$), indicating that generation mode alters the direction of binary confidence's relationship with depth.}\n  \\label{tab:s9_binary_spearman}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Qwen-rw} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textit{Spearman $\\rho$ with true depth}} \\\\\n    \\quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\\\\n    \\quad log-PPL (observer) & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\\\\n    \\quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textit{Classification}} \\\\\n    \\quad 6-class accuracy    & 0.199    & 0.130    & 0.127    & 0.183 \\\\\n    \\midrule\n    \\multicolumn{5}{l}{Random baseline: 0.167 \\quad $\\Kempirical^{\\text{binary}} = 1$ \\quad $\\Kempirical^{\\text{OBD}} = 2$} \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S10: Pythia Decoding Ablation (exp-020)\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Pairwise $\\auc$ with bootstrap 95\\% CIs across depth pairs for Pythia-1.4B under four decoding configurations (Exp-020; 10{,}000 bootstrap resamples). Complements Table~\\ref{tab:s2_decoding} (Qwen-rewrite) with a second model family. $^\\dagger$Greedy decoding triggers repetition collapse in Pythia-1.4B (4-gram repeat rate: $d_0{=}0.01 \\to d_1{=}0.72$), inflating 0v1 and 1v2 AUC via lexical degeneracy rather than depth-discriminative features.}\n  \\label{tab:s10_pythia_decoding}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Greedy}$^\\dagger$ & \\textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \\textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \\textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\\\\n    \\midrule\n    0 vs.\\ 1 & .9992 & .9948 & .9965 & .9933 \\\\\n    1 vs.\\ 2 & .8838 & .6770 & .7265 & .6172 \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3 & .5342 & .5549 & .5941 & .5226 \\\\\n    3 vs.\\ 4 & .5228 & .5299 & .5698 & .5170 \\\\\n    4 vs.\\ 5 & .5162 & .5013 & .5284 & .5051 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 2 & 2 \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S11: Length Ablation (exp-021)\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Pairwise $\\auc$ across depth pairs for three segment lengths (Exp-021; Qwen2.5-1.5B base, continuation mode). $\\Kempirical{=}2$ is confirmed for 128 and 256 tokens; 512 tokens yields point estimate $\\Kempirical{=}2$ but the 1v2 bootstrap CI lower bound falls marginally below $\\theta$.}\n  \\label{tab:s11_length_ablation}\n  \\begin{tabular}{lccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{128 tokens} & \\textbf{256 tokens} & \\textbf{512 tokens} \\\\\n    \\midrule\n    0 vs.\\ 1 & .9948 & .9956 & .9961 \\\\\n    1 vs.\\ 2 & .6219 & .6282 & .6073$^\\dagger$ \\\\\n    \\cmidrule(lr){1-4}\n    2 vs.\\ 3 & .5531 & .5609 & .5482 \\\\\n    3 vs.\\ 4 & .5218 & .5305 & .5196 \\\\\n    4 vs.\\ 5 & .5104 & .5142 & .5078 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 2$^\\dagger$ \\\\\n    \\bottomrule\n    \\multicolumn{4}{l}{\\footnotesize $^\\dagger$CI $[0.5979,\\,0.6166]$; lower bound ${<}\\theta{=}0.60$.}\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S12: Domain Ablation\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Pairwise $\\auc$ across depth pairs for three text domains (Qwen2.5-1.5B base, continuation mode). Tests generalization of $\\Kempirical{=}2$ beyond C4 web text to structured and technical domains. Same-family scoring (Qwen-1.5B); cross-family controlled values in Table~\\ref{tab:wiki_domain}.}\n  \\label{tab:s12_domain_ablation}\n  \\begin{tabular}{lccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{C4 (web)} & \\textbf{Wikipedia} & \\textbf{arXiv} \\\\\n    \\midrule\n    0 vs.\\ 1 & .9971 & .996 & .9984 \\\\\n    1 vs.\\ 2 & .6112 & .6193 & .8580 \\\\\n    \\cmidrule(lr){1-4}\n    2 vs.\\ 3 & .5609 & .556 & .6427 \\\\\n    3 vs.\\ 4 & .5409 & .528 & .5813 \\\\\n    4 vs.\\ 5 & .5141 & .509 & .5346 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 3 \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S13: Scorer Sensitivity Analysis\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Scorer sensitivity: $\\Kempirical$ under self-scoring vs.\\ cross-scoring. Self-scorer uses the generator's own model family for feature extraction; cross-scorer uses alternative models (Pythia-1.4B, OLMo-1B). $\\Kempirical$ agreement across scorer conditions indicates the boundary is governed by the generation process. Cross-scoring reduces $\\Kempirical$ only for the most marginal self-scorer condition (Qwen-continuation).}\n  \\label{tab:s13_scorer_sensitivity}\n  \\begin{tabular}{lccccc}\n    \\toprule\n    & & \\multicolumn{3}{c}{\\textbf{Scorer}} & \\\\\n    \\cmidrule(lr){3-5}\n    \\textbf{Generator} & \\textbf{Mode} & \\textbf{Self} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Agreement} \\\\\n    \\midrule\n    Qwen-1.5B-Instruct & Rewrite      & 2 (.696) & 2 & 2 & \\checkmark \\\\\n    Qwen-1.5B-Instruct & Continuation & 2 (.611) & 1 & 1 & $\\times$ \\\\\n    Qwen-1.5B (base)   & Continuation & 2 (.626) & 2 & 2 & \\checkmark \\\\\n    Pythia-1.4B         & Continuation & 2 (.654) & 2 & 2 & \\checkmark \\\\\n    OLMo-1B             & Continuation & 2 (.615) & 2 & 2 & \\checkmark \\\\\n    Qwen-7B             & Continuation & 2 (.618) & 2 & 2 & \\checkmark \\\\\n    Mistral-7B          & Continuation & 1 (.594) & 1 & 1 & \\checkmark \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n\\clearpage\n",
      "numLines": 497,
      "startLine": 1,
      "totalLines": 497
    }
  },
  "sourceToolAssistantUUID": "a186ca4e-9f2c-4fc7-b1c4-9243c7333e61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 49 · 2026-05-18T09:57:37.735Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VwbQD4FqgsFjQJDpDh9gQg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "978fa1fc-b74f-4244-9840-ffddd2257b1f",
  "isSidechain": false,
  "requestId": "req_011Cb9qSLs9frHhrSZSGCbqi",
  "type": "assistant",
  "uuid": "0c5c14a3-23b5-45cf-9139-de4e4327c476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VfxG7JyWRitavZy524FYK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 13741,
      "cache_creation_input_tokens": 1397,
      "cache_read_input_tokens": 42870,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1397,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 13741,
          "output_tokens": 293,
          "cache_read_input_tokens": 42870,
          "cache_creation_input_tokens": 1397,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1397
          },
          "type": "message"
        }
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

_source line 50 · 2026-05-18T09:57:37.742Z_

<details><summary>↩ Tool result · `toolu_01VwbQD4FqgsFjQJDpDh9gQg`</summary>

```text
1	\section{Extended Analysis and Limitations}
2	\label{sec:extended_discussion}
3	
4	This section provides supporting tables for cross-scorer validation (Tables~\ref{tab:crossscorer}--\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.
5	
6	\noindent\begin{minipage}{\columnwidth}
7	\centering
8	\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
9	\label{tab:crossscorer}
10	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
11	\end{minipage}
12	
13	\begin{table}[h]
14	\centering
15	\small
16	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\times$ 5 folds $\times$ 5 depth-pairs; 3 generators $\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\eta^2_p = 0.19$) relative to Depth-Pair ($\eta^2_p = 1.00$) and Generator ($\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination. While $\eta^2_p = 0.19$ exceeds Cohen's (1988) threshold for a large effect, the Scorer contribution is approximately 5$\times$ smaller than Generator ($\eta^2_p = 0.89$) and dwarfed by Depth-Pair ($\eta^2_p = 1.00$), supporting its characterization as practically minor in this context.}
17	\label{tab:anova_crossscorer}
18	\begin{tabular}{lrrrr}
19	\toprule
20	\textbf{Source} & \textbf{df} & $F$ & $p$ & $\eta^2_p$ \\
21	\midrule
22	Generator     & 2  & 926.8  & ${<}.001$  & .885 \\
23	Scorer        & 3  & 19.02  & ${<}.001$  & .192 \\
24	Depth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\
25	Gen$\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\
26	Gen$\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\
27	Scorer$\times$Depth & 12 & 2.45 & .005 & .109 \\
28	Residual      & 240 & & & \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
33	\subsection{Extended Limitations}
34	\label{sec:extended_limitations}
35	
36	\emph{Prompt-chain versus retrain-chain.}
37	Retrain-chain validation (Pythia-1.4B LoRA, 5 generations) yields $\Kempirical{\geq}4$ (Table~\ref{tab:retrain_ci}), far exceeding prompt-chain $\Kempirical{=}2$.
38	All pairwise CIs have lower bounds well above $\theta{=}0.60$ ($p < 0.001$), statistically confirming $\Kempirical{\geq}4$.
39	The elevated signal arises from cumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) rather than text-intrinsic degradation; prompt-chain $\Kempirical$ is the operationally relevant boundary for data curation.
40	
41	\begin{table}[h]
42	\centering
43	\small
44	\caption{Retrain-chain pairwise $\auc$ with bootstrap 95\% CIs (Pythia-1.4B LoRA, 5 generations). All CI lower bounds $\gg \theta{=}0.60$.}
45	\label{tab:retrain_ci}
46	\begin{tabular}{lccc}
47	\toprule
48	\textbf{Pair} & $\auc$ & \textbf{95\% CI} & $p$ \\
49	\midrule
50	0v1 & 0.9842 & $[0.9823,\,0.9860]$ & ${<}0.001$ \\
51	1v2 & 0.9471 & $[0.9432,\,0.9509]$ & ${<}0.001$ \\
52	2v3 & 0.8888 & $[0.8832,\,0.8943]$ & ${<}0.001$ \\
53	3v4 & 0.7994 & $[0.7920,\,0.8067]$ & ${<}0.001$ \\
54	\bottomrule
55	\end{tabular}
56	\end{table}
57	
58	\emph{Threshold sensitivity.}
59	Table~\ref{tab:theta_sensitivity} reports $\Kempirical$ across $\theta \in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.
60	Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
61	
62	\begin{table}[h]
63	\centering
64	\small
65	\caption{$\Kempirical$ as a function of $\theta$ across conditions. The \textbf{domain ordering} (arXiv $>$ web $\geq$ cross-scorer) and \textbf{bounded range} ($\Kempirical{\leq}4$) are preserved across $\theta \in [0.55, 0.70]$. The headline result (web $\Kempirical{=}2$, arXiv $\Kempirical{=}3$) holds for $\theta \in [0.575, 0.625]$.}
66	\label{tab:theta_sensitivity}
67	\resizebox{\columnwidth}{!}{%
68	\begin{tabular}{llcccc}
69	\toprule
70	\textbf{Condition} & \textbf{Config} & $\theta{=}0.55$ & $\theta{=}0.60$ & $\theta{=}0.625$ & $\theta{=}0.70$ \\
71	\midrule
72	C4 (web) & Qwen-rw      & 3 & 2 & 2 & 1 \\
73	C4 (web) & Pythia       & 2 & 2 & 2 & 1 \\
74	C4 (web) & OLMo         & 2 & 2 & 1 & 1 \\
75	C4 (web) & Qwen-cont    & 3 & 2 & 2 & 1 \\
76	C4 (web) & Qwen-7B      & 2 & 2 & 2 & 1 \\
77	C4 (web) & Mistral-7B   & 1 & 1 & 1 & 1 \\
78	\midrule
79	arXiv    & Qwen-1.5B-base (cont.) & 4 & 3 & 3 & 2 \\
80	arXiv    & Pythia-1.4B (cont.)    & 4 & 3 & 3 & 2 \\
81	\midrule
82	Cross-scorer & Qwen-cont/Pythia-scored & 2 & 1 & 1 & 1 \\
83	Cross-scorer & Qwen-cont/OLMo-scored   & 2 & 1 & 1 & 1 \\
84	\bottomrule
85	\end{tabular}}
86	\end{table}
87	
88	\emph{Structural confound: token length.}
89	In continuation mode the generation prompt is discarded, so all depths $\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\ machine-generated prompt), not structural composition.
90	Depth~0 texts average ${\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\ref{tab:token_length}).
91	This asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.
92	Within depths 1--5, mean token counts are stable (within-model range $\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\Kempirical{=}2$ are unaffected by length.
93	EOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\%, Pythia 34--36\%, OLMo $<$1\%, Qwen-continuation 17--20\%, Qwen-7B 45--47\%.
94	Models with the highest truncation (Pythia, Qwen-7B) still yield $\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.
95	
96	\emph{Graduated filtering.}
97	All $\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\alpha{=}0.1$: 0.5873; $\alpha{=}0.9$: 0.5892 vs.\ 0.5941); at $\alpha{=}0.9$, HellaSwag matches exactly (0.6701).
98	Binary-ours significantly outperforms all alternatives on MMLU ($p_{\text{corr}} \leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\text{corr}} = 0.011$).
99	\label{tab:pairwise_significance}
100	
101	\subsection{Dose-Response: Contamination Ratio Effect}
102	\label{sec:dose_response}
103	
104	The main filtering experiments (Section~\ref{sec:filtering}) use 100\% synthetic data to maximize effect size.
105	To characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\%, 30\%, and 50\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\ref{tab:dose_response}).
106	
107	\begin{table}[h]
108	\centering
109	\small
110	\caption{MMLU and HellaSwag by contamination ratio and filtering strategy (5 seeds, mean $\pm$ std). Base model MMLU: 0.6018. Binary filtering retains a significant advantage on HellaSwag across all ratios ($p \leq 0.004$, Holm-Bonferroni corrected).}
111	\label{tab:dose_response}
112	\resizebox{\columnwidth}{!}{%
113	\begin{tabular}{lcccccc}
114	\toprule
115	& \multicolumn{2}{c}{\textbf{10\%}} & \multicolumn{2}{c}{\textbf{30\%}} & \multicolumn{2}{c}{\textbf{50\%}} \\
116	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}
117	\textbf{Strategy} & MMLU & HellaSwag & MMLU & HellaSwag & MMLU & HellaSwag \\
118	\midrule
119	No-filter   & $.6058{\pm}.0002$ & $.6689{\pm}.0006$ & $.6069{\pm}.0007$ & $.6664{\pm}.0018$ & $.6063{\pm}.0012$ & $.6680{\pm}.0005$ \\
120	Binary-ours & $\mathbf{.6079{\pm}.0004}$ & $\mathbf{.6727{\pm}.0007}$ & $\mathbf{.6082{\pm}.0011}$ & $\mathbf{.6725{\pm}.0006}$ & $\mathbf{.6088{\pm}.0009}$ & $\mathbf{.6731{\pm}.0004}$ \\
121	Graduated   & $.6066{\pm}.0010$ & $.6700{\pm}.0014$ & $.6072{\pm}.0008$ & $.6665{\pm}.0012$ & $.6062{\pm}.0008$ & $.6679{\pm}.0001$ \\
122	\bottomrule
123	\end{tabular}}
124	\end{table}
125	
126	At all tested ratios (10--50\%), no-filter MMLU remains above the base model (0.6018), indicating that synthetic data at these proportions is net-beneficial rather than harmful.
127	Binary filtering consistently improves over no-filter, with HellaSwag differences significant across all ratios ($p \leq 0.004$, Holm-Bonferroni corrected).
128	MMLU differences are smaller and significant only at 10\% after correction ($p = 0.001$).
129	Graduated weighting is indistinguishable from no-filter at all ratios (MMLU $p \geq 0.27$; HellaSwag $p \geq 0.06$), confirming that depth assignments beyond $\Kempirical$ inject noise regardless of contamination severity.
130	Effect sizes diminish 3--6$\times$ relative to the 100\% setting (Section~\ref{sec:filtering}), but the strategy ordering (binary $>$ graduated $\approx$ no-filter) is preserved.
131	
132	\subsection{Cross-Model Filtering Replication}
133	\label{sec:pythia_filtering}
134	
135	To test whether $\Kempirical{=}2$ correctly predicts optimal curation granularity across architectures, we replicate the filtering experiment on Pythia-1.4B (LoRA rank 8, nucleus $p{=}0.9$, $T{=}1.0$, 3 seeds; Table~\ref{tab:pythia_filtering}).
136	
137	\begin{table}[h]
138	\centering
139	\small
140	\caption{Pythia-1.4B filtering replication (3 seeds, mean $\pm$ std). Strategy ordering matches Qwen (binary $>$ no-filter $>$ graduated on MMLU).}
141	\label{tab:pythia_filtering}
142	\begin{tabular}{lcc}
143	\toprule
144	\textbf{Strategy} & \textbf{MMLU} & \textbf{HellaSwag} \\
145	\midrule
146	No-filter & $.2568{\pm}.0012$ & $.5250{\pm}.0008$ \\
147	Binary-ours & $\mathbf{.2585{\pm}.0004}$ & $.5251{\pm}.0001$ \\
148	Graduated$_{0.9}$ & $.2561{\pm}.0009$ & $\mathbf{.5253{\pm}.0007}$ \\
149	\bottomrule
150	\end{tabular}
151	\end{table}
152	
153	The strategy ordering (binary $>$ no-filter $>$ graduated on MMLU) matches Qwen (Section~\ref{sec:filtering}).
154	The small absolute differences reflect the model's near-chance MMLU baseline rather than filtering inefficacy; the consistent ordering across two architectures supports $\Kempirical{=}2$'s predictive value for curation granularity.
155	HellaSwag differences are negligible across all strategies.
156	
157	\subsection{Feature Subset Stability}
158	\label{sec:feature_subset}
159	
160	To test whether $\Kempirical{=}2$ depends on the specific 15D feature combination, we evaluate random feature subsets of varying size on Pythia-1.4B prompt-chain data (Table~\ref{tab:feature_subset}).
161	
162	\begin{table}[h]
163	\centering
164	\small
165	\caption{1v2 $\auc$ by feature subset size (Pythia-1.4B). $\Kempirical{=}2$ ($\auc > \theta{=}0.60$) is robust at $\geq$8 features.}
166	\label{tab:feature_subset}
167	\begin{tabular}{lcccc}
168	\toprule
169	\textbf{Subset} & \textbf{Tested} & \textbf{Pass} & \textbf{Min $\auc$} & \textbf{Mean $\auc$} \\
170	\midrule
171	15D (full) & 1 & 1 & 0.6262 & 0.6262 \\
172	10D        & 5 & 5 & 0.6153 & 0.6191 \\
173	8D         & 5 & 5 & 0.6056 & 0.6159 \\
174	5D         & 5 & 2 & 0.5856 & 0.5998 \\
175	3D (top-3) & 1 & 0 & 0.5871 & 0.5871 \\
176	\bottomrule
177	\end{tabular}
178	\end{table}
179	
180	$\Kempirical{=}2$ holds for all subsets of size $\geq$8 (10/10 pass, min $\auc = 0.6056$), becomes fragile at 5D (2/5 pass), and fails at 3D (top-3 surprisal features alone: $\auc = 0.5871 < \theta$).
181	The boundary does not depend on any specific feature combination but requires sufficient dimensionality ($\geq$8) to capture the multi-faceted distributional shift between generations 1 and 2.
182	
183	\subsection{self\_BLEU Feature Independence}
184	\label{sec:selfbleu_ablation}
185	
186	To verify that $\Kempirical$ does not depend on the self\_BLEU feature (which may reflect stylistic repetition rather than depth-correlated degradation), we compare 15D and 14D (self\_BLEU removed) classifiers across four model configurations (Table~\ref{tab:selfbleu_ablation}).
187	
188	\begin{table}[h]
189	\centering
190	\small
191	\caption{15D vs.\ 14D (self\_BLEU removed) 1v2 $\auc$ with bootstrap 95\% CIs. Removing self\_BLEU does not change $\Kempirical$ for any configuration. Maximum $|\Delta\auc| = 0.0031$, within bootstrap CI width (${\sim}0.018$).}
192	\label{tab:selfbleu_ablation}
193	\resizebox{\columnwidth}{!}{%
194	\begin{tabular}{lcccc}
195	\toprule
196	\textbf{Model} & $\Kempirical$ & \textbf{15D $\auc$ [CI]} & \textbf{14D $\auc$ [CI]} & $\Delta$ \\
197	\midrule
198	Qwen-base   & 2/2 & $.6288$ $[.620,\,.638]$ & $.6258$ $[.616,\,.635]$ & $-.0031$ \\
199	Pythia-1.4B  & 2/2 & $.8840$ $[.878,\,.890]$ & $.8830$ $[.876,\,.889]$ & $-.0010$ \\
200	LLaMA-8B     & 2/2 & $.6075$ $[.598,\,.617]$ & $.6074$ $[.598,\,.617]$ & $-.0001$ \\
201	Mistral-7B   & 1/1 & $.5902$ $[.580,\,.600]$ & $.5903$ $[.580,\,.600]$ & $+.0002$ \\
202	\bottomrule
203	\end{tabular}}
204	\end{table}
205	
206	All four configurations preserve their $\Kempirical$ under 14D, with negligible AUC change ($|\Delta| \leq 0.003$).
207	The self\_BLEU feature contributes minimally to the depth boundary; $\Kempirical{=}2$ is driven by surprisal and entropy features rather than lexical repetition statistics.
208	
209	\subsection{Wikipedia Domain: Scorer Confound Resolution}
210	\label{sec:wiki_domain}
211	
212	Under same-family scoring (Qwen-1.5B scorer), Wikipedia $\Kempirical$ appeared to exhibit model-family dependence: Qwen generators (1.5B and 7B) yielded $\Kempirical{=}2$, while all four non-Qwen models yielded $\Kempirical{=}1$ (Table~\ref{tab:wiki_domain}).
213	A scorer confound ablation resolves this apparent split.
214	Rescoring the same Qwen-7B Wikipedia text with Pythia-1.4B reduces 1v2 $\auc$ from $0.611$ to $0.587$ ($\Delta = -2.4$\,pp), dropping $\Kempirical$ from 2 to 1.
215	With the scorer confound controlled, all six models yield $\Kempirical{=}1$ on Wikipedia, and the domain ordering simplifies to: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$).
216	
217	\begin{table}[h]
218	\centering
219	\small
220	\caption{Wikipedia pairwise $\auc$ across 6 models. $^\dagger$Qwen rows use same-family scorer (Qwen-1.5B); cross-family scoring (Pythia-1.4B) reduces Qwen-7B to $\Kempirical{=}1$ ($\Delta = -2.4$\,pp), resolving the apparent family split.}
221	\label{tab:wiki_domain}
222	\resizebox{\columnwidth}{!}{%
223	\begin{tabular}{llccccc}
224	\toprule
225	\textbf{Model} & \textbf{Family} & \textbf{0v1} & \textbf{1v2} & \textbf{2v3} & $\Kempirical$ & \textbf{Scorer} \\
226	\midrule
227	Qwen-1.5B (base) & Qwen & ---  & .619 & .550 & 2$^\dagger$ & Qwen-1.5B \\
228	Qwen-1.5B (base) & Qwen & ---  & .599 & ---  & 1 & Pythia-1.4B \\
229	Qwen-7B          & Qwen & .967 & .611 & .556 & 2$^\dagger$ & Qwen-1.5B \\
230	Qwen-7B          & Qwen & ---  & .587 & ---  & 1 & Pythia-1.4B \\
231	\midrule
232	Pythia-1.4B   & non-Qwen & .975 & .585 & .545 & 1 & Qwen-1.5B \\
233	OLMo-1B       & non-Qwen & .993 & .499 & .501 & 1 & Qwen-1.5B \\
234	LLaMA-3.1-8B  & non-Qwen & .932 & .595 & .539 & 1 & Qwen-1.5B \\
235	Mistral-7B    & non-Qwen & .961 & .555 & .524 & 1 & Qwen-1.5B \\
236	\bottomrule
237	\multicolumn{7}{l}{\footnotesize $^\dagger$Same-family scorer; cross-family scoring yields $\Kempirical{=}1$.}
238	\end{tabular}}
239	\end{table}
240	
241	\paragraph{Per-fold transparency.}
242	For Qwen-1.5B, cross-family scoring (Pythia-1.4B) yields $\auc$(1v2) $= 0.5994$, with per-fold values $[0.596, 0.606, 0.600, 0.603, 0.592]$ (2/5 folds marginally above $\theta = 0.60$).
243	The aggregate mean falls below $\theta$, confirming $\Kempirical{=}1$.
244	For Qwen-7B, the corresponding $\auc$ drops further to $0.587$.
245	
246	\subsection{ArXiv Cross-Scorer Bootstrap CIs}
247	\label{sec:arxiv_crossscorer_ci}
248	
249	\begin{table}[h]
250	\centering
251	\small
252	\caption{Bootstrap 95\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}
253	\label{tab:arxiv_crossscorer_ci}
254	\resizebox{\columnwidth}{!}{%
255	\begin{tabular}{lccc}
256	\toprule
257	\textbf{Generator} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & \textbf{CI lower $> \theta$} \\
258	\midrule
259	Qwen-1.5B    & 0.632 & $[0.617,\,0.646]$ & Yes \\
260	LLaMA-3.1-8B & 0.620 & $[0.605,\,0.636]$ & Yes (0.5\,pp margin) \\
261	Mistral-7B   & 0.608 & $[0.593,\,0.622]$ & No \\
262	Qwen-7B      & 0.599 & $[0.584,\,0.613]$ & No \\
263	\bottomrule
264	\end{tabular}}
265	\end{table}
266	
267	\subsection{JSD Decay Analysis}
268	\label{sec:jsd_extended}
269	
270	The token-level JSD between adjacent generations reveals two distinct decay regimes (Figure~\ref{fig:jsd_decay}).
271	For C4 web text, 0v1 JSD exceeds 1v2 by 6--56$\times$ across all 8 models (1B--14B) with $\Kempirical{=}2$ (median cliff ratio ${\sim}$15$\times$), and subsequent pairs converge to a noise floor of ${\sim}$0.003--0.005.
272	Fitting $\jsd(k, k{+}1) \propto e^{-\lambda k}$ yields $\lambda \approx 2.2$--$3.5$ for C4 (mean ${\approx}\,2.9$), consistent with rapid mixing of $G_\delta$ toward its stationary distribution.
273	These decay rates represent qualitative characterizations from 5-point curves rather than precise estimates.
274	The empirical decay rate $\lambda$ is consistent within each domain but varies across domains: C4 yields $\lambda \approx 2.9$, Wikipedia $\lambda \approx 3.1$ (excluding OLMo, whose $\lambda = 6.3$ reflects a capacity-limited collapse: 0v1 $\jsd = 0.169$ with near-complete information loss at the first step, making the exponential fit unreliable), and arXiv $\lambda \approx 1.0$.
275	This cross-model consistency indicates that the contraction rate of $G_\delta$ is governed primarily by the structure of the input domain rather than the model architecture.
276	ArXiv text decays ${\sim}$3$\times$ slower than C4 ($\lambda \approx 1.0$ vs.\ $2.9$), with a correspondingly higher convergence floor (${\sim}$0.007--0.009 vs.\ ${\sim}$0.003--0.004).
277	Formulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, explaining the elevated $\Kempirical{=}3$.
278	The retrain-chain exhibits a fundamentally different profile: $\lambda = 0.285$ with a cliff ratio of only 1.31$\times$ and no sharp drop between adjacent pairs.
279	This gradual, sustained divergence reflects cumulative model-adaptation artifacts rather than text-intrinsic information loss, further supporting the distinction between prompt-chain and retrain-chain $\Kempirical$ (Appendix~\ref{sec:boundary_extended}).
280	
281	\subsection{Boundary Cases and Scale Effect}
282	\label{sec:boundary_extended}
283	
284	Of 9 tested model configurations on C4, 8 yield $\Kempirical{=}2$; Mistral-7B is the sole sub-2 exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, CI $[0.584, 0.603]$), validating $\theta{=}0.60$ as an effective discriminator (gap: $0.594$ vs.\ $0.611$--$0.696$).
285	Mistral's cross-domain profile reinforces the domain-governed interpretation: despite $\Kempirical{=}1$ on both C4 and Wikipedia, it yields $\Kempirical{=}3$ on arXiv (1v2 $\auc = 0.820$, 2v3 $= 0.628$), and this profile persists under cross-scorer validation (Pythia-1.4B scorer: C4 $\Kempirical{=}1$, arXiv $\Kempirical{=}3$ (2v3 $\auc = 0.608$, CI $[0.593, 0.622]$)), indicating that domain structural complexity can rescue even web-text one-wash generators (Table~\ref{tab:domain_kstar}).
286	Larger models produce more human-like text, reducing 0v1 JSD: 0.16--0.29 at $\leq$1.5B, 0.077--0.13 at 7--14B.
287	However, Qwen-14B still yields $\Kempirical{=}2$ (1v2 $\auc = 0.621$, CI $[0.612, 0.630]$), with 0v1 $\auc = 0.960$ comparable to Qwen-7B ($0.964$), indicating that scale in the 1B--14B range does not shift the discrimination boundary.
288	
289	\paragraph{Sample-size control.}
290	As a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\Kempirical{=}1$ (1v2 $\auc = 0.601$, CI $[0.586, 0.616]$).
291	Reduced sample size widens confidence intervals and produces more conservative $\Kempirical$ estimates, confirming that arXiv's $\Kempirical{=}3$ at the same sample size reflects genuine domain signal rather than a statistical artifact of smaller training sets.
292	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c5c14a3-23b5-45cf-9139-de4e4327c476",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "cace27c9-fd66-4304-b199-680e0b686791",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
      "content": "\\section{Extended Analysis and Limitations}\n\\label{sec:extended_discussion}\n\nThis section provides supporting tables for cross-scorer validation (Tables~\\ref{tab:crossscorer}--\\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{minipage}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair) on per-fold pairwise $\\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\\times$ 5 folds $\\times$ 5 depth-pairs; 3 generators $\\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\\eta^2_p = 0.19$) relative to Depth-Pair ($\\eta^2_p = 1.00$) and Generator ($\\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination. While $\\eta^2_p = 0.19$ exceeds Cohen's (1988) threshold for a large effect, the Scorer contribution is approximately 5$\\times$ smaller than Generator ($\\eta^2_p = 0.89$) and dwarfed by Depth-Pair ($\\eta^2_p = 1.00$), supporting its characterization as practically minor in this context.}\n\\label{tab:anova_crossscorer}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Source} & \\textbf{df} & $F$ & $p$ & $\\eta^2_p$ \\\\\n\\midrule\nGenerator     & 2  & 926.8  & ${<}.001$  & .885 \\\\\nScorer        & 3  & 19.02  & ${<}.001$  & .192 \\\\\nDepth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\\\\nGen$\\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\\\\nGen$\\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\\\\nScorer$\\times$Depth & 12 & 2.45 & .005 & .109 \\\\\nResidual      & 240 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Extended Limitations}\n\\label{sec:extended_limitations}\n\n\\emph{Prompt-chain versus retrain-chain.}\nRetrain-chain validation (Pythia-1.4B LoRA, 5 generations) yields $\\Kempirical{\\geq}4$ (Table~\\ref{tab:retrain_ci}), far exceeding prompt-chain $\\Kempirical{=}2$.\nAll pairwise CIs have lower bounds well above $\\theta{=}0.60$ ($p < 0.001$), statistically confirming $\\Kempirical{\\geq}4$.\nThe elevated signal arises from cumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) rather than text-intrinsic degradation; prompt-chain $\\Kempirical$ is the operationally relevant boundary for data curation.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Retrain-chain pairwise $\\auc$ with bootstrap 95\\% CIs (Pythia-1.4B LoRA, 5 generations). All CI lower bounds $\\gg \\theta{=}0.60$.}\n\\label{tab:retrain_ci}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Pair} & $\\auc$ & \\textbf{95\\% CI} & $p$ \\\\\n\\midrule\n0v1 & 0.9842 & $[0.9823,\\,0.9860]$ & ${<}0.001$ \\\\\n1v2 & 0.9471 & $[0.9432,\\,0.9509]$ & ${<}0.001$ \\\\\n2v3 & 0.8888 & $[0.8832,\\,0.8943]$ & ${<}0.001$ \\\\\n3v4 & 0.7994 & $[0.7920,\\,0.8067]$ & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\emph{Threshold sensitivity.}\nTable~\\ref{tab:theta_sensitivity} reports $\\Kempirical$ across $\\theta \\in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.\nQwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp; all ten boundary comparisons yield permutation $p < 0.001$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{$\\Kempirical$ as a function of $\\theta$ across conditions. The \\textbf{domain ordering} (arXiv $>$ web $\\geq$ cross-scorer) and \\textbf{bounded range} ($\\Kempirical{\\leq}4$) are preserved across $\\theta \\in [0.55, 0.70]$. The headline result (web $\\Kempirical{=}2$, arXiv $\\Kempirical{=}3$) holds for $\\theta \\in [0.575, 0.625]$.}\n\\label{tab:theta_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Config} & $\\theta{=}0.55$ & $\\theta{=}0.60$ & $\\theta{=}0.625$ & $\\theta{=}0.70$ \\\\\n\\midrule\nC4 (web) & Qwen-rw      & 3 & 2 & 2 & 1 \\\\\nC4 (web) & Pythia       & 2 & 2 & 2 & 1 \\\\\nC4 (web) & OLMo         & 2 & 2 & 1 & 1 \\\\\nC4 (web) & Qwen-cont    & 3 & 2 & 2 & 1 \\\\\nC4 (web) & Qwen-7B      & 2 & 2 & 2 & 1 \\\\\nC4 (web) & Mistral-7B   & 1 & 1 & 1 & 1 \\\\\n\\midrule\narXiv    & Qwen-1.5B-base (cont.) & 4 & 3 & 3 & 2 \\\\\narXiv    & Pythia-1.4B (cont.)    & 4 & 3 & 3 & 2 \\\\\n\\midrule\nCross-scorer & Qwen-cont/Pythia-scored & 2 & 1 & 1 & 1 \\\\\nCross-scorer & Qwen-cont/OLMo-scored   & 2 & 1 & 1 & 1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\emph{Structural confound: token length.}\nIn continuation mode the generation prompt is discarded, so all depths $\\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\\ machine-generated prompt), not structural composition.\nDepth~0 texts average ${\\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\\ref{tab:token_length}).\nThis asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.\nWithin depths 1--5, mean token counts are stable (within-model range $\\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\\Kempirical{=}2$ are unaffected by length.\nEOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\\%, Pythia 34--36\\%, OLMo $<$1\\%, Qwen-continuation 17--20\\%, Qwen-7B 45--47\\%.\nModels with the highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.\n\n\\emph{Graduated filtering.}\nAll $\\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\\alpha{=}0.1$: 0.5873; $\\alpha{=}0.9$: 0.5892 vs.\\ 0.5941); at $\\alpha{=}0.9$, HellaSwag matches exactly (0.6701).\nBinary-ours significantly outperforms all alternatives on MMLU ($p_{\\text{corr}} \\leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\\text{corr}} = 0.011$).\n\\label{tab:pairwise_significance}\n\n\\subsection{Dose-Response: Contamination Ratio Effect}\n\\label{sec:dose_response}\n\nThe main filtering experiments (Section~\\ref{sec:filtering}) use 100\\% synthetic data to maximize effect size.\nTo characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\\%, 30\\%, and 50\\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\\ref{tab:dose_response}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MMLU and HellaSwag by contamination ratio and filtering strategy (5 seeds, mean $\\pm$ std). Base model MMLU: 0.6018. Binary filtering retains a significant advantage on HellaSwag across all ratios ($p \\leq 0.004$, Holm-Bonferroni corrected).}\n\\label{tab:dose_response}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{10\\%}} & \\multicolumn{2}{c}{\\textbf{30\\%}} & \\multicolumn{2}{c}{\\textbf{50\\%}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\n\\textbf{Strategy} & MMLU & HellaSwag & MMLU & HellaSwag & MMLU & HellaSwag \\\\\n\\midrule\nNo-filter   & $.6058{\\pm}.0002$ & $.6689{\\pm}.0006$ & $.6069{\\pm}.0007$ & $.6664{\\pm}.0018$ & $.6063{\\pm}.0012$ & $.6680{\\pm}.0005$ \\\\\nBinary-ours & $\\mathbf{.6079{\\pm}.0004}$ & $\\mathbf{.6727{\\pm}.0007}$ & $\\mathbf{.6082{\\pm}.0011}$ & $\\mathbf{.6725{\\pm}.0006}$ & $\\mathbf{.6088{\\pm}.0009}$ & $\\mathbf{.6731{\\pm}.0004}$ \\\\\nGraduated   & $.6066{\\pm}.0010$ & $.6700{\\pm}.0014$ & $.6072{\\pm}.0008$ & $.6665{\\pm}.0012$ & $.6062{\\pm}.0008$ & $.6679{\\pm}.0001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt all tested ratios (10--50\\%), no-filter MMLU remains above the base model (0.6018), indicating that synthetic data at these proportions is net-beneficial rather than harmful.\nBinary filtering consistently improves over no-filter, with HellaSwag differences significant across all ratios ($p \\leq 0.004$, Holm-Bonferroni corrected).\nMMLU differences are smaller and significant only at 10\\% after correction ($p = 0.001$).\nGraduated weighting is indistinguishable from no-filter at all ratios (MMLU $p \\geq 0.27$; HellaSwag $p \\geq 0.06$), confirming that depth assignments beyond $\\Kempirical$ inject noise regardless of contamination severity.\nEffect sizes diminish 3--6$\\times$ relative to the 100\\% setting (Section~\\ref{sec:filtering}), but the strategy ordering (binary $>$ graduated $\\approx$ no-filter) is preserved.\n\n\\subsection{Cross-Model Filtering Replication}\n\\label{sec:pythia_filtering}\n\nTo test whether $\\Kempirical{=}2$ correctly predicts optimal curation granularity across architectures, we replicate the filtering experiment on Pythia-1.4B (LoRA rank 8, nucleus $p{=}0.9$, $T{=}1.0$, 3 seeds; Table~\\ref{tab:pythia_filtering}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pythia-1.4B filtering replication (3 seeds, mean $\\pm$ std). Strategy ordering matches Qwen (binary $>$ no-filter $>$ graduated on MMLU).}\n\\label{tab:pythia_filtering}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU} & \\textbf{HellaSwag} \\\\\n\\midrule\nNo-filter & $.2568{\\pm}.0012$ & $.5250{\\pm}.0008$ \\\\\nBinary-ours & $\\mathbf{.2585{\\pm}.0004}$ & $.5251{\\pm}.0001$ \\\\\nGraduated$_{0.9}$ & $.2561{\\pm}.0009$ & $\\mathbf{.5253{\\pm}.0007}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe strategy ordering (binary $>$ no-filter $>$ graduated on MMLU) matches Qwen (Section~\\ref{sec:filtering}).\nThe small absolute differences reflect the model's near-chance MMLU baseline rather than filtering inefficacy; the consistent ordering across two architectures supports $\\Kempirical{=}2$'s predictive value for curation granularity.\nHellaSwag differences are negligible across all strategies.\n\n\\subsection{Feature Subset Stability}\n\\label{sec:feature_subset}\n\nTo test whether $\\Kempirical{=}2$ depends on the specific 15D feature combination, we evaluate random feature subsets of varying size on Pythia-1.4B prompt-chain data (Table~\\ref{tab:feature_subset}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{1v2 $\\auc$ by feature subset size (Pythia-1.4B). $\\Kempirical{=}2$ ($\\auc > \\theta{=}0.60$) is robust at $\\geq$8 features.}\n\\label{tab:feature_subset}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Subset} & \\textbf{Tested} & \\textbf{Pass} & \\textbf{Min $\\auc$} & \\textbf{Mean $\\auc$} \\\\\n\\midrule\n15D (full) & 1 & 1 & 0.6262 & 0.6262 \\\\\n10D        & 5 & 5 & 0.6153 & 0.6191 \\\\\n8D         & 5 & 5 & 0.6056 & 0.6159 \\\\\n5D         & 5 & 2 & 0.5856 & 0.5998 \\\\\n3D (top-3) & 1 & 0 & 0.5871 & 0.5871 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$\\Kempirical{=}2$ holds for all subsets of size $\\geq$8 (10/10 pass, min $\\auc = 0.6056$), becomes fragile at 5D (2/5 pass), and fails at 3D (top-3 surprisal features alone: $\\auc = 0.5871 < \\theta$).\nThe boundary does not depend on any specific feature combination but requires sufficient dimensionality ($\\geq$8) to capture the multi-faceted distributional shift between generations 1 and 2.\n\n\\subsection{self\\_BLEU Feature Independence}\n\\label{sec:selfbleu_ablation}\n\nTo verify that $\\Kempirical$ does not depend on the self\\_BLEU feature (which may reflect stylistic repetition rather than depth-correlated degradation), we compare 15D and 14D (self\\_BLEU removed) classifiers across four model configurations (Table~\\ref{tab:selfbleu_ablation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{15D vs.\\ 14D (self\\_BLEU removed) 1v2 $\\auc$ with bootstrap 95\\% CIs. Removing self\\_BLEU does not change $\\Kempirical$ for any configuration. Maximum $|\\Delta\\auc| = 0.0031$, within bootstrap CI width (${\\sim}0.018$).}\n\\label{tab:selfbleu_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & $\\Kempirical$ & \\textbf{15D $\\auc$ [CI]} & \\textbf{14D $\\auc$ [CI]} & $\\Delta$ \\\\\n\\midrule\nQwen-base   & 2/2 & $.6288$ $[.620,\\,.638]$ & $.6258$ $[.616,\\,.635]$ & $-.0031$ \\\\\nPythia-1.4B  & 2/2 & $.8840$ $[.878,\\,.890]$ & $.8830$ $[.876,\\,.889]$ & $-.0010$ \\\\\nLLaMA-8B     & 2/2 & $.6075$ $[.598,\\,.617]$ & $.6074$ $[.598,\\,.617]$ & $-.0001$ \\\\\nMistral-7B   & 1/1 & $.5902$ $[.580,\\,.600]$ & $.5903$ $[.580,\\,.600]$ & $+.0002$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAll four configurations preserve their $\\Kempirical$ under 14D, with negligible AUC change ($|\\Delta| \\leq 0.003$).\nThe self\\_BLEU feature contributes minimally to the depth boundary; $\\Kempirical{=}2$ is driven by surprisal and entropy features rather than lexical repetition statistics.\n\n\\subsection{Wikipedia Domain: Scorer Confound Resolution}\n\\label{sec:wiki_domain}\n\nUnder same-family scoring (Qwen-1.5B scorer), Wikipedia $\\Kempirical$ appeared to exhibit model-family dependence: Qwen generators (1.5B and 7B) yielded $\\Kempirical{=}2$, while all four non-Qwen models yielded $\\Kempirical{=}1$ (Table~\\ref{tab:wiki_domain}).\nA scorer confound ablation resolves this apparent split.\nRescoring the same Qwen-7B Wikipedia text with Pythia-1.4B reduces 1v2 $\\auc$ from $0.611$ to $0.587$ ($\\Delta = -2.4$\\,pp), dropping $\\Kempirical$ from 2 to 1.\nWith the scorer confound controlled, all six models yield $\\Kempirical{=}1$ on Wikipedia, and the domain ordering simplifies to: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $>$ Wikipedia ($\\Kempirical{=}1$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Wikipedia pairwise $\\auc$ across 6 models. $^\\dagger$Qwen rows use same-family scorer (Qwen-1.5B); cross-family scoring (Pythia-1.4B) reduces Qwen-7B to $\\Kempirical{=}1$ ($\\Delta = -2.4$\\,pp), resolving the apparent family split.}\n\\label{tab:wiki_domain}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Family} & \\textbf{0v1} & \\textbf{1v2} & \\textbf{2v3} & $\\Kempirical$ & \\textbf{Scorer} \\\\\n\\midrule\nQwen-1.5B (base) & Qwen & ---  & .619 & .550 & 2$^\\dagger$ & Qwen-1.5B \\\\\nQwen-1.5B (base) & Qwen & ---  & .599 & ---  & 1 & Pythia-1.4B \\\\\nQwen-7B          & Qwen & .967 & .611 & .556 & 2$^\\dagger$ & Qwen-1.5B \\\\\nQwen-7B          & Qwen & ---  & .587 & ---  & 1 & Pythia-1.4B \\\\\n\\midrule\nPythia-1.4B   & non-Qwen & .975 & .585 & .545 & 1 & Qwen-1.5B \\\\\nOLMo-1B       & non-Qwen & .993 & .499 & .501 & 1 & Qwen-1.5B \\\\\nLLaMA-3.1-8B  & non-Qwen & .932 & .595 & .539 & 1 & Qwen-1.5B \\\\\nMistral-7B    & non-Qwen & .961 & .555 & .524 & 1 & Qwen-1.5B \\\\\n\\bottomrule\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$Same-family scorer; cross-family scoring yields $\\Kempirical{=}1$.}\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-fold transparency.}\nFor Qwen-1.5B, cross-family scoring (Pythia-1.4B) yields $\\auc$(1v2) $= 0.5994$, with per-fold values $[0.596, 0.606, 0.600, 0.603, 0.592]$ (2/5 folds marginally above $\\theta = 0.60$).\nThe aggregate mean falls below $\\theta$, confirming $\\Kempirical{=}1$.\nFor Qwen-7B, the corresponding $\\auc$ drops further to $0.587$.\n\n\\subsection{ArXiv Cross-Scorer Bootstrap CIs}\n\\label{sec:arxiv_crossscorer_ci}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}\n\\label{tab:arxiv_crossscorer_ci}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Generator} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & \\textbf{CI lower $> \\theta$} \\\\\n\\midrule\nQwen-1.5B    & 0.632 & $[0.617,\\,0.646]$ & Yes \\\\\nLLaMA-3.1-8B & 0.620 & $[0.605,\\,0.636]$ & Yes (0.5\\,pp margin) \\\\\nMistral-7B   & 0.608 & $[0.593,\\,0.622]$ & No \\\\\nQwen-7B      & 0.599 & $[0.584,\\,0.613]$ & No \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{JSD Decay Analysis}\n\\label{sec:jsd_extended}\n\nThe token-level JSD between adjacent generations reveals two distinct decay regimes (Figure~\\ref{fig:jsd_decay}).\nFor C4 web text, 0v1 JSD exceeds 1v2 by 6--56$\\times$ across all 8 models (1B--14B) with $\\Kempirical{=}2$ (median cliff ratio ${\\sim}$15$\\times$), and subsequent pairs converge to a noise floor of ${\\sim}$0.003--0.005.\nFitting $\\jsd(k, k{+}1) \\propto e^{-\\lambda k}$ yields $\\lambda \\approx 2.2$--$3.5$ for C4 (mean ${\\approx}\\,2.9$), consistent with rapid mixing of $G_\\delta$ toward its stationary distribution.\nThese decay rates represent qualitative characterizations from 5-point curves rather than precise estimates.\nThe empirical decay rate $\\lambda$ is consistent within each domain but varies across domains: C4 yields $\\lambda \\approx 2.9$, Wikipedia $\\lambda \\approx 3.1$ (excluding OLMo, whose $\\lambda = 6.3$ reflects a capacity-limited collapse: 0v1 $\\jsd = 0.169$ with near-complete information loss at the first step, making the exponential fit unreliable), and arXiv $\\lambda \\approx 1.0$.\nThis cross-model consistency indicates that the contraction rate of $G_\\delta$ is governed primarily by the structure of the input domain rather than the model architecture.\nArXiv text decays ${\\sim}$3$\\times$ slower than C4 ($\\lambda \\approx 1.0$ vs.\\ $2.9$), with a correspondingly higher convergence floor (${\\sim}$0.007--0.009 vs.\\ ${\\sim}$0.003--0.004).\nFormulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, explaining the elevated $\\Kempirical{=}3$.\nThe retrain-chain exhibits a fundamentally different profile: $\\lambda = 0.285$ with a cliff ratio of only 1.31$\\times$ and no sharp drop between adjacent pairs.\nThis gradual, sustained divergence reflects cumulative model-adaptation artifacts rather than text-intrinsic information loss, further supporting the distinction between prompt-chain and retrain-chain $\\Kempirical$ (Appendix~\\ref{sec:boundary_extended}).\n\n\\subsection{Boundary Cases and Scale Effect}\n\\label{sec:boundary_extended}\n\nOf 9 tested model configurations on C4, 8 yield $\\Kempirical{=}2$; Mistral-7B is the sole sub-2 exception ($\\Kempirical{=}1$; 1v2 $\\auc = 0.594$, CI $[0.584, 0.603]$), validating $\\theta{=}0.60$ as an effective discriminator (gap: $0.594$ vs.\\ $0.611$--$0.696$).\nMistral's cross-domain profile reinforces the domain-governed interpretation: despite $\\Kempirical{=}1$ on both C4 and Wikipedia, it yields $\\Kempirical{=}3$ on arXiv (1v2 $\\auc = 0.820$, 2v3 $= 0.628$), and this profile persists under cross-scorer validation (Pythia-1.4B scorer: C4 $\\Kempirical{=}1$, arXiv $\\Kempirical{=}3$ (2v3 $\\auc = 0.608$, CI $[0.593, 0.622]$)), indicating that domain structural complexity can rescue even web-text one-wash generators (Table~\\ref{tab:domain_kstar}).\nLarger models produce more human-like text, reducing 0v1 JSD: 0.16--0.29 at $\\leq$1.5B, 0.077--0.13 at 7--14B.\nHowever, Qwen-14B still yields $\\Kempirical{=}2$ (1v2 $\\auc = 0.621$, CI $[0.612, 0.630]$), with 0v1 $\\auc = 0.960$ comparable to Qwen-7B ($0.964$), indicating that scale in the 1B--14B range does not shift the discrimination boundary.\n\n\\paragraph{Sample-size control.}\nAs a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\\Kempirical{=}1$ (1v2 $\\auc = 0.601$, CI $[0.586, 0.616]$).\nReduced sample size widens confidence intervals and produces more conservative $\\Kempirical$ estimates, confirming that arXiv's $\\Kempirical{=}3$ at the same sample size reflects genuine domain signal rather than a statistical artifact of smaller training sets.\n",
      "numLines": 292,
      "startLine": 1,
      "totalLines": 292
    }
  },
  "sourceToolAssistantUUID": "0c5c14a3-23b5-45cf-9139-de4e4327c476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 51 · 2026-05-18T09:57:38.193Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0142QUXX3LZSEZJGzECAgYza`</summary>

```json
{
  "pattern": "tables/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cace27c9-fd66-4304-b199-680e0b686791",
  "isSidechain": false,
  "requestId": "req_011Cb9qSLs9frHhrSZSGCbqi",
  "type": "assistant",
  "uuid": "ba02b295-7b05-4ea2-be51-6b08377e9fdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VfxG7JyWRitavZy524FYK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 13741,
      "cache_creation_input_tokens": 1397,
      "cache_read_input_tokens": 42870,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1397,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 13741,
          "output_tokens": 293,
          "cache_read_input_tokens": 42870,
          "cache_creation_input_tokens": 1397,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1397
          },
          "type": "message"
        }
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

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性**  ### Venue 信息 - **目标**: EMNLP 2026（ARR May 2026 cycle） - **Deadline**: 2026-05-25 - **格式**: ACL 双栏模板，`\\usepackage[review]{acl}`，Long…",
  "leafUuid": "ffeca9ec-6915-40f3-a953-288812c96a91",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on generational depth contamination detection",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Assistant

_source line 54 · 2026-05-18T09:57:42.570Z_

<details><summary>Logged reasoning block</summary>

```text
Let me find the tables directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffeca9ec-6915-40f3-a953-288812c96a91",
  "isSidechain": false,
  "requestId": "req_011Cb9qSsDma71yB26eBFL5x",
  "type": "assistant",
  "uuid": "1c95b8be-55fd-417d-9d42-1654b50c4617",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VitT4Lnfy1hcboAyNYMdd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 35634,
      "cache_read_input_tokens": 44267,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35634,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 44267,
          "cache_creation_input_tokens": 35634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35634
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-18T09:57:43.155Z_

查找表格文件的实际位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c95b8be-55fd-417d-9d42-1654b50c4617",
  "isSidechain": false,
  "requestId": "req_011Cb9qSsDma71yB26eBFL5x",
  "type": "assistant",
  "uuid": "360cb107-5d67-4a15-8431-5b9698b6275b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VitT4Lnfy1hcboAyNYMdd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 35634,
      "cache_read_input_tokens": 44267,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35634,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 44267,
          "cache_creation_input_tokens": 35634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35634
          },
          "type": "message"
        }
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

_source line 56 · 2026-05-18T09:57:44.744Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01N64TMBWGwQdTWA3qrK7emb`</summary>

```json
{
  "pattern": "**/docs/paper/tables/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "360cb107-5d67-4a15-8431-5b9698b6275b",
  "isSidechain": false,
  "requestId": "req_011Cb9qSsDma71yB26eBFL5x",
  "type": "assistant",
  "uuid": "6dec4cd7-8620-476e-a44f-f5b4e3cfdf1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VitT4Lnfy1hcboAyNYMdd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 35634,
      "cache_read_input_tokens": 44267,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35634,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 44267,
          "cache_creation_input_tokens": 35634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35634
          },
          "type": "message"
        }
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

_source line 57 · 2026-05-18T09:57:44.771Z_

<details><summary>↩ Tool result · `toolu_01N64TMBWGwQdTWA3qrK7emb`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_filtering_main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_alpha_sweep.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_pairwise_significance.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6dec4cd7-8620-476e-a44f-f5b4e3cfdf1a",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "4a8e9414-79ec-47c5-b255-c5960853ddad",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_filtering_main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_alpha_sweep.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_pairwise_significance.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex"
    ],
    "durationMs": 19,
    "numFiles": 6,
    "truncated": false
  },
  "sourceToolAssistantUUID": "6dec4cd7-8620-476e-a44f-f5b4e3cfdf1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-18T09:57:48.069Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GeUMPAj7BBudJVuDBY6Mpy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_filtering_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a8e9414-79ec-47c5-b255-c5960853ddad",
  "isSidechain": false,
  "requestId": "req_011Cb9qTMHyNZ9dQ4eyPvS4i",
  "type": "assistant",
  "uuid": "d78ef51d-9230-4f62-b7e0-de3a03884c6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CFWZ4BzwVPHUTm5nLQzWRj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 417,
      "cache_read_input_tokens": 79901,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 417,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 79901,
          "cache_creation_input_tokens": 417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 417
          },
          "type": "message"
        }
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

_source line 59 · 2026-05-18T09:57:48.074Z_

<details><summary>↩ Tool result · `toolu_01GeUMPAj7BBudJVuDBY6Mpy`</summary>

```text
1	\begin{tabular}{lcc}
2	\toprule
3	\textbf{Strategy} & \textbf{MMLU} & \textbf{HellaSwag} \\
4	\midrule
5	Base model (no training) & 0.6018 & 0.6821 \\
6	\midrule
7	Binary-ours ($\Kstar{=}2$) & \textbf{0.5941}$\pm$0.0008 & \textbf{0.6701}$\pm$0.0006 \\
8	Binary-Drayson & 0.5913$\pm$0.0009 & 0.6691$\pm$0.0004 \\
9	Surprisal & 0.5894$\pm$0.0009 & 0.6641$\pm$0.0006 \\
10	Graduated ($\alpha{=}0.9$) & 0.5892$\pm$0.0008 & 0.6701$\pm$0.0007 \\
11	DSIR & 0.5869$\pm$0.0003 & 0.6631$\pm$0.0007 \\
12	No filter & 0.5865$\pm$0.0010 & 0.6638$\pm$0.0008 \\
13	\bottomrule
14	\end{tabular}
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d78ef51d-9230-4f62-b7e0-de3a03884c6a",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "2a25addb-5643-4fd9-a893-cc40d102e274",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_filtering_main.tex",
      "content": "\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU} & \\textbf{HellaSwag} \\\\\n\\midrule\nBase model (no training) & 0.6018 & 0.6821 \\\\\n\\midrule\nBinary-ours ($\\Kstar{=}2$) & \\textbf{0.5941}$\\pm$0.0008 & \\textbf{0.6701}$\\pm$0.0006 \\\\\nBinary-Drayson & 0.5913$\\pm$0.0009 & 0.6691$\\pm$0.0004 \\\\\nSurprisal & 0.5894$\\pm$0.0009 & 0.6641$\\pm$0.0006 \\\\\nGraduated ($\\alpha{=}0.9$) & 0.5892$\\pm$0.0008 & 0.6701$\\pm$0.0007 \\\\\nDSIR & 0.5869$\\pm$0.0003 & 0.6631$\\pm$0.0007 \\\\\nNo filter & 0.5865$\\pm$0.0010 & 0.6638$\\pm$0.0008 \\\\\n\\bottomrule\n\\end{tabular}\n",
      "numLines": 15,
      "startLine": 1,
      "totalLines": 15
    }
  },
  "sourceToolAssistantUUID": "d78ef51d-9230-4f62-b7e0-de3a03884c6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-18T09:57:48.461Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WUTooCWjQwtyfxowLHuzem`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a25addb-5643-4fd9-a893-cc40d102e274",
  "isSidechain": false,
  "requestId": "req_011Cb9qTMHyNZ9dQ4eyPvS4i",
  "type": "assistant",
  "uuid": "273a072f-ae16-4bb3-8176-485c10ab8038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CFWZ4BzwVPHUTm5nLQzWRj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 417,
      "cache_read_input_tokens": 79901,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 417,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 79901,
          "cache_creation_input_tokens": 417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 417
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-18T09:57:48.467Z_

<details><summary>↩ Tool result · `toolu_01WUTooCWjQwtyfxowLHuzem`</summary>

```text
1	{\small
2	\begin{tabular}{llcccc}
3	\toprule
4	\textbf{Scorer} & \textbf{Gen.\ Data} & $\boldsymbol{K^*}$ & \textbf{AUC(0v1)} & \textbf{AUC(1v2)} & \textbf{Spearman}~$\boldsymbol{\rho}$ \\
5	\midrule
6	% --- Qwen-RW block ---
7	Qwen-1.5B (self) & Qwen-RW & 2 & --- & 0.6955 & --- \\
8	Pythia-1.4B       & Qwen-RW & 2 & 0.9923 & 0.7012 & 0.906 \\
9	OLMo-1B           & Qwen-RW & 2 & 0.9918 & 0.6947 & 0.920 \\
10	\midrule
11	% --- Qwen-cont block ---
12	Qwen-1.5B (self) & Qwen-cont & 2 & --- & 0.6112 & --- \\
13	Pythia-1.4B       & Qwen-cont & \textcolor{red}{1\textsuperscript{$\dagger$}} & 0.9900 & \underline{0.5923} & 0.942 \\
14	OLMo-1B           & Qwen-cont & \textcolor{red}{1\textsuperscript{$\dagger$}} & 0.9890 & \underline{0.5858} & 0.902 \\
15	\midrule
16	% --- Qwen-7B cross-scale block ---
17	Qwen-1.5B        & Qwen-7B-cont & 2 & 0.9644 & 0.6178 & --- \\
18	\bottomrule
19	\end{tabular}
20	}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "273a072f-ae16-4bb3-8176-485c10ab8038",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "c79ad091-e034-4220-a491-dd7dfb87e948",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex",
      "content": "{\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Scorer} & \\textbf{Gen.\\ Data} & $\\boldsymbol{K^*}$ & \\textbf{AUC(0v1)} & \\textbf{AUC(1v2)} & \\textbf{Spearman}~$\\boldsymbol{\\rho}$ \\\\\n\\midrule\n% --- Qwen-RW block ---\nQwen-1.5B (self) & Qwen-RW & 2 & --- & 0.6955 & --- \\\\\nPythia-1.4B       & Qwen-RW & 2 & 0.9923 & 0.7012 & 0.906 \\\\\nOLMo-1B           & Qwen-RW & 2 & 0.9918 & 0.6947 & 0.920 \\\\\n\\midrule\n% --- Qwen-cont block ---\nQwen-1.5B (self) & Qwen-cont & 2 & --- & 0.6112 & --- \\\\\nPythia-1.4B       & Qwen-cont & \\textcolor{red}{1\\textsuperscript{$\\dagger$}} & 0.9900 & \\underline{0.5923} & 0.942 \\\\\nOLMo-1B           & Qwen-cont & \\textcolor{red}{1\\textsuperscript{$\\dagger$}} & 0.9890 & \\underline{0.5858} & 0.902 \\\\\n\\midrule\n% --- Qwen-7B cross-scale block ---\nQwen-1.5B        & Qwen-7B-cont & 2 & 0.9644 & 0.6178 & --- \\\\\n\\bottomrule\n\\end{tabular}\n}\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  },
  "sourceToolAssistantUUID": "273a072f-ae16-4bb3-8176-485c10ab8038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 62 · 2026-05-18T09:57:51.704Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have read all the main content, appendix, and tables. Let me also fetch the ARR reviewer guidelines page for specific details, and then search for any potentially missing references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c79ad091-e034-4220-a491-dd7dfb87e948",
  "isSidechain": false,
  "requestId": "req_011Cb9qTdAD9szASuTfhbAqJ",
  "type": "assistant",
  "uuid": "5ccc5223-cf12-4a25-ae00-e7bdeecdcb32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJFbnpTr2H2iXn8YaFKjXa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 80318,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1134,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 80318,
          "cache_creation_input_tokens": 1134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1134
          },
          "type": "message"
        }
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

_source line 63 · 2026-05-18T09:57:52.205Z_

搜索可能遗漏的近期相关工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ccc5223-cf12-4a25-ae00-e7bdeecdcb32",
  "isSidechain": false,
  "requestId": "req_011Cb9qTdAD9szASuTfhbAqJ",
  "type": "assistant",
  "uuid": "01461566-2038-49e5-82fb-f7b9da31c826",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJFbnpTr2H2iXn8YaFKjXa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 80318,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1134,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 80318,
          "cache_creation_input_tokens": 1134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1134
          },
          "type": "message"
        }
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

_source line 64 · 2026-05-18T09:57:53.290Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018tbGwTHVK4SokocvpsUB8D`</summary>

```json
{
  "query": "recursive synthetic text detection generational depth estimation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01461566-2038-49e5-82fb-f7b9da31c826",
  "isSidechain": false,
  "requestId": "req_011Cb9qTdAD9szASuTfhbAqJ",
  "type": "assistant",
  "uuid": "ad7c70be-192a-472e-af3f-527e73274b9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJFbnpTr2H2iXn8YaFKjXa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 80318,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1134,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 80318,
          "cache_creation_input_tokens": 1134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1134
          },
          "type": "message"
        }
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

_source line 65 · 2026-05-18T09:57:54.101Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M11H74dtvPtwd5vB4a4emD`</summary>

```json
{
  "query": "model collapse data contamination detection filtering 2025 2026 NeurIPS ICML ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad7c70be-192a-472e-af3f-527e73274b9c",
  "isSidechain": false,
  "requestId": "req_011Cb9qTdAD9szASuTfhbAqJ",
  "type": "assistant",
  "uuid": "663bd2f7-1a09-4e43-843a-7f60973e0280",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJFbnpTr2H2iXn8YaFKjXa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 80318,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1134,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 80318,
          "cache_creation_input_tokens": 1134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1134
          },
          "type": "message"
        }
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

_source line 66 · 2026-05-18T09:57:54.537Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CmrVPJ8eiNbi4J1LTing29`</summary>

```json
{
  "query": "\"iterative synthetic data\" detection depth multi-generation text 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "663bd2f7-1a09-4e43-843a-7f60973e0280",
  "isSidechain": false,
  "requestId": "req_011Cb9qTdAD9szASuTfhbAqJ",
  "type": "assistant",
  "uuid": "e3d1e549-bb1b-4a99-a07b-ef5b71244173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJFbnpTr2H2iXn8YaFKjXa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 80318,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1134,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 80318,
          "cache_creation_input_tokens": 1134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1134
          },
          "type": "message"
        }
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

_source line 67 · 2026-05-18T09:58:01.038Z_

<details><summary>↩ Tool result · `toolu_01M11H74dtvPtwd5vB4a4emD`</summary>

```text
Web search results for query: "model collapse data contamination detection filtering 2025 2026 NeurIPS ICML ICLR"

Links: [{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Preventing Model Collapse in the Synthetic-Data Era","url":"https://cseweb.ucsd.edu/~yuxiangw/classes/AIsafety-2025Fall/Lectures/preventing_model_collapse_suraj.pdf"},{"title":"ICML Poster Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://icml.cc/virtual/2025/poster/44713"},{"title":"ICML 2025 Papers","url":"https://icml.cc/virtual/2025/papers.html"},{"title":"NeurIPS Poster A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://neurips.cc/virtual/2025/poster/119754"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"Strong Model Collapse | OpenReview","url":"https://openreview.net/forum?id=et5l9qPUhm"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"ICML 2025 Orals","url":"https://icml.cc/virtual/2025/events/oral"},{"title":"ICML Poster How Much Can We Forget about Data Contamination?","url":"https://icml.cc/virtual/2025/poster/45377"}]

I've performed the web search for your query about model collapse, data contamination detection and filtering related to recent conferences. Here are the key findings:

## Major Conference Papers (2025-2026)

**ICLR 2025:**
- "Strong Model Collapse" was published as a conference paper at ICLR 2025
- The paper establishes a strong form of model collapse phenomenon - critical performance degradation due to synthetic data in training corpus - showing that even as little as 1 per 1000 synthetic data can lead to collapse

**ICML 2025:**
- A paper titled "Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World" was presented, discussing how collapse can be avoided by managing how available data are used in pretraining
- An ICML 2025 poster titled "How Much Can We Forget about Data Contamination?" challenges the common assumption that small-scale benchmark data leakage into training data renders evaluations invalid

**NeurIPS 2025:**
- A paper titled "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective" addresses how recursive training on synthetic data leads to performance degradation

## Detection and Filtering Solutions

Recent studies caution that recursively training models on synthetic data alone can lead to degradation of quality, a phenomenon called model collapse. Watermarking and provenance tracking enable safe data curation at scale and form a comprehensive defense against synthetic data contamination when combined with organizational policies and technical guardrails.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "663bd2f7-1a09-4e43-843a-7f60973e0280",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "a1d4990c-27f2-4047-a943-c3c71f04fadc",
  "toolUseResult": {
    "query": "model collapse data contamination detection filtering 2025 2026 NeurIPS ICML ICLR",
    "results": [
      {
        "tool_use_id": "srvtoolu_019Aeg1K1MbsCzSVdoFpouFU",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"
          },
          {
            "title": "Preventing Model Collapse in the Synthetic-Data Era",
            "url": "https://cseweb.ucsd.edu/~yuxiangw/classes/AIsafety-2025Fall/Lectures/preventing_model_collapse_suraj.pdf"
          },
          {
            "title": "ICML Poster Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World",
            "url": "https://icml.cc/virtual/2025/poster/44713"
          },
          {
            "title": "ICML 2025 Papers",
            "url": "https://icml.cc/virtual/2025/papers.html"
          },
          {
            "title": "NeurIPS Poster A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective",
            "url": "https://neurips.cc/virtual/2025/poster/119754"
          },
          {
            "title": "ICLR 2025 Papers",
            "url": "https://iclr.cc/virtual/2025/papers.html"
          },
          {
            "title": "Strong Model Collapse | OpenReview",
            "url": "https://openreview.net/forum?id=et5l9qPUhm"
          },
          {
            "title": "Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.",
            "url": "https://arxiv.org/html/2510.16657v1"
          },
          {
            "title": "ICML 2025 Orals",
            "url": "https://icml.cc/virtual/2025/events/oral"
          },
          {
            "title": "ICML Poster How Much Can We Forget about Data Contamination?",
            "url": "https://icml.cc/virtual/2025/poster/45377"
          }
        ]
      },
      "I've performed the web search for your query about model collapse, data contamination detection and filtering related to recent conferences. Here are the key findings:\n\n## Major Conference Papers (2025-2026)\n\n**ICLR 2025:**\n- \"Strong Model Collapse\" was published as a conference paper at ICLR 2025\n- The paper establishes a strong form of model collapse phenomenon - critical performance degradation due to synthetic data in training corpus - showing that even as little as 1 per 1000 synthetic data can lead to collapse\n\n**ICML 2025:**\n- A paper titled \"Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World\" was presented, discussing how collapse can be avoided by managing how available data are used in pretraining\n- An ICML 2025 poster titled \"How Much Can We Forget about Data Contamination?\" challenges the common assumption that small-scale benchmark data leakage into training data renders evaluations invalid\n\n**NeurIPS 2025:**\n- A paper titled \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\" addresses how recursive training on synthetic data leads to performance degradation\n\n## Detection and Filtering Solutions\n\nRecent studies caution that recursively training models on synthetic data alone can lead to degradation of quality, a phenomenon called model collapse. Watermarking and provenance tracking enable safe data curation at scale and form a comprehensive defense against synthetic data contamination when combined with organizational policies and technical guardrails."
    ],
    "durationSeconds": 6.933789674999993
  },
  "sourceToolAssistantUUID": "663bd2f7-1a09-4e43-843a-7f60973e0280",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 68 · 2026-05-18T09:58:01.569Z_

<details><summary>↩ Tool result · `toolu_018tbGwTHVK4SokocvpsUB8D`</summary>

```text
Web search results for query: "recursive synthetic text detection generational depth estimation 2024 2025"

Links: [{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654"},{"title":"(PDF) Machine-generated text detection prevents language model collapse","url":"https://www.researchgate.net/publication/397412242_Machine-generated_text_detection_prevents_language_model_collapse"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"A Survey on LLM-Generated Text Detection:","url":"https://arxiv.org/pdf/2310.14724"},{"title":"Enhancing the Robustness of AI-Generated Text Detectors: A Survey","url":"https://www.mdpi.com/2227-7390/13/13/2145"},{"title":"DEPTH ANY VIDEO WITH SCALABLE SYNTHETIC DATA","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f23750c16a2b5e7e4992db4702a0c366-Paper-Conference.pdf"},{"title":"Benchmarking AI Text Detection: Assessing Detectors ...","url":"https://aclanthology.org/2025.genaidetect-1.4.pdf"},{"title":"TempParaphraser: \"Heating Up\" Text to Evade AI- ...","url":"https://aclanthology.org/2025.emnlp-main.1607.pdf"},{"title":"The Imitation Game revisited: A comprehensive survey on recent advances in AI-generated text detection - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417425003161"},{"title":"Recent Trends in Vision-Based Depth Estimation","url":"https://arxiv.org/pdf/2507.11540"}]

Based on the search results, I found relevant research on machine-generated text detection and recursive training in 2024-2025:

## Key Findings

A paper published at the 2025 Conference on Empirical Methods in Natural Language Processing addresses machine-generated text detection to prevent language model collapse. In recursive training processes, further model iterations are trained on a mix of human and synthetic data from the previous generation(s).

The method was validated on four LLMs from two model families (GPT-2 and SmolLM2), and demonstrates that it not only prevents model collapse but also improves performance compared to training on purely human data.

## Generational Depth and Detection

The research addresses challenges in recursive text generation. Deterministic decoding strategies lead to severe model collapse with perplexity scores increasing significantly, while stochastic sampling methods exhibit linear degradation across generations.

## Related Context

Recursive paraphrase can significantly reduce detection rates for AI-generated text detection, highlighting the challenge of detecting text that has been recursively modified through multiple generations.

The search results indicate this is an active area of research in 2024-2025, focusing on how to detect and manage synthetic text when models are trained on recursively generated data, and how generational depth affects both detection accuracy and model quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad7c70be-192a-472e-af3f-527e73274b9c",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "acc83827-d07f-4ca5-8d15-40fa80959647",
  "toolUseResult": {
    "query": "recursive synthetic text detection generational depth estimation 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NqgU2oaWtXBf97hw8TJWVw",
        "content": [
          {
            "title": "Machine-generated text detection prevents language model collapse",
            "url": "https://arxiv.org/html/2502.15654"
          },
          {
            "title": "(PDF) Machine-generated text detection prevents language model collapse",
            "url": "https://www.researchgate.net/publication/397412242_Machine-generated_text_detection_prevents_language_model_collapse"
          },
          {
            "title": "Diversity Boosts AI-Generated Text Detection",
            "url": "https://arxiv.org/pdf/2509.18880"
          },
          {
            "title": "A Survey on LLM-Generated Text Detection:",
            "url": "https://arxiv.org/pdf/2310.14724"
          },
          {
            "title": "Enhancing the Robustness of AI-Generated Text Detectors: A Survey",
            "url": "https://www.mdpi.com/2227-7390/13/13/2145"
          },
          {
            "title": "DEPTH ANY VIDEO WITH SCALABLE SYNTHETIC DATA",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/f23750c16a2b5e7e4992db4702a0c366-Paper-Conference.pdf"
          },
          {
            "title": "Benchmarking AI Text Detection: Assessing Detectors ...",
            "url": "https://aclanthology.org/2025.genaidetect-1.4.pdf"
          },
          {
            "title": "TempParaphraser: \"Heating Up\" Text to Evade AI- ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1607.pdf"
          },
          {
            "title": "The Imitation Game revisited: A comprehensive survey on recent advances in AI-generated text detection - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0957417425003161"
          },
          {
            "title": "Recent Trends in Vision-Based Depth Estimation",
            "url": "https://arxiv.org/pdf/2507.11540"
          }
        ]
      },
      "Based on the search results, I found relevant research on machine-generated text detection and recursive training in 2024-2025:\n\n## Key Findings\n\nA paper published at the 2025 Conference on Empirical Methods in Natural Language Processing addresses machine-generated text detection to prevent language model collapse. In recursive training processes, further model iterations are trained on a mix of human and synthetic data from the previous generation(s).\n\nThe method was validated on four LLMs from two model families (GPT-2 and SmolLM2), and demonstrates that it not only prevents model collapse but also improves performance compared to training on purely human data.\n\n## Generational Depth and Detection\n\nThe research addresses challenges in recursive text generation. Deterministic decoding strategies lead to severe model collapse with perplexity scores increasing significantly, while stochastic sampling methods exhibit linear degradation across generations.\n\n## Related Context\n\nRecursive paraphrase can significantly reduce detection rates for AI-generated text detection, highlighting the challenge of detecting text that has been recursively modified through multiple generations.\n\nThe search results indicate this is an active area of research in 2024-2025, focusing on how to detect and manage synthetic text when models are trained on recursively generated data, and how generational depth affects both detection accuracy and model quality."
    ],
    "durationSeconds": 8.276315556000002
  },
  "sourceToolAssistantUUID": "ad7c70be-192a-472e-af3f-527e73274b9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 69_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性**  ### Venue 信息 - **目标**: EMNLP 2026（ARR May 2026 cycle） - **Deadline**: 2026-05-25 - **格式**: ACL 双栏模板，`\\usepackage[review]{acl}`，Long…",
  "leafUuid": "acc83827-d07f-4ca5-8d15-40fa80959647",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Runtime record

_source line 70_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on generational depth contamination detection",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Tool result

_source line 71 · 2026-05-18T09:58:02.752Z_

<details><summary>↩ Tool result · `toolu_01CmrVPJ8eiNbi4J1LTing29`</summary>

```text
Web search results for query: ""iterative synthetic data" detection depth multi-generation text 2025"

Links: [{"title":"Synthetic Data Generation Using Large Language Models: Advances in Text and Code","url":"https://arxiv.org/html/2503.14023v2"},{"title":"GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub","url":"https://github.com/pengr/LLM-Synthetic-Data"},{"title":"A Lightweight Pipeline for Rewards-Guided Synthetic Text ...","url":"https://proceedings.scipy.org/articles/hprh2773.pdf"},{"title":"Synthetic Text Generation for Training Large Language Models","url":"https://openreview.net/pdf?id=mHySkOp46b"},{"title":"ORCHESTRATING SYNTHETIC DATA WITH REASONING","url":"https://openreview.net/pdf?id=VOoeogZbMb"},{"title":"Designing synthetic datasets for the real world: Mechanism design and reasoning from first principles","url":"https://research.google/blog/designing-synthetic-datasets-for-the-real-world-mechanism-design-and-reasoning-from-first-principles/"},{"title":"ARISE: Iterative Rule Induction and Synthetic Data Generation for Text Classification - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.359/"},{"title":"[2502.17607] Synthetic Text Generation for Training Large Language Models via Gradient Matching","url":"https://arxiv.org/abs/2502.17607"},{"title":"What is Synthetic Data Generation (SDG)? | NVIDIA Glossary","url":"https://www.nvidia.com/en-us/glossary/synthetic-data-generation/"},{"title":"Generative Models for Synthetic Data: A Deep Dive into the Gen AI Era | by Jay Vithlani | Dec, 2025 | Medium","url":"https://medium.com/@jvithlani4/generative-models-for-synthetic-data-a-deep-dive-into-the-gen-ai-era-cbd5bcb77187"}]

I've performed the web search for "iterative synthetic data detection depth multi-generation text 2025". Here are the key findings:

## Recent Research on Iterative Synthetic Data Generation

Large language models (LLMs) are transforming synthetic training data generation in both natural language and code domains, with key techniques including prompt-based generation, retrieval-augmented pipelines, and iterative self-refinement.

### Multi-Generation and Iterative Approaches

Recent frameworks employ reasoning-driven, recursive expansion processes where at each depth level, the system generates multiple candidate sub-categories that are evaluated, merged, and filtered by a critic model, building a dense, hierarchical taxonomy through iterative "propose-and-refine" loops.

One complete pipeline integrates all components into an iterative loop where in each subsequent iteration, new synthetic samples are generated and merged with the deduplicated dataset from the previous round, with the combined dataset then subjected to semantic deduplication to maintain high semantic diversity and quality standards.

### Text Classification Approach

ARISE is a framework that combines synthetic data generation and automatic rule induction via bootstrapping to iteratively filter the generated rules and data.

### Important Concerns with Multi-Generation

If you train a model on synthetic data, generate more data from it, then train again, quality degrades rapidly as the tails of the distribution disappear and the model converges to an average version of reality due to self-referential training amplifying biases with variance shrinking with each generation.

The search results show active research in 2025 on iterative synthetic data generation with various approaches to maintaining quality and diversity across multiple generations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3d1e549-bb1b-4a99-a07b-ef5b71244173",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "76a7575e-ec9d-48e4-93d5-b6f46965d84c",
  "toolUseResult": {
    "query": "\"iterative synthetic data\" detection depth multi-generation text 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KG7mwkV8iCmizMKWKSPpK7",
        "content": [
          {
            "title": "Synthetic Data Generation Using Large Language Models: Advances in Text and Code",
            "url": "https://arxiv.org/html/2503.14023v2"
          },
          {
            "title": "GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub",
            "url": "https://github.com/pengr/LLM-Synthetic-Data"
          },
          {
            "title": "A Lightweight Pipeline for Rewards-Guided Synthetic Text ...",
            "url": "https://proceedings.scipy.org/articles/hprh2773.pdf"
          },
          {
            "title": "Synthetic Text Generation for Training Large Language Models",
            "url": "https://openreview.net/pdf?id=mHySkOp46b"
          },
          {
            "title": "ORCHESTRATING SYNTHETIC DATA WITH REASONING",
            "url": "https://openreview.net/pdf?id=VOoeogZbMb"
          },
          {
            "title": "Designing synthetic datasets for the real world: Mechanism design and reasoning from first principles",
            "url": "https://research.google/blog/designing-synthetic-datasets-for-the-real-world-mechanism-design-and-reasoning-from-first-principles/"
          },
          {
            "title": "ARISE: Iterative Rule Induction and Synthetic Data Generation for Text Classification - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-naacl.359/"
          },
          {
            "title": "[2502.17607] Synthetic Text Generation for Training Large Language Models via Gradient Matching",
            "url": "https://arxiv.org/abs/2502.17607"
          },
          {
            "title": "What is Synthetic Data Generation (SDG)? | NVIDIA Glossary",
            "url": "https://www.nvidia.com/en-us/glossary/synthetic-data-generation/"
          },
          {
            "title": "Generative Models for Synthetic Data: A Deep Dive into the Gen AI Era | by Jay Vithlani | Dec, 2025 | Medium",
            "url": "https://medium.com/@jvithlani4/generative-models-for-synthetic-data-a-deep-dive-into-the-gen-ai-era-cbd5bcb77187"
          }
        ]
      },
      "I've performed the web search for \"iterative synthetic data detection depth multi-generation text 2025\". Here are the key findings:\n\n## Recent Research on Iterative Synthetic Data Generation\n\nLarge language models (LLMs) are transforming synthetic training data generation in both natural language and code domains, with key techniques including prompt-based generation, retrieval-augmented pipelines, and iterative self-refinement.\n\n### Multi-Generation and Iterative Approaches\n\nRecent frameworks employ reasoning-driven, recursive expansion processes where at each depth level, the system generates multiple candidate sub-categories that are evaluated, merged, and filtered by a critic model, building a dense, hierarchical taxonomy through iterative \"propose-and-refine\" loops.\n\nOne complete pipeline integrates all components into an iterative loop where in each subsequent iteration, new synthetic samples are generated and merged with the deduplicated dataset from the previous round, with the combined dataset then subjected to semantic deduplication to maintain high semantic diversity and quality standards.\n\n### Text Classification Approach\n\nARISE is a framework that combines synthetic data generation and automatic rule induction via bootstrapping to iteratively filter the generated rules and data.\n\n### Important Concerns with Multi-Generation\n\nIf you train a model on synthetic data, generate more data from it, then train again, quality degrades rapidly as the tails of the distribution disappear and the model converges to an average version of reality due to self-referential training amplifying biases with variance shrinking with each generation.\n\nThe search results show active research in 2025 on iterative synthetic data generation with various approaches to maintaining quality and diversity across multiple generations."
    ],
    "durationSeconds": 8.209849857000009
  },
  "sourceToolAssistantUUID": "e3d1e549-bb1b-4a99-a07b-ef5b71244173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 72 · 2026-05-18T09:58:02.755Z_

```json
{
  "parentUuid": "76a7575e-ec9d-48e4-93d5-b6f46965d84c",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a8aa6739-a260-4cc5-9972-8f23e3cc3e52",
  "timestamp": "2026-05-18T09:58:02.755Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 73 · 2026-05-18T09:58:06.113Z_

<details><summary>Logged reasoning block</summary>

```text
Let me search for a few more potentially missing references - specifically watermarking approaches for synthetic text provenance (which would be a relevant comparison), and any other work on ordinal/multi-class machine-generated text classification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8aa6739-a260-4cc5-9972-8f23e3cc3e52",
  "isSidechain": false,
  "requestId": "req_011Cb9qUg3s8H4fKQ59UFpHx",
  "type": "assistant",
  "uuid": "e23c3a18-b935-4e08-adb5-40ddc2202130",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lqj76j4ZyY5GQUXi63thSo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3045,
      "cache_read_input_tokens": 81452,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3045,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 81452,
          "cache_creation_input_tokens": 3045,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3045
          },
          "type": "message"
        }
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

_source line 74 · 2026-05-18T09:58:06.656Z_

搜索额外的可能遗漏引用方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e23c3a18-b935-4e08-adb5-40ddc2202130",
  "isSidechain": false,
  "requestId": "req_011Cb9qUg3s8H4fKQ59UFpHx",
  "type": "assistant",
  "uuid": "b1464866-7cd6-4542-94fe-b67a46b27e71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lqj76j4ZyY5GQUXi63thSo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3045,
      "cache_read_input_tokens": 81452,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3045,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 81452,
          "cache_creation_input_tokens": 3045,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3045
          },
          "type": "message"
        }
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

_source line 75 · 2026-05-18T09:58:07.635Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012MN99XbZiHsDgcpWdDEFTq`</summary>

```json
{
  "query": "watermarking LLM text provenance synthetic data detection 2024 2025 ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1464866-7cd6-4542-94fe-b67a46b27e71",
  "isSidechain": false,
  "requestId": "req_011Cb9qUg3s8H4fKQ59UFpHx",
  "type": "assistant",
  "uuid": "78b5e014-2415-46cd-88e1-68dbc1e45627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lqj76j4ZyY5GQUXi63thSo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3045,
      "cache_read_input_tokens": 81452,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3045,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 81452,
          "cache_creation_input_tokens": 3045,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3045
          },
          "type": "message"
        }
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

_source line 76 · 2026-05-18T09:58:08.046Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RA6DVSrybYyqfDU57mdpbx`</summary>

```json
{
  "query": "\"ordinal classification\" \"machine-generated text\" OR \"synthetic text\" depth generation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78b5e014-2415-46cd-88e1-68dbc1e45627",
  "isSidechain": false,
  "requestId": "req_011Cb9qUg3s8H4fKQ59UFpHx",
  "type": "assistant",
  "uuid": "ca1c73b7-f058-421f-9180-575f2d81918c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lqj76j4ZyY5GQUXi63thSo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3045,
      "cache_read_input_tokens": 81452,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3045,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 81452,
          "cache_creation_input_tokens": 3045,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3045
          },
          "type": "message"
        }
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

_source line 77 · 2026-05-18T09:58:15.160Z_

<details><summary>↩ Tool result · `toolu_01RA6DVSrybYyqfDU57mdpbx`</summary>

```text
Web search results for query: ""ordinal classification" "machine-generated text" OR "synthetic text" depth generation 2024 2025"

Links: [{"title":"Synthetic Data Generation Using Large Language Models: Advances in Text and Code","url":"https://arxiv.org/html/2503.14023v1"},{"title":"GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub","url":"https://github.com/pengr/LLM-Synthetic-Data"},{"title":"Synthetic Data Generation Using Large Language Models","url":"https://arxiv.org/pdf/2503.14023"},{"title":"Synthetic Data Generation Using Large Language Models ...","url":"https://aclanthology.org/2025.finnlp-1.7.pdf"},{"title":"Stress-testing Machine Generated Text Detection: Shifting Language Models Writing Style to Fool Detectors","url":"https://arxiv.org/html/2505.24523"},{"title":"Text Classification: How Machine Learning Is Revolutionizing Text Categorization","url":"https://www.mdpi.com/2078-2489/16/2/130"},{"title":"How to Generalize the Detection of AI-Generated Text","url":"https://aclanthology.org/2025.findings-emnlp.1388.pdf"},{"title":"On LLMs-Driven Synthetic Data Generation, Curation, and ...","url":"https://aclanthology.org/2024.findings-acl.658.pdf"},{"title":"A Comprehensive Dataset for Human vs. AI Generated Text Detection","url":"https://arxiv.org/html/2510.22874v1"},{"title":"Benchmarking AI Text Detection: Assessing Detectors ...","url":"https://aclanthology.org/2025.genaidetect-1.4.pdf"}]

I've performed a web search for your query. The results focus on synthetic text generation and detection rather than specifically on "ordinal classification" in the context of machine-generated text with "depth generation." Here's what I found:

## Key Findings:

**Synthetic Text Generation & LLMs (2024-2025)**

Large language models have unlocked new possibilities for generating synthetic training data by producing artificial but task-relevant examples that can augment or substitute for real-world datasets, with key techniques including prompt-based generation, retrieval-augmented pipelines, and iterative self-refinement.

**Machine-Generated Text Detection**

Most detectors struggle when applied to out-of-domain samples, with weaknesses attributed to reliance on superficial stylistic cues and sensitivity to variations in text complexity. Recent work in 2025 has focused on identifying linguistic properties leveraged by MGT detectors and using fine-tuning techniques to generate synthetic texts that resemble human-written texts.

**Text Classification with Synthetic Data (2024-2025)**

Methods are being used to enrich low-resource tasks like classification and question answering. Recent studies in 2024 have emphasized leveraging pre-trained language models, domain-specific adaptations, and innovative clustering techniques.

However, the search results don't specifically address "ordinal classification" or "depth generation" as combined concepts. If you're looking for more specific information about these particular aspects, you may need to provide additional context or search for more specialized terminology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca1c73b7-f058-421f-9180-575f2d81918c",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "9c157b46-fdbc-46f0-a5cc-49fa4919b2c5",
  "toolUseResult": {
    "query": "\"ordinal classification\" \"machine-generated text\" OR \"synthetic text\" depth generation 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_011VfE6SJUj1cKmFqYnZNHm3",
        "content": [
          {
            "title": "Synthetic Data Generation Using Large Language Models: Advances in Text and Code",
            "url": "https://arxiv.org/html/2503.14023v1"
          },
          {
            "title": "GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub",
            "url": "https://github.com/pengr/LLM-Synthetic-Data"
          },
          {
            "title": "Synthetic Data Generation Using Large Language Models",
            "url": "https://arxiv.org/pdf/2503.14023"
          },
          {
            "title": "Synthetic Data Generation Using Large Language Models ...",
            "url": "https://aclanthology.org/2025.finnlp-1.7.pdf"
          },
          {
            "title": "Stress-testing Machine Generated Text Detection: Shifting Language Models Writing Style to Fool Detectors",
            "url": "https://arxiv.org/html/2505.24523"
          },
          {
            "title": "Text Classification: How Machine Learning Is Revolutionizing Text Categorization",
            "url": "https://www.mdpi.com/2078-2489/16/2/130"
          },
          {
            "title": "How to Generalize the Detection of AI-Generated Text",
            "url": "https://aclanthology.org/2025.findings-emnlp.1388.pdf"
          },
          {
            "title": "On LLMs-Driven Synthetic Data Generation, Curation, and ...",
            "url": "https://aclanthology.org/2024.findings-acl.658.pdf"
          },
          {
            "title": "A Comprehensive Dataset for Human vs. AI Generated Text Detection",
            "url": "https://arxiv.org/html/2510.22874v1"
          },
          {
            "title": "Benchmarking AI Text Detection: Assessing Detectors ...",
            "url": "https://aclanthology.org/2025.genaidetect-1.4.pdf"
          }
        ]
      },
      "I've performed a web search for your query. The results focus on synthetic text generation and detection rather than specifically on \"ordinal classification\" in the context of machine-generated text with \"depth generation.\" Here's what I found:\n\n## Key Findings:\n\n**Synthetic Text Generation & LLMs (2024-2025)**\n\nLarge language models have unlocked new possibilities for generating synthetic training data by producing artificial but task-relevant examples that can augment or substitute for real-world datasets, with key techniques including prompt-based generation, retrieval-augmented pipelines, and iterative self-refinement.\n\n**Machine-Generated Text Detection**\n\nMost detectors struggle when applied to out-of-domain samples, with weaknesses attributed to reliance on superficial stylistic cues and sensitivity to variations in text complexity. Recent work in 2025 has focused on identifying linguistic properties leveraged by MGT detectors and using fine-tuning techniques to generate synthetic texts that resemble human-written texts.\n\n**Text Classification with Synthetic Data (2024-2025)**\n\nMethods are being used to enrich low-resource tasks like classification and question answering. Recent studies in 2024 have emphasized leveraging pre-trained language models, domain-specific adaptations, and innovative clustering techniques.\n\nHowever, the search results don't specifically address \"ordinal classification\" or \"depth generation\" as combined concepts. If you're looking for more specific information about these particular aspects, you may need to provide additional context or search for more specialized terminology."
    ],
    "durationSeconds": 7.109843938999998
  },
  "sourceToolAssistantUUID": "ca1c73b7-f058-421f-9180-575f2d81918c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 78 · 2026-05-18T09:58:19.382Z_

<details><summary>↩ Tool result · `toolu_012MN99XbZiHsDgcpWdDEFTq`</summary>

```text
Web search results for query: "watermarking LLM text provenance synthetic data detection 2024 2025 ACL EMNLP"

Links: [{"title":"EMNLP 2024 Main Conference Waterfall: Scalable Framework for Robust Text Watermarking and Provenance for LLMs","url":"https://arxiv.org/html/2407.04411v2"},{"title":"arXiv:2411.05091v2 [cs.LG] 20 Jun 2025 1 Watermarking Language Models through","url":"https://www.arxiv.org/pdf/2411.05091"},{"title":"GitHub - THU-BPM/MarkLLM: [EMNLP 2024 Demo] MarkLLM: An Open-Source Toolkit for LLM Watermarking · GitHub","url":"https://github.com/THU-BPM/MarkLLM"},{"title":"Evaluating LLM Watermarking Methods for Medical Texts","url":"https://aclanthology.org/2025.findings-emnlp.818.pdf"},{"title":"Securing Large Language Models: A Survey of Watermarking and Fingerprinting Techniques | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3773028"},{"title":"MARKLLM: An Open-Source Toolkit for LLM Watermarking","url":"https://aclanthology.org/2024.emnlp-demo.7.pdf"},{"title":"WASA: WAtermark-based Source Attribution for Large ...","url":"https://aclanthology.org/2025.findings-acl.1219.pdf"},{"title":"LLM Watermarking for Copyright Protection and Content Integrity | Blog | Ziyang Zeng","url":"https://ziyang.io/blog/2025-llm-watermarking-for-copyright-and-integrity"},{"title":"Where Am I From? Identifying Origin of LLM-generated ...","url":"https://aclanthology.org/2024.emnlp-main.681.pdf"},{"title":"SimMark: A Robust Sentence-Level Similarity-Based ...","url":"https://aclanthology.org/2025.emnlp-main.1567.pdf"}]

Based on the search results, here are the key findings on watermarking, LLM text provenance, and synthetic data detection from recent 2024-2025 ACL/EMNLP research:

## Major Research Contributions

**Text Provenance & Data Attribution:**

Waterfall, presented at EMNLP 2024, demonstrates that watermarks of LLM training data can be detected in LLM output, allowing for detection of unauthorized use of data for LLM training and potentially enabling model-centric watermarking of open-sourced LLMs. Waterfall comprises several key innovations, such as being the first to use LLM as paraphrasers for watermarking along with a novel combination of techniques that are surprisingly effective in achieving robust verifiability and scalability.

WASA (WAtermark-based Source Attribution) framework produces synthetic texts with embedded watermarks that allow for effective source attribution, accepted at ACL 2025 Findings.

**Toolkits & Open-Source Resources:**

MarkLLM: An Open-Source Toolkit for LLM Watermarking was accepted by EMNLP 2024 Demo. This toolkit implements multiple watermarking families and detection methods.

**Watermark Robustness & Cross-lingual Consistency:**

Multiple 2024-2025 papers address robustness questions, including "Can LLM Watermarks Robustly Prevent Unauthorized Knowledge Distillation?" (ACL 2025 Main) and "Can Watermarks Survive Translation? On the Cross-lingual Consistency of Text Watermark for Large Language Models" (ACL 2024 Main).

**Watermark Attacks & Vulnerabilities:**

The Self-Information Rewrite Attack (SIRA) by Cheng et al. (2025) demonstrates how understanding watermark design principles can be exploited to create an effective removal attack.

**Sentence-Level Watermarking:**

Recent work like SimMark enables detection of watermarked text via a soft-z-test even under paraphrase attacks, addressing robustness against text transformations.

These contributions collectively advance the field of LLM watermarking for both copyright protection and synthetic content detection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78b5e014-2415-46cd-88e1-68dbc1e45627",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "4f3c8293-79db-4d35-af83-583f5eddfe5d",
  "toolUseResult": {
    "query": "watermarking LLM text provenance synthetic data detection 2024 2025 ACL EMNLP",
    "results": [
      {
        "tool_use_id": "srvtoolu_019wLpa28sMjZK3WCcuuD2rY",
        "content": [
          {
            "title": "EMNLP 2024 Main Conference Waterfall: Scalable Framework for Robust Text Watermarking and Provenance for LLMs",
            "url": "https://arxiv.org/html/2407.04411v2"
          },
          {
            "title": "arXiv:2411.05091v2 [cs.LG] 20 Jun 2025 1 Watermarking Language Models through",
            "url": "https://www.arxiv.org/pdf/2411.05091"
          },
          {
            "title": "GitHub - THU-BPM/MarkLLM: [EMNLP 2024 Demo] MarkLLM: An Open-Source Toolkit for LLM Watermarking · GitHub",
            "url": "https://github.com/THU-BPM/MarkLLM"
          },
          {
            "title": "Evaluating LLM Watermarking Methods for Medical Texts",
            "url": "https://aclanthology.org/2025.findings-emnlp.818.pdf"
          },
          {
            "title": "Securing Large Language Models: A Survey of Watermarking and Fingerprinting Techniques | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3773028"
          },
          {
            "title": "MARKLLM: An Open-Source Toolkit for LLM Watermarking",
            "url": "https://aclanthology.org/2024.emnlp-demo.7.pdf"
          },
          {
            "title": "WASA: WAtermark-based Source Attribution for Large ...",
            "url": "https://aclanthology.org/2025.findings-acl.1219.pdf"
          },
          {
            "title": "LLM Watermarking for Copyright Protection and Content Integrity | Blog | Ziyang Zeng",
            "url": "https://ziyang.io/blog/2025-llm-watermarking-for-copyright-and-integrity"
          },
          {
            "title": "Where Am I From? Identifying Origin of LLM-generated ...",
            "url": "https://aclanthology.org/2024.emnlp-main.681.pdf"
          },
          {
            "title": "SimMark: A Robust Sentence-Level Similarity-Based ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1567.pdf"
          }
        ]
      },
      "Based on the search results, here are the key findings on watermarking, LLM text provenance, and synthetic data detection from recent 2024-2025 ACL/EMNLP research:\n\n## Major Research Contributions\n\n**Text Provenance & Data Attribution:**\n\nWaterfall, presented at EMNLP 2024, demonstrates that watermarks of LLM training data can be detected in LLM output, allowing for detection of unauthorized use of data for LLM training and potentially enabling model-centric watermarking of open-sourced LLMs. Waterfall comprises several key innovations, such as being the first to use LLM as paraphrasers for watermarking along with a novel combination of techniques that are surprisingly effective in achieving robust verifiability and scalability.\n\nWASA (WAtermark-based Source Attribution) framework produces synthetic texts with embedded watermarks that allow for effective source attribution, accepted at ACL 2025 Findings.\n\n**Toolkits & Open-Source Resources:**\n\nMarkLLM: An Open-Source Toolkit for LLM Watermarking was accepted by EMNLP 2024 Demo. This toolkit implements multiple watermarking families and detection methods.\n\n**Watermark Robustness & Cross-lingual Consistency:**\n\nMultiple 2024-2025 papers address robustness questions, including \"Can LLM Watermarks Robustly Prevent Unauthorized Knowledge Distillation?\" (ACL 2025 Main) and \"Can Watermarks Survive Translation? On the Cross-lingual Consistency of Text Watermark for Large Language Models\" (ACL 2024 Main).\n\n**Watermark Attacks & Vulnerabilities:**\n\nThe Self-Information Rewrite Attack (SIRA) by Cheng et al. (2025) demonstrates how understanding watermark design principles can be exploited to create an effective removal attack.\n\n**Sentence-Level Watermarking:**\n\nRecent work like SimMark enables detection of watermarked text via a soft-z-test even under paraphrase attacks, addressing robustness against text transformations.\n\nThese contributions collectively advance the field of LLM watermarking for both copyright protection and synthetic content detection."
    ],
    "durationSeconds": 11.744160451999996
  },
  "sourceToolAssistantUUID": "78b5e014-2415-46cd-88e1-68dbc1e45627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 79 · 2026-05-18T09:59:29.437Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the paper and the landscape. Let me also check if there are reference files to count total references.

Key observations from my thorough reading:

**Reference check results:**
- 34 total bib entries, all cited (no orphans, no missing)
- 28 verified online, 4 not found (mitchell2023detectgpt, basani2026diveye, zawalski2026codec, hans2024binoculars - these are likely real papers that just didn't match well in OpenAlex), 2 mismatches (alemohammad2024selfconsuming first author, mehta2025beyond first author)


- The "not found" papers are known real papers (DetectGPT, Binoculars, etc.) - likely just OpenAlex matching issues

Now let me compile my thorough review. The paper introduces generational depth estimation for recursive synthetic text, using a classifier trained on 15 statistical features to measure K* (the maximum depth where adjacent generations remain distinguishable). Their findings show K* varies by domain—web text reaches K*=2, arXiv reaches K*=3, and Wikipedia only K*=1—validated through cross-model transfer, cross-scorer validation, and downstream filtering applications.

The framing of generational depth as a distinct problem is genuinely novel, and the K* concept provides an elegant, well-defined boundary for measuring discrimination limits. The domain-specific ordering they discover (arXiv > C4 > Wikipedia) has nice theoretical grounding in structural complexity, and their experimental scope is impressively broad across 9 models, 5 families, 3 domains, and 4 decoding strategies.

However, the technical novelty is limited—the approach boils down to extracting hand-crafted statistical features and training a standard LightGBM classifier with an OBD wrapper, which is established methodology from Frank & Hall (2001). There's no new model architecture, training objective, or theoretical contribution underlying the method itself.

The K*=2 finding for web text is really a negative result reframed as a positive one. It essentially shows that after one generation of synthetic text, further generations become indistinguishable, which severely limits practical utility beyond binary detection. While the paper acknowledges this "one-wash laundering" effect, it doesn't fully reckon with what that means for the method's real-world applicability.

The connection to Drayson et al. (2025) also feels underdeveloped—they already did binary MGT detection with SIR filtering, and this work claims to provide post-hoc grounding for that approach, but the relationship and incremental value aren't clearly articulated.

The extension from binary to ordinal classification is conceptually straightforward but methodologically thin. The approach just decomposes the ordinal problem into pairwise binary classifiers rather than introducing any ordinal-specific innovations. Additionally, the related work section is sparse at 34 references and notably omits watermarking-based approaches for synthetic text detection.

The experimental validation is also narrow—it relies on a single downstream task across two models, with Pythia showing a near-chance MMLU baseline that undermines the filtering results' credibility.  The dose-response analysis in the appendix reveals minimal effect sizes at realistic contamination levels (10-50%), and there's no comparison against watermarking or neural detector baselines.

Now I'm scanning the tex files for writing quality markers. The introduction uses hyphens rather than em-dashes, and the prose is clear and professional overall, though the Discussion section is quite dense with many labeled paragraphs. The authors do anticipate potential objections around threshold sensitivity and confounds, which strengthens the argument.

The writing doesn't show excessive em-dashes or the most obvious AI patterns, though some sentences in the abstract run quite long. The paper's main issue is scope creep—it's simultaneously a measurement study, a detection paper, and a data curation paper, which dilutes the core contribution. Section 5 on filtering feels like an afterthought trying to justify the measurement work, but the practical utility is limited. The abstract is also packed with too many specifics (model counts, parameter ranges, statistical thresholds) that make it dense rather than compelling.

Looking at the contributions, the first one—empirical measurement of K*—is genuinely novel and well-supported by the core sections, along with the domain ordering invariance finding and generator-independent features. The filtering validation mentioned in the introduction isn't formally listed as a contribution but appears in Section 5. The paper uses the correct ACL review format and maintains anonymity, though the "first empirical measurement" claim hinges on how narrowly the problem is defined.

Now I'm examining the paper more carefully for term definitions and potential AI writing patterns. I notice the LaTeX uses hyphenated compounds like "one-wash laundering" rather than em-dashes, so I need to look for actual em-dash usage to check for stylistic markers. Thinking through what I've observed so far, the main strengths are the novel problem formulation around generational depth estimation and K*, plus the comprehensive experimental design spanning multiple models and families with thorough ablations.

The statistical rigor with bootstrap confidence intervals and permutation tests is solid, and the honest discussion of limitations is refreshing. The finding that domain ordering matters (arXiv > C4 > Wikipedia) provides useful insights, and the cross-scorer and cross-model validation strengthens the claims. On the weakness side, the technical novelty is limited since it's essentially standard features fed into an off-the-shelf classifier, and K*=2 severely constrains practical applicability beyond binary detection. The filtering effect sizes are disappointingly small—less than a percentage point difference on MMLU—and the related work section feels sparse at 34 references, notably missing watermarking literature and some recent data collapse papers. There's also some conceptual murkiness about whether the paper is primarily about measurement, detection, or curation, and while the authors show robustness across thresholds, the dependence on θ=0.60 remains a potential limitation.

Now I'm checking whether the paper includes the Responsible NLP Research Checklist that ACL ARR requires, and I'm also verifying the reference count against typical EMNLP standards. At 34 entries, this is on the lower end—most EMNLP papers cite 30-50+ sources. Looking at what's missing, there's no mention of seminal watermarking work like Kirchenbauer et al.'s 2023 paper, no engagement with data quality benchmarks like FineWeb or Dolma, and some key detection papers appear to be absent from the citations.

Checking the main.tex file, I don't see a checklist included, which could be a format compliance issue for ARR submission. On the excitement dimension, while the problem formulation is novel and the experimental work is thorough, the practical impact is constrained by the K*=2 limitation, and the domain ordering findings are fairly intuitive. My overall assessment lands around 3.0-3.5—the work has merit in its novel framing and rigorous evaluation, but the limited technical novelty and practical constraints keep it from being a strong accept.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f3c8293-79db-4d35-af83-583f5eddfe5d",
  "isSidechain": false,
  "requestId": "req_011Cb9qVuBBHWCc3iQRVbxfp",
  "type": "assistant",
  "uuid": "a4801671-5754-4f71-abeb-1b4587d11ba4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdJnU5oGZfkjguWsifvSjU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 828,
      "cache_creation_input_tokens": 1331,
      "cache_read_input_tokens": 84497,
      "output_tokens": 3220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 828,
          "output_tokens": 3220,
          "cache_read_input_tokens": 84497,
          "cache_creation_input_tokens": 1331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1331
          },
          "type": "message"
        }
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

_source line 80 · 2026-05-18T09:59:29.480Z_

检查 AI 写作痕迹和格式问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4801671-5754-4f71-abeb-1b4587d11ba4",
  "isSidechain": false,
  "requestId": "req_011Cb9qVuBBHWCc3iQRVbxfp",
  "type": "assistant",
  "uuid": "d637acea-b8ea-4396-b453-91c535a3eabc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdJnU5oGZfkjguWsifvSjU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 828,
      "cache_creation_input_tokens": 1331,
      "cache_read_input_tokens": 84497,
      "output_tokens": 3220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 828,
          "output_tokens": 3220,
          "cache_read_input_tokens": 84497,
          "cache_creation_input_tokens": 1331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1331
          },
          "type": "message"
        }
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

_source line 81 · 2026-05-18T09:59:31.397Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01V8oReowYrwSScgikThDvnP`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d637acea-b8ea-4396-b453-91c535a3eabc",
  "isSidechain": false,
  "requestId": "req_011Cb9qVuBBHWCc3iQRVbxfp",
  "type": "assistant",
  "uuid": "91432b2b-bcb6-4b5b-af6c-58f5ea627342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdJnU5oGZfkjguWsifvSjU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 828,
      "cache_creation_input_tokens": 1331,
      "cache_read_input_tokens": 84497,
      "output_tokens": 3220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 828,
          "output_tokens": 3220,
          "cache_read_input_tokens": 84497,
          "cache_creation_input_tokens": 1331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1331
          },
          "type": "message"
        }
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

_source line 82 · 2026-05-18T09:59:34.843Z_

<details><summary>↩ Tool result · `toolu_01B67GW9eFp9bYacGMgpQJ4W`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90d34c2b-fd5b-4da7-9e7c-b0ba693ee521",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "caec3426-5a7f-4cb0-92c2-6925ff254da1",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "90d34c2b-fd5b-4da7-9e7c-b0ba693ee521",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-18T09:59:31.416Z_

<details><summary>↩ Tool result · `toolu_01V8oReowYrwSScgikThDvnP`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:1:% EMNLP 2026 Main — ARR May 2026
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91432b2b-bcb6-4b5b-af6c-58f5ea627342",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "bd8f1568-d257-4f00-a9e5-cd1bc044fb75",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:1:% EMNLP 2026 Main — ARR May 2026",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "91432b2b-bcb6-4b5b-af6c-58f5ea627342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-18T09:59:32.367Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01MCJMJrBJdYxpbuL6xHDCYz`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd8f1568-d257-4f00-a9e5-cd1bc044fb75",
  "isSidechain": false,
  "requestId": "req_011Cb9qVuBBHWCc3iQRVbxfp",
  "type": "assistant",
  "uuid": "3b43b2fe-73d0-41fb-87f3-bc368d2fdec2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdJnU5oGZfkjguWsifvSjU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 828,
      "cache_creation_input_tokens": 1331,
      "cache_read_input_tokens": 84497,
      "output_tokens": 3220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 828,
          "output_tokens": 3220,
          "cache_read_input_tokens": 84497,
          "cache_creation_input_tokens": 1331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1331
          },
          "type": "message"
        }
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

_source line 85 · 2026-05-18T09:59:32.384Z_

<details><summary>↩ Tool result · `toolu_01MCJMJrBJdYxpbuL6xHDCYz`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b43b2fe-73d0-41fb-87f3-bc368d2fdec2",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "405f1ba4-7cdf-4124-9163-a034afc3a176",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "3b43b2fe-73d0-41fb-87f3-bc368d2fdec2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-18T09:59:33.820Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01JUR19L7mwvN1H9gw7H3vgu`</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
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
  "parentUuid": "405f1ba4-7cdf-4124-9163-a034afc3a176",
  "isSidechain": false,
  "requestId": "req_011Cb9qVuBBHWCc3iQRVbxfp",
  "type": "assistant",
  "uuid": "c3621160-5f1e-44ba-92b4-06aaa31a0b10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdJnU5oGZfkjguWsifvSjU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 828,
      "cache_creation_input_tokens": 1331,
      "cache_read_input_tokens": 84497,
      "output_tokens": 3220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 828,
          "output_tokens": 3220,
          "cache_read_input_tokens": 84497,
          "cache_creation_input_tokens": 1331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1331
          },
          "type": "message"
        }
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

_source line 87 · 2026-05-18T09:59:33.830Z_

<details><summary>↩ Tool result · `toolu_01JUR19L7mwvN1H9gw7H3vgu`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:5:Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:6:In the context of diffusion models, \citet{shi2025collapse} trace a generalization-to-memorization transition under iterative synthetic training.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:18:DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling, a special case when $\Kstar = 1$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:20:\paragraph{Ordinal classification and probing.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:21:Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:39:The elevated signal arises from cumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) rather than text-intrinsic degradation; prompt-chain $\Kempirical$ is the operationally relevant boundary for data curation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:96:\emph{Graduated filtering.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:277:Formulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, explaining the elevated $\Kempirical{=}3$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:80:Generational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:79:Qwen-rewrite $\Kempirical$ remains 2 under all scorers; Qwen-continuation drops to 1 (1v2 $\auc$: $0.6112 \to 0.5923/0.5858$), consistent with its marginality under self-scoring.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:129:The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4): formulaic features (LaTeX formatting, citation patterns, mathematical notation) degrade slowly under autoregressive generation and supply persistent depth signal across four architecture families and 1.4B--8B parameters.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:141:Neither model scale (1B--14B), architecture family, nor decoding strategy alters this ordering, establishing source-domain structural complexity as the primary determinant of $\Kempirical$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:47:$\Kempirical{=}2$ for web text is not a negative result but a precise measurement: it rules out both $\Kempirical{=}1$ (no depth signal beyond 0v1) and $\Kempirical{\geq}3$ (graduated tracking feasible), while arXiv $\Kempirical{=}3$ confirms the framework captures real domain-level variation rather than a methodological ceiling.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:54:Mixed-domain corpora thus require domain-stratified filtering, and $\Kempirical{=}2$ provides post-hoc grounding for the binary approach of \citet{drayson2025} (segment-length sensitivity in Table~\ref{tab:s11_length_ablation}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:24:\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:228:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:477:  \caption{Scorer sensitivity: $\Kempirical$ under self-scoring vs.\ cross-scoring. Self-scorer uses the generator's own model family for feature extraction; cross-scorer uses alternative models (Pythia-1.4B, OLMo-1B). $\Kempirical$ agreement across scorer conditions indicates the boundary is governed by the generation process. Cross-scoring reduces $\Kempirical$ only for the most marginal self-scorer condition (Qwen-continuation).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex:10:This gap cuts across multiple communities: binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}), membership inference~\cite{zawalski2026codec} addresses a different question, and the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3621160-5f1e-44ba-92b4-06aaa31a0b10",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "b9cea20e-1906-4453-a5d9-918c36396fea",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:5:Iterative training on model outputs causes tail-distribution degradation~\\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model}.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:6:In the context of diffusion models, \\citet{shi2025collapse} trace a generalization-to-memorization transition under iterative synthetic training.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:18:DSIR~\\cite{xie2023dsir}, D4~\\cite{tirumala2023d4}, and DoReMi~\\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\\cite{drayson2025} combined binary detection with importance resampling, a special case when $\\Kstar = 1$.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:20:\\paragraph{Ordinal classification and probing.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:21:Our OBD classifier follows Frank \\& Hall's~\\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:39:The elevated signal arises from cumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) rather than text-intrinsic degradation; prompt-chain $\\Kempirical$ is the operationally relevant boundary for data curation.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:96:\\emph{Graduated filtering.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:277:Formulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, explaining the elevated $\\Kempirical{=}3$.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:80:Generational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:79:Qwen-rewrite $\\Kempirical$ remains 2 under all scorers; Qwen-continuation drops to 1 (1v2 $\\auc$: $0.6112 \\to 0.5923/0.5858$), consistent with its marginality under self-scoring.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:129:The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\\ ${\\sim}0.01$ for C4): formulaic features (LaTeX formatting, citation patterns, mathematical notation) degrade slowly under autoregressive generation and supply persistent depth signal across four architecture families and 1.4B--8B parameters.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:141:Neither model scale (1B--14B), architecture family, nor decoding strategy alters this ordering, establishing source-domain structural complexity as the primary determinant of $\\Kempirical$.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:47:$\\Kempirical{=}2$ for web text is not a negative result but a precise measurement: it rules out both $\\Kempirical{=}1$ (no depth signal beyond 0v1) and $\\Kempirical{\\geq}3$ (graduated tracking feasible), while arXiv $\\Kempirical{=}3$ confirms the framework captures real domain-level variation rather than a methodological ceiling.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:54:Mixed-domain corpora thus require domain-stratified filtering, and $\\Kempirical{=}2$ provides post-hoc grounding for the binary approach of \\citet{drayson2025} (segment-length sensitivity in Table~\\ref{tab:s11_length_ablation}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:24:\\caption{Top-3 features by single-feature $\\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:228:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:477:  \\caption{Scorer sensitivity: $\\Kempirical$ under self-scoring vs.\\ cross-scoring. Self-scorer uses the generator's own model family for feature extraction; cross-scorer uses alternative models (Pythia-1.4B, OLMo-1B). $\\Kempirical$ agreement across scorer conditions indicates the boundary is governed by the generation process. Cross-scoring reduces $\\Kempirical$ only for the most marginal self-scorer condition (Qwen-continuation).}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex:10:This gap cuts across multiple communities: binary detectors~\\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\\ref{sec:binary_confidence}), membership inference~\\cite{zawalski2026codec} addresses a different question, and the model collapse literature~\\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool.",
    "numLines": 18
  },
  "sourceToolAssistantUUID": "c3621160-5f1e-44ba-92b4-06aaa31a0b10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-18T09:59:34.831Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01B67GW9eFp9bYacGMgpQJ4W`</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally|Notably|It is worth noting",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9cea20e-1906-4453-a5d9-918c36396fea",
  "isSidechain": false,
  "requestId": "req_011Cb9qVuBBHWCc3iQRVbxfp",
  "type": "assistant",
  "uuid": "90d34c2b-fd5b-4da7-9e7c-b0ba693ee521",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdJnU5oGZfkjguWsifvSjU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 828,
      "cache_creation_input_tokens": 1331,
      "cache_read_input_tokens": 84497,
      "output_tokens": 3220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 828,
          "output_tokens": 3220,
          "cache_read_input_tokens": 84497,
          "cache_creation_input_tokens": 1331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1331
          },
          "type": "message"
        }
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

_source line 89_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性**  ### Venue 信息 - **目标**: EMNLP 2026（ARR May 2026 cycle） - **Deadline**: 2026-05-25 - **格式**: ACL 双栏模板，`\\usepackage[review]{acl}`，Long…",
  "leafUuid": "caec3426-5a7f-4cb0-92c2-6925ff254da1",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Runtime record

_source line 90_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on generational depth contamination detection",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Assistant

_source line 91 · 2026-05-18T09:59:40.176Z_

<details><summary>Logged reasoning block</summary>

```text
Good findings:
- Only 1 em-dash found (in a comment line: `% EMNLP 2026 Main — ARR May 2026`), not in paper content.
- No explanatory en-dashes.
- No "Furthermore/Moreover/Additionally/Notably" usage.
- Some -ing patterns but mostly legitimate usage (not trailing -ing phrases).

The writing is clean of AI markers. 

Now let me also check for the ARR Responsible NLP Research Checklist. Let me search for it in the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caec3426-5a7f-4cb0-92c2-6925ff254da1",
  "isSidechain": false,
  "requestId": "req_011Cb9qbTrqFvb72wa5qsNzV",
  "type": "assistant",
  "uuid": "ff4b1d8b-c2ae-4047-99b4-86715aae669c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVLPVxpF5jURBeC9K5m7Hz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6071,
      "cache_read_input_tokens": 85828,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 376,
          "cache_read_input_tokens": 85828,
          "cache_creation_input_tokens": 6071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6071
          },
          "type": "message"
        }
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

_source line 92 · 2026-05-18T09:59:40.665Z_

检查是否包含 Responsible NLP Research Checklist。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff4b1d8b-c2ae-4047-99b4-86715aae669c",
  "isSidechain": false,
  "requestId": "req_011Cb9qbTrqFvb72wa5qsNzV",
  "type": "assistant",
  "uuid": "8f8b6a01-7fe3-49ce-8885-9b01a38b75f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVLPVxpF5jURBeC9K5m7Hz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6071,
      "cache_read_input_tokens": 85828,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 376,
          "cache_read_input_tokens": 85828,
          "cache_creation_input_tokens": 6071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6071
          },
          "type": "message"
        }
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

_source line 93 · 2026-05-18T09:59:41.648Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01HbZFFjeaCsvfWWJL2WXpbK`</summary>

```json
{
  "pattern": "checklist|Checklist|responsible|Responsible",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f8b6a01-7fe3-49ce-8885-9b01a38b75f6",
  "isSidechain": false,
  "requestId": "req_011Cb9qbTrqFvb72wa5qsNzV",
  "type": "assistant",
  "uuid": "ddcdb5de-cdea-4e29-b3db-8de6f8e05f66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVLPVxpF5jURBeC9K5m7Hz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6071,
      "cache_read_input_tokens": 85828,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 376,
          "cache_read_input_tokens": 85828,
          "cache_creation_input_tokens": 6071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6071
          },
          "type": "message"
        }
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

_source line 94 · 2026-05-18T09:59:42.170Z_

<details><summary>↩ Tool result · `toolu_01FNCCJMmXG3iL5wjqwmTDBt`</summary>

```text
1	% === References for gen-depth-contamination ===
2	% Source: literature_map.yaml — verified 2026-05-15
3	
4	% === Must-Cite ===
5	
6	@inproceedings{drayson2025,
7	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
8	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
9	  booktitle={Proceedings of EMNLP},
10	  year={2025},
11	  url={https://arxiv.org/abs/2502.15654}
12	}
13	
14	@inproceedings{schaeffer2025position,
15	  title={Position: Model Collapse Does Not Mean What You Think},
16	  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},
17	  booktitle={Proceedings of ICML},
18	  year={2025},
19	  url={https://arxiv.org/abs/2503.03150}
20	}
21	
22	@inproceedings{kazdan2025collapse,
23	  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},
24	  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},
25	  booktitle={Proceedings of ICML},
26	  year={2025},
27	  url={https://arxiv.org/abs/2410.16713}
28	}
29	
30	@inproceedings{mitchell2023detectgpt,
31	  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
32	  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
33	  booktitle={Proceedings of ICML},
34	  year={2023}
35	}
36	
37	% === Should-Cite ===
38	
39	@article{basani2026diveye,
40	  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},
41	  author={Basani, Advik Raj and Chen, Pin-Yu},
42	  journal={Transactions on Machine Learning Research},
43	  issn={2835-8856},
44	  year={2026},
45	  url={https://arxiv.org/abs/2509.18880}
46	}
47	
48	@inproceedings{zawalski2026codec,
49	  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},
50	  author={Zawalski, Micha{\l} and Boubdir, Meriem and Ba{\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},
51	  booktitle={Proceedings of ICLR},
52	  year={2026},
53	  url={https://arxiv.org/abs/2510.27055}
54	}
55	
56	@inproceedings{zhang2024minkpp,
57	  title={Min-{K}\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
58	  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},
59	  booktitle={Proceedings of EMNLP},
60	  year={2024}
61	}
62	
63	@article{shumailov2024collapse,
64	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
65	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
66	  journal={Nature},
67	  volume={631},
68	  pages={755--759},
69	  year={2024}
70	}
71	
72	@inproceedings{alemohammad2024selfconsuming,
73	  title={Self-Consuming Generative Models Go {MAD}},
74	  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
75	  booktitle={Proceedings of ICLR},
76	  year={2024}
77	}
78	
79	@inproceedings{dohmatob2024model,
80	  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},
81	  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},
82	  booktitle={Proceedings of ICML},
83	  year={2024}
84	}
85	
86	@inproceedings{xie2023dsir,
87	  title={Data Selection for Language Models via Importance Resampling},
88	  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
89	  booktitle={Advances in Neural Information Processing Systems},
90	  year={2023}
91	}
92	
93	@inproceedings{tirumala2023d4,
94	  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},
95	  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},
96	  booktitle={Advances in Neural Information Processing Systems},
97	  year={2023}
98	}
99	
100	@inproceedings{xie2023doremi,
101	  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},
102	  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},
103	  booktitle={Advances in Neural Information Processing Systems},
104	  year={2023}
105	}
106	
107	@inproceedings{hans2024binoculars,
108	  title={Spotting {LLMs} With Binoculars},
109	  author={Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
110	  booktitle={Proceedings of ICML},
111	  year={2024}
112	}
113	
114	% === Probing Classifiers ===
115	
116	@inproceedings{alain2017understanding,
117	  title={Understanding Intermediate Layers Using Linear Classifier Probes},
118	  author={Alain, Guillaume and Bengio, Yoshua},
119	  booktitle={ICLR Workshop},
120	  year={2017}
121	}
122	
123	@article{belinkov2022probing,
124	  title={Probing Classifiers: Promises, Shortcomings, and Advances},
125	  author={Belinkov, Yonatan},
126	  journal={Computational Linguistics},
127	  volume={48},
128	  number={1},
129	  pages={207--219},
130	  year={2022}
131	}
132	
133	% === Model Collapse Avoidability ===
134	
135	@inproceedings{bao2024fast,
136	  title={{Fast-DetectGPT}: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature},
137	  author={Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
138	  booktitle={Proceedings of ICLR},
139	  year={2024},
140	  url={https://arxiv.org/abs/2310.05130}
141	}
142	
143	@inproceedings{frank2001ordinal,
144	  title={A Simple Approach to Ordinal Classification},
145	  author={Frank, Eibe and Hall, Mark},
146	  booktitle={Proceedings of ECML},
147	  pages={145--156},
148	  year={2001}
149	}
150	
151	% === Beyond-Binary Detection ===
152	
153	@inproceedings{cheng2025beyond,
154	  title={Beyond Binary: Towards Fine-Grained {LLM}-Generated Text Detection via Role Recognition and Involvement Measurement},
155	  author={Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
156	  booktitle={Proceedings of the ACM Web Conference (WWW)},
157	  year={2025},
158	  url={https://arxiv.org/abs/2410.14259}
159	}
160	
161	@article{mehta2025beyond,
162	  title={Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models},
163	  author={Mehta, Sushant},
164	  journal={arXiv preprint arXiv:2511.17602},
165	  year={2025},
166	  url={https://arxiv.org/abs/2511.17602}
167	}
168	
169	% === AI-Generated Content Prevalence ===
170	
171	@inproceedings{sun2025aigt,
172	  title={Are We in the {AI}-Generated Text World Already? Quantifying and Monitoring {AIGT} on Social Media},
173	  author={Sun, Zhen and Zhang, Zongmin and Shen, Xinyue and Zhang, Ziyi and Liu, Yule and Backes, Michael and Zhang, Yang and He, Xinlei},
174	  booktitle={Proceedings of ACL},
175	  year={2025},
176	  url={https://arxiv.org/abs/2412.18148}
177	}
178	
179	@article{spennemann2025quantifying,
180	  title={Delving into: the Quantification of {AI}-Generated Content on the Internet (Synthetic Data)},
181	  author={Spennemann, Dirk H. R.},
182	  journal={arXiv preprint arXiv:2504.08755},
183	  year={2025},
184	  url={https://arxiv.org/abs/2504.08755}
185	}
186	
187	% === New entries (added 2026-05-16, Round 4 reviewer) ===
188	
189	@inproceedings{dohmatob2025strong,
190	  title={Strong Model Collapse},
191	  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
192	  booktitle={Proceedings of ICLR},
193	  year={2025},
194	  url={https://arxiv.org/abs/2410.04840}
195	}
196	
197	@inproceedings{wang2024semeval,
198	  title={{SemEval}-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection},
199	  author={Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas},
200	  booktitle={Proceedings of SemEval},
201	  year={2024},
202	  url={https://arxiv.org/abs/2404.14183}
203	}
204	
205	@inproceedings{gerstgrasser2024model,
206	  title={Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data},
207	  author={Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
208	  booktitle={Proceedings of COLM},
209	  year={2024},
210	  url={https://arxiv.org/abs/2404.01413}
211	}
212	
213	@inproceedings{guo2024curious,
214	  title={The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},
215	  author={Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chloe},
216	  booktitle={Findings of NAACL},
217	  year={2024},
218	  url={https://arxiv.org/abs/2311.09807}
219	}
220	
221	@article{briesch2023selfconsuming,
222	  title={Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop},
223	  author={Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},
224	  journal={arXiv preprint arXiv:2311.16822},
225	  year={2023},
226	  url={https://arxiv.org/abs/2311.16822}
227	}
228	
229	@inproceedings{padmakumar2024writing,
230	  title={Does Writing with Language Models Reduce Content Diversity?},
231	  author={Padmakumar, Vishakh and He, He},
232	  booktitle={Proceedings of ICLR},
233	  year={2024},
234	  url={https://arxiv.org/abs/2309.05196}
235	}
236	
237	% === New entries (added 2026-05-15, FR-10) ===
238	
239	@inproceedings{krishna2023paraphrasing,
240	  title={Paraphrasing Evades Detectors of {AI}-Generated Text, but Retrieval is an Effective Defense},
241	  author={Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
242	  booktitle={Advances in Neural Information Processing Systems},
243	  year={2023}
244	}
245	
246	@article{sadasivan2023detect,
247	  title={Can {AI}-Generated Text be Reliably Detected?},
248	  author={Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
249	  journal={arXiv preprint arXiv:2303.11156},
250	  year={2023},
251	  url={https://arxiv.org/abs/2303.11156}
252	}
253	
254	@inproceedings{hao2025rewrite,
255	  title={Learning to Rewrite: Generalized {LLM}-Generated Text Detection},
256	  author={Hao, Wei and Guan, Ran and Lu, Kangjie and Zhang, Shuai},
257	  booktitle={Findings of ACL},
258	  year={2025}
259	}
260	
261	@inproceedings{shi2025collapse,
262	  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},
263	  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},
264	  booktitle={Advances in Neural Information Processing Systems},
265	  year={2025}
266	}
267	
268	@article{gambetta2024surplexity,
269	  title={Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},
270	  author={Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and Knott, Alistair and Pappalardo, Luca},
271	  journal={arXiv preprint arXiv:2410.12341},
272	  year={2024}
273	}
274	
275	@inproceedings{amin2025escaping,
276	  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},
277	  author={Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar and Vassilvitskii, Sergei},
278	  booktitle={Advances in Neural Information Processing Systems},
279	  year={2025}
280	}
281	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cd12de9-5483-48e7-8d10-a1e8acef5046",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "2873a4d1-7db0-44d5-9319-5713c60388af",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
      "content": "% === References for gen-depth-contamination ===\n% Source: literature_map.yaml — verified 2026-05-15\n\n% === Must-Cite ===\n\n@inproceedings{drayson2025,\n  title={Machine-Generated Text Detection Prevents Language Model Collapse},\n  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  booktitle={Proceedings of EMNLP},\n  year={2025},\n  url={https://arxiv.org/abs/2502.15654}\n}\n\n@inproceedings{schaeffer2025position,\n  title={Position: Model Collapse Does Not Mean What You Think},\n  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},\n  booktitle={Proceedings of ICML},\n  year={2025},\n  url={https://arxiv.org/abs/2503.03150}\n}\n\n@inproceedings{kazdan2025collapse,\n  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},\n  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},\n  booktitle={Proceedings of ICML},\n  year={2025},\n  url={https://arxiv.org/abs/2410.16713}\n}\n\n@inproceedings{mitchell2023detectgpt,\n  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},\n  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  booktitle={Proceedings of ICML},\n  year={2023}\n}\n\n% === Should-Cite ===\n\n@article{basani2026diveye,\n  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},\n  author={Basani, Advik Raj and Chen, Pin-Yu},\n  journal={Transactions on Machine Learning Research},\n  issn={2835-8856},\n  year={2026},\n  url={https://arxiv.org/abs/2509.18880}\n}\n\n@inproceedings{zawalski2026codec,\n  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},\n  author={Zawalski, Micha{\\l} and Boubdir, Meriem and Ba{\\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},\n  booktitle={Proceedings of ICLR},\n  year={2026},\n  url={https://arxiv.org/abs/2510.27055}\n}\n\n@inproceedings{zhang2024minkpp,\n  title={Min-{K}\\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},\n  booktitle={Proceedings of EMNLP},\n  year={2024}\n}\n\n@article{shumailov2024collapse,\n  title={{AI} Models Collapse When Trained on Recursively Generated Data},\n  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal={Nature},\n  volume={631},\n  pages={755--759},\n  year={2024}\n}\n\n@inproceedings{alemohammad2024selfconsuming,\n  title={Self-Consuming Generative Models Go {MAD}},\n  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle={Proceedings of ICLR},\n  year={2024}\n}\n\n@inproceedings{dohmatob2024model,\n  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},\n  booktitle={Proceedings of ICML},\n  year={2024}\n}\n\n@inproceedings{xie2023dsir,\n  title={Data Selection for Language Models via Importance Resampling},\n  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@inproceedings{tirumala2023d4,\n  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},\n  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@inproceedings{xie2023doremi,\n  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},\n  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@inproceedings{hans2024binoculars,\n  title={Spotting {LLMs} With Binoculars},\n  author={Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  booktitle={Proceedings of ICML},\n  year={2024}\n}\n\n% === Probing Classifiers ===\n\n@inproceedings{alain2017understanding,\n  title={Understanding Intermediate Layers Using Linear Classifier Probes},\n  author={Alain, Guillaume and Bengio, Yoshua},\n  booktitle={ICLR Workshop},\n  year={2017}\n}\n\n@article{belinkov2022probing,\n  title={Probing Classifiers: Promises, Shortcomings, and Advances},\n  author={Belinkov, Yonatan},\n  journal={Computational Linguistics},\n  volume={48},\n  number={1},\n  pages={207--219},\n  year={2022}\n}\n\n% === Model Collapse Avoidability ===\n\n@inproceedings{bao2024fast,\n  title={{Fast-DetectGPT}: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature},\n  author={Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  booktitle={Proceedings of ICLR},\n  year={2024},\n  url={https://arxiv.org/abs/2310.05130}\n}\n\n@inproceedings{frank2001ordinal,\n  title={A Simple Approach to Ordinal Classification},\n  author={Frank, Eibe and Hall, Mark},\n  booktitle={Proceedings of ECML},\n  pages={145--156},\n  year={2001}\n}\n\n% === Beyond-Binary Detection ===\n\n@inproceedings{cheng2025beyond,\n  title={Beyond Binary: Towards Fine-Grained {LLM}-Generated Text Detection via Role Recognition and Involvement Measurement},\n  author={Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},\n  booktitle={Proceedings of the ACM Web Conference (WWW)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.14259}\n}\n\n@article{mehta2025beyond,\n  title={Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models},\n  author={Mehta, Sushant},\n  journal={arXiv preprint arXiv:2511.17602},\n  year={2025},\n  url={https://arxiv.org/abs/2511.17602}\n}\n\n% === AI-Generated Content Prevalence ===\n\n@inproceedings{sun2025aigt,\n  title={Are We in the {AI}-Generated Text World Already? Quantifying and Monitoring {AIGT} on Social Media},\n  author={Sun, Zhen and Zhang, Zongmin and Shen, Xinyue and Zhang, Ziyi and Liu, Yule and Backes, Michael and Zhang, Yang and He, Xinlei},\n  booktitle={Proceedings of ACL},\n  year={2025},\n  url={https://arxiv.org/abs/2412.18148}\n}\n\n@article{spennemann2025quantifying,\n  title={Delving into: the Quantification of {AI}-Generated Content on the Internet (Synthetic Data)},\n  author={Spennemann, Dirk H. R.},\n  journal={arXiv preprint arXiv:2504.08755},\n  year={2025},\n  url={https://arxiv.org/abs/2504.08755}\n}\n\n% === New entries (added 2026-05-16, Round 4 reviewer) ===\n\n@inproceedings{dohmatob2025strong,\n  title={Strong Model Collapse},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle={Proceedings of ICLR},\n  year={2025},\n  url={https://arxiv.org/abs/2410.04840}\n}\n\n@inproceedings{wang2024semeval,\n  title={{SemEval}-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection},\n  author={Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas},\n  booktitle={Proceedings of SemEval},\n  year={2024},\n  url={https://arxiv.org/abs/2404.14183}\n}\n\n@inproceedings{gerstgrasser2024model,\n  title={Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data},\n  author={Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  booktitle={Proceedings of COLM},\n  year={2024},\n  url={https://arxiv.org/abs/2404.01413}\n}\n\n@inproceedings{guo2024curious,\n  title={The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},\n  author={Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chloe},\n  booktitle={Findings of NAACL},\n  year={2024},\n  url={https://arxiv.org/abs/2311.09807}\n}\n\n@article{briesch2023selfconsuming,\n  title={Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop},\n  author={Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},\n  journal={arXiv preprint arXiv:2311.16822},\n  year={2023},\n  url={https://arxiv.org/abs/2311.16822}\n}\n\n@inproceedings{padmakumar2024writing,\n  title={Does Writing with Language Models Reduce Content Diversity?},\n  author={Padmakumar, Vishakh and He, He},\n  booktitle={Proceedings of ICLR},\n  year={2024},\n  url={https://arxiv.org/abs/2309.05196}\n}\n\n% === New entries (added 2026-05-15, FR-10) ===\n\n@inproceedings{krishna2023paraphrasing,\n  title={Paraphrasing Evades Detectors of {AI}-Generated Text, but Retrieval is an Effective Defense},\n  author={Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@article{sadasivan2023detect,\n  title={Can {AI}-Generated Text be Reliably Detected?},\n  author={Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  journal={arXiv preprint arXiv:2303.11156},\n  year={2023},\n  url={https://arxiv.org/abs/2303.11156}\n}\n\n@inproceedings{hao2025rewrite,\n  title={Learning to Rewrite: Generalized {LLM}-Generated Text Detection},\n  author={Hao, Wei and Guan, Ran and Lu, Kangjie and Zhang, Shuai},\n  booktitle={Findings of ACL},\n  year={2025}\n}\n\n@inproceedings{shi2025collapse,\n  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},\n  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2025}\n}\n\n@article{gambetta2024surplexity,\n  title={Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},\n  author={Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and Knott, Alistair and Pappalardo, Luca},\n  journal={arXiv preprint arXiv:2410.12341},\n  year={2024}\n}\n\n@inproceedings{amin2025escaping,\n  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},\n  author={Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar and Vassilvitskii, Sergei},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2025}\n}\n",
      "numLines": 281,
      "startLine": 1,
      "totalLines": 281
    }
  },
  "sourceToolAssistantUUID": "7cd12de9-5483-48e7-8d10-a1e8acef5046",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-18T09:59:41.664Z_

<details><summary>↩ Tool result · `toolu_01HbZFFjeaCsvfWWJL2WXpbK`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddcdb5de-cdea-4e29-b3db-8de6f8e05f66",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "e5c06186-f949-4a86-a887-f1543900efbb",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "ddcdb5de-cdea-4e29-b3db-8de6f8e05f66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-18T09:59:42.164Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FNCCJMmXG3iL5wjqwmTDBt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5c06186-f949-4a86-a887-f1543900efbb",
  "isSidechain": false,
  "requestId": "req_011Cb9qbTrqFvb72wa5qsNzV",
  "type": "assistant",
  "uuid": "7cd12de9-5483-48e7-8d10-a1e8acef5046",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVLPVxpF5jURBeC9K5m7Hz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6071,
      "cache_read_input_tokens": 85828,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 376,
          "cache_read_input_tokens": 85828,
          "cache_creation_input_tokens": 6071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6071
          },
          "type": "message"
        }
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

_source line 97 · 2026-05-18T09:59:42.268Z_

```json
{
  "parentUuid": "2873a4d1-7db0-44d5-9319-5713c60388af",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "adef18ec-b4ea-4fb7-bc6c-7ae71b5a9e48",
  "timestamp": "2026-05-18T09:59:42.268Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 98 · 2026-05-18T09:59:48.776Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me compile the full review. Key observations:

1. **No Responsible NLP Research Checklist** found in the paper. ARR requires this.
2. **34 references total** - on the lower end for EMNLP.
3. **No em-dashes or AI writing markers** - the writing is clean.
4. **Missing references**: watermarking (Kirchenbauer et al. 2023), some data quality papers.

Let me now write the full review and post it to the Director.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adef18ec-b4ea-4fb7-bc6c-7ae71b5a9e48",
  "isSidechain": false,
  "requestId": "req_011Cb9qc1XairqRArWdcGuMh",
  "type": "assistant",
  "uuid": "77d483cc-b4f0-447f-bb23-171b200693ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158jJQYQ7sr1EAL95qVexkL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5173,
      "cache_read_input_tokens": 91899,
      "output_tokens": 5088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5173,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5088,
          "cache_read_input_tokens": 91899,
          "cache_creation_input_tokens": 5173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5173
          },
          "type": "message"
        }
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

_source line 99 · 2026-05-18T09:59:50.323Z_

已完成全文通读、引用验证、格式检查和相关工作搜索。现在撰写审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77d483cc-b4f0-447f-bb23-171b200693ff",
  "isSidechain": false,
  "requestId": "req_011Cb9qc1XairqRArWdcGuMh",
  "type": "assistant",
  "uuid": "c1cd9931-da75-494c-9f76-891253c0ca56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158jJQYQ7sr1EAL95qVexkL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5173,
      "cache_read_input_tokens": 91899,
      "output_tokens": 5088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5173,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5088,
          "cache_read_input_tokens": 91899,
          "cache_creation_input_tokens": 5173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5173
          },
          "type": "message"
        }
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

_source line 100 · 2026-05-18T10:01:44.512Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01XFc6RZyxB9gLZQ3SJbhNPE`</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见（新颖性 + 完整性侧重）\n\n---\n\n## Summary\n\n本文提出 \"generational depth estimation\" 任务，旨在测量递归合成文本经历了多少轮生成。核心概念 K*（discrimination boundary）定义为相邻代际仍可区分的最大深度。使用 15 维统计特征 + OBD-LightGBM 分类器，在 9 个模型配置（5 个架构族、1B–14B）、3 个域、4 种解码策略上实验，发现 web 文本 K*=2、arXiv K*=3、Wikipedia K*=1。下游验证显示 K*=2 正确预测 binary filtering 为最优策略。\n\n---\n\n## Strengths\n\n**S1. 问题定义新颖且形式化清晰。** \"Generational depth estimation\" 作为一个新任务被首次明确提出并形式化（Eq.1, Section 3.1）。K* 概念借助 Data Processing Inequality 给出理论动机，再通过 AUC 阈值操作化，形成了一个可复现的测量框架。这是本文最核心的贡献，在现有文献中确实没有直接先例。\n\n**S2. 实验覆盖面广且统计严格。** 9 个模型配置、5 个架构族、3 个域、4 种解码策略，加上 bootstrap CI、permutation test、ANOVA 等统计工具（Table 1, Table S8, Table 7），实验设计的系统性在同类工作中突出。对 marginal cases（Qwen-cont CI lower bound 仅超 θ 0.002, Section 4.1; LLaMA-8B borderline, Table S2b）的透明报告值得肯定。\n\n**S3. 域排序结果有洞察力。** arXiv (K*=3) > C4 (K*=2) > Wikipedia (K*=1) 的域排序（Table 4, Section 4.5）在跨模型、跨评分器条件下一致保持，建立了域结构复杂度作为 K* 主导因素的论点。Mistral-7B 在 C4 上 K*=1 但在 arXiv 上 K*=3（Section 6）提供了域主导而非模型主导的有力证据。\n\n**S4. 消融分析充分。** 阈值敏感性（Table 8, Figure 3）、self-BLEU 消融（Table S14）、特征子集稳定性（Table S15）、长度混淆因素控制（Table S5, Appendix E）、scorer confound 解析（Table S13, Appendix H）——几乎对每个潜在质疑都进行了预防性分析。\n\n**S5. 写作质量高。** 无明显 AI 写作痕迹（无解释性 em-dash、无 Furthermore/Moreover 堆砌、无 -ing 短语结尾）。术语定义完整（K*, OBD, AUC 阈值等首次出现均有定义）。主线基本统一。\n\n---\n\n## Weaknesses\n\n**W1. [critical] 核心技术贡献偏薄——方法层面缺乏新颖性。**\n\n本文的方法由三部分组成：(a) 15 维手工统计特征（surprisal moments、词汇多样性、频率尾部），(b) Frank & Hall (2001) 的 OBD 分解，(c) 现成的 LightGBM。三者均为已有技术的直接组合，无新模型架构、新训练目标、新理论结果。论文的新颖性完全依赖问题定义和实验发现，而非方法创新。\n\n- 具体位置：Section 3.2（Features and Classifier）仅描述特征定义和现有分类器，无方法论突破\n- 为什么影响接收：EMNLP 作为 NLP 顶会，对 method contribution 有期望。纯测量/实验论文需要发现本身足够深刻或颠覆性来弥补方法创新不足\n- 建议：明确 positioning 为 empirical/measurement paper，或增加方法创新（如设计专门的 depth-aware 架构、理论推导 K* 的解析上界）\n\n**W2. [critical] K*=2 的实际意义有限——与 binary detection 的增量不清晰。**\n\nK*=2 意味着一次生成后文本即无法与更深层合成内容区分（\"one-wash laundering\"），这使得本文的 depth estimation 框架在 web 文本上退化为 binary detection。论文在 Discussion（\"Why K* matters\"）中试图将此定性为 \"precise measurement\" 而非 negative result，但这一论点说服力不足：\n\n- Drayson et al. (2025) 已经用 binary detection + SIR filtering 取得了有效的数据筛选效果（cited in Section 2, Related Work）。本文 Section 5 的 filtering 实验本质上验证了 binary 策略最优，等于 post-hoc 证实了已有工作的合理性，而非提供新的实践能力\n- 下游 MMLU 改善仅 0.77pp（Table 5: 0.5941 vs. 0.5865 no-filter），虽然统计显著，但 practical significance 很小\n- Dose-response 分析（Appendix F, Table 10）在 10–50% 污染率下效应量缩小 3–6×，graduated filtering 与 no-filter 无显著差异\n- 建议：(a) 更诚实地讨论 K*=2 的 negative implications；(b) 强调 arXiv K*=3 和 retrain-chain K*≥4 的正面结果，展示框架在 depth>2 场景的真正价值；(c) 提供 K*=3 域上 graduated vs. binary filtering 的对比实验，验证框架在 depth>2 时确实能指导更精细的策略选择\n\n**W3. [major] Filtering 实验规模和设计偏弱，难以支撑 Contribution 级别的 claim。**\n\n- 仅使用一个下游模型（Qwen2.5-1.5B-Instruct）+ 两个 benchmark（MMLU, HellaSwag）\n- Pythia-1.4B 复制实验（Appendix G, Table 11）的 MMLU baseline 仅 0.2568（近乎随机），filtering 差异（0.2585 vs. 0.2568）缺乏实际意义\n- 100% synthetic 设定是极端上界，而现实场景效果微弱（Table 10）\n- Section 5 标题为 \"K*-Aware Data Filtering\"，但实际上仅使用了 binary filtering（K*=2 导致），并未真正展示 K*-aware 的精细粒度筛选\n- 具体位置：Section 5, Table 5, Appendix F–G\n- 建议：在 arXiv (K*=3) 上运行 graduated filtering 实验，展示 depth-aware filtering 在 K*>2 时的真实优势\n\n**W4. [major] Related Work 引用密度偏低（34 篇），多个重要方向缺失。**\n\n34 篇引用对 EMNLP 而言偏少。以下方向缺乏覆盖：\n\n1. **Watermarking-based provenance tracking**：Kirchenbauer et al. (2023) \"A Watermark for Large Language Models\" 是 LLM 文本溯源的里程碑工作；WASA (ACL 2025), Waterfall (EMNLP 2024) 等提供了替代的合成文本追踪范式。论文完全未讨论 watermarking 作为 depth tracking 的替代方案\n2. **大规模数据质量工程**：FineWeb (Penedo et al. 2024), RedPajama, Dolma 等项目在数据筛选实践中影响深远，但 Related Work 的 \"Data selection and curation\" 段仅 2 行\n3. **训练数据检测的更多方法**：GLTR (Gehrmann et al. 2019), GPTZero 系列，以及 EMNLP 2024/2025 的多篇 MGT detection 工作\n4. **模型 collapse 缓解的更多近期工作**：如 \"Escaping Model Collapse via Synthetic Data Verification\" (arXiv 2510.16657)\n\n- 具体位置：Section 2（仅 22 行正文，4 个 paragraph）\n- 建议：扩展 Related Work 到至少 40+ 引用；增加 watermarking 段讨论为什么 post-hoc detection 比 proactive watermarking 在某些场景更适用\n\n**W5. [major] 论文身份（identity）不够清晰——measurement paper, detection paper, 还是 curation paper？**\n\n论文同时声称三类贡献：(a) K* 测量（measurement），(b) 跨模型迁移的检测能力（detection），(c) 下游 filtering 指导（curation）。这三者之间的权重分配不均且逻辑连接不够紧密：\n\n- Abstract 和 Introduction 的故事线主要围绕 measurement（K* 的测量和性质），但 Contribution list 的第三条是 cross-model transfer（更偏 detection），而 Section 5 突然转向 curation 应用\n- 论文核心发现（K*=2）实际上否定了 depth-aware curation 的必要性（对 web 文本），使 curation 叙事自相矛盾\n- 具体位置：Abstract（187 words，试图覆盖所有三个方向，数字堆砌）；Introduction Contribution list (a)–(c)；Section 5\n- 建议：明确定位为 measurement/empirical paper，将 filtering 降级为 validation experiment 而非独立 contribution\n\n**W6. [minor] Abstract 数字堆砌，信息密度过高。**\n\nAbstract 在约 190 words 中塞入了：9 model configurations, 5 architecture families, 1B–14B, 3 source domains, 4 decoding strategies, θ=0.60, Cohen's h≈0.20, K*∈{1,2,3}, 8/9 configurations, K*=2, K*=3, 80–92%, ρ>0.90, MMLU 0.5941 vs. 0.6018。审稿人 30 秒内无法消化这么多数字。\n\n- 建议：保留 2–3 个关键数字（K*=2 for web text, K*=3 for academic text, 80–92% cross-model transfer），其余移至正文\n\n**W7. [minor] Qwen 家族过度代表。**\n\n9 个配置中 5 个是 Qwen 变体（Qwen-rw, Qwen-cont, Qwen-base, Qwen-7B, Qwen-14B），其余 4 个架构族各仅 1 个配置。这导致多个分析（cross-scorer, arXiv domain）中 Qwen 的 scorer confound 成为反复出现的问题。虽然不影响核心结论，但削弱了\"跨架构\"claim 的说服力。\n\n- 具体位置：Table 1（Section 3.3）\n- 建议：在 Limitations 中更明确承认 Qwen 过度代表的问题\n\n**W8. [minor] Responsible NLP Research Checklist 缺失。**\n\nARR 2026 要求提交 Responsible NLP Research Checklist（通过 OpenReview 表单或独立 section）。当前稿件中未找到 checklist 相关内容。\n\n---\n\n## Questions\n\n**Q1.** arXiv K*=3 的发现意味着 depth-aware (graduated) filtering 在该域应当优于 binary。是否有 arXiv 域的 filtering 实验？如果 K*=3 能带来 graduated filtering 的实际优势，这将大幅加强论文的 practical contribution。\n\n**Q2.** Qwen-continuation 的 1v2 CI lower bound 仅超 θ 0.002（Section 4.1, Limitations (4)），cross-scorer 验证直接将其降至 K*=1。这是否意味着该配置的 K*=2 判定实质上不 robust？如果去掉这个 marginal case，\"8/9 configurations yield K*=2\" 的 claim 是否应改为 \"7/9\"？\n\n**Q3.** 论文使用 prompt-chain（isolating text-level degradation），而实际 web contamination 更可能涉及 retrain-chain 或混合场景。Prompt-chain K*=2 而 retrain-chain K*≥4 (Appendix E)——这一巨大差异是否意味着 prompt-chain K* 在实际数据筛选中的适用性有限？\n\n**Q4.** Data Processing Inequality 保证了 K_theory 的存在（Section 3.1），但论文未提供 K_theory 的任何上界估计。K* 与 K_theory 之间的 gap 有多大？是否可能通过更强的特征（如 neural probe 的 K*=3 for Qwen）显著提升 K*？\n\n**Q5.** Self-BLEU 的计算使用同 fold 同 depth 的参考样本（Section 3.2）。在部署场景下 depth label 未知，self-BLEU 不可计算。论文提到可以用 corpus-level self-similarity 替代或直接去掉（14D ablation），但这意味着 deployment feature set 与 training feature set 不同。这是否影响报告的 transfer 结果？\n\n---\n\n## Missing References\n\n1. **Kirchenbauer et al. (2023)** \"A Watermark for Large Language Models\" (ICML 2023) — watermarking 作为合成文本追踪的替代范式，必须讨论\n2. **Pan et al. (2024)** \"Waterfall: Framework for Robust Text Watermarking and Provenance for LLMs\" (EMNLP 2024)\n3. **Gehrmann et al. (2019)** \"GLTR: Statistical Detection and Visualization of Generated Text\" (ACL 2019) — 早期统计检测方法，与本文 feature 设计高度相关\n4. **Penedo et al. (2024)** \"The FineWeb Datasets\" — 大规模 web 数据筛选实践\n5. **Ippolito et al. (2020)** \"Automatic Detection of Generated Text is Easiest when Humans are Fooled\" (ACL 2020) — 人类与自动检测器对比的经典工作\n6. 建议增加至少 8–10 篇引用以达到 EMNLP 典型密度\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 (Findings)**\n\n**Confidence: high**（我对 synthetic text detection、model collapse、data curation 领域较熟悉，仔细检查了核心实验数据）\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨、统计方法规范，但 filtering 实验规模偏小且效应量微弱；K*=2 核心结论的部分配置 marginal |\n| Excitement | 2.5/5 | 问题定义有新意，但核心发现（K*=2 → binary filtering optimal）的实际增量相对 Drayson et al. (2025) 有限 |\n| Reproducibility | 4/5 | 特征定义清晰（Table S5）、超参数完整（Table S6–S7）、数据集公开；承诺代码释放 |\n| Overall | 3.0 | 问题新颖、实验扎实，但方法层面缺乏技术深度，核心发现的实际意义被 K*=2 限制，filtering 验证偏弱。适合 Findings 收录 |\n\n**简要总评：** 本文提出了一个新颖的问题（generational depth estimation）并进行了系统的实验测量，这是其最大优势。但方法层面仅是已有技术的组合（hand-crafted features + OBD + LightGBM），缺乏技术深度。核心发现 K*=2 本质上意味着 depth estimation 对 web 文本退化为 binary detection，与已有工作（Drayson et al. 2025）的实践增量有限。如果能补充 arXiv (K*=3) 域的 graduated filtering 实验以展示 depth-aware 策略的真正优势，并扩展 related work，论文可提升至 Borderline Conference。",
  "reviewer_id": "2",
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1cd9931-da75-494c-9f76-891253c0ca56",
  "isSidechain": false,
  "requestId": "req_011Cb9qc1XairqRArWdcGuMh",
  "type": "assistant",
  "uuid": "bd00b850-cb88-4ece-943b-e64a17876756",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158jJQYQ7sr1EAL95qVexkL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5173,
      "cache_read_input_tokens": 91899,
      "output_tokens": 5088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5173,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5088,
          "cache_read_input_tokens": 91899,
          "cache_creation_input_tokens": 5173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5173
          },
          "type": "message"
        }
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

_source line 101_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性**  ### Venue 信息 - **目标**: EMNLP 2026（ARR May 2026 cycle） - **Deadline**: 2026-05-25 - **格式**: ACL 双栏模板，`\\usepackage[review]{acl}`，Long…",
  "leafUuid": "bd00b850-cb88-4ece-943b-e64a17876756",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Runtime record

_source line 102_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on generational depth contamination detection",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Tool result

_source line 103 · 2026-05-18T10:01:48.768Z_

<details><summary>↩ Tool result · `toolu_01XFc6RZyxB9gLZQ3SJbhNPE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd00b850-cb88-4ece-943b-e64a17876756",
  "isSidechain": false,
  "promptId": "0319cb62-3396-4024-9c89-2feacc535b49",
  "type": "user",
  "uuid": "d55dfb80-affe-44fd-8569-618d245d335e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "bd00b850-cb88-4ece-943b-e64a17876756",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 104_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on generational depth contamination detection",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Runtime record

_source line 105 · 2026-05-18T10:03:26.924Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T10:03:26.924Z",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "content": "[Round 1 审稿请求]:\n## Step 2: 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Weakness、Question 和 Missing Reference：\n- **[AGREE]**：同意并说明理由（可补充你自己的发现）\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n  \n特别关注：你和 R1 在哪些关键问题上看法一致？哪些地方有分歧？\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Summary\n本文定义并测量了递归合成文本的\"代际深度辨别边界\" K*：在相邻代际间分类器能可靠区分的最大深度。使用 15 维统计特征 + OBD-LightGBM 分类器，在 9 个模型配置（5 个架构族, 1B–14B）、3 个领域、4 种解码策略上测得 K*∈{1,2,3}，其中 web 文本 K*=2，arXiv K*=3，Wikipedia K*=1。论文还展示了 80–92% 的跨模型迁移率和下游数据过滤验证。\n\n### Strengths\nS1. 问题新颖且定义清晰。K* 填补了二元检测和 model collapse 文献之间的空白。\nS2. 实验覆盖面广。9 模型×3 域×4 解码，cross-scorer/domain/model 系统性控制混淆。\nS3. 统计处理高于平均水平。Bootstrap CIs、permutation tests、ANOVA、Holm-Bonferroni、Cohen's h。\nS4. 消融实验充分。\nS5. Limitations 诚实且详尽。\n\n### Weaknesses\n**W1. [critical] θ=0.60 阈值的三重论证中，两条缺乏严谨性，整个 K* 框架的稳健性依赖此参数。**\n- 论证 (a) Cohen's h ≈ 0.20 在脚注自承是 \"motivating analogy\"，但正文作为\"第一条独立证据\"展示\n- 论证 (b) permutation test 证明 AUC > chance，但无法区分 θ=0.55 和 θ=0.65\n- 论证 (c) 是 post-hoc gap observation，不应包装为\"独立证据\"\n- 实际后果：θ=0.55 时 Qwen 升至 K*=3；θ=0.70 时全部降至 K*=1。OLMo (1v2=0.6145) 和 Qwen-cont (1v2=0.6112) 的 K*=2 余量仅 1–1.5 pp\n- 建议：放弃\"三条独立证据\"包装，坦率承认 θ 是数据驱动选择\n\n**W2. [critical] \"Generator-independent\" / \"text-intrinsic\" 措辞与 scorer 依赖性矛盾。**\n- Cross-scorer 验证显示 Qwen-cont K* 从 2 降至 1\n- Wikipedia same-family scoring 人为提升 K*，cross-family 后降回 1\n- ANOVA Scorer η²_p = 0.192 论文淡化为 \"practically minor\"，但在 θ 选择中却用 Cohen convention——选择性引用\n- 9 个 C4 配置中至少 2 个换 scorer 后 K* 改变\n- 建议：改为 \"generator-transferable under fixed scorer\"\n\n**W3. [major] 下游过滤实验效应量极小，实际意义不确定。**\n- 100% 合成: binary-ours MMLU +0.77pp，但所有策略都在退化\n- Dose-response 10%: binary vs. no-filter = +0.21pp MMLU\n- Pythia: +0.17pp MMLU（baseline 0.2568 近乎随机）\n- \"~50% reduction in degradation\" 是相对量，绝对量 <1pp\n- 建议：明确区分\"统计显著\"和\"实际有意义\"\n\n**W4. [major] Data Processing Inequality 引用技术上不够精确。**\n- DPI 保证 I(X; Y_k) 单调递减，但论文 K* 基于相邻代际 (Y_{k-1}, Y_k) 可区分性——两个不同的量\n- \"Together with Markov chain convergence\" 需要遍历性/不可约性假设，LLM 输出空间是否满足未讨论\n- 不影响经验结果，但影响 \"information-theoretic guarantee\" 叙事\n- 建议：降低理论声明强度，定位为 motivation 而非 guarantee\n\n**W5. [major] \"Domain structural complexity\" 作为 K* 主要决定因素的解释缺乏操作化定义。**\n- \"structural complexity\" 从未被形式化定义或独立测量\n- arXiv K*=3 可能是分类器检测 LaTeX 格式退化而非真正的 depth signal\n- JSD 的 λ 值是 K* 的后果而非原因\n- 建议：提出可操作的 complexity 度量或承认为经验观察\n\n**W6. [minor] 跨模型迁移 \"80–92%\" 掩盖了绝对精度低（~0.35）。**\n\n**W7. [minor] arXiv 与 C4 样本量差异（2,200 vs. 5,000）对 CI 宽度影响。**\n- C4 子采样至 n=2,200 后 K* 降至 1——暴露 C4 K*=2 在小样本下不稳定\n\n### Questions\nQ1. OBD vs. multiclass LightGBM 的 MAE 差异是否有统计检验？\nQ2. Cross-scorer ANOVA N=300 如何构成？per-fold AUC 作为 DV 时 fold 非独立性？\nQ3. Retrain-chain K*≥4 vs prompt-chain K*=2——K* 框架对最需要它的场景是否适用？\nQ4. GPT-5.5/Claude Opus 4.6 zero-shot baseline 的 prompt 和 input 是什么？\nQ5. 为什么没讨论 watermarking 作为 baseline？\n\n### Missing References\n- Kirchenbauer et al. (2023) watermarking\n- 更多 ordinal classification 文献\n- Penedo et al. (2023/2024) FineWeb/RefinedWeb 数据策展\n\n### Overall Assessment\nScore: 3.0 (Findings), Confidence: 4 (High)\n核心经验发现有效，问题新颖，但 claims 强度需校准。Findings 水平充分，main conference 需加强 framing 严谨性和下游实用性。\n\n---\n\n请逐条回应以上所有 Weakness (W1–W7)、Question (Q1–Q5) 和 Missing References。"
}
```

---


### Runtime record

_source line 106 · 2026-05-18T10:03:26.925Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T10:03:26.925Z",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


## Round 2

## Round 2

2 recorded events


### User

_source line 107 · 2026-05-18T10:03:26.914Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d55dfb80-affe-44fd-8569-618d245d335e",
  "isSidechain": false,
  "promptId": "45562aac-6eb0-4db0-8447-1b023d1e76ac",
  "type": "user",
  "isMeta": true,
  "uuid": "1f97352e-f8b3-42a9-844c-359425c9515f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 108 · 2026-05-18T10:03:26.914Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f97352e-f8b3-42a9-844c-359425c9515f",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "37eb8c71-2f29-4837-a6fa-b2bbca01a59c",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "ae7595d3-3e93-4f29-b468-7bd5ba79beb6",
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

## Round 3

10 recorded events


### User

_source line 109 · 2026-05-18T10:03:27.009Z_

[Round 1 审稿请求]:
## Step 2: 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Weakness、Question 和 Missing Reference：
- **[AGREE]**：同意并说明理由（可补充你自己的发现）
- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）
  
特别关注：你和 R1 在哪些关键问题上看法一致？哪些地方有分歧？

---

## Reviewer 1 完整审稿意见

### Summary
本文定义并测量了递归合成文本的"代际深度辨别边界" K*：在相邻代际间分类器能可靠区分的最大深度。使用 15 维统计特征 + OBD-LightGBM 分类器，在 9 个模型配置（5 个架构族, 1B–14B）、3 个领域、4 种解码策略上测得 K*∈{1,2,3}，其中 web 文本 K*=2，arXiv K*=3，Wikipedia K*=1。论文还展示了 80–92% 的跨模型迁移率和下游数据过滤验证。

### Strengths
S1. 问题新颖且定义清晰。K* 填补了二元检测和 model collapse 文献之间的空白。
S2. 实验覆盖面广。9 模型×3 域×4 解码，cross-scorer/domain/model 系统性控制混淆。
S3. 统计处理高于平均水平。Bootstrap CIs、permutation tests、ANOVA、Holm-Bonferroni、Cohen's h。
S4. 消融实验充分。
S5. Limitations 诚实且详尽。

### Weaknesses
**W1. [critical] θ=0.60 阈值的三重论证中，两条缺乏严谨性，整个 K* 框架的稳健性依赖此参数。**
- 论证 (a) Cohen's h ≈ 0.20 在脚注自承是 "motivating analogy"，但正文作为"第一条独立证据"展示
- 论证 (b) permutation test 证明 AUC > chance，但无法区分 θ=0.55 和 θ=0.65
- 论证 (c) 是 post-hoc gap observation，不应包装为"独立证据"
- 实际后果：θ=0.55 时 Qwen 升至 K*=3；θ=0.70 时全部降至 K*=1。OLMo (1v2=0.6145) 和 Qwen-cont (1v2=0.6112) 的 K*=2 余量仅 1–1.5 pp
- 建议：放弃"三条独立证据"包装，坦率承认 θ 是数据驱动选择

**W2. [critical] "Generator-independent" / "text-intrinsic" 措辞与 scorer 依赖性矛盾。**
- Cross-scorer 验证显示 Qwen-cont K* 从 2 降至 1
- Wikipedia same-family scoring 人为提升 K*，cross-family 后降回 1
- ANOVA Scorer η²_p = 0.192 论文淡化为 "practically minor"，但在 θ 选择中却用 Cohen convention——选择性引用
- 9 个 C4 配置中至少 2 个换 scorer 后 K* 改变
- 建议：改为 "generator-transferable under fixed scorer"

**W3. [major] 下游过滤实验效应量极小，实际意义不确定。**
- 100% 合成: binary-ours MMLU +0.77pp，但所有策略都在退化
- Dose-response 10%: binary vs. no-filter = +0.21pp MMLU
- Pythia: +0.17pp MMLU（baseline 0.2568 近乎随机）
- "~50% reduction in degradation" 是相对量，绝对量 <1pp
- 建议：明确区分"统计显著"和"实际有意义"

**W4. [major] Data Processing Inequality 引用技术上不够精确。**
- DPI 保证 I(X; Y_k) 单调递减，但论文 K* 基于相邻代际 (Y_{k-1}, Y_k) 可区分性——两个不同的量
- "Together with Markov chain convergence" 需要遍历性/不可约性假设，LLM 输出空间是否满足未讨论
- 不影响经验结果，但影响 "information-theoretic guarantee" 叙事
- 建议：降低理论声明强度，定位为 motivation 而非 guarantee

**W5. [major] "Domain structural complexity" 作为 K* 主要决定因素的解释缺乏操作化定义。**
- "structural complexity" 从未被形式化定义或独立测量
- arXiv K*=3 可能是分类器检测 LaTeX 格式退化而非真正的 depth signal
- JSD 的 λ 值是 K* 的后果而非原因
- 建议：提出可操作的 complexity 度量或承认为经验观察

**W6. [minor] 跨模型迁移 "80–92%" 掩盖了绝对精度低（~0.35）。**

**W7. [minor] arXiv 与 C4 样本量差异（2,200 vs. 5,000）对 CI 宽度影响。**
- C4 子采样至 n=2,200 后 K* 降至 1——暴露 C4 K*=2 在小样本下不稳定

### Questions
Q1. OBD vs. multiclass LightGBM 的 MAE 差异是否有统计检验？
Q2. Cross-scorer ANOVA N=300 如何构成？per-fold AUC 作为 DV 时 fold 非独立性？
Q3. Retrain-chain K*≥4 vs prompt-chain K*=2——K* 框架对最需要它的场景是否适用？
Q4. GPT-5.5/Claude Opus 4.6 zero-shot baseline 的 prompt 和 input 是什么？
Q5. 为什么没讨论 watermarking 作为 baseline？

### Missing References
- Kirchenbauer et al. (2023) watermarking
- 更多 ordinal classification 文献
- Penedo et al. (2023/2024) FineWeb/RefinedWeb 数据策展

### Overall Assessment
Score: 3.0 (Findings), Confidence: 4 (High)
核心经验发现有效，问题新颖，但 claims 强度需校准。Findings 水平充分，main conference 需加强 framing 严谨性和下游实用性。

---

请逐条回应以上所有 Weakness (W1–W7)、Question (Q1–Q5) 和 Missing References。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37eb8c71-2f29-4837-a6fa-b2bbca01a59c",
  "isSidechain": false,
  "promptId": "45562aac-6eb0-4db0-8447-1b023d1e76ac",
  "type": "user",
  "uuid": "4b94b204-296c-4e37-ab66-6451cc37a8ad",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 110 · 2026-05-18T10:03:59.610Z_

<details><summary>Logged reasoning block</summary>

```text
The Director is asking me to cross-review Reviewer 1's opinions, responding to each weakness, question, and missing reference with [AGREE] or [REBUT]. Let me carefully go through each point based on my own reading of the paper.

Let me think through each item:

**W1. θ=0.60 threshold justification**
R1 argues the three-part justification is weak. I partially agree - the Cohen's h analogy is acknowledged as such in the footnote, and the "three independent lines of evidence" framing is somewhat oversold. However, the θ sensitivity analysis (Figure 3, Table 8) does show K*=2 is stable across [0.575, 0.625], and the key observation is the ~5-11pp discontinuity between 1v2 and 2v3 AUC clusters. 

The robustness analysis actually does support the finding even if the original framing overstates it. Partial AGREE.

**W2. "Generator-independent" vs scorer dependence**
R1 makes a strong point here. The Qwen-cont case drops from K*=2 to K*=1 under cross-scoring, and Wikipedia same-family scoring inflates K*. The η²_p = 0.192 for Scorer is indeed characterized as "practically minor" while being a "large" effect by Cohen's convention - that's selective application of standards. This is a legitimate criticism. The paper does acknowledge scorer effects exist, but the claim of generator-independence is overstated given how much the results shift.

AGREE overall, with some nuance.

**W3. Filtering effect sizes**
I raised a similar concern. Strongly agree.

**W4. DPI citation precision**
The DPI guarantees monotone decreasing mutual information, but K* measures something different - adjacent-generation discriminability. The Markov chain convergence argument needs ergodicity assumptions that aren't fully justified. The paper frames this as motivation rather than formal proof, which is fair, but the language about guaranteeing finite K_theory is stronger than the actual theoretical support warrants.

**W5. "Domain structural complexity" lacks operationalization**
Valid point - the paper invokes structural complexity as an explanation but never formally defines or independently measures it. The JSD values are consequences, not causes. The arXiv explanation about LaTeX degradation is plausible but could be a confound; the classifier might be picking up format decay rather than genuine depth.

**W6. Transfer accuracy "80-92%" vs absolute accuracy ~0.35**
The retention rates are a reasonable metric, but the absolute 6-class accuracy is genuinely low. This doesn't invalidate the core findings, though it's worth acknowledging the practical limitations.

**W7. arXiv vs C4 sample size**
The paper addresses this with a subsample control showing C4 drops to K*=1 at n=2,200, which reveals the C4 result is sample-sensitive. The arXiv K*=3 at the same size is the stronger signal, so this criticism is fair but the paper does engage with it.

**Q1. OBD vs multiclass statistical test**
The MAE difference between methods is small, and whether that difference is statistically meaningful requires proper testing rather than just reporting the raw values.

**Q2. ANOVA N=300 construction**
The design breaks down to 3 generators × 4 scorers × 5 folds × 5 depth-pairs, but the per-fold AUC values aren't fully independent under GroupKFold, which is a legitimate technical concern.

**Q3. Retrain-chain applicability**
This mirrors my own question about the method's generalizability.

**Q4. Zero-shot baseline details**
The prompts used for the language models aren't detailed in the main text or appendix, which makes it hard to assess those results.

**Q5. Watermark**
Both reviewers and I flagged this—using watermarking as a baseline is problematic.

**Missing References**
Kirchenbauer and FineWeb citations are missing, and both I and the other reviewer caught this gap.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b94b204-296c-4e37-ab66-6451cc37a8ad",
  "isSidechain": false,
  "requestId": "req_011Cb9qtadbwTat46kCBVDpt",
  "type": "assistant",
  "uuid": "b7230399-609d-46fb-bc0d-d11e5bfbded6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVNoVzgE9tkmLCH3XEDL7r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2049,
      "cache_read_input_tokens": 102237,
      "output_tokens": 5954,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2049,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5954,
          "cache_read_input_tokens": 102237,
          "cache_creation_input_tokens": 2049,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2049
          },
          "type": "message"
        }
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

_source line 111 · 2026-05-18T10:03:59.613Z_

逐条回应 Reviewer 1 的审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7230399-609d-46fb-bc0d-d11e5bfbded6",
  "isSidechain": false,
  "requestId": "req_011Cb9qtadbwTat46kCBVDpt",
  "type": "assistant",
  "uuid": "30c9c486-7079-46c9-95b5-1a8bb4ed2371",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVNoVzgE9tkmLCH3XEDL7r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2049,
      "cache_read_input_tokens": 102237,
      "output_tokens": 5954,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2049,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5954,
          "cache_read_input_tokens": 102237,
          "cache_creation_input_tokens": 2049,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2049
          },
          "type": "message"
        }
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

_source line 112 · 2026-05-18T10:05:36.137Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_014M8ZmKrcy7jgVsjKPNkwt8`</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条评议\n\n---\n\n### Weaknesses\n\n**[AGREE] R1-W1: θ=0.60 阈值的\"三重论证\"包装过度**\n\n同意 R1 的核心判断。重新审阅 Section 3.1（Threshold choice 段），三条论证确实存在以下问题：\n\n- 论证 (a) Cohen's h ≈ 0.20：脚注已自承为 \"motivating analogy rather than a formal justification\"，但正文将其列为 \"first\" independent evidence，措辞不匹配\n- 论证 (b) permutation test：仅证明 AUC > chance (0.50)，对 θ 的具体取值没有区分力，R1 指出了这一点\n- 论证 (c) gap observation：这是对数据分布的描述（1v2 cluster 0.61–0.70, 2v3 cluster 0.55–0.59），不应包装为独立证据\n\n但我补充一点 R1 未充分肯定的内容：Figure 3 (fig_kstar_theta) 和 Table 8 (theta_sensitivity) 确实展示了 K*=2 在 θ∈[0.575, 0.625] 区间的稳定性，且域排序（arXiv > C4 > Wikipedia）在全 θ 范围保持。核心发现对 θ 的具体值不高度敏感——但\"三条独立证据\"的包装方式确实需要修正。\n\nR1 建议\"坦率承认 θ 是数据驱动选择\"合理。我建议保留论证 (c)（gap observation）作为主要支撑，但改为诚实的 empirical observation 而非\"独立证据\"。\n\n---\n\n**[AGREE] R1-W2: \"Generator-independent\" 措辞与 scorer 依赖性矛盾**\n\n这是 R1 审稿中最精准的技术批评，我完全同意。具体证据：\n\n1. Table S13 (Scorer Sensitivity)：Qwen-cont 在 cross-scoring 下从 K*=2 降至 K*=1（1v2 AUC: 0.6112 → 0.5923/0.5858）\n2. Appendix H (Wiki Domain, Table S16)：Qwen-7B same-family scoring K*=2，cross-family 降至 K*=1（Δ = -2.4pp）\n3. ANOVA Table 7：Scorer η²_p = 0.192，论文称 \"practically minor\"，但按 Cohen convention 这是 large effect。R1 正确指出了这种选择性引用——Section 3.1 用 Cohen's h 作为 θ 的论据，Section 4.2 又淡化 Cohen 对 η²_p 的分类标准\n\n我在 Round 1 审稿（W1, Q2）中也注意到 Qwen-cont 的 marginal boundary，但 R1 将这一问题上升到术语层面（\"generator-independent\" 与实际 scorer 依赖性的系统性矛盾），分析更到位。\n\nR1 建议改为 \"generator-transferable under fixed scorer\" 精准且可操作。论文应在 Abstract（\"Generator-independent statistical features\"）和 Contribution (c) 中修正措辞。\n\n---\n\n**[AGREE] R1-W3: 下游过滤效应量极小**\n\n完全同意，这也是我的核心关切之一（我的 W2、W3）。补充 R1 未详细展开的一点：\n\n- Section 5 标题 \"K*-Aware Data Filtering\" 暗示一种基于 K* 的精细化过滤策略，但实际实验因 K*=2 完全退化为 binary filtering。论文真正需要的是在 K*=3 的 arXiv 域上运行 graduated vs. binary 的对比——这才能展示 K*-aware filtering 相对 binary 的增量价值\n- Dose-response (Table 10)：10% 污染下 binary vs. no-filter 仅 +0.21pp MMLU，且 MMLU 差异在 30%/50% 时 Holm-Bonferroni 校正后不显著（仅 HellaSwag 显著），论文正文未充分区分这两个 benchmark 的不同表现\n\nR1 和我对此问题的判断高度一致：filtering 实验作为 contribution 级别的 claim 支撑不足。\n\n---\n\n**[AGREE with nuance] R1-W4: DPI 引用技术精度**\n\nR1 的技术批评是正确的：DPI 保证 I(X; Y_k) 单调递减，但论文的 K* 基于相邻代际 (Y_{k-1}, Y_k) 可区分性。这两个量之间的关系需要额外论证（如相邻代际互信息的单调性需要更强条件）。\n\n不过我对严重性的判断略有不同：Section 3.1 的关键句是 \"Together with Markov chain convergence, this guarantees a finite K_theory beyond which adjacent generations are indistinguishable\"——这里 \"Markov chain convergence\" 确实可以保证相邻代际最终不可区分（mixing），但论文未讨论 LLM 输出空间是否满足 ergodicity/irreducibility。实际上，autoregressive generation 在有限温度下的 mixing 行为是可以论证的（非零温度采样赋予输出分布 full support），但论文确实跳过了这一步。\n\nR1 建议\"降低理论声明强度，定位为 motivation 而非 guarantee\"是合理的。这不影响任何经验结论，但影响 framing 的严谨性。\n\n---\n\n**[AGREE] R1-W5: \"Domain structural complexity\" 缺乏操作化定义**\n\n同意。\"Structural complexity\" 在论文中反复出现（Section 4.5: \"source-domain structural complexity as the primary determinant\"；Discussion: \"domain structural complexity\"），但从未被形式化定义或独立测量。\n\nR1 提出的替代解释（arXiv K*=3 可能反映 LaTeX 格式退化而非真正的 depth signal）值得认真考虑。Section 4.5 将 arXiv 的高 K* 归因于 \"formulaic features (LaTeX formatting, citation patterns, mathematical notation) degrade slowly under autoregressive generation\"——但如果分类器主要检测的是 LaTeX 语法错误的累积（如 \\cite{} 格式在多轮生成中逐渐损坏），而非内容层面的 depth signal，那么 arXiv K*=3 的意义就不同了。\n\n我在 Round 1 审稿中未充分展开这一方向，R1 的分析更深入。建议论文：(a) 对 arXiv 数据做 LaTeX markup 去除后的 ablation，验证 K*=3 是否依赖格式特征；(b) 或坦率承认 \"structural complexity\" 是经验性术语，并给出可测量的 proxy（如 vocabulary entropy、格式标记密度）。\n\n---\n\n**[REBUT] R1-W6: 跨模型迁移 \"80–92%\" 掩盖绝对精度低（~0.35）**\n\n部分反驳。R1 认为 80–92% retention rate 掩盖了 6-class 绝对精度低（~0.35），这在字面上是正确的，但误解了论文的 metric 设计意图。\n\nK* 的核心度量是 pairwise AUC（相邻代际的二分类能力），而非 6-class ordinal accuracy。Table S1 的 6-class accuracy 确实低（diagonal ~0.38–0.42），但这恰恰是 K*=2 的预期结果——深度 2+ 不可区分，所以 6-class 必然接近 3-class（depth 0, 1, 2+）的上限。论文用 transfer retention rate（off-diagonal / diagonal）衡量跨模型迁移是合理的，因为它控制了任务难度的基线。\n\n但 R1 的关切仍有一定合理性：Abstract 说 \"80–92% cross-model transfer\" 而不解释这是 retention rate 而非 absolute accuracy，对不熟悉此 metric 的读者确实可能造成误导。建议 Abstract 和 Contribution (c) 明确说明 \"80–92% accuracy retention\"。\n\n---\n\n**[AGREE] R1-W7: arXiv 与 C4 样本量差异对 CI 的影响**\n\n同意。Appendix I (Section boundary_extended) 中 C4 子采样至 n=2,200 后 K* 降至 1（1v2 AUC=0.601, CI [0.586, 0.616]），说明 C4 K*=2 在小样本下 fragile。论文将此解释为 \"arXiv K*=3 at the same sample size reflects genuine domain signal rather than statistical artifact\"——这一推理方向是对的（arXiv 在同样小样本下仍为 K*=3），但同时也暴露 C4 K*=2 的效应量在实际部署（可能面临小样本）时并不稳健。\n\n论文应在 Limitations 中更明确讨论 sample size 对 K*=2 判定的影响：至少需要多少样本才能 reliably 判定 K*=2？这对实践部署至关重要。\n\n---\n\n### Questions\n\n**[AGREE] R1-Q1: OBD vs. multiclass LightGBM 缺乏统计检验**\n\nSection 3.2 报告 MAE 差异（0.984 vs. 1.016）和 pairwise AUC 差异（0.6095 vs. 0.4883 for OLR），但未提供 OBD vs. multiclass LightGBM 的配对统计检验（如 paired t-test across folds）。这是一个小但合理的遗漏。\n\n---\n\n**[AGREE] R1-Q2: ANOVA 设计的 fold 非独立性**\n\nTable 7 caption 说 N=300（12 cells × 5 folds × 5 depth-pairs; 3 generators × 4 scorers）。使用 per-fold AUC 作为 DV 时，同一 GroupKFold 划分的不同 fold 之间的 AUC 值并非完全独立（共享数据划分结构）。这可能导致 F-test 的 Type I error inflation。虽然主要结论（Depth-Pair 主导方差）不太可能受影响，但 Scorer 的显著性判断可能被高估。R1 的质疑有统计基础。\n\n---\n\n**[AGREE] R1-Q3: Retrain-chain K*≥4 vs prompt-chain K*=2 的适用性**\n\n这也是我在 Round 1 中提出的问题（Q3）。Prompt-chain 隔离了 text-level degradation，但实际 web 污染更可能涉及 retrain-chain（模型在前代输出上微调后生成新内容）。Retrain-chain K*≥4 (Appendix E, Table 6) 意味着 depth estimation 在那种场景下有更大价值，但论文的主体实验全部基于 prompt-chain。\n\n论文在 Limitations (2) 和 Discussion 中承认了这一点，但措辞较轻。R1 和我对此的关切一致：论文应更明确讨论 prompt-chain K* 对实际部署场景的适用性边界。\n\n---\n\n**[AGREE] R1-Q4: Zero-shot baseline 的 prompt 和 input 细节**\n\nTable S3 (LLM Zero-Shot) 报告了 GPT-5.5 和 Claude Opus 4.6 的混淆矩阵，但论文主体和附录中均未找到具体的 prompt template、input format、是否提供 few-shot examples 等关键细节。这影响 reproducibility。\n\n---\n\n**[AGREE] R1-Q5: 为什么没讨论 watermarking**\n\nR1 和我（Missing References 第 1 条）都独立指出了这一遗漏。Watermarking（Kirchenbauer et al. 2023）提供了一种 proactive 的合成文本追踪范式，与本文的 post-hoc detection 形成互补。Related Work 中完全不讨论 watermarking 是一个显著遗漏，尤其是在 EMNLP 社区近年来 watermarking 文献大量增长的背景下。\n\n---\n\n### Missing References\n\n**[AGREE] Kirchenbauer et al. (2023) watermarking**：与我的 Missing References 第 1 条一致。必须引用。\n\n**[AGREE] Penedo et al. FineWeb/RefinedWeb**：与我的 Missing References 第 4 条一致。Data curation 实践的重要工作，Related Work \"Data selection and curation\" 段（目前仅 2 行）需要扩展。\n\n**[AGREE with caveat] 更多 ordinal classification 文献**：合理建议，但影响较小。论文的 OBD 方法直接引用了 Frank & Hall (2001)，对于 ordinal classification 的更广泛文献（如 Gutierrez et al. 2016 survey, Diaz & Athey 2019 等），由于论文并非 ordinal classification 方法论文，引用 1-2 篇 survey 即可，无需大量补充。\n\n---\n\n### 总结：R2 与 R1 的一致性和分歧\n\n**高度一致的关键问题（两位 reviewer 独立得出相同结论）：**\n\n1. **下游 filtering 效应量过小**（R1-W3 ≈ R2-W2/W3）：这是论文最大的实践层面弱点。两位 reviewer 均认为 filtering 实验难以支撑 contribution 级别的 claim\n2. **Watermarking 引用缺失**（R1-Q5/Missing Refs ≈ R2-Missing Refs #1）：一致认为是重要遗漏\n3. **Retrain-chain 适用性**（R1-Q3 ≈ R2-Q3）：一致质疑 prompt-chain K* 的实际场景覆盖度\n4. **引用密度偏低**（R1-Missing Refs ≈ R2-W4）\n\n**R1 独有且 R2 同意的重要发现：**\n\n5. **θ 阈值三重论证包装过度**（R1-W1）：R1 的分析比我更到位，我在 Round 1 中未专门展开此问题\n6. **\"Generator-independent\" 措辞矛盾**（R1-W2）：R1 上升到术语层面的批评比我的 marginal boundary 关切更系统\n7. **DPI 引用精度**（R1-W4）和 **\"structural complexity\" 操作化缺失**（R1-W5）：R1 发现了我未充分覆盖的理论/概念层问题\n\n**R2 独有的关切（R1 未充分覆盖）：**\n\n8. **方法技术新颖性不足**（R2-W1）：R1 未将此列为 weakness——我认为这是论文在 main conference 层面的核心短板\n9. **论文身份不清**（R2-W5）：measurement vs. detection vs. curation 的三重定位问题\n10. **Qwen 过度代表**（R2-W7）\n\n**唯一分歧：R1-W6（transfer retention rate 掩盖低绝对精度）**\n\n我部分反驳了这一点。Retention rate 作为 transfer 度量是合理的（控制了任务难度），但同意 Abstract 表述可能误导。\n\n**评分一致性：** 两位 reviewer 均给 3.0 (Findings)，confidence 均为 high。这一高度一致性表明论文的问题是系统性的，非单一 reviewer 的偏好。",
  "reviewer_id": "2",
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30c9c486-7079-46c9-95b5-1a8bb4ed2371",
  "isSidechain": false,
  "requestId": "req_011Cb9qtadbwTat46kCBVDpt",
  "type": "assistant",
  "uuid": "4527b1c2-d5cd-4e30-b1d4-46aafd7ae59e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVNoVzgE9tkmLCH3XEDL7r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2049,
      "cache_read_input_tokens": 102237,
      "output_tokens": 5954,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2049,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5954,
          "cache_read_input_tokens": 102237,
          "cache_creation_input_tokens": 2049,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2049
          },
          "type": "message"
        }
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

_source line 113_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Step 2: 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见  以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Weakness、Question 和 Missing Reference： - **[AGREE]**：同意并说明理由（可补充你自己的发现） - **[REBUT]**：反驳并提供证据（cite 具体 Section/T…",
  "leafUuid": "4527b1c2-d5cd-4e30-b1d4-46aafd7ae59e",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Runtime record

_source line 114_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on generational depth contamination detection",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Tool result

_source line 115 · 2026-05-18T10:05:40.592Z_

<details><summary>↩ Tool result · `toolu_014M8ZmKrcy7jgVsjKPNkwt8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4527b1c2-d5cd-4e30-b1d4-46aafd7ae59e",
  "isSidechain": false,
  "promptId": "45562aac-6eb0-4db0-8447-1b023d1e76ac",
  "type": "user",
  "uuid": "39c28227-1a9e-47ca-a110-31cd0d92065f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "4527b1c2-d5cd-4e30-b1d4-46aafd7ae59e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 116_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on generational depth contamination detection",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Runtime record

_source line 117 · 2026-05-18T14:29:52.308Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T14:29:52.308Z",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "content": "[Round 2 审稿请求]:\n## Round 2（修订评估）— Reviewer 2\n\n**模式**: 继续审稿。论文已更新，你的任务是逐条检查上轮 issue 是否已充分解决，并识别修改是否引入新问题。\n\n### Venue 信息\n- EMNLP 2026, ARR May 2026, Deadline 2026-05-25\n- ACL 双栏模板 [review], Long paper 8 页, Double-blind\n- 评分: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit\n\n### 论文路径\n- 主文件: `projects/gen-depth-contamination/docs/paper/main.tex`\n- 分节: introduction.tex, related_work.tex, method.tex, experiments_c1.tex, experiments_c3.tex, discussion.tex, conclusion.tex\n- 附录: appendix.tex, appendix_extended.tex\n- 表格: tables/ 目录\n\n### 你的侧重：新颖性 + 完整性\n\n**上轮报告评分**: 3.0 (Findings)\n\n### 必须逐条检查的 Issue 列表（你的侧重）\n\n对每条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 具体理由（cite Section/Table/Figure）。\n\n#### Critical Issues\n\n**FR7-N2** Related Work 遗漏重要引用\n- 上轮要求：必须补充 watermarking 段（Kirchenbauer 2023 + proactive vs post-hoc）和 data curation 段（FineWeb）。至少补充 4-6 篇引用\n- 检查点：Related Work 是否新增 watermarking 段？FineWeb/Penedo 是否被引用？Gehrmann (GLTR) 是否被引用？引用总数是否从 34 增加？Section 2 行数是否增加？\n\n**FR7-N4** K*=2 的 negative result 性质未被正面讨论\n- 上轮要求：Discussion 更诚实讨论 K*=2 implications；强调 arXiv K*=3 和 retrain-chain K*≥4 的正面结果\n- 检查点：Discussion 是否有新段落讨论 K*=2 的 measurement value / domain diagnostic / prescriptive implications？\n\n#### Major Issues\n\n**FR7-W1** 论文定位不清 (measurement/detection/curation)\n- 上轮要求：Contribution list 重组为 primary(measurement) + secondary(transfer) + tertiary(validation)\n- 检查点：Introduction contribution list 是否重组？filtering 是否从独立 contribution 降级为 validation？\n\n**FR7-W2** 与 Drayson et al. 区分不足\n- 上轮要求：Discussion 更明确说明相对 Drayson 的增量（binary-sufficiency 定量证据 + 域依赖性洞察）\n- 检查点：Discussion 或 Related Work 是否有新的 Drayson positioning 内容？\n\n**FR8-W5** Watermarking 完全未讨论\n- 上轮要求：Related Work 增加 watermarking 段\n- 检查点：与 FR7-N2 一起检查\n\n#### Minor Issues\n\n**FR8-W2** Abstract 数字堆砌\n- 上轮要求：精简至 2-3 个关键数字\n- 检查点：Abstract 数字数量是否减少？word count？\n\n**FR8-W3** Qwen 过度代表\n- 上轮要求：Limitations 更明确承认\n- 检查点：Limitations 是否新增 Qwen 相关内容？\n\n**FR8-W4** 80-92% 未说明为 retention rate\n- 上轮要求：Abstract/Contribution 明确说明 \"accuracy retention\"\n- 检查点：Abstract 的 80-92% 是否加了 \"retention\" 说明？\n\n### 额外审查要求\n\n1. **写作质量检查**：修改后是否引入了新的 AI 写作痕迹（em-dash、-ing phrases、过度分段）？\n2. **主线统一性**：修改是否破坏了 Abstract → Introduction → Method → Results → Discussion → Conclusion 的叙事一致性？\n3. **引用密度**：总引用数？新增引用是否有正确的 positioning？\n4. **页数检查**：修改后是否超过 8 页正文限制？\n\n### 输出格式\n\n```\n## Issue Resolution Status\n\n### Critical\nFR7-N2: [RESOLVED/STILL_OPEN] — 理由...\nFR7-N4: [RESOLVED/STILL_OPEN] — 理由...\n\n### Major\nFR7-W1: [RESOLVED/STILL_OPEN] — 理由...\n...\n\n### Minor\nFR8-W2: [RESOLVED/STILL_OPEN] — 理由...\n...\n\n## Writing Quality Check\n（新引入的 AI 痕迹？主线统一性？引用密度？页数？）\n\n## New Issues（修改引入的新问题，如有）\nN1. ...\n\n## Overall Assessment Update\n上轮: 3.0 (Findings)\n本轮: X.X — 理由...\n```"
}
````

---


### Runtime record

_source line 118 · 2026-05-18T14:29:52.308Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T14:29:52.308Z",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


## Round 4

## Round 4

2 recorded events


### User

_source line 119 · 2026-05-18T14:29:52.299Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39c28227-1a9e-47ca-a110-31cd0d92065f",
  "isSidechain": false,
  "promptId": "a76e3a98-645a-445f-972e-aeb6711b75d1",
  "type": "user",
  "isMeta": true,
  "uuid": "23f068f0-cd6f-4752-95be-4d114df6eace",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 120 · 2026-05-18T14:29:52.299Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23f068f0-cd6f-4752-95be-4d114df6eace",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "8225df5f-398b-4f36-8316-3571626a19ad",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "07522930-0ee1-4597-8a95-e8b2daecf544",
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


## Round 5

## Round 5

45 recorded events


### User

_source line 121 · 2026-05-18T14:29:52.396Z_

[Round 2 审稿请求]:
## Round 2（修订评估）— Reviewer 2

**模式**: 继续审稿。论文已更新，你的任务是逐条检查上轮 issue 是否已充分解决，并识别修改是否引入新问题。

### Venue 信息
- EMNLP 2026, ARR May 2026, Deadline 2026-05-25
- ACL 双栏模板 [review], Long paper 8 页, Double-blind
- 评分: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit

### 论文路径
- 主文件: `projects/gen-depth-contamination/docs/paper/main.tex`
- 分节: introduction.tex, related_work.tex, method.tex, experiments_c1.tex, experiments_c3.tex, discussion.tex, conclusion.tex
- 附录: appendix.tex, appendix_extended.tex
- 表格: tables/ 目录

### 你的侧重：新颖性 + 完整性

**上轮报告评分**: 3.0 (Findings)

### 必须逐条检查的 Issue 列表（你的侧重）

对每条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 具体理由（cite Section/Table/Figure）。

#### Critical Issues

**FR7-N2** Related Work 遗漏重要引用
- 上轮要求：必须补充 watermarking 段（Kirchenbauer 2023 + proactive vs post-hoc）和 data curation 段（FineWeb）。至少补充 4-6 篇引用
- 检查点：Related Work 是否新增 watermarking 段？FineWeb/Penedo 是否被引用？Gehrmann (GLTR) 是否被引用？引用总数是否从 34 增加？Section 2 行数是否增加？

**FR7-N4** K*=2 的 negative result 性质未被正面讨论
- 上轮要求：Discussion 更诚实讨论 K*=2 implications；强调 arXiv K*=3 和 retrain-chain K*≥4 的正面结果
- 检查点：Discussion 是否有新段落讨论 K*=2 的 measurement value / domain diagnostic / prescriptive implications？

#### Major Issues

**FR7-W1** 论文定位不清 (measurement/detection/curation)
- 上轮要求：Contribution list 重组为 primary(measurement) + secondary(transfer) + tertiary(validation)
- 检查点：Introduction contribution list 是否重组？filtering 是否从独立 contribution 降级为 validation？

**FR7-W2** 与 Drayson et al. 区分不足
- 上轮要求：Discussion 更明确说明相对 Drayson 的增量（binary-sufficiency 定量证据 + 域依赖性洞察）
- 检查点：Discussion 或 Related Work 是否有新的 Drayson positioning 内容？

**FR8-W5** Watermarking 完全未讨论
- 上轮要求：Related Work 增加 watermarking 段
- 检查点：与 FR7-N2 一起检查

#### Minor Issues

**FR8-W2** Abstract 数字堆砌
- 上轮要求：精简至 2-3 个关键数字
- 检查点：Abstract 数字数量是否减少？word count？

**FR8-W3** Qwen 过度代表
- 上轮要求：Limitations 更明确承认
- 检查点：Limitations 是否新增 Qwen 相关内容？

**FR8-W4** 80-92% 未说明为 retention rate
- 上轮要求：Abstract/Contribution 明确说明 "accuracy retention"
- 检查点：Abstract 的 80-92% 是否加了 "retention" 说明？

### 额外审查要求

1. **写作质量检查**：修改后是否引入了新的 AI 写作痕迹（em-dash、-ing phrases、过度分段）？
2. **主线统一性**：修改是否破坏了 Abstract → Introduction → Method → Results → Discussion → Conclusion 的叙事一致性？
3. **引用密度**：总引用数？新增引用是否有正确的 positioning？
4. **页数检查**：修改后是否超过 8 页正文限制？

### 输出格式

```
## Issue Resolution Status

### Critical
FR7-N2: [RESOLVED/STILL_OPEN] — 理由...
FR7-N4: [RESOLVED/STILL_OPEN] — 理由...

### Major
FR7-W1: [RESOLVED/STILL_OPEN] — 理由...
...

### Minor
FR8-W2: [RESOLVED/STILL_OPEN] — 理由...
...

## Writing Quality Check
（新引入的 AI 痕迹？主线统一性？引用密度？页数？）

## New Issues（修改引入的新问题，如有）
N1. ...

## Overall Assessment Update
上轮: 3.0 (Findings)
本轮: X.X — 理由...
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8225df5f-398b-4f36-8316-3571626a19ad",
  "isSidechain": false,
  "promptId": "a76e3a98-645a-445f-972e-aeb6711b75d1",
  "type": "user",
  "uuid": "7e490c5b-c924-45f9-a8e3-8cbebca18ba8",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 122 · 2026-05-18T14:30:00.200Z_

开始 Round 2 审稿。重新读取所有修改后的论文文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e490c5b-c924-45f9-a8e3-8cbebca18ba8",
  "isSidechain": false,
  "requestId": "req_011CbACCvsMCEqjH5hUV5FY5",
  "type": "assistant",
  "uuid": "809fa7bb-de81-4711-b1fe-748e7d6db314",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECzDnd2j5NdSKnjmmowK97",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 100323,
      "cache_read_input_tokens": 11841,
      "output_tokens": 621,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 100323,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 621,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 100323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 100323
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool call

_source line 123 · 2026-05-18T14:30:01.636Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P52pSy2iAiXyZ5zQ1AdmsJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "809fa7bb-de81-4711-b1fe-748e7d6db314",
  "isSidechain": false,
  "requestId": "req_011CbACCvsMCEqjH5hUV5FY5",
  "type": "assistant",
  "uuid": "7030055c-05f0-43e1-86f9-90d9c93966dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECzDnd2j5NdSKnjmmowK97",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 100323,
      "cache_read_input_tokens": 11841,
      "output_tokens": 621,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 100323,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 621,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 100323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 100323
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 124 · 2026-05-18T14:30:01.647Z_

<details><summary>↩ Tool result · `toolu_01P52pSy2iAiXyZ5zQ1AdmsJ`</summary>

```text
1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	\usepackage[section]{placeins}
18	
19	\newcommand{\Kstar}{{K^*}}
20	\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
21	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
22	\newcommand{\auc}{\text{AUC}}
23	\newcommand{\jsd}{\text{JSD}}
24	
25	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	% === Abstract ===
33	\begin{abstract}
34	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
35	We measure the discrimination boundary $\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable) using 15 statistical features and an OBD-LightGBM classifier.
36	Across five architecture families (1B--14B), three source domains, and four decoding strategies at $\theta{=}0.60$, $\Kempirical{=}2$ for general web text (8/9 model configurations) and $\Kempirical{=}3$ for structured academic text (arXiv).
37	A single generation pass suffices to render general web text indistinguishable from deeper synthetic content, a \emph{one-wash laundering} effect.
38	Generator-independent statistical features, computed via a fixed reference scorer, enable 80--92\% accuracy retention among continuation-mode generators, and cross-scorer validation is consistent with $\Kempirical$ being governed by the generation process rather than the scoring model.
39	Downstream, domain-appropriate $\Kempirical$ correctly predicts optimal curation granularity: when contamination causes detectable quality loss, binary filtering minimizes degradation most effectively for web text.
40	\end{abstract}
41	
42	% === Section 1: Introduction ===
43	\input{introduction}
44	
45	% === Section 2: Related Work ===
46	\input{related_work}
47	
48	% === Section 3: Method ===
49	\input{method}
50	
51	% === Section 4: Experiments ===
52	\input{experiments_c1}
53	
54	% === Section 5: K*-Aware Data Filtering ===
55	\input{experiments_c3}
56	
57	% === Section 6: Discussion ===
58	\input{discussion}
59	
60	% === Section 7: Conclusion ===
61	\input{conclusion}
62	
63	% === Limitations (ACL required, unnumbered) ===
64	\clearpage
65	\section*{Limitations}
66	
67	Our findings are bounded by:
68	(1)~\emph{Scope}: model scale $\leq$14B (5 architecture families), English text (C4, Wikipedia, arXiv), four decoding strategies; arXiv $\Kempirical{=}3$ is confirmed with five models across four architecture families but with reduced sample size ($n{=}2{,}200$ per model); subsampling analysis indicates $n{\geq}2{,}500$ suffices for 100\% reliable $\Kempirical$ determination (Appendix~\ref{sec:power_curve}).
69	(2)~\emph{Protocol}: all main experiments use prompt-chain, which isolates text-intrinsic degradation from training dynamics; real-world contamination involves both prompting and retraining, and retrain-chain yields $\Kempirical{\geq}4$ (Pythia-1.4B LoRA; Appendix~\ref{sec:extended_limitations}), so prompt-chain $\Kempirical$ may underestimate discriminability in mixed settings.
70	(3)~\emph{Threshold}: $\Kempirical$ ranges from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; 8/9 configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (Mistral-7B: $\Kempirical{=}1$).
71	(4)~\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.002; cross-scorer validation drops this to $\Kempirical{=}1$ (Section~\ref{sec:transfer}). LLaMA-3.1-8B represents the most marginal $\Kempirical{=}2$ assignment, with the 1v2 CI lower bound within 0.3 percentage points of $\theta$.
72	(5)~\emph{Feature set}: the 15D features yield a feature-set-specific lower bound ($\Ktheory$ may be strictly higher); neural probe $\Kempirical$ is model-dependent ($3$ for Qwen, $2$ for Pythia/OLMo).
73	(6)~\emph{Segment length}: $\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \theta$); 512 tokens yields point estimate $\Kempirical{=}2$ but CI lower marginally below $\theta$ ($0.5979$), indicating the boundary weakens at longer generation lengths.
74	(7)~\emph{Curation applicability}: the filtering evaluation is validated on two architectures (Qwen2.5-1.5B-Instruct and Pythia-1.4B) with consistent strategy ordering (Appendix~\ref{sec:pythia_filtering}), though absolute improvement remains small and effect sizes diminish at lower contamination ratios (10--50\%; Appendix~\ref{sec:dose_response}).
75	(8)~\emph{Family balance}: the Qwen2.5 family provides 5/9 configurations; though spanning three scales (1.5B, 7B, 14B) and two training variants (base, instruct), aggregate statistics weight this family more heavily than the four single-configuration families.
76	Additional limitations (cross-model scoring sensitivity, feature ranking variability at the 1v2 boundary, structural composition confound analysis) appear in Appendix~\ref{sec:extended_limitations}.
77	
78	% === Ethics Statement (ACL required, unnumbered) ===
79	\section*{Ethics Statement}
80	
81	Generational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.
82	Our experiments use publicly available corpora (C4, Wikipedia, arXiv abstracts) and do not involve personally identifiable information.
83	A potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\auc \geq 0.96$ at 0v1) remains robust.
84	Code and generated corpora will be released upon acceptance to enable reproducibility.
85	
86	\bibliography{references}
87	
88	\input{appendix}
89	\input{appendix_extended}
90	
91	\end{document}
92	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7030055c-05f0-43e1-86f9-90d9c93966dc",
  "isSidechain": false,
  "promptId": "a76e3a98-645a-445f-972e-aeb6711b75d1",
  "type": "user",
  "uuid": "6c5f6159-4265-4239-88c1-d72d47f00584",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
      "content": "% EMNLP 2026 Main — ARR May 2026\n% Generational Depth Contamination\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\\usepackage[section]{placeins}\n\n\\newcommand{\\Kstar}{{K^*}}\n\\newcommand{\\Kempirical}{{K^*_{\\text{empirical}}}}\n\\newcommand{\\Ktheory}{{K^*_{\\text{theory}}}}\n\\newcommand{\\auc}{\\text{AUC}}\n\\newcommand{\\jsd}{\\text{JSD}}\n\n\\title{Generational Depth Estimation of Recursive Synthetic Text:\\\\Measuring the Discrimination Boundary}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% === Abstract ===\n\\begin{abstract}\nWeb-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.\nWe measure the discrimination boundary $\\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable) using 15 statistical features and an OBD-LightGBM classifier.\nAcross five architecture families (1B--14B), three source domains, and four decoding strategies at $\\theta{=}0.60$, $\\Kempirical{=}2$ for general web text (8/9 model configurations) and $\\Kempirical{=}3$ for structured academic text (arXiv).\nA single generation pass suffices to render general web text indistinguishable from deeper synthetic content, a \\emph{one-wash laundering} effect.\nGenerator-independent statistical features, computed via a fixed reference scorer, enable 80--92\\% accuracy retention among continuation-mode generators, and cross-scorer validation is consistent with $\\Kempirical$ being governed by the generation process rather than the scoring model.\nDownstream, domain-appropriate $\\Kempirical$ correctly predicts optimal curation granularity: when contamination causes detectable quality loss, binary filtering minimizes degradation most effectively for web text.\n\\end{abstract}\n\n% === Section 1: Introduction ===\n\\input{introduction}\n\n% === Section 2: Related Work ===\n\\input{related_work}\n\n% === Section 3: Method ===\n\\input{method}\n\n% === Section 4: Experiments ===\n\\input{experiments_c1}\n\n% === Section 5: K*-Aware Data Filtering ===\n\\input{experiments_c3}\n\n% === Section 6: Discussion ===\n\\input{discussion}\n\n% === Section 7: Conclusion ===\n\\input{conclusion}\n\n% === Limitations (ACL required, unnumbered) ===\n\\clearpage\n\\section*{Limitations}\n\nOur findings are bounded by:\n(1)~\\emph{Scope}: model scale $\\leq$14B (5 architecture families), English text (C4, Wikipedia, arXiv), four decoding strategies; arXiv $\\Kempirical{=}3$ is confirmed with five models across four architecture families but with reduced sample size ($n{=}2{,}200$ per model); subsampling analysis indicates $n{\\geq}2{,}500$ suffices for 100\\% reliable $\\Kempirical$ determination (Appendix~\\ref{sec:power_curve}).\n(2)~\\emph{Protocol}: all main experiments use prompt-chain, which isolates text-intrinsic degradation from training dynamics; real-world contamination involves both prompting and retraining, and retrain-chain yields $\\Kempirical{\\geq}4$ (Pythia-1.4B LoRA; Appendix~\\ref{sec:extended_limitations}), so prompt-chain $\\Kempirical$ may underestimate discriminability in mixed settings.\n(3)~\\emph{Threshold}: $\\Kempirical$ ranges from 2--3 at $\\theta{=}0.55$ to 1 at $\\theta{=}0.70$; 8/9 configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (Mistral-7B: $\\Kempirical{=}1$).\n(4)~\\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.002; cross-scorer validation drops this to $\\Kempirical{=}1$ (Section~\\ref{sec:transfer}). LLaMA-3.1-8B represents the most marginal $\\Kempirical{=}2$ assignment, with the 1v2 CI lower bound within 0.3 percentage points of $\\theta$.\n(5)~\\emph{Feature set}: the 15D features yield a feature-set-specific lower bound ($\\Ktheory$ may be strictly higher); neural probe $\\Kempirical$ is model-dependent ($3$ for Qwen, $2$ for Pythia/OLMo).\n(6)~\\emph{Segment length}: $\\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \\theta$); 512 tokens yields point estimate $\\Kempirical{=}2$ but CI lower marginally below $\\theta$ ($0.5979$), indicating the boundary weakens at longer generation lengths.\n(7)~\\emph{Curation applicability}: the filtering evaluation is validated on two architectures (Qwen2.5-1.5B-Instruct and Pythia-1.4B) with consistent strategy ordering (Appendix~\\ref{sec:pythia_filtering}), though absolute improvement remains small and effect sizes diminish at lower contamination ratios (10--50\\%; Appendix~\\ref{sec:dose_response}).\n(8)~\\emph{Family balance}: the Qwen2.5 family provides 5/9 configurations; though spanning three scales (1.5B, 7B, 14B) and two training variants (base, instruct), aggregate statistics weight this family more heavily than the four single-configuration families.\nAdditional limitations (cross-model scoring sensitivity, feature ranking variability at the 1v2 boundary, structural composition confound analysis) appear in Appendix~\\ref{sec:extended_limitations}.\n\n% === Ethics Statement (ACL required, unnumbered) ===\n\\section*{Ethics Statement}\n\nGenerational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.\nOur experiments use publicly available corpora (C4, Wikipedia, arXiv abstracts) and do not involve personally identifiable information.\nA potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\\auc \\geq 0.96$ at 0v1) remains robust.\nCode and generated corpora will be released upon acceptance to enable reproducibility.\n\n\\bibliography{references}\n\n\\input{appendix}\n\\input{appendix_extended}\n\n\\end{document}\n",
      "numLines": 92,
      "startLine": 1,
      "totalLines": 92
    }
  },
  "sourceToolAssistantUUID": "7030055c-05f0-43e1-86f9-90d9c93966dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-18T14:30:05.062Z_

<details><summary>↩ Tool result · `toolu_01Uf2Dd3XRB95mbg3PtcpNpf`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We measure the generational depth discrimination boundary $\Kempirical$ for recursive synthetic text.
5	$\Kempirical \in \{1, 2, 3\}$ depends on source domain and model characteristics: general web text yields $\Kempirical{=}2$ across 8/9 configurations (5 families, 1B--14B; $p \leq 0.002$), with $\Kempirical{=}3$ for academic text, confirmed across five models and four architecture families.
6	Generator-independent features enable 80--92\% accuracy retention across generators ($\rho > 0.90$), making $\Kempirical$ measurement practical without generator-specific training.
7	As downstream validation, $\Kempirical{=}2$ supports binary filtering as the optimal granularity for web text: graduated depth weighting cannot exploit information that does not exist beyond the discrimination boundary.
8	$\Kempirical$ provides a representation-dependent lower bound on discriminable depth; the gap to $\Ktheory$ may narrow with richer features, scaling beyond 14B, and retrain-chain characterization.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a9718b3-dbbe-4dd3-a8f2-e3831ef06163",
  "isSidechain": false,
  "promptId": "a76e3a98-645a-445f-972e-aeb6711b75d1",
  "type": "user",
  "uuid": "e1f6819a-a25f-4179-a893-7d85350a8b68",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe measure the generational depth discrimination boundary $\\Kempirical$ for recursive synthetic text.\n$\\Kempirical \\in \\{1, 2, 3\\}$ depends on source domain and model characteristics: general web text yields $\\Kempirical{=}2$ across 8/9 configurations (5 families, 1B--14B; $p \\leq 0.002$), with $\\Kempirical{=}3$ for academic text, confirmed across five models and four architecture families.\nGenerator-independent features enable 80--92\\% accuracy retention across generators ($\\rho > 0.90$), making $\\Kempirical$ measurement practical without generator-specific training.\nAs downstream validation, $\\Kempirical{=}2$ supports binary filtering as the optimal granularity for web text: graduated depth weighting cannot exploit information that does not exist beyond the discrimination boundary.\n$\\Kempirical$ provides a representation-dependent lower bound on discriminable depth; the gap to $\\Ktheory$ may narrow with richer features, scaling beyond 14B, and retrain-chain characterization.\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "5a9718b3-dbbe-4dd3-a8f2-e3831ef06163",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-18T14:30:02.100Z_

<details open><summary>🔧 Tool call — Read · `toolu_017HiefYJFtHsZfbHqtgEj4H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c5f6159-4265-4239-88c1-d72d47f00584",
  "isSidechain": false,
  "requestId": "req_011CbACCvsMCEqjH5hUV5FY5",
  "type": "assistant",
  "uuid": "884af575-346e-4a12-b7e3-7e0fe2d2490c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECzDnd2j5NdSKnjmmowK97",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 100323,
      "cache_read_input_tokens": 11841,
      "output_tokens": 621,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 100323,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 621,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 100323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 100323
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-18T14:30:02.109Z_

<details><summary>↩ Tool result · `toolu_017HiefYJFtHsZfbHqtgEj4H`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.
9	
10	This gap cuts across multiple communities: binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}), membership inference~\cite{zawalski2026codec} addresses a different question, and the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool.
11	Data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} likewise ignore recursive depth.
12	No existing method estimates how many rounds of recursive generation a text has undergone.
13	
14	Knowing whether the discriminable depth is finite, and where it saturates, has direct practical consequences.
15	For data curation, the saturation point determines filtering granularity: if discrimination collapses at depth 2, graduated weighting beyond that boundary injects noise, and binary filtering becomes the principled choice.
16	Model collapse theory predicts monotonic quality degradation across generations, but existing analyses are population-level and provide no per-text measure of where degradation saturates.
17	$\Kempirical$ fills this gap by localizing the generation at which adjacent outputs become empirically indistinguishable.
18	
19	The Data Processing Inequality implies that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
20	We empirically measure $\Kempirical$ (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features computed via a fixed reference scorer (Section~\ref{sec:features}) and an Ordinal Binary Decomposition (OBD) LightGBM classifier.
21	We operationalize $\Kempirical$ as the deepest $k \geq 1$ where the pairwise $\auc_{k-1,k}$ exceeds $\theta = 0.60$ (Section~\ref{sec:formulation}).
22	
23	Our contributions:
24	\begin{enumerate}[label=(\alph*),nosep]
25	  \item \textbf{First empirical measurement of $\Kempirical$} across 9 model configurations (5 architecture families, 1B--14B), 3 source domains, and 4 decoding strategies at $\theta{=}0.60$ ($p \leq 0.002$; Section~\ref{sec:kstar_boundary}).
26	  Both supervised OBD and zero-shot frontier Large Language Models (LLMs) show no statistically significant difference beyond $\Kempirical$ (McNemar $p > 0.05$, $N{=}500$; Section~\ref{sec:why_kstar}).
27	  \item \textbf{Domain ordering invariance}: the hierarchy arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$) is preserved across six models spanning four architecture families, three scales (1B--14B), and four decoding strategies, with $\Kempirical$ consistently varying by source domain (Section~\ref{sec:cross_domain}).
28	  \item \textbf{Practical validation}: generator-independent features enable 80--92\% accuracy retention among continuation-mode generators ($\rho > 0.90$; Section~\ref{sec:transfer}), and $\Kempirical{=}2$ correctly predicts binary filtering as optimal granularity for web text (Section~\ref{sec:filtering}).
29	\end{enumerate}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "884af575-346e-4a12-b7e3-7e0fe2d2490c",
  "isSidechain": false,
  "promptId": "a76e3a98-645a-445f-972e-aeb6711b75d1",
  "type": "user",
  "uuid": "c695039c-2a6c-4f40-b95e-a10444bfd265",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.\nEstimates suggest that a substantial fraction of online text is machine-generated~\\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.\nWhen models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\\cite{shumailov2024collapse, dohmatob2024model}.\nThis degradation arises in both \\emph{retrain-chains} (iteratively training on model outputs) and \\emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\\ref{sec:extended_limitations}).\nYet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.\n\nThis gap cuts across multiple communities: binary detectors~\\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\\ref{sec:binary_confidence}), membership inference~\\cite{zawalski2026codec} addresses a different question, and the model collapse literature~\\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool.\nData selection methods~\\cite{xie2023dsir, tirumala2023d4, drayson2025} likewise ignore recursive depth.\nNo existing method estimates how many rounds of recursive generation a text has undergone.\n\nKnowing whether the discriminable depth is finite, and where it saturates, has direct practical consequences.\nFor data curation, the saturation point determines filtering granularity: if discrimination collapses at depth 2, graduated weighting beyond that boundary injects noise, and binary filtering becomes the principled choice.\nModel collapse theory predicts monotonic quality degradation across generations, but existing analyses are population-level and provide no per-text measure of where degradation saturates.\n$\\Kempirical$ fills this gap by localizing the generation at which adjacent outputs become empirically indistinguishable.\n\nThe Data Processing Inequality implies that information degrades monotonically across generations, motivating a finite discrimination boundary $\\Kstar$.\nWe empirically measure $\\Kempirical$ (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features computed via a fixed reference scorer (Section~\\ref{sec:features}) and an Ordinal Binary Decomposition (OBD) LightGBM classifier.\nWe operationalize $\\Kempirical$ as the deepest $k \\geq 1$ where the pairwise $\\auc_{k-1,k}$ exceeds $\\theta = 0.60$ (Section~\\ref{sec:formulation}).\n\nOur contributions:\n\\begin{enumerate}[label=(\\alph*),nosep]\n  \\item \\textbf{First empirical measurement of $\\Kempirical$} across 9 model configurations (5 architecture families, 1B--14B), 3 source domains, and 4 decoding strategies at $\\theta{=}0.60$ ($p \\leq 0.002$; Section~\\ref{sec:kstar_boundary}).\n  Both supervised OBD and zero-shot frontier Large Language Models (LLMs) show no statistically significant difference beyond $\\Kempirical$ (McNemar $p > 0.05$, $N{=}500$; Section~\\ref{sec:why_kstar}).\n  \\item \\textbf{Domain ordering invariance}: the hierarchy arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $>$ Wikipedia ($\\Kempirical{=}1$) is preserved across six models spanning four architecture families, three scales (1B--14B), and four decoding strategies, with $\\Kempirical$ consistently varying by source domain (Section~\\ref{sec:cross_domain}).\n  \\item \\textbf{Practical validation}: generator-independent features enable 80--92\\% accuracy retention among continuation-mode generators ($\\rho > 0.90$; Section~\\ref{sec:transfer}), and $\\Kempirical{=}2$ correctly predicts binary filtering as optimal granularity for web text (Section~\\ref{sec:filtering}).\n\\end{enumerate}\n",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 30
    }
  },
  "sourceToolAssistantUUID": "884af575-346e-4a12-b7e3-7e0fe2d2490c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-18T14:30:02.576Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JMyMzmoA7wsj63rpq4ciKt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c695039c-2a6c-4f40-b95e-a10444bfd265",
  "isSidechain": false,
  "requestId": "req_011CbACCvsMCEqjH5hUV5FY5",
  "type": "assistant",
  "uuid": "c3e1abf3-53bf-4910-b954-cc20d0cfe529",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECzDnd2j5NdSKnjmmowK97",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 100323,
      "cache_read_input_tokens": 11841,
      "output_tokens": 621,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 100323,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 621,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 100323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 100323
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-18T14:30:02.581Z_

<details><summary>↩ Tool result · `toolu_01JMyMzmoA7wsj63rpq4ciKt`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model}.
6	In the context of diffusion models, \citet{shi2025collapse} trace a generalization-to-memorization transition under iterative synthetic training.
7	\citet{gambetta2024surplexity} propose surplexity, a single surprisal-based collapse indicator; our 15-dimensional feature set captures richer distributional structure and enables cross-model transfer.
8	\citet{amin2025escaping} show that weak-data curation can mitigate collapse, connecting to our filtering evaluation (Section~\ref{sec:filtering}).
9	Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}, making $\Kempirical = 2$ a conservative lower bound.
10	This literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.
11	
12	\paragraph{Beyond binary detection.}
13	Binary detectors~\cite{gehrmann2019gltr, mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate.
14	Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
15	None estimates recursive generation depth.
16	Watermarking~\cite{kirchenbauer2023watermark} embeds detectable signals at generation time but does not apply to text already in the wild.
17	
18	\paragraph{Data selection and curation.}
19	DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, DoReMi~\cite{xie2023doremi}, and FineWeb~\cite{penedo2024fineweb} address corpus quality through domain-aware filtering and deduplication but are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling, a special case when $\Kstar = 1$.
20	
21	\paragraph{Ordinal classification and probing.}
22	Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3e1abf3-53bf-4910-b954-cc20d0cfe529",
  "isSidechain": false,
  "promptId": "a76e3a98-645a-445f-972e-aeb6711b75d1",
  "type": "user",
  "uuid": "dfe6c423-067a-4b9c-a3a4-30dd102b905c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Model collapse and recursive degradation.}\nIterative training on model outputs causes tail-distribution degradation~\\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model}.\nIn the context of diffusion models, \\citet{shi2025collapse} trace a generalization-to-memorization transition under iterative synthetic training.\n\\citet{gambetta2024surplexity} propose surplexity, a single surprisal-based collapse indicator; our 15-dimensional feature set captures richer distributional structure and enables cross-model transfer.\n\\citet{amin2025escaping} show that weak-data curation can mitigate collapse, connecting to our filtering evaluation (Section~\\ref{sec:filtering}).\nOur prompt-chain operates in the replace regime~\\cite{kazdan2025collapse}, making $\\Kempirical = 2$ a conservative lower bound.\nThis literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.\n\n\\paragraph{Beyond binary detection.}\nBinary detectors~\\cite{gehrmann2019gltr, mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate.\nRecent work extends beyond binary labels to collaboration degree~\\cite{cheng2025beyond}, contamination hierarchies~\\cite{mehta2025beyond}, and multigenerator benchmarks~\\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\\cite{hao2025rewrite}; CoDeC~\\cite{zawalski2026codec} addresses contamination via membership inference.\nNone estimates recursive generation depth.\nWatermarking~\\cite{kirchenbauer2023watermark} embeds detectable signals at generation time but does not apply to text already in the wild.\n\n\\paragraph{Data selection and curation.}\nDSIR~\\cite{xie2023dsir}, D4~\\cite{tirumala2023d4}, DoReMi~\\cite{xie2023doremi}, and FineWeb~\\cite{penedo2024fineweb} address corpus quality through domain-aware filtering and deduplication but are depth-agnostic; Drayson et al.~\\cite{drayson2025} combined binary detection with importance resampling, a special case when $\\Kstar = 1$.\n\n\\paragraph{Ordinal classification and probing.}\nOur OBD classifier follows Frank \\& Hall's~\\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  },
  "sourceToolAssistantUUID": "c3e1abf3-53bf-4910-b954-cc20d0cfe529",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-18T14:30:03.048Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ATw63MLgcNeBMnrf2UiPay`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfe6c423-067a-4b9c-a3a4-30dd102b905c",
  "isSidechain": false,
  "requestId": "req_011CbACCvsMCEqjH5hUV5FY5",
  "type": "assistant",
  "uuid": "69631fd7-4153-4e8a-b60d-06aa541082d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECzDnd2j5NdSKnjmmowK97",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 100323,
      "cache_read_input_tokens": 11841,
      "output_tokens": 621,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 100323,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 621,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 100323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 100323
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-18T14:30:03.053Z_

<details><summary>↩ Tool result · `toolu_01ATw63MLgcNeBMnrf2UiPay`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: the original signal degrades monotonically.
17	Together with Markov chain convergence, this motivates a finite $\Ktheory$ beyond which adjacent generations become indistinguishable.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\{k \geq 1 : \auc_{k-1,k} > \theta\},
22	  \label{eq:kstar}
23	\end{equation}
24	where $\auc_{k-1,k}$ is the point-estimate pairwise AUC (Area Under the ROC Curve) and $\theta = 0.60$ is a data-driven operational threshold (motivated below).
25	Bootstrap 95\% confidence intervals (CIs; 1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
26	
27	\paragraph{Threshold choice.}
28	We set $\theta{=}0.60$ as a data-driven operational threshold, chosen at the empirical discontinuity in the AUC distribution (Figure~\ref{fig:kstar_theta}).
29	A 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\,0.55$ and $p < 0.002$ for all boundary comparisons, placing $\theta{=}0.60$ well above the empirical null.
30	$\Kempirical{=}2$ is stable across $\theta \in [0.55, 0.65]$ for all but two marginal configurations (Table~\ref{tab:kstar_ci_extended}): 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, creating a ${\sim}$5--11\,pp discontinuity.
31	Only at extremes does $\Kempirical$ shift: $\theta{=}0.55$ yields $\Kempirical{=}3$ for two Qwen configurations; $\theta{=}0.70$ yields $\Kempirical{=}1$ across all configurations.
32	The downstream filtering evaluation (Section~\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\theta$, avoiding circularity.
33	
34	\subsection{Features and Classifier}
35	\label{sec:features}
36	
37	Each document is characterized by a 15-dimensional feature vector spanning four groups: \emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).
38	All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
39	Self-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.
40	Removing self-BLEU reduces mean $\auc_{1v2}$ by $< 1$\,pp across all models (14D $\Kempirical = 2$ for all 4 configurations; bootstrap CIs in Table~\ref{tab:selfbleu_ablation}); in deployment where depth labels are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted with minimal performance loss.
41	Hand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.
42	
43	We use \emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\text{depth} > k \mid \mathbf{x})$ via LightGBM (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
44	OBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\auc$ (mean 0.6095 vs.\ 0.4883 for ordinal logistic regression).
45	
46	\subsection{Experimental Setup}
47	\label{sec:experimental_setup}
48	
49	We evaluate nine configurations spanning five architecture families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B, Qwen2.5-14B, Pythia-1.4B, OLMo-1B, LLaMA-3.1-8B, and Mistral-7B (all continuation except Qwen-rw).
50	Each uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).
51	Default decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.
52	Continuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.
53	Evaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\auc$ as primary metric.
54	
55	\begin{table}[t]
56	\centering
57	\small
58	\caption{Experimental configurations for depth-chain generation. \textbf{Config}: shorthand identifier; \textbf{Model}: architecture and parameter count; \textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}
59	\label{tab:setup}
60	\resizebox{\columnwidth}{!}{%
61	\begin{tabular}{llcc}
62	\toprule
63	\textbf{Config} & \textbf{Model} & \textbf{Mode} & $N$ \\
64	\midrule
65	Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\
66	Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\
67	Qwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\
68	Pythia    & Pythia-1.4B            & Continuation & 5{,}000 \\
69	OLMo      & OLMo-1B               & Continuation & 5{,}000 \\
70	Qwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\
71	Qwen-14B  & Qwen2.5-14B           & Continuation & 5{,}000 \\
72	LLaMA-8B  & LLaMA-3.1-8B          & Continuation & 5{,}000 \\
73	Mistral   & Mistral-7B            & Continuation & 5{,}000 \\
74	\bottomrule
75	\end{tabular}}
76	\end{table}
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69631fd7-4153-4e8a-b60d-06aa541082d5",
  "isSidechain": false,
  "promptId": "a76e3a98-645a-445f-972e-aeb6711b75d1",
  "type": "user",
  "uuid": "746973c4-462f-4113-8558-a82c13fed8e9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/pipeline.pdf}\n\\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}\n\\label{fig:pipeline}\n\\end{figure*}\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nA generation operator $G_\\delta$ (LLM + decoding strategy $\\delta$) produces successive generations $X \\to Y_1 \\to \\cdots \\to Y_K$, where $Y_k = G_\\delta(Y_{k-1})$ and $Y_0 \\triangleq X$ (Figure~\\ref{fig:pipeline}).\nThis sequence forms a Markov chain.\nBy the Data Processing Inequality, $I(X; Y_1) \\geq I(X; Y_2) \\geq \\cdots \\geq 0$: the original signal degrades monotonically.\nTogether with Markov chain convergence, this motivates a finite $\\Ktheory$ beyond which adjacent generations become indistinguishable.\n\nWe define the operational lower bound:\n\\begin{equation}\n  \\Kempirical = \\max\\{k \\geq 1 : \\auc_{k-1,k} > \\theta\\},\n  \\label{eq:kstar}\n\\end{equation}\nwhere $\\auc_{k-1,k}$ is the point-estimate pairwise AUC (Area Under the ROC Curve) and $\\theta = 0.60$ is a data-driven operational threshold (motivated below).\nBootstrap 95\\% confidence intervals (CIs; 1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\\theta$ and non-boundary-pair CI upper bounds fall below $\\theta$ (Section~\\ref{sec:kstar_boundary}).\n\n\\paragraph{Threshold choice.}\nWe set $\\theta{=}0.60$ as a data-driven operational threshold, chosen at the empirical discontinuity in the AUC distribution (Figure~\\ref{fig:kstar_theta}).\nA 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\\,0.55$ and $p < 0.002$ for all boundary comparisons, placing $\\theta{=}0.60$ well above the empirical null.\n$\\Kempirical{=}2$ is stable across $\\theta \\in [0.55, 0.65]$ for all but two marginal configurations (Table~\\ref{tab:kstar_ci_extended}): 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, creating a ${\\sim}$5--11\\,pp discontinuity.\nOnly at extremes does $\\Kempirical$ shift: $\\theta{=}0.55$ yields $\\Kempirical{=}3$ for two Qwen configurations; $\\theta{=}0.70$ yields $\\Kempirical{=}1$ across all configurations.\nThe downstream filtering evaluation (Section~\\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\\theta$, avoiding circularity.\n\n\\subsection{Features and Classifier}\n\\label{sec:features}\n\nEach document is characterized by a 15-dimensional feature vector spanning four groups: \\emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \\emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \\emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \\emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).\nAll features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\\ref{tab:s5_features}, Appendix).\nSelf-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \\#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.\nRemoving self-BLEU reduces mean $\\auc_{1v2}$ by $< 1$\\,pp across all models (14D $\\Kempirical = 2$ for all 4 configurations; bootstrap CIs in Table~\\ref{tab:selfbleu_ablation}); in deployment where depth labels are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted with minimal performance loss.\nHand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.\n\nWe use \\emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\\text{depth} > k \\mid \\mathbf{x})$ via LightGBM (hyperparameters in Table~\\ref{tab:s6_lgbm_params}).\nOBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\\auc$ (mean 0.6095 vs.\\ 0.4883 for ordinal logistic regression).\n\n\\subsection{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate nine configurations spanning five architecture families (Table~\\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B, Qwen2.5-14B, Pythia-1.4B, OLMo-1B, LLaMA-3.1-8B, and Mistral-7B (all continuation except Qwen-rw).\nEach uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).\nDefault decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.\nContinuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.\nEvaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\\auc$ as primary metric.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Experimental configurations for depth-chain generation. \\textbf{Config}: shorthand identifier; \\textbf{Model}: architecture and parameter count; \\textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}\n\\label{tab:setup}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Config} & \\textbf{Model} & \\textbf{Mode} & $N$ \\\\\n\\midrule\nQwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\\\\nQwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\\\\nQwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\\\\nPythia    & Pythia-1.4B            & Continuation & 5{,}000 \\\\\nOLMo      & OLMo-1B               & Continuation & 5{,}000 \\\\\nQwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\\\\nQwen-14B  & Qwen2.5-14B           & Continuation & 5{,}000 \\\\\nLLaMA-8B  & LLaMA-3.1-8B          & Continuation & 5{,}000 \\\\\nMistral   & Mistral-7B            & Continuation & 5{,}000 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 77,
      "startLine": 1,
      "totalLines": 77
    }
  },
  "sourceToolAssistantUUID": "69631fd7-4153-4e8a-b60d-06aa541082d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-18T14:30:03.511Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KrFWCeyio5QNYxGTo6oUb7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "746973c4-462f-4113-8558-a82c13fed8e9",
  "isSidechain": false,
  "requestId": "req_011CbACCvsMCEqjH5hUV5FY5",
  "type": "assistant",
  "uuid": "7ccc6937-6631-485d-a94c-f1182feede2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECzDnd2j5NdSKnjmmowK97",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 100323,
      "cache_read_input_tokens": 11841,
      "output_tokens": 621,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 100323,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 621,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 100323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 100323
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-18T14:30:03.516Z_

<details><summary>↩ Tool result · `toolu_01KrFWCeyio5QNYxGTo6oUb7`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on nine model configurations spanning five architecture families:
5	Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, Qwen2.5-14B, LLaMA-3.1-8B, and Mistral-7B, all in continuation mode except where noted.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
7	
8	%% ====================================================================
9	\subsection{\texorpdfstring{$\Kempirical \leq 2$}{K*<=2} Across Model Configurations (C4)}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
17	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
18	\label{tab:kstar_ci}
19	\begin{tabular}{lcccccccccc}
20	\toprule
21	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
22	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
23	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
24	\midrule
25	0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\,.967] \\
26	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .6145 & [.605,\,.625]\rlap{$^*$} & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
27	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .5496 & [.540,\,.560] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
28	3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\
29	4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\
30	\bottomrule
31	\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\
32	\multicolumn{11}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}
33	\end{tabular}
34	\end{table*}
35	
36	\begin{figure}[t]
37	\centering
38	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
39	\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\theta = 0.60$.}
40	\label{fig:auc_decay}
41	\end{figure}
42	
43	Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical \leq 2$ across all 9 model configurations: 8/9 yield $\Kempirical{=}2$ (1v2 $\auc$ range: 0.6112--0.6955; all CI lower bounds $> \theta$; permutation $p < 0.001$), while Mistral-7B is the sole exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, below $\theta$; Section~\ref{sec:boundary_cases}).
44	LLaMA-3.1-8B yields $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123$, 95\% CI $[0.603, 0.622]$; borderline: 1/5 folds falls below $\theta$; Table~\ref{tab:kstar_ci_extended}).
45	All four decoding strategies likewise yield $\Kempirical{=}2$ (Table~\ref{tab:s2_decoding}).
46	The 1v2 spread due to generation mode ($\Delta = 8.4$\,pp within Qwen) exceeds the spread across models in continuation mode ($\Delta = 3.9$\,pp).
47	
48	\paragraph{Scale and instruction-tuning invariance.}
49	$\Kempirical{=}2$ persists from 1.5B through 14B: Qwen-14B (1v2 $\auc = 0.621$ $[0.612, 0.630]$), Qwen-7B ($0.6168$ $[0.608, 0.626]$), and LLaMA-3.1-8B ($0.6123$) all exceed $\theta$, despite progressively reduced 0v1 signal (0.960 at 14B, 0.964 at 7B, 0.923 at 8B vs.\ $> 0.99$ at $\leq$1.5B).
50	A base-vs.-instruct ablation at 1.5B likewise yields $\Kempirical = 2$ (1v2 $\auc = 0.626$), indicating the boundary is not an instruction-tuning artifact.
51	
52	\begin{figure}[t]
53	\centering
54	\includegraphics[width=\columnwidth]{figures/fig_kstar_theta.pdf}
55	\caption{$\Kempirical(\theta)$ sensitivity curve for six configurations. $\Kempirical$: maximum discriminable depth; $\theta$: AUC decision threshold. All configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (dashed line). At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
56	\label{fig:kstar_theta}
57	\end{figure}
58	
59	Figure~\ref{fig:kstar_theta} shows $\Kempirical$ as a function of $\theta$: web text $\Kempirical{=}2$ is stable across a 5\,pp window ($\theta \in [0.575, 0.625]$), with a gradual transition to $\Kempirical{=}3$ at $\theta{=}0.55$ (two Qwen configurations) and $\Kempirical{=}1$ at $\theta{=}0.70$.
60	The domain ordering (arXiv $>$ web $\geq$ cross-scorer) is preserved across the full $\theta$ range (Table~\ref{tab:theta_sensitivity}; Figure~\ref{fig:theta_sensitivity} in Appendix shows the complete model $\times$ domain $\theta$ sensitivity).
61	All four decoding strategies likewise yield $\Kempirical = 2$ at $\theta{=}0.60$ (1v2 $\auc \in [0.687, 0.704]$; Table~\ref{tab:s2_decoding}).
62	
63	%% ====================================================================
64	\subsection{Generator-Independent Transfer}
65	\label{sec:transfer}
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=0.85\columnwidth]{figures/fig3_transfer_heatmap.pdf}
70	\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\leftrightarrow$OLMo: 90--92\%; Qwen-rewrite$\to$continuation: 61--63\%.}
71	\label{fig:transfer_heatmap}
72	\end{figure}
73	
74	Continuation-mode classifiers transfer well across generators (Figure~\ref{fig:transfer_heatmap}; full matrix in Table~\ref{tab:s1_transfer}): Pythia$\leftrightarrow$OLMo retains 90--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\% (0v1 cross-model $\auc > 0.96$ for all pairs).
75	Qwen-rewrite classifiers transfer poorly (61--63\%), consistent with reliance on mode-specific artifacts rather than generalizable depth features.
76	
77	\paragraph{Cross-scorer validation.}
78	Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\ref{tab:crossscorer}).
79	Qwen-rewrite $\Kempirical$ remains 2 under all scorers; Qwen-continuation drops to 1 (1v2 $\auc$: $0.6112 \to 0.5923/0.5858$), consistent with its marginality under self-scoring.
80	Both alternative scorers agree on $\Kempirical$ per generation mode, indicating that $\Kempirical$ is governed by the generation process rather than the scorer.
81	For arXiv, cross-scoring with Pythia-1.4B preserves $\Kempirical{=}3$ for three of four generators (Qwen-1.5B, LLaMA-8B, Mistral-7B; 2v3 $\auc$ range: 0.608--0.632).
82	Qwen-7B exhibits a borderline decrease to $\Kempirical{=}2$ (2v3 $\auc = 0.599$ vs.\ $0.626$ self-scored, $\Delta = -2.7$\,pp; 3/5 folds above $\theta$), consistent with the Qwen family's scorer sensitivity observed on C4 and Wikipedia.
83	Bootstrap CIs (10{,}000 resamples) confirm $\Kempirical{=}3$ for Qwen-1.5B (CI lower $= 0.617$) and LLaMA-8B (CI lower $= 0.605$); for Mistral-7B (CI: $[0.593, 0.622]$) and Qwen-7B (CI: $[0.584, 0.613]$), the CI straddles $\theta$, indicating that their $\Kempirical{=}3$ assignment is sensitive to resampling variance (Table~\ref{tab:arxiv_crossscorer_ci}).
84	A three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair; $N{=}300$; Table~\ref{tab:anova_crossscorer}) confirms that Depth-Pair dominates variance ($\eta^2_p = 0.998$); Scorer is statistically significant ($p < .001$) but practically minor ($\eta^2_p = 0.192$), consistent with a detectable but small scorer influence on absolute discriminability.
85	
86	%% ====================================================================
87	\subsection{Feature Ordering and Generation Mode}
88	\label{sec:feature_degradation}
89	\label{sec:generation_mode}
90	
91	Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
92	The top-3 features (\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability; however, no single feature subset of size ${<}8$ reliably sustains $\Kempirical{=}2$ (Appendix~\ref{sec:feature_subset}).
93	A feature group ablation (Appendix~\ref{sec:feature_ablation}) confirms that surprisal (base) dominates on arXiv (single AUC $= 0.809$, LOO $\Delta = 0.031$); on C4 and Wikipedia, all LOO drops fall within fold variance ($\leq 0.007$).
94	Qwen-rewrite diverges (\texttt{freq\_entropy} dominates), consistent with its poor cross-model transfer (61--63\%).
95	Within Qwen, rewrite yields 1v2 $\auc = 0.6955$ vs.\ continuation's $0.6112$ ($\Delta = +8.4$\,pp); continuation mode is therefore recommended as the canonical condition.
96	
97	%% ====================================================================
98	\subsection{Neural Probe}
99	\label{sec:neural_probe}
100	
101	Replacing the 15D features with frozen encoder hidden states (MLP probe; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia and OLMo remain at $\Kempirical^{\text{neural}} = 2$ ($\auc_{2v3}$: 0.5963, 0.5892).
102	The Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\ref{sec:transfer}); the 15D features yield consistent $\Kempirical = 2$ across all families.
103	
104	\noindent\begin{minipage}{\columnwidth}
105	\centering
106	\footnotesize
107	\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $\Kempirical^{\text{neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}
108	\label{tab:neural_probe_crossmodel}
109	\resizebox{\columnwidth}{!}{%
110	\begin{tabular}{lccc}
111	\toprule
112	\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
113	\midrule
114	Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
115	Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
116	OLMo-1B    & 0.5892 & $[0.582,\,0.597]$ & 2 \\
117	\bottomrule
118	\end{tabular}}
119	\end{minipage}
120	
121	%% ====================================================================
122	\subsection{Cross-Domain Variation}
123	\label{sec:cross_domain}
124	
125	The preceding experiments use C4 (general web text).
126	To test whether $\Kempirical$ reflects domain structure or model identity, we evaluate on arXiv abstracts ($n{=}2{,}200$ per model) and Wikipedia ($n{=}5{,}000$ per model) across six model configurations spanning four architecture families (Table~\ref{tab:domain_kstar}).
127	
128	\paragraph{arXiv ($\Kempirical{=}3$): five-model cross-validation.}
129	All five domain-competent models yield $\Kempirical{=}3$ on arXiv, with boundary-pair $\auc$ (2v3) ranging from 0.6215 to 0.6545, all exceeding $\theta$.
130	The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4): formulaic features (LaTeX formatting, citation patterns, mathematical notation) degrade slowly under autoregressive generation and supply persistent depth signal across four architecture families and 1.4B--8B parameters.
131	Removing LaTeX markup reduces 2v3 AUC by ${\sim}$1.8\,pp but preserves $\Kempirical{=}3$ (CI lower $= 0.610 > \theta$; Table~\ref{tab:latex_ablation}), confirming that content-level properties dominate.
132	OLMo-1B constitutes a capacity failure rather than a counter-example; its arXiv generations are entirely out-of-domain (0v1 JSD $= 0.33$, near-total information loss at the first step), yielding $\Kempirical{=}1$.
133	Mistral-7B provides the strongest domain-dependence evidence: $\Kempirical{=}1$ on C4 (Section~\ref{sec:boundary_cases}) but $\Kempirical{=}3$ on arXiv, confirming that domain structure alone can shift $\Kempirical$ by two levels within the same model.
134	
135	\paragraph{Wikipedia ($\Kempirical{=}1$): single-generation saturation.}
136	With scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield $\Kempirical{=}1$ on Wikipedia: 1v2 $\auc$ ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below $\theta$.
137	Wikipedia represents the simplest domain tested; its encyclopedic regularity provides minimal structural signal beyond the 0v1 boundary, and a single generation pass suffices for complete saturation.
138	A same-family scorer confound inflates the apparent $\Kempirical$ for Qwen generators: Qwen-1.5B scoring yields $\Kempirical{=}2$ (1v2 $\auc \approx 0.61$--$0.62$), but cross-family scoring reduces 1v2 by 2.4\,pp to below $\theta$ (Appendix~\ref{sec:wiki_domain}).
139	This +1 depth bias under same-family scoring is specific to Qwen generators on Wikipedia and does not affect C4 results (Section~\ref{sec:transfer}).
140	
141	\paragraph{Domain as the sole dominant factor.}
142	With the scorer confound controlled, the domain ordering is uniform across all tested models: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$).
143	Neither model scale (1B--14B), architecture family, nor decoding strategy alters this ordering, establishing source-domain structural complexity as the primary determinant of $\Kempirical$.
144	
145	\noindent\begin{minipage}{\columnwidth}
146	\centering
147	\footnotesize
148	\captionof{table}{Domain $\times$ Model $\Kempirical$ matrix (scorer-controlled). Wikipedia values use cross-family scorer (Pythia-1.4B). $^*$OLMo arXiv: capacity failure (out-of-domain generation). $^\dagger$Raw same-family scoring yields $\Kempirical{=}2$; controlled value shown (Appendix~\ref{sec:wiki_domain}).}
149	\label{tab:domain_kstar}
150	\resizebox{\columnwidth}{!}{%
151	\begin{tabular}{lccc}
152	\toprule
153	\textbf{Model} & \textbf{C4} & \textbf{arXiv} & \textbf{Wikipedia} \\
154	\midrule
155	Qwen-1.5B    & 2 & 3 & 1$^\dagger$ \\
156	Qwen-7B      & 2 & 3 & 1$^\dagger$ \\
157	Pythia-1.4B  & 2 & 3 & 1 \\
158	OLMo-1B      & 2 & 1$^*$ & 1 \\
159	LLaMA-3.1-8B & 2 & 3 & 1 \\
160	Mistral-7B   & 1 & 3 & 1 \\
161	\bottomrule
162	\end{tabular}}
163	\end{minipage}
164	
165	%% ====================================================================
166	\subsection{Binary Detector Confidence}
167	\label{sec:binary_confidence}
168	
169	Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.
170	The observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.
171	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ccc6937-6631-485d-a94c-f1182feede2d",
  "isSidechain": false,
  "promptId": "a76e3a98-645a-445f-972e-aeb6711b75d1",
  "type": "user",
  "uuid": "8d667d03-2a33-45a3-b6d1-5473738c40ba",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate generational depth estimation on nine model configurations spanning five architecture families:\nPythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, Qwen2.5-14B, LLaMA-3.1-8B, and Mistral-7B, all in continuation mode except where noted.\nAll experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).\n\n%% ====================================================================\n\\subsection{\\texorpdfstring{$\\Kempirical \\leq 2$}{K*<=2} Across Model Configurations (C4)}\n\\label{sec:kstar_boundary}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Pairwise $\\auc$ for adjacent depth pairs with bootstrap 95\\% CIs and permutation $p$-values for boundary rows.\n$\\Kempirical = 2$ requires 1v2 $\\auc > \\theta{=}0.60$ and 2v3 $\\auc < \\theta$; CIs quantify boundary uncertainty.\nExtended results (all models) in Table~\\ref{tab:kstar_ci_extended}.}\n\\label{tab:kstar_ci}\n\\begin{tabular}{lcccccccccc}\n\\toprule\n & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\n & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n\\midrule\n0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\\,.967] \\\\\n1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6539 & [.645,\\,.663]\\rlap{$^*$} & .6145 & [.605,\\,.625]\\rlap{$^*$} & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} \\\\\n2v3 & .5893 & [.580,\\,.599] & .5514 & [.542,\\,.563] & .5496 & [.540,\\,.560] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] \\\\\n3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\\\\n4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\\\\n\\bottomrule\n\\multicolumn{11}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_auc_decay.pdf}\n\\caption{Pairwise $\\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\\theta = 0.60$.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:kstar_ci} and Figure~\\ref{fig:auc_decay} show $\\Kempirical \\leq 2$ across all 9 model configurations: 8/9 yield $\\Kempirical{=}2$ (1v2 $\\auc$ range: 0.6112--0.6955; all CI lower bounds $> \\theta$; permutation $p < 0.001$), while Mistral-7B is the sole exception ($\\Kempirical{=}1$; 1v2 $\\auc = 0.594$, below $\\theta$; Section~\\ref{sec:boundary_cases}).\nLLaMA-3.1-8B yields $\\Kempirical{=}2$ (0v1 $\\auc = 0.9225$, 1v2 $\\auc = 0.6123$, 95\\% CI $[0.603, 0.622]$; borderline: 1/5 folds falls below $\\theta$; Table~\\ref{tab:kstar_ci_extended}).\nAll four decoding strategies likewise yield $\\Kempirical{=}2$ (Table~\\ref{tab:s2_decoding}).\nThe 1v2 spread due to generation mode ($\\Delta = 8.4$\\,pp within Qwen) exceeds the spread across models in continuation mode ($\\Delta = 3.9$\\,pp).\n\n\\paragraph{Scale and instruction-tuning invariance.}\n$\\Kempirical{=}2$ persists from 1.5B through 14B: Qwen-14B (1v2 $\\auc = 0.621$ $[0.612, 0.630]$), Qwen-7B ($0.6168$ $[0.608, 0.626]$), and LLaMA-3.1-8B ($0.6123$) all exceed $\\theta$, despite progressively reduced 0v1 signal (0.960 at 14B, 0.964 at 7B, 0.923 at 8B vs.\\ $> 0.99$ at $\\leq$1.5B).\nA base-vs.-instruct ablation at 1.5B likewise yields $\\Kempirical = 2$ (1v2 $\\auc = 0.626$), indicating the boundary is not an instruction-tuning artifact.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_kstar_theta.pdf}\n\\caption{$\\Kempirical(\\theta)$ sensitivity curve for six configurations. $\\Kempirical$: maximum discriminable depth; $\\theta$: AUC decision threshold. All configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (dashed line). At $\\theta{=}0.70$, all drop to $\\Kempirical{=}1$.}\n\\label{fig:kstar_theta}\n\\end{figure}\n\nFigure~\\ref{fig:kstar_theta} shows $\\Kempirical$ as a function of $\\theta$: web text $\\Kempirical{=}2$ is stable across a 5\\,pp window ($\\theta \\in [0.575, 0.625]$), with a gradual transition to $\\Kempirical{=}3$ at $\\theta{=}0.55$ (two Qwen configurations) and $\\Kempirical{=}1$ at $\\theta{=}0.70$.\nThe domain ordering (arXiv $>$ web $\\geq$ cross-scorer) is preserved across the full $\\theta$ range (Table~\\ref{tab:theta_sensitivity}; Figure~\\ref{fig:theta_sensitivity} in Appendix shows the complete model $\\times$ domain $\\theta$ sensitivity).\nAll four decoding strategies likewise yield $\\Kempirical = 2$ at $\\theta{=}0.60$ (1v2 $\\auc \\in [0.687, 0.704]$; Table~\\ref{tab:s2_decoding}).\n\n%% ====================================================================\n\\subsection{Generator-Independent Transfer}\n\\label{sec:transfer}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig3_transfer_heatmap.pdf}\n\\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\\leftrightarrow$OLMo: 90--92\\%; Qwen-rewrite$\\to$continuation: 61--63\\%.}\n\\label{fig:transfer_heatmap}\n\\end{figure}\n\nContinuation-mode classifiers transfer well across generators (Figure~\\ref{fig:transfer_heatmap}; full matrix in Table~\\ref{tab:s1_transfer}): Pythia$\\leftrightarrow$OLMo retains 90--92\\%, Qwen-cont$\\leftrightarrow$Pythia 84--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\% (0v1 cross-model $\\auc > 0.96$ for all pairs).\nQwen-rewrite classifiers transfer poorly (61--63\\%), consistent with reliance on mode-specific artifacts rather than generalizable depth features.\n\n\\paragraph{Cross-scorer validation.}\nReplacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\\ref{tab:crossscorer}).\nQwen-rewrite $\\Kempirical$ remains 2 under all scorers; Qwen-continuation drops to 1 (1v2 $\\auc$: $0.6112 \\to 0.5923/0.5858$), consistent with its marginality under self-scoring.\nBoth alternative scorers agree on $\\Kempirical$ per generation mode, indicating that $\\Kempirical$ is governed by the generation process rather than the scorer.\nFor arXiv, cross-scoring with Pythia-1.4B preserves $\\Kempirical{=}3$ for three of four generators (Qwen-1.5B, LLaMA-8B, Mistral-7B; 2v3 $\\auc$ range: 0.608--0.632).\nQwen-7B exhibits a borderline decrease to $\\Kempirical{=}2$ (2v3 $\\auc = 0.599$ vs.\\ $0.626$ self-scored, $\\Delta = -2.7$\\,pp; 3/5 folds above $\\theta$), consistent with the Qwen family's scorer sensitivity observed on C4 and Wikipedia.\nBootstrap CIs (10{,}000 resamples) confirm $\\Kempirical{=}3$ for Qwen-1.5B (CI lower $= 0.617$) and LLaMA-8B (CI lower $= 0.605$); for Mistral-7B (CI: $[0.593, 0.622]$) and Qwen-7B (CI: $[0.584, 0.613]$), the CI straddles $\\theta$, indicating that their $\\Kempirical{=}3$ assignment is sensitive to resampling variance (Table~\\ref{tab:arxiv_crossscorer_ci}).\nA three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair; $N{=}300$; Table~\\ref{tab:anova_crossscorer}) confirms that Depth-Pair dominates variance ($\\eta^2_p = 0.998$); Scorer is statistically significant ($p < .001$) but practically minor ($\\eta^2_p = 0.192$), consistent with a detectable but small scorer influence on absolute discriminability.\n\n%% ====================================================================\n\\subsection{Feature Ordering and Generation Mode}\n\\label{sec:feature_degradation}\n\\label{sec:generation_mode}\n\nAmong continuation-mode models, single-feature $\\auc$ rankings are highly correlated ($\\rho \\geq 0.85$; Table~\\ref{tab:top_features}).\nThe top-3 features (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}, \\texttt{surp\\_d2\\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability; however, no single feature subset of size ${<}8$ reliably sustains $\\Kempirical{=}2$ (Appendix~\\ref{sec:feature_subset}).\nA feature group ablation (Appendix~\\ref{sec:feature_ablation}) confirms that surprisal (base) dominates on arXiv (single AUC $= 0.809$, LOO $\\Delta = 0.031$); on C4 and Wikipedia, all LOO drops fall within fold variance ($\\leq 0.007$).\nQwen-rewrite diverges (\\texttt{freq\\_entropy} dominates), consistent with its poor cross-model transfer (61--63\\%).\nWithin Qwen, rewrite yields 1v2 $\\auc = 0.6955$ vs.\\ continuation's $0.6112$ ($\\Delta = +8.4$\\,pp); continuation mode is therefore recommended as the canonical condition.\n\n%% ====================================================================\n\\subsection{Neural Probe}\n\\label{sec:neural_probe}\n\nReplacing the 15D features with frozen encoder hidden states (MLP probe; Table~\\ref{tab:neural_probe_crossmodel}), Qwen achieves $\\Kempirical^{\\text{neural}} = 3$ (2v3 $\\auc = 0.6159$), while Pythia and OLMo remain at $\\Kempirical^{\\text{neural}} = 2$ ($\\auc_{2v3}$: 0.5963, 0.5892).\nThe Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\\ref{sec:transfer}); the 15D features yield consistent $\\Kempirical = 2$ across all families.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\\ $d{+}1$ text. $\\Kempirical^{\\text{neural}}$: maximum depth where AUC exceeds $\\theta = 0.60$.}\n\\label{tab:neural_probe_crossmodel}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & $\\Kempirical^{\\text{neural}}$ \\\\\n\\midrule\nQwen-1.5B  & 0.6159 & $[0.610,\\,0.622]$ & 3 \\\\\nPythia-1.4B & 0.5963 & $[0.589,\\,0.603]$ & 2 \\\\\nOLMo-1B    & 0.5892 & $[0.582,\\,0.597]$ & 2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Cross-Domain Variation}\n\\label{sec:cross_domain}\n\nThe preceding experiments use C4 (general web text).\nTo test whether $\\Kempirical$ reflects domain structure or model identity, we evaluate on arXiv abstracts ($n{=}2{,}200$ per model) and Wikipedia ($n{=}5{,}000$ per model) across six model configurations spanning four architecture families (Table~\\ref{tab:domain_kstar}).\n\n\\paragraph{arXiv ($\\Kempirical{=}3$): five-model cross-validation.}\nAll five domain-competent models yield $\\Kempirical{=}3$ on arXiv, with boundary-pair $\\auc$ (2v3) ranging from 0.6215 to 0.6545, all exceeding $\\theta$.\nThe elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\\ ${\\sim}0.01$ for C4): formulaic features (LaTeX formatting, citation patterns, mathematical notation) degrade slowly under autoregressive generation and supply persistent depth signal across four architecture families and 1.4B--8B parameters.\nRemoving LaTeX markup reduces 2v3 AUC by ${\\sim}$1.8\\,pp but preserves $\\Kempirical{=}3$ (CI lower $= 0.610 > \\theta$; Table~\\ref{tab:latex_ablation}), confirming that content-level properties dominate.\nOLMo-1B constitutes a capacity failure rather than a counter-example; its arXiv generations are entirely out-of-domain (0v1 JSD $= 0.33$, near-total information loss at the first step), yielding $\\Kempirical{=}1$.\nMistral-7B provides the strongest domain-dependence evidence: $\\Kempirical{=}1$ on C4 (Section~\\ref{sec:boundary_cases}) but $\\Kempirical{=}3$ on arXiv, confirming that domain structure alone can shift $\\Kempirical$ by two levels within the same model.\n\n\\paragraph{Wikipedia ($\\Kempirical{=}1$): single-generation saturation.}\nWith scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield $\\Kempirical{=}1$ on Wikipedia: 1v2 $\\auc$ ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below $\\theta$.\nWikipedia represents the simplest domain tested; its encyclopedic regularity provides minimal structural signal beyond the 0v1 boundary, and a single generation pass suffices for complete saturation.\nA same-family scorer confound inflates the apparent $\\Kempirical$ for Qwen generators: Qwen-1.5B scoring yields $\\Kempirical{=}2$ (1v2 $\\auc \\approx 0.61$--$0.62$), but cross-family scoring reduces 1v2 by 2.4\\,pp to below $\\theta$ (Appendix~\\ref{sec:wiki_domain}).\nThis +1 depth bias under same-family scoring is specific to Qwen generators on Wikipedia and does not affect C4 results (Section~\\ref{sec:transfer}).\n\n\\paragraph{Domain as the sole dominant factor.}\nWith the scorer confound controlled, the domain ordering is uniform across all tested models: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $>$ Wikipedia ($\\Kempirical{=}1$).\nNeither model scale (1B--14B), architecture family, nor decoding strategy alters this ordering, establishing source-domain structural complexity as the primary determinant of $\\Kempirical$.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Domain $\\times$ Model $\\Kempirical$ matrix (scorer-controlled). Wikipedia values use cross-family scorer (Pythia-1.4B). $^*$OLMo arXiv: capacity failure (out-of-domain generation). $^\\dagger$Raw same-family scoring yields $\\Kempirical{=}2$; controlled value shown (Appendix~\\ref{sec:wiki_domain}).}\n\\label{tab:domain_kstar}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{C4} & \\textbf{arXiv} & \\textbf{Wikipedia} \\\\\n\\midrule\nQwen-1.5B    & 2 & 3 & 1$^\\dagger$ \\\\\nQwen-7B      & 2 & 3 & 1$^\\dagger$ \\\\\nPythia-1.4B  & 2 & 3 & 1 \\\\\nOLMo-1B      & 2 & 1$^*$ & 1 \\\\\nLLaMA-3.1-8B & 2 & 3 & 1 \\\\\nMistral-7B   & 1 & 3 & 1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Binary Detector Confidence}\n\\label{sec:binary_confidence}\n\nBinary detectors (DivEye~\\cite{basani2026diveye}, Binoculars~\\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\\rho| = 0.06$--$0.46$; Table~\\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\\leq 0.199$ vs.\\ 0.167 baseline), pairwise $\\auc$ yields $\\Kempirical^{\\text{binary}} \\leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.\nThe observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.\n",
      "numLines": 171,
      "startLine": 1,
      "totalLines": 171
    }
  },
  "sourceToolAssistantUUID": "7ccc6937-6631-485d-a94c-f1182feede2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-18T14:30:04.462Z_

<details open><summary>🔧 Tool call — Read · `toolu_018Ubfr6J3TjyM2AZZ37qjw4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d667d03-2a33-45a3-b6d1-5473738c40ba",
  "isSidechain": false,
  "requestId": "req_011CbACCvsMCEqjH5hUV5FY5",
  "type": "assistant",
  "uuid": "1fd43007-0fc5-4753-8106-98951b1471b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECzDnd2j5NdSKnjmmowK97",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 100323,
      "cache_read_input_tokens": 11841,
      "output_tokens": 621,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 100323,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 621,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 100323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 100323
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-18T14:30:04.466Z_

<details><summary>↩ Tool result · `toolu_018Ubfr6J3TjyM2AZZ37qjw4`</summary>

```text
1	\section{Downstream Filtering Validation}
2	\label{sec:filtering}
3	
4	We test whether $\Kempirical$ has predictive value for curation strategy selection, using a single-model setup (Qwen2.5-1.5B-Instruct) as proof of concept.
5	$\Kempirical = 2$ predicts that binary curation should suffice, and that graduated performance should converge toward binary as the decay steepness increases.
6	We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} ($w = 1 - P(\text{synthetic})$ from 15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \cdot \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal} (retain above median), and (vi)~\textbf{DSIR}~\citep{xie2023dsir}.
7	We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU (a multitask language understanding benchmark) and HellaSwag (a commonsense reasoning benchmark) across 5 seeds (51 total runs: 5 base strategies $\times$ 5 seeds $+$ 5 graduated-$\alpha$ values $\times$ 5 seeds $+$ 1 base-model reference; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \exp(-\alpha \hat{d})$. Mean $\pm$ std over 5 seeds. Full $\alpha$ sweep in Appendix~\ref{sec:extended_limitations}.}
13	\label{tab:tab_filtering_main}
14	\resizebox{\columnwidth}{!}{\input{tables/tab_filtering_main}}
15	\end{table}
16	
17	Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp ($p_{\text{corr}} < 0.05$ vs.\ all alternatives).
18	The absolute improvement is modest (${\sim}$0.8\,pp), consistent with the constrained dynamic range of a 100\% synthetic upper-bound setting; real-world contamination ratios are typically lower and effect sizes scale accordingly.
19	The strategy ordering is interpretable through $\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduated strategies assign weights to depths 2--5 based on near-random classifier outputs, injecting noise.
20	Graduated filtering converges monotonically toward binary: at $\alpha{=}0.9$, it matches binary-ours on HellaSwag exactly ($\Delta = 0$, $p_{\text{corr}} = 1.00$) but remains significantly worse on MMLU ($p_{\text{corr}} = 0.011$).
21	DSIR is indistinguishable from no-filter, confirming that depth-aware features are necessary for curation in recursively contaminated corpora (Figure~\ref{fig:filtering_strategies} in Appendix).
22	Binary filtering retains a consistent advantage across contamination levels (10--50\%), with effect sizes diminishing 3--6$\times$ relative to the 100\% setting; graduated weighting remains indistinguishable from no-filter at all tested ratios, confirming that depth assignments beyond $\Kempirical$ inject noise regardless of severity (Appendix~\ref{sec:dose_response}).
23	Cross-model replication on Pythia-1.4B confirms the binary $>$ graduated ordering (Appendix~\ref{sec:pythia_filtering}), consistent with $\Kempirical{=}2$ predicting binary filtering as optimal granularity.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fd43007-0fc5-4753-8106-98951b1471b5",
  "isSidechain": false,
  "promptId": "a76e3a98-645a-445f-972e-aeb6711b75d1",
  "type": "user",
  "uuid": "525c3e29-79fd-4888-9227-c25e1dc89fb3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex",
      "content": "\\section{Downstream Filtering Validation}\n\\label{sec:filtering}\n\nWe test whether $\\Kempirical$ has predictive value for curation strategy selection, using a single-model setup (Qwen2.5-1.5B-Instruct) as proof of concept.\n$\\Kempirical = 2$ predicts that binary curation should suffice, and that graduated performance should converge toward binary as the decay steepness increases.\nWe compare six strategies on 30{,}000 documents (depths 0--5): (i)~\\textbf{no-filter}, (ii)~\\textbf{binary-ours} ($w = 1 - P(\\text{synthetic})$ from 15D LightGBM), (iii)~\\textbf{binary-Drayson}~\\citep{drayson2025}, (iv)~\\textbf{graduated} ($w = \\exp(-\\alpha \\cdot \\hat{d})$, $\\alpha \\in \\{0.1,\\ldots,0.9\\}$), (v)~\\textbf{surprisal} (retain above median), and (vi)~\\textbf{DSIR}~\\citep{xie2023dsir}.\nWe fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\\alpha_{\\text{LoRA}}{=}16$) for 3 epochs on MMLU (a multitask language understanding benchmark) and HellaSwag (a commonsense reasoning benchmark) across 5 seeds (51 total runs: 5 base strategies $\\times$ 5 seeds $+$ 5 graduated-$\\alpha$ values $\\times$ 5 seeds $+$ 1 base-model reference; this 100\\% synthetic setting is an upper bound~\\cite{shumailov2024collapse, dohmatob2024model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \\exp(-\\alpha \\hat{d})$. Mean $\\pm$ std over 5 seeds. Full $\\alpha$ sweep in Appendix~\\ref{sec:extended_limitations}.}\n\\label{tab:tab_filtering_main}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_filtering_main}}\n\\end{table}\n\nBinary-ours minimizes MMLU degradation most effectively (Table~\\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\\,pp (no-filter) to $-$0.77\\,pp ($p_{\\text{corr}} < 0.05$ vs.\\ all alternatives).\nThe absolute improvement is modest (${\\sim}$0.8\\,pp), consistent with the constrained dynamic range of a 100\\% synthetic upper-bound setting; real-world contamination ratios are typically lower and effect sizes scale accordingly.\nThe strategy ordering is interpretable through $\\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduated strategies assign weights to depths 2--5 based on near-random classifier outputs, injecting noise.\nGraduated filtering converges monotonically toward binary: at $\\alpha{=}0.9$, it matches binary-ours on HellaSwag exactly ($\\Delta = 0$, $p_{\\text{corr}} = 1.00$) but remains significantly worse on MMLU ($p_{\\text{corr}} = 0.011$).\nDSIR is indistinguishable from no-filter, confirming that depth-aware features are necessary for curation in recursively contaminated corpora (Figure~\\ref{fig:filtering_strategies} in Appendix).\nBinary filtering retains a consistent advantage across contamination levels (10--50\\%), with effect sizes diminishing 3--6$\\times$ relative to the 100\\% setting; graduated weighting remains indistinguishable from no-filter at all tested ratios, confirming that depth assignments beyond $\\Kempirical$ inject noise regardless of severity (Appendix~\\ref{sec:dose_response}).\nCross-model replication on Pythia-1.4B confirms the binary $>$ graduated ordering (Appendix~\\ref{sec:pythia_filtering}), consistent with $\\Kempirical{=}2$ predicting binary filtering as optimal granularity.\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  },
  "sourceToolAssistantUUID": "1fd43007-0fc5-4753-8106-98951b1471b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-18T14:30:04.931Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XLHhNYZxf15PY6mxAVKVfY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "525c3e29-79fd-4888-9227-c25e1dc89fb3",
  "isSidechain": false,
  "requestId": "req_011CbACCvsMCEqjH5hUV5FY5",
  "type": "assistant",
  "uuid": "6902da79-6c78-4047-b1db-d51aecff8d34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECzDnd2j5NdSKnjmmowK97",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 100323,
      "cache_read_input_tokens": 11841,
      "output_tokens": 621,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 100323,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 621,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 100323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 100323
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-18T14:30:04.937Z_

<details><summary>↩ Tool result · `toolu_01XLHhNYZxf15PY6mxAVKVfY`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	\label{sec:why_kstar}
4	\label{sec:one_wash}
5	\label{sec:negative_graduated}
6	\label{sec:repr_dependence}
7	\label{sec:boundary_cases}
8	\label{sec:length_confound}
9	
10	\begin{figure}[t]
11	\centering
12	\includegraphics[width=\columnwidth]{figures/fig_jsd_decay.pdf}
13	\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\Kempirical{=}2$; dashed purple: Mistral-7B ($\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\Kempirical{=}3$); dotted red: retrain-chain ($\Kempirical{\geq}4$). C4 models exhibit a sharp cliff ($\lambda \approx 2.2$--$3.5$), while arXiv decays gradually ($\lambda \approx 1.0$) and retrain-chain shows no cliff ($\lambda = 0.285$).}
14	\label{fig:jsd_decay}
15	\end{figure}
16	
17	\paragraph{One-wash laundering (web text).}
18	For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
19	A single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.
20	Converging evidence supports a data-intrinsic interpretation: OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 8--38\% (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).
21	
22	\paragraph{JSD decay and the discrimination boundary.}
23	Token-level Jensen-Shannon Divergence (JSD) between adjacent generations reveals two distinct decay regimes (Figure~\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\times$, median ${\sim}$15$\times$) followed by rapid convergence to a noise floor, while arXiv decays ${\sim}$3$\times$ slower ($\lambda \approx 1.0$ vs.\ $2.9$).
24	Cross-model consistency indicates that $G_\delta$ contraction rate is domain-governed.
25	The retrain-chain profile ($\lambda = 0.285$, no cliff) reflects model-adaptation artifacts rather than text-intrinsic loss: retrain-chain $\Kempirical{\geq}4$ (Pythia-1.4B LoRA; Table~\ref{tab:retrain_ci}) far exceeds prompt-chain $\Kempirical{=}2$ (Appendix~\ref{sec:jsd_extended}).
26	
27	\paragraph{Graduated filtering failure.}
28	For web text, 2v3 $\auc < \theta$ across all model configurations, so depth assignments for $d \geq 2$ approximate random labels; graduated weighting injects noise, explaining convergence toward binary at high $\alpha$ (Appendix~\ref{sec:extended_limitations}).
29	The strategy ordering binary $>$ graduated aligns with the $\Kempirical{=}2$ prediction: graduated approaches cannot exploit depth information that does not exist beyond the discrimination boundary.
30	On arXiv ($\Kempirical{=}3$), graduated filtering similarly shows no improvement over unfiltered data, consistent with $\Kempirical$ capturing discriminability rather than curation utility.
31	DSIR fails differently: bigram hashing captures domain shift but not depth-correlated signatures (pattern persists across 10--50\% contamination ratios; Appendix~\ref{sec:dose_response}).
32	
33	\paragraph{Representation and scorer dependence.}
34	$\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$, while Pythia and OLMo match the 15D boundary at $\Kempirical^{\text{neural}} = 2$ (Table~\ref{tab:neural_probe_crossmodel}); the 15D features trade one depth level for cross-model consistency (8/9 configurations $\Kempirical{\leq}2$).
35	$\Kempirical$ can also depend on scorer family: on Wikipedia, cross-family scoring reduces $\Kempirical$ from 2 to 1 ($\Delta = -2.4$\,pp; Appendix~\ref{sec:wiki_domain}), while on C4 it preserves feature rankings ($\rho > 0.90$) and $\Kempirical$ for 6/8 configurations (Section~\ref{sec:transfer}).
36	Scorer sensitivity is inversely related to domain lexical diversity; we recommend cross-family validation for new domains.
37	
38	\paragraph{Domain dependence of $\Kempirical$.}
39	C4 web text yields $\Kempirical{=}2$ (8/9 configurations, 1B--14B), while arXiv yields $\Kempirical{=}3$ across five models and four architecture families (Section~\ref{sec:cross_domain}).
40	With scorer confound controlled, all six models yield $\Kempirical{=}1$ on Wikipedia (Appendix~\ref{sec:wiki_domain}), producing a consistent ordering by source domain: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$), which correlates with domain-level lexical diversity.
41	The sole C4 exception (Mistral-7B, $\Kempirical{=}1$) has $\Kempirical{=}3$ on arXiv, reinforcing the domain-governed interpretation (Appendix~\ref{sec:boundary_extended}).
42	A LaTeX markup ablation confirms that content-level properties dominate (2v3 $\Delta = -1.8$\,pp, $\Kempirical$ unchanged; Appendix~\ref{sec:latex_ablation}).
43	
44	
45	\paragraph{Why $\Kempirical$ matters.}
46	$\Kempirical{=}2$ for web text is not a negative result but a precise measurement: it rules out both $\Kempirical{=}1$ (no depth signal beyond 0v1) and $\Kempirical{\geq}3$ (graduated tracking feasible), while arXiv $\Kempirical{=}3$ confirms the framework captures real domain-level variation rather than a methodological ceiling.
47	$\Kempirical$ thus serves as an empirical diagnostic of domain properties and is directly prescriptive for curation granularity.
48	The method combines established components (LightGBM, hand-crafted features, ordinal decomposition); the contribution is the measurement framework and the empirical characterization it enables.
49	
50	
51	
52	\paragraph{Practical implications.}
53	For web text ($\Kempirical{=}2$), graduated depth weighting injects noise beyond the boundary, validating binary filtering as optimal (Section~\ref{sec:filtering}); for arXiv ($\Kempirical{=}3$), an additional depth level carries discriminative signal.
54	Mixed-domain corpora thus require domain-stratified filtering; $\Kempirical{=}2$ provides post-hoc grounding for the binary approach of \citet{drayson2025}.
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6902da79-6c78-4047-b1db-d51aecff8d34",
  "isSidechain": false,
  "promptId": "a76e3a98-645a-445f-972e-aeb6711b75d1",
  "type": "user",
  "uuid": "bac127d7-0116-4128-b540-d95c783c3284",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\\label{sec:why_kstar}\n\\label{sec:one_wash}\n\\label{sec:negative_graduated}\n\\label{sec:repr_dependence}\n\\label{sec:boundary_cases}\n\\label{sec:length_confound}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_jsd_decay.pdf}\n\\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\\Kempirical{=}2$; dashed purple: Mistral-7B ($\\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\\Kempirical{=}3$); dotted red: retrain-chain ($\\Kempirical{\\geq}4$). C4 models exhibit a sharp cliff ($\\lambda \\approx 2.2$--$3.5$), while arXiv decays gradually ($\\lambda \\approx 1.0$) and retrain-chain shows no cliff ($\\lambda = 0.285$).}\n\\label{fig:jsd_decay}\n\\end{figure}\n\n\\paragraph{One-wash laundering (web text).}\nFor general web text, $\\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\\auc \\geq 0.92$), 1v2 drops by ${\\sim}$30\\,pp, and 2v3 falls below $\\theta$.\nA single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.\nConverging evidence supports a data-intrinsic interpretation: OBD achieves 96\\% depth-0 recall but only 14--22\\% for depths 2--4; frontier LLMs show 8--38\\% (McNemar $p > 0.05$ vs.\\ OBD; Table~\\ref{tab:s3_llm_zeroshot}).\n\n\\paragraph{JSD decay and the discrimination boundary.}\nToken-level Jensen-Shannon Divergence (JSD) between adjacent generations reveals two distinct decay regimes (Figure~\\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\\times$, median ${\\sim}$15$\\times$) followed by rapid convergence to a noise floor, while arXiv decays ${\\sim}$3$\\times$ slower ($\\lambda \\approx 1.0$ vs.\\ $2.9$).\nCross-model consistency indicates that $G_\\delta$ contraction rate is domain-governed.\nThe retrain-chain profile ($\\lambda = 0.285$, no cliff) reflects model-adaptation artifacts rather than text-intrinsic loss: retrain-chain $\\Kempirical{\\geq}4$ (Pythia-1.4B LoRA; Table~\\ref{tab:retrain_ci}) far exceeds prompt-chain $\\Kempirical{=}2$ (Appendix~\\ref{sec:jsd_extended}).\n\n\\paragraph{Graduated filtering failure.}\nFor web text, 2v3 $\\auc < \\theta$ across all model configurations, so depth assignments for $d \\geq 2$ approximate random labels; graduated weighting injects noise, explaining convergence toward binary at high $\\alpha$ (Appendix~\\ref{sec:extended_limitations}).\nThe strategy ordering binary $>$ graduated aligns with the $\\Kempirical{=}2$ prediction: graduated approaches cannot exploit depth information that does not exist beyond the discrimination boundary.\nOn arXiv ($\\Kempirical{=}3$), graduated filtering similarly shows no improvement over unfiltered data, consistent with $\\Kempirical$ capturing discriminability rather than curation utility.\nDSIR fails differently: bigram hashing captures domain shift but not depth-correlated signatures (pattern persists across 10--50\\% contamination ratios; Appendix~\\ref{sec:dose_response}).\n\n\\paragraph{Representation and scorer dependence.}\n$\\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\\Kempirical^{\\text{neural}} = 3$, while Pythia and OLMo match the 15D boundary at $\\Kempirical^{\\text{neural}} = 2$ (Table~\\ref{tab:neural_probe_crossmodel}); the 15D features trade one depth level for cross-model consistency (8/9 configurations $\\Kempirical{\\leq}2$).\n$\\Kempirical$ can also depend on scorer family: on Wikipedia, cross-family scoring reduces $\\Kempirical$ from 2 to 1 ($\\Delta = -2.4$\\,pp; Appendix~\\ref{sec:wiki_domain}), while on C4 it preserves feature rankings ($\\rho > 0.90$) and $\\Kempirical$ for 6/8 configurations (Section~\\ref{sec:transfer}).\nScorer sensitivity is inversely related to domain lexical diversity; we recommend cross-family validation for new domains.\n\n\\paragraph{Domain dependence of $\\Kempirical$.}\nC4 web text yields $\\Kempirical{=}2$ (8/9 configurations, 1B--14B), while arXiv yields $\\Kempirical{=}3$ across five models and four architecture families (Section~\\ref{sec:cross_domain}).\nWith scorer confound controlled, all six models yield $\\Kempirical{=}1$ on Wikipedia (Appendix~\\ref{sec:wiki_domain}), producing a consistent ordering by source domain: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $>$ Wikipedia ($\\Kempirical{=}1$), which correlates with domain-level lexical diversity.\nThe sole C4 exception (Mistral-7B, $\\Kempirical{=}1$) has $\\Kempirical{=}3$ on arXiv, reinforcing the domain-governed interpretation (Appendix~\\ref{sec:boundary_extended}).\nA LaTeX markup ablation confirms that content-level properties dominate (2v3 $\\Delta = -1.8$\\,pp, $\\Kempirical$ unchanged; Appendix~\\ref{sec:latex_ablation}).\n\n\n\\paragraph{Why $\\Kempirical$ matters.}\n$\\Kempirical{=}2$ for web text is not a negative result but a precise measurement: it rules out both $\\Kempirical{=}1$ (no depth signal beyond 0v1) and $\\Kempirical{\\geq}3$ (graduated tracking feasible), while arXiv $\\Kempirical{=}3$ confirms the framework captures real domain-level variation rather than a methodological ceiling.\n$\\Kempirical$ thus serves as an empirical diagnostic of domain properties and is directly prescriptive for curation granularity.\nThe method combines established components (LightGBM, hand-crafted features, ordinal decomposition); the contribution is the measurement framework and the empirical characterization it enables.\n\n\n\n\\paragraph{Practical implications.}\nFor web text ($\\Kempirical{=}2$), graduated depth weighting injects noise beyond the boundary, validating binary filtering as optimal (Section~\\ref{sec:filtering}); for arXiv ($\\Kempirical{=}3$), an additional depth level carries discriminative signal.\nMixed-domain corpora thus require domain-stratified filtering; $\\Kempirical{=}2$ provides post-hoc grounding for the binary approach of \\citet{drayson2025}.\n",
      "numLines": 55,
      "startLine": 1,
      "totalLines": 55
    }
  },
  "sourceToolAssistantUUID": "6902da79-6c78-4047-b1db-d51aecff8d34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-18T14:30:05.058Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Uf2Dd3XRB95mbg3PtcpNpf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bac127d7-0116-4128-b540-d95c783c3284",
  "isSidechain": false,
  "requestId": "req_011CbACCvsMCEqjH5hUV5FY5",
  "type": "assistant",
  "uuid": "5a9718b3-dbbe-4dd3-a8f2-e3831ef06163",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECzDnd2j5NdSKnjmmowK97",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 100323,
      "cache_read_input_tokens": 11841,
      "output_tokens": 621,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 100323,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 621,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 100323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 100323
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Runtime record

_source line 139 · 2026-05-18T14:30:05.124Z_

```json
{
  "parentUuid": "e1f6819a-a25f-4179-a893-7d85350a8b68",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d2df6de3-9fcb-43e8-93cf-c1015ff652d6",
  "timestamp": "2026-05-18T14:30:05.124Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 140_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2（修订评估）— Reviewer 2  **模式**: 继续审稿。论文已更新，你的任务是逐条检查上轮 issue 是否已充分解决，并识别修改是否引入新问题。  ### Venue 信息 - EMNLP 2026, ARR May 2026, Deadline 2026-05-25 - ACL 双栏模板 [review], Long paper 8…",
  "leafUuid": "d2df6de3-9fcb-43e8-93cf-c1015ff652d6",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Runtime record

_source line 141_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on generational depth contamination detection",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671"
}
```

---


### Assistant

_source line 142 · 2026-05-18T14:30:10.993Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now read the updated appendix files and references to check for changes, and also check for new additions (LaTeX ablation, feature ablation, power curve, theta sensitivity figure).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2df6de3-9fcb-43e8-93cf-c1015ff652d6",
  "isSidechain": false,
  "requestId": "req_011CbACDsCN4cTfNR4tfos6a",
  "type": "assistant",
  "uuid": "9b67d304-8b1a-4fdc-b120-1b55a879f7af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWyxzXDRt2P61ogveme4Wr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16637,
      "cache_read_input_tokens": 112164,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 112164,
          "cache_creation_input_tokens": 16637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16637
          },
          "type": "message"
        }
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

_source line 143 · 2026-05-18T14:30:11.496Z_

继续读取更新后的附录和引用文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b67d304-8b1a-4fdc-b120-1b55a879f7af",
  "isSidechain": false,
  "requestId": "req_011CbACDsCN4cTfNR4tfos6a",
  "type": "assistant",
  "uuid": "5a589ee7-7bcf-434e-9bfd-ad389d4f0ffd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWyxzXDRt2P61ogveme4Wr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16637,
      "cache_read_input_tokens": 112164,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 112164,
          "cache_creation_input_tokens": 16637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16637
          },
          "type": "message"
        }
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

_source line 144 · 2026-05-18T14:30:12.954Z_

<details open><summary>🔧 Tool call — Read · `toolu_0134TF3ximiZgRrmX1L82sQ9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a589ee7-7bcf-434e-9bfd-ad389d4f0ffd",
  "isSidechain": false,
  "requestId": "req_011CbACDsCN4cTfNR4tfos6a",
  "type": "assistant",
  "uuid": "08f6a07a-9fc1-4512-a754-5b1955b734df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWyxzXDRt2P61ogveme4Wr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16637,
      "cache_read_input_tokens": 112164,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 112164,
          "cache_creation_input_tokens": 16637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16637
          },
          "type": "message"
        }
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

_source line 145 · 2026-05-18T14:30:13.478Z_

<details><summary>↩ Tool result · `toolu_0134TF3ximiZgRrmX1L82sQ9`</summary>

```text
1	\appendix
2	\section{Supplementary Figures}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
7	\caption{Downstream performance of all filtering strategies (5 seeds, $\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}
8	\label{fig:filtering_strategies}
9	\end{figure}
10	
11	\begin{figure}[t]
12	  \centering
13	  \includegraphics[width=\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}
14	  \caption{Pairwise $\auc$ decay curves for five model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\Kempirical=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}
15	  \label{fig:s1_auc_decay_ci}
16	\end{figure}
17	
18	\section{Supplementary Tables}
19	
20	%%% Feature ranking table (moved from main text)
21	\begin{table}[t]
22	\centering
23	\small
24	\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
25	\label{tab:top_features}
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{cllll}
28	\toprule
29	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
30	\midrule
31	1 & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \texttt{freq\_entropy} & \textbf{\texttt{surp\_d1\_std}} \\
32	2 & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_std}} \\
33	3 & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_d2\_std}} \\
34	\bottomrule
35	\end{tabular}}
36	\end{table}
37	
38	%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)
39	\begin{table*}[t]
40	  \centering
41	  \caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}
42	  \label{tab:s1_transfer}
43	  \begin{tabular}{lcccc}
44	    \toprule
45	    \multirow{2}{*}{\textbf{Train Model}} & \multicolumn{4}{c}{\textbf{Test Model}} \\
46	    \cmidrule(lr){2-5}
47	    & Qwen-rw & Pythia & OLMo & Qwen-cont \\
48	    \midrule
49	    Qwen-rw   & \textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\
50	    Pythia    & 0.2718 & \textbf{0.3856} & 0.3531 & 0.3287 \\
51	    OLMo      & 0.2768 & 0.3450 & \textbf{0.3822} & 0.3244 \\
52	    Qwen-cont & 0.3440 & 0.3284 & 0.3112 & \textbf{0.3875} \\
53	    \bottomrule
54	  \end{tabular}
55	  \vspace{4pt}
56	
57	  \footnotesize
58	  \textit{Transfer retention} between models $A$ and $B$ is defined as $\frac{1}{2}\bigl(\frac{\mathrm{acc}(A \to B)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}} + \frac{\mathrm{acc}(B \to A)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}}\bigr)$.
59	  Notable pairs: Pythia$\leftrightarrow$OLMo 91--92\%, Qwen-cont$\leftrightarrow$Pythia 83--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\%, Qwen-rw$\to$Pythia/OLMo 61--63\%.
60	\end{table*}
61	
62	%%% Table S2: Decoding Ablation AUC (exp-003)
63	\begin{table*}[t]
64	  \centering
65	  \caption{Pairwise AUC with bootstrap 95\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\,vs.\,2 and 2\,vs.\,3 marks the empirical detectability boundary $\Kempirical=2$. Bottom rows report cross-configuration Spearman $\rho$ on per-feature discriminative-power rankings.}
66	  \label{tab:s2_decoding}
67	  \footnotesize
68	  \begin{tabular}{lcccc}
69	    \toprule
70	    \textbf{Depth Pair} & \textbf{Greedy} & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
71	    \midrule
72	    0 vs.\ 1 & $.980\;[.977,\,.982]$ & $.995\;[.993,\,.996]$ & $.988\;[.986,\,.990]$ & $.998\;[.998,\,.999]$ \\
73	    1 vs.\ 2 & $.689\;[.680,\,.698]$ & $.687\;[.677,\,.695]$ & $.689\;[.680,\,.697]$ & $.704\;[.695,\,.713]$ \\
74	    \cmidrule(lr){1-5}
75	    2 vs.\ 3 & $.561\;[.552,\,.571]$ & $.592\;[.582,\,.601]$\rlap{$^\dagger$} & $.590\;[.581,\,.600]$ & $.582\;[.572,\,.592]$ \\
76	    3 vs.\ 4 & $.540\;[.531,\,.550]$ & $.547\;[.537,\,.557]$ & $.539\;[.529,\,.549]$ & $.529\;[.519,\,.540]$ \\
77	    4 vs.\ 5 & $.514\;[.503,\,.524]$ & $.507\;[.496,\,.517]^{\ddagger}$ & $.535\;[.524,\,.545]$ & $.524\;[.513,\,.535]$ \\
78	    \midrule
79	    \multicolumn{5}{l}{\textbf{Cross-config feature Spearman $\rho$}} \\
80	    \midrule
81	    \multicolumn{2}{l}{Greedy vs.\ Nuc $p{=}0.9$} & 0.600 &
82	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}0.7$} & 0.782 \\
83	    \multicolumn{2}{l}{Greedy vs.\ $T{=}0.7$} & 0.914 &
84	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}1.2$} & 0.893 \\
85	    \multicolumn{2}{l}{Greedy vs.\ $T{=}1.2$} & 0.532 &
86	    \multicolumn{1}{l}{$T{=}0.7$ vs.\ $T{=}1.2$} & 0.668 \\
87	    \bottomrule
88	    \multicolumn{5}{l}{${}^{\dagger}$\,CI upper bound (0.601) marginally exceeds $\theta{=}0.60$ by 0.001.} \\
89	    \multicolumn{5}{l}{${}^{\ddagger}$\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}
90	  \end{tabular}
91	\end{table*}
92	
93	%%% Table S2b: Extended K* CI (all models including new additions)
94	\begin{table*}[t]
95	  \centering
96	  \footnotesize
97	  \caption{Extended pairwise $\auc$ with bootstrap 95\% CIs for all 9 model configurations.
98	  This table extends Table~\ref{tab:kstar_ci} in the main text with Qwen-base, Qwen-14B, LLaMA-8B, and Mistral-7B.
99	  8/9 yield $\Kempirical = 2$; Mistral-7B yields $\Kempirical = 1$ (1v2 $\auc < \theta$).}
100	  \label{tab:kstar_ci_extended}
101	  \resizebox{\textwidth}{!}{%
102	  \begin{tabular}{lcccccccccccccccccc}
103	    \toprule
104	     & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} & \multicolumn{2}{c}{Qwen-14B\rlap{$^\ddagger$}} & \multicolumn{2}{c}{Qwen-base} & \multicolumn{2}{c}{LLaMA-8B} & \multicolumn{2}{c}{Mistral-7B} \\
105	    \cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}\cmidrule(lr){12-13}\cmidrule(lr){14-15}\cmidrule(lr){16-17}\cmidrule(lr){18-19}
106	     & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
107	    \midrule
108	    0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\,.967] & .960 & [.956,\,.963] & .987 & [.985,\,.989] & .9225 & [.918,\,.927] & .930 & [.925,\,.935] \\
109	    1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .6145 & [.605,\,.625]\rlap{$^*$} & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} & .621 & [.612,\,.630]\rlap{$^*$} & .626 & [.617,\,.635]\rlap{$^*$} & .6123 & [.603,\,.622]\rlap{$^*$} & .594 & [.584,\,.603] \\
110	    2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .5496 & [.540,\,.560] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] & .549 & [.539,\,.559] & .550 & [.540,\,.560] & .5518 & [.542,\,.562] & .548 & [.538,\,.558] \\
111	    3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & & .524 & [.514,\,.535] & .529 & [.519,\,.540] & .5203 & [.510,\,.531] & .521 & \\
112	    4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & & .515 & [.505,\,.527] & .518 & [.508,\,.529] & .5089 & [.499,\,.519] & .510 & \\
113	    \bottomrule
114	    \multicolumn{19}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all boundary comparisons. Mistral-7B 1v2: $p = 0.001$ but $\auc < \theta$, hence $\Kempirical{=}1$.} \\
115	    \multicolumn{19}{l}{\footnotesize $^\ddagger$Qwen-7B: Qwen2.5-7B (fp16); Qwen-14B: Qwen2.5-14B; scorer: Qwen2.5-1.5B.}
116	  \end{tabular}}
117	
118	\end{table*}
119	
120	%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)
121	\begin{table*}[t]
122	  \centering
123	  \caption{LLM zero-shot depth classification: $5{\times}5$ confusion matrices
124	    (Exp-011). Both frontier LLMs achieve high binary detection accuracy
125	    (GPT-5.5: 0.8780; Claude Opus~4.6: 0.8818) but near-chance 5-class
126	    accuracy (${\sim}0.33$ vs.\ OBD-LightGBM baseline 0.386, evaluated on the full test set $N{=}5{,}000$). GPT-5.5
127	    strongly identifies depth-0 text (recall${=}0.7700$) but collapses on
128	    depth-4 (recall${=}0.0800$), misclassifying 50/100 depth-4 samples as
129	    depth-2. Claude Opus~4.6 shows more uniform errors across depths 1--4,
130	    with depth-4 recall (0.3700) substantially exceeding GPT-5.5.
131	    Per-depth recall comparison with OBD-LightGBM in Table~\ref{tab:s3c_perdepth}.}
132	  \label{tab:s3_llm_zeroshot}
133	
134	  \vspace{0.5em}
135	  \begin{subtable}{0.48\textwidth}
136	    \centering
137	    \caption{GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)}
138	    \label{tab:s3a_gpt55}
139	    \small
140	    \begin{tabular}{lcccccc}
141	      \toprule
142	      & \multicolumn{5}{c}{Predicted Depth} & \\
143	      \cmidrule(lr){2-6}
144	      True & 0 & 1 & 2 & 3 & 4 & Rec. \\
145	      \midrule
146	      0 & \textbf{77} & 18 &  4 &  0 &  1 & .770 \\
147	      1 &  9 & \textbf{19} & 36 & 24 & 12 & .190 \\
148	      2 &  8 & 10 & \textbf{38} & 35 &  9 & .380 \\
149	      3 & 10 & 16 & 35 & \textbf{24} & 15 & .240 \\
150	      4 & 11 & 13 & 50 & 18 &  \textbf{8} & .080 \\
151	      \bottomrule
152	    \end{tabular}
153	  \end{subtable}
154	  \hfill
155	  \begin{subtable}{0.48\textwidth}
156	    \centering
157	    \caption{Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)}
158	    \label{tab:s3b_claude}
159	    \small
160	    \begin{tabular}{lcccccc}
161	      \toprule
162	      & \multicolumn{5}{c}{Predicted Depth} & \\
163	      \cmidrule(lr){2-6}
164	      True & 0 & 1 & 2 & 3 & 4 & Rec. \\
165	      \midrule
166	      0 & \textbf{69} & 26 &  3 &  0 &  2 & .690 \\
167	      1 &  8 & \textbf{21} & 32 & 11 & 28 & .210 \\
168	      2 &  6 & 36 & \textbf{28} &  5 & 25 & .280 \\
169	      3 &  7 & 20 & 31 & \textbf{10} & 31 & .100 \\
170	      4 &  7 & 28 & 22 &  6 & \textbf{37} & .370 \\
171	      \bottomrule
172	    \end{tabular}
173	  \end{subtable}
174	\end{table*}
175	
176	\begin{table}[t]
177	  \centering
178	  \small
179	  \caption{Per-depth recall (\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\geq 2$, consistent with $\Kempirical = 2$.}
180	  \label{tab:s3c_perdepth}
181	  \resizebox{\columnwidth}{!}{%
182	  \begin{tabular}{lccccc}
183	    \toprule
184	    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\
185	    \midrule
186	    OBD-LightGBM & \textbf{96} & \textbf{39} & 14 & 19 & 22 \\
187	    GPT-5.5      & 77 & 19 & \textbf{38} & \textbf{24} &  8 \\
188	    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \textbf{37} \\
189	    \bottomrule
190	  \end{tabular}}
191	\end{table}
192	
193	\paragraph{Zero-shot prompt template.}
194	Both GPT-5.5 and Claude Opus~4.6 received the following system prompt (temperature 0, single-token output constraint):
195	
196	\begin{quote}
197	\small
198	\texttt{The following text passage was produced through recursive LLM generation starting from human-written text (depth~0). Each successive generation feeds the previous output back to the LLM: depth~0 = human, depth~1 = first LLM pass, depth~2 = second pass, etc.}
199	
200	\texttt{Estimate the generational depth (0, 1, 2, 3, or 4) of the passage below. Respond with only the depth number.}
201	
202	\texttt{Text: \{text\}}
203	\end{quote}
204	
205	%%% Table: Token Length and EOS Truncation Analysis
206	\begin{table*}[t]
207	  \centering
208	  \small
209	  \caption{Mean subword token count per depth and EOS truncation rate (\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend within any model; the 0v1 length asymmetry (human texts shorter) makes detection \emph{more conservative}, not inflated. See Section~\ref{sec:length_confound} for discussion.}
210	  \label{tab:token_length}
211	  \begin{tabular}{lcccccccc}
212	    \toprule
213	    & \multicolumn{6}{c}{\textbf{Mean Token Count}} & & \\
214	    \cmidrule(lr){2-7}
215	    \textbf{Model} & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 & Depth 5 & \textbf{EOS Trunc.\ (\%)} & \textbf{Severity} \\
216	    \midrule
217	    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\
218	    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\
219	    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negligible \\
220	    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Moderate \\
221	    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\
222	    \midrule
223	    \multicolumn{9}{l}{\textit{Decoding ablation (Qwen-rw 1.5B)}} \\
224	    \quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\
225	    \quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\
226	    \quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\
227	    \quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\
228	    \bottomrule
229	  \end{tabular}
230	
231	  \vspace{4pt}
232	  \footnotesize
233	  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.
234	\end{table*}
235	
236	%%% Table S4: Dataset Statistics
237	\begin{table}[t]
238	  \centering
239	  \small
240	  \caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}
241	  \label{tab:s4_dataset_stats}
242	  \resizebox{\columnwidth}{!}{%
243	  \begin{tabular}{clrl}
244	    \toprule
245	    \textbf{Depth} & \textbf{$N$ samples} & \textbf{Mean tokens} & \textbf{Source} \\
246	    \midrule
247	    0 & 5{,}000 & 147.8 & C4 validation (human) \\
248	    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\
249	    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\
250	    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\
251	    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
252	    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
253	    \midrule
254	    \multicolumn{2}{l}{Total} & \multicolumn{2}{l}{30{,}000 samples} \\
255	    \bottomrule
256	  \end{tabular}}
257	\end{table}
258	
259	%%% Table S5: Complete 15-D Feature Descriptions
260	\begin{table*}[t]
261	  \centering
262	  \caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}
263	  \label{tab:s5_features}
264	  \begin{tabular}{llp{0.45\textwidth}l}
265	    \toprule
266	    \textbf{Group} & \textbf{Feature} & \textbf{Description} & \textbf{Range} \\
267	    \midrule
268	    \multirow{9}{*}{\rotatebox[origin=c]{90}{\textsc{Surprisal}}}
269	    & \texttt{surp\_mean}   & Mean token surprisal $\frac{1}{T}\sum_t -\log p(x_t \mid x_{&lt;t})$ & $\mathbb{R}^+$ \\
270	    & \texttt{surp\_std}    & Standard deviation of token surprisal & $\mathbb{R}^+$ \\
271	    & \texttt{surp\_skew}   & Skewness of the surprisal distribution & $\mathbb{R}$ \\
272	    & \texttt{surp\_kurt}   & Excess kurtosis of the surprisal distribution & $\mathbb{R}$ \\
273	    & \texttt{surp\_d1\_mean} & Mean of first-order surprisal differences $\Delta s_t = s_{t+1} - s_t$ & $\mathbb{R}$ \\
274	    & \texttt{surp\_d1\_std}  & Std of first-order surprisal differences & $\mathbb{R}^+$ \\
275	    & \texttt{surp\_d1\_skew} & Skewness of first-order surprisal differences & $\mathbb{R}$ \\
276	    & \texttt{surp\_d2\_mean} & Mean of second-order differences $\Delta^2 s_t$ & $\mathbb{R}$ \\
277	    & \texttt{surp\_d2\_std}  & Std of second-order surprisal differences & $\mathbb{R}^+$ \\
278	    \midrule
279	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Lex}}}
280	    & \texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\
281	    & \texttt{hapax\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\
282	    & \texttt{self\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\
283	    \midrule
284	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Freq}}}
285	    & \texttt{freq\_kurtosis}  & Excess kurtosis of word frequency distribution & $\mathbb{R}$ \\
286	    & \texttt{freq\_entropy}   & Shannon entropy of word frequencies: $-\sum p_w \log_2 p_w$ & $\mathbb{R}^+$ \\
287	    & \texttt{low\_freq\_ratio} & Proportion of vocabulary with count $\leq 2$ & $[0, 1]$ \\
288	    \bottomrule
289	  \end{tabular}
290	\end{table*}
291	
292	%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap
293	\begin{table*}[t]
294	\begin{minipage}[t]{0.45\textwidth}
295	  \centering
296	  \small
297	  \captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \texttt{doc\_id} to prevent data leakage from the same seed document appearing in both train and test.}
298	  \label{tab:s6_lgbm_params}
299	  \begin{tabular}{ll}
300	    \toprule
301	    \textbf{Parameter} & \textbf{Value} \\
302	    \midrule
303	    \texttt{n\_estimators}      & 200 \\
304	    \texttt{learning\_rate}     & 0.05 \\
305	    \texttt{max\_depth}         & 6 \\
306	    \texttt{num\_leaves}        & 31 \\
307	    \texttt{verbose}            & $-1$ \\
308	    \texttt{n\_jobs}            & $-1$ (all cores) \\
309	    Cross-validation            & 5-fold GroupKFold \\
310	    Grouping key                & \texttt{doc\_id} \\
311	    Objective                   & Binary (per depth pair) \\
312	    \bottomrule
313	  \end{tabular}
314	\end{minipage}\hfill
315	\begin{minipage}[t]{0.52\textwidth}
316	  \centering
317	  \small
318	  \captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}
319	  \label{tab:s7_neural_probe}
320	  \resizebox{\textwidth}{!}{%
321	  \begin{tabular}{ll}
322	    \toprule
323	    \textbf{Component} & \textbf{Details} \\
324	    \midrule
325	    \multicolumn{2}{l}{\textit{Embedding extraction}} \\
326	    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\
327	    Representation    & Last hidden state, attention-masked avg pool \\
328	    Embedding dim     & 1536 / 2048 / 2048 \\
329	    Max sequence len   & 512 tokens \\
330	    \midrule
331	    \multicolumn{2}{l}{\textit{MLP classifier}} \\
332	    Architecture      & $d_{\text{emb}} \to 512 \to 256 \to 6$ \\
333	    Activations       & ReLU \\
334	    Dropout           & 0.1 (after each hidden layer) \\
335	    Output            & 6-class softmax \\
336	    \midrule
337	    \multicolumn{2}{l}{\textit{Training}} \\
338	    Optimizer         & Adam ($\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\
339	    Loss              & Cross-entropy \\
340	    Batch size        & 256 \\
341	    Max epochs        & 20 \\
342	    Early stopping    & Patience = 5 (validation loss) \\
343	    Cross-validation  & 5-fold GroupKFold \\
344	    \bottomrule
345	  \end{tabular}%
346	  }
347	\end{minipage}
348	\end{table*}
349	
350	%%% Table S8: Per-Model Bootstrap CI Results (exp-007)
351	\begin{table*}[t]
352	  \centering
353	  \footnotesize
354	  \caption{Pairwise AUC with bootstrap 95\% confidence intervals for four model-mode configurations (Exp-007, 1{,}000 bootstrap resamples). The horizontal rule separates depth pairs above and below the detectability threshold $\theta = 0.60$. Permutation $p$-values test $H_0\colon \auc = 0.50$. All pairs are significant at $p < 0.01$ except OLMo 3\,vs.\,4 ($p = 0.064$) and 4\,vs.\,5 ($p = 0.232$), consistent with convergence to chance at deeper generations.}
355	  \label{tab:s8_cv_folds}
356	  \begin{tabular}{lcccc}
357	    \toprule
358	    \textbf{Depth Pair} & \textbf{Qwen-rewrite} & \textbf{Pythia-1.4B} & \textbf{OLMo-1B} & \textbf{Qwen-cont} \\
359	    \midrule
360	    0 vs.\ 1
361	      & $.996\;[.995,\,.997]$
362	      & $.993\;[.992,\,.994]$
363	      & $.997\;[.996,\,.998]$
364	      & $.997\;[.996,\,.998]$ \\
365	    1 vs.\ 2
366	      & $.696\;[.686,\,.704]$
367	      & $.654\;[.645,\,.663]$
368	      & $.615\;[.605,\,.625]$
369	      & $.611\;[.602,\,.621]$ \\
370	    \cmidrule(lr){1-5}
371	    2 vs.\ 3
372	      & $.589\;[.580,\,.599]$
373	      & $.551\;[.542,\,.563]$
374	      & $.550\;[.540,\,.560]$
375	      & $.561\;[.551,\,.571]$ \\
376	    3 vs.\ 4
377	      & $.544\;[.533,\,.555]$
378	      & $.515\;[.504,\,.526]$
379	      & $.509\;[.497,\,.520]^{\dagger}$
380	      & $.541\;[.531,\,.551]$ \\
381	    4 vs.\ 5
382	      & $.534\;[.524,\,.545]$
383	      & $.514\;[.502,\,.525]$
384	      & $.505\;[.493,\,.515]^{\ddagger}$
385	      & $.514\;[.504,\,.526]$ \\
386	    \bottomrule
387	  \end{tabular}
388	
389	  \vspace{4pt}
390	  \footnotesize
391	  Each cell: AUC $[95\%$ CI$]$. CI from 1{,}000 bootstrap resamples; $p$-values from 500-resample permutation test.
392	  ${}^{\dagger}$\,$p = 0.064$;\; ${}^{\ddagger}$\,$p = 0.232$;\; all other pairs $p < 0.01$.
393	\end{table*}
394	
395	%%% Table S9: Binary Detector Spearman ρ (exp-012)
396	\begin{table*}[t]
397	  \centering
398	  \small
399	  \caption{Spearman rank correlation ($\rho$) between binary detector confidence scores and true generational depth, and 6-class depth classification accuracy (Exp-012). Three metrics: log-PPL from the reference model (DivEye), log-PPL from the observer model, and PPL ratio (Binoculars; observer: Pythia-1.4B, performer: OLMo-1B). Random baseline for 6-class accuracy: 0.167. While statistically significant, correlations are driven by the 0v1 boundary; confidence scores do not monotonically track depth beyond generation~1. Qwen-rewrite exhibits reversed sign ($\rho > 0$), indicating that generation mode alters the direction of binary confidence's relationship with depth.}
400	  \label{tab:s9_binary_spearman}
401	  \begin{tabular}{lcccc}
402	    \toprule
403	    & \textbf{Qwen-rw} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} \\
404	    \midrule
405	    \multicolumn{5}{l}{\textit{Spearman $\rho$ with true depth}} \\
406	    \quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\
407	    \quad log-PPL (observer) & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\
408	    \quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\
409	    \midrule
410	    \multicolumn{5}{l}{\textit{Classification}} \\
411	    \quad 6-class accuracy    & 0.199    & 0.130    & 0.127    & 0.183 \\
412	    \midrule
413	    \multicolumn{5}{l}{Random baseline: 0.167 \quad $\Kempirical^{\text{binary}} = 1$ \quad $\Kempirical^{\text{OBD}} = 2$} \\
414	    \bottomrule
415	  \end{tabular}
416	\end{table*}
417	
418	%%% Table S10: Pythia Decoding Ablation (exp-020)
419	\begin{table*}[t]
420	  \centering
421	  \small
422	  \caption{Pairwise $\auc$ with bootstrap 95\% CIs across depth pairs for Pythia-1.4B under four decoding configurations (Exp-020; 10{,}000 bootstrap resamples). Complements Table~\ref{tab:s2_decoding} (Qwen-rewrite) with a second model family. $^\dagger$Greedy decoding triggers repetition collapse in Pythia-1.4B (4-gram repeat rate: $d_0{=}0.01 \to d_1{=}0.72$), inflating 0v1 and 1v2 AUC via lexical degeneracy rather than depth-discriminative features.}
423	  \label{tab:s10_pythia_decoding}
424	  \begin{tabular}{lcccc}
425	    \toprule
426	    \textbf{Depth Pair} & \textbf{Greedy}$^\dagger$ & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
427	    \midrule
428	    0 vs.\ 1 & .9992 & .9948 & .9965 & .9933 \\
429	    1 vs.\ 2 & .8838 & .6770 & .7265 & .6172 \\
430	    \cmidrule(lr){1-5}
431	    2 vs.\ 3 & .5342 & .5549 & .5941 & .5226 \\
432	    3 vs.\ 4 & .5228 & .5299 & .5698 & .5170 \\
433	    4 vs.\ 5 & .5162 & .5013 & .5284 & .5051 \\
434	    \midrule
435	    $\Kempirical$ & 2 & 2 & 2 & 2 \\
436	    \bottomrule
437	  \end{tabular}
438	\end{table*}
439	
440	%%% Table S11: Length Ablation (exp-021)
441	\begin{table*}[t]
442	  \centering
443	  \small
444	  \caption{Pairwise $\auc$ across depth pairs for three segment lengths (Exp-021; Qwen2.5-1.5B base, continuation mode). $\Kempirical{=}2$ is confirmed for 128 and 256 tokens; 512 tokens yields point estimate $\Kempirical{=}2$ but the 1v2 bootstrap CI lower bound falls marginally below $\theta$.}
445	  \label{tab:s11_length_ablation}
446	  \begin{tabular}{lccc}
447	    \toprule
448	    \textbf{Depth Pair} & \textbf{128 tokens} & \textbf{256 tokens} & \textbf{512 tokens} \\
449	    \midrule
450	    0 vs.\ 1 & .9948 & .9956 & .9961 \\
451	    1 vs.\ 2 & .6219 & .6282 & .6073$^\dagger$ \\
452	    \cmidrule(lr){1-4}
453	    2 vs.\ 3 & .5531 & .5609 & .5482 \\
454	    3 vs.\ 4 & .5218 & .5305 & .5196 \\
455	    4 vs.\ 5 & .5104 & .5142 & .5078 \\
456	    \midrule
457	    $\Kempirical$ & 2 & 2 & 2$^\dagger$ \\
458	    \bottomrule
459	    \multicolumn{4}{l}{\footnotesize $^\dagger$CI $[0.5979,\,0.6166]$; lower bound ${<}\theta{=}0.60$.}
460	  \end{tabular}
461	\end{table*}
462	
463	%%% Table S12: Domain Ablation
464	\begin{table*}[t]
465	  \centering
466	  \small
467	  \caption{Pairwise $\auc$ across depth pairs for three text domains (Qwen2.5-1.5B base, continuation mode). Tests generalization of $\Kempirical{=}2$ beyond C4 web text to structured and technical domains. Same-family scoring (Qwen-1.5B); cross-family controlled values in Table~\ref{tab:wiki_domain}.}
468	  \label{tab:s12_domain_ablation}
469	  \begin{tabular}{lccc}
470	    \toprule
471	    \textbf{Depth Pair} & \textbf{C4 (web)} & \textbf{Wikipedia} & \textbf{arXiv} \\
472	    \midrule
473	    0 vs.\ 1 & .9971 & .996 & .9984 \\
474	    1 vs.\ 2 & .6112 & .6193 & .8580 \\
475	    \cmidrule(lr){1-4}
476	    2 vs.\ 3 & .5609 & .556 & .6427 \\
477	    3 vs.\ 4 & .5409 & .528 & .5813 \\
478	    4 vs.\ 5 & .5141 & .509 & .5346 \\
479	    \midrule
480	    $\Kempirical$ & 2 & 2 & 3 \\
481	    \bottomrule
482	  \end{tabular}
483	\end{table*}
484	
485	%%% Table S13: Scorer Sensitivity Analysis
486	\begin{table*}[t]
487	  \centering
488	  \small
489	  \caption{Scorer sensitivity: $\Kempirical$ under self-scoring vs.\ cross-scoring. Self-scorer uses the generator's own model family for feature extraction; cross-scorer uses alternative models (Pythia-1.4B, OLMo-1B). $\Kempirical$ agreement across scorer conditions indicates the boundary is governed by the generation process. Cross-scoring reduces $\Kempirical$ only for the most marginal self-scorer condition (Qwen-continuation).}
490	  \label{tab:s13_scorer_sensitivity}
491	  \begin{tabular}{lccccc}
492	    \toprule
493	    & & \multicolumn{3}{c}{\textbf{Scorer}} & \\
494	    \cmidrule(lr){3-5}
495	    \textbf{Generator} & \textbf{Mode} & \textbf{Self} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Agreement} \\
496	    \midrule
497	    Qwen-1.5B-Instruct & Rewrite      & 2 (.696) & 2 & 2 & \checkmark \\
498	    Qwen-1.5B-Instruct & Continuation & 2 (.611) & 1 & 1 & $\times$ \\
499	    Qwen-1.5B (base)   & Continuation & 2 (.626) & 2 & 2 & \checkmark \\
500	    Pythia-1.4B         & Continuation & 2 (.654) & 2 & 2 & \checkmark \\
501	    OLMo-1B             & Continuation & 2 (.615) & 2 & 2 & \checkmark \\
502	    Qwen-7B             & Continuation & 2 (.618) & 2 & 2 & \checkmark \\
503	    Mistral-7B          & Continuation & 1 (.594) & 1 & 1 & \checkmark \\
504	    \bottomrule
505	  \end{tabular}
506	\end{table*}
507	
508	\clearpage
509	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08f6a07a-9fc1-4512-a754-5b1955b734df",
  "isSidechain": false,
  "promptId": "a76e3a98-645a-445f-972e-aeb6711b75d1",
  "type": "user",
  "uuid": "31924bab-b0ff-4caa-b2e4-2feaf281535d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
      "content": "\\appendix\n\\section{Supplementary Figures}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_filtering_strategies.pdf}\n\\caption{Downstream performance of all filtering strategies (5 seeds, $\\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}\n\\label{fig:filtering_strategies}\n\\end{figure}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}\n  \\caption{Pairwise $\\auc$ decay curves for five model-mode configurations with bootstrap 95\\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\\Kempirical=2$ boundary where $\\auc$ drops below $\\theta=0.60$. This figure complements Figure~\\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}\n  \\label{fig:s1_auc_decay_ci}\n\\end{figure}\n\n\\section{Supplementary Tables}\n\n%%% Feature ranking table (moved from main text)\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Top-3 features by single-feature $\\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}\n\\label{tab:top_features}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{cllll}\n\\toprule\nRank & Pythia & OLMo & Qwen-rw & Qwen-cont \\\\\n\\midrule\n1 & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_std}} & \\texttt{freq\\_entropy} & \\textbf{\\texttt{surp\\_d1\\_std}} \\\\\n2 & \\textbf{\\texttt{surp\\_d2\\_std}} & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_std}} & \\textbf{\\texttt{surp\\_std}} \\\\\n3 & \\textbf{\\texttt{surp\\_std}} & \\textbf{\\texttt{surp\\_d2\\_std}} & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_d2\\_std}} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}\n  \\label{tab:s1_transfer}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\multirow{2}{*}{\\textbf{Train Model}} & \\multicolumn{4}{c}{\\textbf{Test Model}} \\\\\n    \\cmidrule(lr){2-5}\n    & Qwen-rw & Pythia & OLMo & Qwen-cont \\\\\n    \\midrule\n    Qwen-rw   & \\textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\\\\n    Pythia    & 0.2718 & \\textbf{0.3856} & 0.3531 & 0.3287 \\\\\n    OLMo      & 0.2768 & 0.3450 & \\textbf{0.3822} & 0.3244 \\\\\n    Qwen-cont & 0.3440 & 0.3284 & 0.3112 & \\textbf{0.3875} \\\\\n    \\bottomrule\n  \\end{tabular}\n  \\vspace{4pt}\n\n  \\footnotesize\n  \\textit{Transfer retention} between models $A$ and $B$ is defined as $\\frac{1}{2}\\bigl(\\frac{\\mathrm{acc}(A \\to B)}{\\sqrt{\\mathrm{acc}(A \\to A) \\cdot \\mathrm{acc}(B \\to B)}} + \\frac{\\mathrm{acc}(B \\to A)}{\\sqrt{\\mathrm{acc}(A \\to A) \\cdot \\mathrm{acc}(B \\to B)}}\\bigr)$.\n  Notable pairs: Pythia$\\leftrightarrow$OLMo 91--92\\%, Qwen-cont$\\leftrightarrow$Pythia 83--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\%, Qwen-rw$\\to$Pythia/OLMo 61--63\\%.\n\\end{table*}\n\n%%% Table S2: Decoding Ablation AUC (exp-003)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Pairwise AUC with bootstrap 95\\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\\,vs.\\,2 and 2\\,vs.\\,3 marks the empirical detectability boundary $\\Kempirical=2$. Bottom rows report cross-configuration Spearman $\\rho$ on per-feature discriminative-power rankings.}\n  \\label{tab:s2_decoding}\n  \\footnotesize\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Greedy} & \\textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \\textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \\textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\\\\n    \\midrule\n    0 vs.\\ 1 & $.980\\;[.977,\\,.982]$ & $.995\\;[.993,\\,.996]$ & $.988\\;[.986,\\,.990]$ & $.998\\;[.998,\\,.999]$ \\\\\n    1 vs.\\ 2 & $.689\\;[.680,\\,.698]$ & $.687\\;[.677,\\,.695]$ & $.689\\;[.680,\\,.697]$ & $.704\\;[.695,\\,.713]$ \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3 & $.561\\;[.552,\\,.571]$ & $.592\\;[.582,\\,.601]$\\rlap{$^\\dagger$} & $.590\\;[.581,\\,.600]$ & $.582\\;[.572,\\,.592]$ \\\\\n    3 vs.\\ 4 & $.540\\;[.531,\\,.550]$ & $.547\\;[.537,\\,.557]$ & $.539\\;[.529,\\,.549]$ & $.529\\;[.519,\\,.540]$ \\\\\n    4 vs.\\ 5 & $.514\\;[.503,\\,.524]$ & $.507\\;[.496,\\,.517]^{\\ddagger}$ & $.535\\;[.524,\\,.545]$ & $.524\\;[.513,\\,.535]$ \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textbf{Cross-config feature Spearman $\\rho$}} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Greedy vs.\\ Nuc $p{=}0.9$} & 0.600 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}0.7$} & 0.782 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}0.7$} & 0.914 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}1.2$} & 0.893 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}1.2$} & 0.532 &\n    \\multicolumn{1}{l}{$T{=}0.7$ vs.\\ $T{=}1.2$} & 0.668 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{${}^{\\dagger}$\\,CI upper bound (0.601) marginally exceeds $\\theta{=}0.60$ by 0.001.} \\\\\n    \\multicolumn{5}{l}{${}^{\\ddagger}$\\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S2b: Extended K* CI (all models including new additions)\n\\begin{table*}[t]\n  \\centering\n  \\footnotesize\n  \\caption{Extended pairwise $\\auc$ with bootstrap 95\\% CIs for all 9 model configurations.\n  This table extends Table~\\ref{tab:kstar_ci} in the main text with Qwen-base, Qwen-14B, LLaMA-8B, and Mistral-7B.\n  8/9 yield $\\Kempirical = 2$; Mistral-7B yields $\\Kempirical = 1$ (1v2 $\\auc < \\theta$).}\n  \\label{tab:kstar_ci_extended}\n  \\resizebox{\\textwidth}{!}{%\n  \\begin{tabular}{lcccccccccccccccccc}\n    \\toprule\n     & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} & \\multicolumn{2}{c}{Qwen-14B\\rlap{$^\\ddagger$}} & \\multicolumn{2}{c}{Qwen-base} & \\multicolumn{2}{c}{LLaMA-8B} & \\multicolumn{2}{c}{Mistral-7B} \\\\\n    \\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\\cmidrule(lr){12-13}\\cmidrule(lr){14-15}\\cmidrule(lr){16-17}\\cmidrule(lr){18-19}\n     & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n    \\midrule\n    0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\\,.967] & .960 & [.956,\\,.963] & .987 & [.985,\\,.989] & .9225 & [.918,\\,.927] & .930 & [.925,\\,.935] \\\\\n    1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6539 & [.645,\\,.663]\\rlap{$^*$} & .6145 & [.605,\\,.625]\\rlap{$^*$} & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} & .621 & [.612,\\,.630]\\rlap{$^*$} & .626 & [.617,\\,.635]\\rlap{$^*$} & .6123 & [.603,\\,.622]\\rlap{$^*$} & .594 & [.584,\\,.603] \\\\\n    2v3 & .5893 & [.580,\\,.599] & .5514 & [.542,\\,.563] & .5496 & [.540,\\,.560] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] & .549 & [.539,\\,.559] & .550 & [.540,\\,.560] & .5518 & [.542,\\,.562] & .548 & [.538,\\,.558] \\\\\n    3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & & .524 & [.514,\\,.535] & .529 & [.519,\\,.540] & .5203 & [.510,\\,.531] & .521 & \\\\\n    4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & & .515 & [.505,\\,.527] & .518 & [.508,\\,.529] & .5089 & [.499,\\,.519] & .510 & \\\\\n    \\bottomrule\n    \\multicolumn{19}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all boundary comparisons. Mistral-7B 1v2: $p = 0.001$ but $\\auc < \\theta$, hence $\\Kempirical{=}1$.} \\\\\n    \\multicolumn{19}{l}{\\footnotesize $^\\ddagger$Qwen-7B: Qwen2.5-7B (fp16); Qwen-14B: Qwen2.5-14B; scorer: Qwen2.5-1.5B.}\n  \\end{tabular}}\n\n\\end{table*}\n\n%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)\n\\begin{table*}[t]\n  \\centering\n  \\caption{LLM zero-shot depth classification: $5{\\times}5$ confusion matrices\n    (Exp-011). Both frontier LLMs achieve high binary detection accuracy\n    (GPT-5.5: 0.8780; Claude Opus~4.6: 0.8818) but near-chance 5-class\n    accuracy (${\\sim}0.33$ vs.\\ OBD-LightGBM baseline 0.386, evaluated on the full test set $N{=}5{,}000$). GPT-5.5\n    strongly identifies depth-0 text (recall${=}0.7700$) but collapses on\n    depth-4 (recall${=}0.0800$), misclassifying 50/100 depth-4 samples as\n    depth-2. Claude Opus~4.6 shows more uniform errors across depths 1--4,\n    with depth-4 recall (0.3700) substantially exceeding GPT-5.5.\n    Per-depth recall comparison with OBD-LightGBM in Table~\\ref{tab:s3c_perdepth}.}\n  \\label{tab:s3_llm_zeroshot}\n\n  \\vspace{0.5em}\n  \\begin{subtable}{0.48\\textwidth}\n    \\centering\n    \\caption{GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)}\n    \\label{tab:s3a_gpt55}\n    \\small\n    \\begin{tabular}{lcccccc}\n      \\toprule\n      & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n      \\cmidrule(lr){2-6}\n      True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n      \\midrule\n      0 & \\textbf{77} & 18 &  4 &  0 &  1 & .770 \\\\\n      1 &  9 & \\textbf{19} & 36 & 24 & 12 & .190 \\\\\n      2 &  8 & 10 & \\textbf{38} & 35 &  9 & .380 \\\\\n      3 & 10 & 16 & 35 & \\textbf{24} & 15 & .240 \\\\\n      4 & 11 & 13 & 50 & 18 &  \\textbf{8} & .080 \\\\\n      \\bottomrule\n    \\end{tabular}\n  \\end{subtable}\n  \\hfill\n  \\begin{subtable}{0.48\\textwidth}\n    \\centering\n    \\caption{Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)}\n    \\label{tab:s3b_claude}\n    \\small\n    \\begin{tabular}{lcccccc}\n      \\toprule\n      & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n      \\cmidrule(lr){2-6}\n      True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n      \\midrule\n      0 & \\textbf{69} & 26 &  3 &  0 &  2 & .690 \\\\\n      1 &  8 & \\textbf{21} & 32 & 11 & 28 & .210 \\\\\n      2 &  6 & 36 & \\textbf{28} &  5 & 25 & .280 \\\\\n      3 &  7 & 20 & 31 & \\textbf{10} & 31 & .100 \\\\\n      4 &  7 & 28 & 22 &  6 & \\textbf{37} & .370 \\\\\n      \\bottomrule\n    \\end{tabular}\n  \\end{subtable}\n\\end{table*}\n\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Per-depth recall (\\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\\geq 2$, consistent with $\\Kempirical = 2$.}\n  \\label{tab:s3c_perdepth}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lccccc}\n    \\toprule\n    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\\\\n    \\midrule\n    OBD-LightGBM & \\textbf{96} & \\textbf{39} & 14 & 19 & 22 \\\\\n    GPT-5.5      & 77 & 19 & \\textbf{38} & \\textbf{24} &  8 \\\\\n    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \\textbf{37} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n\\paragraph{Zero-shot prompt template.}\nBoth GPT-5.5 and Claude Opus~4.6 received the following system prompt (temperature 0, single-token output constraint):\n\n\\begin{quote}\n\\small\n\\texttt{The following text passage was produced through recursive LLM generation starting from human-written text (depth~0). Each successive generation feeds the previous output back to the LLM: depth~0 = human, depth~1 = first LLM pass, depth~2 = second pass, etc.}\n\n\\texttt{Estimate the generational depth (0, 1, 2, 3, or 4) of the passage below. Respond with only the depth number.}\n\n\\texttt{Text: \\{text\\}}\n\\end{quote}\n\n%%% Table: Token Length and EOS Truncation Analysis\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Mean subword token count per depth and EOS truncation rate (\\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend within any model; the 0v1 length asymmetry (human texts shorter) makes detection \\emph{more conservative}, not inflated. See Section~\\ref{sec:length_confound} for discussion.}\n  \\label{tab:token_length}\n  \\begin{tabular}{lcccccccc}\n    \\toprule\n    & \\multicolumn{6}{c}{\\textbf{Mean Token Count}} & & \\\\\n    \\cmidrule(lr){2-7}\n    \\textbf{Model} & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 & Depth 5 & \\textbf{EOS Trunc.\\ (\\%)} & \\textbf{Severity} \\\\\n    \\midrule\n    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\\\\n    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\\\\n    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negligible \\\\\n    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Moderate \\\\\n    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\\\\n    \\midrule\n    \\multicolumn{9}{l}{\\textit{Decoding ablation (Qwen-rw 1.5B)}} \\\\\n    \\quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\\\\n    \\quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\\\\n    \\quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\\\\n    \\quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\\\\n    \\bottomrule\n  \\end{tabular}\n\n  \\vspace{4pt}\n  \\footnotesize\n  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.\n\\end{table*}\n\n%%% Table S4: Dataset Statistics\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}\n  \\label{tab:s4_dataset_stats}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{clrl}\n    \\toprule\n    \\textbf{Depth} & \\textbf{$N$ samples} & \\textbf{Mean tokens} & \\textbf{Source} \\\\\n    \\midrule\n    0 & 5{,}000 & 147.8 & C4 validation (human) \\\\\n    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\\\\n    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\\\\n    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\\\\n    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Total} & \\multicolumn{2}{l}{30{,}000 samples} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S5: Complete 15-D Feature Descriptions\n\\begin{table*}[t]\n  \\centering\n  \\caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}\n  \\label{tab:s5_features}\n  \\begin{tabular}{llp{0.45\\textwidth}l}\n    \\toprule\n    \\textbf{Group} & \\textbf{Feature} & \\textbf{Description} & \\textbf{Range} \\\\\n    \\midrule\n    \\multirow{9}{*}{\\rotatebox[origin=c]{90}{\\textsc{Surprisal}}}\n    & \\texttt{surp\\_mean}   & Mean token surprisal $\\frac{1}{T}\\sum_t -\\log p(x_t \\mid x_{&lt;t})$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_std}    & Standard deviation of token surprisal & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_skew}   & Skewness of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_kurt}   & Excess kurtosis of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_mean} & Mean of first-order surprisal differences $\\Delta s_t = s_{t+1} - s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_std}  & Std of first-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_d1\\_skew} & Skewness of first-order surprisal differences & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_mean} & Mean of second-order differences $\\Delta^2 s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_std}  & Std of second-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Lex}}}\n    & \\texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\\\\n    & \\texttt{hapax\\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\\\\n    & \\texttt{self\\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Freq}}}\n    & \\texttt{freq\\_kurtosis}  & Excess kurtosis of word frequency distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{freq\\_entropy}   & Shannon entropy of word frequencies: $-\\sum p_w \\log_2 p_w$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{low\\_freq\\_ratio} & Proportion of vocabulary with count $\\leq 2$ & $[0, 1]$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap\n\\begin{table*}[t]\n\\begin{minipage}[t]{0.45\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \\texttt{doc\\_id} to prevent data leakage from the same seed document appearing in both train and test.}\n  \\label{tab:s6_lgbm_params}\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Parameter} & \\textbf{Value} \\\\\n    \\midrule\n    \\texttt{n\\_estimators}      & 200 \\\\\n    \\texttt{learning\\_rate}     & 0.05 \\\\\n    \\texttt{max\\_depth}         & 6 \\\\\n    \\texttt{num\\_leaves}        & 31 \\\\\n    \\texttt{verbose}            & $-1$ \\\\\n    \\texttt{n\\_jobs}            & $-1$ (all cores) \\\\\n    Cross-validation            & 5-fold GroupKFold \\\\\n    Grouping key                & \\texttt{doc\\_id} \\\\\n    Objective                   & Binary (per depth pair) \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{minipage}\\hfill\n\\begin{minipage}[t]{0.52\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}\n  \\label{tab:s7_neural_probe}\n  \\resizebox{\\textwidth}{!}{%\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Component} & \\textbf{Details} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Embedding extraction}} \\\\\n    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\\\\n    Representation    & Last hidden state, attention-masked avg pool \\\\\n    Embedding dim     & 1536 / 2048 / 2048 \\\\\n    Max sequence len   & 512 tokens \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{MLP classifier}} \\\\\n    Architecture      & $d_{\\text{emb}} \\to 512 \\to 256 \\to 6$ \\\\\n    Activations       & ReLU \\\\\n    Dropout           & 0.1 (after each hidden layer) \\\\\n    Output            & 6-class softmax \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Training}} \\\\\n    Optimizer         & Adam ($\\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\\\\n    Loss              & Cross-entropy \\\\\n    Batch size        & 256 \\\\\n    Max epochs        & 20 \\\\\n    Early stopping    & Patience = 5 (validation loss) \\\\\n    Cross-validation  & 5-fold GroupKFold \\\\\n    \\bottomrule\n  \\end{tabular}%\n  }\n\\end{minipage}\n\\end{table*}\n\n%%% Table S8: Per-Model Bootstrap CI Results (exp-007)\n\\begin{table*}[t]\n  \\centering\n  \\footnotesize\n  \\caption{Pairwise AUC with bootstrap 95\\% confidence intervals for four model-mode configurations (Exp-007, 1{,}000 bootstrap resamples). The horizontal rule separates depth pairs above and below the detectability threshold $\\theta = 0.60$. Permutation $p$-values test $H_0\\colon \\auc = 0.50$. All pairs are significant at $p < 0.01$ except OLMo 3\\,vs.\\,4 ($p = 0.064$) and 4\\,vs.\\,5 ($p = 0.232$), consistent with convergence to chance at deeper generations.}\n  \\label{tab:s8_cv_folds}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Qwen-rewrite} & \\textbf{Pythia-1.4B} & \\textbf{OLMo-1B} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    0 vs.\\ 1\n      & $.996\\;[.995,\\,.997]$\n      & $.993\\;[.992,\\,.994]$\n      & $.997\\;[.996,\\,.998]$\n      & $.997\\;[.996,\\,.998]$ \\\\\n    1 vs.\\ 2\n      & $.696\\;[.686,\\,.704]$\n      & $.654\\;[.645,\\,.663]$\n      & $.615\\;[.605,\\,.625]$\n      & $.611\\;[.602,\\,.621]$ \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3\n      & $.589\\;[.580,\\,.599]$\n      & $.551\\;[.542,\\,.563]$\n      & $.550\\;[.540,\\,.560]$\n      & $.561\\;[.551,\\,.571]$ \\\\\n    3 vs.\\ 4\n      & $.544\\;[.533,\\,.555]$\n      & $.515\\;[.504,\\,.526]$\n      & $.509\\;[.497,\\,.520]^{\\dagger}$\n      & $.541\\;[.531,\\,.551]$ \\\\\n    4 vs.\\ 5\n      & $.534\\;[.524,\\,.545]$\n      & $.514\\;[.502,\\,.525]$\n      & $.505\\;[.493,\\,.515]^{\\ddagger}$\n      & $.514\\;[.504,\\,.526]$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\n  \\vspace{4pt}\n  \\footnotesize\n  Each cell: AUC $[95\\%$ CI$]$. CI from 1{,}000 bootstrap resamples; $p$-values from 500-resample permutation test.\n  ${}^{\\dagger}$\\,$p = 0.064$;\\; ${}^{\\ddagger}$\\,$p = 0.232$;\\; all other pairs $p < 0.01$.\n\\end{table*}\n\n%%% Table S9: Binary Detector Spearman ρ (exp-012)\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Spearman rank correlation ($\\rho$) between binary detector confidence scores and true generational depth, and 6-class depth classification accuracy (Exp-012). Three metrics: log-PPL from the reference model (DivEye), log-PPL from the observer model, and PPL ratio (Binoculars; observer: Pythia-1.4B, performer: OLMo-1B). Random baseline for 6-class accuracy: 0.167. While statistically significant, correlations are driven by the 0v1 boundary; confidence scores do not monotonically track depth beyond generation~1. Qwen-rewrite exhibits reversed sign ($\\rho > 0$), indicating that generation mode alters the direction of binary confidence's relationship with depth.}\n  \\label{tab:s9_binary_spearman}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Qwen-rw} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textit{Spearman $\\rho$ with true depth}} \\\\\n    \\quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\\\\n    \\quad log-PPL (observer) & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\\\\n    \\quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textit{Classification}} \\\\\n    \\quad 6-class accuracy    & 0.199    & 0.130    & 0.127    & 0.183 \\\\\n    \\midrule\n    \\multicolumn{5}{l}{Random baseline: 0.167 \\quad $\\Kempirical^{\\text{binary}} = 1$ \\quad $\\Kempirical^{\\text{OBD}} = 2$} \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S10: Pythia Decoding Ablation (exp-020)\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Pairwise $\\auc$ with bootstrap 95\\% CIs across depth pairs for Pythia-1.4B under four decoding configurations (Exp-020; 10{,}000 bootstrap resamples). Complements Table~\\ref{tab:s2_decoding} (Qwen-rewrite) with a second model family. $^\\dagger$Greedy decoding triggers repetition collapse in Pythia-1.4B (4-gram repeat rate: $d_0{=}0.01 \\to d_1{=}0.72$), inflating 0v1 and 1v2 AUC via lexical degeneracy rather than depth-discriminative features.}\n  \\label{tab:s10_pythia_decoding}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Greedy}$^\\dagger$ & \\textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \\textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \\textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\\\\n    \\midrule\n    0 vs.\\ 1 & .9992 & .9948 & .9965 & .9933 \\\\\n    1 vs.\\ 2 & .8838 & .6770 & .7265 & .6172 \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3 & .5342 & .5549 & .5941 & .5226 \\\\\n    3 vs.\\ 4 & .5228 & .5299 & .5698 & .5170 \\\\\n    4 vs.\\ 5 & .5162 & .5013 & .5284 & .5051 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 2 & 2 \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S11: Length Ablation (exp-021)\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Pairwise $\\auc$ across depth pairs for three segment lengths (Exp-021; Qwen2.5-1.5B base, continuation mode). $\\Kempirical{=}2$ is confirmed for 128 and 256 tokens; 512 tokens yields point estimate $\\Kempirical{=}2$ but the 1v2 bootstrap CI lower bound falls marginally below $\\theta$.}\n  \\label{tab:s11_length_ablation}\n  \\begin{tabular}{lccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{128 tokens} & \\textbf{256 tokens} & \\textbf{512 tokens} \\\\\n    \\midrule\n    0 vs.\\ 1 & .9948 & .9956 & .9961 \\\\\n    1 vs.\\ 2 & .6219 & .6282 & .6073$^\\dagger$ \\\\\n    \\cmidrule(lr){1-4}\n    2 vs.\\ 3 & .5531 & .5609 & .5482 \\\\\n    3 vs.\\ 4 & .5218 & .5305 & .5196 \\\\\n    4 vs.\\ 5 & .5104 & .5142 & .5078 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 2$^\\dagger$ \\\\\n    \\bottomrule\n    \\multicolumn{4}{l}{\\footnotesize $^\\dagger$CI $[0.5979,\\,0.6166]$; lower bound ${<}\\theta{=}0.60$.}\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S12: Domain Ablation\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Pairwise $\\auc$ across depth pairs for three text domains (Qwen2.5-1.5B base, continuation mode). Tests generalization of $\\Kempirical{=}2$ beyond C4 web text to structured and technical domains. Same-family scoring (Qwen-1.5B); cross-family controlled values in Table~\\ref{tab:wiki_domain}.}\n  \\label{tab:s12_domain_ablation}\n  \\begin{tabular}{lccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{C4 (web)} & \\textbf{Wikipedia} & \\textbf{arXiv} \\\\\n    \\midrule\n    0 vs.\\ 1 & .9971 & .996 & .9984 \\\\\n    1 vs.\\ 2 & .6112 & .6193 & .8580 \\\\\n    \\cmidrule(lr){1-4}\n    2 vs.\\ 3 & .5609 & .556 & .6427 \\\\\n    3 vs.\\ 4 & .5409 & .528 & .5813 \\\\\n    4 vs.\\ 5 & .5141 & .509 & .5346 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 3 \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S13: Scorer Sensitivity Analysis\n\\begin{table*}[t]\n  \\centering\n  \\small\n  \\caption{Scorer sensitivity: $\\Kempirical$ under self-scoring vs.\\ cross-scoring. Self-scorer uses the generator's own model family for feature extraction; cross-scorer uses alternative models (Pythia-1.4B, OLMo-1B). $\\Kempirical$ agreement across scorer conditions indicates the boundary is governed by the generation process. Cross-scoring reduces $\\Kempirical$ only for the most marginal self-scorer condition (Qwen-continuation).}\n  \\label{tab:s13_scorer_sensitivity}\n  \\begin{tabular}{lccccc}\n    \\toprule\n    & & \\multicolumn{3}{c}{\\textbf{Scorer}} & \\\\\n    \\cmidrule(lr){3-5}\n    \\textbf{Generator} & \\textbf{Mode} & \\textbf{Self} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Agreement} \\\\\n    \\midrule\n    Qwen-1.5B-Instruct & Rewrite      & 2 (.696) & 2 & 2 & \\checkmark \\\\\n    Qwen-1.5B-Instruct & Continuation & 2 (.611) & 1 & 1 & $\\times$ \\\\\n    Qwen-1.5B (base)   & Continuation & 2 (.626) & 2 & 2 & \\checkmark \\\\\n    Pythia-1.4B         & Continuation & 2 (.654) & 2 & 2 & \\checkmark \\\\\n    OLMo-1B             & Continuation & 2 (.615) & 2 & 2 & \\checkmark \\\\\n    Qwen-7B             & Continuation & 2 (.618) & 2 & 2 & \\checkmark \\\\\n    Mistral-7B          & Continuation & 1 (.594) & 1 & 1 & \\checkmark \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n\\clearpage\n",
      "numLines": 509,
      "startLine": 1,
      "totalLines": 509
    }
  },
  "sourceToolAssistantUUID": "08f6a07a-9fc1-4512-a754-5b1955b734df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-18T14:30:13.887Z_

<details open><summary>🔧 Tool call — Read · `toolu_019Uwye3WjcWAYMFhfKLvsFH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31924bab-b0ff-4caa-b2e4-2feaf281535d",
  "isSidechain": false,
  "requestId": "req_011CbACDsCN4cTfNR4tfos6a",
  "type": "assistant",
  "uuid": "d3004721-8eff-45ad-9719-797b6352fea6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWyxzXDRt2P61ogveme4Wr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16637,
      "cache_read_input_tokens": 112164,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 112164,
          "cache_creation_input_tokens": 16637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16637
          },
          "type": "message"
        }
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

_source line 147 · 2026-05-18T14:30:14.173Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NaZkYExKVfmnB23XWBXF2S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3004721-8eff-45ad-9719-797b6352fea6",
  "isSidechain": false,
  "requestId": "req_011CbACDsCN4cTfNR4tfos6a",
  "type": "assistant",
  "uuid": "a0de701b-92a0-4d52-b596-89a4e475352c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWyxzXDRt2P61ogveme4Wr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16637,
      "cache_read_input_tokens": 112164,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 112164,
          "cache_creation_input_tokens": 16637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16637
          },
          "type": "message"
        }
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

_source line 148 · 2026-05-18T14:30:14.183Z_

<details><summary>↩ Tool result · `toolu_01NaZkYExKVfmnB23XWBXF2S`</summary>

```text
1	% === References for gen-depth-contamination ===
2	% Source: literature_map.yaml — verified 2026-05-15
3	
4	% === Must-Cite ===
5	
6	@inproceedings{drayson2025,
7	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
8	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
9	  booktitle={Proceedings of EMNLP},
10	  year={2025},
11	  url={https://arxiv.org/abs/2502.15654}
12	}
13	
14	@inproceedings{schaeffer2025position,
15	  title={Position: Model Collapse Does Not Mean What You Think},
16	  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},
17	  booktitle={Proceedings of ICML},
18	  year={2025},
19	  url={https://arxiv.org/abs/2503.03150}
20	}
21	
22	@inproceedings{kazdan2025collapse,
23	  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},
24	  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},
25	  booktitle={Proceedings of ICML},
26	  year={2025},
27	  url={https://arxiv.org/abs/2410.16713}
28	}
29	
30	@inproceedings{mitchell2023detectgpt,
31	  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
32	  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
33	  booktitle={Proceedings of ICML},
34	  year={2023}
35	}
36	
37	% === Should-Cite ===
38	
39	@article{basani2026diveye,
40	  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},
41	  author={Basani, Advik Raj and Chen, Pin-Yu},
42	  journal={Transactions on Machine Learning Research},
43	  issn={2835-8856},
44	  year={2026},
45	  url={https://arxiv.org/abs/2509.18880}
46	}
47	
48	@inproceedings{zawalski2026codec,
49	  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},
50	  author={Zawalski, Micha{\l} and Boubdir, Meriem and Ba{\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},
51	  booktitle={Proceedings of ICLR},
52	  year={2026},
53	  url={https://arxiv.org/abs/2510.27055}
54	}
55	
56	@inproceedings{zhang2024minkpp,
57	  title={Min-{K}\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
58	  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},
59	  booktitle={Proceedings of EMNLP},
60	  year={2024}
61	}
62	
63	@article{shumailov2024collapse,
64	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
65	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
66	  journal={Nature},
67	  volume={631},
68	  pages={755--759},
69	  year={2024}
70	}
71	
72	@inproceedings{alemohammad2024selfconsuming,
73	  title={Self-Consuming Generative Models Go {MAD}},
74	  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
75	  booktitle={Proceedings of ICLR},
76	  year={2024}
77	}
78	
79	@inproceedings{dohmatob2024model,
80	  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},
81	  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},
82	  booktitle={Proceedings of ICML},
83	  year={2024}
84	}
85	
86	@inproceedings{xie2023dsir,
87	  title={Data Selection for Language Models via Importance Resampling},
88	  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
89	  booktitle={Advances in Neural Information Processing Systems},
90	  year={2023}
91	}
92	
93	@inproceedings{tirumala2023d4,
94	  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},
95	  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},
96	  booktitle={Advances in Neural Information Processing Systems},
97	  year={2023}
98	}
99	
100	@inproceedings{xie2023doremi,
101	  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},
102	  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},
103	  booktitle={Advances in Neural Information Processing Systems},
104	  year={2023}
105	}
106	
107	@inproceedings{hans2024binoculars,
108	  title={Spotting {LLMs} With Binoculars},
109	  author={Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
110	  booktitle={Proceedings of ICML},
111	  year={2024}
112	}
113	
114	% === Probing Classifiers ===
115	
116	@inproceedings{alain2017understanding,
117	  title={Understanding Intermediate Layers Using Linear Classifier Probes},
118	  author={Alain, Guillaume and Bengio, Yoshua},
119	  booktitle={ICLR Workshop},
120	  year={2017}
121	}
122	
123	@article{belinkov2022probing,
124	  title={Probing Classifiers: Promises, Shortcomings, and Advances},
125	  author={Belinkov, Yonatan},
126	  journal={Computational Linguistics},
127	  volume={48},
128	  number={1},
129	  pages={207--219},
130	  year={2022}
131	}
132	
133	% === Model Collapse Avoidability ===
134	
135	@inproceedings{bao2024fast,
136	  title={{Fast-DetectGPT}: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature},
137	  author={Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
138	  booktitle={Proceedings of ICLR},
139	  year={2024},
140	  url={https://arxiv.org/abs/2310.05130}
141	}
142	
143	@inproceedings{frank2001ordinal,
144	  title={A Simple Approach to Ordinal Classification},
145	  author={Frank, Eibe and Hall, Mark},
146	  booktitle={Proceedings of ECML},
147	  pages={145--156},
148	  year={2001}
149	}
150	
151	% === Beyond-Binary Detection ===
152	
153	@inproceedings{cheng2025beyond,
154	  title={Beyond Binary: Towards Fine-Grained {LLM}-Generated Text Detection via Role Recognition and Involvement Measurement},
155	  author={Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
156	  booktitle={Proceedings of the ACM Web Conference (WWW)},
157	  year={2025},
158	  url={https://arxiv.org/abs/2410.14259}
159	}
160	
161	@article{mehta2025beyond,
162	  title={Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models},
163	  author={Mehta, Sushant},
164	  journal={arXiv preprint arXiv:2511.17602},
165	  year={2025},
166	  url={https://arxiv.org/abs/2511.17602}
167	}
168	
169	% === AI-Generated Content Prevalence ===
170	
171	@inproceedings{sun2025aigt,
172	  title={Are We in the {AI}-Generated Text World Already? Quantifying and Monitoring {AIGT} on Social Media},
173	  author={Sun, Zhen and Zhang, Zongmin and Shen, Xinyue and Zhang, Ziyi and Liu, Yule and Backes, Michael and Zhang, Yang and He, Xinlei},
174	  booktitle={Proceedings of ACL},
175	  year={2025},
176	  url={https://arxiv.org/abs/2412.18148}
177	}
178	
179	@article{spennemann2025quantifying,
180	  title={Delving into: the Quantification of {AI}-Generated Content on the Internet (Synthetic Data)},
181	  author={Spennemann, Dirk H. R.},
182	  journal={arXiv preprint arXiv:2504.08755},
183	  year={2025},
184	  url={https://arxiv.org/abs/2504.08755}
185	}
186	
187	% === New entries (added 2026-05-16, Round 4 reviewer) ===
188	
189	@inproceedings{dohmatob2025strong,
190	  title={Strong Model Collapse},
191	  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
192	  booktitle={Proceedings of ICLR},
193	  year={2025},
194	  url={https://arxiv.org/abs/2410.04840}
195	}
196	
197	@inproceedings{wang2024semeval,
198	  title={{SemEval}-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection},
199	  author={Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas},
200	  booktitle={Proceedings of SemEval},
201	  year={2024},
202	  url={https://arxiv.org/abs/2404.14183}
203	}
204	
205	@inproceedings{gerstgrasser2024model,
206	  title={Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data},
207	  author={Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
208	  booktitle={Proceedings of COLM},
209	  year={2024},
210	  url={https://arxiv.org/abs/2404.01413}
211	}
212	
213	@inproceedings{guo2024curious,
214	  title={The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},
215	  author={Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chloe},
216	  booktitle={Findings of NAACL},
217	  year={2024},
218	  url={https://arxiv.org/abs/2311.09807}
219	}
220	
221	@article{briesch2023selfconsuming,
222	  title={Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop},
223	  author={Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},
224	  journal={arXiv preprint arXiv:2311.16822},
225	  year={2023},
226	  url={https://arxiv.org/abs/2311.16822}
227	}
228	
229	@inproceedings{padmakumar2024writing,
230	  title={Does Writing with Language Models Reduce Content Diversity?},
231	  author={Padmakumar, Vishakh and He, He},
232	  booktitle={Proceedings of ICLR},
233	  year={2024},
234	  url={https://arxiv.org/abs/2309.05196}
235	}
236	
237	% === New entries (added 2026-05-15, FR-10) ===
238	
239	@inproceedings{krishna2023paraphrasing,
240	  title={Paraphrasing Evades Detectors of {AI}-Generated Text, but Retrieval is an Effective Defense},
241	  author={Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
242	  booktitle={Advances in Neural Information Processing Systems},
243	  year={2023}
244	}
245	
246	@article{sadasivan2023detect,
247	  title={Can {AI}-Generated Text be Reliably Detected?},
248	  author={Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
249	  journal={arXiv preprint arXiv:2303.11156},
250	  year={2023},
251	  url={https://arxiv.org/abs/2303.11156}
252	}
253	
254	@inproceedings{hao2025rewrite,
255	  title={Learning to Rewrite: Generalized {LLM}-Generated Text Detection},
256	  author={Hao, Wei and Guan, Ran and Lu, Kangjie and Zhang, Shuai},
257	  booktitle={Findings of ACL},
258	  year={2025}
259	}
260	
261	@inproceedings{shi2025collapse,
262	  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},
263	  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},
264	  booktitle={Advances in Neural Information Processing Systems},
265	  year={2025}
266	}
267	
268	@article{gambetta2024surplexity,
269	  title={Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},
270	  author={Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and Knott, Alistair and Pappalardo, Luca},
271	  journal={arXiv preprint arXiv:2410.12341},
272	  year={2024}
273	}
274	
275	@inproceedings{amin2025escaping,
276	  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},
277	  author={Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar and Vassilvitskii, Sergei},
278	  booktitle={Advances in Neural Information Processing Systems},
279	  year={2025}
280	}
281	
282	@inproceedings{kirchenbauer2023watermark,
283	  title     = {A Watermark for Large Language Models},
284	  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
285	  booktitle = {Proceedings of the 40th International Conference on Machine Learning},
286	  pages     = {17061--17084},
287	  year      = {2023},
288	  volume    = {202},
289	  series    = {Proceedings of Machine Learning Research},
290	  publisher = {PMLR}
291	}
292	
293	@inproceedings{penedo2024fineweb,
294	  title     = {The {FineWeb} Datasets: Decanting the Web for the Finest Text Data at Scale},
295	  author    = {Penedo, Guilherme and Kydl{\'{\i}}{\v{c}}ek, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas},
296	  booktitle = {Advances in Neural Information Processing Systems},
297	  volume    = {37},
298	  pages     = {30811--30849},
299	  year      = {2024}
300	}
301	
302	@inproceedings{gehrmann2019gltr,
303	  title     = {{GLTR}: Statistical Detection and Visualization of Generated Text},
304	  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander},
305	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
306	  pages     = {111--116},
307	  year      = {2019},
308	  address   = {Florence, Italy},
309	  publisher = {Association for Computational Linguistics},
310	  doi       = {10.18653/v1/P19-3019}
311	}
312	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0de701b-92a0-4d52-b596-89a4e475352c",
  "isSidechain": false,
  "promptId": "a76e3a98-645a-445f-972e-aeb6711b75d1",
  "type": "user",
  "uuid": "3ec81371-cc85-4e49-9471-23712239d8fe",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
      "content": "% === References for gen-depth-contamination ===\n% Source: literature_map.yaml — verified 2026-05-15\n\n% === Must-Cite ===\n\n@inproceedings{drayson2025,\n  title={Machine-Generated Text Detection Prevents Language Model Collapse},\n  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  booktitle={Proceedings of EMNLP},\n  year={2025},\n  url={https://arxiv.org/abs/2502.15654}\n}\n\n@inproceedings{schaeffer2025position,\n  title={Position: Model Collapse Does Not Mean What You Think},\n  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},\n  booktitle={Proceedings of ICML},\n  year={2025},\n  url={https://arxiv.org/abs/2503.03150}\n}\n\n@inproceedings{kazdan2025collapse,\n  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},\n  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},\n  booktitle={Proceedings of ICML},\n  year={2025},\n  url={https://arxiv.org/abs/2410.16713}\n}\n\n@inproceedings{mitchell2023detectgpt,\n  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},\n  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  booktitle={Proceedings of ICML},\n  year={2023}\n}\n\n% === Should-Cite ===\n\n@article{basani2026diveye,\n  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},\n  author={Basani, Advik Raj and Chen, Pin-Yu},\n  journal={Transactions on Machine Learning Research},\n  issn={2835-8856},\n  year={2026},\n  url={https://arxiv.org/abs/2509.18880}\n}\n\n@inproceedings{zawalski2026codec,\n  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},\n  author={Zawalski, Micha{\\l} and Boubdir, Meriem and Ba{\\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},\n  booktitle={Proceedings of ICLR},\n  year={2026},\n  url={https://arxiv.org/abs/2510.27055}\n}\n\n@inproceedings{zhang2024minkpp,\n  title={Min-{K}\\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},\n  booktitle={Proceedings of EMNLP},\n  year={2024}\n}\n\n@article{shumailov2024collapse,\n  title={{AI} Models Collapse When Trained on Recursively Generated Data},\n  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal={Nature},\n  volume={631},\n  pages={755--759},\n  year={2024}\n}\n\n@inproceedings{alemohammad2024selfconsuming,\n  title={Self-Consuming Generative Models Go {MAD}},\n  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle={Proceedings of ICLR},\n  year={2024}\n}\n\n@inproceedings{dohmatob2024model,\n  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},\n  booktitle={Proceedings of ICML},\n  year={2024}\n}\n\n@inproceedings{xie2023dsir,\n  title={Data Selection for Language Models via Importance Resampling},\n  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@inproceedings{tirumala2023d4,\n  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},\n  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@inproceedings{xie2023doremi,\n  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},\n  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@inproceedings{hans2024binoculars,\n  title={Spotting {LLMs} With Binoculars},\n  author={Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  booktitle={Proceedings of ICML},\n  year={2024}\n}\n\n% === Probing Classifiers ===\n\n@inproceedings{alain2017understanding,\n  title={Understanding Intermediate Layers Using Linear Classifier Probes},\n  author={Alain, Guillaume and Bengio, Yoshua},\n  booktitle={ICLR Workshop},\n  year={2017}\n}\n\n@article{belinkov2022probing,\n  title={Probing Classifiers: Promises, Shortcomings, and Advances},\n  author={Belinkov, Yonatan},\n  journal={Computational Linguistics},\n  volume={48},\n  number={1},\n  pages={207--219},\n  year={2022}\n}\n\n% === Model Collapse Avoidability ===\n\n@inproceedings{bao2024fast,\n  title={{Fast-DetectGPT}: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature},\n  author={Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  booktitle={Proceedings of ICLR},\n  year={2024},\n  url={https://arxiv.org/abs/2310.05130}\n}\n\n@inproceedings{frank2001ordinal,\n  title={A Simple Approach to Ordinal Classification},\n  author={Frank, Eibe and Hall, Mark},\n  booktitle={Proceedings of ECML},\n  pages={145--156},\n  year={2001}\n}\n\n% === Beyond-Binary Detection ===\n\n@inproceedings{cheng2025beyond,\n  title={Beyond Binary: Towards Fine-Grained {LLM}-Generated Text Detection via Role Recognition and Involvement Measurement},\n  author={Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},\n  booktitle={Proceedings of the ACM Web Conference (WWW)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.14259}\n}\n\n@article{mehta2025beyond,\n  title={Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models},\n  author={Mehta, Sushant},\n  journal={arXiv preprint arXiv:2511.17602},\n  year={2025},\n  url={https://arxiv.org/abs/2511.17602}\n}\n\n% === AI-Generated Content Prevalence ===\n\n@inproceedings{sun2025aigt,\n  title={Are We in the {AI}-Generated Text World Already? Quantifying and Monitoring {AIGT} on Social Media},\n  author={Sun, Zhen and Zhang, Zongmin and Shen, Xinyue and Zhang, Ziyi and Liu, Yule and Backes, Michael and Zhang, Yang and He, Xinlei},\n  booktitle={Proceedings of ACL},\n  year={2025},\n  url={https://arxiv.org/abs/2412.18148}\n}\n\n@article{spennemann2025quantifying,\n  title={Delving into: the Quantification of {AI}-Generated Content on the Internet (Synthetic Data)},\n  author={Spennemann, Dirk H. R.},\n  journal={arXiv preprint arXiv:2504.08755},\n  year={2025},\n  url={https://arxiv.org/abs/2504.08755}\n}\n\n% === New entries (added 2026-05-16, Round 4 reviewer) ===\n\n@inproceedings{dohmatob2025strong,\n  title={Strong Model Collapse},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle={Proceedings of ICLR},\n  year={2025},\n  url={https://arxiv.org/abs/2410.04840}\n}\n\n@inproceedings{wang2024semeval,\n  title={{SemEval}-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection},\n  author={Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas},\n  booktitle={Proceedings of SemEval},\n  year={2024},\n  url={https://arxiv.org/abs/2404.14183}\n}\n\n@inproceedings{gerstgrasser2024model,\n  title={Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data},\n  author={Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  booktitle={Proceedings of COLM},\n  year={2024},\n  url={https://arxiv.org/abs/2404.01413}\n}\n\n@inproceedings{guo2024curious,\n  title={The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},\n  author={Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chloe},\n  booktitle={Findings of NAACL},\n  year={2024},\n  url={https://arxiv.org/abs/2311.09807}\n}\n\n@article{briesch2023selfconsuming,\n  title={Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop},\n  author={Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},\n  journal={arXiv preprint arXiv:2311.16822},\n  year={2023},\n  url={https://arxiv.org/abs/2311.16822}\n}\n\n@inproceedings{padmakumar2024writing,\n  title={Does Writing with Language Models Reduce Content Diversity?},\n  author={Padmakumar, Vishakh and He, He},\n  booktitle={Proceedings of ICLR},\n  year={2024},\n  url={https://arxiv.org/abs/2309.05196}\n}\n\n% === New entries (added 2026-05-15, FR-10) ===\n\n@inproceedings{krishna2023paraphrasing,\n  title={Paraphrasing Evades Detectors of {AI}-Generated Text, but Retrieval is an Effective Defense},\n  author={Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@article{sadasivan2023detect,\n  title={Can {AI}-Generated Text be Reliably Detected?},\n  author={Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  journal={arXiv preprint arXiv:2303.11156},\n  year={2023},\n  url={https://arxiv.org/abs/2303.11156}\n}\n\n@inproceedings{hao2025rewrite,\n  title={Learning to Rewrite: Generalized {LLM}-Generated Text Detection},\n  author={Hao, Wei and Guan, Ran and Lu, Kangjie and Zhang, Shuai},\n  booktitle={Findings of ACL},\n  year={2025}\n}\n\n@inproceedings{shi2025collapse,\n  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},\n  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2025}\n}\n\n@article{gambetta2024surplexity,\n  title={Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},\n  author={Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and Knott, Alistair and Pappalardo, Luca},\n  journal={arXiv preprint arXiv:2410.12341},\n  year={2024}\n}\n\n@inproceedings{amin2025escaping,\n  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},\n  author={Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar and Vassilvitskii, Sergei},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2025}\n}\n\n@inproceedings{kirchenbauer2023watermark,\n  title     = {A Watermark for Large Language Models},\n  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning},\n  pages     = {17061--17084},\n  year      = {2023},\n  volume    = {202},\n  series    = {Proceedings of Machine Learning Research},\n  publisher = {PMLR}\n}\n\n@inproceedings{penedo2024fineweb,\n  title     = {The {FineWeb} Datasets: Decanting the Web for the Finest Text Data at Scale},\n  author    = {Penedo, Guilherme and Kydl{\\'{\\i}}{\\v{c}}ek, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {37},\n  pages     = {30811--30849},\n  year      = {2024}\n}\n\n@inproceedings{gehrmann2019gltr,\n  title     = {{GLTR}: Statistical Detection and Visualization of Generated Text},\n  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  pages     = {111--116},\n  year      = {2019},\n  address   = {Florence, Italy},\n  publisher = {Association for Computational Linguistics},\n  doi       = {10.18653/v1/P19-3019}\n}\n",
      "numLines": 312,
      "startLine": 1,
      "totalLines": 312
    }
  },
  "sourceToolAssistantUUID": "a0de701b-92a0-4d52-b596-89a4e475352c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "5836cf50-96e4-4556-97ef-940e6ea69671",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
