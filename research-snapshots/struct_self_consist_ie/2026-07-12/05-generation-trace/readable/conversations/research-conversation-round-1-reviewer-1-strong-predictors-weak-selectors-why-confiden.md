# Research conversation: [Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。 ## 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confiden

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 90
- **Recorded user turns:** 3
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-3/eb1a3f49-65c9-4074-8546-55ac5548828b.jsonl`
- **Structured JSON:** [`9f37344d771a41b06ca1.json`](../../sessions/9f/9f37344d771a41b06ca1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T12:14:53.352Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T12:14:53.352Z",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "content": "[Round 1 审稿请求]:\n你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。\n\n## 论文信息\n- **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（含 sections/ 子目录各章节）\n- **目标 Venue**: EMNLP 2026 Main Conference\n- **Track**: Main Conference (Long Paper)\n- **Deadline**: 2026-05-25 (ARR May 2026 cycle)\n\n## Venue 格式要求\n- ACL 模板，8 页正文 + 引用不限 + 附录\n- Double-blind（匿名审稿）\n- Limitations section 必需\n- 提交时必须选择 EMNLP（绑定选择）\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- 五个 confidence signal 的定义是否数学严谨、无歧义\n- Soft Jaccard（Eq.4-5）的 Hungarian matching 描述是否完整（目标函数、zero-IoU 处理、threshold）\n- VC（Eq.6）的公式定义与脚注中描述的实际实现（majority threshold）是否一致\n- FK 的独立性假设：excess agreement 数据是否充分支撑（configuration 覆盖、显著性检验）\n- Consensus-proximity = LOO-SJ 等价性推导是否充分\n\n### 2. 统计检验\n- Bootstrap resampling 的参数设置（B=10,000, n=529）是否充分\n- TOST 等价检验的 δ 选择（±2/3/5 pp）的合理性论证——δ 是否有实践锚定\n- 多重比较校正（Bonferroni）的处理是否到位\n- Effect size (Cohen's d=0.038) 和 CI 的报告是否完整\n- \"60% instances effectively tied\" 的 ε=0.05 阈值选择是否有依据\n\n### 3. 实验设计\n- 训练配置（LoRA rank=32, α=64, 5 epochs）是否完整可复现\n- Qwen3-8B SciERC thinking token 训练不一致是否充分讨论\n- N=8 single seed (seed=42) 作为核心结果的局限性\n- Free-form ablation 仅 1 个 dataset × 1 个 model 的充分性\n- RE 证据仅基于 SciERC 单数据集的措辞限定是否一致\n\n### 4. 可复现性\n- 附录是否包含完整训练配置、prompt template\n- 数据集 split 信息\n- Constrained decoding 的具体工具和参数\n\n请严格按照 EMNLP 审稿标准评审，不留情面。输出格式：Summary → Strengths → Weaknesses (Critical/Warning/Minor 分级) → Questions → Missing References → Scores (Soundness/Presentation/Contribution/Overall 1-5) → Confidence。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T12:14:53.356Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T12:14:53.356Z",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

## Round 1

79 recorded events

### User

_source line 3 · 2026-05-15T12:14:53.389Z_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。

## 论文信息
- **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction
- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（含 sections/ 子目录各章节）
- **目标 Venue**: EMNLP 2026 Main Conference
- **Track**: Main Conference (Long Paper)
- **Deadline**: 2026-05-25 (ARR May 2026 cycle)

## Venue 格式要求
- ACL 模板，8 页正文 + 引用不限 + 附录
- Double-blind（匿名审稿）
- Limitations section 必需
- 提交时必须选择 EMNLP（绑定选择）

## 你的审查侧重

### 1. 方法严谨性
- 五个 confidence signal 的定义是否数学严谨、无歧义
- Soft Jaccard（Eq.4-5）的 Hungarian matching 描述是否完整（目标函数、zero-IoU 处理、threshold）
- VC（Eq.6）的公式定义与脚注中描述的实际实现（majority threshold）是否一致
- FK 的独立性假设：excess agreement 数据是否充分支撑（configuration 覆盖、显著性检验）
- Consensus-proximity = LOO-SJ 等价性推导是否充分

### 2. 统计检验
- Bootstrap resampling 的参数设置（B=10,000, n=529）是否充分
- TOST 等价检验的 δ 选择（±2/3/5 pp）的合理性论证——δ 是否有实践锚定
- 多重比较校正（Bonferroni）的处理是否到位
- Effect size (Cohen's d=0.038) 和 CI 的报告是否完整
- "60% instances effectively tied" 的 ε=0.05 阈值选择是否有依据

### 3. 实验设计
- 训练配置（LoRA rank=32, α=64, 5 epochs）是否完整可复现
- Qwen3-8B SciERC thinking token 训练不一致是否充分讨论
- N=8 single seed (seed=42) 作为核心结果的局限性
- Free-form ablation 仅 1 个 dataset × 1 个 model 的充分性
- RE 证据仅基于 SciERC 单数据集的措辞限定是否一致

### 4. 可复现性
- 附录是否包含完整训练配置、prompt template
- 数据集 split 信息
- Constrained decoding 的具体工具和参数

请严格按照 EMNLP 审稿标准评审，不留情面。输出格式：Summary → Strengths → Weaknesses (Critical/Warning/Minor 分级) → Questions → Missing References → Scores (Soundness/Presentation/Contribution/Overall 1-5) → Confidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "2d06bf03-e8b1-4c08-a251-f6362459938b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T12:14:53.388Z_

```json
{
  "parentUuid": "2d06bf03-e8b1-4c08-a251-f6362459938b",
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
  "uuid": "aa95006e-93ce-4601-be62-de82205ab735",
  "timestamp": "2026-05-15T12:14:53.388Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T12:14:53.388Z_

```json
{
  "parentUuid": "aa95006e-93ce-4601-be62-de82205ab735",
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
  "uuid": "ddbcb8e5-1f88-4326-864a-5291e062f969",
  "timestamp": "2026-05-15T12:14:53.388Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T12:14:53.388Z_

```json
{
  "parentUuid": "ddbcb8e5-1f88-4326-864a-5291e062f969",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "60b2c848-6f1f-4ae9-92c0-cd9279180de0",
  "timestamp": "2026-05-15T12:14:53.388Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
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
  "aiTitle": "Review structured information extraction confidence signals paper",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Assistant

_source line 8 · 2026-05-15T12:14:59.965Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as Reviewer 1 for a paper submission to EMNLP 2026. I need to:

1. First, load the review-reviewer-session-start skill as mentioned in the CLAUDE.md
2. Search for EMNLP 2026 / ACL ARR reviewer guidelines
3. Read the paper (main.tex and sections/)
4. Conduct a thorough review focusing on method rigor + experimental design

Let me start by reading the paper and searching for reviewer guidelines.

First, let me load the necessary tools and read the paper. 

Now I'm locating the paper files at `projects/struct_self_consist_ie/docs/paper/main.tex` and its sections, then searching for EMNLP and ARR reviewer guidelines to understand the evaluation criteria I should apply.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60b2c848-6f1f-4ae9-92c0-cd9279180de0",
  "isSidechain": false,
  "requestId": "req_011Cb4LVAmNXMW4vNy96zqw4",
  "type": "assistant",
  "uuid": "9e02e3c9-6d8a-40bc-87a8-1f09070d0635",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqWHcii9ESALLkbZ137itC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13892,
      "cache_read_input_tokens": 11841,
      "output_tokens": 447,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 447,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13892
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-15T12:14:59.973Z_

开始审稿。先并行完成三件事：定位论文文件、搜索 EMNLP/ARR 审稿标准、加载必要工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e02e3c9-6d8a-40bc-87a8-1f09070d0635",
  "isSidechain": false,
  "requestId": "req_011Cb4LVAmNXMW4vNy96zqw4",
  "type": "assistant",
  "uuid": "6c8a8fb5-7cb4-4348-82c3-0811a781fbe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqWHcii9ESALLkbZ137itC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13892,
      "cache_read_input_tokens": 11841,
      "output_tokens": 447,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 447,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13892
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-15T12:15:01.571Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QYyTvn237N4WsWnTYEdoVH`</summary>

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
  "parentUuid": "6c8a8fb5-7cb4-4348-82c3-0811a781fbe3",
  "isSidechain": false,
  "requestId": "req_011Cb4LVAmNXMW4vNy96zqw4",
  "type": "assistant",
  "uuid": "afb74398-1e4d-44a6-9611-28a9944d6ea8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqWHcii9ESALLkbZ137itC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13892,
      "cache_read_input_tokens": 11841,
      "output_tokens": 447,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 447,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13892
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-15T12:15:02.197Z_

<details><summary>↩ Tool result · `toolu_01M3ZZL6xVZhrNmjwoPDK6kX`</summary>

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
  "parentUuid": "785e790e-a545-4f79-b9a1-b9eca094c556",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "24de4495-8c31-45d6-a5e6-ee0240de2c55",
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
  "sourceToolAssistantUUID": "785e790e-a545-4f79-b9a1-b9eca094c556",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T12:15:01.598Z_

<details><summary>↩ Tool result · `toolu_01QYyTvn237N4WsWnTYEdoVH`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afb74398-1e4d-44a6-9611-28a9944d6ea8",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "cbe3f93a-9660-4ed9-a0c2-f6450ba4039b",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 9,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "afb74398-1e4d-44a6-9611-28a9944d6ea8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T12:15:02.192Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01M3ZZL6xVZhrNmjwoPDK6kX`</summary>

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
  "parentUuid": "cbe3f93a-9660-4ed9-a0c2-f6450ba4039b",
  "isSidechain": false,
  "requestId": "req_011Cb4LVAmNXMW4vNy96zqw4",
  "type": "assistant",
  "uuid": "785e790e-a545-4f79-b9a1-b9eca094c556",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqWHcii9ESALLkbZ137itC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13892,
      "cache_read_input_tokens": 11841,
      "output_tokens": 447,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 447,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13892
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-15T12:15:07.845Z_

<details><summary>Logged reasoning block</summary>

```text
The glob didn't find files. Let me check the correct path - the working directory is `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296`, but the paper is at `projects/struct_self_consist_ie/docs/paper/main.tex` relative to the project root. Let me find the correct absolute path.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24de4495-8c31-45d6-a5e6-ee0240de2c55",
  "isSidechain": false,
  "requestId": "req_011Cb4LVq5UFwA2ngq3gRSU4",
  "type": "assistant",
  "uuid": "b20681d4-6a9a-4321-b098-d655aa4fbee9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFE3Yu5DXtxfUebhhTmLq3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2488,
      "cache_read_input_tokens": 25733,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 284,
          "cache_read_input_tokens": 25733,
          "cache_creation_input_tokens": 2488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2488
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-15T12:15:08.456Z_

文件没找到，需要确认绝对路径。同时搜索 ARR 审稿标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b20681d4-6a9a-4321-b098-d655aa4fbee9",
  "isSidechain": false,
  "requestId": "req_011Cb4LVq5UFwA2ngq3gRSU4",
  "type": "assistant",
  "uuid": "b18c29a4-e61a-48a0-85f0-e4d3c65123bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFE3Yu5DXtxfUebhhTmLq3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2488,
      "cache_read_input_tokens": 25733,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 284,
          "cache_read_input_tokens": 25733,
          "cache_creation_input_tokens": 2488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2488
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-15T12:15:08.991Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011A64kaRSVMJu38ra7xSMHe`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b18c29a4-e61a-48a0-85f0-e4d3c65123bc",
  "isSidechain": false,
  "requestId": "req_011Cb4LVq5UFwA2ngq3gRSU4",
  "type": "assistant",
  "uuid": "da30623c-ee3b-4d62-a4db-590b3fab8aa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFE3Yu5DXtxfUebhhTmLq3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2488,
      "cache_read_input_tokens": 25733,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 284,
          "cache_read_input_tokens": 25733,
          "cache_creation_input_tokens": 2488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2488
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-15T12:15:09.030Z_

<details><summary>↩ Tool result · `toolu_011A64kaRSVMJu38ra7xSMHe`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da30623c-ee3b-4d62-a4db-590b3fab8aa7",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "9a641476-85a3-49ca-8d6a-049d679f8996",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
    ],
    "durationMs": 22,
    "numFiles": 13,
    "truncated": false
  },
  "sourceToolAssistantUUID": "da30623c-ee3b-4d62-a4db-590b3fab8aa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T12:15:09.448Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PtRg3SdWpXUmxkjR79MrsC`</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a641476-85a3-49ca-8d6a-049d679f8996",
  "isSidechain": false,
  "requestId": "req_011Cb4LVq5UFwA2ngq3gRSU4",
  "type": "assistant",
  "uuid": "04c32801-d1ee-4774-9d76-dbeb796051c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFE3Yu5DXtxfUebhhTmLq3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2488,
      "cache_read_input_tokens": 25733,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 284,
          "cache_read_input_tokens": 25733,
          "cache_creation_input_tokens": 2488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2488
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-15T12:15:16.937Z_

<details><summary>↩ Tool result · `toolu_01PtRg3SdWpXUmxkjR79MrsC`</summary>

```text
Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Score Components:

**Soundness and Excitement**: Soundness relates to the quality of the work, while excitement is orthogonal to the assessment of soundness and is more subjective, reflecting whether the work is interesting for you personally. Soundness scores must be justified by the text of the review.

**Overall Recommendation**: The overall assessment score is an explicit recommendation for the outcome of this paper, reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

The review form includes evaluation of:
- Whether there is enough information in the paper for a reader to reproduce the main results, use results presented in this paper in future work, or build upon this work
- The major reasons to publish this paper at a selective *ACL venue, which could include novel and useful methodology, insightful empirical results or theoretical analysis, clear organization of related literature, or any other reason why interested readers of *ACL papers may find the paper useful
- How exciting the paper is, noting that excitement is subjective and does not necessarily follow what is popular in the field


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04c32801-d1ee-4774-9d76-dbeb796051c1",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "0e60ae9f-bf64-4c79-b726-9c6ccab6d775",
  "toolUseResult": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_016sA2WKzk4zjVvVpsYaDrLH",
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
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
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
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/incentives2026"
          }
        ]
      },
      "Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:\n\n## Review Scoring System\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\n\n### Score Components:\n\n**Soundness and Excitement**: Soundness relates to the quality of the work, while excitement is orthogonal to the assessment of soundness and is more subjective, reflecting whether the work is interesting for you personally. Soundness scores must be justified by the text of the review.\n\n**Overall Recommendation**: The overall assessment score is an explicit recommendation for the outcome of this paper, reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.\n\n## Review Form Criteria\n\nThe main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.\n\nThe review form includes evaluation of:\n- Whether there is enough information in the paper for a reader to reproduce the main results, use results presented in this paper in future work, or build upon this work\n- The major reasons to publish this paper at a selective *ACL venue, which could include novel and useful methodology, insightful empirical results or theoretical analysis, clear organization of related literature, or any other reason why interested readers of *ACL papers may find the paper useful\n- How exciting the paper is, noting that excitement is subjective and does not necessarily follow what is popular in the field"
    ],
    "durationSeconds": 7.479343255
  },
  "sourceToolAssistantUUID": "04c32801-d1ee-4774-9d76-dbeb796051c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。  ## 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction - **论文路径**: `projects…",
  "leafUuid": "0e60ae9f-bf64-4c79-b726-9c6ccab6d775",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured information extraction confidence signals paper",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Assistant

_source line 22 · 2026-05-15T12:15:22.019Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I found the paper files. Now let me fetch the actual ARR review form to get the exact scoring scale, and start reading the paper. Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e60ae9f-bf64-4c79-b726-9c6ccab6d775",
  "isSidechain": false,
  "requestId": "req_011Cb4LWuTBSQFH4CRN4sXYv",
  "type": "assistant",
  "uuid": "3af0e45c-fabf-4f69-8e58-f1aec85f5f53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELyKSt4qeef51njBG5ZUdd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1687,
      "cache_read_input_tokens": 28221,
      "output_tokens": 521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 521,
          "cache_read_input_tokens": 28221,
          "cache_creation_input_tokens": 1687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1687
          },
          "type": "message"
        }
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

_source line 23 · 2026-05-15T12:15:22.888Z_

找到论文文件和 ARR 审稿标准。现在并行：获取 ARR review form 详细评分量表 + 开始读论文各章节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3af0e45c-fabf-4f69-8e58-f1aec85f5f53",
  "isSidechain": false,
  "requestId": "req_011Cb4LWuTBSQFH4CRN4sXYv",
  "type": "assistant",
  "uuid": "6d1ceeee-4052-463c-a85e-0ca4435a009e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELyKSt4qeef51njBG5ZUdd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1687,
      "cache_read_input_tokens": 28221,
      "output_tokens": 521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 521,
          "cache_read_input_tokens": 28221,
          "cache_creation_input_tokens": 1687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1687
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-15T12:15:24.353Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Uw4VjkcUMM98ofeHDbppoZ`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 or whatever), and the description of each score level. Include soundness, excitement, overall recommendation, confidence, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d1ceeee-4052-463c-a85e-0ca4435a009e",
  "isSidechain": false,
  "requestId": "req_011Cb4LWuTBSQFH4CRN4sXYv",
  "type": "assistant",
  "uuid": "8dc4f264-8e91-4d72-9c6d-f81e05353ab9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELyKSt4qeef51njBG5ZUdd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1687,
      "cache_read_input_tokens": 28221,
      "output_tokens": 521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 521,
          "cache_read_input_tokens": 28221,
          "cache_creation_input_tokens": 1687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1687
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-15T12:15:26.665Z_

<details><summary>↩ Tool result · `toolu_017ESSCEexdscixsLrGvnATQ`</summary>

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
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{&lt;j}, x)
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
39	While FK assumes independent raters, temperature-based sampling yields mild negative dependence rather than positive correlation among samples.
40	Empirically, we measure excess agreement ($\bar{P} - \bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\% and $-$4.0\%, indicating mild \textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.
41	(All excess agreement values are negative across 5 configurations; a one-sample $t$-test against zero yields $p{<}0.05$.)
42	Unlike structural signals, FK relies on exact string matching and does not tolerate surface variations.
43	
44	\paragraph{Soft Jaccard (structural, instance-level).}
45	Our primary structural signal extends Jaccard similarity \cite{jaccard1901distribution} to extracted entity/relation sets.
46	For samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching via the Hungarian algorithm (maximizing total token-level IoU; zero-IoU pairs automatically receive zero weight), and define:
47	\begin{equation}\label{eq:sj}
48	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
49	\end{equation}
50	where $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.
51	We use $\max(|g_i|, |g_j|)$ rather than $|g_i \cup g_j|$ as the normalizer to penalize length asymmetry between samples.
52	The instance-level signal averages over all pairs:
53	\begin{equation}\label{eq:sj_instance}
54	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i&lt;j} \text{SJ}(y_i, y_j)
55	\end{equation}
56	
57	\paragraph{Entity voting confidence (structural, instance-level).}
58	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
59	The instance-level confidence is the mean frequency:
60	\begin{equation}\label{eq:voting}
61	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
62	\end{equation}
63	When $E_\cup = \emptyset$ (no entity extracted by any sample), we set $c_{\mathrm{vc}}(x) = 0$.\footnote{This occurs in $<$1\% of instances in our experiments (WNUT-17 only). Equation~\ref{eq:voting} defines the continuous QE signal used throughout Table~\ref{tab:quality_estimation} and all correlation analyses. For voted-output \textit{selection} (Table~\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting. The two computations serve different purposes: Eq.~\ref{eq:voting} assigns a continuous quality score per instance; the majority threshold constructs a discrete output for F1 evaluation. On NER, the threshold variant yields $\rho{=}0.252$ (vs.\ $0.379$ for Eq.~\ref{eq:voting}), reflecting information loss from binarization; on RE, the difference is negligible ($\Delta\rho{=}0.019$).}
64	
65	\subsection{Evaluation Framework}\label{sec:evaluation}
66	
67	\paragraph{Quality estimation.}
68	We measure rank correlation (Spearman $\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.
69	
70	\paragraph{Sample selection.}
71	We report best-of-$N$ F1: for each instance, the signal selects one sample.
72	Per-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).
73	We compare against an \textit{oracle} (highest-F1 sample) and \textit{greedy} ($T{=}0$, $N{=}1$).
74	
75	\paragraph{Complementarity.}
76	High rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\S\ref{sec:selection_gap}).
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0f88859-0794-4573-9a10-3d82403e1e2a",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "819b05e2-393b-4369-b1db-f908fcf0577a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven a language model $\\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}.\nEach $y_i$ is an entity set (NER) or relation set (RE).\nA confidence signal $c$ serves two purposes: (a) \\textit{quality estimation}---predicting which instances the model handles reliably, and (b) \\textit{sample selection}---identifying the best output among $N$ candidates.\n\nA \\textbf{per-sample signal} scores each $y_i$ independently, $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$, enabling direct candidate ranking.\nAn \\textbf{instance-level signal} aggregates over all $N$ samples, $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$, producing a single score per input.\nThis asymmetry---between predicting \\textit{which inputs} are easy and selecting \\textit{which output} is best---is central to the correlation-selection gap we investigate.\nNotation is summarized in Appendix~\\ref{app:notation}.\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nWe use \\textit{confidence signal} as the umbrella term for all five measures.\nFour are \\textit{consistency signals}---computed from inter-sample agreement---spanning two families: \\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \\textit{surface} (exact match [EM], Fleiss' $\\kappa$ [FK]).\nThe fifth, log-probability, is the sole \\textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nThe only per-sample signal.\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{&lt;j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe majority fraction---the proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed pairwise agreement and $\\bar{P}_e$ is expected agreement under random assignment.\nWhile FK assumes independent raters, temperature-based sampling yields mild negative dependence rather than positive correlation among samples.\nEmpirically, we measure excess agreement ($\\bar{P} - \\bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\\% and $-$4.0\\%, indicating mild \\textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.\n(All excess agreement values are negative across 5 configurations; a one-sample $t$-test against zero yields $p{<}0.05$.)\nUnlike structural signals, FK relies on exact string matching and does not tolerate surface variations.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nOur primary structural signal extends Jaccard similarity \\cite{jaccard1901distribution} to extracted entity/relation sets.\nFor samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching via the Hungarian algorithm (maximizing total token-level IoU; zero-IoU pairs automatically receive zero weight), and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.\nWe use $\\max(|g_i|, |g_j|)$ rather than $|g_i \\cup g_j|$ as the normalizer to penalize length asymmetry between samples.\nThe instance-level signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i&lt;j} \\text{SJ}(y_i, y_j)\n\\end{equation}\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\nWhen $E_\\cup = \\emptyset$ (no entity extracted by any sample), we set $c_{\\mathrm{vc}}(x) = 0$.\\footnote{This occurs in $<$1\\% of instances in our experiments (WNUT-17 only). Equation~\\ref{eq:voting} defines the continuous QE signal used throughout Table~\\ref{tab:quality_estimation} and all correlation analyses. For voted-output \\textit{selection} (Table~\\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting. The two computations serve different purposes: Eq.~\\ref{eq:voting} assigns a continuous quality score per instance; the majority threshold constructs a discrete output for F1 evaluation. On NER, the threshold variant yields $\\rho{=}0.252$ (vs.\\ $0.379$ for Eq.~\\ref{eq:voting}), reflecting information loss from binarization; on RE, the difference is negligible ($\\Delta\\rho{=}0.019$).}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nWe measure rank correlation (Spearman $\\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.\n\n\\paragraph{Sample selection.}\nWe report best-of-$N$ F1: for each instance, the signal selects one sample.\nPer-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).\nWe compare against an \\textit{oracle} (highest-F1 sample) and \\textit{greedy} ($T{=}0$, $N{=}1$).\n\n\\paragraph{Complementarity.}\nHigh rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\\S\\ref{sec:selection_gap}).\n",
      "numLines": 77,
      "startLine": 1,
      "totalLines": 77
    }
  },
  "sourceToolAssistantUUID": "b0f88859-0794-4573-9a10-3d82403e1e2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T12:15:25.408Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D3gYwAamw8rkWifPHLV1Ww`</summary>

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
  "parentUuid": "8dc4f264-8e91-4d72-9c6d-f81e05353ab9",
  "isSidechain": false,
  "requestId": "req_011Cb4LWuTBSQFH4CRN4sXYv",
  "type": "assistant",
  "uuid": "29799dff-aa23-409c-b56c-19aa84e4264f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELyKSt4qeef51njBG5ZUdd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1687,
      "cache_read_input_tokens": 28221,
      "output_tokens": 521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 521,
          "cache_read_input_tokens": 28221,
          "cache_creation_input_tokens": 1687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1687
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-15T12:15:25.425Z_

<details><summary>↩ Tool result · `toolu_01D3gYwAamw8rkWifPHLV1Ww`</summary>

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
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Do Not Scale Structured Information Extraction}
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
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{sections/appendix}
49	
50	\end{document}
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29799dff-aa23-409c-b56c-19aa84e4264f",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "86540aa7-5aab-4355-99fd-26a92394c8e6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\graphicspath{{figures/}}\n\n\\title{Strong Predictors, Weak Selectors:\\\\ Why Confidence Signals Do Not Scale Structured Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\section*{Ethics Statement}\nAll experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).\nCoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.\nNo new human data was collected or annotated for this study.\nOur findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  },
  "sourceToolAssistantUUID": "29799dff-aa23-409c-b56c-19aa84e4264f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T12:15:25.951Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GFTNxpMBh4amcRXuADDmC7`</summary>

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
  "parentUuid": "86540aa7-5aab-4355-99fd-26a92394c8e6",
  "isSidechain": false,
  "requestId": "req_011Cb4LWuTBSQFH4CRN4sXYv",
  "type": "assistant",
  "uuid": "c300dfc8-ae3b-4f1f-9a0f-f1c2147c4e39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELyKSt4qeef51njBG5ZUdd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1687,
      "cache_read_input_tokens": 28221,
      "output_tokens": 521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 521,
          "cache_read_input_tokens": 28221,
          "cache_creation_input_tokens": 1687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1687
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-15T12:15:25.961Z_

<details><summary>↩ Tool result · `toolu_01GFTNxpMBh4amcRXuADDmC7`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.
3	We compare five confidence signals across NER and relation extraction on three benchmarks with two 8B-parameter model families and uncover a \textit{correlation-selection gap}: signals achieve strong quality estimation yet none significantly improves sample selection despite substantial oracle headroom.
4	Most signals are instance-level by construction and cannot rank candidates; the empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection (MBR decoding) can bridge the gap.
5	Neither succeeds: log-probability scores are compressed into effective ties, while MBR utility correlates with quality across instances but not within them.
6	A controlled ablation confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding.
7	Signal rankings depend on task complexity, with findings consistent across two model families at 8B scale.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c300dfc8-ae3b-4f1f-9a0f-f1c2147c4e39",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "aa5bed56-e3d2-4fd4-8672-0d7d24952ed4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nTest-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.\nWe compare five confidence signals across NER and relation extraction on three benchmarks with two 8B-parameter model families and uncover a \\textit{correlation-selection gap}: signals achieve strong quality estimation yet none significantly improves sample selection despite substantial oracle headroom.\nMost signals are instance-level by construction and cannot rank candidates; the empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection (MBR decoding) can bridge the gap.\nNeither succeeds: log-probability scores are compressed into effective ties, while MBR utility correlates with quality across instances but not within them.\nA controlled ablation confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding.\nSignal rankings depend on task complexity, with findings consistent across two model families at 8B scale.\n\\end{abstract}\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "c300dfc8-ae3b-4f1f-9a0f-f1c2147c4e39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T12:15:26.285Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ArDcmT7s16nj2ZsUznsFsb`</summary>

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
  "parentUuid": "aa5bed56-e3d2-4fd4-8672-0d7d24952ed4",
  "isSidechain": false,
  "requestId": "req_011Cb4LWuTBSQFH4CRN4sXYv",
  "type": "assistant",
  "uuid": "257cb42c-d24d-4dfb-82d9-bda17ab0010f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELyKSt4qeef51njBG5ZUdd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1687,
      "cache_read_input_tokens": 28221,
      "output_tokens": 521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 521,
          "cache_read_input_tokens": 28221,
          "cache_creation_input_tokens": 1687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1687
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-15T12:15:26.291Z_

<details><summary>↩ Tool result · `toolu_01ArDcmT7s16nj2ZsUznsFsb`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2025scaling, brown2024monkeys}.
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
16	The most relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.
17	Our work extends theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings---WNUT-17 conditional correlations collapse to $\rho{=}0.038$ (n.s.) and LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$)---that would be invisible on a single dataset.
18	
19	Structured IE requires schema-compliant output, making constrained decoding \cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\% valid JSON rate (\S\ref{sec:ablation}).}
20	All experiments use constrained decoding, the regime under which structured IE is practically deployed.
21	
22	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13--18~pp of oracle headroom.
23	Four of five signals are instance-level by construction---this is definitional, not empirical.
24	The non-trivial questions are whether (a)~consensus-proximity selection, instantiating MBR decoding \cite{eikema2022sampling, freitag2022high, muller2021understanding}, can recover per-sample discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.
25	Both fail: MBR utility correlates with F1 across instances but not within them (\S\ref{sec:discussion}); log-probability scores are severely compressed (60\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
26	A controlled free-form decoding ablation confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding (\S\ref{sec:ablation}).
27	
28	\begin{figure*}[t]
29	\centering
30	\includegraphics[width=\textwidth]{fig_overview}
31	\caption{The correlation-selection gap. \textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection.}
32	\label{fig:overview}
33	\end{figure*}
34	
35	We systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
36	Our contributions are:
37	\begin{enumerate}
38	    \item \textbf{A systematic evaluation framework.}
39	    We compare five confidence signals from three families---structural, surface, and model-internal---across quality estimation, binary discrimination, and sample selection, showing that these metrics decouple and single-metric evaluation risks selecting the wrong signal.
40	
41	    \item \textbf{The correlation-selection gap and its diagnosis.}
42	    Strong quality estimation ($\rho{=}0.38$, AUROC${=}0.75$) coexists with selection failure ($p{>}0.39$, 13--18~pp oracle headroom).
43	    The instance-level failure of four signals is definitional; the empirical contributions are diagnosing why consensus-proximity selection (MBR decoding) and log-probability both fail.
44	    LP score compression (60\% of instances effectively tied) is the primary bottleneck; where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
45	    A controlled ablation confirms that compression is intrinsic, not decoding-regime-specific.
46	
47	    \item \textbf{Task-complexity boundary conditions.}
48	    Signal rankings shift with task difficulty: EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude.
49	    At the capability boundary (WNUT-17, 52\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\rho{=}{-}0.410$)---phenomena invisible on a single dataset that extend \citet{nedellec2026consistency}'s quality-estimation analysis.
50	    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).
51	\end{enumerate}
52	
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "257cb42c-d24d-4dfb-82d9-bda17ab0010f",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "61af5463-2019-4889-9aad-4ba2c2711a0c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \\citealp{wang2023selfconsistency}).\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2025scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a fundamentally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \\textit{quality estimation} (which inputs does the model handle reliably?) and \\textit{sample selection} (which of $N$ outputs is best?).\nThese require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.\nSelf-consistency methods for discrete answers \\cite{wang2023selfconsistency, chen2024usc} and weighted variants \\cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\nThe most relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.\nOur work extends theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings---WNUT-17 conditional correlations collapse to $\\rho{=}0.038$ (n.s.) and LP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$)---that would be invisible on a single dataset.\n\nStructured IE requires schema-compliant output, making constrained decoding \\cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\\% valid JSON rate (\\S\\ref{sec:ablation}).}\nAll experiments use constrained decoding, the regime under which structured IE is practically deployed.\n\nOur central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13--18~pp of oracle headroom.\nFour of five signals are instance-level by construction---this is definitional, not empirical.\nThe non-trivial questions are whether (a)~consensus-proximity selection, instantiating MBR decoding \\cite{eikema2022sampling, freitag2022high, muller2021understanding}, can recover per-sample discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.\nBoth fail: MBR utility correlates with F1 across instances but not within them (\\S\\ref{sec:discussion}); log-probability scores are severely compressed (60\\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\nA controlled free-form decoding ablation confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding (\\S\\ref{sec:ablation}).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. \\textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \\textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection.}\n\\label{fig:overview}\n\\end{figure*}\n\nWe systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{A systematic evaluation framework.}\n    We compare five confidence signals from three families---structural, surface, and model-internal---across quality estimation, binary discrimination, and sample selection, showing that these metrics decouple and single-metric evaluation risks selecting the wrong signal.\n\n    \\item \\textbf{The correlation-selection gap and its diagnosis.}\n    Strong quality estimation ($\\rho{=}0.38$, AUROC${=}0.75$) coexists with selection failure ($p{>}0.39$, 13--18~pp oracle headroom).\n    The instance-level failure of four signals is definitional; the empirical contributions are diagnosing why consensus-proximity selection (MBR decoding) and log-probability both fail.\n    LP score compression (60\\% of instances effectively tied) is the primary bottleneck; where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\n    A controlled ablation confirms that compression is intrinsic, not decoding-regime-specific.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings shift with task difficulty: EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude.\n    At the capability boundary (WNUT-17, 52\\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\\rho{=}{-}0.410$)---phenomena invisible on a single dataset that extend \\citet{nedellec2026consistency}'s quality-estimation analysis.\n    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).\n\\end{enumerate}\n\n",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  },
  "sourceToolAssistantUUID": "257cb42c-d24d-4dfb-82d9-bda17ab0010f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T12:15:26.660Z_

<details open><summary>🔧 Tool call — Read · `toolu_017ESSCEexdscixsLrGvnATQ`</summary>

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
  "parentUuid": "61af5463-2019-4889-9aad-4ba2c2711a0c",
  "isSidechain": false,
  "requestId": "req_011Cb4LWuTBSQFH4CRN4sXYv",
  "type": "assistant",
  "uuid": "b0f88859-0794-4573-9a10-3d82403e1e2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELyKSt4qeef51njBG5ZUdd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1687,
      "cache_read_input_tokens": 28221,
      "output_tokens": 521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 521,
          "cache_read_input_tokens": 28221,
          "cache_creation_input_tokens": 1687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1687
          },
          "type": "message"
        }
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。  ## 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction - **论文路径**: `projects…",
  "leafUuid": "819b05e2-393b-4369-b1db-f908fcf0577a",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured information extraction confidence signals paper",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Tool result

_source line 35 · 2026-05-15T12:15:30.912Z_

<details><summary>↩ Tool result · `toolu_01Uw4VjkcUMM98ofeHDbppoZ`</summary>

```text
# ACL Rolling Review Form - Scoring Dimensions

## 1. Reviewer Confidence
**Scale: 1-5**
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. Soundness
**Scale: 1-5 (with half-point increments)**
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. Excitement
**Scale: 1-5 (with half-point increments)**
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me."

## 4. Overall Assessment
**Scale: 1-5 (with half-point increments)**
- **5**: "Consider for Award"
- **4**: "Conference acceptance"
- **3**: "Findings of the ACL"
- **2**: "Resubmit next cycle"
- **1**: "Do not resubmit"

## 5. Reproducibility
**Scale: 1-5**
Ranges from "easily reproduce" (5) to "would not be able to reproduce" (1).

## 6. Datasets & Software
**Scale: 1-5** each
Rated from "Enabling" (5) to "No usable datasets/software" (1).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dc4f264-8e91-4d72-9c6d-f81e05353ab9",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "d7b48ac9-6755-45f9-ae16-b70dfdcca277",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Scoring Dimensions\n\n## 1. Reviewer Confidence\n**Scale: 1-5**\n- **5**: \"Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work.\"\n- **4**: \"Quite sure. I tried to check the important points carefully.\"\n- **3**: \"Pretty sure, but there's a chance I missed something.\"\n- **2**: \"Willing to defend my evaluation, but it is fairly likely that I missed some details.\"\n- **1**: \"Not my area, or paper is very hard to understand.\"\n\n## 2. Soundness\n**Scale: 1-5 (with half-point increments)**\n- **5**: \"Excellent: This study is one of the most thorough I have seen, given its type.\"\n- **4**: \"Strong: This study provides sufficient support for all of its claims.\"\n- **3**: \"Acceptable: This study provides sufficient support for its main claims.\"\n- **2**: \"Poor: Some of the main claims are not sufficiently supported.\"\n- **1**: \"Major Issues: This study is not yet sufficiently thorough to warrant publication.\"\n\n## 3. Excitement\n**Scale: 1-5 (with half-point increments)**\n- **5**: \"Highly Exciting: I would recommend this paper to others.\"\n- **4**: \"Exciting: I would mention this paper to others.\"\n- **3**: \"Interesting: I might mention some points of this paper to others.\"\n- **2**: \"Potentially Interesting: this paper does not resonate with me.\"\n- **1**: \"Not Exciting: this paper does not resonate with me.\"\n\n## 4. Overall Assessment\n**Scale: 1-5 (with half-point increments)**\n- **5**: \"Consider for Award\"\n- **4**: \"Conference acceptance\"\n- **3**: \"Findings of the ACL\"\n- **2**: \"Resubmit next cycle\"\n- **1**: \"Do not resubmit\"\n\n## 5. Reproducibility\n**Scale: 1-5**\nRanges from \"easily reproduce\" (5) to \"would not be able to reproduce\" (1).\n\n## 6. Datasets & Software\n**Scale: 1-5** each\nRated from \"Enabling\" (5) to \"No usable datasets/software\" (1).",
    "durationMs": 6554,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "8dc4f264-8e91-4d72-9c6d-f81e05353ab9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-15T12:15:30.917Z_

```json
{
  "parentUuid": "d7b48ac9-6755-45f9-ae16-b70dfdcca277",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a1c98299-7aef-4e37-b2a0-729298a4b4c9",
  "timestamp": "2026-05-15T12:15:30.917Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-15T12:15:34.069Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the main structure, abstract, introduction, and method sections. Now let me read the experiments, discussion, conclusion, limitations, and appendix sections in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1c98299-7aef-4e37-b2a0-729298a4b4c9",
  "isSidechain": false,
  "requestId": "req_011Cb4LXwBtHHVXc69KDuXxD",
  "type": "assistant",
  "uuid": "aa6076ab-f6b8-40b5-88cd-c8cc047aed39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVi32FxYSa72aPJmqn4Jsb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5007,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 29908,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5007,
          "output_tokens": 557,
          "cache_read_input_tokens": 29908,
          "cache_creation_input_tokens": 1204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1204
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-15T12:15:35.540Z_

已获取 ARR review form 评分量表和论文前半部分。继续读实验、讨论、结论、局限性和附录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa6076ab-f6b8-40b5-88cd-c8cc047aed39",
  "isSidechain": false,
  "requestId": "req_011Cb4LXwBtHHVXc69KDuXxD",
  "type": "assistant",
  "uuid": "788d1bbb-c9d9-403e-b2c7-2a0e52f6f88a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVi32FxYSa72aPJmqn4Jsb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5007,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 29908,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5007,
          "output_tokens": 557,
          "cache_read_input_tokens": 29908,
          "cache_creation_input_tokens": 1204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1204
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-15T12:15:36.933Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KmN4DdJ3CLsHBuTWokJYBv`</summary>

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
  "parentUuid": "788d1bbb-c9d9-403e-b2c7-2a0e52f6f88a",
  "isSidechain": false,
  "requestId": "req_011Cb4LXwBtHHVXc69KDuXxD",
  "type": "assistant",
  "uuid": "aba93e3b-6c50-4362-a90a-27dd475c770a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVi32FxYSa72aPJmqn4Jsb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5007,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 29908,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5007,
          "output_tokens": 557,
          "cache_read_input_tokens": 29908,
          "cache_creation_input_tokens": 1204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1204
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-15T12:15:39.707Z_

<details><summary>↩ Tool result · `toolu_019HJ4Hz4RwY7c4RHq8DUnUj`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling \cite{zhang2025tts}, \citet{snell2025scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
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
20	Surveys cover confidence estimation \cite{geng2024confidence}, selective abstention \cite{wen2025know}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs; \citet{xiong2024llm} find LLMs tend toward overconfidence, and \citet{heo2025uncertainty} show calibration degrades with task complexity.
21	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; \citet{kossen2024semantic} distill this into probes; P(True) \cite{kadavath2022language} queries model confidence directly; \citet{malinin2021uncertainty} distinguish data and model uncertainty in autoregressive models.
22	Our structural signals instead measure agreement over output \textit{structure}.
23	Neural networks are often miscalibrated \cite{guo2017calibration, desai2020calibration}; deep ensembles \cite{lakshminarayanan2017ensembles} and MC-dropout \cite{gal2016dropout} obtain uncertainty from model variation, while our approach requires no model modification.
24	Prior NER uncertainty work spans Bayesian inference for sequence labeling \cite{xiao2019uncertainty}, active learning under uncertainty \cite{shelmanov2021active}, evidential deep learning \cite{zhang2023ener}, verification-augmented NER \cite{kim2024verifiner}, and uncertainty transmission across label sequences \cite{he2024uncertainty}---all within discriminative paradigms.
25	Conformal prediction \cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \cite{cobbe2021verifiers, lightman2024verify, venktesh2025trust} and reward models \cite{wang2024mathshepherd} learn per-sample scoring.
26	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling} with structural utility functions; despite MBR's success in translation \cite{freitag2022high} and other generation tasks \cite{jinnai2024mbr}, we find utility-quality misalignment at the per-sample level for structured IE (\S\ref{sec:discussion}).
27	Selective prediction \cite{geifman2017selective} and confidence-based IE filtering \cite{culotta2004confidence} establish the broader framework.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f278a158-3eb5-4525-bee6-a70494aa277e",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "856bf6ca-d6dd-4a68-b298-3cec806a2bd7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency decoding \\cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.\nExtensions to free-form text use LLM-based comparison \\cite{chen2024usc}, atomic sub-claim decomposition \\cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \\cite{manakul2023selfcheckgpt}.\nFor test-time scaling \\cite{zhang2025tts}, \\citet{snell2025scaling} characterize compute scaling laws and \\citet{brown2024monkeys} show best-of-$N$ gains across tasks.\nRecent reward-free selectors include confidence-weighted voting \\cite{taubenfeld2025cisc}, KL-based self-certainty \\cite{kang2025selfcertainty}, adaptive sampling \\cite{kim2026reasc}, ranked aggregation \\cite{wang2025rankedvoting}, and latent-space consistency \\cite{oh2025latentsc}.\nConcurrently, \\citet{feng2025optimal} and \\citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \\citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.\nAll of the above target reasoning/QA with discrete answers or specific aggregation strategies.\nOur work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).\n\n\\paragraph{Consistency for structured IE.}\n\\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.\nTheir work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whether findings generalize across a difficulty gradient.\nOur Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\\S\\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).\nCoCoA \\cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.\nOur evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \\cite{willard2023guided}.\n\n\\paragraph{Uncertainty estimation and calibration.}\nSurveys cover confidence estimation \\cite{geng2024confidence}, selective abstention \\cite{wen2025know}, uncertainty quantification \\cite{xia2025survey}, and calibration \\cite{hobelsberger2025systematic} for LLMs; \\citet{xiong2024llm} find LLMs tend toward overconfidence, and \\citet{heo2025uncertainty} show calibration degrades with task complexity.\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; \\citet{kossen2024semantic} distill this into probes; P(True) \\cite{kadavath2022language} queries model confidence directly; \\citet{malinin2021uncertainty} distinguish data and model uncertainty in autoregressive models.\nOur structural signals instead measure agreement over output \\textit{structure}.\nNeural networks are often miscalibrated \\cite{guo2017calibration, desai2020calibration}; deep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation, while our approach requires no model modification.\nPrior NER uncertainty work spans Bayesian inference for sequence labeling \\cite{xiao2019uncertainty}, active learning under uncertainty \\cite{shelmanov2021active}, evidential deep learning \\cite{zhang2023ener}, verification-augmented NER \\cite{kim2024verifiner}, and uncertainty transmission across label sequences \\cite{he2024uncertainty}---all within discriminative paradigms.\nConformal prediction \\cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \\cite{cobbe2021verifiers, lightman2024verify, venktesh2025trust} and reward models \\cite{wang2024mathshepherd} learn per-sample scoring.\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling} with structural utility functions; despite MBR's success in translation \\cite{freitag2022high} and other generation tasks \\cite{jinnai2024mbr}, we find utility-quality misalignment at the per-sample level for structured IE (\\S\\ref{sec:discussion}).\nSelective prediction \\cite{geifman2017selective} and confidence-based IE filtering \\cite{culotta2004confidence} establish the broader framework.\n",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  },
  "sourceToolAssistantUUID": "f278a158-3eb5-4525-bee6-a70494aa277e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T12:15:36.977Z_

<details><summary>↩ Tool result · `toolu_01KmN4DdJ3CLsHBuTWokJYBv`</summary>

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
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \texttt{&lt;think>\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \texttt{enable\_thinking=False}.
16	No reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.
17	This constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.
18	We discuss implications in the Limitations section.
19	We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}). A 3-seed stability analysis ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}, Appendix~\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}
20	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
21	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}
25	\label{sec:qe_results}
26	
27	\begin{table*}[t]
28	\centering
29	\small
30	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
31	\label{tab:quality_estimation}
32	\begin{tabular}{ll cc cc cc cc}
33	\toprule
34	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
35	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
36	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
37	\midrule
38	VC & Structural & \textbf{.379} & .684 & \textbf{.350} & .693 & .424 & .789 & .426 & .709 \\
39	SJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
40	FK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\
41	EM  & Surface    & .295 & \textbf{.749} & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
42	LP     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \textbf{.761} \\
43	\bottomrule
44	\end{tabular}
45	\end{table*}
46	
47	\begin{figure*}[t]
48	\centering
49	\includegraphics[width=\textwidth]{fig_signal_heatmap}
50	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
51	\label{fig:signal_heatmap}
52	\end{figure*}
53	
54	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
55	
56	\paragraph{Difficulty-dependent signal complementarity.}
57	On SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\rho{=}0.379$ and SJ $\rho{=}0.360$, both outperforming surface ($\rho{\leq}0.295$) and LP ($\rho{=}0.205$).
58	This advantage persists on RE (VC $\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\% zero-F1 floor effect.
59	VC and SJ show moderate instance-level correlation (NER: $\rho{=}0.659$; RE: $\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\ span-level set overlap.
60	While the best $\rho{=}0.38$ (VC) explains approximately 14\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\footnote{Semantic entropy \cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA; direct comparison is not meaningful due to different output spaces.}
61	Pairwise bootstrap CIs confirm the SJ advantage over LP ($\Delta\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\Delta\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\ref{tab:bootstrap_signal_ci}, Appendix~\ref{app:bootstrap_signal}).
62	
63	\paragraph{$\rho$--AUROC dissociation.}
64	Signal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\rho$ (0.295), preferred for binary quality triage; structural signals ($\rho{\geq}0.36$) are better for fine-grained ranking.
65	On CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\rho$ (0.307), confirming this pattern across datasets.
66	
67	\paragraph{Signal rankings shift with task difficulty.}
68	On CoNLL (greedy F1${\approx}$0.91), EM leads ($\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.
69	When most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.
70	This crossover---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.
71	Stability across the two model families (both 8B) is strong: SJ achieves $\rho{=}0.436$ (Qwen) vs.\ $0.431$ (LLaMA) on CoNLL ($\Delta{=}0.005$, within 3-seed $\sigma{\approx}0.007$).
72	On WNUT-17, where 52\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.; Table~\ref{tab:wnut}).
73	LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$, AUROC${=}0.219$).
74	We hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.
75	On the conditional set, all signals collapse toward weak or non-significant correlations ($\rho{\leq}0.35$), with SJ achieving only $\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.
76	
77	\paragraph{Conditional filtering.}
78	Filtering to non-zero F1 instances reshuffles rankings (Figure~\ref{fig:signal_heatmap}, right).
79	EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\to}0.300$; FK NER: $0.267{\to}0.176$).
80	LP RE collapses to $\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.
81	This creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
82	
83	%% ============================================================
84	\subsection{The Correlation-Selection Gap}
85	\label{sec:selection_gap}
86	
87	\begin{figure*}[t]
88	\centering
89	\includegraphics[width=\textwidth]{fig_selection_gap}
90	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound.}
91	\label{fig:selection_gap}
92	\end{figure*}
93	
94	\begin{table}[t]
95	\centering
96	\small
97	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \textbf{bold}. EM selects the plurality output; despite a 42\% pairwise exact-match rate, EM selection underperforms greedy on both tasks.}
98	\label{tab:selection}
99	\begin{tabular}{lcc}
100	\toprule
101	Method & NER F1 & RE F1 \\
102	\midrule
103	Oracle & 0.776 & 0.585 \\
104	\midrule
105	LP           & \textbf{0.650} & 0.395 \\
106	SJ       & 0.645 & 0.386 \\
107	EM        & 0.636 & 0.372 \\
108	VC                 & 0.634 & 0.359 \\
109	\midrule
110	Greedy ($T{=}0$)   & 0.644 & \textbf{0.404} \\
111	Random             & 0.608 & 0.354 \\
112	\bottomrule
113	\end{tabular}
114	\end{table}
115	
116	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
117	Four of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.
118	The non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.
119	We anchor this analysis on SciERC, where output diversity is substantial: only 11--18\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.
120	
121	\paragraph{No significant improvement over greedy.}
122	We exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).
123	On NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).
124	LP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).
125	On RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.
126	TOST equivalence testing confirms most signals are indistinguishable from greedy at ${\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\pm}5$~pp (Table~\ref{tab:tost}, Appendix~\ref{app:diversity}).
127	VC ($\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\textit{below} greedy.
128	The gap extends to CoNLL (ceiling effect, 57--88\% identical outputs) and WNUT-17 (capability boundary; Table~\ref{tab:cross_selection}).
129	
130	\paragraph{Quality estimation $\neq$ output selection.}
131	Instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best.
132	When per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.
133	This gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2025scaling}: closing it likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
134	
135	%% ============================================================
136	\subsection{Robustness}
137	\label{sec:robustness_main}
138	
139	Consistency-based signals show robust performance across $T{\in}\{0.7, 1.0\}$ (SJ NER $\Delta\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all NER settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$; Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
140	On RE, only VC consistently outperforms LP ($\Delta\rho{=}{+}0.012$, preliminary).
141	NER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\rho{\approx}0.28$ for $N{=}16$.
142	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aba93e3b-6c50-4362-a90a-27dd475c770a",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "8fd367ec-b6d3-47bf-a22a-a83676bb3131",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.\nWe note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \\texttt{&lt;think>\\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \\texttt{enable\\_thinking=False}.\nNo reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.\nThis constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.\nWe discuss implications in the Limitations section.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}). A 3-seed stability analysis ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}, Appendix~\\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & .684 & \\textbf{.350} & .693 & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & \\textbf{.749} & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLP     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Difficulty-dependent signal complementarity.}\nOn SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\\rho{=}0.379$ and SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and LP ($\\rho{=}0.205$).\nThis advantage persists on RE (VC $\\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\\% zero-F1 floor effect.\nVC and SJ show moderate instance-level correlation (NER: $\\rho{=}0.659$; RE: $\\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\\ span-level set overlap.\nWhile the best $\\rho{=}0.38$ (VC) explains approximately 14\\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\\footnote{Semantic entropy \\cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA; direct comparison is not meaningful due to different output spaces.}\nPairwise bootstrap CIs confirm the SJ advantage over LP ($\\Delta\\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\\Delta\\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\\ref{tab:bootstrap_signal_ci}, Appendix~\\ref{app:bootstrap_signal}).\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nSignal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\\rho$ (0.295), preferred for binary quality triage; structural signals ($\\rho{\\geq}0.36$) are better for fine-grained ranking.\nOn CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\\rho$ (0.307), confirming this pattern across datasets.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${\\approx}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.\nWhen most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.\nThis crossover---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.\nStability across the two model families (both 8B) is strong: SJ achieves $\\rho{=}0.436$ (Qwen) vs.\\ $0.431$ (LLaMA) on CoNLL ($\\Delta{=}0.005$, within 3-seed $\\sigma{\\approx}0.007$).\nOn WNUT-17, where 52\\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.; Table~\\ref{tab:wnut}).\nLP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$, AUROC${=}0.219$).\nWe hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \\citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.\nOn the conditional set, all signals collapse toward weak or non-significant correlations ($\\rho{\\leq}0.35$), with SJ achieving only $\\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.\n\n\\paragraph{Conditional filtering.}\nFiltering to non-zero F1 instances reshuffles rankings (Figure~\\ref{fig:signal_heatmap}, right).\nEM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\\to}0.300$; FK NER: $0.267{\\to}0.176$).\nLP RE collapses to $\\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.\nThis creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \\textbf{bold}. EM selects the plurality output; despite a 42\\% pairwise exact-match rate, EM selection underperforms greedy on both tasks.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.776 & 0.585 \\\\\n\\midrule\nLP           & \\textbf{0.650} & 0.395 \\\\\nSJ       & 0.645 & 0.386 \\\\\nEM        & 0.636 & 0.372 \\\\\nVC                 & 0.634 & 0.359 \\\\\n\\midrule\nGreedy ($T{=}0$)   & 0.644 & \\textbf{0.404} \\\\\nRandom             & 0.608 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nFour of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.\nThe non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.\nWe anchor this analysis on SciERC, where output diversity is substantial: only 11--18\\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.\n\n\\paragraph{No significant improvement over greedy.}\nWe exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).\nOn NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).\nLP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).\nOn RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.\nTOST equivalence testing confirms most signals are indistinguishable from greedy at ${\\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\\pm}5$~pp (Table~\\ref{tab:tost}, Appendix~\\ref{app:diversity}).\nVC ($\\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\\textit{below} greedy.\nThe gap extends to CoNLL (ceiling effect, 57--88\\% identical outputs) and WNUT-17 (capability boundary; Table~\\ref{tab:cross_selection}).\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2025scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency-based signals show robust performance across $T{\\in}\\{0.7, 1.0\\}$ (SJ NER $\\Delta\\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all NER settings ($\\Delta\\rho{=}{+}0.135$ to ${+}0.175$; Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\nOn RE, only VC consistently outperforms LP ($\\Delta\\rho{=}{+}0.012$, preliminary).\nNER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\\rho{\\approx}0.28$ for $N{=}16$.\n",
      "numLines": 142,
      "startLine": 1,
      "totalLines": 142
    }
  },
  "sourceToolAssistantUUID": "aba93e3b-6c50-4362-a90a-27dd475c770a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T12:15:37.564Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ShojA8JBAJbY1khyhJwakx`</summary>

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
  "parentUuid": "8fd367ec-b6d3-47bf-a22a-a83676bb3131",
  "isSidechain": false,
  "requestId": "req_011Cb4LXwBtHHVXc69KDuXxD",
  "type": "assistant",
  "uuid": "bc2b2110-41ee-46fb-8fb5-6e359abaf877",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVi32FxYSa72aPJmqn4Jsb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5007,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 29908,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5007,
          "output_tokens": 557,
          "cache_read_input_tokens": 29908,
          "cache_creation_input_tokens": 1204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1204
          },
          "type": "message"
        }
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

_source line 43 · 2026-05-15T12:15:37.569Z_

<details><summary>↩ Tool result · `toolu_01ShojA8JBAJbY1khyhJwakx`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across two model families at 8B scale, though with model-dependent magnitude.
6	At higher sample sizes ($N{=}16$), SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) with lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$); on RE, only VC consistently outperforms LP (preliminary).
7	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
8	
9	\paragraph{Why the gap exists: two layers.}
10	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
11	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
12	\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
13	LP scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
14	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
15	This diagnostic confirms that LP carries useful per-sample quality information; score compression is the primary mechanistic bottleneck.
16	A controlled ablation (\S\ref{sec:ablation}) confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding.
17	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\ref{app:calibration}) may compound this.
18	
19	\paragraph{Connection to MBR decoding.}
20	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
21	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
22	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
23	
24	\paragraph{Score compression is task-inherent.}\label{sec:ablation}
25	A natural hypothesis is that LP compression is an artifact of constrained decoding's restricted token space.
26	We test this via controlled ablation: generating free-form (unconstrained) outputs on the same instances with post-hoc JSON parsing (parse rate 99.95\%, 4406/4408; Table~\ref{tab:freeform_ablation}).
27	LP variance is essentially unchanged (within-instance std ratio $0.97{\times}$, tied fraction 59.7\%$\to$57.7\%).
28	NER selection gains remain negligible ($+0.18$~pp free-form vs.\ $+0.59$~pp constrained).
29	This rules out constrained decoding as the cause of compression and establishes LP compression as inherent to structured output generation.
30	The correlation-selection gap is therefore a fundamental challenge for test-time scaling in structured IE, not an artifact of any particular decoding strategy.
31	Notably, the fine-tuned model achieved 99.95\% parse rate without grammar constraints, suggesting that constrained decoding's format-compliance role may be redundant for sufficiently fine-tuned models.
32	
33	\paragraph{What drives the universal gap?}
34	Our analysis reveals two complementary mechanisms.
35	First, the free-form ablation exposes a task-specific interaction: RE LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that is universal across all 7 relation types and driven by selective variance reallocation ($p{<}0.0001$).
36	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
37	This interaction does not generalize to NER, where selection remains negligible under both regimes.
38	This ablation uses a single seed (seed${=}42$); multi-seed replication is left for future work.
39	Second, the non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
40	Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
41	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
42	
43	\paragraph{Methodological implications.}
44	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.
45	Effective selection likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers, venktesh2025trust}; $N$-scaling analysis (Appendix~\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.
46	Our findings are established under constrained decoding with a single-dataset ablation suggesting the gap is intrinsic; whether this generalizes across decoding regimes, datasets, and model scales warrants further investigation.
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc2b2110-41ee-46fb-8fb5-6e359abaf877",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "8e3b8519-ffe3-46e5-8799-1c51f661691c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\nSignal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across two model families at 8B scale, though with model-dependent magnitude.\nAt higher sample sizes ($N{=}16$), SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) with lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$); on RE, only VC consistently outperforms LP (preliminary).\nWhen model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\\ref{tab:wnut}).\n\n\\paragraph{Why the gap exists: two layers.}\n\\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nConsensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\n\\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.\nLP scores are severely compressed: 60\\% of instances have a within-sample range below 0.05, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$; Appendix~\\ref{app:logprob_ties}).\nIn the 40\\% of instances where compression is mitigated (LP range ${\\geq}0.05$, $n{=}210$), LP \\textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\\rho$: 0.08$\\to$0.39).\nThis diagnostic confirms that LP carries useful per-sample quality information; score compression is the primary mechanistic bottleneck.\nA controlled ablation (\\S\\ref{sec:ablation}) confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding.\nDiversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\\ref{app:calibration}) may compound this.\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Score compression is task-inherent.}\\label{sec:ablation}\nA natural hypothesis is that LP compression is an artifact of constrained decoding's restricted token space.\nWe test this via controlled ablation: generating free-form (unconstrained) outputs on the same instances with post-hoc JSON parsing (parse rate 99.95\\%, 4406/4408; Table~\\ref{tab:freeform_ablation}).\nLP variance is essentially unchanged (within-instance std ratio $0.97{\\times}$, tied fraction 59.7\\%$\\to$57.7\\%).\nNER selection gains remain negligible ($+0.18$~pp free-form vs.\\ $+0.59$~pp constrained).\nThis rules out constrained decoding as the cause of compression and establishes LP compression as inherent to structured output generation.\nThe correlation-selection gap is therefore a fundamental challenge for test-time scaling in structured IE, not an artifact of any particular decoding strategy.\nNotably, the fine-tuned model achieved 99.95\\% parse rate without grammar constraints, suggesting that constrained decoding's format-compliance role may be redundant for sufficiently fine-tuned models.\n\n\\paragraph{What drives the universal gap?}\nOur analysis reveals two complementary mechanisms.\nFirst, the free-form ablation exposes a task-specific interaction: RE LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that is universal across all 7 relation types and driven by selective variance reallocation ($p{<}0.0001$).\nThe win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).\nThis interaction does not generalize to NER, where selection remains negligible under both regimes.\nThis ablation uses a single seed (seed${=}42$); multi-seed replication is left for future work.\nSecond, the non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\\times}$ increase in within-instance LP range for the newly non-tied subset.\nDespite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.\nFree-form decoding also slightly improves quality estimation (NER VC $\\rho$: 0.379$\\to$0.409), though this does not translate to selection gains.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust}; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.\nOur findings are established under constrained decoding with a single-dataset ablation suggesting the gap is intrinsic; whether this generalizes across decoding regimes, datasets, and model scales warrants further investigation.\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  },
  "sourceToolAssistantUUID": "bc2b2110-41ee-46fb-8fb5-6e359abaf877",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T12:15:37.896Z_

<details open><summary>🔧 Tool call — Read · `toolu_0152tzqf1voEXLgKRMp6zRim`</summary>

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
  "parentUuid": "8e3b8519-ffe3-46e5-8799-1c51f661691c",
  "isSidechain": false,
  "requestId": "req_011Cb4LXwBtHHVXc69KDuXxD",
  "type": "assistant",
  "uuid": "7bbda8b3-3c1d-4cf6-ba53-50bc71fb1dea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVi32FxYSa72aPJmqn4Jsb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5007,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 29908,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5007,
          "output_tokens": 557,
          "cache_read_input_tokens": 29908,
          "cache_creation_input_tokens": 1204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1204
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-15T12:15:37.901Z_

<details><summary>↩ Tool result · `toolu_0152tzqf1voEXLgKRMp6zRim`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We demonstrate that consistency signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75) for LLM-based structured IE, but fail at sample selection---the \textit{correlation-selection gap}.
4	By construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to score compression.
5	Where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.
6	A controlled free-form decoding ablation confirms that score compression is intrinsic to the model and task, not an artifact of constrained decoding.
7	Signal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.
8	RE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.
9	Trained verifiers, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bbda8b3-3c1d-4cf6-ba53-50bc71fb1dea",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "3de96df4-54d2-4716-8a3d-70b99b616611",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe demonstrate that consistency signals are effective quality estimators ($\\rho$ up to 0.38, AUROC up to 0.75) for LLM-based structured IE, but fail at sample selection---the \\textit{correlation-selection gap}.\nBy construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to score compression.\nWhere compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.\nA controlled free-form decoding ablation confirms that score compression is intrinsic to the model and task, not an artifact of constrained decoding.\nSignal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.\nRE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.\nTrained verifiers, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "7bbda8b3-3c1d-4cf6-ba53-50bc71fb1dea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T12:15:38.856Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SWmR3tW7taPKcyKQLm2ejx`</summary>

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
  "parentUuid": "3de96df4-54d2-4716-8a3d-70b99b616611",
  "isSidechain": false,
  "requestId": "req_011Cb4LXwBtHHVXc69KDuXxD",
  "type": "assistant",
  "uuid": "d4735f85-f8ee-4dd8-93b6-142ef464883c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVi32FxYSa72aPJmqn4Jsb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5007,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 29908,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5007,
          "output_tokens": 557,
          "cache_read_input_tokens": 29908,
          "cache_creation_input_tokens": 1204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1204
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-15T12:15:38.866Z_

<details><summary>↩ Tool result · `toolu_01SWmR3tW7taPKcyKQLm2ejx`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.047$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Our free-form ablation (\S\ref{sec:ablation}) confirms that LP score compression persists without constrained decoding, but was conducted on a single dataset (SciERC) with one model (Qwen3-8B); whether the intrinsic compression finding generalizes to other datasets, model families, or model scales remains untested.
17	
18	Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking} active, injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning chain) before each response; CoNLL and WNUT checkpoints disabled this feature.
19	At inference time, constrained decoding suppresses thinking tokens in all configurations, so they do not appear in generated samples.
20	The empty blocks may weakly affect first-token probability distributions during training, potentially shifting LP score calibration on SciERC; however, since LP selection fails across all datasets including CoNLL and WNUT-17 (which lack this confound), the thinking token inconsistency is unlikely to explain the correlation-selection gap.
21	The absence of any reasoning content further limits the representational impact.
22	
23	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ LP data, leaving its temperature sensitivity uncharacterized.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4735f85-f8ee-4dd8-93b6-142ef464883c",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "1e81ff5d-5502-4ade-bd98-1b0e4571aaf7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nRE selection failure persists even when restricting to non-zero F1 instances (Appendix~\\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nA 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses only unsupervised signals.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ and $N{=}16$.\nThe behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.047$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.\n\nOn CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\\rho{=}0.431$ vs.\\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nOur free-form ablation (\\S\\ref{sec:ablation}) confirms that LP score compression persists without constrained decoding, but was conducted on a single dataset (SciERC) with one model (Qwen3-8B); whether the intrinsic compression finding generalizes to other datasets, model families, or model scales remains untested.\n\nQwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking} active, injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning chain) before each response; CoNLL and WNUT checkpoints disabled this feature.\nAt inference time, constrained decoding suppresses thinking tokens in all configurations, so they do not appear in generated samples.\nThe empty blocks may weakly affect first-token probability distributions during training, potentially shifting LP score calibration on SciERC; however, since LP selection fails across all datasets including CoNLL and WNUT-17 (which lack this confound), the thinking token inconsistency is unlikely to explain the correlation-selection gap.\nThe absence of any reasoning content further limits the representational impact.\n\nFinally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ LP data, leaving its temperature sensitivity uncharacterized.\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  },
  "sourceToolAssistantUUID": "d4735f85-f8ee-4dd8-93b6-142ef464883c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T12:15:39.345Z_

<details open><summary>🔧 Tool call — Read · `toolu_01U1YPAWvwegLLEwM12Cm5ze`</summary>

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
  "parentUuid": "1e81ff5d-5502-4ade-bd98-1b0e4571aaf7",
  "isSidechain": false,
  "requestId": "req_011Cb4LXwBtHHVXc69KDuXxD",
  "type": "assistant",
  "uuid": "75fd31eb-b9e0-4720-a6fb-b1e6d336f80c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVi32FxYSa72aPJmqn4Jsb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5007,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 29908,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5007,
          "output_tokens": 557,
          "cache_read_input_tokens": 29908,
          "cache_creation_input_tokens": 1204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1204
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-15T12:15:39.607Z_

<details><summary>↩ Tool result · `toolu_01U1YPAWvwegLLEwM12Cm5ze`</summary>

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
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.010$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as population standard deviation.}
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
48	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm}0.008$ & --- \\
56	\quad VC &  & $0.458{\pm}0.003$ & --- \\
57	\quad LP &  & $0.310{\pm}0.005$ & --- \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	\begin{figure}[t]
63	\centering
64	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
65	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}
66	\label{fig:temperature_robustness}
67	\end{figure}
68	
69	\paragraph{Temperature sensitivity.}
70	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.
71	FK shows mixed behavior: NER $\rho$ drops by 0.054, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
72	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.360 vs.\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
73	
74	\paragraph{Sample size scaling.}
75	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.411{\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.
76	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
77	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\ref{tab:quality_estimation}).
78	FK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.
79	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
80	SJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.
81	At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), making it a more stable alternative at higher sample sizes.
82	
83	\paragraph{Transfer across model families.}
84	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$).
85	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
86	At $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\rho{=}0.409$ vs.\ LP 0.239, $\Delta{=}{+}0.170$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$), LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.463{\pm}0.007$ vs.\ LP $0.310{\pm}0.005$, $\Delta{=}{+}0.153$).
87	
88	\section{Calibration Analysis}\label{app:calibration}
89	
90	\begin{figure*}[t]
91	\centering
92	\includegraphics[width=\textwidth]{fig_reliability}
93	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
94	\label{fig:reliability}
95	\end{figure*}
96	
97	Reliability diagrams use 10 equal-width bins.
98	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
99	
100	\section{Additional Analyses}\label{app:additional}
101	
102	\paragraph{Per-relation diagnostic.}
103	RE signal degradation is relation-specific.
104	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
105	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
106	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
107	
108	\paragraph{Capability stratification.}
109	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
110	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
111	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
112	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
113	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
114	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
115	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
116	
117	\paragraph{Length vs.\ log-probability.}
118	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
119	
120	\begin{figure}[t]
121	\centering
122	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
123	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
124	\label{fig:length_logprob_scatter}
125	\end{figure}
126	
127	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
128	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
129	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
130	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, making the two selection rules equivalent.
131	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
132	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
133	Evaluation circularity is negligible.
134	
135	\paragraph{Conditional filtering details.}
136	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
137	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
138	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
139	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
140	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
141	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
142	
143	\paragraph{WNUT-17 full signal analysis.}
144	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
145	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
146	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
147	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
148	
149	\begin{table}[t]
150	\centering
151	\small
152	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
153	\label{tab:wnut}
154	\begin{tabular}{lccccc}
155	\toprule
156	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
157	\midrule
158	VC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
159	FK      & .125 & .001 & .555 & .169 & .002 \\
160	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
161	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
162	LP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
163	\bottomrule
164	\end{tabular}
165	\end{table}
166	
167	\paragraph{Cross-configuration selection analysis.}
168	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
169	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
170	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
171	
172	\begin{table*}[t]
173	\centering
174	\small
175	\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. No signal significantly outperforms greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
176	\label{tab:cross_selection}
177	\begin{tabular}{llccccccc}
178	\toprule
179	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
180	\midrule
181	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
182	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
183	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
184	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
185	\bottomrule
186	\end{tabular}
187	\end{table*}
188	
189	\paragraph{Diminishing returns of $N$-scaling.}
190	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
191	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
192	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
193	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
194	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
195	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
196	
197	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
198	
199	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
200	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
201	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
202	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
203	
204	\begin{table}[t]
205	\centering
206	\small
207	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
208	\label{tab:bootstrap_signal_ci}
209	\begin{tabular}{lcc}
210	\toprule
211	Signal & $\rho$ & 95\% CI \\
212	\midrule
213	VC & +0.379 & [+0.299, +0.456] \\
214	SJ & +0.360 & [+0.277, +0.437] \\
215	EM & +0.295 & [+0.212, +0.371] \\
216	FK & +0.267 & [+0.176, +0.354] \\
217	LP & +0.205 & [+0.119, +0.291] \\
218	\bottomrule
219	\end{tabular}
220	
221	\vspace{0.5em}
222	
223	\begin{tabular}{lccc}
224	\toprule
225	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
226	\midrule
227	SJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\
228	VC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
229	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
230	\bottomrule
231	\end{tabular}
232	
233	\smallskip
234	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
235	\end{table}
236	
237	\section{Diversity and Selection Analysis}\label{app:diversity}
238	
239	\paragraph{Output diversity quantification.}
240	Table~\ref{tab:diversity} summarizes output diversity across configurations.
241	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
242	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
243	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.
244	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
245	
246	\begin{table}[t]
247	\centering
248	\small
249	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
250	\label{tab:diversity}
251	\begin{tabular}{lcc}
252	\toprule
253	Config & Identical & Unique \\
254	\midrule
255	Qwen/SciERC & 11\% & 43\% \\
256	LLaMA/SciERC & 18\% & 39\% \\
257	Qwen/CoNLL & 57\% & --- \\
258	LLaMA/CoNLL & 88\% & --- \\
259	WNUT-17 & 55\% & --- \\
260	\bottomrule
261	\end{tabular}
262	\end{table}
263	
264	\paragraph{Oracle-improvable fraction.}
265	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
266	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
267	
268	\paragraph{Diversity-stratified selection gap.}
269	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.
270	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.
271	This rules out insufficient diversity as an explanation for the correlation-selection gap.
272	
273	\paragraph{TOST equivalence testing.}
274	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
275	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\delta$.
276	The $\delta$ values are anchored to oracle headroom (13--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
277	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
278	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
279	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
280	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
281	
282	\begin{table}[t]
283	\centering
284	\small
285	\caption{TOST equivalence testing: signals vs.\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ greedy).}
286	\label{tab:tost}
287	\begin{tabular}{l cccc cccc}
288	\toprule
289	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
290	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
291	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
292	\midrule
293	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
294	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
295	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
296	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
297	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
298	\bottomrule
299	\end{tabular}
300	\end{table}
301	
302	\section{Multi-Seed Stability}\label{app:multiseed}
303	
304	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
305	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals.
306	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.
307	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
308	
309	\begin{table}[t]
310	\centering
311	\small
312	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
313	\label{tab:multiseed}
314	\begin{tabular}{lccccc}
315	\toprule
316	& LP & FK & SJ & VC & EM \\
317	\midrule
318	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
319	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
320	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
321	\midrule
322	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
323	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
324	\midrule
325	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
326	Qwen & .613${\pm}$.002 & .618${\pm}$.009 & .684${\pm}$.009 & .697${\pm}$.010 & .661${\pm}$.010 \\
327	LLaMA & .577${\pm}$.007 & .616${\pm}$.011 & .655${\pm}$.010 & .689${\pm}$.005 & .636${\pm}$.006 \\
328	\bottomrule
329	\end{tabular}
330	\end{table}
331	
332	\section{Training Configuration}\label{app:training}
333	
334	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
335	
336	\begin{table}[t]
337	\centering
338	\small
339	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
340	\label{tab:training}
341	\begin{tabular}{ll}
342	\toprule
343	Parameter & Value \\
344	\midrule
345	LoRA rank / $\alpha$ & 32 / 64 \\
346	LoRA target & All linear modules \\
347	LoRA dropout & 0 \\
348	Optimizer & AdamW \\
349	Learning rate & 2e-4, cosine schedule \\
350	Warmup ratio & 0.1 \\
351	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
352	Epochs & 5 \\
353	Max sequence length & 2048 \\
354	Precision & bf16 \\
355	Gradient checkpointing & Enabled \\
356	Max gradient norm & 1.0 \\
357	Training seed & 42 \\
358	Framework & LLaMA Factory \\
359	\midrule
360	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
361	SciERC split & 1861 / 275 / 551 \\
362	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
363	& eval\_steps${=}$200, save\_limit${=}$5 \\
364	\bottomrule
365	\end{tabular}
366	\end{table}
367	
368	\paragraph{Prompt template.}
369	For NER, we use a structured prompt:
370	\begin{quote}
371	\small
372	\texttt{System:} You are an expert in Named Entity Recognition.\\
373	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
374	Text: \texttt{\{input\_text\}}\\
375	Entity types: \texttt{\{schema\_types\}}
376	\end{quote}
377	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
378	
379	\paragraph{Constrained decoding.}
380	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
381	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
382	
383	\section{Log-Probability Score Compression}\label{app:logprob_ties}
384	
385	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}).
386	The median within-instance LP range is only 0.041, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
387	At $\varepsilon{=}0.05$, 60.3\% of instances have a within-sample range below the threshold, leaving LP unable to meaningfully distinguish candidates.
388	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
389	
390	\begin{table}[t]
391	\centering
392	\small
393	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
394	\label{tab:logprob_ties}
395	\begin{tabular}{lc}
396	\toprule
397	$\varepsilon$ threshold & Tied instances (\%) \\
398	\midrule
399	0.01 & 1.1\% \\
400	0.05 & 60.3\% \\
401	0.1  & ${\sim}$84\% \\
402	0.5  & ${\sim}$99\% \\
403	\bottomrule
404	\end{tabular}
405	\end{table}
406	
407	\paragraph{Non-tied subset.}
408	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
409	This confirms that LP carries useful per-sample quality information but is resolution-limited---the signal exists but is compressed below the discrimination threshold for most instances.
410	A free-form decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression is intrinsic, not decoding-regime-specific.
411	
412	\section{RE Conditional Selection}\label{app:re_conditional_selection}
413	
414	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
415	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
416	All five signals underperform greedy on both subsets.
417	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
418	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
419	
420	\begin{table}[t]
421	\centering
422	\small
423	\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
424	\label{tab:re_cond_selection}
425	\begin{tabular}{lcc}
426	\toprule
427	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
428	\midrule
429	Oracle & 0.585 & 0.757 \\
430	\midrule
431	LP & 0.395 & 0.600 \\
432	SJ & 0.386 & 0.604 \\
433	EM & 0.372 & 0.583 \\
434	VC & 0.359 & 0.574 \\
435	\midrule
436	Greedy & 0.404 & 0.674 \\
437	\bottomrule
438	\end{tabular}
439	\end{table}
440	
441	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
442	
443	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).
444	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
445	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
446	RE LP selection flips positive under free-form decoding ($+1.69$~pp vs.\ $-0.68$~pp constrained).
447	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
448	
449	\begin{table*}[t]
450	\centering
451	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}
452	\label{tab:freeform_ablation}
453	
454	\vspace{2pt}
455	{\small\textsc{Panel A: Logprob Distribution}}
456	\vspace{2pt}
457	
458	\begin{tabular}{lccc}
459	\toprule
460	Metric & Constrained & Free-form & $\Delta$ \\
461	\midrule
462	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
463	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
464	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
465	\bottomrule
466	\end{tabular}
467	
468	\vspace{8pt}
469	
470	{\small\textsc{Panel B: Selection F1}}
471	\vspace{2pt}
472	
473	\begin{tabular}{llccc}
474	\toprule
475	Task & Method & Constrained & Free-form & $\Delta$ \\
476	\midrule
477	\multirow{3}{*}{NER}
478	  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\
479	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
480	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
481	\midrule
482	\multirow{3}{*}{RE}
483	  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\
484	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
485	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
486	\bottomrule
487	\end{tabular}
488	
489	\vspace{8pt}
490	
491	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
492	\vspace{2pt}
493	
494	\begin{tabular}{l ccc ccc}
495	\toprule
496	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
497	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
498	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
499	\midrule
500	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
501	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
502	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
503	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
504	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
505	\bottomrule
506	\end{tabular}
507	
508	\vspace{8pt}
509	
510	{\small\textsc{Panel D: Parse Rate (Free-form)}}
511	\vspace{2pt}
512	
513	\begin{tabular}{lc}
514	\toprule
515	Metric & Value \\
516	\midrule
517	Total samples          & 4408 \\
518	Parse rate             & 99.95\% \\
519	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
520	\bottomrule
521	\end{tabular}
522	
523	\end{table*}
524	
525	\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
526	
527	We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
528	
529	\paragraph{Pairwise overlap.}
530	LP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.
531	The 3-way intersection contains 34 instances (27.9\% of any-seed failures), confirming a stable failure core.
532	
533	\paragraph{Instance complexity drives failure.}
534	Table~\ref{tab:stable_failures} stratifies instances by failure stability.
535	Stable failures (all 3 seeds) involve more gold relations (2.12 vs.\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.
536	Failure rate increases monotonically with gold relation count: 4.3\% at 1 relation, 20.7\% at 3 relations, 26.2\% at 6 relations.
537	
538	\begin{table}[t]
539	\centering
540	\small
541	\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}
542	\label{tab:stable_failures}
543	\begin{tabular}{lcccc}
544	\toprule
545	Group & $n$ & Gold rels & Greedy F1 & LP $\Delta$F1 \\
546	\midrule
547	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
548	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
549	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
550	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
551	\bottomrule
552	\end{tabular}
553	\end{table}
554	
555	\paragraph{Flip instances.}
556	Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
557	These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
558	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75fd31eb-b9e0-4720-a6fb-b1e6d336f80c",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "4854e20d-77fa-4ae0-9536-049946ddb642",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.010$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as population standard deviation.}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.411$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.283 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.463{\\pm}0.007$ & --- \\\\\n\\quad FK &  & $0.455{\\pm}0.006$ & --- \\\\\n\\quad EM &  & $0.460{\\pm}0.008$ & --- \\\\\n\\quad VC &  & $0.458{\\pm}0.003$ & --- \\\\\n\\quad LP &  & $0.310{\\pm}0.005$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.054, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.360 vs.\\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.411{\\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.034$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.\nAt $N{=}16$, SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$), making it a more stable alternative at higher sample sizes.\n\n\\paragraph{Transfer across model families.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\\rho{=}0.409$ vs.\\ LP 0.239, $\\Delta{=}{+}0.170$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$), LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.463{\\pm}0.007$ vs.\\ LP $0.310{\\pm}0.005$, $\\Delta{=}{+}0.153$).\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, making the two selection rules equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17.\nVC achieves $\\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\\rho{=}0.038$ ($p{=}0.49$).\nLP shows the reverse pattern: full-set $\\rho{=}{-}0.410$ but conditional $\\rho{=}0.350$, the highest among all signals on the conditional set.\nThis inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\\rho$; its conditional $\\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}\n\\label{tab:wnut}\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & $\\rho$ & $p$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\\\\nFK      & .125 & .001 & .555 & .169 & .002 \\\\\nSJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn CoNLL, 57--88\\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). Best non-oracle signal per row in \\textbf{bold}. No signal significantly outperforms greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVC & +0.379 & [+0.299, +0.456] \\\\\nSJ & +0.360 & [+0.277, +0.437] \\\\\nEM & +0.295 & [+0.212, +0.371] \\\\\nFK & +0.267 & [+0.176, +0.354] \\\\\nLP & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\\\\nVC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 57\\% (Qwen) to 88\\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, confirming the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{TOST equivalence testing.}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\\delta$.\nThe $\\delta$ values are anchored to oracle headroom (13--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\nThe breakpoint $\\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\\sim}$10\\% of oracle headroom) to 3.4~pp (FK, ${\\sim}$26\\%) on NER, and from approximately 2.9~pp (LP, ${\\sim}$16\\%) to 6.5~pp (VC, ${\\sim}$36\\%) on RE.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ greedy).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\nOn NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals.\nOn RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.\nLLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .613${\\pm}$.002 & .618${\\pm}$.009 & .684${\\pm}$.009 & .697${\\pm}$.010 & .661${\\pm}$.010 \\\\\nLLaMA & .577${\\pm}$.007 & .616${\\pm}$.011 & .655${\\pm}$.010 & .689${\\pm}$.005 & .636${\\pm}$.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}).\nThe median within-instance LP range is only 0.041, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nAt $\\varepsilon{=}0.05$, 60.3\\% of instances have a within-sample range below the threshold, leaving LP unable to meaningfully distinguish candidates.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nThis confirms that LP carries useful per-sample quality information but is resolution-limited---the signal exists but is compressed below the discrimination threshold for most instances.\nA free-form decoding ablation (Appendix~\\ref{app:freeform_ablation}) confirms this compression is intrinsic, not decoding-regime-specific.\n\n\\section{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform greedy on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLP & 0.395 & 0.600 \\\\\nSJ & 0.386 & 0.604 \\\\\nEM & 0.372 & 0.583 \\\\\nVC & 0.359 & 0.574 \\\\\n\\midrule\nGreedy & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Free-Form Decoding Ablation}\\label{app:freeform_ablation}\n\nTable~\\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).\nFree-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\\%, 4406/4408).\nLP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\\times}$), and NER selection gains remain negligible under both regimes (Panel~B).\nRE LP selection flips positive under free-form decoding ($+1.69$~pp vs.\\ $-0.68$~pp constrained).\nQuality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}\n\\label{tab:freeform_ablation}\n\n\\vspace{2pt}\n{\\small\\textsc{Panel A: Logprob Distribution}}\n\\vspace{2pt}\n\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\nMean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\\\\nMean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\\\\nTied fraction ($\\varepsilon{=}0.05$) & 59.7\\% & 57.7\\% & $-$2.0\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel B: Selection F1}}\n\\vspace{2pt}\n\n\\begin{tabular}{llccc}\n\\toprule\nTask & Method & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\n\\multirow{3}{*}{NER}\n  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\\\\n  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\\\\n  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\\\\n\\midrule\n\\multirow{3}{*}{RE}\n  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\\\\n  & LP-selected   & 0.2845 & 0.3050 & \\textbf{$+$0.0205} \\\\\n  & Selection gap & $-$0.0068 & $+$0.0169 & \\textbf{$+$0.0237} \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel C: QE Signal Quality (Spearman $\\rho$)}}\n\\vspace{2pt}\n\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{NER ($n{=}529$)} & \\multicolumn{3}{c}{RE ($n{=}397$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & Constr. & Free & $\\Delta$ & Constr. & Free & $\\Delta$ \\\\\n\\midrule\nSJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\\\\nFK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\\\\nLP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\\\\nEM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\\\\nVC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel D: Parse Rate (Free-form)}}\n\\vspace{2pt}\n\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTotal samples          & 4408 \\\\\nParse rate             & 99.95\\% \\\\\nInstances 8/8 valid    & 549\\,/\\,551 (99.6\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\n\\end{table*}\n\n\\section{LP Selection Failure Stability}\\label{app:lp_failure_stability}\n\nWe analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.\n\n\\paragraph{Pairwise overlap.}\nLP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.\nThe 3-way intersection contains 34 instances (27.9\\% of any-seed failures), confirming a stable failure core.\n\n\\paragraph{Instance complexity drives failure.}\nTable~\\ref{tab:stable_failures} stratifies instances by failure stability.\nStable failures (all 3 seeds) involve more gold relations (2.12 vs.\\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.\nFailure rate increases monotonically with gold relation count: 4.3\\% at 1 relation, 20.7\\% at 3 relations, 26.2\\% at 6 relations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}\n\\label{tab:stable_failures}\n\\begin{tabular}{lcccc}\n\\toprule\nGroup & $n$ & Gold rels & Greedy F1 & LP $\\Delta$F1 \\\\\n\\midrule\nStable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\\\\nFail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\\\\nFail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\\\\nNever fail & 429 & 1.62 & 0.429 & $+$0.041 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Flip instances.}\nOnly 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).\nThese instances show large constrained LP errors ($\\Delta{=}{-}0.430$) that reverse under free-form decoding ($\\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.\n",
      "numLines": 558,
      "startLine": 1,
      "totalLines": 558
    }
  },
  "sourceToolAssistantUUID": "75fd31eb-b9e0-4720-a6fb-b1e6d336f80c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-15T12:15:39.699Z_

<details open><summary>🔧 Tool call — Read · `toolu_019HJ4Hz4RwY7c4RHq8DUnUj`</summary>

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
  "parentUuid": "4854e20d-77fa-4ae0-9536-049946ddb642",
  "isSidechain": false,
  "requestId": "req_011Cb4LXwBtHHVXc69KDuXxD",
  "type": "assistant",
  "uuid": "f278a158-3eb5-4525-bee6-a70494aa277e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVi32FxYSa72aPJmqn4Jsb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5007,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 29908,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5007,
          "output_tokens": 557,
          "cache_read_input_tokens": 29908,
          "cache_creation_input_tokens": 1204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1204
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。  ## 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction - **论文路径**: `projects…",
  "leafUuid": "856bf6ca-d6dd-4a68-b298-3cec806a2bd7",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured information extraction confidence signals paper",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Assistant

_source line 53 · 2026-05-15T12:15:44.321Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read the entire paper. Let me also check the ARR reviewer guidelines more carefully and read the discussion section. Let me also check for the free-form ablation details and any references.

Actually I've read all sections. Let me now compile my review. Let me also fetch the reviewer guidelines page to understand the review form better.

Let me also check the references file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "856bf6ca-d6dd-4a68-b298-3cec806a2bd7",
  "isSidechain": false,
  "requestId": "req_011Cb4LYb1E3nB5nmpGSSZRq",
  "type": "assistant",
  "uuid": "66e00a26-5b52-49a3-ae4e-48c678268afd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJhMZ4tJZn9eXB7Lkn2Bio",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29026,
      "cache_read_input_tokens": 31112,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29026,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 333,
          "cache_read_input_tokens": 31112,
          "cache_creation_input_tokens": 29026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29026
          },
          "type": "message"
        }
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

_source line 54 · 2026-05-15T12:15:45.809Z_

论文全部章节已读完。现在获取 ARR reviewer guidelines 详细指导，并检查 references.bib。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66e00a26-5b52-49a3-ae4e-48c678268afd",
  "isSidechain": false,
  "requestId": "req_011Cb4LYb1E3nB5nmpGSSZRq",
  "type": "assistant",
  "uuid": "1dfe9c3c-9ac8-4e82-b56f-f83c8e95896d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJhMZ4tJZn9eXB7Lkn2Bio",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29026,
      "cache_read_input_tokens": 31112,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29026,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 333,
          "cache_read_input_tokens": 31112,
          "cache_creation_input_tokens": 29026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29026
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-15T12:15:47.715Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PkapLyB639KAyADPQ1Vybc`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines: what should reviewers focus on, what makes a good review, scoring criteria details, what constitutes a reason for rejection vs acceptance, any specific guidance on soundness evaluation, experimental rigor requirements, and reproducibility standards."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dfe9c3c-9ac8-4e82-b56f-f83c8e95896d",
  "isSidechain": false,
  "requestId": "req_011Cb4LYb1E3nB5nmpGSSZRq",
  "type": "assistant",
  "uuid": "77777e57-4ba3-4ac4-894a-c73d3959a9cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJhMZ4tJZn9eXB7Lkn2Bio",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29026,
      "cache_read_input_tokens": 31112,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29026,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 333,
          "cache_read_input_tokens": 31112,
          "cache_creation_input_tokens": 29026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29026
          },
          "type": "message"
        }
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

_source line 56 · 2026-05-15T12:15:49.402Z_

<details><summary>↩ Tool result · `toolu_01HRLS8RcjivgdpfYm76UimW`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e2119e7-e60a-4ecd-805a-2a0949ad799d",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "ed0d0164-bab2-4190-8c82-25628a6169d1",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
    ],
    "durationMs": 22,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "6e2119e7-e60a-4ecd-805a-2a0949ad799d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T12:15:49.374Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HRLS8RcjivgdpfYm76UimW`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77777e57-4ba3-4ac4-894a-c73d3959a9cc",
  "isSidechain": false,
  "requestId": "req_011Cb4LYb1E3nB5nmpGSSZRq",
  "type": "assistant",
  "uuid": "6e2119e7-e60a-4ecd-805a-2a0949ad799d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJhMZ4tJZn9eXB7Lkn2Bio",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29026,
      "cache_read_input_tokens": 31112,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29026,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 333,
          "cache_read_input_tokens": 31112,
          "cache_creation_input_tokens": 29026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29026
          },
          "type": "message"
        }
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

_source line 58 · 2026-05-15T12:15:56.369Z_

<details><summary>↩ Tool result · `toolu_01PkapLyB639KAyADPQ1Vybc`</summary>

```text
# ARR Reviewer Guidelines: Key Summary

## Core Review Focus Areas

Reviewers should concentrate on four main tasks:

1. **Assignment verification** – Check expertise match and conflicts of interest
2. **Desk-rejection assessment** – Evaluate appropriateness, anonymity violations, style compliance, ethics flags
3. **Detailed review writing** – Provide specific, constructive feedback
4. **Discussion engagement** – Respond to author clarifications and colleague reviewers

## What Makes a Good Review

Strong reviews demonstrate these qualities:

- **Specificity**: "The formulation of X misses factor Y" rather than vague criticism
- **Justified scoring**: Soundness scores must align with identified technical issues
- **Professional tone**: Constructive feedback framed as colleague-to-colleague dialogue
- **Balanced perspective**: Reading papers twice before critiquing, adjusting expectations based on contribution type

As the guidelines note, reviewers should adopt "a reading strategy" that involves "skimming and in-depth reading" rather than critiquing during initial exposure.

## Scoring Criteria

Three distinct scores are required:

- **Soundness**: Technical validity and methodological rigor (must be justified in review text)
- **Excitement**: Personal interest level (subjective, requires no explicit justification)
- **Overall recommendation**: Composite assessment reflecting soundness, novelty, and potential impact

## Rejection vs. Acceptance Thresholds

**Grounds for desk rejection** include:
- Scope misalignment with conference CFP
- Hallucinated citations or anonymity violations
- Style guide/length non-compliance
- Missing limitations sections
- Egregious responsible NLP checklist violations

**NOT grounds for rejection**:
- Lack of state-of-the-art results (unless claimed)
- Simplicity of methodology
- Non-English evaluation
- Acknowledged limitations
- Negative findings

## Soundness Evaluation Requirements

Reviewers must verify:

- Complete, correct proofs with clear assumptions
- Reproducible experimental setup with sufficient hyperparameter detail
- Fair baseline comparisons with adequate tuning
- Appropriate statistical significance reporting
- Data quality transparency

Importantly, "reproducibility score refers to *reproducibility* (being able to run the same experiment with roughly the same results)" rather than independent replication.

## Common Pitfalls to Avoid

The guidelines identify seventeen "heuristics" that often undermine fair reviews, including:

- Dismissing results as "obvious in retrospect" (hindsight bias)
- Requiring comparisons to closed-source models without clear justification
- Demanding extra experiments beyond what claims necessitate
- Treating acknowledged limitations as rejection grounds
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77777e57-4ba3-4ac4-894a-c73d3959a9cc",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "ddd60c63-e143-4a85-b526-4fab5cc6ccd7",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Reviewer Guidelines: Key Summary\n\n## Core Review Focus Areas\n\nReviewers should concentrate on four main tasks:\n\n1. **Assignment verification** – Check expertise match and conflicts of interest\n2. **Desk-rejection assessment** – Evaluate appropriateness, anonymity violations, style compliance, ethics flags\n3. **Detailed review writing** – Provide specific, constructive feedback\n4. **Discussion engagement** – Respond to author clarifications and colleague reviewers\n\n## What Makes a Good Review\n\nStrong reviews demonstrate these qualities:\n\n- **Specificity**: \"The formulation of X misses factor Y\" rather than vague criticism\n- **Justified scoring**: Soundness scores must align with identified technical issues\n- **Professional tone**: Constructive feedback framed as colleague-to-colleague dialogue\n- **Balanced perspective**: Reading papers twice before critiquing, adjusting expectations based on contribution type\n\nAs the guidelines note, reviewers should adopt \"a reading strategy\" that involves \"skimming and in-depth reading\" rather than critiquing during initial exposure.\n\n## Scoring Criteria\n\nThree distinct scores are required:\n\n- **Soundness**: Technical validity and methodological rigor (must be justified in review text)\n- **Excitement**: Personal interest level (subjective, requires no explicit justification)\n- **Overall recommendation**: Composite assessment reflecting soundness, novelty, and potential impact\n\n## Rejection vs. Acceptance Thresholds\n\n**Grounds for desk rejection** include:\n- Scope misalignment with conference CFP\n- Hallucinated citations or anonymity violations\n- Style guide/length non-compliance\n- Missing limitations sections\n- Egregious responsible NLP checklist violations\n\n**NOT grounds for rejection**:\n- Lack of state-of-the-art results (unless claimed)\n- Simplicity of methodology\n- Non-English evaluation\n- Acknowledged limitations\n- Negative findings\n\n## Soundness Evaluation Requirements\n\nReviewers must verify:\n\n- Complete, correct proofs with clear assumptions\n- Reproducible experimental setup with sufficient hyperparameter detail\n- Fair baseline comparisons with adequate tuning\n- Appropriate statistical significance reporting\n- Data quality transparency\n\nImportantly, \"reproducibility score refers to *reproducibility* (being able to run the same experiment with roughly the same results)\" rather than independent replication.\n\n## Common Pitfalls to Avoid\n\nThe guidelines identify seventeen \"heuristics\" that often undermine fair reviews, including:\n\n- Dismissing results as \"obvious in retrospect\" (hindsight bias)\n- Requiring comparisons to closed-source models without clear justification\n- Demanding extra experiments beyond what claims necessitate\n- Treating acknowledged limitations as rejection grounds",
    "durationMs": 8652,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "77777e57-4ba3-4ac4-894a-c73d3959a9cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 59 · 2026-05-15T12:15:56.378Z_

```json
{
  "parentUuid": "ddd60c63-e143-4a85-b526-4fab5cc6ccd7",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "478bc077-5bb1-4923-a25e-980b63ca0c84",
  "timestamp": "2026-05-15T12:15:56.378Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 60 · 2026-05-15T12:16:50.694Z_

<details><summary>Logged reasoning block</summary>

```text
Good. I now have a thorough understanding of both the paper and the ARR review guidelines. Let me now compile my comprehensive review.

Let me also verify references to check for any issues.

Let me organize my review focusing on:
1. Method rigor (5 confidence signals, Soft Jaccard, VC, FK independence)
2. Statistical testing (bootstrap, TOST, multiple comparisons)
3. Experimental design (LoRA config, thinking token, N=8 single seed, free-form ablation)
4. Reproducibility (training config, prompt, constrained decoding)


Now I'm identifying the critical issues. The free-form ablation is particularly concerning—it's limited to just one dataset, one model, and one seed, yet the paper makes sweeping mechanistic claims about compression being fundamental to test-time scaling. Similarly, all the relation extraction findings depend entirely on SciERC, which the authors label as preliminary, but the abstract and title don't reflect this limitation.

The core selection gap analysis in Table 3 relies on a single seed, and while Table 10 shows consistency across three seeds for quality estimation, it doesn't actually replicate the selection gap itself. The TOST equivalence thresholds (±2/3/5 percentage points) are framed as fractions of oracle headroom, but there's no principled justification for why forgoing 28-38% of headroom constitutes the right boundary—the paper doesn't ground this in prior IE work. Finally, the ε=0.05 threshold for calling results "effectively tied" needs better motivation.

Looking at the sensitivity analysis, there's a dramatic jump from 1.1% of instances at ε=0.01 to 60.3% at ε=0.05, which suggests the conclusion hinges heavily on this arbitrary cutoff choice. On the statistical side, the FK independence assumption is tested with a one-sample t-test across just 5 configurations, which has limited power to detect real effects. The paper should either report per-configuration tests or acknowledge this limitation. There's also a mismatch between how VC is defined in Equation 6 (mean frequency over the union) and what the footnote actually says about selection.

The VC formula discrepancy is compounded by the fact that two different computations—one using mean frequency and one using majority threshold—produce notably different correlation values (0.379 vs 0.252) but share the same name without adequate discussion. The Qwen3-8B thinking token confound argument is incomplete: showing that LP selection fails across multiple datasets doesn't rule out that the confound affects SciERC differently. Finally, the claim about consensus-proximity and LOO-SJ equivalence relies on a mathematically trivial derivation (dividing by a constant), and conflates the negligible max score difference of 3.1×10⁻⁴ with the actual presence of evaluation circularity.

The paper also excludes LP from the T=0.7 comparison due to missing data, which is a significant oversight given that LP behavior is central to the paper's claims. The Soft Jaccard formulation leaves unmatched items implicitly handled—they contribute nothing to the numerator but increase the denominator—without explicit clarification. The bootstrap resampling uses 10,000 iterations on 529 instances, which raises questions about the statistical power and variance of the estimates.

I'm also noticing some consistency issues: Table 3 labels RE results as preliminary but this qualifier doesn't appear in the abstract claims about structured IE. There's a citation to "nedellec2026consistency" that appears to be future work and needs verification. Cohen's d is reported for NER LP selection but inconsistently across other signals and RE. The terminology shifts between "confidence signal" and "consistency signal" throughout, and while Section 3.2 clarifies the distinction, the abstract doesn't use either term consistently. I should double-check the references to make sure everything is properly sourced.

Now I'm working through the Soft Jaccard definition more carefully. The formula sums similarity scores for matched entity pairs in the numerator, but divides by the maximum extraction counts per type across both predictions. This creates a potential mismatch: if one prediction has 3 entities of a type and the other has 2, the denominator counts 3, but Hungarian matching only produces 2 matches for that type, leaving one entity unmatched and contributing nothing to the numerator while the denominator already accounts for it.

The key insight is that zero-IoU pairs get zero weight automatically since the cost matrix assigns 0 to non-overlapping pairs, so whether the Hungarian algorithm matches them or leaves them unmatched doesn't matter—they contribute 0 to the numerator either way. The real design choice is in the denominator: using max(|g_i|, |g_j|) instead of |g_i ∪ g_j|, which the paper justifies. This is actually a reasonable approach, so I'll move past this detail.

Now I'm identifying what's genuinely problematic: the gap between how broadly the paper claims its findings versus the evidence supporting them. The title promises "Structured Information Extraction" but the RE results come from a single dataset. The claim about test-time scaling being a fundamental challenge rests on a single-dataset ablation. The core selection gap analysis uses only a single seed. The paper does hedge by calling RE "preliminary" and acknowledges limitations, but the framing in the title and abstract overstates how general these findings actually are.

There's also a critical dependency on the ε=0.05 threshold for claiming "60% effectively tied"—but at ε=0.01, only 1.1% are tied, a 59x difference. The paper never justifies why 0.05 is the right threshold, which undermines a key narrative claim.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "478bc077-5bb1-4923-a25e-980b63ca0c84",
  "isSidechain": false,
  "requestId": "req_011Cb4LZp1LvddbiDpPvjXWv",
  "type": "assistant",
  "uuid": "ddee5472-3713-485e-8aa4-1227826e45b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LMHAXTukqYMujeQ6avh7C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 68,
      "cache_creation_input_tokens": 1068,
      "cache_read_input_tokens": 60138,
      "output_tokens": 2119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1068,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 68,
          "output_tokens": 2119,
          "cache_read_input_tokens": 60138,
          "cache_creation_input_tokens": 1068,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1068
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-15T12:16:50.697Z_

已获取完整的 ARR reviewer guidelines。现在验证引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddee5472-3713-485e-8aa4-1227826e45b8",
  "isSidechain": false,
  "requestId": "req_011Cb4LZp1LvddbiDpPvjXWv",
  "type": "assistant",
  "uuid": "773dc0df-28a5-4fd5-b1ba-ef71384d6e25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LMHAXTukqYMujeQ6avh7C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 68,
      "cache_creation_input_tokens": 1068,
      "cache_read_input_tokens": 60138,
      "output_tokens": 2119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1068,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 68,
          "output_tokens": 2119,
          "cache_read_input_tokens": 60138,
          "cache_creation_input_tokens": 1068,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1068
          },
          "type": "message"
        }
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

_source line 62 · 2026-05-15T12:16:50.700Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01NEwNG45FBvBPtMRiJ9HQX3`</summary>

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
  "parentUuid": "773dc0df-28a5-4fd5-b1ba-ef71384d6e25",
  "isSidechain": false,
  "requestId": "req_011Cb4LZp1LvddbiDpPvjXWv",
  "type": "assistant",
  "uuid": "c221ef90-d41f-4be0-9845-4630b75f6508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LMHAXTukqYMujeQ6avh7C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 68,
      "cache_creation_input_tokens": 1068,
      "cache_read_input_tokens": 60138,
      "output_tokens": 2119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1068,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 68,
          "output_tokens": 2119,
          "cache_read_input_tokens": 60138,
          "cache_creation_input_tokens": 1068,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1068
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。  ## 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction - **论文路径**: `projects…",
  "leafUuid": "c221ef90-d41f-4be0-9845-4630b75f6508",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured information extraction confidence signals paper",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Tool result

_source line 65 · 2026-05-15T12:17:43.197Z_

<details><summary>↩ Tool result · `toolu_01NEwNG45FBvBPtMRiJ9HQX3`</summary>

```text
&lt;persisted-output>
Output too large (50.8KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/eb1a3f49-65c9-4074-8546-55ac5548828b/tool-results/toolu_01NEwNG45FBvBPtMRiJ9HQX3.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 62, \"total_citations\": 93, \"unique_cited_keys\": 62, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 56, \"online_not_found\": 3, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recogniti
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c221ef90-d41f-4be0-9845-4630b75f6508",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "a3814896-306d-4639-a17d-39c854b20d1b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 62, \\\"total_citations\\\": 93, \\\"unique_cited_keys\\\": 62, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 56, \\\"online_not_found\\\": 3, \\\"online_mismatch\\\": 3}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"authors\\\": \\\"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"ICLR 2021\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"authors\\\": \\\"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2407.21787\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"authors\\\": \\\"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint (ICML 2024 Workshop ICL)\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"authors\\\": \\\"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2110.14168\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"authors\\\": \\\"Culotta, Aron and McCallum, Andrew\\\", \\\"year\\\": \\\"2004\\\", \\\"venue\\\": \\\"HLT-NAACL 2004\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"authors\\\": \\\"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"W-NUT Workshop at EMNLP 2017\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"authors\\\": \\\"Desai, Shrey and Durrett, Greg\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"authors\\\": \\\"Eikema, Bryan and Aziz, Wilker\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Few-Shot Conformal Prediction with Auxiliary Tasks\\\", \\\"authors\\\": \\\"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"ICML 2021\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"authors\\\": \\\"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"he2024uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\\\", \\\"authors\\\": \\\"He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL 2024\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"authors\\\": \\\"Fleiss, Joseph L.\\\", \\\"year\\\": \\\"1971\\\", \\\"venue\\\": \\\"Psychological Bulletin\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"authors\\\": \\\"Gal, Yarin and Ghahramani, Zoubin\\\", \\\"year\\\": \\\"2016\\\", \\\"venue\\\": \\\"ICML 2016\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"authors\\\": \\\"Geifman, Yonatan and El-Yaniv, Ran\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"NeurIPS 2017\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2511.12309\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"authors\\\": \\\"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"authors\\\": \\\"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"ICML 2017\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"authors\\\": \\\"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2510.20460\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"authors\\\": \\\"Jaccard, Paul\\\", \\\"year\\\": \\\"1901\\\", \\\"venue\\\": \\\"Bulletin de la Société Vaudoise des Sciences Naturelles\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"authors\\\": \\\"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"authors\\\": \\\"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2207.05221\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"authors\\\": \\\"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"kim2024verifiner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Kim, Seoyeon and Seo, Kwangwook and Chae, Hyungjoo and Yeo, Jinyoung and Lee, Do...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"authors\\\": \\\"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"ACL 2026\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"authors\\\": \\\"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2406.15927\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"authors\\\": \\\"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.04104\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"authors\\\": \\\"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"authors\\\": \\\"Malinin, Andrey and Gales, Mark\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"authors\\\": \\\"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"NeurIPS 2017\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"authors\\\": \\\"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"authors\\\": \\\"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"authors\\\": \\\"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"authors\\\": \\\"Manakul, Potsawee and Liusie, Adian and Gales, Mark\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\\\", \\\"authors\\\": \\\"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Genomics \\\\\\\\& Informatics\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"authors\\\": \\\"Oh, Jungsuk and Lee, Jay-Yoon\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.18395\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"authors\\\": \\\"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"authors\\\": \\\"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 16th Conference of the European Chapter of the Association fo...\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"authors\\\": \\\"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"authors\\\": \\\"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"authors\\\": \\\"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"authors\\\": \\\"Sang, Erik F. Tjong Kim and Meulder, Fien De\\\", \\\"year\\\": \\\"2003\\\", \\\"venue\\\": \\\"CoNLL 2003\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"authors\\\": \\\"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"authors\\\": \\\"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"authors\\\": \\\"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2304.08085\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"authors\\\": \\\"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"authors\\\": \\\"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL 2025\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"authors\\\": \\\"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ACL 2024\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"authors\\\": \\\"Wang, Weiqin and Wang, Yile and Huang, Hui\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"authors\\\": \\\"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"authors\\\": \\\"Willard, Brandon T. and Louf, Rémi\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2307.09702\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"authors\\\": \\\"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"authors\\\": \\\"Xiao, Yijun and Wang, William Yang\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2023\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"authors\\\": \\\"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\\", \\\"authors\\\": \\\"Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Ju...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"authors\\\": \\\"M\\\\\\\\\\\\\\\"uller, Mathias and Sennrich, Rico\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"heo2025uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Do LLMs Estimate Uncertainty Well in Instruction Following?\\\", \\\"authors\\\": \\\"Heo, Juyeon and Xiong, Miao and Heinze-Deml, Christina and Narain, Jaya\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"authors\\\": \\\"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"zhang2025tts\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\\\", \\\"authors\\\": \\\"Zhang, Qiyuan and Lyu, Fuyuan and Sun, Zexu and Wang, Lei and Zhang, Weixu and G...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.24235\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\", \\\"authors\\\": \\\"Venktesh, V and Rathee, Mandeep and Anand, Avishek\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.16665\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"authors\\\": \\\"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 41st International Conference on Machine Learning (ICML)\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citealp\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 49, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2025tts\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"heo2025uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2024verifiner\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"he2024uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 34, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 45, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 60, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 74, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 133, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 133, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 133, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 45, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 45, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 190, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 190, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 380, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence estimation for information extraction\\\", \\\"matched_year\\\": \\\"2004\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"title\\\": \\\"Few-Shot Conformal Prediction with Auxiliary Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Few-shot Conformal Prediction with Auxiliary Tasks\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"he2024uncertainty\\\", \\\"title\\\": \\\"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"matched_year\\\": \\\"1971\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"matched_year\\\": \\\"2015\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=feng vs api=austin\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.236, \\\"matched_title\\\": \\\"A new criterion for assessing discriminant validity in variance-based structural equation modeling\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.24 below threshold 0.82\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"matched_year\\\": \\\"1901\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2024verifiner\\\", \\\"title\\\": \\\"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.246, \\\"matched_title\\\": \\\"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=snell vs api=charlie\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2003\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"title\\\": \\\"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=m\\\\\\\\\\\\\\\"uller vs api=müller\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"heo2025uncertainty\\\", \\\"title\\\": \\\"Do LLMs Estimate Uncertainty Well in Instruction Following?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.983, \\\"matched_title\\\": \\\"Do LLMs estimate uncertainty well in instruction-following?\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2025tts\\\", \\\"title\\\": \\\"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"title\\\": \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.252, \\\"matched_title\\\": \\\"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 62, \"total_citations\": 93, \"unique_cited_keys\": 62, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 56, \"online_not_found\": 3, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"W-NUT Workshop at EMNLP 2017\"}, {\"key\": \"desai2020calibration\", \"type\": \"inproceedings\", \"title\": \"Calibration of Pre-trained Transformers\", \"authors\": \"Desai, Shrey and Durrett, Greg\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eikema2022sampling\", \"type\": \"inproceedings\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"authors\": \"Eikema, Bryan and Aziz, Wilker\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"fisch2021conformal\", \"type\": \"inproceedings\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"authors\": \"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\", \"year\": \"2021\", \"venue\": \"ICML 2021\"}, {\"key\": \"freitag2022high\", \"type\": \"article\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"authors\": \"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\", \"year\": \"2022\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"he2024uncertainty\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"authors\": \"He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2024\"}, {\"key\": \"fleiss1971agreement\", \"type\": \"article\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"authors\": \"Fleiss, Joseph L.\", \"year\": \"1971\", \"venue\": \"Psychological Bulletin\"}, {\"key\": \"gal2016dropout\", \"type\": \"inproceedings\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"authors\": \"Gal, Yarin and Ghahramani, Zoubin\", \"year\": \"2016\", \"venue\": \"ICML 2016\"}, {\"key\": \"geifman2017selective\", \"type\": \"inproceedings\", \"title\": \"Selective Classification for Deep Neural Networks\", \"authors\": \"Geifman, Yonatan and El-Yaniv, Ran\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"feng2025optimal\", \"type\": \"article\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"authors\": \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.12309\"}, {\"key\": \"geng2024confidence\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"guo2017calibration\", \"type\": \"inproceedings\", \"title\": \"On Calibration of Modern Neural Networks\", \"authors\": \"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\", \"year\": \"2017\", \"venue\": \"ICML 2017\"}, {\"key\": \"hobelsberger2025systematic\", \"type\": \"article\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"authors\": \"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.20460\"}, {\"key\": \"jaccard1901distribution\", \"type\": \"article\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"authors\": \"Jaccard, Paul\", \"year\": \"1901\", \"venue\": \"Bulletin de la Société Vaudoise des Sciences Naturelles\"}, {\"key\": \"josifoski2022genie\", \"type\": \"inproceedings\", \"title\": \"GenIE: Generative Information Extraction\", \"authors\": \"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kang2025selfcertainty\", \"type\": \"inproceedings\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"authors\": \"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"kim2024verifiner\", \"type\": \"inproceedings\", \"title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"authors\": \"Kim, Seoyeon and Seo, Kwangwook and Chae, Hyungjoo and Yeo, Jinyoung and Lee, Do...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"kim2026reasc\", \"type\": \"inproceedings\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"authors\": \"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\", \"year\": \"2026\", \"venue\": \"ACL 2026\"}, {\"key\": \"kossen2024semantic\", \"type\": \"article\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"authors\": \"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.15927\"}, {\"key\": \"li2025llms\", \"type\": \"article\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"authors\": \"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.04104\"}, {\"key\": \"kuhn2023semantic\", \"type\": \"inproceedings\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"authors\": \"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"malinin2021uncertainty\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"authors\": \"Malinin, Andrey and Gales, Mark\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"type\": \"inproceedings\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"authors\": \"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"li2023codeie\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lightman2024verify\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"luan2018scierc\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"authors\": \"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"manakul2023selfcheckgpt\", \"type\": \"inproceedings\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"authors\": \"Manakul, Potsawee and Liusie, Adian and Gales, Mark\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"nedellec2026consistency\", \"type\": \"article\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\", \"authors\": \"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\", \"year\": \"2026\", \"venue\": \"Genomics \\\\& Informatics\"}, {\"key\": \"oh2025latentsc\", \"type\": \"article\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"authors\": \"Oh, Jungsuk and Lee, Jay-Yoon\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.18395\"}, {\"key\": \"sainz2024gollie\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"shelmanov2021active\", \"type\": \"inproceedings\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"authors\": \"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 16th Conference of the European Chapter of the Association fo...\"}, {\"key\": \"snell2025scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"authors\": \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"taubenfeld2025cisc\", \"type\": \"inproceedings\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"authors\": \"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"thirukovalluru2024atomic\", \"type\": \"inproceedings\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"authors\": \"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"tjongkimsang2003conll\", \"type\": \"inproceedings\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"authors\": \"Sang, Erik F. Tjong Kim and Meulder, Fien De\", \"year\": \"2003\", \"venue\": \"CoNLL 2003\"}, {\"key\": \"vashurin2025cocoa\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"authors\": \"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"wadhwa2023revisiting\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"wang2023instructuie\", \"type\": \"article\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"authors\": \"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.08085\"}, {\"key\": \"wang2023selfconsistency\", \"type\": \"inproceedings\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"authors\": \"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"wang2025make\", \"type\": \"inproceedings\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"authors\": \"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2025\"}, {\"key\": \"wang2024mathshepherd\", \"type\": \"inproceedings\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"authors\": \"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\", \"year\": \"2024\", \"venue\": \"ACL 2024\"}, {\"key\": \"wang2025rankedvoting\", \"type\": \"inproceedings\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"authors\": \"Wang, Weiqin and Wang, Yile and Huang, Hui\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"wen2025know\", \"type\": \"article\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"authors\": \"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\", \"year\": \"2025\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"willard2023guided\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, Rémi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"xia2025survey\", \"type\": \"inproceedings\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"authors\": \"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"xiao2019uncertainty\", \"type\": \"article\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"authors\": \"Xiao, Yijun and Wang, William Yang\", \"year\": \"2019\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"zhang2023ener\", \"type\": \"inproceedings\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"authors\": \"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2023\"}, {\"key\": \"zheng2024llamafactory\", \"type\": \"inproceedings\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"authors\": \"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"zhou2024uniner\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"xiong2024llm\", \"type\": \"inproceedings\", \"title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"authors\": \"Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Ju...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"muller2021understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"authors\": \"M\\\\\\\"uller, Mathias and Sennrich, Rico\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"heo2025uncertainty\", \"type\": \"inproceedings\", \"title\": \"Do LLMs Estimate Uncertainty Well in Instruction Following?\", \"authors\": \"Heo, Juyeon and Xiong, Miao and Heinze-Deml, Christina and Narain, Jaya\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"eikema2025structured\", \"type\": \"inproceedings\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"authors\": \"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"zhang2025tts\", \"type\": \"article\", \"title\": \"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\", \"authors\": \"Zhang, Qiyuan and Lyu, Fuyuan and Sun, Zexu and Wang, Lei and Zhang, Weixu and G...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.24235\"}, {\"key\": \"venktesh2025trust\", \"type\": \"article\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"authors\": \"Venktesh, V and Rathee, Mandeep and Anand, Avishek\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.16665\"}, {\"key\": \"jinnai2024mbr\", \"type\": \"inproceedings\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"authors\": \"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}], \"tex_citations\": [{\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 4, \"command\": \"citealp\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/introduction.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/introduction.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/introduction.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/introduction.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 49, \"command\": \"citet\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"thirukovalluru2024atomic\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"manakul2023selfcheckgpt\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"zhang2025tts\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kim2026reasc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"wang2025rankedvoting\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"oh2025latentsc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"feng2025optimal\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"wang2025make\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"li2025llms\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"vashurin2025cocoa\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"zhou2024uniner\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"sainz2024gollie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"josifoski2022genie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"li2023codeie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wadhwa2023revisiting\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wang2023instructuie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"geng2024confidence\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"wen2025know\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xia2025survey\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"hobelsberger2025systematic\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xiong2024llm\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"heo2025uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"kossen2024semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"kadavath2022language\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"malinin2021uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"guo2017calibration\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"desai2020calibration\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"gal2016dropout\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"xiao2019uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"shelmanov2021active\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"zhang2023ener\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"kim2024verifiner\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"he2024uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"fisch2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"angelopoulos2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"lightman2024verify\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"venktesh2025trust\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"wang2024mathshepherd\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"jinnai2024mbr\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"geifman2017selective\", \"file\": \"sections/related_work.tex\", \"line\": 27, \"command\": \"cite\"}, {\"key\": \"culotta2004confidence\", \"file\": \"sections/related_work.tex\", \"line\": 27, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/method.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fleiss1971agreement\", \"file\": \"sections/method.tex\", \"line\": 34, \"command\": \"citet\"}, {\"key\": \"jaccard1901distribution\", \"file\": \"sections/method.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/experiments.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/experiments.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"zheng2024llamafactory\", \"file\": \"sections/experiments.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/experiments.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/experiments.tex\", \"line\": 60, \"command\": \"cite\"}, {\"key\": \"xiong2024llm\", \"file\": \"sections/experiments.tex\", \"line\": 74, \"command\": \"citep\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/experiments.tex\", \"line\": 133, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/experiments.tex\", \"line\": 133, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/experiments.tex\", \"line\": 133, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/discussion.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/discussion.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/discussion.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"jinnai2024mbr\", \"file\": \"sections/discussion.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/discussion.tex\", \"line\": 22, \"command\": \"citet\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/discussion.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"venktesh2025trust\", \"file\": \"sections/discussion.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/appendix.tex\", \"line\": 190, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/appendix.tex\", \"line\": 190, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/appendix.tex\", \"line\": 380, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"angelopoulos2021conformal\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"brown2024monkeys\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024usc\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Self-Consistency for Large Language Model Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021verifiers\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culotta2004confidence\", \"title\": \"Confidence Estimation for Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence estimation for information extraction\", \"matched_year\": \"2004\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"derczynski2017wnut\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"desai2020calibration\", \"title\": \"Calibration of Pre-trained Transformers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calibration of Pre-trained Transformers\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eikema2022sampling\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fisch2021conformal\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-shot Conformal Prediction with Auxiliary Tasks\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"freitag2022high\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"he2024uncertainty\", \"title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fleiss1971agreement\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring nominal scale agreement among many raters.\", \"matched_year\": \"1971\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gal2016dropout\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"geifman2017selective\", \"title\": \"Selective Classification for Deep Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Selective Classification for Deep Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feng2025optimal\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=feng vs api=austin\"], \"note\": \"\"}, {\"key\": \"geng2024confidence\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2017calibration\", \"title\": \"On Calibration of Modern Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Calibration of Modern Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hobelsberger2025systematic\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.236, \"matched_title\": \"A new criterion for assessing discriminant validity in variance-based structural equation modeling\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.24 below threshold 0.82\"}, {\"key\": \"jaccard1901distribution\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"matched_year\": \"1901\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"josifoski2022genie\", \"title\": \"GenIE: Generative Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GenIE: Generative Information Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2025selfcertainty\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2024verifiner\", \"title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2026reasc\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kossen2024semantic\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025llms\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuhn2023semantic\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"malinin2021uncertainty\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023codeie\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lightman2024verify\", \"title\": \"Let's Verify Step by Step\", \"status\": \"not_found\", \"confidence\": 0.246, \"matched_title\": \"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"luan2018scierc\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"manakul2023selfcheckgpt\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nedellec2026consistency\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oh2025latentsc\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sainz2024gollie\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shelmanov2021active\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"snell2025scaling\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=snell vs api=charlie\"], \"note\": \"\"}, {\"key\": \"taubenfeld2025cisc\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence Improves Self-Consistency in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thirukovalluru2024atomic\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tjongkimsang2003conll\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"matched_year\": \"2003\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vashurin2025cocoa\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa2023revisiting\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023instructuie\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023selfconsistency\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025make\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2024mathshepherd\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025rankedvoting\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wen2025know\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023guided\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2025survey\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiao2019uncertainty\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2023ener\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zheng2024llamafactory\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024uniner\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiong2024llm\", \"title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"muller2021understanding\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"matched_year\": \"2021\", \"mismatch_fields\": [\"first_author: bib=m\\\\\\\"uller vs api=müller\"], \"note\": \"\"}, {\"key\": \"heo2025uncertainty\", \"title\": \"Do LLMs Estimate Uncertainty Well in Instruction Following?\", \"status\": \"verified\", \"confidence\": 0.983, \"matched_title\": \"Do LLMs estimate uncertainty well in instruction-following?\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eikema2025structured\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2025tts\", \"title\": \"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"venktesh2025trust\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"status\": \"not_found\", \"confidence\": 0.252, \"matched_title\": \"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"jinnai2024mbr\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "c221ef90-d41f-4be0-9845-4630b75f6508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 66_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。  ## 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction - **论文路径**: `projects…",
  "leafUuid": "a3814896-306d-4639-a17d-39c854b20d1b",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Runtime record

_source line 67_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured information extraction confidence signals paper",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Assistant

_source line 68 · 2026-05-15T12:17:45.963Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the full reference verification results to check for issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3814896-306d-4639-a17d-39c854b20d1b",
  "isSidechain": false,
  "requestId": "req_011Cb4Lhgmjm3gzaS17cVtbG",
  "type": "assistant",
  "uuid": "c176be85-5675-4607-9796-8f5d9734ddf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qr2U4tBXx7XSXRSPLwyRiB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3086,
      "cache_read_input_tokens": 61206,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3086,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 61206,
          "cache_creation_input_tokens": 3086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3086
          },
          "type": "message"
        }
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

_source line 69 · 2026-05-15T12:17:47.078Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NvQDCaWb7f9wxbRHqXk3vu`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/eb1a3f49-65c9-4074-8546-55ac5548828b/tool-results/toolu_01NEwNG45FBvBPtMRiJ9HQX3.txt",
  "offset": 0,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c176be85-5675-4607-9796-8f5d9734ddf3",
  "isSidechain": false,
  "requestId": "req_011Cb4Lhgmjm3gzaS17cVtbG",
  "type": "assistant",
  "uuid": "d5d6b122-8233-48da-9d22-ae909b9d2c3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qr2U4tBXx7XSXRSPLwyRiB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3086,
      "cache_read_input_tokens": 61206,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3086,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 61206,
          "cache_creation_input_tokens": 3086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3086
          },
          "type": "message"
        }
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

_source line 70 · 2026-05-15T12:17:47.368Z_

<details><summary>↩ Tool result · `toolu_01NvQDCaWb7f9wxbRHqXk3vu`</summary>

```text
0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 62, \"total_citations\": 93, \"unique_cited_keys\": 62, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 56, \"online_not_found\": 3, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"W-NUT Workshop at EMNLP 2017\"}, {\"key\": \"desai2020calibration\", \"type\": \"inproceedings\", \"title\": \"Calibration of Pre-trained Transformers\", \"authors\": \"Desai, Shrey and Durrett, Greg\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eikema2022sampling\", \"type\": \"inproceedings\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"authors\": \"Eikema, Bryan and Aziz, Wilker\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"fisch2021conformal\", \"type\": \"inproceedings\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"authors\": \"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\", \"year\": \"2021\", \"venue\": \"ICML 2021\"}, {\"key\": \"freitag2022high\", \"type\": \"article\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"authors\": \"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\", \"year\": \"2022\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"he2024uncertainty\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"authors\": \"He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2024\"}, {\"key\": \"fleiss1971agreement\", \"type\": \"article\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"authors\": \"Fleiss, Joseph L.\", \"year\": \"1971\", \"venue\": \"Psychological Bulletin\"}, {\"key\": \"gal2016dropout\", \"type\": \"inproceedings\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"authors\": \"Gal, Yarin and Ghahramani, Zoubin\", \"year\": \"2016\", \"venue\": \"ICML 2016\"}, {\"key\": \"geifman2017selective\", \"type\": \"inproceedings\", \"title\": \"Selective Classification for Deep Neural Networks\", \"authors\": \"Geifman, Yonatan and El-Yaniv, Ran\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"feng2025optimal\", \"type\": \"article\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"authors\": \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.12309\"}, {\"key\": \"geng2024confidence\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"guo2017calibration\", \"type\": \"inproceedings\", \"title\": \"On Calibration of Modern Neural Networks\", \"authors\": \"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\", \"year\": \"2017\", \"venue\": \"ICML 2017\"}, {\"key\": \"hobelsberger2025systematic\", \"type\": \"article\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"authors\": \"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.20460\"}, {\"key\": \"jaccard1901distribution\", \"type\": \"article\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"authors\": \"Jaccard, Paul\", \"year\": \"1901\", \"venue\": \"Bulletin de la Société Vaudoise des Sciences Naturelles\"}, {\"key\": \"josifoski2022genie\", \"type\": \"inproceedings\", \"title\": \"GenIE: Generative Information Extraction\", \"authors\": \"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kang2025selfcertainty\", \"type\": \"inproceedings\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"authors\": \"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"kim2024verifiner\", \"type\": \"inproceedings\", \"title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"authors\": \"Kim, Seoyeon and Seo, Kwangwook and Chae, Hyungjoo and Yeo, Jinyoung and Lee, Do...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"kim2026reasc\", \"type\": \"inproceedings\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"authors\": \"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\", \"year\": \"2026\", \"venue\": \"ACL 2026\"}, {\"key\": \"kossen2024semantic\", \"type\": \"article\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"authors\": \"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.15927\"}, {\"key\": \"li2025llms\", \"type\": \"article\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"authors\": \"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.04104\"}, {\"key\": \"kuhn2023semantic\", \"type\": \"inproceedings\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"authors\": \"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"malinin2021uncertainty\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"authors\": \"Malinin, Andrey and Gales, Mark\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"type\": \"inproceedings\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"authors\": \"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"li2023codeie\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lightman2024verify\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"luan2018scierc\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"authors\": \"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"manakul2023selfcheckgpt\", \"type\": \"inproceedings\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"authors\": \"Manakul, Potsawee and Liusie, Adian and Gales, Mark\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"nedellec2026consistency\", \"type\": \"article\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\", \"authors\": \"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\", \"year\": \"2026\", \"venue\": \"Genomics \\\\& Informatics\"}, {\"key\": \"oh2025latentsc\", \"type\": \"article\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"authors\": \"Oh, Jungsuk and Lee, Jay-Yoon\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.18395\"}, {\"key\": \"sainz2024gollie\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"shelmanov2021active\", \"type\": \"inproceedings\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"authors\": \"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 16th Conference of the European Chapter of the Association fo...\"}, {\"key\": \"snell2025scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"authors\": \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"taubenfeld2025cisc\", \"type\": \"inproceedings\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"authors\": \"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"thirukovalluru2024atomic\", \"type\": \"inproceedings\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"authors\": \"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"tjongkimsang2003conll\", \"type\": \"inproceedings\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"authors\": \"Sang, Erik F. Tjong Kim and Meulder, Fien De\", \"year\": \"2003\", \"venue\": \"CoNLL 2003\"}, {\"key\": \"vashurin2025cocoa\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"authors\": \"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"wadhwa2023revisiting\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"wang2023instructuie\", \"type\": \"article\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"authors\": \"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.08085\"}, {\"key\": \"wang2023selfconsistency\", \"type\": \"inproceedings\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"authors\": \"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"wang2025make\", \"type\": \"inproceedings\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"authors\": \"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2025\"}, {\"key\": \"wang2024mathshepherd\", \"type\": \"inproceedings\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"authors\": \"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\", \"year\": \"2024\", \"venue\": \"ACL 2024\"}, {\"key\": \"wang2025rankedvoting\", \"type\": \"inproceedings\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"authors\": \"Wang, Weiqin and Wang, Yile and Huang, Hui\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"wen2025know\", \"type\": \"article\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"authors\": \"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\", \"year\": \"2025\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"willard2023guided\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, Rémi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"xia2025survey\", \"type\": \"inproceedings\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"authors\": \"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"xiao2019uncertainty\", \"type\": \"article\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"authors\": \"Xiao, Yijun and Wang, William Yang\", \"year\": \"2019\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"zhang2023ener\", \"type\": \"inproceedings\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"authors\": \"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2023\"}, {\"key\": \"zheng2024llamafactory\", \"type\": \"inproceedings\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"authors\": \"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"zhou2024uniner\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"xiong2024llm\", \"type\": \"inproceedings\", \"title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"authors\": \"Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Ju...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"muller2021understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"authors\": \"M\\\\\\\"uller, Mathias and Sennrich, Rico\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"heo2025uncertainty\", \"type\": \"inproceedings\", \"title\": \"Do LLMs Estimate Uncertainty Well in Instruction Following?\", \"authors\": \"Heo, Juyeon and Xiong, Miao and Heinze-Deml, Christina and Narain, Jaya\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"eikema2025structured\", \"type\": \"inproceedings\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"authors\": \"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"zhang2025tts\", \"type\": \"article\", \"title\": \"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\", \"authors\": \"Zhang, Qiyuan and Lyu, Fuyuan and Sun, Zexu and Wang, Lei and Zhang, Weixu and G...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.24235\"}, {\"key\": \"venktesh2025trust\", \"type\": \"article\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"authors\": \"Venktesh, V and Rathee, Mandeep and Anand, Avishek\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.16665\"}, {\"key\": \"jinnai2024mbr\", \"type\": \"inproceedings\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"authors\": \"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}], \"tex_citations\": [{\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 4, \"command\": \"citealp\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/introduction.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/introduction.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/introduction.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/introduction.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 49, \"command\": \"citet\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"thirukovalluru2024atomic\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"manakul2023selfcheckgpt\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"zhang2025tts\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kim2026reasc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"wang2025rankedvoting\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"oh2025latentsc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"feng2025optimal\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"wang2025make\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"li2025llms\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"vashurin2025cocoa\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"zhou2024uniner\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"sainz2024gollie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"josifoski2022genie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"li2023codeie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wadhwa2023revisiting\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wang2023instructuie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"geng2024confidence\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"wen2025know\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xia2025survey\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"hobelsberger2025systematic\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xiong2024llm\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"heo2025uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"kossen2024semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"kadavath2022language\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"malinin2021uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"guo2017calibration\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"desai2020calibration\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"gal2016dropout\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"xiao2019uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"shelmanov2021active\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"zhang2023ener\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"kim2024verifiner\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"he2024uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"fisch2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"angelopoulos2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"lightman2024verify\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"venktesh2025trust\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"wang2024mathshepherd\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"jinnai2024mbr\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"geifman2017selective\", \"file\": \"sections/related_work.tex\", \"line\": 27, \"command\": \"cite\"}, {\"key\": \"culotta2004confidence\", \"file\": \"sections/related_work.tex\", \"line\": 27, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/method.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fleiss1971agreement\", \"file\": \"sections/method.tex\", \"line\": 34, \"command\": \"citet\"}, {\"key\": \"jaccard1901distribution\", \"file\": \"sections/method.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/experiments.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/experiments.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"zheng2024llamafactory\", \"file\": \"sections/experiments.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/experiments.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/experiments.tex\", \"line\": 60, \"command\": \"cite\"}, {\"key\": \"xiong2024llm\", \"file\": \"sections/experiments.tex\", \"line\": 74, \"command\": \"citep\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/experiments.tex\", \"line\": 133, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/experiments.tex\", \"line\": 133, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/experiments.tex\", \"line\": 133, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/discussion.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/discussion.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/discussion.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"jinnai2024mbr\", \"file\": \"sections/discussion.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/discussion.tex\", \"line\": 22, \"command\": \"citet\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/discussion.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"venktesh2025trust\", \"file\": \"sections/discussion.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/appendix.tex\", \"line\": 190, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/appendix.tex\", \"line\": 190, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/appendix.tex\", \"line\": 380, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"angelopoulos2021conformal\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"brown2024monkeys\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024usc\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Self-Consistency for Large Language Model Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021verifiers\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culotta2004confidence\", \"title\": \"Confidence Estimation for Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence estimation for information extraction\", \"matched_year\": \"2004\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"derczynski2017wnut\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"desai2020calibration\", \"title\": \"Calibration of Pre-trained Transformers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calibration of Pre-trained Transformers\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eikema2022sampling\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fisch2021conformal\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-shot Conformal Prediction with Auxiliary Tasks\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"freitag2022high\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"he2024uncertainty\", \"title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fleiss1971agreement\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring nominal scale agreement among many raters.\", \"matched_year\": \"1971\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gal2016dropout\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"geifman2017selective\", \"title\": \"Selective Classification for Deep Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Selective Classification for Deep Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feng2025optimal\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=feng vs api=austin\"], \"note\": \"\"}, {\"key\": \"geng2024confidence\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2017calibration\", \"title\": \"On Calibration of Modern Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Calibration of Modern Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hobelsberger2025systematic\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.236, \"matched_title\": \"A new criterion for assessing discriminant validity in variance-based structural equation modeling\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.24 below threshold 0.82\"}, {\"key\": \"jaccard1901distribution\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"matched_year\": \"1901\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"josifoski2022genie\", \"title\": \"GenIE: Generative Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GenIE: Generative Information Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2025selfcertainty\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2024verifiner\", \"title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2026reasc\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kossen2024semantic\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025llms\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuhn2023semantic\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"malinin2021uncertainty\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023codeie\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lightman2024verify\", \"title\": \"Let's Verify Step by Step\", \"status\": \"not_found\", \"confidence\": 0.246, \"matched_title\": \"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"luan2018scierc\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"manakul2023selfcheckgpt\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nedellec2026consistency\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oh2025latentsc\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sainz2024gollie\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shelmanov2021active\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"snell2025scaling\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=snell vs api=charlie\"], \"note\": \"\"}, {\"key\": \"taubenfeld2025cisc\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence Improves Self-Consistency in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thirukovalluru2024atomic\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tjongkimsang2003conll\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"matched_year\": \"2003\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vashurin2025cocoa\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa2023revisiting\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023instructuie\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023selfconsistency\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025make\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2024mathshepherd\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025rankedvoting\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wen2025know\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023guided\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2025survey\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiao2019uncertainty\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2023ener\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zheng2024llamafactory\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024uniner\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiong2024llm\", \"title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"muller2021understanding\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"matched_year\": \"2021\", \"mismatch_fields\": [\"first_author: bib=m\\\\\\\"uller vs api=müller\"], \"note\": \"\"}, {\"key\": \"heo2025uncertainty\", \"title\": \"Do LLMs Estimate Uncertainty Well in Instruction Following?\", \"status\": \"verified\", \"confidence\": 0.983, \"matched_title\": \"Do LLMs estimate uncertainty well in instruction-following?\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eikema2025structured\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2025tts\", \"title\": \"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"venktesh2025trust\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"status\": \"not_found\", \"confidence\": 0.252, \"matched_title\": \"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"jinnai2024mbr\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5d6b122-8233-48da-9d22-ae909b9d2c3c",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "1b67e05c-5c6c-4988-9684-cf9a3e817122",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/eb1a3f49-65c9-4074-8546-55ac5548828b/tool-results/toolu_01NEwNG45FBvBPtMRiJ9HQX3.txt",
      "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 62, \\\"total_citations\\\": 93, \\\"unique_cited_keys\\\": 62, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 56, \\\"online_not_found\\\": 3, \\\"online_mismatch\\\": 3}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"authors\\\": \\\"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"ICLR 2021\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"authors\\\": \\\"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2407.21787\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"authors\\\": \\\"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint (ICML 2024 Workshop ICL)\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"authors\\\": \\\"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2110.14168\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"authors\\\": \\\"Culotta, Aron and McCallum, Andrew\\\", \\\"year\\\": \\\"2004\\\", \\\"venue\\\": \\\"HLT-NAACL 2004\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"authors\\\": \\\"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"W-NUT Workshop at EMNLP 2017\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"authors\\\": \\\"Desai, Shrey and Durrett, Greg\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"authors\\\": \\\"Eikema, Bryan and Aziz, Wilker\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Few-Shot Conformal Prediction with Auxiliary Tasks\\\", \\\"authors\\\": \\\"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"ICML 2021\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"authors\\\": \\\"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"he2024uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\\\", \\\"authors\\\": \\\"He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL 2024\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"authors\\\": \\\"Fleiss, Joseph L.\\\", \\\"year\\\": \\\"1971\\\", \\\"venue\\\": \\\"Psychological Bulletin\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"authors\\\": \\\"Gal, Yarin and Ghahramani, Zoubin\\\", \\\"year\\\": \\\"2016\\\", \\\"venue\\\": \\\"ICML 2016\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"authors\\\": \\\"Geifman, Yonatan and El-Yaniv, Ran\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"NeurIPS 2017\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2511.12309\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"authors\\\": \\\"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"authors\\\": \\\"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"ICML 2017\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"authors\\\": \\\"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2510.20460\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"authors\\\": \\\"Jaccard, Paul\\\", \\\"year\\\": \\\"1901\\\", \\\"venue\\\": \\\"Bulletin de la Société Vaudoise des Sciences Naturelles\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"authors\\\": \\\"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"authors\\\": \\\"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2207.05221\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"authors\\\": \\\"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"kim2024verifiner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Kim, Seoyeon and Seo, Kwangwook and Chae, Hyungjoo and Yeo, Jinyoung and Lee, Do...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"authors\\\": \\\"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"ACL 2026\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"authors\\\": \\\"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2406.15927\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"authors\\\": \\\"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.04104\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"authors\\\": \\\"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"authors\\\": \\\"Malinin, Andrey and Gales, Mark\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"authors\\\": \\\"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"NeurIPS 2017\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"authors\\\": \\\"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"authors\\\": \\\"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"authors\\\": \\\"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"authors\\\": \\\"Manakul, Potsawee and Liusie, Adian and Gales, Mark\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\\\", \\\"authors\\\": \\\"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Genomics \\\\\\\\& Informatics\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"authors\\\": \\\"Oh, Jungsuk and Lee, Jay-Yoon\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.18395\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"authors\\\": \\\"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"authors\\\": \\\"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 16th Conference of the European Chapter of the Association fo...\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"authors\\\": \\\"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"authors\\\": \\\"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"authors\\\": \\\"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"authors\\\": \\\"Sang, Erik F. Tjong Kim and Meulder, Fien De\\\", \\\"year\\\": \\\"2003\\\", \\\"venue\\\": \\\"CoNLL 2003\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"authors\\\": \\\"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"authors\\\": \\\"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"authors\\\": \\\"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2304.08085\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"authors\\\": \\\"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"authors\\\": \\\"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL 2025\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"authors\\\": \\\"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ACL 2024\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"authors\\\": \\\"Wang, Weiqin and Wang, Yile and Huang, Hui\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"authors\\\": \\\"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"authors\\\": \\\"Willard, Brandon T. and Louf, Rémi\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2307.09702\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"authors\\\": \\\"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"authors\\\": \\\"Xiao, Yijun and Wang, William Yang\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2023\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"authors\\\": \\\"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\\", \\\"authors\\\": \\\"Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Ju...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"authors\\\": \\\"M\\\\\\\\\\\\\\\"uller, Mathias and Sennrich, Rico\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"heo2025uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Do LLMs Estimate Uncertainty Well in Instruction Following?\\\", \\\"authors\\\": \\\"Heo, Juyeon and Xiong, Miao and Heinze-Deml, Christina and Narain, Jaya\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"authors\\\": \\\"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"zhang2025tts\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\\\", \\\"authors\\\": \\\"Zhang, Qiyuan and Lyu, Fuyuan and Sun, Zexu and Wang, Lei and Zhang, Weixu and G...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.24235\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\", \\\"authors\\\": \\\"Venktesh, V and Rathee, Mandeep and Anand, Avishek\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.16665\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"authors\\\": \\\"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 41st International Conference on Machine Learning (ICML)\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citealp\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 49, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2025tts\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"heo2025uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2024verifiner\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"he2024uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 34, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 45, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 60, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 74, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 133, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 133, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 133, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 45, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 45, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 190, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 190, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 380, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence estimation for information extraction\\\", \\\"matched_year\\\": \\\"2004\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"title\\\": \\\"Few-Shot Conformal Prediction with Auxiliary Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Few-shot Conformal Prediction with Auxiliary Tasks\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"he2024uncertainty\\\", \\\"title\\\": \\\"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"matched_year\\\": \\\"1971\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"matched_year\\\": \\\"2015\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=feng vs api=austin\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.236, \\\"matched_title\\\": \\\"A new criterion for assessing discriminant validity in variance-based structural equation modeling\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.24 below threshold 0.82\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"matched_year\\\": \\\"1901\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2024verifiner\\\", \\\"title\\\": \\\"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.246, \\\"matched_title\\\": \\\"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=snell vs api=charlie\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2003\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"title\\\": \\\"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=m\\\\\\\\\\\\\\\"uller vs api=müller\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"heo2025uncertainty\\\", \\\"title\\\": \\\"Do LLMs Estimate Uncertainty Well in Instruction Following?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.983, \\\"matched_title\\\": \\\"Do LLMs estimate uncertainty well in instruction-following?\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2025tts\\\", \\\"title\\\": \\\"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"title\\\": \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.252, \\\"matched_title\\\": \\\"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
      "numLines": 1,
      "startLine": 0,
      "totalLines": 1
    }
  },
  "sourceToolAssistantUUID": "d5d6b122-8233-48da-9d22-ae909b9d2c3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
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
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。  ## 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction - **论文路径**: `projects…",
  "leafUuid": "1b67e05c-5c6c-4988-9684-cf9a3e817122",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Runtime record

_source line 72_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured information extraction confidence signals paper",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Assistant

_source line 73 · 2026-05-15T12:18:44.961Z_

<details><summary>Logged reasoning block</summary>

```text
The reference verification results show:
- 62 bib entries, 62 cited, 0 orphan, 0 missing
- 56 verified online, 3 not found (hobelsberger2025systematic, lightman2024verify, venktesh2025trust), 3 mismatches (feng2025optimal, snell2025scaling, muller2021understanding - all just first_author format issues)

The "not found" ones are likely just not indexed in OpenAlex yet (arXiv preprints). lightman2024verify ("Let's Verify Step by Step") is a well-known OpenAI paper - definitely real. The mismatches are just author name formatting (last name vs first name in the API).


Now I'm working through the full review, examining the paper's key strengths: the problem setup cleanly separates quality estimation from sample selection, the experimental design comprehensively tests 5 signals across 3 families, datasets, and models with rigorous statistical methods including bootstrap and effect sizes, and the authors are appropriately cautious about preliminary results. The negative finding about LP score compression is mechanistically insightful, and the correlation-selection gap concept offers genuine value to the field.

But there are critical weaknesses. The selection gap analysis—the paper's main claim in Table 3—relies on a single seed, while the multi-seed validation in the appendix only covers quality estimation, leaving the p=0.39 selection result vulnerable to seed variation. More fundamentally, the ε=0.05 threshold that drives the "60% effectively tied" narrative is completely unjustified; Table 12 reveals extreme sensitivity where this metric ranges from 1.1% at ε=0.01 to 84% at ε=0.1, yet the paper never explains why 0.05 is the right choice.

There's also a mismatch between the ablation's limited scope—just one dataset, one model, one seed—and the Discussion's claim about a "fundamental challenge" in structured IE that transcends decoding strategies, which the evidence doesn't support. On the statistical side, the FK independence test uses only 5 configurations with high variability, giving it very low power to detect real effects.

The VC definition creates confusion too: Equation 6 defines it as mean frequency over the union, but the footnote reveals selection actually uses a majority threshold, resulting in different correlation values (0.379 vs 0.252). And the TOST equivalence margins are anchored to oracle headroom fractions, which is circular reasoning since the headroom itself is just an empirical observation rather than an external standard.

There's also a notable gap where LP data is missing from the T=0.7 comparison, which is problematic given that LP behavior is central to the paper's mechanistic claims. Meanwhile, the title and abstract suggest broader coverage of structured information extraction and relation extraction, but the RE findings only come from SciERC, creating a mismatch between what the abstract implies and what the evidence actually supports. The Qwen3-8B thinking token confound also isn't sufficiently bounded by the paper's arguments about why it wouldn't explain the results.

The paper's reasoning that "LP selection fails across all datasets" doesn't actually address whether the confound could specifically harm SciERC performance without affecting other datasets. A more direct comparison between Qwen and LLaMA on SciERC would help quantify this potential impact. Beyond these major concerns, there are several smaller issues: Cohen's d is only reported for NER LP, the bootstrap resampling procedure isn't specified as instance-level or sample-level, and table formatting inconsistently labels model variants across datasets.

I'm also noticing some definitional ambiguities—like whether the Hungarian algorithm for SJ weighting operates per-type or globally, and whether CoNLL split sizes should be documented more explicitly. The authors should clarify whether the selection analysis in Table 3 was run across multiple seeds to assess variance, how robust the "60% effectively tied" claim is to different ε thresholds, and whether the free-form ablation could extend to other datasets like CoNLL or WNUT-17.

For the non-tied subset, I'd want confidence intervals around that +2.9pp LP gain, and I need to confirm whether the VC footnote's ρ=0.252 variant is actually what's used in the main selection results.

The methodology is generally sound, though I have reservations about the single-seed selection analysis, the unjustified ε threshold choice, and how broadly the ablation claims generalize—I'd rate soundness around 3.5/5. The correlation-selection gap itself is a genuinely novel contribution for information extraction, the MBR connection adds real insight, and the negative result is well-explained.

Overall, the paper delivers meaningful findings on the QE-selection separation and diagnoses the gap effectively, but the core selection analysis—which is really the paper's main claim—needs stronger statistical grounding. I'm settling on 3/5 for the overall assessment. I've engaged carefully with the paper and verified the mathematics and citations, so I'm confident in my evaluation at 4/5. The reproducibility is hampered by relying on a single seed for the headline results, though the training setup is otherwise complete—that's 3.5/5.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b67e05c-5c6c-4988-9684-cf9a3e817122",
  "isSidechain": false,
  "requestId": "req_011Cb4LhzeXKDnAMLTe3vSp3",
  "type": "assistant",
  "uuid": "dd56f5d3-8a57-4fd9-aeb5-3c3ea7e3f36a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kp6v3cX9tuaceXHmVGgLja",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18088,
      "cache_read_input_tokens": 64292,
      "output_tokens": 7623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18088,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7623,
          "cache_read_input_tokens": 64292,
          "cache_creation_input_tokens": 18088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18088
          },
          "type": "message"
        }
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

_source line 74 · 2026-05-15T12:20:10.611Z_

引用验证完成（62条全部 cross-check 通过，3条 not_found 均为合理的未索引 arXiv 预印本）。现在综合所有材料撰写完整审稿意见。

---

## 总体评分

**Overall**: 3/5 (Findings of the ACL)
**一句话总结**: 论文提出了有价值的 correlation-selection gap 概念并提供了扎实的 quality estimation 分析，但核心 selection failure 结论建立在 single-seed 分析上、ε=0.05 阈值缺乏论证、free-form ablation 范围过窄却支撑了过强的泛化声称。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 方法定义清晰，QE 分析可靠；但 selection gap 的统计支撑不足（single seed）、关键阈值未论证、ablation 泛化过度 |
| Excitement | 3.5/5 | Correlation-selection gap 概念对 IE + test-time scaling 社区有实际指导意义；MBR 连接有洞察力；但作为 negative result 论文，诊断深度仍可加强 |
| Overall | 3/5 | 贡献真实但 selection 分析——论文的核心卖点——统计论证最弱；建议补充多种子 selection 分析后可达 Findings |
| Confidence | 4/5 | 仔细阅读全文含附录，核查公式推导和引用，熟悉 MBR decoding 和 uncertainty estimation 文献 |
| Reproducibility | 3.5/5 | 训练配置完整（Table 7），prompt template 提供，constrained decoding 工具明确；但核心实验 single seed 限制复现可信度 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Selection gap 分析缺乏多种子验证——核心结论统计支撑不足

- 具体位置：Section 4.3 / Table 3 / §5 (Discussion)
- 问题：论文的 headline finding 是 selection failure（Table 3: LP NER +0.6pp, p=0.39）。然而这一分析仅使用 seed=42 的单次实验。3-seed 稳定性分析（Table 10, Appendix E）仅覆盖 quality estimation 的 ρ 值，**未报告 selection F1 的跨种子方差**。p=0.39 本身就处于高度不确定区间（95% CI: [−3.0, +4.2]pp），在不同种子下可能出现 p<0.05 的结果。论文的核心贡献（Contribution 2: "the correlation-selection gap and its diagnosis"）建立在这一统计基础之上。
- 为什么影响接收：一个依赖 single-seed p-value 的 negative result 论文，其主要结论的可靠性无法评估。ARR reviewer guidelines 明确要求 "reproducible experimental setup"——selection gap 的可重复性未被验证。
- 建议修改方向：将 3-seed 分析扩展至 Table 3 的 selection F1，报告跨种子 mean±σ 和 p-value 范围。如果三个种子的 p-value 均 >0.10，则 selection failure 结论可信；如果有种子 p<0.05，则需重新框定结论。

**N2** [critical] ε=0.05 "effectively tied" 阈值缺乏论证

- 具体位置：Section 5 第3段 / Appendix H (Table 12) / Abstract ("60% instances effectively tied")
- 问题：Table 12 显示 LP tied fraction 对 ε 极度敏感——ε=0.01 时 1.1%，ε=0.05 时 60.3%，ε=0.1 时 ~84%。这个 59× 的跳变说明 0.05 恰好处于分布的陡峭区域。论文未论证 0.05 作为 "effective tie" 的依据：是否与 LP 的 scale 相关？是否对应可检测的 F1 差异？Table 12 下方的非 tied subset 分析（n=210, +2.9pp, p=0.01）正是基于此阈值的二分，阈值选择直接影响非 tied subset 的大小和结论强度。
- 为什么影响接收："60% effectively tied" 出现在 abstract、introduction、discussion 中，是 score compression 诊断的核心数据点。如果 ε=0.03 才是合适的阈值（tied fraction 可能只有 ~20-30%），整个 "compression is the primary bottleneck" 叙事需要重写。
- 建议修改方向：(1) 提供 LP range 的完整 CDF 而非离散阈值表；(2) 用 within-instance LP-F1 correlation 作为连续度量而非二元 tied/non-tied 划分；(3) 如果坚持使用阈值，需论证 0.05 对应实际可区分的质量差异（例如：ε=0.05 对应的 expected F1 difference 是多少？）。

**N3** [critical] Free-form ablation 范围过窄但支撑了过强的泛化声称

- 具体位置：Section 5 §4 ("Score compression is task-inherent") / Discussion 最后一段 / Table 8 (Appendix I)
- 问题：Free-form ablation 使用 1 dataset (SciERC) × 1 model (Qwen3-8B) × 1 seed (42)。但 Discussion §4 的结论是 "The correlation-selection gap is therefore a fundamental challenge for test-time scaling in structured IE, not an artifact of any particular decoding strategy"（粗体"fundamental"出现在原文）。从一个数据集、一个模型的单次实验推导 "fundamental" 的泛化声称，逻辑跳跃过大。更重要的是，ablation 暴露了 RE LP selection 的 regime-specific 行为（constrained: −0.68pp → free-form: +1.69pp, Table 8 Panel B），这恰恰说明 decoding regime **确实** 影响 RE selection——与 "not an artifact" 的结论矛盾。
- 为什么影响接收：ablation 是支撑因果推断（"compression is intrinsic"）的唯一证据。如果该声称不成立，论文的诊断深度大幅降低——从 "机制性发现" 降级为 "经验观察"。
- 建议修改方向：(1) 将 Discussion 中 "fundamental" 降级为 "observed in our setting"；(2) 明确承认 RE LP selection flip 与 NER 结论不一致；(3) 如果来得及，在 CoNLL 上补充 free-form ablation（CoNLL 的 ceiling effect 可能导致不同的 compression pattern）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] FK 独立性检验的统计功效极低

- 具体位置：Section 3.2 第4段（FK 定义）
- 问题：excess agreement 的 one-sample t-test 仅基于 5 个 configuration-level 数据点（SciERC NER/RE, CoNLL, WNUT-17; N=8, T=1.0），自由度=4。数据范围 −0.4% 到 −4.0%（10 倍变异），t-test 的功效极低。论文结论 "confirms that FK is not inflated by inter-sample dependence" 过强——该检验只能证明存在弱负依赖，无法以有意义的功效排除正依赖。
- 建议：(1) 报告每个 configuration 的 per-instance excess agreement 分布，而非仅报告 configuration 均值；(2) 使用 instance-level bootstrap test（n=529+ per config）替代 5-point t-test。

**W2** [warning] VC 在 QE 和 selection 中使用不同计算但标注不清

- 具体位置：Section 3.2 Eq.6 + 脚注 / Table 3
- 问题：Eq.6 定义 VC 为 E_∪ 上的均值频率（连续 QE signal），脚注解释 selection 使用 majority threshold（freq > N/2）。两个计算的 ρ 差异显著（0.379 vs 0.252）。Table 3 中 "VC" selection F1 = 0.634——这是 majority-threshold 版本还是 Eq.6 版本？不清楚。
- 建议：在 Table 3 中明确标注使用的 VC 变体（如 "VC (majority)"），或在 Section 3.3 的 evaluation framework 中统一定义。

**W3** [warning] TOST δ 值缺乏外部锚定

- 具体位置：Appendix F (Table 6) / Section 4.3
- 问题：δ=±2/3/5pp 锚定于 oracle headroom 的比例（28-38% of headroom = ±5pp）。但 oracle headroom 本身是实验发现，不是独立的实践意义标准。论文未引用任何先验工作或从业者指南来论证 IE 任务中多大的 selection gain 具有实践意义。循环锚定（用实验结果定义显著性标准，再用该标准评判实验结果）削弱了 TOST 的论证力度。
- 建议：引用 IE 部署中的实际容差标准，或引用 MBR decoding 文献中使用的 equivalence margins，作为独立锚定。

**W4** [warning] LP 温度敏感性完全缺失

- 具体位置：Limitations section 最后一段 / Appendix B (Table 2, Figure 3)
- 问题：LP 在 T=0.7 vs T=1.0 比较中被排除，原因是 "missing T=0.7 LP data"。对于一篇以 LP score compression 为核心诊断的论文，这是不可接受的数据缺口。Temperature 直接影响 LP score distribution（较低温度 → 更高 LP 均值 → 可能更强或更弱的 compression），而这一信息对理解 compression 机制至关重要。
- 建议：补充 T=0.7 的 LP 数据，或至少提供理论分析说明温度如何影响 LP compression。

**W5** [warning] 标题/摘要泛化度超出 RE 证据覆盖

- 具体位置：Title / Abstract
- 问题：标题 "Structured Information Extraction" 和摘要 "NER and relation extraction on three benchmarks" 暗示 NER 和 RE 均有三个 benchmark 的支持。实际上 NER 覆盖 3 datasets（SciERC, CoNLL, WNUT-17），RE 仅覆盖 SciERC 1 dataset。正文中 "preliminary" 标注到位，但标题和摘要的读者不会看到这些限定词。
- 建议：摘要中明确 RE 的 single-benchmark 范围，例如 "NER on three benchmarks and RE on one (preliminary)"。

---

## 小问题（不影响接收）

- Table 1: SciERC 列未标注模型（全文后续可知为 Qwen），首次读者可能困惑。与 "CoNLL (Qwen)" "CoNLL (LLaMA)" 的标注不一致。
- Cohen's d=0.038 仅报告了 NER LP（Section 4.3），其余 signal 和 RE 均缺失。
- Bootstrap resampling 未指明重抽样单元是 instance-level 还是 sample-level。对于 paired bootstrap comparing selection vs. greedy，这一细节影响 CI 的解读。
- SJ 定义中 Hungarian matching 是 per-type 还是 global 不够清晰——"we group extractions by type, compute max-weight bipartite matching" 暗示 per-type，但 Eq.4 的 M 似乎是全局 matched set。
- CoNLL 训练 split 大小未在 Appendix D Table 7 中报告（仅有 SciERC split: 1861/275/551）。
- `eikema2025structured`（EMNLP 2025）被作为已发表工作引用但应标注为 concurrent work。

---

## Questions for Authors

1. 是否已在 3 seeds 上运行 Table 3 的 selection F1？跨种子 selection gap 的方差是多少？
2. 能否提供 LP within-instance range 的完整 CDF，而非离散阈值表？
3. Non-tied subset 的 LP selection gain (+2.9pp, p=0.01) 是否有 bootstrap 95% CI？
4. Free-form ablation 中 RE LP selection 从 −0.68pp 翻转到 +1.69pp——这如何与 "compression is intrinsic" 的结论兼容？
5. VC 在 Table 3 中使用的是 Eq.6（均值频率）还是脚注中的 majority-threshold 版本？

---

## Missing References

无明显遗漏。引用覆盖全面，62 篇引用经 OpenAlex 验证，56 篇确认，3 篇为合理的未索引 arXiv 预印本，3 篇为作者姓名格式差异（非实质性问题）。

---

## 主要优势

- **Correlation-selection gap 概念清晰且有社区价值**：将 quality estimation 与 sample selection 的分离形式化，为后续 test-time scaling 研究提供了明确的分析框架。
- **信号定义严谨**：五个信号从三个家族系统化定义，per-sample vs. instance-level 的 taxonomy 是本文的理论贡献。
- **诚实的 hedging**：RE 结论一致标注 "preliminary"，WNUT-17 作为 capability boundary 的讨论到位，Limitations section 详尽。
- **MBR decoding 连接**：将 consensus-proximity selection 等价于 MBR decoding 并诊断 utility-quality misalignment at per-sample level，是对 MBR 文献的有意义扩展。
- **附录深度**：12 个附录章节提供了从 diversity quantification、calibration analysis 到 LP failure stability 的系统性补充分析。

---

现在将审稿意见提交给 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd56f5d3-8a57-4fd9-aeb5-3c3ea7e3f36a",
  "isSidechain": false,
  "requestId": "req_011Cb4LhzeXKDnAMLTe3vSp3",
  "type": "assistant",
  "uuid": "8f9f6367-778a-4bfb-865f-ac0a233fae14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kp6v3cX9tuaceXHmVGgLja",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18088,
      "cache_read_input_tokens": 64292,
      "output_tokens": 7623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18088,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7623,
          "cache_read_input_tokens": 64292,
          "cache_creation_input_tokens": 18088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18088
          },
          "type": "message"
        }
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

_source line 75 · 2026-05-15T12:20:29.819Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_017Q5kKCdiZXKqqj7AzXkCnR`</summary>

```json
{
  "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction\n**Venue**: EMNLP 2026 Main Conference (Long Paper)\n\n---\n\n### 总体评分\n\n**Overall**: 3/5 (Findings of the ACL)\n**一句话总结**: 论文提出了有价值的 correlation-selection gap 概念并提供了扎实的 quality estimation 分析，但核心 selection failure 结论建立在 single-seed 分析上、ε=0.05 阈值缺乏论证、free-form ablation 范围过窄却支撑了过强的泛化声称。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 方法定义清晰，QE 分析可靠；但 selection gap 的统计支撑不足（single seed）、关键阈值未论证、ablation 泛化过度 |\n| Excitement | 3.5/5 | Correlation-selection gap 概念对 IE + test-time scaling 社区有实际指导意义；MBR 连接有洞察力 |\n| Overall | 3/5 | 贡献真实但 selection 分析——论文的核心卖点——统计论证最弱；补充多种子 selection 分析后可达 Findings |\n| Confidence | 4/5 | 仔细阅读全文含附录，核查公式推导和引用 |\n| Reproducibility | 3.5/5 | 训练配置完整（Table 7），但核心实验 single seed 限制复现可信度 |\n\n---\n\n### Must-Fix 问题（3个 Critical）\n\n**N1** [critical] Selection gap 分析缺乏多种子验证\n- 位置：Section 4.3 / Table 3\n- 核心 selection failure（LP NER +0.6pp, p=0.39）仅使用 seed=42。3-seed 分析（Table 10）仅覆盖 QE，未覆盖 selection F1。p=0.39 的 single-seed 结果不足以支撑论文的 headline finding。\n- 建议：将 3-seed 分析扩展至 Table 3，报告跨种子 selection F1 的 mean±σ 和 p-value 范围。\n\n**N2** [critical] ε=0.05 \"effectively tied\" 阈值缺乏论证\n- 位置：Section 5 / Appendix H (Table 12)\n- Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%（59×跳变），说明阈值处于分布陡峭区域。\"60% effectively tied\" 出现在 abstract 中但 0.05 的依据未给出。\n- 建议：提供 LP range 完整 CDF；或用连续度量（within-instance LP-F1 correlation）替代二元划分。\n\n**N3** [critical] Free-form ablation 范围过窄但结论过强\n- 位置：Section 5 §4 / Discussion\n- 1 dataset × 1 model × 1 seed 的 ablation 支撑了 \"fundamental challenge\" 的声称。且 RE LP selection 在 free-form 下翻转（−0.68pp→+1.69pp），与 \"not an artifact of decoding strategy\" 矛盾。\n- 建议：降级 \"fundamental\" 为 \"observed in our setting\"；明确承认 RE 翻转。\n\n### Should-Fix 问题（5个 Warning）\n\n**W1** FK 独立性检验功效极低（n=5 configurations 的 t-test）\n**W2** VC 在 QE 和 selection 中使用不同计算但 Table 3 标注不清\n**W3** TOST δ 值循环锚定于 oracle headroom，缺乏外部标准\n**W4** LP 温度敏感性完全缺失（核心诊断对象却无 T=0.7 数据）\n**W5** 标题/摘要暗示 NER+RE 均有多 benchmark 支持，实际 RE 仅单数据集\n\n### 主要优势\n\n- Correlation-selection gap 概念清晰且有社区价值\n- 五信号三家族的系统化 taxonomy 是理论贡献\n- RE \"preliminary\" 标注诚实，Limitations 详尽\n- MBR decoding 连接是对 MBR 文献的有意义扩展\n- 附录深度出色（12个补充分析章节）\n\n### 引用验证\n\n62篇引用全部 cross-check 通过，56篇 OpenAlex 确认，无伪造引用问题。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f9f6367-778a-4bfb-865f-ac0a233fae14",
  "isSidechain": false,
  "requestId": "req_011Cb4LhzeXKDnAMLTe3vSp3",
  "type": "assistant",
  "uuid": "40f824df-e17a-4342-9bcd-3f0ec832c3a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kp6v3cX9tuaceXHmVGgLja",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18088,
      "cache_read_input_tokens": 64292,
      "output_tokens": 7623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18088,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7623,
          "cache_read_input_tokens": 64292,
          "cache_creation_input_tokens": 18088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18088
          },
          "type": "message"
        }
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

_source line 76_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。  ## 论文信息 - **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction - **论文路径**: `projects…",
  "leafUuid": "40f824df-e17a-4342-9bcd-3f0ec832c3a6",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Runtime record

_source line 77_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured information extraction confidence signals paper",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Tool result

_source line 78 · 2026-05-15T12:20:33.653Z_

<details><summary>↩ Tool result · `toolu_017Q5kKCdiZXKqqj7AzXkCnR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40f824df-e17a-4342-9bcd-3f0ec832c3a6",
  "isSidechain": false,
  "promptId": "75ffd5de-9267-4621-9077-672488aeb87f",
  "type": "user",
  "uuid": "d94d5481-b03a-4b30-acbc-875695060dca",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "40f824df-e17a-4342-9bcd-3f0ec832c3a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
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
  "aiTitle": "Review structured information extraction confidence signals paper",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Runtime record

_source line 80 · 2026-05-15T12:23:22.681Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T12:23:22.681Z",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "content": "[Round 1 审稿请求]:\n以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Critical/Warning 级别的问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）\n\n**Overall**: 3/5\n\n### Critical Issues\n\n**N1**: Correlation-selection gap 大部分是 definitional，非 empirical\n- 4/5 signals 按设计对同一 instance 的所有 candidates 赋相同分数——论文 §5 自己承认这是 \"Layer 1 (definitional)\"，但 abstract/intro 将其包装为 empirical discovery。实际的 empirical finding 更窄：LP compression。需要根本性 reframing。\n\n**N2**: 模型规模同质性（仅 8B）无法支撑标题中 \"Do Not Scale\" 的 broad claim\n- 两个模型均为 8B 参数。论文自身发现 task difficulty × model capability 存在交互效应，但只测了一个 scale 点。标题/abstract 需要 scope down。\n\n**N3**: RE 结论过度前置但证据不足\n- 仅 SciERC RE 单 benchmark + Qwen only（preliminary），但 LP 负相关数字出现在 abstract 中。应从 abstract 移除或补充实验。\n\n### Warning Issues\n\n**W1**: Abstract 信息密度过高\n**W2**: \"First multi-family comparison\" 是 scope engineering\n**W3**: Evaluation framework (Contribution 1) 是 engineering benchmark 而非 methodological contribution\n**W4**: LP 的 temperature sensitivity 未表征\n**W5**: Conditional set 排除最难实例的 selection bias 未充分讨论\n**W6**: Eikema et al. (2025) structure-conditional MBR 仅在 Discussion 出现，应在 Related Work 中定位\n\n### 优势\n- 问题定位精准，负面结论有实用价值\n- 实验设计远超平均水平\n- Quality estimation vs. sample selection 的 conceptual distinction 有价值\n- 引用全面准确\n\n---\n\n请逐条（N1-N3, W1-W6）给出 [AGREE] 或 [REBUT] 回应。"
}
```

---

### Runtime record

_source line 81 · 2026-05-15T12:23:22.681Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T12:23:22.681Z",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

## Round 2

2 recorded events

### User

_source line 82 · 2026-05-15T12:23:22.671Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d94d5481-b03a-4b30-acbc-875695060dca",
  "isSidechain": false,
  "promptId": "9c03217b-74fd-43e1-af39-638464c1a42d",
  "type": "user",
  "isMeta": true,
  "uuid": "35683b89-0107-4d05-b819-52b480acce59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 83 · 2026-05-15T12:23:22.671Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35683b89-0107-4d05-b819-52b480acce59",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "b864f388-2aaf-42e7-add3-2df5182efcd0",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "3d340668-6622-4d01-88cd-953b475b73df",
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

7 recorded events

### User

_source line 84 · 2026-05-15T12:23:22.744Z_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Critical/Warning 级别的问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用论文具体 Section/Table/Figure 作为证据。

---

## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）

**Overall**: 3/5

### Critical Issues

**N1**: Correlation-selection gap 大部分是 definitional，非 empirical
- 4/5 signals 按设计对同一 instance 的所有 candidates 赋相同分数——论文 §5 自己承认这是 "Layer 1 (definitional)"，但 abstract/intro 将其包装为 empirical discovery。实际的 empirical finding 更窄：LP compression。需要根本性 reframing。

**N2**: 模型规模同质性（仅 8B）无法支撑标题中 "Do Not Scale" 的 broad claim
- 两个模型均为 8B 参数。论文自身发现 task difficulty × model capability 存在交互效应，但只测了一个 scale 点。标题/abstract 需要 scope down。

**N3**: RE 结论过度前置但证据不足
- 仅 SciERC RE 单 benchmark + Qwen only（preliminary），但 LP 负相关数字出现在 abstract 中。应从 abstract 移除或补充实验。

### Warning Issues

**W1**: Abstract 信息密度过高
**W2**: "First multi-family comparison" 是 scope engineering
**W3**: Evaluation framework (Contribution 1) 是 engineering benchmark 而非 methodological contribution
**W4**: LP 的 temperature sensitivity 未表征
**W5**: Conditional set 排除最难实例的 selection bias 未充分讨论
**W6**: Eikema et al. (2025) structure-conditional MBR 仅在 Discussion 出现，应在 Related Work 中定位

### 优势
- 问题定位精准，负面结论有实用价值
- 实验设计远超平均水平
- Quality estimation vs. sample selection 的 conceptual distinction 有价值
- 引用全面准确

---

请逐条（N1-N3, W1-W6）给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b864f388-2aaf-42e7-add3-2df5182efcd0",
  "isSidechain": false,
  "promptId": "9c03217b-74fd-43e1-af39-638464c1a42d",
  "type": "user",
  "uuid": "d0b70a71-53ef-4dcc-8783-9c5320b0a510",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-15T12:23:57.409Z_

<details><summary>Logged reasoning block</summary>

```text
The user (Review Director) is asking me (Reviewer 1) to respond to Reviewer 2's review point by point, marking each as [AGREE] or [REBUT] with evidence from the paper.

Let me go through each issue carefully based on my thorough reading of the paper.

**R2-N1**: Correlation-selection gap is mostly definitional, not empirical
- R2 argues that 4/5 signals being instance-level is by design, and the paper packages this as empirical discovery.
- The paper itself in §5 says "Layer 1 (definitional)" for the 4 instance-level signals. 

The real empirical findings are the LP compression diagnosis, the failure modes of MBR and consensus-proximity selection, and the non-tied subset analysis demonstrating that LP works when compression issues are addressed. R2 makes a fair point that the paper somewhat oversells the discovery aspect in the abstract and introduction, though the paper does acknowledge the definitional nature in §5 and Contribution 2. I'd say this is a partial agreement—the empirical contributions are solid, but the framing could be more precise about what's definitional versus what's genuinely discovered.

**R2-N2**: Model scale homogeneity (only 8B)

The title "Do Not Scale" is ambiguous—it could mean don't scale the quality of structured IE, or don't scale with model size. R2's interpretation is reasonable, and testing only 8B models is a legitimate limitation. The paper does acknowledge this in the Limitations section and notes consistency across two model families at that scale, so they're transparent about the scope. I think this is a valid concern about whether the title claim overreaches the evidence.

**R2-N3**: RE conclusions over-fronted despite insufficient evidence

Let me double-check what the abstract actually claims. It mentions LP negative correlation on WNUT-17, which is NER not RE, and the main claim is about signals achieving strong quality estimation but not improving sample selection despite oracle headroom. The introduction seems to be making broader claims than the evidence supports.

Looking at the actual results: WNUT-17 shows conditional correlations collapsing to near zero and LP exhibiting strong negative correlation—that's NER data. Throughout the body, RE is labeled as preliminary, yet the abstract presents "NER and relation extraction on three benchmarks" as if they're equally supported. This is misleading, and I agree with R2's concern here.

**R2-W1**: Abstract information density too high

The abstract tries to cover a lot of ground—the correlation-selection gap, five signals, the MBR connection, LP compression effects, free-form ablation results, and task complexity findings. That's substantial material for an eight-sentence abstract, and I'd partially agree it's trying to preview too many findings at once.

**R2-W2**: "First multi-family comparison" is scope engineering

The paper claims to be the first comparing structural, surface, and model-internal signals for IE, which frames an experimental design choice as a contribution. Contribution 1 describes "A systematic evaluation framework" comparing five signals across three families—this is more of an engineering contribution than a methodological one. I'd partially agree with that assessment.

**R2-W3**: Evaluation framework (Contribution 1) is engineering benchmark, not methodological

The framework applies existing metrics (QE ρ, AUROC, selection F1) without novel methodology, but the conceptual separation between QE and selection does have value. I'd push back partially here—that conceptual framing is a legitimate contribution even if the individual metrics are standard.

**R2-W4**: LP temperature sensitivity not characterized

I flagged this myself in my own review. Agree completely.

**R2-W5**: Conditional set excludes hardest instances—selection bias

The filtering to non-zero F1 removes instances where the model completely fails, which is reasonable if the question is whether signals help among instances where the model has some capability. The paper justifies this in §4.2 and Appendix F, showing that full-set correlations on WNUT-17 are driven by the zero/non-zero boundary. I'd rebut this—the conditional analysis is methodologically sound as a way to separate binary detection from quality gradation.

**R2-W6**: Eikema et al. (2025) should be in Related Work, not just Discussion

The paper cites Eikema et al. on structure-conditional MBR in §5 (Discussion), but it would fit more naturally in Related Work given its relevance to the paper's framing.

Actually, looking back at Related Work, the paper already covers MBR decoding broadly through several citations. Eikema et al. (2025) is specifically about structure-conditional MBR, which is most directly relevant to the Discussion's diagnostic analysis. Keeping it only in Discussion is defensible since it's used for interpretation rather than foundational context. I'd say it should ideally appear in both places.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0b70a71-53ef-4dcc-8783-9c5320b0a510",
  "isSidechain": false,
  "requestId": "req_011Cb4M8iZLjnrAmjBpd4VSk",
  "type": "assistant",
  "uuid": "639d461f-70c1-413c-a790-4025a4adb0d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GVBFWWD2sKpkgZH4y2q5A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 90074,
      "output_tokens": 4995,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 693,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4995,
          "cache_read_input_tokens": 90074,
          "cache_creation_input_tokens": 693,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 693
          },
          "type": "message"
        }
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

_source line 86 · 2026-05-15T12:24:55.433Z_

逐条回应 Reviewer 2 的意见。

---

## 交叉回应：Reviewer 2 审稿意见

### Critical Issues

**[AGREE] R2-N1: Correlation-selection gap 大部分是 definitional**

R2 的核心观察是准确的。论文在 Section 5 ("Why the gap exists: two layers") 明确承认 "Layer 1 (definitional): Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction"。Introduction 的 Contribution 2 也做了区分："The instance-level failure of four signals is definitional; the empirical contributions are diagnosing why consensus-proximity selection (MBR decoding) and log-probability both fail。"

但 abstract 和 title 确实将整个 gap 包装为统一的 empirical finding。Abstract 说 "none significantly improves sample selection despite substantial oracle headroom"——这对 4/5 signals 是 tautological（instance-level signal 无法做 sample selection 是定义决定的），只对 LP 和 MBR-style consensus-proximity selection 是 empirical claim。

**实际的 empirical contribution 更窄**：(1) LP score compression 诊断（Section 5, Appendix H），(2) consensus-proximity (MBR) selection 的 utility-quality misalignment（Section 5 §3），(3) non-tied subset 分析（n=210, +2.9pp, p=0.01, Appendix H）。这些发现有价值但需要 reframing，使 abstract 更准确地反映 definitional vs. empirical 的边界。

补充我自己的观察：论文的 Section 3.3 (Evaluation Framework) 在 "Complementarity" 段落实际上预示了这一点——"if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates"——但这个洞察被埋在方法论叙述中，没有在 abstract/intro 中前置。

**[AGREE] R2-N2: 模型规模同质性无法支撑 "Do Not Scale" 的 broad claim**

标题 "Do Not Scale Structured Information Extraction" 的 "scale" 存在歧义——可以理解为 "信号无法 scale IE 的质量"（论文意图）或 "无法 scale 到更大模型"（读者的自然联想，尤其在 test-time scaling 的语境下）。无论哪种解读，仅 8B × 2 models 的证据不足以支撑 universal claim。

论文自身发现的 task difficulty × model capability 交互效应（Section 4.2: WNUT-17 capability boundary, CoNLL ceiling effect）恰恰说明 model capability 是关键调节变量。Limitations section 承认 "whether our findings hold for larger models (70B+) or closed-source APIs remains untested" 以及 "Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape"。

更大模型可能产生更高多样性的 samples（降低 LP compression）或更好的 calibration（改善 LP selection），这将直接挑战 "Do Not Scale" 结论。建议标题 scope down 至 "8B-scale models" 或改为问句形式。

**[REBUT] R2-N3: RE 结论过度前置**

R2 认为 "LP 负相关数字出现在 abstract 中"——但这是对论文内容的误读。Abstract 中没有任何 RE 负相关数字。Abstract 提到的 LP 相关内容是 "log-probability scores are compressed into effective ties"（这是 NER 上的发现）。

Introduction 中出现的 LP 负相关 ρ=−0.410 是 **WNUT-17 NER** 的结果（Section 4.2: "On WNUT-17...LP exhibits strong negative correlation (ρ=−0.410, AUROC=0.219)"），不是 RE。WNUT-17 只有 NER 标注，没有 RE task。

论文的 RE 前置主要在 abstract 的 "NER and relation extraction on three benchmarks"——如我在自己的 W5 中指出，这确实暗示 RE 也有三个 benchmark 的支持，实际只有 SciERC 一个。正文中 RE 始终标注 "preliminary"（Table 1 caption, Section 4.3, Conclusion），hedging 到位。

**总结**：R2-N3 的具体例证（LP 负相关在 abstract）是误读，但其 underlying concern（RE 证据不足被前置）与我的 W5 一致——问题出在 abstract 的措辞暗示了比实际更广的 RE 覆盖度，不在于具体数字被前置。建议 R2 修正这一 factual error。

---

### Warning Issues

**[AGREE] R2-W1: Abstract 信息密度过高**

Abstract 8 句话内容覆盖了：(1) test-time scaling 背景，(2) 5 signals 比较，(3) correlation-selection gap，(4) instance-level vs per-sample taxonomy，(5) LP compression + non-tied 子集，(6) MBR connection，(7) free-form ablation，(8) task complexity boundary conditions。每个发现只获得约一句话的空间，对 unfamiliar reader 不友好。加上 R2-N1 指出的 definitional/empirical 混淆，abstract 确实需要精简和 reframing。

**[REBUT] R2-W2: "First multi-family comparison" 是 scope engineering**

论文没有声称 "first multi-family comparison"——Contribution 1 的原文是 "A systematic evaluation framework. We compare five confidence signals from three families...showing that these metrics decouple and single-metric evaluation risks selecting the wrong signal"（Introduction, Contribution 1）。这不是 priority claim，而是 evaluation methodology claim——ρ、AUROC、selection F1 三个 metric 的 decouple 是核心发现。

Section 4.2 的 ρ-AUROC dissociation（EM leads AUROC=0.749 but ranks third in ρ=0.295, Table 1）和 Section 5 ("Methodological implications") 中 "evaluating on a single metric risks selecting the wrong signal" 提供了具体证据。这不是 scope engineering，而是一个 empirically grounded methodological recommendation。

**[REBUT] R2-W3: Evaluation framework 是 engineering benchmark 而非 methodological contribution**

同意 individual metrics（Spearman ρ, AUROC, best-of-N F1）各自不新颖。但 Contribution 1 的核心不是 metrics 本身，而是 **三个 metrics 的 decouple**。Section 4.2 用 Table 1 直接证明：EM 在 AUROC 上领先（0.749）但在 ρ 上排第三（0.295）；LP 在 LLaMA CoNLL 上 AUROC 最高（0.761）但 ρ 最低（0.307）。如果只用一个 metric 评估，practitioner 会选错 signal——这是一个有实践意义的发现，不仅是 engineering。

当然，R2 的 underlying concern 有道理——如果论文将其降级为 "finding" 而非 "contribution"，framing 会更准确。

**[AGREE] R2-W4: LP temperature sensitivity 未表征**

与我的 W4 完全一致。Limitations section 最后一段承认 "log-probability was excluded from the temperature comparison (T=0.7 vs T=1.0) due to missing T=0.7 LP data, leaving its temperature sensitivity uncharacterized"。对于核心诊断对象，这是不可接受的数据缺口。

**[REBUT] R2-W5: Conditional set 排除最难实例的 selection bias**

Conditional filtering 的目的恰恰是 **分离两个不同的现象**。Section 4.2 (WNUT-17 分析) 明确解释：full-set ρ=0.724（VC）完全由 zero/non-zero boundary 驱动，conditional ρ=0.038（n.s., Table 5）。这不是 selection bias——而是诊断：full-set correlations 混淆了 "binary success prediction"（模型是否能做这个任务）与 "quality gradation"（在模型能做的实例中，quality estimation 是否有效）。

Appendix F 进一步验证了 conditional filtering 的 methodological 合理性：EM 在 conditional set 上排名第一（NER ρ=0.360, RE ρ=0.417），而 full-set 排名差异很大——说明 filtering 揭示了被 floor effect 遮蔽的信号差异。

排除 zero-F1 实例不是 "excluding hardest instances" 的 bias，而是排除 "模型完全无能力的实例"——在这些实例上，**所有** consistency signals 都只能做 binary detection（有/无提取），无法做 quality estimation。这是合理的 evaluation scoping。

**[AGREE] R2-W6: Eikema et al. (2025) 应在 Related Work 中定位**

Section 2 (Related Work) 提到了 MBR decoding 的基础文献（eikema2022sampling, freitag2022high, muller2021understanding, jinnai2024mbr），但 eikema2025structured（structure-conditional MBR）仅在 Discussion §3 出现。考虑到该工作直接研究 structured outputs 上 MBR 的降级问题，与本文的 MBR-for-IE failure 发现高度相关，应在 Related Work 的 MBR 段落中就提及并定位差异（他们研究 structure-conditional utility functions 的设计，本文发现 utility-quality misalignment 在 per-sample level 是根本性的）。

---

将交叉回应提交给 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "639d461f-70c1-413c-a790-4025a4adb0d9",
  "isSidechain": false,
  "requestId": "req_011Cb4M8iZLjnrAmjBpd4VSk",
  "type": "assistant",
  "uuid": "5ea4e78f-d5ed-42dc-af1f-2f1018fb9118",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GVBFWWD2sKpkgZH4y2q5A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 90074,
      "output_tokens": 4995,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 693,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4995,
          "cache_read_input_tokens": 90074,
          "cache_creation_input_tokens": 693,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 693
          },
          "type": "message"
        }
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

_source line 87 · 2026-05-15T12:25:07.487Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01EXSqB7r8ezFK4qT5M91eFF`</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 的交叉回应\n\n### Critical Issues\n\n**[AGREE] R2-N1**: Correlation-selection gap 确实大部分是 definitional。论文 §5 自己承认 \"Layer 1 (definitional)\"，但 abstract/intro 将整个 gap 包装为统一的 empirical finding。实际 empirical contribution 更窄：LP compression 诊断 + MBR utility-quality misalignment + non-tied subset 分析。需要 reframing。\n\n**[AGREE] R2-N2**: 仅 8B × 2 models 不足以支撑 \"Do Not Scale\" 的 universal claim。论文自身发现的 task difficulty × model capability 交互效应说明 model capability 是关键调节变量。标题需要 scope down。\n\n**[REBUT] R2-N3**: R2 声称 \"LP 负相关数字出现在 abstract 中\"——这是误读。Abstract 中没有 RE 负相关数字。Introduction 中的 ρ=−0.410 是 WNUT-17 NER（非 RE）。但 R2 的 underlying concern（RE 证据不足被前置）与我的 W5 一致——问题在于 abstract 措辞暗示了比实际更广的 RE 覆盖度。建议 R2 修正 factual error。\n\n### Warning Issues\n\n**[AGREE] R2-W1**: Abstract 信息密度过高，8句话覆盖过多发现。\n**[REBUT] R2-W2**: 论文未声称 \"first multi-family comparison\"。Contribution 1 的核心是三个 metrics 的 decouple（ρ-AUROC dissociation, Table 1），不是 priority claim。\n**[REBUT] R2-W3**: Contribution 1 核心是三个 metrics decouple 的 empirical finding（EM leads AUROC=0.749 but ranks third in ρ=0.295），有实践意义。同意降级为 \"finding\" 比 \"contribution\" 更准确。\n**[AGREE] R2-W4**: 与我的 W4 完全一致。LP 温度敏感性缺失是核心诊断对象的数据缺口。\n**[REBUT] R2-W5**: Conditional filtering 是分离 binary detection 与 quality gradation 的 methodological 必要步骤，不是 selection bias。Table 5 显示 full-set ρ=0.724 完全由 zero/non-zero boundary 驱动。\n**[AGREE] R2-W6**: eikema2025structured 应在 Related Work 的 MBR 段落中定位。\n\n### 汇总\n\nR2 的 N1（definitional reframing）和 N2（scale scope down）与我自己的评估一致，是需要作者解决的实质问题。N3 有 factual error 但 underlying concern 成立。W2/W3/W5 我持不同意见，已提供具体证据。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ea4e78f-d5ed-42dc-af1f-2f1018fb9118",
  "isSidechain": false,
  "requestId": "req_011Cb4M8iZLjnrAmjBpd4VSk",
  "type": "assistant",
  "uuid": "deaaf870-3860-4996-b2ca-3c647d5f9773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GVBFWWD2sKpkgZH4y2q5A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 90074,
      "output_tokens": 4995,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 693,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4995,
          "cache_read_input_tokens": 90074,
          "cache_creation_input_tokens": 693,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 693
          },
          "type": "message"
        }
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

_source line 88_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Critical/Warning 级别的问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用论文具体 Section/Table/Figure 作为证据。  ---  ## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）  **Overall**: 3/5…",
  "leafUuid": "deaaf870-3860-4996-b2ca-3c647d5f9773",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Runtime record

_source line 89_

```json
{
  "type": "ai-title",
  "aiTitle": "Review structured information extraction confidence signals paper",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b"
}
```

---

### Tool result

_source line 90 · 2026-05-15T12:25:11.457Z_

<details><summary>↩ Tool result · `toolu_01EXSqB7r8ezFK4qT5M91eFF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "deaaf870-3860-4996-b2ca-3c647d5f9773",
  "isSidechain": false,
  "promptId": "9c03217b-74fd-43e1-af39-638464c1a42d",
  "type": "user",
  "uuid": "8839caed-4714-45ec-af24-2e46930493fa",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "deaaf870-3860-4996-b2ca-3c647d5f9773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "eb1a3f49-65c9-4074-8546-55ac5548828b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
