# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2 **你的审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 呈现** ### Venue 信息 - **目标**: EMNLP 2026 Main 

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 127
- **Recorded user turns:** 3
- **Tool calls:** 34
- **Original source:** `logs/chats/exported-trajectories/account-3/e427ec35-e53e-4958-bb7f-c7a35811281b.jsonl`
- **Structured JSON:** [`7322c7cf524558b010ee.json`](../../sessions/73/7322c7cf524558b010ee.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T04:18:45.034Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T04:18:45.034Z",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "content": "[Round 1 审稿请求]:\n## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 呈现**\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数**: 长文 8 页 + 无限参考文献 + 附录不计入页数\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n- **附录规则**: 附录在 references 之后，审稿人可选择性参考但不应要求内容必须移至附录\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`\n（各章节在 `sections/` 子目录下：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex）\n引用文件：`references.bib`\n\n### 论文概要\n论文评估 5 种置信度信号（Soft Jaccard, Voting Confidence, Exact Match, Fleiss' κ, Log-probability）在 LLM-based structured IE（NER + RE）中的 quality estimation 和 sample selection 能力。核心发现是 \"correlation-selection gap\"：信号能预测质量但无法改善 best-of-N 选择。3 个贡献：(1) metric dissociation (QE vs selection), (2) LP compression 和 MBR failure, (3) difficulty-dependent signal rankings。\n\n### 审查重点（必须逐条评估）\n\n1. **新颖性评估**\n   - \"Correlation-selection gap\" 概念是否真正 novel？与 MBR decoding 文献中已知的 utility-quality misalignment 有何本质区别？\n   - 对比 Yao et al. (2026)（论文明确 cite 为最近相关工作），增量贡献是什么？是否足以支撑 main conference paper？\n   - \"Instance-level signals fail by construction\" 是 definitional 而非 empirical contribution——论文是否正确区分了这两者？\n   - LP compression 作为核心 empirical finding 的新颖性？verbalized confidence baseline 是否增强了贡献？\n\n2. **相关工作覆盖**\n   - 搜索 2025-2026 年相关工作：self-consistency for structured prediction, MBR decoding for IE, confidence estimation for NER/RE, test-time scaling for structured outputs\n   - 是否遗漏重要 baseline 或对比方法？例如：learned verifiers, reward models, ensemble methods\n   - 与 Eikema & Aziz (2025) structured MBR 的讨论是否充分？\n   - uncertainty quantification 文献（semantic uncertainty, P(True)）的覆盖是否足够？\n\n3. **写作质量**\n   - 论文结构是否清晰？8 页内容密度是否适当？\n   - 术语定义是否一致（per-sample vs instance-level, quality estimation vs sample selection）？\n   - Figure/Table 设计是否有效传达核心信息？\n   - Abstract 是否准确反映论文内容？是否有 overclaiming？\n   - \"Preliminary\" 标注在论文中频繁出现——是否影响论文整体可信度？\n\n4. **格式合规**\n   - 页数是否在 8 页限制内？\n   - 引用格式是否符合 ACL/natbib 规范？\n   - 匿名是否完全？检查是否有作者身份泄露（GitHub links, institution names, 服务器信息等）\n   - Ethics Statement 是否充分？\n   - Limitations 是否诚实且全面？\n\n5. **呈现与叙事**\n   - 核心 \"negative result\"（信号无法 selection）的 framing 是否恰当？\n   - 是否给出足够的 actionable insight？还是仅仅 \"X doesn't work\"？\n   - Discussion 中 \"trained verifiers\" 的前瞻讨论是否有价值？\n   - 大量实验细节放在 appendix 中——正文是否 self-contained？\n\n请按 EMNLP 审稿标准输出完整审稿报告，包括：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (1-5 scale + confidence)。同时搜索最新相关工作，检查是否有遗漏。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T04:18:45.037Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T04:18:45.037Z",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

## Round 1

109 recorded events

### User

_source line 3 · 2026-05-16T04:18:45.072Z_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 呈现**

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **页数**: 长文 8 页 + 无限参考文献 + 附录不计入页数
- **模板**: ACL style（`\usepackage[review]{acl}`）
- **匿名**: Double-blind
- **附录规则**: 附录在 references 之后，审稿人可选择性参考但不应要求内容必须移至附录

### 论文路径
`projects/struct_self_consist_ie/docs/paper/main.tex`
（各章节在 `sections/` 子目录下：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex）
引用文件：`references.bib`

### 论文概要
论文评估 5 种置信度信号（Soft Jaccard, Voting Confidence, Exact Match, Fleiss' κ, Log-probability）在 LLM-based structured IE（NER + RE）中的 quality estimation 和 sample selection 能力。核心发现是 "correlation-selection gap"：信号能预测质量但无法改善 best-of-N 选择。3 个贡献：(1) metric dissociation (QE vs selection), (2) LP compression 和 MBR failure, (3) difficulty-dependent signal rankings。

### 审查重点（必须逐条评估）

1. **新颖性评估**
   - "Correlation-selection gap" 概念是否真正 novel？与 MBR decoding 文献中已知的 utility-quality misalignment 有何本质区别？
   - 对比 Yao et al. (2026)（论文明确 cite 为最近相关工作），增量贡献是什么？是否足以支撑 main conference paper？
   - "Instance-level signals fail by construction" 是 definitional 而非 empirical contribution——论文是否正确区分了这两者？
   - LP compression 作为核心 empirical finding 的新颖性？verbalized confidence baseline 是否增强了贡献？

2. **相关工作覆盖**
   - 搜索 2025-2026 年相关工作：self-consistency for structured prediction, MBR decoding for IE, confidence estimation for NER/RE, test-time scaling for structured outputs
   - 是否遗漏重要 baseline 或对比方法？例如：learned verifiers, reward models, ensemble methods
   - 与 Eikema & Aziz (2025) structured MBR 的讨论是否充分？
   - uncertainty quantification 文献（semantic uncertainty, P(True)）的覆盖是否足够？

3. **写作质量**
   - 论文结构是否清晰？8 页内容密度是否适当？
   - 术语定义是否一致（per-sample vs instance-level, quality estimation vs sample selection）？
   - Figure/Table 设计是否有效传达核心信息？
   - Abstract 是否准确反映论文内容？是否有 overclaiming？
   - "Preliminary" 标注在论文中频繁出现——是否影响论文整体可信度？

4. **格式合规**
   - 页数是否在 8 页限制内？
   - 引用格式是否符合 ACL/natbib 规范？
   - 匿名是否完全？检查是否有作者身份泄露（GitHub links, institution names, 服务器信息等）
   - Ethics Statement 是否充分？
   - Limitations 是否诚实且全面？

5. **呈现与叙事**
   - 核心 "negative result"（信号无法 selection）的 framing 是否恰当？
   - 是否给出足够的 actionable insight？还是仅仅 "X doesn't work"？
   - Discussion 中 "trained verifiers" 的前瞻讨论是否有价值？
   - 大量实验细节放在 appendix 中——正文是否 self-contained？

请按 EMNLP 审稿标准输出完整审稿报告，包括：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (1-5 scale + confidence)。同时搜索最新相关工作，检查是否有遗漏。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "8d700424-00a2-470b-a1fa-902eaa64c4fd",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T04:18:45.071Z_

```json
{
  "parentUuid": "8d700424-00a2-470b-a1fa-902eaa64c4fd",
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
  "uuid": "132263cc-677e-4430-9bda-70383da652fd",
  "timestamp": "2026-05-16T04:18:45.071Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T04:18:45.071Z_

```json
{
  "parentUuid": "132263cc-677e-4430-9bda-70383da652fd",
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
  "uuid": "977b8350-c5ed-4ea6-88be-a8b60e634309",
  "timestamp": "2026-05-16T04:18:45.071Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T04:18:45.071Z_

```json
{
  "parentUuid": "977b8350-c5ed-4ea6-88be-a8b60e634309",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7148cfeb-2c6a-4f59-be94-20d59b940dd8",
  "timestamp": "2026-05-16T04:18:45.071Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
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
  "aiTitle": "Review Round 1 for structured IE confidence estimation paper",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Assistant

_source line 8 · 2026-05-16T04:18:50.416Z_

<details><summary>Logged reasoning block</summary>

```text
The user (Review Director) is asking me to perform a Round 1 review of a paper as Reviewer 2, focusing on novelty, related work coverage, writing quality, and presentation. Let me start by:

1. Loading the review-reviewer-session-start skill to initialize
2. Reading the paper materials
3. Searching for EMNLP 2026 / ACL ARR reviewer guidelines
4. Searching for recent related work

Let me begin by reading the paper and searching for reviewer guidelines in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7148cfeb-2c6a-4f59-be94-20d59b940dd8",
  "isSidechain": false,
  "requestId": "req_011Cb5bzC2L2NdtPEer4QLQX",
  "type": "assistant",
  "uuid": "1a6ab30f-c7dd-4977-a1b9-e6adb3ea70ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Awp5yoocEupE7M3hfJhGps",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14305,
      "cache_read_input_tokens": 11841,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14305,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 302,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14305
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-16T04:18:51.415Z_

开始 Round 1 审稿。先并行执行：读取论文各章节、搜索 ARR reviewer guidelines、搜索最新相关工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a6ab30f-c7dd-4977-a1b9-e6adb3ea70ae",
  "isSidechain": false,
  "requestId": "req_011Cb5bzC2L2NdtPEer4QLQX",
  "type": "assistant",
  "uuid": "db8839f7-30c5-4354-af79-f7c0f6a602e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Awp5yoocEupE7M3hfJhGps",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14305,
      "cache_read_input_tokens": 11841,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14305,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 302,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14305
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-16T04:18:52.353Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019PxDH3bB4q95BnUYna34to`</summary>

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
  "parentUuid": "db8839f7-30c5-4354-af79-f7c0f6a602e5",
  "isSidechain": false,
  "requestId": "req_011Cb5bzC2L2NdtPEer4QLQX",
  "type": "assistant",
  "uuid": "dca2d4ff-a915-4c63-91a1-ac53d641267a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Awp5yoocEupE7M3hfJhGps",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14305,
      "cache_read_input_tokens": 11841,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14305,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 302,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14305
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-16T04:18:52.361Z_

<details><summary>↩ Tool result · `toolu_019PxDH3bB4q95BnUYna34to`</summary>

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
  "parentUuid": "dca2d4ff-a915-4c63-91a1-ac53d641267a",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "29d8285a-2031-4a17-805f-468e19b9c415",
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
  "sourceToolAssistantUUID": "dca2d4ff-a915-4c63-91a1-ac53d641267a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-16T04:18:54.561Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me start by reading the paper sections and searching for reviewer guidelines in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29d8285a-2031-4a17-805f-468e19b9c415",
  "isSidechain": false,
  "requestId": "req_011Cb5bzjCZtkXU3P2xUiDS4",
  "type": "assistant",
  "uuid": "a838c167-28c9-4939-8bb5-4972b0ea7cbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gp2AedjpawWpgp8uyif5f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 26146,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 390,
          "cache_read_input_tokens": 26146,
          "cache_creation_input_tokens": 2297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2297
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-16T04:18:55.567Z_

开始并行读取论文各章节、搜索 ARR reviewer guidelines 和最新相关工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a838c167-28c9-4939-8bb5-4972b0ea7cbc",
  "isSidechain": false,
  "requestId": "req_011Cb5bzjCZtkXU3P2xUiDS4",
  "type": "assistant",
  "uuid": "b8e3ee66-117e-4ccb-8a6c-69b3d8405f86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gp2AedjpawWpgp8uyif5f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 26146,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 390,
          "cache_read_input_tokens": 26146,
          "cache_creation_input_tokens": 2297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2297
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-16T04:18:56.529Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NGhXPEhZTdbpep1QEMdQnm`</summary>

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
  "parentUuid": "b8e3ee66-117e-4ccb-8a6c-69b3d8405f86",
  "isSidechain": false,
  "requestId": "req_011Cb5bzjCZtkXU3P2xUiDS4",
  "type": "assistant",
  "uuid": "ba80408d-0185-4d39-b45f-f25bb173387a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gp2AedjpawWpgp8uyif5f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 26146,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 390,
          "cache_read_input_tokens": 26146,
          "cache_creation_input_tokens": 2297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2297
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-16T04:18:56.544Z_

<details><summary>↩ Tool result · `toolu_01NGhXPEhZTdbpep1QEMdQnm`</summary>

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
21	\title{Strong Predictors, Weak Selectors:\\ The Correlation-Selection Gap in LLM-Based Information Extraction}
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
  "parentUuid": "ba80408d-0185-4d39-b45f-f25bb173387a",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "0b1f2057-f999-4540-baf5-41a3ae648539",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\graphicspath{{figures/}}\n\n\\title{Strong Predictors, Weak Selectors:\\\\ The Correlation-Selection Gap in LLM-Based Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\section*{Ethics Statement}\nAll experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).\nCoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.\nNo new human data was collected or annotated for this study.\nOur findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.\nCode and data will be released upon acceptance at [anonymized URL].\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  },
  "sourceToolAssistantUUID": "ba80408d-0185-4d39-b45f-f25bb173387a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T04:18:57.520Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01S9carzZ5aJyLGZxbpzNkPo`</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b1f2057-f999-4540-baf5-41a3ae648539",
  "isSidechain": false,
  "requestId": "req_011Cb5bzjCZtkXU3P2xUiDS4",
  "type": "assistant",
  "uuid": "b6583ef5-53e7-4d78-8f92-9ffed029f568",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gp2AedjpawWpgp8uyif5f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 26146,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 390,
          "cache_read_input_tokens": 26146,
          "cache_creation_input_tokens": 2297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2297
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-16T04:18:57.538Z_

<details><summary>↩ Tool result · `toolu_01S9carzZ5aJyLGZxbpzNkPo`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6583ef5-53e7-4d78-8f92-9ffed029f568",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "4f014d2b-cb73-48fa-a8c2-8fa8a4ab7fac",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 13,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "b6583ef5-53e7-4d78-8f92-9ffed029f568",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T04:18:58.002Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BFXfMgpfwCe53rPvXknFGm`</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring rubric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f014d2b-cb73-48fa-a8c2-8fa8a4ab7fac",
  "isSidechain": false,
  "requestId": "req_011Cb5bzjCZtkXU3P2xUiDS4",
  "type": "assistant",
  "uuid": "5917842f-570b-4366-abb8-ddb569064c78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gp2AedjpawWpgp8uyif5f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 26146,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 390,
          "cache_read_input_tokens": 26146,
          "cache_creation_input_tokens": 2297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2297
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-16T04:18:58.484Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Segif2nPHFvv5mhNxM7hzo`</summary>

```json
{
  "query": "self-consistency structured prediction NER RE confidence estimation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5917842f-570b-4366-abb8-ddb569064c78",
  "isSidechain": false,
  "requestId": "req_011Cb5bzjCZtkXU3P2xUiDS4",
  "type": "assistant",
  "uuid": "81dc4269-d918-44e1-a866-dc879c4bf92a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gp2AedjpawWpgp8uyif5f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 26146,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 390,
          "cache_read_input_tokens": 26146,
          "cache_creation_input_tokens": 2297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2297
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-16T04:18:58.813Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018vL5yN8dzE2SN5z8BwnrJu`</summary>

```json
{
  "query": "MBR decoding information extraction structured output 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81dc4269-d918-44e1-a866-dc879c4bf92a",
  "isSidechain": false,
  "requestId": "req_011Cb5bzjCZtkXU3P2xUiDS4",
  "type": "assistant",
  "uuid": "f348fb39-4b63-46c4-b496-3a5140b073b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gp2AedjpawWpgp8uyif5f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 26146,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 390,
          "cache_read_input_tokens": 26146,
          "cache_creation_input_tokens": 2297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2297
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 呈现**  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **页数**: 长文 8 页 +…",
  "leafUuid": "f348fb39-4b63-46c4-b496-3a5140b073b7",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 for structured IE confidence estimation paper",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Tool result

_source line 23 · 2026-05-16T04:19:04.650Z_

<details><summary>↩ Tool result · `toolu_01BFXfMgpfwCe53rPvXknFGm`</summary>

```text
Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring rubric"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"}]

Based on the web search results, here's what I found regarding ACL ARR 2025-2026 reviewer guidelines:

## Key Scoring Framework

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score Requirements

The soundness scores must be justified by the text of the review. Additionally, if you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

## Excitement vs. Soundness Distinction

Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Review Form Elements

The review form also includes assessment of:
- Whether authors have adequately discussed the limitations and potential positive and negative societal impacts of their work
- Whether there is enough information in the paper for a reader to reproduce the main results or build upon this work
- Ethical issues with the paper and the extent to which they have been acknowledged or addressed by the authors

For more detailed information about the complete review form and criteria, you can access the official resources at aclrollingreview.org/reviewerguidelines and aclrollingreview.org/reviewform.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5917842f-570b-4366-abb8-ddb569064c78",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "58ef929d-9616-4fdc-a0d7-092062d2b0db",
  "toolUseResult": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring rubric",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CXg3uPRBx84Qwpsy5gAdvq",
        "content": [
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewform"
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
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "aclrollingreview/cfp.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"
          },
          {
            "title": "aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"
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
            "title": "ACLRollingReview (@ReviewAcl) / X",
            "url": "https://x.com/reviewacl"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding ACL ARR 2025-2026 reviewer guidelines:\n\n## Key Scoring Framework\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\n\n## Soundness Score Requirements\n\nThe soundness scores must be justified by the text of the review. Additionally, if you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.\n\n## Excitement vs. Soundness Distinction\n\nSometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.\n\n## Review Form Elements\n\nThe review form also includes assessment of:\n- Whether authors have adequately discussed the limitations and potential positive and negative societal impacts of their work\n- Whether there is enough information in the paper for a reader to reproduce the main results or build upon this work\n- Ethical issues with the paper and the extent to which they have been acknowledged or addressed by the authors\n\nFor more detailed information about the complete review form and criteria, you can access the official resources at aclrollingreview.org/reviewerguidelines and aclrollingreview.org/reviewform."
    ],
    "durationSeconds": 6.642258018999999
  },
  "sourceToolAssistantUUID": "5917842f-570b-4366-abb8-ddb569064c78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T04:19:05.954Z_

<details><summary>↩ Tool result · `toolu_018vL5yN8dzE2SN5z8BwnrJu`</summary>

```text
Web search results for query: "MBR decoding information extraction structured output 2025 2026"

Links: [{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Taming LLM Outputs: Your Guide to Structured Text Generation","url":"https://www.dataiku.com/stories/blog/your-guide-to-structured-text-generation"},{"title":"Constrained Decoding: Grammar-Guided Generation for Structured LLM Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output"},{"title":"A Guide to Structured Outputs Using Constrained Decoding","url":"https://www.aidancooper.co.uk/constrained-decoding/"},{"title":"Large language model driven transferable key information ...","url":"https://www.nature.com/articles/s41598-025-15627-z.pdf"},{"title":"Grammar-constrained decoding for structured information ...","url":"https://public-pages-files-2025.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/pdf"},{"title":"LLM Structured Outputs: The Practical Guide for Every Provider [2026]","url":"https://techsy.io/en/blog/llm-structured-outputs-guide"}]

Based on the search results, here's what I found regarding MBR decoding, information extraction, and structured output for 2025-2026:

## Constrained Decoding and Structured Output

Constrained decoding is the technique behind guaranteed structured output. It inserts a logit processor between the model's output and the sampling step, tracking position within the target grammar and masking invalid tokens.

## Recent Developments (2025-2026)

In Phase 4: High-performance engines (2025 to 2026), open-source engines like XGrammar and llguidance achieved near-zero overhead constrained decoding. XGrammar is the default structured generation backend for vLLM, SGLang, and TensorRT-LLM as of March 2026, achieving under 40 microseconds per token with near-zero overhead in JSON generation.

llguidance from Microsoft uses a Rust-based Earley parser at ~50 microseconds per token with negligible startup costs.

## Information Extraction Applications

Task-specific fine-tuning has shown success in structured output generation, particularly for tasks like named-entity recognition and information extraction. In the field of structured information extraction, there are typically semantic and syntactic constraints on the output of information extraction systems, which can typically not be guaranteed using standard (fine-tuned) encoder-decoder architectures.

## Provider Adoption

By 2025-2026, every major provider had adopted the same approach to structured outputs using constrained decoding for schema compliance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f348fb39-4b63-46c4-b496-3a5140b073b7",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "ec5c07ef-6f98-45a1-bd5a-96239dad831a",
  "toolUseResult": {
    "query": "MBR decoding information extraction structured output 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PnGyW8QTR7rU9aRwYoY2yp",
        "content": [
          {
            "title": "Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"
          },
          {
            "title": "SLOT: Structuring the Output of Large Language Models",
            "url": "https://aclanthology.org/2025.emnlp-industry.32.pdf"
          },
          {
            "title": "Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts",
            "url": "https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"
          },
          {
            "title": "How Structured Outputs and Constrained Decoding Work | Let's Data Science",
            "url": "https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"
          },
          {
            "title": "Taming LLM Outputs: Your Guide to Structured Text Generation",
            "url": "https://www.dataiku.com/stories/blog/your-guide-to-structured-text-generation"
          },
          {
            "title": "Constrained Decoding: Grammar-Guided Generation for Structured LLM Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer",
            "url": "https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output"
          },
          {
            "title": "A Guide to Structured Outputs Using Constrained Decoding",
            "url": "https://www.aidancooper.co.uk/constrained-decoding/"
          },
          {
            "title": "Large language model driven transferable key information ...",
            "url": "https://www.nature.com/articles/s41598-025-15627-z.pdf"
          },
          {
            "title": "Grammar-constrained decoding for structured information ...",
            "url": "https://public-pages-files-2025.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/pdf"
          },
          {
            "title": "LLM Structured Outputs: The Practical Guide for Every Provider [2026]",
            "url": "https://techsy.io/en/blog/llm-structured-outputs-guide"
          }
        ]
      },
      "Based on the search results, here's what I found regarding MBR decoding, information extraction, and structured output for 2025-2026:\n\n## Constrained Decoding and Structured Output\n\nConstrained decoding is the technique behind guaranteed structured output. It inserts a logit processor between the model's output and the sampling step, tracking position within the target grammar and masking invalid tokens.\n\n## Recent Developments (2025-2026)\n\nIn Phase 4: High-performance engines (2025 to 2026), open-source engines like XGrammar and llguidance achieved near-zero overhead constrained decoding. XGrammar is the default structured generation backend for vLLM, SGLang, and TensorRT-LLM as of March 2026, achieving under 40 microseconds per token with near-zero overhead in JSON generation.\n\nllguidance from Microsoft uses a Rust-based Earley parser at ~50 microseconds per token with negligible startup costs.\n\n## Information Extraction Applications\n\nTask-specific fine-tuning has shown success in structured output generation, particularly for tasks like named-entity recognition and information extraction. In the field of structured information extraction, there are typically semantic and syntactic constraints on the output of information extraction systems, which can typically not be guaranteed using standard (fine-tuned) encoder-decoder architectures.\n\n## Provider Adoption\n\nBy 2025-2026, every major provider had adopted the same approach to structured outputs using constrained decoding for schema compliance."
    ],
    "durationSeconds": 7.137087890999999
  },
  "sourceToolAssistantUUID": "f348fb39-4b63-46c4-b496-3a5140b073b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T04:19:06.302Z_

<details><summary>↩ Tool result · `toolu_01Segif2nPHFvv5mhNxM7hzo`</summary>

```text
Web search results for query: "self-consistency structured prediction NER RE confidence estimation 2025 2026"

Links: [{"title":"Learning When to Sample: Confidence-Aware Self-Consistency for","url":"https://arxiv.org/pdf/2603.08999"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/pdf/2502.06233"},{"title":"[1111.1386] Confidence Estimation in Structured Prediction","url":"https://arxiv.org/abs/1111.1386"},{"title":"Confidence Estimation Techniques","url":"https://www.emergentmind.com/topics/confidence-estimation-techniques"},{"title":"Learning When to Sample: Confidence-Aware Self-Consistency for Efficient LLM Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2603.08999"},{"title":"Thought Pruning for Efficient Scaling with Self-Consistency","url":"https://aclanthology.org/2025.emnlp-main.1750.pdf"},{"title":"A Calibrated Reflection Approach for Enhancing ...","url":"https://aclanthology.org/2025.trustnlp-main.26.pdf"},{"title":"(PDF) Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://www.researchgate.net/publication/359390115_Self-Consistency_Improves_Chain_of_Thought_Reasoning_in_Language_Models"},{"title":"Deep Think with Confidence DEEP THINK WITH CONFIDENCE","url":"https://jiaweizzhao.github.io/deepconf/static/pdfs/deepconf_arxiv.pdf"},{"title":"[2605.07806] Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs","url":"https://arxiv.org/abs/2605.07806"}]

I've found several relevant research papers and resources on self-consistency, structured prediction, confidence estimation, and related topics from 2025-2026. Here's a summary of the key findings:

## Recent Research on Confidence and Self-Consistency (2025-2026)

**Confidence-Aware Self-Consistency for LLM Reasoning:**
Recent work assigns confidence scores to intermediate reasoning steps and uses them to weight and aggregate multiple Chain-of-Thought paths, improving robustness over vanilla self-consistency by explicitly leveraging uncertainty.

**Confidence Estimation Techniques:**
For NER with noisy labels, integrated confidence estimation facilitates "partial marginalization" using global (CRF-based) or local (softmax) confidence, with calibration adjustments to reflect the internal structure of entity tags. Additionally, in LLMs, relative judgment approaches—such as pairwise "confidence preference" ranking combined with rank aggregation methods—produce more reliable, discriminative confidence scores than absolute or self-consistency prompting.

**Structured Prediction and Self-Consistency:**
A confidence-aware reasoning framework analyzes a single completed Chain-of-Thought to determine whether additional multi-path reasoning is necessary, avoiding unnecessary sampling and computation, and introduces an attention-based RNN decision model that leverages sentence-wise numeric and linguistic features to capture temporal reasoning dynamics and assess reasoning reliability.

**Deep Confidence Estimation:**
Group confidence quantifies the confidence of intermediate reasoning steps, providing a more localized and smoother signal by averaging token confidence over overlapping spans of the reasoning trace.

**Self-Assessment Approaches:**
Competence-related appraisal dimensions, particularly effort and ability, consistently match or outperform confidence across most settings, with effort additionally yielding less overoptimistic estimates that remain stable across model sizes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81dc4269-d918-44e1-a866-dc879c4bf92a",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "d02446e9-4cb6-4963-a31d-b5c5395ac12e",
  "toolUseResult": {
    "query": "self-consistency structured prediction NER RE confidence estimation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WWm2ia4mSn5rHR7TGrDr8z",
        "content": [
          {
            "title": "Learning When to Sample: Confidence-Aware Self-Consistency for",
            "url": "https://arxiv.org/pdf/2603.08999"
          },
          {
            "title": "Confidence Improves Self-Consistency in LLMs",
            "url": "https://arxiv.org/pdf/2502.06233"
          },
          {
            "title": "[1111.1386] Confidence Estimation in Structured Prediction",
            "url": "https://arxiv.org/abs/1111.1386"
          },
          {
            "title": "Confidence Estimation Techniques",
            "url": "https://www.emergentmind.com/topics/confidence-estimation-techniques"
          },
          {
            "title": "Learning When to Sample: Confidence-Aware Self-Consistency for Efficient LLM Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2603.08999"
          },
          {
            "title": "Thought Pruning for Efficient Scaling with Self-Consistency",
            "url": "https://aclanthology.org/2025.emnlp-main.1750.pdf"
          },
          {
            "title": "A Calibrated Reflection Approach for Enhancing ...",
            "url": "https://aclanthology.org/2025.trustnlp-main.26.pdf"
          },
          {
            "title": "(PDF) Self-Consistency Improves Chain of Thought Reasoning in Language Models",
            "url": "https://www.researchgate.net/publication/359390115_Self-Consistency_Improves_Chain_of_Thought_Reasoning_in_Language_Models"
          },
          {
            "title": "Deep Think with Confidence DEEP THINK WITH CONFIDENCE",
            "url": "https://jiaweizzhao.github.io/deepconf/static/pdfs/deepconf_arxiv.pdf"
          },
          {
            "title": "[2605.07806] Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs",
            "url": "https://arxiv.org/abs/2605.07806"
          }
        ]
      },
      "I've found several relevant research papers and resources on self-consistency, structured prediction, confidence estimation, and related topics from 2025-2026. Here's a summary of the key findings:\n\n## Recent Research on Confidence and Self-Consistency (2025-2026)\n\n**Confidence-Aware Self-Consistency for LLM Reasoning:**\nRecent work assigns confidence scores to intermediate reasoning steps and uses them to weight and aggregate multiple Chain-of-Thought paths, improving robustness over vanilla self-consistency by explicitly leveraging uncertainty.\n\n**Confidence Estimation Techniques:**\nFor NER with noisy labels, integrated confidence estimation facilitates \"partial marginalization\" using global (CRF-based) or local (softmax) confidence, with calibration adjustments to reflect the internal structure of entity tags. Additionally, in LLMs, relative judgment approaches—such as pairwise \"confidence preference\" ranking combined with rank aggregation methods—produce more reliable, discriminative confidence scores than absolute or self-consistency prompting.\n\n**Structured Prediction and Self-Consistency:**\nA confidence-aware reasoning framework analyzes a single completed Chain-of-Thought to determine whether additional multi-path reasoning is necessary, avoiding unnecessary sampling and computation, and introduces an attention-based RNN decision model that leverages sentence-wise numeric and linguistic features to capture temporal reasoning dynamics and assess reasoning reliability.\n\n**Deep Confidence Estimation:**\nGroup confidence quantifies the confidence of intermediate reasoning steps, providing a more localized and smoother signal by averaging token confidence over overlapping spans of the reasoning trace.\n\n**Self-Assessment Approaches:**\nCompetence-related appraisal dimensions, particularly effort and ability, consistently match or outperform confidence across most settings, with effort additionally yielding less overoptimistic estimates that remain stable across model sizes."
    ],
    "durationSeconds": 7.815648909999998
  },
  "sourceToolAssistantUUID": "81dc4269-d918-44e1-a866-dc879c4bf92a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-16T04:19:08.881Z_

<details><summary>Logged reasoning block</summary>

```text
The glob didn't find files - I need to check the correct path. Let me look for the sections directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d02446e9-4cb6-4963-a31d-b5c5395ac12e",
  "isSidechain": false,
  "requestId": "req_011Cb5c1kkcRERFDSaWx8PAZ",
  "type": "assistant",
  "uuid": "ff303582-5532-4fb5-9485-58abedb57a5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvaxuQB2BtTN1QAB1jFrgP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 2771,
      "cache_read_input_tokens": 28443,
      "output_tokens": 398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2771,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 936,
          "output_tokens": 398,
          "cache_read_input_tokens": 28443,
          "cache_creation_input_tokens": 2771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2771
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-16T04:19:09.332Z_

Glob 路径有误，需要找到正确的 sections 目录。同时获取 ARR review form 详细内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff303582-5532-4fb5-9485-58abedb57a5a",
  "isSidechain": false,
  "requestId": "req_011Cb5c1kkcRERFDSaWx8PAZ",
  "type": "assistant",
  "uuid": "20c9bbb4-7621-4e56-bb2e-36bc056c85ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvaxuQB2BtTN1QAB1jFrgP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 2771,
      "cache_read_input_tokens": 28443,
      "output_tokens": 398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2771,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 936,
          "output_tokens": 398,
          "cache_read_input_tokens": 28443,
          "cache_creation_input_tokens": 2771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2771
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-16T04:19:10.313Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019MuhpzzqoxZ4vQHvFcnuBr`</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20c9bbb4-7621-4e56-bb2e-36bc056c85ae",
  "isSidechain": false,
  "requestId": "req_011Cb5c1kkcRERFDSaWx8PAZ",
  "type": "assistant",
  "uuid": "4ee0b34b-552c-4a7b-96ad-d729cff0c7ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvaxuQB2BtTN1QAB1jFrgP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 2771,
      "cache_read_input_tokens": 28443,
      "output_tokens": 398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2771,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 936,
          "output_tokens": 398,
          "cache_read_input_tokens": 28443,
          "cache_creation_input_tokens": 2771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2771
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-16T04:19:10.351Z_

<details><summary>↩ Tool result · `toolu_019MuhpzzqoxZ4vQHvFcnuBr`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ee0b34b-552c-4a7b-96ad-d729cff0c7ca",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "e312f9ca-ff7a-4a53-85b0-1b1c9a1dc347",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
    ],
    "durationMs": 29,
    "numFiles": 9,
    "truncated": false
  },
  "sourceToolAssistantUUID": "4ee0b34b-552c-4a7b-96ad-d729cff0c7ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T04:19:12.184Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Uapz84UzauXE7EC8EVHk8k`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc), and the description of each score level. I need the exact rubric for soundness, excitement, overall assessment, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e312f9ca-ff7a-4a53-85b0-1b1c9a1dc347",
  "isSidechain": false,
  "requestId": "req_011Cb5c1kkcRERFDSaWx8PAZ",
  "type": "assistant",
  "uuid": "529aa8b4-0434-496d-8de9-41aedf0a31bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvaxuQB2BtTN1QAB1jFrgP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 2771,
      "cache_read_input_tokens": 28443,
      "output_tokens": 398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2771,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 936,
          "output_tokens": 398,
          "cache_read_input_tokens": 28443,
          "cache_creation_input_tokens": 2771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2771
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-16T04:19:13.288Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KBEyL76G6Qz3uEc1jB1JPj`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, how to score papers, what constitutes a strong vs weak paper, and any specific instructions about novelty, soundness, reproducibility, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "529aa8b4-0434-496d-8de9-41aedf0a31bf",
  "isSidechain": false,
  "requestId": "req_011Cb5c1kkcRERFDSaWx8PAZ",
  "type": "assistant",
  "uuid": "d0b45067-5dea-4e50-9b3d-c03e8aada9e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvaxuQB2BtTN1QAB1jFrgP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 2771,
      "cache_read_input_tokens": 28443,
      "output_tokens": 398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2771,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 936,
          "output_tokens": 398,
          "cache_read_input_tokens": 28443,
          "cache_creation_input_tokens": 2771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2771
          },
          "type": "message"
        }
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

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 呈现**  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **页数**: 长文 8 页 +…",
  "leafUuid": "d0b45067-5dea-4e50-9b3d-c03e8aada9e0",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 for structured IE confidence estimation paper",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Tool result

_source line 34 · 2026-05-16T04:19:18.365Z_

<details><summary>↩ Tool result · `toolu_01Uapz84UzauXE7EC8EVHk8k`</summary>

```text
# ACL Rolling Review Form - Scoring Rubrics

## Reviewer Confidence
**Scale: 1-5**
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness
**Scale: 1-5 (with .5 increments)**
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement
**Scale: 1-5 (with .5 increments)**
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend presentation."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points to others."
- **2**: "Potentially Interesting: does not resonate with me, but might with others."
- **1**: "Not Exciting: does not resonate with me."

## Overall Assessment
**Scale: 1-5 (with .5 increments)**
- **5**: "Consider for Award"
- **4**: "Conference"
- **3**: "Findings"
- **2**: "Resubmit next cycle"
- **1**: "Do not resubmit"

## Additional Scored Dimensions
- **Reproducibility** (1-5)
- **Datasets** (1-5)
- **Software** (1-5)
- **Author Identity Knowledge** (1-5)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "529aa8b4-0434-496d-8de9-41aedf0a31bf",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "0b69100a-45c7-46c7-a479-6a1a57e0f488",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Scoring Rubrics\n\n## Reviewer Confidence\n**Scale: 1-5**\n- **5**: \"Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work.\"\n- **4**: \"Quite sure. I tried to check the important points carefully.\"\n- **3**: \"Pretty sure, but there's a chance I missed something.\"\n- **2**: \"Willing to defend my evaluation, but it is fairly likely that I missed some details.\"\n- **1**: \"Not my area, or paper is very hard to understand.\"\n\n## Soundness\n**Scale: 1-5 (with .5 increments)**\n- **5**: \"Excellent: This study is one of the most thorough I have seen.\"\n- **4**: \"Strong: This study provides sufficient support for all its claims.\"\n- **3**: \"Acceptable: This study provides sufficient support for its main claims.\"\n- **2**: \"Poor: Some main claims are not sufficiently supported.\"\n- **1**: \"Major Issues: This study is not yet sufficiently thorough to warrant publication.\"\n\n## Excitement\n**Scale: 1-5 (with .5 increments)**\n- **5**: \"Highly Exciting: I would recommend this paper to others and/or attend presentation.\"\n- **4**: \"Exciting: I would mention this paper to others.\"\n- **3**: \"Interesting: I might mention some points to others.\"\n- **2**: \"Potentially Interesting: does not resonate with me, but might with others.\"\n- **1**: \"Not Exciting: does not resonate with me.\"\n\n## Overall Assessment\n**Scale: 1-5 (with .5 increments)**\n- **5**: \"Consider for Award\"\n- **4**: \"Conference\"\n- **3**: \"Findings\"\n- **2**: \"Resubmit next cycle\"\n- **1**: \"Do not resubmit\"\n\n## Additional Scored Dimensions\n- **Reproducibility** (1-5)\n- **Datasets** (1-5)\n- **Software** (1-5)\n- **Author Identity Knowledge** (1-5)",
    "durationMs": 6177,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "529aa8b4-0434-496d-8de9-41aedf0a31bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-16T04:19:27.289Z_

<details><summary>↩ Tool result · `toolu_01KBEyL76G6Qz3uEc1jB1JPj`</summary>

```text
# ARR Reviewer Guidelines: Core Evaluation Framework

## What Reviewers Should Evaluate

Reviewers assess papers across multiple dimensions:

**Soundness**: Technical correctness and methodological validity. Reviews must justify soundness scores with evidence from the review text.

**Excitement**: Personal interest level, kept separate from soundness assessment since subjective preferences shouldn't drive rejection.

**Overall Recommendation**: A composite judgment reflecting soundness, novelty, impact, and potential contribution to the field.

## Key Evaluation Criteria

**Specificity Requirements**
Reviewers must be concrete. Instead of writing "missing relevant references," identify specific works. Rather than stating "X is unclear," explain what information is absent from the description.

**Technical Soundness Assessment**
- Verify mathematical formulations are correct
- Check proof completeness and validity
- Ensure experimental design supports claims
- Validate statistical significance reporting
- Confirm reproducibility details are sufficient

**Novelty Evaluation**
Papers need "sufficient evidence for the claim that the authors are making"—not necessarily state-of-the-art results. "Highly similar work X and Y has been published [3+ months prior to submission deadline]" constitutes plagiarism concern; otherwise, acknowledge that "many findings seem obvious in retrospect, but community awareness differs."

## Common Problematic Review Heuristics to Avoid

Reviewers should question whether they're applying bias rather than legitimate critique:

- Dismissing findings as "unsurprising" despite lacking prior empirical validation
- Rejecting work for methodological simplicity when simpler solutions are preferable
- Requiring state-of-the-art results when contributions exist on other dimensions
- Criticizing resource/analysis papers for lacking modeling novelty
- Penalizing non-English research as less generalizable than English-only work

## NLP-Specific Issues to Flag

**Methodology Problems (M1-M5)**
- LLM-only evaluation lacking reliability validation
- Insufficient reproducibility details
- Undisclosed data quality issues
- Unmotivated model/benchmark selection
- Incomplete mathematical assumptions or proofs

**Result Interpretation Issues (R1-R5)**
- Statistical problems or p-hacking
- Claims exceeding evaluation scope
- Speculation presented as conclusions
- Overclaiming or misleading framing
- Missing significance assessment

**General Issues (G1-G5)**
- Unclear research questions or contributions
- Reliance on questionable precedents
- Misrepresented or missing related work
- Undefined key terminology
- Misattributed or incorrect citations

## Scoring Alignment Requirement

Low soundness scores must correlate with identified technical flaws. If you rate a paper low without explaining substantial issues, your review lacks credibility. Conversely, papers can score high on soundness while receiving lower excitement scores.

## Professional Standards

Reviews should maintain professional, neutral tone. The guidelines emphasize: "Write the review you would like to get yourself." Sarcasm, dismissiveness, or insulting language violates peer review standards, particularly given anonymous reviewer power dynamics.

## Resubmission-Specific Guidance

**Repeat reviewers** should confirm authors addressed previous concerns, explicitly acknowledging their revision notes and explaining whether weaknesses were adequately resolved.

**Substitute reviewers** distinguish between (i) previously identified weaknesses inadequately addressed, (ii) newly raised critical soundness issues, and (iii) other new suggestions for improvement.

**Fresh reviewers** form independent assessments, then cross-reference with prior reviews to explain whether previous weaknesses persist despite revisions.

## Confidentiality and Anonymity Rules

- All submission and review information is strictly confidential
- Don't submit manuscripts to third-party services, including non-privacy-preserving AI tools
- Don't deliberately search for paper preprints to identify authors
- If author identity becomes apparent, disclose this to the area chair
- Postpone literature searches until after forming initial impressions

## Generative AI Policy

Reviewers cannot use AI to draft reviews initially, though responsible editing assistance (especially for non-native speakers) is acceptable. Critically, "neither reviewers nor editors may upload their peer review report into a non-privacy-preserving generative tool." Papers with hidden prompt injections designed to manipulate AI reviewers should be flagged for desk rejection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0b45067-5dea-4e50-9b3d-c03e8aada9e0",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "dd1b7884-5011-450a-a4ea-2cee5469c1ef",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Reviewer Guidelines: Core Evaluation Framework\n\n## What Reviewers Should Evaluate\n\nReviewers assess papers across multiple dimensions:\n\n**Soundness**: Technical correctness and methodological validity. Reviews must justify soundness scores with evidence from the review text.\n\n**Excitement**: Personal interest level, kept separate from soundness assessment since subjective preferences shouldn't drive rejection.\n\n**Overall Recommendation**: A composite judgment reflecting soundness, novelty, impact, and potential contribution to the field.\n\n## Key Evaluation Criteria\n\n**Specificity Requirements**\nReviewers must be concrete. Instead of writing \"missing relevant references,\" identify specific works. Rather than stating \"X is unclear,\" explain what information is absent from the description.\n\n**Technical Soundness Assessment**\n- Verify mathematical formulations are correct\n- Check proof completeness and validity\n- Ensure experimental design supports claims\n- Validate statistical significance reporting\n- Confirm reproducibility details are sufficient\n\n**Novelty Evaluation**\nPapers need \"sufficient evidence for the claim that the authors are making\"—not necessarily state-of-the-art results. \"Highly similar work X and Y has been published [3+ months prior to submission deadline]\" constitutes plagiarism concern; otherwise, acknowledge that \"many findings seem obvious in retrospect, but community awareness differs.\"\n\n## Common Problematic Review Heuristics to Avoid\n\nReviewers should question whether they're applying bias rather than legitimate critique:\n\n- Dismissing findings as \"unsurprising\" despite lacking prior empirical validation\n- Rejecting work for methodological simplicity when simpler solutions are preferable\n- Requiring state-of-the-art results when contributions exist on other dimensions\n- Criticizing resource/analysis papers for lacking modeling novelty\n- Penalizing non-English research as less generalizable than English-only work\n\n## NLP-Specific Issues to Flag\n\n**Methodology Problems (M1-M5)**\n- LLM-only evaluation lacking reliability validation\n- Insufficient reproducibility details\n- Undisclosed data quality issues\n- Unmotivated model/benchmark selection\n- Incomplete mathematical assumptions or proofs\n\n**Result Interpretation Issues (R1-R5)**\n- Statistical problems or p-hacking\n- Claims exceeding evaluation scope\n- Speculation presented as conclusions\n- Overclaiming or misleading framing\n- Missing significance assessment\n\n**General Issues (G1-G5)**\n- Unclear research questions or contributions\n- Reliance on questionable precedents\n- Misrepresented or missing related work\n- Undefined key terminology\n- Misattributed or incorrect citations\n\n## Scoring Alignment Requirement\n\nLow soundness scores must correlate with identified technical flaws. If you rate a paper low without explaining substantial issues, your review lacks credibility. Conversely, papers can score high on soundness while receiving lower excitement scores.\n\n## Professional Standards\n\nReviews should maintain professional, neutral tone. The guidelines emphasize: \"Write the review you would like to get yourself.\" Sarcasm, dismissiveness, or insulting language violates peer review standards, particularly given anonymous reviewer power dynamics.\n\n## Resubmission-Specific Guidance\n\n**Repeat reviewers** should confirm authors addressed previous concerns, explicitly acknowledging their revision notes and explaining whether weaknesses were adequately resolved.\n\n**Substitute reviewers** distinguish between (i) previously identified weaknesses inadequately addressed, (ii) newly raised critical soundness issues, and (iii) other new suggestions for improvement.\n\n**Fresh reviewers** form independent assessments, then cross-reference with prior reviews to explain whether previous weaknesses persist despite revisions.\n\n## Confidentiality and Anonymity Rules\n\n- All submission and review information is strictly confidential\n- Don't submit manuscripts to third-party services, including non-privacy-preserving AI tools\n- Don't deliberately search for paper preprints to identify authors\n- If author identity becomes apparent, disclose this to the area chair\n- Postpone literature searches until after forming initial impressions\n\n## Generative AI Policy\n\nReviewers cannot use AI to draft reviews initially, though responsible editing assistance (especially for non-native speakers) is acceptable. Critically, \"neither reviewers nor editors may upload their peer review report into a non-privacy-preserving generative tool.\" Papers with hidden prompt injections designed to manipulate AI reviewers should be flagged for desk rejection.",
    "durationMs": 13998,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "d0b45067-5dea-4e50-9b3d-c03e8aada9e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-16T04:19:27.297Z_

```json
{
  "parentUuid": "dd1b7884-5011-450a-a4ea-2cee5469c1ef",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d42f3b60-ee7c-4147-9a17-edd1e9305514",
  "timestamp": "2026-05-16T04:19:27.297Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-16T04:19:34.409Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the ARR review form and guidelines. Now let me read all the paper sections in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d42f3b60-ee7c-4147-9a17-edd1e9305514",
  "isSidechain": false,
  "requestId": "req_011Cb5c3JmiYULv38aiosTyv",
  "type": "assistant",
  "uuid": "b3c186a7-1648-45cc-9dce-17252cab70f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4VCbKZST9khKu9p1eDX5N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 31214,
      "output_tokens": 822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 822,
          "cache_read_input_tokens": 31214,
          "cache_creation_input_tokens": 3351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3351
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-16T04:19:34.537Z_

ARR 评分标准已获取。现在并行读取论文所有章节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3c186a7-1648-45cc-9dce-17252cab70f3",
  "isSidechain": false,
  "requestId": "req_011Cb5c3JmiYULv38aiosTyv",
  "type": "assistant",
  "uuid": "670de17c-dfd0-4ef6-bdd3-1e34c6585e59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4VCbKZST9khKu9p1eDX5N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 31214,
      "output_tokens": 822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 822,
          "cache_read_input_tokens": 31214,
          "cache_creation_input_tokens": 3351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3351
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-16T04:19:35.168Z_

<details open><summary>🔧 Tool call — Read · `toolu_016ohXTag1yeYFBR5jJrjoBg`</summary>

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
  "parentUuid": "670de17c-dfd0-4ef6-bdd3-1e34c6585e59",
  "isSidechain": false,
  "requestId": "req_011Cb5c3JmiYULv38aiosTyv",
  "type": "assistant",
  "uuid": "a4f6262e-2b8d-4f27-b199-5b53baa647be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4VCbKZST9khKu9p1eDX5N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 31214,
      "output_tokens": 822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 822,
          "cache_read_input_tokens": 31214,
          "cache_creation_input_tokens": 3351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3351
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-16T04:19:38.935Z_

<details><summary>↩ Tool result · `toolu_017MzhT9dvPo8dsfq8urPZ8Z`</summary>

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
43	@inproceedings{eikema2022sampling,
44	  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},
45	  author = {Eikema, Bryan and Aziz, Wilker},
46	  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
47	  year = {2022},
48	  pages = {10978--10993},
49	  doi = {10.18653/v1/2022.emnlp-main.754}
50	}
51	
52	@article{freitag2022high,
53	  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},
54	  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},
55	  journal = {Transactions of the Association for Computational Linguistics},
56	  volume = {10},
57	  year = {2022},
58	  pages = {811--825},
59	  doi = {10.1162/tacl_a_00491}
60	}
61	
62	@article{fleiss1971agreement,
63	  title = {Measuring nominal scale agreement among many raters.},
64	  author = {Fleiss, Joseph L.},
65	  journal = {Psychological Bulletin},
66	  year = {1971},
67	  doi = {10.1037/h0031619},
68	  url = {http://dx.doi.org/10.1037/h0031619}
69	}
70	
71	@article{feng2025optimal,
72	  title = {Optimal Self-Consistency for Efficient Reasoning with Large Language Models},
73	  author = {Feng, Austin and Alonso, Marius and Odonnat, Ambroise},
74	  journal = {arXiv preprint arXiv:2511.12309},
75	  year = {2025},
76	  url = {https://arxiv.org/abs/2511.12309}
77	}
78	
79	@inproceedings{geng2024confidence,
80	  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},
81	  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},
82	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
83	  year = {2024},
84	  doi = {10.18653/v1/2024.naacl-long.366},
85	  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}
86	}
87	
88	@article{hobelsberger2025systematic,
89	  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},
90	  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},
91	  journal = {arXiv preprint arXiv:2510.20460},
92	  year = {2025},
93	  url = {https://arxiv.org/abs/2510.20460}
94	}
95	
96	@article{kadavath2022language,
97	  title = {Language Models (Mostly) Know What They Know},
98	  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},
99	  journal = {arXiv preprint arXiv:2207.05221},
100	  year = {2022},
101	  url = {https://arxiv.org/abs/2207.05221}
102	}
103	
104	@inproceedings{kang2025selfcertainty,
105	  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},
106	  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},
107	  booktitle = {NeurIPS 2025},
108	  year = {2025},
109	  url = {https://arxiv.org/abs/2502.18581}
110	}
111	
112	@inproceedings{kim2026reasc,
113	  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},
114	  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},
115	  booktitle = {ACL 2026},
116	  year = {2026},
117	  url = {https://arxiv.org/abs/2601.02970}
118	}
119	
120	@article{li2025llms,
121	  title = {LLMs Can Generate a Better Answer by Aggregating Their Own Responses},
122	  author = {Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi and Liang, Chen and Chen, Weizhu and Wang, Haoyu and Zhao, Tuo},
123	  journal = {arXiv preprint arXiv:2503.04104},
124	  year = {2025},
125	  url = {https://arxiv.org/abs/2503.04104}
126	}
127	
128	@inproceedings{kuhn2023semantic,
129	  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},
130	  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},
131	  booktitle = {ICLR 2023},
132	  year = {2023},
133	  url = {https://arxiv.org/abs/2302.09664}
134	}
135	
136	@inproceedings{malinin2021uncertainty,
137	  title = {Uncertainty Estimation in Autoregressive Structured Prediction},
138	  author = {Malinin, Andrey and Gales, Mark},
139	  booktitle = {International Conference on Learning Representations},
140	  year = {2021},
141	  url = {https://openreview.net/forum?id=jN5y-zb5Q7m}
142	}
143	
144	@inproceedings{li2023codeie,
145	  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
146	  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
147	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},
148	  year = {2023},
149	  doi = {10.18653/v1/2023.acl-long.855},
150	  url = {https://arxiv.org/abs/2305.05711}
151	}
152	
153	@inproceedings{lightman2024verify,
154	  title = {Let's Verify Step by Step},
155	  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
156	  booktitle = {ICLR 2024},
157	  year = {2024},
158	  url = {https://arxiv.org/abs/2305.20050}
159	}
160	
161	@inproceedings{luan2018scierc,
162	  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
163	  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
164	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
165	  year = {2018},
166	  doi = {10.18653/v1/D18-1360},
167	  url = {http://dx.doi.org/10.18653/v1/D18-1360}
168	}
169	
170	@inproceedings{manakul2023selfcheckgpt,
171	  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},
172	  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},
173	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
174	  year = {2023},
175	  doi = {10.18653/v1/2023.emnlp-main.557},
176	  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}
177	}
178	
179	@article{yao2026consistency,
180	  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},
181	  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},
182	  journal = {Genomics \& Informatics},
183	  year = {2026},
184	  doi = {10.1186/s44342-025-00063-2},
185	  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}
186	}
187	
188	@article{oh2025latentsc,
189	  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},
190	  author = {Oh, Jungsuk and Lee, Jay-Yoon},
191	  journal = {arXiv preprint arXiv:2508.18395},
192	  year = {2025},
193	  url = {https://arxiv.org/abs/2508.18395}
194	}
195	
196	@inproceedings{sainz2024gollie,
197	  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
198	  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},
199	  booktitle = {ICLR 2024},
200	  year = {2024},
201	  url = {https://arxiv.org/abs/2310.03668}
202	}
203	
204	@inproceedings{snell2025scaling,
205	  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},
206	  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
207	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
208	  year = {2025},
209	  url = {https://arxiv.org/abs/2408.03314}
210	}
211	
212	@inproceedings{taubenfeld2025cisc,
213	  title = {Confidence Improves Self-Consistency in LLMs},
214	  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},
215	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
216	  year = {2025},
217	  doi = {10.18653/v1/2025.findings-acl.1030},
218	  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}
219	}
220	
221	@inproceedings{thirukovalluru2024atomic,
222	  title = {Atomic Self-Consistency for Better Long Form Generations},
223	  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},
224	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
225	  year = {2024},
226	  doi = {10.18653/v1/2024.emnlp-main.706},
227	  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}
228	}
229	
230	@inproceedings{tjongkimsang2003conll,
231	  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},
232	  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},
233	  booktitle = {CoNLL 2003},
234	  year = {2003},
235	  url = {https://aclanthology.org/W03-0419/}
236	}
237	
238	@inproceedings{vashurin2025cocoa,
239	  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},
240	  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},
241	  booktitle = {NeurIPS 2025},
242	  year = {2025},
243	  url = {https://arxiv.org/abs/2502.04964}
244	}
245	
246	@inproceedings{wadhwa2023revisiting,
247	  title = {Revisiting Relation Extraction in the era of Large Language Models},
248	  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},
249	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
250	  year = {2023},
251	  doi = {10.18653/v1/2023.acl-long.868},
252	  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}
253	}
254	
255	@inproceedings{wang2023selfconsistency,
256	  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},
257	  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
258	  booktitle = {ICLR 2023},
259	  year = {2023},
260	  url = {https://arxiv.org/abs/2203.11171}
261	}
262	
263	@inproceedings{wang2025make,
264	  title = {Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning},
265	  author = {Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueqi and Tan, Chuyi and Pan, Boyuan and Hu, Yao and Li, Kan},
266	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
267	  pages = {6919--6932},
268	  year = {2025}
269	}
270	
271	@inproceedings{wang2025rankedvoting,
272	  title = {Ranked Voting based Self-Consistency of Large Language Models},
273	  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},
274	  booktitle = {ACL Findings 2025},
275	  year = {2025},
276	  url = {https://arxiv.org/abs/2505.10772}
277	}
278	
279	@article{willard2023guided,
280	  title = {Efficient Guided Generation for Large Language Models},
281	  author = {Willard, Brandon T. and Louf, Rémi},
282	  journal = {arXiv preprint arXiv:2307.09702},
283	  year = {2023},
284	  url = {https://arxiv.org/abs/2307.09702}
285	}
286	
287	@inproceedings{xia2025survey,
288	  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},
289	  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},
290	  booktitle = {ACL Findings 2025},
291	  year = {2025},
292	  url = {https://aclanthology.org/2025.findings-acl.1101/}
293	}
294	
295	@inproceedings{zheng2024llamafactory,
296	  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},
297	  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},
298	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},
299	  year = {2024},
300	  pages = {400--410},
301	  doi = {10.18653/v1/2024.acl-demos.38}
302	}
303	
304	@inproceedings{zhou2024uniner,
305	  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
306	  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
307	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
308	  year = {2024},
309	  url = {https://arxiv.org/abs/2308.03279}
310	}
311	
312	@inproceedings{muller2021understanding,
313	  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},
314	  author = {M{\"u}ller, Mathias and Sennrich, Rico},
315	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
316	  year = {2021},
317	  url = {https://arxiv.org/abs/2105.08504}
318	}
319	
320	@inproceedings{eikema2025structured,
321	  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},
322	  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},
323	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
324	  year = {2025},
325	  url = {https://arxiv.org/abs/2510.20700}
326	}
327	
328	@article{venktesh2025trust,
329	  title = {Trust but Verify! A Survey on Verification Design for Test-time Scaling},
330	  author = {Venktesh, V and Rathee, Mandeep and Anand, Avishek},
331	  journal = {arXiv preprint arXiv:2508.16665},
332	  year = {2025},
333	  url = {https://arxiv.org/abs/2508.16665}
334	}
335	
336	@inproceedings{jinnai2024mbr,
337	  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},
338	  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},
339	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
340	  year = {2024},
341	  url = {https://arxiv.org/abs/2311.05263}
342	}
343	
344	@inproceedings{ratinov2009design,
345	  title = {Design Challenges and Misconceptions in Named Entity Recognition},
346	  author = {Ratinov, Lev and Roth, Dan},
347	  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},
348	  year = {2009},
349	  pages = {147--155},
350	  publisher = {Association for Computational Linguistics}
351	}
352	
353	@inproceedings{bergkirkpatrick2012empirical,
354	  title = {An Empirical Investigation of Statistical Significance in {NLP}},
355	  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},
356	  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},
357	  year = {2012},
358	  pages = {995--1005},
359	  publisher = {Association for Computational Linguistics}
360	}
361	
362	@inproceedings{tian2023calibration,
363	  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models},
364	  author = {Tian, Katherine and Mitchell, Eric and Yao, Huaxiu and Manning, Christopher D. and Finn, Chelsea},
365	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
366	  year = {2023},
367	  pages = {1278--1294},
368	  publisher = {Association for Computational Linguistics}
369	}
370	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c305e3c0-5fb7-4bde-9dd7-88db6ad84cfe",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "490ae973-00d9-4947-8fad-6df8726a91a5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{culotta2004confidence,\n  title = {Confidence Estimation for Information Extraction},\n  author = {Culotta, Aron and McCallum, Andrew},\n  booktitle = {HLT-NAACL 2004},\n  year = {2004},\n  url = {https://aclanthology.org/N04-4028/}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {W-NUT Workshop at EMNLP 2017},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@article{feng2025optimal,\n  title = {Optimal Self-Consistency for Efficient Reasoning with Large Language Models},\n  author = {Feng, Austin and Alonso, Marius and Odonnat, Ambroise},\n  journal = {arXiv preprint arXiv:2511.12309},\n  year = {2025},\n  url = {https://arxiv.org/abs/2511.12309}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n@article{hobelsberger2025systematic,\n  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},\n  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},\n  journal = {arXiv preprint arXiv:2510.20460},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20460}\n}\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kim2026reasc,\n  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},\n  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},\n  booktitle = {ACL 2026},\n  year = {2026},\n  url = {https://arxiv.org/abs/2601.02970}\n}\n\n@article{li2025llms,\n  title = {LLMs Can Generate a Better Answer by Aggregating Their Own Responses},\n  author = {Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi and Liang, Chen and Chen, Weizhu and Wang, Haoyu and Zhao, Tuo},\n  journal = {arXiv preprint arXiv:2503.04104},\n  year = {2025},\n  url = {https://arxiv.org/abs/2503.04104}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {International Conference on Learning Representations},\n  year = {2021},\n  url = {https://openreview.net/forum?id=jN5y-zb5Q7m}\n}\n\n@inproceedings{li2023codeie,\n  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.855},\n  url = {https://arxiv.org/abs/2305.05711}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@article{oh2025latentsc,\n  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},\n  author = {Oh, Jungsuk and Lee, Jay-Yoon},\n  journal = {arXiv preprint arXiv:2508.18395},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.18395}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {CoNLL 2003},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{vashurin2025cocoa,\n  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},\n  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.04964}\n}\n\n@inproceedings{wadhwa2023revisiting,\n  title = {Revisiting Relation Extraction in the era of Large Language Models},\n  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.868},\n  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@inproceedings{wang2025make,\n  title = {Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning},\n  author = {Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueqi and Tan, Chuyi and Pan, Boyuan and Hu, Yao and Li, Kan},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},\n  pages = {6919--6932},\n  year = {2025}\n}\n\n@inproceedings{wang2025rankedvoting,\n  title = {Ranked Voting based Self-Consistency of Large Language Models},\n  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.10772}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@article{venktesh2025trust,\n  title = {Trust but Verify! A Survey on Verification Design for Test-time Scaling},\n  author = {Venktesh, V and Rathee, Mandeep and Anand, Avishek},\n  journal = {arXiv preprint arXiv:2508.16665},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.16665}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models},\n  author = {Tian, Katherine and Mitchell, Eric and Yao, Huaxiu and Manning, Christopher D. and Finn, Chelsea},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {1278--1294},\n  publisher = {Association for Computational Linguistics}\n}\n",
      "numLines": 370,
      "startLine": 1,
      "totalLines": 370
    }
  },
  "sourceToolAssistantUUID": "c305e3c0-5fb7-4bde-9dd7-88db6ad84cfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-16T04:19:35.176Z_

<details><summary>↩ Tool result · `toolu_016ohXTag1yeYFBR5jJrjoBg`</summary>

```text
1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but information extraction (IE) produces \textit{sets} of entities and relations with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals across NER and RE benchmarks at two model scales (4B and 8B).
4	All signals achieve strong quality estimation (Spearman $\rho$ up to 0.45), yet none improves best-of-$N$ selection despite substantial oracle headroom---the \textit{correlation-selection gap}.
5	Four instance-level signals fail by construction; the empirical finding is that log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats, 60\% tied).
6	A 4-seed free-form decoding ablation confirms NER compression is not an artifact of constrained decoding; on RE, LP selection reverses direction under free-form decoding ($+1.8{\pm}0.1$~pp; preliminary, single benchmark), suggesting regime-dependent behavior.
7	Consensus-proximity selection (MBR) correlates with F1 across instances but not within them.
8	Signal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4f6262e-2b8d-4f27-b199-5b53baa647be",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "06dcb36d-8087-467a-be3b-b4e81ef8d66c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nSelf-consistency yields large gains on discrete-answer tasks, but information extraction (IE) produces \\textit{sets} of entities and relations with partial overlap, where no majority vote analog exists.\nWe evaluate five confidence signals across NER and RE benchmarks at two model scales (4B and 8B).\nAll signals achieve strong quality estimation (Spearman $\\rho$ up to 0.45), yet none improves best-of-$N$ selection despite substantial oracle headroom---the \\textit{correlation-selection gap}.\nFour instance-level signals fail by construction; the empirical finding is that log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats, 60\\% tied).\nA 4-seed free-form decoding ablation confirms NER compression is not an artifact of constrained decoding; on RE, LP selection reverses direction under free-form decoding ($+1.8{\\pm}0.1$~pp; preliminary, single benchmark), suggesting regime-dependent behavior.\nConsensus-proximity selection (MBR) correlates with F1 across instances but not within them.\nSignal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.\n\\end{abstract}\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "a4f6262e-2b8d-4f27-b199-5b53baa647be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-16T04:19:35.640Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MPxNmhf3Sdrat3wc6p9ADp`</summary>

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
  "parentUuid": "06dcb36d-8087-467a-be3b-b4e81ef8d66c",
  "isSidechain": false,
  "requestId": "req_011Cb5c3JmiYULv38aiosTyv",
  "type": "assistant",
  "uuid": "275fb47e-d639-441a-990e-56450b9c70b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4VCbKZST9khKu9p1eDX5N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 31214,
      "output_tokens": 822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 822,
          "cache_read_input_tokens": 31214,
          "cache_creation_input_tokens": 3351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3351
          },
          "type": "message"
        }
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

_source line 43 · 2026-05-16T04:19:35.650Z_

<details><summary>↩ Tool result · `toolu_01MPxNmhf3Sdrat3wc6p9ADp`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But information extraction (IE) poses a structurally different challenge: the output is a \textit{set} of entities or relations, two samples may extract overlapping but non-identical structures, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE; we extend their work with structural matching, selection analysis, and a difficulty gradient.
9	
10	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency signals achieve strong quality estimation ($\rho$ up to 0.45) but fail at sample selection despite substantial oracle headroom.
11	Instance-level signals (4 of 5) fail by construction---they assign identical scores to all candidates.
12	The empirical contribution concerns log-probability (LP), the only per-sample signal: LP scores are too compressed within instances to discriminate (median range 0.041 nats; \S\ref{sec:discussion}), and consensus-proximity selection (MBR) fails because utility correlates with F1 across instances but not within them.
13	
14	\begin{figure*}[t]
15	\centering
16	\includegraphics[width=\textwidth]{fig_overview}
17	\caption{The correlation-selection gap. \textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection.}
18	\label{fig:overview}
19	\end{figure*}
20	
21	We evaluate five signals from three families---structural, surface, and model-internal---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).
22	Our contributions:
23	\begin{enumerate}
24	    \item \textbf{Metric dissociation.}
25	    Quality estimation, binary discrimination, and sample selection decouple; single-metric evaluation risks selecting the wrong signal.
26	
27	    \item \textbf{LP compression and MBR failure.}
28	    Log-probability, the only per-sample signal, is too compressed within instances to select (median range 0.041 nats, 60\% tied); consensus-proximity selection (MBR) correlates with F1 across instances but not within them. A 4-seed free-form ablation confirms compression is not caused by constrained decoding.
29	
30	    \item \textbf{Difficulty- and task-dependent signal rankings.}
31	    Rankings shift with task complexity and collapse at the capability boundary. RE conclusions rest on SciERC alone (preliminary).
32	\end{enumerate}
33	
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "275fb47e-d639-441a-990e-56450b9c70b3",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "31222557-6b73-45f5-9bf0-bb92652e6174",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \\citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \\cite{snell2025scaling, brown2024monkeys}.\nBut information extraction (IE) poses a structurally different challenge: the output is a \\textit{set} of entities or relations, two samples may extract overlapping but non-identical structures, and there is no obvious majority to vote on.\n\nPrior work on confidence estimation for LLM-based IE has conflated \\textit{quality estimation} (which inputs does the model handle reliably?) with \\textit{sample selection} (which of $N$ outputs is best?).\nExisting self-consistency methods \\cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\n\\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE; we extend their work with structural matching, selection analysis, and a difficulty gradient.\n\nOur central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency signals achieve strong quality estimation ($\\rho$ up to 0.45) but fail at sample selection despite substantial oracle headroom.\nInstance-level signals (4 of 5) fail by construction---they assign identical scores to all candidates.\nThe empirical contribution concerns log-probability (LP), the only per-sample signal: LP scores are too compressed within instances to discriminate (median range 0.041 nats; \\S\\ref{sec:discussion}), and consensus-proximity selection (MBR) fails because utility correlates with F1 across instances but not within them.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. \\textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \\textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection.}\n\\label{fig:overview}\n\\end{figure*}\n\nWe evaluate five signals from three families---structural, surface, and model-internal---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).\nOur contributions:\n\\begin{enumerate}\n    \\item \\textbf{Metric dissociation.}\n    Quality estimation, binary discrimination, and sample selection decouple; single-metric evaluation risks selecting the wrong signal.\n\n    \\item \\textbf{LP compression and MBR failure.}\n    Log-probability, the only per-sample signal, is too compressed within instances to select (median range 0.041 nats, 60\\% tied); consensus-proximity selection (MBR) correlates with F1 across instances but not within them. A 4-seed free-form ablation confirms compression is not caused by constrained decoding.\n\n    \\item \\textbf{Difficulty- and task-dependent signal rankings.}\n    Rankings shift with task complexity and collapse at the capability boundary. RE conclusions rest on SciERC alone (preliminary).\n\\end{enumerate}\n\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  },
  "sourceToolAssistantUUID": "275fb47e-d639-441a-990e-56450b9c70b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-16T04:19:36.093Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RsfxiLi7A8wz2jPWWiMeRC`</summary>

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
  "parentUuid": "31222557-6b73-45f5-9bf0-bb92652e6174",
  "isSidechain": false,
  "requestId": "req_011Cb5c3JmiYULv38aiosTyv",
  "type": "assistant",
  "uuid": "398450e7-eae0-4c52-83c8-4fb565174eaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4VCbKZST9khKu9p1eDX5N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 31214,
      "output_tokens": 822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 822,
          "cache_read_input_tokens": 31214,
          "cache_creation_input_tokens": 3351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3351
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-16T04:19:36.105Z_

<details><summary>↩ Tool result · `toolu_01RsfxiLi7A8wz2jPWWiMeRC`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2025latentsc} all target discrete answers.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.
12	\citet{culotta2004confidence} pioneer confidence estimation for IE via CRF marginals; our signals are model-agnostic.
13	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided}.
14	
15	\paragraph{Uncertainty estimation and calibration.}
16	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs.
17	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; P(True) \cite{kadavath2022language} queries model confidence directly; \citet{malinin2021uncertainty} study predictive uncertainty for autoregressive structured prediction.
18	Our structural signals instead measure agreement over output \textit{structure}, requiring no model modification.
19	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling} with structural utility functions.
20	\citet{eikema2025structured} find that standard MBR utilities degrade on structured outputs due to bag-of-unit mismatches---consistent with our finding that consensus-proximity selection fails for IE; we show the specific failure: utility correlates with F1 across instances but not within them (\S\ref{sec:discussion}).
21	Trained verifiers \cite{cobbe2021verifiers, lightman2024verify} learn per-sample scoring that may bridge this gap.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "398450e7-eae0-4c52-83c8-4fb565174eaf",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "aef101e9-89b3-42a6-b8c6-a0727b4ca84d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency \\cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \\cite{chen2024usc}, sub-claim decomposition \\cite{thirukovalluru2024atomic}, or hallucination detection \\cite{manakul2023selfcheckgpt}.\nTest-time scaling studies \\cite{snell2025scaling, brown2024monkeys} and reward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2025latentsc} all target discrete answers.\nConcurrently, \\citet{feng2025optimal} and \\citet{wang2025make} adapt self-consistency to difficulty-aware settings; \\citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.\nOur work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.\n\n\\paragraph{Consistency for structured IE.}\n\\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.\nCoCoA \\cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.\n\\citet{culotta2004confidence} pioneer confidence estimation for IE via CRF marginals; our signals are model-agnostic.\nOur evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \\cite{willard2023guided}.\n\n\\paragraph{Uncertainty estimation and calibration.}\nSurveys cover confidence estimation \\cite{geng2024confidence}, uncertainty quantification \\cite{xia2025survey}, and calibration \\cite{hobelsberger2025systematic} for LLMs.\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; P(True) \\cite{kadavath2022language} queries model confidence directly; \\citet{malinin2021uncertainty} study predictive uncertainty for autoregressive structured prediction.\nOur structural signals instead measure agreement over output \\textit{structure}, requiring no model modification.\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling} with structural utility functions.\n\\citet{eikema2025structured} find that standard MBR utilities degrade on structured outputs due to bag-of-unit mismatches---consistent with our finding that consensus-proximity selection fails for IE; we show the specific failure: utility correlates with F1 across instances but not within them (\\S\\ref{sec:discussion}).\nTrained verifiers \\cite{cobbe2021verifiers, lightman2024verify} learn per-sample scoring that may bridge this gap.\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  },
  "sourceToolAssistantUUID": "398450e7-eae0-4c52-83c8-4fb565174eaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-16T04:19:36.845Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HsUGTjsdjWV8vf6Dyrqq1E`</summary>

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
  "parentUuid": "aef101e9-89b3-42a6-b8c6-a0727b4ca84d",
  "isSidechain": false,
  "requestId": "req_011Cb5c3JmiYULv38aiosTyv",
  "type": "assistant",
  "uuid": "ccfb5387-bb36-41f7-8089-901a063247dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4VCbKZST9khKu9p1eDX5N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 31214,
      "output_tokens": 822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 822,
          "cache_read_input_tokens": 31214,
          "cache_creation_input_tokens": 3351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3351
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-16T04:19:36.854Z_

<details><summary>↩ Tool result · `toolu_01HsUGTjsdjWV8vf6Dyrqq1E`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set (NER) or relation set (RE).
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	
8	\subsection{Confidence Signals}\label{sec:signals}
9	
10	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
11	
12	\paragraph{Log-probability (model-internal, per-sample).}
13	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
14	\begin{equation}\label{eq:logprob}
15	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{&lt;j}, x)
16	\end{equation}
17	
18	\paragraph{Exact match voting (surface, instance-level).}
19	The proportion of samples producing the most common output:
20	\begin{equation}\label{eq:em}
21	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
22	\end{equation}
23	
24	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
25	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
26	\begin{equation}\label{eq:fk}
27	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
28	\end{equation}
29	where $\bar{P}$ is mean observed and $\bar{P}_e$ expected agreement.
30	Temperature-based sampling introduces mild negative dependence ($-$0.4\% to $-$4.0\%; Appendix~\ref{app:fk_independence}), which does not inflate FK.
31	Unlike structural signals, FK relies on exact string matching.
32	
33	\paragraph{Soft Jaccard (structural, instance-level).}
34	For samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU), and define:
35	\begin{equation}\label{eq:sj}
36	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
37	\end{equation}
38	where $M$ is the matched set, $\text{sim}(a_m, b_m)$ is the token-level IoU between matched spans, and $\max(|g_i|, |g_j|)$ penalizes length asymmetry.
39	The instance-level signal averages over all pairs:
40	\begin{equation}\label{eq:sj_instance}
41	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i&lt;j} \text{SJ}(y_i, y_j)
42	\end{equation}
43	
44	\paragraph{Entity voting confidence (structural, instance-level).}
45	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
46	The instance-level confidence is the mean frequency:
47	\begin{equation}\label{eq:voting}
48	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
49	\end{equation}
50	When $E_\cup = \emptyset$, we set $c_{\mathrm{vc}}(x) = 0$.\footnote{Equation~\ref{eq:voting} defines the continuous QE signal; for voted-output \textit{selection} (Table~\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting.}
51	
52	\subsection{Evaluation Framework}\label{sec:evaluation}
53	
54	\paragraph{Quality estimation.}
55	Spearman $\rho$ between the signal and instance-level F1, and AUROC classifying instances as above/below median F1.
56	Correlation analyses exclude empty gold annotations ($n{=}529$ on SciERC after filtering 22/551); selection retains the full set ($n{=}551$).
57	
58	\paragraph{Sample selection.}
59	Best-of-$N$ F1: per-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to consensus.
60	Baselines: \textit{oracle} (highest-F1 sample) and \textit{greedy} (a single $T{=}1.0$ sample, not argmax decoding).
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ccfb5387-bb36-41f7-8089-901a063247dd",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "cdbb187d-8e5f-4523-87fe-4c92af095c64",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven model $\\mathcal{M}$ and input $x$, we sample $N$ outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}, where each $y_i$ is an entity set (NER) or relation set (RE).\nA \\textbf{per-sample signal} $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$ scores each output independently; an \\textbf{instance-level signal} $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$ produces a single score per input (notation in Appendix~\\ref{app:notation}).\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nFour are \\textit{consistency signals}: \\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \\textit{surface} (exact match [EM], Fleiss' $\\kappa$ [FK]); log-probability [LP] is the sole \\textit{model-internal}, per-sample signal.\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{&lt;j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed and $\\bar{P}_e$ expected agreement.\nTemperature-based sampling introduces mild negative dependence ($-$0.4\\% to $-$4.0\\%; Appendix~\\ref{app:fk_independence}), which does not inflate FK.\nUnlike structural signals, FK relies on exact string matching.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nFor samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU), and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set, $\\text{sim}(a_m, b_m)$ is the token-level IoU between matched spans, and $\\max(|g_i|, |g_j|)$ penalizes length asymmetry.\nThe instance-level signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i&lt;j} \\text{SJ}(y_i, y_j)\n\\end{equation}\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\nWhen $E_\\cup = \\emptyset$, we set $c_{\\mathrm{vc}}(x) = 0$.\\footnote{Equation~\\ref{eq:voting} defines the continuous QE signal; for voted-output \\textit{selection} (Table~\\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting.}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nSpearman $\\rho$ between the signal and instance-level F1, and AUROC classifying instances as above/below median F1.\nCorrelation analyses exclude empty gold annotations ($n{=}529$ on SciERC after filtering 22/551); selection retains the full set ($n{=}551$).\n\n\\paragraph{Sample selection.}\nBest-of-$N$ F1: per-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to consensus.\nBaselines: \\textit{oracle} (highest-F1 sample) and \\textit{greedy} (a single $T{=}1.0$ sample, not argmax decoding).\n",
      "numLines": 61,
      "startLine": 1,
      "totalLines": 61
    }
  },
  "sourceToolAssistantUUID": "ccfb5387-bb36-41f7-8089-901a063247dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-16T04:19:37.709Z_

<details open><summary>🔧 Tool call — Read · `toolu_016MUiT7Ft8gvKYhx2wQbd1U`</summary>

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
  "parentUuid": "cdbb187d-8e5f-4523-87fe-4c92af095c64",
  "isSidechain": false,
  "requestId": "req_011Cb5c3JmiYULv38aiosTyv",
  "type": "assistant",
  "uuid": "7f8fb617-3080-4fff-bcbe-4169e99d86e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4VCbKZST9khKu9p1eDX5N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 31214,
      "output_tokens": 822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 822,
          "cache_read_input_tokens": 31214,
          "cache_creation_input_tokens": 3351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3351
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-16T04:19:37.717Z_

<details><summary>↩ Tool result · `toolu_016MUiT7Ft8gvKYhx2wQbd1U`</summary>

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
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation ($\rho$ and AUROC; $N{=}8$, seed${=}42$, single-seed; 3-seed stability in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE: preliminary. $N{=}16$ in Table~\ref{tab:robustness}.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
31	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
32	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
33	\midrule
34	VC & Structural & \textbf{.379} & \textbf{.663} & \textbf{.350} & .694 & .424 & .789 & .426 & .709 \\
35	SJ  & Structural & .360 & .650 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
36	FK & Surface & .267 & .602 & .275 & .609 & .400 & .774 & .428 & .703 \\
37	EM  & Surface    & .295 & .614 & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
38	\midrule
39	LP     & Model      & .205 & .578 & .266 & .601 & .316 & .753 & .307 & \textbf{.761} \\
40	\bottomrule
41	\end{tabular}
42	\end{table*}
43	
44	Table~\ref{tab:quality_estimation} presents $\rho$ and AUROC for five signals across tasks and models.\footnote{$\varepsilon{=}0.05$ applies only to selection (\S\ref{sec:selection_gap}); quality estimation is $\varepsilon$-free. Selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}).}
45	
46	\paragraph{Signal rankings are difficulty-dependent.}
47	On SciERC NER, structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over surface ($\rho{\leq}0.295$) and LP ($0.205$); bootstrap CIs confirm the SJ--LP gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
48	On CoNLL (greedy F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$); the $\rho$--AUROC dissociation across datasets reflects use-case alignment.
49	On RE (preliminary), LP rises above SJ and FK at $N{=}16$ (Table~\ref{tab:multiseed}).
50	At the capability boundary---WNUT-17 (52\% zero F1)---all conditional signals collapse (Table~\ref{tab:wnut}); restricting to non-zero instances reshuffles rankings, with EM strongest on NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$; preliminary) while LP RE collapses to $\rho{=}0.011$ (preliminary) (Figure~\ref{fig:signal_heatmap}, Appendix~\ref{app:additional}).
51	
52	%% ============================================================
53	\subsection{The Correlation-Selection Gap}
54	\label{sec:selection_gap}
55	
56	We define the correlation-selection gap as the disparity between a signal's instance-level rank correlation with F1 and its ability to select the best output from $N$ candidates.
57	
58	\begin{table}[t]
59	\centering
60	\small
61	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). LP is per-sample; others are instance-level. NER: 2-seed mean${\pm}\sigma$, Fisher $p$ vs.\ greedy; RE: single seed (preliminary). Best non-oracle in \textbf{bold}. $^\dagger$Greedy: $T{=}1.0$ sample.}
62	\label{tab:selection}
63	\begin{tabular}{lccc}
64	\toprule
65	Method & NER F1 & $p$ & RE F1 \\
66	\midrule
67	Oracle & $0.778 \pm 0.003$ & --- & 0.585 \\
68	\midrule
69	\multicolumn{4}{l}{\textit{Per-sample signal}} \\
70	LP           & $\mathbf{0.647} \pm 0.005$ & .29 & 0.395 \\
71	\midrule
72	\multicolumn{4}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
73	SJ           & $0.646 \pm 0.002$ & .68 & 0.386 \\
74	FK           & $0.646 \pm 0.001$ & .79 & --- \\
75	EM           & $0.637 \pm 0.001$ & .45 & 0.372 \\
76	VC           & $0.623 \pm 0.004$ & .26 & 0.359 \\
77	\midrule
78	Greedy$^\dagger$ & $0.645 \pm 0.001$ & --- & \textbf{0.404} \\
79	Random           & $0.610 \pm 0.003$ & --- & 0.354 \\
80	\bottomrule
81	\end{tabular}
82	\end{table}
83	
84	Despite strong quality estimation, confidence signals yield limited selection gains (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
85	Instance-level signals (SJ, FK, EM, VC) assign identical scores to all candidates per input and cannot rank outputs by construction; the key question is whether LP---the only per-sample signal---can exploit the oracle headroom.
86	
87	\paragraph{No significant improvement over greedy.}
88	On SciERC NER (2-seed sign tests, $n{=}551$), the oracle (0.778) reveals 13.3~pp of headroom above greedy (0.645), yet LP achieves only 0.647 ($\Delta{=}{+}0.2$~pp, $p{=}0.29$); no signal consistently improves selection ($p{>}0.05$; TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration, Appendix~\ref{app:tost}).
89	On RE, the best signal (LP, 0.395) falls below greedy (0.404; preliminary), with 18.1~pp unrealized.
90	The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}).
91	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best; closing this gap likely requires trained verifiers \cite{cobbe2021verifiers}.\footnote{For negative results (all $p{>}0.05$), uncorrected tests suffice; the sole positive finding (non-tied LP subset, $+2.9$~pp, $p{=}0.004$; \S\ref{sec:discussion}) survives Bonferroni correction over 5 comparisons.}
92	
93	%% ============================================================
94	\subsection{Robustness}
95	\label{sec:robustness_main}
96	
97	Consistency signals are robust across $T{\in}\{0.7, 1.0\}$ with sublinear $N$-scaling gains (Table~\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\Delta\rho{=}{+}0.044$).
98	NER calibration is reasonable (ECE 0.069--0.096); RE miscalibration (ECE${\leq}$0.339, preliminary) caps $\rho$ at ${\approx}0.28$ for $N{=}16$ (Appendix~\ref{app:calibration}).
99	
100	\begin{table}[t]
101	\centering
102	\small
103	\caption{Scale ablation: Qwen3-8B vs.\ 4B quality estimation ($\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. $^\dagger$Preliminary.}
104	\label{tab:scale_ablation}
105	\begin{tabular}{@{}ll cc r@{}}
106	\toprule
107	& & \textbf{8B} & \textbf{4B} & $\Delta$ \\
108	\midrule
109	CoNLL NER & SJ & .436 & .422 & $-$.014 \\
110	          & FK & .400 & .418 & $+$.018 \\
111	SciERC NER & SJ & .360 & .422 & $+$.062 \\
112	           & FK & .267 & .326 & $+$.059 \\
113	SciERC RE$^\dagger$ & SJ & .250 & .267 & $+$.017 \\
114	           & FK & .275 & .359 & $+$.084 \\
115	\bottomrule
116	\end{tabular}
117	\end{table}
118	
119	\paragraph{Scale robustness.}
120	Repeating with Qwen3-4B (Table~\ref{tab:scale_ablation}), quality estimation is comparable or improved (mean $|\Delta\rho|{=}0.042$), yet selection remains below greedy on SciERC ($\Delta$ up to $-3.4$~pp) despite 13.0~pp of oracle headroom, and indistinguishable on CoNLL (${<}0.3$~pp, 1.7~pp headroom). Within the 3B--8B range tested across two model families, task difficulty appears to be the primary driver of the gap.
121	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f8fb617-3080-4fff-bcbe-4169e99d86e9",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "fd9c0edf-f8dd-41bf-846f-5c6820243706",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures.\nQwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\\ref{app:thinking_token}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\\ref{app:n_scaling}).}\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation ($\\rho$ and AUROC; $N{=}8$, seed${=}42$, single-seed; 3-seed stability in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. RE: preliminary. $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & \\textbf{.350} & .694 & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .266 & .601 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models.\\footnote{$\\varepsilon{=}0.05$ applies only to selection (\\S\\ref{sec:selection_gap}); quality estimation is $\\varepsilon$-free. Selection F1 is stable across $\\varepsilon \\in [0, 0.2]$ (Appendix~\\ref{app:epsilon_robustness}).}\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC NER, structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over surface ($\\rho{\\leq}0.295$) and LP ($0.205$); bootstrap CIs confirm the SJ--LP gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (greedy F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$); the $\\rho$--AUROC dissociation across datasets reflects use-case alignment.\nOn RE (preliminary), LP rises above SJ and FK at $N{=}16$ (Table~\\ref{tab:multiseed}).\nAt the capability boundary---WNUT-17 (52\\% zero F1)---all conditional signals collapse (Table~\\ref{tab:wnut}); restricting to non-zero instances reshuffles rankings, with EM strongest on NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$; preliminary) while LP RE collapses to $\\rho{=}0.011$ (preliminary) (Figure~\\ref{fig:signal_heatmap}, Appendix~\\ref{app:additional}).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nWe define the correlation-selection gap as the disparity between a signal's instance-level rank correlation with F1 and its ability to select the best output from $N$ candidates.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). LP is per-sample; others are instance-level. NER: 2-seed mean${\\pm}\\sigma$, Fisher $p$ vs.\\ greedy; RE: single seed (preliminary). Best non-oracle in \\textbf{bold}. $^\\dagger$Greedy: $T{=}1.0$ sample.}\n\\label{tab:selection}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & NER F1 & $p$ & RE F1 \\\\\n\\midrule\nOracle & $0.778 \\pm 0.003$ & --- & 0.585 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 & 0.395 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .68 & 0.386 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 & --- \\\\\nEM           & $0.637 \\pm 0.001$ & .45 & 0.372 \\\\\nVC           & $0.623 \\pm 0.004$ & .26 & 0.359 \\\\\n\\midrule\nGreedy$^\\dagger$ & $0.645 \\pm 0.001$ & --- & \\textbf{0.404} \\\\\nRandom           & $0.610 \\pm 0.003$ & --- & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited selection gains (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nInstance-level signals (SJ, FK, EM, VC) assign identical scores to all candidates per input and cannot rank outputs by construction; the key question is whether LP---the only per-sample signal---can exploit the oracle headroom.\n\n\\paragraph{No significant improvement over greedy.}\nOn SciERC NER (2-seed sign tests, $n{=}551$), the oracle (0.778) reveals 13.3~pp of headroom above greedy (0.645), yet LP achieves only 0.647 ($\\Delta{=}{+}0.2$~pp, $p{=}0.29$); no signal consistently improves selection ($p{>}0.05$; TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration, Appendix~\\ref{app:tost}).\nOn RE, the best signal (LP, 0.395) falls below greedy (0.404; preliminary), with 18.1~pp unrealized.\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}).\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best; closing this gap likely requires trained verifiers \\cite{cobbe2021verifiers}.\\footnote{For negative results (all $p{>}0.05$), uncorrected tests suffice; the sole positive finding (non-tied LP subset, $+2.9$~pp, $p{=}0.004$; \\S\\ref{sec:discussion}) survives Bonferroni correction over 5 comparisons.}\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\\Delta\\rho{=}{+}0.044$).\nNER calibration is reasonable (ECE 0.069--0.096); RE miscalibration (ECE${\\leq}$0.339, preliminary) caps $\\rho$ at ${\\approx}0.28$ for $N{=}16$ (Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: Qwen3-8B vs.\\ 4B quality estimation ($\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. $^\\dagger$Preliminary.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL NER & SJ & .436 & .422 & $-$.014 \\\\\n          & FK & .400 & .418 & $+$.018 \\\\\nSciERC NER & SJ & .360 & .422 & $+$.062 \\\\\n           & FK & .267 & .326 & $+$.059 \\\\\nSciERC RE$^\\dagger$ & SJ & .250 & .267 & $+$.017 \\\\\n           & FK & .275 & .359 & $+$.084 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nRepeating with Qwen3-4B (Table~\\ref{tab:scale_ablation}), quality estimation is comparable or improved (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below greedy on SciERC ($\\Delta$ up to $-3.4$~pp) despite 13.0~pp of oracle headroom, and indistinguishable on CoNLL (${<}0.3$~pp, 1.7~pp headroom). Within the 3B--8B range tested across two model families, task difficulty appears to be the primary driver of the gap.\n",
      "numLines": 121,
      "startLine": 1,
      "totalLines": 121
    }
  },
  "sourceToolAssistantUUID": "7f8fb617-3080-4fff-bcbe-4169e99d86e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-16T04:19:38.175Z_

<details open><summary>🔧 Tool call — Read · `toolu_019A3rP5y3S6APn5ze2feaoK`</summary>

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
  "parentUuid": "fd9c0edf-f8dd-41bf-846f-5c6820243706",
  "isSidechain": false,
  "requestId": "req_011Cb5c3JmiYULv38aiosTyv",
  "type": "assistant",
  "uuid": "5bf93190-a38f-4e8d-bd29-7eddc4344769",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4VCbKZST9khKu9p1eDX5N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 31214,
      "output_tokens": 822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 822,
          "cache_read_input_tokens": 31214,
          "cache_creation_input_tokens": 3351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3351
          },
          "type": "message"
        }
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

_source line 51 · 2026-05-16T04:19:38.180Z_

<details><summary>↩ Tool result · `toolu_019A3rP5y3S6APn5ze2feaoK`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	VC leads on hard NER ($\rho{=}0.379$); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on RE (preliminary), LP outperforms structural signals (Table~\ref{tab:multiseed}).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.
6	
7	\paragraph{Why the gap exists.}
8	Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
9	Log-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\ref{tab:logprob_ties}).
10	Where compression is mitigated ($n{=}210$ instances with above-median spread), LP selection outperforms greedy ($+2.9$~pp, $p{=}0.004$), confirming compression as the bottleneck; the gap holds even among high-diversity instances (Appendix~\ref{app:diversity}).
11	Doubling to $N{=}16$ expands oracle headroom by $+4.4$~pp without improving selection; on RE at 4B scale (preliminary), LP is the sole positive signal ($\Delta{=}{+}0.7$~pp, $p{=}0.058$; Table~\ref{tab:re_n16_selection}), consistent with LP being the strongest RE selection signal across scales, though still below greedy at 8B.
12	A verbalized confidence baseline confirms that score compression is not LP-specific: the model's self-rated confidence (mean 8.6/10) is even more compressed and yields the weakest selection (Appendix~\ref{app:verbalized_confidence}).
13	
14	\paragraph{Ablation: free-form decoding.}\label{sec:ablation}
15	Removing grammar constraints (SciERC NER, Qwen3-8B, 4 seeds) yields nearly identical LP distributions (std ratio 0.97) and negligible selection changes (Appendix~\ref{app:freeform_ablation}), ruling out constrained decoding as the cause of NER compression.
16	On RE, LP selection consistently reverses direction under free-form decoding ($+1.8{\pm}0.1$~pp, 4 seeds; Appendix~\ref{app:freeform_ablation}), while under constrained decoding LP falls below greedy ($-0.9$~pp at 8B).
17	RE LP selection is thus regime-dependent: constrained decoding suppresses it, free-form decoding recovers it, and at 4B $N{=}16$ it is marginally positive ($+0.7$~pp, $p{=}0.058$).
18	This pattern is preliminary (single RE benchmark, 40\% zero-F1 rate).
19	VC becomes per-sample in the selection context (each candidate's overlap with the majority-voted output varies), yet tends to select the most typical rather than the best output---consistent with MBR's known mode-seeking bias \cite{eikema2022sampling}.
20	More broadly, all consensus-proximity strategies fail because utility correlates with F1 across instances but not within them (Appendix~\ref{app:mbr_discussion}).
21	
22	\paragraph{Methodological implications.}
23	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal.
24	Effective selection likely requires trained verifiers \cite{cobbe2021verifiers, venktesh2025trust}; $N{=}8$ captures most quality estimation benefit (Appendix~\ref{app:n_scaling}).
25	Structural signals are robust to domain shift when the training schema subsumes the target (Appendix~\ref{app:ood}).
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bf93190-a38f-4e8d-bd29-7eddc4344769",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "d2ae6040-534d-440d-a606-4c82560fdd29",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nVC leads on hard NER ($\\rho{=}0.379$); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on RE (preliminary), LP outperforms structural signals (Table~\\ref{tab:multiseed}).\nRankings hold across model families and a 4B ablation (Table~\\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.\n\n\\paragraph{Why the gap exists.}\nFour of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nLog-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\\ref{tab:logprob_ties}).\nWhere compression is mitigated ($n{=}210$ instances with above-median spread), LP selection outperforms greedy ($+2.9$~pp, $p{=}0.004$), confirming compression as the bottleneck; the gap holds even among high-diversity instances (Appendix~\\ref{app:diversity}).\nDoubling to $N{=}16$ expands oracle headroom by $+4.4$~pp without improving selection; on RE at 4B scale (preliminary), LP is the sole positive signal ($\\Delta{=}{+}0.7$~pp, $p{=}0.058$; Table~\\ref{tab:re_n16_selection}), consistent with LP being the strongest RE selection signal across scales, though still below greedy at 8B.\nA verbalized confidence baseline confirms that score compression is not LP-specific: the model's self-rated confidence (mean 8.6/10) is even more compressed and yields the weakest selection (Appendix~\\ref{app:verbalized_confidence}).\n\n\\paragraph{Ablation: free-form decoding.}\\label{sec:ablation}\nRemoving grammar constraints (SciERC NER, Qwen3-8B, 4 seeds) yields nearly identical LP distributions (std ratio 0.97) and negligible selection changes (Appendix~\\ref{app:freeform_ablation}), ruling out constrained decoding as the cause of NER compression.\nOn RE, LP selection consistently reverses direction under free-form decoding ($+1.8{\\pm}0.1$~pp, 4 seeds; Appendix~\\ref{app:freeform_ablation}), while under constrained decoding LP falls below greedy ($-0.9$~pp at 8B).\nRE LP selection is thus regime-dependent: constrained decoding suppresses it, free-form decoding recovers it, and at 4B $N{=}16$ it is marginally positive ($+0.7$~pp, $p{=}0.058$).\nThis pattern is preliminary (single RE benchmark, 40\\% zero-F1 rate).\nVC becomes per-sample in the selection context (each candidate's overlap with the majority-voted output varies), yet tends to select the most typical rather than the best output---consistent with MBR's known mode-seeking bias \\cite{eikema2022sampling}.\nMore broadly, all consensus-proximity strategies fail because utility correlates with F1 across instances but not within them (Appendix~\\ref{app:mbr_discussion}).\n\n\\paragraph{Methodological implications.}\nThe decoupling of $\\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal.\nEffective selection likely requires trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust}; $N{=}8$ captures most quality estimation benefit (Appendix~\\ref{app:n_scaling}).\nStructural signals are robust to domain shift when the training schema subsumes the target (Appendix~\\ref{app:ood}).\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  },
  "sourceToolAssistantUUID": "5bf93190-a38f-4e8d-bd29-7eddc4344769",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-16T04:19:38.262Z_

<details open><summary>🔧 Tool call — Read · `toolu_01U8jVBMPLa1t5Z3FxQroEqJ`</summary>

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
  "parentUuid": "d2ae6040-534d-440d-a606-4c82560fdd29",
  "isSidechain": false,
  "requestId": "req_011Cb5c3JmiYULv38aiosTyv",
  "type": "assistant",
  "uuid": "7639a9b2-5b11-4327-8ea4-b9af2afa9e6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4VCbKZST9khKu9p1eDX5N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 31214,
      "output_tokens": 822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 822,
          "cache_read_input_tokens": 31214,
          "cache_creation_input_tokens": 3351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3351
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-16T04:19:38.266Z_

<details><summary>↩ Tool result · `toolu_01U8jVBMPLa1t5Z3FxQroEqJ`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based structured IE, revealing the \textit{correlation-selection gap}: strong quality estimation ($\rho$ up to 0.45) coexists with selection failure.
4	Instance-level signals fail by construction; the core empirical finding is that log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats, 60\% tied), and consensus-proximity selection (MBR) fails because utility correlates with F1 across but not within instances.
5	A 4-seed free-form ablation confirms NER compression is not caused by constrained decoding; on RE, LP selection reverses direction (preliminary, single benchmark).
6	Signal rankings shift with difficulty across NER benchmarks and collapse at the capability boundary---consistent across two model families (3B--8B).
7	RE conclusions rest on SciERC alone (preliminary, 40\% zero-F1 rate); trained verifiers and scaling to 70B+ are promising directions.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7639a9b2-5b11-4327-8ea4-b9af2afa9e6c",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "5b9b3f82-d691-480e-b2c9-531486febc53",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluate five confidence signals for quality estimation and sample selection in LLM-based structured IE, revealing the \\textit{correlation-selection gap}: strong quality estimation ($\\rho$ up to 0.45) coexists with selection failure.\nInstance-level signals fail by construction; the core empirical finding is that log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats, 60\\% tied), and consensus-proximity selection (MBR) fails because utility correlates with F1 across but not within instances.\nA 4-seed free-form ablation confirms NER compression is not caused by constrained decoding; on RE, LP selection reverses direction (preliminary, single benchmark).\nSignal rankings shift with difficulty across NER benchmarks and collapse at the capability boundary---consistent across two model families (3B--8B).\nRE conclusions rest on SciERC alone (preliminary, 40\\% zero-F1 rate); trained verifiers and scaling to 70B+ are promising directions.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "7639a9b2-5b11-4327-8ea4-b9af2afa9e6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-16T04:19:38.598Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Wy4mUEH6a7UCuAa8HvRefA`</summary>

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
  "parentUuid": "5b9b3f82-d691-480e-b2c9-531486febc53",
  "isSidechain": false,
  "requestId": "req_011Cb5c3JmiYULv38aiosTyv",
  "type": "assistant",
  "uuid": "39b71c5a-30b6-46d2-b584-b1d8edcfaa2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4VCbKZST9khKu9p1eDX5N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 31214,
      "output_tokens": 822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 822,
          "cache_read_input_tokens": 31214,
          "cache_creation_input_tokens": 3351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3351
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-16T04:19:38.603Z_

<details><summary>↩ Tool result · `toolu_01Wy4mUEH6a7UCuAa8HvRefA`</summary>

```text
1	Our evaluation covers three NER datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1; generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE shows a directional LP reversal under free-form decoding.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39b71c5a-30b6-46d2-b584-b1d8edcfaa2b",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "0bdaa19e-f272-47f5-8874-bc7a77dfbe67",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers three NER datasets but only one RE benchmark (SciERC), where 40\\% of instances receive zero F1; generalization to other RE benchmarks remains unvalidated.\nWe cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.\nWe do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\\ref{app:n_scaling}).\nThe free-form ablation covers SciERC NER and CoNLL NER with one model; RE shows a directional LP reversal under free-form decoding.\nQwen3-8B's SciERC checkpoint used empty \\texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\\ref{app:thinking_token}).\nLP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.\nWe tested verbalized confidence \\cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\\ref{app:verbalized_confidence}).\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "39b71c5a-30b6-46d2-b584-b1d8edcfaa2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-16T04:19:38.884Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UvraRCdfGq8PT8d64XAj5P`</summary>

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
  "parentUuid": "0bdaa19e-f272-47f5-8874-bc7a77dfbe67",
  "isSidechain": false,
  "requestId": "req_011Cb5c3JmiYULv38aiosTyv",
  "type": "assistant",
  "uuid": "49d29f8b-b80f-48ae-89e3-50fb42ee181a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4VCbKZST9khKu9p1eDX5N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 31214,
      "output_tokens": 822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 822,
          "cache_read_input_tokens": 31214,
          "cache_creation_input_tokens": 3351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3351
          },
          "type": "message"
        }
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

_source line 57 · 2026-05-16T04:19:38.930Z_

<details open><summary>🔧 Tool call — Read · `toolu_017MzhT9dvPo8dsfq8urPZ8Z`</summary>

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
  "parentUuid": "49d29f8b-b80f-48ae-89e3-50fb42ee181a",
  "isSidechain": false,
  "requestId": "req_011Cb5c3JmiYULv38aiosTyv",
  "type": "assistant",
  "uuid": "c305e3c0-5fb7-4bde-9dd7-88db6ad84cfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4VCbKZST9khKu9p1eDX5N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 31214,
      "output_tokens": 822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 822,
          "cache_read_input_tokens": 31214,
          "cache_creation_input_tokens": 3351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3351
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 呈现**  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **页数**: 长文 8 页 +…",
  "leafUuid": "b51c91a7-a896-48cf-877b-8b8e6c5d41e5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 for structured IE confidence estimation paper",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Tool result

_source line 60 · 2026-05-16T04:19:39.134Z_

<details><summary>↩ Tool result · `toolu_01UvraRCdfGq8PT8d64XAj5P`</summary>

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
206	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
207	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
208	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
209	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
210	
211	\begin{table}[t]
212	\centering
213	\small
214	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
215	\label{tab:wnut}
216	\begin{tabular}{lccccc}
217	\toprule
218	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
219	\midrule
220	VC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
221	FK      & .125 & .001 & .555 & .169 & .002 \\
222	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
223	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
224	LP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
225	\bottomrule
226	\end{tabular}
227	\end{table}
228	
229	\paragraph{Cross-configuration selection analysis.}
230	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
231	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
232	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
233	
234	\begin{table*}[t]
235	\centering
236	\small
237	\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
238	\label{tab:cross_selection}
239	\begin{tabular}{llccccccc}
240	\toprule
241	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
242	\midrule
243	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
244	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
245	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
246	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
247	\bottomrule
248	\end{tabular}
249	\end{table*}
250	
251	\paragraph{Diminishing returns of $N$-scaling.}
252	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
253	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
254	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
255	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
256	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
257	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
258	
259	\paragraph{$N{=}16$ CoNLL selection: small but significant.}
260	While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.
261	VC achieves the largest gain over greedy ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
262	These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
263	This reinforces the primary finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.
264	
265	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
266	
267	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
268	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
269	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
270	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
271	
272	\begin{table}[t]
273	\centering
274	\small
275	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
276	\label{tab:bootstrap_signal_ci}
277	\begin{tabular}{lcc}
278	\toprule
279	Signal & $\rho$ & 95\% CI \\
280	\midrule
281	VC & +0.379 & [+0.299, +0.456] \\
282	SJ & +0.360 & [+0.277, +0.437] \\
283	EM & +0.295 & [+0.212, +0.371] \\
284	FK & +0.267 & [+0.176, +0.354] \\
285	LP & +0.205 & [+0.119, +0.291] \\
286	\bottomrule
287	\end{tabular}
288	
289	\vspace{0.5em}
290	
291	\begin{tabular}{lccc}
292	\toprule
293	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
294	\midrule
295	SJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\
296	VC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
297	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
298	\bottomrule
299	\end{tabular}
300	
301	\smallskip
302	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
303	\end{table}
304	
305	At $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.
306	On SciERC NER ($n{=}529$), SJ--FK ($\Delta\rho{=}0.147$--$0.160$, all $p{\leq}0.002$) and VC--FK ($\Delta\rho{=}0.138$--$0.188$, all $p{\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\Delta\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).
307	On CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\Delta\rho{=}0.071$ ($p{<}0.001$), SJ $\Delta\rho{=}0.056$ ($p{<}0.001$), VC $\Delta\rho{=}0.022$ ($p{=}0.040$).
308	
309	\section{Diversity and Selection Analysis}\label{app:diversity}
310	
311	\begin{figure*}[t]
312	\centering
313	\includegraphics[width=\textwidth]{fig_selection_gap}
314	\caption{The correlation-selection gap on SciERC NER ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.40, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound. RE selection results in Table~\ref{tab:selection}.}
315	\label{fig:selection_gap}
316	\end{figure*}
317	
318	\paragraph{Output diversity quantification.}
319	Table~\ref{tab:diversity} summarizes output diversity across configurations.
320	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
321	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
322	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.
323	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
324	
325	\begin{table}[t]
326	\centering
327	\small
328	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
329	\label{tab:diversity}
330	\begin{tabular}{lcc}
331	\toprule
332	Config & Identical & Unique \\
333	\midrule
334	Qwen/SciERC & 11\% & 43\% \\
335	LLaMA/SciERC & 18\% & 39\% \\
336	Qwen/CoNLL & 57\% & --- \\
337	LLaMA/CoNLL & 88\% & --- \\
338	WNUT-17 & 55\% & --- \\
339	\bottomrule
340	\end{tabular}
341	\end{table}
342	
343	\paragraph{Oracle-improvable fraction.}
344	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding greedy\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \S\ref{sec:evaluation}); the diversity quantification in Table~\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
345	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
346	
347	\paragraph{Diversity-stratified selection gap.}
348	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.
349	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.
350	This rules out insufficient diversity as an explanation for the correlation-selection gap.
351	
352	\paragraph{TOST equivalence testing.}\label{app:tost}
353	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
354	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\delta$.
355	The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
356	These proportions use the same test data that defines the headroom, introducing circularity: $\delta$ is anchored to the very quantity it contextualizes.
357	We address this below with externally anchored equivalence margins.
358	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
359	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
360	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
361	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
362	
363	\begin{table}[t]
364	\centering
365	\small
366	\caption{TOST equivalence testing: signals vs.\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ greedy).}
367	\label{tab:tost}
368	\begin{tabular}{l cccc cccc}
369	\toprule
370	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
371	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
372	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
373	\midrule
374	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
375	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
376	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
377	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
378	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
379	\bottomrule
380	\end{tabular}
381	\end{table}
382	
383	\paragraph{External equivalence margins.}
384	The oracle-headroom anchors above introduce circularity, as a reviewer correctly noted: $\delta$ is calibrated against the very quantity it contextualizes.
385	To resolve this, we supplement with three externally grounded margins:
386	(1) $\delta_{\mathrm{SEM}}$: the bootstrapped standard error of greedy F1 (0.43--1.33~pp depending on configuration), representing measurement noise;
387	(2) $\delta_{\mathrm{practical}}{=}0.5$~pp, reflecting the threshold below which NER differences are considered negligible \cite{ratinov2009design};
388	(3) $\delta_{\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \cite{bergkirkpatrick2012empirical}.
389	
390	Results under these external anchors diverge sharply by configuration.
391	On LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\Delta|{\leq}0.1$~pp) and tight CIs at this sample size.
392	On Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\delta$: selection F1 degrades by 0.9--1.5~pp relative to greedy, exceeding even $\delta_{\mathrm{literature}}$.
393	On SciERC NER ($n{=}529$), only SJ passes at $\delta_{\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.
394	These external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to greedy under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.
395	
396	\section{Multi-Seed Stability}\label{app:multiseed}
397	
398	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
399	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals.
400	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.
401	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
402	
403	\begin{table}[t]
404	\centering
405	\small
406	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
407	\label{tab:multiseed}
408	\begin{tabular}{lccccc}
409	\toprule
410	& LP & FK & SJ & VC & EM \\
411	\midrule
412	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
413	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
414	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
415	\midrule
416	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
417	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
418	\midrule
419	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
420	Qwen & .613${\pm}$.002 & .618${\pm}$.009 & .684${\pm}$.009 & .697${\pm}$.010 & .661${\pm}$.010 \\
421	LLaMA & .577${\pm}$.007 & .616${\pm}$.011 & .655${\pm}$.010 & .689${\pm}$.005 & .636${\pm}$.006 \\
422	\bottomrule
423	\end{tabular}
424	\end{table}
425	
426	\section{Training Configuration}\label{app:training}
427	
428	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
429	
430	\begin{table}[t]
431	\centering
432	\small
433	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
434	\label{tab:training}
435	\begin{tabular}{ll}
436	\toprule
437	Parameter & Value \\
438	\midrule
439	LoRA rank / $\alpha$ & 32 / 64 \\
440	LoRA target & All linear modules \\
441	LoRA dropout & 0 \\
442	Optimizer & AdamW \\
443	Learning rate & 2e-4, cosine schedule \\
444	Warmup ratio & 0.1 \\
445	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
446	Epochs & 5 \\
447	Max sequence length & 2048 \\
448	Precision & bf16 \\
449	Gradient checkpointing & Enabled \\
450	Max gradient norm & 1.0 \\
451	Training seed & 42 \\
452	Framework & LLaMA Factory \\
453	\midrule
454	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
455	SciERC split & 1861 / 275 / 551 \\
456	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
457	& eval\_steps${=}$200, save\_limit${=}$5 \\
458	\bottomrule
459	\end{tabular}
460	\end{table}
461	
462	\paragraph{Prompt template.}
463	For NER, we use a structured prompt:
464	\begin{quote}
465	\small
466	\texttt{System:} You are an expert in Named Entity Recognition.\\
467	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
468	Text: \texttt{\{input\_text\}}\\
469	Entity types: \texttt{\{schema\_types\}}
470	\end{quote}
471	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
472	
473	\paragraph{Constrained decoding.}
474	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
475	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
476	
477	\section{Thinking Token Impact Analysis}\label{app:thinking_token}
478	
479	Qwen3-8B's SciERC checkpoint was trained with empty \texttt{&lt;think>&lt;/think>} blocks prepended to each response (\S\ref{sec:setup}).
480	We quantify the potential impact on LP scores through three complementary arguments.
481	
482	\paragraph{LP shift magnitude.}
483	Empty thinking tokens (mean 4.5 per sample) constitute 2.1\% of tokens on SciERC.
484	The estimated LP shift is 0.001 nats per token (2.68\% of the median within-instance LP range of 0.041 nats).
485	Because all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\%$ of instances.
486	
487	\paragraph{Constant prefix cancellation.}
488	All $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.
489	Any LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \textit{rankings} unchanged.
490	
491	\paragraph{CoNLL control group.}
492	CoNLL and WNUT-17 checkpoints were trained without thinking tokens (\texttt{enable\_thinking=False}).
493	If thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.
494	Instead, CoNLL shows \textit{higher} tied fractions at both temperatures (86.8\% at $T{=}1.0$, 95.8\% at $T{=}0.7$) than SciERC (60.3\% at $T{=}1.0$), directly contradicting the thinking-token hypothesis.
495	
496	\section{Log-Probability Score Compression}\label{app:logprob_ties}
497	
498	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
499	The median within-instance LP range is only 0.041 nats---below the $\varepsilon{=}0.05$ threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice.
500	At $\varepsilon{=}0.05$, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below the threshold, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
501	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
502	This compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\%$ (vs.\ seed${=}42$: $0.041$ nats, $60.3\%$).
503	Seed~456 uses a different subtask flag (joint vs.\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\ 8.20 nats; Mann--Whitney $p{=}0.55$), confirming that the subtask change does not affect compression.
504	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
505	
506	\begin{figure}[t]
507	\centering
508	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
509	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
510	\label{fig:lp_range_cdf}
511	\end{figure}
512	
513	\begin{table}[t]
514	\centering
515	\small
516	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
517	\label{tab:logprob_ties}
518	\begin{tabular}{lc}
519	\toprule
520	$\varepsilon$ threshold & Tied instances (\%) \\
521	\midrule
522	0.01 & 1.1\% \\
523	0.05 & 60.3\% \\
524	0.1  & ${\sim}$84\% \\
525	0.5  & ${\sim}$99\% \\
526	\bottomrule
527	\end{tabular}
528	\end{table}
529	
530	\paragraph{Non-tied subset.}
531	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
532	As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.
533	A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
534	
535	\paragraph{$\varepsilon$ sensitivity sweep.}
536	Table~\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\varepsilon{=}0.01$ to $0.20$.
537	The tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.
538	$\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\varepsilon{\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\leq}36$).
539	
540	\begin{table}[t]
541	\centering
542	\small
543	\caption{$\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\%'' = fraction with within-instance LP range ${<}\varepsilon$. $\Delta$: selection F1 gain over greedy on the non-tied subset. The tied fraction increases smoothly; $\varepsilon{=}0.05$ yields the strongest statistical separation.}
544	\label{tab:epsilon_sweep}
545	\begin{tabular}{ccccc}
546	\toprule
547	$\varepsilon$ & Tied\% & Non-tied $n$ & $\Delta$ (pp) & $p$ \\
548	\midrule
549	0.01 & 1.1\% & 523 & $+$0.58 & .21 \\
550	0.02 & 13.6\% & 457 & $+$0.83 & .15 \\
551	0.03 & 31.8\% & 361 & $+$1.31 & .079 \\
552	\textbf{0.05} & \textbf{60.3\%} & \textbf{210} & \textbf{$+$2.86} & \textbf{.004} \\
553	0.10 & 83.9\% & 85 & $+$3.69 & .034 \\
554	0.15 & 93.2\% & 36 & $+$4.15 & .11 \\
555	0.20 & 96.4\% & 19 & $+$4.59 & .13 \\
556	\bottomrule
557	\end{tabular}
558	\end{table}
559	
560	\paragraph{$\varepsilon$ robustness of selection F1.}\label{app:epsilon_robustness}
561	The preceding analysis stratifies LP by a tied/non-tied threshold; consistency-based signals (SJ, FK, VC, EM) also use $\varepsilon$ to define MBR-style proximity in selection.
562	Table~\ref{tab:epsilon_robustness} reports the maximum selection F1 variation across $\varepsilon \in [0, 0.2]$ for all signals and configurations.
563	At $\varepsilon{=}0.05$, consistency signals change by at most 1.09~pp (mean 0.21~pp), with EM completely $\varepsilon$-invariant (integer scoring); LP is the most sensitive (up to 3.65~pp across the full range), as expected.
564	Spearman $\rho$---the primary quality estimation metric throughout---is a continuous rank correlation that does not depend on any discretization threshold; the $\varepsilon$ parameter affects only the selection analysis.
565	
566	\begin{table}[t]
567	\centering
568	\small
569	\caption{Maximum selection F1 variation (pp) across $\varepsilon \in [0, 0.2]$. At $\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\varepsilon$ governs its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}
570	\label{tab:epsilon_robustness}
571	\begin{tabular}{lcccc}
572	\toprule
573	& \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL}} \\
574	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
575	Signal & Qwen & LLaMA & Qwen & LLaMA \\
576	\midrule
577	SJ & 0.92 & 1.45 & 0.99 & 0.18 \\
578	FK & 1.03 & 0.93 & 0.60 & 0.15 \\
579	VC & 2.33 & 0.53 & 0.72 & 0.18 \\
580	EM & 0.00 & 0.00 & 0.00 & 0.00 \\
581	LP & 3.65 & 2.58 & 3.00 & 0.31 \\
582	\bottomrule
583	\end{tabular}
584	\end{table}
585	
586	\section{RE Conditional Selection}\label{app:re_conditional_selection}
587	
588	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
589	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
590	All five signals underperform greedy on both subsets.
591	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
592	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
593	
594	\begin{table}[t]
595	\centering
596	\small
597	\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
598	\label{tab:re_cond_selection}
599	\begin{tabular}{lcc}
600	\toprule
601	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
602	\midrule
603	Oracle & 0.585 & 0.757 \\
604	\midrule
605	LP & 0.395 & 0.600 \\
606	SJ & 0.386 & 0.604 \\
607	EM & 0.372 & 0.583 \\
608	VC & 0.359 & 0.574 \\
609	\midrule
610	Greedy & 0.404 & 0.674 \\
611	\bottomrule
612	\end{tabular}
613	\end{table}
614	
615	\section{RE $N{=}16$ Selection Analysis}\label{app:re_n16_selection}
616	
617	Table~\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.
618	All four consistency signals underperform greedy, with EM showing the largest deficit ($\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).
619	LP is the only positive signal ($\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).
620	Even the most favorable seed captures only ${\sim}9\%$ of the 17.1~pp oracle headroom.
621	This cross-task consistency---LP as the only viable selection signal on both NER and RE---reinforces the structural limitation of instance-level signals for candidate ranking.
622	
623	\begin{table}[t]
624	\centering
625	\small
626	\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\pm}\sigma$, $n{=}551$). Fisher combined $p$ vs.\ greedy. LP is the only signal with positive $\Delta$. $\sigma$ is population standard deviation over 3 seeds.}
627	\label{tab:re_n16_selection}
628	\begin{tabular}{lccc}
629	\toprule
630	Method & F1 & $\Delta$ (pp) & $p$(Fisher) \\
631	\midrule
632	Oracle & $.463{\pm}.006$ & $+$17.1 & --- \\
633	\midrule
634	LP & $\mathbf{.299}{\pm}.007$ & $+$0.7 & .058 \\
635	VC & $.284{\pm}.002$ & $-$0.8 & .973 \\
636	FK & $.283{\pm}.005$ & $-$0.9 & .985 \\
637	SJ & $.281{\pm}.005$ & $-$1.0 & .993 \\
638	EM & $.277{\pm}.007$ & $-$1.5 & .999 \\
639	\midrule
640	Greedy & $.291{\pm}.000$ & --- & --- \\
641	Random & $.262{\pm}.001$ & $-$2.9 & --- \\
642	\bottomrule
643	\end{tabular}
644	\end{table}
645	
646	\section{MBR Decoding and Task-Specific Interactions}\label{app:mbr_discussion}
647	
648	\paragraph{Connection to MBR decoding.}
649	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
650	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
651	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
652	
653	\paragraph{Task-specific decoding interactions.}
654	The free-form ablation reveals divergent behavior across tasks.
655	On RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).
656	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
657	This interaction does not generalize to NER, where selection remains negligible under both regimes.
658	This ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.
659	The non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
660	Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
661	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
662	
663	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
664	
665	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).
666	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
667	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
668	RE LP selection consistently reverses direction under free-form decoding across 4 seeds: $+1.84{\pm}0.12$~pp (seeds 42/123/456/789: $+1.69$, $+1.76$, $+2.00$, $+1.91$~pp) vs.\ $-0.68$~pp constrained.
669	The constrained reference ($-0.68$~pp) uses the ablation-matched baseline; the primary experiment (Table~\ref{tab:selection}) yields $-0.9$~pp on the same gold-filtered set.
670	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
671	
672	\begin{table*}[t]
673	\centering
674	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\pm}0.12$~pp).}
675	\label{tab:freeform_ablation}
676	
677	\vspace{2pt}
678	{\small\textsc{Panel A: Logprob Distribution}}
679	\vspace{2pt}
680	
681	\begin{tabular}{lccc}
682	\toprule
683	Metric & Constrained & Free-form & $\Delta$ \\
684	\midrule
685	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
686	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
687	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
688	\bottomrule
689	\end{tabular}
690	
691	\vspace{8pt}
692	
693	{\small\textsc{Panel B: Selection F1}}
694	\vspace{2pt}
695	
696	\begin{tabular}{llccc}
697	\toprule
698	Task & Method & Constrained & Free-form & $\Delta$ \\
699	\midrule
700	\multirow{3}{*}{NER}
701	  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\
702	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
703	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
704	\midrule
705	\multirow{3}{*}{RE}
706	  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\
707	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
708	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
709	\bottomrule
710	\end{tabular}
711	
712	\vspace{8pt}
713	
714	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
715	\vspace{2pt}
716	
717	\begin{tabular}{l ccc ccc}
718	\toprule
719	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
720	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
721	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
722	\midrule
723	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
724	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
725	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
726	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
727	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
728	\bottomrule
729	\end{tabular}
730	
731	\vspace{8pt}
732	
733	{\small\textsc{Panel D: Parse Rate (Free-form)}}
734	\vspace{2pt}
735	
736	\begin{tabular}{lc}
737	\toprule
738	Metric & Value \\
739	\midrule
740	Total samples          & 4408 \\
741	Parse rate             & 99.95\% \\
742	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
743	\bottomrule
744	\end{tabular}
745	
746	\end{table*}
747	
748	\paragraph{CoNLL NER free-form results.}
749	Extending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\pm}0.007$ across seeds---higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\% tied fraction under constrained decoding.
750	Free-form decoding reduces the tied fraction modestly, yet selection remains below greedy: LP-selected F1${=}0.896$ vs.\ greedy $0.904$ ($\Delta{=}{-}0.77$~pp).
751	Quality estimation under free-form decoding yields SJ $\rho{=}0.461$, EM $\rho{=}0.471$, LP $\rho{=}0.326$---comparable to constrained results (Table~\ref{tab:quality_estimation}).
752	The failure to improve selection despite reduced compression is consistent with CoNLL's low oracle headroom (4.25~pp at $N{=}8$), which limits the selection space regardless of score distribution quality.
753	
754	\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
755	
756	We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
757	
758	\paragraph{Pairwise overlap.}
759	LP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.
760	The 3-way intersection contains 34 instances (27.9\% of any-seed failures), confirming a stable failure core.
761	
762	\paragraph{Instance complexity drives failure.}
763	Table~\ref{tab:stable_failures} stratifies instances by failure stability.
764	Stable failures (all 3 seeds) involve more gold relations (2.12 vs.\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.
765	Failure rate increases monotonically with gold relation count: 4.3\% at 1 relation, 20.7\% at 3 relations, 26.2\% at 6 relations.
766	
767	\begin{table}[t]
768	\centering
769	\small
770	\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}
771	\label{tab:stable_failures}
772	\begin{tabular}{lcccc}
773	\toprule
774	Group & $n$ & Gold rels & Greedy F1 & LP $\Delta$F1 \\
775	\midrule
776	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
777	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
778	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
779	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
780	\bottomrule
781	\end{tabular}
782	\end{table}
783	
784	\paragraph{Flip instances.}
785	Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
786	These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
787	
788	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
789	
790	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
791	
792	\begin{table}[t]
793	\centering
794	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
795	\label{tab:n-scaling}
796	\small
797	\begin{tabular}{l ccc ccc}
798	\toprule
799	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
800	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
801	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
802	\midrule
803	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
804	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
805	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
806	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
807	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
808	\midrule
809	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
810	\bottomrule
811	\end{tabular}
812	\end{table}
813	
814	\begin{table}[t]
815	\centering
816	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
817	\label{tab:ranking-stability}
818	\small
819	\begin{tabular}{ll cc l}
820	\toprule
821	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
822	\midrule
823	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
824	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
825	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
826	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
827	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
828	\bottomrule
829	\end{tabular}
830	\end{table}
831	
832	\begin{table}[t]
833	\centering
834	\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
835	\label{tab:sigma-comparison}
836	\small
837	\begin{tabular}{l cc cc}
838	\toprule
839	 & \multicolumn{2}{c}{\textbf{NER} $\sigma_\rho$} & \multicolumn{2}{c}{\textbf{RE} $\sigma_\rho$} \\
840	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
841	Signal & $N\!=\!8$ & $N\!=\!16$ & $N\!=\!8$ & $N\!=\!16$ \\
842	\midrule
843	SJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\
844	FK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\
845	VC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\
846	EM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\
847	LP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\
848	\midrule
849	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
850	\bottomrule
851	\end{tabular}
852	\end{table}
853	
854	Signal rankings are highly stable across seeds: Kendall's $W{=}1.000$ for NER at $N{=}8$ (both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}).
855	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER), confirming that additional samples stabilize structural signals more than LP.
856	
857	\section{Cross-Dataset OOD Analysis}\label{app:ood}
858	
859	To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\to$narrower schema) and vice versa (Table~\ref{tab:ood}).
860	
861	\begin{table}[t]
862	\centering
863	\small
864	\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\rho$ from Table~\ref{tab:quality_estimation} (same model, same seed). \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
865	\label{tab:ood}
866	\begin{tabular}{l ccc ccc}
867	\toprule
868	 & \multicolumn{3}{c}{\textbf{SciERC$\to$CoNLL}} & \multicolumn{3}{c}{\textbf{CoNLL$\to$SciERC}} \\
869	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
870	Signal & $\rho$ & In-dom. & $\Delta$ & $\rho$ & In-dom. & $\Delta$ \\
871	\midrule
872	VC & .469\textsuperscript{***} & .379 & +.090 & +.105\textsuperscript{*} & .379 & $-$.274 \\
873	SJ & .378\textsuperscript{***} & .360 & +.018 & $-$.186\textsuperscript{***} & .360 & $-$.546 \\
874	EM & .300\textsuperscript{***} & .295 & +.005 & $-$.202\textsuperscript{***} & .295 & $-$.497 \\
875	FK & .285\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\
876	LP & .246\textsuperscript{***} & .205 & +.041 & $-$.152\textsuperscript{***} & .205 & $-$.357 \\
877	\bottomrule
878	\end{tabular}
879	\end{table}
880	
881	\paragraph{Wider-to-narrower schema transfer.}
882	When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.379$, $\Delta{=}{+}0.090$), SJ $\rho{=}0.378$ (in-domain $0.360$, $\Delta{=}{+}0.018$), and FK $\rho{=}0.285$ (in-domain $0.267$, $\Delta{=}{+}0.018$).
883	The wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (greedy F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.
884	
885	\paragraph{Narrower-to-wider schema transfer (excluded).}
886	The reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.
887	The CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (greedy NER F1${=}0.009$, RE F1${=}0.001$).
888	Under this regime, most signals flip to negative or near-zero correlations (Table~\ref{tab:ood}); only VC retains weak positive correlation ($\rho{=}0.105$, $p{=}0.016$).
889	These negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\S\ref{sec:qe_results}), not evidence against signal utility.
890	
891	\paragraph{Asymmetry interpretation.}
892	The directional asymmetry is driven by schema coverage: wider$\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.
893	This extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.
894	
895	\section{Verbalized Confidence}\label{app:verbalized_confidence}
896	
897	We evaluate verbalized confidence (VerbConf) as a second per-sample signal following \citet{tian2023calibration}: after generating each structured output, the model is prompted to rate its confidence on a 1--10 scale.
898	Table~\ref{tab:verbconf} reports quality estimation and selection results.
899	
900	\begin{table}[t]
901	\centering
902	\small
903	\caption{Verbalized confidence (VerbConf) vs.\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}
904	\label{tab:verbconf}
905	\begin{tabular}{l cc cc}
906	\toprule
907	 & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{CoNLL NER}} \\
908	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
909	Metric & VerbConf & LP & VerbConf & LP \\
910	\midrule
911	$\rho$ & 0.297 & 0.205 & 0.337 & 0.316 \\
912	AUROC & 0.681 & 0.578 & 0.747 & 0.753 \\
913	Selection F1 & 0.620 & 0.647 & 0.889 & 0.904 \\
914	$\Delta$ vs.\ greedy & $-$2.45\,pp & $+$0.2\,pp & $-$1.93\,pp & $-$0.77\,pp \\
915	\midrule
916	Mean score & 8.58\,/\,10 & --- & 9.24\,/\,10 & --- \\
917	Parse fail rate & 0.26\% & --- & 0\% & --- \\
918	\bottomrule
919	\end{tabular}
920	\end{table}
921	
922	\paragraph{Severe overconfidence.}
923	VerbConf exhibits extreme score compression: mean confidence is 8.58/10 on SciERC (greedy F1${=}0.645$) and 9.24/10 on CoNLL (greedy F1${=}0.904$), with most scores concentrated in the 8--10 range.
924	This compression is more severe than LP (which spans a 0.041-nat median range), confirming that score compression is a general property of model self-assessment, not an artifact of log-probability computation.
925	
926	\paragraph{QE--selection decoupling.}
927	VerbConf achieves higher $\rho$ than LP on both datasets (SciERC: 0.297 vs.\ 0.205; CoNLL: 0.337 vs.\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\ 0.578; CoNLL: 0.747 vs.\ 0.753), yet yields the worst selection among all signals ($\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).
928	This dissociation further demonstrates the correlation-selection gap: a signal can rank instances by expected quality without being able to discriminate candidates within an instance.
929	The AUROC--$\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\rho$ at 0.337) reflects differing sensitivity to binary vs.\ ordinal discrimination.
930	
931	\section{LLaMA-3.2-3B Scale Ablation}\label{app:llama3b}
932	
933	To extend scale coverage below 4B, we fine-tune LLaMA-3.2-3B-Instruct on SciERC NER under identical training conditions (LoRA rank${=}32$, $\alpha{=}64$, 5 epochs) and evaluate quality estimation and selection (Table~\ref{tab:llama3b}).
934	
935	\begin{table}[t]
936	\centering
937	\small
938	\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}
939	\label{tab:llama3b}
940	\begin{tabular}{l cc cc}
941	\toprule
942	Signal & $\rho$ & AUROC & Sel.\ F1 & $\Delta$ vs.\ greedy \\
943	\midrule
944	VC & \textbf{.460} & .743 & 0.611 & $-$1.54\,pp \\
945	SJ & .375 & .738 & \textbf{0.633} & $+$0.61\,pp \\
946	EM & .334 & \textbf{.776} & --- & --- \\
947	FK & .268 & .671 & 0.630 & $+$0.28\,pp \\
948	LP & .266 & .633 & 0.628 & $+$0.12\,pp \\
949	\midrule
950	Greedy & --- & --- & 0.627 & --- \\
951	Oracle & --- & --- & 0.763 & --- \\
952	\bottomrule
953	\end{tabular}
954	\end{table}
955	
956	The $\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\ref{tab:quality_estimation}), confirming ranking stability across two model families spanning 3B--8B.
957	AUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), reflecting the $\rho$--AUROC dissociation noted in the main text.
958	Despite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC---the strongest QE signal---yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.
959	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49d29f8b-b80f-48ae-89e3-50fb42ee181a",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "8f5bf301-fe7b-4d21-adde-f95f8656babf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\nWe exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\\%; SciERC: 22/551, 4.0\\%).\nFor these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\\rho$ depending on signal behavior at the boundary.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as sample standard deviation.}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\quad LP & $T{=}0.7$ & 0.249 & --- \\\\\n\\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.411$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.283 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.474{\\pm}0.009$ & --- \\\\\n\\quad FK &  & $0.467{\\pm}0.009$ & --- \\\\\n\\quad EM &  & $0.473{\\pm}0.010$ & --- \\\\\n\\quad VC &  & $0.470{\\pm}0.006$ & --- \\\\\n\\quad LP &  & $0.311{\\pm}0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\\Delta\\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.\nFK NER $\\rho$ drops by 0.022, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nLP exhibits the largest temperature effect on NER ($\\rho{=}0.249$ at $T{=}0.7$ vs.\\ $0.205$ at $T{=}1.0$, $\\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.\nAcross all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.411{\\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.034$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, suggesting that structural and binary-agreement signals are the most robust to $N$.\nAt $N{=}16$, SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$), making it a more stable alternative at higher sample sizes.\n\n\\paragraph{Transfer across model families.}\nLLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, $\\Delta\\rho{=}0.069$; permutation $p{=}0.06$, borderline).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\\rho{=}0.409$ vs.\\ LP 0.239, $\\Delta{=}{+}0.170$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$),\\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.474{\\pm}0.009$ vs.\\ LP $0.311{\\pm}0.003$, $\\Delta{=}{+}0.163$).\n\n\\paragraph{FK independence: instance-level permutation test.}\\label{app:fk_independence}\n\nTo verify that Fleiss' $\\kappa$ reflects genuine within-instance agreement rather than marginal-rate artifacts, we conduct instance-level permutation tests across three configurations.\nFor each instance, we permute sample labels 10{,}000 times to generate a null distribution of FK under independence, then compare the observed FK against this null via a one-sample $t$-test and permutation $p$-value.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}\n\\label{tab:fk_independence}\n\\begin{tabular}{lrcccc}\n\\toprule\nConfig & $n$ & FK mean & 95\\% CI & $t$ & Split-half $r$ \\\\\n\\midrule\nSciERC (Qwen) & 529 & 0.402 & [0.376, 0.428] & 30.8 & 0.395 \\\\\nCoNLL (LLaMA) & 2{,}756 & 0.927 & [0.919, 0.935] & 225.9 & 0.578 \\\\\nCoNLL (Qwen) & 2{,}756 & 0.720 & [0.706, 0.734] & 102.1 & 0.520 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:fk_independence} reports the results.\nAll configurations reject the independence null at $p{<}0.001$ ($n{=}529$--$2{,}756$), confirming that FK captures genuine inter-sample agreement rather than chance label co-occurrence.\nSplit-half reliability ranges from $r{=}0.395$ (SciERC) to $r{=}0.578$ (CoNLL LLaMA), indicating moderate stability: FK estimates from half the samples correlate positively with those from the other half, though the SciERC value suggests noisier estimation on harder tasks with fewer samples.\nThe higher FK means on CoNLL ($0.720$--$0.927$) vs.\\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, making the two selection rules equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{SJ normalizer robustness.}\nEquation~\\ref{eq:sj} uses $\\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \\cup g_j|$.\nTable~\\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\\Delta\\rho|{<}0.01$ in every case, confirming that the choice between max and union normalization does not affect conclusions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SJ normalizer comparison (Spearman $\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\\max(|g_i|,|g_j|)$; Union: $|g_i \\cup g_j|$.}\n\\label{tab:sj_normalizer}\n\\begin{tabular}{@{}ll ccc@{}}\n\\toprule\nDataset & Model & $\\rho$(max) & $\\rho$(union) & $\\Delta\\rho$ \\\\\n\\midrule\nCoNLL & Qwen3-8B & .436 & .438 & $-$.002 \\\\\nCoNLL & Qwen3-4B & .422 & .421 & $+$.000 \\\\\nCoNLL & LLaMA-8B & .431 & .432 & $-$.000 \\\\\nSciERC & Qwen3-8B & .360 & .365 & $-$.005 \\\\\nSciERC & Qwen3-4B & .422 & .423 & $-$.001 \\\\\nSciERC & LLaMA-8B & .363 & .372 & $-$.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\\Delta\\rho{=}{-}0.005$, $p{=}0.53$; preliminary).\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17.\nVC achieves $\\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\\rho{=}0.038$ ($p{=}0.49$).\nLP shows the reverse pattern: full-set $\\rho{=}{-}0.410$ but conditional $\\rho{=}0.350$, the highest among all signals on the conditional set.\nThis inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\\rho$; its conditional $\\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}\n\\label{tab:wnut}\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & $\\rho$ & $p$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\\\\nFK      & .125 & .001 & .555 & .169 & .002 \\\\\nSJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn CoNLL, 57--88\\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \\textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\paragraph{$N{=}16$ CoNLL selection: small but significant.}\nWhile quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.\nVC achieves the largest gain over greedy ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).\nThese gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\\% of the available headroom.\nThis reinforces the primary finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVC & +0.379 & [+0.299, +0.456] \\\\\nSJ & +0.360 & [+0.277, +0.437] \\\\\nEM & +0.295 & [+0.212, +0.371] \\\\\nFK & +0.267 & [+0.176, +0.354] \\\\\nLP & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\\\\nVC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\nAt $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.\nOn SciERC NER ($n{=}529$), SJ--FK ($\\Delta\\rho{=}0.147$--$0.160$, all $p{\\leq}0.002$) and VC--FK ($\\Delta\\rho{=}0.138$--$0.188$, all $p{\\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\\Delta\\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).\nOn CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\\Delta\\rho{=}0.071$ ($p{<}0.001$), SJ $\\Delta\\rho{=}0.056$ ($p{<}0.001$), VC $\\Delta\\rho{=}0.022$ ($p{=}0.040$).\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC NER ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.40, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound. RE selection results in Table~\\ref{tab:selection}.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 57\\% (Qwen) to 88\\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding greedy\\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \\S\\ref{sec:evaluation}); the diversity quantification in Table~\\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, confirming the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{TOST equivalence testing.}\\label{app:tost}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\\delta$.\nThe $\\delta$ values are contextualized against oracle headroom (12--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\nThese proportions use the same test data that defines the headroom, introducing circularity: $\\delta$ is anchored to the very quantity it contextualizes.\nWe address this below with externally anchored equivalence margins.\nThe breakpoint $\\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\\sim}$10\\% of oracle headroom) to 3.4~pp (FK, ${\\sim}$26\\%) on NER, and from approximately 2.9~pp (LP, ${\\sim}$16\\%) to 6.5~pp (VC, ${\\sim}$36\\%) on RE.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ greedy).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{External equivalence margins.}\nThe oracle-headroom anchors above introduce circularity, as a reviewer correctly noted: $\\delta$ is calibrated against the very quantity it contextualizes.\nTo resolve this, we supplement with three externally grounded margins:\n(1) $\\delta_{\\mathrm{SEM}}$: the bootstrapped standard error of greedy F1 (0.43--1.33~pp depending on configuration), representing measurement noise;\n(2) $\\delta_{\\mathrm{practical}}{=}0.5$~pp, reflecting the threshold below which NER differences are considered negligible \\cite{ratinov2009design};\n(3) $\\delta_{\\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \\cite{bergkirkpatrick2012empirical}.\n\nResults under these external anchors diverge sharply by configuration.\nOn LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\\Delta|{\\leq}0.1$~pp) and tight CIs at this sample size.\nOn Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\\delta$: selection F1 degrades by 0.9--1.5~pp relative to greedy, exceeding even $\\delta_{\\mathrm{literature}}$.\nOn SciERC NER ($n{=}529$), only SJ passes at $\\delta_{\\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.\nThese external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to greedy under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\nOn NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals.\nOn RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.\nLLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .613${\\pm}$.002 & .618${\\pm}$.009 & .684${\\pm}$.009 & .697${\\pm}$.010 & .661${\\pm}$.010 \\\\\nLLaMA & .577${\\pm}$.007 & .616${\\pm}$.011 & .655${\\pm}$.010 & .689${\\pm}$.005 & .636${\\pm}$.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}\n\n\\section{Thinking Token Impact Analysis}\\label{app:thinking_token}\n\nQwen3-8B's SciERC checkpoint was trained with empty \\texttt{&lt;think>&lt;/think>} blocks prepended to each response (\\S\\ref{sec:setup}).\nWe quantify the potential impact on LP scores through three complementary arguments.\n\n\\paragraph{LP shift magnitude.}\nEmpty thinking tokens (mean 4.5 per sample) constitute 2.1\\% of tokens on SciERC.\nThe estimated LP shift is 0.001 nats per token (2.68\\% of the median within-instance LP range of 0.041 nats).\nBecause all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\\%$ of instances.\n\n\\paragraph{Constant prefix cancellation.}\nAll $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.\nAny LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \\textit{rankings} unchanged.\n\n\\paragraph{CoNLL control group.}\nCoNLL and WNUT-17 checkpoints were trained without thinking tokens (\\texttt{enable\\_thinking=False}).\nIf thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.\nInstead, CoNLL shows \\textit{higher} tied fractions at both temperatures (86.8\\% at $T{=}1.0$, 95.8\\% at $T{=}0.7$) than SciERC (60.3\\% at $T{=}1.0$), directly contradicting the thinking-token hypothesis.\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}, Figure~\\ref{fig:lp_range_cdf}).\nThe median within-instance LP range is only 0.041 nats---below the $\\varepsilon{=}0.05$ threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice.\nAt $\\varepsilon{=}0.05$, 60.3\\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below the threshold, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nThe CDF rises smoothly with no cliff or discontinuity (Figure~\\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.\nThis compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\\%$ (vs.\\ seed${=}42$: $0.041$ nats, $60.3\\%$).\nSeed~456 uses a different subtask flag (joint vs.\\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\\ 8.20 nats; Mann--Whitney $p{=}0.55$), confirming that the subtask change does not affect compression.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_lp_range_cdf}\n\\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}\n\\label{fig:lp_range_cdf}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nAs a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\\rho(\\text{LP}, \\text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\\% of instances achieve $p{<}0.05$ significance, and $\\rho(\\text{LP range}, \\text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.\nA free-form NER decoding ablation (Appendix~\\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.\n\n\\paragraph{$\\varepsilon$ sensitivity sweep.}\nTable~\\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\\varepsilon{=}0.01$ to $0.20$.\nThe tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.\n$\\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\\varepsilon{\\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\\leq}36$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\\%'' = fraction with within-instance LP range ${<}\\varepsilon$. $\\Delta$: selection F1 gain over greedy on the non-tied subset. The tied fraction increases smoothly; $\\varepsilon{=}0.05$ yields the strongest statistical separation.}\n\\label{tab:epsilon_sweep}\n\\begin{tabular}{ccccc}\n\\toprule\n$\\varepsilon$ & Tied\\% & Non-tied $n$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n0.01 & 1.1\\% & 523 & $+$0.58 & .21 \\\\\n0.02 & 13.6\\% & 457 & $+$0.83 & .15 \\\\\n0.03 & 31.8\\% & 361 & $+$1.31 & .079 \\\\\n\\textbf{0.05} & \\textbf{60.3\\%} & \\textbf{210} & \\textbf{$+$2.86} & \\textbf{.004} \\\\\n0.10 & 83.9\\% & 85 & $+$3.69 & .034 \\\\\n0.15 & 93.2\\% & 36 & $+$4.15 & .11 \\\\\n0.20 & 96.4\\% & 19 & $+$4.59 & .13 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{$\\varepsilon$ robustness of selection F1.}\\label{app:epsilon_robustness}\nThe preceding analysis stratifies LP by a tied/non-tied threshold; consistency-based signals (SJ, FK, VC, EM) also use $\\varepsilon$ to define MBR-style proximity in selection.\nTable~\\ref{tab:epsilon_robustness} reports the maximum selection F1 variation across $\\varepsilon \\in [0, 0.2]$ for all signals and configurations.\nAt $\\varepsilon{=}0.05$, consistency signals change by at most 1.09~pp (mean 0.21~pp), with EM completely $\\varepsilon$-invariant (integer scoring); LP is the most sensitive (up to 3.65~pp across the full range), as expected.\nSpearman $\\rho$---the primary quality estimation metric throughout---is a continuous rank correlation that does not depend on any discretization threshold; the $\\varepsilon$ parameter affects only the selection analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Maximum selection F1 variation (pp) across $\\varepsilon \\in [0, 0.2]$. At $\\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\\varepsilon$ governs its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}\n\\label{tab:epsilon_robustness}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & Qwen & LLaMA & Qwen & LLaMA \\\\\n\\midrule\nSJ & 0.92 & 1.45 & 0.99 & 0.18 \\\\\nFK & 1.03 & 0.93 & 0.60 & 0.15 \\\\\nVC & 2.33 & 0.53 & 0.72 & 0.18 \\\\\nEM & 0.00 & 0.00 & 0.00 & 0.00 \\\\\nLP & 3.65 & 2.58 & 3.00 & 0.31 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform greedy on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLP & 0.395 & 0.600 \\\\\nSJ & 0.386 & 0.604 \\\\\nEM & 0.372 & 0.583 \\\\\nVC & 0.359 & 0.574 \\\\\n\\midrule\nGreedy & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{RE $N{=}16$ Selection Analysis}\\label{app:re_n16_selection}\n\nTable~\\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.\nAll four consistency signals underperform greedy, with EM showing the largest deficit ($\\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).\nLP is the only positive signal ($\\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).\nEven the most favorable seed captures only ${\\sim}9\\%$ of the 17.1~pp oracle headroom.\nThis cross-task consistency---LP as the only viable selection signal on both NER and RE---reinforces the structural limitation of instance-level signals for candidate ranking.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\\pm}\\sigma$, $n{=}551$). Fisher combined $p$ vs.\\ greedy. LP is the only signal with positive $\\Delta$. $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:re_n16_selection}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & F1 & $\\Delta$ (pp) & $p$(Fisher) \\\\\n\\midrule\nOracle & $.463{\\pm}.006$ & $+$17.1 & --- \\\\\n\\midrule\nLP & $\\mathbf{.299}{\\pm}.007$ & $+$0.7 & .058 \\\\\nVC & $.284{\\pm}.002$ & $-$0.8 & .973 \\\\\nFK & $.283{\\pm}.005$ & $-$0.9 & .985 \\\\\nSJ & $.281{\\pm}.005$ & $-$1.0 & .993 \\\\\nEM & $.277{\\pm}.007$ & $-$1.5 & .999 \\\\\n\\midrule\nGreedy & $.291{\\pm}.000$ & --- & --- \\\\\nRandom & $.262{\\pm}.001$ & $-$2.9 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{MBR Decoding and Task-Specific Interactions}\\label{app:mbr_discussion}\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Task-specific decoding interactions.}\nThe free-form ablation reveals divergent behavior across tasks.\nOn RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).\nThe win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).\nThis interaction does not generalize to NER, where selection remains negligible under both regimes.\nThis ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.\nThe non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\\times}$ increase in within-instance LP range for the newly non-tied subset.\nDespite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.\nFree-form decoding also slightly improves quality estimation (NER VC $\\rho$: 0.379$\\to$0.409), though this does not translate to selection gains.\n\n\\section{Free-Form Decoding Ablation}\\label{app:freeform_ablation}\n\nTable~\\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).\nFree-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\\%, 4406/4408).\nLP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\\times}$), and NER selection gains remain negligible under both regimes (Panel~B).\nRE LP selection consistently reverses direction under free-form decoding across 4 seeds: $+1.84{\\pm}0.12$~pp (seeds 42/123/456/789: $+1.69$, $+1.76$, $+2.00$, $+1.91$~pp) vs.\\ $-0.68$~pp constrained.\nThe constrained reference ($-0.68$~pp) uses the ablation-matched baseline; the primary experiment (Table~\\ref{tab:selection}) yields $-0.9$~pp on the same gold-filtered set.\nQuality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\\pm}0.12$~pp).}\n\\label{tab:freeform_ablation}\n\n\\vspace{2pt}\n{\\small\\textsc{Panel A: Logprob Distribution}}\n\\vspace{2pt}\n\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\nMean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\\\\nMean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\\\\nTied fraction ($\\varepsilon{=}0.05$) & 59.7\\% & 57.7\\% & $-$2.0\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel B: Selection F1}}\n\\vspace{2pt}\n\n\\begin{tabular}{llccc}\n\\toprule\nTask & Method & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\n\\multirow{3}{*}{NER}\n  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\\\\n  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\\\\n  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\\\\n\\midrule\n\\multirow{3}{*}{RE}\n  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\\\\n  & LP-selected   & 0.2845 & 0.3050 & \\textbf{$+$0.0205} \\\\\n  & Selection gap & $-$0.0068 & $+$0.0169 & \\textbf{$+$0.0237} \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel C: QE Signal Quality (Spearman $\\rho$)}}\n\\vspace{2pt}\n\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{NER ($n{=}529$)} & \\multicolumn{3}{c}{RE ($n{=}397$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & Constr. & Free & $\\Delta$ & Constr. & Free & $\\Delta$ \\\\\n\\midrule\nSJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\\\\nFK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\\\\nLP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\\\\nEM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\\\\nVC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel D: Parse Rate (Free-form)}}\n\\vspace{2pt}\n\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTotal samples          & 4408 \\\\\nParse rate             & 99.95\\% \\\\\nInstances 8/8 valid    & 549\\,/\\,551 (99.6\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\n\\end{table*}\n\n\\paragraph{CoNLL NER free-form results.}\nExtending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\\pm}0.007$ across seeds---higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\\% tied fraction under constrained decoding.\nFree-form decoding reduces the tied fraction modestly, yet selection remains below greedy: LP-selected F1${=}0.896$ vs.\\ greedy $0.904$ ($\\Delta{=}{-}0.77$~pp).\nQuality estimation under free-form decoding yields SJ $\\rho{=}0.461$, EM $\\rho{=}0.471$, LP $\\rho{=}0.326$---comparable to constrained results (Table~\\ref{tab:quality_estimation}).\nThe failure to improve selection despite reduced compression is consistent with CoNLL's low oracle headroom (4.25~pp at $N{=}8$), which limits the selection space regardless of score distribution quality.\n\n\\section{LP Selection Failure Stability}\\label{app:lp_failure_stability}\n\nWe analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.\n\n\\paragraph{Pairwise overlap.}\nLP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.\nThe 3-way intersection contains 34 instances (27.9\\% of any-seed failures), confirming a stable failure core.\n\n\\paragraph{Instance complexity drives failure.}\nTable~\\ref{tab:stable_failures} stratifies instances by failure stability.\nStable failures (all 3 seeds) involve more gold relations (2.12 vs.\\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.\nFailure rate increases monotonically with gold relation count: 4.3\\% at 1 relation, 20.7\\% at 3 relations, 26.2\\% at 6 relations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}\n\\label{tab:stable_failures}\n\\begin{tabular}{lcccc}\n\\toprule\nGroup & $n$ & Gold rels & Greedy F1 & LP $\\Delta$F1 \\\\\n\\midrule\nStable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\\\\nFail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\\\\nFail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\\\\nNever fail & 429 & 1.62 & 0.429 & $+$0.041 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Flip instances.}\nOnly 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).\nThese instances show large constrained LP errors ($\\Delta{=}{-}0.430$) that reverse under free-form decoding ($\\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.\n\n\\section{$N$-Scaling Detailed Analysis}\\label{app:n_scaling}\n\nTables~\\ref{tab:n-scaling}--\\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\\rho$).}\n\\label{tab:n-scaling}\n\\small\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{NER} $\\rho$} & \\multicolumn{3}{c}{\\textbf{RE} $\\rho$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ \\\\\n\\midrule\nSJ & 0.3641 & 0.4105 & \\textbf{+0.0464} & 0.2485 & 0.2758 & \\textbf{+0.0273} \\\\\nFK & 0.2536 & 0.2833 & \\textbf{+0.0297} & 0.2903 & 0.2964 & \\textbf{+0.0061} \\\\\nVC & 0.3861 & 0.4092 & \\textbf{+0.0231} & 0.3088 & 0.3738 & \\textbf{+0.0650} \\\\\nLP & 0.2167 & 0.2393 & \\textbf{+0.0226} & 0.2970 & 0.3100 & \\textbf{+0.0130} \\\\\nEM & 0.3071 & 0.3395 & \\textbf{+0.0324} & 0.1353 & 0.1506 & \\textbf{+0.0153} \\\\\n\\midrule\nMean & 0.3055 & 0.3364 & \\textbf{+0.0308} & 0.2560 & 0.2813 & \\textbf{+0.0253} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}\n\\label{tab:ranking-stability}\n\\small\n\\begin{tabular}{ll cc l}\n\\toprule\nModel & Task & $N$ & Kendall's $W$ & Consensus ranking \\\\\n\\midrule\nQwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\nQwen  & NER & 16 & 0.956 & SJ $\\approx$ VC $>$ EM $>$ FK $>$ LP \\\\\nQwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nQwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nLLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed standard deviation ($\\sigma$) of Spearman $\\rho$ at $N\\!=\\!8$ vs.\\ $N\\!=\\!16$ (Qwen3-8B, SciERC, 3 seeds). $\\sigma$ is population standard deviation.}\n\\label{tab:sigma-comparison}\n\\small\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{NER} $\\sigma_\\rho$} & \\multicolumn{2}{c}{\\textbf{RE} $\\sigma_\\rho$} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $N\\!=\\!8$ & $N\\!=\\!16$ \\\\\n\\midrule\nSJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\\\\nFK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\\\\nVC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\\\\nEM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\\\\nLP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\\\\n\\midrule\nMean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSignal rankings are highly stable across seeds: Kendall's $W{=}1.000$ for NER at $N{=}8$ (both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\\ref{tab:ranking-stability}).\nDoubling $N$ reduces cross-seed $\\sigma$ by 32\\% on NER and 24\\% on RE (Table~\\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\\%$ NER) and EM ($-59\\%$ NER), confirming that additional samples stabilize structural signals more than LP.\n\n\\section{Cross-Dataset OOD Analysis}\\label{app:ood}\n\nTo test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\\to$narrower schema) and vice versa (Table~\\ref{tab:ood}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-dataset OOD quality estimation (Spearman $\\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\\rho$ from Table~\\ref{tab:quality_estimation} (same model, same seed). \\textsuperscript{***}$p{<}0.001$, \\textsuperscript{*}$p{<}0.05$.}\n\\label{tab:ood}\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{SciERC$\\to$CoNLL}} & \\multicolumn{3}{c}{\\textbf{CoNLL$\\to$SciERC}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $\\rho$ & In-dom. & $\\Delta$ & $\\rho$ & In-dom. & $\\Delta$ \\\\\n\\midrule\nVC & .469\\textsuperscript{***} & .379 & +.090 & +.105\\textsuperscript{*} & .379 & $-$.274 \\\\\nSJ & .378\\textsuperscript{***} & .360 & +.018 & $-$.186\\textsuperscript{***} & .360 & $-$.546 \\\\\nEM & .300\\textsuperscript{***} & .295 & +.005 & $-$.202\\textsuperscript{***} & .295 & $-$.497 \\\\\nFK & .285\\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\\\\nLP & .246\\textsuperscript{***} & .205 & +.041 & $-$.152\\textsuperscript{***} & .205 & $-$.357 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Wider-to-narrower schema transfer.}\nWhen the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\\rho$ from Table~\\ref{tab:quality_estimation}): VC reaches $\\rho{=}0.469$ (in-domain $0.379$, $\\Delta{=}{+}0.090$), SJ $\\rho{=}0.378$ (in-domain $0.360$, $\\Delta{=}{+}0.018$), and FK $\\rho{=}0.285$ (in-domain $0.267$, $\\Delta{=}{+}0.018$).\nThe wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (greedy F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.\n\n\\paragraph{Narrower-to-wider schema transfer (excluded).}\nThe reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.\nThe CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (greedy NER F1${=}0.009$, RE F1${=}0.001$).\nUnder this regime, most signals flip to negative or near-zero correlations (Table~\\ref{tab:ood}); only VC retains weak positive correlation ($\\rho{=}0.105$, $p{=}0.016$).\nThese negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\\S\\ref{sec:qe_results}), not evidence against signal utility.\n\n\\paragraph{Asymmetry interpretation.}\nThe directional asymmetry is driven by schema coverage: wider$\\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.\nThis extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.\n\n\\section{Verbalized Confidence}\\label{app:verbalized_confidence}\n\nWe evaluate verbalized confidence (VerbConf) as a second per-sample signal following \\citet{tian2023calibration}: after generating each structured output, the model is prompted to rate its confidence on a 1--10 scale.\nTable~\\ref{tab:verbconf} reports quality estimation and selection results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Verbalized confidence (VerbConf) vs.\\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}\n\\label{tab:verbconf}\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{CoNLL NER}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nMetric & VerbConf & LP & VerbConf & LP \\\\\n\\midrule\n$\\rho$ & 0.297 & 0.205 & 0.337 & 0.316 \\\\\nAUROC & 0.681 & 0.578 & 0.747 & 0.753 \\\\\nSelection F1 & 0.620 & 0.647 & 0.889 & 0.904 \\\\\n$\\Delta$ vs.\\ greedy & $-$2.45\\,pp & $+$0.2\\,pp & $-$1.93\\,pp & $-$0.77\\,pp \\\\\n\\midrule\nMean score & 8.58\\,/\\,10 & --- & 9.24\\,/\\,10 & --- \\\\\nParse fail rate & 0.26\\% & --- & 0\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Severe overconfidence.}\nVerbConf exhibits extreme score compression: mean confidence is 8.58/10 on SciERC (greedy F1${=}0.645$) and 9.24/10 on CoNLL (greedy F1${=}0.904$), with most scores concentrated in the 8--10 range.\nThis compression is more severe than LP (which spans a 0.041-nat median range), confirming that score compression is a general property of model self-assessment, not an artifact of log-probability computation.\n\n\\paragraph{QE--selection decoupling.}\nVerbConf achieves higher $\\rho$ than LP on both datasets (SciERC: 0.297 vs.\\ 0.205; CoNLL: 0.337 vs.\\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\\ 0.578; CoNLL: 0.747 vs.\\ 0.753), yet yields the worst selection among all signals ($\\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).\nThis dissociation further demonstrates the correlation-selection gap: a signal can rank instances by expected quality without being able to discriminate candidates within an instance.\nThe AUROC--$\\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\\rho$ at 0.337) reflects differing sensitivity to binary vs.\\ ordinal discrimination.\n\n\\section{LLaMA-3.2-3B Scale Ablation}\\label{app:llama3b}\n\nTo extend scale coverage below 4B, we fine-tune LLaMA-3.2-3B-Instruct on SciERC NER under identical training conditions (LoRA rank${=}32$, $\\alpha{=}64$, 5 epochs) and evaluate quality estimation and selection (Table~\\ref{tab:llama3b}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}\n\\label{tab:llama3b}\n\\begin{tabular}{l cc cc}\n\\toprule\nSignal & $\\rho$ & AUROC & Sel.\\ F1 & $\\Delta$ vs.\\ greedy \\\\\n\\midrule\nVC & \\textbf{.460} & .743 & 0.611 & $-$1.54\\,pp \\\\\nSJ & .375 & .738 & \\textbf{0.633} & $+$0.61\\,pp \\\\\nEM & .334 & \\textbf{.776} & --- & --- \\\\\nFK & .268 & .671 & 0.630 & $+$0.28\\,pp \\\\\nLP & .266 & .633 & 0.628 & $+$0.12\\,pp \\\\\n\\midrule\nGreedy & --- & --- & 0.627 & --- \\\\\nOracle & --- & --- & 0.763 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\\ref{tab:quality_estimation}), confirming ranking stability across two model families spanning 3B--8B.\nAUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), reflecting the $\\rho$--AUROC dissociation noted in the main text.\nDespite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC---the strongest QE signal---yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.\n",
      "numLines": 959,
      "startLine": 1,
      "totalLines": 959
    }
  },
  "sourceToolAssistantUUID": "49d29f8b-b80f-48ae-89e3-50fb42ee181a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 61 · 2026-05-16T04:19:39.141Z_

```json
{
  "parentUuid": "8f5bf301-fe7b-4d21-adde-f95f8656babf",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b51c91a7-a896-48cf-877b-8b8e6c5d41e5",
  "timestamp": "2026-05-16T04:19:39.141Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 呈现**  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **页数**: 长文 8 页 +…",
  "leafUuid": "b51c91a7-a896-48cf-877b-8b8e6c5d41e5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 for structured IE confidence estimation paper",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Assistant

_source line 64 · 2026-05-16T04:19:42.731Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've now read the complete paper. Let me now search for additional related work that may be missing, and verify references. Let me also check for anonymity issues and search for more recent relevant work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b51c91a7-a896-48cf-877b-8b8e6c5d41e5",
  "isSidechain": false,
  "requestId": "req_011Cb5c4BCLeGb6G15J3Cji5",
  "type": "assistant",
  "uuid": "98563fe6-05dc-4a45-9db9-2ed6dfa26bf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158LmNoZTmb7SRGHzqMHeqb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7006,
      "cache_creation_input_tokens": 36489,
      "cache_read_input_tokens": 34565,
      "output_tokens": 432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7006,
          "output_tokens": 432,
          "cache_read_input_tokens": 34565,
          "cache_creation_input_tokens": 36489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36489
          },
          "type": "message"
        }
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

_source line 65 · 2026-05-16T04:19:43.717Z_

论文全文已读完。现在并行搜索更多可能遗漏的相关工作，并验证引用完整性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98563fe6-05dc-4a45-9db9-2ed6dfa26bf2",
  "isSidechain": false,
  "requestId": "req_011Cb5c4BCLeGb6G15J3Cji5",
  "type": "assistant",
  "uuid": "33a93679-b23f-4589-b176-a9a4b6cc50c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158LmNoZTmb7SRGHzqMHeqb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7006,
      "cache_creation_input_tokens": 36489,
      "cache_read_input_tokens": 34565,
      "output_tokens": 432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7006,
          "output_tokens": 432,
          "cache_read_input_tokens": 34565,
          "cache_creation_input_tokens": 36489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36489
          },
          "type": "message"
        }
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

_source line 66 · 2026-05-16T04:19:44.824Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UurVobeXCFg426yyhb49mt`</summary>

```json
{
  "query": "confidence estimation NER relation extraction LLM 2025 2026 learned verifier reward model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33a93679-b23f-4589-b176-a9a4b6cc50c0",
  "isSidechain": false,
  "requestId": "req_011Cb5c4BCLeGb6G15J3Cji5",
  "type": "assistant",
  "uuid": "a0cf2555-c30a-48ad-8419-d1c1f56dd752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158LmNoZTmb7SRGHzqMHeqb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7006,
      "cache_creation_input_tokens": 36489,
      "cache_read_input_tokens": 34565,
      "output_tokens": 432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7006,
          "output_tokens": 432,
          "cache_read_input_tokens": 34565,
          "cache_creation_input_tokens": 36489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36489
          },
          "type": "message"
        }
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

_source line 67 · 2026-05-16T04:19:45.152Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Av3nG939GvqC4T98vz8fX3`</summary>

```json
{
  "query": "test-time compute scaling structured output information extraction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0cf2555-c30a-48ad-8419-d1c1f56dd752",
  "isSidechain": false,
  "requestId": "req_011Cb5c4BCLeGb6G15J3Cji5",
  "type": "assistant",
  "uuid": "2be7f878-385b-4e50-a39d-47e4e260f36b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158LmNoZTmb7SRGHzqMHeqb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7006,
      "cache_creation_input_tokens": 36489,
      "cache_read_input_tokens": 34565,
      "output_tokens": 432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7006,
          "output_tokens": 432,
          "cache_read_input_tokens": 34565,
          "cache_creation_input_tokens": 36489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36489
          },
          "type": "message"
        }
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

_source line 68 · 2026-05-16T04:19:45.625Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H9BuAactzcCJTHg4XgW8uC`</summary>

```json
{
  "query": "semantic uncertainty structured prediction set-valued output 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2be7f878-385b-4e50-a39d-47e4e260f36b",
  "isSidechain": false,
  "requestId": "req_011Cb5c4BCLeGb6G15J3Cji5",
  "type": "assistant",
  "uuid": "7244aa4b-fcb4-495a-8f60-d829d597b718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158LmNoZTmb7SRGHzqMHeqb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7006,
      "cache_creation_input_tokens": 36489,
      "cache_read_input_tokens": 34565,
      "output_tokens": 432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7006,
          "output_tokens": 432,
          "cache_read_input_tokens": 34565,
          "cache_creation_input_tokens": 36489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36489
          },
          "type": "message"
        }
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

_source line 69 · 2026-05-16T04:19:47.375Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NiYnj7LN2SKTVS8M5pfEQ8`</summary>

```json
{
  "query": "\"correlation-selection gap\" OR \"quality estimation\" OR \"best-of-N selection\" structured prediction NER 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7244aa4b-fcb4-495a-8f60-d829d597b718",
  "isSidechain": false,
  "requestId": "req_011Cb5c4BCLeGb6G15J3Cji5",
  "type": "assistant",
  "uuid": "7a67e3dc-5425-4b12-a5bc-5ef250c9796d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158LmNoZTmb7SRGHzqMHeqb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7006,
      "cache_creation_input_tokens": 36489,
      "cache_read_input_tokens": 34565,
      "output_tokens": 432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7006,
          "output_tokens": 432,
          "cache_read_input_tokens": 34565,
          "cache_creation_input_tokens": 36489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36489
          },
          "type": "message"
        }
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

_source line 70 · 2026-05-16T04:19:48.936Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01UgEHwG5Aiv5rfm8PgYCe3v`</summary>

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
  "parentUuid": "7a67e3dc-5425-4b12-a5bc-5ef250c9796d",
  "isSidechain": false,
  "requestId": "req_011Cb5c4BCLeGb6G15J3Cji5",
  "type": "assistant",
  "uuid": "2850ffcd-8f99-4f03-bc60-d1d8015c0cc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158LmNoZTmb7SRGHzqMHeqb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7006,
      "cache_creation_input_tokens": 36489,
      "cache_read_input_tokens": 34565,
      "output_tokens": 432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7006,
          "output_tokens": 432,
          "cache_read_input_tokens": 34565,
          "cache_creation_input_tokens": 36489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36489
          },
          "type": "message"
        }
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

_source line 71 · 2026-05-16T04:19:51.758Z_

<details><summary>↩ Tool result · `toolu_01UurVobeXCFg426yyhb49mt`</summary>

```text
Web search results for query: "confidence estimation NER relation extraction LLM 2025 2026 learned verifier reward model"

Links: [{"title":"GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-RLVR"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2503.02623"},{"title":"GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub","url":"https://github.com/bobxwu/learning-from-rewards-llm-papers"},{"title":"Reinforcement Learning with Verifiable Rewards Implicitly ...","url":"https://arxiv.org/pdf/2506.14245"},{"title":"taming overconfidence in llms: reward calibration in rlhf","url":"https://arxiv.org/pdf/2410.09724"},{"title":"[2506.14245] Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs","url":"https://arxiv.org/abs/2506.14245"},{"title":"Large language model augmented joint learning framework for entity-relation extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1568494625014073"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Reinforcement+Learning+with+Verifiable+Rewards+(RLVR)"},{"title":"Mind the Generation Process: Fine-Grained Confidence Estimation During LLM Generation","url":"https://arxiv.org/html/2508.12040v1"},{"title":"RLVR: Verifiable Rewards for Reliable Enterprise LLMs | Appen","url":"https://www.appen.com/blog/rlvr"}]

The search has returned relevant results on confidence estimation, learned verifier reward models, and reinforcement learning with verifiable rewards (RLVR) for LLMs in 2025-2026. Here are the key findings:

## Confidence Estimation and Reward Models for LLMs

Recent research on confidence estimation shows that methods like "Rewarding Doubt" produce more useful and actionable confidence estimates and consistently outperform baseline approaches like Trained Probe, demonstrating stronger ability to generalize to new datasets.

A novel approach models confidence estimation as a betting game using a reward function based on the logarithmic scoring rule—a strictly proper scoring rule—which is the first to be optimized through reinforcement-learning-based policy optimization to directly train confidence calibration in LLM generations.

## Reinforcement Learning with Verifiable Rewards (RLVR)

RLVR has emerged as an indispensable paradigm for enhancing reasoning in Large Language Models, though standard policy optimization methods like GRPO often converge to low-entropy policies, leading to severe mode collapse and limited output diversity.

Recent research demonstrates that RLVR can extend the reasoning boundary for both mathematical and coding tasks, supported by a novel evaluation metric called CoT-Pass@K, which captures reasoning success by accounting for both the final answer and intermediate reasoning steps.

## Practical Applications

RLVR trains models to earn rewards only when outputs pass programmatic checks—the system samples multiple candidates, runs them through verifiers, and updates the policy toward behaviors that pass, with verifier-based rewards incentivizing correct reasoning and supporting evaluations that check both the answer and chain of thought.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0cf2555-c30a-48ad-8419-d1c1f56dd752",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "f64769b7-a588-4d1c-ba5f-39684aa3fdca",
  "toolUseResult": {
    "query": "confidence estimation NER relation extraction LLM 2025 2026 learned verifier reward model",
    "results": [
      {
        "tool_use_id": "srvtoolu_01W4Hi7WYZqM8dFtxd5jCj62",
        "content": [
          {
            "title": "GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub",
            "url": "https://github.com/opendilab/awesome-RLVR"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2503.02623"
          },
          {
            "title": "GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub",
            "url": "https://github.com/bobxwu/learning-from-rewards-llm-papers"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards Implicitly ...",
            "url": "https://arxiv.org/pdf/2506.14245"
          },
          {
            "title": "taming overconfidence in llms: reward calibration in rlhf",
            "url": "https://arxiv.org/pdf/2410.09724"
          },
          {
            "title": "[2506.14245] Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs",
            "url": "https://arxiv.org/abs/2506.14245"
          },
          {
            "title": "Large language model augmented joint learning framework for entity-relation extraction - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S1568494625014073"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Reinforcement+Learning+with+Verifiable+Rewards+(RLVR)"
          },
          {
            "title": "Mind the Generation Process: Fine-Grained Confidence Estimation During LLM Generation",
            "url": "https://arxiv.org/html/2508.12040v1"
          },
          {
            "title": "RLVR: Verifiable Rewards for Reliable Enterprise LLMs | Appen",
            "url": "https://www.appen.com/blog/rlvr"
          }
        ]
      },
      "The search has returned relevant results on confidence estimation, learned verifier reward models, and reinforcement learning with verifiable rewards (RLVR) for LLMs in 2025-2026. Here are the key findings:\n\n## Confidence Estimation and Reward Models for LLMs\n\nRecent research on confidence estimation shows that methods like \"Rewarding Doubt\" produce more useful and actionable confidence estimates and consistently outperform baseline approaches like Trained Probe, demonstrating stronger ability to generalize to new datasets.\n\nA novel approach models confidence estimation as a betting game using a reward function based on the logarithmic scoring rule—a strictly proper scoring rule—which is the first to be optimized through reinforcement-learning-based policy optimization to directly train confidence calibration in LLM generations.\n\n## Reinforcement Learning with Verifiable Rewards (RLVR)\n\nRLVR has emerged as an indispensable paradigm for enhancing reasoning in Large Language Models, though standard policy optimization methods like GRPO often converge to low-entropy policies, leading to severe mode collapse and limited output diversity.\n\nRecent research demonstrates that RLVR can extend the reasoning boundary for both mathematical and coding tasks, supported by a novel evaluation metric called CoT-Pass@K, which captures reasoning success by accounting for both the final answer and intermediate reasoning steps.\n\n## Practical Applications\n\nRLVR trains models to earn rewards only when outputs pass programmatic checks—the system samples multiple candidates, runs them through verifiers, and updates the policy toward behaviors that pass, with verifier-based rewards incentivizing correct reasoning and supporting evaluations that check both the answer and chain of thought."
    ],
    "durationSeconds": 6.929894238999994
  },
  "sourceToolAssistantUUID": "a0cf2555-c30a-48ad-8419-d1c1f56dd752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-16T04:19:52.435Z_

<details><summary>↩ Tool result · `toolu_01Av3nG939GvqC4T98vz8fX3`</summary>

```text
Web search results for query: "test-time compute scaling structured output information extraction 2025 2026"

Links: [{"title":"What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models","url":"https://testtimescaling.github.io/"},{"title":"[2512.02008] The Art of Scaling Test-Time Compute for Large Language Models","url":"https://arxiv.org/abs/2512.02008"},{"title":"Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=BMJ3pyYxu2"},{"title":"Scaling Test-Time Compute to Achieve IOI Gold Medal with Open-Weight Models","url":"https://arxiv.org/html/2510.14232v2"},{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"Inference-Time Scaling of Verification: Self-Evolving Deep Research Agents via Test-Time Rubric-Guided Verification","url":"https://arxiv.org/html/2601.15808v2"},{"title":"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview","url":"https://openreview.net/forum?id=4FWAwZtd2n"},{"title":"Scaling Test-Time Compute for Agentic Coding","url":"https://www.emergentmind.com/papers/2604.16529"},{"title":"[2604.16529] Scaling Test-Time Compute for Agentic Coding","url":"https://arxiv.org/abs/2604.16529"},{"title":"[2503.24235] A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?","url":"https://arxiv.org/abs/2503.24235"}]

Here are the search results for your query about test-time compute scaling, structured output, and information extraction in 2025-2026:

## Key Research Areas

**Test-Time Scaling Overview**

Test-time scaling (TTS) has emerged as a prominent research focus, with recent studies demonstrating that it can elicit problem-solving capabilities of LLMs, enabling breakthroughs in specialized reasoning tasks like mathematics and coding, as well as general tasks like open-ended Q&A.

**Comprehensive Survey Framework**

A unified framework has been proposed structured along four core dimensions of TTS research: what to scale, how to scale, where to scale, and how well to scale.

**Structured Output Applications**

Several recent works focus on structured representations for test-time compute:

- One framework converts each rollout into a structured summary that preserves salient hypotheses, progress, and failure modes while discarding low-signal trace details for agentic coding.

- Forest-of-Thought employs sparse activation strategies to select relevant reasoning paths and introduces dynamic self-correction strategies for real-time error correction and consensus-guided decision-making.

**Reasoning and Verification**

Recent work formalizes agent reflection pipelines for Deep Research Agents and introduces comprehensive failure taxonomies to categorize failures systematically and derive structured rubrics for outcome-based rewards.

**Practical Applications**

GenCluster is a scalable test-time compute framework that combines large-scale generation, behavioral clustering, ranking, and submission strategies to efficiently explore solution spaces, with performance scaling consistently with available compute.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2be7f878-385b-4e50-a39d-47e4e260f36b",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "d1c082a9-ea8d-4366-bce2-58080d5b0e44",
  "toolUseResult": {
    "query": "test-time compute scaling structured output information extraction 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015yF3mfbpk22abwy2fNcoEV",
        "content": [
          {
            "title": "What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models",
            "url": "https://testtimescaling.github.io/"
          },
          {
            "title": "[2512.02008] The Art of Scaling Test-Time Compute for Large Language Models",
            "url": "https://arxiv.org/abs/2512.02008"
          },
          {
            "title": "Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=BMJ3pyYxu2"
          },
          {
            "title": "Scaling Test-Time Compute to Achieve IOI Gold Medal with Open-Weight Models",
            "url": "https://arxiv.org/html/2510.14232v2"
          },
          {
            "title": "GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub",
            "url": "https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"
          },
          {
            "title": "Inference-Time Scaling of Verification: Self-Evolving Deep Research Agents via Test-Time Rubric-Guided Verification",
            "url": "https://arxiv.org/html/2601.15808v2"
          },
          {
            "title": "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=4FWAwZtd2n"
          },
          {
            "title": "Scaling Test-Time Compute for Agentic Coding",
            "url": "https://www.emergentmind.com/papers/2604.16529"
          },
          {
            "title": "[2604.16529] Scaling Test-Time Compute for Agentic Coding",
            "url": "https://arxiv.org/abs/2604.16529"
          },
          {
            "title": "[2503.24235] A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?",
            "url": "https://arxiv.org/abs/2503.24235"
          }
        ]
      },
      "Here are the search results for your query about test-time compute scaling, structured output, and information extraction in 2025-2026:\n\n## Key Research Areas\n\n**Test-Time Scaling Overview**\n\nTest-time scaling (TTS) has emerged as a prominent research focus, with recent studies demonstrating that it can elicit problem-solving capabilities of LLMs, enabling breakthroughs in specialized reasoning tasks like mathematics and coding, as well as general tasks like open-ended Q&A.\n\n**Comprehensive Survey Framework**\n\nA unified framework has been proposed structured along four core dimensions of TTS research: what to scale, how to scale, where to scale, and how well to scale.\n\n**Structured Output Applications**\n\nSeveral recent works focus on structured representations for test-time compute:\n\n- One framework converts each rollout into a structured summary that preserves salient hypotheses, progress, and failure modes while discarding low-signal trace details for agentic coding.\n\n- Forest-of-Thought employs sparse activation strategies to select relevant reasoning paths and introduces dynamic self-correction strategies for real-time error correction and consensus-guided decision-making.\n\n**Reasoning and Verification**\n\nRecent work formalizes agent reflection pipelines for Deep Research Agents and introduces comprehensive failure taxonomies to categorize failures systematically and derive structured rubrics for outcome-based rewards.\n\n**Practical Applications**\n\nGenCluster is a scalable test-time compute framework that combines large-scale generation, behavioral clustering, ranking, and submission strategies to efficiently explore solution spaces, with performance scaling consistently with available compute."
    ],
    "durationSeconds": 7.280379562000002
  },
  "sourceToolAssistantUUID": "2be7f878-385b-4e50-a39d-47e4e260f36b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-16T04:19:52.749Z_

<details><summary>↩ Tool result · `toolu_01H9BuAactzcCJTHg4XgW8uC`</summary>

```text
Web search results for query: "semantic uncertainty structured prediction set-valued output 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2025 CONFORMAL STRUCTURED PREDICTION","url":"https://par.nsf.gov/servlets/purl/10610745"},{"title":"Conformal Prediction: A Data Perspective | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3736575"},{"title":"Conformal Structured Prediction | OpenReview","url":"https://openreview.net/forum?id=mKfmLQXP6J"},{"title":"An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12375657/"},{"title":"A Survey on Uncertainty Quantification of Large Language Models: Taxonomy, Open Research Challenges, and Future Directions | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3744238"},{"title":"Beyond Semantic Entropy: Boosting LLM Uncertainty ...","url":"https://aclanthology.org/2025.findings-acl.234.pdf"},{"title":"Improving Uncertainty Estimation through Semantically Diverse Language Generation | OpenReview","url":"https://openreview.net/forum?id=HSi4VetQLj"},{"title":"Possibilistic Predictive Uncertainty for Deep Learning","url":"https://arxiv.org/html/2605.00600"},{"title":"Uncertainty in Structured Prediction | Request PDF","url":"https://www.researchgate.net/publication/339350628_Uncertainty_in_Structured_Prediction"}]

Based on the search results, here's an overview of recent research on semantic uncertainty, structured prediction, and set-valued outputs from 2025-2026:

## Key Research Areas

### Semantic Uncertainty in Language Models

Recent work on Semantically Diverse Language Generation (SDLG) steers LLMs to generate semantically diverse yet likely alternatives for an initially generated text, providing a precise measure of aleatoric semantic uncertainty and detecting whether initial text is likely to be hallucinated.

### Conformal Structured Prediction

Conformal prediction replaces a traditional model with a conformal predictor that outputs a set of labels capturing the model's uncertainty. For complex structured outputs such as text generation, traditional prediction sets might include a large number of labels and be hard to interpret. Recent frameworks modify conformal prediction algorithms to output structured prediction sets that implicitly represent sets of labels.

### Set-Valued Outputs

Recent neural network approaches include RS-NN (2025) which predicts set-valued outputs. This represents an emerging direction for uncertainty quantification through explicit set-valued predictions.

### Broader Uncertainty Quantification

Conformal prediction is a distribution-free uncertainty quantification framework that reliably provides valid predictive inference for black-box models by constructing prediction sets or intervals that contain the true output with a specified probability. Existing methods categorize uncertainty quantification approaches for LLMs into four main classes: token-level, self-verbalized, semantic-similarity, and mechanistic interpretability methods.

These research directions address the challenge of providing interpretable, reliable uncertainty estimates for complex prediction tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7244aa4b-fcb4-495a-8f60-d829d597b718",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "7f8c4360-3563-4743-89e6-3e4436f4d753",
  "toolUseResult": {
    "query": "semantic uncertainty structured prediction set-valued output 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ELsNxVRNuQYoDSjjt3EzcQ",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 CONFORMAL STRUCTURED PREDICTION",
            "url": "https://par.nsf.gov/servlets/purl/10610745"
          },
          {
            "title": "Conformal Prediction: A Data Perspective | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3736575"
          },
          {
            "title": "Conformal Structured Prediction | OpenReview",
            "url": "https://openreview.net/forum?id=mKfmLQXP6J"
          },
          {
            "title": "An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12375657/"
          },
          {
            "title": "A Survey on Uncertainty Quantification of Large Language Models: Taxonomy, Open Research Challenges, and Future Directions | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3744238"
          },
          {
            "title": "Beyond Semantic Entropy: Boosting LLM Uncertainty ...",
            "url": "https://aclanthology.org/2025.findings-acl.234.pdf"
          },
          {
            "title": "Improving Uncertainty Estimation through Semantically Diverse Language Generation | OpenReview",
            "url": "https://openreview.net/forum?id=HSi4VetQLj"
          },
          {
            "title": "Possibilistic Predictive Uncertainty for Deep Learning",
            "url": "https://arxiv.org/html/2605.00600"
          },
          {
            "title": "Uncertainty in Structured Prediction | Request PDF",
            "url": "https://www.researchgate.net/publication/339350628_Uncertainty_in_Structured_Prediction"
          }
        ]
      },
      "Based on the search results, here's an overview of recent research on semantic uncertainty, structured prediction, and set-valued outputs from 2025-2026:\n\n## Key Research Areas\n\n### Semantic Uncertainty in Language Models\n\nRecent work on Semantically Diverse Language Generation (SDLG) steers LLMs to generate semantically diverse yet likely alternatives for an initially generated text, providing a precise measure of aleatoric semantic uncertainty and detecting whether initial text is likely to be hallucinated.\n\n### Conformal Structured Prediction\n\nConformal prediction replaces a traditional model with a conformal predictor that outputs a set of labels capturing the model's uncertainty. For complex structured outputs such as text generation, traditional prediction sets might include a large number of labels and be hard to interpret. Recent frameworks modify conformal prediction algorithms to output structured prediction sets that implicitly represent sets of labels.\n\n### Set-Valued Outputs\n\nRecent neural network approaches include RS-NN (2025) which predicts set-valued outputs. This represents an emerging direction for uncertainty quantification through explicit set-valued predictions.\n\n### Broader Uncertainty Quantification\n\nConformal prediction is a distribution-free uncertainty quantification framework that reliably provides valid predictive inference for black-box models by constructing prediction sets or intervals that contain the true output with a specified probability. Existing methods categorize uncertainty quantification approaches for LLMs into four main classes: token-level, self-verbalized, semantic-similarity, and mechanistic interpretability methods.\n\nThese research directions address the challenge of providing interpretable, reliable uncertainty estimates for complex prediction tasks."
    ],
    "durationSeconds": 7.122007588000008
  },
  "sourceToolAssistantUUID": "7244aa4b-fcb4-495a-8f60-d829d597b718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 74_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 呈现**  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **页数**: 长文 8 页 +…",
  "leafUuid": "7f8c4360-3563-4743-89e6-3e4436f4d753",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Runtime record

_source line 75_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 for structured IE confidence estimation paper",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Tool result

_source line 76 · 2026-05-16T04:19:53.998Z_

<details><summary>↩ Tool result · `toolu_01NiYnj7LN2SKTVS8M5pfEQ8`</summary>

```text
Web search results for query: ""correlation-selection gap" OR "quality estimation" OR "best-of-N selection" structured prediction NER 2025 2026"

Links: [{"title":"SubLIME: Subset Selection via Rank Correlation Prediction ...","url":"https://aclanthology.org/2025.acl-long.1477.pdf"},{"title":"SubLIME: Subset Selection via Rank Correlation Prediction for Data-Efficient LLM Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1477/"},{"title":"NeurIPS 2025 Papers with Code & Data – Paper Digest","url":"https://www.paperdigest.org/2025/11/neurips-2025-papers-with-code-data/"},{"title":"Awards - ACL 2025","url":"https://2025.aclweb.org/program/awards/"},{"title":"Evaluating Prediction Performance: A Simulation Study Comparing Penalized and Classical Variable Selection Methods in Low-Dimensional Data","url":"https://www.mdpi.com/2076-3417/15/13/7443"},{"title":"Prediction in Future Samples Studied in Terms of the Gain from Selection | Psychometrika | Cambridge Core","url":"https://www.cambridge.org/core/journals/psychometrika/article/abs/prediction-in-future-samples-studied-in-terms-of-the-gain-from-selection/6AD2B07188FE92880719B7247DF2CB90"},{"title":"Machine Learning Jul 2025","url":"https://www.arxiv.org/list/cs.LG/2025-07?skip=675&show=1000"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=550&show=2000"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=1500&show=2000"},{"title":"Overcoming Common Flaws in the Evaluation of Selective Classification Systems","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/047c84ec50bd8ea29349b996fc64af4b-Paper-Conference.pdf"}]

I've completed the web search for your query. Here's a summary of the most relevant findings:

## Key Results:

**SubLIME: Subset Selection via Rank Correlation Prediction (ACL 2025)**

The most directly relevant result is SubLIME, which trains a Rank Correlation Prediction (RCP) model combining limited performance data from 5-20 anchor LLMs with dataset intrinsic metrics (Difficulty, Quality, and Distributional Dispersion) to predict how closely a candidate subset reflects full-benchmark rankings, and selects a "winning" subset (1-20% of full set data) for evaluating new LLMs while preserving global rankings. This work was presented at the 63rd Annual Meeting of the Association for Computational Linguistics in July 2025 in Vienna, Austria.

**Related Research:**

The search also returned work on selective classification systems, including the AUGRC (Area Under the Generalized Risk Coverage) curve, a metric designed to overcome flaws of current multi-threshold metrics for selective classification systems.

**Note on NER and Structured Prediction:**

While your query included terms related to structured prediction and NER (Named Entity Recognition), the search results primarily focused on subset selection and quality estimation for LLM evaluation rather than NER-specific applications. The SubLIME paper appears to be the most relevant match to your search terms, particularly regarding quality estimation and selection mechanisms in the 2025 timeframe.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a67e3dc-5425-4b12-a5bc-5ef250c9796d",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "ef1b1d3c-6597-4874-9283-d35c98b8327c",
  "toolUseResult": {
    "query": "\"correlation-selection gap\" OR \"quality estimation\" OR \"best-of-N selection\" structured prediction NER 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FQdw9E3Evu5GcCAsa4KD5W",
        "content": [
          {
            "title": "SubLIME: Subset Selection via Rank Correlation Prediction ...",
            "url": "https://aclanthology.org/2025.acl-long.1477.pdf"
          },
          {
            "title": "SubLIME: Subset Selection via Rank Correlation Prediction for Data-Efficient LLM Evaluation - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.1477/"
          },
          {
            "title": "NeurIPS 2025 Papers with Code & Data – Paper Digest",
            "url": "https://www.paperdigest.org/2025/11/neurips-2025-papers-with-code-data/"
          },
          {
            "title": "Awards - ACL 2025",
            "url": "https://2025.aclweb.org/program/awards/"
          },
          {
            "title": "Evaluating Prediction Performance: A Simulation Study Comparing Penalized and Classical Variable Selection Methods in Low-Dimensional Data",
            "url": "https://www.mdpi.com/2076-3417/15/13/7443"
          },
          {
            "title": "Prediction in Future Samples Studied in Terms of the Gain from Selection | Psychometrika | Cambridge Core",
            "url": "https://www.cambridge.org/core/journals/psychometrika/article/abs/prediction-in-future-samples-studied-in-terms-of-the-gain-from-selection/6AD2B07188FE92880719B7247DF2CB90"
          },
          {
            "title": "Machine Learning Jul 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-07?skip=675&show=1000"
          },
          {
            "title": "Machine Learning Sep 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-09?skip=550&show=2000"
          },
          {
            "title": "Machine Learning May 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-05?skip=1500&show=2000"
          },
          {
            "title": "Overcoming Common Flaws in the Evaluation of Selective Classification Systems",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/047c84ec50bd8ea29349b996fc64af4b-Paper-Conference.pdf"
          }
        ]
      },
      "I've completed the web search for your query. Here's a summary of the most relevant findings:\n\n## Key Results:\n\n**SubLIME: Subset Selection via Rank Correlation Prediction (ACL 2025)**\n\nThe most directly relevant result is SubLIME, which trains a Rank Correlation Prediction (RCP) model combining limited performance data from 5-20 anchor LLMs with dataset intrinsic metrics (Difficulty, Quality, and Distributional Dispersion) to predict how closely a candidate subset reflects full-benchmark rankings, and selects a \"winning\" subset (1-20% of full set data) for evaluating new LLMs while preserving global rankings. This work was presented at the 63rd Annual Meeting of the Association for Computational Linguistics in July 2025 in Vienna, Austria.\n\n**Related Research:**\n\nThe search also returned work on selective classification systems, including the AUGRC (Area Under the Generalized Risk Coverage) curve, a metric designed to overcome flaws of current multi-threshold metrics for selective classification systems.\n\n**Note on NER and Structured Prediction:**\n\nWhile your query included terms related to structured prediction and NER (Named Entity Recognition), the search results primarily focused on subset selection and quality estimation for LLM evaluation rather than NER-specific applications. The SubLIME paper appears to be the most relevant match to your search terms, particularly regarding quality estimation and selection mechanisms in the 2025 timeframe."
    ],
    "durationSeconds": 6.620068529999997
  },
  "sourceToolAssistantUUID": "7a67e3dc-5425-4b12-a5bc-5ef250c9796d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-16T04:20:31.563Z_

<details><summary>↩ Tool result · `toolu_01UgEHwG5Aiv5rfm8PgYCe3v`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 44, \"total_citations\": 66, \"unique_cited_keys\": 44, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 38, \"online_not_found\": 3, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"W-NUT Workshop at EMNLP 2017\"}, {\"key\": \"eikema2022sampling\", \"type\": \"inproceedings\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"authors\": \"Eikema, Bryan and Aziz, Wilker\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"freitag2022high\", \"type\": \"article\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"authors\": \"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\", \"year\": \"2022\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"fleiss1971agreement\", \"type\": \"article\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"authors\": \"Fleiss, Joseph L.\", \"year\": \"1971\", \"venue\": \"Psychological Bulletin\"}, {\"key\": \"feng2025optimal\", \"type\": \"article\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"authors\": \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.12309\"}, {\"key\": \"geng2024confidence\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"hobelsberger2025systematic\", \"type\": \"article\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"authors\": \"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.20460\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kang2025selfcertainty\", \"type\": \"inproceedings\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"authors\": \"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"kim2026reasc\", \"type\": \"inproceedings\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"authors\": \"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\", \"year\": \"2026\", \"venue\": \"ACL 2026\"}, {\"key\": \"li2025llms\", \"type\": \"article\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"authors\": \"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.04104\"}, {\"key\": \"kuhn2023semantic\", \"type\": \"inproceedings\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"authors\": \"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"malinin2021uncertainty\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"authors\": \"Malinin, Andrey and Gales, Mark\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"li2023codeie\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lightman2024verify\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"luan2018scierc\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"authors\": \"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"manakul2023selfcheckgpt\", \"type\": \"inproceedings\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"authors\": \"Manakul, Potsawee and Liusie, Adian and Gales, Mark\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"yao2026consistency\", \"type\": \"article\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\", \"authors\": \"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\", \"year\": \"2026\", \"venue\": \"Genomics \\\\& Informatics\"}, {\"key\": \"oh2025latentsc\", \"type\": \"article\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"authors\": \"Oh, Jungsuk and Lee, Jay-Yoon\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.18395\"}, {\"key\": \"sainz2024gollie\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"snell2025scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"authors\": \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"taubenfeld2025cisc\", \"type\": \"inproceedings\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"authors\": \"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"thirukovalluru2024atomic\", \"type\": \"inproceedings\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"authors\": \"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"tjongkimsang2003conll\", \"type\": \"inproceedings\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"authors\": \"Sang, Erik F. Tjong Kim and Meulder, Fien De\", \"year\": \"2003\", \"venue\": \"CoNLL 2003\"}, {\"key\": \"vashurin2025cocoa\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"authors\": \"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"wadhwa2023revisiting\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"wang2023selfconsistency\", \"type\": \"inproceedings\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"authors\": \"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"wang2025make\", \"type\": \"inproceedings\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"authors\": \"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2025\"}, {\"key\": \"wang2025rankedvoting\", \"type\": \"inproceedings\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"authors\": \"Wang, Weiqin and Wang, Yile and Huang, Hui\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"willard2023guided\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, Rémi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"xia2025survey\", \"type\": \"inproceedings\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"authors\": \"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"zheng2024llamafactory\", \"type\": \"inproceedings\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"authors\": \"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"zhou2024uniner\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"muller2021understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"authors\": \"M\\\\\\\"uller, Mathias and Sennrich, Rico\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"eikema2025structured\", \"type\": \"inproceedings\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"authors\": \"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"venktesh2025trust\", \"type\": \"article\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"authors\": \"Venktesh, V and Rathee, Mandeep and Anand, Avishek\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.16665\"}, {\"key\": \"jinnai2024mbr\", \"type\": \"inproceedings\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"authors\": \"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}, {\"key\": \"ratinov2009design\", \"type\": \"inproceedings\", \"title\": \"Design Challenges and Misconceptions in Named Entity Recognition\", \"authors\": \"Ratinov, Lev and Roth, Dan\", \"year\": \"2009\", \"venue\": \"Proceedings of the Thirteenth Conference on Computational Natural Language Learn...\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"type\": \"inproceedings\", \"title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"authors\": \"Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan\", \"year\": \"2012\", \"venue\": \"Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Languag...\"}, {\"key\": \"tian2023calibration\", \"type\": \"inproceedings\", \"title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models\", \"authors\": \"Tian, Katherine and Mitchell, Eric and Yao, Huaxiu and Manning, Christopher D. a...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}], \"tex_citations\": [{\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"yao2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/introduction.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/introduction.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/introduction.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"thirukovalluru2024atomic\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"manakul2023selfcheckgpt\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"kim2026reasc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wang2025rankedvoting\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"oh2025latentsc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"feng2025optimal\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"wang2025make\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"li2025llms\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"yao2026consistency\", \"file\": \"sections/related_work.tex\", \"line\": 10, \"command\": \"citet\"}, {\"key\": \"vashurin2025cocoa\", \"file\": \"sections/related_work.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"culotta2004confidence\", \"file\": \"sections/related_work.tex\", \"line\": 12, \"command\": \"citet\"}, {\"key\": \"zhou2024uniner\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"sainz2024gollie\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"li2023codeie\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"wadhwa2023revisiting\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"geng2024confidence\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"xia2025survey\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"hobelsberger2025systematic\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"kadavath2022language\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"malinin2021uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"citet\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/related_work.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"lightman2024verify\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/method.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fleiss1971agreement\", \"file\": \"sections/method.tex\", \"line\": 25, \"command\": \"citet\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/experiments.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/experiments.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"zheng2024llamafactory\", \"file\": \"sections/experiments.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/experiments.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/experiments.tex\", \"line\": 91, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/discussion.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/discussion.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"venktesh2025trust\", \"file\": \"sections/discussion.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"tian2023calibration\", \"file\": \"sections/limitations.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/appendix.tex\", \"line\": 252, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/appendix.tex\", \"line\": 252, \"command\": \"cite\"}, {\"key\": \"ratinov2009design\", \"file\": \"sections/appendix.tex\", \"line\": 387, \"command\": \"cite\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"file\": \"sections/appendix.tex\", \"line\": 388, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/appendix.tex\", \"line\": 474, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/appendix.tex\", \"line\": 649, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/appendix.tex\", \"line\": 649, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/appendix.tex\", \"line\": 650, \"command\": \"cite\"}, {\"key\": \"jinnai2024mbr\", \"file\": \"sections/appendix.tex\", \"line\": 650, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/appendix.tex\", \"line\": 651, \"command\": \"citet\"}, {\"key\": \"tian2023calibration\", \"file\": \"sections/appendix.tex\", \"line\": 897, \"command\": \"citet\"}], \"online_verification\": [{\"key\": \"brown2024monkeys\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024usc\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Self-Consistency for Large Language Model Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021verifiers\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culotta2004confidence\", \"title\": \"Confidence Estimation for Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence estimation for information extraction\", \"matched_year\": \"2004\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"derczynski2017wnut\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eikema2022sampling\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"freitag2022high\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fleiss1971agreement\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring nominal scale agreement among many raters.\", \"matched_year\": \"1971\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feng2025optimal\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=feng vs api=austin\"], \"note\": \"\"}, {\"key\": \"geng2024confidence\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hobelsberger2025systematic\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.236, \"matched_title\": \"A new criterion for assessing discriminant validity in variance-based structural equation modeling\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.24 below threshold 0.82\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2025selfcertainty\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2026reasc\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025llms\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuhn2023semantic\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"malinin2021uncertainty\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023codeie\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lightman2024verify\", \"title\": \"Let's Verify Step by Step\", \"status\": \"not_found\", \"confidence\": 0.246, \"matched_title\": \"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"luan2018scierc\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"manakul2023selfcheckgpt\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yao2026consistency\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oh2025latentsc\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sainz2024gollie\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"snell2025scaling\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=snell vs api=charlie\"], \"note\": \"\"}, {\"key\": \"taubenfeld2025cisc\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence Improves Self-Consistency in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thirukovalluru2024atomic\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tjongkimsang2003conll\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"matched_year\": \"2003\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vashurin2025cocoa\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa2023revisiting\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023selfconsistency\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025make\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025rankedvoting\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023guided\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2025survey\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zheng2024llamafactory\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024uniner\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"muller2021understanding\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"matched_year\": \"2021\", \"mismatch_fields\": [\"first_author: bib=m\\\\\\\"uller vs api=müller\"], \"note\": \"\"}, {\"key\": \"eikema2025structured\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"venktesh2025trust\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"status\": \"not_found\", \"confidence\": 0.252, \"matched_title\": \"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"jinnai2024mbr\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ratinov2009design\", \"title\": \"Design Challenges and Misconceptions in Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Design challenges and misconceptions in named entity recognition\", \"matched_year\": \"2009\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"matched_year\": \"2012\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tian2023calibration\", \"title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models\", \"status\": \"verified\", \"confidence\": 0.866, \"matched_title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2850ffcd-8f99-4f03-bc60-d1d8015c0cc3",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "73a67321-b10a-44e3-866d-fb4323f3bd35",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 44, \\\"total_citations\\\": 66, \\\"unique_cited_keys\\\": 44, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 38, \\\"online_not_found\\\": 3, \\\"online_mismatch\\\": 3}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"brown2024monkeys\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"authors\\\": \\\"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2407.21787\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"authors\\\": \\\"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint (ICML 2024 Workshop ICL)\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"authors\\\": \\\"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2110.14168\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"authors\\\": \\\"Culotta, Aron and McCallum, Andrew\\\", \\\"year\\\": \\\"2004\\\", \\\"venue\\\": \\\"HLT-NAACL 2004\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"authors\\\": \\\"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"W-NUT Workshop at EMNLP 2017\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"authors\\\": \\\"Eikema, Bryan and Aziz, Wilker\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"authors\\\": \\\"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"authors\\\": \\\"Fleiss, Joseph L.\\\", \\\"year\\\": \\\"1971\\\", \\\"venue\\\": \\\"Psychological Bulletin\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2511.12309\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"authors\\\": \\\"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"authors\\\": \\\"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2510.20460\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"authors\\\": \\\"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2207.05221\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"authors\\\": \\\"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"authors\\\": \\\"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"ACL 2026\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"authors\\\": \\\"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.04104\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"authors\\\": \\\"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"authors\\\": \\\"Malinin, Andrey and Gales, Mark\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"authors\\\": \\\"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"authors\\\": \\\"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"authors\\\": \\\"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"authors\\\": \\\"Manakul, Potsawee and Liusie, Adian and Gales, Mark\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"yao2026consistency\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\\\", \\\"authors\\\": \\\"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Genomics \\\\\\\\& Informatics\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"authors\\\": \\\"Oh, Jungsuk and Lee, Jay-Yoon\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.18395\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"authors\\\": \\\"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"authors\\\": \\\"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"authors\\\": \\\"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"authors\\\": \\\"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"authors\\\": \\\"Sang, Erik F. Tjong Kim and Meulder, Fien De\\\", \\\"year\\\": \\\"2003\\\", \\\"venue\\\": \\\"CoNLL 2003\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"authors\\\": \\\"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"authors\\\": \\\"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"authors\\\": \\\"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"authors\\\": \\\"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL 2025\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"authors\\\": \\\"Wang, Weiqin and Wang, Yile and Huang, Hui\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"authors\\\": \\\"Willard, Brandon T. and Louf, Rémi\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2307.09702\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"authors\\\": \\\"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"authors\\\": \\\"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"authors\\\": \\\"M\\\\\\\\\\\\\\\"uller, Mathias and Sennrich, Rico\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"authors\\\": \\\"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\", \\\"authors\\\": \\\"Venktesh, V and Rathee, Mandeep and Anand, Avishek\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.16665\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"authors\\\": \\\"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 41st International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"ratinov2009design\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Design Challenges and Misconceptions in Named Entity Recognition\\\", \\\"authors\\\": \\\"Ratinov, Lev and Roth, Dan\\\", \\\"year\\\": \\\"2009\\\", \\\"venue\\\": \\\"Proceedings of the Thirteenth Conference on Computational Natural Language Learn...\\\"}, {\\\"key\\\": \\\"bergkirkpatrick2012empirical\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"An Empirical Investigation of Statistical Significance in NLP\\\", \\\"authors\\\": \\\"Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan\\\", \\\"year\\\": \\\"2012\\\", \\\"venue\\\": \\\"Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Languag...\\\"}, {\\\"key\\\": \\\"tian2023calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models\\\", \\\"authors\\\": \\\"Tian, Katherine and Mitchell, Eric and Yao, Huaxiu and Manning, Christopher D. a...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"yao2026consistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"yao2026consistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 91, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tian2023calibration\\\", \\\"file\\\": \\\"sections/limitations.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 252, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 252, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ratinov2009design\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 387, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"bergkirkpatrick2012empirical\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 388, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 474, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 649, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 649, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 650, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 650, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 651, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"tian2023calibration\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 897, \\\"command\\\": \\\"citet\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"brown2024monkeys\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence estimation for information extraction\\\", \\\"matched_year\\\": \\\"2004\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"matched_year\\\": \\\"1971\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=feng vs api=austin\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.236, \\\"matched_title\\\": \\\"A new criterion for assessing discriminant validity in variance-based structural equation modeling\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.24 below threshold 0.82\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.246, \\\"matched_title\\\": \\\"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yao2026consistency\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=snell vs api=charlie\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2003\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=m\\\\\\\\\\\\\\\"uller vs api=müller\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"title\\\": \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.252, \\\"matched_title\\\": \\\"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ratinov2009design\\\", \\\"title\\\": \\\"Design Challenges and Misconceptions in Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Design challenges and misconceptions in named entity recognition\\\", \\\"matched_year\\\": \\\"2009\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"bergkirkpatrick2012empirical\\\", \\\"title\\\": \\\"An Empirical Investigation of Statistical Significance in NLP\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"An Empirical Investigation of Statistical Significance in NLP\\\", \\\"matched_year\\\": \\\"2012\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tian2023calibration\\\", \\\"title\\\": \\\"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.866, \\\"matched_title\\\": \\\"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 44, \"total_citations\": 66, \"unique_cited_keys\": 44, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 38, \"online_not_found\": 3, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"W-NUT Workshop at EMNLP 2017\"}, {\"key\": \"eikema2022sampling\", \"type\": \"inproceedings\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"authors\": \"Eikema, Bryan and Aziz, Wilker\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"freitag2022high\", \"type\": \"article\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"authors\": \"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\", \"year\": \"2022\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"fleiss1971agreement\", \"type\": \"article\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"authors\": \"Fleiss, Joseph L.\", \"year\": \"1971\", \"venue\": \"Psychological Bulletin\"}, {\"key\": \"feng2025optimal\", \"type\": \"article\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"authors\": \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.12309\"}, {\"key\": \"geng2024confidence\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"hobelsberger2025systematic\", \"type\": \"article\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"authors\": \"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.20460\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kang2025selfcertainty\", \"type\": \"inproceedings\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"authors\": \"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"kim2026reasc\", \"type\": \"inproceedings\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"authors\": \"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\", \"year\": \"2026\", \"venue\": \"ACL 2026\"}, {\"key\": \"li2025llms\", \"type\": \"article\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"authors\": \"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.04104\"}, {\"key\": \"kuhn2023semantic\", \"type\": \"inproceedings\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"authors\": \"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"malinin2021uncertainty\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"authors\": \"Malinin, Andrey and Gales, Mark\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"li2023codeie\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lightman2024verify\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"luan2018scierc\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"authors\": \"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"manakul2023selfcheckgpt\", \"type\": \"inproceedings\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"authors\": \"Manakul, Potsawee and Liusie, Adian and Gales, Mark\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"yao2026consistency\", \"type\": \"article\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\", \"authors\": \"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\", \"year\": \"2026\", \"venue\": \"Genomics \\\\& Informatics\"}, {\"key\": \"oh2025latentsc\", \"type\": \"article\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"authors\": \"Oh, Jungsuk and Lee, Jay-Yoon\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.18395\"}, {\"key\": \"sainz2024gollie\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"snell2025scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"authors\": \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"taubenfeld2025cisc\", \"type\": \"inproceedings\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"authors\": \"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"thirukovalluru2024atomic\", \"type\": \"inproceedings\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"authors\": \"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"tjongkimsang2003conll\", \"type\": \"inproceedings\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"authors\": \"Sang, Erik F. Tjong Kim and Meulder, Fien De\", \"year\": \"2003\", \"venue\": \"CoNLL 2003\"}, {\"key\": \"vashurin2025cocoa\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"authors\": \"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"wadhwa2023revisiting\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"wang2023selfconsistency\", \"type\": \"inproceedings\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"authors\": \"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"wang2025make\", \"type\": \"inproceedings\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"authors\": \"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2025\"}, {\"key\": \"wang2025rankedvoting\", \"type\": \"inproceedings\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"authors\": \"Wang, Weiqin and Wang, Yile and Huang, Hui\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"willard2023guided\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, Rémi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"xia2025survey\", \"type\": \"inproceedings\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"authors\": \"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"zheng2024llamafactory\", \"type\": \"inproceedings\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"authors\": \"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"zhou2024uniner\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"muller2021understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"authors\": \"M\\\\\\\"uller, Mathias and Sennrich, Rico\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"eikema2025structured\", \"type\": \"inproceedings\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"authors\": \"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"venktesh2025trust\", \"type\": \"article\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"authors\": \"Venktesh, V and Rathee, Mandeep and Anand, Avishek\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.16665\"}, {\"key\": \"jinnai2024mbr\", \"type\": \"inproceedings\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"authors\": \"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}, {\"key\": \"ratinov2009design\", \"type\": \"inproceedings\", \"title\": \"Design Challenges and Misconceptions in Named Entity Recognition\", \"authors\": \"Ratinov, Lev and Roth, Dan\", \"year\": \"2009\", \"venue\": \"Proceedings of the Thirteenth Conference on Computational Natural Language Learn...\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"type\": \"inproceedings\", \"title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"authors\": \"Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan\", \"year\": \"2012\", \"venue\": \"Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Languag...\"}, {\"key\": \"tian2023calibration\", \"type\": \"inproceedings\", \"title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models\", \"authors\": \"Tian, Katherine and Mitchell, Eric and Yao, Huaxiu and Manning, Christopher D. a...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}], \"tex_citations\": [{\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/introduction.tex\", \"line\": 3, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"yao2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/introduction.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/introduction.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/introduction.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"thirukovalluru2024atomic\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"manakul2023selfcheckgpt\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"kim2026reasc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wang2025rankedvoting\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"oh2025latentsc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"feng2025optimal\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"wang2025make\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"li2025llms\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"yao2026consistency\", \"file\": \"sections/related_work.tex\", \"line\": 10, \"command\": \"citet\"}, {\"key\": \"vashurin2025cocoa\", \"file\": \"sections/related_work.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"culotta2004confidence\", \"file\": \"sections/related_work.tex\", \"line\": 12, \"command\": \"citet\"}, {\"key\": \"zhou2024uniner\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"sainz2024gollie\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"li2023codeie\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"wadhwa2023revisiting\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"geng2024confidence\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"xia2025survey\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"hobelsberger2025systematic\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"kadavath2022language\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"malinin2021uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"citet\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/related_work.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"lightman2024verify\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/method.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fleiss1971agreement\", \"file\": \"sections/method.tex\", \"line\": 25, \"command\": \"citet\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/experiments.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/experiments.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"zheng2024llamafactory\", \"file\": \"sections/experiments.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/experiments.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/experiments.tex\", \"line\": 91, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/discussion.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/discussion.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"venktesh2025trust\", \"file\": \"sections/discussion.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"tian2023calibration\", \"file\": \"sections/limitations.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/appendix.tex\", \"line\": 252, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/appendix.tex\", \"line\": 252, \"command\": \"cite\"}, {\"key\": \"ratinov2009design\", \"file\": \"sections/appendix.tex\", \"line\": 387, \"command\": \"cite\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"file\": \"sections/appendix.tex\", \"line\": 388, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/appendix.tex\", \"line\": 474, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/appendix.tex\", \"line\": 649, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/appendix.tex\", \"line\": 649, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/appendix.tex\", \"line\": 650, \"command\": \"cite\"}, {\"key\": \"jinnai2024mbr\", \"file\": \"sections/appendix.tex\", \"line\": 650, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/appendix.tex\", \"line\": 651, \"command\": \"citet\"}, {\"key\": \"tian2023calibration\", \"file\": \"sections/appendix.tex\", \"line\": 897, \"command\": \"citet\"}], \"online_verification\": [{\"key\": \"brown2024monkeys\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024usc\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Self-Consistency for Large Language Model Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021verifiers\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culotta2004confidence\", \"title\": \"Confidence Estimation for Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence estimation for information extraction\", \"matched_year\": \"2004\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"derczynski2017wnut\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eikema2022sampling\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"freitag2022high\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fleiss1971agreement\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring nominal scale agreement among many raters.\", \"matched_year\": \"1971\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feng2025optimal\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=feng vs api=austin\"], \"note\": \"\"}, {\"key\": \"geng2024confidence\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hobelsberger2025systematic\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.236, \"matched_title\": \"A new criterion for assessing discriminant validity in variance-based structural equation modeling\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.24 below threshold 0.82\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2025selfcertainty\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2026reasc\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025llms\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuhn2023semantic\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"malinin2021uncertainty\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023codeie\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lightman2024verify\", \"title\": \"Let's Verify Step by Step\", \"status\": \"not_found\", \"confidence\": 0.246, \"matched_title\": \"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"luan2018scierc\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"manakul2023selfcheckgpt\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yao2026consistency\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oh2025latentsc\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sainz2024gollie\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"snell2025scaling\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=snell vs api=charlie\"], \"note\": \"\"}, {\"key\": \"taubenfeld2025cisc\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence Improves Self-Consistency in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thirukovalluru2024atomic\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tjongkimsang2003conll\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"matched_year\": \"2003\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vashurin2025cocoa\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa2023revisiting\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023selfconsistency\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025make\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025rankedvoting\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023guided\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2025survey\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zheng2024llamafactory\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024uniner\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"muller2021understanding\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"matched_year\": \"2021\", \"mismatch_fields\": [\"first_author: bib=m\\\\\\\"uller vs api=müller\"], \"note\": \"\"}, {\"key\": \"eikema2025structured\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"venktesh2025trust\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"status\": \"not_found\", \"confidence\": 0.252, \"matched_title\": \"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"jinnai2024mbr\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ratinov2009design\", \"title\": \"Design Challenges and Misconceptions in Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Design challenges and misconceptions in named entity recognition\", \"matched_year\": \"2009\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bergkirkpatrick2012empirical\", \"title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"An Empirical Investigation of Statistical Significance in NLP\", \"matched_year\": \"2012\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tian2023calibration\", \"title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models\", \"status\": \"verified\", \"confidence\": 0.866, \"matched_title\": \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "2850ffcd-8f99-4f03-bc60-d1d8015c0cc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 呈现**  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **页数**: 长文 8 页 +…",
  "leafUuid": "73a67321-b10a-44e3-866d-fb4323f3bd35",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 for structured IE confidence estimation paper",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Assistant

_source line 80 · 2026-05-16T04:20:50.412Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the paper. Let me also search for a few more specific potentially missing references and then compile my review.

Key observations:

1. **Reference verification**: 38/44 verified, 3 not found (hobelsberger2025, lightman2024, venktesh2025 - these are likely valid arXiv preprints that OpenAlex doesn't index), 3 mismatches (feng2025 author name format, snell2025 author name, muller2021 encoding). No orphan or missing bib entries.


2. **Novelty concerns**: The correlation-selection gap is conceptually interesting but relies on a definitional limitation rather than an empirical finding, and while LP compression serves as the main empirical contribution, it feels somewhat incremental compared to Yao et al. (2026) — though the paper does add value through structural matching, selection analysis, and difficulty gradients. I should also check whether conformal structured prediction and related work on self-assessments for performance prediction are adequately addressed.

3. **Writing and presentation**: The paper is generally well-written and thorough, though "preliminary" gets used quite frequently. The format looks correct with the ACL review package, anonymous submission, ethics statement, and limitations section all in place. I need to verify anonymity by checking for any exposed GitHub links or institution names, and I should estimate the page count across all the substantial sections — abstract through ethics statement — though I can't actually compile the LaTeX to confirm.

4. **Reference gaps**: I'm looking for any additional missing citations, particularly around ensemble methods for information extraction and uncertainty quantification literature specific to NER tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73a67321-b10a-44e3-866d-fb4323f3bd35",
  "isSidechain": false,
  "requestId": "req_011Cb5c83NAEpNmF5K9pHPYC",
  "type": "assistant",
  "uuid": "1e23e707-823a-45ce-a95b-a8f7d08f5fc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKcQTPartwbwuRt9zajxcb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23910,
      "cache_read_input_tokens": 71054,
      "output_tokens": 686,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23910,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 686,
          "cache_read_input_tokens": 71054,
          "cache_creation_input_tokens": 23910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23910
          },
          "type": "message"
        }
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

_source line 81 · 2026-05-16T04:20:50.414Z_

搜索更多可能遗漏的相关工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e23e707-823a-45ce-a95b-a8f7d08f5fc3",
  "isSidechain": false,
  "requestId": "req_011Cb5c83NAEpNmF5K9pHPYC",
  "type": "assistant",
  "uuid": "513958c4-25cb-4b86-8775-176a82e79a30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKcQTPartwbwuRt9zajxcb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23910,
      "cache_read_input_tokens": 71054,
      "output_tokens": 686,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23910,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 686,
          "cache_read_input_tokens": 71054,
          "cache_creation_input_tokens": 23910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23910
          },
          "type": "message"
        }
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

_source line 82 · 2026-05-16T04:20:50.423Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NrGpiVgETFVNgU6yhAdrQp`</summary>

```json
{
  "query": "\"Thought Pruning\" self-consistency structured prediction efficient scaling EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "513958c4-25cb-4b86-8775-176a82e79a30",
  "isSidechain": false,
  "requestId": "req_011Cb5c83NAEpNmF5K9pHPYC",
  "type": "assistant",
  "uuid": "2664872a-2e84-4a59-bc55-9fa6e94c615e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKcQTPartwbwuRt9zajxcb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23910,
      "cache_read_input_tokens": 71054,
      "output_tokens": 686,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23910,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 686,
          "cache_read_input_tokens": 71054,
          "cache_creation_input_tokens": 23910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23910
          },
          "type": "message"
        }
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

_source line 83 · 2026-05-16T04:20:50.429Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TmE8Wg9FmvcqYRPzMFvbcM`</summary>

```json
{
  "query": "\"beyond confidence\" \"self-assessments\" LLM performance prediction 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2664872a-2e84-4a59-bc55-9fa6e94c615e",
  "isSidechain": false,
  "requestId": "req_011Cb5c83NAEpNmF5K9pHPYC",
  "type": "assistant",
  "uuid": "58c02adb-2dff-4b14-ae5a-8f3dae62a085",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKcQTPartwbwuRt9zajxcb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23910,
      "cache_read_input_tokens": 71054,
      "output_tokens": 686,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23910,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 686,
          "cache_read_input_tokens": 71054,
          "cache_creation_input_tokens": 23910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23910
          },
          "type": "message"
        }
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

_source line 84 · 2026-05-16T04:20:50.432Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q1DrZcKi8U4finAeeD5rqS`</summary>

```json
{
  "query": "conformal prediction structured information extraction NER set-valued 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58c02adb-2dff-4b14-ae5a-8f3dae62a085",
  "isSidechain": false,
  "requestId": "req_011Cb5c83NAEpNmF5K9pHPYC",
  "type": "assistant",
  "uuid": "ae68432f-2d3d-4266-84cd-9e7afff1c3a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKcQTPartwbwuRt9zajxcb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23910,
      "cache_read_input_tokens": 71054,
      "output_tokens": 686,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23910,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 686,
          "cache_read_input_tokens": 71054,
          "cache_creation_input_tokens": 23910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23910
          },
          "type": "message"
        }
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

_source line 85 · 2026-05-16T04:20:57.112Z_

<details><summary>↩ Tool result · `toolu_01TmE8Wg9FmvcqYRPzMFvbcM`</summary>

```text
Web search results for query: ""beyond confidence" "self-assessments" LLM performance prediction 2026 arxiv"

Links: [{"title":"[2605.07806] Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs","url":"https://arxiv.org/abs/2605.07806"},{"title":"LLM Performance Predictors: Learning When to Escalate in Hybrid Human-AI Moderation Systems","url":"https://arxiv.org/html/2601.07006v1"},{"title":"Learning to Route LLMs with Confidence Tokens","url":"https://arxiv.org/html/2410.13284v3"},{"title":"Confidence Estimation in Automatic Short Answer Grading with LLMs","url":"https://arxiv.org/html/2605.00200v1"},{"title":"LLM Performance Predictors","url":"https://www.emergentmind.com/topics/llm-performance-predictors-lpps"},{"title":"Cycles of Thought: Measuring LLM Confidence through Stable Explanations","url":"https://arxiv.org/html/2406.03441v1"},{"title":"Are LLM Decisions Faithful to Verbal Confidence?","url":"https://arxiv.org/html/2601.07767v1"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/html/2502.06233v1"},{"title":"Robust LLM Performance Certification via Constrained Maximum Likelihood Estimation","url":"https://arxiv.org/html/2604.03257"},{"title":"A Survey on Evaluation of LLM-based Agents","url":"https://arxiv.org/html/2503.16416v2"}]

I found the paper you were searching for! Here's what I found:

The primary result from your search is the arXiv paper 2605.07806: "Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs". 

This recent paper investigates alternatives to confidence for predicting LLM performance. The researchers elicit six appraisal-based dimensions of self-assessment, alongside confidence, and evaluate their utility for predicting model failure across 12 LLMs and 38 tasks spanning eight domains.

Key findings include:

- Competence-related appraisal dimensions, particularly effort and ability, consistently match or outperform confidence across most settings, with effort additionally yielding less overoptimistic estimates that remain stable across model sizes.

- The most informative dimension varies systematically with task characteristics: effort is most predictive for reasoning-intensive tasks, while ability and confidence dominate on retrieval-oriented tasks.

- The findings indicate that structured multidimensional self-assessment is a promising approach to improving the reliability and safety of language model deployment across diverse real-world settings.

The paper was submitted on May 8, 2026, making it very recent research in the field of LLM performance prediction and uncertainty quantification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58c02adb-2dff-4b14-ae5a-8f3dae62a085",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "ec81e591-1229-4b8f-8468-79749486b92c",
  "toolUseResult": {
    "query": "\"beyond confidence\" \"self-assessments\" LLM performance prediction 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TmvwzwCtb9GrG9Amq4iVNN",
        "content": [
          {
            "title": "[2605.07806] Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs",
            "url": "https://arxiv.org/abs/2605.07806"
          },
          {
            "title": "LLM Performance Predictors: Learning When to Escalate in Hybrid Human-AI Moderation Systems",
            "url": "https://arxiv.org/html/2601.07006v1"
          },
          {
            "title": "Learning to Route LLMs with Confidence Tokens",
            "url": "https://arxiv.org/html/2410.13284v3"
          },
          {
            "title": "Confidence Estimation in Automatic Short Answer Grading with LLMs",
            "url": "https://arxiv.org/html/2605.00200v1"
          },
          {
            "title": "LLM Performance Predictors",
            "url": "https://www.emergentmind.com/topics/llm-performance-predictors-lpps"
          },
          {
            "title": "Cycles of Thought: Measuring LLM Confidence through Stable Explanations",
            "url": "https://arxiv.org/html/2406.03441v1"
          },
          {
            "title": "Are LLM Decisions Faithful to Verbal Confidence?",
            "url": "https://arxiv.org/html/2601.07767v1"
          },
          {
            "title": "Confidence Improves Self-Consistency in LLMs",
            "url": "https://arxiv.org/html/2502.06233v1"
          },
          {
            "title": "Robust LLM Performance Certification via Constrained Maximum Likelihood Estimation",
            "url": "https://arxiv.org/html/2604.03257"
          },
          {
            "title": "A Survey on Evaluation of LLM-based Agents",
            "url": "https://arxiv.org/html/2503.16416v2"
          }
        ]
      },
      "I found the paper you were searching for! Here's what I found:\n\nThe primary result from your search is the arXiv paper 2605.07806: \"Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs\". \n\nThis recent paper investigates alternatives to confidence for predicting LLM performance. The researchers elicit six appraisal-based dimensions of self-assessment, alongside confidence, and evaluate their utility for predicting model failure across 12 LLMs and 38 tasks spanning eight domains.\n\nKey findings include:\n\n- Competence-related appraisal dimensions, particularly effort and ability, consistently match or outperform confidence across most settings, with effort additionally yielding less overoptimistic estimates that remain stable across model sizes.\n\n- The most informative dimension varies systematically with task characteristics: effort is most predictive for reasoning-intensive tasks, while ability and confidence dominate on retrieval-oriented tasks.\n\n- The findings indicate that structured multidimensional self-assessment is a promising approach to improving the reliability and safety of language model deployment across diverse real-world settings.\n\nThe paper was submitted on May 8, 2026, making it very recent research in the field of LLM performance prediction and uncertainty quantification."
    ],
    "durationSeconds": 6.680178555000006
  },
  "sourceToolAssistantUUID": "58c02adb-2dff-4b14-ae5a-8f3dae62a085",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-16T04:20:57.301Z_

<details><summary>↩ Tool result · `toolu_01NrGpiVgETFVNgU6yhAdrQp`</summary>

```text
Web search results for query: ""Thought Pruning" self-consistency structured prediction efficient scaling EMNLP 2025"

Links: [{"title":"Thought Pruning for Efficient Scaling with Self-Consistency","url":"https://aclanthology.org/2025.emnlp-main.1750.pdf"},{"title":"GitHub - hyscale-lab/slimsc: Official repository for the EMNLP 2025 paper \"Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency\".","url":"https://github.com/hyscale-lab/slimsc"},{"title":"Confidence-Aware Reasoning: Optimizing Self-Guided ...","url":"https://aclanthology.org/2025.emnlp-industry.146.pdf"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"Revisiting Pruning vs Quantization for Small Language ...","url":"https://aclanthology.org/2025.findings-emnlp.645.pdf"},{"title":"An Empirical Study of LLM Reasoning Ability Under Strict ...","url":"https://aclanthology.org/2025.emnlp-main.389.pdf"},{"title":"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps","url":"https://aclanthology.org/2025.emnlp-main.504.pdf"},{"title":"EMNLP 2025 Highlights and Research Directions - Megagon","url":"https://megagon.ai/emnlp2025-highlights/"},{"title":"EMNLP.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/EMNLP.2025"},{"title":"Revisiting Pruning vs Quantization for Small Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.645/"}]

I found information about your search query. The results are primarily about **Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency**, which appears to be an EMNLP 2025 paper.

## Key Findings:

The work is an EMNLP 2025 accepted paper titled "Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency".

**Problem Being Addressed:**
Standard Self-Consistency improves LLM reasoning but is computationally expensive and slow due to generating many full reasoning chains.

**The Proposed Solution:**
Slim-SC is a dynamic thought-pruning method that identifies and removes redundant chains step-by-step during generation based on their semantic similarity. The analysis reveals that correct and incorrect chains form distinct semantic clusters, with incorrect chains often being highly redundant.

**Results:**
The method achieves significant efficiency gains, reducing end-to-end latency by up to 45% (on GPQA) and token usage by up to 32% (on AIME-2024), while maintaining or even slightly improving accuracy (+0.5pp on GPQA) by retaining a more effective set of diverse candidate chains for the final vote.

The paper was presented at EMNLP 2025, which took place November 4-9, 2025. The authors are Colin Hong, Xu Guo, Anand Chaanan Singh, Esha Choukse, and Dmitrii Ustiugov, with an official GitHub repository available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2664872a-2e84-4a59-bc55-9fa6e94c615e",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "032fa1cc-0467-441f-b32f-e5f921620747",
  "toolUseResult": {
    "query": "\"Thought Pruning\" self-consistency structured prediction efficient scaling EMNLP 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KL35RFtf7YR6D8eLJjrg7u",
        "content": [
          {
            "title": "Thought Pruning for Efficient Scaling with Self-Consistency",
            "url": "https://aclanthology.org/2025.emnlp-main.1750.pdf"
          },
          {
            "title": "GitHub - hyscale-lab/slimsc: Official repository for the EMNLP 2025 paper \"Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency\".",
            "url": "https://github.com/hyscale-lab/slimsc"
          },
          {
            "title": "Confidence-Aware Reasoning: Optimizing Self-Guided ...",
            "url": "https://aclanthology.org/2025.emnlp-industry.146.pdf"
          },
          {
            "title": "Accepted Findings Papers - EMNLP 2025",
            "url": "https://2025.emnlp.org/program/find_papers/"
          },
          {
            "title": "Revisiting Pruning vs Quantization for Small Language ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.645.pdf"
          },
          {
            "title": "An Empirical Study of LLM Reasoning Ability Under Strict ...",
            "url": "https://aclanthology.org/2025.emnlp-main.389.pdf"
          },
          {
            "title": "Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps",
            "url": "https://aclanthology.org/2025.emnlp-main.504.pdf"
          },
          {
            "title": "EMNLP 2025 Highlights and Research Directions - Megagon",
            "url": "https://megagon.ai/emnlp2025-highlights/"
          },
          {
            "title": "EMNLP.2025 | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/venue/EMNLP.2025"
          },
          {
            "title": "Revisiting Pruning vs Quantization for Small Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-emnlp.645/"
          }
        ]
      },
      "I found information about your search query. The results are primarily about **Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency**, which appears to be an EMNLP 2025 paper.\n\n## Key Findings:\n\nThe work is an EMNLP 2025 accepted paper titled \"Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency\".\n\n**Problem Being Addressed:**\nStandard Self-Consistency improves LLM reasoning but is computationally expensive and slow due to generating many full reasoning chains.\n\n**The Proposed Solution:**\nSlim-SC is a dynamic thought-pruning method that identifies and removes redundant chains step-by-step during generation based on their semantic similarity. The analysis reveals that correct and incorrect chains form distinct semantic clusters, with incorrect chains often being highly redundant.\n\n**Results:**\nThe method achieves significant efficiency gains, reducing end-to-end latency by up to 45% (on GPQA) and token usage by up to 32% (on AIME-2024), while maintaining or even slightly improving accuracy (+0.5pp on GPQA) by retaining a more effective set of diverse candidate chains for the final vote.\n\nThe paper was presented at EMNLP 2025, which took place November 4-9, 2025. The authors are Colin Hong, Xu Guo, Anand Chaanan Singh, Esha Choukse, and Dmitrii Ustiugov, with an official GitHub repository available."
    ],
    "durationSeconds": 6.874044336000006
  },
  "sourceToolAssistantUUID": "2664872a-2e84-4a59-bc55-9fa6e94c615e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-16T04:20:59.086Z_

<details><summary>↩ Tool result · `toolu_01Q1DrZcKi8U4finAeeD5rqS`</summary>

```text
Web search results for query: "conformal prediction structured information extraction NER set-valued 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025 CONFORMAL STRUCTURED PREDICTION","url":"https://par.nsf.gov/servlets/purl/10610745"},{"title":"Conformal Prediction: A Data Perspective | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3736575"},{"title":"Conformal Prediction: A Data Perspective","url":"https://arxiv.org/pdf/2410.06494"},{"title":"Ontology-conformal recognition of materials entities using language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-03619-y"},{"title":"ICLR Conformal Structured Prediction","url":"https://iclr.cc/virtual/2025/32866"},{"title":"[2410.06296] Conformal Structured Prediction","url":"https://arxiv.org/abs/2410.06296"},{"title":"Conformal Structured Prediction | OpenReview","url":"https://openreview.net/forum?id=mKfmLQXP6J"},{"title":"Conformal Prediction for Natural Language Processing: A Survey | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/Conformal-Prediction-for-Natural-Language"},{"title":"Conformal Prediction Sets Improve Human Decision Making","url":"https://arxiv.org/html/2401.13744v3"},{"title":"ICML Poster Volume Optimality in Conformal Prediction with Structured Prediction Sets","url":"https://icml.cc/virtual/2025/poster/44066"}]

The search results reveal several relevant recent works on conformal prediction applied to structured tasks:

## Key Findings

**Conformal Structured Prediction Framework**: A general framework for conformal prediction in the structured prediction setting modifies existing conformal prediction algorithms to output structured prediction sets that implicitly represent sets of labels. While existing conformal prediction algorithms have largely targeted classification and regression settings, for complex structured outputs such as text generation by large language models (LLMs), prediction sets might include a large number of labels and therefore be hard for users to interpret.

**Application to NLP Tasks**: For POS tagging and text infilling, research proposes CP-enhanced BERT and BiLSTM algorithms to ensure their statistical reliability. Additionally, a modified CP algorithm produces multi-label prediction sets with a strict limit on false positives by using a greedy algorithm based on non-conformity scores to optimize true positive rates while controlling false positives.

**Named Entity Recognition (NER)**: Recent work has connected conformal methods with ontology-constrained NER. Named entity recognition (NER) is a fundamental subtask when transforming unstructured information contained in text into structured knowledge. One study used the Few-NERD dataset with each word annotated as a named entity class, selecting a single entity from every sentence as the classification target.

**Set-Valued Predictions**: Conformal prediction replaces a model with a conformal predictor that outputs a set of labels capturing the uncertainty of the model, and provides a coverage guarantee—the prediction set is guaranteed to contain the ground truth label with high probability.

These developments suggest an active research area combining conformal prediction with structured information extraction tasks in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae68432f-2d3d-4266-84cd-9e7afff1c3a6",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "110a3bf9-51f9-4059-9f14-c8224de03a56",
  "toolUseResult": {
    "query": "conformal prediction structured information extraction NER set-valued 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RJnZNiUnW5pjsWyLy5LAg9",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2025 CONFORMAL STRUCTURED PREDICTION",
            "url": "https://par.nsf.gov/servlets/purl/10610745"
          },
          {
            "title": "Conformal Prediction: A Data Perspective | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3736575"
          },
          {
            "title": "Conformal Prediction: A Data Perspective",
            "url": "https://arxiv.org/pdf/2410.06494"
          },
          {
            "title": "Ontology-conformal recognition of materials entities using language models | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-025-03619-y"
          },
          {
            "title": "ICLR Conformal Structured Prediction",
            "url": "https://iclr.cc/virtual/2025/32866"
          },
          {
            "title": "[2410.06296] Conformal Structured Prediction",
            "url": "https://arxiv.org/abs/2410.06296"
          },
          {
            "title": "Conformal Structured Prediction | OpenReview",
            "url": "https://openreview.net/forum?id=mKfmLQXP6J"
          },
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/Conformal-Prediction-for-Natural-Language"
          },
          {
            "title": "Conformal Prediction Sets Improve Human Decision Making",
            "url": "https://arxiv.org/html/2401.13744v3"
          },
          {
            "title": "ICML Poster Volume Optimality in Conformal Prediction with Structured Prediction Sets",
            "url": "https://icml.cc/virtual/2025/poster/44066"
          }
        ]
      },
      "The search results reveal several relevant recent works on conformal prediction applied to structured tasks:\n\n## Key Findings\n\n**Conformal Structured Prediction Framework**: A general framework for conformal prediction in the structured prediction setting modifies existing conformal prediction algorithms to output structured prediction sets that implicitly represent sets of labels. While existing conformal prediction algorithms have largely targeted classification and regression settings, for complex structured outputs such as text generation by large language models (LLMs), prediction sets might include a large number of labels and therefore be hard for users to interpret.\n\n**Application to NLP Tasks**: For POS tagging and text infilling, research proposes CP-enhanced BERT and BiLSTM algorithms to ensure their statistical reliability. Additionally, a modified CP algorithm produces multi-label prediction sets with a strict limit on false positives by using a greedy algorithm based on non-conformity scores to optimize true positive rates while controlling false positives.\n\n**Named Entity Recognition (NER)**: Recent work has connected conformal methods with ontology-constrained NER. Named entity recognition (NER) is a fundamental subtask when transforming unstructured information contained in text into structured knowledge. One study used the Few-NERD dataset with each word annotated as a named entity class, selecting a single entity from every sentence as the classification target.\n\n**Set-Valued Predictions**: Conformal prediction replaces a model with a conformal predictor that outputs a set of labels capturing the uncertainty of the model, and provides a coverage guarantee—the prediction set is guaranteed to contain the ground truth label with high probability.\n\nThese developments suggest an active research area combining conformal prediction with structured information extraction tasks in 2025."
    ],
    "durationSeconds": 8.651382211000003
  },
  "sourceToolAssistantUUID": "ae68432f-2d3d-4266-84cd-9e7afff1c3a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 88 · 2026-05-16T04:20:59.091Z_

```json
{
  "parentUuid": "110a3bf9-51f9-4059-9f14-c8224de03a56",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a92fa618-b5e9-4c89-a43d-c35f1a472113",
  "timestamp": "2026-05-16T04:20:59.091Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 89_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 呈现**  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **页数**: 长文 8 页 +…",
  "leafUuid": "a92fa618-b5e9-4c89-a43d-c35f1a472113",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Runtime record

_source line 90_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 for structured IE confidence estimation paper",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Assistant

_source line 91 · 2026-05-16T04:21:01.930Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also check if there's a compiled PDF to verify page count and visual quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a92fa618-b5e9-4c89-a43d-c35f1a472113",
  "isSidechain": false,
  "requestId": "req_011Cb5cA4yhcbtiFccRJ3BTu",
  "type": "assistant",
  "uuid": "790e7ddf-3288-431e-8594-e685a45cd387",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012j3GNJg65hF3SzM12jdjGz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3308,
      "cache_read_input_tokens": 94964,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 94964,
          "cache_creation_input_tokens": 3308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3308
          },
          "type": "message"
        }
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

_source line 92 · 2026-05-16T04:21:02.386Z_

检查是否有编译好的 PDF 以验证页数和视觉质量。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "790e7ddf-3288-431e-8594-e685a45cd387",
  "isSidechain": false,
  "requestId": "req_011Cb5cA4yhcbtiFccRJ3BTu",
  "type": "assistant",
  "uuid": "691e6037-933f-4f17-b2ab-840aed4be24f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012j3GNJg65hF3SzM12jdjGz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3308,
      "cache_read_input_tokens": 94964,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 94964,
          "cache_creation_input_tokens": 3308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3308
          },
          "type": "message"
        }
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

_source line 93 · 2026-05-16T04:21:04.177Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018pVpuCkjqaRFJTBD2FGD1Y`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "691e6037-933f-4f17-b2ab-840aed4be24f",
  "isSidechain": false,
  "requestId": "req_011Cb5cA4yhcbtiFccRJ3BTu",
  "type": "assistant",
  "uuid": "604451a3-d4f7-42ca-94f1-f667af6da6ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012j3GNJg65hF3SzM12jdjGz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3308,
      "cache_read_input_tokens": 94964,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 94964,
          "cache_creation_input_tokens": 3308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3308
          },
          "type": "message"
        }
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

_source line 94 · 2026-05-16T04:21:04.216Z_

<details><summary>↩ Tool result · `toolu_018pVpuCkjqaRFJTBD2FGD1Y`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_length_logprob_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_lp_range_cdf.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "604451a3-d4f7-42ca-94f1-f667af6da6ec",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "49f17cd2-43c8-4772-a4b3-5b38db576b90",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_length_logprob_scatter.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_lp_range_cdf.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf"
    ],
    "durationMs": 26,
    "numFiles": 8,
    "truncated": false
  },
  "sourceToolAssistantUUID": "604451a3-d4f7-42ca-94f1-f667af6da6ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-16T04:21:07.315Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01FWdz9n817425gE5cgzmGBz`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-8",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49f17cd2-43c8-4772-a4b3-5b38db576b90",
  "isSidechain": false,
  "requestId": "req_011Cb5cASwnzQx3SkCeAJj42",
  "type": "assistant",
  "uuid": "70273720-83c3-4e97-8c6d-89bdb61ff694",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QyYFi7XqJ7DsTdfMJ16LQz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 532,
      "cache_read_input_tokens": 98272,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 532,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 98272,
          "cache_creation_input_tokens": 532,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 532
          },
          "type": "message"
        }
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

_source line 96 · 2026-05-16T04:21:09.705Z_

<details><summary>↩ Tool result · `toolu_01FWdz9n817425gE5cgzmGBz`</summary>

```text
Error: result (5,375,711 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/e427ec35-e53e-4958-bb7f-c7a35811281b/tool-results/mcp-agent-ml-research-pdf_to_images-1778905269695.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/e427ec35-e53e-4958-bb7f-c7a35811281b/tool-results/mcp-agent-ml-research-pdf_to_images-1778905269695.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/e427ec35-e53e-4958-bb7f-c7a35811281b/tool-results/mcp-agent-ml-research-pdf_to_images-1778905269695.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70273720-83c3-4e97-8c6d-89bdb61ff694",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "2daec4a4-e005-4f29-8d87-db1bbcd2c0a6",
  "toolUseResult": "Error: result (5,375,711 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/e427ec35-e53e-4958-bb7f-c7a35811281b/tool-results/mcp-agent-ml-research-pdf_to_images-1778905269695.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/e427ec35-e53e-4958-bb7f-c7a35811281b/tool-results/mcp-agent-ml-research-pdf_to_images-1778905269695.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/e427ec35-e53e-4958-bb7f-c7a35811281b/tool-results/mcp-agent-ml-research-pdf_to_images-1778905269695.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 96,
    "serialized_bytes": 5375748,
    "serialized_sha256": "319d15f3daea9630911403367c67d94dbdfd45a13a6eb5db0ad20a0cfd9e2bce",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "70273720-83c3-4e97-8c6d-89bdb61ff694",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 97_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 呈现**  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **页数**: 长文 8 页 +…",
  "leafUuid": "2daec4a4-e005-4f29-8d87-db1bbcd2c0a6",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Runtime record

_source line 98_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 for structured IE confidence estimation paper",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Assistant

_source line 99 · 2026-05-16T04:21:12.216Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF images are too large to load directly. Let me try page by page with lower dpi or just check specific pages for page count.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2daec4a4-e005-4f29-8d87-db1bbcd2c0a6",
  "isSidechain": false,
  "requestId": "req_011Cb5cArep57Y863jTWFbef",
  "type": "assistant",
  "uuid": "1c378451-d386-446d-a613-b354e66d3b19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HH4DQvHeidAj41WQ2UfoqH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 98804,
      "output_tokens": 378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 706,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 378,
          "cache_read_input_tokens": 98804,
          "cache_creation_input_tokens": 706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 706
          },
          "type": "message"
        }
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

_source line 100 · 2026-05-16T04:21:13.186Z_

PDF 太大，用子 agent 检查页数和视觉排版。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c378451-d386-446d-a613-b354e66d3b19",
  "isSidechain": false,
  "requestId": "req_011Cb5cArep57Y863jTWFbef",
  "type": "assistant",
  "uuid": "c5db91dd-845e-4d76-8117-3fbe37d5673e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HH4DQvHeidAj41WQ2UfoqH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 98804,
      "output_tokens": 378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 706,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 378,
          "cache_read_input_tokens": 98804,
          "cache_creation_input_tokens": 706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 706
          },
          "type": "message"
        }
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

_source line 101 · 2026-05-16T04:21:17.921Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01RMtVuTva9MDJkQocC2Tjyh`</summary>

```json
{
  "description": "Check PDF page count and layout",
  "prompt": "I need you to check the compiled PDF of a paper at /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf\n\n1. First, use pdf_to_images to render pages 1-2 only at dpi=150, and visually inspect:\n   - Does the paper use ACL review format (with line numbers)?\n   - Is anonymity maintained (author field = \"Anonymous\")?\n   - Is the layout clean?\n   \n2. Then render pages 7-8 at dpi=150 to check:\n   - Where does the main text end (before References)?\n   - Estimate total main body page count\n\n3. Then render the last 2-3 pages to see:\n   - Where appendix begins\n   - Total page count\n\nReport back: total page count, whether main body fits 8 pages, anonymity status, and any visual issues.",
  "subagent_type": "Explore"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5db91dd-845e-4d76-8117-3fbe37d5673e",
  "isSidechain": false,
  "requestId": "req_011Cb5cArep57Y863jTWFbef",
  "type": "assistant",
  "uuid": "2722e005-8a95-4d33-80a3-a95bbfb0f74f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HH4DQvHeidAj41WQ2UfoqH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 98804,
      "output_tokens": 378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 706,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 378,
          "cache_read_input_tokens": 98804,
          "cache_creation_input_tokens": 706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 706
          },
          "type": "message"
        }
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

_source line 102 · 2026-05-16T04:22:00.875Z_

<details><summary>↩ Tool result · `toolu_01RMtVuTva9MDJkQocC2Tjyh`</summary>

```text
Perfect! I've now inspected all the key pages. Let me provide you with a comprehensive report:

## PDF Inspection Report

**Total Page Count: 22 pages**

### 1. Format and Anonymity Check (Pages 1-2)

**ACL Review Format with Line Numbers:** YES
- The paper displays clear line numbers in the left margin (visible as 001, 002, 003, etc.)
- This is the standard ACL review format

**Anonymity Status:** MAINTAINED
- Author field reads "Anonymous ACL submission"
- No author names or institutional affiliations visible on the first page
- Properly anonymized for peer review

**Layout Quality:** CLEAN
- Well-formatted title: "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction"
- Professional abstract section with clear structure
- Two-column layout on page 2 with figures (Quality Estimation and Sample Selection diagrams)
- Good visual organization

### 2. Main Body Length Check (Pages 7-8)

**Where Main Text Ends:** Page 8 transitions to the References section
- Page 7 contains the last substantive content sections including results and analysis (V. Verbatim, VI. Robustness Analysis, etc.)
- Page 8 begins with References (two columns of citations)

**Estimated Main Body Page Count: Approximately 6-7 pages**
- Introduction and early content: pages 1-2 (with abstract)
- Main methodology and results: pages 3-7
- References begin on page 8

### 3. Appendix and Total Structure (Pages 20-22)

**Where Appendix Begins:** Around page 9-10 (Appendix A starts after References conclude)
- Pages 20-21 contain appendix material with detailed tables and analysis (V. X-Scaling Detailed Analysis, Cross-Dataset OOD Analysis, Verbatim Consistency sections with tables)
- Page 22 shows mostly blank space with only text "at larger scales." and page number "22" at bottom

**Total Page Breakdown:**
- Main body (intro + methodology + results): 6-7 pages
- References: 1-2 pages  
- Appendix: 12-14 pages
- Final page 22: nearly blank (end matter)

### Summary

- **Total pages: 22**
- **Main body fits within 8 pages: YES** (actually ~6-7 pages, leaving room in the 8-page limit)
- **Anonymity: PROPERLY MAINTAINED** (Anonymous ACL submission)
- **Visual Issues: NONE DETECTED** - Layout is clean, professional, properly formatted with ACL line numbers

The paper is well-prepared for review with proper anonymization and follows ACL submission guidelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2722e005-8a95-4d33-80a3-a95bbfb0f74f",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "4cc82def-b8c3-49d3-8c0c-4b4308e6d779",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to check the compiled PDF of a paper at /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf\n\n1. First, use pdf_to_images to render pages 1-2 only at dpi=150, and visually inspect:\n   - Does the paper use ACL review format (with line numbers)?\n   - Is anonymity maintained (author field = \"Anonymous\")?\n   - Is the layout clean?\n   \n2. Then render pages 7-8 at dpi=150 to check:\n   - Where does the main text end (before References)?\n   - Estimate total main body page count\n\n3. Then render the last 2-3 pages to see:\n   - Where appendix begins\n   - Total page count\n\nReport back: total page count, whether main body fits 8 pages, anonymity status, and any visual issues.",
    "agentId": "a54883851bb30c005",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I've now inspected all the key pages. Let me provide you with a comprehensive report:\n\n## PDF Inspection Report\n\n**Total Page Count: 22 pages**\n\n### 1. Format and Anonymity Check (Pages 1-2)\n\n**ACL Review Format with Line Numbers:** YES\n- The paper displays clear line numbers in the left margin (visible as 001, 002, 003, etc.)\n- This is the standard ACL review format\n\n**Anonymity Status:** MAINTAINED\n- Author field reads \"Anonymous ACL submission\"\n- No author names or institutional affiliations visible on the first page\n- Properly anonymized for peer review\n\n**Layout Quality:** CLEAN\n- Well-formatted title: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction\"\n- Professional abstract section with clear structure\n- Two-column layout on page 2 with figures (Quality Estimation and Sample Selection diagrams)\n- Good visual organization\n\n### 2. Main Body Length Check (Pages 7-8)\n\n**Where Main Text Ends:** Page 8 transitions to the References section\n- Page 7 contains the last substantive content sections including results and analysis (V. Verbatim, VI. Robustness Analysis, etc.)\n- Page 8 begins with References (two columns of citations)\n\n**Estimated Main Body Page Count: Approximately 6-7 pages**\n- Introduction and early content: pages 1-2 (with abstract)\n- Main methodology and results: pages 3-7\n- References begin on page 8\n\n### 3. Appendix and Total Structure (Pages 20-22)\n\n**Where Appendix Begins:** Around page 9-10 (Appendix A starts after References conclude)\n- Pages 20-21 contain appendix material with detailed tables and analysis (V. X-Scaling Detailed Analysis, Cross-Dataset OOD Analysis, Verbatim Consistency sections with tables)\n- Page 22 shows mostly blank space with only text \"at larger scales.\" and page number \"22\" at bottom\n\n**Total Page Breakdown:**\n- Main body (intro + methodology + results): 6-7 pages\n- References: 1-2 pages  \n- Appendix: 12-14 pages\n- Final page 22: nearly blank (end matter)\n\n### Summary\n\n- **Total pages: 22**\n- **Main body fits within 8 pages: YES** (actually ~6-7 pages, leaving room in the 8-page limit)\n- **Anonymity: PROPERLY MAINTAINED** (Anonymous ACL submission)\n- **Visual Issues: NONE DETECTED** - Layout is clean, professional, properly formatted with ACL line numbers\n\nThe paper is well-prepared for review with proper anonymization and follows ACL submission guidelines."
      }
    ],
    "totalDurationMs": 42950,
    "totalTokens": 30027,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 4350,
      "cache_read_input_tokens": 25026,
      "output_tokens": 649,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4350
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 649,
          "cache_read_input_tokens": 25026,
          "cache_creation_input_tokens": 4350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4350,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 0,
      "bashCount": 8,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 3
    }
  },
  "sourceToolAssistantUUID": "2722e005-8a95-4d33-80a3-a95bbfb0f74f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 103 · 2026-05-16T04:22:29.529Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have all the information I need. Let me now compose my comprehensive review report.

Let me summarize what I've found:

## Key Issues for My Review:

### Novelty:
1. "Correlation-selection gap" - Is this truly novel? The distinction between instance-level signals and per-sample signals is somewhat obvious once stated. Four of five signals are instance-level, and the paper acknowledges they "fail by construction." This is definitional, not empirical.

2. LP compression as core finding - interesting but somewhat expected given constrained decoding and temperature settings.


3. Compared to Yao et al. (2026), the extensions with structural matching and selection analysis represent reasonable incremental progress, though the difficulty gradient aspect is somewhat expected.
4. The paper's core insight about MBR-style selection failing for IE aligns with related work on structured utilities, and they do acknowledge this connection.
5. The tautological nature of the "instance-level signals fail by construction" claim undermines the novelty—if a signal produces one score per input, it inherently cannot distinguish between samples.

The real empirical contribution boils down to LP compression and the MBR failure analysis. On related work, coverage is solid with 44 verified references, though there are some notable gaps: recent work on conformal structured prediction, alternative self-assessment signals, and confidence-aware sampling methods that directly address similar problems aren't included, and ensemble approaches are entirely absent.

The writing is generally clear and well-structured, though "preliminary" gets used repeatedly throughout the results section—honest but somewhat undermining. The paper packs substantial content into seven pages plus appendix while maintaining readability. The negative result framing actually works well here: it identifies a genuine gap and explains why existing approaches fall short, with actionable takeaways like difficulty-dependent signal recommendations and the N=8 practical threshold. The discussion of trained verifiers points toward future directions, and the work is self-contained enough that the main text stands alone despite the extensive appendix.

Most references check out—38 of 44 verified with just a few recent arXiv preprints I couldn't locate and minor author name formatting inconsistencies. Now I'm settling on scores: soundness around 3.5 since the methodology is solid but the RE conclusions are limited to a single benchmark, excitement between 2.5 and 3 because while the core finding is useful it's somewhat expected for a negative result paper, and overall around 3 reflecting thorough empirical work with incremental novelty. Reproducibility looks strong at 4 given the detailed appendix and promised code release.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cc82def-b8c3-49d3-8c0c-4b4308e6d779",
  "isSidechain": false,
  "requestId": "req_011Cb5cEdA4i2FHdtoGQY8Qk",
  "type": "assistant",
  "uuid": "e4eef388-5820-4036-88de-dd14c18dab83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3dBMa6sgH4bJB8JBZdzmS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1035,
      "cache_read_input_tokens": 99510,
      "output_tokens": 7506,
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
          "output_tokens": 7506,
          "cache_read_input_tokens": 99510,
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

### Assistant

_source line 104 · 2026-05-16T04:24:02.570Z_

所有材料已收集完毕。现在编写完整审稿报告。

---

## 总体评分
**Overall**: 3.0 / 5 (Findings)
**一句话总结**: 一篇方法论扎实的 empirical study，但核心概念"correlation-selection gap"的新颖性不足以支撑 main conference；instance-level signals "fail by construction" 是 definitional observation 而非 empirical contribution，LP compression 虽有价值但增量有限。

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计系统、统计方法严谨（bootstrap CI、TOST、permutation test），但 RE 结论仅基于 SciERC 单一 benchmark，且核心 claim 之一（instance-level signals fail by construction）是 definitional 而非 empirical |
| Excitement | 2.5/5 | 核心发现对 IE 实践者有参考价值，但"不同粒度的信号做不了同一件事"这一观察在概念上并不意外；相比 MBR 文献中已有的 utility-quality misalignment 讨论，增量贡献有限 |
| Overall | 3.0/5 | 适合 Findings track：thorough、honest、useful，但 novelty 和 impact 不够 main conference |
| Reproducibility | 4/5 | 训练配置、prompt 模板、超参数均在 Appendix 完整报告；代码承诺 acceptance 后公开；vLLM + constrained decoding 细节充分 |
| Confidence | 4/5 | 仔细阅读全文和 appendix，熟悉 self-consistency、MBR decoding 和 IE confidence estimation 相关文献 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] "Instance-level signals fail by construction" 是 definitional observation，不应算作 empirical contribution

- 具体位置：Section 1 (Contribution 1 "Metric dissociation")、Section 4.2 第二段、Section 5 第二段
- 问题：论文反复强调"四个 instance-level signals 因结构上只产生单一分数而无法做 per-sample selection"，但这是定义层面的必然结果（同一个数赋给所有 candidate，自然无法区分），不构成 empirical finding。论文自己也承认 "fail by construction"，但仍将其列为三大贡献之一（Contribution 1: "Metric dissociation"），混淆了 definitional 和 empirical contribution 的边界。
- 为什么影响接收：如果去掉这个 definitional 部分，论文的 empirical novelty 只剩 LP compression 和 MBR within-instance failure——前者是一个有趣但 scope 有限的观察，后者与 Eikema & Aziz (2025) 的 structured MBR 发现高度一致。整体 contribution bar 不够 main conference。
- 建议修改方向：将 instance-level 与 per-sample 的区分作为 problem formulation 中的前提条件呈现（Section 3），而非贡献之一。将 contribution 聚焦于 LP compression 的 empirical characterization 和 difficulty-dependent signal rankings，避免 overclaiming。

**N2** [critical] RE 结论仅基于 SciERC 单一 benchmark 且 40% zero-F1 rate，不足以支撑泛化性 claim

- 具体位置：Table 1（只有 SciERC RE 列）、Section 4.2 RE F1 结果、Conclusion 第 5 行
- 问题：论文在 NER 上使用了 3 个 benchmark（SciERC、CoNLL-2003、WNUT-17），但 RE 只用了 SciERC 且 40% 的 instance F1 为零。论文多次标注"preliminary"（正文至少出现 11 次），但同时在 Conclusion 和 Abstract 中将 RE 的 LP reversal under free-form decoding 作为核心发现之一呈现。在一个 40% failure rate 的单一 dataset 上的"preliminary"发现不应以 contribution-level claim 呈现。
- 为什么影响接收：RE 是 IE 的核心任务之一；如果 RE 部分全部标注为 preliminary，论文实质上只评估了 NER 任务，coverage 不够支撑"LLM-Based Information Extraction"这个 title scope。
- 建议修改方向：(a) 增加至少一个 RE benchmark（如 TACRED, DocRED, NYT），或 (b) 明确将 title 和 abstract 的 scope 限定为 NER，将 RE 作为"exploratory extension"在 discussion 中简要呈现。

**N3** [critical] 与 Yao et al. (2026) 的增量贡献定义不够清晰

- 具体位置：Section 1 第 8 行、Section 2 第 10 行
- 问题：论文 cite Yao et al. (2026) 并声称"we extend their work with structural matching, selection analysis, and a difficulty gradient"，但 (a) structural matching 的优势在 main result 中仅体现为 SJ 比 EM 高约 0.065 $\rho$（SciERC NER），bootstrap CI 显示 marginal significance；(b) selection analysis 的核心发现是"没有 signal 能做 selection"，这是一个 negative result；(c) difficulty gradient 的分析在 WNUT-17 上所有 signal 都 collapse，信息量有限。三个"extension"的 combined novelty 是否足够？
- 为什么影响接收：与 concurrent/recent work 的区分是 reviewers 和 ACs 做接收决定的关键因素。目前的 framing 让 contribution 看起来像是 Yao et al. (2026) 的 incremental extension + negative result，novelty bar 存疑。
- 建议修改方向：更明确地阐述 Yao et al. (2026) 未能回答的具体 research question，以及本文的 answers 为什么重要。特别是 selection analysis 作为"诊断性贡献"的价值——向社区展示 existing signals 有什么本质局限——需要更有力的 framing。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "Preliminary" 标注过于频繁，削弱论文可信度

- 具体位置：Abstract 第 6 行、Table 1 caption、Table 2 中多处、Section 4.2、Section 5、Conclusion
- 问题：正文和表格中"preliminary"出现至少 11 次。虽然标注诚实，但如此高频率让读者怀疑：如果作者自己都认为 RE 结果是 preliminary，为什么不在提交前完善？这给人一种"工作未完成就提交"的印象。
- 建议：要么在提交前补全 RE 实验使其不再 preliminary，要么将 RE 分析集中到一个明确标记的 subsection 中而非散布全文，减少"preliminary"出现频率。

**W2** [warning] LP compression 的解释不够深入——为什么 compressed？

- 具体位置：Section 5 "Why the gap exists"、Appendix G
- 问题：论文详细 characterize 了 LP compression（median range 0.041 nats, 60% tied），并排除了 constrained decoding 和 thinking token 作为原因，但未给出 LP 为什么在 within-instance 层面如此 compressed 的 mechanistic explanation。Verbalized confidence 同样 compressed（Appendix L）强化了"这是一个普遍现象"，但也进一步凸显了缺乏解释。
- 建议：讨论可能的 mechanism——例如，fine-tuned model 在 IE 任务上的 posterior 是否天然 peaked（low entropy over valid extractions），导致 LP 在正确和接近正确的 output 之间几乎没有区分度？这会增加论文的 explanatory depth。

**W3** [warning] 缺少对 conformal prediction / set-valued uncertainty 方向的讨论

- 具体位置：Section 2 "Uncertainty estimation and calibration"
- 问题：Conformal Structured Prediction (Mohri et al., ICLR 2025) 提出了针对 structured prediction 的 set-valued uncertainty quantification 框架，与本文的问题设置高度相关——都处理 set-valued output 的 uncertainty。论文未讨论 conformal approaches 是否能提供 selection-level 信号。
- 建议：在 Related Work 或 Discussion 中简要讨论 conformal prediction 作为 alternative uncertainty framework 的潜力。

**W4** [warning] 模型规模限于 3B-8B，对结论的适用范围有重要限制

- 具体位置：Limitations 第 2 行、Section 4.3 scale ablation
- 问题：论文仅覆盖 3B-8B 规模。在 test-time scaling 文献中，larger models (70B+) 的 output diversity 和 LP 分布可能有质的变化——更强的 model 可能产生更分散的 LP range，潜在地缩小 correlation-selection gap。Limitations 中提到但未充分讨论其对核心结论的影响。
- 建议：在 Discussion 中增加对规模影响的 informed speculation，例如基于已有 scaling law 文献的预测。

**W5** [warning] 选择 Spearman $\rho$ 作为核心 QE metric 缺乏充分 justification

- 具体位置：Section 3.3 "Quality estimation"
- 问题：$\rho$ 衡量 monotonic rank correlation，但 QE 的实际应用场景更多是 "哪些 instance 需要人工审查"（更接近 AUROC 的 binary classification 设置）。论文展示了 $\rho$-AUROC dissociation（Section 4.1 CoNLL），但未讨论在什么应用场景下应该使用哪个 metric。
- 建议：增加 1-2 句说明选择 $\rho$ 作为 primary metric 的 rationale，以及不同应用场景下 metric 选择的建议。

## 小问题（不影响接收）

- **引用格式**：`feng2025optimal` 的 bib entry 中 first author 字段 "Feng, Austin" 与 OpenAlex 匹配的 first name 不一致（bib 用 surname "Feng"，实际 first author 是 "Austin Feng"——这里是 bib 格式正确，API mismatch 无需修改）。`hobelsberger2025systematic` 和 `venktesh2025trust` 在 OpenAlex 上未找到匹配，可能是很新的 arXiv preprint。
- **术语一致性**：正文中交替使用 "per-sample signal" 和 "per-sample scoring"（Section 1 vs. Abstract），以及 "consensus-proximity selection" 和 "MBR" 作为同一概念的不同名称。建议在首次定义时明确二者等价关系。
- **Table 2 caption**："$^\dagger$Greedy: $T{=}1.0$ sample" 这里用脚注定义 greedy 略显随意，考虑到 greedy 在 NLP 中通常指 argmax decoding，建议正文第一次提及时就明确说明 "greedy 指 single sample at $T{=}1.0$, not argmax decoding"。
- **Ethics Statement**：提到 "CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement"，但该 corpus 的许可条款近年有争议，建议确认当前使用是否完全合规。
- **Figure 1 (fig_overview)**：两栏宽图，但 caption 中 "Left" 和 "Right" panel 的描述相当抽象——建议增加具体数值标注（如"$\rho=0.38$"）让图更 informative。

## 缺失引用

1. **Conformal Structured Prediction** (Mohri et al., ICLR 2025; arxiv 2410.06296) — 针对 structured prediction 的 set-valued uncertainty quantification，直接相关于本文处理 set-valued output 的 uncertainty estimation 问题
2. **"Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs"** (arxiv 2605.07806, May 2026) — 发现 effort/ability 等维度比 confidence 更能预测 LLM 性能，与本文的 verbalized confidence 分析互补
3. **"Learning When to Sample: Confidence-Aware Self-Consistency"** (arxiv 2603.08999, March 2026) — 用 confidence 决定是否需要额外 sampling，直接相关于本文的 difficulty-dependent signal analysis
4. **Slim-SC / Thought Pruning** (EMNLP 2025) — 通过语义聚类剪枝 redundant chains 来提升 self-consistency 效率，与本文的"更多 samples 无法提升 selection"发现形成有趣对比

## 主要优势

- **实验设计系统且严谨**：5 个 signal × 3 个 NER dataset × 2 个 model × 多 seed/温度/N 的 cross-product，配合 bootstrap CI、TOST、permutation test 等统计工具，在 negative result 论文中做到了较高标准。
- **诚实的 scope 限定**：频繁标注"preliminary"虽然影响阅读体验，但反映了负责任的学术态度；Limitations section 全面且坦诚。
- **清晰的 practical recommendations**：Table~\ref{tab:quality_estimation} 和 Discussion 中的 signal 选择建议（VC for hard NER, EM for easy NER, LP for RE）直接可 actionable。
- **Appendix 质量高**：22 页中 12+ 页 appendix，包含 LOO-SJ equivalence proof、SJ normalizer robustness、FK independence test、free-form ablation、OOD analysis 等，展示了作者对方法论细节的重视。
- **MBR failure 的 within- vs across-instance 分析**（Appendix M）是一个有价值的诊断贡献，清晰解释了为什么 consensus-proximity selection 在 IE 上失败。

---

将审稿报告发送给 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4eef388-5820-4036-88de-dd14c18dab83",
  "isSidechain": false,
  "requestId": "req_011Cb5cEdA4i2FHdtoGQY8Qk",
  "type": "assistant",
  "uuid": "e54bafee-6da9-4db9-a39e-a4b044bf71dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3dBMa6sgH4bJB8JBZdzmS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1035,
      "cache_read_input_tokens": 99510,
      "output_tokens": 7506,
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
          "output_tokens": 7506,
          "cache_read_input_tokens": 99510,
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

### Tool call

_source line 105 · 2026-05-16T04:24:34.415Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_011N9FeqByPUkJx2xd2vsFip`</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿报告\n\n**审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 呈现**\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5 (Findings)\n**一句话总结**: 方法论扎实的 empirical study，但核心概念 \"correlation-selection gap\" 的新颖性不足以支撑 main conference；instance-level signals \"fail by construction\" 是 definitional observation 而非 empirical contribution，LP compression 虽有价值但增量有限。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计系统、统计方法严谨（bootstrap CI、TOST、permutation test），但 RE 结论仅基于单一 benchmark 且 40% zero-F1，核心 claim 之一是 definitional 而非 empirical |\n| Excitement | 2.5/5 | 对 IE 实践者有参考价值，但\"不同粒度的信号做不了同一件事\"概念上不意外；相比 MBR 文献中已有的 utility-quality misalignment，增量有限 |\n| Overall | 3.0/5 | 适合 Findings：thorough、honest、useful，但 novelty 和 impact 不够 main conference |\n| Reproducibility | 4/5 | 训练配置、prompt、超参数完整；代码承诺 acceptance 后公开 |\n| Confidence | 4/5 | 仔细阅读全文和 appendix，熟悉相关文献 |\n\n## Must-Fix 问题\n\n**N1** [critical] \"Instance-level signals fail by construction\" 是 definitional observation，不应算作 empirical contribution\n- 位置：Section 1 Contribution 1、Section 4.2 第二段、Section 5 第二段\n- 论文反复强调四个 instance-level signals 因只产生单一分数而无法 per-sample selection，但这是定义层面的必然结果，不构成 empirical finding。论文自己也承认 \"fail by construction\"，却仍列为三大贡献之一（\"Metric dissociation\"）。去掉 definitional 部分后，empirical novelty 只剩 LP compression 和 MBR within-instance failure——前者 scope 有限，后者与 Eikema & Aziz (2025) structured MBR 发现高度一致。\n- 建议：将 instance-level/per-sample 区分作为 problem formulation 前提（Section 3），聚焦 LP compression 和 difficulty-dependent rankings 作为贡献。\n\n**N2** [critical] RE 结论仅基于 SciERC 单一 benchmark 且 40% zero-F1 rate\n- 位置：Table 1 RE 列、Table 2 RE F1、Conclusion 第 5 行\n- NER 有 3 个 benchmark，RE 只有 SciERC（40% zero-F1）。正文 \"preliminary\" 出现至少 11 次，但 Abstract 和 Conclusion 仍将 RE LP reversal 作为核心发现。单一 40% failure rate dataset 上的 \"preliminary\" 发现不应以 contribution-level claim 呈现。\"LLM-Based Information Extraction\" title scope 与实际 RE coverage 不匹配。\n- 建议：增加至少一个 RE benchmark，或将 scope 明确限定为 NER。\n\n**N3** [critical] 与 Yao et al. (2026) 的增量贡献定义不够清晰\n- 位置：Section 1 第 8 行、Section 2 第 10 行\n- 三个 \"extension\"（structural matching、selection analysis、difficulty gradient）中：(a) SJ 比 EM 高 0.065 ρ 仅 marginal significance；(b) selection analysis 核心是 negative result；(c) WNUT-17 所有 signal collapse。Combined novelty 是否足够 main conference paper？\n- 建议：更明确阐述 Yao et al. 未回答的具体 research question，以及本文 answers 为什么重要。\n\n## Should-Fix 问题\n\n**W1** [warning] \"Preliminary\" 标注过于频繁，削弱论文可信度\n- 正文至少 11 次 \"preliminary\"，给人 \"工作未完成就提交\" 的印象。\n- 建议：补全 RE 实验或将 RE 集中到明确标记的 subsection。\n\n**W2** [warning] LP compression 缺乏 mechanistic explanation\n- Section 5 详细 characterize 了 compression 现象并排除了多个原因，但未解释 WHY——例如 fine-tuned model 在 IE 任务上的 posterior 是否天然 peaked？\n- 建议：增加对 LP compression 机制的讨论。\n\n**W3** [warning] 缺少对 conformal prediction / set-valued uncertainty 的讨论\n- Conformal Structured Prediction (ICLR 2025, arxiv 2410.06296) 直接处理 structured prediction 的 set-valued uncertainty，与本文问题设置高度相关。\n- 建议：在 Related Work 或 Discussion 中简要讨论。\n\n**W4** [warning] 3B-8B 规模限制对结论适用范围影响大\n- Larger models (70B+) 的 LP 分布可能有质的变化。Limitations 提到但未充分讨论。\n\n**W5** [warning] Spearman ρ 作为 primary QE metric 缺乏 justification\n- ρ 衡量 rank correlation，但实际 QE 应用更接近 AUROC 的 binary classification。论文展示了 ρ-AUROC dissociation 但未讨论选择标准。\n\n## 小问题\n- 术语交替使用 \"per-sample signal\"/\"per-sample scoring\"、\"consensus-proximity selection\"/\"MBR\"，建议首次定义时明确等价关系\n- Table 2 \"Greedy: T=1.0 sample\" 在 NLP 中 greedy 通常指 argmax，建议正文首次提及时明确说明\n- Figure 1 caption 抽象，建议增加具体数值标注\n- Ethics Statement 中 CoNLL-2003 Reuters 许可条款近年有争议，建议确认合规性\n\n## 缺失引用\n1. Conformal Structured Prediction (ICLR 2025; arxiv 2410.06296) — set-valued uncertainty for structured prediction\n2. \"Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs\" (arxiv 2605.07806, May 2026) — alternative self-assessment dimensions\n3. \"Learning When to Sample: Confidence-Aware Self-Consistency\" (arxiv 2603.08999, March 2026) — confidence-aware sampling\n4. Slim-SC / Thought Pruning (EMNLP 2025) — efficient self-consistency via semantic pruning\n\n## 主要优势\n- 实验设计系统且严谨：5 signal × 3 NER dataset × 2 model × 多 seed/温度/N，配合完善的统计检验\n- 诚实的 scope 限定和负责任的 \"preliminary\" 标注\n- 清晰的 practical recommendations（VC for hard NER, EM for easy NER, LP for RE）\n- 高质量 Appendix（22 页中 12+ 页），包含 LOO-SJ equivalence、FK independence test、OOD analysis 等\n- MBR within- vs across-instance failure analysis 是有价值的诊断贡献\n\n## 格式合规\n- 页数：主体约 7 页（含 Limitations + Ethics），References 之后 Appendix，符合 8 页限制\n- 模板：`\\usepackage[review]{acl}` ✓，行号可见\n- 匿名：author = \"Anonymous\" ✓，未发现身份泄露\n- Ethics Statement：存在但较简短\n- Limitations：诚实且全面",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e54bafee-6da9-4db9-a39e-a4b044bf71dd",
  "isSidechain": false,
  "requestId": "req_011Cb5cEdA4i2FHdtoGQY8Qk",
  "type": "assistant",
  "uuid": "22d02112-241f-4a31-b9f3-723311581777",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3dBMa6sgH4bJB8JBZdzmS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1035,
      "cache_read_input_tokens": 99510,
      "output_tokens": 7506,
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
          "output_tokens": 7506,
          "cache_read_input_tokens": 99510,
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

### Runtime record

_source line 106_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的审查侧重：新颖性 + 相关工作覆盖 + 写作质量 + 呈现**  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **页数**: 长文 8 页 +…",
  "leafUuid": "22d02112-241f-4a31-b9f3-723311581777",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Runtime record

_source line 107_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 for structured IE confidence estimation paper",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Tool result

_source line 108 · 2026-05-16T04:24:38.120Z_

<details><summary>↩ Tool result · `toolu_011N9FeqByPUkJx2xd2vsFip`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22d02112-241f-4a31-b9f3-723311581777",
  "isSidechain": false,
  "promptId": "ef843608-8ab6-4fee-b2de-770e28382297",
  "type": "user",
  "uuid": "634cf450-97e9-41c0-b667-033299d93ffa",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "22d02112-241f-4a31-b9f3-723311581777",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 109_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 for structured IE confidence estimation paper",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Runtime record

_source line 110 · 2026-05-16T04:25:18.805Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T04:25:18.805Z",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "content": "[Round 1 审稿请求]:\n## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Overall: 3.5/5, Soundness 3.5, Excitement 3, Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] RE 覆盖不足与 claim scope 不匹配\n- Title \"LLM-Based Information Extraction\" + Abstract 将 RE 作为核心维度，但 RE 仅有 SciERC 一个 benchmark（40% zero-F1）。NER 3 个 benchmark，RE 0 个额外。\"Preliminary\" ≥12 次但 title/abstract 未体现。\n- 建议：限定 title/abstract scope 或增加 RE benchmark。\n\n**N2** [critical] ε=0.05 \"tied fraction\" 阈值的 circularity\n- Appendix 声称 median LP range (0.041) 低于 ε=0.05 作为 \"data-driven justification\"——这是 circular reasoning。Table 11 ε sweep 显示 ε=0.05 恰好给出最强 p-value (p=0.004)，暗示 p-value optimization。\n- 建议：用 pre-registered 或 literature-grounded ε，或报告 ε-free 连续指标。\n\n**N3** [critical] \"LP compression is model/task intrinsic\" 因果推断被 RE reversal 削弱\n- Abstract 声称 free-form ablation confirms compression not a decoding artifact，但 RE LP selection 在 free-form 下从 −0.68 pp 反转为 +1.69 pp。至少对 RE，constrained decoding 确实是 LP selection failure 的一个因素。\n\n### Should-Fix 问题\n\n**W1** Scale range (3B–8B) 过窄，不足以支撑 \"task difficulty is primary driver\" 因果结论\n**W2** 3 seeds 统计效力不足（Kendall's W=1.000 with n=3 不具信息量）\n**W3** \"Greedy\" baseline 实为 T=1.0 random sample，命名混淆\n**W4** 缺少信号组合实验（如 VC 筛选 + LP 排序）\n**W5** Gold-empty filtering 比例差异（CoNLL 20.2% vs SciERC 4.0%）影响跨数据集可比性\n**W6** Thinking token confound 的 CoNLL control 论证薄弱——CoNLL 高 tied fraction 更可能因 task easiness\n\n### 小问题\n- Table 3 NER 2-seed vs 其他 3 seeds 未说明\n- Figure 1 caption 对 LP 不适用\n- \\cite vs \\citet 不一致\n\n### Missing References\n- Huang et al. (2024) \"Large Language Models Cannot Self-Correct Reasoning Yet\"\n- Fernandes et al. (2022) \"Quality-Aware Decoding for Neural Machine Translation\"\n\n### 主要优势\n- 统计方法论上乘\n- 三指标 dissociation 框架有贡献\n- 极其详尽的 appendix\n- LP compression 诊断分析系统性强\n- Matched training protocol\n\n---\n\n请对 Reviewer 1 的每个 Must-Fix、Should-Fix、小问题和缺失引用逐条回应 [AGREE] 或 [REBUT]。"
}
```

---

### Runtime record

_source line 111 · 2026-05-16T04:25:18.805Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T04:25:18.805Z",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

## Round 2

2 recorded events

### User

_source line 112 · 2026-05-16T04:25:18.796Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "634cf450-97e9-41c0-b667-033299d93ffa",
  "isSidechain": false,
  "promptId": "972e434d-f261-4952-9bd8-d6687c8bbc36",
  "type": "user",
  "isMeta": true,
  "uuid": "6fda9f02-c40d-4e77-8077-27759081d6d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 113 · 2026-05-16T04:25:18.796Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fda9f02-c40d-4e77-8077-27759081d6d8",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "8e3249a8-dbe6-4afb-8374-cf26a75ac374",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "0c3c074f-a63a-48aa-9b7b-9c1c8b218eba",
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

14 recorded events

### User

_source line 114 · 2026-05-16T04:25:18.911Z_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 1 的完整审稿原文：

### Overall: 3.5/5, Soundness 3.5, Excitement 3, Confidence 4/5

### Must-Fix 问题

**N1** [critical] RE 覆盖不足与 claim scope 不匹配
- Title "LLM-Based Information Extraction" + Abstract 将 RE 作为核心维度，但 RE 仅有 SciERC 一个 benchmark（40% zero-F1）。NER 3 个 benchmark，RE 0 个额外。"Preliminary" ≥12 次但 title/abstract 未体现。
- 建议：限定 title/abstract scope 或增加 RE benchmark。

**N2** [critical] ε=0.05 "tied fraction" 阈值的 circularity
- Appendix 声称 median LP range (0.041) 低于 ε=0.05 作为 "data-driven justification"——这是 circular reasoning。Table 11 ε sweep 显示 ε=0.05 恰好给出最强 p-value (p=0.004)，暗示 p-value optimization。
- 建议：用 pre-registered 或 literature-grounded ε，或报告 ε-free 连续指标。

**N3** [critical] "LP compression is model/task intrinsic" 因果推断被 RE reversal 削弱
- Abstract 声称 free-form ablation confirms compression not a decoding artifact，但 RE LP selection 在 free-form 下从 −0.68 pp 反转为 +1.69 pp。至少对 RE，constrained decoding 确实是 LP selection failure 的一个因素。

### Should-Fix 问题

**W1** Scale range (3B–8B) 过窄，不足以支撑 "task difficulty is primary driver" 因果结论
**W2** 3 seeds 统计效力不足（Kendall's W=1.000 with n=3 不具信息量）
**W3** "Greedy" baseline 实为 T=1.0 random sample，命名混淆
**W4** 缺少信号组合实验（如 VC 筛选 + LP 排序）
**W5** Gold-empty filtering 比例差异（CoNLL 20.2% vs SciERC 4.0%）影响跨数据集可比性
**W6** Thinking token confound 的 CoNLL control 论证薄弱——CoNLL 高 tied fraction 更可能因 task easiness

### 小问题
- Table 3 NER 2-seed vs 其他 3 seeds 未说明
- Figure 1 caption 对 LP 不适用
- \cite vs \citet 不一致

### Missing References
- Huang et al. (2024) "Large Language Models Cannot Self-Correct Reasoning Yet"
- Fernandes et al. (2022) "Quality-Aware Decoding for Neural Machine Translation"

### 主要优势
- 统计方法论上乘
- 三指标 dissociation 框架有贡献
- 极其详尽的 appendix
- LP compression 诊断分析系统性强
- Matched training protocol

---

请对 Reviewer 1 的每个 Must-Fix、Should-Fix、小问题和缺失引用逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e3249a8-dbe6-4afb-8374-cf26a75ac374",
  "isSidechain": false,
  "promptId": "972e434d-f261-4952-9bd8-d6687c8bbc36",
  "type": "user",
  "uuid": "50649d1f-925a-4db9-a700-91c13ff5c18b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 115 · 2026-05-16T04:26:11.526Z_

<details><summary>Logged reasoning block</summary>

```text
The Director is asking me to respond to Reviewer 1's review, point by point, using [AGREE] or [REBUT] with evidence from the paper. Let me go through each item carefully.

Let me re-read key parts of the paper to make sure my responses are grounded in specific evidence.

Let me go through Reviewer 1's points:

**N1** RE coverage insufficient - I raised this same issue as my N2. I agree.

**N2** ε=0.05 circularity - This is an interesting point. Let me check the paper's handling of this. The paper says in Appendix G (line 499): "The median within-instance LP range is only 0.041 nats—below the ε=0.05 threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice." And Table 11 shows the ε sweep. 

Looking at the sensitivity analysis, ε=0.05 does yield the strongest p-value at .004 compared to other thresholds, but the paper also justifies this choice through the empirical distribution of LP ranges rather than selecting it post-hoc based on statistical significance. sweep in Table 12 (Appendix G), showing selection F1 is robust across ε ∈ [0, 0.2]. And the paper does present the full sweep transparently. However, calling it "data-driven justification" when it happens to give the best p-value is indeed problematic. But I should note that the paper also presents ε-free continuous metrics (within-instance ρ(LP, F1) = 0.248 across all instances, Appendix G line 532). So this partially addresses the concern.

Actually, let me reconsider. The ε=0.05 is used for the tied/non-tied partition analysis, but the main selection results in Table 2 don't depend on ε for LP (LP directly ranks candidates by their scores). The ε is used for:
1. Defining the "tied" vs "non-tied" subset analysis
2. For consensus-based signals in MBR-style selection

Looking at the robustness section, Spearman ρ is the primary quality metric and doesn't depend on any discretization threshold—ε only affects the diagnostic subset analysis. For the main result in Table 2, LP ranks candidates directly without ε, so the circularity concern is really about the non-tied subset analysis, not the primary finding that LP selection matches greedy across the full dataset. The Abstract's claim about compression being intrinsic is worth revisiting though, given the RE reversal point. So the distinction is that LP compression itself—the tightness of the distribution—appears intrinsic to NER and doesn't depend on decoding regime, but for RE, the *selection* of which model wins reverses between constrained and free-form decoding, even though the underlying distributions stay similar. This suggests the paper's core claim about NER holds up, though the RE behavior reveals something more complex about how small LP differences get interpreted differently depending on the decoding setup.

Looking at the weaknesses now: the scale range critique is valid and overlaps with my own concern. The statistical power issue with only 3 seeds and perfect Kendall's W is legitimate, though the paper's practical choice and small variance values provide some reassurance. The "greedy" terminology is genuinely confusing given the actual definition. The missing experiments around combining signals—like using VC for filtering and LP for ranking—would strengthen the work, though that's more of an extension than a core flaw.

On the gold-empty filtering discrepancy between CoNLL and SciERC, the paper does explain this in the appendix due to dataset characteristics, but it deserves more visibility in the main text. For the thinking token control argument on CoNLL, I need to examine whether the high tied fraction is actually attributable to task easiness rather than the thinking tokens themselves.

Looking at the paper's logic: if thinking tokens caused LP compression on SciERC, CoNLL should show lower tied fractions, but it shows higher ones instead. However, R1 makes a fair point that CoNLL's inherent task difficulty is a confound here—easier tasks naturally produce higher tied fractions regardless of thinking tokens, so the control isn't as clean as presented.

There are also some minor presentation issues to address: Table 2 uses 2-seed statistics for NER while other tables use 3 seeds, which needs clarification; Figure 1's caption about instance-level signals might misleadingly suggest it applies to all signal types; and there's some inconsistency in citation formatting that should be standardized.

I should also note that while Huang et al.'s work on self-correction is tangentially related, Fernandes et al.'s paper on quality-aware decoding with MBR is directly relevant to the discussion and worth including.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50649d1f-925a-4db9-a700-91c13ff5c18b",
  "isSidechain": false,
  "requestId": "req_011Cb5cVDwjNdTeca9BAz8fp",
  "type": "assistant",
  "uuid": "5f1cb778-8c02-41ab-a708-261d25551600",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018B9oNPhSbBP266TwTu4yic",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 82058,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 82058,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2224,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 82058,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 82058
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 60660
      }
    }
  }
}
```

</details>

---

### Assistant

_source line 116 · 2026-05-16T04:26:11.543Z_

逐条回应 Reviewer 1 的审稿意见。先确认几个关键细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f1cb778-8c02-41ab-a708-261d25551600",
  "isSidechain": false,
  "requestId": "req_011Cb5cVDwjNdTeca9BAz8fp",
  "type": "assistant",
  "uuid": "ca811da8-8ced-4e83-91a3-bdec44f99a69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018B9oNPhSbBP266TwTu4yic",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 82058,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 82058,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2224,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 82058,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 82058
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 60660
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-16T04:26:12.440Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AVaGkjpPXfDk3Yx6i3LHRv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 496,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca811da8-8ced-4e83-91a3-bdec44f99a69",
  "isSidechain": false,
  "requestId": "req_011Cb5cVDwjNdTeca9BAz8fp",
  "type": "assistant",
  "uuid": "be31fffb-1397-42fc-89cb-41008f931bd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018B9oNPhSbBP266TwTu4yic",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 82058,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 82058,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2224,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 82058,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 82058
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 60660
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-16T04:26:13.159Z_

<details><summary>↩ Tool result · `toolu_019WqXpru4h54f1jLRBwjeBC`</summary>

```text
55	
56	We define the correlation-selection gap as the disparity between a signal's instance-level rank correlation with F1 and its ability to select the best output from $N$ candidates.
57	
58	\begin{table}[t]
59	\centering
60	\small
61	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). LP is per-sample; others are instance-level. NER: 2-seed mean${\pm}\sigma$, Fisher $p$ vs.\ greedy; RE: single seed (preliminary). Best non-oracle in \textbf{bold}. $^\dagger$Greedy: $T{=}1.0$ sample.}
62	\label{tab:selection}
63	\begin{tabular}{lccc}
64	\toprule
65	Method & NER F1 & $p$ & RE F1 \\
66	\midrule
67	Oracle & $0.778 \pm 0.003$ & --- & 0.585 \\
68	\midrule
69	\multicolumn{4}{l}{\textit{Per-sample signal}} \\
70	LP           & $\mathbf{0.647} \pm 0.005$ & .29 & 0.395 \\
71	\midrule
72	\multicolumn{4}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
73	SJ           & $0.646 \pm 0.002$ & .68 & 0.386 \\
74	FK           & $0.646 \pm 0.001$ & .79 & --- \\
75	EM           & $0.637 \pm 0.001$ & .45 & 0.372 \\
76	VC           & $0.623 \pm 0.004$ & .26 & 0.359 \\
77	\midrule
78	Greedy$^\dagger$ & $0.645 \pm 0.001$ & --- & \textbf{0.404} \\
79	Random           & $0.610 \pm 0.003$ & --- & 0.354 \\
80	\bottomrule
81	\end{tabular}
82	\end{table}
83	
84	Despite strong quality estimation, confidence signals yield limited selection gains (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
85	Instance-level signals (SJ, FK, EM, VC) assign identical scores to all candidates per input and cannot rank outputs by construction; the key question is whether LP---the only per-sample signal---can exploit the oracle headroom.
86	
87	\paragraph{No significant improvement over greedy.}
88	On SciERC NER (2-seed sign tests, $n{=}551$), the oracle (0.778) reveals 13.3~pp of headroom above greedy (0.645), yet LP achieves only 0.647 ($\Delta{=}{+}0.2$~pp, $p{=}0.29$); no signal consistently improves selection ($p{>}0.05$; TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration, Appendix~\ref{app:tost}).
89	On RE, the best signal (LP, 0.395) falls below greedy (0.404; preliminary), with 18.1~pp unrealized.
90	The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}).
91	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best; closing this gap likely requires trained verifiers \cite{cobbe2021verifiers}.\footnote{For negative results (all $p{>}0.05$), uncorrected tests suffice; the sole positive finding (non-tied LP subset, $+2.9$~pp, $p{=}0.004$; \S\ref{sec:discussion}) survives Bonferroni correction over 5 comparisons.}
92	
93	%% ============================================================
94	\subsection{Robustness}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6aeed4b1-a9b4-4180-be97-205051ab9ba2",
  "isSidechain": false,
  "promptId": "972e434d-f261-4952-9bd8-d6687c8bbc36",
  "type": "user",
  "uuid": "c4e87549-437d-42e5-aab5-3b2e40bf57f3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\nWe define the correlation-selection gap as the disparity between a signal's instance-level rank correlation with F1 and its ability to select the best output from $N$ candidates.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). LP is per-sample; others are instance-level. NER: 2-seed mean${\\pm}\\sigma$, Fisher $p$ vs.\\ greedy; RE: single seed (preliminary). Best non-oracle in \\textbf{bold}. $^\\dagger$Greedy: $T{=}1.0$ sample.}\n\\label{tab:selection}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & NER F1 & $p$ & RE F1 \\\\\n\\midrule\nOracle & $0.778 \\pm 0.003$ & --- & 0.585 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 & 0.395 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .68 & 0.386 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 & --- \\\\\nEM           & $0.637 \\pm 0.001$ & .45 & 0.372 \\\\\nVC           & $0.623 \\pm 0.004$ & .26 & 0.359 \\\\\n\\midrule\nGreedy$^\\dagger$ & $0.645 \\pm 0.001$ & --- & \\textbf{0.404} \\\\\nRandom           & $0.610 \\pm 0.003$ & --- & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited selection gains (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nInstance-level signals (SJ, FK, EM, VC) assign identical scores to all candidates per input and cannot rank outputs by construction; the key question is whether LP---the only per-sample signal---can exploit the oracle headroom.\n\n\\paragraph{No significant improvement over greedy.}\nOn SciERC NER (2-seed sign tests, $n{=}551$), the oracle (0.778) reveals 13.3~pp of headroom above greedy (0.645), yet LP achieves only 0.647 ($\\Delta{=}{+}0.2$~pp, $p{=}0.29$); no signal consistently improves selection ($p{>}0.05$; TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration, Appendix~\\ref{app:tost}).\nOn RE, the best signal (LP, 0.395) falls below greedy (0.404; preliminary), with 18.1~pp unrealized.\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}).\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best; closing this gap likely requires trained verifiers \\cite{cobbe2021verifiers}.\\footnote{For negative results (all $p{>}0.05$), uncorrected tests suffice; the sole positive finding (non-tied LP subset, $+2.9$~pp, $p{=}0.004$; \\S\\ref{sec:discussion}) survives Bonferroni correction over 5 comparisons.}\n\n%% ============================================================\n\\subsection{Robustness}",
      "numLines": 40,
      "startLine": 55,
      "totalLines": 121
    }
  },
  "sourceToolAssistantUUID": "6aeed4b1-a9b4-4180-be97-205051ab9ba2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-16T04:26:12.453Z_

<details><summary>↩ Tool result · `toolu_01AVaGkjpPXfDk3Yx6i3LHRv`</summary>

```text
496	\section{Log-Probability Score Compression}\label{app:logprob_ties}
497	
498	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
499	The median within-instance LP range is only 0.041 nats---below the $\varepsilon{=}0.05$ threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice.
500	At $\varepsilon{=}0.05$, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below the threshold, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
501	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
502	This compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\%$ (vs.\ seed${=}42$: $0.041$ nats, $60.3\%$).
503	Seed~456 uses a different subtask flag (joint vs.\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\ 8.20 nats; Mann--Whitney $p{=}0.55$), confirming that the subtask change does not affect compression.
504	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
505	
506	\begin{figure}[t]
507	\centering
508	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
509	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
510	\label{fig:lp_range_cdf}
511	\end{figure}
512	
513	\begin{table}[t]
514	\centering
515	\small
516	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
517	\label{tab:logprob_ties}
518	\begin{tabular}{lc}
519	\toprule
520	$\varepsilon$ threshold & Tied instances (\%) \\
521	\midrule
522	0.01 & 1.1\% \\
523	0.05 & 60.3\% \\
524	0.1  & ${\sim}$84\% \\
525	0.5  & ${\sim}$99\% \\
526	\bottomrule
527	\end{tabular}
528	\end{table}
529	
530	\paragraph{Non-tied subset.}
531	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
532	As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.
533	A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
534	
535	\paragraph{$\varepsilon$ sensitivity sweep.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be31fffb-1397-42fc-89cb-41008f931bd8",
  "isSidechain": false,
  "promptId": "972e434d-f261-4952-9bd8-d6687c8bbc36",
  "type": "user",
  "uuid": "f0ce4e62-bbf4-426c-936f-37d105ac702e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}, Figure~\\ref{fig:lp_range_cdf}).\nThe median within-instance LP range is only 0.041 nats---below the $\\varepsilon{=}0.05$ threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice.\nAt $\\varepsilon{=}0.05$, 60.3\\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below the threshold, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nThe CDF rises smoothly with no cliff or discontinuity (Figure~\\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.\nThis compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\\%$ (vs.\\ seed${=}42$: $0.041$ nats, $60.3\\%$).\nSeed~456 uses a different subtask flag (joint vs.\\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\\ 8.20 nats; Mann--Whitney $p{=}0.55$), confirming that the subtask change does not affect compression.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_lp_range_cdf}\n\\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}\n\\label{fig:lp_range_cdf}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nAs a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\\rho(\\text{LP}, \\text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\\% of instances achieve $p{<}0.05$ significance, and $\\rho(\\text{LP range}, \\text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.\nA free-form NER decoding ablation (Appendix~\\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.\n\n\\paragraph{$\\varepsilon$ sensitivity sweep.}",
      "numLines": 40,
      "startLine": 496,
      "totalLines": 959
    }
  },
  "sourceToolAssistantUUID": "be31fffb-1397-42fc-89cb-41008f931bd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-16T04:26:13.153Z_

<details open><summary>🔧 Tool call — Read · `toolu_019WqXpru4h54f1jLRBwjeBC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": 55,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0ce4e62-bbf4-426c-936f-37d105ac702e",
  "isSidechain": false,
  "requestId": "req_011Cb5cVDwjNdTeca9BAz8fp",
  "type": "assistant",
  "uuid": "6aeed4b1-a9b4-4180-be97-205051ab9ba2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018B9oNPhSbBP266TwTu4yic",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 82058,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 82058,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2224,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 82058,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 82058
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 60660
      }
    }
  }
}
```

</details>

---

### Runtime record

_source line 121 · 2026-05-16T04:26:13.259Z_

```json
{
  "parentUuid": "c4e87549-437d-42e5-aab5-3b2e40bf57f3",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "740ed3c2-341b-4349-aeff-4eb719fc6d69",
  "timestamp": "2026-05-16T04:26:13.259Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 122_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 交叉分享 — Reviewer 1 的完整审稿意见  请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。  ---  以下是 Reviewer 1 的完整审稿原文：  ### Overall: 3.5/5…",
  "leafUuid": "740ed3c2-341b-4349-aeff-4eb719fc6d69",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Runtime record

_source line 123_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 for structured IE confidence estimation paper",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b"
}
```

---

### Assistant

_source line 124 · 2026-05-16T04:26:22.701Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the details I need. Let me compose my cross-review response to Reviewer 1's points.

Let me re-read the Abstract to carefully check N3:
"A 4-seed free-form decoding ablation confirms NER compression is not an artifact of constrained decoding; on RE, LP selection reverses direction under free-form decoding (+1.8±0.1 pp; preliminary, single benchmark), suggesting regime-dependent behavior."

So the Abstract does scope the NER claim correctly and separately notes RE. But R1's point is about the broader narrative - if constrained decoding affects LP selection for RE, then "compression is model/task intrinsic" can't be a blanket claim.


The free-form ablation reveals something important: the distributional properties of LP scores stay remarkably stable across decoding regimes (the compression itself is intrinsic), but what actually changes is how those compressed scores translate into task performance for RE. So the distinction is that compression is a model property, but the downstream utility of those compressed representations varies by task and regime.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "740ed3c2-341b-4349-aeff-4eb719fc6d69",
  "isSidechain": false,
  "requestId": "req_011Cb5cZEHgVRAQkgNVeoNAg",
  "type": "assistant",
  "uuid": "e0e6540a-ff76-450b-bba0-7c7ae672f6de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XngSyXqCfP6PsnzYqZiE9w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4596,
      "cache_read_input_tokens": 93899,
      "output_tokens": 4949,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4596,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4949,
          "cache_read_input_tokens": 93899,
          "cache_creation_input_tokens": 4596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4596
          },
          "type": "message"
        }
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

_source line 125 · 2026-05-16T04:27:33.085Z_

已确认关键细节。以下是对 Reviewer 1 各条的逐条回应。

---

## Must-Fix 问题

**[AGREE] R1-N1: RE 覆盖不足与 claim scope 不匹配**

与我的 N2 完全一致。Title "LLM-Based Information Extraction" 暗示 NER+RE 双任务的充分覆盖，但 RE 仅有 SciERC（40% zero-F1），且正文"preliminary"出现 ≥11 次。Abstract 第 6 行和 Conclusion 第 5 行仍将 RE LP reversal 作为核心发现呈现，与"preliminary"标注矛盾。Reviewer 1 的建议（限定 scope 或增加 benchmark）是正确的修改方向。

**[AGREE with nuance] R1-N2: ε=0.05 circularity**

同意核心批评：Appendix G（line 499）称 median LP range 0.041 nats "providing data-driven justification for this cutoff" 确实构成 circular reasoning——用数据选阈值，再用该阈值得到最强 p-value（Table 11: ε=0.05 给出 p=0.004，而 ε=0.03 为 p=0.079，ε=0.10 为 p=0.034），有 p-value optimization 之嫌。

但需指出两个缓解因素：(1) 论文的**主 selection 结果**（Table 2）不依赖 ε——LP 直接对 candidate 排序，全 dataset 上 Δ=+0.2pp (p=0.29)，这是 ε-free 的；ε 仅影响诊断性的 tied/non-tied subset 分析。(2) Appendix G（line 532）报告了 ε-free 的连续指标：pooled within-instance ρ(LP, F1)=0.248，佐证了 LP 在 instance 内有弱正信号但 compression 限制利用。因此 circularity 影响的是辅助分析的 credibility，不动摇主结论。建议作者采用 literature-grounded ε 或直接以连续 CDF 呈现。

**[REBUT with partial agreement] R1-N3: RE reversal 削弱 "LP compression is intrinsic" 因果推断**

Reviewer 1 的观察有道理但混淆了两个层面：LP **compression**（分布特征）和 LP **selection outcome**（选择效果）。

Free-form ablation Panel A（Appendix I, Table 14）明确显示 LP 分布在两种 regime 下几乎一致：NER within-instance std ratio = 0.97, mean range difference = −0.0024 nats, tied fraction 从 59.7% 仅降到 57.7%。也即 **LP compression 本身确实是 intrinsic 的，不因 decoding regime 改变**。

RE 上反转的是 **selection outcome**（从 −0.68pp 到 +1.69pp），而非 LP 分布。这说明在 compression 同等的情况下，free-form decoding 改变了 LP 分数与质量之间的 *mapping*——可能因为 constrained decoding 对 RE 任务的 token-level probability 分配方式不同于 NER。论文 Discussion（Section 5, line 14-18）将此称为 "regime-dependent behavior"，Abstract 也正确区分了 "confirms NER compression" 与 "on RE, LP selection reverses direction"。

不过，我同意 R1 的隐含批评：论文未充分解释 **为什么** 同样 compressed 的 LP 在 RE free-form 下突然有效。这个 mechanistic gap 降低了该发现的说服力。建议增加对 RE-specific decoding interaction 的分析。

## Should-Fix 问题

**[AGREE] R1-W1: Scale range (3B–8B) 过窄**

与我的 W4 一致。"Task difficulty is the primary driver" 这个因果表述（Section 4.3, line 120）在 3B–8B range 内可能成立，但不能排除 70B+ 规模下 LP distribution 发生质变的可能。

**[AGREE] R1-W2: 3 seeds 统计效力不足，Kendall's W=1.000 不具信息量**

正确的统计批评。Kendall's W with n=3 rankings 的 critical value 门槛极低——5 个 signal 的 3 个 ranking 完全一致（W=1.000）看似完美，但实际上 W 的置信区间极宽。Appendix K（Table 16）报告 W=1.000 for NER at N=8 但样本量太小无法排除巧合。论文应增加 seeds 或至少报告 W 的 exact permutation p-value 而非仅给 W 值。

**[AGREE] R1-W3: "Greedy" baseline 命名混淆**

与我的小问题一致。Table 2 footnote 定义 "Greedy: T=1.0 sample"，但在 NLP 中 greedy decoding 通常指 argmax (T→0)。一个 T=1.0 随机样本更准确的名称应为 "single-sample" 或 "baseline sample"。当前命名会误导读者以为 baseline 是 deterministic argmax。

**[AGREE] R1-W4: 缺少信号组合实验**

有效建议。论文评估了 5 个独立 signal，但未探索组合方案——例如用 VC（instance-level）做 difficulty-aware routing（高 VC → 直接输出; 低 VC → 用 LP 做 per-sample selection），或简单的 VC×LP 乘积。考虑到论文 Discussion 中已指出 VC 和 LP 在不同 regime 下各有优势（Section 5 line 1-3），不探索组合是一个明显的遗漏。这不会改变核心 negative result，但能提供更完整的 empirical picture。

**[REBUT] R1-W5: Gold-empty filtering 比例差异影响跨数据集可比性**

Appendix B（line 30-32）明确解释了 filtering 原因："For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality." CoNLL 20.2% gold-empty 是数据集本身特征（3453 中 697 个句子没有标注实体），不是方法论选择。

更关键的是：(1) 论文的跨数据集对比主要在 signal **rankings** 而非绝对 ρ 值层面进行（如 Table 1 中 structural > surface > LP 的排序在两个 dataset 上一致）；(2) Selection 分析使用 full set (n=551 / n=3453) 不做 filtering（Section 3.3, line 56-57: "Correlation analyses exclude empty gold annotations; selection retains the full set"）。Gold-empty filtering 仅影响 QE correlation，且 filtering 比例差异反映的是 task 特征而非 confound。

**[AGREE with nuance] R1-W6: Thinking token confound 的 CoNLL control 论证薄弱**

同意 R1 的核心观察：CoNLL 高 tied fraction（86.8%）更可能因 task easiness（greedy F1≈0.91, 57-88% identical outputs per Table 8）而非 thinking token 的缺失。论文 Appendix D（line 491-494）的论证是 "如果 thinking token 导致 SciERC LP compression，CoNLL 应更低，但实际更高"——这个 control 不 clean，因为 task difficulty 是 confound。

不过 Appendix D 另外两个论证较强：(1) LP shift magnitude 仅 0.001 nats/token（2.68% of median range），且 all samples 共享同一 prefix → within-instance ranking 不变（line 483-489）；(2) constant prefix cancellation argument 基于数学推理而非 empirical control。thinking token confound 的总体证据充分，只是 CoNLL control 这个具体论证确实弱。

## 小问题

**[AGREE] R1-Minor-1: Table 2 NER 2-seed vs 其他 3-seed 未说明**

Table 2 caption 标注 "NER: 2-seed mean±σ"，但 Table 7（multi-seed stability）用 3 seeds。为什么 selection 用 2 seeds 而 QE 用 3 seeds？如果是因为一个 seed 的 selection 实验未完成，应在文中说明。

**[AGREE] R1-Minor-2: Figure 1 caption 对 LP 不适用**

Figure 1 caption 说 "instance-level signals assign identical scores to all candidates, precluding sample selection"，这只适用于 4 个 instance-level signals。LP 是 per-sample signal，不受此限制。Caption 应区分两类 signal 的 failure mode。

**[REBUT] R1-Minor-3: \cite vs \citet 不一致**

检查 tex 源码，`\citet` 用于句中主语位置（如 "Yao et al. (2026) examine..."，Section 2 line 10），`\citep`/`\cite` 用于括号引用，符合 natbib 标准用法。未发现系统性不一致。如 R1 能指出具体位置，可进一步检查。

## 缺失引用

**[REBUT] R1-Missing-1: Huang et al. (2024) "Large Language Models Cannot Self-Correct Reasoning Yet"**

该论文讨论 LLM self-correction（模型修改自己的推理输出），与本文的 self-consistency（多次采样后比较/选择）是不同的 paradigm。本文不涉及 iterative self-correction，而是 one-shot multi-sample evaluation。关联性有限，不构成必须引用的缺失。

**[AGREE] R1-Missing-2: Fernandes et al. (2022) "Quality-Aware Decoding for Neural Machine Translation"**

直接相关。Fernandes et al. 将 quality estimation 与 MBR decoding 结合，使用 learned quality estimators 进行 reranking——本文 Discussion 中 "trained verifiers" 的建议（Section 5, line 24）与此高度相关。引用该工作能更好地将本文的 negative result（unsupervised signals 无法 selection）与已有的 supervised quality-aware decoding 文献连接起来。

---

将交叉回应发送给 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0e6540a-ff76-450b-bba0-7c7ae672f6de",
  "isSidechain": false,
  "requestId": "req_011Cb5cZEHgVRAQkgNVeoNAg",
  "type": "assistant",
  "uuid": "fe47cf9c-ac9c-4ccf-976b-73ce528ddbe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XngSyXqCfP6PsnzYqZiE9w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4596,
      "cache_read_input_tokens": 93899,
      "output_tokens": 4949,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4596,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4949,
          "cache_read_input_tokens": 93899,
          "cache_creation_input_tokens": 4596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4596
          },
          "type": "message"
        }
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

_source line 126 · 2026-05-16T04:27:55.318Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01WNrzYNBeZF2hWuJ9rsZHzs`</summary>

```json
{
  "text": "## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix\n\n**[AGREE] R1-N1: RE 覆盖不足与 claim scope 不匹配**\n与我的 N2 完全一致。Title 暗示 NER+RE 充分覆盖，但 RE 仅有 SciERC（40% zero-F1），\"preliminary\" ≥11 次但 title/abstract 未体现。\n\n**[AGREE with nuance] R1-N2: ε=0.05 circularity**\n同意核心批评：Appendix G (line 499) \"data-driven justification\" 确为 circular reasoning，Table 11 中 ε=0.05 恰好给出最强 p=0.004 有 p-hacking 之嫌。但需指出两个缓解因素：(1) 主 selection 结果（Table 2）不依赖 ε——LP 直接排序 candidate，全 dataset Δ=+0.2pp (p=0.29) 是 ε-free 的；ε 仅影响诊断性 tied/non-tied subset 分析。(2) Appendix G (line 532) 报告了 ε-free 连续指标 pooled within-instance ρ(LP, F1)=0.248。circularity 影响辅助分析 credibility，不动摇主结论。\n\n**[REBUT with partial agreement] R1-N3: RE reversal 削弱 \"compression is intrinsic\" 因果推断**\nR1 混淆了两个层面。Free-form ablation Panel A (Appendix I, Table 14) 显示 LP **分布** 在两种 regime 下几乎一致（std ratio 0.97, range difference −0.0024, tied fraction 59.7%→57.7%）。LP compression 本身确实 intrinsic。RE 反转的是 **selection outcome**（−0.68→+1.69pp），非 LP 分布。Abstract 正确区分 \"confirms NER compression\" 与 \"on RE, LP selection reverses\"。但同意论文未充分解释 WHY 同样 compressed 的 LP 在 RE free-form 下有效，这个 mechanistic gap 需要补充。\n\n### Should-Fix\n\n**[AGREE] R1-W1**: 与我的 W4 一致。3B-8B 不足以支撑因果结论。\n\n**[AGREE] R1-W2**: 正确统计批评。W=1.000 with n=3 置信区间极宽，应增 seeds 或报告 exact permutation p-value。\n\n**[AGREE] R1-W3**: 与我的小问题一致。\"Greedy\" 在 NLP 中通常指 argmax，T=1.0 sample 应命名为 \"single-sample baseline\"。\n\n**[AGREE] R1-W4**: 有效建议。不探索 VC+LP 等组合是明显遗漏，尤其是论文已指出两者在不同 regime 下各有优势（Section 5）。\n\n**[REBUT] R1-W5**: Gold-empty filtering 比例差异反映 dataset 特征而非 confound。Appendix B 解释了原因。跨数据集对比在 signal ranking 层面（非绝对 ρ 值），且 selection 分析用 full set 不 filter（Section 3.3, line 56-57）。\n\n**[AGREE with nuance] R1-W6**: 同意 CoNLL control 论证弱——task easiness 是 confound。但 Appendix D 另两个论证较强：LP shift 仅 0.001 nats/token (2.68% of median range)，且 constant prefix cancellation 基于数学推理。thinking token 问题总体证据充分，仅 CoNLL control 这一个论证弱。\n\n### 小问题\n\n**[AGREE] R1-Minor-1**: Table 2 NER 2-seed vs Table 7 QE 3-seed 差异未解释。\n**[AGREE] R1-Minor-2**: Figure 1 caption 不适用于 LP（per-sample signal）。\n**[REBUT] R1-Minor-3**: 检查 tex 源码，\\citet 用于句中主语、\\cite 用于括号引用，符合 natbib 标准。\n\n### 缺失引用\n\n**[REBUT] R1-Missing-1**: Huang et al. (2024) 讨论 self-correction（iterative修改），非 self-consistency（one-shot多采样比较），paradigm 不同，关联有限。\n**[AGREE] R1-Missing-2**: Fernandes et al. (2022) Quality-Aware Decoding 直接相关，将 QE 与 MBR 结合用 learned estimator rerank，与本文 \"trained verifiers\" 建议高度相关。\n\n### 总结\nR1 审稿质量高。我们在 RE 覆盖不足（R1-N1 = 我的 N2）、scale 局限（R1-W1 = 我的 W4）、greedy 命名（R1-W3 = 我的 minor）上达成共识。主要分歧在 N3（我认为 compression 本身 intrinsic 有证据，selection outcome 变化是另一回事）和 W5（filtering 差异是 dataset 特征非 confound）。ε circularity（R1-N2）是我未识别的新问题，同意其对辅助分析的影响，但主结论不受影响。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe47cf9c-ac9c-4ccf-976b-73ce528ddbe7",
  "isSidechain": false,
  "requestId": "req_011Cb5cZEHgVRAQkgNVeoNAg",
  "type": "assistant",
  "uuid": "55fa9e3e-4603-450a-a664-9aeda6bdbaa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XngSyXqCfP6PsnzYqZiE9w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4596,
      "cache_read_input_tokens": 93899,
      "output_tokens": 4949,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4596,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4949,
          "cache_read_input_tokens": 93899,
          "cache_creation_input_tokens": 4596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4596
          },
          "type": "message"
        }
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

_source line 127 · 2026-05-16T04:27:59.294Z_

<details><summary>↩ Tool result · `toolu_01WNrzYNBeZF2hWuJ9rsZHzs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55fa9e3e-4603-450a-a664-9aeda6bdbaa9",
  "isSidechain": false,
  "promptId": "972e434d-f261-4952-9bd8-d6687c8bbc36",
  "type": "user",
  "uuid": "c765725b-0885-40d3-a22e-45070a67fe77",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "55fa9e3e-4603-450a-a664-9aeda6bdbaa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "e427ec35-e53e-4958-bb7f-c7a35811281b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
