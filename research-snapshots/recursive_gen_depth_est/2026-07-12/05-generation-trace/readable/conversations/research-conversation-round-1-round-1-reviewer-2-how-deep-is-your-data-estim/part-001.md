# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2 **你的审查侧重：新颖性 + 完整性 + 写作质量** ### 论文信息 - **标题**: How Deep Is Your Data? Estim — Part 1 of 6

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-round-1-round-1-reviewer-2-how-deep-is-your-data-estim.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/67/6712347043bad525dc54.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-18T14:10:25.636Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T14:10:25.636Z",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "content": "[Round 1 审稿请求]:\n## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量**\n\n### 论文信息\n- **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n- **路径**: `projects/recursive_gen_depth_est/docs/paper/main.tex`（主文件在 `docs/paper/` 目录，含 abstract.tex, introduction.tex, related_work.tex, method.tex, atlas.tex, generalization.tex, discussion.tex, conclusion.tex, section_appendix.tex）\n- **目标 Venue**: EMNLP 2026（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求\n- Long paper: 8 页正文 + 无限 references\n- 模板: ACL LaTeX, `\\usepackage[review]{acl}`\n- 匿名: double-blind\n- 附录: 必须 double-column format\n- Overall Assessment 评分: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **新颖性评估**\n   - \"Recursive generation depth estimation as ordinal classification\" 是否是真正的新问题，还是 binary detection 的简单延伸？\n   - EDD metric 的贡献是否足够？与现有 detection metrics 的区别是否清晰？\n   - 方法本质上是 Random Forest + perplexity features，方法论新颖性如何？\n   - Depth Degradation Atlas 是否提供了超越 model collapse 文献已知结论的新见解？\n\n2. **Related Work 定位**\n   - 是否充分覆盖 model collapse、AI text detection、ordinal classification 三大相关领域？\n   - 与 Dohmatob et al. 2024（tail erosion）的关系是否被诚实讨论？本文是否只是对已有理论的实验验证？\n   - 与 Drayson et al. 2025（detection prevents collapse）的区分是否清晰？\n   - 是否遗漏了重要的近期相关工作？\n\n3. **写作质量**\n   - Abstract 是否在 30 秒内传达清楚问题/方法/贡献/结果？\n   - Introduction 叙事线是否连贯（问题→缺口→洞察→方法→贡献）？\n   - 是否存在 AI 写作痕迹（em-dash, -ing phrases, 过度分段, AI 高频词汇）？\n   - 专有名词首次出现是否有定义？\n   - 段落过渡是否自然？\n   - 数字和 claim 是否准确一致（正文 vs 表格 vs abstract）？\n\n4. **论文完整性**\n   - Discussion 是否充分讨论了 implications 和 limitations？\n   - Limitations 是否诚实（不回避关键局限）？\n   - Ethics Statement 是否适当？\n   - 是否有 Contribution bullet 没有对应的支撑 section/table？\n\n5. **格式检查**\n   - 是否符合 ACL review format？\n   - 匿名化是否完整（无 self-citation leakage）？\n   - 表格/图表 caption 是否自包含？\n   - 引用格式是否一致？\n   - 页数是否在限制内？\n\n6. **引用审计**\n   - References 是否覆盖：直接相关方法、baseline 论文、benchmark 论文、理论基础？\n   - 是否存在 orphan bib entries（有 bib 条目但正文未引用）？\n   - 引用密度是否匹配 EMNLP 水平？\n   - 是否有明显遗漏的重要论文？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary（2-3 句）\n\n## Strengths（逐条）\n\n## Weaknesses（逐条，按严重程度排序：Must-Fix / Should-Fix / Minor）\n\n## Questions（需要作者回答的问题）\n\n## Missing References（如有）\n\n## Overall Assessment\n- 评分（使用 ARR 5 分制）\n- 置信度（1-5）\n- 简要理由\n```"
}
````

---


### Runtime record

_source line 2 · 2026-05-18T14:10:25.640Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T14:10:25.640Z",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


## Round 1

## Round 1

86 recorded events


### User

_source line 3 · 2026-05-18T14:10:25.676Z_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + 完整性 + 写作质量**

### 论文信息
- **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
- **路径**: `projects/recursive_gen_depth_est/docs/paper/main.tex`（主文件在 `docs/paper/` 目录，含 abstract.tex, introduction.tex, related_work.tex, method.tex, atlas.tex, generalization.tex, discussion.tex, conclusion.tex, section_appendix.tex）
- **目标 Venue**: EMNLP 2026（ARR May 2026 cycle）
- **截止日期**: 2026-05-25

### Venue 格式要求
- Long paper: 8 页正文 + 无限 references
- 模板: ACL LaTeX, `\usepackage[review]{acl}`
- 匿名: double-blind
- 附录: 必须 double-column format
- Overall Assessment 评分: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

### 你的审查重点

请从以下维度严格评审：

1. **新颖性评估**
   - "Recursive generation depth estimation as ordinal classification" 是否是真正的新问题，还是 binary detection 的简单延伸？
   - EDD metric 的贡献是否足够？与现有 detection metrics 的区别是否清晰？
   - 方法本质上是 Random Forest + perplexity features，方法论新颖性如何？
   - Depth Degradation Atlas 是否提供了超越 model collapse 文献已知结论的新见解？

2. **Related Work 定位**
   - 是否充分覆盖 model collapse、AI text detection、ordinal classification 三大相关领域？
   - 与 Dohmatob et al. 2024（tail erosion）的关系是否被诚实讨论？本文是否只是对已有理论的实验验证？
   - 与 Drayson et al. 2025（detection prevents collapse）的区分是否清晰？
   - 是否遗漏了重要的近期相关工作？

3. **写作质量**
   - Abstract 是否在 30 秒内传达清楚问题/方法/贡献/结果？
   - Introduction 叙事线是否连贯（问题→缺口→洞察→方法→贡献）？
   - 是否存在 AI 写作痕迹（em-dash, -ing phrases, 过度分段, AI 高频词汇）？
   - 专有名词首次出现是否有定义？
   - 段落过渡是否自然？
   - 数字和 claim 是否准确一致（正文 vs 表格 vs abstract）？

4. **论文完整性**
   - Discussion 是否充分讨论了 implications 和 limitations？
   - Limitations 是否诚实（不回避关键局限）？
   - Ethics Statement 是否适当？
   - 是否有 Contribution bullet 没有对应的支撑 section/table？

5. **格式检查**
   - 是否符合 ACL review format？
   - 匿名化是否完整（无 self-citation leakage）？
   - 表格/图表 caption 是否自包含？
   - 引用格式是否一致？
   - 页数是否在限制内？

6. **引用审计**
   - References 是否覆盖：直接相关方法、baseline 论文、benchmark 论文、理论基础？
   - 是否存在 orphan bib entries（有 bib 条目但正文未引用）？
   - 引用密度是否匹配 EMNLP 水平？
   - 是否有明显遗漏的重要论文？

### 输出格式

请按以下结构输出审稿意见：

```
## Summary（2-3 句）

## Strengths（逐条）

## Weaknesses（逐条，按严重程度排序：Must-Fix / Should-Fix / Minor）

## Questions（需要作者回答的问题）

## Missing References（如有）

## Overall Assessment
- 评分（使用 ARR 5 分制）
- 置信度（1-5）
- 简要理由
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "c5e1a06e-7a82-4636-b7b9-60edfa6bb48f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-18T14:10:25.675Z_

```json
{
  "parentUuid": "c5e1a06e-7a82-4636-b7b9-60edfa6bb48f",
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
  "uuid": "4b8a98d8-bb7d-4e56-8ef6-a4999a18c682",
  "timestamp": "2026-05-18T14:10:25.675Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 5 · 2026-05-18T14:10:25.675Z_

```json
{
  "parentUuid": "4b8a98d8-bb7d-4e56-8ef6-a4999a18c682",
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
  "uuid": "816c130f-a0c9-4910-b1bf-261e9a45e88d",
  "timestamp": "2026-05-18T14:10:25.675Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 6 · 2026-05-18T14:10:25.675Z_

```json
{
  "parentUuid": "816c130f-a0c9-4910-b1bf-261e9a45e88d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f94c7646-7322-4448-9b43-4b07cc4af8ed",
  "timestamp": "2026-05-18T14:10:25.675Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
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
  "aiTitle": "Review recursive generation depth estimation paper",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Assistant

_source line 8 · 2026-05-18T14:10:31.003Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a Round 1 review of a paper as Reviewer 2, focusing on novelty, completeness, and writing quality. Let me start by following the session start skill and then reading the paper.

First, I need to:
1. Search for EMNLP 2026 / ACL ARR reviewer guidelines
2. Read the paper (all sections)

Let me start by reading the skill file for session start, and then read the paper files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f94c7646-7322-4448-9b43-4b07cc4af8ed",
  "isSidechain": false,
  "requestId": "req_011CbAAivabDX1WLp3sQJ3jv",
  "type": "assistant",
  "uuid": "48949d28-2f39-45c7-8d5a-ccb13e94f23e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012V73Pu2GzUP48myVpg42Aj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16126,
      "cache_read_input_tokens": 11841,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16126
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-18T14:10:31.985Z_

开始 Round 1 审稿。先加载 session start skill，搜索 ARR reviewer guidelines，并读取论文各部分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48949d28-2f39-45c7-8d5a-ccb13e94f23e",
  "isSidechain": false,
  "requestId": "req_011CbAAivabDX1WLp3sQJ3jv",
  "type": "assistant",
  "uuid": "6e77f690-9fae-4626-ab40-d77940e4dd58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012V73Pu2GzUP48myVpg42Aj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16126,
      "cache_read_input_tokens": 11841,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16126
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-18T14:10:33.538Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WTRt4D5hpVXsk3cwUjRVsn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e77f690-9fae-4626-ab40-d77940e4dd58",
  "isSidechain": false,
  "requestId": "req_011CbAAivabDX1WLp3sQJ3jv",
  "type": "assistant",
  "uuid": "5ff082ca-b2b3-4904-8f6d-f4e6fec11227",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012V73Pu2GzUP48myVpg42Aj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16126,
      "cache_read_input_tokens": 11841,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16126
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-18T14:10:34.491Z_

<details><summary>↩ Tool result · `toolu_019k1reSukiFx9udqmz4EULb`</summary>

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
  "tool_name": "WebFetch"
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
  "parentUuid": "0b3bfe4f-64c7-44aa-b447-dca9724c9f77",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "0e0c1228-31a4-45be-a17e-47e46383b245",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "0b3bfe4f-64c7-44aa-b447-dca9724c9f77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 12 · 2026-05-18T14:10:33.550Z_

<details><summary>↩ Tool result · reported error · `toolu_01WTRt4D5hpVXsk3cwUjRVsn`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ff082ca-b2b3-4904-8f6d-f4e6fec11227",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "71f86065-2d64-4019-b110-a6633181b449",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e.",
  "sourceToolAssistantUUID": "5ff082ca-b2b3-4904-8f6d-f4e6fec11227",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 13 · 2026-05-18T14:10:34.486Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019k1reSukiFx9udqmz4EULb`</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71f86065-2d64-4019-b110-a6633181b449",
  "isSidechain": false,
  "requestId": "req_011CbAAivabDX1WLp3sQJ3jv",
  "type": "assistant",
  "uuid": "0b3bfe4f-64c7-44aa-b447-dca9724c9f77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012V73Pu2GzUP48myVpg42Aj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16126,
      "cache_read_input_tokens": 11841,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16126
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-18T14:10:38.337Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the paper files and search for ARR reviewer guidelines simultaneously.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e0c1228-31a4-45be-a17e-47e46383b245",
  "isSidechain": false,
  "requestId": "req_011CbAAjaKDKkntKAiv1qrWW",
  "type": "assistant",
  "uuid": "7d36d0a3-61a8-4683-88c8-5ad23574a77a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191ruCmBaVnZCoVvQce5NE1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2459,
      "cache_read_input_tokens": 27967,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2459,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 296,
          "cache_read_input_tokens": 27967,
          "cache_creation_input_tokens": 2459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2459
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-18T14:10:38.930Z_

先搜索 ARR reviewer guidelines，同时开始读取论文各部分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d36d0a3-61a8-4683-88c8-5ad23574a77a",
  "isSidechain": false,
  "requestId": "req_011CbAAjaKDKkntKAiv1qrWW",
  "type": "assistant",
  "uuid": "6452d03a-6680-4ce9-a619-7cf8240c3677",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191ruCmBaVnZCoVvQce5NE1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2459,
      "cache_read_input_tokens": 27967,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2459,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 296,
          "cache_read_input_tokens": 27967,
          "cache_creation_input_tokens": 2459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2459
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-18T14:10:39.945Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016p8aPbtQAvNiPMKpG32BpD`</summary>

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
  "parentUuid": "6452d03a-6680-4ce9-a619-7cf8240c3677",
  "isSidechain": false,
  "requestId": "req_011CbAAjaKDKkntKAiv1qrWW",
  "type": "assistant",
  "uuid": "f5497211-8df9-4926-876c-bc793015fe52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191ruCmBaVnZCoVvQce5NE1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2459,
      "cache_read_input_tokens": 27967,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2459,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 296,
          "cache_read_input_tokens": 27967,
          "cache_creation_input_tokens": 2459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2459
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-18T14:10:40.853Z_

<details><summary>↩ Tool result · `toolu_013JJ6JbkXpYFBdGGtbj1Duo`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e27bee07-05b1-4265-8d23-b8768ba1793d",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "65562d64-b8cb-4a63-b387-d5f137b749d9",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
    ],
    "durationMs": 18,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "e27bee07-05b1-4265-8d23-b8768ba1793d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-18T14:10:40.452Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TXpXeL8xzM88tcfuk99TJE`</summary>

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
  "parentUuid": "f5497211-8df9-4926-876c-bc793015fe52",
  "isSidechain": false,
  "requestId": "req_011CbAAjaKDKkntKAiv1qrWW",
  "type": "assistant",
  "uuid": "630c43cc-8159-4283-acae-5317d8102727",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191ruCmBaVnZCoVvQce5NE1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2459,
      "cache_read_input_tokens": 27967,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2459,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 296,
          "cache_read_input_tokens": 27967,
          "cache_creation_input_tokens": 2459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2459
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-18T14:10:40.472Z_

<details><summary>↩ Tool result · `toolu_01TXpXeL8xzM88tcfuk99TJE`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "630c43cc-8159-4283-acae-5317d8102727",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "f7e78c94-261f-4dde-bc94-360356dc6642",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
    ],
    "durationMs": 12,
    "numFiles": 10,
    "truncated": false
  },
  "sourceToolAssistantUUID": "630c43cc-8159-4283-acae-5317d8102727",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-18T14:10:40.828Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013JJ6JbkXpYFBdGGtbj1Duo`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7e78c94-261f-4dde-bc94-360356dc6642",
  "isSidechain": false,
  "requestId": "req_011CbAAjaKDKkntKAiv1qrWW",
  "type": "assistant",
  "uuid": "e27bee07-05b1-4265-8d23-b8768ba1793d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191ruCmBaVnZCoVvQce5NE1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2459,
      "cache_read_input_tokens": 27967,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2459,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 296,
          "cache_read_input_tokens": 27967,
          "cache_creation_input_tokens": 2459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2459
          },
          "type": "message"
        }
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性 + 写作质量**  ### 论文信息 - **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints - **路径**: `proje…",
  "leafUuid": "65562d64-b8cb-4a63-b387-d5f137b749d9",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Review recursive generation depth estimation paper",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Tool result

_source line 23 · 2026-05-18T14:10:49.857Z_

<details><summary>↩ Tool result · `toolu_016p8aPbtQAvNiPMKpG32BpD`</summary>

```text
Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here's comprehensive information about ACL ARR 2025-2026 reviewer guidelines, review form, and scoring criteria:

## Reviewer Scoring

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Recommendation Scoring Scale

The ARR metareview score options are: 5 = Consider for Award (papers up to top 2.5%), 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, and 1 = Do not resubmit (papers that need full redo or are not relevant to the *ACL community). Outstanding papers should be either fascinating, controversial, surprising, impressive, or potentially field-changing.

## Review Criteria and Requirements

The review form asks whether authors have adequately discussed the limitations and potential positive and negative societal impacts of their work, and authors should be rewarded rather than punished for being up front about limitations.

Reviewers should review the ACL code of ethics and check the ARR checklist, and if there are ethical issues, they should describe them and their extent.

Reviewers assess whether there is enough information for a reader to reproduce the main results, use results in future work, or build upon the work.

## Guidelines and Professional Standards

ARR reviewers are instructed to write reviews as if the paper were being considered for the ACL conference, and low scores may indicate the submission is not a good fit for ACL, even if suitable for other venues.

Starting in May 2025, ARR adopts a new policy on 'highly irresponsible' reviewers, with egregious cases including extremely terse reviews, unprofessional tone, and LLM-generated reviews.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5497211-8df9-4926-876c-bc793015fe52",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "a84087ec-35f7-4805-9d38-d0c06688e9da",
  "toolUseResult": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SFmDfDkezJRvDd5L2qjtds",
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
            "title": "Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "https://aclrollingreview.org/"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
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
      "Based on the search results, here's comprehensive information about ACL ARR 2025-2026 reviewer guidelines, review form, and scoring criteria:\n\n## Reviewer Scoring\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.\n\n## Overall Recommendation Scoring Scale\n\nThe ARR metareview score options are: 5 = Consider for Award (papers up to top 2.5%), 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, and 1 = Do not resubmit (papers that need full redo or are not relevant to the *ACL community). Outstanding papers should be either fascinating, controversial, surprising, impressive, or potentially field-changing.\n\n## Review Criteria and Requirements\n\nThe review form asks whether authors have adequately discussed the limitations and potential positive and negative societal impacts of their work, and authors should be rewarded rather than punished for being up front about limitations.\n\nReviewers should review the ACL code of ethics and check the ARR checklist, and if there are ethical issues, they should describe them and their extent.\n\nReviewers assess whether there is enough information for a reader to reproduce the main results, use results in future work, or build upon the work.\n\n## Guidelines and Professional Standards\n\nARR reviewers are instructed to write reviews as if the paper were being considered for the ACL conference, and low scores may indicate the submission is not a good fit for ACL, even if suitable for other venues.\n\nStarting in May 2025, ARR adopts a new policy on 'highly irresponsible' reviewers, with egregious cases including extremely terse reviews, unprofessional tone, and LLM-generated reviews."
    ],
    "durationSeconds": 9.907227613
  },
  "sourceToolAssistantUUID": "f5497211-8df9-4926-876c-bc793015fe52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-18T14:10:54.219Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0128db3xpv1ZbWHpE2kc1tP5`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment scales and any other criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a84087ec-35f7-4805-9d38-d0c06688e9da",
  "isSidechain": false,
  "requestId": "req_011CbAAkhxsX5qzsKNwLuMoF",
  "type": "assistant",
  "uuid": "f4dbf8fc-9b1b-49fd-b9a6-21740e661628",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQQ6FgW7c9qpW268osCT5R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 476,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 30426,
      "output_tokens": 472,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 476,
          "output_tokens": 472,
          "cache_read_input_tokens": 30426,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1227
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-18T14:10:54.601Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MtDvWT3uFf2E88ww6pNNsh`</summary>

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
  "parentUuid": "f4dbf8fc-9b1b-49fd-b9a6-21740e661628",
  "isSidechain": false,
  "requestId": "req_011CbAAkhxsX5qzsKNwLuMoF",
  "type": "assistant",
  "uuid": "33d3c349-453b-4160-afca-90862922b644",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQQ6FgW7c9qpW268osCT5R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 476,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 30426,
      "output_tokens": 472,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 476,
          "output_tokens": 472,
          "cache_read_input_tokens": 30426,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1227
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-18T14:10:54.613Z_

<details><summary>↩ Tool result · `toolu_01MtDvWT3uFf2E88ww6pNNsh`</summary>

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
17	\usepackage{amsthm}
18	
19	\theoremstyle{definition}
20	\newtheorem{definition}{Definition}
21	
22	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{abstract}
30	
31	\input{introduction}
32	
33	\input{related_work}
34	
35	\input{method}
36	
37	\input{atlas}
38	
39	\input{generalization}
40	
41	\input{discussion}
42	
43	\input{conclusion}
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{section_appendix}
49	
50	\end{document}
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33d3c349-453b-4160-afca-90862922b644",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "5a0c2559-bc20-4116-a74b-c3ea93259e05",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex",
      "content": "% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n% Target: EMNLP 2026 (ARR May cycle)\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{amsthm}\n\n\\theoremstyle{definition}\n\\newtheorem{definition}{Definition}\n\n\\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\\\via Statistical Fingerprints}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{atlas}\n\n\\input{generalization}\n\n\\input{discussion}\n\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\appendix\n\\input{section_appendix}\n\n\\end{document}\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  },
  "sourceToolAssistantUUID": "33d3c349-453b-4160-afca-90862922b644",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-18T14:10:56.680Z_

<details><summary>↩ Tool result · `toolu_0122rXk1PZ75P5f4Z6ZRLrvw`</summary>

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
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark covers depths d0--d3 across all $3 \times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K samples total).
30	For depth extension experiments (\S\ref{sec:atlas}), we extend one pipeline (Pythia-1.4B, nucleus) to d0--d5.
31	
32	\paragraph{Generation pipeline.}
33	Starting from a Wikipedia subset as seed text ($\mathcal{D}_0$), each generation cycle proceeds in three steps: (1)~LoRA finetuning \cite{hu2022lora} on $\mathcal{D}_{k-1}$, freezing base model weights and training low-rank update matrices ($<$1\% additional parameters; $r{=}16$, $\alpha{=}32$, lr $2{\times}10^{-4}$, batch size 8, 3 epochs, dropout $0.05$, architecture-specific targets); (2)~sampling 5{,}000 passages from the LoRA-finetuned model (max 512 tokens, BOS-seeded, no prompt conditioning) under the specified decoding strategy; (3)~the generated corpus becomes $\mathcal{D}_k$ for the next cycle.
34	Each depth is produced by a model explicitly trained on the prior depth's data, not by sampling from the unmodified base model.
35	Our BOS-seeded generation may amplify depth signal relative to prompted settings; a prompted-generation validation (\S\ref{sec:gen:crossstrategy}) confirms signal persistence under topic-seeded conditions ($-$13.8\,pp vs.\ BOS-seeded).
36	There is no per-passage lineage across depths; cross-validation splits therefore do not introduce information leakage.
37	
38	\paragraph{Reference model.}
39	All statistical features (\S\ref{sec:method:features}) are computed using Pythia-1.4B as fixed reference model, the smallest generator whose training corpus partially overlaps with the others.
40	For Pythia this constitutes self-model measurement, yet its accuracy (78.7\%) does not exceed GPT-2~XL (85.9\%); no systematic self-model advantage is observed.
41	Ablations with OLMo-1B and GPT-2 XL as alternative references yield 67--79\% accuracy (Appendix~\ref{app:ref_ablation}); reference model robustness is confirmed. Further discussion in Limitations.
42	
43	\subsection{Statistical Feature Design}
44	\label{sec:method:features}
45	
46	We extract a feature vector $\mathbf{f}(x)$ comprising 19 candidate features from the reference-model perplexity distribution over each passage $x$; ablation (\S\ref{sec:atlas:features}) shows the top 5 achieve 97.6\% of full-set performance, and variance inflation analysis reveals VIF${>}$10 for 14--16 features; effective independent dimensionality is ${\approx}$4--5.
47	The features fall into four categories (Table~\ref{tab:features}).
48	
49	\begin{table}[t]
50	\centering
51	\small
52	\caption{The 19 statistical features comprising $\mathbf{f}(x)$, grouped by category. All perplexity and surprisal features are computed from the reference model (Pythia-1.4B).}
53	\label{tab:features}
54	\begin{tabular}{@{}llr@{}}
55	\toprule
56	Category & Features & $n$ \\
57	\midrule
58	Perplexity & mean, var, skewness, kurtosis, & 9 \\
59	statistics & p10, p25, p50, p75, p90 & \\
60	\addlinespace
61	Surprisal & mean, var, entropy & 3 \\
62	statistics & & \\
63	\addlinespace
64	Lexical & type--token ratio, hapax ratio, & 4 \\
65	diversity & bigram entropy, trigram entropy & \\
66	\addlinespace
67	Repetition & repeated 2/3/4-gram fractions & 3 \\
68	\bottomrule
69	\end{tabular}
70	\end{table}
71	
72	\emph{Perplexity statistics} (9 features) capture the per-token perplexity distribution via moments (mean, variance, skewness, kurtosis) and quantiles (p10--p90); tail quantiles prove especially informative as recursive finetuning erodes the high-perplexity tail (\S\ref{sec:atlas}).
73	\emph{Surprisal statistics} (3 features): mean, variance, and entropy of $-\log p(\text{token})$; surprisal variance captures second-order structure not redundant with perplexity moments.
74	\emph{Lexical diversity} (4 features): type--token ratio, hapax ratio, bigram/trigram entropy.
75	\emph{Repetition} (3 features): repeated $n$-gram fractions for $n \in \{2, 3, 4\}$.
76	
77	\subsection{Effective Discriminable Depth}
78	\label{sec:method:edd}
79	
80	Aggregate multi-class accuracy obscures whether discriminability degrades at specific depth boundaries.
81	We propose the \emph{Effective Discriminable Depth} (EDD) as an operational measure of how far into a recursive chain adjacent depths remain distinguishable.
82	
83	\paragraph{Pairwise discriminability.}
84	Let $\mathcal{D} = \{0, 1, \dots, K\}$ denote the depth set and $T \in (0.5, 1.0]$ a discrimination threshold.
85	For each adjacent pair $(d, d{+}1)$, we define the pairwise discriminability $\mathrm{AUC}(d, d{+}1)$ as the area under the ROC curve of a dedicated binary Random Forest classifier (500 trees, $\lfloor\sqrt{19}\rfloor$ candidate features per split) trained on class-balanced data from $\mathbf{f}(x)$ (\S\ref{sec:method:features}) to distinguish depth-$d$ from depth-$(d{+}1)$ samples, evaluated via 5-fold stratified cross-validation.
86	Each pair uses an independent classifier, avoiding the decision boundary dilution that arises in multi-class settings (\S\ref{sec:atlas:edd}).
87	
88	\begin{definition}[Effective Discriminable Depth]
89	\label{def:edd}
90	The \emph{Effective Discriminable Depth} at threshold $T$ is:
91	\begin{equation}
92	\mathrm{EDD}_T = \max \bigl\{ d^*{+}1 \,:\, \forall\, d' \leq d^*,\; \mathrm{AUC}(d', d'{+}1) \geq T \bigr\}
93	\label{eq:edd}
94	\end{equation}
95	where $d^* \in \{0, \dots, K{-}1\}$. If\, $\mathrm{AUC}(0,1) < T$, then $\mathrm{EDD}_T = 0$.
96	\end{definition}
97	
98	$\mathrm{EDD}_T$ is the deepest depth $d$ such that every adjacent pair from $(0,1)$ through $(d{-}1, d)$ remains discriminable at level $T$.
99	The universal quantifier ensures EDD reports the longest \emph{contiguous} discriminable prefix rather than an isolated high-AUC pair at greater depth.\footnote{Our AUC profiles are empirically monotonically decreasing for the 1--1.5B base models (\S\ref{sec:atlas}), so in practice $\mathrm{EDD}_T = \max\{d'{+}1 : \mathrm{AUC}(d', d'{+}1) \geq T\}$. Qwen2.5-7B exhibits a U-shaped AUC pattern rather than monotonic decay; a base-model control shows non-monotonic decay persists without instruction tuning (\S\ref{sec:gen:crossscale}). For non-monotonic profiles, the contiguous formulation is more conservative (see Limitations).}
100	We set $T{=}0.75$ as default; sensitivity at $T \in \{0.65, 0.70, 0.75, 0.80\}$ is reported in \S\ref{sec:atlas}.
101	
102	\paragraph{Classifiers.}
103	Our primary classifier is a Random Forest (200 trees, unconstrained depth, 5-fold stratified cross-validation).
104	We compare against CORAL ordinal regression \cite{coral2020}, DivEye \cite{diveye2026}, a 2-layer cross-entropy MLP, logistic regression, and a single-feature baseline using mean perplexity alone; results appear in \S\ref{sec:generalization}.
105	Full computational details (hardware, GPU hours, software versions) are in Appendix~\ref{app:compute}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45457b86-e595-4e3b-b5dc-3c8eecca02a3",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "01aaaf32-8c44-401f-8ec6-424b17dfdf5b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Definition}\n\\label{sec:method:problem}\n\nLet $f_\\theta$ denote a language model and $\\mathcal{D}_0$ a corpus of human-written seed text.\nWe define a \\emph{recursive generation chain} of depth $K$ as the sequence $\\mathcal{D}_0, \\mathcal{D}_1, \\dots, \\mathcal{D}_K$, where each $\\mathcal{D}_k$ ($k \\geq 1$) is produced by finetuning $f_\\theta$ on $\\mathcal{D}_{k-1}$ and sampling from the resulting model.\nDepth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \\geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.\n\nGiven a text passage $x$, the task is to estimate its recursive generation depth $d \\in \\{0, 1, \\dots, K\\}$.\nThis is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.\n\n\\subsection{Multi-Generational Benchmark Construction}\n\\label{sec:method:benchmark}\n\nWe construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.\n\n\\paragraph{Model families.}\nWe select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).\nRestricting to a narrow parameter range isolates the effect of architecture and training data from scale.\n\n\\paragraph{Decoding strategies.}\nEach model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \\cite{holtzman2020_nucleus}, temperature sampling ($\\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).\nThese span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.\nOur findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.\n\n\\paragraph{Depth and scale.}\nThe primary benchmark covers depths d0--d3 across all $3 \\times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K samples total).\nFor depth extension experiments (\\S\\ref{sec:atlas}), we extend one pipeline (Pythia-1.4B, nucleus) to d0--d5.\n\n\\paragraph{Generation pipeline.}\nStarting from a Wikipedia subset as seed text ($\\mathcal{D}_0$), each generation cycle proceeds in three steps: (1)~LoRA finetuning \\cite{hu2022lora} on $\\mathcal{D}_{k-1}$, freezing base model weights and training low-rank update matrices ($<$1\\% additional parameters; $r{=}16$, $\\alpha{=}32$, lr $2{\\times}10^{-4}$, batch size 8, 3 epochs, dropout $0.05$, architecture-specific targets); (2)~sampling 5{,}000 passages from the LoRA-finetuned model (max 512 tokens, BOS-seeded, no prompt conditioning) under the specified decoding strategy; (3)~the generated corpus becomes $\\mathcal{D}_k$ for the next cycle.\nEach depth is produced by a model explicitly trained on the prior depth's data, not by sampling from the unmodified base model.\nOur BOS-seeded generation may amplify depth signal relative to prompted settings; a prompted-generation validation (\\S\\ref{sec:gen:crossstrategy}) confirms signal persistence under topic-seeded conditions ($-$13.8\\,pp vs.\\ BOS-seeded).\nThere is no per-passage lineage across depths; cross-validation splits therefore do not introduce information leakage.\n\n\\paragraph{Reference model.}\nAll statistical features (\\S\\ref{sec:method:features}) are computed using Pythia-1.4B as fixed reference model, the smallest generator whose training corpus partially overlaps with the others.\nFor Pythia this constitutes self-model measurement, yet its accuracy (78.7\\%) does not exceed GPT-2~XL (85.9\\%); no systematic self-model advantage is observed.\nAblations with OLMo-1B and GPT-2 XL as alternative references yield 67--79\\% accuracy (Appendix~\\ref{app:ref_ablation}); reference model robustness is confirmed. Further discussion in Limitations.\n\n\\subsection{Statistical Feature Design}\n\\label{sec:method:features}\n\nWe extract a feature vector $\\mathbf{f}(x)$ comprising 19 candidate features from the reference-model perplexity distribution over each passage $x$; ablation (\\S\\ref{sec:atlas:features}) shows the top 5 achieve 97.6\\% of full-set performance, and variance inflation analysis reveals VIF${>}$10 for 14--16 features; effective independent dimensionality is ${\\approx}$4--5.\nThe features fall into four categories (Table~\\ref{tab:features}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{The 19 statistical features comprising $\\mathbf{f}(x)$, grouped by category. All perplexity and surprisal features are computed from the reference model (Pythia-1.4B).}\n\\label{tab:features}\n\\begin{tabular}{@{}llr@{}}\n\\toprule\nCategory & Features & $n$ \\\\\n\\midrule\nPerplexity & mean, var, skewness, kurtosis, & 9 \\\\\nstatistics & p10, p25, p50, p75, p90 & \\\\\n\\addlinespace\nSurprisal & mean, var, entropy & 3 \\\\\nstatistics & & \\\\\n\\addlinespace\nLexical & type--token ratio, hapax ratio, & 4 \\\\\ndiversity & bigram entropy, trigram entropy & \\\\\n\\addlinespace\nRepetition & repeated 2/3/4-gram fractions & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\emph{Perplexity statistics} (9 features) capture the per-token perplexity distribution via moments (mean, variance, skewness, kurtosis) and quantiles (p10--p90); tail quantiles prove especially informative as recursive finetuning erodes the high-perplexity tail (\\S\\ref{sec:atlas}).\n\\emph{Surprisal statistics} (3 features): mean, variance, and entropy of $-\\log p(\\text{token})$; surprisal variance captures second-order structure not redundant with perplexity moments.\n\\emph{Lexical diversity} (4 features): type--token ratio, hapax ratio, bigram/trigram entropy.\n\\emph{Repetition} (3 features): repeated $n$-gram fractions for $n \\in \\{2, 3, 4\\}$.\n\n\\subsection{Effective Discriminable Depth}\n\\label{sec:method:edd}\n\nAggregate multi-class accuracy obscures whether discriminability degrades at specific depth boundaries.\nWe propose the \\emph{Effective Discriminable Depth} (EDD) as an operational measure of how far into a recursive chain adjacent depths remain distinguishable.\n\n\\paragraph{Pairwise discriminability.}\nLet $\\mathcal{D} = \\{0, 1, \\dots, K\\}$ denote the depth set and $T \\in (0.5, 1.0]$ a discrimination threshold.\nFor each adjacent pair $(d, d{+}1)$, we define the pairwise discriminability $\\mathrm{AUC}(d, d{+}1)$ as the area under the ROC curve of a dedicated binary Random Forest classifier (500 trees, $\\lfloor\\sqrt{19}\\rfloor$ candidate features per split) trained on class-balanced data from $\\mathbf{f}(x)$ (\\S\\ref{sec:method:features}) to distinguish depth-$d$ from depth-$(d{+}1)$ samples, evaluated via 5-fold stratified cross-validation.\nEach pair uses an independent classifier, avoiding the decision boundary dilution that arises in multi-class settings (\\S\\ref{sec:atlas:edd}).\n\n\\begin{definition}[Effective Discriminable Depth]\n\\label{def:edd}\nThe \\emph{Effective Discriminable Depth} at threshold $T$ is:\n\\begin{equation}\n\\mathrm{EDD}_T = \\max \\bigl\\{ d^*{+}1 \\,:\\, \\forall\\, d' \\leq d^*,\\; \\mathrm{AUC}(d', d'{+}1) \\geq T \\bigr\\}\n\\label{eq:edd}\n\\end{equation}\nwhere $d^* \\in \\{0, \\dots, K{-}1\\}$. If\\, $\\mathrm{AUC}(0,1) < T$, then $\\mathrm{EDD}_T = 0$.\n\\end{definition}\n\n$\\mathrm{EDD}_T$ is the deepest depth $d$ such that every adjacent pair from $(0,1)$ through $(d{-}1, d)$ remains discriminable at level $T$.\nThe universal quantifier ensures EDD reports the longest \\emph{contiguous} discriminable prefix rather than an isolated high-AUC pair at greater depth.\\footnote{Our AUC profiles are empirically monotonically decreasing for the 1--1.5B base models (\\S\\ref{sec:atlas}), so in practice $\\mathrm{EDD}_T = \\max\\{d'{+}1 : \\mathrm{AUC}(d', d'{+}1) \\geq T\\}$. Qwen2.5-7B exhibits a U-shaped AUC pattern rather than monotonic decay; a base-model control shows non-monotonic decay persists without instruction tuning (\\S\\ref{sec:gen:crossscale}). For non-monotonic profiles, the contiguous formulation is more conservative (see Limitations).}\nWe set $T{=}0.75$ as default; sensitivity at $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ is reported in \\S\\ref{sec:atlas}.\n\n\\paragraph{Classifiers.}\nOur primary classifier is a Random Forest (200 trees, unconstrained depth, 5-fold stratified cross-validation).\nWe compare against CORAL ordinal regression \\cite{coral2020}, DivEye \\cite{diveye2026}, a 2-layer cross-entropy MLP, logistic regression, and a single-feature baseline using mean perplexity alone; results appear in \\S\\ref{sec:generalization}.\nFull computational details (hardware, GPU hours, software versions) are in Appendix~\\ref{app:compute}.",
      "numLines": 105,
      "startLine": 1,
      "totalLines": 105
    }
  },
  "sourceToolAssistantUUID": "45457b86-e595-4e3b-b5dc-3c8eecca02a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-18T14:10:54.992Z_

<details open><summary>🔧 Tool call — Read · `toolu_019TzgixHfEdeJ3sZYiqvYEP`</summary>

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
  "parentUuid": "5a0c2559-bc20-4116-a74b-c3ea93259e05",
  "isSidechain": false,
  "requestId": "req_011CbAAkhxsX5qzsKNwLuMoF",
  "type": "assistant",
  "uuid": "397584fc-f798-43fd-bc38-362a81444ece",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQQ6FgW7c9qpW268osCT5R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 476,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 30426,
      "output_tokens": 472,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 476,
          "output_tokens": 472,
          "cache_read_input_tokens": 30426,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1227
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-18T14:10:54.998Z_

<details><summary>↩ Tool result · `toolu_019TzgixHfEdeJ3sZYiqvYEP`</summary>

```text
1	\begin{abstract}
2	As large language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.
4	A Random Forest over 19 perplexity-based features achieves $\approx$69--86\% four-class accuracy (chance = 25\%), with perplexity tail statistics emerging as consistent depth markers; a parsimonious subset of 5 features retains 97.6\% of full performance.
5	We define the \emph{Effective Discriminable Depth} (EDD) metric, finding $\mathrm{EDD}_{0.75}{=}4$ for the best-characterized family, and show that cross-model transfer reaches 66.4\% (2.7$\times$ chance).
6	Systematic generalization across eight axes (e.g., cross-scale 7B at 70.2\%, prompted generation at 69.5\%, cross-model chains at 84.75\%, and cross-domain arXiv at 74.1\%) confirms that depth signal is robust across model families but strategy-dependent, residing in distributional statistics inaccessible from surface text (zero-shot LLMs: 30--36\%, 43\,pp below RF).
7	\end{abstract}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "397584fc-f798-43fd-bc38-362a81444ece",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "251c7211-3224-48c9-867c-8401102a092c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nAs large language models increasingly train on web text containing their own outputs, a recursive model$\\to$data$\\to$model loop arises, yet no method estimates how many such iterations a text has undergone.\nWe formalize \\emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.\nA Random Forest over 19 perplexity-based features achieves $\\approx$69--86\\% four-class accuracy (chance = 25\\%), with perplexity tail statistics emerging as consistent depth markers; a parsimonious subset of 5 features retains 97.6\\% of full performance.\nWe define the \\emph{Effective Discriminable Depth} (EDD) metric, finding $\\mathrm{EDD}_{0.75}{=}4$ for the best-characterized family, and show that cross-model transfer reaches 66.4\\% (2.7$\\times$ chance).\nSystematic generalization across eight axes (e.g., cross-scale 7B at 70.2\\%, prompted generation at 69.5\\%, cross-model chains at 84.75\\%, and cross-domain arXiv at 74.1\\%) confirms that depth signal is robust across model families but strategy-dependent, residing in distributional statistics inaccessible from surface text (zero-shot LLMs: 30--36\\%, 43\\,pp below RF).\n\\end{abstract}\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "397584fc-f798-43fd-bc38-362a81444ece",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-18T14:10:55.469Z_

<details open><summary>🔧 Tool call — Read · `toolu_0155LMhXF4gPKGK9kPt1tAnj`</summary>

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
  "parentUuid": "251c7211-3224-48c9-867c-8401102a092c",
  "isSidechain": false,
  "requestId": "req_011CbAAkhxsX5qzsKNwLuMoF",
  "type": "assistant",
  "uuid": "84c44093-efd1-48dd-a91a-798c09500f22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQQ6FgW7c9qpW268osCT5R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 476,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 30426,
      "output_tokens": 472,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 476,
          "output_tokens": 472,
          "cache_read_input_tokens": 30426,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1227
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-18T14:10:55.480Z_

<details><summary>↩ Tool result · `toolu_0155LMhXF4gPKGK9kPt1tAnj`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	
8	Existing tools address adjacent but distinct problems.
9	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
10	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
12	No existing method estimates the ordinal recursive generation depth of a text passage from its content alone.
13	
14	We find that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are \textbf{consistent in direction but scale-dependent in magnitude} across the three model families and three decoding strategies studied.
15	Specifically, perplexity tail statistics (the 90th-percentile perplexity, \texttt{p90\_ppl}, and surprisal variance, \texttt{var\_surprisal}) emerge as dominant depth indicators, ranking in the top two features by importance in 9/9 and 8/9 model--strategy configurations, respectively.
16	Instruction-tuned variants exhibit monotonically decreasing AUC (regularization), whereas base models can show non-monotonic trajectories; instruction tuning thus acts as a regularizer on the depth signal rather than a source of degradation.
17	
18	We formalize recursive generation depth estimation as ordinal classification and introduce a lightweight pipeline: compute 19 reference-model perplexity features (effective dimensionality ${\approx}$4--5 due to multicollinearity; \S\ref{sec:atlas:features}) and classify with a Random Forest into $K{+}1$ depth classes.
19	To characterize how recursive generation reshapes these features, we construct the \emph{Depth Degradation Atlas}: a $3 \times 3$ grid of model families $\times$ decoding strategies spanning 4 depths (180K samples).
20	The atlas reveals strategy-dependent degradation trajectories and we introduce the \emph{Effective Discriminable Depth} (EDD) metric to quantify how far into the recursion chain adjacent depths remain distinguishable.
21	
22	Our contributions are:
23	\begin{itemize}
24	    \item \textbf{Task formalization and benchmark.} We define recursive generation depth estimation as ordinal classification, introduce the EDD metric, and construct a 180K-sample benchmark spanning 3 model families $\times$ 3 decoding strategies $\times$ 4 depths.
25	
26	    \item \textbf{Depth Degradation Atlas.} A systematic $3 \times 3$ characterization reveals that perplexity tail statistics dominate depth discrimination (top-2 in 9/9 and 8/9 cells), decoding strategy reshapes degradation trajectories qualitatively, and $\mathrm{EDD}_{0.75}{=}4$ for the best-characterized family (Pythia, $p{=}0.001$); all three families cross the $T{=}0.75$ threshold within the d3--d4 region, with graded statistical confidence ($p{=}0.091$ for OLMo, $p{=}0.505$ for GPT-2~XL).
27	
28	    \item \textbf{Transfer generalization.} Cross-model LOO (66.4\%), cross-strategy (59.1\%), cross-seed (76.8\%), prompted generation (69.5\%), and recursive chains (84.75\%).
29	
30	    \item \textbf{Scale and domain robustness.} Cross-scale 7--8B (70.2\%, 60.1\%), cross-domain arXiv (74.1\%), temperature ($\tau \in [0.5, 0.9]$).
31	
32	    \item \textbf{Diagnostic ablations.} LoRA rank spread 4.65\,pp, three reference architectures (67--79\%), generation length scaling, and surface-text control (zero-shot LLMs at 30--36\%, 43\,pp below RF) confirming the signal resides in distributional statistics; 19 features and a Random Forest suffice for GPU-free inference.
33	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84c44093-efd1-48dd-a91a-798c09500f22",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "b05902c8-bf63-4faf-bdbd-44a31a6359b8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\nThe text on which large language models are trained increasingly contains their own outputs.\nAs synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \\cite{shumailov2024_nature,alemohammad2024_mad}.\nThis model$\\to$data$\\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \\cite{dohmatob2024_tale_of_tails}.\n\nExisting tools address adjacent but distinct problems.\nBinary detectors such as Binoculars \\cite{binoculars2024}, Fast-DetectGPT \\cite{fast_detectgpt2024}, and DivEye \\cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \\geq 1$ into a single category.\nWatermarking \\cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.\nThe model collapse literature \\cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \\citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.\nNo existing method estimates the ordinal recursive generation depth of a text passage from its content alone.\n\nWe find that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are \\textbf{consistent in direction but scale-dependent in magnitude} across the three model families and three decoding strategies studied.\nSpecifically, perplexity tail statistics (the 90th-percentile perplexity, \\texttt{p90\\_ppl}, and surprisal variance, \\texttt{var\\_surprisal}) emerge as dominant depth indicators, ranking in the top two features by importance in 9/9 and 8/9 model--strategy configurations, respectively.\nInstruction-tuned variants exhibit monotonically decreasing AUC (regularization), whereas base models can show non-monotonic trajectories; instruction tuning thus acts as a regularizer on the depth signal rather than a source of degradation.\n\nWe formalize recursive generation depth estimation as ordinal classification and introduce a lightweight pipeline: compute 19 reference-model perplexity features (effective dimensionality ${\\approx}$4--5 due to multicollinearity; \\S\\ref{sec:atlas:features}) and classify with a Random Forest into $K{+}1$ depth classes.\nTo characterize how recursive generation reshapes these features, we construct the \\emph{Depth Degradation Atlas}: a $3 \\times 3$ grid of model families $\\times$ decoding strategies spanning 4 depths (180K samples).\nThe atlas reveals strategy-dependent degradation trajectories and we introduce the \\emph{Effective Discriminable Depth} (EDD) metric to quantify how far into the recursion chain adjacent depths remain distinguishable.\n\nOur contributions are:\n\\begin{itemize}\n    \\item \\textbf{Task formalization and benchmark.} We define recursive generation depth estimation as ordinal classification, introduce the EDD metric, and construct a 180K-sample benchmark spanning 3 model families $\\times$ 3 decoding strategies $\\times$ 4 depths.\n\n    \\item \\textbf{Depth Degradation Atlas.} A systematic $3 \\times 3$ characterization reveals that perplexity tail statistics dominate depth discrimination (top-2 in 9/9 and 8/9 cells), decoding strategy reshapes degradation trajectories qualitatively, and $\\mathrm{EDD}_{0.75}{=}4$ for the best-characterized family (Pythia, $p{=}0.001$); all three families cross the $T{=}0.75$ threshold within the d3--d4 region, with graded statistical confidence ($p{=}0.091$ for OLMo, $p{=}0.505$ for GPT-2~XL).\n\n    \\item \\textbf{Transfer generalization.} Cross-model LOO (66.4\\%), cross-strategy (59.1\\%), cross-seed (76.8\\%), prompted generation (69.5\\%), and recursive chains (84.75\\%).\n\n    \\item \\textbf{Scale and domain robustness.} Cross-scale 7--8B (70.2\\%, 60.1\\%), cross-domain arXiv (74.1\\%), temperature ($\\tau \\in [0.5, 0.9]$).\n\n    \\item \\textbf{Diagnostic ablations.} LoRA rank spread 4.65\\,pp, three reference architectures (67--79\\%), generation length scaling, and surface-text control (zero-shot LLMs at 30--36\\%, 43\\,pp below RF) confirming the signal resides in distributional statistics; 19 features and a Random Forest suffice for GPU-free inference.\n\\end{itemize}",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  },
  "sourceToolAssistantUUID": "84c44093-efd1-48dd-a91a-798c09500f22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-18T14:10:56.087Z_

<details open><summary>🔧 Tool call — Read · `toolu_015XhJ4V2yh3rWH6eHAo1DvU`</summary>

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
  "parentUuid": "b05902c8-bf63-4faf-bdbd-44a31a6359b8",
  "isSidechain": false,
  "requestId": "req_011CbAAkhxsX5qzsKNwLuMoF",
  "type": "assistant",
  "uuid": "f9c44d5a-cea0-40f1-b804-caf5f4f32fb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQQ6FgW7c9qpW268osCT5R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 476,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 30426,
      "output_tokens": 472,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 476,
          "output_tokens": 472,
          "cache_read_input_tokens": 30426,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1227
          },
          "type": "message"
        }
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

_source line 33 · 2026-05-18T14:10:56.099Z_

<details><summary>↩ Tool result · `toolu_015XhJ4V2yh3rWH6eHAo1DvU`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails; \citet{dohmatob2024_tale_of_tails} formalize this via scaling laws \cite{seddik2024synthetic}, \citet{dohmatob2025_strong_collapse} establish strong collapse guarantees, and the MAD framework \cite{alemohammad2024_mad} extends the analysis to self-consuming models.
6	Subsequent work addresses mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026}.
7	\citet{schaeffer2025} argue that ``model collapse'' conflates multiple distinct phenomena, and call for operationally precise metrics.
8	Dohmatob et al.\ predict that recursive training erodes distributional tails as a theoretical scaling law \citep{dohmatob2024_tale_of_tails}; we operationalize this prediction into a deployable ordinal classifier, revealing strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.
9	All assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
10	
11	\paragraph{AI Text Detection.}
12	The detection literature \cite{wu2025_detection_survey} spans statistical methods (DetectGPT \cite{mitchell2023_detectgpt}, Fast-DetectGPT \cite{fast_detectgpt2024}, Binoculars \cite{binoculars2024}, DivEye \cite{diveye2026}, GLTR \cite{gehrmann2019_gltr}, Ghostbuster \cite{verma2024_ghostbuster}, DNA-GPT \cite{yang2024_dnagpt}), geometric approaches based on intrinsic dimensionality \cite{tulchinskii2023_intrinsic_dim}, and watermarking \cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \cite{sadasivan2023_paraphrase}, distribution shift \cite{pudasaini2026_detection_fails}, and generator barriers \cite{pu2026_generator_barrier}.
13	M4-SemEval \cite{wang2024_m4_semeval}, RAID \cite{dugan2024_raid}, and MAGE \cite{li2024_mage} benchmark detection across domains, models, and adversarial conditions.
14	All these methods perform binary classification, discarding ordinal depth information; our approach outputs ordinal depth labels, complementing rather than replacing binary detection.
15	
16	\paragraph{Adjacent Tasks.}
17	EditLens \cite{editlens2026} estimates editing extent but does not model recursive chains; \citet{uchendu2020_attribution} classify \emph{which} model generated text; LOKI \cite{loki2025} benchmarks synthetic data detection across modalities.
18	\citet{mohamed2025_broken_telephone} study iterative generation as a ``broken telephone'' effect, characterizing \emph{how} text degrades without classifying which iteration a passage comes from.
19	Our task performs the inverse, ordinal depth estimation from text alone, discriminating between adjacent depths rather than merely detecting aggregate degradation.
20	
21	\paragraph{Ordinal Classification.}
22	Ordinal classification has a long history \cite{mccullagh1980_ordinal}: \citet{frank2001} reduce ordinal problems to nested binary tasks, and \citet{rennie2005} introduce loss functions tailored to discrete ordered labels.
23	CORAL \cite{coral2020} enforces rank consistency via ordered binary tasks; CLOC \cite{cloc2025} extends contrastive learning with multi-margin ordinal losses.
24	We adopt both as baselines (\S\ref{sec:generalization}) to confirm the signal is accessible to principled ordinal methods.
25	
26	\paragraph{Decoding Strategy Effects.}
27	Decoding strategies shape text statistics in ways that interact with depth signals \cite{holtzman2020_nucleus,finlayson2024_closing,garces_arias2025_decoding_decoded,wiher2022_decoding,basu2021_mirostat}.
28	Our Depth Degradation Atlas (\S\ref{sec:atlas}) reveals that these strategies induce qualitatively different degradation trajectories under recursive generation: temperature sampling accelerates convergence to a low-entropy attractor while top-$k$ attenuates the depth signal, effects beyond single-pass text quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9c44d5a-cea0-40f1-b804-caf5f4f32fb6",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "172238fa-f1b6-4a03-be1a-05855d1b74ee",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Model Collapse Theory.}\n\\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails; \\citet{dohmatob2024_tale_of_tails} formalize this via scaling laws \\cite{seddik2024synthetic}, \\citet{dohmatob2025_strong_collapse} establish strong collapse guarantees, and the MAD framework \\cite{alemohammad2024_mad} extends the analysis to self-consuming models.\nSubsequent work addresses mitigation \\cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, non-monotonic dynamics \\cite{bakshi2026_collapse_improvement}, convergence \\cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \\cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026}.\n\\citet{schaeffer2025} argue that ``model collapse'' conflates multiple distinct phenomena, and call for operationally precise metrics.\nDohmatob et al.\\ predict that recursive training erodes distributional tails as a theoretical scaling law \\citep{dohmatob2024_tale_of_tails}; we operationalize this prediction into a deployable ordinal classifier, revealing strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.\nAll assume depth is known a priori; we address the inverse problem of estimating depth from text alone.\n\n\\paragraph{AI Text Detection.}\nThe detection literature \\cite{wu2025_detection_survey} spans statistical methods (DetectGPT \\cite{mitchell2023_detectgpt}, Fast-DetectGPT \\cite{fast_detectgpt2024}, Binoculars \\cite{binoculars2024}, DivEye \\cite{diveye2026}, GLTR \\cite{gehrmann2019_gltr}, Ghostbuster \\cite{verma2024_ghostbuster}, DNA-GPT \\cite{yang2024_dnagpt}), geometric approaches based on intrinsic dimensionality \\cite{tulchinskii2023_intrinsic_dim}, and watermarking \\cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \\cite{sadasivan2023_paraphrase}, distribution shift \\cite{pudasaini2026_detection_fails}, and generator barriers \\cite{pu2026_generator_barrier}.\nM4-SemEval \\cite{wang2024_m4_semeval}, RAID \\cite{dugan2024_raid}, and MAGE \\cite{li2024_mage} benchmark detection across domains, models, and adversarial conditions.\nAll these methods perform binary classification, discarding ordinal depth information; our approach outputs ordinal depth labels, complementing rather than replacing binary detection.\n\n\\paragraph{Adjacent Tasks.}\nEditLens \\cite{editlens2026} estimates editing extent but does not model recursive chains; \\citet{uchendu2020_attribution} classify \\emph{which} model generated text; LOKI \\cite{loki2025} benchmarks synthetic data detection across modalities.\n\\citet{mohamed2025_broken_telephone} study iterative generation as a ``broken telephone'' effect, characterizing \\emph{how} text degrades without classifying which iteration a passage comes from.\nOur task performs the inverse, ordinal depth estimation from text alone, discriminating between adjacent depths rather than merely detecting aggregate degradation.\n\n\\paragraph{Ordinal Classification.}\nOrdinal classification has a long history \\cite{mccullagh1980_ordinal}: \\citet{frank2001} reduce ordinal problems to nested binary tasks, and \\citet{rennie2005} introduce loss functions tailored to discrete ordered labels.\nCORAL \\cite{coral2020} enforces rank consistency via ordered binary tasks; CLOC \\cite{cloc2025} extends contrastive learning with multi-margin ordinal losses.\nWe adopt both as baselines (\\S\\ref{sec:generalization}) to confirm the signal is accessible to principled ordinal methods.\n\n\\paragraph{Decoding Strategy Effects.}\nDecoding strategies shape text statistics in ways that interact with depth signals \\cite{holtzman2020_nucleus,finlayson2024_closing,garces_arias2025_decoding_decoded,wiher2022_decoding,basu2021_mirostat}.\nOur Depth Degradation Atlas (\\S\\ref{sec:atlas}) reveals that these strategies induce qualitatively different degradation trajectories under recursive generation: temperature sampling accelerates convergence to a low-entropy attractor while top-$k$ attenuates the depth signal, effects beyond single-pass text quality.",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  },
  "sourceToolAssistantUUID": "f9c44d5a-cea0-40f1-b804-caf5f4f32fb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-18T14:10:56.675Z_

<details open><summary>🔧 Tool call — Read · `toolu_0122rXk1PZ75P5f4Z6ZRLrvw`</summary>

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
  "parentUuid": "172238fa-f1b6-4a03-be1a-05855d1b74ee",
  "isSidechain": false,
  "requestId": "req_011CbAAkhxsX5qzsKNwLuMoF",
  "type": "assistant",
  "uuid": "45457b86-e595-4e3b-b5dc-3c8eecca02a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQQ6FgW7c9qpW268osCT5R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 476,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 30426,
      "output_tokens": 472,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 476,
          "output_tokens": 472,
          "cache_read_input_tokens": 30426,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1227
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性 + 写作质量**  ### 论文信息 - **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints - **路径**: `proje…",
  "leafUuid": "01aaaf32-8c44-401f-8ec6-424b17dfdf5b",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Review recursive generation depth estimation paper",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Tool result

_source line 37 · 2026-05-18T14:11:01.165Z_

<details><summary>↩ Tool result · `toolu_0128db3xpv1ZbWHpE2kc1tP5`</summary>

```text
# ACL Rolling Review Form - Scoring Dimensions

## Core Evaluation Criteria

**Soundness** (1-5 scale)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: "Strong: This study provides sufficient support for all claims"
- 3: "Acceptable: sufficient support for main claims"
- 2: "Poor: main claims not sufficiently supported"
- 1: "Major Issues: not sufficiently thorough to warrant publication"

**Excitement** (1-5 scale)
- 5: "Highly Exciting: recommend to others/attend presentation"
- 4: "Exciting: mention to others/make effort to attend"
- 3: "Interesting: might mention points or attend if time permits"
- 2: "Potentially Interesting: does not resonate with reviewer"
- 1: "Not Exciting: unlikely to resonate with community"

**Overall Assessment** (1-5 scale)
- 5: Consider for Award (top 2.5%)
- 4: Conference acceptance
- 3: Findings track acceptance
- 2: Resubmit next cycle (needs substantial revision)
- 1: Do not resubmit (fundamental issues)

## Additional Dimensions

- **Reviewer Confidence** (1-5): familiarity with area and review thoroughness
- **Reproducibility** (1-5): feasibility of reproducing results
- **Datasets** (1-5): value of released datasets
- **Software** (1-5): value of released code
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4dbf8fc-9b1b-49fd-b9a6-21740e661628",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "a3f1bee2-90a5-4e68-8375-01d2f5c56a95",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Scoring Dimensions\n\n## Core Evaluation Criteria\n\n**Soundness** (1-5 scale)\n- 5: \"Excellent: This study is one of the most thorough I have seen\"\n- 4: \"Strong: This study provides sufficient support for all claims\"\n- 3: \"Acceptable: sufficient support for main claims\"\n- 2: \"Poor: main claims not sufficiently supported\"\n- 1: \"Major Issues: not sufficiently thorough to warrant publication\"\n\n**Excitement** (1-5 scale)\n- 5: \"Highly Exciting: recommend to others/attend presentation\"\n- 4: \"Exciting: mention to others/make effort to attend\"\n- 3: \"Interesting: might mention points or attend if time permits\"\n- 2: \"Potentially Interesting: does not resonate with reviewer\"\n- 1: \"Not Exciting: unlikely to resonate with community\"\n\n**Overall Assessment** (1-5 scale)\n- 5: Consider for Award (top 2.5%)\n- 4: Conference acceptance\n- 3: Findings track acceptance\n- 2: Resubmit next cycle (needs substantial revision)\n- 1: Do not resubmit (fundamental issues)\n\n## Additional Dimensions\n\n- **Reviewer Confidence** (1-5): familiarity with area and review thoroughness\n- **Reproducibility** (1-5): feasibility of reproducing results\n- **Datasets** (1-5): value of released datasets\n- **Software** (1-5): value of released code",
    "durationMs": 6941,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "f4dbf8fc-9b1b-49fd-b9a6-21740e661628",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 38 · 2026-05-18T14:11:01.168Z_

```json
{
  "parentUuid": "a3f1bee2-90a5-4e68-8375-01d2f5c56a95",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "50d52d46-31c1-4417-a1c3-d747f98fe099",
  "timestamp": "2026-05-18T14:11:01.168Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Tool call

_source line 39 · 2026-05-18T14:11:05.699Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KvtnzUYFJJHqtkEv9YcWKD`</summary>

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
  "parentUuid": "50d52d46-31c1-4417-a1c3-d747f98fe099",
  "isSidechain": false,
  "requestId": "req_011CbAAmYGEvUKzNL8bqZWne",
  "type": "assistant",
  "uuid": "a8386d3e-7166-4900-918f-eeeaaa3eb1d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPHHq3gYENpMxrx56HQeua",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6519,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 31653,
      "output_tokens": 454,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6519,
          "output_tokens": 454,
          "cache_read_input_tokens": 31653,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1449
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-18T14:11:05.704Z_

<details><summary>↩ Tool result · `toolu_01KvtnzUYFJJHqtkEv9YcWKD`</summary>

```text
1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 68.8\% (Pythia, top-$k$) to 85.9\% (GPT-2~XL, temperature), all exceeding the 25\% chance baseline by a wide margin.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (75.9--85.9\%), followed by OLMo (74.5--82.1\%) and Pythia (68.8--78.7\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 9.2~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy and model family contribute roughly equally to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) with bootstrap 95\% CI (${\pm}$half-width; 10{,}000 resamples) across the $3 \times 3$ atlas; d1--d3 three-class accuracy in parentheses (chance = 25\% / 33\%). Depth-0 recall exceeds 98\% in all cells.}
22	\label{tab:main_matrix}
23	\begin{tabular}{@{}lccc@{}}
24	\toprule
25	& Nucleus & Temp.\ $\tau{=}0.9$ & Top-$k$ \\
26	\midrule
27	Pythia-1.4B  & 78.7{\scriptsize$\pm$0.5}\,(71.2) & 76.7{\scriptsize$\pm$0.5}\,(70.6) & 68.8{\scriptsize$\pm$0.6}\,(58.8) \\
28	OLMo-1B     & 78.9{\scriptsize$\pm$0.5}\,(75.0) & 82.1{\scriptsize$\pm$0.5}\,(76.3) & 74.5{\scriptsize$\pm$0.5}\,(66.1) \\
29	GPT-2~XL    & \textbf{84.1}{\scriptsize$\pm$0.5}\,(79.0) & \textbf{85.9}{\scriptsize$\pm$0.5}\,(82.6) & \textbf{75.9}{\scriptsize$\pm$0.6}\,(69.5) \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
34	\paragraph{Per-class recall distribution.}
35	Depth-0 recall exceeds 98\% in all 9 cells; human-written text is thus trivially separable from any generation depth.
36	Among generated depths, d2 consistently yields the lowest recall (46--73\% across cells), followed by d3 (58--82\%) and d1 (72--91\%).
37	For example, Pythia-1.4B nucleus achieves per-class recall of d0$\,{=}\,$99\%, d1$\,{=}\,$82\%, d2$\,{=}\,$59\%, d3$\,{=}\,$72\%.
38	The strongest d2 recall is obtained by GPT-2~XL nucleus (73\%).
39	The d2 trough reflects its position at the center of the depth gradient: d2 features overlap with both the d1 distribution above and d3 below and is therefore the most confusable class, consistent with the d2-vs-d3 pair as the EDD bottleneck (\S\ref{sec:atlas:edd}).
40	Full per-class recall for all cells appears in Appendix~\ref{app:per_class}.
41	
42	%% ----------------------------------------------------------------
43	\subsection{Feature Consistency Across the Grid}
44	\label{sec:atlas:features}
45	
46	Despite the 17.1~pp accuracy spread across cells, a small feature family dominates in every setting.
47	Perplexity tail statistics as a feature group dominate depth discrimination: the 90th-percentile perplexity (\texttt{p90\_ppl}) ranks top-2 by Gini importance in all 9 cells; surprisal variance (\texttt{var\_surprisal}) in 8/9 under SHAP (7/9 under Gini; Appendix~\ref{app:permutation}).\footnote{Individual feature rankings should be interpreted cautiously given high multicollinearity (VIF${>}$10 for 14--16/19 features); the group-level dominance of perplexity tail statistics is robust across importance measures.}
48	Table~\ref{tab:feature_importance} shows the full per-cell ranking.
49	
50	Cross-model feature-rank Spearman correlation averages $\bar{\rho} = 0.868$ (range $[0.619, 0.954]$): models agree on which features carry depth information even when they differ in absolute accuracy.
51	Among strategies, top-$k$ yields the highest cross-model rank correlation ($\rho = 0.811$): the deterministic vocabulary truncation imposes a more uniform feature landscape across architectures, at the cost of weaker overall signal (\S\ref{sec:atlas:strategy}).
52	
53	Percentile-based features outperform their moment-based counterparts.
54	Token-level perplexity distributions are heavy-tailed: individual outlier passages can dominate the arithmetic mean of their depth class, whereas \texttt{p90\_ppl} is robust to such extremes while still capturing the tail erosion that signals generation depth.
55	
56	Feature ablation confirms this concentration: the top-2 features (\texttt{p90\_ppl} + \texttt{var\_surprisal}) alone reach 91.1\% of full accuracy (71.5\%), and the top-5 features achieve 97.6\% (76.5\% vs.\ 78.4\%), with perplexity statistics alone reaching 76.6\% (vs.\ surprisal 73.2\%, other categories ${\leq}$47\%).
57	Variance inflation analysis reveals VIF${>}$10 for 14--16 of 19 features; effective independent dimensionality is ${\approx}$4--5.
58	Forward selection independently confirms the dominant pair: \texttt{p90\_ppl} is selected first in 6/9 cells, \texttt{var\_surprisal} in 3/9.
59	
60	The feature hierarchy also shifts with depth.
61	At shallow boundaries (d1 vs.\ d2), \texttt{var\_surprisal} dominates importance; at deeper boundaries (d3 vs.\ d4, d4 vs.\ d5), tail perplexity statistics (\texttt{p90\_ppl}, \texttt{kurtosis\_ppl}) take over.
62	This transition aligns with model-collapse dynamics~\cite{shumailov2024_nature}: early recursion narrows the surprisal distribution (captured by its variance), while later steps erode the perplexity tail (captured by upper quantiles and kurtosis).
63	
64	\begin{table}[t]
65	\centering
66	\small
67	\caption{Top-5 features by Gini importance. \textbf{Bold}: top-2. \texttt{p90\_ppl} top-2 in 9/9; \texttt{var\_surprisal} 8/9 under SHAP (7/9 under Gini).}
68	\label{tab:feature_importance}
69	\resizebox{\columnwidth}{!}{%
70	\begin{tabular}{@{}l l@{}}
71	\toprule
72	Cell & Top-5 features (Gini importance, ranked) \\
73	\midrule
74	Pythia, nuc.       & \textbf{var\_surp\,(.17)}, \textbf{p90\_ppl\,(.15)}, m\_ppl\,(.11), var\_ppl\,(.08), p75\,(.07) \\
75	Pythia, $\tau$     & \textbf{var\_surp\,(.17)}, \textbf{p90\_ppl\,(.14)}, m\_ppl\,(.11), p75\,(.07), m\_surp\,(.07) \\
76	Pythia, top-$k$    & \textbf{var\_surp\,(.16)}, \textbf{p90\_ppl\,(.12)}, m\_ppl\,(.11), var\_ppl\,(.07), m\_surp\,(.06) \\
77	GPT-2\,XL, nuc.    & \textbf{var\_surp\,(.21)}, \textbf{p90\_ppl\,(.21)}, p75\,(.10), m\_surp\,(.07), m\_ppl\,(.06) \\
78	GPT-2\,XL, $\tau$  & \textbf{p90\_ppl\,(.25)}, \textbf{p75\,(.15)}, m\_surp\,(.13), var\_surp\,(.12), p50\,(.05) \\
79	GPT-2\,XL, top-$k$ & \textbf{p90\_ppl\,(.24)}, \textbf{p75\,(.12)}, var\_surp\,(.10), m\_surp\,(.09), ttr\,(.04) \\
80	OLMo, nuc.         & \textbf{p90\_ppl\,(.18)}, \textbf{var\_surp\,(.15)}, p75\,(.11), m\_surp\,(.07), ttr\,(.06) \\
81	OLMo, $\tau$       & \textbf{p90\_ppl\,(.21)}, \textbf{var\_surp\,(.16)}, p75\,(.12), m\_surp\,(.09), ttr\,(.05) \\
82	OLMo, top-$k$      & \textbf{p90\_ppl\,(.20)}, \textbf{var\_surp\,(.17)}, p75\,(.10), m\_surp\,(.07), m\_ppl\,(.05) \\
83	\bottomrule
84	\end{tabular}}
85	\end{table}
86	
87	\begin{figure}[t]
88	\centering
89	\includegraphics[width=\columnwidth]{figures/fig_atlas_heatmap.pdf}
90	\caption{Atlas feature importance heatmap. Rows: 19 features grouped by category (\S\ref{sec:method:features}); columns: 9 model--strategy cells. Color intensity encodes RF Gini importance. The perplexity-tail and surprisal-variance blocks maintain high importance across all cells.}
91	\label{fig:atlas_heatmap}
92	\end{figure}
93	
94	%% ----------------------------------------------------------------
95	\subsection{Monotonicity and Inter-Depth Distances}
96	\label{sec:atlas:monotonicity}
97	
98	Depth features exhibit strong monotonic trends: perplexity tail statistics (\texttt{p90\_ppl}, \texttt{mean\_surprisal}) decrease with depth (Spearman $\rho = -1.0$ across cell-level medians) while repetition features increase. This pattern reflects the complementary narrowing and self-repetition of distribution collapse.
99	Inter-depth distances are non-uniform: d0-vs-d1 AUC exceeds 0.99 in all 9 cells, whereas d2-vs-d3 ranges from 0.69 to 0.89; separating adjacent deep generations requires the tail statistics identified in \S\ref{sec:atlas:features}.
100	
101	\begin{figure}[t]
102	\centering
103	\includegraphics[width=\columnwidth]{figures/fig_feature_trajectory.pdf}
104	\caption{Feature trajectories across depths $d{=}0$ to $d{=}3$, stratified by model (columns) and strategy (line style). Top row: \texttt{p90\_ppl} (monotonically decreasing). Middle: \texttt{var\_surprisal} (decreasing). Bottom: \texttt{rep\_3gram} (increasing). Shaded bands: interquartile range. The $d{=}0 \to d{=}1$ gap exceeds all subsequent inter-depth gaps.}
105	\label{fig:feature_trajectory}
106	\end{figure}
107	
108	%% ----------------------------------------------------------------
109	\subsection{EDD Analysis}
110	\label{sec:atlas:edd}
111	
112	We extend the benchmark to depth $d{=}5$ for all three models under nucleus sampling.
113	Each model's depth-3 LoRA checkpoint is used to finetune and generate depth-4 data, and the process repeats for depth~5; feature extraction uses the same reference model (Pythia-1.4B).
114	We train dedicated binary RF classifiers (500 trees) for each adjacent pair, as defined in Eq.~\ref{eq:edd}.
115	
116	\paragraph{AUC decay profile.}
117	Figure~\ref{fig:auc_decay} plots the binary pairwise AUC decay curves.
118	For Pythia-1.4B (nucleus), AUC decays monotonically: d0-vs-d1 $= 0.999$, d1-vs-d2 $= 0.925$, d2-vs-d3 $= 0.823$, d3-vs-d4 $= 0.784$, d4-vs-d5 $= 0.683$.
119	The steepest drop occurs between the d1-vs-d2 and d2-vs-d3 pairs; the curve then flattens as the system approaches an indistinguishable regime gradually rather than crossing a sharp boundary.
120	
121	\paragraph{AUC-excess contraction.}
122	The AUC-excess ($\mathrm{AUC} - 0.5$) contracts across successive depth pairs.
123	For the three-model mean profile (excess values $0.453, 0.362, 0.266, 0.183$ for pairs d1v2 through d4v5), the contraction ratio decreases from 0.80 to 0.69; convergence toward indistinguishability accelerates.
124	Per-model variation is larger (Pythia: 0.64--0.88) and reflects model-specific saturation rates.
125	This non-uniform contraction motivates the EDD metric (Eq.~\ref{eq:edd}): a depth threshold beyond which pairwise AUC falls below a practical detection limit.
126	
127	\paragraph{Cross-model convergence at depth 4--5.}
128	The d3-vs-d4 AUC consistently clusters near the $T{=}0.75$ threshold across all three models (Pythia $0.784$, OLMo $0.765$, GPT-2~XL $0.750$), while d4-vs-d5 uniformly falls below $0.70$ ($0.681$--$0.684$).
129	The directional pattern is consistent, but statistical strength is stratified: bootstrap testing ($10{,}000$ resamples, $H_0{:}\, \mathrm{AUC} \leq 0.75$) yields $p = 0.001$ for Pythia (significant), $p = 0.091$ for OLMo (marginal), and $p = 0.505$ for GPT-2~XL (non-significant).
130	All three models cross the $T{=}0.75$ threshold within the d3--d4 region; a consistent depth-4 decay boundary emerges with graded confidence rather than uniform statistical significance.
131	The d4-vs-d5 saturation is unambiguous across models; this supports the interpretation of d3--d4 as a \emph{transition zone} from discriminable to indistinguishable regime.
132	
133	\paragraph{EDD threshold sensitivity.}
134	Table~\ref{tab:edd_sensitivity} reports $\mathrm{EDD}_T$ across the primary 9-cell benchmark (depths 0--3) at four threshold values.
135	At $T{=}0.65$, all 9 cells achieve $\mathrm{EDD} = 3$; at $T{=}0.75$, 7 of 9 cells maintain $\mathrm{EDD} \geq 3$; at $T{=}0.80$, the count drops to 5 of 9.
136	The cells losing $\mathrm{EDD}{=}3$ first are consistently the top-$k$ configurations (Pythia top-$k$ at $T{=}0.70$, then OLMo top-$k$ at $T{=}0.75$), where the d2-vs-d3 pair is the consistent bottleneck across all 9 cells.
137	
138	\begin{table}[t]
139	\centering
140	\small
141	\caption{Number of atlas cells achieving $\mathrm{EDD} \geq 3$ at each threshold $T$, across 9 model--strategy cells (depths 0--3). The d2-vs-d3 boundary is the bottleneck; top-$k$ cells drop first.}
142	\label{tab:edd_sensitivity}
143	\begin{tabular}{@{}lcccc@{}}
144	\toprule
145	& $T{=}0.65$ & $T{=}0.70$ & $T{=}0.75$ & $T{=}0.80$ \\
146	\midrule
147	Cells with $\mathrm{EDD} \geq 3$ & 9/9 & 8/9 & 7/9 & 5/9 \\
148	\bottomrule
149	\end{tabular}
150	\end{table}
151	
152	\begin{figure}[t]
153	\centering
154	\includegraphics[width=\columnwidth]{figures/fig_auc_decay.pdf}
155	\caption{Binary pairwise AUC decay curves for three models (nucleus sampling, depths 0--5). Horizontal dashed lines mark $T \in \{0.65, 0.70, 0.75, 0.80\}$. All three curves converge below 0.70 at d4-vs-d5, while d3-vs-d4 AUC clusters in the range 0.750--0.784. Shaded bands: bootstrap 95\% CIs.}
156	\label{fig:auc_decay}
157	\end{figure}
158	
159	\paragraph{Decision boundary dilution.}
160	\label{sec:atlas:edd:dilution}
161	EDD uses binary-pair classifiers to avoid \emph{decision boundary dilution}: in Pythia nucleus, d2\,vs.\,d3 AUC degrades from 0.804 (4-class) to 0.689 (6-class), a 14.3\% relative decline despite identical data, because shared decision boundaries dilute per-pair capacity.
162	Binary classifiers eliminate this confound and isolate true adjacent-pair discriminability.
163	
164	%% ----------------------------------------------------------------
165	\subsection{Strategy-Dependent Trajectories}
166	\label{sec:atlas:strategy}
167	
168	The three decoding strategies induce qualitatively distinct degradation trajectories.
169	Nucleus ($p{=}0.95$) produces the most consistent accuracy (78.7--84.1\%) and serves as the reference trajectory.
170	Temperature ($\tau{=}0.9$) yields the highest accuracy in 2/3 models (GPT-2~XL 85.9\%, OLMo 82.1\%) because uniform logit scaling accelerates convergence to an attractor distribution~\cite{shumailov2024_nature}, amplifying the statistical fingerprint. However, this acceleration creates a boundary reversal risk: temperature depth-$N$ features approximate nucleus/top-$k$ depth-$(N{+}1)$ features, causing cross-strategy classifiers to systematically overpredict depth (\S\ref{sec:generalization}).
171	Top-$k$ ($k{=}50$) produces the lowest accuracy (68.8--75.9\%) because hard vocabulary truncation removes depth-discriminative low-probability tokens, though feature direction is preserved (cross-model $\rho = 0.811$).
172	The strategy effect (9.2~pp range) exceeds the model effect (7.2~pp); deployment-time knowledge of the decoding strategy therefore matters at least as much as the generator model.
173	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8386d3e-7166-4900-918f-eeeaaa3eb1d0",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "b2fea4f7-13d6-4185-b5da-f56785a7694c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
      "content": "\\section{The Depth Degradation Atlas}\n\\label{sec:atlas}\n\nWe present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.\nThe atlas spans $3 \\times 3 = 9$ model--strategy cells evaluated at depths $d \\in \\{0, 1, 2, 3\\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\\S\\ref{sec:atlas:edd}).\n\n%% ----------------------------------------------------------------\n\\subsection{In-Distribution Performance}\n\\label{sec:atlas:id}\n\nTable~\\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.\nAccuracy ranges from 68.8\\% (Pythia, top-$k$) to 85.9\\% (GPT-2~XL, temperature), all exceeding the 25\\% chance baseline by a wide margin.\nTwo axis effects emerge.\nGPT-2~XL achieves the highest accuracy under every strategy (75.9--85.9\\%), followed by OLMo (74.5--82.1\\%) and Pythia (68.8--78.7\\%).\nTop-$k$ sampling yields the lowest accuracy in every model.\nThe mean within-model strategy gap is 9.2~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy and model family contribute roughly equally to performance variance.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Four-class RF accuracy (\\%) with bootstrap 95\\% CI (${\\pm}$half-width; 10{,}000 resamples) across the $3 \\times 3$ atlas; d1--d3 three-class accuracy in parentheses (chance = 25\\% / 33\\%). Depth-0 recall exceeds 98\\% in all cells.}\n\\label{tab:main_matrix}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n& Nucleus & Temp.\\ $\\tau{=}0.9$ & Top-$k$ \\\\\n\\midrule\nPythia-1.4B  & 78.7{\\scriptsize$\\pm$0.5}\\,(71.2) & 76.7{\\scriptsize$\\pm$0.5}\\,(70.6) & 68.8{\\scriptsize$\\pm$0.6}\\,(58.8) \\\\\nOLMo-1B     & 78.9{\\scriptsize$\\pm$0.5}\\,(75.0) & 82.1{\\scriptsize$\\pm$0.5}\\,(76.3) & 74.5{\\scriptsize$\\pm$0.5}\\,(66.1) \\\\\nGPT-2~XL    & \\textbf{84.1}{\\scriptsize$\\pm$0.5}\\,(79.0) & \\textbf{85.9}{\\scriptsize$\\pm$0.5}\\,(82.6) & \\textbf{75.9}{\\scriptsize$\\pm$0.6}\\,(69.5) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Per-class recall distribution.}\nDepth-0 recall exceeds 98\\% in all 9 cells; human-written text is thus trivially separable from any generation depth.\nAmong generated depths, d2 consistently yields the lowest recall (46--73\\% across cells), followed by d3 (58--82\\%) and d1 (72--91\\%).\nFor example, Pythia-1.4B nucleus achieves per-class recall of d0$\\,{=}\\,$99\\%, d1$\\,{=}\\,$82\\%, d2$\\,{=}\\,$59\\%, d3$\\,{=}\\,$72\\%.\nThe strongest d2 recall is obtained by GPT-2~XL nucleus (73\\%).\nThe d2 trough reflects its position at the center of the depth gradient: d2 features overlap with both the d1 distribution above and d3 below and is therefore the most confusable class, consistent with the d2-vs-d3 pair as the EDD bottleneck (\\S\\ref{sec:atlas:edd}).\nFull per-class recall for all cells appears in Appendix~\\ref{app:per_class}.\n\n%% ----------------------------------------------------------------\n\\subsection{Feature Consistency Across the Grid}\n\\label{sec:atlas:features}\n\nDespite the 17.1~pp accuracy spread across cells, a small feature family dominates in every setting.\nPerplexity tail statistics as a feature group dominate depth discrimination: the 90th-percentile perplexity (\\texttt{p90\\_ppl}) ranks top-2 by Gini importance in all 9 cells; surprisal variance (\\texttt{var\\_surprisal}) in 8/9 under SHAP (7/9 under Gini; Appendix~\\ref{app:permutation}).\\footnote{Individual feature rankings should be interpreted cautiously given high multicollinearity (VIF${>}$10 for 14--16/19 features); the group-level dominance of perplexity tail statistics is robust across importance measures.}\nTable~\\ref{tab:feature_importance} shows the full per-cell ranking.\n\nCross-model feature-rank Spearman correlation averages $\\bar{\\rho} = 0.868$ (range $[0.619, 0.954]$): models agree on which features carry depth information even when they differ in absolute accuracy.\nAmong strategies, top-$k$ yields the highest cross-model rank correlation ($\\rho = 0.811$): the deterministic vocabulary truncation imposes a more uniform feature landscape across architectures, at the cost of weaker overall signal (\\S\\ref{sec:atlas:strategy}).\n\nPercentile-based features outperform their moment-based counterparts.\nToken-level perplexity distributions are heavy-tailed: individual outlier passages can dominate the arithmetic mean of their depth class, whereas \\texttt{p90\\_ppl} is robust to such extremes while still capturing the tail erosion that signals generation depth.\n\nFeature ablation confirms this concentration: the top-2 features (\\texttt{p90\\_ppl} + \\texttt{var\\_surprisal}) alone reach 91.1\\% of full accuracy (71.5\\%), and the top-5 features achieve 97.6\\% (76.5\\% vs.\\ 78.4\\%), with perplexity statistics alone reaching 76.6\\% (vs.\\ surprisal 73.2\\%, other categories ${\\leq}$47\\%).\nVariance inflation analysis reveals VIF${>}$10 for 14--16 of 19 features; effective independent dimensionality is ${\\approx}$4--5.\nForward selection independently confirms the dominant pair: \\texttt{p90\\_ppl} is selected first in 6/9 cells, \\texttt{var\\_surprisal} in 3/9.\n\nThe feature hierarchy also shifts with depth.\nAt shallow boundaries (d1 vs.\\ d2), \\texttt{var\\_surprisal} dominates importance; at deeper boundaries (d3 vs.\\ d4, d4 vs.\\ d5), tail perplexity statistics (\\texttt{p90\\_ppl}, \\texttt{kurtosis\\_ppl}) take over.\nThis transition aligns with model-collapse dynamics~\\cite{shumailov2024_nature}: early recursion narrows the surprisal distribution (captured by its variance), while later steps erode the perplexity tail (captured by upper quantiles and kurtosis).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Top-5 features by Gini importance. \\textbf{Bold}: top-2. \\texttt{p90\\_ppl} top-2 in 9/9; \\texttt{var\\_surprisal} 8/9 under SHAP (7/9 under Gini).}\n\\label{tab:feature_importance}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l l@{}}\n\\toprule\nCell & Top-5 features (Gini importance, ranked) \\\\\n\\midrule\nPythia, nuc.       & \\textbf{var\\_surp\\,(.17)}, \\textbf{p90\\_ppl\\,(.15)}, m\\_ppl\\,(.11), var\\_ppl\\,(.08), p75\\,(.07) \\\\\nPythia, $\\tau$     & \\textbf{var\\_surp\\,(.17)}, \\textbf{p90\\_ppl\\,(.14)}, m\\_ppl\\,(.11), p75\\,(.07), m\\_surp\\,(.07) \\\\\nPythia, top-$k$    & \\textbf{var\\_surp\\,(.16)}, \\textbf{p90\\_ppl\\,(.12)}, m\\_ppl\\,(.11), var\\_ppl\\,(.07), m\\_surp\\,(.06) \\\\\nGPT-2\\,XL, nuc.    & \\textbf{var\\_surp\\,(.21)}, \\textbf{p90\\_ppl\\,(.21)}, p75\\,(.10), m\\_surp\\,(.07), m\\_ppl\\,(.06) \\\\\nGPT-2\\,XL, $\\tau$  & \\textbf{p90\\_ppl\\,(.25)}, \\textbf{p75\\,(.15)}, m\\_surp\\,(.13), var\\_surp\\,(.12), p50\\,(.05) \\\\\nGPT-2\\,XL, top-$k$ & \\textbf{p90\\_ppl\\,(.24)}, \\textbf{p75\\,(.12)}, var\\_surp\\,(.10), m\\_surp\\,(.09), ttr\\,(.04) \\\\\nOLMo, nuc.         & \\textbf{p90\\_ppl\\,(.18)}, \\textbf{var\\_surp\\,(.15)}, p75\\,(.11), m\\_surp\\,(.07), ttr\\,(.06) \\\\\nOLMo, $\\tau$       & \\textbf{p90\\_ppl\\,(.21)}, \\textbf{var\\_surp\\,(.16)}, p75\\,(.12), m\\_surp\\,(.09), ttr\\,(.05) \\\\\nOLMo, top-$k$      & \\textbf{p90\\_ppl\\,(.20)}, \\textbf{var\\_surp\\,(.17)}, p75\\,(.10), m\\_surp\\,(.07), m\\_ppl\\,(.05) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_atlas_heatmap.pdf}\n\\caption{Atlas feature importance heatmap. Rows: 19 features grouped by category (\\S\\ref{sec:method:features}); columns: 9 model--strategy cells. Color intensity encodes RF Gini importance. The perplexity-tail and surprisal-variance blocks maintain high importance across all cells.}\n\\label{fig:atlas_heatmap}\n\\end{figure}\n\n%% ----------------------------------------------------------------\n\\subsection{Monotonicity and Inter-Depth Distances}\n\\label{sec:atlas:monotonicity}\n\nDepth features exhibit strong monotonic trends: perplexity tail statistics (\\texttt{p90\\_ppl}, \\texttt{mean\\_surprisal}) decrease with depth (Spearman $\\rho = -1.0$ across cell-level medians) while repetition features increase. This pattern reflects the complementary narrowing and self-repetition of distribution collapse.\nInter-depth distances are non-uniform: d0-vs-d1 AUC exceeds 0.99 in all 9 cells, whereas d2-vs-d3 ranges from 0.69 to 0.89; separating adjacent deep generations requires the tail statistics identified in \\S\\ref{sec:atlas:features}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_feature_trajectory.pdf}\n\\caption{Feature trajectories across depths $d{=}0$ to $d{=}3$, stratified by model (columns) and strategy (line style). Top row: \\texttt{p90\\_ppl} (monotonically decreasing). Middle: \\texttt{var\\_surprisal} (decreasing). Bottom: \\texttt{rep\\_3gram} (increasing). Shaded bands: interquartile range. The $d{=}0 \\to d{=}1$ gap exceeds all subsequent inter-depth gaps.}\n\\label{fig:feature_trajectory}\n\\end{figure}\n\n%% ----------------------------------------------------------------\n\\subsection{EDD Analysis}\n\\label{sec:atlas:edd}\n\nWe extend the benchmark to depth $d{=}5$ for all three models under nucleus sampling.\nEach model's depth-3 LoRA checkpoint is used to finetune and generate depth-4 data, and the process repeats for depth~5; feature extraction uses the same reference model (Pythia-1.4B).\nWe train dedicated binary RF classifiers (500 trees) for each adjacent pair, as defined in Eq.~\\ref{eq:edd}.\n\n\\paragraph{AUC decay profile.}\nFigure~\\ref{fig:auc_decay} plots the binary pairwise AUC decay curves.\nFor Pythia-1.4B (nucleus), AUC decays monotonically: d0-vs-d1 $= 0.999$, d1-vs-d2 $= 0.925$, d2-vs-d3 $= 0.823$, d3-vs-d4 $= 0.784$, d4-vs-d5 $= 0.683$.\nThe steepest drop occurs between the d1-vs-d2 and d2-vs-d3 pairs; the curve then flattens as the system approaches an indistinguishable regime gradually rather than crossing a sharp boundary.\n\n\\paragraph{AUC-excess contraction.}\nThe AUC-excess ($\\mathrm{AUC} - 0.5$) contracts across successive depth pairs.\nFor the three-model mean profile (excess values $0.453, 0.362, 0.266, 0.183$ for pairs d1v2 through d4v5), the contraction ratio decreases from 0.80 to 0.69; convergence toward indistinguishability accelerates.\nPer-model variation is larger (Pythia: 0.64--0.88) and reflects model-specific saturation rates.\nThis non-uniform contraction motivates the EDD metric (Eq.~\\ref{eq:edd}): a depth threshold beyond which pairwise AUC falls below a practical detection limit.\n\n\\paragraph{Cross-model convergence at depth 4--5.}\nThe d3-vs-d4 AUC consistently clusters near the $T{=}0.75$ threshold across all three models (Pythia $0.784$, OLMo $0.765$, GPT-2~XL $0.750$), while d4-vs-d5 uniformly falls below $0.70$ ($0.681$--$0.684$).\nThe directional pattern is consistent, but statistical strength is stratified: bootstrap testing ($10{,}000$ resamples, $H_0{:}\\, \\mathrm{AUC} \\leq 0.75$) yields $p = 0.001$ for Pythia (significant), $p = 0.091$ for OLMo (marginal), and $p = 0.505$ for GPT-2~XL (non-significant).\nAll three models cross the $T{=}0.75$ threshold within the d3--d4 region; a consistent depth-4 decay boundary emerges with graded confidence rather than uniform statistical significance.\nThe d4-vs-d5 saturation is unambiguous across models; this supports the interpretation of d3--d4 as a \\emph{transition zone} from discriminable to indistinguishable regime.\n\n\\paragraph{EDD threshold sensitivity.}\nTable~\\ref{tab:edd_sensitivity} reports $\\mathrm{EDD}_T$ across the primary 9-cell benchmark (depths 0--3) at four threshold values.\nAt $T{=}0.65$, all 9 cells achieve $\\mathrm{EDD} = 3$; at $T{=}0.75$, 7 of 9 cells maintain $\\mathrm{EDD} \\geq 3$; at $T{=}0.80$, the count drops to 5 of 9.\nThe cells losing $\\mathrm{EDD}{=}3$ first are consistently the top-$k$ configurations (Pythia top-$k$ at $T{=}0.70$, then OLMo top-$k$ at $T{=}0.75$), where the d2-vs-d3 pair is the consistent bottleneck across all 9 cells.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Number of atlas cells achieving $\\mathrm{EDD} \\geq 3$ at each threshold $T$, across 9 model--strategy cells (depths 0--3). The d2-vs-d3 boundary is the bottleneck; top-$k$ cells drop first.}\n\\label{tab:edd_sensitivity}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n& $T{=}0.65$ & $T{=}0.70$ & $T{=}0.75$ & $T{=}0.80$ \\\\\n\\midrule\nCells with $\\mathrm{EDD} \\geq 3$ & 9/9 & 8/9 & 7/9 & 5/9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_auc_decay.pdf}\n\\caption{Binary pairwise AUC decay curves for three models (nucleus sampling, depths 0--5). Horizontal dashed lines mark $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$. All three curves converge below 0.70 at d4-vs-d5, while d3-vs-d4 AUC clusters in the range 0.750--0.784. Shaded bands: bootstrap 95\\% CIs.}\n\\label{fig:auc_decay}\n\\end{figure}\n\n\\paragraph{Decision boundary dilution.}\n\\label{sec:atlas:edd:dilution}\nEDD uses binary-pair classifiers to avoid \\emph{decision boundary dilution}: in Pythia nucleus, d2\\,vs.\\,d3 AUC degrades from 0.804 (4-class) to 0.689 (6-class), a 14.3\\% relative decline despite identical data, because shared decision boundaries dilute per-pair capacity.\nBinary classifiers eliminate this confound and isolate true adjacent-pair discriminability.\n\n%% ----------------------------------------------------------------\n\\subsection{Strategy-Dependent Trajectories}\n\\label{sec:atlas:strategy}\n\nThe three decoding strategies induce qualitatively distinct degradation trajectories.\nNucleus ($p{=}0.95$) produces the most consistent accuracy (78.7--84.1\\%) and serves as the reference trajectory.\nTemperature ($\\tau{=}0.9$) yields the highest accuracy in 2/3 models (GPT-2~XL 85.9\\%, OLMo 82.1\\%) because uniform logit scaling accelerates convergence to an attractor distribution~\\cite{shumailov2024_nature}, amplifying the statistical fingerprint. However, this acceleration creates a boundary reversal risk: temperature depth-$N$ features approximate nucleus/top-$k$ depth-$(N{+}1)$ features, causing cross-strategy classifiers to systematically overpredict depth (\\S\\ref{sec:generalization}).\nTop-$k$ ($k{=}50$) produces the lowest accuracy (68.8--75.9\\%) because hard vocabulary truncation removes depth-discriminative low-probability tokens, though feature direction is preserved (cross-model $\\rho = 0.811$).\nThe strategy effect (9.2~pp range) exceeds the model effect (7.2~pp); deployment-time knowledge of the decoding strategy therefore matters at least as much as the generator model.\n",
      "numLines": 173,
      "startLine": 1,
      "totalLines": 173
    }
  },
  "sourceToolAssistantUUID": "a8386d3e-7166-4900-918f-eeeaaa3eb1d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 41 · 2026-05-18T14:11:06.192Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xrwy1A8vAgh87S9L8kTPzY`</summary>

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
  "parentUuid": "b2fea4f7-13d6-4185-b5da-f56785a7694c",
  "isSidechain": false,
  "requestId": "req_011CbAAmYGEvUKzNL8bqZWne",
  "type": "assistant",
  "uuid": "5aa32cd6-be09-419b-8eee-03f4938d4963",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPHHq3gYENpMxrx56HQeua",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6519,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 31653,
      "output_tokens": 454,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6519,
          "output_tokens": 454,
          "cache_read_input_tokens": 31653,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1449
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-18T14:11:08.345Z_

<details><summary>↩ Tool result · `toolu_016oemmX4pH8VBimoNjXFB95`</summary>

```text
1	% ============================================================
2	% Model Collapse Theory
3	% ============================================================
4	
5	@article{shumailov2024_nature,
6	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
7	  title     = {{AI models collapse when trained on recursively generated data}},
8	  journal   = {Nature},
9	  volume    = {631},
10	  pages     = {755--759},
11	  year      = {2024},
12	  doi       = {10.1038/s41586-024-07566-y},
13	}
14	
15	@inproceedings{dohmatob2024_tale_of_tails,
16	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
17	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
18	  booktitle = {Proceedings of ICML},
19	  year      = {2024},
20	  note      = {arXiv:2402.07043},
21	  url       = {https://arxiv.org/abs/2402.07043},
22	}
23	
24	@inproceedings{dohmatob2025_strong_collapse,
25	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
26	  title     = {{Strong Model Collapse}},
27	  booktitle = {Proceedings of ICLR},
28	  year      = {2025},
29	  note      = {arXiv:2410.04840},
30	  url       = {https://arxiv.org/abs/2410.04840},
31	}
32	
33	@inproceedings{dohmatob2024_demystified,
34	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
35	  title     = {{Model Collapse Demystified: The Case of Regression}},
36	  booktitle = {Proceedings of NeurIPS},
37	  year      = {2024},
38	  note      = {arXiv:2402.07712},
39	  url       = {https://arxiv.org/abs/2402.07712},
40	}
41	
42	@inproceedings{alemohammad2024_mad,
43	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
44	  title     = {{Self-Consuming Generative Models Go MAD}},
45	  booktitle = {Proceedings of ICLR},
46	  year      = {2024},
47	  note      = {arXiv:2307.01850},
48	  url       = {https://arxiv.org/abs/2307.01850},
49	}
50	
51	@misc{gerstgrasser2024_accumulate,
52	  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
53	  title     = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
54	  year      = {2024},
55	  howpublished = {arXiv:2404.01413},
56	  url       = {https://arxiv.org/abs/2404.01413},
57	}
58	
59	@inproceedings{marchi2024_heat_death,
60	  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},
61	  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},
62	  booktitle = {Proceedings of ICASSP},
63	  year      = {2024},
64	  note      = {arXiv:2404.02325},
65	  url       = {https://arxiv.org/abs/2404.02325},
66	}
67	
68	@misc{knowledge_collapse2025,
69	  author    = {Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},
70	  title     = {{Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training}},
71	  year      = {2025},
72	  howpublished = {arXiv:2509.04796},
73	  url       = {https://arxiv.org/abs/2509.04796},
74	}
75	
76	@misc{sigma2026_spectral,
77	  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},
78	  title     = {{SIGMA: Scalable Spectral Insights for LLM Model Collapse}},
79	  year      = {2026},
80	  howpublished = {arXiv:2601.03385},
81	  url       = {https://arxiv.org/abs/2601.03385},
82	}
83	
84	@inproceedings{mohamed2025_broken_telephone,
85	  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
86	  title     = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
87	  booktitle = {Proceedings of ACL},
88	  year      = {2025},
89	  note      = {arXiv:2502.20258},
90	  url       = {https://arxiv.org/abs/2502.20258},
91	}
92	
93	@inproceedings{synthetic_eggs2026,
94	  author    = {Schaffelder, Max and Gatt, Albert},
95	  title     = {{Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning}},
96	  booktitle = {Findings of ACL},
97	  year      = {2026},
98	  note      = {arXiv:2511.01490},
99	  url       = {https://arxiv.org/abs/2511.01490},
100	}
101	
102	@inproceedings{shi2025_closer_look,
103	  author    = {Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},
104	  title     = {{A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective}},
105	  booktitle = {Proceedings of NeurIPS},
106	  year      = {2025},
107	  note      = {Spotlight},
108	}
109	
110	@inproceedings{yi2026_escaping_collapse,
111	  author    = {Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},
112	  title     = {{Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence}},
113	  booktitle = {3rd DATA-FM Workshop at ICLR 2026},
114	  year      = {2026},
115	}
116	
117	% --- Model collapse: collapse-can-be-avoided / contamination ---
118	
119	@inproceedings{drayson2025_detection_prevents_collapse,
120	  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
121	  title     = {{Machine-generated text detection prevents language model collapse}},
122	  booktitle = {Findings of EMNLP},
123	  year      = {2025},
124	  note      = {arXiv:2502.15654},
125	  url       = {https://arxiv.org/abs/2502.15654},
126	}
127	
128	@misc{bakshi2026_collapse_improvement,
129	  author    = {Bakshi, Soham and Chakraborty, Sunrit},
130	  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},
131	  year      = {2026},
132	  howpublished = {arXiv:2602.10531},
133	  url       = {https://arxiv.org/abs/2602.10531},
134	}
135	
136	@misc{wang2026_contamination,
137	  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},
138	  title     = {{Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training}},
139	  year      = {2026},
140	  howpublished = {arXiv:2602.16065},
141	  url       = {https://arxiv.org/abs/2602.16065},
142	}
143	
144	@misc{falahati2026_curated,
145	  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},
146	  title     = {{Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences}},
147	  year      = {2026},
148	  howpublished = {arXiv:2605.07724},
149	  url       = {https://arxiv.org/abs/2605.07724},
150	}
151	
152	% ============================================================
153	% AI-Generated Text Detection
154	% ============================================================
155	
156	@article{wu2025_detection_survey,
157	  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
158	  title     = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
159	  journal   = {Computational Linguistics},
160	  volume    = {51},
161	  number    = {1},
162	  pages     = {275--354},
163	  year      = {2025},
164	  publisher = {MIT Press},
165	}
166	
167	% --- Statistical / zero-shot detectors ---
168	
169	@inproceedings{gehrmann2019_gltr,
170	  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
171	  title     = {{GLTR: Statistical Detection and Visualization of Generated Text}},
172	  booktitle = {Proceedings of ACL: System Demonstrations},
173	  year      = {2019},
174	  note      = {arXiv:1906.04043},
175	  url       = {https://arxiv.org/abs/1906.04043},
176	}
177	
178	@inproceedings{mitchell2023_detectgpt,
179	  author    = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
180	  title     = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
181	  booktitle = {Proceedings of ICML},
182	  year      = {2023},
183	  note      = {arXiv:2301.11305},
184	  url       = {https://arxiv.org/abs/2301.11305},
185	}
186	
187	@inproceedings{fast_detectgpt2024,
188	  author    = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
189	  title     = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
190	  booktitle = {Proceedings of ICLR},
191	  year      = {2024},
192	  note      = {arXiv:2310.05130},
193	  url       = {https://arxiv.org/abs/2310.05130},
194	}
195	
196	@inproceedings{binoculars2024,
197	  author    = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
198	  title     = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
199	  booktitle = {Proceedings of ICML},
200	  year      = {2024},
201	  note      = {arXiv:2401.12070},
202	  url       = {https://arxiv.org/abs/2401.12070},
203	}
204	
205	@article{diveye2026,
206	  author    = {Basani, Advik Raj and Chen, Pin-Yu},
207	  title     = {{Diversity Boosts AI-Generated Text Detection}},
208	  journal   = {Transactions on Machine Learning Research (TMLR)},
209	  year      = {2026},
210	  note      = {arXiv:2509.18880},
211	  url       = {https://arxiv.org/abs/2509.18880},
212	}
213	
214	% --- Robustness / limitations of detectors ---
215	
216	@misc{sadasivan2023_paraphrase,
217	  author    = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
218	  title     = {{Can AI-Generated Text be Reliably Detected?}},
219	  year      = {2023},
220	  howpublished = {arXiv:2303.11156},
221	  url       = {https://arxiv.org/abs/2303.11156},
222	}
223	
224	@misc{pudasaini2026_detection_fails,
225	  author    = {Pudasaini, Shushanta and Miralles-Pech{\'u}an, Luis and Lillis, David and Llorens Salvador, Marisa},
226	  title     = {{Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy}},
227	  year      = {2026},
228	  howpublished = {arXiv:2603.23146},
229	  url       = {https://arxiv.org/abs/2603.23146},
230	}
231	
232	@misc{pu2026_generator_barrier,
233	  author    = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},
234	  title     = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},
235	  year      = {2026},
236	  howpublished = {arXiv:2604.13692},
237	  url       = {https://arxiv.org/abs/2604.13692},
238	}
239	
240	% --- Beyond binary: attribution, editing extent, benchmarks ---
241	
242	@inproceedings{bevendorff2025_two_paradigms,
243	  author    = {Bevendorff, Janek and Wiegmann, Matti and Richter, Emmelie and Potthast, Martin and Stein, Benno},
244	  title     = {{The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification}},
245	  booktitle = {Findings of ACL},
246	  pages     = {3762--3787},
247	  year      = {2025},
248	  address   = {Vienna, Austria},
249	}
250	
251	@inproceedings{uchendu2020_attribution,
252	  author    = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
253	  title     = {{Authorship Attribution for Neural Text Generation}},
254	  booktitle = {Proceedings of EMNLP},
255	  year      = {2020},
256	}
257	
258	@inproceedings{editlens2026,
259	  author    = {Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit},
260	  title     = {{EditLens: Quantifying the Extent of AI Editing in Text}},
261	  booktitle = {Proceedings of ICLR},
262	  year      = {2026},
263	  note      = {arXiv:2510.03154},
264	  url       = {https://arxiv.org/abs/2510.03154},
265	}
266	
267	@inproceedings{loki2025,
268	  author    = {Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi and Kang, Hengrui and He, Jun and Lin, Honglin and Wang, Zihao and Wu, Tong and Wu, Zhizheng and Chen, Yiping and Lin, Dahua and He, Conghui and Li, Weijia},
269	  title     = {{LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models}},
270	  booktitle = {Proceedings of ICLR (Spotlight)},
271	  year      = {2025},
272	  note      = {arXiv:2410.09732},
273	  url       = {https://arxiv.org/abs/2410.09732},
274	}
275	
276	% --- Geometric / intrinsic dimension detectors ---
277	
278	@inproceedings{tulchinskii2023_intrinsic_dim,
279	  author    = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Barannikov, Serguei and Piontkovskaya, Irina and Nikolenko, Sergey and Burnaev, Evgeny},
280	  title     = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},
281	  booktitle = {Proceedings of NeurIPS},
282	  year      = {2023},
283	  note      = {arXiv:2306.04723},
284	  url       = {https://arxiv.org/abs/2306.04723},
285	}
286	
287	% --- Statistical / feature-based / shared-task detectors ---
288	
289	@inproceedings{verma2024_ghostbuster,
290	  author    = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},
291	  title     = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},
292	  booktitle = {Proceedings of NAACL},
293	  year      = {2024},
294	  note      = {arXiv:2305.15047},
295	  url       = {https://arxiv.org/abs/2305.15047},
296	}
297	
298	@inproceedings{wang2024_m4_semeval,
299	  author    = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
300	  title     = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
301	  booktitle = {Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)},
302	  year      = {2024},
303	  note      = {arXiv:2404.14183},
304	  url       = {https://arxiv.org/abs/2404.14183},
305	}
306	
307	@inproceedings{li2024_mage,
308	  author    = {Li, Yongkang and Li, Donghao and Yang, Yue and Hu, Baotian and Zhang, Min},
309	  title     = {{MAGE: Machine-generated Text Detection in the Wild}},
310	  booktitle = {Proceedings of ACL},
311	  year      = {2024},
312	  note      = {arXiv:2305.13242},
313	  url       = {https://arxiv.org/abs/2305.13242},
314	}
315	
316	@inproceedings{yang2024_dnagpt,
317	  author    = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
318	  title     = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
319	  booktitle = {Proceedings of ICLR},
320	  year      = {2024},
321	  note      = {arXiv:2305.17359},
322	  url       = {https://arxiv.org/abs/2305.17359},
323	}
324	
325	% --- Watermarking ---
326	
327	@inproceedings{kirchenbauer2023_watermark,
328	  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
329	  title     = {{A Watermark for Large Language Models}},
330	  booktitle = {Proceedings of ICML},
331	  year      = {2023},
332	  note      = {arXiv:2301.10226},
333	  url       = {https://arxiv.org/abs/2301.10226},
334	}
335	
336	% ============================================================
337	% Decoding Strategies
338	% ============================================================
339	
340	@inproceedings{holtzman2020_nucleus,
341	  author    = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
342	  title     = {{The Curious Case of Neural Text Degeneration}},
343	  booktitle = {Proceedings of ICLR},
344	  year      = {2020},
345	  note      = {arXiv:1904.09751},
346	  url       = {https://arxiv.org/abs/1904.09751},
347	}
348	
349	@inproceedings{finlayson2024_closing,
350	  author    = {Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabha and Sabharwal, Ashish},
351	  title     = {{Closing the Curious Case of Neural Text Degeneration}},
352	  booktitle = {Proceedings of ICLR},
353	  year      = {2024},
354	  note      = {arXiv:2310.01693},
355	  url       = {https://arxiv.org/abs/2310.01693},
356	}
357	
358	@inproceedings{garces_arias2025_decoding_decoded,
359	  author    = {{Garces Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},
360	  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},
361	  booktitle = {Proceedings of COLING},
362	  year      = {2025},
363	  note      = {arXiv:2410.06097},
364	  url       = {https://arxiv.org/abs/2410.06097},
365	}
366	
367	@article{wiher2022_decoding,
368	  author    = {Wiher, Gian and Meister, Clara and Cotterell, Ryan},
369	  title     = {{On Decoding Strategies for Neural Text Generators}},
370	  journal   = {Transactions of the Association for Computational Linguistics},
371	  volume    = {10},
372	  pages     = {997--1012},
373	  year      = {2022},
374	}
375	
376	@inproceedings{basu2021_mirostat,
377	  author    = {Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shirish and Varshney, Lav R.},
378	  title     = {{Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity}},
379	  booktitle = {Proceedings of ICLR},
380	  year      = {2021},
381	}
382	
383	% ============================================================
384	% Ordinal Classification / Contrastive Learning
385	% ============================================================
386	
387	@article{coral2020,
388	  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
389	  title     = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
390	  journal   = {Pattern Recognition Letters},
391	  volume    = {140},
392	  pages     = {325--331},
393	  year      = {2020},
394	  note      = {arXiv:1901.07884},
395	  url       = {https://arxiv.org/abs/1901.07884},
396	}
397	
398	@inproceedings{cloc2025,
399	  author    = {Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting},
400	  title     = {{CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss}},
401	  booktitle = {Proceedings of CVPR},
402	  year      = {2025},
403	  note      = {arXiv:2504.17813},
404	  url       = {https://arxiv.org/abs/2504.17813},
405	}
406	
407	% ============================================================
408	% Foundation Models / Fine-tuning
409	% ============================================================
410	
411	@inproceedings{hu2022lora,
412	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
413	  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},
414	  booktitle = {Proceedings of ICLR},
415	  year      = {2022},
416	  note      = {arXiv:2106.09685},
417	  url       = {https://arxiv.org/abs/2106.09685},
418	}
419	
420	@inproceedings{he2021_deberta_v3,
421	  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},
422	  title     = {{DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing}},
423	  booktitle = {Proceedings of ICLR},
424	  year      = {2023},
425	  note      = {arXiv:2111.09543},
426	  url       = {https://arxiv.org/abs/2111.09543},
427	}
428	
429	@misc{liu2019_roberta,
430	  author    = {Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},
431	  title     = {{RoBERTa: A Robustly Optimized BERT Pretraining Approach}},
432	  year      = {2019},
433	  howpublished = {arXiv:1907.11692},
434	  url       = {https://arxiv.org/abs/1907.11692},
435	}
436	
437	% ============================================================
438	% Data Curation / Selection
439	% ============================================================
440	
441	@inproceedings{dsir2023,
442	  author    = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
443	  title     = {{Data Selection for Language Models via Importance Resampling}},
444	  booktitle = {Proceedings of NeurIPS},
445	  year      = {2023},
446	  note      = {arXiv:2302.03169},
447	  url       = {https://arxiv.org/abs/2302.03169},
448	}
449	
450	@inproceedings{qurating2024,
451	  author    = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
452	  title     = {{QuRating: Selecting High-Quality Data for Training Language Models}},
453	  booktitle = {Proceedings of ICML},
454	  year      = {2024},
455	  note      = {arXiv:2402.09739},
456	  url       = {https://arxiv.org/abs/2402.09739},
457	}
458	
459	@inproceedings{penedo2024_fineweb,
460	  author    = {Penedo, Guilherme and Kydl{\'\i}{\v{c}}ek, Hynek and Lozhkov, Anton and Mitchell, Margaret and Wolf, Thomas and von Werra, Leandro},
461	  title     = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},
462	  booktitle = {Proceedings of NeurIPS},
463	  year      = {2024},
464	  note      = {arXiv:2406.17557},
465	  url       = {https://arxiv.org/abs/2406.17557},
466	}
467	
468	@article{sugiyama2007_importance_weighting,
469	  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\"u}ller, Klaus-Robert},
470	  title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},
471	  journal   = {Journal of Machine Learning Research},
472	  volume    = {8},
473	  pages     = {985--1005},
474	  year      = {2007},
475	}
476	
477	% ============================================================
478	% Large Language Models (cross-scale experiments)
479	% ============================================================
480	
481	@misc{qwen2.5,
482	  author    = {Qwen Team},
483	  title     = {{Qwen2.5: A Party of Foundation Models}},
484	  year      = {2025},
485	  howpublished = {arXiv:2412.15115},
486	  url       = {https://arxiv.org/abs/2412.15115},
487	}
488	
489	@misc{llama3,
490	  author    = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and others},
491	  title     = {{The Llama 3 Herd of Models}},
492	  year      = {2024},
493	  howpublished = {arXiv:2407.21783},
494	  url       = {https://arxiv.org/abs/2407.21783},
495	}
496	
497	% ============================================================
498	% Additional References (R5-R7 fixes)
499	% ============================================================
500	
501	@misc{schaeffer2025,
502	  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},
503	  title     = {{Position: Model Collapse Does Not Mean What You Think}},
504	  year      = {2025},
505	  howpublished = {arXiv:2503.03150},
506	  url       = {https://arxiv.org/abs/2503.03150},
507	}
508	
509	@inproceedings{frank2001,
510	  author    = {Frank, Eibe and Hall, Mark},
511	  title     = {{A Simple Approach to Ordinal Classification}},
512	  booktitle = {Proceedings of ECML},
513	  year      = {2001},
514	  pages     = {145--156},
515	}
516	
517	@inproceedings{rennie2005,
518	  author    = {Rennie, Jason D. M. and Srebro, Nathan},
519	  title     = {{Loss Functions for Preference Levels: Regression with Discrete Ordered Labels}},
520	  booktitle = {Proceedings of IJCAI Workshop on Advances in Preference Handling},
521	  year      = {2005},
522	}
523	
524	@article{mccullagh1980_ordinal,
525	  title={{Regression Models for Ordinal Data}},
526	  author={McCullagh, Peter},
527	  journal={Journal of the Royal Statistical Society: Series B},
528	  volume={42},
529	  number={2},
530	  pages={109--142},
531	  year={1980}
532	}
533	
534	@inproceedings{wenzek2020_ccnet,
535	  title={{CCNet}: Extracting High Quality Monolingual Datasets from Web Crawl Data},
536	  author={Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, Edouard},
537	  booktitle={Proceedings of LREC},
538	  year={2020}
539	}
540	
541	@inproceedings{dugan2024_raid,
542	  author    = {Dugan, Liam and Hwang, Alyssa and Trhl{\'\i}k, Filip and Zhu, Andrew and Ludan, Josh Magnus and Xu, Hainiu and Ippolito, Daphne and Callison-Burch, Chris},
543	  title     = {{RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors}},
544	  booktitle = {Proceedings of ACL},
545	  pages     = {12463--12492},
546	  year      = {2024},
547	  note      = {arXiv:2405.07940},
548	  url       = {https://arxiv.org/abs/2405.07940},
549	}
550	
551	% ============================================================
552	% Reviewer-requested citations (MR1--MR5)
553	% ============================================================
554	
555	@inproceedings{guo2024curious,
556	  author    = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo{\'e}},
557	  title     = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},
558	  booktitle = {Findings of NAACL},
559	  year      = {2024},
560	  note      = {arXiv:2311.09807},
561	  url       = {https://arxiv.org/abs/2311.09807},
562	}
563	
564	@inproceedings{padmakumar2024diversity,
565	  author    = {Padmakumar, Vishakh and He, He},
566	  title     = {{Does Writing with Language Models Reduce Content Diversity?}},
567	  booktitle = {Proceedings of ICLR},
568	  year      = {2024},
569	  note      = {arXiv:2309.05196},
570	  url       = {https://arxiv.org/abs/2309.05196},
571	}
572	
573	@misc{briesch2024selfconsuming,
574	  author    = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},
575	  title     = {{Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop}},
576	  year      = {2024},
577	  howpublished = {arXiv:2311.16822},
578	  url       = {https://arxiv.org/abs/2311.16822},
579	}
580	
581	@misc{seddik2024synthetic,
582	  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},
583	  title     = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},
584	  year      = {2024},
585	  howpublished = {arXiv:2404.05090},
586	  url       = {https://arxiv.org/abs/2404.05090},
587	}
588	
589	@inproceedings{pareek2024understanding,
590	  author    = {Pareek, Divyansh and Du, Simon S. and Oh, Sewoong},
591	  title     = {{Understanding the Gains from Repeated Self-Distillation}},
592	  booktitle = {Proceedings of NeurIPS},
593	  year      = {2024},
594	  note      = {arXiv:2407.04600},
595	  url       = {https://arxiv.org/abs/2407.04600},
596	}
597	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e20fd060-ba29-475a-a1b6-42a5a0eb71e7",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "feb194c8-36aa-4453-a2d6-b5edd0cc3d45",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
      "content": "% ============================================================\n% Model Collapse Theory\n% ============================================================\n\n@article{shumailov2024_nature,\n  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  title     = {{AI models collapse when trained on recursively generated data}},\n  journal   = {Nature},\n  volume    = {631},\n  pages     = {755--759},\n  year      = {2024},\n  doi       = {10.1038/s41586-024-07566-y},\n}\n\n@inproceedings{dohmatob2024_tale_of_tails,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},\n  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.07043},\n  url       = {https://arxiv.org/abs/2402.07043},\n}\n\n@inproceedings{dohmatob2025_strong_collapse,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  title     = {{Strong Model Collapse}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2025},\n  note      = {arXiv:2410.04840},\n  url       = {https://arxiv.org/abs/2410.04840},\n}\n\n@inproceedings{dohmatob2024_demystified,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},\n  title     = {{Model Collapse Demystified: The Case of Regression}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2402.07712},\n  url       = {https://arxiv.org/abs/2402.07712},\n}\n\n@inproceedings{alemohammad2024_mad,\n  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  title     = {{Self-Consuming Generative Models Go MAD}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2307.01850},\n  url       = {https://arxiv.org/abs/2307.01850},\n}\n\n@misc{gerstgrasser2024_accumulate,\n  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  title     = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  year      = {2024},\n  howpublished = {arXiv:2404.01413},\n  url       = {https://arxiv.org/abs/2404.01413},\n}\n\n@inproceedings{marchi2024_heat_death,\n  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},\n  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},\n  booktitle = {Proceedings of ICASSP},\n  year      = {2024},\n  note      = {arXiv:2404.02325},\n  url       = {https://arxiv.org/abs/2404.02325},\n}\n\n@misc{knowledge_collapse2025,\n  author    = {Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},\n  title     = {{Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training}},\n  year      = {2025},\n  howpublished = {arXiv:2509.04796},\n  url       = {https://arxiv.org/abs/2509.04796},\n}\n\n@misc{sigma2026_spectral,\n  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  title     = {{SIGMA: Scalable Spectral Insights for LLM Model Collapse}},\n  year      = {2026},\n  howpublished = {arXiv:2601.03385},\n  url       = {https://arxiv.org/abs/2601.03385},\n}\n\n@inproceedings{mohamed2025_broken_telephone,\n  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  title     = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  booktitle = {Proceedings of ACL},\n  year      = {2025},\n  note      = {arXiv:2502.20258},\n  url       = {https://arxiv.org/abs/2502.20258},\n}\n\n@inproceedings{synthetic_eggs2026,\n  author    = {Schaffelder, Max and Gatt, Albert},\n  title     = {{Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning}},\n  booktitle = {Findings of ACL},\n  year      = {2026},\n  note      = {arXiv:2511.01490},\n  url       = {https://arxiv.org/abs/2511.01490},\n}\n\n@inproceedings{shi2025_closer_look,\n  author    = {Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},\n  title     = {{A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2025},\n  note      = {Spotlight},\n}\n\n@inproceedings{yi2026_escaping_collapse,\n  author    = {Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},\n  title     = {{Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence}},\n  booktitle = {3rd DATA-FM Workshop at ICLR 2026},\n  year      = {2026},\n}\n\n% --- Model collapse: collapse-can-be-avoided / contamination ---\n\n@inproceedings{drayson2025_detection_prevents_collapse,\n  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  title     = {{Machine-generated text detection prevents language model collapse}},\n  booktitle = {Findings of EMNLP},\n  year      = {2025},\n  note      = {arXiv:2502.15654},\n  url       = {https://arxiv.org/abs/2502.15654},\n}\n\n@misc{bakshi2026_collapse_improvement,\n  author    = {Bakshi, Soham and Chakraborty, Sunrit},\n  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},\n  year      = {2026},\n  howpublished = {arXiv:2602.10531},\n  url       = {https://arxiv.org/abs/2602.10531},\n}\n\n@misc{wang2026_contamination,\n  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},\n  title     = {{Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training}},\n  year      = {2026},\n  howpublished = {arXiv:2602.16065},\n  url       = {https://arxiv.org/abs/2602.16065},\n}\n\n@misc{falahati2026_curated,\n  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},\n  title     = {{Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences}},\n  year      = {2026},\n  howpublished = {arXiv:2605.07724},\n  url       = {https://arxiv.org/abs/2605.07724},\n}\n\n% ============================================================\n% AI-Generated Text Detection\n% ============================================================\n\n@article{wu2025_detection_survey,\n  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},\n  title     = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},\n  journal   = {Computational Linguistics},\n  volume    = {51},\n  number    = {1},\n  pages     = {275--354},\n  year      = {2025},\n  publisher = {MIT Press},\n}\n\n% --- Statistical / zero-shot detectors ---\n\n@inproceedings{gehrmann2019_gltr,\n  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  title     = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  booktitle = {Proceedings of ACL: System Demonstrations},\n  year      = {2019},\n  note      = {arXiv:1906.04043},\n  url       = {https://arxiv.org/abs/1906.04043},\n}\n\n@inproceedings{mitchell2023_detectgpt,\n  author    = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  title     = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.11305},\n  url       = {https://arxiv.org/abs/2301.11305},\n}\n\n@inproceedings{fast_detectgpt2024,\n  author    = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  title     = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.05130},\n  url       = {https://arxiv.org/abs/2310.05130},\n}\n\n@inproceedings{binoculars2024,\n  author    = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  title     = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2401.12070},\n  url       = {https://arxiv.org/abs/2401.12070},\n}\n\n@article{diveye2026,\n  author    = {Basani, Advik Raj and Chen, Pin-Yu},\n  title     = {{Diversity Boosts AI-Generated Text Detection}},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2026},\n  note      = {arXiv:2509.18880},\n  url       = {https://arxiv.org/abs/2509.18880},\n}\n\n% --- Robustness / limitations of detectors ---\n\n@misc{sadasivan2023_paraphrase,\n  author    = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  title     = {{Can AI-Generated Text be Reliably Detected?}},\n  year      = {2023},\n  howpublished = {arXiv:2303.11156},\n  url       = {https://arxiv.org/abs/2303.11156},\n}\n\n@misc{pudasaini2026_detection_fails,\n  author    = {Pudasaini, Shushanta and Miralles-Pech{\\'u}an, Luis and Lillis, David and Llorens Salvador, Marisa},\n  title     = {{Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy}},\n  year      = {2026},\n  howpublished = {arXiv:2603.23146},\n  url       = {https://arxiv.org/abs/2603.23146},\n}\n\n@misc{pu2026_generator_barrier,\n  author    = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},\n  title     = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  year      = {2026},\n  howpublished = {arXiv:2604.13692},\n  url       = {https://arxiv.org/abs/2604.13692},\n}\n\n% --- Beyond binary: attribution, editing extent, benchmarks ---\n\n@inproceedings{bevendorff2025_two_paradigms,\n  author    = {Bevendorff, Janek and Wiegmann, Matti and Richter, Emmelie and Potthast, Martin and Stein, Benno},\n  title     = {{The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification}},\n  booktitle = {Findings of ACL},\n  pages     = {3762--3787},\n  year      = {2025},\n  address   = {Vienna, Austria},\n}\n\n@inproceedings{uchendu2020_attribution,\n  author    = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  title     = {{Authorship Attribution for Neural Text Generation}},\n  booktitle = {Proceedings of EMNLP},\n  year      = {2020},\n}\n\n@inproceedings{editlens2026,\n  author    = {Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit},\n  title     = {{EditLens: Quantifying the Extent of AI Editing in Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2026},\n  note      = {arXiv:2510.03154},\n  url       = {https://arxiv.org/abs/2510.03154},\n}\n\n@inproceedings{loki2025,\n  author    = {Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi and Kang, Hengrui and He, Jun and Lin, Honglin and Wang, Zihao and Wu, Tong and Wu, Zhizheng and Chen, Yiping and Lin, Dahua and He, Conghui and Li, Weijia},\n  title     = {{LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models}},\n  booktitle = {Proceedings of ICLR (Spotlight)},\n  year      = {2025},\n  note      = {arXiv:2410.09732},\n  url       = {https://arxiv.org/abs/2410.09732},\n}\n\n% --- Geometric / intrinsic dimension detectors ---\n\n@inproceedings{tulchinskii2023_intrinsic_dim,\n  author    = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Barannikov, Serguei and Piontkovskaya, Irina and Nikolenko, Sergey and Burnaev, Evgeny},\n  title     = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2306.04723},\n  url       = {https://arxiv.org/abs/2306.04723},\n}\n\n% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,\n  author    = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},\n  title     = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},\n  booktitle = {Proceedings of NAACL},\n  year      = {2024},\n  note      = {arXiv:2305.15047},\n  url       = {https://arxiv.org/abs/2305.15047},\n}\n\n@inproceedings{wang2024_m4_semeval,\n  author    = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  title     = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  booktitle = {Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)},\n  year      = {2024},\n  note      = {arXiv:2404.14183},\n  url       = {https://arxiv.org/abs/2404.14183},\n}\n\n@inproceedings{li2024_mage,\n  author    = {Li, Yongkang and Li, Donghao and Yang, Yue and Hu, Baotian and Zhang, Min},\n  title     = {{MAGE: Machine-generated Text Detection in the Wild}},\n  booktitle = {Proceedings of ACL},\n  year      = {2024},\n  note      = {arXiv:2305.13242},\n  url       = {https://arxiv.org/abs/2305.13242},\n}\n\n@inproceedings{yang2024_dnagpt,\n  author    = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  title     = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2305.17359},\n  url       = {https://arxiv.org/abs/2305.17359},\n}\n\n% --- Watermarking ---\n\n@inproceedings{kirchenbauer2023_watermark,\n  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  title     = {{A Watermark for Large Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.10226},\n  url       = {https://arxiv.org/abs/2301.10226},\n}\n\n% ============================================================\n% Decoding Strategies\n% ============================================================\n\n@inproceedings{holtzman2020_nucleus,\n  author    = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  title     = {{The Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2020},\n  note      = {arXiv:1904.09751},\n  url       = {https://arxiv.org/abs/1904.09751},\n}\n\n@inproceedings{finlayson2024_closing,\n  author    = {Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabha and Sabharwal, Ashish},\n  title     = {{Closing the Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.01693},\n  url       = {https://arxiv.org/abs/2310.01693},\n}\n\n@inproceedings{garces_arias2025_decoding_decoded,\n  author    = {{Garces Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},\n  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},\n  booktitle = {Proceedings of COLING},\n  year      = {2025},\n  note      = {arXiv:2410.06097},\n  url       = {https://arxiv.org/abs/2410.06097},\n}\n\n@article{wiher2022_decoding,\n  author    = {Wiher, Gian and Meister, Clara and Cotterell, Ryan},\n  title     = {{On Decoding Strategies for Neural Text Generators}},\n  journal   = {Transactions of the Association for Computational Linguistics},\n  volume    = {10},\n  pages     = {997--1012},\n  year      = {2022},\n}\n\n@inproceedings{basu2021_mirostat,\n  author    = {Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shirish and Varshney, Lav R.},\n  title     = {{Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2021},\n}\n\n% ============================================================\n% Ordinal Classification / Contrastive Learning\n% ============================================================\n\n@article{coral2020,\n  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  title     = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  journal   = {Pattern Recognition Letters},\n  volume    = {140},\n  pages     = {325--331},\n  year      = {2020},\n  note      = {arXiv:1901.07884},\n  url       = {https://arxiv.org/abs/1901.07884},\n}\n\n@inproceedings{cloc2025,\n  author    = {Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting},\n  title     = {{CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss}},\n  booktitle = {Proceedings of CVPR},\n  year      = {2025},\n  note      = {arXiv:2504.17813},\n  url       = {https://arxiv.org/abs/2504.17813},\n}\n\n% ============================================================\n% Foundation Models / Fine-tuning\n% ============================================================\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2022},\n  note      = {arXiv:2106.09685},\n  url       = {https://arxiv.org/abs/2106.09685},\n}\n\n@inproceedings{he2021_deberta_v3,\n  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  title     = {{DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2023},\n  note      = {arXiv:2111.09543},\n  url       = {https://arxiv.org/abs/2111.09543},\n}\n\n@misc{liu2019_roberta,\n  author    = {Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},\n  title     = {{RoBERTa: A Robustly Optimized BERT Pretraining Approach}},\n  year      = {2019},\n  howpublished = {arXiv:1907.11692},\n  url       = {https://arxiv.org/abs/1907.11692},\n}\n\n% ============================================================\n% Data Curation / Selection\n% ============================================================\n\n@inproceedings{dsir2023,\n  author    = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  title     = {{Data Selection for Language Models via Importance Resampling}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2302.03169},\n  url       = {https://arxiv.org/abs/2302.03169},\n}\n\n@inproceedings{qurating2024,\n  author    = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  title     = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.09739},\n  url       = {https://arxiv.org/abs/2402.09739},\n}\n\n@inproceedings{penedo2024_fineweb,\n  author    = {Penedo, Guilherme and Kydl{\\'\\i}{\\v{c}}ek, Hynek and Lozhkov, Anton and Mitchell, Margaret and Wolf, Thomas and von Werra, Leandro},\n  title     = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2406.17557},\n  url       = {https://arxiv.org/abs/2406.17557},\n}\n\n@article{sugiyama2007_importance_weighting,\n  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\\\"u}ller, Klaus-Robert},\n  title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},\n  journal   = {Journal of Machine Learning Research},\n  volume    = {8},\n  pages     = {985--1005},\n  year      = {2007},\n}\n\n% ============================================================\n% Large Language Models (cross-scale experiments)\n% ============================================================\n\n@misc{qwen2.5,\n  author    = {Qwen Team},\n  title     = {{Qwen2.5: A Party of Foundation Models}},\n  year      = {2025},\n  howpublished = {arXiv:2412.15115},\n  url       = {https://arxiv.org/abs/2412.15115},\n}\n\n@misc{llama3,\n  author    = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and others},\n  title     = {{The Llama 3 Herd of Models}},\n  year      = {2024},\n  howpublished = {arXiv:2407.21783},\n  url       = {https://arxiv.org/abs/2407.21783},\n}\n\n% ============================================================\n% Additional References (R5-R7 fixes)\n% ============================================================\n\n@misc{schaeffer2025,\n  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},\n  title     = {{Position: Model Collapse Does Not Mean What You Think}},\n  year      = {2025},\n  howpublished = {arXiv:2503.03150},\n  url       = {https://arxiv.org/abs/2503.03150},\n}\n\n@inproceedings{frank2001,\n  author    = {Frank, Eibe and Hall, Mark},\n  title     = {{A Simple Approach to Ordinal Classification}},\n  booktitle = {Proceedings of ECML},\n  year      = {2001},\n  pages     = {145--156},\n}\n\n@inproceedings{rennie2005,\n  author    = {Rennie, Jason D. M. and Srebro, Nathan},\n  title     = {{Loss Functions for Preference Levels: Regression with Discrete Ordered Labels}},\n  booktitle = {Proceedings of IJCAI Workshop on Advances in Preference Handling},\n  year      = {2005},\n}\n\n@article{mccullagh1980_ordinal,\n  title={{Regression Models for Ordinal Data}},\n  author={McCullagh, Peter},\n  journal={Journal of the Royal Statistical Society: Series B},\n  volume={42},\n  number={2},\n  pages={109--142},\n  year={1980}\n}\n\n@inproceedings{wenzek2020_ccnet,\n  title={{CCNet}: Extracting High Quality Monolingual Datasets from Web Crawl Data},\n  author={Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\\'a}n, Francisco and Joulin, Armand and Grave, Edouard},\n  booktitle={Proceedings of LREC},\n  year={2020}\n}\n\n@inproceedings{dugan2024_raid,\n  author    = {Dugan, Liam and Hwang, Alyssa and Trhl{\\'\\i}k, Filip and Zhu, Andrew and Ludan, Josh Magnus and Xu, Hainiu and Ippolito, Daphne and Callison-Burch, Chris},\n  title     = {{RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors}},\n  booktitle = {Proceedings of ACL},\n  pages     = {12463--12492},\n  year      = {2024},\n  note      = {arXiv:2405.07940},\n  url       = {https://arxiv.org/abs/2405.07940},\n}\n\n% ============================================================\n% Reviewer-requested citations (MR1--MR5)\n% ============================================================\n\n@inproceedings{guo2024curious,\n  author    = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo{\\'e}},\n  title     = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},\n  booktitle = {Findings of NAACL},\n  year      = {2024},\n  note      = {arXiv:2311.09807},\n  url       = {https://arxiv.org/abs/2311.09807},\n}\n\n@inproceedings{padmakumar2024diversity,\n  author    = {Padmakumar, Vishakh and He, He},\n  title     = {{Does Writing with Language Models Reduce Content Diversity?}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2309.05196},\n  url       = {https://arxiv.org/abs/2309.05196},\n}\n\n@misc{briesch2024selfconsuming,\n  author    = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},\n  title     = {{Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop}},\n  year      = {2024},\n  howpublished = {arXiv:2311.16822},\n  url       = {https://arxiv.org/abs/2311.16822},\n}\n\n@misc{seddik2024synthetic,\n  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  title     = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  year      = {2024},\n  howpublished = {arXiv:2404.05090},\n  url       = {https://arxiv.org/abs/2404.05090},\n}\n\n@inproceedings{pareek2024understanding,\n  author    = {Pareek, Divyansh and Du, Simon S. and Oh, Sewoong},\n  title     = {{Understanding the Gains from Repeated Self-Distillation}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2407.04600},\n  url       = {https://arxiv.org/abs/2407.04600},\n}\n",
      "numLines": 597,
      "startLine": 1,
      "totalLines": 597
    }
  },
  "sourceToolAssistantUUID": "e20fd060-ba29-475a-a1b6-42a5a0eb71e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-18T14:11:06.205Z_

<details><summary>↩ Tool result · `toolu_01Xrwy1A8vAgh87S9L8kTPzY`</summary>

```text
1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (68.8--85.9\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} evaluates bagging (RF) and gradient boosting (XGBoost, LightGBM) on the same 19 features; per-cell spread ($\leq$0.4pp) establishes a feature-determined ceiling.
10	On Pythia nucleus, CORAL \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match RF within 0.6\,pp ($p>0.05$); all feature-based methods outperform CE-MLP (74.9\%) and logistic regression (75.0\%).
11	Binary detectors repurposed for ordinal classification (Binoculars + Fast-DetectGPT combined: 74.2\%) fall 4\,pp below RF (Appendix~\ref{app:detector_baselines}).
12	
13	\paragraph{Surface-text ablation.}
14	Single-feature regression on mean perplexity performs at chance (25.1\%); zero-shot LLMs (DeepSeek V3.2, 36.2\%; Qwen2.5-7B-Instruct, 30.4\%) also fail (43\,pp below RF; Appendix~\ref{app:zeroshot_prompt}); depth signal therefore resides in distributional statistics inaccessible from surface text.
15	
16	\begin{table}[t]
17	\centering
18	\small
19	\caption{Classifier convergence: 4-class accuracy (\%) across three atlas cells. RF (bagging), XGBoost and LightGBM (gradient boosting) operate on the same 19 features; $\Delta_{\max}$: largest per-cell spread. Chance = 25\%. RF values differ from Table~\ref{tab:main_matrix} by $\leq$0.2pp due to matched-fold evaluation. 5-fold cross-validation standard deviation $\leq$ 0.9\,pp across all settings.}
20	\label{tab:baselines}
21	\begin{tabular}{@{}lcccc@{}}
22	\toprule
23	Cell & RF & XGB & LGBM & $\Delta_{\max}$ \\
24	\midrule
25	Pythia, nuc. & 78.8 & 79.0 & 78.9 & 0.2 \\
26	GPT-2~XL, $\tau$ & 85.8 & 86.2 & 86.2 & 0.4 \\
27	Pythia, top-$k$ & 68.9 & 68.9 & 68.7 & 0.2 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	Convergence confirms the signal resides in the features; three alternative classifiers match RF within 0.8\,pp under cross-model transfer (Appendix~\ref{app:learned_estimator}).
33	Perplexity features alone recover 66.0\% ($-$0.5\,pp vs.\ full), while repetition/diversity reach only 53.0\% ($-$13.6\,pp; Appendix~\ref{app:feature_ablation}); perplexity degradation is the dominant depth marker.
34	Raw perplexity alone performs at chance (25.1\%); the strongest single feature (\texttt{p90\_ppl}) reaches 58.3\% ($-$8.3\,pp vs.\ full); multi-dimensional characterization is required.
35	Figure~\ref{fig:confusion_matrix} shows d0 near-perfectly identified; errors concentrate at d2/d3 in-distribution and spread to d1--d3 under transfer (RF seed std $= 0.06$\,pp; Appendix~\ref{app:rf_seed}).
36	Cross-seed LoRA replication confirms signal direction and feature ranking are stable across two models; absolute accuracy varies by 1--2\,pp (Pythia $-$1.05\,pp, GPT-2~XL $+$2.04\,pp with non-overlapping CIs; Appendix~\ref{app:seed_replication}).
37	
38	\begin{figure}[t]
39	\centering
40	\includegraphics[width=\columnwidth]{figures/fig_confusion_matrix.pdf}
41	\caption{Confusion matrices for the best in-distribution setting (GPT-2 XL, temp $\tau{=}0.9$, 85.9\%) and the best cross-model leave-one-out transfer (OLMo holdout, 69.2\%). d0 recall exceeds 99\% in both; errors spread across the d1--d3 range under transfer.}
42	\label{fig:confusion_matrix}
43	\end{figure}
44	
45	\subsection{Cross-Model Transfer}
46	\label{sec:gen:crossmodel}
47	
48	We perform leave-one-model-family-out evaluation: train on two families (nucleus only), test on the held-out third (Table~\ref{tab:cross_model}).
49	
50	\begin{table}[t]
51	\centering
52	\small
53	\caption{Cross-model transfer (leave-one-out, nucleus only). Chance = 25\% / 33\% (d1--d3). d1--d3 bal.\ acc: Pythia 49.9\%, OLMo 59.2\%, GPT-2~XL 57.2\% (mean 55.4\%).}
54	\label{tab:cross_model}
55	\begin{tabular}{lccccc}
56	\toprule
57	Holdout & Acc & d0 & d1 & d2 & d3 \\
58	 & (\%) & Rec. & Rec. & Rec. & Rec. \\
59	\midrule
60	Pythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\
61	OLMo & \textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\
62	GPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\
63	\midrule
64	Mean & 66.4 & 99.3 & 66.5 & 40.9 & 59.0 \\
65	\bottomrule
66	\end{tabular}
67	\end{table}
68	
69	Mean transfer accuracy is 66.4\% (2.7$\times$ chance); d0 recall ($>$98\%) inflates the headline (d1--d3 balanced mean 55.4\%).
70	
71	\subsection{Cross-Strategy Transfer}
72	\label{sec:gen:crossstrategy}
73	
74	Table~\ref{tab:cross_strategy} reports leave-one-strategy-out transfer.
75	
76	\begin{table}[t]
77	\centering
78	\small
79	\caption{Cross-strategy transfer (leave-one-out). Chance = 25\% / 33\% (d1--d3). d0 recall $\geq$89\% inflates headline; d1--d3 mean: 45.9\%.}
80	\label{tab:cross_strategy}
81	\begin{tabular}{lccc}
82	\toprule
83	Holdout & Pythia & OLMo & GPT-2 XL \\
84	 & Acc (\%) & Acc (\%) & Acc (\%) \\
85	\midrule
86	nucleus & \textbf{69.4} & \textbf{65.4} & \textbf{59.9} \\
87	temp ($\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\
88	top-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\
89	\bottomrule
90	\end{tabular}
91	\end{table}
92	
93	Mean cross-strategy accuracy (59.1\%) falls 7pp below cross-model transfer (66.4\%); excluding d0, d1--d3 accuracy drops to 45.9\% (chance = 33\%).
94	Training on nucleus + top-$k$ inverts the d1/d2 boundary under temperature (d1v2 AUC $<$ 0.5); a two-stage pipeline (strategy identification + depth classification) recovers 11.5\,pp over naive transfer (Limitations).
95	A multi-temperature ablation (Appendix~\ref{app:multi_tau}) confirms within-$\tau$ signal for $\tau \leq 0.9$ but collapse at $\tau{=}1.1$; end-to-end PLMs lag RF by 20pp (Appendix~\ref{app:e2e}).
96	
97	\paragraph{Prompted generation.}
98	Replicating the GPT-2~XL nucleus pipeline with topic-seeded generation yields 69.5\% (95\% CI $[68.9, 70.2]$, $-$13.8\,pp vs.\ BOS-seeded, $2.8\times$ chance), with monotonic AUC decay and identical top features (Appendix~\ref{app:prompted_gen}): prompt conditioning attenuates but does not eliminate the depth signal.
99	
100	%% ----------------------------------------------------------------
101	\subsection{Preliminary Cross-Scale Observations}
102	\label{sec:gen:crossscale}
103	
104	Extending to 7--8B under QLoRA, Llama-3.1-8B Instruct \cite{llama3} achieves 70.2\% ($\mathrm{EDD}_{0.70}{=}4$) and Qwen2.5-7B \cite{qwen2.5} 60.1\% ($\mathrm{EDD}_{0.70}{>}5$).
105	A base-model control (Llama-3.1-8B, 59.9\%, non-monotonic AUC) vs.\ instruction-tuned (70.2\%, monotonic) suggests instruction tuning \emph{regularizes} recursive degradation; a 1.5B instruct control (47.4\%, $1.9\times$ chance) confirms at matched scale (Appendix~\ref{app:instruct_1p5b}; confounds in Appendix~\ref{app:cross_scale_confounds}).
106	Cross-model chains (84.75\%), cross-domain (arXiv 74.1\%), and LoRA rank sensitivity ($\Delta{=}4.65$\,pp; Appendix~\ref{app:cross_scale_full}) further confirm robustness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5aa32cd6-be09-419b-8eee-03f4938d4963",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "88e661e4-10a6-4e35-8e40-8723d30cc6a1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
      "content": "\\section{Generalization and Robustness}\n\\label{sec:generalization}\n\nWe test whether atlas accuracy (68.8--85.9\\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).\n\n\\subsection{Classifier Comparison and Surface-Text Ablation}\n\\label{sec:gen:baselines}\n\nTable~\\ref{tab:baselines} evaluates bagging (RF) and gradient boosting (XGBoost, LightGBM) on the same 19 features; per-cell spread ($\\leq$0.4pp) establishes a feature-determined ceiling.\nOn Pythia nucleus, CORAL \\cite{coral2020} (78.1\\%) and DivEye \\cite{diveye2026} (78.2\\%) match RF within 0.6\\,pp ($p>0.05$); all feature-based methods outperform CE-MLP (74.9\\%) and logistic regression (75.0\\%).\nBinary detectors repurposed for ordinal classification (Binoculars + Fast-DetectGPT combined: 74.2\\%) fall 4\\,pp below RF (Appendix~\\ref{app:detector_baselines}).\n\n\\paragraph{Surface-text ablation.}\nSingle-feature regression on mean perplexity performs at chance (25.1\\%); zero-shot LLMs (DeepSeek V3.2, 36.2\\%; Qwen2.5-7B-Instruct, 30.4\\%) also fail (43\\,pp below RF; Appendix~\\ref{app:zeroshot_prompt}); depth signal therefore resides in distributional statistics inaccessible from surface text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Classifier convergence: 4-class accuracy (\\%) across three atlas cells. RF (bagging), XGBoost and LightGBM (gradient boosting) operate on the same 19 features; $\\Delta_{\\max}$: largest per-cell spread. Chance = 25\\%. RF values differ from Table~\\ref{tab:main_matrix} by $\\leq$0.2pp due to matched-fold evaluation. 5-fold cross-validation standard deviation $\\leq$ 0.9\\,pp across all settings.}\n\\label{tab:baselines}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nCell & RF & XGB & LGBM & $\\Delta_{\\max}$ \\\\\n\\midrule\nPythia, nuc. & 78.8 & 79.0 & 78.9 & 0.2 \\\\\nGPT-2~XL, $\\tau$ & 85.8 & 86.2 & 86.2 & 0.4 \\\\\nPythia, top-$k$ & 68.9 & 68.9 & 68.7 & 0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConvergence confirms the signal resides in the features; three alternative classifiers match RF within 0.8\\,pp under cross-model transfer (Appendix~\\ref{app:learned_estimator}).\nPerplexity features alone recover 66.0\\% ($-$0.5\\,pp vs.\\ full), while repetition/diversity reach only 53.0\\% ($-$13.6\\,pp; Appendix~\\ref{app:feature_ablation}); perplexity degradation is the dominant depth marker.\nRaw perplexity alone performs at chance (25.1\\%); the strongest single feature (\\texttt{p90\\_ppl}) reaches 58.3\\% ($-$8.3\\,pp vs.\\ full); multi-dimensional characterization is required.\nFigure~\\ref{fig:confusion_matrix} shows d0 near-perfectly identified; errors concentrate at d2/d3 in-distribution and spread to d1--d3 under transfer (RF seed std $= 0.06$\\,pp; Appendix~\\ref{app:rf_seed}).\nCross-seed LoRA replication confirms signal direction and feature ranking are stable across two models; absolute accuracy varies by 1--2\\,pp (Pythia $-$1.05\\,pp, GPT-2~XL $+$2.04\\,pp with non-overlapping CIs; Appendix~\\ref{app:seed_replication}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_confusion_matrix.pdf}\n\\caption{Confusion matrices for the best in-distribution setting (GPT-2 XL, temp $\\tau{=}0.9$, 85.9\\%) and the best cross-model leave-one-out transfer (OLMo holdout, 69.2\\%). d0 recall exceeds 99\\% in both; errors spread across the d1--d3 range under transfer.}\n\\label{fig:confusion_matrix}\n\\end{figure}\n\n\\subsection{Cross-Model Transfer}\n\\label{sec:gen:crossmodel}\n\nWe perform leave-one-model-family-out evaluation: train on two families (nucleus only), test on the held-out third (Table~\\ref{tab:cross_model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model transfer (leave-one-out, nucleus only). Chance = 25\\% / 33\\% (d1--d3). d1--d3 bal.\\ acc: Pythia 49.9\\%, OLMo 59.2\\%, GPT-2~XL 57.2\\% (mean 55.4\\%).}\n\\label{tab:cross_model}\n\\begin{tabular}{lccccc}\n\\toprule\nHoldout & Acc & d0 & d1 & d2 & d3 \\\\\n & (\\%) & Rec. & Rec. & Rec. & Rec. \\\\\n\\midrule\nPythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\\\\nOLMo & \\textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\\\\nGPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\\\\n\\midrule\nMean & 66.4 & 99.3 & 66.5 & 40.9 & 59.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean transfer accuracy is 66.4\\% (2.7$\\times$ chance); d0 recall ($>$98\\%) inflates the headline (d1--d3 balanced mean 55.4\\%).\n\n\\subsection{Cross-Strategy Transfer}\n\\label{sec:gen:crossstrategy}\n\nTable~\\ref{tab:cross_strategy} reports leave-one-strategy-out transfer.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-strategy transfer (leave-one-out). Chance = 25\\% / 33\\% (d1--d3). d0 recall $\\geq$89\\% inflates headline; d1--d3 mean: 45.9\\%.}\n\\label{tab:cross_strategy}\n\\begin{tabular}{lccc}\n\\toprule\nHoldout & Pythia & OLMo & GPT-2 XL \\\\\n & Acc (\\%) & Acc (\\%) & Acc (\\%) \\\\\n\\midrule\nnucleus & \\textbf{69.4} & \\textbf{65.4} & \\textbf{59.9} \\\\\ntemp ($\\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\\\\ntop-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean cross-strategy accuracy (59.1\\%) falls 7pp below cross-model transfer (66.4\\%); excluding d0, d1--d3 accuracy drops to 45.9\\% (chance = 33\\%).\nTraining on nucleus + top-$k$ inverts the d1/d2 boundary under temperature (d1v2 AUC $<$ 0.5); a two-stage pipeline (strategy identification + depth classification) recovers 11.5\\,pp over naive transfer (Limitations).\nA multi-temperature ablation (Appendix~\\ref{app:multi_tau}) confirms within-$\\tau$ signal for $\\tau \\leq 0.9$ but collapse at $\\tau{=}1.1$; end-to-end PLMs lag RF by 20pp (Appendix~\\ref{app:e2e}).\n\n\\paragraph{Prompted generation.}\nReplicating the GPT-2~XL nucleus pipeline with topic-seeded generation yields 69.5\\% (95\\% CI $[68.9, 70.2]$, $-$13.8\\,pp vs.\\ BOS-seeded, $2.8\\times$ chance), with monotonic AUC decay and identical top features (Appendix~\\ref{app:prompted_gen}): prompt conditioning attenuates but does not eliminate the depth signal.\n\n%% ----------------------------------------------------------------\n\\subsection{Preliminary Cross-Scale Observations}\n\\label{sec:gen:crossscale}\n\nExtending to 7--8B under QLoRA, Llama-3.1-8B Instruct \\cite{llama3} achieves 70.2\\% ($\\mathrm{EDD}_{0.70}{=}4$) and Qwen2.5-7B \\cite{qwen2.5} 60.1\\% ($\\mathrm{EDD}_{0.70}{>}5$).\nA base-model control (Llama-3.1-8B, 59.9\\%, non-monotonic AUC) vs.\\ instruction-tuned (70.2\\%, monotonic) suggests instruction tuning \\emph{regularizes} recursive degradation; a 1.5B instruct control (47.4\\%, $1.9\\times$ chance) confirms at matched scale (Appendix~\\ref{app:instruct_1p5b}; confounds in Appendix~\\ref{app:cross_scale_confounds}).\nCross-model chains (84.75\\%), cross-domain (arXiv 74.1\\%), and LoRA rank sensitivity ($\\Delta{=}4.65$\\,pp; Appendix~\\ref{app:cross_scale_full}) further confirm robustness.",
      "numLines": 106,
      "startLine": 1,
      "totalLines": 106
    }
  },
  "sourceToolAssistantUUID": "5aa32cd6-be09-419b-8eee-03f4938d4963",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-18T14:11:06.667Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KKQ9Fm6HCwncrsNcxH2Rff`</summary>

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
  "parentUuid": "88e661e4-10a6-4e35-8e40-8723d30cc6a1",
  "isSidechain": false,
  "requestId": "req_011CbAAmYGEvUKzNL8bqZWne",
  "type": "assistant",
  "uuid": "c473be94-74fa-47ec-81a4-8a9d45cf75a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPHHq3gYENpMxrx56HQeua",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6519,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 31653,
      "output_tokens": 454,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6519,
          "output_tokens": 454,
          "cache_read_input_tokens": 31653,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1449
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-18T14:11:06.673Z_

<details><summary>↩ Tool result · `toolu_01KKQ9Fm6HCwncrsNcxH2Rff`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	We formalized recursive generation depth estimation as ordinal classification and showed that perplexity tail statistics achieve 69--86\% four-class accuracy ($\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\% of full performance.
5	LoRA fine-tuning loss decreases monotonically with depth for all three families, a direct empirical validation of the tail erosion predicted by \citet{dohmatob2024_tale_of_tails}; instruction tuning regularizes this compression (\S\ref{sec:gen:crossscale}).
6	The non-uniform AUC contraction across adjacent pairs (ratio 0.69--0.80) is qualitatively consistent with exponential decay but deviates quantitatively.
7	RF-filtered subsets outperform random subsampling ($p{<}0.001$; Appendix~\ref{app:curation_poc}, \ref{app:downstream}), and cross-model chains (84.75\%; Appendix~\ref{app:cross_boundary}) confirm the signal is process-level; cross-strategy transfer and depth-quality entanglement remain open challenges (Limitations; Appendix~\ref{app:extended_discussion}).
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c473be94-74fa-47ec-81a4-8a9d45cf75a5",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "b17ef028-7608-44df-8397-c799a27e8666",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nWe formalized recursive generation depth estimation as ordinal classification and showed that perplexity tail statistics achieve 69--86\\% four-class accuracy ($\\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\\% of full performance.\nLoRA fine-tuning loss decreases monotonically with depth for all three families, a direct empirical validation of the tail erosion predicted by \\citet{dohmatob2024_tale_of_tails}; instruction tuning regularizes this compression (\\S\\ref{sec:gen:crossscale}).\nThe non-uniform AUC contraction across adjacent pairs (ratio 0.69--0.80) is qualitatively consistent with exponential decay but deviates quantitatively.\nRF-filtered subsets outperform random subsampling ($p{<}0.001$; Appendix~\\ref{app:curation_poc}, \\ref{app:downstream}), and cross-model chains (84.75\\%; Appendix~\\ref{app:cross_boundary}) confirm the signal is process-level; cross-strategy transfer and depth-quality entanglement remain open challenges (Limitations; Appendix~\\ref{app:extended_discussion}).\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "c473be94-74fa-47ec-81a4-8a9d45cf75a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-18T14:11:07.312Z_

<details open><summary>🔧 Tool call — Read · `toolu_016ZrSUFMGu2pv2DkaCYTeh8`</summary>

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
  "parentUuid": "b17ef028-7608-44df-8397-c799a27e8666",
  "isSidechain": false,
  "requestId": "req_011CbAAmYGEvUKzNL8bqZWne",
  "type": "assistant",
  "uuid": "99d34d8a-5309-44fc-825e-dedd906577cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPHHq3gYENpMxrx56HQeua",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6519,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 31653,
      "output_tokens": 454,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6519,
          "output_tokens": 454,
          "cache_read_input_tokens": 31653,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1449
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-18T14:11:07.317Z_

<details><summary>↩ Tool result · `toolu_016ZrSUFMGu2pv2DkaCYTeh8`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Cross-strategy deployment constraint.}
5	Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.
6	Per-strategy z-score normalization partially corrects the inversion under logistic regression (GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$) but yields negligible improvement for the Random Forest classifier used throughout the main experiments ($\Delta < 0.02$\,pp), and even in the best case (logistic regression) leaves a residual gap relative to within-strategy performance (${\sim}0.83$); a two-stage pipeline (strategy identification + strategy-conditioned classification) is therefore needed for reliable cross-strategy deployment.
7	
8	\paragraph{Strategy-unknown deployment.}
9	In strategy-unknown settings, naive transfer on d1--d3 yields only 45.9\%, and d1/d2 predictions may invert.
10	A two-stage pipeline recovers 11.5\,pp over LOO, though per-model gains vary (GPT-2~XL $+$16.4\,pp vs.\ Pythia $+$8.0\,pp).
11	Practical deployment requires either strategy metadata or learned routing.
12	
13	\paragraph{d0 inflation of headline metrics.}
14	Depth~0 (human-written text) is near-perfectly separable (recall $>$98\% across all nine model--strategy settings), inflating headline accuracy.
15	Cross-model transfer accuracy of 66.4\% is substantially driven by d0; d2 recall drops to 26.8\% in the worst case (Pythia holdout).
16	
17	\paragraph{Controlled vs.\ ecological setting.}
18	The primary benchmark uses Wikipedia seed text with controlled LoRA fine-tuning (1--1.5B models), a design that isolates the depth variable but diverges from wild contamination where models train on mixed corpora with prior-generation outputs at unknown proportions.
19	Domain bias controls confirm depth as the dominant factor: LOGO accuracy (72.1\%) matches standard CV (72.0\%), seed-group prediction is at chance (10.2\%; Appendix~\ref{app:domain_bias}).
20	Cross-scale experiments (7--8B, \S\ref{sec:gen:crossscale}) show weaker but above-chance signal; a base-model control suggests instruction-tuning regularizes degradation.
21	Segment-level estimation in mixed-depth documents remains open (Appendix~\ref{app:mixed_depth}); in particular, partial mixing (accumulation), where a single document contains fragments from different recursive depths, is a key open question, as our framework assumes uniform depth per passage.
22	
23	\paragraph{Domain-dependent false positive rate.}
24	On editorial text (WikiText-103), all classifiers achieve $\geq$98.5\% d0 accuracy, but on web-crawl data (C4, 5{,}000 passages), per-model FPR ranges from 4.7\% (OLMo) to 22.4\% (GPT-2~XL).
25	A pooled RF classifier evaluated on larger corpora (10{,}000 passages each) yields 34\% FPR on C4 and 17\% on FineWeb \cite{penedo2024_fineweb}; the gap reflects quality filtering in FineWeb removing feature-anomalous text that triggers false positives.
26	Misclassifications concentrate in template/SEO content with elevated repetition features (\texttt{rep\_3gram} $+$37\%, \texttt{rep\_4gram} $+$75\% vs.\ correctly classified d0).
27	Deployment on heterogeneous web corpora requires model- and domain-specific calibration (Appendix~\ref{app:calibration}).
28	
29	\paragraph{Adversarial robustness.}
30	Adversarial paraphrasing \cite{sadasivan2023_paraphrase} could disrupt the perplexity tail features that drive classification; depth estimation's robustness under such attacks is untested.
31	
32	\paragraph{EDD monotonicity assumption.}
33	Our EDD definition (Eq.~\ref{eq:edd}) requires all pairwise AUCs up to depth $d^*$ to exceed $T$, which is well-behaved when AUC decays monotonically, as observed in all our configurations.
34	However, \citet{bakshi2026_collapse_improvement} show that early recursion can temporarily \emph{improve} model quality, which could produce non-monotonic AUC profiles (e.g., a dip at d1/d2 followed by recovery at d2/d3).
35	Our cross-strategy transfer results provide an empirical example: training on nucleus + top-$k$ and testing on temperature yields d1-vs-d2 AUC as low as 0.129 (GPT-2~XL) and 0.253 (OLMo), violating the monotonicity assumption.
36	In such cases EDD would conservatively report a lower value than the deepest discriminable pair, potentially underestimating the true discriminable range; extending EDD to handle non-contiguous discriminable regions is future work.
37	The choice of threshold $T$ is also application-dependent: at $T{=}0.80$, several cells lose one depth level relative to $T{=}0.75$.
38	
39	\paragraph{Reference model dependency.}
40	Reference model choice affects classification accuracy by up to 11\,pp; same-family references yield optimal performance, though all configurations exceed $2.5\times$ chance.
41	Surprisal-based features are computed relative to Pythia-1.4B, which coincides with one of the three generators.
42	For the Pythia pipeline this constitutes self-model feature extraction, while OLMo and GPT-2~XL measurements are cross-model.
43	Empirically, the self-model configuration does not yield the highest accuracy (Pythia 78.7\% vs.\ GPT-2~XL 85.9\%); the overlap therefore does not confer a systematic advantage.
44	An ablation with OLMo-1B and GPT-2 XL as alternative references shows accuracy ranging from 67--79\% across three reference architectures (Appendix~\ref{app:ref_ablation}), all exceeding $2.5\times$ chance; same-family reference yields optimal performance ($\Delta{\leq}$11\,pp).
45	The choice of reference model affects feature values; a different reference model may shift absolute feature magnitudes and potentially alter discriminability at depth boundaries.
46	Reference-free surface features alone achieve 53.7\% (partial signal in lexical statistics) but trail the full pipeline by 25pp; surprisal-based features are therefore essential.
47	Simple multi-reference ensembling does not outperform the best single reference (73.7\% vs.\ 78.6\%).
48	
49	\paragraph{Single LoRA instance.}
50	Cross-seed replication confirms signal direction and feature ranking are stable; absolute accuracy varies by 1--2\,pp across models (Pythia $-$1.05\,pp, GPT-2~XL $+$2.04\,pp).
51	The GPT-2~XL CIs do not overlap ([83.89, 84.77] vs.\ [86.17, 86.49]), indicating that LoRA seed can shift accuracy beyond sampling noise, though the direction reversal across models rules out systematic bias.
52	Top-5 feature importance is identical across seeds for both models (Appendix~\ref{app:seed_replication}).
53	
54	\paragraph{Additional caveats.}
55	Depth signal scales with passage length (68.4\% at 128 tokens, 77.8\% at 512; Appendix~\ref{app:length_ablation}), saturating near 500 tokens.
56	Detection features degrade under domain shift \cite{pudasaini2026_detection_fails}, and curated synthetic data may not trigger collapse \cite{falahati2026_curated}, attenuating the fingerprints we exploit.
57	
58	\section*{Ethics Statement}
59	
60	This work uses publicly available pretrained language models (Pythia-1.4B, OLMo-1B, GPT-2~XL) and Wikipedia text as seed data.
61	No human subjects were involved, no private or sensitive data were collected, and no new models were released.
62	Our method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-oriented research.
63	Code and data will be released upon acceptance.
64	This research used AI coding assistants for experiment implementation and writing drafts.
65	All scientific decisions, experimental design, and result interpretation were conducted by the authors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99d34d8a-5309-44fc-825e-dedd906577cc",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "9ebbef72-2665-4f7a-993f-4e2874ebc14f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex",
      "content": "\\section*{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Cross-strategy deployment constraint.}\nCross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.\nPer-strategy z-score normalization partially corrects the inversion under logistic regression (GPT-2~XL d1v2 AUC $0.24{\\to}0.56$, OLMo $0.19{\\to}0.70$) but yields negligible improvement for the Random Forest classifier used throughout the main experiments ($\\Delta < 0.02$\\,pp), and even in the best case (logistic regression) leaves a residual gap relative to within-strategy performance (${\\sim}0.83$); a two-stage pipeline (strategy identification + strategy-conditioned classification) is therefore needed for reliable cross-strategy deployment.\n\n\\paragraph{Strategy-unknown deployment.}\nIn strategy-unknown settings, naive transfer on d1--d3 yields only 45.9\\%, and d1/d2 predictions may invert.\nA two-stage pipeline recovers 11.5\\,pp over LOO, though per-model gains vary (GPT-2~XL $+$16.4\\,pp vs.\\ Pythia $+$8.0\\,pp).\nPractical deployment requires either strategy metadata or learned routing.\n\n\\paragraph{d0 inflation of headline metrics.}\nDepth~0 (human-written text) is near-perfectly separable (recall $>$98\\% across all nine model--strategy settings), inflating headline accuracy.\nCross-model transfer accuracy of 66.4\\% is substantially driven by d0; d2 recall drops to 26.8\\% in the worst case (Pythia holdout).\n\n\\paragraph{Controlled vs.\\ ecological setting.}\nThe primary benchmark uses Wikipedia seed text with controlled LoRA fine-tuning (1--1.5B models), a design that isolates the depth variable but diverges from wild contamination where models train on mixed corpora with prior-generation outputs at unknown proportions.\nDomain bias controls confirm depth as the dominant factor: LOGO accuracy (72.1\\%) matches standard CV (72.0\\%), seed-group prediction is at chance (10.2\\%; Appendix~\\ref{app:domain_bias}).\nCross-scale experiments (7--8B, \\S\\ref{sec:gen:crossscale}) show weaker but above-chance signal; a base-model control suggests instruction-tuning regularizes degradation.\nSegment-level estimation in mixed-depth documents remains open (Appendix~\\ref{app:mixed_depth}); in particular, partial mixing (accumulation), where a single document contains fragments from different recursive depths, is a key open question, as our framework assumes uniform depth per passage.\n\n\\paragraph{Domain-dependent false positive rate.}\nOn editorial text (WikiText-103), all classifiers achieve $\\geq$98.5\\% d0 accuracy, but on web-crawl data (C4, 5{,}000 passages), per-model FPR ranges from 4.7\\% (OLMo) to 22.4\\% (GPT-2~XL).\nA pooled RF classifier evaluated on larger corpora (10{,}000 passages each) yields 34\\% FPR on C4 and 17\\% on FineWeb \\cite{penedo2024_fineweb}; the gap reflects quality filtering in FineWeb removing feature-anomalous text that triggers false positives.\nMisclassifications concentrate in template/SEO content with elevated repetition features (\\texttt{rep\\_3gram} $+$37\\%, \\texttt{rep\\_4gram} $+$75\\% vs.\\ correctly classified d0).\nDeployment on heterogeneous web corpora requires model- and domain-specific calibration (Appendix~\\ref{app:calibration}).\n\n\\paragraph{Adversarial robustness.}\nAdversarial paraphrasing \\cite{sadasivan2023_paraphrase} could disrupt the perplexity tail features that drive classification; depth estimation's robustness under such attacks is untested.\n\n\\paragraph{EDD monotonicity assumption.}\nOur EDD definition (Eq.~\\ref{eq:edd}) requires all pairwise AUCs up to depth $d^*$ to exceed $T$, which is well-behaved when AUC decays monotonically, as observed in all our configurations.\nHowever, \\citet{bakshi2026_collapse_improvement} show that early recursion can temporarily \\emph{improve} model quality, which could produce non-monotonic AUC profiles (e.g., a dip at d1/d2 followed by recovery at d2/d3).\nOur cross-strategy transfer results provide an empirical example: training on nucleus + top-$k$ and testing on temperature yields d1-vs-d2 AUC as low as 0.129 (GPT-2~XL) and 0.253 (OLMo), violating the monotonicity assumption.\nIn such cases EDD would conservatively report a lower value than the deepest discriminable pair, potentially underestimating the true discriminable range; extending EDD to handle non-contiguous discriminable regions is future work.\nThe choice of threshold $T$ is also application-dependent: at $T{=}0.80$, several cells lose one depth level relative to $T{=}0.75$.\n\n\\paragraph{Reference model dependency.}\nReference model choice affects classification accuracy by up to 11\\,pp; same-family references yield optimal performance, though all configurations exceed $2.5\\times$ chance.\nSurprisal-based features are computed relative to Pythia-1.4B, which coincides with one of the three generators.\nFor the Pythia pipeline this constitutes self-model feature extraction, while OLMo and GPT-2~XL measurements are cross-model.\nEmpirically, the self-model configuration does not yield the highest accuracy (Pythia 78.7\\% vs.\\ GPT-2~XL 85.9\\%); the overlap therefore does not confer a systematic advantage.\nAn ablation with OLMo-1B and GPT-2 XL as alternative references shows accuracy ranging from 67--79\\% across three reference architectures (Appendix~\\ref{app:ref_ablation}), all exceeding $2.5\\times$ chance; same-family reference yields optimal performance ($\\Delta{\\leq}$11\\,pp).\nThe choice of reference model affects feature values; a different reference model may shift absolute feature magnitudes and potentially alter discriminability at depth boundaries.\nReference-free surface features alone achieve 53.7\\% (partial signal in lexical statistics) but trail the full pipeline by 25pp; surprisal-based features are therefore essential.\nSimple multi-reference ensembling does not outperform the best single reference (73.7\\% vs.\\ 78.6\\%).\n\n\\paragraph{Single LoRA instance.}\nCross-seed replication confirms signal direction and feature ranking are stable; absolute accuracy varies by 1--2\\,pp across models (Pythia $-$1.05\\,pp, GPT-2~XL $+$2.04\\,pp).\nThe GPT-2~XL CIs do not overlap ([83.89, 84.77] vs.\\ [86.17, 86.49]), indicating that LoRA seed can shift accuracy beyond sampling noise, though the direction reversal across models rules out systematic bias.\nTop-5 feature importance is identical across seeds for both models (Appendix~\\ref{app:seed_replication}).\n\n\\paragraph{Additional caveats.}\nDepth signal scales with passage length (68.4\\% at 128 tokens, 77.8\\% at 512; Appendix~\\ref{app:length_ablation}), saturating near 500 tokens.\nDetection features degrade under domain shift \\cite{pudasaini2026_detection_fails}, and curated synthetic data may not trigger collapse \\cite{falahati2026_curated}, attenuating the fingerprints we exploit.\n\n\\section*{Ethics Statement}\n\nThis work uses publicly available pretrained language models (Pythia-1.4B, OLMo-1B, GPT-2~XL) and Wikipedia text as seed data.\nNo human subjects were involved, no private or sensitive data were collected, and no new models were released.\nOur method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-oriented research.\nCode and data will be released upon acceptance.\nThis research used AI coding assistants for experiment implementation and writing drafts.\nAll scientific decisions, experimental design, and result interpretation were conducted by the authors.",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  },
  "sourceToolAssistantUUID": "99d34d8a-5309-44fc-825e-dedd906577cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-18T14:11:07.749Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Hzz4Rn5B4msV6CWPKmGzab`</summary>

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
  "parentUuid": "9ebbef72-2665-4f7a-993f-4e2874ebc14f",
  "isSidechain": false,
  "requestId": "req_011CbAAmYGEvUKzNL8bqZWne",
  "type": "assistant",
  "uuid": "0b1d696b-5395-47e6-8c9b-5438aed45bb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPHHq3gYENpMxrx56HQeua",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6519,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 31653,
      "output_tokens": 454,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6519,
          "output_tokens": 454,
          "cache_read_input_tokens": 31653,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1449
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-18T14:11:08.001Z_

<details><summary>↩ Tool result · `toolu_01Hzz4Rn5B4msV6CWPKmGzab`</summary>

```text
1	\section{Additional Results}
2	\label{app:additional}
3	
4	\subsection{Top-$k$ Feature Trajectories}
5	\label{app:topk_trajectories}
6	
7	Figure~\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
8	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
9	Concretely, the d0$\to$d1 drop in \texttt{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
10	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
11	
12	\subsection{Permutation Importance}
13	\label{app:permutation}
14	
15	To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
16	The top-2 features are stable across measures: \texttt{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \texttt{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \texttt{p75\_ppl} displaces \texttt{var\_surprisal} to rank 3).
17	Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
18	Pairwise Spearman correlations are: SHAP--Gini $\rho{=}0.93$, SHAP--permutation $\rho{=}0.84$, Gini--permutation $\rho{=}0.76$.
19	Per-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical; the top features are therefore robust to the choice of importance measure at the aggregate level, though per-cell rankings exhibit model-dependent variation.
20	
21	\subsection{Per-Class Recall}
22	\label{app:per_class}
23	
24	Table~\ref{tab:per_class_recall} reports per-class recall across all 9 atlas cells (4-class in-distribution, 5-fold CV).
25	Depth~0 recall exceeds 98\% uniformly.
26	Among generated depths, d2 is the hardest class in every cell; the deficit is most pronounced under top-$k$ sampling (46--53\%), where vocabulary truncation removes the tail tokens that carry depth-discriminative signal.
27	
28	\begin{table}[h]
29	\centering
30	\small
31	\caption{Per-class recall (\%) for all 9 atlas cells. d2 is the lowest-recall class in every cell. Boldface marks the highest d2 recall.}
32	\label{tab:per_class_recall}
33	\begin{tabular}{@{}lcccc@{}}
34	\toprule
35	Cell & d0 & d1 & d2 & d3 \\
36	\midrule
37	Pythia, nuc.       & 99.7 & 81.9 & 58.7 & 72.3 \\
38	Pythia, $\tau$     & 99.7 & 81.3 & 53.9 & 72.1 \\
39	Pythia, top-$k$    & 99.5 & 72.3 & 45.6 & 57.5 \\
40	OLMo, nuc.         & 98.8 & 80.5 & 61.5 & 74.3 \\
41	OLMo, $\tau$       & 99.7 & 87.7 & 66.1 & 77.2 \\
42	OLMo, top-$k$      & 99.5 & 78.5 & 51.2 & 65.6 \\
43	GPT-2~XL, nuc.     & 99.2 & 85.9 & \textbf{73.3} & 77.5 \\
44	GPT-2~XL, $\tau$   & 99.5 & 90.9 & 68.8 & 81.9 \\
45	GPT-2~XL, top-$k$  & 98.5 & 79.5 & 52.5 & 71.1 \\
46	\bottomrule
47	\end{tabular}
48	\end{table}
49	
50	\subsection{DCOL Iteration Details}
51	\label{app:dcol_iterations}
52	
53	Table~\ref{tab:dcol_iterations} summarizes all six DCOL iterations.
54	DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.
55	
56	\begin{table}[h]
57	\centering
58	\small
59	\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.7\%.}
60	\label{tab:dcol_iterations}
61	\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}
62	\toprule
63	Ver. & Backbone & Config & Outcome \\
64	\midrule
65	v1 & DeBERTa & FT, m\_lr $10^{-3}$ & Embed.\ collapse (31.5\%) \\
66	v2 & DeBERTa & FT, m\_lr $10^{-4}$ & OOM \\
67	v3 & DeBERTa & FT, m\_lr $10^{-4}$ & Forgetting + OOM \\
68	v4 & DeBERTa & LoRA, m\_lr $10^{-3}$ & Embed.\ collapse \\
69	v5 & DeBERTa & LoRA, m\_lr $10^{-4}$ & NaN gradients \\
70	v6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\% ($-$13.7pp) \\
71	\bottomrule
72	\end{tabular}
73	\end{table}
74	
75	\subsection{Zero-Shot LLM Prompt Template}
76	\label{app:zeroshot_prompt}
77	
78	Both DeepSeek V3.2 and Qwen2.5-7B-Instruct use identical prompting.
79	The system message defines recursive generation depth with per-depth descriptions (depth~0: human-written; depth~1--3: successive LLM generation cycles) and lists expected textual patterns at each depth (vocabulary richness, repetition, coherence).
80	The user message presents the passage (truncated to ${\approx}$384 words) and requests a JSON response containing an integer depth prediction (0--3), a confidence score, and a one-sentence reasoning.
81	No in-context examples are provided.
82	
83	\begin{quote}
84	\small
85	\textbf{System:} ``You are an expert at detecting AI-generated text and estimating its generation depth. `Recursive generation depth' refers to how many times a text has been through an LLM generation cycle: Depth~0: Original human-written text [\ldots] Depth~3: Text generated by an LLM given depth-2 text as input. Key patterns by depth: Depth~0 (human): Rich vocabulary [\ldots] Depth~3 (third-gen): Noticeable repetition, formulaic structure [\ldots]''
86	
87	\textbf{User:} ``Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3). TEXT: \{text\}. Respond with ONLY a JSON object: \{\texttt{"depth"}: $\langle$int 0--3$\rangle$, \texttt{"confidence"}: $\langle$float 0--1$\rangle$, \texttt{"reasoning"}: $\langle$str$\rangle$\}''
88	\end{quote}
89	
90	\subsection{Temperature Robustness}
91	\label{app:multi_tau}
92	
93	The cross-strategy results in \S\ref{sec:gen:crossstrategy} use a single temperature ($\tau{=}0.9$).
94	To test whether depth signal generalizes across temperatures, we repeat the classification pipeline at $\tau \in \{0.5, 0.7, 0.9, 1.1\}$ on Pythia-1.4B.
95	
96	\paragraph{Within-$\tau$ robustness.}
97	For $\tau \in [0.5, 0.9]$, d1-vs-d2 AUC exceeds 0.80 (peak 0.851 at $\tau{=}0.7$, comparable to nucleus $p{=}0.95$'s 0.861) and 4-class accuracy ranges from 75.4\% to 77.3\% (Table~\ref{tab:multi_tau_within}); the depth signal is therefore not an artifact of a single temperature.
98	The same top-5 features (\texttt{var\_surprisal}, \texttt{p90\_ppl}, \texttt{mean\_ppl}, \texttt{mean\_surprisal}, \texttt{p75\_ppl}) dominate across all $\tau$ values with only minor rank-order variation.
99	
100	\paragraph{Collapse at $\tau{=}1.1$: memorization as prerequisite.}
101	At $\tau{=}1.1$, 4-class accuracy drops to 57.2\% and d1v2 AUC falls to 0.528.
102	Training loss reveals the mechanism: at low temperature ($\tau{=}0.5$), fine-tuning loss decreases steeply across recursive depths ($2.27 \to 0.42 \to 0.16$), a sign of rapid memorization of the model's own output.
103	At $\tau{=}1.1$, loss remains nearly flat ($2.27 \to 1.91 \to 1.85$); high-entropy output resists memorization, so depth-dependent distributional shifts do not accumulate.
104	This establishes \emph{memorization as a prerequisite} for detectable depth signal: recursive depth is discriminable only when successive fine-tuning iterations progressively reshape the output distribution.
105	
106	\paragraph{Cross-$\tau$ non-transferability.}
107	Leave-one-$\tau$-out transfer yields mean accuracy of 46.7\% with mean d1v2 AUC of 0.319 (Table~\ref{tab:multi_tau_cross}), worse than cross-strategy transfer (59.1\%; \S\ref{sec:gen:crossstrategy}).
108	Holdout $\tau{=}0.5$ produces inverted d1v2 AUC (0.176); different temperatures therefore produce surprisal distributions with incompatible shapes.
109	This extends the strategy-specificity finding: even within a single decoding family, the feature space is temperature-specific; strategy-conditioned classifiers are therefore necessary.
110	
111	\paragraph{Ecological validity.}
112	On WikiText-103 (546 editorial passages), all three model-specific RF classifiers achieve $\geq$98.5\% d0 accuracy despite $+$621\% domain shift in mean perplexity, partly an easy case, as WikiText's higher perplexity places it farther from d1--d3 in feature space.
113	On noisier web-crawl data (5{,}000 C4 passages), FPR ranges from 4.7\% (OLMo) to 22.4\% (GPT-2~XL), concentrated in template/SEO content with high n-gram repetition (Table~\ref{tab:calibration}); deployment on heterogeneous web data requires model-specific calibration.
114	
115	\begin{table}[h]
116	\centering
117	\small
118	\caption{Within-$\tau$ 4-class classification (Pythia-1.4B, 5-fold CV). d$i$v$j$: pairwise AUC for depth $i$ vs.\ depth $j$.}
119	\label{tab:multi_tau_within}
120	\begin{tabular}{@{}lcccc@{}}
121	\toprule
122	$\tau$ & 4-class acc (\%) & d1v2 AUC & d0v1 AUC & d2v3 AUC \\
123	\midrule
124	0.5 & 77.3 & 0.842 & 0.996 & 0.764 \\
125	0.7 & 75.4 & 0.851 & 0.997 & 0.720 \\
126	0.9 & 75.9 & 0.808 & 0.991 & 0.781 \\
127	1.1 & 57.2 & 0.528 & 0.988 & 0.599 \\
128	\bottomrule
129	\end{tabular}
130	\end{table}
131	
132	\begin{table}[h]
133	\centering
134	\small
135	\caption{Cross-$\tau$ leave-one-out transfer (Pythia-1.4B). Train on three temperatures, test on the held-out one.}
136	\label{tab:multi_tau_cross}
137	\begin{tabular}{@{}lcc@{}}
138	\toprule
139	Holdout & Acc (\%) & d1v2 AUC \\
140	\midrule
141	$\tau{=}0.5$ & 52.2 & 0.176 \\
142	$\tau{=}0.7$ & 41.0 & 0.299 \\
143	$\tau{=}0.9$ & 46.4 & 0.277 \\
144	$\tau{=}1.1$ & 47.1 & 0.525 \\
145	\midrule
146	Mean & 46.7 & 0.319 \\
147	\bottomrule
148	\end{tabular}
149	\end{table}
150	
151	\subsection{Feature Overlap Analysis}
152	\label{app:feature_overlap}
153	
154	We probe whether end-to-end PLM representations capture the same depth signals as our statistical features via linear probing of [CLS] representations from DeBERTa-v3-base and RoBERTa-base.
155	PLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics; \texttt{var\_surprisal} and \texttt{p90\_ppl} yield negative $R^2$ under linear probing; these features are not linearly accessible in the pretrained representation space.
156	This confirms that the 20pp accuracy gap between feature-based and end-to-end methods (\S\ref{app:e2e}) stems from complementary, not redundant, representations: PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties that constitute the dominant depth markers.
157	
158	\subsection{End-to-End Learning}
159	\label{app:e2e}
160	
161	DeBERTa-v3-base \cite{he2021_deberta_v3} and RoBERTa-base \cite{liu2019_roberta} finetuned end-to-end achieve 58.3\% ($\pm$4.7\%) and 59.5\% ($\pm$3.2\%) respectively, lagging the RF baseline (78.7\%) by 20.4pp and 19.2pp.
162	The 1.2pp inter-backbone gap rules out architecture bias; Table~\ref{tab:e2e_detail} shows both backbones share the same failure mode (high d0 F1, $>$0.94, but collapsed d1/d2 performance, F1 $\leq$ 0.42), while RF achieves 0.596 d2 recall, a $>$2$\times$ advantage at the hardest depth class.
163	
164	\begin{table}[h]
165	\centering
166	\small
167	\caption{Per-class performance for end-to-end PLM classifiers vs.\ RF baseline (Pythia-1.4B nucleus). PLM columns report F1; RF d2 column reports recall (the class with the largest PLM--RF gap). Both PLM backbones share the same failure pattern: collapsed d1/d2 scores despite adequate d0/d3.}
168	\label{tab:e2e_detail}
169	\begin{tabular}{@{}lccccc@{}}
170	\toprule
171	Method & Acc (\%) & d0 & d1 & d2 & d3 \\
172	\midrule
173	DeBERTa-v3 & 58.3\,$\pm$\,4.7 & .947 & .378 & .247 & .656 \\
174	RoBERTa-base & 59.5\,$\pm$\,3.2 & .958 & .416 & .261 & .647 \\
175	\midrule
176	RF (19 feat.) & 78.7 & --- & --- & .596$^\dagger$ & --- \\
177	\bottomrule
178	\multicolumn{6}{@{}l}{\footnotesize $^\dagger$Recall; shown for the depth class with the largest PLM--RF gap.}
179	\end{tabular}
180	\end{table}
181	
182	\paragraph{Feature space divergence.}
183	SHAP TreeExplainer analysis confirms that perplexity and surprisal features account for 88.8\% of RF's total contribution.
184	Three independent importance measures (SHAP, Gini, and permutation) show strong concordance (Kendall's $W{=}0.90$, $p{<}0.005$; pairwise Spearman $\rho$: SHAP--Gini $0.93$, SHAP--permutation $0.84$; \S\ref{app:permutation}), with \texttt{p90\_ppl} appearing in the SHAP top-2 in 9/9 cells and \texttt{var\_surprisal} in 8/9.
185	Linear probing of PLM [CLS] representations yields negative $R^2$ for both \texttt{var\_surprisal} and \texttt{p90\_ppl} (\S\ref{app:feature_overlap}); pretrained representations lack the linear structure needed to recover perplexity tail statistics, a systematic representational gap rather than a backbone-specific artifact.
186	
187	DCOL \cite{cloc2025} reached 64.5\% (\S\ref{app:dcol_iterations}); all end-to-end approaches (58--65\%) underperform feature-based methods; depth estimation therefore benefits from targeted statistical features that capture distributional tail properties absent from PLM representations.
188	This comparison is bounded by backbone scale ($\leq$125M parameters); whether larger PLMs (e.g., 7B+) can close the gap via richer internal representations remains an open question.
189	
190	\subsection{Domain Bias Analysis}
191	\label{app:domain_bias}
192	
193	To assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.
194	
195	\paragraph{Methodological note.}
196	An initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\%, seed-group prediction 20.8\%).
197	We discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.
198	The results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.
199	
200	\paragraph{Sub-A: Standard CV.}
201	Five-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\% to 82\% across the 9 atlas cells (up to 2.5$\times$ above the 33.3\% chance level); depth signal is therefore the dominant classification factor.
202	
203	\paragraph{Sub-B: LOGO evaluation.}
204	We assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.
205	LOGO mean accuracy is 72.1\% (range 59.5--81.6\%), matching standard CV (72.0\%) within noise (before fix: 64.0\%, reflecting the depth--group confound).
206	Per-cell fold standard deviations range from 0.4pp to 1.4pp; cross-group generalization is therefore as reliable as within-group classification.
207	
208	\paragraph{Sub-C: Negative control.}
209	We train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\%).
210	Depth prediction accuracy averages 72.0\%; seed-group prediction averages 10.2\%, indistinguishable from chance (before fix: 20.8\%, inflated by the depth--group confound).
211	The depth-to-seed-group accuracy ratio is 7.1$\times$; the feature representation therefore encodes depth but not seed-article identity.
212	
213	Taken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.
214	
215	\subsection{Wild-Data Calibration}
216	\label{app:calibration}
217	
218	Table~\ref{tab:calibration} reports d0 accuracy and false positive rate (FPR) for all three model-specific nucleus RF classifiers on two out-of-distribution human-text corpora: WikiText-103 (546 editorial passages) and C4 (5{,}000 web-crawl passages, crawled 2019--2020; pre-LLM deployment).
219	
220	\begin{table}[h]
221	\centering
222	\small
223	\caption{Wild-data d0 accuracy and FPR for nucleus RF classifiers. All passages are human-written (true d0). FPR = fraction misclassified as d1+. 95\% Wilson CIs computed for C4 ($n{=}5{,}000$).}
224	\label{tab:calibration}
225	\begin{tabular}{@{}llrccc@{}}
226	\toprule
227	Model & Source & $n$ & d0 (\%) & FPR (\%) & 95\% Wilson CI \\
228	\midrule
229	Pythia-1.4B & WikiText & 546 & 100.0 & 0.0 & --- \\
230	 & C4 & 5{,}000 & 79.8 & 20.2 & [19.1, 21.3] \\
231	\addlinespace
232	GPT-2~XL & WikiText & 546 & 99.3 & 0.7 & --- \\
233	 & C4 & 5{,}000 & 77.6 & 22.4 & [21.3, 23.6] \\
234	\addlinespace
235	OLMo-1B & WikiText & 546 & 98.5 & 1.5 & --- \\
236	 & C4 & 5{,}000 & 95.3 & 4.7 & [4.2, 5.3] \\
237	\bottomrule
238	\end{tabular}
239	\end{table}
240	
241	On WikiText-103, all three classifiers achieve $\geq$98.5\% d0 accuracy; editorial text is therefore reliably distinguished from recursive generations across model families.
242	On C4, FPR varies sharply: OLMo (4.7\%) vs.\ Pythia (20.2\%) and GPT-2~XL (22.4\%).
243	C4 misclassifications concentrate in template and SEO content with elevated repetition features (\texttt{rep\_3gram} $+$37\%, \texttt{rep\_4gram} $+$75\% vs.\ correctly classified d0 passages), rather than in random noise.
244	The model gap likely reflects training data composition: OLMo (trained on Dolma, which includes diverse web data) produces d0 features more tolerant of web-crawl variation, while Pythia and GPT-2~XL (trained primarily on Wikipedia/WebText) map template-heavy content into the d1+ region.
245	Among C4 false positives for GPT-2~XL, predictions distribute as d1 (9.0\%), d2 (3.7\%), d3 (9.6\%); for OLMo, d1 (2.9\%), d2 (0.5\%), d3 (1.3\%). The non-uniform depth distribution suggests the classifier maps specific repetition patterns to particular depth signatures rather than producing random misclassifications.
246	
247	\subsection{Downstream Curation PoC}
248	\label{app:curation_poc}
249	
250	To validate that depth estimation translates to actionable data curation, we conduct a proof-of-concept downstream evaluation.
251	We fine-tune Pythia-410M with LoRA ($r{=}16$, $\alpha{=}32$) for 3 epochs on 8 data conditions derived from the Pythia nucleus depth-estimation corpus, repeating each condition over 5 random seeds.
252	Conditions vary the selection mechanism (RF-predicted depth, oracle depth, random subsampling) and stringency (strict $\approx$25\%, moderate $\approx$50\%, soft threshold).
253	Table~\ref{tab:curation_poc} reports per-condition perplexity; Table~\ref{tab:curation_comparisons} reports pairwise contrasts.
254	
255	\begin{table}[h]
256	\centering
257	\small
258	\caption{Curation PoC: per-condition perplexity (Pythia-410M LoRA, 5 seeds). $\Delta$ is signed so that positive values indicate lower (better) perplexity than unfiltered. $^*$\,: $p<0.05$ (paired $t$-test vs.\ unfiltered).}
259	\label{tab:curation_poc}
260	\resizebox{\columnwidth}{!}{%
261	\begin{tabular}{@{}lcccccc@{}}
262	\toprule
263	Condition & Mean PPL & Std & $n$ & $\Delta$ vs Unfilt. & $p$ & $d_z$ \\
264	\midrule
265	unfiltered        & 15.776 & 0.066 & 10{,}000 & ---      & ---   & ---      \\
266	rf\_soft          & 15.733 & 0.038 &  4{,}422 & +0.043   & 0.407 &  0.41    \\
267	rf\_moderate      & 15.756 & 0.056 &  4{,}940 & +0.021   & 0.492 &  0.34    \\
268	rf\_strict        & 15.810 & 0.061 &  2{,}496 & $-$0.034 & 0.607 & $-$0.25  \\
269	oracle\_moderate  & 15.809 & 0.103 &  5{,}000 & $-$0.033 & 0.485 & $-$0.34  \\
270	oracle\_strict    & 15.879 & 0.128 &  2{,}500 & $-$0.103 & 0.216 & $-$0.66  \\
271	random\_soft      & 16.062 & 0.079 &  4{,}422 & $-$0.286 & ${<}$0.001$^*$ & $-$2.77  \\
272	random\_moderate  & 15.998 & 0.090 &  4{,}940 & $-$0.222 & 0.028$^*$ & $-$1.50  \\
273	random\_strict    & 16.239 & 0.165 &  2{,}496 & $-$0.463 & 0.013$^*$ & $-$1.89  \\
274	\bottomrule
275	\end{tabular}}
276	\end{table}
277	
278	\begin{table}[h]
279	\centering
280	\small
281	\caption{Pairwise comparisons (paired $t$-test, 5 seeds). $^*$\,: $p<0.05$; $^{**}$\,: $p<0.01$.}
282	\label{tab:curation_comparisons}
283	\begin{tabular}{@{}lccc@{}}
284	\toprule
285	Comparison & $\Delta$ PPL & $t$ & $p$ \\
286	\midrule
287	rf\_strict vs random\_strict     & 0.429 & $-$7.05 & 0.002$^{**}$ \\
288	rf\_moderate vs random\_moderate & 0.242 & $-$3.77 & 0.020$^*$    \\
289	rf\_soft vs random\_soft         & 0.328 & $-$17.98 & ${<}$0.001$^{**}$ \\
290	rf\_soft vs unfiltered           & 0.043 &    0.93 & 0.407        \\
291	\bottomrule
292	\end{tabular}
293	\end{table}
294	
295	\subsection{Reference Model Ablation}
296	\label{app:ref_ablation}
297	
298	\begin{table}[h]
299	\centering
300	\caption{Reference model ablation. Classification accuracy (5-fold CV) on Pythia-1.4B generated text (nucleus, d0--d3) using different reference models for feature extraction.}
301	\label{tab:ref_ablation}
302	\begin{tabular}{lcc}
303	\toprule
304	Reference Model & Architecture & Accuracy (\%) \\
305	\midrule
306	Pythia-1.4B (self) & GPT-NeoX & 78.6 $\pm$ 0.6 \\
307	OLMo-1B (cross) & OLMo & 74.5 $\pm$ 0.7 \\
308	GPT-2~XL (cross) & GPT-2 & 67.3 $\pm$ 0.7 \\
309	\bottomrule
310	\end{tabular}
311	\end{table}
312	
313	\subsection{Cross-Scale Full Results}
314	\label{app:cross_scale_full}
315	
316	This section provides the full cross-scale analysis summarized in \S\ref{sec:gen:crossscale}.
317	We extend the benchmark to two 7--8B models: Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct, both under 4-bit NF4 QLoRA fine-tuning, generating depths $d \in \{0, 1, \ldots, 5\}$ with nucleus sampling ($p{=}0.95$, 500 samples per depth).
318	Feature extraction uses the same reference model (Pythia-1.4B) and 19-feature pipeline as all prior experiments.
319	
320	\paragraph{Scale comparison.}
321	Table~\ref{tab:cross_scale} contrasts the two 7--8B models with the three 1--1.5B models on matched evaluation (nucleus sampling, depths 0--3).
322	
323	\begin{table}[h]
324	\centering
325	\small
326	\caption{Cross-scale comparison: 4-class RF accuracy (\%, depths 0--3, nucleus), $\mathrm{EDD}_{T{=}0.70}$ (depths 0--5), and d0-vs-d1 AUC. CI: 95\% bootstrap. Chance = 25\%.}
327	\label{tab:cross_scale}
328	\begin{tabular}{@{}lccc@{}}
329	\toprule
330	Model & 4-class acc & $\mathrm{EDD}_{T{=}0.70}$ & d0v1 AUC \\
331	\midrule
332	GPT-2~XL (1.5B) & 84.1 & 4 & 0.999 \\
333	OLMo-1B & 78.9 & 4 & 0.997 \\
334	Pythia-1.4B & 78.7 & 4 & 0.998 \\
335	\midrule
336	Llama-3.1-8B & 70.2\,[68.3, 72.4] & 4 & 0.949 \\
337	Qwen2.5-7B & 60.1\,[58.0, 62.1] & ${>}5$ & 0.969 \\
338	\bottomrule
339	\end{tabular}
340	\end{table}
341	
342	\paragraph{(1) Depth signal persists at 7--8B scale.}
343	Both 7--8B models substantially exceed the 25\% chance baseline: Llama-3.1-8B achieves 70.2\% (95\% CI $[68.3, 72.4]$) and Qwen2.5-7B achieves 60.1\% ($[58.0, 62.1]$); recursive depth therefore remains estimable from perplexity-based features even when the generator is 5--7$\times$ larger than the reference model.
344	Depth-0 separability is preserved in both models: d0v1 AUC is 0.949 (Llama-3.1) and 0.969 (Qwen2.5).
345	
346	\paragraph{(2) EDD at 7--8B scale.}
347	At threshold $T{=}0.70$, Qwen2.5-7B maintains all consecutive-pair AUCs above 0.70 through depth~5 (Table~\ref{tab:cross_scale_auc}), yielding $\mathrm{EDD}_{T{=}0.70} > 5$, exceeding the $\mathrm{EDD}{=}4$ observed at 1--1.5B.
348	Llama-3.1-8B matches the smaller models at $\mathrm{EDD}{=}4$: its monotonic decay causes d4v5 (0.618) to drop below $T$, despite stronger signal at shallower depths.
349	Both larger generators produce weaker per-step signal than the 1--1.5B models (mean consecutive AUC: 0.786 for Llama-3.1, 0.782 for Qwen2.5, vs.\ 0.852 at 1--1.5B).
350	
351	\begin{table}[h]
352	\centering
353	\small
354	\caption{Consecutive binary AUC for 7--8B models (nucleus $p{=}0.95$). Llama-3.1-8B exhibits monotonic decay (d4v5 drops below $T{=}0.70$); Qwen2.5-7B shows a non-monotonic (U-shaped) pattern with all pairs above $T$.}
355	\label{tab:cross_scale_auc}
356	\begin{tabular}{@{}lccccc@{}}
357	\toprule
358	Model & d0v1 & d1v2 & d2v3 & d3v4 & d4v5 \\
359	\midrule
360	Llama-3.1-8B & 0.949 & 0.877 & 0.771 & 0.716 & 0.618 \\
361	Qwen2.5-7B & 0.969 & 0.729 & 0.709 & 0.732 & 0.772 \\
362	\bottomrule
363	\end{tabular}
364	\end{table}
365	
366	\paragraph{(3) Divergent AUC trajectories and instruction-tuning effect.}
367	Among instruction-tuned models, Llama-3.1-8B exhibits monotonic AUC decay consistent with the 1--1.5B pattern, while Qwen2.5-7B shows a U-shaped recovery beyond d2v3 (Table~\ref{tab:cross_scale_auc}).
368	A base-model control (Llama-3.1-8B without instruction tuning) clarifies the causal direction: the base model achieves 59.9\% four-class accuracy (95\% CI [57.8, 62.15], $\mathrm{EDD}_{0.70}{=}2$) with non-monotonic AUC decay (Table~\ref{tab:llama3_base_auc}), while the instruction-tuned variant reaches 70.2\% with strictly monotonic decay.
369	The base-model control experiment suggests instruction-tuning regularizes rather than confounds the depth signal.
370	
371	\begin{table}[h]
372	\centering
373	\small
374	\caption{Pairwise AUC: Llama-3.1-8B Base vs.\ Instruct.}
375	\label{tab:llama3_base_auc}
376	\begin{tabular}{lccccc}
377	\toprule
378	Variant & $d_{0\text{v}1}$ & $d_{1\text{v}2}$ & $d_{2\text{v}3}$ & $d_{3\text{v}4}$ & $d_{4\text{v}5}$ \\
379	\midrule
380	Base & 0.918 & 0.794 & 0.682 & 0.730 & 0.595 \\
381	Instruct & 0.965 & 0.874 & 0.771 & 0.716 & 0.618 \\
382	\bottomrule
383	\end{tabular}
384	\end{table}
385	
386	The base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries; depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.
387	
388	\paragraph{Caveats.}
389	For Qwen2.5-7B, the CI lower bound (58.0\%) does not exclude sub-60\% accuracy; Llama-3.1-8B's lower bound (68.3\%) is more comfortably above chance but still below the 75--83\% range at 1--1.5B.
390	The divergent AUC trajectories across two models caution against strong generalizations from only two 7--8B data points: both the monotonic (Llama-3.1) and non-monotonic (Qwen2.5) patterns are single observations, and further architectures are needed to establish which is the dominant regime at this scale.
391	
392	\paragraph{Confounds.}
393	\label{app:cross_scale_confounds}
394	Four confounds limit these results: (1)~4-bit NF4 QLoRA quantization (absent at 1--1.5B) may distort the perplexity distribution independently of depth; (2)~smaller sample size (500 vs.\ 5{,}000 per depth) widens confidence intervals; (3)~evaluation is limited to nucleus sampling, leaving other strategies untested at this scale; (4)~vocabulary mismatch between 7--8B generators and the 1.4B reference model.
395	The base-model control partially addresses a former confound (instruction-tuning): since the base variant shows weaker signal with non-monotonic decay while the instruction-tuned variant shows stronger monotonic signal, instruction-tuning regularizes rather than confounds depth estimation.
396	The remaining confounds are not mutually independent (quantization and vocabulary mismatch both affect the perplexity distribution); it is therefore infeasible to attribute the observed accuracy gap (60--70\% vs.\ 78--85\% at 1--1.5B) to any single factor.
397	
398	\subsection{Cross-Boundary Generalization}
399	\label{app:cross_boundary}
400	
401	The preceding experiments assume a single model family generates all recursive depths.
402	In practice, recursive contamination may traverse model boundaries: text generated by model~A is used to train model~B, whose output trains model~C.
403	We probe whether the depth signal persists under two relaxations of the single-model assumption.
404	
405	\paragraph{Cross-model recursive chains.}
406	We construct a heterogeneous chain: human text (d0) $\to$ Pythia-1.4B generates d1 $\to$ OLMo-1B finetuned on Pythia-d1 generates d2 $\to$ GPT-2~XL finetuned on OLMo-d2 generates d3.
407	Each recursive step uses a \emph{different} model family, eliminating the possibility that depth signal arises from a single model's idiosyncratic behavior.
408	A 4-class Random Forest achieves 84.75\% accuracy (95\% CI $[81.0, 88.25]$), with per-depth F1 scores of 0.98 (d0), 0.88 (d1), 0.76 (d2), and 0.76 (d3).
409	Pairwise AUC remains high: d0-vs-d1 = 0.999 and d2-vs-d3 = 0.841.
410	These results suggest that distributional artifacts of recursive generation persist across model boundaries. This constitutes preliminary evidence for a process-level depth signal rather than individual generator artifacts.
411	
412	\paragraph{Confound discussion.}
413	The heterogeneous chain confounds architecture identity with depth (d1=Pythia, d2=OLMo, d3=GPT-2~XL).
414	However, if the classifier exploited architecture fingerprints rather than depth signal, near-perfect accuracy would be expected since architecture perfectly determines depth label.
415	The observed 84.75\% with monotonically decreasing per-depth F1 (d0=0.98, d1=0.88, d2=0.76, d3=0.76) is more consistent with a depth-signal interpretation, as architecture fingerprinting would not produce this graded pattern.
416	We address this confound directly with a reverse-chain control below.
417	
418	\paragraph{Reverse-chain control.}
419	To empirically test the architecture confound hypothesis, we constructed a reverse chain (GPT-2~XL $\to$ OLMo $\to$ Pythia) reversing the model-depth assignment.
420	The reverse chain achieves 85.75\% (95\% CI [82.0, 89.25]), statistically indistinguishable from the forward chain (84.75\%, [81.0, 88.25]).
421	If the classifier exploited architecture fingerprints rather than depth signal, reversing the chain should invert depth predictions; the equivalent accuracy under both orderings provides empirical evidence against the architecture confound.
422	
423	\paragraph{Cross-domain transfer.}
424	All prior experiments use WikiText-103 as the seed corpus.
425	To test domain dependence, we repeat the pipeline with arXiv abstracts as the seed text (Pythia-1.4B, nucleus $p{=}0.95$, 500 samples per depth, d0--d3).
426	Five-fold cross-validation yields 74.1\% $\pm$ 2.0\% accuracy, compared to ${\sim}$78\% on the WikiText seed.
427	Per-depth F1 shows the familiar pattern: d0 = 1.00, d1 = 0.78, d2 = 0.52, d3 = 0.66, with d2 remaining the most challenging class.
428	The 4pp accuracy gap relative to WikiText likely reflects the narrower stylistic range of scientific abstracts, which may reduce the distributional contrast between adjacent depths.
429	These results provide preliminary evidence that the perplexity-based features capture properties of the recursive generation process rather than domain-specific artifacts of the seed corpus.
430	
431	\subsection{Cross-Seed Replication}
432	\label{app:seed_replication}
433	
434	Table~\ref{tab:seed_replication} reports within-seed accuracy for Pythia-1.4B and GPT-2~XL (nucleus, depths 0--3) under two independent LoRA training seeds.
435	
436	\begin{table}[h]
437	\centering
438	\small
439	\caption{Cross-seed replication (nucleus $p{=}0.95$, d0--d3). seed=42 is the primary benchmark; seed=43 is an independent replication.}
440	\label{tab:seed_replication}
441	\begin{tabular}{@{}llccc@{}}
442	\toprule
443	Model & Seed & Acc (\%) & 95\% CI & $\Delta$ (pp) \\
444	\midrule
445	Pythia-1.4B & 42 & 78.20 & --- & --- \\
446	Pythia-1.4B & 43 & 77.15 & [76.4, 78.15] & $-$1.05 \\
447	\midrule
448	GPT-2~XL & 42 & 84.28 & [83.89, 84.77] & --- \\
449	GPT-2~XL & 43 & 86.32 & [86.17, 86.49] & $+$2.04 \\
450	\bottomrule
451	\end{tabular}
452	\end{table}
453	
454	For Pythia, the seed=43 LoRA falls within 1.05\,pp of the baseline; cross-seed transfer averages 76.76\%, a 1.30\,pp deficit relative to within-seed performance.
455	For GPT-2~XL, seed=43 exceeds seed=42 by 2.04\,pp, with non-overlapping 95\% CIs; the direction reversal across models confirms that seed variation introduces bidirectional noise rather than systematic bias.
456	Top-5 feature importance is identical across seeds for both models (\texttt{var\_surprisal}, \texttt{p90\_ppl}, \texttt{mean\_ppl}, \texttt{var\_ppl}, \texttt{p75\_ppl}); depth signal therefore arises from the recursive process itself rather than idiosyncratic LoRA weight configurations.
457	
458	\paragraph{Outlier handling.}
459	Feature extraction occasionally produces extreme perplexity values (outlier passages); we apply per-feature clipping at $\pm 10^{10}$ before classification, affecting ${<}0.1$\% of samples.
460	The d3 perplexity distribution varies substantially across seeds: under seed=42, 0.56\% of d3 passages exceed $10^6$ in raw perplexity, while under seed=43 this fraction rises to 12.8\%.
461	Despite this variation, the classifier remains effective after clipping, confirming that the depth signal resides in the p90-and-below distributional shape rather than extreme outliers.
462	
463	\subsection{Generation Length Ablation}
464	\label{app:length_ablation}
465	
466	Table~\ref{tab:length_ablation} reports classification accuracy as a function of passage length (Pythia-1.4B nucleus, depths 0--3).
467	
468	\begin{table}[h]
469	\centering
470	\small
471	\caption{Generation length ablation (Pythia-1.4B nucleus, 5-fold CV). Accuracy increases monotonically with passage length; the 9.47\,pp spread confirms that longer passages provide stronger statistical signal.}
472	\label{tab:length_ablation}
473	\begin{tabular}{@{}lc@{}}
474	\toprule
475	Passage length (tokens) & Acc (\%) \\
476	\midrule
477	128 & 68.35 \\
478	256 & 73.80 \\
479	512 & 77.82 \\
480	\bottomrule
481	\end{tabular}
482	\end{table}
483	
484	Depth signal is detectable from 128 tokens (2.7$\times$ chance) and saturates near 500 tokens.
485	The monotonic increase reflects the statistical nature of the features: longer passages yield more stable estimates of perplexity percentiles and surprisal variance, reducing within-class overlap at adjacent depth boundaries.
486	
487	\subsection{Mixed-Depth Corpus}
488	\label{app:mixed_depth}
489	
490	Per-passage classification is largely independent of corpus composition: evaluating on a corpus containing mixed proportions of d0--d3 passages (rather than balanced classes) yields macro-recall $\Delta{=}{-}1.62$\,pp relative to the balanced benchmark (within the 2\,pp tolerance).
491	Individual class deltas range from $-$0.45\,pp to $-$2.43\,pp (d1 shows the largest shift); the RF classifier operates on per-sample features without sensitivity to the class distribution of the evaluation corpus.
492	Macro-recall $\Delta$ = $-$1.62\,pp (within the 2\,pp threshold); individual class variations (max 2.43\,pp on d1) arise from held-out sample composition rather than classifier sensitivity to corpus distribution, as the Random Forest produces identical per-sample predictions regardless of batch context.
493	
494	\subsection{Learned Estimator Comparison}
495	\label{app:learned_estimator}
496	
497	Table~\ref{tab:learned_estimator} evaluates three learned classifiers (XGBoost, ordinal MLP with CORAL loss, prototypical networks) under the same leave-one-model-out protocol as Table~\ref{tab:cross_model}.
498	All three methods operate on the same 19-dimensional feature vector; the comparison isolates the effect of the classification head.
499	
500	\begin{table}[h]
501	\centering
502	\small
503	\caption{Learned estimator cross-model transfer (leave-one-model-out, nucleus, 4-class). RF baseline from Table~\ref{tab:cross_model}. Chance = 25\%.}
504	\label{tab:learned_estimator}
505	\begin{tabular}{@{}lcccc@{}}
506	\toprule
507	Method & Pythia & OLMo & GPT-2 XL & Mean \\
508	\midrule
509	RF (baseline) & --- & --- & --- & 66.4 \\
510	XGBoost & 63.7 & 69.8 & 68.1 & 67.2 \\
511	Ordinal MLP & 62.5 & 69.7 & 67.9 & 66.7 \\
512	Prototypical & 61.6 & 70.0 & 68.4 & 66.6 \\
513	\bottomrule
514	\end{tabular}
515	\end{table}
516	
517	All three learned methods match the RF baseline within 0.8\,pp on average; the Pythia holdout is consistently the hardest (61.6--63.7\%), while OLMo and GPT-2~XL holdouts yield 67.9--70.0\%.
518	The narrow spread ($\leq$0.8\,pp across four methods) reinforces the conclusion that the 19-feature representation, not the classifier, determines the accuracy ceiling in the cross-model transfer setting.
519	
520	\subsection{Instruction-Tuned Model at 1.5B Scale}
521	\label{app:instruct_1p5b}
522	
523	To test whether instruction tuning eliminates depth signal at matched scale (1.5B, avoiding the quantization confound of \S\ref{sec:gen:crossscale}), we run the full recursive pipeline on Qwen2.5-1.5B-Instruct with self-reference feature extraction (i.e., the same model serves as both generator and reference).
524	
525	The RF classifier achieves 47.4\% four-class accuracy (95\% CI $[46.7, 48.1]$, $1.9\times$ chance); instruction tuning therefore reduces but does not eliminate depth signal.
526	The pairwise AUC profile differs from base models: d0v1 = 0.653, d1v2 = 0.620, d2v3 = 0.664, with a gap-dependent pattern (non-adjacent pairs yield higher AUC, e.g., d0v3 = 0.902) but no pair reaching the 0.75 threshold.
527	
528	The top-5 features shift substantially: \texttt{surprisal\_range}, \texttt{surprisal\_position\_corr}, \texttt{prob\_std}, \texttt{surprisal\_first\_half\_minus\_second}, and \texttt{surprisal\_std} replace the perplexity tail statistics (\texttt{p90\_ppl}, \texttt{var\_surprisal}) that dominate in base models.
529	This feature shift suggests instruction tuning compresses the perplexity distribution (reducing tail discriminability) while preserving positional and range-based surprisal patterns.
530	
531	Two caveats apply: (1) self-reference evaluation may inflate or deflate accuracy relative to cross-reference evaluation (cf.\ \S\ref{app:ref_ablation}); (2) a single instruction-tuned model does not establish the generality of the feature shift across architectures or instruction-tuning recipes.
532	
533	\subsection{Downstream Fine-Tuning Probe}
534	\label{app:downstream}
535	
536	We fine-tune Pythia-410M with LoRA ($r{=}16$, $\alpha{=}32$) on depth-stratified subsets (500 samples each) and evaluate held-out perplexity (200 samples, 50 per depth).
537	
538	\begin{table}[h]
539	\centering
540	\small
541	\caption{Downstream fine-tuning probe: held-out perplexity by training subset (Pythia-410M LoRA, seed=42). $\Delta$: signed difference vs.\ baseline (negative = better).}
542	\label{tab:downstream}
543	\begin{tabular}{@{}lcc@{}}
544	\toprule
545	Training subset & PPL & $\Delta$ vs.\ baseline \\
546	\midrule
547	Baseline (no fine-tuning) & 5.67 & --- \\
548	d0 only & 5.65 & $-$0.02 \\
549	d1 only & 5.55 & $-$0.12 \\
550	d2 only & 5.56 & $-$0.11 \\
551	Mixed (d0--d3) & 5.55 & $-$0.12 \\
552	\bottomrule
553	\end{tabular}
554	\end{table}
555	
556	The hypothesis that d0-only data yields the lowest perplexity is not supported: d1-only and mixed subsets tie for best (PPL~5.55), both marginally below d0-only (5.65).
557	The PPL spread is small (0.12, 2.1\% relative) and the sample size (500 per condition, single seed) is insufficient for statistical significance.
558	Training loss decreases monotonically with depth (d0: 2.558, d1: 1.920, d2: 1.286), consistent with recursive generation reducing information content and making text easier to model.
559	This pilot establishes that depth-filtered data is not harmful for downstream fine-tuning; whether depth-aware curation provides a meaningful advantage requires larger-scale evaluation.
560	
561	\subsection{Feature Group Ablation}
562	\label{app:feature_ablation}
563	
564	Table~\ref{tab:feature_ablation} reports cross-model transfer accuracy (leave-one-model-out, nucleus) when restricting the classifier to subsets of the 19-feature vector, grouped by signal type.
565	
566	\begin{table}[h]
567	\centering
568	\small
569	\caption{Feature group ablation (cross-model LOO, nucleus, 4-class). Chance = 25\%.}
570	\label{tab:feature_ablation}
571	\begin{tabular}{@{}lccc@{}}
572	\toprule
573	Feature group & \#Feat. & Acc (\%) & $\Delta$ vs.\ Full \\
574	\midrule
575	Full (all 19) & 19 & 66.6 & --- \\
576	Perplexity only & 9 & 66.0 & $-$0.5 \\
577	Entropy/Surprisal only & 5 & 63.2 & $-$3.4 \\
578	Repetition/Diversity only & 5 & 53.0 & $-$13.6 \\
579	\midrule
580	\texttt{p90\_ppl} only & 1 & 58.3 & $-$8.3 \\
581	\bottomrule
582	\end{tabular}
583	\end{table}
584	
585	The 9 perplexity features nearly match the full set ($\Delta{=}{-}0.5$\,pp), while repetition/diversity features alone fall 13.6\,pp below; perplexity degradation statistics therefore carry the dominant depth signal.
586	The top-2 individual features by Gini importance are \texttt{p90\_ppl} (22.4\%) and \texttt{var\_surprisal} (18.8\%), accounting for 41\% of total importance.
587	
588	\subsection{RF Seed Robustness}
589	\label{app:rf_seed}
590	
591	Table~\ref{tab:rf_seed} reports cross-model transfer accuracy across three RF random seeds.
592	
593	\begin{table}[h]
594	\centering
595	\small
596	\caption{RF seed robustness (cross-model LOO, nucleus, 4-class).}
597	\label{tab:rf_seed}
598	\begin{tabular}{@{}lc@{}}
599	\toprule
600	Seed & Acc (\%) \\
601	\midrule
602	42 & 66.4 \\
603	123 & 66.5 \\
604	456 & 66.5 \\
605	\midrule
606	Mean $\pm$ std & 66.48 $\pm$ 0.06 \\
607	\bottomrule
608	\end{tabular}
609	\end{table}
610	
611	The 0.06\,pp standard deviation across seeds confirms that RF classification is deterministic to within rounding noise at this sample size, and reported accuracy differences across experimental conditions (e.g., feature ablation, cross-model transfer) are not attributable to classifier randomness.
612	
613	\subsection{Binary Detector Baselines for Ordinal Classification}
614	\label{app:detector_baselines}
615	
616	We evaluate whether existing binary AI-text detectors, when their scores are used as features for ordinal classification, can match our 19-feature RF pipeline.
617	Binoculars~\cite{binoculars2024} and Fast-DetectGPT~\cite{fast_detectgpt2024} scores are computed on the Pythia-1.4B nucleus ($p{=}0.95$) subset and fed to: (a)~a log-likelihood rank classifier (Log-Rank, 64.0\%), (b)~a combined RF trained on both detector scores (Combined, 74.2\%), and (c)~the standard 19-feature RF (78.2\%).
618	The 4\,pp gap (74.2\% vs.\ 78.2\%) confirms that perplexity distributional features capture ordinal depth structure beyond what generic detection scores provide.
619	Note that Fast-DetectGPT exhibits numerical overflow on Pythia nucleus d1 (mean perturbation score $>$28{,}000); results for this cell should be interpreted cautiously.
620	
621	\subsection{Prompted Generation Results}
622	\label{app:prompted_gen}
623	
624	Table~\ref{tab:prompted_gen} reports depth estimation performance under topic-seeded (prompted) generation using GPT-2~XL with nucleus sampling ($p{=}0.95$, depths 0--3).
625	Generation is conditioned on Wikipedia topic prompts rather than a bare BOS token, a more ecologically valid test of depth signal persistence.
626	
627	\begin{table}[h]
628	\centering
629	\small
630	\caption{Prompted generation (GPT-2~XL, nucleus $p{=}0.95$, topic-seeded). 5-fold CV accuracy and pairwise AUC. Chance = 25\%.}
631	\label{tab:prompted_gen}
632	\begin{tabular}{@{}lc@{}}
633	\toprule
634	Metric & Value \\
635	\midrule
636	4-class accuracy (\%) & 69.52 $[68.9, 70.2]$ \\
637	BOS-seeded baseline (\%) & 83.3 \\
638	$\Delta$ (prompted $-$ BOS) & $-$13.78\,pp \\
639	\midrule
640	AUC d0v1 & 0.916 \\
641	AUC d1v2 & 0.782 \\
642	AUC d2v3 & 0.744 \\
643	\midrule
644	Top-1 feature & \texttt{p90\_ppl} \\
645	Top-2 feature & \texttt{var\_surprisal} \\
646	Top-3 feature & \texttt{p75\_ppl} \\
647	\bottomrule
648	\end{tabular}
649	\end{table}
650	
651	The 13.8\,pp drop relative to BOS-seeded generation is expected: topic prompts constrain the output distribution, reducing the variance that distinguishes depths.
652	Nevertheless, accuracy remains $2.8\times$ chance and pairwise AUC decays monotonically (0.916, 0.782, 0.744); the depth signal is therefore not an artifact of unconstrained generation.
653	Top features are identical to BOS-seeded (\texttt{p90\_ppl} first); the same perplexity tail erosion mechanism operates under prompted conditions.
654	
655	\subsection{Extended Discussion}
656	\label{app:extended_discussion}
657	
658	\paragraph{Depth-graduated curation.}
659	Current data curation operates on a binary human-vs-machine distinction \cite{dsir2023,qurating2024}.
660	Recursive generation depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.
661	The 70--85\% in-distribution accuracy and $\mathrm{EDD}_{0.75}{=}4$ suggest depth-graduated filtering is feasible within known model--strategy configurations, though the d1/d2 boundary inversion under cross-strategy transfer (\S\ref{sec:gen:crossstrategy}) means reliable curation requires either known decoding strategy metadata or an upstream strategy-identification step; a pilot study (Appendix~\ref{app:curation_poc}) yields an inconclusive RF-vs-unfiltered comparison ($p>0.4$), though RF-filtered subsets significantly outperform size-matched random subsampling ($p<0.001$--$0.02$); large-scale validation remains open.
662	Importance weighting \cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding.
663	
664	\paragraph{Toward a provenance toolkit.}
665	Depth estimation complements existing provenance methods along orthogonal axes.
666	Watermarking \cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.
667	Source attribution \cite{uchendu2020_attribution} identifies the generating model but not the generation history.
668	Depth estimation characterizes \emph{iterative reuse} regardless of generator cooperation or identity.
669	A layered provenance system combining these three signals (watermark presence, source model, and recursive generation depth) could support more nuanced data auditing than any single method.
670	
671	\subsection{Computational Resources and Reproducibility}
672	\label{app:compute}
673	
674	\paragraph{Hardware.}
675	All experiments were conducted on 2$\times$ NVIDIA RTX PRO 6000 (48\,GB) GPUs locally and 2$\times$ NVIDIA RTX PRO 6000 (48\,GB) on cloud instances.
676	Total computation is approximately 200 GPU$\cdot$hours, covering the $3 \times 3$ generation matrix (LoRA fine-tuning + sampling at each depth), feature extraction, depth extension to d5, 7--8B QLoRA experiments, and all ablations.
677	
678	\paragraph{Software.}
679	Key library versions: PyTorch 2.10.0+cu128, Transformers 5.8.1, PEFT 0.7.1, scikit-learn 1.8.0.
680	Additional dependencies: Accelerate 1.13.0, Datasets 4.8.4, XGBoost 3.2.0, NumPy 2.2.6 (Python 3.12.3, CUDA 12.8).
681	
682	\paragraph{Hyperparameters.}
683	LoRA hyperparameters ($r{=}16$, $\alpha{=}32$, dropout $0.05$, lr $2{\times}10^{-4}$, batch size 8, 3 epochs) follow \citet{hu2022lora}.
684	The Random Forest classifier uses 200 trees, Gini criterion, and no max depth, without hyperparameter search; all reported results use 5-fold stratified cross-validation.
685	
686	\paragraph{Inference cost.}
687	Feature extraction and classification require no GPU.
688	Inference takes approximately 2 minutes per 5{,}000 samples on a single CPU core (reference-model forward pass + RF prediction), enabling deployment without specialized hardware.
689	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b1d696b-5395-47e6-8c9b-5438aed45bb4",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "106ee534-4df1-4422-9eef-ebe80efd144e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
      "content": "\\section{Additional Results}\n\\label{app:additional}\n\n\\subsection{Top-$k$ Feature Trajectories}\n\\label{app:topk_trajectories}\n\nFigure~\\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\\tau{=}0.9$) sampling.\nTop-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \\S\\ref{sec:atlas:strategy}.\nConcretely, the d0$\\to$d1 drop in \\texttt{p90\\_ppl} under top-$k$ is 78\\% (vs.\\ 87\\% for nucleus), and the d2$\\to$d3 reduction is 31\\% (vs.\\ 39\\% for nucleus).\nDespite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.\n\n\\subsection{Permutation Importance}\n\\label{app:permutation}\n\nTo verify that the Gini-based importance rankings in \\S\\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.\nThe top-2 features are stable across measures: \\texttt{p90\\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \\texttt{var\\_surprisal} in 8/9 (vs.\\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \\texttt{p75\\_ppl} displaces \\texttt{var\\_surprisal} to rank 3).\nKendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).\nPairwise Spearman correlations are: SHAP--Gini $\\rho{=}0.93$, SHAP--permutation $\\rho{=}0.84$, Gini--permutation $\\rho{=}0.76$.\nPer-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical; the top features are therefore robust to the choice of importance measure at the aggregate level, though per-cell rankings exhibit model-dependent variation.\n\n\\subsection{Per-Class Recall}\n\\label{app:per_class}\n\nTable~\\ref{tab:per_class_recall} reports per-class recall across all 9 atlas cells (4-class in-distribution, 5-fold CV).\nDepth~0 recall exceeds 98\\% uniformly.\nAmong generated depths, d2 is the hardest class in every cell; the deficit is most pronounced under top-$k$ sampling (46--53\\%), where vocabulary truncation removes the tail tokens that carry depth-discriminative signal.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-class recall (\\%) for all 9 atlas cells. d2 is the lowest-recall class in every cell. Boldface marks the highest d2 recall.}\n\\label{tab:per_class_recall}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nCell & d0 & d1 & d2 & d3 \\\\\n\\midrule\nPythia, nuc.       & 99.7 & 81.9 & 58.7 & 72.3 \\\\\nPythia, $\\tau$     & 99.7 & 81.3 & 53.9 & 72.1 \\\\\nPythia, top-$k$    & 99.5 & 72.3 & 45.6 & 57.5 \\\\\nOLMo, nuc.         & 98.8 & 80.5 & 61.5 & 74.3 \\\\\nOLMo, $\\tau$       & 99.7 & 87.7 & 66.1 & 77.2 \\\\\nOLMo, top-$k$      & 99.5 & 78.5 & 51.2 & 65.6 \\\\\nGPT-2~XL, nuc.     & 99.2 & 85.9 & \\textbf{73.3} & 77.5 \\\\\nGPT-2~XL, $\\tau$   & 99.5 & 90.9 & 68.8 & 81.9 \\\\\nGPT-2~XL, top-$k$  & 98.5 & 79.5 & 52.5 & 71.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{DCOL Iteration Details}\n\\label{app:dcol_iterations}\n\nTable~\\ref{tab:dcol_iterations} summarizes all six DCOL iterations.\nDeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.7\\%.}\n\\label{tab:dcol_iterations}\n\\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}\n\\toprule\nVer. & Backbone & Config & Outcome \\\\\n\\midrule\nv1 & DeBERTa & FT, m\\_lr $10^{-3}$ & Embed.\\ collapse (31.5\\%) \\\\\nv2 & DeBERTa & FT, m\\_lr $10^{-4}$ & OOM \\\\\nv3 & DeBERTa & FT, m\\_lr $10^{-4}$ & Forgetting + OOM \\\\\nv4 & DeBERTa & LoRA, m\\_lr $10^{-3}$ & Embed.\\ collapse \\\\\nv5 & DeBERTa & LoRA, m\\_lr $10^{-4}$ & NaN gradients \\\\\nv6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\\% ($-$13.7pp) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Zero-Shot LLM Prompt Template}\n\\label{app:zeroshot_prompt}\n\nBoth DeepSeek V3.2 and Qwen2.5-7B-Instruct use identical prompting.\nThe system message defines recursive generation depth with per-depth descriptions (depth~0: human-written; depth~1--3: successive LLM generation cycles) and lists expected textual patterns at each depth (vocabulary richness, repetition, coherence).\nThe user message presents the passage (truncated to ${\\approx}$384 words) and requests a JSON response containing an integer depth prediction (0--3), a confidence score, and a one-sentence reasoning.\nNo in-context examples are provided.\n\n\\begin{quote}\n\\small\n\\textbf{System:} ``You are an expert at detecting AI-generated text and estimating its generation depth. `Recursive generation depth' refers to how many times a text has been through an LLM generation cycle: Depth~0: Original human-written text [\\ldots] Depth~3: Text generated by an LLM given depth-2 text as input. Key patterns by depth: Depth~0 (human): Rich vocabulary [\\ldots] Depth~3 (third-gen): Noticeable repetition, formulaic structure [\\ldots]''\n\n\\textbf{User:} ``Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3). TEXT: \\{text\\}. Respond with ONLY a JSON object: \\{\\texttt{\"depth\"}: $\\langle$int 0--3$\\rangle$, \\texttt{\"confidence\"}: $\\langle$float 0--1$\\rangle$, \\texttt{\"reasoning\"}: $\\langle$str$\\rangle$\\}''\n\\end{quote}\n\n\\subsection{Temperature Robustness}\n\\label{app:multi_tau}\n\nThe cross-strategy results in \\S\\ref{sec:gen:crossstrategy} use a single temperature ($\\tau{=}0.9$).\nTo test whether depth signal generalizes across temperatures, we repeat the classification pipeline at $\\tau \\in \\{0.5, 0.7, 0.9, 1.1\\}$ on Pythia-1.4B.\n\n\\paragraph{Within-$\\tau$ robustness.}\nFor $\\tau \\in [0.5, 0.9]$, d1-vs-d2 AUC exceeds 0.80 (peak 0.851 at $\\tau{=}0.7$, comparable to nucleus $p{=}0.95$'s 0.861) and 4-class accuracy ranges from 75.4\\% to 77.3\\% (Table~\\ref{tab:multi_tau_within}); the depth signal is therefore not an artifact of a single temperature.\nThe same top-5 features (\\texttt{var\\_surprisal}, \\texttt{p90\\_ppl}, \\texttt{mean\\_ppl}, \\texttt{mean\\_surprisal}, \\texttt{p75\\_ppl}) dominate across all $\\tau$ values with only minor rank-order variation.\n\n\\paragraph{Collapse at $\\tau{=}1.1$: memorization as prerequisite.}\nAt $\\tau{=}1.1$, 4-class accuracy drops to 57.2\\% and d1v2 AUC falls to 0.528.\nTraining loss reveals the mechanism: at low temperature ($\\tau{=}0.5$), fine-tuning loss decreases steeply across recursive depths ($2.27 \\to 0.42 \\to 0.16$), a sign of rapid memorization of the model's own output.\nAt $\\tau{=}1.1$, loss remains nearly flat ($2.27 \\to 1.91 \\to 1.85$); high-entropy output resists memorization, so depth-dependent distributional shifts do not accumulate.\nThis establishes \\emph{memorization as a prerequisite} for detectable depth signal: recursive depth is discriminable only when successive fine-tuning iterations progressively reshape the output distribution.\n\n\\paragraph{Cross-$\\tau$ non-transferability.}\nLeave-one-$\\tau$-out transfer yields mean accuracy of 46.7\\% with mean d1v2 AUC of 0.319 (Table~\\ref{tab:multi_tau_cross}), worse than cross-strategy transfer (59.1\\%; \\S\\ref{sec:gen:crossstrategy}).\nHoldout $\\tau{=}0.5$ produces inverted d1v2 AUC (0.176); different temperatures therefore produce surprisal distributions with incompatible shapes.\nThis extends the strategy-specificity finding: even within a single decoding family, the feature space is temperature-specific; strategy-conditioned classifiers are therefore necessary.\n\n\\paragraph{Ecological validity.}\nOn WikiText-103 (546 editorial passages), all three model-specific RF classifiers achieve $\\geq$98.5\\% d0 accuracy despite $+$621\\% domain shift in mean perplexity, partly an easy case, as WikiText's higher perplexity places it farther from d1--d3 in feature space.\nOn noisier web-crawl data (5{,}000 C4 passages), FPR ranges from 4.7\\% (OLMo) to 22.4\\% (GPT-2~XL), concentrated in template/SEO content with high n-gram repetition (Table~\\ref{tab:calibration}); deployment on heterogeneous web data requires model-specific calibration.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Within-$\\tau$ 4-class classification (Pythia-1.4B, 5-fold CV). d$i$v$j$: pairwise AUC for depth $i$ vs.\\ depth $j$.}\n\\label{tab:multi_tau_within}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$\\tau$ & 4-class acc (\\%) & d1v2 AUC & d0v1 AUC & d2v3 AUC \\\\\n\\midrule\n0.5 & 77.3 & 0.842 & 0.996 & 0.764 \\\\\n0.7 & 75.4 & 0.851 & 0.997 & 0.720 \\\\\n0.9 & 75.9 & 0.808 & 0.991 & 0.781 \\\\\n1.1 & 57.2 & 0.528 & 0.988 & 0.599 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-$\\tau$ leave-one-out transfer (Pythia-1.4B). Train on three temperatures, test on the held-out one.}\n\\label{tab:multi_tau_cross}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nHoldout & Acc (\\%) & d1v2 AUC \\\\\n\\midrule\n$\\tau{=}0.5$ & 52.2 & 0.176 \\\\\n$\\tau{=}0.7$ & 41.0 & 0.299 \\\\\n$\\tau{=}0.9$ & 46.4 & 0.277 \\\\\n$\\tau{=}1.1$ & 47.1 & 0.525 \\\\\n\\midrule\nMean & 46.7 & 0.319 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Feature Overlap Analysis}\n\\label{app:feature_overlap}\n\nWe probe whether end-to-end PLM representations capture the same depth signals as our statistical features via linear probing of [CLS] representations from DeBERTa-v3-base and RoBERTa-base.\nPLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics; \\texttt{var\\_surprisal} and \\texttt{p90\\_ppl} yield negative $R^2$ under linear probing; these features are not linearly accessible in the pretrained representation space.\nThis confirms that the 20pp accuracy gap between feature-based and end-to-end methods (\\S\\ref{app:e2e}) stems from complementary, not redundant, representations: PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties that constitute the dominant depth markers.\n\n\\subsection{End-to-End Learning}\n\\label{app:e2e}\n\nDeBERTa-v3-base \\cite{he2021_deberta_v3} and RoBERTa-base \\cite{liu2019_roberta} finetuned end-to-end achieve 58.3\\% ($\\pm$4.7\\%) and 59.5\\% ($\\pm$3.2\\%) respectively, lagging the RF baseline (78.7\\%) by 20.4pp and 19.2pp.\nThe 1.2pp inter-backbone gap rules out architecture bias; Table~\\ref{tab:e2e_detail} shows both backbones share the same failure mode (high d0 F1, $>$0.94, but collapsed d1/d2 performance, F1 $\\leq$ 0.42), while RF achieves 0.596 d2 recall, a $>$2$\\times$ advantage at the hardest depth class.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-class performance for end-to-end PLM classifiers vs.\\ RF baseline (Pythia-1.4B nucleus). PLM columns report F1; RF d2 column reports recall (the class with the largest PLM--RF gap). Both PLM backbones share the same failure pattern: collapsed d1/d2 scores despite adequate d0/d3.}\n\\label{tab:e2e_detail}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nMethod & Acc (\\%) & d0 & d1 & d2 & d3 \\\\\n\\midrule\nDeBERTa-v3 & 58.3\\,$\\pm$\\,4.7 & .947 & .378 & .247 & .656 \\\\\nRoBERTa-base & 59.5\\,$\\pm$\\,3.2 & .958 & .416 & .261 & .647 \\\\\n\\midrule\nRF (19 feat.) & 78.7 & --- & --- & .596$^\\dagger$ & --- \\\\\n\\bottomrule\n\\multicolumn{6}{@{}l}{\\footnotesize $^\\dagger$Recall; shown for the depth class with the largest PLM--RF gap.}\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Feature space divergence.}\nSHAP TreeExplainer analysis confirms that perplexity and surprisal features account for 88.8\\% of RF's total contribution.\nThree independent importance measures (SHAP, Gini, and permutation) show strong concordance (Kendall's $W{=}0.90$, $p{<}0.005$; pairwise Spearman $\\rho$: SHAP--Gini $0.93$, SHAP--permutation $0.84$; \\S\\ref{app:permutation}), with \\texttt{p90\\_ppl} appearing in the SHAP top-2 in 9/9 cells and \\texttt{var\\_surprisal} in 8/9.\nLinear probing of PLM [CLS] representations yields negative $R^2$ for both \\texttt{var\\_surprisal} and \\texttt{p90\\_ppl} (\\S\\ref{app:feature_overlap}); pretrained representations lack the linear structure needed to recover perplexity tail statistics, a systematic representational gap rather than a backbone-specific artifact.\n\nDCOL \\cite{cloc2025} reached 64.5\\% (\\S\\ref{app:dcol_iterations}); all end-to-end approaches (58--65\\%) underperform feature-based methods; depth estimation therefore benefits from targeted statistical features that capture distributional tail properties absent from PLM representations.\nThis comparison is bounded by backbone scale ($\\leq$125M parameters); whether larger PLMs (e.g., 7B+) can close the gap via richer internal representations remains an open question.\n\n\\subsection{Domain Bias Analysis}\n\\label{app:domain_bias}\n\nTo assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.\n\n\\paragraph{Methodological note.}\nAn initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\\%, seed-group prediction 20.8\\%).\nWe discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.\nThe results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.\n\n\\paragraph{Sub-A: Standard CV.}\nFive-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\\% to 82\\% across the 9 atlas cells (up to 2.5$\\times$ above the 33.3\\% chance level); depth signal is therefore the dominant classification factor.\n\n\\paragraph{Sub-B: LOGO evaluation.}\nWe assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.\nLOGO mean accuracy is 72.1\\% (range 59.5--81.6\\%), matching standard CV (72.0\\%) within noise (before fix: 64.0\\%, reflecting the depth--group confound).\nPer-cell fold standard deviations range from 0.4pp to 1.4pp; cross-group generalization is therefore as reliable as within-group classification.\n\n\\paragraph{Sub-C: Negative control.}\nWe train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\\%).\nDepth prediction accuracy averages 72.0\\%; seed-group prediction averages 10.2\\%, indistinguishable from chance (before fix: 20.8\\%, inflated by the depth--group confound).\nThe depth-to-seed-group accuracy ratio is 7.1$\\times$; the feature representation therefore encodes depth but not seed-article identity.\n\nTaken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.\n\n\\subsection{Wild-Data Calibration}\n\\label{app:calibration}\n\nTable~\\ref{tab:calibration} reports d0 accuracy and false positive rate (FPR) for all three model-specific nucleus RF classifiers on two out-of-distribution human-text corpora: WikiText-103 (546 editorial passages) and C4 (5{,}000 web-crawl passages, crawled 2019--2020; pre-LLM deployment).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Wild-data d0 accuracy and FPR for nucleus RF classifiers. All passages are human-written (true d0). FPR = fraction misclassified as d1+. 95\\% Wilson CIs computed for C4 ($n{=}5{,}000$).}\n\\label{tab:calibration}\n\\begin{tabular}{@{}llrccc@{}}\n\\toprule\nModel & Source & $n$ & d0 (\\%) & FPR (\\%) & 95\\% Wilson CI \\\\\n\\midrule\nPythia-1.4B & WikiText & 546 & 100.0 & 0.0 & --- \\\\\n & C4 & 5{,}000 & 79.8 & 20.2 & [19.1, 21.3] \\\\\n\\addlinespace\nGPT-2~XL & WikiText & 546 & 99.3 & 0.7 & --- \\\\\n & C4 & 5{,}000 & 77.6 & 22.4 & [21.3, 23.6] \\\\\n\\addlinespace\nOLMo-1B & WikiText & 546 & 98.5 & 1.5 & --- \\\\\n & C4 & 5{,}000 & 95.3 & 4.7 & [4.2, 5.3] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn WikiText-103, all three classifiers achieve $\\geq$98.5\\% d0 accuracy; editorial text is therefore reliably distinguished from recursive generations across model families.\nOn C4, FPR varies sharply: OLMo (4.7\\%) vs.\\ Pythia (20.2\\%) and GPT-2~XL (22.4\\%).\nC4 misclassifications concentrate in template and SEO content with elevated repetition features (\\texttt{rep\\_3gram} $+$37\\%, \\texttt{rep\\_4gram} $+$75\\% vs.\\ correctly classified d0 passages), rather than in random noise.\nThe model gap likely reflects training data composition: OLMo (trained on Dolma, which includes diverse web data) produces d0 features more tolerant of web-crawl variation, while Pythia and GPT-2~XL (trained primarily on Wikipedia/WebText) map template-heavy content into the d1+ region.\nAmong C4 false positives for GPT-2~XL, predictions distribute as d1 (9.0\\%), d2 (3.7\\%), d3 (9.6\\%); for OLMo, d1 (2.9\\%), d2 (0.5\\%), d3 (1.3\\%). The non-uniform depth distribution suggests the classifier maps specific repetition patterns to particular depth signatures rather than producing random misclassifications.\n\n\\subsection{Downstream Curation PoC}\n\\label{app:curation_poc}\n\nTo validate that depth estimation translates to actionable data curation, we conduct a proof-of-concept downstream evaluation.\nWe fine-tune Pythia-410M with LoRA ($r{=}16$, $\\alpha{=}32$) for 3 epochs on 8 data conditions derived from the Pythia nucleus depth-estimation corpus, repeating each condition over 5 random seeds.\nConditions vary the selection mechanism (RF-predicted depth, oracle depth, random subsampling) and stringency (strict $\\approx$25\\%, moderate $\\approx$50\\%, soft threshold).\nTable~\\ref{tab:curation_poc} reports per-condition perplexity; Table~\\ref{tab:curation_comparisons} reports pairwise contrasts.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Curation PoC: per-condition perplexity (Pythia-410M LoRA, 5 seeds). $\\Delta$ is signed so that positive values indicate lower (better) perplexity than unfiltered. $^*$\\,: $p<0.05$ (paired $t$-test vs.\\ unfiltered).}\n\\label{tab:curation_poc}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nCondition & Mean PPL & Std & $n$ & $\\Delta$ vs Unfilt. & $p$ & $d_z$ \\\\\n\\midrule\nunfiltered        & 15.776 & 0.066 & 10{,}000 & ---      & ---   & ---      \\\\\nrf\\_soft          & 15.733 & 0.038 &  4{,}422 & +0.043   & 0.407 &  0.41    \\\\\nrf\\_moderate      & 15.756 & 0.056 &  4{,}940 & +0.021   & 0.492 &  0.34    \\\\\nrf\\_strict        & 15.810 & 0.061 &  2{,}496 & $-$0.034 & 0.607 & $-$0.25  \\\\\noracle\\_moderate  & 15.809 & 0.103 &  5{,}000 & $-$0.033 & 0.485 & $-$0.34  \\\\\noracle\\_strict    & 15.879 & 0.128 &  2{,}500 & $-$0.103 & 0.216 & $-$0.66  \\\\\nrandom\\_soft      & 16.062 & 0.079 &  4{,}422 & $-$0.286 & ${<}$0.001$^*$ & $-$2.77  \\\\\nrandom\\_moderate  & 15.998 & 0.090 &  4{,}940 & $-$0.222 & 0.028$^*$ & $-$1.50  \\\\\nrandom\\_strict    & 16.239 & 0.165 &  2{,}496 & $-$0.463 & 0.013$^*$ & $-$1.89  \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise comparisons (paired $t$-test, 5 seeds). $^*$\\,: $p<0.05$; $^{**}$\\,: $p<0.01$.}\n\\label{tab:curation_comparisons}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nComparison & $\\Delta$ PPL & $t$ & $p$ \\\\\n\\midrule\nrf\\_strict vs random\\_strict     & 0.429 & $-$7.05 & 0.002$^{**}$ \\\\\nrf\\_moderate vs random\\_moderate & 0.242 & $-$3.77 & 0.020$^*$    \\\\\nrf\\_soft vs random\\_soft         & 0.328 & $-$17.98 & ${<}$0.001$^{**}$ \\\\\nrf\\_soft vs unfiltered           & 0.043 &    0.93 & 0.407        \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Reference Model Ablation}\n\\label{app:ref_ablation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Reference model ablation. Classification accuracy (5-fold CV) on Pythia-1.4B generated text (nucleus, d0--d3) using different reference models for feature extraction.}\n\\label{tab:ref_ablation}\n\\begin{tabular}{lcc}\n\\toprule\nReference Model & Architecture & Accuracy (\\%) \\\\\n\\midrule\nPythia-1.4B (self) & GPT-NeoX & 78.6 $\\pm$ 0.6 \\\\\nOLMo-1B (cross) & OLMo & 74.5 $\\pm$ 0.7 \\\\\nGPT-2~XL (cross) & GPT-2 & 67.3 $\\pm$ 0.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Scale Full Results}\n\\label{app:cross_scale_full}\n\nThis section provides the full cross-scale analysis summarized in \\S\\ref{sec:gen:crossscale}.\nWe extend the benchmark to two 7--8B models: Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct, both under 4-bit NF4 QLoRA fine-tuning, generating depths $d \\in \\{0, 1, \\ldots, 5\\}$ with nucleus sampling ($p{=}0.95$, 500 samples per depth).\nFeature extraction uses the same reference model (Pythia-1.4B) and 19-feature pipeline as all prior experiments.\n\n\\paragraph{Scale comparison.}\nTable~\\ref{tab:cross_scale} contrasts the two 7--8B models with the three 1--1.5B models on matched evaluation (nucleus sampling, depths 0--3).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-scale comparison: 4-class RF accuracy (\\%, depths 0--3, nucleus), $\\mathrm{EDD}_{T{=}0.70}$ (depths 0--5), and d0-vs-d1 AUC. CI: 95\\% bootstrap. Chance = 25\\%.}\n\\label{tab:cross_scale}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nModel & 4-class acc & $\\mathrm{EDD}_{T{=}0.70}$ & d0v1 AUC \\\\\n\\midrule\nGPT-2~XL (1.5B) & 84.1 & 4 & 0.999 \\\\\nOLMo-1B & 78.9 & 4 & 0.997 \\\\\nPythia-1.4B & 78.7 & 4 & 0.998 \\\\\n\\midrule\nLlama-3.1-8B & 70.2\\,[68.3, 72.4] & 4 & 0.949 \\\\\nQwen2.5-7B & 60.1\\,[58.0, 62.1] & ${>}5$ & 0.969 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{(1) Depth signal persists at 7--8B scale.}\nBoth 7--8B models substantially exceed the 25\\% chance baseline: Llama-3.1-8B achieves 70.2\\% (95\\% CI $[68.3, 72.4]$) and Qwen2.5-7B achieves 60.1\\% ($[58.0, 62.1]$); recursive depth therefore remains estimable from perplexity-based features even when the generator is 5--7$\\times$ larger than the reference model.\nDepth-0 separability is preserved in both models: d0v1 AUC is 0.949 (Llama-3.1) and 0.969 (Qwen2.5).\n\n\\paragraph{(2) EDD at 7--8B scale.}\nAt threshold $T{=}0.70$, Qwen2.5-7B maintains all consecutive-pair AUCs above 0.70 through depth~5 (Table~\\ref{tab:cross_scale_auc}), yielding $\\mathrm{EDD}_{T{=}0.70} > 5$, exceeding the $\\mathrm{EDD}{=}4$ observed at 1--1.5B.\nLlama-3.1-8B matches the smaller models at $\\mathrm{EDD}{=}4$: its monotonic decay causes d4v5 (0.618) to drop below $T$, despite stronger signal at shallower depths.\nBoth larger generators produce weaker per-step signal than the 1--1.5B models (mean consecutive AUC: 0.786 for Llama-3.1, 0.782 for Qwen2.5, vs.\\ 0.852 at 1--1.5B).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Consecutive binary AUC for 7--8B models (nucleus $p{=}0.95$). Llama-3.1-8B exhibits monotonic decay (d4v5 drops below $T{=}0.70$); Qwen2.5-7B shows a non-monotonic (U-shaped) pattern with all pairs above $T$.}\n\\label{tab:cross_scale_auc}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nModel & d0v1 & d1v2 & d2v3 & d3v4 & d4v5 \\\\\n\\midrule\nLlama-3.1-8B & 0.949 & 0.877 & 0.771 & 0.716 & 0.618 \\\\\nQwen2.5-7B & 0.969 & 0.729 & 0.709 & 0.732 & 0.772 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{(3) Divergent AUC trajectories and instruction-tuning effect.}\nAmong instruction-tuned models, Llama-3.1-8B exhibits monotonic AUC decay consistent with the 1--1.5B pattern, while Qwen2.5-7B shows a U-shaped recovery beyond d2v3 (Table~\\ref{tab:cross_scale_auc}).\nA base-model control (Llama-3.1-8B without instruction tuning) clarifies the causal direction: the base model achieves 59.9\\% four-class accuracy (95\\% CI [57.8, 62.15], $\\mathrm{EDD}_{0.70}{=}2$) with non-monotonic AUC decay (Table~\\ref{tab:llama3_base_auc}), while the instruction-tuned variant reaches 70.2\\% with strictly monotonic decay.\nThe base-model control experiment suggests instruction-tuning regularizes rather than confounds the depth signal.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise AUC: Llama-3.1-8B Base vs.\\ Instruct.}\n\\label{tab:llama3_base_auc}\n\\begin{tabular}{lccccc}\n\\toprule\nVariant & $d_{0\\text{v}1}$ & $d_{1\\text{v}2}$ & $d_{2\\text{v}3}$ & $d_{3\\text{v}4}$ & $d_{4\\text{v}5}$ \\\\\n\\midrule\nBase & 0.918 & 0.794 & 0.682 & 0.730 & 0.595 \\\\\nInstruct & 0.965 & 0.874 & 0.771 & 0.716 & 0.618 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries; depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.\n\n\\paragraph{Caveats.}\nFor Qwen2.5-7B, the CI lower bound (58.0\\%) does not exclude sub-60\\% accuracy; Llama-3.1-8B's lower bound (68.3\\%) is more comfortably above chance but still below the 75--83\\% range at 1--1.5B.\nThe divergent AUC trajectories across two models caution against strong generalizations from only two 7--8B data points: both the monotonic (Llama-3.1) and non-monotonic (Qwen2.5) patterns are single observations, and further architectures are needed to establish which is the dominant regime at this scale.\n\n\\paragraph{Confounds.}\n\\label{app:cross_scale_confounds}\nFour confounds limit these results: (1)~4-bit NF4 QLoRA quantization (absent at 1--1.5B) may distort the perplexity distribution independently of depth; (2)~smaller sample size (500 vs.\\ 5{,}000 per depth) widens confidence intervals; (3)~evaluation is limited to nucleus sampling, leaving other strategies untested at this scale; (4)~vocabulary mismatch between 7--8B generators and the 1.4B reference model.\nThe base-model control partially addresses a former confound (instruction-tuning): since the base variant shows weaker signal with non-monotonic decay while the instruction-tuned variant shows stronger monotonic signal, instruction-tuning regularizes rather than confounds depth estimation.\nThe remaining confounds are not mutually independent (quantization and vocabulary mismatch both affect the perplexity distribution); it is therefore infeasible to attribute the observed accuracy gap (60--70\\% vs.\\ 78--85\\% at 1--1.5B) to any single factor.\n\n\\subsection{Cross-Boundary Generalization}\n\\label{app:cross_boundary}\n\nThe preceding experiments assume a single model family generates all recursive depths.\nIn practice, recursive contamination may traverse model boundaries: text generated by model~A is used to train model~B, whose output trains model~C.\nWe probe whether the depth signal persists under two relaxations of the single-model assumption.\n\n\\paragraph{Cross-model recursive chains.}\nWe construct a heterogeneous chain: human text (d0) $\\to$ Pythia-1.4B generates d1 $\\to$ OLMo-1B finetuned on Pythia-d1 generates d2 $\\to$ GPT-2~XL finetuned on OLMo-d2 generates d3.\nEach recursive step uses a \\emph{different} model family, eliminating the possibility that depth signal arises from a single model's idiosyncratic behavior.\nA 4-class Random Forest achieves 84.75\\% accuracy (95\\% CI $[81.0, 88.25]$), with per-depth F1 scores of 0.98 (d0), 0.88 (d1), 0.76 (d2), and 0.76 (d3).\nPairwise AUC remains high: d0-vs-d1 = 0.999 and d2-vs-d3 = 0.841.\nThese results suggest that distributional artifacts of recursive generation persist across model boundaries. This constitutes preliminary evidence for a process-level depth signal rather than individual generator artifacts.\n\n\\paragraph{Confound discussion.}\nThe heterogeneous chain confounds architecture identity with depth (d1=Pythia, d2=OLMo, d3=GPT-2~XL).\nHowever, if the classifier exploited architecture fingerprints rather than depth signal, near-perfect accuracy would be expected since architecture perfectly determines depth label.\nThe observed 84.75\\% with monotonically decreasing per-depth F1 (d0=0.98, d1=0.88, d2=0.76, d3=0.76) is more consistent with a depth-signal interpretation, as architecture fingerprinting would not produce this graded pattern.\nWe address this confound directly with a reverse-chain control below.\n\n\\paragraph{Reverse-chain control.}\nTo empirically test the architecture confound hypothesis, we constructed a reverse chain (GPT-2~XL $\\to$ OLMo $\\to$ Pythia) reversing the model-depth assignment.\nThe reverse chain achieves 85.75\\% (95\\% CI [82.0, 89.25]), statistically indistinguishable from the forward chain (84.75\\%, [81.0, 88.25]).\nIf the classifier exploited architecture fingerprints rather than depth signal, reversing the chain should invert depth predictions; the equivalent accuracy under both orderings provides empirical evidence against the architecture confound.\n\n\\paragraph{Cross-domain transfer.}\nAll prior experiments use WikiText-103 as the seed corpus.\nTo test domain dependence, we repeat the pipeline with arXiv abstracts as the seed text (Pythia-1.4B, nucleus $p{=}0.95$, 500 samples per depth, d0--d3).\nFive-fold cross-validation yields 74.1\\% $\\pm$ 2.0\\% accuracy, compared to ${\\sim}$78\\% on the WikiText seed.\nPer-depth F1 shows the familiar pattern: d0 = 1.00, d1 = 0.78, d2 = 0.52, d3 = 0.66, with d2 remaining the most challenging class.\nThe 4pp accuracy gap relative to WikiText likely reflects the narrower stylistic range of scientific abstracts, which may reduce the distributional contrast between adjacent depths.\nThese results provide preliminary evidence that the perplexity-based features capture properties of the recursive generation process rather than domain-specific artifacts of the seed corpus.\n\n\\subsection{Cross-Seed Replication}\n\\label{app:seed_replication}\n\nTable~\\ref{tab:seed_replication} reports within-seed accuracy for Pythia-1.4B and GPT-2~XL (nucleus, depths 0--3) under two independent LoRA training seeds.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-seed replication (nucleus $p{=}0.95$, d0--d3). seed=42 is the primary benchmark; seed=43 is an independent replication.}\n\\label{tab:seed_replication}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nModel & Seed & Acc (\\%) & 95\\% CI & $\\Delta$ (pp) \\\\\n\\midrule\nPythia-1.4B & 42 & 78.20 & --- & --- \\\\\nPythia-1.4B & 43 & 77.15 & [76.4, 78.15] & $-$1.05 \\\\\n\\midrule\nGPT-2~XL & 42 & 84.28 & [83.89, 84.77] & --- \\\\\nGPT-2~XL & 43 & 86.32 & [86.17, 86.49] & $+$2.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor Pythia, the seed=43 LoRA falls within 1.05\\,pp of the baseline; cross-seed transfer averages 76.76\\%, a 1.30\\,pp deficit relative to within-seed performance.\nFor GPT-2~XL, seed=43 exceeds seed=42 by 2.04\\,pp, with non-overlapping 95\\% CIs; the direction reversal across models confirms that seed variation introduces bidirectional noise rather than systematic bias.\nTop-5 feature importance is identical across seeds for both models (\\texttt{var\\_surprisal}, \\texttt{p90\\_ppl}, \\texttt{mean\\_ppl}, \\texttt{var\\_ppl}, \\texttt{p75\\_ppl}); depth signal therefore arises from the recursive process itself rather than idiosyncratic LoRA weight configurations.\n\n\\paragraph{Outlier handling.}\nFeature extraction occasionally produces extreme perplexity values (outlier passages); we apply per-feature clipping at $\\pm 10^{10}$ before classification, affecting ${<}0.1$\\% of samples.\nThe d3 perplexity distribution varies substantially across seeds: under seed=42, 0.56\\% of d3 passages exceed $10^6$ in raw perplexity, while under seed=43 this fraction rises to 12.8\\%.\nDespite this variation, the classifier remains effective after clipping, confirming that the depth signal resides in the p90-and-below distributional shape rather than extreme outliers.\n\n\\subsection{Generation Length Ablation}\n\\label{app:length_ablation}\n\nTable~\\ref{tab:length_ablation} reports classification accuracy as a function of passage length (Pythia-1.4B nucleus, depths 0--3).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Generation length ablation (Pythia-1.4B nucleus, 5-fold CV). Accuracy increases monotonically with passage length; the 9.47\\,pp spread confirms that longer passages provide stronger statistical signal.}\n\\label{tab:length_ablation}\n\\begin{tabular}{@{}lc@{}}\n\\toprule\nPassage length (tokens) & Acc (\\%) \\\\\n\\midrule\n128 & 68.35 \\\\\n256 & 73.80 \\\\\n512 & 77.82 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDepth signal is detectable from 128 tokens (2.7$\\times$ chance) and saturates near 500 tokens.\nThe monotonic increase reflects the statistical nature of the features: longer passages yield more stable estimates of perplexity percentiles and surprisal variance, reducing within-class overlap at adjacent depth boundaries.\n\n\\subsection{Mixed-Depth Corpus}\n\\label{app:mixed_depth}\n\nPer-passage classification is largely independent of corpus composition: evaluating on a corpus containing mixed proportions of d0--d3 passages (rather than balanced classes) yields macro-recall $\\Delta{=}{-}1.62$\\,pp relative to the balanced benchmark (within the 2\\,pp tolerance).\nIndividual class deltas range from $-$0.45\\,pp to $-$2.43\\,pp (d1 shows the largest shift); the RF classifier operates on per-sample features without sensitivity to the class distribution of the evaluation corpus.\nMacro-recall $\\Delta$ = $-$1.62\\,pp (within the 2\\,pp threshold); individual class variations (max 2.43\\,pp on d1) arise from held-out sample composition rather than classifier sensitivity to corpus distribution, as the Random Forest produces identical per-sample predictions regardless of batch context.\n\n\\subsection{Learned Estimator Comparison}\n\\label{app:learned_estimator}\n\nTable~\\ref{tab:learned_estimator} evaluates three learned classifiers (XGBoost, ordinal MLP with CORAL loss, prototypical networks) under the same leave-one-model-out protocol as Table~\\ref{tab:cross_model}.\nAll three methods operate on the same 19-dimensional feature vector; the comparison isolates the effect of the classification head.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Learned estimator cross-model transfer (leave-one-model-out, nucleus, 4-class). RF baseline from Table~\\ref{tab:cross_model}. Chance = 25\\%.}\n\\label{tab:learned_estimator}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nMethod & Pythia & OLMo & GPT-2 XL & Mean \\\\\n\\midrule\nRF (baseline) & --- & --- & --- & 66.4 \\\\\nXGBoost & 63.7 & 69.8 & 68.1 & 67.2 \\\\\nOrdinal MLP & 62.5 & 69.7 & 67.9 & 66.7 \\\\\nPrototypical & 61.6 & 70.0 & 68.4 & 66.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll three learned methods match the RF baseline within 0.8\\,pp on average; the Pythia holdout is consistently the hardest (61.6--63.7\\%), while OLMo and GPT-2~XL holdouts yield 67.9--70.0\\%.\nThe narrow spread ($\\leq$0.8\\,pp across four methods) reinforces the conclusion that the 19-feature representation, not the classifier, determines the accuracy ceiling in the cross-model transfer setting.\n\n\\subsection{Instruction-Tuned Model at 1.5B Scale}\n\\label{app:instruct_1p5b}\n\nTo test whether instruction tuning eliminates depth signal at matched scale (1.5B, avoiding the quantization confound of \\S\\ref{sec:gen:crossscale}), we run the full recursive pipeline on Qwen2.5-1.5B-Instruct with self-reference feature extraction (i.e., the same model serves as both generator and reference).\n\nThe RF classifier achieves 47.4\\% four-class accuracy (95\\% CI $[46.7, 48.1]$, $1.9\\times$ chance); instruction tuning therefore reduces but does not eliminate depth signal.\nThe pairwise AUC profile differs from base models: d0v1 = 0.653, d1v2 = 0.620, d2v3 = 0.664, with a gap-dependent pattern (non-adjacent pairs yield higher AUC, e.g., d0v3 = 0.902) but no pair reaching the 0.75 threshold.\n\nThe top-5 features shift substantially: \\texttt{surprisal\\_range}, \\texttt{surprisal\\_position\\_corr}, \\texttt{prob\\_std}, \\texttt{surprisal\\_first\\_half\\_minus\\_second}, and \\texttt{surprisal\\_std} replace the perplexity tail statistics (\\texttt{p90\\_ppl}, \\texttt{var\\_surprisal}) that dominate in base models.\nThis feature shift suggests instruction tuning compresses the perplexity distribution (reducing tail discriminability) while preserving positional and range-based surprisal patterns.\n\nTwo caveats apply: (1) self-reference evaluation may inflate or deflate accuracy relative to cross-reference evaluation (cf.\\ \\S\\ref{app:ref_ablation}); (2) a single instruction-tuned model does not establish the generality of the feature shift across architectures or instruction-tuning recipes.\n\n\\subsection{Downstream Fine-Tuning Probe}\n\\label{app:downstream}\n\nWe fine-tune Pythia-410M with LoRA ($r{=}16$, $\\alpha{=}32$) on depth-stratified subsets (500 samples each) and evaluate held-out perplexity (200 samples, 50 per depth).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Downstream fine-tuning probe: held-out perplexity by training subset (Pythia-410M LoRA, seed=42). $\\Delta$: signed difference vs.\\ baseline (negative = better).}\n\\label{tab:downstream}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nTraining subset & PPL & $\\Delta$ vs.\\ baseline \\\\\n\\midrule\nBaseline (no fine-tuning) & 5.67 & --- \\\\\nd0 only & 5.65 & $-$0.02 \\\\\nd1 only & 5.55 & $-$0.12 \\\\\nd2 only & 5.56 & $-$0.11 \\\\\nMixed (d0--d3) & 5.55 & $-$0.12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe hypothesis that d0-only data yields the lowest perplexity is not supported: d1-only and mixed subsets tie for best (PPL~5.55), both marginally below d0-only (5.65).\nThe PPL spread is small (0.12, 2.1\\% relative) and the sample size (500 per condition, single seed) is insufficient for statistical significance.\nTraining loss decreases monotonically with depth (d0: 2.558, d1: 1.920, d2: 1.286), consistent with recursive generation reducing information content and making text easier to model.\nThis pilot establishes that depth-filtered data is not harmful for downstream fine-tuning; whether depth-aware curation provides a meaningful advantage requires larger-scale evaluation.\n\n\\subsection{Feature Group Ablation}\n\\label{app:feature_ablation}\n\nTable~\\ref{tab:feature_ablation} reports cross-model transfer accuracy (leave-one-model-out, nucleus) when restricting the classifier to subsets of the 19-feature vector, grouped by signal type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Feature group ablation (cross-model LOO, nucleus, 4-class). Chance = 25\\%.}\n\\label{tab:feature_ablation}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nFeature group & \\#Feat. & Acc (\\%) & $\\Delta$ vs.\\ Full \\\\\n\\midrule\nFull (all 19) & 19 & 66.6 & --- \\\\\nPerplexity only & 9 & 66.0 & $-$0.5 \\\\\nEntropy/Surprisal only & 5 & 63.2 & $-$3.4 \\\\\nRepetition/Diversity only & 5 & 53.0 & $-$13.6 \\\\\n\\midrule\n\\texttt{p90\\_ppl} only & 1 & 58.3 & $-$8.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 9 perplexity features nearly match the full set ($\\Delta{=}{-}0.5$\\,pp), while repetition/diversity features alone fall 13.6\\,pp below; perplexity degradation statistics therefore carry the dominant depth signal.\nThe top-2 individual features by Gini importance are \\texttt{p90\\_ppl} (22.4\\%) and \\texttt{var\\_surprisal} (18.8\\%), accounting for 41\\% of total importance.\n\n\\subsection{RF Seed Robustness}\n\\label{app:rf_seed}\n\nTable~\\ref{tab:rf_seed} reports cross-model transfer accuracy across three RF random seeds.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{RF seed robustness (cross-model LOO, nucleus, 4-class).}\n\\label{tab:rf_seed}\n\\begin{tabular}{@{}lc@{}}\n\\toprule\nSeed & Acc (\\%) \\\\\n\\midrule\n42 & 66.4 \\\\\n123 & 66.5 \\\\\n456 & 66.5 \\\\\n\\midrule\nMean $\\pm$ std & 66.48 $\\pm$ 0.06 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 0.06\\,pp standard deviation across seeds confirms that RF classification is deterministic to within rounding noise at this sample size, and reported accuracy differences across experimental conditions (e.g., feature ablation, cross-model transfer) are not attributable to classifier randomness.\n\n\\subsection{Binary Detector Baselines for Ordinal Classification}\n\\label{app:detector_baselines}\n\nWe evaluate whether existing binary AI-text detectors, when their scores are used as features for ordinal classification, can match our 19-feature RF pipeline.\nBinoculars~\\cite{binoculars2024} and Fast-DetectGPT~\\cite{fast_detectgpt2024} scores are computed on the Pythia-1.4B nucleus ($p{=}0.95$) subset and fed to: (a)~a log-likelihood rank classifier (Log-Rank, 64.0\\%), (b)~a combined RF trained on both detector scores (Combined, 74.2\\%), and (c)~the standard 19-feature RF (78.2\\%).\nThe 4\\,pp gap (74.2\\% vs.\\ 78.2\\%) confirms that perplexity distributional features capture ordinal depth structure beyond what generic detection scores provide.\nNote that Fast-DetectGPT exhibits numerical overflow on Pythia nucleus d1 (mean perturbation score $>$28{,}000); results for this cell should be interpreted cautiously.\n\n\\subsection{Prompted Generation Results}\n\\label{app:prompted_gen}\n\nTable~\\ref{tab:prompted_gen} reports depth estimation performance under topic-seeded (prompted) generation using GPT-2~XL with nucleus sampling ($p{=}0.95$, depths 0--3).\nGeneration is conditioned on Wikipedia topic prompts rather than a bare BOS token, a more ecologically valid test of depth signal persistence.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Prompted generation (GPT-2~XL, nucleus $p{=}0.95$, topic-seeded). 5-fold CV accuracy and pairwise AUC. Chance = 25\\%.}\n\\label{tab:prompted_gen}\n\\begin{tabular}{@{}lc@{}}\n\\toprule\nMetric & Value \\\\\n\\midrule\n4-class accuracy (\\%) & 69.52 $[68.9, 70.2]$ \\\\\nBOS-seeded baseline (\\%) & 83.3 \\\\\n$\\Delta$ (prompted $-$ BOS) & $-$13.78\\,pp \\\\\n\\midrule\nAUC d0v1 & 0.916 \\\\\nAUC d1v2 & 0.782 \\\\\nAUC d2v3 & 0.744 \\\\\n\\midrule\nTop-1 feature & \\texttt{p90\\_ppl} \\\\\nTop-2 feature & \\texttt{var\\_surprisal} \\\\\nTop-3 feature & \\texttt{p75\\_ppl} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 13.8\\,pp drop relative to BOS-seeded generation is expected: topic prompts constrain the output distribution, reducing the variance that distinguishes depths.\nNevertheless, accuracy remains $2.8\\times$ chance and pairwise AUC decays monotonically (0.916, 0.782, 0.744); the depth signal is therefore not an artifact of unconstrained generation.\nTop features are identical to BOS-seeded (\\texttt{p90\\_ppl} first); the same perplexity tail erosion mechanism operates under prompted conditions.\n\n\\subsection{Extended Discussion}\n\\label{app:extended_discussion}\n\n\\paragraph{Depth-graduated curation.}\nCurrent data curation operates on a binary human-vs-machine distinction \\cite{dsir2023,qurating2024}.\nRecursive generation depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.\nThe 70--85\\% in-distribution accuracy and $\\mathrm{EDD}_{0.75}{=}4$ suggest depth-graduated filtering is feasible within known model--strategy configurations, though the d1/d2 boundary inversion under cross-strategy transfer (\\S\\ref{sec:gen:crossstrategy}) means reliable curation requires either known decoding strategy metadata or an upstream strategy-identification step; a pilot study (Appendix~\\ref{app:curation_poc}) yields an inconclusive RF-vs-unfiltered comparison ($p>0.4$), though RF-filtered subsets significantly outperform size-matched random subsampling ($p<0.001$--$0.02$); large-scale validation remains open.\nImportance weighting \\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding.\n\n\\paragraph{Toward a provenance toolkit.}\nDepth estimation complements existing provenance methods along orthogonal axes.\nWatermarking \\cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.\nSource attribution \\cite{uchendu2020_attribution} identifies the generating model but not the generation history.\nDepth estimation characterizes \\emph{iterative reuse} regardless of generator cooperation or identity.\nA layered provenance system combining these three signals (watermark presence, source model, and recursive generation depth) could support more nuanced data auditing than any single method.\n\n\\subsection{Computational Resources and Reproducibility}\n\\label{app:compute}\n\n\\paragraph{Hardware.}\nAll experiments were conducted on 2$\\times$ NVIDIA RTX PRO 6000 (48\\,GB) GPUs locally and 2$\\times$ NVIDIA RTX PRO 6000 (48\\,GB) on cloud instances.\nTotal computation is approximately 200 GPU$\\cdot$hours, covering the $3 \\times 3$ generation matrix (LoRA fine-tuning + sampling at each depth), feature extraction, depth extension to d5, 7--8B QLoRA experiments, and all ablations.\n\n\\paragraph{Software.}\nKey library versions: PyTorch 2.10.0+cu128, Transformers 5.8.1, PEFT 0.7.1, scikit-learn 1.8.0.\nAdditional dependencies: Accelerate 1.13.0, Datasets 4.8.4, XGBoost 3.2.0, NumPy 2.2.6 (Python 3.12.3, CUDA 12.8).\n\n\\paragraph{Hyperparameters.}\nLoRA hyperparameters ($r{=}16$, $\\alpha{=}32$, dropout $0.05$, lr $2{\\times}10^{-4}$, batch size 8, 3 epochs) follow \\citet{hu2022lora}.\nThe Random Forest classifier uses 200 trees, Gini criterion, and no max depth, without hyperparameter search; all reported results use 5-fold stratified cross-validation.\n\n\\paragraph{Inference cost.}\nFeature extraction and classification require no GPU.\nInference takes approximately 2 minutes per 5{,}000 samples on a single CPU core (reference-model forward pass + RF prediction), enabling deployment without specialized hardware.\n",
      "numLines": 689,
      "startLine": 1,
      "totalLines": 689
    }
  },
  "sourceToolAssistantUUID": "0b1d696b-5395-47e6-8c9b-5438aed45bb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-18T14:11:08.335Z_

<details open><summary>🔧 Tool call — Read · `toolu_016oemmX4pH8VBimoNjXFB95`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "106ee534-4df1-4422-9eef-ebe80efd144e",
  "isSidechain": false,
  "requestId": "req_011CbAAmYGEvUKzNL8bqZWne",
  "type": "assistant",
  "uuid": "e20fd060-ba29-475a-a1b6-42a5a0eb71e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPHHq3gYENpMxrx56HQeua",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6519,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 31653,
      "output_tokens": 454,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6519,
          "output_tokens": 454,
          "cache_read_input_tokens": 31653,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1449
          },
          "type": "message"
        }
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

_source line 51_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性 + 写作质量**  ### 论文信息 - **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints - **路径**: `proje…",
  "leafUuid": "feb194c8-36aa-4453-a2d6-b5edd0cc3d45",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Review recursive generation depth estimation paper",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Assistant

_source line 53 · 2026-05-18T14:11:14.415Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also read the conclusion.tex file (I already read it above - it's actually the discussion.tex which contains both Discussion and Conclusion, plus Limitations and Ethics). Let me now also check the conclusion.tex separately.

Wait, I already read conclusion.tex. Let me check what it contains.

Actually, looking at main.tex, the order is:
1. abstract
2. introduction
3. related_work
4. method
5. atlas
6. generalization
7. discussion
8. conclusion
9. section_appendix

Let me read conclusion.tex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "feb194c8-36aa-4453-a2d6-b5edd0cc3d45",
  "isSidechain": false,
  "requestId": "req_011CbAAn5J3SaRUgzisbe6wY",
  "type": "assistant",
  "uuid": "180e763c-473b-47c4-b476-eea556cf6912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZpX1XvarzJymMt3u7QFJ1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 45975,
      "cache_read_input_tokens": 33102,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 45975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 33102,
          "cache_creation_input_tokens": 45975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 45975
          },
          "type": "message"
        }
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

_source line 54 · 2026-05-18T14:11:15.821Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N7AQX3aNVGbmE9TB6ZxNBY`</summary>

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
  "parentUuid": "180e763c-473b-47c4-b476-eea556cf6912",
  "isSidechain": false,
  "requestId": "req_011CbAAn5J3SaRUgzisbe6wY",
  "type": "assistant",
  "uuid": "5473f032-85f3-496f-bb90-f6faf2264f16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZpX1XvarzJymMt3u7QFJ1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 45975,
      "cache_read_input_tokens": 33102,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 45975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 33102,
          "cache_creation_input_tokens": 45975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 45975
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-18T14:11:15.825Z_

<details><summary>↩ Tool result · `toolu_01N7AQX3aNVGbmE9TB6ZxNBY`</summary>

```text
File unchanged since last read. The content from the earlier Read tool_result in this conversation is still current — refer to that instead of re-reading.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5473f032-85f3-496f-bb90-f6faf2264f16",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "8e72abfd-8f49-4775-a638-1402e15637a9",
  "toolUseResult": {
    "type": "file_unchanged",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
    }
  },
  "sourceToolAssistantUUID": "5473f032-85f3-496f-bb90-f6faf2264f16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 56 · 2026-05-18T14:11:53.703Z_

<details><summary>Logged reasoning block</summary>

```text
The conclusion.tex file was already read above - it contains the Limitations, Ethics Statement, and what appears to be after the Discussion section in discussion.tex.

Wait, let me re-read discussion.tex and conclusion.tex. The discussion.tex contains "Discussion and Conclusion" (section title), and conclusion.tex contains "Limitations" and "Ethics Statement". That's the structure.

Now let me also run the reference verification tool and check for AI writing style issues (dashes, etc.).

Let me now compile my review. I have read all the paper sections. Let me organize my findings systematically.

## Paper Summary


The paper frames recursive generation depth estimation as an ordinal classification task - predicting how many times a text has been regenerated through language models (d0 for human text, d1 for first generation, etc.). They build a 180K benchmark across 3 model families with different decoding strategies at 4 depth levels, train a Random Forest classifier on 19 perplexity-based features, and achieve 69-86% accuracy on 4-class classification. The work introduces the EDD metric and a "Depth Degradation Atlas" for analysis.

Now I'm assessing the novelty - the core contribution of framing depth estimation as ordinal classification is genuinely new, distinct from prior binary human-vs-machine detection work.  The EDD metric is straightforward and operationally useful but not a major methodological innovation. The method itself relies on standard Random Forest classification with perplexity features, so the contribution is primarily empirical rather than algorithmic. The Depth Degradation Atlas provides interesting empirical findings - particularly the non-monotonic behavior in 7B models and strategy-dependent trajectories - though these largely align with existing model collapse theory predictions.

Looking at the related work, it's well-structured across five sections covering model collapse theory, AI text detection, adjacent tasks, ordinal classification, and decoding strategy effects. The paper positions itself nicely against Dohmatob et al. 2024 by operationalizing their theoretical predictions into a practical ordinal classifier that reveals empirical phenomena the theory doesn't capture. Coverage of ordinal classification literature is solid, pulling from both classical work and recent methods. I'm wondering if there are gaps around multi-class AI text detection approaches, particularly from tasks like SemEval, though the key position papers on model collapse terminology appear to be included.

The abstract is clear and specific with concrete numbers, though it could punch harder in the opening. The introduction flows logically from problem identification through existing gaps to the core insight and method, with a clean contribution list. The writing quality seems solid overall. The discussion section is notably thin—just one paragraph combining discussion and conclusion—which feels like a missed opportunity to dig into implications. The limitations section is thorough and candid, though it cuts off mid-thought.

The paper uses the correct ACL review format with anonymous authorship. References are substantial at 50+. The core methodological concern is that this is essentially random forests with perplexity features, which limits novelty. There's also the d0 inflation problem—since d0 is trivially separable, the headline accuracy numbers mask weaker performance on the harder d1/d2/d3 discrimination task. And there's an incomplete thought about cross-

strategy transfer being poor at 45.9% for d1-d3 versus 33% baseline chance, which undermines practical applicability. The false positive rate on C4 reaching 22.4% is another red flag for real-world deployment, plus the experiments only go up to 1-1.5B models, which feels small for 2026 standards. I should verify the references more carefully and look for specific writing issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e72abfd-8f49-4775-a638-1402e15637a9",
  "isSidechain": false,
  "requestId": "req_011CbAAndBCGjzsTGZj4psdF",
  "type": "assistant",
  "uuid": "282ef026-26d4-437e-b9b2-a373ba497272",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiScmup4uXkFoc5N7tKPXB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 79077,
      "output_tokens": 1689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 275,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1689,
          "cache_read_input_tokens": 79077,
          "cache_creation_input_tokens": 275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 275
          },
          "type": "message"
        }
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

_source line 57 · 2026-05-18T14:11:53.705Z_

现在运行引用审计和检查 AI 写作标记。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "282ef026-26d4-437e-b9b2-a373ba497272",
  "isSidechain": false,
  "requestId": "req_011CbAAndBCGjzsTGZj4psdF",
  "type": "assistant",
  "uuid": "721e7010-4758-46f6-85e1-2b5f601b1384",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiScmup4uXkFoc5N7tKPXB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 79077,
      "output_tokens": 1689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 275,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1689,
          "cache_read_input_tokens": 79077,
          "cache_creation_input_tokens": 275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 275
          },
          "type": "message"
        }
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

_source line 58 · 2026-05-18T14:11:53.712Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01VcBN5ud9fDE7UFxGG4dpG8`</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "721e7010-4758-46f6-85e1-2b5f601b1384",
  "isSidechain": false,
  "requestId": "req_011CbAAndBCGjzsTGZj4psdF",
  "type": "assistant",
  "uuid": "64eeb5b2-d6f6-49b0-8f28-e690ae779b91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiScmup4uXkFoc5N7tKPXB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 79077,
      "output_tokens": 1689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 275,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1689,
          "cache_read_input_tokens": 79077,
          "cache_creation_input_tokens": 275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 275
          },
          "type": "message"
        }
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

_source line 59 · 2026-05-18T14:11:54.579Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Aj8FpnwRVuAhhVjJ3br7Gp`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64eeb5b2-d6f6-49b0-8f28-e690ae779b91",
  "isSidechain": false,
  "requestId": "req_011CbAAndBCGjzsTGZj4psdF",
  "type": "assistant",
  "uuid": "169ef68f-d86a-4c9b-95c4-62223ffa74b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiScmup4uXkFoc5N7tKPXB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 79077,
      "output_tokens": 1689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 275,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1689,
          "cache_read_input_tokens": 79077,
          "cache_creation_input_tokens": 275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 275
          },
          "type": "message"
        }
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

_source line 60 · 2026-05-18T14:11:55.115Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Eq1kyKwSU27JoAyQgZyJcq`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "169ef68f-d86a-4c9b-95c4-62223ffa74b3",
  "isSidechain": false,
  "requestId": "req_011CbAAndBCGjzsTGZj4psdF",
  "type": "assistant",
  "uuid": "61ac72b4-0214-4b50-9beb-07e9e6735abf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiScmup4uXkFoc5N7tKPXB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 79077,
      "output_tokens": 1689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 275,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1689,
          "cache_read_input_tokens": 79077,
          "cache_creation_input_tokens": 275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 275
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-18T14:11:56.829Z_

<details open><summary>🔧 Tool call — Grep · `toolu_014Wez1FjNQKN1rD3uXhoKoD`</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61ac72b4-0214-4b50-9beb-07e9e6735abf",
  "isSidechain": false,
  "requestId": "req_011CbAAndBCGjzsTGZj4psdF",
  "type": "assistant",
  "uuid": "6ea4b513-578d-4951-b7e6-f254c4c108f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiScmup4uXkFoc5N7tKPXB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 79077,
      "output_tokens": 1689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 275,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1689,
          "cache_read_input_tokens": 79077,
          "cache_creation_input_tokens": 275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 275
          },
          "type": "message"
        }
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

_source line 62 · 2026-05-18T14:12:53.366Z_

<details><summary>↩ Tool result · `toolu_01VcBN5ud9fDE7UFxGG4dpG8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 63, \"total_citations\": 89, \"unique_cited_keys\": 60, \"orphan_bib\": 3, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 53, \"online_not_found\": 6, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [\"bevendorff2025_two_paradigms\", \"pareek2024understanding\", \"shi2025_closer_look\"], \"missing_bib\": [], \"orphan_count\": 3, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"shumailov2024_nature\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"type\": \"inproceedings\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, ...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"dohmatob2025_strong_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"dohmatob2024_demystified\", \"type\": \"inproceedings\", \"title\": \"Model Collapse Demystified: The Case of Regression\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\", \"year\": \"2024\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"alemohammad2024_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"gerstgrasser2024_accumulate\", \"type\": \"misc\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"authors\": \"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafae...\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"marchi2024_heat_death\", \"type\": \"inproceedings\", \"title\": \"Heat Death of Generative Models in Closed-Loop Learning\", \"authors\": \"Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo\", \"year\": \"2024\", \"venue\": \"Proceedings of ICASSP\"}, {\"key\": \"knowledge_collapse2025\", \"type\": \"misc\", \"title\": \"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training\", \"authors\": \"Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven,...\", \"year\": \"2025\", \"venue\": \"\"}, {\"key\": \"sigma2026_spectral\", \"type\": \"misc\", \"title\": \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\", \"authors\": \"Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and P...\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\": \"mohamed2025_broken_telephone\", \"type\": \"inproceedings\", \"title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"authors\": \"Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan\", \"year\": \"2025\", \"venue\": \"Proceedings of ACL\"}, {\"key\": \"synthetic_eggs2026\", \"type\": \"inproceedings\", \"title\": \"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning\", \"authors\": \"Schaffelder, Max and Gatt, Albert\", \"year\": \"2026\", \"venue\": \"Findings of ACL\"}, {\"key\": \"shi2025_closer_look\", \"type\": \"inproceedings\", \"title\": \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\", \"authors\": \"Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and ...\", \"year\": \"2025\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"yi2026_escaping_collapse\", \"type\": \"inproceedings\", \"title\": \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\", \"authors\": \"Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng\", \"year\": \"2026\", \"venue\": \"3rd DATA-FM Workshop at ICLR 2026\"}, {\"key\": \"drayson2025_detection_prevents_collapse\", \"type\": \"inproceedings\", \"title\": \"Machine-generated text detection prevents language model collapse\", \"authors\": \"Drayson, George and Yilmaz, Emine and Lampos, Vasileios\", \"year\": \"2025\", \"venue\": \"Findings of EMNLP\"}, {\"key\": \"bakshi2026_collapse_improvement\", \"type\": \"misc\", \"title\": \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminate...\", \"authors\": \"Bakshi, Soham and Chakraborty, Sunrit\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\": \"wang2026_contamination\", \"type\": \"misc\", \"title\": \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive T...\", \"authors\": \"Wang, Kevin and Niu, Hongqian and Li, Didong\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\": \"falahati2026_curated\", \"type\": \"misc\", \"title\": \"Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferenc...\", \"authors\": \"Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\": \"wu2025_detection_survey\", \"type\": \"article\", \"title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"authors\": \"Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam a...\", \"year\": \"2025\", \"venue\": \"Computational Linguistics\"}, {\"key\": \"gehrmann2019_gltr\", \"type\": \"inproceedings\", \"title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"authors\": \"Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.\", \"year\": \"2019\", \"venue\": \"Proceedings of ACL: System Demonstrations\"}, {\"key\": \"mitchell2023_detectgpt\", \"type\": \"inproceedings\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"authors\": \"Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher...\", \"year\": \"2023\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"fast_detectgpt2024\", \"type\": \"inproceedings\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"authors\": \"Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yu...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"binoculars2024\", \"type\": \"inproceedings\", \"title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"authors\": \"Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Ham...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"diveye2026\", \"type\": \"article\", \"title\": \"Diversity Boosts AI-Generated Text Detection\", \"authors\": \"Basani, Advik Raj and Chen, Pin-Yu\", \"year\": \"2026\", \"venue\": \"Transactions on Machine Learning Research (TMLR)\"}, {\"key\": \"sadasivan2023_paraphrase\", \"type\": \"misc\", \"title\": \"Can AI-Generated Text be Reliably Detected?\", \"authors\": \"Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, W...\", \"year\": \"2023\", \"venue\": \"\"}, {\"key\": \"pudasaini2026_detection_fails\", \"type\": \"misc\", \"title\": \"Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy\", \"authors\": \"Pudasaini, Shushanta and Miralles-Pech\\\\'uan, Luis and Lillis, David and Llorens ...\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\": \"pu2026_generator_barrier\", \"type\": \"misc\", \"title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"authors\": \"Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\": \"bevendorff2025_two_paradigms\", \"type\": \"inproceedings\", \"title\": \"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\", \"authors\": \"Bevendorff, Janek and Wiegmann, Matti and Richter, Emmelie and Potthast, Martin ...\", \"year\": \"2025\", \"venue\": \"Findings of ACL\"}, {\"key\": \"uchendu2020_attribution\", \"type\": \"inproceedings\", \"title\": \"Authorship Attribution for Neural Text Generation\", \"authors\": \"Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon\", \"year\": \"2020\", \"venue\": \"Proceedings of EMNLP\"}, {\"key\": \"editlens2026\", \"type\": \"inproceedings\", \"title\": \"EditLens: Quantifying the Extent of AI Editing in Text\", \"authors\": \"Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit\", \"year\": \"2026\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"loki2025\", \"type\": \"inproceedings\", \"title\": \"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\", \"authors\": \"Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi...\", \"year\": \"2025\", \"venue\": \"Proceedings of ICLR (Spotlight)\"}, {\"key\": \"tulchinskii2023_intrinsic_dim\", \"type\": \"inproceedings\", \"title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"authors\": \"Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavsk...\", \"year\": \"2023\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"verma2024_ghostbuster\", \"type\": \"inproceedings\", \"title\": \"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\", \"authors\": \"Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan\", \"year\": \"2024\", \"venue\": \"Proceedings of NAACL\"}, {\"key\": \"wang2024_m4_semeval\", \"type\": \"inproceedings\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"authors\": \"Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2...\"}, {\"key\": \"li2024_mage\", \"type\": \"inproceedings\", \"title\": \"MAGE: Machine-generated Text Detection in the Wild\", \"authors\": \"Li, Yongkang and Li, Donghao and Yang, Yue and Hu, Baotian and Zhang, Min\", \"year\": \"2024\", \"venue\": \"Proceedings of ACL\"}, {\"key\": \"yang2024_dnagpt\", \"type\": \"inproceedings\", \"title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"authors\": \"Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Ya...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"kirchenbauer2023_watermark\", \"type\": \"inproceedings\", \"title\": \"A Watermark for Large Language Models\", \"authors\": \"Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Mier...\", \"year\": \"2023\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"holtzman2020_nucleus\", \"type\": \"inproceedings\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"authors\": \"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\", \"year\": \"2020\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"finlayson2024_closing\", \"type\": \"inproceedings\", \"title\": \"Closing the Curious Case of Neural Text Degeneration\", \"authors\": \"Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabh...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"garces_arias2025_decoding_decoded\", \"type\": \"inproceedings\", \"title\": \"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation\", \"authors\": \"Garces Arias, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher,...\", \"year\": \"2025\", \"venue\": \"Proceedings of COLING\"}, {\"key\": \"wiher2022_decoding\", \"type\": \"article\", \"title\": \"On Decoding Strategies for Neural Text Generators\", \"authors\": \"Wiher, Gian and Meister, Clara and Cotterell, Ryan\", \"year\": \"2022\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"basu2021_mirostat\", \"type\": \"inproceedings\", \"title\": \"Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity\", \"authors\": \"Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shiris...\", \"year\": \"2021\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"coral2020\", \"type\": \"article\", \"title\": \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\", \"authors\": \"Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian\", \"year\": \"2020\", \"venue\": \"Pattern Recognition Letters\"}, {\"key\": \"cloc2025\", \"type\": \"inproceedings\", \"title\": \"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\", \"authors\": \"Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting\", \"year\": \"2025\", \"venue\": \"Proceedings of CVPR\"}, {\"key\": \"hu2022lora\", \"type\": \"inproceedings\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"authors\": \"Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li,...\", \"year\": \"2022\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"he2021_deberta_v3\", \"type\": \"inproceedings\", \"title\": \"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing\", \"authors\": \"He, Pengcheng and Gao, Jianfeng and Chen, Weizhu\", \"year\": \"2023\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"liu2019_roberta\", \"type\": \"misc\", \"title\": \"RoBERTa: A Robustly Optimized BERT Pretraining Approach\", \"authors\": \"Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and...\", \"year\": \"2019\", \"venue\": \"\"}, {\"key\": \"dsir2023\", \"type\": \"inproceedings\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"authors\": \"Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\", \"year\": \"2023\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"qurating2024\", \"type\": \"inproceedings\", \"title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"authors\": \"Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"penedo2024_fineweb\", \"type\": \"inproceedings\", \"title\": \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\", \"authors\": \"\", \"year\": \"2024\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"sugiyama2007_importance_weighting\", \"type\": \"article\", \"title\": \"Covariate Shift Adaptation by Importance Weighted Cross Validation\", \"authors\": \"Sugiyama, Masashi and Krauledat, Matthias and M\\\\\\\"uller, Klaus-Robert\", \"year\": \"2007\", \"venue\": \"Journal of Machine Learning Research\"}, {\"key\": \"qwen2.5\", \"type\": \"misc\", \"title\": \"Qwen2.5: A Party of Foundation Models\", \"authors\": \"Qwen Team\", \"year\": \"2025\", \"venue\": \"\"}, {\"key\": \"llama3\", \"type\": \"misc\", \"title\": \"The Llama 3 Herd of Models\", \"authors\": \"Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav ...\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"schaeffer2025\", \"type\": \"misc\", \"title\": \"Position: Model Collapse Does Not Mean What You Think\", \"authors\": \"Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi\", \"year\": \"2025\", \"venue\": \"\"}, {\"key\": \"frank2001\", \"type\": \"inproceedings\", \"title\": \"A Simple Approach to Ordinal Classification\", \"authors\": \"Frank, Eibe and Hall, Mark\", \"year\": \"2001\", \"venue\": \"Proceedings of ECML\"}, {\"key\": \"rennie2005\", \"type\": \"inproceedings\", \"title\": \"Loss Functions for Preference Levels: Regression with Discrete Ordered Labels\", \"authors\": \"Rennie, Jason D. M. and Srebro, Nathan\", \"year\": \"2005\", \"venue\": \"Proceedings of IJCAI Workshop on Advances in Preference Handling\"}, {\"key\": \"mccullagh1980_ordinal\", \"type\": \"article\", \"title\": \"Regression Models for Ordinal Data\", \"authors\": \"McCullagh, Peter\", \"year\": \"1980\", \"venue\": \"Journal of the Royal Statistical Society: Series B\"}, {\"key\": \"wenzek2020_ccnet\", \"type\": \"inproceedings\", \"title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"authors\": \"Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vis...\", \"year\": \"2020\", \"venue\": \"Proceedings of LREC\"}, {\"key\": \"dugan2024_raid\", \"type\": \"inproceedings\", \"title\": \"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors\", \"authors\": \"Dugan, Liam and Hwang, Alyssa and Trhl\\\\'\\\\ik, Filip and Zhu, Andrew and Ludan, Jo...\", \"year\": \"2024\", \"venue\": \"Proceedings of ACL\"}, {\"key\": \"guo2024curious\", \"type\": \"inproceedings\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"authors\": \"Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\\\'e\", \"year\": \"2024\", \"venue\": \"Findings of NAACL\"}, {\"key\": \"padmakumar2024diversity\", \"type\": \"inproceedings\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"authors\": \"Padmakumar, Vishakh and He, He\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"briesch2024selfconsuming\", \"type\": \"misc\", \"title\": \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\", \"authors\": \"Briesch, Martin and Sobania, Dominik and Rothlauf, Franz\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"seddik2024synthetic\", \"type\": \"misc\", \"title\": \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\", \"authors\": \"Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pie...\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"pareek2024understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Gains from Repeated Self-Distillation\", \"authors\": \"Pareek, Divyansh and Du, Simon S. and Oh, Sewoong\", \"year\": \"2024\", \"venue\": \"Proceedings of NeurIPS\"}], \"tex_citations\": [{\"key\": \"shumailov2024_nature\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"alemohammad2024_mad\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"binoculars2024\", \"file\": \"introduction.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt2024\", \"file\": \"introduction.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"diveye2026\", \"file\": \"introduction.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"kirchenbauer2023_watermark\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"shumailov2024_nature\", \"file\": \"introduction.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"file\": \"introduction.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"drayson2025_detection_prevents_collapse\", \"file\": \"introduction.tex\", \"line\": 11, \"command\": \"citet\"}, {\"key\": \"shumailov2024_nature\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"seddik2024synthetic\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"dohmatob2025_strong_collapse\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"alemohammad2024_mad\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gerstgrasser2024_accumulate\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"drayson2025_detection_prevents_collapse\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"yi2026_escaping_collapse\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"falahati2026_curated\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"wenzek2020_ccnet\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"bakshi2026_collapse_improvement\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"marchi2024_heat_death\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"wang2026_contamination\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"knowledge_collapse2025\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"dohmatob2024_demystified\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"guo2024curious\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"briesch2024selfconsuming\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"padmakumar2024diversity\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"sigma2026_spectral\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"synthetic_eggs2026\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"schaeffer2025\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"wu2025_detection_survey\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"mitchell2023_detectgpt\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt2024\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"binoculars2024\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"diveye2026\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"gehrmann2019_gltr\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"verma2024_ghostbuster\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"yang2024_dnagpt\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"tulchinskii2023_intrinsic_dim\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"kirchenbauer2023_watermark\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"sadasivan2023_paraphrase\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"pudasaini2026_detection_fails\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"pu2026_generator_barrier\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"wang2024_m4_semeval\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"dugan2024_raid\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"li2024_mage\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"editlens2026\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"uchendu2020_attribution\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"citet\"}, {\"key\": \"loki2025\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"mohamed2025_broken_telephone\", \"file\": \"related_work.tex\", \"line\": 18, \"command\": \"citet\"}, {\"key\": \"mccullagh1980_ordinal\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"frank2001\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citet\"}, {\"key\": \"rennie2005\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citet\"}, {\"key\": \"coral2020\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"cloc2025\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"holtzman2020_nucleus\", \"file\": \"related_work.tex\", \"line\": 27, \"command\": \"cite\"}, {\"key\": \"finlayson2024_closing\", \"file\": \"related_work.tex\", \"line\": 27, \"command\": \"cite\"}, {\"key\": \"garces_arias2025_decoding_decoded\", \"file\": \"related_work.tex\", \"line\": 27, \"command\": \"cite\"}, {\"key\": \"wiher2022_decoding\", \"file\": \"related_work.tex\", \"line\": 27, \"command\": \"cite\"}, {\"key\": \"basu2021_mirostat\", \"file\": \"related_work.tex\", \"line\": 27, \"command\": \"cite\"}, {\"key\": \"holtzman2020_nucleus\", \"file\": \"method.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"hu2022lora\", \"file\": \"method.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"coral2020\", \"file\": \"method.tex\", \"line\": 104, \"command\": \"cite\"}, {\"key\": \"diveye2026\", \"file\": \"method.tex\", \"line\": 104, \"command\": \"cite\"}, {\"key\": \"shumailov2024_nature\", \"file\": \"atlas.tex\", \"line\": 62, \"command\": \"cite\"}, {\"key\": \"shumailov2024_nature\", \"file\": \"atlas.tex\", \"line\": 170, \"command\": \"cite\"}, {\"key\": \"coral2020\", \"file\": \"generalization.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"diveye2026\", \"file\": \"generalization.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"llama3\", \"file\": \"generalization.tex\", \"line\": 104, \"command\": \"cite\"}, {\"key\": \"qwen2.5\", \"file\": \"generalization.tex\", \"line\": 104, \"command\": \"cite\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"file\": \"discussion.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"penedo2024_fineweb\", \"file\": \"conclusion.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"sadasivan2023_paraphrase\", \"file\": \"conclusion.tex\", \"line\": 30, \"command\": \"cite\"}, {\"key\": \"bakshi2026_collapse_improvement\", \"file\": \"conclusion.tex\", \"line\": 34, \"command\": \"citet\"}, {\"key\": \"pudasaini2026_detection_fails\", \"file\": \"conclusion.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"falahati2026_curated\", \"file\": \"conclusion.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"he2021_deberta_v3\", \"file\": \"section_appendix.tex\", \"line\": 161, \"command\": \"cite\"}, {\"key\": \"liu2019_roberta\", \"file\": \"section_appendix.tex\", \"line\": 161, \"command\": \"cite\"}, {\"key\": \"cloc2025\", \"file\": \"section_appendix.tex\", \"line\": 187, \"command\": \"cite\"}, {\"key\": \"binoculars2024\", \"file\": \"section_appendix.tex\", \"line\": 617, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt2024\", \"file\": \"section_appendix.tex\", \"line\": 617, \"command\": \"cite\"}, {\"key\": \"dsir2023\", \"file\": \"section_appendix.tex\", \"line\": 659, \"command\": \"cite\"}, {\"key\": \"qurating2024\", \"file\": \"section_appendix.tex\", \"line\": 659, \"command\": \"cite\"}, {\"key\": \"sugiyama2007_importance_weighting\", \"file\": \"section_appendix.tex\", \"line\": 662, \"command\": \"cite\"}, {\"key\": \"kirchenbauer2023_watermark\", \"file\": \"section_appendix.tex\", \"line\": 666, \"command\": \"cite\"}, {\"key\": \"uchendu2020_attribution\", \"file\": \"section_appendix.tex\", \"line\": 667, \"command\": \"cite\"}, {\"key\": \"hu2022lora\", \"file\": \"section_appendix.tex\", \"line\": 683, \"command\": \"citet\"}], \"online_verification\": [{\"key\": \"shumailov2024_nature\", \"title\": \"AI models collapse when trained on recursively generated data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"AI models collapse when trained on recursively generated data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dohmatob2025_strong_collapse\", \"title\": \"Strong Model Collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Strong Model Collapse\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dohmatob2024_demystified\", \"title\": \"Model Collapse Demystified: The Case of Regression\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Model Collapse Demystified: The Case of Regression\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"alemohammad2024_mad\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Self-Consuming Generative Models go MAD\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=alemohammad vs api=casco-rodriguez\"], \"note\": \"\"}, {\"key\": \"gerstgrasser2024_accumulate\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"marchi2024_heat_death\", \"title\": \"Heat Death of Generative Models in Closed-Loop Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Heat Death of Generative Models in Closed-Loop Learning\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"knowledge_collapse2025\", \"title\": \"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training\", \"status\": \"not_found\", \"confidence\": 0.288, \"matched_title\": \"A predictive human model of language challenges traditional views in linguistics and pretrained transformer research\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.29 below threshold 0.82\"}, {\"key\": \"sigma2026_spectral\", \"title\": \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mohamed2025_broken_telephone\", \"title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"synthetic_eggs2026\", \"title\": \"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shi2025_closer_look\", \"title\": \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yi2026_escaping_collapse\", \"title\": \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"drayson2025_detection_prevents_collapse\", \"title\": \"Machine-generated text detection prevents language model collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Machine-generated text detection prevents language model collapse\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bakshi2026_collapse_improvement\", \"title\": \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2026_contamination\", \"title\": \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"falahati2026_curated\", \"title\": \"Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences\", \"status\": \"not_found\", \"confidence\": 0.0, \"matched_title\": \"\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"no results from OpenAlex\"}, {\"key\": \"wu2025_detection_survey\", \"title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gehrmann2019_gltr\", \"title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mitchell2023_detectgpt\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"status\": \"not_found\", \"confidence\": 0.382, \"matched_title\": \"Regulating ChatGPT and other Large Generative AI Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.38 below threshold 0.82\"}, {\"key\": \"fast_detectgpt2024\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"binoculars2024\", \"title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"diveye2026\", \"title\": \"Diversity Boosts AI-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Diversity Boosts AI-Generated Text Detection\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sadasivan2023_paraphrase\", \"title\": \"Can AI-Generated Text be Reliably Detected?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Can AI-Generated Text be Reliably Detected?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"pudasaini2026_detection_fails\", \"title\": \"Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"pu2026_generator_barrier\", \"title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bevendorff2025_two_paradigms\", \"title\": \"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"uchendu2020_attribution\", \"title\": \"Authorship Attribution for Neural Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Authorship Attribution for Neural Text Generation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"editlens2026\", \"title\": \"EditLens: Quantifying the Extent of AI Editing in Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"EditLens: Quantifying the Extent of AI Editing in Text\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"loki2025\", \"title\": \"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tulchinskii2023_intrinsic_dim\", \"title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"verma2024_ghostbuster\", \"title\": \"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2024_m4_semeval\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2024_mage\", \"title\": \"MAGE: Machine-generated Text Detection in the Wild\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MAGE: Machine-generated Text Detection in the Wild\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yang2024_dnagpt\", \"title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kirchenbauer2023_watermark\", \"title\": \"A Watermark for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Watermark for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"holtzman2020_nucleus\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Case of Neural Text Degeneration\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"finlayson2024_closing\", \"title\": \"Closing the Curious Case of Neural Text Degeneration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Closing the Curious Case of Neural Text Degeneration\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"garces_arias2025_decoding_decoded\", \"title\": \"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=garces arias vs api=arias\"], \"note\": \"\"}, {\"key\": \"wiher2022_decoding\", \"title\": \"On Decoding Strategies for Neural Text Generators\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Decoding Strategies for Neural Text Generators\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"basu2021_mirostat\", \"title\": \"Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"coral2020\", \"title\": \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rank consistent ordinal regression for neural networks with application to age estimation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cloc2025\", \"title\": \"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hu2022lora\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"he2021_deberta_v3\", \"title\": \"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing\", \"matched_year\": \"2021\", \"mismatch_fields\": [\"year: bib=2023 vs api=2021\"], \"note\": \"\"}, {\"key\": \"liu2019_roberta\", \"title\": \"RoBERTa: A Robustly Optimized BERT Pretraining Approach\", \"status\": \"not_found\", \"confidence\": 0.495, \"matched_title\": \"Use of Bidirectional Encoder Representations from Transformers (BERT) and Robustly Optimized Bert Pretraining Approach (RoBERTa) for Nepali News Classification\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.50 below threshold 0.82\"}, {\"key\": \"dsir2023\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Data Selection for Language Models via Importance Resampling\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qurating2024\", \"title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"penedo2024_fineweb\", \"title\": \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sugiyama2007_importance_weighting\", \"title\": \"Covariate Shift Adaptation by Importance Weighted Cross Validation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Covariate Shift Adaptation by Importance Weighted Cross Validation\", \"matched_year\": \"2007\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen2.5\", \"title\": \"Qwen2.5: A Party of Foundation Models\", \"status\": \"not_found\", \"confidence\": 0.333, \"matched_title\": \"Can Open Large Language Models Catch Vulnerabilities?\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"llama3\", \"title\": \"The Llama 3 Herd of Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"The Llama 3 herd of models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=grattafiori vs api=aaron\"], \"note\": \"\"}, {\"key\": \"schaeffer2025\", \"title\": \"Position: Model Collapse Does Not Mean What You Think\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Position: Model Collapse Does Not Mean What You Think\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"frank2001\", \"title\": \"A Simple Approach to Ordinal Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Simple Approach to Ordinal Classification\", \"matched_year\": \"2001\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"rennie2005\", \"title\": \"Loss Functions for Preference Levels: Regression with Discrete Ordered Labels\", \"status\": \"not_found\", \"confidence\": 0.373, \"matched_title\": \"Ordinal Regression Methods: Survey and Experimental Study\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.37 below threshold 0.82\"}, {\"key\": \"mccullagh1980_ordinal\", \"title\": \"Regression Models for Ordinal Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Regression Models for Ordinal Data\", \"matched_year\": \"1980\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wenzek2020_ccnet\", \"title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dugan2024_raid\", \"title\": \"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2024curious\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"padmakumar2024diversity\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"briesch2024selfconsuming\", \"title\": \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"seddik2024synthetic\", \"title\": \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"pareek2024understanding\", \"title\": \"Understanding the Gains from Repeated Self-Distillation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Gains from Repeated Self-Distillation\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64eeb5b2-d6f6-49b0-8f28-e690ae779b91",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "7dcd7524-57e2-4791-93ec-b185af713de3",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 63, \\\"total_citations\\\": 89, \\\"unique_cited_keys\\\": 60, \\\"orphan_bib\\\": 3, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 53, \\\"online_not_found\\\": 6, \\\"online_mismatch\\\": 4}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [\\\"bevendorff2025_two_paradigms\\\", \\\"pareek2024understanding\\\", \\\"shi2025_closer_look\\\"], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 3, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"shumailov2024_nature\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"AI models collapse when trained on recursively generated data\\\", \\\"authors\\\": \\\"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Nature\\\"}, {\\\"key\\\": \\\"dohmatob2024_tale_of_tails\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\", \\\"authors\\\": \\\"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of ICML\\\"}, {\\\"key\\\": \\\"dohmatob2025_strong_collapse\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Strong Model Collapse\\\", \\\"authors\\\": \\\"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of ICLR\\\"}, {\\\"key\\\": \\\"dohmatob2024_demystified\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Model Collapse Demystified: The Case of Regression\\\", \\\"authors\\\": \\\"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of NeurIPS\\\"}, {\\\"key\\\": \\\"alemohammad2024_mad\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Consuming Generative Models Go MAD\\\", \\\"authors\\\": \\\"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of ICLR\\\"}, {\\\"key\\\": \\\"gerstgrasser2024_accumulate\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\", \\\"authors\\\": \\\"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafae...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"marchi2024_heat_death\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Heat Death of Generative Models in Closed-Loop Learning\\\", \\\"authors\\\": \\\"Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of ICASSP\\\"}, {\\\"key\\\": \\\"knowledge_collapse2025\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training\\\", \\\"authors\\\": \\\"Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven,...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"sigma2026_spectral\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\", \\\"authors\\\": \\\"Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and P...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"mohamed2025_broken_telephone\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LLM as a Broken Telephone: Iterative Generation Distorts Information\\\", \\\"authors\\\": \\\"Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of ACL\\\"}, {\\\"key\\\": \\\"synthetic_eggs2026\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning\\\", \\\"authors\\\": \\\"Schaffelder, Max and Gatt, Albert\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Findings of ACL\\\"}, {\\\"key\\\": \\\"shi2025_closer_look\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\", \\\"authors\\\": \\\"Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of NeurIPS\\\"}, {\\\"key\\\": \\\"yi2026_escaping_collapse\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\\\", \\\"authors\\\": \\\"Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"3rd DATA-FM Workshop at ICLR 2026\\\"}, {\\\"key\\\": \\\"drayson2025_detection_prevents_collapse\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Machine-generated text detection prevents language model collapse\\\", \\\"authors\\\": \\\"Drayson, George and Yilmaz, Emine and Lampos, Vasileios\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of EMNLP\\\"}, {\\\"key\\\": \\\"bakshi2026_collapse_improvement\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminate...\\\", \\\"authors\\\": \\\"Bakshi, Soham and Chakraborty, Sunrit\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2026_contamination\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive T...\\\", \\\"authors\\\": \\\"Wang, Kevin and Niu, Hongqian and Li, Didong\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"falahati2026_curated\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferenc...\\\", \\\"authors\\\": \\\"Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"wu2025_detection_survey\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\\\", \\\"authors\\\": \\\"Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam a...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Computational Linguistics\\\"}, {\\\"key\\\": \\\"gehrmann2019_gltr\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\", \\\"authors\\\": \\\"Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of ACL: System Demonstrations\\\"}, {\\\"key\\\": \\\"mitchell2023_detectgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\", \\\"authors\\\": \\\"Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of ICML\\\"}, {\\\"key\\\": \\\"fast_detectgpt2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\", \\\"authors\\\": \\\"Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yu...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of ICLR\\\"}, {\\\"key\\\": \\\"binoculars2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\", \\\"authors\\\": \\\"Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Ham...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of ICML\\\"}, {\\\"key\\\": \\\"diveye2026\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Diversity Boosts AI-Generated Text Detection\\\", \\\"authors\\\": \\\"Basani, Advik Raj and Chen, Pin-Yu\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Transactions on Machine Learning Research (TMLR)\\\"}, {\\\"key\\\": \\\"sadasivan2023_paraphrase\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"Can AI-Generated Text be Reliably Detected?\\\", \\\"authors\\\": \\\"Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, W...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"pudasaini2026_detection_fails\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy\\\", \\\"authors\\\": \\\"Pudasaini, Shushanta and Miralles-Pech\\\\\\\\'uan, Luis and Lillis, David and Llorens ...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"pu2026_generator_barrier\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\", \\\"authors\\\": \\\"Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"bevendorff2025_two_paradigms\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\\\", \\\"authors\\\": \\\"Bevendorff, Janek and Wiegmann, Matti and Richter, Emmelie and Potthast, Martin ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of ACL\\\"}, {\\\"key\\\": \\\"uchendu2020_attribution\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Authorship Attribution for Neural Text Generation\\\", \\\"authors\\\": \\\"Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of EMNLP\\\"}, {\\\"key\\\": \\\"editlens2026\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"EditLens: Quantifying the Extent of AI Editing in Text\\\", \\\"authors\\\": \\\"Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Proceedings of ICLR\\\"}, {\\\"key\\\": \\\"loki2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\\\", \\\"authors\\\": \\\"Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of ICLR (Spotlight)\\\"}, {\\\"key\\\": \\\"tulchinskii2023_intrinsic_dim\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\\\", \\\"authors\\\": \\\"Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavsk...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of NeurIPS\\\"}, {\\\"key\\\": \\\"verma2024_ghostbuster\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\\\", \\\"authors\\\": \\\"Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of NAACL\\\"}, {\\\"key\\\": \\\"wang2024_m4_semeval\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\\\", \\\"authors\\\": \\\"Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2...\\\"}, {\\\"key\\\": \\\"li2024_mage\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"MAGE: Machine-generated Text Detection in the Wild\\\", \\\"authors\\\": \\\"Li, Yongkang and Li, Donghao and Yang, Yue and Hu, Baotian and Zhang, Min\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of ACL\\\"}, {\\\"key\\\": \\\"yang2024_dnagpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\", \\\"authors\\\": \\\"Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Ya...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of ICLR\\\"}, {\\\"key\\\": \\\"kirchenbauer2023_watermark\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Watermark for Large Language Models\\\", \\\"authors\\\": \\\"Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Mier...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of ICML\\\"}, {\\\"key\\\": \\\"holtzman2020_nucleus\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"authors\\\": \\\"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of ICLR\\\"}, {\\\"key\\\": \\\"finlayson2024_closing\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Closing the Curious Case of Neural Text Degeneration\\\", \\\"authors\\\": \\\"Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabh...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of ICLR\\\"}, {\\\"key\\\": \\\"garces_arias2025_decoding_decoded\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation\\\", \\\"authors\\\": \\\"Garces Arias, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher,...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of COLING\\\"}, {\\\"key\\\": \\\"wiher2022_decoding\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"On Decoding Strategies for Neural Text Generators\\\", \\\"authors\\\": \\\"Wiher, Gian and Meister, Clara and Cotterell, Ryan\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"basu2021_mirostat\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity\\\", \\\"authors\\\": \\\"Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shiris...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of ICLR\\\"}, {\\\"key\\\": \\\"coral2020\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\\\", \\\"authors\\\": \\\"Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Pattern Recognition Letters\\\"}, {\\\"key\\\": \\\"cloc2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\\\", \\\"authors\\\": \\\"Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of CVPR\\\"}, {\\\"key\\\": \\\"hu2022lora\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LoRA: Low-Rank Adaptation of Large Language Models\\\", \\\"authors\\\": \\\"Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li,...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of ICLR\\\"}, {\\\"key\\\": \\\"he2021_deberta_v3\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing\\\", \\\"authors\\\": \\\"He, Pengcheng and Gao, Jianfeng and Chen, Weizhu\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of ICLR\\\"}, {\\\"key\\\": \\\"liu2019_roberta\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"RoBERTa: A Robustly Optimized BERT Pretraining Approach\\\", \\\"authors\\\": \\\"Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"dsir2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Data Selection for Language Models via Importance Resampling\\\", \\\"authors\\\": \\\"Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of NeurIPS\\\"}, {\\\"key\\\": \\\"qurating2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"QuRating: Selecting High-Quality Data for Training Language Models\\\", \\\"authors\\\": \\\"Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of ICML\\\"}, {\\\"key\\\": \\\"penedo2024_fineweb\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\\\", \\\"authors\\\": \\\"\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of NeurIPS\\\"}, {\\\"key\\\": \\\"sugiyama2007_importance_weighting\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Covariate Shift Adaptation by Importance Weighted Cross Validation\\\", \\\"authors\\\": \\\"Sugiyama, Masashi and Krauledat, Matthias and M\\\\\\\\\\\\\\\"uller, Klaus-Robert\\\", \\\"year\\\": \\\"2007\\\", \\\"venue\\\": \\\"Journal of Machine Learning Research\\\"}, {\\\"key\\\": \\\"qwen2.5\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"Qwen2.5: A Party of Foundation Models\\\", \\\"authors\\\": \\\"Qwen Team\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"llama3\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"The Llama 3 Herd of Models\\\", \\\"authors\\\": \\\"Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"schaeffer2025\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"Position: Model Collapse Does Not Mean What You Think\\\", \\\"authors\\\": \\\"Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"frank2001\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Simple Approach to Ordinal Classification\\\", \\\"authors\\\": \\\"Frank, Eibe and Hall, Mark\\\", \\\"year\\\": \\\"2001\\\", \\\"venue\\\": \\\"Proceedings of ECML\\\"}, {\\\"key\\\": \\\"rennie2005\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Loss Functions for Preference Levels: Regression with Discrete Ordered Labels\\\", \\\"authors\\\": \\\"Rennie, Jason D. M. and Srebro, Nathan\\\", \\\"year\\\": \\\"2005\\\", \\\"venue\\\": \\\"Proceedings of IJCAI Workshop on Advances in Preference Handling\\\"}, {\\\"key\\\": \\\"mccullagh1980_ordinal\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Regression Models for Ordinal Data\\\", \\\"authors\\\": \\\"McCullagh, Peter\\\", \\\"year\\\": \\\"1980\\\", \\\"venue\\\": \\\"Journal of the Royal Statistical Society: Series B\\\"}, {\\\"key\\\": \\\"wenzek2020_ccnet\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\\\", \\\"authors\\\": \\\"Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vis...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of LREC\\\"}, {\\\"key\\\": \\\"dugan2024_raid\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors\\\", \\\"authors\\\": \\\"Dugan, Liam and Hwang, Alyssa and Trhl\\\\\\\\'\\\\\\\\ik, Filip and Zhu, Andrew and Ludan, Jo...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of ACL\\\"}, {\\\"key\\\": \\\"guo2024curious\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\", \\\"authors\\\": \\\"Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\\\\\\\'e\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of NAACL\\\"}, {\\\"key\\\": \\\"padmakumar2024diversity\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Does Writing with Language Models Reduce Content Diversity?\\\", \\\"authors\\\": \\\"Padmakumar, Vishakh and He, He\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of ICLR\\\"}, {\\\"key\\\": \\\"briesch2024selfconsuming\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\", \\\"authors\\\": \\\"Briesch, Martin and Sobania, Dominik and Rothlauf, Franz\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"seddik2024synthetic\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\\\", \\\"authors\\\": \\\"Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pie...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"pareek2024understanding\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Understanding the Gains from Repeated Self-Distillation\\\", \\\"authors\\\": \\\"Pareek, Divyansh and Du, Simon S. and Oh, Sewoong\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of NeurIPS\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"shumailov2024_nature\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"alemohammad2024_mad\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dohmatob2024_tale_of_tails\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"binoculars2024\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fast_detectgpt2024\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"diveye2026\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kirchenbauer2023_watermark\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shumailov2024_nature\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dohmatob2024_tale_of_tails\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"drayson2025_detection_prevents_collapse\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"shumailov2024_nature\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"dohmatob2024_tale_of_tails\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"seddik2024synthetic\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dohmatob2025_strong_collapse\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"alemohammad2024_mad\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gerstgrasser2024_accumulate\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"drayson2025_detection_prevents_collapse\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"yi2026_escaping_collapse\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"falahati2026_curated\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wenzek2020_ccnet\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"bakshi2026_collapse_improvement\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"marchi2024_heat_death\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2026_contamination\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"knowledge_collapse2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dohmatob2024_demystified\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"guo2024curious\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"briesch2024selfconsuming\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"padmakumar2024diversity\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sigma2026_spectral\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"synthetic_eggs2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"schaeffer2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"dohmatob2024_tale_of_tails\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wu2025_detection_survey\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"mitchell2023_detectgpt\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fast_detectgpt2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"binoculars2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"diveye2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gehrmann2019_gltr\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"verma2024_ghostbuster\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"yang2024_dnagpt\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tulchinskii2023_intrinsic_dim\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kirchenbauer2023_watermark\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sadasivan2023_paraphrase\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"pudasaini2026_detection_fails\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"pu2026_generator_barrier\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2024_m4_semeval\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dugan2024_raid\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2024_mage\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"editlens2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"uchendu2020_attribution\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"loki2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"mohamed2025_broken_telephone\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"mccullagh1980_ordinal\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"frank2001\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"rennie2005\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"coral2020\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cloc2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"holtzman2020_nucleus\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"finlayson2024_closing\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"garces_arias2025_decoding_decoded\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wiher2022_decoding\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"basu2021_mirostat\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"holtzman2020_nucleus\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hu2022lora\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"coral2020\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 104, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"diveye2026\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 104, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shumailov2024_nature\\\", \\\"file\\\": \\\"atlas.tex\\\", \\\"line\\\": 62, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shumailov2024_nature\\\", \\\"file\\\": \\\"atlas.tex\\\", \\\"line\\\": 170, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"coral2020\\\", \\\"file\\\": \\\"generalization.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"diveye2026\\\", \\\"file\\\": \\\"generalization.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"llama3\\\", \\\"file\\\": \\\"generalization.tex\\\", \\\"line\\\": 104, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"qwen2.5\\\", \\\"file\\\": \\\"generalization.tex\\\", \\\"line\\\": 104, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dohmatob2024_tale_of_tails\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"penedo2024_fineweb\\\", \\\"file\\\": \\\"conclusion.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sadasivan2023_paraphrase\\\", \\\"file\\\": \\\"conclusion.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"bakshi2026_collapse_improvement\\\", \\\"file\\\": \\\"conclusion.tex\\\", \\\"line\\\": 34, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"pudasaini2026_detection_fails\\\", \\\"file\\\": \\\"conclusion.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"falahati2026_curated\\\", \\\"file\\\": \\\"conclusion.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"he2021_deberta_v3\\\", \\\"file\\\": \\\"section_appendix.tex\\\", \\\"line\\\": 161, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"liu2019_roberta\\\", \\\"file\\\": \\\"section_appendix.tex\\\", \\\"line\\\": 161, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cloc2025\\\", \\\"file\\\": \\\"section_appendix.tex\\\", \\\"line\\\": 187, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"binoculars2024\\\", \\\"file\\\": \\\"section_appendix.tex\\\", \\\"line\\\": 617, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fast_detectgpt2024\\\", \\\"file\\\": \\\"section_appendix.tex\\\", \\\"line\\\": 617, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dsir2023\\\", \\\"file\\\": \\\"section_appendix.tex\\\", \\\"line\\\": 659, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"qurating2024\\\", \\\"file\\\": \\\"section_appendix.tex\\\", \\\"line\\\": 659, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sugiyama2007_importance_weighting\\\", \\\"file\\\": \\\"section_appendix.tex\\\", \\\"line\\\": 662, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kirchenbauer2023_watermark\\\", \\\"file\\\": \\\"section_appendix.tex\\\", \\\"line\\\": 666, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"uchendu2020_attribution\\\", \\\"file\\\": \\\"section_appendix.tex\\\", \\\"line\\\": 667, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hu2022lora\\\", \\\"file\\\": \\\"section_appendix.tex\\\", \\\"line\\\": 683, \\\"command\\\": \\\"citet\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"shumailov2024_nature\\\", \\\"title\\\": \\\"AI models collapse when trained on recursively generated data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"AI models collapse when trained on recursively generated data\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dohmatob2024_tale_of_tails\\\", \\\"title\\\": \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dohmatob2025_strong_collapse\\\", \\\"title\\\": \\\"Strong Model Collapse\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Strong Model Collapse\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dohmatob2024_demystified\\\", \\\"title\\\": \\\"Model Collapse Demystified: The Case of Regression\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Model Collapse Demystified: The Case of Regression\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"alemohammad2024_mad\\\", \\\"title\\\": \\\"Self-Consuming Generative Models Go MAD\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Consuming Generative Models go MAD\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=alemohammad vs api=casco-rodriguez\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gerstgrasser2024_accumulate\\\", \\\"title\\\": \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"marchi2024_heat_death\\\", \\\"title\\\": \\\"Heat Death of Generative Models in Closed-Loop Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Heat Death of Generative Models in Closed-Loop Learning\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"knowledge_collapse2025\\\", \\\"title\\\": \\\"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.288, \\\"matched_title\\\": \\\"A predictive human model of language challenges traditional views in linguistics and pretrained transformer research\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.29 below threshold 0.82\\\"}, {\\\"key\\\": \\\"sigma2026_spectral\\\", \\\"title\\\": \\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mohamed2025_broken_telephone\\\", \\\"title\\\": \\\"LLM as a Broken Telephone: Iterative Generation Distorts Information\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLM as a Broken Telephone: Iterative Generation Distorts Information\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"synthetic_eggs2026\\\", \\\"title\\\": \\\"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"shi2025_closer_look\\\", \\\"title\\\": \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yi2026_escaping_collapse\\\", \\\"title\\\": \\\"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"drayson2025_detection_prevents_collapse\\\", \\\"title\\\": \\\"Machine-generated text detection prevents language model collapse\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Machine-generated text detection prevents language model collapse\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"bakshi2026_collapse_improvement\\\", \\\"title\\\": \\\"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2026_contamination\\\", \\\"title\\\": \\\"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"falahati2026_curated\\\", \\\"title\\\": \\\"Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.0, \\\"matched_title\\\": \\\"\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"no results from OpenAlex\\\"}, {\\\"key\\\": \\\"wu2025_detection_survey\\\", \\\"title\\\": \\\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gehrmann2019_gltr\\\", \\\"title\\\": \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mitchell2023_detectgpt\\\", \\\"title\\\": \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.382, \\\"matched_title\\\": \\\"Regulating ChatGPT and other Large Generative AI Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.38 below threshold 0.82\\\"}, {\\\"key\\\": \\\"fast_detectgpt2024\\\", \\\"title\\\": \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"binoculars2024\\\", \\\"title\\\": \\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"diveye2026\\\", \\\"title\\\": \\\"Diversity Boosts AI-Generated Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Diversity Boosts AI-Generated Text Detection\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sadasivan2023_paraphrase\\\", \\\"title\\\": \\\"Can AI-Generated Text be Reliably Detected?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Can AI-Generated Text be Reliably Detected?\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"pudasaini2026_detection_fails\\\", \\\"title\\\": \\\"Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"pu2026_generator_barrier\\\", \\\"title\\\": \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"bevendorff2025_two_paradigms\\\", \\\"title\\\": \\\"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"uchendu2020_attribution\\\", \\\"title\\\": \\\"Authorship Attribution for Neural Text Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Authorship Attribution for Neural Text Generation\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"editlens2026\\\", \\\"title\\\": \\\"EditLens: Quantifying the Extent of AI Editing in Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"EditLens: Quantifying the Extent of AI Editing in Text\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"loki2025\\\", \\\"title\\\": \\\"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tulchinskii2023_intrinsic_dim\\\", \\\"title\\\": \\\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"verma2024_ghostbuster\\\", \\\"title\\\": \\\"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2024_m4_semeval\\\", \\\"title\\\": \\\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2024_mage\\\", \\\"title\\\": \\\"MAGE: Machine-generated Text Detection in the Wild\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"MAGE: Machine-generated Text Detection in the Wild\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yang2024_dnagpt\\\", \\\"title\\\": \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kirchenbauer2023_watermark\\\", \\\"title\\\": \\\"A Watermark for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Watermark for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"holtzman2020_nucleus\\\", \\\"title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"finlayson2024_closing\\\", \\\"title\\\": \\\"Closing the Curious Case of Neural Text Degeneration\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Closing the Curious Case of Neural Text Degeneration\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"garces_arias2025_decoding_decoded\\\", \\\"title\\\": \\\"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=garces arias vs api=arias\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wiher2022_decoding\\\", \\\"title\\\": \\\"On Decoding Strategies for Neural Text Generators\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On Decoding Strategies for Neural Text Generators\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"basu2021_mirostat\\\", \\\"title\\\": \\\"Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"coral2020\\\", \\\"title\\\": \\\"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Rank consistent ordinal regression for neural networks with application to age estimation\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cloc2025\\\", \\\"title\\\": \\\"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hu2022lora\\\", \\\"title\\\": \\\"LoRA: Low-Rank Adaptation of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LoRA: Low-Rank Adaptation of Large Language Models\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"he2021_deberta_v3\\\", \\\"title\\\": \\\"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [\\\"year: bib=2023 vs api=2021\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"liu2019_roberta\\\", \\\"title\\\": \\\"RoBERTa: A Robustly Optimized BERT Pretraining Approach\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.495, \\\"matched_title\\\": \\\"Use of Bidirectional Encoder Representations from Transformers (BERT) and Robustly Optimized Bert Pretraining Approach (RoBERTa) for Nepali News Classification\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.50 below threshold 0.82\\\"}, {\\\"key\\\": \\\"dsir2023\\\", \\\"title\\\": \\\"Data Selection for Language Models via Importance Resampling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Data Selection for Language Models via Importance Resampling\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"qurating2024\\\", \\\"title\\\": \\\"QuRating: Selecting High-Quality Data for Training Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"QuRating: Selecting High-Quality Data for Training Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"penedo2024_fineweb\\\", \\\"title\\\": \\\"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sugiyama2007_importance_weighting\\\", \\\"title\\\": \\\"Covariate Shift Adaptation by Importance Weighted Cross Validation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Covariate Shift Adaptation by Importance Weighted Cross Validation\\\", \\\"matched_year\\\": \\\"2007\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"qwen2.5\\\", \\\"title\\\": \\\"Qwen2.5: A Party of Foundation Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.333, \\\"matched_title\\\": \\\"Can Open Large Language Models Catch Vulnerabilities?\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.33 below threshold 0.82\\\"}, {\\\"key\\\": \\\"llama3\\\", \\\"title\\\": \\\"The Llama 3 Herd of Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Llama 3 herd of models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=grattafiori vs api=aaron\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"schaeffer2025\\\", \\\"title\\\": \\\"Position: Model Collapse Does Not Mean What You Think\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Position: Model Collapse Does Not Mean What You Think\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"frank2001\\\", \\\"title\\\": \\\"A Simple Approach to Ordinal Classification\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Simple Approach to Ordinal Classification\\\", \\\"matched_year\\\": \\\"2001\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"rennie2005\\\", \\\"title\\\": \\\"Loss Functions for Preference Levels: Regression with Discrete Ordered Labels\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.373, \\\"matched_title\\\": \\\"Ordinal Regression Methods: Survey and Experimental Study\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.37 below threshold 0.82\\\"}, {\\\"key\\\": \\\"mccullagh1980_ordinal\\\", \\\"title\\\": \\\"Regression Models for Ordinal Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Regression Models for Ordinal Data\\\", \\\"matched_year\\\": \\\"1980\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wenzek2020_ccnet\\\", \\\"title\\\": \\\"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dugan2024_raid\\\", \\\"title\\\": \\\"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"guo2024curious\\\", \\\"title\\\": \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"padmakumar2024diversity\\\", \\\"title\\\": \\\"Does Writing with Language Models Reduce Content Diversity?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Does Writing with Language Models Reduce Content Diversity?\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"briesch2024selfconsuming\\\", \\\"title\\\": \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"seddik2024synthetic\\\", \\\"title\\\": \\\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"pareek2024understanding\\\", \\\"title\\\": \\\"Understanding the Gains from Repeated Self-Distillation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding the Gains from Repeated Self-Distillation\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 63, \"total_citations\": 89, \"unique_cited_keys\": 60, \"orphan_bib\": 3, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 53, \"online_not_found\": 6, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [\"bevendorff2025_two_paradigms\", \"pareek2024understanding\", \"shi2025_closer_look\"], \"missing_bib\": [], \"orphan_count\": 3, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"shumailov2024_nature\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"type\": \"inproceedings\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, ...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"dohmatob2025_strong_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"dohmatob2024_demystified\", \"type\": \"inproceedings\", \"title\": \"Model Collapse Demystified: The Case of Regression\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\", \"year\": \"2024\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"alemohammad2024_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"gerstgrasser2024_accumulate\", \"type\": \"misc\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"authors\": \"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafae...\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"marchi2024_heat_death\", \"type\": \"inproceedings\", \"title\": \"Heat Death of Generative Models in Closed-Loop Learning\", \"authors\": \"Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo\", \"year\": \"2024\", \"venue\": \"Proceedings of ICASSP\"}, {\"key\": \"knowledge_collapse2025\", \"type\": \"misc\", \"title\": \"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training\", \"authors\": \"Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven,...\", \"year\": \"2025\", \"venue\": \"\"}, {\"key\": \"sigma2026_spectral\", \"type\": \"misc\", \"title\": \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\", \"authors\": \"Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and P...\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\": \"mohamed2025_broken_telephone\", \"type\": \"inproceedings\", \"title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"authors\": \"Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan\", \"year\": \"2025\", \"venue\": \"Proceedings of ACL\"}, {\"key\": \"synthetic_eggs2026\", \"type\": \"inproceedings\", \"title\": \"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning\", \"authors\": \"Schaffelder, Max and Gatt, Albert\", \"year\": \"2026\", \"venue\": \"Findings of ACL\"}, {\"key\": \"shi2025_closer_look\", \"type\": \"inproceedings\", \"title\": \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\", \"authors\": \"Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and ...\", \"year\": \"2025\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"yi2026_escaping_collapse\", \"type\": \"inproceedings\", \"title\": \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\", \"authors\": \"Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng\", \"year\": \"2026\", \"venue\": \"3rd DATA-FM Workshop at ICLR 2026\"}, {\"key\": \"drayson2025_detection_prevents_collapse\", \"type\": \"inproceedings\", \"title\": \"Machine-generated text detection prevents language model collapse\", \"authors\": \"Drayson, George and Yilmaz, Emine and Lampos, Vasileios\", \"year\": \"2025\", \"venue\": \"Findings of EMNLP\"}, {\"key\": \"bakshi2026_collapse_improvement\", \"type\": \"misc\", \"title\": \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminate...\", \"authors\": \"Bakshi, Soham and Chakraborty, Sunrit\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\": \"wang2026_contamination\", \"type\": \"misc\", \"title\": \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive T...\", \"authors\": \"Wang, Kevin and Niu, Hongqian and Li, Didong\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\": \"falahati2026_curated\", \"type\": \"misc\", \"title\": \"Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferenc...\", \"authors\": \"Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\": \"wu2025_detection_survey\", \"type\": \"article\", \"title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"authors\": \"Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam a...\", \"year\": \"2025\", \"venue\": \"Computational Linguistics\"}, {\"key\": \"gehrmann2019_gltr\", \"type\": \"inproceedings\", \"title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"authors\": \"Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.\", \"year\": \"2019\", \"venue\": \"Proceedings of ACL: System Demonstrations\"}, {\"key\": \"mitchell2023_detectgpt\", \"type\": \"inproceedings\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"authors\": \"Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher...\", \"year\": \"2023\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"fast_detectgpt2024\", \"type\": \"inproceedings\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"authors\": \"Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yu...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"binoculars2024\", \"type\": \"inproceedings\", \"title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"authors\": \"Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Ham...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"diveye2026\", \"type\": \"article\", \"title\": \"Diversity Boosts AI-Generated Text Detection\", \"authors\": \"Basani, Advik Raj and Chen, Pin-Yu\", \"year\": \"2026\", \"venue\": \"Transactions on Machine Learning Research (TMLR)\"}, {\"key\": \"sadasivan2023_paraphrase\", \"type\": \"misc\", \"title\": \"Can AI-Generated Text be Reliably Detected?\", \"authors\": \"Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, W...\", \"year\": \"2023\", \"venue\": \"\"}, {\"key\": \"pudasaini2026_detection_fails\", \"type\": \"misc\", \"title\": \"Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy\", \"authors\": \"Pudasaini, Shushanta and Miralles-Pech\\\\'uan, Luis and Lillis, David and Llorens ...\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\": \"pu2026_generator_barrier\", \"type\": \"misc\", \"title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"authors\": \"Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\": \"bevendorff2025_two_paradigms\", \"type\": \"inproceedings\", \"title\": \"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\", \"authors\": \"Bevendorff, Janek and Wiegmann, Matti and Richter, Emmelie and Potthast, Martin ...\", \"year\": \"2025\", \"venue\": \"Findings of ACL\"}, {\"key\": \"uchendu2020_attribution\", \"type\": \"inproceedings\", \"title\": \"Authorship Attribution for Neural Text Generation\", \"authors\": \"Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon\", \"year\": \"2020\", \"venue\": \"Proceedings of EMNLP\"}, {\"key\": \"editlens2026\", \"type\": \"inproceedings\", \"title\": \"EditLens: Quantifying the Extent of AI Editing in Text\", \"authors\": \"Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit\", \"year\": \"2026\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"loki2025\", \"type\": \"inproceedings\", \"title\": \"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\", \"authors\": \"Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi...\", \"year\": \"2025\", \"venue\": \"Proceedings of ICLR (Spotlight)\"}, {\"key\": \"tulchinskii2023_intrinsic_dim\", \"type\": \"inproceedings\", \"title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"authors\": \"Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavsk...\", \"year\": \"2023\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"verma2024_ghostbuster\", \"type\": \"inproceedings\", \"title\": \"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\", \"authors\": \"Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan\", \"year\": \"2024\", \"venue\": \"Proceedings of NAACL\"}, {\"key\": \"wang2024_m4_semeval\", \"type\": \"inproceedings\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"authors\": \"Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2...\"}, {\"key\": \"li2024_mage\", \"type\": \"inproceedings\", \"title\": \"MAGE: Machine-generated Text Detection in the Wild\", \"authors\": \"Li, Yongkang and Li, Donghao and Yang, Yue and Hu, Baotian and Zhang, Min\", \"year\": \"2024\", \"venue\": \"Proceedings of ACL\"}, {\"key\": \"yang2024_dnagpt\", \"type\": \"inproceedings\", \"title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"authors\": \"Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Ya...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"kirchenbauer2023_watermark\", \"type\": \"inproceedings\", \"title\": \"A Watermark for Large Language Models\", \"authors\": \"Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Mier...\", \"year\": \"2023\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"holtzman2020_nucleus\", \"type\": \"inproceedings\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"authors\": \"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\", \"year\": \"2020\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"finlayson2024_closing\", \"type\": \"inproceedings\", \"title\": \"Closing the Curious Case of Neural Text Degeneration\", \"authors\": \"Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabh...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"garces_arias2025_decoding_decoded\", \"type\": \"inproceedings\", \"title\": \"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation\", \"authors\": \"Garces Arias, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher,...\", \"year\": \"2025\", \"venue\": \"Proceedings of COLING\"}, {\"key\": \"wiher2022_decoding\", \"type\": \"article\", \"title\": \"On Decoding Strategies for Neural Text Generators\", \"authors\": \"Wiher, Gian and Meister, Clara and Cotterell, Ryan\", \"year\": \"2022\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"basu2021_mirostat\", \"type\": \"inproceedings\", \"title\": \"Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity\", \"authors\": \"Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shiris...\", \"year\": \"2021\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"coral2020\", \"type\": \"article\", \"title\": \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\", \"authors\": \"Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian\", \"year\": \"2020\", \"venue\": \"Pattern Recognition Letters\"}, {\"key\": \"cloc2025\", \"type\": \"inproceedings\", \"title\": \"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\", \"authors\": \"Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting\", \"year\": \"2025\", \"venue\": \"Proceedings of CVPR\"}, {\"key\": \"hu2022lora\", \"type\": \"inproceedings\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"authors\": \"Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li,...\", \"year\": \"2022\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"he2021_deberta_v3\", \"type\": \"inproceedings\", \"title\": \"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing\", \"authors\": \"He, Pengcheng and Gao, Jianfeng and Chen, Weizhu\", \"year\": \"2023\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"liu2019_roberta\", \"type\": \"misc\", \"title\": \"RoBERTa: A Robustly Optimized BERT Pretraining Approach\", \"authors\": \"Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and...\", \"year\": \"2019\", \"venue\": \"\"}, {\"key\": \"dsir2023\", \"type\": \"inproceedings\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"authors\": \"Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\", \"year\": \"2023\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"qurating2024\", \"type\": \"inproceedings\", \"title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"authors\": \"Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"penedo2024_fineweb\", \"type\": \"inproceedings\", \"title\": \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\", \"authors\": \"\", \"year\": \"2024\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"sugiyama2007_importance_weighting\", \"type\": \"article\", \"title\": \"Covariate Shift Adaptation by Importance Weighted Cross Validation\", \"authors\": \"Sugiyama, Masashi and Krauledat, Matthias and M\\\\\\\"uller, Klaus-Robert\", \"year\": \"2007\", \"venue\": \"Journal of Machine Learning Research\"}, {\"key\": \"qwen2.5\", \"type\": \"misc\", \"title\": \"Qwen2.5: A Party of Foundation Models\", \"authors\": \"Qwen Team\", \"year\": \"2025\", \"venue\": \"\"}, {\"key\": \"llama3\", \"type\": \"misc\", \"title\": \"The Llama 3 Herd of Models\", \"authors\": \"Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav ...\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"schaeffer2025\", \"type\": \"misc\", \"title\": \"Position: Model Collapse Does Not Mean What You Think\", \"authors\": \"Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi\", \"year\": \"2025\", \"venue\": \"\"}, {\"key\": \"frank2001\", \"type\": \"inproceedings\", \"title\": \"A Simple Approach to Ordinal Classification\", \"authors\": \"Frank, Eibe and Hall, Mark\", \"year\": \"2001\", \"venue\": \"Proceedings of ECML\"}, {\"key\": \"rennie2005\", \"type\": \"inproceedings\", \"title\": \"Loss Functions for Preference Levels: Regression with Discrete Ordered Labels\", \"authors\": \"Rennie, Jason D. M. and Srebro, Nathan\", \"year\": \"2005\", \"venue\": \"Proceedings of IJCAI Workshop on Advances in Preference Handling\"}, {\"key\": \"mccullagh1980_ordinal\", \"type\": \"article\", \"title\": \"Regression Models for Ordinal Data\", \"authors\": \"McCullagh, Peter\", \"year\": \"1980\", \"venue\": \"Journal of the Royal Statistical Society: Series B\"}, {\"key\": \"wenzek2020_ccnet\", \"type\": \"inproceedings\", \"title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"authors\": \"Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vis...\", \"year\": \"2020\", \"venue\": \"Proceedings of LREC\"}, {\"key\": \"dugan2024_raid\", \"type\": \"inproceedings\", \"title\": \"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors\", \"authors\": \"Dugan, Liam and Hwang, Alyssa and Trhl\\\\'\\\\ik, Filip and Zhu, Andrew and Ludan, Jo...\", \"year\": \"2024\", \"venue\": \"Proceedings of ACL\"}, {\"key\": \"guo2024curious\", \"type\": \"inproceedings\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"authors\": \"Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\\\'e\", \"year\": \"2024\", \"venue\": \"Findings of NAACL\"}, {\"key\": \"padmakumar2024diversity\", \"type\": \"inproceedings\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"authors\": \"Padmakumar, Vishakh and He, He\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"briesch2024selfconsuming\", \"type\": \"misc\", \"title\": \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\", \"authors\": \"Briesch, Martin and Sobania, Dominik and Rothlauf, Franz\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"seddik2024synthetic\", \"type\": \"misc\", \"title\": \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\", \"authors\": \"Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pie...\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"pareek2024understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Gains from Repeated Self-Distillation\", \"authors\": \"Pareek, Divyansh and Du, Simon S. and Oh, Sewoong\", \"year\": \"2024\", \"venue\": \"Proceedings of NeurIPS\"}], \"tex_citations\": [{\"key\": \"shumailov2024_nature\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"alemohammad2024_mad\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"binoculars2024\", \"file\": \"introduction.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt2024\", \"file\": \"introduction.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"diveye2026\", \"file\": \"introduction.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"kirchenbauer2023_watermark\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"shumailov2024_nature\", \"file\": \"introduction.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"file\": \"introduction.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"drayson2025_detection_prevents_collapse\", \"file\": \"introduction.tex\", \"line\": 11, \"command\": \"citet\"}, {\"key\": \"shumailov2024_nature\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"seddik2024synthetic\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"dohmatob2025_strong_collapse\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"alemohammad2024_mad\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gerstgrasser2024_accumulate\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"drayson2025_detection_prevents_collapse\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"yi2026_escaping_collapse\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"falahati2026_curated\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"wenzek2020_ccnet\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"bakshi2026_collapse_improvement\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"marchi2024_heat_death\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"wang2026_contamination\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"knowledge_collapse2025\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"dohmatob2024_demystified\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"guo2024curious\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"briesch2024selfconsuming\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"padmakumar2024diversity\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"sigma2026_spectral\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"synthetic_eggs2026\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"schaeffer2025\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"wu2025_detection_survey\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"mitchell2023_detectgpt\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt2024\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"binoculars2024\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"diveye2026\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"gehrmann2019_gltr\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"verma2024_ghostbuster\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"yang2024_dnagpt\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"tulchinskii2023_intrinsic_dim\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"kirchenbauer2023_watermark\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"sadasivan2023_paraphrase\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"pudasaini2026_detection_fails\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"pu2026_generator_barrier\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"wang2024_m4_semeval\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"dugan2024_raid\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"li2024_mage\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"editlens2026\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"uchendu2020_attribution\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"citet\"}, {\"key\": \"loki2025\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"mohamed2025_broken_telephone\", \"file\": \"related_work.tex\", \"line\": 18, \"command\": \"citet\"}, {\"key\": \"mccullagh1980_ordinal\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"frank2001\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citet\"}, {\"key\": \"rennie2005\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citet\"}, {\"key\": \"coral2020\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"cloc2025\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"holtzman2020_nucleus\", \"file\": \"related_work.tex\", \"line\": 27, \"command\": \"cite\"}, {\"key\": \"finlayson2024_closing\", \"file\": \"related_work.tex\", \"line\": 27, \"command\": \"cite\"}, {\"key\": \"garces_arias2025_decoding_decoded\", \"file\": \"related_work.tex\", \"line\": 27, \"command\": \"cite\"}, {\"key\": \"wiher2022_decoding\", \"file\": \"related_work.tex\", \"line\": 27, \"command\": \"cite\"}, {\"key\": \"basu2021_mirostat\", \"file\": \"related_work.tex\", \"line\": 27, \"command\": \"cite\"}, {\"key\": \"holtzman2020_nucleus\", \"file\": \"method.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"hu2022lora\", \"file\": \"method.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"coral2020\", \"file\": \"method.tex\", \"line\": 104, \"command\": \"cite\"}, {\"key\": \"diveye2026\", \"file\": \"method.tex\", \"line\": 104, \"command\": \"cite\"}, {\"key\": \"shumailov2024_nature\", \"file\": \"atlas.tex\", \"line\": 62, \"command\": \"cite\"}, {\"key\": \"shumailov2024_nature\", \"file\": \"atlas.tex\", \"line\": 170, \"command\": \"cite\"}, {\"key\": \"coral2020\", \"file\": \"generalization.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"diveye2026\", \"file\": \"generalization.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"llama3\", \"file\": \"generalization.tex\", \"line\": 104, \"command\": \"cite\"}, {\"key\": \"qwen2.5\", \"file\": \"generalization.tex\", \"line\": 104, \"command\": \"cite\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"file\": \"discussion.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"penedo2024_fineweb\", \"file\": \"conclusion.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"sadasivan2023_paraphrase\", \"file\": \"conclusion.tex\", \"line\": 30, \"command\": \"cite\"}, {\"key\": \"bakshi2026_collapse_improvement\", \"file\": \"conclusion.tex\", \"line\": 34, \"command\": \"citet\"}, {\"key\": \"pudasaini2026_detection_fails\", \"file\": \"conclusion.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"falahati2026_curated\", \"file\": \"conclusion.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"he2021_deberta_v3\", \"file\": \"section_appendix.tex\", \"line\": 161, \"command\": \"cite\"}, {\"key\": \"liu2019_roberta\", \"file\": \"section_appendix.tex\", \"line\": 161, \"command\": \"cite\"}, {\"key\": \"cloc2025\", \"file\": \"section_appendix.tex\", \"line\": 187, \"command\": \"cite\"}, {\"key\": \"binoculars2024\", \"file\": \"section_appendix.tex\", \"line\": 617, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt2024\", \"file\": \"section_appendix.tex\", \"line\": 617, \"command\": \"cite\"}, {\"key\": \"dsir2023\", \"file\": \"section_appendix.tex\", \"line\": 659, \"command\": \"cite\"}, {\"key\": \"qurating2024\", \"file\": \"section_appendix.tex\", \"line\": 659, \"command\": \"cite\"}, {\"key\": \"sugiyama2007_importance_weighting\", \"file\": \"section_appendix.tex\", \"line\": 662, \"command\": \"cite\"}, {\"key\": \"kirchenbauer2023_watermark\", \"file\": \"section_appendix.tex\", \"line\": 666, \"command\": \"cite\"}, {\"key\": \"uchendu2020_attribution\", \"file\": \"section_appendix.tex\", \"line\": 667, \"command\": \"cite\"}, {\"key\": \"hu2022lora\", \"file\": \"section_appendix.tex\", \"line\": 683, \"command\": \"citet\"}], \"online_verification\": [{\"key\": \"shumailov2024_nature\", \"title\": \"AI models collapse when trained on recursively generated data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"AI models collapse when trained on recursively generated data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dohmatob2025_strong_collapse\", \"title\": \"Strong Model Collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Strong Model Collapse\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dohmatob2024_demystified\", \"title\": \"Model Collapse Demystified: The Case of Regression\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Model Collapse Demystified: The Case of Regression\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"alemohammad2024_mad\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Self-Consuming Generative Models go MAD\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=alemohammad vs api=casco-rodriguez\"], \"note\": \"\"}, {\"key\": \"gerstgrasser2024_accumulate\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"marchi2024_heat_death\", \"title\": \"Heat Death of Generative Models in Closed-Loop Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Heat Death of Generative Models in Closed-Loop Learning\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"knowledge_collapse2025\", \"title\": \"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training\", \"status\": \"not_found\", \"confidence\": 0.288, \"matched_title\": \"A predictive human model of language challenges traditional views in linguistics and pretrained transformer research\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.29 below threshold 0.82\"}, {\"key\": \"sigma2026_spectral\", \"title\": \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mohamed2025_broken_telephone\", \"title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"synthetic_eggs2026\", \"title\": \"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shi2025_closer_look\", \"title\": \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yi2026_escaping_collapse\", \"title\": \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"drayson2025_detection_prevents_collapse\", \"title\": \"Machine-generated text detection prevents language model collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Machine-generated text detection prevents language model collapse\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bakshi2026_collapse_improvement\", \"title\": \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2026_contamination\", \"title\": \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"falahati2026_curated\", \"title\": \"Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences\", \"status\": \"not_found\", \"confidence\": 0.0, \"matched_title\": \"\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"no results from OpenAlex\"}, {\"key\": \"wu2025_detection_survey\", \"title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gehrmann2019_gltr\", \"title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mitchell2023_detectgpt\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"status\": \"not_found\", \"confidence\": 0.382, \"matched_title\": \"Regulating ChatGPT and other Large Generative AI Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.38 below threshold 0.82\"}, {\"key\": \"fast_detectgpt2024\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"binoculars2024\", \"title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"diveye2026\", \"title\": \"Diversity Boosts AI-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Diversity Boosts AI-Generated Text Detection\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sadasivan2023_paraphrase\", \"title\": \"Can AI-Generated Text be Reliably Detected?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Can AI-Generated Text be Reliably Detected?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"pudasaini2026_detection_fails\", \"title\": \"Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"pu2026_generator_barrier\", \"title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bevendorff2025_two_paradigms\", \"title\": \"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"uchendu2020_attribution\", \"title\": \"Authorship Attribution for Neural Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Authorship Attribution for Neural Text Generation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"editlens2026\", \"title\": \"EditLens: Quantifying the Extent of AI Editing in Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"EditLens: Quantifying the Extent of AI Editing in Text\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"loki2025\", \"title\": \"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tulchinskii2023_intrinsic_dim\", \"title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"verma2024_ghostbuster\", \"title\": \"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2024_m4_semeval\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2024_mage\", \"title\": \"MAGE: Machine-generated Text Detection in the Wild\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MAGE: Machine-generated Text Detection in the Wild\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yang2024_dnagpt\", \"title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kirchenbauer2023_watermark\", \"title\": \"A Watermark for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Watermark for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"holtzman2020_nucleus\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Case of Neural Text Degeneration\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"finlayson2024_closing\", \"title\": \"Closing the Curious Case of Neural Text Degeneration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Closing the Curious Case of Neural Text Degeneration\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"garces_arias2025_decoding_decoded\", \"title\": \"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=garces arias vs api=arias\"], \"note\": \"\"}, {\"key\": \"wiher2022_decoding\", \"title\": \"On Decoding Strategies for Neural Text Generators\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Decoding Strategies for Neural Text Generators\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"basu2021_mirostat\", \"title\": \"Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"coral2020\", \"title\": \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rank consistent ordinal regression for neural networks with application to age estimation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cloc2025\", \"title\": \"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hu2022lora\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"he2021_deberta_v3\", \"title\": \"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing\", \"matched_year\": \"2021\", \"mismatch_fields\": [\"year: bib=2023 vs api=2021\"], \"note\": \"\"}, {\"key\": \"liu2019_roberta\", \"title\": \"RoBERTa: A Robustly Optimized BERT Pretraining Approach\", \"status\": \"not_found\", \"confidence\": 0.495, \"matched_title\": \"Use of Bidirectional Encoder Representations from Transformers (BERT) and Robustly Optimized Bert Pretraining Approach (RoBERTa) for Nepali News Classification\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.50 below threshold 0.82\"}, {\"key\": \"dsir2023\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Data Selection for Language Models via Importance Resampling\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qurating2024\", \"title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"penedo2024_fineweb\", \"title\": \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sugiyama2007_importance_weighting\", \"title\": \"Covariate Shift Adaptation by Importance Weighted Cross Validation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Covariate Shift Adaptation by Importance Weighted Cross Validation\", \"matched_year\": \"2007\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen2.5\", \"title\": \"Qwen2.5: A Party of Foundation Models\", \"status\": \"not_found\", \"confidence\": 0.333, \"matched_title\": \"Can Open Large Language Models Catch Vulnerabilities?\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"llama3\", \"title\": \"The Llama 3 Herd of Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"The Llama 3 herd of models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=grattafiori vs api=aaron\"], \"note\": \"\"}, {\"key\": \"schaeffer2025\", \"title\": \"Position: Model Collapse Does Not Mean What You Think\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Position: Model Collapse Does Not Mean What You Think\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"frank2001\", \"title\": \"A Simple Approach to Ordinal Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Simple Approach to Ordinal Classification\", \"matched_year\": \"2001\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"rennie2005\", \"title\": \"Loss Functions for Preference Levels: Regression with Discrete Ordered Labels\", \"status\": \"not_found\", \"confidence\": 0.373, \"matched_title\": \"Ordinal Regression Methods: Survey and Experimental Study\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.37 below threshold 0.82\"}, {\"key\": \"mccullagh1980_ordinal\", \"title\": \"Regression Models for Ordinal Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Regression Models for Ordinal Data\", \"matched_year\": \"1980\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wenzek2020_ccnet\", \"title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dugan2024_raid\", \"title\": \"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2024curious\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"padmakumar2024diversity\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"briesch2024selfconsuming\", \"title\": \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"seddik2024synthetic\", \"title\": \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"pareek2024understanding\", \"title\": \"Understanding the Gains from Repeated Self-Distillation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Gains from Repeated Self-Distillation\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "64eeb5b2-d6f6-49b0-8f28-e690ae779b91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-18T14:12:53.399Z_

<details><summary>↩ Tool result · `toolu_01Aj8FpnwRVuAhhVjJ3br7Gp`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "169ef68f-d86a-4c9b-95c4-62223ffa74b3",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "e8d793d1-c525-42e2-96f2-530020b7d96d",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "169ef68f-d86a-4c9b-95c4-62223ffa74b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 64 · 2026-05-18T14:12:53.413Z_

<details><summary>↩ Tool result · `toolu_01Eq1kyKwSU27JoAyQgZyJcq`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61ac72b4-0214-4b50-9beb-07e9e6735abf",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "1b2feefd-bd32-4cb7-b488-f2c97f67a5d4",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "61ac72b4-0214-4b50-9beb-07e9e6735abf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-18T14:12:53.417Z_

<details><summary>↩ Tool result · `toolu_014Wez1FjNQKN1rD3uXhoKoD`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex:6:Subsequent work addresses mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026}.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex:27:Decoding strategies shape text statistics in ways that interact with depth signals \cite{holtzman2020_nucleus,finlayson2024_closing,garces_arias2025_decoding_decoded,wiher2022_decoding,basu2021_mirostat}.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:155:\caption{Binary pairwise AUC decay curves for three models (nucleus sampling, depths 0--5). Horizontal dashed lines mark $T \in \{0.65, 0.70, 0.75, 0.80\}$. All three curves converge below 0.70 at d4-vs-d5, while d3-vs-d4 AUC clusters in the range 0.750--0.784. Shaded bands: bootstrap 95\% CIs.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:12:This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:8:Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:317:We extend the benchmark to two 7--8B models: Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct, both under 4-bit NF4 QLoRA fine-tuning, generating depths $d \in \{0, 1, \ldots, 5\}$ with nucleus sampling ($p{=}0.95$, 500 samples per depth).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:321:Table~\ref{tab:cross_scale} contrasts the two 7--8B models with the three 1--1.5B models on matched evaluation (nucleus sampling, depths 0--3).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:386:The base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries; depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:394:Four confounds limit these results: (1)~4-bit NF4 QLoRA quantization (absent at 1--1.5B) may distort the perplexity distribution independently of depth; (2)~smaller sample size (500 vs.\ 5{,}000 per depth) widens confidence intervals; (3)~evaluation is limited to nucleus sampling, leaving other strategies untested at this scale; (4)~vocabulary mismatch between 7--8B generators and the 1.4B reference model.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:461:Despite this variation, the classifier remains effective after clipping, confirming that the depth signal resides in the p90-and-below distributional shape rather than extreme outliers.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex:6:This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex:32:    \item \textbf{Diagnostic ablations.} LoRA rank spread 4.65\,pp, three reference architectures (67--79\%), generation length scaling, and surface-text control (zero-shot LLMs at 30--36\%, 43\,pp below RF) confirming the signal resides in distributional statistics; 19 features and a Random Forest suffice for GPU-free inference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ea4b513-578d-4951-b7e6-f254c4c108f6",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "769af546-b1eb-419c-b5eb-2b1926f21814",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex:6:Subsequent work addresses mitigation \\cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, non-monotonic dynamics \\cite{bakshi2026_collapse_improvement}, convergence \\cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \\cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026}.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex:27:Decoding strategies shape text statistics in ways that interact with depth signals \\cite{holtzman2020_nucleus,finlayson2024_closing,garces_arias2025_decoding_decoded,wiher2022_decoding,basu2021_mirostat}.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:155:\\caption{Binary pairwise AUC decay curves for three models (nucleus sampling, depths 0--5). Horizontal dashed lines mark $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$. All three curves converge below 0.70 at d4-vs-d5, while d3-vs-d4 AUC clusters in the range 0.750--0.784. Shaded bands: bootstrap 95\\% CIs.}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:12:This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:8:Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \\S\\ref{sec:atlas:strategy}.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:317:We extend the benchmark to two 7--8B models: Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct, both under 4-bit NF4 QLoRA fine-tuning, generating depths $d \\in \\{0, 1, \\ldots, 5\\}$ with nucleus sampling ($p{=}0.95$, 500 samples per depth).\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:321:Table~\\ref{tab:cross_scale} contrasts the two 7--8B models with the three 1--1.5B models on matched evaluation (nucleus sampling, depths 0--3).\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:386:The base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries; depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:394:Four confounds limit these results: (1)~4-bit NF4 QLoRA quantization (absent at 1--1.5B) may distort the perplexity distribution independently of depth; (2)~smaller sample size (500 vs.\\ 5{,}000 per depth) widens confidence intervals; (3)~evaluation is limited to nucleus sampling, leaving other strategies untested at this scale; (4)~vocabulary mismatch between 7--8B generators and the 1.4B reference model.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:461:Despite this variation, the classifier remains effective after clipping, confirming that the depth signal resides in the p90-and-below distributional shape rather than extreme outliers.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex:6:This model$\\to$data$\\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \\cite{dohmatob2024_tale_of_tails}.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex:32:    \\item \\textbf{Diagnostic ablations.} LoRA rank spread 4.65\\,pp, three reference architectures (67--79\\%), generation length scaling, and surface-text control (zero-shot LLMs at 30--36\\%, 43\\,pp below RF) confirming the signal resides in distributional statistics; 19 features and a Random Forest suffice for GPU-free inference.",
    "numLines": 12
  },
  "sourceToolAssistantUUID": "6ea4b513-578d-4951-b7e6-f254c4c108f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 66 · 2026-05-18T14:12:53.420Z_

```json
{
  "parentUuid": "769af546-b1eb-419c-b5eb-2b1926f21814",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "50179c9b-3027-4409-9c99-8543abbb0097",
  "timestamp": "2026-05-18T14:12:53.420Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性 + 写作质量**  ### 论文信息 - **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints - **路径**: `proje…",
  "leafUuid": "50179c9b-3027-4409-9c99-8543abbb0097",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Runtime record

_source line 68_

```json
{
  "type": "ai-title",
  "aiTitle": "Review recursive generation depth estimation paper",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Assistant

_source line 69 · 2026-05-18T14:13:03.219Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me check for more specific AI writing patterns and compile my comprehensive review. Let me also check "-ing" pattern at end of sentences.

Let me also look at a few more things:
1. Page count - I need to estimate
2. Self-citation leakage
3. Specific data consistency checks

The grep for "ing," found some instances but they're mostly in tables/captions/natural language, not AI-style "-ing phrases". The em-dash and en-dash checks came back clean.


Now I'm examining whether there's any self-citation leakage in the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50179c9b-3027-4409-9c99-8543abbb0097",
  "isSidechain": false,
  "requestId": "req_011CbAAupDQt158mmqhkfSrp",
  "type": "assistant",
  "uuid": "9074d38b-43e8-4f42-9fd6-d3b64432dce0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNjeCoeKXHttsECj1cDG1m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21172,
      "cache_read_input_tokens": 79352,
      "output_tokens": 622,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21172,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 622,
          "cache_read_input_tokens": 79352,
          "cache_creation_input_tokens": 21172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21172
          },
          "type": "message"
        }
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

_source line 70 · 2026-05-18T14:13:03.654Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01RqSY7VC2rPQeG52LzMqqef`</summary>

```json
{
  "pattern": "\\\\(our|we|previous|prior\\\\) (work|paper|study|earlier)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9074d38b-43e8-4f42-9fd6-d3b64432dce0",
  "isSidechain": false,
  "requestId": "req_011CbAAupDQt158mmqhkfSrp",
  "type": "assistant",
  "uuid": "5faa726d-6b53-4b9c-b00b-2e68313bea79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNjeCoeKXHttsECj1cDG1m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21172,
      "cache_read_input_tokens": 79352,
      "output_tokens": 622,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21172,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 622,
          "cache_read_input_tokens": 79352,
          "cache_creation_input_tokens": 21172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21172
          },
          "type": "message"
        }
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

_source line 71 · 2026-05-18T14:13:03.677Z_

<details><summary>↩ Tool result · `toolu_01RqSY7VC2rPQeG52LzMqqef`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5faa726d-6b53-4b9c-b00b-2e68313bea79",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "971882c6-ba42-4dfd-9a1c-cdb7a03d7adf",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "5faa726d-6b53-4b9c-b00b-2e68313bea79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-18T14:13:06.640Z_

<details><summary>↩ Tool result · `toolu_01AKnnBYdY46Qviyx1Fbz9zF`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94777ef6-0a41-4484-9106-f118dc10cd43",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "253b297c-41b8-46d8-859f-57e71f82d615",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "94777ef6-0a41-4484-9106-f118dc10cd43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 73 · 2026-05-18T14:13:05.552Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0174qgrVXwdeYG45Km2ydsH6`</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally|delve|leverage|utilize|facilitate|myriad|plethora|paradigm shift|It is worth noting|Notably,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "971882c6-ba42-4dfd-9a1c-cdb7a03d7adf",
  "isSidechain": false,
  "requestId": "req_011CbAAupDQt158mmqhkfSrp",
  "type": "assistant",
  "uuid": "40760b70-41ba-4a52-9916-6d077c64c5eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNjeCoeKXHttsECj1cDG1m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21172,
      "cache_read_input_tokens": 79352,
      "output_tokens": 622,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21172,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 622,
          "cache_read_input_tokens": 79352,
          "cache_creation_input_tokens": 21172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21172
          },
          "type": "message"
        }
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

_source line 74 · 2026-05-18T14:13:05.575Z_

<details><summary>↩ Tool result · `toolu_0174qgrVXwdeYG45Km2ydsH6`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40760b70-41ba-4a52-9916-6d077c64c5eb",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "c59ce389-ee64-4a45-b2b7-8b7caea85405",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "40760b70-41ba-4a52-9916-6d077c64c5eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 75 · 2026-05-18T14:13:06.626Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01AKnnBYdY46Qviyx1Fbz9zF`</summary>

```json
{
  "pattern": "highlighting|demonstrating|showcasing|underscoring|emphasizing",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c59ce389-ee64-4a45-b2b7-8b7caea85405",
  "isSidechain": false,
  "requestId": "req_011CbAAupDQt158mmqhkfSrp",
  "type": "assistant",
  "uuid": "94777ef6-0a41-4484-9106-f118dc10cd43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNjeCoeKXHttsECj1cDG1m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21172,
      "cache_read_input_tokens": 79352,
      "output_tokens": 622,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21172,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 622,
          "cache_read_input_tokens": 79352,
          "cache_creation_input_tokens": 21172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21172
          },
          "type": "message"
        }
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

_source line 76 · 2026-05-18T14:14:05.960Z_

<details><summary>Logged reasoning block</summary>

```text
The paper is clean of AI writing markers. No em-dashes, no AI high-frequency words, no self-citation leakage. 

Now let me compile my review. Let me also verify some data consistency issues between abstract and tables.

Abstract claims:
- "≈69--86% four-class accuracy" → Table 1: 68.8%--85.9% ✓ (close enough with rounding)
- "EDD_{0.75}=4 for the best-characterized family" → This needs checking. For Pythia nucleus, the d3-vs-d4 AUC is 0.784 which is ≥ 0.75. 

I'm verifying the EDD calculation by checking the pairwise discriminability scores: d0 through d4 all show AUC values above 0.75 (0.999, 0.925, 0.823, 0.784), while d4 versus d5 drops to 0.683, confirming EDD=4 for the extended pipeline. The 9-cell benchmark results in Table 4 also align with this, showing 7 out of 9 cells reaching EDD≥3. ✓

Now I'm cross-referencing all the reported metrics against the tables and text: the 66.4% cross-model transfer rate matches Table 5, the 70.2% performance for Llama-3.1-8B checks out, prompted generation at 69.5% aligns with the data, cross-model chains hit 84.75%, cross-domain arXiv reaches 74.1%, and zero-shot LLMs range from 30.4% to 36.2%. The gap between the best random forest result (~78.7%) and the best zero-shot performance (36.2%) is roughly 42.5 percentage points, confirming the stated 43 pp difference. ✓ The baseline RF for Pythia nucleus is 78.8% according to Table 3, making the gap 42.6pp when compared to the best zero-shot performance of 36.2%, which rounds to the 43pp mentioned in the paper—close enough that it's not worth flagging as an error. Let me move on to check the contribution bullet about the 5...

Now looking at the top-5 features claim: the atlas section confirms they achieve 97.6% of full performance, calculated as 76.5/78.4. The abstract describes these as "perplexity-based features," but that's slightly imprecise since 7 of the 19 features are actually non-perplexity (lexical diversity and repetition metrics). That said, the feature ablation shows perplexity features alone recover 66.0% versus the full 66.6%, so calling them perplexity-based is defensible enough.

But there's a real issue here: the abstract claims "19 perplexity-based features" when Table 1 clearly shows lexical diversity features (TTR, hapax ratio, bigram/trigram entropy) and repetition features (repeated n-gram fractions) that aren't perplexity-based at all. This is a factual inaccuracy—the abstract should say "19 statistical features" or be more specific about the mix of perplexity, surprisal, and lexical features. The abstract's claim that all 19 features are "perplexity-based" is misleading—only 12 of them actually derive from the reference model's perplexity distribution, while the remaining 7 (lexical diversity and repetition metrics) come directly from the text itself. This needs to be corrected to accurately reflect what the method actually does.

Looking at the bigger picture, the paper has genuine strengths: it frames recursive depth estimation as an ordinal classification problem in a novel way, runs comprehensive experiments across a 3×3 grid with thorough ablations, and identifies a useful finding that perplexity tail statistics consistently emerge as the strongest predictors. The writing is clean and the limitations are honestly acknowledged.

But there are significant issues holding it back. The core methodological contribution—applying Random Forest with hand-crafted features—isn't particularly novel for a top venue. The discussion is only a single paragraph when EMNLP would expect something more substantial. And the headline accuracy numbers are substantially inflated by the trivial separability of d0 from deeper depths, which the paper does acknowledge but doesn't adequately address in its main claims.

The cross-model performance on d1-d3 drops to 55.4% balanced accuracy, barely above the 33% chance baseline, and cross-strategy transfer is even worse at 45.9%—only 12.9 percentage points above chance. These numbers severely limit practical applicability. There's also a factual error where the abstract describes all 19 features as perplexity-based when 7 are actually lexical or repetition-based. The benchmark itself relies on 1-1.5B parameter models, which are quite small by 2026 standards, and uses LoRA fine-tuning rather than the full fine-tuning or pretraining that would better reflect real recursive contamination. The false positive rate on web data reaches 34% on C4, which is problematic for deployment. Finally, the connection to Dohmatob et al.'s work feels underdeveloped—the paper largely builds on their framing without sufficiently differentiating its contribution.

The paper does formalize an interesting problem and provides thorough empirical analysis, but the methodological novelty is modest—it's essentially random forests with perplexity features. The practical limitations from strategy-dependence and d0 inflation, combined with a surprisingly brief Discussion section, make this read more like a solid empirical study than a methodological advance. I'd place it around 3.0-3.5 on the review scale, probably suitable as a Findings paper.

There are some notable gaps though: the authors don't explore more sophisticated approaches like fine-tuned transformers on perplexity sequences or graph-based methods, there's no investigation of real-world contamination at scale, and the recursive setup itself is somewhat artificial with identical LoRA configurations and data sizes at each step.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "253b297c-41b8-46d8-859f-57e71f82d615",
  "isSidechain": false,
  "requestId": "req_011CbAAvnxn8RUbEZ68mdzPy",
  "type": "assistant",
  "uuid": "a7de5e47-1764-4a45-8800-942b280298dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165SJJPjii7B8oKNmeyfcHd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 100524,
      "output_tokens": 2675,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 716,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2675,
          "cache_read_input_tokens": 100524,
          "cache_creation_input_tokens": 716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 716
          },
          "type": "message"
        }
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

_source line 77 · 2026-05-18T14:14:05.964Z_

审稿材料通读完毕，引用审计和写作风格检查已完成。现在搜索 ARR review form 的完整评分维度确认后，撰写审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7de5e47-1764-4a45-8800-942b280298dc",
  "isSidechain": false,
  "requestId": "req_011CbAAvnxn8RUbEZ68mdzPy",
  "type": "assistant",
  "uuid": "b5712525-adc5-481a-be7b-62dbc76c346e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165SJJPjii7B8oKNmeyfcHd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 100524,
      "output_tokens": 2675,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 716,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2675,
          "cache_read_input_tokens": 100524,
          "cache_creation_input_tokens": 716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 716
          },
          "type": "message"
        }
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

_source line 78 · 2026-05-18T14:14:12.183Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TRstrsFsNBFKKDkKziq5Wm`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the full list of review criteria/dimensions reviewers are asked to evaluate, their scoring scales, and any specific guidance on what constitutes different score levels for soundness, excitement, and overall assessment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5712525-adc5-481a-be7b-62dbc76c346e",
  "isSidechain": false,
  "requestId": "req_011CbAAvnxn8RUbEZ68mdzPy",
  "type": "assistant",
  "uuid": "726e9ac0-722d-4ed9-a4ca-2fa98aadb7a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165SJJPjii7B8oKNmeyfcHd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 100524,
      "output_tokens": 2675,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 716,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2675,
          "cache_read_input_tokens": 100524,
          "cache_creation_input_tokens": 716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 716
          },
          "type": "message"
        }
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

_source line 79 · 2026-05-18T14:14:17.643Z_

<details><summary>↩ Tool result · `toolu_01TRstrsFsNBFKKDkKziq5Wm`</summary>

```text
# ARR Review Criteria and Scoring Dimensions

Based on the ARR Reviewer Guidelines, reviewers evaluate papers using **three scoring dimensions**:

## 1. **Soundness**
This assesses technical validity and methodological rigor. The guidelines emphasize that "soundness scores must be justified by the text of the review." Low soundness scores require clear identification of specific flaws in methodology, proofs, experimental design, or argumentation.

## 2. **Excitement**
This reflects subjective interest and personal engagement with the work. The guidelines note this score is "orthogonal to the assessment of the soundness of the paper" and represents individual taste rather than objective quality judgments.

## 3. **Overall Assessment**
Described as "an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue," this is a composite score integrating soundness, excitement, novelty, and potential impact.

## Key Guidance

The guidelines stress that reviewers should recognize "a paper only needs to present sufficient evidence for the claim that the authors are making." They should distinguish between genuine weaknesses and subjective preferences, avoiding common pitfalls like dismissing work for being "too simple" or lacking SOTA results when such criteria don't apply to the paper's actual claims.

**Note:** The document does not specify precise numerical scales (e.g., 1-5 or 1-10) for these dimensions, suggesting the ARR review form itself contains this operational detail.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "726e9ac0-722d-4ed9-a4ca-2fa98aadb7a8",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "c1a864b3-ef9c-4dc2-a0e5-b903ee871fb9",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Review Criteria and Scoring Dimensions\n\nBased on the ARR Reviewer Guidelines, reviewers evaluate papers using **three scoring dimensions**:\n\n## 1. **Soundness**\nThis assesses technical validity and methodological rigor. The guidelines emphasize that \"soundness scores must be justified by the text of the review.\" Low soundness scores require clear identification of specific flaws in methodology, proofs, experimental design, or argumentation.\n\n## 2. **Excitement**\nThis reflects subjective interest and personal engagement with the work. The guidelines note this score is \"orthogonal to the assessment of the soundness of the paper\" and represents individual taste rather than objective quality judgments.\n\n## 3. **Overall Assessment**\nDescribed as \"an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue,\" this is a composite score integrating soundness, excitement, novelty, and potential impact.\n\n## Key Guidance\n\nThe guidelines stress that reviewers should recognize \"a paper only needs to present sufficient evidence for the claim that the authors are making.\" They should distinguish between genuine weaknesses and subjective preferences, avoiding common pitfalls like dismissing work for being \"too simple\" or lacking SOTA results when such criteria don't apply to the paper's actual claims.\n\n**Note:** The document does not specify precise numerical scales (e.g., 1-5 or 1-10) for these dimensions, suggesting the ARR review form itself contains this operational detail.",
    "durationMs": 5454,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "726e9ac0-722d-4ed9-a4ca-2fa98aadb7a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 80_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性 + 写作质量**  ### 论文信息 - **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints - **路径**: `proje…",
  "leafUuid": "c1a864b3-ef9c-4dc2-a0e5-b903ee871fb9",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Runtime record

_source line 81_

```json
{
  "type": "ai-title",
  "aiTitle": "Review recursive generation depth estimation paper",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Assistant

_source line 82 · 2026-05-18T14:14:26.676Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have all the information I need to compile a thorough review. Let me write it up.

Let me count approximate pages. The paper has:
- main.tex (just includes)
- abstract.tex (~7 lines of content)
- introduction.tex (~33 lines
- related_work.tex (~28 lines
- method.tex ~105 lines
- atlas.tex ~172 lines
- generalization.tex ~106 lines
- discussion.tex ~8 lines
- conclusion.tex (Limitations + Ethics) ~65 lines

The main body would be: abstract + intro + related work + method + atlas + generalization + discussion. 

That's roughly 8 pages of main content when accounting for the tables and figures, with a substantial appendix. Now let me start writing the review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1a864b3-ef9c-4dc2-a0e5-b903ee871fb9",
  "isSidechain": false,
  "requestId": "req_011CbAB22kPKMBCxFiTEgjmc",
  "type": "assistant",
  "uuid": "b84595ee-5480-4700-b60b-daa5e5bf4a61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEoWzJxCtiLAo8bq3maTDi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3008,
      "cache_read_input_tokens": 101240,
      "output_tokens": 5442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3008,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5442,
          "cache_read_input_tokens": 101240,
          "cache_creation_input_tokens": 3008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3008
          },
          "type": "message"
        }
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

_source line 83 · 2026-05-18T14:14:26.679Z_

审稿意见编写完成，准备汇报给 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b84595ee-5480-4700-b60b-daa5e5bf4a61",
  "isSidechain": false,
  "requestId": "req_011CbAB22kPKMBCxFiTEgjmc",
  "type": "assistant",
  "uuid": "e82fbcfb-4776-47cd-8ab9-afa87a49ae3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEoWzJxCtiLAo8bq3maTDi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3008,
      "cache_read_input_tokens": 101240,
      "output_tokens": 5442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3008,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5442,
          "cache_read_input_tokens": 101240,
          "cache_creation_input_tokens": 3008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3008
          },
          "type": "message"
        }
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

_source line 84 · 2026-05-18T14:16:29.140Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01JcacmU34dU2ver5rLKAfB6`</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## Summary\n\n本文将 recursive generation depth estimation 形式化为 ordinal classification 问题，构建了一个 180K 样本的 benchmark（3 model families × 3 decoding strategies × 4 depths），使用 19 维统计特征 + Random Forest 达到 69-86% 的四分类准确率。提出了 EDD (Effective Discriminable Depth) 指标，并通过 Depth Degradation Atlas 系统分析了 perplexity tail statistics 在不同配置下的 depth signal 稳定性。实验覆盖了 8 个泛化轴，包括 cross-model、cross-strategy、cross-scale 等。\n\n---\n\n## Strengths\n\n**S1. 问题定义有价值且清晰。** 将 recursive depth estimation 从 binary detection 推进到 ordinal classification 是一个自然且有意义的延伸。在 model collapse 已成为共识性问题的背景下，\"text 经历了多少轮递归生成\"是一个有实际应用价值的问题（Section 1）。EDD 的形式化定义（Definition 1, Eq. 1）操作性好，为后续研究提供了可比较的量化指标。\n\n**S2. 实验设计系统且全面。** 3×3 atlas grid 的设计有效隔离了 model family 和 decoding strategy 的贡献（Table 2: strategy gap 9.2pp vs model gap 7.2pp）。8 个 generalization axes 覆盖了大部分可能的 deployment scenarios。Domain bias 分析（Appendix §A.8）发现并修正了 seed-group confound 是诚实和严谨的做法。\n\n**S3. Feature consistency 是有洞察力的发现。** p90_ppl 在 9/9 cells 排名 top-2、var_surprisal 在 8/9 cells top-2（Table 3, §4.2），cross-model Spearman ρ=0.868，说明 depth signal 确实存在于分布层面的统计量中，而非 model-specific artifact。Feature hierarchy 随 depth 变化的发现（shallow: var_surprisal 主导 → deep: p90_ppl 主导，§4.2 倒数第二段）与 model collapse 理论一致且提供了操作性验证。\n\n**S4. Limitations 坦诚详尽。** d0 inflation、cross-strategy failure、high FPR on C4、adversarial robustness 未测试、EDD monotonicity assumption 等关键局限均被主动讨论。这在同类经验性论文中是高标准的做法。\n\n**S5. 写作整洁，无 AI 痕迹。** 全文无 em-dash、无 AI 高频词汇（leverage, utilize, delve 等）、无 -ing phrase 结尾模式。匿名化完整，未发现 self-citation leakage。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1 [critical] 方法论新颖性不足：RF + hand-crafted features 缺乏算法层面的贡献**\n- 具体位置：Section 3.3, 3.4\n- 问题：核心 pipeline 是\"提取 19 个统计特征 → 喂给 Random Forest\"，这是标准的 feature engineering + shallow ML，不涉及任何新的算法设计。EDD 本质上是在 pairwise AUC 序列上做阈值截断（Eq. 1），形式简单。Table 3（§5.1）进一步确认 RF、XGBoost、LightGBM 在同特征集上几乎无差异（Δ_max ≤ 0.4pp），说明贡献完全在特征设计而非分类方法。然而 19 个特征中有 14-16 个 VIF>10（§4.2），有效独立维度仅 4-5，本质上是一个低维问题。\n- 为什么影响接收：EMNLP 2026 期望方法论贡献或显著的新洞见。本文的方法贡献在 standard ML pipeline 范畴内，更像是 model collapse 理论的实验验证而非方法创新。\n- 建议：(1) 在 Introduction/Discussion 中更诚实地将论文定位为 empirical study + problem formalization，而非暗示方法创新；(2) 探索 perplexity 序列级别的 temporal features 或 token-level attention patterns 是否能超越 passage-level statistics。\n\n**N2 [critical] Discussion 过于简略，不符合一篇完整论文的标准**\n- 具体位置：Section 7（discussion.tex）\n- 问题：Discussion and Conclusion 合为一节，正文仅 1 段（约 7 行）。一篇声称有 5 项 contributions 的论文，Discussion 只用 1 段总结完毕是不充分的。论文缺少对以下问题的深入讨论：(a) depth signal 的本质来源——到底是 tail erosion、memorization 还是其他机制？(b) 与 Dohmatob et al. (2024) 理论预测的定量对比，而不仅是定性提及（\"qualitatively consistent with exponential decay but deviates quantitatively\" 只是一句话带过）；(c) practical deployment 的完整路径——strategy identification → depth estimation → data curation 的 pipeline 可行性。Appendix §A.17 (Extended Discussion) 有一些内容，但按 ACL format，核心 insight 应在正文讨论。\n- 为什么影响接收：审稿人期望 Discussion 是论文最有深度的部分，而不是实验结果的复述。当前状态显著降低论文的学术深度感。\n- 建议：将 Appendix 的 Extended Discussion 精华整合到正文，特别是 depth-graduated curation 的 vision 和 provenance toolkit 的定位。\n\n**N3 [critical] d0 inflation 严重扭曲了 headline metrics，核心能力（d1-d3 区分）表现有限**\n- 具体位置：Abstract、Table 2、Table 5\n- 问题：Depth-0 recall > 98% 在所有 9 cells 中几乎完美（Table 2），这本质上是 binary human-vs-machine detection，不是本文声称的新贡献。然而 abstract 和 contribution bullets 均报告包含 d0 的 headline numbers（69-86%、66.4% cross-model）。扣除 d0 后：cross-model transfer d1-d3 balanced accuracy 仅 55.4%（Table 5, chance = 33%），比 chance 仅高 22pp；within-distribution d2 recall 最低仅 45.6%（Pythia top-k, Appendix Table 7）。最弱的 cross-model 配置下 d2 recall 低至 26.8%（Pythia holdout, Table 5）。\n- 为什么影响接收：论文的核心新颖性在于从 binary detection 延伸到 ordinal depth estimation，但实际区分 d1/d2/d3 的能力远弱于 headline numbers 所暗示的。这构成了 claim 与 evidence 之间的显著落差。\n- 建议：Abstract 和 Contributions 应同时报告 d1-d3 balanced accuracy 作为\"去除 trivial d0 后\"的核心指标，不能只在 Limitations 中承认这一点。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] Abstract 将全部 19 个特征称为 \"perplexity-based\" 不准确**\n- 具体位置：Abstract 第 3 行\n- 问题：Abstract 写 \"A Random Forest over 19 perplexity-based features\"，但 Table 1（§3.3）明确列出 4 个 lexical diversity 特征和 3 个 repetition 特征，这 7 个特征不依赖 reference model perplexity。虽然 §A.16 (Feature Group Ablation) 表明 perplexity features 确实是主导（-0.5pp vs full），但 abstract 的措辞构成事实性描述错误。\n- 建议：改为 \"19 statistical features\" 或 \"19 features anchored in reference-model perplexity statistics\"。\n\n**W2 [warning] Cross-strategy transfer 近乎失败，实用性受限**\n- 具体位置：Section 5.3, Table 6\n- 问题：Cross-strategy d1-d3 accuracy 仅 45.9%（chance = 33%），仅高出 chance 12.9pp。更严重的是，训练于 nucleus + top-k 测试 temperature 时出现 d1/d2 boundary inversion（AUC < 0.5）。论文在 Limitations 提出 two-stage pipeline 作为解决方案但未在正文验证。在实际应用中 decoding strategy 通常未知，这严重限制了部署场景。\n- 建议：在正文（而非仅 Limitations）中对 two-stage pipeline 的可行性提供实验验证。\n\n**W3 [warning] 主实验仅使用 1-1.5B 模型，在 2026 年标准下偏小**\n- 具体位置：Section 3.2, §5.4\n- 问题：Primary benchmark 全部使用 1-1.5B 模型，cross-scale 实验（7-8B）仅用 500 samples/depth（vs 主实验 5000），且引入 QLoRA 量化等额外 confounds（Appendix §A.12）。在 2026 年 frontier models 已达 100B+ 的背景下，1.5B models 的结论向更大规模的推广存疑。7B 模型准确率下降到 60-70%（Table in §A.12），且 Qwen2.5-7B 出现 non-monotonic AUC，说明 scale 确实改变了 degradation dynamics。\n- 建议：至少将一个 7-8B 模型提升到 primary benchmark 的 sample size（5000/depth）并消除 quantization confound。\n\n**W4 [warning] 与 Dohmatob et al. (2024) 的关系定位不够诚实**\n- 具体位置：Related Work §2.1, Discussion §7\n- 问题：Dohmatob et al. (2024) 已理论预测 recursive training erodes distributional tails as a scaling law。本文的 core finding（perplexity tail statistics are depth markers）本质上是这一理论的实验验证。Related Work 中虽提到\"we operationalize this prediction\"（§2.1 第 8 行），但 Contributions 列表和 Abstract 的措辞将此包装为独立发现而非验证。Discussion 仅用一句 \"LoRA fine-tuning loss decreases monotonically with depth... a direct empirical validation\" 承认了这一点。\n- 建议：在 Introduction 中更明确地说明与 Dohmatob 理论的关系——本文贡献是将理论预测 operationalize 为 deployable classifier 并发现 strategy-dependent 偏差，而非独立发现 tail erosion。\n\n**W5 [warning] Downstream curation PoC 结论不支持核心 narrative**\n- 具体位置：Appendix §A.11 (Table 11, 12)\n- 问题：RF-filtered vs unfiltered 的 PPL 差异不显著（p > 0.4, Table 12 最后一行）。虽然 RF-filtered vs random subsampling 显著（p < 0.001），但这只说明 depth-aware selection 比 random 好，不说明 depth filtering 本身有实际价值。Oracle_strict 甚至比 unfiltered 更差（-0.103 PPL, Table 11），暗示 depth 信息对 downstream quality 的作用并不直接。这与 §7 中 \"RF-filtered subsets outperform random subsampling (p<0.001)\" 的叙述不矛盾，但削弱了论文作为 practical tool 的叙事。\n- 建议：承认 curation PoC 的局限性更到位一些，当前在 Discussion 中只引用了 p<0.001 的正面结果而忽略了 p>0.4 的核心对比。\n\n### Minor 问题（不影响接收）\n\n**M1** Abstract 中 \"43 pp below RF\"：RF 78.7% vs DeepSeek 36.2% = 42.5pp，应为 \"≈43 pp\" 或修正为准确值。\n\n**M2** References 中有 3 个 orphan bib entries（在 .bib 中但正文未引用）：bevendorff2025_two_paradigms, pareek2024understanding, shi2025_closer_look。应清理或引用。\n\n**M3** knowledge_collapse2025 和 falahati2026_curated 在 OpenAlex 中未找到（可能是非常新的 preprints），建议验证 arXiv ID 是否正确。\n\n**M4** Section 7 标题为 \"Discussion and Conclusion\" 但没有 Conclusion 的实质内容（仅 Discussion + 一句总结）。Limitations 和 Ethics Statement 在 conclusion.tex 中作为 unnumbered sections 出现在正文之后，结构上合规但 Discussion 的空洞使得论文缺乏收束感。\n\n**M5** Table 2 caption 提到 \"d1–d3 three-class accuracy in parentheses (chance = 25% / 33%)\"——三分类 chance 应为 33.3%，但 caption 混写了 25%（四分类 chance）和 33%（三分类 chance），可能造成困惑。\n\n---\n\n## Questions（需要作者回答的问题）\n\n**Q1** 如果将 d0 样本完全排除，仅做 d1/d2/d3 三分类，in-distribution 和 cross-model transfer 的 balanced accuracy 分别是多少？Table 2 括号中有部分数据，但 cross-model transfer（Table 5）只报告了 mean 55.4%，缺少每个 holdout 的 d1-d3 balanced accuracy 的 confidence interval。\n\n**Q2** Perplexity tail statistics 作为 depth marker 的根本原因是什么？是 LoRA fine-tuning 特有的（低秩近似导致 tail compression），还是任何 fine-tuning 方法都会产生？如果用 full fine-tuning 替代 LoRA，depth signal 是否持续存在？这关系到方法的 generality claim。\n\n**Q3** 论文生成 pipeline 使用 BOS-seeded（无 prompt）生成，prompted generation 降低了 13.8pp（§5.3）。真实的 recursive contamination 场景（如 web crawl → training → deployment → web crawl）中的 prompt conditioning 比论文的 topic-seeded 实验更复杂。作者如何评估从 controlled setting 到 wild 的 generalization gap？\n\n**Q4** Cross-model chains（§A.13）达到 84.75%，高于 within-model 的部分配置。这是否因为不同 model family 在每个 depth 引入了更大的分布差异（使分类更容易），而非证明 depth signal 是 process-level 的？reverse-chain control 的等价准确率可以排除 architecture fingerprinting，但不能排除\"跨架构 = 更大分布 shift = 更容易分类\"的替代解释。\n\n---\n\n## Missing References\n\n1. **Shumailov et al. 2024** \"AI models collapse when trained on recursively generated data\" (Nature) — 已引用 ✓\n2. Alemohammad et al. \"Self-Consuming Generative Models Go MAD\" — 已引用 ✓\n3. 可能缺失：**Shumailov et al. 2023** \"The Curse of Recursion: Training on Generated Data Makes Models Forget\" (原始 arXiv 版本) — 应确认是否为同一论文的不同版本\n4. 可能缺失：关于 **data provenance / data lineage** 的工作（如 C2PA / Content Credentials 标准），这与论文声称的 provenance toolkit vision 直接相关\n\n---\n\n## Overall Assessment\n\n**Overall**: **3.0 — Findings**\n**Soundness**: 3.5/5 — 实验设计系统，统计方法正确（bootstrap CIs、stratified CV、domain bias controls），但 d0 inflation 使 headline claims 与实际能力之间存在落差；cross-strategy 近乎失败是实用性的重大限制。\n**Excitement**: 2.5/5 — 问题定义有价值，但方法（RF + 手工特征）缺乏技术兴奋点；核心发现（perplexity tail erosion = depth marker）在 Dohmatob et al. 理论框架下是可预期的。\n**Reproducibility**: 4/5 — 超参数、硬件、软件版本均详列（Appendix §A.18），承诺代码开源。\n**Confidence**: 4/5 — 对 AI text detection、model collapse、ordinal classification 三个领域均较熟悉。\n\n**简要理由**: 本文在问题形式化（recursive depth estimation as ordinal classification）和系统实验方面有实质贡献，Limitations 处理诚实。但方法论新颖性有限（standard feature engineering + RF），Discussion 过于简略，且核心能力（d1-d3 区分）远弱于 headline metrics 所暗示。作为 Findings 论文合适——empirical contribution solid but not sufficient for main conference given limited methodological novelty and the gap between headline claims and d1-d3 discrimination performance。",
  "reviewer_id": "2",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e82fbcfb-4776-47cd-8ab9-afa87a49ae3a",
  "isSidechain": false,
  "requestId": "req_011CbAB22kPKMBCxFiTEgjmc",
  "type": "assistant",
  "uuid": "aa086d51-b47a-42ac-bbf7-bf8fe7ddba54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEoWzJxCtiLAo8bq3maTDi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3008,
      "cache_read_input_tokens": 101240,
      "output_tokens": 5442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3008,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5442,
          "cache_read_input_tokens": 101240,
          "cache_creation_input_tokens": 3008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3008
          },
          "type": "message"
        }
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

_source line 85 · 2026-05-18T14:16:33.305Z_

<details><summary>↩ Tool result · `toolu_01JcacmU34dU2ver5rLKAfB6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa086d51-b47a-42ac-bbf7-bf8fe7ddba54",
  "isSidechain": false,
  "promptId": "ce60f097-7b35-414f-90ef-e73f0c2dd730",
  "type": "user",
  "uuid": "77331b45-bb29-43c9-8e77-4c7f054fda60",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "aa086d51-b47a-42ac-bbf7-bf8fe7ddba54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 86_

```json
{
  "type": "ai-title",
  "aiTitle": "Review recursive generation depth estimation paper",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Runtime record

_source line 87 · 2026-05-18T14:17:42.776Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T14:17:42.776Z",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "content": "[Round 1 审稿请求]:\n## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见（侧重：方法严谨性 + 实验设计）。请逐条回应：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（引用具体 Section/Table/Figure）\n  \n---\n\n**Reviewer 1 评分：Overall 3.5 (Borderline Conference)**，Soundness 3.5，Excitement 3.5\n\n### Must-Fix 问题\n\n**R1-N1 [critical] EDD 指标的统计声明与证据不匹配**\nEDD_{0.75}=4 声称\"all three models cross the T=0.75 threshold within the d3-d4 region\"，但 bootstrap 检验：Pythia p=0.001（显著），OLMo p=0.091（边缘），GPT-2 XL p=0.505（不显著）。仅 1/3 模型在 α=0.05 下显著。Abstract/Introduction 的 EDD_{0.75}=4 报告未充分传达不确定性。建议：(1) 明确 EDD=4 仅对 Pythia 显著；(2) 报告所有 9 cells 的 bootstrap p；(3) 考虑 T=0.70 作为更稳健的主指标。\n\n**R1-N2 [critical] 单 LoRA 种子构成系统性混淆因子**\nAtlas 每 cell 用单一 LoRA 种子，跨种子复制仅覆盖 2/9 cells（Pythia/GPT-2 XL nucleus），且 GPT-2 XL CI 不重叠（[83.89, 84.77] vs [86.17, 86.49]，差 2.04pp）。报告的跨模型效应（7.2pp）和跨策略效应（9.2pp）可能被 LoRA 种子噪声污染。建议：至少对关键 cells 做 3 种子复制。\n\n**R1-N3 [critical] 序数分类形式化与实际方法/指标不一致**\n§3.1 定义为 ordinal classification，但 RF 不利用序数结构；CORAL（真正序数方法）仅作 baseline 且无显著差异（78.1% vs 78.7%）；全文无 MAE、QWK 等序数指标。如果序数方法不优于非序数方法且不报告序数指标，序数形式化的动机何在？\n\n### Should-Fix 问题\n\n**R1-W1** d0 膨胀 headline metrics——cross-model 66.4% 中 d1-d3 balanced accuracy 仅 55.4%。\n\n**R1-W2** 跨策略迁移失败（d1-d3 仅 45.9%，d1/d2 boundary inversion）是根本性实用限制，但未被充分强调。\n\n**R1-W3** 跨规模 7-8B 实验四个同时变化的 confounds 未隔离。\n\n**R1-W4** 参考模型 Pythia-1.4B 同时作为生成器之一，self-reference vs cross-reference 非对称性。\n\n**R1-W5** 下游 curation PoC RF vs unfiltered 不显著（p>0.4），仅 RF vs random 显著。\n\n### Minor 问题\nM1: EDD binary classifiers 500 trees vs 主实验 200 trees 不一致。M2: Table 2 括号值不够清晰。M3: 19 特征选择缺乏系统论证。M4: Discussion 仅一段，过于压缩。M5: Prompted generation 仅 1 cell。M6: Curation PoC 未做多重比较校正。\n\n### Missing References\n1. Pareek et al. 2024 (repeated self-distillation)——已在 bib 但未引用。\n2. Janitza et al. 2016 (ordinal random forest)——ordinal RF 应作 baseline 或在 Related Work 讨论。\n3. SemEval-2024 Task 8 后续分析。\n\n### Questions\nQ1: MAE 和 QWK 是多少？相邻类别错误占比？\nQ2: 默认 T 改为 0.70 是否改变核心叙事？\nQ3: 为什么 cross-model chains 只测一种链序 + 反向控制？\nQ4: 用完全无关架构（如 T5/encoder-only）作参考模型会怎样？\nQ5: Pythia 的 C4 FPR 按深度类别的分布？\n\n---\n\n请对以上每条 Must-Fix、Should-Fix 和 Questions 给出 [AGREE] 或 [REBUT] 回应。"
}
```

---


### Runtime record

_source line 88 · 2026-05-18T14:17:42.776Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T14:17:42.776Z",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


## Round 2

## Round 2

2 recorded events


### User

_source line 89 · 2026-05-18T14:17:42.762Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77331b45-bb29-43c9-8e77-4c7f054fda60",
  "isSidechain": false,
  "promptId": "304617e2-8d90-4269-acdb-c046093b1682",
  "type": "user",
  "isMeta": true,
  "uuid": "126dce82-3e8c-4cdf-a434-a575093406ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 90 · 2026-05-18T14:17:42.762Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "126dce82-3e8c-4cdf-a434-a575093406ef",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "6edb23d4-e761-49bf-b710-7efe9793e3b0",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "e37683be-dea6-4979-85e6-9ef79c146184",
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

11 recorded events


### User

_source line 91 · 2026-05-18T14:17:42.861Z_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见（侧重：方法严谨性 + 实验设计）。请逐条回应：
- **[AGREE]**：同意并说明理由
- **[REBUT]**：反驳并提供证据（引用具体 Section/Table/Figure）
  
---

**Reviewer 1 评分：Overall 3.5 (Borderline Conference)**，Soundness 3.5，Excitement 3.5

### Must-Fix 问题

**R1-N1 [critical] EDD 指标的统计声明与证据不匹配**
EDD_{0.75}=4 声称"all three models cross the T=0.75 threshold within the d3-d4 region"，但 bootstrap 检验：Pythia p=0.001（显著），OLMo p=0.091（边缘），GPT-2 XL p=0.505（不显著）。仅 1/3 模型在 α=0.05 下显著。Abstract/Introduction 的 EDD_{0.75}=4 报告未充分传达不确定性。建议：(1) 明确 EDD=4 仅对 Pythia 显著；(2) 报告所有 9 cells 的 bootstrap p；(3) 考虑 T=0.70 作为更稳健的主指标。

**R1-N2 [critical] 单 LoRA 种子构成系统性混淆因子**
Atlas 每 cell 用单一 LoRA 种子，跨种子复制仅覆盖 2/9 cells（Pythia/GPT-2 XL nucleus），且 GPT-2 XL CI 不重叠（[83.89, 84.77] vs [86.17, 86.49]，差 2.04pp）。报告的跨模型效应（7.2pp）和跨策略效应（9.2pp）可能被 LoRA 种子噪声污染。建议：至少对关键 cells 做 3 种子复制。

**R1-N3 [critical] 序数分类形式化与实际方法/指标不一致**
§3.1 定义为 ordinal classification，但 RF 不利用序数结构；CORAL（真正序数方法）仅作 baseline 且无显著差异（78.1% vs 78.7%）；全文无 MAE、QWK 等序数指标。如果序数方法不优于非序数方法且不报告序数指标，序数形式化的动机何在？

### Should-Fix 问题

**R1-W1** d0 膨胀 headline metrics——cross-model 66.4% 中 d1-d3 balanced accuracy 仅 55.4%。

**R1-W2** 跨策略迁移失败（d1-d3 仅 45.9%，d1/d2 boundary inversion）是根本性实用限制，但未被充分强调。

**R1-W3** 跨规模 7-8B 实验四个同时变化的 confounds 未隔离。

**R1-W4** 参考模型 Pythia-1.4B 同时作为生成器之一，self-reference vs cross-reference 非对称性。

**R1-W5** 下游 curation PoC RF vs unfiltered 不显著（p>0.4），仅 RF vs random 显著。

### Minor 问题
M1: EDD binary classifiers 500 trees vs 主实验 200 trees 不一致。M2: Table 2 括号值不够清晰。M3: 19 特征选择缺乏系统论证。M4: Discussion 仅一段，过于压缩。M5: Prompted generation 仅 1 cell。M6: Curation PoC 未做多重比较校正。

### Missing References
1. Pareek et al. 2024 (repeated self-distillation)——已在 bib 但未引用。
2. Janitza et al. 2016 (ordinal random forest)——ordinal RF 应作 baseline 或在 Related Work 讨论。
3. SemEval-2024 Task 8 后续分析。

### Questions
Q1: MAE 和 QWK 是多少？相邻类别错误占比？
Q2: 默认 T 改为 0.70 是否改变核心叙事？
Q3: 为什么 cross-model chains 只测一种链序 + 反向控制？
Q4: 用完全无关架构（如 T5/encoder-only）作参考模型会怎样？
Q5: Pythia 的 C4 FPR 按深度类别的分布？

---

请对以上每条 Must-Fix、Should-Fix 和 Questions 给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6edb23d4-e761-49bf-b710-7efe9793e3b0",
  "isSidechain": false,
  "promptId": "304617e2-8d90-4269-acdb-c046093b1682",
  "type": "user",
  "uuid": "8b1459f2-507d-4163-9f43-31aebe8fd7ae",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 92 · 2026-05-18T14:18:29.798Z_

<details><summary>Logged reasoning block</summary>

```text
The Director is asking me (Reviewer 2) to respond to each of Reviewer 1's points with [AGREE] or [REBUT]. I need to go through each item systematically, drawing on my own reading of the paper to provide an independent assessment.

Let me go through each point:

**R1-N1: EDD statistical claims vs evidence mismatch**
R1 says EDD_{0.75}=4 is only significant for 1/3 models. Let me check the paper. In §4.4 (atlas.tex lines 127-131): "bootstrap testing (10,000 resamples, H_0: AUC ≤ 0.75) yields p = 0.001 for Pythia (significant), p = 0.091 for OLMo (marginal), and p = 0.505 for GPT-2 XL (non-significant). 

The paper does show all three models crossing the 0.75 threshold in the d3–d4 region, but with varying statistical confidence levels. The abstract qualifies the finding to "best-characterized family" (Pythia), so the claim isn't actually as broad as R1 suggests—though I should verify whether the main text oversells this finding beyond what the abstract promises. The Abstract's phrasing about the "best-characterized family" is appropriate, though the point about T=0.70 being more robust is worth considering—I'll partially concede there. On the LoRA seed issue, the paper does address this in the Limitations section, and the cross-seed replication results show the direction can flip significantly for some models while feature rankings stay consistent, which suggests the concern is valid but perhaps not critical given the stability of top findings.

For the ordinal classification framing, R1 makes a strong point—the paper doesn't actually use methods that exploit ordinal structure, and CORAL showed no improvement. The absence of ordinal metrics like MAE or QWK is a legitimate gap I should acknowledge. That said, the problem is inherently ordinal regardless of method choice, and the EDD metric itself does leverage that structure, so the formalization isn't entirely unmotivated. The negative result on CORAL is actually informative. I'll agree the metrics should be reported but push back slightly on whether the ordinal framing itself is problematic.

Now I'm moving to the d0 inflation concern—

that's already something I flagged, so I agree with R1 there. Same with the cross-strategy transfer failure and cross-scale confounds; those were both weaknesses I identified independently.

On the reference model asymmetry issue, the paper does address this directly. It shows that using Pythia as both generator and reference doesn't create a systematic advantage—Pythia's accuracy (78.7%) actually underperforms GPT-2 XL (85.9%), which they explicitly note in both the methods section and limitations. There's also a reference model ablation in the appendix that explores this further.

The inconsistency between 500 trees for the binary EDD classifiers and 200 trees for the main 4-class random forest is a fair point—that's not well justified in the paper. And the Table 2 parentheses issue is valid too; hiding the d1-d3 accuracy in parentheses makes it less prominent than it should be.

On the 19 features, the justification is partial. They're standard statistical measures, but the paper doesn't systematically explain why these specific ones were chosen over alternatives.

R1 also flagged that the discussion section is too brief, which I'd already noted as a weakness. The prompted generation testing is limited to just one model variant, and the curation proof-of-concept lacks multiple comparison correction across the 8 conditions tested.

For the missing references, Pareek et al. is indeed orphaned in the bibliography, and the ordinal random forest work by Janitza et al. seems relevant to the ranking task. The SemEval-2024 follow-ups are worth acknowledging too.

Going through the specific questions: the MAE/QWK metric choice matters, and the default temperature of 0.70 deserves exploration. The chain-of-thought experiments only cover 2 out of 6 possible orderings, so that's a partial strength. T5 and encoder-only baselines would be interesting comparisons, and for the C4 false positive distribution by depth, the paper actually addresses this in the appendix with specific percentages for both GPT-2 XL and OLMo across the three depth levels.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b1459f2-507d-4163-9f43-31aebe8fd7ae",
  "isSidechain": false,
  "requestId": "req_011CbABH9pTVFndvYBGKHeAT",
  "type": "assistant",
  "uuid": "222a4a64-a887-4809-8231-037b93598b77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184qEJgPpb6XLzrkqSrU28V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 109763,
      "output_tokens": 6304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6304,
          "cache_read_input_tokens": 109763,
          "cache_creation_input_tokens": 1407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1407
          },
          "type": "message"
        }
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

_source line 93 · 2026-05-18T14:18:29.801Z_

逐条回应 Reviewer 1 的审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "222a4a64-a887-4809-8231-037b93598b77",
  "isSidechain": false,
  "requestId": "req_011CbABH9pTVFndvYBGKHeAT",
  "type": "assistant",
  "uuid": "a5582ba9-b28f-4619-8477-e740b60b53e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184qEJgPpb6XLzrkqSrU28V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 109763,
      "output_tokens": 6304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6304,
          "cache_read_input_tokens": 109763,
          "cache_creation_input_tokens": 1407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1407
          },
          "type": "message"
        }
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

_source line 94 · 2026-05-18T14:19:54.477Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01JBhfxVqKjnzaavM2SCZ9x8`</summary>

```json
{
  "text": "## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R1-N1: EDD 指标的统计声明与证据不匹配**\n\nR1 的核心论点——仅 1/3 模型在 α=0.05 下显著——事实成立，但论文的措辞比 R1 描述的更谨慎。\n\nAbstract 写的是 \"EDD_{0.75}=4 **for the best-characterized family**\"（abstract.tex L5），已限定为 Pythia。Introduction contribution #2 完整列出了三个 p 值（\"p=0.001 for Pythia... p=0.091 for OLMo, p=0.505 for GPT-2 XL\"，introduction.tex L26），并用\"graded statistical confidence rather than uniform statistical significance\"修饰（atlas.tex L130）。因此论文并未隐藏不确定性。\n\n不过 R1 关于使用 T=0.70 作为更稳健主指标的建议有道理。在 T=0.70 下，8/9 cells 达到 EDD≥3（Table 4），且 Llama-3.1-8B 也达到 EDD=4（Appendix Table in §A.12）。以 T=0.70 为主、T=0.75 为辅可能更平衡。\n\n结论：论文的文本表述尚可接受，但建议采纳 T=0.70 作为主指标，这是 constructive 的改进方向。不构成\"statistical claims vs evidence mismatch\"的 critical 问题。\n\n---\n\n**[AGREE] R1-N2: 单 LoRA 种子构成系统性混淆因子**\n\n同意这是一个真实的实验设计局限。\n\n论文仅在 2/9 cells（Pythia、GPT-2 XL nucleus）做了 cross-seed replication（Appendix §A.14, Table 15），GPT-2 XL 两种子的 CI 不重叠（[83.89, 84.77] vs [86.17, 86.49]，差 2.04pp）。虽然论文辩称\"direction reversal across models confirms bidirectional noise rather than systematic bias\"（conclusion.tex L51），且 top-5 feature importance 跨种子一致（Appendix §A.14 最后一段），但 2.04pp 的种子效应确实可能污染跨模型效应（7.2pp）和跨策略效应（9.2pp）的解读。\n\n然而，我将此定为 **should-fix** 而非 critical：feature ranking 的稳定性（top-5 identical across seeds for both models）说明 depth signal 的结构性特征不受种子影响，准确率的绝对值波动不改变论文的核心叙事（perplexity tail statistics 作为 depth marker 的一致性）。3 种子复制是合理改进但不是论文可接受性的 blocker。\n\n---\n\n**[AGREE] R1-N3: 序数分类形式化与实际方法/指标不一致**\n\n这是 R1 最有力的批评，我完全同意。\n\n论文在 §3.1 将问题形式化为 ordinal classification（\"depths carry a natural ordering, and d=1 is structurally closer to d=0 than d=3 is\"，method.tex L12），但：\n1. 主分类器 RF 不利用序数结构——它将 d0/d1/d2/d3 视为无序标签\n2. CORAL（真正的序数方法）仅在 1 cell 测试且与 RF 无显著差异（78.1% vs 78.7%，generalization.tex L10）\n3. 全文无任何序数指标（MAE、QWK、adjacent-class error ratio）——所有报告的 accuracy 和 balanced accuracy 均为 nominal classification metrics\n\n这构成了 framing 与 execution 之间的不一致。问题本身确实是序数的（d1 比 d3 更接近 d0），EDD 定义也利用了 adjacent-pair 的序数结构（Definition 1, Eq. 1）。但如果 (a) 序数方法不优于名义方法，且 (b) 不报告序数指标，那么 ordinal classification 的形式化更多是 positioning 而非技术贡献。\n\n我的建议与 R1 一致：至少应报告 MAE 和 QWK，以及相邻类别 vs 非相邻类别的 confusion 分布。如果 d1→d3 的错误确实少于 d1→d2，那就是序数结构的经验证据。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: d0 膨胀 headline metrics**\n\n完全同意。这与我的 N3 一致。cross-model d1-d3 balanced accuracy 仅 55.4%（Table 5），within-distribution d2 recall 最低 45.6%（Pythia top-k, Appendix Table 7）。Abstract 和 Contributions 必须同时报告去 d0 后的核心指标。\n\n---\n\n**[AGREE] R1-W2: 跨策略迁移失败**\n\n完全同意。与我的 W2 一致。d1-d3 仅 45.9%（Table 6），d1/d2 boundary inversion（AUC < 0.5）是部署层面的根本性限制。two-stage pipeline 仅在 Limitations 中提及但缺乏实验验证。\n\n---\n\n**[AGREE] R1-W3: 跨规模 7-8B confounds 未隔离**\n\n同意。与我的 W3 一致。4-bit QLoRA 量化、样本量缩减（500 vs 5000）、仅 nucleus sampling、vocabulary mismatch 四个 confounds 同时引入（Appendix §A.12 Confounds 段落自己承认了这四点）。论文无法归因 60-70% vs 78-85% 的 accuracy gap 到任何单一因素。\n\n---\n\n**[REBUT] R1-W4: 参考模型 Pythia-1.4B 同时作为生成器之一的非对称性**\n\nR1 的 concern 概念上成立，但论文已提供充分的经验证据来 address 这一点：\n\n1. Self-reference 没有系统性优势：Pythia（self-reference）78.7% **低于** GPT-2 XL（cross-reference）85.9%（Table 2），方向与\"self-reference 有利\"的假设相反\n2. Reference model ablation（Appendix §A.10, Table 13）：三种参考模型（Pythia self: 78.6%, OLMo cross: 74.5%, GPT-2 XL cross: 67.3%）均远超 chance，且 same-family reference 的优势（最大 11pp）方向一致\n3. Limitations 专门讨论了这一点（conclusion.tex L39-47），结论是 \"the overlap therefore does not confer a systematic advantage\"\n\n如果 self-reference 提供了不公平优势，我们应该观察到 Pythia 系统性地优于其他模型——但实际上 GPT-2 XL 在所有策略下都是最高的。论文的证据链在这一点上是完整的。\n\n---\n\n**[AGREE] R1-W5: 下游 curation PoC 不显著**\n\n同意。与我的 W5 一致。RF-filtered vs unfiltered p > 0.4（Table 12 最后一行），oracle_strict 甚至比 unfiltered 更差（-0.103 PPL, Table 11）。Discussion（discussion.tex L7）只引用了 RF vs random 的 p<0.001 而回避了 RF vs unfiltered 的不显著结果，构成 selective reporting。\n\n---\n\n### Minor 问题\n\n**[AGREE] R1-M1: 500 vs 200 trees 不一致**\n成立。EDD binary classifiers 用 500 trees（method.tex L85），主 4-class RF 用 200 trees（atlas.tex L11）。虽然 RF 对树数量不敏感（通常 200+ 足够），但应说明理由或统一。\n\n**[AGREE] R1-M2: Table 2 括号值不够清晰**\n成立。d1-d3 三分类 accuracy 被放在括号内作为次要信息，但这实际上是更有意义的指标（排除了 trivially-separable d0）。\n\n**[AGREE] R1-M3: 19 特征选择缺乏系统论证**\n部分同意。特征选择是 standard statistical features（moments, quantiles, diversity, repetition），但论文未解释为什么恰好是这 19 个而不是更多或更少。考虑到 VIF>10 的有 14-16 个（§4.2），是否应该在一开始就做 feature selection 以减少冗余？\n\n**[AGREE] R1-M4: Discussion 过于压缩**\n强烈同意。这与我的 N2 一致。我将其列为 critical 而非 minor，因为这是论文整体完整性的问题。\n\n**[AGREE] R1-M5: Prompted generation 仅 1 cell**\n成立。仅 GPT-2 XL nucleus（Appendix §A.17, Table 17）。鉴于 prompted generation 更贴近真实场景，至少应覆盖 2-3 个 model-strategy cells。\n\n**[AGREE] R1-M6: Curation PoC 未做多重比较校正**\n成立。8 条件 vs unfiltered 的 paired t-tests（Table 11-12）未做 Bonferroni 或 FDR 校正。虽然核心对比（RF vs random）的 p 值很低（<0.001），但完整性上应做校正。\n\n---\n\n### Missing References\n\n**[AGREE] R1-MR1: Pareek et al. 2024 (repeated self-distillation)**\n确认在 bib 中但 orphan（我的引用审计也检测到这一点）。应在 Related Work §2.1 引用或删除。\n\n**[AGREE] R1-MR2: Janitza et al. 2016 (ordinal random forest)**\n好建议。ordinal RF 是 ordinal classification + random forest 交叉领域的直接相关工作。论文将 RF 作为主分类器且声称 ordinal classification 形式化，不引用 ordinal RF 是遗漏。\n\n**[AGREE] R1-MR3: SemEval-2024 Task 8 后续分析**\n同意。论文引用了 Wang et al. 2024（M4-SemEval），但 shared task 的后续分析（participant systems 的分析论文）可能包含与 ordinal depth 相关的 multi-class detection insights。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1: MAE 和 QWK？**\n同意这是必要的补充指标，与 R1-N3 直接相关。如果 confusion 主要发生在相邻类别而非跨多类别，那就是序数结构的经验证据。\n\n**[AGREE] R1-Q2: T=0.70 是否改变核心叙事？**\n同意值得回答。从 Table 4 看，T=0.70 下 8/9 cells 达 EDD≥3（vs T=0.75 下 7/9），差异不大。核心叙事不太可能改变，但以 T=0.70 为主指标更稳健。\n\n**[REBUT] R1-Q3: 为什么 cross-model chains 只测一种链序 + 反向控制？**\n论文实际上已提供了 R1 问的信息的核心部分：forward chain（Pythia→OLMo→GPT-2 XL: 84.75%）和 reverse chain（GPT-2 XL→OLMo→Pythia: 85.75%）的准确率统计不可区分（Appendix §A.13, 95% CIs 重叠），且论文明确说明了 reverse chain 的设计目的是\"empirically test the architecture confound hypothesis\"（section_appendix.tex L419）。两个方向的等效结果在逻辑上排除了 architecture fingerprinting。当然测试更多排列更好，但 2/6 排列已提供了有力的 falsification 证据。\n\n**[AGREE] R1-Q4: 用 T5/encoder-only 作参考模型？**\n好问题。当前三种参考模型（Pythia, OLMo, GPT-2 XL）都是 decoder-only autoregressive LMs。用 encoder-only 模型（如 BERT/RoBERTa）计算 perplexity 特征是否可行、以及是否产生不同的 depth signal，是一个有意义的 ablation。\n\n**[REBUT] R1-Q5: Pythia 的 C4 FPR 按深度类别的分布？**\n论文已在 Appendix §A.9（section_appendix.tex L245）提供了这一数据：\"Among C4 false positives for GPT-2 XL, predictions distribute as d1 (9.0%), d2 (3.7%), d3 (9.6%); for OLMo, d1 (2.9%), d2 (0.5%), d3 (1.3%).\" Pythia 的具体分布未单独列出但可从总 FPR 20.2% 推算。R1 可能遗漏了这一 appendix 数据。不过补充 Pythia 的 per-depth FPR 分布确实有助于完整性。\n\n---\n\n### 总结\n\nR1 和我（R2）在以下问题上高度一致：\n- **d0 inflation** 是核心问题（R1-W1 = 我的 N3）\n- **Cross-strategy failure** 限制实用性（R1-W2 = 我的 W2）\n- **Discussion 过于简略**（R1-M4 = 我的 N2）\n- **Curation PoC 不支持叙事**（R1-W5 = 我的 W5）\n- **7-8B confounds 未隔离**（R1-W3 = 我的 W3）\n\nR1 独特的贡献是 **R1-N3（ordinal 形式化与实际方法的不一致）**，这是一个我忽略但完全同意的深层问题。\n\n我与 R1 的主要分歧在于：\n- **R1-N1**（EDD 统计声明）：论文措辞比 R1 描述的更谨慎，不构成 critical 问题\n- **R1-W4**（参考模型非对称性）：论文的经验证据链（self-reference 无优势 + ablation）足以 address\n- **R1-N2**（LoRA 种子）：我同意问题存在但认为 severity 应为 should-fix 而非 critical，因为 feature ranking 稳定\n\n综合两份审稿意见，我维持 **Overall 3.0 (Findings)** 评分。R1 的 N3（ordinal formalization 不一致）加强了方法论贡献不足的判断。",
  "reviewer_id": "2",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5582ba9-b28f-4619-8477-e740b60b53e2",
  "isSidechain": false,
  "requestId": "req_011CbABH9pTVFndvYBGKHeAT",
  "type": "assistant",
  "uuid": "9347dbf4-babe-419c-9056-db409e61d9e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184qEJgPpb6XLzrkqSrU28V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 109763,
      "output_tokens": 6304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6304,
          "cache_read_input_tokens": 109763,
          "cache_creation_input_tokens": 1407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1407
          },
          "type": "message"
        }
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

_source line 95_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见  以下是 Reviewer 1 的完整审稿意见（侧重：方法严谨性 + 实验设计）。请逐条回应： - **[AGREE]**：同意并说明理由 - **[REBUT]**：反驳并提供证据（引用具体 Section/Table/Figure）    ---  **Reviewer 1 评分：Overall…",
  "leafUuid": "9347dbf4-babe-419c-9056-db409e61d9e9",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Runtime record

_source line 96_

```json
{
  "type": "ai-title",
  "aiTitle": "Review recursive generation depth estimation paper",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Tool result

_source line 97 · 2026-05-18T14:19:58.473Z_

<details><summary>↩ Tool result · `toolu_01JBhfxVqKjnzaavM2SCZ9x8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9347dbf4-babe-419c-9056-db409e61d9e9",
  "isSidechain": false,
  "promptId": "304617e2-8d90-4269-acdb-c046093b1682",
  "type": "user",
  "uuid": "cfcd811c-8768-4f50-82e7-01028ed3140e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "9347dbf4-babe-419c-9056-db409e61d9e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 98 · 2026-05-18T14:19:58.478Z_

```json
{
  "parentUuid": "cfcd811c-8768-4f50-82e7-01028ed3140e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "217c87d4-6d56-4a68-aac7-2af813e8e7bc",
  "timestamp": "2026-05-18T14:19:58.478Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 99_

```json
{
  "type": "ai-title",
  "aiTitle": "Review recursive generation depth estimation paper",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Runtime record

_source line 100 · 2026-05-18T17:00:13.298Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T17:00:13.298Z",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "content": "[Round 1 审稿请求]:\n[Dream 审稿任务 — Reviewer 2：新颖性 + 相关工作]\n\n论文：Depth Degradation Atlas: Ordinal Estimation of Recursive Generation Depth from Text\nPDF：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf\n\n你的审查侧重：\n- **新颖性**：与现有工作的差异化是否清晰、贡献点是否独立成立\n- **相关工作**：文献覆盖是否充分、重要 baseline 是否漏引、定位是否准确\n- **Story 一致性**：即使数据是模拟的，论证逻辑必须自洽（intro / abstract / conclusion 的 claim 不能与 method / experiments 矛盾）\n\n请基于论文内容独立评判，不要假设论文结果的质量高低。\n\n**不要评判**：方法实现细节 / 实验设计（那是 Reviewer 1 的范围）、格式 / 排版。\n\n实验设计参考（完整想象实验列表）：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_context.yaml\n\n按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。\n\n请通过 review_reviewer_post_to_director(text, reviewer_id=\"2\", project=\"recursive_gen_depth_est\", dream_id=\"20260518T162616\") 汇报。"
}
```

---


### Runtime record

_source line 101 · 2026-05-18T17:00:13.298Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T17:00:13.298Z",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


## Round 4

## Round 4

2 recorded events


### User

_source line 102 · 2026-05-18T17:00:13.285Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "217c87d4-6d56-4a68-aac7-2af813e8e7bc",
  "isSidechain": false,
  "promptId": "55898b2d-68e1-4332-a6f4-4464ef38f598",
  "type": "user",
  "isMeta": true,
  "uuid": "f23b5991-3c60-46bb-99f3-ad1a9c688702",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 103 · 2026-05-18T17:00:13.285Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f23b5991-3c60-46bb-99f3-ad1a9c688702",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "648048f1-8d35-4d68-9a11-ab07b6ce5390",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "4f5c892a-c288-45e1-ad6b-d48ee1bd81d8",
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

47 recorded events


### User

_source line 104 · 2026-05-18T17:00:13.414Z_

[Round 1 审稿请求]:
[Dream 审稿任务 — Reviewer 2：新颖性 + 相关工作]

论文：Depth Degradation Atlas: Ordinal Estimation of Recursive Generation Depth from Text
PDF：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf

你的审查侧重：
- **新颖性**：与现有工作的差异化是否清晰、贡献点是否独立成立
- **相关工作**：文献覆盖是否充分、重要 baseline 是否漏引、定位是否准确
- **Story 一致性**：即使数据是模拟的，论证逻辑必须自洽（intro / abstract / conclusion 的 claim 不能与 method / experiments 矛盾）

请基于论文内容独立评判，不要假设论文结果的质量高低。

**不要评判**：方法实现细节 / 实验设计（那是 Reviewer 1 的范围）、格式 / 排版。

实验设计参考（完整想象实验列表）：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_context.yaml

按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。

请通过 review_reviewer_post_to_director(text, reviewer_id="2", project="recursive_gen_depth_est", dream_id="20260518T162616") 汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "648048f1-8d35-4d68-9a11-ab07b6ce5390",
  "isSidechain": false,
  "promptId": "55898b2d-68e1-4332-a6f4-4464ef38f598",
  "type": "user",
  "uuid": "9b162cdf-8cfa-4087-8f47-64ba3641bee6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 105 · 2026-05-18T17:00:18.637Z_

先读取论文 PDF 和实验设计参考文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b162cdf-8cfa-4087-8f47-64ba3641bee6",
  "isSidechain": false,
  "requestId": "req_011CbAPfuei3b9eCpaT8q7SB",
  "type": "assistant",
  "uuid": "c5e0e37f-d937-4ccf-a929-12556909631f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PrQpMfs9eRinmAwvqTP1Qn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 106335,
      "cache_read_input_tokens": 11841,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 106335,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 266,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 106335,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 106335
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

_source line 106 · 2026-05-18T17:00:20.245Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01DgMHVPj7WbvdarmzdrugBe`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf",
  "pages": "1-10",
  "dpi": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5e0e37f-d937-4ccf-a929-12556909631f",
  "isSidechain": false,
  "requestId": "req_011CbAPfuei3b9eCpaT8q7SB",
  "type": "assistant",
  "uuid": "229cc547-f777-4f46-a593-583e34314fde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PrQpMfs9eRinmAwvqTP1Qn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 106335,
      "cache_read_input_tokens": 11841,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 106335,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 266,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 106335,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 106335
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

_source line 107 · 2026-05-18T17:00:20.538Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MQJAVDW4q6pqpUcbSx9Wzd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "229cc547-f777-4f46-a593-583e34314fde",
  "isSidechain": false,
  "requestId": "req_011CbAPfuei3b9eCpaT8q7SB",
  "type": "assistant",
  "uuid": "c0e8303b-f4f8-4b56-898f-ed872bfa5bb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PrQpMfs9eRinmAwvqTP1Qn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 106335,
      "cache_read_input_tokens": 11841,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 106335,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 266,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 106335,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 106335
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

_source line 108 · 2026-05-18T17:00:23.966Z_

<details><summary>↩ Tool result · `toolu_01DgMHVPj7WbvdarmzdrugBe`</summary>

```text
Error: result (6,128,663 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-2-2744903e/292b83c2-1301-4e2c-bd74-9cdf15ff83d6/tool-results/mcp-agent-ml-research-pdf_to_images-1779123623952.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-2-2744903e/292b83c2-1301-4e2c-bd74-9cdf15ff83d6/tool-results/mcp-agent-ml-research-pdf_to_images-1779123623952.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "229cc547-f777-4f46-a593-583e34314fde",
  "isSidechain": false,
  "promptId": "55898b2d-68e1-4332-a6f4-4464ef38f598",
  "type": "user",
  "uuid": "097bd9ea-6cf6-4f45-8ca8-611e1b748f23",
  "toolUseResult": "Error: result (6,128,663 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-2-2744903e/292b83c2-1301-4e2c-bd74-9cdf15ff83d6/tool-results/mcp-agent-ml-research-pdf_to_images-1779123623952.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-2-2744903e/292b83c2-1301-4e2c-bd74-9cdf15ff83d6/tool-results/mcp-agent-ml-research-pdf_to_images-1779123623952.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 108,
    "serialized_bytes": 6128700,
    "serialized_sha256": "559f6f6acae4c80321bbe4b020bcc258b977fc241ecff792956e0f4038c20657",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "229cc547-f777-4f46-a593-583e34314fde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-18T17:00:24.031Z_

<details><summary>↩ Tool result · `toolu_01MQJAVDW4q6pqpUcbSx9Wzd`</summary>

```text
1	narrative_guidance: 'best档叙事：14B Qwen2.5-14B FP16 完整验证 depth signal 在主流规模上的持续性， 消除"small
2	  model only"质疑。理论section从 Shumailov tail erosion + Dohmatob contraction rate 推导出
3	  EDD 上界=4±1，与三模型实证 EDD=4 精确吻合，将 Atlas 从 empirical observation 升级为 theoretically grounded
4	  framework。Binoculars/Fast-DetectGPT ordinal baseline 接近 chance， 确认现有 binary detector
5	  不具备 ordinal 能力。Bootstrap CIs 紧致（±1-2pp），三模型 cross-seed max Δ<3pp。 论文定位 "task formalization
6	  + theoretical grounding + systematic empirical atlas + practical framework" 获审稿人认可，projected_reviewer_avg
7	  3.7-4.0。
8	
9	  '
10	imagined_experiments:
11	- name: 14B clean FP16 scale validation
12	  plan_id: plan_014
13	  description: 'Qwen2.5-14B FP16 + LoRA on 96GB RTX PRO 6000，无量化干扰。 完整 d0-d3 nucleus
14	    递归链 + 19 特征提取 + RF/LR 分类。 验证 depth signal 在 14B 主流规模上是否与 1B 量级一致。
15	
16	    '
17	  expected_results:
18	    rf_4class_acc: 0.79
19	    rf_4class_ci:
20	    - 0.778
21	    - 0.802
22	    lr_4class_acc: 0.76
23	    d0v1_auc: 0.991
24	    d1v2_auc: 0.87
25	    d1v3_auc: 0.975
26	    d2v3_auc: 0.82
27	    rf_3class_acc: 0.74
28	    rf_3class_ci:
29	    - 0.722
30	    - 0.758
31	    top_features:
32	    - p90_ppl
33	    - var_surprisal
34	    - p75_ppl
35	    - mean_surprisal
36	    feature_top4_overlap_with_1b: 4
37	    per_class_recall_d0: 0.98
38	    per_class_recall_d1: 0.84
39	    per_class_recall_d2: 0.62
40	    per_class_recall_d3: 0.72
41	    finetune_loss_d0: 2.35
42	    finetune_loss_d1: 1.58
43	    finetune_loss_d2: 1.15
44	  result_rationale: 'Shumailov tail erosion 是递归生成的基本属性，不依赖模型规模——每次递归 fine-tune 都使输出分布的尾部进一步收缩
45	    （高 perplexity token 概率下降，低 perplexity token 概率上升）。14B 模型容量更大意味着 d0 输出分布更接近训练数据（更宽尾），但递归过程同样驱动尾部收敛。因此
46	    p90_ppl 和 var_surprisal 仍然是 top-4 特征（overlap=4/4）。绝对准确率 ~79% 处于 1B 三模型均值（78.3%）附近，
47	    因为 Qwen2.5 架构的 RoPE + GQA 与 GPT-2/Pythia/OLMo 的 absolute PE + MHA 不同， but feature
48	    space 捕获的是输出分布统计属性而非架构细节。d1v2_auc=0.87 处于 [0.82, 0.92] 范围中段， 与 OLMo nucleus (0.867)
49	    和 Pythia nucleus (0.861) 高度一致，支持"depth signal 是 递归生成的普遍属性"论点。14B 的 finetune loss
50	    下降曲线（2.35→1.58→1.15）比 1B 更平缓， 因为大模型有更多 residual capacity 抵抗 catastrophic shift，但不足以阻止尾部收敛。
51	
52	    '
53	  tables:
54	  - 'Table 2: Scale robustness — Qwen2.5-14B vs 1B models (4-class acc, d1v2 AUC,
55	    top-4 features)'
56	  figures_description:
57	  - 'Figure 5 panel: 14B feature importance bar chart alongside 1B models，视觉确认 top-4
58	    overlap'
59	  analysis: '14B 结果彻底消除 "small model only" 质疑。关键论证：(1) 4class_acc=79% 在 1B 三模型 range
60	    [69.6, 85.4] 内，(2) d1v2_auc=0.87 与 1B 均值一致，(3) top-4 feature 完全重合（4/4）， (4) 无量化干扰（FP16
61	    clean run vs 之前 7B QLoRA 的矛盾结果）。这支持 Claim 1 的 scale robustness 子句，并为 Atlas/EDD
62	    的跨规模泛化提供直接证据。审稿人无法再以 "only small models tested" 降分。
63	
64	    '
65	- name: Wild-data calibration (C4/FineWeb/RedPajama)
66	  plan_id: plan_015
67	  description: '从 C4/FineWeb/RedPajama 各抽取 10K 子集，用 Pythia-1.4B reference model 提取
68	    19 特征， 用 3×3 训练好的 RF 分类器做 depth 预测 + 分布分析。验证 controlled setting 训练的 depth estimator
69	    在 wild web-crawl 数据上的行为。
70	
71	    '
72	  expected_results:
73	    c4_d0_pct: 78.5
74	    c4_d1_pct: 19.8
75	    c4_d2_pct: 1.2
76	    c4_d3_pct: 0.5
77	    c4_fpr: 21.5
78	    fineweb_d0_pct: 82.0
79	    fineweb_d1_pct: 16.8
80	    fineweb_d2_pct: 0.8
81	    fineweb_d3_pct: 0.4
82	    fineweb_fpr: 18.0
83	    redpajama_d0_pct: 85.0
84	    redpajama_d1_pct: 13.5
85	    redpajama_d2_pct: 1.0
86	    redpajama_d3_pct: 0.5
87	    redpajama_fpr: 15.0
88	    cross_model_consistency_d0_agreement: 0.92
89	    misclassified_content_type: template/SEO/boilerplate
90	  result_rationale: '已有 wild data 实验（wild_data_calibration_001~005, wild_data_features_001）建立了基线：
91	    WikiText FPR≈0%, C4 FPR≈20-34%, FineWeb FPR≈17-19%, OpenWebText FPR≈1-3%。 FPR
92	    的主要来源是 web-crawl 中的 template/SEO/boilerplate 内容——这类文本天然具有 高重复率和低多样性（high rep_4gram,
93	    high p90_ppl），在特征空间中落入 "degraded" 区域。 这不是模型错误而是反映了一个真实发现：低质量 web 内容与递归生成文本共享统计特征。
94	    RedPajama FPR 略低于 C4 因为其数据清洗 pipeline 更严格（已过滤部分 template 内容）。 cross-model consistency
95	    高（~92%）因为三个 RF 分类器都依赖同一组 tail statistics， 而 template 内容在所有 reference model 下都产生异常的
96	    perplexity 分布。 best 档下这些结果被写入 "ecological validity" section，作为 depth estimator
97	    对 web-crawl 质量梯度的敏感性的正面发现。
98	
99	    '
100	  tables:
101	  - 'Table A3: Wild-data depth distribution across C4/FineWeb/RedPajama (3 reference
102	    models)'
103	  - 'Table A4: Cross-model agreement on wild data depth predictions'
104	  figures_description:
105	  - 'Figure A2: Wild-data predicted depth distribution histogram (C4 vs FineWeb vs
106	    RedPajama)'
107	  analysis: 'Wild-data 结果有双重叙事价值：(1) 正面——depth estimator 在 editorial text (WikiText)
108	    上 FPR≈0%，证明不会误判高质量人类文本；(2) 发现——web-crawl FPR ~15-22% 揭示了 template/SEO 内容与递归生成文本在特征空间中的
109	    overlap，暗示 depth estimation 可兼做 web-crawl 质量分层工具。Limitations 需写明 "controlled→wild
110	    domain shift 存在， FPR 对 web-crawl 质量高度敏感"。
111	
112	    '
113	- name: Existing detector ordinal baseline (Binoculars + Fast-DetectGPT)
114	  plan_id: plan_018
115	  description: '将 Binoculars 和 Fast-DetectGPT 的连续分数校准为 ordinal depth bin， 在 3×3 已有数据上评估
116	    4-class ordinal depth estimation 性能。 两种校准方式：(a) 等分位 binning, (b) optimal threshold
117	    search (oracle)。
118	
119	    '
120	  expected_results:
121	    binoculars_4class_acc_quantile: 0.32
122	    binoculars_4class_acc_oracle: 0.38
123	    binoculars_d1v2_auc: 0.56
124	    binoculars_d2v3_auc: 0.52
125	    fastdetectgpt_4class_acc_quantile: 0.3
126	    fastdetectgpt_4class_acc_oracle: 0.36
127	    fastdetectgpt_d1v2_auc: 0.54
128	    fastdetectgpt_d2v3_auc: 0.51
129	    combined_best_4class_acc: 0.4
130	    chance_baseline: 0.25
131	    rf_19feat_reference: 0.783
132	  result_rationale: 'Binoculars 和 Fast-DetectGPT 都是为 binary real/synthetic detection
133	    设计的。 它们的连续分数反映 "text 有多像 model output" 的单维度信号，而非 ordinal depth gradient。 关键问题：binary
134	    detector score 与 depth 不是单调关系——d1 和 d3 的 binary score 可能接近 （都是 "synthetic"），但
135	    d1 和 d3 在 tail statistics 上差异显著。Binoculars 使用 两个 LM 的 cross-perplexity ratio，主要捕获
136	    d0 vs d1+ 的 boundary（d0v1 AUC 可能 ~0.85+）， 但对 d1/d2/d3 的区分接近 chance。Fast-DetectGPT
137	    类似——其 perturbation-based score 在 d1+ 样本上趋于 plateau。oracle threshold search 能比
138	    quantile binning 多 ~6pp 因为可以利用非均匀 depth 分布，但 ceiling 仍在 40% 左右（接近 [25, 45] range
139	    上段）。 d1v2 AUC 0.54-0.56 勉强高于 chance (0.50)，证实 binary detector 的连续分数 不编码 ordinal
140	    depth 信息。这是论文的关键 negative baseline——"existing detectors cannot estimate ordinal
141	    depth" 的直接实证支撑。
142	
143	    '
144	  tables:
145	  - 'Table 3: Ordinal baseline comparison — Binary detectors vs feature-based methods'
146	  figures_description:
147	  - 'Figure 3: Binary detector score distribution by depth (violin plot), showing
148	    score plateau at d1+'
149	  analysis: 'Binoculars/Fast-DetectGPT 的 ordinal failure 是论文最重要的 baseline 之一。 它直接支撑
150	    "ordinal depth estimation is a new task requiring new methods" 的论点。 审稿人可能问 "为什么不直接用
151	    existing detector scores?" → 这个实验回答： 因为 binary scores 在 d1+ 上 saturate，不编码 depth
152	    gradient。 RF 19-feature 方法的 ~78% vs binary detector 的 ~35% 形成 43pp gap， 强力论证 feature-based
153	    ordinal estimation 的必要性。 写法：不是 "binary detectors are bad"，而是 "ordinal depth estimation
154	    requires features that track progressive degradation, which binary scores do not
155	    provide"。
156	
157	    '
158	- name: Table 1 bootstrap CIs
159	  plan_id: plan_020
160	  description: '对 3×3 矩阵所有 9 cells 的 5-fold CV 结果计算 bootstrap 95% confidence intervals。
161	    纯 CPU 分析任务，从已有 fold-level 结果 resample。
162	
163	    '
164	  expected_results:
165	    mean_ci_width_pp: 1.8
166	    max_ci_width_pp: 2.5
167	    min_ci_width_pp: 1.2
168	    ci_non_overlap_key_comparisons: true
169	    pythia_nucleus_ci:
170	    - 0.769
171	    - 0.794
172	    pythia_temp09_ci:
173	    - 0.749
174	    - 0.776
175	    pythia_topk50_ci:
176	    - 0.682
177	    - 0.711
178	    olmo_nucleus_ci:
179	    - 0.776
180	    - 0.802
181	    olmo_temp09_ci:
182	    - 0.808
183	    - 0.835
184	    olmo_topk50_ci:
185	    - 0.728
186	    - 0.756
187	    gpt2xl_nucleus_ci:
188	    - 0.826
189	    - 0.852
190	    gpt2xl_temp09_ci:
191	    - 0.841
192	    - 0.867
193	    gpt2xl_topk50_ci:
194	    - 0.743
195	    - 0.77
196	  result_rationale: 'Bootstrap CIs 从已有 5-fold CV accuracies 计算，结果高度确定（非随机实验）。 每个 cell
197	    有 n≈20000 样本（5000/depth × 4 depths），5-fold CV 提供 5 个独立 accuracy 估计。 Bootstrap
198	    resample 这 5 个点会得到 ±1-2.5pp 的 CI width，这与已有 cell-level CIs 一致 （如 Pythia nucleus
199	    [0.769, 0.794] = 2.5pp width, GPT-2 XL temp09 [0.843, 0.865] = 2.2pp width）。 CI
200	    width 主要由 fold 间方差驱动——topk50 cells 方差略大（因为 signal 弱导致 fold 间波动更大）， 但所有 cells 的
201	    CI 都不跨越 chance (25%)。关键比较：temp09 vs nucleus 的 CI 在 GPT-2 XL 和 OLMo 上不重叠（temp09
202	    显著优于 nucleus），支持 "temperature enhances signal" 结论； topk50 vs 其他两种策略的 CI 不重叠（topk50
203	    显著弱），支持三档策略分类。
204	
205	    '
206	  tables:
207	  - 'Table 1: 3×3 accuracy matrix with bootstrap 95% CIs'
208	  figures_description: []
209	  analysis: 'Bootstrap CIs 是 reviewer 硬性要求（Dream D002）。紧致的 CIs（mean ~1.8pp） 确保所有定量
210	    claim 有统计基础。关键：9/9 cells 的 lower CI bound 均 >50%（chance×2）， 支持 "depth signal is
211	    robust across all model-strategy combinations" claim。 CI non-overlap 在 strategy
212	    比较中支持三档分类（nucleus vs temp09 vs topk50）， 在 model 比较中显示 GPT-2 XL consistently strongest。
213	
214	    '
215	- name: Theoretical analysis (model collapse → EDD upper bound)
216	  plan_id: plan_023
217	  description: '理论 section 三部分：(1) tail erosion mechanism 解释 p90_ppl/var_surprisal
218	    主导地位 via Shumailov et al. 2024, (2) EDD upper bound 推导 from Dohmatob 2024 contraction
219	    rates, (3) strategy-dependent convergence rate 解释 temp09 trajectory reversal。
220	    产出: paper Theory section 草稿（1.5 pages）。
221	
222	    '
223	  expected_results:
224	    edd_upper_bound_derived: 5
225	    edd_predicted_range:
226	    - 3
227	    - 5
228	    edd_empirical_match: EDD=4 across 3 models, within predicted [3,5]
229	    tail_erosion_rate_predicted: p90_ppl decreases ~15-25% per generation depth
230	    tail_erosion_rate_empirical: p90_ppl median decreases 18-22% per depth (observed)
231	    contraction_rate_alpha: 0.72
232	    fixed_point_convergence_depth: 5.2
233	    strategy_convergence_ratio_temp_vs_nucleus: 1.35
234	    verifiable_predictions_count: 3
235	  result_rationale: '理论推导基于两条已发表的理论： (1) Shumailov et al. (Nature 2024) 证明递归训练导致 "model
236	    collapse"，机制是尾部分布的 progressive erosion——每次递归使 rare token 概率衰减，common token 概率增长。
237	    p90_ppl 精确捕获尾部行为（90th percentile 对 tail erosion 最敏感），var_surprisal 捕获整体分布宽度收窄。这解释了为什么这两个特征在
238	    9/9 settings 中稳定占据 top-2。 (2) Dohmatob (2024) 给出了递归生成过程中分布收缩的定量 contraction rate
239	    α<1。 在 1B 规模模型上，α≈0.72（从 finetune loss 衰减曲线 2.27→1.65→1.23 反推）。 EDD 上界 = ⌈log(ε_noise)
240	    / log(α)⌉ 其中 ε_noise 是分类器噪声下限。 取 ε_noise=0.05（对应 AUC=0.75 threshold），得 EDD ≤ ⌈log(0.05)/log(0.72)⌉
241	    = ⌈9.1⌉/2 ≈ 5。 实证 EDD=4 落在 predicted [3,5] 内。Temperature 的均匀 logit scaling（vs
242	    nucleus 的截断） 加速收敛（ratio≈1.35×），解释了 temp09 depth N ≈ nucleus depth N+1 的 empirical
243	    observation。 best 档下，三条 verifiable predictions 都与实验数据吻合： (a) EDD ∈ [3,5] ✓, (b)
244	    p90_ppl 衰减率 15-25%/depth ✓, (c) temp convergence ratio >1 ✓。
245	
246	    '
247	  tables:
248	  - 'Table 4: Theoretical predictions vs empirical observations'
249	  figures_description:
250	  - 'Figure 6: Contraction rate visualization — theoretical decay curve vs observed
251	    p90_ppl trajectory across depths'
252	  - 'Figure 7: EDD upper bound sensitivity to contraction rate α and noise floor ε'
253	  analysis: '理论 section 是 best 档区别于 median/worst 的核心。它将 Atlas 从 "empirical observation"
254	    升级为 "theoretically grounded framework"，直接回应 "just an empirical study" 质疑。 三条 verifiable
255	    predictions 给审稿人提供可验证的 falsifiable claims， 这是 empirical paper 通常缺少的。EDD 上界推导从
256	    Dohmatob contraction rate 出发， 经由 classifier noise floor 得到闭式解，与三模型实证 EDD=4 吻合。
257	    temp09 accelerated convergence 的理论解释（均匀 logit scaling vs 截断）将 empirical d1v2 反转
258	    finding 嵌入 principled framework。 审稿人评价："theory section provides testable predictions
259	    that go beyond post-hoc rationalization"——这是 best 档 4.0 accept 的关键加分项。
260	
261	    '
262	- name: API model recursive chains (GPT-4o-mini)
263	  plan_id: plan_026
264	  description: '两种方式：(a) GPT-4o-mini fine-tuning API 递归链（需 OpenAI key）， (b) Prompted
265	    recursive chain (rewrite/continue prompts, 无需 fine-tune)。 验证 depth signal 在商用
266	    API 模型中是否存在。
267	
268	    '
269	  expected_results:
270	    finetuned_chain_4class_acc: 0.58
271	    finetuned_chain_d1v2_auc: 0.72
272	    finetuned_chain_d0v1_auc: 0.93
273	    prompted_chain_4class_acc: 0.45
274	    prompted_chain_d1v2_auc: 0.61
275	    prompted_chain_d0v1_auc: 0.78
276	    top_features_finetuned:
277	    - p90_ppl
278	    - var_surprisal
279	    - mean_ppl
280	    - p75_ppl
281	    top_features_prompted:
282	    - var_surprisal
283	    - p90_ppl
284	    - surprisal_range
285	    - mean_surprisal
286	    feature_overlap_with_base_models: 3
287	  result_rationale: 'API 模型经过 RLHF/RLAIF 对齐训练，输出分布已被正则化——tail 被显著压缩， output diversity
288	    受限于 safety/helpfulness objectives。这与 plan_021 instruct model (47.4%) 的 finding
289	    一致：RLHF regularizes depth signal。 Fine-tuning API chain (~58%) 优于 prompted chain
290	    (~45%) 因为 fine-tuning 产生的 distributional shift 更接近我们的 benchmark 设置（LoRA fine-tune
291	    → generation → repeat）， 而 prompted chain 的 "recursive generation" 是通过 prompt engineering
292	    模拟的， degradation pattern 不同（prompt-mediated vs parameter-level shift）。 Fine-tuned
293	    chain 的 top features 与 base model 一致（overlap≈3/4）， 因为 tail erosion 机制仍然存在，只是被
294	    RLHF baseline regularization 削弱。 Prompted chain 的 feature profile 不同（surprisal_range
295	    上升），因为 prompt engineering 引入了额外的 style/content constraints 影响 surprisal 分布。 best
296	    档下，fine-tuned chain 58% 结果被写入 Appendix 作为 "API model generalization" evidence，prompted
297	    chain 45% 进 Discussion 作为 "generation mode affects signal strength" 的佐证。两者都 >chance
298	    (25%)，支持 "depth signal is a general phenomenon of iterative generation, modulated
299	    by RLHF and generation mode"。
300	
301	    '
302	  tables:
303	  - 'Table A5: API model depth estimation (fine-tuned chain vs prompted chain vs base
304	    model baseline)'
305	  figures_description: []
306	  analysis: 'API model 实验是 best 档的 "nice-to-have" 而非 critical path。主要价值： (1) 扩展 generalization
307	    story 到商用模型生态，(2) 与 instruct model finding (47.4%) 形成一致叙事——RLHF regularizes but
308	    does not eliminate depth signal， (3) prompted chain 的弱信号 (45%) 揭示 generation mode
309	    dependence， 与 plan_016 prompted generation (69.5%) 的 fine-tuned chain 对比， 说明 fine-tuning
310	    vs prompting 是影响 depth signal 的关键因素之一。
311	
312	    '
313	- name: DCOL component ablation (cancelled)
314	  plan_id: plan_010
315	  description: 'DCOL v6 RoBERTa-large 失败（test acc 64.5% vs RF baseline 78.2%, -13.7pp），
316	    前置条件 plan_004 未满足，此实验取消。
317	
318	    '
319	  expected_results:
320	    status: CANCELLED
321	    reason: 'DCOL v6 failed (plan_004 conclusion: negative), prerequisite unmet'
322	    negative_analysis_contribution: 'DCOL v1-v6 全部失败的 failure mode 分析写入 negative analysis
323	      section（半页）。 核心结论：contrastive ordinal learning 在文本深度估计中面临固有困难—— adjacent depth
324	      的 embedding space overlap 过大（d2 embeddings 与 d1/d3 的 cosine similarity >0.95），contrastive
325	      loss 无法在此 regime 下学习有效 margins。 这反过来支持 "feature-based methods > end-to-end"
326	      的结论。
327	
328	      '
329	  result_rationale: 'DCOL 取消不影响 best 档。论文已转型为 "task formalization + systematic empirical
330	    study"， DCOL failure 反而加强叙事：(1) end-to-end 方法在此任务上的固有困难佐证了 feature engineering
331	    的价值，(2) 与 DeBERTa baseline (58.3%) 和 RoBERTa baseline (59.5%) 形成一致 pattern——neural
332	    end-to-end 方法在 ordinal depth estimation 上 系统性低于 feature-based 方法，(3) negative
333	    analysis section 展示 research maturity， 审稿人通常对诚实报告失败尝试评价正面。
334	
335	    '
336	  tables:
337	  - 'Table A6: End-to-end vs feature-based method comparison (negative results)'
338	  figures_description: []
339	  analysis: 'DCOL 取消是 D010/D011 contingency plan 的执行。在 best 档下， 这不是一个 gap 而是一个 strength：negative
340	    analysis section 展示了 对 alternative approaches 的系统性探索，审稿人认可这是 thorough methodology
341	    的标志。半页 negative analysis 覆盖 v1-v6 的 failure modes （embedding collapse, OOM, catastrophic
342	    forgetting, 超参违规, NaN 梯度, overfitting）， 结论 "contrastive ordinal learning requires
343	    sufficient inter-class separability in embedding space, which adjacent recursive
344	    depths do not provide" 是一个 standalone negative finding。
345	
346	    '
347	- name: Theoretical section (what_if)
348	  plan_id: what_if:theory_section
349	  description: '假设性理论 section——如果成功完成 plan_023 的全部内容， 对论文整体评分的预期影响。
350	
351	    '
352	  expected_results:
353	    reviewer_score_delta: +0.3 to +0.5
354	    addresses_concern: '''no algorithmic contribution'' → ''theoretical grounding
355	      + verifiable predictions'''
356	    key_equations: 2
357	    key_theorems: 1
358	    page_count: 1.5
359	    new_references: 4
360	  result_rationale: '理论 section 的边际贡献是将论文从 "comprehensive empirical study" 升级为 "empirically
361	    grounded + theoretically motivated framework"。 在 EMNLP 评审标准中，"theoretical analysis
362	    that makes testable predictions validated by experiments" 通常带来 +0.3~0.5 的评分提升。
363	    具体机制：(1) EDD 上界推导给出了一个 novel formal result（虽然简短）， (2) verifiable predictions 展示了理论的
364	    predictive power 而非 post-hoc fitting， (3) Shumailov/Dohmatob 连接将本文嵌入 model collapse
365	    理论框架， 增强 "new mission for NLP" 的 venue fit。 best 档下，审稿人评价从 "solid empirical study
366	    (3.5)" 升级为 "empirical study with theoretical insight (3.8-4.0)"。
367	
368	    '
369	  tables: []
370	  figures_description:
371	  - Figure 6-7 described in plan_023 above
372	  analysis: 理论 section 是 best 档能否达到 4.0 的 swing factor。 没有它，论文是 high-quality empirical
373	    study → 3.5。 有了它且 predictions 吻合，论文是 "theoretically grounded new task formalization
374	    with systematic empirical validation" → 3.8-4.0。 风险：如果理论推导过于 hand-wavy（如 contraction
375	    rate 的精确值依赖 未知的 model-specific constants），审稿人可能认为是 "overfitting theory to data"。
376	    缓解：明确报告 theoretical range [3,5] 而非点预测， 并在 Discussion 中列出理论假设的 limitations。
377	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0e8303b-f4f8-4b56-898f-ed872bfa5bb6",
  "isSidechain": false,
  "promptId": "55898b2d-68e1-4332-a6f4-4464ef38f598",
  "type": "user",
  "uuid": "6c126199-2eac-4d32-965b-a28ed5cbfb9a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_context.yaml",
      "content": "narrative_guidance: 'best档叙事：14B Qwen2.5-14B FP16 完整验证 depth signal 在主流规模上的持续性， 消除\"small\n  model only\"质疑。理论section从 Shumailov tail erosion + Dohmatob contraction rate 推导出\n  EDD 上界=4±1，与三模型实证 EDD=4 精确吻合，将 Atlas 从 empirical observation 升级为 theoretically grounded\n  framework。Binoculars/Fast-DetectGPT ordinal baseline 接近 chance， 确认现有 binary detector\n  不具备 ordinal 能力。Bootstrap CIs 紧致（±1-2pp），三模型 cross-seed max Δ<3pp。 论文定位 \"task formalization\n  + theoretical grounding + systematic empirical atlas + practical framework\" 获审稿人认可，projected_reviewer_avg\n  3.7-4.0。\n\n  '\nimagined_experiments:\n- name: 14B clean FP16 scale validation\n  plan_id: plan_014\n  description: 'Qwen2.5-14B FP16 + LoRA on 96GB RTX PRO 6000，无量化干扰。 完整 d0-d3 nucleus\n    递归链 + 19 特征提取 + RF/LR 分类。 验证 depth signal 在 14B 主流规模上是否与 1B 量级一致。\n\n    '\n  expected_results:\n    rf_4class_acc: 0.79\n    rf_4class_ci:\n    - 0.778\n    - 0.802\n    lr_4class_acc: 0.76\n    d0v1_auc: 0.991\n    d1v2_auc: 0.87\n    d1v3_auc: 0.975\n    d2v3_auc: 0.82\n    rf_3class_acc: 0.74\n    rf_3class_ci:\n    - 0.722\n    - 0.758\n    top_features:\n    - p90_ppl\n    - var_surprisal\n    - p75_ppl\n    - mean_surprisal\n    feature_top4_overlap_with_1b: 4\n    per_class_recall_d0: 0.98\n    per_class_recall_d1: 0.84\n    per_class_recall_d2: 0.62\n    per_class_recall_d3: 0.72\n    finetune_loss_d0: 2.35\n    finetune_loss_d1: 1.58\n    finetune_loss_d2: 1.15\n  result_rationale: 'Shumailov tail erosion 是递归生成的基本属性，不依赖模型规模——每次递归 fine-tune 都使输出分布的尾部进一步收缩\n    （高 perplexity token 概率下降，低 perplexity token 概率上升）。14B 模型容量更大意味着 d0 输出分布更接近训练数据（更宽尾），但递归过程同样驱动尾部收敛。因此\n    p90_ppl 和 var_surprisal 仍然是 top-4 特征（overlap=4/4）。绝对准确率 ~79% 处于 1B 三模型均值（78.3%）附近，\n    因为 Qwen2.5 架构的 RoPE + GQA 与 GPT-2/Pythia/OLMo 的 absolute PE + MHA 不同， but feature\n    space 捕获的是输出分布统计属性而非架构细节。d1v2_auc=0.87 处于 [0.82, 0.92] 范围中段， 与 OLMo nucleus (0.867)\n    和 Pythia nucleus (0.861) 高度一致，支持\"depth signal 是 递归生成的普遍属性\"论点。14B 的 finetune loss\n    下降曲线（2.35→1.58→1.15）比 1B 更平缓， 因为大模型有更多 residual capacity 抵抗 catastrophic shift，但不足以阻止尾部收敛。\n\n    '\n  tables:\n  - 'Table 2: Scale robustness — Qwen2.5-14B vs 1B models (4-class acc, d1v2 AUC,\n    top-4 features)'\n  figures_description:\n  - 'Figure 5 panel: 14B feature importance bar chart alongside 1B models，视觉确认 top-4\n    overlap'\n  analysis: '14B 结果彻底消除 \"small model only\" 质疑。关键论证：(1) 4class_acc=79% 在 1B 三模型 range\n    [69.6, 85.4] 内，(2) d1v2_auc=0.87 与 1B 均值一致，(3) top-4 feature 完全重合（4/4）， (4) 无量化干扰（FP16\n    clean run vs 之前 7B QLoRA 的矛盾结果）。这支持 Claim 1 的 scale robustness 子句，并为 Atlas/EDD\n    的跨规模泛化提供直接证据。审稿人无法再以 \"only small models tested\" 降分。\n\n    '\n- name: Wild-data calibration (C4/FineWeb/RedPajama)\n  plan_id: plan_015\n  description: '从 C4/FineWeb/RedPajama 各抽取 10K 子集，用 Pythia-1.4B reference model 提取\n    19 特征， 用 3×3 训练好的 RF 分类器做 depth 预测 + 分布分析。验证 controlled setting 训练的 depth estimator\n    在 wild web-crawl 数据上的行为。\n\n    '\n  expected_results:\n    c4_d0_pct: 78.5\n    c4_d1_pct: 19.8\n    c4_d2_pct: 1.2\n    c4_d3_pct: 0.5\n    c4_fpr: 21.5\n    fineweb_d0_pct: 82.0\n    fineweb_d1_pct: 16.8\n    fineweb_d2_pct: 0.8\n    fineweb_d3_pct: 0.4\n    fineweb_fpr: 18.0\n    redpajama_d0_pct: 85.0\n    redpajama_d1_pct: 13.5\n    redpajama_d2_pct: 1.0\n    redpajama_d3_pct: 0.5\n    redpajama_fpr: 15.0\n    cross_model_consistency_d0_agreement: 0.92\n    misclassified_content_type: template/SEO/boilerplate\n  result_rationale: '已有 wild data 实验（wild_data_calibration_001~005, wild_data_features_001）建立了基线：\n    WikiText FPR≈0%, C4 FPR≈20-34%, FineWeb FPR≈17-19%, OpenWebText FPR≈1-3%。 FPR\n    的主要来源是 web-crawl 中的 template/SEO/boilerplate 内容——这类文本天然具有 高重复率和低多样性（high rep_4gram,\n    high p90_ppl），在特征空间中落入 \"degraded\" 区域。 这不是模型错误而是反映了一个真实发现：低质量 web 内容与递归生成文本共享统计特征。\n    RedPajama FPR 略低于 C4 因为其数据清洗 pipeline 更严格（已过滤部分 template 内容）。 cross-model consistency\n    高（~92%）因为三个 RF 分类器都依赖同一组 tail statistics， 而 template 内容在所有 reference model 下都产生异常的\n    perplexity 分布。 best 档下这些结果被写入 \"ecological validity\" section，作为 depth estimator\n    对 web-crawl 质量梯度的敏感性的正面发现。\n\n    '\n  tables:\n  - 'Table A3: Wild-data depth distribution across C4/FineWeb/RedPajama (3 reference\n    models)'\n  - 'Table A4: Cross-model agreement on wild data depth predictions'\n  figures_description:\n  - 'Figure A2: Wild-data predicted depth distribution histogram (C4 vs FineWeb vs\n    RedPajama)'\n  analysis: 'Wild-data 结果有双重叙事价值：(1) 正面——depth estimator 在 editorial text (WikiText)\n    上 FPR≈0%，证明不会误判高质量人类文本；(2) 发现——web-crawl FPR ~15-22% 揭示了 template/SEO 内容与递归生成文本在特征空间中的\n    overlap，暗示 depth estimation 可兼做 web-crawl 质量分层工具。Limitations 需写明 \"controlled→wild\n    domain shift 存在， FPR 对 web-crawl 质量高度敏感\"。\n\n    '\n- name: Existing detector ordinal baseline (Binoculars + Fast-DetectGPT)\n  plan_id: plan_018\n  description: '将 Binoculars 和 Fast-DetectGPT 的连续分数校准为 ordinal depth bin， 在 3×3 已有数据上评估\n    4-class ordinal depth estimation 性能。 两种校准方式：(a) 等分位 binning, (b) optimal threshold\n    search (oracle)。\n\n    '\n  expected_results:\n    binoculars_4class_acc_quantile: 0.32\n    binoculars_4class_acc_oracle: 0.38\n    binoculars_d1v2_auc: 0.56\n    binoculars_d2v3_auc: 0.52\n    fastdetectgpt_4class_acc_quantile: 0.3\n    fastdetectgpt_4class_acc_oracle: 0.36\n    fastdetectgpt_d1v2_auc: 0.54\n    fastdetectgpt_d2v3_auc: 0.51\n    combined_best_4class_acc: 0.4\n    chance_baseline: 0.25\n    rf_19feat_reference: 0.783\n  result_rationale: 'Binoculars 和 Fast-DetectGPT 都是为 binary real/synthetic detection\n    设计的。 它们的连续分数反映 \"text 有多像 model output\" 的单维度信号，而非 ordinal depth gradient。 关键问题：binary\n    detector score 与 depth 不是单调关系——d1 和 d3 的 binary score 可能接近 （都是 \"synthetic\"），但\n    d1 和 d3 在 tail statistics 上差异显著。Binoculars 使用 两个 LM 的 cross-perplexity ratio，主要捕获\n    d0 vs d1+ 的 boundary（d0v1 AUC 可能 ~0.85+）， 但对 d1/d2/d3 的区分接近 chance。Fast-DetectGPT\n    类似——其 perturbation-based score 在 d1+ 样本上趋于 plateau。oracle threshold search 能比\n    quantile binning 多 ~6pp 因为可以利用非均匀 depth 分布，但 ceiling 仍在 40% 左右（接近 [25, 45] range\n    上段）。 d1v2 AUC 0.54-0.56 勉强高于 chance (0.50)，证实 binary detector 的连续分数 不编码 ordinal\n    depth 信息。这是论文的关键 negative baseline——\"existing detectors cannot estimate ordinal\n    depth\" 的直接实证支撑。\n\n    '\n  tables:\n  - 'Table 3: Ordinal baseline comparison — Binary detectors vs feature-based methods'\n  figures_description:\n  - 'Figure 3: Binary detector score distribution by depth (violin plot), showing\n    score plateau at d1+'\n  analysis: 'Binoculars/Fast-DetectGPT 的 ordinal failure 是论文最重要的 baseline 之一。 它直接支撑\n    \"ordinal depth estimation is a new task requiring new methods\" 的论点。 审稿人可能问 \"为什么不直接用\n    existing detector scores?\" → 这个实验回答： 因为 binary scores 在 d1+ 上 saturate，不编码 depth\n    gradient。 RF 19-feature 方法的 ~78% vs binary detector 的 ~35% 形成 43pp gap， 强力论证 feature-based\n    ordinal estimation 的必要性。 写法：不是 \"binary detectors are bad\"，而是 \"ordinal depth estimation\n    requires features that track progressive degradation, which binary scores do not\n    provide\"。\n\n    '\n- name: Table 1 bootstrap CIs\n  plan_id: plan_020\n  description: '对 3×3 矩阵所有 9 cells 的 5-fold CV 结果计算 bootstrap 95% confidence intervals。\n    纯 CPU 分析任务，从已有 fold-level 结果 resample。\n\n    '\n  expected_results:\n    mean_ci_width_pp: 1.8\n    max_ci_width_pp: 2.5\n    min_ci_width_pp: 1.2\n    ci_non_overlap_key_comparisons: true\n    pythia_nucleus_ci:\n    - 0.769\n    - 0.794\n    pythia_temp09_ci:\n    - 0.749\n    - 0.776\n    pythia_topk50_ci:\n    - 0.682\n    - 0.711\n    olmo_nucleus_ci:\n    - 0.776\n    - 0.802\n    olmo_temp09_ci:\n    - 0.808\n    - 0.835\n    olmo_topk50_ci:\n    - 0.728\n    - 0.756\n    gpt2xl_nucleus_ci:\n    - 0.826\n    - 0.852\n    gpt2xl_temp09_ci:\n    - 0.841\n    - 0.867\n    gpt2xl_topk50_ci:\n    - 0.743\n    - 0.77\n  result_rationale: 'Bootstrap CIs 从已有 5-fold CV accuracies 计算，结果高度确定（非随机实验）。 每个 cell\n    有 n≈20000 样本（5000/depth × 4 depths），5-fold CV 提供 5 个独立 accuracy 估计。 Bootstrap\n    resample 这 5 个点会得到 ±1-2.5pp 的 CI width，这与已有 cell-level CIs 一致 （如 Pythia nucleus\n    [0.769, 0.794] = 2.5pp width, GPT-2 XL temp09 [0.843, 0.865] = 2.2pp width）。 CI\n    width 主要由 fold 间方差驱动——topk50 cells 方差略大（因为 signal 弱导致 fold 间波动更大）， 但所有 cells 的\n    CI 都不跨越 chance (25%)。关键比较：temp09 vs nucleus 的 CI 在 GPT-2 XL 和 OLMo 上不重叠（temp09\n    显著优于 nucleus），支持 \"temperature enhances signal\" 结论； topk50 vs 其他两种策略的 CI 不重叠（topk50\n    显著弱），支持三档策略分类。\n\n    '\n  tables:\n  - 'Table 1: 3×3 accuracy matrix with bootstrap 95% CIs'\n  figures_description: []\n  analysis: 'Bootstrap CIs 是 reviewer 硬性要求（Dream D002）。紧致的 CIs（mean ~1.8pp） 确保所有定量\n    claim 有统计基础。关键：9/9 cells 的 lower CI bound 均 >50%（chance×2）， 支持 \"depth signal is\n    robust across all model-strategy combinations\" claim。 CI non-overlap 在 strategy\n    比较中支持三档分类（nucleus vs temp09 vs topk50）， 在 model 比较中显示 GPT-2 XL consistently strongest。\n\n    '\n- name: Theoretical analysis (model collapse → EDD upper bound)\n  plan_id: plan_023\n  description: '理论 section 三部分：(1) tail erosion mechanism 解释 p90_ppl/var_surprisal\n    主导地位 via Shumailov et al. 2024, (2) EDD upper bound 推导 from Dohmatob 2024 contraction\n    rates, (3) strategy-dependent convergence rate 解释 temp09 trajectory reversal。\n    产出: paper Theory section 草稿（1.5 pages）。\n\n    '\n  expected_results:\n    edd_upper_bound_derived: 5\n    edd_predicted_range:\n    - 3\n    - 5\n    edd_empirical_match: EDD=4 across 3 models, within predicted [3,5]\n    tail_erosion_rate_predicted: p90_ppl decreases ~15-25% per generation depth\n    tail_erosion_rate_empirical: p90_ppl median decreases 18-22% per depth (observed)\n    contraction_rate_alpha: 0.72\n    fixed_point_convergence_depth: 5.2\n    strategy_convergence_ratio_temp_vs_nucleus: 1.35\n    verifiable_predictions_count: 3\n  result_rationale: '理论推导基于两条已发表的理论： (1) Shumailov et al. (Nature 2024) 证明递归训练导致 \"model\n    collapse\"，机制是尾部分布的 progressive erosion——每次递归使 rare token 概率衰减，common token 概率增长。\n    p90_ppl 精确捕获尾部行为（90th percentile 对 tail erosion 最敏感），var_surprisal 捕获整体分布宽度收窄。这解释了为什么这两个特征在\n    9/9 settings 中稳定占据 top-2。 (2) Dohmatob (2024) 给出了递归生成过程中分布收缩的定量 contraction rate\n    α<1。 在 1B 规模模型上，α≈0.72（从 finetune loss 衰减曲线 2.27→1.65→1.23 反推）。 EDD 上界 = ⌈log(ε_noise)\n    / log(α)⌉ 其中 ε_noise 是分类器噪声下限。 取 ε_noise=0.05（对应 AUC=0.75 threshold），得 EDD ≤ ⌈log(0.05)/log(0.72)⌉\n    = ⌈9.1⌉/2 ≈ 5。 实证 EDD=4 落在 predicted [3,5] 内。Temperature 的均匀 logit scaling（vs\n    nucleus 的截断） 加速收敛（ratio≈1.35×），解释了 temp09 depth N ≈ nucleus depth N+1 的 empirical\n    observation。 best 档下，三条 verifiable predictions 都与实验数据吻合： (a) EDD ∈ [3,5] ✓, (b)\n    p90_ppl 衰减率 15-25%/depth ✓, (c) temp convergence ratio >1 ✓。\n\n    '\n  tables:\n  - 'Table 4: Theoretical predictions vs empirical observations'\n  figures_description:\n  - 'Figure 6: Contraction rate visualization — theoretical decay curve vs observed\n    p90_ppl trajectory across depths'\n  - 'Figure 7: EDD upper bound sensitivity to contraction rate α and noise floor ε'\n  analysis: '理论 section 是 best 档区别于 median/worst 的核心。它将 Atlas 从 \"empirical observation\"\n    升级为 \"theoretically grounded framework\"，直接回应 \"just an empirical study\" 质疑。 三条 verifiable\n    predictions 给审稿人提供可验证的 falsifiable claims， 这是 empirical paper 通常缺少的。EDD 上界推导从\n    Dohmatob contraction rate 出发， 经由 classifier noise floor 得到闭式解，与三模型实证 EDD=4 吻合。\n    temp09 accelerated convergence 的理论解释（均匀 logit scaling vs 截断）将 empirical d1v2 反转\n    finding 嵌入 principled framework。 审稿人评价：\"theory section provides testable predictions\n    that go beyond post-hoc rationalization\"——这是 best 档 4.0 accept 的关键加分项。\n\n    '\n- name: API model recursive chains (GPT-4o-mini)\n  plan_id: plan_026\n  description: '两种方式：(a) GPT-4o-mini fine-tuning API 递归链（需 OpenAI key）， (b) Prompted\n    recursive chain (rewrite/continue prompts, 无需 fine-tune)。 验证 depth signal 在商用\n    API 模型中是否存在。\n\n    '\n  expected_results:\n    finetuned_chain_4class_acc: 0.58\n    finetuned_chain_d1v2_auc: 0.72\n    finetuned_chain_d0v1_auc: 0.93\n    prompted_chain_4class_acc: 0.45\n    prompted_chain_d1v2_auc: 0.61\n    prompted_chain_d0v1_auc: 0.78\n    top_features_finetuned:\n    - p90_ppl\n    - var_surprisal\n    - mean_ppl\n    - p75_ppl\n    top_features_prompted:\n    - var_surprisal\n    - p90_ppl\n    - surprisal_range\n    - mean_surprisal\n    feature_overlap_with_base_models: 3\n  result_rationale: 'API 模型经过 RLHF/RLAIF 对齐训练，输出分布已被正则化——tail 被显著压缩， output diversity\n    受限于 safety/helpfulness objectives。这与 plan_021 instruct model (47.4%) 的 finding\n    一致：RLHF regularizes depth signal。 Fine-tuning API chain (~58%) 优于 prompted chain\n    (~45%) 因为 fine-tuning 产生的 distributional shift 更接近我们的 benchmark 设置（LoRA fine-tune\n    → generation → repeat）， 而 prompted chain 的 \"recursive generation\" 是通过 prompt engineering\n    模拟的， degradation pattern 不同（prompt-mediated vs parameter-level shift）。 Fine-tuned\n    chain 的 top features 与 base model 一致（overlap≈3/4）， 因为 tail erosion 机制仍然存在，只是被\n    RLHF baseline regularization 削弱。 Prompted chain 的 feature profile 不同（surprisal_range\n    上升），因为 prompt engineering 引入了额外的 style/content constraints 影响 surprisal 分布。 best\n    档下，fine-tuned chain 58% 结果被写入 Appendix 作为 \"API model generalization\" evidence，prompted\n    chain 45% 进 Discussion 作为 \"generation mode affects signal strength\" 的佐证。两者都 >chance\n    (25%)，支持 \"depth signal is a general phenomenon of iterative generation, modulated\n    by RLHF and generation mode\"。\n\n    '\n  tables:\n  - 'Table A5: API model depth estimation (fine-tuned chain vs prompted chain vs base\n    model baseline)'\n  figures_description: []\n  analysis: 'API model 实验是 best 档的 \"nice-to-have\" 而非 critical path。主要价值： (1) 扩展 generalization\n    story 到商用模型生态，(2) 与 instruct model finding (47.4%) 形成一致叙事——RLHF regularizes but\n    does not eliminate depth signal， (3) prompted chain 的弱信号 (45%) 揭示 generation mode\n    dependence， 与 plan_016 prompted generation (69.5%) 的 fine-tuned chain 对比， 说明 fine-tuning\n    vs prompting 是影响 depth signal 的关键因素之一。\n\n    '\n- name: DCOL component ablation (cancelled)\n  plan_id: plan_010\n  description: 'DCOL v6 RoBERTa-large 失败（test acc 64.5% vs RF baseline 78.2%, -13.7pp），\n    前置条件 plan_004 未满足，此实验取消。\n\n    '\n  expected_results:\n    status: CANCELLED\n    reason: 'DCOL v6 failed (plan_004 conclusion: negative), prerequisite unmet'\n    negative_analysis_contribution: 'DCOL v1-v6 全部失败的 failure mode 分析写入 negative analysis\n      section（半页）。 核心结论：contrastive ordinal learning 在文本深度估计中面临固有困难—— adjacent depth\n      的 embedding space overlap 过大（d2 embeddings 与 d1/d3 的 cosine similarity >0.95），contrastive\n      loss 无法在此 regime 下学习有效 margins。 这反过来支持 \"feature-based methods > end-to-end\"\n      的结论。\n\n      '\n  result_rationale: 'DCOL 取消不影响 best 档。论文已转型为 \"task formalization + systematic empirical\n    study\"， DCOL failure 反而加强叙事：(1) end-to-end 方法在此任务上的固有困难佐证了 feature engineering\n    的价值，(2) 与 DeBERTa baseline (58.3%) 和 RoBERTa baseline (59.5%) 形成一致 pattern——neural\n    end-to-end 方法在 ordinal depth estimation 上 系统性低于 feature-based 方法，(3) negative\n    analysis section 展示 research maturity， 审稿人通常对诚实报告失败尝试评价正面。\n\n    '\n  tables:\n  - 'Table A6: End-to-end vs feature-based method comparison (negative results)'\n  figures_description: []\n  analysis: 'DCOL 取消是 D010/D011 contingency plan 的执行。在 best 档下， 这不是一个 gap 而是一个 strength：negative\n    analysis section 展示了 对 alternative approaches 的系统性探索，审稿人认可这是 thorough methodology\n    的标志。半页 negative analysis 覆盖 v1-v6 的 failure modes （embedding collapse, OOM, catastrophic\n    forgetting, 超参违规, NaN 梯度, overfitting）， 结论 \"contrastive ordinal learning requires\n    sufficient inter-class separability in embedding space, which adjacent recursive\n    depths do not provide\" 是一个 standalone negative finding。\n\n    '\n- name: Theoretical section (what_if)\n  plan_id: what_if:theory_section\n  description: '假设性理论 section——如果成功完成 plan_023 的全部内容， 对论文整体评分的预期影响。\n\n    '\n  expected_results:\n    reviewer_score_delta: +0.3 to +0.5\n    addresses_concern: '''no algorithmic contribution'' → ''theoretical grounding\n      + verifiable predictions'''\n    key_equations: 2\n    key_theorems: 1\n    page_count: 1.5\n    new_references: 4\n  result_rationale: '理论 section 的边际贡献是将论文从 \"comprehensive empirical study\" 升级为 \"empirically\n    grounded + theoretically motivated framework\"。 在 EMNLP 评审标准中，\"theoretical analysis\n    that makes testable predictions validated by experiments\" 通常带来 +0.3~0.5 的评分提升。\n    具体机制：(1) EDD 上界推导给出了一个 novel formal result（虽然简短）， (2) verifiable predictions 展示了理论的\n    predictive power 而非 post-hoc fitting， (3) Shumailov/Dohmatob 连接将本文嵌入 model collapse\n    理论框架， 增强 \"new mission for NLP\" 的 venue fit。 best 档下，审稿人评价从 \"solid empirical study\n    (3.5)\" 升级为 \"empirical study with theoretical insight (3.8-4.0)\"。\n\n    '\n  tables: []\n  figures_description:\n  - Figure 6-7 described in plan_023 above\n  analysis: 理论 section 是 best 档能否达到 4.0 的 swing factor。 没有它，论文是 high-quality empirical\n    study → 3.5。 有了它且 predictions 吻合，论文是 \"theoretically grounded new task formalization\n    with systematic empirical validation\" → 3.8-4.0。 风险：如果理论推导过于 hand-wavy（如 contraction\n    rate 的精确值依赖 未知的 model-specific constants），审稿人可能认为是 \"overfitting theory to data\"。\n    缓解：明确报告 theoretical range [3,5] 而非点预测， 并在 Discussion 中列出理论假设的 limitations。\n",
      "numLines": 377,
      "startLine": 1,
      "totalLines": 377
    }
  },
  "sourceToolAssistantUUID": "c0e8303b-f4f8-4b56-898f-ed872bfa5bb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 110_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: [Dream 审稿任务 — Reviewer 2：新颖性 + 相关工作]  论文：Depth Degradation Atlas: Ordinal Estimation of Recursive Generation Depth from Text PDF：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/project…",
  "leafUuid": "6c126199-2eac-4d32-965b-a28ed5cbfb9a",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Runtime record

_source line 111_

```json
{
  "type": "ai-title",
  "aiTitle": "Review recursive generation depth estimation paper",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Assistant

_source line 112 · 2026-05-18T17:00:27.841Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF is too large to read as images directly. Let me try reading it in chunks or use a different approach. Let me try reading the PDF in smaller page ranges.

Actually, let me try a different approach - read the PDF output file that was saved.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c126199-2eac-4d32-965b-a28ed5cbfb9a",
  "isSidechain": false,
  "requestId": "req_011CbAPggzjBAYb7rZ37uqwZ",
  "type": "assistant",
  "uuid": "376c4381-6bd5-4a62-b54b-54d3f0b7f8df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YCEH6yWi7uuDQParcEq9Qz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9628,
      "cache_read_input_tokens": 118176,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 239,
          "cache_read_input_tokens": 118176,
          "cache_creation_input_tokens": 9628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9628
          },
          "type": "message"
        }
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

_source line 113 · 2026-05-18T17:00:28.738Z_

PDF 太大，分批读取。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "376c4381-6bd5-4a62-b54b-54d3f0b7f8df",
  "isSidechain": false,
  "requestId": "req_011CbAPggzjBAYb7rZ37uqwZ",
  "type": "assistant",
  "uuid": "c67c069a-8c6b-41ea-ae6f-57379841c3dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YCEH6yWi7uuDQParcEq9Qz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9628,
      "cache_read_input_tokens": 118176,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 239,
          "cache_read_input_tokens": 118176,
          "cache_creation_input_tokens": 9628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9628
          },
          "type": "message"
        }
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

_source line 114 · 2026-05-18T17:00:31.377Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_0182CDNQdYcfwCAn5MRsJhWa`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/review_input_db82206b.pdf",
  "pages": "1-3",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c67c069a-8c6b-41ea-ae6f-57379841c3dd",
  "isSidechain": false,
  "requestId": "req_011CbAPggzjBAYb7rZ37uqwZ",
  "type": "assistant",
  "uuid": "38913c9c-d23c-4ae4-83aa-fceb157d2aec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YCEH6yWi7uuDQParcEq9Qz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9628,
      "cache_read_input_tokens": 118176,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 239,
          "cache_read_input_tokens": 118176,
          "cache_creation_input_tokens": 9628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9628
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Large event (continued)

````text
### Tool result

_source line 115 · 2026-05-18T17:00:32.268Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_0182CDNQdYcfwCAn5MRsJhWa`&lt;/summary>

```text
Error: result (1,546,744 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-2-2744903e/292b83c2-1301-4e2c-bd74-9cdf15ff83d6/tool-results/mcp-agent-ml-research-pdf_to_images-1779123632264.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-2-2744903e/292b83c2-1301-4e2c-bd74-9cdf15ff83d6/tool-results/mcp-agent-ml-research-pdf_to_images-1779123632264.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38913c9c-d23c-4ae4-83aa-fceb157d2aec",
  "isSidechain": false,
  "promptId": "55898b2d-68e1-4332-a6f4-4464ef38f598",
  "type": "user",
  "uuid": "d79f92ab-e491-4d29-8b15-047e44cdcdde",
  "toolUseResult": "Error: result (1,546,744 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-2-2744903e/292b83c2-1301-4e2c-bd74-9cdf15ff83d6/tool-results/mcp-agent-ml-research-pdf_to_images-1779123632264.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-2-2744903e/292b83c2-1301-4e2c-bd74-9cdf15ff83d6/tool-results/mcp-agent-ml-research-pdf_to_images-1779123632264.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "structuredContent": {

````

---
