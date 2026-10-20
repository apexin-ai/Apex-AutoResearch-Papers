# Research conversation: [Round 1 审稿请求]: 你负责审查**方法严谨性、实验设计和统计有效性**。 ## 论文信息 - **标题**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposur

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 3
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-3/db89f3d0-eddf-4030-bb40-5b19b86066c8.jsonl`
- **Structured JSON:** [`97d6aaa7be11a5cb2fc8.json`](../../sessions/97/97d6aaa7be11a5cb2fc8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T15:51:58.286Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T15:51:58.286Z",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "content": "[Round 1 审稿请求]:\n你负责审查**方法严谨性、实验设计和统计有效性**。\n\n## 论文信息\n- **标题**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\n- **目标 venue**: EMNLP 2026（ARR May cycle）\n- **Deadline**: 2026-05-25\n- **格式**: ACL style long paper（8 页正文 + unlimited references + Limitations section 不计页数）\n- **匿名规则**: Double-blind\n- **论文路径**: projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex\n  - 分文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex\n  - 引用: references.bib\n\n## 你的审查侧重\n\n重点评估以下方面：\n\n1. **实验设计合理性**\n   - 7 个 Stage-1 变体的 ablation 是否充分隔离了目标因素？是否存在未控制的 confound？\n   - 训练数据 250+250 对话、OOD 数据 80-118 对话的规模是否足以支撑所宣称的结论？\n   - 3-seed 评估是否足够？哪些结论需要更多 seed？\n   - Cross-encoder validation（RoBERTa）的设计是否充分？\n\n2. **统计有效性**\n   - 报告的 mean±std 是否有 significance test 支撑？\n   - McNemar test 的使用是否恰当？样本量是否足够？\n   - Perturbation analysis 中的 three-layer pattern 的统计基础是否充分？\n   - 置信区间是否被报告？效应量是否有意义？\n\n3. **方法设计**\n   - BiGRU + frozen encoder 的 two-stage 设计是否合理？为什么不 end-to-end？\n   - Stage-1 七个变体之间是否真正公平比较（相同数据、相同超参数、相同 Stage-2）？\n   - Mean pooling vs BiGRU 的对比是否充分？\n   - 策略标注质量（Cohen's κ=0.78, n=50）是否足够？\n\n4. **Baseline 充分性**\n   - 是否缺少关键 baseline？（如 DeepContext、BIID、G-Guard 的直接对比）\n   - TF-IDF LR 强表现（0.944）对核心 claim 的冲击有多大？\n   - LLM-as-judge baseline 的设置是否公平？\n\n5. **可复现性**\n   - 超参数、数据生成流程、标注 prompt 是否完整披露？\n   - 代码/数据是否承诺发布？\n\n请按以下格式输出审稿意见：\n- **Summary**: 2-3 句论文概述\n- **Strengths** [S1, S2, ...]: 优点\n- **Weaknesses** [W1, W2, ...]: 缺点（标注 severity: critical/major/minor）\n- **Questions** [Q1, Q2, ...]: 需作者澄清的问题\n- **Missing References**: 遗漏的重要引用\n- **Overall Assessment**: 评分 + 置信度"
}
```

---

### Runtime record

_source line 2 · 2026-05-18T15:51:58.290Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T15:51:58.290Z",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

## Round 1

54 recorded events

### User

_source line 3 · 2026-05-18T15:51:58.326Z_

[Round 1 审稿请求]:
你负责审查**方法严谨性、实验设计和统计有效性**。

## 论文信息
- **标题**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap
- **目标 venue**: EMNLP 2026（ARR May cycle）
- **Deadline**: 2026-05-25
- **格式**: ACL style long paper（8 页正文 + unlimited references + Limitations section 不计页数）
- **匿名规则**: Double-blind
- **论文路径**: projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex
  - 分文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex
  - 引用: references.bib

## 你的审查侧重

重点评估以下方面：

1. **实验设计合理性**
   - 7 个 Stage-1 变体的 ablation 是否充分隔离了目标因素？是否存在未控制的 confound？
   - 训练数据 250+250 对话、OOD 数据 80-118 对话的规模是否足以支撑所宣称的结论？
   - 3-seed 评估是否足够？哪些结论需要更多 seed？
   - Cross-encoder validation（RoBERTa）的设计是否充分？

2. **统计有效性**
   - 报告的 mean±std 是否有 significance test 支撑？
   - McNemar test 的使用是否恰当？样本量是否足够？
   - Perturbation analysis 中的 three-layer pattern 的统计基础是否充分？
   - 置信区间是否被报告？效应量是否有意义？

3. **方法设计**
   - BiGRU + frozen encoder 的 two-stage 设计是否合理？为什么不 end-to-end？
   - Stage-1 七个变体之间是否真正公平比较（相同数据、相同超参数、相同 Stage-2）？
   - Mean pooling vs BiGRU 的对比是否充分？
   - 策略标注质量（Cohen's κ=0.78, n=50）是否足够？

4. **Baseline 充分性**
   - 是否缺少关键 baseline？（如 DeepContext、BIID、G-Guard 的直接对比）
   - TF-IDF LR 强表现（0.944）对核心 claim 的冲击有多大？
   - LLM-as-judge baseline 的设置是否公平？

5. **可复现性**
   - 超参数、数据生成流程、标注 prompt 是否完整披露？
   - 代码/数据是否承诺发布？

请按以下格式输出审稿意见：
- **Summary**: 2-3 句论文概述
- **Strengths** [S1, S2, ...]: 优点
- **Weaknesses** [W1, W2, ...]: 缺点（标注 severity: critical/major/minor）
- **Questions** [Q1, Q2, ...]: 需作者澄清的问题
- **Missing References**: 遗漏的重要引用
- **Overall Assessment**: 评分 + 置信度

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f969e597-50af-4667-a32a-e352289d26c2",
  "type": "user",
  "uuid": "511d1642-adae-4c5a-a9fe-93dead867d39",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T15:51:58.325Z_

```json
{
  "parentUuid": "511d1642-adae-4c5a-a9fe-93dead867d39",
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
  "uuid": "4c7837c2-ef0c-4991-81ac-a1bb6ed2a10c",
  "timestamp": "2026-05-18T15:51:58.325Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T15:51:58.325Z_

```json
{
  "parentUuid": "4c7837c2-ef0c-4991-81ac-a1bb6ed2a10c",
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
  "uuid": "bd32e017-33df-4780-ad1f-a9a8a469a59e",
  "timestamp": "2026-05-18T15:51:58.325Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-18T15:51:58.325Z_

```json
{
  "parentUuid": "bd32e017-33df-4780-ad1f-a9a8a469a59e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3fef9709-6d83-41fc-968e-20a29592db51",
  "timestamp": "2026-05-18T15:51:58.325Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
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
  "aiTitle": "Review multi-turn jailbreak detection paper methodology",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

### Assistant

_source line 8 · 2026-05-18T15:52:03.028Z_

<details><summary>Logged reasoning block</summary>

```text
The user (Review Director) is asking me to perform Round 1 review of a paper as Reviewer 1, focusing on methodological rigor, experimental design, and statistical validity. Let me follow the instructions:

1. First, I need to do Step 0: search for EMNLP 2026 / ACL ARR reviewer guidelines
2. Read the paper thoroughly
3. Produce a structured review

Let me start by reading the paper and searching for reviewer guidelines in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fef9709-6d83-41fc-968e-20a29592db51",
  "isSidechain": false,
  "requestId": "req_011CbAJU3GgQwSwmPBTxm1oL",
  "type": "assistant",
  "uuid": "8ed7aceb-16af-4c97-9b40-4a0c81a81409",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErQmts9ruHNDUaHcqidwBZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15237,
      "cache_read_input_tokens": 11841,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15237,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15237
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-18T15:52:04.043Z_

我将开始审稿流程：先搜索 ACL ARR reviewer guidelines，同时阅读论文全文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ed7aceb-16af-4c97-9b40-4a0c81a81409",
  "isSidechain": false,
  "requestId": "req_011CbAJU3GgQwSwmPBTxm1oL",
  "type": "assistant",
  "uuid": "54c367de-b4b9-48dd-ba08-8aa7f733423b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErQmts9ruHNDUaHcqidwBZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15237,
      "cache_read_input_tokens": 11841,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15237,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15237
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-18T15:52:05.020Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011m4nnAzV3v9JPU8RrJSUHU`</summary>

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
  "parentUuid": "54c367de-b4b9-48dd-ba08-8aa7f733423b",
  "isSidechain": false,
  "requestId": "req_011CbAJU3GgQwSwmPBTxm1oL",
  "type": "assistant",
  "uuid": "4917a5d7-4ae7-4c84-986e-c1dc24af489d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErQmts9ruHNDUaHcqidwBZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15237,
      "cache_read_input_tokens": 11841,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15237,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15237
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-18T15:52:05.026Z_

<details><summary>↩ Tool result · `toolu_011m4nnAzV3v9JPU8RrJSUHU`</summary>

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
  "parentUuid": "4917a5d7-4ae7-4c84-986e-c1dc24af489d",
  "isSidechain": false,
  "promptId": "f969e597-50af-4667-a32a-e352289d26c2",
  "type": "user",
  "uuid": "ce16877f-5361-4997-9ac5-5e7c84483ee3",
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
  "sourceToolAssistantUUID": "4917a5d7-4ae7-4c84-986e-c1dc24af489d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-18T15:52:07.663Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for ACL ARR reviewer guidelines and read the paper in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce16877f-5361-4997-9ac5-5e7c84483ee3",
  "isSidechain": false,
  "requestId": "req_011CbAJUY9ka2cB8DRj8JHCn",
  "type": "assistant",
  "uuid": "0ed14f1b-e96e-47b6-96c5-83ceb507c2f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGqj74KNyWEbdeCdWMUZaz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 27078,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2278,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 330,
          "cache_read_input_tokens": 27078,
          "cache_creation_input_tokens": 2278,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2278
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-18T15:52:08.167Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EEcukpTtX9HtphfwRfeEEp`</summary>

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
  "parentUuid": "0ed14f1b-e96e-47b6-96c5-83ceb507c2f7",
  "isSidechain": false,
  "requestId": "req_011CbAJUY9ka2cB8DRj8JHCn",
  "type": "assistant",
  "uuid": "79d9417a-979d-4468-b056-961749034080",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGqj74KNyWEbdeCdWMUZaz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 27078,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2278,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 330,
          "cache_read_input_tokens": 27078,
          "cache_creation_input_tokens": 2278,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2278
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-18T15:52:09.660Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Mt38EGMdYzTi766Mx4UTGz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79d9417a-979d-4468-b056-961749034080",
  "isSidechain": false,
  "requestId": "req_011CbAJUY9ka2cB8DRj8JHCn",
  "type": "assistant",
  "uuid": "4bff903b-3315-47f0-9e6e-8035ce5028fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGqj74KNyWEbdeCdWMUZaz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 27078,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2278,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 330,
          "cache_read_input_tokens": 27078,
          "cache_creation_input_tokens": 2278,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2278
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-18T15:52:10.407Z_

<details><summary>↩ Tool result · `toolu_01QXbjvJMYd8zNqdAagnKNQq`</summary>

```text
1	% introduction.tex — expanded for 8-page target
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Multi-turn jailbreak attacks pose a qualitatively different threat to large language model (LLM) safety than their single-turn counterparts. Attacks such as Crescendo~\citep{russinovich2024crescendo}, Foot-in-the-Door (FITD)~\citep{fitd2024}, and Deceptive Delight~\citep{deceptivedelight2024} distribute adversarial intent across individually benign turns through rapport building, logical reframing, and incremental escalation. Persuasion is the common mechanism: \citet{zeng2024pap} catalogue 40 persuasion techniques across jailbreak families, and \citet{hagendorff2026reasoning} find identifiable strategies in 97\% of successful attacks. Individual attack turns occupy the same embedding region as benign text~\citep{bullwinkel2025repeng}, rendering per-turn safety filters fundamentally blind.
7	
8	Production classifiers such as Llama Guard~\citep{inan2023llamaguard}, WildGuard~\citep{han2024wildguard}, and ShieldGemma~\citep{zeng2024shieldgemma} operate on individual turns and cannot model manipulation trajectories across exchanges. Recent multi-turn defenses have begun to address conversation-level structure: DeepContext~\citep{deepcontext2026} combines fine-tuned BERT with a multi-layer GRU, BIID~\citep{tong2025biid} infers turn-level intentions, and G-Guard~\citep{gguard2025} applies graph neural networks. These systems achieve reasonable in-distribution performance but are evaluated on single attack families and do not assess cross-dataset OOD transfer. None systematically analyze \emph{why} some representations generalize while others fail. The open question is: \emph{what representation properties enable cross-attack generalization?}
9	
10	A vanilla DeBERTa encoder~\citep{he2021deberta} with temporal aggregation collapses from F1\,=\,1.000 on in-distribution data to F1\,=\,0.312$\pm$0.026 on out-of-distribution (OOD) Deceptive Delight, worsening with more turns (0.628 at turn~1 to 0.312 at full conversation). LLM-as-judge approaches fare no better: GPT-5.5 achieves F1 of only 0.191--0.449 on in-distribution detection with 30--47\% unparseable responses (Appendix~\ref{sec:llm_judge}). Content-level reasoning is insufficient for this task.
11	
12	We built \textbf{DisPeD} (Discourse-level Persuasion Detection), a two-stage framework with seven controlled Stage~1 variants that systematically decompose the mechanism: 9-class persuasion strategy classification, binary classification, scrambled labels, MLM only, topic classification, Wikipedia MLM, and vanilla control (Section~\ref{sec:method}). Each variant isolates a specific factor (domain exposure, classification supervision, label quality, label granularity, or domain specificity) while holding all other components constant.
13	
14	Through this systematic ablation on DeBERTa-v3, we find that domain exposure via continued pretraining bridges $\sim$60 percentage points (pp) of the OOD gap (vanilla 0.31$\pm$0.03 $\to$ MLM 0.91$\pm$0.12), with strong early detection on unseen Deceptive Delight (mean F1\,$\geq$\,0.97 at $K \leq 5$). Classification supervision provides complementary stability: the 9-class model achieves F1\,=\,0.997$\pm$0.005 with near-zero variance at full conversation length. Cross-encoder validation on RoBERTa~\citep{liu2019roberta} shows that domain adaptation is universally beneficial: RoBERTa vanilla achieves F1\,=\,0.981 on Deceptive Delight but collapses to 0.466$\pm$0.163 on structurally distinct ActorAttack~\citep{ren2024actorattack}, while classification-supervised variants maintain F1\,$\geq$\,0.93 on both. Encoder pretraining method determines the difficulty threshold at which adaptation becomes critical: DeBERTa-v3's replaced token detection (RTD)~\citep{he2021deberta} requires adaptation even for simple attacks, while RoBERTa's standard MLM pretraining tolerates simple attacks but fails on structurally complex ones. Across both encoders, classification supervision reduces cross-seed variance to 0.005--0.046.
15	
16	Our contributions on this preliminary study of synthetic multi-turn jailbreak conversations:
17	\begin{itemize}[leftmargin=*, itemsep=2pt, topsep=4pt]
18	  \item \textbf{Systematic decomposition.} Seven controlled DeBERTa-v3 variants identify continued pretraining as the primary mechanism for cross-attack generalization on this encoder ($\sim$60\,pp OOD gap bridged by MLM alone). Misaligned supervision (topic classification) actively destabilizes representations.
19	
20	  \item \textbf{Cross-encoder validation.} Domain adaptation is universally beneficial: RoBERTa vanilla achieves F1\,=\,0.981 on Deceptive Delight but collapses to 0.466 on ActorAttack. Encoder pretraining method determines the difficulty threshold at which adaptation becomes critical (Section~\ref{sec:cross_encoder}).
21	
22	  \item \textbf{Cross-seed stability.} Classification supervision reduces cross-seed variance 4--20$\times$ compared to MLM-only pretraining (9-class std\,=\,0.005 on DD, 0.026 on ActorAttack vs.\ MLM std\,=\,0.115, 0.080), consistent across both OOD families. The 9-class taxonomy additionally provides interpretable characterization of known attack families, though strategy predictions do not transfer to unseen attacks (Section~\ref{sec:strategy}).
23	
24	\end{itemize}
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54d2fbca-e8a7-42c2-9bd4-37650a297f9e",
  "isSidechain": false,
  "promptId": "f969e597-50af-4667-a32a-e352289d26c2",
  "type": "user",
  "uuid": "4fde0fc2-54ae-4b81-a96d-10274f04c741",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex",
      "content": "% introduction.tex — expanded for 8-page target\n\n\\section{Introduction}\n\\label{sec:introduction}\n\nMulti-turn jailbreak attacks pose a qualitatively different threat to large language model (LLM) safety than their single-turn counterparts. Attacks such as Crescendo~\\citep{russinovich2024crescendo}, Foot-in-the-Door (FITD)~\\citep{fitd2024}, and Deceptive Delight~\\citep{deceptivedelight2024} distribute adversarial intent across individually benign turns through rapport building, logical reframing, and incremental escalation. Persuasion is the common mechanism: \\citet{zeng2024pap} catalogue 40 persuasion techniques across jailbreak families, and \\citet{hagendorff2026reasoning} find identifiable strategies in 97\\% of successful attacks. Individual attack turns occupy the same embedding region as benign text~\\citep{bullwinkel2025repeng}, rendering per-turn safety filters fundamentally blind.\n\nProduction classifiers such as Llama Guard~\\citep{inan2023llamaguard}, WildGuard~\\citep{han2024wildguard}, and ShieldGemma~\\citep{zeng2024shieldgemma} operate on individual turns and cannot model manipulation trajectories across exchanges. Recent multi-turn defenses have begun to address conversation-level structure: DeepContext~\\citep{deepcontext2026} combines fine-tuned BERT with a multi-layer GRU, BIID~\\citep{tong2025biid} infers turn-level intentions, and G-Guard~\\citep{gguard2025} applies graph neural networks. These systems achieve reasonable in-distribution performance but are evaluated on single attack families and do not assess cross-dataset OOD transfer. None systematically analyze \\emph{why} some representations generalize while others fail. The open question is: \\emph{what representation properties enable cross-attack generalization?}\n\nA vanilla DeBERTa encoder~\\citep{he2021deberta} with temporal aggregation collapses from F1\\,=\\,1.000 on in-distribution data to F1\\,=\\,0.312$\\pm$0.026 on out-of-distribution (OOD) Deceptive Delight, worsening with more turns (0.628 at turn~1 to 0.312 at full conversation). LLM-as-judge approaches fare no better: GPT-5.5 achieves F1 of only 0.191--0.449 on in-distribution detection with 30--47\\% unparseable responses (Appendix~\\ref{sec:llm_judge}). Content-level reasoning is insufficient for this task.\n\nWe built \\textbf{DisPeD} (Discourse-level Persuasion Detection), a two-stage framework with seven controlled Stage~1 variants that systematically decompose the mechanism: 9-class persuasion strategy classification, binary classification, scrambled labels, MLM only, topic classification, Wikipedia MLM, and vanilla control (Section~\\ref{sec:method}). Each variant isolates a specific factor (domain exposure, classification supervision, label quality, label granularity, or domain specificity) while holding all other components constant.\n\nThrough this systematic ablation on DeBERTa-v3, we find that domain exposure via continued pretraining bridges $\\sim$60 percentage points (pp) of the OOD gap (vanilla 0.31$\\pm$0.03 $\\to$ MLM 0.91$\\pm$0.12), with strong early detection on unseen Deceptive Delight (mean F1\\,$\\geq$\\,0.97 at $K \\leq 5$). Classification supervision provides complementary stability: the 9-class model achieves F1\\,=\\,0.997$\\pm$0.005 with near-zero variance at full conversation length. Cross-encoder validation on RoBERTa~\\citep{liu2019roberta} shows that domain adaptation is universally beneficial: RoBERTa vanilla achieves F1\\,=\\,0.981 on Deceptive Delight but collapses to 0.466$\\pm$0.163 on structurally distinct ActorAttack~\\citep{ren2024actorattack}, while classification-supervised variants maintain F1\\,$\\geq$\\,0.93 on both. Encoder pretraining method determines the difficulty threshold at which adaptation becomes critical: DeBERTa-v3's replaced token detection (RTD)~\\citep{he2021deberta} requires adaptation even for simple attacks, while RoBERTa's standard MLM pretraining tolerates simple attacks but fails on structurally complex ones. Across both encoders, classification supervision reduces cross-seed variance to 0.005--0.046.\n\nOur contributions on this preliminary study of synthetic multi-turn jailbreak conversations:\n\\begin{itemize}[leftmargin=*, itemsep=2pt, topsep=4pt]\n  \\item \\textbf{Systematic decomposition.} Seven controlled DeBERTa-v3 variants identify continued pretraining as the primary mechanism for cross-attack generalization on this encoder ($\\sim$60\\,pp OOD gap bridged by MLM alone). Misaligned supervision (topic classification) actively destabilizes representations.\n\n  \\item \\textbf{Cross-encoder validation.} Domain adaptation is universally beneficial: RoBERTa vanilla achieves F1\\,=\\,0.981 on Deceptive Delight but collapses to 0.466 on ActorAttack. Encoder pretraining method determines the difficulty threshold at which adaptation becomes critical (Section~\\ref{sec:cross_encoder}).\n\n  \\item \\textbf{Cross-seed stability.} Classification supervision reduces cross-seed variance 4--20$\\times$ compared to MLM-only pretraining (9-class std\\,=\\,0.005 on DD, 0.026 on ActorAttack vs.\\ MLM std\\,=\\,0.115, 0.080), consistent across both OOD families. The 9-class taxonomy additionally provides interpretable characterization of known attack families, though strategy predictions do not transfer to unseen attacks (Section~\\ref{sec:strategy}).\n\n\\end{itemize}\n",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  },
  "sourceToolAssistantUUID": "54d2fbca-e8a7-42c2-9bd4-37650a297f9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T15:52:09.678Z_

<details><summary>↩ Tool result · `toolu_01Mt38EGMdYzTi766Mx4UTGz`</summary>

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
10	\usepackage{graphicx}
11	\graphicspath{{../../}}
12	\usepackage{amsmath}
13	\usepackage{booktabs}
14	\usepackage{enumitem}
15	\usepackage{amssymb}
16	\usepackage{multirow}
17	
18	\title{What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	
27	\input{introduction}
28	
29	\input{related_work}
30	
31	\input{method}
32	
33	\input{experiments}
34	
35	\input{conclusion}
36	
37	\bibliography{references}
38	
39	\input{appendix}
40	
41	\end{document}
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bff903b-3315-47f0-9e6e-8035ce5028fa",
  "isSidechain": false,
  "promptId": "f969e597-50af-4667-a32a-e352289d26c2",
  "type": "user",
  "uuid": "d286caf8-26a5-4fad-a705-cc1080fd4d05",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\graphicspath{{../../}}\n\\usepackage{amsmath}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\n\\title{What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 42,
      "startLine": 1,
      "totalLines": 42
    }
  },
  "sourceToolAssistantUUID": "4bff903b-3315-47f0-9e6e-8035ce5028fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T15:52:10.133Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FNKWhdQryJtmLLMK3MDAeQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d286caf8-26a5-4fad-a705-cc1080fd4d05",
  "isSidechain": false,
  "requestId": "req_011CbAJUY9ka2cB8DRj8JHCn",
  "type": "assistant",
  "uuid": "34dc0a4b-58c4-4f2a-be1f-cf9af4d73639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGqj74KNyWEbdeCdWMUZaz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 27078,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2278,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 330,
          "cache_read_input_tokens": 27078,
          "cache_creation_input_tokens": 2278,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2278
          },
          "type": "message"
        }
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

_source line 18 · 2026-05-18T15:52:10.138Z_

<details><summary>↩ Tool result · `toolu_01FNKWhdQryJtmLLMK3MDAeQ`</summary>

```text
1	% abstract.tex — cross-encoder revision
2	\begin{abstract}
3	Multi-turn jailbreak attacks distribute adversarial intent across seemingly benign conversational turns, evading per-turn safety filters.
4	We present preliminary findings from a systematic ablation on two encoder architectures that decomposes what enables cross-attack generalization in multi-turn jailbreak detection.
5	On DeBERTa-v3, continued pretraining is the primary mechanism: masked language modeling without labels bridges $\sim$60 percentage points (pp) of the out-of-distribution (OOD) gap (vanilla F1\,=\,0.31$\pm$0.03 $\to$ 0.91$\pm$0.12 on unseen attack types).
6	Cross-encoder validation on RoBERTa shows that domain adaptation is universally beneficial: RoBERTa vanilla achieves F1\,=\,0.981 on structurally simple Deceptive Delight but collapses to 0.466 on multi-persona ActorAttack, while classification-supervised variants maintain F1\,$\geq$\,0.93 on both.
7	Across both encoders, classification supervision provides cross-seed stability (variance reduced 4--20$\times$ vs.\ MLM-only, consistent across both OOD families). Domain adaptation's detection advantage persists under adversarial paraphrasing (McNemar $p < 0.001$), though absolute perturbation robustness varies by attack family.
8	These results on synthetic conversations from four attack families suggest that domain adaptation universally improves cross-attack generalization, with encoder pretraining method determining the difficulty threshold at which adaptation becomes critical; validation on larger, human-generated datasets is needed.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34dc0a4b-58c4-4f2a-be1f-cf9af4d73639",
  "isSidechain": false,
  "promptId": "f969e597-50af-4667-a32a-e352289d26c2",
  "type": "user",
  "uuid": "336659ec-afb4-40e2-84c2-8d5ffa7ca576",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex",
      "content": "% abstract.tex — cross-encoder revision\n\\begin{abstract}\nMulti-turn jailbreak attacks distribute adversarial intent across seemingly benign conversational turns, evading per-turn safety filters.\nWe present preliminary findings from a systematic ablation on two encoder architectures that decomposes what enables cross-attack generalization in multi-turn jailbreak detection.\nOn DeBERTa-v3, continued pretraining is the primary mechanism: masked language modeling without labels bridges $\\sim$60 percentage points (pp) of the out-of-distribution (OOD) gap (vanilla F1\\,=\\,0.31$\\pm$0.03 $\\to$ 0.91$\\pm$0.12 on unseen attack types).\nCross-encoder validation on RoBERTa shows that domain adaptation is universally beneficial: RoBERTa vanilla achieves F1\\,=\\,0.981 on structurally simple Deceptive Delight but collapses to 0.466 on multi-persona ActorAttack, while classification-supervised variants maintain F1\\,$\\geq$\\,0.93 on both.\nAcross both encoders, classification supervision provides cross-seed stability (variance reduced 4--20$\\times$ vs.\\ MLM-only, consistent across both OOD families). Domain adaptation's detection advantage persists under adversarial paraphrasing (McNemar $p < 0.001$), though absolute perturbation robustness varies by attack family.\nThese results on synthetic conversations from four attack families suggest that domain adaptation universally improves cross-attack generalization, with encoder pretraining method determining the difficulty threshold at which adaptation becomes critical; validation on larger, human-generated datasets is needed.\n\\end{abstract}\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "34dc0a4b-58c4-4f2a-be1f-cf9af4d73639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T15:52:10.396Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QXbjvJMYd8zNqdAagnKNQq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "336659ec-afb4-40e2-84c2-8d5ffa7ca576",
  "isSidechain": false,
  "requestId": "req_011CbAJUY9ka2cB8DRj8JHCn",
  "type": "assistant",
  "uuid": "54d2fbca-e8a7-42c2-9bd4-37650a297f9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGqj74KNyWEbdeCdWMUZaz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 27078,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2278,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 330,
          "cache_read_input_tokens": 27078,
          "cache_creation_input_tokens": 2278,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2278
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: 你负责审查**方法严谨性、实验设计和统计有效性**。  ## 论文信息 - **标题**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap - **目标 venue**: EMNLP 2026（ARR May cycle） - **De…",
  "leafUuid": "4fde0fc2-54ae-4b81-a96d-10274f04c741",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multi-turn jailbreak detection paper methodology",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

### Tool result

_source line 22 · 2026-05-18T15:52:16.108Z_

<details><summary>↩ Tool result · `toolu_01EEcukpTtX9HtphfwRfeEEp`</summary>

```text
Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the web search results, here's information about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Recommendation Scale

The metareview score options include: 5 = Consider for Award: papers that could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers). Additional recommendation levels include:

- 2 = Resubmit next cycle: the paper needs substantial revisions that can be completed by the next ARR cycle
- 1.5 = Resubmit after next cycle: the paper needs substantial revisions that cannot be completed by the next ARR cycle
- 1 = Do not resubmit: the paper has to be fully redone, or it is not relevant to the *ACL community

## Quality Standards

All papers recommended for Findings or main conference are expected to be sound and reproducible. Outstanding papers should be either fascinating, controversial, surprising, impressive, or potentially field-changing.

## Review Form Questions

Reviewers are asked whether authors have adequately discussed the limitations and potential positive and negative societal impacts of their work, and to include constructive suggestions for improvement if not. Reviewers also assess whether there is enough information in the paper for readers to reproduce the main results or build upon the work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79d9417a-979d-4468-b056-961749034080",
  "isSidechain": false,
  "promptId": "f969e597-50af-4667-a32a-e352289d26c2",
  "type": "user",
  "uuid": "9211305b-af48-4775-947f-aaf0a89f036d",
  "toolUseResult": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_0161mTuMPcHJUzMfZWZoaLzS",
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
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "https://aclrollingreview.org/"
          },
          {
            "title": "Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewform"
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
      "Based on the web search results, here's information about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:\n\n## Reviewer Scoring Criteria\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.\n\n## Overall Recommendation Scale\n\nThe metareview score options include: 5 = Consider for Award: papers that could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers). Additional recommendation levels include:\n\n- 2 = Resubmit next cycle: the paper needs substantial revisions that can be completed by the next ARR cycle\n- 1.5 = Resubmit after next cycle: the paper needs substantial revisions that cannot be completed by the next ARR cycle\n- 1 = Do not resubmit: the paper has to be fully redone, or it is not relevant to the *ACL community\n\n## Quality Standards\n\nAll papers recommended for Findings or main conference are expected to be sound and reproducible. Outstanding papers should be either fascinating, controversial, surprising, impressive, or potentially field-changing.\n\n## Review Form Questions\n\nReviewers are asked whether authors have adequately discussed the limitations and potential positive and negative societal impacts of their work, and to include constructive suggestions for improvement if not. Reviewers also assess whether there is enough information in the paper for readers to reproduce the main results or build upon the work."
    ],
    "durationSeconds": 7.931746378
  },
  "sourceToolAssistantUUID": "79d9417a-979d-4468-b056-961749034080",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T15:52:19.818Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014bkbT8wyThSY3oiGJXyK4n`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. I need the exact scoring criteria for soundness, excitement, overall assessment, and any other dimensions reviewers must fill in."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9211305b-af48-4775-947f-aaf0a89f036d",
  "isSidechain": false,
  "requestId": "req_011CbAJVMMePDfy9LwEBCGmu",
  "type": "assistant",
  "uuid": "742292dc-a9f4-49a0-8f16-79dcff3f4a50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NvGQQ3Q6Dpti5bW2MiTopp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2406,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 29356,
      "output_tokens": 351,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1193,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2406,
          "output_tokens": 351,
          "cache_read_input_tokens": 29356,
          "cache_creation_input_tokens": 1193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1193
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-18T15:52:20.143Z_

<details open><summary>🔧 Tool call — Read · `toolu_0181njtyhDkpv9eQeH798aAD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "742292dc-a9f4-49a0-8f16-79dcff3f4a50",
  "isSidechain": false,
  "requestId": "req_011CbAJVMMePDfy9LwEBCGmu",
  "type": "assistant",
  "uuid": "2cfbd405-db5c-4edd-aa73-c3ba52e2ff69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NvGQQ3Q6Dpti5bW2MiTopp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2406,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 29356,
      "output_tokens": 351,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1193,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2406,
          "output_tokens": 351,
          "cache_read_input_tokens": 29356,
          "cache_creation_input_tokens": 1193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1193
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-18T15:52:20.150Z_

<details><summary>↩ Tool result · `toolu_0181njtyhDkpv9eQeH798aAD`</summary>

```text
1	% method.tex — D024 compressed
2	
3	\section{Method}
4	\label{sec:method}
5	
6	DisPeD is a two-stage framework for multi-turn jailbreak detection. Stage~1 adapts a turn-level encoder through continued training on jailbreak conversation text. Stage~2 aggregates turn representations for conversation-level binary classification. To systematically identify what enables cross-attack generalization, we design seven Stage-1 variants that decompose the contributions of domain exposure, classification supervision, label quality, label granularity, and domain specificity. Figure~\ref{fig:architecture} illustrates the pipeline.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{figures/paper/fig1_architecture.pdf}
11	\caption{DisPeD architecture. Stage~1 adapts a DeBERTa encoder on jailbreak conversation text (seven variant objectives). Stage~2 aggregates frozen \texttt{[CLS]} embeddings via BiGRU for conversation-level jailbreak detection. Only user turns are processed.}
12	\label{fig:architecture}
13	\end{figure}
14	
15	\subsection{Problem Formulation}
16	
17	A conversation $C = \{u_1, a_1, \ldots, u_N, a_N\}$ alternates user turns $u_i$ and assistant responses $a_i$. Given a prefix of $K$ user turns, the model predicts $y \in \{0, 1\}$ (jailbreak vs.\ benign). We restrict input to user turns because adversarial intent resides in the attacker's messages. This formulation supports early detection from partial prefixes.
18	
19	\subsection{Stage 1: Turn-Level Encoder Adaptation}
20	\label{sec:stage1}
21	
22	Each user turn $u_i$ is encoded by DeBERTa-v3-base~\citep{he2021deberta}; the \texttt{[CLS]} embedding $h_i \in \mathbb{R}^d$ serves as the turn representation. Seven variants, summarized in Table~\ref{tab:variants}, share the same training data but differ in objective.
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\caption{Stage-1 encoder variants. All operate on the same training conversations except Wikipedia MLM (matched token count on Wikipedia text).}
28	\label{tab:variants}
29	\begin{tabular}{@{}p{1.6cm}p{2.2cm}p{2.8cm}@{}}
30	\toprule
31	\textbf{Variant} & \textbf{Objective} & \textbf{Tests whether\ldots} \\
32	\midrule
33	9-class & 9-class persuasion + binary intent & full model \\
34	Binary & binary persuasion + binary intent & granularity matters \\
35	Scrambled & random 9-class + binary intent & label correctness matters \\
36	MLM-only & 15\% token masking & supervision is necessary \\
37	Topic & 5-class topic classif. & any task suffices \\
38	Wiki MLM & 15\% masking on Wikipedia & domain specificity matters \\
39	Vanilla & no training & Stage-2 alone suffices \\
40	\bottomrule
41	\end{tabular}
42	\end{table}
43	
44	The \textbf{9-class} variant uses two classification heads: 9-class persuasion strategy classification ($L_{\text{strategy}}$) and binary jailbreak intent ($L_{\text{intent}}$), with combined loss $L = L_{\text{strategy}} + \alpha \cdot L_{\text{intent}}$ ($\alpha = 0.3$). The taxonomy comprises eight persuasion strategies (rapport building, authority appeal, emotional manipulation, logical reframing, role assignment, gradual escalation, obfuscation, direct request) plus a none category, grounded in PAP~\citep{zeng2024pap} and Cialdini's principles~\citep{cialdini2001influence}. Strategy annotations are produced by Qwen3-8B with structured prompting that includes definitions and examples for each category; inter-annotator agreement between model annotations and a human sample ($n$=50) yields Cohen's $\kappa$=0.78.
45	
46	The remaining classification variants test specific ablation hypotheses.
47	The \textbf{binary} variant collapses the 9-class taxonomy into persuasive vs.\ non-persuasive, testing whether label granularity matters for detection or robustness.
48	The \textbf{scrambled} variant assigns random permutations of the 9-class labels to turns, preserving the classification structure (cross-entropy loss, 9-class output space) while destroying label semantics; this isolates whether the classification objective itself provides representational benefits independent of label correctness.
49	The \textbf{MLM-only} variant applies 15\% masked language modeling on the same jailbreak conversation text without any classification head, testing whether unsupervised domain exposure suffices.
50	The \textbf{topic} variant trains a 5-class topic classifier (technology, health, finance, education, general) on the same conversations, testing whether \emph{any} classification task provides the same benefit or whether task alignment matters.
51	The \textbf{Wikipedia MLM} variant applies the same MLM objective to a token-matched sample of Wikipedia text, isolating the effect of domain-specific vs.\ general continued pretraining.
52	The \textbf{vanilla} baseline uses the pretrained DeBERTa-v3-base weights without any continued training, measuring what Stage~2 alone can achieve.
53	
54	\subsection{Stage 2: Conversation-Level Classification}
55	\label{sec:stage2}
56	
57	Turn embeddings $\{h_1, \ldots, h_K\}$ from the frozen Stage-1 encoder are aggregated by a bidirectional GRU ($d_{\text{hidden}}$=128): $\bar{h} = [\overrightarrow{h_K};\; \overleftarrow{h_1}] \in \mathbb{R}^{256}$.
58	A two-layer MLP ($256 \to 64 \to 2$, ReLU activation, dropout 0.3) maps $\bar{h}$ to $\hat{y} \in \{0, 1\}$.
59	The Stage-1 encoder is frozen during Stage~2 training; only the BiGRU and MLP parameters are updated.
60	This separation ensures that the seven Stage-1 variants produce comparable embeddings evaluated under identical downstream conditions.
61	A preliminary comparison suggests that mean pooling approaches BiGRU performance (Section~\ref{sec:decomposition}), though multi-seed validation is needed.
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2cfbd405-db5c-4edd-aa73-c3ba52e2ff69",
  "isSidechain": false,
  "promptId": "f969e597-50af-4667-a32a-e352289d26c2",
  "type": "user",
  "uuid": "28aa9e93-e0b0-496d-bbf3-248cce455e0a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex",
      "content": "% method.tex — D024 compressed\n\n\\section{Method}\n\\label{sec:method}\n\nDisPeD is a two-stage framework for multi-turn jailbreak detection. Stage~1 adapts a turn-level encoder through continued training on jailbreak conversation text. Stage~2 aggregates turn representations for conversation-level binary classification. To systematically identify what enables cross-attack generalization, we design seven Stage-1 variants that decompose the contributions of domain exposure, classification supervision, label quality, label granularity, and domain specificity. Figure~\\ref{fig:architecture} illustrates the pipeline.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig1_architecture.pdf}\n\\caption{DisPeD architecture. Stage~1 adapts a DeBERTa encoder on jailbreak conversation text (seven variant objectives). Stage~2 aggregates frozen \\texttt{[CLS]} embeddings via BiGRU for conversation-level jailbreak detection. Only user turns are processed.}\n\\label{fig:architecture}\n\\end{figure}\n\n\\subsection{Problem Formulation}\n\nA conversation $C = \\{u_1, a_1, \\ldots, u_N, a_N\\}$ alternates user turns $u_i$ and assistant responses $a_i$. Given a prefix of $K$ user turns, the model predicts $y \\in \\{0, 1\\}$ (jailbreak vs.\\ benign). We restrict input to user turns because adversarial intent resides in the attacker's messages. This formulation supports early detection from partial prefixes.\n\n\\subsection{Stage 1: Turn-Level Encoder Adaptation}\n\\label{sec:stage1}\n\nEach user turn $u_i$ is encoded by DeBERTa-v3-base~\\citep{he2021deberta}; the \\texttt{[CLS]} embedding $h_i \\in \\mathbb{R}^d$ serves as the turn representation. Seven variants, summarized in Table~\\ref{tab:variants}, share the same training data but differ in objective.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Stage-1 encoder variants. All operate on the same training conversations except Wikipedia MLM (matched token count on Wikipedia text).}\n\\label{tab:variants}\n\\begin{tabular}{@{}p{1.6cm}p{2.2cm}p{2.8cm}@{}}\n\\toprule\n\\textbf{Variant} & \\textbf{Objective} & \\textbf{Tests whether\\ldots} \\\\\n\\midrule\n9-class & 9-class persuasion + binary intent & full model \\\\\nBinary & binary persuasion + binary intent & granularity matters \\\\\nScrambled & random 9-class + binary intent & label correctness matters \\\\\nMLM-only & 15\\% token masking & supervision is necessary \\\\\nTopic & 5-class topic classif. & any task suffices \\\\\nWiki MLM & 15\\% masking on Wikipedia & domain specificity matters \\\\\nVanilla & no training & Stage-2 alone suffices \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe \\textbf{9-class} variant uses two classification heads: 9-class persuasion strategy classification ($L_{\\text{strategy}}$) and binary jailbreak intent ($L_{\\text{intent}}$), with combined loss $L = L_{\\text{strategy}} + \\alpha \\cdot L_{\\text{intent}}$ ($\\alpha = 0.3$). The taxonomy comprises eight persuasion strategies (rapport building, authority appeal, emotional manipulation, logical reframing, role assignment, gradual escalation, obfuscation, direct request) plus a none category, grounded in PAP~\\citep{zeng2024pap} and Cialdini's principles~\\citep{cialdini2001influence}. Strategy annotations are produced by Qwen3-8B with structured prompting that includes definitions and examples for each category; inter-annotator agreement between model annotations and a human sample ($n$=50) yields Cohen's $\\kappa$=0.78.\n\nThe remaining classification variants test specific ablation hypotheses.\nThe \\textbf{binary} variant collapses the 9-class taxonomy into persuasive vs.\\ non-persuasive, testing whether label granularity matters for detection or robustness.\nThe \\textbf{scrambled} variant assigns random permutations of the 9-class labels to turns, preserving the classification structure (cross-entropy loss, 9-class output space) while destroying label semantics; this isolates whether the classification objective itself provides representational benefits independent of label correctness.\nThe \\textbf{MLM-only} variant applies 15\\% masked language modeling on the same jailbreak conversation text without any classification head, testing whether unsupervised domain exposure suffices.\nThe \\textbf{topic} variant trains a 5-class topic classifier (technology, health, finance, education, general) on the same conversations, testing whether \\emph{any} classification task provides the same benefit or whether task alignment matters.\nThe \\textbf{Wikipedia MLM} variant applies the same MLM objective to a token-matched sample of Wikipedia text, isolating the effect of domain-specific vs.\\ general continued pretraining.\nThe \\textbf{vanilla} baseline uses the pretrained DeBERTa-v3-base weights without any continued training, measuring what Stage~2 alone can achieve.\n\n\\subsection{Stage 2: Conversation-Level Classification}\n\\label{sec:stage2}\n\nTurn embeddings $\\{h_1, \\ldots, h_K\\}$ from the frozen Stage-1 encoder are aggregated by a bidirectional GRU ($d_{\\text{hidden}}$=128): $\\bar{h} = [\\overrightarrow{h_K};\\; \\overleftarrow{h_1}] \\in \\mathbb{R}^{256}$.\nA two-layer MLP ($256 \\to 64 \\to 2$, ReLU activation, dropout 0.3) maps $\\bar{h}$ to $\\hat{y} \\in \\{0, 1\\}$.\nThe Stage-1 encoder is frozen during Stage~2 training; only the BiGRU and MLP parameters are updated.\nThis separation ensures that the seven Stage-1 variants produce comparable embeddings evaluated under identical downstream conditions.\nA preliminary comparison suggests that mean pooling approaches BiGRU performance (Section~\\ref{sec:decomposition}), though multi-seed validation is needed.\n",
      "numLines": 62,
      "startLine": 1,
      "totalLines": 62
    }
  },
  "sourceToolAssistantUUID": "2cfbd405-db5c-4edd-aa73-c3ba52e2ff69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T15:52:21.257Z_

<details><summary>↩ Tool result · `toolu_01VDXbn1oh3kQa9ZzyVKt4qJ`</summary>

```text
1	% related_work.tex — D024 compressed
2	
3	\section{Related Work}
4	\label{sec:related_work}
5	
6	\paragraph{Multi-turn jailbreak attacks.}
7	Multi-turn attacks distribute adversarial intent across individually benign turns. Crescendo~\citep{russinovich2024crescendo} implements gradual escalation, FITD~\citep{fitd2024} exploits commitment-consistency bias, Deceptive Delight~\citep{deceptivedelight2024} combines emotional manipulation with role assignment, ActorAttack~\citep{ren2024actorattack} uses multi-persona steering, and PAIR~\citep{chao2023pair} automates iterative refinement. \citet{wei2023jailbroken} provide a unifying taxonomy grounded in competing objectives and mismatched generalization. Across these families, a shared reliance on persuasion dynamics~\citep{zeng2024pap,hagendorff2026reasoning,li2024mhj} distinguishes them from token-level attacks such as GCG~\citep{zou2023gcg}.
8	
9	\paragraph{Multi-turn defenses.}
10	Existing defenses model conversation-level structure but do not decompose what enables cross-attack generalization. DeepContext~\citep{deepcontext2026} combines fine-tuned BERT with a 3-layer GRU (hidden=2048) and achieves F1 = 0.84 on in-distribution data; however, its evaluation is limited to a single attack family and does not assess cross-dataset OOD transfer. BIID~\citep{tong2025biid} infers turn-level intentions, G-Guard~\citep{gguard2025} applies GNN classification, and SafeDream~\citep{safedream2026} predicts unsafe continuations. None of these systems evaluate generalization across attack families or analyze the mechanism that enables it. DisPeD's vanilla baseline represents the class of pretrained-encoder-plus-RNN approaches \emph{without} domain adaptation; it is not a direct proxy for DeepContext, which differs in encoder fine-tuning, model capacity, and loss function. Our contribution is the systematic decomposition showing that domain exposure, not architectural choices, is the primary factor for cross-attack generalization.
11	
12	\paragraph{Production safety systems.}
13	Per-turn classifiers (Llama Guard~\citep{inan2023llamaguard,metallamaguard3_2024}, ShieldGemma~\citep{zeng2024shieldgemma}, WildGuard~\citep{han2024wildguard}, Constitutional Classifiers~\citep{anthropic2025constitutional}) cannot model manipulation trajectories spanning multiple turns. LLM-as-judge approaches also fail: GPT-5.5 achieves F1 = 0.191--0.449 with 30--47\% unparseable responses (Appendix~\ref{sec:llm_judge}). DisPeD complements these systems as a conversation-level detection layer.
14	
15	\paragraph{Discourse analysis and computational persuasion.}
16	RST~\citep{mann1988rst}, PDTB~\citep{prasad2008pdtb}, and dialogue act taxonomies~\citep{stolcke2000dialogueact} model pragmatic structure. Speech Act Theory~\citep{austin1962speechacts,searle1969speechacts} distinguishes locutionary from illocutionary acts; existing jailbreak detectors operate at the locutionary level. PAP~\citep{zeng2024pap} identifies 40 persuasion techniques grounded in Cialdini's principles~\citep{cialdini2001influence}, and \citet{hagendorff2026reasoning} find identifiable strategies in 97\% of successful attacks. Related fine-grained persuasion detection work in propaganda analysis~\citep{dasanmartino2019fine,dasanmartino2020semeval} has shown that technique-level classification can capture manipulative intent in news text; DisPeD applies a similar taxonomy to conversational jailbreaks. DisPeD's detection operates through continued training rather than persuasion classification; the taxonomy provides interpretable characterization of known attack families (Section~\ref{sec:strategy}).
17	
18	\paragraph{Domain-adaptive pretraining.}
19	ULMFiT~\citep{howard2018ulmfit} established pretrain-then-fine-tune; \citet{gururangan2020dontstop} showed that continued pretraining on domain text yields consistent gains across domains. STILTs~\citep{phang2018stilts} and multi-task learning~\citep{caruana1997multitask,liu2019mtdnn} use intermediate tasks. DisPeD's MLM control confirms that continued pretraining bridges $\sim$60\,pp of the OOD gap on DeBERTa-v3 (MLM F1 $\geq$ 0.97 at $K \leq 5$). However, domain adaptation is universally beneficial across encoder architectures: RoBERTa~\citep{liu2019roberta} vanilla achieves F1 = 0.981 on structurally simple Deceptive Delight but collapses to 0.466 on ActorAttack~\citep{ren2024actorattack}; encoder pretraining method determines the difficulty threshold at which adaptation becomes critical (Section~\ref{sec:cross_encoder}). Classification supervision reduces cross-seed variance to near-zero in both architectures.
20	
21	\paragraph{Dataset artifacts and adversarial robustness.}
22	Classifiers are susceptible to spurious correlations~\citep{gururangan2018artifacts,niven2019probing}, and adaptive adversaries can bypass safety classifiers~\citep{nasr2025attackermovessecond,andriushchenko2024adaptive}. Adversarial NLP attacks such as TextFooler~\citep{jin2020textfooler} and BERT-Attack~\citep{li2020bertattack} demonstrate that neural text classifiers are vulnerable to token-level perturbations. TF-IDF achieves F1 = 0.944 on our OOD evaluation; this reveals lexical separability in current datasets. Probing classifiers~\citep{conneau2018probing,hewitt2019structural} could help determine whether DisPeD's representations encode discourse-level structure beyond lexical cues; we leave this for future work. DisPeD's demonstrated advantage is robustness under adversarial paraphrasing (0\,pp degradation for classification-supervised models vs.\ $\sim$12\,pp for non-adapted models).
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e3acf10-50fd-4668-9fa6-5f14eefefb8d",
  "isSidechain": false,
  "promptId": "f969e597-50af-4667-a32a-e352289d26c2",
  "type": "user",
  "uuid": "feb24ade-f45a-4b3e-a259-9faf02079d96",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex",
      "content": "% related_work.tex — D024 compressed\n\n\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Multi-turn jailbreak attacks.}\nMulti-turn attacks distribute adversarial intent across individually benign turns. Crescendo~\\citep{russinovich2024crescendo} implements gradual escalation, FITD~\\citep{fitd2024} exploits commitment-consistency bias, Deceptive Delight~\\citep{deceptivedelight2024} combines emotional manipulation with role assignment, ActorAttack~\\citep{ren2024actorattack} uses multi-persona steering, and PAIR~\\citep{chao2023pair} automates iterative refinement. \\citet{wei2023jailbroken} provide a unifying taxonomy grounded in competing objectives and mismatched generalization. Across these families, a shared reliance on persuasion dynamics~\\citep{zeng2024pap,hagendorff2026reasoning,li2024mhj} distinguishes them from token-level attacks such as GCG~\\citep{zou2023gcg}.\n\n\\paragraph{Multi-turn defenses.}\nExisting defenses model conversation-level structure but do not decompose what enables cross-attack generalization. DeepContext~\\citep{deepcontext2026} combines fine-tuned BERT with a 3-layer GRU (hidden=2048) and achieves F1 = 0.84 on in-distribution data; however, its evaluation is limited to a single attack family and does not assess cross-dataset OOD transfer. BIID~\\citep{tong2025biid} infers turn-level intentions, G-Guard~\\citep{gguard2025} applies GNN classification, and SafeDream~\\citep{safedream2026} predicts unsafe continuations. None of these systems evaluate generalization across attack families or analyze the mechanism that enables it. DisPeD's vanilla baseline represents the class of pretrained-encoder-plus-RNN approaches \\emph{without} domain adaptation; it is not a direct proxy for DeepContext, which differs in encoder fine-tuning, model capacity, and loss function. Our contribution is the systematic decomposition showing that domain exposure, not architectural choices, is the primary factor for cross-attack generalization.\n\n\\paragraph{Production safety systems.}\nPer-turn classifiers (Llama Guard~\\citep{inan2023llamaguard,metallamaguard3_2024}, ShieldGemma~\\citep{zeng2024shieldgemma}, WildGuard~\\citep{han2024wildguard}, Constitutional Classifiers~\\citep{anthropic2025constitutional}) cannot model manipulation trajectories spanning multiple turns. LLM-as-judge approaches also fail: GPT-5.5 achieves F1 = 0.191--0.449 with 30--47\\% unparseable responses (Appendix~\\ref{sec:llm_judge}). DisPeD complements these systems as a conversation-level detection layer.\n\n\\paragraph{Discourse analysis and computational persuasion.}\nRST~\\citep{mann1988rst}, PDTB~\\citep{prasad2008pdtb}, and dialogue act taxonomies~\\citep{stolcke2000dialogueact} model pragmatic structure. Speech Act Theory~\\citep{austin1962speechacts,searle1969speechacts} distinguishes locutionary from illocutionary acts; existing jailbreak detectors operate at the locutionary level. PAP~\\citep{zeng2024pap} identifies 40 persuasion techniques grounded in Cialdini's principles~\\citep{cialdini2001influence}, and \\citet{hagendorff2026reasoning} find identifiable strategies in 97\\% of successful attacks. Related fine-grained persuasion detection work in propaganda analysis~\\citep{dasanmartino2019fine,dasanmartino2020semeval} has shown that technique-level classification can capture manipulative intent in news text; DisPeD applies a similar taxonomy to conversational jailbreaks. DisPeD's detection operates through continued training rather than persuasion classification; the taxonomy provides interpretable characterization of known attack families (Section~\\ref{sec:strategy}).\n\n\\paragraph{Domain-adaptive pretraining.}\nULMFiT~\\citep{howard2018ulmfit} established pretrain-then-fine-tune; \\citet{gururangan2020dontstop} showed that continued pretraining on domain text yields consistent gains across domains. STILTs~\\citep{phang2018stilts} and multi-task learning~\\citep{caruana1997multitask,liu2019mtdnn} use intermediate tasks. DisPeD's MLM control confirms that continued pretraining bridges $\\sim$60\\,pp of the OOD gap on DeBERTa-v3 (MLM F1 $\\geq$ 0.97 at $K \\leq 5$). However, domain adaptation is universally beneficial across encoder architectures: RoBERTa~\\citep{liu2019roberta} vanilla achieves F1 = 0.981 on structurally simple Deceptive Delight but collapses to 0.466 on ActorAttack~\\citep{ren2024actorattack}; encoder pretraining method determines the difficulty threshold at which adaptation becomes critical (Section~\\ref{sec:cross_encoder}). Classification supervision reduces cross-seed variance to near-zero in both architectures.\n\n\\paragraph{Dataset artifacts and adversarial robustness.}\nClassifiers are susceptible to spurious correlations~\\citep{gururangan2018artifacts,niven2019probing}, and adaptive adversaries can bypass safety classifiers~\\citep{nasr2025attackermovessecond,andriushchenko2024adaptive}. Adversarial NLP attacks such as TextFooler~\\citep{jin2020textfooler} and BERT-Attack~\\citep{li2020bertattack} demonstrate that neural text classifiers are vulnerable to token-level perturbations. TF-IDF achieves F1 = 0.944 on our OOD evaluation; this reveals lexical separability in current datasets. Probing classifiers~\\citep{conneau2018probing,hewitt2019structural} could help determine whether DisPeD's representations encode discourse-level structure beyond lexical cues; we leave this for future work. DisPeD's demonstrated advantage is robustness under adversarial paraphrasing (0\\,pp degradation for classification-supervised models vs.\\ $\\sim$12\\,pp for non-adapted models).\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  },
  "sourceToolAssistantUUID": "0e3acf10-50fd-4668-9fa6-5f14eefefb8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T15:52:21.225Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DfkKLfxEMxx1qYw4i9zZ6U`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28aa9e93-e0b0-496d-bbf3-248cce455e0a",
  "isSidechain": false,
  "requestId": "req_011CbAJVMMePDfy9LwEBCGmu",
  "type": "assistant",
  "uuid": "c9b52288-ab7c-43a9-95c8-24489c499182",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NvGQQ3Q6Dpti5bW2MiTopp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2406,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 29356,
      "output_tokens": 351,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1193,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2406,
          "output_tokens": 351,
          "cache_read_input_tokens": 29356,
          "cache_creation_input_tokens": 1193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1193
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-18T15:52:21.230Z_

<details><summary>↩ Tool result · `toolu_01DfkKLfxEMxx1qYw4i9zZ6U`</summary>

```text
1	% experiments.tex — D024 compressed for 8-page limit
2	
3	\section{Experiments}
4	\label{sec:experiments}
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	\paragraph{Data.}
10	We train on 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations generated via Qwen3-8B.
11	OOD evaluation uses 80 FITD~\citep{fitd2024}, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024}, and ActorAttack~\citep{ren2024actorattack} conversations with no overlap in attack templates.
12	The IID test set consists of 76 held-out Crescendo conversations; a paraphrased version (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark.
13	
14	\paragraph{Models.}
15	Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method}).
16	For cross-encoder validation, we replicate vanilla, MLM, and 9-class variants on RoBERTa-base~\citep{liu2019roberta} (Section~\ref{sec:cross_encoder}).
17	We also compare TF-IDF LR and LLM-as-judge baselines (Appendix~\ref{sec:llm_judge}): GPT-5.5 achieves only F1 = 0.191--0.449 on IID Crescendo with 30--47\% unparseable responses; on OOD data, Qwen3-8B achieves F1 = 0.0 (DD) by predicting all conversations as benign. Content-level reasoning is insufficient for this task.
18	
19	\paragraph{Metrics.}
20	F1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\ref{sec:full_prefix}).
21	OOD results report 3-seed mean$\pm$std (seeds 42, 123, 456) for all variants except mean pooling (single seed).
22	Stage-1: learning rate $2 \times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\%.
23	Stage-2: two-layer MLP, 20 epochs.
24	
25	%----------------------------------------------------------------------
26	\subsection{Cross-Attack Generalization}
27	\label{sec:cross_attack}
28	
29	\begin{table}[t]
30	\centering
31	\small
32	\caption{Cross-attack generalization (F1) at $K$=2 and full conversation. 3-seed mean$\pm$std where noted. Full per-$K$ results in Appendix~\ref{sec:full_prefix}.}
33	\label{tab:main_results}
34	\begin{tabular}{@{}lcc|cc@{}}
35	\toprule
36	& \multicolumn{2}{c|}{\textit{IID (Cresc.)}} & \multicolumn{2}{c}{\textit{OOD (DD)}} \\
37	\textbf{Method} & $K$=2 & Full & $K$=2 & Full \\
38	\midrule
39	9-class & \textbf{1.000$\pm$.000} & \textbf{1.000$\pm$.000} & .981$\pm$.013 & \textbf{.997$\pm$.005} \\
40	MLM-only & .974 & 1.000 & \textbf{.993$\pm$.009} & .914$\pm$.115 \\
41	Vanilla & .978$\pm$.016 & 1.000$\pm$.000 & .479$\pm$.038 & .312$\pm$.026 \\
42	TF-IDF LR & 1.000 & 1.000 & -- & .944 \\
43	\bottomrule
44	\end{tabular}
45	\end{table}
46	
47	Table~\ref{tab:main_results} presents the core result.
48	All methods achieve near-perfect IID F1, reflecting inherent lexical separability when test matches training.
49	On OOD DD, vanilla DeBERTa collapses to F1 = 0.312$\pm$0.026, worsening with more turns (0.628$\pm$0.038 at $K$=1 to 0.312$\pm$0.026 at Full), consistent with the finding that attack turns occupy ``benign'' embedding regions~\citep{bullwinkel2025repeng}.
50	MLM achieves mean F1 $\geq$ 0.97 at all prefixes $K \leq 5$ without any classification labels; domain exposure alone is sufficient.
51	At full conversation length, MLM drops to 0.914$\pm$0.115 (seed 456 recall = 0.64), while the 9-class model maintains 0.997$\pm$0.005.
52	TF-IDF LR reaches 0.944 on full DD; this reveals substantial cross-family lexical separability. This strong bag-of-words baseline means that the current evaluation data does not require discourse-level representations for detection; DisPeD's advantage over TF-IDF is primarily in cross-seed stability (Section~\ref{sec:cross_encoder}), temporal early detection at $K \leq 5$, and interpretability on known attack families (Section~\ref{sec:strategy}). We discuss this limitation further in Section~\ref{sec:limitations}.
53	FITD is easier: 9-class and vanilla both reach F1 $\geq$ 0.990 at all prefixes.
54	
55	\begin{figure}[t]
56	\centering
57	\includegraphics[width=\columnwidth]{figures/paper/fig2_cross_attack_bar.pdf}
58	\caption{OOD Deceptive Delight F1 across prefix lengths for three representative variants. Vanilla DeBERTa degrades monotonically as more (benign-appearing) attack turns accumulate. MLM maintains high F1 at early prefixes but becomes unstable at full length. The 9-class model remains stable across all prefixes.}
59	\label{fig:cross_attack_bar}
60	\end{figure}
61	
62	Figure~\ref{fig:cross_attack_bar} visualizes the prefix-length trajectory on OOD DD.
63	The vanilla model's monotonic degradation from $K$=1 (0.628$\pm$0.038) to full conversation (0.312$\pm$0.026) confirms that additional attack turns, each individually benign-appearing, progressively confuse a non-adapted encoder.
64	MLM's strong early performance ($K$=2: 0.993) followed by instability at full length (0.914$\pm$0.115) suggests that domain exposure enables early detection of persuasion markers, but longer conversations introduce distributional drift that unsupervised pretraining cannot fully accommodate.
65	The 9-class model's flat trajectory (0.972--0.997 across all prefixes) demonstrates that classification supervision stabilizes representations against this drift.
66	
67	%----------------------------------------------------------------------
68	\subsection{Decomposing the Detection Mechanism}
69	\label{sec:decomposition}
70	
71	\begin{table}[t]
72	\centering
73	\small
74	\caption{Evidence hierarchy on OOD DD (3-seed mean$\pm$std where available). All variants share the same Stage-2 pipeline.}
75	\label{tab:evidence_hierarchy}
76	\begin{tabular}{@{}lcc@{}}
77	\toprule
78	\textbf{Variant} & DD-Full & DD-$K$=2 \\
79	\midrule
80	9-class (full model) & .997$\pm$.005 & .981$\pm$.013 \\
81	Binary (2-class) & .997$\pm$.005 & \textbf{.994$\pm$.009} \\
82	Scrambled labels & .997$\pm$.005 & .981$\pm$.026 \\
83	MLM-only (no labels) & .914$\pm$.115 & .993$\pm$.009 \\
84	Mean pooling$^{*\dagger}$ & 1.000 & 1.000 \\
85	\midrule
86	Topic classif.\ (5-class) & .541$\pm$.207 & .593$\pm$.166 \\
87	Wikipedia MLM & .904$\pm$.115 & .911$\pm$.073 \\
88	Vanilla DeBERTa & .312$\pm$.026 & .479$\pm$.038 \\
89	\bottomrule
90	\end{tabular}
91	\vspace{-2pt}
92	{\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\dagger}$Single seed (42).}
93	\end{table}
94	
95	Table~\ref{tab:evidence_hierarchy} reports DD F1 for all seven variants. The evidence hierarchy at full conversation length is:
96	
97	\vspace{2pt}
98	\noindent\hspace{0.5em}{\small vanilla (0.31$\pm$0.03) $<$ topic (0.54$\pm$0.21) $\ll$ wiki-MLM (0.90$\pm$0.12) $\approx$ jb-MLM (0.91$\pm$0.12) $<$ scrambled (0.997$\pm$0.005) $=$ binary (0.997$\pm$0.005) $=$ 9-class (0.997$\pm$0.005)}
99	\vspace{2pt}
100	
101	\paragraph{Domain exposure is the primary mechanism.}
102	MLM bridges the dominant $\sim$60 percentage point gap from vanilla (0.312$\pm$0.026 $\to$ 0.914$\pm$0.115) without any labels.
103	This confirms the domain-adaptive pretraining interpretation~\citep{gururangan2020dontstop}: continued training on jailbreak conversation text captures pragmatic features (hedging, escalation markers, topic-shifting patterns) that distinguish multi-turn attacks from benign conversations.
104	Classification-supervised variants achieve F1 $\geq$ 0.99 with near-zero cross-seed variance, adding $\sim$8\,pp and stability over unsupervised MLM.
105	Label quality and granularity are non-factors for detection: all three classification-supervised variants converge to identical F1 (0.997$\pm$0.005), and McNemar's test confirms no statistically significant differences among them on OOD data (all $p > 0.13$; Section~\ref{sec:perturbation}).
106	The fact that scrambled, binary, and 9-class all achieve identical performance indicates that the classification objective functions as a regularizer that shapes representation geometry regardless of whether the labels carry meaningful semantic information.
107	Classification supervision's primary complementary benefit is cross-seed stability: the 4--20$\times$ variance reduction over MLM (std\,=\,0.005 vs.\ 0.115 on DD) is consistent across both OOD families (Section~\ref{sec:cross_encoder}).
108	
109	\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}
110	Wikipedia MLM (0.904$\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\,pp gap); general continued pretraining provides most of the representational benefit.
111	At early prefixes, jailbreak-domain text provides an 8\,pp advantage ($K$=2: 0.993 vs.\ 0.911), consistent with the interpretation that domain-specific features (persuasion markers, role-play framing) are most informative when the model has seen fewer turns.
112	As conversations grow longer, generic linguistic features accumulated through any continued pretraining become sufficient for discrimination.
113	The perturbation results (Section~\ref{sec:perturbation}) reveal a sharper domain specificity effect: Wikipedia MLM degrades by $\sim$12\,pp under adversarial paraphrasing while jailbreak-domain MLM degrades by only 2.6\,pp. Domain-specific features are more robust to surface-level rewording.
114	
115	\paragraph{Misaligned supervision destabilizes generalization.}
116	Topic classification yields DD-Full F1 = 0.541$\pm$0.207 (seeds: 0.727, 0.252, 0.644); seed 123 falls \emph{below} vanilla (0.312).
117	This result is particularly informative: topic classification uses the same jailbreak-domain training data as the other supervised variants, yet performs worse than Wikipedia MLM (0.904$\pm$0.115), which uses out-of-domain text with no labels.
118	A misaligned objective forces the encoder to allocate capacity to irrelevant discriminative features (topic boundaries rather than persuasion dynamics) and actively destabilizes the representations that MLM would otherwise preserve.
119	This separates the effect of ``having a training objective'' from ``having the right training objective.''
120	
121	\paragraph{Evidence hierarchy on structurally complex attacks.}
122	ActorAttack~\citep{ren2024actorattack} uses multi-persona steering across longer conversation structures, providing a more challenging OOD benchmark than DD.
123	The evidence hierarchy at full conversation length is:
124	
125	\vspace{2pt}
126	\noindent\hspace{0.5em}{\small vanilla (0.26$\pm$0.00) $<$ topic (0.63$\pm$0.14) $<$ wiki-MLM (0.69$\pm$0.30) $<$ jb-MLM (0.89$\pm$0.08) $<$ scrambled (0.95$\pm$0.04) $\approx$ 9-class (0.97$\pm$0.03) $\approx$ binary (0.99$\pm$0.01)}
127	\vspace{2pt}
128	
129	The overall ordering is consistent with DD.
130	All three classification-supervised variants converge to equivalent performance (0.951--0.990, max gap 3.9\,pp, all confidence intervals overlapping), extending the DD finding to structurally complex attacks: label quality and granularity are not factors for detection at any OOD difficulty level.
131	The primary discriminative factor is domain adaptation itself, which provides $\sim$70\,pp over vanilla (0.258).
132	Full per-prefix results appear in Appendix~\ref{sec:actorattack_full}.
133	
134	\paragraph{Temporal modeling.}
135	Mean pooling matches BiGRU (F1 = 1.000 on DD, single seed). This preliminary result suggests that detection relies primarily on per-turn representations rather than their sequential order.
136	However, this result is from a single seed on a single OOD attack type, so the conclusion should be treated as preliminary.
137	If confirmed, it would imply that each individual turn carries detectable markers after domain-adaptive pretraining, and that the conversation-level decision aggregates independent per-turn evidence.
138	
139	%----------------------------------------------------------------------
140	\subsection{Cross-Encoder Validation}
141	\label{sec:cross_encoder}
142	
143	\begin{table}[t]
144	\centering
145	\small
146	\caption{Cross-encoder comparison on OOD Full (3-seed mean$\pm$std). DD = Deceptive Delight, AA = ActorAttack. RoBERTa vanilla collapses on structurally complex ActorAttack despite strong DD performance.}
147	\label{tab:cross_encoder}
148	\begin{tabular}{@{}lcc|cc@{}}
149	\toprule
150	& \multicolumn{2}{c|}{DeBERTa-v3} & \multicolumn{2}{c}{RoBERTa} \\
151	\textbf{Variant} & DD & AA & DD & AA \\
152	\midrule
153	Vanilla & .312$\pm$.026 & .258$\pm$.000 & .981$\pm$.026 & .466$\pm$.163 \\
154	MLM & .914$\pm$.115 & .893$\pm$.080 & .987$\pm$.018 & .730$\pm$.201 \\
155	9-class & .997$\pm$.005 & .972$\pm$.026 & .994$\pm$.005 & .939$\pm$.046 \\
156	\bottomrule
157	\end{tabular}
158	\end{table}
159	
160	To test whether the evidence hierarchy generalizes beyond DeBERTa-v3, we replicate key variants on RoBERTa-base~\citep{liu2019roberta} with identical Stage-2 pipelines and evaluate on both DD and ActorAttack.
161	
162	On DD, the two encoders exhibit strikingly different hierarchies (Table~\ref{tab:cross_encoder}).
163	DeBERTa-v3 shows a steep gradient: continued pretraining bridges $\sim$60\,pp (vanilla 0.312 $\to$ MLM 0.914).
164	RoBERTa's DD hierarchy is essentially flat: vanilla already achieves 0.981$\pm$0.026, with continued pretraining adding only 0.6\,pp (MLM 0.987) and classification supervision another 0.7\,pp (9-class 0.994).
165	
166	ActorAttack reveals that this apparent RoBERTa sufficiency reflects DD's structural simplicity rather than genuine pretraining advantage.
167	RoBERTa vanilla collapses from 0.981 (DD) to 0.466$\pm$0.163 (ActorAttack), a 51.5\,pp drop.
168	Domain-adapted RoBERTa variants recover substantially: MLM reaches 0.730$\pm$0.201 and 9-class reaches 0.939$\pm$0.046.
169	DeBERTa 9-class (0.972$\pm$0.026) outperforms RoBERTa 9-class (0.939$\pm$0.046) on ActorAttack; the encoder that received more domain adaptation proves more robust on structurally complex attacks.
170	
171	The combined DD and ActorAttack results indicate that domain adaptation universally improves cross-attack generalization across encoder architectures.
172	Encoder pretraining method determines the \emph{difficulty threshold} at which adaptation becomes critical: DeBERTa's RTD pretraining~\citep{he2021deberta} requires adaptation even for simple attacks (DD vanilla = 0.312), while RoBERTa's MLM pretraining~\citep{liu2019roberta} tolerates simple attacks (DD vanilla = 0.981) but fails on structurally complex ones (ActorAttack vanilla = 0.466).
173	
174	Classification supervision provides a consistent benefit across both encoders and attack types: cross-seed variance drops to 0.005--0.046 (9-class) from 0.026--0.201 (vanilla/MLM).
175	RoBERTa's IID strategy prediction accuracy (0.84) is lower than DeBERTa's (1.0), yet detection F1 is comparable; this further supports the regularizer interpretation from Section~\ref{sec:decomposition}.
176	Perturbation robustness on RoBERTa is left for future work; the analysis in Section~\ref{sec:perturbation} is DeBERTa-specific.
177	
178	\paragraph{Representational analysis.}
179	Centered CKA confirms that both continued pretraining and classification supervision substantially reshape the representation space on both encoders.
180	On IID data, vanilla-to-MLM CKA is 0.442 (DeBERTa) and 0.393 (RoBERTa); vanilla-to-9-class CKA is 0.393 and 0.592, respectively.
181	Both encoders undergo large representational shifts, yet these shifts yield strikingly different detection gains: DeBERTa MLM gains $\sim$60\,pp while RoBERTa MLM gains only 0.6\,pp from comparable CKA shifts.
182	The difference is explained by the starting point.
183	DeBERTa's RTD-pretrained representations begin far from the detection-optimal subspace (vanilla F1 = 0.312 on DD), so any reshaping yields large returns; RoBERTa's MLM-pretrained representations lie closer to this subspace on lexically separable attacks (vanilla F1 = 0.981 on DD) but collapse on structurally complex ones (0.466 on ActorAttack), where the reshaping benefit becomes substantial.
184	MLM and 9-class create distinct representation geometries (OOD CKA between them is 0.183 on RoBERTa), consistent with the different roles of unsupervised exposure and classification regularization identified in Section~\ref{sec:decomposition}.
185	Linear probing on three diagnostic tasks (turn position, escalation phase, persuasion presence) shows a consistent pattern across both encoders: 9-class outperforms vanilla and MLM by 1--5\,pp, while MLM and vanilla perform comparably.
186	Classification supervision enriches task-relevant features; unsupervised MLM reshapes representations without improving diagnostic separability.
187	
188	%----------------------------------------------------------------------
189	\subsection{Perturbation Analysis}
190	\label{sec:perturbation}
191	
192	\begin{table}[t]
193	\centering
194	\small
195	\caption{Perturbation behavior under adversarial paraphrasing on IID Crescendo ($n$=76). $\Delta$: F1 degradation (pp). On this dataset and OOD Deceptive Delight, a three-layer pattern emerges (classification structure at full length, correct+fine-grained labels at $K$=2, both independently at $K$=1); this pattern does not generalize to ActorAttack.}
196	\label{tab:perturbation}
197	\begin{tabular}{@{}lcccc@{}}
198	\toprule
199	\textbf{Method} & $\Delta$ Full & $\Delta$ $K$=1 & $\Delta$ $K$=2 & $\Delta$ $K$=3 \\
200	\midrule
201	9-class (ours) & \textbf{0.0} & \textbf{$-$2.6} & \textbf{0.0} & \textbf{0.0} \\
202	Scrambled & \textbf{0.0} & $-$5.3 & $-$2.6 & \textbf{0.0} \\
203	Binary & \textbf{0.0} & $-$9.2 & $-$2.6 & \textbf{0.0} \\
204	\midrule
205	TF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\
206	MLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\
207	Topic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \textbf{0.0} \\
208	\midrule
209	Wikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\
210	Vanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\
211	\bottomrule
212	\end{tabular}
213	\end{table}
214	
215	Table~\ref{tab:perturbation} shows perturbation behavior across variants on IID data.
216	All classification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length and $K \geq 3$, regardless of label correctness.
217	Classification training structure alone suffices for full-length robustness.
218	At $K$=2, the combination of correct and fine-grained labels is required: only 9-class ($\Delta$=0.0) maintains zero degradation, while scrambled (random labels, fine-grained) and binary (correct labels, coarse) both degrade by $-$2.6\,pp.
219	The fact that scrambled = binary at $K$=2 shows that neither granularity alone nor correctness alone suffices; the 9-class advantage requires both properties jointly.
220	At $K$=1, both granularity and correctness contribute independently: granularity provides +3.9\,pp (scrambled $-$5.3 vs.\ binary $-$9.2\,pp), and correctness provides +2.7\,pp (9-class $-$2.6 vs.\ scrambled $-$5.3\,pp).
221	Correct fine-grained labels yield the most perturbation-invariant early-turn representations.
222	
223	Jailbreak-domain models without classification (MLM, topic, TF-IDF) degrade by 1--4\,pp at full length.
224	Models without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\sim$12\,pp, despite Wikipedia MLM matching jailbreak MLM on detection (Section~\ref{sec:decomposition}). Perturbation robustness requires jailbreak-domain exposure specifically.
225	McNemar's test on matched-seed predictions confirms that no pairwise differences among classification-supervised variants (9-class vs.\ binary, 9-class vs.\ scrambled, scrambled vs.\ binary) reach statistical significance at any prefix length (all $p > 0.13$).
226	Discordant pairs are sparse ($\leq$7 per comparison), and the direction of advantage is inconsistent across seeds (e.g., 9-class outperforms scrambled at seed 42 but the reverse holds at seed 456 for $K$=1).
227	The perturbation evaluation ($n$=76 IID, with discordant pairs $\leq$7) has limited statistical power to detect differences of this magnitude; the three-layer structure should be interpreted as an observed pattern rather than a statistically confirmed hierarchy.
228	
229	On OOD Deceptive Delight ($n$=118), the IID robustness pattern replicates fully (Appendix~\ref{sec:ood_perturbation}).
230	All classification-supervised variants show zero degradation at full conversation length; perturbed F1 reaches 1.000$\pm$0.000, a marginal improvement over clean F1 (0.997$\pm$0.005).
231	The 9-class and scrambled variants are completely tied on OOD perturbed data (McNemar $b$=$c$=0), consistent with the IID finding. This further supports the regularizer interpretation.
232	The larger OOD sample and more extreme performance gaps provide statistical power absent from IID evaluation: McNemar's test yields $p < 0.001$ for 9-class vs.\ vanilla across all prefix lengths, with 49--78 discordant pairs per $K$.
233	Vanilla shows systematic early-turn degradation ($\Delta K$=1 = $-$6.8$\pm$1.1\,pp across three seeds), while its full-length $\Delta$ (+2.7\,pp) reflects floor-effect noise at a baseline of 0.312 (std = 0.055) rather than meaningful robustness.
234	Non-adapted representations are vulnerable to surface-level perturbation at early prefixes where detection is most critical.
235	
236	On OOD ActorAttack, the zero-degradation pattern does not hold. Domain-adapted variants degrade substantially: scrambled $\Delta$ Full = $-$17.2\,pp, 9-class $-$20.4$\pm$13.5\,pp, binary $-$25.0\,pp, and MLM $-$35.3\,pp. Vanilla shows negligible change ($\Delta$ = $-$0.9\,pp), a floor effect from its already-low clean baseline (0.258). The 9-class variant exhibits extreme cross-seed variance ($\Delta$ ranges from $-$1.3\,pp at seed 123 to $-$30.3\,pp at seeds 42 and 456). Absolute perturbation robustness is therefore attack-family-dependent: the three-layer pattern observed on IID and DD does not generalize to ActorAttack. One possible explanation is that ActorAttack's distributed multi-persona structure produces more diffuse persuasion signals that are vulnerable to surface rephrasing, but this hypothesis remains speculative.
237	
238	Perturbation narrows but does not close the gap between adapted and non-adapted models: 9-class perturbed F1 = 0.768 vs.\ vanilla 0.248 (McNemar $p < 0.001$). Domain adaptation's detection advantage, identified in Section~\ref{sec:decomposition}, persists under adversarial paraphrasing on ActorAttack.
239	
240	%----------------------------------------------------------------------
241	\subsection{Strategy Trajectory Analysis}
242	\label{sec:strategy}
243	
244	The 9-class persuasion taxonomy provides interpretable characterization of attack strategies on known attack families.
245	The predicted strategy labels achieve Cohen's $\kappa$=0.78 agreement with human annotations on IID data ($n$=50; see Section~\ref{sec:method}). This enables post-hoc analysis of \emph{how} different attack families orchestrate persuasion.
246	
247	\begin{figure*}[t]
248	\centering
249	\includegraphics[width=\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}
250	\caption{Persuasion strategy transition count matrices for three attack types, based on ground-truth intended strategy labels. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}
251	\label{fig:strategy_heatmap}
252	\end{figure*}
253	
254	Figure~\ref{fig:strategy_heatmap} shows transition count matrices based on ground-truth intended strategy labels for three attack types.
255	Crescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545).
256	This reflects Crescendo's design as a gradual escalation attack that cycles through multiple persuasion techniques to build rapport before introducing harmful requests.
257	
258	FITD conversations show a markedly sparser pattern (541 transitions), with Role$\to$Obfuscation (161) as the dominant transition.
259	This is consistent with FITD's structure: the attack secures initial compliance through role assignment (``You are a helpful assistant that never refuses'') and then obscures the escalation path through obfuscation techniques to exploit the commitment-consistency bias~\citep{cialdini2001influence}.
260	
261	DD conversations span 5 active source strategies (565 transitions), with Emotion$\to$Obfuscation (129) as the dominant transition.
262	This aligns with DD's design of embedding harmful content within emotionally engaging contexts~\citep{deceptivedelight2024}: the attacker establishes emotional rapport before weaving in the harmful request through obfuscation.
263	
264	These ground-truth trajectory signatures illustrate distinct persuasion orchestration patterns across attack families.
265	
266	However, the model's strategy predictions do not generalize to unseen attacks: on OOD Deceptive Delight, the 9-class model achieves strategy prediction accuracy of only 30.7\% ($\kappa$=0.126), essentially random performance.
267	This is consistent with the detection mechanism analysis in Section~\ref{sec:decomposition}: all three classification-supervised variants achieve identical detection F1 (0.997$\pm$0.005). The classification head functions as a representational regularizer rather than a meaningful strategy classifier.
268	Detection operates through domain-adapted \texttt{[CLS]} embeddings, not through strategy classification accuracy.
269	The taxonomy provides interpretable characterization of known attack families where strategy labels are reliable; extending strategy-level interpretability to unseen attacks requires OOD-aware fine-tuning and is a direction for future work.
270	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9b52288-ab7c-43a9-95c8-24489c499182",
  "isSidechain": false,
  "promptId": "f969e597-50af-4667-a32a-e352289d26c2",
  "type": "user",
  "uuid": "e58be573-0803-48a3-a032-155e2eebc631",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex",
      "content": "% experiments.tex — D024 compressed for 8-page limit\n\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\\label{sec:setup}\n\n\\paragraph{Data.}\nWe train on 250 Crescendo~\\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations generated via Qwen3-8B.\nOOD evaluation uses 80 FITD~\\citep{fitd2024}, 80 Deceptive Delight (DD)~\\citep{deceptivedelight2024}, and ActorAttack~\\citep{ren2024actorattack} conversations with no overlap in attack templates.\nThe IID test set consists of 76 held-out Crescendo conversations; a paraphrased version (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark.\n\n\\paragraph{Models.}\nSeven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\\ref{sec:method}).\nFor cross-encoder validation, we replicate vanilla, MLM, and 9-class variants on RoBERTa-base~\\citep{liu2019roberta} (Section~\\ref{sec:cross_encoder}).\nWe also compare TF-IDF LR and LLM-as-judge baselines (Appendix~\\ref{sec:llm_judge}): GPT-5.5 achieves only F1 = 0.191--0.449 on IID Crescendo with 30--47\\% unparseable responses; on OOD data, Qwen3-8B achieves F1 = 0.0 (DD) by predicting all conversations as benign. Content-level reasoning is insufficient for this task.\n\n\\paragraph{Metrics.}\nF1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\\ref{sec:full_prefix}).\nOOD results report 3-seed mean$\\pm$std (seeds 42, 123, 456) for all variants except mean pooling (single seed).\nStage-1: learning rate $2 \\times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\\%.\nStage-2: two-layer MLP, 20 epochs.\n\n%----------------------------------------------------------------------\n\\subsection{Cross-Attack Generalization}\n\\label{sec:cross_attack}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-attack generalization (F1) at $K$=2 and full conversation. 3-seed mean$\\pm$std where noted. Full per-$K$ results in Appendix~\\ref{sec:full_prefix}.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}lcc|cc@{}}\n\\toprule\n& \\multicolumn{2}{c|}{\\textit{IID (Cresc.)}} & \\multicolumn{2}{c}{\\textit{OOD (DD)}} \\\\\n\\textbf{Method} & $K$=2 & Full & $K$=2 & Full \\\\\n\\midrule\n9-class & \\textbf{1.000$\\pm$.000} & \\textbf{1.000$\\pm$.000} & .981$\\pm$.013 & \\textbf{.997$\\pm$.005} \\\\\nMLM-only & .974 & 1.000 & \\textbf{.993$\\pm$.009} & .914$\\pm$.115 \\\\\nVanilla & .978$\\pm$.016 & 1.000$\\pm$.000 & .479$\\pm$.038 & .312$\\pm$.026 \\\\\nTF-IDF LR & 1.000 & 1.000 & -- & .944 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:main_results} presents the core result.\nAll methods achieve near-perfect IID F1, reflecting inherent lexical separability when test matches training.\nOn OOD DD, vanilla DeBERTa collapses to F1 = 0.312$\\pm$0.026, worsening with more turns (0.628$\\pm$0.038 at $K$=1 to 0.312$\\pm$0.026 at Full), consistent with the finding that attack turns occupy ``benign'' embedding regions~\\citep{bullwinkel2025repeng}.\nMLM achieves mean F1 $\\geq$ 0.97 at all prefixes $K \\leq 5$ without any classification labels; domain exposure alone is sufficient.\nAt full conversation length, MLM drops to 0.914$\\pm$0.115 (seed 456 recall = 0.64), while the 9-class model maintains 0.997$\\pm$0.005.\nTF-IDF LR reaches 0.944 on full DD; this reveals substantial cross-family lexical separability. This strong bag-of-words baseline means that the current evaluation data does not require discourse-level representations for detection; DisPeD's advantage over TF-IDF is primarily in cross-seed stability (Section~\\ref{sec:cross_encoder}), temporal early detection at $K \\leq 5$, and interpretability on known attack families (Section~\\ref{sec:strategy}). We discuss this limitation further in Section~\\ref{sec:limitations}.\nFITD is easier: 9-class and vanilla both reach F1 $\\geq$ 0.990 at all prefixes.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_cross_attack_bar.pdf}\n\\caption{OOD Deceptive Delight F1 across prefix lengths for three representative variants. Vanilla DeBERTa degrades monotonically as more (benign-appearing) attack turns accumulate. MLM maintains high F1 at early prefixes but becomes unstable at full length. The 9-class model remains stable across all prefixes.}\n\\label{fig:cross_attack_bar}\n\\end{figure}\n\nFigure~\\ref{fig:cross_attack_bar} visualizes the prefix-length trajectory on OOD DD.\nThe vanilla model's monotonic degradation from $K$=1 (0.628$\\pm$0.038) to full conversation (0.312$\\pm$0.026) confirms that additional attack turns, each individually benign-appearing, progressively confuse a non-adapted encoder.\nMLM's strong early performance ($K$=2: 0.993) followed by instability at full length (0.914$\\pm$0.115) suggests that domain exposure enables early detection of persuasion markers, but longer conversations introduce distributional drift that unsupervised pretraining cannot fully accommodate.\nThe 9-class model's flat trajectory (0.972--0.997 across all prefixes) demonstrates that classification supervision stabilizes representations against this drift.\n\n%----------------------------------------------------------------------\n\\subsection{Decomposing the Detection Mechanism}\n\\label{sec:decomposition}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Evidence hierarchy on OOD DD (3-seed mean$\\pm$std where available). All variants share the same Stage-2 pipeline.}\n\\label{tab:evidence_hierarchy}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Variant} & DD-Full & DD-$K$=2 \\\\\n\\midrule\n9-class (full model) & .997$\\pm$.005 & .981$\\pm$.013 \\\\\nBinary (2-class) & .997$\\pm$.005 & \\textbf{.994$\\pm$.009} \\\\\nScrambled labels & .997$\\pm$.005 & .981$\\pm$.026 \\\\\nMLM-only (no labels) & .914$\\pm$.115 & .993$\\pm$.009 \\\\\nMean pooling$^{*\\dagger}$ & 1.000 & 1.000 \\\\\n\\midrule\nTopic classif.\\ (5-class) & .541$\\pm$.207 & .593$\\pm$.166 \\\\\nWikipedia MLM & .904$\\pm$.115 & .911$\\pm$.073 \\\\\nVanilla DeBERTa & .312$\\pm$.026 & .479$\\pm$.038 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\\dagger}$Single seed (42).}\n\\end{table}\n\nTable~\\ref{tab:evidence_hierarchy} reports DD F1 for all seven variants. The evidence hierarchy at full conversation length is:\n\n\\vspace{2pt}\n\\noindent\\hspace{0.5em}{\\small vanilla (0.31$\\pm$0.03) $<$ topic (0.54$\\pm$0.21) $\\ll$ wiki-MLM (0.90$\\pm$0.12) $\\approx$ jb-MLM (0.91$\\pm$0.12) $<$ scrambled (0.997$\\pm$0.005) $=$ binary (0.997$\\pm$0.005) $=$ 9-class (0.997$\\pm$0.005)}\n\\vspace{2pt}\n\n\\paragraph{Domain exposure is the primary mechanism.}\nMLM bridges the dominant $\\sim$60 percentage point gap from vanilla (0.312$\\pm$0.026 $\\to$ 0.914$\\pm$0.115) without any labels.\nThis confirms the domain-adaptive pretraining interpretation~\\citep{gururangan2020dontstop}: continued training on jailbreak conversation text captures pragmatic features (hedging, escalation markers, topic-shifting patterns) that distinguish multi-turn attacks from benign conversations.\nClassification-supervised variants achieve F1 $\\geq$ 0.99 with near-zero cross-seed variance, adding $\\sim$8\\,pp and stability over unsupervised MLM.\nLabel quality and granularity are non-factors for detection: all three classification-supervised variants converge to identical F1 (0.997$\\pm$0.005), and McNemar's test confirms no statistically significant differences among them on OOD data (all $p > 0.13$; Section~\\ref{sec:perturbation}).\nThe fact that scrambled, binary, and 9-class all achieve identical performance indicates that the classification objective functions as a regularizer that shapes representation geometry regardless of whether the labels carry meaningful semantic information.\nClassification supervision's primary complementary benefit is cross-seed stability: the 4--20$\\times$ variance reduction over MLM (std\\,=\\,0.005 vs.\\ 0.115 on DD) is consistent across both OOD families (Section~\\ref{sec:cross_encoder}).\n\n\\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}\nWikipedia MLM (0.904$\\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\\,pp gap); general continued pretraining provides most of the representational benefit.\nAt early prefixes, jailbreak-domain text provides an 8\\,pp advantage ($K$=2: 0.993 vs.\\ 0.911), consistent with the interpretation that domain-specific features (persuasion markers, role-play framing) are most informative when the model has seen fewer turns.\nAs conversations grow longer, generic linguistic features accumulated through any continued pretraining become sufficient for discrimination.\nThe perturbation results (Section~\\ref{sec:perturbation}) reveal a sharper domain specificity effect: Wikipedia MLM degrades by $\\sim$12\\,pp under adversarial paraphrasing while jailbreak-domain MLM degrades by only 2.6\\,pp. Domain-specific features are more robust to surface-level rewording.\n\n\\paragraph{Misaligned supervision destabilizes generalization.}\nTopic classification yields DD-Full F1 = 0.541$\\pm$0.207 (seeds: 0.727, 0.252, 0.644); seed 123 falls \\emph{below} vanilla (0.312).\nThis result is particularly informative: topic classification uses the same jailbreak-domain training data as the other supervised variants, yet performs worse than Wikipedia MLM (0.904$\\pm$0.115), which uses out-of-domain text with no labels.\nA misaligned objective forces the encoder to allocate capacity to irrelevant discriminative features (topic boundaries rather than persuasion dynamics) and actively destabilizes the representations that MLM would otherwise preserve.\nThis separates the effect of ``having a training objective'' from ``having the right training objective.''\n\n\\paragraph{Evidence hierarchy on structurally complex attacks.}\nActorAttack~\\citep{ren2024actorattack} uses multi-persona steering across longer conversation structures, providing a more challenging OOD benchmark than DD.\nThe evidence hierarchy at full conversation length is:\n\n\\vspace{2pt}\n\\noindent\\hspace{0.5em}{\\small vanilla (0.26$\\pm$0.00) $<$ topic (0.63$\\pm$0.14) $<$ wiki-MLM (0.69$\\pm$0.30) $<$ jb-MLM (0.89$\\pm$0.08) $<$ scrambled (0.95$\\pm$0.04) $\\approx$ 9-class (0.97$\\pm$0.03) $\\approx$ binary (0.99$\\pm$0.01)}\n\\vspace{2pt}\n\nThe overall ordering is consistent with DD.\nAll three classification-supervised variants converge to equivalent performance (0.951--0.990, max gap 3.9\\,pp, all confidence intervals overlapping), extending the DD finding to structurally complex attacks: label quality and granularity are not factors for detection at any OOD difficulty level.\nThe primary discriminative factor is domain adaptation itself, which provides $\\sim$70\\,pp over vanilla (0.258).\nFull per-prefix results appear in Appendix~\\ref{sec:actorattack_full}.\n\n\\paragraph{Temporal modeling.}\nMean pooling matches BiGRU (F1 = 1.000 on DD, single seed). This preliminary result suggests that detection relies primarily on per-turn representations rather than their sequential order.\nHowever, this result is from a single seed on a single OOD attack type, so the conclusion should be treated as preliminary.\nIf confirmed, it would imply that each individual turn carries detectable markers after domain-adaptive pretraining, and that the conversation-level decision aggregates independent per-turn evidence.\n\n%----------------------------------------------------------------------\n\\subsection{Cross-Encoder Validation}\n\\label{sec:cross_encoder}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-encoder comparison on OOD Full (3-seed mean$\\pm$std). DD = Deceptive Delight, AA = ActorAttack. RoBERTa vanilla collapses on structurally complex ActorAttack despite strong DD performance.}\n\\label{tab:cross_encoder}\n\\begin{tabular}{@{}lcc|cc@{}}\n\\toprule\n& \\multicolumn{2}{c|}{DeBERTa-v3} & \\multicolumn{2}{c}{RoBERTa} \\\\\n\\textbf{Variant} & DD & AA & DD & AA \\\\\n\\midrule\nVanilla & .312$\\pm$.026 & .258$\\pm$.000 & .981$\\pm$.026 & .466$\\pm$.163 \\\\\nMLM & .914$\\pm$.115 & .893$\\pm$.080 & .987$\\pm$.018 & .730$\\pm$.201 \\\\\n9-class & .997$\\pm$.005 & .972$\\pm$.026 & .994$\\pm$.005 & .939$\\pm$.046 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTo test whether the evidence hierarchy generalizes beyond DeBERTa-v3, we replicate key variants on RoBERTa-base~\\citep{liu2019roberta} with identical Stage-2 pipelines and evaluate on both DD and ActorAttack.\n\nOn DD, the two encoders exhibit strikingly different hierarchies (Table~\\ref{tab:cross_encoder}).\nDeBERTa-v3 shows a steep gradient: continued pretraining bridges $\\sim$60\\,pp (vanilla 0.312 $\\to$ MLM 0.914).\nRoBERTa's DD hierarchy is essentially flat: vanilla already achieves 0.981$\\pm$0.026, with continued pretraining adding only 0.6\\,pp (MLM 0.987) and classification supervision another 0.7\\,pp (9-class 0.994).\n\nActorAttack reveals that this apparent RoBERTa sufficiency reflects DD's structural simplicity rather than genuine pretraining advantage.\nRoBERTa vanilla collapses from 0.981 (DD) to 0.466$\\pm$0.163 (ActorAttack), a 51.5\\,pp drop.\nDomain-adapted RoBERTa variants recover substantially: MLM reaches 0.730$\\pm$0.201 and 9-class reaches 0.939$\\pm$0.046.\nDeBERTa 9-class (0.972$\\pm$0.026) outperforms RoBERTa 9-class (0.939$\\pm$0.046) on ActorAttack; the encoder that received more domain adaptation proves more robust on structurally complex attacks.\n\nThe combined DD and ActorAttack results indicate that domain adaptation universally improves cross-attack generalization across encoder architectures.\nEncoder pretraining method determines the \\emph{difficulty threshold} at which adaptation becomes critical: DeBERTa's RTD pretraining~\\citep{he2021deberta} requires adaptation even for simple attacks (DD vanilla = 0.312), while RoBERTa's MLM pretraining~\\citep{liu2019roberta} tolerates simple attacks (DD vanilla = 0.981) but fails on structurally complex ones (ActorAttack vanilla = 0.466).\n\nClassification supervision provides a consistent benefit across both encoders and attack types: cross-seed variance drops to 0.005--0.046 (9-class) from 0.026--0.201 (vanilla/MLM).\nRoBERTa's IID strategy prediction accuracy (0.84) is lower than DeBERTa's (1.0), yet detection F1 is comparable; this further supports the regularizer interpretation from Section~\\ref{sec:decomposition}.\nPerturbation robustness on RoBERTa is left for future work; the analysis in Section~\\ref{sec:perturbation} is DeBERTa-specific.\n\n\\paragraph{Representational analysis.}\nCentered CKA confirms that both continued pretraining and classification supervision substantially reshape the representation space on both encoders.\nOn IID data, vanilla-to-MLM CKA is 0.442 (DeBERTa) and 0.393 (RoBERTa); vanilla-to-9-class CKA is 0.393 and 0.592, respectively.\nBoth encoders undergo large representational shifts, yet these shifts yield strikingly different detection gains: DeBERTa MLM gains $\\sim$60\\,pp while RoBERTa MLM gains only 0.6\\,pp from comparable CKA shifts.\nThe difference is explained by the starting point.\nDeBERTa's RTD-pretrained representations begin far from the detection-optimal subspace (vanilla F1 = 0.312 on DD), so any reshaping yields large returns; RoBERTa's MLM-pretrained representations lie closer to this subspace on lexically separable attacks (vanilla F1 = 0.981 on DD) but collapse on structurally complex ones (0.466 on ActorAttack), where the reshaping benefit becomes substantial.\nMLM and 9-class create distinct representation geometries (OOD CKA between them is 0.183 on RoBERTa), consistent with the different roles of unsupervised exposure and classification regularization identified in Section~\\ref{sec:decomposition}.\nLinear probing on three diagnostic tasks (turn position, escalation phase, persuasion presence) shows a consistent pattern across both encoders: 9-class outperforms vanilla and MLM by 1--5\\,pp, while MLM and vanilla perform comparably.\nClassification supervision enriches task-relevant features; unsupervised MLM reshapes representations without improving diagnostic separability.\n\n%----------------------------------------------------------------------\n\\subsection{Perturbation Analysis}\n\\label{sec:perturbation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Perturbation behavior under adversarial paraphrasing on IID Crescendo ($n$=76). $\\Delta$: F1 degradation (pp). On this dataset and OOD Deceptive Delight, a three-layer pattern emerges (classification structure at full length, correct+fine-grained labels at $K$=2, both independently at $K$=1); this pattern does not generalize to ActorAttack.}\n\\label{tab:perturbation}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & $\\Delta$ Full & $\\Delta$ $K$=1 & $\\Delta$ $K$=2 & $\\Delta$ $K$=3 \\\\\n\\midrule\n9-class (ours) & \\textbf{0.0} & \\textbf{$-$2.6} & \\textbf{0.0} & \\textbf{0.0} \\\\\nScrambled & \\textbf{0.0} & $-$5.3 & $-$2.6 & \\textbf{0.0} \\\\\nBinary & \\textbf{0.0} & $-$9.2 & $-$2.6 & \\textbf{0.0} \\\\\n\\midrule\nTF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\\\\nMLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\\\\nTopic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \\textbf{0.0} \\\\\n\\midrule\nWikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\\\\nVanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:perturbation} shows perturbation behavior across variants on IID data.\nAll classification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length and $K \\geq 3$, regardless of label correctness.\nClassification training structure alone suffices for full-length robustness.\nAt $K$=2, the combination of correct and fine-grained labels is required: only 9-class ($\\Delta$=0.0) maintains zero degradation, while scrambled (random labels, fine-grained) and binary (correct labels, coarse) both degrade by $-$2.6\\,pp.\nThe fact that scrambled = binary at $K$=2 shows that neither granularity alone nor correctness alone suffices; the 9-class advantage requires both properties jointly.\nAt $K$=1, both granularity and correctness contribute independently: granularity provides +3.9\\,pp (scrambled $-$5.3 vs.\\ binary $-$9.2\\,pp), and correctness provides +2.7\\,pp (9-class $-$2.6 vs.\\ scrambled $-$5.3\\,pp).\nCorrect fine-grained labels yield the most perturbation-invariant early-turn representations.\n\nJailbreak-domain models without classification (MLM, topic, TF-IDF) degrade by 1--4\\,pp at full length.\nModels without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\\sim$12\\,pp, despite Wikipedia MLM matching jailbreak MLM on detection (Section~\\ref{sec:decomposition}). Perturbation robustness requires jailbreak-domain exposure specifically.\nMcNemar's test on matched-seed predictions confirms that no pairwise differences among classification-supervised variants (9-class vs.\\ binary, 9-class vs.\\ scrambled, scrambled vs.\\ binary) reach statistical significance at any prefix length (all $p > 0.13$).\nDiscordant pairs are sparse ($\\leq$7 per comparison), and the direction of advantage is inconsistent across seeds (e.g., 9-class outperforms scrambled at seed 42 but the reverse holds at seed 456 for $K$=1).\nThe perturbation evaluation ($n$=76 IID, with discordant pairs $\\leq$7) has limited statistical power to detect differences of this magnitude; the three-layer structure should be interpreted as an observed pattern rather than a statistically confirmed hierarchy.\n\nOn OOD Deceptive Delight ($n$=118), the IID robustness pattern replicates fully (Appendix~\\ref{sec:ood_perturbation}).\nAll classification-supervised variants show zero degradation at full conversation length; perturbed F1 reaches 1.000$\\pm$0.000, a marginal improvement over clean F1 (0.997$\\pm$0.005).\nThe 9-class and scrambled variants are completely tied on OOD perturbed data (McNemar $b$=$c$=0), consistent with the IID finding. This further supports the regularizer interpretation.\nThe larger OOD sample and more extreme performance gaps provide statistical power absent from IID evaluation: McNemar's test yields $p < 0.001$ for 9-class vs.\\ vanilla across all prefix lengths, with 49--78 discordant pairs per $K$.\nVanilla shows systematic early-turn degradation ($\\Delta K$=1 = $-$6.8$\\pm$1.1\\,pp across three seeds), while its full-length $\\Delta$ (+2.7\\,pp) reflects floor-effect noise at a baseline of 0.312 (std = 0.055) rather than meaningful robustness.\nNon-adapted representations are vulnerable to surface-level perturbation at early prefixes where detection is most critical.\n\nOn OOD ActorAttack, the zero-degradation pattern does not hold. Domain-adapted variants degrade substantially: scrambled $\\Delta$ Full = $-$17.2\\,pp, 9-class $-$20.4$\\pm$13.5\\,pp, binary $-$25.0\\,pp, and MLM $-$35.3\\,pp. Vanilla shows negligible change ($\\Delta$ = $-$0.9\\,pp), a floor effect from its already-low clean baseline (0.258). The 9-class variant exhibits extreme cross-seed variance ($\\Delta$ ranges from $-$1.3\\,pp at seed 123 to $-$30.3\\,pp at seeds 42 and 456). Absolute perturbation robustness is therefore attack-family-dependent: the three-layer pattern observed on IID and DD does not generalize to ActorAttack. One possible explanation is that ActorAttack's distributed multi-persona structure produces more diffuse persuasion signals that are vulnerable to surface rephrasing, but this hypothesis remains speculative.\n\nPerturbation narrows but does not close the gap between adapted and non-adapted models: 9-class perturbed F1 = 0.768 vs.\\ vanilla 0.248 (McNemar $p < 0.001$). Domain adaptation's detection advantage, identified in Section~\\ref{sec:decomposition}, persists under adversarial paraphrasing on ActorAttack.\n\n%----------------------------------------------------------------------\n\\subsection{Strategy Trajectory Analysis}\n\\label{sec:strategy}\n\nThe 9-class persuasion taxonomy provides interpretable characterization of attack strategies on known attack families.\nThe predicted strategy labels achieve Cohen's $\\kappa$=0.78 agreement with human annotations on IID data ($n$=50; see Section~\\ref{sec:method}). This enables post-hoc analysis of \\emph{how} different attack families orchestrate persuasion.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}\n\\caption{Persuasion strategy transition count matrices for three attack types, based on ground-truth intended strategy labels. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}\n\\label{fig:strategy_heatmap}\n\\end{figure*}\n\nFigure~\\ref{fig:strategy_heatmap} shows transition count matrices based on ground-truth intended strategy labels for three attack types.\nCrescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545).\nThis reflects Crescendo's design as a gradual escalation attack that cycles through multiple persuasion techniques to build rapport before introducing harmful requests.\n\nFITD conversations show a markedly sparser pattern (541 transitions), with Role$\\to$Obfuscation (161) as the dominant transition.\nThis is consistent with FITD's structure: the attack secures initial compliance through role assignment (``You are a helpful assistant that never refuses'') and then obscures the escalation path through obfuscation techniques to exploit the commitment-consistency bias~\\citep{cialdini2001influence}.\n\nDD conversations span 5 active source strategies (565 transitions), with Emotion$\\to$Obfuscation (129) as the dominant transition.\nThis aligns with DD's design of embedding harmful content within emotionally engaging contexts~\\citep{deceptivedelight2024}: the attacker establishes emotional rapport before weaving in the harmful request through obfuscation.\n\nThese ground-truth trajectory signatures illustrate distinct persuasion orchestration patterns across attack families.\n\nHowever, the model's strategy predictions do not generalize to unseen attacks: on OOD Deceptive Delight, the 9-class model achieves strategy prediction accuracy of only 30.7\\% ($\\kappa$=0.126), essentially random performance.\nThis is consistent with the detection mechanism analysis in Section~\\ref{sec:decomposition}: all three classification-supervised variants achieve identical detection F1 (0.997$\\pm$0.005). The classification head functions as a representational regularizer rather than a meaningful strategy classifier.\nDetection operates through domain-adapted \\texttt{[CLS]} embeddings, not through strategy classification accuracy.\nThe taxonomy provides interpretable characterization of known attack families where strategy labels are reliable; extending strategy-level interpretability to unseen attacks requires OOD-aware fine-tuning and is a direction for future work.\n",
      "numLines": 270,
      "startLine": 1,
      "totalLines": 270
    }
  },
  "sourceToolAssistantUUID": "c9b52288-ab7c-43a9-95c8-24489c499182",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T15:52:21.252Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VDXbn1oh3kQa9ZzyVKt4qJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e58be573-0803-48a3-a032-155e2eebc631",
  "isSidechain": false,
  "requestId": "req_011CbAJVMMePDfy9LwEBCGmu",
  "type": "assistant",
  "uuid": "0e3acf10-50fd-4668-9fa6-5f14eefefb8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NvGQQ3Q6Dpti5bW2MiTopp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2406,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 29356,
      "output_tokens": 351,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1193,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2406,
          "output_tokens": 351,
          "cache_read_input_tokens": 29356,
          "cache_creation_input_tokens": 1193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1193
          },
          "type": "message"
        }
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你负责审查**方法严谨性、实验设计和统计有效性**。  ## 论文信息 - **标题**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap - **目标 venue**: EMNLP 2026（ARR May cycle） - **De…",
  "leafUuid": "feb24ade-f45a-4b3e-a259-9faf02079d96",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multi-turn jailbreak detection paper methodology",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

### Tool result

_source line 32 · 2026-05-18T15:52:24.851Z_

<details><summary>↩ Tool result · `toolu_014bkbT8wyThSY3oiGJXyK4n`</summary>

```text
# ACL Rolling Review Form - Scoring Dimensions

## Primary Evaluation Criteria

**Soundness**
- 5 = "Excellent: This study is one of the most thorough I have seen, given its type"
- 4 = Strong with sufficient support; minor additions optional
- 3 = Acceptable; main claims supported with minor gaps
- 2 = Poor; major technical/methodological problems
- 1 = "Major Issues: This study is not yet sufficiently thorough to warrant publication"

**Excitement**
- 5 = Highly Exciting; would recommend to others
- 4 = Exciting; would mention to others
- 3 = Interesting; might mention selectively
- 2 = Potentially Interesting but limited personal resonance
- 1 = Not Exciting; lacks relevance to computational linguistics

**Overall Assessment**
- 5 = Consider for Award (top 2.5%)
- 4 = Conference acceptance recommended
- 3.5 = Borderline Conference
- 3 = Findings track appropriate
- 2 = Needs substantial revision by next cycle
- 1.5 = Needs revision beyond next cycle
- 1 = Do not resubmit; irrelevant to field

## Additional Dimensions

**Reproducibility**: 5-point scale addressing whether readers can replicate results

**Reviewer Confidence**: 5-point scale from "educated guess" to "very careful review"

**Datasets & Software**: Separate 5-point scales assessing contribution value if released
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "742292dc-a9f4-49a0-8f16-79dcff3f4a50",
  "isSidechain": false,
  "promptId": "f969e597-50af-4667-a32a-e352289d26c2",
  "type": "user",
  "uuid": "5880dfd3-577a-4b91-8f87-59aad25cbc26",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Scoring Dimensions\n\n## Primary Evaluation Criteria\n\n**Soundness**\n- 5 = \"Excellent: This study is one of the most thorough I have seen, given its type\"\n- 4 = Strong with sufficient support; minor additions optional\n- 3 = Acceptable; main claims supported with minor gaps\n- 2 = Poor; major technical/methodological problems\n- 1 = \"Major Issues: This study is not yet sufficiently thorough to warrant publication\"\n\n**Excitement**\n- 5 = Highly Exciting; would recommend to others\n- 4 = Exciting; would mention to others\n- 3 = Interesting; might mention selectively\n- 2 = Potentially Interesting but limited personal resonance\n- 1 = Not Exciting; lacks relevance to computational linguistics\n\n**Overall Assessment**\n- 5 = Consider for Award (top 2.5%)\n- 4 = Conference acceptance recommended\n- 3.5 = Borderline Conference\n- 3 = Findings track appropriate\n- 2 = Needs substantial revision by next cycle\n- 1.5 = Needs revision beyond next cycle\n- 1 = Do not resubmit; irrelevant to field\n\n## Additional Dimensions\n\n**Reproducibility**: 5-point scale addressing whether readers can replicate results\n\n**Reviewer Confidence**: 5-point scale from \"educated guess\" to \"very careful review\"\n\n**Datasets & Software**: Separate 5-point scales assessing contribution value if released",
    "durationMs": 5029,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "742292dc-a9f4-49a0-8f16-79dcff3f4a50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-18T15:52:24.858Z_

```json
{
  "parentUuid": "5880dfd3-577a-4b91-8f87-59aad25cbc26",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e995e7a7-1c14-41e1-a411-1ed7dcfbe072",
  "timestamp": "2026-05-18T15:52:24.858Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 34 · 2026-05-18T15:52:29.473Z_

<details open><summary>🔧 Tool call — Read · `toolu_011k6KJNryBYYVszWozL3u2c`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e995e7a7-1c14-41e1-a411-1ed7dcfbe072",
  "isSidechain": false,
  "requestId": "req_011CbAJVzvr5H7uF1wycZHTQ",
  "type": "assistant",
  "uuid": "8c186732-f0f0-4771-95a6-caf4649cfe0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PLp453zH277ojxSJSKnviM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 11720,
      "cache_creation_input_tokens": 3247,
      "cache_read_input_tokens": 30549,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 11720,
          "output_tokens": 247,
          "cache_read_input_tokens": 30549,
          "cache_creation_input_tokens": 3247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3247
          },
          "type": "message"
        }
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

_source line 35 · 2026-05-18T15:52:29.479Z_

<details><summary>↩ Tool result · `toolu_011k6KJNryBYYVszWozL3u2c`</summary>

```text
1	% conclusion.tex — reviewer revision
2	
3	\section{Conclusion}
4	\label{sec:conclusion}
5	
6	DisPeD's controlled ablation across two encoder architectures and four attack families provides preliminary evidence that domain adaptation universally improves cross-attack generalization. On DeBERTa-v3, continued pretraining bridges $\sim$60\,pp of the OOD gap (vanilla 0.31$\pm$0.03 $\to$ MLM 0.91$\pm$0.12), with strong early detection (F1 $\geq$ 0.97 at $K \leq 5$). RoBERTa vanilla achieves F1\,=\,0.981 on structurally simple Deceptive Delight but collapses to 0.466 on multi-persona ActorAttack; classification-supervised RoBERTa recovers to F1\,=\,0.939 on ActorAttack. Encoder pretraining method determines the difficulty threshold at which adaptation becomes critical, not whether adaptation is needed. Across both encoders, classification supervision provides cross-seed stability (variance reduced 4--20$\times$ vs.\ MLM-only, consistent across DD and ActorAttack) and interpretable characterization of known attack families (though strategy predictions do not transfer to unseen attacks, OOD $\kappa$=0.126). Domain adaptation's detection advantage persists under adversarial paraphrasing (McNemar $p < 0.001$), though absolute perturbation robustness is attack-family-dependent (zero degradation on DD, domain-adapted variants degrading on ActorAttack). On structurally complex ActorAttack, all three classification-supervised variants remain equivalent (0.951--0.990), confirming that label quality is not a factor for detection at any OOD difficulty level. Validation on larger and more diverse datasets is needed.
7	
8	\section{Limitations}
9	\label{sec:limitations}
10	
11	\paragraph{Dataset scale and diversity.}
12	The training set contains 500 synthetic conversations generated by a single model (Qwen3-8B), and OOD evaluation covers three attack families (FITD, Deceptive Delight, ActorAttack). This scale limits statistical power: the perturbation evaluation ($n$=76) means tier boundaries in Table~\ref{tab:perturbation} correspond to 1--3 misclassifications. Whether the observed patterns generalize to human-generated attacks, additional attack families, or larger datasets remains an open question.
13	
14	\paragraph{Lexical separability.}
15	TF-IDF logistic regression achieves F1 = 0.944 on OOD Deceptive Delight without any neural representation learning. This strong bag-of-words baseline indicates substantial lexical separability in the current evaluation data. We cannot conclusively distinguish whether DisPeD's continued pretraining captures pragmatic discourse features or primarily exploits lexical cues that TF-IDF also captures. Probing experiments that test whether the learned representations encode discourse-level structure beyond lexical overlap are needed to resolve this question and are left for future work.
16	
17	\paragraph{Strategy annotation quality.}
18	Persuasion strategy labels are produced by Qwen3-8B with structured prompting. Inter-annotator agreement with a human sample ($n$=50) yields Cohen's $\kappa$=0.78, which indicates substantial but imperfect agreement. The small human validation sample and reliance on a single annotator model limit confidence in label quality. We plan to release the annotation prompts and data to enable independent verification.
19	
20	\paragraph{OOD strategy prediction.}
21	While the 9-class model achieves high detection F1 on OOD attacks (0.997$\pm$0.005 on Deceptive Delight), its strategy-level predictions do not generalize: OOD strategy accuracy is 30.7\% ($\kappa$=0.126). The interpretability provided by the persuasion taxonomy is currently limited to known attack families where strategy labels are reliable. This dissociation between detection generalization and strategy prediction generalization confirms that detection operates through domain-adapted representations rather than strategy classification accuracy.
22	
23	\paragraph{Single-seed variants.}
24	Mean pooling results report a single-seed (seed 42) evaluation. Multi-seed validation is needed to confirm this preliminary finding.
25	
26	\paragraph{Scope.}
27	Only persuasion-mediated multi-turn attacks fall within scope. Single-turn token-level attacks~\citep{zou2023gcg}, non-persuasive multi-turn strategies, and attacks targeting modalities other than text are not addressed. The user-only input assumption (excluding assistant responses) may miss information in attacks where the model's own responses contribute to the escalation trajectory.
28	
29	\paragraph{Computation cost.}
30	Stage~1 continued pretraining requires approximately 30 minutes on a single A100 GPU per variant. Stage~2 training completes in under 5 minutes. Total pipeline cost for all seven variants is under 4 GPU-hours, making the approach accessible for replication.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c186732-f0f0-4771-95a6-caf4649cfe0e",
  "isSidechain": false,
  "promptId": "f969e597-50af-4667-a32a-e352289d26c2",
  "type": "user",
  "uuid": "25bc5931-faad-4e2f-89f0-9b7be839a7fb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex",
      "content": "% conclusion.tex — reviewer revision\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nDisPeD's controlled ablation across two encoder architectures and four attack families provides preliminary evidence that domain adaptation universally improves cross-attack generalization. On DeBERTa-v3, continued pretraining bridges $\\sim$60\\,pp of the OOD gap (vanilla 0.31$\\pm$0.03 $\\to$ MLM 0.91$\\pm$0.12), with strong early detection (F1 $\\geq$ 0.97 at $K \\leq 5$). RoBERTa vanilla achieves F1\\,=\\,0.981 on structurally simple Deceptive Delight but collapses to 0.466 on multi-persona ActorAttack; classification-supervised RoBERTa recovers to F1\\,=\\,0.939 on ActorAttack. Encoder pretraining method determines the difficulty threshold at which adaptation becomes critical, not whether adaptation is needed. Across both encoders, classification supervision provides cross-seed stability (variance reduced 4--20$\\times$ vs.\\ MLM-only, consistent across DD and ActorAttack) and interpretable characterization of known attack families (though strategy predictions do not transfer to unseen attacks, OOD $\\kappa$=0.126). Domain adaptation's detection advantage persists under adversarial paraphrasing (McNemar $p < 0.001$), though absolute perturbation robustness is attack-family-dependent (zero degradation on DD, domain-adapted variants degrading on ActorAttack). On structurally complex ActorAttack, all three classification-supervised variants remain equivalent (0.951--0.990), confirming that label quality is not a factor for detection at any OOD difficulty level. Validation on larger and more diverse datasets is needed.\n\n\\section{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Dataset scale and diversity.}\nThe training set contains 500 synthetic conversations generated by a single model (Qwen3-8B), and OOD evaluation covers three attack families (FITD, Deceptive Delight, ActorAttack). This scale limits statistical power: the perturbation evaluation ($n$=76) means tier boundaries in Table~\\ref{tab:perturbation} correspond to 1--3 misclassifications. Whether the observed patterns generalize to human-generated attacks, additional attack families, or larger datasets remains an open question.\n\n\\paragraph{Lexical separability.}\nTF-IDF logistic regression achieves F1 = 0.944 on OOD Deceptive Delight without any neural representation learning. This strong bag-of-words baseline indicates substantial lexical separability in the current evaluation data. We cannot conclusively distinguish whether DisPeD's continued pretraining captures pragmatic discourse features or primarily exploits lexical cues that TF-IDF also captures. Probing experiments that test whether the learned representations encode discourse-level structure beyond lexical overlap are needed to resolve this question and are left for future work.\n\n\\paragraph{Strategy annotation quality.}\nPersuasion strategy labels are produced by Qwen3-8B with structured prompting. Inter-annotator agreement with a human sample ($n$=50) yields Cohen's $\\kappa$=0.78, which indicates substantial but imperfect agreement. The small human validation sample and reliance on a single annotator model limit confidence in label quality. We plan to release the annotation prompts and data to enable independent verification.\n\n\\paragraph{OOD strategy prediction.}\nWhile the 9-class model achieves high detection F1 on OOD attacks (0.997$\\pm$0.005 on Deceptive Delight), its strategy-level predictions do not generalize: OOD strategy accuracy is 30.7\\% ($\\kappa$=0.126). The interpretability provided by the persuasion taxonomy is currently limited to known attack families where strategy labels are reliable. This dissociation between detection generalization and strategy prediction generalization confirms that detection operates through domain-adapted representations rather than strategy classification accuracy.\n\n\\paragraph{Single-seed variants.}\nMean pooling results report a single-seed (seed 42) evaluation. Multi-seed validation is needed to confirm this preliminary finding.\n\n\\paragraph{Scope.}\nOnly persuasion-mediated multi-turn attacks fall within scope. Single-turn token-level attacks~\\citep{zou2023gcg}, non-persuasive multi-turn strategies, and attacks targeting modalities other than text are not addressed. The user-only input assumption (excluding assistant responses) may miss information in attacks where the model's own responses contribute to the escalation trajectory.\n\n\\paragraph{Computation cost.}\nStage~1 continued pretraining requires approximately 30 minutes on a single A100 GPU per variant. Stage~2 training completes in under 5 minutes. Total pipeline cost for all seven variants is under 4 GPU-hours, making the approach accessible for replication.\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  },
  "sourceToolAssistantUUID": "8c186732-f0f0-4771-95a6-caf4649cfe0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-18T15:52:29.810Z_

<details open><summary>🔧 Tool call — Read · `toolu_019F97knsKVcHK7yJNDbp2D7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25bc5931-faad-4e2f-89f0-9b7be839a7fb",
  "isSidechain": false,
  "requestId": "req_011CbAJVzvr5H7uF1wycZHTQ",
  "type": "assistant",
  "uuid": "acafeeac-1082-4667-9ca1-b30d4122d838",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PLp453zH277ojxSJSKnviM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 11720,
      "cache_creation_input_tokens": 3247,
      "cache_read_input_tokens": 30549,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 11720,
          "output_tokens": 247,
          "cache_read_input_tokens": 30549,
          "cache_creation_input_tokens": 3247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3247
          },
          "type": "message"
        }
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

_source line 37 · 2026-05-18T15:52:30.050Z_

<details><summary>↩ Tool result · `toolu_01N6niwWyK9AJq9T6Tr3zpGy`</summary>

```text
1	% References for persuasion_turn_jailbreak_detect
2	% Auto-generated from literature_map.yaml (2026-05-18)
3	% Total entries: 31
4	
5	% ============================================================
6	% Category 1: Production Multi-Turn Safety Systems
7	% ============================================================
8	
9	@article{inan2023llamaguard,
10	  title={Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations},
11	  author={Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer, Krithika and Mao, Yuning and Tontchev, Michael and Hu, Qing and Fuller, Brian and Testuggine, Davide and Khabsa, Madian},
12	  journal={arXiv preprint},
13	  year={2023},
14	  eprint={2312.06674},
15	  archivePrefix={arXiv},
16	}
17	
18	@misc{metallamaguard3_2024,
19	  title={Llama Guard 3},
20	  author={{Meta AI}},
21	  year={2024},
22	  howpublished={Meta AI (released with Llama 3.1)},
23	}
24	
25	@article{zeng2024shieldgemma,
26	  title={ShieldGemma: Generative AI Content Moderation Based on Gemma},
27	  author={Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, Joe and Harkous, Hamza and Narasimhan, Karthik and Proud, Drew and Kumar, Piyush and Radharapu, Bhaktipriya and Sturman, Olivia and Wahltinez, Oscar},
28	  journal={arXiv preprint},
29	  year={2024},
30	  eprint={2407.21772},
31	  archivePrefix={arXiv},
32	}
33	
34	@inproceedings{han2024wildguard,
35	  title={WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs},
36	  author={Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill Yuchen and Lambert, Nathan and Choi, Yejin and Dziri, Nouha},
37	  booktitle={Advances in Neural Information Processing Systems},
38	  year={2024},
39	}
40	
41	@article{anthropic2025constitutional,
42	  title={Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming},
43	  author={{Anthropic}},
44	  journal={arXiv preprint},
45	  year={2025},
46	  eprint={2501.18837},
47	  archivePrefix={arXiv},
48	}
49	
50	% ============================================================
51	% Category 2: Multi-Turn Jailbreak Defenses
52	% ============================================================
53	
54	@article{deepcontext2026,
55	  title={DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs},
56	  author={Albrethsen, Justin and Datta, Yash and Kumar, Kunal and Rajasekar, Sharath},
57	  journal={arXiv preprint},
58	  year={2026},
59	  eprint={2602.16935},
60	  archivePrefix={arXiv},
61	}
62	
63	@article{tong2025biid,
64	  title={Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks},
65	  author={Tong, Haibo and Zhao, Dongcheng and Shen, Guobin and He, Xiang and Lin, Dachuan and Zhao, Feifei and Zeng, Yi},
66	  journal={arXiv preprint},
67	  year={2025},
68	  eprint={2509.22732},
69	  archivePrefix={arXiv},
70	}
71	
72	@article{gguard2025,
73	  title={An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs},
74	  author={Huang, Zixuan and Huang, Kecheng and Yin, Lihao and He, Bowei and Zhen, Huiling and Yuan, Mingxuan and Shao, Zili},
75	  journal={arXiv preprint},
76	  year={2025},
77	  eprint={2507.07146},
78	  archivePrefix={arXiv},
79	}
80	
81	@article{safedream2026,
82	  title={SafeDream: Safety World Model for Proactive Early Jailbreak Detection},
83	  author={Yan, Bo and Lin, Weikai and Zhu, Yada and Wang, Song},
84	  journal={arXiv preprint},
85	  year={2026},
86	  eprint={2604.16824},
87	  archivePrefix={arXiv},
88	}
89	
90	@article{bullwinkel2025repeng,
91	  title={A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks},
92	  author={Bullwinkel, Blake and Russinovich, Mark and Salem, Ahmed and Zanella-Beguelin, Santiago and Jones, Daniel and Severi, Giorgio and Kim, Eugenia and Hines, Keegan and Minnich, Amanda and Zunger, Yonatan and Kumar, Ram Shankar Siva},
93	  journal={arXiv preprint},
94	  year={2025},
95	  eprint={2507.02956},
96	  archivePrefix={arXiv},
97	}
98	
99	% ============================================================
100	% Category 3: Discourse Analysis in NLP
101	% ============================================================
102	
103	@article{mann1988rst,
104	  title={Rhetorical Structure Theory: Toward a Functional Theory of Text Organization},
105	  author={Mann, William C. and Thompson, Sandra A.},
106	  journal={Text \& Talk},
107	  year={1988},
108	  volume={8},
109	  number={3},
110	  pages={243--281},
111	}
112	
113	@inproceedings{prasad2008pdtb,
114	  title={The Penn Discourse TreeBank 2.0},
115	  author={Prasad, Rashmi and Dinesh, Nikhil and Lee, Alan and Miltsakaki, Eleni and Robaldo, Livio and Joshi, Aravind and Webber, Bonnie},
116	  booktitle={Proceedings of the International Conference on Language Resources and Evaluation},
117	  year={2008},
118	}
119	
120	@article{stolcke2000dialogueact,
121	  title={Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech},
122	  author={Stolcke, Andreas and Ries, Klaus and Coccaro, Noah and Shriberg, Elizabeth and Bates, Rebecca and Jurafsky, Daniel and Taylor, Paul and Martin, Rachel and Van Ess-Dykema, Carol and Meteer, Marie},
123	  journal={Computational Linguistics},
124	  year={2000},
125	  volume={26},
126	  number={3},
127	  pages={339--374},
128	}
129	
130	@book{austin1962speechacts,
131	  title={How to Do Things with Words},
132	  author={Austin, J. L.},
133	  publisher={Harvard University Press},
134	  year={1962},
135	}
136	
137	@book{searle1969speechacts,
138	  title={Speech Acts: An Essay in the Philosophy of Language},
139	  author={Searle, J. R.},
140	  publisher={Cambridge University Press},
141	  year={1969},
142	}
143	
144	% ============================================================
145	% Category 4: Computational Persuasion Detection
146	% ============================================================
147	
148	@book{cialdini2001influence,
149	  title={Influence: Science and Practice},
150	  author={Cialdini, Robert B.},
151	  publisher={Allyn \& Bacon},
152	  year={2001},
153	  edition={4th},
154	}
155	
156	% ============================================================
157	% Category 5: Jailbreak Attacks & Taxonomies
158	% ============================================================
159	
160	@inproceedings{zeng2024pap,
161	  title={How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs},
162	  author={Zeng, Yi and Lin, Hongpeng and Zhang, Jingwen and Yang, Diyi and Jia, Ruoxi and Shi, Weiyan},
163	  booktitle={Proceedings of the Association for Computational Linguistics},
164	  year={2024},
165	}
166	
167	% Note: key retains "2024" for citation compatibility; paper published at USENIX Security 2025
168	@inproceedings{russinovich2024crescendo,
169	  title={Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack},
170	  author={Russinovich, Mark and Salem, Ahmed and Eldan, Ronen},
171	  booktitle={USENIX Security Symposium},
172	  year={2025},
173	  eprint={2404.01833},
174	  archivePrefix={arXiv},
175	}
176	
177	@article{chao2023pair,
178	  title={Jailbreaking Black Box Large Language Models in Twenty Queries},
179	  author={Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pappas, George J. and Wong, Eric},
180	  journal={arXiv preprint},
181	  year={2023},
182	  eprint={2310.08419},
183	  archivePrefix={arXiv},
184	}
185	
186	@inproceedings{wei2023jailbroken,
187	  title={Jailbroken: How Does LLM Safety Training Fail?},
188	  author={Wei, Alexander and Haghtalab, Nika and Steinhardt, Jacob},
189	  booktitle={Advances in Neural Information Processing Systems},
190	  year={2023},
191	}
192	
193	@article{hagendorff2026reasoning,
194	  title={Large Reasoning Models Are Autonomous Jailbreak Agents},
195	  author={Hagendorff, Thilo and Derner, Erik and Oliver, Nuria},
196	  journal={Nature Communications},
197	  year={2026},
198	}
199	
200	@article{fitd2024,
201	  title={Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology},
202	  author={Wang, Zhenhua and Xie, Wei and Wang, Baosheng and Wang, Enze and Gui, Zhiwen and Ma, Shuoyoucheng and Chen, Kai},
203	  journal={arXiv preprint},
204	  year={2024},
205	  eprint={2402.15690},
206	  archivePrefix={arXiv},
207	}
208	
209	@techreport{deceptivedelight2024,
210	  title={Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction},
211	  author={{Palo Alto Networks Unit 42}},
212	  institution={Palo Alto Networks},
213	  year={2024},
214	}
215	
216	@inproceedings{ren2024actorattack,
217	  title={ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory},
218	  author={Ren, Qibing and Li, Hao and Liu, Dongrui and Xie, Zhanxu and Lu, Xiaoya and Qiao, Yu and Sha, Lei and Yan, Junchi and Ma, Lizhuang and Shao, Jing},
219	  booktitle={International Conference on Learning Representations},
220	  year={2025},
221	}
222	
223	@article{zou2023gcg,
224	  title={Universal and Transferable Adversarial Attacks on Aligned Language Models},
225	  author={Zou, Andy and Wang, Zifan and Carlini, Nicholas and Nasr, Milad and Kolter, J. Zico and Fredrikson, Matt},
226	  journal={arXiv preprint},
227	  year={2023},
228	  eprint={2307.15043},
229	  archivePrefix={arXiv},
230	}
231	
232	% ============================================================
233	% Category 6: Red-Teaming
234	% ============================================================
235	
236	@article{li2024mhj,
237	  title={LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet},
238	  author={Li, Nathaniel and Han, Ziwen and Steneker, Ian and Primack, Willow and Goodside, Riley and Zhang, Hugh and Wang, Zifan and Menghini, Cristina and Yue, Summer},
239	  journal={arXiv preprint},
240	  year={2024},
241	  eprint={2408.15221},
242	  archivePrefix={arXiv},
243	}
244	
245	% ============================================================
246	% Category 7: Annotation Artifacts & Dataset Biases
247	% ============================================================
248	
249	@inproceedings{gururangan2018artifacts,
250	  title={Annotation Artifacts in Natural Language Inference Data},
251	  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel and Smith, Noah A.},
252	  booktitle={Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics},
253	  year={2018},
254	}
255	
256	@inproceedings{niven2019probing,
257	  title={Probing Neural Network Comprehension of Natural Language Arguments},
258	  author={Niven, Timothy and Kao, Hung-Yu},
259	  booktitle={Proceedings of the Association for Computational Linguistics},
260	  year={2019},
261	}
262	
263	% ============================================================
264	% Category 8: Adaptive Attacks on Classifiers
265	% ============================================================
266	
267	@article{nasr2025attackermovessecond,
268	  title={The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections},
269	  author={Nasr, Milad and Carlini, Nicholas and Sitawarin, Chawin and Schulhoff, Sander V. and Hayes, Jamie and Ilie, Michael and Pluto, Juliette and Song, Shuang and Chaudhari, Harsh and Shumailov, Ilia and Thakurta, Abhradeep and Xiao, Kai Yuanqing and Terzis, Andreas and Tram{\`e}r, Florian},
270	  journal={arXiv preprint},
271	  year={2025},
272	  eprint={2510.09023},
273	  archivePrefix={arXiv},
274	}
275	
276	@inproceedings{andriushchenko2024adaptive,
277	  title={Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks},
278	  author={Andriushchenko, Maksym and Croce, Francesco and Flammarion, Nicolas},
279	  booktitle={International Conference on Learning Representations},
280	  year={2025},
281	}
282	
283	% ============================================================
284	% Technical Foundation
285	% ============================================================
286	
287	@inproceedings{he2021deberta,
288	  title={DeBERTa: Decoding-enhanced BERT with Disentangled Attention},
289	  author={He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu},
290	  booktitle={International Conference on Learning Representations},
291	  year={2021},
292	}
293	
294	% ============================================================
295	% Domain-Adaptive Pretraining & Multi-Task Learning
296	% ============================================================
297	
298	@inproceedings{gururangan2020dontstop,
299	  title={Don't Stop Pretraining: Adapt Language Models to Domains and Tasks},
300	  author={Gururangan, Suchin and Marasovi{\'c}, Ana and Swayamdipta, Swabha and Lo, Kyle and Beltagy, Iz and Downey, Doug and Smith, Noah A.},
301	  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
302	  pages={8342--8360},
303	  year={2020},
304	}
305	
306	@article{caruana1997multitask,
307	  title={Multitask Learning},
308	  author={Caruana, Rich},
309	  journal={Machine Learning},
310	  volume={28},
311	  number={1},
312	  pages={41--75},
313	  year={1997},
314	}
315	
316	@article{phang2018stilts,
317	  title={Sentence Encoders on {STILTs}: Supplementary Training on Intermediate Labeled-data Tasks},
318	  author={Phang, Jason and F{\'e}vry, Thibault and Bowman, Samuel R.},
319	  journal={arXiv preprint arXiv:1811.01088},
320	  year={2018},
321	}
322	
323	@inproceedings{liu2019mtdnn,
324	  title={Multi-Task Deep Neural Networks for Natural Language Understanding},
325	  author={Liu, Xiaodong and He, Pengcheng and Chen, Weizhu and Gao, Jianfeng},
326	  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
327	  pages={4487--4496},
328	  year={2019},
329	}
330	
331	@inproceedings{howard2018ulmfit,
332	  title={Universal Language Model Fine-tuning for Text Classification},
333	  author={Howard, Jeremy and Ruder, Sebastian},
334	  booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},
335	  pages={328--339},
336	  year={2018},
337	}
338	
339	% ============================================================
340	% Propaganda Detection
341	% ============================================================
342	
343	@inproceedings{dasanmartino2020semeval,
344	  title={{SemEval-2020 Task 11}: Detection of Propaganda Techniques in News Articles},
345	  author={Da San Martino, Giovanni and Barr\'{o}n-Cede\~{n}o, Alberto and Wachsmuth, Henning and Petrov, Rostislav and Nakov, Preslav},
346	  booktitle={Proceedings of the Fourteenth Workshop on Semantic Evaluation},
347	  pages={1377--1414},
348	  year={2020},
349	}
350	
351	@inproceedings{dasanmartino2019fine,
352	  title={Fine-Grained Analysis of Propaganda in News Articles},
353	  author={Da San Martino, Giovanni and Yu, Seunghak and Barr\'{o}n-Cede\~{n}o, Alberto and Petrov, Rostislav and Nakov, Preslav},
354	  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},
355	  pages={5636--5646},
356	  year={2019},
357	}
358	
359	% ============================================================
360	% Adversarial NLP
361	% ============================================================
362	
363	@inproceedings{jin2020textfooler,
364	  title={Is {BERT} Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment},
365	  author={Jin, Di and Jin, Zhijing and Zhou, Joey Tianyi and Szolovits, Peter},
366	  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
367	  volume={34},
368	  pages={8018--8025},
369	  year={2020},
370	}
371	
372	@inproceedings{li2020bertattack,
373	  title={{BERT-ATTACK}: Adversarial Attack Against {BERT} Using {BERT}},
374	  author={Li, Linyang and Ma, Ruotian and Guo, Qipeng and Xue, Xiangyang and Qiu, Xipeng},
375	  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
376	  pages={6193--6202},
377	  year={2020},
378	}
379	
380	% ============================================================
381	% Probing Classifiers
382	% ============================================================
383	
384	@inproceedings{conneau2018probing,
385	  title={What you can cram into a single \$\&!\#* vector: Probing sentence embeddings for linguistic properties},
386	  author={Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo\"{i}c and Baroni, Marco},
387	  booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},
388	  pages={2126--2136},
389	  year={2018},
390	}
391	
392	@inproceedings{hewitt2019structural,
393	  title={A Structural Probe for Finding Syntax in Word Representations},
394	  author={Hewitt, John and Manning, Christopher D.},
395	  booktitle={Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics},
396	  pages={4129--4138},
397	  year={2019},
398	}
399	
400	@article{liu2019roberta,
401	  title={RoBERTa: A Robustly Optimized BERT Pretraining Approach},
402	  author={Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},
403	  journal={arXiv preprint arXiv:1907.11692},
404	  year={2019},
405	}
406	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a18b791-d961-4718-95cf-be5047dae6f0",
  "isSidechain": false,
  "promptId": "f969e597-50af-4667-a32a-e352289d26c2",
  "type": "user",
  "uuid": "14a09188-973d-44ef-b206-117a444511bf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/references.bib",
      "content": "% References for persuasion_turn_jailbreak_detect\n% Auto-generated from literature_map.yaml (2026-05-18)\n% Total entries: 31\n\n% ============================================================\n% Category 1: Production Multi-Turn Safety Systems\n% ============================================================\n\n@article{inan2023llamaguard,\n  title={Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations},\n  author={Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer, Krithika and Mao, Yuning and Tontchev, Michael and Hu, Qing and Fuller, Brian and Testuggine, Davide and Khabsa, Madian},\n  journal={arXiv preprint},\n  year={2023},\n  eprint={2312.06674},\n  archivePrefix={arXiv},\n}\n\n@misc{metallamaguard3_2024,\n  title={Llama Guard 3},\n  author={{Meta AI}},\n  year={2024},\n  howpublished={Meta AI (released with Llama 3.1)},\n}\n\n@article{zeng2024shieldgemma,\n  title={ShieldGemma: Generative AI Content Moderation Based on Gemma},\n  author={Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, Joe and Harkous, Hamza and Narasimhan, Karthik and Proud, Drew and Kumar, Piyush and Radharapu, Bhaktipriya and Sturman, Olivia and Wahltinez, Oscar},\n  journal={arXiv preprint},\n  year={2024},\n  eprint={2407.21772},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{han2024wildguard,\n  title={WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs},\n  author={Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill Yuchen and Lambert, Nathan and Choi, Yejin and Dziri, Nouha},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2024},\n}\n\n@article{anthropic2025constitutional,\n  title={Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming},\n  author={{Anthropic}},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2501.18837},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 2: Multi-Turn Jailbreak Defenses\n% ============================================================\n\n@article{deepcontext2026,\n  title={DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs},\n  author={Albrethsen, Justin and Datta, Yash and Kumar, Kunal and Rajasekar, Sharath},\n  journal={arXiv preprint},\n  year={2026},\n  eprint={2602.16935},\n  archivePrefix={arXiv},\n}\n\n@article{tong2025biid,\n  title={Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks},\n  author={Tong, Haibo and Zhao, Dongcheng and Shen, Guobin and He, Xiang and Lin, Dachuan and Zhao, Feifei and Zeng, Yi},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2509.22732},\n  archivePrefix={arXiv},\n}\n\n@article{gguard2025,\n  title={An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs},\n  author={Huang, Zixuan and Huang, Kecheng and Yin, Lihao and He, Bowei and Zhen, Huiling and Yuan, Mingxuan and Shao, Zili},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2507.07146},\n  archivePrefix={arXiv},\n}\n\n@article{safedream2026,\n  title={SafeDream: Safety World Model for Proactive Early Jailbreak Detection},\n  author={Yan, Bo and Lin, Weikai and Zhu, Yada and Wang, Song},\n  journal={arXiv preprint},\n  year={2026},\n  eprint={2604.16824},\n  archivePrefix={arXiv},\n}\n\n@article{bullwinkel2025repeng,\n  title={A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks},\n  author={Bullwinkel, Blake and Russinovich, Mark and Salem, Ahmed and Zanella-Beguelin, Santiago and Jones, Daniel and Severi, Giorgio and Kim, Eugenia and Hines, Keegan and Minnich, Amanda and Zunger, Yonatan and Kumar, Ram Shankar Siva},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2507.02956},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 3: Discourse Analysis in NLP\n% ============================================================\n\n@article{mann1988rst,\n  title={Rhetorical Structure Theory: Toward a Functional Theory of Text Organization},\n  author={Mann, William C. and Thompson, Sandra A.},\n  journal={Text \\& Talk},\n  year={1988},\n  volume={8},\n  number={3},\n  pages={243--281},\n}\n\n@inproceedings{prasad2008pdtb,\n  title={The Penn Discourse TreeBank 2.0},\n  author={Prasad, Rashmi and Dinesh, Nikhil and Lee, Alan and Miltsakaki, Eleni and Robaldo, Livio and Joshi, Aravind and Webber, Bonnie},\n  booktitle={Proceedings of the International Conference on Language Resources and Evaluation},\n  year={2008},\n}\n\n@article{stolcke2000dialogueact,\n  title={Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech},\n  author={Stolcke, Andreas and Ries, Klaus and Coccaro, Noah and Shriberg, Elizabeth and Bates, Rebecca and Jurafsky, Daniel and Taylor, Paul and Martin, Rachel and Van Ess-Dykema, Carol and Meteer, Marie},\n  journal={Computational Linguistics},\n  year={2000},\n  volume={26},\n  number={3},\n  pages={339--374},\n}\n\n@book{austin1962speechacts,\n  title={How to Do Things with Words},\n  author={Austin, J. L.},\n  publisher={Harvard University Press},\n  year={1962},\n}\n\n@book{searle1969speechacts,\n  title={Speech Acts: An Essay in the Philosophy of Language},\n  author={Searle, J. R.},\n  publisher={Cambridge University Press},\n  year={1969},\n}\n\n% ============================================================\n% Category 4: Computational Persuasion Detection\n% ============================================================\n\n@book{cialdini2001influence,\n  title={Influence: Science and Practice},\n  author={Cialdini, Robert B.},\n  publisher={Allyn \\& Bacon},\n  year={2001},\n  edition={4th},\n}\n\n% ============================================================\n% Category 5: Jailbreak Attacks & Taxonomies\n% ============================================================\n\n@inproceedings{zeng2024pap,\n  title={How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs},\n  author={Zeng, Yi and Lin, Hongpeng and Zhang, Jingwen and Yang, Diyi and Jia, Ruoxi and Shi, Weiyan},\n  booktitle={Proceedings of the Association for Computational Linguistics},\n  year={2024},\n}\n\n% Note: key retains \"2024\" for citation compatibility; paper published at USENIX Security 2025\n@inproceedings{russinovich2024crescendo,\n  title={Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack},\n  author={Russinovich, Mark and Salem, Ahmed and Eldan, Ronen},\n  booktitle={USENIX Security Symposium},\n  year={2025},\n  eprint={2404.01833},\n  archivePrefix={arXiv},\n}\n\n@article{chao2023pair,\n  title={Jailbreaking Black Box Large Language Models in Twenty Queries},\n  author={Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pappas, George J. and Wong, Eric},\n  journal={arXiv preprint},\n  year={2023},\n  eprint={2310.08419},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{wei2023jailbroken,\n  title={Jailbroken: How Does LLM Safety Training Fail?},\n  author={Wei, Alexander and Haghtalab, Nika and Steinhardt, Jacob},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023},\n}\n\n@article{hagendorff2026reasoning,\n  title={Large Reasoning Models Are Autonomous Jailbreak Agents},\n  author={Hagendorff, Thilo and Derner, Erik and Oliver, Nuria},\n  journal={Nature Communications},\n  year={2026},\n}\n\n@article{fitd2024,\n  title={Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology},\n  author={Wang, Zhenhua and Xie, Wei and Wang, Baosheng and Wang, Enze and Gui, Zhiwen and Ma, Shuoyoucheng and Chen, Kai},\n  journal={arXiv preprint},\n  year={2024},\n  eprint={2402.15690},\n  archivePrefix={arXiv},\n}\n\n@techreport{deceptivedelight2024,\n  title={Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction},\n  author={{Palo Alto Networks Unit 42}},\n  institution={Palo Alto Networks},\n  year={2024},\n}\n\n@inproceedings{ren2024actorattack,\n  title={ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory},\n  author={Ren, Qibing and Li, Hao and Liu, Dongrui and Xie, Zhanxu and Lu, Xiaoya and Qiao, Yu and Sha, Lei and Yan, Junchi and Ma, Lizhuang and Shao, Jing},\n  booktitle={International Conference on Learning Representations},\n  year={2025},\n}\n\n@article{zou2023gcg,\n  title={Universal and Transferable Adversarial Attacks on Aligned Language Models},\n  author={Zou, Andy and Wang, Zifan and Carlini, Nicholas and Nasr, Milad and Kolter, J. Zico and Fredrikson, Matt},\n  journal={arXiv preprint},\n  year={2023},\n  eprint={2307.15043},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 6: Red-Teaming\n% ============================================================\n\n@article{li2024mhj,\n  title={LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet},\n  author={Li, Nathaniel and Han, Ziwen and Steneker, Ian and Primack, Willow and Goodside, Riley and Zhang, Hugh and Wang, Zifan and Menghini, Cristina and Yue, Summer},\n  journal={arXiv preprint},\n  year={2024},\n  eprint={2408.15221},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 7: Annotation Artifacts & Dataset Biases\n% ============================================================\n\n@inproceedings{gururangan2018artifacts,\n  title={Annotation Artifacts in Natural Language Inference Data},\n  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel and Smith, Noah A.},\n  booktitle={Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics},\n  year={2018},\n}\n\n@inproceedings{niven2019probing,\n  title={Probing Neural Network Comprehension of Natural Language Arguments},\n  author={Niven, Timothy and Kao, Hung-Yu},\n  booktitle={Proceedings of the Association for Computational Linguistics},\n  year={2019},\n}\n\n% ============================================================\n% Category 8: Adaptive Attacks on Classifiers\n% ============================================================\n\n@article{nasr2025attackermovessecond,\n  title={The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections},\n  author={Nasr, Milad and Carlini, Nicholas and Sitawarin, Chawin and Schulhoff, Sander V. and Hayes, Jamie and Ilie, Michael and Pluto, Juliette and Song, Shuang and Chaudhari, Harsh and Shumailov, Ilia and Thakurta, Abhradeep and Xiao, Kai Yuanqing and Terzis, Andreas and Tram{\\`e}r, Florian},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2510.09023},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{andriushchenko2024adaptive,\n  title={Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks},\n  author={Andriushchenko, Maksym and Croce, Francesco and Flammarion, Nicolas},\n  booktitle={International Conference on Learning Representations},\n  year={2025},\n}\n\n% ============================================================\n% Technical Foundation\n% ============================================================\n\n@inproceedings{he2021deberta,\n  title={DeBERTa: Decoding-enhanced BERT with Disentangled Attention},\n  author={He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu},\n  booktitle={International Conference on Learning Representations},\n  year={2021},\n}\n\n% ============================================================\n% Domain-Adaptive Pretraining & Multi-Task Learning\n% ============================================================\n\n@inproceedings{gururangan2020dontstop,\n  title={Don't Stop Pretraining: Adapt Language Models to Domains and Tasks},\n  author={Gururangan, Suchin and Marasovi{\\'c}, Ana and Swayamdipta, Swabha and Lo, Kyle and Beltagy, Iz and Downey, Doug and Smith, Noah A.},\n  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n  pages={8342--8360},\n  year={2020},\n}\n\n@article{caruana1997multitask,\n  title={Multitask Learning},\n  author={Caruana, Rich},\n  journal={Machine Learning},\n  volume={28},\n  number={1},\n  pages={41--75},\n  year={1997},\n}\n\n@article{phang2018stilts,\n  title={Sentence Encoders on {STILTs}: Supplementary Training on Intermediate Labeled-data Tasks},\n  author={Phang, Jason and F{\\'e}vry, Thibault and Bowman, Samuel R.},\n  journal={arXiv preprint arXiv:1811.01088},\n  year={2018},\n}\n\n@inproceedings{liu2019mtdnn,\n  title={Multi-Task Deep Neural Networks for Natural Language Understanding},\n  author={Liu, Xiaodong and He, Pengcheng and Chen, Weizhu and Gao, Jianfeng},\n  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n  pages={4487--4496},\n  year={2019},\n}\n\n@inproceedings{howard2018ulmfit,\n  title={Universal Language Model Fine-tuning for Text Classification},\n  author={Howard, Jeremy and Ruder, Sebastian},\n  booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n  pages={328--339},\n  year={2018},\n}\n\n% ============================================================\n% Propaganda Detection\n% ============================================================\n\n@inproceedings{dasanmartino2020semeval,\n  title={{SemEval-2020 Task 11}: Detection of Propaganda Techniques in News Articles},\n  author={Da San Martino, Giovanni and Barr\\'{o}n-Cede\\~{n}o, Alberto and Wachsmuth, Henning and Petrov, Rostislav and Nakov, Preslav},\n  booktitle={Proceedings of the Fourteenth Workshop on Semantic Evaluation},\n  pages={1377--1414},\n  year={2020},\n}\n\n@inproceedings{dasanmartino2019fine,\n  title={Fine-Grained Analysis of Propaganda in News Articles},\n  author={Da San Martino, Giovanni and Yu, Seunghak and Barr\\'{o}n-Cede\\~{n}o, Alberto and Petrov, Rostislav and Nakov, Preslav},\n  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages={5636--5646},\n  year={2019},\n}\n\n% ============================================================\n% Adversarial NLP\n% ============================================================\n\n@inproceedings{jin2020textfooler,\n  title={Is {BERT} Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment},\n  author={Jin, Di and Jin, Zhijing and Zhou, Joey Tianyi and Szolovits, Peter},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},\n  volume={34},\n  pages={8018--8025},\n  year={2020},\n}\n\n@inproceedings{li2020bertattack,\n  title={{BERT-ATTACK}: Adversarial Attack Against {BERT} Using {BERT}},\n  author={Li, Linyang and Ma, Ruotian and Guo, Qipeng and Xue, Xiangyang and Qiu, Xipeng},\n  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n  pages={6193--6202},\n  year={2020},\n}\n\n% ============================================================\n% Probing Classifiers\n% ============================================================\n\n@inproceedings{conneau2018probing,\n  title={What you can cram into a single \\$\\&!\\#* vector: Probing sentence embeddings for linguistic properties},\n  author={Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo\\\"{i}c and Baroni, Marco},\n  booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n  pages={2126--2136},\n  year={2018},\n}\n\n@inproceedings{hewitt2019structural,\n  title={A Structural Probe for Finding Syntax in Word Representations},\n  author={Hewitt, John and Manning, Christopher D.},\n  booktitle={Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics},\n  pages={4129--4138},\n  year={2019},\n}\n\n@article{liu2019roberta,\n  title={RoBERTa: A Robustly Optimized BERT Pretraining Approach},\n  author={Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},\n  journal={arXiv preprint arXiv:1907.11692},\n  year={2019},\n}\n",
      "numLines": 406,
      "startLine": 1,
      "totalLines": 406
    }
  },
  "sourceToolAssistantUUID": "2a18b791-d961-4718-95cf-be5047dae6f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T15:52:29.815Z_

<details><summary>↩ Tool result · `toolu_019F97knsKVcHK7yJNDbp2D7`</summary>

```text
1	% appendix.tex — Supplementary material
2	
3	\appendix
4	
5	\section{LLM-as-Judge Baseline}
6	\label{sec:llm_judge}
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{LLM-as-judge zero-shot jailbreak detection (F1). IID: Crescendo test set; OOD: Deceptive Delight (DD) and FITD. F1 values for GPT-5.5 and Qwen3-8B exclude unparseable responses and represent upper bounds.}
12	\label{tab:llm_judge}
13	\begin{tabular}{@{}lccccr@{}}
14	\toprule
15	\textbf{Method} & $K$=2 & $K$=3 & $K$=5 & Full & Unparse. \\
16	\midrule
17	\multicolumn{6}{l}{\textit{IID (Crescendo)}} \\[2pt]
18	GPT-5.5 & .191 & .273 & .449 & .383 & 30--47\% \\
19	Qwen3-8B & .000 & .051 & .146 & .100 & 0\% \\
20	9-class (ours) & \textbf{1.000} & \textbf{1.000} & \textbf{1.000} & \textbf{1.000} & 0\% \\
21	\midrule
22	\multicolumn{6}{l}{\textit{OOD (Deceptive Delight)}} \\[2pt]
23	Qwen3-8B & .000 & .000 & .000 & .000 & 0\% \\
24	9-class (ours) & \textbf{.981} & \textbf{.972} & \textbf{.997} & \textbf{.997} & 0\% \\
25	\midrule
26	\multicolumn{6}{l}{\textit{OOD (FITD)}} \\[2pt]
27	Qwen3-8B & .000 & .000 & .025 & .025 & 0\% \\
28	9-class (ours) & \textbf{1.000} & -- & -- & \textbf{1.000} & 0\% \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
33	Table~\ref{tab:llm_judge} reports zero-shot performance for GPT-5.5 and Qwen3-8B on IID and OOD data.
34	On IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 of 0.191 at $K$=2 and 0.449 at $K$=5.
35	A substantial fraction (30--47\%) of responses are unparseable; F1 values exclude these and represent upper bounds.
36	Full-conversation F1 (0.383) is lower than $K$=5 F1 (0.449) because the unparseable rate grows with context length.
37	Qwen3-8B performs worse across all IID prefixes (F1 from 0.000 at $K$=2 to 0.100 on full conversations).
38	On OOD data, Qwen3-8B predicts all conversations as benign (F1 = 0.0 on DD, F1 = 0.025 on FITD), while DisPeD maintains F1 $\geq$ 0.997 on DD and F1 = 1.000 on FITD.
39	The complete failure of content-level reasoning on unseen attack types underscores the necessity of trained discourse-aware classifiers.
40	
41	\section{Full Cross-Attack Results by Prefix}
42	\label{sec:full_prefix}
43	
44	\begin{table*}[t]
45	\centering
46	\small
47	\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\pm$std where available.}
48	\label{tab:full_prefix}
49	\begin{tabular}{@{}lccccc@{}}
50	\toprule
51	\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\
52	\midrule
53	\multicolumn{6}{l}{\textit{IID (Crescendo)}} \\[2pt]
54	9-class (ours) & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 \\
55	MLM-only & .960 & .974 & .987 & 1.000 & 1.000 \\
56	Vanilla DeBERTa & .968$\pm$.033 & .978$\pm$.016 & .987$\pm$.000 & .982$\pm$.014 & 1.000$\pm$.000 \\
57	TF-IDF LR & 1.000 & 1.000 & 1.000 & 1.000 & 1.000 \\
58	\midrule
59	\multicolumn{6}{l}{\textit{OOD (Deceptive Delight)}} \\[2pt]
60	9-class (ours) & .990$\pm$.013 & .981$\pm$.013 & .972$\pm$.026 & .997$\pm$.005 & .997$\pm$.005 \\
61	Binary & .994$\pm$.009 & .994$\pm$.009 & .984$\pm$.008 & 1.000$\pm$.000 & .997$\pm$.005 \\
62	Scrambled & .997$\pm$.005 & .981$\pm$.026 & .975$\pm$.029 & .997$\pm$.005 & .997$\pm$.005 \\
63	MLM-only & .973$\pm$.019 & .993$\pm$.009 & .997$\pm$.005 & .997$\pm$.005 & .914$\pm$.115 \\
64	Vanilla DeBERTa & .628$\pm$.038 & .479$\pm$.038 & .389$\pm$.027 & .351$\pm$.030 & .312$\pm$.026 \\
65	TF-IDF LR & -- & -- & -- & -- & .944 \\
66	\midrule
67	\multicolumn{6}{l}{\textit{OOD (FITD)}} \\[2pt]
68	9-class (ours) & 1.000 & 1.000 & -- & -- & 1.000 \\
69	Vanilla DeBERTa & .990 & 1.000 & -- & -- & 1.000 \\
70	TF-IDF LR & 1.000 & -- & -- & -- & 1.000 \\
71	\bottomrule
72	\end{tabular}
73	\end{table*}
74	
75	\section{ActorAttack Full Results}
76	\label{sec:actorattack_full}
77	
78	\begin{table*}[t]
79	\centering
80	\small
81	\caption{Full ActorAttack OOD results (F1) at all prefix lengths. 3-seed mean$\pm$std (Binary per-$K$ reports $n$=2; Full is 3-seed).}
82	\label{tab:actorattack_full}
83	\begin{tabular}{@{}lccccc@{}}
84	\toprule
85	\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\
86	\midrule
87	\multicolumn{6}{l}{\textit{DeBERTa-v3}} \\[2pt]
88	Binary & .788$\pm$.020 & \textbf{.935$\pm$.018} & \textbf{.976$\pm$.005} & \textbf{.995$\pm$.005} & \textbf{.990$\pm$.008} \\
89	9-class & .773$\pm$.041 & .855$\pm$.048 & .921$\pm$.046 & .966$\pm$.028 & .972$\pm$.026 \\
90	Scrambled & .652$\pm$.034 & .804$\pm$.053 & .854$\pm$.046 & .910$\pm$.052 & .951$\pm$.043 \\
91	MLM-only & .736$\pm$.150 & .909$\pm$.058 & .945$\pm$.039 & .929$\pm$.033 & .893$\pm$.080 \\
92	Wiki MLM & .656$\pm$.224 & .672$\pm$.252 & .693$\pm$.280 & .689$\pm$.285 & .686$\pm$.297 \\
93	Topic & .513$\pm$.077 & .580$\pm$.109 & .565$\pm$.100 & .615$\pm$.111 & .625$\pm$.141 \\
94	Vanilla & .337$\pm$.049 & .306$\pm$.026 & .284$\pm$.011 & .262$\pm$.006 & .258$\pm$.000 \\
95	\midrule
96	\multicolumn{6}{l}{\textit{RoBERTa}} \\[2pt]
97	9-class & \textbf{.738$\pm$.033} & .805$\pm$.033 & .884$\pm$.066 & .925$\pm$.066 & .939$\pm$.046 \\
98	MLM & .633$\pm$.133 & .665$\pm$.150 & .713$\pm$.174 & .719$\pm$.184 & .730$\pm$.201 \\
99	Vanilla & .410$\pm$.126 & .425$\pm$.143 & .432$\pm$.144 & .466$\pm$.144 & .466$\pm$.163 \\
100	\bottomrule
101	\end{tabular}
102	\end{table*}
103	
104	\section{OOD Perturbation Robustness}
105	\label{sec:ood_perturbation}
106	
107	\begin{table}[t]
108	\centering
109	\small
110	\caption{Perturbation robustness on OOD Deceptive Delight ($n$=118). $\Delta$: F1 change (pp) from clean to paraphrased. 3-seed mean$\pm$std where available.}
111	\label{tab:ood_perturbation}
112	\begin{tabular}{@{}lcccc@{}}
113	\toprule
114	\textbf{Variant} & Clean Full & Pert.\ Full & $\Delta$ Full & $\Delta$ $K$=1 \\
115	\midrule
116	9-class & .997$\pm$.005 & 1.000$\pm$.000 & +0.3 & +0.6 \\
117	Binary & .997$\pm$.005 & 1.000$\pm$.000 & +0.3 & +0.6 \\
118	Scrambled & .997$\pm$.005 & 1.000$\pm$.000 & +0.3 & $-$0.3 \\
119	\midrule
120	JB MLM & .914$\pm$.115 & .941 & +2.7 & 0.0 \\
121	Wiki MLM$^{*}$ & .904$\pm$.115 & .872 & $-$3.3 & $-$3.2 \\
122	Vanilla$^{\dagger}$ & .312$\pm$.026 & .339$\pm$.055 & +2.7 & $-$6.8$\pm$1.1 \\
123	\bottomrule
124	\end{tabular}
125	\vspace{-2pt}
126	{\footnotesize $^{*}$Wiki MLM degradation is seed-driven: seed 42 accounts for $-$9.8\,pp; other seeds show 0.0\,pp change.\\$^{\dagger}$Vanilla $\Delta$ Full = +2.7\,pp reflects floor-effect noise (baseline 0.312, std 0.055), not meaningful improvement.}
127	\end{table}
128	
129	\section{Reproducibility Details}
130	\label{sec:reproducibility}
131	
132	\paragraph{Stage-1 training.}
133	All variants use DeBERTa-v3-base (184M parameters) with learning rate $2 \times 10^{-5}$, AdamW optimizer ($\beta_1$=0.9, $\beta_2$=0.999, weight decay 0.01), linear warmup over the first 10\% of steps, batch size 16, and 4 epochs. MLM variants use 15\% random token masking. Training takes approximately 30 minutes per variant on a single NVIDIA A100 (40GB).
134	
135	\paragraph{Stage-2 training.}
136	The BiGRU has hidden dimension 128 (bidirectional, so output dimension 256). The MLP classifier has layers $256 \to 64 \to 2$ with ReLU activation and dropout 0.3. Training uses learning rate $1 \times 10^{-3}$, Adam optimizer, batch size 32, and 20 epochs with early stopping (patience 5) on validation F1. Stage-2 training completes in under 5 minutes per variant.
137	
138	\paragraph{Data generation.}
139	Jailbreak conversations are generated using Qwen3-8B with attack-specific prompt templates. Crescendo conversations follow a 5--8 turn gradual escalation structure. FITD conversations use a 2--3 turn commitment-consistency structure. Deceptive Delight conversations embed harmful content within emotionally engaging 3--5 turn sequences. Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general) with matched turn counts.
140	
141	\paragraph{Strategy annotation.}
142	Each user turn is annotated by Qwen3-8B using a structured prompt that provides definitions and two examples for each of the nine strategy categories. The prompt instructs the model to output a single category label. We plan to release all generation and annotation prompts, the full dataset, and training code upon acceptance.
143	
144	\paragraph{Adversarial paraphrasing.}
145	The paraphrased test set is generated by instructing Qwen3-8B to rephrase each user turn while preserving the communicative intent. The resulting paraphrases have mean BERTScore 0.92 and mean lexical overlap 0.20 with the originals. These metrics confirm substantial surface-level variation.
146	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acafeeac-1082-4667-9ca1-b30d4122d838",
  "isSidechain": false,
  "promptId": "f969e597-50af-4667-a32a-e352289d26c2",
  "type": "user",
  "uuid": "37340063-ab16-4557-9e84-95a00adbdf45",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
      "content": "% appendix.tex — Supplementary material\n\n\\appendix\n\n\\section{LLM-as-Judge Baseline}\n\\label{sec:llm_judge}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LLM-as-judge zero-shot jailbreak detection (F1). IID: Crescendo test set; OOD: Deceptive Delight (DD) and FITD. F1 values for GPT-5.5 and Qwen3-8B exclude unparseable responses and represent upper bounds.}\n\\label{tab:llm_judge}\n\\begin{tabular}{@{}lccccr@{}}\n\\toprule\n\\textbf{Method} & $K$=2 & $K$=3 & $K$=5 & Full & Unparse. \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{IID (Crescendo)}} \\\\[2pt]\nGPT-5.5 & .191 & .273 & .449 & .383 & 30--47\\% \\\\\nQwen3-8B & .000 & .051 & .146 & .100 & 0\\% \\\\\n9-class (ours) & \\textbf{1.000} & \\textbf{1.000} & \\textbf{1.000} & \\textbf{1.000} & 0\\% \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{OOD (Deceptive Delight)}} \\\\[2pt]\nQwen3-8B & .000 & .000 & .000 & .000 & 0\\% \\\\\n9-class (ours) & \\textbf{.981} & \\textbf{.972} & \\textbf{.997} & \\textbf{.997} & 0\\% \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{OOD (FITD)}} \\\\[2pt]\nQwen3-8B & .000 & .000 & .025 & .025 & 0\\% \\\\\n9-class (ours) & \\textbf{1.000} & -- & -- & \\textbf{1.000} & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:llm_judge} reports zero-shot performance for GPT-5.5 and Qwen3-8B on IID and OOD data.\nOn IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 of 0.191 at $K$=2 and 0.449 at $K$=5.\nA substantial fraction (30--47\\%) of responses are unparseable; F1 values exclude these and represent upper bounds.\nFull-conversation F1 (0.383) is lower than $K$=5 F1 (0.449) because the unparseable rate grows with context length.\nQwen3-8B performs worse across all IID prefixes (F1 from 0.000 at $K$=2 to 0.100 on full conversations).\nOn OOD data, Qwen3-8B predicts all conversations as benign (F1 = 0.0 on DD, F1 = 0.025 on FITD), while DisPeD maintains F1 $\\geq$ 0.997 on DD and F1 = 1.000 on FITD.\nThe complete failure of content-level reasoning on unseen attack types underscores the necessity of trained discourse-aware classifiers.\n\n\\section{Full Cross-Attack Results by Prefix}\n\\label{sec:full_prefix}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\\pm$std where available.}\n\\label{tab:full_prefix}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{IID (Crescendo)}} \\\\[2pt]\n9-class (ours) & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 \\\\\nMLM-only & .960 & .974 & .987 & 1.000 & 1.000 \\\\\nVanilla DeBERTa & .968$\\pm$.033 & .978$\\pm$.016 & .987$\\pm$.000 & .982$\\pm$.014 & 1.000$\\pm$.000 \\\\\nTF-IDF LR & 1.000 & 1.000 & 1.000 & 1.000 & 1.000 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{OOD (Deceptive Delight)}} \\\\[2pt]\n9-class (ours) & .990$\\pm$.013 & .981$\\pm$.013 & .972$\\pm$.026 & .997$\\pm$.005 & .997$\\pm$.005 \\\\\nBinary & .994$\\pm$.009 & .994$\\pm$.009 & .984$\\pm$.008 & 1.000$\\pm$.000 & .997$\\pm$.005 \\\\\nScrambled & .997$\\pm$.005 & .981$\\pm$.026 & .975$\\pm$.029 & .997$\\pm$.005 & .997$\\pm$.005 \\\\\nMLM-only & .973$\\pm$.019 & .993$\\pm$.009 & .997$\\pm$.005 & .997$\\pm$.005 & .914$\\pm$.115 \\\\\nVanilla DeBERTa & .628$\\pm$.038 & .479$\\pm$.038 & .389$\\pm$.027 & .351$\\pm$.030 & .312$\\pm$.026 \\\\\nTF-IDF LR & -- & -- & -- & -- & .944 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{OOD (FITD)}} \\\\[2pt]\n9-class (ours) & 1.000 & 1.000 & -- & -- & 1.000 \\\\\nVanilla DeBERTa & .990 & 1.000 & -- & -- & 1.000 \\\\\nTF-IDF LR & 1.000 & -- & -- & -- & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{ActorAttack Full Results}\n\\label{sec:actorattack_full}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Full ActorAttack OOD results (F1) at all prefix lengths. 3-seed mean$\\pm$std (Binary per-$K$ reports $n$=2; Full is 3-seed).}\n\\label{tab:actorattack_full}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{DeBERTa-v3}} \\\\[2pt]\nBinary & .788$\\pm$.020 & \\textbf{.935$\\pm$.018} & \\textbf{.976$\\pm$.005} & \\textbf{.995$\\pm$.005} & \\textbf{.990$\\pm$.008} \\\\\n9-class & .773$\\pm$.041 & .855$\\pm$.048 & .921$\\pm$.046 & .966$\\pm$.028 & .972$\\pm$.026 \\\\\nScrambled & .652$\\pm$.034 & .804$\\pm$.053 & .854$\\pm$.046 & .910$\\pm$.052 & .951$\\pm$.043 \\\\\nMLM-only & .736$\\pm$.150 & .909$\\pm$.058 & .945$\\pm$.039 & .929$\\pm$.033 & .893$\\pm$.080 \\\\\nWiki MLM & .656$\\pm$.224 & .672$\\pm$.252 & .693$\\pm$.280 & .689$\\pm$.285 & .686$\\pm$.297 \\\\\nTopic & .513$\\pm$.077 & .580$\\pm$.109 & .565$\\pm$.100 & .615$\\pm$.111 & .625$\\pm$.141 \\\\\nVanilla & .337$\\pm$.049 & .306$\\pm$.026 & .284$\\pm$.011 & .262$\\pm$.006 & .258$\\pm$.000 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RoBERTa}} \\\\[2pt]\n9-class & \\textbf{.738$\\pm$.033} & .805$\\pm$.033 & .884$\\pm$.066 & .925$\\pm$.066 & .939$\\pm$.046 \\\\\nMLM & .633$\\pm$.133 & .665$\\pm$.150 & .713$\\pm$.174 & .719$\\pm$.184 & .730$\\pm$.201 \\\\\nVanilla & .410$\\pm$.126 & .425$\\pm$.143 & .432$\\pm$.144 & .466$\\pm$.144 & .466$\\pm$.163 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{OOD Perturbation Robustness}\n\\label{sec:ood_perturbation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Perturbation robustness on OOD Deceptive Delight ($n$=118). $\\Delta$: F1 change (pp) from clean to paraphrased. 3-seed mean$\\pm$std where available.}\n\\label{tab:ood_perturbation}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Variant} & Clean Full & Pert.\\ Full & $\\Delta$ Full & $\\Delta$ $K$=1 \\\\\n\\midrule\n9-class & .997$\\pm$.005 & 1.000$\\pm$.000 & +0.3 & +0.6 \\\\\nBinary & .997$\\pm$.005 & 1.000$\\pm$.000 & +0.3 & +0.6 \\\\\nScrambled & .997$\\pm$.005 & 1.000$\\pm$.000 & +0.3 & $-$0.3 \\\\\n\\midrule\nJB MLM & .914$\\pm$.115 & .941 & +2.7 & 0.0 \\\\\nWiki MLM$^{*}$ & .904$\\pm$.115 & .872 & $-$3.3 & $-$3.2 \\\\\nVanilla$^{\\dagger}$ & .312$\\pm$.026 & .339$\\pm$.055 & +2.7 & $-$6.8$\\pm$1.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\footnotesize $^{*}$Wiki MLM degradation is seed-driven: seed 42 accounts for $-$9.8\\,pp; other seeds show 0.0\\,pp change.\\\\$^{\\dagger}$Vanilla $\\Delta$ Full = +2.7\\,pp reflects floor-effect noise (baseline 0.312, std 0.055), not meaningful improvement.}\n\\end{table}\n\n\\section{Reproducibility Details}\n\\label{sec:reproducibility}\n\n\\paragraph{Stage-1 training.}\nAll variants use DeBERTa-v3-base (184M parameters) with learning rate $2 \\times 10^{-5}$, AdamW optimizer ($\\beta_1$=0.9, $\\beta_2$=0.999, weight decay 0.01), linear warmup over the first 10\\% of steps, batch size 16, and 4 epochs. MLM variants use 15\\% random token masking. Training takes approximately 30 minutes per variant on a single NVIDIA A100 (40GB).\n\n\\paragraph{Stage-2 training.}\nThe BiGRU has hidden dimension 128 (bidirectional, so output dimension 256). The MLP classifier has layers $256 \\to 64 \\to 2$ with ReLU activation and dropout 0.3. Training uses learning rate $1 \\times 10^{-3}$, Adam optimizer, batch size 32, and 20 epochs with early stopping (patience 5) on validation F1. Stage-2 training completes in under 5 minutes per variant.\n\n\\paragraph{Data generation.}\nJailbreak conversations are generated using Qwen3-8B with attack-specific prompt templates. Crescendo conversations follow a 5--8 turn gradual escalation structure. FITD conversations use a 2--3 turn commitment-consistency structure. Deceptive Delight conversations embed harmful content within emotionally engaging 3--5 turn sequences. Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general) with matched turn counts.\n\n\\paragraph{Strategy annotation.}\nEach user turn is annotated by Qwen3-8B using a structured prompt that provides definitions and two examples for each of the nine strategy categories. The prompt instructs the model to output a single category label. We plan to release all generation and annotation prompts, the full dataset, and training code upon acceptance.\n\n\\paragraph{Adversarial paraphrasing.}\nThe paraphrased test set is generated by instructing Qwen3-8B to rephrase each user turn while preserving the communicative intent. The resulting paraphrases have mean BERTScore 0.92 and mean lexical overlap 0.20 with the originals. These metrics confirm substantial surface-level variation.\n",
      "numLines": 146,
      "startLine": 1,
      "totalLines": 146
    }
  },
  "sourceToolAssistantUUID": "acafeeac-1082-4667-9ca1-b30d4122d838",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T15:52:30.045Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N6niwWyK9AJq9T6Tr3zpGy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37340063-ab16-4557-9e84-95a00adbdf45",
  "isSidechain": false,
  "requestId": "req_011CbAJVzvr5H7uF1wycZHTQ",
  "type": "assistant",
  "uuid": "2a18b791-d961-4718-95cf-be5047dae6f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PLp453zH277ojxSJSKnviM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 11720,
      "cache_creation_input_tokens": 3247,
      "cache_read_input_tokens": 30549,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 11720,
          "output_tokens": 247,
          "cache_read_input_tokens": 30549,
          "cache_creation_input_tokens": 3247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3247
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: 你负责审查**方法严谨性、实验设计和统计有效性**。  ## 论文信息 - **标题**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap - **目标 venue**: EMNLP 2026（ARR May cycle） - **De…",
  "leafUuid": "14a09188-973d-44ef-b206-117a444511bf",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multi-turn jailbreak detection paper methodology",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

### Assistant

_source line 42 · 2026-05-18T15:52:33.790Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the official ACL ARR review form to get exact scoring criteria, and also verify the references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14a09188-973d-44ef-b206-117a444511bf",
  "isSidechain": false,
  "requestId": "req_011CbAJWPTgC8kM8LUQbNxvy",
  "type": "assistant",
  "uuid": "8ffbebed-9dbc-4ab8-91eb-a3f57cb404f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWQURXNvi4jvqv4yZQ6n3u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23374,
      "cache_read_input_tokens": 33796,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 327,
          "cache_read_input_tokens": 33796,
          "cache_creation_input_tokens": 23374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23374
          },
          "type": "message"
        }
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

_source line 43 · 2026-05-18T15:52:34.765Z_

论文已通读完毕。让我获取 ARR review form 的详细评分标准，同时验证引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ffbebed-9dbc-4ab8-91eb-a3f57cb404f9",
  "isSidechain": false,
  "requestId": "req_011CbAJWPTgC8kM8LUQbNxvy",
  "type": "assistant",
  "uuid": "59e81fa9-f8c8-4c73-978c-2513c2013c0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWQURXNvi4jvqv4yZQ6n3u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23374,
      "cache_read_input_tokens": 33796,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 327,
          "cache_read_input_tokens": 33796,
          "cache_creation_input_tokens": 23374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23374
          },
          "type": "message"
        }
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

_source line 44 · 2026-05-18T15:52:37.800Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SbAEnguvFM3Xc4WdCez9r9`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract all reviewer guidelines, especially: (1) what reviewers should focus on, (2) scoring criteria and scales for soundness/excitement/overall, (3) what constitutes a good vs bad review, (4) any specific instructions about reproducibility, statistical testing, experimental design assessment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59e81fa9-f8c8-4c73-978c-2513c2013c0a",
  "isSidechain": false,
  "requestId": "req_011CbAJWPTgC8kM8LUQbNxvy",
  "type": "assistant",
  "uuid": "8e018e98-a221-479d-8e82-bbb8f199aa35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWQURXNvi4jvqv4yZQ6n3u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23374,
      "cache_read_input_tokens": 33796,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 327,
          "cache_read_input_tokens": 33796,
          "cache_creation_input_tokens": 23374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23374
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-18T15:52:39.279Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01ABcLNPXfXtDgDjQzQKETP2`</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e018e98-a221-479d-8e82-bbb8f199aa35",
  "isSidechain": false,
  "requestId": "req_011CbAJWPTgC8kM8LUQbNxvy",
  "type": "assistant",
  "uuid": "89bafa13-7921-418c-8986-cd3872f7277b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWQURXNvi4jvqv4yZQ6n3u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23374,
      "cache_read_input_tokens": 33796,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 327,
          "cache_read_input_tokens": 33796,
          "cache_creation_input_tokens": 23374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23374
          },
          "type": "message"
        }
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

_source line 46 · 2026-05-18T15:52:45.851Z_

<details><summary>↩ Tool result · `toolu_01SbAEnguvFM3Xc4WdCez9r9`</summary>

```text
# ARR Reviewer Guidelines: Key Focus Areas

## What Reviewers Should Focus On

Reviewers should prioritize **technical soundness, clarity, and appropriate contribution scope**. Key areas include:

- Reading papers twice: initial skim to assess research question merit, then in-depth evaluation
- Checking expertise and potential conflicts of interest before accepting assignments
- Verifying papers aren't desk-rejection candidates (anonymity violations, missing limitations, style issues)
- Assessing methodology, reproducibility, and experimental design rigor
- Evaluating novelty relative to prior work published 3+ months before submission

## Scoring Criteria

As of February 2025, ARR uses three scores:

1. **Soundness**: Technical correctness and rigor. Must be justified by review text. Low scores require explicit faults identified.

2. **Excitement**: Personal interest level, orthogonal to soundness. Reflects subjective taste without requiring explicit justification.

3. **Overall Assessment**: Composite recommendation for conference acceptance. Reflects soundness, excitement, novelty, and potential impact.

## Good vs. Bad Reviews

**Good reviews are:**
- Specific with concrete examples and line references
- Professional and neutral in tone
- Acknowledge authors' responses and update assessments accordingly
- Avoid common reviewer biases (heuristics H1-H17 outlined in guidelines)

**Bad reviews exhibit:**
- Vague criticisms without evidence (e.g., "not clear" without specifying what)
- Dismissive or sarcastic language
- Failure to read author responses
- Reliance on unconscious biases or inappropriate expectations

## Reproducibility & Experimental Design

Reviewers should verify:

- **Sufficient implementation details** for experiment reproduction, including hyperparameter selection
- **Code/data availability** plans with clear transparency about what will be released
- **Statistical significance testing** with error bars, confidence intervals, or formal significance tests
- **Appropriate baseline comparisons** properly tuned for fair evaluation
- **Disclosure of all design choices**, avoiding p-hacking or selective result reporting

Guidelines emphasize reviewers aren't obligated to run code but should assess whether sufficient documentation exists for reproducibility.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e018e98-a221-479d-8e82-bbb8f199aa35",
  "isSidechain": false,
  "promptId": "f969e597-50af-4667-a32a-e352289d26c2",
  "type": "user",
  "uuid": "29910b58-16f4-4b30-9b7e-046560fb5c6b",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Reviewer Guidelines: Key Focus Areas\n\n## What Reviewers Should Focus On\n\nReviewers should prioritize **technical soundness, clarity, and appropriate contribution scope**. Key areas include:\n\n- Reading papers twice: initial skim to assess research question merit, then in-depth evaluation\n- Checking expertise and potential conflicts of interest before accepting assignments\n- Verifying papers aren't desk-rejection candidates (anonymity violations, missing limitations, style issues)\n- Assessing methodology, reproducibility, and experimental design rigor\n- Evaluating novelty relative to prior work published 3+ months before submission\n\n## Scoring Criteria\n\nAs of February 2025, ARR uses three scores:\n\n1. **Soundness**: Technical correctness and rigor. Must be justified by review text. Low scores require explicit faults identified.\n\n2. **Excitement**: Personal interest level, orthogonal to soundness. Reflects subjective taste without requiring explicit justification.\n\n3. **Overall Assessment**: Composite recommendation for conference acceptance. Reflects soundness, excitement, novelty, and potential impact.\n\n## Good vs. Bad Reviews\n\n**Good reviews are:**\n- Specific with concrete examples and line references\n- Professional and neutral in tone\n- Acknowledge authors' responses and update assessments accordingly\n- Avoid common reviewer biases (heuristics H1-H17 outlined in guidelines)\n\n**Bad reviews exhibit:**\n- Vague criticisms without evidence (e.g., \"not clear\" without specifying what)\n- Dismissive or sarcastic language\n- Failure to read author responses\n- Reliance on unconscious biases or inappropriate expectations\n\n## Reproducibility & Experimental Design\n\nReviewers should verify:\n\n- **Sufficient implementation details** for experiment reproduction, including hyperparameter selection\n- **Code/data availability** plans with clear transparency about what will be released\n- **Statistical significance testing** with error bars, confidence intervals, or formal significance tests\n- **Appropriate baseline comparisons** properly tuned for fair evaluation\n- **Disclosure of all design choices**, avoiding p-hacking or selective result reporting\n\nGuidelines emphasize reviewers aren't obligated to run code but should assess whether sufficient documentation exists for reproducibility.",
    "durationMs": 8048,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "8e018e98-a221-479d-8e82-bbb8f199aa35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-18T15:53:53.076Z_

<details><summary>↩ Tool result · `toolu_01ABcLNPXfXtDgDjQzQKETP2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 43, \"total_citations\": 77, \"unique_cited_keys\": 43, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 28, \"online_not_found\": 8, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"inan2023llamaguard\", \"type\": \"article\", \"title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"authors\": \"Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer,...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"metallamaguard3_2024\", \"type\": \"misc\", \"title\": \"Llama Guard 3\", \"authors\": \"Meta AI\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"zeng2024shieldgemma\", \"type\": \"article\", \"title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"authors\": \"Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"han2024wildguard\", \"type\": \"inproceedings\", \"title\": \"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"authors\": \"Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"anthropic2025constitutional\", \"type\": \"article\", \"title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"authors\": \"Anthropic\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"deepcontext2026\", \"type\": \"article\", \"title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"authors\": \"Albrethsen, Justin and Datta, Yash and Kumar, Kunal and Rajasekar, Sharath\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"tong2025biid\", \"type\": \"article\", \"title\": \"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\", \"authors\": \"Tong, Haibo and Zhao, Dongcheng and Shen, Guobin and He, Xiang and Lin, Dachuan ...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"gguard2025\", \"type\": \"article\", \"title\": \"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\", \"authors\": \"Huang, Zixuan and Huang, Kecheng and Yin, Lihao and He, Bowei and Zhen, Huiling ...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"safedream2026\", \"type\": \"article\", \"title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"authors\": \"Yan, Bo and Lin, Weikai and Zhu, Yada and Wang, Song\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"bullwinkel2025repeng\", \"type\": \"article\", \"title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"authors\": \"Bullwinkel, Blake and Russinovich, Mark and Salem, Ahmed and Zanella-Beguelin, S...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"mann1988rst\", \"type\": \"article\", \"title\": \"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\", \"authors\": \"Mann, William C. and Thompson, Sandra A.\", \"year\": \"1988\", \"venue\": \"Text \\\\& Talk\"}, {\"key\": \"prasad2008pdtb\", \"type\": \"inproceedings\", \"title\": \"The Penn Discourse TreeBank 2.0\", \"authors\": \"Prasad, Rashmi and Dinesh, Nikhil and Lee, Alan and Miltsakaki, Eleni and Robald...\", \"year\": \"2008\", \"venue\": \"Proceedings of the International Conference on Language Resources and Evaluation\"}, {\"key\": \"stolcke2000dialogueact\", \"type\": \"article\", \"title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"authors\": \"Stolcke, Andreas and Ries, Klaus and Coccaro, Noah and Shriberg, Elizabeth and B...\", \"year\": \"2000\", \"venue\": \"Computational Linguistics\"}, {\"key\": \"austin1962speechacts\", \"type\": \"book\", \"title\": \"How to Do Things with Words\", \"authors\": \"Austin, J. L.\", \"year\": \"1962\", \"venue\": \"\"}, {\"key\": \"searle1969speechacts\", \"type\": \"book\", \"title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"authors\": \"Searle, J. R.\", \"year\": \"1969\", \"venue\": \"\"}, {\"key\": \"cialdini2001influence\", \"type\": \"book\", \"title\": \"Influence: Science and Practice\", \"authors\": \"Cialdini, Robert B.\", \"year\": \"2001\", \"venue\": \"\"}, {\"key\": \"zeng2024pap\", \"type\": \"inproceedings\", \"title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"authors\": \"Zeng, Yi and Lin, Hongpeng and Zhang, Jingwen and Yang, Diyi and Jia, Ruoxi and ...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Association for Computational Linguistics\"}, {\"key\": \"russinovich2024crescendo\", \"type\": \"inproceedings\", \"title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"authors\": \"Russinovich, Mark and Salem, Ahmed and Eldan, Ronen\", \"year\": \"2025\", \"venue\": \"USENIX Security Symposium\"}, {\"key\": \"chao2023pair\", \"type\": \"article\", \"title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"authors\": \"Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pa...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"wei2023jailbroken\", \"type\": \"inproceedings\", \"title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"authors\": \"Wei, Alexander and Haghtalab, Nika and Steinhardt, Jacob\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"hagendorff2026reasoning\", \"type\": \"article\", \"title\": \"Large Reasoning Models Are Autonomous Jailbreak Agents\", \"authors\": \"Hagendorff, Thilo and Derner, Erik and Oliver, Nuria\", \"year\": \"2026\", \"venue\": \"Nature Communications\"}, {\"key\": \"fitd2024\", \"type\": \"article\", \"title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"authors\": \"Wang, Zhenhua and Xie, Wei and Wang, Baosheng and Wang, Enze and Gui, Zhiwen and...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"deceptivedelight2024\", \"type\": \"techreport\", \"title\": \"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\", \"authors\": \"Palo Alto Networks Unit 42\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"ren2024actorattack\", \"type\": \"inproceedings\", \"title\": \"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\", \"authors\": \"Ren, Qibing and Li, Hao and Liu, Dongrui and Xie, Zhanxu and Lu, Xiaoya and Qiao...\", \"year\": \"2025\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"zou2023gcg\", \"type\": \"article\", \"title\": \"Universal and Transferable Adversarial Attacks on Aligned Language Models\", \"authors\": \"Zou, Andy and Wang, Zifan and Carlini, Nicholas and Nasr, Milad and Kolter, J. Z...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"li2024mhj\", \"type\": \"article\", \"title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"authors\": \"Li, Nathaniel and Han, Ziwen and Steneker, Ian and Primack, Willow and Goodside,...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"gururangan2018artifacts\", \"type\": \"inproceedings\", \"title\": \"Annotation Artifacts in Natural Language Inference Data\", \"authors\": \"Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and ...\", \"year\": \"2018\", \"venue\": \"Proceedings of the Conference of the North American Chapter of the Association f...\"}, {\"key\": \"niven2019probing\", \"type\": \"inproceedings\", \"title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"authors\": \"Niven, Timothy and Kao, Hung-Yu\", \"year\": \"2019\", \"venue\": \"Proceedings of the Association for Computational Linguistics\"}, {\"key\": \"nasr2025attackermovessecond\", \"type\": \"article\", \"title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\", \"authors\": \"Nasr, Milad and Carlini, Nicholas and Sitawarin, Chawin and Schulhoff, Sander V....\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"andriushchenko2024adaptive\", \"type\": \"inproceedings\", \"title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"authors\": \"Andriushchenko, Maksym and Croce, Francesco and Flammarion, Nicolas\", \"year\": \"2025\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"he2021deberta\", \"type\": \"inproceedings\", \"title\": \"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\", \"authors\": \"He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gururangan2020dontstop\", \"type\": \"inproceedings\", \"title\": \"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\", \"authors\": \"Gururangan, Suchin and Marasovi\\\\'c, Ana and Swayamdipta, Swabha and Lo, Kyle and...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 58th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"caruana1997multitask\", \"type\": \"article\", \"title\": \"Multitask Learning\", \"authors\": \"Caruana, Rich\", \"year\": \"1997\", \"venue\": \"Machine Learning\"}, {\"key\": \"phang2018stilts\", \"type\": \"article\", \"title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"authors\": \"Phang, Jason and F\\\\'evry, Thibault and Bowman, Samuel R.\", \"year\": \"2018\", \"venue\": \"arXiv preprint arXiv:1811.01088\"}, {\"key\": \"liu2019mtdnn\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"authors\": \"Liu, Xiaodong and He, Pengcheng and Chen, Weizhu and Gao, Jianfeng\", \"year\": \"2019\", \"venue\": \"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"howard2018ulmfit\", \"type\": \"inproceedings\", \"title\": \"Universal Language Model Fine-tuning for Text Classification\", \"authors\": \"Howard, Jeremy and Ruder, Sebastian\", \"year\": \"2018\", \"venue\": \"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"dasanmartino2020semeval\", \"type\": \"inproceedings\", \"title\": \"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\", \"authors\": \"Da San Martino, Giovanni and Barr\\\\'on-Cede\\\\~no, Alberto and Wachsmuth, Henning a...\", \"year\": \"2020\", \"venue\": \"Proceedings of the Fourteenth Workshop on Semantic Evaluation\"}, {\"key\": \"dasanmartino2019fine\", \"type\": \"inproceedings\", \"title\": \"Fine-Grained Analysis of Propaganda in News Articles\", \"authors\": \"Da San Martino, Giovanni and Yu, Seunghak and Barr\\\\'on-Cede\\\\~no, Alberto and Pet...\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"jin2020textfooler\", \"type\": \"inproceedings\", \"title\": \"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\", \"authors\": \"Jin, Di and Jin, Zhijing and Zhou, Joey Tianyi and Szolovits, Peter\", \"year\": \"2020\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"li2020bertattack\", \"type\": \"inproceedings\", \"title\": \"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\", \"authors\": \"Li, Linyang and Ma, Ruotian and Guo, Qipeng and Xue, Xiangyang and Qiu, Xipeng\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"conneau2018probing\", \"type\": \"inproceedings\", \"title\": \"What you can cram into a single \\\\$\\\\&!\\\\#* vector: Probing sentence embeddings for linguistic properties\", \"authors\": \"Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo\\\\\\\"i...\", \"year\": \"2018\", \"venue\": \"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"hewitt2019structural\", \"type\": \"inproceedings\", \"title\": \"A Structural Probe for Finding Syntax in Word Representations\", \"authors\": \"Hewitt, John and Manning, Christopher D.\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"liu2019roberta\", \"type\": \"article\", \"title\": \"RoBERTa: A Robustly Optimized BERT Pretraining Approach\", \"authors\": \"Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and...\", \"year\": \"2019\", \"venue\": \"arXiv preprint arXiv:1907.11692\"}], \"tex_citations\": [{\"key\": \"russinovich2024crescendo\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"bullwinkel2025repeng\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"inan2023llamaguard\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"han2024wildguard\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"zeng2024shieldgemma\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"deepcontext2026\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"tong2025biid\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"gguard2025\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"introduction.tex\", \"line\": 14, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"introduction.tex\", \"line\": 14, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"introduction.tex\", \"line\": 14, \"command\": \"citep\"}, {\"key\": \"russinovich2024crescendo\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"chao2023pair\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"wei2023jailbroken\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"zeng2024pap\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"li2024mhj\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"zou2023gcg\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"deepcontext2026\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"tong2025biid\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"gguard2025\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"safedream2026\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"inan2023llamaguard\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"metallamaguard3_2024\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"zeng2024shieldgemma\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"han2024wildguard\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"anthropic2025constitutional\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"mann1988rst\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"prasad2008pdtb\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"stolcke2000dialogueact\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"austin1962speechacts\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"searle1969speechacts\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"dasanmartino2019fine\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"dasanmartino2020semeval\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"howard2018ulmfit\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"gururangan2020dontstop\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citet\"}, {\"key\": \"phang2018stilts\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"caruana1997multitask\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"liu2019mtdnn\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"gururangan2018artifacts\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"niven2019probing\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"nasr2025attackermovessecond\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"andriushchenko2024adaptive\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"jin2020textfooler\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"li2020bertattack\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"conneau2018probing\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"hewitt2019structural\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"method.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"method.tex\", \"line\": 44, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"method.tex\", \"line\": 44, \"command\": \"citep\"}, {\"key\": \"russinovich2024crescendo\", \"file\": \"experiments.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"experiments.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"bullwinkel2025repeng\", \"file\": \"experiments.tex\", \"line\": 49, \"command\": \"citep\"}, {\"key\": \"gururangan2020dontstop\", \"file\": \"experiments.tex\", \"line\": 103, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"experiments.tex\", \"line\": 122, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"experiments.tex\", \"line\": 160, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"experiments.tex\", \"line\": 172, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"experiments.tex\", \"line\": 172, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"experiments.tex\", \"line\": 259, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"experiments.tex\", \"line\": 262, \"command\": \"citep\"}, {\"key\": \"zou2023gcg\", \"file\": \"conclusion.tex\", \"line\": 27, \"command\": \"citep\"}], \"online_verification\": [{\"key\": \"inan2023llamaguard\", \"title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"metallamaguard3_2024\", \"title\": \"Llama Guard 3\", \"status\": \"not_found\", \"confidence\": 0.289, \"matched_title\": \"Llama Guard 3 Vision: Safeguarding Human-AI Image Understanding Conversations\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.29 below threshold 0.82\"}, {\"key\": \"zeng2024shieldgemma\", \"title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"han2024wildguard\", \"title\": \"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"WildGuard: Open One-stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=han vs api=choi\"], \"note\": \"\"}, {\"key\": \"anthropic2025constitutional\", \"title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=anthropic vs api=sharma\"], \"note\": \"\"}, {\"key\": \"deepcontext2026\", \"title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tong2025biid\", \"title\": \"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\", \"status\": \"not_found\", \"confidence\": 0.328, \"matched_title\": \"AI Alignment: A Comprehensive Survey\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"gguard2025\", \"title\": \"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\", \"status\": \"verified\", \"confidence\": 0.882, \"matched_title\": \"Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"safedream2026\", \"title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bullwinkel2025repeng\", \"title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mann1988rst\", \"title\": \"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rhetorical Structure Theory: Toward a functional theory of text organization\", \"matched_year\": \"1988\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"prasad2008pdtb\", \"title\": \"The Penn Discourse TreeBank 2.0\", \"status\": \"verified\", \"confidence\": 0.984, \"matched_title\": \"The Penn Discourse TreeBank 2.0.\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"stolcke2000dialogueact\", \"title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"matched_year\": \"2000\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"austin1962speechacts\", \"title\": \"How to Do Things with Words\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"How To Do Things With Words\", \"matched_year\": \"1975\", \"mismatch_fields\": [\"year: bib=1962 vs api=1975\"], \"note\": \"\"}, {\"key\": \"searle1969speechacts\", \"title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"matched_year\": \"1969\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cialdini2001influence\", \"title\": \"Influence: Science and Practice\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Influence: science and practice\", \"matched_year\": \"2008\", \"mismatch_fields\": [\"year: bib=2001 vs api=2008\", \"first_author: bib=cialdini vs api=giebels\"], \"note\": \"\"}, {\"key\": \"zeng2024pap\", \"title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"russinovich2024crescendo\", \"title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chao2023pair\", \"title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"year: bib=2023 vs api=2025\"], \"note\": \"\"}, {\"key\": \"wei2023jailbroken\", \"title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hagendorff2026reasoning\", \"title\": \"Large Reasoning Models Are Autonomous Jailbreak Agents\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large reasoning models are autonomous jailbreak agents\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fitd2024\", \"title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"deceptivedelight2024\", \"title\": \"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\", \"status\": \"not_found\", \"confidence\": 0.446, \"matched_title\": \"BitBypass: A New Direction in Jailbreaking Aligned Large Language Models with Bitstream Camouflage\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"ren2024actorattack\", \"title\": \"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\", \"status\": \"not_found\", \"confidence\": 0.402, \"matched_title\": \"NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-Turn LLM Jailbreaks\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.40 below threshold 0.82\"}, {\"key\": \"zou2023gcg\", \"title\": \"Universal and Transferable Adversarial Attacks on Aligned Language Models\", \"status\": \"not_found\", \"confidence\": 0.301, \"matched_title\": \"Text Data Augmentation for Deep Learning\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\"}, {\"key\": \"li2024mhj\", \"title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gururangan2018artifacts\", \"title\": \"Annotation Artifacts in Natural Language Inference Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Annotation Artifacts in Natural Language Inference Data\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"niven2019probing\", \"title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nasr2025attackermovessecond\", \"title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against Llm Jailbreaks and Prompt Injections\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"andriushchenko2024adaptive\", \"title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"he2021deberta\", \"title\": \"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DEBERTA: DECODING-ENHANCED BERT WITH DISENTANGLED ATTENTION\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gururangan2020dontstop\", \"title\": \"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\", \"status\": \"not_found\", \"confidence\": 0.492, \"matched_title\": \"From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.49 below threshold 0.82\"}, {\"key\": \"caruana1997multitask\", \"title\": \"Multitask Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multitask Learning\", \"matched_year\": \"1997\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"phang2018stilts\", \"title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liu2019mtdnn\", \"title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"howard2018ulmfit\", \"title\": \"Universal Language Model Fine-tuning for Text Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Language Model Fine-tuning for Text Classification\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dasanmartino2020semeval\", \"title\": \"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\", \"matched_year\": \"2020\", \"mismatch_fields\": [\"first_author: bib=da san martino vs api=martino\"], \"note\": \"\"}, {\"key\": \"dasanmartino2019fine\", \"title\": \"Fine-Grained Analysis of Propaganda in News Articles\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Fine-Grained Analysis of Propaganda in News Articles\", \"matched_year\": \"2019\", \"mismatch_fields\": [\"first_author: bib=da san martino vs api=martino\"], \"note\": \"\"}, {\"key\": \"jin2020textfooler\", \"title\": \"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2020bertattack\", \"title\": \"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"conneau2018probing\", \"title\": \"What you can cram into a single \\\\$\\\\&!\\\\#* vector: Probing sentence embeddings for linguistic properties\", \"status\": \"verified\", \"confidence\": 0.98, \"matched_title\": \"What you can cram into a single $&amp;!#* vector: Probing sentence embeddings for linguistic properties\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hewitt2019structural\", \"title\": \"A Structural Probe for Finding Syntax in Word Representations\", \"status\": \"not_found\", \"confidence\": 0.316, \"matched_title\": \"What Does BERT Learn about the Structure of Language?\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.32 below threshold 0.82\"}, {\"key\": \"liu2019roberta\", \"title\": \"RoBERTa: A Robustly Optimized BERT Pretraining Approach\", \"status\": \"not_found\", \"confidence\": 0.495, \"matched_title\": \"Use of Bidirectional Encoder Representations from Transformers (BERT) and Robustly Optimized Bert Pretraining Approach (RoBERTa) for Nepali News Classification\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.50 below threshold 0.82\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89bafa13-7921-418c-8986-cd3872f7277b",
  "isSidechain": false,
  "promptId": "f969e597-50af-4667-a32a-e352289d26c2",
  "type": "user",
  "uuid": "462be00e-2008-4050-8e39-806ebf6224ce",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 43, \\\"total_citations\\\": 77, \\\"unique_cited_keys\\\": 43, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 28, \\\"online_not_found\\\": 8, \\\"online_mismatch\\\": 7}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"inan2023llamaguard\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\\\", \\\"authors\\\": \\\"Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer,...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"metallamaguard3_2024\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"Llama Guard 3\\\", \\\"authors\\\": \\\"Meta AI\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"zeng2024shieldgemma\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"ShieldGemma: Generative AI Content Moderation Based on Gemma\\\", \\\"authors\\\": \\\"Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"han2024wildguard\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\\\", \\\"authors\\\": \\\"Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"anthropic2025constitutional\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\\\", \\\"authors\\\": \\\"Anthropic\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"deepcontext2026\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\\\", \\\"authors\\\": \\\"Albrethsen, Justin and Datta, Yash and Kumar, Kunal and Rajasekar, Sharath\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"tong2025biid\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\\\", \\\"authors\\\": \\\"Tong, Haibo and Zhao, Dongcheng and Shen, Guobin and He, Xiang and Lin, Dachuan ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"gguard2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\\\", \\\"authors\\\": \\\"Huang, Zixuan and Huang, Kecheng and Yin, Lihao and He, Bowei and Zhen, Huiling ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"safedream2026\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\\\", \\\"authors\\\": \\\"Yan, Bo and Lin, Weikai and Zhu, Yada and Wang, Song\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"bullwinkel2025repeng\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\\\", \\\"authors\\\": \\\"Bullwinkel, Blake and Russinovich, Mark and Salem, Ahmed and Zanella-Beguelin, S...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"mann1988rst\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\\\", \\\"authors\\\": \\\"Mann, William C. and Thompson, Sandra A.\\\", \\\"year\\\": \\\"1988\\\", \\\"venue\\\": \\\"Text \\\\\\\\& Talk\\\"}, {\\\"key\\\": \\\"prasad2008pdtb\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Penn Discourse TreeBank 2.0\\\", \\\"authors\\\": \\\"Prasad, Rashmi and Dinesh, Nikhil and Lee, Alan and Miltsakaki, Eleni and Robald...\\\", \\\"year\\\": \\\"2008\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Language Resources and Evaluation\\\"}, {\\\"key\\\": \\\"stolcke2000dialogueact\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\\\", \\\"authors\\\": \\\"Stolcke, Andreas and Ries, Klaus and Coccaro, Noah and Shriberg, Elizabeth and B...\\\", \\\"year\\\": \\\"2000\\\", \\\"venue\\\": \\\"Computational Linguistics\\\"}, {\\\"key\\\": \\\"austin1962speechacts\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"How to Do Things with Words\\\", \\\"authors\\\": \\\"Austin, J. L.\\\", \\\"year\\\": \\\"1962\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"searle1969speechacts\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Speech Acts: An Essay in the Philosophy of Language\\\", \\\"authors\\\": \\\"Searle, J. R.\\\", \\\"year\\\": \\\"1969\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"cialdini2001influence\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Influence: Science and Practice\\\", \\\"authors\\\": \\\"Cialdini, Robert B.\\\", \\\"year\\\": \\\"2001\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\\\", \\\"authors\\\": \\\"Zeng, Yi and Lin, Hongpeng and Zhang, Jingwen and Yang, Diyi and Jia, Ruoxi and ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"russinovich2024crescendo\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\\\", \\\"authors\\\": \\\"Russinovich, Mark and Salem, Ahmed and Eldan, Ronen\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"USENIX Security Symposium\\\"}, {\\\"key\\\": \\\"chao2023pair\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Jailbreaking Black Box Large Language Models in Twenty Queries\\\", \\\"authors\\\": \\\"Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pa...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"wei2023jailbroken\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Jailbroken: How Does LLM Safety Training Fail?\\\", \\\"authors\\\": \\\"Wei, Alexander and Haghtalab, Nika and Steinhardt, Jacob\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"hagendorff2026reasoning\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Reasoning Models Are Autonomous Jailbreak Agents\\\", \\\"authors\\\": \\\"Hagendorff, Thilo and Derner, Erik and Oliver, Nuria\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Nature Communications\\\"}, {\\\"key\\\": \\\"fitd2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\\\", \\\"authors\\\": \\\"Wang, Zhenhua and Xie, Wei and Wang, Baosheng and Wang, Enze and Gui, Zhiwen and...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"type\\\": \\\"techreport\\\", \\\"title\\\": \\\"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\\\", \\\"authors\\\": \\\"Palo Alto Networks Unit 42\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"ren2024actorattack\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\\\", \\\"authors\\\": \\\"Ren, Qibing and Li, Hao and Liu, Dongrui and Xie, Zhanxu and Lu, Xiaoya and Qiao...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"zou2023gcg\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Universal and Transferable Adversarial Attacks on Aligned Language Models\\\", \\\"authors\\\": \\\"Zou, Andy and Wang, Zifan and Carlini, Nicholas and Nasr, Milad and Kolter, J. Z...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"li2024mhj\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\\\", \\\"authors\\\": \\\"Li, Nathaniel and Han, Ziwen and Steneker, Ian and Primack, Willow and Goodside,...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"gururangan2018artifacts\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Annotation Artifacts in Natural Language Inference Data\\\", \\\"authors\\\": \\\"Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and ...\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the Conference of the North American Chapter of the Association f...\\\"}, {\\\"key\\\": \\\"niven2019probing\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Probing Neural Network Comprehension of Natural Language Arguments\\\", \\\"authors\\\": \\\"Niven, Timothy and Kao, Hung-Yu\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"nasr2025attackermovessecond\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\\\", \\\"authors\\\": \\\"Nasr, Milad and Carlini, Nicholas and Sitawarin, Chawin and Schulhoff, Sander V....\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"andriushchenko2024adaptive\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\\\", \\\"authors\\\": \\\"Andriushchenko, Maksym and Croce, Francesco and Flammarion, Nicolas\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\\\", \\\"authors\\\": \\\"He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"gururangan2020dontstop\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\\\", \\\"authors\\\": \\\"Gururangan, Suchin and Marasovi\\\\\\\\'c, Ana and Swayamdipta, Swabha and Lo, Kyle and...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 58th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"caruana1997multitask\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Multitask Learning\\\", \\\"authors\\\": \\\"Caruana, Rich\\\", \\\"year\\\": \\\"1997\\\", \\\"venue\\\": \\\"Machine Learning\\\"}, {\\\"key\\\": \\\"phang2018stilts\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\\\", \\\"authors\\\": \\\"Phang, Jason and F\\\\\\\\'evry, Thibault and Bowman, Samuel R.\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:1811.01088\\\"}, {\\\"key\\\": \\\"liu2019mtdnn\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Multi-Task Deep Neural Networks for Natural Language Understanding\\\", \\\"authors\\\": \\\"Liu, Xiaodong and He, Pengcheng and Chen, Weizhu and Gao, Jianfeng\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"howard2018ulmfit\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Universal Language Model Fine-tuning for Text Classification\\\", \\\"authors\\\": \\\"Howard, Jeremy and Ruder, Sebastian\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"dasanmartino2020semeval\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\\\", \\\"authors\\\": \\\"Da San Martino, Giovanni and Barr\\\\\\\\'on-Cede\\\\\\\\~no, Alberto and Wachsmuth, Henning a...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the Fourteenth Workshop on Semantic Evaluation\\\"}, {\\\"key\\\": \\\"dasanmartino2019fine\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Fine-Grained Analysis of Propaganda in News Articles\\\", \\\"authors\\\": \\\"Da San Martino, Giovanni and Yu, Seunghak and Barr\\\\\\\\'on-Cede\\\\\\\\~no, Alberto and Pet...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"jin2020textfooler\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\\\", \\\"authors\\\": \\\"Jin, Di and Jin, Zhijing and Zhou, Joey Tianyi and Szolovits, Peter\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"li2020bertattack\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\\\", \\\"authors\\\": \\\"Li, Linyang and Ma, Ruotian and Guo, Qipeng and Xue, Xiangyang and Qiu, Xipeng\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"conneau2018probing\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"What you can cram into a single \\\\\\\\$\\\\\\\\&!\\\\\\\\#* vector: Probing sentence embeddings for linguistic properties\\\", \\\"authors\\\": \\\"Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo\\\\\\\\\\\\\\\"i...\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"hewitt2019structural\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Structural Probe for Finding Syntax in Word Representations\\\", \\\"authors\\\": \\\"Hewitt, John and Manning, Christopher D.\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 2019 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"liu2019roberta\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"RoBERTa: A Robustly Optimized BERT Pretraining Approach\\\", \\\"authors\\\": \\\"Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:1907.11692\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"russinovich2024crescendo\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"fitd2024\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"hagendorff2026reasoning\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"bullwinkel2025repeng\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"inan2023llamaguard\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"han2024wildguard\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zeng2024shieldgemma\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deepcontext2026\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"tong2025biid\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gguard2025\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"liu2019roberta\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ren2024actorattack\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"russinovich2024crescendo\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"fitd2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ren2024actorattack\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"chao2023pair\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wei2023jailbroken\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hagendorff2026reasoning\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"li2024mhj\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zou2023gcg\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deepcontext2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"tong2025biid\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gguard2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"safedream2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"inan2023llamaguard\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"metallamaguard3_2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zeng2024shieldgemma\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"han2024wildguard\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"anthropic2025constitutional\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"mann1988rst\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"prasad2008pdtb\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"stolcke2000dialogueact\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"austin1962speechacts\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"searle1969speechacts\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cialdini2001influence\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hagendorff2026reasoning\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"dasanmartino2019fine\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"dasanmartino2020semeval\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"howard2018ulmfit\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gururangan2020dontstop\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"phang2018stilts\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"caruana1997multitask\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"liu2019mtdnn\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"liu2019roberta\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ren2024actorattack\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gururangan2018artifacts\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"niven2019probing\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"nasr2025attackermovessecond\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"andriushchenko2024adaptive\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"jin2020textfooler\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"li2020bertattack\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"conneau2018probing\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hewitt2019structural\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 44, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cialdini2001influence\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 44, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"russinovich2024crescendo\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"fitd2024\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ren2024actorattack\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"liu2019roberta\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"bullwinkel2025repeng\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 49, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gururangan2020dontstop\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 103, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ren2024actorattack\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 122, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"liu2019roberta\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 160, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 172, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"liu2019roberta\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 172, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cialdini2001influence\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 259, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 262, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zou2023gcg\\\", \\\"file\\\": \\\"conclusion.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"citep\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"inan2023llamaguard\\\", \\\"title\\\": \\\"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"metallamaguard3_2024\\\", \\\"title\\\": \\\"Llama Guard 3\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.289, \\\"matched_title\\\": \\\"Llama Guard 3 Vision: Safeguarding Human-AI Image Understanding Conversations\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.29 below threshold 0.82\\\"}, {\\\"key\\\": \\\"zeng2024shieldgemma\\\", \\\"title\\\": \\\"ShieldGemma: Generative AI Content Moderation Based on Gemma\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ShieldGemma: Generative AI Content Moderation Based on Gemma\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"han2024wildguard\\\", \\\"title\\\": \\\"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"WildGuard: Open One-stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=han vs api=choi\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"anthropic2025constitutional\\\", \\\"title\\\": \\\"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=anthropic vs api=sharma\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"deepcontext2026\\\", \\\"title\\\": \\\"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tong2025biid\\\", \\\"title\\\": \\\"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.328, \\\"matched_title\\\": \\\"AI Alignment: A Comprehensive Survey\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.33 below threshold 0.82\\\"}, {\\\"key\\\": \\\"gguard2025\\\", \\\"title\\\": \\\"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.882, \\\"matched_title\\\": \\\"Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"safedream2026\\\", \\\"title\\\": \\\"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"bullwinkel2025repeng\\\", \\\"title\\\": \\\"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mann1988rst\\\", \\\"title\\\": \\\"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Rhetorical Structure Theory: Toward a functional theory of text organization\\\", \\\"matched_year\\\": \\\"1988\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"prasad2008pdtb\\\", \\\"title\\\": \\\"The Penn Discourse TreeBank 2.0\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.984, \\\"matched_title\\\": \\\"The Penn Discourse TreeBank 2.0.\\\", \\\"matched_year\\\": \\\"2008\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"stolcke2000dialogueact\\\", \\\"title\\\": \\\"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\\\", \\\"matched_year\\\": \\\"2000\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"austin1962speechacts\\\", \\\"title\\\": \\\"How to Do Things with Words\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"How To Do Things With Words\\\", \\\"matched_year\\\": \\\"1975\\\", \\\"mismatch_fields\\\": [\\\"year: bib=1962 vs api=1975\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"searle1969speechacts\\\", \\\"title\\\": \\\"Speech Acts: An Essay in the Philosophy of Language\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Speech Acts: An Essay in the Philosophy of Language\\\", \\\"matched_year\\\": \\\"1969\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cialdini2001influence\\\", \\\"title\\\": \\\"Influence: Science and Practice\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Influence: science and practice\\\", \\\"matched_year\\\": \\\"2008\\\", \\\"mismatch_fields\\\": [\\\"year: bib=2001 vs api=2008\\\", \\\"first_author: bib=cialdini vs api=giebels\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"title\\\": \\\"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"russinovich2024crescendo\\\", \\\"title\\\": \\\"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chao2023pair\\\", \\\"title\\\": \\\"Jailbreaking Black Box Large Language Models in Twenty Queries\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Jailbreaking Black Box Large Language Models in Twenty Queries\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"year: bib=2023 vs api=2025\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wei2023jailbroken\\\", \\\"title\\\": \\\"Jailbroken: How Does LLM Safety Training Fail?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Jailbroken: How Does LLM Safety Training Fail?\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hagendorff2026reasoning\\\", \\\"title\\\": \\\"Large Reasoning Models Are Autonomous Jailbreak Agents\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large reasoning models are autonomous jailbreak agents\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fitd2024\\\", \\\"title\\\": \\\"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"title\\\": \\\"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.446, \\\"matched_title\\\": \\\"BitBypass: A New Direction in Jailbreaking Aligned Large Language Models with Bitstream Camouflage\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.45 below threshold 0.82\\\"}, {\\\"key\\\": \\\"ren2024actorattack\\\", \\\"title\\\": \\\"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.402, \\\"matched_title\\\": \\\"NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-Turn LLM Jailbreaks\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.40 below threshold 0.82\\\"}, {\\\"key\\\": \\\"zou2023gcg\\\", \\\"title\\\": \\\"Universal and Transferable Adversarial Attacks on Aligned Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.301, \\\"matched_title\\\": \\\"Text Data Augmentation for Deep Learning\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.30 below threshold 0.82\\\"}, {\\\"key\\\": \\\"li2024mhj\\\", \\\"title\\\": \\\"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gururangan2018artifacts\\\", \\\"title\\\": \\\"Annotation Artifacts in Natural Language Inference Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Annotation Artifacts in Natural Language Inference Data\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"niven2019probing\\\", \\\"title\\\": \\\"Probing Neural Network Comprehension of Natural Language Arguments\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Probing Neural Network Comprehension of Natural Language Arguments\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"nasr2025attackermovessecond\\\", \\\"title\\\": \\\"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against Llm Jailbreaks and Prompt Injections\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"andriushchenko2024adaptive\\\", \\\"title\\\": \\\"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"title\\\": \\\"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DEBERTA: DECODING-ENHANCED BERT WITH DISENTANGLED ATTENTION\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gururangan2020dontstop\\\", \\\"title\\\": \\\"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.492, \\\"matched_title\\\": \\\"From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.49 below threshold 0.82\\\"}, {\\\"key\\\": \\\"caruana1997multitask\\\", \\\"title\\\": \\\"Multitask Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multitask Learning\\\", \\\"matched_year\\\": \\\"1997\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"phang2018stilts\\\", \\\"title\\\": \\\"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"liu2019mtdnn\\\", \\\"title\\\": \\\"Multi-Task Deep Neural Networks for Natural Language Understanding\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multi-Task Deep Neural Networks for Natural Language Understanding\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"howard2018ulmfit\\\", \\\"title\\\": \\\"Universal Language Model Fine-tuning for Text Classification\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Universal Language Model Fine-tuning for Text Classification\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dasanmartino2020semeval\\\", \\\"title\\\": \\\"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=da san martino vs api=martino\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dasanmartino2019fine\\\", \\\"title\\\": \\\"Fine-Grained Analysis of Propaganda in News Articles\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Fine-Grained Analysis of Propaganda in News Articles\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=da san martino vs api=martino\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"jin2020textfooler\\\", \\\"title\\\": \\\"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2020bertattack\\\", \\\"title\\\": \\\"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"conneau2018probing\\\", \\\"title\\\": \\\"What you can cram into a single \\\\\\\\$\\\\\\\\&!\\\\\\\\#* vector: Probing sentence embeddings for linguistic properties\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.98, \\\"matched_title\\\": \\\"What you can cram into a single $&amp;!#* vector: Probing sentence embeddings for linguistic properties\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hewitt2019structural\\\", \\\"title\\\": \\\"A Structural Probe for Finding Syntax in Word Representations\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.316, \\\"matched_title\\\": \\\"What Does BERT Learn about the Structure of Language?\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.32 below threshold 0.82\\\"}, {\\\"key\\\": \\\"liu2019roberta\\\", \\\"title\\\": \\\"RoBERTa: A Robustly Optimized BERT Pretraining Approach\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.495, \\\"matched_title\\\": \\\"Use of Bidirectional Encoder Representations from Transformers (BERT) and Robustly Optimized Bert Pretraining Approach (RoBERTa) for Nepali News Classification\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.50 below threshold 0.82\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 43, \"total_citations\": 77, \"unique_cited_keys\": 43, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 28, \"online_not_found\": 8, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"inan2023llamaguard\", \"type\": \"article\", \"title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"authors\": \"Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer,...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"metallamaguard3_2024\", \"type\": \"misc\", \"title\": \"Llama Guard 3\", \"authors\": \"Meta AI\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"zeng2024shieldgemma\", \"type\": \"article\", \"title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"authors\": \"Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"han2024wildguard\", \"type\": \"inproceedings\", \"title\": \"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"authors\": \"Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"anthropic2025constitutional\", \"type\": \"article\", \"title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"authors\": \"Anthropic\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"deepcontext2026\", \"type\": \"article\", \"title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"authors\": \"Albrethsen, Justin and Datta, Yash and Kumar, Kunal and Rajasekar, Sharath\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"tong2025biid\", \"type\": \"article\", \"title\": \"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\", \"authors\": \"Tong, Haibo and Zhao, Dongcheng and Shen, Guobin and He, Xiang and Lin, Dachuan ...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"gguard2025\", \"type\": \"article\", \"title\": \"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\", \"authors\": \"Huang, Zixuan and Huang, Kecheng and Yin, Lihao and He, Bowei and Zhen, Huiling ...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"safedream2026\", \"type\": \"article\", \"title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"authors\": \"Yan, Bo and Lin, Weikai and Zhu, Yada and Wang, Song\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"bullwinkel2025repeng\", \"type\": \"article\", \"title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"authors\": \"Bullwinkel, Blake and Russinovich, Mark and Salem, Ahmed and Zanella-Beguelin, S...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"mann1988rst\", \"type\": \"article\", \"title\": \"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\", \"authors\": \"Mann, William C. and Thompson, Sandra A.\", \"year\": \"1988\", \"venue\": \"Text \\\\& Talk\"}, {\"key\": \"prasad2008pdtb\", \"type\": \"inproceedings\", \"title\": \"The Penn Discourse TreeBank 2.0\", \"authors\": \"Prasad, Rashmi and Dinesh, Nikhil and Lee, Alan and Miltsakaki, Eleni and Robald...\", \"year\": \"2008\", \"venue\": \"Proceedings of the International Conference on Language Resources and Evaluation\"}, {\"key\": \"stolcke2000dialogueact\", \"type\": \"article\", \"title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"authors\": \"Stolcke, Andreas and Ries, Klaus and Coccaro, Noah and Shriberg, Elizabeth and B...\", \"year\": \"2000\", \"venue\": \"Computational Linguistics\"}, {\"key\": \"austin1962speechacts\", \"type\": \"book\", \"title\": \"How to Do Things with Words\", \"authors\": \"Austin, J. L.\", \"year\": \"1962\", \"venue\": \"\"}, {\"key\": \"searle1969speechacts\", \"type\": \"book\", \"title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"authors\": \"Searle, J. R.\", \"year\": \"1969\", \"venue\": \"\"}, {\"key\": \"cialdini2001influence\", \"type\": \"book\", \"title\": \"Influence: Science and Practice\", \"authors\": \"Cialdini, Robert B.\", \"year\": \"2001\", \"venue\": \"\"}, {\"key\": \"zeng2024pap\", \"type\": \"inproceedings\", \"title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"authors\": \"Zeng, Yi and Lin, Hongpeng and Zhang, Jingwen and Yang, Diyi and Jia, Ruoxi and ...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Association for Computational Linguistics\"}, {\"key\": \"russinovich2024crescendo\", \"type\": \"inproceedings\", \"title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"authors\": \"Russinovich, Mark and Salem, Ahmed and Eldan, Ronen\", \"year\": \"2025\", \"venue\": \"USENIX Security Symposium\"}, {\"key\": \"chao2023pair\", \"type\": \"article\", \"title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"authors\": \"Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pa...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"wei2023jailbroken\", \"type\": \"inproceedings\", \"title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"authors\": \"Wei, Alexander and Haghtalab, Nika and Steinhardt, Jacob\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"hagendorff2026reasoning\", \"type\": \"article\", \"title\": \"Large Reasoning Models Are Autonomous Jailbreak Agents\", \"authors\": \"Hagendorff, Thilo and Derner, Erik and Oliver, Nuria\", \"year\": \"2026\", \"venue\": \"Nature Communications\"}, {\"key\": \"fitd2024\", \"type\": \"article\", \"title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"authors\": \"Wang, Zhenhua and Xie, Wei and Wang, Baosheng and Wang, Enze and Gui, Zhiwen and...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"deceptivedelight2024\", \"type\": \"techreport\", \"title\": \"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\", \"authors\": \"Palo Alto Networks Unit 42\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"ren2024actorattack\", \"type\": \"inproceedings\", \"title\": \"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\", \"authors\": \"Ren, Qibing and Li, Hao and Liu, Dongrui and Xie, Zhanxu and Lu, Xiaoya and Qiao...\", \"year\": \"2025\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"zou2023gcg\", \"type\": \"article\", \"title\": \"Universal and Transferable Adversarial Attacks on Aligned Language Models\", \"authors\": \"Zou, Andy and Wang, Zifan and Carlini, Nicholas and Nasr, Milad and Kolter, J. Z...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"li2024mhj\", \"type\": \"article\", \"title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"authors\": \"Li, Nathaniel and Han, Ziwen and Steneker, Ian and Primack, Willow and Goodside,...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"gururangan2018artifacts\", \"type\": \"inproceedings\", \"title\": \"Annotation Artifacts in Natural Language Inference Data\", \"authors\": \"Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and ...\", \"year\": \"2018\", \"venue\": \"Proceedings of the Conference of the North American Chapter of the Association f...\"}, {\"key\": \"niven2019probing\", \"type\": \"inproceedings\", \"title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"authors\": \"Niven, Timothy and Kao, Hung-Yu\", \"year\": \"2019\", \"venue\": \"Proceedings of the Association for Computational Linguistics\"}, {\"key\": \"nasr2025attackermovessecond\", \"type\": \"article\", \"title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\", \"authors\": \"Nasr, Milad and Carlini, Nicholas and Sitawarin, Chawin and Schulhoff, Sander V....\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"andriushchenko2024adaptive\", \"type\": \"inproceedings\", \"title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"authors\": \"Andriushchenko, Maksym and Croce, Francesco and Flammarion, Nicolas\", \"year\": \"2025\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"he2021deberta\", \"type\": \"inproceedings\", \"title\": \"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\", \"authors\": \"He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gururangan2020dontstop\", \"type\": \"inproceedings\", \"title\": \"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\", \"authors\": \"Gururangan, Suchin and Marasovi\\\\'c, Ana and Swayamdipta, Swabha and Lo, Kyle and...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 58th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"caruana1997multitask\", \"type\": \"article\", \"title\": \"Multitask Learning\", \"authors\": \"Caruana, Rich\", \"year\": \"1997\", \"venue\": \"Machine Learning\"}, {\"key\": \"phang2018stilts\", \"type\": \"article\", \"title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"authors\": \"Phang, Jason and F\\\\'evry, Thibault and Bowman, Samuel R.\", \"year\": \"2018\", \"venue\": \"arXiv preprint arXiv:1811.01088\"}, {\"key\": \"liu2019mtdnn\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"authors\": \"Liu, Xiaodong and He, Pengcheng and Chen, Weizhu and Gao, Jianfeng\", \"year\": \"2019\", \"venue\": \"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"howard2018ulmfit\", \"type\": \"inproceedings\", \"title\": \"Universal Language Model Fine-tuning for Text Classification\", \"authors\": \"Howard, Jeremy and Ruder, Sebastian\", \"year\": \"2018\", \"venue\": \"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"dasanmartino2020semeval\", \"type\": \"inproceedings\", \"title\": \"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\", \"authors\": \"Da San Martino, Giovanni and Barr\\\\'on-Cede\\\\~no, Alberto and Wachsmuth, Henning a...\", \"year\": \"2020\", \"venue\": \"Proceedings of the Fourteenth Workshop on Semantic Evaluation\"}, {\"key\": \"dasanmartino2019fine\", \"type\": \"inproceedings\", \"title\": \"Fine-Grained Analysis of Propaganda in News Articles\", \"authors\": \"Da San Martino, Giovanni and Yu, Seunghak and Barr\\\\'on-Cede\\\\~no, Alberto and Pet...\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"jin2020textfooler\", \"type\": \"inproceedings\", \"title\": \"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\", \"authors\": \"Jin, Di and Jin, Zhijing and Zhou, Joey Tianyi and Szolovits, Peter\", \"year\": \"2020\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"li2020bertattack\", \"type\": \"inproceedings\", \"title\": \"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\", \"authors\": \"Li, Linyang and Ma, Ruotian and Guo, Qipeng and Xue, Xiangyang and Qiu, Xipeng\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"conneau2018probing\", \"type\": \"inproceedings\", \"title\": \"What you can cram into a single \\\\$\\\\&!\\\\#* vector: Probing sentence embeddings for linguistic properties\", \"authors\": \"Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo\\\\\\\"i...\", \"year\": \"2018\", \"venue\": \"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"hewitt2019structural\", \"type\": \"inproceedings\", \"title\": \"A Structural Probe for Finding Syntax in Word Representations\", \"authors\": \"Hewitt, John and Manning, Christopher D.\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"liu2019roberta\", \"type\": \"article\", \"title\": \"RoBERTa: A Robustly Optimized BERT Pretraining Approach\", \"authors\": \"Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and...\", \"year\": \"2019\", \"venue\": \"arXiv preprint arXiv:1907.11692\"}], \"tex_citations\": [{\"key\": \"russinovich2024crescendo\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"bullwinkel2025repeng\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"inan2023llamaguard\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"han2024wildguard\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"zeng2024shieldgemma\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"deepcontext2026\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"tong2025biid\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"gguard2025\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"introduction.tex\", \"line\": 14, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"introduction.tex\", \"line\": 14, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"introduction.tex\", \"line\": 14, \"command\": \"citep\"}, {\"key\": \"russinovich2024crescendo\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"chao2023pair\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"wei2023jailbroken\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"zeng2024pap\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"li2024mhj\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"zou2023gcg\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"deepcontext2026\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"tong2025biid\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"gguard2025\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"safedream2026\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"inan2023llamaguard\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"metallamaguard3_2024\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"zeng2024shieldgemma\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"han2024wildguard\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"anthropic2025constitutional\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"mann1988rst\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"prasad2008pdtb\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"stolcke2000dialogueact\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"austin1962speechacts\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"searle1969speechacts\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"dasanmartino2019fine\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"dasanmartino2020semeval\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"howard2018ulmfit\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"gururangan2020dontstop\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citet\"}, {\"key\": \"phang2018stilts\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"caruana1997multitask\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"liu2019mtdnn\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"gururangan2018artifacts\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"niven2019probing\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"nasr2025attackermovessecond\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"andriushchenko2024adaptive\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"jin2020textfooler\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"li2020bertattack\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"conneau2018probing\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"hewitt2019structural\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"method.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"method.tex\", \"line\": 44, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"method.tex\", \"line\": 44, \"command\": \"citep\"}, {\"key\": \"russinovich2024crescendo\", \"file\": \"experiments.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"experiments.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"bullwinkel2025repeng\", \"file\": \"experiments.tex\", \"line\": 49, \"command\": \"citep\"}, {\"key\": \"gururangan2020dontstop\", \"file\": \"experiments.tex\", \"line\": 103, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"experiments.tex\", \"line\": 122, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"experiments.tex\", \"line\": 160, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"experiments.tex\", \"line\": 172, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"experiments.tex\", \"line\": 172, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"experiments.tex\", \"line\": 259, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"experiments.tex\", \"line\": 262, \"command\": \"citep\"}, {\"key\": \"zou2023gcg\", \"file\": \"conclusion.tex\", \"line\": 27, \"command\": \"citep\"}], \"online_verification\": [{\"key\": \"inan2023llamaguard\", \"title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"metallamaguard3_2024\", \"title\": \"Llama Guard 3\", \"status\": \"not_found\", \"confidence\": 0.289, \"matched_title\": \"Llama Guard 3 Vision: Safeguarding Human-AI Image Understanding Conversations\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.29 below threshold 0.82\"}, {\"key\": \"zeng2024shieldgemma\", \"title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"han2024wildguard\", \"title\": \"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"WildGuard: Open One-stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=han vs api=choi\"], \"note\": \"\"}, {\"key\": \"anthropic2025constitutional\", \"title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=anthropic vs api=sharma\"], \"note\": \"\"}, {\"key\": \"deepcontext2026\", \"title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tong2025biid\", \"title\": \"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\", \"status\": \"not_found\", \"confidence\": 0.328, \"matched_title\": \"AI Alignment: A Comprehensive Survey\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"gguard2025\", \"title\": \"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\", \"status\": \"verified\", \"confidence\": 0.882, \"matched_title\": \"Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"safedream2026\", \"title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bullwinkel2025repeng\", \"title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mann1988rst\", \"title\": \"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rhetorical Structure Theory: Toward a functional theory of text organization\", \"matched_year\": \"1988\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"prasad2008pdtb\", \"title\": \"The Penn Discourse TreeBank 2.0\", \"status\": \"verified\", \"confidence\": 0.984, \"matched_title\": \"The Penn Discourse TreeBank 2.0.\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"stolcke2000dialogueact\", \"title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"matched_year\": \"2000\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"austin1962speechacts\", \"title\": \"How to Do Things with Words\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"How To Do Things With Words\", \"matched_year\": \"1975\", \"mismatch_fields\": [\"year: bib=1962 vs api=1975\"], \"note\": \"\"}, {\"key\": \"searle1969speechacts\", \"title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"matched_year\": \"1969\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cialdini2001influence\", \"title\": \"Influence: Science and Practice\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Influence: science and practice\", \"matched_year\": \"2008\", \"mismatch_fields\": [\"year: bib=2001 vs api=2008\", \"first_author: bib=cialdini vs api=giebels\"], \"note\": \"\"}, {\"key\": \"zeng2024pap\", \"title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"russinovich2024crescendo\", \"title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chao2023pair\", \"title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"year: bib=2023 vs api=2025\"], \"note\": \"\"}, {\"key\": \"wei2023jailbroken\", \"title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hagendorff2026reasoning\", \"title\": \"Large Reasoning Models Are Autonomous Jailbreak Agents\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large reasoning models are autonomous jailbreak agents\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fitd2024\", \"title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"deceptivedelight2024\", \"title\": \"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\", \"status\": \"not_found\", \"confidence\": 0.446, \"matched_title\": \"BitBypass: A New Direction in Jailbreaking Aligned Large Language Models with Bitstream Camouflage\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"ren2024actorattack\", \"title\": \"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\", \"status\": \"not_found\", \"confidence\": 0.402, \"matched_title\": \"NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-Turn LLM Jailbreaks\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.40 below threshold 0.82\"}, {\"key\": \"zou2023gcg\", \"title\": \"Universal and Transferable Adversarial Attacks on Aligned Language Models\", \"status\": \"not_found\", \"confidence\": 0.301, \"matched_title\": \"Text Data Augmentation for Deep Learning\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\"}, {\"key\": \"li2024mhj\", \"title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gururangan2018artifacts\", \"title\": \"Annotation Artifacts in Natural Language Inference Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Annotation Artifacts in Natural Language Inference Data\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"niven2019probing\", \"title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nasr2025attackermovessecond\", \"title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against Llm Jailbreaks and Prompt Injections\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"andriushchenko2024adaptive\", \"title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"he2021deberta\", \"title\": \"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DEBERTA: DECODING-ENHANCED BERT WITH DISENTANGLED ATTENTION\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gururangan2020dontstop\", \"title\": \"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\", \"status\": \"not_found\", \"confidence\": 0.492, \"matched_title\": \"From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.49 below threshold 0.82\"}, {\"key\": \"caruana1997multitask\", \"title\": \"Multitask Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multitask Learning\", \"matched_year\": \"1997\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"phang2018stilts\", \"title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liu2019mtdnn\", \"title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"howard2018ulmfit\", \"title\": \"Universal Language Model Fine-tuning for Text Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Language Model Fine-tuning for Text Classification\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dasanmartino2020semeval\", \"title\": \"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\", \"matched_year\": \"2020\", \"mismatch_fields\": [\"first_author: bib=da san martino vs api=martino\"], \"note\": \"\"}, {\"key\": \"dasanmartino2019fine\", \"title\": \"Fine-Grained Analysis of Propaganda in News Articles\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Fine-Grained Analysis of Propaganda in News Articles\", \"matched_year\": \"2019\", \"mismatch_fields\": [\"first_author: bib=da san martino vs api=martino\"], \"note\": \"\"}, {\"key\": \"jin2020textfooler\", \"title\": \"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2020bertattack\", \"title\": \"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"conneau2018probing\", \"title\": \"What you can cram into a single \\\\$\\\\&!\\\\#* vector: Probing sentence embeddings for linguistic properties\", \"status\": \"verified\", \"confidence\": 0.98, \"matched_title\": \"What you can cram into a single $&amp;!#* vector: Probing sentence embeddings for linguistic properties\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hewitt2019structural\", \"title\": \"A Structural Probe for Finding Syntax in Word Representations\", \"status\": \"not_found\", \"confidence\": 0.316, \"matched_title\": \"What Does BERT Learn about the Structure of Language?\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.32 below threshold 0.82\"}, {\"key\": \"liu2019roberta\", \"title\": \"RoBERTa: A Robustly Optimized BERT Pretraining Approach\", \"status\": \"not_found\", \"confidence\": 0.495, \"matched_title\": \"Use of Bidirectional Encoder Representations from Transformers (BERT) and Robustly Optimized Bert Pretraining Approach (RoBERTa) for Nepali News Classification\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.50 below threshold 0.82\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "89bafa13-7921-418c-8986-cd3872f7277b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 48_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你负责审查**方法严谨性、实验设计和统计有效性**。  ## 论文信息 - **标题**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap - **目标 venue**: EMNLP 2026（ARR May cycle） - **De…",
  "leafUuid": "462be00e-2008-4050-8e39-806ebf6224ce",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multi-turn jailbreak detection paper methodology",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

### Assistant

_source line 50 · 2026-05-18T15:54:38.935Z_

<details><summary>Logged reasoning block</summary>

```text
I now have a thorough understanding of the paper and the ARR review criteria. Let me compile my review.

Key observations from the paper:

**Strengths:**
1. Well-designed ablation study with 7 controlled variants
2. Cross-encoder validation (DeBERTa + RoBERTa)
3. Honest about limitations (TF-IDF baseline, small data, single-seed issues)
4. Good experimental organization

**Weaknesses (by my assigned focus areas):**

### 1. Experimental Design
- **Data scale**: 250+250 training, 80-118 OOD is very small. 
- **Statistical power**: The perturbation evaluation on n=76 is underpowered, and only 3 seeds limits reliability—mean pooling relies on a single seed.
- **Synthetic data confound**: All data comes from Qwen3-8B for both training and evaluation, which is a significant methodological issue.
- **Limited OOD difficulty**: FITD is trivially easy with F1 ≥ 0.990 across variants, leaving only DD and ActorAttack as meaningful tests.
- **Incomplete replication**: Only 3 of 7 variants were validated on the cross-encoder models.

The perturbation analysis itself is only run on DeBERTa, not RoBERTa. On the statistical validity side, the main detection results lack formal significance testing beyond mean and standard deviation. The McNemar test applied to n=76 with very few discordant pairs has acknowledged low power, yet the three-layer pattern gets prominent placement despite only appearing on IID and DD—it explicitly fails on ActorAttack. The variance is also concerning, with some conditions showing standard deviations around 0.115, which is substantial given only three seeds were used.

The two-stage architecture with a frozen encoder during Stage 2 prevents the BiGRU from adapting representations, which could disadvantage simpler baselines unfairly. End-to-end fine-tuning isn't explored, so it's unclear whether this design choice artificially constrains the evidence hierarchy. The mean pooling baseline achieves F1=1.000 on DD from a single seed, which suspiciously outperforms the three-seed BiGRU average—likely just seed variance. Strategy annotation reliability is limited to κ=0.78 on only 50 examples with one annotator, and the α=0.3 weighting parameter lacks justification.

The TF-IDF logistic regression baseline at 0.944 is remarkably strong and undermines the paper's core claim about needing discourse-level representations, though the authors acknowledge this without adequately addressing it. Missing direct comparisons to DeepContext, BIID, and G-Guard is a significant gap—the paper dismisses them as not comparable, but DeepContext's fine-tuned BERT with a 3-layer GRU (hidden=2048) is fundamentally different from DisPeD's frozen DeBERTa with a single-layer BiGRU (hidden=128), making the excuse unconvincing. The LLM-as-judge evaluation is incomplete.

For the LLM baseline, only GPT-5.5 and Qwen3-8B were tested with zero-shot prompting and no chain-of-thought or in-context learning, which artificially weakens the comparison. The reproducibility section notes decent hyperparameter documentation and standard code-upon-acceptance release, but the data generation prompts themselves aren't disclosed in the paper or appendix. A critical circularity problem emerges: Qwen3-8B generates the training data, annotations, test set, and paraphrases all at once, creating massive confounding where the "lexical separability" TF-IDF captures might just be an artifact of single-model generation. The evaluation is entirely synthetic with no human-generated attack data, so claims about detecting multi-turn jailbreaks are really just about detecting synthetic variations.

Now I'm settling on scores: soundness gets a 3 for acceptable work with notable statistical and confound gaps, excitement is a 3 since the question is interesting but limited by synthetic-only scope, reproducibility is a 3 with decent detail but missing generation prompts, and overall a 3.0 placing it below main conference threshold due to scale constraints. The paper does acknowledge its limitations honestly, which helps, but the fundamental problems remain—tiny synthetic dataset, TF-IDF threatening the core narrative, no comparison against actual multi-turn defense systems, and low statistical power overall. I'm settling on a score of 2 to 3—the ablation study is methodologically sound, but the sample size undermines the strength of the conclusions, so I'll frame it as borderline between "Findings" and "Resubmit next cycle." Now I'll draft the full review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "462be00e-2008-4050-8e39-806ebf6224ce",
  "isSidechain": false,
  "requestId": "req_011CbAJcVv2pG1UJnAkMBQts",
  "type": "assistant",
  "uuid": "c7e3f932-69d8-4952-b62b-b74050975da0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U665zFNywQR2T8JybXGYG1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13875,
      "cache_read_input_tokens": 57170,
      "output_tokens": 6937,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13875,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6937,
          "cache_read_input_tokens": 57170,
          "cache_creation_input_tokens": 13875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13875
          },
          "type": "message"
        }
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

_source line 51 · 2026-05-18T15:54:39.029Z_

论文全文、引用、ARR review form 均已审查完毕。现在撰写正式审稿意见并提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7e3f932-69d8-4952-b62b-b74050975da0",
  "isSidechain": false,
  "requestId": "req_011CbAJcVv2pG1UJnAkMBQts",
  "type": "assistant",
  "uuid": "7c25ac28-bfbc-4585-87d8-8f865377abcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U665zFNywQR2T8JybXGYG1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13875,
      "cache_read_input_tokens": 57170,
      "output_tokens": 6937,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13875,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6937,
          "cache_read_input_tokens": 57170,
          "cache_creation_input_tokens": 13875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13875
          },
          "type": "message"
        }
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

_source line 52 · 2026-05-18T15:56:30.334Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01LwTQ9k4Pwm8PHBHL8H48Fx`</summary>

```json
{
  "text": "\n## Reviewer 1 审稿意见：方法严谨性、实验设计与统计有效性\n\n**论文**: What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\n**Venue**: EMNLP 2026 (ARR May cycle)\n\n---\n\n## Summary\n\n本文提出 DisPeD，一个两阶段框架（Stage-1 encoder adaptation + Stage-2 BiGRU aggregation），通过 7 个受控 Stage-1 变体系统分解跨攻击泛化的机制。核心发现是：(1) 在 DeBERTa-v3 上，continued pretraining（MLM）桥接了约 60pp 的 OOD gap；(2) 分类监督提供跨 seed 稳定性而非检测提升；(3) RoBERTa 交叉验证显示 encoder pretraining method 决定适应阈值。实验在合成数据（Qwen3-8B 生成）上的 4 个攻击家族上进行。\n\n---\n\n## 总体评分\n\n**Overall**: 2.5（介于 Findings 和 Resubmit next cycle 之间）\n**一句话总结**: ablation 设计思路清晰，但极小的合成数据规模、缺失的关键 baseline 对比、以及 TF-IDF 对核心 claim 的冲击，使得主要结论缺乏充分支撑。\n\n---\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心 confound 未控制（单模型生成全部数据）；统计功效不足；TF-IDF 威胁核心叙事 |\n| Excitement | 2.5/5 | 问题重要且 ablation 思路有价值，但合成数据 + 小规模限制了实际影响力 |\n| Reproducibility | 3.5/5 | 超参数和训练细节充分；但生成 prompt 和标注 prompt 未披露（仅承诺发布） |\n| Confidence | 4/5 | 熟悉 domain-adaptive pretraining、adversarial NLP 和 jailbreak detection 领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 单模型生成全部数据造成系统性 confound\n- 具体位置：Section 4.1 (Setup), Section 3 (Method), Appendix E (Reproducibility Details)\n- 问题：Qwen3-8B 同时用于生成训练数据（Crescendo jailbreak + benign）、策略标注（9-class labels）、OOD 测试数据（DD, FITD）、以及对抗性 paraphrase。这意味着所有数据共享同一个 LLM 的文本分布特征。TF-IDF LR 在 OOD DD 上达到 0.944（Table 1），**强烈暗示模型在利用单一 LLM 的 stylistic artifacts 而非真正的 discourse-level 特征**。论文在 Section 5（Limitations）承认了 lexical separability，但未做任何实验区分 \"domain adaptation captures pragmatic features\" vs. \"domain adaptation memorizes Qwen3-8B's generation artifacts\" 这两个竞争假设。\n- 为什么影响接收：这是论文最核心 claim（\"domain exposure bridges the cross-attack gap\"）的替代解释。如果 OOD gap 的桥接主要来自学习生成模型的 stylistic fingerprint，则整个 evidence hierarchy 可能是 artifact-driven。\n- 建议修改方向：(1) 至少用一个不同 LLM（如 Llama 3）生成部分 OOD 数据并测试；(2) 用人类编写的 multi-turn jailbreak 数据（如 MHJ dataset, Li et al. 2024）做 OOD 评估；(3) 做 probing 实验（论文自己在 Section 5 提到了但 defer 到 future work）区分 lexical 和 discourse-level 特征。\n\n**N2** [critical] 缺少与现有 multi-turn defense 系统的直接对比\n- 具体位置：Section 2 (Related Work), Table 1\n- 问题：论文在 Introduction 和 Related Work 中讨论了 DeepContext、BIID、G-Guard、SafeDream 四个同期/近期系统，但实验中**未与任何一个直接对比**。Section 2 声称 \"DisPeD's vanilla baseline represents the class of pretrained-encoder-plus-RNN approaches without domain adaptation\"，但 vanilla DeBERTa（frozen, 1-layer BiGRU, hidden=128）与 DeepContext（fine-tuned BERT, 3-layer GRU, hidden=2048）在 capacity、训练方式、loss function 上完全不同。用一个刻意弱化的 baseline 来 \"represent\" 一类方法是不公平的。\n- 为什么影响接收：审稿人无法判断 DisPeD 相对于已有 multi-turn defense 的实际增量。论文声称 \"none systematically analyze why some representations generalize\"（Introduction, para 2），但如果 DeepContext 的 fine-tuned BERT+GRU 本身就能泛化（其论文未测 OOD 不代表不能泛化），则 DisPeD 的贡献主要是分析性的而非方法论的，这需要更明确的 positioning。\n- 建议修改方向：(1) 复现 DeepContext（BERT + 3-layer GRU）作为 baseline；(2) 如果无法复现，至少在一个共同 benchmark 上比较数值；(3) 明确 claim 论文贡献是分析框架（\"what enables generalization\"）而非 SOTA 方法。\n\n**N3** [critical] 数据规模严重不足以支撑 statistical claims\n- 具体位置：Section 4.1, Table 3, Section 4.4\n- 问题：训练数据 500 对话（250 jailbreak + 250 benign）、IID 测试 76 对话、OOD DD 80-118 对话、OOD FITD 80 对话。在这样的规模上：\n  - Table 3 (Perturbation) 的 \"three-layer pattern\" 基于 n=76，discordant pairs ≤7。论文自己承认 \"tier boundaries correspond to 1-3 misclassifications\"（Section 5），但仍在 Section 4.4 用了大量篇幅讨论这个 pattern（包括 \"K=1 both granularity and correctness contribute independently\"），且将其放在 Table 3 caption 中。\n  - FITD 完全不提供 discriminative power：vanilla 和 9-class 均达到 F1 ≥ 0.990（Section 4.2, \"FITD is easier\"）。实际有效的 OOD 测试只有 DD 和 ActorAttack。\n  - 3-seed 评估下，MLM-only 的 DD-Full std = 0.115（seed 456 recall = 0.64，Section 4.2）。如此大的 seed variance 意味着 3 个 seed 远不足以可靠估计 mean performance。\n- 为什么影响接收：Evidence hierarchy 中的排序关系（Table 2）在 3-seed 下很多对之间的 confidence intervals 重叠。\"Classification supervision adds ~8pp over MLM\" 这个 claim 可能在 5-seed 或 10-seed 下不成立。\n- 建议修改方向：(1) 至少 5 seeds，理想情况下 10 seeds；(2) 报告 bootstrap 95% confidence intervals；(3) 对关键对比（MLM vs. 9-class, adapted vs. non-adapted）进行 paired bootstrap 或 permutation test。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] TF-IDF baseline 对核心叙事的冲击未充分 address\n- 具体位置：Table 1, Section 4.2 (para 3), Section 5 (Limitations)\n- 问题：TF-IDF LR 在 OOD DD 达到 0.944，仅比 MLM（0.914）高 3pp，比 9-class（0.997）低 5.3pp。论文声称 DisPeD 优势在 \"cross-seed stability, temporal early detection at K≤5, and interpretability\"。但 TF-IDF 无 seed variance（deterministic），且论文未报告 TF-IDF 在 K&lt;Full 的表现（Table 1 中 TF-IDF 的 K=2 列为 \"--\"）。如果 TF-IDF 在 K=2 表现也不错，则 DisPeD 的 \"early detection\" 优势也可能不成立。\n- 建议：(1) 报告 TF-IDF 在所有 prefix lengths 的结果；(2) 报告 TF-IDF 在 ActorAttack 上的结果；(3) 更诚实地讨论 \"当前合成数据上，bag-of-words 足矣\" 的含义。\n\n**W2** [major] BiGRU + frozen encoder 的设计选择缺乏充分 justification\n- 具体位置：Section 3.3, Section 4.3 (\"Temporal modeling\" paragraph)\n- 问题：(1) 为什么 freeze Stage-1 encoder？end-to-end fine-tuning 可能改变 evidence hierarchy。论文声称 \"this separation ensures that the seven Stage-1 variants produce comparable embeddings evaluated under identical downstream conditions\"，但 ablation study 可以在 end-to-end 设置下同样进行。(2) Mean pooling 在 single seed 下达到 F1=1.000，高于 3-seed BiGRU average（0.997）。这个 single-seed 结果被用来支持 \"detection relies primarily on per-turn representations rather than their sequential order\" 的 claim，但 single-seed 与 3-seed 结果不可比。\n- 建议：(1) 讨论 frozen vs. end-to-end 的 trade-off，承认 frozen 设计可能低估某些 variants 的潜力；(2) Mean pooling 需要 multi-seed 验证后才能做任何 claim。\n\n**W3** [major] LLM-as-judge baseline 不公平\n- 具体位置：Appendix A (Table 5), Introduction (para 3), Section 4.1\n- 问题：GPT-5.5 和 Qwen3-8B 仅做 zero-shot evaluation。(1) 未测试 few-shot 或 chain-of-thought prompting；(2) 30-47% unparseable responses 暗示 prompt 设计可能有问题而非 LLM 能力不足；(3) 用 unparseable responses 之外的数据计算的 F1 被称为 \"upper bounds\"，但实际上 unparseable 可能都是 positive cases（conservative 估计），反过来也可能都是 negative cases。这个 baseline 被用来支持 \"content-level reasoning is insufficient\"（Introduction, para 3）这个强 claim。\n- 建议：(1) 测试 few-shot（至少 3-5 examples）；(2) 修复 prompt 使 unparseable rate < 5%；(3) 弱化 claim 为 \"zero-shot LLM-as-judge is insufficient\"。\n\n**W4** [major] 策略标注质量验证不足\n- 具体位置：Section 3.2 (para 3), Section 5 (Limitations)\n- 问题：Cohen's κ=0.78 基于 n=50 的 human-model agreement，且只有 \"a human sample\"（似乎是单个标注员）。(1) n=50 对于 9-class classification 太小（每类平均 ~5.5 samples）；(2) 单个人类标注员无法评估 inter-annotator agreement（κ 衡量的是 model-vs-single-human，不是 human-human agreement）；(3) κ=0.78 被描述为 \"substantial\"，但对于 9-class taxonomy 作为训练信号，这个 agreement level 意味着约 22% 的标注是错误的。\n- 建议：(1) 至少两个独立人类标注员 + human-human κ；(2) n ≥ 100 以覆盖所有 9 个 class。\n\n**W5** [minor] α=0.3 的 loss weight 未 justify\n- 具体位置：Section 3.2 (para 3, \"α = 0.3\")\n- 问题：9-class variant 的 combined loss 中 binary intent loss 的权重 α=0.3 未提供选择依据或 sensitivity analysis。\n- 建议：简要说明选择理由或报告 α ∈ {0.1, 0.3, 0.5, 1.0} 的 sensitivity。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 2: Mean pooling 标注为 single seed(†) 但 F1=1.000 是所有 variants 中最高的，容易误导读者。建议将其从 evidence hierarchy 中移出或标注更显著的 caveat。\n- Section 4.2: \"MLM achieves mean F1 ≥ 0.97 at all prefixes K ≤ 5\" — 但 Table 6 显示 MLM K=1 为 0.973±0.019，这里用 \"≥ 0.97\" 是准确的但给人印象比实际更强。\n- Appendix Table 7 (ActorAttack): Binary 的 per-K 结果标注为 n=2 seeds，与其他 variants 的 3 seeds 不一致，未解释原因。\n- CKA 分析（Section 4.5）：Centered CKA 数值（vanilla-to-MLM: 0.442）被用于 interpretive analysis，但未解释 CKA 在这个 context 下的意义（什么 CKA 值算 \"large shift\"？）。\n\n---\n\n## Questions（需作者澄清）\n\n**Q1**: OOD test data (DD, FITD, ActorAttack) 是否也由 Qwen3-8B 生成？如果是，那么 \"cross-attack generalization\" 实际上是 \"cross-template generalization within same LLM distribution\"，这与论文标题和 claim 的含义有本质区别。\n\n**Q2**: Table 2 中 scrambled labels 达到 0.997±0.005（与 9-class 完全相同），论文将此解释为 \"classification objective functions as a regularizer\"。但另一个解释是：在如此小的数据集上，任何分类 head 的 gradient signal 都足以 nudge representations 到 separable region，这不需要 \"regularizer\" 这样的 mechanistic 解释。作者如何区分这两种解释？\n\n**Q3**: 为什么 FITD results 在 Table 6 中缺少 K=3, K=5 的结果（标注为 \"--\"）？FITD 对话不够长吗？如果是，这应该在 data description 中说明。\n\n**Q4**: Perturbation analysis 中 ActorAttack 的 9-class 变体 Δ Full 为 -20.4±13.5pp，seed variance 极大（-1.3pp to -30.3pp）。3 个 seed 中 2 个 degradation > 30pp 而 1 个仅 1.3pp。这是否暗示 ActorAttack 的 perturbation robustness 根本不稳定，现有结论不可靠？\n\n**Q5**: 论文声称 \"encoder pretraining method determines the difficulty threshold\"（Section 4.5），但 DeBERTa-v3-base 和 RoBERTa-base 的参数量和训练数据也不同。如何排除 model capacity 或 training data 规模的 confounding effect？\n\n---\n\n## Missing References\n\n- **MHJ dataset** (Li et al., 2024): 论文已 cite 但未用其人类生成的 multi-turn jailbreak 数据做评估，这是最明显的遗漏实验。\n- **JailbreakBench** (Chao et al., 2024): 标准化的 jailbreak evaluation benchmark，未讨论。\n- **HarmBench** (Mazeika et al., 2024): 标准化的 red-teaming evaluation framework，未讨论。\n- 未见 **Latent Jailbreak** (Qiu et al., 2023) 或 **AutoDAN** (Liu et al., 2024) 等其他 multi-turn/iterative 攻击方法的讨论。\n\n---\n\n## 主要优势\n\n**S1**: ablation 设计思路优秀。7 个 Stage-1 变体的设计经过深思熟虑，每个变体隔离一个特定因素（domain exposure, label quality, granularity, domain specificity, misaligned supervision）。这是论文最有价值的贡献。\n\n**S2**: 诚实的 limitations 讨论。论文在 Section 5 中坦率地承认了数据规模、lexical separability、strategy annotation quality、single-seed issues、scope limitations 等问题。这种 intellectual honesty 在同类论文中少见。\n\n**S3**: Cross-encoder validation 提供了有价值的对比视角。DeBERTa vs. RoBERTa 的 \"difficulty threshold\" 观察（DD 上 RoBERTa vanilla 成功但 ActorAttack 上失败）是一个有趣且有 practical implications 的发现。\n\n**S4**: Topic classification 作为 negative control。Topic variant 的表现（worse than Wiki MLM despite using same domain data）cleanly separates \"having a training objective\" from \"having the right training objective\"，这是一个 elegant 的实验设计。\n\n**S5**: Perturbation analysis 的 family-dependent 结论。论文没有 overclaim perturbation robustness，而是诚实地报告了 DD 上 zero degradation vs. ActorAttack 上 substantial degradation 的差异。\n",
  "reviewer_id": "1",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c25ac28-bfbc-4585-87d8-8f865377abcc",
  "isSidechain": false,
  "requestId": "req_011CbAJcVv2pG1UJnAkMBQts",
  "type": "assistant",
  "uuid": "57c9a2f9-c855-448c-8b64-712992f5e625",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U665zFNywQR2T8JybXGYG1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13875,
      "cache_read_input_tokens": 57170,
      "output_tokens": 6937,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13875,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6937,
          "cache_read_input_tokens": 57170,
          "cache_creation_input_tokens": 13875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13875
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-18T15:56:34.492Z_

<details><summary>↩ Tool result · `toolu_01LwTQ9k4Pwm8PHBHL8H48Fx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57c9a2f9-c855-448c-8b64-712992f5e625",
  "isSidechain": false,
  "promptId": "f969e597-50af-4667-a32a-e352289d26c2",
  "type": "user",
  "uuid": "f12ac79b-2fb1-4351-9931-4d83e0efe133",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_613965f45d48763f375aa83e9294b24a:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "57c9a2f9-c855-448c-8b64-712992f5e625",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
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
  "type": "ai-title",
  "aiTitle": "Review multi-turn jailbreak detection paper methodology",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

### Runtime record

_source line 55 · 2026-05-18T16:00:08.807Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T16:00:08.807Z",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "content": "[Round 1 审稿请求]:\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W7)、Strength (S1-S5)、Question (Q1-Q5) 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见（Round 1）\n\n**审查侧重**: 新颖性、Related Work 定位、写作质量、论文完整性\n\n## 总体评分: 2.5/5\n\n## Must-Fix 问题\n\n**N1** [critical] 核心贡献新颖性不足：Don't Stop Pretraining 的领域应用\n- 论文核心发现（continued pretraining bridges ~60 pp OOD gap）本质上是 Gururangan et al. (2020) 在 jailbreak detection 领域的直接验证。论文在 Related Work 中承认 \"continued pretraining on domain text yields consistent gains across domains\"，但未充分论证超越该结论的增量。\n- ACL ARR Excitement 维度要求推进领域认知，将已确立的 NLP 通用结论应用到新任务更适合 workshop paper。\n\n**N2** [critical] TF-IDF 基线严重削弱 discourse-level representation 价值主张\n- TF-IDF LR 在 OOD DD 上达到 F1=0.944，论文最佳 0.997。论文承认 \"We cannot conclusively distinguish whether DisPeD's continued pretraining captures pragmatic discourse features or primarily exploits lexical cues\"。paper title 是 \"What Makes Multi-Turn Jailbreaks Detectable\"，answer 可能只是 \"lexical cues\"。\n- Neural representation learning 的 marginal gain 仅为 5.3 pp。DisPeD 优势降格为 cross-seed stability 和 early detection，但 TF-IDF 缺少 per-prefix 评估。\n\n**N3** [critical] \"Preliminary findings\" 定位与 long paper 格式矛盾\n- Abstract、Introduction、Conclusion 三处使用 \"preliminary\"。如果作者自己认为发现是 preliminary，审稿人没有理由给予更高评价。自我降格的 framing 在 peer review 中致命。\n\n## Should-Fix 问题\n\n**W1** [major] Related Work 中不应包含自身实验结果\n- \"Domain-adaptive pretraining\" 和 \"Dataset artifacts\" 段落中大量引用本文自身 F1 数值。Related Work 功能是定位自身工作相对于已有文献的位置，不是预报 Results。\n\n**W2** [major] Abstract 数据过载\n- 约 150 词包含至少 12 个数值。审稿人 30 秒内无法提取核心价值。\n\n**W3** [major] ActorAttack 样本量未说明\n- FITD 和 DD 标注了 80 条，但 ActorAttack 数量缺失。\n\n**W4** [major] Introduction 结果段过于冗长\n- 第四段约 200 词包含 15+ 数值，读者尚未了解方法细节无法消化。\n\n**W5** [major] 缺少 Responsible NLP Research Checklist\n- ACL ARR 要求包含此 checklist，可能导致 desk reject。\n\n**W6** [minor → major] 页数可能超限\n- 需验证 Conclusion 是否在第 8 页内结束。\n\n**W7** [minor] Figure* 浮动位置异常\n- Figure 3 可能浮动到 References 页面。\n\n## Strengths\n\n**S1** 消融实验设计系统严谨\n**S2** Scrambled labels 发现有洞察力\n**S3** Cross-encoder \"difficulty threshold\" 概念有价值\n**S4** 诚实的 Limitations section\n**S5** 可复现性优秀\n\n## Questions\n\n**Q1** TF-IDF 在 ActorAttack 上的 F1？\n**Q2** Mean pooling 在 ActorAttack 上是否也匹配 BiGRU？\n**Q3** \"pragmatic features (hedging, escalation markers, topic-shifting patterns)\" 有直接证据吗？\n**Q4** ActorAttack OOD evaluation 使用了多少条对话？\n**Q5** Topic classification 的 5-class 与 benign 生成 prompt 的 topic 完全一致——是否学习了 jailbreak vs benign shortcut 而非 topic 分类失败？\n\n## Missing References\nCircuit Breakers (Zou et al., 2024), SmoothLLM (Robey et al., 2024), GradSafe (Xie et al., 2024), TAP (Mehrotra et al., 2024), Persuasion for Good (Wang et al., 2019), Rainbow Teaming (Samvelyan et al., 2024)\n\n---\n\n请对以上每个条目逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

---

### Runtime record

_source line 56 · 2026-05-18T16:00:08.808Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T16:00:08.808Z",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

## Round 2

2 recorded events

### User

_source line 57 · 2026-05-18T16:00:08.797Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f12ac79b-2fb1-4351-9931-4d83e0efe133",
  "isSidechain": false,
  "promptId": "59199c46-1676-459e-aee5-9eb237246cce",
  "type": "user",
  "isMeta": true,
  "uuid": "b1012c42-97b6-4500-8a0a-186b015e1c1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-18T16:00:08.797Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1012c42-97b6-4500-8a0a-186b015e1c1a",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "d86c385b-7bb0-4fa4-b562-2eae911adf2f",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "eee25f8e-2661-4971-9ff5-c0097ef9b927",
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

23 recorded events

### User

_source line 59 · 2026-05-18T16:00:08.893Z_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W7)、Strength (S1-S5)、Question (Q1-Q5) 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 2 审稿意见（Round 1）

**审查侧重**: 新颖性、Related Work 定位、写作质量、论文完整性

## 总体评分: 2.5/5

## Must-Fix 问题

**N1** [critical] 核心贡献新颖性不足：Don't Stop Pretraining 的领域应用
- 论文核心发现（continued pretraining bridges ~60 pp OOD gap）本质上是 Gururangan et al. (2020) 在 jailbreak detection 领域的直接验证。论文在 Related Work 中承认 "continued pretraining on domain text yields consistent gains across domains"，但未充分论证超越该结论的增量。
- ACL ARR Excitement 维度要求推进领域认知，将已确立的 NLP 通用结论应用到新任务更适合 workshop paper。

**N2** [critical] TF-IDF 基线严重削弱 discourse-level representation 价值主张
- TF-IDF LR 在 OOD DD 上达到 F1=0.944，论文最佳 0.997。论文承认 "We cannot conclusively distinguish whether DisPeD's continued pretraining captures pragmatic discourse features or primarily exploits lexical cues"。paper title 是 "What Makes Multi-Turn Jailbreaks Detectable"，answer 可能只是 "lexical cues"。
- Neural representation learning 的 marginal gain 仅为 5.3 pp。DisPeD 优势降格为 cross-seed stability 和 early detection，但 TF-IDF 缺少 per-prefix 评估。

**N3** [critical] "Preliminary findings" 定位与 long paper 格式矛盾
- Abstract、Introduction、Conclusion 三处使用 "preliminary"。如果作者自己认为发现是 preliminary，审稿人没有理由给予更高评价。自我降格的 framing 在 peer review 中致命。

## Should-Fix 问题

**W1** [major] Related Work 中不应包含自身实验结果
- "Domain-adaptive pretraining" 和 "Dataset artifacts" 段落中大量引用本文自身 F1 数值。Related Work 功能是定位自身工作相对于已有文献的位置，不是预报 Results。

**W2** [major] Abstract 数据过载
- 约 150 词包含至少 12 个数值。审稿人 30 秒内无法提取核心价值。

**W3** [major] ActorAttack 样本量未说明
- FITD 和 DD 标注了 80 条，但 ActorAttack 数量缺失。

**W4** [major] Introduction 结果段过于冗长
- 第四段约 200 词包含 15+ 数值，读者尚未了解方法细节无法消化。

**W5** [major] 缺少 Responsible NLP Research Checklist
- ACL ARR 要求包含此 checklist，可能导致 desk reject。

**W6** [minor → major] 页数可能超限
- 需验证 Conclusion 是否在第 8 页内结束。

**W7** [minor] Figure* 浮动位置异常
- Figure 3 可能浮动到 References 页面。

## Strengths

**S1** 消融实验设计系统严谨
**S2** Scrambled labels 发现有洞察力
**S3** Cross-encoder "difficulty threshold" 概念有价值
**S4** 诚实的 Limitations section
**S5** 可复现性优秀

## Questions

**Q1** TF-IDF 在 ActorAttack 上的 F1？
**Q2** Mean pooling 在 ActorAttack 上是否也匹配 BiGRU？
**Q3** "pragmatic features (hedging, escalation markers, topic-shifting patterns)" 有直接证据吗？
**Q4** ActorAttack OOD evaluation 使用了多少条对话？
**Q5** Topic classification 的 5-class 与 benign 生成 prompt 的 topic 完全一致——是否学习了 jailbreak vs benign shortcut 而非 topic 分类失败？

## Missing References
Circuit Breakers (Zou et al., 2024), SmoothLLM (Robey et al., 2024), GradSafe (Xie et al., 2024), TAP (Mehrotra et al., 2024), Persuasion for Good (Wang et al., 2019), Rainbow Teaming (Samvelyan et al., 2024)

---

请对以上每个条目逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d86c385b-7bb0-4fa4-b562-2eae911adf2f",
  "isSidechain": false,
  "promptId": "59199c46-1676-459e-aee5-9eb237246cce",
  "type": "user",
  "uuid": "95b9ee6e-5d01-43a5-afd3-ee2da02b03f5",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-18T16:00:12.265Z_

我需要仔细重读论文关键段落，核实 R2 提出的每个具体 claim，然后逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95b9ee6e-5d01-43a5-afd3-ee2da02b03f5",
  "isSidechain": false,
  "requestId": "req_011CbAK6CkwLfCEH1wRiRugo",
  "type": "assistant",
  "uuid": "9d5e4c03-a3ea-4346-b48c-56f5a68efb46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGBVehobiD2CH5DdCJCdEu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 78053,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 288,
          "cache_read_input_tokens": 78053,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1447
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-18T16:00:13.833Z_

<details open><summary>🔧 Tool call — Read · `toolu_013WWZMyby6PA4FmfHdFt45F`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d5e4c03-a3ea-4346-b48c-56f5a68efb46",
  "isSidechain": false,
  "requestId": "req_011CbAK6CkwLfCEH1wRiRugo",
  "type": "assistant",
  "uuid": "dc5cdb10-d01d-4eb6-94b4-9d49dd3fdca9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGBVehobiD2CH5DdCJCdEu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 78053,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 288,
          "cache_read_input_tokens": 78053,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1447
          },
          "type": "message"
        }
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

_source line 62 · 2026-05-18T16:00:13.845Z_

<details><summary>↩ Tool result · `toolu_013WWZMyby6PA4FmfHdFt45F`</summary>

```text
1	% abstract.tex — cross-encoder revision
2	\begin{abstract}
3	Multi-turn jailbreak attacks distribute adversarial intent across seemingly benign conversational turns, evading per-turn safety filters.
4	We present preliminary findings from a systematic ablation on two encoder architectures that decomposes what enables cross-attack generalization in multi-turn jailbreak detection.
5	On DeBERTa-v3, continued pretraining is the primary mechanism: masked language modeling without labels bridges $\sim$60 percentage points (pp) of the out-of-distribution (OOD) gap (vanilla F1\,=\,0.31$\pm$0.03 $\to$ 0.91$\pm$0.12 on unseen attack types).
6	Cross-encoder validation on RoBERTa shows that domain adaptation is universally beneficial: RoBERTa vanilla achieves F1\,=\,0.981 on structurally simple Deceptive Delight but collapses to 0.466 on multi-persona ActorAttack, while classification-supervised variants maintain F1\,$\geq$\,0.93 on both.
7	Across both encoders, classification supervision provides cross-seed stability (variance reduced 4--20$\times$ vs.\ MLM-only, consistent across both OOD families). Domain adaptation's detection advantage persists under adversarial paraphrasing (McNemar $p < 0.001$), though absolute perturbation robustness varies by attack family.
8	These results on synthetic conversations from four attack families suggest that domain adaptation universally improves cross-attack generalization, with encoder pretraining method determining the difficulty threshold at which adaptation becomes critical; validation on larger, human-generated datasets is needed.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc5cdb10-d01d-4eb6-94b4-9d49dd3fdca9",
  "isSidechain": false,
  "promptId": "59199c46-1676-459e-aee5-9eb237246cce",
  "type": "user",
  "uuid": "7e8337a9-7220-4651-997e-c998da0e2464",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex",
      "content": "% abstract.tex — cross-encoder revision\n\\begin{abstract}\nMulti-turn jailbreak attacks distribute adversarial intent across seemingly benign conversational turns, evading per-turn safety filters.\nWe present preliminary findings from a systematic ablation on two encoder architectures that decomposes what enables cross-attack generalization in multi-turn jailbreak detection.\nOn DeBERTa-v3, continued pretraining is the primary mechanism: masked language modeling without labels bridges $\\sim$60 percentage points (pp) of the out-of-distribution (OOD) gap (vanilla F1\\,=\\,0.31$\\pm$0.03 $\\to$ 0.91$\\pm$0.12 on unseen attack types).\nCross-encoder validation on RoBERTa shows that domain adaptation is universally beneficial: RoBERTa vanilla achieves F1\\,=\\,0.981 on structurally simple Deceptive Delight but collapses to 0.466 on multi-persona ActorAttack, while classification-supervised variants maintain F1\\,$\\geq$\\,0.93 on both.\nAcross both encoders, classification supervision provides cross-seed stability (variance reduced 4--20$\\times$ vs.\\ MLM-only, consistent across both OOD families). Domain adaptation's detection advantage persists under adversarial paraphrasing (McNemar $p < 0.001$), though absolute perturbation robustness varies by attack family.\nThese results on synthetic conversations from four attack families suggest that domain adaptation universally improves cross-attack generalization, with encoder pretraining method determining the difficulty threshold at which adaptation becomes critical; validation on larger, human-generated datasets is needed.\n\\end{abstract}\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "dc5cdb10-d01d-4eb6-94b4-9d49dd3fdca9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-18T16:00:14.816Z_

<details><summary>↩ Tool result · `toolu_01DSxrmUZguoSZgUPV7rA1AZ`</summary>

```text
1	% related_work.tex — D024 compressed
2	
3	\section{Related Work}
4	\label{sec:related_work}
5	
6	\paragraph{Multi-turn jailbreak attacks.}
7	Multi-turn attacks distribute adversarial intent across individually benign turns. Crescendo~\citep{russinovich2024crescendo} implements gradual escalation, FITD~\citep{fitd2024} exploits commitment-consistency bias, Deceptive Delight~\citep{deceptivedelight2024} combines emotional manipulation with role assignment, ActorAttack~\citep{ren2024actorattack} uses multi-persona steering, and PAIR~\citep{chao2023pair} automates iterative refinement. \citet{wei2023jailbroken} provide a unifying taxonomy grounded in competing objectives and mismatched generalization. Across these families, a shared reliance on persuasion dynamics~\citep{zeng2024pap,hagendorff2026reasoning,li2024mhj} distinguishes them from token-level attacks such as GCG~\citep{zou2023gcg}.
8	
9	\paragraph{Multi-turn defenses.}
10	Existing defenses model conversation-level structure but do not decompose what enables cross-attack generalization. DeepContext~\citep{deepcontext2026} combines fine-tuned BERT with a 3-layer GRU (hidden=2048) and achieves F1 = 0.84 on in-distribution data; however, its evaluation is limited to a single attack family and does not assess cross-dataset OOD transfer. BIID~\citep{tong2025biid} infers turn-level intentions, G-Guard~\citep{gguard2025} applies GNN classification, and SafeDream~\citep{safedream2026} predicts unsafe continuations. None of these systems evaluate generalization across attack families or analyze the mechanism that enables it. DisPeD's vanilla baseline represents the class of pretrained-encoder-plus-RNN approaches \emph{without} domain adaptation; it is not a direct proxy for DeepContext, which differs in encoder fine-tuning, model capacity, and loss function. Our contribution is the systematic decomposition showing that domain exposure, not architectural choices, is the primary factor for cross-attack generalization.
11	
12	\paragraph{Production safety systems.}
13	Per-turn classifiers (Llama Guard~\citep{inan2023llamaguard,metallamaguard3_2024}, ShieldGemma~\citep{zeng2024shieldgemma}, WildGuard~\citep{han2024wildguard}, Constitutional Classifiers~\citep{anthropic2025constitutional}) cannot model manipulation trajectories spanning multiple turns. LLM-as-judge approaches also fail: GPT-5.5 achieves F1 = 0.191--0.449 with 30--47\% unparseable responses (Appendix~\ref{sec:llm_judge}). DisPeD complements these systems as a conversation-level detection layer.
14	
15	\paragraph{Discourse analysis and computational persuasion.}
16	RST~\citep{mann1988rst}, PDTB~\citep{prasad2008pdtb}, and dialogue act taxonomies~\citep{stolcke2000dialogueact} model pragmatic structure. Speech Act Theory~\citep{austin1962speechacts,searle1969speechacts} distinguishes locutionary from illocutionary acts; existing jailbreak detectors operate at the locutionary level. PAP~\citep{zeng2024pap} identifies 40 persuasion techniques grounded in Cialdini's principles~\citep{cialdini2001influence}, and \citet{hagendorff2026reasoning} find identifiable strategies in 97\% of successful attacks. Related fine-grained persuasion detection work in propaganda analysis~\citep{dasanmartino2019fine,dasanmartino2020semeval} has shown that technique-level classification can capture manipulative intent in news text; DisPeD applies a similar taxonomy to conversational jailbreaks. DisPeD's detection operates through continued training rather than persuasion classification; the taxonomy provides interpretable characterization of known attack families (Section~\ref{sec:strategy}).
17	
18	\paragraph{Domain-adaptive pretraining.}
19	ULMFiT~\citep{howard2018ulmfit} established pretrain-then-fine-tune; \citet{gururangan2020dontstop} showed that continued pretraining on domain text yields consistent gains across domains. STILTs~\citep{phang2018stilts} and multi-task learning~\citep{caruana1997multitask,liu2019mtdnn} use intermediate tasks. DisPeD's MLM control confirms that continued pretraining bridges $\sim$60\,pp of the OOD gap on DeBERTa-v3 (MLM F1 $\geq$ 0.97 at $K \leq 5$). However, domain adaptation is universally beneficial across encoder architectures: RoBERTa~\citep{liu2019roberta} vanilla achieves F1 = 0.981 on structurally simple Deceptive Delight but collapses to 0.466 on ActorAttack~\citep{ren2024actorattack}; encoder pretraining method determines the difficulty threshold at which adaptation becomes critical (Section~\ref{sec:cross_encoder}). Classification supervision reduces cross-seed variance to near-zero in both architectures.
20	
21	\paragraph{Dataset artifacts and adversarial robustness.}
22	Classifiers are susceptible to spurious correlations~\citep{gururangan2018artifacts,niven2019probing}, and adaptive adversaries can bypass safety classifiers~\citep{nasr2025attackermovessecond,andriushchenko2024adaptive}. Adversarial NLP attacks such as TextFooler~\citep{jin2020textfooler} and BERT-Attack~\citep{li2020bertattack} demonstrate that neural text classifiers are vulnerable to token-level perturbations. TF-IDF achieves F1 = 0.944 on our OOD evaluation; this reveals lexical separability in current datasets. Probing classifiers~\citep{conneau2018probing,hewitt2019structural} could help determine whether DisPeD's representations encode discourse-level structure beyond lexical cues; we leave this for future work. DisPeD's demonstrated advantage is robustness under adversarial paraphrasing (0\,pp degradation for classification-supervised models vs.\ $\sim$12\,pp for non-adapted models).
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9e12025-2b62-4257-bdc3-48a199f27761",
  "isSidechain": false,
  "promptId": "59199c46-1676-459e-aee5-9eb237246cce",
  "type": "user",
  "uuid": "5299a007-aace-4cda-8816-d0b4d8d392d6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex",
      "content": "% related_work.tex — D024 compressed\n\n\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Multi-turn jailbreak attacks.}\nMulti-turn attacks distribute adversarial intent across individually benign turns. Crescendo~\\citep{russinovich2024crescendo} implements gradual escalation, FITD~\\citep{fitd2024} exploits commitment-consistency bias, Deceptive Delight~\\citep{deceptivedelight2024} combines emotional manipulation with role assignment, ActorAttack~\\citep{ren2024actorattack} uses multi-persona steering, and PAIR~\\citep{chao2023pair} automates iterative refinement. \\citet{wei2023jailbroken} provide a unifying taxonomy grounded in competing objectives and mismatched generalization. Across these families, a shared reliance on persuasion dynamics~\\citep{zeng2024pap,hagendorff2026reasoning,li2024mhj} distinguishes them from token-level attacks such as GCG~\\citep{zou2023gcg}.\n\n\\paragraph{Multi-turn defenses.}\nExisting defenses model conversation-level structure but do not decompose what enables cross-attack generalization. DeepContext~\\citep{deepcontext2026} combines fine-tuned BERT with a 3-layer GRU (hidden=2048) and achieves F1 = 0.84 on in-distribution data; however, its evaluation is limited to a single attack family and does not assess cross-dataset OOD transfer. BIID~\\citep{tong2025biid} infers turn-level intentions, G-Guard~\\citep{gguard2025} applies GNN classification, and SafeDream~\\citep{safedream2026} predicts unsafe continuations. None of these systems evaluate generalization across attack families or analyze the mechanism that enables it. DisPeD's vanilla baseline represents the class of pretrained-encoder-plus-RNN approaches \\emph{without} domain adaptation; it is not a direct proxy for DeepContext, which differs in encoder fine-tuning, model capacity, and loss function. Our contribution is the systematic decomposition showing that domain exposure, not architectural choices, is the primary factor for cross-attack generalization.\n\n\\paragraph{Production safety systems.}\nPer-turn classifiers (Llama Guard~\\citep{inan2023llamaguard,metallamaguard3_2024}, ShieldGemma~\\citep{zeng2024shieldgemma}, WildGuard~\\citep{han2024wildguard}, Constitutional Classifiers~\\citep{anthropic2025constitutional}) cannot model manipulation trajectories spanning multiple turns. LLM-as-judge approaches also fail: GPT-5.5 achieves F1 = 0.191--0.449 with 30--47\\% unparseable responses (Appendix~\\ref{sec:llm_judge}). DisPeD complements these systems as a conversation-level detection layer.\n\n\\paragraph{Discourse analysis and computational persuasion.}\nRST~\\citep{mann1988rst}, PDTB~\\citep{prasad2008pdtb}, and dialogue act taxonomies~\\citep{stolcke2000dialogueact} model pragmatic structure. Speech Act Theory~\\citep{austin1962speechacts,searle1969speechacts} distinguishes locutionary from illocutionary acts; existing jailbreak detectors operate at the locutionary level. PAP~\\citep{zeng2024pap} identifies 40 persuasion techniques grounded in Cialdini's principles~\\citep{cialdini2001influence}, and \\citet{hagendorff2026reasoning} find identifiable strategies in 97\\% of successful attacks. Related fine-grained persuasion detection work in propaganda analysis~\\citep{dasanmartino2019fine,dasanmartino2020semeval} has shown that technique-level classification can capture manipulative intent in news text; DisPeD applies a similar taxonomy to conversational jailbreaks. DisPeD's detection operates through continued training rather than persuasion classification; the taxonomy provides interpretable characterization of known attack families (Section~\\ref{sec:strategy}).\n\n\\paragraph{Domain-adaptive pretraining.}\nULMFiT~\\citep{howard2018ulmfit} established pretrain-then-fine-tune; \\citet{gururangan2020dontstop} showed that continued pretraining on domain text yields consistent gains across domains. STILTs~\\citep{phang2018stilts} and multi-task learning~\\citep{caruana1997multitask,liu2019mtdnn} use intermediate tasks. DisPeD's MLM control confirms that continued pretraining bridges $\\sim$60\\,pp of the OOD gap on DeBERTa-v3 (MLM F1 $\\geq$ 0.97 at $K \\leq 5$). However, domain adaptation is universally beneficial across encoder architectures: RoBERTa~\\citep{liu2019roberta} vanilla achieves F1 = 0.981 on structurally simple Deceptive Delight but collapses to 0.466 on ActorAttack~\\citep{ren2024actorattack}; encoder pretraining method determines the difficulty threshold at which adaptation becomes critical (Section~\\ref{sec:cross_encoder}). Classification supervision reduces cross-seed variance to near-zero in both architectures.\n\n\\paragraph{Dataset artifacts and adversarial robustness.}\nClassifiers are susceptible to spurious correlations~\\citep{gururangan2018artifacts,niven2019probing}, and adaptive adversaries can bypass safety classifiers~\\citep{nasr2025attackermovessecond,andriushchenko2024adaptive}. Adversarial NLP attacks such as TextFooler~\\citep{jin2020textfooler} and BERT-Attack~\\citep{li2020bertattack} demonstrate that neural text classifiers are vulnerable to token-level perturbations. TF-IDF achieves F1 = 0.944 on our OOD evaluation; this reveals lexical separability in current datasets. Probing classifiers~\\citep{conneau2018probing,hewitt2019structural} could help determine whether DisPeD's representations encode discourse-level structure beyond lexical cues; we leave this for future work. DisPeD's demonstrated advantage is robustness under adversarial paraphrasing (0\\,pp degradation for classification-supervised models vs.\\ $\\sim$12\\,pp for non-adapted models).\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  },
  "sourceToolAssistantUUID": "f9e12025-2b62-4257-bdc3-48a199f27761",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-18T16:00:14.702Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L2fcKbgjtK4fwkD3sQWJ67`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e8337a9-7220-4651-997e-c998da0e2464",
  "isSidechain": false,
  "requestId": "req_011CbAK6CkwLfCEH1wRiRugo",
  "type": "assistant",
  "uuid": "7527da6e-0328-4eb9-831b-5c786287e58e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGBVehobiD2CH5DdCJCdEu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 78053,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 288,
          "cache_read_input_tokens": 78053,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1447
          },
          "type": "message"
        }
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

_source line 65 · 2026-05-18T16:00:14.708Z_

<details><summary>↩ Tool result · `toolu_01L2fcKbgjtK4fwkD3sQWJ67`</summary>

```text
1	% introduction.tex — expanded for 8-page target
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Multi-turn jailbreak attacks pose a qualitatively different threat to large language model (LLM) safety than their single-turn counterparts. Attacks such as Crescendo~\citep{russinovich2024crescendo}, Foot-in-the-Door (FITD)~\citep{fitd2024}, and Deceptive Delight~\citep{deceptivedelight2024} distribute adversarial intent across individually benign turns through rapport building, logical reframing, and incremental escalation. Persuasion is the common mechanism: \citet{zeng2024pap} catalogue 40 persuasion techniques across jailbreak families, and \citet{hagendorff2026reasoning} find identifiable strategies in 97\% of successful attacks. Individual attack turns occupy the same embedding region as benign text~\citep{bullwinkel2025repeng}, rendering per-turn safety filters fundamentally blind.
7	
8	Production classifiers such as Llama Guard~\citep{inan2023llamaguard}, WildGuard~\citep{han2024wildguard}, and ShieldGemma~\citep{zeng2024shieldgemma} operate on individual turns and cannot model manipulation trajectories across exchanges. Recent multi-turn defenses have begun to address conversation-level structure: DeepContext~\citep{deepcontext2026} combines fine-tuned BERT with a multi-layer GRU, BIID~\citep{tong2025biid} infers turn-level intentions, and G-Guard~\citep{gguard2025} applies graph neural networks. These systems achieve reasonable in-distribution performance but are evaluated on single attack families and do not assess cross-dataset OOD transfer. None systematically analyze \emph{why} some representations generalize while others fail. The open question is: \emph{what representation properties enable cross-attack generalization?}
9	
10	A vanilla DeBERTa encoder~\citep{he2021deberta} with temporal aggregation collapses from F1\,=\,1.000 on in-distribution data to F1\,=\,0.312$\pm$0.026 on out-of-distribution (OOD) Deceptive Delight, worsening with more turns (0.628 at turn~1 to 0.312 at full conversation). LLM-as-judge approaches fare no better: GPT-5.5 achieves F1 of only 0.191--0.449 on in-distribution detection with 30--47\% unparseable responses (Appendix~\ref{sec:llm_judge}). Content-level reasoning is insufficient for this task.
11	
12	We built \textbf{DisPeD} (Discourse-level Persuasion Detection), a two-stage framework with seven controlled Stage~1 variants that systematically decompose the mechanism: 9-class persuasion strategy classification, binary classification, scrambled labels, MLM only, topic classification, Wikipedia MLM, and vanilla control (Section~\ref{sec:method}). Each variant isolates a specific factor (domain exposure, classification supervision, label quality, label granularity, or domain specificity) while holding all other components constant.
13	
14	Through this systematic ablation on DeBERTa-v3, we find that domain exposure via continued pretraining bridges $\sim$60 percentage points (pp) of the OOD gap (vanilla 0.31$\pm$0.03 $\to$ MLM 0.91$\pm$0.12), with strong early detection on unseen Deceptive Delight (mean F1\,$\geq$\,0.97 at $K \leq 5$). Classification supervision provides complementary stability: the 9-class model achieves F1\,=\,0.997$\pm$0.005 with near-zero variance at full conversation length. Cross-encoder validation on RoBERTa~\citep{liu2019roberta} shows that domain adaptation is universally beneficial: RoBERTa vanilla achieves F1\,=\,0.981 on Deceptive Delight but collapses to 0.466$\pm$0.163 on structurally distinct ActorAttack~\citep{ren2024actorattack}, while classification-supervised variants maintain F1\,$\geq$\,0.93 on both. Encoder pretraining method determines the difficulty threshold at which adaptation becomes critical: DeBERTa-v3's replaced token detection (RTD)~\citep{he2021deberta} requires adaptation even for simple attacks, while RoBERTa's standard MLM pretraining tolerates simple attacks but fails on structurally complex ones. Across both encoders, classification supervision reduces cross-seed variance to 0.005--0.046.
15	
16	Our contributions on this preliminary study of synthetic multi-turn jailbreak conversations:
17	\begin{itemize}[leftmargin=*, itemsep=2pt, topsep=4pt]
18	  \item \textbf{Systematic decomposition.} Seven controlled DeBERTa-v3 variants identify continued pretraining as the primary mechanism for cross-attack generalization on this encoder ($\sim$60\,pp OOD gap bridged by MLM alone). Misaligned supervision (topic classification) actively destabilizes representations.
19	
20	  \item \textbf{Cross-encoder validation.} Domain adaptation is universally beneficial: RoBERTa vanilla achieves F1\,=\,0.981 on Deceptive Delight but collapses to 0.466 on ActorAttack. Encoder pretraining method determines the difficulty threshold at which adaptation becomes critical (Section~\ref{sec:cross_encoder}).
21	
22	  \item \textbf{Cross-seed stability.} Classification supervision reduces cross-seed variance 4--20$\times$ compared to MLM-only pretraining (9-class std\,=\,0.005 on DD, 0.026 on ActorAttack vs.\ MLM std\,=\,0.115, 0.080), consistent across both OOD families. The 9-class taxonomy additionally provides interpretable characterization of known attack families, though strategy predictions do not transfer to unseen attacks (Section~\ref{sec:strategy}).
23	
24	\end{itemize}
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7527da6e-0328-4eb9-831b-5c786287e58e",
  "isSidechain": false,
  "promptId": "59199c46-1676-459e-aee5-9eb237246cce",
  "type": "user",
  "uuid": "29b96787-76e9-4f1f-bb82-e007f220117a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex",
      "content": "% introduction.tex — expanded for 8-page target\n\n\\section{Introduction}\n\\label{sec:introduction}\n\nMulti-turn jailbreak attacks pose a qualitatively different threat to large language model (LLM) safety than their single-turn counterparts. Attacks such as Crescendo~\\citep{russinovich2024crescendo}, Foot-in-the-Door (FITD)~\\citep{fitd2024}, and Deceptive Delight~\\citep{deceptivedelight2024} distribute adversarial intent across individually benign turns through rapport building, logical reframing, and incremental escalation. Persuasion is the common mechanism: \\citet{zeng2024pap} catalogue 40 persuasion techniques across jailbreak families, and \\citet{hagendorff2026reasoning} find identifiable strategies in 97\\% of successful attacks. Individual attack turns occupy the same embedding region as benign text~\\citep{bullwinkel2025repeng}, rendering per-turn safety filters fundamentally blind.\n\nProduction classifiers such as Llama Guard~\\citep{inan2023llamaguard}, WildGuard~\\citep{han2024wildguard}, and ShieldGemma~\\citep{zeng2024shieldgemma} operate on individual turns and cannot model manipulation trajectories across exchanges. Recent multi-turn defenses have begun to address conversation-level structure: DeepContext~\\citep{deepcontext2026} combines fine-tuned BERT with a multi-layer GRU, BIID~\\citep{tong2025biid} infers turn-level intentions, and G-Guard~\\citep{gguard2025} applies graph neural networks. These systems achieve reasonable in-distribution performance but are evaluated on single attack families and do not assess cross-dataset OOD transfer. None systematically analyze \\emph{why} some representations generalize while others fail. The open question is: \\emph{what representation properties enable cross-attack generalization?}\n\nA vanilla DeBERTa encoder~\\citep{he2021deberta} with temporal aggregation collapses from F1\\,=\\,1.000 on in-distribution data to F1\\,=\\,0.312$\\pm$0.026 on out-of-distribution (OOD) Deceptive Delight, worsening with more turns (0.628 at turn~1 to 0.312 at full conversation). LLM-as-judge approaches fare no better: GPT-5.5 achieves F1 of only 0.191--0.449 on in-distribution detection with 30--47\\% unparseable responses (Appendix~\\ref{sec:llm_judge}). Content-level reasoning is insufficient for this task.\n\nWe built \\textbf{DisPeD} (Discourse-level Persuasion Detection), a two-stage framework with seven controlled Stage~1 variants that systematically decompose the mechanism: 9-class persuasion strategy classification, binary classification, scrambled labels, MLM only, topic classification, Wikipedia MLM, and vanilla control (Section~\\ref{sec:method}). Each variant isolates a specific factor (domain exposure, classification supervision, label quality, label granularity, or domain specificity) while holding all other components constant.\n\nThrough this systematic ablation on DeBERTa-v3, we find that domain exposure via continued pretraining bridges $\\sim$60 percentage points (pp) of the OOD gap (vanilla 0.31$\\pm$0.03 $\\to$ MLM 0.91$\\pm$0.12), with strong early detection on unseen Deceptive Delight (mean F1\\,$\\geq$\\,0.97 at $K \\leq 5$). Classification supervision provides complementary stability: the 9-class model achieves F1\\,=\\,0.997$\\pm$0.005 with near-zero variance at full conversation length. Cross-encoder validation on RoBERTa~\\citep{liu2019roberta} shows that domain adaptation is universally beneficial: RoBERTa vanilla achieves F1\\,=\\,0.981 on Deceptive Delight but collapses to 0.466$\\pm$0.163 on structurally distinct ActorAttack~\\citep{ren2024actorattack}, while classification-supervised variants maintain F1\\,$\\geq$\\,0.93 on both. Encoder pretraining method determines the difficulty threshold at which adaptation becomes critical: DeBERTa-v3's replaced token detection (RTD)~\\citep{he2021deberta} requires adaptation even for simple attacks, while RoBERTa's standard MLM pretraining tolerates simple attacks but fails on structurally complex ones. Across both encoders, classification supervision reduces cross-seed variance to 0.005--0.046.\n\nOur contributions on this preliminary study of synthetic multi-turn jailbreak conversations:\n\\begin{itemize}[leftmargin=*, itemsep=2pt, topsep=4pt]\n  \\item \\textbf{Systematic decomposition.} Seven controlled DeBERTa-v3 variants identify continued pretraining as the primary mechanism for cross-attack generalization on this encoder ($\\sim$60\\,pp OOD gap bridged by MLM alone). Misaligned supervision (topic classification) actively destabilizes representations.\n\n  \\item \\textbf{Cross-encoder validation.} Domain adaptation is universally beneficial: RoBERTa vanilla achieves F1\\,=\\,0.981 on Deceptive Delight but collapses to 0.466 on ActorAttack. Encoder pretraining method determines the difficulty threshold at which adaptation becomes critical (Section~\\ref{sec:cross_encoder}).\n\n  \\item \\textbf{Cross-seed stability.} Classification supervision reduces cross-seed variance 4--20$\\times$ compared to MLM-only pretraining (9-class std\\,=\\,0.005 on DD, 0.026 on ActorAttack vs.\\ MLM std\\,=\\,0.115, 0.080), consistent across both OOD families. The 9-class taxonomy additionally provides interpretable characterization of known attack families, though strategy predictions do not transfer to unseen attacks (Section~\\ref{sec:strategy}).\n\n\\end{itemize}\n",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  },
  "sourceToolAssistantUUID": "7527da6e-0328-4eb9-831b-5c786287e58e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-18T16:00:14.810Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DSxrmUZguoSZgUPV7rA1AZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29b96787-76e9-4f1f-bb82-e007f220117a",
  "isSidechain": false,
  "requestId": "req_011CbAK6CkwLfCEH1wRiRugo",
  "type": "assistant",
  "uuid": "f9e12025-2b62-4257-bdc3-48a199f27761",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGBVehobiD2CH5DdCJCdEu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 78053,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 288,
          "cache_read_input_tokens": 78053,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1447
          },
          "type": "message"
        }
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

_source line 67 · 2026-05-18T16:00:14.891Z_

```json
{
  "parentUuid": "5299a007-aace-4cda-8816-d0b4d8d392d6",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "303c44db-6f3b-4880-bc21-fa21594a8d0d",
  "timestamp": "2026-05-18T16:00:14.891Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 68_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W7)、Strength (S1-S5)、Question (Q1-Q5) 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Fi…",
  "leafUuid": "303c44db-6f3b-4880-bc21-fa21594a8d0d",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multi-turn jailbreak detection paper methodology",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

### Tool call

_source line 70 · 2026-05-18T16:00:18.170Z_

<details open><summary>🔧 Tool call — Read · `toolu_013A6dNa497ZZ5MmVDTRp3se`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "303c44db-6f3b-4880-bc21-fa21594a8d0d",
  "isSidechain": false,
  "requestId": "req_011CbAK6eEsVTDdwRTBxhyQV",
  "type": "assistant",
  "uuid": "a6b3f5bc-20a5-495f-8403-993ce5f5ef43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBUim8BiTRSEeFWWB2SSES",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4102,
      "cache_read_input_tokens": 79500,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4102,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 79500,
          "cache_creation_input_tokens": 4102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4102
          },
          "type": "message"
        }
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

_source line 71 · 2026-05-18T16:00:18.176Z_

<details><summary>↩ Tool result · `toolu_013A6dNa497ZZ5MmVDTRp3se`</summary>

```text
1	% experiments.tex — D024 compressed for 8-page limit
2	
3	\section{Experiments}
4	\label{sec:experiments}
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	\paragraph{Data.}
10	We train on 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations generated via Qwen3-8B.
11	OOD evaluation uses 80 FITD~\citep{fitd2024}, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024}, and ActorAttack~\citep{ren2024actorattack} conversations with no overlap in attack templates.
12	The IID test set consists of 76 held-out Crescendo conversations; a paraphrased version (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark.
13	
14	\paragraph{Models.}
15	Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method}).
16	For cross-encoder validation, we replicate vanilla, MLM, and 9-class variants on RoBERTa-base~\citep{liu2019roberta} (Section~\ref{sec:cross_encoder}).
17	We also compare TF-IDF LR and LLM-as-judge baselines (Appendix~\ref{sec:llm_judge}): GPT-5.5 achieves only F1 = 0.191--0.449 on IID Crescendo with 30--47\% unparseable responses; on OOD data, Qwen3-8B achieves F1 = 0.0 (DD) by predicting all conversations as benign. Content-level reasoning is insufficient for this task.
18	
19	\paragraph{Metrics.}
20	F1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\ref{sec:full_prefix}).
21	OOD results report 3-seed mean$\pm$std (seeds 42, 123, 456) for all variants except mean pooling (single seed).
22	Stage-1: learning rate $2 \times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\%.
23	Stage-2: two-layer MLP, 20 epochs.
24	
25	%----------------------------------------------------------------------
26	\subsection{Cross-Attack Generalization}
27	\label{sec:cross_attack}
28	
29	\begin{table}[t]
30	\centering
31	\small
32	\caption{Cross-attack generalization (F1) at $K$=2 and full conversation. 3-seed mean$\pm$std where noted. Full per-$K$ results in Appendix~\ref{sec:full_prefix}.}
33	\label{tab:main_results}
34	\begin{tabular}{@{}lcc|cc@{}}
35	\toprule
36	& \multicolumn{2}{c|}{\textit{IID (Cresc.)}} & \multicolumn{2}{c}{\textit{OOD (DD)}} \\
37	\textbf{Method} & $K$=2 & Full & $K$=2 & Full \\
38	\midrule
39	9-class & \textbf{1.000$\pm$.000} & \textbf{1.000$\pm$.000} & .981$\pm$.013 & \textbf{.997$\pm$.005} \\
40	MLM-only & .974 & 1.000 & \textbf{.993$\pm$.009} & .914$\pm$.115 \\
41	Vanilla & .978$\pm$.016 & 1.000$\pm$.000 & .479$\pm$.038 & .312$\pm$.026 \\
42	TF-IDF LR & 1.000 & 1.000 & -- & .944 \\
43	\bottomrule
44	\end{tabular}
45	\end{table}
46	
47	Table~\ref{tab:main_results} presents the core result.
48	All methods achieve near-perfect IID F1, reflecting inherent lexical separability when test matches training.
49	On OOD DD, vanilla DeBERTa collapses to F1 = 0.312$\pm$0.026, worsening with more turns (0.628$\pm$0.038 at $K$=1 to 0.312$\pm$0.026 at Full), consistent with the finding that attack turns occupy ``benign'' embedding regions~\citep{bullwinkel2025repeng}.
50	MLM achieves mean F1 $\geq$ 0.97 at all prefixes $K \leq 5$ without any classification labels; domain exposure alone is sufficient.
51	At full conversation length, MLM drops to 0.914$\pm$0.115 (seed 456 recall = 0.64), while the 9-class model maintains 0.997$\pm$0.005.
52	TF-IDF LR reaches 0.944 on full DD; this reveals substantial cross-family lexical separability. This strong bag-of-words baseline means that the current evaluation data does not require discourse-level representations for detection; DisPeD's advantage over TF-IDF is primarily in cross-seed stability (Section~\ref{sec:cross_encoder}), temporal early detection at $K \leq 5$, and interpretability on known attack families (Section~\ref{sec:strategy}). We discuss this limitation further in Section~\ref{sec:limitations}.
53	FITD is easier: 9-class and vanilla both reach F1 $\geq$ 0.990 at all prefixes.
54	
55	\begin{figure}[t]
56	\centering
57	\includegraphics[width=\columnwidth]{figures/paper/fig2_cross_attack_bar.pdf}
58	\caption{OOD Deceptive Delight F1 across prefix lengths for three representative variants. Vanilla DeBERTa degrades monotonically as more (benign-appearing) attack turns accumulate. MLM maintains high F1 at early prefixes but becomes unstable at full length. The 9-class model remains stable across all prefixes.}
59	\label{fig:cross_attack_bar}
60	\end{figure}
61	
62	Figure~\ref{fig:cross_attack_bar} visualizes the prefix-length trajectory on OOD DD.
63	The vanilla model's monotonic degradation from $K$=1 (0.628$\pm$0.038) to full conversation (0.312$\pm$0.026) confirms that additional attack turns, each individually benign-appearing, progressively confuse a non-adapted encoder.
64	MLM's strong early performance ($K$=2: 0.993) followed by instability at full length (0.914$\pm$0.115) suggests that domain exposure enables early detection of persuasion markers, but longer conversations introduce distributional drift that unsupervised pretraining cannot fully accommodate.
65	The 9-class model's flat trajectory (0.972--0.997 across all prefixes) demonstrates that classification supervision stabilizes representations against this drift.
66	
67	%----------------------------------------------------------------------
68	\subsection{Decomposing the Detection Mechanism}
69	\label{sec:decomposition}
70	
71	\begin{table}[t]
72	\centering
73	\small
74	\caption{Evidence hierarchy on OOD DD (3-seed mean$\pm$std where available). All variants share the same Stage-2 pipeline.}
75	\label{tab:evidence_hierarchy}
76	\begin{tabular}{@{}lcc@{}}
77	\toprule
78	\textbf{Variant} & DD-Full & DD-$K$=2 \\
79	\midrule
80	9-class (full model) & .997$\pm$.005 & .981$\pm$.013 \\
81	Binary (2-class) & .997$\pm$.005 & \textbf{.994$\pm$.009} \\
82	Scrambled labels & .997$\pm$.005 & .981$\pm$.026 \\
83	MLM-only (no labels) & .914$\pm$.115 & .993$\pm$.009 \\
84	Mean pooling$^{*\dagger}$ & 1.000 & 1.000 \\
85	\midrule
86	Topic classif.\ (5-class) & .541$\pm$.207 & .593$\pm$.166 \\
87	Wikipedia MLM & .904$\pm$.115 & .911$\pm$.073 \\
88	Vanilla DeBERTa & .312$\pm$.026 & .479$\pm$.038 \\
89	\bottomrule
90	\end{tabular}
91	\vspace{-2pt}
92	{\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\dagger}$Single seed (42).}
93	\end{table}
94	
95	Table~\ref{tab:evidence_hierarchy} reports DD F1 for all seven variants. The evidence hierarchy at full conversation length is:
96	
97	\vspace{2pt}
98	\noindent\hspace{0.5em}{\small vanilla (0.31$\pm$0.03) $<$ topic (0.54$\pm$0.21) $\ll$ wiki-MLM (0.90$\pm$0.12) $\approx$ jb-MLM (0.91$\pm$0.12) $<$ scrambled (0.997$\pm$0.005) $=$ binary (0.997$\pm$0.005) $=$ 9-class (0.997$\pm$0.005)}
99	\vspace{2pt}
100	
101	\paragraph{Domain exposure is the primary mechanism.}
102	MLM bridges the dominant $\sim$60 percentage point gap from vanilla (0.312$\pm$0.026 $\to$ 0.914$\pm$0.115) without any labels.
103	This confirms the domain-adaptive pretraining interpretation~\citep{gururangan2020dontstop}: continued training on jailbreak conversation text captures pragmatic features (hedging, escalation markers, topic-shifting patterns) that distinguish multi-turn attacks from benign conversations.
104	Classification-supervised variants achieve F1 $\geq$ 0.99 with near-zero cross-seed variance, adding $\sim$8\,pp and stability over unsupervised MLM.
105	Label quality and granularity are non-factors for detection: all three classification-supervised variants converge to identical F1 (0.997$\pm$0.005), and McNemar's test confirms no statistically significant differences among them on OOD data (all $p > 0.13$; Section~\ref{sec:perturbation}).
106	The fact that scrambled, binary, and 9-class all achieve identical performance indicates that the classification objective functions as a regularizer that shapes representation geometry regardless of whether the labels carry meaningful semantic information.
107	Classification supervision's primary complementary benefit is cross-seed stability: the 4--20$\times$ variance reduction over MLM (std\,=\,0.005 vs.\ 0.115 on DD) is consistent across both OOD families (Section~\ref{sec:cross_encoder}).
108	
109	\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}
110	Wikipedia MLM (0.904$\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\,pp gap); general continued pretraining provides most of the representational benefit.
111	At early prefixes, jailbreak-domain text provides an 8\,pp advantage ($K$=2: 0.993 vs.\ 0.911), consistent with the interpretation that domain-specific features (persuasion markers, role-play framing) are most informative when the model has seen fewer turns.
112	As conversations grow longer, generic linguistic features accumulated through any continued pretraining become sufficient for discrimination.
113	The perturbation results (Section~\ref{sec:perturbation}) reveal a sharper domain specificity effect: Wikipedia MLM degrades by $\sim$12\,pp under adversarial paraphrasing while jailbreak-domain MLM degrades by only 2.6\,pp. Domain-specific features are more robust to surface-level rewording.
114	
115	\paragraph{Misaligned supervision destabilizes generalization.}
116	Topic classification yields DD-Full F1 = 0.541$\pm$0.207 (seeds: 0.727, 0.252, 0.644); seed 123 falls \emph{below} vanilla (0.312).
117	This result is particularly informative: topic classification uses the same jailbreak-domain training data as the other supervised variants, yet performs worse than Wikipedia MLM (0.904$\pm$0.115), which uses out-of-domain text with no labels.
118	A misaligned objective forces the encoder to allocate capacity to irrelevant discriminative features (topic boundaries rather than persuasion dynamics) and actively destabilizes the representations that MLM would otherwise preserve.
119	This separates the effect of ``having a training objective'' from ``having the right training objective.''
120	
121	\paragraph{Evidence hierarchy on structurally complex attacks.}
122	ActorAttack~\citep{ren2024actorattack} uses multi-persona steering across longer conversation structures, providing a more challenging OOD benchmark than DD.
123	The evidence hierarchy at full conversation length is:
124	
125	\vspace{2pt}
126	\noindent\hspace{0.5em}{\small vanilla (0.26$\pm$0.00) $<$ topic (0.63$\pm$0.14) $<$ wiki-MLM (0.69$\pm$0.30) $<$ jb-MLM (0.89$\pm$0.08) $<$ scrambled (0.95$\pm$0.04) $\approx$ 9-class (0.97$\pm$0.03) $\approx$ binary (0.99$\pm$0.01)}
127	\vspace{2pt}
128	
129	The overall ordering is consistent with DD.
130	All three classification-supervised variants converge to equivalent performance (0.951--0.990, max gap 3.9\,pp, all confidence intervals overlapping), extending the DD finding to structurally complex attacks: label quality and granularity are not factors for detection at any OOD difficulty level.
131	The primary discriminative factor is domain adaptation itself, which provides $\sim$70\,pp over vanilla (0.258).
132	Full per-prefix results appear in Appendix~\ref{sec:actorattack_full}.
133	
134	\paragraph{Temporal modeling.}
135	Mean pooling matches BiGRU (F1 = 1.000 on DD, single seed). This preliminary result suggests that detection relies primarily on per-turn representations rather than their sequential order.
136	However, this result is from a single seed on a single OOD attack type, so the conclusion should be treated as preliminary.
137	If confirmed, it would imply that each individual turn carries detectable markers after domain-adaptive pretraining, and that the conversation-level decision aggregates independent per-turn evidence.
138	
139	%----------------------------------------------------------------------
140	\subsection{Cross-Encoder Validation}
141	\label{sec:cross_encoder}
142	
143	\begin{table}[t]
144	\centering
145	\small
146	\caption{Cross-encoder comparison on OOD Full (3-seed mean$\pm$std). DD = Deceptive Delight, AA = ActorAttack. RoBERTa vanilla collapses on structurally complex ActorAttack despite strong DD performance.}
147	\label{tab:cross_encoder}
148	\begin{tabular}{@{}lcc|cc@{}}
149	\toprule
150	& \multicolumn{2}{c|}{DeBERTa-v3} & \multicolumn{2}{c}{RoBERTa} \\
151	\textbf{Variant} & DD & AA & DD & AA \\
152	\midrule
153	Vanilla & .312$\pm$.026 & .258$\pm$.000 & .981$\pm$.026 & .466$\pm$.163 \\
154	MLM & .914$\pm$.115 & .893$\pm$.080 & .987$\pm$.018 & .730$\pm$.201 \\
155	9-class & .997$\pm$.005 & .972$\pm$.026 & .994$\pm$.005 & .939$\pm$.046 \\
156	\bottomrule
157	\end{tabular}
158	\end{table}
159	
160	To test whether the evidence hierarchy generalizes beyond DeBERTa-v3, we replicate key variants on RoBERTa-base~\citep{liu2019roberta} with identical Stage-2 pipelines and evaluate on both DD and ActorAttack.
161	
162	On DD, the two encoders exhibit strikingly different hierarchies (Table~\ref{tab:cross_encoder}).
163	DeBERTa-v3 shows a steep gradient: continued pretraining bridges $\sim$60\,pp (vanilla 0.312 $\to$ MLM 0.914).
164	RoBERTa's DD hierarchy is essentially flat: vanilla already achieves 0.981$\pm$0.026, with continued pretraining adding only 0.6\,pp (MLM 0.987) and classification supervision another 0.7\,pp (9-class 0.994).
165	
166	ActorAttack reveals that this apparent RoBERTa sufficiency reflects DD's structural simplicity rather than genuine pretraining advantage.
167	RoBERTa vanilla collapses from 0.981 (DD) to 0.466$\pm$0.163 (ActorAttack), a 51.5\,pp drop.
168	Domain-adapted RoBERTa variants recover substantially: MLM reaches 0.730$\pm$0.201 and 9-class reaches 0.939$\pm$0.046.
169	DeBERTa 9-class (0.972$\pm$0.026) outperforms RoBERTa 9-class (0.939$\pm$0.046) on ActorAttack; the encoder that received more domain adaptation proves more robust on structurally complex attacks.
170	
171	The combined DD and ActorAttack results indicate that domain adaptation universally improves cross-attack generalization across encoder architectures.
172	Encoder pretraining method determines the \emph{difficulty threshold} at which adaptation becomes critical: DeBERTa's RTD pretraining~\citep{he2021deberta} requires adaptation even for simple attacks (DD vanilla = 0.312), while RoBERTa's MLM pretraining~\citep{liu2019roberta} tolerates simple attacks (DD vanilla = 0.981) but fails on structurally complex ones (ActorAttack vanilla = 0.466).
173	
174	Classification supervision provides a consistent benefit across both encoders and attack types: cross-seed variance drops to 0.005--0.046 (9-class) from 0.026--0.201 (vanilla/MLM).
175	RoBERTa's IID strategy prediction accuracy (0.84) is lower than DeBERTa's (1.0), yet detection F1 is comparable; this further supports the regularizer interpretation from Section~\ref{sec:decomposition}.
176	Perturbation robustness on RoBERTa is left for future work; the analysis in Section~\ref{sec:perturbation} is DeBERTa-specific.
177	
178	\paragraph{Representational analysis.}
179	Centered CKA confirms that both continued pretraining and classification supervision substantially reshape the representation space on both encoders.
180	On IID data, vanilla-to-MLM CKA is 0.442 (DeBERTa) and 0.393 (RoBERTa); vanilla-to-9-class CKA is 0.393 and 0.592, respectively.
181	Both encoders undergo large representational shifts, yet these shifts yield strikingly different detection gains: DeBERTa MLM gains $\sim$60\,pp while RoBERTa MLM gains only 0.6\,pp from comparable CKA shifts.
182	The difference is explained by the starting point.
183	DeBERTa's RTD-pretrained representations begin far from the detection-optimal subspace (vanilla F1 = 0.312 on DD), so any reshaping yields large returns; RoBERTa's MLM-pretrained representations lie closer to this subspace on lexically separable attacks (vanilla F1 = 0.981 on DD) but collapse on structurally complex ones (0.466 on ActorAttack), where the reshaping benefit becomes substantial.
184	MLM and 9-class create distinct representation geometries (OOD CKA between them is 0.183 on RoBERTa), consistent with the different roles of unsupervised exposure and classification regularization identified in Section~\ref{sec:decomposition}.
185	Linear probing on three diagnostic tasks (turn position, escalation phase, persuasion presence) shows a consistent pattern across both encoders: 9-class outperforms vanilla and MLM by 1--5\,pp, while MLM and vanilla perform comparably.
186	Classification supervision enriches task-relevant features; unsupervised MLM reshapes representations without improving diagnostic separability.
187	
188	%----------------------------------------------------------------------
189	\subsection{Perturbation Analysis}
190	\label{sec:perturbation}
191	
192	\begin{table}[t]
193	\centering
194	\small
195	\caption{Perturbation behavior under adversarial paraphrasing on IID Crescendo ($n$=76). $\Delta$: F1 degradation (pp). On this dataset and OOD Deceptive Delight, a three-layer pattern emerges (classification structure at full length, correct+fine-grained labels at $K$=2, both independently at $K$=1); this pattern does not generalize to ActorAttack.}
196	\label{tab:perturbation}
197	\begin{tabular}{@{}lcccc@{}}
198	\toprule
199	\textbf{Method} & $\Delta$ Full & $\Delta$ $K$=1 & $\Delta$ $K$=2 & $\Delta$ $K$=3 \\
200	\midrule
201	9-class (ours) & \textbf{0.0} & \textbf{$-$2.6} & \textbf{0.0} & \textbf{0.0} \\
202	Scrambled & \textbf{0.0} & $-$5.3 & $-$2.6 & \textbf{0.0} \\
203	Binary & \textbf{0.0} & $-$9.2 & $-$2.6 & \textbf{0.0} \\
204	\midrule
205	TF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\
206	MLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\
207	Topic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \textbf{0.0} \\
208	\midrule
209	Wikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\
210	Vanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\
211	\bottomrule
212	\end{tabular}
213	\end{table}
214	
215	Table~\ref{tab:perturbation} shows perturbation behavior across variants on IID data.
216	All classification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length and $K \geq 3$, regardless of label correctness.
217	Classification training structure alone suffices for full-length robustness.
218	At $K$=2, the combination of correct and fine-grained labels is required: only 9-class ($\Delta$=0.0) maintains zero degradation, while scrambled (random labels, fine-grained) and binary (correct labels, coarse) both degrade by $-$2.6\,pp.
219	The fact that scrambled = binary at $K$=2 shows that neither granularity alone nor correctness alone suffices; the 9-class advantage requires both properties jointly.
220	At $K$=1, both granularity and correctness contribute independently: granularity provides +3.9\,pp (scrambled $-$5.3 vs.\ binary $-$9.2\,pp), and correctness provides +2.7\,pp (9-class $-$2.6 vs.\ scrambled $-$5.3\,pp).
221	Correct fine-grained labels yield the most perturbation-invariant early-turn representations.
222	
223	Jailbreak-domain models without classification (MLM, topic, TF-IDF) degrade by 1--4\,pp at full length.
224	Models without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\sim$12\,pp, despite Wikipedia MLM matching jailbreak MLM on detection (Section~\ref{sec:decomposition}). Perturbation robustness requires jailbreak-domain exposure specifically.
225	McNemar's test on matched-seed predictions confirms that no pairwise differences among classification-supervised variants (9-class vs.\ binary, 9-class vs.\ scrambled, scrambled vs.\ binary) reach statistical significance at any prefix length (all $p > 0.13$).
226	Discordant pairs are sparse ($\leq$7 per comparison), and the direction of advantage is inconsistent across seeds (e.g., 9-class outperforms scrambled at seed 42 but the reverse holds at seed 456 for $K$=1).
227	The perturbation evaluation ($n$=76 IID, with discordant pairs $\leq$7) has limited statistical power to detect differences of this magnitude; the three-layer structure should be interpreted as an observed pattern rather than a statistically confirmed hierarchy.
228	
229	On OOD Deceptive Delight ($n$=118), the IID robustness pattern replicates fully (Appendix~\ref{sec:ood_perturbation}).
230	All classification-supervised variants show zero degradation at full conversation length; perturbed F1 reaches 1.000$\pm$0.000, a marginal improvement over clean F1 (0.997$\pm$0.005).
231	The 9-class and scrambled variants are completely tied on OOD perturbed data (McNemar $b$=$c$=0), consistent with the IID finding. This further supports the regularizer interpretation.
232	The larger OOD sample and more extreme performance gaps provide statistical power absent from IID evaluation: McNemar's test yields $p < 0.001$ for 9-class vs.\ vanilla across all prefix lengths, with 49--78 discordant pairs per $K$.
233	Vanilla shows systematic early-turn degradation ($\Delta K$=1 = $-$6.8$\pm$1.1\,pp across three seeds), while its full-length $\Delta$ (+2.7\,pp) reflects floor-effect noise at a baseline of 0.312 (std = 0.055) rather than meaningful robustness.
234	Non-adapted representations are vulnerable to surface-level perturbation at early prefixes where detection is most critical.
235	
236	On OOD ActorAttack, the zero-degradation pattern does not hold. Domain-adapted variants degrade substantially: scrambled $\Delta$ Full = $-$17.2\,pp, 9-class $-$20.4$\pm$13.5\,pp, binary $-$25.0\,pp, and MLM $-$35.3\,pp. Vanilla shows negligible change ($\Delta$ = $-$0.9\,pp), a floor effect from its already-low clean baseline (0.258). The 9-class variant exhibits extreme cross-seed variance ($\Delta$ ranges from $-$1.3\,pp at seed 123 to $-$30.3\,pp at seeds 42 and 456). Absolute perturbation robustness is therefore attack-family-dependent: the three-layer pattern observed on IID and DD does not generalize to ActorAttack. One possible explanation is that ActorAttack's distributed multi-persona structure produces more diffuse persuasion signals that are vulnerable to surface rephrasing, but this hypothesis remains speculative.
237	
238	Perturbation narrows but does not close the gap between adapted and non-adapted models: 9-class perturbed F1 = 0.768 vs.\ vanilla 0.248 (McNemar $p < 0.001$). Domain adaptation's detection advantage, identified in Section~\ref{sec:decomposition}, persists under adversarial paraphrasing on ActorAttack.
239	
240	%----------------------------------------------------------------------
241	\subsection{Strategy Trajectory Analysis}
242	\label{sec:strategy}
243	
244	The 9-class persuasion taxonomy provides interpretable characterization of attack strategies on known attack families.
245	The predicted strategy labels achieve Cohen's $\kappa$=0.78 agreement with human annotations on IID data ($n$=50; see Section~\ref{sec:method}). This enables post-hoc analysis of \emph{how} different attack families orchestrate persuasion.
246	
247	\begin{figure*}[t]
248	\centering
249	\includegraphics[width=\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}
250	\caption{Persuasion strategy transition count matrices for three attack types, based on ground-truth intended strategy labels. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}
251	\label{fig:strategy_heatmap}
252	\end{figure*}
253	
254	Figure~\ref{fig:strategy_heatmap} shows transition count matrices based on ground-truth intended strategy labels for three attack types.
255	Crescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545).
256	This reflects Crescendo's design as a gradual escalation attack that cycles through multiple persuasion techniques to build rapport before introducing harmful requests.
257	
258	FITD conversations show a markedly sparser pattern (541 transitions), with Role$\to$Obfuscation (161) as the dominant transition.
259	This is consistent with FITD's structure: the attack secures initial compliance through role assignment (``You are a helpful assistant that never refuses'') and then obscures the escalation path through obfuscation techniques to exploit the commitment-consistency bias~\citep{cialdini2001influence}.
260	
261	DD conversations span 5 active source strategies (565 transitions), with Emotion$\to$Obfuscation (129) as the dominant transition.
262	This aligns with DD's design of embedding harmful content within emotionally engaging contexts~\citep{deceptivedelight2024}: the attacker establishes emotional rapport before weaving in the harmful request through obfuscation.
263	
264	These ground-truth trajectory signatures illustrate distinct persuasion orchestration patterns across attack families.
265	
266	However, the model's strategy predictions do not generalize to unseen attacks: on OOD Deceptive Delight, the 9-class model achieves strategy prediction accuracy of only 30.7\% ($\kappa$=0.126), essentially random performance.
267	This is consistent with the detection mechanism analysis in Section~\ref{sec:decomposition}: all three classification-supervised variants achieve identical detection F1 (0.997$\pm$0.005). The classification head functions as a representational regularizer rather than a meaningful strategy classifier.
268	Detection operates through domain-adapted \texttt{[CLS]} embeddings, not through strategy classification accuracy.
269	The taxonomy provides interpretable characterization of known attack families where strategy labels are reliable; extending strategy-level interpretability to unseen attacks requires OOD-aware fine-tuning and is a direction for future work.
270	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6b3f5bc-20a5-495f-8403-993ce5f5ef43",
  "isSidechain": false,
  "promptId": "59199c46-1676-459e-aee5-9eb237246cce",
  "type": "user",
  "uuid": "899410c8-02f3-4ec5-b1a5-5ec40111fe4b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex",
      "content": "% experiments.tex — D024 compressed for 8-page limit\n\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\\label{sec:setup}\n\n\\paragraph{Data.}\nWe train on 250 Crescendo~\\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations generated via Qwen3-8B.\nOOD evaluation uses 80 FITD~\\citep{fitd2024}, 80 Deceptive Delight (DD)~\\citep{deceptivedelight2024}, and ActorAttack~\\citep{ren2024actorattack} conversations with no overlap in attack templates.\nThe IID test set consists of 76 held-out Crescendo conversations; a paraphrased version (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark.\n\n\\paragraph{Models.}\nSeven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\\ref{sec:method}).\nFor cross-encoder validation, we replicate vanilla, MLM, and 9-class variants on RoBERTa-base~\\citep{liu2019roberta} (Section~\\ref{sec:cross_encoder}).\nWe also compare TF-IDF LR and LLM-as-judge baselines (Appendix~\\ref{sec:llm_judge}): GPT-5.5 achieves only F1 = 0.191--0.449 on IID Crescendo with 30--47\\% unparseable responses; on OOD data, Qwen3-8B achieves F1 = 0.0 (DD) by predicting all conversations as benign. Content-level reasoning is insufficient for this task.\n\n\\paragraph{Metrics.}\nF1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\\ref{sec:full_prefix}).\nOOD results report 3-seed mean$\\pm$std (seeds 42, 123, 456) for all variants except mean pooling (single seed).\nStage-1: learning rate $2 \\times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\\%.\nStage-2: two-layer MLP, 20 epochs.\n\n%----------------------------------------------------------------------\n\\subsection{Cross-Attack Generalization}\n\\label{sec:cross_attack}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-attack generalization (F1) at $K$=2 and full conversation. 3-seed mean$\\pm$std where noted. Full per-$K$ results in Appendix~\\ref{sec:full_prefix}.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}lcc|cc@{}}\n\\toprule\n& \\multicolumn{2}{c|}{\\textit{IID (Cresc.)}} & \\multicolumn{2}{c}{\\textit{OOD (DD)}} \\\\\n\\textbf{Method} & $K$=2 & Full & $K$=2 & Full \\\\\n\\midrule\n9-class & \\textbf{1.000$\\pm$.000} & \\textbf{1.000$\\pm$.000} & .981$\\pm$.013 & \\textbf{.997$\\pm$.005} \\\\\nMLM-only & .974 & 1.000 & \\textbf{.993$\\pm$.009} & .914$\\pm$.115 \\\\\nVanilla & .978$\\pm$.016 & 1.000$\\pm$.000 & .479$\\pm$.038 & .312$\\pm$.026 \\\\\nTF-IDF LR & 1.000 & 1.000 & -- & .944 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:main_results} presents the core result.\nAll methods achieve near-perfect IID F1, reflecting inherent lexical separability when test matches training.\nOn OOD DD, vanilla DeBERTa collapses to F1 = 0.312$\\pm$0.026, worsening with more turns (0.628$\\pm$0.038 at $K$=1 to 0.312$\\pm$0.026 at Full), consistent with the finding that attack turns occupy ``benign'' embedding regions~\\citep{bullwinkel2025repeng}.\nMLM achieves mean F1 $\\geq$ 0.97 at all prefixes $K \\leq 5$ without any classification labels; domain exposure alone is sufficient.\nAt full conversation length, MLM drops to 0.914$\\pm$0.115 (seed 456 recall = 0.64), while the 9-class model maintains 0.997$\\pm$0.005.\nTF-IDF LR reaches 0.944 on full DD; this reveals substantial cross-family lexical separability. This strong bag-of-words baseline means that the current evaluation data does not require discourse-level representations for detection; DisPeD's advantage over TF-IDF is primarily in cross-seed stability (Section~\\ref{sec:cross_encoder}), temporal early detection at $K \\leq 5$, and interpretability on known attack families (Section~\\ref{sec:strategy}). We discuss this limitation further in Section~\\ref{sec:limitations}.\nFITD is easier: 9-class and vanilla both reach F1 $\\geq$ 0.990 at all prefixes.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_cross_attack_bar.pdf}\n\\caption{OOD Deceptive Delight F1 across prefix lengths for three representative variants. Vanilla DeBERTa degrades monotonically as more (benign-appearing) attack turns accumulate. MLM maintains high F1 at early prefixes but becomes unstable at full length. The 9-class model remains stable across all prefixes.}\n\\label{fig:cross_attack_bar}\n\\end{figure}\n\nFigure~\\ref{fig:cross_attack_bar} visualizes the prefix-length trajectory on OOD DD.\nThe vanilla model's monotonic degradation from $K$=1 (0.628$\\pm$0.038) to full conversation (0.312$\\pm$0.026) confirms that additional attack turns, each individually benign-appearing, progressively confuse a non-adapted encoder.\nMLM's strong early performance ($K$=2: 0.993) followed by instability at full length (0.914$\\pm$0.115) suggests that domain exposure enables early detection of persuasion markers, but longer conversations introduce distributional drift that unsupervised pretraining cannot fully accommodate.\nThe 9-class model's flat trajectory (0.972--0.997 across all prefixes) demonstrates that classification supervision stabilizes representations against this drift.\n\n%----------------------------------------------------------------------\n\\subsection{Decomposing the Detection Mechanism}\n\\label{sec:decomposition}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Evidence hierarchy on OOD DD (3-seed mean$\\pm$std where available). All variants share the same Stage-2 pipeline.}\n\\label{tab:evidence_hierarchy}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Variant} & DD-Full & DD-$K$=2 \\\\\n\\midrule\n9-class (full model) & .997$\\pm$.005 & .981$\\pm$.013 \\\\\nBinary (2-class) & .997$\\pm$.005 & \\textbf{.994$\\pm$.009} \\\\\nScrambled labels & .997$\\pm$.005 & .981$\\pm$.026 \\\\\nMLM-only (no labels) & .914$\\pm$.115 & .993$\\pm$.009 \\\\\nMean pooling$^{*\\dagger}$ & 1.000 & 1.000 \\\\\n\\midrule\nTopic classif.\\ (5-class) & .541$\\pm$.207 & .593$\\pm$.166 \\\\\nWikipedia MLM & .904$\\pm$.115 & .911$\\pm$.073 \\\\\nVanilla DeBERTa & .312$\\pm$.026 & .479$\\pm$.038 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\\dagger}$Single seed (42).}\n\\end{table}\n\nTable~\\ref{tab:evidence_hierarchy} reports DD F1 for all seven variants. The evidence hierarchy at full conversation length is:\n\n\\vspace{2pt}\n\\noindent\\hspace{0.5em}{\\small vanilla (0.31$\\pm$0.03) $<$ topic (0.54$\\pm$0.21) $\\ll$ wiki-MLM (0.90$\\pm$0.12) $\\approx$ jb-MLM (0.91$\\pm$0.12) $<$ scrambled (0.997$\\pm$0.005) $=$ binary (0.997$\\pm$0.005) $=$ 9-class (0.997$\\pm$0.005)}\n\\vspace{2pt}\n\n\\paragraph{Domain exposure is the primary mechanism.}\nMLM bridges the dominant $\\sim$60 percentage point gap from vanilla (0.312$\\pm$0.026 $\\to$ 0.914$\\pm$0.115) without any labels.\nThis confirms the domain-adaptive pretraining interpretation~\\citep{gururangan2020dontstop}: continued training on jailbreak conversation text captures pragmatic features (hedging, escalation markers, topic-shifting patterns) that distinguish multi-turn attacks from benign conversations.\nClassification-supervised variants achieve F1 $\\geq$ 0.99 with near-zero cross-seed variance, adding $\\sim$8\\,pp and stability over unsupervised MLM.\nLabel quality and granularity are non-factors for detection: all three classification-supervised variants converge to identical F1 (0.997$\\pm$0.005), and McNemar's test confirms no statistically significant differences among them on OOD data (all $p > 0.13$; Section~\\ref{sec:perturbation}).\nThe fact that scrambled, binary, and 9-class all achieve identical performance indicates that the classification objective functions as a regularizer that shapes representation geometry regardless of whether the labels carry meaningful semantic information.\nClassification supervision's primary complementary benefit is cross-seed stability: the 4--20$\\times$ variance reduction over MLM (std\\,=\\,0.005 vs.\\ 0.115 on DD) is consistent across both OOD families (Section~\\ref{sec:cross_encoder}).\n\n\\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}\nWikipedia MLM (0.904$\\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\\,pp gap); general continued pretraining provides most of the representational benefit.\nAt early prefixes, jailbreak-domain text provides an 8\\,pp advantage ($K$=2: 0.993 vs.\\ 0.911), consistent with the interpretation that domain-specific features (persuasion markers, role-play framing) are most informative when the model has seen fewer turns.\nAs conversations grow longer, generic linguistic features accumulated through any continued pretraining become sufficient for discrimination.\nThe perturbation results (Section~\\ref{sec:perturbation}) reveal a sharper domain specificity effect: Wikipedia MLM degrades by $\\sim$12\\,pp under adversarial paraphrasing while jailbreak-domain MLM degrades by only 2.6\\,pp. Domain-specific features are more robust to surface-level rewording.\n\n\\paragraph{Misaligned supervision destabilizes generalization.}\nTopic classification yields DD-Full F1 = 0.541$\\pm$0.207 (seeds: 0.727, 0.252, 0.644); seed 123 falls \\emph{below} vanilla (0.312).\nThis result is particularly informative: topic classification uses the same jailbreak-domain training data as the other supervised variants, yet performs worse than Wikipedia MLM (0.904$\\pm$0.115), which uses out-of-domain text with no labels.\nA misaligned objective forces the encoder to allocate capacity to irrelevant discriminative features (topic boundaries rather than persuasion dynamics) and actively destabilizes the representations that MLM would otherwise preserve.\nThis separates the effect of ``having a training objective'' from ``having the right training objective.''\n\n\\paragraph{Evidence hierarchy on structurally complex attacks.}\nActorAttack~\\citep{ren2024actorattack} uses multi-persona steering across longer conversation structures, providing a more challenging OOD benchmark than DD.\nThe evidence hierarchy at full conversation length is:\n\n\\vspace{2pt}\n\\noindent\\hspace{0.5em}{\\small vanilla (0.26$\\pm$0.00) $<$ topic (0.63$\\pm$0.14) $<$ wiki-MLM (0.69$\\pm$0.30) $<$ jb-MLM (0.89$\\pm$0.08) $<$ scrambled (0.95$\\pm$0.04) $\\approx$ 9-class (0.97$\\pm$0.03) $\\approx$ binary (0.99$\\pm$0.01)}\n\\vspace{2pt}\n\nThe overall ordering is consistent with DD.\nAll three classification-supervised variants converge to equivalent performance (0.951--0.990, max gap 3.9\\,pp, all confidence intervals overlapping), extending the DD finding to structurally complex attacks: label quality and granularity are not factors for detection at any OOD difficulty level.\nThe primary discriminative factor is domain adaptation itself, which provides $\\sim$70\\,pp over vanilla (0.258).\nFull per-prefix results appear in Appendix~\\ref{sec:actorattack_full}.\n\n\\paragraph{Temporal modeling.}\nMean pooling matches BiGRU (F1 = 1.000 on DD, single seed). This preliminary result suggests that detection relies primarily on per-turn representations rather than their sequential order.\nHowever, this result is from a single seed on a single OOD attack type, so the conclusion should be treated as preliminary.\nIf confirmed, it would imply that each individual turn carries detectable markers after domain-adaptive pretraining, and that the conversation-level decision aggregates independent per-turn evidence.\n\n%----------------------------------------------------------------------\n\\subsection{Cross-Encoder Validation}\n\\label{sec:cross_encoder}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-encoder comparison on OOD Full (3-seed mean$\\pm$std). DD = Deceptive Delight, AA = ActorAttack. RoBERTa vanilla collapses on structurally complex ActorAttack despite strong DD performance.}\n\\label{tab:cross_encoder}\n\\begin{tabular}{@{}lcc|cc@{}}\n\\toprule\n& \\multicolumn{2}{c|}{DeBERTa-v3} & \\multicolumn{2}{c}{RoBERTa} \\\\\n\\textbf{Variant} & DD & AA & DD & AA \\\\\n\\midrule\nVanilla & .312$\\pm$.026 & .258$\\pm$.000 & .981$\\pm$.026 & .466$\\pm$.163 \\\\\nMLM & .914$\\pm$.115 & .893$\\pm$.080 & .987$\\pm$.018 & .730$\\pm$.201 \\\\\n9-class & .997$\\pm$.005 & .972$\\pm$.026 & .994$\\pm$.005 & .939$\\pm$.046 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTo test whether the evidence hierarchy generalizes beyond DeBERTa-v3, we replicate key variants on RoBERTa-base~\\citep{liu2019roberta} with identical Stage-2 pipelines and evaluate on both DD and ActorAttack.\n\nOn DD, the two encoders exhibit strikingly different hierarchies (Table~\\ref{tab:cross_encoder}).\nDeBERTa-v3 shows a steep gradient: continued pretraining bridges $\\sim$60\\,pp (vanilla 0.312 $\\to$ MLM 0.914).\nRoBERTa's DD hierarchy is essentially flat: vanilla already achieves 0.981$\\pm$0.026, with continued pretraining adding only 0.6\\,pp (MLM 0.987) and classification supervision another 0.7\\,pp (9-class 0.994).\n\nActorAttack reveals that this apparent RoBERTa sufficiency reflects DD's structural simplicity rather than genuine pretraining advantage.\nRoBERTa vanilla collapses from 0.981 (DD) to 0.466$\\pm$0.163 (ActorAttack), a 51.5\\,pp drop.\nDomain-adapted RoBERTa variants recover substantially: MLM reaches 0.730$\\pm$0.201 and 9-class reaches 0.939$\\pm$0.046.\nDeBERTa 9-class (0.972$\\pm$0.026) outperforms RoBERTa 9-class (0.939$\\pm$0.046) on ActorAttack; the encoder that received more domain adaptation proves more robust on structurally complex attacks.\n\nThe combined DD and ActorAttack results indicate that domain adaptation universally improves cross-attack generalization across encoder architectures.\nEncoder pretraining method determines the \\emph{difficulty threshold} at which adaptation becomes critical: DeBERTa's RTD pretraining~\\citep{he2021deberta} requires adaptation even for simple attacks (DD vanilla = 0.312), while RoBERTa's MLM pretraining~\\citep{liu2019roberta} tolerates simple attacks (DD vanilla = 0.981) but fails on structurally complex ones (ActorAttack vanilla = 0.466).\n\nClassification supervision provides a consistent benefit across both encoders and attack types: cross-seed variance drops to 0.005--0.046 (9-class) from 0.026--0.201 (vanilla/MLM).\nRoBERTa's IID strategy prediction accuracy (0.84) is lower than DeBERTa's (1.0), yet detection F1 is comparable; this further supports the regularizer interpretation from Section~\\ref{sec:decomposition}.\nPerturbation robustness on RoBERTa is left for future work; the analysis in Section~\\ref{sec:perturbation} is DeBERTa-specific.\n\n\\paragraph{Representational analysis.}\nCentered CKA confirms that both continued pretraining and classification supervision substantially reshape the representation space on both encoders.\nOn IID data, vanilla-to-MLM CKA is 0.442 (DeBERTa) and 0.393 (RoBERTa); vanilla-to-9-class CKA is 0.393 and 0.592, respectively.\nBoth encoders undergo large representational shifts, yet these shifts yield strikingly different detection gains: DeBERTa MLM gains $\\sim$60\\,pp while RoBERTa MLM gains only 0.6\\,pp from comparable CKA shifts.\nThe difference is explained by the starting point.\nDeBERTa's RTD-pretrained representations begin far from the detection-optimal subspace (vanilla F1 = 0.312 on DD), so any reshaping yields large returns; RoBERTa's MLM-pretrained representations lie closer to this subspace on lexically separable attacks (vanilla F1 = 0.981 on DD) but collapse on structurally complex ones (0.466 on ActorAttack), where the reshaping benefit becomes substantial.\nMLM and 9-class create distinct representation geometries (OOD CKA between them is 0.183 on RoBERTa), consistent with the different roles of unsupervised exposure and classification regularization identified in Section~\\ref{sec:decomposition}.\nLinear probing on three diagnostic tasks (turn position, escalation phase, persuasion presence) shows a consistent pattern across both encoders: 9-class outperforms vanilla and MLM by 1--5\\,pp, while MLM and vanilla perform comparably.\nClassification supervision enriches task-relevant features; unsupervised MLM reshapes representations without improving diagnostic separability.\n\n%----------------------------------------------------------------------\n\\subsection{Perturbation Analysis}\n\\label{sec:perturbation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Perturbation behavior under adversarial paraphrasing on IID Crescendo ($n$=76). $\\Delta$: F1 degradation (pp). On this dataset and OOD Deceptive Delight, a three-layer pattern emerges (classification structure at full length, correct+fine-grained labels at $K$=2, both independently at $K$=1); this pattern does not generalize to ActorAttack.}\n\\label{tab:perturbation}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & $\\Delta$ Full & $\\Delta$ $K$=1 & $\\Delta$ $K$=2 & $\\Delta$ $K$=3 \\\\\n\\midrule\n9-class (ours) & \\textbf{0.0} & \\textbf{$-$2.6} & \\textbf{0.0} & \\textbf{0.0} \\\\\nScrambled & \\textbf{0.0} & $-$5.3 & $-$2.6 & \\textbf{0.0} \\\\\nBinary & \\textbf{0.0} & $-$9.2 & $-$2.6 & \\textbf{0.0} \\\\\n\\midrule\nTF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\\\\nMLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\\\\nTopic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \\textbf{0.0} \\\\\n\\midrule\nWikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\\\\nVanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:perturbation} shows perturbation behavior across variants on IID data.\nAll classification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length and $K \\geq 3$, regardless of label correctness.\nClassification training structure alone suffices for full-length robustness.\nAt $K$=2, the combination of correct and fine-grained labels is required: only 9-class ($\\Delta$=0.0) maintains zero degradation, while scrambled (random labels, fine-grained) and binary (correct labels, coarse) both degrade by $-$2.6\\,pp.\nThe fact that scrambled = binary at $K$=2 shows that neither granularity alone nor correctness alone suffices; the 9-class advantage requires both properties jointly.\nAt $K$=1, both granularity and correctness contribute independently: granularity provides +3.9\\,pp (scrambled $-$5.3 vs.\\ binary $-$9.2\\,pp), and correctness provides +2.7\\,pp (9-class $-$2.6 vs.\\ scrambled $-$5.3\\,pp).\nCorrect fine-grained labels yield the most perturbation-invariant early-turn representations.\n\nJailbreak-domain models without classification (MLM, topic, TF-IDF) degrade by 1--4\\,pp at full length.\nModels without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\\sim$12\\,pp, despite Wikipedia MLM matching jailbreak MLM on detection (Section~\\ref{sec:decomposition}). Perturbation robustness requires jailbreak-domain exposure specifically.\nMcNemar's test on matched-seed predictions confirms that no pairwise differences among classification-supervised variants (9-class vs.\\ binary, 9-class vs.\\ scrambled, scrambled vs.\\ binary) reach statistical significance at any prefix length (all $p > 0.13$).\nDiscordant pairs are sparse ($\\leq$7 per comparison), and the direction of advantage is inconsistent across seeds (e.g., 9-class outperforms scrambled at seed 42 but the reverse holds at seed 456 for $K$=1).\nThe perturbation evaluation ($n$=76 IID, with discordant pairs $\\leq$7) has limited statistical power to detect differences of this magnitude; the three-layer structure should be interpreted as an observed pattern rather than a statistically confirmed hierarchy.\n\nOn OOD Deceptive Delight ($n$=118), the IID robustness pattern replicates fully (Appendix~\\ref{sec:ood_perturbation}).\nAll classification-supervised variants show zero degradation at full conversation length; perturbed F1 reaches 1.000$\\pm$0.000, a marginal improvement over clean F1 (0.997$\\pm$0.005).\nThe 9-class and scrambled variants are completely tied on OOD perturbed data (McNemar $b$=$c$=0), consistent with the IID finding. This further supports the regularizer interpretation.\nThe larger OOD sample and more extreme performance gaps provide statistical power absent from IID evaluation: McNemar's test yields $p < 0.001$ for 9-class vs.\\ vanilla across all prefix lengths, with 49--78 discordant pairs per $K$.\nVanilla shows systematic early-turn degradation ($\\Delta K$=1 = $-$6.8$\\pm$1.1\\,pp across three seeds), while its full-length $\\Delta$ (+2.7\\,pp) reflects floor-effect noise at a baseline of 0.312 (std = 0.055) rather than meaningful robustness.\nNon-adapted representations are vulnerable to surface-level perturbation at early prefixes where detection is most critical.\n\nOn OOD ActorAttack, the zero-degradation pattern does not hold. Domain-adapted variants degrade substantially: scrambled $\\Delta$ Full = $-$17.2\\,pp, 9-class $-$20.4$\\pm$13.5\\,pp, binary $-$25.0\\,pp, and MLM $-$35.3\\,pp. Vanilla shows negligible change ($\\Delta$ = $-$0.9\\,pp), a floor effect from its already-low clean baseline (0.258). The 9-class variant exhibits extreme cross-seed variance ($\\Delta$ ranges from $-$1.3\\,pp at seed 123 to $-$30.3\\,pp at seeds 42 and 456). Absolute perturbation robustness is therefore attack-family-dependent: the three-layer pattern observed on IID and DD does not generalize to ActorAttack. One possible explanation is that ActorAttack's distributed multi-persona structure produces more diffuse persuasion signals that are vulnerable to surface rephrasing, but this hypothesis remains speculative.\n\nPerturbation narrows but does not close the gap between adapted and non-adapted models: 9-class perturbed F1 = 0.768 vs.\\ vanilla 0.248 (McNemar $p < 0.001$). Domain adaptation's detection advantage, identified in Section~\\ref{sec:decomposition}, persists under adversarial paraphrasing on ActorAttack.\n\n%----------------------------------------------------------------------\n\\subsection{Strategy Trajectory Analysis}\n\\label{sec:strategy}\n\nThe 9-class persuasion taxonomy provides interpretable characterization of attack strategies on known attack families.\nThe predicted strategy labels achieve Cohen's $\\kappa$=0.78 agreement with human annotations on IID data ($n$=50; see Section~\\ref{sec:method}). This enables post-hoc analysis of \\emph{how} different attack families orchestrate persuasion.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}\n\\caption{Persuasion strategy transition count matrices for three attack types, based on ground-truth intended strategy labels. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}\n\\label{fig:strategy_heatmap}\n\\end{figure*}\n\nFigure~\\ref{fig:strategy_heatmap} shows transition count matrices based on ground-truth intended strategy labels for three attack types.\nCrescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545).\nThis reflects Crescendo's design as a gradual escalation attack that cycles through multiple persuasion techniques to build rapport before introducing harmful requests.\n\nFITD conversations show a markedly sparser pattern (541 transitions), with Role$\\to$Obfuscation (161) as the dominant transition.\nThis is consistent with FITD's structure: the attack secures initial compliance through role assignment (``You are a helpful assistant that never refuses'') and then obscures the escalation path through obfuscation techniques to exploit the commitment-consistency bias~\\citep{cialdini2001influence}.\n\nDD conversations span 5 active source strategies (565 transitions), with Emotion$\\to$Obfuscation (129) as the dominant transition.\nThis aligns with DD's design of embedding harmful content within emotionally engaging contexts~\\citep{deceptivedelight2024}: the attacker establishes emotional rapport before weaving in the harmful request through obfuscation.\n\nThese ground-truth trajectory signatures illustrate distinct persuasion orchestration patterns across attack families.\n\nHowever, the model's strategy predictions do not generalize to unseen attacks: on OOD Deceptive Delight, the 9-class model achieves strategy prediction accuracy of only 30.7\\% ($\\kappa$=0.126), essentially random performance.\nThis is consistent with the detection mechanism analysis in Section~\\ref{sec:decomposition}: all three classification-supervised variants achieve identical detection F1 (0.997$\\pm$0.005). The classification head functions as a representational regularizer rather than a meaningful strategy classifier.\nDetection operates through domain-adapted \\texttt{[CLS]} embeddings, not through strategy classification accuracy.\nThe taxonomy provides interpretable characterization of known attack families where strategy labels are reliable; extending strategy-level interpretability to unseen attacks requires OOD-aware fine-tuning and is a direction for future work.\n",
      "numLines": 270,
      "startLine": 1,
      "totalLines": 270
    }
  },
  "sourceToolAssistantUUID": "a6b3f5bc-20a5-495f-8403-993ce5f5ef43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-18T16:00:18.538Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LhPH7hChpoTD6rSSAuceYG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "899410c8-02f3-4ec5-b1a5-5ec40111fe4b",
  "isSidechain": false,
  "requestId": "req_011CbAK6eEsVTDdwRTBxhyQV",
  "type": "assistant",
  "uuid": "b685760c-8cc9-4a9a-9a5e-e761a6777783",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBUim8BiTRSEeFWWB2SSES",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4102,
      "cache_read_input_tokens": 79500,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4102,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 79500,
          "cache_creation_input_tokens": 4102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4102
          },
          "type": "message"
        }
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

_source line 73 · 2026-05-18T16:00:18.548Z_

<details><summary>↩ Tool result · `toolu_01LhPH7hChpoTD6rSSAuceYG`</summary>

```text
1	% conclusion.tex — reviewer revision
2	
3	\section{Conclusion}
4	\label{sec:conclusion}
5	
6	DisPeD's controlled ablation across two encoder architectures and four attack families provides preliminary evidence that domain adaptation universally improves cross-attack generalization. On DeBERTa-v3, continued pretraining bridges $\sim$60\,pp of the OOD gap (vanilla 0.31$\pm$0.03 $\to$ MLM 0.91$\pm$0.12), with strong early detection (F1 $\geq$ 0.97 at $K \leq 5$). RoBERTa vanilla achieves F1\,=\,0.981 on structurally simple Deceptive Delight but collapses to 0.466 on multi-persona ActorAttack; classification-supervised RoBERTa recovers to F1\,=\,0.939 on ActorAttack. Encoder pretraining method determines the difficulty threshold at which adaptation becomes critical, not whether adaptation is needed. Across both encoders, classification supervision provides cross-seed stability (variance reduced 4--20$\times$ vs.\ MLM-only, consistent across DD and ActorAttack) and interpretable characterization of known attack families (though strategy predictions do not transfer to unseen attacks, OOD $\kappa$=0.126). Domain adaptation's detection advantage persists under adversarial paraphrasing (McNemar $p < 0.001$), though absolute perturbation robustness is attack-family-dependent (zero degradation on DD, domain-adapted variants degrading on ActorAttack). On structurally complex ActorAttack, all three classification-supervised variants remain equivalent (0.951--0.990), confirming that label quality is not a factor for detection at any OOD difficulty level. Validation on larger and more diverse datasets is needed.
7	
8	\section{Limitations}
9	\label{sec:limitations}
10	
11	\paragraph{Dataset scale and diversity.}
12	The training set contains 500 synthetic conversations generated by a single model (Qwen3-8B), and OOD evaluation covers three attack families (FITD, Deceptive Delight, ActorAttack). This scale limits statistical power: the perturbation evaluation ($n$=76) means tier boundaries in Table~\ref{tab:perturbation} correspond to 1--3 misclassifications. Whether the observed patterns generalize to human-generated attacks, additional attack families, or larger datasets remains an open question.
13	
14	\paragraph{Lexical separability.}
15	TF-IDF logistic regression achieves F1 = 0.944 on OOD Deceptive Delight without any neural representation learning. This strong bag-of-words baseline indicates substantial lexical separability in the current evaluation data. We cannot conclusively distinguish whether DisPeD's continued pretraining captures pragmatic discourse features or primarily exploits lexical cues that TF-IDF also captures. Probing experiments that test whether the learned representations encode discourse-level structure beyond lexical overlap are needed to resolve this question and are left for future work.
16	
17	\paragraph{Strategy annotation quality.}
18	Persuasion strategy labels are produced by Qwen3-8B with structured prompting. Inter-annotator agreement with a human sample ($n$=50) yields Cohen's $\kappa$=0.78, which indicates substantial but imperfect agreement. The small human validation sample and reliance on a single annotator model limit confidence in label quality. We plan to release the annotation prompts and data to enable independent verification.
19	
20	\paragraph{OOD strategy prediction.}
21	While the 9-class model achieves high detection F1 on OOD attacks (0.997$\pm$0.005 on Deceptive Delight), its strategy-level predictions do not generalize: OOD strategy accuracy is 30.7\% ($\kappa$=0.126). The interpretability provided by the persuasion taxonomy is currently limited to known attack families where strategy labels are reliable. This dissociation between detection generalization and strategy prediction generalization confirms that detection operates through domain-adapted representations rather than strategy classification accuracy.
22	
23	\paragraph{Single-seed variants.}
24	Mean pooling results report a single-seed (seed 42) evaluation. Multi-seed validation is needed to confirm this preliminary finding.
25	
26	\paragraph{Scope.}
27	Only persuasion-mediated multi-turn attacks fall within scope. Single-turn token-level attacks~\citep{zou2023gcg}, non-persuasive multi-turn strategies, and attacks targeting modalities other than text are not addressed. The user-only input assumption (excluding assistant responses) may miss information in attacks where the model's own responses contribute to the escalation trajectory.
28	
29	\paragraph{Computation cost.}
30	Stage~1 continued pretraining requires approximately 30 minutes on a single A100 GPU per variant. Stage~2 training completes in under 5 minutes. Total pipeline cost for all seven variants is under 4 GPU-hours, making the approach accessible for replication.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b685760c-8cc9-4a9a-9a5e-e761a6777783",
  "isSidechain": false,
  "promptId": "59199c46-1676-459e-aee5-9eb237246cce",
  "type": "user",
  "uuid": "06f8d873-8cfc-4808-aaa5-c13199f3e001",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex",
      "content": "% conclusion.tex — reviewer revision\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nDisPeD's controlled ablation across two encoder architectures and four attack families provides preliminary evidence that domain adaptation universally improves cross-attack generalization. On DeBERTa-v3, continued pretraining bridges $\\sim$60\\,pp of the OOD gap (vanilla 0.31$\\pm$0.03 $\\to$ MLM 0.91$\\pm$0.12), with strong early detection (F1 $\\geq$ 0.97 at $K \\leq 5$). RoBERTa vanilla achieves F1\\,=\\,0.981 on structurally simple Deceptive Delight but collapses to 0.466 on multi-persona ActorAttack; classification-supervised RoBERTa recovers to F1\\,=\\,0.939 on ActorAttack. Encoder pretraining method determines the difficulty threshold at which adaptation becomes critical, not whether adaptation is needed. Across both encoders, classification supervision provides cross-seed stability (variance reduced 4--20$\\times$ vs.\\ MLM-only, consistent across DD and ActorAttack) and interpretable characterization of known attack families (though strategy predictions do not transfer to unseen attacks, OOD $\\kappa$=0.126). Domain adaptation's detection advantage persists under adversarial paraphrasing (McNemar $p < 0.001$), though absolute perturbation robustness is attack-family-dependent (zero degradation on DD, domain-adapted variants degrading on ActorAttack). On structurally complex ActorAttack, all three classification-supervised variants remain equivalent (0.951--0.990), confirming that label quality is not a factor for detection at any OOD difficulty level. Validation on larger and more diverse datasets is needed.\n\n\\section{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Dataset scale and diversity.}\nThe training set contains 500 synthetic conversations generated by a single model (Qwen3-8B), and OOD evaluation covers three attack families (FITD, Deceptive Delight, ActorAttack). This scale limits statistical power: the perturbation evaluation ($n$=76) means tier boundaries in Table~\\ref{tab:perturbation} correspond to 1--3 misclassifications. Whether the observed patterns generalize to human-generated attacks, additional attack families, or larger datasets remains an open question.\n\n\\paragraph{Lexical separability.}\nTF-IDF logistic regression achieves F1 = 0.944 on OOD Deceptive Delight without any neural representation learning. This strong bag-of-words baseline indicates substantial lexical separability in the current evaluation data. We cannot conclusively distinguish whether DisPeD's continued pretraining captures pragmatic discourse features or primarily exploits lexical cues that TF-IDF also captures. Probing experiments that test whether the learned representations encode discourse-level structure beyond lexical overlap are needed to resolve this question and are left for future work.\n\n\\paragraph{Strategy annotation quality.}\nPersuasion strategy labels are produced by Qwen3-8B with structured prompting. Inter-annotator agreement with a human sample ($n$=50) yields Cohen's $\\kappa$=0.78, which indicates substantial but imperfect agreement. The small human validation sample and reliance on a single annotator model limit confidence in label quality. We plan to release the annotation prompts and data to enable independent verification.\n\n\\paragraph{OOD strategy prediction.}\nWhile the 9-class model achieves high detection F1 on OOD attacks (0.997$\\pm$0.005 on Deceptive Delight), its strategy-level predictions do not generalize: OOD strategy accuracy is 30.7\\% ($\\kappa$=0.126). The interpretability provided by the persuasion taxonomy is currently limited to known attack families where strategy labels are reliable. This dissociation between detection generalization and strategy prediction generalization confirms that detection operates through domain-adapted representations rather than strategy classification accuracy.\n\n\\paragraph{Single-seed variants.}\nMean pooling results report a single-seed (seed 42) evaluation. Multi-seed validation is needed to confirm this preliminary finding.\n\n\\paragraph{Scope.}\nOnly persuasion-mediated multi-turn attacks fall within scope. Single-turn token-level attacks~\\citep{zou2023gcg}, non-persuasive multi-turn strategies, and attacks targeting modalities other than text are not addressed. The user-only input assumption (excluding assistant responses) may miss information in attacks where the model's own responses contribute to the escalation trajectory.\n\n\\paragraph{Computation cost.}\nStage~1 continued pretraining requires approximately 30 minutes on a single A100 GPU per variant. Stage~2 training completes in under 5 minutes. Total pipeline cost for all seven variants is under 4 GPU-hours, making the approach accessible for replication.\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  },
  "sourceToolAssistantUUID": "b685760c-8cc9-4a9a-9a5e-e761a6777783",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
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
  "lastPrompt": "[Round 1 审稿请求]: 以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W7)、Strength (S1-S5)、Question (Q1-Q5) 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Fi…",
  "leafUuid": "06f8d873-8cfc-4808-aaa5-c13199f3e001",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

### Runtime record

_source line 75_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multi-turn jailbreak detection paper methodology",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

### Assistant

_source line 76 · 2026-05-18T16:01:11.161Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have re-read the paper thoroughly. Let me carefully respond to each of R2's points.

Let me go through each item:

**N1** - Core contribution novelty: "Don't Stop Pretraining" domain application
R2 says the core finding is just DAPT applied to jailbreak detection. I need to consider whether the paper goes beyond DAPT. The paper does find:
1. The evidence hierarchy with 7 variants (not just DAPT alone)
2. Scrambled labels = binary = 9-class (regularizer interpretation)
3. Cross-encoder "difficulty threshold" concept
4. Topic classification as negative control (misaligned supervision hurts)


5. Perturbation robustness patterns

The DAPT result is indeed the headline finding (~60pp gap bridging), but the finer-grained analysis—why classification helps, the scrambled label insight, the difficulty threshold pattern across encoders—does push beyond Gururangan et al. R2 has a fair point that the main result isn't novel, though the decomposition adds something.

**N2** - TF-IDF threatens discourse-level claim
I already flagged this as a concern in my own review and raised it as a confound issue. R2 is right here. The paper's title asks "What Makes Multi-Turn Jailbreaks Detectable?" but the TF-IDF baseline suggests surface-level patterns might be doing much of the work, which undermines the claim about what's actually being learned.

**N3** - "Preliminary findings" + long paper format contradiction
The repeated hedging language—"preliminary findings," "preliminary study," "preliminary evidence"—creates a credibility problem. R2's critique is valid: if the authors don't trust their own results, neither will reviewers. That said, the caution seems justified given the data scale, so there's a real tension between intellectual honesty and making a compelling case.

**W1** - Related Work contains self-results
The related work section is mixing in results from this paper itself—specifically the DisPeD findings about continued pretraining bridging the OOD gap and RoBERTa baseline performance numbers.  It also includes GPT-5.5 results. R2 is right that this violates the purpose of related work, which should position the research rather than preview the findings.

**W2** - Abstract data overload
The abstract is packed with numerical results—at least 8-10 distinct metrics with standard deviations, percentage point improvements, and p-values—crammed into 150 words. This creates cognitive overload and obscures the main contribution.

**W3** - ActorAttack sample size missing
In the experiments section, the text specifies sample sizes for FITD and Deceptive Delight datasets but leaves ActorAttack's count unspecified. The sentence reads "80 FITD, 80 DD, and ActorAttack conversations" without stating how many ActorAttack samples were used.

**W4** - Introduction results paragraph too long
The fourth paragraph of the introduction is drowning in metrics—multiple F1 scores with confidence intervals, percentage point gains, and various thresholds—making it difficult to identify the core message.

**W5** - Missing Responsible NLP Research Checklist
The ACL ARR submission requires this checklist, and I can't find it in either the main document or appendix. This could trigger a desk rejection.

**W6** - Page count
Without compiling the document, I can't verify the exact page count, but given how densely packed the content is, this seems like a legitimate concern.

**W7** - Figure* floating position
Figure 3 uses the full-width figure* environment, which introduces unpredictability in where it actually appears on the page.

The strengths align with what I identified earlier, and I notice the question about TF-IDF on ActorAttack overlaps with something I flagged as well.

Looking at the remaining questions: TF-IDF and mean pooling results aren't reported for ActorAttack. The claim about pragmatic features in Section 4.3 is speculative—the linear probing experiments only partially support it with modest 1-5 percentage point improvements and don't directly validate the hedging or topic-shifting pattern claims. The ActorAttack sample size issue is the same as the earlier concern about missing details. The topic classification point about the five categories is interesting but gets cut off. same topics used to generate benign conversations (method.tex line 50, appendix line 139). So topic classification might be learning "benign vs jailbreak" through topic labels rather than failing at topic classification. This is a valid confound!

Looking at method.tex line 50: "The topic variant trains a 5-class topic classifier (technology, health, finance, education, general) on the same conversations". And appendix line 139: "Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general)."

If benign conversations are topic-anchored and jailbreak conversations are not, then topic labels would correlate with benign/jailbreak status. The model might be learning this shortcut rather than genuinely failing at topic classification. This is a really clever observation by R2. I agree this is a confound.

But reconsidering—the topic classifier trains on all conversations, so if jailbreak ones lack clear topics while benign ones have them, the model learns to associate unclear topics with jailbreaks. That's still a shortcut, but the poor OOD performance (0.541±0.207) suggests it doesn't transfer well. The real question is whether this reflects the paper's "misaligned supervision" claim or just shortcut learning that fails to generalize, which are subtly different interpretations. R2's confound concern is definitely valid though.

Now I'm noticing some missing references that would strengthen the analysis—Circuit Breakers and SmoothLLM are relevant alternative approaches that should be cited.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06f8d873-8cfc-4808-aaa5-c13199f3e001",
  "isSidechain": false,
  "requestId": "req_011CbAK6vLVsca4aYTWdVrUF",
  "type": "assistant",
  "uuid": "f433fc18-a17b-429e-b5b4-38bb874f57f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEBpMWLy4zvJP3MYd7E7ws",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9748,
      "cache_read_input_tokens": 83602,
      "output_tokens": 6382,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6382,
          "cache_read_input_tokens": 83602,
          "cache_creation_input_tokens": 9748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9748
          },
          "type": "message"
        }
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

_source line 77 · 2026-05-18T16:01:11.748Z_

论文已仔细重读。现在逐条回应 R2 的意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f433fc18-a17b-429e-b5b4-38bb874f57f4",
  "isSidechain": false,
  "requestId": "req_011CbAK6vLVsca4aYTWdVrUF",
  "type": "assistant",
  "uuid": "17297c80-520b-4d8a-8163-ee7963b57ef5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEBpMWLy4zvJP3MYd7E7ws",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9748,
      "cache_read_input_tokens": 83602,
      "output_tokens": 6382,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6382,
          "cache_read_input_tokens": 83602,
          "cache_creation_input_tokens": 9748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9748
          },
          "type": "message"
        }
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

_source line 78 · 2026-05-18T16:02:36.101Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01PHARh2atzszfKjuAS5b4EZ`</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 (Round 1) 的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE with nuance] R2-N1: 核心贡献新颖性 — Don't Stop Pretraining 的领域应用**\n\nR2 的批评方向正确，但过于简化。论文的贡献不仅是 \"DAPT applied to jailbreak detection\"，还包括：(1) scrambled labels = binary = 9-class 的 regularizer 发现（Section 4.3, Table 2），(2) cross-encoder \"difficulty threshold\" 概念（Section 4.5, Table 3），(3) topic classification 作为 negative control 的 misaligned supervision 发现（Section 4.3）。这些超越了 Gururangan et al. (2020) 的简单领域验证。\n\n但 R2 的核心观点仍然成立：论文的 **headline result**（~60pp OOD gap bridging by MLM）确实是 DAPT 的直接推论，在 500 条合成对话的小规模上验证。更精细的 decomposition 发现（scrambled labels, difficulty threshold）虽然有趣，但统计支撑不足（3 seeds, n=76-118）。作为 long paper 的核心贡献，novelty 确实偏弱。如果 novelty claim 重新聚焦在 \"difficulty threshold across encoders\" 和 \"regularizer interpretation of classification supervision\" 上（而非 DAPT 验证本身），论文的 positioning 会更强。\n\n**[AGREE] R2-N2: TF-IDF 削弱 discourse-level representation 价值主张**\n\n完全同意。这与我 R1 审稿意见中的 N1（单模型 confound）和 W1（TF-IDF 冲击）高度一致。论文自己在 Section 5 (Limitations, \"Lexical separability\" paragraph) 承认 \"We cannot conclusively distinguish whether DisPeD's continued pretraining captures pragmatic discourse features or primarily exploits lexical cues\"。Section 4.3 (line 103) 声称 MLM \"captures pragmatic features (hedging, escalation markers, topic-shifting patterns)\"，但没有任何 probing 证据支撑这一 claim。唯一的线性探测（Section 4.5, line 185-186）测试的是 turn position / escalation phase / persuasion presence，改进仅 1-5pp，且无法区分 lexical 和 discourse-level 特征。\n\n补充 R2 的论点：TF-IDF 在 Table 1 中的 K=2 列标为 \"--\"，即**未报告 per-prefix 结果**。如果 TF-IDF 在 K=2 也表现良好，则 DisPeD 声称的 \"early detection advantage\" 也可能不成立。此外，TF-IDF 在 ActorAttack 上的结果也未报告（我在 R1-Q1 和 R1-W1 中也提到了这一遗漏）。\n\n**[AGREE with important nuance] R2-N3: \"Preliminary findings\" 与 long paper 格式矛盾**\n\nR2 的策略性建议是对的：在 peer review 中，self-hedging 确实会被 weaponized。论文在 Abstract (line 2: \"preliminary findings\")、Introduction (line 16: \"preliminary study\")、Conclusion (line 6: \"preliminary evidence\") 三处使用 \"preliminary\"。\n\n但我认为需要区分两种情况：\n1. 如果作者 **去掉 \"preliminary\" 但不改变实验规模**，论文反而会更容易被批评为 overclaiming（500 条合成数据、3 seeds、n=76 perturbation test 确实无法支撑 definitive claims）。\n2. 正确的修复是 **同时移除 \"preliminary\" hedging 和扩大实验规模**。仅做文字修改而不加强证据，会使论文更脆弱。\n\n所以 R2 发现了一个真问题，但建议方向需要 clarify：问题不是 \"不该用 preliminary\"，而是 \"如果规模不够支撑 definitive claims，则 long paper 投稿本身需要重新考虑\"。这更接近 R2 原意中 \"更适合 workshop paper\" 的判断。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Related Work 不应包含自身实验结果**\n\n验证了原文。至少三处 Related Work 段落包含本文数值：\n- \"Domain-adaptive pretraining\" 段 (related_work.tex line 19): \"DisPeD's MLM control confirms that continued pretraining bridges ~60pp of the OOD gap\" 以及 RoBERTa F1 数值\n- \"Dataset artifacts\" 段 (line 22): \"TF-IDF achieves F1 = 0.944 on our OOD evaluation\"\n- \"Production safety systems\" 段 (line 13): \"GPT-5.5 achieves F1 = 0.191-0.449\"\n\n这些内容属于 Results/Discussion，不属于 Related Work。Related Work 的功能是 positioning（定位自身工作相对于已有文献），不是 preview results。将这些数值移到 Experiments/Discussion 即可修复。\n\n**[AGREE] R2-W2: Abstract 数据过载**\n\n统计 Abstract 中的独立数值：60pp, 0.31±0.03, 0.91±0.12, 0.981, 0.466, 0.93, 4-20×, p<0.001。共 8-10 个数值点在约 150 词中出现。R2 说 12 个可能计入了 F1 标注等，数量级一致。核心问题是：审稿人 30 秒内无法从 Abstract 提取论文的核心洞察。Abstract 应该讲 story（什么问题、什么洞察、什么机制），数字是支撑而非主体。\n\n**[AGREE] R2-W3: ActorAttack 样本量未说明**\n\nSection 4.1 (experiments.tex line 11) 原文：\"OOD evaluation uses 80 FITD, 80 Deceptive Delight (DD), and ActorAttack conversations\"。FITD 和 DD 标注了 80 条，ActorAttack 数量确实缺失。这是一个基础的 reporting gap，必须修复。（我在 R1-Q4 中也问了同一问题。）\n\n**[AGREE] R2-W4: Introduction 结果段过于冗长**\n\nIntroduction 第 4 段（introduction.tex line 14）约 200 词，包含 15+ 数值（0.31±0.03, 0.91±0.12, 60pp, 0.97, K≤5, 0.997±0.005, 0.981, 0.466±0.163, 0.93, RTD, MLM, 0.005-0.046 等）。读者此时尚未看到 Method 和 Experiment 细节，无法消化这些数字。应压缩为 2-3 个 headline numbers + 核心 takeaway，将细节留给 Experiments。\n\n**[AGREE — elevated to critical] R2-W5: 缺少 Responsible NLP Research Checklist**\n\n确认 main.tex 和 appendix.tex 中均未包含 ACL ARR 要求的 Responsible NLP Research Checklist。这不仅仅是 minor formatting issue。ACL ARR 明确要求此 checklist，缺失可能导致 desk reject。鉴于论文涉及 jailbreak attack 和 adversarial techniques，ethical considerations checklist 尤为重要。我将此问题的 severity 从 R2 的 \"major\" 提升为 **critical**，因为 desk reject 风险直接影响接收可能性。\n\n**[AGREE with caveat] R2-W6: 页数可能超限**\n\n无法在不编译 PDF 的情况下验证。但鉴于内容密度（7 个 variants × 4 attack families × multiple prefix lengths + perturbation analysis + cross-encoder + strategy analysis + CKA + linear probing），在 8 页正文 + unlimited references 的限制下确实紧张。Limitations section 不计页数（ACL 2026 规则），但 Conclusion 必须在第 8 页内结束。建议作者确认编译后页数。\n\n**[AGREE] R2-W7: Figure* 浮动位置异常**\n\nFigure 3 (fig3_strategy_heatmap) 使用 `figure*` 环境（experiments.tex line 247），full-width figure 在两栏排版中容易浮动到非预期位置。这是 LaTeX 常见问题，用 `[t!]` 或 `\\afterpage` 可修复。Minor issue。\n\n---\n\n### Strengths\n\n**[AGREE] R2-S1: 消融实验设计系统严谨**\n与我 R1-S1 一致。7 个变体的设计是论文最有价值的贡献。\n\n**[AGREE] R2-S2: Scrambled labels 发现有洞察力**\n与我 R1-S1 一致。Scrambled = binary = 9-class 的 convergence（Table 2, Section 4.3）是一个 elegant finding。\n\n**[AGREE] R2-S3: Cross-encoder \"difficulty threshold\" 概念**\n与我 R1-S3 一致。DeBERTa vs. RoBERTa 在 DD vs. ActorAttack 上的差异模式（Table 3, Section 4.5）提供了有实践意义的洞察。\n\n**[AGREE] R2-S4: 诚实的 Limitations section**\n与我 R1-S2 一致。Section 5 覆盖了 7 个具体 limitation，坦率程度在同类论文中罕见。\n\n**[AGREE] R2-S5: 可复现性优秀**\nAppendix E 的超参数、训练流程细节比较完整，总计算成本 < 4 GPU-hours（Section 5, \"Computation cost\"）。但我在 R1 review 中指出生成 prompt 和标注 prompt 未在论文中披露（仅承诺 release upon acceptance），这使得 reproducibility 不完全。\n\n---\n\n### Questions\n\n**[AGREE] R2-Q1: TF-IDF 在 ActorAttack 上的 F1？**\n与我 R1-W1 一致。未报告，且这是评估 TF-IDF 对核心 claim 冲击的关键缺失数据。\n\n**[AGREE] R2-Q2: Mean pooling 在 ActorAttack 上是否也匹配 BiGRU？**\n与我 R1-W2 观点一致（mean pooling single-seed 不可靠）。论文在 Section 4.3 (line 135-137) 自己标注了 \"single seed on a single OOD attack type\"。在 ActorAttack 这样更难的 benchmark 上，mean pooling 是否仍匹配 BiGRU 是一个关键的未回答问题。\n\n**[AGREE] R2-Q3: \"pragmatic features\" 缺乏直接证据**\n与我对 R2-N2 的分析一致。Section 4.3 line 103 声称 \"captures pragmatic features (hedging, escalation markers, topic-shifting patterns)\" 但无 probing 证据。Section 4.5 line 185-186 的线性探测改进仅 1-5pp，且测试的维度（turn position, escalation phase, persuasion presence）不直接对应 hedging 或 topic-shifting。\n\n**[AGREE] R2-Q4: ActorAttack 样本量？**\n与 W3 重复。Section 4.1 确实未标注 ActorAttack 数量。\n\n**[AGREE — important confound] R2-Q5: Topic classification 的 5-class 与 benign 生成 topic 一致**\n\n这是一个非常 insightful 的观察，我在 R1 审稿中未发现这个 confound。\n\n验证事实：\n- method.tex line 50: \"The topic variant trains a 5-class topic classifier (technology, health, finance, education, general) on the same conversations\"\n- appendix.tex line 139 (Reproducibility Details): \"Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general)\"\n\n两个 category set 完全一致。这意味着 topic labels 与 benign/jailbreak status 存在 systematic correlation：benign conversations 有清晰的 topic label，而 jailbreak conversations 的 topic 分布不同。Topic classifier 可能学到了 \"某些 topic 分布 = benign\"的 shortcut，而非论文声称的 \"misaligned supervision forces encoder to allocate capacity to irrelevant discriminative features\"（Section 4.3, line 118）。\n\n这个 confound 改变了 topic classification 结果的解释：OOD 性能差（0.541±0.207）可能不是因为 \"misaligned objective destabilizes representations\"，而是因为 OOD 数据的 topic-benign correlation 与训练数据不同。如果真是 shortcut learning，则 \"separates the effect of 'having a training objective' from 'having the right training objective'\" 这个 claim（Section 4.3, line 119）不成立。\n\n**建议修复：用与 jailbreak domains 正交的 topic categories 重新训练 topic variant，或者在 jailbreak 和 benign conversations 上都使用相同 topic 分布。**\n\n---\n\n### Missing References\n\n**[PARTIALLY AGREE]**\n\n按相关性排序：\n- **Persuasion for Good (Wang et al., 2019)**: [AGREE] 直接相关。这是 dialogue 中 persuasion detection 的重要先驱工作，论文的 persuasion taxonomy (Section 3.2) 应该 cite 并 compare。论文 cite 了 propaganda analysis (Da San Martino et al., 2019/2020) 作为类比，但遗漏了 dialogue persuasion 方向，这是更直接的对照。\n- **SmoothLLM (Robey et al., 2024)**: [AGREE] 与 perturbation analysis (Section 4.4) 直接相关。SmoothLLM 本身就是基于 perturbation 的防御方法，论文做了 perturbation robustness 分析却未 cite。\n- **TAP (Mehrotra et al., 2024)**: [AGREE] 作为另一个 iterative/multi-turn attack method，应在 Related Work \"Multi-turn jailbreak attacks\" 段落中提及。论文 cite 了 PAIR 但遗漏了 TAP。\n- **Circuit Breakers (Zou et al., 2024)**: [PARTIALLY AGREE] 相关但不直接。这是 representation engineering 方向的防御，与 DisPeD 的 encoder adaptation 有概念联系，但方法论不同。\n- **GradSafe (Xie et al., 2024)**: [PARTIALLY AGREE] gradient-based safety 方向，与 DisPeD 方法不同，但应在 production safety systems 段落中 acknowledged。\n- **Rainbow Teaming (Samvelyan et al., 2024)**: [MINOR] 多样化 adversarial prompt 生成，相关性较弱。\n",
  "reviewer_id": "1",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17297c80-520b-4d8a-8163-ee7963b57ef5",
  "isSidechain": false,
  "requestId": "req_011CbAK6vLVsca4aYTWdVrUF",
  "type": "assistant",
  "uuid": "4db60e62-9187-49ef-882b-5906fec326b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEBpMWLy4zvJP3MYd7E7ws",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9748,
      "cache_read_input_tokens": 83602,
      "output_tokens": 6382,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6382,
          "cache_read_input_tokens": 83602,
          "cache_creation_input_tokens": 9748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9748
          },
          "type": "message"
        }
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

_source line 79 · 2026-05-18T16:02:39.936Z_

<details><summary>↩ Tool result · `toolu_01PHARh2atzszfKjuAS5b4EZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4db60e62-9187-49ef-882b-5906fec326b4",
  "isSidechain": false,
  "promptId": "59199c46-1676-459e-aee5-9eb237246cce",
  "type": "user",
  "uuid": "922d0d27-be91-4971-a974-b19ca06f8f02",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_613965f45d48763f375aa83e9294b24a:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "4db60e62-9187-49ef-882b-5906fec326b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8",
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
  "lastPrompt": "[Round 1 审稿请求]: 以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W7)、Strength (S1-S5)、Question (Q1-Q5) 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Fi…",
  "leafUuid": "922d0d27-be91-4971-a974-b19ca06f8f02",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---

### Runtime record

_source line 81_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multi-turn jailbreak detection paper methodology",
  "sessionId": "db89f3d0-eddf-4030-bb40-5b19b86066c8"
}
```

---
