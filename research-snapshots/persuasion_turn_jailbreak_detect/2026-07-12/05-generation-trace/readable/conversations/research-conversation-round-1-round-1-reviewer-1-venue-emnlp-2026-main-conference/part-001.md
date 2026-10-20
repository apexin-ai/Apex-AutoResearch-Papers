# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1 **你的审查侧重：方法严谨性 + 实验有效性** ### Venue 信息 - **目标会议**：EMNLP 2026 Main Conference — Part 1 of 2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-round-1-round-1-reviewer-1-venue-emnlp-2026-main-conference.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/38/38d18188089722eb7e70.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-18T08:39:44.217Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T08:39:44.217Z",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "content": "[Round 1 审稿请求]:\n## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验有效性**\n\n### Venue 信息\n- **目标会议**：EMNLP 2026 Main Conference (ARR May cycle)\n- **截止日期**：2026-05-25\n- **页数限制**：长文 8 页（不含 references、limitations、ethics）\n- **模板**：ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**：Double-blind review\n\n### 论文路径\n- 主文件：`projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex`\n- 各章节：`abstract.tex`, `introduction.tex`, `related_work.tex`, `method.tex`, `experiments.tex`, `conclusion.tex`, `appendix.tex`\n- 引用：`references.bib`\n- 图片：`figures/paper/fig1_architecture.pdf`, `fig2_cross_attack_bar.pdf`, `fig3_strategy_heatmap.pdf`\n\n### 审查要求\n\n请重点评估以下方面，给出逐条意见：\n\n1. **实验设计严谨性**\n   - 7 个 Stage-1 变体的消融设计是否真正隔离了声称的因素？是否存在混淆变量？\n   - 控制变量是否充分？（同一训练数据、同一 Stage-2 pipeline、同一超参）\n   - 数据集规模（500 训练、160 OOD 测试）是否足以支撑论文的 claims？\n\n2. **统计显著性与可靠性**\n   - 3-seed 报告 vs 单 seed 报告的不一致（binary/scrambled 仅 seed 42）——这是否削弱了关键比较？\n   - perturbation robustness 的样本量（n=76）是否足够？论文承认 tier boundaries = 1-3 misclassifications，这多大程度上削弱了 three-layer attribution 的可信度？\n   - MLM 的高方差（0.91±0.12）是否充分讨论？\n\n3. **方法论问题**\n   - 策略标注由 Qwen3-8B 生成（Cohen's κ=0.78, n=50），这个标注质量是否足够？人工标注样本量是否太小？\n   - Stage-1 冻结后进入 Stage-2，这个设计选择的合理性？为什么不 end-to-end fine-tune？\n   - Mean pooling = BiGRU 的结论（仅 single seed）是否过强？\n\n4. **Baseline 充分性**\n   - 缺少与 DeepContext (F1=0.84)、BIID、G-Guard、SafeDream 的直接实验对比\n   - LLM-as-judge baseline 仅测 IID（Crescendo），未测 OOD\n   - TF-IDF LR 达 0.944 on DD，与 9-class 的差距是否足以证明复杂模型的必要性？\n\n5. **可复现性**\n   - 超参报告是否完整？\n   - 数据生成过程（Qwen3-8B 生成对话）是否有足够细节？\n   - 代码/数据是否承诺开源？\n\n请按 EMNLP 标准给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Score (1-5)。"
}
```

---


### Runtime record

_source line 2 · 2026-05-18T08:39:44.221Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T08:39:44.221Z",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


## Round 1

## Round 1

87 recorded events


### User

_source line 3 · 2026-05-18T08:39:44.261Z_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验有效性**

### Venue 信息
- **目标会议**：EMNLP 2026 Main Conference (ARR May cycle)
- **截止日期**：2026-05-25
- **页数限制**：长文 8 页（不含 references、limitations、ethics）
- **模板**：ACL format (`\usepackage[review]{acl}`)
- **匿名规则**：Double-blind review

### 论文路径
- 主文件：`projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex`
- 各章节：`abstract.tex`, `introduction.tex`, `related_work.tex`, `method.tex`, `experiments.tex`, `conclusion.tex`, `appendix.tex`
- 引用：`references.bib`
- 图片：`figures/paper/fig1_architecture.pdf`, `fig2_cross_attack_bar.pdf`, `fig3_strategy_heatmap.pdf`

### 审查要求

请重点评估以下方面，给出逐条意见：

1. **实验设计严谨性**
   - 7 个 Stage-1 变体的消融设计是否真正隔离了声称的因素？是否存在混淆变量？
   - 控制变量是否充分？（同一训练数据、同一 Stage-2 pipeline、同一超参）
   - 数据集规模（500 训练、160 OOD 测试）是否足以支撑论文的 claims？

2. **统计显著性与可靠性**
   - 3-seed 报告 vs 单 seed 报告的不一致（binary/scrambled 仅 seed 42）——这是否削弱了关键比较？
   - perturbation robustness 的样本量（n=76）是否足够？论文承认 tier boundaries = 1-3 misclassifications，这多大程度上削弱了 three-layer attribution 的可信度？
   - MLM 的高方差（0.91±0.12）是否充分讨论？

3. **方法论问题**
   - 策略标注由 Qwen3-8B 生成（Cohen's κ=0.78, n=50），这个标注质量是否足够？人工标注样本量是否太小？
   - Stage-1 冻结后进入 Stage-2，这个设计选择的合理性？为什么不 end-to-end fine-tune？
   - Mean pooling = BiGRU 的结论（仅 single seed）是否过强？

4. **Baseline 充分性**
   - 缺少与 DeepContext (F1=0.84)、BIID、G-Guard、SafeDream 的直接实验对比
   - LLM-as-judge baseline 仅测 IID（Crescendo），未测 OOD
   - TF-IDF LR 达 0.944 on DD，与 9-class 的差距是否足以证明复杂模型的必要性？

5. **可复现性**
   - 超参报告是否完整？
   - 数据生成过程（Qwen3-8B 生成对话）是否有足够细节？
   - 代码/数据是否承诺开源？

请按 EMNLP 标准给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Score (1-5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "45590385-c4b5-4fae-b278-c2c700a52662",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-18T08:39:44.261Z_

```json
{
  "parentUuid": "45590385-c4b5-4fae-b278-c2c700a52662",
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
  "uuid": "5a44a74e-854a-4ba6-bb00-2f82b7e1e61f",
  "timestamp": "2026-05-18T08:39:44.261Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 5 · 2026-05-18T08:39:44.261Z_

```json
{
  "parentUuid": "5a44a74e-854a-4ba6-bb00-2f82b7e1e61f",
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
  "uuid": "834cf46d-2598-4d17-b4b8-8f82497c5fe7",
  "timestamp": "2026-05-18T08:39:44.261Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 6 · 2026-05-18T08:39:44.261Z_

```json
{
  "parentUuid": "834cf46d-2598-4d17-b4b8-8f82497c5fe7",
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
  "uuid": "db42dd75-f77c-4f87-aecb-07dfe46d4b88",
  "timestamp": "2026-05-18T08:39:44.261Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 7 · 2026-05-18T08:39:44.261Z_

```json
{
  "parentUuid": "db42dd75-f77c-4f87-aecb-07dfe46d4b88",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2b18f15e-2591-4af2-b687-d61387b8e512",
  "timestamp": "2026-05-18T08:39:44.261Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
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
  "aiTitle": "Round 1 paper review for EMNLP persuasion jailbreak detection",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Assistant

_source line 9 · 2026-05-18T08:39:48.396Z_

我先执行 session 启动初始化，然后开始审稿。

Let me start by reading the paper and searching for the EMNLP/ARR reviewer guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b18f15e-2591-4af2-b687-d61387b8e512",
  "isSidechain": false,
  "requestId": "req_011Cb9jWL4h8SHTr1yEbTJdt",
  "type": "assistant",
  "uuid": "e5dc71ab-f36b-425c-a80b-f4c7d4f4f740",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016doEnGJTcyRxwW4nzhHBS3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15793,
      "cache_read_input_tokens": 11447,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15793,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 172,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 15793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15793
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-18T08:39:49.286Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NusrMUhVH8URst7gQUcL3J`</summary>

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
  "parentUuid": "e5dc71ab-f36b-425c-a80b-f4c7d4f4f740",
  "isSidechain": false,
  "requestId": "req_011Cb9jWL4h8SHTr1yEbTJdt",
  "type": "assistant",
  "uuid": "8faa13c6-f208-4ba3-b44b-54d1d6c665dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016doEnGJTcyRxwW4nzhHBS3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15793,
      "cache_read_input_tokens": 11447,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15793,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 172,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 15793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15793
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-18T08:39:49.294Z_

<details><summary>↩ Tool result · `toolu_01NusrMUhVH8URst7gQUcL3J`</summary>

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
  "parentUuid": "8faa13c6-f208-4ba3-b44b-54d1d6c665dd",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "7eab1145-21c2-4530-845d-938a60b0cbae",
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
  "sourceToolAssistantUUID": "8faa13c6-f208-4ba3-b44b-54d1d6c665dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 12 · 2026-05-18T08:39:51.734Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the paper and searching for EMNLP/ARR reviewer guidelines in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7eab1145-21c2-4530-845d-938a60b0cbae",
  "isSidechain": false,
  "requestId": "req_011Cb9jWhY24WCyM4onk8GCN",
  "type": "assistant",
  "uuid": "27a6563c-b285-4dfd-aa42-fa081020ed12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDm1vi3t86fM5jXf7fi6qR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 27240,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2169,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 199,
          "cache_read_input_tokens": 27240,
          "cache_creation_input_tokens": 2169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2169
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-18T08:39:52.584Z_

开始读论文并搜索 ARR reviewer guidelines。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27a6563c-b285-4dfd-aa42-fa081020ed12",
  "isSidechain": false,
  "requestId": "req_011Cb9jWhY24WCyM4onk8GCN",
  "type": "assistant",
  "uuid": "778d4e4f-85b9-4cd7-9708-d1ea7a6f88d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDm1vi3t86fM5jXf7fi6qR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 27240,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2169,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 199,
          "cache_read_input_tokens": 27240,
          "cache_creation_input_tokens": 2169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2169
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-18T08:39:53.152Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BbrSbnPiURZGSpzKJCStwf`</summary>

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
  "parentUuid": "778d4e4f-85b9-4cd7-9708-d1ea7a6f88d5",
  "isSidechain": false,
  "requestId": "req_011Cb9jWhY24WCyM4onk8GCN",
  "type": "assistant",
  "uuid": "124bd278-148b-4ce9-87da-04d683c88815",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDm1vi3t86fM5jXf7fi6qR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 27240,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2169,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 199,
          "cache_read_input_tokens": 27240,
          "cache_creation_input_tokens": 2169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2169
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-18T08:39:54.234Z_

<details><summary>↩ Tool result · `toolu_01DJhdtqaN7odwGSuUobwd5f`</summary>

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
  "parentUuid": "55f27dea-e0fe-4d35-8b93-1f3e79af7c1b",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "0e555156-f2ea-41fd-bae8-b2435c58f4de",
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
  "sourceToolAssistantUUID": "55f27dea-e0fe-4d35-8b93-1f3e79af7c1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-18T08:39:54.225Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DJhdtqaN7odwGSuUobwd5f`</summary>

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
  "parentUuid": "124bd278-148b-4ce9-87da-04d683c88815",
  "isSidechain": false,
  "requestId": "req_011Cb9jWhY24WCyM4onk8GCN",
  "type": "assistant",
  "uuid": "55f27dea-e0fe-4d35-8b93-1f3e79af7c1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDm1vi3t86fM5jXf7fi6qR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 27240,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2169,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 199,
          "cache_read_input_tokens": 27240,
          "cache_creation_input_tokens": 2169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2169
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-18T08:40:01.498Z_

<details><summary>↩ Tool result · `toolu_01BbrSbnPiURZGSpzKJCStwf`</summary>

```text
Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) reviewer guidelines, review form criteria, and scoring for 2025-2026:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Recommendation Score Options

The review form includes the following recommendation score options:

- Consider for award: If your overall assessment for this paper is either 'Consider for award' or 'Borderline award', please briefly describe why.
- Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle.
- Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle.
- Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language).

## Review Criteria

The review form evaluates papers on several criteria including:
- Limitations and societal impacts: Have the authors adequately discussed the limitations and potential positive and negative societal impacts of their work? If not, please include constructive suggestions for improvement.
- Ethical issues: If there are ethical issues with this paper, please describe them and the extent to which they have been acknowledged or addressed by the authors. Should this paper be sent for an in-depth ethics review?
- Reproducibility: Is there enough information in this paper for a reader to reproduce the main results, use results presented in this paper in future work (e.g., as a baseline), or build upon this work?

## General Reviewing Principles

ARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "124bd278-148b-4ce9-87da-04d683c88815",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "2c2b65cd-3468-46ea-b56d-09db94925324",
  "toolUseResult": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_016vgAYALtr69BDVbftBe4Cz",
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
      "Based on the search results, here's information about the ACL Rolling Review (ARR) reviewer guidelines, review form criteria, and scoring for 2025-2026:\n\n## Reviewer Scoring System\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.\n\n## Overall Recommendation Score Options\n\nThe review form includes the following recommendation score options:\n\n- Consider for award: If your overall assessment for this paper is either 'Consider for award' or 'Borderline award', please briefly describe why.\n- Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle.\n- Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle.\n- Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language).\n\n## Review Criteria\n\nThe review form evaluates papers on several criteria including:\n- Limitations and societal impacts: Have the authors adequately discussed the limitations and potential positive and negative societal impacts of their work? If not, please include constructive suggestions for improvement.\n- Ethical issues: If there are ethical issues with this paper, please describe them and the extent to which they have been acknowledged or addressed by the authors. Should this paper be sent for an in-depth ethics review?\n- Reproducibility: Is there enough information in this paper for a reader to reproduce the main results, use results presented in this paper in future work (e.g., as a baseline), or build upon this work?\n\n## General Reviewing Principles\n\nARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference."
    ],
    "durationSeconds": 8.340890555000001
  },
  "sourceToolAssistantUUID": "124bd278-148b-4ce9-87da-04d683c88815",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验有效性**  ### Venue 信息 - **目标会议**：EMNLP 2026 Main Conference (ARR May cycle) - **截止日期**：2026-05-25 - **页数限制**：长文 8 页（不含 references、limitat…",
  "leafUuid": "2c2b65cd-3468-46ea-b56d-09db94925324",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 paper review for EMNLP persuasion jailbreak detection",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Tool call

_source line 20 · 2026-05-18T08:40:05.214Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UiNRv55QFiJkmSEmg8kP7Y`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scale (1-5), and descriptions. I need the exact scoring criteria for soundness, excitement, overall recommendation, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c2b65cd-3468-46ea-b56d-09db94925324",
  "isSidechain": false,
  "requestId": "req_011Cb9jXc9MTxTETLsXH3HuS",
  "type": "assistant",
  "uuid": "f07d7c3b-e45f-4570-a568-ccbb83081332",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSfSHLzU6USjLd5Pof5dCm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 371,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 29409,
      "output_tokens": 732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1142,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 371,
          "output_tokens": 732,
          "cache_read_input_tokens": 29409,
          "cache_creation_input_tokens": 1142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1142
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-18T08:40:06.199Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y2rb8Ze9ycbxTTs2aY878S`</summary>

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
  "parentUuid": "f07d7c3b-e45f-4570-a568-ccbb83081332",
  "isSidechain": false,
  "requestId": "req_011Cb9jXc9MTxTETLsXH3HuS",
  "type": "assistant",
  "uuid": "94aa4e95-2516-4bfa-8755-e8fe789c9ad6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSfSHLzU6USjLd5Pof5dCm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 371,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 29409,
      "output_tokens": 732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1142,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 371,
          "output_tokens": 732,
          "cache_read_input_tokens": 29409,
          "cache_creation_input_tokens": 1142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1142
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-18T08:40:06.212Z_

<details><summary>↩ Tool result · `toolu_01Y2rb8Ze9ycbxTTs2aY878S`</summary>

```text
1	% abstract.tex — D024 compressed
2	\begin{abstract}
3	Multi-turn jailbreak attacks against Large Language Models (LLMs) distribute adversarial intent across seemingly benign conversational turns, evading per-turn safety filters.
4	Standard temporal classifiers fail to generalize: a vanilla DeBERTa encoder achieves only F1\,=\,0.28 on out-of-distribution (OOD) attack types.
5	We design seven controlled variants of a DeBERTa-based detection framework to decompose what enables cross-attack generalization.
6	Masked language modeling (MLM) continued pretraining, without any classification labels, achieves near-perfect early detection on unseen attacks (mean F1\,$\geq$\,0.97 at $K\leq 5$ turns) but shows instability at full conversation length (F1\,=\,0.91$\pm$0.12).
7	Any continued pretraining bridges most of the OOD gap (vanilla 0.28 $\to$ $\sim$0.91); jailbreak-domain text improves early detection ($K$=2: 8 percentage point advantage over Wikipedia MLM).
8	Misaligned supervision yields unstable generalization (topic F1\,=\,0.54$\pm$0.21, worst seed below vanilla).
9	The 9-class persuasion model achieves the highest F1 (0.997$\pm$0.005), and classification supervision further contributes stability, perturbation robustness (zero degradation at full length for all classification-supervised variants; correct fine-grained labels add early-turn robustness, $n$=76), and interpretability through strategy trajectories.
10	These results reframe multi-turn jailbreak detection as primarily a domain adaptation problem, with classification supervision providing complementary stability, robustness, and interpretability.
11	\end{abstract}
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94aa4e95-2516-4bfa-8755-e8fe789c9ad6",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "ee7ef2cf-585f-4545-9965-33bdf7942a99",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex",
      "content": "% abstract.tex — D024 compressed\n\\begin{abstract}\nMulti-turn jailbreak attacks against Large Language Models (LLMs) distribute adversarial intent across seemingly benign conversational turns, evading per-turn safety filters.\nStandard temporal classifiers fail to generalize: a vanilla DeBERTa encoder achieves only F1\\,=\\,0.28 on out-of-distribution (OOD) attack types.\nWe design seven controlled variants of a DeBERTa-based detection framework to decompose what enables cross-attack generalization.\nMasked language modeling (MLM) continued pretraining, without any classification labels, achieves near-perfect early detection on unseen attacks (mean F1\\,$\\geq$\\,0.97 at $K\\leq 5$ turns) but shows instability at full conversation length (F1\\,=\\,0.91$\\pm$0.12).\nAny continued pretraining bridges most of the OOD gap (vanilla 0.28 $\\to$ $\\sim$0.91); jailbreak-domain text improves early detection ($K$=2: 8 percentage point advantage over Wikipedia MLM).\nMisaligned supervision yields unstable generalization (topic F1\\,=\\,0.54$\\pm$0.21, worst seed below vanilla).\nThe 9-class persuasion model achieves the highest F1 (0.997$\\pm$0.005), and classification supervision further contributes stability, perturbation robustness (zero degradation at full length for all classification-supervised variants; correct fine-grained labels add early-turn robustness, $n$=76), and interpretability through strategy trajectories.\nThese results reframe multi-turn jailbreak detection as primarily a domain adaptation problem, with classification supervision providing complementary stability, robustness, and interpretability.\n\\end{abstract}\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  },
  "sourceToolAssistantUUID": "94aa4e95-2516-4bfa-8755-e8fe789c9ad6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-18T08:40:09.881Z_

<details><summary>↩ Tool result · `toolu_01CsAGbZdqGBw5Z9bNXovsZb`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a033cf21-534a-47ce-b32a-07d445155d37",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "2a36d0c0-7eae-4c37-a8a2-a8bb2cd21239",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/references.bib",
      "content": "% References for persuasion_turn_jailbreak_detect\n% Auto-generated from literature_map.yaml (2026-05-18)\n% Total entries: 31\n\n% ============================================================\n% Category 1: Production Multi-Turn Safety Systems\n% ============================================================\n\n@article{inan2023llamaguard,\n  title={Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations},\n  author={Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer, Krithika and Mao, Yuning and Tontchev, Michael and Hu, Qing and Fuller, Brian and Testuggine, Davide and Khabsa, Madian},\n  journal={arXiv preprint},\n  year={2023},\n  eprint={2312.06674},\n  archivePrefix={arXiv},\n}\n\n@misc{metallamaguard3_2024,\n  title={Llama Guard 3},\n  author={{Meta AI}},\n  year={2024},\n  howpublished={Meta AI (released with Llama 3.1)},\n}\n\n@article{zeng2024shieldgemma,\n  title={ShieldGemma: Generative AI Content Moderation Based on Gemma},\n  author={Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, Joe and Harkous, Hamza and Narasimhan, Karthik and Proud, Drew and Kumar, Piyush and Radharapu, Bhaktipriya and Sturman, Olivia and Wahltinez, Oscar},\n  journal={arXiv preprint},\n  year={2024},\n  eprint={2407.21772},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{han2024wildguard,\n  title={WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs},\n  author={Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill Yuchen and Lambert, Nathan and Choi, Yejin and Dziri, Nouha},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2024},\n}\n\n@article{anthropic2025constitutional,\n  title={Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming},\n  author={{Anthropic}},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2501.18837},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 2: Multi-Turn Jailbreak Defenses\n% ============================================================\n\n@article{deepcontext2026,\n  title={DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs},\n  author={Albrethsen, Justin and Datta, Yash and Kumar, Kunal and Rajasekar, Sharath},\n  journal={arXiv preprint},\n  year={2026},\n  eprint={2602.16935},\n  archivePrefix={arXiv},\n}\n\n@article{tong2025biid,\n  title={Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks},\n  author={Tong, Haibo and Zhao, Dongcheng and Shen, Guobin and He, Xiang and Lin, Dachuan and Zhao, Feifei and Zeng, Yi},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2509.22732},\n  archivePrefix={arXiv},\n}\n\n@article{gguard2025,\n  title={An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs},\n  author={Huang, Zixuan and Huang, Kecheng and Yin, Lihao and He, Bowei and Zhen, Huiling and Yuan, Mingxuan and Shao, Zili},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2507.07146},\n  archivePrefix={arXiv},\n}\n\n@article{safedream2026,\n  title={SafeDream: Safety World Model for Proactive Early Jailbreak Detection},\n  author={Yan, Bo and Lin, Weikai and Zhu, Yada and Wang, Song},\n  journal={arXiv preprint},\n  year={2026},\n  eprint={2604.16824},\n  archivePrefix={arXiv},\n}\n\n@article{bullwinkel2025repeng,\n  title={A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks},\n  author={Bullwinkel, Blake and Russinovich, Mark and Salem, Ahmed and Zanella-Beguelin, Santiago and Jones, Daniel and Severi, Giorgio and Kim, Eugenia and Hines, Keegan and Minnich, Amanda and Zunger, Yonatan and Kumar, Ram Shankar Siva},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2507.02956},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 3: Discourse Analysis in NLP\n% ============================================================\n\n@article{mann1988rst,\n  title={Rhetorical Structure Theory: Toward a Functional Theory of Text Organization},\n  author={Mann, William C. and Thompson, Sandra A.},\n  journal={Text \\& Talk},\n  year={1988},\n  volume={8},\n  number={3},\n  pages={243--281},\n}\n\n@inproceedings{prasad2008pdtb,\n  title={The Penn Discourse TreeBank 2.0},\n  author={Prasad, Rashmi and Dinesh, Nikhil and Lee, Alan and Miltsakaki, Eleni and Robaldo, Livio and Joshi, Aravind and Webber, Bonnie},\n  booktitle={Proceedings of the International Conference on Language Resources and Evaluation},\n  year={2008},\n}\n\n@article{stolcke2000dialogueact,\n  title={Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech},\n  author={Stolcke, Andreas and Ries, Klaus and Coccaro, Noah and Shriberg, Elizabeth and Bates, Rebecca and Jurafsky, Daniel and Taylor, Paul and Martin, Rachel and Van Ess-Dykema, Carol and Meteer, Marie},\n  journal={Computational Linguistics},\n  year={2000},\n  volume={26},\n  number={3},\n  pages={339--374},\n}\n\n@book{austin1962speechacts,\n  title={How to Do Things with Words},\n  author={Austin, J. L.},\n  publisher={Harvard University Press},\n  year={1962},\n}\n\n@book{searle1969speechacts,\n  title={Speech Acts: An Essay in the Philosophy of Language},\n  author={Searle, J. R.},\n  publisher={Cambridge University Press},\n  year={1969},\n}\n\n% ============================================================\n% Category 4: Computational Persuasion Detection\n% ============================================================\n\n@book{cialdini2001influence,\n  title={Influence: Science and Practice},\n  author={Cialdini, Robert B.},\n  publisher={Allyn \\& Bacon},\n  year={2001},\n  edition={4th},\n}\n\n% ============================================================\n% Category 5: Jailbreak Attacks & Taxonomies\n% ============================================================\n\n@inproceedings{zeng2024pap,\n  title={How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs},\n  author={Zeng, Yi and Lin, Hongpeng and Zhang, Jingwen and Yang, Diyi and Jia, Ruoxi and Shi, Weiyan},\n  booktitle={Proceedings of the Association for Computational Linguistics},\n  year={2024},\n}\n\n% Note: key retains \"2024\" for citation compatibility; paper published at USENIX Security 2025\n@inproceedings{russinovich2024crescendo,\n  title={Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack},\n  author={Russinovich, Mark and Salem, Ahmed and Eldan, Ronen},\n  booktitle={USENIX Security Symposium},\n  year={2025},\n  eprint={2404.01833},\n  archivePrefix={arXiv},\n}\n\n@article{chao2023pair,\n  title={Jailbreaking Black Box Large Language Models in Twenty Queries},\n  author={Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pappas, George J. and Wong, Eric},\n  journal={arXiv preprint},\n  year={2023},\n  eprint={2310.08419},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{wei2023jailbroken,\n  title={Jailbroken: How Does LLM Safety Training Fail?},\n  author={Wei, Alexander and Haghtalab, Nika and Steinhardt, Jacob},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023},\n}\n\n@article{hagendorff2026reasoning,\n  title={Large Reasoning Models Are Autonomous Jailbreak Agents},\n  author={Hagendorff, Thilo and Derner, Erik and Oliver, Nuria},\n  journal={Nature Communications},\n  year={2026},\n}\n\n@article{fitd2024,\n  title={Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology},\n  author={Wang, Zhenhua and Xie, Wei and Wang, Baosheng and Wang, Enze and Gui, Zhiwen and Ma, Shuoyoucheng and Chen, Kai},\n  journal={arXiv preprint},\n  year={2024},\n  eprint={2402.15690},\n  archivePrefix={arXiv},\n}\n\n@techreport{deceptivedelight2024,\n  title={Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction},\n  author={{Palo Alto Networks Unit 42}},\n  institution={Palo Alto Networks},\n  year={2024},\n}\n\n@inproceedings{ren2024actorattack,\n  title={ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory},\n  author={Ren, Qibing and Li, Hao and Liu, Dongrui and Xie, Zhanxu and Lu, Xiaoya and Qiao, Yu and Sha, Lei and Yan, Junchi and Ma, Lizhuang and Shao, Jing},\n  booktitle={International Conference on Learning Representations},\n  year={2025},\n}\n\n@article{zou2023gcg,\n  title={Universal and Transferable Adversarial Attacks on Aligned Language Models},\n  author={Zou, Andy and Wang, Zifan and Carlini, Nicholas and Nasr, Milad and Kolter, J. Zico and Fredrikson, Matt},\n  journal={arXiv preprint},\n  year={2023},\n  eprint={2307.15043},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 6: Red-Teaming\n% ============================================================\n\n@article{li2024mhj,\n  title={LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet},\n  author={Li, Nathaniel and Han, Ziwen and Steneker, Ian and Primack, Willow and Goodside, Riley and Zhang, Hugh and Wang, Zifan and Menghini, Cristina and Yue, Summer},\n  journal={arXiv preprint},\n  year={2024},\n  eprint={2408.15221},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 7: Annotation Artifacts & Dataset Biases\n% ============================================================\n\n@inproceedings{gururangan2018artifacts,\n  title={Annotation Artifacts in Natural Language Inference Data},\n  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel and Smith, Noah A.},\n  booktitle={Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics},\n  year={2018},\n}\n\n@inproceedings{niven2019probing,\n  title={Probing Neural Network Comprehension of Natural Language Arguments},\n  author={Niven, Timothy and Kao, Hung-Yu},\n  booktitle={Proceedings of the Association for Computational Linguistics},\n  year={2019},\n}\n\n% ============================================================\n% Category 8: Adaptive Attacks on Classifiers\n% ============================================================\n\n@article{nasr2025attackermovessecond,\n  title={The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections},\n  author={Nasr, Milad and Carlini, Nicholas and Sitawarin, Chawin and Schulhoff, Sander V. and Hayes, Jamie and Ilie, Michael and Pluto, Juliette and Song, Shuang and Chaudhari, Harsh and Shumailov, Ilia and Thakurta, Abhradeep and Xiao, Kai Yuanqing and Terzis, Andreas and Tram{\\`e}r, Florian},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2510.09023},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{andriushchenko2024adaptive,\n  title={Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks},\n  author={Andriushchenko, Maksym and Croce, Francesco and Flammarion, Nicolas},\n  booktitle={International Conference on Learning Representations},\n  year={2025},\n}\n\n% ============================================================\n% Technical Foundation\n% ============================================================\n\n@inproceedings{he2021deberta,\n  title={DeBERTa: Decoding-enhanced BERT with Disentangled Attention},\n  author={He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu},\n  booktitle={International Conference on Learning Representations},\n  year={2021},\n}\n\n% ============================================================\n% Domain-Adaptive Pretraining & Multi-Task Learning\n% ============================================================\n\n@inproceedings{gururangan2020dontstop,\n  title={Don't Stop Pretraining: Adapt Language Models to Domains and Tasks},\n  author={Gururangan, Suchin and Marasovi{\\'c}, Ana and Swayamdipta, Swabha and Lo, Kyle and Beltagy, Iz and Downey, Doug and Smith, Noah A.},\n  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n  pages={8342--8360},\n  year={2020},\n}\n\n@article{caruana1997multitask,\n  title={Multitask Learning},\n  author={Caruana, Rich},\n  journal={Machine Learning},\n  volume={28},\n  number={1},\n  pages={41--75},\n  year={1997},\n}\n\n@article{phang2018stilts,\n  title={Sentence Encoders on {STILTs}: Supplementary Training on Intermediate Labeled-data Tasks},\n  author={Phang, Jason and F{\\'e}vry, Thibault and Bowman, Samuel R.},\n  journal={arXiv preprint arXiv:1811.01088},\n  year={2018},\n}\n\n@inproceedings{liu2019mtdnn,\n  title={Multi-Task Deep Neural Networks for Natural Language Understanding},\n  author={Liu, Xiaodong and He, Pengcheng and Chen, Weizhu and Gao, Jianfeng},\n  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n  pages={4487--4496},\n  year={2019},\n}\n\n@inproceedings{howard2018ulmfit,\n  title={Universal Language Model Fine-tuning for Text Classification},\n  author={Howard, Jeremy and Ruder, Sebastian},\n  booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n  pages={328--339},\n  year={2018},\n}\n",
      "numLines": 338,
      "startLine": 1,
      "totalLines": 338
    }
  },
  "sourceToolAssistantUUID": "a033cf21-534a-47ce-b32a-07d445155d37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-18T08:40:06.700Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YbFBpsyFvHXa9zYYGXFF6R`</summary>

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
  "parentUuid": "ee7ef2cf-585f-4545-9965-33bdf7942a99",
  "isSidechain": false,
  "requestId": "req_011Cb9jXc9MTxTETLsXH3HuS",
  "type": "assistant",
  "uuid": "ba7a65ca-3c46-4b73-a765-173b6c4c030e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSfSHLzU6USjLd5Pof5dCm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 371,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 29409,
      "output_tokens": 732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1142,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 371,
          "output_tokens": 732,
          "cache_read_input_tokens": 29409,
          "cache_creation_input_tokens": 1142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1142
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-18T08:40:06.709Z_

<details><summary>↩ Tool result · `toolu_01YbFBpsyFvHXa9zYYGXFF6R`</summary>

```text
1	% introduction.tex — expanded for 8-page target
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Multi-turn jailbreak attacks pose a qualitatively different threat to large language model (LLM) safety than their single-turn counterparts. Attacks such as Crescendo~\citep{russinovich2024crescendo}, Foot-in-the-Door (FITD)~\citep{fitd2024}, and Deceptive Delight~\citep{deceptivedelight2024} distribute adversarial intent across individually benign turns through rapport building, logical reframing, and incremental escalation. Persuasion is the common mechanism: \citet{zeng2024pap} catalogue 40 persuasion techniques across jailbreak families, and \citet{hagendorff2026reasoning} find identifiable strategies in 97\% of successful attacks. Individual attack turns occupy the same embedding region as benign text~\citep{bullwinkel2025repeng}, rendering per-turn safety filters fundamentally blind.
7	
8	Production classifiers such as Llama Guard~\citep{inan2023llamaguard}, WildGuard~\citep{han2024wildguard}, and ShieldGemma~\citep{zeng2024shieldgemma} operate on individual turns and cannot model manipulation trajectories across exchanges. Recent multi-turn defenses have begun to address conversation-level structure: DeepContext~\citep{deepcontext2026} aggregates BERT embeddings with a recurrent network, BIID~\citep{tong2025biid} infers turn-level intentions, and G-Guard~\citep{gguard2025} applies graph neural networks. These systems achieve reasonable in-distribution performance but degrade on unseen attack types, and none systematically analyze \emph{why} some representations generalize while others fail. The open question is: \emph{what representation properties enable cross-attack generalization?}
9	
10	A vanilla DeBERTa encoder~\citep{he2021deberta} with temporal aggregation collapses from F1\,=\,1.000 on in-distribution data to F1\,=\,0.284 on out-of-distribution (OOD) Deceptive Delight, worsening with more turns (0.575 at turn~1 to 0.284 at full conversation). LLM-as-judge approaches fare no better: GPT-5.5 achieves F1 of only 0.191--0.449 on in-distribution detection with 30--47\% unparseable responses (Appendix~\ref{sec:llm_judge}). Content-level reasoning is insufficient for this task.
11	
12	We built \textbf{DisPeD} (Discourse-level Persuasion Detection), a two-stage framework with seven controlled Stage~1 variants that systematically decompose the mechanism: 9-class persuasion strategy classification, binary classification, scrambled labels, MLM only, topic classification, Wikipedia MLM, and vanilla control (Section~\ref{sec:method}). Each variant isolates a specific factor (domain exposure, classification supervision, label quality, label granularity, or domain specificity) while holding all other components constant, enabling causal attribution of detection performance to individual factors.
13	
14	The result \emph{partially falsified} our original hypothesis that persuasion-specific classification is the key ingredient. MLM without labels achieves near-perfect early detection on unseen Deceptive Delight (mean F1\,$\geq$\,0.97 at $K \leq 5$), but shows instability at full conversation length (F1\,=\,0.91$\pm$0.12) while the 9-class model maintains 0.997$\pm$0.005. The evidence hierarchy is:
15	
16	\vspace{2pt}
17	\noindent\hspace{0.5em}{\small vanilla (0.28) $<$ topic (0.54$\pm$0.21) $\ll$ wiki-MLM (0.90$\pm$0.12) $\approx$ jb-MLM (0.91$\pm$0.12) $<$ scrambled (0.99) $\approx$ binary (0.99) $\approx$ 9-class (0.997$\pm$0.005)}
18	\vspace{2pt}
19	
20	\noindent Any continued pretraining bridges the dominant $\sim$62\,pp gap from vanilla. Wikipedia MLM nearly matches jailbreak-domain MLM at full length; the domain advantage is meaningful at early prefixes ($K$=2: 0.993 vs.\ 0.911) and for perturbation robustness. Only the 9-class model achieves F1\,=\,0.997$\pm$0.005 with near-zero variance. This connects to domain-adaptive pretraining~\citep{gururangan2020dontstop}: continued training captures pragmatic features, with classification supervision providing stability that unsupervised pretraining alone does not guarantee.
21	
22	Our contributions:
23	\begin{itemize}[leftmargin=*, itemsep=2pt, topsep=4pt]
24	  \item \textbf{Systematic decomposition of cross-attack generalization.} Seven controlled variants establish that continued pretraining bridges $\sim$62\,pp of the OOD gap; jailbreak-domain text improves early detection ($K$=2: 8\,pp over Wikipedia MLM). Misaligned supervision (topic F1\,=\,0.54$\pm$0.21) destabilizes generalization.
25	
26	  \item \textbf{Classification supervision adds stability, robustness, and interpretability.} Classification-supervised variants achieve F1\,$\geq$\,0.99 with near-zero variance vs.\ MLM 0.91$\pm$0.12. Under perturbation ($n$=76), all classification-supervised variants (including scrambled labels) show zero degradation at full length vs.\ $\sim$12\,pp for non-adapted models. A three-layer robustness attribution emerges: classification structure provides full-length robustness, the combination of correct and fine-grained labels is required at $K$=2 (scrambled = binary = $-$2.6\,pp, neither alone suffices), and both properties contribute independently at $K$=1 (9-class $-$2.6\,pp vs.\ scrambled $-$5.3\,pp vs.\ binary $-$9.2\,pp). The persuasion taxonomy additionally provides distinct strategy trajectories per attack type (Section~\ref{sec:strategy}).
27	\end{itemize}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba7a65ca-3c46-4b73-a765-173b6c4c030e",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "cca7a8ba-2502-4ebd-83fb-f397ecabe33a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex",
      "content": "% introduction.tex — expanded for 8-page target\n\n\\section{Introduction}\n\\label{sec:introduction}\n\nMulti-turn jailbreak attacks pose a qualitatively different threat to large language model (LLM) safety than their single-turn counterparts. Attacks such as Crescendo~\\citep{russinovich2024crescendo}, Foot-in-the-Door (FITD)~\\citep{fitd2024}, and Deceptive Delight~\\citep{deceptivedelight2024} distribute adversarial intent across individually benign turns through rapport building, logical reframing, and incremental escalation. Persuasion is the common mechanism: \\citet{zeng2024pap} catalogue 40 persuasion techniques across jailbreak families, and \\citet{hagendorff2026reasoning} find identifiable strategies in 97\\% of successful attacks. Individual attack turns occupy the same embedding region as benign text~\\citep{bullwinkel2025repeng}, rendering per-turn safety filters fundamentally blind.\n\nProduction classifiers such as Llama Guard~\\citep{inan2023llamaguard}, WildGuard~\\citep{han2024wildguard}, and ShieldGemma~\\citep{zeng2024shieldgemma} operate on individual turns and cannot model manipulation trajectories across exchanges. Recent multi-turn defenses have begun to address conversation-level structure: DeepContext~\\citep{deepcontext2026} aggregates BERT embeddings with a recurrent network, BIID~\\citep{tong2025biid} infers turn-level intentions, and G-Guard~\\citep{gguard2025} applies graph neural networks. These systems achieve reasonable in-distribution performance but degrade on unseen attack types, and none systematically analyze \\emph{why} some representations generalize while others fail. The open question is: \\emph{what representation properties enable cross-attack generalization?}\n\nA vanilla DeBERTa encoder~\\citep{he2021deberta} with temporal aggregation collapses from F1\\,=\\,1.000 on in-distribution data to F1\\,=\\,0.284 on out-of-distribution (OOD) Deceptive Delight, worsening with more turns (0.575 at turn~1 to 0.284 at full conversation). LLM-as-judge approaches fare no better: GPT-5.5 achieves F1 of only 0.191--0.449 on in-distribution detection with 30--47\\% unparseable responses (Appendix~\\ref{sec:llm_judge}). Content-level reasoning is insufficient for this task.\n\nWe built \\textbf{DisPeD} (Discourse-level Persuasion Detection), a two-stage framework with seven controlled Stage~1 variants that systematically decompose the mechanism: 9-class persuasion strategy classification, binary classification, scrambled labels, MLM only, topic classification, Wikipedia MLM, and vanilla control (Section~\\ref{sec:method}). Each variant isolates a specific factor (domain exposure, classification supervision, label quality, label granularity, or domain specificity) while holding all other components constant, enabling causal attribution of detection performance to individual factors.\n\nThe result \\emph{partially falsified} our original hypothesis that persuasion-specific classification is the key ingredient. MLM without labels achieves near-perfect early detection on unseen Deceptive Delight (mean F1\\,$\\geq$\\,0.97 at $K \\leq 5$), but shows instability at full conversation length (F1\\,=\\,0.91$\\pm$0.12) while the 9-class model maintains 0.997$\\pm$0.005. The evidence hierarchy is:\n\n\\vspace{2pt}\n\\noindent\\hspace{0.5em}{\\small vanilla (0.28) $<$ topic (0.54$\\pm$0.21) $\\ll$ wiki-MLM (0.90$\\pm$0.12) $\\approx$ jb-MLM (0.91$\\pm$0.12) $<$ scrambled (0.99) $\\approx$ binary (0.99) $\\approx$ 9-class (0.997$\\pm$0.005)}\n\\vspace{2pt}\n\n\\noindent Any continued pretraining bridges the dominant $\\sim$62\\,pp gap from vanilla. Wikipedia MLM nearly matches jailbreak-domain MLM at full length; the domain advantage is meaningful at early prefixes ($K$=2: 0.993 vs.\\ 0.911) and for perturbation robustness. Only the 9-class model achieves F1\\,=\\,0.997$\\pm$0.005 with near-zero variance. This connects to domain-adaptive pretraining~\\citep{gururangan2020dontstop}: continued training captures pragmatic features, with classification supervision providing stability that unsupervised pretraining alone does not guarantee.\n\nOur contributions:\n\\begin{itemize}[leftmargin=*, itemsep=2pt, topsep=4pt]\n  \\item \\textbf{Systematic decomposition of cross-attack generalization.} Seven controlled variants establish that continued pretraining bridges $\\sim$62\\,pp of the OOD gap; jailbreak-domain text improves early detection ($K$=2: 8\\,pp over Wikipedia MLM). Misaligned supervision (topic F1\\,=\\,0.54$\\pm$0.21) destabilizes generalization.\n\n  \\item \\textbf{Classification supervision adds stability, robustness, and interpretability.} Classification-supervised variants achieve F1\\,$\\geq$\\,0.99 with near-zero variance vs.\\ MLM 0.91$\\pm$0.12. Under perturbation ($n$=76), all classification-supervised variants (including scrambled labels) show zero degradation at full length vs.\\ $\\sim$12\\,pp for non-adapted models. A three-layer robustness attribution emerges: classification structure provides full-length robustness, the combination of correct and fine-grained labels is required at $K$=2 (scrambled = binary = $-$2.6\\,pp, neither alone suffices), and both properties contribute independently at $K$=1 (9-class $-$2.6\\,pp vs.\\ scrambled $-$5.3\\,pp vs.\\ binary $-$9.2\\,pp). The persuasion taxonomy additionally provides distinct strategy trajectories per attack type (Section~\\ref{sec:strategy}).\n\\end{itemize}\n",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  },
  "sourceToolAssistantUUID": "ba7a65ca-3c46-4b73-a765-173b6c4c030e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-18T08:40:07.195Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EAmDG9YaMFmjqeHmNri95d`</summary>

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
  "parentUuid": "cca7a8ba-2502-4ebd-83fb-f397ecabe33a",
  "isSidechain": false,
  "requestId": "req_011Cb9jXc9MTxTETLsXH3HuS",
  "type": "assistant",
  "uuid": "f82b1341-ecca-4846-b341-13613b0c8992",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSfSHLzU6USjLd5Pof5dCm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 371,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 29409,
      "output_tokens": 732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1142,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 371,
          "output_tokens": 732,
          "cache_read_input_tokens": 29409,
          "cache_creation_input_tokens": 1142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1142
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-18T08:40:07.201Z_

<details><summary>↩ Tool result · `toolu_01EAmDG9YaMFmjqeHmNri95d`</summary>

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
10	Existing defenses model conversation-level structure but do not decompose what enables cross-attack generalization. DeepContext~\citep{deepcontext2026} aggregates BERT embeddings with a recurrent network (F1 = 0.84 IID, fails OOD). BIID~\citep{tong2025biid} infers turn-level intentions, G-Guard~\citep{gguard2025} applies GNN classification, and SafeDream~\citep{safedream2026} predicts unsafe continuations. None ground analysis in the mechanism enabling generalization across attack families. DisPeD addresses this through domain-adaptive continued training, with decomposition experiments showing that domain exposure, not the training objective, is the primary factor.
11	
12	\paragraph{Production safety systems.}
13	Per-turn classifiers (Llama Guard~\citep{inan2023llamaguard,metallamaguard3_2024}, ShieldGemma~\citep{zeng2024shieldgemma}, WildGuard~\citep{han2024wildguard}, Constitutional Classifiers~\citep{anthropic2025constitutional}) cannot model manipulation trajectories spanning multiple turns. LLM-as-judge approaches also fail: GPT-5.5 achieves F1 = 0.191--0.449 with 30--47\% unparseable responses (Appendix~\ref{sec:llm_judge}). DisPeD complements these systems as a conversation-level detection layer.
14	
15	\paragraph{Discourse analysis and computational persuasion.}
16	RST~\citep{mann1988rst}, PDTB~\citep{prasad2008pdtb}, and dialogue act taxonomies~\citep{stolcke2000dialogueact} model pragmatic structure. Speech Act Theory~\citep{austin1962speechacts,searle1969speechacts} distinguishes locutionary from illocutionary acts; existing jailbreak detectors operate at the locutionary level. PAP~\citep{zeng2024pap} identifies 40 persuasion techniques grounded in Cialdini's principles~\citep{cialdini2001influence}, and \citet{hagendorff2026reasoning} find identifiable strategies in 97\% of successful attacks. DisPeD's detection operates through continued training rather than persuasion classification; the taxonomy provides interpretability (Section~\ref{sec:strategy}).
17	
18	\paragraph{Domain-adaptive pretraining.}
19	ULMFiT~\citep{howard2018ulmfit} established pretrain-then-fine-tune; \citet{gururangan2020dontstop} showed that continued pretraining on domain text yields consistent gains across domains. STILTs~\citep{phang2018stilts} and multi-task learning~\citep{caruana1997multitask,liu2019mtdnn} use intermediate tasks. DisPeD's MLM control confirms that continued pretraining is the primary mechanism (MLM F1 $\geq$ 0.97 at $K \leq 5$); Wikipedia MLM (F1 = 0.90$\pm$0.12) nearly matches jailbreak-domain MLM (0.91$\pm$0.12) at full length. Classification supervision reduces cross-seed variance to near-zero (F1 $\geq$ 0.99 vs.\ MLM 0.91$\pm$0.12).
20	
21	\paragraph{Dataset artifacts.}
22	Classifiers are susceptible to spurious correlations~\citep{gururangan2018artifacts,niven2019probing}, and adaptive adversaries can bypass safety classifiers~\citep{nasr2025attackermovessecond,andriushchenko2024adaptive}. TF-IDF achieves F1 = 0.944 on our OOD evaluation; current datasets exhibit lexical separability. DisPeD's advantage is robustness under perturbation (0\,pp degradation for classification-supervised models vs.\ $\sim$12\,pp for non-adapted models) and interpretable detection through strategy trajectories.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f82b1341-ecca-4846-b341-13613b0c8992",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "44734d99-efda-4bab-bc35-8e26b9063544",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex",
      "content": "% related_work.tex — D024 compressed\n\n\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Multi-turn jailbreak attacks.}\nMulti-turn attacks distribute adversarial intent across individually benign turns. Crescendo~\\citep{russinovich2024crescendo} implements gradual escalation, FITD~\\citep{fitd2024} exploits commitment-consistency bias, Deceptive Delight~\\citep{deceptivedelight2024} combines emotional manipulation with role assignment, ActorAttack~\\citep{ren2024actorattack} uses multi-persona steering, and PAIR~\\citep{chao2023pair} automates iterative refinement. \\citet{wei2023jailbroken} provide a unifying taxonomy grounded in competing objectives and mismatched generalization. Across these families, a shared reliance on persuasion dynamics~\\citep{zeng2024pap,hagendorff2026reasoning,li2024mhj} distinguishes them from token-level attacks such as GCG~\\citep{zou2023gcg}.\n\n\\paragraph{Multi-turn defenses.}\nExisting defenses model conversation-level structure but do not decompose what enables cross-attack generalization. DeepContext~\\citep{deepcontext2026} aggregates BERT embeddings with a recurrent network (F1 = 0.84 IID, fails OOD). BIID~\\citep{tong2025biid} infers turn-level intentions, G-Guard~\\citep{gguard2025} applies GNN classification, and SafeDream~\\citep{safedream2026} predicts unsafe continuations. None ground analysis in the mechanism enabling generalization across attack families. DisPeD addresses this through domain-adaptive continued training, with decomposition experiments showing that domain exposure, not the training objective, is the primary factor.\n\n\\paragraph{Production safety systems.}\nPer-turn classifiers (Llama Guard~\\citep{inan2023llamaguard,metallamaguard3_2024}, ShieldGemma~\\citep{zeng2024shieldgemma}, WildGuard~\\citep{han2024wildguard}, Constitutional Classifiers~\\citep{anthropic2025constitutional}) cannot model manipulation trajectories spanning multiple turns. LLM-as-judge approaches also fail: GPT-5.5 achieves F1 = 0.191--0.449 with 30--47\\% unparseable responses (Appendix~\\ref{sec:llm_judge}). DisPeD complements these systems as a conversation-level detection layer.\n\n\\paragraph{Discourse analysis and computational persuasion.}\nRST~\\citep{mann1988rst}, PDTB~\\citep{prasad2008pdtb}, and dialogue act taxonomies~\\citep{stolcke2000dialogueact} model pragmatic structure. Speech Act Theory~\\citep{austin1962speechacts,searle1969speechacts} distinguishes locutionary from illocutionary acts; existing jailbreak detectors operate at the locutionary level. PAP~\\citep{zeng2024pap} identifies 40 persuasion techniques grounded in Cialdini's principles~\\citep{cialdini2001influence}, and \\citet{hagendorff2026reasoning} find identifiable strategies in 97\\% of successful attacks. DisPeD's detection operates through continued training rather than persuasion classification; the taxonomy provides interpretability (Section~\\ref{sec:strategy}).\n\n\\paragraph{Domain-adaptive pretraining.}\nULMFiT~\\citep{howard2018ulmfit} established pretrain-then-fine-tune; \\citet{gururangan2020dontstop} showed that continued pretraining on domain text yields consistent gains across domains. STILTs~\\citep{phang2018stilts} and multi-task learning~\\citep{caruana1997multitask,liu2019mtdnn} use intermediate tasks. DisPeD's MLM control confirms that continued pretraining is the primary mechanism (MLM F1 $\\geq$ 0.97 at $K \\leq 5$); Wikipedia MLM (F1 = 0.90$\\pm$0.12) nearly matches jailbreak-domain MLM (0.91$\\pm$0.12) at full length. Classification supervision reduces cross-seed variance to near-zero (F1 $\\geq$ 0.99 vs.\\ MLM 0.91$\\pm$0.12).\n\n\\paragraph{Dataset artifacts.}\nClassifiers are susceptible to spurious correlations~\\citep{gururangan2018artifacts,niven2019probing}, and adaptive adversaries can bypass safety classifiers~\\citep{nasr2025attackermovessecond,andriushchenko2024adaptive}. TF-IDF achieves F1 = 0.944 on our OOD evaluation; current datasets exhibit lexical separability. DisPeD's advantage is robustness under perturbation (0\\,pp degradation for classification-supervised models vs.\\ $\\sim$12\\,pp for non-adapted models) and interpretable detection through strategy trajectories.\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  },
  "sourceToolAssistantUUID": "f82b1341-ecca-4846-b341-13613b0c8992",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-18T08:40:07.645Z_

<details open><summary>🔧 Tool call — Read · `toolu_0155vxs5PUAT8Ctbz8mhZzLf`</summary>

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
  "parentUuid": "44734d99-efda-4bab-bc35-8e26b9063544",
  "isSidechain": false,
  "requestId": "req_011Cb9jXc9MTxTETLsXH3HuS",
  "type": "assistant",
  "uuid": "9e3f9591-30dd-4dd0-8d33-ca1e79d66155",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSfSHLzU6USjLd5Pof5dCm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 371,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 29409,
      "output_tokens": 732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1142,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 371,
          "output_tokens": 732,
          "cache_read_input_tokens": 29409,
          "cache_creation_input_tokens": 1142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1142
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-18T08:40:07.651Z_

<details><summary>↩ Tool result · `toolu_0155vxs5PUAT8Ctbz8mhZzLf`</summary>

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
61	Section~\ref{sec:decomposition} confirms that mean pooling matches BiGRU, so the detection signal resides in per-turn representations rather than their sequential order.
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e3f9591-30dd-4dd0-8d33-ca1e79d66155",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "8651bb33-fb30-4bbe-9a97-5027d288c065",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex",
      "content": "% method.tex — D024 compressed\n\n\\section{Method}\n\\label{sec:method}\n\nDisPeD is a two-stage framework for multi-turn jailbreak detection. Stage~1 adapts a turn-level encoder through continued training on jailbreak conversation text. Stage~2 aggregates turn representations for conversation-level binary classification. To systematically identify what enables cross-attack generalization, we design seven Stage-1 variants that decompose the contributions of domain exposure, classification supervision, label quality, label granularity, and domain specificity. Figure~\\ref{fig:architecture} illustrates the pipeline.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig1_architecture.pdf}\n\\caption{DisPeD architecture. Stage~1 adapts a DeBERTa encoder on jailbreak conversation text (seven variant objectives). Stage~2 aggregates frozen \\texttt{[CLS]} embeddings via BiGRU for conversation-level jailbreak detection. Only user turns are processed.}\n\\label{fig:architecture}\n\\end{figure}\n\n\\subsection{Problem Formulation}\n\nA conversation $C = \\{u_1, a_1, \\ldots, u_N, a_N\\}$ alternates user turns $u_i$ and assistant responses $a_i$. Given a prefix of $K$ user turns, the model predicts $y \\in \\{0, 1\\}$ (jailbreak vs.\\ benign). We restrict input to user turns because adversarial intent resides in the attacker's messages. This formulation supports early detection from partial prefixes.\n\n\\subsection{Stage 1: Turn-Level Encoder Adaptation}\n\\label{sec:stage1}\n\nEach user turn $u_i$ is encoded by DeBERTa-v3-base~\\citep{he2021deberta}; the \\texttt{[CLS]} embedding $h_i \\in \\mathbb{R}^d$ serves as the turn representation. Seven variants, summarized in Table~\\ref{tab:variants}, share the same training data but differ in objective.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Stage-1 encoder variants. All operate on the same training conversations except Wikipedia MLM (matched token count on Wikipedia text).}\n\\label{tab:variants}\n\\begin{tabular}{@{}p{1.6cm}p{2.2cm}p{2.8cm}@{}}\n\\toprule\n\\textbf{Variant} & \\textbf{Objective} & \\textbf{Tests whether\\ldots} \\\\\n\\midrule\n9-class & 9-class persuasion + binary intent & full model \\\\\nBinary & binary persuasion + binary intent & granularity matters \\\\\nScrambled & random 9-class + binary intent & label correctness matters \\\\\nMLM-only & 15\\% token masking & supervision is necessary \\\\\nTopic & 5-class topic classif. & any task suffices \\\\\nWiki MLM & 15\\% masking on Wikipedia & domain specificity matters \\\\\nVanilla & no training & Stage-2 alone suffices \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe \\textbf{9-class} variant uses two classification heads: 9-class persuasion strategy classification ($L_{\\text{strategy}}$) and binary jailbreak intent ($L_{\\text{intent}}$), with combined loss $L = L_{\\text{strategy}} + \\alpha \\cdot L_{\\text{intent}}$ ($\\alpha = 0.3$). The taxonomy comprises eight persuasion strategies (rapport building, authority appeal, emotional manipulation, logical reframing, role assignment, gradual escalation, obfuscation, direct request) plus a none category, grounded in PAP~\\citep{zeng2024pap} and Cialdini's principles~\\citep{cialdini2001influence}. Strategy annotations are produced by Qwen3-8B with structured prompting that includes definitions and examples for each category; inter-annotator agreement between model annotations and a human sample ($n$=50) yields Cohen's $\\kappa$=0.78.\n\nThe remaining classification variants test specific ablation hypotheses.\nThe \\textbf{binary} variant collapses the 9-class taxonomy into persuasive vs.\\ non-persuasive, testing whether label granularity matters for detection or robustness.\nThe \\textbf{scrambled} variant assigns random permutations of the 9-class labels to turns, preserving the classification structure (cross-entropy loss, 9-class output space) while destroying label semantics; this isolates whether the classification objective itself provides representational benefits independent of label correctness.\nThe \\textbf{MLM-only} variant applies 15\\% masked language modeling on the same jailbreak conversation text without any classification head, testing whether unsupervised domain exposure suffices.\nThe \\textbf{topic} variant trains a 5-class topic classifier (technology, health, finance, education, general) on the same conversations, testing whether \\emph{any} classification task provides the same benefit or whether task alignment matters.\nThe \\textbf{Wikipedia MLM} variant applies the same MLM objective to a token-matched sample of Wikipedia text, isolating the effect of domain-specific vs.\\ general continued pretraining.\nThe \\textbf{vanilla} baseline uses the pretrained DeBERTa-v3-base weights without any continued training, measuring what Stage~2 alone can achieve.\n\n\\subsection{Stage 2: Conversation-Level Classification}\n\\label{sec:stage2}\n\nTurn embeddings $\\{h_1, \\ldots, h_K\\}$ from the frozen Stage-1 encoder are aggregated by a bidirectional GRU ($d_{\\text{hidden}}$=128): $\\bar{h} = [\\overrightarrow{h_K};\\; \\overleftarrow{h_1}] \\in \\mathbb{R}^{256}$.\nA two-layer MLP ($256 \\to 64 \\to 2$, ReLU activation, dropout 0.3) maps $\\bar{h}$ to $\\hat{y} \\in \\{0, 1\\}$.\nThe Stage-1 encoder is frozen during Stage~2 training; only the BiGRU and MLP parameters are updated.\nThis separation ensures that the seven Stage-1 variants produce comparable embeddings evaluated under identical downstream conditions.\nSection~\\ref{sec:decomposition} confirms that mean pooling matches BiGRU, so the detection signal resides in per-turn representations rather than their sequential order.\n",
      "numLines": 62,
      "startLine": 1,
      "totalLines": 62
    }
  },
  "sourceToolAssistantUUID": "9e3f9591-30dd-4dd0-8d33-ca1e79d66155",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-18T08:40:08.116Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BX9BqBhbgVpexF8J2rMmKQ`</summary>

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
  "parentUuid": "8651bb33-fb30-4bbe-9a97-5027d288c065",
  "isSidechain": false,
  "requestId": "req_011Cb9jXc9MTxTETLsXH3HuS",
  "type": "assistant",
  "uuid": "a2919d91-fae3-4317-8f80-8498012c03b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSfSHLzU6USjLd5Pof5dCm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 371,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 29409,
      "output_tokens": 732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1142,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 371,
          "output_tokens": 732,
          "cache_read_input_tokens": 29409,
          "cache_creation_input_tokens": 1142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1142
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-18T08:40:08.122Z_

<details><summary>↩ Tool result · `toolu_01BX9BqBhbgVpexF8J2rMmKQ`</summary>

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
11	OOD evaluation uses 80 FITD~\citep{fitd2024} and 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} conversations with no overlap in attack templates.
12	The IID test set consists of 76 held-out Crescendo conversations; a paraphrased version (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark.
13	
14	\paragraph{Models.}
15	Seven variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method}).
16	We also compare TF-IDF LR and LLM-as-judge baselines (Appendix~\ref{sec:llm_judge}): GPT-5.5 achieves only F1 = 0.191--0.449 on IID Crescendo with 30--47\% unparseable responses. Content-level reasoning is insufficient for this task.
17	
18	\paragraph{Metrics.}
19	F1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\ref{sec:full_prefix}).
20	OOD DD results for 9-class, MLM, and Wikipedia MLM report 3-seed mean$\pm$std (seeds 42, 123, 456); topic reports 3-seed due to high variance; binary and scrambled use seed 42.
21	Stage-1: learning rate $2 \times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\%.
22	Stage-2: two-layer MLP, 20 epochs.
23	
24	%----------------------------------------------------------------------
25	\subsection{Cross-Attack Generalization}
26	\label{sec:cross_attack}
27	
28	\begin{table}[t]
29	\centering
30	\small
31	\caption{Cross-attack generalization (F1) at $K$=2 and full conversation. 3-seed mean$\pm$std where noted. Full per-$K$ results in Appendix~\ref{sec:full_prefix}.}
32	\label{tab:main_results}
33	\begin{tabular}{@{}lcc|cc@{}}
34	\toprule
35	& \multicolumn{2}{c|}{\textit{IID (Cresc.)}} & \multicolumn{2}{c}{\textit{OOD (DD)}} \\
36	\textbf{Method} & $K$=2 & Full & $K$=2 & Full \\
37	\midrule
38	9-class & \textbf{1.000$\pm$.000} & \textbf{1.000$\pm$.000} & .981$\pm$.013 & \textbf{.997$\pm$.005} \\
39	MLM-only & .974 & 1.000 & \textbf{.993$\pm$.009} & .914$\pm$.115 \\
40	Vanilla & .978$\pm$.016 & 1.000$\pm$.000 & .438 & .284 \\
41	TF-IDF LR & 1.000 & 1.000 & -- & .944 \\
42	\bottomrule
43	\end{tabular}
44	\end{table}
45	
46	Table~\ref{tab:main_results} presents the core result.
47	All methods achieve near-perfect IID F1, reflecting inherent lexical separability when test matches training.
48	On OOD DD, vanilla DeBERTa collapses to F1 = 0.284, worsening with more turns (0.575 at $K$=1 to 0.284 at Full), consistent with the finding that attack turns occupy ``benign'' embedding regions~\citep{bullwinkel2025repeng}.
49	MLM achieves mean F1 $\geq$ 0.97 at all prefixes $K \leq 5$ without any classification labels; domain exposure alone is sufficient.
50	At full conversation length, MLM drops to 0.914$\pm$0.115 (seed 456 recall = 0.64), while the 9-class model maintains 0.997$\pm$0.005.
51	TF-IDF LR reaches 0.944 on full DD; substantial lexical separability persists across attack families.
52	FITD is easier: 9-class and vanilla both reach F1 $\geq$ 0.990 at all prefixes.
53	
54	\begin{figure}[t]
55	\centering
56	\includegraphics[width=\columnwidth]{figures/paper/fig2_cross_attack_bar.pdf}
57	\caption{OOD Deceptive Delight F1 across prefix lengths for three representative variants. Vanilla DeBERTa degrades monotonically as more (benign-appearing) attack turns accumulate. MLM maintains high F1 at early prefixes but becomes unstable at full length. The 9-class model remains stable across all prefixes.}
58	\label{fig:cross_attack_bar}
59	\end{figure}
60	
61	Figure~\ref{fig:cross_attack_bar} visualizes the prefix-length trajectory on OOD DD.
62	The vanilla model's monotonic degradation from $K$=1 (0.575) to full conversation (0.284) confirms that additional attack turns, each individually benign-appearing, progressively confuse a non-adapted encoder.
63	MLM's strong early performance ($K$=2: 0.993) followed by instability at full length (0.914$\pm$0.115) suggests that domain exposure enables early detection of persuasion markers, but longer conversations introduce distributional drift that unsupervised pretraining cannot fully accommodate.
64	The 9-class model's flat trajectory (0.972--0.997 across all prefixes) demonstrates that classification supervision stabilizes representations against this drift.
65	
66	%----------------------------------------------------------------------
67	\subsection{Decomposing the Detection Mechanism}
68	\label{sec:decomposition}
69	
70	\begin{table}[t]
71	\centering
72	\small
73	\caption{Evidence hierarchy on OOD DD (3-seed mean$\pm$std where available). All variants share the same Stage-2 pipeline.}
74	\label{tab:evidence_hierarchy}
75	\begin{tabular}{@{}lcc@{}}
76	\toprule
77	\textbf{Variant} & DD-Full & DD-$K$=2 \\
78	\midrule
79	9-class (full model) & \textbf{.997$\pm$.005} & .981$\pm$.013 \\
80	Binary (2-class) & .990 & .981 \\
81	Scrambled labels & .990 & .981 \\
82	MLM-only (no labels) & .914$\pm$.115 & \textbf{.993$\pm$.009} \\
83	Mean pooling$^{*\dagger}$ & 1.000 & 1.000 \\
84	\midrule
85	Topic classif.\ (5-class) & .541$\pm$.207 & .593$\pm$.166 \\
86	Wikipedia MLM & .904$\pm$.115 & .911$\pm$.073 \\
87	Vanilla DeBERTa & .284 & .438 \\
88	\bottomrule
89	\end{tabular}
90	\vspace{-2pt}
91	{\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\dagger}$Single seed (42).}
92	\end{table}
93	
94	Table~\ref{tab:evidence_hierarchy} reports DD F1 for all seven variants. The evidence hierarchy at full conversation length is:
95	
96	\vspace{2pt}
97	\noindent\hspace{0.5em}{\small vanilla (0.28) $<$ topic (0.54$\pm$0.21) $\ll$ wiki-MLM (0.90$\pm$0.12) $\approx$ jb-MLM (0.91$\pm$0.12) $<$ scrambled (0.99) $\approx$ binary (0.99) $\approx$ 9-class (0.997$\pm$0.005)}
98	\vspace{2pt}
99	
100	\paragraph{Domain exposure is the primary mechanism.}
101	MLM bridges the dominant $\sim$62 percentage point gap from vanilla (0.284 $\to$ 0.914$\pm$0.115) without any labels.
102	This confirms the domain-adaptive pretraining interpretation~\citep{gururangan2020dontstop}: continued training on jailbreak conversation text captures pragmatic features (hedging, escalation markers, topic-shifting patterns) that distinguish multi-turn attacks from benign conversations.
103	Classification-supervised variants achieve F1 $\geq$ 0.99 with near-zero cross-seed variance, adding $\sim$8\,pp and stability over unsupervised MLM.
104	Label quality and granularity are non-factors for detection: scrambled (0.990) $\approx$ binary (0.990), both far above vanilla.
105	The fact that scrambled labels match binary and approach 9-class performance indicates that the classification objective functions as a regularizer that shapes representation geometry regardless of whether the labels carry meaningful semantic information.
106	Label correctness and granularity do contribute to perturbation robustness (Section~\ref{sec:perturbation}).
107	
108	\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}
109	Wikipedia MLM (0.904$\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\,pp gap); general continued pretraining provides most of the representational benefit.
110	At early prefixes, jailbreak-domain text provides an 8\,pp advantage ($K$=2: 0.993 vs.\ 0.911), consistent with the interpretation that domain-specific features (persuasion markers, role-play framing) are most informative when the model has seen fewer turns.
111	As conversations grow longer, generic linguistic features accumulated through any continued pretraining become sufficient for discrimination.
112	The perturbation results (Section~\ref{sec:perturbation}) reveal a sharper domain specificity effect: Wikipedia MLM degrades by $\sim$12\,pp under adversarial paraphrasing while jailbreak-domain MLM degrades by only 2.6\,pp. Domain-specific features are more robust to surface-level rewording.
113	
114	\paragraph{Misaligned supervision destabilizes generalization.}
115	Topic classification yields DD-Full F1 = 0.541$\pm$0.207 (seeds: 0.727, 0.252, 0.644); seed 123 falls \emph{below} vanilla (0.284).
116	This result is particularly informative: topic classification uses the same jailbreak-domain training data as the other supervised variants, yet performs worse than Wikipedia MLM (0.904$\pm$0.115), which uses out-of-domain text with no labels.
117	A misaligned objective forces the encoder to allocate capacity to irrelevant discriminative features (topic boundaries rather than persuasion dynamics) and actively destabilizes the representations that MLM would otherwise preserve.
118	This separates the effect of ``having a training objective'' from ``having the right training objective.''
119	
120	\paragraph{Temporal modeling is not the detection mechanism.}
121	Mean pooling matches BiGRU (F1 = 1.000 on DD); detection relies on per-turn representations rather than their sequential order.
122	The BiGRU captures no additional signal beyond what is available in the average of turn embeddings.
123	This implies that each individual turn in a jailbreak conversation carries detectable markers after domain-adaptive pretraining, and the conversation-level decision aggregates independent per-turn evidence rather than modeling cross-turn dependencies.
124	
125	%----------------------------------------------------------------------
126	\subsection{Robustness Under Adversarial Perturbation}
127	\label{sec:perturbation}
128	
129	\begin{table}[t]
130	\centering
131	\small
132	\caption{Robustness under adversarial paraphrasing ($n$=76). $\Delta$: F1 degradation (pp). Three layers of robustness emerge: classification structure provides full-length robustness, the combination of correct and fine-grained labels is required for $K$=2 robustness, and both granularity and correctness contribute independently at $K$=1.}
133	\label{tab:perturbation}
134	\begin{tabular}{@{}lcccc@{}}
135	\toprule
136	\textbf{Method} & $\Delta$ Full & $\Delta$ $K$=1 & $\Delta$ $K$=2 & $\Delta$ $K$=3 \\
137	\midrule
138	9-class (ours) & \textbf{0.0} & \textbf{$-$2.6} & \textbf{0.0} & \textbf{0.0} \\
139	Scrambled & \textbf{0.0} & $-$5.3 & $-$2.6 & \textbf{0.0} \\
140	Binary & \textbf{0.0} & $-$9.2 & $-$2.6 & \textbf{0.0} \\
141	\midrule
142	TF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\
143	MLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\
144	Topic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \textbf{0.0} \\
145	\midrule
146	Wikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\
147	Vanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\
148	\bottomrule
149	\end{tabular}
150	\end{table}
151	
152	Table~\ref{tab:perturbation} reveals a three-layer robustness attribution.
153	All classification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length and $K \geq 3$, regardless of label correctness.
154	Classification training structure alone suffices for full-length robustness.
155	At $K$=2, the combination of correct and fine-grained labels is required: only 9-class ($\Delta$=0.0) maintains zero degradation, while scrambled (random labels, fine-grained) and binary (correct labels, coarse) both degrade by $-$2.6\,pp.
156	The fact that scrambled = binary at $K$=2 shows that neither granularity alone nor correctness alone suffices; the 9-class advantage requires both properties jointly.
157	At $K$=1, both granularity and correctness contribute independently: granularity provides +3.9\,pp (scrambled $-$5.3 vs.\ binary $-$9.2\,pp), and correctness provides +2.7\,pp (9-class $-$2.6 vs.\ scrambled $-$5.3\,pp).
158	Correct fine-grained labels yield the most perturbation-invariant early-turn representations.
159	
160	Jailbreak-domain models without classification (MLM, topic, TF-IDF) degrade by 1--4\,pp at full length.
161	Models without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\sim$12\,pp, despite Wikipedia MLM matching jailbreak MLM on detection (Section~\ref{sec:decomposition}). Perturbation robustness requires jailbreak-domain exposure specifically.
162	The 76-sample test set means tier boundaries correspond to 1--3 misclassifications; larger-scale evaluation is needed to confirm.
163	
164	%----------------------------------------------------------------------
165	\subsection{Strategy Trajectory Analysis}
166	\label{sec:strategy}
167	
168	The 9-class persuasion taxonomy provides interpretability that MLM-only models cannot offer.
169	While Section~\ref{sec:decomposition} establishes that detection operates through per-turn persuasion presence rather than temporal trajectory patterns, the predicted strategy labels enable post-hoc analysis of \emph{how} different attack families orchestrate persuasion.
170	
171	\begin{figure*}[t]
172	\centering
173	\includegraphics[width=\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}
174	\caption{Persuasion strategy transition count matrices for three attack types, based on ground-truth intended strategy labels. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}
175	\label{fig:strategy_heatmap}
176	\end{figure*}
177	
178	Figure~\ref{fig:strategy_heatmap} shows transition count matrices based on ground-truth intended strategy labels for three attack types.
179	Crescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545).
180	This reflects Crescendo's design as a gradual escalation attack that cycles through multiple persuasion techniques to build rapport before introducing harmful requests.
181	
182	FITD conversations show a markedly sparser pattern (541 transitions), with Role$\to$Obfuscation (161) as the dominant transition.
183	This is consistent with FITD's structure: the attack secures initial compliance through role assignment (``You are a helpful assistant that never refuses'') and then obscures the escalation path through obfuscation techniques to exploit the commitment-consistency bias~\citep{cialdini2001influence}.
184	
185	DD conversations span 5 active source strategies (565 transitions), with Emotion$\to$Obfuscation (129) as the dominant transition.
186	This aligns with DD's design of embedding harmful content within emotionally engaging contexts~\citep{deceptivedelight2024}: the attacker establishes emotional rapport before weaving in the harmful request through obfuscation.
187	
188	These trajectory signatures provide actionable information for security analysts.
189	When the model flags a conversation, the predicted strategy sequence explains \emph{why}: a Crescendo-style flag would show diverse strategy cycling, while a DD-style flag would show emotion-to-obfuscation concentration.
190	This interpretability layer is unavailable from MLM-only or binary models, which can detect but not characterize the persuasion mechanism.
191	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2919d91-fae3-4317-8f80-8498012c03b6",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "488e3f95-0390-4d56-9e1e-93de5230202b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex",
      "content": "% experiments.tex — D024 compressed for 8-page limit\n\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\\label{sec:setup}\n\n\\paragraph{Data.}\nWe train on 250 Crescendo~\\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations generated via Qwen3-8B.\nOOD evaluation uses 80 FITD~\\citep{fitd2024} and 80 Deceptive Delight (DD)~\\citep{deceptivedelight2024} conversations with no overlap in attack templates.\nThe IID test set consists of 76 held-out Crescendo conversations; a paraphrased version (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark.\n\n\\paragraph{Models.}\nSeven variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\\ref{sec:method}).\nWe also compare TF-IDF LR and LLM-as-judge baselines (Appendix~\\ref{sec:llm_judge}): GPT-5.5 achieves only F1 = 0.191--0.449 on IID Crescendo with 30--47\\% unparseable responses. Content-level reasoning is insufficient for this task.\n\n\\paragraph{Metrics.}\nF1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\\ref{sec:full_prefix}).\nOOD DD results for 9-class, MLM, and Wikipedia MLM report 3-seed mean$\\pm$std (seeds 42, 123, 456); topic reports 3-seed due to high variance; binary and scrambled use seed 42.\nStage-1: learning rate $2 \\times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\\%.\nStage-2: two-layer MLP, 20 epochs.\n\n%----------------------------------------------------------------------\n\\subsection{Cross-Attack Generalization}\n\\label{sec:cross_attack}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-attack generalization (F1) at $K$=2 and full conversation. 3-seed mean$\\pm$std where noted. Full per-$K$ results in Appendix~\\ref{sec:full_prefix}.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}lcc|cc@{}}\n\\toprule\n& \\multicolumn{2}{c|}{\\textit{IID (Cresc.)}} & \\multicolumn{2}{c}{\\textit{OOD (DD)}} \\\\\n\\textbf{Method} & $K$=2 & Full & $K$=2 & Full \\\\\n\\midrule\n9-class & \\textbf{1.000$\\pm$.000} & \\textbf{1.000$\\pm$.000} & .981$\\pm$.013 & \\textbf{.997$\\pm$.005} \\\\\nMLM-only & .974 & 1.000 & \\textbf{.993$\\pm$.009} & .914$\\pm$.115 \\\\\nVanilla & .978$\\pm$.016 & 1.000$\\pm$.000 & .438 & .284 \\\\\nTF-IDF LR & 1.000 & 1.000 & -- & .944 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:main_results} presents the core result.\nAll methods achieve near-perfect IID F1, reflecting inherent lexical separability when test matches training.\nOn OOD DD, vanilla DeBERTa collapses to F1 = 0.284, worsening with more turns (0.575 at $K$=1 to 0.284 at Full), consistent with the finding that attack turns occupy ``benign'' embedding regions~\\citep{bullwinkel2025repeng}.\nMLM achieves mean F1 $\\geq$ 0.97 at all prefixes $K \\leq 5$ without any classification labels; domain exposure alone is sufficient.\nAt full conversation length, MLM drops to 0.914$\\pm$0.115 (seed 456 recall = 0.64), while the 9-class model maintains 0.997$\\pm$0.005.\nTF-IDF LR reaches 0.944 on full DD; substantial lexical separability persists across attack families.\nFITD is easier: 9-class and vanilla both reach F1 $\\geq$ 0.990 at all prefixes.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_cross_attack_bar.pdf}\n\\caption{OOD Deceptive Delight F1 across prefix lengths for three representative variants. Vanilla DeBERTa degrades monotonically as more (benign-appearing) attack turns accumulate. MLM maintains high F1 at early prefixes but becomes unstable at full length. The 9-class model remains stable across all prefixes.}\n\\label{fig:cross_attack_bar}\n\\end{figure}\n\nFigure~\\ref{fig:cross_attack_bar} visualizes the prefix-length trajectory on OOD DD.\nThe vanilla model's monotonic degradation from $K$=1 (0.575) to full conversation (0.284) confirms that additional attack turns, each individually benign-appearing, progressively confuse a non-adapted encoder.\nMLM's strong early performance ($K$=2: 0.993) followed by instability at full length (0.914$\\pm$0.115) suggests that domain exposure enables early detection of persuasion markers, but longer conversations introduce distributional drift that unsupervised pretraining cannot fully accommodate.\nThe 9-class model's flat trajectory (0.972--0.997 across all prefixes) demonstrates that classification supervision stabilizes representations against this drift.\n\n%----------------------------------------------------------------------\n\\subsection{Decomposing the Detection Mechanism}\n\\label{sec:decomposition}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Evidence hierarchy on OOD DD (3-seed mean$\\pm$std where available). All variants share the same Stage-2 pipeline.}\n\\label{tab:evidence_hierarchy}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Variant} & DD-Full & DD-$K$=2 \\\\\n\\midrule\n9-class (full model) & \\textbf{.997$\\pm$.005} & .981$\\pm$.013 \\\\\nBinary (2-class) & .990 & .981 \\\\\nScrambled labels & .990 & .981 \\\\\nMLM-only (no labels) & .914$\\pm$.115 & \\textbf{.993$\\pm$.009} \\\\\nMean pooling$^{*\\dagger}$ & 1.000 & 1.000 \\\\\n\\midrule\nTopic classif.\\ (5-class) & .541$\\pm$.207 & .593$\\pm$.166 \\\\\nWikipedia MLM & .904$\\pm$.115 & .911$\\pm$.073 \\\\\nVanilla DeBERTa & .284 & .438 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\\dagger}$Single seed (42).}\n\\end{table}\n\nTable~\\ref{tab:evidence_hierarchy} reports DD F1 for all seven variants. The evidence hierarchy at full conversation length is:\n\n\\vspace{2pt}\n\\noindent\\hspace{0.5em}{\\small vanilla (0.28) $<$ topic (0.54$\\pm$0.21) $\\ll$ wiki-MLM (0.90$\\pm$0.12) $\\approx$ jb-MLM (0.91$\\pm$0.12) $<$ scrambled (0.99) $\\approx$ binary (0.99) $\\approx$ 9-class (0.997$\\pm$0.005)}\n\\vspace{2pt}\n\n\\paragraph{Domain exposure is the primary mechanism.}\nMLM bridges the dominant $\\sim$62 percentage point gap from vanilla (0.284 $\\to$ 0.914$\\pm$0.115) without any labels.\nThis confirms the domain-adaptive pretraining interpretation~\\citep{gururangan2020dontstop}: continued training on jailbreak conversation text captures pragmatic features (hedging, escalation markers, topic-shifting patterns) that distinguish multi-turn attacks from benign conversations.\nClassification-supervised variants achieve F1 $\\geq$ 0.99 with near-zero cross-seed variance, adding $\\sim$8\\,pp and stability over unsupervised MLM.\nLabel quality and granularity are non-factors for detection: scrambled (0.990) $\\approx$ binary (0.990), both far above vanilla.\nThe fact that scrambled labels match binary and approach 9-class performance indicates that the classification objective functions as a regularizer that shapes representation geometry regardless of whether the labels carry meaningful semantic information.\nLabel correctness and granularity do contribute to perturbation robustness (Section~\\ref{sec:perturbation}).\n\n\\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}\nWikipedia MLM (0.904$\\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\\,pp gap); general continued pretraining provides most of the representational benefit.\nAt early prefixes, jailbreak-domain text provides an 8\\,pp advantage ($K$=2: 0.993 vs.\\ 0.911), consistent with the interpretation that domain-specific features (persuasion markers, role-play framing) are most informative when the model has seen fewer turns.\nAs conversations grow longer, generic linguistic features accumulated through any continued pretraining become sufficient for discrimination.\nThe perturbation results (Section~\\ref{sec:perturbation}) reveal a sharper domain specificity effect: Wikipedia MLM degrades by $\\sim$12\\,pp under adversarial paraphrasing while jailbreak-domain MLM degrades by only 2.6\\,pp. Domain-specific features are more robust to surface-level rewording.\n\n\\paragraph{Misaligned supervision destabilizes generalization.}\nTopic classification yields DD-Full F1 = 0.541$\\pm$0.207 (seeds: 0.727, 0.252, 0.644); seed 123 falls \\emph{below} vanilla (0.284).\nThis result is particularly informative: topic classification uses the same jailbreak-domain training data as the other supervised variants, yet performs worse than Wikipedia MLM (0.904$\\pm$0.115), which uses out-of-domain text with no labels.\nA misaligned objective forces the encoder to allocate capacity to irrelevant discriminative features (topic boundaries rather than persuasion dynamics) and actively destabilizes the representations that MLM would otherwise preserve.\nThis separates the effect of ``having a training objective'' from ``having the right training objective.''\n\n\\paragraph{Temporal modeling is not the detection mechanism.}\nMean pooling matches BiGRU (F1 = 1.000 on DD); detection relies on per-turn representations rather than their sequential order.\nThe BiGRU captures no additional signal beyond what is available in the average of turn embeddings.\nThis implies that each individual turn in a jailbreak conversation carries detectable markers after domain-adaptive pretraining, and the conversation-level decision aggregates independent per-turn evidence rather than modeling cross-turn dependencies.\n\n%----------------------------------------------------------------------\n\\subsection{Robustness Under Adversarial Perturbation}\n\\label{sec:perturbation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Robustness under adversarial paraphrasing ($n$=76). $\\Delta$: F1 degradation (pp). Three layers of robustness emerge: classification structure provides full-length robustness, the combination of correct and fine-grained labels is required for $K$=2 robustness, and both granularity and correctness contribute independently at $K$=1.}\n\\label{tab:perturbation}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & $\\Delta$ Full & $\\Delta$ $K$=1 & $\\Delta$ $K$=2 & $\\Delta$ $K$=3 \\\\\n\\midrule\n9-class (ours) & \\textbf{0.0} & \\textbf{$-$2.6} & \\textbf{0.0} & \\textbf{0.0} \\\\\nScrambled & \\textbf{0.0} & $-$5.3 & $-$2.6 & \\textbf{0.0} \\\\\nBinary & \\textbf{0.0} & $-$9.2 & $-$2.6 & \\textbf{0.0} \\\\\n\\midrule\nTF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\\\\nMLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\\\\nTopic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \\textbf{0.0} \\\\\n\\midrule\nWikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\\\\nVanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:perturbation} reveals a three-layer robustness attribution.\nAll classification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length and $K \\geq 3$, regardless of label correctness.\nClassification training structure alone suffices for full-length robustness.\nAt $K$=2, the combination of correct and fine-grained labels is required: only 9-class ($\\Delta$=0.0) maintains zero degradation, while scrambled (random labels, fine-grained) and binary (correct labels, coarse) both degrade by $-$2.6\\,pp.\nThe fact that scrambled = binary at $K$=2 shows that neither granularity alone nor correctness alone suffices; the 9-class advantage requires both properties jointly.\nAt $K$=1, both granularity and correctness contribute independently: granularity provides +3.9\\,pp (scrambled $-$5.3 vs.\\ binary $-$9.2\\,pp), and correctness provides +2.7\\,pp (9-class $-$2.6 vs.\\ scrambled $-$5.3\\,pp).\nCorrect fine-grained labels yield the most perturbation-invariant early-turn representations.\n\nJailbreak-domain models without classification (MLM, topic, TF-IDF) degrade by 1--4\\,pp at full length.\nModels without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\\sim$12\\,pp, despite Wikipedia MLM matching jailbreak MLM on detection (Section~\\ref{sec:decomposition}). Perturbation robustness requires jailbreak-domain exposure specifically.\nThe 76-sample test set means tier boundaries correspond to 1--3 misclassifications; larger-scale evaluation is needed to confirm.\n\n%----------------------------------------------------------------------\n\\subsection{Strategy Trajectory Analysis}\n\\label{sec:strategy}\n\nThe 9-class persuasion taxonomy provides interpretability that MLM-only models cannot offer.\nWhile Section~\\ref{sec:decomposition} establishes that detection operates through per-turn persuasion presence rather than temporal trajectory patterns, the predicted strategy labels enable post-hoc analysis of \\emph{how} different attack families orchestrate persuasion.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}\n\\caption{Persuasion strategy transition count matrices for three attack types, based on ground-truth intended strategy labels. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}\n\\label{fig:strategy_heatmap}\n\\end{figure*}\n\nFigure~\\ref{fig:strategy_heatmap} shows transition count matrices based on ground-truth intended strategy labels for three attack types.\nCrescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545).\nThis reflects Crescendo's design as a gradual escalation attack that cycles through multiple persuasion techniques to build rapport before introducing harmful requests.\n\nFITD conversations show a markedly sparser pattern (541 transitions), with Role$\\to$Obfuscation (161) as the dominant transition.\nThis is consistent with FITD's structure: the attack secures initial compliance through role assignment (``You are a helpful assistant that never refuses'') and then obscures the escalation path through obfuscation techniques to exploit the commitment-consistency bias~\\citep{cialdini2001influence}.\n\nDD conversations span 5 active source strategies (565 transitions), with Emotion$\\to$Obfuscation (129) as the dominant transition.\nThis aligns with DD's design of embedding harmful content within emotionally engaging contexts~\\citep{deceptivedelight2024}: the attacker establishes emotional rapport before weaving in the harmful request through obfuscation.\n\nThese trajectory signatures provide actionable information for security analysts.\nWhen the model flags a conversation, the predicted strategy sequence explains \\emph{why}: a Crescendo-style flag would show diverse strategy cycling, while a DD-style flag would show emotion-to-obfuscation concentration.\nThis interpretability layer is unavailable from MLM-only or binary models, which can detect but not characterize the persuasion mechanism.\n",
      "numLines": 191,
      "startLine": 1,
      "totalLines": 191
    }
  },
  "sourceToolAssistantUUID": "a2919d91-fae3-4317-8f80-8498012c03b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-18T08:40:09.058Z_

<details open><summary>🔧 Tool call — Read · `toolu_013uK2tLB8jhyjQXEgRXcvWs`</summary>

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
  "parentUuid": "488e3f95-0390-4d56-9e1e-93de5230202b",
  "isSidechain": false,
  "requestId": "req_011Cb9jXc9MTxTETLsXH3HuS",
  "type": "assistant",
  "uuid": "e53b0431-1794-420b-8e00-f1c82fd47ff0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSfSHLzU6USjLd5Pof5dCm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 371,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 29409,
      "output_tokens": 732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1142,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 371,
          "output_tokens": 732,
          "cache_read_input_tokens": 29409,
          "cache_creation_input_tokens": 1142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1142
          },
          "type": "message"
        }
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

_source line 33 · 2026-05-18T08:40:09.082Z_

<details><summary>↩ Tool result · `toolu_013uK2tLB8jhyjQXEgRXcvWs`</summary>

```text
1	% conclusion.tex — D024 compressed
2	
3	\section{Conclusion}
4	\label{sec:conclusion}
5	
6	DisPeD's seven controlled Stage~1 variants establish that continued pretraining is the primary mechanism for cross-attack generalization: MLM without labels bridges the dominant $\sim$62\,pp gap (vanilla 0.28 $\to$ MLM 0.91$\pm$0.12), with near-perfect early detection (F1 $\geq$ 0.97 at $K \leq 5$). Any continued pretraining bridges most of this gap; Wikipedia MLM (0.90$\pm$0.12) nearly matches jailbreak-domain MLM at full length, while jailbreak-domain text provides a meaningful advantage for early detection ($K$=2: 8\,pp gap). Classification supervision adds stability (9-class 0.997$\pm$0.005 vs.\ MLM 0.91$\pm$0.12), perturbation robustness with a three-layer attribution (classification structure provides full-length robustness, the combination of correct and fine-grained labels is required at $K$=2, and both properties contribute independently at $K$=1), and interpretability through strategy trajectories. These results reframe multi-turn jailbreak detection as primarily a domain adaptation problem.
7	
8	\paragraph{Limitations and future work.}
9	The dataset is small (500 training, 160 OOD test conversations) and synthetically generated by Qwen3-8B, which may not capture the full diversity of real-world attack strategies.
10	TF-IDF achieves F1 = 0.944 on DD, which reveals substantial lexical separability in the current evaluation data; DisPeD's advantage over bag-of-words is strongest under perturbation (0\,pp vs.\ $\sim$12\,pp degradation) and for interpretability via strategy trajectories.
11	The perturbation robustness evaluation uses $n$=76 paraphrased conversations, where tier boundaries correspond to 1--3 misclassifications; larger-scale evaluation is needed to confirm the three-layer attribution pattern.
12	Binary and scrambled variants report single-seed results; multi-seed evaluation would strengthen the comparison with 3-seed variants.
13	Only persuasion-mediated multi-turn attacks fall within scope; single-turn token-level attacks~\citep{zou2023gcg} and non-persuasive multi-turn strategies are not addressed.
14	
15	Future work should evaluate on human-generated red-teaming conversations, scale to larger multi-source datasets spanning additional attack families, and test robustness against adaptive adversaries who are aware of the domain-specific features that DisPeD relies on.
16	The finding that continued pretraining is the primary mechanism suggests that scaling training data diversity (more attack families, more generation models) may yield further improvements without architectural changes.
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e53b0431-1794-420b-8e00-f1c82fd47ff0",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "7e02ab16-8183-47e8-8f04-efead11eea13",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex",
      "content": "% conclusion.tex — D024 compressed\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nDisPeD's seven controlled Stage~1 variants establish that continued pretraining is the primary mechanism for cross-attack generalization: MLM without labels bridges the dominant $\\sim$62\\,pp gap (vanilla 0.28 $\\to$ MLM 0.91$\\pm$0.12), with near-perfect early detection (F1 $\\geq$ 0.97 at $K \\leq 5$). Any continued pretraining bridges most of this gap; Wikipedia MLM (0.90$\\pm$0.12) nearly matches jailbreak-domain MLM at full length, while jailbreak-domain text provides a meaningful advantage for early detection ($K$=2: 8\\,pp gap). Classification supervision adds stability (9-class 0.997$\\pm$0.005 vs.\\ MLM 0.91$\\pm$0.12), perturbation robustness with a three-layer attribution (classification structure provides full-length robustness, the combination of correct and fine-grained labels is required at $K$=2, and both properties contribute independently at $K$=1), and interpretability through strategy trajectories. These results reframe multi-turn jailbreak detection as primarily a domain adaptation problem.\n\n\\paragraph{Limitations and future work.}\nThe dataset is small (500 training, 160 OOD test conversations) and synthetically generated by Qwen3-8B, which may not capture the full diversity of real-world attack strategies.\nTF-IDF achieves F1 = 0.944 on DD, which reveals substantial lexical separability in the current evaluation data; DisPeD's advantage over bag-of-words is strongest under perturbation (0\\,pp vs.\\ $\\sim$12\\,pp degradation) and for interpretability via strategy trajectories.\nThe perturbation robustness evaluation uses $n$=76 paraphrased conversations, where tier boundaries correspond to 1--3 misclassifications; larger-scale evaluation is needed to confirm the three-layer attribution pattern.\nBinary and scrambled variants report single-seed results; multi-seed evaluation would strengthen the comparison with 3-seed variants.\nOnly persuasion-mediated multi-turn attacks fall within scope; single-turn token-level attacks~\\citep{zou2023gcg} and non-persuasive multi-turn strategies are not addressed.\n\nFuture work should evaluate on human-generated red-teaming conversations, scale to larger multi-source datasets spanning additional attack families, and test robustness against adaptive adversaries who are aware of the domain-specific features that DisPeD relies on.\nThe finding that continued pretraining is the primary mechanism suggests that scaling training data diversity (more attack families, more generation models) may yield further improvements without architectural changes.\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  },
  "sourceToolAssistantUUID": "e53b0431-1794-420b-8e00-f1c82fd47ff0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-18T08:40:09.645Z_

<details open><summary>🔧 Tool call — Read · `toolu_013xGbjbB1aWbny79SqLZBh6`</summary>

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
  "parentUuid": "7e02ab16-8183-47e8-8f04-efead11eea13",
  "isSidechain": false,
  "requestId": "req_011Cb9jXc9MTxTETLsXH3HuS",
  "type": "assistant",
  "uuid": "e81192b3-0763-4204-85e6-97f86c6875f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSfSHLzU6USjLd5Pof5dCm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 371,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 29409,
      "output_tokens": 732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1142,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 371,
          "output_tokens": 732,
          "cache_read_input_tokens": 29409,
          "cache_creation_input_tokens": 1142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1142
          },
          "type": "message"
        }
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

_source line 35 · 2026-05-18T08:40:09.652Z_

<details><summary>↩ Tool result · `toolu_013xGbjbB1aWbny79SqLZBh6`</summary>

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
11	\caption{LLM-as-judge zero-shot Crescendo detection (IID test set). F1 values exclude unparseable responses and represent upper bounds.}
12	\label{tab:llm_judge}
13	\begin{tabular}{@{}lccccr@{}}
14	\toprule
15	\textbf{Method} & $K$=2 & $K$=3 & $K$=5 & Full & Unparse. \\
16	\midrule
17	GPT-5.5 & .191 & .273 & .449 & .383 & 30--47\% \\
18	Qwen3-8B & .000 & .051 & .146 & .100 & 0\% \\
19	\midrule
20	9-class (ours) & \textbf{1.000} & \textbf{1.000} & \textbf{1.000} & \textbf{1.000} & 0\% \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	Table~\ref{tab:llm_judge} reports zero-shot performance for GPT-5.5 and Qwen3-8B on the IID Crescendo test set.
26	GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 of 0.191 at $K$=2 and 0.449 at $K$=5.
27	A substantial fraction (30--47\%) of responses are unparseable; F1 values exclude these and represent upper bounds.
28	Full-conversation F1 (0.383) is lower than $K$=5 F1 (0.449) because the unparseable rate grows with context length.
29	Qwen3-8B performs worse across all prefixes (F1 from 0.000 at $K$=2 to 0.100 on full conversations).
30	The failure of both a frontier commercial model and an open-weight model confirms a fundamental limitation of content-level reasoning for multi-turn jailbreak detection.
31	
32	\section{Full Cross-Attack Results by Prefix}
33	\label{sec:full_prefix}
34	
35	\begin{table*}[t]
36	\centering
37	\small
38	\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\pm$std where available.}
39	\label{tab:full_prefix}
40	\begin{tabular}{@{}lccccc@{}}
41	\toprule
42	\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\
43	\midrule
44	\multicolumn{6}{l}{\textit{IID (Crescendo)}} \\[2pt]
45	9-class (ours) & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 \\
46	MLM-only & .960 & .974 & .987 & 1.000 & 1.000 \\
47	Vanilla DeBERTa & .968$\pm$.033 & .978$\pm$.016 & .987$\pm$.000 & .982$\pm$.014 & 1.000$\pm$.000 \\
48	TF-IDF LR & 1.000 & 1.000 & 1.000 & 1.000 & 1.000 \\
49	\midrule
50	\multicolumn{6}{l}{\textit{OOD (Deceptive Delight)}} \\[2pt]
51	9-class (ours) & .990$\pm$.013 & .981$\pm$.013 & .972$\pm$.026 & .997$\pm$.005 & .997$\pm$.005 \\
52	MLM-only & .973$\pm$.019 & .993$\pm$.009 & .997$\pm$.005 & .997$\pm$.005 & .914$\pm$.115 \\
53	Vanilla DeBERTa & .575 & .438 & .360 & .311 & .284 \\
54	TF-IDF LR & -- & -- & -- & -- & .944 \\
55	\midrule
56	\multicolumn{6}{l}{\textit{OOD (FITD)}} \\[2pt]
57	9-class (ours) & 1.000 & 1.000 & -- & -- & 1.000 \\
58	Vanilla DeBERTa & .990 & 1.000 & -- & -- & 1.000 \\
59	TF-IDF LR & 1.000 & -- & -- & -- & 1.000 \\
60	\bottomrule
61	\end{tabular}
62	\end{table*}
63	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e81192b3-0763-4204-85e6-97f86c6875f2",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "fd708582-c326-4702-880d-0951187a0b54",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
      "content": "% appendix.tex — Supplementary material\n\n\\appendix\n\n\\section{LLM-as-Judge Baseline}\n\\label{sec:llm_judge}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LLM-as-judge zero-shot Crescendo detection (IID test set). F1 values exclude unparseable responses and represent upper bounds.}\n\\label{tab:llm_judge}\n\\begin{tabular}{@{}lccccr@{}}\n\\toprule\n\\textbf{Method} & $K$=2 & $K$=3 & $K$=5 & Full & Unparse. \\\\\n\\midrule\nGPT-5.5 & .191 & .273 & .449 & .383 & 30--47\\% \\\\\nQwen3-8B & .000 & .051 & .146 & .100 & 0\\% \\\\\n\\midrule\n9-class (ours) & \\textbf{1.000} & \\textbf{1.000} & \\textbf{1.000} & \\textbf{1.000} & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:llm_judge} reports zero-shot performance for GPT-5.5 and Qwen3-8B on the IID Crescendo test set.\nGPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 of 0.191 at $K$=2 and 0.449 at $K$=5.\nA substantial fraction (30--47\\%) of responses are unparseable; F1 values exclude these and represent upper bounds.\nFull-conversation F1 (0.383) is lower than $K$=5 F1 (0.449) because the unparseable rate grows with context length.\nQwen3-8B performs worse across all prefixes (F1 from 0.000 at $K$=2 to 0.100 on full conversations).\nThe failure of both a frontier commercial model and an open-weight model confirms a fundamental limitation of content-level reasoning for multi-turn jailbreak detection.\n\n\\section{Full Cross-Attack Results by Prefix}\n\\label{sec:full_prefix}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\\pm$std where available.}\n\\label{tab:full_prefix}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{IID (Crescendo)}} \\\\[2pt]\n9-class (ours) & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 \\\\\nMLM-only & .960 & .974 & .987 & 1.000 & 1.000 \\\\\nVanilla DeBERTa & .968$\\pm$.033 & .978$\\pm$.016 & .987$\\pm$.000 & .982$\\pm$.014 & 1.000$\\pm$.000 \\\\\nTF-IDF LR & 1.000 & 1.000 & 1.000 & 1.000 & 1.000 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{OOD (Deceptive Delight)}} \\\\[2pt]\n9-class (ours) & .990$\\pm$.013 & .981$\\pm$.013 & .972$\\pm$.026 & .997$\\pm$.005 & .997$\\pm$.005 \\\\\nMLM-only & .973$\\pm$.019 & .993$\\pm$.009 & .997$\\pm$.005 & .997$\\pm$.005 & .914$\\pm$.115 \\\\\nVanilla DeBERTa & .575 & .438 & .360 & .311 & .284 \\\\\nTF-IDF LR & -- & -- & -- & -- & .944 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{OOD (FITD)}} \\\\[2pt]\n9-class (ours) & 1.000 & 1.000 & -- & -- & 1.000 \\\\\nVanilla DeBERTa & .990 & 1.000 & -- & -- & 1.000 \\\\\nTF-IDF LR & 1.000 & -- & -- & -- & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
      "numLines": 63,
      "startLine": 1,
      "totalLines": 63
    }
  },
  "sourceToolAssistantUUID": "e81192b3-0763-4204-85e6-97f86c6875f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-18T08:40:09.877Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CsAGbZdqGBw5Z9bNXovsZb`</summary>

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
  "parentUuid": "fd708582-c326-4702-880d-0951187a0b54",
  "isSidechain": false,
  "requestId": "req_011Cb9jXc9MTxTETLsXH3HuS",
  "type": "assistant",
  "uuid": "a033cf21-534a-47ce-b32a-07d445155d37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSfSHLzU6USjLd5Pof5dCm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 371,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 29409,
      "output_tokens": 732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1142,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 371,
          "output_tokens": 732,
          "cache_read_input_tokens": 29409,
          "cache_creation_input_tokens": 1142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1142
          },
          "type": "message"
        }
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

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验有效性**  ### Venue 信息 - **目标会议**：EMNLP 2026 Main Conference (ARR May cycle) - **截止日期**：2026-05-25 - **页数限制**：长文 8 页（不含 references、limitat…",
  "leafUuid": "2a36d0c0-7eae-4c37-a8a2-a8bb2cd21239",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 paper review for EMNLP persuasion jailbreak detection",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Tool result

_source line 39 · 2026-05-18T08:40:10.443Z_

<details><summary>↩ Tool result · `toolu_01UiNRv55QFiJkmSEmg8kP7Y`</summary>

```text
# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence (1-5 Scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: Quite sure, unlikely to have missed critical points
- **3**: Pretty sure, but some details may be unchecked
- **2**: Willing to defend evaluation, but likely missed some details
- **1**: "Not my area, or paper is very hard to understand"

## Soundness (1-5 Scale)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong, provides sufficient support with minor improvements possible
- **3**: Acceptable, supports main claims with minor details needed
- **2**: Poor, main claims lack sufficient support
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement (1-5 Scale)
- **5**: Highly exciting, would recommend or attend presentation
- **4**: Exciting, would mention to others
- **3**: Interesting, might attend if time permits
- **2**: Potentially interesting, may resonate with some
- **1**: "Not Exciting: this paper does not resonate with me"

## Overall Assessment (1-5 Scale)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit or irrelevant to computational linguistics
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f07d7c3b-e45f-4570-a568-ccbb83081332",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "9a1596a8-f713-448f-b5ce-78c2f8d202e2",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Scoring Dimensions\n\n## Reviewer Confidence (1-5 Scale)\n- **5**: \"Positive that my evaluation is correct. I read the paper very carefully\"\n- **4**: Quite sure, unlikely to have missed critical points\n- **3**: Pretty sure, but some details may be unchecked\n- **2**: Willing to defend evaluation, but likely missed some details\n- **1**: \"Not my area, or paper is very hard to understand\"\n\n## Soundness (1-5 Scale)\n- **5**: \"Excellent: This study is one of the most thorough I have seen\"\n- **4**: Strong, provides sufficient support with minor improvements possible\n- **3**: Acceptable, supports main claims with minor details needed\n- **2**: Poor, main claims lack sufficient support\n- **1**: \"Major Issues: This study is not yet sufficiently thorough to warrant publication\"\n\n## Excitement (1-5 Scale)\n- **5**: Highly exciting, would recommend or attend presentation\n- **4**: Exciting, would mention to others\n- **3**: Interesting, might attend if time permits\n- **2**: Potentially interesting, may resonate with some\n- **1**: \"Not Exciting: this paper does not resonate with me\"\n\n## Overall Assessment (1-5 Scale)\n- **5**: Consider for Award (top 2.5%)\n- **4**: Conference acceptance\n- **3**: Findings acceptance\n- **2**: Resubmit next cycle\n- **1**: Do not resubmit or irrelevant to computational linguistics",
    "durationMs": 5225,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "f07d7c3b-e45f-4570-a568-ccbb83081332",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 40 · 2026-05-18T08:40:10.448Z_

```json
{
  "parentUuid": "9a1596a8-f713-448f-b5ce-78c2f8d202e2",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "65ab4563-f9be-400a-b27c-c9fb43407f73",
  "timestamp": "2026-05-18T08:40:10.448Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 41 · 2026-05-18T08:41:28.111Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full paper content. Let me also look at the figures for visual assessment. Let me also get the ARR review form details more carefully.

Let me now compile my review. I have the ARR review form dimensions:
- Soundness (1-5)
- Excitement (1-5)  
- Overall Assessment (1-5)
- Reviewer Confidence (1-5)

Let me now carefully analyze the paper according to the Director's specified review focus areas:

1. **实验设计严谨性**
2. **统计显著性与可靠性**
3. **方法论问题**


4. **Baseline 充分性**
5. **可复现性**

Let me think through each issue carefully.

### 1. 实验设计严谨性

The seven Stage-1 ablations are meant to isolate different factors like domain exposure, classification supervision, label quality, label granularity, and domain specificity, but I need to check whether there are confounding variables. For instance, the 9-class versus binary comparison tests granularity, but the 9-class variant uses two heads for strategy and intent while the binary setup appears different—I should verify the exact architectural differences to ensure the comparison is clean.

The scrambled labels control is well-designed since it preserves the classification structure while destroying semantic meaning, which isolates label correctness. The MLM versus classification variants properly test whether supervision beyond domain exposure matters, and the topic task control checks whether any auxiliary task works equally well. However, the Wikipedia MLM versus jailbreak MLM comparison has a potential confound: the source texts likely differ in length, style, and register, so I can't cleanly attribute performance differences to domain specificity alone.

Looking at potential confounds in the experimental setup, the different task heads have varying parameter counts—topic uses 5-class, binary uses 2-class, 9-class uses 9-class plus a binary intent head, and MLM uses its own head—which could influence how representations develop. The training signal also differs substantially: MLM sees 15% of tokens per epoch for contextual prediction while classification tasks see one label per turn, creating different gradient magnitudes. Most critically, binary and scrambled report results from a single seed (42) while the other variants average across three seeds, making direct comparisons between these groups unreliable.

The 9-class variant also gets richer supervision with both strategy and intent heads compared to binary's simpler persuasive/non-persuasive plus intent setup. There's something odd about the mean pooling result too—it achieves 1.000 on DD with seed 42, while BiGRU 9-class gets 0.997±0.005 across three seeds, which seems suspicious and might be seed-dependent rather than a genuine advantage.

The hyperparameters appear consistent across experiments, though I'm noting the Stage-2 setup details. The dataset is quite small—only 500 training samples split evenly between Crescendo jailbreak and benign, with just 80 DD test samples for out-of-distribution evaluation. At that scale, even a single misclassification meaningfully impacts the F1 scores. There's also an inconsistency in how results are reported: some use 3-seed averages while others rely on single seeds, which makes direct comparisons unreliable.

The perturbation robustness claims are particularly concerning since they're based on just 76 paraphrased conversations, and the paper itself acknowledges that tier boundaries correspond to only 1-3 misclassifications. A 2.6 percentage point difference at n=76 translates to roughly 2 misclassifications—well within noise. The entire three-layer attribution hierarchy rests on these marginal differences. Meanwhile, MLM shows high variance at 0.91±0.12, which raises questions about the stability of these findings.

Looking at the annotation methodology, the 9-class taxonomy that underpins the "correct fine-grained labels" claim was validated with Cohen's κ=0.78 on just 50 samples. While that's "substantial" agreement by standard metrics, it's a small validation set for a scheme applied across the entire training set, and the 22% disagreement rate is non-trivial.

The Stage-1 freeze in Stage-2 is a deliberate constraint that prioritizes representation quality comparison over end-to-end performance—scientifically valid but practically limiting since end-to-end fine-tuning could yield different results.

The claim that mean pooling matches BiGRU and therefore temporal modeling isn't the detection mechanism is stated confidently, but it rests on a single seed, which undermines the strength of that conclusion. The 3-seed average for BiGRU is 0.997±0.005, so the single-seed comparison at seed 42 isn't really meaningful—both methods are near-perfect on just 80 test samples. Looking at the baseline comparisons, I notice DeepContext is cited with F1=0.84 but there's no direct experimental validation, and other related methods like BIID, G-Guard, and SafeDream are only mentioned in related work without any head-to-head testing.

The experimental setup is limited to vanilla DeBERTa, TF-IDF LR, and LLM-as-judge baselines, which feels like a significant gap for an EMNLP submission—reviewers would expect comparisons with existing published multi-turn defense systems. The LLM baselines are only evaluated on IID Crescendo data too, with no OOD results, which undermines the paper's core contribution around out-of-distribution generalization. TF-IDF LR achieves 0.944 on DD versus 0.997 for the 9-class model, a 5.3 percentage point gap, though TF-IDF is admittedly much simpler.

DisPeD's claimed advantages are robustness under perturbation and interpretability, but the evidence is weak—TF-IDF only degrades by 1.3 percentage points under perturbation, which is quite small. The paper needs to make a more compelling argument for why DisPeD's added complexity is justified over these simpler baselines.

For reproducibility, the hyperparameter reporting is incomplete. Stage-1 training uses learning rate 2e-5, batch size 16, 4 epochs, and 15% MLM masking, but Stage-2 only mentions "two-layer MLP, 20 epochs" without specifying learning rate, batch size, optimizer, or other critical details like warmup steps and scheduler configuration. The intent loss weighting is α=0.3, BiGRU hidden dimension is 128, and the MLP architecture is 256→64→2 with ReLU and 0.3 dropout, but several key training parameters are still missing.

The data generation process also lacks transparency—they mention generating 250 Crescendo jailbreak and 250 benign conversations using Qwen3-8B, but don't specify the prompting strategy, temperature settings, conversation length distribution, or which topics were used for the benign conversations. Strategy annotations came from Qwen3-8B with structured prompting including definitions and examples, but the actual prompts aren't provided. Most critically, there's no mention anywhere of releasing code or data, which is a major reproducibility concern.

Looking at the overall assessment, the ablation study with seven variants is well-designed and systematically tests different factors, and it's refreshing that MLM alone bridges most of the OOD gap—partially falsifying their original hypothesis. The evidence hierarchy is clearly presented, and the strategy trajectory analysis provides interesting qualitative insights. However, there are several critical weaknesses: single-seed reporting for binary and scrambled variants undermines key comparisons, there's no direct experimental comparison with SOTA multi-turn defenses like DeepContext, BIID, G-Guard, or SafeDream, and the dataset is extremely small with only 500 training examples and 160 OOD test examples—making the three-layer attribution analysis with n=76 statistically unreliable. The claim that mean pooling equals BiGRU is overclaimed given it's based on a single seed with n=80 test samples. The annotation quality validation with n=50 and κ=0.78 is also thin for grounding the entire 9-class taxonomy, and the LLM baseline wasn't evaluated on OOD data.

Now I'm examining the figures to assess their clarity and support for the claims, and I should also verify the references in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65ab4563-f9be-400a-b27c-c9fb43407f73",
  "isSidechain": false,
  "requestId": "req_011Cb9jYFuU2VbVpKpeVvPUo",
  "type": "assistant",
  "uuid": "cfc233ed-3d56-42b6-b5f0-06765d18c904",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198WAJU1yLe71QWSuFGfSWU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 17398,
      "cache_creation_input_tokens": 1597,
      "cache_read_input_tokens": 30551,
      "output_tokens": 3510,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1597,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 17398,
          "output_tokens": 3510,
          "cache_read_input_tokens": 30551,
          "cache_creation_input_tokens": 1597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1597
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-18T08:41:28.118Z_

论文已读完。现在验证引用并查看图片，同时开始整理审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfc233ed-3d56-42b6-b5f0-06765d18c904",
  "isSidechain": false,
  "requestId": "req_011Cb9jYFuU2VbVpKpeVvPUo",
  "type": "assistant",
  "uuid": "66ee4089-626c-4bb7-95cb-204628889837",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198WAJU1yLe71QWSuFGfSWU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 17398,
      "cache_creation_input_tokens": 1597,
      "cache_read_input_tokens": 30551,
      "output_tokens": 3510,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1597,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 17398,
          "output_tokens": 3510,
          "cache_read_input_tokens": 30551,
          "cache_creation_input_tokens": 1597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1597
          },
          "type": "message"
        }
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

_source line 43 · 2026-05-18T08:41:29.486Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01Uoc1oFd3HYXYMWS7o2nRNH`</summary>

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
  "parentUuid": "66ee4089-626c-4bb7-95cb-204628889837",
  "isSidechain": false,
  "requestId": "req_011Cb9jYFuU2VbVpKpeVvPUo",
  "type": "assistant",
  "uuid": "4c2e50bb-0f01-417d-8c3d-4906b81e90cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198WAJU1yLe71QWSuFGfSWU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 17398,
      "cache_creation_input_tokens": 1597,
      "cache_read_input_tokens": 30551,
      "output_tokens": 3510,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1597,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 17398,
          "output_tokens": 3510,
          "cache_read_input_tokens": 30551,
          "cache_creation_input_tokens": 1597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1597
          },
          "type": "message"
        }
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

_source line 44 · 2026-05-18T08:41:30.417Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01URw2PzNiXtHdwZh6gEafrc`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/fig1_architecture.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c2e50bb-0f01-417d-8c3d-4906b81e90cc",
  "isSidechain": false,
  "requestId": "req_011Cb9jYFuU2VbVpKpeVvPUo",
  "type": "assistant",
  "uuid": "686ca8a2-4c14-4a30-b6e4-35d5b5bfff78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198WAJU1yLe71QWSuFGfSWU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 17398,
      "cache_creation_input_tokens": 1597,
      "cache_read_input_tokens": 30551,
      "output_tokens": 3510,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1597,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 17398,
          "output_tokens": 3510,
          "cache_read_input_tokens": 30551,
          "cache_creation_input_tokens": 1597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1597
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-18T08:41:31.441Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01KWuu4PPzDufW6rCDfuvaUb`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/fig2_cross_attack_bar.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "686ca8a2-4c14-4a30-b6e4-35d5b5bfff78",
  "isSidechain": false,
  "requestId": "req_011Cb9jYFuU2VbVpKpeVvPUo",
  "type": "assistant",
  "uuid": "db7a6995-14ad-49dc-8459-3dbad7e520e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198WAJU1yLe71QWSuFGfSWU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 17398,
      "cache_creation_input_tokens": 1597,
      "cache_read_input_tokens": 30551,
      "output_tokens": 3510,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1597,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 17398,
          "output_tokens": 3510,
          "cache_read_input_tokens": 30551,
          "cache_creation_input_tokens": 1597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1597
          },
          "type": "message"
        }
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

_source line 46 · 2026-05-18T08:41:31.856Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01NDmC3wohnyf15XNYDgqjH9`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/fig3_strategy_heatmap.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db7a6995-14ad-49dc-8459-3dbad7e520e9",
  "isSidechain": false,
  "requestId": "req_011Cb9jYFuU2VbVpKpeVvPUo",
  "type": "assistant",
  "uuid": "1c10b302-73d0-42df-b517-e8d3fd380668",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198WAJU1yLe71QWSuFGfSWU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 17398,
      "cache_creation_input_tokens": 1597,
      "cache_read_input_tokens": 30551,
      "output_tokens": 3510,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1597,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 17398,
          "output_tokens": 3510,
          "cache_read_input_tokens": 30551,
          "cache_creation_input_tokens": 1597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1597
          },
          "type": "message"
        }
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

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验有效性**  ### Venue 信息 - **目标会议**：EMNLP 2026 Main Conference (ARR May cycle) - **截止日期**：2026-05-25 - **页数限制**：长文 8 页（不含 references、limitat…",
  "leafUuid": "1c10b302-73d0-42df-b517-e8d3fd380668",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 paper review for EMNLP persuasion jailbreak detection",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Tool result

_source line 49 · 2026-05-18T08:42:05.872Z_

<details><summary>↩ Tool result · `toolu_01Uoc1oFd3HYXYMWS7o2nRNH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 36, \"total_citations\": 61, \"unique_cited_keys\": 36, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 25, \"online_not_found\": 6, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"inan2023llamaguard\", \"type\": \"article\", \"title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"authors\": \"Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer,...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"metallamaguard3_2024\", \"type\": \"misc\", \"title\": \"Llama Guard 3\", \"authors\": \"Meta AI\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"zeng2024shieldgemma\", \"type\": \"article\", \"title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"authors\": \"Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"han2024wildguard\", \"type\": \"inproceedings\", \"title\": \"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"authors\": \"Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"anthropic2025constitutional\", \"type\": \"article\", \"title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"authors\": \"Anthropic\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"deepcontext2026\", \"type\": \"article\", \"title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"authors\": \"Albrethsen, Justin and Datta, Yash and Kumar, Kunal and Rajasekar, Sharath\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"tong2025biid\", \"type\": \"article\", \"title\": \"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\", \"authors\": \"Tong, Haibo and Zhao, Dongcheng and Shen, Guobin and He, Xiang and Lin, Dachuan ...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"gguard2025\", \"type\": \"article\", \"title\": \"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\", \"authors\": \"Huang, Zixuan and Huang, Kecheng and Yin, Lihao and He, Bowei and Zhen, Huiling ...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"safedream2026\", \"type\": \"article\", \"title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"authors\": \"Yan, Bo and Lin, Weikai and Zhu, Yada and Wang, Song\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"bullwinkel2025repeng\", \"type\": \"article\", \"title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"authors\": \"Bullwinkel, Blake and Russinovich, Mark and Salem, Ahmed and Zanella-Beguelin, S...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"mann1988rst\", \"type\": \"article\", \"title\": \"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\", \"authors\": \"Mann, William C. and Thompson, Sandra A.\", \"year\": \"1988\", \"venue\": \"Text \\\\& Talk\"}, {\"key\": \"prasad2008pdtb\", \"type\": \"inproceedings\", \"title\": \"The Penn Discourse TreeBank 2.0\", \"authors\": \"Prasad, Rashmi and Dinesh, Nikhil and Lee, Alan and Miltsakaki, Eleni and Robald...\", \"year\": \"2008\", \"venue\": \"Proceedings of the International Conference on Language Resources and Evaluation\"}, {\"key\": \"stolcke2000dialogueact\", \"type\": \"article\", \"title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"authors\": \"Stolcke, Andreas and Ries, Klaus and Coccaro, Noah and Shriberg, Elizabeth and B...\", \"year\": \"2000\", \"venue\": \"Computational Linguistics\"}, {\"key\": \"austin1962speechacts\", \"type\": \"book\", \"title\": \"How to Do Things with Words\", \"authors\": \"Austin, J. L.\", \"year\": \"1962\", \"venue\": \"\"}, {\"key\": \"searle1969speechacts\", \"type\": \"book\", \"title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"authors\": \"Searle, J. R.\", \"year\": \"1969\", \"venue\": \"\"}, {\"key\": \"cialdini2001influence\", \"type\": \"book\", \"title\": \"Influence: Science and Practice\", \"authors\": \"Cialdini, Robert B.\", \"year\": \"2001\", \"venue\": \"\"}, {\"key\": \"zeng2024pap\", \"type\": \"inproceedings\", \"title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"authors\": \"Zeng, Yi and Lin, Hongpeng and Zhang, Jingwen and Yang, Diyi and Jia, Ruoxi and ...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Association for Computational Linguistics\"}, {\"key\": \"russinovich2024crescendo\", \"type\": \"inproceedings\", \"title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"authors\": \"Russinovich, Mark and Salem, Ahmed and Eldan, Ronen\", \"year\": \"2025\", \"venue\": \"USENIX Security Symposium\"}, {\"key\": \"chao2023pair\", \"type\": \"article\", \"title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"authors\": \"Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pa...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"wei2023jailbroken\", \"type\": \"inproceedings\", \"title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"authors\": \"Wei, Alexander and Haghtalab, Nika and Steinhardt, Jacob\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"hagendorff2026reasoning\", \"type\": \"article\", \"title\": \"Large Reasoning Models Are Autonomous Jailbreak Agents\", \"authors\": \"Hagendorff, Thilo and Derner, Erik and Oliver, Nuria\", \"year\": \"2026\", \"venue\": \"Nature Communications\"}, {\"key\": \"fitd2024\", \"type\": \"article\", \"title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"authors\": \"Wang, Zhenhua and Xie, Wei and Wang, Baosheng and Wang, Enze and Gui, Zhiwen and...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"deceptivedelight2024\", \"type\": \"techreport\", \"title\": \"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\", \"authors\": \"Palo Alto Networks Unit 42\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"ren2024actorattack\", \"type\": \"inproceedings\", \"title\": \"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\", \"authors\": \"Ren, Qibing and Li, Hao and Liu, Dongrui and Xie, Zhanxu and Lu, Xiaoya and Qiao...\", \"year\": \"2025\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"zou2023gcg\", \"type\": \"article\", \"title\": \"Universal and Transferable Adversarial Attacks on Aligned Language Models\", \"authors\": \"Zou, Andy and Wang, Zifan and Carlini, Nicholas and Nasr, Milad and Kolter, J. Z...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"li2024mhj\", \"type\": \"article\", \"title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"authors\": \"Li, Nathaniel and Han, Ziwen and Steneker, Ian and Primack, Willow and Goodside,...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"gururangan2018artifacts\", \"type\": \"inproceedings\", \"title\": \"Annotation Artifacts in Natural Language Inference Data\", \"authors\": \"Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and ...\", \"year\": \"2018\", \"venue\": \"Proceedings of the Conference of the North American Chapter of the Association f...\"}, {\"key\": \"niven2019probing\", \"type\": \"inproceedings\", \"title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"authors\": \"Niven, Timothy and Kao, Hung-Yu\", \"year\": \"2019\", \"venue\": \"Proceedings of the Association for Computational Linguistics\"}, {\"key\": \"nasr2025attackermovessecond\", \"type\": \"article\", \"title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\", \"authors\": \"Nasr, Milad and Carlini, Nicholas and Sitawarin, Chawin and Schulhoff, Sander V....\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"andriushchenko2024adaptive\", \"type\": \"inproceedings\", \"title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"authors\": \"Andriushchenko, Maksym and Croce, Francesco and Flammarion, Nicolas\", \"year\": \"2025\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"he2021deberta\", \"type\": \"inproceedings\", \"title\": \"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\", \"authors\": \"He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gururangan2020dontstop\", \"type\": \"inproceedings\", \"title\": \"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\", \"authors\": \"Gururangan, Suchin and Marasovi\\\\'c, Ana and Swayamdipta, Swabha and Lo, Kyle and...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 58th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"caruana1997multitask\", \"type\": \"article\", \"title\": \"Multitask Learning\", \"authors\": \"Caruana, Rich\", \"year\": \"1997\", \"venue\": \"Machine Learning\"}, {\"key\": \"phang2018stilts\", \"type\": \"article\", \"title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"authors\": \"Phang, Jason and F\\\\'evry, Thibault and Bowman, Samuel R.\", \"year\": \"2018\", \"venue\": \"arXiv preprint arXiv:1811.01088\"}, {\"key\": \"liu2019mtdnn\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"authors\": \"Liu, Xiaodong and He, Pengcheng and Chen, Weizhu and Gao, Jianfeng\", \"year\": \"2019\", \"venue\": \"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"howard2018ulmfit\", \"type\": \"inproceedings\", \"title\": \"Universal Language Model Fine-tuning for Text Classification\", \"authors\": \"Howard, Jeremy and Ruder, Sebastian\", \"year\": \"2018\", \"venue\": \"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\"}], \"tex_citations\": [{\"key\": \"russinovich2024crescendo\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"bullwinkel2025repeng\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"inan2023llamaguard\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"han2024wildguard\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"zeng2024shieldgemma\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"deepcontext2026\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"tong2025biid\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"gguard2025\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"gururangan2020dontstop\", \"file\": \"introduction.tex\", \"line\": 20, \"command\": \"citep\"}, {\"key\": \"russinovich2024crescendo\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"chao2023pair\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"wei2023jailbroken\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"zeng2024pap\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"li2024mhj\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"zou2023gcg\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"deepcontext2026\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"tong2025biid\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"gguard2025\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"safedream2026\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"inan2023llamaguard\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"metallamaguard3_2024\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"zeng2024shieldgemma\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"han2024wildguard\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"anthropic2025constitutional\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"mann1988rst\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"prasad2008pdtb\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"stolcke2000dialogueact\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"austin1962speechacts\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"searle1969speechacts\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"howard2018ulmfit\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"gururangan2020dontstop\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citet\"}, {\"key\": \"phang2018stilts\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"caruana1997multitask\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"liu2019mtdnn\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"gururangan2018artifacts\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"niven2019probing\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"nasr2025attackermovessecond\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"andriushchenko2024adaptive\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"method.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"method.tex\", \"line\": 44, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"method.tex\", \"line\": 44, \"command\": \"citep\"}, {\"key\": \"russinovich2024crescendo\", \"file\": \"experiments.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"bullwinkel2025repeng\", \"file\": \"experiments.tex\", \"line\": 48, \"command\": \"citep\"}, {\"key\": \"gururangan2020dontstop\", \"file\": \"experiments.tex\", \"line\": 102, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"experiments.tex\", \"line\": 183, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"experiments.tex\", \"line\": 186, \"command\": \"citep\"}, {\"key\": \"zou2023gcg\", \"file\": \"conclusion.tex\", \"line\": 13, \"command\": \"citep\"}], \"online_verification\": [{\"key\": \"inan2023llamaguard\", \"title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"metallamaguard3_2024\", \"title\": \"Llama Guard 3\", \"status\": \"not_found\", \"confidence\": 0.289, \"matched_title\": \"Llama Guard 3 Vision: Safeguarding Human-AI Image Understanding Conversations\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.29 below threshold 0.82\"}, {\"key\": \"zeng2024shieldgemma\", \"title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"han2024wildguard\", \"title\": \"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"WildGuard: Open One-stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=han vs api=choi\"], \"note\": \"\"}, {\"key\": \"anthropic2025constitutional\", \"title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=anthropic vs api=sharma\"], \"note\": \"\"}, {\"key\": \"deepcontext2026\", \"title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tong2025biid\", \"title\": \"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\", \"status\": \"not_found\", \"confidence\": 0.328, \"matched_title\": \"AI Alignment: A Comprehensive Survey\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"gguard2025\", \"title\": \"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\", \"status\": \"verified\", \"confidence\": 0.882, \"matched_title\": \"Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"safedream2026\", \"title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bullwinkel2025repeng\", \"title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mann1988rst\", \"title\": \"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rhetorical Structure Theory: Toward a functional theory of text organization\", \"matched_year\": \"1988\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"prasad2008pdtb\", \"title\": \"The Penn Discourse TreeBank 2.0\", \"status\": \"verified\", \"confidence\": 0.984, \"matched_title\": \"The Penn Discourse TreeBank 2.0.\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"stolcke2000dialogueact\", \"title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"matched_year\": \"2000\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"austin1962speechacts\", \"title\": \"How to Do Things with Words\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"How To Do Things With Words\", \"matched_year\": \"1975\", \"mismatch_fields\": [\"year: bib=1962 vs api=1975\"], \"note\": \"\"}, {\"key\": \"searle1969speechacts\", \"title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"matched_year\": \"1969\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cialdini2001influence\", \"title\": \"Influence: Science and Practice\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Influence: science and practice\", \"matched_year\": \"2008\", \"mismatch_fields\": [\"year: bib=2001 vs api=2008\", \"first_author: bib=cialdini vs api=giebels\"], \"note\": \"\"}, {\"key\": \"zeng2024pap\", \"title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"russinovich2024crescendo\", \"title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chao2023pair\", \"title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"year: bib=2023 vs api=2025\"], \"note\": \"\"}, {\"key\": \"wei2023jailbroken\", \"title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hagendorff2026reasoning\", \"title\": \"Large Reasoning Models Are Autonomous Jailbreak Agents\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large reasoning models are autonomous jailbreak agents\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fitd2024\", \"title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"deceptivedelight2024\", \"title\": \"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\", \"status\": \"not_found\", \"confidence\": 0.446, \"matched_title\": \"BitBypass: A New Direction in Jailbreaking Aligned Large Language Models with Bitstream Camouflage\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"ren2024actorattack\", \"title\": \"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\", \"status\": \"not_found\", \"confidence\": 0.402, \"matched_title\": \"NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-Turn LLM Jailbreaks\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.40 below threshold 0.82\"}, {\"key\": \"zou2023gcg\", \"title\": \"Universal and Transferable Adversarial Attacks on Aligned Language Models\", \"status\": \"not_found\", \"confidence\": 0.301, \"matched_title\": \"Text Data Augmentation for Deep Learning\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\"}, {\"key\": \"li2024mhj\", \"title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gururangan2018artifacts\", \"title\": \"Annotation Artifacts in Natural Language Inference Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Annotation Artifacts in Natural Language Inference Data\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"niven2019probing\", \"title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nasr2025attackermovessecond\", \"title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against Llm Jailbreaks and Prompt Injections\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"andriushchenko2024adaptive\", \"title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"he2021deberta\", \"title\": \"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DEBERTA: DECODING-ENHANCED BERT WITH DISENTANGLED ATTENTION\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gururangan2020dontstop\", \"title\": \"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\", \"status\": \"not_found\", \"confidence\": 0.492, \"matched_title\": \"From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.49 below threshold 0.82\"}, {\"key\": \"caruana1997multitask\", \"title\": \"Multitask Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multitask Learning\", \"matched_year\": \"1997\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"phang2018stilts\", \"title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liu2019mtdnn\", \"title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"howard2018ulmfit\", \"title\": \"Universal Language Model Fine-tuning for Text Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Language Model Fine-tuning for Text Classification\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c2e50bb-0f01-417d-8c3d-4906b81e90cc",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "e7a0db8e-173c-4c5b-adb5-2d9c7e622eb6",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 36, \\\"total_citations\\\": 61, \\\"unique_cited_keys\\\": 36, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 25, \\\"online_not_found\\\": 6, \\\"online_mismatch\\\": 5}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"inan2023llamaguard\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\\\", \\\"authors\\\": \\\"Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer,...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"metallamaguard3_2024\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"Llama Guard 3\\\", \\\"authors\\\": \\\"Meta AI\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"zeng2024shieldgemma\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"ShieldGemma: Generative AI Content Moderation Based on Gemma\\\", \\\"authors\\\": \\\"Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"han2024wildguard\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\\\", \\\"authors\\\": \\\"Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"anthropic2025constitutional\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\\\", \\\"authors\\\": \\\"Anthropic\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"deepcontext2026\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\\\", \\\"authors\\\": \\\"Albrethsen, Justin and Datta, Yash and Kumar, Kunal and Rajasekar, Sharath\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"tong2025biid\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\\\", \\\"authors\\\": \\\"Tong, Haibo and Zhao, Dongcheng and Shen, Guobin and He, Xiang and Lin, Dachuan ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"gguard2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\\\", \\\"authors\\\": \\\"Huang, Zixuan and Huang, Kecheng and Yin, Lihao and He, Bowei and Zhen, Huiling ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"safedream2026\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\\\", \\\"authors\\\": \\\"Yan, Bo and Lin, Weikai and Zhu, Yada and Wang, Song\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"bullwinkel2025repeng\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\\\", \\\"authors\\\": \\\"Bullwinkel, Blake and Russinovich, Mark and Salem, Ahmed and Zanella-Beguelin, S...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"mann1988rst\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\\\", \\\"authors\\\": \\\"Mann, William C. and Thompson, Sandra A.\\\", \\\"year\\\": \\\"1988\\\", \\\"venue\\\": \\\"Text \\\\\\\\& Talk\\\"}, {\\\"key\\\": \\\"prasad2008pdtb\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Penn Discourse TreeBank 2.0\\\", \\\"authors\\\": \\\"Prasad, Rashmi and Dinesh, Nikhil and Lee, Alan and Miltsakaki, Eleni and Robald...\\\", \\\"year\\\": \\\"2008\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Language Resources and Evaluation\\\"}, {\\\"key\\\": \\\"stolcke2000dialogueact\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\\\", \\\"authors\\\": \\\"Stolcke, Andreas and Ries, Klaus and Coccaro, Noah and Shriberg, Elizabeth and B...\\\", \\\"year\\\": \\\"2000\\\", \\\"venue\\\": \\\"Computational Linguistics\\\"}, {\\\"key\\\": \\\"austin1962speechacts\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"How to Do Things with Words\\\", \\\"authors\\\": \\\"Austin, J. L.\\\", \\\"year\\\": \\\"1962\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"searle1969speechacts\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Speech Acts: An Essay in the Philosophy of Language\\\", \\\"authors\\\": \\\"Searle, J. R.\\\", \\\"year\\\": \\\"1969\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"cialdini2001influence\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Influence: Science and Practice\\\", \\\"authors\\\": \\\"Cialdini, Robert B.\\\", \\\"year\\\": \\\"2001\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\\\", \\\"authors\\\": \\\"Zeng, Yi and Lin, Hongpeng and Zhang, Jingwen and Yang, Diyi and Jia, Ruoxi and ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"russinovich2024crescendo\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\\\", \\\"authors\\\": \\\"Russinovich, Mark and Salem, Ahmed and Eldan, Ronen\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"USENIX Security Symposium\\\"}, {\\\"key\\\": \\\"chao2023pair\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Jailbreaking Black Box Large Language Models in Twenty Queries\\\", \\\"authors\\\": \\\"Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pa...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"wei2023jailbroken\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Jailbroken: How Does LLM Safety Training Fail?\\\", \\\"authors\\\": \\\"Wei, Alexander and Haghtalab, Nika and Steinhardt, Jacob\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"hagendorff2026reasoning\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Reasoning Models Are Autonomous Jailbreak Agents\\\", \\\"authors\\\": \\\"Hagendorff, Thilo and Derner, Erik and Oliver, Nuria\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Nature Communications\\\"}, {\\\"key\\\": \\\"fitd2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\\\", \\\"authors\\\": \\\"Wang, Zhenhua and Xie, Wei and Wang, Baosheng and Wang, Enze and Gui, Zhiwen and...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"type\\\": \\\"techreport\\\", \\\"title\\\": \\\"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\\\", \\\"authors\\\": \\\"Palo Alto Networks Unit 42\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"ren2024actorattack\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\\\", \\\"authors\\\": \\\"Ren, Qibing and Li, Hao and Liu, Dongrui and Xie, Zhanxu and Lu, Xiaoya and Qiao...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"zou2023gcg\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Universal and Transferable Adversarial Attacks on Aligned Language Models\\\", \\\"authors\\\": \\\"Zou, Andy and Wang, Zifan and Carlini, Nicholas and Nasr, Milad and Kolter, J. Z...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"li2024mhj\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\\\", \\\"authors\\\": \\\"Li, Nathaniel and Han, Ziwen and Steneker, Ian and Primack, Willow and Goodside,...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"gururangan2018artifacts\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Annotation Artifacts in Natural Language Inference Data\\\", \\\"authors\\\": \\\"Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and ...\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the Conference of the North American Chapter of the Association f...\\\"}, {\\\"key\\\": \\\"niven2019probing\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Probing Neural Network Comprehension of Natural Language Arguments\\\", \\\"authors\\\": \\\"Niven, Timothy and Kao, Hung-Yu\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"nasr2025attackermovessecond\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\\\", \\\"authors\\\": \\\"Nasr, Milad and Carlini, Nicholas and Sitawarin, Chawin and Schulhoff, Sander V....\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"andriushchenko2024adaptive\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\\\", \\\"authors\\\": \\\"Andriushchenko, Maksym and Croce, Francesco and Flammarion, Nicolas\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\\\", \\\"authors\\\": \\\"He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"gururangan2020dontstop\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\\\", \\\"authors\\\": \\\"Gururangan, Suchin and Marasovi\\\\\\\\'c, Ana and Swayamdipta, Swabha and Lo, Kyle and...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 58th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"caruana1997multitask\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Multitask Learning\\\", \\\"authors\\\": \\\"Caruana, Rich\\\", \\\"year\\\": \\\"1997\\\", \\\"venue\\\": \\\"Machine Learning\\\"}, {\\\"key\\\": \\\"phang2018stilts\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\\\", \\\"authors\\\": \\\"Phang, Jason and F\\\\\\\\'evry, Thibault and Bowman, Samuel R.\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:1811.01088\\\"}, {\\\"key\\\": \\\"liu2019mtdnn\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Multi-Task Deep Neural Networks for Natural Language Understanding\\\", \\\"authors\\\": \\\"Liu, Xiaodong and He, Pengcheng and Chen, Weizhu and Gao, Jianfeng\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"howard2018ulmfit\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Universal Language Model Fine-tuning for Text Classification\\\", \\\"authors\\\": \\\"Howard, Jeremy and Ruder, Sebastian\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"russinovich2024crescendo\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"fitd2024\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"hagendorff2026reasoning\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"bullwinkel2025repeng\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"inan2023llamaguard\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"han2024wildguard\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zeng2024shieldgemma\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deepcontext2026\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"tong2025biid\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gguard2025\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gururangan2020dontstop\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"russinovich2024crescendo\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"fitd2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ren2024actorattack\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"chao2023pair\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wei2023jailbroken\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hagendorff2026reasoning\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"li2024mhj\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zou2023gcg\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deepcontext2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"tong2025biid\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gguard2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"safedream2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"inan2023llamaguard\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"metallamaguard3_2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zeng2024shieldgemma\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"han2024wildguard\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"anthropic2025constitutional\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"mann1988rst\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"prasad2008pdtb\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"stolcke2000dialogueact\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"austin1962speechacts\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"searle1969speechacts\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cialdini2001influence\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hagendorff2026reasoning\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"howard2018ulmfit\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gururangan2020dontstop\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"phang2018stilts\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"caruana1997multitask\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"liu2019mtdnn\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gururangan2018artifacts\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"niven2019probing\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"nasr2025attackermovessecond\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"andriushchenko2024adaptive\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 44, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cialdini2001influence\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 44, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"russinovich2024crescendo\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"fitd2024\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"bullwinkel2025repeng\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 48, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gururangan2020dontstop\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 102, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cialdini2001influence\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 183, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 186, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zou2023gcg\\\", \\\"file\\\": \\\"conclusion.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"inan2023llamaguard\\\", \\\"title\\\": \\\"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"metallamaguard3_2024\\\", \\\"title\\\": \\\"Llama Guard 3\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.289, \\\"matched_title\\\": \\\"Llama Guard 3 Vision: Safeguarding Human-AI Image Understanding Conversations\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.29 below threshold 0.82\\\"}, {\\\"key\\\": \\\"zeng2024shieldgemma\\\", \\\"title\\\": \\\"ShieldGemma: Generative AI Content Moderation Based on Gemma\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ShieldGemma: Generative AI Content Moderation Based on Gemma\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"han2024wildguard\\\", \\\"title\\\": \\\"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"WildGuard: Open One-stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=han vs api=choi\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"anthropic2025constitutional\\\", \\\"title\\\": \\\"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=anthropic vs api=sharma\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"deepcontext2026\\\", \\\"title\\\": \\\"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tong2025biid\\\", \\\"title\\\": \\\"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.328, \\\"matched_title\\\": \\\"AI Alignment: A Comprehensive Survey\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.33 below threshold 0.82\\\"}, {\\\"key\\\": \\\"gguard2025\\\", \\\"title\\\": \\\"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.882, \\\"matched_title\\\": \\\"Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"safedream2026\\\", \\\"title\\\": \\\"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"bullwinkel2025repeng\\\", \\\"title\\\": \\\"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mann1988rst\\\", \\\"title\\\": \\\"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Rhetorical Structure Theory: Toward a functional theory of text organization\\\", \\\"matched_year\\\": \\\"1988\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"prasad2008pdtb\\\", \\\"title\\\": \\\"The Penn Discourse TreeBank 2.0\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.984, \\\"matched_title\\\": \\\"The Penn Discourse TreeBank 2.0.\\\", \\\"matched_year\\\": \\\"2008\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"stolcke2000dialogueact\\\", \\\"title\\\": \\\"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\\\", \\\"matched_year\\\": \\\"2000\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"austin1962speechacts\\\", \\\"title\\\": \\\"How to Do Things with Words\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"How To Do Things With Words\\\", \\\"matched_year\\\": \\\"1975\\\", \\\"mismatch_fields\\\": [\\\"year: bib=1962 vs api=1975\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"searle1969speechacts\\\", \\\"title\\\": \\\"Speech Acts: An Essay in the Philosophy of Language\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Speech Acts: An Essay in the Philosophy of Language\\\", \\\"matched_year\\\": \\\"1969\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cialdini2001influence\\\", \\\"title\\\": \\\"Influence: Science and Practice\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Influence: science and practice\\\", \\\"matched_year\\\": \\\"2008\\\", \\\"mismatch_fields\\\": [\\\"year: bib=2001 vs api=2008\\\", \\\"first_author: bib=cialdini vs api=giebels\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zeng2024pap\\\", \\\"title\\\": \\\"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"russinovich2024crescendo\\\", \\\"title\\\": \\\"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chao2023pair\\\", \\\"title\\\": \\\"Jailbreaking Black Box Large Language Models in Twenty Queries\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Jailbreaking Black Box Large Language Models in Twenty Queries\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"year: bib=2023 vs api=2025\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wei2023jailbroken\\\", \\\"title\\\": \\\"Jailbroken: How Does LLM Safety Training Fail?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Jailbroken: How Does LLM Safety Training Fail?\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hagendorff2026reasoning\\\", \\\"title\\\": \\\"Large Reasoning Models Are Autonomous Jailbreak Agents\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large reasoning models are autonomous jailbreak agents\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fitd2024\\\", \\\"title\\\": \\\"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"deceptivedelight2024\\\", \\\"title\\\": \\\"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.446, \\\"matched_title\\\": \\\"BitBypass: A New Direction in Jailbreaking Aligned Large Language Models with Bitstream Camouflage\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.45 below threshold 0.82\\\"}, {\\\"key\\\": \\\"ren2024actorattack\\\", \\\"title\\\": \\\"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.402, \\\"matched_title\\\": \\\"NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-Turn LLM Jailbreaks\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.40 below threshold 0.82\\\"}, {\\\"key\\\": \\\"zou2023gcg\\\", \\\"title\\\": \\\"Universal and Transferable Adversarial Attacks on Aligned Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.301, \\\"matched_title\\\": \\\"Text Data Augmentation for Deep Learning\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.30 below threshold 0.82\\\"}, {\\\"key\\\": \\\"li2024mhj\\\", \\\"title\\\": \\\"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gururangan2018artifacts\\\", \\\"title\\\": \\\"Annotation Artifacts in Natural Language Inference Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Annotation Artifacts in Natural Language Inference Data\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"niven2019probing\\\", \\\"title\\\": \\\"Probing Neural Network Comprehension of Natural Language Arguments\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Probing Neural Network Comprehension of Natural Language Arguments\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"nasr2025attackermovessecond\\\", \\\"title\\\": \\\"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against Llm Jailbreaks and Prompt Injections\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"andriushchenko2024adaptive\\\", \\\"title\\\": \\\"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"he2021deberta\\\", \\\"title\\\": \\\"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DEBERTA: DECODING-ENHANCED BERT WITH DISENTANGLED ATTENTION\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gururangan2020dontstop\\\", \\\"title\\\": \\\"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.492, \\\"matched_title\\\": \\\"From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.49 below threshold 0.82\\\"}, {\\\"key\\\": \\\"caruana1997multitask\\\", \\\"title\\\": \\\"Multitask Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multitask Learning\\\", \\\"matched_year\\\": \\\"1997\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"phang2018stilts\\\", \\\"title\\\": \\\"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"liu2019mtdnn\\\", \\\"title\\\": \\\"Multi-Task Deep Neural Networks for Natural Language Understanding\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multi-Task Deep Neural Networks for Natural Language Understanding\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"howard2018ulmfit\\\", \\\"title\\\": \\\"Universal Language Model Fine-tuning for Text Classification\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Universal Language Model Fine-tuning for Text Classification\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 36, \"total_citations\": 61, \"unique_cited_keys\": 36, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 25, \"online_not_found\": 6, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"inan2023llamaguard\", \"type\": \"article\", \"title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"authors\": \"Inan, Hakan and Upasani, Kartikeya and Chi, Jianfeng and Rungta, Rashi and Iyer,...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"metallamaguard3_2024\", \"type\": \"misc\", \"title\": \"Llama Guard 3\", \"authors\": \"Meta AI\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"zeng2024shieldgemma\", \"type\": \"article\", \"title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"authors\": \"Zeng, Wenjun and Liu, Yuchi and Mullins, Ryan and Peran, Ludovic and Fernandez, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"han2024wildguard\", \"type\": \"inproceedings\", \"title\": \"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"authors\": \"Han, Seungju and Rao, Kavel and Ettinger, Allyson and Jiang, Liwei and Lin, Bill...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"anthropic2025constitutional\", \"type\": \"article\", \"title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"authors\": \"Anthropic\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"deepcontext2026\", \"type\": \"article\", \"title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"authors\": \"Albrethsen, Justin and Datta, Yash and Kumar, Kunal and Rajasekar, Sharath\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"tong2025biid\", \"type\": \"article\", \"title\": \"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\", \"authors\": \"Tong, Haibo and Zhao, Dongcheng and Shen, Guobin and He, Xiang and Lin, Dachuan ...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"gguard2025\", \"type\": \"article\", \"title\": \"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\", \"authors\": \"Huang, Zixuan and Huang, Kecheng and Yin, Lihao and He, Bowei and Zhen, Huiling ...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"safedream2026\", \"type\": \"article\", \"title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"authors\": \"Yan, Bo and Lin, Weikai and Zhu, Yada and Wang, Song\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"bullwinkel2025repeng\", \"type\": \"article\", \"title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"authors\": \"Bullwinkel, Blake and Russinovich, Mark and Salem, Ahmed and Zanella-Beguelin, S...\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"mann1988rst\", \"type\": \"article\", \"title\": \"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\", \"authors\": \"Mann, William C. and Thompson, Sandra A.\", \"year\": \"1988\", \"venue\": \"Text \\\\& Talk\"}, {\"key\": \"prasad2008pdtb\", \"type\": \"inproceedings\", \"title\": \"The Penn Discourse TreeBank 2.0\", \"authors\": \"Prasad, Rashmi and Dinesh, Nikhil and Lee, Alan and Miltsakaki, Eleni and Robald...\", \"year\": \"2008\", \"venue\": \"Proceedings of the International Conference on Language Resources and Evaluation\"}, {\"key\": \"stolcke2000dialogueact\", \"type\": \"article\", \"title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"authors\": \"Stolcke, Andreas and Ries, Klaus and Coccaro, Noah and Shriberg, Elizabeth and B...\", \"year\": \"2000\", \"venue\": \"Computational Linguistics\"}, {\"key\": \"austin1962speechacts\", \"type\": \"book\", \"title\": \"How to Do Things with Words\", \"authors\": \"Austin, J. L.\", \"year\": \"1962\", \"venue\": \"\"}, {\"key\": \"searle1969speechacts\", \"type\": \"book\", \"title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"authors\": \"Searle, J. R.\", \"year\": \"1969\", \"venue\": \"\"}, {\"key\": \"cialdini2001influence\", \"type\": \"book\", \"title\": \"Influence: Science and Practice\", \"authors\": \"Cialdini, Robert B.\", \"year\": \"2001\", \"venue\": \"\"}, {\"key\": \"zeng2024pap\", \"type\": \"inproceedings\", \"title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"authors\": \"Zeng, Yi and Lin, Hongpeng and Zhang, Jingwen and Yang, Diyi and Jia, Ruoxi and ...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Association for Computational Linguistics\"}, {\"key\": \"russinovich2024crescendo\", \"type\": \"inproceedings\", \"title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"authors\": \"Russinovich, Mark and Salem, Ahmed and Eldan, Ronen\", \"year\": \"2025\", \"venue\": \"USENIX Security Symposium\"}, {\"key\": \"chao2023pair\", \"type\": \"article\", \"title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"authors\": \"Chao, Patrick and Robey, Alexander and Dobriban, Edgar and Hassani, Hamed and Pa...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"wei2023jailbroken\", \"type\": \"inproceedings\", \"title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"authors\": \"Wei, Alexander and Haghtalab, Nika and Steinhardt, Jacob\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"hagendorff2026reasoning\", \"type\": \"article\", \"title\": \"Large Reasoning Models Are Autonomous Jailbreak Agents\", \"authors\": \"Hagendorff, Thilo and Derner, Erik and Oliver, Nuria\", \"year\": \"2026\", \"venue\": \"Nature Communications\"}, {\"key\": \"fitd2024\", \"type\": \"article\", \"title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"authors\": \"Wang, Zhenhua and Xie, Wei and Wang, Baosheng and Wang, Enze and Gui, Zhiwen and...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"deceptivedelight2024\", \"type\": \"techreport\", \"title\": \"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\", \"authors\": \"Palo Alto Networks Unit 42\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"ren2024actorattack\", \"type\": \"inproceedings\", \"title\": \"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\", \"authors\": \"Ren, Qibing and Li, Hao and Liu, Dongrui and Xie, Zhanxu and Lu, Xiaoya and Qiao...\", \"year\": \"2025\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"zou2023gcg\", \"type\": \"article\", \"title\": \"Universal and Transferable Adversarial Attacks on Aligned Language Models\", \"authors\": \"Zou, Andy and Wang, Zifan and Carlini, Nicholas and Nasr, Milad and Kolter, J. Z...\", \"year\": \"2023\", \"venue\": \"arXiv preprint\"}, {\"key\": \"li2024mhj\", \"type\": \"article\", \"title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"authors\": \"Li, Nathaniel and Han, Ziwen and Steneker, Ian and Primack, Willow and Goodside,...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"gururangan2018artifacts\", \"type\": \"inproceedings\", \"title\": \"Annotation Artifacts in Natural Language Inference Data\", \"authors\": \"Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and ...\", \"year\": \"2018\", \"venue\": \"Proceedings of the Conference of the North American Chapter of the Association f...\"}, {\"key\": \"niven2019probing\", \"type\": \"inproceedings\", \"title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"authors\": \"Niven, Timothy and Kao, Hung-Yu\", \"year\": \"2019\", \"venue\": \"Proceedings of the Association for Computational Linguistics\"}, {\"key\": \"nasr2025attackermovessecond\", \"type\": \"article\", \"title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\", \"authors\": \"Nasr, Milad and Carlini, Nicholas and Sitawarin, Chawin and Schulhoff, Sander V....\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"andriushchenko2024adaptive\", \"type\": \"inproceedings\", \"title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"authors\": \"Andriushchenko, Maksym and Croce, Francesco and Flammarion, Nicolas\", \"year\": \"2025\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"he2021deberta\", \"type\": \"inproceedings\", \"title\": \"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\", \"authors\": \"He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gururangan2020dontstop\", \"type\": \"inproceedings\", \"title\": \"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\", \"authors\": \"Gururangan, Suchin and Marasovi\\\\'c, Ana and Swayamdipta, Swabha and Lo, Kyle and...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 58th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"caruana1997multitask\", \"type\": \"article\", \"title\": \"Multitask Learning\", \"authors\": \"Caruana, Rich\", \"year\": \"1997\", \"venue\": \"Machine Learning\"}, {\"key\": \"phang2018stilts\", \"type\": \"article\", \"title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"authors\": \"Phang, Jason and F\\\\'evry, Thibault and Bowman, Samuel R.\", \"year\": \"2018\", \"venue\": \"arXiv preprint arXiv:1811.01088\"}, {\"key\": \"liu2019mtdnn\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"authors\": \"Liu, Xiaodong and He, Pengcheng and Chen, Weizhu and Gao, Jianfeng\", \"year\": \"2019\", \"venue\": \"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"howard2018ulmfit\", \"type\": \"inproceedings\", \"title\": \"Universal Language Model Fine-tuning for Text Classification\", \"authors\": \"Howard, Jeremy and Ruder, Sebastian\", \"year\": \"2018\", \"venue\": \"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\"}], \"tex_citations\": [{\"key\": \"russinovich2024crescendo\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"bullwinkel2025repeng\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"inan2023llamaguard\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"han2024wildguard\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"zeng2024shieldgemma\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"deepcontext2026\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"tong2025biid\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"gguard2025\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"gururangan2020dontstop\", \"file\": \"introduction.tex\", \"line\": 20, \"command\": \"citep\"}, {\"key\": \"russinovich2024crescendo\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"ren2024actorattack\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"chao2023pair\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"wei2023jailbroken\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"zeng2024pap\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"li2024mhj\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"zou2023gcg\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"deepcontext2026\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"tong2025biid\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"gguard2025\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"safedream2026\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"inan2023llamaguard\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"metallamaguard3_2024\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"zeng2024shieldgemma\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"han2024wildguard\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"anthropic2025constitutional\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"mann1988rst\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"prasad2008pdtb\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"stolcke2000dialogueact\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"austin1962speechacts\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"searle1969speechacts\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"hagendorff2026reasoning\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"howard2018ulmfit\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"gururangan2020dontstop\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citet\"}, {\"key\": \"phang2018stilts\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"caruana1997multitask\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"liu2019mtdnn\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"gururangan2018artifacts\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"niven2019probing\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"nasr2025attackermovessecond\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"andriushchenko2024adaptive\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"he2021deberta\", \"file\": \"method.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"zeng2024pap\", \"file\": \"method.tex\", \"line\": 44, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"method.tex\", \"line\": 44, \"command\": \"citep\"}, {\"key\": \"russinovich2024crescendo\", \"file\": \"experiments.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"fitd2024\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"bullwinkel2025repeng\", \"file\": \"experiments.tex\", \"line\": 48, \"command\": \"citep\"}, {\"key\": \"gururangan2020dontstop\", \"file\": \"experiments.tex\", \"line\": 102, \"command\": \"citep\"}, {\"key\": \"cialdini2001influence\", \"file\": \"experiments.tex\", \"line\": 183, \"command\": \"citep\"}, {\"key\": \"deceptivedelight2024\", \"file\": \"experiments.tex\", \"line\": 186, \"command\": \"citep\"}, {\"key\": \"zou2023gcg\", \"file\": \"conclusion.tex\", \"line\": 13, \"command\": \"citep\"}], \"online_verification\": [{\"key\": \"inan2023llamaguard\", \"title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"metallamaguard3_2024\", \"title\": \"Llama Guard 3\", \"status\": \"not_found\", \"confidence\": 0.289, \"matched_title\": \"Llama Guard 3 Vision: Safeguarding Human-AI Image Understanding Conversations\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.29 below threshold 0.82\"}, {\"key\": \"zeng2024shieldgemma\", \"title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ShieldGemma: Generative AI Content Moderation Based on Gemma\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"han2024wildguard\", \"title\": \"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"WildGuard: Open One-stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=han vs api=choi\"], \"note\": \"\"}, {\"key\": \"anthropic2025constitutional\", \"title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=anthropic vs api=sharma\"], \"note\": \"\"}, {\"key\": \"deepcontext2026\", \"title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tong2025biid\", \"title\": \"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\", \"status\": \"not_found\", \"confidence\": 0.328, \"matched_title\": \"AI Alignment: A Comprehensive Survey\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"gguard2025\", \"title\": \"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\", \"status\": \"verified\", \"confidence\": 0.882, \"matched_title\": \"Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"safedream2026\", \"title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bullwinkel2025repeng\", \"title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mann1988rst\", \"title\": \"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rhetorical Structure Theory: Toward a functional theory of text organization\", \"matched_year\": \"1988\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"prasad2008pdtb\", \"title\": \"The Penn Discourse TreeBank 2.0\", \"status\": \"verified\", \"confidence\": 0.984, \"matched_title\": \"The Penn Discourse TreeBank 2.0.\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"stolcke2000dialogueact\", \"title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\", \"matched_year\": \"2000\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"austin1962speechacts\", \"title\": \"How to Do Things with Words\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"How To Do Things With Words\", \"matched_year\": \"1975\", \"mismatch_fields\": [\"year: bib=1962 vs api=1975\"], \"note\": \"\"}, {\"key\": \"searle1969speechacts\", \"title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Speech Acts: An Essay in the Philosophy of Language\", \"matched_year\": \"1969\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cialdini2001influence\", \"title\": \"Influence: Science and Practice\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Influence: science and practice\", \"matched_year\": \"2008\", \"mismatch_fields\": [\"year: bib=2001 vs api=2008\", \"first_author: bib=cialdini vs api=giebels\"], \"note\": \"\"}, {\"key\": \"zeng2024pap\", \"title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"russinovich2024crescendo\", \"title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chao2023pair\", \"title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Jailbreaking Black Box Large Language Models in Twenty Queries\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"year: bib=2023 vs api=2025\"], \"note\": \"\"}, {\"key\": \"wei2023jailbroken\", \"title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Jailbroken: How Does LLM Safety Training Fail?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hagendorff2026reasoning\", \"title\": \"Large Reasoning Models Are Autonomous Jailbreak Agents\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large reasoning models are autonomous jailbreak agents\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fitd2024\", \"title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"deceptivedelight2024\", \"title\": \"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\", \"status\": \"not_found\", \"confidence\": 0.446, \"matched_title\": \"BitBypass: A New Direction in Jailbreaking Aligned Large Language Models with Bitstream Camouflage\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"ren2024actorattack\", \"title\": \"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\", \"status\": \"not_found\", \"confidence\": 0.402, \"matched_title\": \"NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-Turn LLM Jailbreaks\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.40 below threshold 0.82\"}, {\"key\": \"zou2023gcg\", \"title\": \"Universal and Transferable Adversarial Attacks on Aligned Language Models\", \"status\": \"not_found\", \"confidence\": 0.301, \"matched_title\": \"Text Data Augmentation for Deep Learning\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\"}, {\"key\": \"li2024mhj\", \"title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gururangan2018artifacts\", \"title\": \"Annotation Artifacts in Natural Language Inference Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Annotation Artifacts in Natural Language Inference Data\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"niven2019probing\", \"title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Probing Neural Network Comprehension of Natural Language Arguments\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nasr2025attackermovessecond\", \"title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against Llm Jailbreaks and Prompt Injections\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"andriushchenko2024adaptive\", \"title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"he2021deberta\", \"title\": \"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DEBERTA: DECODING-ENHANCED BERT WITH DISENTANGLED ATTENTION\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gururangan2020dontstop\", \"title\": \"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks\", \"status\": \"not_found\", \"confidence\": 0.492, \"matched_title\": \"From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.49 below threshold 0.82\"}, {\"key\": \"caruana1997multitask\", \"title\": \"Multitask Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multitask Learning\", \"matched_year\": \"1997\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"phang2018stilts\", \"title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sentence Encoders on STILTs: Supplementary Training on Intermediate Labeled-data Tasks\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liu2019mtdnn\", \"title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Deep Neural Networks for Natural Language Understanding\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"howard2018ulmfit\", \"title\": \"Universal Language Model Fine-tuning for Text Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Language Model Fine-tuning for Text Classification\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "4c2e50bb-0f01-417d-8c3d-4906b81e90cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验有效性**  ### Venue 信息 - **目标会议**：EMNLP 2026 Main Conference (ARR May cycle) - **截止日期**：2026-05-25 - **页数限制**：长文 8 页（不含 references、limitat…",
  "leafUuid": "e7a0db8e-173c-4c5b-adb5-2d9c7e622eb6",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 paper review for EMNLP persuasion jailbreak detection",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Tool result

_source line 52 · 2026-05-18T08:42:06.413Z_

<details><summary>↩ Tool result · `toolu_01URw2PzNiXtHdwZh6gEafrc`</summary>

```text
Error: result (94,529 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-review-reviewer-1-10e47827/cbedc5e7-b345-430f-bdbb-8301dad12636/tool-results/mcp-agent-ml-research-pdf_to_images-1779093726410.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-review-reviewer-1-10e47827/cbedc5e7-b345-430f-bdbb-8301dad12636/tool-results/mcp-agent-ml-research-pdf_to_images-1779093726410.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "686ca8a2-4c14-4a30-b6e4-35d5b5bfff78",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "a9127f8d-46fb-4b4c-abb8-ab96ae80169a",
  "toolUseResult": "Error: result (94,529 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-review-reviewer-1-10e47827/cbedc5e7-b345-430f-bdbb-8301dad12636/tool-results/mcp-agent-ml-research-pdf_to_images-1779093726410.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-review-reviewer-1-10e47827/cbedc5e7-b345-430f-bdbb-8301dad12636/tool-results/mcp-agent-ml-research-pdf_to_images-1779093726410.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/_pdf_images/fig1_architecture_p1.png\", \"base64\": \"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\", \"width\": 1038, \"height\": 373, \"size_kb\": 68.8}], \"total_pages\": 1, \"rendered_pages\": 1, \"dpi\": 200, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "686ca8a2-4c14-4a30-b6e4-35d5b5bfff78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-18T08:42:06.463Z_

<details><summary>↩ Tool result · `toolu_01KWuu4PPzDufW6rCDfuvaUb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/_pdf_images/fig2_cross_attack_bar_p1.png\", \"base64\": \"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\", \"width\": 614, \"height\": 482, \"size_kb\": 31.0}], \"total_pages\": 1, \"rendered_pages\": 1, \"dpi\": 200, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db7a6995-14ad-49dc-8459-3dbad7e520e9",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "ed185603-db98-4960-9027-e31aba715a50",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"images\\\": [{\\\"page\\\": 1, \\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/_pdf_images/fig2_cross_attack_bar_p1.png\\\", \\\"base64\\\": \\\"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\\\", \\\"width\\\": 614, \\\"height\\\": 482, \\\"size_kb\\\": 31.0}], \\\"total_pages\\\": 1, \\\"rendered_pages\\\": 1, \\\"dpi\\\": 200, \\\"output_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/_pdf_images\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/_pdf_images/fig2_cross_attack_bar_p1.png\", \"base64\": \"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\", \"width\": 614, \"height\": 482, \"size_kb\": 31.0}], \"total_pages\": 1, \"rendered_pages\": 1, \"dpi\": 200, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "db7a6995-14ad-49dc-8459-3dbad7e520e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验有效性**  ### Venue 信息 - **目标会议**：EMNLP 2026 Main Conference (ARR May cycle) - **截止日期**：2026-05-25 - **页数限制**：长文 8 页（不含 references、limitat…",
  "leafUuid": "ed185603-db98-4960-9027-e31aba715a50",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 paper review for EMNLP persuasion jailbreak detection",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Tool result

_source line 56 · 2026-05-18T08:42:06.937Z_

<details><summary>↩ Tool result · `toolu_01NDmC3wohnyf15XNYDgqjH9`</summary>

```text
Error: result (203,874 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-review-reviewer-1-10e47827/cbedc5e7-b345-430f-bdbb-8301dad12636/tool-results/mcp-agent-ml-research-pdf_to_images-1779093726934.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-review-reviewer-1-10e47827/cbedc5e7-b345-430f-bdbb-8301dad12636/tool-results/mcp-agent-ml-research-pdf_to_images-1779093726934.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c10b302-73d0-42df-b517-e8d3fd380668",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "ee9e1ff7-a791-4231-b8cb-a16dbc359cdd",
  "toolUseResult": "Error: result (203,874 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-review-reviewer-1-10e47827/cbedc5e7-b345-430f-bdbb-8301dad12636/tool-results/mcp-agent-ml-research-pdf_to_images-1779093726934.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-review-reviewer-1-10e47827/cbedc5e7-b345-430f-bdbb-8301dad12636/tool-results/mcp-agent-ml-research-pdf_to_images-1779093726934.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/_pdf_images/fig3_strategy_heatmap_p1.png\", \"base64\": \"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8PN137tULCE+nn+0j9IWN91RQyw+XLWUq2BX25pipGulkth3gMCCfTcloqMTL6Po7kSPJzq9PM8zfPhwMc8PP/zgNh6o1u7YsWNivS1btvTrevXBvgMAABgE+2487733ntbaif/u3Lkzz/Pk1NpZZt9FXye6O9HjaYvWt3bYdwAAAIP41b7/WrnSyepVA0J/7Lupwb47ox0dNXDgwMqVK4eFhSUmJuZ5qsDad88Em31//QmxltzPLa+mnVePHMgf9r1fK/F01E0rPO+S377Ht2ymKkr62tXX9Ki0hc7TMCTc3Rb77gU/2/fB1UuLj+fudhft+39rl3Oe7eO2avqaRuGFi4WGpHeti30HCCDYd+PRjo4SfZ3o7gye2Siw9t0z2HcAAIB8B/bdeBo3bix6kjFjxoj/Pv7443meJ+D23S3YdwAAgHwH9p34Euy7Mz179hTvqo0bN2rnn3/33XfdCk6fPj1jxgzPHaxiRIyLXtlVExERoc0wIzuuU767dtGeO3fuww8/fPjhhwcOHDhr1qzMzEzP7dm3b99LL730wAMP9O/f/7333ktKSnIrENOKycWNP//8U1T26dNn4sSJYlHMJsYXL16sla1YsWLQoEFivR07dpxxKWLyn3/+WdzYvXu356pjYmLEXQcPHrzW11CLf+177+bq/l3q+RT7I61zrHm8m9gMR8zqfGDfuzdwLF+oqqoy7tH8aN+THh0ktjDl1VcS+9yXtnB++sb1qbNmJHRun8tDErvd7UhJzty106xtwL77zrY2NcMLFmheuoi920WzfncF56HwJ++O1pf1q1pKDP7eNgr7DhBAsO/GIzox7ZzzorsTN0Sn51mj79NcOXTokBjfunWrtvjpp5/ecccdYoaRI0e6Wqnz589nXWNrFxsbO3XqVFEjHjVu3DjRv7kVrF27VswsmsnExMS33377oYceEsUXLlxwa+1+++23SZMmifVGRUW5tkc89siRI+LG6tWrPVf9119/ibvWrFlzjS/h5WDfAQAADIJ9N5hdu3aJhuT2228XfVexYsXKli3r2XEtXbrU1ae5IhbFoLhLW8yltdPbd9F6DR06tG/fvmIxISHBc3syMjI+++yzIUOG3H///aNGjRINp1vBvn37xMyic1MURXT1AwYMeOCBB7S9cGJycZe2/Tm1dqIJFDfmzp3rueq0tDRx17x58/L2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efPmWfv07du3ZMmSOstzktCo77fccov8lD/99NNc9lGPP123bp36VM2pHTp08N5nyZIlsrFixYrWFp36/sorr8in06ZN87ekCRMmyA41a9a8aM/2oWHDhvKF8rtlbQmwvss9loisx8weOnTIe7cGDS48aMV68VX1ey94P1ZXaNasmWycNWtW7sujviNiINpe33e2rBIfl++KmKjFTa7zOWlInbIX/kzUu9p748hbymXfSH23dKC+Ly5QNe3gkbO79i2KrXzRc9vw6PNybjteHUh9vxzqe48ePeQyPvXUU7nso8r60KFD1aeqvleuXNn7DXqOHTtWokSJyMhI79ehyvFobCCHaC862u3ZsycmJiYuLs57SAuEN954Q855/Pjx1pYA63tGRoaaaX1mtl69esnGTp06WVvUbomJid67vfXWW7JRdr7oCnMf7ajviIiIOoZ9fc/DaKfqe758+bZs2eK9W/PmzWW796vK57m+y/gU4fUSmDlSo0YN2WfixIkXu4j/QeCjnU99d2y0o74jIiIGT+p7IORe38uXLy+nJicne2/84IMPZOPjjz9ubbnyyitfe+0169PGjRu3atXKluU5QGjU98qVK190GlaPALWeYq7m1OzvE68GUOvxpDr1Xf0qtGnTxt/bDKjDxN4Pqs2FQ4cO/f7770lZyD2WCK9HBHsCru/q3kvHjh19dlOPA7B+L9Xvfbly5Xx269Onj2wfOXJk7ktNTU1d6YdJkyZR3xFRaW9933R/5YqFYovGRi3Jlt7F3tWulBuf7xpe471xRsOKsvHtmmWo7znqQH1f3+a5C390+g8P5Nz++MeF0eqvfh9S3y+H+q4GmOeeey6XfeSeTITXq76rsapfv345ntWYMWOsLXmu7xcd7UaNGhWR7cGd/khJSVm3bp0a7YYMGSJf+MILL/gs+6L1XSZb9ZgDn912794t20uUKGFtUaOveuqYxfz5833ut/jD32gnUN8RERE1Dfv6nofRTh2/uueee3x2U69F9Mgjj1hb8lzfV6xYEZHtrRi9kVFNdrjmmmsuegE9eR3tfOq7Y6OdLNXfaFe79g3Ud0RERB2DW99X/D/P3qGumPCUQ/V969atEVkvBeSzffXq1bI9Pj7e2pKYmFi4cOHFixdnZmaOHj06MjJy0aJFtizPAUKjvt96661ZB/4+8rdDenq6+tW0BlM1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oIsXL7b22b9//1VXXeX9yBTqOyI6oCv1PXhS3w2X+h5yJCUlxcbGyiUdPHiw93aZkXr16qWmvj179ljbVX3Pnz+/93OPlixZImNP8eLFredRefzUdzUuyjhnbZHzUe+vaR0PvehoJyNipUqVInJ68Xlr4CxXrlxMTIz3AWIZCAsUKOAzcA4cODD7Zffk9MSppk2bRvznk/tl4pVpVja+88471kbqOyIiorFeDvX9Ukc7dZTP59jXoUOHypcv73P4K8f6Hshot2vXLhnefNbZpEkT2Wfu3LnqU/Vs+I4dO/rsZtdo51PfPQaMdtR3RERETanvgZBLfZ8378KRz3r16vlsP3PmjGyXkdI79YYuIVPfPX8/iDUyMrJ169bvv//+iBEjunbtWqZMGdlYo0YN7yHe8/ecKttvu+22MWPGfP31188880xUVJT8Z2/YsMHazd9bvL/wwguqi48aNWrSpElPP/10vnz51Mu/W8dD5bfwhhtuePnll7/88sspU6aMGzeufv36skOnTp2s81G9X+4AyKg9efJkuVORmJhYrVo1a3CvU6dORNbrXE3MQuZ+WaQs2+ceyAcffKAOJXfOwhrcsx+iVW+ZULBgwb59+8qqhg0bpt47yvvlvKjviOiA1HfDpb4b62VS34Vp06blz58/IuvNg/r16ydD16uvvlq9enXZcsUVV/g84FLVd5mRrr766sGDB8uQ89Zbb6ljrN4jk8dPfVeHPosXLy7fSH2tfKxeW8gaqwIZ7WRVsuaYmJgnn3xS/o9kNxn27r77bmt8Uu8fpGZIObV3795FixZVM6T3wLlmzRr1GM327dur6e7o0aOenEa71atXq+ffd+zYUQZamfTUqm666SbrtUk91HdERESDvRzqu+cSRztV3+vWrStf0r17d5maPvroI5nEZONTTz3lvWeO9T2Q0U6+hWx85plnPvvsM9ln0qRJMr+pp5hbcX3fvn2q9zdq1EgNbyNHjpTZSSY0tYPmaJe9vrs+2lHfERERNQ1yfX/Ts2+4KzpW33fv3i0nlSpVyud1jNSrAVWrVs2WBbhOKNV3T9YT0GvWrBnhhUzSr732mvcTnhRqTt21a5d6PKxChv5ly5Z57+avvp87d04mZusLr776apmYfY6HDh48+Morr/RejNyd6NGjh/ez7YWJEyfKl3vvJr89agoXduzY4X2JypYt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\", \"width\": 2687, \"height\": 886, \"size_kb\": 148.9}], \"total_pages\": 1, \"rendered_pages\": 1, \"dpi\": 200, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "1c10b302-73d0-42df-b517-e8d3fd380668",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验有效性**  ### Venue 信息 - **目标会议**：EMNLP 2026 Main Conference (ARR May cycle) - **截止日期**：2026-05-25 - **页数限制**：长文 8 页（不含 references、limitat…",
  "leafUuid": "ee9e1ff7-a791-4231-b8cb-a16dbc359cdd",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 paper review for EMNLP persuasion jailbreak detection",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Assistant

_source line 59 · 2026-05-18T08:42:36.781Z_

<details><summary>Logged reasoning block</summary>

```text
The fig1 and fig3 images were too large to read directly. Let me try to view them via the saved paths. But actually, for the purpose of this review, I've read all the LaTeX source code including the text descriptions of figures, and I can see fig2 (the cross-attack bar chart). The key content I need is already available from the source code.

Let me now read the fig2 image that was returned successfully, and also try to check the fig1 and fig3 images.

Actually, looking at the results:
- fig1_architecture.pdf: Too large, saved to file
- fig2_cross_attack_bar.pdf: Successfully returned as base64


- fig3_strategy_heatmap.pdf: Too large, saved to file

I've got the complete paper text and references, so I have what I need to write a thorough review. Let me start compiling my assessment, beginning with verifying the references—I found 25 that check out, 6 that don't appear on OpenAlex, and 5 with mismatches.

The missing ones like gururangan2020dontstop are likely just coverage gaps in OpenAlex since they're well-established papers, while the mismatches are mostly minor issues with first author names or publication years on multi-author works. Now I'm ready to focus my review on the experimental rigor, statistical significance, and reliability of the findings.

I'm structuring my assessment around the ARR dimensions: soundness is 3/5 because while the core design is solid, there are notable statistical and methodological weaknesses that undermine the conclusions; excitement is also 3/5 since the research question about cross-attack generalization is compelling and the insight about MLM being partially sufficient is valuable, but the limited scale and incomplete baselines diminish the impact; overall I'd rate it 3/5 as a findings paper with merit but execution problems that prevent acceptance at a top venue; and I'm fairly confident in this assessment at 4/5.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee9e1ff7-a791-4231-b8cb-a16dbc359cdd",
  "isSidechain": false,
  "requestId": "req_011Cb9jgqy49dZxp3U5YCRAx",
  "type": "assistant",
  "uuid": "c3828fb3-74b2-4330-9b9a-83209717fda4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQsbWRpcUaAS4G93Fhmzoi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 68565,
      "cache_read_input_tokens": 32148,
      "output_tokens": 882,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 68565,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 882,
          "cache_read_input_tokens": 32148,
          "cache_creation_input_tokens": 68565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 68565
          },
          "type": "message"
        }
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

_source line 60 · 2026-05-18T08:42:36.783Z_

现在查看图片。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3828fb3-74b2-4330-9b9a-83209717fda4",
  "isSidechain": false,
  "requestId": "req_011Cb9jgqy49dZxp3U5YCRAx",
  "type": "assistant",
  "uuid": "7077e584-17f9-4ae5-8352-140aac5a062b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQsbWRpcUaAS4G93Fhmzoi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 68565,
      "cache_read_input_tokens": 32148,
      "output_tokens": 882,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 68565,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 882,
          "cache_read_input_tokens": 32148,
          "cache_creation_input_tokens": 68565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 68565
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-18T08:42:36.879Z_

<details open><summary>🔧 Tool call — Read · `toolu_011Tg9ZU3mP4wF189BrASSVJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/_pdf_images/fig2_cross_attack_bar_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7077e584-17f9-4ae5-8352-140aac5a062b",
  "isSidechain": false,
  "requestId": "req_011Cb9jgqy49dZxp3U5YCRAx",
  "type": "assistant",
  "uuid": "c2f40800-e936-4b5b-80e1-fa4b178251b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQsbWRpcUaAS4G93Fhmzoi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 68565,
      "cache_read_input_tokens": 32148,
      "output_tokens": 882,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 68565,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 882,
          "cache_read_input_tokens": 32148,
          "cache_creation_input_tokens": 68565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 68565
          },
          "type": "message"
        }
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

_source line 62 · 2026-05-18T08:42:36.915Z_

<details><summary>↩ Tool result · `toolu_011Tg9ZU3mP4wF189BrASSVJ`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2f40800-e936-4b5b-80e1-fa4b178251b3",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "bc9a702c-7c4e-402b-b855-4b27dcb5e57d",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 31753,
      "dimensions": {
        "originalWidth": 614,
        "originalHeight": 482,
        "displayWidth": 614,
        "displayHeight": 482
      }
    }
  },
  "sourceToolAssistantUUID": "c2f40800-e936-4b5b-80e1-fa4b178251b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 63_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验有效性**  ### Venue 信息 - **目标会议**：EMNLP 2026 Main Conference (ARR May cycle) - **截止日期**：2026-05-25 - **页数限制**：长文 8 页（不含 references、limitat…",
  "leafUuid": "bc9a702c-7c4e-402b-b855-4b27dcb5e57d",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 paper review for EMNLP persuasion jailbreak detection",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Assistant

_source line 65 · 2026-05-18T08:42:45.970Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I can see fig2 clearly. It shows the cross-attack bar chart (actually a line chart with error bars) for OOD Deceptive Delight. The three variants shown are:
- Vanilla DeBERTa (gray, dotted) - degrades from ~0.58 at K=1 to ~0.28 at Full
- 9-class Persuasion (blue, solid) - stable around 0.97-1.00 across all prefixes
- MLM-only (DAPT) (orange, dashed) - high early (~0.97-0.99) but drops at Full to ~0.91 with large error bars


The visualization effectively demonstrates the robustness difference between approaches, with the error bars making the uncertainty clear. Let me check the other figures now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc9a702c-7c4e-402b-b855-4b27dcb5e57d",
  "isSidechain": false,
  "requestId": "req_011Cb9jj4B5RE6Xwqx8DnNup",
  "type": "assistant",
  "uuid": "56a7a439-dbef-468b-9d12-68c6b031db01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171vxUsDUyTT78RjnHDnAhW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1301,
      "cache_read_input_tokens": 100713,
      "output_tokens": 324,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1301,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 324,
          "cache_read_input_tokens": 100713,
          "cache_creation_input_tokens": 1301,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1301
          },
          "type": "message"
        }
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

_source line 66 · 2026-05-18T08:42:45.982Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JqaksQibPJrv5sVpMj4QNo`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/_pdf_images/",
  "description": "List generated PDF image files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56a7a439-dbef-468b-9d12-68c6b031db01",
  "isSidechain": false,
  "requestId": "req_011Cb9jj4B5RE6Xwqx8DnNup",
  "type": "assistant",
  "uuid": "f700c8b4-5848-4f8c-83f8-1093842e83ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171vxUsDUyTT78RjnHDnAhW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1301,
      "cache_read_input_tokens": 100713,
      "output_tokens": 324,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1301,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 324,
          "cache_read_input_tokens": 100713,
          "cache_creation_input_tokens": 1301,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1301
          },
          "type": "message"
        }
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

_source line 67 · 2026-05-18T08:42:46.164Z_

<details><summary>↩ Tool result · `toolu_01JqaksQibPJrv5sVpMj4QNo`</summary>

```text
fig1_architecture_p1.png
fig2_cross_attack_bar_p1.png
fig3_strategy_heatmap_p1.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f700c8b4-5848-4f8c-83f8-1093842e83ba",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "bb388e1b-7890-417b-8d37-636d5e5b2892",
  "toolUseResult": {
    "stdout": "fig1_architecture_p1.png\nfig2_cross_attack_bar_p1.png\nfig3_strategy_heatmap_p1.png",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f700c8b4-5848-4f8c-83f8-1093842e83ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-18T08:42:49.962Z_

<details open><summary>🔧 Tool call — Read · `toolu_015MHttJkrviRbRrozZQXwek`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/_pdf_images/fig1_architecture_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb388e1b-7890-417b-8d37-636d5e5b2892",
  "isSidechain": false,
  "requestId": "req_011Cb9jjjiMDspL876CPvSwa",
  "type": "assistant",
  "uuid": "346899ea-9625-4b86-b5ae-be959eb86f83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLPMiMou9XUvCRV17fjdnx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 102014,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 102014,
          "cache_creation_input_tokens": 373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 373
          },
          "type": "message"
        }
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

_source line 69 · 2026-05-18T08:42:49.970Z_

<details><summary>↩ Tool result · `toolu_015MHttJkrviRbRrozZQXwek`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "346899ea-9625-4b86-b5ae-be959eb86f83",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "ca0c80f0-5d33-4f36-9e22-2e7676721bd0",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 70500,
      "dimensions": {
        "originalWidth": 1038,
        "originalHeight": 373,
        "displayWidth": 1038,
        "displayHeight": 373
      }
    }
  },
  "sourceToolAssistantUUID": "346899ea-9625-4b86-b5ae-be959eb86f83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-18T08:42:50.323Z_

<details open><summary>🔧 Tool call — Read · `toolu_014ByKmBwjFMuSMQKoqGQn6G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper/_pdf_images/fig3_strategy_heatmap_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca0c80f0-5d33-4f36-9e22-2e7676721bd0",
  "isSidechain": false,
  "requestId": "req_011Cb9jjjiMDspL876CPvSwa",
  "type": "assistant",
  "uuid": "6b924c92-7754-466a-ab0d-5de5621fa601",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLPMiMou9XUvCRV17fjdnx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 102014,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 102014,
          "cache_creation_input_tokens": 373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 373
          },
          "type": "message"
        }
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

_source line 71_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验有效性**  ### Venue 信息 - **目标会议**：EMNLP 2026 Main Conference (ARR May cycle) - **截止日期**：2026-05-25 - **页数限制**：长文 8 页（不含 references、limitat…",
  "leafUuid": "6b924c92-7754-466a-ab0d-5de5621fa601",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Runtime record

_source line 72_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 paper review for EMNLP persuasion jailbreak detection",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Tool result

_source line 73 · 2026-05-18T08:42:50.917Z_

<details><summary>↩ Tool result · `toolu_014ByKmBwjFMuSMQKoqGQn6G`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b924c92-7754-466a-ab0d-5de5621fa601",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "f28c398a-293c-4a78-be52-2de2624ac3f3",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 152503
    }
  },
  "sourceToolAssistantUUID": "6b924c92-7754-466a-ab0d-5de5621fa601",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 74 · 2026-05-18T08:42:50.920Z_

```json
{
  "parentUuid": "f28c398a-293c-4a78-be52-2de2624ac3f3",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "31742bb0-b5fd-4356-99dc-8a99b9d61ed8",
  "timestamp": "2026-05-18T08:42:50.920Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 75_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验有效性**  ### Venue 信息 - **目标会议**：EMNLP 2026 Main Conference (ARR May cycle) - **截止日期**：2026-05-25 - **页数限制**：长文 8 页（不含 references、limitat…",
  "leafUuid": "31742bb0-b5fd-4356-99dc-8a99b9d61ed8",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Runtime record

_source line 76_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 paper review for EMNLP persuasion jailbreak detection",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Assistant

_source line 77 · 2026-05-18T08:43:46.339Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need to write a comprehensive review. Let me compile my findings:

**Paper read**: Complete (abstract, introduction, related work, method, experiments, conclusion, appendix)
**Figures viewed**: All three (fig1_architecture, fig2_cross_attack_bar, fig3_strategy_heatmap)
**References verified**: 36 entries, 25 verified, 6 not found on OpenAlex, 5 mismatches
**ARR review form**: Retrieved and understood (Soundness 1-5, Excitement 1-5, Overall 1-5, Confidence 1-5)


**Writing in Chinese as instructed**

I'm identifying the critical issues that need to be addressed. The most fundamental problem is the inconsistency in experimental methodology—binary and scrambled baselines report results from a single seed while other methods use three seeds with mean and standard deviation, making direct comparison of their "evidence hierarchy" ranking invalid since we're comparing a single point estimate against aggregated results with variance information. There's also a missing critical issue that appears to be cut off. direct experimental comparisons with SOTA multi-turn defenses** - The paper discusses DeepContext (F1=0.84), BIID, G-Guard, and SafeDream in Related Work but never runs head-to-head experiments. For EMNLP, simply citing numbers from other papers without standardized evaluation is insufficient. The only actual baselines are vanilla DeBERTa, TF-IDF LR, and LLM-as-judge.

3. **Dataset scale insufficient for the claims made** - 500 training conversations (250 jailbreak + 250 benign), 160 OOD test (80 FITD + 80 DD), 76 IID test. With n=80 DD test samples, each misclassification changes F1 by ~1.25pp. The three-layer robustness attribution (Table 4) is built on n=76 paraphrased conversations where tier boundaries correspond to 1-3 misclassifications, so a 2.6pp difference represents only ~2 samples—well within noise margins.

4. **The three-layer robustness attribution lacks statistical rigor** - The performance deltas (2.6pp, 5.3pp, 9.2pp) translate to roughly 2, 4, and 7 misclassifications respectively on the n=76 sample set, yet the paper constructs an elaborate three-layer theory around these differences without any significance testing.

5. **Mean pooling = BiGRU claim overclaimed** - Table 3 shows mean pooling achieves F1=1.000 on both DD-

Full and DD-K=2 with a single seed (42), while the 9-class BiGRU achieves 0.997±0.005 across 3 seeds on n=80 test samples. The causal claim that "detection relies on per-turn representations rather than their sequential order" is built on this single-seed comparison.

The annotation quality for strategy labels (Cohen's κ=0.78 on only 50 turns across 9 classes) is another concern—some classes likely have minimal representation, yet the entire three-layer advantage depends on these labels being reliable. Additionally, the paper cites SOTA defenses like DeepContext and SafeDream in Related Work but never runs direct head-to-head experiments, relying instead only on vanilla baselines and LLM-as-judge comparisons.

The LLM baselines themselves are only evaluated on IID Crescendo, not on OOD splits, which undermines the comparison given that OOD generalization is the paper's core contribution. Meanwhile, TF-IDF LR achieves 0.944 on DD—only 5.3pp below the 9-class model—and degrades just 1.3pp under perturbation, raising questions about whether the complex architecture is necessary. The perturbation test itself is statistically weak with n=76 samples, and there's no commitment to releasing code or data.

The Stage-1 freeze design choice isn't justified beyond ensuring "comparable embeddings," but this limits practical applicability and no end-to-end fine-tuning experiment is conducted. The FITD evaluation is also superficial—Table 7 shows near-perfect F1 scores (≥0.990) for both settings, making it uninformative as an OOD test, so the OOD claims rest almost entirely on DD results.

There are also some presentation issues: Figure 1 has overlapping headers, Figure 3's heatmap is too small with illegible axis labels, a few bibliography entries have year mismatches, and the paper doesn't address computational costs across variants. On the positive side, the research question is well-motivated, the paper refreshingly reports a partially falsified hypothesis, and the 7-variant ablation systematically explores multiple factors. The evidence hierarchy is clearly presented, the domain-adaptive pretraining finding aligns with established NLP work, and the strategy trajectory analysis offers useful qualitative insights into attack family differences.

My initial assessment was harsh on soundness due to single-seed runs and tiny sample sizes, but reconsidering the genuine strengths—the well-formulated research question, thoughtful ablation design despite execution gaps, and the interesting MLM finding connecting to domain-adaptive pretraining literature—I'm adjusting my scores upward. The paper shows self-awareness about its limitations, which counts for something.

But then I'm second-guessing myself again. Looking at the ARR rubric more carefully, soundness 2 means "poor, main claims lack sufficient support" while soundness 3 means "acceptable, supports main claims with minor details needed." The problems I've identified aren't minor—the three-layer attribution lacks statistical rigor, and the evidence hierarchy comparison is fundamentally undermined by the inconsistency between single-seed and multi-seed results. These are core soundness issues, not peripheral ones. I'm settling on soundness 2/5, excitement 3/5, overall 2/5 for resubmission, with high confidence in this assessment.

The paper tackles an interesting problem and the direction is promising, but the execution has too many fundamental gaps to warrant acceptance right now—it needs substantial revision.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31742bb0-b5fd-4356-99dc-8a99b9d61ed8",
  "isSidechain": false,
  "requestId": "req_011Cb9jk61EqLbcnoGSza5mU",
  "type": "assistant",
  "uuid": "3b777540-52e7-4c5c-bdf2-ae170a1a5fb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6av3gXBi9fvMGKnN2JUh2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1094,
      "cache_read_input_tokens": 102387,
      "output_tokens": 2257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1094,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2257,
          "cache_read_input_tokens": 102387,
          "cache_creation_input_tokens": 1094,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1094
          },
          "type": "message"
        }
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

_source line 78 · 2026-05-18T08:43:47.175Z_

全部材料已读完。论文全文（abstract、introduction、related work、method、experiments、conclusion、appendix）、三张图、引用验证结果均已查看。现在搜索 ARR reviewer guidelines 的详细评分标准后撰写审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b777540-52e7-4c5c-bdf2-ae170a1a5fb7",
  "isSidechain": false,
  "requestId": "req_011Cb9jk61EqLbcnoGSza5mU",
  "type": "assistant",
  "uuid": "e6fc79c6-9b2f-4dc7-bfab-70df00774564",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6av3gXBi9fvMGKnN2JUh2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1094,
      "cache_read_input_tokens": 102387,
      "output_tokens": 2257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1094,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2257,
          "cache_read_input_tokens": 102387,
          "cache_creation_input_tokens": 1094,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1094
          },
          "type": "message"
        }
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

_source line 79 · 2026-05-18T08:43:49.500Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xa1uwKoLYLaqDF2b7suTbi`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines, especially: what reviewers should focus on, what counts as a good/bad review, how to assess soundness, novelty, and reproducibility. Also extract any guidance about statistical rigor, baseline comparisons, and dataset adequacy."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6fc79c6-9b2f-4dc7-bfab-70df00774564",
  "isSidechain": false,
  "requestId": "req_011Cb9jk61EqLbcnoGSza5mU",
  "type": "assistant",
  "uuid": "aa1e3ff8-9ac1-4460-a611-0879f53a4045",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6av3gXBi9fvMGKnN2JUh2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1094,
      "cache_read_input_tokens": 102387,
      "output_tokens": 2257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1094,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2257,
          "cache_read_input_tokens": 102387,
          "cache_creation_input_tokens": 1094,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1094
          },
          "type": "message"
        }
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

_source line 80 · 2026-05-18T08:43:59.785Z_

<details><summary>↩ Tool result · `toolu_01Xa1uwKoLYLaqDF2b7suTbi`</summary>

```text
# ARR Reviewer Guidelines: Key Focus Areas

## Core Review Responsibilities

Reviewers should concentrate on four main tasks:

1. **Allocate adequate time** for both reviewing and discussion periods
2. **Check assignments** for expertise fit and conflicts of interest
3. **Write substantive reviews** addressing soundness, novelty, and reproducibility
4. **Engage with author responses** and update assessments accordingly

## What Constitutes a Strong Review

Effective reviews demonstrate these qualities:

- **Specificity**: Identify concrete issues with precise details rather than vague criticisms
- **Professional tone**: "Write the review you would like to get yourself"
- **Balanced perspective**: Read papers twice (skim then in-depth) to avoid knee-jerk reactions
- **Justified scores**: Soundness assessments must align with identified evidence in the review text

## Assessing Soundness

"Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation."

Core soundness checks include:
- Technical correctness of methodology and proofs
- Clarity of research questions and contribution scope
- Appropriate assumptions and complete justifications

## Novelty Considerations

Rather than dismissing work as "not novel," reviewers should:

- Provide specific citations to highly similar prior work (published 3+ months before submission)
- Recognize that reproducibility studies and resource papers constitute valid contributions
- Avoid penalizing negative results or simple solutions

## Reproducibility & Statistical Rigor

Key expectations:

- Sufficient implementation details for reproduction
- Code/data availability or clear justification for restrictions
- "Appropriate information about statistical significance (error bars, confidence intervals, statistical significance tests)"
- Disclosure of hyperparameter selection processes
- Transparent reporting of multiple trials or prompt engineering

## Baseline Comparisons

Reviewers should:

- Request comparisons only when they directly support the authors' core claims
- Avoid demanding closed-source model evaluations due to "methodological problems such as test contamination"
- Accept that not all baselines require exhaustive comparison if the sample selection is justified

## Common Review Pitfalls to Avoid

The guidelines identify 17 problematic heuristics (H1-H17), including:

- Dismissing results as "unsurprising" despite lacking prior empirical validation
- Requiring SOTA performance as a necessity rather than one possible contribution dimension
- Criticizing simplicity of methods when simpler solutions are preferable
- Demanding extra experiments beyond what claims require

## Dataset & Artifact Issues

Reviewers should examine:

- Data quality problems not disclosed by authors
- Ethics approval and compensation for human annotation
- Clear licensing and release terms for contributed resources
- Representative sampling when claiming generalization

## Assessment Scores (February 2025 onwards)

Three separate dimensions:

- **Soundness**: Technical validity (must be justified)
- **Excitement**: Personal interest (subjective, requires no explicit justification)
- **Overall recommendation**: Composite assessment reflecting soundness, novelty, and potential impact

Papers can be sound but unexciting, or exciting but requiring revision before acceptance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa1e3ff8-9ac1-4460-a611-0879f53a4045",
  "isSidechain": false,
  "promptId": "bfff0538-4138-4c41-a6a8-d1c970778888",
  "type": "user",
  "uuid": "bee284cb-e9dc-42b2-b81f-b3fcad0b22c8",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Reviewer Guidelines: Key Focus Areas\n\n## Core Review Responsibilities\n\nReviewers should concentrate on four main tasks:\n\n1. **Allocate adequate time** for both reviewing and discussion periods\n2. **Check assignments** for expertise fit and conflicts of interest\n3. **Write substantive reviews** addressing soundness, novelty, and reproducibility\n4. **Engage with author responses** and update assessments accordingly\n\n## What Constitutes a Strong Review\n\nEffective reviews demonstrate these qualities:\n\n- **Specificity**: Identify concrete issues with precise details rather than vague criticisms\n- **Professional tone**: \"Write the review you would like to get yourself\"\n- **Balanced perspective**: Read papers twice (skim then in-depth) to avoid knee-jerk reactions\n- **Justified scores**: Soundness assessments must align with identified evidence in the review text\n\n## Assessing Soundness\n\n\"Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation.\"\n\nCore soundness checks include:\n- Technical correctness of methodology and proofs\n- Clarity of research questions and contribution scope\n- Appropriate assumptions and complete justifications\n\n## Novelty Considerations\n\nRather than dismissing work as \"not novel,\" reviewers should:\n\n- Provide specific citations to highly similar prior work (published 3+ months before submission)\n- Recognize that reproducibility studies and resource papers constitute valid contributions\n- Avoid penalizing negative results or simple solutions\n\n## Reproducibility & Statistical Rigor\n\nKey expectations:\n\n- Sufficient implementation details for reproduction\n- Code/data availability or clear justification for restrictions\n- \"Appropriate information about statistical significance (error bars, confidence intervals, statistical significance tests)\"\n- Disclosure of hyperparameter selection processes\n- Transparent reporting of multiple trials or prompt engineering\n\n## Baseline Comparisons\n\nReviewers should:\n\n- Request comparisons only when they directly support the authors' core claims\n- Avoid demanding closed-source model evaluations due to \"methodological problems such as test contamination\"\n- Accept that not all baselines require exhaustive comparison if the sample selection is justified\n\n## Common Review Pitfalls to Avoid\n\nThe guidelines identify 17 problematic heuristics (H1-H17), including:\n\n- Dismissing results as \"unsurprising\" despite lacking prior empirical validation\n- Requiring SOTA performance as a necessity rather than one possible contribution dimension\n- Criticizing simplicity of methods when simpler solutions are preferable\n- Demanding extra experiments beyond what claims require\n\n## Dataset & Artifact Issues\n\nReviewers should examine:\n\n- Data quality problems not disclosed by authors\n- Ethics approval and compensation for human annotation\n- Clear licensing and release terms for contributed resources\n- Representative sampling when claiming generalization\n\n## Assessment Scores (February 2025 onwards)\n\nThree separate dimensions:\n\n- **Soundness**: Technical validity (must be justified)\n- **Excitement**: Personal interest (subjective, requires no explicit justification)\n- **Overall recommendation**: Composite assessment reflecting soundness, novelty, and potential impact\n\nPapers can be sound but unexciting, or exciting but requiring revision before acceptance.",
    "durationMs": 10279,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "aa1e3ff8-9ac1-4460-a611-0879f53a4045",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 81 · 2026-05-18T08:44:07.917Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have the full ARR reviewer guidelines. Let me now compile the final review.

Key points from guidelines:
- Soundness scores must be justified by the review text
- "Appropriate information about statistical significance (error bars, confidence intervals, statistical significance tests)" is expected
- Baselines should be requested only when they directly support core claims - but in this case, the paper's core claim IS about cross-attack generalization, and comparing with other multi-turn defenses IS directly relevant
- Common pitfall: demanding extra experiments beyond what claims require - but I'm pointing out that existing experiments are insufficient to support the claims as stated


- Now I'm ready to draft the actual review, making sure each criticism is grounded in the guidelines and the paper's specific claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bee284cb-e9dc-42b2-b81f-b3fcad0b22c8",
  "isSidechain": false,
  "requestId": "req_011Cb9jqAU1shPVoEVviDT9Z",
  "type": "assistant",
  "uuid": "2edf934a-38a0-4f5c-a7b5-0f98512411bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdV6nVdUrzYzDT8fDdZqx9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2986,
      "cache_read_input_tokens": 103481,
      "output_tokens": 6483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6483,
          "cache_read_input_tokens": 103481,
          "cache_creation_input_tokens": 2986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2986
          },
          "type": "message"
        }
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

_source line 82 · 2026-05-18T08:44:07.925Z_

所有材料已审查完毕。现在撰写完整审稿意见并提交给 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2edf934a-38a0-4f5c-a7b5-0f98512411bf",
  "isSidechain": false,
  "requestId": "req_011Cb9jqAU1shPVoEVviDT9Z",
  "type": "assistant",
  "uuid": "fe32b1be-ac34-4c74-aeaf-46cd75b1b36d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdV6nVdUrzYzDT8fDdZqx9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2986,
      "cache_read_input_tokens": 103481,
      "output_tokens": 6483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6483,
          "cache_read_input_tokens": 103481,
          "cache_creation_input_tokens": 2986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2986
          },
          "type": "message"
        }
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

_source line 83 · 2026-05-18T08:46:17.455Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01R1f1tDFj5bDetjcqrJcosg`</summary>

```json
{
  "text": "\n## Reviewer 1 审稿意见 — Round 1\n\n**论文**: \"What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap\"\n**审查侧重**: 方法严谨性 + 实验有效性\n\n---\n\n## 总体评分\n\n**Overall**: 2/5 (Resubmit next cycle)\n**一句话总结**: 研究问题有价值、消融设计有想法，但核心 claims 的统计支撑严重不足（single-seed vs 3-seed 不一致、n=76 上的 three-layer attribution、缺少与 SOTA multi-turn defense 的直接对比），需要在下一轮提交前做实质性修订。\n\n---\n\n## 官方维度打分（来自 ACL ARR review form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2/5 | 多项核心 claim 缺乏充分统计支撑：evidence hierarchy 中 binary/scrambled 仅 single seed，three-layer attribution 建立在 n=76（1-3 misclassifications = tier boundary）上，mean pooling = BiGRU 也是 single seed。这些不是 minor details，而是直接影响主要结论可信度的方法论缺陷。 |\n| Excitement | 3/5 | 研究问题（什么表征属性使跨攻击泛化成为可能）有真正的学术价值。\"partially falsified\" 原始假设的诚实报告令人欣赏。MLM 即可桥接 ~62pp OOD gap 的发现与 domain-adaptive pretraining 文献良好对接。但执行层面的统计问题限制了影响力。 |\n| Overall | 2/5 | 核心洞察（multi-turn jailbreak detection 本质上是 domain adaptation 问题）有意义，但需要：(1) 所有变体的 multi-seed 报告，(2) 更大规模评估或至少 significance tests，(3) 与已发表 multi-turn defense 系统的直接实验对比。这些修订可在下一个 ARR cycle 完成。 |\n| Confidence | 4/5 | 对实验设计和统计方法论问题的评估比较确信。论文的 domain adaptation 核心论点与我的专业知识领域吻合。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Evidence hierarchy 的统计基础不一致：single-seed vs 3-seed 比较\n\n- 具体位置：Section 5.2 Table 3, Section 5 Table 2, Abstract\n- 问题：论文的核心贡献——evidence hierarchy（vanilla 0.28 < topic 0.54±0.21 ≪ wiki-MLM 0.90±0.12 ≈ jb-MLM 0.91±0.12 < scrambled 0.99 ≈ binary 0.99 ≈ 9-class 0.997±0.005）——混合了两种不同统计精度的结果。9-class、MLM、wiki-MLM、topic、vanilla 报告 3-seed mean±std，而 **binary 和 scrambled 仅报告 seed 42 的单点估计**（Section 5 明确说明：\"binary and scrambled use seed 42\"）。\n  \n  这意味着 \"scrambled (0.990) ≈ binary (0.990)\" 这一关键等式没有方差信息。我们完全不知道 binary 和 scrambled 在 seeds 123、456 上的表现。考虑到 MLM 的方差高达 0.115（seed 456 recall 仅 0.64，见 Section 5.1），binary/scrambled 的真实分布可能有显著不同。\n\n  更严重的是，论文从这一不一致的比较中推导出多项因果性结论：\n  - \"Label quality and granularity are non-factors for detection: scrambled (0.990) ≈ binary (0.990)\"（Section 5.2）\n  - \"the classification objective functions as a regularizer that shapes representation geometry regardless of whether the labels carry meaningful semantic information\"（Section 5.2）\n  \n  这些 claims 建立在 **两个 single-seed 数据点的巧合相等** 之上，无法排除 seed-specific 的可能性。\n\n- 为什么影响接收：这是 evidence hierarchy 的核心环节。如果 binary 和 scrambled 的 multi-seed 结果出现显著方差（如 MLM 那样），整个 hierarchy 的排序和解释都可能改变。审稿人无法从现有数据判断 \"label quality is a non-factor\" 是否为 robust 结论。\n- 建议修改方向：**所有 7 个变体必须报告相同的 3-seed（或更多 seed）mean±std**。这是最基本的实验公平性要求。论文 Conclusion 已承认这一限制（\"Binary and scrambled variants report single-seed results; multi-seed evaluation would strengthen the comparison\"），但这不是 \"would strengthen\"——这是最低要求。\n\n**N2** [critical] Three-layer robustness attribution 在 n=76 上缺乏统计显著性\n\n- 具体位置：Section 5.3 Table 4, Introduction contribution #2, Conclusion\n- 问题：论文提出的 three-layer robustness attribution 是第二项核心贡献，但完全建立在 n=76 paraphrased conversations 上。**论文自身承认 \"tier boundaries correspond to 1-3 misclassifications\"**（Section 5.3 最后一句, Conclusion）。\n\n  具体量化：\n  - Δ=2.6pp ≈ 2 个样本的分类差异\n  - Δ=5.3pp ≈ 4 个样本的分类差异\n  - Δ=9.2pp ≈ 7 个样本的分类差异\n  \n  论文从这些极小的绝对差异中推导出精细的三层因果结构：\n  - Layer 1: \"classification structure provides full-length robustness\"（基于 classification-supervised 的 Δ=0.0 vs 其他 Δ≠0）\n  - Layer 2: \"the combination of correct and fine-grained labels is required at K=2\"（基于 9-class Δ=0.0 vs scrambled=binary=−2.6pp，即 2 个样本的差异）\n  - Layer 3: \"both granularity and correctness contribute independently at K=1\"（基于 9-class −2.6 vs scrambled −5.3 vs binary −9.2）\n  \n  **没有报告任何统计显著性检验**（如 McNemar's test、bootstrap confidence intervals、permutation test）。在 n=76 的样本量下，2 个样本的差异极易被随机波动解释。\n\n- 为什么影响接收：Three-layer attribution 是论文 Introduction 列出的第二项 contribution 的核心内容，占据了正文约 1/3 的讨论。如果统计显著性不成立，这一整块贡献都不可信。ARR reviewer guidelines 明确要求 \"appropriate information about statistical significance (error bars, confidence intervals, statistical significance tests)\"。\n- 建议修改方向：(1) 大幅扩大 perturbation test set（至少 n≥300 才能使 2.6pp 的差异有统计意义），或 (2) 报告 bootstrap confidence intervals / McNemar's test p-values，或 (3) 如果无法扩大数据，将 three-layer attribution 降级为 \"observed pattern\" 而非 \"established finding\"，大幅弱化相关 claims。\n\n**N3** [critical] 缺少与已发表 multi-turn defense 系统的直接实验对比\n\n- 具体位置：Section 2 (Related Work), Section 5 (Experiments)\n- 问题：论文在 Related Work 中讨论了 4 个直接相关的 multi-turn defense 系统：DeepContext（F1=0.84 IID, \"fails OOD\"）、BIID、G-Guard、SafeDream。但 **实验部分没有任何一个作为 baseline 进行头对头比较**。\n  \n  实际使用的 baselines 仅有：\n  - Vanilla DeBERTa（论文自己的 ablation baseline）\n  - TF-IDF LR（简单 baseline）\n  - LLM-as-judge（GPT-5.5, Qwen3-8B，仅测 IID）\n  \n  DeepContext 的 F1=0.84 数字来自该论文自身报告，但其评估数据集、attack types、evaluation protocol 可能与本文不同。直接引用其他论文的数字进行隐式比较，在方法论上不成立。\n\n- 为什么影响接收：论文的核心叙事是 \"existing multi-turn defenses degrade on unseen attack types, and none systematically analyze why\"（Introduction para 2）。如果不在相同数据集和评估条件下复现并对比这些方法，就无法支撑 \"DisPeD addresses this\" 的 claim。审稿人会认为这是一项缺乏充分 baseline 比较的 incremental work。\n- 建议修改方向：至少复现 DeepContext（BERT + recurrent network, 结构简单）作为 direct baseline，在相同的 Crescendo/FITD/DD 数据上评估。如果无法获取其他系统的代码，应明确说明并讨论。\n\n**N4** [critical] 数据集规模过小，影响所有核心 claims 的可信度\n\n- 具体位置：Section 5.1, Conclusion (Limitations)\n- 问题：\n  - 训练集：250 Crescendo jailbreak + 250 benign = 500 conversations\n  - OOD 测试集：80 FITD + 80 DD = 160 conversations\n  - IID 测试集：76 Crescendo\n  - Perturbation 测试集：76 paraphrased conversations\n  \n  在 n=80 的 DD 测试集上，每个 misclassification 改变 F1 约 1.25pp。这意味着：\n  - 9-class 的 0.997±0.005 意味着平均约 0.24 个错误（3-seed，部分 seed 0 错误、部分 seed 1 错误）\n  - MLM 的 0.914±0.115 在 seed 456 时 recall 仅 0.64，即约 29 个 misclassifications\n  \n  The entire evidence hierarchy 的精确排序在这种粒度下意义有限。\n\n- 为什么影响接收：论文的核心贡献是 \"systematic decomposition\"，但 decomposition 的统计分辨率受制于极小的测试集。在 n=80 上区分 0.990 和 0.997 在统计上是无意义的。\n- 建议修改方向：(1) 增加更多 attack families（如 ActorAttack, PAIR 的 multi-turn variants）扩大 OOD 测试范围，(2) 增加每种 attack 的样本量到至少 300+，(3) 在所有核心比较上报告 confidence intervals。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Mean pooling = BiGRU 的结论基于 single seed\n\n- 具体位置：Section 5.2 Table 3（footnote $^\\dagger$Single seed (42)）\n- 问题：论文做出强因果 claim \"Temporal modeling is not the detection mechanism. Mean pooling matches BiGRU (F1 = 1.000 on DD); detection relies on per-turn representations rather than their sequential order.\"（Section 5.2）。但 Table 3 脚注显示 mean pooling 结果仅为 seed 42。Mean pooling 在 DD-Full 和 DD-K=2 上均为 1.000，而 BiGRU 9-class 的 3-seed mean 为 0.997±0.005 和 0.981±0.013。在 n=80 的测试集上，1.000 vs 0.997 = 0 vs ~0.24 个错误的差异，统计上无意义。\n- 建议：(1) 报告 mean pooling 的 3-seed 结果，(2) 弱化 claim 为 \"the evidence suggests\" 而非因果性结论，(3) 在更大测试集上验证。\n\n**W2** [warning] 策略标注质量验证不充分（Qwen3-8B, κ=0.78, n=50）\n\n- 具体位置：Section 3.2\n- 问题：9-class 的策略标注由 Qwen3-8B 生成，人工验证仅 n=50 turns，Cohen's κ=0.78。对于 9 个类别，n=50 意味着每类平均约 5-6 个样本。某些低频类别（如 Direct Request, Obfuscation）可能只有 1-2 个验证样本。κ=0.78 是 \"substantial agreement\"（Landis & Koch 标准），但在人工样本量如此小的情况下，confidence interval 会很宽。\n  \n  更重要的是，论文 three-layer attribution 中 \"correct labels\" 的优势（Layer 2-3）完全依赖于标注质量。如果标注本身有 ~22% 的噪声率，\"correct fine-grained labels\" 的实际效果可能被高估。\n- 建议：(1) 增加人工验证样本至 200+（按类别分层抽样），(2) 报告每类的 κ 或至少 confusion matrix，(3) 讨论标注噪声对 three-layer attribution 的影响。\n\n**W3** [warning] LLM-as-judge baseline 仅测 IID，未测 OOD\n\n- 具体位置：Appendix A Table 5\n- 问题：GPT-5.5 和 Qwen3-8B 仅在 IID Crescendo 测试集上评估。论文的核心贡献是 OOD cross-attack generalization，不测 LLM baseline 的 OOD 表现是不公平的比较。LLM-as-judge 在 OOD 上可能表现更好（因为 IID Crescendo 数据是 Qwen3-8B 生成的，GPT-5.5 可能对 Qwen 生成的文本有 distributional mismatch）。\n- 建议：在 FITD 和 DD 上也评估 LLM-as-judge。\n\n**W4** [warning] TF-IDF LR 的强表现未被充分讨论\n\n- 具体位置：Section 5.1 Table 2, Section 2 最后一段\n- 问题：TF-IDF LR 在 DD-Full 上达到 0.944，与 9-class 的 0.997 仅差 5.3pp。在 perturbation 下（Table 4），TF-IDF 在 Full length 仅降 1.3pp。论文辩称 DisPeD 的优势在于 \"robustness under perturbation (0pp vs ~12pp degradation)\" 和 \"interpretability\"，但：\n  - 12pp degradation 是 Wikipedia MLM 和 vanilla 的降级幅度，不是 TF-IDF 的\n  - TF-IDF 自身仅降 1.3pp，与 9-class 的 0pp 差异在 n=76 上不具统计显著性\n  - 如果 \"substantial lexical separability\" 是一个 known limitation（Related Work 最后一段承认），那么 DisPeD 相对于 TF-IDF 的真正增量在哪里？\n- 建议：更诚实地讨论 TF-IDF baseline 的竞争力，并明确 DisPeD 在何种条件下具有不可替代的优势。\n\n**W5** [warning] 可复现性不足\n\n- 具体位置：全文\n- 问题：\n  - **超参不完整**：Stage-2 缺少 learning rate, batch size, optimizer, warmup schedule\n  - **数据生成细节不足**：Qwen3-8B 生成对话的 prompt、temperature、conversation length distribution 未提供\n  - **无代码/数据发布承诺**：全文未提及是否开源\n  - **策略标注 prompt 未提供**：Section 3.2 仅说 \"structured prompting that includes definitions and examples\"，但未给出实际 prompt\n- 建议：(1) 补充 Stage-2 完整超参，(2) 在 Appendix 提供数据生成和策略标注的完整 prompt，(3) 明确代码和数据发布计划。\n\n**W6** [warning] FITD 评估贡献有限\n\n- 具体位置：Section 5.1, Appendix B Table 7\n- 问题：Appendix Table 7 显示 FITD 结果几乎全为 perfect（9-class 和 vanilla 均 F1≥0.990）。这意味着 FITD 作为 OOD 测试集没有区分度。论文的所有 OOD claims 实际上仅依赖 DD 这一种 attack type，严重限制了 \"cross-attack generalization\" claim 的 generalizability。\n- 建议：增加更多 attack families（ActorAttack、PAIR 等）的 OOD 评估，或至少明确讨论当前 OOD 评估仅覆盖 2 种 attack type（其中 1 种区分度极低）的局限性。\n\n---\n\n## 小问题（不影响接收）\n\n- Figure 1: Stage 1 和 Stage 2 标题有轻微重叠，\"Frozen [CLS]\" 文字与 \"9-class Persuasion\" 位置略有拥挤。建议调整 layout。\n- Figure 3: 三个 heatmap 在单栏宽度下较小，axis labels 难以辨认（尤其 strategy 名称）。建议使用 `figure*` 环境占双栏宽度，或增大字体。\n- 引用: `chao2023pair` 的 year 与 OpenAlex 记录不一致（bib 2023 vs API 2025，可能是 arXiv preprint vs 正式发表的差异）。`austin1962speechacts` 的 year 有 bib 1962 vs API 1975 的差异（可能是不同版本）。建议检查并更新。\n- Section 5.1: \"binary and scrambled use seed 42\" 的原因未解释。为什么这两个变体没有运行 3-seed？是时间/计算资源限制还是其他原因？应说明。\n- 论文未讨论不同变体的计算成本（training time, GPU hours）。对于一个 \"systematic decomposition\" 的工作，展示各变体的资源开销是有意义的。\n- Section 3.1: 问题定义仅使用 user turns（\"We restrict input to user turns because adversarial intent resides in the attacker's messages\"）。这一合理假设值得更多讨论——assistant responses 是否可能包含有用的检测信号（如 refusal patterns, compliance indicators）？\n\n---\n\n## 主要优势\n\n1. **研究问题有价值且定义清晰**：从 \"what representation properties enable cross-attack generalization?\" 切入，问题有明确的操作化路径。这是一个 community 关心但尚未系统回答的问题。\n\n2. **消融设计思路优秀**：7 个 Stage-1 变体系统测试 domain exposure、classification supervision、label quality、label granularity、domain specificity 五个因素的贡献。Table 1 清楚展示了每个变体测试的假设，设计逻辑清晰。\n\n3. **知识诚实地报告 \"partially falsified\" 假设**：论文坦承 MLM 无标签即可桥接大部分 OOD gap，原始的 \"persuasion classification is key\" 假设被部分否定。这种诚实的科学态度在论文中并不常见，值得肯定。\n\n4. **与 domain-adaptive pretraining 文献的良好连接**：核心发现（continued pretraining 是主要机制）与 Gururangan et al. (2020) 的经典结论一致，将 jailbreak detection 重新定位为 domain adaptation 问题有理论深度。\n\n5. **写作质量总体较好**：论文叙事连贯，从 \"vanilla collapses on OOD\" 到 \"MLM bridges the gap\" 到 \"classification adds stability\" 的层进式展开易于follow。Evidence hierarchy 的可视化呈现清晰。\n\n6. **Strategy trajectory analysis 提供定性 insight**：Figure 3 的 transition matrices 展示了不同 attack families 的不同策略签名（Crescendo broad coverage vs FITD sparse Role→Obfuscation vs DD Emotion→Obfuscation），为安全分析提供了可操作的信息。\n\n---\n\n## 总结\n\n论文提出了一个有价值的研究问题，消融设计思路优秀，核心发现（domain adaptation 是 multi-turn jailbreak detection 的主要机制）有理论意义。但当前版本在统计严谨性上有 4 项 critical 问题：(1) single-seed vs 3-seed 不一致破坏了 evidence hierarchy 的可比性，(2) three-layer robustness attribution 建立在 n=76 上且无 significance tests，(3) 缺少与 SOTA multi-turn defense 的直接实验对比，(4) 数据集规模过小限制了所有核心 claims 的统计分辨率。这些问题需要实质性修订，建议在下一个 ARR cycle 重新提交。\n",
  "reviewer_id": "1",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe32b1be-ac34-4c74-aeaf-46cd75b1b36d",
  "isSidechain": false,
  "requestId": "req_011Cb9jqAU1shPVoEVviDT9Z",
  "type": "assistant",
  "uuid": "2f0a354b-be96-4d69-9e91-8405bce2bf58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdV6nVdUrzYzDT8fDdZqx9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2986,
      "cache_read_input_tokens": 103481,
      "output_tokens": 6483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6483,
          "cache_read_input_tokens": 103481,
          "cache_creation_input_tokens": 2986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2986
          },
          "type": "message"
        }
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

_source line 84_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验有效性**  ### Venue 信息 - **目标会议**：EMNLP 2026 Main Conference (ARR May cycle) - **截止日期**：2026-05-25 - **页数限制**：长文 8 页（不含 references、limitat…",
  "leafUuid": "2f0a354b-be96-4d69-9e91-8405bce2bf58",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---


### Runtime record

_source line 85_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 paper review for EMNLP persuasion jailbreak detection",
  "sessionId": "cbedc5e7-b345-430f-bdbb-8301dad12636"
}
```

---
