# Research conversation: [Round 1 审稿请求]: ## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量） ### 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confide

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 126
- **Recorded user turns:** 1
- **Tool calls:** 38
- **Original source:** `logs/chats/exported-trajectories/account-3/4d69282c-32b0-4839-ba8f-96c846d16f13.jsonl`
- **Structured JSON:** [`7511b5b3df5289837234.json`](../../sessions/75/7511b5b3df5289837234.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T05:55:34.309Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T05:55:34.309Z",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "content": "[Round 1 审稿请求]:\n## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### 论文信息\n- **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\n- **路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（各章节在 `docs/paper/sections/` 下）\n- **目标 venue**: EMNLP 2026 Main Conference Long Paper (ACL Rolling Review)\n- **截止日期**: 2026-05-25\n- **格式**: ACL style, ≤8 页正文, 附录不计页数, double-blind\n\n### 你的审查侧重\n\n**核心任务**: 评估论文的新颖性、贡献完整性、写作质量和格式合规性。\n\n重点审查以下方面：\n\n1. **新颖性与贡献增量**\n   - 相对于 Yao et al. (2026) 的增量是否足够清晰（他们也做了 consistency + NER/RE）\n   - \"Correlation-selection gap\" 概念是否新颖，还是 MBR 社区已知的结论换了个名字\n   - Contribution 1 \"methodological premise\"（4/5 signals instance-level by construction）是定义推论还是实验发现？是否应计为独立贡献？\n   - 纯诊断性论文（几乎所有 remedy 均 negative）对 EMNLP main conference 的门槛是否足够\n   - Few-NERD LP +1.36pp 作为 practical positive contribution 的分量\n\n2. **Related Work 完整性**\n   - 引用覆盖度：直接相关方法、baseline 论文、benchmark 论文、理论基础\n   - 与 MBR decoding 文献（Eikema, Freitag, Deguchi）的差异化定位\n   - 是否有遗漏的重要相关工作（特别是 structured prediction confidence, constrained decoding, diversity in generation）\n   - 检查 bib 条目：是否有 orphan entries（bib 中有但正文未引用）\n\n3. **叙事结构与主线统一性**\n   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成连贯主线\n   - Abstract 是否过度压缩/数字过载（~170 words, 8+ quantitative values）\n   - Introduction 的 5 段结构是否完整\n   - Contribution 列表与后续 section 的对应关系\n   - Discussion 篇幅是否合理（7 个子话题）\n\n4. **写作质量（去 AI 风格）**\n   - grep 检查：解释性 em-dash (—) / en-dash (–) 数量\n   - -ing phrase 结尾检查\n   - 过度分段检查\n   - 专有名词首次使用时是否有定义\n   - 用词黑名单检查（delve into, leverage, utilize, facilitate, myriad, plethora）\n\n5. **格式合规**\n   - 页数是否在 8 页限制内\n   - 匿名化是否完整（无 author 泄漏、无 URL 泄漏）\n   - 参考文献格式\n   - 图表规范（caption 自包含、小数精度一致、最优加粗）\n   - Limitations 和 Ethics Statement 是否充实\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n4. **Questions** (需要作者澄清的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (strong reject / weak reject / borderline / weak accept / strong accept) + 置信度 (1-5)\n\n严格客观，不留情面。特别注意写作风格和格式细节。"
}
```

---

### Runtime record

_source line 2 · 2026-05-18T05:55:34.313Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T05:55:34.313Z",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

## Round 1

124 recorded events

### User

_source line 3 · 2026-05-18T05:55:34.352Z_

[Round 1 审稿请求]:
## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）

### 论文信息
- **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction
- **路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（各章节在 `docs/paper/sections/` 下）
- **目标 venue**: EMNLP 2026 Main Conference Long Paper (ACL Rolling Review)
- **截止日期**: 2026-05-25
- **格式**: ACL style, ≤8 页正文, 附录不计页数, double-blind

### 你的审查侧重

**核心任务**: 评估论文的新颖性、贡献完整性、写作质量和格式合规性。

重点审查以下方面：

1. **新颖性与贡献增量**
   - 相对于 Yao et al. (2026) 的增量是否足够清晰（他们也做了 consistency + NER/RE）
   - "Correlation-selection gap" 概念是否新颖，还是 MBR 社区已知的结论换了个名字
   - Contribution 1 "methodological premise"（4/5 signals instance-level by construction）是定义推论还是实验发现？是否应计为独立贡献？
   - 纯诊断性论文（几乎所有 remedy 均 negative）对 EMNLP main conference 的门槛是否足够
   - Few-NERD LP +1.36pp 作为 practical positive contribution 的分量

2. **Related Work 完整性**
   - 引用覆盖度：直接相关方法、baseline 论文、benchmark 论文、理论基础
   - 与 MBR decoding 文献（Eikema, Freitag, Deguchi）的差异化定位
   - 是否有遗漏的重要相关工作（特别是 structured prediction confidence, constrained decoding, diversity in generation）
   - 检查 bib 条目：是否有 orphan entries（bib 中有但正文未引用）

3. **叙事结构与主线统一性**
   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成连贯主线
   - Abstract 是否过度压缩/数字过载（~170 words, 8+ quantitative values）
   - Introduction 的 5 段结构是否完整
   - Contribution 列表与后续 section 的对应关系
   - Discussion 篇幅是否合理（7 个子话题）

4. **写作质量（去 AI 风格）**
   - grep 检查：解释性 em-dash (—) / en-dash (–) 数量
   - -ing phrase 结尾检查
   - 过度分段检查
   - 专有名词首次使用时是否有定义
   - 用词黑名单检查（delve into, leverage, utilize, facilitate, myriad, plethora）

5. **格式合规**
   - 页数是否在 8 页限制内
   - 匿名化是否完整（无 author 泄漏、无 URL 泄漏）
   - 参考文献格式
   - 图表规范（caption 自包含、小数精度一致、最优加粗）
   - Limitations 和 Ethics Statement 是否充实

### 输出格式

请按以下结构输出审稿意见：
1. **Summary** (2-3 句)
2. **Strengths** (逐条)
3. **Weaknesses** (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])
4. **Questions** (需要作者澄清的)
5. **Missing References** (如有)
6. **Overall Assessment** (strong reject / weak reject / borderline / weak accept / strong accept) + 置信度 (1-5)

严格客观，不留情面。特别注意写作风格和格式细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "4baf7d47-293e-46b8-8bf8-b7822ce8ab38",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T05:55:34.351Z_

```json
{
  "parentUuid": "4baf7d47-293e-46b8-8bf8-b7822ce8ab38",
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
  "uuid": "bc729951-92e8-455b-9817-dacdea6fc99a",
  "timestamp": "2026-05-18T05:55:34.351Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T05:55:34.351Z_

```json
{
  "parentUuid": "bc729951-92e8-455b-9817-dacdea6fc99a",
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
  "uuid": "76f513ba-d8a0-4c7a-80a8-2620d0ed3386",
  "timestamp": "2026-05-18T05:55:34.351Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-18T05:55:34.351Z_

```json
{
  "parentUuid": "76f513ba-d8a0-4c7a-80a8-2620d0ed3386",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bcb290e2-0e22-4975-8a25-031c95c1a3c7",
  "timestamp": "2026-05-18T05:55:34.351Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
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
  "aiTitle": "Review structured IE paper for EMNLP 2026",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Assistant

_source line 8 · 2026-05-18T05:55:40.332Z_

<details><summary>Logged reasoning block</summary>

```text
The user (Review Director) is asking me to perform a thorough review of a paper as Reviewer 2, focusing on novelty, completeness, writing quality, and format compliance. Let me start by:

1. First, running the review-reviewer-session-start skill to initialize
2. Searching for EMNLP 2026 / ACL ARR reviewer guidelines
3. Reading the paper

Let me begin by reading the paper and searching for reviewer guidelines in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcb290e2-0e22-4975-8a25-031c95c1a3c7",
  "isSidechain": false,
  "requestId": "req_011Cb9WzFVcuPTboWurptmDt",
  "type": "assistant",
  "uuid": "5a0180ec-bfb4-45fa-bcc8-9fb7bda3ecd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbYodMd1jUSc9vRvn7kk45",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15395,
      "cache_read_input_tokens": 11841,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 277,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15395
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-18T05:55:40.859Z_

开始执行 Reviewer 2 审稿任务。先初始化 session 并读取论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a0180ec-bfb4-45fa-bcc8-9fb7bda3ecd0",
  "isSidechain": false,
  "requestId": "req_011Cb9WzFVcuPTboWurptmDt",
  "type": "assistant",
  "uuid": "7e4b7d07-4d4d-4ac7-9f53-0454eb4dc1f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbYodMd1jUSc9vRvn7kk45",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15395,
      "cache_read_input_tokens": 11841,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 277,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15395
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-18T05:55:41.718Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Rv6QD2HqHif65hdDSdonbB`</summary>

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
  "parentUuid": "7e4b7d07-4d4d-4ac7-9f53-0454eb4dc1f5",
  "isSidechain": false,
  "requestId": "req_011Cb9WzFVcuPTboWurptmDt",
  "type": "assistant",
  "uuid": "c9012ba8-6e77-4eac-ae4c-cbab5c196136",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbYodMd1jUSc9vRvn7kk45",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15395,
      "cache_read_input_tokens": 11841,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 277,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15395
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-18T05:55:41.725Z_

<details><summary>↩ Tool result · `toolu_01Rv6QD2HqHif65hdDSdonbB`</summary>

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
  "parentUuid": "c9012ba8-6e77-4eac-ae4c-cbab5c196136",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "eff0d166-4a31-42ea-bdb7-d6a915ef8c6d",
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
  "sourceToolAssistantUUID": "c9012ba8-6e77-4eac-ae4c-cbab5c196136",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-18T05:55:45.787Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me start by:
1. Reading the paper (main.tex and sections)
2. Searching for ACL ARR / EMNLP 2026 reviewer guidelines
3. Running verify_references
4. Checking for writing quality issues (dashes, etc.)

Let me do these in parallel where possible.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eff0d166-4a31-42ea-bdb7-d6a915ef8c6d",
  "isSidechain": false,
  "requestId": "req_011Cb9WzoD6iMmUMG11zcbYz",
  "type": "assistant",
  "uuid": "8447e704-0eb3-4540-a1fd-c3ce94fa863e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8SqGPDmNTYBHpFD7BmyNh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2273,
      "cache_read_input_tokens": 27236,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2273,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 179,
          "cache_read_input_tokens": 27236,
          "cache_creation_input_tokens": 2273,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2273
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-18T05:55:46.325Z_

先并行读取论文、搜索审稿标准、验证引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8447e704-0eb3-4540-a1fd-c3ce94fa863e",
  "isSidechain": false,
  "requestId": "req_011Cb9WzoD6iMmUMG11zcbYz",
  "type": "assistant",
  "uuid": "59af5871-63e5-44cb-a30b-852bf22ab0d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8SqGPDmNTYBHpFD7BmyNh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2273,
      "cache_read_input_tokens": 27236,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2273,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 179,
          "cache_read_input_tokens": 27236,
          "cache_creation_input_tokens": 2273,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2273
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-18T05:55:46.586Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01NFT6Ayp5o8hjUiFmEDtVuh`</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59af5871-63e5-44cb-a30b-852bf22ab0d6",
  "isSidechain": false,
  "requestId": "req_011Cb9WzoD6iMmUMG11zcbYz",
  "type": "assistant",
  "uuid": "55f06c3d-8519-43cf-a0e0-c0ae7da756bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8SqGPDmNTYBHpFD7BmyNh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2273,
      "cache_read_input_tokens": 27236,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2273,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 179,
          "cache_read_input_tokens": 27236,
          "cache_creation_input_tokens": 2273,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2273
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-18T05:55:46.606Z_

<details><summary>↩ Tool result · `toolu_01NFT6Ayp5o8hjUiFmEDtVuh`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55f06c3d-8519-43cf-a0e0-c0ae7da756bb",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "b355299e-51b3-4453-bf85-7994c662f206",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 13,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "55f06c3d-8519-43cf-a0e0-c0ae7da756bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T05:55:49.152Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01AZdiezRweaiMKxAm6vzxeW`</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/**/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b355299e-51b3-4453-bf85-7994c662f206",
  "isSidechain": false,
  "requestId": "req_011Cb9X19w2odyk4gvuP9dzx",
  "type": "assistant",
  "uuid": "248097ee-43d2-4c69-bb1b-126f8e40fc2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWBE3dhYTTWqsk7hY7aF6r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 194,
      "cache_read_input_tokens": 29509,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 194,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 29509,
          "cache_creation_input_tokens": 194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 194
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-18T05:55:49.162Z_

<details><summary>↩ Tool result · `toolu_01AZdiezRweaiMKxAm6vzxeW`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "248097ee-43d2-4c69-bb1b-126f8e40fc2e",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "5bf374cd-faf7-453d-a2dc-7462d4e29397",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 7,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "248097ee-43d2-4c69-bb1b-126f8e40fc2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T05:55:51.843Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01NQnJNarWsHj8BxEVRxcijb`</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bf374cd-faf7-453d-a2dc-7462d4e29397",
  "isSidechain": false,
  "requestId": "req_011Cb9X1Lx4ctAVEvpvTXpL9",
  "type": "assistant",
  "uuid": "417cba44-a488-4725-9fa3-016dd60bdfbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yYX1f6mzvVC3TYUG6EnnJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 81,
      "cache_read_input_tokens": 29703,
      "output_tokens": 63,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 81,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 63,
          "cache_read_input_tokens": 29703,
          "cache_creation_input_tokens": 81,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 81
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-18T05:55:51.865Z_

<details><summary>↩ Tool result · `toolu_01NQnJNarWsHj8BxEVRxcijb`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "417cba44-a488-4725-9fa3-016dd60bdfbe",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "667c5b3d-ede9-405e-b7af-210f5fc1bb53",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 14,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "417cba44-a488-4725-9fa3-016dd60bdfbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T05:55:56.329Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01CZ3x9uU77kzw8gfDMW3MVY`</summary>

```json
{
  "description": "Find paper tex files",
  "subagent_type": "Explore",
  "prompt": "I need to find the LaTeX paper files for the project \"struct_self_consist_ie\". The paper might be at:\n- projects/struct_self_consist_ie/docs/paper/main.tex\n- projects/struct_self_consist_ie/paper/main.tex\n- Or elsewhere\n\nSearch broadly under /home/ubuntu/ for any .tex files related to this project. Also look for .bib files. Report all paths found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "667c5b3d-ede9-405e-b7af-210f5fc1bb53",
  "isSidechain": false,
  "requestId": "req_011Cb9X1YHwXwPDK8ezzQ3Ct",
  "type": "assistant",
  "uuid": "7ed96334-b3ae-42e1-bdbe-19e5e3b72c13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCuqoc999ifqVkCYK8bGZC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 78,
      "cache_read_input_tokens": 29784,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 78,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 29784,
          "cache_creation_input_tokens": 78,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 78
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-18T05:56:03.075Z_

<details><summary>↩ Tool result · `toolu_01CZ3x9uU77kzw8gfDMW3MVY`</summary>

```text
Perfect! I found the LaTeX and bibliography files for the struct_self_consist_ie project. Here's the comprehensive report:

## Main Paper Files

**Primary paper directory:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/`

**Main entry point:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`

**Bibliography:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib`

## Paper Sections (in docs/paper/sections/)

- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex`

## Additional Artifact Files

The artifacts directory also contains numerous generated LaTeX files from DREAM reports and experimental outputs, such as:
- Tables and figures (`bootstrap_ci_tables.tex`, `per_type_lp_table.tex`, etc.)
- Generated paper versions from DREAM reports

The main paper structure is in `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/` with the entry point at `main.tex` and references at `references.bib`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ed96334-b3ae-42e1-bdbe-19e5e3b72c13",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "685a7e4f-d2fc-4ad5-b62d-e8171b278965",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to find the LaTeX paper files for the project \"struct_self_consist_ie\". The paper might be at:\n- projects/struct_self_consist_ie/docs/paper/main.tex\n- projects/struct_self_consist_ie/paper/main.tex\n- Or elsewhere\n\nSearch broadly under /home/ubuntu/ for any .tex files related to this project. Also look for .bib files. Report all paths found.",
    "agentId": "af53ddeec3e1defd9",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I found the LaTeX and bibliography files for the struct_self_consist_ie project. Here's the comprehensive report:\n\n## Main Paper Files\n\n**Primary paper directory:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/`\n\n**Main entry point:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n\n**Bibliography:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib`\n\n## Paper Sections (in docs/paper/sections/)\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex`\n\n## Additional Artifact Files\n\nThe artifacts directory also contains numerous generated LaTeX files from DREAM reports and experimental outputs, such as:\n- Tables and figures (`bootstrap_ci_tables.tex`, `per_type_lp_table.tex`, etc.)\n- Generated paper versions from DREAM reports\n\nThe main paper structure is in `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/` with the entry point at `main.tex` and references at `references.bib`."
      }
    ],
    "totalDurationMs": 6742,
    "totalTokens": 22820,
    "totalToolUseCount": 2,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3902,
      "cache_read_input_tokens": 18222,
      "output_tokens": 689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3902
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 689,
          "cache_read_input_tokens": 18222,
          "cache_creation_input_tokens": 3902,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3902,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 2,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "7ed96334-b3ae-42e1-bdbe-19e5e3b72c13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）  ### 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction - **路径**: `projects…",
  "leafUuid": "685a7e4f-d2fc-4ad5-b62d-e8171b278965",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured IE paper for EMNLP 2026",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Assistant

_source line 24 · 2026-05-18T05:56:06.219Z_

找到论文文件。现在并行读取所有章节、搜索审稿标准、验证引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "685a7e4f-d2fc-4ad5-b62d-e8171b278965",
  "isSidechain": false,
  "requestId": "req_011Cb9X2N9miJVEyGts1Pie8",
  "type": "assistant",
  "uuid": "00152082-4542-4a16-9f7f-ec66490346f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016WhzYh3YFegwgkQT2cjgN7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 888,
      "cache_read_input_tokens": 29862,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 29862,
          "cache_creation_input_tokens": 888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 888
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-18T05:56:06.501Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KFJecSz4vpvuMzyQWZZNu3`</summary>

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
  "parentUuid": "00152082-4542-4a16-9f7f-ec66490346f9",
  "isSidechain": false,
  "requestId": "req_011Cb9X2N9miJVEyGts1Pie8",
  "type": "assistant",
  "uuid": "6468bf70-1098-44ed-b82b-bef0dd1b0b25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016WhzYh3YFegwgkQT2cjgN7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 888,
      "cache_read_input_tokens": 29862,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 29862,
          "cache_creation_input_tokens": 888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 888
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-18T05:56:06.509Z_

<details><summary>↩ Tool result · `toolu_01KFJecSz4vpvuMzyQWZZNu3`</summary>

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
  "parentUuid": "6468bf70-1098-44ed-b82b-bef0dd1b0b25",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "0de291c9-159a-4625-9af6-4853f562735c",
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
  "sourceToolAssistantUUID": "6468bf70-1098-44ed-b82b-bef0dd1b0b25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T05:56:09.009Z_

<details open><summary>🔧 Tool call — Read · `toolu_015bBfTJEJcQNepuF2yhSuhC`</summary>

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
  "parentUuid": "0de291c9-159a-4625-9af6-4853f562735c",
  "isSidechain": false,
  "requestId": "req_011Cb9X2cxGFFGVS68egBGtk",
  "type": "assistant",
  "uuid": "acee0a19-0db6-4f3c-b817-a06378848cd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTzxsLx1DZJCiA4eGGUi7h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 722,
      "cache_read_input_tokens": 30750,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 30750,
          "cache_creation_input_tokens": 722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 722
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-18T05:56:09.013Z_

<details><summary>↩ Tool result · `toolu_015bBfTJEJcQNepuF2yhSuhC`</summary>

```text
1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals (four instance-level, one per-sample log-probability [LP]) for quality estimation and sample selection on four NER benchmarks using 4B\textendash 8B models.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), supporting selective prediction.
5	For selection, LP achieves $+1.36$~pp on Few-NERD ($p{<}0.001$) under two jointly necessary conditions: low instance degeneracy and adequate LP-quality alignment ($\rho \gtrsim 0.3$).
6	When either condition is violated, LP gains fall below detectable thresholds despite ${\sim}$13~pp oracle headroom, a disparity we term the \textbf{correlation-selection gap}.
7	Two mechanisms explain this gap: \textit{instance degeneracy} (14\textendash 59\% of instances yield identical F1 scores across all samples) eliminates headroom; \textit{weak LP-quality alignment} prevents exploiting the remainder.
8	A methodological premise underlies both: four of five signals are instance-level aggregates that by definition cannot rank candidates.
9	Degeneracy is controllable via temperature and training convergence; closing the gap for structural signals likely requires learned per-sample scoring.
10	\end{abstract}
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acee0a19-0db6-4f3c-b817-a06378848cd5",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "4311c9fe-2594-44f9-8400-de6bf77855fe",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nSelf-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \\textit{sets} of entities with partial overlap, where no majority vote analog exists.\nWe evaluate five confidence signals (four instance-level, one per-sample log-probability [LP]) for quality estimation and sample selection on four NER benchmarks using 4B\\textendash 8B models.\nAll signals achieve reliable quality estimation ($\\rho$ up to 0.45, AUROC up to 0.82), supporting selective prediction.\nFor selection, LP achieves $+1.36$~pp on Few-NERD ($p{<}0.001$) under two jointly necessary conditions: low instance degeneracy and adequate LP-quality alignment ($\\rho \\gtrsim 0.3$).\nWhen either condition is violated, LP gains fall below detectable thresholds despite ${\\sim}$13~pp oracle headroom, a disparity we term the \\textbf{correlation-selection gap}.\nTwo mechanisms explain this gap: \\textit{instance degeneracy} (14\\textendash 59\\% of instances yield identical F1 scores across all samples) eliminates headroom; \\textit{weak LP-quality alignment} prevents exploiting the remainder.\nA methodological premise underlies both: four of five signals are instance-level aggregates that by definition cannot rank candidates.\nDegeneracy is controllable via temperature and training convergence; closing the gap for structural signals likely requires learned per-sample scoring.\n\\end{abstract}\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  },
  "sourceToolAssistantUUID": "acee0a19-0db6-4f3c-b817-a06378848cd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-18T05:56:09.077Z_

```json
{
  "parentUuid": "4311c9fe-2594-44f9-8400-de6bf77855fe",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b44010c3-b604-4fc2-84b6-d8287137f9a3",
  "timestamp": "2026-05-18T05:56:09.077Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-18T05:56:12.046Z_

<details open><summary>🔧 Tool call — Read · `toolu_016PbXHKY4CX2n4gnA9UU2gb`</summary>

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
  "parentUuid": "b44010c3-b604-4fc2-84b6-d8287137f9a3",
  "isSidechain": false,
  "requestId": "req_011Cb9X2oxoBMZuLRQCRDHRm",
  "type": "assistant",
  "uuid": "c535919e-3e53-410b-9c6e-b27cf876b88b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBtVJSrcjGCtTMgMV979Pe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 581,
      "cache_read_input_tokens": 31472,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 581,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 31472,
          "cache_creation_input_tokens": 581,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 581
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-18T05:56:12.063Z_

<details><summary>↩ Tool result · `toolu_016PbXHKY4CX2n4gnA9UU2gb`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we investigate \textit{why} this correlation does not reliably translate to selection gains, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
13	For selection, LP achieves $+1.36$~pp on Few-NERD ($p{<}0.001$) when two conditions are jointly met: low instance degeneracy (13.8\%) and adequate alignment ($\rho{\approx}0.5$), with gains scaling with $N$ ($+0.52$~pp, $p{=}0.003$).
14	On SciERC, the observed LP gain ($+0.2$~pp, $p{=}0.29$) falls below the minimum detectable effect (${\approx}$1.5~pp at 80\% power, $n{=}529$) despite 13~pp oracle headroom. We term this disparity between quality estimation strength and selection effectiveness the \textbf{correlation-selection gap}.
15	Two mechanisms explain this gap: (a)~\textit{instance degeneracy} (14\textendash 59\% of instances yield identical F1 scores across all $N$ samples, eliminating headroom); and (b)~\textit{weak LP-quality alignment} (within-instance $\rho(\text{LP}, \text{F1})$ too low to exploit the remaining headroom; \S\ref{sec:discussion}).
16	
17	\begin{figure*}[t]
18	\centering
19	\includegraphics[width=\textwidth]{fig_overview}
20	\caption{The correlation-selection gap. \textbf{Left}: consistency signals reliably predict instance-level quality ($\rho$ up to 0.45 on CoNLL, 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82). \textbf{Right}: quality estimation does not translate to selection; all methods approximately match greedy decoding ($T{=}0$) despite 13~pp oracle headroom (\S\ref{sec:discussion}).}
21	\label{fig:overview}
22	\end{figure*}
23	
24	We evaluate five signals from three families (structural, surface, and model-internal) on SciERC \cite{luan2018scierc} as a primary medium-difficulty test bed, with Few-NERD \cite{ding2021fewnerd} (low-degeneracy contrast), CoNLL-2003 \cite{tjongkimsang2003conll} (ceiling-effect control), and WNUT-17 \cite{derczynski2017wnut} (signal-collapse boundary), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).
25	We vary candidate pool size ($N{\in}\{2,\ldots,32\}$), signal sophistication, and model capacity within the 4B\textendash 8B range; behavior at 70B+ scales remains an open question.
26	An exploratory extension to relation extraction is reported in Appendix~\ref{app:re_extension}.
27	Our contributions:
28	\begin{enumerate}
29	    \item \textbf{Quality estimation framework and a methodological premise.}
30	    Five signals from three families evaluated on four NER benchmarks, two model families, and a 4B ablation, achieving reliable quality estimation ($\rho$ up to 0.45; AUROC up to 0.82).
31	    A definitional observation structures the analysis: four of five signals are instance-level aggregates that by design assign identical scores to all candidates; this per-sample vs.\ instance-level distinction determines which signals can, in principle, improve selection.
32	
33	    \item \textbf{Two empirical mechanisms underlying the correlation-selection gap.}
34	    Instance degeneracy (14\textendash 59\% of instances yield identical F1 scores across all samples) eliminates headroom for consensus-based selection; weak LP-quality alignment (within-instance $\rho{\approx}0.24$ on SciERC) prevents exploiting the remaining headroom.
35	    Temperature ablation provides the primary evidence that both conditions are independently necessary ($T{=}1.2$: degeneracy 12.5\%, alignment $\rho{=}0.225$; \S\ref{sec:discussion}); LoRA-rank, entity-token LP, and supervised combination of the five signals studied corroborate the pattern.
36	
37	    \item \textbf{Practical conditions for LP selection.}
38	    LP achieves $+1.36$~pp on Few-NERD ($p{<}0.001$) and scales with $N$ ($+0.52$~pp, $p{=}0.003$) when degeneracy ${<}$15\% and alignment $\rho \gtrsim 0.3$.
39	    Per-entity-type analysis within Few-NERD ($\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$; types share model and tokenizer, so effective degrees of freedom may be lower) provides supporting evidence; temperature and training convergence offer controllable levers for degeneracy.
40	\end{enumerate}
41	
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c535919e-3e53-410b-9c6e-b27cf876b88b",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "58b04b08-1a62-431e-9d2a-e2bce8faf069",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \\citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \\cite{snell2025scaling, brown2024monkeys}.\nBut named entity recognition (NER) poses a structurally different challenge: the output is a \\textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.\n\nPrior work on confidence estimation for LLM-based IE has conflated \\textit{quality estimation} (which inputs does the model handle reliably?) with \\textit{sample selection} (which of $N$ outputs is best?).\nExisting self-consistency methods \\cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.\nUnlike \\citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we investigate \\textit{why} this correlation does not reliably translate to selection gains, diagnosing degeneracy and compression as the two blocking mechanisms.\nOur experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.\n\nA methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.\nAll signals achieve reliable quality estimation ($\\rho$ up to 0.45, AUROC up to 0.82; Figure~\\ref{fig:overview}), supporting selective prediction.\nFor selection, LP achieves $+1.36$~pp on Few-NERD ($p{<}0.001$) when two conditions are jointly met: low instance degeneracy (13.8\\%) and adequate alignment ($\\rho{\\approx}0.5$), with gains scaling with $N$ ($+0.52$~pp, $p{=}0.003$).\nOn SciERC, the observed LP gain ($+0.2$~pp, $p{=}0.29$) falls below the minimum detectable effect (${\\approx}$1.5~pp at 80\\% power, $n{=}529$) despite 13~pp oracle headroom. We term this disparity between quality estimation strength and selection effectiveness the \\textbf{correlation-selection gap}.\nTwo mechanisms explain this gap: (a)~\\textit{instance degeneracy} (14\\textendash 59\\% of instances yield identical F1 scores across all $N$ samples, eliminating headroom); and (b)~\\textit{weak LP-quality alignment} (within-instance $\\rho(\\text{LP}, \\text{F1})$ too low to exploit the remaining headroom; \\S\\ref{sec:discussion}).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. \\textbf{Left}: consistency signals reliably predict instance-level quality ($\\rho$ up to 0.45 on CoNLL, 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82). \\textbf{Right}: quality estimation does not translate to selection; all methods approximately match greedy decoding ($T{=}0$) despite 13~pp oracle headroom (\\S\\ref{sec:discussion}).}\n\\label{fig:overview}\n\\end{figure*}\n\nWe evaluate five signals from three families (structural, surface, and model-internal) on SciERC \\cite{luan2018scierc} as a primary medium-difficulty test bed, with Few-NERD \\cite{ding2021fewnerd} (low-degeneracy contrast), CoNLL-2003 \\cite{tjongkimsang2003conll} (ceiling-effect control), and WNUT-17 \\cite{derczynski2017wnut} (signal-collapse boundary), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).\nWe vary candidate pool size ($N{\\in}\\{2,\\ldots,32\\}$), signal sophistication, and model capacity within the 4B\\textendash 8B range; behavior at 70B+ scales remains an open question.\nAn exploratory extension to relation extraction is reported in Appendix~\\ref{app:re_extension}.\nOur contributions:\n\\begin{enumerate}\n    \\item \\textbf{Quality estimation framework and a methodological premise.}\n    Five signals from three families evaluated on four NER benchmarks, two model families, and a 4B ablation, achieving reliable quality estimation ($\\rho$ up to 0.45; AUROC up to 0.82).\n    A definitional observation structures the analysis: four of five signals are instance-level aggregates that by design assign identical scores to all candidates; this per-sample vs.\\ instance-level distinction determines which signals can, in principle, improve selection.\n\n    \\item \\textbf{Two empirical mechanisms underlying the correlation-selection gap.}\n    Instance degeneracy (14\\textendash 59\\% of instances yield identical F1 scores across all samples) eliminates headroom for consensus-based selection; weak LP-quality alignment (within-instance $\\rho{\\approx}0.24$ on SciERC) prevents exploiting the remaining headroom.\n    Temperature ablation provides the primary evidence that both conditions are independently necessary ($T{=}1.2$: degeneracy 12.5\\%, alignment $\\rho{=}0.225$; \\S\\ref{sec:discussion}); LoRA-rank, entity-token LP, and supervised combination of the five signals studied corroborate the pattern.\n\n    \\item \\textbf{Practical conditions for LP selection.}\n    LP achieves $+1.36$~pp on Few-NERD ($p{<}0.001$) and scales with $N$ ($+0.52$~pp, $p{=}0.003$) when degeneracy ${<}$15\\% and alignment $\\rho \\gtrsim 0.3$.\n    Per-entity-type analysis within Few-NERD ($\\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$; types share model and tokenizer, so effective degrees of freedom may be lower) provides supporting evidence; temperature and training convergence offer controllable levers for degeneracy.\n\\end{enumerate}\n\n",
      "numLines": 42,
      "startLine": 1,
      "totalLines": 42
    }
  },
  "sourceToolAssistantUUID": "c535919e-3e53-410b-9c6e-b27cf876b88b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-18T05:56:15.113Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H1Q9K7Da5AhC5gaPhm3sYF`</summary>

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
  "parentUuid": "58b04b08-1a62-431e-9d2a-e2bce8faf069",
  "isSidechain": false,
  "requestId": "req_011Cb9X33FVzJKz6tBm9Mku9",
  "type": "assistant",
  "uuid": "0e3f65f3-24fb-4dc5-a318-ad37de2b2fab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqfzDGtSVd3kv38f1NSNoq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1831,
      "cache_read_input_tokens": 32053,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1831,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 32053,
          "cache_creation_input_tokens": 1831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1831
          },
          "type": "message"
        }
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

_source line 33 · 2026-05-18T05:56:15.120Z_

<details><summary>↩ Tool result · `toolu_01H1Q9K7Da5AhC5gaPhm3sYF`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement; \citet{feng2025optimal} and \citet{wang2025make} adapt to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
6	We extend self-consistency to set-valued structured outputs and identify the correlation-selection gap.
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation is necessary but not sufficient, diagnosing degeneracy and compression as blocking mechanisms.
10	Our experiments use fine-tuned models, where degeneracy is most pronounced and is modulated by task structure and training convergence (Appendix~\ref{app:epoch_confound}).
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization; our supervised verifier baseline (\S\ref{sec:robustness_main}) suggests combination strategy is not the bottleneck.
12	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
13	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided, park2024grammar, schall2025hidden, yun2025price}.
14	
15	\paragraph{Uncertainty estimation and MBR decoding.}
16	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic}; semantic uncertainty \cite{kuhn2023semantic} and P(True) \cite{kadavath2022language} provide model-internal alternatives.
17	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \cite{freitag2022high} and code generation where execution-based MBR improves selection \cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\rho{=}0.52$; \S\ref{sec:discussion}).
18	\citet{eikema2025structured} find MBR utilities degrade on structured outputs; our diagnosis is complementary: degeneracy, not utility misalignment, is the primary bottleneck.
19	Our QE results connect to selective prediction \cite{kuleshov2015calibrated}: signals with AUROC up to 0.82 support abstention policies independent of sample selection.
20	
21	\paragraph{Best-of-$N$ with learned verifiers.}
22	\citet{gao2023scaling} establish BoN scaling laws; our unsupervised signals face a more fundamental limitation than reward overoptimization.
23	Trained verifiers \cite{cobbe2021verifiers, lightman2024verify, fernandes2022quality} learn per-sample scoring; reward model ensembles mitigate but do not eliminate reward hacking \cite{eisenstein2023helping}. Our LoRA-rank ablation (degeneracy 7.2\%, selection still shows no improvement at $\rho{\approx}0.24$) suggests that, within the five unsupervised signals studied, increasing output diversity alone is insufficient.
24	Fine-tuning contributes to degeneracy, analogous to diversity collapse in RLHF \cite{kirk2024understanding}; constrained structured outputs limit the diversity that temperature scaling \cite{holtzman2020curious} or diverse decoding \cite{vijayakumar2018diverse} can recover.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e3f65f3-24fb-4dc5-a318-ad37de2b2fab",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "3378bf8e-c6f8-46f4-982e-7e0859e7a927",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency \\cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \\cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.\nTest-time scaling studies \\cite{snell2025scaling, brown2024monkeys} and reward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement; \\citet{feng2025optimal} and \\citet{wang2025make} adapt to difficulty-aware settings; \\citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.\nWe extend self-consistency to set-valued structured outputs and identify the correlation-selection gap.\n\n\\paragraph{Consistency for structured IE.}\n\\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation is necessary but not sufficient, diagnosing degeneracy and compression as blocking mechanisms.\nOur experiments use fine-tuned models, where degeneracy is most pronounced and is modulated by task structure and training convergence (Appendix~\\ref{app:epoch_confound}).\nCoCoA \\cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization; our supervised verifier baseline (\\S\\ref{sec:robustness_main}) suggests combination strategy is not the bottleneck.\nEarlier work on confidence for structured prediction \\cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.\nOur evaluation builds on generative IE \\cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \\cite{willard2023guided, park2024grammar, schall2025hidden, yun2025price}.\n\n\\paragraph{Uncertainty estimation and MBR decoding.}\nSurveys cover confidence estimation \\cite{geng2024confidence}, uncertainty quantification \\cite{xia2025survey}, and calibration \\cite{hobelsberger2025systematic}; semantic uncertainty \\cite{kuhn2023semantic} and P(True) \\cite{kadavath2022language} provide model-internal alternatives.\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \\cite{freitag2022high} and code generation where execution-based MBR improves selection \\cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\\rho{=}0.52$; \\S\\ref{sec:discussion}).\n\\citet{eikema2025structured} find MBR utilities degrade on structured outputs; our diagnosis is complementary: degeneracy, not utility misalignment, is the primary bottleneck.\nOur QE results connect to selective prediction \\cite{kuleshov2015calibrated}: signals with AUROC up to 0.82 support abstention policies independent of sample selection.\n\n\\paragraph{Best-of-$N$ with learned verifiers.}\n\\citet{gao2023scaling} establish BoN scaling laws; our unsupervised signals face a more fundamental limitation than reward overoptimization.\nTrained verifiers \\cite{cobbe2021verifiers, lightman2024verify, fernandes2022quality} learn per-sample scoring; reward model ensembles mitigate but do not eliminate reward hacking \\cite{eisenstein2023helping}. Our LoRA-rank ablation (degeneracy 7.2\\%, selection still shows no improvement at $\\rho{\\approx}0.24$) suggests that, within the five unsupervised signals studied, increasing output diversity alone is insufficient.\nFine-tuning contributes to degeneracy, analogous to diversity collapse in RLHF \\cite{kirk2024understanding}; constrained structured outputs limit the diversity that temperature scaling \\cite{holtzman2020curious} or diverse decoding \\cite{vijayakumar2018diverse} can recover.\n",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  },
  "sourceToolAssistantUUID": "0e3f65f3-24fb-4dc5-a318-ad37de2b2fab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）  ### 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction - **路径**: `projects…",
  "leafUuid": "3378bf8e-c6f8-46f4-982e-7e0859e7a927",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured IE paper for EMNLP 2026",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Tool call

_source line 36 · 2026-05-18T05:56:17.710Z_

<details open><summary>🔧 Tool call — Read · `toolu_012u8GsukCUPzDB6vbzmu7Dx`</summary>

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
  "parentUuid": "3378bf8e-c6f8-46f4-982e-7e0859e7a927",
  "isSidechain": false,
  "requestId": "req_011Cb9X3Fi75CwqAmRkoYHPs",
  "type": "assistant",
  "uuid": "d3330051-e300-43a4-bf78-341d5b211587",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyfTUaCsF2meoisUQjNxq5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1197,
      "cache_read_input_tokens": 33884,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1197,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 33884,
          "cache_creation_input_tokens": 1197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1197
          },
          "type": "message"
        }
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

_source line 37 · 2026-05-18T05:56:17.715Z_

<details><summary>↩ Tool result · `toolu_012u8GsukCUPzDB6vbzmu7Dx`</summary>

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
39	where $M$ is the matched set, $\text{sim}(a_m, b_m)$ is the token-level IoU, and $\max(|g_i|, |g_j|)$ penalizes length asymmetry.\footnote{The two normalizer variants produce nearly identical rankings ($|\Delta\rho|{\leq}0.009$; Table~\ref{tab:sj_normalizer}).}
40	The instance-level QE signal averages over all pairs: $c_{\text{sj}}(x) = \binom{N}{2}^{-1} \sum_{i&lt;j} \text{SJ}(y_i, y_j)$.
41	For selection, consensus-proximity converts this to per-sample utility $u_{\text{sj}}(y_i) = (N{-}1)^{-1} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, equivalent to MBR decoding \cite{eikema2022sampling}. The same construction applies to FK, EM, and VC.
42	
43	\paragraph{Entity voting confidence (structural, instance-level).}
44	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
45	The instance-level confidence is the mean frequency:
46	\begin{equation}\label{eq:voting}
47	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
48	\end{equation}
49	When $E_\cup = \emptyset$, $c_{\mathrm{vc}}(x) = 0$.\footnote{For voted-output \textit{selection}, we include only entities with frequency ${>}N/2$ (standard majority voting).}
50	
51	\subsection{Evaluation Framework}\label{sec:evaluation}
52	
53	\paragraph{Quality estimation.}
54	Spearman $\rho$ between the signal and instance-level F1, and AUROC classifying instances as above/below median F1.
55	Both quality estimation and selection exclude instances with no gold annotations: $n{=}529$ on SciERC (from 551), $n{=}2{,}756$ on CoNLL (from 3{,}453).\footnote{On CoNLL, full-set ($n{=}3{,}453$) Spearman $\rho$ values are higher than gold-filtered ($n{=}2{,}756$) by $+0.03$--$0.05$ due to the zero/non-zero boundary inflating correlations, paralleling the effect documented for WNUT-17 in Appendix~\ref{app:additional}.}
56	
57	\paragraph{Sample selection.}
58	Best-of-$N$ F1: per-sample signals (LP) directly rank candidates; instance-level signals rank via consensus-proximity (MBR utility; see SJ definition above).
59	Baselines: \textit{oracle} (highest-F1 sample) and \textit{greedy} ($T{=}0$ argmax decoding).
60	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3330051-e300-43a4-bf78-341d5b211587",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "74027831-348b-4646-bee5-d0ff4a304640",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven model $\\mathcal{M}$ and input $x$, we sample $N$ outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}, where each $y_i$ is an entity set.\nA \\textbf{per-sample signal} $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$ scores each output independently; an \\textbf{instance-level signal} $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$ produces a single score per input (notation in Appendix~\\ref{app:notation}).\nThis distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\\S\\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nFour are \\textit{consistency signals}: \\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \\textit{surface} (exact match [EM], Fleiss' $\\kappa$ [FK]); log-probability [LP] is the sole \\textit{model-internal}, per-sample signal.\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{&lt;j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed and $\\bar{P}_e$ expected agreement.\nTemperature-based sampling introduces mild negative dependence ($-$0.4\\% to $-$4.0\\%; Appendix~\\ref{app:fk_independence}), which does not inflate FK.\nUnlike structural signals, FK relies on exact string matching.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nFor samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU), and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set, $\\text{sim}(a_m, b_m)$ is the token-level IoU, and $\\max(|g_i|, |g_j|)$ penalizes length asymmetry.\\footnote{The two normalizer variants produce nearly identical rankings ($|\\Delta\\rho|{\\leq}0.009$; Table~\\ref{tab:sj_normalizer}).}\nThe instance-level QE signal averages over all pairs: $c_{\\text{sj}}(x) = \\binom{N}{2}^{-1} \\sum_{i&lt;j} \\text{SJ}(y_i, y_j)$.\nFor selection, consensus-proximity converts this to per-sample utility $u_{\\text{sj}}(y_i) = (N{-}1)^{-1} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, equivalent to MBR decoding \\cite{eikema2022sampling}. The same construction applies to FK, EM, and VC.\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\nWhen $E_\\cup = \\emptyset$, $c_{\\mathrm{vc}}(x) = 0$.\\footnote{For voted-output \\textit{selection}, we include only entities with frequency ${>}N/2$ (standard majority voting).}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nSpearman $\\rho$ between the signal and instance-level F1, and AUROC classifying instances as above/below median F1.\nBoth quality estimation and selection exclude instances with no gold annotations: $n{=}529$ on SciERC (from 551), $n{=}2{,}756$ on CoNLL (from 3{,}453).\\footnote{On CoNLL, full-set ($n{=}3{,}453$) Spearman $\\rho$ values are higher than gold-filtered ($n{=}2{,}756$) by $+0.03$--$0.05$ due to the zero/non-zero boundary inflating correlations, paralleling the effect documented for WNUT-17 in Appendix~\\ref{app:additional}.}\n\n\\paragraph{Sample selection.}\nBest-of-$N$ F1: per-sample signals (LP) directly rank candidates; instance-level signals rank via consensus-proximity (MBR utility; see SJ definition above).\nBaselines: \\textit{oracle} (highest-F1 sample) and \\textit{greedy} ($T{=}0$ argmax decoding).\n",
      "numLines": 60,
      "startLine": 1,
      "totalLines": 60
    }
  },
  "sourceToolAssistantUUID": "d3330051-e300-43a4-bf78-341d5b211587",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-18T05:56:20.540Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MeCVPN1nBSCCMfs71mYkRh`</summary>

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
  "parentUuid": "74027831-348b-4646-bee5-d0ff4a304640",
  "isSidechain": false,
  "requestId": "req_011Cb9X3T6iFxEh7HUxyiuY6",
  "type": "assistant",
  "uuid": "afe494ef-690c-430c-a48a-12d15371be5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KyJyQZKDkUkdVczPW5v7oM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1983,
      "cache_read_input_tokens": 35081,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 35081,
          "cache_creation_input_tokens": 1983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1983
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-18T05:56:20.545Z_

<details><summary>↩ Tool result · `toolu_01MeCVPN1nBSCCMfs71mYkRh`</summary>

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
15	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, except Few-NERD models which use 3 epochs (early stopping at the best validation checkpoint; a 5-epoch control confirms LP selection remains positive though gains are halved; Appendix~\ref{app:epoch_confound}).
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
48	On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
49	On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$).
50	At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
51	
52	%% ============================================================
53	\subsection{The Correlation-Selection Gap}
54	\label{sec:selection_gap}
55	
56	Two mechanisms block selection: instance degeneracy collapses the candidate pool for consensus-based approaches, and weak LP-quality alignment prevents exploiting the remaining headroom.
57	A methodological observation underlies both: four instance-level signals cannot rank candidates by construction; LP requires both low degeneracy and adequate alignment ($\rho \gtrsim 0.3$).
58	
59	\begin{table}[t]
60	\centering
61	\small
62	\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \textbf{bold}. Non-tied subset in \S\ref{sec:discussion}; RE in Appendix~\ref{app:re_extension}.}
63	\label{tab:selection}
64	\begin{tabular}{lcc}
65	\toprule
66	Method & NER F1 & $p$ \\
67	\midrule
68	Oracle & $0.778 \pm 0.003$ & --- \\
69	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
70	\midrule
71	\multicolumn{3}{l}{\textit{Per-sample signal}} \\
72	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
73	\midrule
74	\multicolumn{3}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
75	SJ           & $0.646 \pm 0.002$ & .67 \\
76	FK           & $0.646 \pm 0.001$ & .79 \\
77	EM           & $0.637 \pm 0.001$ & --- \\
78	VC           & $0.623 \pm 0.004$ & --- \\
79	\midrule
80	Random           & $0.610 \pm 0.003$ & --- \\
81	\bottomrule
82	\end{tabular}
83	\end{table}
84	
85	Despite moderate quality estimation, no signal consistently improves selection over greedy (Table~\ref{tab:selection}).
86	Instance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed.
87	
88	\paragraph{No significant improvement over greedy.}
89	On SciERC ($n{=}529$, 2-seed sign tests\footnote{Seed variation $\sigma{\leq}0.026$ (Table~\ref{tab:multiseed}); MDE${\approx}$1.5~pp at 80\% power for $n{=}529$, so a 1~pp effect yields only ${\sim}$55\% power. Few-NERD ($n{=}32{,}565$; MDE${\approx}$0.22~pp) provides the definitive test.}), the oracle (0.778) reveals 13.3~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\approx}$1.5~pp).
90	The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \textit{degradation} (Appendix~\ref{app:tost}).
91	Few-NERD provides the definitive contrast: LP achieves $+1.36$~pp ($p{<}0.001$) at low degeneracy (\S\ref{sec:fewnerd}), while structural signals still degrade selection.
92	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best; closing this gap likely requires trained verifiers \cite{cobbe2021verifiers}.\footnote{The sole positive finding (non-tied LP subset, $+2.9$~pp, $p{=}0.004$; \S\ref{sec:discussion}) survives Bonferroni correction over 5 comparisons.}
93	
94	%% ============================================================
95	\subsection{Cross-Dataset Contrast: Few-NERD}
96	\label{sec:fewnerd}
97	
98	\begin{table}[t]
99	\centering
100	\small
101	\caption{Cross-dataset comparison of LP selection effectiveness (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). LP $\rho$: Spearman correlation between max token-level log-probability and instance F1. LP selection gains are inversely associated with instance degeneracy.\protect\footnotemark\protect\footnotemark}
102	\label{tab:fewnerd}
103	\begin{tabular}{lcccccc}
104	\toprule
105	Dataset & $n$ & Greedy & Headroom & Degen\% & LP $\rho$ & LP $\Delta$ \\
106	\midrule
107	CoNLL & 2{,}756 & .908 & 4.0\,pp & 59.1\% & .302 & $-$1.05\,pp \\
108	SciERC & 529 & .644 & 13.2\,pp & 17.8\% & .215 & $+$0.61\,pp \\
109	Few-NERD & 32{,}565 & .748 & 12.4\,pp & 13.8\% & .421 & $\mathbf{+1.36}$\,pp \\
110	\bottomrule
111	\end{tabular}
112	\end{table}
113	\footnotetext{SciERC values (greedy${=}0.644$, headroom${=}13.2$~pp) differ slightly from Table~\ref{tab:selection} (greedy${=}0.645$, headroom${=}13.3$~pp) due to max-LP aggregation and single-seed evaluation; the ranking is unchanged.}
114	\footnotetext{Instance degeneracy: fraction of gold-filtered instances where all $N$ samples produce identical instance-level F1.}
115	
116	Few-NERD (Table~\ref{tab:fewnerd}) confirms that LP selection effectiveness is inversely associated with degeneracy.
117	Under standard early stopping, Few-NERD degeneracy is 13.8\% (training convergence modulates this rate, Appendix~\ref{app:epoch_confound}), and LP achieves $+1.36$~pp (95\% CI $[+1.18, +1.53]$, $p{<}0.001$), while all structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp).
118	
119	\paragraph{Two necessary conditions for LP selection.}
120	The cross-dataset gradient is consistent with an inverse relationship (59.1\% $\to$ $-1.05$~pp, 17.8\% $\to$ $+0.61$~pp, 13.8\% $\to$ $+1.36$~pp; $n{=}3$ datasets, exploratory given 5+ confounds; Figure~\ref{fig:degeneracy_scatter}), with supporting evidence from per-entity-type analysis within Few-NERD ($n{=}8$, $\rho{=}{-}0.881$, $p{=}0.004$; entity types share model, tokenizer, and temperature, so effective degrees of freedom may be lower than 6).
121	Low degeneracy alone is not sufficient: the LoRA-rank ablation (\S\ref{sec:robustness_main}) reduces degeneracy to 7.2\% yet LP does not improve selection because $\rho(\text{LP}, \text{F1}){\approx}0.24$.
122	Few-NERD satisfies both conditions: low degeneracy (13.8\%) and strong alignment ($\rho{\approx}0.5$; per-type detail in Appendix~\ref{app:per_type_lp}).
123	All five signals achieve positive QE on Few-NERD (LP $\rho{=}0.42$, VC $0.39$), yet only LP translates QE into selection; the gap confirms that strong instance-level QE cannot rank candidates within an instance.
124	
125	\begin{figure}[t]
126	\centering
127	\includegraphics[width=\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}
128	\caption{Instance degeneracy vs.\ LP selection gain. Blue circles: cross-dataset ($n{=}3$, exploratory). Orange triangles: per-entity-type within Few-NERD ($n{=}8$, $\rho{=}{-}0.881$, $p{=}0.004$; types share model and tokenizer). The dashed line at ${\sim}$15\%\protect\footnotemark{} separates regimes where LP improves (left) vs.\ shows insufficient evidence (right).}
129	\label{fig:degeneracy_scatter}
130	\end{figure}
131	
132	\footnotetext{Boundary between Person (13.4\%, $+1.25$~pp) and Art (19.8\%, $-0.17$~pp).}
133	
134	\paragraph{LP selection scales with sample budget.}
135	Doubling $N$ from 8 to 16 on Few-NERD yields $+0.52$~pp (paired $p{=}0.003$, CI $[+0.17, +0.87]$), driven by reduced degeneracy (14.6\% $\to$ 7.0\%) expanding headroom (12.1 $\to$ 15.4~pp), while LP ranking quality remains stable ($\rho{\approx}0.62$).
136	Structural signals remain uniformly negative at $N{=}16$; the gap persists regardless of sample budget.
137	
138	%% ============================================================
139	\subsection{Robustness}
140	\label{sec:robustness_main}
141	
142	Consistency signals are robust across $T{\in}\{0.7, 1.0\}$ with sublinear $N$-scaling gains (Table~\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\Delta\rho{=}{+}0.044$).
143	Signal rankings are stable across seeds (Kendall's $W{=}1.0$ at $N{=}8$, though statistical precision is limited with $m{=}3$ raters, exact $p{\approx}0.028$; Table~\ref{tab:ranking-stability}).
144	NER calibration is reasonable (ECE 0.069--0.096; Appendix~\ref{app:calibration}).
145	
146	\begin{table}[t]
147	\centering
148	\small
149	\caption{Scale ablation: Qwen3-8B vs.\ 4B NER quality estimation ($\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. RE scale ablation in Appendix~\ref{app:re_extension}.}
150	\label{tab:scale_ablation}
151	\begin{tabular}{@{}ll cc r@{}}
152	\toprule
153	& & \textbf{8B} & \textbf{4B} & $\Delta$ \\
154	\midrule
155	CoNLL & SJ & .436 & .422 & $-$.014 \\
156	      & FK & .400 & .418 & $+$.018 \\
157	SciERC & SJ & .360 & .422 & $+$.062 \\
158	       & FK & .267 & .326 & $+$.059 \\
159	\bottomrule
160	\end{tabular}
161	\end{table}
162	
163	\paragraph{Scale robustness.}
164	With Qwen3-4B (Table~\ref{tab:scale_ablation}), QE is comparable (mean $|\Delta\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\ref{app:llama3b}).
165	Degeneracy scales with capability: 8B shows 17.8\% vs.\ 4B's 10.4\% on SciERC (Table~\ref{tab:degeneracy}).
166	
167	\paragraph{LoRA-rank ablation.}
168	Training with LoRA rank${=}8$ (vs.\ 32) lowers degeneracy from 17.8\% to 7.2\% and increases headroom to 16.0~pp, but LP does not improve selection (0.635 vs.\ greedy 0.640).
169	This ablation conflates diversity with model capacity (rank 8 has fewer trainable parameters); within-instance $\rho(\text{LP}, \text{F1}){\approx}0.24$ remains too weak despite wider LP spread (0.057 vs.\ 0.041 nats).
170	Temperature manipulation (\S\ref{sec:discussion}) provides a cleaner test by altering diversity without changing capacity, and yields the same conclusion: both low degeneracy and adequate alignment are independently necessary.
171	
172	\paragraph{Supervised verifier baseline.}
173	Supervised verifiers (logistic regression, MLP, random forest) trained on all five signals (3-fold CV, SciERC, $N{=}16$, $+17.9$~pp headroom) all perform at or below greedy\footnote{Greedy F1 is 0.644 (3-seed mean), consistent with Table~\ref{tab:selection}.} (LR: $-0.3$~pp; MLP: $-0.6$~pp; RF: $-2.9$~pp).
174	Adding pairwise interaction features does not help (AUROC 0.632 vs.\ 0.639).
175	Within these five unsupervised signals, the bottleneck is in what they encode, not how they are combined; whether richer representations (e.g., hidden states, entity embeddings) could close the gap remains untested.
176	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afe494ef-690c-430c-a48a-12d15371be5c",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "cb020667-660d-48d0-bbba-205ec72609dd",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 52\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, except Few-NERD models which use 3 epochs (early stopping at the best validation checkpoint; a 5-epoch control confirms LP selection remains positive though gains are halved; Appendix~\\ref{app:epoch_confound}).\nQwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\\ref{app:thinking_token}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\\ref{app:n_scaling}).}\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\\footnote{Quality estimation uses a single primary seed (seed${=}42$); selection uses 2-seed averages for variance estimation. Three-seed experiments ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}) confirm ranking stability; the reduced seed count for primary results reflects computational budget.}\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. RE results in Appendix~\\ref{app:re_extension}. $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models.\\footnote{$\\varepsilon{=}0.05$ applies only to selection (\\S\\ref{sec:selection_gap}); quality estimation is $\\varepsilon$-free. Selection F1 is stable across $\\varepsilon \\in [0, 0.2]$ (Appendix~\\ref{app:epsilon_robustness}).}\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$).\nAt the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nTwo mechanisms block selection: instance degeneracy collapses the candidate pool for consensus-based approaches, and weak LP-quality alignment prevents exploiting the remaining headroom.\nA methodological observation underlies both: four instance-level signals cannot rank candidates by construction; LP requires both low degeneracy and adequate alignment ($\\rho \\gtrsim 0.3$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. Non-tied subset in \\S\\ref{sec:discussion}; RE in Appendix~\\ref{app:re_extension}.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & $p$ \\\\\n\\midrule\nOracle & $0.778 \\pm 0.003$ & --- \\\\\nGreedy ($T{=}0$) & $0.645 \\pm 0.001$ & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .67 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 \\\\\nEM           & $0.637 \\pm 0.001$ & --- \\\\\nVC           & $0.623 \\pm 0.004$ & --- \\\\\n\\midrule\nRandom           & $0.610 \\pm 0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite moderate quality estimation, no signal consistently improves selection over greedy (Table~\\ref{tab:selection}).\nInstance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed.\n\n\\paragraph{No significant improvement over greedy.}\nOn SciERC ($n{=}529$, 2-seed sign tests\\footnote{Seed variation $\\sigma{\\leq}0.026$ (Table~\\ref{tab:multiseed}); MDE${\\approx}$1.5~pp at 80\\% power for $n{=}529$, so a 1~pp effect yields only ${\\sim}$55\\% power. Few-NERD ($n{=}32{,}565$; MDE${\\approx}$0.22~pp) provides the definitive test.}), the oracle (0.778) reveals 13.3~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\\approx}$1.5~pp).\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \\textit{degradation} (Appendix~\\ref{app:tost}).\nFew-NERD provides the definitive contrast: LP achieves $+1.36$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best; closing this gap likely requires trained verifiers \\cite{cobbe2021verifiers}.\\footnote{The sole positive finding (non-tied LP subset, $+2.9$~pp, $p{=}0.004$; \\S\\ref{sec:discussion}) survives Bonferroni correction over 5 comparisons.}\n\n%% ============================================================\n\\subsection{Cross-Dataset Contrast: Few-NERD}\n\\label{sec:fewnerd}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-dataset comparison of LP selection effectiveness (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). LP $\\rho$: Spearman correlation between max token-level log-probability and instance F1. LP selection gains are inversely associated with instance degeneracy.\\protect\\footnotemark\\protect\\footnotemark}\n\\label{tab:fewnerd}\n\\begin{tabular}{lcccccc}\n\\toprule\nDataset & $n$ & Greedy & Headroom & Degen\\% & LP $\\rho$ & LP $\\Delta$ \\\\\n\\midrule\nCoNLL & 2{,}756 & .908 & 4.0\\,pp & 59.1\\% & .302 & $-$1.05\\,pp \\\\\nSciERC & 529 & .644 & 13.2\\,pp & 17.8\\% & .215 & $+$0.61\\,pp \\\\\nFew-NERD & 32{,}565 & .748 & 12.4\\,pp & 13.8\\% & .421 & $\\mathbf{+1.36}$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\\footnotetext{SciERC values (greedy${=}0.644$, headroom${=}13.2$~pp) differ slightly from Table~\\ref{tab:selection} (greedy${=}0.645$, headroom${=}13.3$~pp) due to max-LP aggregation and single-seed evaluation; the ranking is unchanged.}\n\\footnotetext{Instance degeneracy: fraction of gold-filtered instances where all $N$ samples produce identical instance-level F1.}\n\nFew-NERD (Table~\\ref{tab:fewnerd}) confirms that LP selection effectiveness is inversely associated with degeneracy.\nUnder standard early stopping, Few-NERD degeneracy is 13.8\\% (training convergence modulates this rate, Appendix~\\ref{app:epoch_confound}), and LP achieves $+1.36$~pp (95\\% CI $[+1.18, +1.53]$, $p{<}0.001$), while all structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp).\n\n\\paragraph{Two necessary conditions for LP selection.}\nThe cross-dataset gradient is consistent with an inverse relationship (59.1\\% $\\to$ $-1.05$~pp, 17.8\\% $\\to$ $+0.61$~pp, 13.8\\% $\\to$ $+1.36$~pp; $n{=}3$ datasets, exploratory given 5+ confounds; Figure~\\ref{fig:degeneracy_scatter}), with supporting evidence from per-entity-type analysis within Few-NERD ($n{=}8$, $\\rho{=}{-}0.881$, $p{=}0.004$; entity types share model, tokenizer, and temperature, so effective degrees of freedom may be lower than 6).\nLow degeneracy alone is not sufficient: the LoRA-rank ablation (\\S\\ref{sec:robustness_main}) reduces degeneracy to 7.2\\% yet LP does not improve selection because $\\rho(\\text{LP}, \\text{F1}){\\approx}0.24$.\nFew-NERD satisfies both conditions: low degeneracy (13.8\\%) and strong alignment ($\\rho{\\approx}0.5$; per-type detail in Appendix~\\ref{app:per_type_lp}).\nAll five signals achieve positive QE on Few-NERD (LP $\\rho{=}0.42$, VC $0.39$), yet only LP translates QE into selection; the gap confirms that strong instance-level QE cannot rank candidates within an instance.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n\\caption{Instance degeneracy vs.\\ LP selection gain. Blue circles: cross-dataset ($n{=}3$, exploratory). Orange triangles: per-entity-type within Few-NERD ($n{=}8$, $\\rho{=}{-}0.881$, $p{=}0.004$; types share model and tokenizer). The dashed line at ${\\sim}$15\\%\\protect\\footnotemark{} separates regimes where LP improves (left) vs.\\ shows insufficient evidence (right).}\n\\label{fig:degeneracy_scatter}\n\\end{figure}\n\n\\footnotetext{Boundary between Person (13.4\\%, $+1.25$~pp) and Art (19.8\\%, $-0.17$~pp).}\n\n\\paragraph{LP selection scales with sample budget.}\nDoubling $N$ from 8 to 16 on Few-NERD yields $+0.52$~pp (paired $p{=}0.003$, CI $[+0.17, +0.87]$), driven by reduced degeneracy (14.6\\% $\\to$ 7.0\\%) expanding headroom (12.1 $\\to$ 15.4~pp), while LP ranking quality remains stable ($\\rho{\\approx}0.62$).\nStructural signals remain uniformly negative at $N{=}16$; the gap persists regardless of sample budget.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\\Delta\\rho{=}{+}0.044$).\nSignal rankings are stable across seeds (Kendall's $W{=}1.0$ at $N{=}8$, though statistical precision is limited with $m{=}3$ raters, exact $p{\\approx}0.028$; Table~\\ref{tab:ranking-stability}).\nNER calibration is reasonable (ECE 0.069--0.096; Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: Qwen3-8B vs.\\ 4B NER quality estimation ($\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. RE scale ablation in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL & SJ & .436 & .422 & $-$.014 \\\\\n      & FK & .400 & .418 & $+$.018 \\\\\nSciERC & SJ & .360 & .422 & $+$.062 \\\\\n       & FK & .267 & .326 & $+$.059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nWith Qwen3-4B (Table~\\ref{tab:scale_ablation}), QE is comparable (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\\ref{app:llama3b}).\nDegeneracy scales with capability: 8B shows 17.8\\% vs.\\ 4B's 10.4\\% on SciERC (Table~\\ref{tab:degeneracy}).\n\n\\paragraph{LoRA-rank ablation.}\nTraining with LoRA rank${=}8$ (vs.\\ 32) lowers degeneracy from 17.8\\% to 7.2\\% and increases headroom to 16.0~pp, but LP does not improve selection (0.635 vs.\\ greedy 0.640).\nThis ablation conflates diversity with model capacity (rank 8 has fewer trainable parameters); within-instance $\\rho(\\text{LP}, \\text{F1}){\\approx}0.24$ remains too weak despite wider LP spread (0.057 vs.\\ 0.041 nats).\nTemperature manipulation (\\S\\ref{sec:discussion}) provides a cleaner test by altering diversity without changing capacity, and yields the same conclusion: both low degeneracy and adequate alignment are independently necessary.\n\n\\paragraph{Supervised verifier baseline.}\nSupervised verifiers (logistic regression, MLP, random forest) trained on all five signals (3-fold CV, SciERC, $N{=}16$, $+17.9$~pp headroom) all perform at or below greedy\\footnote{Greedy F1 is 0.644 (3-seed mean), consistent with Table~\\ref{tab:selection}.} (LR: $-0.3$~pp; MLP: $-0.6$~pp; RF: $-2.9$~pp).\nAdding pairwise interaction features does not help (AUROC 0.632 vs.\\ 0.639).\nWithin these five unsupervised signals, the bottleneck is in what they encode, not how they are combined; whether richer representations (e.g., hidden states, entity embeddings) could close the gap remains untested.\n",
      "numLines": 176,
      "startLine": 1,
      "totalLines": 176
    }
  },
  "sourceToolAssistantUUID": "afe494ef-690c-430c-a48a-12d15371be5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）  ### 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction - **路径**: `projects…",
  "leafUuid": "cb020667-660d-48d0-bbba-205ec72609dd",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured IE paper for EMNLP 2026",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Tool call

_source line 42 · 2026-05-18T05:56:24.769Z_

<details open><summary>🔧 Tool call — Read · `toolu_018WJroxNVNKkBzp1UiX7Fam`</summary>

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
  "parentUuid": "cb020667-660d-48d0-bbba-205ec72609dd",
  "isSidechain": false,
  "requestId": "req_011Cb9X3eqeU2qYGyojpcvvJ",
  "type": "assistant",
  "uuid": "f45815ec-27b2-4992-81a3-e4dac4f223f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YygxNZegY6gs4MnHydMgX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5598,
      "cache_read_input_tokens": 37064,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5598,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 37064,
          "cache_creation_input_tokens": 5598,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5598
          },
          "type": "message"
        }
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

_source line 43 · 2026-05-18T05:56:24.773Z_

<details><summary>↩ Tool result · `toolu_018WJroxNVNKkBzp1UiX7Fam`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications for practitioners.}
4	All signals achieve positive quality estimation across non-collapsed datasets (LP $\rho{=}0.42$ on Few-NERD, VC $\rho{=}0.38$ on SciERC, EM AUROC${=}0.82$ on CoNLL), with rankings stable across model families and a 4B ablation (Table~\ref{tab:scale_ablation}).
5	For selection, LP achieves significant gains only when both conditions are met ($+1.36$~pp on Few-NERD, $p{<}0.001$; Table~\ref{tab:fewnerd}); structural signals uniformly degrade selection.
6	RE signal rankings are in Appendix~\ref{app:re_extension}.
7	
8	\paragraph{Why the gap exists.}
9	Two mechanisms block selection: \textit{instance degeneracy} (consensus-proximity) and \textit{weak LP-quality alignment} (per-sample).
10	Within non-degenerate instances, MBR utility \cite{eikema2022sampling} correlates positively with F1 (SJ median $\rho{=}0.524$) and closes 23--41\% of the oracle gap, but 17.8\% (SciERC) to 59.1\% (CoNLL) of instances produce identical F1 across all samples, eliminating headroom entirely (Table~\ref{tab:degeneracy}).
11	Degeneracy is determined by the interplay of task structure, model architecture, and training convergence (Appendix~\ref{app:epoch_confound}); cross-model evidence (LLaMA 86.4\% vs.\ Qwen 59.1\% on CoNLL; Table~\ref{tab:cross_selection}) reinforces the pattern.
12	LP is severely compressed (median range 0.041 nats; Table~\ref{tab:logprob_ties}), with pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$.
13	
14	\paragraph{Non-tied subset and $N$-scaling.}
15	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), within-instance $\rho$ rises to 0.39 and LP selection yields $+2.9$~pp ($p{=}0.004$, survives Bonferroni; Table~\ref{tab:nontied_main}).
16	LP scales with $N$ in the low-degeneracy regime ($+0.52$~pp from $N{=}8$ to 16 on Few-NERD, $p{=}0.003$; \S\ref{sec:fewnerd}); on SciERC, even $N{=}32$ captures less than 5\% of headroom (Table~\ref{tab:n_scaling_selection}).
17	An oracle tiebreaker within VC-equivalent groups recovers $+7.9$~pp, confirming per-sample signal exists but current signals cannot extract it (full analyses in Appendices~\ref{app:n_scaling}, \ref{app:verbalized_confidence}, \ref{app:vc_quartile}).
18	
19	\paragraph{LP compression mechanisms.}
20	Four non-mutually-exclusive mechanisms contribute: token-level averaging, schema-dominated tokens, vocabulary restriction under constrained decoding, and format-token dilution.
21	Free-form decoding rules out constraint-imposed mechanisms for NER (std ratio 0.97; Appendix~\ref{app:freeform_ablation}) but restores LP selection for RE ($+2.35$~pp, $p{=}0.025$; Appendix~\ref{app:re_extension}).
22	Entity-token LP exhibits $4{\times}$ higher variance yet performs worse ($-2.0$~pp SciERC, $-3.3$~pp CoNLL): fine-tuned models assign near-deterministic probabilities at the representation level, and compression cannot be broken by disaggregating to entity tokens.
23	LP failures show cross-seed stability (Jaccard${=}0.42$; Appendix~\ref{app:lp_failure_stability}), consistent with a systematic failure mode.
24	
25	\paragraph{Regime boundaries.}
26	At the low-resource boundary (WNUT-17), QE signals collapse (VC conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); at the ceiling boundary (CoNLL, degeneracy 59--86\%), LP degrades selection ($-1.05$~pp).
27	In the moderate regime, two conditions jointly determine effectiveness.
28	Temperature manipulation provides the primary evidence ($T{=}1.2$: degeneracy 12.5\%, $\rho{=}0.225$; Table~\ref{tab:t_degeneracy}): it alters output diversity without changing model capacity, isolating the degeneracy lever from alignment.
29	Even at degeneracy approaching Few-NERD levels (12.5\% vs.\ 13.8\%), LP does not improve selection because alignment remains weak ($\rho{=}0.225$ vs.\ Few-NERD ${\sim}$0.5).
30	LoRA rank${=}8$ (degeneracy 7.2\%, $\rho{=}0.24$) corroborates the pattern, though this ablation conflates diversity with capacity (secondary evidence).
31	The cross-dataset gradient (59\% $\to$ $-1.05$~pp, 18\% $\to$ $+0.61$~pp, 14\% $\to$ $+1.36$~pp; $n{=}3$ datasets, exploratory) is consistent with an inverse relationship; per-entity-type analysis within Few-NERD ($\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$; entity types share model and tokenizer, effective $\mathit{df}$ may be lower; Appendix~\ref{app:per_type_lp}) provides supporting evidence.
32	
33	\paragraph{Practical guidelines.}
34	Practitioners should first estimate instance degeneracy and LP-quality alignment on a labeled development set.
35	The decision rule is: if degeneracy ${<}$15\% and within-instance $\rho(\text{LP}, \text{F1}) \gtrsim 0.3$, use LP selection (Few-NERD: $+1.36$~pp, $p{<}0.001$; gains scale with $N$); otherwise, prefer greedy decoding ($T{=}0$), using structural signals for quality estimation only ($\rho{=}0.43$--$0.47$ even in the high-degeneracy regime; Table~\ref{tab:degeneracy}).
36	Temperature provides a controllable lever for degeneracy (40.3\% at $T{=}0.5$ to 12.5\% at $T{=}1.2$; Table~\ref{tab:t_degeneracy}) but cannot address alignment; training convergence offers a second lever: on Few-NERD, degeneracy rises from 11\% to 31\% between 3 and 5 epochs, halving LP gains (Table~\ref{tab:epoch_confound}); a SciERC 3-point curve (3, 5, 10 epochs) shows both conditions degrading in tandem, with degeneracy rising from 6.4\% to 47.8\% while within-instance alignment collapses ($\rho$: 0.317 $\to$ 0.282 $\to$ 0.120) and LP selection remains below detectable thresholds at all three checkpoints, confirming that degeneracy is convergence-driven rather than a fixed dataset property (Table~\ref{tab:epoch_scierc}); even at 3 epochs (degeneracy 6.4\%), SciERC alignment remains insufficient ($\rho{=}0.317$ vs.\ Few-NERD ${\sim}$0.5), reinforcing that low degeneracy alone does not guarantee selection gains.
37	Standard calibration methods preserve within-instance argmax and cannot change selection; even multi-feature variants yield no improvement ($p{=}0.31$--$0.83$; Appendix~\ref{app:calibration_baseline}), confirming the bottleneck is alignment rather than miscalibration.
38	
39	\paragraph{Methodological implications.}
40	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; even supervised combination of these five unsupervised signals does not close the oracle gap (\S\ref{sec:robustness_main}).
41	Effective selection requires content-aware verifiers \cite{cobbe2021verifiers, venktesh2025trust}; $N{=}8$ captures most QE benefit (Appendix~\ref{app:n_scaling}).
42	Structural signals are robust to domain shift when the training schema subsumes the target (Appendix~\ref{app:ood}).
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f45815ec-27b2-4992-81a3-e4dac4f223f2",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "b86e3651-bc36-4c2d-832c-8cc660e8c02b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Implications for practitioners.}\nAll signals achieve positive quality estimation across non-collapsed datasets (LP $\\rho{=}0.42$ on Few-NERD, VC $\\rho{=}0.38$ on SciERC, EM AUROC${=}0.82$ on CoNLL), with rankings stable across model families and a 4B ablation (Table~\\ref{tab:scale_ablation}).\nFor selection, LP achieves significant gains only when both conditions are met ($+1.36$~pp on Few-NERD, $p{<}0.001$; Table~\\ref{tab:fewnerd}); structural signals uniformly degrade selection.\nRE signal rankings are in Appendix~\\ref{app:re_extension}.\n\n\\paragraph{Why the gap exists.}\nTwo mechanisms block selection: \\textit{instance degeneracy} (consensus-proximity) and \\textit{weak LP-quality alignment} (per-sample).\nWithin non-degenerate instances, MBR utility \\cite{eikema2022sampling} correlates positively with F1 (SJ median $\\rho{=}0.524$) and closes 23--41\\% of the oracle gap, but 17.8\\% (SciERC) to 59.1\\% (CoNLL) of instances produce identical F1 across all samples, eliminating headroom entirely (Table~\\ref{tab:degeneracy}).\nDegeneracy is determined by the interplay of task structure, model architecture, and training convergence (Appendix~\\ref{app:epoch_confound}); cross-model evidence (LLaMA 86.4\\% vs.\\ Qwen 59.1\\% on CoNLL; Table~\\ref{tab:cross_selection}) reinforces the pattern.\nLP is severely compressed (median range 0.041 nats; Table~\\ref{tab:logprob_ties}), with pooled within-instance $\\rho(\\text{LP}, \\text{F1}){=}0.248$.\n\n\\paragraph{Non-tied subset and $N$-scaling.}\nWhere compression is mitigated (LP range ${\\geq}0.05$, $n{=}210$), within-instance $\\rho$ rises to 0.39 and LP selection yields $+2.9$~pp ($p{=}0.004$, survives Bonferroni; Table~\\ref{tab:nontied_main}).\nLP scales with $N$ in the low-degeneracy regime ($+0.52$~pp from $N{=}8$ to 16 on Few-NERD, $p{=}0.003$; \\S\\ref{sec:fewnerd}); on SciERC, even $N{=}32$ captures less than 5\\% of headroom (Table~\\ref{tab:n_scaling_selection}).\nAn oracle tiebreaker within VC-equivalent groups recovers $+7.9$~pp, confirming per-sample signal exists but current signals cannot extract it (full analyses in Appendices~\\ref{app:n_scaling}, \\ref{app:verbalized_confidence}, \\ref{app:vc_quartile}).\n\n\\paragraph{LP compression mechanisms.}\nFour non-mutually-exclusive mechanisms contribute: token-level averaging, schema-dominated tokens, vocabulary restriction under constrained decoding, and format-token dilution.\nFree-form decoding rules out constraint-imposed mechanisms for NER (std ratio 0.97; Appendix~\\ref{app:freeform_ablation}) but restores LP selection for RE ($+2.35$~pp, $p{=}0.025$; Appendix~\\ref{app:re_extension}).\nEntity-token LP exhibits $4{\\times}$ higher variance yet performs worse ($-2.0$~pp SciERC, $-3.3$~pp CoNLL): fine-tuned models assign near-deterministic probabilities at the representation level, and compression cannot be broken by disaggregating to entity tokens.\nLP failures show cross-seed stability (Jaccard${=}0.42$; Appendix~\\ref{app:lp_failure_stability}), consistent with a systematic failure mode.\n\n\\paragraph{Regime boundaries.}\nAt the low-resource boundary (WNUT-17), QE signals collapse (VC conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); at the ceiling boundary (CoNLL, degeneracy 59--86\\%), LP degrades selection ($-1.05$~pp).\nIn the moderate regime, two conditions jointly determine effectiveness.\nTemperature manipulation provides the primary evidence ($T{=}1.2$: degeneracy 12.5\\%, $\\rho{=}0.225$; Table~\\ref{tab:t_degeneracy}): it alters output diversity without changing model capacity, isolating the degeneracy lever from alignment.\nEven at degeneracy approaching Few-NERD levels (12.5\\% vs.\\ 13.8\\%), LP does not improve selection because alignment remains weak ($\\rho{=}0.225$ vs.\\ Few-NERD ${\\sim}$0.5).\nLoRA rank${=}8$ (degeneracy 7.2\\%, $\\rho{=}0.24$) corroborates the pattern, though this ablation conflates diversity with capacity (secondary evidence).\nThe cross-dataset gradient (59\\% $\\to$ $-1.05$~pp, 18\\% $\\to$ $+0.61$~pp, 14\\% $\\to$ $+1.36$~pp; $n{=}3$ datasets, exploratory) is consistent with an inverse relationship; per-entity-type analysis within Few-NERD ($\\rho{=}{-}0.881$, $p{=}0.004$, $n{=}8$; entity types share model and tokenizer, effective $\\mathit{df}$ may be lower; Appendix~\\ref{app:per_type_lp}) provides supporting evidence.\n\n\\paragraph{Practical guidelines.}\nPractitioners should first estimate instance degeneracy and LP-quality alignment on a labeled development set.\nThe decision rule is: if degeneracy ${<}$15\\% and within-instance $\\rho(\\text{LP}, \\text{F1}) \\gtrsim 0.3$, use LP selection (Few-NERD: $+1.36$~pp, $p{<}0.001$; gains scale with $N$); otherwise, prefer greedy decoding ($T{=}0$), using structural signals for quality estimation only ($\\rho{=}0.43$--$0.47$ even in the high-degeneracy regime; Table~\\ref{tab:degeneracy}).\nTemperature provides a controllable lever for degeneracy (40.3\\% at $T{=}0.5$ to 12.5\\% at $T{=}1.2$; Table~\\ref{tab:t_degeneracy}) but cannot address alignment; training convergence offers a second lever: on Few-NERD, degeneracy rises from 11\\% to 31\\% between 3 and 5 epochs, halving LP gains (Table~\\ref{tab:epoch_confound}); a SciERC 3-point curve (3, 5, 10 epochs) shows both conditions degrading in tandem, with degeneracy rising from 6.4\\% to 47.8\\% while within-instance alignment collapses ($\\rho$: 0.317 $\\to$ 0.282 $\\to$ 0.120) and LP selection remains below detectable thresholds at all three checkpoints, confirming that degeneracy is convergence-driven rather than a fixed dataset property (Table~\\ref{tab:epoch_scierc}); even at 3 epochs (degeneracy 6.4\\%), SciERC alignment remains insufficient ($\\rho{=}0.317$ vs.\\ Few-NERD ${\\sim}$0.5), reinforcing that low degeneracy alone does not guarantee selection gains.\nStandard calibration methods preserve within-instance argmax and cannot change selection; even multi-feature variants yield no improvement ($p{=}0.31$--$0.83$; Appendix~\\ref{app:calibration_baseline}), confirming the bottleneck is alignment rather than miscalibration.\n\n\\paragraph{Methodological implications.}\nThe decoupling of $\\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; even supervised combination of these five unsupervised signals does not close the oracle gap (\\S\\ref{sec:robustness_main}).\nEffective selection requires content-aware verifiers \\cite{cobbe2021verifiers, venktesh2025trust}; $N{=}8$ captures most QE benefit (Appendix~\\ref{app:n_scaling}).\nStructural signals are robust to domain shift when the training schema subsumes the target (Appendix~\\ref{app:ood}).\n",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  },
  "sourceToolAssistantUUID": "f45815ec-27b2-4992-81a3-e4dac4f223f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-18T05:56:27.420Z_

<details open><summary>🔧 Tool call — Read · `toolu_012p6xTwkVTVYuBVcyzHngPS`</summary>

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
  "parentUuid": "b86e3651-bc36-4c2d-832c-8cc660e8c02b",
  "isSidechain": false,
  "requestId": "req_011Cb9X3ysssQjUBvwvi4pSR",
  "type": "assistant",
  "uuid": "cbb5510d-6599-40a1-99b3-7882c74faac2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMwoe2iSSZTa7wy7mbTZxe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2378,
      "cache_read_input_tokens": 42662,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2378,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 42662,
          "cache_creation_input_tokens": 2378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2378
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-18T05:56:27.433Z_

<details><summary>↩ Tool result · `toolu_012p6xTwkVTVYuBVcyzHngPS`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER across four benchmarks spanning a difficulty gradient.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), supporting selective prediction.
5	For selection, LP achieves $+1.36$~pp on Few-NERD ($p{<}0.001$) when two conditions are jointly met: low instance degeneracy (${<}$15\%) and adequate LP-quality alignment ($\rho \gtrsim 0.3$); gains scale with sample budget ($+0.52$~pp, $N{=}8{\to}16$, $p{=}0.003$).
6	When either condition is violated, LP gains fall below detectable thresholds despite 12\textendash 14~pp oracle headroom: on SciERC (17.8\% degeneracy, $\rho{\approx}0.24$), LP yields $+0.61$~pp (below the ${\approx}$1.5~pp MDE at 80\% power); on CoNLL (59.1\% degeneracy), LP degrades selection ($-1.05$~pp).
7	Two mechanisms explain this gap: instance degeneracy (14\textendash 59\% of instances yield identical F1 scores) eliminates headroom, and weak LP-quality alignment prevents exploiting the remainder.
8	Structural signals do not improve selection regardless of degeneracy, and supervised combination of these five unsupervised signals does not close the oracle gap; whether richer representations (e.g., hidden states, entity embeddings) could change this conclusion remains open.
9	Whether these patterns persist at 70B+ scales remains open.
10	Closing the gap for structural signals likely requires content-aware verifiers \cite{cobbe2021verifiers}; LP provides a practical baseline when both conditions are met, with degeneracy controllable via temperature and training convergence.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbb5510d-6599-40a1-99b3-7882c74faac2",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "821fb229-1288-47ad-8115-e00b673b2a7a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluate five confidence signals for quality estimation and sample selection in LLM-based NER across four benchmarks spanning a difficulty gradient.\nAll signals achieve reliable quality estimation ($\\rho$ up to 0.45, AUROC up to 0.82), supporting selective prediction.\nFor selection, LP achieves $+1.36$~pp on Few-NERD ($p{<}0.001$) when two conditions are jointly met: low instance degeneracy (${<}$15\\%) and adequate LP-quality alignment ($\\rho \\gtrsim 0.3$); gains scale with sample budget ($+0.52$~pp, $N{=}8{\\to}16$, $p{=}0.003$).\nWhen either condition is violated, LP gains fall below detectable thresholds despite 12\\textendash 14~pp oracle headroom: on SciERC (17.8\\% degeneracy, $\\rho{\\approx}0.24$), LP yields $+0.61$~pp (below the ${\\approx}$1.5~pp MDE at 80\\% power); on CoNLL (59.1\\% degeneracy), LP degrades selection ($-1.05$~pp).\nTwo mechanisms explain this gap: instance degeneracy (14\\textendash 59\\% of instances yield identical F1 scores) eliminates headroom, and weak LP-quality alignment prevents exploiting the remainder.\nStructural signals do not improve selection regardless of degeneracy, and supervised combination of these five unsupervised signals does not close the oracle gap; whether richer representations (e.g., hidden states, entity embeddings) could change this conclusion remains open.\nWhether these patterns persist at 70B+ scales remains open.\nClosing the gap for structural signals likely requires content-aware verifiers \\cite{cobbe2021verifiers}; LP provides a practical baseline when both conditions are met, with degeneracy controllable via temperature and training convergence.\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  },
  "sourceToolAssistantUUID": "cbb5510d-6599-40a1-99b3-7882c74faac2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-18T05:56:30.031Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YKXRg5q7MSyKWvwYJpfYJx`</summary>

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
  "parentUuid": "821fb229-1288-47ad-8115-e00b673b2a7a",
  "isSidechain": false,
  "requestId": "req_011Cb9X4AMRCuv5GeysrFaRK",
  "type": "assistant",
  "uuid": "448fe7d2-6926-443a-82a7-8e0d43112514",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcAF4B5Fc86L6mQtEzf4fp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 593,
      "cache_read_input_tokens": 45040,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 45040,
          "cache_creation_input_tokens": 593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 593
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-18T05:56:30.040Z_

<details><summary>↩ Tool result · `toolu_01YKXRg5q7MSyKWvwYJpfYJx`</summary>

```text
1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and the two conditions may shift in opposite directions.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
12	We tested one remedy for LP compression (entity-token-only LP, excluding format/schema tokens) which fails to improve selection despite increasing within-instance variance on SciERC ($4{\times}$); LP${\times}$VC combinations also fail to recover selection (\S\ref{sec:discussion}). Our supervised verifier baseline uses only the five unsupervised signals studied; richer representations (hidden states, entity embeddings) remain unexplored and could potentially close the gap. Calibration-based approaches are also untested.
13	Our selection experiments use 2 training seeds (stability $\sigma{\leq}0.026$); while within-seed statistical power is high ($n{=}32{,}565$ for Few-NERD), training seed stochasticity is not exhaustively quantified.
14	Few-NERD models are trained for 3 epochs (vs.\ 5 for other datasets) due to earlier convergence; epoch confound analyses on both Few-NERD (2-point) and SciERC (3-point, including 10-epoch overfitting) are provided in Appendix~\ref{app:epoch_confound}.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "448fe7d2-6926-443a-82a7-8e0d43112514",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "b8258761-3218-4e88-94bf-f1ec7382dcc8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.\nWe cover 4B\\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and the two conditions may shift in opposite directions.\nWe do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\\ref{app:n_scaling}).\nThe free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\\ref{app:re_extension}.\nQwen3-8B's SciERC checkpoint used empty \\texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\\ref{app:thinking_token}).\nLP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.\nWe tested verbalized confidence \\cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\\ref{app:verbalized_confidence}).\nAd-hoc LP${\\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \\S\\ref{sec:discussion}); whether \\textit{learned} combinations could close the gap remains open.\nThe $\\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\\varepsilon \\in [0, 0.2]$ (Appendix~\\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.\nWe tested one remedy for LP compression (entity-token-only LP, excluding format/schema tokens) which fails to improve selection despite increasing within-instance variance on SciERC ($4{\\times}$); LP${\\times}$VC combinations also fail to recover selection (\\S\\ref{sec:discussion}). Our supervised verifier baseline uses only the five unsupervised signals studied; richer representations (hidden states, entity embeddings) remain unexplored and could potentially close the gap. Calibration-based approaches are also untested.\nOur selection experiments use 2 training seeds (stability $\\sigma{\\leq}0.026$); while within-seed statistical power is high ($n{=}32{,}565$ for Few-NERD), training seed stochasticity is not exhaustively quantified.\nFew-NERD models are trained for 3 epochs (vs.\\ 5 for other datasets) due to earlier convergence; epoch confound analyses on both Few-NERD (2-point) and SciERC (3-point, including 10-epoch overfitting) are provided in Appendix~\\ref{app:epoch_confound}.\n",
      "numLines": 15,
      "startLine": 1,
      "totalLines": 15
    }
  },
  "sourceToolAssistantUUID": "448fe7d2-6926-443a-82a7-8e0d43112514",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-18T05:56:32.766Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VUgs9yUmdUeaQzjZJRxSqa`</summary>

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
  "parentUuid": "b8258761-3218-4e88-94bf-f1ec7382dcc8",
  "isSidechain": false,
  "requestId": "req_011Cb9X4Mh3eCupioeYVgcKF",
  "type": "assistant",
  "uuid": "a4882802-e347-4c62-bb99-636c1d071029",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wi8YQm5CCM9dyVKbdJ2nF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 966,
      "cache_read_input_tokens": 45633,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 966,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 45633,
          "cache_creation_input_tokens": 966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 966
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-18T05:56:33.073Z_

<details><summary>↩ Tool result · reported error · `toolu_01VUgs9yUmdUeaQzjZJRxSqa`</summary>

```text
File content (35137 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4882802-e347-4c62-bb99-636c1d071029",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "bd760bff-7d7a-4a81-bae1-a30ebc22b9b3",
  "toolUseResult": "Error: File content (35137 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "a4882802-e347-4c62-bb99-636c1d071029",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）  ### 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction - **路径**: `projects…",
  "leafUuid": "bd760bff-7d7a-4a81-bae1-a30ebc22b9b3",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured IE paper for EMNLP 2026",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Tool call

_source line 52 · 2026-05-18T05:56:35.760Z_

<details open><summary>🔧 Tool call — Read · `toolu_011x7Ea5e9VGqouLGvV5P6PV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd760bff-7d7a-4a81-bae1-a30ebc22b9b3",
  "isSidechain": false,
  "requestId": "req_011Cb9X4aQXSUyjdfZVVBArc",
  "type": "assistant",
  "uuid": "1dee6fcc-c760-4336-9ba6-2c45fb43bfc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BdCeuTgF5XGfaNbHkPEcqo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 153,
      "cache_read_input_tokens": 46599,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 46599,
          "cache_creation_input_tokens": 153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 153
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-18T05:56:35.766Z_

<details><summary>↩ Tool result · `toolu_011x7Ea5e9VGqouLGvV5P6PV`</summary>

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
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
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
82	The magnitude of $N$-scaling gains is setting-dependent (LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$), though the direction is consistently positive.
83	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\ref{tab:quality_estimation}).
84	FK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.
85	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
86	SJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, structural and binary-agreement signals are the most robust to $N$.
87	At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), a more stable alternative at higher sample sizes.
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
116	All configurations reject the independence null at $p{<}0.001$ ($n{=}529$--$2{,}756$), FK captures genuine inter-sample agreement rather than chance label co-occurrence.
117	Split-half reliability ranges from $r{=}0.395$ (SciERC) to $r{=}0.578$ (CoNLL LLaMA), moderate stability: FK estimates from half the samples correlate positively with those from the other half, though the SciERC value suggests noisier estimation on harder tasks with fewer samples.
118	The higher FK means on CoNLL ($0.720$--$0.927$) vs.\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.
119	
120	\section{Calibration Analysis}\label{app:calibration}
121	
122	\begin{figure*}[t]
123	\centering
124	\includegraphics[width=\textwidth]{fig_reliability}
125	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}
126	\label{fig:reliability}
127	\end{figure*}
128	
129	Reliability diagrams use 10 equal-width bins.
130	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
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
144	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives. This is a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
145	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
146	
147	\paragraph{Capability stratification.}
148	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
149	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
150	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$): longer, more relation-dense sentences provide richer structure for consistency-based estimation.
151	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
152	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
153	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$, all far above the full-set levels.
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
169	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$; the two selection rules are equivalent.
170	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
171	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
172	Evaluation circularity is negligible.
173	
174	\paragraph{SJ normalizer robustness.}
175	Equation~\ref{eq:sj} uses $\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \cup g_j|$.
176	Table~\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\Delta\rho|{<}0.01$ in every case, the choice between max and union normalization does not affect conclusions.
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
200	EM ranks first across all four tested conditional configurations: SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$). This holds despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1dee6fcc-c760-4336-9ba6-2c45fb43bfc8",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "e8b479e0-19a0-43fa-a9fd-6036a162a342",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\nWe exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\\%; SciERC: 22/551, 4.0\\%).\nFor these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\\rho$ depending on signal behavior at the boundary.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as sample standard deviation.}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\quad LP & $T{=}0.7$ & 0.249 & --- \\\\\n\\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.411$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.283 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.474{\\pm}0.009$ & --- \\\\\n\\quad FK &  & $0.467{\\pm}0.009$ & --- \\\\\n\\quad EM &  & $0.473{\\pm}0.010$ & --- \\\\\n\\quad VC &  & $0.470{\\pm}0.006$ & --- \\\\\n\\quad LP &  & $0.311{\\pm}0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\\Delta\\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.\nFK NER $\\rho$ drops by 0.022, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nLP exhibits the largest temperature effect on NER ($\\rho{=}0.249$ at $T{=}0.7$ vs.\\ $0.205$ at $T{=}1.0$, $\\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.\nAcross all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.411{\\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.\nThe magnitude of $N$-scaling gains is setting-dependent (LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$), though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.034$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, structural and binary-agreement signals are the most robust to $N$.\nAt $N{=}16$, SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$), a more stable alternative at higher sample sizes.\n\n\\paragraph{Transfer across model families.}\nLLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, $\\Delta\\rho{=}0.069$; permutation $p{=}0.06$, borderline).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\\rho{=}0.409$ vs.\\ LP 0.239, $\\Delta{=}{+}0.170$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$),\\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.474{\\pm}0.009$ vs.\\ LP $0.311{\\pm}0.003$, $\\Delta{=}{+}0.163$).\n\n\\paragraph{FK independence: instance-level permutation test.}\\label{app:fk_independence}\n\nTo verify that Fleiss' $\\kappa$ reflects genuine within-instance agreement rather than marginal-rate artifacts, we conduct instance-level permutation tests across three configurations.\nFor each instance, we permute sample labels 10{,}000 times to generate a null distribution of FK under independence, then compare the observed FK against this null via a one-sample $t$-test and permutation $p$-value.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}\n\\label{tab:fk_independence}\n\\begin{tabular}{lrcccc}\n\\toprule\nConfig & $n$ & FK mean & 95\\% CI & $t$ & Split-half $r$ \\\\\n\\midrule\nSciERC (Qwen) & 529 & 0.402 & [0.376, 0.428] & 30.8 & 0.395 \\\\\nCoNLL (LLaMA) & 2{,}756 & 0.927 & [0.919, 0.935] & 225.9 & 0.578 \\\\\nCoNLL (Qwen) & 2{,}756 & 0.720 & [0.706, 0.734] & 102.1 & 0.520 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:fk_independence} reports the results.\nAll configurations reject the independence null at $p{<}0.001$ ($n{=}529$--$2{,}756$), FK captures genuine inter-sample agreement rather than chance label co-occurrence.\nSplit-half reliability ranges from $r{=}0.395$ (SciERC) to $r{=}0.578$ (CoNLL LLaMA), moderate stability: FK estimates from half the samples correlate positively with those from the other half, though the SciERC value suggests noisier estimation on harder tasks with fewer samples.\nThe higher FK means on CoNLL ($0.720$--$0.927$) vs.\\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives. This is a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$): longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$, all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$; the two selection rules are equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{SJ normalizer robustness.}\nEquation~\\ref{eq:sj} uses $\\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \\cup g_j|$.\nTable~\\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\\Delta\\rho|{<}0.01$ in every case, the choice between max and union normalization does not affect conclusions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SJ normalizer comparison (Spearman $\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\\max(|g_i|,|g_j|)$; Union: $|g_i \\cup g_j|$.}\n\\label{tab:sj_normalizer}\n\\begin{tabular}{@{}ll ccc@{}}\n\\toprule\nDataset & Model & $\\rho$(max) & $\\rho$(union) & $\\Delta\\rho$ \\\\\n\\midrule\nCoNLL & Qwen3-8B & .436 & .438 & $-$.002 \\\\\nCoNLL & Qwen3-4B & .422 & .421 & $+$.000 \\\\\nCoNLL & LLaMA-8B & .431 & .432 & $-$.000 \\\\\nSciERC & Qwen3-8B & .360 & .365 & $-$.005 \\\\\nSciERC & Qwen3-4B & .422 & .423 & $-$.001 \\\\\nSciERC & LLaMA-8B & .363 & .372 & $-$.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\\Delta\\rho{=}{-}0.005$, $p{=}0.53$; preliminary).\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations: SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$). This holds despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).",
      "numLines": 200,
      "startLine": 1,
      "totalLines": 1354
    }
  },
  "sourceToolAssistantUUID": "1dee6fcc-c760-4336-9ba6-2c45fb43bfc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）  ### 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction - **路径**: `projects…",
  "leafUuid": "e8b479e0-19a0-43fa-a9fd-6036a162a342",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured IE paper for EMNLP 2026",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Assistant

_source line 56 · 2026-05-18T05:56:39.687Z_

Now let me search for reviewer guidelines, run reference verification, and check writing quality in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8b479e0-19a0-43fa-a9fd-6036a162a342",
  "isSidechain": false,
  "requestId": "req_011Cb9X4n4WHn6b6UEfQjY4P",
  "type": "assistant",
  "uuid": "095352c1-b3a7-4a73-9c59-578716e9ef62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVzGHDKkbgbY5CVp3vwQ1y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6145,
      "cache_read_input_tokens": 46752,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6145,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 46752,
          "cache_creation_input_tokens": 6145,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6145
          },
          "type": "message"
        }
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

_source line 57 · 2026-05-18T05:56:39.993Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JZNRBhKJqqQXnr5k1Ei6hD`</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "095352c1-b3a7-4a73-9c59-578716e9ef62",
  "isSidechain": false,
  "requestId": "req_011Cb9X4n4WHn6b6UEfQjY4P",
  "type": "assistant",
  "uuid": "0826e3c3-7549-4bd4-bf3c-704851e84731",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVzGHDKkbgbY5CVp3vwQ1y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6145,
      "cache_read_input_tokens": 46752,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6145,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 46752,
          "cache_creation_input_tokens": 6145,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6145
          },
          "type": "message"
        }
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

_source line 58 · 2026-05-18T05:56:48.504Z_

<details><summary>↩ Tool result · `toolu_01JZNRBhKJqqQXnr5k1Ei6hD`</summary>

```text
Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

I've found comprehensive information about ACL Rolling Review 2026 reviewer guidelines and review form criteria. Here's what I found:

## Reviewer Guidelines

When you accept a reviewing request for an ARR cycle, you'll receive a kick-off email from OpenReview listing important dates. You should block time for checking assignments, working on reviews, and submitting them on time.

To preserve double-blind review, reviewers should not actively try to discover author identity and should search for related work without deliberately trying to find the particular submission.

Each submission receives at least three reviews. The reviewer's main tasks are checking appropriateness of the submission and its assignment, writing a well-justified review, and updating the review based on author-reviewer discussion.

## Review Form Criteria

Reviewers are asked what are the major reasons to publish the paper, which could include novel and useful methodology, insightful empirical results or theoretical analysis, and clear organization of related literature.

Reviewers should identify concerns about correctness, limited impact, lack of clarity, or other reasons why interested readers might gain less from this paper than other papers under consideration.

For excitement rating, reviewers should consider if the paper presents conceptual breakthroughs, challenges common assumptions, impacts some community, or is relevant to their own research.

Reviewers should assess whether there is enough information for readers to reproduce main results or build upon the work.

Reviewers should review the ACL code of ethics and the author's ARR checklist, describe any ethical issues, and recommend whether the paper should receive in-depth ethics review.

The full review form and guidelines are available at aclrollingreview.org.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0826e3c3-7549-4bd4-bf3c-704851e84731",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "648c8b42-48d8-4942-a2ad-f86fef09e30e",
  "toolUseResult": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria",
    "results": [
      {
        "tool_use_id": "srvtoolu_016hPfjof8HH5WcZ5ZESgejk",
        "content": [
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
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
            "title": "Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/incentives2026"
          },
          {
            "title": "aclrollingreview/cfp.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"
          },
          {
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "ACL Rolling Review | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/acl-rolling-review"
          }
        ]
      },
      "I've found comprehensive information about ACL Rolling Review 2026 reviewer guidelines and review form criteria. Here's what I found:\n\n## Reviewer Guidelines\n\nWhen you accept a reviewing request for an ARR cycle, you'll receive a kick-off email from OpenReview listing important dates. You should block time for checking assignments, working on reviews, and submitting them on time.\n\nTo preserve double-blind review, reviewers should not actively try to discover author identity and should search for related work without deliberately trying to find the particular submission.\n\nEach submission receives at least three reviews. The reviewer's main tasks are checking appropriateness of the submission and its assignment, writing a well-justified review, and updating the review based on author-reviewer discussion.\n\n## Review Form Criteria\n\nReviewers are asked what are the major reasons to publish the paper, which could include novel and useful methodology, insightful empirical results or theoretical analysis, and clear organization of related literature.\n\nReviewers should identify concerns about correctness, limited impact, lack of clarity, or other reasons why interested readers might gain less from this paper than other papers under consideration.\n\nFor excitement rating, reviewers should consider if the paper presents conceptual breakthroughs, challenges common assumptions, impacts some community, or is relevant to their own research.\n\nReviewers should assess whether there is enough information for readers to reproduce main results or build upon the work.\n\nReviewers should review the ACL code of ethics and the author's ARR checklist, describe any ethical issues, and recommend whether the paper should receive in-depth ethics review.\n\nThe full review form and guidelines are available at aclrollingreview.org."
    ],
    "durationSeconds": 8.507115934000002
  },
  "sourceToolAssistantUUID": "0826e3c3-7549-4bd4-bf3c-704851e84731",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 59 · 2026-05-18T05:56:48.508Z_

```json
{
  "parentUuid": "648c8b42-48d8-4942-a2ad-f86fef09e30e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "239db165-1f7b-4081-b9dc-0070a3734909",
  "timestamp": "2026-05-18T05:56:48.508Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 60 · 2026-05-18T05:56:53.920Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019b3BiGG2bJSDPFN7oiAVq8`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all dimensions, rating scales, and criteria. I need the exact scoring dimensions (e.g., soundness, excitement, reproducibility), their scales (1-5?), and descriptions of each rating level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "239db165-1f7b-4081-b9dc-0070a3734909",
  "isSidechain": false,
  "requestId": "req_011Cb9X5iUj9dtAUiN2DyoQW",
  "type": "assistant",
  "uuid": "abef910e-4c58-4f21-91e9-19c2c90e0aa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D53pD8Gto1L1CUy6yw3HR8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1035,
      "cache_read_input_tokens": 52897,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1035,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 52897,
          "cache_creation_input_tokens": 1035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1035
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-18T05:57:00.185Z_

<details><summary>↩ Tool result · `toolu_019b3BiGG2bJSDPFN7oiAVq8`</summary>

```text
# ACL Rolling Review Form: Complete Dimensions & Scales

## Primary Scoring Dimensions

**1. Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: Quite sure with unlikely missed details
- 3: Pretty sure but may have missed something
- 2: Willing to defend but fairly likely missed details
- 1: "Not my area, or paper is very hard to understand"

**2. Soundness** (1-5 scale with .5 increments)
- 5: "This study is one of the most thorough I have seen"
- 4: "Strong: This study provides sufficient support for all claims"
- 3: "Acceptable: sufficient support for main claims"
- 2: Some main claims lack support; major technical problems
- 1: "Not yet sufficiently thorough to warrant publication"

**3. Excitement** (1-5 scale with .5 increments)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: "Exciting: I would mention this paper to others"
- 3: Interesting; might attend presentation
- 2: Potentially interesting but doesn't resonate personally
- 1: "Not Exciting: does not resonate with me"

**4. Overall Assessment** (1-5 scale with .5 increments)
- 5: Consider for Award (top 2.5%)
- 4: Conference acceptance
- 3: Findings journal acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

**5. Reproducibility** (1-5 scale)
- 5: "They could easily reproduce the results"
- 4: Mostly reproducible with minor variations
- 3: Reproducible with difficulty; underspecified parameters
- 2: Hard to reproduce; unavailable data
- 1: Unable to reproduce regardless of effort

**6. Datasets** (1-5 scale)
- 5: Enabling research direction changes
- 4: Useful for ongoing work
- 3: Potentially useful
- 2: Documentary value only
- 1: No usable datasets

**7. Software** (1-5 scale)
- 5: Enabling research direction changes
- 4: Useful for researchers/developers
- 3: Potentially useful
- 2: Documentary utility
- 1: No usable software

**8. Author Identity Knowledge** (1-5 scale)
- 5-1: Range from certain identification to complete anonymity
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "abef910e-4c58-4f21-91e9-19c2c90e0aa4",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "e5460568-f4eb-44ae-a75c-d763d233182c",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form: Complete Dimensions & Scales\n\n## Primary Scoring Dimensions\n\n**1. Reviewer Confidence** (1-5 scale)\n- 5: \"Positive that my evaluation is correct. I read the paper very carefully\"\n- 4: Quite sure with unlikely missed details\n- 3: Pretty sure but may have missed something\n- 2: Willing to defend but fairly likely missed details\n- 1: \"Not my area, or paper is very hard to understand\"\n\n**2. Soundness** (1-5 scale with .5 increments)\n- 5: \"This study is one of the most thorough I have seen\"\n- 4: \"Strong: This study provides sufficient support for all claims\"\n- 3: \"Acceptable: sufficient support for main claims\"\n- 2: Some main claims lack support; major technical problems\n- 1: \"Not yet sufficiently thorough to warrant publication\"\n\n**3. Excitement** (1-5 scale with .5 increments)\n- 5: \"Highly Exciting: I would recommend this paper to others\"\n- 4: \"Exciting: I would mention this paper to others\"\n- 3: Interesting; might attend presentation\n- 2: Potentially interesting but doesn't resonate personally\n- 1: \"Not Exciting: does not resonate with me\"\n\n**4. Overall Assessment** (1-5 scale with .5 increments)\n- 5: Consider for Award (top 2.5%)\n- 4: Conference acceptance\n- 3: Findings journal acceptance\n- 2: Resubmit next cycle\n- 1: Do not resubmit\n\n**5. Reproducibility** (1-5 scale)\n- 5: \"They could easily reproduce the results\"\n- 4: Mostly reproducible with minor variations\n- 3: Reproducible with difficulty; underspecified parameters\n- 2: Hard to reproduce; unavailable data\n- 1: Unable to reproduce regardless of effort\n\n**6. Datasets** (1-5 scale)\n- 5: Enabling research direction changes\n- 4: Useful for ongoing work\n- 3: Potentially useful\n- 2: Documentary value only\n- 1: No usable datasets\n\n**7. Software** (1-5 scale)\n- 5: Enabling research direction changes\n- 4: Useful for researchers/developers\n- 3: Potentially useful\n- 2: Documentary utility\n- 1: No usable software\n\n**8. Author Identity Knowledge** (1-5 scale)\n- 5-1: Range from certain identification to complete anonymity",
    "durationMs": 6260,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "abef910e-4c58-4f21-91e9-19c2c90e0aa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-18T05:57:06.429Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01HSvVkkhWuL2warwzzfLxYN`</summary>

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
  "parentUuid": "e5460568-f4eb-44ae-a75c-d763d233182c",
  "isSidechain": false,
  "requestId": "req_011Cb9X6dMBhmGGRQ7agaBXk",
  "type": "assistant",
  "uuid": "cb8d9f81-eca9-4df7-9ef8-d5910db6aa66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPCAer7qNXeF1LQk3i14VM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 53932,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 53932,
          "cache_creation_input_tokens": 752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 752
          },
          "type": "message"
        }
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

_source line 63 · 2026-05-18T05:57:54.793Z_

<details><summary>↩ Tool result · `toolu_01HSvVkkhWuL2warwzzfLxYN`</summary>

```text
&lt;persisted-output>
Output too large (49.6KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/4d69282c-32b0-4839-ba8f-96c846d16f13/tool-results/toolu_01HSvVkkhWuL2warwzzfLxYN.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 60, \"total_citations\": 86, \"unique_cited_keys\": 60, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 53, \"online_not_found\": 3, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"vijayakumar2018diverse\", \"type\": \"inproceedings\", \"title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"authors\": \"Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and S...\", \"year\": \"2018\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"shi2022mbr\", \"type\": \"inproceedings\", \"title\": \"Natural Language to Code Translation with Execution\", \"authors\": \"Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eisenstein2023helping\", \"type\": \"article\", \"title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"authors\": \"Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2312.09244\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb8d9f81-eca9-4df7-9ef8-d5910db6aa66",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "c5ef9e79-17e3-4da4-b216-4b36f45e6693",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 60, \\\"total_citations\\\": 86, \\\"unique_cited_keys\\\": 60, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 53, \\\"online_not_found\\\": 3, \\\"online_mismatch\\\": 4}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"vijayakumar2018diverse\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Diverse Beam Search for Improved Description of Complex Scenes\\\", \\\"authors\\\": \\\"Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and S...\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"shi2022mbr\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Natural Language to Code Translation with Execution\\\", \\\"authors\\\": \\\"Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"eisenstein2023helping\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\\\", \\\"authors\\\": \\\"Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2312.09244\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"authors\\\": \\\"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2407.21787\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"authors\\\": \\\"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICML 2024 Workshop on In-Context Learning\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"authors\\\": \\\"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2110.14168\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"authors\\\": \\\"Culotta, Aron and McCallum, Andrew\\\", \\\"year\\\": \\\"2004\\\", \\\"venue\\\": \\\"Proceedings of the Human Language Technology Conference of the North American Ch...\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"authors\\\": \\\"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)\\\"}, {\\\"key\\\": \\\"ding2021fewnerd\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"authors\\\": \\\"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"authors\\\": \\\"Eikema, Bryan and Aziz, Wilker\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"authors\\\": \\\"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"authors\\\": \\\"Fleiss, Joseph L.\\\", \\\"year\\\": \\\"1971\\\", \\\"venue\\\": \\\"Psychological Bulletin\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2511.12309\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"authors\\\": \\\"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"authors\\\": \\\"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2510.20460\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"authors\\\": \\\"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2207.05221\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"authors\\\": \\\"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems 38 (NeurIPS)\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"authors\\\": \\\"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Proceedings of the 64th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"authors\\\": \\\"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.04104\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"authors\\\": \\\"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the Eleventh International Conference on Learning Representations...\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"authors\\\": \\\"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"authors\\\": \\\"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Twelfth International Conference on Learning Representations ...\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"authors\\\": \\\"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"authors\\\": \\\"Manakul, Potsawee and Liusie, Adian and Gales, Mark\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"yao2026consistency\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\\\", \\\"authors\\\": \\\"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Genomics \\\\\\\\& Informatics\\\"}, {\\\"key\\\": \\\"oh2026latentsc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"authors\\\": \\\"Oh, Jungsuk and Lee, Jay-Yoon\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"authors\\\": \\\"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Twelfth International Conference on Learning Representations ...\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"authors\\\": \\\"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"authors\\\": \\\"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"authors\\\": \\\"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"authors\\\": \\\"Sang, Erik F. Tjong Kim and Meulder, Fien De\\\", \\\"year\\\": \\\"2003\\\", \\\"venue\\\": \\\"Proceedings of the Seventh Conference on Computational Natural Language Learning...\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"authors\\\": \\\"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems 38 (NeurIPS)\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"authors\\\": \\\"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"authors\\\": \\\"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the Eleventh International Conference on Learning Representations...\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"authors\\\": \\\"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL 2025\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"authors\\\": \\\"Wang, Weiqin and Wang, Yile and Huang, Hui\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"authors\\\": \\\"Willard, Brandon T. and Louf, Rémi\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2307.09702\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"authors\\\": \\\"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"authors\\\": \\\"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"authors\\\": \\\"M\\\\\\\\\\\\\\\"uller, Mathias and Sennrich, Rico\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"authors\\\": \\\"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\", \\\"authors\\\": \\\"Venktesh, V and Rathee, Mandeep and Anand, Avishek\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.16665\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"authors\\\": \\\"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 41st International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"ratinov2009design\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Design Challenges and Misconceptions in Named Entity Recognition\\\", \\\"authors\\\": \\\"Ratinov, Lev and Roth, Dan\\\", \\\"year\\\": \\\"2009\\\", \\\"venue\\\": \\\"Proceedings of the Thirteenth Conference on Computational Natural Language Learn...\\\"}, {\\\"key\\\": \\\"bergkirkpatrick2012empirical\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"An Empirical Investigation of Statistical Significance in NLP\\\", \\\"authors\\\": \\\"Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan\\\", \\\"year\\\": \\\"2012\\\", \\\"venue\\\": \\\"Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Languag...\\\"}, {\\\"key\\\": \\\"tian2023calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Hum...\\\", \\\"authors\\\": \\\"Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafail...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"fernandes2022quality\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Quality-Aware Decoding for Neural Machine Translation\\\", \\\"authors\\\": \\\"Fernandes, Patrick and Farinhas, Ant\\\\\\\\'onio and Rei, Ricardo and de Souza, Jos\\\\\\\\'e...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"deguchi2024centroid\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Centroid-Based Efficient Minimum Bayes Risk Decoding\\\", \\\"authors\\\": \\\"Deguchi, Hiroyuki and Sakai, Yusuke and Kamigaito, Hidetaka and Watanabe, Taro a...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2024\\\"}, {\\\"key\\\": \\\"mejer2010confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence in Structured-Prediction Using Confidence-Weighted Models\\\", \\\"authors\\\": \\\"Mejer, Avihai and Crammer, Koby\\\", \\\"year\\\": \\\"2010\\\", \\\"venue\\\": \\\"Proceedings of the 2010 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"schall2025hidden\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\\\", \\\"authors\\\": \\\"Schall, Maximilian and de Melo, Gerard\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of Recent Advances in Natural Language Processing (RANLP)\\\"}, {\\\"key\\\": \\\"yun2025price\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Price of Format: Diversity Collapse in LLMs\\\", \\\"authors\\\": \\\"Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingb...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: EMNLP 2025\\\"}, {\\\"key\\\": \\\"park2024grammar\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Grammar-Aligned Decoding\\\", \\\"authors\\\": \\\"Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadi...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems 37 (NeurIPS)\\\"}, {\\\"key\\\": \\\"gao2023scaling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scaling Laws for Reward Model Overoptimization\\\", \\\"authors\\\": \\\"Gao, Leo and Schulman, John and Hilton, Jacob\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 40th International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"kirk2024understanding\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Understanding the Effects of RLHF on LLM Generalisation and Diversity\\\", \\\"authors\\\": \\\"Kirk, Robert and Mediratta, Ishita and Nalmpantis, Christoforos and Luketina, Je...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Twelfth International Conference on Learning Representations ...\\\"}, {\\\"key\\\": \\\"holtzman2020curious\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"authors\\\": \\\"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the Eighth International Conference on Learning Representations (...\\\"}, {\\\"key\\\": \\\"kuleshov2015calibrated\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Calibrated Structured Prediction\\\", \\\"authors\\\": \\\"Kuleshov, Volodymyr and Liang, Percy\\\", \\\"year\\\": \\\"2015\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems 28 (NeurIPS)\\\"}, {\\\"key\\\": \\\"fomicheva2020unsupervised\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Unsupervised Quality Estimation for Neural Machine Translation\\\", \\\"authors\\\": \\\"Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Fr\\\\\\\\'ed\\\\\\\\'eric an...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"platt1999probabilistic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods\\\", \\\"authors\\\": \\\"Platt, John C.\\\", \\\"year\\\": \\\"1999\\\", \\\"venue\\\": \\\"Advances in Large Margin Classifiers\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"authors\\\": \\\"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Proceedings of the 34th International Conference on Machine Learning\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"yao2026consistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ding2021fewnerd\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"oh2026latentsc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"yao2026consistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"mejer2010confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fomicheva2020unsupervised\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"park2024grammar\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"schall2025hidden\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"yun2025price\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"deguchi2024centroid\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shi2022mbr\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"kuleshov2015calibrated\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gao2023scaling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fernandes2022quality\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eisenstein2023helping\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kirk2024understanding\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"holtzman2020curious\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"vijayakumar2018diverse\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 41, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ding2021fewnerd\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 92, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 41, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 41, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/conclusion.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tian2023calibration\\\", \\\"file\\\": \\\"sections/limitations.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 251, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 251, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ratinov2009design\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 406, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"bergkirkpatrick2012empirical\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 407, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 499, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 752, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 752, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 753, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 753, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 754, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"tian2023calibration\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 1104, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"platt1999probabilistic\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 1268, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 1268, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"vijayakumar2018diverse\\\", \\\"title\\\": \\\"Diverse Beam Search for Improved Description of Complex Scenes\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Diverse Beam Search for Improved Description of Complex Scenes\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"shi2022mbr\\\", \\\"title\\\": \\\"Natural Language to Code Translation with Execution\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Natural Language to Code Translation with Execution\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eisenstein2023helping\\\", \\\"title\\\": \\\"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence estimation for information extraction\\\", \\\"matched_year\\\": \\\"2004\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ding2021fewnerd\\\", \\\"title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"matched_year\\\": \\\"1971\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=feng vs api=austin\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.236, \\\"matched_title\\\": \\\"A new criterion for assessing discriminant validity in variance-based structural equation modeling\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.24 below threshold 0.82\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.246, \\\"matched_title\\\": \\\"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yao2026consistency\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"oh2026latentsc\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=snell vs api=charlie\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2003\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=m\\\\\\\\\\\\\\\"uller vs api=müller\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"title\\\": \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.252, \\\"matched_title\\\": \\\"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ratinov2009design\\\", \\\"title\\\": \\\"Design Challenges and Misconceptions in Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Design challenges and misconceptions in named entity recognition\\\", \\\"matched_year\\\": \\\"2009\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"bergkirkpatrick2012empirical\\\", \\\"title\\\": \\\"An Empirical Investigation of Statistical Significance in NLP\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"An Empirical Investigation of Statistical Significance in NLP\\\", \\\"matched_year\\\": \\\"2012\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tian2023calibration\\\", \\\"title\\\": \\\"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fernandes2022quality\\\", \\\"title\\\": \\\"Quality-Aware Decoding for Neural Machine Translation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Quality-Aware Decoding for Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"deguchi2024centroid\\\", \\\"title\\\": \\\"Centroid-Based Efficient Minimum Bayes Risk Decoding\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Centroid-Based Efficient Minimum Bayes Risk Decoding\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mejer2010confidence\\\", \\\"title\\\": \\\"Confidence in Structured-Prediction Using Confidence-Weighted Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence in Structured-Prediction Using Confidence-Weighted Models\\\", \\\"matched_year\\\": \\\"2010\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"schall2025hidden\\\", \\\"title\\\": \\\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yun2025price\\\", \\\"title\\\": \\\"The Price of Format: Diversity Collapse in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Price of Format: Diversity Collapse in LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"park2024grammar\\\", \\\"title\\\": \\\"Grammar-Aligned Decoding\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Grammar-Aligned Decoding\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=park vs api=berg-kirkpatrick\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gao2023scaling\\\", \\\"title\\\": \\\"Scaling Laws for Reward Model Overoptimization\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scaling Laws for Reward Model Overoptimization\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kirk2024understanding\\\", \\\"title\\\": \\\"Understanding the Effects of RLHF on LLM Generalisation and Diversity\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding the Effects of RLHF on LLM Generalisation and Diversity\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"holtzman2020curious\\\", \\\"title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kuleshov2015calibrated\\\", \\\"title\\\": \\\"Calibrated Structured Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calibrated structured prediction\\\", \\\"matched_year\\\": \\\"2015\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fomicheva2020unsupervised\\\", \\\"title\\\": \\\"Unsupervised Quality Estimation for Neural Machine Translation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Unsupervised Quality Estimation for Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"platt1999probabilistic\\\", \\\"title\\\": \\\"Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Probabilistic Outputs for Support vector Machines and Comparisons to Regularized Likelihood Methods\\\", \\\"matched_year\\\": \\\"1999\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 60, \"total_citations\": 86, \"unique_cited_keys\": 60, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 53, \"online_not_found\": 3, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"vijayakumar2018diverse\", \"type\": \"inproceedings\", \"title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"authors\": \"Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and S...\", \"year\": \"2018\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"shi2022mbr\", \"type\": \"inproceedings\", \"title\": \"Natural Language to Code Translation with Execution\", \"authors\": \"Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eisenstein2023helping\", \"type\": \"article\", \"title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"authors\": \"Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2312.09244\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"ICML 2024 Workshop on In-Context Learning\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"Proceedings of the Human Language Technology Conference of the North American Ch...\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)\"}, {\"key\": \"ding2021fewnerd\", \"type\": \"inproceedings\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"authors\": \"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"eikema2022sampling\", \"type\": \"inproceedings\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"authors\": \"Eikema, Bryan and Aziz, Wilker\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"freitag2022high\", \"type\": \"article\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"authors\": \"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\", \"year\": \"2022\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"fleiss1971agreement\", \"type\": \"article\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"authors\": \"Fleiss, Joseph L.\", \"year\": \"1971\", \"venue\": \"Psychological Bulletin\"}, {\"key\": \"feng2025optimal\", \"type\": \"article\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"authors\": \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.12309\"}, {\"key\": \"geng2024confidence\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"hobelsberger2025systematic\", \"type\": \"article\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"authors\": \"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.20460\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kang2025selfcertainty\", \"type\": \"inproceedings\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"authors\": \"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems 38 (NeurIPS)\"}, {\"key\": \"kim2026reasc\", \"type\": \"inproceedings\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"authors\": \"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\", \"year\": \"2026\", \"venue\": \"Proceedings of the 64th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"li2025llms\", \"type\": \"article\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"authors\": \"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.04104\"}, {\"key\": \"kuhn2023semantic\", \"type\": \"inproceedings\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"authors\": \"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\", \"year\": \"2023\", \"venue\": \"Proceedings of the Eleventh International Conference on Learning Representations...\"}, {\"key\": \"li2023codeie\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lightman2024verify\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Twelfth International Conference on Learning Representations ...\"}, {\"key\": \"luan2018scierc\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"authors\": \"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"manakul2023selfcheckgpt\", \"type\": \"inproceedings\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"authors\": \"Manakul, Potsawee and Liusie, Adian and Gales, Mark\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"yao2026consistency\", \"type\": \"article\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\", \"authors\": \"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\", \"year\": \"2026\", \"venue\": \"Genomics \\\\& Informatics\"}, {\"key\": \"oh2026latentsc\", \"type\": \"inproceedings\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"authors\": \"Oh, Jungsuk and Lee, Jay-Yoon\", \"year\": \"2026\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)\"}, {\"key\": \"sainz2024gollie\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Twelfth International Conference on Learning Representations ...\"}, {\"key\": \"snell2025scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"authors\": \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"taubenfeld2025cisc\", \"type\": \"inproceedings\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"authors\": \"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"thirukovalluru2024atomic\", \"type\": \"inproceedings\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"authors\": \"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"tjongkimsang2003conll\", \"type\": \"inproceedings\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"authors\": \"Sang, Erik F. Tjong Kim and Meulder, Fien De\", \"year\": \"2003\", \"venue\": \"Proceedings of the Seventh Conference on Computational Natural Language Learning...\"}, {\"key\": \"vashurin2025cocoa\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"authors\": \"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems 38 (NeurIPS)\"}, {\"key\": \"wadhwa2023revisiting\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"wang2023selfconsistency\", \"type\": \"inproceedings\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"authors\": \"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\", \"year\": \"2023\", \"venue\": \"Proceedings of the Eleventh International Conference on Learning Representations...\"}, {\"key\": \"wang2025make\", \"type\": \"inproceedings\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"authors\": \"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2025\"}, {\"key\": \"wang2025rankedvoting\", \"type\": \"inproceedings\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"authors\": \"Wang, Weiqin and Wang, Yile and Huang, Hui\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"willard2023guided\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, Rémi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"xia2025survey\", \"type\": \"inproceedings\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"authors\": \"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"zheng2024llamafactory\", \"type\": \"inproceedings\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"authors\": \"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"zhou2024uniner\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"muller2021understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"authors\": \"M\\\\\\\"uller, Mathias and Sennrich, Rico\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"eikema2025structured\", \"type\": \"inproceedings\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"authors\": \"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"venktesh2025trust\", \"type\": \"article\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"authors\": \"Venktesh, V and Rathee, Mandeep and Anand, Avishek\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.16665\"}, {\"key\": \"jinnai2024mbr\", \"type\": \"inproceedings\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"authors\": \"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}, {\"key\": \"ratinov2009design\", \"type\": \"inproceedings\", \"title\": \"Design Challenges and Misconceptions in Named Entity Recognition\", \"authors\": \"Ratinov, Lev and Roth, Dan\", \"year\": \"2009\", \"venue\": \"Proceedings of the Thirteenth Conference on Computational Natural Language Learn...\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"type\": \"inproceedings\", \"title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"authors\": \"Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan\", \"year\": \"2012\", \"venue\": \"Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Languag...\"}, {\"key\": \"tian2023calibration\", \"type\": \"inproceedings\", \"title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Hum...\", \"authors\": \"Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafail...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"fernandes2022quality\", \"type\": \"inproceedings\", \"title\": \"Quality-Aware Decoding for Neural Machine Translation\", \"authors\": \"Fernandes, Patrick and Farinhas, Ant\\\\'onio and Rei, Ricardo and de Souza, Jos\\\\'e...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"deguchi2024centroid\", \"type\": \"inproceedings\", \"title\": \"Centroid-Based Efficient Minimum Bayes Risk Decoding\", \"authors\": \"Deguchi, Hiroyuki and Sakai, Yusuke and Kamigaito, Hidetaka and Watanabe, Taro a...\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2024\"}, {\"key\": \"mejer2010confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence in Structured-Prediction Using Confidence-Weighted Models\", \"authors\": \"Mejer, Avihai and Crammer, Koby\", \"year\": \"2010\", \"venue\": \"Proceedings of the 2010 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"schall2025hidden\", \"type\": \"inproceedings\", \"title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"authors\": \"Schall, Maximilian and de Melo, Gerard\", \"year\": \"2025\", \"venue\": \"Proceedings of Recent Advances in Natural Language Processing (RANLP)\"}, {\"key\": \"yun2025price\", \"type\": \"inproceedings\", \"title\": \"The Price of Format: Diversity Collapse in LLMs\", \"authors\": \"Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingb...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2025\"}, {\"key\": \"park2024grammar\", \"type\": \"inproceedings\", \"title\": \"Grammar-Aligned Decoding\", \"authors\": \"Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadi...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems 37 (NeurIPS)\"}, {\"key\": \"gao2023scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling Laws for Reward Model Overoptimization\", \"authors\": \"Gao, Leo and Schulman, John and Hilton, Jacob\", \"year\": \"2023\", \"venue\": \"Proceedings of the 40th International Conference on Machine Learning (ICML)\"}, {\"key\": \"kirk2024understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Effects of RLHF on LLM Generalisation and Diversity\", \"authors\": \"Kirk, Robert and Mediratta, Ishita and Nalmpantis, Christoforos and Luketina, Je...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Twelfth International Conference on Learning Representations ...\"}, {\"key\": \"holtzman2020curious\", \"type\": \"inproceedings\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"authors\": \"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\", \"year\": \"2020\", \"venue\": \"Proceedings of the Eighth International Conference on Learning Representations (...\"}, {\"key\": \"kuleshov2015calibrated\", \"type\": \"inproceedings\", \"title\": \"Calibrated Structured Prediction\", \"authors\": \"Kuleshov, Volodymyr and Liang, Percy\", \"year\": \"2015\", \"venue\": \"Advances in Neural Information Processing Systems 28 (NeurIPS)\"}, {\"key\": \"fomicheva2020unsupervised\", \"type\": \"article\", \"title\": \"Unsupervised Quality Estimation for Neural Machine Translation\", \"authors\": \"Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Fr\\\\'ed\\\\'eric an...\", \"year\": \"2020\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"platt1999probabilistic\", \"type\": \"inproceedings\", \"title\": \"Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods\", \"authors\": \"Platt, John C.\", \"year\": \"1999\", \"venue\": \"Advances in Large Margin Classifiers\"}, {\"key\": \"guo2017calibration\", \"type\": \"inproceedings\", \"title\": \"On Calibration of Modern Neural Networks\", \"authors\": \"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\", \"year\": \"2017\", \"venue\": \"Proceedings of the 34th International Conference on Machine Learning\"}], \"tex_citations\": [{\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"yao2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"ding2021fewnerd\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"thirukovalluru2024atomic\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"manakul2023selfcheckgpt\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"kim2026reasc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wang2025rankedvoting\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"oh2026latentsc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"feng2025optimal\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"wang2025make\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"li2025llms\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"yao2026consistency\", \"file\": \"sections/related_work.tex\", \"line\": 9, \"command\": \"citet\"}, {\"key\": \"vashurin2025cocoa\", \"file\": \"sections/related_work.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"culotta2004confidence\", \"file\": \"sections/related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"mejer2010confidence\", \"file\": \"sections/related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"fomicheva2020unsupervised\", \"file\": \"sections/related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"zhou2024uniner\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"sainz2024gollie\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"li2023codeie\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"wadhwa2023revisiting\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"park2024grammar\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"schall2025hidden\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"yun2025price\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"geng2024confidence\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"xia2025survey\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"hobelsberger2025systematic\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"kadavath2022language\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"deguchi2024centroid\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"shi2022mbr\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/related_work.tex\", \"line\": 18, \"command\": \"citet\"}, {\"key\": \"kuleshov2015calibrated\", \"file\": \"sections/related_work.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"gao2023scaling\", \"file\": \"sections/related_work.tex\", \"line\": 22, \"command\": \"citet\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"lightman2024verify\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"fernandes2022quality\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"eisenstein2023helping\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"kirk2024understanding\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"holtzman2020curious\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"vijayakumar2018diverse\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/method.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fleiss1971agreement\", \"file\": \"sections/method.tex\", \"line\": 26, \"command\": \"citet\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/method.tex\", \"line\": 41, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/experiments.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"ding2021fewnerd\", \"file\": \"sections/experiments.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/experiments.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"zheng2024llamafactory\", \"file\": \"sections/experiments.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/experiments.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/experiments.tex\", \"line\": 92, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/discussion.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/discussion.tex\", \"line\": 41, \"command\": \"cite\"}, {\"key\": \"venktesh2025trust\", \"file\": \"sections/discussion.tex\", \"line\": 41, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/conclusion.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"tian2023calibration\", \"file\": \"sections/limitations.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/appendix.tex\", \"line\": 251, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/appendix.tex\", \"line\": 251, \"command\": \"cite\"}, {\"key\": \"ratinov2009design\", \"file\": \"sections/appendix.tex\", \"line\": 406, \"command\": \"cite\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"file\": \"sections/appendix.tex\", \"line\": 407, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/appendix.tex\", \"line\": 499, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/appendix.tex\", \"line\": 752, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/appendix.tex\", \"line\": 752, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/appendix.tex\", \"line\": 753, \"command\": \"cite\"}, {\"key\": \"jinnai2024mbr\", \"file\": \"sections/appendix.tex\", \"line\": 753, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/appendix.tex\", \"line\": 754, \"command\": \"citet\"}, {\"key\": \"tian2023calibration\", \"file\": \"sections/appendix.tex\", \"line\": 1104, \"command\": \"citet\"}, {\"key\": \"platt1999probabilistic\", \"file\": \"sections/appendix.tex\", \"line\": 1268, \"command\": \"cite\"}, {\"key\": \"guo2017calibration\", \"file\": \"sections/appendix.tex\", \"line\": 1268, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"vijayakumar2018diverse\", \"title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shi2022mbr\", \"title\": \"Natural Language to Code Translation with Execution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Natural Language to Code Translation with Execution\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eisenstein2023helping\", \"title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"brown2024monkeys\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024usc\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Self-Consistency for Large Language Model Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021verifiers\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culotta2004confidence\", \"title\": \"Confidence Estimation for Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence estimation for information extraction\", \"matched_year\": \"2004\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"derczynski2017wnut\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ding2021fewnerd\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eikema2022sampling\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"freitag2022high\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fleiss1971agreement\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring nominal scale agreement among many raters.\", \"matched_year\": \"1971\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feng2025optimal\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=feng vs api=austin\"], \"note\": \"\"}, {\"key\": \"geng2024confidence\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hobelsberger2025systematic\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.236, \"matched_title\": \"A new criterion for assessing discriminant validity in variance-based structural equation modeling\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.24 below threshold 0.82\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2025selfcertainty\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2026reasc\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025llms\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuhn2023semantic\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023codeie\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lightman2024verify\", \"title\": \"Let's Verify Step by Step\", \"status\": \"not_found\", \"confidence\": 0.246, \"matched_title\": \"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"luan2018scierc\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"manakul2023selfcheckgpt\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yao2026consistency\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oh2026latentsc\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sainz2024gollie\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"snell2025scaling\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=snell vs api=charlie\"], \"note\": \"\"}, {\"key\": \"taubenfeld2025cisc\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence Improves Self-Consistency in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thirukovalluru2024atomic\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tjongkimsang2003conll\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"matched_year\": \"2003\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vashurin2025cocoa\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa2023revisiting\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023selfconsistency\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025make\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025rankedvoting\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023guided\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2025survey\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zheng2024llamafactory\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024uniner\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"muller2021understanding\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"matched_year\": \"2021\", \"mismatch_fields\": [\"first_author: bib=m\\\\\\\"uller vs api=müller\"], \"note\": \"\"}, {\"key\": \"eikema2025structured\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"venktesh2025trust\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"status\": \"not_found\", \"confidence\": 0.252, \"matched_title\": \"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"jinnai2024mbr\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ratinov2009design\", \"title\": \"Design Challenges and Misconceptions in Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Design challenges and misconceptions in named entity recognition\", \"matched_year\": \"2009\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"matched_year\": \"2012\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tian2023calibration\", \"title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fernandes2022quality\", \"title\": \"Quality-Aware Decoding for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Quality-Aware Decoding for Neural Machine Translation\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"deguchi2024centroid\", \"title\": \"Centroid-Based Efficient Minimum Bayes Risk Decoding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Centroid-Based Efficient Minimum Bayes Risk Decoding\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mejer2010confidence\", \"title\": \"Confidence in Structured-Prediction Using Confidence-Weighted Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence in Structured-Prediction Using Confidence-Weighted Models\", \"matched_year\": \"2010\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"schall2025hidden\", \"title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yun2025price\", \"title\": \"The Price of Format: Diversity Collapse in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Price of Format: Diversity Collapse in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"park2024grammar\", \"title\": \"Grammar-Aligned Decoding\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Grammar-Aligned Decoding\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=park vs api=berg-kirkpatrick\"], \"note\": \"\"}, {\"key\": \"gao2023scaling\", \"title\": \"Scaling Laws for Reward Model Overoptimization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scaling Laws for Reward Model Overoptimization\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kirk2024understanding\", \"title\": \"Understanding the Effects of RLHF on LLM Generalisation and Diversity\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Effects of RLHF on LLM Generalisation and Diversity\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"holtzman2020curious\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Case of Neural Text Degeneration\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuleshov2015calibrated\", \"title\": \"Calibrated Structured Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calibrated structured prediction\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fomicheva2020unsupervised\", \"title\": \"Unsupervised Quality Estimation for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Unsupervised Quality Estimation for Neural Machine Translation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"platt1999probabilistic\", \"title\": \"Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Probabilistic Outputs for Support vector Machines and Comparisons to Regularized Likelihood Methods\", \"matched_year\": \"1999\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2017calibration\", \"title\": \"On Calibration of Modern Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Calibration of Modern Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "cb8d9f81-eca9-4df7-9ef8-d5910db6aa66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 64_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）  ### 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction - **路径**: `projects…",
  "leafUuid": "c5ef9e79-17e3-4da4-b216-4b36f45e6693",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured IE paper for EMNLP 2026",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Tool call

_source line 66 · 2026-05-18T05:57:58.480Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Gbvy6U6SkWeCyG1eto9qfq`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/4d69282c-32b0-4839-ba8f-96c846d16f13/tool-results/toolu_01HSvVkkhWuL2warwzzfLxYN.txt",
  "offset": 0,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5ef9e79-17e3-4da4-b216-4b36f45e6693",
  "isSidechain": false,
  "requestId": "req_011Cb9XAbwU7o1UYiBUTnVZg",
  "type": "assistant",
  "uuid": "607ffac6-45d2-41d7-9f08-f455ba4ac098",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gwe99jeYc8mZDpLYmyRrNP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1009,
      "cache_read_input_tokens": 54684,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 54684,
          "cache_creation_input_tokens": 1009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1009
          },
          "type": "message"
        }
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

_source line 67 · 2026-05-18T05:57:58.780Z_

<details><summary>↩ Tool result · `toolu_01Gbvy6U6SkWeCyG1eto9qfq`</summary>

```text
0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 60, \"total_citations\": 86, \"unique_cited_keys\": 60, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 53, \"online_not_found\": 3, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"vijayakumar2018diverse\", \"type\": \"inproceedings\", \"title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"authors\": \"Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and S...\", \"year\": \"2018\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"shi2022mbr\", \"type\": \"inproceedings\", \"title\": \"Natural Language to Code Translation with Execution\", \"authors\": \"Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eisenstein2023helping\", \"type\": \"article\", \"title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"authors\": \"Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2312.09244\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"ICML 2024 Workshop on In-Context Learning\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"Proceedings of the Human Language Technology Conference of the North American Ch...\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)\"}, {\"key\": \"ding2021fewnerd\", \"type\": \"inproceedings\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"authors\": \"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"eikema2022sampling\", \"type\": \"inproceedings\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"authors\": \"Eikema, Bryan and Aziz, Wilker\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"freitag2022high\", \"type\": \"article\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"authors\": \"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\", \"year\": \"2022\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"fleiss1971agreement\", \"type\": \"article\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"authors\": \"Fleiss, Joseph L.\", \"year\": \"1971\", \"venue\": \"Psychological Bulletin\"}, {\"key\": \"feng2025optimal\", \"type\": \"article\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"authors\": \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.12309\"}, {\"key\": \"geng2024confidence\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"hobelsberger2025systematic\", \"type\": \"article\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"authors\": \"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.20460\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kang2025selfcertainty\", \"type\": \"inproceedings\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"authors\": \"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems 38 (NeurIPS)\"}, {\"key\": \"kim2026reasc\", \"type\": \"inproceedings\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"authors\": \"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\", \"year\": \"2026\", \"venue\": \"Proceedings of the 64th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"li2025llms\", \"type\": \"article\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"authors\": \"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.04104\"}, {\"key\": \"kuhn2023semantic\", \"type\": \"inproceedings\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"authors\": \"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\", \"year\": \"2023\", \"venue\": \"Proceedings of the Eleventh International Conference on Learning Representations...\"}, {\"key\": \"li2023codeie\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lightman2024verify\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Twelfth International Conference on Learning Representations ...\"}, {\"key\": \"luan2018scierc\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"authors\": \"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"manakul2023selfcheckgpt\", \"type\": \"inproceedings\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"authors\": \"Manakul, Potsawee and Liusie, Adian and Gales, Mark\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"yao2026consistency\", \"type\": \"article\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\", \"authors\": \"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\", \"year\": \"2026\", \"venue\": \"Genomics \\\\& Informatics\"}, {\"key\": \"oh2026latentsc\", \"type\": \"inproceedings\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"authors\": \"Oh, Jungsuk and Lee, Jay-Yoon\", \"year\": \"2026\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)\"}, {\"key\": \"sainz2024gollie\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Twelfth International Conference on Learning Representations ...\"}, {\"key\": \"snell2025scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"authors\": \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"taubenfeld2025cisc\", \"type\": \"inproceedings\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"authors\": \"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"thirukovalluru2024atomic\", \"type\": \"inproceedings\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"authors\": \"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"tjongkimsang2003conll\", \"type\": \"inproceedings\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"authors\": \"Sang, Erik F. Tjong Kim and Meulder, Fien De\", \"year\": \"2003\", \"venue\": \"Proceedings of the Seventh Conference on Computational Natural Language Learning...\"}, {\"key\": \"vashurin2025cocoa\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"authors\": \"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems 38 (NeurIPS)\"}, {\"key\": \"wadhwa2023revisiting\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"wang2023selfconsistency\", \"type\": \"inproceedings\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"authors\": \"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\", \"year\": \"2023\", \"venue\": \"Proceedings of the Eleventh International Conference on Learning Representations...\"}, {\"key\": \"wang2025make\", \"type\": \"inproceedings\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"authors\": \"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2025\"}, {\"key\": \"wang2025rankedvoting\", \"type\": \"inproceedings\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"authors\": \"Wang, Weiqin and Wang, Yile and Huang, Hui\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"willard2023guided\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, Rémi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"xia2025survey\", \"type\": \"inproceedings\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"authors\": \"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"zheng2024llamafactory\", \"type\": \"inproceedings\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"authors\": \"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"zhou2024uniner\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"muller2021understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"authors\": \"M\\\\\\\"uller, Mathias and Sennrich, Rico\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"eikema2025structured\", \"type\": \"inproceedings\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"authors\": \"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"venktesh2025trust\", \"type\": \"article\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"authors\": \"Venktesh, V and Rathee, Mandeep and Anand, Avishek\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.16665\"}, {\"key\": \"jinnai2024mbr\", \"type\": \"inproceedings\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"authors\": \"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}, {\"key\": \"ratinov2009design\", \"type\": \"inproceedings\", \"title\": \"Design Challenges and Misconceptions in Named Entity Recognition\", \"authors\": \"Ratinov, Lev and Roth, Dan\", \"year\": \"2009\", \"venue\": \"Proceedings of the Thirteenth Conference on Computational Natural Language Learn...\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"type\": \"inproceedings\", \"title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"authors\": \"Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan\", \"year\": \"2012\", \"venue\": \"Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Languag...\"}, {\"key\": \"tian2023calibration\", \"type\": \"inproceedings\", \"title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Hum...\", \"authors\": \"Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafail...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"fernandes2022quality\", \"type\": \"inproceedings\", \"title\": \"Quality-Aware Decoding for Neural Machine Translation\", \"authors\": \"Fernandes, Patrick and Farinhas, Ant\\\\'onio and Rei, Ricardo and de Souza, Jos\\\\'e...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"deguchi2024centroid\", \"type\": \"inproceedings\", \"title\": \"Centroid-Based Efficient Minimum Bayes Risk Decoding\", \"authors\": \"Deguchi, Hiroyuki and Sakai, Yusuke and Kamigaito, Hidetaka and Watanabe, Taro a...\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2024\"}, {\"key\": \"mejer2010confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence in Structured-Prediction Using Confidence-Weighted Models\", \"authors\": \"Mejer, Avihai and Crammer, Koby\", \"year\": \"2010\", \"venue\": \"Proceedings of the 2010 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"schall2025hidden\", \"type\": \"inproceedings\", \"title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"authors\": \"Schall, Maximilian and de Melo, Gerard\", \"year\": \"2025\", \"venue\": \"Proceedings of Recent Advances in Natural Language Processing (RANLP)\"}, {\"key\": \"yun2025price\", \"type\": \"inproceedings\", \"title\": \"The Price of Format: Diversity Collapse in LLMs\", \"authors\": \"Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingb...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2025\"}, {\"key\": \"park2024grammar\", \"type\": \"inproceedings\", \"title\": \"Grammar-Aligned Decoding\", \"authors\": \"Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadi...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems 37 (NeurIPS)\"}, {\"key\": \"gao2023scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling Laws for Reward Model Overoptimization\", \"authors\": \"Gao, Leo and Schulman, John and Hilton, Jacob\", \"year\": \"2023\", \"venue\": \"Proceedings of the 40th International Conference on Machine Learning (ICML)\"}, {\"key\": \"kirk2024understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Effects of RLHF on LLM Generalisation and Diversity\", \"authors\": \"Kirk, Robert and Mediratta, Ishita and Nalmpantis, Christoforos and Luketina, Je...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Twelfth International Conference on Learning Representations ...\"}, {\"key\": \"holtzman2020curious\", \"type\": \"inproceedings\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"authors\": \"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\", \"year\": \"2020\", \"venue\": \"Proceedings of the Eighth International Conference on Learning Representations (...\"}, {\"key\": \"kuleshov2015calibrated\", \"type\": \"inproceedings\", \"title\": \"Calibrated Structured Prediction\", \"authors\": \"Kuleshov, Volodymyr and Liang, Percy\", \"year\": \"2015\", \"venue\": \"Advances in Neural Information Processing Systems 28 (NeurIPS)\"}, {\"key\": \"fomicheva2020unsupervised\", \"type\": \"article\", \"title\": \"Unsupervised Quality Estimation for Neural Machine Translation\", \"authors\": \"Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Fr\\\\'ed\\\\'eric an...\", \"year\": \"2020\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"platt1999probabilistic\", \"type\": \"inproceedings\", \"title\": \"Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods\", \"authors\": \"Platt, John C.\", \"year\": \"1999\", \"venue\": \"Advances in Large Margin Classifiers\"}, {\"key\": \"guo2017calibration\", \"type\": \"inproceedings\", \"title\": \"On Calibration of Modern Neural Networks\", \"authors\": \"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\", \"year\": \"2017\", \"venue\": \"Proceedings of the 34th International Conference on Machine Learning\"}], \"tex_citations\": [{\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"yao2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"ding2021fewnerd\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"thirukovalluru2024atomic\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"manakul2023selfcheckgpt\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"kim2026reasc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wang2025rankedvoting\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"oh2026latentsc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"feng2025optimal\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"wang2025make\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"li2025llms\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"yao2026consistency\", \"file\": \"sections/related_work.tex\", \"line\": 9, \"command\": \"citet\"}, {\"key\": \"vashurin2025cocoa\", \"file\": \"sections/related_work.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"culotta2004confidence\", \"file\": \"sections/related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"mejer2010confidence\", \"file\": \"sections/related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"fomicheva2020unsupervised\", \"file\": \"sections/related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"zhou2024uniner\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"sainz2024gollie\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"li2023codeie\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"wadhwa2023revisiting\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"park2024grammar\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"schall2025hidden\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"yun2025price\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"geng2024confidence\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"xia2025survey\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"hobelsberger2025systematic\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"kadavath2022language\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"deguchi2024centroid\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"shi2022mbr\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/related_work.tex\", \"line\": 18, \"command\": \"citet\"}, {\"key\": \"kuleshov2015calibrated\", \"file\": \"sections/related_work.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"gao2023scaling\", \"file\": \"sections/related_work.tex\", \"line\": 22, \"command\": \"citet\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"lightman2024verify\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"fernandes2022quality\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"eisenstein2023helping\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"kirk2024understanding\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"holtzman2020curious\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"vijayakumar2018diverse\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/method.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fleiss1971agreement\", \"file\": \"sections/method.tex\", \"line\": 26, \"command\": \"citet\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/method.tex\", \"line\": 41, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/experiments.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"ding2021fewnerd\", \"file\": \"sections/experiments.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/experiments.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"zheng2024llamafactory\", \"file\": \"sections/experiments.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/experiments.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/experiments.tex\", \"line\": 92, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/discussion.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/discussion.tex\", \"line\": 41, \"command\": \"cite\"}, {\"key\": \"venktesh2025trust\", \"file\": \"sections/discussion.tex\", \"line\": 41, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/conclusion.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"tian2023calibration\", \"file\": \"sections/limitations.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/appendix.tex\", \"line\": 251, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/appendix.tex\", \"line\": 251, \"command\": \"cite\"}, {\"key\": \"ratinov2009design\", \"file\": \"sections/appendix.tex\", \"line\": 406, \"command\": \"cite\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"file\": \"sections/appendix.tex\", \"line\": 407, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/appendix.tex\", \"line\": 499, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/appendix.tex\", \"line\": 752, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/appendix.tex\", \"line\": 752, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/appendix.tex\", \"line\": 753, \"command\": \"cite\"}, {\"key\": \"jinnai2024mbr\", \"file\": \"sections/appendix.tex\", \"line\": 753, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/appendix.tex\", \"line\": 754, \"command\": \"citet\"}, {\"key\": \"tian2023calibration\", \"file\": \"sections/appendix.tex\", \"line\": 1104, \"command\": \"citet\"}, {\"key\": \"platt1999probabilistic\", \"file\": \"sections/appendix.tex\", \"line\": 1268, \"command\": \"cite\"}, {\"key\": \"guo2017calibration\", \"file\": \"sections/appendix.tex\", \"line\": 1268, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"vijayakumar2018diverse\", \"title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Diverse Beam Search for Improved Description of Complex Scenes\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shi2022mbr\", \"title\": \"Natural Language to Code Translation with Execution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Natural Language to Code Translation with Execution\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eisenstein2023helping\", \"title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"brown2024monkeys\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024usc\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Self-Consistency for Large Language Model Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021verifiers\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culotta2004confidence\", \"title\": \"Confidence Estimation for Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence estimation for information extraction\", \"matched_year\": \"2004\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"derczynski2017wnut\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ding2021fewnerd\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eikema2022sampling\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"freitag2022high\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fleiss1971agreement\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring nominal scale agreement among many raters.\", \"matched_year\": \"1971\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feng2025optimal\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=feng vs api=austin\"], \"note\": \"\"}, {\"key\": \"geng2024confidence\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hobelsberger2025systematic\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.236, \"matched_title\": \"A new criterion for assessing discriminant validity in variance-based structural equation modeling\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.24 below threshold 0.82\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2025selfcertainty\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2026reasc\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025llms\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuhn2023semantic\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023codeie\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lightman2024verify\", \"title\": \"Let's Verify Step by Step\", \"status\": \"not_found\", \"confidence\": 0.246, \"matched_title\": \"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"luan2018scierc\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"manakul2023selfcheckgpt\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yao2026consistency\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oh2026latentsc\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sainz2024gollie\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"snell2025scaling\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=snell vs api=charlie\"], \"note\": \"\"}, {\"key\": \"taubenfeld2025cisc\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence Improves Self-Consistency in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thirukovalluru2024atomic\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tjongkimsang2003conll\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"matched_year\": \"2003\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vashurin2025cocoa\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa2023revisiting\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023selfconsistency\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025make\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025rankedvoting\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023guided\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2025survey\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zheng2024llamafactory\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024uniner\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"muller2021understanding\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"matched_year\": \"2021\", \"mismatch_fields\": [\"first_author: bib=m\\\\\\\"uller vs api=müller\"], \"note\": \"\"}, {\"key\": \"eikema2025structured\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"venktesh2025trust\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"status\": \"not_found\", \"confidence\": 0.252, \"matched_title\": \"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"jinnai2024mbr\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ratinov2009design\", \"title\": \"Design Challenges and Misconceptions in Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Design challenges and misconceptions in named entity recognition\", \"matched_year\": \"2009\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"matched_year\": \"2012\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tian2023calibration\", \"title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fernandes2022quality\", \"title\": \"Quality-Aware Decoding for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Quality-Aware Decoding for Neural Machine Translation\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"deguchi2024centroid\", \"title\": \"Centroid-Based Efficient Minimum Bayes Risk Decoding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Centroid-Based Efficient Minimum Bayes Risk Decoding\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mejer2010confidence\", \"title\": \"Confidence in Structured-Prediction Using Confidence-Weighted Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence in Structured-Prediction Using Confidence-Weighted Models\", \"matched_year\": \"2010\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"schall2025hidden\", \"title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yun2025price\", \"title\": \"The Price of Format: Diversity Collapse in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Price of Format: Diversity Collapse in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"park2024grammar\", \"title\": \"Grammar-Aligned Decoding\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Grammar-Aligned Decoding\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=park vs api=berg-kirkpatrick\"], \"note\": \"\"}, {\"key\": \"gao2023scaling\", \"title\": \"Scaling Laws for Reward Model Overoptimization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scaling Laws for Reward Model Overoptimization\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kirk2024understanding\", \"title\": \"Understanding the Effects of RLHF on LLM Generalisation and Diversity\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Effects of RLHF on LLM Generalisation and Diversity\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"holtzman2020curious\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Case of Neural Text Degeneration\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuleshov2015calibrated\", \"title\": \"Calibrated Structured Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calibrated structured prediction\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fomicheva2020unsupervised\", \"title\": \"Unsupervised Quality Estimation for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Unsupervised Quality Estimation for Neural Machine Translation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"platt1999probabilistic\", \"title\": \"Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Probabilistic Outputs for Support vector Machines and Comparisons to Regularized Likelihood Methods\", \"matched_year\": \"1999\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2017calibration\", \"title\": \"On Calibration of Modern Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Calibration of Modern Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "607ffac6-45d2-41d7-9f08-f455ba4ac098",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "a410112d-eea0-4ca0-bb7c-c52a4523ebc0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/4d69282c-32b0-4839-ba8f-96c846d16f13/tool-results/toolu_01HSvVkkhWuL2warwzzfLxYN.txt",
      "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 60, \\\"total_citations\\\": 86, \\\"unique_cited_keys\\\": 60, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 53, \\\"online_not_found\\\": 3, \\\"online_mismatch\\\": 4}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"vijayakumar2018diverse\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Diverse Beam Search for Improved Description of Complex Scenes\\\", \\\"authors\\\": \\\"Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and S...\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"shi2022mbr\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Natural Language to Code Translation with Execution\\\", \\\"authors\\\": \\\"Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"eisenstein2023helping\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\\\", \\\"authors\\\": \\\"Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2312.09244\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"authors\\\": \\\"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2407.21787\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"authors\\\": \\\"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICML 2024 Workshop on In-Context Learning\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"authors\\\": \\\"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2110.14168\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"authors\\\": \\\"Culotta, Aron and McCallum, Andrew\\\", \\\"year\\\": \\\"2004\\\", \\\"venue\\\": \\\"Proceedings of the Human Language Technology Conference of the North American Ch...\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"authors\\\": \\\"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)\\\"}, {\\\"key\\\": \\\"ding2021fewnerd\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"authors\\\": \\\"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"authors\\\": \\\"Eikema, Bryan and Aziz, Wilker\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"authors\\\": \\\"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"authors\\\": \\\"Fleiss, Joseph L.\\\", \\\"year\\\": \\\"1971\\\", \\\"venue\\\": \\\"Psychological Bulletin\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2511.12309\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"authors\\\": \\\"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"authors\\\": \\\"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2510.20460\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"authors\\\": \\\"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2207.05221\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"authors\\\": \\\"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems 38 (NeurIPS)\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"authors\\\": \\\"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Proceedings of the 64th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"authors\\\": \\\"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.04104\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"authors\\\": \\\"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the Eleventh International Conference on Learning Representations...\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"authors\\\": \\\"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"authors\\\": \\\"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Twelfth International Conference on Learning Representations ...\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"authors\\\": \\\"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"authors\\\": \\\"Manakul, Potsawee and Liusie, Adian and Gales, Mark\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"yao2026consistency\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\\\", \\\"authors\\\": \\\"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Genomics \\\\\\\\& Informatics\\\"}, {\\\"key\\\": \\\"oh2026latentsc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"authors\\\": \\\"Oh, Jungsuk and Lee, Jay-Yoon\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"authors\\\": \\\"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Twelfth International Conference on Learning Representations ...\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"authors\\\": \\\"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"authors\\\": \\\"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"authors\\\": \\\"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"authors\\\": \\\"Sang, Erik F. Tjong Kim and Meulder, Fien De\\\", \\\"year\\\": \\\"2003\\\", \\\"venue\\\": \\\"Proceedings of the Seventh Conference on Computational Natural Language Learning...\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"authors\\\": \\\"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems 38 (NeurIPS)\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"authors\\\": \\\"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"authors\\\": \\\"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the Eleventh International Conference on Learning Representations...\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"authors\\\": \\\"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL 2025\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"authors\\\": \\\"Wang, Weiqin and Wang, Yile and Huang, Hui\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"authors\\\": \\\"Willard, Brandon T. and Louf, Rémi\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2307.09702\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"authors\\\": \\\"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"authors\\\": \\\"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"authors\\\": \\\"M\\\\\\\\\\\\\\\"uller, Mathias and Sennrich, Rico\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"authors\\\": \\\"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\", \\\"authors\\\": \\\"Venktesh, V and Rathee, Mandeep and Anand, Avishek\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.16665\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"authors\\\": \\\"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 41st International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"ratinov2009design\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Design Challenges and Misconceptions in Named Entity Recognition\\\", \\\"authors\\\": \\\"Ratinov, Lev and Roth, Dan\\\", \\\"year\\\": \\\"2009\\\", \\\"venue\\\": \\\"Proceedings of the Thirteenth Conference on Computational Natural Language Learn...\\\"}, {\\\"key\\\": \\\"bergkirkpatrick2012empirical\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"An Empirical Investigation of Statistical Significance in NLP\\\", \\\"authors\\\": \\\"Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan\\\", \\\"year\\\": \\\"2012\\\", \\\"venue\\\": \\\"Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Languag...\\\"}, {\\\"key\\\": \\\"tian2023calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Hum...\\\", \\\"authors\\\": \\\"Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafail...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"fernandes2022quality\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Quality-Aware Decoding for Neural Machine Translation\\\", \\\"authors\\\": \\\"Fernandes, Patrick and Farinhas, Ant\\\\\\\\'onio and Rei, Ricardo and de Souza, Jos\\\\\\\\'e...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"deguchi2024centroid\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Centroid-Based Efficient Minimum Bayes Risk Decoding\\\", \\\"authors\\\": \\\"Deguchi, Hiroyuki and Sakai, Yusuke and Kamigaito, Hidetaka and Watanabe, Taro a...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2024\\\"}, {\\\"key\\\": \\\"mejer2010confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence in Structured-Prediction Using Confidence-Weighted Models\\\", \\\"authors\\\": \\\"Mejer, Avihai and Crammer, Koby\\\", \\\"year\\\": \\\"2010\\\", \\\"venue\\\": \\\"Proceedings of the 2010 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"schall2025hidden\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\\\", \\\"authors\\\": \\\"Schall, Maximilian and de Melo, Gerard\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of Recent Advances in Natural Language Processing (RANLP)\\\"}, {\\\"key\\\": \\\"yun2025price\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Price of Format: Diversity Collapse in LLMs\\\", \\\"authors\\\": \\\"Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingb...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: EMNLP 2025\\\"}, {\\\"key\\\": \\\"park2024grammar\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Grammar-Aligned Decoding\\\", \\\"authors\\\": \\\"Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadi...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems 37 (NeurIPS)\\\"}, {\\\"key\\\": \\\"gao2023scaling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scaling Laws for Reward Model Overoptimization\\\", \\\"authors\\\": \\\"Gao, Leo and Schulman, John and Hilton, Jacob\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 40th International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"kirk2024understanding\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Understanding the Effects of RLHF on LLM Generalisation and Diversity\\\", \\\"authors\\\": \\\"Kirk, Robert and Mediratta, Ishita and Nalmpantis, Christoforos and Luketina, Je...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Twelfth International Conference on Learning Representations ...\\\"}, {\\\"key\\\": \\\"holtzman2020curious\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"authors\\\": \\\"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the Eighth International Conference on Learning Representations (...\\\"}, {\\\"key\\\": \\\"kuleshov2015calibrated\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Calibrated Structured Prediction\\\", \\\"authors\\\": \\\"Kuleshov, Volodymyr and Liang, Percy\\\", \\\"year\\\": \\\"2015\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems 28 (NeurIPS)\\\"}, {\\\"key\\\": \\\"fomicheva2020unsupervised\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Unsupervised Quality Estimation for Neural Machine Translation\\\", \\\"authors\\\": \\\"Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Fr\\\\\\\\'ed\\\\\\\\'eric an...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"platt1999probabilistic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods\\\", \\\"authors\\\": \\\"Platt, John C.\\\", \\\"year\\\": \\\"1999\\\", \\\"venue\\\": \\\"Advances in Large Margin Classifiers\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"authors\\\": \\\"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Proceedings of the 34th International Conference on Machine Learning\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"yao2026consistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ding2021fewnerd\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"oh2026latentsc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"yao2026consistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"mejer2010confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fomicheva2020unsupervised\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"park2024grammar\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"schall2025hidden\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"yun2025price\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"deguchi2024centroid\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shi2022mbr\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"kuleshov2015calibrated\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gao2023scaling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fernandes2022quality\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eisenstein2023helping\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kirk2024understanding\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"holtzman2020curious\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"vijayakumar2018diverse\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 41, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ding2021fewnerd\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 92, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 41, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 41, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/conclusion.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tian2023calibration\\\", \\\"file\\\": \\\"sections/limitations.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 251, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 251, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ratinov2009design\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 406, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"bergkirkpatrick2012empirical\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 407, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 499, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 752, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 752, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 753, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 753, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 754, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"tian2023calibration\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 1104, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"platt1999probabilistic\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 1268, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 1268, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"vijayakumar2018diverse\\\", \\\"title\\\": \\\"Diverse Beam Search for Improved Description of Complex Scenes\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Diverse Beam Search for Improved Description of Complex Scenes\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"shi2022mbr\\\", \\\"title\\\": \\\"Natural Language to Code Translation with Execution\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Natural Language to Code Translation with Execution\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eisenstein2023helping\\\", \\\"title\\\": \\\"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence estimation for information extraction\\\", \\\"matched_year\\\": \\\"2004\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ding2021fewnerd\\\", \\\"title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"matched_year\\\": \\\"1971\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=feng vs api=austin\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.236, \\\"matched_title\\\": \\\"A new criterion for assessing discriminant validity in variance-based structural equation modeling\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.24 below threshold 0.82\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.246, \\\"matched_title\\\": \\\"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yao2026consistency\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"oh2026latentsc\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=snell vs api=charlie\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2003\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=m\\\\\\\\\\\\\\\"uller vs api=müller\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"title\\\": \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.252, \\\"matched_title\\\": \\\"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ratinov2009design\\\", \\\"title\\\": \\\"Design Challenges and Misconceptions in Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Design challenges and misconceptions in named entity recognition\\\", \\\"matched_year\\\": \\\"2009\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"bergkirkpatrick2012empirical\\\", \\\"title\\\": \\\"An Empirical Investigation of Statistical Significance in NLP\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"An Empirical Investigation of Statistical Significance in NLP\\\", \\\"matched_year\\\": \\\"2012\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tian2023calibration\\\", \\\"title\\\": \\\"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fernandes2022quality\\\", \\\"title\\\": \\\"Quality-Aware Decoding for Neural Machine Translation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Quality-Aware Decoding for Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"deguchi2024centroid\\\", \\\"title\\\": \\\"Centroid-Based Efficient Minimum Bayes Risk Decoding\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Centroid-Based Efficient Minimum Bayes Risk Decoding\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mejer2010confidence\\\", \\\"title\\\": \\\"Confidence in Structured-Prediction Using Confidence-Weighted Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence in Structured-Prediction Using Confidence-Weighted Models\\\", \\\"matched_year\\\": \\\"2010\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"schall2025hidden\\\", \\\"title\\\": \\\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yun2025price\\\", \\\"title\\\": \\\"The Price of Format: Diversity Collapse in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Price of Format: Diversity Collapse in LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"park2024grammar\\\", \\\"title\\\": \\\"Grammar-Aligned Decoding\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Grammar-Aligned Decoding\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=park vs api=berg-kirkpatrick\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gao2023scaling\\\", \\\"title\\\": \\\"Scaling Laws for Reward Model Overoptimization\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scaling Laws for Reward Model Overoptimization\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kirk2024understanding\\\", \\\"title\\\": \\\"Understanding the Effects of RLHF on LLM Generalisation and Diversity\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding the Effects of RLHF on LLM Generalisation and Diversity\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"holtzman2020curious\\\", \\\"title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kuleshov2015calibrated\\\", \\\"title\\\": \\\"Calibrated Structured Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calibrated structured prediction\\\", \\\"matched_year\\\": \\\"2015\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fomicheva2020unsupervised\\\", \\\"title\\\": \\\"Unsupervised Quality Estimation for Neural Machine Translation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Unsupervised Quality Estimation for Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"platt1999probabilistic\\\", \\\"title\\\": \\\"Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Probabilistic Outputs for Support vector Machines and Comparisons to Regularized Likelihood Methods\\\", \\\"matched_year\\\": \\\"1999\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
      "numLines": 1,
      "startLine": 0,
      "totalLines": 1
    }
  },
  "sourceToolAssistantUUID": "607ffac6-45d2-41d7-9f08-f455ba4ac098",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
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
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）  ### 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction - **路径**: `projects…",
  "leafUuid": "a410112d-eea0-4ca0-bb7c-c52a4523ebc0",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured IE paper for EMNLP 2026",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Assistant

_source line 70 · 2026-05-18T05:58:07.807Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now check for writing quality issues - dashes, -ing patterns, etc. Let me also check the rest of the appendix for important content, and look for page count.

Reference verification summary:
- 60 bib entries, 86 citations, 60 unique cited keys
- 0 orphan bib, 0 missing bib entries
- 53 verified, 3 not found (hobelsberger2025systematic, lightman2024verify, venktesh2025trust), 4 mismatch (feng2025optimal, snell2025scaling, muller2021understanding, park2024grammar)


- The unfound entries are likely just arXiv preprints not yet indexed in OpenAlex, and the mismatches appear to be minor formatting differences in author names.

Now I'm moving on to check the writing quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a410112d-eea0-4ca0-bb7c-c52a4523ebc0",
  "isSidechain": false,
  "requestId": "req_011Cb9XAtwAe7UtaiFAvzMfA",
  "type": "assistant",
  "uuid": "9a596985-15ad-463e-b6bd-f7f31aadc4d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELYmBMgVfjD8BmzmpMNaLD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17401,
      "cache_read_input_tokens": 55693,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 356,
          "cache_read_input_tokens": 55693,
          "cache_creation_input_tokens": 17401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17401
          },
          "type": "message"
        }
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

_source line 71 · 2026-05-18T05:58:07.812Z_

现在检查写作质量问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a596985-15ad-463e-b6bd-f7f31aadc4d2",
  "isSidechain": false,
  "requestId": "req_011Cb9XAtwAe7UtaiFAvzMfA",
  "type": "assistant",
  "uuid": "c3afb689-267e-4970-b19a-8ef9b92eb21a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELYmBMgVfjD8BmzmpMNaLD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17401,
      "cache_read_input_tokens": 55693,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 356,
          "cache_read_input_tokens": 55693,
          "cache_creation_input_tokens": 17401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17401
          },
          "type": "message"
        }
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

_source line 72 · 2026-05-18T05:58:08.928Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01RKSX4AtvEcLXju6gVNPbZC`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3afb689-267e-4970-b19a-8ef9b92eb21a",
  "isSidechain": false,
  "requestId": "req_011Cb9XAtwAe7UtaiFAvzMfA",
  "type": "assistant",
  "uuid": "0fe5196a-072b-4f9b-9b3a-94b01e23c144",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELYmBMgVfjD8BmzmpMNaLD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17401,
      "cache_read_input_tokens": 55693,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 356,
          "cache_read_input_tokens": 55693,
          "cache_creation_input_tokens": 17401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17401
          },
          "type": "message"
        }
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

_source line 73 · 2026-05-18T05:58:08.941Z_

<details><summary>↩ Tool result · `toolu_01RKSX4AtvEcLXju6gVNPbZC`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fe5196a-072b-4f9b-9b3a-94b01e23c144",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "27b3d296-5e20-49d9-a92d-df6b611cedf9",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "0fe5196a-072b-4f9b-9b3a-94b01e23c144",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-18T05:58:12.228Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LpKh8iLH3MHU1LEFWcrWUC`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27b3d296-5e20-49d9-a92d-df6b611cedf9",
  "isSidechain": false,
  "requestId": "req_011Cb9XBeak4honL6vb7R9Ve",
  "type": "assistant",
  "uuid": "ecc27e8f-87bb-4132-8314-0700349e7a74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCEzu5s3ZzEWaY6ScynLEz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 371,
      "cache_read_input_tokens": 73094,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 371,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 73094,
          "cache_creation_input_tokens": 371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 371
          },
          "type": "message"
        }
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

_source line 75 · 2026-05-18T05:58:12.239Z_

<details><summary>↩ Tool result · `toolu_01LpKh8iLH3MHU1LEFWcrWUC`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecc27e8f-87bb-4132-8314-0700349e7a74",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "f424dd76-ef06-405e-892f-fac7299be927",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "ecc27e8f-87bb-4132-8314-0700349e7a74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-18T05:58:15.476Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01U6S2ZCSzZD8cr6KRJFdo4w`</summary>

```json
{
  "pattern": "\\\\textendash",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f424dd76-ef06-405e-892f-fac7299be927",
  "isSidechain": false,
  "requestId": "req_011Cb9XBtcbfzxk66dwMwMyR",
  "type": "assistant",
  "uuid": "3c8eec00-30b1-4b24-9f3b-8c6f4e0d0df8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Rq3CcfWuPVxBLEo4bkB73",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 155,
      "cache_read_input_tokens": 73465,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 73465,
          "cache_creation_input_tokens": 155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 155
          },
          "type": "message"
        }
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

_source line 77 · 2026-05-18T05:58:15.495Z_

<details><summary>↩ Tool result · `toolu_01U6S2ZCSzZD8cr6KRJFdo4w`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex:6:When either condition is violated, LP gains fall below detectable thresholds despite 12\textendash 14~pp oracle headroom: on SciERC (17.8\% degeneracy, $\rho{\approx}0.24$), LP yields $+0.61$~pp (below the ${\approx}$1.5~pp MDE at 80\% power); on CoNLL (59.1\% degeneracy), LP degrades selection ($-1.05$~pp).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex:7:Two mechanisms explain this gap: instance degeneracy (14\textendash 59\% of instances yield identical F1 scores) eliminates headroom, and weak LP-quality alignment prevents exploiting the remainder.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex:2:We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and the two conditions may shift in opposite directions.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:3:We evaluate five confidence signals (four instance-level, one per-sample log-probability [LP]) for quality estimation and sample selection on four NER benchmarks using 4B\textendash 8B models.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:7:Two mechanisms explain this gap: \textit{instance degeneracy} (14\textendash 59\% of instances yield identical F1 scores across all samples) eliminates headroom; \textit{weak LP-quality alignment} prevents exploiting the remainder.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:15:Two mechanisms explain this gap: (a)~\textit{instance degeneracy} (14\textendash 59\% of instances yield identical F1 scores across all $N$ samples, eliminating headroom); and (b)~\textit{weak LP-quality alignment} (within-instance $\rho(\text{LP}, \text{F1})$ too low to exploit the remaining headroom; \S\ref{sec:discussion}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:25:We vary candidate pool size ($N{\in}\{2,\ldots,32\}$), signal sophistication, and model capacity within the 4B\textendash 8B range; behavior at 70B+ scales remains an open question.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:34:    Instance degeneracy (14\textendash 59\% of instances yield identical F1 scores across all samples) eliminates headroom for consensus-based selection; weak LP-quality alignment (within-instance $\rho{\approx}0.24$ on SciERC) prevents exploiting the remaining headroom.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c8eec00-30b1-4b24-9f3b-8c6f4e0d0df8",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "c10ddd52-eb96-473b-81c3-1acf98f4cdd0",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex:6:When either condition is violated, LP gains fall below detectable thresholds despite 12\\textendash 14~pp oracle headroom: on SciERC (17.8\\% degeneracy, $\\rho{\\approx}0.24$), LP yields $+0.61$~pp (below the ${\\approx}$1.5~pp MDE at 80\\% power); on CoNLL (59.1\\% degeneracy), LP degrades selection ($-1.05$~pp).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex:7:Two mechanisms explain this gap: instance degeneracy (14\\textendash 59\\% of instances yield identical F1 scores) eliminates headroom, and weak LP-quality alignment prevents exploiting the remainder.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex:2:We cover 4B\\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and the two conditions may shift in opposite directions.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:3:We evaluate five confidence signals (four instance-level, one per-sample log-probability [LP]) for quality estimation and sample selection on four NER benchmarks using 4B\\textendash 8B models.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:7:Two mechanisms explain this gap: \\textit{instance degeneracy} (14\\textendash 59\\% of instances yield identical F1 scores across all samples) eliminates headroom; \\textit{weak LP-quality alignment} prevents exploiting the remainder.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:15:Two mechanisms explain this gap: (a)~\\textit{instance degeneracy} (14\\textendash 59\\% of instances yield identical F1 scores across all $N$ samples, eliminating headroom); and (b)~\\textit{weak LP-quality alignment} (within-instance $\\rho(\\text{LP}, \\text{F1})$ too low to exploit the remaining headroom; \\S\\ref{sec:discussion}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:25:We vary candidate pool size ($N{\\in}\\{2,\\ldots,32\\}$), signal sophistication, and model capacity within the 4B\\textendash 8B range; behavior at 70B+ scales remains an open question.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:34:    Instance degeneracy (14\\textendash 59\\% of instances yield identical F1 scores across all samples) eliminates headroom for consensus-based selection; weak LP-quality alignment (within-instance $\\rho{\\approx}0.24$ on SciERC) prevents exploiting the remaining headroom.",
    "numLines": 8
  },
  "sourceToolAssistantUUID": "3c8eec00-30b1-4b24-9f3b-8c6f4e0d0df8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-18T05:58:18.769Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WxBAceqPHM22Pr9R5vK19q`</summary>

```json
{
  "pattern": "ing,|ing\\.|ing;|ing —|ing –",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c10ddd52-eb96-473b-81c3-1acf98f4cdd0",
  "isSidechain": false,
  "requestId": "req_011Cb9XC8cxpANGTE5qmkNaW",
  "type": "assistant",
  "uuid": "9b17ecd7-45b6-494d-9cce-0b68925834e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015zUZtGqrnMXNeiQQKq3DM4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1061,
      "cache_read_input_tokens": 73620,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1061,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 73620,
          "cache_creation_input_tokens": 1061,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1061
          },
          "type": "message"
        }
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

_source line 79 · 2026-05-18T05:58:18.794Z_

<details><summary>↩ Tool result · `toolu_01WxBAceqPHM22Pr9R5vK19q`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:3:\paragraph{Self-consistency and test-time scaling.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:4:Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:5:Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement; \citet{feng2025optimal} and \citet{wang2025make} adapt to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:15:\paragraph{Uncertainty estimation and MBR decoding.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:17:Our selection strategies instantiate MBR decoding \cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \cite{freitag2022high} and code generation where execution-based MBR improves selection \cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\rho{=}0.52$; \S\ref{sec:discussion}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:23:Trained verifiers \cite{cobbe2021verifiers, lightman2024verify, fernandes2022quality} learn per-sample scoring; reward model ensembles mitigate but do not eliminate reward hacking \cite{eisenstein2023helping}. Our LoRA-rank ablation (degeneracy 7.2\%, selection still shows no improvement at $\rho{\approx}0.24$) suggests that, within the five unsupervised signals studied, increasing output diversity alone is insufficient.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:14:\paragraph{Models and sampling.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:117:Under standard early stopping, Few-NERD degeneracy is 13.8\% (training convergence modulates this rate, Appendix~\ref{app:epoch_confound}), and LP achieves $+1.36$~pp (95\% CI $[+1.18, +1.53]$, $p{<}0.001$), while all structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:14:\paragraph{Non-tied subset and $N$-scaling.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:20:Four non-mutually-exclusive mechanisms contribute: token-level averaging, schema-dominated tokens, vocabulary restriction under constrained decoding, and format-token dilution.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex:32:Unlike structural signals, FK relies on exact string matching.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:9:Degeneracy is controllable via temperature and training convergence; closing the gap for structural signals likely requires learned per-sample scoring.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:80:\paragraph{Sample size scaling.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:92:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:157:Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:162:\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:170:Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:250:\paragraph{Diminishing returns of $N$-scaling.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:259:While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:352:Table~\ref{tab:degeneracy} quantifies instance degeneracy across configurations. ``Constant F1'' denotes instances where all $N$ samples receive identical instance-level F1; ``Constant utility'' denotes instances where MBR (SJ) utility is identical across candidates, preventing ranking.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:371:\paragraph{TOST equivalence testing.}\label{app:tost}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:418:The sole positive finding, the non-tied LP subset ($+2.9$~pp, $p{=}0.004$; \S\ref{sec:discussion}), survives Bonferroni correction over 5 signal comparisons ($p_{\mathrm{adj}}{=}0.020 < 0.05$), as noted in the main text footnote.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:425:On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM. This reversal from the NER ranking reflects RE's higher sensitivity to per-sample scoring.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:498:\paragraph{Constrained decoding.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:513:All $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:523:Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:558:A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:675:The signal ranking differs from NER: VC leads ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM, a reversal reflecting RE's higher sensitivity to per-sample scoring.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:686:\paragraph{Free-form decoding.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:751:\paragraph{Connection to MBR decoding.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:752:Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:763:Despite this reshuffling, aggregate NER selection gains remain negligible. Score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:852:Extending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\pm}0.007$ across seeds, higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\% tied fraction under constrained decoding.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:859:We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1033:Oracle headroom increases monotonically with temperature ($+7.8$~pp at $T{=}0.5$ to $+13.3$~pp at $T{=}1.0$), plateauing at $T{=}1.2$ ($+13.0$~pp); the plateau suggests $T{=}1.0$ already approaches the diversity ceiling for constrained structured decoding.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1133:\paragraph{QE--selection decoupling.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1170:After gold-filtering (removing instances with no gold entities), the evaluation set contains $n{=}32{,}565$ instances across 8 coarse entity types; 11.9\% receive zero F1 under greedy decoding.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1304:This finding refines the narrative: degeneracy is not a fixed property of datasets but is modulated by the degree of training convergence. Over-trained models compress their output distributions, collapsing diversity even on datasets that support it under well-regularized training.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1309:\caption{Training convergence confound on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$). ``Degen.'': constant-F1 instance degeneracy (gold-filtered). ``Valid'': fraction of instances with non-degenerate outputs. ``$\rho$ mean/med'': within-instance LP-quality correlation. The 3-epoch model corresponds to standard early stopping; the 5-epoch model is a controlled ablation.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:3:Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b17ecd7-45b6-494d-9cce-0b68925834e8",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "c1bd6574-239c-4827-abe7-a5853f021911",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:3:\\paragraph{Self-consistency and test-time scaling.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:4:Self-consistency \\cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \\cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:5:Test-time scaling studies \\cite{snell2025scaling, brown2024monkeys} and reward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement; \\citet{feng2025optimal} and \\citet{wang2025make} adapt to difficulty-aware settings; \\citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:15:\\paragraph{Uncertainty estimation and MBR decoding.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:17:Our selection strategies instantiate MBR decoding \\cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \\cite{freitag2022high} and code generation where execution-based MBR improves selection \\cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\\rho{=}0.52$; \\S\\ref{sec:discussion}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:23:Trained verifiers \\cite{cobbe2021verifiers, lightman2024verify, fernandes2022quality} learn per-sample scoring; reward model ensembles mitigate but do not eliminate reward hacking \\cite{eisenstein2023helping}. Our LoRA-rank ablation (degeneracy 7.2\\%, selection still shows no improvement at $\\rho{\\approx}0.24$) suggests that, within the five unsupervised signals studied, increasing output diversity alone is insufficient.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:14:\\paragraph{Models and sampling.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:117:Under standard early stopping, Few-NERD degeneracy is 13.8\\% (training convergence modulates this rate, Appendix~\\ref{app:epoch_confound}), and LP achieves $+1.36$~pp (95\\% CI $[+1.18, +1.53]$, $p{<}0.001$), while all structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:14:\\paragraph{Non-tied subset and $N$-scaling.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:20:Four non-mutually-exclusive mechanisms contribute: token-level averaging, schema-dominated tokens, vocabulary restriction under constrained decoding, and format-token dilution.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex:32:Unlike structural signals, FK relies on exact string matching.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:9:Degeneracy is controllable via temperature and training convergence; closing the gap for structural signals likely requires learned per-sample scoring.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:80:\\paragraph{Sample size scaling.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:92:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:157:Figure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:162:\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:170:Standard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:250:\\paragraph{Diminishing returns of $N$-scaling.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:259:While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:352:Table~\\ref{tab:degeneracy} quantifies instance degeneracy across configurations. ``Constant F1'' denotes instances where all $N$ samples receive identical instance-level F1; ``Constant utility'' denotes instances where MBR (SJ) utility is identical across candidates, preventing ranking.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:371:\\paragraph{TOST equivalence testing.}\\label{app:tost}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:418:The sole positive finding, the non-tied LP subset ($+2.9$~pp, $p{=}0.004$; \\S\\ref{sec:discussion}), survives Bonferroni correction over 5 signal comparisons ($p_{\\mathrm{adj}}{=}0.020 < 0.05$), as noted in the main text footnote.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:425:On RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM. This reversal from the NER ranking reflects RE's higher sensitivity to per-sample scoring.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:498:\\paragraph{Constrained decoding.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:513:All $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:523:Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}, Figure~\\ref{fig:lp_range_cdf}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:558:A free-form NER decoding ablation (Appendix~\\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:675:The signal ranking differs from NER: VC leads ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM, a reversal reflecting RE's higher sensitivity to per-sample scoring.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:686:\\paragraph{Free-form decoding.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:751:\\paragraph{Connection to MBR decoding.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:752:Our selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:763:Despite this reshuffling, aggregate NER selection gains remain negligible. Score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:852:Extending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\\pm}0.007$ across seeds, higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\\% tied fraction under constrained decoding.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:859:We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1033:Oracle headroom increases monotonically with temperature ($+7.8$~pp at $T{=}0.5$ to $+13.3$~pp at $T{=}1.0$), plateauing at $T{=}1.2$ ($+13.0$~pp); the plateau suggests $T{=}1.0$ already approaches the diversity ceiling for constrained structured decoding.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1133:\\paragraph{QE--selection decoupling.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1170:After gold-filtering (removing instances with no gold entities), the evaluation set contains $n{=}32{,}565$ instances across 8 coarse entity types; 11.9\\% receive zero F1 under greedy decoding.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1304:This finding refines the narrative: degeneracy is not a fixed property of datasets but is modulated by the degree of training convergence. Over-trained models compress their output distributions, collapsing diversity even on datasets that support it under well-regularized training.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1309:\\caption{Training convergence confound on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$). ``Degen.'': constant-F1 instance degeneracy (gold-filtered). ``Valid'': fraction of instances with non-degenerate outputs. ``$\\rho$ mean/med'': within-instance LP-quality correlation. The 3-epoch model corresponds to standard early stopping; the 5-epoch model is a controlled ablation.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:3:Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \\citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \\cite{snell2025scaling, brown2024monkeys}.",
    "numLines": 40
  },
  "sourceToolAssistantUUID": "9b17ecd7-45b6-494d-9cce-0b68925834e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
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
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）  ### 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction - **路径**: `projects…",
  "leafUuid": "c1bd6574-239c-4827-abe7-a5853f021911",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Runtime record

_source line 81_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured IE paper for EMNLP 2026",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Tool call

_source line 82 · 2026-05-18T05:58:22.879Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01DvstyYy1jVWkGt6Gp3F59q`</summary>

```json
{
  "pattern": "delve|leverage|utilize|facilitate|myriad|plethora",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1bd6574-239c-4827-abe7-a5853f021911",
  "isSidechain": false,
  "requestId": "req_011Cb9XCNdaUrGwjqV2CZgK2",
  "type": "assistant",
  "uuid": "3b2f0d6d-bbf7-44b4-8a77-7b3e30ffdff2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Spvund57pdBFL3iMbWZcye",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4052,
      "cache_read_input_tokens": 74681,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 74681,
          "cache_creation_input_tokens": 4052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4052
          },
          "type": "message"
        }
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

_source line 83 · 2026-05-18T05:58:22.894Z_

<details><summary>↩ Tool result · `toolu_01DvstyYy1jVWkGt6Gp3F59q`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b2f0d6d-bbf7-44b4-8a77-7b3e30ffdff2",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "e2c9e96a-933b-47ad-ac2c-b18513add685",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "3b2f0d6d-bbf7-44b4-8a77-7b3e30ffdff2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-18T05:58:27.136Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LTeecdgQqYFt8ebaxcSJES`</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally|It is worth noting|Notably,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2c9e96a-933b-47ad-ac2c-b18513add685",
  "isSidechain": false,
  "requestId": "req_011Cb9XCgkFJtYMcAxzfGcTn",
  "type": "assistant",
  "uuid": "67d6c6af-a686-48f0-8067-93bb5b0d10fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EUhCQbLa3Lt6tHST6SCZeq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 188,
      "cache_read_input_tokens": 78733,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 188,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 78733,
          "cache_creation_input_tokens": 188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 188
          },
          "type": "message"
        }
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

_source line 85 · 2026-05-18T05:58:27.151Z_

<details><summary>↩ Tool result · `toolu_01LTeecdgQqYFt8ebaxcSJES`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67d6c6af-a686-48f0-8067-93bb5b0d10fa",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "1577d196-9e57-41de-8557-bcc5cca10ee2",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "67d6c6af-a686-48f0-8067-93bb5b0d10fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 86 · 2026-05-18T05:58:27.153Z_

```json
{
  "parentUuid": "1577d196-9e57-41de-8557-bcc5cca10ee2",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2c47d9f2-1a84-4856-9c3e-7208005d1dc5",
  "timestamp": "2026-05-18T05:58:27.153Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 87 · 2026-05-18T05:58:30.821Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01X6Wuyn9QrHoSz7quqo76K1`</summary>

```json
{
  "pattern": "\\\\textendash",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c47d9f2-1a84-4856-9c3e-7208005d1dc5",
  "isSidechain": false,
  "requestId": "req_011Cb9XCzByzSmrfUmbnPnDE",
  "type": "assistant",
  "uuid": "c55c1bb8-4d3d-4cfe-bdd9-b7fd9e265e24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TUDA3PmKw7JKkWE3wyMjW3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 78921,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 78921,
          "cache_creation_input_tokens": 271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 271
          },
          "type": "message"
        }
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

_source line 88 · 2026-05-18T05:58:30.836Z_

<details><summary>↩ Tool result · `toolu_01X6Wuyn9QrHoSz7quqo76K1`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c55c1bb8-4d3d-4cfe-bdd9-b7fd9e265e24",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "f9108291-3fa7-40b4-bfde-ce41b55d959f",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "c55c1bb8-4d3d-4cfe-bdd9-b7fd9e265e24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 89 · 2026-05-18T05:58:34.342Z_

现在检查编译后的 PDF 页数以及查看 appendix 更多内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9108291-3fa7-40b4-bfde-ce41b55d959f",
  "isSidechain": false,
  "requestId": "req_011Cb9XDGTmmLrHvTcG3wUXY",
  "type": "assistant",
  "uuid": "a6905739-4edc-412c-ac96-ba38f6cd8dc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01STj5KE5AvAF5eQpHddsyBV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 163,
      "cache_read_input_tokens": 79192,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 79192,
          "cache_creation_input_tokens": 163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 163
          },
          "type": "message"
        }
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

_source line 90 · 2026-05-18T05:58:34.670Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LBoLWkoapDBLVHG82ve5fp`</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/docs/paper/**/*.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6905739-4edc-412c-ac96-ba38f6cd8dc0",
  "isSidechain": false,
  "requestId": "req_011Cb9XDGTmmLrHvTcG3wUXY",
  "type": "assistant",
  "uuid": "f098f3d5-a9be-40f9-af21-e71e4c80d9d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01STj5KE5AvAF5eQpHddsyBV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 163,
      "cache_read_input_tokens": 79192,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 79192,
          "cache_creation_input_tokens": 163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 163
          },
          "type": "message"
        }
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

_source line 91 · 2026-05-18T05:58:34.678Z_

<details><summary>↩ Tool result · `toolu_01LBoLWkoapDBLVHG82ve5fp`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f098f3d5-a9be-40f9-af21-e71e4c80d9d9",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "0e0755f7-8bd1-4d27-96ec-c64486186888",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 6,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "f098f3d5-a9be-40f9-af21-e71e4c80d9d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-18T05:58:37.553Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XDuBMMR7ehcSbAD3wzDaXU`</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/**/*.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e0755f7-8bd1-4d27-96ec-c64486186888",
  "isSidechain": false,
  "requestId": "req_011Cb9XDYgqpFmZqvmqrsheU",
  "type": "assistant",
  "uuid": "c769a0cf-6296-45b7-b858-2d09ee019424",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AqsQhbMdKRtxZvJ48YzrcJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 109,
      "cache_read_input_tokens": 79355,
      "output_tokens": 63,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 109,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 63,
          "cache_read_input_tokens": 79355,
          "cache_creation_input_tokens": 109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 109
          },
          "type": "message"
        }
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

_source line 93 · 2026-05-18T05:58:37.581Z_

<details><summary>↩ Tool result · `toolu_01XDuBMMR7ehcSbAD3wzDaXU`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c769a0cf-6296-45b7-b858-2d09ee019424",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "93a3298d-a5d3-4306-a9c0-f4f78328ff17",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 10,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "c769a0cf-6296-45b7-b858-2d09ee019424",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-18T05:58:42.204Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011ipyUWJrhXE8L6yxQ1dkgN`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && wc -l sections/*.tex main.tex",
  "description": "Count lines in all tex files to estimate page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93a3298d-a5d3-4306-a9c0-f4f78328ff17",
  "isSidechain": false,
  "requestId": "req_011Cb9XDksa3fBTTwM8vBMHr",
  "type": "assistant",
  "uuid": "3f17a7b2-4e28-45cd-9477-81678ce810cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Yn87qMSnW2qt6mLCJqiU6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 78,
      "cache_read_input_tokens": 79464,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 78,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 79464,
          "cache_creation_input_tokens": 78,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 78
          },
          "type": "message"
        }
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

_source line 95 · 2026-05-18T05:58:42.459Z_

<details><summary>↩ Tool result · `toolu_011ipyUWJrhXE8L6yxQ1dkgN`</summary>

```text
    10 sections/abstract.tex
  1353 sections/appendix.tex
    10 sections/conclusion.tex
    42 sections/discussion.tex
   175 sections/experiments.tex
    41 sections/introduction.tex
    14 sections/limitations.tex
    59 sections/method.tex
    24 sections/related_work.tex
    51 main.tex
  1779 total
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f17a7b2-4e28-45cd-9477-81678ce810cb",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "39eaa2ff-16fb-40cc-80f0-9e03e56f0dbb",
  "toolUseResult": {
    "stdout": "    10 sections/abstract.tex\n  1353 sections/appendix.tex\n    10 sections/conclusion.tex\n    42 sections/discussion.tex\n   175 sections/experiments.tex\n    41 sections/introduction.tex\n    14 sections/limitations.tex\n    59 sections/method.tex\n    24 sections/related_work.tex\n    51 main.tex\n  1779 total",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3f17a7b2-4e28-45cd-9477-81678ce810cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-18T05:58:46.852Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014kgRQQRnC1fkyuJhsanMgR`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && cat sections/abstract.tex sections/introduction.tex sections/related_work.tex sections/method.tex sections/experiments.tex sections/discussion.tex sections/conclusion.tex sections/limitations.tex | wc -l",
  "description": "Count main body lines (excluding appendix)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39eaa2ff-16fb-40cc-80f0-9e03e56f0dbb",
  "isSidechain": false,
  "requestId": "req_011Cb9XE87G16YjaMcJtXVhq",
  "type": "assistant",
  "uuid": "38915ef0-70eb-4218-b549-13e72c0b92b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5agMXAUJa6E17pqoTNEYL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 284,
      "cache_read_input_tokens": 79542,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 284,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 79542,
          "cache_creation_input_tokens": 284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 284
          },
          "type": "message"
        }
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

_source line 97 · 2026-05-18T05:58:46.934Z_

<details><summary>↩ Tool result · `toolu_014kgRQQRnC1fkyuJhsanMgR`</summary>

```text
375
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38915ef0-70eb-4218-b549-13e72c0b92b0",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "ebdede8c-4449-4893-9a57-b0774bf7613e",
  "toolUseResult": {
    "stdout": "375",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "38915ef0-70eb-4218-b549-13e72c0b92b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-18T05:58:50.597Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HHcJWM1wZR8NSyvbBad4Kh`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && cat sections/abstract.tex sections/introduction.tex sections/related_work.tex sections/method.tex sections/experiments.tex sections/discussion.tex sections/conclusion.tex sections/limitations.tex | wc -w",
  "description": "Count main body word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebdede8c-4449-4893-9a57-b0774bf7613e",
  "isSidechain": false,
  "requestId": "req_011Cb9XESmAuW9BMkUk1Hevy",
  "type": "assistant",
  "uuid": "ac743c54-5664-4d04-ae53-5bb1dd406692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKWpQYChjSc2nSwZkBUshC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 224,
      "cache_read_input_tokens": 79826,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 79826,
          "cache_creation_input_tokens": 224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 224
          },
          "type": "message"
        }
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

_source line 99 · 2026-05-18T05:58:50.662Z_

<details><summary>↩ Tool result · `toolu_01HHcJWM1wZR8NSyvbBad4Kh`</summary>

```text
4635
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac743c54-5664-4d04-ae53-5bb1dd406692",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "240f0d5e-85b3-4052-8784-2191c6685945",
  "toolUseResult": {
    "stdout": "4635",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ac743c54-5664-4d04-ae53-5bb1dd406692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-18T05:58:53.429Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RAwVBdwU3TBFEhb2MWr67H`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && cat sections/abstract.tex | wc -w",
  "description": "Count abstract word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "240f0d5e-85b3-4052-8784-2191c6685945",
  "isSidechain": false,
  "requestId": "req_011Cb9XEiiccATmUfHSmok5N",
  "type": "assistant",
  "uuid": "7f0f08e7-e4a4-411e-919e-5899946ec8a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWZJWmwjZ8QpKenpAzdEyc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 222,
      "cache_read_input_tokens": 80050,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 80050,
          "cache_creation_input_tokens": 222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 222
          },
          "type": "message"
        }
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

_source line 101 · 2026-05-18T05:58:53.485Z_

<details><summary>↩ Tool result · `toolu_01RAwVBdwU3TBFEhb2MWr67H`</summary>

```text
178
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f0f08e7-e4a4-411e-919e-5899946ec8a2",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "2adde8ce-0c4c-4521-9b69-063ea60706e3",
  "toolUseResult": {
    "stdout": "178",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7f0f08e7-e4a4-411e-919e-5899946ec8a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-18T05:58:56.527Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X5cRjXqDnXBf4ta86pW8gB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2adde8ce-0c4c-4521-9b69-063ea60706e3",
  "isSidechain": false,
  "requestId": "req_011Cb9XEvnQRxQ6dMrDAmJv2",
  "type": "assistant",
  "uuid": "6da65eff-e62b-4849-8037-73de2033766b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DpZVgGbU6DRS2EmUiyweZU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 183,
      "cache_read_input_tokens": 80272,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 183,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 80272,
          "cache_creation_input_tokens": 183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 183
          },
          "type": "message"
        }
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

_source line 103 · 2026-05-18T05:58:56.532Z_

<details><summary>↩ Tool result · `toolu_01X5cRjXqDnXBf4ta86pW8gB`</summary>

```text
200	EM ranks first across all four tested conditional configurations: SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$). This holds despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
201	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
202	On the conditional set, where the model demonstrably produces varied outputs, exact agreement becomes the strongest quality signal.
203	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
204	
205	\paragraph{WNUT-17 full signal analysis.}
206	Table~\ref{tab:wnut} reports all five signals on WNUT-17 with full-set and conditional $\rho$.
207	
208	\begin{table}[t]
209	\centering
210	\small
211	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\rho$ reflects binary success prediction; conditional $\rho$ measures quality gradation. LP's conditional $\rho$ is highest despite negative full-set $\rho$.}
212	\label{tab:wnut}
213	\begin{tabular}{lcccc}
214	\toprule
215	Signal & $\rho$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
216	\midrule
217	VC      & .724 & .913 & .038 & .487 \\
218	FK      & .125 & .555 & .169 & .002 \\
219	SJ      & .089 & .517 & .288 & ${<}$1e-7 \\
220	EM      & .050 & .487 & .333 & ${<}$1e-9 \\
221	LP & $-$.410 & .219 & .350 & ${<}$1e-10 \\
222	\bottomrule
223	\end{tabular}
224	\end{table}
225	The full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.
226	VC's high full-set $\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, $p{=}0.49$), while LP's conditional $\rho{=}0.350$ is the highest among all signals on the non-zero subset, full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
227	
228	\paragraph{Cross-configuration selection analysis.}
229	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
230	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
231	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect (single-sample F1 ${\approx}$0.91--0.92) rather than signal failure, and selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
232	
233	\begin{table*}[t]
234	\centering
235	\small
236	\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
237	\label{tab:cross_selection}
238	\begin{tabular}{llccccccc}
239	\toprule
240	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
241	\midrule
242	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
243	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
244	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
245	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
246	\bottomrule
247	\end{tabular}
248	\end{table*}
249	
250	\paragraph{Diminishing returns of $N$-scaling.}
251	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
252	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
253	Structural signals use $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, each additional comparison yields diminishing information.
254	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
255	For sample selection, additional samples increase the oracle upper bound (more draws raise the probability of a high-quality candidate), but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
256	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
257	
258	\paragraph{$N{=}16$ CoNLL selection: small but significant.}
259	While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.
260	VC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
261	These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
262	This reinforces the primary finding: even under the most favorable conditions (high baseline performance, more candidates, and aggregated multi-seed evidence), signal-based selection recovers only a fraction of the oracle headroom available.
263	
264	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
265	
266	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
267	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, the structural advantage reported in \S\ref{sec:qe_results} is robust.
268	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant; these two structural signals perform comparably.
269	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
270	
271	\begin{table}[t]
272	\centering
273	\small
274	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
275	\label{tab:bootstrap_signal_ci}
276	\begin{tabular}{lcc}
277	\toprule
278	Signal & $\rho$ & 95\% CI \\
279	\midrule
280	VC & +0.379 & [+0.299, +0.456] \\
281	SJ & +0.360 & [+0.277, +0.437] \\
282	EM & +0.295 & [+0.212, +0.371] \\
283	FK & +0.267 & [+0.176, +0.354] \\
284	LP & +0.205 & [+0.119, +0.291] \\
285	\bottomrule
286	\end{tabular}
287	
288	\vspace{0.5em}
289	
290	\begin{tabular}{lccc}
291	\toprule
292	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
293	\midrule
294	SJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\
295	VC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
296	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
297	\bottomrule
298	\end{tabular}
299	
300	\smallskip
301	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
302	\end{table}
303	
304	At $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.
305	On SciERC NER ($n{=}529$), SJ--FK ($\Delta\rho{=}0.147$--$0.160$, all $p{\leq}0.002$) and VC--FK ($\Delta\rho{=}0.138$--$0.188$, all $p{\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\Delta\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).
306	On CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\Delta\rho{=}0.071$ ($p{<}0.001$), SJ $\Delta\rho{=}0.056$ ($p{<}0.001$), VC $\Delta\rho{=}0.022$ ($p{=}0.040$).
307	
308	\section{Diversity and Selection Analysis}\label{app:diversity}
309	
310	\begin{figure*}[t]
311	\centering
312	\includegraphics[width=\textwidth]{fig_selection_gap}
313	\caption{The correlation-selection gap on SciERC NER ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.40, no signal significantly outperforms single-sample (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound. RE selection results in Table~\ref{tab:selection}.}
314	\label{fig:selection_gap}
315	\end{figure*}
316	
317	\paragraph{Output diversity quantification.}
318	Table~\ref{tab:diversity} summarizes output diversity across configurations.
319	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
320	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
321	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect where single-sample F1 already exceeds 0.90.
322	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
323	
324	\begin{table}[t]
325	\centering
326	\small
327	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
328	\label{tab:diversity}
329	\begin{tabular}{lcc}
330	\toprule
331	Config & Identical & Unique \\
332	\midrule
333	Qwen/SciERC & 11\% & 43\% \\
334	LLaMA/SciERC & 18\% & 39\% \\
335	Qwen/CoNLL & 57\% & --- \\
336	LLaMA/CoNLL & 88\% & --- \\
337	WNUT-17 & 55\% & --- \\
338	\bottomrule
339	\end{tabular}
340	\end{table}
341	
342	\paragraph{Oracle-improvable fraction.}
343	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding single-sample\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \S\ref{sec:evaluation}); the diversity quantification in Table~\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
344	On CoNLL, only 4--9\% of instances are improvable, consistent with the ceiling effect.
345	
346	\paragraph{Diversity-stratified selection gap.}
347	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below single-sample, and LP, the only per-sample signal, achieves merely $+$0.8~pp.
348	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below single-sample and LP captures only $+$2.0~pp.
349	This rules out insufficient diversity as an explanation for the correlation-selection gap.
350	
351	\paragraph{Instance degeneracy statistics.}
352	Table~\ref{tab:degeneracy} quantifies instance degeneracy across configurations. ``Constant F1'' denotes instances where all $N$ samples receive identical instance-level F1; ``Constant utility'' denotes instances where MBR (SJ) utility is identical across candidates, preventing ranking.
353	
354	\begin{table}[t]
355	\centering
356	\small
357	\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}
358	\label{tab:degeneracy}
359	\begin{tabular}{lccc}
360	\toprule
361	& \shortstack{SciERC 8B\\($N{=}8$)} & \shortstack{SciERC 4B\\($N{=}8$)} & \shortstack{CoNLL 8B\\($N{=}16$)} \\
362	\midrule
363	Constant F1 & 17.8\% & 10.4\% & 48.3\% \\
364	Constant utility & 13\% & 7.0\% & 49\% \\
365	Oracle gap closed (non-deg.) & 23\% & 25.2\% & 41\% \\
366	Within-inst.\ SJ $\rho$ (median) & 0.524 & 0.550 & 0.994 \\
367	\bottomrule
368	\end{tabular}
369	\end{table}
370	
371	\paragraph{TOST equivalence testing.}\label{app:tost}
372	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
373	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\delta$.
374	The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
375	These proportions use the same test data that defines the headroom, introducing circularity: $\delta$ is anchored to the very quantity it contextualizes.
376	We address this below with externally anchored equivalence margins.
377	The breakpoint $\delta^*$, the minimum equivalence margin at which each signal passes TOST, ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
378	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
379	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
380	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
381	
382	\begin{table}[t]
383	\centering
384	\small
385	\caption{TOST equivalence testing: signals vs.\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ single-sample).}
386	\label{tab:tost}
387	\begin{tabular}{l cccc cccc}
388	\toprule
389	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
390	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
391	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
392	\midrule
393	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
394	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
395	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
396	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
397	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
398	\bottomrule
399	\end{tabular}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6da65eff-e62b-4849-8037-73de2033766b",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "9294e396-aece-4480-8853-018468e7a601",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "EM ranks first across all four tested conditional configurations: SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$). This holds despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set, where the model demonstrably produces varied outputs, exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17 with full-set and conditional $\\rho$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\\rho$ reflects binary success prediction; conditional $\\rho$ measures quality gradation. LP's conditional $\\rho$ is highest despite negative full-set $\\rho$.}\n\\label{tab:wnut}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\rho$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & .913 & .038 & .487 \\\\\nFK      & .125 & .555 & .169 & .002 \\\\\nSJ      & .089 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\nThe full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.\nVC's high full-set $\\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, $p{=}0.49$), while LP's conditional $\\rho{=}0.350$ is the highest among all signals on the non-zero subset, full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn CoNLL, 57--88\\% of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect (single-sample F1 ${\\approx}$0.91--0.92) rather than signal failure, and selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \\textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals use $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, each additional comparison yields diminishing information.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound (more draws raise the probability of a high-quality candidate), but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\paragraph{$N{=}16$ CoNLL selection: small but significant.}\nWhile quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.\nVC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).\nThese gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\\% of the available headroom.\nThis reinforces the primary finding: even under the most favorable conditions (high baseline performance, more candidates, and aggregated multi-seed evidence), signal-based selection recovers only a fraction of the oracle headroom available.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, the structural advantage reported in \\S\\ref{sec:qe_results} is robust.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant; these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVC & +0.379 & [+0.299, +0.456] \\\\\nSJ & +0.360 & [+0.277, +0.437] \\\\\nEM & +0.295 & [+0.212, +0.371] \\\\\nFK & +0.267 & [+0.176, +0.354] \\\\\nLP & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\\\\nVC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\nAt $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.\nOn SciERC NER ($n{=}529$), SJ--FK ($\\Delta\\rho{=}0.147$--$0.160$, all $p{\\leq}0.002$) and VC--FK ($\\Delta\\rho{=}0.138$--$0.188$, all $p{\\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\\Delta\\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).\nOn CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\\Delta\\rho{=}0.071$ ($p{<}0.001$), SJ $\\Delta\\rho{=}0.056$ ($p{<}0.001$), VC $\\Delta\\rho{=}0.022$ ($p{=}0.040$).\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC NER ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.40, no signal significantly outperforms single-sample (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound. RE selection results in Table~\\ref{tab:selection}.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 57\\% (Qwen) to 88\\% (LLaMA) of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect where single-sample F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding single-sample\\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \\S\\ref{sec:evaluation}); the diversity quantification in Table~\\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, consistent with the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below single-sample, and LP, the only per-sample signal, achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below single-sample and LP captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{Instance degeneracy statistics.}\nTable~\\ref{tab:degeneracy} quantifies instance degeneracy across configurations. ``Constant F1'' denotes instances where all $N$ samples receive identical instance-level F1; ``Constant utility'' denotes instances where MBR (SJ) utility is identical across candidates, preventing ranking.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}\n\\label{tab:degeneracy}\n\\begin{tabular}{lccc}\n\\toprule\n& \\shortstack{SciERC 8B\\\\($N{=}8$)} & \\shortstack{SciERC 4B\\\\($N{=}8$)} & \\shortstack{CoNLL 8B\\\\($N{=}16$)} \\\\\n\\midrule\nConstant F1 & 17.8\\% & 10.4\\% & 48.3\\% \\\\\nConstant utility & 13\\% & 7.0\\% & 49\\% \\\\\nOracle gap closed (non-deg.) & 23\\% & 25.2\\% & 41\\% \\\\\nWithin-inst.\\ SJ $\\rho$ (median) & 0.524 & 0.550 & 0.994 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{TOST equivalence testing.}\\label{app:tost}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\\delta$.\nThe $\\delta$ values are contextualized against oracle headroom (12--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\nThese proportions use the same test data that defines the headroom, introducing circularity: $\\delta$ is anchored to the very quantity it contextualizes.\nWe address this below with externally anchored equivalence margins.\nThe breakpoint $\\delta^*$, the minimum equivalence margin at which each signal passes TOST, ranges from approximately 1.3~pp (SJ, ${\\sim}$10\\% of oracle headroom) to 3.4~pp (FK, ${\\sim}$26\\%) on NER, and from approximately 2.9~pp (LP, ${\\sim}$16\\%) to 6.5~pp (VC, ${\\sim}$36\\%) on RE.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ single-sample).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}",
      "numLines": 200,
      "startLine": 200,
      "totalLines": 1354
    }
  },
  "sourceToolAssistantUUID": "6da65eff-e62b-4849-8037-73de2033766b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
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
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）  ### 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction - **路径**: `projects…",
  "leafUuid": "9294e396-aece-4480-8853-018468e7a601",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Runtime record

_source line 105_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured IE paper for EMNLP 2026",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Assistant

_source line 106 · 2026-05-18T05:58:59.903Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now check the rest of the appendix for key content and see if there are any figures directories.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9294e396-aece-4480-8853-018468e7a601",
  "isSidechain": false,
  "requestId": "req_011Cb9XFAnmSZNvPmJLsAzDf",
  "type": "assistant",
  "uuid": "9b94f7fc-aed9-49b0-8204-4c49342a0e34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ftutm5wiUgkLCizJMFnus",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6313,
      "cache_read_input_tokens": 80455,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6313,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 80455,
          "cache_creation_input_tokens": 6313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6313
          },
          "type": "message"
        }
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

_source line 107 · 2026-05-18T05:59:00.903Z_

Let me also check for some more appendix content and search for key missing related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b94f7fc-aed9-49b0-8204-4c49342a0e34",
  "isSidechain": false,
  "requestId": "req_011Cb9XFAnmSZNvPmJLsAzDf",
  "type": "assistant",
  "uuid": "d7e9cf29-4792-46fe-b384-9db2da4556e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ftutm5wiUgkLCizJMFnus",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6313,
      "cache_read_input_tokens": 80455,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6313,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 80455,
          "cache_creation_input_tokens": 6313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6313
          },
          "type": "message"
        }
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

_source line 108 · 2026-05-18T05:59:02.613Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Mcrjn8LaNytRdtQcnzBHbX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 400,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7e9cf29-4792-46fe-b384-9db2da4556e0",
  "isSidechain": false,
  "requestId": "req_011Cb9XFAnmSZNvPmJLsAzDf",
  "type": "assistant",
  "uuid": "154e76d7-baa8-4d9a-94e3-99173dfc5a81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ftutm5wiUgkLCizJMFnus",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6313,
      "cache_read_input_tokens": 80455,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6313,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 80455,
          "cache_creation_input_tokens": 6313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6313
          },
          "type": "message"
        }
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

_source line 109 · 2026-05-18T05:59:02.619Z_

<details><summary>↩ Tool result · `toolu_01Mcrjn8LaNytRdtQcnzBHbX`</summary>

```text
400	\end{table}
401	
402	\paragraph{External equivalence margins.}
403	The oracle-headroom anchors above introduce circularity, as a reviewer correctly noted: $\delta$ is calibrated against the very quantity it contextualizes.
404	To resolve this, we supplement with three externally grounded margins:
405	(1) $\delta_{\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), which represents measurement noise;
406	(2) $\delta_{\mathrm{practical}}{=}0.5$~pp, the threshold below which NER differences are considered negligible \cite{ratinov2009design};
407	(3) $\delta_{\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \cite{bergkirkpatrick2012empirical}.
408	
409	Results under these external anchors diverge sharply by configuration.
410	On LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\Delta|{\leq}0.1$~pp) and tight CIs at this sample size.
411	On Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, which exceeds even $\delta_{\mathrm{literature}}$.
412	On SciERC NER ($n{=}529$), only SJ passes at $\delta_{\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.
413	These external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.
414	
415	\paragraph{Multiple comparison considerations.}\label{app:multiple_comparisons}
416	Our primary selection analysis involves ${\sim}$20 comparisons (5 signals $\times$ 3--4 configurations).
417	Since all primary selection results are non-significant ($p{>}0.05$), applying Benjamini-Hochberg correction can only make these results more conservative, strengthening the ``no signal beats greedy'' conclusion.
418	The sole positive finding, the non-tied LP subset ($+2.9$~pp, $p{=}0.004$; \S\ref{sec:discussion}), survives Bonferroni correction over 5 signal comparisons ($p_{\mathrm{adj}}{=}0.020 < 0.05$), as noted in the main text footnote.
419	For quality estimation signal rankings, differences between the top signals (e.g., VC vs.\ SJ on SciERC) should be interpreted as descriptive rather than as statistically confirmed orderings, given the limited power of 3-seed comparisons.
420	
421	\section{Multi-Seed Stability}\label{app:multiseed}
422	
423	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
424	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).
425	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM. This reversal from the NER ranking reflects RE's higher sensitivity to per-sample scoring.
426	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
427	
428	\begin{table}[t]
429	\centering
430	\small
431	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
432	\label{tab:multiseed}
433	\begin{tabular}{lccccc}
434	\toprule
435	& LP & FK & SJ & VC & EM \\
436	\midrule
437	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
438	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
439	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
440	\midrule
441	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
442	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
443	\midrule
444	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
445	Qwen & .579${\pm}$.008 & .600${\pm}$.016 & .659${\pm}$.016 & .677${\pm}$.011 & .631${\pm}$.013 \\
446	LLaMA & .565${\pm}$.008 & .593${\pm}$.006 & .632${\pm}$.012 & .673${\pm}$.009 & .606${\pm}$.005 \\
447	\bottomrule
448	\end{tabular}
449	\end{table}
450	
451	\section{Training Configuration}\label{app:training}
452	
453	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
454	
455	\begin{table}[t]
456	\centering
457	\small
458	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
459	\label{tab:training}
460	\begin{tabular}{ll}
461	\toprule
462	Parameter & Value \\
463	\midrule
464	LoRA rank / $\alpha$ & 32 / 64 \\
465	LoRA target & All linear modules \\
466	LoRA dropout & 0 \\
467	Optimizer & AdamW \\
468	Learning rate & 2e-4, cosine schedule \\
469	Warmup ratio & 0.1 \\
470	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
471	Epochs & 5 \\
472	Max sequence length & 2048 \\
473	Precision & bf16 \\
474	Gradient checkpointing & Enabled \\
475	Max gradient norm & 1.0 \\
476	Training seed & 42 \\
477	Framework & LLaMA Factory \\
478	\midrule
479	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
480	SciERC split & 1861 / 275 / 551 \\
481	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
482	& eval\_steps${=}$200, save\_limit${=}$5 \\
483	\bottomrule
484	\end{tabular}
485	\end{table}
486	
487	\paragraph{Prompt template.}
488	For NER, we use a structured prompt:
489	\begin{quote}
490	\small
491	\texttt{System:} You are an expert in Named Entity Recognition.\\
492	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
493	Text: \texttt{\{input\_text\}}\\
494	Entity types: \texttt{\{schema\_types\}}
495	\end{quote}
496	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
497	
498	\paragraph{Constrained decoding.}
499	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
500	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
501	
502	\section{Thinking Token Impact Analysis}\label{app:thinking_token}
503	
504	Qwen3-8B's SciERC checkpoint was trained with empty \texttt{&lt;think>&lt;/think>} blocks prepended to each response (\S\ref{sec:setup}).
505	We quantify the potential impact on LP scores through three complementary arguments.
506	
507	\paragraph{LP shift magnitude.}
508	Empty thinking tokens (mean 4.5 per sample) constitute 2.1\% of tokens on SciERC.
509	The estimated LP shift is 0.001 nats per token (2.68\% of the median within-instance LP range of 0.041 nats).
510	Because all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\%$ of instances.
511	
512	\paragraph{Constant prefix cancellation.}
513	All $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.
514	Any LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \textit{rankings} unchanged.
515	
516	\paragraph{CoNLL control group.}
517	CoNLL and WNUT-17 checkpoints were trained without thinking tokens (\texttt{enable\_thinking=False}).
518	If thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.
519	Instead, CoNLL shows \textit{higher} tied fractions at both temperatures (86.8\% at $T{=}1.0$, 95.8\% at $T{=}0.7$) than SciERC (60.3\% at $T{=}1.0$), directly contradicting the thinking-token hypothesis.
520	
521	\section{Log-Probability Score Compression}\label{app:logprob_ties}
522	
523	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
524	The median within-instance LP range is only 0.041 nats; we use $\varepsilon{=}0.05$ as an illustrative threshold to characterize this compression.
525	At this cutpoint, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\varepsilon$, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
526	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}); compression is a pervasive regime rather than a bimodal split.
527	This compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\%$ (vs.\ seed${=}42$: $0.041$ nats, $60.3\%$).
528	Seed~456 uses a different subtask flag (joint vs.\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\ 8.20 nats; Mann--Whitney $p{=}0.55$); the subtask change does not affect compression.
529	For comparison, SJ has only 12.5\% tied instances at the same threshold; SJ's advantage over LP for selection is one of score resolution, not information content.
530	
531	\begin{figure}[t]
532	\centering
533	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
534	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
535	\label{fig:lp_range_cdf}
536	\end{figure}
537	
538	\begin{table}[t]
539	\centering
540	\small
541	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
542	\label{tab:logprob_ties}
543	\begin{tabular}{lc}
544	\toprule
545	$\varepsilon$ threshold & Tied instances (\%) \\
546	\midrule
547	0.01 & 1.1\% \\
548	0.05 & 60.3\% \\
549	0.1  & ${\sim}$84\% \\
550	0.5  & ${\sim}$99\% \\
551	\bottomrule
552	\end{tabular}
553	\end{table}
554	
555	\paragraph{Non-tied subset.}
556	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms single-sample ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
557	As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability. LP carries information, but compression limits its exploitation.
558	A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
559	
560	\paragraph{$\varepsilon$ sensitivity sweep (post-hoc exploratory).}
561	Table~\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\varepsilon{=}0.01$ to $0.20$ as a post-hoc exploratory analysis characterizing how selection gain varies with compression severity.
562	The tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.
563	$\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\varepsilon{\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\leq}36$).
564	
565	\begin{table}[t]
566	\centering
567	\small
568	\caption{$\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\%'' = fraction with within-instance LP range ${<}\varepsilon$. $\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\varepsilon{=}0.05$ yields the strongest statistical separation.}
569	\label{tab:epsilon_sweep}
570	\begin{tabular}{ccccc}
571	\toprule
572	$\varepsilon$ & Tied\% & Non-tied $n$ & $\Delta$ (pp) & $p$ \\
573	\midrule
574	0.01 & 1.1\% & 523 & $+$0.58 & .21 \\
575	0.02 & 13.6\% & 457 & $+$0.83 & .15 \\
576	0.03 & 31.8\% & 361 & $+$1.31 & .079 \\
577	\textbf{0.05} & \textbf{60.3\%} & \textbf{210} & \textbf{$+$2.86} & \textbf{.004} \\
578	0.10 & 83.9\% & 85 & $+$3.69 & .034 \\
579	0.15 & 93.2\% & 36 & $+$4.15 & .11 \\
580	0.20 & 96.4\% & 19 & $+$4.59 & .13 \\
581	\bottomrule
582	\end{tabular}
583	\end{table}
584	
585	\paragraph{$\varepsilon$ robustness of selection F1.}\label{app:epsilon_robustness}
586	The preceding analysis stratifies LP by a tied/non-tied threshold; consistency-based signals (SJ, FK, VC, EM) also use $\varepsilon$ to define MBR-style proximity in selection.
587	Table~\ref{tab:epsilon_robustness} reports the maximum selection F1 variation across $\varepsilon \in [0, 0.2]$ for all signals and configurations.
588	At $\varepsilon{=}0.05$, consistency signals change by at most 1.09~pp (mean 0.21~pp), with EM completely $\varepsilon$-invariant (integer scoring); LP is the most sensitive (up to 3.65~pp across the full range), as expected.
589	Spearman $\rho$, the primary quality estimation metric throughout, is a continuous rank correlation that does not depend on any discretization threshold; the $\varepsilon$ parameter affects only the selection analysis.
590	
591	\begin{table}[t]
592	\centering
593	\small
594	\caption{Maximum selection F1 variation (pp) across $\varepsilon \in [0, 0.2]$. At $\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\varepsilon$ governs its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}
595	\label{tab:epsilon_robustness}
596	\begin{tabular}{lcccc}
597	\toprule
598	& \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL}} \\
599	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "154e76d7-baa8-4d9a-94e3-99173dfc5a81",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "5ccebf73-1330-4c27-89c9-719e3a3fa0f0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\end{table}\n\n\\paragraph{External equivalence margins.}\nThe oracle-headroom anchors above introduce circularity, as a reviewer correctly noted: $\\delta$ is calibrated against the very quantity it contextualizes.\nTo resolve this, we supplement with three externally grounded margins:\n(1) $\\delta_{\\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), which represents measurement noise;\n(2) $\\delta_{\\mathrm{practical}}{=}0.5$~pp, the threshold below which NER differences are considered negligible \\cite{ratinov2009design};\n(3) $\\delta_{\\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \\cite{bergkirkpatrick2012empirical}.\n\nResults under these external anchors diverge sharply by configuration.\nOn LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\\Delta|{\\leq}0.1$~pp) and tight CIs at this sample size.\nOn Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, which exceeds even $\\delta_{\\mathrm{literature}}$.\nOn SciERC NER ($n{=}529$), only SJ passes at $\\delta_{\\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.\nThese external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.\n\n\\paragraph{Multiple comparison considerations.}\\label{app:multiple_comparisons}\nOur primary selection analysis involves ${\\sim}$20 comparisons (5 signals $\\times$ 3--4 configurations).\nSince all primary selection results are non-significant ($p{>}0.05$), applying Benjamini-Hochberg correction can only make these results more conservative, strengthening the ``no signal beats greedy'' conclusion.\nThe sole positive finding, the non-tied LP subset ($+2.9$~pp, $p{=}0.004$; \\S\\ref{sec:discussion}), survives Bonferroni correction over 5 signal comparisons ($p_{\\mathrm{adj}}{=}0.020 < 0.05$), as noted in the main text footnote.\nFor quality estimation signal rankings, differences between the top signals (e.g., VC vs.\\ SJ on SciERC) should be interpreted as descriptive rather than as statistically confirmed orderings, given the limited power of 3-seed comparisons.\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\nOn NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).\nOn RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM. This reversal from the NER ranking reflects RE's higher sensitivity to per-sample scoring.\nLLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .579${\\pm}$.008 & .600${\\pm}$.016 & .659${\\pm}$.016 & .677${\\pm}$.011 & .631${\\pm}$.013 \\\\\nLLaMA & .565${\\pm}$.008 & .593${\\pm}$.006 & .632${\\pm}$.012 & .673${\\pm}$.009 & .606${\\pm}$.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}\n\n\\section{Thinking Token Impact Analysis}\\label{app:thinking_token}\n\nQwen3-8B's SciERC checkpoint was trained with empty \\texttt{&lt;think>&lt;/think>} blocks prepended to each response (\\S\\ref{sec:setup}).\nWe quantify the potential impact on LP scores through three complementary arguments.\n\n\\paragraph{LP shift magnitude.}\nEmpty thinking tokens (mean 4.5 per sample) constitute 2.1\\% of tokens on SciERC.\nThe estimated LP shift is 0.001 nats per token (2.68\\% of the median within-instance LP range of 0.041 nats).\nBecause all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\\%$ of instances.\n\n\\paragraph{Constant prefix cancellation.}\nAll $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.\nAny LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \\textit{rankings} unchanged.\n\n\\paragraph{CoNLL control group.}\nCoNLL and WNUT-17 checkpoints were trained without thinking tokens (\\texttt{enable\\_thinking=False}).\nIf thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.\nInstead, CoNLL shows \\textit{higher} tied fractions at both temperatures (86.8\\% at $T{=}1.0$, 95.8\\% at $T{=}0.7$) than SciERC (60.3\\% at $T{=}1.0$), directly contradicting the thinking-token hypothesis.\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}, Figure~\\ref{fig:lp_range_cdf}).\nThe median within-instance LP range is only 0.041 nats; we use $\\varepsilon{=}0.05$ as an illustrative threshold to characterize this compression.\nAt this cutpoint, 60.3\\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\\varepsilon$, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nThe CDF rises smoothly with no cliff or discontinuity (Figure~\\ref{fig:lp_range_cdf}); compression is a pervasive regime rather than a bimodal split.\nThis compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\\%$ (vs.\\ seed${=}42$: $0.041$ nats, $60.3\\%$).\nSeed~456 uses a different subtask flag (joint vs.\\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\\ 8.20 nats; Mann--Whitney $p{=}0.55$); the subtask change does not affect compression.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold; SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_lp_range_cdf}\n\\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}\n\\label{fig:lp_range_cdf}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms single-sample ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nAs a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\\rho(\\text{LP}, \\text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\\% of instances achieve $p{<}0.05$ significance, and $\\rho(\\text{LP range}, \\text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability. LP carries information, but compression limits its exploitation.\nA free-form NER decoding ablation (Appendix~\\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.\n\n\\paragraph{$\\varepsilon$ sensitivity sweep (post-hoc exploratory).}\nTable~\\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\\varepsilon{=}0.01$ to $0.20$ as a post-hoc exploratory analysis characterizing how selection gain varies with compression severity.\nThe tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.\n$\\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\\varepsilon{\\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\\leq}36$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\\%'' = fraction with within-instance LP range ${<}\\varepsilon$. $\\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\\varepsilon{=}0.05$ yields the strongest statistical separation.}\n\\label{tab:epsilon_sweep}\n\\begin{tabular}{ccccc}\n\\toprule\n$\\varepsilon$ & Tied\\% & Non-tied $n$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n0.01 & 1.1\\% & 523 & $+$0.58 & .21 \\\\\n0.02 & 13.6\\% & 457 & $+$0.83 & .15 \\\\\n0.03 & 31.8\\% & 361 & $+$1.31 & .079 \\\\\n\\textbf{0.05} & \\textbf{60.3\\%} & \\textbf{210} & \\textbf{$+$2.86} & \\textbf{.004} \\\\\n0.10 & 83.9\\% & 85 & $+$3.69 & .034 \\\\\n0.15 & 93.2\\% & 36 & $+$4.15 & .11 \\\\\n0.20 & 96.4\\% & 19 & $+$4.59 & .13 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{$\\varepsilon$ robustness of selection F1.}\\label{app:epsilon_robustness}\nThe preceding analysis stratifies LP by a tied/non-tied threshold; consistency-based signals (SJ, FK, VC, EM) also use $\\varepsilon$ to define MBR-style proximity in selection.\nTable~\\ref{tab:epsilon_robustness} reports the maximum selection F1 variation across $\\varepsilon \\in [0, 0.2]$ for all signals and configurations.\nAt $\\varepsilon{=}0.05$, consistency signals change by at most 1.09~pp (mean 0.21~pp), with EM completely $\\varepsilon$-invariant (integer scoring); LP is the most sensitive (up to 3.65~pp across the full range), as expected.\nSpearman $\\rho$, the primary quality estimation metric throughout, is a continuous rank correlation that does not depend on any discretization threshold; the $\\varepsilon$ parameter affects only the selection analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Maximum selection F1 variation (pp) across $\\varepsilon \\in [0, 0.2]$. At $\\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\\varepsilon$ governs its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}\n\\label{tab:epsilon_robustness}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}",
      "numLines": 200,
      "startLine": 400,
      "totalLines": 1354
    }
  },
  "sourceToolAssistantUUID": "154e76d7-baa8-4d9a-94e3-99173dfc5a81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 110 · 2026-05-18T05:59:02.682Z_

```json
{
  "parentUuid": "5ccebf73-1330-4c27-89c9-719e3a3fa0f0",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a7accc6e-c28d-4efc-8906-c3adf06ee8e3",
  "timestamp": "2026-05-18T05:59:02.682Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 111_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）  ### 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction - **路径**: `projects…",
  "leafUuid": "a7accc6e-c28d-4efc-8906-c3adf06ee8e3",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Runtime record

_source line 112_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured IE paper for EMNLP 2026",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Tool call

_source line 113 · 2026-05-18T05:59:07.405Z_

<details open><summary>🔧 Tool call — Read · `toolu_012D2jiQ3uQzWfQkYDxb8CtJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 600,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7accc6e-c28d-4efc-8906-c3adf06ee8e3",
  "isSidechain": false,
  "requestId": "req_011Cb9XFc43pVsKQ8WjFco5w",
  "type": "assistant",
  "uuid": "41e084e2-3d1a-44b8-aea4-f75d56d5a54b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nzwt9YJJfNg8aMC6toiYnu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5631,
      "cache_read_input_tokens": 86768,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 86768,
          "cache_creation_input_tokens": 5631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5631
          },
          "type": "message"
        }
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

_source line 114 · 2026-05-18T05:59:07.410Z_

<details><summary>↩ Tool result · `toolu_012D2jiQ3uQzWfQkYDxb8CtJ`</summary>

```text
600	Signal & Qwen & LLaMA & Qwen & LLaMA \\
601	\midrule
602	SJ & 0.92 & 1.45 & 0.99 & 0.18 \\
603	FK & 1.03 & 0.93 & 0.60 & 0.15 \\
604	VC & 2.33 & 0.53 & 0.72 & 0.18 \\
605	EM & 0.00 & 0.00 & 0.00 & 0.00 \\
606	LP & 3.65 & 2.58 & 3.00 & 0.31 \\
607	\bottomrule
608	\end{tabular}
609	\end{table}
610	
611	\paragraph{Non-tied subset analysis.}
612	Table~\ref{tab:nontied_main} presents the non-tied subset analysis referenced in \S\ref{sec:discussion}.
613	
614	\begin{table}[t]
615	\centering
616	\small
617	\caption{Non-tied subset analysis (SciERC, Qwen3-8B, $N{=}8$, $T{=}1.0$). Instances split at LP range $\varepsilon{=}0.05$. Within-instance $\rho$ and selection gain both concentrate in the non-tied subset. Full $\varepsilon$ sweep in Table~\ref{tab:epsilon_sweep}.}
618	\label{tab:nontied_main}
619	\begin{tabular}{lccc}
620	\toprule
621	Subset & $n$ & $\rho$(LP,F1) & LP $\Delta$ vs.\ greedy \\
622	\midrule
623	Tied (range ${<}0.05$) & 319 & 0.08 & ${\approx}0$ \\
624	Non-tied (range ${\geq}0.05$) & 210 & 0.39 & $+$2.9~pp ($p{=}0.004$) \\
625	\midrule
626	All instances & 529 & 0.248 & $+$0.2~pp ($p{=}0.29$) \\
627	\bottomrule
628	\end{tabular}
629	\end{table}
630	
631	\section{Consistency-Stratified Selection Analysis}\label{app:vc_quartile}
632	
633	Table~\ref{tab:vc_quartile} stratifies SciERC instances by voting confidence (VC) quartiles and reports selection $\Delta$ (gain over single-sample) for LP and SJ.
634	
635	\begin{table}[t]
636	\centering
637	\small
638	\caption{Selection $\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}
639	\label{tab:vc_quartile}
640	\begin{tabular}{lcccc}
641	\toprule
642	Quartile & Mean VC & LP $\Delta$ & SJ $\Delta$ & Oracle (pp) \\
643	\midrule
644	\multicolumn{5}{l}{\textit{NER}} \\
645	Q1 (low) & 0.30 & $+$1.55 & $+$0.54 & 16.85 \\
646	Q2 & 0.51 & $-$0.65 & $-$1.89 & 14.35 \\
647	Q3 & 0.68 & $+$1.97 & $+$1.84 & 16.83 \\
648	Q4 (high) & 0.92 & $-$0.41 & $-$0.04 & 4.78 \\
649	\midrule
650	\multicolumn{5}{l}{\textit{$^\dagger$RE}} \\
651	Q1 (low) & --- & $-$3.56 & --- & --- \\
652	Q4 (high) & --- & $+$4.01 & --- & --- \\
653	\bottomrule
654	\end{tabular}
655	\end{table}
656	
657	The NER pattern reveals two complementary failure modes rather than a monotonic relationship between consistency and selection gain:
658	\begin{itemize}
659	\item \textbf{Q4 ceiling effect.} High-consistency instances (mean VC${=}0.92$) have oracle headroom of only 4.78~pp. Samples have already converged, leaving little room for any signal to improve selection.
660	\item \textbf{Q1--Q2 noise.} Low-consistency instances retain large headroom (14--17~pp) but LP rankings are unreliable, and LP rankings produce inconsistent $\Delta$ signs across quartiles.
661	\end{itemize}
662	
663	On $^\dagger$RE, the pattern differs: Q4 LP achieves $+4.01$~pp; LP may recover selection ability when high consistency coincides with structured output diversity. This is a single-dataset observation and should be interpreted cautiously.
664	
665	On CoNLL NER, Q3--Q4 instances have VC${=}1.0$ (all samples identical), and $\Delta{=}0$ universally; this ceiling effect is even more extreme than SciERC Q4.
666	
667	\section{Exploratory Extension to Relation Extraction}\label{app:re_extension}
668	
669	We extend the NER evaluation to relation extraction (RE) on SciERC as an exploratory single-benchmark analysis.
670	RE produces sets of (head, relation, tail) triples with partial overlap; 40\% of RE instances receive zero F1, and entity span errors account for 55.5\% of RE false negatives, a prerequisite failure that consistency signals cannot detect (\S\ref{app:additional}).
671	All RE results use Qwen3-8B unless noted; single-seed ($\text{seed}{=}42$) for $N{=}8$ analyses, 3-seed for $N{=}16$.
672	
673	\paragraph{Quality estimation.}
674	RE quality estimation is reported in Table~\ref{tab:multiseed} (3-seed means).
675	The signal ranking differs from NER: VC leads ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM, a reversal reflecting RE's higher sensitivity to per-sample scoring.
676	RE miscalibration is more severe than NER (ECE 0.109--0.339; Figure~\ref{fig:reliability}).
677	
678	\paragraph{Selection.}
679	Table~\ref{tab:re_cond_selection} presents RE selection at $N{=}8$: no signal outperforms single-sample (0.404) on the full set ($n{=}397$) or the non-zero subset ($n{=}238$), with 18.1~pp of unrealized oracle headroom.
680	At $N{=}16$ (Qwen3-4B, Table~\ref{tab:re_n16_selection}), LP is the sole positive signal ($\Delta{=}{+}0.7$~pp, $p{=}0.058$), consistent with LP being the strongest RE selection signal across scales.
681	
682	\paragraph{Scale ablation.}
683	At 4B scale (Qwen3-4B, $N{=}8$, $\text{seed}{=}42$), RE quality estimation shows FK $\rho{=}0.359$ and LP $\rho{=}0.351$, both above their 8B counterparts (FK 0.275, LP 0.266), while SJ declines ($0.267$ vs.\ $0.250$).
684	Selection remains below single-sample on RE ($\Delta$ up to $-3.4$~pp) despite 17.1~pp of oracle headroom.
685	
686	\paragraph{Free-form decoding.}
687	RE LP selection consistently reverses direction under free-form decoding ($+1.8{\pm}0.1$~pp across 4 seeds vs.\ $-0.9$~pp under constrained decoding at 8B; \S\ref{app:freeform_ablation}); constrained decoding's fixed template likely obscures LP signal in RE (\S\ref{app:mbr_discussion}).
688	
689	\section{RE Conditional Selection}\label{app:re_conditional_selection}
690	
691	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
692	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
693	All five signals underperform single-sample on both subsets.
694	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because single-sample is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
695	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
696	
697	\begin{table}[t]
698	\centering
699	\small
700	\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
701	\label{tab:re_cond_selection}
702	\begin{tabular}{lcc}
703	\toprule
704	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
705	\midrule
706	Oracle & 0.585 & 0.757 \\
707	\midrule
708	LP & 0.395 & 0.600 \\
709	SJ & 0.386 & 0.604 \\
710	EM & 0.372 & 0.583 \\
711	VC & 0.359 & 0.574 \\
712	\midrule
713	Greedy & 0.404 & 0.674 \\
714	\bottomrule
715	\end{tabular}
716	\end{table}
717	
718	\section{RE $N{=}16$ Selection Analysis}\label{app:re_n16_selection}
719	
720	Table~\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.
721	All four consistency signals underperform single-sample, with EM showing the largest deficit ($\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).
722	LP is the only positive signal ($\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).
723	Even the most favorable seed captures only ${\sim}9\%$ of the 17.1~pp oracle headroom.
724	This cross-task consistency (LP as the only viable selection signal on both NER and RE) reinforces the persistent limitation of instance-level signals for candidate ranking across tested regimes.
725	
726	\begin{table}[t]
727	\centering
728	\small
729	\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\pm}\sigma$, $n{=}551$). Fisher combined $p$ vs.\ greedy. LP is the only signal with positive $\Delta$. $\sigma$ is population standard deviation over 3 seeds.}
730	\label{tab:re_n16_selection}
731	\begin{tabular}{lccc}
732	\toprule
733	Method & F1 & $\Delta$ (pp) & $p$(Fisher) \\
734	\midrule
735	Oracle & $.463{\pm}.006$ & $+$17.1 & --- \\
736	\midrule
737	LP & $\mathbf{.299}{\pm}.007$ & $+$0.7 & .058 \\
738	VC & $.284{\pm}.002$ & $-$0.8 & .973 \\
739	FK & $.283{\pm}.005$ & $-$0.9 & .985 \\
740	SJ & $.281{\pm}.005$ & $-$1.0 & .993 \\
741	EM & $.277{\pm}.007$ & $-$1.5 & .999 \\
742	\midrule
743	Greedy & $.291{\pm}.000$ & --- & --- \\
744	Random & $.262{\pm}.001$ & $-$2.9 & --- \\
745	\bottomrule
746	\end{tabular}
747	\end{table}
748	
749	\section{MBR Decoding and Task-Specific Interactions}\label{app:mbr_discussion}
750	
751	\paragraph{Connection to MBR decoding.}
752	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
753	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy, the core of the correlation-selection gap.
754	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs, consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
755	
756	\paragraph{Task-specific decoding interactions.}
757	The free-form ablation reveals divergent behavior across tasks.
758	On RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).
759	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
760	This interaction does not generalize to NER, where selection remains negligible under both regimes.
761	This ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.
762	The non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472: 87 instances newly gain LP discrimination while others lose it, and the newly non-tied subset shows a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
763	Despite this reshuffling, aggregate NER selection gains remain negligible. Score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
764	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
765	
766	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
767	
768	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).
769	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
770	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
771	RE LP selection consistently reverses direction under free-form decoding across 4 seeds: $+1.84{\pm}0.12$~pp (seeds 42/123/456/789: $+1.69$, $+1.76$, $+2.00$, $+1.91$~pp) vs.\ $-0.68$~pp constrained.
772	The constrained reference ($-0.68$~pp) uses the ablation-matched baseline; the primary experiment (Table~\ref{tab:selection}) yields $-0.9$~pp on the same gold-filtered set.
773	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
774	
775	\begin{table*}[t]
776	\centering
777	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\pm}0.12$~pp).}
778	\label{tab:freeform_ablation}
779	
780	\vspace{2pt}
781	{\small\textsc{Panel A: Logprob Distribution}}
782	\vspace{2pt}
783	
784	\begin{tabular}{lccc}
785	\toprule
786	Metric & Constrained & Free-form & $\Delta$ \\
787	\midrule
788	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
789	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
790	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
791	\bottomrule
792	\end{tabular}
793	
794	\vspace{8pt}
795	
796	{\small\textsc{Panel B: Selection F1}}
797	\vspace{2pt}
798	
799	\begin{tabular}{llccc}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41e084e2-3d1a-44b8-aea4-f75d56d5a54b",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "bf29942c-65b8-4598-8e19-59ed95bd9cf0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "Signal & Qwen & LLaMA & Qwen & LLaMA \\\\\n\\midrule\nSJ & 0.92 & 1.45 & 0.99 & 0.18 \\\\\nFK & 1.03 & 0.93 & 0.60 & 0.15 \\\\\nVC & 2.33 & 0.53 & 0.72 & 0.18 \\\\\nEM & 0.00 & 0.00 & 0.00 & 0.00 \\\\\nLP & 3.65 & 2.58 & 3.00 & 0.31 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset analysis.}\nTable~\\ref{tab:nontied_main} presents the non-tied subset analysis referenced in \\S\\ref{sec:discussion}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Non-tied subset analysis (SciERC, Qwen3-8B, $N{=}8$, $T{=}1.0$). Instances split at LP range $\\varepsilon{=}0.05$. Within-instance $\\rho$ and selection gain both concentrate in the non-tied subset. Full $\\varepsilon$ sweep in Table~\\ref{tab:epsilon_sweep}.}\n\\label{tab:nontied_main}\n\\begin{tabular}{lccc}\n\\toprule\nSubset & $n$ & $\\rho$(LP,F1) & LP $\\Delta$ vs.\\ greedy \\\\\n\\midrule\nTied (range ${<}0.05$) & 319 & 0.08 & ${\\approx}0$ \\\\\nNon-tied (range ${\\geq}0.05$) & 210 & 0.39 & $+$2.9~pp ($p{=}0.004$) \\\\\n\\midrule\nAll instances & 529 & 0.248 & $+$0.2~pp ($p{=}0.29$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Consistency-Stratified Selection Analysis}\\label{app:vc_quartile}\n\nTable~\\ref{tab:vc_quartile} stratifies SciERC instances by voting confidence (VC) quartiles and reports selection $\\Delta$ (gain over single-sample) for LP and SJ.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Selection $\\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}\n\\label{tab:vc_quartile}\n\\begin{tabular}{lcccc}\n\\toprule\nQuartile & Mean VC & LP $\\Delta$ & SJ $\\Delta$ & Oracle (pp) \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{NER}} \\\\\nQ1 (low) & 0.30 & $+$1.55 & $+$0.54 & 16.85 \\\\\nQ2 & 0.51 & $-$0.65 & $-$1.89 & 14.35 \\\\\nQ3 & 0.68 & $+$1.97 & $+$1.84 & 16.83 \\\\\nQ4 (high) & 0.92 & $-$0.41 & $-$0.04 & 4.78 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$^\\dagger$RE}} \\\\\nQ1 (low) & --- & $-$3.56 & --- & --- \\\\\nQ4 (high) & --- & $+$4.01 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe NER pattern reveals two complementary failure modes rather than a monotonic relationship between consistency and selection gain:\n\\begin{itemize}\n\\item \\textbf{Q4 ceiling effect.} High-consistency instances (mean VC${=}0.92$) have oracle headroom of only 4.78~pp. Samples have already converged, leaving little room for any signal to improve selection.\n\\item \\textbf{Q1--Q2 noise.} Low-consistency instances retain large headroom (14--17~pp) but LP rankings are unreliable, and LP rankings produce inconsistent $\\Delta$ signs across quartiles.\n\\end{itemize}\n\nOn $^\\dagger$RE, the pattern differs: Q4 LP achieves $+4.01$~pp; LP may recover selection ability when high consistency coincides with structured output diversity. This is a single-dataset observation and should be interpreted cautiously.\n\nOn CoNLL NER, Q3--Q4 instances have VC${=}1.0$ (all samples identical), and $\\Delta{=}0$ universally; this ceiling effect is even more extreme than SciERC Q4.\n\n\\section{Exploratory Extension to Relation Extraction}\\label{app:re_extension}\n\nWe extend the NER evaluation to relation extraction (RE) on SciERC as an exploratory single-benchmark analysis.\nRE produces sets of (head, relation, tail) triples with partial overlap; 40\\% of RE instances receive zero F1, and entity span errors account for 55.5\\% of RE false negatives, a prerequisite failure that consistency signals cannot detect (\\S\\ref{app:additional}).\nAll RE results use Qwen3-8B unless noted; single-seed ($\\text{seed}{=}42$) for $N{=}8$ analyses, 3-seed for $N{=}16$.\n\n\\paragraph{Quality estimation.}\nRE quality estimation is reported in Table~\\ref{tab:multiseed} (3-seed means).\nThe signal ranking differs from NER: VC leads ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM, a reversal reflecting RE's higher sensitivity to per-sample scoring.\nRE miscalibration is more severe than NER (ECE 0.109--0.339; Figure~\\ref{fig:reliability}).\n\n\\paragraph{Selection.}\nTable~\\ref{tab:re_cond_selection} presents RE selection at $N{=}8$: no signal outperforms single-sample (0.404) on the full set ($n{=}397$) or the non-zero subset ($n{=}238$), with 18.1~pp of unrealized oracle headroom.\nAt $N{=}16$ (Qwen3-4B, Table~\\ref{tab:re_n16_selection}), LP is the sole positive signal ($\\Delta{=}{+}0.7$~pp, $p{=}0.058$), consistent with LP being the strongest RE selection signal across scales.\n\n\\paragraph{Scale ablation.}\nAt 4B scale (Qwen3-4B, $N{=}8$, $\\text{seed}{=}42$), RE quality estimation shows FK $\\rho{=}0.359$ and LP $\\rho{=}0.351$, both above their 8B counterparts (FK 0.275, LP 0.266), while SJ declines ($0.267$ vs.\\ $0.250$).\nSelection remains below single-sample on RE ($\\Delta$ up to $-3.4$~pp) despite 17.1~pp of oracle headroom.\n\n\\paragraph{Free-form decoding.}\nRE LP selection consistently reverses direction under free-form decoding ($+1.8{\\pm}0.1$~pp across 4 seeds vs.\\ $-0.9$~pp under constrained decoding at 8B; \\S\\ref{app:freeform_ablation}); constrained decoding's fixed template likely obscures LP signal in RE (\\S\\ref{app:mbr_discussion}).\n\n\\section{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform single-sample on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\\ $-4.5$~pp on full set), because single-sample is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLP & 0.395 & 0.600 \\\\\nSJ & 0.386 & 0.604 \\\\\nEM & 0.372 & 0.583 \\\\\nVC & 0.359 & 0.574 \\\\\n\\midrule\nGreedy & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{RE $N{=}16$ Selection Analysis}\\label{app:re_n16_selection}\n\nTable~\\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.\nAll four consistency signals underperform single-sample, with EM showing the largest deficit ($\\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).\nLP is the only positive signal ($\\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).\nEven the most favorable seed captures only ${\\sim}9\\%$ of the 17.1~pp oracle headroom.\nThis cross-task consistency (LP as the only viable selection signal on both NER and RE) reinforces the persistent limitation of instance-level signals for candidate ranking across tested regimes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\\pm}\\sigma$, $n{=}551$). Fisher combined $p$ vs.\\ greedy. LP is the only signal with positive $\\Delta$. $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:re_n16_selection}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & F1 & $\\Delta$ (pp) & $p$(Fisher) \\\\\n\\midrule\nOracle & $.463{\\pm}.006$ & $+$17.1 & --- \\\\\n\\midrule\nLP & $\\mathbf{.299}{\\pm}.007$ & $+$0.7 & .058 \\\\\nVC & $.284{\\pm}.002$ & $-$0.8 & .973 \\\\\nFK & $.283{\\pm}.005$ & $-$0.9 & .985 \\\\\nSJ & $.281{\\pm}.005$ & $-$1.0 & .993 \\\\\nEM & $.277{\\pm}.007$ & $-$1.5 & .999 \\\\\n\\midrule\nGreedy & $.291{\\pm}.000$ & --- & --- \\\\\nRandom & $.262{\\pm}.001$ & $-$2.9 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{MBR Decoding and Task-Specific Interactions}\\label{app:mbr_discussion}\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy, the core of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs, consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Task-specific decoding interactions.}\nThe free-form ablation reveals divergent behavior across tasks.\nOn RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).\nThe win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).\nThis interaction does not generalize to NER, where selection remains negligible under both regimes.\nThis ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.\nThe non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472: 87 instances newly gain LP discrimination while others lose it, and the newly non-tied subset shows a $3{\\times}$ increase in within-instance LP range for the newly non-tied subset.\nDespite this reshuffling, aggregate NER selection gains remain negligible. Score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.\nFree-form decoding also slightly improves quality estimation (NER VC $\\rho$: 0.379$\\to$0.409), though this does not translate to selection gains.\n\n\\section{Free-Form Decoding Ablation}\\label{app:freeform_ablation}\n\nTable~\\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).\nFree-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\\%, 4406/4408).\nLP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\\times}$), and NER selection gains remain negligible under both regimes (Panel~B).\nRE LP selection consistently reverses direction under free-form decoding across 4 seeds: $+1.84{\\pm}0.12$~pp (seeds 42/123/456/789: $+1.69$, $+1.76$, $+2.00$, $+1.91$~pp) vs.\\ $-0.68$~pp constrained.\nThe constrained reference ($-0.68$~pp) uses the ablation-matched baseline; the primary experiment (Table~\\ref{tab:selection}) yields $-0.9$~pp on the same gold-filtered set.\nQuality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\\pm}0.12$~pp).}\n\\label{tab:freeform_ablation}\n\n\\vspace{2pt}\n{\\small\\textsc{Panel A: Logprob Distribution}}\n\\vspace{2pt}\n\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\nMean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\\\\nMean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\\\\nTied fraction ($\\varepsilon{=}0.05$) & 59.7\\% & 57.7\\% & $-$2.0\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel B: Selection F1}}\n\\vspace{2pt}\n\n\\begin{tabular}{llccc}",
      "numLines": 200,
      "startLine": 600,
      "totalLines": 1354
    }
  },
  "sourceToolAssistantUUID": "41e084e2-3d1a-44b8-aea4-f75d56d5a54b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 115 · 2026-05-18T05:59:35.018Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read enough of the paper to form a thorough review. Let me compile my findings and write the review. Let me also look at the remaining appendix sections briefly for completeness.

Key observations so far:

**Reference verification**: 
- 60 entries, 0 orphan, 0 missing, 53 verified, 3 not found (likely too recent for OpenAlex), 4 mismatch (minor)

**Writing quality**:
- No em-dash (—) or en-dash (–) issues
- `\textendash` used only for number ranges (4B–8B, 14–59%), which is acceptable


- No blacklist words present, no repetitive transition patterns, and the -ing phrases used feel natural rather than formulaic

Now I'm assessing the novelty. Yao et al. (2026) showed that consistency correlates with accuracy for NER and RE tasks on hard-prompted LLMs, but this paper distinguishes itself by investigating why that correlation fails to translate into effective selection—a meaningful difference, though the comparison requires careful framing since Yao uses hard prompting while this work focuses on fine-tuned models. The core contribution around correlation-selection gaps needs...

The "correlation-selection gap" concept itself isn't entirely new—MBR decoding already demonstrates scenarios where correlation doesn't guarantee selection performance—but applying this diagnosis specifically to structured IE through the lens of degeneracy and weak alignment has some novelty value. The first methodological contribution is somewhat circular: four of five signals are instance-level by design, so they inherently can't rank candidates across the board, which reads more as a definitional observation than an experimental finding. The paper's strength lies in its diagnostic approach, though the positive results are modest (LP gains 1.36pp on Few-NERD) while most other findings are negative, raising questions about whether the diagnostic value alone justifies publication at a top venue.

The related work section is solid with 60 references and good coverage of MBR literature.

Now I'm assessing the paper's structure and formatting—the abstract is quite dense at 178 words with eight quantitative values, the introduction follows a standard five-paragraph structure but the contributions section is packed, and the discussion spans seven paragraphs covering disparate topics which might benefit from tighter organization. The submission appears to meet ACL formatting requirements with an ethics statement included, and the body text around 4600 words should fit within the page limit given the tables and figures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf29942c-65b8-4598-8e19-59ed95bd9cf0",
  "isSidechain": false,
  "requestId": "req_011Cb9XFxZ6MUPTBxoiG1kzE",
  "type": "assistant",
  "uuid": "0b57a202-8ab3-4806-8f3a-3cc8a25e9a48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U251UgzeYXHGtudCYoZeoP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5132,
      "cache_read_input_tokens": 92399,
      "output_tokens": 855,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 855,
          "cache_read_input_tokens": 92399,
          "cache_creation_input_tokens": 5132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5132
          },
          "type": "message"
        }
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

_source line 116 · 2026-05-18T05:59:35.021Z_

论文已全部通读。现在编写完整审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b57a202-8ab3-4806-8f3a-3cc8a25e9a48",
  "isSidechain": false,
  "requestId": "req_011Cb9XFxZ6MUPTBxoiG1kzE",
  "type": "assistant",
  "uuid": "84dcdf16-a28d-48fe-981f-fa837b68c8fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U251UgzeYXHGtudCYoZeoP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5132,
      "cache_read_input_tokens": 92399,
      "output_tokens": 855,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 855,
          "cache_read_input_tokens": 92399,
          "cache_creation_input_tokens": 5132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5132
          },
          "type": "message"
        }
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

_source line 117 · 2026-05-18T05:59:35.032Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MwrfU7gEEjFL1FWiyTxvgi`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidance about what constitutes reasons to accept/reject a paper, how to evaluate novelty, how to handle negative results papers, and any specific guidance about diagnostic/analysis papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84dcdf16-a28d-48fe-981f-fa837b68c8fa",
  "isSidechain": false,
  "requestId": "req_011Cb9XFxZ6MUPTBxoiG1kzE",
  "type": "assistant",
  "uuid": "d4bbbc34-be3f-41b6-a8ff-f3edb498b2d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U251UgzeYXHGtudCYoZeoP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5132,
      "cache_read_input_tokens": 92399,
      "output_tokens": 855,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 855,
          "cache_read_input_tokens": 92399,
          "cache_creation_input_tokens": 5132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5132
          },
          "type": "message"
        }
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

_source line 118_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）  ### 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction - **路径**: `projects…",
  "leafUuid": "d4bbbc34-be3f-41b6-a8ff-f3edb498b2d1",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Runtime record

_source line 119_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured IE paper for EMNLP 2026",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Tool result

_source line 120 · 2026-05-18T05:59:41.774Z_

<details><summary>↩ Tool result · `toolu_01MwrfU7gEEjFL1FWiyTxvgi`</summary>

```text
# Key Reviewer Guidance on Paper Evaluation

## Reasons to Accept/Reject

The guidelines emphasize that **soundness is necessary but not sufficient**. Papers should be rejected only when they have genuine flaws, not for subjective preferences. The document explicitly warns against common problematic rejection rationales:

- "The results are not surprising" (H1) - findings may seem obvious retroactively but represent novel empirical contributions
- "The results are not SOTA" (H5) - achieving state-of-the-art is "neither necessary nor sufficient for a scientific contribution"
- "This method is too simple" (H7) - simpler solutions are preferable as they're "less brittle and easier to deploy"

Papers merit acceptance when they demonstrate technical soundness and make appropriate contributions to their claimed scope, even if reviewers personally lack enthusiasm.

## Evaluating Novelty

The guidance distinguishes between contribution types. Novelty isn't limited to methodological innovation—the field should encourage "reimplementations and systematic analyses of prior work." However, if authors claim novelty, reviewers must verify by providing specific references to prior work (H3). The three-month publication threshold applies: prior work must be officially published, not merely preprinted.

## Negative Results Papers

The guidelines explicitly support negative results: "The bias towards publishing only positive results is a known problem in many fields...if something systematically does not work where it could be expected to, the community does need to know about it" (H6).

## Analysis/Diagnostic Papers

These papers receive particular protection in the guidelines. Resource papers, reproduction studies, and analyses represent "proper contributions in scope of ARR" when appropriately presented, countering reviewer dismissal of non-modeling work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4bbbc34-be3f-41b6-a8ff-f3edb498b2d1",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "c2ae635e-3af8-4f7f-a815-89a6da05d80f",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# Key Reviewer Guidance on Paper Evaluation\n\n## Reasons to Accept/Reject\n\nThe guidelines emphasize that **soundness is necessary but not sufficient**. Papers should be rejected only when they have genuine flaws, not for subjective preferences. The document explicitly warns against common problematic rejection rationales:\n\n- \"The results are not surprising\" (H1) - findings may seem obvious retroactively but represent novel empirical contributions\n- \"The results are not SOTA\" (H5) - achieving state-of-the-art is \"neither necessary nor sufficient for a scientific contribution\"\n- \"This method is too simple\" (H7) - simpler solutions are preferable as they're \"less brittle and easier to deploy\"\n\nPapers merit acceptance when they demonstrate technical soundness and make appropriate contributions to their claimed scope, even if reviewers personally lack enthusiasm.\n\n## Evaluating Novelty\n\nThe guidance distinguishes between contribution types. Novelty isn't limited to methodological innovation—the field should encourage \"reimplementations and systematic analyses of prior work.\" However, if authors claim novelty, reviewers must verify by providing specific references to prior work (H3). The three-month publication threshold applies: prior work must be officially published, not merely preprinted.\n\n## Negative Results Papers\n\nThe guidelines explicitly support negative results: \"The bias towards publishing only positive results is a known problem in many fields...if something systematically does not work where it could be expected to, the community does need to know about it\" (H6).\n\n## Analysis/Diagnostic Papers\n\nThese papers receive particular protection in the guidelines. Resource papers, reproduction studies, and analyses represent \"proper contributions in scope of ARR\" when appropriately presented, countering reviewer dismissal of non-modeling work.",
    "durationMs": 6736,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "d4bbbc34-be3f-41b6-a8ff-f3edb498b2d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 121 · 2026-05-18T06:00:14.408Z_

<details><summary>Logged reasoning block</summary>

```text
This is very relevant. ARR explicitly supports negative results papers and diagnostic/analysis papers. The guidelines say:
- "Negative results: if something systematically does not work where it could be expected to, the community does need to know about it"
- Analysis papers are "proper contributions in scope of ARR"
- "The results are not surprising" is listed as a problematic rejection rationale

This is important context for my review. Now let me finalize the review.

Let me think through the major points:

**Strengths:**
1. Thorough experimental design with well-designed controls (4 datasets spanning difficulty gradient, 2 model families, 4B ablation)


2. Clear separation of quality estimation vs. selection — important methodological contribution
3. Statistical rigor (bootstrap CIs, TOST equivalence testing, MDE calculation, Bonferroni correction)
4. Extensive ablations (temperature, N-scaling, LoRA rank, free-form decoding, entity-token LP, supervised verifier)
5. Massive appendix demonstrating thoroughness

**Weaknesses:**
1. [Must-Fix] Contribution 1 "methodological premise" — the observation that 4/5 signals are instance-level by construction is definitional, not experimental. Claiming this as a contribution inflates the contribution list.
2. [Must-Fix] The paper needs to address a critical issue with how it frames its findings.
3. [Should-Fix] Abstract is very dense with 8+ quantitative values in 178 words. Reads like a results summary rather than a narrative abstract.
4. [Should-Fix] Discussion section has 7 paragraph-level subtopics — too fragmented for the space. Some should be consolidated or moved to appendix.
5. [Should-Fix] The paper doesn't build a verifier (the obvious next step) — acknowledged in limitations but this significantly limits the contribution. The paper diagnoses the problem but stops short of proposing a solution.
6. [Should-Fix] Positioning relative to Yao et al. (2026) needs clarification on what truly distinguishes this work.
7. [Minor] `\textendash` used correctly for ranges but excessively throughout — same numbers (14–59%) appear in abstract, introduction, and conclusion.
8. [Minor] Repetition of core findings across sections — the same numbers appear verbatim in abstract, introduction, experiments, discussion, and conclusion.

Now I'm reconsidering the novelty angle. The correlation-selection gap isn't entirely new — prior work like Eikema & Aziz (2022) and Müller & Sennrich (2021) already established that MBR utility choice matters and that MBR doesn't always improve. More recent work from Eikema et al. (2025) specifically found MBR utilities degrade on structured outputs, so the core observation here feels somewhat incremental.

What does feel novel is the specific application to NER with set-valued outputs, the identification of two independent mechanisms (degeneracy and weak alignment), and the empirical demonstration that both are necessary conditions. Instance degeneracy itself is somewhat expected given that fine-tuning collapses diversity, but the paper's real value lies in its diagnostic clarity — separating quality estimation from selection issues and providing actionable guidelines. That's a solid empirical contribution under ARR standards, though the main weakness is that the "what to do about it" part feels incomplete.

Looking at this holistically, I'm settling on a borderline rating. The experimental rigor is genuinely impressive and the problem matters, but the core insight about correlation-selection gaps has precedent in the MBR literature, and the practical impact is limited by the negative results. I'd score this around 3/5 overall — solid methodological work with useful diagnostics, but incremental novelty and constrained actionability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2ae635e-3af8-4f7f-a815-89a6da05d80f",
  "isSidechain": false,
  "requestId": "req_011Cb9XJVGbZwujnH7JEr1UM",
  "type": "assistant",
  "uuid": "5af8ee99-8b8f-40b0-b29d-8350f6eb37ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ENQTtjvGcC8EK35EA1pvbi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1243,
      "cache_read_input_tokens": 97531,
      "output_tokens": 7373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7373,
          "cache_read_input_tokens": 97531,
          "cache_creation_input_tokens": 1243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1243
          },
          "type": "message"
        }
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

_source line 122 · 2026-05-18T06:00:14.663Z_

审稿意见已准备好，现在提交给 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5af8ee99-8b8f-40b0-b29d-8350f6eb37ee",
  "isSidechain": false,
  "requestId": "req_011Cb9XJVGbZwujnH7JEr1UM",
  "type": "assistant",
  "uuid": "8f80d98a-3fac-45bd-b782-b0ccc26cc42a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ENQTtjvGcC8EK35EA1pvbi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1243,
      "cache_read_input_tokens": 97531,
      "output_tokens": 7373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7373,
          "cache_read_input_tokens": 97531,
          "cache_creation_input_tokens": 1243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1243
          },
          "type": "message"
        }
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

_source line 123 · 2026-05-18T06:02:30.565Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01A6yrR3SCUSYpZcqiYcHDBa`</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见 — Round 1\n\n**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\n**审查侧重**: 新颖性 + 完整性 + 写作质量 + 格式合规\n\n---\n\n## 1. Summary\n\n本文评估五种置信度信号（四种 instance-level，一种 per-sample LP）在 LLM-based NER 中的质量估计（QE）和样本选择（selection）效果，横跨四个 benchmark、两个模型家族和一个 4B ablation。核心发现是：所有信号均可进行可靠的 QE（ρ 最高 0.45，AUROC 最高 0.82），但仅 LP 在 Few-NERD 上实现了显著的选择增益（+1.36pp），且需要两个条件同时满足（低 instance degeneracy 和足够的 LP-quality alignment）。作者将 QE 强度与选择失败之间的落差命名为 \"correlation-selection gap\"，并诊断出两个阻断机制。\n\n---\n\n## 2. Strengths\n\n**S1. 实验设计严谨且系统化。** 四个数据集构成 difficulty gradient（ceiling → medium → low-degeneracy → collapse boundary），每个数据集有明确的诊断角色。两个模型家族 + 4B ablation 增强了泛化性。QE 和 selection 的分离是一个重要的方法论贡献。\n\n**S2. 统计方法论远超同类工作。** Bootstrap CIs（Table 9）、TOST equivalence testing（Appendix）、MDE 计算（n=529 对应 ~1.5pp）、Bonferroni correction、Fisher combined p-values、external equivalence margins（Ratinov 2009, Berg-Kirkpatrick 2012）——这些构成了一个罕见的完整统计分析框架。\n\n**S3. 消融实验全面且可信。** Temperature ablation（隔离 diversity 和 capacity）、LoRA-rank ablation（conflated 但有 secondary evidence 价值）、free-form decoding ablation（排除 constrained decoding 作为 NER LP compression 的唯一原因）、entity-token LP（排除 token averaging 作为唯一机制）、supervised verifier baseline（排除信号组合策略）——每个 ablation 都有明确的诊断目的。\n\n**S4. Appendix 的深度令人印象深刻。** 1353 行 appendix 覆盖了几乎所有可预见的审稿人质疑：FK 独立性检验、SJ normalizer 鲁棒性、ε 灵敏度分析、epoch confound、thinking token 分析、OOD、calibration baseline 等。这是负责任的学术写作。\n\n**S5. 引用完整且无 orphan/missing 条目。** verify_references 确认 60 条 bib entry 全部被引用，0 orphan、0 missing。在线验证 53/60 confirmed，3 条 not_found（均为最近 arXiv preprint，尚未被 OpenAlex 索引），4 条 minor mismatch（作者名格式差异）。\n\n**S6. 写作质量优秀，AI 痕迹极少。** 无 em-dash/en-dash 解释性使用（`\\textendash` 仅用于数字范围），无黑名单用词（delve/leverage/utilize/facilitate/myriad/plethora），无 Furthermore/Moreover/Additionally 堆砌，无过度分段。\n\n---\n\n## 3. Weaknesses\n\n### Must-Fix\n\n**N1 [critical] Contribution 1 中 \"methodological premise\" 的贡献定位不当**\n- 具体位置：Section 1, Contribution 1; Section 2 (§2.1); Abstract line 8\n- 问题：\"A definitional observation structures the analysis: four of five signals are instance-level aggregates that by design assign identical scores to all candidates\" 是一个定义推论，不是实验发现。Instance-level signal 无法区分 per-sample candidates 是信号定义的直接推论——任何理解 MBR decoding 的读者都能从定义推导出这一点。将此列为 Contribution 1 的一部分（与 \"Quality estimation framework\" 并列）inflates 了贡献清单。\n- 为什么影响接收：审稿人（特别是熟悉 MBR/uncertainty 的审稿人）可能将此视为 trivial observation 被 overclaimed，进而质疑整篇论文的 novelty bar。\n- 建议修改方向：将其降级为 Method section 的 framing observation（目前已经是），从 Contribution 列表中移除或明确标注为 \"definitional premise that structures our analysis\" 而非 contribution。Contribution 1 可以聚焦于 \"five-signal QE framework across 4 benchmarks and 2 model families\" 本身。\n\n**N2 [critical] \"Correlation-selection gap\" 的新颖性需要更锐利的差异化定位**\n- 具体位置：Section 1 (term coined), Section 3 (§3.3), Section 5\n- 问题：MBR decoding 文献已经建立了 utility function 选择不当导致选择失败的先例。Eikema et al. (2025)（论文已引用）明确发现 MBR utilities degrade on structured outputs。Müller & Sennrich (2021) 讨论了 MBR 的 properties 和 limitations。论文引用了这些工作但差异化定位不够锐利——读者可能会问：\"这和 Eikema et al. (2025) 发现的 'utility degradation on structured outputs' 有什么本质区别？\"\n- 为什么影响接收：如果审稿人认为核心概念是已知结论的 domain-specific 重述，novelty 评分将严重受损。\n- 建议修改方向：在 Introduction 或 Related Work 中增加一段明确的对比：\"Eikema et al. (2025) attribute MBR failure to utility misalignment; our diagnosis is complementary but distinct: on non-degenerate instances, SJ utility is well-aligned with F1 (median ρ=0.524, Table X), yet selection still fails because instance degeneracy eliminates headroom. The bottleneck is not the utility function but the input distribution.\"（论文在 §2.3 line 18 已经有类似表述，但过于简略——应该更加突出这一差异，因为这是论文最关键的 novelty claim。）\n\n### Should-Fix\n\n**W1 [warning] Abstract 数字过载，叙事被压缩**\n- 具体位置：Abstract (178 words, 8+ quantitative values)\n- 问题：Abstract 包含 ρ up to 0.45、AUROC up to 0.82、+1.36pp、p<0.001、ρ ≳ 0.3、14–59%、~13pp 等至少 8 个定量值。30 秒内审稿人无法消化这些数字。关键叙事（\"为什么 QE 强但 selection 弱\"）被数字堆积淹没。\n- 建议：保留 3 个以内关键数字（如 ρ up to 0.45 for QE、+1.36pp for LP selection、14–59% degeneracy），其余用 qualitative language 替代。\n\n**W2 [warning] 论文的 actionable contribution 偏薄**\n- 具体位置：Section 5 \"Practical guidelines\"; Limitations\n- 问题：论文的主要积极发现是 LP 在 Few-NERD 上 +1.36pp（~1.8% relative improvement），且需要两个特定条件（degeneracy <15%, ρ ≳ 0.3）。对于不满足条件的场景（SciERC, CoNLL, WNUT），actionable advice 是 \"use greedy decoding\"——这等于告诉 practitioner 回到原点。论文诊断了问题但没有提出解决方案。acknowledged in Limitations (line 3: \"We do not train a verifier\")，但这显著降低了 practical impact。\n- 建议：（a）在 Discussion 中增加一段 \"toward closing the gap\" 的 forward-looking analysis，超越简单引用 Cobbe et al.——例如讨论 hidden state verifiers 的可行性，或 entity embedding 作为 per-sample signal 的初步分析；（b）明确 Few-NERD +1.36pp 在实际部署中的意义（是否超过 inference cost 的代价？8 次采样的 latency/cost overhead 是多少？）。\n\n**W3 [warning] Discussion section 过于碎片化**\n- 具体位置：Section 5 (7 个 \\paragraph)\n- 问题：Discussion 包含 7 个独立的 paragraph topic（practitioners, why gap exists, non-tied subset, LP compression, regime boundaries, practical guidelines, methodological implications）。每个 topic 只有 1 段，无法深入展开。\"Practical guidelines\" 段特别长（单段 ~180 words），包含 temperature curve、epoch confound、calibration 等多个子话题，读起来像压缩过的 laundry list。\n- 建议：合并 \"Implications for practitioners\" 和 \"Practical guidelines\" 为一个 subsection；合并 \"Why the gap exists\" 和 \"LP compression mechanisms\" 为一个 subsection；将 \"Regime boundaries\" 的部分内容移入 Experiments。\n\n**W4 [warning] 纯诊断性论文（几乎全部 negative results）对 EMNLP main conference 的门槛**\n- 具体位置：全文\n- 问题：ARR reviewer guidelines 明确支持 negative results papers（\"if something systematically does not work where it could be expected to, the community does need to know about it\"），但论文需要确保诊断价值足够高。目前论文的核心信息可以用一句话概括：\"Instance-level signals can't rank candidates by definition, and LP is too compressed to do so in practice unless degeneracy is low and alignment is adequate.\" 这一诊断是否足够 surprising 来支撑 8 页正文 + 大量 appendix？\n- 建议：论文应该在 Introduction 中更明确地 argue 为什么这个诊断是 non-trivial（不仅仅是 \"the community needs to know\"，而是 \"this changes how we think about test-time scaling for structured tasks\"），并且展示现有文献中的 implicit assumption（structured IE 应该受益于 self-consistency）被系统性 falsified。\n\n**W5 [warning] 核心发现的重复性过高**\n- 具体位置：Abstract, Introduction (§1 lines 11-15, Contribution 2-3), Experiments (§4.3, §4.4), Discussion (§5 para 1-2), Conclusion\n- 问题：\"14–59% degeneracy\", \"+1.36pp on Few-NERD\", \"ρ up to 0.45\", \"AUROC up to 0.82\" 等数字在 abstract、introduction、experiments、discussion、conclusion 中几乎逐字重复。这种程度的 recapitulation 浪费了宝贵的正文空间，且给审稿人留下 \"padding\" 的印象。\n- 建议：Abstract 和 Conclusion 可以保留具体数字；Introduction 的 contribution list 引用 section/table 即可，不需要重复完整数字；Discussion 重点解释 mechanism 而非重述 results。\n\n**W6 [warning] Few-NERD 训练设置差异引入混淆**\n- 具体位置：Section 4.1 line 15; Appendix (epoch confound)\n- 问题：Few-NERD 使用 3 epochs（其他数据集 5 epochs），这是论文中唯一正面结果的来源。虽然 Appendix 提供了 5-epoch control（\"LP selection remains positive though gains are halved\"），但这恰恰证明 epoch 是一个关键 confound。3 epochs → 低 degeneracy → LP selection 有效；5 epochs → 高 degeneracy → LP gains halved。那么 Few-NERD 的成功究竟是 dataset property 还是 training artifact？\n- 建议：在正文中更显著地讨论这一 confound（目前只在 Appendix），并考虑在 SciERC 上使用 3-epoch checkpoint 进行 selection 实验（Appendix 的 3-point curve 只报告了 degeneracy 和 alignment，没有报告 selection F1）。\n\n### Minor\n\n**M1** `\\textendash` 使用正确（仅用于数字范围如 4B–8B, 14–59%），但相同范围在多处重复（Abstract, Introduction, Conclusion 均出现 \"14\\textendash 59\\%\"），属于上述重复问题的子集。\n\n**M2** Table 3 (§4.4) caption 中有两个 `\\footnotemark`，对应的 `\\footnotetext` 紧随表格之后。这种 split footnote 在 ACL 格式中技术上可行但不优雅，且第二个 footnote 的编号可能在编译时出错。建议改为表格 caption 内的 parenthetical note。\n\n**M3** Conclusion 最后两句 (\"Whether these patterns persist at 70B+ scales remains open.\" 和 \"Closing the gap...\") 结构松散。\"Whether...remains open\" 在 Limitations 中已说过，Conclusion 的最后一句应该是 forward-looking statement 而非重复 limitation。\n\n**M4** Ethics Statement (main.tex lines 40-44) 较为单薄（4 句），特别是 \"Code and data will be released upon acceptance at [anonymized URL]\" 这种 boilerplate。建议增加一句关于 potential misuse（如 practitioners 可能 overrely on QE signals for deployment gating without understanding selection limitations）的讨论。\n\n**M5** Table 1 (quality estimation) 只报告 SciERC 和 CoNLL 两个数据集的结果，Few-NERD 和 WNUT-17 的结果分散在正文和 Appendix 中。建议在 Table 1 中增加 Few-NERD 列，因为它是 selection 成功的关键数据集。\n\n---\n\n## 4. Questions\n\n**Q1.** SciERC 3-epoch checkpoint（Table appendix epoch_scierc）的 degeneracy 为 6.4%，alignment ρ=0.317。这已经接近 Few-NERD 的 degeneracy 水平（13.8%），且 alignment 高于论文提出的 ρ ≳ 0.3 threshold。那么 SciERC 3-epoch 的 selection F1 是多少？如果 selection 仍然为 negative，那么 \"two jointly necessary conditions\" 的 claim 就需要修正（可能需要更高的 alignment threshold，或存在第三个 factor）。\n\n**Q2.** 论文使用 macro F1 作为 evaluation metric（Table 2 caption \"macro F1\"），但 SciERC 有 6 个 entity types，Few-NERD 有 8 个。不同 entity types 之间的 F1 variance 可能很大。是否分析过 per-type LP selection 的 heterogeneity 在 SciERC 上的表现（Few-NERD 的 per-type 分析已在 Appendix 中）？\n\n**Q3.** Supervised verifier baseline（§4.5 line 172-175）使用 logistic regression/MLP/random forest 但仅以 5 个 unsupervised signals 作为特征。这不是公平的 verifier baseline——真正的 verifier（如 Cobbe et al.）使用 hidden states 或 full output representations。论文已在 limitations 中承认，但 \"supervised verifier baseline\" 这一名称可能误导读者认为已经测试了 learned verifier 的上限。建议更名为 \"supervised signal combination\" 或 \"meta-learner over unsupervised signals\"。\n\n**Q4.** Per-entity-type analysis within Few-NERD 报告 ρ=-0.881, p=0.004, n=8。但论文也承认 \"entity types share model, tokenizer, and temperature, so effective degrees of freedom may be lower than 6\"。如果 effective df < 6，那么 p=0.004 可能不可靠。是否有 permutation test 或 bootstrap 来验证？\n\n---\n\n## 5. Missing References\n\n引用覆盖度总体良好（60 条），但以下方向可能有遗漏：\n\n- **Structured prediction diversity**: Ippolito et al. (2019) \"Comparison of Diverse Decoding Methods from Conditional Language Models\" — 讨论了 structured output 多样性问题，与 degeneracy 诊断直接相关。\n- **Confidence estimation for sequence labeling**: Fomicheva et al. (2020) 已引用，但 Xiao & Wang (2021) \"On Hallucination and Predictive Uncertainty in Conditional Language Generation\" 讨论了 generation uncertainty 与 quality 的关系。\n- **Sample efficiency in best-of-N**: Li et al. (2024) \"Rain: Your Language Models Can Align Themselves without Finetuning\" 中的 self-evaluation 机制可能与 LP-as-selector 的讨论相关。\n\n以上均为 suggestion，不构成 must-cite。\n\n---\n\n## 6. 格式合规检查\n\n| 检查项 | 状态 | 备注 |\n|--------|------|------|\n| ACL style template | ✓ | `\\usepackage[review]{acl}` |\n| 匿名化 | ✓ | `\\author{Anonymous}`，无 URL 泄漏 |\n| 行号 | ✓ | review mode 启用 |\n| 页数 | △ | 无编译 PDF 可供验证；正文 ~4600 words + 3 tables + 2 figures，估计 7-8 页，应在限制内 |\n| Limitations | ✓ | 充实，14 行，覆盖 scale、verifier、seed、epoch 等 |\n| Ethics Statement | ⚠ | 较薄（4 句），见 M4 |\n| References 格式 | ✓ | `\\bibliography{references}` 正确引用 |\n| 图表 caption | ✓ | 自包含，Table 2/3 有完整的实验设置描述 |\n| 小数精度 | ✓ | Table 1 统一 3 位小数 |\n| 最优加粗 | ✓ | Table 1, 2, 3 均有 bold 标注 |\n\n---\n\n## 7. Overall Assessment\n\n### 官方维度打分（ACL Rolling Review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论严谨，统计分析全面。但 \"two necessary conditions\" 的 claim 基于 3 个数据集的 observational evidence + 单个 per-type analysis（n=8，df 存疑），causal claim 的支撑偏弱。Temperature ablation 是最强证据，但只在 SciERC 上进行。 |\n| Excitement | 2.5/5 | 诊断价值真实存在，但核心发现的 surprise factor 有限：instance-level signals 无法 rank candidates 是 definitional，LP compression 在 fine-tuned models 上是可预期的。Positive finding（+1.36pp）较小且 dataset-specific。 |\n| Overall | 3/5 | Borderline。实验执行优秀（top 10% thoroughness），但 novelty 和 practical impact 均处于 borderline 水平。作为 Findings 论文完全合格，作为 main conference 论文需要更锐利的 novelty framing 和至少一个 stronger positive contribution。 |\n| Reproducibility | 4/5 | 训练配置完整（Table appendix training），prompt template 给出，vLLM + constrained decoding 细节充分。Code release promised。唯一减分：2 seeds（非 3）for primary selection results。 |\n| Confidence | 4/5 | 熟悉 self-consistency、MBR decoding、NER evaluation 和 uncertainty estimation 文献。仔细阅读了正文和 ~60% appendix。 |\n\n### 总体评分\n\n**Overall**: 3/5 (Borderline — Findings acceptance, borderline for main conference)\n\n**一句话总结**: 实验设计和统计分析堪称 exemplary，但核心诊断的新颖性受限于 MBR 文献中的已有结论，且唯一的正面发现（LP +1.36pp on Few-NERD）过小且 dataset-specific，难以支撑 main conference 的 excitement bar。\n\n### 接收建议\n\n如果作者能：(1) 锐化与 Eikema et al. (2025) 的差异化定位，(2) 在 SciERC 3-epoch checkpoint 上报告 selection F1 以验证 \"two necessary conditions\" claim，(3) 精简重复内容并加强 forward-looking discussion，则有望升至 weak accept。当前状态下建议 Findings track。\n",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f80d98a-3fac-45bd-b782-b0ccc26cc42a",
  "isSidechain": false,
  "requestId": "req_011Cb9XJVGbZwujnH7JEr1UM",
  "type": "assistant",
  "uuid": "aa1d1c45-3ed1-4ab0-8c60-a4d4e2db782f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ENQTtjvGcC8EK35EA1pvbi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1243,
      "cache_read_input_tokens": 97531,
      "output_tokens": 7373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7373,
          "cache_read_input_tokens": 97531,
          "cache_creation_input_tokens": 1243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1243
          },
          "type": "message"
        }
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

_source line 124_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）  ### 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction - **路径**: `projects…",
  "leafUuid": "aa1d1c45-3ed1-4ab0-8c60-a4d4e2db782f",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Runtime record

_source line 125_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured IE paper for EMNLP 2026",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13"
}
```

---

### Tool result

_source line 126 · 2026-05-18T06:02:35.868Z_

<details><summary>↩ Tool result · `toolu_01A6yrR3SCUSYpZcqiYcHDBa`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa1d1c45-3ed1-4ab0-8c60-a4d4e2db782f",
  "isSidechain": false,
  "promptId": "7e6eefcf-2c2f-4283-b3f0-334cc9cf9d89",
  "type": "user",
  "uuid": "cd278a5a-be51-4406-8a8c-10ac509e0995",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "aa1d1c45-3ed1-4ab0-8c60-a4d4e2db782f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "4d69282c-32b0-4839-ba8f-96c846d16f13",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
