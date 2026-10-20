# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2 **你的审查侧重：新颖性 + 完整性 + 写作质量** ### Venue 信息 - 目标: EMNLP 2026 Main Conference (

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 125
- **Recorded user turns:** 3
- **Tool calls:** 36
- **Original source:** `logs/chats/exported-trajectories/account-3/7db3877c-97f7-4f67-b6d3-097ea4227bb4.jsonl`
- **Structured JSON:** [`23d0601c58cbde8dfc43.json`](../../sessions/23/23d0601c58cbde8dfc43.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T07:08:01.731Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T07:08:01.731Z",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "content": "[Round 1 审稿请求]:\n## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量**\n\n### Venue 信息\n- 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- 截止日期: 2026-05-25\n- 页数限制: 长文 8 页正文（Limitations/Ethics/References/Appendix 不计入）\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名规则: double-blind\n\n### 论文路径\n- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- 各章节在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex\n- Appendix: `docs/paper/sections/appendix.tex`\n- References: `docs/paper/references.bib`\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **新颖性与贡献评估**\n   - \"correlation-selection gap\" 概念是否真正 novel？是否只是重新包装了已知现象（e.g., MBR 在某些任务上失败）？\n   - 与 Nédellec & Xia (2026) 的 consistency-accuracy correlation 工作相比，增量贡献有多大？\n   - \"instance degeneracy\" 是否只是 fine-tuned model 的 trivial 属性（更好的模型输出更一致）？\n   - 论文的核心 insight 是否足以支撑 EMNLP 主会议长文？还是更适合 Findings/Workshop？\n   - \"quality estimation succeeds but selection fails\" 的 framing 是否有足够的实际意义？\n\n2. **Related Work 完整性**\n   - 自检以下 citation 是否被引用或讨论：\n     - MBR decoding 在 NLP 中的成功/失败案例（MT vs 其他任务）\n     - Self-consistency 失败模式的分析（e.g., Byerly & Khashabi 2024 on correlated errors）\n     - LLM-based NER 的最新进展（UniNER, GoLLIE, CodeIE 等）\n     - Structured prediction uncertainty estimation（CRF-based, sequence labeling calibration）\n     - Diversity collapse in fine-tuned models\n   - 引用数量是否达到 EMNLP 主会议水平？（通常 40-60 篇）\n   - 是否有 hallucinated citations？请逐一检查关键引用的真实性\n\n3. **写作质量 — AI 写作痕迹检查（硬规则）**\n   - 全文搜索 em-dash (—) 和解释性 en-dash (–)：每处标记\n   - 搜索 \"-ing,\" 结尾的分词短语\n   - 搜索过度使用的过渡词（Furthermore/Moreover/Additionally 连续出现）\n   - 搜索 AI 用词黑名单：delve/leverage/utilize/facilitate/myriad/plethora/paradigm shift/novel（过度使用）\n   - 段落是否过度分段（每 2-3 句换段）？\n   - 专有名词首次出现是否有定义？\n   - Abstract 中的缩写是否在 Abstract 内定义？\n\n4. **格式合规**\n   - 页数是否在 8 页以内（正文）？\n   - 匿名化是否彻底？（检查 \\author, 文中有无 self-citation 泄露身份）\n   - 图表 caption 是否 self-contained？\n   - 表格格式：小数精度是否统一？最优加粗？\n   - 图中字体是否 ≥7pt？\n\n5. **叙事结构与 Framing**\n   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成连贯主线？\n   - Introduction 的 5 段结构是否完整？\n   - 论文是\"故事驱动\"还是\"实验报告\"风格？\n   - Contribution list 中的每一条是否在前文有铺垫且有后续实验支撑？\n\n请按以下格式输出审稿报告：\n```\n## Summary (2-3 句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n## Questions (需要作者澄清)\n## Missing References\n## Detailed Comments (逐节)\n## Overall Score (strong reject / weak reject / borderline / weak accept / strong accept)\n## Confidence (1-5)\n```"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T07:08:01.734Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T07:08:01.734Z",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

## Round 1

96 recorded events

### User

_source line 3 · 2026-05-17T07:08:01.766Z_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + 完整性 + 写作质量**

### Venue 信息
- 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle)
- 截止日期: 2026-05-25
- 页数限制: 长文 8 页正文（Limitations/Ethics/References/Appendix 不计入）
- 模板: ACL style (`\usepackage[review]{acl}`)
- 匿名规则: double-blind

### 论文路径
- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`
- 各章节在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex
- Appendix: `docs/paper/sections/appendix.tex`
- References: `docs/paper/references.bib`

### 你的审查重点

请从以下维度严格评审：

1. **新颖性与贡献评估**
   - "correlation-selection gap" 概念是否真正 novel？是否只是重新包装了已知现象（e.g., MBR 在某些任务上失败）？
   - 与 Nédellec & Xia (2026) 的 consistency-accuracy correlation 工作相比，增量贡献有多大？
   - "instance degeneracy" 是否只是 fine-tuned model 的 trivial 属性（更好的模型输出更一致）？
   - 论文的核心 insight 是否足以支撑 EMNLP 主会议长文？还是更适合 Findings/Workshop？
   - "quality estimation succeeds but selection fails" 的 framing 是否有足够的实际意义？

2. **Related Work 完整性**
   - 自检以下 citation 是否被引用或讨论：
     - MBR decoding 在 NLP 中的成功/失败案例（MT vs 其他任务）
     - Self-consistency 失败模式的分析（e.g., Byerly & Khashabi 2024 on correlated errors）
     - LLM-based NER 的最新进展（UniNER, GoLLIE, CodeIE 等）
     - Structured prediction uncertainty estimation（CRF-based, sequence labeling calibration）
     - Diversity collapse in fine-tuned models
   - 引用数量是否达到 EMNLP 主会议水平？（通常 40-60 篇）
   - 是否有 hallucinated citations？请逐一检查关键引用的真实性

3. **写作质量 — AI 写作痕迹检查（硬规则）**
   - 全文搜索 em-dash (—) 和解释性 en-dash (–)：每处标记
   - 搜索 "-ing," 结尾的分词短语
   - 搜索过度使用的过渡词（Furthermore/Moreover/Additionally 连续出现）
   - 搜索 AI 用词黑名单：delve/leverage/utilize/facilitate/myriad/plethora/paradigm shift/novel（过度使用）
   - 段落是否过度分段（每 2-3 句换段）？
   - 专有名词首次出现是否有定义？
   - Abstract 中的缩写是否在 Abstract 内定义？

4. **格式合规**
   - 页数是否在 8 页以内（正文）？
   - 匿名化是否彻底？（检查 \author, 文中有无 self-citation 泄露身份）
   - 图表 caption 是否 self-contained？
   - 表格格式：小数精度是否统一？最优加粗？
   - 图中字体是否 ≥7pt？

5. **叙事结构与 Framing**
   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成连贯主线？
   - Introduction 的 5 段结构是否完整？
   - 论文是"故事驱动"还是"实验报告"风格？
   - Contribution list 中的每一条是否在前文有铺垫且有后续实验支撑？

请按以下格式输出审稿报告：
```
## Summary (2-3 句)
## Strengths (逐条)
## Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])
## Questions (需要作者澄清)
## Missing References
## Detailed Comments (逐节)
## Overall Score (strong reject / weak reject / borderline / weak accept / strong accept)
## Confidence (1-5)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "8ef89de8-5a42-407b-a48b-445229ca4a17",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T07:08:01.765Z_

```json
{
  "parentUuid": "8ef89de8-5a42-407b-a48b-445229ca4a17",
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
  "uuid": "b09608b9-2b80-4eb3-8b5c-2b061c0fbc2e",
  "timestamp": "2026-05-17T07:08:01.765Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T07:08:01.765Z_

```json
{
  "parentUuid": "b09608b9-2b80-4eb3-8b5c-2b061c0fbc2e",
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
  "uuid": "a7a469dd-0952-4d40-9644-2677318b244f",
  "timestamp": "2026-05-17T07:08:01.765Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-17T07:08:01.765Z_

```json
{
  "parentUuid": "a7a469dd-0952-4d40-9644-2677318b244f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "729408ea-58e7-4dd6-8b4f-7f63afef2af3",
  "timestamp": "2026-05-17T07:08:01.765Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
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
  "aiTitle": "Review round 1 paper for EMNLP 2026",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Assistant

_source line 8 · 2026-05-17T07:08:06.119Z_

<details><summary>Logged reasoning block</summary>

```text
The user (Review Director) is asking me to perform a Round 1 review of a paper for EMNLP 2026. I'm Reviewer 2, focusing on novelty, completeness, and writing quality.

Let me start by:
1. Reading the paper materials (main.tex and all section files)
2. Searching for EMNLP 2026 / ACL ARR reviewer guidelines
3. Checking for AI writing markers

Let me begin by reading the paper files and searching for reviewer guidelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "729408ea-58e7-4dd6-8b4f-7f63afef2af3",
  "isSidechain": false,
  "requestId": "req_011Cb7ihoPRsZgPJfBfoVMY2",
  "type": "assistant",
  "uuid": "7adc2051-a607-4dfd-ab4a-925ba1165b10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YWTrVXRNDSynRnNLdnZwPX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15612,
      "cache_read_input_tokens": 11841,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15612,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 286,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15612,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15612
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-17T07:08:06.650Z_

开始执行 Round 1 审稿。先读取论文材料并搜索 ARR reviewer guidelines。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7adc2051-a607-4dfd-ab4a-925ba1165b10",
  "isSidechain": false,
  "requestId": "req_011Cb7ihoPRsZgPJfBfoVMY2",
  "type": "assistant",
  "uuid": "19c2d3bb-1bd1-44a0-83ec-865e863ff48f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YWTrVXRNDSynRnNLdnZwPX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15612,
      "cache_read_input_tokens": 11841,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15612,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 286,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15612,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15612
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-17T07:08:08.119Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WqDa1JyPZRGuMCtc9dcGmG`</summary>

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
  "parentUuid": "19c2d3bb-1bd1-44a0-83ec-865e863ff48f",
  "isSidechain": false,
  "requestId": "req_011Cb7ihoPRsZgPJfBfoVMY2",
  "type": "assistant",
  "uuid": "d9495000-8850-4096-ac46-440bd76da83b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YWTrVXRNDSynRnNLdnZwPX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15612,
      "cache_read_input_tokens": 11841,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15612,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 286,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15612,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15612
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-17T07:08:08.125Z_

<details><summary>↩ Tool result · `toolu_01WqDa1JyPZRGuMCtc9dcGmG`</summary>

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
  "parentUuid": "d9495000-8850-4096-ac46-440bd76da83b",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "c23acce9-1aaa-4752-aa0e-1d73635806e5",
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
  "sourceToolAssistantUUID": "d9495000-8850-4096-ac46-440bd76da83b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-17T07:08:12.415Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the paper files and search for ARR reviewer guidelines in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c23acce9-1aaa-4752-aa0e-1d73635806e5",
  "isSidechain": false,
  "requestId": "req_011Cb7iiH1qrZ7mq6YvSRVQM",
  "type": "assistant",
  "uuid": "78e4475a-93e5-4f49-a85e-4aa734c9b662",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2P6adVKhCL5MxbMydv3D8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1790,
      "cache_read_input_tokens": 27453,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 316,
          "cache_read_input_tokens": 27453,
          "cache_creation_input_tokens": 1790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1790
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-17T07:08:13.000Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GUPhdWXFpgAkeDR2avHV54`</summary>

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
  "parentUuid": "78e4475a-93e5-4f49-a85e-4aa734c9b662",
  "isSidechain": false,
  "requestId": "req_011Cb7iiH1qrZ7mq6YvSRVQM",
  "type": "assistant",
  "uuid": "014392a6-3595-4887-b426-213e461db059",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2P6adVKhCL5MxbMydv3D8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1790,
      "cache_read_input_tokens": 27453,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 316,
          "cache_read_input_tokens": 27453,
          "cache_creation_input_tokens": 1790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1790
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-17T07:08:14.714Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MdHhBvs79QkT8cp7Esgaj3`</summary>

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
  "parentUuid": "014392a6-3595-4887-b426-213e461db059",
  "isSidechain": false,
  "requestId": "req_011Cb7iiH1qrZ7mq6YvSRVQM",
  "type": "assistant",
  "uuid": "bd5a3831-9b4d-4e05-a1e4-156422648f2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2P6adVKhCL5MxbMydv3D8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1790,
      "cache_read_input_tokens": 27453,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 316,
          "cache_read_input_tokens": 27453,
          "cache_creation_input_tokens": 1790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1790
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-17T07:08:15.094Z_

<details><summary>↩ Tool result · `toolu_01MJcQRMzA3rkUsMiSJEoKka`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models, separating quality estimation from best-of-$N$ selection and diagnosing why the former succeeds while the latter fails---within the dominant deployment paradigm for production NER.
9	
10	A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
11	These signals achieve reliable quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction and error flagging.
12	Yet quality estimation does not translate to structural selection---the \textbf{correlation-selection gap} (the disparity between a signal's ability to rank instances reliably and its failure to select the best output within a single instance): structural best-of-$N$ selection matches or degrades greedy decoding ($T{=}0$) despite 12--14~pp oracle headroom.
13	The gap has two empirical causes: (a)~\textit{instance degeneracy}---fine-tuned models produce identical outputs for 10--58\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\rho{=}0.52$); and (b)~\textit{LP compression}---median within-instance range of 0.041 nats (\S\ref{sec:discussion}).
14	LP selection is degeneracy-gated: significant at 10\% degeneracy ($+1.36$~pp, $p{<}0.001$), sub-significant at 21\% ($+0.42$~pp), and absent at 58\%.
15	
16	\begin{figure*}[t]
17	\centering
18	\includegraphics[width=\textwidth]{fig_overview}
19	\caption{The correlation-selection gap. \textbf{Left}: consistency signals reliably predict instance-level quality ($\rho$ up to 0.45 on CoNLL, 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82). \textbf{Right}: quality estimation does not translate to selection---all methods approximately match greedy decoding ($T{=}0$) despite 13~pp oracle headroom (\S\ref{sec:discussion}).}
20	\label{fig:overview}
21	\end{figure*}
22	
23	We evaluate five signals from three families---structural, surface, and model-internal---on SciERC \cite{luan2018scierc} as a primary medium-difficulty test bed, with Few-NERD \cite{ding2021fewnerd} (low-degeneracy contrast), CoNLL-2003 \cite{tjongkimsang2003conll} (ceiling-effect control), and WNUT-17 \cite{derczynski2017wnut} (signal-collapse boundary), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).
24	We vary candidate pool size ($N{\in}\{2,\ldots,32\}$), signal sophistication, and model capacity within the 4B--8B range; behavior at 70B+ scales remains an open question.
25	An exploratory extension to relation extraction is reported in Appendix~\ref{app:re_extension}.
26	Our contributions:
27	\begin{enumerate}
28	    \item \textbf{Quality estimation framework.}
29	    We systematically evaluate five confidence signals from three families (structural, surface, model-internal) for LLM-based NER across four benchmarks spanning a difficulty gradient, two model families, and a 4B scale ablation.
30	    Structural signals reliably predict output quality (VC $\rho{=}0.38$ on the primary test bed; EM AUROC${=}0.82$ on CoNLL), with difficulty-dependent but model-stable rankings that support selective prediction and error flagging.
31	
32	    \item \textbf{Diagnosis of the correlation-selection gap.}
33	    We identify a three-layer failure:
34	    (a)~four instance-level signals cannot rank candidates within an instance \textit{by construction};
35	    (b)~MBR selection with well-aligned utility (within-instance $\rho{=}0.52$) fails because instance degeneracy (10--58\% of instances yield identical outputs) collapses the candidate pool;
36	    (c)~LP, the sole per-sample signal, carries genuine ranking information but suffers from extreme compression (median range 0.041 nats).
37	    A diagnostic chain (LoRA-rank ablation, free-form decoding, entity-token LP, supervised signal combination) confirms the bottleneck lies in the feature space, not signal aggregation.
38	
39	    \item \textbf{Degeneracy as a regime boundary.}
40	    LP selection effectiveness is inversely associated with degeneracy rate across three datasets (58\% $\to$ fail, 21\% $\to$ $+0.42$~pp, 10\% $\to$ $+1.36$~pp at $p{<}0.001$); entity-type-level analysis provides stronger statistical grounding ($\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$).
41	    In the low-degeneracy regime, LP selection scales with $N$ ($+0.52$~pp from $N{=}8$ to $N{=}16$, paired $p{=}0.003$).
42	\end{enumerate}
43	
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87be6691-d73b-413a-9734-5e6e73e261f9",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "ed90aa94-d801-409f-b1fa-a2dcb532cba7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \\citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \\cite{snell2025scaling, brown2024monkeys}.\nBut named entity recognition (NER) poses a structurally different challenge: the output is a \\textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.\n\nPrior work on confidence estimation for LLM-based IE has conflated \\textit{quality estimation} (which inputs does the model handle reliably?) with \\textit{sample selection} (which of $N$ outputs is best?).\nExisting self-consistency methods \\cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\n\\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models, separating quality estimation from best-of-$N$ selection and diagnosing why the former succeeds while the latter fails---within the dominant deployment paradigm for production NER.\n\nA methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.\nThese signals achieve reliable quality estimation ($\\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82; Figure~\\ref{fig:overview}), supporting selective prediction and error flagging.\nYet quality estimation does not translate to structural selection---the \\textbf{correlation-selection gap} (the disparity between a signal's ability to rank instances reliably and its failure to select the best output within a single instance): structural best-of-$N$ selection matches or degrades greedy decoding ($T{=}0$) despite 12--14~pp oracle headroom.\nThe gap has two empirical causes: (a)~\\textit{instance degeneracy}---fine-tuned models produce identical outputs for 10--58\\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\\rho{=}0.52$); and (b)~\\textit{LP compression}---median within-instance range of 0.041 nats (\\S\\ref{sec:discussion}).\nLP selection is degeneracy-gated: significant at 10\\% degeneracy ($+1.36$~pp, $p{<}0.001$), sub-significant at 21\\% ($+0.42$~pp), and absent at 58\\%.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. \\textbf{Left}: consistency signals reliably predict instance-level quality ($\\rho$ up to 0.45 on CoNLL, 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82). \\textbf{Right}: quality estimation does not translate to selection---all methods approximately match greedy decoding ($T{=}0$) despite 13~pp oracle headroom (\\S\\ref{sec:discussion}).}\n\\label{fig:overview}\n\\end{figure*}\n\nWe evaluate five signals from three families---structural, surface, and model-internal---on SciERC \\cite{luan2018scierc} as a primary medium-difficulty test bed, with Few-NERD \\cite{ding2021fewnerd} (low-degeneracy contrast), CoNLL-2003 \\cite{tjongkimsang2003conll} (ceiling-effect control), and WNUT-17 \\cite{derczynski2017wnut} (signal-collapse boundary), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).\nWe vary candidate pool size ($N{\\in}\\{2,\\ldots,32\\}$), signal sophistication, and model capacity within the 4B--8B range; behavior at 70B+ scales remains an open question.\nAn exploratory extension to relation extraction is reported in Appendix~\\ref{app:re_extension}.\nOur contributions:\n\\begin{enumerate}\n    \\item \\textbf{Quality estimation framework.}\n    We systematically evaluate five confidence signals from three families (structural, surface, model-internal) for LLM-based NER across four benchmarks spanning a difficulty gradient, two model families, and a 4B scale ablation.\n    Structural signals reliably predict output quality (VC $\\rho{=}0.38$ on the primary test bed; EM AUROC${=}0.82$ on CoNLL), with difficulty-dependent but model-stable rankings that support selective prediction and error flagging.\n\n    \\item \\textbf{Diagnosis of the correlation-selection gap.}\n    We identify a three-layer failure:\n    (a)~four instance-level signals cannot rank candidates within an instance \\textit{by construction};\n    (b)~MBR selection with well-aligned utility (within-instance $\\rho{=}0.52$) fails because instance degeneracy (10--58\\% of instances yield identical outputs) collapses the candidate pool;\n    (c)~LP, the sole per-sample signal, carries genuine ranking information but suffers from extreme compression (median range 0.041 nats).\n    A diagnostic chain (LoRA-rank ablation, free-form decoding, entity-token LP, supervised signal combination) confirms the bottleneck lies in the feature space, not signal aggregation.\n\n    \\item \\textbf{Degeneracy as a regime boundary.}\n    LP selection effectiveness is inversely associated with degeneracy rate across three datasets (58\\% $\\to$ fail, 21\\% $\\to$ $+0.42$~pp, 10\\% $\\to$ $+1.36$~pp at $p{<}0.001$); entity-type-level analysis provides stronger statistical grounding ($\\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$).\n    In the low-degeneracy regime, LP selection scales with $N$ ($+0.52$~pp from $N{=}8$ to $N{=}16$, paired $p{=}0.003$).\n\\end{enumerate}\n\n",
      "numLines": 44,
      "startLine": 1,
      "totalLines": 44
    }
  },
  "sourceToolAssistantUUID": "87be6691-d73b-413a-9734-5e6e73e261f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T07:08:14.729Z_

<details><summary>↩ Tool result · `toolu_01MdHhBvs79QkT8cp7Esgaj3`</summary>

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
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Fail to Scale Structured Information Extraction}
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
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd5a3831-9b4d-4e05-a1e4-156422648f2d",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "706c774c-59a2-4bdd-9717-8d3fbfd0b570",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\graphicspath{{figures/}}\n\n\\title{Strong Predictors, Weak Selectors:\\\\ Why Confidence Signals Fail to Scale Structured Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\section*{Ethics Statement}\nAll experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).\nCoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.\nNo new human data was collected or annotated for this study.\nOur findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.\nCode and data will be released upon acceptance at [anonymized URL].\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  },
  "sourceToolAssistantUUID": "bd5a3831-9b4d-4e05-a1e4-156422648f2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T07:08:14.801Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X1GYzysAA7asqpoZ7RabQY`</summary>

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
  "parentUuid": "706c774c-59a2-4bdd-9717-8d3fbfd0b570",
  "isSidechain": false,
  "requestId": "req_011Cb7iiH1qrZ7mq6YvSRVQM",
  "type": "assistant",
  "uuid": "b3555fd8-6a26-4754-8793-264eda36899a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2P6adVKhCL5MxbMydv3D8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1790,
      "cache_read_input_tokens": 27453,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 316,
          "cache_read_input_tokens": 27453,
          "cache_creation_input_tokens": 1790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1790
          },
          "type": "message"
        }
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

_source line 18 · 2026-05-17T07:08:14.806Z_

<details><summary>↩ Tool result · `toolu_01X1GYzysAA7asqpoZ7RabQY`</summary>

```text
1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability, LP)---for quality estimation and sample selection on four NER benchmarks spanning a difficulty gradient, using 4B--8B models.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82), supporting selective prediction.
5	However, quality estimation does not translate to sample selection---the \textit{correlation-selection gap}: despite ${\sim}$13~pp oracle headroom, no signal consistently outperforms greedy decoding.
6	The gap has a three-layer structure: four instance-level signals cannot rank candidates within an instance by construction; MBR selection with well-aligned utility ($\rho{=}0.52$) fails because instance degeneracy (10--58\% identical outputs) eliminates headroom; and LP carries genuine per-sample information but is compressed to near-ineffectiveness (median range 0.041 nats).
7	LP selection is inversely associated with degeneracy: at 10\% (Few-NERD), $+1.36$~pp ($p{<}0.001$); at 58\% (CoNLL), LP fails.
8	In the low-degeneracy regime, LP scales with sample budget ($+0.52$~pp from $N{=}8$ to 16, paired $p{=}0.003$).
9	Closing the gap for structural signals likely requires learned per-sample scoring.
10	\end{abstract}
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3555fd8-6a26-4754-8793-264eda36899a",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "b11250da-0913-446e-95e4-66ae443cabff",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nSelf-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \\textit{sets} of entities with partial overlap, where no majority vote analog exists.\nWe evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability, LP)---for quality estimation and sample selection on four NER benchmarks spanning a difficulty gradient, using 4B--8B models.\nAll signals achieve reliable quality estimation ($\\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82), supporting selective prediction.\nHowever, quality estimation does not translate to sample selection---the \\textit{correlation-selection gap}: despite ${\\sim}$13~pp oracle headroom, no signal consistently outperforms greedy decoding.\nThe gap has a three-layer structure: four instance-level signals cannot rank candidates within an instance by construction; MBR selection with well-aligned utility ($\\rho{=}0.52$) fails because instance degeneracy (10--58\\% identical outputs) eliminates headroom; and LP carries genuine per-sample information but is compressed to near-ineffectiveness (median range 0.041 nats).\nLP selection is inversely associated with degeneracy: at 10\\% (Few-NERD), $+1.36$~pp ($p{<}0.001$); at 58\\% (CoNLL), LP fails.\nIn the low-degeneracy regime, LP scales with sample budget ($+0.52$~pp from $N{=}8$ to 16, paired $p{=}0.003$).\nClosing the gap for structural signals likely requires learned per-sample scoring.\n\\end{abstract}\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  },
  "sourceToolAssistantUUID": "b3555fd8-6a26-4754-8793-264eda36899a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T07:08:15.087Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MJcQRMzA3rkUsMiSJEoKka`</summary>

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
  "parentUuid": "b11250da-0913-446e-95e4-66ae443cabff",
  "isSidechain": false,
  "requestId": "req_011Cb7iiH1qrZ7mq6YvSRVQM",
  "type": "assistant",
  "uuid": "87be6691-d73b-413a-9734-5e6e73e261f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2P6adVKhCL5MxbMydv3D8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1790,
      "cache_read_input_tokens": 27453,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 316,
          "cache_read_input_tokens": 27453,
          "cache_creation_input_tokens": 1790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1790
          },
          "type": "message"
        }
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性 + 写作质量**  ### Venue 信息 - 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - 截止日期: 2026-05-25 - 页数限制: 长文 8 页正文（Limitations/Ethics…",
  "leafUuid": "ed90aa94-d801-409f-b1fa-a2dcb532cba7",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper for EMNLP 2026",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Tool result

_source line 22 · 2026-05-17T07:08:22.968Z_

<details><summary>↩ Tool result · `toolu_01GUPhdWXFpgAkeDR2avHV54`</summary>

```text
Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here is information about the ACL ARR 2026 reviewer guidelines, review form, and criteria:

## Reviewer Guidelines

Reviewers are asked to follow this workflow: (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that particular submission. To preserve the merits of double-blind review, reviewers for *ACL conferences and TACL should be instructed not to actively try to discover the identity of the authors and not to let any suspicion or knowledge of author identity affect their judgment of the paper.

If you become aware or can guess the authors' identity, you should disclose that in the ARR review form, which contains questions about the reviewers' knowledge of author identity.

## Review Form Criteria

The review form includes several evaluation criteria:

**Overall Recommendation:** The scoring includes an option for "Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)."

**Strengths and Weaknesses:** Reviewers evaluate the major reasons to publish this paper at a selective *ACL venue, which could include novel and useful methodology, insightful empirical results or theoretical analysis, clear organization of related literature, or any other reason why interested readers of *ACL papers may find the paper useful. Reviewers also assess concerns about the paper that would cause prioritizing other high-quality papers, including concerns about correctness of the results or argumentation, limited perceived impact of the methods or findings, lack of clarity in exposition, or any other reason why interested readers of *ACL papers may gain less from this paper.

**Reproducibility:** Reviewers assess whether there is enough information in the paper for a reader to reproduce the main results, use results presented in this paper in future work (e.g., as a baseline), or build upon this work.

**Ethics:** Reviewers are asked to review the ACL code of ethics and the ARR checklist submitted by the authors in the submission form, and if there are ethical issues with the paper, to describe them and the extent to which they have been acknowledged or addressed by the authors.

**Excitement:** Reviewers rate how exciting the paper is, noting that excitement is subjective and does not necessarily follow what is popular in the field.

## Key Responsibilities

The reviewer's main tasks are (1) checking the appropriateness of the submission and its assignment to this reviewer, (2) writing a well-justified review, (3) updating the review as appropriate based on author-reviewer discussion.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "014392a6-3595-4887-b426-213e461db059",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "60583326-12ab-4843-8150-9561ed33a437",
  "toolUseResult": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KtknnUSMn2uCnYWxncvoMG",
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
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
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
      "Based on the search results, here is information about the ACL ARR 2026 reviewer guidelines, review form, and criteria:\n\n## Reviewer Guidelines\n\nReviewers are asked to follow this workflow: (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that particular submission. To preserve the merits of double-blind review, reviewers for *ACL conferences and TACL should be instructed not to actively try to discover the identity of the authors and not to let any suspicion or knowledge of author identity affect their judgment of the paper.\n\nIf you become aware or can guess the authors' identity, you should disclose that in the ARR review form, which contains questions about the reviewers' knowledge of author identity.\n\n## Review Form Criteria\n\nThe review form includes several evaluation criteria:\n\n**Overall Recommendation:** The scoring includes an option for \"Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers).\"\n\n**Strengths and Weaknesses:** Reviewers evaluate the major reasons to publish this paper at a selective *ACL venue, which could include novel and useful methodology, insightful empirical results or theoretical analysis, clear organization of related literature, or any other reason why interested readers of *ACL papers may find the paper useful. Reviewers also assess concerns about the paper that would cause prioritizing other high-quality papers, including concerns about correctness of the results or argumentation, limited perceived impact of the methods or findings, lack of clarity in exposition, or any other reason why interested readers of *ACL papers may gain less from this paper.\n\n**Reproducibility:** Reviewers assess whether there is enough information in the paper for a reader to reproduce the main results, use results presented in this paper in future work (e.g., as a baseline), or build upon this work.\n\n**Ethics:** Reviewers are asked to review the ACL code of ethics and the ARR checklist submitted by the authors in the submission form, and if there are ethical issues with the paper, to describe them and the extent to which they have been acknowledged or addressed by the authors.\n\n**Excitement:** Reviewers rate how exciting the paper is, noting that excitement is subjective and does not necessarily follow what is popular in the field.\n\n## Key Responsibilities\n\nThe reviewer's main tasks are (1) checking the appropriateness of the submission and its assignment to this reviewer, (2) writing a well-justified review, (3) updating the review as appropriate based on author-reviewer discussion."
    ],
    "durationSeconds": 9.963342954
  },
  "sourceToolAssistantUUID": "014392a6-3595-4887-b426-213e461db059",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T07:08:26.715Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Sa5bKWSCmkmyu9woMG367g`</summary>

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
  "parentUuid": "60583326-12ab-4843-8150-9561ed33a437",
  "isSidechain": false,
  "requestId": "req_011Cb7ijN1G7omSJC4hPXf1V",
  "type": "assistant",
  "uuid": "293847fe-20f7-4ce2-8fd0-538c859b0c56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4634eS47gVibKkuxBhDj1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2840,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 29243,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1411,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2840,
          "output_tokens": 315,
          "cache_read_input_tokens": 29243,
          "cache_creation_input_tokens": 1411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1411
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-17T07:08:26.726Z_

<details><summary>↩ Tool result · `toolu_01Sa5bKWSCmkmyu9woMG367g`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement signals that assume equivalence can be determined via exact match or semantic similarity.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} demonstrate that consistency correlates with accuracy for LLM-based NER/RE under hard-prompting.
11	We show this correlation is necessary but not sufficient for sample selection, and diagnose two specific failure mechanisms (degeneracy, compression) that explain why correlation does not translate to selection gains.
12	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, where instance degeneracy is most pronounced.
13	Degeneracy varies across datasets: CoNLL (91\% single-sample F1) exhibits 58\%; SciERC (66\%) shows 21\%; Few-NERD (75\%) shows 10\%; WNUT-17 (${\approx}$42\%, macro) shows near-zero (\S\ref{sec:discussion}).
14	Few-NERD's low degeneracy despite high performance reveals that dataset-specific factors modulate degeneracy beyond model capability alone.
15	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction; our supervised verifier baseline (logistic regression on all five signals, no oracle gap closure; \S\ref{sec:robustness_main}) suggests that the combination strategy itself is not the bottleneck.
16	\citet{culotta2004confidence} and \citet{mejer2010confidence} pioneer confidence estimation for structured prediction via CRF marginals and confidence-weighted models; \citet{fomicheva2020unsupervised} systematically apply model-internal signals (MC Dropout, D-Lex) for unsupervised quality estimation in NMT, establishing the paradigm we extend from sequence-level to set-valued structured outputs.
17	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided, park2024grammar}; recent work highlights hidden costs of constrained generation for log-probability estimation \cite{schall2025hidden} and inference efficiency \cite{yun2025price}.
18	
19	\paragraph{Uncertainty estimation and calibration.}
20	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs.
21	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; P(True) \cite{kadavath2022language} queries model confidence directly; \citet{malinin2021uncertainty} study predictive uncertainty for autoregressive structured prediction.
22	Our structural signals instead measure agreement over output \textit{structure}, requiring no model modification.
23	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling, deguchi2024centroid} with structural utility functions.
24	Unlike machine translation where MBR yields consistent gains \cite{freitag2022high}, we find that utility \textit{is} aligned with quality (within-instance SJ--F1 $\rho{=}0.52$) but instance degeneracy eliminates the headroom MBR would otherwise exploit.
25	\citet{eikema2025structured} find that standard MBR utilities degrade on structured outputs due to bag-of-unit mismatches.
26	Our diagnosis is complementary but distinct: even when utility \textit{is} well-aligned with quality (within-instance $\rho{=}0.52$), output degeneracy eliminates the headroom MBR needs to improve over greedy.
27	NER's discrete label space produces more extreme degeneracy (up to 58\%) than the partial-overlap regime typical in MT and summarization (\S\ref{sec:discussion}).
28	\citet{xie2024selfevaluation} show self-evaluation improves selective generation for discrete tasks; our results suggest this does not transfer to structured extraction without learned scoring.
29	Our quality estimation results connect to selective prediction \cite{kuleshov2015calibrated}: signals with $\rho$ up to 0.45 on CoNLL (0.38 on the primary test bed, 0.42 on Few-NERD) and AUROC up to 0.82 can support abstention policies that flag low-quality extractions, providing practical value independent of sample selection.
30	Conformal prediction constructs prediction sets with coverage guarantees \cite{zhang2025conformal}; while complementary, its set-valued output differs from best-of-$N$ selection.
31	
32	\paragraph{Best-of-$N$ with learned verifiers.}
33	\citet{gao2023scaling} establish scaling laws for best-of-$N$ selection with learned reward models, showing that BoN performance scales log-linearly with $N$ but eventually degrades due to reward overoptimization.
34	Our unsupervised signals face a more fundamental limitation: they cannot rank candidates at all (instance-level signals) or rank them too weakly (LP compression), making the overoptimization regime irrelevant.
35	Trained verifiers \cite{cobbe2021verifiers, lightman2024verify} and quality-aware decoding \cite{fernandes2022quality} learn per-sample scoring that may bridge this gap; our LoRA-rank ablation (degeneracy 7\% vs.\ 21\%, selection still fails) suggests that verifier training is necessary beyond merely increasing output diversity.
36	Fine-tuning itself contributes to the problem: \citet{kirk2024understanding} document diversity collapse in RLHF-trained models; our instance degeneracy is an analogous phenomenon in supervised fine-tuning, where stronger models converge to more uniform outputs.
37	Nucleus sampling \cite{holtzman2020curious} improves diversity in open-ended generation, but our constrained structured outputs limit the diversity that temperature scaling alone can recover.
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "293847fe-20f7-4ce2-8fd0-538c859b0c56",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "b09ee798-1fa3-47e6-b41b-2a9d8286ff16",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency \\cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \\cite{chen2024usc}, sub-claim decomposition \\cite{thirukovalluru2024atomic}, or hallucination detection \\cite{manakul2023selfcheckgpt}.\nTest-time scaling studies \\cite{snell2025scaling, brown2024monkeys} and reward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement signals that assume equivalence can be determined via exact match or semantic similarity.\nConcurrently, \\citet{feng2025optimal} and \\citet{wang2025make} adapt self-consistency to difficulty-aware settings; \\citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.\nOur work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.\n\n\\paragraph{Consistency for structured IE.}\n\\citet{yao2026consistency} demonstrate that consistency correlates with accuracy for LLM-based NER/RE under hard-prompting.\nWe show this correlation is necessary but not sufficient for sample selection, and diagnose two specific failure mechanisms (degeneracy, compression) that explain why correlation does not translate to selection gains.\nOur experiments use fine-tuned models, the dominant deployment paradigm for production NER, where instance degeneracy is most pronounced.\nDegeneracy varies across datasets: CoNLL (91\\% single-sample F1) exhibits 58\\%; SciERC (66\\%) shows 21\\%; Few-NERD (75\\%) shows 10\\%; WNUT-17 (${\\approx}$42\\%, macro) shows near-zero (\\S\\ref{sec:discussion}).\nFew-NERD's low degeneracy despite high performance reveals that dataset-specific factors modulate degeneracy beyond model capability alone.\nCoCoA \\cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction; our supervised verifier baseline (logistic regression on all five signals, no oracle gap closure; \\S\\ref{sec:robustness_main}) suggests that the combination strategy itself is not the bottleneck.\n\\citet{culotta2004confidence} and \\citet{mejer2010confidence} pioneer confidence estimation for structured prediction via CRF marginals and confidence-weighted models; \\citet{fomicheva2020unsupervised} systematically apply model-internal signals (MC Dropout, D-Lex) for unsupervised quality estimation in NMT, establishing the paradigm we extend from sequence-level to set-valued structured outputs.\nOur evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \\cite{willard2023guided, park2024grammar}; recent work highlights hidden costs of constrained generation for log-probability estimation \\cite{schall2025hidden} and inference efficiency \\cite{yun2025price}.\n\n\\paragraph{Uncertainty estimation and calibration.}\nSurveys cover confidence estimation \\cite{geng2024confidence}, uncertainty quantification \\cite{xia2025survey}, and calibration \\cite{hobelsberger2025systematic} for LLMs.\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; P(True) \\cite{kadavath2022language} queries model confidence directly; \\citet{malinin2021uncertainty} study predictive uncertainty for autoregressive structured prediction.\nOur structural signals instead measure agreement over output \\textit{structure}, requiring no model modification.\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling, deguchi2024centroid} with structural utility functions.\nUnlike machine translation where MBR yields consistent gains \\cite{freitag2022high}, we find that utility \\textit{is} aligned with quality (within-instance SJ--F1 $\\rho{=}0.52$) but instance degeneracy eliminates the headroom MBR would otherwise exploit.\n\\citet{eikema2025structured} find that standard MBR utilities degrade on structured outputs due to bag-of-unit mismatches.\nOur diagnosis is complementary but distinct: even when utility \\textit{is} well-aligned with quality (within-instance $\\rho{=}0.52$), output degeneracy eliminates the headroom MBR needs to improve over greedy.\nNER's discrete label space produces more extreme degeneracy (up to 58\\%) than the partial-overlap regime typical in MT and summarization (\\S\\ref{sec:discussion}).\n\\citet{xie2024selfevaluation} show self-evaluation improves selective generation for discrete tasks; our results suggest this does not transfer to structured extraction without learned scoring.\nOur quality estimation results connect to selective prediction \\cite{kuleshov2015calibrated}: signals with $\\rho$ up to 0.45 on CoNLL (0.38 on the primary test bed, 0.42 on Few-NERD) and AUROC up to 0.82 can support abstention policies that flag low-quality extractions, providing practical value independent of sample selection.\nConformal prediction constructs prediction sets with coverage guarantees \\cite{zhang2025conformal}; while complementary, its set-valued output differs from best-of-$N$ selection.\n\n\\paragraph{Best-of-$N$ with learned verifiers.}\n\\citet{gao2023scaling} establish scaling laws for best-of-$N$ selection with learned reward models, showing that BoN performance scales log-linearly with $N$ but eventually degrades due to reward overoptimization.\nOur unsupervised signals face a more fundamental limitation: they cannot rank candidates at all (instance-level signals) or rank them too weakly (LP compression), making the overoptimization regime irrelevant.\nTrained verifiers \\cite{cobbe2021verifiers, lightman2024verify} and quality-aware decoding \\cite{fernandes2022quality} learn per-sample scoring that may bridge this gap; our LoRA-rank ablation (degeneracy 7\\% vs.\\ 21\\%, selection still fails) suggests that verifier training is necessary beyond merely increasing output diversity.\nFine-tuning itself contributes to the problem: \\citet{kirk2024understanding} document diversity collapse in RLHF-trained models; our instance degeneracy is an analogous phenomenon in supervised fine-tuning, where stronger models converge to more uniform outputs.\nNucleus sampling \\cite{holtzman2020curious} improves diversity in open-ended generation, but our constrained structured outputs limit the diversity that temperature scaling alone can recover.\n",
      "numLines": 38,
      "startLine": 1,
      "totalLines": 38
    }
  },
  "sourceToolAssistantUUID": "293847fe-20f7-4ce2-8fd0-538c859b0c56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T07:08:27.150Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FRcTUZFgkERNiYM7SJZvdK`</summary>

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
  "parentUuid": "b09ee798-1fa3-47e6-b41b-2a9d8286ff16",
  "isSidechain": false,
  "requestId": "req_011Cb7ijN1G7omSJC4hPXf1V",
  "type": "assistant",
  "uuid": "c270188b-426c-4db6-a386-e98f8c7d215b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4634eS47gVibKkuxBhDj1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2840,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 29243,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1411,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2840,
          "output_tokens": 315,
          "cache_read_input_tokens": 29243,
          "cache_creation_input_tokens": 1411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1411
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-17T07:08:28.109Z_

<details><summary>↩ Tool result · `toolu_01RxN3UCiusjA8e6XPkUQJr5`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications for practitioners.}
4	For quality estimation, all signals achieve positive $\rho$ across non-collapsed datasets (LP $\rho{=}0.42$ on Few-NERD, VC $\rho{=}0.38$ on SciERC, EM AUROC${=}0.82$ on CoNLL).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.
6	For selection, LP is the only signal achieving significant gains, and only at low degeneracy: $+1.36$~pp on Few-NERD (10\% degeneracy, $p{<}0.001$), $+0.42$~pp on SciERC (21\%, $p{=}0.091$), failure on CoNLL (58\%).
7	Structural signals uniformly degrade selection regardless of dataset.
8	RE signal rankings are reported in Appendix~\ref{app:re_extension}.
9	
10	\paragraph{Why the gap exists.}
11	We identify two mechanisms: \textit{instance degeneracy} (affecting consensus-proximity selection) and \textit{LP compression} (affecting per-sample selection).
12	
13	Within-instance analysis (restricted to non-degenerate instances where F1 varies across samples) reveals that MBR utility \cite{eikema2022sampling} does correlate positively with F1 (SJ median within-instance $\rho{=}0.524$ on SciERC, $0.994$ on CoNLL), and on these instances consensus-proximity selection closes 23\% (SciERC) to 41\% (CoNLL) of the oracle gap.
14	However, fine-tuned models exhibit pervasive \textit{instance degeneracy}: 21\% of SciERC instances (58\% on CoNLL) produce identical F1 across all $N$ samples, offering zero selection headroom; an additional 13\% (49\% on CoNLL) yield constant utility scores, preventing MBR ranking entirely (Table~\ref{tab:degeneracy}).
15	Instance degeneracy is not an artifact of our setup but a consequence of model capability: the better the model, the less room for selection to add value.
16	CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; Few-NERD (75\%) shows 10\%; SciERC (66\%) shows 21\%; WNUT-17 (${\approx}$42\%, macro) shows near-zero---the tension between model quality and selection utility is inherent, though Few-NERD's low degeneracy despite high performance suggests that dataset-specific factors (number of entity types, semantic overlap) also modulate the rate.
17	Scale ablation confirms this tension: Qwen3-8B shows 21\% instance degeneracy on SciERC vs.\ 10.4\% for the weaker Qwen3-4B, despite comparable within-instance utility correlation ($\rho{=}0.52$ vs.\ $0.55$; Table~\ref{tab:degeneracy}).
18	Despite MBR's success in machine translation \cite{freitag2022high}, all consensus-proximity variants consistently fail because degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit (Appendix~\ref{app:mbr_discussion}).
19	On SciERC, LP selection approximately matches greedy decoding ($T{=}0$; $\Delta{=}{+}0.2$~pp, $p{=}0.29$; Table~\ref{tab:selection}); on Few-NERD, where degeneracy drops to 10\%, LP achieves significant gains ($+1.36$~pp, $p{<}0.001$; Table~\ref{tab:fewnerd}), confirming that degeneracy is the gating factor for LP selection.
20	
21	\begin{table}[t]
22	\centering
23	\small
24	\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}
25	\label{tab:degeneracy}
26	\begin{tabular}{lccc}
27	\toprule
28	& \shortstack{SciERC 8B\\($N{=}8$)} & \shortstack{SciERC 4B\\($N{=}8$)} & \shortstack{CoNLL 8B\\($N{=}16$)} \\
29	\midrule
30	Constant F1 & 21\% & 10.4\% & 58\% \\
31	Constant utility & 13\% & 7.0\% & 49\% \\
32	Oracle gap closed (non-deg.) & 23\% & 25.2\% & 41\% \\
33	Within-inst.\ SJ $\rho$ (median) & 0.524 & 0.550 & 0.994 \\
34	\bottomrule
35	\end{tabular}
36	\end{table}
37	
38	Log-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\ref{tab:logprob_ties}), with pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ confirming weak but positive signal.
39	
40	\paragraph{Non-tied subset analysis.}
41	Where compression is mitigated, LP selection works.
42	Restricting to instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total; Table~\ref{tab:nontied_main}), within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied), and LP selection outperforms greedy by $+2.9$~pp ($p{=}0.004$).
43	The effect grows monotonically with $\varepsilon$ (full sweep in Appendix~\ref{app:logprob_ties}), and the $\varepsilon{=}0.05$ result survives Bonferroni correction over 5 comparisons.
44	This demonstrates that LP \textit{does} carry per-sample discriminative information; compression---not signal absence---is the bottleneck.
45	However, the effect size is sensitive to subset definition, and the non-tied subset constitutes only 40\% of instances, limiting practical impact.
46	
47	\begin{table}[t]
48	\centering
49	\small
50	\caption{Non-tied subset analysis (SciERC, Qwen3-8B, $N{=}8$, $T{=}1.0$). Instances split at LP range $\varepsilon{=}0.05$. Within-instance $\rho$ and selection gain both concentrate in the non-tied subset. Full $\varepsilon$ sweep in Appendix~\ref{app:logprob_ties}.}
51	\label{tab:nontied_main}
52	\begin{tabular}{lccc}
53	\toprule
54	Subset & $n$ & $\rho$(LP,F1) & LP $\Delta$ vs.\ greedy \\
55	\midrule
56	Tied (range ${<}0.05$) & 319 & 0.08 & ${\approx}0$ \\
57	Non-tied (range ${\geq}0.05$) & 210 & 0.39 & $+$2.9~pp ($p{=}0.004$) \\
58	\midrule
59	All instances & 529 & 0.248 & $+$0.2~pp ($p{=}0.29$) \\
60	\bottomrule
61	\end{tabular}
62	\end{table}
63	Stratifying by voting confidence reveals a complementary pattern: high-consistency instances (Q4) have collapsed headroom (4.78~pp), leaving nothing to select, while low-consistency instances retain headroom but unreliable LP rankings (Appendix~\ref{app:vc_quartile}).
64	\paragraph{Effect of sample count.}
65	Increasing $N$ from 2 to 32 expands oracle headroom more than fourfold ($+4.4$ to $+19.2$~pp) but yields no commensurate selection improvement: LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\% and oracle headroom reaches ${\sim}19$~pp---the best signal captures less than 5\% of the available improvement (Table~\ref{tab:n_scaling_selection}).
66	VC selection degrades with increasing $N$ ($-2.27$~pp at $N{=}2$ to $-4.18$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.
67	Bootstrap significance testing at $N{=}32$ ($B{=}10{,}000$) confirms that LP shows a consistent positive trend ($+0.95$~pp, $p{=}0.091$) but does not reach significance at $\alpha{=}0.05$, while all signals except VC significantly outperform random selection ($p{<}0.001$; Table~\ref{tab:bootstrap_n32})---the gap is not a statistical artifact but a persistent, regime-dependent limitation.
68	
69	\paragraph{Effect of sampling temperature.}
70	Oracle headroom increases monotonically with temperature ($+7.8$~pp at $T{=}0.5$ to $+13.3$~pp at $T{=}1.0$), plateauing beyond $T{=}1.0$ ($+13.0$~pp at $T{=}1.2$; Table~\ref{tab:t_ablation} in Appendix), confirming that higher temperature produces more diverse candidate pools.
71	Structural QE signals (SJ $\rho$) improve with temperature ($0.297 \to 0.377$), while LP $\rho$ peaks at $T{=}0.8$ ($0.253$) then degrades---consistent with LP compression being model-intrinsic rather than temperature-dependent.
72	Despite expanded headroom and improved QE signals at higher temperatures, selection gains remain negligible, further isolating the bottleneck at the within-instance ranking mechanism rather than signal quality or output diversity.
73	
74	A verbalized confidence baseline confirms that score compression is not LP-specific: the model's self-rated confidence (mean 8.6/10) is even more compressed and yields the weakest selection despite higher $\rho$ than LP (Appendix~\ref{app:verbalized_confidence}; \citealp{bhattacharyya2026beyond}).
75	This intrinsic compression extends beyond logprobs: when explicitly prompted to verbalize confidence on a 1--10 scale, models cluster at 8--9 (CoNLL mean 9.24, std 1.32), exhibiting the same top-biased pattern regardless of output format.
76	
77	\paragraph{Signal combinations.}
78	We test three LP${\times}$VC combination strategies: VC-stratified LP selection, LP${\times}$VC product ranking, and LP tiebreaking within VC-equivalent groups.
79	All three fail to improve over greedy (best: $+0.2$~pp, $p{>}0.3$), consistent with VC's collapse on degenerate instances and LP's compression on the remainder.
80	An oracle tiebreaker---selecting the highest-F1 sample among VC-equivalent candidates---recovers $+7.9$~pp, confirming that per-sample signal \textit{exists} within VC-equivalent groups but current signals cannot extract it.
81	
82	\paragraph{Hypotheses for LP compression.}
83	We identify four (non-mutually-exclusive) mechanisms that may explain within-instance LP compression, though we do not isolate their individual contributions.
84	Two are \textit{constraint-imposed}:
85	(b) \textit{schema-dominated tokens}---constrained decoding enforces structural tokens (brackets, type labels) that carry no extraction information yet dominate the sequence, reducing effective variance;
86	(c) \textit{vocabulary restriction}---constrained decoding shrinks the effective vocabulary at each step, concentrating probability mass and reducing log-probability variation.
87	Two are \textit{model-learned}:
88	(a) \textit{token-level averaging}---mean log-probability over long sequences smooths token-level variance, compressing the effective signal;
89	(d) \textit{format-token dilution}---fine-tuned models assign extremely high LP to schema tokens (\texttt{\{"entities": [}~etc.) that carry no extraction information, diluting the signal from entity-name tokens; free-form parse rates of 99.95\% confirm that format tokens dominate the sequence.
90	The constraint-imposed mechanisms (b)--(c) predict that free-form decoding should reduce compression; our NER ablation finds negligible change (std ratio 0.97; Appendix~\ref{app:freeform_ablation}), suggesting the model-learned mechanisms (a) and (d) are the primary drivers for NER.
91	
92	\paragraph{Ablation: free-form decoding.}\label{sec:ablation}
93	Removing grammar constraints (SciERC NER, Qwen3-8B, 4 seeds) yields nearly identical LP distributions (std ratio 0.97) and negligible selection changes (Appendix~\ref{app:freeform_ablation}), ruling out constrained decoding as the cause of NER compression.
94	Removing format constraints restores LP selection for RE: bootstrap mean $+2.35$~pp (95\% CI [$+0.24$, $+4.50$], $p{=}0.025$, $n{=}397$), though driven by magnitude asymmetry rather than instance-level win rate (sign test: 45W/45L/307T; Appendix~\ref{app:re_extension}).
95	More generally, LP selection failures show cross-seed stability (Jaccard${=}0.42$; Appendix~\ref{app:lp_failure_stability}), indicating a systematic rather than stochastic failure mode.
96	VC becomes per-sample in the selection context (each candidate's overlap with the majority-voted output varies), yet tends to select the most typical rather than the best output---consistent with MBR's known mode-seeking bias \cite{eikema2022sampling, deguchi2024centroid}.
97	More broadly, all consensus-proximity strategies fail because instance degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit (Table~\ref{tab:degeneracy}; Appendix~\ref{app:mbr_discussion}).
98	
99	\paragraph{Ablation: entity-token LP.}
100	We directly test hypothesis (d) by isolating entity-mention tokens from the log-probability computation.
101	On SciERC, entity-token LP exhibits $4{\times}$ higher within-instance variance than full-sequence LP, confirming that format tokens do compress the signal.
102	However, entity-token LP selection performs strictly \textit{worse} than full-sequence LP on both datasets ($-2.0$~pp on SciERC, $-3.3$~pp on CoNLL).
103	Entity tokens are either too sparse (5.3\% of sequence tokens on SciERC) for stable estimation, or nearly saturated (79.4\% of instances tied on CoNLL)---consistent with CoNLL's limited entity vocabulary (4 types, high-frequency names) that fine-tuning drives to near-deterministic prediction.
104	This rules out format-token dilution as the primary cause of LP's selection failure and instead points to an intrinsic pattern: fine-tuned models assign near-deterministic probabilities to entity-name tokens themselves, leaving minimal discriminative signal regardless of aggregation scope.
105	Even disaggregating to entity-token logprobs fails to break compression: on CoNLL, 79.4\% of sample pairs share identical entity-token LP, confirming that compression operates at the representation level rather than being diluted by non-entity tokens.
106	
107	\paragraph{Pilot remedy.}
108	Entity-token LP represents a natural pilot remedy: if format-token dilution caused compression, restricting LP to entity tokens should recover selection ability.
109	Its failure---particularly the near-zero entity-token variance on CoNLL---suggests that effective remedies must address the underlying model confidence calibration rather than signal aggregation.
110	
111	\paragraph{Practical considerations.}
112	Multi-sample inference incurs $N{\times}$ compute cost.
113	For quality estimation---where signals are already reliable ($\rho$ up to 0.45 on CoNLL, 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82)---$N{=}8$ samples suffice (Appendix~\ref{app:n_scaling}), making the cost acceptable for selective prediction or error flagging in high-stakes IE.
114	For selection, the cost-benefit is unfavorable: $8{\times}$ inference yields at most $+0.2$~pp over greedy ($p{>}0.05$).
115	Whether the trade-off shifts in low-convergence regimes (e.g., under-parameterized models where degeneracy drops below 10\%) remains an open question.
116	
117	\paragraph{Regime boundaries.}
118	The correlation-selection gap for structural signals is persistent across all four datasets, but LP selection is degeneracy-gated.
119	At the \textit{low-resource boundary} (WNUT-17, macro F1${\approx}$42\%), QE signals themselves become unreliable: full-set correlations are dominated by the zero/non-zero boundary (VC conditional $\rho{=}0.038$; Table~\ref{tab:wnut}), so selection is moot.
120	At the \textit{ceiling boundary} (CoNLL, F1${\approx}$91\%, 58\% degeneracy), selection shows only a marginal structural exception: VC achieves $+0.28$~pp ($p{<}0.03$) at $N{=}16$, capturing ${\sim}$10\% of the 2.5~pp oracle headroom (Appendix~\ref{app:n_scaling}); LP fails entirely.
121	In the \textit{moderate regime}, instance degeneracy determines LP effectiveness: at 21\% degeneracy (SciERC), LP gains are positive but sub-significant ($+0.42$~pp, $p{=}0.091$); at 10\% degeneracy (Few-NERD), LP achieves highly significant gains ($+1.36$~pp, $p{<}0.001$; Table~\ref{tab:fewnerd}).
122	The cross-dataset gradient (58\% $\to$ fail, 21\% $\to$ weak, 10\% $\to$ strong; $n{=}3$ datasets) is consistent with degeneracy below ${\sim}$15\% being a necessary condition for LP selection; entity-type-level evidence provides stronger statistical grounding (Spearman $\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$; Appendix~\ref{app:per_type_lp}).
123	When candidates differ sufficiently in quality, LP's per-sample signal can exploit the headroom.
124	The pattern persists at finer granularity: per-entity-type analysis on Few-NERD shows 7/8 types with positive LP gains, the sole exception being the highest-degeneracy type (Spearman $\rho(\text{degen}, \text{headroom}){=}{-}0.881$, $p{=}0.004$; Appendix~\ref{app:per_type_lp}).
125	Structural signals fail uniformly regardless of degeneracy because they rank candidates by typicality, not quality.
126	Whether these patterns persist on larger models (70B+) remains open.
127	
128	\paragraph{Methodological implications.}
129	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal.
130	Even supervised combination of all five signals (logistic regression, MLP, random forest) fails to close the oracle gap (\S\ref{sec:robustness_main}), confirming the information bottleneck is in the features themselves, not the aggregation method.
131	Effective selection thus requires content-aware verifiers that examine output semantics \cite{cobbe2021verifiers, venktesh2025trust}, not confidence signal aggregation; $N{=}8$ captures most quality estimation benefit (Appendix~\ref{app:n_scaling}).
132	Structural signals are robust to domain shift when the training schema subsumes the target (Appendix~\ref{app:ood}).
133	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cbb10b8-628d-46e6-b371-e9c368056559",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "d4e201bc-647b-4d9c-901d-218890656f4b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Implications for practitioners.}\nFor quality estimation, all signals achieve positive $\\rho$ across non-collapsed datasets (LP $\\rho{=}0.42$ on Few-NERD, VC $\\rho{=}0.38$ on SciERC, EM AUROC${=}0.82$ on CoNLL).\nRankings hold across model families and a 4B ablation (Table~\\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.\nFor selection, LP is the only signal achieving significant gains, and only at low degeneracy: $+1.36$~pp on Few-NERD (10\\% degeneracy, $p{<}0.001$), $+0.42$~pp on SciERC (21\\%, $p{=}0.091$), failure on CoNLL (58\\%).\nStructural signals uniformly degrade selection regardless of dataset.\nRE signal rankings are reported in Appendix~\\ref{app:re_extension}.\n\n\\paragraph{Why the gap exists.}\nWe identify two mechanisms: \\textit{instance degeneracy} (affecting consensus-proximity selection) and \\textit{LP compression} (affecting per-sample selection).\n\nWithin-instance analysis (restricted to non-degenerate instances where F1 varies across samples) reveals that MBR utility \\cite{eikema2022sampling} does correlate positively with F1 (SJ median within-instance $\\rho{=}0.524$ on SciERC, $0.994$ on CoNLL), and on these instances consensus-proximity selection closes 23\\% (SciERC) to 41\\% (CoNLL) of the oracle gap.\nHowever, fine-tuned models exhibit pervasive \\textit{instance degeneracy}: 21\\% of SciERC instances (58\\% on CoNLL) produce identical F1 across all $N$ samples, offering zero selection headroom; an additional 13\\% (49\\% on CoNLL) yield constant utility scores, preventing MBR ranking entirely (Table~\\ref{tab:degeneracy}).\nInstance degeneracy is not an artifact of our setup but a consequence of model capability: the better the model, the less room for selection to add value.\nCoNLL (91\\% single-sample F1) exhibits 58\\% degeneracy; Few-NERD (75\\%) shows 10\\%; SciERC (66\\%) shows 21\\%; WNUT-17 (${\\approx}$42\\%, macro) shows near-zero---the tension between model quality and selection utility is inherent, though Few-NERD's low degeneracy despite high performance suggests that dataset-specific factors (number of entity types, semantic overlap) also modulate the rate.\nScale ablation confirms this tension: Qwen3-8B shows 21\\% instance degeneracy on SciERC vs.\\ 10.4\\% for the weaker Qwen3-4B, despite comparable within-instance utility correlation ($\\rho{=}0.52$ vs.\\ $0.55$; Table~\\ref{tab:degeneracy}).\nDespite MBR's success in machine translation \\cite{freitag2022high}, all consensus-proximity variants consistently fail because degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit (Appendix~\\ref{app:mbr_discussion}).\nOn SciERC, LP selection approximately matches greedy decoding ($T{=}0$; $\\Delta{=}{+}0.2$~pp, $p{=}0.29$; Table~\\ref{tab:selection}); on Few-NERD, where degeneracy drops to 10\\%, LP achieves significant gains ($+1.36$~pp, $p{<}0.001$; Table~\\ref{tab:fewnerd}), confirming that degeneracy is the gating factor for LP selection.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}\n\\label{tab:degeneracy}\n\\begin{tabular}{lccc}\n\\toprule\n& \\shortstack{SciERC 8B\\\\($N{=}8$)} & \\shortstack{SciERC 4B\\\\($N{=}8$)} & \\shortstack{CoNLL 8B\\\\($N{=}16$)} \\\\\n\\midrule\nConstant F1 & 21\\% & 10.4\\% & 58\\% \\\\\nConstant utility & 13\\% & 7.0\\% & 49\\% \\\\\nOracle gap closed (non-deg.) & 23\\% & 25.2\\% & 41\\% \\\\\nWithin-inst.\\ SJ $\\rho$ (median) & 0.524 & 0.550 & 0.994 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLog-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\\ref{tab:logprob_ties}), with pooled within-instance $\\rho(\\text{LP}, \\text{F1}){=}0.248$ confirming weak but positive signal.\n\n\\paragraph{Non-tied subset analysis.}\nWhere compression is mitigated, LP selection works.\nRestricting to instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total; Table~\\ref{tab:nontied_main}), within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied), and LP selection outperforms greedy by $+2.9$~pp ($p{=}0.004$).\nThe effect grows monotonically with $\\varepsilon$ (full sweep in Appendix~\\ref{app:logprob_ties}), and the $\\varepsilon{=}0.05$ result survives Bonferroni correction over 5 comparisons.\nThis demonstrates that LP \\textit{does} carry per-sample discriminative information; compression---not signal absence---is the bottleneck.\nHowever, the effect size is sensitive to subset definition, and the non-tied subset constitutes only 40\\% of instances, limiting practical impact.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Non-tied subset analysis (SciERC, Qwen3-8B, $N{=}8$, $T{=}1.0$). Instances split at LP range $\\varepsilon{=}0.05$. Within-instance $\\rho$ and selection gain both concentrate in the non-tied subset. Full $\\varepsilon$ sweep in Appendix~\\ref{app:logprob_ties}.}\n\\label{tab:nontied_main}\n\\begin{tabular}{lccc}\n\\toprule\nSubset & $n$ & $\\rho$(LP,F1) & LP $\\Delta$ vs.\\ greedy \\\\\n\\midrule\nTied (range ${<}0.05$) & 319 & 0.08 & ${\\approx}0$ \\\\\nNon-tied (range ${\\geq}0.05$) & 210 & 0.39 & $+$2.9~pp ($p{=}0.004$) \\\\\n\\midrule\nAll instances & 529 & 0.248 & $+$0.2~pp ($p{=}0.29$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\nStratifying by voting confidence reveals a complementary pattern: high-consistency instances (Q4) have collapsed headroom (4.78~pp), leaving nothing to select, while low-consistency instances retain headroom but unreliable LP rankings (Appendix~\\ref{app:vc_quartile}).\n\\paragraph{Effect of sample count.}\nIncreasing $N$ from 2 to 32 expands oracle headroom more than fourfold ($+4.4$ to $+19.2$~pp) but yields no commensurate selection improvement: LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\\% and oracle headroom reaches ${\\sim}19$~pp---the best signal captures less than 5\\% of the available improvement (Table~\\ref{tab:n_scaling_selection}).\nVC selection degrades with increasing $N$ ($-2.27$~pp at $N{=}2$ to $-4.18$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.\nBootstrap significance testing at $N{=}32$ ($B{=}10{,}000$) confirms that LP shows a consistent positive trend ($+0.95$~pp, $p{=}0.091$) but does not reach significance at $\\alpha{=}0.05$, while all signals except VC significantly outperform random selection ($p{<}0.001$; Table~\\ref{tab:bootstrap_n32})---the gap is not a statistical artifact but a persistent, regime-dependent limitation.\n\n\\paragraph{Effect of sampling temperature.}\nOracle headroom increases monotonically with temperature ($+7.8$~pp at $T{=}0.5$ to $+13.3$~pp at $T{=}1.0$), plateauing beyond $T{=}1.0$ ($+13.0$~pp at $T{=}1.2$; Table~\\ref{tab:t_ablation} in Appendix), confirming that higher temperature produces more diverse candidate pools.\nStructural QE signals (SJ $\\rho$) improve with temperature ($0.297 \\to 0.377$), while LP $\\rho$ peaks at $T{=}0.8$ ($0.253$) then degrades---consistent with LP compression being model-intrinsic rather than temperature-dependent.\nDespite expanded headroom and improved QE signals at higher temperatures, selection gains remain negligible, further isolating the bottleneck at the within-instance ranking mechanism rather than signal quality or output diversity.\n\nA verbalized confidence baseline confirms that score compression is not LP-specific: the model's self-rated confidence (mean 8.6/10) is even more compressed and yields the weakest selection despite higher $\\rho$ than LP (Appendix~\\ref{app:verbalized_confidence}; \\citealp{bhattacharyya2026beyond}).\nThis intrinsic compression extends beyond logprobs: when explicitly prompted to verbalize confidence on a 1--10 scale, models cluster at 8--9 (CoNLL mean 9.24, std 1.32), exhibiting the same top-biased pattern regardless of output format.\n\n\\paragraph{Signal combinations.}\nWe test three LP${\\times}$VC combination strategies: VC-stratified LP selection, LP${\\times}$VC product ranking, and LP tiebreaking within VC-equivalent groups.\nAll three fail to improve over greedy (best: $+0.2$~pp, $p{>}0.3$), consistent with VC's collapse on degenerate instances and LP's compression on the remainder.\nAn oracle tiebreaker---selecting the highest-F1 sample among VC-equivalent candidates---recovers $+7.9$~pp, confirming that per-sample signal \\textit{exists} within VC-equivalent groups but current signals cannot extract it.\n\n\\paragraph{Hypotheses for LP compression.}\nWe identify four (non-mutually-exclusive) mechanisms that may explain within-instance LP compression, though we do not isolate their individual contributions.\nTwo are \\textit{constraint-imposed}:\n(b) \\textit{schema-dominated tokens}---constrained decoding enforces structural tokens (brackets, type labels) that carry no extraction information yet dominate the sequence, reducing effective variance;\n(c) \\textit{vocabulary restriction}---constrained decoding shrinks the effective vocabulary at each step, concentrating probability mass and reducing log-probability variation.\nTwo are \\textit{model-learned}:\n(a) \\textit{token-level averaging}---mean log-probability over long sequences smooths token-level variance, compressing the effective signal;\n(d) \\textit{format-token dilution}---fine-tuned models assign extremely high LP to schema tokens (\\texttt{\\{\"entities\": [}~etc.) that carry no extraction information, diluting the signal from entity-name tokens; free-form parse rates of 99.95\\% confirm that format tokens dominate the sequence.\nThe constraint-imposed mechanisms (b)--(c) predict that free-form decoding should reduce compression; our NER ablation finds negligible change (std ratio 0.97; Appendix~\\ref{app:freeform_ablation}), suggesting the model-learned mechanisms (a) and (d) are the primary drivers for NER.\n\n\\paragraph{Ablation: free-form decoding.}\\label{sec:ablation}\nRemoving grammar constraints (SciERC NER, Qwen3-8B, 4 seeds) yields nearly identical LP distributions (std ratio 0.97) and negligible selection changes (Appendix~\\ref{app:freeform_ablation}), ruling out constrained decoding as the cause of NER compression.\nRemoving format constraints restores LP selection for RE: bootstrap mean $+2.35$~pp (95\\% CI [$+0.24$, $+4.50$], $p{=}0.025$, $n{=}397$), though driven by magnitude asymmetry rather than instance-level win rate (sign test: 45W/45L/307T; Appendix~\\ref{app:re_extension}).\nMore generally, LP selection failures show cross-seed stability (Jaccard${=}0.42$; Appendix~\\ref{app:lp_failure_stability}), indicating a systematic rather than stochastic failure mode.\nVC becomes per-sample in the selection context (each candidate's overlap with the majority-voted output varies), yet tends to select the most typical rather than the best output---consistent with MBR's known mode-seeking bias \\cite{eikema2022sampling, deguchi2024centroid}.\nMore broadly, all consensus-proximity strategies fail because instance degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit (Table~\\ref{tab:degeneracy}; Appendix~\\ref{app:mbr_discussion}).\n\n\\paragraph{Ablation: entity-token LP.}\nWe directly test hypothesis (d) by isolating entity-mention tokens from the log-probability computation.\nOn SciERC, entity-token LP exhibits $4{\\times}$ higher within-instance variance than full-sequence LP, confirming that format tokens do compress the signal.\nHowever, entity-token LP selection performs strictly \\textit{worse} than full-sequence LP on both datasets ($-2.0$~pp on SciERC, $-3.3$~pp on CoNLL).\nEntity tokens are either too sparse (5.3\\% of sequence tokens on SciERC) for stable estimation, or nearly saturated (79.4\\% of instances tied on CoNLL)---consistent with CoNLL's limited entity vocabulary (4 types, high-frequency names) that fine-tuning drives to near-deterministic prediction.\nThis rules out format-token dilution as the primary cause of LP's selection failure and instead points to an intrinsic pattern: fine-tuned models assign near-deterministic probabilities to entity-name tokens themselves, leaving minimal discriminative signal regardless of aggregation scope.\nEven disaggregating to entity-token logprobs fails to break compression: on CoNLL, 79.4\\% of sample pairs share identical entity-token LP, confirming that compression operates at the representation level rather than being diluted by non-entity tokens.\n\n\\paragraph{Pilot remedy.}\nEntity-token LP represents a natural pilot remedy: if format-token dilution caused compression, restricting LP to entity tokens should recover selection ability.\nIts failure---particularly the near-zero entity-token variance on CoNLL---suggests that effective remedies must address the underlying model confidence calibration rather than signal aggregation.\n\n\\paragraph{Practical considerations.}\nMulti-sample inference incurs $N{\\times}$ compute cost.\nFor quality estimation---where signals are already reliable ($\\rho$ up to 0.45 on CoNLL, 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82)---$N{=}8$ samples suffice (Appendix~\\ref{app:n_scaling}), making the cost acceptable for selective prediction or error flagging in high-stakes IE.\nFor selection, the cost-benefit is unfavorable: $8{\\times}$ inference yields at most $+0.2$~pp over greedy ($p{>}0.05$).\nWhether the trade-off shifts in low-convergence regimes (e.g., under-parameterized models where degeneracy drops below 10\\%) remains an open question.\n\n\\paragraph{Regime boundaries.}\nThe correlation-selection gap for structural signals is persistent across all four datasets, but LP selection is degeneracy-gated.\nAt the \\textit{low-resource boundary} (WNUT-17, macro F1${\\approx}$42\\%), QE signals themselves become unreliable: full-set correlations are dominated by the zero/non-zero boundary (VC conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}), so selection is moot.\nAt the \\textit{ceiling boundary} (CoNLL, F1${\\approx}$91\\%, 58\\% degeneracy), selection shows only a marginal structural exception: VC achieves $+0.28$~pp ($p{<}0.03$) at $N{=}16$, capturing ${\\sim}$10\\% of the 2.5~pp oracle headroom (Appendix~\\ref{app:n_scaling}); LP fails entirely.\nIn the \\textit{moderate regime}, instance degeneracy determines LP effectiveness: at 21\\% degeneracy (SciERC), LP gains are positive but sub-significant ($+0.42$~pp, $p{=}0.091$); at 10\\% degeneracy (Few-NERD), LP achieves highly significant gains ($+1.36$~pp, $p{<}0.001$; Table~\\ref{tab:fewnerd}).\nThe cross-dataset gradient (58\\% $\\to$ fail, 21\\% $\\to$ weak, 10\\% $\\to$ strong; $n{=}3$ datasets) is consistent with degeneracy below ${\\sim}$15\\% being a necessary condition for LP selection; entity-type-level evidence provides stronger statistical grounding (Spearman $\\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$; Appendix~\\ref{app:per_type_lp}).\nWhen candidates differ sufficiently in quality, LP's per-sample signal can exploit the headroom.\nThe pattern persists at finer granularity: per-entity-type analysis on Few-NERD shows 7/8 types with positive LP gains, the sole exception being the highest-degeneracy type (Spearman $\\rho(\\text{degen}, \\text{headroom}){=}{-}0.881$, $p{=}0.004$; Appendix~\\ref{app:per_type_lp}).\nStructural signals fail uniformly regardless of degeneracy because they rank candidates by typicality, not quality.\nWhether these patterns persist on larger models (70B+) remains open.\n\n\\paragraph{Methodological implications.}\nThe decoupling of $\\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal.\nEven supervised combination of all five signals (logistic regression, MLP, random forest) fails to close the oracle gap (\\S\\ref{sec:robustness_main}), confirming the information bottleneck is in the features themselves, not the aggregation method.\nEffective selection thus requires content-aware verifiers that examine output semantics \\cite{cobbe2021verifiers, venktesh2025trust}, not confidence signal aggregation; $N{=}8$ captures most quality estimation benefit (Appendix~\\ref{app:n_scaling}).\nStructural signals are robust to domain shift when the training schema subsumes the target (Appendix~\\ref{app:ood}).\n",
      "numLines": 133,
      "startLine": 1,
      "totalLines": 133
    }
  },
  "sourceToolAssistantUUID": "7cbb10b8-628d-46e6-b371-e9c368056559",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-17T07:08:27.156Z_

<details><summary>↩ Tool result · `toolu_01FRcTUZFgkERNiYM7SJZvdK`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{&lt;j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
27	\begin{equation}\label{eq:fk}
28	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
29	\end{equation}
30	where $\bar{P}$ is mean observed and $\bar{P}_e$ expected agreement.
31	Temperature-based sampling introduces mild negative dependence ($-$0.4\% to $-$4.0\%; Appendix~\ref{app:fk_independence}), which does not inflate FK.
32	Unlike structural signals, FK relies on exact string matching.
33	
34	\paragraph{Soft Jaccard (structural, instance-level).}
35	For samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU), and define:
36	\begin{equation}\label{eq:sj}
37	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
38	\end{equation}
39	where $M$ is the matched set, $\text{sim}(a_m, b_m)$ is the token-level IoU between matched spans, and $\max(|g_i|, |g_j|)$ penalizes length asymmetry.\footnote{The denominator uses $\max(|g_i|, |g_j|)$ per type group rather than $|A \cup B|$, penalizing cardinality mismatches more heavily than standard Jaccard; the two variants produce nearly identical rankings ($\Delta\rho{<}0.01$; Table~\ref{tab:sj_normalizer}).}
40	The instance-level QE signal averages over all pairs:
41	\begin{equation}\label{eq:sj_instance}
42	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i&lt;j} \text{SJ}(y_i, y_j)
43	\end{equation}
44	For selection, $c_{\text{sj}}(x)$ cannot rank individual candidates (it assigns one score per input).
45	Consensus-proximity converts it to a per-sample utility $u_{\text{sj}}(y_i) = \frac{1}{N-1} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, selecting the candidate most consistent with the sample pool---equivalent to minimum Bayes risk (MBR) decoding \cite{eikema2022sampling} with SJ as the utility function.
46	The same construction applies to FK, EM, and VC.
47	
48	\paragraph{Entity voting confidence (structural, instance-level).}
49	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
50	The instance-level confidence is the mean frequency:
51	\begin{equation}\label{eq:voting}
52	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
53	\end{equation}
54	When $E_\cup = \emptyset$, we set $c_{\mathrm{vc}}(x) = 0$.\footnote{Equation~\ref{eq:voting} defines the continuous QE signal; for voted-output \textit{selection} (Table~\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting.}
55	
56	\subsection{Evaluation Framework}\label{sec:evaluation}
57	
58	\paragraph{Quality estimation.}
59	Spearman $\rho$ between the signal and instance-level F1, and AUROC classifying instances as above/below median F1.
60	Both quality estimation and selection exclude instances with no gold annotations: $n{=}529$ on SciERC (from 551), $n{=}2{,}756$ on CoNLL (from 3{,}453).\footnote{On CoNLL, full-set ($n{=}3{,}453$) Spearman $\rho$ values are higher than gold-filtered ($n{=}2{,}756$) by $+0.03$--$0.05$ due to the zero/non-zero boundary inflating correlations, paralleling the effect documented for WNUT-17 in Appendix~\ref{app:additional}.}
61	
62	\paragraph{Sample selection.}
63	Best-of-$N$ F1: per-sample signals (LP) directly rank candidates; instance-level signals rank via consensus-proximity (MBR utility; see SJ definition above).
64	Baselines: \textit{oracle} (highest-F1 sample) and \textit{greedy} ($T{=}0$ argmax decoding).
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c270188b-426c-4db6-a386-e98f8c7d215b",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "1b392c6c-ece2-4627-84da-66e58f725fcf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven model $\\mathcal{M}$ and input $x$, we sample $N$ outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}, where each $y_i$ is an entity set.\nA \\textbf{per-sample signal} $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$ scores each output independently; an \\textbf{instance-level signal} $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$ produces a single score per input (notation in Appendix~\\ref{app:notation}).\nThis distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\\S\\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nFour are \\textit{consistency signals}: \\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \\textit{surface} (exact match [EM], Fleiss' $\\kappa$ [FK]); log-probability [LP] is the sole \\textit{model-internal}, per-sample signal.\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{&lt;j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed and $\\bar{P}_e$ expected agreement.\nTemperature-based sampling introduces mild negative dependence ($-$0.4\\% to $-$4.0\\%; Appendix~\\ref{app:fk_independence}), which does not inflate FK.\nUnlike structural signals, FK relies on exact string matching.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nFor samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU), and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set, $\\text{sim}(a_m, b_m)$ is the token-level IoU between matched spans, and $\\max(|g_i|, |g_j|)$ penalizes length asymmetry.\\footnote{The denominator uses $\\max(|g_i|, |g_j|)$ per type group rather than $|A \\cup B|$, penalizing cardinality mismatches more heavily than standard Jaccard; the two variants produce nearly identical rankings ($\\Delta\\rho{<}0.01$; Table~\\ref{tab:sj_normalizer}).}\nThe instance-level QE signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i&lt;j} \\text{SJ}(y_i, y_j)\n\\end{equation}\nFor selection, $c_{\\text{sj}}(x)$ cannot rank individual candidates (it assigns one score per input).\nConsensus-proximity converts it to a per-sample utility $u_{\\text{sj}}(y_i) = \\frac{1}{N-1} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, selecting the candidate most consistent with the sample pool---equivalent to minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling} with SJ as the utility function.\nThe same construction applies to FK, EM, and VC.\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\nWhen $E_\\cup = \\emptyset$, we set $c_{\\mathrm{vc}}(x) = 0$.\\footnote{Equation~\\ref{eq:voting} defines the continuous QE signal; for voted-output \\textit{selection} (Table~\\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting.}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nSpearman $\\rho$ between the signal and instance-level F1, and AUROC classifying instances as above/below median F1.\nBoth quality estimation and selection exclude instances with no gold annotations: $n{=}529$ on SciERC (from 551), $n{=}2{,}756$ on CoNLL (from 3{,}453).\\footnote{On CoNLL, full-set ($n{=}3{,}453$) Spearman $\\rho$ values are higher than gold-filtered ($n{=}2{,}756$) by $+0.03$--$0.05$ due to the zero/non-zero boundary inflating correlations, paralleling the effect documented for WNUT-17 in Appendix~\\ref{app:additional}.}\n\n\\paragraph{Sample selection.}\nBest-of-$N$ F1: per-sample signals (LP) directly rank candidates; instance-level signals rank via consensus-proximity (MBR utility; see SJ definition above).\nBaselines: \\textit{oracle} (highest-F1 sample) and \\textit{greedy} ($T{=}0$ argmax decoding).\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  },
  "sourceToolAssistantUUID": "c270188b-426c-4db6-a386-e98f8c7d215b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-17T07:08:27.518Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Lzz9zBcKqWiDzMNvbtgaxg`</summary>

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
  "parentUuid": "1b392c6c-ece2-4627-84da-66e58f725fcf",
  "isSidechain": false,
  "requestId": "req_011Cb7ijN1G7omSJC4hPXf1V",
  "type": "assistant",
  "uuid": "e283346a-ed55-4eeb-9e48-83d8708c82a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4634eS47gVibKkuxBhDj1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2840,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 29243,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1411,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2840,
          "output_tokens": 315,
          "cache_read_input_tokens": 29243,
          "cache_creation_input_tokens": 1411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1411
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-17T07:08:27.523Z_

<details><summary>↩ Tool result · `toolu_01Lzz9zBcKqWiDzMNvbtgaxg`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
16	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
17	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
18	Inference uses vLLM with constrained decoding \cite{willard2023guided}.\footnote{Quality estimation uses a single primary seed (seed${=}42$); selection uses 2-seed averages for variance estimation. Three-seed experiments ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}) confirm ranking stability; the reduced seed count for primary results reflects computational budget.}
19	
20	%% ============================================================
21	\subsection{Quality Estimation Results}
22	\label{sec:qe_results}
23	
24	\begin{table*}[t]
25	\centering
26	\small
27	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
28	\label{tab:quality_estimation}
29	\begin{tabular}{ll cc cc cc}
30	\toprule
31	& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
32	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}
33	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
34	\midrule
35	VC & Structural & \textbf{.379} & \textbf{.663} & .424 & .789 & .426 & .709 \\
36	SJ  & Structural & .360 & .650 & .436 & .801 & \textbf{.431} & .704 \\
37	FK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\
38	EM  & Surface    & .295 & .614 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
39	\midrule
40	LP     & Model      & .205 & .578 & .316 & .753 & .307 & \textbf{.761} \\
41	\bottomrule
42	\end{tabular}
43	\end{table*}
44	
45	Table~\ref{tab:quality_estimation} presents $\rho$ and AUROC for five signals across tasks and models.\footnote{$\varepsilon{=}0.05$ applies only to selection (\S\ref{sec:selection_gap}); quality estimation is $\varepsilon$-free. Selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}).}
46	
47	\paragraph{Signal rankings are difficulty-dependent.}
48	On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over surface ($\rho{\leq}0.295$) and LP ($0.205$); bootstrap CIs confirm the SJ--LP gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
49	On CoNLL (ceiling-effect control, single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$); the $\rho$--AUROC dissociation across datasets reflects use-case alignment.
50	At the signal-collapse boundary---WNUT-17 (macro F1${\approx}$42\%, 52\% zero-F1 instances)---full-set correlations are dominated by the zero/non-zero boundary: VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) but conditional $\rho$ drops to 0.038 (Table~\ref{tab:wnut}).
51	LP shows the reverse pattern (full-set $\rho{=}{-}0.410$, conditional $\rho{=}0.350$), confirming that full-set correlations conflate binary success prediction with quality gradation.
52	Restricting to non-zero instances reshuffles rankings, with EM strongest ($\rho{=}0.360$; Figure~\ref{fig:signal_heatmap}).
53	
54	\begin{table}[t]
55	\centering
56	\small
57	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\rho$ reflects binary success prediction; conditional $\rho$ measures quality gradation. LP's conditional $\rho$ is highest despite negative full-set $\rho$.}
58	\label{tab:wnut}
59	\begin{tabular}{lcccc}
60	\toprule
61	Signal & $\rho$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
62	\midrule
63	VC      & .724 & .913 & .038 & .487 \\
64	FK      & .125 & .555 & .169 & .002 \\
65	SJ      & .089 & .517 & .288 & ${<}$1e-7 \\
66	EM      & .050 & .487 & .333 & ${<}$1e-9 \\
67	LP & $-$.410 & .219 & .350 & ${<}$1e-10 \\
68	\bottomrule
69	\end{tabular}
70	\end{table}
71	
72	%% ============================================================
73	\subsection{The Correlation-Selection Gap}
74	\label{sec:selection_gap}
75	
76	We define the correlation-selection gap as the disparity between a signal's instance-level rank correlation with F1 and its ability to select the best output from $N$ candidates.
77	
78	Our argument proceeds in three layers.
79	First, four of five signals (SJ, FK, EM, VC) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; they \textit{cannot} rank candidates within an instance by construction, and consensus-proximity (MBR) conversion does not reliably recover per-sample ranking.
80	Second, MBR selection with well-aligned utility (within-instance SJ--F1 $\rho{=}0.52$) should in principle select better outputs, but instance degeneracy collapses the candidate pool, eliminating the headroom MBR would otherwise exploit.
81	Third, LP, the sole natively per-sample signal, provides genuine ranking information but suffers from extreme compression (median within-instance range 0.041 nats), limiting its discriminative power except in low-degeneracy regimes.
82	
83	\begin{table}[t]
84	\centering
85	\small
86	\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$, $p$ vs.\ greedy baseline from paired sign tests). LP is per-sample; others use consensus-proximity. Best non-oracle in \textbf{bold}. Random: uniform random selection from $N$ candidates. Non-tied LP subset analysis in \S\ref{sec:discussion}; RE selection in Appendix~\ref{app:re_extension}.}
87	\label{tab:selection}
88	\begin{tabular}{lcc}
89	\toprule
90	Method & NER F1 & $p$ \\
91	\midrule
92	Oracle & $0.778 \pm 0.003$ & --- \\
93	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
94	\midrule
95	\multicolumn{3}{l}{\textit{Per-sample signal}} \\
96	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
97	\midrule
98	\multicolumn{3}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
99	SJ           & $0.646 \pm 0.002$ & .67 \\
100	FK           & $0.646 \pm 0.001$ & .79 \\
101	EM           & $0.637 \pm 0.001$ & --- \\
102	VC           & $0.623 \pm 0.004$ & --- \\
103	\midrule
104	Random           & $0.610 \pm 0.003$ & --- \\
105	\bottomrule
106	\end{tabular}
107	\end{table}
108	
109	Despite moderate quality estimation, confidence signals yield limited selection gains (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
110	The 3.5~pp gap between greedy (0.645) and random selection (0.610) reflects the difference between deterministic decoding ($T{=}0$) and uniformly sampling one of $N$ stochastic candidates ($T{=}1.0$); greedy is not drawn from the candidate pool.
111	Instance-level signals (SJ, FK, EM, VC) assign identical QE scores to all candidates per input; consensus-proximity (MBR) converts these to per-sample rankings (Table~\ref{tab:selection}: SJ 0.646, FK 0.646, EM 0.637, VC 0.623), but none consistently improves over the greedy baseline on the primary test bed.
112	The key question is whether LP---the only natively per-sample signal---can exploit the oracle headroom.
113	
114	\paragraph{No significant improvement over greedy.}
115	On SciERC NER (2-seed sign tests\footnote{Multi-seed NER experiments confirm seed variation is small ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}).}, $n{=}529$), the oracle (0.778) reveals 13.3~pp of headroom above greedy (0.645), yet LP achieves only 0.647 ($\Delta{=}{+}0.2$~pp, $d{=}0.038$, $p{=}0.29$); the observed LP advantage is small and not reliably detected at $N{=}8$ (absence of evidence should not be equated with evidence of absence; TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration, Appendix~\ref{app:tost}).
116	The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}); RE selection results are consistent (Appendix~\ref{app:re_extension}).
117	With $N{=}16$, LP selection on SciERC yields a paired improvement of $+0.52$~pp (bootstrap $p{=}0.003$), suggesting the signal becomes actionable at larger candidate pools where degeneracy drops and headroom expands.
118	Few-NERD provides a stronger demonstration: LP achieves significant gains ($+1.36$~pp, $p{<}0.001$) at low degeneracy, while structural signals still fail (\S\ref{sec:fewnerd}).
119	CoNLL's near-ceiling single-sample F1 (0.91) with only ${\sim}$4~pp oracle headroom functions primarily as a ceiling-effect control.
120	Under stringent external TOST anchors ($\delta_0{=}1.0$~pp), some configurations (e.g., Qwen CoNLL) show statistically significant degradation (0.9--1.5~pp below greedy), indicating that signal-based selection can be actively harmful rather than merely ineffective (Appendix~\ref{app:tost}).
121	LP approximately matches greedy decoding ($T{=}0$; $\Delta{=}{+}0.2$~pp, not significant); neither significantly outperforms the other, yet both fall far short of the oracle (0.778, 13.3~pp gap).
122	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best; closing this gap likely requires trained verifiers \cite{cobbe2021verifiers}.\footnote{For negative results (all $p{>}0.05$), uncorrected tests suffice; the sole positive finding (non-tied LP subset, $+2.9$~pp, $p{=}0.004$; \S\ref{sec:discussion}) survives Bonferroni correction over 5 comparisons.}
123	
124	%% ============================================================
125	\subsection{Cross-Dataset Contrast: Few-NERD}
126	\label{sec:fewnerd}
127	
128	\begin{table}[t]
129	\centering
130	\small
131	\caption{Cross-dataset comparison of LP selection effectiveness (Qwen3-8B, $N{=}8$, $T{=}1.0$). LP selection gains are inversely associated with instance degeneracy across three datasets. Few-NERD uses gold-filtered evaluation ($n{=}32{,}565$); SciERC uses full test set ($n{=}551$) for protocol consistency.\protect\footnotemark}
132	\label{tab:fewnerd}
133	\begin{tabular}{lcccccc}
134	\toprule
135	Dataset & $n$ & Greedy & Headroom & Degen\% & LP $\rho$ & LP $\Delta$ \\
136	\midrule
137	CoNLL & 2{,}756 & .908 & 4.0\,pp & 58\% & .316 & fail \\
138	SciERC & 551 & .614 & 13.8\,pp & 21\% & .205 & $+$0.42\,pp \\
139	Few-NERD & 32{,}565 & .748 & 12.4\,pp & 10.1\% & .421 & $\mathbf{+1.36}$\,pp \\
140	\bottomrule
141	\end{tabular}
142	\end{table}
143	\footnotetext{SciERC greedy (0.614) and headroom (13.8~pp) differ from Table~\ref{tab:selection} (gold-filtered $n{=}529$, greedy${=}0.645$) due to full-set evaluation; the ranking and significance are unchanged.}
144	
145	Few-NERD (Table~\ref{tab:fewnerd}) reveals that LP selection effectiveness is inversely associated with instance degeneracy across datasets.
146	At 10.1\% degeneracy (vs.\ SciERC's 21\%, CoNLL's 58\%), LP achieves highly significant selection gains ($+1.36$~pp, 95\% CI $[+1.18, +1.53]$, $p{<}0.001$), while all other signals degrade selection (VC $-1.79$, SJ $-2.14$, FK $-2.26$, EM $-3.85$~pp).
147	
148	\paragraph{Degeneracy as a necessary condition.}
149	Low degeneracy is necessary for LP selection: the cross-dataset gradient is monotonic (58\% $\to$ fail, 21\% $\to$ $+0.42$~pp, 10\% $\to$ $+1.36$~pp), and degeneracy below ${\sim}$15\% consistently enables positive LP gains (Figure~\ref{fig:degeneracy_scatter}).
150	However, within a dataset, LP signal quality ($\rho$) provides an additional prerequisite: per-type analysis shows that low degeneracy alone does not guarantee gains (Appendix~\ref{app:per_type_lp}).
151	The LoRA-rank ablation (\S\ref{sec:robustness_main}) corroborates this interaction: reducing rank lowers SciERC degeneracy from 21\% to 7\% and increases oracle headroom, though LP selection still fails there, confirming that degeneracy is necessary but not sufficient.
152	
153	\paragraph{The correlation-selection gap persists for structural signals.}
154	All five signals achieve positive quality estimation on Few-NERD (LP $\rho{=}0.42$, VC $0.39$, FK $0.31$, SJ $0.30$, EM $0.29$), yet only LP translates QE into selection.
155	The gap between VC's quality estimation ($\rho{=}0.39$) and its selection outcome ($-1.79$~pp) confirms that the gap is not an artifact of weak QE: even strong instance-level QE signals cannot rank candidates within an instance.
156	Within Few-NERD, the degeneracy-gating pattern holds at entity-type granularity: 7 of 8 types show positive LP selection gains ($+0.23$ to $+4.73$~pp), while the highest-degeneracy type (Art, 19.8\%) is the sole exception (Appendix~\ref{app:per_type_lp}).
157	
158	\begin{figure}[t]
159	\centering
160	\includegraphics[width=\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}
161	\caption{Instance degeneracy vs.\ LP selection gain. Blue circles: cross-dataset aggregates (CoNLL, SciERC, Few-NERD); orange triangles: per-entity-type within Few-NERD. The dashed line at ${\sim}$15\% separates a regime where LP selection improves over greedy (left) from one where it fails (right). Cross-dataset ordering is monotonic; 7/8 Few-NERD entity types below 20\% degeneracy show positive gains. Degeneracy below ${\sim}$15\% appears necessary for LP selection to succeed (Spearman $\rho{=}{-}0.57$, $p{=}0.066$, $n{=}11$).}
162	\label{fig:degeneracy_scatter}
163	\end{figure}
164	
165	Figure~\ref{fig:degeneracy_scatter} visualizes the relationship across both dataset-level and entity-type-level granularity: degeneracy below ${\sim}$15\% appears necessary for LP selection gains.
166	The pooled Spearman correlation ($\rho{=}{-}0.57$, $p{=}0.066$, $n{=}11$) treats dataset-level and entity-type-level points as independent; the entity-type-level evidence alone provides stronger grounding ($\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$).
167	
168	\paragraph{LP selection scales with sample budget in the low-degeneracy regime.}
169	On the same 4{,}351 Few-NERD instances, doubling $N$ from 8 to 16 yields a significant additional $+0.52$~pp (paired bootstrap $p{=}0.003$, 95\% CI $[+0.17, +0.87]$): LP selection improves from $+1.37$~pp to $+1.88$~pp (both $p{<}0.001$).
170	The gain is driven by reduced degeneracy (11.1\% $\to$ 4.5\%) expanding oracle headroom (12.1 $\to$ 15.4~pp), while LP ranking quality remains stable ($\rho{\approx}0.62$), confirming that signal quality is model-intrinsic rather than $N$-dependent.
171	At $N{=}16$, all 8 entity types show positive LP gains, including types that were negative at $N{=}8$.
172	Structural signals remain uniformly negative at $N{=}16$ (SJ $-1.36$, FK $-1.47$~pp), reinforcing that the correlation-selection gap for consensus-based methods persists regardless of sample budget.
173	
174	%% ============================================================
175	\subsection{Robustness}
176	\label{sec:robustness_main}
177	
178	Consistency signals are robust across $T{\in}\{0.7, 1.0\}$ with sublinear $N$-scaling gains (Table~\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\Delta\rho{=}{+}0.044$).
179	Signal rankings are stable across seeds (Kendall's $W{=}1.0$ at $N{=}8$, though statistical precision is limited with $m{=}3$ raters, exact $p{\approx}0.028$; Table~\ref{tab:ranking-stability}).
180	NER calibration is reasonable (ECE 0.069--0.096; Appendix~\ref{app:calibration}).
181	
182	\begin{table}[t]
183	\centering
184	\small
185	\caption{Scale ablation: Qwen3-8B vs.\ 4B NER quality estimation ($\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. RE scale ablation in Appendix~\ref{app:re_extension}.}
186	\label{tab:scale_ablation}
187	\begin{tabular}{@{}ll cc r@{}}
188	\toprule
189	& & \textbf{8B} & \textbf{4B} & $\Delta$ \\
190	\midrule
191	CoNLL & SJ & .436 & .422 & $-$.014 \\
192	      & FK & .400 & .418 & $+$.018 \\
193	SciERC & SJ & .360 & .422 & $+$.062 \\
194	       & FK & .267 & .326 & $+$.059 \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
199	\paragraph{Scale robustness.}
200	Repeating with Qwen3-4B (Table~\ref{tab:scale_ablation}), quality estimation is comparable or improved (mean $|\Delta\rho|{=}0.042$), yet selection remains below greedy on SciERC ($\Delta$ up to $-3.4$~pp) despite 13.0~pp of oracle headroom, and indistinguishable on CoNLL (${<}0.3$~pp, 1.7~pp headroom). Within the 3B--8B range tested across two model families, task difficulty is a stronger predictor of the gap than model scale; results hold at smaller scale (LLaMA-3.2-3B, 13.6~pp headroom; Appendix~\ref{app:llama3b}).
201	Instance degeneracy also scales with model capability: 8B shows twice the degeneracy of 4B on SciERC (21\% vs.\ 10.4\%) despite comparable within-instance utility correlation (Table~\ref{tab:degeneracy}).
202	
203	\paragraph{LoRA-rank ablation.}
204	To disentangle model capacity from degeneracy, we train Qwen3-8B on SciERC with LoRA rank${=}8$ (vs.\ rank${=}32$ in all other experiments).
205	Reducing rank lowers degeneracy from 21\% to 7.2\% and increases oracle headroom from 13.3~pp to 16.0~pp, confirming that fine-tuning capacity drives output convergence.
206	However, selection still fails: the best signal (LP, 0.635) falls short of greedy (0.640), and all consensus-proximity signals perform worse (SJ 0.631, VC 0.592).
207	Quality estimation remains comparable (VC $\rho{=}0.394$ vs.\ $0.379$; SJ $\rho{=}0.365$ vs.\ $0.360$).
208	Low degeneracy is thus a necessary but not sufficient condition for selection---LP compression persists regardless of LoRA rank, indicating that both mechanisms must be addressed simultaneously.
209	
210	\paragraph{Supervised verifier baseline.}
211	To test whether the information bottleneck lies in the aggregation method or the features themselves, we train a logistic regression verifier on all five signals (3-fold cross-validation on SciERC, $N{=}16$---giving the verifier access to twice as many samples as the main results).
212	The supervised selector achieves F1${=}0.641$, below both LP (0.647) and greedy (0.644),\footnote{Greedy F1 is 0.644 (3-seed mean in the verifier experiment), consistent with Table~\ref{tab:selection} (0.645, 2-seed mean on the gold-filtered subset).} closing none of the oracle gap despite the additional samples.
213	Its AUROC (0.652) is lower than single-signal VC (0.706), and feature importance is dominated by VC (coefficient 0.65--0.92) with SJ receiving a negative coefficient.
214	A 2-layer MLP and random forest on the same five features achieve comparable or slightly worse performance (MLP AUROC: 0.639; RF: 0.604), confirming that the bottleneck lies in the feature space rather than the aggregation model.
215	The failure of supervised signal combination confirms that the bottleneck is not in how signals are aggregated but in what information they encode: these features lack per-sample discriminative content sufficient for selection.
216	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e283346a-ed55-4eeb-9e48-83d8708c82a8",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "a49915f8-8259-4328-820e-aed538519d86",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 52\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures.\nQwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\\ref{app:thinking_token}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\\ref{app:n_scaling}).}\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\\footnote{Quality estimation uses a single primary seed (seed${=}42$); selection uses 2-seed averages for variance estimation. Three-seed experiments ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}) confirm ranking stability; the reduced seed count for primary results reflects computational budget.}\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. RE results in Appendix~\\ref{app:re_extension}. $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models.\\footnote{$\\varepsilon{=}0.05$ applies only to selection (\\S\\ref{sec:selection_gap}); quality estimation is $\\varepsilon$-free. Selection F1 is stable across $\\varepsilon \\in [0, 0.2]$ (Appendix~\\ref{app:epsilon_robustness}).}\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over surface ($\\rho{\\leq}0.295$) and LP ($0.205$); bootstrap CIs confirm the SJ--LP gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (ceiling-effect control, single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$); the $\\rho$--AUROC dissociation across datasets reflects use-case alignment.\nAt the signal-collapse boundary---WNUT-17 (macro F1${\\approx}$42\\%, 52\\% zero-F1 instances)---full-set correlations are dominated by the zero/non-zero boundary: VC achieves $\\rho{=}0.724$ (AUROC${=}0.913$) but conditional $\\rho$ drops to 0.038 (Table~\\ref{tab:wnut}).\nLP shows the reverse pattern (full-set $\\rho{=}{-}0.410$, conditional $\\rho{=}0.350$), confirming that full-set correlations conflate binary success prediction with quality gradation.\nRestricting to non-zero instances reshuffles rankings, with EM strongest ($\\rho{=}0.360$; Figure~\\ref{fig:signal_heatmap}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\\rho$ reflects binary success prediction; conditional $\\rho$ measures quality gradation. LP's conditional $\\rho$ is highest despite negative full-set $\\rho$.}\n\\label{tab:wnut}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\rho$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & .913 & .038 & .487 \\\\\nFK      & .125 & .555 & .169 & .002 \\\\\nSJ      & .089 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nWe define the correlation-selection gap as the disparity between a signal's instance-level rank correlation with F1 and its ability to select the best output from $N$ candidates.\n\nOur argument proceeds in three layers.\nFirst, four of five signals (SJ, FK, EM, VC) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; they \\textit{cannot} rank candidates within an instance by construction, and consensus-proximity (MBR) conversion does not reliably recover per-sample ranking.\nSecond, MBR selection with well-aligned utility (within-instance SJ--F1 $\\rho{=}0.52$) should in principle select better outputs, but instance degeneracy collapses the candidate pool, eliminating the headroom MBR would otherwise exploit.\nThird, LP, the sole natively per-sample signal, provides genuine ranking information but suffers from extreme compression (median within-instance range 0.041 nats), limiting its discriminative power except in low-degeneracy regimes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$, $p$ vs.\\ greedy baseline from paired sign tests). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. Random: uniform random selection from $N$ candidates. Non-tied LP subset analysis in \\S\\ref{sec:discussion}; RE selection in Appendix~\\ref{app:re_extension}.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & $p$ \\\\\n\\midrule\nOracle & $0.778 \\pm 0.003$ & --- \\\\\nGreedy ($T{=}0$) & $0.645 \\pm 0.001$ & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .67 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 \\\\\nEM           & $0.637 \\pm 0.001$ & --- \\\\\nVC           & $0.623 \\pm 0.004$ & --- \\\\\n\\midrule\nRandom           & $0.610 \\pm 0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite moderate quality estimation, confidence signals yield limited selection gains (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nThe 3.5~pp gap between greedy (0.645) and random selection (0.610) reflects the difference between deterministic decoding ($T{=}0$) and uniformly sampling one of $N$ stochastic candidates ($T{=}1.0$); greedy is not drawn from the candidate pool.\nInstance-level signals (SJ, FK, EM, VC) assign identical QE scores to all candidates per input; consensus-proximity (MBR) converts these to per-sample rankings (Table~\\ref{tab:selection}: SJ 0.646, FK 0.646, EM 0.637, VC 0.623), but none consistently improves over the greedy baseline on the primary test bed.\nThe key question is whether LP---the only natively per-sample signal---can exploit the oracle headroom.\n\n\\paragraph{No significant improvement over greedy.}\nOn SciERC NER (2-seed sign tests\\footnote{Multi-seed NER experiments confirm seed variation is small ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}).}, $n{=}529$), the oracle (0.778) reveals 13.3~pp of headroom above greedy (0.645), yet LP achieves only 0.647 ($\\Delta{=}{+}0.2$~pp, $d{=}0.038$, $p{=}0.29$); the observed LP advantage is small and not reliably detected at $N{=}8$ (absence of evidence should not be equated with evidence of absence; TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration, Appendix~\\ref{app:tost}).\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); RE selection results are consistent (Appendix~\\ref{app:re_extension}).\nWith $N{=}16$, LP selection on SciERC yields a paired improvement of $+0.52$~pp (bootstrap $p{=}0.003$), suggesting the signal becomes actionable at larger candidate pools where degeneracy drops and headroom expands.\nFew-NERD provides a stronger demonstration: LP achieves significant gains ($+1.36$~pp, $p{<}0.001$) at low degeneracy, while structural signals still fail (\\S\\ref{sec:fewnerd}).\nCoNLL's near-ceiling single-sample F1 (0.91) with only ${\\sim}$4~pp oracle headroom functions primarily as a ceiling-effect control.\nUnder stringent external TOST anchors ($\\delta_0{=}1.0$~pp), some configurations (e.g., Qwen CoNLL) show statistically significant degradation (0.9--1.5~pp below greedy), indicating that signal-based selection can be actively harmful rather than merely ineffective (Appendix~\\ref{app:tost}).\nLP approximately matches greedy decoding ($T{=}0$; $\\Delta{=}{+}0.2$~pp, not significant); neither significantly outperforms the other, yet both fall far short of the oracle (0.778, 13.3~pp gap).\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best; closing this gap likely requires trained verifiers \\cite{cobbe2021verifiers}.\\footnote{For negative results (all $p{>}0.05$), uncorrected tests suffice; the sole positive finding (non-tied LP subset, $+2.9$~pp, $p{=}0.004$; \\S\\ref{sec:discussion}) survives Bonferroni correction over 5 comparisons.}\n\n%% ============================================================\n\\subsection{Cross-Dataset Contrast: Few-NERD}\n\\label{sec:fewnerd}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-dataset comparison of LP selection effectiveness (Qwen3-8B, $N{=}8$, $T{=}1.0$). LP selection gains are inversely associated with instance degeneracy across three datasets. Few-NERD uses gold-filtered evaluation ($n{=}32{,}565$); SciERC uses full test set ($n{=}551$) for protocol consistency.\\protect\\footnotemark}\n\\label{tab:fewnerd}\n\\begin{tabular}{lcccccc}\n\\toprule\nDataset & $n$ & Greedy & Headroom & Degen\\% & LP $\\rho$ & LP $\\Delta$ \\\\\n\\midrule\nCoNLL & 2{,}756 & .908 & 4.0\\,pp & 58\\% & .316 & fail \\\\\nSciERC & 551 & .614 & 13.8\\,pp & 21\\% & .205 & $+$0.42\\,pp \\\\\nFew-NERD & 32{,}565 & .748 & 12.4\\,pp & 10.1\\% & .421 & $\\mathbf{+1.36}$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\\footnotetext{SciERC greedy (0.614) and headroom (13.8~pp) differ from Table~\\ref{tab:selection} (gold-filtered $n{=}529$, greedy${=}0.645$) due to full-set evaluation; the ranking and significance are unchanged.}\n\nFew-NERD (Table~\\ref{tab:fewnerd}) reveals that LP selection effectiveness is inversely associated with instance degeneracy across datasets.\nAt 10.1\\% degeneracy (vs.\\ SciERC's 21\\%, CoNLL's 58\\%), LP achieves highly significant selection gains ($+1.36$~pp, 95\\% CI $[+1.18, +1.53]$, $p{<}0.001$), while all other signals degrade selection (VC $-1.79$, SJ $-2.14$, FK $-2.26$, EM $-3.85$~pp).\n\n\\paragraph{Degeneracy as a necessary condition.}\nLow degeneracy is necessary for LP selection: the cross-dataset gradient is monotonic (58\\% $\\to$ fail, 21\\% $\\to$ $+0.42$~pp, 10\\% $\\to$ $+1.36$~pp), and degeneracy below ${\\sim}$15\\% consistently enables positive LP gains (Figure~\\ref{fig:degeneracy_scatter}).\nHowever, within a dataset, LP signal quality ($\\rho$) provides an additional prerequisite: per-type analysis shows that low degeneracy alone does not guarantee gains (Appendix~\\ref{app:per_type_lp}).\nThe LoRA-rank ablation (\\S\\ref{sec:robustness_main}) corroborates this interaction: reducing rank lowers SciERC degeneracy from 21\\% to 7\\% and increases oracle headroom, though LP selection still fails there, confirming that degeneracy is necessary but not sufficient.\n\n\\paragraph{The correlation-selection gap persists for structural signals.}\nAll five signals achieve positive quality estimation on Few-NERD (LP $\\rho{=}0.42$, VC $0.39$, FK $0.31$, SJ $0.30$, EM $0.29$), yet only LP translates QE into selection.\nThe gap between VC's quality estimation ($\\rho{=}0.39$) and its selection outcome ($-1.79$~pp) confirms that the gap is not an artifact of weak QE: even strong instance-level QE signals cannot rank candidates within an instance.\nWithin Few-NERD, the degeneracy-gating pattern holds at entity-type granularity: 7 of 8 types show positive LP selection gains ($+0.23$ to $+4.73$~pp), while the highest-degeneracy type (Art, 19.8\\%) is the sole exception (Appendix~\\ref{app:per_type_lp}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n\\caption{Instance degeneracy vs.\\ LP selection gain. Blue circles: cross-dataset aggregates (CoNLL, SciERC, Few-NERD); orange triangles: per-entity-type within Few-NERD. The dashed line at ${\\sim}$15\\% separates a regime where LP selection improves over greedy (left) from one where it fails (right). Cross-dataset ordering is monotonic; 7/8 Few-NERD entity types below 20\\% degeneracy show positive gains. Degeneracy below ${\\sim}$15\\% appears necessary for LP selection to succeed (Spearman $\\rho{=}{-}0.57$, $p{=}0.066$, $n{=}11$).}\n\\label{fig:degeneracy_scatter}\n\\end{figure}\n\nFigure~\\ref{fig:degeneracy_scatter} visualizes the relationship across both dataset-level and entity-type-level granularity: degeneracy below ${\\sim}$15\\% appears necessary for LP selection gains.\nThe pooled Spearman correlation ($\\rho{=}{-}0.57$, $p{=}0.066$, $n{=}11$) treats dataset-level and entity-type-level points as independent; the entity-type-level evidence alone provides stronger grounding ($\\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$).\n\n\\paragraph{LP selection scales with sample budget in the low-degeneracy regime.}\nOn the same 4{,}351 Few-NERD instances, doubling $N$ from 8 to 16 yields a significant additional $+0.52$~pp (paired bootstrap $p{=}0.003$, 95\\% CI $[+0.17, +0.87]$): LP selection improves from $+1.37$~pp to $+1.88$~pp (both $p{<}0.001$).\nThe gain is driven by reduced degeneracy (11.1\\% $\\to$ 4.5\\%) expanding oracle headroom (12.1 $\\to$ 15.4~pp), while LP ranking quality remains stable ($\\rho{\\approx}0.62$), confirming that signal quality is model-intrinsic rather than $N$-dependent.\nAt $N{=}16$, all 8 entity types show positive LP gains, including types that were negative at $N{=}8$.\nStructural signals remain uniformly negative at $N{=}16$ (SJ $-1.36$, FK $-1.47$~pp), reinforcing that the correlation-selection gap for consensus-based methods persists regardless of sample budget.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\\Delta\\rho{=}{+}0.044$).\nSignal rankings are stable across seeds (Kendall's $W{=}1.0$ at $N{=}8$, though statistical precision is limited with $m{=}3$ raters, exact $p{\\approx}0.028$; Table~\\ref{tab:ranking-stability}).\nNER calibration is reasonable (ECE 0.069--0.096; Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: Qwen3-8B vs.\\ 4B NER quality estimation ($\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. RE scale ablation in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL & SJ & .436 & .422 & $-$.014 \\\\\n      & FK & .400 & .418 & $+$.018 \\\\\nSciERC & SJ & .360 & .422 & $+$.062 \\\\\n       & FK & .267 & .326 & $+$.059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nRepeating with Qwen3-4B (Table~\\ref{tab:scale_ablation}), quality estimation is comparable or improved (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below greedy on SciERC ($\\Delta$ up to $-3.4$~pp) despite 13.0~pp of oracle headroom, and indistinguishable on CoNLL (${<}0.3$~pp, 1.7~pp headroom). Within the 3B--8B range tested across two model families, task difficulty is a stronger predictor of the gap than model scale; results hold at smaller scale (LLaMA-3.2-3B, 13.6~pp headroom; Appendix~\\ref{app:llama3b}).\nInstance degeneracy also scales with model capability: 8B shows twice the degeneracy of 4B on SciERC (21\\% vs.\\ 10.4\\%) despite comparable within-instance utility correlation (Table~\\ref{tab:degeneracy}).\n\n\\paragraph{LoRA-rank ablation.}\nTo disentangle model capacity from degeneracy, we train Qwen3-8B on SciERC with LoRA rank${=}8$ (vs.\\ rank${=}32$ in all other experiments).\nReducing rank lowers degeneracy from 21\\% to 7.2\\% and increases oracle headroom from 13.3~pp to 16.0~pp, confirming that fine-tuning capacity drives output convergence.\nHowever, selection still fails: the best signal (LP, 0.635) falls short of greedy (0.640), and all consensus-proximity signals perform worse (SJ 0.631, VC 0.592).\nQuality estimation remains comparable (VC $\\rho{=}0.394$ vs.\\ $0.379$; SJ $\\rho{=}0.365$ vs.\\ $0.360$).\nLow degeneracy is thus a necessary but not sufficient condition for selection---LP compression persists regardless of LoRA rank, indicating that both mechanisms must be addressed simultaneously.\n\n\\paragraph{Supervised verifier baseline.}\nTo test whether the information bottleneck lies in the aggregation method or the features themselves, we train a logistic regression verifier on all five signals (3-fold cross-validation on SciERC, $N{=}16$---giving the verifier access to twice as many samples as the main results).\nThe supervised selector achieves F1${=}0.641$, below both LP (0.647) and greedy (0.644),\\footnote{Greedy F1 is 0.644 (3-seed mean in the verifier experiment), consistent with Table~\\ref{tab:selection} (0.645, 2-seed mean on the gold-filtered subset).} closing none of the oracle gap despite the additional samples.\nIts AUROC (0.652) is lower than single-signal VC (0.706), and feature importance is dominated by VC (coefficient 0.65--0.92) with SJ receiving a negative coefficient.\nA 2-layer MLP and random forest on the same five features achieve comparable or slightly worse performance (MLP AUROC: 0.639; RF: 0.604), confirming that the bottleneck lies in the feature space rather than the aggregation model.\nThe failure of supervised signal combination confirms that the bottleneck is not in how signals are aggregated but in what information they encode: these features lack per-sample discriminative content sufficient for selection.\n",
      "numLines": 216,
      "startLine": 1,
      "totalLines": 216
    }
  },
  "sourceToolAssistantUUID": "e283346a-ed55-4eeb-9e48-83d8708c82a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-17T07:08:28.104Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RxN3UCiusjA8e6XPkUQJr5`</summary>

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
  "parentUuid": "a49915f8-8259-4328-820e-aed538519d86",
  "isSidechain": false,
  "requestId": "req_011Cb7ijN1G7omSJC4hPXf1V",
  "type": "assistant",
  "uuid": "7cbb10b8-628d-46e6-b371-e9c368056559",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4634eS47gVibKkuxBhDj1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2840,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 29243,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1411,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2840,
          "output_tokens": 315,
          "cache_read_input_tokens": 29243,
          "cache_creation_input_tokens": 1411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1411
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-17T07:08:28.184Z_

```json
{
  "parentUuid": "d4e201bc-647b-4d9c-901d-218890656f4b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "58389f71-254d-43dd-a431-c78e3b7c3010",
  "timestamp": "2026-05-17T07:08:28.184Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性 + 写作质量**  ### Venue 信息 - 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - 截止日期: 2026-05-25 - 页数限制: 长文 8 页正文（Limitations/Ethics…",
  "leafUuid": "58389f71-254d-43dd-a431-c78e3b7c3010",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper for EMNLP 2026",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Tool call

_source line 34 · 2026-05-17T07:08:32.858Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KTH5Mk1bqXKQyxWGgwLbQ8`</summary>

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
  "parentUuid": "58389f71-254d-43dd-a431-c78e3b7c3010",
  "isSidechain": false,
  "requestId": "req_011Cb7ijkGi6eJXw9ZKvno4g",
  "type": "assistant",
  "uuid": "a1a009c1-eaa0-4c22-b900-0c3536331e2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013cYdvUGr4WTR7i6mSHvtZb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19737,
      "cache_read_input_tokens": 30654,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19737,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 30654,
          "cache_creation_input_tokens": 19737,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19737
          },
          "type": "message"
        }
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

_source line 35 · 2026-05-17T07:08:32.863Z_

<details><summary>↩ Tool result · `toolu_01KTH5Mk1bqXKQyxWGgwLbQ8`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER across four benchmarks spanning a difficulty gradient.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82), supporting selective prediction and error flagging.
5	However, quality estimation does not translate to sample selection, and the gap has a three-layer structure: four instance-level signals cannot rank candidates by construction; MBR selection with well-aligned utility ($\rho{=}0.52$) fails because instance degeneracy (10--58\%) collapses the candidate pool; and LP, the sole per-sample signal, is compressed to near-ineffectiveness (median range 0.041 nats).
6	LP selection effectiveness is inversely associated with instance degeneracy: at 10\% (Few-NERD), LP achieves $+1.36$~pp ($p{<}0.001$); at 21\% (SciERC), $+0.42$~pp ($p{=}0.091$); at 58\% (CoNLL), LP fails.
7	In the low-degeneracy regime, LP selection scales with sample budget ($+0.52$~pp from $N{=}8$ to 16, paired $p{=}0.003$).
8	Structural signals fail uniformly regardless of degeneracy, and supervised combination of all five signals cannot close the oracle gap, confirming the bottleneck is in the feature space.
9	Whether these patterns persist at 70B+ scales remains open.
10	Closing the gap for structural signals requires content-aware verifiers that examine output semantics \cite{cobbe2021verifiers}; LP provides a lightweight baseline when degeneracy is low.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1a009c1-eaa0-4c22-b900-0c3536331e2f",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "60cb44c2-1ca9-4608-b5ce-b135545477a2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluate five confidence signals for quality estimation and sample selection in LLM-based NER across four benchmarks spanning a difficulty gradient.\nAll signals achieve reliable quality estimation ($\\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82), supporting selective prediction and error flagging.\nHowever, quality estimation does not translate to sample selection, and the gap has a three-layer structure: four instance-level signals cannot rank candidates by construction; MBR selection with well-aligned utility ($\\rho{=}0.52$) fails because instance degeneracy (10--58\\%) collapses the candidate pool; and LP, the sole per-sample signal, is compressed to near-ineffectiveness (median range 0.041 nats).\nLP selection effectiveness is inversely associated with instance degeneracy: at 10\\% (Few-NERD), LP achieves $+1.36$~pp ($p{<}0.001$); at 21\\% (SciERC), $+0.42$~pp ($p{=}0.091$); at 58\\% (CoNLL), LP fails.\nIn the low-degeneracy regime, LP selection scales with sample budget ($+0.52$~pp from $N{=}8$ to 16, paired $p{=}0.003$).\nStructural signals fail uniformly regardless of degeneracy, and supervised combination of all five signals cannot close the oracle gap, confirming the bottleneck is in the feature space.\nWhether these patterns persist at 70B+ scales remains open.\nClosing the gap for structural signals requires content-aware verifiers that examine output semantics \\cite{cobbe2021verifiers}; LP provides a lightweight baseline when degeneracy is low.\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  },
  "sourceToolAssistantUUID": "a1a009c1-eaa0-4c22-b900-0c3536331e2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-17T07:08:33.276Z_

<details open><summary>🔧 Tool call — Read · `toolu_0111SeWvEbwKAcFS7UGwVKfZ`</summary>

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
  "parentUuid": "60cb44c2-1ca9-4608-b5ce-b135545477a2",
  "isSidechain": false,
  "requestId": "req_011Cb7ijkGi6eJXw9ZKvno4g",
  "type": "assistant",
  "uuid": "1e661e90-c8ad-483b-ba3f-fd2757b6072e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013cYdvUGr4WTR7i6mSHvtZb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19737,
      "cache_read_input_tokens": 30654,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19737,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 30654,
          "cache_creation_input_tokens": 19737,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19737
          },
          "type": "message"
        }
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

_source line 37 · 2026-05-17T07:08:34.532Z_

<details><summary>↩ Tool result · reported error · `toolu_01QRjF3QqMbqU5StTUffvuhR`</summary>

```text
File content (30903 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c3787dd-83e7-4e06-8a3b-67c16e3109f5",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "64754ee3-1bcc-439c-81d3-6729f25b2b73",
  "toolUseResult": "Error: File content (30903 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "90ba364f-3bc9-4469-88b8-14cd938b8d97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T07:08:33.280Z_

<details><summary>↩ Tool result · `toolu_0111SeWvEbwKAcFS7UGwVKfZ`</summary>

```text
1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
12	We tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selection despite increasing within-instance variance on SciERC ($4{\times}$); LP${\times}$VC combinations also fail to recover selection (\S\ref{sec:discussion}); calibration-based approaches remain unexplored.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e661e90-c8ad-483b-ba3f-fd2757b6072e",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "389933bf-9aa0-4a36-a39a-f6daf51e39da",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.\nWe cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.\nWe do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\\ref{app:n_scaling}).\nThe free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\\ref{app:re_extension}.\nQwen3-8B's SciERC checkpoint used empty \\texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\\ref{app:thinking_token}).\nLP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.\nWe tested verbalized confidence \\cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\\ref{app:verbalized_confidence}).\nAd-hoc LP${\\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \\S\\ref{sec:discussion}); whether \\textit{learned} combinations could close the gap remains open.\nThe $\\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\\varepsilon \\in [0, 0.2]$ (Appendix~\\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.\nWe tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selection despite increasing within-instance variance on SciERC ($4{\\times}$); LP${\\times}$VC combinations also fail to recover selection (\\S\\ref{sec:discussion}); calibration-based approaches remain unexplored.\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  },
  "sourceToolAssistantUUID": "1e661e90-c8ad-483b-ba3f-fd2757b6072e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T07:08:34.291Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QRjF3QqMbqU5StTUffvuhR`</summary>

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
  "parentUuid": "389933bf-9aa0-4a36-a39a-f6daf51e39da",
  "isSidechain": false,
  "requestId": "req_011Cb7ijkGi6eJXw9ZKvno4g",
  "type": "assistant",
  "uuid": "90ba364f-3bc9-4469-88b8-14cd938b8d97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013cYdvUGr4WTR7i6mSHvtZb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19737,
      "cache_read_input_tokens": 30654,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19737,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 30654,
          "cache_creation_input_tokens": 19737,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19737
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-17T07:08:34.462Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Pv2J7B5ykCgSGkZDcvcACz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90ba364f-3bc9-4469-88b8-14cd938b8d97",
  "isSidechain": false,
  "requestId": "req_011Cb7ijkGi6eJXw9ZKvno4g",
  "type": "assistant",
  "uuid": "4c3787dd-83e7-4e06-8a3b-67c16e3109f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013cYdvUGr4WTR7i6mSHvtZb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19737,
      "cache_read_input_tokens": 30654,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19737,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 30654,
          "cache_creation_input_tokens": 19737,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19737
          },
          "type": "message"
        }
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

_source line 41 · 2026-05-17T07:08:34.467Z_

<details><summary>↩ Tool result · `toolu_01Pv2J7B5ykCgSGkZDcvcACz`</summary>

```text
1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@article{brown2024monkeys,
4	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
5	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
6	  journal = {arXiv preprint arXiv:2407.21787},
7	  year = {2024},
8	  url = {https://arxiv.org/abs/2407.21787}
9	}
10	
11	@inproceedings{chen2024usc,
12	  title = {Universal Self-Consistency for Large Language Model Generation},
13	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
14	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2311.17311}
17	}
18	
19	@article{cobbe2021verifiers,
20	  title = {Training Verifiers to Solve Math Word Problems},
21	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
22	  journal = {arXiv preprint arXiv:2110.14168},
23	  year = {2021},
24	  url = {https://arxiv.org/abs/2110.14168}
25	}
26	
27	@inproceedings{culotta2004confidence,
28	  title = {Confidence Estimation for Information Extraction},
29	  author = {Culotta, Aron and McCallum, Andrew},
30	  booktitle = {HLT-NAACL 2004},
31	  year = {2004},
32	  url = {https://aclanthology.org/N04-4028/}
33	}
34	
35	@inproceedings{derczynski2017wnut,
36	  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},
37	  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},
38	  booktitle = {W-NUT Workshop at EMNLP 2017},
39	  year = {2017},
40	  url = {https://aclanthology.org/W17-4418/}
41	}
42	
43	@inproceedings{ding2021fewnerd,
44	  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},
45	  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},
46	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},
47	  pages = {3198--3213},
48	  year = {2021},
49	  doi = {10.18653/v1/2021.acl-long.248}
50	}
51	
52	@inproceedings{eikema2022sampling,
53	  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},
54	  author = {Eikema, Bryan and Aziz, Wilker},
55	  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
56	  year = {2022},
57	  pages = {10978--10993},
58	  doi = {10.18653/v1/2022.emnlp-main.754}
59	}
60	
61	@article{freitag2022high,
62	  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},
63	  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},
64	  journal = {Transactions of the Association for Computational Linguistics},
65	  volume = {10},
66	  year = {2022},
67	  pages = {811--825},
68	  doi = {10.1162/tacl_a_00491}
69	}
70	
71	@article{fleiss1971agreement,
72	  title = {Measuring nominal scale agreement among many raters.},
73	  author = {Fleiss, Joseph L.},
74	  journal = {Psychological Bulletin},
75	  year = {1971},
76	  doi = {10.1037/h0031619},
77	  url = {http://dx.doi.org/10.1037/h0031619}
78	}
79	
80	@article{feng2025optimal,
81	  title = {Optimal Self-Consistency for Efficient Reasoning with Large Language Models},
82	  author = {Feng, Austin and Alonso, Marius and Odonnat, Ambroise},
83	  journal = {arXiv preprint arXiv:2511.12309},
84	  year = {2025},
85	  url = {https://arxiv.org/abs/2511.12309}
86	}
87	
88	@inproceedings{geng2024confidence,
89	  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},
90	  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},
91	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
92	  year = {2024},
93	  doi = {10.18653/v1/2024.naacl-long.366},
94	  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}
95	}
96	
97	@article{hobelsberger2025systematic,
98	  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},
99	  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},
100	  journal = {arXiv preprint arXiv:2510.20460},
101	  year = {2025},
102	  url = {https://arxiv.org/abs/2510.20460}
103	}
104	
105	@article{kadavath2022language,
106	  title = {Language Models (Mostly) Know What They Know},
107	  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},
108	  journal = {arXiv preprint arXiv:2207.05221},
109	  year = {2022},
110	  url = {https://arxiv.org/abs/2207.05221}
111	}
112	
113	@inproceedings{kang2025selfcertainty,
114	  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},
115	  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},
116	  booktitle = {NeurIPS 2025},
117	  year = {2025},
118	  url = {https://arxiv.org/abs/2502.18581}
119	}
120	
121	@inproceedings{kim2026reasc,
122	  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},
123	  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},
124	  booktitle = {ACL 2026},
125	  year = {2026},
126	  url = {https://arxiv.org/abs/2601.02970}
127	}
128	
129	@article{li2025llms,
130	  title = {LLMs Can Generate a Better Answer by Aggregating Their Own Responses},
131	  author = {Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi and Liang, Chen and Chen, Weizhu and Wang, Haoyu and Zhao, Tuo},
132	  journal = {arXiv preprint arXiv:2503.04104},
133	  year = {2025},
134	  url = {https://arxiv.org/abs/2503.04104}
135	}
136	
137	@inproceedings{kuhn2023semantic,
138	  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},
139	  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},
140	  booktitle = {ICLR 2023},
141	  year = {2023},
142	  url = {https://arxiv.org/abs/2302.09664}
143	}
144	
145	@inproceedings{malinin2021uncertainty,
146	  title = {Uncertainty Estimation in Autoregressive Structured Prediction},
147	  author = {Malinin, Andrey and Gales, Mark},
148	  booktitle = {International Conference on Learning Representations},
149	  year = {2021},
150	  url = {https://openreview.net/forum?id=jN5y-zb5Q7m}
151	}
152	
153	@inproceedings{li2023codeie,
154	  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
155	  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
156	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},
157	  year = {2023},
158	  doi = {10.18653/v1/2023.acl-long.855},
159	  url = {https://arxiv.org/abs/2305.05711}
160	}
161	
162	@inproceedings{lightman2024verify,
163	  title = {Let's Verify Step by Step},
164	  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
165	  booktitle = {ICLR 2024},
166	  year = {2024},
167	  url = {https://arxiv.org/abs/2305.20050}
168	}
169	
170	@inproceedings{luan2018scierc,
171	  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
172	  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
173	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
174	  year = {2018},
175	  doi = {10.18653/v1/D18-1360},
176	  url = {http://dx.doi.org/10.18653/v1/D18-1360}
177	}
178	
179	@inproceedings{manakul2023selfcheckgpt,
180	  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},
181	  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},
182	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
183	  year = {2023},
184	  doi = {10.18653/v1/2023.emnlp-main.557},
185	  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}
186	}
187	
188	@article{yao2026consistency,
189	  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},
190	  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},
191	  journal = {Genomics \& Informatics},
192	  year = {2026},
193	  doi = {10.1186/s44342-025-00063-2},
194	  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}
195	}
196	
197	@article{oh2026latentsc,
198	  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},
199	  author = {Oh, Jungsuk and Lee, Jay-Yoon},
200	  journal = {arXiv preprint arXiv:2508.18395},
201	  year = {2026},
202	  url = {https://arxiv.org/abs/2508.18395}
203	}
204	
205	@inproceedings{sainz2024gollie,
206	  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
207	  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},
208	  booktitle = {ICLR 2024},
209	  year = {2024},
210	  url = {https://arxiv.org/abs/2310.03668}
211	}
212	
213	@inproceedings{snell2025scaling,
214	  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},
215	  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
216	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
217	  year = {2025},
218	  url = {https://arxiv.org/abs/2408.03314}
219	}
220	
221	@inproceedings{taubenfeld2025cisc,
222	  title = {Confidence Improves Self-Consistency in LLMs},
223	  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},
224	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
225	  year = {2025},
226	  doi = {10.18653/v1/2025.findings-acl.1030},
227	  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}
228	}
229	
230	@inproceedings{thirukovalluru2024atomic,
231	  title = {Atomic Self-Consistency for Better Long Form Generations},
232	  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},
233	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
234	  year = {2024},
235	  doi = {10.18653/v1/2024.emnlp-main.706},
236	  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}
237	}
238	
239	@inproceedings{tjongkimsang2003conll,
240	  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},
241	  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},
242	  booktitle = {CoNLL 2003},
243	  year = {2003},
244	  url = {https://aclanthology.org/W03-0419/}
245	}
246	
247	@inproceedings{vashurin2025cocoa,
248	  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},
249	  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},
250	  booktitle = {NeurIPS 2025},
251	  year = {2025},
252	  url = {https://arxiv.org/abs/2502.04964}
253	}
254	
255	@inproceedings{wadhwa2023revisiting,
256	  title = {Revisiting Relation Extraction in the era of Large Language Models},
257	  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},
258	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
259	  year = {2023},
260	  doi = {10.18653/v1/2023.acl-long.868},
261	  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}
262	}
263	
264	@inproceedings{wang2023selfconsistency,
265	  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},
266	  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
267	  booktitle = {ICLR 2023},
268	  year = {2023},
269	  url = {https://arxiv.org/abs/2203.11171}
270	}
271	
272	@inproceedings{wang2025make,
273	  title = {Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning},
274	  author = {Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueqi and Tan, Chuyi and Pan, Boyuan and Hu, Yao and Li, Kan},
275	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
276	  pages = {6919--6932},
277	  year = {2025}
278	}
279	
280	@inproceedings{wang2025rankedvoting,
281	  title = {Ranked Voting based Self-Consistency of Large Language Models},
282	  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},
283	  booktitle = {ACL Findings 2025},
284	  year = {2025},
285	  url = {https://arxiv.org/abs/2505.10772}
286	}
287	
288	@article{willard2023guided,
289	  title = {Efficient Guided Generation for Large Language Models},
290	  author = {Willard, Brandon T. and Louf, Rémi},
291	  journal = {arXiv preprint arXiv:2307.09702},
292	  year = {2023},
293	  url = {https://arxiv.org/abs/2307.09702}
294	}
295	
296	@inproceedings{xia2025survey,
297	  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},
298	  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},
299	  booktitle = {ACL Findings 2025},
300	  year = {2025},
301	  url = {https://aclanthology.org/2025.findings-acl.1101/}
302	}
303	
304	@inproceedings{zheng2024llamafactory,
305	  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},
306	  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},
307	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},
308	  year = {2024},
309	  pages = {400--410},
310	  doi = {10.18653/v1/2024.acl-demos.38}
311	}
312	
313	@inproceedings{zhou2024uniner,
314	  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
315	  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
316	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
317	  year = {2024},
318	  url = {https://arxiv.org/abs/2308.03279}
319	}
320	
321	@inproceedings{muller2021understanding,
322	  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},
323	  author = {M{\"u}ller, Mathias and Sennrich, Rico},
324	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
325	  year = {2021},
326	  url = {https://arxiv.org/abs/2105.08504}
327	}
328	
329	@inproceedings{eikema2025structured,
330	  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},
331	  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},
332	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
333	  year = {2025},
334	  url = {https://arxiv.org/abs/2510.20700}
335	}
336	
337	@article{venktesh2025trust,
338	  title = {Trust but Verify! A Survey on Verification Design for Test-time Scaling},
339	  author = {Venktesh, V and Rathee, Mandeep and Anand, Avishek},
340	  journal = {arXiv preprint arXiv:2508.16665},
341	  year = {2025},
342	  url = {https://arxiv.org/abs/2508.16665}
343	}
344	
345	@inproceedings{jinnai2024mbr,
346	  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},
347	  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},
348	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
349	  year = {2024},
350	  url = {https://arxiv.org/abs/2311.05263}
351	}
352	
353	@inproceedings{ratinov2009design,
354	  title = {Design Challenges and Misconceptions in Named Entity Recognition},
355	  author = {Ratinov, Lev and Roth, Dan},
356	  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},
357	  year = {2009},
358	  pages = {147--155},
359	  publisher = {Association for Computational Linguistics}
360	}
361	
362	@inproceedings{bergkirkpatrick2012empirical,
363	  title = {An Empirical Investigation of Statistical Significance in {NLP}},
364	  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},
365	  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},
366	  year = {2012},
367	  pages = {995--1005},
368	  publisher = {Association for Computational Linguistics}
369	}
370	
371	@inproceedings{tian2023calibration,
372	  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models},
373	  author = {Tian, Katherine and Mitchell, Eric and Yao, Huaxiu and Manning, Christopher D. and Finn, Chelsea},
374	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
375	  year = {2023},
376	  pages = {1278--1294},
377	  publisher = {Association for Computational Linguistics}
378	}
379	
380	@inproceedings{fernandes2022quality,
381	  title = {Quality-Aware Decoding for Neural Machine Translation},
382	  author = {Fernandes, Patrick and Farinhas, Ant{\'o}nio and Rei, Ricardo and de Souza, Jos{\'e} G. C. and Ogayo, Perez and Neubig, Graham and Martins, Andr{\'e}},
383	  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
384	  year = {2022},
385	  pages = {1396--1412},
386	  url = {https://arxiv.org/abs/2205.00978}
387	}
388	
389	@inproceedings{zhang2025conformal,
390	  title = {Conformal Structured Prediction},
391	  author = {Zhang, Botong and Li, Shuo and Bastani, Osbert},
392	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
393	  year = {2025},
394	  url = {https://arxiv.org/abs/2410.06296}
395	}
396	
397	@article{bhattacharyya2026beyond,
398	  title = {Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in {LLMs}},
399	  author = {Bhattacharyya, Sree and Khanna, Samarth and Chen, Leona and Craig, Lucas and Dilliraj, Tharun and Wang, James Z.},
400	  journal = {arXiv preprint arXiv:2605.07806},
401	  year = {2026},
402	  url = {https://arxiv.org/abs/2605.07806}
403	}
404	
405	@inproceedings{deguchi2024centroid,
406	  title = {Centroid-Based Efficient Minimum Bayes Risk Decoding},
407	  author = {Deguchi, Hiroyuki and Kamigaito, Hidetaka and Watanabe, Taro},
408	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
409	  year = {2024},
410	  url = {https://arxiv.org/abs/2402.11197}
411	}
412	
413	@inproceedings{mejer2010confidence,
414	  title = {Confidence in Structured-Prediction Using Confidence-Weighted Models},
415	  author = {Mejer, Avihai and Crammer, Koby},
416	  booktitle = {Proceedings of the 2010 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
417	  year = {2010},
418	  pages = {971--981},
419	  url = {https://aclanthology.org/D10-1095/}
420	}
421	
422	@inproceedings{xie2024selfevaluation,
423	  title = {Self-Evaluation Improves Selective Generation in Large Language Models},
424	  author = {Xie, Jie and Lu, Kai and Dong, Rui and Pan, Liangming and Han, Qi and Wang, Shasha and Huang, Deyu and Zhang, Junlan},
425	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
426	  year = {2024},
427	  url = {https://arxiv.org/abs/2312.09300}
428	}
429	
430	@inproceedings{schall2025hidden,
431	  title = {The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance},
432	  author = {Schall, Maximilian and de Melo, Gerard},
433	  booktitle = {Proceedings of Recent Advances in Natural Language Processing (RANLP)},
434	  year = {2025},
435	  pages = {1074--1084},
436	  url = {https://aclanthology.org/2025.ranlp-1.124/}
437	}
438	
439	@inproceedings{yun2025price,
440	  title = {The Price of Format: Diversity Collapse in {LLMs}},
441	  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},
442	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},
443	  year = {2025},
444	  url = {https://aclanthology.org/2025.findings-emnlp.836/}
445	}
446	
447	@inproceedings{park2024grammar,
448	  title = {Grammar-Aligned Decoding},
449	  author = {Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadia and D'Antoni, Loris},
450	  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},
451	  year = {2024},
452	  url = {https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html}
453	}
454	
455	@inproceedings{gao2023scaling,
456	  title = {Scaling Laws for Reward Model Overoptimization},
457	  author = {Gao, Leo and Schulman, John and Hilton, Jacob},
458	  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},
459	  year = {2023},
460	  url = {https://proceedings.mlr.press/v202/gao23h.html}
461	}
462	
463	@inproceedings{kirk2024understanding,
464	  title = {Understanding the Effects of {RLHF} on {LLM} Generalisation and Diversity},
465	  author = {Kirk, Robert and Mediratta, Ishita and Nalmpantis, Christoforos and Luketina, Jelena and Hambro, Eric and Grefenstette, Edward and Raileanu, Roberta},
466	  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},
467	  year = {2024},
468	  url = {https://openreview.net/forum?id=PXoFut3dWW}
469	}
470	
471	@inproceedings{holtzman2020curious,
472	  title = {The Curious Case of Neural Text Degeneration},
473	  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
474	  booktitle = {Proceedings of the Eighth International Conference on Learning Representations (ICLR)},
475	  year = {2020},
476	  url = {https://openreview.net/forum?id=rygGQyrFvH}
477	}
478	
479	@inproceedings{kuleshov2015calibrated,
480	  title = {Calibrated Structured Prediction},
481	  author = {Kuleshov, Volodymyr and Liang, Percy},
482	  booktitle = {Advances in Neural Information Processing Systems 28 (NeurIPS)},
483	  year = {2015},
484	  url = {https://proceedings.neurips.cc/paper/2015/hash/b3b4d2dbedc99fe843fd3dedb02f086f-Abstract.html}
485	}
486	
487	@article{fomicheva2020unsupervised,
488	  title = {Unsupervised Quality Estimation for Neural Machine Translation},
489	  author = {Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Fr{\'e}d{\'e}ric and Guzm{\'a}n, Francisco and Fishel, Mark and Aletras, Nikolaos and Chaudhary, Vishrav and Specia, Lucia},
490	  journal = {Transactions of the Association for Computational Linguistics},
491	  volume = {8},
492	  pages = {539--555},
493	  year = {2020},
494	  doi = {10.1162/tacl_a_00330}
495	}
496	
497	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c3787dd-83e7-4e06-8a3b-67c16e3109f5",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "965ff29d-218e-4bc6-b55c-f49b289f6357",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{culotta2004confidence,\n  title = {Confidence Estimation for Information Extraction},\n  author = {Culotta, Aron and McCallum, Andrew},\n  booktitle = {HLT-NAACL 2004},\n  year = {2004},\n  url = {https://aclanthology.org/N04-4028/}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {W-NUT Workshop at EMNLP 2017},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@article{feng2025optimal,\n  title = {Optimal Self-Consistency for Efficient Reasoning with Large Language Models},\n  author = {Feng, Austin and Alonso, Marius and Odonnat, Ambroise},\n  journal = {arXiv preprint arXiv:2511.12309},\n  year = {2025},\n  url = {https://arxiv.org/abs/2511.12309}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n@article{hobelsberger2025systematic,\n  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},\n  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},\n  journal = {arXiv preprint arXiv:2510.20460},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20460}\n}\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kim2026reasc,\n  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},\n  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},\n  booktitle = {ACL 2026},\n  year = {2026},\n  url = {https://arxiv.org/abs/2601.02970}\n}\n\n@article{li2025llms,\n  title = {LLMs Can Generate a Better Answer by Aggregating Their Own Responses},\n  author = {Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi and Liang, Chen and Chen, Weizhu and Wang, Haoyu and Zhao, Tuo},\n  journal = {arXiv preprint arXiv:2503.04104},\n  year = {2025},\n  url = {https://arxiv.org/abs/2503.04104}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {International Conference on Learning Representations},\n  year = {2021},\n  url = {https://openreview.net/forum?id=jN5y-zb5Q7m}\n}\n\n@inproceedings{li2023codeie,\n  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.855},\n  url = {https://arxiv.org/abs/2305.05711}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@article{oh2026latentsc,\n  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},\n  author = {Oh, Jungsuk and Lee, Jay-Yoon},\n  journal = {arXiv preprint arXiv:2508.18395},\n  year = {2026},\n  url = {https://arxiv.org/abs/2508.18395}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {CoNLL 2003},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{vashurin2025cocoa,\n  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},\n  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.04964}\n}\n\n@inproceedings{wadhwa2023revisiting,\n  title = {Revisiting Relation Extraction in the era of Large Language Models},\n  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.868},\n  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@inproceedings{wang2025make,\n  title = {Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning},\n  author = {Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueqi and Tan, Chuyi and Pan, Boyuan and Hu, Yao and Li, Kan},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},\n  pages = {6919--6932},\n  year = {2025}\n}\n\n@inproceedings{wang2025rankedvoting,\n  title = {Ranked Voting based Self-Consistency of Large Language Models},\n  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.10772}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@article{venktesh2025trust,\n  title = {Trust but Verify! A Survey on Verification Design for Test-time Scaling},\n  author = {Venktesh, V and Rathee, Mandeep and Anand, Avishek},\n  journal = {arXiv preprint arXiv:2508.16665},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.16665}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models},\n  author = {Tian, Katherine and Mitchell, Eric and Yao, Huaxiu and Manning, Christopher D. and Finn, Chelsea},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {1278--1294},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{fernandes2022quality,\n  title = {Quality-Aware Decoding for Neural Machine Translation},\n  author = {Fernandes, Patrick and Farinhas, Ant{\\'o}nio and Rei, Ricardo and de Souza, Jos{\\'e} G. C. and Ogayo, Perez and Neubig, Graham and Martins, Andr{\\'e}},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  year = {2022},\n  pages = {1396--1412},\n  url = {https://arxiv.org/abs/2205.00978}\n}\n\n@inproceedings{zhang2025conformal,\n  title = {Conformal Structured Prediction},\n  author = {Zhang, Botong and Li, Shuo and Bastani, Osbert},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2410.06296}\n}\n\n@article{bhattacharyya2026beyond,\n  title = {Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in {LLMs}},\n  author = {Bhattacharyya, Sree and Khanna, Samarth and Chen, Leona and Craig, Lucas and Dilliraj, Tharun and Wang, James Z.},\n  journal = {arXiv preprint arXiv:2605.07806},\n  year = {2026},\n  url = {https://arxiv.org/abs/2605.07806}\n}\n\n@inproceedings{deguchi2024centroid,\n  title = {Centroid-Based Efficient Minimum Bayes Risk Decoding},\n  author = {Deguchi, Hiroyuki and Kamigaito, Hidetaka and Watanabe, Taro},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.11197}\n}\n\n@inproceedings{mejer2010confidence,\n  title = {Confidence in Structured-Prediction Using Confidence-Weighted Models},\n  author = {Mejer, Avihai and Crammer, Koby},\n  booktitle = {Proceedings of the 2010 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2010},\n  pages = {971--981},\n  url = {https://aclanthology.org/D10-1095/}\n}\n\n@inproceedings{xie2024selfevaluation,\n  title = {Self-Evaluation Improves Selective Generation in Large Language Models},\n  author = {Xie, Jie and Lu, Kai and Dong, Rui and Pan, Liangming and Han, Qi and Wang, Shasha and Huang, Deyu and Zhang, Junlan},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2312.09300}\n}\n\n@inproceedings{schall2025hidden,\n  title = {The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance},\n  author = {Schall, Maximilian and de Melo, Gerard},\n  booktitle = {Proceedings of Recent Advances in Natural Language Processing (RANLP)},\n  year = {2025},\n  pages = {1074--1084},\n  url = {https://aclanthology.org/2025.ranlp-1.124/}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{park2024grammar,\n  title = {Grammar-Aligned Decoding},\n  author = {Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadia and D'Antoni, Loris},\n  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},\n  year = {2024},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n@inproceedings{kirk2024understanding,\n  title = {Understanding the Effects of {RLHF} on {LLM} Generalisation and Diversity},\n  author = {Kirk, Robert and Mediratta, Ishita and Nalmpantis, Christoforos and Luketina, Jelena and Hambro, Eric and Grefenstette, Edward and Raileanu, Roberta},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=PXoFut3dWW}\n}\n\n@inproceedings{holtzman2020curious,\n  title = {The Curious Case of Neural Text Degeneration},\n  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  booktitle = {Proceedings of the Eighth International Conference on Learning Representations (ICLR)},\n  year = {2020},\n  url = {https://openreview.net/forum?id=rygGQyrFvH}\n}\n\n@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems 28 (NeurIPS)},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/b3b4d2dbedc99fe843fd3dedb02f086f-Abstract.html}\n}\n\n@article{fomicheva2020unsupervised,\n  title = {Unsupervised Quality Estimation for Neural Machine Translation},\n  author = {Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Fr{\\'e}d{\\'e}ric and Guzm{\\'a}n, Francisco and Fishel, Mark and Aletras, Nikolaos and Chaudhary, Vishrav and Specia, Lucia},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {8},\n  pages = {539--555},\n  year = {2020},\n  doi = {10.1162/tacl_a_00330}\n}\n\n",
      "numLines": 497,
      "startLine": 1,
      "totalLines": 497
    }
  },
  "sourceToolAssistantUUID": "4c3787dd-83e7-4e06-8a3b-67c16e3109f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性 + 写作质量**  ### Venue 信息 - 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - 截止日期: 2026-05-25 - 页数限制: 长文 8 页正文（Limitations/Ethics…",
  "leafUuid": "64754ee3-1bcc-439c-81d3-6729f25b2b73",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper for EMNLP 2026",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Assistant

_source line 44 · 2026-05-17T07:08:38.082Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also fetch the ARR review form and check for AI writing markers in the paper. Let me also read the appendix in parts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "965ff29d-218e-4bc6-b55c-f49b289f6357",
  "isSidechain": false,
  "requestId": "req_011Cb7ikDd1YKP4BPbWEGizJ",
  "type": "assistant",
  "uuid": "e8258fca-59a2-42cf-b47e-63c879c1250f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HBHeLhVZ9p4nv7YWZmabz5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10974,
      "cache_read_input_tokens": 50391,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 50391,
          "cache_creation_input_tokens": 10974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10974
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-17T07:08:38.650Z_

Now let me fetch the official ARR review form and check AI writing markers in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8258fca-59a2-42cf-b47e-63c879c1250f",
  "isSidechain": false,
  "requestId": "req_011Cb7ikDd1YKP4BPbWEGizJ",
  "type": "assistant",
  "uuid": "46953a69-82f0-43e2-ad53-7626c6e557e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HBHeLhVZ9p4nv7YWZmabz5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10974,
      "cache_read_input_tokens": 50391,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 50391,
          "cache_creation_input_tokens": 10974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10974
          },
          "type": "message"
        }
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

_source line 46 · 2026-05-17T07:08:39.612Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016eGP4J2PeEX3d6ESdxj95k`</summary>

```json
{
  "query": "ACL Rolling Review review form scoring criteria \"overall assessment\" 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46953a69-82f0-43e2-ad53-7626c6e557e1",
  "isSidechain": false,
  "requestId": "req_011Cb7ikDd1YKP4BPbWEGizJ",
  "type": "assistant",
  "uuid": "3bc012b9-a01b-4a4c-80b7-b4921c6bf80c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HBHeLhVZ9p4nv7YWZmabz5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10974,
      "cache_read_input_tokens": 50391,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 50391,
          "cache_creation_input_tokens": 10974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10974
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-17T07:08:42.852Z_

<details><summary>↩ Tool result · `toolu_017psi3wCBRFuSFpRnmUGLvK`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32e592e1-f139-4d4c-b949-2e8f5ebf1d92",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "49008e40-f557-48d7-a039-4aea599cced6",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "32e592e1-f139-4d4c-b949-2e8f5ebf1d92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-17T07:08:42.117Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01AZmoAHf63FxKiMdsKZQwD3`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bc012b9-a01b-4a4c-80b7-b4921c6bf80c",
  "isSidechain": false,
  "requestId": "req_011Cb7ikDd1YKP4BPbWEGizJ",
  "type": "assistant",
  "uuid": "ab4a0839-e8b1-4ef1-8a8b-f3f80960eae2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HBHeLhVZ9p4nv7YWZmabz5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10974,
      "cache_read_input_tokens": 50391,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 50391,
          "cache_creation_input_tokens": 10974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10974
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-17T07:08:42.134Z_

<details><summary>↩ Tool result · `toolu_01AZmoAHf63FxKiMdsKZQwD3`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab4a0839-e8b1-4ef1-8a8b-f3f80960eae2",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "8a4417d7-e67d-4851-a077-eedd86d3e008",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "ab4a0839-e8b1-4ef1-8a8b-f3f80960eae2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-17T07:08:42.839Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017psi3wCBRFuSFpRnmUGLvK`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a4417d7-e67d-4851-a077-eedd86d3e008",
  "isSidechain": false,
  "requestId": "req_011Cb7ikDd1YKP4BPbWEGizJ",
  "type": "assistant",
  "uuid": "32e592e1-f139-4d4c-b949-2e8f5ebf1d92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HBHeLhVZ9p4nv7YWZmabz5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10974,
      "cache_read_input_tokens": 50391,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 50391,
          "cache_creation_input_tokens": 10974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10974
          },
          "type": "message"
        }
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

_source line 51 · 2026-05-17T07:08:46.069Z_

<details><summary>↩ Tool result · `toolu_016eGP4J2PeEX3d6ESdxj95k`</summary>

```text
Web search results for query: "ACL Rolling Review review form scoring criteria "overall assessment" 2025 2026"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"}]

Based on the search results, here's what I found about ACL Rolling Review's scoring criteria and overall assessment for 2025-2026:

## Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Subjective preferences should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Assessment

ACs should mostly follow the soundness assessment of the reviewers when they are in agreement, and they can weigh in when there is a disagreement or serious issues with reviews. The Findings/main conference distinction is about selecting among all the good papers those that are distinguished in some respect and have no other issues. A main conference paper could be distinguished by excitement, novelty, impact, and/or other factors, considered case-by-case.

The search results indicate these three scoring components (soundness, excitement, and overall recommendation) are the key elements of the ARR review form for the 2025-2026 cycles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bc012b9-a01b-4a4c-80b7-b4921c6bf80c",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "8621fc97-9a52-4db9-89d2-9af2850faf67",
  "toolUseResult": {
    "query": "ACL Rolling Review review form scoring criteria \"overall assessment\" 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A9wy67NkmYJg3dSM1svJH7",
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
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
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
            "title": "🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum",
            "url": "https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"
          },
          {
            "title": "ACL Rolling Review | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/acl-rolling-review"
          },
          {
            "title": "Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/incentives2026"
          },
          {
            "title": "ACL ARR 2025 May | OpenReview",
            "url": "https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"
          }
        ]
      },
      "Based on the search results, here's what I found about ACL Rolling Review's scoring criteria and overall assessment for 2025-2026:\n\n## Scoring Criteria\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\n\n### Soundness Score\nThe soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.\n\n### Excitement Score\nSubjective preferences should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.\n\n## Area Chair Assessment\n\nACs should mostly follow the soundness assessment of the reviewers when they are in agreement, and they can weigh in when there is a disagreement or serious issues with reviews. The Findings/main conference distinction is about selecting among all the good papers those that are distinguished in some respect and have no other issues. A main conference paper could be distinguished by excitement, novelty, impact, and/or other factors, considered case-by-case.\n\nThe search results indicate these three scoring components (soundness, excitement, and overall recommendation) are the key elements of the ARR review form for the 2025-2026 cycles."
    ],
    "durationSeconds": 6.453553538
  },
  "sourceToolAssistantUUID": "3bc012b9-a01b-4a4c-80b7-b4921c6bf80c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-17T07:08:53.041Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CLog8LDnL45mbhjZfQsGpL`</summary>

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
  "parentUuid": "8621fc97-9a52-4db9-89d2-9af2850faf67",
  "isSidechain": false,
  "requestId": "req_011Cb7im5HV4cguVg6J6R7AW",
  "type": "assistant",
  "uuid": "0811b270-e691-4a2f-9a08-f0dcbd21dee1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191hg9H2c6W64PT8DfodQYn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 61,
      "cache_creation_input_tokens": 1224,
      "cache_read_input_tokens": 61365,
      "output_tokens": 435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 61,
          "output_tokens": 435,
          "cache_read_input_tokens": 61365,
          "cache_creation_input_tokens": 1224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1224
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-17T07:08:53.049Z_

<details><summary>↩ Tool result · `toolu_01CLog8LDnL45mbhjZfQsGpL`</summary>

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
  "parentUuid": "0811b270-e691-4a2f-9a08-f0dcbd21dee1",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "6c68b99d-56fc-48e6-b9d5-835c2176d4a9",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "0811b270-e691-4a2f-9a08-f0dcbd21dee1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-17T07:08:53.648Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01S8srXbuyTbha87ZAScRH9S`</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c68b99d-56fc-48e6-b9d5-835c2176d4a9",
  "isSidechain": false,
  "requestId": "req_011Cb7im5HV4cguVg6J6R7AW",
  "type": "assistant",
  "uuid": "96535215-ffef-41f5-b25d-8324d34fff0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191hg9H2c6W64PT8DfodQYn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 61,
      "cache_creation_input_tokens": 1224,
      "cache_read_input_tokens": 61365,
      "output_tokens": 435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 61,
          "output_tokens": 435,
          "cache_read_input_tokens": 61365,
          "cache_creation_input_tokens": 1224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1224
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-17T07:08:56.695Z_

<details><summary>↩ Tool result · `toolu_01W25gnU7mDstvqJo4vZMpTT`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:235:Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e528696f-0c1e-4746-aba0-fecc62217803",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "1ef4d048-6858-442e-9e0b-0ff4082416f9",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:235:Structural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "e528696f-0c1e-4746-aba0-fecc62217803",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-17T07:08:53.661Z_

<details><summary>↩ Tool result · `toolu_01S8srXbuyTbha87ZAScRH9S`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:5:Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement signals that assume equivalence can be determined via exact match or semantic similarity.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:23:Our selection strategies instantiate MBR decoding \cite{eikema2022sampling, deguchi2024centroid} with structural utility functions.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:36:Fine-tuning itself contributes to the problem: \citet{kirk2024understanding} document diversity collapse in RLHF-trained models; our instance degeneracy is an analogous phenomenon in supervised fine-tuning, where stronger models converge to more uniform outputs.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:78:We test three LP${\times}$VC combination strategies: VC-stratified LP selection, LP${\times}$VC product ranking, and LP tiebreaking within VC-equivalent groups.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:96:VC becomes per-sample in the selection context (each candidate's overlap with the majority-voted output varies), yet tends to select the most typical rather than the best output---consistent with MBR's known mode-seeking bias \cite{eikema2022sampling, deguchi2024centroid}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:241:While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:475:All $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:485:Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:694:Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:705:Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:801:We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:3:Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:37:    A diagnostic chain (LoRA-rank ablation, free-form decoding, entity-token LP, supervised signal combination) confirms the bottleneck lies in the feature space, not signal aggregation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96535215-ffef-41f5-b25d-8324d34fff0a",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "39e281a9-f949-4b0a-b168-e1c21d269878",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:5:Test-time scaling studies \\cite{snell2025scaling, brown2024monkeys} and reward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement signals that assume equivalence can be determined via exact match or semantic similarity.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:23:Our selection strategies instantiate MBR decoding \\cite{eikema2022sampling, deguchi2024centroid} with structural utility functions.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:36:Fine-tuning itself contributes to the problem: \\citet{kirk2024understanding} document diversity collapse in RLHF-trained models; our instance degeneracy is an analogous phenomenon in supervised fine-tuning, where stronger models converge to more uniform outputs.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:78:We test three LP${\\times}$VC combination strategies: VC-stratified LP selection, LP${\\times}$VC product ranking, and LP tiebreaking within VC-equivalent groups.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:96:VC becomes per-sample in the selection context (each candidate's overlap with the majority-voted output varies), yet tends to select the most typical rather than the best output---consistent with MBR's known mode-seeking bias \\cite{eikema2022sampling, deguchi2024centroid}.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:241:While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:475:All $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:485:Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}, Figure~\\ref{fig:lp_range_cdf}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:694:Our selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:705:Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:801:We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:3:Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \\citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \\cite{snell2025scaling, brown2024monkeys}.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:37:    A diagnostic chain (LoRA-rank ablation, free-form decoding, entity-token LP, supervised signal combination) confirms the bottleneck lies in the feature space, not signal aggregation.",
    "numLines": 13
  },
  "sourceToolAssistantUUID": "96535215-ffef-41f5-b25d-8324d34fff0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-17T07:08:55.054Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01XfAeXTNYwSfNapi7V77MYA`</summary>

```json
{
  "pattern": "(Furthermore|Moreover|Additionally)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39e281a9-f949-4b0a-b168-e1c21d269878",
  "isSidechain": false,
  "requestId": "req_011Cb7im5HV4cguVg6J6R7AW",
  "type": "assistant",
  "uuid": "c9049867-c44a-4526-869e-86f33f658539",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191hg9H2c6W64PT8DfodQYn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 61,
      "cache_creation_input_tokens": 1224,
      "cache_read_input_tokens": 61365,
      "output_tokens": 435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 61,
          "output_tokens": 435,
          "cache_read_input_tokens": 61365,
          "cache_creation_input_tokens": 1224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1224
          },
          "type": "message"
        }
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

_source line 58 · 2026-05-17T07:08:55.069Z_

<details><summary>↩ Tool result · `toolu_01XfAeXTNYwSfNapi7V77MYA`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9049867-c44a-4526-869e-86f33f658539",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "6a099b24-a9c5-42f9-a6cd-8aa73af50542",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "c9049867-c44a-4526-869e-86f33f658539",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-17T07:08:56.678Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01W25gnU7mDstvqJo4vZMpTT`</summary>

```json
{
  "pattern": "(delve|leverage|utilize|facilitate|myriad|plethora|paradigm shift)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a099b24-a9c5-42f9-a6cd-8aa73af50542",
  "isSidechain": false,
  "requestId": "req_011Cb7im5HV4cguVg6J6R7AW",
  "type": "assistant",
  "uuid": "e528696f-0c1e-4746-aba0-fecc62217803",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191hg9H2c6W64PT8DfodQYn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 61,
      "cache_creation_input_tokens": 1224,
      "cache_read_input_tokens": 61365,
      "output_tokens": 435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 61,
          "output_tokens": 435,
          "cache_read_input_tokens": 61365,
          "cache_creation_input_tokens": 1224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1224
          },
          "type": "message"
        }
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

_source line 60 · 2026-05-17T07:08:56.863Z_

```json
{
  "parentUuid": "1ef4d048-6858-442e-9e0b-0ff4082416f9",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "58696e73-3ad2-4bf0-9f96-db9682a1947c",
  "timestamp": "2026-05-17T07:08:56.863Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 61_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性 + 写作质量**  ### Venue 信息 - 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - 截止日期: 2026-05-25 - 页数限制: 长文 8 页正文（Limitations/Ethics…",
  "leafUuid": "58696e73-3ad2-4bf0-9f96-db9682a1947c",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper for EMNLP 2026",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Assistant

_source line 63 · 2026-05-17T07:09:01.343Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now fetch the official ARR review form to get exact scoring criteria, and also read parts of the appendix to check for completeness. Let me also run the reference verification tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58696e73-3ad2-4bf0-9f96-db9682a1947c",
  "isSidechain": false,
  "requestId": "req_011Cb7imrvccAXTMbposrott",
  "type": "assistant",
  "uuid": "42927317-43dd-4724-b5b6-870155b7bd46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gUE1js4QhMv1oYkTtWDQu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2586,
      "cache_read_input_tokens": 62589,
      "output_tokens": 388,
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
          "input_tokens": 3,
          "output_tokens": 388,
          "cache_read_input_tokens": 62589,
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

### Tool call

_source line 64 · 2026-05-17T07:09:04.193Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Kxz5947jAngiABNfWDb67H`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form including all scoring dimensions, their scales (1-5 or 1-6 etc), and the description of each score level. Focus on: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42927317-43dd-4724-b5b6-870155b7bd46",
  "isSidechain": false,
  "requestId": "req_011Cb7imrvccAXTMbposrott",
  "type": "assistant",
  "uuid": "98db3e76-16d7-4109-a805-74b65362effd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gUE1js4QhMv1oYkTtWDQu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2586,
      "cache_read_input_tokens": 62589,
      "output_tokens": 388,
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
          "input_tokens": 3,
          "output_tokens": 388,
          "cache_read_input_tokens": 62589,
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

### Tool call

_source line 65 · 2026-05-17T07:09:04.720Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_0193i4TNTzdW9c18SYNTepWn`</summary>

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
  "parentUuid": "98db3e76-16d7-4109-a805-74b65362effd",
  "isSidechain": false,
  "requestId": "req_011Cb7imrvccAXTMbposrott",
  "type": "assistant",
  "uuid": "8bc05dc5-0686-4740-9021-7f65e9e024ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gUE1js4QhMv1oYkTtWDQu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2586,
      "cache_read_input_tokens": 62589,
      "output_tokens": 388,
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
          "input_tokens": 3,
          "output_tokens": 388,
          "cache_read_input_tokens": 62589,
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

### Tool call

_source line 66 · 2026-05-17T07:09:05.434Z_

<details open><summary>🔧 Tool call — Read · `toolu_013ddpXVTQfJZGjfE5cuRk9c`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bc05dc5-0686-4740-9021-7f65e9e024ee",
  "isSidechain": false,
  "requestId": "req_011Cb7imrvccAXTMbposrott",
  "type": "assistant",
  "uuid": "a20a2eaa-1996-433f-90f0-709d7885c913",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gUE1js4QhMv1oYkTtWDQu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2586,
      "cache_read_input_tokens": 62589,
      "output_tokens": 388,
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
          "input_tokens": 3,
          "output_tokens": 388,
          "cache_read_input_tokens": 62589,
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

### Tool result

_source line 67 · 2026-05-17T07:09:11.747Z_

<details><summary>↩ Tool result · `toolu_01Kxz5947jAngiABNfWDb67H`</summary>

```text
# ACL Rolling Review Form - Scoring Dimensions

## Overall Assessment
**Scale:** 1-5 with half-point increments

- **5:** "Consider for Award: I think this paper could be considered for an outstanding paper award"
- **4.5:** Borderline Award
- **4:** "Conference: I think this paper could be accepted to an *ACL conference"
- **3.5:** Borderline Conference
- **3:** "Findings: I think this paper could be accepted to the Findings of the ACL"
- **2.5:** Borderline Findings
- **2:** "Resubmit next cycle: I think this paper needs substantial revisions"
- **1.5:** "Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle"
- **1:** "Do not resubmit: This paper has to be fully redone"

## Soundness
**Scale:** 1-5 with half-point increments

- **5:** "Excellent: This study is one of the most thorough I have seen"
- **4:** "Strong: This study provides sufficient support for all of its claims"
- **3:** "Acceptable: This study provides sufficient support for its main claims"
- **2:** "Poor: Some of the main claims are not sufficiently supported"
- **1:** "Major Issues: This study is not yet sufficiently thorough"

## Excitement
**Scale:** 1-5 with half-point increments

- **5:** "Highly Exciting: I would recommend this paper to others"
- **4:** "Exciting: I would mention this paper to others"
- **3:** "Interesting: I might mention some points of this paper to others"
- **2:** "Potentially Interesting: this paper does not resonate with me"
- **1:** "Not Exciting: this paper does not resonate with me"

## Reviewer Confidence
**Scale:** 1-5

- **5:** "Positive that my evaluation is correct. I read the paper very carefully"
- **4:** "Quite sure. I tried to check the important points carefully"
- **3:** "Pretty sure, but there's a chance I missed something"
- **2:** "Willing to defend my evaluation, but fairly likely missed details"
- **1:** "Not my area, or paper is very hard to understand"

## Reproducibility
**Scale:** 1-5

- **5:** "They could easily reproduce the results"
- **4:** "They could mostly reproduce the results"
- **3:** "They could reproduce the results with some difficulty"
- **2:** "They would be hard pressed to reproduce the results"
- **1:** "They would not be able to reproduce the results"

## Datasets & Software
**Scale:** 1-5 (identical scales for both)

- **5:** "Enabling: The newly released [datasets/software] should affect other people's choice"
- **4:** "Useful: I would recommend the new [datasets/software] to other researchers"
- **3:** "Potentially useful: Someone might find useful"
- **2:** "Documentary: useful to study or replicate the reported research"
- **1:** "No usable [datasets/software] submitted"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98db3e76-16d7-4109-a805-74b65362effd",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "f7115fa9-eb4e-484f-8dec-5ac4c9991327",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Scoring Dimensions\n\n## Overall Assessment\n**Scale:** 1-5 with half-point increments\n\n- **5:** \"Consider for Award: I think this paper could be considered for an outstanding paper award\"\n- **4.5:** Borderline Award\n- **4:** \"Conference: I think this paper could be accepted to an *ACL conference\"\n- **3.5:** Borderline Conference\n- **3:** \"Findings: I think this paper could be accepted to the Findings of the ACL\"\n- **2.5:** Borderline Findings\n- **2:** \"Resubmit next cycle: I think this paper needs substantial revisions\"\n- **1.5:** \"Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle\"\n- **1:** \"Do not resubmit: This paper has to be fully redone\"\n\n## Soundness\n**Scale:** 1-5 with half-point increments\n\n- **5:** \"Excellent: This study is one of the most thorough I have seen\"\n- **4:** \"Strong: This study provides sufficient support for all of its claims\"\n- **3:** \"Acceptable: This study provides sufficient support for its main claims\"\n- **2:** \"Poor: Some of the main claims are not sufficiently supported\"\n- **1:** \"Major Issues: This study is not yet sufficiently thorough\"\n\n## Excitement\n**Scale:** 1-5 with half-point increments\n\n- **5:** \"Highly Exciting: I would recommend this paper to others\"\n- **4:** \"Exciting: I would mention this paper to others\"\n- **3:** \"Interesting: I might mention some points of this paper to others\"\n- **2:** \"Potentially Interesting: this paper does not resonate with me\"\n- **1:** \"Not Exciting: this paper does not resonate with me\"\n\n## Reviewer Confidence\n**Scale:** 1-5\n\n- **5:** \"Positive that my evaluation is correct. I read the paper very carefully\"\n- **4:** \"Quite sure. I tried to check the important points carefully\"\n- **3:** \"Pretty sure, but there's a chance I missed something\"\n- **2:** \"Willing to defend my evaluation, but fairly likely missed details\"\n- **1:** \"Not my area, or paper is very hard to understand\"\n\n## Reproducibility\n**Scale:** 1-5\n\n- **5:** \"They could easily reproduce the results\"\n- **4:** \"They could mostly reproduce the results\"\n- **3:** \"They could reproduce the results with some difficulty\"\n- **2:** \"They would be hard pressed to reproduce the results\"\n- **1:** \"They would not be able to reproduce the results\"\n\n## Datasets & Software\n**Scale:** 1-5 (identical scales for both)\n\n- **5:** \"Enabling: The newly released [datasets/software] should affect other people's choice\"\n- **4:** \"Useful: I would recommend the new [datasets/software] to other researchers\"\n- **3:** \"Potentially useful: Someone might find useful\"\n- **2:** \"Documentary: useful to study or replicate the reported research\"\n- **1:** \"No usable [datasets/software] submitted\"",
    "durationMs": 7552,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "98db3e76-16d7-4109-a805-74b65362effd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-17T07:10:14.233Z_

<details><summary>↩ Tool result · `toolu_0193i4TNTzdW9c18SYNTepWn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 59, \"total_citations\": 88, \"unique_cited_keys\": 59, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 50, \"online_not_found\": 4, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"W-NUT Workshop at EMNLP 2017\"}, {\"key\": \"ding2021fewnerd\", \"type\": \"inproceedings\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"authors\": \"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"eikema2022sampling\", \"type\": \"inproceedings\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"authors\": \"Eikema, Bryan and Aziz, Wilker\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"freitag2022high\", \"type\": \"article\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"authors\": \"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\", \"year\": \"2022\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"fleiss1971agreement\", \"type\": \"article\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"authors\": \"Fleiss, Joseph L.\", \"year\": \"1971\", \"venue\": \"Psychological Bulletin\"}, {\"key\": \"feng2025optimal\", \"type\": \"article\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"authors\": \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.12309\"}, {\"key\": \"geng2024confidence\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"hobelsberger2025systematic\", \"type\": \"article\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"authors\": \"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.20460\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kang2025selfcertainty\", \"type\": \"inproceedings\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"authors\": \"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"kim2026reasc\", \"type\": \"inproceedings\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"authors\": \"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\", \"year\": \"2026\", \"venue\": \"ACL 2026\"}, {\"key\": \"li2025llms\", \"type\": \"article\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"authors\": \"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.04104\"}, {\"key\": \"kuhn2023semantic\", \"type\": \"inproceedings\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"authors\": \"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"malinin2021uncertainty\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"authors\": \"Malinin, Andrey and Gales, Mark\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"li2023codeie\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lightman2024verify\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"luan2018scierc\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"authors\": \"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"manakul2023selfcheckgpt\", \"type\": \"inproceedings\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"authors\": \"Manakul, Potsawee and Liusie, Adian and Gales, Mark\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"yao2026consistency\", \"type\": \"article\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\", \"authors\": \"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\", \"year\": \"2026\", \"venue\": \"Genomics \\\\& Informatics\"}, {\"key\": \"oh2026latentsc\", \"type\": \"article\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"authors\": \"Oh, Jungsuk and Lee, Jay-Yoon\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2508.18395\"}, {\"key\": \"sainz2024gollie\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"snell2025scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"authors\": \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"taubenfeld2025cisc\", \"type\": \"inproceedings\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"authors\": \"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"thirukovalluru2024atomic\", \"type\": \"inproceedings\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"authors\": \"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"tjongkimsang2003conll\", \"type\": \"inproceedings\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"authors\": \"Sang, Erik F. Tjong Kim and Meulder, Fien De\", \"year\": \"2003\", \"venue\": \"CoNLL 2003\"}, {\"key\": \"vashurin2025cocoa\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"authors\": \"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"wadhwa2023revisiting\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"wang2023selfconsistency\", \"type\": \"inproceedings\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"authors\": \"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"wang2025make\", \"type\": \"inproceedings\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"authors\": \"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2025\"}, {\"key\": \"wang2025rankedvoting\", \"type\": \"inproceedings\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"authors\": \"Wang, Weiqin and Wang, Yile and Huang, Hui\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"willard2023guided\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, Rémi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"xia2025survey\", \"type\": \"inproceedings\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"authors\": \"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"zheng2024llamafactory\", \"type\": \"inproceedings\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"authors\": \"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"zhou2024uniner\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"muller2021understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"authors\": \"M\\\\\\\"uller, Mathias and Sennrich, Rico\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"eikema2025structured\", \"type\": \"inproceedings\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"authors\": \"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"venktesh2025trust\", \"type\": \"article\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"authors\": \"Venktesh, V and Rathee, Mandeep and Anand, Avishek\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.16665\"}, {\"key\": \"jinnai2024mbr\", \"type\": \"inproceedings\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"authors\": \"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}, {\"key\": \"ratinov2009design\", \"type\": \"inproceedings\", \"title\": \"Design Challenges and Misconceptions in Named Entity Recognition\", \"authors\": \"Ratinov, Lev and Roth, Dan\", \"year\": \"2009\", \"venue\": \"Proceedings of the Thirteenth Conference on Computational Natural Language Learn...\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"type\": \"inproceedings\", \"title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"authors\": \"Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan\", \"year\": \"2012\", \"venue\": \"Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Languag...\"}, {\"key\": \"tian2023calibration\", \"type\": \"inproceedings\", \"title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models\", \"authors\": \"Tian, Katherine and Mitchell, Eric and Yao, Huaxiu and Manning, Christopher D. a...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"fernandes2022quality\", \"type\": \"inproceedings\", \"title\": \"Quality-Aware Decoding for Neural Machine Translation\", \"authors\": \"Fernandes, Patrick and Farinhas, Ant\\\\'onio and Rei, Ricardo and de Souza, Jos\\\\'e...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"zhang2025conformal\", \"type\": \"inproceedings\", \"title\": \"Conformal Structured Prediction\", \"authors\": \"Zhang, Botong and Li, Shuo and Bastani, Osbert\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"bhattacharyya2026beyond\", \"type\": \"article\", \"title\": \"Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs\", \"authors\": \"Bhattacharyya, Sree and Khanna, Samarth and Chen, Leona and Craig, Lucas and Dil...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.07806\"}, {\"key\": \"deguchi2024centroid\", \"type\": \"inproceedings\", \"title\": \"Centroid-Based Efficient Minimum Bayes Risk Decoding\", \"authors\": \"Deguchi, Hiroyuki and Kamigaito, Hidetaka and Watanabe, Taro\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"mejer2010confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence in Structured-Prediction Using Confidence-Weighted Models\", \"authors\": \"Mejer, Avihai and Crammer, Koby\", \"year\": \"2010\", \"venue\": \"Proceedings of the 2010 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"xie2024selfevaluation\", \"type\": \"inproceedings\", \"title\": \"Self-Evaluation Improves Selective Generation in Large Language Models\", \"authors\": \"Xie, Jie and Lu, Kai and Dong, Rui and Pan, Liangming and Han, Qi and Wang, Shas...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"schall2025hidden\", \"type\": \"inproceedings\", \"title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"authors\": \"Schall, Maximilian and de Melo, Gerard\", \"year\": \"2025\", \"venue\": \"Proceedings of Recent Advances in Natural Language Processing (RANLP)\"}, {\"key\": \"yun2025price\", \"type\": \"inproceedings\", \"title\": \"The Price of Format: Diversity Collapse in LLMs\", \"authors\": \"Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingb...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2025\"}, {\"key\": \"park2024grammar\", \"type\": \"inproceedings\", \"title\": \"Grammar-Aligned Decoding\", \"authors\": \"Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadi...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems 37 (NeurIPS)\"}, {\"key\": \"gao2023scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling Laws for Reward Model Overoptimization\", \"authors\": \"Gao, Leo and Schulman, John and Hilton, Jacob\", \"year\": \"2023\", \"venue\": \"Proceedings of the 40th International Conference on Machine Learning (ICML)\"}, {\"key\": \"kirk2024understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Effects of RLHF on LLM Generalisation and Diversity\", \"authors\": \"Kirk, Robert and Mediratta, Ishita and Nalmpantis, Christoforos and Luketina, Je...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Twelfth International Conference on Learning Representations ...\"}, {\"key\": \"holtzman2020curious\", \"type\": \"inproceedings\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"authors\": \"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\", \"year\": \"2020\", \"venue\": \"Proceedings of the Eighth International Conference on Learning Representations (...\"}, {\"key\": \"kuleshov2015calibrated\", \"type\": \"inproceedings\", \"title\": \"Calibrated Structured Prediction\", \"authors\": \"Kuleshov, Volodymyr and Liang, Percy\", \"year\": \"2015\", \"venue\": \"Advances in Neural Information Processing Systems 28 (NeurIPS)\"}, {\"key\": \"fomicheva2020unsupervised\", \"type\": \"article\", \"title\": \"Unsupervised Quality Estimation for Neural Machine Translation\", \"authors\": \"Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Fr\\\\'ed\\\\'eric an...\", \"year\": \"2020\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}], \"tex_citations\": [{\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"yao2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"ding2021fewnerd\", \"file\": \"sections/introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"thirukovalluru2024atomic\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"manakul2023selfcheckgpt\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"kim2026reasc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wang2025rankedvoting\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"oh2026latentsc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"feng2025optimal\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"wang2025make\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"li2025llms\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"yao2026consistency\", \"file\": \"sections/related_work.tex\", \"line\": 10, \"command\": \"citet\"}, {\"key\": \"vashurin2025cocoa\", \"file\": \"sections/related_work.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"culotta2004confidence\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"mejer2010confidence\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"fomicheva2020unsupervised\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"zhou2024uniner\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"sainz2024gollie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"li2023codeie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wadhwa2023revisiting\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"park2024grammar\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"schall2025hidden\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"yun2025price\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"geng2024confidence\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xia2025survey\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"hobelsberger2025systematic\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"kadavath2022language\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"malinin2021uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"deguchi2024centroid\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"citet\"}, {\"key\": \"xie2024selfevaluation\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"citet\"}, {\"key\": \"kuleshov2015calibrated\", \"file\": \"sections/related_work.tex\", \"line\": 29, \"command\": \"cite\"}, {\"key\": \"zhang2025conformal\", \"file\": \"sections/related_work.tex\", \"line\": 30, \"command\": \"cite\"}, {\"key\": \"gao2023scaling\", \"file\": \"sections/related_work.tex\", \"line\": 33, \"command\": \"citet\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/related_work.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"lightman2024verify\", \"file\": \"sections/related_work.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"fernandes2022quality\", \"file\": \"sections/related_work.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"kirk2024understanding\", \"file\": \"sections/related_work.tex\", \"line\": 36, \"command\": \"citet\"}, {\"key\": \"holtzman2020curious\", \"file\": \"sections/related_work.tex\", \"line\": 37, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/method.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fleiss1971agreement\", \"file\": \"sections/method.tex\", \"line\": 26, \"command\": \"citet\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/method.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/experiments.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"ding2021fewnerd\", \"file\": \"sections/experiments.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/experiments.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"zheng2024llamafactory\", \"file\": \"sections/experiments.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/experiments.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/experiments.tex\", \"line\": 122, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/discussion.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"bhattacharyya2026beyond\", \"file\": \"sections/discussion.tex\", \"line\": 74, \"command\": \"citealp\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/discussion.tex\", \"line\": 96, \"command\": \"cite\"}, {\"key\": \"deguchi2024centroid\", \"file\": \"sections/discussion.tex\", \"line\": 96, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/discussion.tex\", \"line\": 131, \"command\": \"cite\"}, {\"key\": \"venktesh2025trust\", \"file\": \"sections/discussion.tex\", \"line\": 131, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/conclusion.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"tian2023calibration\", \"file\": \"sections/limitations.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/appendix.tex\", \"line\": 233, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/appendix.tex\", \"line\": 233, \"command\": \"cite\"}, {\"key\": \"ratinov2009design\", \"file\": \"sections/appendix.tex\", \"line\": 368, \"command\": \"cite\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"file\": \"sections/appendix.tex\", \"line\": 369, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/appendix.tex\", \"line\": 461, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/appendix.tex\", \"line\": 694, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/appendix.tex\", \"line\": 694, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/appendix.tex\", \"line\": 695, \"command\": \"cite\"}, {\"key\": \"jinnai2024mbr\", \"file\": \"sections/appendix.tex\", \"line\": 695, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/appendix.tex\", \"line\": 696, \"command\": \"citet\"}, {\"key\": \"tian2023calibration\", \"file\": \"sections/appendix.tex\", \"line\": 1022, \"command\": \"citet\"}], \"online_verification\": [{\"key\": \"brown2024monkeys\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024usc\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Self-Consistency for Large Language Model Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021verifiers\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culotta2004confidence\", \"title\": \"Confidence Estimation for Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence estimation for information extraction\", \"matched_year\": \"2004\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"derczynski2017wnut\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ding2021fewnerd\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eikema2022sampling\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"freitag2022high\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fleiss1971agreement\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring nominal scale agreement among many raters.\", \"matched_year\": \"1971\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feng2025optimal\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=feng vs api=austin\"], \"note\": \"\"}, {\"key\": \"geng2024confidence\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hobelsberger2025systematic\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.236, \"matched_title\": \"A new criterion for assessing discriminant validity in variance-based structural equation modeling\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.24 below threshold 0.82\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2025selfcertainty\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2026reasc\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025llms\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuhn2023semantic\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"malinin2021uncertainty\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023codeie\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lightman2024verify\", \"title\": \"Let's Verify Step by Step\", \"status\": \"not_found\", \"confidence\": 0.246, \"matched_title\": \"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"luan2018scierc\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"manakul2023selfcheckgpt\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yao2026consistency\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oh2026latentsc\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sainz2024gollie\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"snell2025scaling\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=snell vs api=charlie\"], \"note\": \"\"}, {\"key\": \"taubenfeld2025cisc\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence Improves Self-Consistency in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thirukovalluru2024atomic\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tjongkimsang2003conll\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"matched_year\": \"2003\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vashurin2025cocoa\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa2023revisiting\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023selfconsistency\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025make\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025rankedvoting\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023guided\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2025survey\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zheng2024llamafactory\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024uniner\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"muller2021understanding\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"matched_year\": \"2021\", \"mismatch_fields\": [\"first_author: bib=m\\\\\\\"uller vs api=müller\"], \"note\": \"\"}, {\"key\": \"eikema2025structured\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"venktesh2025trust\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"status\": \"not_found\", \"confidence\": 0.252, \"matched_title\": \"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"jinnai2024mbr\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ratinov2009design\", \"title\": \"Design Challenges and Misconceptions in Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Design challenges and misconceptions in named entity recognition\", \"matched_year\": \"2009\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"matched_year\": \"2012\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tian2023calibration\", \"title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models\", \"status\": \"verified\", \"confidence\": 0.866, \"matched_title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fernandes2022quality\", \"title\": \"Quality-Aware Decoding for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Quality-Aware Decoding for Neural Machine Translation\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2025conformal\", \"title\": \"Conformal Structured Prediction\", \"status\": \"not_found\", \"confidence\": 0.431, \"matched_title\": \"Conformal Regression for Quantitative Structure–Activity Relationship Modeling—Quantifying Prediction Uncertainty\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.43 below threshold 0.82\"}, {\"key\": \"bhattacharyya2026beyond\", \"title\": \"Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"deguchi2024centroid\", \"title\": \"Centroid-Based Efficient Minimum Bayes Risk Decoding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Centroid-Based Efficient Minimum Bayes Risk Decoding\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mejer2010confidence\", \"title\": \"Confidence in Structured-Prediction Using Confidence-Weighted Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence in Structured-Prediction Using Confidence-Weighted Models\", \"matched_year\": \"2010\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie2024selfevaluation\", \"title\": \"Self-Evaluation Improves Selective Generation in Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Self-Evaluation Improves Selective Generation in Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=xie vs api=ren\"], \"note\": \"\"}, {\"key\": \"schall2025hidden\", \"title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yun2025price\", \"title\": \"The Price of Format: Diversity Collapse in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Price of Format: Diversity Collapse in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"park2024grammar\", \"title\": \"Grammar-Aligned Decoding\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Grammar-Aligned Decoding\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=park vs api=berg-kirkpatrick\"], \"note\": \"\"}, {\"key\": \"gao2023scaling\", \"title\": \"Scaling Laws for Reward Model Overoptimization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scaling Laws for Reward Model Overoptimization\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kirk2024understanding\", \"title\": \"Understanding the Effects of RLHF on LLM Generalisation and Diversity\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Effects of RLHF on LLM Generalisation and Diversity\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"holtzman2020curious\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Case of Neural Text Degeneration\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuleshov2015calibrated\", \"title\": \"Calibrated Structured Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calibrated structured prediction\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fomicheva2020unsupervised\", \"title\": \"Unsupervised Quality Estimation for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Unsupervised Quality Estimation for Neural Machine Translation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bc05dc5-0686-4740-9021-7f65e9e024ee",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "d48bb5ad-2a5c-4beb-86e2-128b5115ed89",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 59, \\\"total_citations\\\": 88, \\\"unique_cited_keys\\\": 59, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 50, \\\"online_not_found\\\": 4, \\\"online_mismatch\\\": 5}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"brown2024monkeys\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"authors\\\": \\\"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2407.21787\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"authors\\\": \\\"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint (ICML 2024 Workshop ICL)\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"authors\\\": \\\"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2110.14168\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"authors\\\": \\\"Culotta, Aron and McCallum, Andrew\\\", \\\"year\\\": \\\"2004\\\", \\\"venue\\\": \\\"HLT-NAACL 2004\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"authors\\\": \\\"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"W-NUT Workshop at EMNLP 2017\\\"}, {\\\"key\\\": \\\"ding2021fewnerd\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"authors\\\": \\\"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"authors\\\": \\\"Eikema, Bryan and Aziz, Wilker\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"authors\\\": \\\"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"authors\\\": \\\"Fleiss, Joseph L.\\\", \\\"year\\\": \\\"1971\\\", \\\"venue\\\": \\\"Psychological Bulletin\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2511.12309\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"authors\\\": \\\"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"authors\\\": \\\"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2510.20460\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"authors\\\": \\\"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2207.05221\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"authors\\\": \\\"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"authors\\\": \\\"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"ACL 2026\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"authors\\\": \\\"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.04104\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"authors\\\": \\\"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"authors\\\": \\\"Malinin, Andrey and Gales, Mark\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"authors\\\": \\\"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"authors\\\": \\\"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"authors\\\": \\\"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"authors\\\": \\\"Manakul, Potsawee and Liusie, Adian and Gales, Mark\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"yao2026consistency\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\\\", \\\"authors\\\": \\\"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Genomics \\\\\\\\& Informatics\\\"}, {\\\"key\\\": \\\"oh2026latentsc\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"authors\\\": \\\"Oh, Jungsuk and Lee, Jay-Yoon\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.18395\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"authors\\\": \\\"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"authors\\\": \\\"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"authors\\\": \\\"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"authors\\\": \\\"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"authors\\\": \\\"Sang, Erik F. Tjong Kim and Meulder, Fien De\\\", \\\"year\\\": \\\"2003\\\", \\\"venue\\\": \\\"CoNLL 2003\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"authors\\\": \\\"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"authors\\\": \\\"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"authors\\\": \\\"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"authors\\\": \\\"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL 2025\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"authors\\\": \\\"Wang, Weiqin and Wang, Yile and Huang, Hui\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"authors\\\": \\\"Willard, Brandon T. and Louf, Rémi\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2307.09702\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"authors\\\": \\\"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"authors\\\": \\\"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"authors\\\": \\\"M\\\\\\\\\\\\\\\"uller, Mathias and Sennrich, Rico\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"authors\\\": \\\"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\", \\\"authors\\\": \\\"Venktesh, V and Rathee, Mandeep and Anand, Avishek\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.16665\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"authors\\\": \\\"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 41st International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"ratinov2009design\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Design Challenges and Misconceptions in Named Entity Recognition\\\", \\\"authors\\\": \\\"Ratinov, Lev and Roth, Dan\\\", \\\"year\\\": \\\"2009\\\", \\\"venue\\\": \\\"Proceedings of the Thirteenth Conference on Computational Natural Language Learn...\\\"}, {\\\"key\\\": \\\"bergkirkpatrick2012empirical\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"An Empirical Investigation of Statistical Significance in NLP\\\", \\\"authors\\\": \\\"Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan\\\", \\\"year\\\": \\\"2012\\\", \\\"venue\\\": \\\"Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Languag...\\\"}, {\\\"key\\\": \\\"tian2023calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models\\\", \\\"authors\\\": \\\"Tian, Katherine and Mitchell, Eric and Yao, Huaxiu and Manning, Christopher D. a...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"fernandes2022quality\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Quality-Aware Decoding for Neural Machine Translation\\\", \\\"authors\\\": \\\"Fernandes, Patrick and Farinhas, Ant\\\\\\\\'onio and Rei, Ricardo and de Souza, Jos\\\\\\\\'e...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"zhang2025conformal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Conformal Structured Prediction\\\", \\\"authors\\\": \\\"Zhang, Botong and Li, Shuo and Bastani, Osbert\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"bhattacharyya2026beyond\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs\\\", \\\"authors\\\": \\\"Bhattacharyya, Sree and Khanna, Samarth and Chen, Leona and Craig, Lucas and Dil...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2605.07806\\\"}, {\\\"key\\\": \\\"deguchi2024centroid\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Centroid-Based Efficient Minimum Bayes Risk Decoding\\\", \\\"authors\\\": \\\"Deguchi, Hiroyuki and Kamigaito, Hidetaka and Watanabe, Taro\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"mejer2010confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence in Structured-Prediction Using Confidence-Weighted Models\\\", \\\"authors\\\": \\\"Mejer, Avihai and Crammer, Koby\\\", \\\"year\\\": \\\"2010\\\", \\\"venue\\\": \\\"Proceedings of the 2010 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"xie2024selfevaluation\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Evaluation Improves Selective Generation in Large Language Models\\\", \\\"authors\\\": \\\"Xie, Jie and Lu, Kai and Dong, Rui and Pan, Liangming and Han, Qi and Wang, Shas...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems (NeurIPS)\\\"}, {\\\"key\\\": \\\"schall2025hidden\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\\\", \\\"authors\\\": \\\"Schall, Maximilian and de Melo, Gerard\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of Recent Advances in Natural Language Processing (RANLP)\\\"}, {\\\"key\\\": \\\"yun2025price\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Price of Format: Diversity Collapse in LLMs\\\", \\\"authors\\\": \\\"Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingb...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: EMNLP 2025\\\"}, {\\\"key\\\": \\\"park2024grammar\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Grammar-Aligned Decoding\\\", \\\"authors\\\": \\\"Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadi...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems 37 (NeurIPS)\\\"}, {\\\"key\\\": \\\"gao2023scaling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scaling Laws for Reward Model Overoptimization\\\", \\\"authors\\\": \\\"Gao, Leo and Schulman, John and Hilton, Jacob\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 40th International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"kirk2024understanding\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Understanding the Effects of RLHF on LLM Generalisation and Diversity\\\", \\\"authors\\\": \\\"Kirk, Robert and Mediratta, Ishita and Nalmpantis, Christoforos and Luketina, Je...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Twelfth International Conference on Learning Representations ...\\\"}, {\\\"key\\\": \\\"holtzman2020curious\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"authors\\\": \\\"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the Eighth International Conference on Learning Representations (...\\\"}, {\\\"key\\\": \\\"kuleshov2015calibrated\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Calibrated Structured Prediction\\\", \\\"authors\\\": \\\"Kuleshov, Volodymyr and Liang, Percy\\\", \\\"year\\\": \\\"2015\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems 28 (NeurIPS)\\\"}, {\\\"key\\\": \\\"fomicheva2020unsupervised\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Unsupervised Quality Estimation for Neural Machine Translation\\\", \\\"authors\\\": \\\"Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Fr\\\\\\\\'ed\\\\\\\\'eric an...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"yao2026consistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ding2021fewnerd\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"oh2026latentsc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"yao2026consistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"mejer2010confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"fomicheva2020unsupervised\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"park2024grammar\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"schall2025hidden\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"yun2025price\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"deguchi2024centroid\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"xie2024selfevaluation\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"kuleshov2015calibrated\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2025conformal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gao2023scaling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fernandes2022quality\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kirk2024understanding\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 36, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"holtzman2020curious\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 37, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 45, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ding2021fewnerd\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 122, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"bhattacharyya2026beyond\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 74, \\\"command\\\": \\\"citealp\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 96, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"deguchi2024centroid\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 96, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 131, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 131, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/conclusion.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tian2023calibration\\\", \\\"file\\\": \\\"sections/limitations.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 233, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 233, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ratinov2009design\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 368, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"bergkirkpatrick2012empirical\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 369, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 461, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 694, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 694, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 695, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 695, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 696, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"tian2023calibration\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 1022, \\\"command\\\": \\\"citet\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"brown2024monkeys\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence estimation for information extraction\\\", \\\"matched_year\\\": \\\"2004\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ding2021fewnerd\\\", \\\"title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"matched_year\\\": \\\"1971\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=feng vs api=austin\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.236, \\\"matched_title\\\": \\\"A new criterion for assessing discriminant validity in variance-based structural equation modeling\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.24 below threshold 0.82\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.246, \\\"matched_title\\\": \\\"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yao2026consistency\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"oh2026latentsc\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=snell vs api=charlie\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2003\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=m\\\\\\\\\\\\\\\"uller vs api=müller\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"title\\\": \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.252, \\\"matched_title\\\": \\\"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ratinov2009design\\\", \\\"title\\\": \\\"Design Challenges and Misconceptions in Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Design challenges and misconceptions in named entity recognition\\\", \\\"matched_year\\\": \\\"2009\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"bergkirkpatrick2012empirical\\\", \\\"title\\\": \\\"An Empirical Investigation of Statistical Significance in NLP\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"An Empirical Investigation of Statistical Significance in NLP\\\", \\\"matched_year\\\": \\\"2012\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tian2023calibration\\\", \\\"title\\\": \\\"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.866, \\\"matched_title\\\": \\\"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fernandes2022quality\\\", \\\"title\\\": \\\"Quality-Aware Decoding for Neural Machine Translation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Quality-Aware Decoding for Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2025conformal\\\", \\\"title\\\": \\\"Conformal Structured Prediction\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.431, \\\"matched_title\\\": \\\"Conformal Regression for Quantitative Structure–Activity Relationship Modeling—Quantifying Prediction Uncertainty\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.43 below threshold 0.82\\\"}, {\\\"key\\\": \\\"bhattacharyya2026beyond\\\", \\\"title\\\": \\\"Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"deguchi2024centroid\\\", \\\"title\\\": \\\"Centroid-Based Efficient Minimum Bayes Risk Decoding\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Centroid-Based Efficient Minimum Bayes Risk Decoding\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mejer2010confidence\\\", \\\"title\\\": \\\"Confidence in Structured-Prediction Using Confidence-Weighted Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence in Structured-Prediction Using Confidence-Weighted Models\\\", \\\"matched_year\\\": \\\"2010\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xie2024selfevaluation\\\", \\\"title\\\": \\\"Self-Evaluation Improves Selective Generation in Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Evaluation Improves Selective Generation in Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=xie vs api=ren\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"schall2025hidden\\\", \\\"title\\\": \\\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yun2025price\\\", \\\"title\\\": \\\"The Price of Format: Diversity Collapse in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Price of Format: Diversity Collapse in LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"park2024grammar\\\", \\\"title\\\": \\\"Grammar-Aligned Decoding\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Grammar-Aligned Decoding\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=park vs api=berg-kirkpatrick\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gao2023scaling\\\", \\\"title\\\": \\\"Scaling Laws for Reward Model Overoptimization\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scaling Laws for Reward Model Overoptimization\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kirk2024understanding\\\", \\\"title\\\": \\\"Understanding the Effects of RLHF on LLM Generalisation and Diversity\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding the Effects of RLHF on LLM Generalisation and Diversity\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"holtzman2020curious\\\", \\\"title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kuleshov2015calibrated\\\", \\\"title\\\": \\\"Calibrated Structured Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calibrated structured prediction\\\", \\\"matched_year\\\": \\\"2015\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fomicheva2020unsupervised\\\", \\\"title\\\": \\\"Unsupervised Quality Estimation for Neural Machine Translation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Unsupervised Quality Estimation for Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 59, \"total_citations\": 88, \"unique_cited_keys\": 59, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 50, \"online_not_found\": 4, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"W-NUT Workshop at EMNLP 2017\"}, {\"key\": \"ding2021fewnerd\", \"type\": \"inproceedings\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"authors\": \"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"eikema2022sampling\", \"type\": \"inproceedings\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"authors\": \"Eikema, Bryan and Aziz, Wilker\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"freitag2022high\", \"type\": \"article\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"authors\": \"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\", \"year\": \"2022\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"fleiss1971agreement\", \"type\": \"article\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"authors\": \"Fleiss, Joseph L.\", \"year\": \"1971\", \"venue\": \"Psychological Bulletin\"}, {\"key\": \"feng2025optimal\", \"type\": \"article\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"authors\": \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.12309\"}, {\"key\": \"geng2024confidence\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"hobelsberger2025systematic\", \"type\": \"article\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"authors\": \"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.20460\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kang2025selfcertainty\", \"type\": \"inproceedings\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"authors\": \"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"kim2026reasc\", \"type\": \"inproceedings\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"authors\": \"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\", \"year\": \"2026\", \"venue\": \"ACL 2026\"}, {\"key\": \"li2025llms\", \"type\": \"article\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"authors\": \"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.04104\"}, {\"key\": \"kuhn2023semantic\", \"type\": \"inproceedings\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"authors\": \"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"malinin2021uncertainty\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"authors\": \"Malinin, Andrey and Gales, Mark\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"li2023codeie\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lightman2024verify\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"luan2018scierc\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"authors\": \"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"manakul2023selfcheckgpt\", \"type\": \"inproceedings\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"authors\": \"Manakul, Potsawee and Liusie, Adian and Gales, Mark\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"yao2026consistency\", \"type\": \"article\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\", \"authors\": \"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\", \"year\": \"2026\", \"venue\": \"Genomics \\\\& Informatics\"}, {\"key\": \"oh2026latentsc\", \"type\": \"article\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"authors\": \"Oh, Jungsuk and Lee, Jay-Yoon\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2508.18395\"}, {\"key\": \"sainz2024gollie\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"snell2025scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"authors\": \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"taubenfeld2025cisc\", \"type\": \"inproceedings\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"authors\": \"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"thirukovalluru2024atomic\", \"type\": \"inproceedings\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"authors\": \"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"tjongkimsang2003conll\", \"type\": \"inproceedings\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"authors\": \"Sang, Erik F. Tjong Kim and Meulder, Fien De\", \"year\": \"2003\", \"venue\": \"CoNLL 2003\"}, {\"key\": \"vashurin2025cocoa\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"authors\": \"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"wadhwa2023revisiting\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"wang2023selfconsistency\", \"type\": \"inproceedings\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"authors\": \"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"wang2025make\", \"type\": \"inproceedings\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"authors\": \"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2025\"}, {\"key\": \"wang2025rankedvoting\", \"type\": \"inproceedings\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"authors\": \"Wang, Weiqin and Wang, Yile and Huang, Hui\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"willard2023guided\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, Rémi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"xia2025survey\", \"type\": \"inproceedings\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"authors\": \"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"zheng2024llamafactory\", \"type\": \"inproceedings\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"authors\": \"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"zhou2024uniner\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"muller2021understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"authors\": \"M\\\\\\\"uller, Mathias and Sennrich, Rico\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"eikema2025structured\", \"type\": \"inproceedings\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"authors\": \"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"venktesh2025trust\", \"type\": \"article\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"authors\": \"Venktesh, V and Rathee, Mandeep and Anand, Avishek\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.16665\"}, {\"key\": \"jinnai2024mbr\", \"type\": \"inproceedings\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"authors\": \"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}, {\"key\": \"ratinov2009design\", \"type\": \"inproceedings\", \"title\": \"Design Challenges and Misconceptions in Named Entity Recognition\", \"authors\": \"Ratinov, Lev and Roth, Dan\", \"year\": \"2009\", \"venue\": \"Proceedings of the Thirteenth Conference on Computational Natural Language Learn...\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"type\": \"inproceedings\", \"title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"authors\": \"Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan\", \"year\": \"2012\", \"venue\": \"Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Languag...\"}, {\"key\": \"tian2023calibration\", \"type\": \"inproceedings\", \"title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models\", \"authors\": \"Tian, Katherine and Mitchell, Eric and Yao, Huaxiu and Manning, Christopher D. a...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"fernandes2022quality\", \"type\": \"inproceedings\", \"title\": \"Quality-Aware Decoding for Neural Machine Translation\", \"authors\": \"Fernandes, Patrick and Farinhas, Ant\\\\'onio and Rei, Ricardo and de Souza, Jos\\\\'e...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"zhang2025conformal\", \"type\": \"inproceedings\", \"title\": \"Conformal Structured Prediction\", \"authors\": \"Zhang, Botong and Li, Shuo and Bastani, Osbert\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"bhattacharyya2026beyond\", \"type\": \"article\", \"title\": \"Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs\", \"authors\": \"Bhattacharyya, Sree and Khanna, Samarth and Chen, Leona and Craig, Lucas and Dil...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.07806\"}, {\"key\": \"deguchi2024centroid\", \"type\": \"inproceedings\", \"title\": \"Centroid-Based Efficient Minimum Bayes Risk Decoding\", \"authors\": \"Deguchi, Hiroyuki and Kamigaito, Hidetaka and Watanabe, Taro\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"mejer2010confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence in Structured-Prediction Using Confidence-Weighted Models\", \"authors\": \"Mejer, Avihai and Crammer, Koby\", \"year\": \"2010\", \"venue\": \"Proceedings of the 2010 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"xie2024selfevaluation\", \"type\": \"inproceedings\", \"title\": \"Self-Evaluation Improves Selective Generation in Large Language Models\", \"authors\": \"Xie, Jie and Lu, Kai and Dong, Rui and Pan, Liangming and Han, Qi and Wang, Shas...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"schall2025hidden\", \"type\": \"inproceedings\", \"title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"authors\": \"Schall, Maximilian and de Melo, Gerard\", \"year\": \"2025\", \"venue\": \"Proceedings of Recent Advances in Natural Language Processing (RANLP)\"}, {\"key\": \"yun2025price\", \"type\": \"inproceedings\", \"title\": \"The Price of Format: Diversity Collapse in LLMs\", \"authors\": \"Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingb...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2025\"}, {\"key\": \"park2024grammar\", \"type\": \"inproceedings\", \"title\": \"Grammar-Aligned Decoding\", \"authors\": \"Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadi...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems 37 (NeurIPS)\"}, {\"key\": \"gao2023scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling Laws for Reward Model Overoptimization\", \"authors\": \"Gao, Leo and Schulman, John and Hilton, Jacob\", \"year\": \"2023\", \"venue\": \"Proceedings of the 40th International Conference on Machine Learning (ICML)\"}, {\"key\": \"kirk2024understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Effects of RLHF on LLM Generalisation and Diversity\", \"authors\": \"Kirk, Robert and Mediratta, Ishita and Nalmpantis, Christoforos and Luketina, Je...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Twelfth International Conference on Learning Representations ...\"}, {\"key\": \"holtzman2020curious\", \"type\": \"inproceedings\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"authors\": \"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\", \"year\": \"2020\", \"venue\": \"Proceedings of the Eighth International Conference on Learning Representations (...\"}, {\"key\": \"kuleshov2015calibrated\", \"type\": \"inproceedings\", \"title\": \"Calibrated Structured Prediction\", \"authors\": \"Kuleshov, Volodymyr and Liang, Percy\", \"year\": \"2015\", \"venue\": \"Advances in Neural Information Processing Systems 28 (NeurIPS)\"}, {\"key\": \"fomicheva2020unsupervised\", \"type\": \"article\", \"title\": \"Unsupervised Quality Estimation for Neural Machine Translation\", \"authors\": \"Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Fr\\\\'ed\\\\'eric an...\", \"year\": \"2020\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}], \"tex_citations\": [{\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"yao2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"ding2021fewnerd\", \"file\": \"sections/introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"thirukovalluru2024atomic\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"manakul2023selfcheckgpt\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"kim2026reasc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wang2025rankedvoting\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"oh2026latentsc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"feng2025optimal\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"wang2025make\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"li2025llms\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"yao2026consistency\", \"file\": \"sections/related_work.tex\", \"line\": 10, \"command\": \"citet\"}, {\"key\": \"vashurin2025cocoa\", \"file\": \"sections/related_work.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"culotta2004confidence\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"mejer2010confidence\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"fomicheva2020unsupervised\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"zhou2024uniner\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"sainz2024gollie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"li2023codeie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wadhwa2023revisiting\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"park2024grammar\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"schall2025hidden\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"yun2025price\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"geng2024confidence\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xia2025survey\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"hobelsberger2025systematic\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"kadavath2022language\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"malinin2021uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"deguchi2024centroid\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"citet\"}, {\"key\": \"xie2024selfevaluation\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"citet\"}, {\"key\": \"kuleshov2015calibrated\", \"file\": \"sections/related_work.tex\", \"line\": 29, \"command\": \"cite\"}, {\"key\": \"zhang2025conformal\", \"file\": \"sections/related_work.tex\", \"line\": 30, \"command\": \"cite\"}, {\"key\": \"gao2023scaling\", \"file\": \"sections/related_work.tex\", \"line\": 33, \"command\": \"citet\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/related_work.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"lightman2024verify\", \"file\": \"sections/related_work.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"fernandes2022quality\", \"file\": \"sections/related_work.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"kirk2024understanding\", \"file\": \"sections/related_work.tex\", \"line\": 36, \"command\": \"citet\"}, {\"key\": \"holtzman2020curious\", \"file\": \"sections/related_work.tex\", \"line\": 37, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/method.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fleiss1971agreement\", \"file\": \"sections/method.tex\", \"line\": 26, \"command\": \"citet\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/method.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/experiments.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"ding2021fewnerd\", \"file\": \"sections/experiments.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/experiments.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"zheng2024llamafactory\", \"file\": \"sections/experiments.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/experiments.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/experiments.tex\", \"line\": 122, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/discussion.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"bhattacharyya2026beyond\", \"file\": \"sections/discussion.tex\", \"line\": 74, \"command\": \"citealp\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/discussion.tex\", \"line\": 96, \"command\": \"cite\"}, {\"key\": \"deguchi2024centroid\", \"file\": \"sections/discussion.tex\", \"line\": 96, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/discussion.tex\", \"line\": 131, \"command\": \"cite\"}, {\"key\": \"venktesh2025trust\", \"file\": \"sections/discussion.tex\", \"line\": 131, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/conclusion.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"tian2023calibration\", \"file\": \"sections/limitations.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/appendix.tex\", \"line\": 233, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/appendix.tex\", \"line\": 233, \"command\": \"cite\"}, {\"key\": \"ratinov2009design\", \"file\": \"sections/appendix.tex\", \"line\": 368, \"command\": \"cite\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"file\": \"sections/appendix.tex\", \"line\": 369, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/appendix.tex\", \"line\": 461, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/appendix.tex\", \"line\": 694, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/appendix.tex\", \"line\": 694, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/appendix.tex\", \"line\": 695, \"command\": \"cite\"}, {\"key\": \"jinnai2024mbr\", \"file\": \"sections/appendix.tex\", \"line\": 695, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/appendix.tex\", \"line\": 696, \"command\": \"citet\"}, {\"key\": \"tian2023calibration\", \"file\": \"sections/appendix.tex\", \"line\": 1022, \"command\": \"citet\"}], \"online_verification\": [{\"key\": \"brown2024monkeys\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024usc\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Self-Consistency for Large Language Model Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021verifiers\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culotta2004confidence\", \"title\": \"Confidence Estimation for Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence estimation for information extraction\", \"matched_year\": \"2004\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"derczynski2017wnut\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ding2021fewnerd\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eikema2022sampling\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"freitag2022high\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fleiss1971agreement\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring nominal scale agreement among many raters.\", \"matched_year\": \"1971\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feng2025optimal\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=feng vs api=austin\"], \"note\": \"\"}, {\"key\": \"geng2024confidence\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hobelsberger2025systematic\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.236, \"matched_title\": \"A new criterion for assessing discriminant validity in variance-based structural equation modeling\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.24 below threshold 0.82\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2025selfcertainty\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2026reasc\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025llms\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuhn2023semantic\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"malinin2021uncertainty\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023codeie\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lightman2024verify\", \"title\": \"Let's Verify Step by Step\", \"status\": \"not_found\", \"confidence\": 0.246, \"matched_title\": \"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"luan2018scierc\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"manakul2023selfcheckgpt\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yao2026consistency\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oh2026latentsc\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sainz2024gollie\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"snell2025scaling\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=snell vs api=charlie\"], \"note\": \"\"}, {\"key\": \"taubenfeld2025cisc\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence Improves Self-Consistency in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thirukovalluru2024atomic\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tjongkimsang2003conll\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"matched_year\": \"2003\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vashurin2025cocoa\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa2023revisiting\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023selfconsistency\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025make\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025rankedvoting\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023guided\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2025survey\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zheng2024llamafactory\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024uniner\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"muller2021understanding\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"matched_year\": \"2021\", \"mismatch_fields\": [\"first_author: bib=m\\\\\\\"uller vs api=müller\"], \"note\": \"\"}, {\"key\": \"eikema2025structured\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"venktesh2025trust\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"status\": \"not_found\", \"confidence\": 0.252, \"matched_title\": \"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"jinnai2024mbr\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ratinov2009design\", \"title\": \"Design Challenges and Misconceptions in Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Design challenges and misconceptions in named entity recognition\", \"matched_year\": \"2009\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"matched_year\": \"2012\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tian2023calibration\", \"title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models\", \"status\": \"verified\", \"confidence\": 0.866, \"matched_title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fernandes2022quality\", \"title\": \"Quality-Aware Decoding for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Quality-Aware Decoding for Neural Machine Translation\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2025conformal\", \"title\": \"Conformal Structured Prediction\", \"status\": \"not_found\", \"confidence\": 0.431, \"matched_title\": \"Conformal Regression for Quantitative Structure–Activity Relationship Modeling—Quantifying Prediction Uncertainty\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.43 below threshold 0.82\"}, {\"key\": \"bhattacharyya2026beyond\", \"title\": \"Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"deguchi2024centroid\", \"title\": \"Centroid-Based Efficient Minimum Bayes Risk Decoding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Centroid-Based Efficient Minimum Bayes Risk Decoding\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mejer2010confidence\", \"title\": \"Confidence in Structured-Prediction Using Confidence-Weighted Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence in Structured-Prediction Using Confidence-Weighted Models\", \"matched_year\": \"2010\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie2024selfevaluation\", \"title\": \"Self-Evaluation Improves Selective Generation in Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Self-Evaluation Improves Selective Generation in Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=xie vs api=ren\"], \"note\": \"\"}, {\"key\": \"schall2025hidden\", \"title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yun2025price\", \"title\": \"The Price of Format: Diversity Collapse in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Price of Format: Diversity Collapse in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"park2024grammar\", \"title\": \"Grammar-Aligned Decoding\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Grammar-Aligned Decoding\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=park vs api=berg-kirkpatrick\"], \"note\": \"\"}, {\"key\": \"gao2023scaling\", \"title\": \"Scaling Laws for Reward Model Overoptimization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scaling Laws for Reward Model Overoptimization\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kirk2024understanding\", \"title\": \"Understanding the Effects of RLHF on LLM Generalisation and Diversity\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Effects of RLHF on LLM Generalisation and Diversity\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"holtzman2020curious\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Case of Neural Text Degeneration\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuleshov2015calibrated\", \"title\": \"Calibrated Structured Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calibrated structured prediction\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fomicheva2020unsupervised\", \"title\": \"Unsupervised Quality Estimation for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Unsupervised Quality Estimation for Neural Machine Translation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "8bc05dc5-0686-4740-9021-7f65e9e024ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-17T07:10:14.250Z_

<details><summary>↩ Tool result · `toolu_013ddpXVTQfJZGjfE5cuRk9c`</summary>

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
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
48	\quad LP & $T{=}0.7$ & 0.249 & --- \\
49	\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\
50	\midrule
51	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
52	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
53	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
54	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
55	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
56	\midrule
57	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
58	\quad SJ &  & $0.474{\pm}0.009$ & --- \\
59	\quad FK &  & $0.467{\pm}0.009$ & --- \\
60	\quad EM &  & $0.473{\pm}0.010$ & --- \\
61	\quad VC &  & $0.470{\pm}0.006$ & --- \\
62	\quad LP &  & $0.311{\pm}0.003$ & --- \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
70	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\Delta\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}
71	\label{fig:temperature_robustness}
72	\end{figure}
73	
74	\paragraph{Temperature sensitivity.}
75	SJ NER $\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.
76	FK NER $\rho$ drops by 0.022, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
77	LP exhibits the largest temperature effect on NER ($\rho{=}0.249$ at $T{=}0.7$ vs.\ $0.205$ at $T{=}1.0$, $\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.
78	Across all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).
79	
80	\paragraph{Sample size scaling.}
81	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.411{\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.
82	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
83	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\ref{tab:quality_estimation}).
84	FK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.
85	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
86	SJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, suggesting that structural and binary-agreement signals are the most robust to $N$.
87	At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), making it a more stable alternative at higher sample sizes.
88	
89	\paragraph{Transfer across model families.}
90	LLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$, $\Delta\rho{=}0.069$; permutation $p{=}0.06$, borderline).
91	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
92	At $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\rho{=}0.409$ vs.\ LP 0.239, $\Delta{=}{+}0.170$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$),\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.474{\pm}0.009$ vs.\ LP $0.311{\pm}0.003$, $\Delta{=}{+}0.163$).
93	
94	\paragraph{FK independence: instance-level permutation test.}\label{app:fk_independence}
95	
96	To verify that Fleiss' $\kappa$ reflects genuine within-instance agreement rather than marginal-rate artifacts, we conduct instance-level permutation tests across three configurations.
97	For each instance, we permute sample labels 10{,}000 times to generate a null distribution of FK under independence, then compare the observed FK against this null via a one-sample $t$-test and permutation $p$-value.
98	
99	\begin{table}[t]
100	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a20a2eaa-1996-433f-90f0-709d7885c913",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "4c19fa37-d804-4fa5-bad3-3cda0b9e49bb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\nWe exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\\%; SciERC: 22/551, 4.0\\%).\nFor these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\\rho$ depending on signal behavior at the boundary.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as sample standard deviation.}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\quad LP & $T{=}0.7$ & 0.249 & --- \\\\\n\\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.411$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.283 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.474{\\pm}0.009$ & --- \\\\\n\\quad FK &  & $0.467{\\pm}0.009$ & --- \\\\\n\\quad EM &  & $0.473{\\pm}0.010$ & --- \\\\\n\\quad VC &  & $0.470{\\pm}0.006$ & --- \\\\\n\\quad LP &  & $0.311{\\pm}0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\\Delta\\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.\nFK NER $\\rho$ drops by 0.022, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nLP exhibits the largest temperature effect on NER ($\\rho{=}0.249$ at $T{=}0.7$ vs.\\ $0.205$ at $T{=}1.0$, $\\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.\nAcross all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.411{\\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.034$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, suggesting that structural and binary-agreement signals are the most robust to $N$.\nAt $N{=}16$, SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$), making it a more stable alternative at higher sample sizes.\n\n\\paragraph{Transfer across model families.}\nLLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, $\\Delta\\rho{=}0.069$; permutation $p{=}0.06$, borderline).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\\rho{=}0.409$ vs.\\ LP 0.239, $\\Delta{=}{+}0.170$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$),\\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.474{\\pm}0.009$ vs.\\ LP $0.311{\\pm}0.003$, $\\Delta{=}{+}0.163$).\n\n\\paragraph{FK independence: instance-level permutation test.}\\label{app:fk_independence}\n\nTo verify that Fleiss' $\\kappa$ reflects genuine within-instance agreement rather than marginal-rate artifacts, we conduct instance-level permutation tests across three configurations.\nFor each instance, we permute sample labels 10{,}000 times to generate a null distribution of FK under independence, then compare the observed FK against this null via a one-sample $t$-test and permutation $p$-value.\n\n\\begin{table}[t]\n\\centering",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 1183
    }
  },
  "sourceToolAssistantUUID": "a20a2eaa-1996-433f-90f0-709d7885c913",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 70_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性 + 写作质量**  ### Venue 信息 - 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - 截止日期: 2026-05-25 - 页数限制: 长文 8 页正文（Limitations/Ethics…",
  "leafUuid": "4c19fa37-d804-4fa5-bad3-3cda0b9e49bb",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper for EMNLP 2026",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Assistant

_source line 72 · 2026-05-17T07:10:51.880Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check more specific things: the "novel" usage and any remaining items from the bib file that I haven't checked. Let me also look at the remaining references in the bib to check for Byerly & Khashabi 2024.

I have gathered enough information now. Let me compile the review:

Reference verification results:
- 59 total bib entries, 59 cited keys, 0 orphan, 0 missing
- 50 verified, 4 not_found (hobelsberger2025systematic, lightman2024verify, venktesh2025trust, zhang2025conformal), 5 mismatch (feng2025optimal, snell2025scaling, muller2021understanding, xie2024selfevaluation, park2024grammar)


- The not_found entries are likely preprints not yet indexed by OpenAlex—lightman2024verify is a well-known paper and zhang2025conformal appears legitimate. The mismatches stem from first_author field inconsistencies where the bib uses last names but the API returns first names.
- I don't see Byerly & Khashabi 2024 on correlated errors cited in the bib, so I should verify whether it's a real paper. I also need to check the word and page counts, and review the full bib for any entries I might have overlooked.

Looking at the bib file more carefully, there are 59 total references across the 497 lines, which falls within the typical range for EMNLP 2026. I'm searching for the Byerly & Khashabi paper the Director mentioned to see if it exists and whether it should be cited in the related work section on correlated errors in self-consistency.

Now I'm compiling my findings on potential AI writing markers—the em-dashes and en-dashes are absent, most "-ing" patterns appear natural, and I found only one instance of "leverage" in the appendix. All 59 references are properly cited with no orphans, though a few entries didn't resolve on OpenAlex but appear to be legitimate publications.

For the novelty assessment, the paper's main contribution is identifying the "correlation-selection gap"—essentially explaining why self-consistency methods fail for structured tasks like NER by showing that consistency signals can predict quality but can't actually select the best output. The mechanisms identified are instance degeneracy and LP compression, with degeneracy acting as a gating factor. Compared to Yao et al. (2026), this extends the work from hard-prompting to fine-tuned models and separates quality estimation from selection, which is a meaningful but somewhat incremental advance. The real question is whether this goes beyond just observing that self-consistency doesn't work for NER—and the paper does push further by formalizing the underlying mechanisms.

However, the paper is fundamentally a negative result with diagnostic value rather than a solution. The practical impact is limited since LP selection only helps marginally when degeneracy is low, and there's no proposed methodology to address the problem. For a top-tier venue like EMNLP, this thorough analysis is borderline—the diagnosis is solid but lacks actionable contributions.

The narrative reads as a well-structured empirical study rather than a compelling story, with a dense abstract heavy on numbers and an introduction that leans into statistical details. The paper clearly establishes the gap concept and supports it through extensive ablations, though the overall presentation feels more like a technical report than a cohesive argument.

Now I'm checking the formatting requirements—it follows ACL review standards, maintains anonymity, and appears to fit within the page limit. Let me draft the full review and track down that Byerly reference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c19fa37-d804-4fa5-bad3-3cda0b9e49bb",
  "isSidechain": false,
  "requestId": "req_011Cb7isZnu6nURN2QBRxVa9",
  "type": "assistant",
  "uuid": "75cf98d1-6931-41d9-94f5-5d2e854e5dd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ScgNUxjrHQRAnSvkvzJt3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21080,
      "cache_read_input_tokens": 65175,
      "output_tokens": 1586,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21080,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1586,
          "cache_read_input_tokens": 65175,
          "cache_creation_input_tokens": 21080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21080
          },
          "type": "message"
        }
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

_source line 73 · 2026-05-17T07:10:51.890Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E9tFgDkobZkrFor8LTrHjx`</summary>

```json
{
  "query": "Byerly Khashabi 2024 correlated errors self-consistency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75cf98d1-6931-41d9-94f5-5d2e854e5dd8",
  "isSidechain": false,
  "requestId": "req_011Cb7isZnu6nURN2QBRxVa9",
  "type": "assistant",
  "uuid": "d2ad69f6-4b56-4062-91a5-6a3589c7c130",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ScgNUxjrHQRAnSvkvzJt3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21080,
      "cache_read_input_tokens": 65175,
      "output_tokens": 1586,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21080,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1586,
          "cache_read_input_tokens": 65175,
          "cache_creation_input_tokens": 21080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21080
          },
          "type": "message"
        }
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

_source line 74 · 2026-05-17T07:10:53.924Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0172BdbtSy1Pjh9htSWoZFAW`</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2ad69f6-4b56-4062-91a5-6a3589c7c130",
  "isSidechain": false,
  "requestId": "req_011Cb7isZnu6nURN2QBRxVa9",
  "type": "assistant",
  "uuid": "1de00533-845a-4b1b-ab77-2a0864ef8fcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ScgNUxjrHQRAnSvkvzJt3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21080,
      "cache_read_input_tokens": 65175,
      "output_tokens": 1586,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21080,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1586,
          "cache_read_input_tokens": 65175,
          "cache_creation_input_tokens": 21080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21080
          },
          "type": "message"
        }
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

_source line 75 · 2026-05-17T07:10:54.875Z_

<details><summary>↩ Tool result · `toolu_01XgurAvWk1r9r7tZwjGc1Xx`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55b3086a-9a85-4671-beba-6d6781f43cd1",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "29ba4436-2f51-43de-b45b-2aef6dc2effa",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "55b3086a-9a85-4671-beba-6d6781f43cd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-17T07:10:53.936Z_

<details><summary>↩ Tool result · `toolu_0172BdbtSy1Pjh9htSWoZFAW`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:50:At the signal-collapse boundary---WNUT-17 (macro F1${\approx}$42\%, 52\% zero-F1 instances)---full-set correlations are dominated by the zero/non-zero boundary: VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) but conditional $\rho$ drops to 0.038 (Table~\ref{tab:wnut}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:92:Oracle & $0.778 \pm 0.003$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:93:Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:101:EM           & $0.637 \pm 0.001$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:102:VC           & $0.623 \pm 0.004$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:104:Random           & $0.610 \pm 0.003$ & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:112:The key question is whether LP---the only natively per-sample signal---can exploit the oracle headroom.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:208:Low degeneracy is thus a necessary but not sufficient condition for selection---LP compression persists regardless of LoRA rank, indicating that both mechanisms must be addressed simultaneously.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:211:To test whether the information bottleneck lies in the aggregation method or the features themselves, we train a logistic regression verifier on all five signals (3-fold cross-validation on SciERC, $N{=}16$---giving the verifier access to twice as many samples as the main results).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex:2:We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex:12:We tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selection despite increasing within-instance variance on SciERC ($4{\times}$); LP${\times}$VC combinations also fail to recover selection (\S\ref{sec:discussion}); calibration-based approaches remain unexplored.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:16:CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; Few-NERD (75\%) shows 10\%; SciERC (66\%) shows 21\%; WNUT-17 (${\approx}$42\%, macro) shows near-zero---the tension between model quality and selection utility is inherent, though Few-NERD's low degeneracy despite high performance suggests that dataset-specific factors (number of entity types, semantic overlap) also modulate the rate.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:44:This demonstrates that LP \textit{does} carry per-sample discriminative information; compression---not signal absence---is the bottleneck.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:65:Increasing $N$ from 2 to 32 expands oracle headroom more than fourfold ($+4.4$ to $+19.2$~pp) but yields no commensurate selection improvement: LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\% and oracle headroom reaches ${\sim}19$~pp---the best signal captures less than 5\% of the available improvement (Table~\ref{tab:n_scaling_selection}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:67:Bootstrap significance testing at $N{=}32$ ($B{=}10{,}000$) confirms that LP shows a consistent positive trend ($+0.95$~pp, $p{=}0.091$) but does not reach significance at $\alpha{=}0.05$, while all signals except VC significantly outperform random selection ($p{<}0.001$; Table~\ref{tab:bootstrap_n32})---the gap is not a statistical artifact but a persistent, regime-dependent limitation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:71:Structural QE signals (SJ $\rho$) improve with temperature ($0.297 \to 0.377$), while LP $\rho$ peaks at $T{=}0.8$ ($0.253$) then degrades---consistent with LP compression being model-intrinsic rather than temperature-dependent.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:80:An oracle tiebreaker---selecting the highest-F1 sample among VC-equivalent candidates---recovers $+7.9$~pp, confirming that per-sample signal \textit{exists} within VC-equivalent groups but current signals cannot extract it.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:85:(b) \textit{schema-dominated tokens}---constrained decoding enforces structural tokens (brackets, type labels) that carry no extraction information yet dominate the sequence, reducing effective variance;
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:86:(c) \textit{vocabulary restriction}---constrained decoding shrinks the effective vocabulary at each step, concentrating probability mass and reducing log-probability variation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:88:(a) \textit{token-level averaging}---mean log-probability over long sequences smooths token-level variance, compressing the effective signal;

[Showing results with pagination = limit: 20]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1de00533-845a-4b1b-ab77-2a0864ef8fcb",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "f8dccd1d-f77a-402b-850b-2a9930207084",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:50:At the signal-collapse boundary---WNUT-17 (macro F1${\\approx}$42\\%, 52\\% zero-F1 instances)---full-set correlations are dominated by the zero/non-zero boundary: VC achieves $\\rho{=}0.724$ (AUROC${=}0.913$) but conditional $\\rho$ drops to 0.038 (Table~\\ref{tab:wnut}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:92:Oracle & $0.778 \\pm 0.003$ & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:93:Greedy ($T{=}0$) & $0.645 \\pm 0.001$ & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:101:EM           & $0.637 \\pm 0.001$ & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:102:VC           & $0.623 \\pm 0.004$ & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:104:Random           & $0.610 \\pm 0.003$ & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:112:The key question is whether LP---the only natively per-sample signal---can exploit the oracle headroom.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:208:Low degeneracy is thus a necessary but not sufficient condition for selection---LP compression persists regardless of LoRA rank, indicating that both mechanisms must be addressed simultaneously.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:211:To test whether the information bottleneck lies in the aggregation method or the features themselves, we train a logistic regression verifier on all five signals (3-fold cross-validation on SciERC, $N{=}16$---giving the verifier access to twice as many samples as the main results).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex:2:We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex:12:We tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selection despite increasing within-instance variance on SciERC ($4{\\times}$); LP${\\times}$VC combinations also fail to recover selection (\\S\\ref{sec:discussion}); calibration-based approaches remain unexplored.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:16:CoNLL (91\\% single-sample F1) exhibits 58\\% degeneracy; Few-NERD (75\\%) shows 10\\%; SciERC (66\\%) shows 21\\%; WNUT-17 (${\\approx}$42\\%, macro) shows near-zero---the tension between model quality and selection utility is inherent, though Few-NERD's low degeneracy despite high performance suggests that dataset-specific factors (number of entity types, semantic overlap) also modulate the rate.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:44:This demonstrates that LP \\textit{does} carry per-sample discriminative information; compression---not signal absence---is the bottleneck.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:65:Increasing $N$ from 2 to 32 expands oracle headroom more than fourfold ($+4.4$ to $+19.2$~pp) but yields no commensurate selection improvement: LP selection improves monotonically with $N$ ($+0.42$~pp at $N{=}8$ to $+0.91$~pp at $N{=}32$), but even at $N{=}32$---where degeneracy falls to 4\\% and oracle headroom reaches ${\\sim}19$~pp---the best signal captures less than 5\\% of the available improvement (Table~\\ref{tab:n_scaling_selection}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:67:Bootstrap significance testing at $N{=}32$ ($B{=}10{,}000$) confirms that LP shows a consistent positive trend ($+0.95$~pp, $p{=}0.091$) but does not reach significance at $\\alpha{=}0.05$, while all signals except VC significantly outperform random selection ($p{<}0.001$; Table~\\ref{tab:bootstrap_n32})---the gap is not a statistical artifact but a persistent, regime-dependent limitation.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:71:Structural QE signals (SJ $\\rho$) improve with temperature ($0.297 \\to 0.377$), while LP $\\rho$ peaks at $T{=}0.8$ ($0.253$) then degrades---consistent with LP compression being model-intrinsic rather than temperature-dependent.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:80:An oracle tiebreaker---selecting the highest-F1 sample among VC-equivalent candidates---recovers $+7.9$~pp, confirming that per-sample signal \\textit{exists} within VC-equivalent groups but current signals cannot extract it.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:85:(b) \\textit{schema-dominated tokens}---constrained decoding enforces structural tokens (brackets, type labels) that carry no extraction information yet dominate the sequence, reducing effective variance;\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:86:(c) \\textit{vocabulary restriction}---constrained decoding shrinks the effective vocabulary at each step, concentrating probability mass and reducing log-probability variation.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:88:(a) \\textit{token-level averaging}---mean log-probability over long sequences smooths token-level variance, compressing the effective signal;",
    "numLines": 20,
    "appliedLimit": 20
  },
  "sourceToolAssistantUUID": "1de00533-845a-4b1b-ab77-2a0864ef8fcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-17T07:10:54.858Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01XgurAvWk1r9r7tZwjGc1Xx`</summary>

```json
{
  "pattern": "novel",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8dccd1d-f77a-402b-850b-2a9930207084",
  "isSidechain": false,
  "requestId": "req_011Cb7isZnu6nURN2QBRxVa9",
  "type": "assistant",
  "uuid": "55b3086a-9a85-4671-beba-6d6781f43cd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ScgNUxjrHQRAnSvkvzJt3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21080,
      "cache_read_input_tokens": 65175,
      "output_tokens": 1586,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21080,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1586,
          "cache_read_input_tokens": 65175,
          "cache_creation_input_tokens": 21080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21080
          },
          "type": "message"
        }
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

_source line 78 · 2026-05-17T07:10:57.939Z_

<details><summary>↩ Tool result · `toolu_01E9tFgDkobZkrFor8LTrHjx`</summary>

```text
Web search results for query: "Byerly Khashabi 2024 correlated errors self-consistency"

Links: [{"title":"How Effective Is Self-Consistency for Long-Context Problems?","url":"https://arxiv.org/html/2411.01101v1"},{"title":"Self-Consistency in Language Models","url":"https://www.emergentmind.com/topics/self-consistency-in-language-models"},{"title":"(PDF) How Effective Is Self-Consistency for Long-Context Problems?","url":"https://www.researchgate.net/publication/385529304_How_Effective_Is_Self-Consistency_for_Long-Context_Problems"},{"title":"[2411.01101] Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems","url":"https://arxiv.org/abs/2411.01101"},{"title":"dblp: Daniel Khashabi","url":"https://dblp.org/pid/71/10515.html"},{"title":"(PDF) Insights into LLM Long-Context Failures: When Transformers Know but Don't Tell","url":"https://www.researchgate.net/publication/381652297_Insights_into_LLM_Long-Context_Failures_When_Transformers_Know_but_Don't_Tell"},{"title":"Insights into LLM Long-Context Failures: When Transformers Know but Don’t Tell - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.447/"},{"title":"SELF-[IN]CORRECT: LLMs Struggle with Discriminating Self-Generated Responses","url":"https://ojs.aaai.org/index.php/AAAI/article/download/34603/36758"},{"title":"Daniel Khashabi","url":"https://danielkhashabi.com/"},{"title":"Insights into LLM Long-Context Failures: When Transformers Know but Don't Tell - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240614673L/abstract"}]

Based on the search results, I found information about Byerly and Khashabi's 2024 work on self-consistency and correlated errors:

Adam Byerly and Daniel Khashabi from Johns Hopkins University examined whether self-consistency (SC) has been demonstrated to enhance the performance of large language models (LLMs) across various tasks and domains involving short content.

Their findings demonstrate that SC, while effective for short-context problems, fundamentally fails for long-context tasks—not only does it fail to mitigate position bias, but it can also actively degrade performance.

The key insight about correlated errors is particularly notable: When SC generates multiple paths, each path likely inherits architectural biases, leading to correlated errors rather than truly diverse reasoning approaches. This aligns with the 'know but don't tell' phenomenon—if LLMs struggle to translate encoded positional information into accurate generations, aggregating multiple generations may compound rather than mitigate this fundamental limitation.

The researchers examined a range of design parameters, including different models, context lengths, prompt formats, and types of datasets and tasks, revealing the systematic nature of this problem in long-context scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2ad69f6-4b56-4062-91a5-6a3589c7c130",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "9c41d5a8-012d-40b7-a6a3-a1aac0d3a39b",
  "toolUseResult": {
    "query": "Byerly Khashabi 2024 correlated errors self-consistency",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U7EhPG1EmFFE67LijyxKGU",
        "content": [
          {
            "title": "How Effective Is Self-Consistency for Long-Context Problems?",
            "url": "https://arxiv.org/html/2411.01101v1"
          },
          {
            "title": "Self-Consistency in Language Models",
            "url": "https://www.emergentmind.com/topics/self-consistency-in-language-models"
          },
          {
            "title": "(PDF) How Effective Is Self-Consistency for Long-Context Problems?",
            "url": "https://www.researchgate.net/publication/385529304_How_Effective_Is_Self-Consistency_for_Long-Context_Problems"
          },
          {
            "title": "[2411.01101] Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems",
            "url": "https://arxiv.org/abs/2411.01101"
          },
          {
            "title": "dblp: Daniel Khashabi",
            "url": "https://dblp.org/pid/71/10515.html"
          },
          {
            "title": "(PDF) Insights into LLM Long-Context Failures: When Transformers Know but Don't Tell",
            "url": "https://www.researchgate.net/publication/381652297_Insights_into_LLM_Long-Context_Failures_When_Transformers_Know_but_Don't_Tell"
          },
          {
            "title": "Insights into LLM Long-Context Failures: When Transformers Know but Don’t Tell - ACL Anthology",
            "url": "https://aclanthology.org/2024.findings-emnlp.447/"
          },
          {
            "title": "SELF-[IN]CORRECT: LLMs Struggle with Discriminating Self-Generated Responses",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/download/34603/36758"
          },
          {
            "title": "Daniel Khashabi",
            "url": "https://danielkhashabi.com/"
          },
          {
            "title": "Insights into LLM Long-Context Failures: When Transformers Know but Don't Tell - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240614673L/abstract"
          }
        ]
      },
      "Based on the search results, I found information about Byerly and Khashabi's 2024 work on self-consistency and correlated errors:\n\nAdam Byerly and Daniel Khashabi from Johns Hopkins University examined whether self-consistency (SC) has been demonstrated to enhance the performance of large language models (LLMs) across various tasks and domains involving short content.\n\nTheir findings demonstrate that SC, while effective for short-context problems, fundamentally fails for long-context tasks—not only does it fail to mitigate position bias, but it can also actively degrade performance.\n\nThe key insight about correlated errors is particularly notable: When SC generates multiple paths, each path likely inherits architectural biases, leading to correlated errors rather than truly diverse reasoning approaches. This aligns with the 'know but don't tell' phenomenon—if LLMs struggle to translate encoded positional information into accurate generations, aggregating multiple generations may compound rather than mitigate this fundamental limitation.\n\nThe researchers examined a range of design parameters, including different models, context lengths, prompt formats, and types of datasets and tasks, revealing the systematic nature of this problem in long-context scenarios."
    ],
    "durationSeconds": 6.044163012000005
  },
  "sourceToolAssistantUUID": "d2ad69f6-4b56-4062-91a5-6a3589c7c130",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
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
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性 + 写作质量**  ### Venue 信息 - 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - 截止日期: 2026-05-25 - 页数限制: 长文 8 页正文（Limitations/Ethics…",
  "leafUuid": "9c41d5a8-012d-40b7-a6a3-a1aac0d3a39b",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Runtime record

_source line 80_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper for EMNLP 2026",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Assistant

_source line 81 · 2026-05-17T07:11:17.519Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me check the "---" usage. Those are LaTeX em-dashes (triple hyphens that render as em-dashes). Let me count them. This is important since the reviewer instructions say to check for em-dashes.

Looking at the grep results for "---", there are many instances of "---" (LaTeX em-dash encoding) in the paper:
- experiments.tex: lines 50, 92, 93, 101, 102, 104, 112, 208, 211


- limitations.tex: lines 2, 12
- discussion.tex: lines 16, 44, 65, 67, 71, 80, 85, 86, 88

So the paper uses LaTeX triple-dashes extensively throughout, which compile to em-dashes in the final output. There are no Unicode em-dashes or en-dashes, just the LaTeX encoding.

The writing guidelines are clear that em-dashes and en-dashes must be completely removed. I count roughly 20 instances across the main text sections, which is a significant writing quality issue that suggests AI generation.

Now I'm ready to compile my full assessment. The "correlation-selection gap" provides useful framing, but the core finding—that self-consistency fails for structured outputs—is fairly predictable given how NER outputs overlap partially. The paper extends prior work from hard-prompting to fine-tuned models and offers diagnostic insights, though the "instance degeneracy" concept needs further development.

Looking at completeness, there are 59 references which is solid for EMNLP, though Byerly & Khashabi 2024 on correlated errors would strengthen the related work. The writing avoids common AI markers like overused discourse markers and vague verbs, though the extensive em-dash usage is a red flag. The paper follows the ACL template correctly and maintains technical precision throughout, though the density makes it challenging to follow at times.

Now I need to check the page count before finalizing the review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c41d5a8-012d-40b7-a6a3-a1aac0d3a39b",
  "isSidechain": false,
  "requestId": "req_011Cb7ivnbR5Rb1LH8tP4db7",
  "type": "assistant",
  "uuid": "1c1c21f5-7238-4460-8192-80ced134a954",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K2Gqe68M4wgMDUxC3mVbEu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2045,
      "cache_creation_input_tokens": 2399,
      "cache_read_input_tokens": 86255,
      "output_tokens": 1064,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2399,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2045,
          "output_tokens": 1064,
          "cache_read_input_tokens": 86255,
          "cache_creation_input_tokens": 2399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2399
          },
          "type": "message"
        }
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

_source line 82 · 2026-05-17T07:11:17.522Z_

Now let me check the `---` (LaTeX em-dash encoding) count more thoroughly across all sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c1c21f5-7238-4460-8192-80ced134a954",
  "isSidechain": false,
  "requestId": "req_011Cb7ivnbR5Rb1LH8tP4db7",
  "type": "assistant",
  "uuid": "9ae541c8-6fd6-49f3-9834-379197a6777f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K2Gqe68M4wgMDUxC3mVbEu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2045,
      "cache_creation_input_tokens": 2399,
      "cache_read_input_tokens": 86255,
      "output_tokens": 1064,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2399,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2045,
          "output_tokens": 1064,
          "cache_read_input_tokens": 86255,
          "cache_creation_input_tokens": 2399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2399
          },
          "type": "message"
        }
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

_source line 83 · 2026-05-17T07:11:18.103Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Jd5taZ7picLGLmrxNhEWa1`</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ae541c8-6fd6-49f3-9834-379197a6777f",
  "isSidechain": false,
  "requestId": "req_011Cb7ivnbR5Rb1LH8tP4db7",
  "type": "assistant",
  "uuid": "4578349b-228b-455e-9f60-6f2a97716d37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K2Gqe68M4wgMDUxC3mVbEu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2045,
      "cache_creation_input_tokens": 2399,
      "cache_read_input_tokens": 86255,
      "output_tokens": 1064,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2399,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2045,
          "output_tokens": 1064,
          "cache_read_input_tokens": 86255,
          "cache_creation_input_tokens": 2399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2399
          },
          "type": "message"
        }
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

_source line 84 · 2026-05-17T07:11:19.384Z_

<details><summary>↩ Tool result · `toolu_01E3rr1KcEnewyMiT3ya9Z58`</summary>

```text
3:Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
7:Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8:\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models, separating quality estimation from best-of-$N$ selection and diagnosing why the former succeeds while the latter fails---within the dominant deployment paradigm for production NER.
12:Yet quality estimation does not translate to structural selection---the \textbf{correlation-selection gap} (the disparity between a signal's ability to rank instances reliably and its failure to select the best output within a single instance): structural best-of-$N$ selection matches or degrades greedy decoding ($T{=}0$) despite 12--14~pp oracle headroom.
13:The gap has two empirical causes: (a)~\textit{instance degeneracy}---fine-tuned models produce identical outputs for 10--58\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\rho{=}0.52$); and (b)~\textit{LP compression}---median within-instance range of 0.041 nats (\S\ref{sec:discussion}).
19:\caption{The correlation-selection gap. \textbf{Left}: consistency signals reliably predict instance-level quality ($\rho$ up to 0.45 on CoNLL, 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82). \textbf{Right}: quality estimation does not translate to selection---all methods approximately match greedy decoding ($T{=}0$) despite 13~pp oracle headroom (\S\ref{sec:discussion}).}
23:We evaluate five signals from three families---structural, surface, and model-internal---on SciERC \cite{luan2018scierc} as a primary medium-difficulty test bed, with Few-NERD \cite{ding2021fewnerd} (low-degeneracy contrast), CoNLL-2003 \cite{tjongkimsang2003conll} (ceiling-effect control), and WNUT-17 \cite{derczynski2017wnut} (signal-collapse boundary), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0942423c-ae6d-4ff1-9dfe-46d6e61717b2",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "336675ae-7f4f-43fe-84de-972376b7dc0e",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "3:Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \\citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \\cite{snell2025scaling, brown2024monkeys}.\n7:Existing self-consistency methods \\cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\n8:\\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models, separating quality estimation from best-of-$N$ selection and diagnosing why the former succeeds while the latter fails---within the dominant deployment paradigm for production NER.\n12:Yet quality estimation does not translate to structural selection---the \\textbf{correlation-selection gap} (the disparity between a signal's ability to rank instances reliably and its failure to select the best output within a single instance): structural best-of-$N$ selection matches or degrades greedy decoding ($T{=}0$) despite 12--14~pp oracle headroom.\n13:The gap has two empirical causes: (a)~\\textit{instance degeneracy}---fine-tuned models produce identical outputs for 10--58\\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\\rho{=}0.52$); and (b)~\\textit{LP compression}---median within-instance range of 0.041 nats (\\S\\ref{sec:discussion}).\n19:\\caption{The correlation-selection gap. \\textbf{Left}: consistency signals reliably predict instance-level quality ($\\rho$ up to 0.45 on CoNLL, 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82). \\textbf{Right}: quality estimation does not translate to selection---all methods approximately match greedy decoding ($T{=}0$) despite 13~pp oracle headroom (\\S\\ref{sec:discussion}).}\n23:We evaluate five signals from three families---structural, surface, and model-internal---on SciERC \\cite{luan2018scierc} as a primary medium-difficulty test bed, with Few-NERD \\cite{ding2021fewnerd} (low-degeneracy contrast), CoNLL-2003 \\cite{tjongkimsang2003conll} (ceiling-effect control), and WNUT-17 \\cite{derczynski2017wnut} (signal-collapse boundary), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).",
    "numLines": 7
  },
  "sourceToolAssistantUUID": "0942423c-ae6d-4ff1-9dfe-46d6e61717b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-17T07:11:18.126Z_

<details><summary>↩ Tool result · `toolu_01Jd5taZ7picLGLmrxNhEWa1`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:9
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:14
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex:2
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:2
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:55
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:7

Found 90 total occurrences across 7 files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4578349b-228b-455e-9f60-6f2a97716d37",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "c39f2a5f-c3ac-4537-9fd6-62995eaa60bb",
  "toolUseResult": {
    "mode": "count",
    "numFiles": 7,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:9\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:14\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex:1\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex:2\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:2\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:55\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:7",
    "numMatches": 90
  },
  "sourceToolAssistantUUID": "4578349b-228b-455e-9f60-6f2a97716d37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-17T07:11:18.720Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01FwpWw67TVdy5D263Wb6TRM`</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c39f2a5f-c3ac-4537-9fd6-62995eaa60bb",
  "isSidechain": false,
  "requestId": "req_011Cb7ivnbR5Rb1LH8tP4db7",
  "type": "assistant",
  "uuid": "c696e230-9575-4ea6-883b-73c91671a5c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K2Gqe68M4wgMDUxC3mVbEu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2045,
      "cache_creation_input_tokens": 2399,
      "cache_read_input_tokens": 86255,
      "output_tokens": 1064,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2399,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2045,
          "output_tokens": 1064,
          "cache_read_input_tokens": 86255,
          "cache_creation_input_tokens": 2399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2399
          },
          "type": "message"
        }
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

_source line 87 · 2026-05-17T07:11:18.730Z_

<details><summary>↩ Tool result · `toolu_01FwpWw67TVdy5D263Wb6TRM`</summary>

```text
3:We evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability, LP)---for quality estimation and sample selection on four NER benchmarks spanning a difficulty gradient, using 4B--8B models.
5:However, quality estimation does not translate to sample selection---the \textit{correlation-selection gap}: despite ${\sim}$13~pp oracle headroom, no signal consistently outperforms greedy decoding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c696e230-9575-4ea6-883b-73c91671a5c2",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "a68f00b5-75aa-4b84-a87b-1224e25262c2",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "3:We evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability, LP)---for quality estimation and sample selection on four NER benchmarks spanning a difficulty gradient, using 4B--8B models.\n5:However, quality estimation does not translate to sample selection---the \\textit{correlation-selection gap}: despite ${\\sim}$13~pp oracle headroom, no signal consistently outperforms greedy decoding.",
    "numLines": 2
  },
  "sourceToolAssistantUUID": "c696e230-9575-4ea6-883b-73c91671a5c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-17T07:11:19.370Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01E3rr1KcEnewyMiT3ya9Z58`</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a68f00b5-75aa-4b84-a87b-1224e25262c2",
  "isSidechain": false,
  "requestId": "req_011Cb7ivnbR5Rb1LH8tP4db7",
  "type": "assistant",
  "uuid": "0942423c-ae6d-4ff1-9dfe-46d6e61717b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K2Gqe68M4wgMDUxC3mVbEu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2045,
      "cache_creation_input_tokens": 2399,
      "cache_read_input_tokens": 86255,
      "output_tokens": 1064,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2399,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2045,
          "output_tokens": 1064,
          "cache_read_input_tokens": 86255,
          "cache_creation_input_tokens": 2399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2399
          },
          "type": "message"
        }
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

_source line 89 · 2026-05-17T07:11:19.499Z_

```json
{
  "parentUuid": "336675ae-7f4f-43fe-84de-972376b7dc0e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7a929269-fba6-47ee-bbf6-571ea42cac1c",
  "timestamp": "2026-05-17T07:11:19.499Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 90 · 2026-05-17T07:11:37.394Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the full review.

Key findings:
1. **Em-dash (---) usage**: 90 total occurrences across all sections (35 in main text excluding appendix). This is excessive and a known AI writing marker.
   - Abstract: 2 occurrences
   - Introduction: 7 occurrences  
   - Method: 1
   - Experiments: 9
   - Discussion: 14
   - Limitations: 2
   - Appendix: 55
   
The main body has roughly 35 instances, many serving as explanatory dashes which is characteristic of AI-generated text.

2. **Reference verification**: All 59 references check out as legitimate, with some "not found" results just being recent preprints that haven't been indexed yet.

3. **Missing references**: Byerly & Khashabi 2024 on self-consistency failures in long-context problems with correlated errors should have been cited but wasn't.

4. **Novelty assessment**: The correlation-selection gap is a useful conceptual contribution, though the paper is primarily a negative result, and the instance degeneracy concept feels somewhat underdeveloped.

5. **Writing quality**: The paper is technically dense and precise, though the Abstract and Introduction are heavy on numerical details.

Now I'm ready to compile the full review and send it to the Director.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a929269-fba6-47ee-bbf6-571ea42cac1c",
  "isSidechain": false,
  "requestId": "req_011Cb7ixNmkwGLcZCsVwoG6W",
  "type": "assistant",
  "uuid": "cb8aa733-e195-4464-bbdf-d81ff443eed9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBVy5AaXCuDNxDCDeaJvWK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4407,
      "cache_read_input_tokens": 88654,
      "output_tokens": 5417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5417,
          "cache_read_input_tokens": 88654,
          "cache_creation_input_tokens": 4407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4407
          },
          "type": "message"
        }
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

_source line 91 · 2026-05-17T07:11:37.497Z_

I now have sufficient information to compile the review. Let me write it up and post to the Director.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb8aa733-e195-4464-bbdf-d81ff443eed9",
  "isSidechain": false,
  "requestId": "req_011Cb7ixNmkwGLcZCsVwoG6W",
  "type": "assistant",
  "uuid": "61b0b799-677d-43d7-b2a2-4b00dba41258",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBVy5AaXCuDNxDCDeaJvWK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4407,
      "cache_read_input_tokens": 88654,
      "output_tokens": 5417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5417,
          "cache_read_input_tokens": 88654,
          "cache_creation_input_tokens": 4407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4407
          },
          "type": "message"
        }
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

_source line 92 · 2026-05-17T07:13:36.871Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01SA3vYQWveydDwmNHquCLwq`</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: \"Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\"\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## Summary (2-3 句)\n\n本文系统评估了五种置信度信号在 LLM-based NER 中的质量估计（QE）和样本选择表现，发现 QE 成功但 selection 失败，并将失败归因于 instance degeneracy 和 LP compression。这是一篇以诊断为核心的 negative result 论文，分析扎实但实际贡献偏向观察和归因，缺乏可操作的方法提出。\n\n---\n\n## Strengths (逐条)\n\n**S1. 问题 framing 清晰且有价值。** \"Correlation-selection gap\" 概念将两个通常被混淆的任务（QE vs. selection）明确分离，对该领域后续研究有 conceptual guidance 意义。\n\n**S2. 实验设计全面且系统。** 四个数据集构成 difficulty gradient（WNUT-17 → SciERC → Few-NERD → CoNLL），两个 model families + 4B ablation，$N$ 和 $T$ 的系统变化，三层诊断链（construction → degeneracy → compression），ablation 覆盖 LoRA rank、free-form decoding、entity-token LP、supervised verifier。\n\n**S3. 统计严谨性高。** 使用 paired sign tests、bootstrap CIs、Bonferroni correction、TOST equivalence testing。明确区分 \"absence of evidence\" 和 \"evidence of absence\"。多 seed 实验确认 ranking stability。\n\n**S4. Negative result 的论证逻辑完整。** 三层结构（by construction → degeneracy → compression）层层递进，supervised verifier baseline 确认 bottleneck 在 feature space 而非 aggregation，使负面结果具有诊断价值。\n\n**S5. Related work 覆盖面广。** 59 篇引用，覆盖 self-consistency、MBR decoding、uncertainty estimation、best-of-N、diversity collapse 等多个相关方向。与 Yao et al. (2026) 的区分清楚。\n\n---\n\n## Weaknesses (逐条)\n\n### Must-Fix 问题\n\n**W1** [Must-Fix] **核心概念 \"correlation-selection gap\" 的新颖性有限**\n\n- 具体位置：Section 1 (Introduction), Section 4.2\n- 问题：该 \"gap\" 本质上是一个已知的 observation 的 repackaging：instance-level signals 无法区分同一 input 的不同 outputs 是其定义的直接推论（论文自己称 \"by construction\"）；MBR 在 structured outputs 上失败已有文献指出 (Eikema et al., 2025)；fine-tuned models 的 diversity collapse 是 Kirk et al. (2024) 和 Yun et al. (2025) 的已知现象。\n- 论文的核心 insight 可以简化为：(1) instance-level signals 不能做 per-sample ranking（trivial by definition），(2) fine-tuned models 输出太一致（known），(3) LP 被 format tokens 压缩（specific but minor）。三者组合的诊断价值有余，但是否构成 EMNLP 主会议长文的贡献量存疑。\n- 为什么影响接收：如果核心 framing 被认为是重新包装已知观察，论文的 contribution bar 不够 main conference。\n- 建议修改方向：需要更清楚地 articulate 为什么诊断本身（而非解决方案）值得作为独立 contribution，或增加可操作的方法（如基于诊断设计的 targeted remedy）。\n\n**W2** [Must-Fix] **\"Instance degeneracy\" 作为概念贡献的独立性不足**\n\n- 具体位置：Section 5 (Discussion), Table 5\n- 问题：论文将 instance degeneracy 描述为 gap 的核心原因，但同时承认 \"the better the model, the less room for selection to add value\"（Section 5, line 15）。这使得 degeneracy 不是一个 \"failure mechanism\" 而是 model success 的 natural consequence。CoNLL 58% degeneracy 对应 91% F1——模型已经很好了，当然输出一致。Few-NERD 10% degeneracy 对应 75% F1——不是 degeneracy \"low\" 而是模型在该任务上 underfit。\n- 为什么影响接收：如果 degeneracy 是 model capability 的 trivial correlate，那 \"degeneracy gates LP selection\" 本质上等价于 \"LP selection only works when the model is bad enough to produce diverse wrong answers\"，这降低了发现的意义。\n- 建议修改方向：需要用 Few-NERD 的反例（75% F1 但仅 10% degeneracy）更有力地论证 degeneracy 不完全是 capability 的 proxy，进一步分析什么 dataset/task properties 独立于 capability 影响 degeneracy。\n\n**W3** [Must-Fix] **缺乏任何可操作的 positive contribution**\n\n- 具体位置：Section 6 (Conclusion), Section 5 (Discussion, \"Pilot remedy\")\n- 问题：论文的全部 takeaway 是 \"closing the gap requires trained verifiers\"（最后一句话 cite Cobbe et al., 2021），但：(a) 不训练 verifier，(b) 不提出新 signal，(c) entity-token LP 作为唯一 remedy 被证明失败。一篇纯诊断性论文在 EMNLP main conference 需要极强的 insight novelty 来补偿缺乏 actionable method 的问题。\n- 为什么影响接收：ARR 的 excitement 评分要求 \"I would mention this paper to others\"——一篇结论为 \"现有方法都不行，需要 future work\" 的论文很难达到这个 bar。\n- 建议修改方向：(1) 增加一个 lightweight trained verifier baseline 来验证诊断的 actionability，或 (2) 将论文定位为 Findings 而非 main conference。\n\n### Should-Fix 问题\n\n**W4** [Should-Fix] **LaTeX em-dash (`---`) 过度使用，存在 AI 写作风格痕迹**\n\n- 具体位置：全文，共 90 处（正文约 35 处，Appendix 55 处）\n- 问题：Abstract 2 处、Introduction 7 处、Experiments 9 处、Discussion 14 处。平均每段出现 1-2 个解释性 em-dash。例如：\n  - \"Self-consistency---majority voting over multiple samples---yields...\"（Introduction L3）\n  - \"quality estimation does not translate to sample selection---the correlation-selection gap\"（Abstract L5）\n  - \"fine-tuned models produce identical outputs for 10--58\\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation\"（Introduction L13）\n- 这是 AI 生成文本的典型标志，经验丰富的审稿人会注意到。正文部分至少应减少到 10 处以内。\n- 建议：用逗号、括号或拆分为两句替代大部分 em-dash。\n\n**W5** [Should-Fix] **Abstract 和 Introduction 过度堆砌数字，报告风格重于故事风格**\n\n- 具体位置：Abstract（10 行中包含约 15 个具体数字）、Introduction（contribution list）\n- 问题：Abstract 第 4 行 \"$\\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82\"；第 6 行 \"$\\rho{=}0.52$... 10--58\\%... median range 0.041 nats\"。读者在 30 秒内无法消化这些数字。Introduction 的 contribution list 同样堆砌了大量具体 $\\rho$ 和 pp 值。\n- 故事线（Why does SC fail for NER?）是有吸引力的，但被数字淹没了。\n- 建议：Abstract 中保留 2-3 个最关键的数字，其余用定性描述。Introduction contribution 中减少内嵌统计。\n\n**W6** [Should-Fix] **与 Yao et al. (2026) 的增量贡献需更明确的差异化**\n\n- 具体位置：Section 2 (Related Work, \"Consistency for structured IE\" paragraph)\n- 问题：论文承认 Yao et al. (2026) 已证明 consistency-accuracy correlation 存在。本文的 claimed extension 是 (1) fine-tuned models, (2) QE/selection 分离, (3) failure diagnosis。但 (1) 是实验设置变化而非方法贡献，(3) 的核心发现（degeneracy + compression）如 W1-W2 所述是较 predictable 的。\n- 建议：增加一个直接的 Table 或 Figure 对比 Yao et al. 的 setting/findings 与本文的差异。\n\n**W7** [Should-Fix] **Missing reference: Byerly & Khashabi (2024) \"Self-Consistency Falls Short\"**\n\n- 这是关于 self-consistency 失败模式的直接相关工作（arXiv:2411.01101），讨论了 correlated errors 导致 SC 失败的机制。本文的 \"instance degeneracy\" 与他们的 \"correlated errors from architectural biases\" 是相关的失败模式——应该引用并讨论区别。\n\n**W8** [Should-Fix] **Discussion section 过长，部分内容适合移入 Appendix**\n\n- 具体位置：Section 5，约占 2+ 页\n- 问题：\"Hypotheses for LP compression\"（4 个假设的列举）、\"Signal combinations\"（3 种策略均失败的报告）、\"Effect of sample count\" 和 \"Effect of sampling temperature\" 都是 robustness/ablation 内容，更适合 Appendix。Discussion 应聚焦 high-level implications。\n- 影响：可能导致正文超 8 页（需确认编译后页数）。\n\n### Minor 问题\n\n**M1** [Minor] Appendix L235 使用 \"leverage\"（AI 用词黑名单）：\"Structural signals leverage $\\binom{N}{2}$ pairwise comparisons\"。\n\n**M2** [Minor] Abstract 中 \"LP\" 首次出现时虽有括号解释 \"(log-probability, LP)\" 但 \"NER\" 和 \"MBR\" 未在 Abstract 内定义。\n\n**M3** [Minor] Table 3 (selection) 中 EM 和 VC 没有 $p$ 值，仅标 \"---\"，但 caption 说 \"$p$ vs. greedy baseline from paired sign tests\"——应解释为何省略。\n\n**M4** [Minor] Figure 2 caption 中 \"dashed line at ~15%\" 使用了 \"~\" 而非精确值——如果是 threshold claim 应提供更严格的定义。\n\n**M5** [Minor] `---` 在 LaTeX 中生成 em-dash 但 `--` 生成 en-dash。文中 \"4B--8B\" 和 \"10--58\\%\" 使用 `--` 是正确的数字范围标记，无需修改。但正文中大量 `---` 作为解释性 dash 应修改。\n\n---\n\n## Questions (需要作者澄清)\n\n**Q1.** Few-NERD 的低 degeneracy (10%) 和高 F1 (75%) 看似矛盾——是否因为 Few-NERD 有 8 个 entity types（vs. CoNLL 的 4 个）导致 output space 更大？如果是，这说明 degeneracy 主要是 output space size 的函数而非 model capability 的函数，这会影响整体叙事。\n\n**Q2.** LoRA rank=8 实验中 degeneracy 降到 7% 但 selection 仍然失败——这是否说明 degeneracy 实际上不是 \"gating factor\"？论文说 \"necessary but not sufficient\"，但如果 necessary condition met 后仍然失败，那 degeneracy 的解释力被高估了。\n\n**Q3.** 论文只在 4B-8B 范围测试——70B+ 模型是否会展现不同的 degeneracy 行为？如果更大模型 degeneracy 更高（符合 \"better model → more degenerate\" 逻辑），那整个 research direction（用 confidence signals 做 selection for structured IE）是否根本无望？\n\n**Q4.** Supervised verifier baseline 只使用了 5 个现有 signal 作为 features——如果加入 token-level features（如 entity-token LP 的分布统计）是否能 close gap？这个 baseline 的 feature space 可能太受限。\n\n---\n\n## Missing References\n\n1. **Byerly & Khashabi (2024)** \"Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems\" (arXiv:2411.01101) — 关于 SC 中 correlated errors 的失败模式分析\n2. **Sequence labeling calibration** — 未见 CRF-based calibration 的经典工作如 Lafferty et al. (2001) 或近年 neural CRF calibration 论文\n3. **Diversity-promoting decoding** — Vijayakumar et al. (2016) \"Diverse Beam Search\" 等多样性解码方法作为 degeneracy 的潜在缓解手段应被讨论\n\n---\n\n## Detailed Comments (逐节)\n\n**Abstract**: 信息过密，15+ 个数字在 10 行内。\"four instance-level... and one per-sample\" 的分类是有效的叙事元素，但后续数字堆砌削弱了可读性。\n\n**Introduction**: 结构完整（背景 → 问题 → 已有不足 → 本文 → 贡献），符合 5 段要求。但 contribution list 中 (2) 和 (3) 有重叠——degeneracy 既是 gap 的原因（contribution 2）又是 regime boundary（contribution 3）。\n\n**Related Work**: 组织良好，四个 paragraph 主题清晰。与 Yao et al. (2026) 的定位合理但可更具体。\n\n**Method**: 公式化清晰，SJ 的定义（Eq. 4）和 instance-level vs. per-sample 的区分是有价值的 methodological contribution。\n\n**Experiments**: 系统性强，Table 1-4 信息密度高。Few-NERD 的 cross-dataset contrast 是最有说服力的部分。\n\n**Discussion**: 内容丰富但过长。\"Why the gap exists\" paragraph 是核心，后续 ablations 重复论证可压缩。\n\n**Conclusion**: 过于简短（10 行），未讨论 broader implications。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 实验设计严谨，统计方法正确，ablations 充分。唯一扣分点：degeneracy 作为 causal mechanism 的论证有循环性（W2）。 |\n| Excitement | 2.5/5 | 问题有趣但结论是 negative result + \"需要 future work\"。缺乏可操作的 positive contribution（W3）。对领域的 guidance 价值有限——告诉人们\"别用 unsupervised signals 做 selection\"但不提供替代方案。 |\n| Reproducibility | 4/5 | 模型、数据集均公开，超参数详细，承诺 code release。Qwen3-8B thinking token confound 有透明披露。 |\n| Overall Assessment | 3/5 (Findings) | 分析质量高但 contribution bar 不够 main conference。适合 Findings。 |\n\n---\n\n## Overall Score\n\n**Borderline reject (leaning Findings)**\n\n这是一篇 well-executed 的实证分析论文，统计严谨性和实验覆盖度都很高。但作为 EMNLP 主会议长文，核心贡献（\"诊断为什么 SC 在 NER 上不行\"）的 novelty 和 actionability 不足：\n- \"correlation-selection gap\" 的两个主要原因分别是 definitional (instance-level signals can't rank by construction) 和 known (fine-tuned models collapse diversity)\n- LP compression 是 specific 且 interesting 的发现，但实际意义有限（即使在 non-tied subset 上 LP 也只 +2.9 pp）\n- 没有 positive method contribution\n\n如果补充 (1) 一个 lightweight trained verifier 证明诊断的 actionability，或 (2) 更深入分析 degeneracy 的 non-trivial determinants（beyond model capability），可以升至 weak accept。\n\n## Confidence\n**4/5** — 我仔细阅读了全文包括 appendix 的关键部分，对 MBR decoding 和 uncertainty estimation 文献有较好了解。对 Few-NERD 数据集的具体 entity type 分布不够熟悉。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61b0b799-677d-43d7-b2a2-4b00dba41258",
  "isSidechain": false,
  "requestId": "req_011Cb7ixNmkwGLcZCsVwoG6W",
  "type": "assistant",
  "uuid": "7c1c841f-e974-4c10-8593-04b90e987563",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBVy5AaXCuDNxDCDeaJvWK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4407,
      "cache_read_input_tokens": 88654,
      "output_tokens": 5417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5417,
          "cache_read_input_tokens": 88654,
          "cache_creation_input_tokens": 4407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4407
          },
          "type": "message"
        }
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

_source line 93_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 完整性 + 写作质量**  ### Venue 信息 - 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - 截止日期: 2026-05-25 - 页数限制: 长文 8 页正文（Limitations/Ethics…",
  "leafUuid": "7c1c841f-e974-4c10-8593-04b90e987563",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Runtime record

_source line 94_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper for EMNLP 2026",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Tool result

_source line 95 · 2026-05-17T07:13:40.633Z_

<details><summary>↩ Tool result · `toolu_01SA3vYQWveydDwmNHquCLwq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c1c841f-e974-4c10-8593-04b90e987563",
  "isSidechain": false,
  "promptId": "0aec64fa-df18-4d86-b7eb-e3c117a67d77",
  "type": "user",
  "uuid": "f763bb3a-f218-4994-9046-710414241bbb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "7c1c841f-e974-4c10-8593-04b90e987563",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 96_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper for EMNLP 2026",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Runtime record

_source line 97 · 2026-05-17T07:15:07.058Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T07:15:07.058Z",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "content": "[Round 1 审稿请求]:\n## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Weakness 和 Question 标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供具体证据，cite 论文中的 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 完整审稿意见\n\n**Overall Score**: Borderline Accept (3.5/5)\n**Confidence**: 4/5\n\n**Strengths**:\nS1. 问题定义清晰且有贡献——\"correlation-selection gap\" 概念化有价值\nS2. 实验设计的系统性——4 NER benchmarks 构成 difficulty gradient\nS3. 统计方法论上佳——Bootstrap CI、paired sign test、TOST、Bonferroni、Kendall's W\nS4. 三层诊断结构有说服力——construction → degeneracy → compression\nS5. 负面结果的审慎表达——\"inversely associated with\" 而非 \"causes\"\nS6. Appendix 丰富且组织有序\n\n**Weaknesses**:\n\n**W1 [Must-Fix]** 跨数据集 degeneracy 梯度的因果推断基础薄弱 (n=3)。三个数据点单调排列概率 1/6。Entity-type-level analysis (n=8, ρ=-0.881, p=0.004) 存在独立性违反。Figure 3 的 pooled correlation (ρ=-0.57, p=0.066, n=11) 混合了两个粒度的观测，统计上有问题。建议增加 2-3 个数据集。\n\n**W2 [Must-Fix]** LoRA rank=8 ablation 的 \"necessary but not sufficient\" claim 存在混淆变量。Rank=8 同时降低了 model capability (greedy F1: 0.645→0.640)、改变了 representation space。LP compression 可能因 model capability 下降而加剧。Few-NERD 10% degeneracy → LP works, rank=8 SciERC 7.2% degeneracy → LP fails 的矛盾未充分解释。\n\n**W3 [Should-Fix]** 负面结果缺少 power analysis。n=529、2 seeds 下检测 1pp 效应的 power 未报告。TOST 的 internal anchor δ=2pp 可能过宽。\n\n**W4 [Should-Fix]** \"Compression is model-intrinsic\" 与 RE free-form results 矛盾。RE free-form decoding 恢复了 LP selection (+2.35pp, p=0.025)，但 Abstract/Introduction 中未 qualify。\n\n**W5 [Should-Fix]** Selection 实验 seed coverage 有限（QE 1 seed, selection 2 seeds）。Few-NERD 核心结果 (LP +1.36pp) 是 1-seed result。\n\n**W6 [Should-Fix]** Few-NERD 训练仅 3 epochs (vs 其他 5 epochs) 可能 confound degeneracy 比较。Under-training → lower degeneracy → 无法区分 dataset effect 和 training effect。\n\n**W7 [Minor]** SJ normalizer claim \"Δρ<0.01\" 措辞精度可改进（实际最大差异 0.009）。\n\n**W8 [Minor]** Table 3 vs Table 4 的 greedy F1 不一致（gold-filtered vs full-set）可能困惑读者。\n\n**Questions**:\nQ1. LoRA rank=8 下 LP 的 median within-instance range 是多少？compression 是否更严重？\nQ2. Few-NERD 训练为何仅 3 epochs？5 epochs 下 degeneracy 是多少？\nQ3. Table 3 sign test 是 instance-level 配对还是 corpus-level？\nQ4. Within-instance SJ-F1 ρ=0.52 的 distribution？多少比例 non-degenerate instances 有 ρ<0？\nQ5. Entity-type-level 分析是否控制了 entity type frequency / average entity count 作为 confound？\n\n**Missing References**: Lightman et al. (2024)、Yoran et al. (2023)、Zhang et al. (2024) DeepMind test-time compute、Eikema et al. (2025) structured MBR\n\n**官方维度打分**: Soundness 3.5/5, Excitement 3.5/5, Reproducibility 4/5\n\n---\n\n请对 W1-W8、Q1-Q5 逐条回应。"
}
```

---

### Runtime record

_source line 98 · 2026-05-17T07:15:07.058Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T07:15:07.058Z",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

## Round 2

2 recorded events

### User

_source line 99 · 2026-05-17T07:15:07.049Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f763bb3a-f218-4994-9046-710414241bbb",
  "isSidechain": false,
  "promptId": "06fb4f38-4b27-4058-9b82-bbbbdb46c0d4",
  "type": "user",
  "isMeta": true,
  "uuid": "3b937f7e-0ed9-4660-a2c8-2aace557ad39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 100 · 2026-05-17T07:15:07.049Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b937f7e-0ed9-4660-a2c8-2aace557ad39",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "543cb0e0-f95d-442f-a7c0-bc61c8be05aa",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "fe269a19-16ac-44cc-8a44-5ef9b8288ce6",
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

25 recorded events

### User

_source line 101 · 2026-05-17T07:15:07.134Z_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Weakness 和 Question 标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供具体证据，cite 论文中的 Section/Table/Figure）。

---

### Reviewer 1 完整审稿意见

**Overall Score**: Borderline Accept (3.5/5)
**Confidence**: 4/5

**Strengths**:
S1. 问题定义清晰且有贡献——"correlation-selection gap" 概念化有价值
S2. 实验设计的系统性——4 NER benchmarks 构成 difficulty gradient
S3. 统计方法论上佳——Bootstrap CI、paired sign test、TOST、Bonferroni、Kendall's W
S4. 三层诊断结构有说服力——construction → degeneracy → compression
S5. 负面结果的审慎表达——"inversely associated with" 而非 "causes"
S6. Appendix 丰富且组织有序

**Weaknesses**:

**W1 [Must-Fix]** 跨数据集 degeneracy 梯度的因果推断基础薄弱 (n=3)。三个数据点单调排列概率 1/6。Entity-type-level analysis (n=8, ρ=-0.881, p=0.004) 存在独立性违反。Figure 3 的 pooled correlation (ρ=-0.57, p=0.066, n=11) 混合了两个粒度的观测，统计上有问题。建议增加 2-3 个数据集。

**W2 [Must-Fix]** LoRA rank=8 ablation 的 "necessary but not sufficient" claim 存在混淆变量。Rank=8 同时降低了 model capability (greedy F1: 0.645→0.640)、改变了 representation space。LP compression 可能因 model capability 下降而加剧。Few-NERD 10% degeneracy → LP works, rank=8 SciERC 7.2% degeneracy → LP fails 的矛盾未充分解释。

**W3 [Should-Fix]** 负面结果缺少 power analysis。n=529、2 seeds 下检测 1pp 效应的 power 未报告。TOST 的 internal anchor δ=2pp 可能过宽。

**W4 [Should-Fix]** "Compression is model-intrinsic" 与 RE free-form results 矛盾。RE free-form decoding 恢复了 LP selection (+2.35pp, p=0.025)，但 Abstract/Introduction 中未 qualify。

**W5 [Should-Fix]** Selection 实验 seed coverage 有限（QE 1 seed, selection 2 seeds）。Few-NERD 核心结果 (LP +1.36pp) 是 1-seed result。

**W6 [Should-Fix]** Few-NERD 训练仅 3 epochs (vs 其他 5 epochs) 可能 confound degeneracy 比较。Under-training → lower degeneracy → 无法区分 dataset effect 和 training effect。

**W7 [Minor]** SJ normalizer claim "Δρ<0.01" 措辞精度可改进（实际最大差异 0.009）。

**W8 [Minor]** Table 3 vs Table 4 的 greedy F1 不一致（gold-filtered vs full-set）可能困惑读者。

**Questions**:
Q1. LoRA rank=8 下 LP 的 median within-instance range 是多少？compression 是否更严重？
Q2. Few-NERD 训练为何仅 3 epochs？5 epochs 下 degeneracy 是多少？
Q3. Table 3 sign test 是 instance-level 配对还是 corpus-level？
Q4. Within-instance SJ-F1 ρ=0.52 的 distribution？多少比例 non-degenerate instances 有 ρ<0？
Q5. Entity-type-level 分析是否控制了 entity type frequency / average entity count 作为 confound？

**Missing References**: Lightman et al. (2024)、Yoran et al. (2023)、Zhang et al. (2024) DeepMind test-time compute、Eikema et al. (2025) structured MBR

**官方维度打分**: Soundness 3.5/5, Excitement 3.5/5, Reproducibility 4/5

---

请对 W1-W8、Q1-Q5 逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "543cb0e0-f95d-442f-a7c0-bc61c8be05aa",
  "isSidechain": false,
  "promptId": "06fb4f38-4b27-4058-9b82-bbbbdb46c0d4",
  "type": "user",
  "uuid": "49da2a79-6be6-445e-83f5-c5bbbea9e98e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 102 · 2026-05-17T07:16:08.663Z_

<details><summary>Logged reasoning block</summary>

```text
The Director is asking me to respond to Reviewer 1's review by going through each weakness (W1-W8) and question (Q1-Q5), marking each as [AGREE] or [REBUT] with evidence from the paper.

Let me carefully analyze each point:

**W1**: Cross-dataset degeneracy gradient causal inference is weak (n=3). Entity-type-level analysis (n=8) has independence violations. Pooled correlation mixes granularities.

Looking at the paper:
- Section 4.3 (experiments.tex line 166): "The pooled Spearman correlation (ρ=−0.57, p=0.066, n=11) treats dataset-level and entity-type-level points as independent; the entity-type-level evidence alone provides stronger grounding (ρ=−0.881, p=0.004, n=8)."


- The paper already acknowledges the pooled correlation problem and explicitly prioritizes the entity-type analysis. The n=3 dataset-level ordering has low statistical power, but the n=8 entity-type analysis within Few-NERD is more robust—though the reviewer's concern about shared model and pipeline dependencies across entities within the same dataset is valid. The paper does recognize these limitations by emphasizing the stronger entity-type evidence.
- I'm partially agreeing with R1 here. The statistical concerns are legitimate, but the paper already hedges appropriately, and the LoRA ablation provides converging evidence for the direction. Adding 2-3 more datasets would strengthen the claim, but it's not essential given the existing support.
- Now looking at W2's concern about the LoRA rank=8 ablation. The issue is that reducing rank confounds two effects: it lowers both capability and degeneracy. The Few-NERD results show that rank=8 enables LP to work at 10%, but in SciERC at rank=8 with 7.2% degeneracy, LP still fails compared to greedy. This apparent contradiction suggests the confound is real—lower rank doesn't simply solve the selection problem.
- The paper argues that degeneracy is necessary but not sufficient, pointing to LP signal quality differences (Few-NERD ρ=0.42 vs SciERC ρ=0.205). But this raises a deeper question: what actually determines LP signal quality? The confound remains unresolved because the paper doesn't measure within-instance variance or correlation metrics at rank=8, so I can't tell if the worse LP performance stems from representation changes or something else entirely.

**W3**: Power analysis is genuinely missing. With n=529 SciERC instances and only 2 seeds, detecting a 1pp effect is underpowered. The paper does have the high-powered Few-NERD result (n=32,565) as a positive case, and it invokes TOST equivalence testing and the caveat about absence of evidence in the appendix, but a formal power calculation for SciERC would make the negative claim much more defensible. I partially agree this is a valid methodological gap, though not fatal given the multi-dataset approach.

**W4**: The compression claim needs nuance. For NER tasks like SciERC, the effect does appear model-intrinsic—removing grammar constraints barely shifts the LP distributions. But for RE, removing format constraints actually restores LP selection with a +2.35pp bootstrap mean (95% CI [+0.24, +4.50], p=0.025), suggesting the compression there is partly driven by the output format rather than being purely intrinsic to the model. So the paper's distinction between task types holds up, though it's not as clean as "compression is always model-intrinsic."

**W5**: The Few-NERD result is underpowered—that +1.36pp gain comes from just a single seed run, whereas the main experiments use 3 seeds with tight variance bounds (σ≤0.026). This single-seed result doesn't have the same stability guarantees as the multi-seed findings elsewhere.

Actually, wait—I'm reconsidering. The p<0.001 significance for Few-NERD isn't about seed replication; it's from a paired statistical test across 32,565 instances within that one seed. With that many instances, the within-seed result has enormous statistical power, so the single seed doesn't undermine the validity of the test itself. The seeds are meant to check replication stability, but instance-level testing with n=32,565 is already well-powered. I think R1 may be conflating seed-level replication with instance-level statistical testing—these are different things. I should push back on this concern.

Now for the epoch count issue: the paper states all models were trained for 5 epochs with identical procedures, but R1 is claiming Few-NERD used only 3 epochs. I don't see evidence of this in what I've reviewed so far, so either it's in a section I haven't checked or R1 is mistaken about this detail. I see the main text specifies 5 epochs uniformly across datasets, though R1 might be referencing something in the appendix I haven't verified—the concern about training epochs as a confound is methodologically sound regardless. For W7, the SJ normalizer claim of Δρ<0.01 is technically correct since the actual maximum is 0.009, though it could be stated more precisely—I'll agree this is minor. On W8, I'm noticing the greedy F1 scores differ between tables: Table 3 shows 0.645 for SciERC with n=529 (gold-filtered), while Table 4 shows 0.614 for the same dataset with n=551 (full set), which suggests the filtering methodology is creating the discrepancy.

The paper does address this in a footnote explaining the difference stems from full-set versus filtered evaluation, so the explanation exists but could be more visible to readers. Looking at the remaining questions: the LoRA rank=8 LP median range appears to be unreported data, the sign test is indeed instance-level paired comparison as stated in the paper, and the within-instance SJ-F1 correlation distribution at ρ=0.52 isn't reported in the materials I can access.

Entity-type frequency as a potential confound is a valid concern that the paper doesn't explicitly address. Now I'm pulling together my full response to these points.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49da2a79-6be6-445e-83f5-c5bbbea9e98e",
  "isSidechain": false,
  "requestId": "req_011Cb7jFA5VpXigCQKKwD3F7",
  "type": "assistant",
  "uuid": "3aefaf98-8221-4127-9a7b-675eb3a28f80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VW16oVZUZL88mRESrRTgty",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1322,
      "cache_read_input_tokens": 98549,
      "output_tokens": 2674,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2674,
          "cache_read_input_tokens": 98549,
          "cache_creation_input_tokens": 1322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1322
          },
          "type": "message"
        }
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

_source line 103 · 2026-05-17T07:16:09.639Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Vmvn5ixth6YJkYXkrYX1kn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 100,
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3aefaf98-8221-4127-9a7b-675eb3a28f80",
  "isSidechain": false,
  "requestId": "req_011Cb7jFA5VpXigCQKKwD3F7",
  "type": "assistant",
  "uuid": "a0faa95e-bd20-4ad2-b72d-6eb15806261a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VW16oVZUZL88mRESrRTgty",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1322,
      "cache_read_input_tokens": 98549,
      "output_tokens": 2674,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2674,
          "cache_read_input_tokens": 98549,
          "cache_creation_input_tokens": 1322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1322
          },
          "type": "message"
        }
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

_source line 104 · 2026-05-17T07:16:09.653Z_

<details><summary>↩ Tool result · `toolu_01Vmvn5ixth6YJkYXkrYX1kn`</summary>

```text
100	\centering
101	\small
102	\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}
103	\label{tab:fk_independence}
104	\begin{tabular}{lrcccc}
105	\toprule
106	Config & $n$ & FK mean & 95\% CI & $t$ & Split-half $r$ \\
107	\midrule
108	SciERC (Qwen) & 529 & 0.402 & [0.376, 0.428] & 30.8 & 0.395 \\
109	CoNLL (LLaMA) & 2{,}756 & 0.927 & [0.919, 0.935] & 225.9 & 0.578 \\
110	CoNLL (Qwen) & 2{,}756 & 0.720 & [0.706, 0.734] & 102.1 & 0.520 \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	Table~\ref{tab:fk_independence} reports the results.
116	All configurations reject the independence null at $p{<}0.001$ ($n{=}529$--$2{,}756$), confirming that FK captures genuine inter-sample agreement rather than chance label co-occurrence.
117	Split-half reliability ranges from $r{=}0.395$ (SciERC) to $r{=}0.578$ (CoNLL LLaMA), indicating moderate stability: FK estimates from half the samples correlate positively with those from the other half, though the SciERC value suggests noisier estimation on harder tasks with fewer samples.
118	The higher FK means on CoNLL ($0.720$--$0.927$) vs.\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.
119	
120	\section{Calibration Analysis}\label{app:calibration}
121	
122	\begin{figure*}[t]
123	\centering
124	\includegraphics[width=\textwidth]{fig_reliability}
125	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
126	\label{fig:reliability}
127	\end{figure*}
128	
129	Reliability diagrams use 10 equal-width bins.
130	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
131	
132	\section{Additional Analyses}\label{app:additional}
133	
134	\begin{figure*}[t]
135	\centering
136	\includegraphics[width=\textwidth]{fig_signal_heatmap}
137	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
138	\label{fig:signal_heatmap}
139	\end{figure*}
140	
141	\paragraph{Per-relation diagnostic.}
142	RE signal degradation is relation-specific.
143	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
144	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
145	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
146	
147	\paragraph{Capability stratification.}
148	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
149	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
150	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
151	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
152	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
153	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
154	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
155	
156	\paragraph{Length vs.\ log-probability.}
157	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
158	
159	\begin{figure}[t]
160	\centering
161	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
162	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
163	\label{fig:length_logprob_scatter}
164	\end{figure}
165	
166	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
167	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
168	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
169	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, making the two selection rules equivalent.
170	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
171	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
172	Evaluation circularity is negligible.
173	
174	\paragraph{SJ normalizer robustness.}
175	Equation~\ref{eq:sj} uses $\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \cup g_j|$.
176	Table~\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\Delta\rho|{<}0.01$ in every case, confirming that the choice between max and union normalization does not affect conclusions.
177	
178	\begin{table}[h]
179	\centering
180	\small
181	\caption{SJ normalizer comparison (Spearman $\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\max(|g_i|,|g_j|)$; Union: $|g_i \cup g_j|$.}
182	\label{tab:sj_normalizer}
183	\begin{tabular}{@{}ll ccc@{}}
184	\toprule
185	Dataset & Model & $\rho$(max) & $\rho$(union) & $\Delta\rho$ \\
186	\midrule
187	CoNLL & Qwen3-8B & .436 & .438 & $-$.002 \\
188	CoNLL & Qwen3-4B & .422 & .421 & $+$.000 \\
189	CoNLL & LLaMA-8B & .431 & .432 & $-$.000 \\
190	SciERC & Qwen3-8B & .360 & .365 & $-$.005 \\
191	SciERC & Qwen3-4B & .422 & .423 & $-$.001 \\
192	SciERC & LLaMA-8B & .363 & .372 & $-$.009 \\
193	\bottomrule
194	\end{tabular}
195	\end{table}
196	
197	\paragraph{Conditional filtering details.}
198	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\Delta\rho{=}{-}0.005$, $p{=}0.53$; preliminary).
199	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
200	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
201	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
202	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
203	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
204	
205	\paragraph{WNUT-17 full signal analysis.}
206	Table~\ref{tab:wnut} (\S\ref{sec:qe_results}) reports all five signals on WNUT-17 with full-set and conditional $\rho$.
207	The full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.
208	VC's high full-set $\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, $p{=}0.49$), while LP's conditional $\rho{=}0.350$ is the highest among all signals on the non-zero subset, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
209	
210	\paragraph{Cross-configuration selection analysis.}
211	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
212	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
213	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (single-sample F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
214	
215	\begin{table*}[t]
216	\centering
217	\small
218	\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
219	\label{tab:cross_selection}
220	\begin{tabular}{llccccccc}
221	\toprule
222	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
223	\midrule
224	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
225	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
226	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
227	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
228	\bottomrule
229	\end{tabular}
230	\end{table*}
231	
232	\paragraph{Diminishing returns of $N$-scaling.}
233	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
234	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
235	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
236	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
237	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
238	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
239	
240	\paragraph{$N{=}16$ CoNLL selection: small but significant.}
241	While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.
242	VC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
243	These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
244	This reinforces the primary finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.
245	
246	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
247	
248	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
249	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0faa95e-bd20-4ad2-b72d-6eb15806261a",
  "isSidechain": false,
  "promptId": "06fb4f38-4b27-4058-9b82-bbbbdb46c0d4",
  "type": "user",
  "uuid": "d7ff8d71-673c-4986-b6d8-af08106bcc43",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\centering\n\\small\n\\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}\n\\label{tab:fk_independence}\n\\begin{tabular}{lrcccc}\n\\toprule\nConfig & $n$ & FK mean & 95\\% CI & $t$ & Split-half $r$ \\\\\n\\midrule\nSciERC (Qwen) & 529 & 0.402 & [0.376, 0.428] & 30.8 & 0.395 \\\\\nCoNLL (LLaMA) & 2{,}756 & 0.927 & [0.919, 0.935] & 225.9 & 0.578 \\\\\nCoNLL (Qwen) & 2{,}756 & 0.720 & [0.706, 0.734] & 102.1 & 0.520 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:fk_independence} reports the results.\nAll configurations reject the independence null at $p{<}0.001$ ($n{=}529$--$2{,}756$), confirming that FK captures genuine inter-sample agreement rather than chance label co-occurrence.\nSplit-half reliability ranges from $r{=}0.395$ (SciERC) to $r{=}0.578$ (CoNLL LLaMA), indicating moderate stability: FK estimates from half the samples correlate positively with those from the other half, though the SciERC value suggests noisier estimation on harder tasks with fewer samples.\nThe higher FK means on CoNLL ($0.720$--$0.927$) vs.\\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, making the two selection rules equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{SJ normalizer robustness.}\nEquation~\\ref{eq:sj} uses $\\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \\cup g_j|$.\nTable~\\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\\Delta\\rho|{<}0.01$ in every case, confirming that the choice between max and union normalization does not affect conclusions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SJ normalizer comparison (Spearman $\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\\max(|g_i|,|g_j|)$; Union: $|g_i \\cup g_j|$.}\n\\label{tab:sj_normalizer}\n\\begin{tabular}{@{}ll ccc@{}}\n\\toprule\nDataset & Model & $\\rho$(max) & $\\rho$(union) & $\\Delta\\rho$ \\\\\n\\midrule\nCoNLL & Qwen3-8B & .436 & .438 & $-$.002 \\\\\nCoNLL & Qwen3-4B & .422 & .421 & $+$.000 \\\\\nCoNLL & LLaMA-8B & .431 & .432 & $-$.000 \\\\\nSciERC & Qwen3-8B & .360 & .365 & $-$.005 \\\\\nSciERC & Qwen3-4B & .422 & .423 & $-$.001 \\\\\nSciERC & LLaMA-8B & .363 & .372 & $-$.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\\Delta\\rho{=}{-}0.005$, $p{=}0.53$; preliminary).\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} (\\S\\ref{sec:qe_results}) reports all five signals on WNUT-17 with full-set and conditional $\\rho$.\nThe full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.\nVC's high full-set $\\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, $p{=}0.49$), while LP's conditional $\\rho{=}0.350$ is the highest among all signals on the non-zero subset, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn CoNLL, 57--88\\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (single-sample F1 ${\\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \\textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\paragraph{$N{=}16$ CoNLL selection: small but significant.}\nWhile quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.\nVC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).\nThese gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\\% of the available headroom.\nThis reinforces the primary finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.",
      "numLines": 150,
      "startLine": 100,
      "totalLines": 1183
    }
  },
  "sourceToolAssistantUUID": "a0faa95e-bd20-4ad2-b72d-6eb15806261a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 105_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见  以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Weakness 和 Question 标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供具体证据，cite 论文中的 Section/Table/Figure）。  ---  ### Reviewe…",
  "leafUuid": "d7ff8d71-673c-4986-b6d8-af08106bcc43",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Runtime record

_source line 106_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper for EMNLP 2026",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Tool call

_source line 107 · 2026-05-17T07:16:14.349Z_

<details open><summary>🔧 Tool call — Read · `toolu_015jY617mNDpr9rXPoKzieKr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 340,
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7ff8d71-673c-4986-b6d8-af08106bcc43",
  "isSidechain": false,
  "requestId": "req_011Cb7jKmekdtZ7f1uy47xYJ",
  "type": "assistant",
  "uuid": "12bf0d35-ed0e-46ef-9291-1da68638b216",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016HoL29Ue8FZDm62YizPg7F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7871,
      "cache_read_input_tokens": 99871,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7871,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 99871,
          "cache_creation_input_tokens": 7871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7871
          },
          "type": "message"
        }
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

_source line 108 · 2026-05-17T07:16:14.360Z_

<details><summary>↩ Tool result · `toolu_015jY617mNDpr9rXPoKzieKr`</summary>

```text
340	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
341	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
342	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
343	
344	\begin{table}[t]
345	\centering
346	\small
347	\caption{TOST equivalence testing: signals vs.\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ single-sample).}
348	\label{tab:tost}
349	\begin{tabular}{l cccc cccc}
350	\toprule
351	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
352	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
353	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
354	\midrule
355	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
356	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
357	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
358	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
359	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
360	\bottomrule
361	\end{tabular}
362	\end{table}
363	
364	\paragraph{External equivalence margins.}
365	The oracle-headroom anchors above introduce circularity, as a reviewer correctly noted: $\delta$ is calibrated against the very quantity it contextualizes.
366	To resolve this, we supplement with three externally grounded margins:
367	(1) $\delta_{\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), representing measurement noise;
368	(2) $\delta_{\mathrm{practical}}{=}0.5$~pp, reflecting the threshold below which NER differences are considered negligible \cite{ratinov2009design};
369	(3) $\delta_{\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \cite{bergkirkpatrick2012empirical}.
370	
371	Results under these external anchors diverge sharply by configuration.
372	On LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\Delta|{\leq}0.1$~pp) and tight CIs at this sample size.
373	On Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, exceeding even $\delta_{\mathrm{literature}}$.
374	On SciERC NER ($n{=}529$), only SJ passes at $\delta_{\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.
375	These external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.
376	
377	\paragraph{Multiple comparison considerations.}\label{app:multiple_comparisons}
378	Our primary selection analysis involves ${\sim}$20 comparisons (5 signals $\times$ 3--4 configurations).
379	Since all primary selection results are non-significant ($p{>}0.05$), applying Benjamini-Hochberg correction can only make these results more conservative, strengthening the ``no signal beats greedy'' conclusion.
380	The sole positive finding---non-tied LP subset ($+2.9$~pp, $p{=}0.004$; \S\ref{sec:discussion})---survives Bonferroni correction over 5 signal comparisons ($p_{\mathrm{adj}}{=}0.020 < 0.05$), as noted in the main text footnote.
381	For quality estimation signal rankings, differences between the top signals (e.g., VC vs.\ SJ on SciERC) should be interpreted as descriptive rather than as statistically confirmed orderings, given the limited power of 3-seed comparisons.
382	
383	\section{Multi-Seed Stability}\label{app:multiseed}
384	
385	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
386	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).
387	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.
388	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
389	
390	\begin{table}[t]
391	\centering
392	\small
393	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
394	\label{tab:multiseed}
395	\begin{tabular}{lccccc}
396	\toprule
397	& LP & FK & SJ & VC & EM \\
398	\midrule
399	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
400	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
401	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
402	\midrule
403	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
404	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
405	\midrule
406	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
407	Qwen & .579${\pm}$.008 & .600${\pm}$.016 & .659${\pm}$.016 & .677${\pm}$.011 & .631${\pm}$.013 \\
408	LLaMA & .565${\pm}$.008 & .593${\pm}$.006 & .632${\pm}$.012 & .673${\pm}$.009 & .606${\pm}$.005 \\
409	\bottomrule
410	\end{tabular}
411	\end{table}
412	
413	\section{Training Configuration}\label{app:training}
414	
415	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
416	
417	\begin{table}[t]
418	\centering
419	\small
420	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
421	\label{tab:training}
422	\begin{tabular}{ll}
423	\toprule
424	Parameter & Value \\
425	\midrule
426	LoRA rank / $\alpha$ & 32 / 64 \\
427	LoRA target & All linear modules \\
428	LoRA dropout & 0 \\
429	Optimizer & AdamW \\
430	Learning rate & 2e-4, cosine schedule \\
431	Warmup ratio & 0.1 \\
432	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
433	Epochs & 5 \\
434	Max sequence length & 2048 \\
435	Precision & bf16 \\
436	Gradient checkpointing & Enabled \\
437	Max gradient norm & 1.0 \\
438	Training seed & 42 \\
439	Framework & LLaMA Factory \\
440	\midrule
441	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
442	SciERC split & 1861 / 275 / 551 \\
443	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
444	& eval\_steps${=}$200, save\_limit${=}$5 \\
445	\bottomrule
446	\end{tabular}
447	\end{table}
448	
449	\paragraph{Prompt template.}
450	For NER, we use a structured prompt:
451	\begin{quote}
452	\small
453	\texttt{System:} You are an expert in Named Entity Recognition.\\
454	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
455	Text: \texttt{\{input\_text\}}\\
456	Entity types: \texttt{\{schema\_types\}}
457	\end{quote}
458	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
459	
460	\paragraph{Constrained decoding.}
461	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
462	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
463	
464	\section{Thinking Token Impact Analysis}\label{app:thinking_token}
465	
466	Qwen3-8B's SciERC checkpoint was trained with empty \texttt{&lt;think>&lt;/think>} blocks prepended to each response (\S\ref{sec:setup}).
467	We quantify the potential impact on LP scores through three complementary arguments.
468	
469	\paragraph{LP shift magnitude.}
470	Empty thinking tokens (mean 4.5 per sample) constitute 2.1\% of tokens on SciERC.
471	The estimated LP shift is 0.001 nats per token (2.68\% of the median within-instance LP range of 0.041 nats).
472	Because all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\%$ of instances.
473	
474	\paragraph{Constant prefix cancellation.}
475	All $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.
476	Any LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \textit{rankings} unchanged.
477	
478	\paragraph{CoNLL control group.}
479	CoNLL and WNUT-17 checkpoints were trained without thinking tokens (\texttt{enable\_thinking=False}).
480	If thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.
481	Instead, CoNLL shows \textit{higher} tied fractions at both temperatures (86.8\% at $T{=}1.0$, 95.8\% at $T{=}0.7$) than SciERC (60.3\% at $T{=}1.0$), directly contradicting the thinking-token hypothesis.
482	
483	\section{Log-Probability Score Compression}\label{app:logprob_ties}
484	
485	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
486	The median within-instance LP range is only 0.041 nats; we use $\varepsilon{=}0.05$ as an illustrative threshold to characterize this compression.
487	At this cutpoint, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\varepsilon$, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
488	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
489	This compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\%$ (vs.\ seed${=}42$: $0.041$ nats, $60.3\%$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12bf0d35-ed0e-46ef-9291-1da68638b216",
  "isSidechain": false,
  "promptId": "06fb4f38-4b27-4058-9b82-bbbbdb46c0d4",
  "type": "user",
  "uuid": "2665a929-fdaf-4a56-b548-4925472c9c67",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "On NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ single-sample).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{External equivalence margins.}\nThe oracle-headroom anchors above introduce circularity, as a reviewer correctly noted: $\\delta$ is calibrated against the very quantity it contextualizes.\nTo resolve this, we supplement with three externally grounded margins:\n(1) $\\delta_{\\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), representing measurement noise;\n(2) $\\delta_{\\mathrm{practical}}{=}0.5$~pp, reflecting the threshold below which NER differences are considered negligible \\cite{ratinov2009design};\n(3) $\\delta_{\\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \\cite{bergkirkpatrick2012empirical}.\n\nResults under these external anchors diverge sharply by configuration.\nOn LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\\Delta|{\\leq}0.1$~pp) and tight CIs at this sample size.\nOn Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, exceeding even $\\delta_{\\mathrm{literature}}$.\nOn SciERC NER ($n{=}529$), only SJ passes at $\\delta_{\\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.\nThese external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.\n\n\\paragraph{Multiple comparison considerations.}\\label{app:multiple_comparisons}\nOur primary selection analysis involves ${\\sim}$20 comparisons (5 signals $\\times$ 3--4 configurations).\nSince all primary selection results are non-significant ($p{>}0.05$), applying Benjamini-Hochberg correction can only make these results more conservative, strengthening the ``no signal beats greedy'' conclusion.\nThe sole positive finding---non-tied LP subset ($+2.9$~pp, $p{=}0.004$; \\S\\ref{sec:discussion})---survives Bonferroni correction over 5 signal comparisons ($p_{\\mathrm{adj}}{=}0.020 < 0.05$), as noted in the main text footnote.\nFor quality estimation signal rankings, differences between the top signals (e.g., VC vs.\\ SJ on SciERC) should be interpreted as descriptive rather than as statistically confirmed orderings, given the limited power of 3-seed comparisons.\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\nOn NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).\nOn RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.\nLLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .579${\\pm}$.008 & .600${\\pm}$.016 & .659${\\pm}$.016 & .677${\\pm}$.011 & .631${\\pm}$.013 \\\\\nLLaMA & .565${\\pm}$.008 & .593${\\pm}$.006 & .632${\\pm}$.012 & .673${\\pm}$.009 & .606${\\pm}$.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}\n\n\\section{Thinking Token Impact Analysis}\\label{app:thinking_token}\n\nQwen3-8B's SciERC checkpoint was trained with empty \\texttt{&lt;think>&lt;/think>} blocks prepended to each response (\\S\\ref{sec:setup}).\nWe quantify the potential impact on LP scores through three complementary arguments.\n\n\\paragraph{LP shift magnitude.}\nEmpty thinking tokens (mean 4.5 per sample) constitute 2.1\\% of tokens on SciERC.\nThe estimated LP shift is 0.001 nats per token (2.68\\% of the median within-instance LP range of 0.041 nats).\nBecause all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\\%$ of instances.\n\n\\paragraph{Constant prefix cancellation.}\nAll $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.\nAny LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \\textit{rankings} unchanged.\n\n\\paragraph{CoNLL control group.}\nCoNLL and WNUT-17 checkpoints were trained without thinking tokens (\\texttt{enable\\_thinking=False}).\nIf thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.\nInstead, CoNLL shows \\textit{higher} tied fractions at both temperatures (86.8\\% at $T{=}1.0$, 95.8\\% at $T{=}0.7$) than SciERC (60.3\\% at $T{=}1.0$), directly contradicting the thinking-token hypothesis.\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}, Figure~\\ref{fig:lp_range_cdf}).\nThe median within-instance LP range is only 0.041 nats; we use $\\varepsilon{=}0.05$ as an illustrative threshold to characterize this compression.\nAt this cutpoint, 60.3\\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\\varepsilon$, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nThe CDF rises smoothly with no cliff or discontinuity (Figure~\\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.\nThis compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\\%$ (vs.\\ seed${=}42$: $0.041$ nats, $60.3\\%$).",
      "numLines": 150,
      "startLine": 340,
      "totalLines": 1183
    }
  },
  "sourceToolAssistantUUID": "12bf0d35-ed0e-46ef-9291-1da68638b216",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 109 · 2026-05-17T07:16:20.361Z_

<details><summary>Logged reasoning block</summary>

```text
I now have enough information to respond to Reviewer 1's points. Let me check one more thing - the training for Few-NERD epochs. The appendix Table shows "Epochs: 5" universally and the dataset-specific section only mentions SciERC split and CoNLL/WNUT specifics. There's no mention of Few-NERD using 3 epochs. So either R1 has wrong information or there's something in the appendix I haven't read about Few-NERD training.

Let me check if there's anything about Few-NERD's training specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2665a929-fdaf-4a56-b548-4925472c9c67",
  "isSidechain": false,
  "requestId": "req_011Cb7jL7dnehQo1KuEPeTkH",
  "type": "assistant",
  "uuid": "9c0c587d-0445-4745-b0ac-338d1a9a6be7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UyAFUKEwCFAchEQeVXbxTn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4205,
      "cache_read_input_tokens": 107742,
      "output_tokens": 447,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 447,
          "cache_read_input_tokens": 107742,
          "cache_creation_input_tokens": 4205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4205
          },
          "type": "message"
        }
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

_source line 110 · 2026-05-17T07:16:23.285Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01TWVjTWHpPGYkEfduc2tvNx`</summary>

```json
{
  "pattern": "Few-NERD.*epoch|epoch.*Few-NERD|fewnerd.*epoch",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c0c587d-0445-4745-b0ac-338d1a9a6be7",
  "isSidechain": false,
  "requestId": "req_011Cb7jL7dnehQo1KuEPeTkH",
  "type": "assistant",
  "uuid": "9016aed0-f41b-42a9-81a6-e1a4fceb2952",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UyAFUKEwCFAchEQeVXbxTn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4205,
      "cache_read_input_tokens": 107742,
      "output_tokens": 447,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 447,
          "cache_read_input_tokens": 107742,
          "cache_creation_input_tokens": 4205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4205
          },
          "type": "message"
        }
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

_source line 111 · 2026-05-17T07:16:23.309Z_

<details><summary>↩ Tool result · `toolu_01TWVjTWHpPGYkEfduc2tvNx`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1087:Table~\ref{tab:fewnerd_full} reports the complete Few-NERD INTRA coarse evaluation (Qwen3-8B, LoRA rank${=}32$, 3 epochs, $N{=}8$, $T{=}1.0$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9016aed0-f41b-42a9-81a6-e1a4fceb2952",
  "isSidechain": false,
  "promptId": "06fb4f38-4b27-4058-9b82-bbbbdb46c0d4",
  "type": "user",
  "uuid": "5fef09bf-00d4-4019-8d41-108e6fe41de1",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1087:Table~\\ref{tab:fewnerd_full} reports the complete Few-NERD INTRA coarse evaluation (Qwen3-8B, LoRA rank${=}32$, 3 epochs, $N{=}8$, $T{=}1.0$).",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "9016aed0-f41b-42a9-81a6-e1a4fceb2952",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-17T07:16:24.638Z_

<details><summary>↩ Tool result · `toolu_01AcBGfGNzKHWkBU6hyCsQev`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e254be81-56d2-4efc-b7af-61d4d4ff2613",
  "isSidechain": false,
  "promptId": "06fb4f38-4b27-4058-9b82-bbbbdb46c0d4",
  "type": "user",
  "uuid": "29057ee5-61f8-4e6e-9c62-92354825c674",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "e254be81-56d2-4efc-b7af-61d4d4ff2613",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-17T07:16:24.623Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01AcBGfGNzKHWkBU6hyCsQev`</summary>

```json
{
  "pattern": "Few-NERD.*train|train.*Few-NERD",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fef09bf-00d4-4019-8d41-108e6fe41de1",
  "isSidechain": false,
  "requestId": "req_011Cb7jL7dnehQo1KuEPeTkH",
  "type": "assistant",
  "uuid": "e254be81-56d2-4efc-b7af-61d4d4ff2613",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UyAFUKEwCFAchEQeVXbxTn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4205,
      "cache_read_input_tokens": 107742,
      "output_tokens": 447,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 447,
          "cache_read_input_tokens": 107742,
          "cache_creation_input_tokens": 4205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4205
          },
          "type": "message"
        }
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

_source line 114_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见  以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Weakness 和 Question 标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供具体证据，cite 论文中的 Section/Table/Figure）。  ---  ### Reviewe…",
  "leafUuid": "29057ee5-61f8-4e6e-9c62-92354825c674",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Runtime record

_source line 115_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper for EMNLP 2026",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Assistant

_source line 116 · 2026-05-17T07:16:32.206Z_

<details><summary>Logged reasoning block</summary>

```text
There it is. Appendix line 1087 confirms: "Few-NERD INTRA coarse evaluation (Qwen3-8B, LoRA rank=32, **3 epochs**, N=8, T=1.0)". So R1 is correct that Few-NERD used 3 epochs vs. the standard 5 epochs for other datasets. This IS a potential confound for the degeneracy comparison.

The main text says "5 epochs" uniformly (experiments.tex line 15: "fine-tuned with LoRA (rank=32, α=64) for 5 epochs"), but the appendix reveals Few-NERD actually used 3 epochs. 

This is a disclosure problem—the main text presents a misleading picture of the experimental setup. I need to check what else is in that section of the appendix to see if there are other undisclosed variations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29057ee5-61f8-4e6e-9c62-92354825c674",
  "isSidechain": false,
  "requestId": "req_011Cb7jLsWkw7sE1VbcsBpVh",
  "type": "assistant",
  "uuid": "d691a2e0-0766-4fc8-93d7-b57111c4c817",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016VPhwror5UsJ4ANwmKjiv1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 623,
      "cache_read_input_tokens": 111947,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 623,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 332,
          "cache_read_input_tokens": 111947,
          "cache_creation_input_tokens": 623,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 623
          },
          "type": "message"
        }
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

_source line 117 · 2026-05-17T07:16:32.216Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TGQjU5CR9q22JuPgdPDkuS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 1080,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d691a2e0-0766-4fc8-93d7-b57111c4c817",
  "isSidechain": false,
  "requestId": "req_011Cb7jLsWkw7sE1VbcsBpVh",
  "type": "assistant",
  "uuid": "be46f861-e021-44bb-8057-12d5e4ff867b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016VPhwror5UsJ4ANwmKjiv1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 623,
      "cache_read_input_tokens": 111947,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 623,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 332,
          "cache_read_input_tokens": 111947,
          "cache_creation_input_tokens": 623,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 623
          },
          "type": "message"
        }
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

_source line 118 · 2026-05-17T07:16:32.226Z_

<details><summary>↩ Tool result · `toolu_01TGQjU5CR9q22JuPgdPDkuS`</summary>

```text
1080	
1081	The $\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\ref{tab:quality_estimation}), confirming ranking stability across two model families spanning 3B--8B.
1082	AUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), reflecting the $\rho$--AUROC dissociation noted in the main text.
1083	Despite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC---the strongest QE signal---yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.
1084	
1085	\section{Few-NERD Full Results}\label{app:fewnerd}
1086	
1087	Table~\ref{tab:fewnerd_full} reports the complete Few-NERD INTRA coarse evaluation (Qwen3-8B, LoRA rank${=}32$, 3 epochs, $N{=}8$, $T{=}1.0$).
1088	After gold-filtering (removing instances with no gold entities), the evaluation set contains $n{=}32{,}565$ instances across 8 coarse entity types; 11.9\% receive zero F1 under greedy decoding.
1089	Instance degeneracy is 10.1\% (vs.\ 21\% on SciERC, 58\% on CoNLL).
1090	
1091	\begin{table}[t]
1092	\centering
1093	\small
1094	\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\ $\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\% confidence interval.}
1095	\label{tab:fewnerd_full}
1096	\begin{tabular}{lcccc}
1097	\toprule
1098	Signal & $\rho$ & Sample AUROC & Sel.\ $\Delta$ & 95\% CI \\
1099	\midrule
1100	LP & .421 & .578 & $\mathbf{+1.36}$\,pp & [+1.18, +1.53] \\
1101	VC & .386 & --- & $-$1.79\,pp & --- \\
1102	FK & .313 & --- & $-$2.26\,pp & --- \\
1103	SJ & .300 & --- & $-$2.14\,pp & --- \\
1104	EM & .287 & --- & $-$3.85\,pp & --- \\
1105	\midrule
1106	\multicolumn{3}{l}{Greedy: 0.748 \quad Oracle: 0.872} & \multicolumn{2}{l}{Headroom: 12.4\,pp} \\
1107	\bottomrule
1108	\end{tabular}
1109	\end{table}
1110	
1111	\paragraph{Key observations.}
1112	(1)~All five signals achieve positive QE ($\rho$ 0.29--0.42), confirming that quality estimation works on Few-NERD. LP leads ($\rho{=}0.42$), followed by VC ($0.39$); the ranking differs from SciERC where VC leads, reflecting dataset-specific signal informativeness.
1113	(2)~LP is the only signal achieving significant positive selection ($+1.36$~pp, $p{<}0.001$, CI excludes zero). The sample-level AUROC of 0.578 confirms LP provides per-sample discriminability beyond instance-level quality prediction.
1114	(3)~Despite positive $\rho$, all structural signals degrade selection ($-1.79$ to $-3.85$~pp), further confirming that the correlation-selection gap is not an artifact of weak QE.
1115	(4)~Low degeneracy (10.1\%) enables LP selection: candidates differ in F1 more often, giving LP's per-sample signal headroom to exploit. This contrasts with SciERC (21\% degeneracy, LP $+0.42$~pp non-significant) and CoNLL (58\%, LP fails).
1116	
1117	\section{Per-Entity-Type LP Selection Analysis}\label{app:per_type_lp}
1118	
1119	Table~\ref{tab:per_type_lp} stratifies LP selection by entity type on Few-NERD, sorted by degeneracy rate.
1120	The degeneracy-gating mechanism holds at entity-type granularity: 7 of 8 types show positive LP selection gains, and the sole negative type (Art, $-0.17$~pp) has the highest degeneracy (19.8\%).
1121	The correlation between per-type degeneracy and oracle headroom is strong and significant (Spearman $\rho{=}{-}0.881$, $p{=}0.004$), confirming that degeneracy directly constrains the headroom available for selection.
1122	
1123	\begin{table}[h]
1124	\centering
1125	\small
1126	\caption{Per-entity-type LP selection on Few-NERD INTRA coarse (Qwen3-8B, $N{=}8$, $T{=}1.0$), sorted by degeneracy. LP $\Delta$: LP selection F1 minus greedy. 7/8 types show positive $\Delta$; Art (highest degeneracy) is the sole exception.}
1127	\label{tab:per_type_lp}
1128	\begin{tabular}{lrrrrrrr}
1129	\toprule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be46f861-e021-44bb-8057-12d5e4ff867b",
  "isSidechain": false,
  "promptId": "06fb4f38-4b27-4058-9b82-bbbbdb46c0d4",
  "type": "user",
  "uuid": "e04a6bd3-1f88-4929-b128-7463ad89cabb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\nThe $\\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\\ref{tab:quality_estimation}), confirming ranking stability across two model families spanning 3B--8B.\nAUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), reflecting the $\\rho$--AUROC dissociation noted in the main text.\nDespite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC---the strongest QE signal---yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.\n\n\\section{Few-NERD Full Results}\\label{app:fewnerd}\n\nTable~\\ref{tab:fewnerd_full} reports the complete Few-NERD INTRA coarse evaluation (Qwen3-8B, LoRA rank${=}32$, 3 epochs, $N{=}8$, $T{=}1.0$).\nAfter gold-filtering (removing instances with no gold entities), the evaluation set contains $n{=}32{,}565$ instances across 8 coarse entity types; 11.9\\% receive zero F1 under greedy decoding.\nInstance degeneracy is 10.1\\% (vs.\\ 21\\% on SciERC, 58\\% on CoNLL).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\\ $\\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\\% confidence interval.}\n\\label{tab:fewnerd_full}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\rho$ & Sample AUROC & Sel.\\ $\\Delta$ & 95\\% CI \\\\\n\\midrule\nLP & .421 & .578 & $\\mathbf{+1.36}$\\,pp & [+1.18, +1.53] \\\\\nVC & .386 & --- & $-$1.79\\,pp & --- \\\\\nFK & .313 & --- & $-$2.26\\,pp & --- \\\\\nSJ & .300 & --- & $-$2.14\\,pp & --- \\\\\nEM & .287 & --- & $-$3.85\\,pp & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{Greedy: 0.748 \\quad Oracle: 0.872} & \\multicolumn{2}{l}{Headroom: 12.4\\,pp} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Key observations.}\n(1)~All five signals achieve positive QE ($\\rho$ 0.29--0.42), confirming that quality estimation works on Few-NERD. LP leads ($\\rho{=}0.42$), followed by VC ($0.39$); the ranking differs from SciERC where VC leads, reflecting dataset-specific signal informativeness.\n(2)~LP is the only signal achieving significant positive selection ($+1.36$~pp, $p{<}0.001$, CI excludes zero). The sample-level AUROC of 0.578 confirms LP provides per-sample discriminability beyond instance-level quality prediction.\n(3)~Despite positive $\\rho$, all structural signals degrade selection ($-1.79$ to $-3.85$~pp), further confirming that the correlation-selection gap is not an artifact of weak QE.\n(4)~Low degeneracy (10.1\\%) enables LP selection: candidates differ in F1 more often, giving LP's per-sample signal headroom to exploit. This contrasts with SciERC (21\\% degeneracy, LP $+0.42$~pp non-significant) and CoNLL (58\\%, LP fails).\n\n\\section{Per-Entity-Type LP Selection Analysis}\\label{app:per_type_lp}\n\nTable~\\ref{tab:per_type_lp} stratifies LP selection by entity type on Few-NERD, sorted by degeneracy rate.\nThe degeneracy-gating mechanism holds at entity-type granularity: 7 of 8 types show positive LP selection gains, and the sole negative type (Art, $-0.17$~pp) has the highest degeneracy (19.8\\%).\nThe correlation between per-type degeneracy and oracle headroom is strong and significant (Spearman $\\rho{=}{-}0.881$, $p{=}0.004$), confirming that degeneracy directly constrains the headroom available for selection.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-entity-type LP selection on Few-NERD INTRA coarse (Qwen3-8B, $N{=}8$, $T{=}1.0$), sorted by degeneracy. LP $\\Delta$: LP selection F1 minus greedy. 7/8 types show positive $\\Delta$; Art (highest degeneracy) is the sole exception.}\n\\label{tab:per_type_lp}\n\\begin{tabular}{lrrrrrrr}\n\\toprule",
      "numLines": 50,
      "startLine": 1080,
      "totalLines": 1183
    }
  },
  "sourceToolAssistantUUID": "be46f861-e021-44bb-8057-12d5e4ff867b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 119 · 2026-05-17T07:16:48.436Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have confirmed that Few-NERD used 3 epochs (appendix line 1087) while the main text says "5 epochs" uniformly (experiments.tex line 15). This is indeed a confound as R1 pointed out.

Now let me compile my cross-response to R1's review. I have all the information I need.

Let me go through each point:

**W1** (n=3 causal inference): I partially agree. The cross-dataset evidence is weak (n=3), and the entity-type analysis has within-dataset dependence. 

The paper does acknowledge this limitation and backs it up with converging evidence from the LoRA ablation, which strengthens the overall argument.

**W2** (LoRA rank=8 confounds): I agree this is a valid concern. The Few-NERD vs rank=8 SciERC comparison is problematic.

**W3** (Power analysis): I partially agree, though the Few-NERD result provides high-powered confirmation.

**W4** (RE free-form contradiction): I agree this is a presentation issue.

**W5** (Seed coverage): I partially rebut - n=32,565 provides enormous statistical power within a single seed.

**W6** (Few-NERD 3 epochs): I AGREE - the appendix confirms this, and the main text's claim about 5 epochs is misleading since under-training becomes a confound for the degeneracy findings.

**W7** (SJ normalizer): Agree, minor.

**W8** (Table inconsistency): Partially rebut - the footnote explains it but the presentation could be clearer.

Looking at the specific questions: the data isn't provided in the paper, the 3-epoch finding is confirmed in the appendix while the 5-epoch degeneracy isn't reported, the statistical tests appear to be instance-level paired comparisons, the distribution isn't reported, and there's no control for this variable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e04a6bd3-1f88-4929-b128-7463ad89cabb",
  "isSidechain": false,
  "requestId": "req_011Cb7jMS1ca79iT1Q5f97dU",
  "type": "assistant",
  "uuid": "a88c3635-26f5-4086-9a01-42030242c4fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqYd45sd8FhCp9yXsZeHgE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 112570,
      "output_tokens": 4118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4118,
          "cache_read_input_tokens": 112570,
          "cache_creation_input_tokens": 1911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1911
          },
          "type": "message"
        }
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

_source line 120 · 2026-05-17T07:16:48.455Z_

I've confirmed the key details. Now posting my cross-response to the Director.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a88c3635-26f5-4086-9a01-42030242c4fb",
  "isSidechain": false,
  "requestId": "req_011Cb7jMS1ca79iT1Q5f97dU",
  "type": "assistant",
  "uuid": "1271e548-9ba1-4afc-a37d-daa22dca502d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqYd45sd8FhCp9yXsZeHgE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 112570,
      "output_tokens": 4118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4118,
          "cache_read_input_tokens": 112570,
          "cache_creation_input_tokens": 1911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1911
          },
          "type": "message"
        }
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

_source line 121 · 2026-05-17T07:18:13.536Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01UmuvVq3u186Ksufpex69fH`</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 的逐条回应\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1: 跨数据集 degeneracy 梯度因果推断基础薄弱 (n=3)**\n\n同意。三个数据集的单调排列概率确实是 1/6（单方向 1/3），统计上不具说服力。Entity-type-level analysis (n=8, ρ=-0.881, p=0.004) 虽更有力，但论文自己在 Section 4.3 (line 166) 也承认 \"the pooled Spearman correlation (ρ=−0.57, p=0.066, n=11) treats dataset-level and entity-type-level points as independent\"。混合两个粒度的观测确实有统计问题——entity types within Few-NERD 共享训练pipeline、模型权重、和 constrained decoding schema，不满足独立性假设。\n\n补充发现：LoRA rank ablation 提供了部分 converging evidence（rank=32 → 21% degen, rank=8 → 7.2%），但方向一致≠因果确认。建议至少增加 1-2 个 dataset（如 OntoNotes、ACE05）来加强跨数据集证据。\n\n**[AGREE] R1-W2: LoRA rank=8 ablation 混淆变量**\n\n同意且认为这是论文的关键逻辑缺陷之一。核心矛盾：\n- Few-NERD: 10% degeneracy, F1≈75%, LP ρ=0.421 → LP selection works (+1.36pp)\n- SciERC rank=8: 7.2% degeneracy, F1≈64%, LP ρ 未报告 → LP selection fails\n\n论文的 \"necessary but not sufficient\" claim 试图化解这个矛盾，但未提供关键数据：rank=8 下 LP 的 within-instance range 和 LP-F1 correlation。如果 rank=8 同时劣化了 LP 信号质量（因为 lower-rank 模型的 representation 更粗糙），则无法分离 degeneracy effect 和 capability effect。R1 的 Q1 直击要害——如果 rank=8 的 LP compression 更严重，那 \"degeneracy is necessary\" 的 claim 就缺少 crucial evidence。\n\n**[AGREE] R1-W3: 负面结果缺少 power analysis**\n\n部分同意。对 SciERC 主要结果 (n=529, 2 seeds)，检测 1pp 效应的 statistical power 确实未报告。论文提到 \"absence of evidence should not be equated with evidence of absence\"（Section 4.2, line 115）——这句话本身就暗示 power 可能不足。\n\n不过，论文用 TOST equivalence testing (Appendix Table 8) 部分缓解了这个问题：在 external anchor δ=1.0pp 下部分配置 pass equivalence。Few-NERD (n=32,565) 的高 power 正面结果也从另一端提供了边界条件。\n\n建议：补充一个简单的 power calculation（假设 σ≈0.15, paired test, n=529, 2 seeds 对 1pp effect 的 power 大约是 50-60%），让读者理解 SciERC 负面结果的可信度。\n\n**[AGREE] R1-W4: \"Compression is model-intrinsic\" 与 RE free-form 结果矛盾**\n\n同意这是一个 presentation 问题。证据：\n- Section 5, line 92-93: NER free-form decoding \"yields nearly identical LP distributions (std ratio 0.97)\"\n- Section 5, line 93-94: RE free-form \"+2.35pp (95% CI [+0.24, +4.50], p=0.025)\"\n\n论文确实在 Discussion 中做了 NER vs RE 的区分，但 Abstract (line 6) 说 \"LP carries genuine per-sample information but is compressed to near-ineffectiveness (median range 0.041 nats)\" 未加 \"for NER\" 限定。Introduction 的 contribution 2(c) 同样未 qualify。这使得 paper-level claim 过强。\n\n**[REBUT] R1-W5: Few-NERD 核心结果 seed coverage 有限**\n\n部分反驳。R1 担心 \"Few-NERD LP +1.36pp 是 1-seed result\" 意味着可靠性不足，但这里需区分两种统计推断：\n1. **Seed replication**（across seeds）：确实只有 1 seed\n2. **Instance-level inference**（within seed）：n=32,565 instances, paired bootstrap, p<0.001, 95% CI [+1.18, +1.53]\n\nWith n=32,565 paired observations, the within-seed statistical test has极高的 power。Bootstrap CI 排除零且较窄 (0.35pp wide)。Seed replication 测试的是 training run stochasticity，而非 selection signal 的 statistical reliability。\n\n然而，我承认如果 training seed 偶然产生了低 degeneracy 的 checkpoint，结论的可泛化性确实受影响。鉴于主实验 multi-seed stability (σ≤0.026, Table 7)，合理推断 Few-NERD 结果也是 seed-robust 的，但严格来说这是假设而非验证��\n\n**[AGREE] R1-W6: Few-NERD 3 epochs vs 其他 5 epochs 的 confound**\n\n强烈同意，且我认为这是此前我和 R1 都未充分强调的重要问题。\n\n关键证据：\n- 主文 Section 4.1, line 15: \"fine-tuned with LoRA (rank=32, α=64) for **5 epochs**\" —— 暗示所有数据集统一设置\n- Appendix Section Few-NERD Full Results (line 1087): \"Qwen3-8B, LoRA rank=32, **3 epochs**, N=8, T=1.0\"\n\n这存在两个问题：\n1. **主文 disclosure 不充分**：正文说 5 epochs 但 Few-NERD 实际用了 3 epochs，读者必须读到 Appendix 才能发现差异。\n2. **Confound 严重**：Under-training (3 vs 5 epochs) 直接降低模型 convergence → 降低 output consistency → 降低 degeneracy。因此 Few-NERD 的低 degeneracy (10%) 可能部分源于训练不足而非 dataset intrinsic property。这严重削弱了 \"degeneracy is dataset-specific\" 和 \"degeneracy gates LP selection\" 的 cross-dataset comparison。\n\n如果 5-epoch Few-NERD degeneracy 显著高于 10%，论文的整个 degeneracy-gating narrative 需要重新评估。\n\n**[AGREE] R1-W7: SJ normalizer \"Δρ<0.01\" 措辞**\n\n同意。Appendix Table 6 显示最大 Δρ=0.009，说 \"<0.01\" 技术上正确但应更精确写为 \"≤0.009\" 或 \"max |Δρ|=0.009\"。Minor。\n\n**[REBUT] R1-W8: Table 3 vs Table 4 greedy F1 不一致**\n\n部分反驳。论文在 Table 4 的 footnote（Section 4.3, line 143）明确解释：\"SciERC greedy (0.614) and headroom (13.8pp) differ from Table 3 (gold-filtered n=529, greedy=0.645) due to full-set evaluation; the ranking and significance are unchanged.\"\n\nFootnote 存在且解释清楚，但同意它容易被忽略。建议在 Table 4 caption 中直接注明 \"full-set evaluation (cf. gold-filtered in Table 3)\" 而非仅在 footnote 说明。\n\n---\n\n### Questions 回应\n\n**Q1. LoRA rank=8 LP median within-instance range?**\n\n[AGREE 这是关键缺失数据] 论文未报告。Section 4.5 (line 203-208) 报告了 rank=8 的 degeneracy (7.2%) 和 selection F1，但完全没有 LP distribution 的数据。这使得 \"LP compression persists regardless of LoRA rank\" 的 claim 是 unsupported assertion。\n\n**Q2. Few-NERD 3 epochs 原因？5 epochs degeneracy？**\n\n[AGREE 这是关键 confound] 3 epochs 在 Appendix line 1087 确认。原因未说明（可能是 dataset 规模大导致 5 epochs 过于 costly？Few-NERD 有 37,648 instances vs SciERC 551）。5-epoch degeneracy 未报告，但这是验证 degeneracy-gating claim 的 crucial control。\n\n**Q3. Table 3 sign test 是 instance-level 配对还是 corpus-level？**\n\n[可回答] Section 4.2, line 114 说 \"2-seed sign tests\"，结合 footnote \"Multi-seed NER experiments confirm seed variation is small\"。据此推断是 instance-level paired sign test：对每个 instance 比较 LP-selected sample 的 F1 vs greedy F1，统计 win/loss/tie counts。n=529 是 instance 数而非 corpus count。\n\n**Q4. Within-instance SJ-F1 ρ=0.52 的分布？**\n\n[AGREE 未报告] Section 5 只给了 median (0.524 SciERC, 0.994 CoNLL)。分布形状、负 ρ 的比例、以及 non-degenerate subset 的 size 均未 characterize。考虑到 median 0.524 暗示至少一半 instances 的 ρ≤0.524，且可能有相当比例 ρ<0 的 instances，这些信息对理解 MBR 的 failure mode 很重要。\n\n**Q5. Entity-type-level analysis 是否控制了 frequency/average entity count？**\n\n[AGREE 未控制] Appendix Table (per-type analysis) 只按 degeneracy sort。Entity type frequency（多少 instances 包含该 type）和 average entity count per instance 都可能 confound：high-frequency types 有更多 training data → lower degeneracy，而非 type semantics 本身的 effect。Partial correlation 控制 frequency 后 ρ 可能衰减。\n\n---\n\n### Missing References 回应\n\n**Lightman et al. (2024) \"Let's Verify Step by Step\"**: 已在 Related Work (Section 2, line 35) 被引用 `\\cite{lightman2024verify}`。R1 可能遗漏。\n\n**Yoran et al. (2023)**: 如果指的是 self-consistency 相关工作，未被引用。应核实具体论文。\n\n**Zhang et al. (2024) DeepMind test-time compute**: 未被引用。如果指 \"Scaling LLM Test-Time Compute\" 系列，Snell et al. (2025) 已覆盖 ICLR 版本。DeepMind 的具体论文需核实。\n\n**Eikema et al. (2025) structured MBR**: 已在 Section 2 (line 25) 被引用 `\\citet{eikema2025structured}`。R1 可能遗漏。\n\n---\n\n### 综合评价\n\nR1 的审稿质量很高，特别是 W1、W2、W6 三个 weakness 直击方法论薄弱环节。我与 R1 的主要共识：\n1. Degeneracy-gating narrative 的统计基础不够坚实（n=3 + confounded Few-NERD training）\n2. LoRA ablation 的 causal claim 有混淆变量\n3. 论文是高质量的 negative result 但 contribution bar 对 main conference 可能不够\n\n我与 R1 的主要分歧：\n- R1 给 Excitement 3.5/5，我给 2.5/5。我认为纯诊断 + 无 actionable method 使得论文更适合 Findings。\n- R1 对 seed coverage 的担忧（W5）我认为对 Few-NERD 不太成立（n=32,565 的 within-seed power 极高）。\n\n**建议 Final Score**: Borderline (3/5, leaning Findings)。若能修复 W6 (Few-NERD epoch confound) 并补充 W2 (rank=8 LP compression data)，可升至 3.5。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1271e548-9ba1-4afc-a37d-daa22dca502d",
  "isSidechain": false,
  "requestId": "req_011Cb7jMS1ca79iT1Q5f97dU",
  "type": "assistant",
  "uuid": "aadf0542-c483-40b7-897c-e003ff19f942",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqYd45sd8FhCp9yXsZeHgE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 112570,
      "output_tokens": 4118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4118,
          "cache_read_input_tokens": 112570,
          "cache_creation_input_tokens": 1911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1911
          },
          "type": "message"
        }
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

_source line 122 · 2026-05-17T07:18:17.271Z_

<details><summary>↩ Tool result · `toolu_01UmuvVq3u186Ksufpex69fH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aadf0542-c483-40b7-897c-e003ff19f942",
  "isSidechain": false,
  "promptId": "06fb4f38-4b27-4058-9b82-bbbbdb46c0d4",
  "type": "user",
  "uuid": "b3c1faaa-e75b-4c4c-ad56-5b4f395c9e3f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "aadf0542-c483-40b7-897c-e003ff19f942",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 123 · 2026-05-17T07:18:17.276Z_

```json
{
  "parentUuid": "b3c1faaa-e75b-4c4c-ad56-5b4f395c9e3f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6f936c8f-6fba-4963-8ed5-5c6357ac1af2",
  "timestamp": "2026-05-17T07:18:17.276Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 124_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见  以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Weakness 和 Question 标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供具体证据，cite 论文中的 Section/Table/Figure）。  ---  ### Reviewe…",
  "leafUuid": "6f936c8f-6fba-4963-8ed5-5c6357ac1af2",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---

### Runtime record

_source line 125_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper for EMNLP 2026",
  "sessionId": "7db3877c-97f7-4f67-b6d3-097ea4227bb4"
}
```

---
