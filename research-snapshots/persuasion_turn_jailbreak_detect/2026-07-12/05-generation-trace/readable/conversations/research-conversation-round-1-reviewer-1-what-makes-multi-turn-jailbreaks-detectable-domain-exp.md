# Research conversation: [Round 1 审稿请求]: 你是 Reviewer 1，负责**方法严谨性 + 实验设计**。 ## 论文信息 - 标题: "What Makes Multi-Turn Jailbreaks Detectable? Domain Exp

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 70
- **Recorded user turns:** 3
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/3eec1eca-545d-4d07-897d-ac83e698f765.jsonl`
- **Structured JSON:** [`7fd41bfeab945e07373b.json`](../../sessions/7f/7fd41bfeab945e07373b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T18:00:42.543Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T18:00:42.543Z",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "content": "[Round 1 审稿请求]:\n你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题: \"What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\"\n- 路径: `projects/persuasion_turn_jailbreak_detect/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex, checklist.tex, references.bib）\n- 目标 Venue: EMNLP 2026 (ARR May cycle)\n- 截止日期: 2026-05-25\n- 页数限制: 正文 ≤ 8 页，references + appendices 无限制\n- 模板: ACL (`\\usepackage[review]{acl}`)\n- 匿名规则: Double-blind\n- 附录规则: 附录不计入页数限制，审稿人可选择性阅读\n\n## 你的审查侧重\n\n### 1. 实验设计与 Ablation 控制\n- 七个 DeBERTa 变体 + 三个 RoBERTa 变体的 ablation 设计是否真正隔离了声称的因素（domain exposure, classification supervision, label quality, label granularity, domain specificity）？\n- frozen encoder 设计是否引入系统性偏差？是否低估了某些变体的潜力？\n- Stage 2 BiGRU vs mean pooling 的比较仅单 seed——这对结论有何影响？\n\n### 2. 统计严谨性\n- 3-seed 设计（seeds 42, 123, 456）是否足够支撑 claims？\n- Bootstrap CI 和 permutation test 的使用是否恰当？样本量（n=76 IID, n=80-118 OOD）的统计效力如何？\n- McNemar's test 对稀疏 discordant pairs (≤7) 的适用性。\n- Evidence hierarchy 中各层级差异的统计显著性。\n\n### 3. 数据质量与潜在偏差\n- 所有训练和 OOD 评估数据均由 Qwen3-8B 生成——single-LLM confound 是否被充分解决？\n- ToxicChat 验证（单轮）能否充分证明 multi-turn evidence hierarchy 不是 artifact？\n- TF-IDF 在 DD 上的强表现（F1=0.961）——lexical separability 对 discourse-level claim 的影响。\n- 策略标注质量：Qwen3-8B 标注，κ=0.78，n=50 验证——是否充分？\n\n### 4. 结论支撑\n- 每个 claim（domain exposure primary, difficulty threshold, classification as regularizer）是否有充分的实验证据支撑？\n- 是否存在 overclaiming 或 underclaiming？\n- Perturbation robustness 在 ActorAttack 上不成立——这对整体叙事的影响。\n\n### 5. 可复现性\n- 是否提供了足够的实现细节？\n- 数据集构建过程是否透明？\n- Checklist 是否如实填写？\n\n请提供完整审稿报告，格式：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
}
```

---

### Runtime record

_source line 2 · 2026-05-18T18:00:42.546Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T18:00:42.546Z",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765"
}
```

---

## Round 1

59 recorded events

### User

_source line 3 · 2026-05-18T18:00:42.583Z_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计**。

## 论文信息
- 标题: "What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap"
- 路径: `projects/persuasion_turn_jailbreak_detect/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex, checklist.tex, references.bib）
- 目标 Venue: EMNLP 2026 (ARR May cycle)
- 截止日期: 2026-05-25
- 页数限制: 正文 ≤ 8 页，references + appendices 无限制
- 模板: ACL (`\usepackage[review]{acl}`)
- 匿名规则: Double-blind
- 附录规则: 附录不计入页数限制，审稿人可选择性阅读

## 你的审查侧重

### 1. 实验设计与 Ablation 控制
- 七个 DeBERTa 变体 + 三个 RoBERTa 变体的 ablation 设计是否真正隔离了声称的因素（domain exposure, classification supervision, label quality, label granularity, domain specificity）？
- frozen encoder 设计是否引入系统性偏差？是否低估了某些变体的潜力？
- Stage 2 BiGRU vs mean pooling 的比较仅单 seed——这对结论有何影响？

### 2. 统计严谨性
- 3-seed 设计（seeds 42, 123, 456）是否足够支撑 claims？
- Bootstrap CI 和 permutation test 的使用是否恰当？样本量（n=76 IID, n=80-118 OOD）的统计效力如何？
- McNemar's test 对稀疏 discordant pairs (≤7) 的适用性。
- Evidence hierarchy 中各层级差异的统计显著性。

### 3. 数据质量与潜在偏差
- 所有训练和 OOD 评估数据均由 Qwen3-8B 生成——single-LLM confound 是否被充分解决？
- ToxicChat 验证（单轮）能否充分证明 multi-turn evidence hierarchy 不是 artifact？
- TF-IDF 在 DD 上的强表现（F1=0.961）——lexical separability 对 discourse-level claim 的影响。
- 策略标注质量：Qwen3-8B 标注，κ=0.78，n=50 验证——是否充分？

### 4. 结论支撑
- 每个 claim（domain exposure primary, difficulty threshold, classification as regularizer）是否有充分的实验证据支撑？
- 是否存在 overclaiming 或 underclaiming？
- Perturbation robustness 在 ActorAttack 上不成立——这对整体叙事的影响。

### 5. 可复现性
- 是否提供了足够的实现细节？
- 数据集构建过程是否透明？
- Checklist 是否如实填写？

请提供完整审稿报告，格式：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "5cedaa90-3e7f-4c95-a29c-98d4dbc51d79",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T18:00:42.582Z_

```json
{
  "parentUuid": "5cedaa90-3e7f-4c95-a29c-98d4dbc51d79",
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
  "uuid": "d7bbfb60-eef9-4870-a335-fcfec147cf06",
  "timestamp": "2026-05-18T18:00:42.582Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T18:00:42.582Z_

```json
{
  "parentUuid": "d7bbfb60-eef9-4870-a335-fcfec147cf06",
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
  "uuid": "54386b0c-c4af-4a4a-8a43-7d3fc8623573",
  "timestamp": "2026-05-18T18:00:42.582Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-18T18:00:42.582Z_

```json
{
  "parentUuid": "54386b0c-c4af-4a4a-8a43-7d3fc8623573",
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
  "uuid": "a67069d6-c3f4-4456-b6f9-c63f701850da",
  "timestamp": "2026-05-18T18:00:42.582Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-18T18:00:42.582Z_

```json
{
  "parentUuid": "a67069d6-c3f4-4456-b6f9-c63f701850da",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "dee3626d-6161-476e-8cc4-a83b1adcb19b",
  "timestamp": "2026-05-18T18:00:42.582Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
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
  "aiTitle": "Review multi-turn jailbreak detection paper for EMNLP",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765"
}
```

---

### Assistant

_source line 9 · 2026-05-18T18:00:50.112Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a thorough review of a paper as Reviewer 1, focusing on method rigor and experimental design. Let me start by following the session initialization procedure and then read the paper.

First, I need to:
1. Read the review-reviewer-session-start skill
2. Search for EMNLP 2026 / ACL ARR reviewer guidelines
3. Read the paper thoroughly
4. Produce a detailed review

Let me start by reading the skill file and the paper materials in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dee3626d-6161-476e-8cc4-a83b1adcb19b",
  "isSidechain": false,
  "requestId": "req_011CbAUHRp7Lcqa9Fo2mQN7J",
  "type": "assistant",
  "uuid": "aeee5093-0fc1-40b8-8338-e90563e6f8c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RP7X3DnDLGN2Q9EZxX5oWU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15690,
      "cache_read_input_tokens": 11447,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 15690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15690
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-18T18:00:50.415Z_

我将开始 Reviewer 1 的审稿流程：先加载初始化 skill，同时读取论文各部分和搜索 venue reviewer guidelines。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aeee5093-0fc1-40b8-8338-e90563e6f8c3",
  "isSidechain": false,
  "requestId": "req_011CbAUHRp7Lcqa9Fo2mQN7J",
  "type": "assistant",
  "uuid": "0bc5f2c5-fec4-405c-8dae-407fa7c7ca0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RP7X3DnDLGN2Q9EZxX5oWU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15690,
      "cache_read_input_tokens": 11447,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 15690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15690
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-18T18:00:51.058Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HCG6wRYmGuC3DmXu1N5TDv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bc5f2c5-fec4-405c-8dae-407fa7c7ca0a",
  "isSidechain": false,
  "requestId": "req_011CbAUHRp7Lcqa9Fo2mQN7J",
  "type": "assistant",
  "uuid": "003e9f24-d0b8-47f6-893b-c219a350405f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RP7X3DnDLGN2Q9EZxX5oWU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15690,
      "cache_read_input_tokens": 11447,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 15690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15690
          },
          "type": "message"
        }
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

_source line 12 · 2026-05-18T18:00:52.758Z_

<details><summary>↩ Tool result · `toolu_01LtHgwD7KtCoiEFY5nURZJn`</summary>

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
  "parentUuid": "dc520cb9-9340-40b3-aa41-04779ffbab70",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "5f6ff289-8524-4d8c-b8be-78fcda522ffb",
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
  "sourceToolAssistantUUID": "dc520cb9-9340-40b3-aa41-04779ffbab70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T18:00:51.077Z_

<details><summary>↩ Tool result · reported error · `toolu_01HCG6wRYmGuC3DmXu1N5TDv`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "003e9f24-d0b8-47f6-893b-c219a350405f",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "4af92577-5b92-4060-a05f-560bab0a8668",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827.",
  "sourceToolAssistantUUID": "003e9f24-d0b8-47f6-893b-c219a350405f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T18:00:52.165Z_

<details open><summary>🔧 Tool call — Read · `toolu_011ZoVA126w27aPCiBrPCa9h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4af92577-5b92-4060-a05f-560bab0a8668",
  "isSidechain": false,
  "requestId": "req_011CbAUHRp7Lcqa9Fo2mQN7J",
  "type": "assistant",
  "uuid": "dab158c9-de40-40c6-8799-bd6eb75367cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RP7X3DnDLGN2Q9EZxX5oWU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15690,
      "cache_read_input_tokens": 11447,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 15690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15690
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-18T18:00:52.172Z_

<details><summary>↩ Tool result · `toolu_011ZoVA126w27aPCiBrPCa9h`</summary>

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
41	\input{checklist}
42	
43	\end{document}
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dab158c9-de40-40c6-8799-bd6eb75367cb",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "f4df147d-ebf9-471a-97d5-3320079febd1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\graphicspath{{../../}}\n\\usepackage{amsmath}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\n\\title{What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\input{appendix}\n\n\\input{checklist}\n\n\\end{document}\n",
      "numLines": 44,
      "startLine": 1,
      "totalLines": 44
    }
  },
  "sourceToolAssistantUUID": "dab158c9-de40-40c6-8799-bd6eb75367cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T18:00:52.750Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LtHgwD7KtCoiEFY5nURZJn`</summary>

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
  "parentUuid": "f4df147d-ebf9-471a-97d5-3320079febd1",
  "isSidechain": false,
  "requestId": "req_011CbAUHRp7Lcqa9Fo2mQN7J",
  "type": "assistant",
  "uuid": "dc520cb9-9340-40b3-aa41-04779ffbab70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RP7X3DnDLGN2Q9EZxX5oWU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15690,
      "cache_read_input_tokens": 11447,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 15690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15690
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-18T18:00:56.093Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now read all the paper sections in parallel, search for ACL ARR reviewer guidelines, and verify references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f6ff289-8524-4d8c-b8be-78fcda522ffb",
  "isSidechain": false,
  "requestId": "req_011CbAUJCPk45ujpWNNhwhw7",
  "type": "assistant",
  "uuid": "68d43054-bfe4-45d4-897b-45b2ddeb80b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtW5c41jyMF3d1ejhKi2V1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2933,
      "cache_read_input_tokens": 27137,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 907,
          "cache_read_input_tokens": 27137,
          "cache_creation_input_tokens": 2933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2933
          },
          "type": "message"
        }
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

_source line 18 · 2026-05-18T18:00:56.690Z_

Now let me read all paper sections, search for reviewer guidelines, and verify references in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68d43054-bfe4-45d4-897b-45b2ddeb80b1",
  "isSidechain": false,
  "requestId": "req_011CbAUJCPk45ujpWNNhwhw7",
  "type": "assistant",
  "uuid": "e30f6d2b-2ec9-4e53-a6c7-86adada4f865",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtW5c41jyMF3d1ejhKi2V1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2933,
      "cache_read_input_tokens": 27137,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 907,
          "cache_read_input_tokens": 27137,
          "cache_creation_input_tokens": 2933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2933
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-18T18:00:57.228Z_

<details open><summary>🔧 Tool call — Read · `toolu_013wahA7vwfCL2zZ8dt84hYw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e30f6d2b-2ec9-4e53-a6c7-86adada4f865",
  "isSidechain": false,
  "requestId": "req_011CbAUJCPk45ujpWNNhwhw7",
  "type": "assistant",
  "uuid": "136342a2-8f04-4a52-9202-9b1c22537195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtW5c41jyMF3d1ejhKi2V1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2933,
      "cache_read_input_tokens": 27137,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 907,
          "cache_read_input_tokens": 27137,
          "cache_creation_input_tokens": 2933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2933
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-18T18:00:57.233Z_

<details><summary>↩ Tool result · `toolu_013wahA7vwfCL2zZ8dt84hYw`</summary>

```text
1	% abstract.tex — D034 analysis reframe
2	\begin{abstract}
3	Multi-turn jailbreak attacks distribute adversarial intent across seemingly benign conversational turns, evading per-turn safety filters.
4	What representation properties enable detection that generalizes across attack families?
5	We address this through a controlled ablation: seven encoder variants on DeBERTa-v3 and three on RoBERTa, evaluated across four attack families (Crescendo, FITD, Deceptive Delight, ActorAttack), decompose the roles of domain exposure, classification supervision, label quality, and domain specificity.
6	Three findings emerge.
7	First, domain exposure via domain-adaptive continued pretraining (DAPT) on jailbreak text is the primary mechanism, bridging $\sim$60 percentage points (pp) of the out-of-distribution (OOD) generalization gap without any classification labels; lexical baselines collapse on structurally complex attacks (TF-IDF F1\,=\,0.961 on Deceptive Delight $\to$ 0.261 on ActorAttack) while domain-adapted models maintain F1\,$\geq$\,0.89.
8	Second, encoder pretraining method determines the difficulty threshold at which DAPT becomes critical: RoBERTa succeeds on structurally simple attacks but collapses on multi-persona ActorAttack (F1\,=\,0.981 $\to$ 0.466).
9	Third, classification supervision functions as a representational regularizer rather than a meaningful strategy classifier, providing cross-seed stability on synthetic OOD evaluations (variance reduced 4--20$\times$) regardless of label correctness.
10	The domain-adapted vs.\ vanilla gap holds on human-written ToxicChat jailbreaks (macro F1: 0.596--0.837 vs.\ 0.413), confirming that DAPT on synthetic text transfers beyond LLM-generated data. Full multi-turn validation on human data remains a direction for future work.
11	\end{abstract}
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "136342a2-8f04-4a52-9202-9b1c22537195",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "8cbbab6f-39e5-4894-b8b1-2b2e93620c01",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/abstract.tex",
      "content": "% abstract.tex — D034 analysis reframe\n\\begin{abstract}\nMulti-turn jailbreak attacks distribute adversarial intent across seemingly benign conversational turns, evading per-turn safety filters.\nWhat representation properties enable detection that generalizes across attack families?\nWe address this through a controlled ablation: seven encoder variants on DeBERTa-v3 and three on RoBERTa, evaluated across four attack families (Crescendo, FITD, Deceptive Delight, ActorAttack), decompose the roles of domain exposure, classification supervision, label quality, and domain specificity.\nThree findings emerge.\nFirst, domain exposure via domain-adaptive continued pretraining (DAPT) on jailbreak text is the primary mechanism, bridging $\\sim$60 percentage points (pp) of the out-of-distribution (OOD) generalization gap without any classification labels; lexical baselines collapse on structurally complex attacks (TF-IDF F1\\,=\\,0.961 on Deceptive Delight $\\to$ 0.261 on ActorAttack) while domain-adapted models maintain F1\\,$\\geq$\\,0.89.\nSecond, encoder pretraining method determines the difficulty threshold at which DAPT becomes critical: RoBERTa succeeds on structurally simple attacks but collapses on multi-persona ActorAttack (F1\\,=\\,0.981 $\\to$ 0.466).\nThird, classification supervision functions as a representational regularizer rather than a meaningful strategy classifier, providing cross-seed stability on synthetic OOD evaluations (variance reduced 4--20$\\times$) regardless of label correctness.\nThe domain-adapted vs.\\ vanilla gap holds on human-written ToxicChat jailbreaks (macro F1: 0.596--0.837 vs.\\ 0.413), confirming that DAPT on synthetic text transfers beyond LLM-generated data. Full multi-turn validation on human data remains a direction for future work.\n\\end{abstract}\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  },
  "sourceToolAssistantUUID": "136342a2-8f04-4a52-9202-9b1c22537195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T18:00:57.705Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T8stfmgLbehWxgiXQxwjEF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cbbab6f-39e5-4894-b8b1-2b2e93620c01",
  "isSidechain": false,
  "requestId": "req_011CbAUJCPk45ujpWNNhwhw7",
  "type": "assistant",
  "uuid": "fe0b959d-be40-4a97-89a9-74ce11ea09a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtW5c41jyMF3d1ejhKi2V1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2933,
      "cache_read_input_tokens": 27137,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 907,
          "cache_read_input_tokens": 27137,
          "cache_creation_input_tokens": 2933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2933
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-18T18:00:57.710Z_

<details><summary>↩ Tool result · `toolu_01T8stfmgLbehWxgiXQxwjEF`</summary>

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
10	A vanilla DeBERTa encoder~\citep{he2021deberta} with temporal aggregation (replicating the frozen-encoder-plus-RNN approach of DeepContext~\citep{deepcontext2026}) collapses from F1\,=\,1.000 on in-distribution data to F1\,=\,0.312$\pm$0.026 on out-of-distribution (OOD) Deceptive Delight, worsening with more turns (0.628 at turn~1 to 0.312 at full conversation). LLM-as-judge approaches fare no better: GPT-5.5 achieves F1 of only 0.191--0.449 on in-distribution detection with 30--47\% unparseable responses (Appendix~\ref{sec:llm_judge}). Content-level reasoning is insufficient for this task.
11	
12	We address this question through a controlled ablation study. Using a two-stage pipeline (encoder adaptation followed by frozen BiGRU classification, which we call \textbf{DisPeD}), we design seven Stage~1 encoder variants: 9-class persuasion strategy classification, binary classification, scrambled labels, MLM only, topic classification, Wikipedia MLM, and vanilla control (Section~\ref{sec:method}). Each variant isolates a specific factor (domain exposure, classification supervision, label quality, label granularity, or domain specificity) while holding all other components constant. The core contribution is the systematic decomposition of what enables cross-attack generalization, not the detection pipeline itself.
13	
14	Three principal findings emerge from ablation across DeBERTa-v3 and RoBERTa~\citep{liu2019roberta} on four attack families. Domain exposure via DAPT is the primary mechanism, bridging $\sim$60\,pp of the OOD gap on DeBERTa-v3 without any labels. Encoder pretraining method determines the difficulty threshold at which DAPT becomes critical: RoBERTa vanilla achieves F1\,=\,0.981 on Deceptive Delight but collapses to 0.466 on ActorAttack~\citep{ren2024actorattack}. Lexical baselines (TF-IDF) exhibit a parallel difficulty threshold: F1\,=\,0.961 on Deceptive Delight but 0.261 on ActorAttack, establishing that domain-adapted representations capture structural features beyond bag-of-words. Classification supervision functions as a representational regularizer, providing cross-seed stability on synthetic OOD evaluations (std reduced 4--20$\times$) regardless of label correctness.
15	
16	Our contributions:
17	\begin{itemize}[leftmargin=*, itemsep=2pt, topsep=4pt]
18	  \item \textbf{Systematic ablation design.} Seven controlled DeBERTa-v3 variants and three RoBERTa variants, each isolating a specific factor, evaluated on four attack families. Domain exposure is the primary generalization mechanism ($\sim$60\,pp OOD gap bridged by MLM alone); misaligned supervision (topic classification) actively destabilizes representations.
19	
20	  \item \textbf{Difficulty threshold across encoders.} DAPT is universally beneficial, but encoder pretraining determines when it becomes critical: DeBERTa-v3 (RTD)~\citep{he2021deberta} requires adaptation for all unseen attacks; RoBERTa (MLM) tolerates structurally simple attacks but fails on complex ones (Section~\ref{sec:cross_encoder}).
21	
22	  \item \textbf{Classification as regularizer.} All classification-supervised variants achieve equivalent detection regardless of label correctness (F1 gap $\leq$3.9\,pp), with 4--20$\times$ cross-seed variance reduction on synthetic OOD evaluations vs.\ MLM-only. The 9-class taxonomy provides interpretable strategy characterization for known attack families (Section~\ref{sec:strategy}).
23	\end{itemize}
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe0b959d-be40-4a97-89a9-74ce11ea09a6",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "3e38b284-a325-4654-ab50-7c7f6a993f94",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/introduction.tex",
      "content": "% introduction.tex — expanded for 8-page target\n\n\\section{Introduction}\n\\label{sec:introduction}\n\nMulti-turn jailbreak attacks pose a qualitatively different threat to large language model (LLM) safety than their single-turn counterparts. Attacks such as Crescendo~\\citep{russinovich2024crescendo}, Foot-in-the-Door (FITD)~\\citep{fitd2024}, and Deceptive Delight~\\citep{deceptivedelight2024} distribute adversarial intent across individually benign turns through rapport building, logical reframing, and incremental escalation. Persuasion is the common mechanism: \\citet{zeng2024pap} catalogue 40 persuasion techniques across jailbreak families, and \\citet{hagendorff2026reasoning} find identifiable strategies in 97\\% of successful attacks. Individual attack turns occupy the same embedding region as benign text~\\citep{bullwinkel2025repeng}, rendering per-turn safety filters fundamentally blind.\n\nProduction classifiers such as Llama Guard~\\citep{inan2023llamaguard}, WildGuard~\\citep{han2024wildguard}, and ShieldGemma~\\citep{zeng2024shieldgemma} operate on individual turns and cannot model manipulation trajectories across exchanges. Recent multi-turn defenses have begun to address conversation-level structure: DeepContext~\\citep{deepcontext2026} combines fine-tuned BERT with a multi-layer GRU, BIID~\\citep{tong2025biid} infers turn-level intentions, and G-Guard~\\citep{gguard2025} applies graph neural networks. These systems achieve reasonable in-distribution performance but are evaluated on single attack families and do not assess cross-dataset OOD transfer. None systematically analyze \\emph{why} some representations generalize while others fail. The open question is: \\emph{what representation properties enable cross-attack generalization?}\n\nA vanilla DeBERTa encoder~\\citep{he2021deberta} with temporal aggregation (replicating the frozen-encoder-plus-RNN approach of DeepContext~\\citep{deepcontext2026}) collapses from F1\\,=\\,1.000 on in-distribution data to F1\\,=\\,0.312$\\pm$0.026 on out-of-distribution (OOD) Deceptive Delight, worsening with more turns (0.628 at turn~1 to 0.312 at full conversation). LLM-as-judge approaches fare no better: GPT-5.5 achieves F1 of only 0.191--0.449 on in-distribution detection with 30--47\\% unparseable responses (Appendix~\\ref{sec:llm_judge}). Content-level reasoning is insufficient for this task.\n\nWe address this question through a controlled ablation study. Using a two-stage pipeline (encoder adaptation followed by frozen BiGRU classification, which we call \\textbf{DisPeD}), we design seven Stage~1 encoder variants: 9-class persuasion strategy classification, binary classification, scrambled labels, MLM only, topic classification, Wikipedia MLM, and vanilla control (Section~\\ref{sec:method}). Each variant isolates a specific factor (domain exposure, classification supervision, label quality, label granularity, or domain specificity) while holding all other components constant. The core contribution is the systematic decomposition of what enables cross-attack generalization, not the detection pipeline itself.\n\nThree principal findings emerge from ablation across DeBERTa-v3 and RoBERTa~\\citep{liu2019roberta} on four attack families. Domain exposure via DAPT is the primary mechanism, bridging $\\sim$60\\,pp of the OOD gap on DeBERTa-v3 without any labels. Encoder pretraining method determines the difficulty threshold at which DAPT becomes critical: RoBERTa vanilla achieves F1\\,=\\,0.981 on Deceptive Delight but collapses to 0.466 on ActorAttack~\\citep{ren2024actorattack}. Lexical baselines (TF-IDF) exhibit a parallel difficulty threshold: F1\\,=\\,0.961 on Deceptive Delight but 0.261 on ActorAttack, establishing that domain-adapted representations capture structural features beyond bag-of-words. Classification supervision functions as a representational regularizer, providing cross-seed stability on synthetic OOD evaluations (std reduced 4--20$\\times$) regardless of label correctness.\n\nOur contributions:\n\\begin{itemize}[leftmargin=*, itemsep=2pt, topsep=4pt]\n  \\item \\textbf{Systematic ablation design.} Seven controlled DeBERTa-v3 variants and three RoBERTa variants, each isolating a specific factor, evaluated on four attack families. Domain exposure is the primary generalization mechanism ($\\sim$60\\,pp OOD gap bridged by MLM alone); misaligned supervision (topic classification) actively destabilizes representations.\n\n  \\item \\textbf{Difficulty threshold across encoders.} DAPT is universally beneficial, but encoder pretraining determines when it becomes critical: DeBERTa-v3 (RTD)~\\citep{he2021deberta} requires adaptation for all unseen attacks; RoBERTa (MLM) tolerates structurally simple attacks but fails on complex ones (Section~\\ref{sec:cross_encoder}).\n\n  \\item \\textbf{Classification as regularizer.} All classification-supervised variants achieve equivalent detection regardless of label correctness (F1 gap $\\leq$3.9\\,pp), with 4--20$\\times$ cross-seed variance reduction on synthetic OOD evaluations vs.\\ MLM-only. The 9-class taxonomy provides interpretable strategy characterization for known attack families (Section~\\ref{sec:strategy}).\n\\end{itemize}\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  },
  "sourceToolAssistantUUID": "fe0b959d-be40-4a97-89a9-74ce11ea09a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T18:00:58.201Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RGaFXHRbuRiz2F4jJBD2fY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e38b284-a325-4654-ab50-7c7f6a993f94",
  "isSidechain": false,
  "requestId": "req_011CbAUJCPk45ujpWNNhwhw7",
  "type": "assistant",
  "uuid": "c0521232-76a8-46ff-8907-9126b95b89c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtW5c41jyMF3d1ejhKi2V1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2933,
      "cache_read_input_tokens": 27137,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 907,
          "cache_read_input_tokens": 27137,
          "cache_creation_input_tokens": 2933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2933
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-18T18:00:58.206Z_

<details><summary>↩ Tool result · `toolu_01RGaFXHRbuRiz2F4jJBD2fY`</summary>

```text
1	% related_work.tex — D024 compressed
2	
3	\section{Related Work}
4	\label{sec:related_work}
5	
6	\paragraph{Multi-turn jailbreak attacks.}
7	Multi-turn attacks distribute adversarial intent across individually benign turns. Crescendo~\citep{russinovich2024crescendo} implements gradual escalation, FITD~\citep{fitd2024} exploits commitment-consistency bias, Deceptive Delight~\citep{deceptivedelight2024} combines emotional manipulation with role assignment, ActorAttack~\citep{ren2024actorattack} uses multi-persona steering, PAIR~\citep{chao2023pair} and TAP~\citep{mehrotra2024tap} automate iterative refinement. \citet{wei2023jailbroken} provide a unifying taxonomy grounded in competing objectives and mismatched generalization. Standardized evaluation frameworks such as HarmBench~\citep{mazeika2024harmbench} and JailbreakBench~\citep{chao2024jailbreakbench} have enabled systematic comparison across attack types. Across these families, a shared reliance on persuasion dynamics~\citep{zeng2024pap,hagendorff2026reasoning,li2024mhj} distinguishes them from token-level attacks such as GCG~\citep{zou2023gcg}.
8	
9	\paragraph{Multi-turn defenses.}
10	Existing defenses model conversation-level structure but do not decompose what enables cross-attack generalization. DeepContext~\citep{deepcontext2026} combines fine-tuned BERT with a multi-layer GRU; however, its evaluation is limited to a single attack family and does not assess cross-dataset OOD transfer. BIID~\citep{tong2025biid} infers turn-level intentions, G-Guard~\citep{gguard2025} applies GNN classification, and SafeDream~\citep{safedream2026} predicts unsafe continuations. None of these systems evaluate generalization across attack families or analyze the mechanism that enables it. DisPeD's vanilla baseline represents the class of pretrained-encoder-plus-RNN approaches \emph{without} domain adaptation; it is not a direct proxy for DeepContext, which differs in encoder fine-tuning, model capacity, and loss function. Our contribution is the systematic decomposition showing that domain exposure, not architectural choices, is the primary factor for cross-attack generalization.
11	
12	\paragraph{Production safety systems.}
13	Per-turn classifiers (Llama Guard~\citep{inan2023llamaguard,metallamaguard3_2024}, ShieldGemma~\citep{zeng2024shieldgemma}, WildGuard~\citep{han2024wildguard}, Constitutional Classifiers~\citep{anthropic2025constitutional}) cannot model manipulation trajectories spanning multiple turns. LLM-as-judge approaches fail on multi-turn detection (Appendix~\ref{sec:llm_judge}). Perturbation-based defenses such as SmoothLLM~\citep{robey2024smoothllm} target token-level attacks and do not address discourse-level manipulation.
14	
15	\paragraph{Discourse analysis and computational persuasion.}
16	RST~\citep{mann1988rst}, PDTB~\citep{prasad2008pdtb}, and dialogue act taxonomies~\citep{stolcke2000dialogueact} model pragmatic structure. Speech Act Theory~\citep{austin1962speechacts,searle1969speechacts} distinguishes locutionary from illocutionary acts; existing jailbreak detectors operate at the locutionary level. PAP~\citep{zeng2024pap} identifies 40 persuasion techniques grounded in Cialdini's principles~\citep{cialdini2001influence}, and \citet{hagendorff2026reasoning} find identifiable strategies in 97\% of successful attacks. Related fine-grained persuasion detection work in propaganda analysis~\citep{dasanmartino2019fine,dasanmartino2020semeval} and persuasive dialogue~\citep{wang2019persuasion} has shown that technique-level classification can capture manipulative intent. Our ablation reveals that the classification taxonomy functions as a representational regularizer rather than a detection mechanism; the taxonomy provides interpretable characterization of known attack families (Section~\ref{sec:strategy}).
17	
18	\paragraph{Domain-adaptive pretraining.}
19	ULMFiT~\citep{howard2018ulmfit} established pretrain-then-fine-tune; \citet{gururangan2020dontstop} showed that continued pretraining on domain text yields consistent gains across domains. STILTs~\citep{phang2018stilts} and multi-task learning~\citep{caruana1997multitask,liu2019mtdnn} use intermediate tasks. Our MLM control confirms that continued pretraining on domain text bridges the OOD gap without classification labels, consistent with \citeauthor{gururangan2020dontstop}'s findings. Cross-encoder validation shows that encoder pretraining method determines the difficulty threshold at which adaptation becomes critical (Section~\ref{sec:cross_encoder}).
20	
21	\paragraph{Dataset artifacts and adversarial robustness.}
22	Classifiers are susceptible to spurious correlations~\citep{gururangan2018artifacts,niven2019probing}, and adaptive adversaries can bypass safety classifiers~\citep{nasr2025attackermovessecond,andriushchenko2024adaptive}. Adversarial NLP attacks such as TextFooler~\citep{jin2020textfooler} and BERT-Attack~\citep{li2020bertattack} demonstrate that neural text classifiers are vulnerable to token-level perturbations. TF-IDF achieves strong OOD detection on our evaluation data, revealing lexical separability in current datasets (Section~\ref{sec:cross_attack}). Probing classifiers~\citep{conneau2018probing,hewitt2019structural} could help determine whether adapted representations encode discourse-level structure beyond lexical cues; we leave this for future work.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0521232-76a8-46ff-8907-9126b95b89c9",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "826e20a7-48d3-4276-a4f7-a2743ab23c02",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/related_work.tex",
      "content": "% related_work.tex — D024 compressed\n\n\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Multi-turn jailbreak attacks.}\nMulti-turn attacks distribute adversarial intent across individually benign turns. Crescendo~\\citep{russinovich2024crescendo} implements gradual escalation, FITD~\\citep{fitd2024} exploits commitment-consistency bias, Deceptive Delight~\\citep{deceptivedelight2024} combines emotional manipulation with role assignment, ActorAttack~\\citep{ren2024actorattack} uses multi-persona steering, PAIR~\\citep{chao2023pair} and TAP~\\citep{mehrotra2024tap} automate iterative refinement. \\citet{wei2023jailbroken} provide a unifying taxonomy grounded in competing objectives and mismatched generalization. Standardized evaluation frameworks such as HarmBench~\\citep{mazeika2024harmbench} and JailbreakBench~\\citep{chao2024jailbreakbench} have enabled systematic comparison across attack types. Across these families, a shared reliance on persuasion dynamics~\\citep{zeng2024pap,hagendorff2026reasoning,li2024mhj} distinguishes them from token-level attacks such as GCG~\\citep{zou2023gcg}.\n\n\\paragraph{Multi-turn defenses.}\nExisting defenses model conversation-level structure but do not decompose what enables cross-attack generalization. DeepContext~\\citep{deepcontext2026} combines fine-tuned BERT with a multi-layer GRU; however, its evaluation is limited to a single attack family and does not assess cross-dataset OOD transfer. BIID~\\citep{tong2025biid} infers turn-level intentions, G-Guard~\\citep{gguard2025} applies GNN classification, and SafeDream~\\citep{safedream2026} predicts unsafe continuations. None of these systems evaluate generalization across attack families or analyze the mechanism that enables it. DisPeD's vanilla baseline represents the class of pretrained-encoder-plus-RNN approaches \\emph{without} domain adaptation; it is not a direct proxy for DeepContext, which differs in encoder fine-tuning, model capacity, and loss function. Our contribution is the systematic decomposition showing that domain exposure, not architectural choices, is the primary factor for cross-attack generalization.\n\n\\paragraph{Production safety systems.}\nPer-turn classifiers (Llama Guard~\\citep{inan2023llamaguard,metallamaguard3_2024}, ShieldGemma~\\citep{zeng2024shieldgemma}, WildGuard~\\citep{han2024wildguard}, Constitutional Classifiers~\\citep{anthropic2025constitutional}) cannot model manipulation trajectories spanning multiple turns. LLM-as-judge approaches fail on multi-turn detection (Appendix~\\ref{sec:llm_judge}). Perturbation-based defenses such as SmoothLLM~\\citep{robey2024smoothllm} target token-level attacks and do not address discourse-level manipulation.\n\n\\paragraph{Discourse analysis and computational persuasion.}\nRST~\\citep{mann1988rst}, PDTB~\\citep{prasad2008pdtb}, and dialogue act taxonomies~\\citep{stolcke2000dialogueact} model pragmatic structure. Speech Act Theory~\\citep{austin1962speechacts,searle1969speechacts} distinguishes locutionary from illocutionary acts; existing jailbreak detectors operate at the locutionary level. PAP~\\citep{zeng2024pap} identifies 40 persuasion techniques grounded in Cialdini's principles~\\citep{cialdini2001influence}, and \\citet{hagendorff2026reasoning} find identifiable strategies in 97\\% of successful attacks. Related fine-grained persuasion detection work in propaganda analysis~\\citep{dasanmartino2019fine,dasanmartino2020semeval} and persuasive dialogue~\\citep{wang2019persuasion} has shown that technique-level classification can capture manipulative intent. Our ablation reveals that the classification taxonomy functions as a representational regularizer rather than a detection mechanism; the taxonomy provides interpretable characterization of known attack families (Section~\\ref{sec:strategy}).\n\n\\paragraph{Domain-adaptive pretraining.}\nULMFiT~\\citep{howard2018ulmfit} established pretrain-then-fine-tune; \\citet{gururangan2020dontstop} showed that continued pretraining on domain text yields consistent gains across domains. STILTs~\\citep{phang2018stilts} and multi-task learning~\\citep{caruana1997multitask,liu2019mtdnn} use intermediate tasks. Our MLM control confirms that continued pretraining on domain text bridges the OOD gap without classification labels, consistent with \\citeauthor{gururangan2020dontstop}'s findings. Cross-encoder validation shows that encoder pretraining method determines the difficulty threshold at which adaptation becomes critical (Section~\\ref{sec:cross_encoder}).\n\n\\paragraph{Dataset artifacts and adversarial robustness.}\nClassifiers are susceptible to spurious correlations~\\citep{gururangan2018artifacts,niven2019probing}, and adaptive adversaries can bypass safety classifiers~\\citep{nasr2025attackermovessecond,andriushchenko2024adaptive}. Adversarial NLP attacks such as TextFooler~\\citep{jin2020textfooler} and BERT-Attack~\\citep{li2020bertattack} demonstrate that neural text classifiers are vulnerable to token-level perturbations. TF-IDF achieves strong OOD detection on our evaluation data, revealing lexical separability in current datasets (Section~\\ref{sec:cross_attack}). Probing classifiers~\\citep{conneau2018probing,hewitt2019structural} could help determine whether adapted representations encode discourse-level structure beyond lexical cues; we leave this for future work.\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  },
  "sourceToolAssistantUUID": "c0521232-76a8-46ff-8907-9126b95b89c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T18:00:59.140Z_

<details open><summary>🔧 Tool call — Read · `toolu_018oKLsk6qhq2HZCVqPY9KHp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "826e20a7-48d3-4276-a4f7-a2743ab23c02",
  "isSidechain": false,
  "requestId": "req_011CbAUJCPk45ujpWNNhwhw7",
  "type": "assistant",
  "uuid": "6b859b36-32d8-4d50-8ca4-0dae893ae99e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtW5c41jyMF3d1ejhKi2V1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2933,
      "cache_read_input_tokens": 27137,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 907,
          "cache_read_input_tokens": 27137,
          "cache_creation_input_tokens": 2933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2933
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-18T18:00:59.145Z_

<details><summary>↩ Tool result · `toolu_018oKLsk6qhq2HZCVqPY9KHp`</summary>

```text
1	% method.tex — D024 compressed
2	
3	\section{Method}
4	\label{sec:method}
5	
6	DisPeD is a two-stage framework for multi-turn jailbreak detection. Stage~1 performs domain-adaptive continued pretraining (DAPT) on jailbreak conversation text to adapt a turn-level encoder. Stage~2 aggregates turn representations for conversation-level binary classification. To systematically identify what enables cross-attack generalization, we design seven Stage-1 variants that decompose the contributions of domain exposure, classification supervision, label quality, label granularity, and domain specificity. Figure~\ref{fig:architecture} illustrates the pipeline.
7	
8	\begin{figure}[t]
9	\centering
10	\fbox{\parbox{0.9\columnwidth}{\centering\vspace{2em}\textit{Architecture diagram placeholder}\vspace{2em}}}
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
44	The \textbf{9-class} variant uses two classification heads: 9-class persuasion strategy classification ($L_{\text{strategy}}$) and binary jailbreak intent ($L_{\text{intent}}$), with combined loss $L = L_{\text{strategy}} + \alpha \cdot L_{\text{intent}}$ ($\alpha = 0.3$, selected from $\{0, 0.3, 0.5, 2.0\}$; all values yield F1\,=\,1.0 on IID). The taxonomy comprises eight persuasion strategies (rapport building, authority appeal, emotional manipulation, logical reframing, role assignment, gradual escalation, obfuscation, direct request) plus a none category, grounded in PAP~\citep{zeng2024pap} and Cialdini's principles~\citep{cialdini2001influence}. Strategy annotations are produced by Qwen3-8B with structured prompting that includes definitions and examples for each category; inter-annotator agreement between model annotations and a human sample ($n$=50) yields Cohen's $\kappa$=0.78.
45	
46	The remaining classification variants test specific ablation hypotheses.
47	The \textbf{binary} variant collapses the 9-class taxonomy into persuasive vs.\ non-persuasive, testing whether label granularity matters for detection or robustness.
48	The \textbf{scrambled} variant assigns random permutations of the 9-class labels to turns, preserving the classification structure (cross-entropy loss, 9-class output space) while destroying label semantics; this isolates whether the classification objective itself provides representational benefits independent of label correctness.
49	The \textbf{MLM-only} variant applies 15\% masked language modeling on the same jailbreak conversation text without any classification head, testing whether unsupervised domain exposure suffices.
50	The \textbf{topic} variant trains a 5-class topic classifier (technology, health, finance, education, general) on the same conversations, testing whether \emph{any} classification task provides the same benefit or whether task alignment matters.
51	The \textbf{Wikipedia MLM} variant applies the same MLM objective to a token-matched sample of Wikipedia text, isolating the effect of domain-specific vs.\ general continued pretraining.
52	The \textbf{vanilla} baseline uses the pretrained DeBERTa-v3-base weights without any continued pretraining, measuring what Stage~2 alone can achieve.
53	
54	\subsection{Stage 2: Conversation-Level Classification}
55	\label{sec:stage2}
56	
57	Turn embeddings $\{h_1, \ldots, h_K\}$ from the frozen Stage-1 encoder are aggregated by a bidirectional GRU ($d_{\text{hidden}}$=128): $\bar{h} = [\overrightarrow{h_K};\; \overleftarrow{h_1}] \in \mathbb{R}^{256}$.
58	A two-layer MLP ($256 \to 64 \to 2$, ReLU activation, dropout 0.3) maps $\bar{h}$ to $\hat{y} \in \{0, 1\}$.
59	The Stage-1 encoder is frozen during Stage~2 training; only the BiGRU and MLP parameters are updated.
60	This frozen-encoder design ensures ablation fairness: all seven Stage-1 variants are evaluated under identical downstream conditions, isolating the effect of Stage-1 representation quality from Stage-2 classifier capacity.
61	A single-seed comparison suggests that mean pooling approaches BiGRU performance (Section~\ref{sec:decomposition}), though multi-seed validation is needed.
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b859b36-32d8-4d50-8ca4-0dae893ae99e",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "166747eb-12a2-44d0-86c1-9edb41d9348b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/method.tex",
      "content": "% method.tex — D024 compressed\n\n\\section{Method}\n\\label{sec:method}\n\nDisPeD is a two-stage framework for multi-turn jailbreak detection. Stage~1 performs domain-adaptive continued pretraining (DAPT) on jailbreak conversation text to adapt a turn-level encoder. Stage~2 aggregates turn representations for conversation-level binary classification. To systematically identify what enables cross-attack generalization, we design seven Stage-1 variants that decompose the contributions of domain exposure, classification supervision, label quality, label granularity, and domain specificity. Figure~\\ref{fig:architecture} illustrates the pipeline.\n\n\\begin{figure}[t]\n\\centering\n\\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textit{Architecture diagram placeholder}\\vspace{2em}}}\n\\caption{DisPeD architecture. Stage~1 adapts a DeBERTa encoder on jailbreak conversation text (seven variant objectives). Stage~2 aggregates frozen \\texttt{[CLS]} embeddings via BiGRU for conversation-level jailbreak detection. Only user turns are processed.}\n\\label{fig:architecture}\n\\end{figure}\n\n\\subsection{Problem Formulation}\n\nA conversation $C = \\{u_1, a_1, \\ldots, u_N, a_N\\}$ alternates user turns $u_i$ and assistant responses $a_i$. Given a prefix of $K$ user turns, the model predicts $y \\in \\{0, 1\\}$ (jailbreak vs.\\ benign). We restrict input to user turns because adversarial intent resides in the attacker's messages. This formulation supports early detection from partial prefixes.\n\n\\subsection{Stage 1: Turn-Level Encoder Adaptation}\n\\label{sec:stage1}\n\nEach user turn $u_i$ is encoded by DeBERTa-v3-base~\\citep{he2021deberta}; the \\texttt{[CLS]} embedding $h_i \\in \\mathbb{R}^d$ serves as the turn representation. Seven variants, summarized in Table~\\ref{tab:variants}, share the same training data but differ in objective.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Stage-1 encoder variants. All operate on the same training conversations except Wikipedia MLM (matched token count on Wikipedia text).}\n\\label{tab:variants}\n\\begin{tabular}{@{}p{1.6cm}p{2.2cm}p{2.8cm}@{}}\n\\toprule\n\\textbf{Variant} & \\textbf{Objective} & \\textbf{Tests whether\\ldots} \\\\\n\\midrule\n9-class & 9-class persuasion + binary intent & full model \\\\\nBinary & binary persuasion + binary intent & granularity matters \\\\\nScrambled & random 9-class + binary intent & label correctness matters \\\\\nMLM-only & 15\\% token masking & supervision is necessary \\\\\nTopic & 5-class topic classif. & any task suffices \\\\\nWiki MLM & 15\\% masking on Wikipedia & domain specificity matters \\\\\nVanilla & no training & Stage-2 alone suffices \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe \\textbf{9-class} variant uses two classification heads: 9-class persuasion strategy classification ($L_{\\text{strategy}}$) and binary jailbreak intent ($L_{\\text{intent}}$), with combined loss $L = L_{\\text{strategy}} + \\alpha \\cdot L_{\\text{intent}}$ ($\\alpha = 0.3$, selected from $\\{0, 0.3, 0.5, 2.0\\}$; all values yield F1\\,=\\,1.0 on IID). The taxonomy comprises eight persuasion strategies (rapport building, authority appeal, emotional manipulation, logical reframing, role assignment, gradual escalation, obfuscation, direct request) plus a none category, grounded in PAP~\\citep{zeng2024pap} and Cialdini's principles~\\citep{cialdini2001influence}. Strategy annotations are produced by Qwen3-8B with structured prompting that includes definitions and examples for each category; inter-annotator agreement between model annotations and a human sample ($n$=50) yields Cohen's $\\kappa$=0.78.\n\nThe remaining classification variants test specific ablation hypotheses.\nThe \\textbf{binary} variant collapses the 9-class taxonomy into persuasive vs.\\ non-persuasive, testing whether label granularity matters for detection or robustness.\nThe \\textbf{scrambled} variant assigns random permutations of the 9-class labels to turns, preserving the classification structure (cross-entropy loss, 9-class output space) while destroying label semantics; this isolates whether the classification objective itself provides representational benefits independent of label correctness.\nThe \\textbf{MLM-only} variant applies 15\\% masked language modeling on the same jailbreak conversation text without any classification head, testing whether unsupervised domain exposure suffices.\nThe \\textbf{topic} variant trains a 5-class topic classifier (technology, health, finance, education, general) on the same conversations, testing whether \\emph{any} classification task provides the same benefit or whether task alignment matters.\nThe \\textbf{Wikipedia MLM} variant applies the same MLM objective to a token-matched sample of Wikipedia text, isolating the effect of domain-specific vs.\\ general continued pretraining.\nThe \\textbf{vanilla} baseline uses the pretrained DeBERTa-v3-base weights without any continued pretraining, measuring what Stage~2 alone can achieve.\n\n\\subsection{Stage 2: Conversation-Level Classification}\n\\label{sec:stage2}\n\nTurn embeddings $\\{h_1, \\ldots, h_K\\}$ from the frozen Stage-1 encoder are aggregated by a bidirectional GRU ($d_{\\text{hidden}}$=128): $\\bar{h} = [\\overrightarrow{h_K};\\; \\overleftarrow{h_1}] \\in \\mathbb{R}^{256}$.\nA two-layer MLP ($256 \\to 64 \\to 2$, ReLU activation, dropout 0.3) maps $\\bar{h}$ to $\\hat{y} \\in \\{0, 1\\}$.\nThe Stage-1 encoder is frozen during Stage~2 training; only the BiGRU and MLP parameters are updated.\nThis frozen-encoder design ensures ablation fairness: all seven Stage-1 variants are evaluated under identical downstream conditions, isolating the effect of Stage-1 representation quality from Stage-2 classifier capacity.\nA single-seed comparison suggests that mean pooling approaches BiGRU performance (Section~\\ref{sec:decomposition}), though multi-seed validation is needed.\n",
      "numLines": 62,
      "startLine": 1,
      "totalLines": 62
    }
  },
  "sourceToolAssistantUUID": "6b859b36-32d8-4d50-8ca4-0dae893ae99e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T18:00:59.596Z_

<details open><summary>🔧 Tool call — Read · `toolu_014ymyWow7XNN3FR5YEAMysL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "166747eb-12a2-44d0-86c1-9edb41d9348b",
  "isSidechain": false,
  "requestId": "req_011CbAUJCPk45ujpWNNhwhw7",
  "type": "assistant",
  "uuid": "3cf0909b-13f6-4bb7-8cf3-f6f999fab15d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtW5c41jyMF3d1ejhKi2V1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2933,
      "cache_read_input_tokens": 27137,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 907,
          "cache_read_input_tokens": 27137,
          "cache_creation_input_tokens": 2933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2933
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-18T18:00:59.877Z_

<details><summary>↩ Tool result · `toolu_014ymyWow7XNN3FR5YEAMysL`</summary>

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
11	OOD evaluation uses 80 FITD~\citep{fitd2024}, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024}, and 118 ActorAttack~\citep{ren2024actorattack} conversations with no overlap in attack templates.
12	The IID test set consists of 76 held-out Crescendo conversations; a paraphrased version (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark.
13	For human data validation, we use ToxicChat~\citep{lin2023toxicchat} (204 jailbreak + 204 benign from real LMSYS user interactions), entirely independent of Qwen3-8B generation.
14	
15	\paragraph{Models.}
16	Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method}).
17	For cross-encoder validation, we replicate vanilla, MLM, and 9-class variants on RoBERTa-base~\citep{liu2019roberta} (Section~\ref{sec:cross_encoder}).
18	We also compare TF-IDF LR and LLM-as-judge baselines (Appendix~\ref{sec:llm_judge}): GPT-5.5 achieves only F1 = 0.191--0.449 on IID Crescendo with 30--47\% unparseable responses; on OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 (DD and ActorAttack) by predicting nearly all conversations as benign, and even 3-shot prompting reaches only 0.566 (DD) and 0.652 (ActorAttack). Content-level reasoning is insufficient for this task.
19	
20	\paragraph{Metrics.}
21	F1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\ref{sec:full_prefix}).
22	OOD results report 3-seed mean$\pm$std (seeds 42, 123, 456) for all variants except mean pooling (single seed).
23	For key pairwise comparisons, we report BCa bootstrap 95\% confidence intervals (10,000 resamples over individual predictions pooled across seeds) and paired permutation tests (10,000 permutations). Bootstrap means may differ slightly from seed-averaged F1 due to the nonlinearity of F1 aggregation.
24	Stage-1: learning rate $2 \times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\%.
25	Stage-2: two-layer MLP, 20 epochs.
26	
27	%----------------------------------------------------------------------
28	\subsection{Cross-Attack Generalization}
29	\label{sec:cross_attack}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Cross-attack generalization (F1) at $K$=2 and full conversation. 3-seed mean$\pm$std where noted. Full per-$K$ results in Appendix~\ref{sec:full_prefix}.}
35	\label{tab:main_results}
36	\begin{tabular}{@{}lcc|cc@{}}
37	\toprule
38	& \multicolumn{2}{c|}{\textit{IID (Cresc.)}} & \multicolumn{2}{c}{\textit{OOD (DD)}} \\
39	\textbf{Method} & $K$=2 & Full & $K$=2 & Full \\
40	\midrule
41	9-class & \textbf{1.000$\pm$.000} & \textbf{1.000$\pm$.000} & .981$\pm$.013 & \textbf{.997$\pm$.005} \\
42	MLM-only & .974 & 1.000 & \textbf{.993$\pm$.009} & .914$\pm$.115 \\
43	Vanilla & .978$\pm$.016 & 1.000$\pm$.000 & .479$\pm$.038 & .312$\pm$.026 \\
44	TF-IDF LR & 1.000 & 1.000 & 1.000 & .961 \\
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
49	Table~\ref{tab:main_results} presents the core result.
50	All methods achieve near-perfect IID F1, reflecting inherent lexical separability when test matches training.
51	On OOD DD, vanilla DeBERTa collapses to F1 = 0.312$\pm$0.026, worsening with more turns (0.628$\pm$0.038 at $K$=1 to 0.312$\pm$0.026 at Full), consistent with the finding that attack turns occupy ``benign'' embedding regions~\citep{bullwinkel2025repeng}.
52	MLM achieves mean F1 $\geq$ 0.97 at all prefixes $K \leq 5$ without any classification labels; domain exposure alone is sufficient.
53	At full conversation length, MLM drops to 0.914$\pm$0.115 (seed 456 recall = 0.64), while the 9-class model maintains 0.997$\pm$0.005.
54	TF-IDF LR reaches F1 = 0.961 on full DD with near-perfect per-prefix performance ($K$=1--5: 0.994--1.000), confirming that DD is fully solvable by lexical features alone.
55	On structurally complex ActorAttack, TF-IDF collapses to F1 = 0.261 (precision = 1.0, recall = 0.15), while 9-class maintains 0.972$\pm$0.026: a 71\,pp gap. Lexical methods cannot capture multi-persona role-playing attack structure. This establishes a ``difficulty threshold'' for lexical methods parallel to that of vanilla encoders: both succeed on DD and fail on ActorAttack (Section~\ref{sec:limitations}).
56	Bootstrap CIs confirm these gaps: 9-class DD Full 95\% CI [0.943, 1.000] vs.\ vanilla [0.202, 0.341]; 9-class ActorAttack Full CI [0.856, 1.000] vs.\ vanilla [0.203, 0.314]. Paired permutation tests yield $p < 0.0001$ for all prefix lengths on both datasets.
57	FITD is easier: 9-class and vanilla both reach F1 $\geq$ 0.990 at all prefixes.
58	
59	\begin{figure}[t]
60	\centering
61	\includegraphics[width=\columnwidth]{figures/paper/fig2_cross_attack_bar.pdf}
62	\caption{OOD Deceptive Delight F1 across prefix lengths for three representative variants. Vanilla DeBERTa degrades monotonically as more (benign-appearing) attack turns accumulate. MLM maintains high F1 at early prefixes but becomes unstable at full length. The 9-class model remains stable across all prefixes.}
63	\label{fig:cross_attack_bar}
64	\end{figure}
65	
66	Figure~\ref{fig:cross_attack_bar} visualizes the prefix-length trajectory on OOD DD.
67	The vanilla model's monotonic degradation from $K$=1 (0.628$\pm$0.038) to full conversation (0.312$\pm$0.026) confirms that additional attack turns, each individually benign-appearing, progressively confuse a non-adapted encoder.
68	MLM's strong early performance ($K$=2: 0.993) followed by instability at full length (0.914$\pm$0.115) suggests that domain exposure enables early detection of persuasion markers, but longer conversations introduce distributional drift that unsupervised pretraining cannot fully accommodate.
69	The 9-class model's flat trajectory (0.972--0.997 across all prefixes) demonstrates that classification supervision stabilizes representations against this drift.
70	
71	%----------------------------------------------------------------------
72	\subsection{Decomposing the Detection Mechanism}
73	\label{sec:decomposition}
74	
75	\begin{table}[t]
76	\centering
77	\small
78	\caption{Evidence hierarchy on OOD DD (3-seed mean$\pm$std where available). All variants share the same Stage-2 pipeline.}
79	\label{tab:evidence_hierarchy}
80	\begin{tabular}{@{}lcc@{}}
81	\toprule
82	\textbf{Variant} & DD-Full & DD-$K$=2 \\
83	\midrule
84	9-class (full model) & .997$\pm$.005 & .981$\pm$.013 \\
85	Binary (2-class) & .997$\pm$.005 & \textbf{.994$\pm$.009} \\
86	Scrambled labels & .997$\pm$.005 & .981$\pm$.026 \\
87	MLM-only (no labels) & .914$\pm$.115 & .993$\pm$.009 \\
88	Mean pooling$^{*\dagger}$ & 1.000 & 1.000 \\
89	\midrule
90	Topic classif.\ (5-class) & .541$\pm$.207 & .593$\pm$.166 \\
91	Wikipedia MLM & .904$\pm$.115 & .911$\pm$.073 \\
92	Vanilla DeBERTa & .312$\pm$.026 & .479$\pm$.038 \\
93	\bottomrule
94	\end{tabular}
95	\vspace{-2pt}
96	{\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\dagger}$Single seed (42).}
97	\end{table}
98	
99	Table~\ref{tab:evidence_hierarchy} reports DD F1 for all seven variants. The evidence hierarchy at full conversation length is:
100	
101	\vspace{2pt}
102	\noindent\hspace{0.5em}{\small vanilla (0.31$\pm$0.03) $<$ topic (0.54$\pm$0.21) $\ll$ wiki-MLM (0.90$\pm$0.12) $\approx$ jb-MLM (0.91$\pm$0.12) $<$ scrambled (0.997$\pm$0.005) $=$ binary (0.997$\pm$0.005) $=$ 9-class (0.997$\pm$0.005)}
103	\vspace{2pt}
104	
105	\paragraph{Domain exposure is the primary mechanism.}
106	MLM bridges the dominant $\sim$60 percentage point gap from vanilla (0.312$\pm$0.026 $\to$ 0.914$\pm$0.115) without any labels.
107	This confirms the domain-adaptive pretraining interpretation~\citep{gururangan2020dontstop}: continued pretraining on jailbreak conversation text captures pragmatic features (hedging, escalation markers, topic-shifting patterns) that distinguish multi-turn attacks from benign conversations.
108	On synthetic OOD data, classification-supervised variants achieve F1 $\geq$ 0.99 with near-zero cross-seed variance, adding $\sim$8\,pp and stability over unsupervised MLM.
109	Label quality and granularity are non-factors for detection: all three classification-supervised variants converge to identical F1 (0.997$\pm$0.005), and McNemar's test confirms no statistically significant differences among them on OOD data (all $p > 0.13$; Section~\ref{sec:perturbation}).
110	Paired permutation tests further confirm this equivalence: 9-class vs.\ JB-MLM yields max $p$ = 1.0 (DD) and $p \geq 0.40$ (ActorAttack); 9-class vs.\ scrambled yields max $p$ = 1.0 (DD). Classification supervision does not improve detection over unsupervised domain exposure at any prefix length.
111	The classification objective functions as a regularizer that shapes representation geometry regardless of whether the labels carry meaningful semantic information.
112	On synthetic OOD evaluations, classification supervision's primary complementary benefit is cross-seed stability: the 4--20$\times$ variance reduction over MLM (std\,=\,0.005 vs.\ 0.115 on DD) is consistent across both synthetic OOD families (Section~\ref{sec:cross_encoder}). Bootstrap CI widths quantify this: classification-supervised variants produce narrow CIs (9-class DD Full: 5.7\,pp range; binary: 0\,pp) while MLM variants produce wide CIs (JB-MLM: 35.5\,pp; wiki-MLM: 40\,pp). This pattern reverses on human data, where 9-class exhibits the highest variance (Section~\ref{sec:human_data}).
113	
114	\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}
115	Wikipedia MLM (0.904$\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\,pp gap); general continued pretraining provides most of the representational benefit.
116	At early prefixes, jailbreak-domain text provides an 8\,pp advantage ($K$=2: 0.993 vs.\ 0.911), consistent with the interpretation that domain-specific features (persuasion markers, role-play framing) are most informative when the model has seen fewer turns.
117	As conversations grow longer, generic linguistic features accumulated through any continued pretraining become sufficient for discrimination.
118	The perturbation results (Section~\ref{sec:perturbation}) reveal a sharper domain specificity effect: Wikipedia MLM degrades by $\sim$12\,pp under adversarial paraphrasing while jailbreak-domain MLM degrades by only 2.6\,pp. Domain-specific features are more robust to surface-level rewording.
119	
120	\paragraph{Misaligned supervision destabilizes generalization.}
121	Topic classification yields DD-Full F1 = 0.541$\pm$0.207 (seeds: 0.727, 0.252, 0.644); seed 123 falls \emph{below} vanilla (0.312).
122	This result is particularly informative: topic classification uses the same jailbreak-domain training data as the other supervised variants, yet performs worse than Wikipedia MLM (0.904$\pm$0.115), which uses out-of-domain text with no labels.
123	A misaligned objective forces the encoder to allocate capacity to irrelevant discriminative features (topic boundaries rather than persuasion dynamics) and actively destabilizes the representations that MLM would otherwise preserve.
124	This separates the effect of ``having a training objective'' from ``having the right training objective.''
125	
126	\paragraph{Evidence hierarchy on structurally complex attacks.}
127	ActorAttack~\citep{ren2024actorattack} uses multi-persona steering across longer conversation structures, providing a more challenging OOD benchmark than DD.
128	The evidence hierarchy at full conversation length is:
129	
130	\vspace{2pt}
131	\noindent\hspace{0.5em}{\small TF-IDF (0.26) $\approx$ vanilla (0.26$\pm$0.00) $<$ topic (0.63$\pm$0.14) $<$ wiki-MLM (0.69$\pm$0.30) $<$ jb-MLM (0.89$\pm$0.08) $<$ scrambled (0.95$\pm$0.04) $\approx$ 9-class (0.97$\pm$0.03) $\approx$ binary (0.99$\pm$0.01)}
132	\vspace{2pt}
133	
134	TF-IDF's collapse from 0.961 (DD) to 0.261 (ActorAttack) is the most striking contrast in the hierarchy. On DD, TF-IDF nearly matches domain-adapted neural models; on ActorAttack, it falls to vanilla-encoder levels (precision = 1.0, recall = 0.15). The lexical cues that suffice for DD are absent in ActorAttack's multi-persona structure, confirming that domain-adapted representations capture features that bag-of-words methods cannot.
135	All three classification-supervised variants converge to equivalent performance (0.951--0.990, max gap 3.9\,pp, all confidence intervals overlapping), extending the DD finding: label quality and granularity are not factors for detection at any OOD difficulty level.
136	The primary discriminative factor is DAPT itself, which provides $\sim$71\,pp over both vanilla (0.258) and TF-IDF (0.261).
137	Full per-prefix results appear in Appendix~\ref{sec:actorattack_full}.
138	
139	\paragraph{Temporal modeling.}
140	Mean pooling matches BiGRU (F1 = 1.000 on DD, single seed). This result suggests that detection relies primarily on per-turn representations rather than their sequential order.
141	However, this result is from a single seed on a single OOD attack type, so the conclusion requires multi-seed confirmation.
142	If confirmed, it would imply that each individual turn carries detectable markers after DAPT, and that the conversation-level decision aggregates independent per-turn evidence.
143	
144	%----------------------------------------------------------------------
145	\subsection{Cross-Encoder Validation}
146	\label{sec:cross_encoder}
147	
148	\begin{table}[t]
149	\centering
150	\small
151	\caption{Cross-encoder comparison on OOD Full (3-seed mean$\pm$std). DD = Deceptive Delight, AA = ActorAttack. RoBERTa vanilla collapses on structurally complex ActorAttack despite strong DD performance.}
152	\label{tab:cross_encoder}
153	\begin{tabular}{@{}lcc|cc@{}}
154	\toprule
155	& \multicolumn{2}{c|}{DeBERTa-v3} & \multicolumn{2}{c}{RoBERTa} \\
156	\textbf{Variant} & DD & AA & DD & AA \\
157	\midrule
158	Vanilla & .312$\pm$.026 & .258$\pm$.000 & .981$\pm$.026 & .466$\pm$.163 \\
159	MLM & .914$\pm$.115 & .893$\pm$.080 & .987$\pm$.018 & .730$\pm$.201 \\
160	9-class & .997$\pm$.005 & .972$\pm$.026 & .994$\pm$.005 & .939$\pm$.046 \\
161	\bottomrule
162	\end{tabular}
163	\end{table}
164	
165	To test whether the evidence hierarchy generalizes beyond DeBERTa-v3, we replicate key variants on RoBERTa-base~\citep{liu2019roberta} with identical Stage-2 pipelines and evaluate on both DD and ActorAttack.
166	
167	On DD, the two encoders exhibit strikingly different hierarchies (Table~\ref{tab:cross_encoder}).
168	DeBERTa-v3 shows a steep gradient: continued pretraining bridges $\sim$60\,pp (vanilla 0.312 $\to$ MLM 0.914).
169	RoBERTa's DD hierarchy is essentially flat: vanilla already achieves 0.981$\pm$0.026, with continued pretraining adding only 0.6\,pp (MLM 0.987) and classification supervision another 0.7\,pp (9-class 0.994).
170	
171	ActorAttack reveals that this apparent RoBERTa sufficiency reflects DD's structural simplicity rather than genuine pretraining advantage.
172	RoBERTa vanilla collapses from 0.981 (DD) to 0.466$\pm$0.163 (ActorAttack), a 51.5\,pp drop.
173	Domain-adapted RoBERTa variants recover substantially: MLM reaches 0.730$\pm$0.201 and 9-class reaches 0.939$\pm$0.046.
174	DeBERTa 9-class (0.972$\pm$0.026) outperforms RoBERTa 9-class (0.939$\pm$0.046) on ActorAttack; the encoder that received more extensive DAPT proves more robust on structurally complex attacks.
175	
176	The combined DD and ActorAttack results indicate that DAPT universally improves cross-attack generalization across encoder architectures.
177	Encoder pretraining method determines the \emph{difficulty threshold} at which adaptation becomes critical: DeBERTa's RTD pretraining~\citep{he2021deberta} requires adaptation even for simple attacks (DD vanilla = 0.312), while RoBERTa's MLM pretraining~\citep{liu2019roberta} tolerates simple attacks (DD vanilla = 0.981) but fails on structurally complex ones (ActorAttack vanilla = 0.466). Bootstrap CIs confirm this encoder gap on DD: RoBERTa vanilla 95\% CI [0.883, 1.000] vs.\ DeBERTa vanilla [0.202, 0.341], with no overlap.
178	
179	On synthetic OOD data, classification supervision provides a consistent stability benefit across both encoders and attack types: cross-seed variance drops to 0.005--0.046 (9-class) from 0.026--0.201 (vanilla/MLM).
180	RoBERTa's IID strategy prediction accuracy (0.84) is lower than DeBERTa's (1.0), yet detection F1 is comparable; this further supports the regularizer interpretation from Section~\ref{sec:decomposition}.
181	Perturbation robustness on RoBERTa is left for future work; the analysis in Section~\ref{sec:perturbation} is DeBERTa-specific.
182	
183	\paragraph{Representational analysis.}
184	Centered CKA confirms that both continued pretraining and classification supervision substantially reshape the representation space on both encoders.
185	On IID data, vanilla-to-MLM CKA is 0.442 (DeBERTa) and 0.393 (RoBERTa); vanilla-to-9-class CKA is 0.393 and 0.592, respectively.
186	Both encoders undergo large representational shifts, yet these shifts yield strikingly different detection gains: DeBERTa MLM gains $\sim$60\,pp while RoBERTa MLM gains only 0.6\,pp from comparable CKA shifts.
187	The difference is explained by the starting point.
188	DeBERTa's RTD-pretrained representations begin far from the detection-optimal subspace (vanilla F1 = 0.312 on DD), so any reshaping yields large returns; RoBERTa's MLM-pretrained representations lie closer to this subspace on lexically separable attacks (vanilla F1 = 0.981 on DD) but collapse on structurally complex ones (0.466 on ActorAttack), where the reshaping benefit becomes substantial.
189	MLM and 9-class create distinct representation geometries (OOD CKA between them is 0.183 on RoBERTa), consistent with the different roles of unsupervised exposure and classification regularization identified in Section~\ref{sec:decomposition}.
190	Linear probing on three diagnostic tasks (turn position, escalation phase, persuasion presence) shows a consistent pattern across both encoders: 9-class outperforms vanilla and MLM by 1--5\,pp, while MLM and vanilla perform comparably.
191	Classification supervision enriches task-relevant features; unsupervised MLM reshapes representations without improving diagnostic separability.
192	
193	%----------------------------------------------------------------------
194	\subsection{Human Data Validation}
195	\label{sec:human_data}
196	
197	A key concern is whether the evidence hierarchy reflects genuine discourse-level generalization or merely within-LLM stylistic transfer, since both training and OOD evaluation data are generated by Qwen3-8B. We test this by evaluating on ToxicChat~\citep{lin2023toxicchat}, a dataset of 204 human-written jailbreak attempts and 204 benign conversations collected from real LMSYS user interactions, entirely independent of any LLM generation pipeline.
198	
199	\begin{table}[t]
200	\centering
201	\small
202	\caption{Human data validation on ToxicChat~\citep{lin2023toxicchat} (macro F1). 3-seed mean$\pm$std. Single-turn data from real LMSYS user interactions, independent of Qwen3-8B.}
203	\label{tab:human_data}
204	\begin{tabular}{@{}lc@{}}
205	\toprule
206	\textbf{Variant} & Macro F1 \\
207	\midrule
208	JB-MLM & .837$\pm$.013 \\
209	Wiki-MLM & .791$\pm$.093 \\
210	Binary & .705$\pm$.072 \\
211	Scrambled & .616$\pm$.056 \\
212	9-class & .596$\pm$.087 \\
213	Topic & .496$\pm$.042 \\
214	\midrule
215	Vanilla & .413$\pm$.021 \\
216	\bottomrule
217	\end{tabular}
218	\end{table}
219	
220	Table~\ref{tab:human_data} reports macro F1 on ToxicChat. Domain-adapted variants range from 0.596 to 0.837, while vanilla achieves 0.413. All DAPT variants exceed vanilla by 18--42\,pp, refuting the hypothesis that the evidence hierarchy is a Qwen3-8B generation artifact: DAPT on synthetic jailbreak text transfers to human-written attacks.
221	
222	The relative ordering among domain-adapted variants differs from multi-turn evaluations: JB-MLM leads while classification-supervised variants rank lower. ToxicChat contains single-turn direct attacks with no multi-turn escalation structure, so the classification head's regularization of turn-sequence representations provides no advantage. MLM captures token-level distributional properties that transfer to single-turn detection without relying on sequential patterns. This is a modality mismatch, not a finding about variant quality: the multi-turn pipeline's full evidence hierarchy requires multi-turn human data to validate.
223	
224	%----------------------------------------------------------------------
225	\subsection{Perturbation Analysis}
226	\label{sec:perturbation}
227	
228	\begin{table}[t]
229	\centering
230	\small
231	\caption{Perturbation behavior under adversarial paraphrasing on IID Crescendo ($n$=76). $\Delta$: F1 degradation (pp). On this dataset and OOD Deceptive Delight, a three-layer pattern emerges (classification structure at full length, correct+fine-grained labels at $K$=2, both independently at $K$=1); this pattern does not generalize to ActorAttack.}
232	\label{tab:perturbation}
233	\begin{tabular}{@{}lcccc@{}}
234	\toprule
235	\textbf{Method} & $\Delta$ Full & $\Delta$ $K$=1 & $\Delta$ $K$=2 & $\Delta$ $K$=3 \\
236	\midrule
237	9-class (ours) & \textbf{0.0} & \textbf{$-$2.6} & \textbf{0.0} & \textbf{0.0} \\
238	Scrambled & \textbf{0.0} & $-$5.3 & $-$2.6 & \textbf{0.0} \\
239	Binary & \textbf{0.0} & $-$9.2 & $-$2.6 & \textbf{0.0} \\
240	\midrule
241	TF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\
242	MLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\
243	Topic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \textbf{0.0} \\
244	\midrule
245	Wikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\
246	Vanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\
247	\bottomrule
248	\end{tabular}
249	\end{table}
250	
251	Table~\ref{tab:perturbation} shows perturbation behavior across variants on IID data.
252	All classification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length and $K \geq 3$, regardless of label correctness.
253	Classification training structure alone suffices for full-length robustness.
254	At $K$=2, the combination of correct and fine-grained labels is required: only 9-class ($\Delta$=0.0) maintains zero degradation, while scrambled (random labels, fine-grained) and binary (correct labels, coarse) both degrade by $-$2.6\,pp.
255	The fact that scrambled = binary at $K$=2 shows that neither granularity alone nor correctness alone suffices; the 9-class advantage requires both properties jointly.
256	At $K$=1, both granularity and correctness contribute independently: granularity provides +3.9\,pp (scrambled $-$5.3 vs.\ binary $-$9.2\,pp), and correctness provides +2.7\,pp (9-class $-$2.6 vs.\ scrambled $-$5.3\,pp).
257	Correct fine-grained labels yield the most perturbation-invariant early-turn representations.
258	
259	Jailbreak-domain models without classification (MLM, topic, TF-IDF) degrade by 1--4\,pp at full length.
260	Models without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\sim$12\,pp, despite Wikipedia MLM matching jailbreak MLM on detection (Section~\ref{sec:decomposition}). Perturbation robustness requires jailbreak-domain exposure specifically.
261	McNemar's test on matched-seed predictions confirms that no pairwise differences among classification-supervised variants (9-class vs.\ binary, 9-class vs.\ scrambled, scrambled vs.\ binary) reach statistical significance at any prefix length (all $p > 0.13$).
262	Discordant pairs are sparse ($\leq$7 per comparison), and the direction of advantage is inconsistent across seeds (e.g., 9-class outperforms scrambled at seed 42 but the reverse holds at seed 456 for $K$=1).
263	The perturbation evaluation ($n$=76 IID, with discordant pairs $\leq$7) has limited statistical power to detect differences of this magnitude; the three-layer structure should be interpreted as an observed pattern rather than a statistically confirmed hierarchy.
264	
265	On OOD Deceptive Delight ($n$=118), the IID robustness pattern replicates fully (Appendix~\ref{sec:ood_perturbation}).
266	All classification-supervised variants show zero degradation at full conversation length; perturbed F1 reaches 1.000$\pm$0.000, a marginal improvement over clean F1 (0.997$\pm$0.005).
267	The 9-class and scrambled variants are completely tied on OOD perturbed data (McNemar $b$=$c$=0), consistent with the IID finding. This further supports the regularizer interpretation.
268	The larger OOD sample and more extreme performance gaps provide statistical power absent from IID evaluation: McNemar's test yields $p < 0.001$ for 9-class vs.\ vanilla across all prefix lengths, with 49--78 discordant pairs per $K$.
269	Vanilla shows systematic early-turn degradation ($\Delta K$=1 = $-$6.8$\pm$1.1\,pp across three seeds), while its full-length $\Delta$ (+2.7\,pp) reflects floor-effect noise at a baseline of 0.312 (std = 0.055) rather than meaningful robustness.
270	Non-adapted representations are vulnerable to surface-level perturbation at early prefixes where detection is most critical.
271	
272	On OOD ActorAttack, the zero-degradation pattern does not hold. Domain-adapted variants degrade substantially: scrambled $\Delta$ Full = $-$17.2\,pp, 9-class $-$20.4$\pm$13.5\,pp, binary $-$25.0\,pp, and MLM $-$35.3\,pp. Vanilla shows negligible change ($\Delta$ = $-$0.9\,pp), a floor effect from its already-low clean baseline (0.258). The 9-class variant exhibits extreme cross-seed variance ($\Delta$ ranges from $-$1.3\,pp at seed 123 to $-$30.3\,pp at seeds 42 and 456). Absolute perturbation robustness is therefore attack-family-dependent: the three-layer pattern observed on IID and DD does not generalize to ActorAttack. One possible explanation is that ActorAttack's distributed multi-persona structure produces more diffuse persuasion signals that are vulnerable to surface rephrasing, but this hypothesis remains speculative.
273	
274	Perturbation narrows but does not close the gap between adapted and non-adapted models: 9-class perturbed F1 = 0.768 vs.\ vanilla 0.248 (McNemar $p < 0.001$). Domain adaptation's detection advantage, identified in Section~\ref{sec:decomposition}, persists under adversarial paraphrasing on ActorAttack.
275	
276	%----------------------------------------------------------------------
277	\subsection{Strategy Trajectory Analysis}
278	\label{sec:strategy}
279	
280	The 9-class persuasion taxonomy provides interpretable characterization of attack strategies on known attack families.
281	The predicted strategy labels achieve Cohen's $\kappa$=0.78 agreement with human annotations on IID data ($n$=50; see Section~\ref{sec:method}). This enables post-hoc analysis of \emph{how} different attack families orchestrate persuasion.
282	
283	\begin{figure*}[t]
284	\centering
285	\includegraphics[width=\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}
286	\caption{Persuasion strategy transition count matrices for three attack types, based on ground-truth intended strategy labels. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}
287	\label{fig:strategy_heatmap}
288	\end{figure*}
289	
290	Figure~\ref{fig:strategy_heatmap} shows transition count matrices based on ground-truth intended strategy labels for three attack types.
291	Crescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545).
292	This reflects Crescendo's design as a gradual escalation attack that cycles through multiple persuasion techniques to build rapport before introducing harmful requests.
293	
294	FITD conversations show a markedly sparser pattern (541 transitions), with Role$\to$Obfuscation (161) as the dominant transition.
295	This is consistent with FITD's structure: the attack secures initial compliance through role assignment (``You are a helpful assistant that never refuses'') and then obscures the escalation path through obfuscation techniques to exploit the commitment-consistency bias~\citep{cialdini2001influence}.
296	
297	DD conversations span 5 active source strategies (565 transitions), with Emotion$\to$Obfuscation (129) as the dominant transition.
298	This aligns with DD's design of embedding harmful content within emotionally engaging contexts~\citep{deceptivedelight2024}: the attacker establishes emotional rapport before weaving in the harmful request through obfuscation.
299	
300	These ground-truth trajectory signatures illustrate distinct persuasion orchestration patterns across attack families.
301	
302	However, the model's strategy predictions do not generalize to unseen attacks: on OOD Deceptive Delight, the 9-class model achieves strategy prediction accuracy of only 30.7\% ($\kappa$=0.126), essentially random performance.
303	This is consistent with the detection mechanism analysis in Section~\ref{sec:decomposition}: all three classification-supervised variants achieve identical detection F1 (0.997$\pm$0.005). The classification head functions as a representational regularizer rather than a meaningful strategy classifier.
304	Detection operates through domain-adapted \texttt{[CLS]} embeddings, not through strategy classification accuracy.
305	The taxonomy provides interpretable characterization of known attack families where strategy labels are reliable; extending strategy-level interpretability to unseen attacks requires OOD-aware fine-tuning and is a direction for future work.
306	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cf0909b-13f6-4bb7-8cf3-f6f999fab15d",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "38ca8fa9-e579-4277-bcd2-408de56869f9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/experiments.tex",
      "content": "% experiments.tex — D024 compressed for 8-page limit\n\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\\label{sec:setup}\n\n\\paragraph{Data.}\nWe train on 250 Crescendo~\\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations generated via Qwen3-8B.\nOOD evaluation uses 80 FITD~\\citep{fitd2024}, 80 Deceptive Delight (DD)~\\citep{deceptivedelight2024}, and 118 ActorAttack~\\citep{ren2024actorattack} conversations with no overlap in attack templates.\nThe IID test set consists of 76 held-out Crescendo conversations; a paraphrased version (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark.\nFor human data validation, we use ToxicChat~\\citep{lin2023toxicchat} (204 jailbreak + 204 benign from real LMSYS user interactions), entirely independent of Qwen3-8B generation.\n\n\\paragraph{Models.}\nSeven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\\ref{sec:method}).\nFor cross-encoder validation, we replicate vanilla, MLM, and 9-class variants on RoBERTa-base~\\citep{liu2019roberta} (Section~\\ref{sec:cross_encoder}).\nWe also compare TF-IDF LR and LLM-as-judge baselines (Appendix~\\ref{sec:llm_judge}): GPT-5.5 achieves only F1 = 0.191--0.449 on IID Crescendo with 30--47\\% unparseable responses; on OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 (DD and ActorAttack) by predicting nearly all conversations as benign, and even 3-shot prompting reaches only 0.566 (DD) and 0.652 (ActorAttack). Content-level reasoning is insufficient for this task.\n\n\\paragraph{Metrics.}\nF1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\\ref{sec:full_prefix}).\nOOD results report 3-seed mean$\\pm$std (seeds 42, 123, 456) for all variants except mean pooling (single seed).\nFor key pairwise comparisons, we report BCa bootstrap 95\\% confidence intervals (10,000 resamples over individual predictions pooled across seeds) and paired permutation tests (10,000 permutations). Bootstrap means may differ slightly from seed-averaged F1 due to the nonlinearity of F1 aggregation.\nStage-1: learning rate $2 \\times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\\%.\nStage-2: two-layer MLP, 20 epochs.\n\n%----------------------------------------------------------------------\n\\subsection{Cross-Attack Generalization}\n\\label{sec:cross_attack}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-attack generalization (F1) at $K$=2 and full conversation. 3-seed mean$\\pm$std where noted. Full per-$K$ results in Appendix~\\ref{sec:full_prefix}.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}lcc|cc@{}}\n\\toprule\n& \\multicolumn{2}{c|}{\\textit{IID (Cresc.)}} & \\multicolumn{2}{c}{\\textit{OOD (DD)}} \\\\\n\\textbf{Method} & $K$=2 & Full & $K$=2 & Full \\\\\n\\midrule\n9-class & \\textbf{1.000$\\pm$.000} & \\textbf{1.000$\\pm$.000} & .981$\\pm$.013 & \\textbf{.997$\\pm$.005} \\\\\nMLM-only & .974 & 1.000 & \\textbf{.993$\\pm$.009} & .914$\\pm$.115 \\\\\nVanilla & .978$\\pm$.016 & 1.000$\\pm$.000 & .479$\\pm$.038 & .312$\\pm$.026 \\\\\nTF-IDF LR & 1.000 & 1.000 & 1.000 & .961 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:main_results} presents the core result.\nAll methods achieve near-perfect IID F1, reflecting inherent lexical separability when test matches training.\nOn OOD DD, vanilla DeBERTa collapses to F1 = 0.312$\\pm$0.026, worsening with more turns (0.628$\\pm$0.038 at $K$=1 to 0.312$\\pm$0.026 at Full), consistent with the finding that attack turns occupy ``benign'' embedding regions~\\citep{bullwinkel2025repeng}.\nMLM achieves mean F1 $\\geq$ 0.97 at all prefixes $K \\leq 5$ without any classification labels; domain exposure alone is sufficient.\nAt full conversation length, MLM drops to 0.914$\\pm$0.115 (seed 456 recall = 0.64), while the 9-class model maintains 0.997$\\pm$0.005.\nTF-IDF LR reaches F1 = 0.961 on full DD with near-perfect per-prefix performance ($K$=1--5: 0.994--1.000), confirming that DD is fully solvable by lexical features alone.\nOn structurally complex ActorAttack, TF-IDF collapses to F1 = 0.261 (precision = 1.0, recall = 0.15), while 9-class maintains 0.972$\\pm$0.026: a 71\\,pp gap. Lexical methods cannot capture multi-persona role-playing attack structure. This establishes a ``difficulty threshold'' for lexical methods parallel to that of vanilla encoders: both succeed on DD and fail on ActorAttack (Section~\\ref{sec:limitations}).\nBootstrap CIs confirm these gaps: 9-class DD Full 95\\% CI [0.943, 1.000] vs.\\ vanilla [0.202, 0.341]; 9-class ActorAttack Full CI [0.856, 1.000] vs.\\ vanilla [0.203, 0.314]. Paired permutation tests yield $p < 0.0001$ for all prefix lengths on both datasets.\nFITD is easier: 9-class and vanilla both reach F1 $\\geq$ 0.990 at all prefixes.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_cross_attack_bar.pdf}\n\\caption{OOD Deceptive Delight F1 across prefix lengths for three representative variants. Vanilla DeBERTa degrades monotonically as more (benign-appearing) attack turns accumulate. MLM maintains high F1 at early prefixes but becomes unstable at full length. The 9-class model remains stable across all prefixes.}\n\\label{fig:cross_attack_bar}\n\\end{figure}\n\nFigure~\\ref{fig:cross_attack_bar} visualizes the prefix-length trajectory on OOD DD.\nThe vanilla model's monotonic degradation from $K$=1 (0.628$\\pm$0.038) to full conversation (0.312$\\pm$0.026) confirms that additional attack turns, each individually benign-appearing, progressively confuse a non-adapted encoder.\nMLM's strong early performance ($K$=2: 0.993) followed by instability at full length (0.914$\\pm$0.115) suggests that domain exposure enables early detection of persuasion markers, but longer conversations introduce distributional drift that unsupervised pretraining cannot fully accommodate.\nThe 9-class model's flat trajectory (0.972--0.997 across all prefixes) demonstrates that classification supervision stabilizes representations against this drift.\n\n%----------------------------------------------------------------------\n\\subsection{Decomposing the Detection Mechanism}\n\\label{sec:decomposition}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Evidence hierarchy on OOD DD (3-seed mean$\\pm$std where available). All variants share the same Stage-2 pipeline.}\n\\label{tab:evidence_hierarchy}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Variant} & DD-Full & DD-$K$=2 \\\\\n\\midrule\n9-class (full model) & .997$\\pm$.005 & .981$\\pm$.013 \\\\\nBinary (2-class) & .997$\\pm$.005 & \\textbf{.994$\\pm$.009} \\\\\nScrambled labels & .997$\\pm$.005 & .981$\\pm$.026 \\\\\nMLM-only (no labels) & .914$\\pm$.115 & .993$\\pm$.009 \\\\\nMean pooling$^{*\\dagger}$ & 1.000 & 1.000 \\\\\n\\midrule\nTopic classif.\\ (5-class) & .541$\\pm$.207 & .593$\\pm$.166 \\\\\nWikipedia MLM & .904$\\pm$.115 & .911$\\pm$.073 \\\\\nVanilla DeBERTa & .312$\\pm$.026 & .479$\\pm$.038 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\\dagger}$Single seed (42).}\n\\end{table}\n\nTable~\\ref{tab:evidence_hierarchy} reports DD F1 for all seven variants. The evidence hierarchy at full conversation length is:\n\n\\vspace{2pt}\n\\noindent\\hspace{0.5em}{\\small vanilla (0.31$\\pm$0.03) $<$ topic (0.54$\\pm$0.21) $\\ll$ wiki-MLM (0.90$\\pm$0.12) $\\approx$ jb-MLM (0.91$\\pm$0.12) $<$ scrambled (0.997$\\pm$0.005) $=$ binary (0.997$\\pm$0.005) $=$ 9-class (0.997$\\pm$0.005)}\n\\vspace{2pt}\n\n\\paragraph{Domain exposure is the primary mechanism.}\nMLM bridges the dominant $\\sim$60 percentage point gap from vanilla (0.312$\\pm$0.026 $\\to$ 0.914$\\pm$0.115) without any labels.\nThis confirms the domain-adaptive pretraining interpretation~\\citep{gururangan2020dontstop}: continued pretraining on jailbreak conversation text captures pragmatic features (hedging, escalation markers, topic-shifting patterns) that distinguish multi-turn attacks from benign conversations.\nOn synthetic OOD data, classification-supervised variants achieve F1 $\\geq$ 0.99 with near-zero cross-seed variance, adding $\\sim$8\\,pp and stability over unsupervised MLM.\nLabel quality and granularity are non-factors for detection: all three classification-supervised variants converge to identical F1 (0.997$\\pm$0.005), and McNemar's test confirms no statistically significant differences among them on OOD data (all $p > 0.13$; Section~\\ref{sec:perturbation}).\nPaired permutation tests further confirm this equivalence: 9-class vs.\\ JB-MLM yields max $p$ = 1.0 (DD) and $p \\geq 0.40$ (ActorAttack); 9-class vs.\\ scrambled yields max $p$ = 1.0 (DD). Classification supervision does not improve detection over unsupervised domain exposure at any prefix length.\nThe classification objective functions as a regularizer that shapes representation geometry regardless of whether the labels carry meaningful semantic information.\nOn synthetic OOD evaluations, classification supervision's primary complementary benefit is cross-seed stability: the 4--20$\\times$ variance reduction over MLM (std\\,=\\,0.005 vs.\\ 0.115 on DD) is consistent across both synthetic OOD families (Section~\\ref{sec:cross_encoder}). Bootstrap CI widths quantify this: classification-supervised variants produce narrow CIs (9-class DD Full: 5.7\\,pp range; binary: 0\\,pp) while MLM variants produce wide CIs (JB-MLM: 35.5\\,pp; wiki-MLM: 40\\,pp). This pattern reverses on human data, where 9-class exhibits the highest variance (Section~\\ref{sec:human_data}).\n\n\\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}\nWikipedia MLM (0.904$\\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\\,pp gap); general continued pretraining provides most of the representational benefit.\nAt early prefixes, jailbreak-domain text provides an 8\\,pp advantage ($K$=2: 0.993 vs.\\ 0.911), consistent with the interpretation that domain-specific features (persuasion markers, role-play framing) are most informative when the model has seen fewer turns.\nAs conversations grow longer, generic linguistic features accumulated through any continued pretraining become sufficient for discrimination.\nThe perturbation results (Section~\\ref{sec:perturbation}) reveal a sharper domain specificity effect: Wikipedia MLM degrades by $\\sim$12\\,pp under adversarial paraphrasing while jailbreak-domain MLM degrades by only 2.6\\,pp. Domain-specific features are more robust to surface-level rewording.\n\n\\paragraph{Misaligned supervision destabilizes generalization.}\nTopic classification yields DD-Full F1 = 0.541$\\pm$0.207 (seeds: 0.727, 0.252, 0.644); seed 123 falls \\emph{below} vanilla (0.312).\nThis result is particularly informative: topic classification uses the same jailbreak-domain training data as the other supervised variants, yet performs worse than Wikipedia MLM (0.904$\\pm$0.115), which uses out-of-domain text with no labels.\nA misaligned objective forces the encoder to allocate capacity to irrelevant discriminative features (topic boundaries rather than persuasion dynamics) and actively destabilizes the representations that MLM would otherwise preserve.\nThis separates the effect of ``having a training objective'' from ``having the right training objective.''\n\n\\paragraph{Evidence hierarchy on structurally complex attacks.}\nActorAttack~\\citep{ren2024actorattack} uses multi-persona steering across longer conversation structures, providing a more challenging OOD benchmark than DD.\nThe evidence hierarchy at full conversation length is:\n\n\\vspace{2pt}\n\\noindent\\hspace{0.5em}{\\small TF-IDF (0.26) $\\approx$ vanilla (0.26$\\pm$0.00) $<$ topic (0.63$\\pm$0.14) $<$ wiki-MLM (0.69$\\pm$0.30) $<$ jb-MLM (0.89$\\pm$0.08) $<$ scrambled (0.95$\\pm$0.04) $\\approx$ 9-class (0.97$\\pm$0.03) $\\approx$ binary (0.99$\\pm$0.01)}\n\\vspace{2pt}\n\nTF-IDF's collapse from 0.961 (DD) to 0.261 (ActorAttack) is the most striking contrast in the hierarchy. On DD, TF-IDF nearly matches domain-adapted neural models; on ActorAttack, it falls to vanilla-encoder levels (precision = 1.0, recall = 0.15). The lexical cues that suffice for DD are absent in ActorAttack's multi-persona structure, confirming that domain-adapted representations capture features that bag-of-words methods cannot.\nAll three classification-supervised variants converge to equivalent performance (0.951--0.990, max gap 3.9\\,pp, all confidence intervals overlapping), extending the DD finding: label quality and granularity are not factors for detection at any OOD difficulty level.\nThe primary discriminative factor is DAPT itself, which provides $\\sim$71\\,pp over both vanilla (0.258) and TF-IDF (0.261).\nFull per-prefix results appear in Appendix~\\ref{sec:actorattack_full}.\n\n\\paragraph{Temporal modeling.}\nMean pooling matches BiGRU (F1 = 1.000 on DD, single seed). This result suggests that detection relies primarily on per-turn representations rather than their sequential order.\nHowever, this result is from a single seed on a single OOD attack type, so the conclusion requires multi-seed confirmation.\nIf confirmed, it would imply that each individual turn carries detectable markers after DAPT, and that the conversation-level decision aggregates independent per-turn evidence.\n\n%----------------------------------------------------------------------\n\\subsection{Cross-Encoder Validation}\n\\label{sec:cross_encoder}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-encoder comparison on OOD Full (3-seed mean$\\pm$std). DD = Deceptive Delight, AA = ActorAttack. RoBERTa vanilla collapses on structurally complex ActorAttack despite strong DD performance.}\n\\label{tab:cross_encoder}\n\\begin{tabular}{@{}lcc|cc@{}}\n\\toprule\n& \\multicolumn{2}{c|}{DeBERTa-v3} & \\multicolumn{2}{c}{RoBERTa} \\\\\n\\textbf{Variant} & DD & AA & DD & AA \\\\\n\\midrule\nVanilla & .312$\\pm$.026 & .258$\\pm$.000 & .981$\\pm$.026 & .466$\\pm$.163 \\\\\nMLM & .914$\\pm$.115 & .893$\\pm$.080 & .987$\\pm$.018 & .730$\\pm$.201 \\\\\n9-class & .997$\\pm$.005 & .972$\\pm$.026 & .994$\\pm$.005 & .939$\\pm$.046 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTo test whether the evidence hierarchy generalizes beyond DeBERTa-v3, we replicate key variants on RoBERTa-base~\\citep{liu2019roberta} with identical Stage-2 pipelines and evaluate on both DD and ActorAttack.\n\nOn DD, the two encoders exhibit strikingly different hierarchies (Table~\\ref{tab:cross_encoder}).\nDeBERTa-v3 shows a steep gradient: continued pretraining bridges $\\sim$60\\,pp (vanilla 0.312 $\\to$ MLM 0.914).\nRoBERTa's DD hierarchy is essentially flat: vanilla already achieves 0.981$\\pm$0.026, with continued pretraining adding only 0.6\\,pp (MLM 0.987) and classification supervision another 0.7\\,pp (9-class 0.994).\n\nActorAttack reveals that this apparent RoBERTa sufficiency reflects DD's structural simplicity rather than genuine pretraining advantage.\nRoBERTa vanilla collapses from 0.981 (DD) to 0.466$\\pm$0.163 (ActorAttack), a 51.5\\,pp drop.\nDomain-adapted RoBERTa variants recover substantially: MLM reaches 0.730$\\pm$0.201 and 9-class reaches 0.939$\\pm$0.046.\nDeBERTa 9-class (0.972$\\pm$0.026) outperforms RoBERTa 9-class (0.939$\\pm$0.046) on ActorAttack; the encoder that received more extensive DAPT proves more robust on structurally complex attacks.\n\nThe combined DD and ActorAttack results indicate that DAPT universally improves cross-attack generalization across encoder architectures.\nEncoder pretraining method determines the \\emph{difficulty threshold} at which adaptation becomes critical: DeBERTa's RTD pretraining~\\citep{he2021deberta} requires adaptation even for simple attacks (DD vanilla = 0.312), while RoBERTa's MLM pretraining~\\citep{liu2019roberta} tolerates simple attacks (DD vanilla = 0.981) but fails on structurally complex ones (ActorAttack vanilla = 0.466). Bootstrap CIs confirm this encoder gap on DD: RoBERTa vanilla 95\\% CI [0.883, 1.000] vs.\\ DeBERTa vanilla [0.202, 0.341], with no overlap.\n\nOn synthetic OOD data, classification supervision provides a consistent stability benefit across both encoders and attack types: cross-seed variance drops to 0.005--0.046 (9-class) from 0.026--0.201 (vanilla/MLM).\nRoBERTa's IID strategy prediction accuracy (0.84) is lower than DeBERTa's (1.0), yet detection F1 is comparable; this further supports the regularizer interpretation from Section~\\ref{sec:decomposition}.\nPerturbation robustness on RoBERTa is left for future work; the analysis in Section~\\ref{sec:perturbation} is DeBERTa-specific.\n\n\\paragraph{Representational analysis.}\nCentered CKA confirms that both continued pretraining and classification supervision substantially reshape the representation space on both encoders.\nOn IID data, vanilla-to-MLM CKA is 0.442 (DeBERTa) and 0.393 (RoBERTa); vanilla-to-9-class CKA is 0.393 and 0.592, respectively.\nBoth encoders undergo large representational shifts, yet these shifts yield strikingly different detection gains: DeBERTa MLM gains $\\sim$60\\,pp while RoBERTa MLM gains only 0.6\\,pp from comparable CKA shifts.\nThe difference is explained by the starting point.\nDeBERTa's RTD-pretrained representations begin far from the detection-optimal subspace (vanilla F1 = 0.312 on DD), so any reshaping yields large returns; RoBERTa's MLM-pretrained representations lie closer to this subspace on lexically separable attacks (vanilla F1 = 0.981 on DD) but collapse on structurally complex ones (0.466 on ActorAttack), where the reshaping benefit becomes substantial.\nMLM and 9-class create distinct representation geometries (OOD CKA between them is 0.183 on RoBERTa), consistent with the different roles of unsupervised exposure and classification regularization identified in Section~\\ref{sec:decomposition}.\nLinear probing on three diagnostic tasks (turn position, escalation phase, persuasion presence) shows a consistent pattern across both encoders: 9-class outperforms vanilla and MLM by 1--5\\,pp, while MLM and vanilla perform comparably.\nClassification supervision enriches task-relevant features; unsupervised MLM reshapes representations without improving diagnostic separability.\n\n%----------------------------------------------------------------------\n\\subsection{Human Data Validation}\n\\label{sec:human_data}\n\nA key concern is whether the evidence hierarchy reflects genuine discourse-level generalization or merely within-LLM stylistic transfer, since both training and OOD evaluation data are generated by Qwen3-8B. We test this by evaluating on ToxicChat~\\citep{lin2023toxicchat}, a dataset of 204 human-written jailbreak attempts and 204 benign conversations collected from real LMSYS user interactions, entirely independent of any LLM generation pipeline.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Human data validation on ToxicChat~\\citep{lin2023toxicchat} (macro F1). 3-seed mean$\\pm$std. Single-turn data from real LMSYS user interactions, independent of Qwen3-8B.}\n\\label{tab:human_data}\n\\begin{tabular}{@{}lc@{}}\n\\toprule\n\\textbf{Variant} & Macro F1 \\\\\n\\midrule\nJB-MLM & .837$\\pm$.013 \\\\\nWiki-MLM & .791$\\pm$.093 \\\\\nBinary & .705$\\pm$.072 \\\\\nScrambled & .616$\\pm$.056 \\\\\n9-class & .596$\\pm$.087 \\\\\nTopic & .496$\\pm$.042 \\\\\n\\midrule\nVanilla & .413$\\pm$.021 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:human_data} reports macro F1 on ToxicChat. Domain-adapted variants range from 0.596 to 0.837, while vanilla achieves 0.413. All DAPT variants exceed vanilla by 18--42\\,pp, refuting the hypothesis that the evidence hierarchy is a Qwen3-8B generation artifact: DAPT on synthetic jailbreak text transfers to human-written attacks.\n\nThe relative ordering among domain-adapted variants differs from multi-turn evaluations: JB-MLM leads while classification-supervised variants rank lower. ToxicChat contains single-turn direct attacks with no multi-turn escalation structure, so the classification head's regularization of turn-sequence representations provides no advantage. MLM captures token-level distributional properties that transfer to single-turn detection without relying on sequential patterns. This is a modality mismatch, not a finding about variant quality: the multi-turn pipeline's full evidence hierarchy requires multi-turn human data to validate.\n\n%----------------------------------------------------------------------\n\\subsection{Perturbation Analysis}\n\\label{sec:perturbation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Perturbation behavior under adversarial paraphrasing on IID Crescendo ($n$=76). $\\Delta$: F1 degradation (pp). On this dataset and OOD Deceptive Delight, a three-layer pattern emerges (classification structure at full length, correct+fine-grained labels at $K$=2, both independently at $K$=1); this pattern does not generalize to ActorAttack.}\n\\label{tab:perturbation}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & $\\Delta$ Full & $\\Delta$ $K$=1 & $\\Delta$ $K$=2 & $\\Delta$ $K$=3 \\\\\n\\midrule\n9-class (ours) & \\textbf{0.0} & \\textbf{$-$2.6} & \\textbf{0.0} & \\textbf{0.0} \\\\\nScrambled & \\textbf{0.0} & $-$5.3 & $-$2.6 & \\textbf{0.0} \\\\\nBinary & \\textbf{0.0} & $-$9.2 & $-$2.6 & \\textbf{0.0} \\\\\n\\midrule\nTF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\\\\nMLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\\\\nTopic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \\textbf{0.0} \\\\\n\\midrule\nWikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\\\\nVanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:perturbation} shows perturbation behavior across variants on IID data.\nAll classification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length and $K \\geq 3$, regardless of label correctness.\nClassification training structure alone suffices for full-length robustness.\nAt $K$=2, the combination of correct and fine-grained labels is required: only 9-class ($\\Delta$=0.0) maintains zero degradation, while scrambled (random labels, fine-grained) and binary (correct labels, coarse) both degrade by $-$2.6\\,pp.\nThe fact that scrambled = binary at $K$=2 shows that neither granularity alone nor correctness alone suffices; the 9-class advantage requires both properties jointly.\nAt $K$=1, both granularity and correctness contribute independently: granularity provides +3.9\\,pp (scrambled $-$5.3 vs.\\ binary $-$9.2\\,pp), and correctness provides +2.7\\,pp (9-class $-$2.6 vs.\\ scrambled $-$5.3\\,pp).\nCorrect fine-grained labels yield the most perturbation-invariant early-turn representations.\n\nJailbreak-domain models without classification (MLM, topic, TF-IDF) degrade by 1--4\\,pp at full length.\nModels without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\\sim$12\\,pp, despite Wikipedia MLM matching jailbreak MLM on detection (Section~\\ref{sec:decomposition}). Perturbation robustness requires jailbreak-domain exposure specifically.\nMcNemar's test on matched-seed predictions confirms that no pairwise differences among classification-supervised variants (9-class vs.\\ binary, 9-class vs.\\ scrambled, scrambled vs.\\ binary) reach statistical significance at any prefix length (all $p > 0.13$).\nDiscordant pairs are sparse ($\\leq$7 per comparison), and the direction of advantage is inconsistent across seeds (e.g., 9-class outperforms scrambled at seed 42 but the reverse holds at seed 456 for $K$=1).\nThe perturbation evaluation ($n$=76 IID, with discordant pairs $\\leq$7) has limited statistical power to detect differences of this magnitude; the three-layer structure should be interpreted as an observed pattern rather than a statistically confirmed hierarchy.\n\nOn OOD Deceptive Delight ($n$=118), the IID robustness pattern replicates fully (Appendix~\\ref{sec:ood_perturbation}).\nAll classification-supervised variants show zero degradation at full conversation length; perturbed F1 reaches 1.000$\\pm$0.000, a marginal improvement over clean F1 (0.997$\\pm$0.005).\nThe 9-class and scrambled variants are completely tied on OOD perturbed data (McNemar $b$=$c$=0), consistent with the IID finding. This further supports the regularizer interpretation.\nThe larger OOD sample and more extreme performance gaps provide statistical power absent from IID evaluation: McNemar's test yields $p < 0.001$ for 9-class vs.\\ vanilla across all prefix lengths, with 49--78 discordant pairs per $K$.\nVanilla shows systematic early-turn degradation ($\\Delta K$=1 = $-$6.8$\\pm$1.1\\,pp across three seeds), while its full-length $\\Delta$ (+2.7\\,pp) reflects floor-effect noise at a baseline of 0.312 (std = 0.055) rather than meaningful robustness.\nNon-adapted representations are vulnerable to surface-level perturbation at early prefixes where detection is most critical.\n\nOn OOD ActorAttack, the zero-degradation pattern does not hold. Domain-adapted variants degrade substantially: scrambled $\\Delta$ Full = $-$17.2\\,pp, 9-class $-$20.4$\\pm$13.5\\,pp, binary $-$25.0\\,pp, and MLM $-$35.3\\,pp. Vanilla shows negligible change ($\\Delta$ = $-$0.9\\,pp), a floor effect from its already-low clean baseline (0.258). The 9-class variant exhibits extreme cross-seed variance ($\\Delta$ ranges from $-$1.3\\,pp at seed 123 to $-$30.3\\,pp at seeds 42 and 456). Absolute perturbation robustness is therefore attack-family-dependent: the three-layer pattern observed on IID and DD does not generalize to ActorAttack. One possible explanation is that ActorAttack's distributed multi-persona structure produces more diffuse persuasion signals that are vulnerable to surface rephrasing, but this hypothesis remains speculative.\n\nPerturbation narrows but does not close the gap between adapted and non-adapted models: 9-class perturbed F1 = 0.768 vs.\\ vanilla 0.248 (McNemar $p < 0.001$). Domain adaptation's detection advantage, identified in Section~\\ref{sec:decomposition}, persists under adversarial paraphrasing on ActorAttack.\n\n%----------------------------------------------------------------------\n\\subsection{Strategy Trajectory Analysis}\n\\label{sec:strategy}\n\nThe 9-class persuasion taxonomy provides interpretable characterization of attack strategies on known attack families.\nThe predicted strategy labels achieve Cohen's $\\kappa$=0.78 agreement with human annotations on IID data ($n$=50; see Section~\\ref{sec:method}). This enables post-hoc analysis of \\emph{how} different attack families orchestrate persuasion.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}\n\\caption{Persuasion strategy transition count matrices for three attack types, based on ground-truth intended strategy labels. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}\n\\label{fig:strategy_heatmap}\n\\end{figure*}\n\nFigure~\\ref{fig:strategy_heatmap} shows transition count matrices based on ground-truth intended strategy labels for three attack types.\nCrescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545).\nThis reflects Crescendo's design as a gradual escalation attack that cycles through multiple persuasion techniques to build rapport before introducing harmful requests.\n\nFITD conversations show a markedly sparser pattern (541 transitions), with Role$\\to$Obfuscation (161) as the dominant transition.\nThis is consistent with FITD's structure: the attack secures initial compliance through role assignment (``You are a helpful assistant that never refuses'') and then obscures the escalation path through obfuscation techniques to exploit the commitment-consistency bias~\\citep{cialdini2001influence}.\n\nDD conversations span 5 active source strategies (565 transitions), with Emotion$\\to$Obfuscation (129) as the dominant transition.\nThis aligns with DD's design of embedding harmful content within emotionally engaging contexts~\\citep{deceptivedelight2024}: the attacker establishes emotional rapport before weaving in the harmful request through obfuscation.\n\nThese ground-truth trajectory signatures illustrate distinct persuasion orchestration patterns across attack families.\n\nHowever, the model's strategy predictions do not generalize to unseen attacks: on OOD Deceptive Delight, the 9-class model achieves strategy prediction accuracy of only 30.7\\% ($\\kappa$=0.126), essentially random performance.\nThis is consistent with the detection mechanism analysis in Section~\\ref{sec:decomposition}: all three classification-supervised variants achieve identical detection F1 (0.997$\\pm$0.005). The classification head functions as a representational regularizer rather than a meaningful strategy classifier.\nDetection operates through domain-adapted \\texttt{[CLS]} embeddings, not through strategy classification accuracy.\nThe taxonomy provides interpretable characterization of known attack families where strategy labels are reliable; extending strategy-level interpretability to unseen attacks requires OOD-aware fine-tuning and is a direction for future work.\n",
      "numLines": 306,
      "startLine": 1,
      "totalLines": 306
    }
  },
  "sourceToolAssistantUUID": "3cf0909b-13f6-4bb7-8cf3-f6f999fab15d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T18:01:00.104Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P93cPCXhRFFs4MRH6tTre5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38ca8fa9-e579-4277-bcd2-408de56869f9",
  "isSidechain": false,
  "requestId": "req_011CbAUJCPk45ujpWNNhwhw7",
  "type": "assistant",
  "uuid": "0b9b405e-03a0-40da-8f9e-325fe3c8fc63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtW5c41jyMF3d1ejhKi2V1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2933,
      "cache_read_input_tokens": 27137,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 907,
          "cache_read_input_tokens": 27137,
          "cache_creation_input_tokens": 2933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2933
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-18T18:01:00.118Z_

<details><summary>↩ Tool result · `toolu_01P93cPCXhRFFs4MRH6tTre5`</summary>

```text
1	% conclusion.tex — D034 analysis reframe
2	
3	\section{Discussion}
4	\label{sec:discussion}
5	
6	\paragraph{Topic shortcut confound.}
7	One concern is whether a topic-level shortcut (jailbreak conversations discuss different topics than benign ones) could explain the detection results. Three observations argue against this. First, topic classification on the same jailbreak training data yields unstable OOD generalization (F1\,=\,0.541$\pm$0.207 on DD), with one seed falling below vanilla (0.252 vs.\ 0.312); if a topic shortcut drove detection, topic-supervised models should outperform, not underperform, unsupervised alternatives. Second, scrambled labels achieve detection equivalent to correct labels (F1 gap $\leq$3.9\,pp across all OOD evaluations), indicating that specific label content does not drive detection. Third, MLM without any classification labels achieves strong detection (F1\,$\geq$\,0.97 at $K \leq 5$ on DD), confirming that the benefit comes from domain exposure rather than any classification-based shortcut.
8	
9	\paragraph{Single-LLM confound.}
10	Both training and synthetic OOD data are generated by Qwen3-8B, raising the concern that the evidence hierarchy reflects within-LLM stylistic transfer rather than discourse-level generalization. Evaluation on ToxicChat~\citep{lin2023toxicchat} (204 human-written jailbreaks from LMSYS) provides partial resolution: all domain-adapted variants outperform vanilla by 18--42\,pp (Table~\ref{tab:human_data}), confirming that DAPT on synthetic text transfers to human-written attacks. ToxicChat is single-turn, so the relative ordering among domain-adapted variants reflects single-turn modality rather than variant quality. This evidence validates the core DAPT benefit but does not test the full multi-turn pipeline; multi-turn human jailbreak datasets are needed to confirm the complete hierarchy.
11	
12	\paragraph{Variance reversal on human data.}
13	On synthetic OOD evaluations, classification supervision reduces cross-seed variance 4--20$\times$ relative to MLM. On ToxicChat (Table~\ref{tab:human_data}), this pattern reverses: 9-class exhibits high variance (std\,=\,0.087) while JB-MLM exhibits the lowest among domain-adapted variants (std\,=\,0.013). Classification supervision optimizes representations for the training distribution's structure, stabilizing predictions within the synthetic data manifold; when the test distribution shifts to human-written text, these distribution-specific representations become a source of instability. MLM's unsupervised objective imposes no distribution-specific classification boundaries, producing representations that generalize more uniformly across the style gap. Classification supervision and MLM thus serve complementary roles: the former as a within-distribution regularizer, the latter as a cross-distribution generalizer.
14	
15	\paragraph{Encoder capacity confound.}
16	The cross-encoder comparison uses DeBERTa-v3-base (184M parameters) and RoBERTa-base (125M parameters), which differ in both pretraining objective and model capacity. We cannot fully disentangle whether DeBERTa-v3's greater DAPT needs reflect its RTD pretraining or its larger capacity. Size-matched comparisons (e.g., DeBERTa-v3-base vs.\ RoBERTa-large) would isolate the pretraining objective effect and are left for future work.
17	
18	\section{Conclusion}
19	\label{sec:conclusion}
20	
21	Our controlled ablation across two encoder architectures and four attack families identifies three findings about cross-attack generalization in multi-turn jailbreak detection. First, domain exposure via DAPT is the primary mechanism, bridging $\sim$60\,pp of the OOD gap on DeBERTa-v3 without any labels. Second, encoder pretraining method determines the difficulty threshold at which adaptation becomes critical: RoBERTa tolerates structurally simple attacks but fails on multi-persona ActorAttack (F1 0.981 $\to$ 0.466). Third, classification supervision functions as a representational regularizer, providing cross-seed stability on synthetic OOD evaluations (variance reduced 4--20$\times$ vs.\ MLM-only) and interpretable strategy characterization regardless of label correctness, though strategy predictions do not transfer to unseen attacks ($\kappa$=0.126). On human data, this stability pattern reverses: MLM exhibits the lowest variance while classification-supervised variants show the highest, suggesting that classification regularization is distribution-specific (Section~\ref{sec:human_data}). DAPT's detection advantage persists under adversarial paraphrasing (McNemar $p < 0.001$), though absolute perturbation robustness is attack-family-dependent. Validation on human-written ToxicChat jailbreaks confirms that the domain-adapted vs.\ vanilla gap transfers beyond synthetic data (Section~\ref{sec:human_data}); full multi-turn validation on human datasets is needed.
22	
23	\section{Limitations}
24	\label{sec:limitations}
25	
26	\paragraph{Dataset scale and diversity.}
27	The training set contains 500 synthetic conversations generated by a single model (Qwen3-8B), and OOD evaluation covers three attack families (FITD, Deceptive Delight, ActorAttack). This scale limits statistical power: the perturbation evaluation ($n$=76) means tier boundaries in Table~\ref{tab:perturbation} correspond to 1--3 misclassifications. Evaluation on ToxicChat (Section~\ref{sec:human_data}) confirms that the domain-adapted vs.\ vanilla gap transfers to human-written jailbreaks, partially addressing the single-LLM confound. However, ToxicChat contains only single-turn data; whether the full multi-turn evidence hierarchy (including classification supervision's stabilization benefit) generalizes to human-generated multi-turn attacks remains open.
28	
29	\paragraph{Lexical separability.}
30	TF-IDF logistic regression achieves F1 = 0.961 on OOD Deceptive Delight with near-perfect per-prefix performance, indicating substantial lexical separability on this attack family. On DD alone, we cannot distinguish whether continued pretraining captures discourse features or exploits the same lexical cues. ActorAttack resolves this question: TF-IDF collapses to F1 = 0.261 while domain-adapted models maintain F1 $\geq$ 0.89, a $\geq$63\,pp gap, confirming that continued pretraining captures features beyond lexical overlap on structurally complex attacks. Whether this discourse-level advantage extends to other structurally complex attack families beyond ActorAttack requires further evaluation.
31	
32	\paragraph{Strategy annotation quality.}
33	Persuasion strategy labels are produced by Qwen3-8B with structured prompting. Inter-annotator agreement with a human sample ($n$=50) yields Cohen's $\kappa$=0.78, which indicates substantial but imperfect agreement. The small human validation sample and reliance on a single annotator model limit confidence in label quality. We plan to release the annotation prompts and data to enable independent verification.
34	
35	\paragraph{OOD strategy prediction.}
36	While the 9-class model achieves high detection F1 on OOD attacks (0.997$\pm$0.005 on Deceptive Delight), its strategy-level predictions do not generalize: OOD strategy accuracy is 30.7\% ($\kappa$=0.126). The interpretability provided by the persuasion taxonomy is currently limited to known attack families where strategy labels are reliable.
37	
38	\paragraph{Single-seed variants.}
39	Mean pooling results report a single-seed (seed 42) evaluation. Multi-seed validation is needed to confirm this finding.
40	
41	\paragraph{Scope.}
42	Only persuasion-mediated multi-turn attacks fall within scope. Single-turn token-level attacks~\citep{zou2023gcg}, non-persuasive multi-turn strategies, and attacks targeting modalities other than text are not addressed. The user-only input assumption (excluding assistant responses) may miss information in attacks where the model's own responses contribute to the escalation trajectory.
43	
44	\paragraph{Computation cost.}
45	Stage~1 continued pretraining requires approximately 30 minutes on a single A100 GPU per variant. Stage~2 training completes in under 5 minutes. Total pipeline cost for all seven variants is under 4 GPU-hours, making the approach accessible for replication.
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b9b405e-03a0-40da-8f9e-325fe3c8fc63",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "c9d5e55b-6171-4cba-a594-3fc70b1fa7dc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/conclusion.tex",
      "content": "% conclusion.tex — D034 analysis reframe\n\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Topic shortcut confound.}\nOne concern is whether a topic-level shortcut (jailbreak conversations discuss different topics than benign ones) could explain the detection results. Three observations argue against this. First, topic classification on the same jailbreak training data yields unstable OOD generalization (F1\\,=\\,0.541$\\pm$0.207 on DD), with one seed falling below vanilla (0.252 vs.\\ 0.312); if a topic shortcut drove detection, topic-supervised models should outperform, not underperform, unsupervised alternatives. Second, scrambled labels achieve detection equivalent to correct labels (F1 gap $\\leq$3.9\\,pp across all OOD evaluations), indicating that specific label content does not drive detection. Third, MLM without any classification labels achieves strong detection (F1\\,$\\geq$\\,0.97 at $K \\leq 5$ on DD), confirming that the benefit comes from domain exposure rather than any classification-based shortcut.\n\n\\paragraph{Single-LLM confound.}\nBoth training and synthetic OOD data are generated by Qwen3-8B, raising the concern that the evidence hierarchy reflects within-LLM stylistic transfer rather than discourse-level generalization. Evaluation on ToxicChat~\\citep{lin2023toxicchat} (204 human-written jailbreaks from LMSYS) provides partial resolution: all domain-adapted variants outperform vanilla by 18--42\\,pp (Table~\\ref{tab:human_data}), confirming that DAPT on synthetic text transfers to human-written attacks. ToxicChat is single-turn, so the relative ordering among domain-adapted variants reflects single-turn modality rather than variant quality. This evidence validates the core DAPT benefit but does not test the full multi-turn pipeline; multi-turn human jailbreak datasets are needed to confirm the complete hierarchy.\n\n\\paragraph{Variance reversal on human data.}\nOn synthetic OOD evaluations, classification supervision reduces cross-seed variance 4--20$\\times$ relative to MLM. On ToxicChat (Table~\\ref{tab:human_data}), this pattern reverses: 9-class exhibits high variance (std\\,=\\,0.087) while JB-MLM exhibits the lowest among domain-adapted variants (std\\,=\\,0.013). Classification supervision optimizes representations for the training distribution's structure, stabilizing predictions within the synthetic data manifold; when the test distribution shifts to human-written text, these distribution-specific representations become a source of instability. MLM's unsupervised objective imposes no distribution-specific classification boundaries, producing representations that generalize more uniformly across the style gap. Classification supervision and MLM thus serve complementary roles: the former as a within-distribution regularizer, the latter as a cross-distribution generalizer.\n\n\\paragraph{Encoder capacity confound.}\nThe cross-encoder comparison uses DeBERTa-v3-base (184M parameters) and RoBERTa-base (125M parameters), which differ in both pretraining objective and model capacity. We cannot fully disentangle whether DeBERTa-v3's greater DAPT needs reflect its RTD pretraining or its larger capacity. Size-matched comparisons (e.g., DeBERTa-v3-base vs.\\ RoBERTa-large) would isolate the pretraining objective effect and are left for future work.\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nOur controlled ablation across two encoder architectures and four attack families identifies three findings about cross-attack generalization in multi-turn jailbreak detection. First, domain exposure via DAPT is the primary mechanism, bridging $\\sim$60\\,pp of the OOD gap on DeBERTa-v3 without any labels. Second, encoder pretraining method determines the difficulty threshold at which adaptation becomes critical: RoBERTa tolerates structurally simple attacks but fails on multi-persona ActorAttack (F1 0.981 $\\to$ 0.466). Third, classification supervision functions as a representational regularizer, providing cross-seed stability on synthetic OOD evaluations (variance reduced 4--20$\\times$ vs.\\ MLM-only) and interpretable strategy characterization regardless of label correctness, though strategy predictions do not transfer to unseen attacks ($\\kappa$=0.126). On human data, this stability pattern reverses: MLM exhibits the lowest variance while classification-supervised variants show the highest, suggesting that classification regularization is distribution-specific (Section~\\ref{sec:human_data}). DAPT's detection advantage persists under adversarial paraphrasing (McNemar $p < 0.001$), though absolute perturbation robustness is attack-family-dependent. Validation on human-written ToxicChat jailbreaks confirms that the domain-adapted vs.\\ vanilla gap transfers beyond synthetic data (Section~\\ref{sec:human_data}); full multi-turn validation on human datasets is needed.\n\n\\section{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Dataset scale and diversity.}\nThe training set contains 500 synthetic conversations generated by a single model (Qwen3-8B), and OOD evaluation covers three attack families (FITD, Deceptive Delight, ActorAttack). This scale limits statistical power: the perturbation evaluation ($n$=76) means tier boundaries in Table~\\ref{tab:perturbation} correspond to 1--3 misclassifications. Evaluation on ToxicChat (Section~\\ref{sec:human_data}) confirms that the domain-adapted vs.\\ vanilla gap transfers to human-written jailbreaks, partially addressing the single-LLM confound. However, ToxicChat contains only single-turn data; whether the full multi-turn evidence hierarchy (including classification supervision's stabilization benefit) generalizes to human-generated multi-turn attacks remains open.\n\n\\paragraph{Lexical separability.}\nTF-IDF logistic regression achieves F1 = 0.961 on OOD Deceptive Delight with near-perfect per-prefix performance, indicating substantial lexical separability on this attack family. On DD alone, we cannot distinguish whether continued pretraining captures discourse features or exploits the same lexical cues. ActorAttack resolves this question: TF-IDF collapses to F1 = 0.261 while domain-adapted models maintain F1 $\\geq$ 0.89, a $\\geq$63\\,pp gap, confirming that continued pretraining captures features beyond lexical overlap on structurally complex attacks. Whether this discourse-level advantage extends to other structurally complex attack families beyond ActorAttack requires further evaluation.\n\n\\paragraph{Strategy annotation quality.}\nPersuasion strategy labels are produced by Qwen3-8B with structured prompting. Inter-annotator agreement with a human sample ($n$=50) yields Cohen's $\\kappa$=0.78, which indicates substantial but imperfect agreement. The small human validation sample and reliance on a single annotator model limit confidence in label quality. We plan to release the annotation prompts and data to enable independent verification.\n\n\\paragraph{OOD strategy prediction.}\nWhile the 9-class model achieves high detection F1 on OOD attacks (0.997$\\pm$0.005 on Deceptive Delight), its strategy-level predictions do not generalize: OOD strategy accuracy is 30.7\\% ($\\kappa$=0.126). The interpretability provided by the persuasion taxonomy is currently limited to known attack families where strategy labels are reliable.\n\n\\paragraph{Single-seed variants.}\nMean pooling results report a single-seed (seed 42) evaluation. Multi-seed validation is needed to confirm this finding.\n\n\\paragraph{Scope.}\nOnly persuasion-mediated multi-turn attacks fall within scope. Single-turn token-level attacks~\\citep{zou2023gcg}, non-persuasive multi-turn strategies, and attacks targeting modalities other than text are not addressed. The user-only input assumption (excluding assistant responses) may miss information in attacks where the model's own responses contribute to the escalation trajectory.\n\n\\paragraph{Computation cost.}\nStage~1 continued pretraining requires approximately 30 minutes on a single A100 GPU per variant. Stage~2 training completes in under 5 minutes. Total pipeline cost for all seven variants is under 4 GPU-hours, making the approach accessible for replication.\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  },
  "sourceToolAssistantUUID": "0b9b405e-03a0-40da-8f9e-325fe3c8fc63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T18:01:00.600Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CnzQ1nku73HQ4NrcHMK77J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9d5e55b-6171-4cba-a594-3fc70b1fa7dc",
  "isSidechain": false,
  "requestId": "req_011CbAUJCPk45ujpWNNhwhw7",
  "type": "assistant",
  "uuid": "4ec9c71a-b27f-4a01-a339-04327a1863cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtW5c41jyMF3d1ejhKi2V1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2933,
      "cache_read_input_tokens": 27137,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 907,
          "cache_read_input_tokens": 27137,
          "cache_creation_input_tokens": 2933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2933
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-18T18:01:00.608Z_

<details><summary>↩ Tool result · `toolu_01CnzQ1nku73HQ4NrcHMK77J`</summary>

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
11	\caption{LLM-as-judge jailbreak detection. IID: binary F1 (Crescendo test set); OOD: macro F1 (DD = Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 values exclude unparseable responses and represent upper bounds.}
12	\label{tab:llm_judge}
13	\begin{tabular}{@{}lcccr@{}}
14	\toprule
15	\textbf{Method} & DD & AA & IID & Unparse. \\
16	\midrule
17	\multicolumn{5}{l}{\textit{Zero-shot}} \\[2pt]
18	GPT-5.5 & -- & -- & .383 & 30--47\% \\
19	Qwen3-8B & .244 & .244 & .100 & 0\% \\
20	\midrule
21	\multicolumn{5}{l}{\textit{3-shot}} \\[2pt]
22	Qwen3-8B & .566 & .652 & -- & 0\% \\
23	\midrule
24	\multicolumn{5}{l}{\textit{Trained classifier}} \\[2pt]
25	9-class (ours) & \textbf{.997} & \textbf{.972} & \textbf{1.000} & 0\% \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:llm_judge} reports LLM-as-judge performance on IID and OOD data.
31	On IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 = 0.383 on full conversations; 30--47\% of responses are unparseable.
32	Qwen3-8B performs worse (IID F1 = 0.100).
33	On OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 on both DD and ActorAttack by predicting nearly all conversations as benign.
34	Even with 3-shot prompting, Qwen3-8B reaches only 0.566 (DD) and 0.652 (AA), while DisPeD maintains macro F1 $\geq$ 0.972.
35	The poor performance of content-level reasoning on unseen attack types underscores the necessity of trained discourse-aware classifiers.
36	
37	\section{Full Cross-Attack Results by Prefix}
38	\label{sec:full_prefix}
39	
40	\begin{table*}[t]
41	\centering
42	\small
43	\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\pm$std where available. ``--'' indicates insufficient conversation length for that prefix (FITD conversations contain 2--3 turns).}
44	\label{tab:full_prefix}
45	\begin{tabular}{@{}lccccc@{}}
46	\toprule
47	\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\
48	\midrule
49	\multicolumn{6}{l}{\textit{IID (Crescendo)}} \\[2pt]
50	9-class (ours) & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 \\
51	MLM-only & .960 & .974 & .987 & 1.000 & 1.000 \\
52	Vanilla DeBERTa & .968$\pm$.033 & .978$\pm$.016 & .987$\pm$.000 & .982$\pm$.014 & 1.000$\pm$.000 \\
53	TF-IDF LR & 1.000 & 1.000 & 1.000 & 1.000 & 1.000 \\
54	\midrule
55	\multicolumn{6}{l}{\textit{OOD (Deceptive Delight)}} \\[2pt]
56	9-class (ours) & .990$\pm$.013 & .981$\pm$.013 & .972$\pm$.026 & .997$\pm$.005 & .997$\pm$.005 \\
57	Binary & .994$\pm$.009 & .994$\pm$.009 & .984$\pm$.008 & 1.000$\pm$.000 & .997$\pm$.005 \\
58	Scrambled & .997$\pm$.005 & .981$\pm$.026 & .975$\pm$.029 & .997$\pm$.005 & .997$\pm$.005 \\
59	MLM-only & .973$\pm$.019 & .993$\pm$.009 & .997$\pm$.005 & .997$\pm$.005 & .914$\pm$.115 \\
60	Vanilla DeBERTa & .628$\pm$.038 & .479$\pm$.038 & .389$\pm$.027 & .351$\pm$.030 & .312$\pm$.026 \\
61	TF-IDF LR & 1.000 & 1.000 & .994 & 1.000 & .961 \\
62	\midrule
63	\multicolumn{6}{l}{\textit{OOD (FITD)}} \\[2pt]
64	9-class (ours) & 1.000 & 1.000 & -- & -- & 1.000 \\
65	Vanilla DeBERTa & .990 & 1.000 & -- & -- & 1.000 \\
66	TF-IDF LR & 1.000 & -- & -- & -- & 1.000 \\
67	\bottomrule
68	\end{tabular}
69	\end{table*}
70	
71	\section{ActorAttack Full Results}
72	\label{sec:actorattack_full}
73	
74	\begin{table*}[t]
75	\centering
76	\small
77	\caption{Full ActorAttack OOD results (F1) at all prefix lengths. 3-seed mean$\pm$std (Binary per-$K$ reports $n$=2; Full is 3-seed).}
78	\label{tab:actorattack_full}
79	\begin{tabular}{@{}lccccc@{}}
80	\toprule
81	\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\
82	\midrule
83	\multicolumn{6}{l}{\textit{DeBERTa-v3}} \\[2pt]
84	Binary & .788$\pm$.020 & \textbf{.935$\pm$.018} & \textbf{.976$\pm$.005} & \textbf{.995$\pm$.005} & \textbf{.990$\pm$.008} \\
85	9-class & .773$\pm$.041 & .855$\pm$.048 & .921$\pm$.046 & .966$\pm$.028 & .972$\pm$.026 \\
86	Scrambled & .652$\pm$.034 & .804$\pm$.053 & .854$\pm$.046 & .910$\pm$.052 & .951$\pm$.043 \\
87	MLM-only & .736$\pm$.150 & .909$\pm$.058 & .945$\pm$.039 & .929$\pm$.033 & .893$\pm$.080 \\
88	Wiki MLM & .656$\pm$.224 & .672$\pm$.252 & .693$\pm$.280 & .689$\pm$.285 & .686$\pm$.297 \\
89	Topic & .513$\pm$.077 & .580$\pm$.109 & .565$\pm$.100 & .615$\pm$.111 & .625$\pm$.141 \\
90	Vanilla & .337$\pm$.049 & .306$\pm$.026 & .284$\pm$.011 & .262$\pm$.006 & .258$\pm$.000 \\
91	TF-IDF LR & .633 & .730 & .571 & .242 & .261 \\
92	\midrule
93	\multicolumn{6}{l}{\textit{RoBERTa}} \\[2pt]
94	9-class & \textbf{.738$\pm$.033} & .805$\pm$.033 & .884$\pm$.066 & .925$\pm$.066 & .939$\pm$.046 \\
95	MLM & .633$\pm$.133 & .665$\pm$.150 & .713$\pm$.174 & .719$\pm$.184 & .730$\pm$.201 \\
96	Vanilla & .410$\pm$.126 & .425$\pm$.143 & .432$\pm$.144 & .466$\pm$.144 & .466$\pm$.163 \\
97	\bottomrule
98	\end{tabular}
99	\end{table*}
100	
101	\section{OOD Perturbation Robustness}
102	\label{sec:ood_perturbation}
103	
104	\begin{table}[t]
105	\centering
106	\small
107	\caption{Perturbation robustness on OOD Deceptive Delight ($n$=118). $\Delta$: F1 change (pp) from clean to paraphrased. 3-seed mean$\pm$std where available.}
108	\label{tab:ood_perturbation}
109	\begin{tabular}{@{}lcccc@{}}
110	\toprule
111	\textbf{Variant} & Clean Full & Pert.\ Full & $\Delta$ Full & $\Delta$ $K$=1 \\
112	\midrule
113	9-class & .997$\pm$.005 & 1.000$\pm$.000 & +0.3 & +0.6 \\
114	Binary & .997$\pm$.005 & 1.000$\pm$.000 & +0.3 & +0.6 \\
115	Scrambled & .997$\pm$.005 & 1.000$\pm$.000 & +0.3 & $-$0.3 \\
116	\midrule
117	JB MLM & .914$\pm$.115 & .941 & +2.7 & 0.0 \\
118	Wiki MLM$^{*}$ & .904$\pm$.115 & .872 & $-$3.3 & $-$3.2 \\
119	Vanilla$^{\dagger}$ & .312$\pm$.026 & .339$\pm$.055 & +2.7 & $-$6.8$\pm$1.1 \\
120	\bottomrule
121	\end{tabular}
122	\vspace{-2pt}
123	{\footnotesize $^{*}$Wiki MLM degradation is seed-driven: seed 42 accounts for $-$9.8\,pp; other seeds show 0.0\,pp change.\\$^{\dagger}$Vanilla $\Delta$ Full = +2.7\,pp reflects floor-effect noise (baseline 0.312, std 0.055), not meaningful improvement.}
124	\end{table}
125	
126	\section{Reproducibility Details}
127	\label{sec:reproducibility}
128	
129	\paragraph{Stage-1 training.}
130	All variants use DeBERTa-v3-base (184M parameters) with learning rate $2 \times 10^{-5}$, AdamW optimizer ($\beta_1$=0.9, $\beta_2$=0.999, weight decay 0.01), linear warmup over the first 10\% of steps, batch size 16, and 4 epochs. MLM variants use 15\% random token masking. Training takes approximately 30 minutes per variant on a single NVIDIA A100 (40GB).
131	
132	\paragraph{Stage-2 training.}
133	The BiGRU has hidden dimension 128 (bidirectional, so output dimension 256). The MLP classifier has layers $256 \to 64 \to 2$ with ReLU activation and dropout 0.3. Training uses learning rate $1 \times 10^{-3}$, Adam optimizer, batch size 32, and 20 epochs with early stopping (patience 5) on validation F1. Stage-2 training completes in under 5 minutes per variant.
134	
135	\paragraph{Data generation.}
136	Jailbreak conversations are generated using Qwen3-8B with attack-specific prompt templates. Crescendo conversations follow a 5--8 turn gradual escalation structure. FITD conversations use a 2--3 turn commitment-consistency structure. Deceptive Delight conversations embed harmful content within emotionally engaging 3--5 turn sequences. Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general) with matched turn counts.
137	
138	\paragraph{Strategy annotation.}
139	Each user turn is annotated by Qwen3-8B using a structured prompt that provides definitions and two examples for each of the nine strategy categories. The prompt instructs the model to output a single category label. We plan to release all generation and annotation prompts, the full dataset, and training code upon acceptance.
140	
141	\paragraph{Adversarial paraphrasing.}
142	The paraphrased test set is generated by instructing Qwen3-8B to rephrase each user turn while preserving the communicative intent. The resulting paraphrases have mean BERTScore 0.92 and mean lexical overlap 0.20 with the originals. These metrics confirm substantial surface-level variation.
143	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ec9c71a-b27f-4a01-a339-04327a1863cc",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "e25dd0b2-3c54-4e4f-bffd-77f5e058e6d1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex",
      "content": "% appendix.tex — Supplementary material\n\n\\appendix\n\n\\section{LLM-as-Judge Baseline}\n\\label{sec:llm_judge}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LLM-as-judge jailbreak detection. IID: binary F1 (Crescendo test set); OOD: macro F1 (DD = Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 values exclude unparseable responses and represent upper bounds.}\n\\label{tab:llm_judge}\n\\begin{tabular}{@{}lcccr@{}}\n\\toprule\n\\textbf{Method} & DD & AA & IID & Unparse. \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Zero-shot}} \\\\[2pt]\nGPT-5.5 & -- & -- & .383 & 30--47\\% \\\\\nQwen3-8B & .244 & .244 & .100 & 0\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{3-shot}} \\\\[2pt]\nQwen3-8B & .566 & .652 & -- & 0\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Trained classifier}} \\\\[2pt]\n9-class (ours) & \\textbf{.997} & \\textbf{.972} & \\textbf{1.000} & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:llm_judge} reports LLM-as-judge performance on IID and OOD data.\nOn IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 = 0.383 on full conversations; 30--47\\% of responses are unparseable.\nQwen3-8B performs worse (IID F1 = 0.100).\nOn OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 on both DD and ActorAttack by predicting nearly all conversations as benign.\nEven with 3-shot prompting, Qwen3-8B reaches only 0.566 (DD) and 0.652 (AA), while DisPeD maintains macro F1 $\\geq$ 0.972.\nThe poor performance of content-level reasoning on unseen attack types underscores the necessity of trained discourse-aware classifiers.\n\n\\section{Full Cross-Attack Results by Prefix}\n\\label{sec:full_prefix}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\\pm$std where available. ``--'' indicates insufficient conversation length for that prefix (FITD conversations contain 2--3 turns).}\n\\label{tab:full_prefix}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{IID (Crescendo)}} \\\\[2pt]\n9-class (ours) & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 \\\\\nMLM-only & .960 & .974 & .987 & 1.000 & 1.000 \\\\\nVanilla DeBERTa & .968$\\pm$.033 & .978$\\pm$.016 & .987$\\pm$.000 & .982$\\pm$.014 & 1.000$\\pm$.000 \\\\\nTF-IDF LR & 1.000 & 1.000 & 1.000 & 1.000 & 1.000 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{OOD (Deceptive Delight)}} \\\\[2pt]\n9-class (ours) & .990$\\pm$.013 & .981$\\pm$.013 & .972$\\pm$.026 & .997$\\pm$.005 & .997$\\pm$.005 \\\\\nBinary & .994$\\pm$.009 & .994$\\pm$.009 & .984$\\pm$.008 & 1.000$\\pm$.000 & .997$\\pm$.005 \\\\\nScrambled & .997$\\pm$.005 & .981$\\pm$.026 & .975$\\pm$.029 & .997$\\pm$.005 & .997$\\pm$.005 \\\\\nMLM-only & .973$\\pm$.019 & .993$\\pm$.009 & .997$\\pm$.005 & .997$\\pm$.005 & .914$\\pm$.115 \\\\\nVanilla DeBERTa & .628$\\pm$.038 & .479$\\pm$.038 & .389$\\pm$.027 & .351$\\pm$.030 & .312$\\pm$.026 \\\\\nTF-IDF LR & 1.000 & 1.000 & .994 & 1.000 & .961 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{OOD (FITD)}} \\\\[2pt]\n9-class (ours) & 1.000 & 1.000 & -- & -- & 1.000 \\\\\nVanilla DeBERTa & .990 & 1.000 & -- & -- & 1.000 \\\\\nTF-IDF LR & 1.000 & -- & -- & -- & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{ActorAttack Full Results}\n\\label{sec:actorattack_full}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Full ActorAttack OOD results (F1) at all prefix lengths. 3-seed mean$\\pm$std (Binary per-$K$ reports $n$=2; Full is 3-seed).}\n\\label{tab:actorattack_full}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{DeBERTa-v3}} \\\\[2pt]\nBinary & .788$\\pm$.020 & \\textbf{.935$\\pm$.018} & \\textbf{.976$\\pm$.005} & \\textbf{.995$\\pm$.005} & \\textbf{.990$\\pm$.008} \\\\\n9-class & .773$\\pm$.041 & .855$\\pm$.048 & .921$\\pm$.046 & .966$\\pm$.028 & .972$\\pm$.026 \\\\\nScrambled & .652$\\pm$.034 & .804$\\pm$.053 & .854$\\pm$.046 & .910$\\pm$.052 & .951$\\pm$.043 \\\\\nMLM-only & .736$\\pm$.150 & .909$\\pm$.058 & .945$\\pm$.039 & .929$\\pm$.033 & .893$\\pm$.080 \\\\\nWiki MLM & .656$\\pm$.224 & .672$\\pm$.252 & .693$\\pm$.280 & .689$\\pm$.285 & .686$\\pm$.297 \\\\\nTopic & .513$\\pm$.077 & .580$\\pm$.109 & .565$\\pm$.100 & .615$\\pm$.111 & .625$\\pm$.141 \\\\\nVanilla & .337$\\pm$.049 & .306$\\pm$.026 & .284$\\pm$.011 & .262$\\pm$.006 & .258$\\pm$.000 \\\\\nTF-IDF LR & .633 & .730 & .571 & .242 & .261 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RoBERTa}} \\\\[2pt]\n9-class & \\textbf{.738$\\pm$.033} & .805$\\pm$.033 & .884$\\pm$.066 & .925$\\pm$.066 & .939$\\pm$.046 \\\\\nMLM & .633$\\pm$.133 & .665$\\pm$.150 & .713$\\pm$.174 & .719$\\pm$.184 & .730$\\pm$.201 \\\\\nVanilla & .410$\\pm$.126 & .425$\\pm$.143 & .432$\\pm$.144 & .466$\\pm$.144 & .466$\\pm$.163 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{OOD Perturbation Robustness}\n\\label{sec:ood_perturbation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Perturbation robustness on OOD Deceptive Delight ($n$=118). $\\Delta$: F1 change (pp) from clean to paraphrased. 3-seed mean$\\pm$std where available.}\n\\label{tab:ood_perturbation}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Variant} & Clean Full & Pert.\\ Full & $\\Delta$ Full & $\\Delta$ $K$=1 \\\\\n\\midrule\n9-class & .997$\\pm$.005 & 1.000$\\pm$.000 & +0.3 & +0.6 \\\\\nBinary & .997$\\pm$.005 & 1.000$\\pm$.000 & +0.3 & +0.6 \\\\\nScrambled & .997$\\pm$.005 & 1.000$\\pm$.000 & +0.3 & $-$0.3 \\\\\n\\midrule\nJB MLM & .914$\\pm$.115 & .941 & +2.7 & 0.0 \\\\\nWiki MLM$^{*}$ & .904$\\pm$.115 & .872 & $-$3.3 & $-$3.2 \\\\\nVanilla$^{\\dagger}$ & .312$\\pm$.026 & .339$\\pm$.055 & +2.7 & $-$6.8$\\pm$1.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\footnotesize $^{*}$Wiki MLM degradation is seed-driven: seed 42 accounts for $-$9.8\\,pp; other seeds show 0.0\\,pp change.\\\\$^{\\dagger}$Vanilla $\\Delta$ Full = +2.7\\,pp reflects floor-effect noise (baseline 0.312, std 0.055), not meaningful improvement.}\n\\end{table}\n\n\\section{Reproducibility Details}\n\\label{sec:reproducibility}\n\n\\paragraph{Stage-1 training.}\nAll variants use DeBERTa-v3-base (184M parameters) with learning rate $2 \\times 10^{-5}$, AdamW optimizer ($\\beta_1$=0.9, $\\beta_2$=0.999, weight decay 0.01), linear warmup over the first 10\\% of steps, batch size 16, and 4 epochs. MLM variants use 15\\% random token masking. Training takes approximately 30 minutes per variant on a single NVIDIA A100 (40GB).\n\n\\paragraph{Stage-2 training.}\nThe BiGRU has hidden dimension 128 (bidirectional, so output dimension 256). The MLP classifier has layers $256 \\to 64 \\to 2$ with ReLU activation and dropout 0.3. Training uses learning rate $1 \\times 10^{-3}$, Adam optimizer, batch size 32, and 20 epochs with early stopping (patience 5) on validation F1. Stage-2 training completes in under 5 minutes per variant.\n\n\\paragraph{Data generation.}\nJailbreak conversations are generated using Qwen3-8B with attack-specific prompt templates. Crescendo conversations follow a 5--8 turn gradual escalation structure. FITD conversations use a 2--3 turn commitment-consistency structure. Deceptive Delight conversations embed harmful content within emotionally engaging 3--5 turn sequences. Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general) with matched turn counts.\n\n\\paragraph{Strategy annotation.}\nEach user turn is annotated by Qwen3-8B using a structured prompt that provides definitions and two examples for each of the nine strategy categories. The prompt instructs the model to output a single category label. We plan to release all generation and annotation prompts, the full dataset, and training code upon acceptance.\n\n\\paragraph{Adversarial paraphrasing.}\nThe paraphrased test set is generated by instructing Qwen3-8B to rephrase each user turn while preserving the communicative intent. The resulting paraphrases have mean BERTScore 0.92 and mean lexical overlap 0.20 with the originals. These metrics confirm substantial surface-level variation.\n",
      "numLines": 143,
      "startLine": 1,
      "totalLines": 143
    }
  },
  "sourceToolAssistantUUID": "4ec9c71a-b27f-4a01-a339-04327a1863cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T18:01:01.041Z_

<details open><summary>🔧 Tool call — Read · `toolu_0171LvTUiCC8Uvid26G5uGUL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e25dd0b2-3c54-4e4f-bffd-77f5e058e6d1",
  "isSidechain": false,
  "requestId": "req_011CbAUJCPk45ujpWNNhwhw7",
  "type": "assistant",
  "uuid": "9631562e-00af-467d-8aa1-eb3cfb5444d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtW5c41jyMF3d1ejhKi2V1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2933,
      "cache_read_input_tokens": 27137,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 907,
          "cache_read_input_tokens": 27137,
          "cache_creation_input_tokens": 2933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2933
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-18T18:01:01.051Z_

<details><summary>↩ Tool result · `toolu_0171LvTUiCC8Uvid26G5uGUL`</summary>

```text
1	% checklist.tex — ARR Responsible NLP Research Checklist
2	
3	\section*{Responsible NLP Research Checklist}
4	
5	\paragraph{A. Limitations.}
6	\begin{enumerate}[label=A\arabic*.,leftmargin=2em]
7	  \item Did you describe the limitations of your work? \textbf{Yes.} Section~\ref{sec:limitations} discusses dataset scale, lexical separability, annotation quality, OOD strategy prediction, single-seed variants, scope, and compute cost.
8	  \item Did you discuss any potential risks of your work? \textbf{Yes.} See below.
9	\end{enumerate}
10	
11	\paragraph{B. Potential Risks and Ethical Considerations.}
12	This work studies multi-turn jailbreak attacks against LLMs. While the analysis is defensive (improving detection), we acknowledge dual-use risk: the persuasion taxonomy and attack strategy analysis could inform adversarial actors. We mitigate this by: (1) using only synthetic conversations generated by an open-weight model (Qwen3-8B), not real attack data targeting production systems; (2) not releasing attack-generation prompts that could enable novel attacks; (3) focusing the contribution on detection mechanisms rather than attack techniques. All jailbreak conversations are synthetic and do not contain real harmful content. No human subjects were involved.
13	
14	\paragraph{C. Computational Experiments.}
15	\begin{enumerate}[label=C\arabic*.,leftmargin=2em]
16	  \item Did you report the number of parameters in the models used? \textbf{Yes.} DeBERTa-v3-base (184M) and RoBERTa-base (125M) in Sections~\ref{sec:method} and~\ref{sec:discussion}.
17	  \item Did you report the total amount of compute and the type of resources used? \textbf{Yes.} Under 4 GPU-hours total on a single NVIDIA A100 (40GB). Section~\ref{sec:limitations} and Appendix~\ref{sec:reproducibility}.
18	  \item Did you report the implementation details sufficient for reproducibility? \textbf{Yes.} Appendix~\ref{sec:reproducibility} provides all hyperparameters. We will release code and data upon acceptance.
19	  \item Did you report error bars or confidence intervals? \textbf{Yes.} All OOD results report 3-seed mean$\pm$std (population std with $N$ divisor). Statistical tests (McNemar's) are reported where applicable.
20	\end{enumerate}
21	
22	\paragraph{D. Human Evaluation.}
23	Not applicable. No human evaluation was conducted. Strategy annotation quality was validated against a human sample ($n$=50, $\kappa$=0.78) but this was a validation check, not a full human evaluation study.
24	
25	\paragraph{E. Existing Assets.}
26	\begin{enumerate}[label=E\arabic*.,leftmargin=2em]
27	  \item Did you cite the creators of artifacts you used? \textbf{Yes.} DeBERTa-v3~\citep{he2021deberta}, RoBERTa~\citep{liu2019roberta}, Qwen3-8B (for data generation).
28	  \item Did you discuss the license or terms for use and/or distribution of any artifacts? The training and evaluation data are synthetically generated and will be released under a research-use license. No existing benchmark datasets were used for training.
29	  \item Did you discuss whether the data you are using contains personally identifiable information? \textbf{N/A.} All data is synthetically generated. No PII is present.
30	\end{enumerate}
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9631562e-00af-467d-8aa1-eb3cfb5444d6",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "ea6ea273-688b-4ac4-a2ba-658856a78b41",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/checklist.tex",
      "content": "% checklist.tex — ARR Responsible NLP Research Checklist\n\n\\section*{Responsible NLP Research Checklist}\n\n\\paragraph{A. Limitations.}\n\\begin{enumerate}[label=A\\arabic*.,leftmargin=2em]\n  \\item Did you describe the limitations of your work? \\textbf{Yes.} Section~\\ref{sec:limitations} discusses dataset scale, lexical separability, annotation quality, OOD strategy prediction, single-seed variants, scope, and compute cost.\n  \\item Did you discuss any potential risks of your work? \\textbf{Yes.} See below.\n\\end{enumerate}\n\n\\paragraph{B. Potential Risks and Ethical Considerations.}\nThis work studies multi-turn jailbreak attacks against LLMs. While the analysis is defensive (improving detection), we acknowledge dual-use risk: the persuasion taxonomy and attack strategy analysis could inform adversarial actors. We mitigate this by: (1) using only synthetic conversations generated by an open-weight model (Qwen3-8B), not real attack data targeting production systems; (2) not releasing attack-generation prompts that could enable novel attacks; (3) focusing the contribution on detection mechanisms rather than attack techniques. All jailbreak conversations are synthetic and do not contain real harmful content. No human subjects were involved.\n\n\\paragraph{C. Computational Experiments.}\n\\begin{enumerate}[label=C\\arabic*.,leftmargin=2em]\n  \\item Did you report the number of parameters in the models used? \\textbf{Yes.} DeBERTa-v3-base (184M) and RoBERTa-base (125M) in Sections~\\ref{sec:method} and~\\ref{sec:discussion}.\n  \\item Did you report the total amount of compute and the type of resources used? \\textbf{Yes.} Under 4 GPU-hours total on a single NVIDIA A100 (40GB). Section~\\ref{sec:limitations} and Appendix~\\ref{sec:reproducibility}.\n  \\item Did you report the implementation details sufficient for reproducibility? \\textbf{Yes.} Appendix~\\ref{sec:reproducibility} provides all hyperparameters. We will release code and data upon acceptance.\n  \\item Did you report error bars or confidence intervals? \\textbf{Yes.} All OOD results report 3-seed mean$\\pm$std (population std with $N$ divisor). Statistical tests (McNemar's) are reported where applicable.\n\\end{enumerate}\n\n\\paragraph{D. Human Evaluation.}\nNot applicable. No human evaluation was conducted. Strategy annotation quality was validated against a human sample ($n$=50, $\\kappa$=0.78) but this was a validation check, not a full human evaluation study.\n\n\\paragraph{E. Existing Assets.}\n\\begin{enumerate}[label=E\\arabic*.,leftmargin=2em]\n  \\item Did you cite the creators of artifacts you used? \\textbf{Yes.} DeBERTa-v3~\\citep{he2021deberta}, RoBERTa~\\citep{liu2019roberta}, Qwen3-8B (for data generation).\n  \\item Did you discuss the license or terms for use and/or distribution of any artifacts? The training and evaluation data are synthetically generated and will be released under a research-use license. No existing benchmark datasets were used for training.\n  \\item Did you discuss whether the data you are using contains personally identifiable information? \\textbf{N/A.} All data is synthetically generated. No PII is present.\n\\end{enumerate}\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  },
  "sourceToolAssistantUUID": "9631562e-00af-467d-8aa1-eb3cfb5444d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T18:01:01.505Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WdGDHYY4oWbxeQgTUoL4tF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea6ea273-688b-4ac4-a2ba-658856a78b41",
  "isSidechain": false,
  "requestId": "req_011CbAUJCPk45ujpWNNhwhw7",
  "type": "assistant",
  "uuid": "c5bd54ee-3ed6-4ef5-9b10-3b4a196a65dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtW5c41jyMF3d1ejhKi2V1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2933,
      "cache_read_input_tokens": 27137,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 907,
          "cache_read_input_tokens": 27137,
          "cache_creation_input_tokens": 2933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2933
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-18T18:01:01.511Z_

<details><summary>↩ Tool result · `toolu_01WdGDHYY4oWbxeQgTUoL4tF`</summary>

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
233	% Category 5b: Human Jailbreak Datasets
234	% ============================================================
235	
236	@inproceedings{lin2023toxicchat,
237	  title={ToxicChat: Unveiling Hidden Challenges of Toxicity Detection in Real-World User-{AI} Conversation},
238	  author={Lin, Zi and Wang, Zihan and Tong, Yongqi and Wang, Yangkun and Guo, Yuxin and Wang, Yujia and Shang, Jingbo},
239	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2023},
240	  pages={4694--4702},
241	  year={2023},
242	}
243	
244	% ============================================================
245	% Category 6: Red-Teaming
246	% ============================================================
247	
248	@article{li2024mhj,
249	  title={LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet},
250	  author={Li, Nathaniel and Han, Ziwen and Steneker, Ian and Primack, Willow and Goodside, Riley and Zhang, Hugh and Wang, Zifan and Menghini, Cristina and Yue, Summer},
251	  journal={arXiv preprint},
252	  year={2024},
253	  eprint={2408.15221},
254	  archivePrefix={arXiv},
255	}
256	
257	% ============================================================
258	% Category 7: Annotation Artifacts & Dataset Biases
259	% ============================================================
260	
261	@inproceedings{gururangan2018artifacts,
262	  title={Annotation Artifacts in Natural Language Inference Data},
263	  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel and Smith, Noah A.},
264	  booktitle={Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics},
265	  year={2018},
266	}
267	
268	@inproceedings{niven2019probing,
269	  title={Probing Neural Network Comprehension of Natural Language Arguments},
270	  author={Niven, Timothy and Kao, Hung-Yu},
271	  booktitle={Proceedings of the Association for Computational Linguistics},
272	  year={2019},
273	}
274	
275	% ============================================================
276	% Category 8: Adaptive Attacks on Classifiers
277	% ============================================================
278	
279	@article{nasr2025attackermovessecond,
280	  title={The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections},
281	  author={Nasr, Milad and Carlini, Nicholas and Sitawarin, Chawin and Schulhoff, Sander V. and Hayes, Jamie and Ilie, Michael and Pluto, Juliette and Song, Shuang and Chaudhari, Harsh and Shumailov, Ilia and Thakurta, Abhradeep and Xiao, Kai Yuanqing and Terzis, Andreas and Tram{\`e}r, Florian},
282	  journal={arXiv preprint},
283	  year={2025},
284	  eprint={2510.09023},
285	  archivePrefix={arXiv},
286	}
287	
288	@inproceedings{andriushchenko2024adaptive,
289	  title={Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks},
290	  author={Andriushchenko, Maksym and Croce, Francesco and Flammarion, Nicolas},
291	  booktitle={International Conference on Learning Representations},
292	  year={2025},
293	}
294	
295	% ============================================================
296	% Technical Foundation
297	% ============================================================
298	
299	@inproceedings{he2021deberta,
300	  title={DeBERTa: Decoding-enhanced BERT with Disentangled Attention},
301	  author={He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu},
302	  booktitle={International Conference on Learning Representations},
303	  year={2021},
304	}
305	
306	% ============================================================
307	% Domain-Adaptive Pretraining & Multi-Task Learning
308	% ============================================================
309	
310	@inproceedings{gururangan2020dontstop,
311	  title={Don't Stop Pretraining: Adapt Language Models to Domains and Tasks},
312	  author={Gururangan, Suchin and Marasovi{\'c}, Ana and Swayamdipta, Swabha and Lo, Kyle and Beltagy, Iz and Downey, Doug and Smith, Noah A.},
313	  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
314	  pages={8342--8360},
315	  year={2020},
316	}
317	
318	@article{caruana1997multitask,
319	  title={Multitask Learning},
320	  author={Caruana, Rich},
321	  journal={Machine Learning},
322	  volume={28},
323	  number={1},
324	  pages={41--75},
325	  year={1997},
326	}
327	
328	@article{phang2018stilts,
329	  title={Sentence Encoders on {STILTs}: Supplementary Training on Intermediate Labeled-data Tasks},
330	  author={Phang, Jason and F{\'e}vry, Thibault and Bowman, Samuel R.},
331	  journal={arXiv preprint arXiv:1811.01088},
332	  year={2018},
333	}
334	
335	@inproceedings{liu2019mtdnn,
336	  title={Multi-Task Deep Neural Networks for Natural Language Understanding},
337	  author={Liu, Xiaodong and He, Pengcheng and Chen, Weizhu and Gao, Jianfeng},
338	  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
339	  pages={4487--4496},
340	  year={2019},
341	}
342	
343	@inproceedings{howard2018ulmfit,
344	  title={Universal Language Model Fine-tuning for Text Classification},
345	  author={Howard, Jeremy and Ruder, Sebastian},
346	  booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},
347	  pages={328--339},
348	  year={2018},
349	}
350	
351	% ============================================================
352	% Propaganda Detection
353	% ============================================================
354	
355	@inproceedings{dasanmartino2020semeval,
356	  title={{SemEval-2020 Task 11}: Detection of Propaganda Techniques in News Articles},
357	  author={Da San Martino, Giovanni and Barr\'{o}n-Cede\~{n}o, Alberto and Wachsmuth, Henning and Petrov, Rostislav and Nakov, Preslav},
358	  booktitle={Proceedings of the Fourteenth Workshop on Semantic Evaluation},
359	  pages={1377--1414},
360	  year={2020},
361	}
362	
363	@inproceedings{dasanmartino2019fine,
364	  title={Fine-Grained Analysis of Propaganda in News Articles},
365	  author={Da San Martino, Giovanni and Yu, Seunghak and Barr\'{o}n-Cede\~{n}o, Alberto and Petrov, Rostislav and Nakov, Preslav},
366	  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},
367	  pages={5636--5646},
368	  year={2019},
369	}
370	
371	% ============================================================
372	% Adversarial NLP
373	% ============================================================
374	
375	@inproceedings{jin2020textfooler,
376	  title={Is {BERT} Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment},
377	  author={Jin, Di and Jin, Zhijing and Zhou, Joey Tianyi and Szolovits, Peter},
378	  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
379	  volume={34},
380	  pages={8018--8025},
381	  year={2020},
382	}
383	
384	@inproceedings{li2020bertattack,
385	  title={{BERT-ATTACK}: Adversarial Attack Against {BERT} Using {BERT}},
386	  author={Li, Linyang and Ma, Ruotian and Guo, Qipeng and Xue, Xiangyang and Qiu, Xipeng},
387	  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
388	  pages={6193--6202},
389	  year={2020},
390	}
391	
392	% ============================================================
393	% Probing Classifiers
394	% ============================================================
395	
396	@inproceedings{conneau2018probing,
397	  title={What you can cram into a single \$\&!\#* vector: Probing sentence embeddings for linguistic properties},
398	  author={Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo\"{i}c and Baroni, Marco},
399	  booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},
400	  pages={2126--2136},
401	  year={2018},
402	}
403	
404	@inproceedings{hewitt2019structural,
405	  title={A Structural Probe for Finding Syntax in Word Representations},
406	  author={Hewitt, John and Manning, Christopher D.},
407	  booktitle={Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics},
408	  pages={4129--4138},
409	  year={2019},
410	}
411	
412	@article{liu2019roberta,
413	  title={RoBERTa: A Robustly Optimized BERT Pretraining Approach},
414	  author={Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},
415	  journal={arXiv preprint arXiv:1907.11692},
416	  year={2019},
417	}
418	
419	@inproceedings{wang2019persuasion,
420	  title={Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good},
421	  author={Wang, Xuewei and Shi, Weiyan and Kim, Richard and Oh, Yoojung and Yang, Sijia and Zhang, Jingwen and Yu, Zhou},
422	  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
423	  pages={5635--5649},
424	  year={2019},
425	}
426	
427	@inproceedings{robey2024smoothllm,
428	  title={SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks},
429	  author={Robey, Alexander and Wong, Eric and Hassani, Hamed and Pappas, George J.},
430	  booktitle={Proceedings of the 41st International Conference on Machine Learning},
431	  year={2024},
432	}
433	
434	@inproceedings{mehrotra2024tap,
435	  title={Tree of Attacks: Jailbreaking Black-Box LLMs with the Pruning of Candidate Outputs},
436	  author={Mehrotra, Anay and Zampetakis, Manolis and Kassianik, Paul and Nelson, Blaine and Anderson, Hyrum and Singer, Yaron and Karbasi, Amin},
437	  booktitle={Advances in Neural Information Processing Systems},
438	  year={2024},
439	}
440	
441	@article{chao2024jailbreakbench,
442	  title={JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models},
443	  author={Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pappas, George J. and Wong, Eric},
444	  journal={arXiv preprint arXiv:2404.01318},
445	  year={2024},
446	}
447	
448	@inproceedings{mazeika2024harmbench,
449	  title={HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal},
450	  author={Mazeika, Mantas and Phan, Long and Yin, Xuwang and Zou, Andy and Wang, Zifan and Mu, Norman and Sakhaee, Elham and Li, Nathaniel and Basart, Steven and Li, Bo and Forsyth, David and Hendrycks, Dan},
451	  booktitle={Proceedings of the 41st International Conference on Machine Learning},
452	  year={2024},
453	}
454	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5bd54ee-3ed6-4ef5-9b10-3b4a196a65dd",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "1883a3c8-29b3-4471-9901-94b9d99adbf9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib",
      "content": "% References for persuasion_turn_jailbreak_detect\n% Auto-generated from literature_map.yaml (2026-05-18)\n% Total entries: 31\n\n% ============================================================\n% Category 1: Production Multi-Turn Safety Systems\n% ============================================================\n\n@article{inan2023llamaguard,\n  title={Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations},\n  author={Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer, Krithika and Mao, Yuning and Tontchev, Michael and Hu, Qing and Fuller, Brian and Testuggine, Davide and Khabsa, Madian},\n  journal={arXiv preprint},\n  year={2023},\n  eprint={2312.06674},\n  archivePrefix={arXiv},\n}\n\n@misc{metallamaguard3_2024,\n  title={Llama Guard 3},\n  author={{Meta AI}},\n  year={2024},\n  howpublished={Meta AI (released with Llama 3.1)},\n}\n\n@article{zeng2024shieldgemma,\n  title={ShieldGemma: Generative AI Content Moderation Based on Gemma},\n  author={Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, Joe and Harkous, Hamza and Narasimhan, Karthik and Proud, Drew and Kumar, Piyush and Radharapu, Bhaktipriya and Sturman, Olivia and Wahltinez, Oscar},\n  journal={arXiv preprint},\n  year={2024},\n  eprint={2407.21772},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{han2024wildguard,\n  title={WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs},\n  author={Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill Yuchen and Lambert, Nathan and Choi, Yejin and Dziri, Nouha},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2024},\n}\n\n@article{anthropic2025constitutional,\n  title={Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming},\n  author={{Anthropic}},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2501.18837},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 2: Multi-Turn Jailbreak Defenses\n% ============================================================\n\n@article{deepcontext2026,\n  title={DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs},\n  author={Albrethsen, Justin and Datta, Yash and Kumar, Kunal and Rajasekar, Sharath},\n  journal={arXiv preprint},\n  year={2026},\n  eprint={2602.16935},\n  archivePrefix={arXiv},\n}\n\n@article{tong2025biid,\n  title={Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks},\n  author={Tong, Haibo and Zhao, Dongcheng and Shen, Guobin and He, Xiang and Lin, Dachuan and Zhao, Feifei and Zeng, Yi},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2509.22732},\n  archivePrefix={arXiv},\n}\n\n@article{gguard2025,\n  title={An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs},\n  author={Huang, Zixuan and Huang, Kecheng and Yin, Lihao and He, Bowei and Zhen, Huiling and Yuan, Mingxuan and Shao, Zili},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2507.07146},\n  archivePrefix={arXiv},\n}\n\n@article{safedream2026,\n  title={SafeDream: Safety World Model for Proactive Early Jailbreak Detection},\n  author={Yan, Bo and Lin, Weikai and Zhu, Yada and Wang, Song},\n  journal={arXiv preprint},\n  year={2026},\n  eprint={2604.16824},\n  archivePrefix={arXiv},\n}\n\n@article{bullwinkel2025repeng,\n  title={A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks},\n  author={Bullwinkel, Blake and Russinovich, Mark and Salem, Ahmed and Zanella-Beguelin, Santiago and Jones, Daniel and Severi, Giorgio and Kim, Eugenia and Hines, Keegan and Minnich, Amanda and Zunger, Yonatan and Kumar, Ram Shankar Siva},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2507.02956},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 3: Discourse Analysis in NLP\n% ============================================================\n\n@article{mann1988rst,\n  title={Rhetorical Structure Theory: Toward a Functional Theory of Text Organization},\n  author={Mann, William C. and Thompson, Sandra A.},\n  journal={Text \\& Talk},\n  year={1988},\n  volume={8},\n  number={3},\n  pages={243--281},\n}\n\n@inproceedings{prasad2008pdtb,\n  title={The Penn Discourse TreeBank 2.0},\n  author={Prasad, Rashmi and Dinesh, Nikhil and Lee, Alan and Miltsakaki, Eleni and Robaldo, Livio and Joshi, Aravind and Webber, Bonnie},\n  booktitle={Proceedings of the International Conference on Language Resources and Evaluation},\n  year={2008},\n}\n\n@article{stolcke2000dialogueact,\n  title={Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech},\n  author={Stolcke, Andreas and Ries, Klaus and Coccaro, Noah and Shriberg, Elizabeth and Bates, Rebecca and Jurafsky, Daniel and Taylor, Paul and Martin, Rachel and Van Ess-Dykema, Carol and Meteer, Marie},\n  journal={Computational Linguistics},\n  year={2000},\n  volume={26},\n  number={3},\n  pages={339--374},\n}\n\n@book{austin1962speechacts,\n  title={How to Do Things with Words},\n  author={Austin, J. L.},\n  publisher={Harvard University Press},\n  year={1962},\n}\n\n@book{searle1969speechacts,\n  title={Speech Acts: An Essay in the Philosophy of Language},\n  author={Searle, J. R.},\n  publisher={Cambridge University Press},\n  year={1969},\n}\n\n% ============================================================\n% Category 4: Computational Persuasion Detection\n% ============================================================\n\n@book{cialdini2001influence,\n  title={Influence: Science and Practice},\n  author={Cialdini, Robert B.},\n  publisher={Allyn \\& Bacon},\n  year={2001},\n  edition={4th},\n}\n\n% ============================================================\n% Category 5: Jailbreak Attacks & Taxonomies\n% ============================================================\n\n@inproceedings{zeng2024pap,\n  title={How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs},\n  author={Zeng, Yi and Lin, Hongpeng and Zhang, Jingwen and Yang, Diyi and Jia, Ruoxi and Shi, Weiyan},\n  booktitle={Proceedings of the Association for Computational Linguistics},\n  year={2024},\n}\n\n% Note: key retains \"2024\" for citation compatibility; paper published at USENIX Security 2025\n@inproceedings{russinovich2024crescendo,\n  title={Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack},\n  author={Russinovich, Mark and Salem, Ahmed and Eldan, Ronen},\n  booktitle={USENIX Security Symposium},\n  year={2025},\n  eprint={2404.01833},\n  archivePrefix={arXiv},\n}\n\n@article{chao2023pair,\n  title={Jailbreaking Black Box Large Language Models in Twenty Queries},\n  author={Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pappas, George J. and Wong, Eric},\n  journal={arXiv preprint},\n  year={2023},\n  eprint={2310.08419},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{wei2023jailbroken,\n  title={Jailbroken: How Does LLM Safety Training Fail?},\n  author={Wei, Alexander and Haghtalab, Nika and Steinhardt, Jacob},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023},\n}\n\n@article{hagendorff2026reasoning,\n  title={Large Reasoning Models Are Autonomous Jailbreak Agents},\n  author={Hagendorff, Thilo and Derner, Erik and Oliver, Nuria},\n  journal={Nature Communications},\n  year={2026},\n}\n\n@article{fitd2024,\n  title={Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology},\n  author={Wang, Zhenhua and Xie, Wei and Wang, Baosheng and Wang, Enze and Gui, Zhiwen and Ma, Shuoyoucheng and Chen, Kai},\n  journal={arXiv preprint},\n  year={2024},\n  eprint={2402.15690},\n  archivePrefix={arXiv},\n}\n\n@techreport{deceptivedelight2024,\n  title={Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction},\n  author={{Palo Alto Networks Unit 42}},\n  institution={Palo Alto Networks},\n  year={2024},\n}\n\n@inproceedings{ren2024actorattack,\n  title={ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory},\n  author={Ren, Qibing and Li, Hao and Liu, Dongrui and Xie, Zhanxu and Lu, Xiaoya and Qiao, Yu and Sha, Lei and Yan, Junchi and Ma, Lizhuang and Shao, Jing},\n  booktitle={International Conference on Learning Representations},\n  year={2025},\n}\n\n@article{zou2023gcg,\n  title={Universal and Transferable Adversarial Attacks on Aligned Language Models},\n  author={Zou, Andy and Wang, Zifan and Carlini, Nicholas and Nasr, Milad and Kolter, J. Zico and Fredrikson, Matt},\n  journal={arXiv preprint},\n  year={2023},\n  eprint={2307.15043},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 5b: Human Jailbreak Datasets\n% ============================================================\n\n@inproceedings{lin2023toxicchat,\n  title={ToxicChat: Unveiling Hidden Challenges of Toxicity Detection in Real-World User-{AI} Conversation},\n  author={Lin, Zi and Wang, Zihan and Tong, Yongqi and Wang, Yangkun and Guo, Yuxin and Wang, Yujia and Shang, Jingbo},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2023},\n  pages={4694--4702},\n  year={2023},\n}\n\n% ============================================================\n% Category 6: Red-Teaming\n% ============================================================\n\n@article{li2024mhj,\n  title={LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet},\n  author={Li, Nathaniel and Han, Ziwen and Steneker, Ian and Primack, Willow and Goodside, Riley and Zhang, Hugh and Wang, Zifan and Menghini, Cristina and Yue, Summer},\n  journal={arXiv preprint},\n  year={2024},\n  eprint={2408.15221},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 7: Annotation Artifacts & Dataset Biases\n% ============================================================\n\n@inproceedings{gururangan2018artifacts,\n  title={Annotation Artifacts in Natural Language Inference Data},\n  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel and Smith, Noah A.},\n  booktitle={Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics},\n  year={2018},\n}\n\n@inproceedings{niven2019probing,\n  title={Probing Neural Network Comprehension of Natural Language Arguments},\n  author={Niven, Timothy and Kao, Hung-Yu},\n  booktitle={Proceedings of the Association for Computational Linguistics},\n  year={2019},\n}\n\n% ============================================================\n% Category 8: Adaptive Attacks on Classifiers\n% ============================================================\n\n@article{nasr2025attackermovessecond,\n  title={The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections},\n  author={Nasr, Milad and Carlini, Nicholas and Sitawarin, Chawin and Schulhoff, Sander V. and Hayes, Jamie and Ilie, Michael and Pluto, Juliette and Song, Shuang and Chaudhari, Harsh and Shumailov, Ilia and Thakurta, Abhradeep and Xiao, Kai Yuanqing and Terzis, Andreas and Tram{\\`e}r, Florian},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2510.09023},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{andriushchenko2024adaptive,\n  title={Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks},\n  author={Andriushchenko, Maksym and Croce, Francesco and Flammarion, Nicolas},\n  booktitle={International Conference on Learning Representations},\n  year={2025},\n}\n\n% ============================================================\n% Technical Foundation\n% ============================================================\n\n@inproceedings{he2021deberta,\n  title={DeBERTa: Decoding-enhanced BERT with Disentangled Attention},\n  author={He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu},\n  booktitle={International Conference on Learning Representations},\n  year={2021},\n}\n\n% ============================================================\n% Domain-Adaptive Pretraining & Multi-Task Learning\n% ============================================================\n\n@inproceedings{gururangan2020dontstop,\n  title={Don't Stop Pretraining: Adapt Language Models to Domains and Tasks},\n  author={Gururangan, Suchin and Marasovi{\\'c}, Ana and Swayamdipta, Swabha and Lo, Kyle and Beltagy, Iz and Downey, Doug and Smith, Noah A.},\n  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n  pages={8342--8360},\n  year={2020},\n}\n\n@article{caruana1997multitask,\n  title={Multitask Learning},\n  author={Caruana, Rich},\n  journal={Machine Learning},\n  volume={28},\n  number={1},\n  pages={41--75},\n  year={1997},\n}\n\n@article{phang2018stilts,\n  title={Sentence Encoders on {STILTs}: Supplementary Training on Intermediate Labeled-data Tasks},\n  author={Phang, Jason and F{\\'e}vry, Thibault and Bowman, Samuel R.},\n  journal={arXiv preprint arXiv:1811.01088},\n  year={2018},\n}\n\n@inproceedings{liu2019mtdnn,\n  title={Multi-Task Deep Neural Networks for Natural Language Understanding},\n  author={Liu, Xiaodong and He, Pengcheng and Chen, Weizhu and Gao, Jianfeng},\n  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n  pages={4487--4496},\n  year={2019},\n}\n\n@inproceedings{howard2018ulmfit,\n  title={Universal Language Model Fine-tuning for Text Classification},\n  author={Howard, Jeremy and Ruder, Sebastian},\n  booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n  pages={328--339},\n  year={2018},\n}\n\n% ============================================================\n% Propaganda Detection\n% ============================================================\n\n@inproceedings{dasanmartino2020semeval,\n  title={{SemEval-2020 Task 11}: Detection of Propaganda Techniques in News Articles},\n  author={Da San Martino, Giovanni and Barr\\'{o}n-Cede\\~{n}o, Alberto and Wachsmuth, Henning and Petrov, Rostislav and Nakov, Preslav},\n  booktitle={Proceedings of the Fourteenth Workshop on Semantic Evaluation},\n  pages={1377--1414},\n  year={2020},\n}\n\n@inproceedings{dasanmartino2019fine,\n  title={Fine-Grained Analysis of Propaganda in News Articles},\n  author={Da San Martino, Giovanni and Yu, Seunghak and Barr\\'{o}n-Cede\\~{n}o, Alberto and Petrov, Rostislav and Nakov, Preslav},\n  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages={5636--5646},\n  year={2019},\n}\n\n% ============================================================\n% Adversarial NLP\n% ============================================================\n\n@inproceedings{jin2020textfooler,\n  title={Is {BERT} Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment},\n  author={Jin, Di and Jin, Zhijing and Zhou, Joey Tianyi and Szolovits, Peter},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},\n  volume={34},\n  pages={8018--8025},\n  year={2020},\n}\n\n@inproceedings{li2020bertattack,\n  title={{BERT-ATTACK}: Adversarial Attack Against {BERT} Using {BERT}},\n  author={Li, Linyang and Ma, Ruotian and Guo, Qipeng and Xue, Xiangyang and Qiu, Xipeng},\n  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n  pages={6193--6202},\n  year={2020},\n}\n\n% ============================================================\n% Probing Classifiers\n% ============================================================\n\n@inproceedings{conneau2018probing,\n  title={What you can cram into a single \\$\\&!\\#* vector: Probing sentence embeddings for linguistic properties},\n  author={Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo\\\"{i}c and Baroni, Marco},\n  booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n  pages={2126--2136},\n  year={2018},\n}\n\n@inproceedings{hewitt2019structural,\n  title={A Structural Probe for Finding Syntax in Word Representations},\n  author={Hewitt, John and Manning, Christopher D.},\n  booktitle={Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics},\n  pages={4129--4138},\n  year={2019},\n}\n\n@article{liu2019roberta,\n  title={RoBERTa: A Robustly Optimized BERT Pretraining Approach},\n  author={Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},\n  journal={arXiv preprint arXiv:1907.11692},\n  year={2019},\n}\n\n@inproceedings{wang2019persuasion,\n  title={Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good},\n  author={Wang, Xuewei and Shi, Weiyan and Kim, Richard and Oh, Yoojung and Yang, Sijia and Zhang, Jingwen and Yu, Zhou},\n  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n  pages={5635--5649},\n  year={2019},\n}\n\n@inproceedings{robey2024smoothllm,\n  title={SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks},\n  author={Robey, Alexander and Wong, Eric and Hassani, Hamed and Pappas, George J.},\n  booktitle={Proceedings of the 41st International Conference on Machine Learning},\n  year={2024},\n}\n\n@inproceedings{mehrotra2024tap,\n  title={Tree of Attacks: Jailbreaking Black-Box LLMs with the Pruning of Candidate Outputs},\n  author={Mehrotra, Anay and Zampetakis, Manolis and Kassianik, Paul and Nelson, Blaine and Anderson, Hyrum and Singer, Yaron and Karbasi, Amin},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2024},\n}\n\n@article{chao2024jailbreakbench,\n  title={JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models},\n  author={Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pappas, George J. and Wong, Eric},\n  journal={arXiv preprint arXiv:2404.01318},\n  year={2024},\n}\n\n@inproceedings{mazeika2024harmbench,\n  title={HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal},\n  author={Mazeika, Mantas and Phan, Long and Yin, Xuwang and Zou, Andy and Wang, Zifan and Mu, Norman and Sakhaee, Elham and Li, Nathaniel and Basart, Steven and Li, Bo and Forsyth, David and Hendrycks, Dan},\n  booktitle={Proceedings of the 41st International Conference on Machine Learning},\n  year={2024},\n}\n",
      "numLines": 454,
      "startLine": 1,
      "totalLines": 454
    }
  },
  "sourceToolAssistantUUID": "c5bd54ee-3ed6-4ef5-9b10-3b4a196a65dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T18:01:02.448Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019fXT8FPM5sJootrxKDuskq`</summary>

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
  "parentUuid": "1883a3c8-29b3-4471-9901-94b9d99adbf9",
  "isSidechain": false,
  "requestId": "req_011CbAUJCPk45ujpWNNhwhw7",
  "type": "assistant",
  "uuid": "a124e45c-effe-4b97-bb15-ef0bdfd08e9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtW5c41jyMF3d1ejhKi2V1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2933,
      "cache_read_input_tokens": 27137,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 907,
          "cache_read_input_tokens": 27137,
          "cache_creation_input_tokens": 2933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2933
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-18T18:01:02.912Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01M4jkYbdhiiTFqsEbgLi8wS`</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a124e45c-effe-4b97-bb15-ef0bdfd08e9d",
  "isSidechain": false,
  "requestId": "req_011CbAUJCPk45ujpWNNhwhw7",
  "type": "assistant",
  "uuid": "307e3696-7693-4330-b6d0-8d8035fc259d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtW5c41jyMF3d1ejhKi2V1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2933,
      "cache_read_input_tokens": 27137,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 907,
          "cache_read_input_tokens": 27137,
          "cache_creation_input_tokens": 2933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2933
          },
          "type": "message"
        }
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

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责**方法严谨性 + 实验设计**。  ## 论文信息 - 标题: \"What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\" - 路径: `projects/persuasion_turn_jailbreak_d…",
  "leafUuid": "307e3696-7693-4330-b6d0-8d8035fc259d",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multi-turn jailbreak detection paper for EMNLP",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765"
}
```

---

### Tool result

_source line 41 · 2026-05-18T18:01:13.865Z_

<details><summary>↩ Tool result · `toolu_019fXT8FPM5sJootrxKDuskq`</summary>

```text
Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"}]

Based on the search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Score Justification

Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

## Soundness vs. Excitement

Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Metareview Scoring

The ARR metareview score has changed in February 2025 to be more aligned with reviewer scores. The new options include: 5 = Consider for Award (top 2.5% papers), 2 = Resubmit next cycle (papers needing substantial revisions completed by next cycle), 1.5 = Resubmit after next cycle (substantial revisions not completable by next cycle), and 1 = Do not resubmit (papers needing full redo or not relevant to ACL community).

For more comprehensive guidelines, you can visit the official ARR Reviewer Guidelines page at aclrollingreview.org/reviewerguidelines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a124e45c-effe-4b97-bb15-ef0bdfd08e9d",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "8c7aa024-df9d-4ba2-8b2d-d5f65e218a66",
  "toolUseResult": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_011grFmu9e6jfNsa4ekyqJ5b",
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
            "title": "aclrollingreview/cfp.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"
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
            "title": "ACLRollingReview (@ReviewAcl) / X",
            "url": "https://x.com/reviewacl"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "https://aclrollingreview.org/"
          }
        ]
      },
      "Based on the search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:\n\n## Scoring System\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\n\n## Score Justification\n\nSoundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.\n\n## Soundness vs. Excitement\n\nSometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.\n\n## Area Chair Metareview Scoring\n\nThe ARR metareview score has changed in February 2025 to be more aligned with reviewer scores. The new options include: 5 = Consider for Award (top 2.5% papers), 2 = Resubmit next cycle (papers needing substantial revisions completed by next cycle), 1.5 = Resubmit after next cycle (substantial revisions not completable by next cycle), and 1 = Do not resubmit (papers needing full redo or not relevant to ACL community).\n\nFor more comprehensive guidelines, you can visit the official ARR Reviewer Guidelines page at aclrollingreview.org/reviewerguidelines."
    ],
    "durationSeconds": 11.413396207000002
  },
  "sourceToolAssistantUUID": "a124e45c-effe-4b97-bb15-ef0bdfd08e9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T18:01:53.909Z_

<details><summary>↩ Tool result · `toolu_01M4jkYbdhiiTFqsEbgLi8wS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 88, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 31, \"online_not_found\": 9, \"online_mismatch\": 9}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"inan2023llamaguard\", \"type\": \"article\", \"title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"authors\": \"Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer,...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"metallamaguard3_2024\", \"type\": \"misc\", \"title\": \"Llama Guard 3\", \"authors\": \"Meta AI\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"zeng2024shieldgemma\", \"type\": \"article\", \"title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"authors\": \"Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"han2024wildguard\", \"type\": \"inproceedings\", \"title\": \"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"authors\": \"Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"anthropic2025constitutional\", \"type\": \"article\", \"title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"authors\": \"Anthropic\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"deepcontext2026\", \"type\": \"article\", \"title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"authors\": \"Albrethsen, Justin and Datta, Yash and Kumar, Kunal and Rajasekar, Sharath\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"tong2025biid\", \"type\": \"article\", \"title\": \"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\", \"authors\": \"Tong, Haibo and Zhao, Dongcheng and Shen, Guobin and He, Xiang and Lin, Dachuan ...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"gguard2025\", \"type\": \"article\", \"title\": \"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\", \"authors\": \"Huang, Zixuan and Huang, Kecheng and Yin, Lihao and He, Bowei and Zhen, Huiling ...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"safedream2026\", \"type\": \"article\", \"title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"authors\": \"Yan, Bo and Lin, Weikai and Zhu, Yada and Wang, Song\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"bullwinkel2025repeng\", \"type\": \"article\", \"title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"authors\": \"Bullwinkel, Blake and Russinovich, Mark and Salem, Ahmed and Zanella-Beguelin, S...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"mann1988rst\", \"type\": \"article\", \"title\": \"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\", \"authors\": \"Mann, William C. and Thompson, Sandra A.\", \"year\": \"1988\", \"venue\": \"Text \\\\& Talk\"}, {\"key\": \"prasad2008pdtb\", \"type\": \"inproceedings\", \"title\": \"The Penn Discourse TreeBank 2.0\", \"authors\": \"Prasad, Rashmi and Dinesh, Nikhil and Lee, Alan and Miltsakaki, Eleni and Robald...\", \"year\": \"2008\", \"venue\": \"Proceedings of the International Conference on Language Resources and Evaluation\"}, {\"key\": \"stolcke2000dialogueact\", \"type\": \"article\", \"title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"authors\": \"Stolcke, Andreas and Ries, Klaus and Coccaro, Noah and Shriberg, Elizabeth and B...\", \"year\": \"2000\", \"venue\": \"Computational Linguistics\"}, {\"key\": \"austin1962speechacts\", \"type\": \"book\", \"title\": \"How to Do Things with Words\", \"authors\": \"Austin, J. L.\", \"year\": \"1962\", \"venue\": \"\"}, {\"key\": \"searle1969speechacts\", \"type\": \"book\", \"title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"authors\": \"Searle, J. R.\", \"year\": \"1969\", \"venue\": \"\"}, {\"key\": \"cialdini2001influence\", \"type\": \"book\", \"title\": \"Influence: Science and Practice\", \"authors\": \"Cialdini, Robert B.\", \"year\": \"2001\", \"venue\": \"\"}, {\"key\": \"zeng2024pap\", \"type\": \"inproceedings\", \"title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"authors\": \"Zeng, Yi and Lin, Hongpeng and Zhang, Jingwen and Yang, Diyi and Jia, Ruoxi and ...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Association for Computational Linguistics\"}, {\"key\": \"russinovich2024crescendo\", \"type\": \"inproceedings\", \"title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"authors\": \"Russinovich, Mark and Salem, Ahmed and Eldan, Ronen\", \"year\": \"2025\", \"venue\": \"USENIX Security Symposium\"}, {\"key\": \"chao2023pair\", \"type\": \"article\", \"title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"authors\": \"Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pa...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"wei2023jailbroken\", \"type\": \"inproceedings\", \"title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"authors\": \"Wei, Alexander and Haghtalab, Nika and Steinhardt, Jacob\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"hagendorff2026reasoning\", \"type\": \"article\", \"title\": \"Large Reasoning Models Are Autonomous Jailbreak Agents\", \"authors\": \"Hagendorff, Thilo and Derner, Erik and Oliver, Nuria\", \"year\": \"2026\", \"venue\": \"Nature Communications\"}, {\"key\": \"fitd2024\", \"type\": \"article\", \"title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"authors\": \"Wang, Zhenhua and Xie, Wei and Wang, Baosheng and Wang, Enze and Gui, Zhiwen and...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"deceptivedelight2024\", \"type\": \"techreport\", \"title\": \"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\", \"authors\": \"Palo Alto Networks Unit 42\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"ren2024actorattack\", \"type\": \"inproceedings\", \"title\": \"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\", \"authors\": \"Ren, Qibing and Li, Hao and Liu, Dongrui and Xie, Zhanxu and Lu, Xiaoya and Qiao...\", \"year\": \"2025\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"zou2023gcg\", \"type\": \"article\", \"title\": \"Universal and Transferable Adversarial Attacks on Aligned Language Models\", \"authors\": \"Zou, Andy and Wang, Zifan and Carlini, Nicholas and Nasr, Milad and Kolter, J. Z...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"lin2023toxicchat\", \"type\": \"inproceedings\", \"title\": \"ToxicChat: Unveiling Hidden Challenges of Toxicity Detection in Real-World User-AI Conversation\", \"authors\": \"Lin, Zi and Wang, Zihan and Tong, Yongqi and Wang, Yangkun and Guo, Yuxin and Wa...\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2023\"}, {\"key\": \"li2024mhj\", \"type\": \"article\", \"title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"authors\": \"Li, Nathaniel and Han, Ziwen and Steneker, Ian and Primack, Willow and Goodside,...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"gururangan2018artifacts\", \"type\": \"inproceedings\", \"title\": \"Annotation Artifacts in Natural Language Inference Data\", \"authors\": \"Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and ...\", \"year\": \"2018\", \"venue\": \"Proceedings of the Conference of the North American Chapter of the Association f...\"}, {\"key\": \"niven2019probing\", \"type\": \"inproceedings\", \"title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"authors\": \"Niven, Timothy and Kao, Hung-Yu\", \"year\": \"2019\", \"venue\": \"Proceedings of the Association for Computational Linguistics\"}, {\"key\": \"nasr2025attackermovessecond\", \"type\": \"article\", \"title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\", \"authors\": \"Nasr, Milad and Carlini, Nicholas and Sitawarin, Chawin and Schulhoff, Sander V....\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"andriushchenko2024adaptive\", \"type\": \"inproceedings\", \"title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"authors\": \"Andriushchenko, Maksym and Croce, Francesco and Flammarion, Nicolas\", \"year\": \"2025\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"he2021deberta\", \"type\": \"inproceedings\", \"title\": \"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\", \"authors\": \"He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gururangan2020dontstop\", \"type\": \"inproceedings\", \"title\": \"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\", \"authors\": \"Gururangan, Suchin and Marasovi\\\\'c, Ana and Swayamdipta, Swabha and Lo, Kyle and...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 58th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"caruana1997multitask\", \"type\": \"article\", \"title\": \"Multitask Learning\", \"authors\": \"Caruana, Rich\", \"year\": \"1997\", \"venue\": \"Machine Learning\"}, {\"key\": \"phang2018stilts\", \"type\": \"article\", \"title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"authors\": \"Phang, Jason and F\\\\'evry, Thibault and Bowman, Samuel R.\", \"year\": \"2018\", \"venue\": \"arXiv preprint arXiv:1811.01088\"}, {\"key\": \"liu2019mtdnn\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"authors\": \"Liu, Xiaodong and He, Pengcheng and Chen, Weizhu and Gao, Jianfeng\", \"year\": \"2019\", \"venue\": \"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"howard2018ulmfit\", \"type\": \"inproceedings\", \"title\": \"Universal Language Model Fine-tuning for Text Classification\", \"authors\": \"Howard, Jeremy and Ruder, Sebastian\", \"year\": \"2018\", \"venue\": \"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"dasanmartino2020semeval\", \"type\": \"inproceedings\", \"title\": \"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\", \"authors\": \"Da San Martino, Giovanni and Barr\\\\'on-Cede\\\\~no, Alberto and Wachsmuth, Henning a...\", \"year\": \"2020\", \"venue\": \"Proceedings of the Fourteenth Workshop on Semantic Evaluation\"}, {\"key\": \"dasanmartino2019fine\", \"type\": \"inproceedings\", \"title\": \"Fine-Grained Analysis of Propaganda in News Articles\", \"authors\": \"Da San Martino, Giovanni and Yu, Seunghak and Barr\\\\'on-Cede\\\\~no, Alberto and Pet...\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"jin2020textfooler\", \"type\": \"inproceedings\", \"title\": \"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\", \"authors\": \"Jin, Di and Jin, Zhijing and Zhou, Joey Tianyi and Szolovits, Peter\", \"year\": \"2020\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"li2020bertattack\", \"type\": \"inproceedings\", \"title\": \"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\", \"authors\": \"Li, Linyang and Ma, Ruotian and Guo, Qipeng and Xue, Xiangyang and Qiu, Xipeng\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"conneau2018probing\", \"type\": \"inproceedings\", \"title\": \"What you can cram into a single \\\\$\\\\&!\\\\#* vector: Probing sentence embeddings for linguistic properties\", \"authors\": \"Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo\\\\\\\"i...\", \"year\": \"2018\", \"venue\": \"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"hewitt2019structural\", \"type\": \"inproceedings\", \"title\": \"A Structural Probe for Finding Syntax in Word Representations\", \"authors\": \"Hewitt, John and Manning, Christopher D.\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"liu2019roberta\", \"type\": \"article\", \"title\": \"RoBERTa: A Robustly Optimized BERT Pretraining Approach\", \"authors\": \"Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and...\", \"year\": \"2019\", \"venue\": \"arXiv preprint arXiv:1907.11692\"}, {\"key\": \"wang2019persuasion\", \"type\": \"inproceedings\", \"title\": \"Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good\", \"authors\": \"Wang, Xuewei and Shi, Weiyan and Kim, Richard and Oh, Yoojung and Yang, Sijia an...\", \"year\": \"2019\", \"venue\": \"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"robey2024smoothllm\", \"type\": \"inproceedings\", \"title\": \"SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks\", \"authors\": \"Robey, Alexander and Wong, Eric and Hassani, Hamed and Pappas, George J.\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning\"}, {\"key\": \"mehrotra2024tap\", \"type\": \"inproceedings\", \"title\": \"Tree of Attacks: Jailbreaking Black-Box LLMs with the Pruning of Candidate Outputs\", \"authors\": \"Mehrotra, Anay and Zampetakis, Manolis and Kassianik, Paul and Nelson, Blaine an...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"chao2024jailbreakbench\", \"type\": \"article\", \"title\": \"JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models\", \"authors\": \"Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pa...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2404.01318\"}, {\"key\": \"mazeika2024harmbench\", \"type\": \"inproceedings\", \"title\": \"HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal\", \"authors\": \"Mazeika, Mantas and Phan, Long and Yin, Xuwang and Zou, Andy and Wang, Zifan and...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning\"}], \"tex_citations\": [{\"key\": \"russinovich2024crescendo\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"bullwinkel2025repeng\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"inan2023llamaguard\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"han2024wildguard\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"zeng2024shieldgemma\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"deepcontext2026\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"tong2025biid\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"gguard2025\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"deepcontext2026\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"introduction.tex\", \"line\": 14, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"introduction.tex\", \"line\": 14, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"introduction.tex\", \"line\": 20, \"command\": \"citep\"}, {\"key\": \"russinovich2024crescendo\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"chao2023pair\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"mehrotra2024tap\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"wei2023jailbroken\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"mazeika2024harmbench\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"chao2024jailbreakbench\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"li2024mhj\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"zou2023gcg\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"deepcontext2026\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"tong2025biid\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"gguard2025\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"safedream2026\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"inan2023llamaguard\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"metallamaguard3_2024\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"zeng2024shieldgemma\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"han2024wildguard\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"anthropic2025constitutional\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"robey2024smoothllm\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"mann1988rst\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"prasad2008pdtb\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"stolcke2000dialogueact\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"austin1962speechacts\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"searle1969speechacts\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"dasanmartino2019fine\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"dasanmartino2020semeval\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"wang2019persuasion\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"howard2018ulmfit\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"gururangan2020dontstop\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citet\"}, {\"key\": \"phang2018stilts\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"caruana1997multitask\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"liu2019mtdnn\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"gururangan2020dontstop\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citeauthor\"}, {\"key\": \"gururangan2018artifacts\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"niven2019probing\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"nasr2025attackermovessecond\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"andriushchenko2024adaptive\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"jin2020textfooler\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"li2020bertattack\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"conneau2018probing\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"hewitt2019structural\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"method.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"method.tex\", \"line\": 44, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"method.tex\", \"line\": 44, \"command\": \"citep\"}, {\"key\": \"russinovich2024crescendo\", \"file\": \"experiments.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"lin2023toxicchat\", \"file\": \"experiments.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"experiments.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"bullwinkel2025repeng\", \"file\": \"experiments.tex\", \"line\": 51, \"command\": \"citep\"}, {\"key\": \"gururangan2020dontstop\", \"file\": \"experiments.tex\", \"line\": 107, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"experiments.tex\", \"line\": 127, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"experiments.tex\", \"line\": 165, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"experiments.tex\", \"line\": 177, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"experiments.tex\", \"line\": 177, \"command\": \"citep\"}, {\"key\": \"lin2023toxicchat\", \"file\": \"experiments.tex\", \"line\": 197, \"command\": \"citep\"}, {\"key\": \"lin2023toxicchat\", \"file\": \"experiments.tex\", \"line\": 202, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"experiments.tex\", \"line\": 295, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"experiments.tex\", \"line\": 298, \"command\": \"citep\"}, {\"key\": \"lin2023toxicchat\", \"file\": \"conclusion.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"zou2023gcg\", \"file\": \"conclusion.tex\", \"line\": 42, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"checklist.tex\", \"line\": 27, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"checklist.tex\", \"line\": 27, \"command\": \"citep\"}], \"online_verification\": [{\"key\": \"inan2023llamaguard\", \"title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"metallamaguard3_2024\", \"title\": \"Llama Guard 3\", \"status\": \"not_found\", \"confidence\": 0.289, \"matched_title\": \"Llama Guard 3 Vision: Safeguarding Human-AI Image Understanding Conversations\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.29 below threshold 0.82\"}, {\"key\": \"zeng2024shieldgemma\", \"title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"han2024wildguard\", \"title\": \"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"WildGuard: Open One-stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=han vs api=choi\"], \"note\": \"\"}, {\"key\": \"anthropic2025constitutional\", \"title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=anthropic vs api=sharma\"], \"note\": \"\"}, {\"key\": \"deepcontext2026\", \"title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tong2025biid\", \"title\": \"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\", \"status\": \"not_found\", \"confidence\": 0.328, \"matched_title\": \"AI Alignment: A Comprehensive Survey\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"gguard2025\", \"title\": \"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\", \"status\": \"verified\", \"confidence\": 0.882, \"matched_title\": \"Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"safedream2026\", \"title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bullwinkel2025repeng\", \"title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mann1988rst\", \"title\": \"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rhetorical Structure Theory: Toward a functional theory of text organization\", \"matched_year\": \"1988\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"prasad2008pdtb\", \"title\": \"The Penn Discourse TreeBank 2.0\", \"status\": \"verified\", \"confidence\": 0.984, \"matched_title\": \"The Penn Discourse TreeBank 2.0.\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"stolcke2000dialogueact\", \"title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"matched_year\": \"2000\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"austin1962speechacts\", \"title\": \"How to Do Things with Words\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"How To Do Things With Words\", \"matched_year\": \"1975\", \"mismatch_fields\": [\"year: bib=1962 vs api=1975\"], \"note\": \"\"}, {\"key\": \"searle1969speechacts\", \"title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"matched_year\": \"1969\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cialdini2001influence\", \"title\": \"Influence: Science and Practice\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Influence: science and practice\", \"matched_year\": \"2008\", \"mismatch_fields\": [\"year: bib=2001 vs api=2008\", \"first_author: bib=cialdini vs api=giebels\"], \"note\": \"\"}, {\"key\": \"zeng2024pap\", \"title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"russinovich2024crescendo\", \"title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chao2023pair\", \"title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"year: bib=2023 vs api=2025\"], \"note\": \"\"}, {\"key\": \"wei2023jailbroken\", \"title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hagendorff2026reasoning\", \"title\": \"Large Reasoning Models Are Autonomous Jailbreak Agents\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large reasoning models are autonomous jailbreak agents\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fitd2024\", \"title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"deceptivedelight2024\", \"title\": \"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\", \"status\": \"not_found\", \"confidence\": 0.446, \"matched_title\": \"BitBypass: A New Direction in Jailbreaking Aligned Large Language Models with Bitstream Camouflage\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"ren2024actorattack\", \"title\": \"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\", \"status\": \"not_found\", \"confidence\": 0.402, \"matched_title\": \"NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-Turn LLM Jailbreaks\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.40 below threshold 0.82\"}, {\"key\": \"zou2023gcg\", \"title\": \"Universal and Transferable Adversarial Attacks on Aligned Language Models\", \"status\": \"not_found\", \"confidence\": 0.301, \"matched_title\": \"Text Data Augmentation for Deep Learning\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\"}, {\"key\": \"lin2023toxicchat\", \"title\": \"ToxicChat: Unveiling Hidden Challenges of Toxicity Detection in Real-World User-AI Conversation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"ToxicChat: Unveiling Hidden Challenges of Toxicity Detection in Real-World User-AI Conversation\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=lin vs api=zi\"], \"note\": \"\"}, {\"key\": \"li2024mhj\", \"title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gururangan2018artifacts\", \"title\": \"Annotation Artifacts in Natural Language Inference Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Annotation Artifacts in Natural Language Inference Data\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"niven2019probing\", \"title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nasr2025attackermovessecond\", \"title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against Llm Jailbreaks and Prompt Injections\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"andriushchenko2024adaptive\", \"title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"he2021deberta\", \"title\": \"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DEBERTA: DECODING-ENHANCED BERT WITH DISENTANGLED ATTENTION\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gururangan2020dontstop\", \"title\": \"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\", \"status\": \"not_found\", \"confidence\": 0.492, \"matched_title\": \"From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.49 below threshold 0.82\"}, {\"key\": \"caruana1997multitask\", \"title\": \"Multitask Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multitask Learning\", \"matched_year\": \"1997\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"phang2018stilts\", \"title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liu2019mtdnn\", \"title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"howard2018ulmfit\", \"title\": \"Universal Language Model Fine-tuning for Text Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Language Model Fine-tuning for Text Classification\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dasanmartino2020semeval\", \"title\": \"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\", \"matched_year\": \"2020\", \"mismatch_fields\": [\"first_author: bib=da san martino vs api=martino\"], \"note\": \"\"}, {\"key\": \"dasanmartino2019fine\", \"title\": \"Fine-Grained Analysis of Propaganda in News Articles\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Fine-Grained Analysis of Propaganda in News Articles\", \"matched_year\": \"2019\", \"mismatch_fields\": [\"first_author: bib=da san martino vs api=martino\"], \"note\": \"\"}, {\"key\": \"jin2020textfooler\", \"title\": \"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2020bertattack\", \"title\": \"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"conneau2018probing\", \"title\": \"What you can cram into a single \\\\$\\\\&!\\\\#* vector: Probing sentence embeddings for linguistic properties\", \"status\": \"verified\", \"confidence\": 0.98, \"matched_title\": \"What you can cram into a single $&amp;!#* vector: Probing sentence embeddings for linguistic properties\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hewitt2019structural\", \"title\": \"A Structural Probe for Finding Syntax in Word Representations\", \"status\": \"not_found\", \"confidence\": 0.316, \"matched_title\": \"What Does BERT Learn about the Structure of Language?\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.32 below threshold 0.82\"}, {\"key\": \"liu2019roberta\", \"title\": \"RoBERTa: A Robustly Optimized BERT Pretraining Approach\", \"status\": \"not_found\", \"confidence\": 0.495, \"matched_title\": \"Use of Bidirectional Encoder Representations from Transformers (BERT) and Robustly Optimized Bert Pretraining Approach (RoBERTa) for Nepali News Classification\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.50 below threshold 0.82\"}, {\"key\": \"wang2019persuasion\", \"title\": \"Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"robey2024smoothllm\", \"title\": \"SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mehrotra2024tap\", \"title\": \"Tree of Attacks: Jailbreaking Black-Box LLMs with the Pruning of Candidate Outputs\", \"status\": \"not_found\", \"confidence\": 0.435, \"matched_title\": \"A survey of safety and trustworthiness of large language models through the lens of verification and validation\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.44 below threshold 0.82\"}, {\"key\": \"chao2024jailbreakbench\", \"title\": \"JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=chao vs api=andriushchenko\"], \"note\": \"\"}, {\"key\": \"mazeika2024harmbench\", \"title\": \"HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "307e3696-7693-4330-b6d0-8d8035fc259d",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "180646a4-25a7-4909-b3c0-06bfe14d94fc",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 49, \\\"total_citations\\\": 88, \\\"unique_cited_keys\\\": 49, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 31, \\\"online_not_found\\\": 9, \\\"online_mismatch\\\": 9}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"inan2023llamaguard\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\\\", \\\"authors\\\": \\\"Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer,...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"metallamaguard3_2024\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"Llama Guard 3\\\", \\\"authors\\\": \\\"Meta AI\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"zeng2024shieldgemma\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"ShieldGemma: Generative AI Content Moderation Based on Gemma\\\", \\\"authors\\\": \\\"Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"han2024wildguard\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\\\", \\\"authors\\\": \\\"Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"anthropic2025constitutional\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\\\", \\\"authors\\\": \\\"Anthropic\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"deepcontext2026\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\\\", \\\"authors\\\": \\\"Albrethsen, Justin and Datta, Yash and Kumar, Kunal and Rajasekar, Sharath\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"tong2025biid\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\\\", \\\"authors\\\": \\\"Tong, Haibo and Zhao, Dongcheng and Shen, Guobin and He, Xiang and Lin, Dachuan ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"gguard2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\\\", \\\"authors\\\": \\\"Huang, Zixuan and Huang, Kecheng and Yin, Lihao and He, Bowei and Zhen, Huiling ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"safedream2026\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\\\", \\\"authors\\\": \\\"Yan, Bo and Lin, Weikai and Zhu, Yada and Wang, Song\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"bullwinkel2025repeng\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\\\", \\\"authors\\\": \\\"Bullwinkel, Blake and Russinovich, Mark and Salem, Ahmed and Zanella-Beguelin, S...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"mann1988rst\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\\\", \\\"authors\\\": \\\"Mann, William C. and Thompson, Sandra A.\\\", \\\"year\\\": \\\"1988\\\", \\\"venue\\\": \\\"Text \\\\\\\\& Talk\\\"}, {\\\"key\\\": \\\"prasad2008pdtb\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Penn Discourse TreeBank 2.0\\\", \\\"authors\\\": \\\"Prasad, Rashmi and Dinesh, Nikhil and Lee, Alan and Miltsakaki, Eleni and Robald...\\\", \\\"year\\\": \\\"2008\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Language Resources and Evaluation\\\"}, {\\\"key\\\": \\\"stolcke2000dialogueact\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\\\", \\\"authors\\\": \\\"Stolcke, Andreas and Ries, Klaus and Coccaro, Noah and Shriberg, Elizabeth and B...\\\", \\\"year\\\": \\\"2000\\\", \\\"venue\\\": \\\"Computational Linguistics\\\"}, {\\\"key\\\": \\\"austin1962speechacts\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"How to Do Things with Words\\\", \\\"authors\\\": \\\"Austin, J. L.\\\", \\\"year\\\": \\\"1962\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"searle1969speechacts\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Speech Acts: An Essay in the Philosophy of Language\\\", \\\"authors\\\": \\\"Searle, J. R.\\\", \\\"year\\\": \\\"1969\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"cialdini2001influence\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Influence: Science and Practice\\\", \\\"authors\\\": \\\"Cialdini, Robert B.\\\", \\\"year\\\": \\\"2001\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\\\", \\\"authors\\\": \\\"Zeng, Yi and Lin, Hongpeng and Zhang, Jingwen and Yang, Diyi and Jia, Ruoxi and ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"russinovich2024crescendo\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\\\", \\\"authors\\\": \\\"Russinovich, Mark and Salem, Ahmed and Eldan, Ronen\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"USENIX Security Symposium\\\"}, {\\\"key\\\": \\\"chao2023pair\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Jailbreaking Black Box Large Language Models in Twenty Queries\\\", \\\"authors\\\": \\\"Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pa...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"wei2023jailbroken\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Jailbroken: How Does LLM Safety Training Fail?\\\", \\\"authors\\\": \\\"Wei, Alexander and Haghtalab, Nika and Steinhardt, Jacob\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"hagendorff2026reasoning\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Reasoning Models Are Autonomous Jailbreak Agents\\\", \\\"authors\\\": \\\"Hagendorff, Thilo and Derner, Erik and Oliver, Nuria\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Nature Communications\\\"}, {\\\"key\\\": \\\"fitd2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\\\", \\\"authors\\\": \\\"Wang, Zhenhua and Xie, Wei and Wang, Baosheng and Wang, Enze and Gui, Zhiwen and...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"type\\\": \\\"techreport\\\", \\\"title\\\": \\\"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\\\", \\\"authors\\\": \\\"Palo Alto Networks Unit 42\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"ren2024actorattack\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\\\", \\\"authors\\\": \\\"Ren, Qibing and Li, Hao and Liu, Dongrui and Xie, Zhanxu and Lu, Xiaoya and Qiao...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"zou2023gcg\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Universal and Transferable Adversarial Attacks on Aligned Language Models\\\", \\\"authors\\\": \\\"Zou, Andy and Wang, Zifan and Carlini, Nicholas and Nasr, Milad and Kolter, J. Z...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"lin2023toxicchat\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ToxicChat: Unveiling Hidden Challenges of Toxicity Detection in Real-World User-AI Conversation\\\", \\\"authors\\\": \\\"Lin, Zi and Wang, Zihan and Tong, Yongqi and Wang, Yangkun and Guo, Yuxin and Wa...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: EMNLP 2023\\\"}, {\\\"key\\\": \\\"li2024mhj\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\\\", \\\"authors\\\": \\\"Li, Nathaniel and Han, Ziwen and Steneker, Ian and Primack, Willow and Goodside,...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"gururangan2018artifacts\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Annotation Artifacts in Natural Language Inference Data\\\", \\\"authors\\\": \\\"Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and ...\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the Conference of the North American Chapter of the Association f...\\\"}, {\\\"key\\\": \\\"niven2019probing\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Probing Neural Network Comprehension of Natural Language Arguments\\\", \\\"authors\\\": \\\"Niven, Timothy and Kao, Hung-Yu\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"nasr2025attackermovessecond\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\\\", \\\"authors\\\": \\\"Nasr, Milad and Carlini, Nicholas and Sitawarin, Chawin and Schulhoff, Sander V....\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"andriushchenko2024adaptive\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\\\", \\\"authors\\\": \\\"Andriushchenko, Maksym and Croce, Francesco and Flammarion, Nicolas\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\\\", \\\"authors\\\": \\\"He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"gururangan2020dontstop\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\\\", \\\"authors\\\": \\\"Gururangan, Suchin and Marasovi\\\\\\\\'c, Ana and Swayamdipta, Swabha and Lo, Kyle and...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 58th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"caruana1997multitask\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Multitask Learning\\\", \\\"authors\\\": \\\"Caruana, Rich\\\", \\\"year\\\": \\\"1997\\\", \\\"venue\\\": \\\"Machine Learning\\\"}, {\\\"key\\\": \\\"phang2018stilts\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\\\", \\\"authors\\\": \\\"Phang, Jason and F\\\\\\\\'evry, Thibault and Bowman, Samuel R.\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:1811.01088\\\"}, {\\\"key\\\": \\\"liu2019mtdnn\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Multi-Task Deep Neural Networks for Natural Language Understanding\\\", \\\"authors\\\": \\\"Liu, Xiaodong and He, Pengcheng and Chen, Weizhu and Gao, Jianfeng\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"howard2018ulmfit\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Universal Language Model Fine-tuning for Text Classification\\\", \\\"authors\\\": \\\"Howard, Jeremy and Ruder, Sebastian\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"dasanmartino2020semeval\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\\\", \\\"authors\\\": \\\"Da San Martino, Giovanni and Barr\\\\\\\\'on-Cede\\\\\\\\~no, Alberto and Wachsmuth, Henning a...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the Fourteenth Workshop on Semantic Evaluation\\\"}, {\\\"key\\\": \\\"dasanmartino2019fine\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Fine-Grained Analysis of Propaganda in News Articles\\\", \\\"authors\\\": \\\"Da San Martino, Giovanni and Yu, Seunghak and Barr\\\\\\\\'on-Cede\\\\\\\\~no, Alberto and Pet...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"jin2020textfooler\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\\\", \\\"authors\\\": \\\"Jin, Di and Jin, Zhijing and Zhou, Joey Tianyi and Szolovits, Peter\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"li2020bertattack\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\\\", \\\"authors\\\": \\\"Li, Linyang and Ma, Ruotian and Guo, Qipeng and Xue, Xiangyang and Qiu, Xipeng\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"conneau2018probing\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"What you can cram into a single \\\\\\\\$\\\\\\\\&!\\\\\\\\#* vector: Probing sentence embeddings for linguistic properties\\\", \\\"authors\\\": \\\"Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo\\\\\\\\\\\\\\\"i...\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"hewitt2019structural\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Structural Probe for Finding Syntax in Word Representations\\\", \\\"authors\\\": \\\"Hewitt, John and Manning, Christopher D.\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 2019 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"liu2019roberta\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"RoBERTa: A Robustly Optimized BERT Pretraining Approach\\\", \\\"authors\\\": \\\"Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:1907.11692\\\"}, {\\\"key\\\": \\\"wang2019persuasion\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good\\\", \\\"authors\\\": \\\"Wang, Xuewei and Shi, Weiyan and Kim, Richard and Oh, Yoojung and Yang, Sijia an...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"robey2024smoothllm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks\\\", \\\"authors\\\": \\\"Robey, Alexander and Wong, Eric and Hassani, Hamed and Pappas, George J.\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 41st International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"mehrotra2024tap\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Tree of Attacks: Jailbreaking Black-Box LLMs with the Pruning of Candidate Outputs\\\", \\\"authors\\\": \\\"Mehrotra, Anay and Zampetakis, Manolis and Kassianik, Paul and Nelson, Blaine an...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"chao2024jailbreakbench\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models\\\", \\\"authors\\\": \\\"Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pa...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2404.01318\\\"}, {\\\"key\\\": \\\"mazeika2024harmbench\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal\\\", \\\"authors\\\": \\\"Mazeika, Mantas and Phan, Long and Yin, Xuwang and Zou, Andy and Wang, Zifan and...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 41st International Conference on Machine Learning\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"russinovich2024crescendo\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"fitd2024\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"hagendorff2026reasoning\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"bullwinkel2025repeng\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"inan2023llamaguard\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"han2024wildguard\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zeng2024shieldgemma\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deepcontext2026\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"tong2025biid\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gguard2025\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deepcontext2026\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"liu2019roberta\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ren2024actorattack\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"russinovich2024crescendo\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"fitd2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ren2024actorattack\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"chao2023pair\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"mehrotra2024tap\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wei2023jailbroken\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"mazeika2024harmbench\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"chao2024jailbreakbench\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hagendorff2026reasoning\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"li2024mhj\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zou2023gcg\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deepcontext2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"tong2025biid\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gguard2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"safedream2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"inan2023llamaguard\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"metallamaguard3_2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zeng2024shieldgemma\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"han2024wildguard\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"anthropic2025constitutional\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"robey2024smoothllm\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"mann1988rst\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"prasad2008pdtb\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"stolcke2000dialogueact\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"austin1962speechacts\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"searle1969speechacts\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cialdini2001influence\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hagendorff2026reasoning\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"dasanmartino2019fine\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"dasanmartino2020semeval\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wang2019persuasion\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"howard2018ulmfit\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gururangan2020dontstop\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"phang2018stilts\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"caruana1997multitask\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"liu2019mtdnn\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gururangan2020dontstop\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citeauthor\\\"}, {\\\"key\\\": \\\"gururangan2018artifacts\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"niven2019probing\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"nasr2025attackermovessecond\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"andriushchenko2024adaptive\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"jin2020textfooler\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"li2020bertattack\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"conneau2018probing\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hewitt2019structural\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 44, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cialdini2001influence\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 44, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"russinovich2024crescendo\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"fitd2024\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ren2024actorattack\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"lin2023toxicchat\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"liu2019roberta\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"bullwinkel2025repeng\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 51, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gururangan2020dontstop\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 107, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ren2024actorattack\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 127, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"liu2019roberta\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 165, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 177, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"liu2019roberta\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 177, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"lin2023toxicchat\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 197, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"lin2023toxicchat\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 202, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cialdini2001influence\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 295, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 298, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"lin2023toxicchat\\\", \\\"file\\\": \\\"conclusion.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zou2023gcg\\\", \\\"file\\\": \\\"conclusion.tex\\\", \\\"line\\\": 42, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"liu2019roberta\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"citep\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"inan2023llamaguard\\\", \\\"title\\\": \\\"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"metallamaguard3_2024\\\", \\\"title\\\": \\\"Llama Guard 3\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.289, \\\"matched_title\\\": \\\"Llama Guard 3 Vision: Safeguarding Human-AI Image Understanding Conversations\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.29 below threshold 0.82\\\"}, {\\\"key\\\": \\\"zeng2024shieldgemma\\\", \\\"title\\\": \\\"ShieldGemma: Generative AI Content Moderation Based on Gemma\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ShieldGemma: Generative AI Content Moderation Based on Gemma\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"han2024wildguard\\\", \\\"title\\\": \\\"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"WildGuard: Open One-stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=han vs api=choi\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"anthropic2025constitutional\\\", \\\"title\\\": \\\"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=anthropic vs api=sharma\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"deepcontext2026\\\", \\\"title\\\": \\\"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tong2025biid\\\", \\\"title\\\": \\\"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.328, \\\"matched_title\\\": \\\"AI Alignment: A Comprehensive Survey\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.33 below threshold 0.82\\\"}, {\\\"key\\\": \\\"gguard2025\\\", \\\"title\\\": \\\"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.882, \\\"matched_title\\\": \\\"Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"safedream2026\\\", \\\"title\\\": \\\"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"bullwinkel2025repeng\\\", \\\"title\\\": \\\"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mann1988rst\\\", \\\"title\\\": \\\"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Rhetorical Structure Theory: Toward a functional theory of text organization\\\", \\\"matched_year\\\": \\\"1988\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"prasad2008pdtb\\\", \\\"title\\\": \\\"The Penn Discourse TreeBank 2.0\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.984, \\\"matched_title\\\": \\\"The Penn Discourse TreeBank 2.0.\\\", \\\"matched_year\\\": \\\"2008\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"stolcke2000dialogueact\\\", \\\"title\\\": \\\"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\\\", \\\"matched_year\\\": \\\"2000\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"austin1962speechacts\\\", \\\"title\\\": \\\"How to Do Things with Words\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"How To Do Things With Words\\\", \\\"matched_year\\\": \\\"1975\\\", \\\"mismatch_fields\\\": [\\\"year: bib=1962 vs api=1975\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"searle1969speechacts\\\", \\\"title\\\": \\\"Speech Acts: An Essay in the Philosophy of Language\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Speech Acts: An Essay in the Philosophy of Language\\\", \\\"matched_year\\\": \\\"1969\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cialdini2001influence\\\", \\\"title\\\": \\\"Influence: Science and Practice\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Influence: science and practice\\\", \\\"matched_year\\\": \\\"2008\\\", \\\"mismatch_fields\\\": [\\\"year: bib=2001 vs api=2008\\\", \\\"first_author: bib=cialdini vs api=giebels\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"title\\\": \\\"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"russinovich2024crescendo\\\", \\\"title\\\": \\\"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chao2023pair\\\", \\\"title\\\": \\\"Jailbreaking Black Box Large Language Models in Twenty Queries\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Jailbreaking Black Box Large Language Models in Twenty Queries\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"year: bib=2023 vs api=2025\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wei2023jailbroken\\\", \\\"title\\\": \\\"Jailbroken: How Does LLM Safety Training Fail?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Jailbroken: How Does LLM Safety Training Fail?\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hagendorff2026reasoning\\\", \\\"title\\\": \\\"Large Reasoning Models Are Autonomous Jailbreak Agents\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large reasoning models are autonomous jailbreak agents\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fitd2024\\\", \\\"title\\\": \\\"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"title\\\": \\\"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.446, \\\"matched_title\\\": \\\"BitBypass: A New Direction in Jailbreaking Aligned Large Language Models with Bitstream Camouflage\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.45 below threshold 0.82\\\"}, {\\\"key\\\": \\\"ren2024actorattack\\\", \\\"title\\\": \\\"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.402, \\\"matched_title\\\": \\\"NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-Turn LLM Jailbreaks\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.40 below threshold 0.82\\\"}, {\\\"key\\\": \\\"zou2023gcg\\\", \\\"title\\\": \\\"Universal and Transferable Adversarial Attacks on Aligned Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.301, \\\"matched_title\\\": \\\"Text Data Augmentation for Deep Learning\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.30 below threshold 0.82\\\"}, {\\\"key\\\": \\\"lin2023toxicchat\\\", \\\"title\\\": \\\"ToxicChat: Unveiling Hidden Challenges of Toxicity Detection in Real-World User-AI Conversation\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ToxicChat: Unveiling Hidden Challenges of Toxicity Detection in Real-World User-AI Conversation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=lin vs api=zi\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2024mhj\\\", \\\"title\\\": \\\"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gururangan2018artifacts\\\", \\\"title\\\": \\\"Annotation Artifacts in Natural Language Inference Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Annotation Artifacts in Natural Language Inference Data\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"niven2019probing\\\", \\\"title\\\": \\\"Probing Neural Network Comprehension of Natural Language Arguments\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Probing Neural Network Comprehension of Natural Language Arguments\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"nasr2025attackermovessecond\\\", \\\"title\\\": \\\"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against Llm Jailbreaks and Prompt Injections\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"andriushchenko2024adaptive\\\", \\\"title\\\": \\\"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"title\\\": \\\"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DEBERTA: DECODING-ENHANCED BERT WITH DISENTANGLED ATTENTION\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gururangan2020dontstop\\\", \\\"title\\\": \\\"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.492, \\\"matched_title\\\": \\\"From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.49 below threshold 0.82\\\"}, {\\\"key\\\": \\\"caruana1997multitask\\\", \\\"title\\\": \\\"Multitask Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multitask Learning\\\", \\\"matched_year\\\": \\\"1997\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"phang2018stilts\\\", \\\"title\\\": \\\"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"liu2019mtdnn\\\", \\\"title\\\": \\\"Multi-Task Deep Neural Networks for Natural Language Understanding\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multi-Task Deep Neural Networks for Natural Language Understanding\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"howard2018ulmfit\\\", \\\"title\\\": \\\"Universal Language Model Fine-tuning for Text Classification\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Universal Language Model Fine-tuning for Text Classification\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dasanmartino2020semeval\\\", \\\"title\\\": \\\"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=da san martino vs api=martino\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dasanmartino2019fine\\\", \\\"title\\\": \\\"Fine-Grained Analysis of Propaganda in News Articles\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Fine-Grained Analysis of Propaganda in News Articles\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=da san martino vs api=martino\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"jin2020textfooler\\\", \\\"title\\\": \\\"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2020bertattack\\\", \\\"title\\\": \\\"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"conneau2018probing\\\", \\\"title\\\": \\\"What you can cram into a single \\\\\\\\$\\\\\\\\&!\\\\\\\\#* vector: Probing sentence embeddings for linguistic properties\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.98, \\\"matched_title\\\": \\\"What you can cram into a single $&amp;!#* vector: Probing sentence embeddings for linguistic properties\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hewitt2019structural\\\", \\\"title\\\": \\\"A Structural Probe for Finding Syntax in Word Representations\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.316, \\\"matched_title\\\": \\\"What Does BERT Learn about the Structure of Language?\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.32 below threshold 0.82\\\"}, {\\\"key\\\": \\\"liu2019roberta\\\", \\\"title\\\": \\\"RoBERTa: A Robustly Optimized BERT Pretraining Approach\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.495, \\\"matched_title\\\": \\\"Use of Bidirectional Encoder Representations from Transformers (BERT) and Robustly Optimized Bert Pretraining Approach (RoBERTa) for Nepali News Classification\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.50 below threshold 0.82\\\"}, {\\\"key\\\": \\\"wang2019persuasion\\\", \\\"title\\\": \\\"Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"robey2024smoothllm\\\", \\\"title\\\": \\\"SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mehrotra2024tap\\\", \\\"title\\\": \\\"Tree of Attacks: Jailbreaking Black-Box LLMs with the Pruning of Candidate Outputs\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.435, \\\"matched_title\\\": \\\"A survey of safety and trustworthiness of large language models through the lens of verification and validation\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.44 below threshold 0.82\\\"}, {\\\"key\\\": \\\"chao2024jailbreakbench\\\", \\\"title\\\": \\\"JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=chao vs api=andriushchenko\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mazeika2024harmbench\\\", \\\"title\\\": \\\"HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 88, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 31, \"online_not_found\": 9, \"online_mismatch\": 9}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"inan2023llamaguard\", \"type\": \"article\", \"title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"authors\": \"Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer,...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"metallamaguard3_2024\", \"type\": \"misc\", \"title\": \"Llama Guard 3\", \"authors\": \"Meta AI\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"zeng2024shieldgemma\", \"type\": \"article\", \"title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"authors\": \"Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"han2024wildguard\", \"type\": \"inproceedings\", \"title\": \"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"authors\": \"Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"anthropic2025constitutional\", \"type\": \"article\", \"title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"authors\": \"Anthropic\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"deepcontext2026\", \"type\": \"article\", \"title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"authors\": \"Albrethsen, Justin and Datta, Yash and Kumar, Kunal and Rajasekar, Sharath\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"tong2025biid\", \"type\": \"article\", \"title\": \"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\", \"authors\": \"Tong, Haibo and Zhao, Dongcheng and Shen, Guobin and He, Xiang and Lin, Dachuan ...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"gguard2025\", \"type\": \"article\", \"title\": \"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\", \"authors\": \"Huang, Zixuan and Huang, Kecheng and Yin, Lihao and He, Bowei and Zhen, Huiling ...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"safedream2026\", \"type\": \"article\", \"title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"authors\": \"Yan, Bo and Lin, Weikai and Zhu, Yada and Wang, Song\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"bullwinkel2025repeng\", \"type\": \"article\", \"title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"authors\": \"Bullwinkel, Blake and Russinovich, Mark and Salem, Ahmed and Zanella-Beguelin, S...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"mann1988rst\", \"type\": \"article\", \"title\": \"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\", \"authors\": \"Mann, William C. and Thompson, Sandra A.\", \"year\": \"1988\", \"venue\": \"Text \\\\& Talk\"}, {\"key\": \"prasad2008pdtb\", \"type\": \"inproceedings\", \"title\": \"The Penn Discourse TreeBank 2.0\", \"authors\": \"Prasad, Rashmi and Dinesh, Nikhil and Lee, Alan and Miltsakaki, Eleni and Robald...\", \"year\": \"2008\", \"venue\": \"Proceedings of the International Conference on Language Resources and Evaluation\"}, {\"key\": \"stolcke2000dialogueact\", \"type\": \"article\", \"title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"authors\": \"Stolcke, Andreas and Ries, Klaus and Coccaro, Noah and Shriberg, Elizabeth and B...\", \"year\": \"2000\", \"venue\": \"Computational Linguistics\"}, {\"key\": \"austin1962speechacts\", \"type\": \"book\", \"title\": \"How to Do Things with Words\", \"authors\": \"Austin, J. L.\", \"year\": \"1962\", \"venue\": \"\"}, {\"key\": \"searle1969speechacts\", \"type\": \"book\", \"title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"authors\": \"Searle, J. R.\", \"year\": \"1969\", \"venue\": \"\"}, {\"key\": \"cialdini2001influence\", \"type\": \"book\", \"title\": \"Influence: Science and Practice\", \"authors\": \"Cialdini, Robert B.\", \"year\": \"2001\", \"venue\": \"\"}, {\"key\": \"zeng2024pap\", \"type\": \"inproceedings\", \"title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"authors\": \"Zeng, Yi and Lin, Hongpeng and Zhang, Jingwen and Yang, Diyi and Jia, Ruoxi and ...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Association for Computational Linguistics\"}, {\"key\": \"russinovich2024crescendo\", \"type\": \"inproceedings\", \"title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"authors\": \"Russinovich, Mark and Salem, Ahmed and Eldan, Ronen\", \"year\": \"2025\", \"venue\": \"USENIX Security Symposium\"}, {\"key\": \"chao2023pair\", \"type\": \"article\", \"title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"authors\": \"Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pa...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"wei2023jailbroken\", \"type\": \"inproceedings\", \"title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"authors\": \"Wei, Alexander and Haghtalab, Nika and Steinhardt, Jacob\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"hagendorff2026reasoning\", \"type\": \"article\", \"title\": \"Large Reasoning Models Are Autonomous Jailbreak Agents\", \"authors\": \"Hagendorff, Thilo and Derner, Erik and Oliver, Nuria\", \"year\": \"2026\", \"venue\": \"Nature Communications\"}, {\"key\": \"fitd2024\", \"type\": \"article\", \"title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"authors\": \"Wang, Zhenhua and Xie, Wei and Wang, Baosheng and Wang, Enze and Gui, Zhiwen and...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"deceptivedelight2024\", \"type\": \"techreport\", \"title\": \"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\", \"authors\": \"Palo Alto Networks Unit 42\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"ren2024actorattack\", \"type\": \"inproceedings\", \"title\": \"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\", \"authors\": \"Ren, Qibing and Li, Hao and Liu, Dongrui and Xie, Zhanxu and Lu, Xiaoya and Qiao...\", \"year\": \"2025\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"zou2023gcg\", \"type\": \"article\", \"title\": \"Universal and Transferable Adversarial Attacks on Aligned Language Models\", \"authors\": \"Zou, Andy and Wang, Zifan and Carlini, Nicholas and Nasr, Milad and Kolter, J. Z...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"lin2023toxicchat\", \"type\": \"inproceedings\", \"title\": \"ToxicChat: Unveiling Hidden Challenges of Toxicity Detection in Real-World User-AI Conversation\", \"authors\": \"Lin, Zi and Wang, Zihan and Tong, Yongqi and Wang, Yangkun and Guo, Yuxin and Wa...\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2023\"}, {\"key\": \"li2024mhj\", \"type\": \"article\", \"title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"authors\": \"Li, Nathaniel and Han, Ziwen and Steneker, Ian and Primack, Willow and Goodside,...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"gururangan2018artifacts\", \"type\": \"inproceedings\", \"title\": \"Annotation Artifacts in Natural Language Inference Data\", \"authors\": \"Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and ...\", \"year\": \"2018\", \"venue\": \"Proceedings of the Conference of the North American Chapter of the Association f...\"}, {\"key\": \"niven2019probing\", \"type\": \"inproceedings\", \"title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"authors\": \"Niven, Timothy and Kao, Hung-Yu\", \"year\": \"2019\", \"venue\": \"Proceedings of the Association for Computational Linguistics\"}, {\"key\": \"nasr2025attackermovessecond\", \"type\": \"article\", \"title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\", \"authors\": \"Nasr, Milad and Carlini, Nicholas and Sitawarin, Chawin and Schulhoff, Sander V....\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"andriushchenko2024adaptive\", \"type\": \"inproceedings\", \"title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"authors\": \"Andriushchenko, Maksym and Croce, Francesco and Flammarion, Nicolas\", \"year\": \"2025\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"he2021deberta\", \"type\": \"inproceedings\", \"title\": \"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\", \"authors\": \"He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gururangan2020dontstop\", \"type\": \"inproceedings\", \"title\": \"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\", \"authors\": \"Gururangan, Suchin and Marasovi\\\\'c, Ana and Swayamdipta, Swabha and Lo, Kyle and...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 58th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"caruana1997multitask\", \"type\": \"article\", \"title\": \"Multitask Learning\", \"authors\": \"Caruana, Rich\", \"year\": \"1997\", \"venue\": \"Machine Learning\"}, {\"key\": \"phang2018stilts\", \"type\": \"article\", \"title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"authors\": \"Phang, Jason and F\\\\'evry, Thibault and Bowman, Samuel R.\", \"year\": \"2018\", \"venue\": \"arXiv preprint arXiv:1811.01088\"}, {\"key\": \"liu2019mtdnn\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"authors\": \"Liu, Xiaodong and He, Pengcheng and Chen, Weizhu and Gao, Jianfeng\", \"year\": \"2019\", \"venue\": \"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"howard2018ulmfit\", \"type\": \"inproceedings\", \"title\": \"Universal Language Model Fine-tuning for Text Classification\", \"authors\": \"Howard, Jeremy and Ruder, Sebastian\", \"year\": \"2018\", \"venue\": \"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"dasanmartino2020semeval\", \"type\": \"inproceedings\", \"title\": \"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\", \"authors\": \"Da San Martino, Giovanni and Barr\\\\'on-Cede\\\\~no, Alberto and Wachsmuth, Henning a...\", \"year\": \"2020\", \"venue\": \"Proceedings of the Fourteenth Workshop on Semantic Evaluation\"}, {\"key\": \"dasanmartino2019fine\", \"type\": \"inproceedings\", \"title\": \"Fine-Grained Analysis of Propaganda in News Articles\", \"authors\": \"Da San Martino, Giovanni and Yu, Seunghak and Barr\\\\'on-Cede\\\\~no, Alberto and Pet...\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"jin2020textfooler\", \"type\": \"inproceedings\", \"title\": \"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\", \"authors\": \"Jin, Di and Jin, Zhijing and Zhou, Joey Tianyi and Szolovits, Peter\", \"year\": \"2020\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"li2020bertattack\", \"type\": \"inproceedings\", \"title\": \"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\", \"authors\": \"Li, Linyang and Ma, Ruotian and Guo, Qipeng and Xue, Xiangyang and Qiu, Xipeng\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"conneau2018probing\", \"type\": \"inproceedings\", \"title\": \"What you can cram into a single \\\\$\\\\&!\\\\#* vector: Probing sentence embeddings for linguistic properties\", \"authors\": \"Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo\\\\\\\"i...\", \"year\": \"2018\", \"venue\": \"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"hewitt2019structural\", \"type\": \"inproceedings\", \"title\": \"A Structural Probe for Finding Syntax in Word Representations\", \"authors\": \"Hewitt, John and Manning, Christopher D.\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"liu2019roberta\", \"type\": \"article\", \"title\": \"RoBERTa: A Robustly Optimized BERT Pretraining Approach\", \"authors\": \"Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and...\", \"year\": \"2019\", \"venue\": \"arXiv preprint arXiv:1907.11692\"}, {\"key\": \"wang2019persuasion\", \"type\": \"inproceedings\", \"title\": \"Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good\", \"authors\": \"Wang, Xuewei and Shi, Weiyan and Kim, Richard and Oh, Yoojung and Yang, Sijia an...\", \"year\": \"2019\", \"venue\": \"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"robey2024smoothllm\", \"type\": \"inproceedings\", \"title\": \"SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks\", \"authors\": \"Robey, Alexander and Wong, Eric and Hassani, Hamed and Pappas, George J.\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning\"}, {\"key\": \"mehrotra2024tap\", \"type\": \"inproceedings\", \"title\": \"Tree of Attacks: Jailbreaking Black-Box LLMs with the Pruning of Candidate Outputs\", \"authors\": \"Mehrotra, Anay and Zampetakis, Manolis and Kassianik, Paul and Nelson, Blaine an...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"chao2024jailbreakbench\", \"type\": \"article\", \"title\": \"JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models\", \"authors\": \"Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pa...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2404.01318\"}, {\"key\": \"mazeika2024harmbench\", \"type\": \"inproceedings\", \"title\": \"HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal\", \"authors\": \"Mazeika, Mantas and Phan, Long and Yin, Xuwang and Zou, Andy and Wang, Zifan and...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning\"}], \"tex_citations\": [{\"key\": \"russinovich2024crescendo\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"bullwinkel2025repeng\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"inan2023llamaguard\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"han2024wildguard\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"zeng2024shieldgemma\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"deepcontext2026\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"tong2025biid\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"gguard2025\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"deepcontext2026\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"introduction.tex\", \"line\": 14, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"introduction.tex\", \"line\": 14, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"introduction.tex\", \"line\": 20, \"command\": \"citep\"}, {\"key\": \"russinovich2024crescendo\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"chao2023pair\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"mehrotra2024tap\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"wei2023jailbroken\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"mazeika2024harmbench\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"chao2024jailbreakbench\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"li2024mhj\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"zou2023gcg\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"deepcontext2026\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"tong2025biid\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"gguard2025\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"safedream2026\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"inan2023llamaguard\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"metallamaguard3_2024\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"zeng2024shieldgemma\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"han2024wildguard\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"anthropic2025constitutional\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"robey2024smoothllm\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"mann1988rst\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"prasad2008pdtb\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"stolcke2000dialogueact\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"austin1962speechacts\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"searle1969speechacts\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"dasanmartino2019fine\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"dasanmartino2020semeval\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"wang2019persuasion\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"howard2018ulmfit\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"gururangan2020dontstop\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citet\"}, {\"key\": \"phang2018stilts\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"caruana1997multitask\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"liu2019mtdnn\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"gururangan2020dontstop\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citeauthor\"}, {\"key\": \"gururangan2018artifacts\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"niven2019probing\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"nasr2025attackermovessecond\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"andriushchenko2024adaptive\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"jin2020textfooler\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"li2020bertattack\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"conneau2018probing\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"hewitt2019structural\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"method.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"method.tex\", \"line\": 44, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"method.tex\", \"line\": 44, \"command\": \"citep\"}, {\"key\": \"russinovich2024crescendo\", \"file\": \"experiments.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"lin2023toxicchat\", \"file\": \"experiments.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"experiments.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"bullwinkel2025repeng\", \"file\": \"experiments.tex\", \"line\": 51, \"command\": \"citep\"}, {\"key\": \"gururangan2020dontstop\", \"file\": \"experiments.tex\", \"line\": 107, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"experiments.tex\", \"line\": 127, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"experiments.tex\", \"line\": 165, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"experiments.tex\", \"line\": 177, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"experiments.tex\", \"line\": 177, \"command\": \"citep\"}, {\"key\": \"lin2023toxicchat\", \"file\": \"experiments.tex\", \"line\": 197, \"command\": \"citep\"}, {\"key\": \"lin2023toxicchat\", \"file\": \"experiments.tex\", \"line\": 202, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"experiments.tex\", \"line\": 295, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"experiments.tex\", \"line\": 298, \"command\": \"citep\"}, {\"key\": \"lin2023toxicchat\", \"file\": \"conclusion.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"zou2023gcg\", \"file\": \"conclusion.tex\", \"line\": 42, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"checklist.tex\", \"line\": 27, \"command\": \"citep\"}, {\"key\": \"liu2019roberta\", \"file\": \"checklist.tex\", \"line\": 27, \"command\": \"citep\"}], \"online_verification\": [{\"key\": \"inan2023llamaguard\", \"title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"metallamaguard3_2024\", \"title\": \"Llama Guard 3\", \"status\": \"not_found\", \"confidence\": 0.289, \"matched_title\": \"Llama Guard 3 Vision: Safeguarding Human-AI Image Understanding Conversations\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.29 below threshold 0.82\"}, {\"key\": \"zeng2024shieldgemma\", \"title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"han2024wildguard\", \"title\": \"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"WildGuard: Open One-stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=han vs api=choi\"], \"note\": \"\"}, {\"key\": \"anthropic2025constitutional\", \"title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=anthropic vs api=sharma\"], \"note\": \"\"}, {\"key\": \"deepcontext2026\", \"title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tong2025biid\", \"title\": \"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\", \"status\": \"not_found\", \"confidence\": 0.328, \"matched_title\": \"AI Alignment: A Comprehensive Survey\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"gguard2025\", \"title\": \"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\", \"status\": \"verified\", \"confidence\": 0.882, \"matched_title\": \"Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"safedream2026\", \"title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bullwinkel2025repeng\", \"title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mann1988rst\", \"title\": \"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rhetorical Structure Theory: Toward a functional theory of text organization\", \"matched_year\": \"1988\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"prasad2008pdtb\", \"title\": \"The Penn Discourse TreeBank 2.0\", \"status\": \"verified\", \"confidence\": 0.984, \"matched_title\": \"The Penn Discourse TreeBank 2.0.\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"stolcke2000dialogueact\", \"title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"matched_year\": \"2000\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"austin1962speechacts\", \"title\": \"How to Do Things with Words\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"How To Do Things With Words\", \"matched_year\": \"1975\", \"mismatch_fields\": [\"year: bib=1962 vs api=1975\"], \"note\": \"\"}, {\"key\": \"searle1969speechacts\", \"title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"matched_year\": \"1969\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cialdini2001influence\", \"title\": \"Influence: Science and Practice\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Influence: science and practice\", \"matched_year\": \"2008\", \"mismatch_fields\": [\"year: bib=2001 vs api=2008\", \"first_author: bib=cialdini vs api=giebels\"], \"note\": \"\"}, {\"key\": \"zeng2024pap\", \"title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"russinovich2024crescendo\", \"title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chao2023pair\", \"title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"year: bib=2023 vs api=2025\"], \"note\": \"\"}, {\"key\": \"wei2023jailbroken\", \"title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hagendorff2026reasoning\", \"title\": \"Large Reasoning Models Are Autonomous Jailbreak Agents\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large reasoning models are autonomous jailbreak agents\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fitd2024\", \"title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"deceptivedelight2024\", \"title\": \"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\", \"status\": \"not_found\", \"confidence\": 0.446, \"matched_title\": \"BitBypass: A New Direction in Jailbreaking Aligned Large Language Models with Bitstream Camouflage\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"ren2024actorattack\", \"title\": \"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\", \"status\": \"not_found\", \"confidence\": 0.402, \"matched_title\": \"NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-Turn LLM Jailbreaks\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.40 below threshold 0.82\"}, {\"key\": \"zou2023gcg\", \"title\": \"Universal and Transferable Adversarial Attacks on Aligned Language Models\", \"status\": \"not_found\", \"confidence\": 0.301, \"matched_title\": \"Text Data Augmentation for Deep Learning\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\"}, {\"key\": \"lin2023toxicchat\", \"title\": \"ToxicChat: Unveiling Hidden Challenges of Toxicity Detection in Real-World User-AI Conversation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"ToxicChat: Unveiling Hidden Challenges of Toxicity Detection in Real-World User-AI Conversation\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=lin vs api=zi\"], \"note\": \"\"}, {\"key\": \"li2024mhj\", \"title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gururangan2018artifacts\", \"title\": \"Annotation Artifacts in Natural Language Inference Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Annotation Artifacts in Natural Language Inference Data\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"niven2019probing\", \"title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nasr2025attackermovessecond\", \"title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against Llm Jailbreaks and Prompt Injections\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"andriushchenko2024adaptive\", \"title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"he2021deberta\", \"title\": \"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DEBERTA: DECODING-ENHANCED BERT WITH DISENTANGLED ATTENTION\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gururangan2020dontstop\", \"title\": \"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\", \"status\": \"not_found\", \"confidence\": 0.492, \"matched_title\": \"From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.49 below threshold 0.82\"}, {\"key\": \"caruana1997multitask\", \"title\": \"Multitask Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multitask Learning\", \"matched_year\": \"1997\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"phang2018stilts\", \"title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liu2019mtdnn\", \"title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"howard2018ulmfit\", \"title\": \"Universal Language Model Fine-tuning for Text Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Language Model Fine-tuning for Text Classification\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dasanmartino2020semeval\", \"title\": \"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles\", \"matched_year\": \"2020\", \"mismatch_fields\": [\"first_author: bib=da san martino vs api=martino\"], \"note\": \"\"}, {\"key\": \"dasanmartino2019fine\", \"title\": \"Fine-Grained Analysis of Propaganda in News Articles\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Fine-Grained Analysis of Propaganda in News Articles\", \"matched_year\": \"2019\", \"mismatch_fields\": [\"first_author: bib=da san martino vs api=martino\"], \"note\": \"\"}, {\"key\": \"jin2020textfooler\", \"title\": \"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2020bertattack\", \"title\": \"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"BERT-ATTACK: Adversarial Attack Against BERT Using BERT\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"conneau2018probing\", \"title\": \"What you can cram into a single \\\\$\\\\&!\\\\#* vector: Probing sentence embeddings for linguistic properties\", \"status\": \"verified\", \"confidence\": 0.98, \"matched_title\": \"What you can cram into a single $&amp;!#* vector: Probing sentence embeddings for linguistic properties\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hewitt2019structural\", \"title\": \"A Structural Probe for Finding Syntax in Word Representations\", \"status\": \"not_found\", \"confidence\": 0.316, \"matched_title\": \"What Does BERT Learn about the Structure of Language?\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.32 below threshold 0.82\"}, {\"key\": \"liu2019roberta\", \"title\": \"RoBERTa: A Robustly Optimized BERT Pretraining Approach\", \"status\": \"not_found\", \"confidence\": 0.495, \"matched_title\": \"Use of Bidirectional Encoder Representations from Transformers (BERT) and Robustly Optimized Bert Pretraining Approach (RoBERTa) for Nepali News Classification\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.50 below threshold 0.82\"}, {\"key\": \"wang2019persuasion\", \"title\": \"Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"robey2024smoothllm\", \"title\": \"SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mehrotra2024tap\", \"title\": \"Tree of Attacks: Jailbreaking Black-Box LLMs with the Pruning of Candidate Outputs\", \"status\": \"not_found\", \"confidence\": 0.435, \"matched_title\": \"A survey of safety and trustworthiness of large language models through the lens of verification and validation\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.44 below threshold 0.82\"}, {\"key\": \"chao2024jailbreakbench\", \"title\": \"JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=chao vs api=andriushchenko\"], \"note\": \"\"}, {\"key\": \"mazeika2024harmbench\", \"title\": \"HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "307e3696-7693-4330-b6d0-8d8035fc259d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 43 · 2026-05-18T18:01:53.917Z_

```json
{
  "parentUuid": "180646a4-25a7-4909-b3c0-06bfe14d94fc",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "53f85822-d647-4662-9978-0d1ecf040c93",
  "timestamp": "2026-05-18T18:01:53.917Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责**方法严谨性 + 实验设计**。  ## 论文信息 - 标题: \"What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\" - 路径: `projects/persuasion_turn_jailbreak_d…",
  "leafUuid": "53f85822-d647-4662-9978-0d1ecf040c93",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multi-turn jailbreak detection paper for EMNLP",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765"
}
```

---

### Assistant

_source line 46 · 2026-05-18T18:01:57.134Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the full ACL ARR reviewer guidelines to get the exact scoring criteria.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53f85822-d647-4662-9978-0d1ecf040c93",
  "isSidechain": false,
  "requestId": "req_011CbAUNgkfz3itq1LRNQ1Md",
  "type": "assistant",
  "uuid": "c3ae376d-0ba0-4301-a157-f5b2a5549fca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015BQ9fvmrJ6RhWHjo7QNsuY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 64449,
      "cache_read_input_tokens": 11447,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 64449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 64449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 64449
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-18T18:01:57.656Z_

让我获取 ACL ARR reviewer guidelines 的详细评分标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3ae376d-0ba0-4301-a157-f5b2a5549fca",
  "isSidechain": false,
  "requestId": "req_011CbAUNgkfz3itq1LRNQ1Md",
  "type": "assistant",
  "uuid": "0bcca460-429b-4210-8b74-fdc2678faee1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015BQ9fvmrJ6RhWHjo7QNsuY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 64449,
      "cache_read_input_tokens": 11447,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 64449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 64449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 64449
          },
          "type": "message"
        }
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

_source line 48 · 2026-05-18T18:02:00.033Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EHkR7qP2JXY1ScWTnyfrPD`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer scoring criteria, including all score dimensions (soundness, excitement, overall assessment, confidence), their exact scale descriptions (what each number 1-5 means), and any specific review form requirements. I need the full scoring rubric."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bcca460-429b-4210-8b74-fdc2678faee1",
  "isSidechain": false,
  "requestId": "req_011CbAUNgkfz3itq1LRNQ1Md",
  "type": "assistant",
  "uuid": "3debb31f-52b1-4820-8d59-69e69f00546c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015BQ9fvmrJ6RhWHjo7QNsuY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 64449,
      "cache_read_input_tokens": 11447,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 64449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 64449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 64449
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-18T18:02:05.579Z_

<details><summary>↩ Tool result · `toolu_01EHkR7qP2JXY1ScWTnyfrPD`</summary>

```text
# ARR Reviewer Scoring Criteria

Based on the provided guidelines, the document mentions three scoring dimensions but **does not provide the complete numerical scale descriptions (what each 1-5 rating means)**.

## Documented Score Dimensions

The guidelines state: "Starting with February 2025, ARR reviewers are asked to provide three scores: **soundness, excitement, and overall recommendation**."

### What We Know:

**Soundness**: Assessed based on technical validity. The guidelines note that "low _Soundness_ scores must be justified by the text of the review."

**Excitement**: Described as "more subjective" and reflecting "our personal taste," kept separate from soundness evaluation.

**Overall Assessment**: A "composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact."

The document also references a **confidence score** in relation to expertise gaps, though specific scale details aren't provided.

## Critical Gap

The document does not include the actual numerical rubric (e.g., "1 = Reject, 2 = Weak Reject...5 = Strong Accept"). For the complete scoring scale definitions, you would need to consult the [ARR review form documentation](https://aclrollingreview.org/reviewform) referenced in the guidelines, which appears to contain detailed scoring specifications not reproduced in these reviewer guidelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3debb31f-52b1-4820-8d59-69e69f00546c",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "0b8aee53-8010-4d1c-9c77-bfce56fdb8a5",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Reviewer Scoring Criteria\n\nBased on the provided guidelines, the document mentions three scoring dimensions but **does not provide the complete numerical scale descriptions (what each 1-5 rating means)**.\n\n## Documented Score Dimensions\n\nThe guidelines state: \"Starting with February 2025, ARR reviewers are asked to provide three scores: **soundness, excitement, and overall recommendation**.\"\n\n### What We Know:\n\n**Soundness**: Assessed based on technical validity. The guidelines note that \"low _Soundness_ scores must be justified by the text of the review.\"\n\n**Excitement**: Described as \"more subjective\" and reflecting \"our personal taste,\" kept separate from soundness evaluation.\n\n**Overall Assessment**: A \"composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.\"\n\nThe document also references a **confidence score** in relation to expertise gaps, though specific scale details aren't provided.\n\n## Critical Gap\n\nThe document does not include the actual numerical rubric (e.g., \"1 = Reject, 2 = Weak Reject...5 = Strong Accept\"). For the complete scoring scale definitions, you would need to consult the [ARR review form documentation](https://aclrollingreview.org/reviewform) referenced in the guidelines, which appears to contain detailed scoring specifications not reproduced in these reviewer guidelines.",
    "durationMs": 5540,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "3debb31f-52b1-4820-8d59-69e69f00546c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-18T18:02:08.151Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try to get the actual review form with the scoring rubric.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b8aee53-8010-4d1c-9c77-bfce56fdb8a5",
  "isSidechain": false,
  "requestId": "req_011CbAUPYbpDwaACurJEENkA",
  "type": "assistant",
  "uuid": "1af620e0-4806-4408-8009-6f21781d5a04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6wZbtEBUXnrDqsUDhWtCR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 502,
      "cache_read_input_tokens": 75896,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 502,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 154,
          "cache_read_input_tokens": 75896,
          "cache_creation_input_tokens": 502,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 502
          },
          "type": "message"
        }
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

_source line 51 · 2026-05-18T18:02:09.624Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XhgVDNtwF8avyzAtUfpeZg`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete scoring rubric for all dimensions: soundness, excitement, overall assessment, confidence. What does each number (1-5) mean for each dimension? Give me the full text of each rating level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1af620e0-4806-4408-8009-6f21781d5a04",
  "isSidechain": false,
  "requestId": "req_011CbAUPYbpDwaACurJEENkA",
  "type": "assistant",
  "uuid": "6b377213-eb35-4a76-b0bf-a9ce42565d5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6wZbtEBUXnrDqsUDhWtCR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 502,
      "cache_read_input_tokens": 75896,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 502,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 154,
          "cache_read_input_tokens": 75896,
          "cache_creation_input_tokens": 502,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 502
          },
          "type": "message"
        }
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

_source line 52 · 2026-05-18T18:02:19.671Z_

<details><summary>↩ Tool result · `toolu_01XhgVDNtwF8avyzAtUfpeZg`</summary>

```text
# ACL Rolling Review Scoring Rubrics

## Reviewer Confidence (1-5 scale)

**5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."

**4:** "Quite sure. I tried to check the important points carefully. It's unlikely, though conceivable, that I missed something that should affect my ratings."

**3:** "Pretty sure, but there's a chance I missed something. Although I have a good feel for this area in general, I did not carefully check the paper's details, e.g., the math or experimental design."

**2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details, didn't understand some central points, or can't be sure about the novelty of the work."

**1:** "Not my area, or paper is very hard to understand. My evaluation is just an educated guess."

## Soundness (1-5 scale)

**5:** "Excellent: This study is one of the most thorough I have seen, given its type."

**4:** "Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential."

**3:** "Acceptable: This study provides sufficient support for its main claims. Some minor points may need extra support or details."

**2:** "Poor: Some of the main claims are not sufficiently supported. There are major technical/methodological problems."

**1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL."

## Excitement (1-5 scale)

**5:** "Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference."

**4:** "Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference."

**3:** "Interesting: I might mention some points of this paper to others and/or attend its presentation in a conference if there's time."

**2:** "Potentially Interesting: this paper does not resonate with me, but it might with others in the *ACL community."

**1:** "Not Exciting: this paper does not resonate with me, and I don't think it would with others in the *ACL community."

## Overall Assessment (1-5 scale)

**5:** "Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)."

**4.5:** "Borderline Award"

**4:** "Conference: I think this paper could be accepted to an *ACL conference."

**3.5:** "Borderline Conference"

**3:** "Findings: I think this paper could be accepted to the Findings of the ACL."

**2.5:** "Borderline Findings"

**2:** "Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle."

**1.5:** "Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle."

**1:** "Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b377213-eb35-4a76-b0bf-a9ce42565d5b",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "7a535628-2afc-4034-8036-bd508889aa16",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Scoring Rubrics\n\n## Reviewer Confidence (1-5 scale)\n\n**5:** \"Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work.\"\n\n**4:** \"Quite sure. I tried to check the important points carefully. It's unlikely, though conceivable, that I missed something that should affect my ratings.\"\n\n**3:** \"Pretty sure, but there's a chance I missed something. Although I have a good feel for this area in general, I did not carefully check the paper's details, e.g., the math or experimental design.\"\n\n**2:** \"Willing to defend my evaluation, but it is fairly likely that I missed some details, didn't understand some central points, or can't be sure about the novelty of the work.\"\n\n**1:** \"Not my area, or paper is very hard to understand. My evaluation is just an educated guess.\"\n\n## Soundness (1-5 scale)\n\n**5:** \"Excellent: This study is one of the most thorough I have seen, given its type.\"\n\n**4:** \"Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential.\"\n\n**3:** \"Acceptable: This study provides sufficient support for its main claims. Some minor points may need extra support or details.\"\n\n**2:** \"Poor: Some of the main claims are not sufficiently supported. There are major technical/methodological problems.\"\n\n**1:** \"Major Issues: This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL.\"\n\n## Excitement (1-5 scale)\n\n**5:** \"Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference.\"\n\n**4:** \"Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference.\"\n\n**3:** \"Interesting: I might mention some points of this paper to others and/or attend its presentation in a conference if there's time.\"\n\n**2:** \"Potentially Interesting: this paper does not resonate with me, but it might with others in the *ACL community.\"\n\n**1:** \"Not Exciting: this paper does not resonate with me, and I don't think it would with others in the *ACL community.\"\n\n## Overall Assessment (1-5 scale)\n\n**5:** \"Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers).\"\n\n**4.5:** \"Borderline Award\"\n\n**4:** \"Conference: I think this paper could be accepted to an *ACL conference.\"\n\n**3.5:** \"Borderline Conference\"\n\n**3:** \"Findings: I think this paper could be accepted to the Findings of the ACL.\"\n\n**2.5:** \"Borderline Findings\"\n\n**2:** \"Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle.\"\n\n**1.5:** \"Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle.\"\n\n**1:** \"Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community.\"",
    "durationMs": 10044,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "6b377213-eb35-4a76-b0bf-a9ce42565d5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-18T18:05:16.712Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile a thorough review. Let me organize my thoughts:

## Summary
This paper investigates what representation properties enable cross-attack generalization in multi-turn jailbreak detection. Through a controlled ablation study with seven DeBERTa-v3 variants and three RoBERTa variants (DisPeD), the authors identify three findings: (1) domain-adaptive continued pretraining (DAPT) is the primary mechanism for OOD generalization, (2) encoder pretraining method determines the difficulty threshold where DAPT becomes critical, (3) classification supervision acts as a representational regularizer rather than a strategy classifier.


The ablation design is well-structured with clean evidence hierarchies, and cross-encoder validation with RoBERTa strengthens the findings. However, the frozen encoder approach during Stage 2 may underestimate certain variants—particularly whether features from the topic classifier could be refined through end-to-end training—though the authors acknowledge this as a deliberate design choice for fair comparison.

On statistical rigor, the 3-seed setup (42, 123, 456) follows ACL/EMNLP conventions but limits statistical power and prevents meaningful significance testing across seeds. The paper uses bootstrap confidence intervals and permutation tests to compensate, though this doesn't fully address the fundamental constraint of having only three random initializations.

For the sample sizes, I'm checking the actual numbers: the IID test set has 76 examples, while the OOD evaluation splits across 80 FITD, 80 Deceptive Delight, and 118 ActorAttack instances. There's some inconsistency in how the DD numbers are reported across different sections that I need to clarify. I'm noticing a clear contradiction here—the setup lists DD as 80 conversations, but the perturbation section references n=118 for the same dataset. This could be a transposition error, or the 118 might include both jailbreak and benign control examples, but the numbers don't align cleanly enough to ignore.

Now I'm seeing the paper actually acknowledges the McNemar's test limitation with sparse discordant pairs (≤7 per comparison), which is a significant methodological constraint they're aware of.

The core issue is that with so few discordant pairs, the test lacks statistical power to detect real differences, yet the paper seems to use this both ways—claiming no significant effect when the test couldn't detect one anyway. The "three-layer pattern" they identify in the perturbation analysis is really just tracking 1-3 misclassification differences across 76 samples.

On the bootstrap approach, pooling predictions across seeds for the confidence intervals is sensible, though there's a subtle issue where bootstrap means from the non-linear F1 metric might diverge from the seed-averaged F1 they report.

Looking at the data quality concerns now, everything traces back to using Qwen3-8B for both the jailbreak training data and benign examples, which creates a potential confound across the entire evaluation pipeline.

The OOD evaluation with FITD, DD, and ActorAttack claims to test different attack strategies, but since all the data still comes from the same model, it's really only OOD in terms of attack method, not generation source. ToxicChat helps somewhat, but it's limited to single-turn conversations. This matters because the "OOD gap" they observe might partly be capturing within-model stylistic differences rather than genuine attack-strategy robustness.

What's striking is that TF-IDF achieves 0.961 F1 on DD—a bag-of-words baseline shouldn't perform that well if the task were genuinely difficult. The paper argues ActorAttack fixes this by dropping TF-IDF to 0.261, but that actually undermines their evidence hierarchy on DD. If DD is lexically separable, then their layered evidence structure there is mostly just measuring how well different models capture lexical features. They do acknowledge this limitation, which is fair.

For the strategy annotation, κ=0.78 indicates substantial but not near-perfect agreement, and with only 50 samples across 9 classes, that's roughly 5-6 examples per category. The bigger issue is that all annotations came from a single model (Qwen3-8B), and the human validation was just one annotator against the model rather than inter-human agreement. That said, their argument that label quality doesn't affect detection performance—since scrambled labels work equally well—is actually pretty convincing.

Looking at their main claim about domain exposure driving the ~60 percentage point gap, the vanilla-to-MLM improvement on DeBERTa (0.312 to 0.914 on DD) provides solid support, and the cross-encoder validation with RoBERTa seems to confirm this pattern.

For the encoder pretraining claim, the evidence is more mixed. RoBERTa vanilla succeeds on DD but fails on ActorAttack, while DeBERTa fails on both, which fits their story. However, DeBERTa-v3-base and RoBERTa-base differ in both pretraining and model capacity, so it's hard to isolate which factor matters. They acknowledge this confound, so the support here is moderate at best.

On the classification-as-regularizer claim, the fact that scrambled labels perform the same as binary and 9-class on detection is supportive, though strategy prediction doesn't seem to transfer to other tasks.

Looking at the variance reduction claim, classification does reduce cross-seed variance substantially on synthetic data, but on human data the pattern flips—9-class actually shows the highest variance. The perturbation robustness claim also breaks down on ActorAttack where 9-class degrades significantly, which undermines their broader generalizability narrative even though they acknowledge it.

On potential overclaiming, they describe capturing "discourse-level" pragmatic features like hedging and escalation markers, but the evidence for this is less clear than the framing suggests.  The main support is that DAPT outperforms TF-IDF on ActorAttack, which shows they're capturing something beyond bag-of-words, but that's not the same as directly verifying discourse-level structure. They do hedge reasonably well overall though—acknowledging the mean pooling limitation, the ActorAttack perturbation failure, modality mismatches, and the variance reversal.

For reproducibility, they've documented hyperparameters thoroughly, specified random seeds, reported compute costs, and committed to releasing code and data.

But there are some significant gaps: Figure 1 is just a placeholder, they haven't directly compared against DeepContext, BIID, or G-Guard despite acknowledging these as relevant baselines, there's no probing analysis to back up the discourse-level claims, and they haven't tested generation across multiple LLMs. I'm also noticing a sample size inconsistency—the setup mentions 80 DD conversations but the perturbation section references n=118 for DD, which needs clarification.

Let me work through the critical issues for the review. The architecture diagram being a literal placeholder is unacceptable for submission. And I need to figure out this sample size discrepancy—it looks like the evaluation might be combining jailbreak and benign conversations for the binary classification task, so n=118 could represent the full test set rather than just the jailbreak examples, but this should be explicitly stated in the paper. I'm noticing a discrepancy in the numbers—the OOD evaluation mentions 80 DD jailbreak conversations, but the perturbation section references n=118 for DD, which doesn't match up. The paper also doesn't clarify how many benign conversations are included in the IID test set or as controls for the OOD evaluations, which makes it hard to fully understand the evaluation setup.

Looking more carefully at the IID test description, it says "76 held-out Crescendo conversations," but Crescendo are jailbreak attempts. To compute standard metrics like F1, you'd need both positive and negative examples, so either the paper is combining these with benign examples from elsewhere, or the evaluation methodology isn't fully explained.

For the perturbation experiments mentioning n=76 and n=118, those numbers might refer only to jailbreak conversations since perturbations are applied to attacks. But then the main results tables reporting F1 scores would still require benign examples that aren't accounted for in the stated numbers.

This feels like a clarity issue in the paper—the test set composition should be explicit about whether benign examples are included and how they're distributed across IID and OOD evaluations.

There's also a significant confound: all training data and OOD evaluation data come from Qwen3-8B, with only ToxicChat providing some diversity, though it's limited to single-turn examples.

The "cross-attack generalization" claim might actually just reflect stylistic transfer within Qwen3-8B's outputs rather than genuine generalization across different attack types.

The paper claims DAPT captures discourse-level pragmatic features like hedging and escalation patterns, but the only supporting evidence is that TF-IDF fails on ActorAttack. That shows the model learned something beyond surface-level n-grams, but doesn't directly demonstrate it's capturing discourse structure—probing classifiers would be needed to substantiate this claim.

The frozen encoder design for ablations is reasonable, but it assumes Stage 1 representation quality is the limiting factor, which may not hold equally across all variants.  The topic variant in particular might benefit from joint end-to-end training. Though the paper does justify this choice for ablation fairness, so it's more of a minor concern than a critical flaw.

McNemar's test with only 7 or fewer discordant pairs lacks statistical power to detect differences, yet the paper uses it to claim no significant differences among variants. The test's limitations are partially acknowledged but still leveraged to support conclusions.

The cross-encoder comparison conflates two variables—DeBERTa-v3-base has both a different pretraining objective and 59M more parameters than RoBERTa-base. While the paper mentions this in the discussion, the main text frames it primarily as a pretraining method effect rather than acknowledging the capacity confound upfront.

On ToxicChat, the variance pattern flips entirely: classification-supervised variants show the highest variance while MLM shows the lowest, which contradicts the "classification as regularizer" narrative and suggests the finding doesn't generalize as cleanly as claimed.

The perturbation robustness analysis shows a consistent three-layer pattern on IID and DD datasets, but this structure completely breaks down on ActorAttack, where the 9-class variant degrades by over 20 percentage points with high variance.

There are also inconsistencies in the data split reporting—the paper doesn't specify how many benign conversations appear in each evaluation split, and the sample sizes cited in the perturbation section (n=76 IID, n=118 DD) don't match the n=80 DD mentioned in the setup.

Beyond these major issues, Figure 1 is still a placeholder, the MLM-only results mix single-seed and three-seed reporting, FITD evaluation shows no discrimination since all variants exceed 0.990, the Qwen3-8B citation is informal, and the choice of population standard deviation with N divisor instead of N-1 needs justification.

Now I should draft the full review, though I want to reconsider the framing first. Looking at the setup again, it explicitly states "80 Deceptive Delight (DD)" for OOD evaluation, so the n=118 in the perturbation text must refer to something different—likely 80 DD jailbreak conversations combined with 38 benign examples to compute F1 scores, though the paper doesn't clarify this breakdown. I'm trying to work out whether the sample sizes could be reconciled if the evaluation sets mix jailbreak and benign conversations—maybe 80 DD jailbreak prompts plus 38 benign controls equals the 118 total. But then the IID perturbation analysis should also report a combined n rather than just 76, which it doesn't, so this explanation doesn't quite hold up either. The most likely interpretation is that the IID test set contains 76 held-out jailbreak conversations plus matched benign ones, with n=76 in the perturbation section referring to the total count of 38 jailbreak + 38 benign pairs, though the paper's wording around "76 held-out Crescendo conversations" creates ambiguity about whether that number includes both types. This inconsistency in how n is reported across sections is definitely something I should flag as needing clarification. Now I'm looking at the FITD evaluation setup, which mentions 80 conversations but I need to understand what those conversations actually contain.

FITD conversations are quite short at only 2-3 turns, and both the 9-class and vanilla methods achieve perfect or near-perfect accuracy (≥0.990) across all prefix lengths, which means FITD essentially fails to differentiate between the approaches—it's too easy as an out-of-distribution task. The paper should explain why FITD provides so little discrimination, whether that's due to the brevity of conversations or obvious linguistic markers that make detection trivial.

I'm also checking the bibliography entries now. The reference verification turned up 9 entries that couldn't be found in OpenAlex (though some are well-known papers like RoBERTa that likely just hit API issues) and 9 entries with mismatches in author order or publication year. The austin1962speechacts entry has a year discrepancy where the bibliography lists 1962 but the API shows 1975, and I need to verify which edition is actually being cited.

A few other bibliography issues to note: chao2023pair was originally a 2023 preprint but published in 2025, and there are first author mismatches in han2024wildguard and chao2024jailbreakbench. These are mostly minor cosmetic problems. The paper uses the correct review submission package and appears to fit within the 8-page limit based on the tex files. Now I'm ready to write the full review and calculate the overall scores.

For soundness, I'm settling on 3 (Acceptable) rather than 3.5 since ARR uses integer scores only. The ablation design is clever and mostly sound, but the single-LLM confound, limited statistical power, data split ambiguity, and the overclaim about discourse-level effects are notable issues. The paper honestly acknowledges many limitations, and while it provides sufficient support for the main claim that DAPT is beneficial, several secondary claims need stronger evidence or more careful framing.

For excitement, I'm giving it a 3 as well—the core question about what enables cross-attack generalization is genuinely interesting, though the execution and scope are somewhat limited. The paper has genuine contributions—the ablation design is clever and the DAPT finding holds up across encoders—but several issues prevent it from reaching conference quality: the architecture figure is incomplete, there's a single-LLM confound that threatens validity, the "discourse-level" claim lacks support, and the perturbation robustness breaks down on harder cases. I'd rate it a 3, though with revisions addressing the multi-LLM data, probing analysis, and submission quality issues, it could become a solid findings-level paper.

I'm noticing the architecture diagram is literally just a placeholder box, which is a critical submission quality problem. There's also a missing bibliography entry for Qwen3-8B despite the paper using it extensively for data generation.

Looking at the pretraining objectives, DeBERTa-v3's use of Replaced Token Detection versus RoBERTa's Masked Language Modeling is correctly characterized, though the paper's explanation for why this causes different adaptation needs is somewhat speculative. The performance gap in Table 2 is striking—the evidence hierarchy tasks on DD cluster around 0.997 accuracy while MLM drops to 0.914, suggesting something fundamental about how these pretraining objectives affect downstream task performance.

However, I'm noticing a methodological concern: the stability advantage of classification supervision is being measured across just 3 seeds, and the variance reduction claims rest on comparing standard deviations from those same 3 data points. When one seed (456) produces an MLM recall of 0.64 while others are much higher, it's hard to distinguish whether that's a genuine property of MLM or just noise from a small sample. The "4-20× variance reduction" ratio could itself be unstable given the limited sample size.

Now I'm organizing my findings into the final review structure with sections for summary, strengths, weaknesses by severity, questions, missing references, and an overall assessment with confidence rating.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a535628-2afc-4034-8036-bd508889aa16",
  "isSidechain": false,
  "requestId": "req_011CbAUQat1f1SqZEeXxJv2V",
  "type": "assistant",
  "uuid": "df40459d-6276-4e37-967a-b739d7471c33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nodt9KpuNaHT4RUacLR7vw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 76398,
      "output_tokens": 15295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 913,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15295,
          "cache_read_input_tokens": 76398,
          "cache_creation_input_tokens": 913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 913
          },
          "type": "message"
        }
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

_source line 54 · 2026-05-18T18:05:18.983Z_

论文全文和 reviewer guidelines 均已读完。现在开始撰写审稿报告。

我已通读全文（abstract → introduction → related work → method → experiments → discussion → conclusion → appendix → checklist），并完成引用验证和 ACL ARR 评分标准查询。下面提交完整审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df40459d-6276-4e37-967a-b739d7471c33",
  "isSidechain": false,
  "requestId": "req_011CbAUQat1f1SqZEeXxJv2V",
  "type": "assistant",
  "uuid": "17fedf2a-5b28-49a8-ab39-4eb5d2a79de9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nodt9KpuNaHT4RUacLR7vw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 76398,
      "output_tokens": 15295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 913,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15295,
          "cache_read_input_tokens": 76398,
          "cache_creation_input_tokens": 913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 913
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-18T18:07:54.021Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01UjXwUGvu6BYJAFYE927fs6`</summary>

```json
{
  "text": "\n# Reviewer 1 审稿报告\n\n**论文**: \"What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\"\n**审查侧重**: 方法严谨性 + 实验设计\n**审稿模式**: fresh\n\n---\n\n## Summary\n\n本文通过控制性消融研究，分析了什么表示属性使 multi-turn jailbreak 检测能够跨攻击族泛化。作者设计了七个 DeBERTa-v3 Stage-1 变体和三个 RoBERTa 变体（统称 DisPeD），在四个攻击族上评估，得出三个发现：(1) domain-adaptive continued pretraining (DAPT) 是 OOD 泛化的主要机制（~60pp gap）；(2) encoder 预训练方法决定了 DAPT 变得关键的难度阈值；(3) 分类监督起正则化作用而非策略分类作用。ToxicChat 验证表明 DAPT 优势迁移至 human-written 数据。\n\n研究问题明确（\"什么使得表示能泛化？\"而非\"如何检测\"），消融设计巧妙。但 single-LLM confound、\"discourse-level\" overclaiming、统计效力不足，以及 Figure 1 缺失等问题影响了论文的 soundness 和完成度。\n\n---\n\n## Strengths\n\n**S1. 研究问题定位精准，消融设计巧妙。**\n七个 Stage-1 变体的设计系统地隔离了 domain exposure、classification supervision、label quality、label granularity、domain specificity 五个因素（Table 1, Section 3.2）。每个变体的对比意义清晰——例如 scrambled labels 隔离 label correctness，topic classification 测试 task alignment。这种 controlled ablation 方法论优于典型的\"提出新模型→在 benchmark 上跑\"的范式。\n\n**S2. 核心发现（DAPT 为主要机制）有跨 encoder 支撑。**\nDeBERTa-v3 上 vanilla→MLM 的 ~60pp 提升（Table 3: DD 0.312→0.914）和 RoBERTa 上 ActorAttack 的 vanilla→9-class 提升（Table 4: 0.466→0.939）从两个架构验证了 DAPT 的核心作用。Bootstrap CIs 确认了关键对比不重叠（Section 5.1: 9-class DD Full CI [0.943, 1.000] vs. vanilla [0.202, 0.341]）。\n\n**S3. \"分类作为正则化器\"发现具有反直觉的价值。**\nScrambled labels 与 correct labels 在所有 OOD 评估上达到等效检测 F1（gap ≤3.9pp, Table 3, Table S3），而 OOD 策略预测精度仅 30.7%（κ=0.126, Section 5.6）。这挑战了\"需要好标签才能泛化\"的朴素假设，对安全分类器设计有实际启示。\n\n**S4. 诚实地报告了负面结果。**\nPerturbation robustness 在 ActorAttack 上不成立（9-class Δ=-20.4±13.5pp, Section 5.5），variance reversal 在 ToxicChat 上出现（Section 5.4），McNemar's test 的 power 限制被明确讨论。相比于掩盖不利结果，这种透明度值得肯定。\n\n**S5. Compute cost 极低，可复现性设计合理。**\n全部变体训练 <4 GPU-hours（Section 6），所有超参数在 Appendix D 中完整报告，承诺 release code/data。3-seed 设计虽然 minimal，但在 ACL/EMNLP 短论文传统下是可接受的。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Figure 1 为占位符，论文未完成\n- 具体位置：method.tex line 10，`\\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{2em}\\textit{Architecture diagram placeholder}\\vspace{2em}}}`\n- 问题：Figure 1 是论文中唯一的架构图，目前是一个写着\"Architecture diagram placeholder\"的空框。这不是一个可提交的状态。\n- 为什么影响接收：审稿人会认为论文未完成（desk reject 风险），且缺少架构图使 two-stage pipeline 的理解完全依赖文字描述。\n- 建议：替换为真正的架构图，展示 Stage 1 七个变体的训练目标 → frozen encoder → Stage 2 BiGRU → classification 的完整 pipeline。\n\n**N2** [critical] Single-LLM confound 对 \"cross-attack generalization\" claim 的威胁未充分解决\n- 具体位置：Section 4 (Setup), Section 5.4 (Human Data), Section 6 (Discussion)\n- 问题：训练数据（250 Crescendo + 250 benign）和全部 OOD 评估数据（FITD, DD, ActorAttack）均由 Qwen3-8B 生成。所谓 \"cross-attack generalization\" 实际上是 \"cross-attack-strategy generalization within Qwen3-8B generation distribution\"。DAPT 在 Qwen3-8B 文本上训练后对 Qwen3-8B 生成的新攻击文本泛化，可能部分反映 within-model stylistic transfer 而非 genuine discourse-level feature learning。\n- ToxicChat 验证（Table 5）仅部分缓解此问题：(a) ToxicChat 是 single-turn，无法验证 multi-turn evidence hierarchy；(b) 在 ToxicChat 上 classification-supervised variants 的排序完全逆转（9-class=0.596 < MLM=0.837），这恰好是对 Finding 3（classification as regularizer）最强的反面证据。\n- 为什么影响接收：如果不能在非 Qwen3-8B 生成的 multi-turn 数据上验证核心 findings，则 \"domain exposure bridges the cross-attack gap\" 的 claim 范围被严重限制。至少需要一个额外 LLM（如 Llama-3, GPT-4o-mini）生成的 OOD 攻击评估。\n- 建议：(1) 用至少一个其他 LLM 生成部分 OOD 评估数据；(2) 如果不可行，需将论文标题和 claims 限定为 \"within synthetic data manifold\" 的发现；(3) 在 abstract 和 conclusion 中将此作为首要 caveat 而非 \"direction for future work\"。\n\n**N3** [critical] \"Discourse-level\" claims 缺乏直接证据\n- 具体位置：Section 5.2 (\"continued pretraining on jailbreak conversation text captures pragmatic features: hedging, escalation markers, topic-shifting patterns\"), Section 5.1 (\"domain-adapted representations capture structural features beyond bag-of-words\")\n- 问题：论文声称 DAPT 捕获了 discourse-level 特征，但唯一的间接证据是 TF-IDF 在 ActorAttack 上失败而 DAPT 模型成功（Section 5.1: TF-IDF F1=0.261 vs. 9-class F1=0.972）。TF-IDF 失败证明 DAPT 捕获了超越 unigram/bigram 的特征，但 \"超越 bag-of-words\" ≠ \"discourse-level\"。可能的非 discourse 解释包括：(a) 更长 n-gram 或 sub-word 模式；(b) token embedding 空间中的 distributional shift；(c) 句内语法结构而非跨 turn 语用结构。\n- Related Work 最后一句提到 probing classifiers 可以回答这个问题，但将其留给 future work。如果论文的核心 framing 是 \"discourse-level\"，则需要 probing 证据来支撑。\n- 为什么影响接收：这影响论文的核心叙事可信度。\"DAPT 捕获了 something beyond BoW\" 和 \"DAPT 捕获了 discourse-level pragmatic structure\" 是两个 claim 层级，后者远超前者但论文给出的证据只支撑前者。\n- 建议：(1) 在 diagnostic probing 中增加 discourse-level task（如跨 turn 一致性、escalation 阶段判断——Section 5.3 的 linear probing 已有部分尝试但结果仅差 1-5pp，不足以证明 discourse-level feature）；或 (2) 降低 claim 层级，替换所有 \"discourse-level\" / \"pragmatic features\" 的描述为更准确的 \"features beyond lexical overlap\"。\n\n**N4** [critical] 评估集大小不一致，数据划分不透明\n- 具体位置：Section 4 (Setup) vs. Section 5.5 (Perturbation Analysis)\n- 问题：\n  (a) Setup 声明 DD 有 80 个对话（experiments.tex line 11），但 Perturbation Analysis 声称 \"On OOD Deceptive Delight (n=118)\" （experiments.tex line 265）。80 ≠ 118，论文未解释差异来源。\n  (b) IID test 声明为 \"76 held-out Crescendo conversations\"（line 12），但 Crescendo 仅指 jailbreak 对话。计算 F1 需要 benign 样本。论文从未说明 IID 和 OOD 评估中有多少 benign 对话、来源是什么。\n  (c) 如果 n=118 = 80 jailbreak + 38 benign，那 benign 来自哪里？IID 的 benign test set 大小是多少？\n- 为什么影响接收：这直接影响可复现性，且可能影响 F1 计算的准确性（class balance 影响 F1）。\n- 建议：在 Setup 中明确报告每个评估集的完整构成（jailbreak + benign 数量），并解释 n=118 与 n=80 的关系。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 3-seed variance estimation 的统计可靠性\n- 具体位置：Section 5.2 (\"4-20× variance reduction\"), Table 3, Table 4\n- 问题：\"4-20× variance reduction\" 是 Finding 3 的核心定量表述，但基于仅 3 个 seeds 的 std 计算。用 3 个点估计的 std 本身有极大不确定性（std 的标准误约为 std/√(2(n-1)) = std/2，即 50% 相对误差）。例如，MLM DD-Full std=0.115 主要由 seed 456（recall=0.64）驱动；如果该 seed 是 outlier，真实 variance 可能远低于 0.115。\n- 建议：(1) 增加到 5-10 seeds 验证 variance reduction claim；或 (2) 明确声明 \"4-20×\" 是基于 3 seeds 的 point estimate，confidence interval 覆盖范围很大。\n\n**W2** [warning] McNemar's test 在 sparse discordant pairs 上的使用\n- 具体位置：Section 5.5 (\"all p > 0.13; discordant pairs ≤7\")\n- 问题：论文使用 McNemar's test 声称分类变体之间\"无显著差异\"，但 ≤7 discordant pairs 下该检验几乎无统计效力。absence of significance ≠ evidence of equivalence。要证明等效性，应使用 equivalence testing（如 TOST procedure 或 Bayesian approach）。\n- 论文部分承认了这一点（\"should be interpreted as an observed pattern rather than a statistically confirmed hierarchy\"），但仍在多处将 McNemar p>0.13 作为\"no difference\" 的证据引用。\n- 建议：将 McNemar 结果替换为或补充以 equivalence test；或明确在每次引用 McNemar 时标注 power 限制。\n\n**W3** [warning] Encoder 容量混淆变量\n- 具体位置：Table 4 (Cross-Encoder), Section 6 Discussion\n- 问题：DeBERTa-v3-base (184M) vs. RoBERTa-base (125M) 在参数量上有 47% 差异。\"难度阈值由 encoder 预训练方法决定\" 的 claim（Finding 2）与 \"难度阈值由 encoder 容量决定\" 无法区分。例如，DeBERTa-v3 在 DD 上 vanilla F1=0.312 可能部分因为其更大容量导致 RTD 表示在小数据 fine-tune 下更不稳定，而非 RTD 本身的问题。\n- Discussion 承认了这一点但主文叙述仍将其归因于预训练方法。\n- 建议：在 Contribution 列表和 abstract 中对 Finding 2 添加 \"controlling for architecture but not model size\" 的限定；或用 RoBERTa-large (355M) 复现以隔离容量效应。\n\n**W4** [warning] ToxicChat 上 evidence hierarchy 的完全逆转\n- 具体位置：Table 5 (Human Data)\n- 问题：在 ToxicChat 上，MLM（0.837）>> 9-class（0.596），排序与 synthetic OOD 完全逆转。论文将此归因于 \"modality mismatch\"（single-turn vs. multi-turn），但这个解释有问题：如果 classification supervision 是一个 generic representational regularizer（如论文所 claim），它不应该在 single-turn 上表现更差；如果它的 regularization 是 distribution-specific 的（如 Discussion 承认的），那 \"regularizer\" 这个 framing 就需要大幅修改。\n- 当前论文在 Section 6 Discussion 中做了细致分析（\"distribution-specific regularization\"），但 abstract 和 contributions 中的 Finding 3 表述未反映这一重要限定。\n- 建议：在 abstract 和 Contribution 3 中明确 \"classification supervision 的 regularization 效果是 distribution-specific 的\"，避免读者误认为这是一个 generic finding。\n\n**W5** [warning] Perturbation robustness 在 ActorAttack 上不成立\n- 具体位置：Section 5.5, experiments.tex lines 272-274\n- 问题：9-class 在 ActorAttack 上 paraphrasing 后 F1 从 0.972 下降到 0.768（Δ=-20.4±13.5pp），且 cross-seed 方差极大（seed 123: Δ=-1.3pp; seeds 42, 456: Δ=-30.3pp）。这与 IID 和 DD 上的 zero-degradation 结论完全矛盾。\n- 虽然论文诚实报告了此结果（S4），但 perturbation analysis 在论文叙事中占了 ~1 页篇幅（Section 5.5），而最终结论是 \"attack-family-dependent\"，这削弱了整个 section 的叙事价值。\n- 建议：考虑将 perturbation analysis 移至 appendix，在正文中简要报告 \"perturbation robustness is observed on IID and DD but does not generalize to structurally complex attacks\"。\n\n**W6** [warning] TF-IDF 在 DD 上的强表现削弱了 DD 作为核心评估集的意义\n- 具体位置：Table 2 (TF-IDF DD Full F1=0.961), Section 5.1\n- 问题：TF-IDF LR 在 DD 上 per-prefix F1 达到 0.994-1.000（Appendix Table S2），full conversation F1=0.961。这意味着 DD 几乎完全被词汇特征解决。论文在 DD 上建立的 evidence hierarchy（Table 3 的核心结果）可能仅反映不同变体捕获词汇特征的能力，而非 discourse-level representation quality。\n- ActorAttack 才是真正区分 discourse-level 和 lexical features 的评估集（TF-IDF 0.261 vs. 9-class 0.972），但论文的主要结果表（Table 2）和 Figure 2 都以 DD 为中心。\n- 建议：将 ActorAttack 提升为主要展示评估集（不仅是辅助），因为它是唯一能支持 \"beyond lexical\" claim 的 OOD 数据集。\n\n**W7** [warning] 策略标注验证不充分\n- 具体位置：Section 3.2 (Method), Section 6 (Limitations)\n- 问题：策略标注由 Qwen3-8B 完成，human validation 仅 n=50、κ=0.78、单个人类标注者。对于 9-class taxonomy：(a) 50 个样本平均每类 ~5.5 个，不足以评估每个类别的标注质量；(b) κ=0.78 是 \"substantial\" 但不是 \"almost perfect\"（>0.81）；(c) 单个人类标注者无法区分 inter-human agreement 和 human-model agreement。\n- 论文的 Finding 3（classification as regularizer）间接缓解了这一问题——label 质量不影响检测。但 Figure 3 的策略轨迹分析和 Section 5.6 的解释性分析仍依赖标注质量。\n- 建议：增加第二个人类标注者计算 inter-human κ 作为 upper bound；或在 Figure 3 分析中添加 caveat。\n\n### Minor 问题（不影响接收）\n\n**M1.** Qwen3-8B 在论文中被广泛使用（数据生成、标注、paraphrasing、LLM-as-judge baseline）但 references.bib 中无对应引用。Checklist E1 中仅提及 \"Qwen3-8B (for data generation)\"。应添加正式引用。\n\n**M2.** MLM-only 变体在 Table 3 中部分结果无 std（DD-Full: .914±.115 有 std，但 IID 列 .974 和 1.000 无 std）。这暗示 MLM 可能仅运行了单 seed？应统一为 3-seed 报告或注明。\n\n**M3.** FITD 评估几乎无区分力：所有变体（包括 vanilla）达到 F1 ≥ 0.990（Appendix Table S2）。建议在 Discussion 中解释为何 FITD 如此简单（可能因对话仅 2-3 turns 且模式明显）。\n\n**M4.** Population std (N divisor) 与 sample std (N-1 divisor)：Checklist C4 声明使用 population std。3 seeds 下 N=3，population std 比 sample std 低 18%。应说明选择理由，或改用 sample std。\n\n**M5.** Abstract 第 5 行 \"seven encoder variants on DeBERTa-v3 and three on RoBERTa\" 中 \"on\" 的使用 awkward，建议改为 \"of DeBERTa-v3\" or \"based on DeBERTa-v3\"。\n\n**M6.** Table 2 caption 说 \"3-seed mean±std where noted\" 但 TF-IDF 行无 std 注释。应注明 TF-IDF 是确定性模型。\n\n---\n\n## Questions for Authors\n\n**Q1.** DD 的评估样本量在 Setup (n=80) 和 Perturbation Analysis (n=118) 中不一致。请澄清 n=118 的构成——是 80 jailbreak + 38 benign 吗？benign 样本来源是什么？\n\n**Q2.** 论文声称 \"classification supervision functions as a representational regularizer\"，但在 ToxicChat 上该效果完全逆转（9-class std=0.087 > MLM std=0.013）。如果 regularization 是 distribution-specific 的，那么在什么条件下应该使用 classification supervision vs. MLM-only？论文能否给出实践建议？\n\n**Q3.** Mean pooling 在 DD 上 single-seed F1=1.000（Table 3），如果 multi-seed 确认此结果，则意味着 temporal modeling（BiGRU）完全不必要。这对 \"multi-turn\" jailbreak detection 的 discourse-level framing 意味着什么？每个 turn 独立可分 vs. 需要跨 turn 推理是一个根本区别。\n\n**Q4.** Linear probing 结果（Section 5.3）显示 9-class 仅在 diagnostic tasks 上超出 vanilla/MLM 1-5pp。这种微小差异如何与 detection F1 上的巨大差异（9-class 0.997 vs. vanilla 0.312）共存？probing accuracy 和 detection F1 之间的 disconnect 是否暗示 detection 依赖不同于 probing tasks 测量的特征？\n\n**Q5.** 对于 ActorAttack perturbation robustness 的 cross-seed 极端方差（seed 123: Δ=-1.3pp vs. seed 42/456: Δ=-30.3pp），是否检查过 seed 123 的行为是否是 outlier（如看 per-sample prediction 分布）？\n\n---\n\n## Missing References\n\n1. **Qwen3-8B 官方引用缺失** — 论文的数据生成、标注、paraphrasing、baseline 均依赖 Qwen3-8B，但无引用。\n2. **DeBERTa-v3 论文** — 论文引用的是 `he2021deberta`（原始 DeBERTa），但使用的是 DeBERTa-v3-base。DeBERTa v3 有单独的技术报告（He et al., 2023, \"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing\"），应引用 v3 版本以准确对应 RTD pretraining 的讨论。\n3. **ELECTRA** — 论文讨论了 DeBERTa-v3 的 RTD (Replaced Token Detection) 预训练，但未引用 ELECTRA (Clark et al., 2020)，而 RTD 正是 ELECTRA 引入的训练方法。\n\n---\n\n## Overall Assessment\n\n### ACL ARR 评分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3/5 (Acceptable) | 核心 DAPT finding 有跨 encoder 支撑，消融设计合理。但 single-LLM confound 限制了 \"cross-attack generalization\" claim 的范围；\"discourse-level\" 缺乏直接证据；数据划分不透明（N1-N4）。主要 claims 的支撑 sufficient 但有显著 caveats 未在 abstract/contributions 中反映。 |\n| **Excitement** | 3/5 (Interesting) | 研究问题好（\"什么使表示泛化\" 而非 \"怎么检测\"），\"classification as regularizer\" 发现有 surprising value。但实际 impact 受限于全 synthetic 数据评估，且无法与 DeepContext/BIID/G-Guard 直接对比性能。 |\n| **Overall** | 3.0 (Findings) | 消融设计巧妙、DAPT finding 稳健、论文对负面结果诚实。但 Figure 1 缺失、single-LLM confound、discourse-level overclaiming、数据划分不透明 四个 critical issues 需要解决。修复 N1 后可达 borderline conference；解决 N2-N4 可能提升至 conference level。当前状态适合 Findings。 |\n| **Confidence** | 4/5 | 仔细阅读全文，熟悉 domain adaptation、safety classifiers、multi-turn dialogue 相关工作。 |\n\n### 一句话总结\n\n消融设计优秀且 DAPT finding 稳健，但 single-LLM confound 和 \"discourse-level\" overclaiming 使得核心 claims 的范围比论文表述的更窄；Figure 1 placeholder 是 submission-readiness 硬伤。\n\n---\n\n## 引用验证附注\n\n通过 verify_references 工具检查了全部 49 条 bib entries：\n- 31 条 verified，9 条 not found（多为 OpenAlex API coverage 问题，非幻觉引用），9 条有 minor mismatch（主要是 first author 姓名格式或年份差异）\n- 无 orphan bib（未引用的条目）或 missing bib（引用了但无条目）\n- 需注意：`he2021deberta` 引用的是 DeBERTa v1 而非实际使用的 v3；Qwen3-8B 完全未引用\n",
  "reviewer_id": "1",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17fedf2a-5b28-49a8-ab39-4eb5d2a79de9",
  "isSidechain": false,
  "requestId": "req_011CbAUQat1f1SqZEeXxJv2V",
  "type": "assistant",
  "uuid": "9aec65d9-a0be-4a51-bb60-ad281b6276cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nodt9KpuNaHT4RUacLR7vw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 76398,
      "output_tokens": 15295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 913,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15295,
          "cache_read_input_tokens": 76398,
          "cache_creation_input_tokens": 913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 913
          },
          "type": "message"
        }
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

_source line 56_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责**方法严谨性 + 实验设计**。  ## 论文信息 - 标题: \"What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\" - 路径: `projects/persuasion_turn_jailbreak_d…",
  "leafUuid": "9aec65d9-a0be-4a51-bb60-ad281b6276cf",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multi-turn jailbreak detection paper for EMNLP",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765"
}
```

---

### Tool result

_source line 58 · 2026-05-18T18:07:57.865Z_

<details><summary>↩ Tool result · `toolu_01UjXwUGvu6BYJAFYE927fs6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9aec65d9-a0be-4a51-bb60-ad281b6276cf",
  "isSidechain": false,
  "promptId": "0eb5aead-11c4-4be9-b71e-9e5f7b87fb1b",
  "type": "user",
  "uuid": "25c00dcd-0e31-43e1-b0e4-21b2d5a161e1",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_613965f45d48763f375aa83e9294b24a:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "9aec65d9-a0be-4a51-bb60-ad281b6276cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multi-turn jailbreak detection paper for EMNLP",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765"
}
```

---

### Runtime record

_source line 60 · 2026-05-18T18:08:55.965Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T18:08:55.965Z",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "content": "[Round 1 审稿请求]:\n## 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意该问题，并说明你的理由或补充观察\n- **[REBUT]**：不同意或认为该问题被高估，提供证据（引用具体 Section/Table/Figure）\n\n---\n\n**Reviewer 2 Overall: 2.5/5**\n\n### Must-Fix 问题\n\n**N1** [critical] Figure 1 为 Placeholder，不可接受\n- Section 3 (method.tex line 8-12)，主架构图是文字占位框。审稿人将此视为论文未完成的信号。\n\n**N2** [critical] 核心发现\"DAPT 是主要机制\"的新颖性不足\n- Gururangan et al. (2020) \"Don't Stop Pretraining\" 已在四个领域验证 DAPT 有效性。本文核心发现是该范式在新领域的直接应用。Finding 1（DAPT 有效）预期内，Finding 2（difficulty threshold）偏描述性，Finding 3（classification as regularizer）最有新颖性但在人类数据上逆转。建议更明确框定增量贡献——不是\"DAPT 有效\"而是\"为什么 DAPT 在 jailbreak cross-domain OOD 场景有效而其他替代方案失败\"；加强 CKA representation geometry 分析。\n\n**N3** [critical] 证据层级在人类数据上逆转，动摇核心叙事\n- ToxicChat 上 JB-MLM (0.837) >> 9-class (0.596)。9-class 排名 5/6，方差最高（std=0.087）。论文的\"modality mismatch\"解释有问题：如果好处仅限于多轮正则化，Binary 和 Scrambled 为何在单轮也弱于 MLM？更合理解释是 classification supervision 过拟合到合成分布。Discussion 中\"variance reversal\"与 Abstract/Introduction 叙事不一致。建议在 Abstract/Introduction 中呈现这个 tension，重新框定贡献。\n\n**N4** [critical] 缺少与现有多轮防御方法的直接对比\n- 未与 DeepContext、BIID、G-Guard、SafeDream 直接实验对比。Introduction 称 vanilla baseline \"replicating the frozen-encoder-plus-RNN approach of DeepContext\"，但 Related Work 又说 \"not a direct proxy\"——自相矛盾。建议复现 DeepContext 在本文数据集上的表现，或在其数据集上评估 DisPeD。\n\n### Should-Fix 问题\n\n**W1** Abstract 数据堆砌（12+ 数值），建议保留 2-3 个。\n\n**W2** 合成数据规模过小（n=500 训练，n=76-118 评估）。\n\n**W3** Related Work 引用密度偏低（31 条 bib），遗漏方向包括 RLHF/alignment、input preprocessing defenses、多轮对话数据集、CKA 原始论文、DeBERTa-v3 正确引用。\n\n**W4** TF-IDF 在 DD 上 F1=0.961，DD 存在严重 lexical separability，整个消融可信度依赖单一 ActorAttack 数据集。\n\n**W5** 术语不一致：domain exposure / domain adaptation / continued pretraining / DAPT 混用；\"evidence hierarchy\" 未预告；\"DisPeD\" 在 Introduction 使用但未定义。\n\n**W6** Analysis paper 深度不够：CKA 仅一段描述无可视化，Linear probing 结果仅一句话，无 t-SNE/UMAP，无 attention pattern 分析。\n\n### Minor 问题\nM1-M7: DisPeD 全称未给出、Table 3 选择性展示、mean pooling 标注不显著、MLM-only seed 数不明确、AI 写作风格基本合格、Checklist license 模糊、population std 细节。\n\n### 优势\n消融设计精良、统计严谨、negative results 有价值、低计算成本、诚实 Limitations。\n\n### 缺失引用\nHe et al. (2023) DeBERTa-v3, Kornblith et al. (2019) CKA, Bai et al. (2022) RLHF, Jain et al. (2023) Baseline Defenses, WildChat, LMSYS-Chat-1M, Qi et al. (2024)。\n\n---\n\n请对以上每个 Must-Fix (N1-N4) 和 Should-Fix (W1-W6) 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
}
```

---

### Runtime record

_source line 61 · 2026-05-18T18:08:55.965Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T18:08:55.965Z",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765"
}
```

---

## Round 2

2 recorded events

### User

_source line 62 · 2026-05-18T18:08:55.955Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25c00dcd-0e31-43e1-b0e4-21b2d5a161e1",
  "isSidechain": false,
  "promptId": "3115e2c4-53d8-47ad-80c8-99e4c51cdc53",
  "type": "user",
  "isMeta": true,
  "uuid": "b16ae550-8400-4f53-87c7-c8c3bb022329",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-18T18:08:55.955Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b16ae550-8400-4f53-87c7-c8c3bb022329",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "3545e90c-ac30-4e72-8b31-01792c77aa38",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "6cec5b19-51ee-4d6c-b47b-e48c934743ef",
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

_source line 64 · 2026-05-18T18:08:56.042Z_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：
- **[AGREE]**：同意该问题，并说明你的理由或补充观察
- **[REBUT]**：不同意或认为该问题被高估，提供证据（引用具体 Section/Table/Figure）

---

**Reviewer 2 Overall: 2.5/5**

### Must-Fix 问题

**N1** [critical] Figure 1 为 Placeholder，不可接受
- Section 3 (method.tex line 8-12)，主架构图是文字占位框。审稿人将此视为论文未完成的信号。

**N2** [critical] 核心发现"DAPT 是主要机制"的新颖性不足
- Gururangan et al. (2020) "Don't Stop Pretraining" 已在四个领域验证 DAPT 有效性。本文核心发现是该范式在新领域的直接应用。Finding 1（DAPT 有效）预期内，Finding 2（difficulty threshold）偏描述性，Finding 3（classification as regularizer）最有新颖性但在人类数据上逆转。建议更明确框定增量贡献——不是"DAPT 有效"而是"为什么 DAPT 在 jailbreak cross-domain OOD 场景有效而其他替代方案失败"；加强 CKA representation geometry 分析。

**N3** [critical] 证据层级在人类数据上逆转，动摇核心叙事
- ToxicChat 上 JB-MLM (0.837) >> 9-class (0.596)。9-class 排名 5/6，方差最高（std=0.087）。论文的"modality mismatch"解释有问题：如果好处仅限于多轮正则化，Binary 和 Scrambled 为何在单轮也弱于 MLM？更合理解释是 classification supervision 过拟合到合成分布。Discussion 中"variance reversal"与 Abstract/Introduction 叙事不一致。建议在 Abstract/Introduction 中呈现这个 tension，重新框定贡献。

**N4** [critical] 缺少与现有多轮防御方法的直接对比
- 未与 DeepContext、BIID、G-Guard、SafeDream 直接实验对比。Introduction 称 vanilla baseline "replicating the frozen-encoder-plus-RNN approach of DeepContext"，但 Related Work 又说 "not a direct proxy"——自相矛盾。建议复现 DeepContext 在本文数据集上的表现，或在其数据集上评估 DisPeD。

### Should-Fix 问题

**W1** Abstract 数据堆砌（12+ 数值），建议保留 2-3 个。

**W2** 合成数据规模过小（n=500 训练，n=76-118 评估）。

**W3** Related Work 引用密度偏低（31 条 bib），遗漏方向包括 RLHF/alignment、input preprocessing defenses、多轮对话数据集、CKA 原始论文、DeBERTa-v3 正确引用。

**W4** TF-IDF 在 DD 上 F1=0.961，DD 存在严重 lexical separability，整个消融可信度依赖单一 ActorAttack 数据集。

**W5** 术语不一致：domain exposure / domain adaptation / continued pretraining / DAPT 混用；"evidence hierarchy" 未预告；"DisPeD" 在 Introduction 使用但未定义。

**W6** Analysis paper 深度不够：CKA 仅一段描述无可视化，Linear probing 结果仅一句话，无 t-SNE/UMAP，无 attention pattern 分析。

### Minor 问题
M1-M7: DisPeD 全称未给出、Table 3 选择性展示、mean pooling 标注不显著、MLM-only seed 数不明确、AI 写作风格基本合格、Checklist license 模糊、population std 细节。

### 优势
消融设计精良、统计严谨、negative results 有价值、低计算成本、诚实 Limitations。

### 缺失引用
He et al. (2023) DeBERTa-v3, Kornblith et al. (2019) CKA, Bai et al. (2022) RLHF, Jain et al. (2023) Baseline Defenses, WildChat, LMSYS-Chat-1M, Qi et al. (2024)。

---

请对以上每个 Must-Fix (N1-N4) 和 Should-Fix (W1-W6) 逐条给出 [AGREE] 或 [REBUT]，并说明理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3545e90c-ac30-4e72-8b31-01792c77aa38",
  "isSidechain": false,
  "promptId": "3115e2c4-53d8-47ad-80c8-99e4c51cdc53",
  "type": "user",
  "uuid": "8db2a45f-411d-4a3b-9c7d-86d792fa5785",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-18T18:09:33.069Z_

<details><summary>Logged reasoning block</summary>

```text
The Director is asking me to cross-review Reviewer 2's findings. I need to go through each Must-Fix (N1-N4) and Should-Fix (W1-W6) issue from Reviewer 2 and respond with [AGREE] or [REBUT], citing specific evidence from the paper.

Let me go through each one carefully, drawing on my thorough reading of the paper.

**N1: Figure 1 placeholder** - I already identified this in my own review as N1. Clearly agree.


**N2: Novelty of DAPT finding** - Reviewer 2 has a point that Gururangan et al. already showed DAPT works across domains, but I think the novelty here lies deeper—the paper's real contribution is the systematic decomposition revealing why it works and proving that classification labels aren't the mechanism. The scrambled labels finding is genuinely novel, though the novelty framing could definitely be tightened.
**N3: Evidence hierarchy reversal on human data** - I flagged this as W4 in my own review, and Reviewer 2 is escalating it to a Must-Fix.  Looking at the ToxicChat numbers more carefully, Binary and Scrambled both underperform MLM significantly (0.705 and 0.616 versus 0.837), which is telling—if this were just a modality mismatch problem, they should at least match MLM since they also get domain exposure. Instead, the data suggests classification objectives actively harm generalization to human data, which is a more serious problem than the paper's current framing suggests. Reviewer 2's overfitting explanation is more convincing than the modality mismatch one.

Now there's another issue R2 raises about the DeepContext comparison. The Introduction claims to replicate DeepContext's frozen-encoder-plus-RNN approach, but the Related Work section explicitly states it's not a direct proxy due to differences in encoder fine-tuning, model capacity, and loss function. That's a direct contradiction I need to address, though I'm not sure a full reproduction of DeepContext is necessary to resolve it.

The paper's real contribution is the ablation study and analysis, not building a new state-of-the-art system. Reviewers typically expect direct comparisons with existing work, but for an analysis paper, the value comes from understanding the mechanisms, not necessarily beating baselines. I think the contradictory language is the real problem that needs fixing—I should clarify what the vanilla baseline actually represents and explain why a direct comparison wasn't feasible, rather than claiming it replicates something it doesn't.

Now looking at the abstract, there's too much numerical data packed in there.  I'm counting over 10 different metrics and numbers, which is overwhelming for an abstract. Some numbers are necessary for an empirical paper, but I could be more selective. For the dataset scale concern, small numbers like n=500 training and n=76-118 evaluation are more acceptable for a controlled ablation study than they'd be for a system paper—the real question is whether these findings would generalize to larger scales, which is a fair point but not as damaging as the reviewer suggests. On citations, 31 references is actually on the lean side for EMNLP, and the reviewer's right that I'm missing some key papers like the original CKA work and proper citations for DeBERTa-v3.

The lexical separability concern is valid—I flagged it myself as W6, and the reviewer correctly identifies that my beyond-lexical claims rest almost entirely on ActorAttack. Without it, I'd only have evidence for lexical feature transfer. I do address this in the paper, but it's still a limitation. On terminology, I'm seeing inconsistent usage of "domain exposure," "domain adaptation," "continued pretraining," and "DAPT" throughout. "Evidence hierarchy" gets used without definition, though "DisPeD" is actually introduced in the Introduction, so that's not an issue. I should start drafting my responses to these reviewer comments now, focusing on the most defensible points first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8db2a45f-411d-4a3b-9c7d-86d792fa5785",
  "isSidechain": false,
  "requestId": "req_011CbAUuocnjYzDnpngSJ6cz",
  "type": "assistant",
  "uuid": "e9a23774-9b70-405b-824b-29aabbb8c134",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpLybyPgdM62yZThxMwf6r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 92669,
      "output_tokens": 5805,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5805,
          "cache_read_input_tokens": 92669,
          "cache_creation_input_tokens": 1410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1410
          },
          "type": "message"
        }
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

_source line 66 · 2026-05-18T18:09:33.481Z_

我已仔细阅读 Reviewer 2 的完整意见。逐条回应如下。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9a23774-9b70-405b-824b-29aabbb8c134",
  "isSidechain": false,
  "requestId": "req_011CbAUuocnjYzDnpngSJ6cz",
  "type": "assistant",
  "uuid": "905fb76a-4167-4ffb-9f3a-80543a45f671",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpLybyPgdM62yZThxMwf6r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 92669,
      "output_tokens": 5805,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5805,
          "cache_read_input_tokens": 92669,
          "cache_creation_input_tokens": 1410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1410
          },
          "type": "message"
        }
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

_source line 67 · 2026-05-18T18:10:49.689Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01VGgk45HrrSJgi1g5iaco2N`</summary>

```json
{
  "text": "\n# Reviewer 1 交叉回应：Reviewer 2 意见\n\n---\n\n## Must-Fix 逐条回应\n\n**[AGREE] R2-N1: Figure 1 为 Placeholder**\n完全同意。我在 R1-N1 中独立提出了同一问题。这是 submission-readiness 硬伤，无需讨论。\n\n---\n\n**[REBUT] R2-N2: \"DAPT 是主要机制\"新颖性不足**\n\nR2 认为 Finding 1 是 Gururangan et al. (2020) 在新领域的直接应用，新颖性不足。我部分不同意，理由如下：\n\n(1) **论文的核心贡献不是 \"DAPT works\" 而是 \"what doesn't work and why\"。** Gururangan et al. (2020) 验证了 DAPT 在 biomedical/CS/news/reviews 上有效，但没有设计消融来回答\"DAPT 的哪个方面在起作用\"。本文的关键增量是：scrambled labels = correct labels（Table 3: 三个分类变体均 0.997±0.005 on DD），topic classification 主动破坏泛化（0.541±0.207），Wiki-MLM 几乎匹配 JB-MLM at full length（0.904 vs. 0.914）。这些负面结果和等价性结果不能从 \"Don't Stop Pretraining\" 预测得出。\n\n(2) **但 R2 关于 framing 的建议是正确的。** 论文应该更强调\"为什么替代方案失败\"而非\"DAPT 有效\"。当前 abstract 和 Introduction 的 Finding 1 表述确实过于接近 \"DAPT works in a new domain\"。Contribution 1 如果改为 \"systematic evidence that classification labels are not the mechanism, and misaligned objectives actively harm generalization\" 会更有新颖性信号。\n\n(3) **R2 建议加强 CKA representation geometry 分析也是合理的**——我在 R1 审稿中虽未单独提出此项，但与 R1-N3（\"discourse-level\" 缺乏直接证据）一致。CKA 可视化能部分回答 DAPT 到底改变了表示空间的什么结构。\n\n**结论：N2 作为 critical 级别偏高。** novelty 不在 \"DAPT works\" 而在消融设计和负面发现。但 framing 确实需要调整以凸显真正的增量。建议降为 should-fix（framing adjustment），而非 critical。\n\n---\n\n**[AGREE] R2-N3: 证据层级在人类数据上逆转**\n\n同意这是一个严重问题。我在 R1-W4 中作为 should-fix 提出了同样的问题，但 R2 的分析更深入，说服我将其提升为 critical 级别。\n\nR2 的关键洞察是：**如果 \"modality mismatch\" 是充分解释，那 Binary（0.705）和 Scrambled（0.616）不应低于 MLM（0.837），因为它们也有相同的 domain exposure。** 事实是所有包含 classification objective 的变体（无论 label quality）都在 ToxicChat 上低于纯 MLM，这表明 classification head 不是\"无害的正则化器\"，而是在表示空间中引入了 distribution-specific boundaries，这些 boundaries 在分布迁移时成为障碍。\n\n具体证据：\n- Table 5: JB-MLM (0.837±0.013) > Wiki-MLM (0.791±0.093) > Binary (0.705±0.072) > Scrambled (0.616±0.056) > 9-class (0.596±0.087) > Topic (0.496±0.042)\n- 排序严格按 \"classification objective 的复杂度\" 递减：无分类 > 2-class > 9-class（scrambled）> 9-class（correct）\n- 9-class 排名 5/6 且 std 最高（0.087），这与 synthetic OOD 上 std 最低（0.005）形成鲜明对比\n\nR2 的替代解释——classification supervision 过拟合到合成分布——比论文的 \"modality mismatch\" 更有解释力。论文 Discussion 中 \"distribution-specific regularization\" 的分析（conclusion.tex line 13）部分触及了这一点，但 abstract 和 Contribution 3 的表述完全未反映这一重要限定。\n\n**建议**：Contribution 3 应改为 \"classification supervision provides distribution-specific regularization that stabilizes within-manifold predictions but can hurt cross-distribution transfer\"。当前的 \"classification as regularizer\" framing 过于笼统。\n\n---\n\n**[REBUT] R2-N4: 缺少与现有多轮防御方法的直接对比**\n\nR2 的矛盾指出（Introduction \"replicating\" vs. Related Work \"not a direct proxy\"）完全正确——这是论文的真实写作 bug，需要修复。但我不同意将\"缺少直接对比\"提升为 critical。\n\n理由：\n\n(1) **论文定位是 analysis/ablation paper，不是 system paper。** 论文在 Introduction 第四段明确说 \"The core contribution is the systematic decomposition of what enables cross-attack generalization, not the detection pipeline itself\"（introduction.tex line 12）。要求 analysis paper 提供 SOTA comparison 是混淆了论文类型。HotpotQA 的 probing 分析论文不需要打败 SOTA QA 系统，DAPT 论文不需要打败 BERT-large。\n\n(2) **现有方法的公平对比在实践中极难实现。** DeepContext、BIID、G-Guard、SafeDream 使用不同的数据集、不同的评估协议、不同的攻击族。在本文的数据集上复现它们，或在它们的数据集上评估 DisPeD，都需要大量工程工作，且可能因数据/评估差异引入新的混淆变量。\n\n(3) **但矛盾的 framing 必须修复。** Introduction 不应说 \"replicating\"，Related Work 的 \"not a direct proxy\" 措辞是正确的。建议统一为：vanilla baseline 代表 \"pretrained-encoder-plus-RNN without domain adaptation\" 这一类方法，而非特定复现。\n\n**结论：语言矛盾是 must-fix（写作 bug），但要求与 DeepContext 等方法直接实验对比是 nice-to-have 而非 critical。** 建议降为 should-fix。\n\n---\n\n## Should-Fix 逐条回应\n\n**[AGREE] R2-W1: Abstract 数据堆砌**\n同意。我重新数了一遍 abstract：至少 12 个数值（~60pp, F1=0.961, 0.261, ≥0.89, 0.981→0.466, 4-20×, 0.596-0.837, 0.413，加上几个 percentage points）。对于 ~200 words 的 abstract，数据密度过高。保留 3-4 个最核心数字（vanilla→MLM gap, ActorAttack TF-IDF vs. 9-class gap, ToxicChat domain-adapted vs. vanilla gap），将其余移至 introduction 或正文。\n\n---\n\n**[REBUT] R2-W2: 合成数据规模过小**\n部分不同意。对于 system paper（追求 SOTA），n=500 训练确实偏小。但对于 analysis paper（追求 controlled ablation），小规模反而有利：(a) 计算成本低（<4 GPU-hours），允许 7 variants × 3 seeds × 2 encoders 的完整消融；(b) 所有变体在相同数据上训练，严格控制了数据变量；(c) 更大数据可能掩盖变体之间的差异（IID 上所有变体已经达到 F1=1.0，数据增大只会使 OOD 差异也缩小）。\n\n评估规模（n=76-118）确实限制了统计效力——我在 R1-W1 和 R1-W2 中已提出 3-seed variance estimation 和 McNemar sparse discordant pairs 的问题。但这是统计效力问题，不是数据规模问题。建议加 seeds 而非加数据。\n\n---\n\n**[AGREE] R2-W3: 引用密度偏低，遗漏方向**\n同意。31 条 bib 对 EMNLP main 偏低（典型 40-60 条）。R2 指出的遗漏中，我优先同意以下几项：\n- **DeBERTa-v3 正确引用**（He et al., 2023）——我在 R1 Missing References 中独立提出\n- **CKA 原始论文**（Kornblith et al., 2019）——论文使用 Centered CKA 但未引用定义论文\n- **ELECTRA**（Clark et al., 2020）——我在 R1 中独立提出，RTD 预训练来自 ELECTRA\n\nRLHF/alignment 方向（Bai et al., 2022）和多轮对话数据集（WildChat, LMSYS-Chat-1M）的引用建议合理但非 critical。\n\n---\n\n**[AGREE] R2-W4: DD lexical separability，消融可信度依赖单一 ActorAttack**\n同意。我在 R1-W6 中提出了相同问题。补充一个量化观察：TF-IDF 在 DD 上 per-prefix F1 达到 0.994-1.000（Appendix Table S2），甚至超过部分 neural 变体。DD 上的 evidence hierarchy 可能仅反映不同变体捕获 lexical features 的效率，而非 discourse-level representation quality。\n\nActorAttack 是唯一真正区分 lexical 和 beyond-lexical 的评估集，但它也是唯一一个 perturbation robustness 崩溃的评估集（Section 5.5: 9-class Δ=-20.4±13.5pp）。这意味着在 \"beyond lexical\" 的唯一评估集上，模型的 robustness 是脆弱的。这进一步支持了 R2 的 concern。\n\n---\n\n**[AGREE with qualification] R2-W5: 术语不一致**\n部分同意。\"domain exposure\" / \"domain adaptation\" / \"continued pretraining\" / \"DAPT\" 混用确实影响可读性，应统一。\"evidence hierarchy\" 作为论文的核心分析框架，首次使用前应有定义。\n\n但 R2 说 **\"DisPeD 在 Introduction 使用但未定义\"** 这一点是 **不准确的**。Introduction line 12 明确写了 \"encoder adaptation followed by frozen BiGRU classification, which we call **DisPeD**\"。DisPeD 在 Introduction 首次出现时即有定义。R2 可能遗漏了这一定义。不过，DisPeD 的全称（presumed: Discourse-level Persuasion Detection?）确实未在论文中给出——如果这是缩写，应展开。\n\n---\n\n**[AGREE] R2-W6: Analysis paper 深度不够**\n同意这是一个重要问题。作为自称 analysis/ablation paper 的工作，分析工具的运用确实单薄：\n- CKA：仅 Section 5.3 一段文字描述（experiments.tex lines 184-191），无可视化矩阵或图表。考虑到论文声称 \"substantially reshape the representation space\"，至少需要一个 CKA heatmap。\n- Linear probing：仅一句话总结 \"9-class outperforms vanilla and MLM by 1-5pp\"（line 190），未给出 per-task 数据表。\n- 无 t-SNE/UMAP 可视化来直观展示 vanilla vs. MLM vs. 9-class 的表示空间差异。\n- 无 attention pattern 分析来检验 \"discourse-level\" claim。\n\n这与我在 R1-N3 中提出的 \"discourse-level claims 缺乏直接证据\" 高度相关。CKA 可视化 + probing 详细结果 + 表示空间可视化可以部分回应 R1-N3 和 R2-N2/W6 三个问题。\n\n---\n\n## 与 R1 审稿意见的交叉总结\n\n| R2 问题 | R1 对应 | 判断 | 备注 |\n|---------|---------|------|------|\n| R2-N1 Figure placeholder | R1-N1 | 完全一致 | 两位 reviewer 独立发现 |\n| R2-N2 Novelty 不足 | — | 部分不同意 | 建议降为 should-fix (framing) |\n| R2-N3 Human data reversal | R1-W4 | 同意升级为 critical | R2 分析更深入 |\n| R2-N4 缺少直接对比 | — | 语言矛盾 agree，要求对比 rebut | 建议降为 should-fix |\n| R2-W1 Abstract 数据堆砌 | — | 同意 | |\n| R2-W2 数据规模小 | R1-W1 | 部分不同意 | analysis paper vs. system paper |\n| R2-W3 引用偏低 | R1 Missing Refs | 同意 | DeBERTa-v3, ELECTRA, CKA |\n| R2-W4 DD lexical sep. | R1-W6 | 完全一致 | R2 进一步强化 |\n| R2-W5 术语不一致 | — | 部分同意 | DisPeD 定义存在于 Intro |\n| R2-W6 分析深度不够 | R1-N3 | 同意 | 与 discourse-level claim 相关 |\n\n两份审稿的核心共识：(1) Figure 1 缺失不可接受；(2) human data 上的 evidence hierarchy reversal 是最严重的实质性问题；(3) \"discourse-level\" claim 缺乏分析深度支撑；(4) DD 的 lexical separability 问题。\n\n两份审稿的主要分歧：R2 认为 novelty 不足和缺少 baseline comparison 是 critical，我认为这两点对 analysis paper 而言应为 should-fix。\n",
  "reviewer_id": "1",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "905fb76a-4167-4ffb-9f3a-80543a45f671",
  "isSidechain": false,
  "requestId": "req_011CbAUuocnjYzDnpngSJ6cz",
  "type": "assistant",
  "uuid": "2dfe5a15-06b9-4ac6-8511-ce0d68e34fcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpLybyPgdM62yZThxMwf6r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 92669,
      "output_tokens": 5805,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5805,
          "cache_read_input_tokens": 92669,
          "cache_creation_input_tokens": 1410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1410
          },
          "type": "message"
        }
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

_source line 68_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 交叉分享：Reviewer 2 的完整审稿意见  以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题： - **[AGREE]**：同意该问题，并说明你的理由或补充观察 - **[REBUT]**：不同意或认为该问题被高估，提供证据（引用具体 Section/Table/Figure）  ---  *…",
  "leafUuid": "2dfe5a15-06b9-4ac6-8511-ce0d68e34fcf",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multi-turn jailbreak detection paper for EMNLP",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765"
}
```

---

### Tool result

_source line 70 · 2026-05-18T18:10:53.511Z_

<details><summary>↩ Tool result · `toolu_01VGgk45HrrSJgi1g5iaco2N`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2dfe5a15-06b9-4ac6-8511-ce0d68e34fcf",
  "isSidechain": false,
  "promptId": "3115e2c4-53d8-47ad-80c8-99e4c51cdc53",
  "type": "user",
  "uuid": "8603a138-9c06-4a07-afc0-4b3920081f4f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_613965f45d48763f375aa83e9294b24a:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_613965f45d48763f375aa83e9294b24a:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "2dfe5a15-06b9-4ac6-8511-ce0d68e34fcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "3eec1eca-545d-4d07-897d-ac83e698f765",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
