# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1 **你的侧重**：方法严谨性 + 实验设计 + 统计分析 ### Venue 信息 - **目标**: EMNLP 2026 Main Confere — Part 1 of 4

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-round-1-round-1-reviewer-1-venue-emnlp-2026-main-confere.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/02/02d0af8e53b2f0fc4dba.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-17T14:17:01.139Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T14:17:01.139Z",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "content": "[Round 1 审稿请求]:\n## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重**：方法严谨性 + 实验设计 + 统计分析\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: Long paper, 8 页正文, ACL `[review]` 模板, double-blind\n- **附录**: 不计入页数限制，但必须双栏格式\n- **必须包含**: Limitations section + Responsible NLP Research Checklist\n\n### 论文路径\n`projects/schema-dag-extraction/docs/paper/main.tex`（多文件结构，需读取 abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）\n\n### 论文概要\n标题: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n研究 training-free LLM IE 中 schema complexity 的两个维度（type count vs type confusability）如何独立预测性能下降。提出 SCS/BCS 指标量化 type confusability。实验横跨 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）和 3 个任务（NER, RE, ED）。包含一个重要负面结果：schema decomposition (SDGD) 在 NER 和 RE 上均失败。\n\n### 审查重点\n请重点审查以下方面，给出详细评估：\n\n1. **实验设计严谨性**\n   - BCS-controlled 实验的 confound control 是否充分？type frequency 混淆变量是否被充分处理？\n   - Count curve 和 BCS-controlled 两个实验范式的互补性是否合理？\n   - 数据集选择（4个）和任务覆盖（NER/RE/ED）是否充分支撑 claim？\n\n2. **统计方法**\n   - TOST 等价性检验的 margin 选择（±3pp）是否合理？\n   - Bootstrap CI 的使用是否恰当？\n   - 多重比较问题的处理（引用 Rothman 1990 作为不需要校正的理由）是否充分？\n   - Pairwise $r^2$ = 1.3-1.7% 的效应量是否足以支撑论文的核心 claim？\n\n3. **结论与证据匹配**\n   - \"Two dimensions\" claim 的证据是否充分？NER 上 batch-level BCS 无显著效果，这如何影响 claim？\n   - SDGD 负面结果的诊断（merge amplification, routing failure）是否有说服力？\n   - Cross-model validation（Llama 8B/70B）的证据力度如何？\n\n4. **可重现性**\n   - 实验细节是否足够重现？\n   - 单 seed 评估 + greedy decoding 的正当性\n\n5. **格式合规**\n   - 正文是否在 8 页以内？\n   - 引用格式是否正确？\n   - 图表是否清晰可读？\n\n请按照标准审稿报告格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Detailed Comments"
}
```

---


### Runtime record

_source line 2 · 2026-05-17T14:17:01.142Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T14:17:01.142Z",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0"
}
```

---


## Round 1

## Round 1

123 recorded events


### User

_source line 3 · 2026-05-17T14:17:01.176Z_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的侧重**：方法严谨性 + 实验设计 + 统计分析

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **格式**: Long paper, 8 页正文, ACL `[review]` 模板, double-blind
- **附录**: 不计入页数限制，但必须双栏格式
- **必须包含**: Limitations section + Responsible NLP Research Checklist

### 论文路径
`projects/schema-dag-extraction/docs/paper/main.tex`（多文件结构，需读取 abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）

### 论文概要
标题: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
研究 training-free LLM IE 中 schema complexity 的两个维度（type count vs type confusability）如何独立预测性能下降。提出 SCS/BCS 指标量化 type confusability。实验横跨 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）和 3 个任务（NER, RE, ED）。包含一个重要负面结果：schema decomposition (SDGD) 在 NER 和 RE 上均失败。

### 审查重点
请重点审查以下方面，给出详细评估：

1. **实验设计严谨性**
   - BCS-controlled 实验的 confound control 是否充分？type frequency 混淆变量是否被充分处理？
   - Count curve 和 BCS-controlled 两个实验范式的互补性是否合理？
   - 数据集选择（4个）和任务覆盖（NER/RE/ED）是否充分支撑 claim？

2. **统计方法**
   - TOST 等价性检验的 margin 选择（±3pp）是否合理？
   - Bootstrap CI 的使用是否恰当？
   - 多重比较问题的处理（引用 Rothman 1990 作为不需要校正的理由）是否充分？
   - Pairwise $r^2$ = 1.3-1.7% 的效应量是否足以支撑论文的核心 claim？

3. **结论与证据匹配**
   - "Two dimensions" claim 的证据是否充分？NER 上 batch-level BCS 无显著效果，这如何影响 claim？
   - SDGD 负面结果的诊断（merge amplification, routing failure）是否有说服力？
   - Cross-model validation（Llama 8B/70B）的证据力度如何？

4. **可重现性**
   - 实验细节是否足够重现？
   - 单 seed 评估 + greedy decoding 的正当性

5. **格式合规**
   - 正文是否在 8 页以内？
   - 引用格式是否正确？
   - 图表是否清晰可读？

请按照标准审稿报告格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Detailed Comments

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "36cc64b5-f288-4ab9-b887-6827073fe8a1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-17T14:17:01.176Z_

```json
{
  "parentUuid": "36cc64b5-f288-4ab9-b887-6827073fe8a1",
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
  "uuid": "fb61dd69-7e9d-4369-bda9-897909bb6d1a",
  "timestamp": "2026-05-17T14:17:01.176Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 5 · 2026-05-17T14:17:01.176Z_

```json
{
  "parentUuid": "fb61dd69-7e9d-4369-bda9-897909bb6d1a",
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
  "uuid": "dcebbb9d-872e-4899-bc28-058185ed59f7",
  "timestamp": "2026-05-17T14:17:01.176Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 6 · 2026-05-17T14:17:01.176Z_

```json
{
  "parentUuid": "dcebbb9d-872e-4899-bc28-058185ed59f7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8084da69-3dd8-4117-9b26-b3722bd32b4a",
  "timestamp": "2026-05-17T14:17:01.176Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
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
  "aiTitle": "Review schema complexity LLM information extraction paper",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0"
}
```

---


### Assistant

_source line 8 · 2026-05-17T14:17:08.832Z_

<details><summary>Logged reasoning block</summary>

```text
The user (Review Director) is asking me to perform a Round 1 review of a paper targeting EMNLP 2026. I need to:

1. First, run the session start skill
2. Search for EMNLP 2026 / ACL ARR reviewer guidelines
3. Read the paper thoroughly
4. Provide a detailed review focusing on methodology rigor, experimental design, and statistical analysis

Let me start by reading the skill for session start, and then read the paper.

Actually, let me first load the review-reviewer-session-start skill, and also search for the ARR review form. Let me also start reading the paper.


I'll load the session start skill and begin reading through the paper files to understand what I'm reviewing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8084da69-3dd8-4117-9b26-b3722bd32b4a",
  "isSidechain": false,
  "requestId": "req_011Cb8HRAQLpDcPftPY5M2Xu",
  "type": "assistant",
  "uuid": "9757d7d0-28c6-4ef8-bd65-de962c1489ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4PVvgaJj8HUJjQAee13Zj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15498,
      "cache_read_input_tokens": 11841,
      "output_tokens": 425,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15498,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 425,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15498
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-17T14:17:09.093Z_

我将开始 Round 1 审稿。先执行 session 启动检查，同时搜索 ARR reviewer guidelines 并阅读论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9757d7d0-28c6-4ef8-bd65-de962c1489ad",
  "isSidechain": false,
  "requestId": "req_011Cb8HRAQLpDcPftPY5M2Xu",
  "type": "assistant",
  "uuid": "131daec5-18df-451b-9fc3-eb384966c697",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4PVvgaJj8HUJjQAee13Zj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15498,
      "cache_read_input_tokens": 11841,
      "output_tokens": 425,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15498,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 425,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15498
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-17T14:17:11.587Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FSKyyNoAFtDdAVzrzaxe1L`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "131daec5-18df-451b-9fc3-eb384966c697",
  "isSidechain": false,
  "requestId": "req_011Cb8HRAQLpDcPftPY5M2Xu",
  "type": "assistant",
  "uuid": "4365c49e-1ea0-4254-abe4-4e86011c85af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4PVvgaJj8HUJjQAee13Zj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15498,
      "cache_read_input_tokens": 11841,
      "output_tokens": 425,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15498,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 425,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15498
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-17T14:17:13.029Z_

<details><summary>↩ Tool result · `toolu_01KCnGJjzbzC4C9Qm2rzbUws`</summary>

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
  "parentUuid": "33800529-53ea-47c0-a8ca-9fa37d5a8228",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "6991e79d-0d10-451a-aceb-e515681d61dc",
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
  "sourceToolAssistantUUID": "33800529-53ea-47c0-a8ca-9fa37d5a8228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 12 · 2026-05-17T14:17:11.602Z_

<details><summary>↩ Tool result · reported error · `toolu_01FSKyyNoAFtDdAVzrzaxe1L`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4365c49e-1ea0-4254-abe4-4e86011c85af",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "50d21eb3-5430-4535-9182-b83b3a936a60",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf.",
  "sourceToolAssistantUUID": "4365c49e-1ea0-4254-abe4-4e86011c85af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 13 · 2026-05-17T14:17:13.016Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KCnGJjzbzC4C9Qm2rzbUws`</summary>

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
  "parentUuid": "50d21eb3-5430-4535-9182-b83b3a936a60",
  "isSidechain": false,
  "requestId": "req_011Cb8HRAQLpDcPftPY5M2Xu",
  "type": "assistant",
  "uuid": "33800529-53ea-47c0-a8ca-9fa37d5a8228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4PVvgaJj8HUJjQAee13Zj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15498,
      "cache_read_input_tokens": 11841,
      "output_tokens": 425,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15498,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 425,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15498
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-17T14:17:17.770Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for the ARR reviewer guidelines and start reading the paper files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6991e79d-0d10-451a-aceb-e515681d61dc",
  "isSidechain": false,
  "requestId": "req_011Cb8HS3NwwX61DN7uHaFiR",
  "type": "assistant",
  "uuid": "67292df8-7510-4347-b2d1-0a33dde97776",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtvbgHvbQmXdABmC8okJW5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 27339,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 333,
          "cache_read_input_tokens": 27339,
          "cache_creation_input_tokens": 2517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2517
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-17T14:17:18.222Z_

开始搜索 ARR reviewer guidelines 并读取论文文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67292df8-7510-4347-b2d1-0a33dde97776",
  "isSidechain": false,
  "requestId": "req_011Cb8HS3NwwX61DN7uHaFiR",
  "type": "assistant",
  "uuid": "bfe248ef-f350-4b50-b84d-09fe5af38b13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtvbgHvbQmXdABmC8okJW5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 27339,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 333,
          "cache_read_input_tokens": 27339,
          "cache_creation_input_tokens": 2517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2517
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-17T14:17:18.827Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gp13kVMQ3mi62JyPtEdAMY`</summary>

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
  "parentUuid": "bfe248ef-f350-4b50-b84d-09fe5af38b13",
  "isSidechain": false,
  "requestId": "req_011Cb8HS3NwwX61DN7uHaFiR",
  "type": "assistant",
  "uuid": "2ecd85dc-b24a-46b5-9c3a-61f02d598cb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtvbgHvbQmXdABmC8okJW5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 27339,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 333,
          "cache_read_input_tokens": 27339,
          "cache_creation_input_tokens": 2517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2517
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-17T14:17:21.477Z_

<details><summary>↩ Tool result · `toolu_01M4bDAjc8hjeLcVGYuDrkGd`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
9	
10	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what modes do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
11	
12	To our knowledge, we present the first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We operationalize confusability via the \emph{Schema Confusability Score} (SCS), defined as pairwise embedding cosine similarity, and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, and MAVEN \cite{maven-2020} using Qwen3-32B (\S\ref{sec:experimental_setup}).
13	
14	Our experiments yield five findings:
15	(1)~Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) and confusability-related type substitution (typical-batch gap ${\approx}\,2.2$\,pp), with count as the dominant factor; the dimensions exhibit bounded association in RE (TOST $p = 0.003$ at $\pm 3$\,pp) but are coupled in NER.
16	(2)~Pairwise SCS predicts type confusion across NER, RE, and ED ($r = 0.112$--$0.129$); at batch level, BCS predicts accuracy in RE ($R^2 = 0.22$--$0.53$) but not in NER (batch-level $r \approx 0$, n.s.).
17	(3)~Effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: $R^2 = 0.53$) and directionally consistent across prompt designs.
18	(4)~Per-type aggregation is confounded by centrality on homogeneous schemas.
19	(5)~Schema decomposition fails due to merge amplification in NER; RE confusability-aware grouping yields no significant improvement over random (+1.4\,pp, $p \approx 0.19$, n.s.) despite oracle routing that recovers +29.8\,pp.
20	
21	Our contributions are:
22	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
23	    \item We conduct the first controlled study that isolates count and confusability effects on training-free LLM IE performance across four datasets and three tasks (\S\ref{sec:count_curves}, \S\ref{sec:bcs_controlled}).
24	    \item We validate that embedding-based confusability scores predict type substitution errors and establish an empirical link between schema similarity and extraction accuracy in RE (\S\ref{sec:scs-validation}).
25	    \item We show that count-related recall decline generalizes across tasks, while batch-level confusability effects are specific to RE; NER shows no batch-level BCS signal despite significant pairwise SCS effects (\S\ref{sec:bcs_controlled}, \S\ref{sec:multi_channel}).
26	    \item We report a negative result: schema decomposition fails due to merge amplification in NER and routing failure in RE, and we diagnose structural barriers to confusability-aware extraction (\S\ref{sec:sdgd}).
27	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68efff6e-c3b5-4efc-9675-64a0b00661f6",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "e476121a-cefe-479c-a5bc-f717f7d9f3b9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\\footnote{Code and data will be released upon acceptance. Anonymous review materials: \\url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\\% with one relation to 49.5\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level), near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat explains this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nThis study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what modes do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nTo our knowledge, we present the first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We operationalize confusability via the \\emph{Schema Confusability Score} (SCS), defined as pairwise embedding cosine similarity, and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).\n\nOur experiments yield five findings:\n(1)~Degradation operates along two dimensions: count-related recall decline (up to $-$49\\,pp for document-level RE) and confusability-related type substitution (typical-batch gap ${\\approx}\\,2.2$\\,pp), with count as the dominant factor; the dimensions exhibit bounded association in RE (TOST $p = 0.003$ at $\\pm 3$\\,pp) but are coupled in NER.\n(2)~Pairwise SCS predicts type confusion across NER, RE, and ED ($r = 0.112$--$0.129$); at batch level, BCS predicts accuracy in RE ($R^2 = 0.22$--$0.53$) but not in NER (batch-level $r \\approx 0$, n.s.).\n(3)~Effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: $R^2 = 0.53$) and directionally consistent across prompt designs.\n(4)~Per-type aggregation is confounded by centrality on homogeneous schemas.\n(5)~Schema decomposition fails due to merge amplification in NER; RE confusability-aware grouping yields no significant improvement over random (+1.4\\,pp, $p \\approx 0.19$, n.s.) despite oracle routing that recovers +29.8\\,pp.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item We conduct the first controlled study that isolates count and confusability effects on training-free LLM IE performance across four datasets and three tasks (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n    \\item We validate that embedding-based confusability scores predict type substitution errors and establish an empirical link between schema similarity and extraction accuracy in RE (\\S\\ref{sec:scs-validation}).\n    \\item We show that count-related recall decline generalizes across tasks, while batch-level confusability effects are specific to RE; NER shows no batch-level BCS signal despite significant pairwise SCS effects (\\S\\ref{sec:bcs_controlled}, \\S\\ref{sec:multi_channel}).\n    \\item We report a negative result: schema decomposition fails due to merge amplification in NER and routing failure in RE, and we diagnose structural barriers to confusability-aware extraction (\\S\\ref{sec:sdgd}).\n\\end{enumerate}",
      "numLines": 27,
      "startLine": 1,
      "totalLines": 27
    }
  },
  "sourceToolAssistantUUID": "68efff6e-c3b5-4efc-9675-64a0b00661f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-17T14:17:20.603Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P8BDokaGbrCXcjxpyAFcbd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ecd85dc-b24a-46b5-9c3a-61f02d598cb1",
  "isSidechain": false,
  "requestId": "req_011Cb8HS3NwwX61DN7uHaFiR",
  "type": "assistant",
  "uuid": "b4cfe1f3-6fad-4f83-847c-81527fdd3756",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtvbgHvbQmXdABmC8okJW5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 27339,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 333,
          "cache_read_input_tokens": 27339,
          "cache_creation_input_tokens": 2517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2517
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-17T14:17:20.904Z_

<details><summary>↩ Tool result · `toolu_01P8BDokaGbrCXcjxpyAFcbd`</summary>

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
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B and 70B-Instruct (FP8). Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms bounded association ($p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp, interaction = 0.47\,pp; Appendix~\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity. The TOST equivalence test is estimated from BCS-controlled batches (counts 4--40) where BCS variation is sufficient; generalization to broader count ranges requires additional controlled experiments.
45	
46	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions. For Few-NERD, SCS is computed from the extraction model's own embeddings (Qwen3), creating a shared-representation dependency. MiniLM cross-check yields a conservative but directionally consistent estimate ($r = 0.172$ vs $r = 0.138$; confusion matrix correlation 0.894), suggesting the effect is not an artifact of shared representations.
47	
48	\item \textbf{NER evaluation metric.} Our exact-match NER evaluation conflates boundary errors (partial span overlap) with type errors (correct span, wrong label). Relaxed matching may yield different confusability effect sizes, as boundary ambiguity may correlate with schema complexity independently of type similarity.
49	
50	\item \textbf{RE format specificity.} RE's clean dimension separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.
51	
52	\item \textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.
53	
54	\item \textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\%$\to$50.4\%) cannot be explained by uniform contamination, which would elevate all conditions equally. BCS slope consistency across independent and within-pool conditions (permutation $p = 0.60$) provides a robustness check that is difficult to reconcile with non-uniform contamination, which would differentially affect specific type subsets. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$). Adding train-origin ratio as a covariate leaves the BCS partial effect unchanged ($p = 0.245$ for origin; Appendix~\ref{app:split-origin}).
55	\end{enumerate}
56	
57	\paragraph{Multiple comparisons.} Cross-dataset comparisons (FewRel, DocRED, Few-NERD, MAVEN) serve as independent replications of the same hypothesis and do not require family-wise correction \citep{rothman-1990}. Within-dataset secondary analyses (e.g., quartile comparisons, slope sensitivity checks) involve multiple looks at the same data; we report individual $p$-values and note that core claims rest on effects reaching $p < 0.001$ \citep{dror-2018-significance}.
58	
59	\input{checklist}
60	
61	\bibliography{references}
62	
63	\appendix
64	
65	\section{Additional Figures}
66	\label{sec:appendix_figures}
67	
68	\begin{table}[h]
69	\centering
70	\small
71	\begin{tabular}{lrr}
72	\toprule
73	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
74	\midrule
75	1 & 0.702 & 0.640 \\
76	64 & 0.273 & 0.304 \\
77	\midrule
78	Decline & $-$43\,pp & $-$34\,pp \\
79	\bottomrule
80	\end{tabular}
81	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
82	\label{tab:cross_model}
83	\end{table}
84	
85	\begin{table}[h]
86	\centering
87	\small
88	\resizebox{\columnwidth}{!}{%
89	\begin{tabular}{crrrrrr}
90	\toprule
91	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
92	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
93	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
94	\midrule
95	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
96	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
97	\bottomrule
98	\end{tabular}}
99	\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
100	\label{tab:cross_model_bcs}
101	\end{table}
102	
103	\begin{table}[h]
104	\centering
105	\small
106	\resizebox{\columnwidth}{!}{%
107	\begin{tabular}{llrrrrrrr}
108	\toprule
109	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
110	\cmidrule(lr){3-7}
111	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
112	\midrule
113	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
114	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
115	\midrule
116	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
117	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
118	\bottomrule
119	\end{tabular}}
120	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}
121	\label{tab:error_taxonomy}
122	\end{table}
123	
124	\section{SDGD Full Protocol and Results}
125	\label{sec:appendix_sdgd}
126	
127	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
128	
129	Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368). SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop. Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\ref{tab:sdgd_results}).
130	
131	\begin{table}[h]
132	\centering
133	\small
134	\resizebox{\columnwidth}{!}{%
135	\begin{tabular}{lrccc}
136	\toprule
137	\textbf{Mode} & \textbf{\# Batches} & \textbf{Precision} & \textbf{Recall} & \textbf{F1} \\
138	\midrule
139	single\_pass & 1 & 0.563 & 0.368 & 0.445 \\
140	\midrule
141	sdgd\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\
142	random\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\
143	per\_type & 66 & 0.194 & 0.586 & 0.292 \\
144	\midrule
145	sdgd\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\
146	random\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\
147	\bottomrule
148	\end{tabular}}
149	\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \texttt{min\_batch\_size=8} (reducing 8$\to$4 batches for sdgd\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}
150	\label{tab:sdgd_results}
151	\end{table}
152	
153	Decomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.
154	
155	Our v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\_zero: 0.210$\to$0.324; random\_batch: 0.249$\to$0.331), but at the cost of disproportionate recall loss (0.314$\to$0.191; 0.446$\to$0.276), yielding lower F1 in both modes (sdgd\_zero: 0.251$\to$0.241; random\_batch: 0.320$\to$0.301).
156	
157	\subsection{Practical Routing Strategies on RE}
158	\label{sec:appendix_routing}
159	
160	We evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.
161	
162	\begin{table}[h]
163	\centering
164	\small
165	\begin{tabular}{@{}lrr@{}}
166	\toprule
167	\textbf{Strategy} & \textbf{Accuracy} & \textbf{$\Delta$ vs.\ Single-Pass} \\
168	\midrule
169	Oracle (gold label) & 72.4\% & +22.0\,pp \\
170	\midrule
171	Max-conf (positive only) & 36.5\% & $-$14.0\,pp \\
172	None-aware & 36.5\% & $-$14.0\,pp \\
173	Margin (positive only) & 35.9\% & $-$14.5\,pp \\
174	Max-conf (all) & 27.7\% & $-$22.7\,pp \\
175	Random & 14.7\% & $-$35.7\,pp \\
176	\midrule
177	Single-pass (no decomposition) & 50.4\% & --- \\
178	\bottomrule
179	\end{tabular}
180	\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\%.}
181	\label{tab:routing_strategies}
182	\end{table}
183	
184	\section{Factorial Analysis and Separability Test}
185	\label{sec:appendix_factorial}
186	
187	To formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\sim$ $\log_2$\,count $+$ BCS $+$ count$\times$BCS) across 69 batches from FewRel spanning five count levels ($k \in \{4, 8, 16, 32, 40\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\,pp). A TOST equivalence test with a $\pm 3$\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\text{TOST}} = 0.003$), supporting bounded association between count and confusability effects.
188	
189	A $2 \times 2$ factorial sensitivity check on FewRel (count $\in \{8, 16\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\S\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.
190	
191	\paragraph{Equivalence margin justification.}
192	We set the $\pm 3$\,pp margin based on three converging anchors. \emph{Empirical}: typical random-batch confusability variation produces 2--5\,pp accuracy differences (batch SD $\approx 4.6$\,pp at count 32). \emph{Practical}: a ${<}3$\,pp accuracy difference falls below deployment-relevant thresholds. \emph{Statistical}: 3\,pp $\approx 0.5 \times$ batch SD, equivalent to Cohen's $d \approx 0.5$ (medium effect threshold; \citealt{lakens-2017-equivalence}). A 3\,pp interaction atop the 2.2\,pp confusability main effect would represent ${>}130\%$ amplification, fundamentally changing whether confusability warrants mitigation. At $\pm 2$\,pp (marginally equivalent, $p = 0.047$), interaction remains bounded below the main effect itself.
193	
194	\begin{table}[h]
195	\centering
196	\small
197	\begin{tabular}{crrl}
198	\toprule
199	\textbf{Margin (pp)} & \textbf{$t_{\text{upper}}$} & \textbf{$p_{\text{TOST}}$} & \textbf{Conclusion} \\
200	\midrule
201	$\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\
202	$\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\
203	$\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\
204	$\pm 5$ & $-5.02$ & ${<}\,0.001$ & Equivalent \\
205	\bottomrule
206	\end{tabular}
207	\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\,pp, 90\% CI [$-$1.0, 2.0]\,pp) is bounded below 2\,pp at marginal significance ($p = 0.047$), confirming that the $\pm 3$\,pp choice does not drive the equivalence conclusion. At $\pm 1$\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}
208	\label{tab:tost_sensitivity}
209	\end{table}
210	
211	\paragraph{Logit-scale sensitivity.}
212	Because accuracy near 50\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\pm 3$\,pp margin ($\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\,pp, still within the $\pm 3$\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check.
213	
214	\section{Within-Pool CI Details}
215	\label{sec:appendix_within_pool}
216	
217	The quartile $\Delta$ for 80-pool 16-relation subsets ($-$3.92\,pp, 95\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.
218	
219	\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}
220	\label{sec:appendix_residualized_bcs}
221	
222	Section~\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.
223	
224	\paragraph{Confound identification.}
225	For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
226	\begin{itemize}[itemsep=2pt,leftmargin=*]
227	\item \textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.
228	\item \textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.
229	\end{itemize}
230	
231	\paragraph{Partial correlation results.}
232	Table~\ref{tab:residualized_bcs} reports raw Spearman $\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.
233	
234	\begin{table}[h]
235	\centering
236	\small
237	\resizebox{\columnwidth}{!}{%
238	\begin{tabular}{llcccc}
239	\toprule
240	\textbf{Embedding} & \textbf{Control} & \textbf{Raw $\rho$} & \textbf{Raw $p$} & \textbf{Partial $r$} & \textbf{Partial $p$} \\
241	\midrule
242	MiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\
243	MiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\
244	MiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\
245	\midrule
246	Qwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\
247	Qwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\
248	Qwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\
249	\bottomrule
250	\end{tabular}}
251	\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \texttt{exp\_maven\_residualized\_bcs}.}
252	\label{tab:residualized_bcs}
253	\end{table}
254	
255	\paragraph{Interpretation.}
256	The two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.
257	
258	Under joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.
259	
260	\section{Batch Composition Results}
261	\label{sec:appendix_batch_composition}
262	
263	See Table~\ref{tab:batch_composition} and the accompanying discussion in \S\ref{sec:sdgd}.
264	
265	\input{prompt_appendix}
266	
267	\section{Prompt Version Sensitivity Analysis}
268	\label{sec:appendix_prompt_sensitivity}
269	
270	We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
271	
272	\paragraph{RE (FewRel).}
273	Under the v1 prompt, the extreme-batch BCS gap (Table~\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.
274	
275	\paragraph{NER (Few-NERD).}
276	The batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\text{BCS}, \text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\S\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.
277	
278	\paragraph{Interpretation.}
279	The $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\% vs.\ 82.3\%), but type confusion under high confusability persists (59.7\% vs.\ 51.0\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.
280	
281	\subsection{Cross-Prompt-Variant BCS Correlation}
282	\label{sec:appendix_prompt_variants}
283	
284	To verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.
285	
286	\begin{table}[h]
287	\centering
288	\small
289	\begin{tabular}{llrrrr}
290	\toprule
291	\textbf{Variant} & \textbf{Count} & \textbf{Mean Acc} & \textbf{$r$} & \textbf{$p$} \\
292	\midrule
293	V2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\
294	V2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\
295	Instruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\
296	Instruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\
297	Chain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\
298	Chain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\
299	Minimal & 8 & 0.852 & $-$0.170 & 0.638 \\
300	Minimal & 32 & 0.615 & $-$0.771 & 0.009 \\
301	\bottomrule
302	\end{tabular}
303	\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}
304	\label{tab:prompt_variants}
305	\end{table}
306	
307	At count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.
308	
309	\section{BCS Aggregation Sensitivity}
310	\label{sec:appendix_bcs_sensitivity}
311	
312	We define Batch Confusability Score (BCS) as the \emph{mean} pairwise SCS across all type pairs in a batch (\S\ref{sec:bcs_controlled}). An alternative definition takes the \emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.
313	
314	\begin{table}[h]
315	\centering
316	\small
317	\resizebox{\columnwidth}{!}{%
318	\begin{tabular}{llcccc}
319	\toprule
320	\textbf{Aggregation} & \textbf{Condition} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} \\
321	\midrule
322	MEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ \\
323	MEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
324	\midrule
325	MAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\,0.001$ \\
326	MAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
327	\bottomrule
328	\end{tabular}}
329	\caption{BCS--accuracy regression under mean vs.\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \approx 0.60$; MAX $p \approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}
330	\label{tab:bcs_aggregation}
331	\end{table}
332	
333	MAX aggregation yields stronger correlations ($r = -0.637$ vs.\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.
334	
335	\section{BCS-Controlled Detailed Results}
336	\label{app:bcs-controlled-table}
337	
338	\begin{table}[h]
339	\centering
340	\small
341	\resizebox{\columnwidth}{!}{%
342	\begin{tabular}{lcrrrr}
343	\toprule
344	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
345	\midrule
346	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
347	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
348	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
349	\bottomrule
350	\end{tabular}}
351	\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
352	\label{tab:bcs_controlled}
353	\end{table}
354	
355	\section{Within-Pool Analysis Methodology}
356	\label{app:within-pool-method}
357	
358	A potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.
359	
360	\begin{table}[h]
361	\centering
362	\small
363	\resizebox{\columnwidth}{!}{%
364	\begin{tabular}{lrrrrrrr}
365	\toprule
366	& \multicolumn{4}{c}{\textbf{Regression (BCS $\to$ Accuracy)}} & \multicolumn{2}{c}{\textbf{Quartile $\Delta$}} \\
367	\cmidrule(lr){2-5} \cmidrule(lr){6-7}
368	\textbf{Setting} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
369	\midrule
370	Independent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\
371	80-pool $\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\
372	Full 80-rel ($n{=}25$)$^\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\
373	\midrule
374	\multicolumn{7}{l}{\footnotesize Permutation test (16-rel vs.\ 80-pool slopes): $p \approx 0.60$ (5{,}000 permutations)} \\
375	\multicolumn{7}{l}{\footnotesize $^\dagger$BCS range (IQR\,=\,0.033) insufficient for regression; slope not interpretable.} \\
376	\bottomrule
377	\end{tabular}}
378	\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\ref{sec:appendix_within_pool} for CI interpretation.}
379	\label{tab:within_pool}
380	\end{table}
381	
382	The within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \approx 0.60$). The smaller quartile gap ($-$3.92\,pp vs.\ $-$5.31\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\ref{sec:appendix_within_pool}).
383	
384	In the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.
385	
386	\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}
387	\label{app:scs-ablation}
388	
389	Table~\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.
390	
391	\begin{table}[h]
392	\centering
393	\small
394	\begin{tabular}{lcccc}
395	\toprule
396	Dataset & SCS$_\text{name}$ $r$ & SCS$_\text{def}$ $r$ & $\Delta r$ & Matrix corr. \\
397	\midrule
398	Few-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\
399	MAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\
400	FewRel & 0.178 & 0.193 & +0.015 & 0.848 \\
401	\bottomrule
402	\end{tabular}
403	\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\Delta r$ indicates no systematic benefit from including definitions.}
404	\label{tab:scs-ablation}
405	\end{table}
406	
407	Few-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.
408	
409	\section{Pair-to-Batch Aggregation Simulation}
410	\label{app:aggregation-sim}
411	
412	The following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\S\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.
413	
414	\paragraph{Setup.} We examine whether the pair-level $R^2 \approx 7\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \approx 22\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\rho_\text{SCS} = 0.35$). For batches of $k=8$ types ($\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.
415	
416	\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\sim$3$\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\approx 3.4$, not 28).
417	
418	\paragraph{Unconditional baseline.}
419	When the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\% CI: 0.001--0.151], well below the observed $R^2 = 0.218$. The analytical formula confirms: $\text{SNR} \times \text{EF} / (\text{SNR} \times \text{EF} + 1) = 0.042$ with the same effective factor $\text{EF} = 3.35$. This ${\sim}5\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \emph{active} confusable pairs, not uniform contributions from all pairs.
420	
421	\section{BCS Independence from Type Composition}
422	\label{app:bcs-composition}
423	
424	FewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\% of explained variance), composition unique $R^2 = 0.298$ (42.3\%), and shared $R^2 = 0.147$ (20.9\%). The near-orthogonality of predictors (VIF${}\,=\,1.06$, $r(\text{BCS}, \text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than proxying for type difficulty.
425	
426	\section{Split-Origin Covariate Analysis}
427	\label{app:split-origin}
428	
429	FewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.
430	
431	\paragraph{Method.}  Across 213 multi-type batches ($k \geq 2$) from the batch-composition experiment (\S\ref{sec:sdgd}) and the factorial design (\S\ref{sec:bcs_controlled}), we compute $\texttt{train\_origin\_ratio} = n_{\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, reflecting the 64/80 base rate).  We fit:
432	\[
433	\text{accuracy} = \beta_0 + \beta_{\text{BCS}} \cdot \text{BCS} + \beta_{\text{origin}} \cdot \text{train\_origin\_ratio} + \varepsilon
434	\]
435	
436	\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\beta_{\text{BCS}} = -0.416$, $p < 10^{-16}$ (vs.\ $\beta = -0.412$, $p < 10^{-16}$ without the covariate).  Train-origin ratio is not independently significant ($\beta_{\text{origin}} = -0.057$, $p = 0.245$), and $\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.
437	
438	Pairwise SCS distributions do not differ significantly between train-origin (64 types, mean\,=\,0.880) and val-origin (16 types, mean\,=\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$), confirming that the train/val split does not introduce systematic confusability bias.
439	
440	\section{Cross-Seed Variance Decomposition}
441	\label{app:variance-decomposition}
442	
443	\begin{table}[h]
444	\centering
445	\small
446	\begin{tabular}{rrrr}
447	\toprule
448	\textbf{Count} & \textbf{Batch SD} & \textbf{Seed SD} & \textbf{Ratio} \\
449	\midrule
450	4 & 0.0889 & 0.0122 & 53.5 \\
451	8 & 0.0820 & 0.0098 & 70.0 \\
452	16 & 0.0626 & 0.0270 & 5.4 \\
453	32 & 0.0462 & 0.0091 & 26.0 \\
454	40 & 0.0421 & 0.0019 & 474.4 \\
455	64 & 0.0245 & 0.0022 & 119.8 \\
456	80 & 0.0001 & 0.0088 & $<$0.1 \\
457	\bottomrule
458	\end{tabular}
459	\caption{Variance decomposition on FewRel (3 seeds $\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}
460	\label{tab:variance_decomposition}
461	\end{table}
462	
463	Intra-batch variance dominates inter-seed variance by 5--474$\times$ across count levels 4--64 (mean 125$\times$), confirming that random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\,=\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\,pp, likely attributable to FP8 quantization non-determinism).
464	
465	\section{Cross-Domain Connections}
466	\label{app:cross-domain}
467	
468	The schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.
469	
470	\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}
471	\label{sec:appendix_cross_model_70b}
472	
473	To test whether the two-dimensional degradation pattern generalizes across model families, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\S\ref{sec:count_curves}, \S\ref{sec:bcs_controlled}).
474	
475	\begin{table}[h]
476	\centering
477	\small
478	\begin{tabular}{lrr}
479	\toprule
480	\textbf{Count} & \textbf{LLaMA-70B} & \textbf{Qwen3-32B} \\
481	\midrule
482	\multicolumn{3}{l}{\textit{RE (FewRel, Classification Accuracy)}} \\
483	8  & 0.757 & 0.805 \\
484	16 & 0.685 & 0.719 \\
485	32 & 0.601 & 0.652 \\
486	64 & 0.504 & 0.539 \\
487	80 & 0.450 & 0.504 \\
488	\midrule
489	\multicolumn{3}{l}{\textit{NER (Few-NERD, Text+Type Match Recall)}} \\
490	2  & 0.323 & 0.515 \\
491	6  & 0.300 & 0.399 \\
492	12 & 0.278 & 0.318 \\
493	22 & 0.252 & 0.279 \\
494	44 & 0.297 & 0.309 \\
495	66 & 0.273 & 0.407 \\
496	\bottomrule
497	\end{tabular}
498	\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\to$80): $-$30.7\,pp (70B) vs.\ $-$30.1\,pp (32B). NER decline (count 2$\to$22): $-$7.1\,pp (70B) vs.\ $-$23.6\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}
499	\label{tab:cross_model_70b}
500	\end{table}
501	
502	Table~\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\,pp (70B) versus $-$30.1\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-driven decline) is directionally consistent across architectures for RE.
503	
504	On NER, the count-driven decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\to$0.252, $-$7.1\,pp; Qwen3: 0.515$\to$0.279, $-$23.6\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).
505	
506	For the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\Delta = +10.9$\,pp, 95\% CI: [$+$3.0, $+$20.1]). The confidence interval excludes zero, confirming the confusability effect at the 70B scale.
507	
508	In summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-driven decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.
509	
510	\section{Few-Shot Prompting and Confusability}
511	\label{sec:appendix_fewshot_bcs}
512	
513	To test whether in-context demonstrations mitigate the BCS-driven confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \S\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\approx 0.36$; 25 high-BCS, mean $\approx 0.80$), drawn from the pre-constructed batch pool of \S\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.
514	
515	\begin{table}[h]
516	\centering
517	\small
518	\resizebox{\columnwidth}{!}{\begin{tabular}{lrrrl}
519	\toprule
520	\textbf{Condition} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
521	\midrule
522	0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\
523	1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\
524	5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\
525	\bottomrule
526	\end{tabular}}
527	\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\,pp at 1-shot, $-$1.0\,pp at 5-shot). The confusability gap widens from +18.5\,pp (0-shot) to +22.8\,pp (5-shot). All metrics are micro-averaged across batches.}
528	\label{tab:fewshot_bcs}
529	\end{table}
530	
531	Demonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\,pp at 1-shot, $-$1.0\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-driven type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \cite{lost-in-middle-2024}.
532	
533	The 0-shot gap (+18.5\,pp) is smaller than the extreme-batch gap reported in \S\ref{sec:bcs_controlled} (+25.5\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.
534	
535	\end{document}
536	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4cfe1f3-6fad-4f83-847c-81527fdd3756",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "49e319cd-bf9d-41e2-b88d-a97d9413be04",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B and 70B-Instruct (FP8). Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.\n\n\\item \\textbf{Factorial interaction tests.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms bounded association ($p_{\\text{TOST}} = 0.003$ at $\\pm 3$\\,pp, interaction = 0.47\\,pp; Appendix~\\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity. The TOST equivalence test is estimated from BCS-controlled batches (counts 4--40) where BCS variation is sufficient; generalization to broader count ranges requires additional controlled experiments.\n\n\\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions. For Few-NERD, SCS is computed from the extraction model's own embeddings (Qwen3), creating a shared-representation dependency. MiniLM cross-check yields a conservative but directionally consistent estimate ($r = 0.172$ vs $r = 0.138$; confusion matrix correlation 0.894), suggesting the effect is not an artifact of shared representations.\n\n\\item \\textbf{NER evaluation metric.} Our exact-match NER evaluation conflates boundary errors (partial span overlap) with type errors (correct span, wrong label). Relaxed matching may yield different confusability effect sizes, as boundary ambiguity may correlate with schema complexity independently of type similarity.\n\n\\item \\textbf{RE format specificity.} RE's clean dimension separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally. BCS slope consistency across independent and within-pool conditions (permutation $p = 0.60$) provides a robustness check that is difficult to reconcile with non-uniform contamination, which would differentially affect specific type subsets. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$). Adding train-origin ratio as a covariate leaves the BCS partial effect unchanged ($p = 0.245$ for origin; Appendix~\\ref{app:split-origin}).\n\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} Cross-dataset comparisons (FewRel, DocRED, Few-NERD, MAVEN) serve as independent replications of the same hypothesis and do not require family-wise correction \\citep{rothman-1990}. Within-dataset secondary analyses (e.g., quartile comparisons, slope sensitivity checks) involve multiple looks at the same data; we report individual $p$-values and note that core claims rest on effects reaching $p < 0.001$ \\citep{dror-2018-significance}.\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$), supporting bounded association between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{Empirical}: typical random-batch confusability variation produces 2--5\\,pp accuracy differences (batch SD $\\approx 4.6$\\,pp at count 32). \\emph{Practical}: a ${<}3$\\,pp accuracy difference falls below deployment-relevant thresholds. \\emph{Statistical}: 3\\,pp $\\approx 0.5 \\times$ batch SD, equivalent to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}). A 3\\,pp interaction atop the 2.2\\,pp confusability main effect would represent ${>}130\\%$ amplification, fundamentally changing whether confusability warrants mitigation. At $\\pm 2$\\,pp (marginally equivalent, $p = 0.047$), interaction remains bounded below the main effect itself.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$), confirming that the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\\% CI: 0.001--0.151], well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than proxying for type difficulty.\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, reflecting the 64/80 base rate).  We fit:\n\\[\n\\text{accuracy} = \\beta_0 + \\beta_{\\text{BCS}} \\cdot \\text{BCS} + \\beta_{\\text{origin}} \\cdot \\text{train\\_origin\\_ratio} + \\varepsilon\n\\]\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 10^{-16}$ (vs.\\ $\\beta = -0.412$, $p < 10^{-16}$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$), confirming that the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$), confirming that random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across model families, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-driven decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-driven decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI: [$+$3.0, $+$20.1]). The confidence interval excludes zero, confirming the confusability effect at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-driven decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-driven confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-driven type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\cite{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\end{document}\n",
      "numLines": 536,
      "startLine": 1,
      "totalLines": 536
    }
  },
  "sourceToolAssistantUUID": "b4cfe1f3-6fad-4f83-847c-81527fdd3756",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-17T14:17:21.231Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FgMXizQCcJZXbEChUqc9Zx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49e319cd-bf9d-41e2-b88d-a97d9413be04",
  "isSidechain": false,
  "requestId": "req_011Cb8HS3NwwX61DN7uHaFiR",
  "type": "assistant",
  "uuid": "689c10b6-fc6c-43b6-86d9-c032084fbac6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtvbgHvbQmXdABmC8okJW5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 27339,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 333,
          "cache_read_input_tokens": 27339,
          "cache_creation_input_tokens": 2517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2517
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-17T14:17:21.236Z_

<details><summary>↩ Tool result · `toolu_01FgMXizQCcJZXbEChUqc9Zx`</summary>

```text
1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). We present the first controlled study isolating these factors in zero-shot LLM IE, spanning NER, RE, and event detection across four datasets, and operationalize confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS, the mean pairwise embedding similarity within a type batch). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) dominates confusability-related type substitution (${\approx}\,2.2$\,pp in typical batches); at batch level, BCS explains 22--53\% of cross-batch accuracy variance in RE but not in NER, where the signal is absent despite significant pairwise effects. Schema decomposition fails in both tasks due to merge amplification (NER) and routing failure (RE), which points to structural barriers to confusability-aware extraction.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "689c10b6-fc6c-43b6-86d9-c032084fbac6",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "71b86570-346e-4c55-92b1-ddcf3507ed32",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nTraining-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). We present the first controlled study isolating these factors in zero-shot LLM IE, spanning NER, RE, and event detection across four datasets, and operationalize confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS, the mean pairwise embedding similarity within a type batch). Degradation operates along two dimensions: count-related recall decline (up to $-$49\\,pp for document-level RE) dominates confusability-related type substitution (${\\approx}\\,2.2$\\,pp in typical batches); at batch level, BCS explains 22--53\\% of cross-batch accuracy variance in RE but not in NER, where the signal is absent despite significant pairwise effects. Schema decomposition fails in both tasks due to merge amplification (NER) and routing failure (RE), which points to structural barriers to confusability-aware extraction.\n\\end{abstract}\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  },
  "sourceToolAssistantUUID": "689c10b6-fc6c-43b6-86d9-c032084fbac6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-17T14:17:21.464Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M4bDAjc8hjeLcVGYuDrkGd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71b86570-346e-4c55-92b1-ddcf3507ed32",
  "isSidechain": false,
  "requestId": "req_011Cb8HS3NwwX61DN7uHaFiR",
  "type": "assistant",
  "uuid": "68efff6e-c3b5-4efc-9675-64a0b00661f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtvbgHvbQmXdABmC8okJW5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 27339,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 333,
          "cache_read_input_tokens": 27339,
          "cache_creation_input_tokens": 2517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2517
          },
          "type": "message"
        }
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

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的侧重**：方法严谨性 + 实验设计 + 统计分析  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **格式**: Long paper, 8 页正文, A…",
  "leafUuid": "e476121a-cefe-479c-a5bc-f717f7d9f3b9",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0"
}
```

---


### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Review schema complexity LLM information extraction paper",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0"
}
```

---


### Tool result

_source line 25 · 2026-05-17T14:17:26.412Z_

<details><summary>↩ Tool result · `toolu_01Gp13kVMQ3mi62JyPtEdAMY`</summary>

```text
Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here's information about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Recommendation Scale

The overall recommendation options are: 5 = Consider for Award (papers that could be considered for an outstanding paper award at an *ACL conference up to top 2.5% papers); 2 = Resubmit next cycle (paper needs substantial revisions that can be completed by the next ARR cycle); 1.5 = Resubmit after next cycle (paper needs substantial revisions that cannot be completed by the next ARR cycle); and 1 = Do not resubmit (paper has to be fully redone, or it is not relevant to the *ACL community).

## Key Review Form Elements

The review form includes assessments of:
- Whether authors have adequately discussed the limitations and potential positive and negative societal impacts of their work
- Ethical issues with the paper and whether it should be sent for in-depth ethics review
- Whether there is enough information in the paper for readers to reproduce the main results

## General Reviewing Principles

ARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference, so low scores may indicate the submission is not a good fit for ACL, even if it may be a good fit for other/more specialized venues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ecd85dc-b24a-46b5-9c3a-61f02d598cb1",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "435e3c7c-ce43-4b21-84fa-daa2d1d2e1d5",
  "toolUseResult": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TpzXdFZbCsb12LsjgLUGJT",
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
            "title": "ACLRollingReview (@ReviewAcl) / X",
            "url": "https://x.com/reviewacl"
          },
          {
            "title": "aclrollingreview/reviewing.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"
          }
        ]
      },
      "Based on the search results, here's information about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:\n\n## Reviewer Scoring Criteria\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.\n\n## Overall Recommendation Scale\n\nThe overall recommendation options are: 5 = Consider for Award (papers that could be considered for an outstanding paper award at an *ACL conference up to top 2.5% papers); 2 = Resubmit next cycle (paper needs substantial revisions that can be completed by the next ARR cycle); 1.5 = Resubmit after next cycle (paper needs substantial revisions that cannot be completed by the next ARR cycle); and 1 = Do not resubmit (paper has to be fully redone, or it is not relevant to the *ACL community).\n\n## Key Review Form Elements\n\nThe review form includes assessments of:\n- Whether authors have adequately discussed the limitations and potential positive and negative societal impacts of their work\n- Ethical issues with the paper and whether it should be sent for in-depth ethics review\n- Whether there is enough information in the paper for readers to reproduce the main results\n\n## General Reviewing Principles\n\nARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference, so low scores may indicate the submission is not a good fit for ACL, even if it may be a good fit for other/more specialized venues."
    ],
    "durationSeconds": 7.580604922000003
  },
  "sourceToolAssistantUUID": "2ecd85dc-b24a-46b5-9c3a-61f02d598cb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 26 · 2026-05-17T14:17:30.963Z_

<details><summary>Logged reasoning block</summary>

```text
Let me continue reading the other paper sections and fetch the ARR review form details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "435e3c7c-ce43-4b21-84fa-daa2d1d2e1d5",
  "isSidechain": false,
  "requestId": "req_011Cb8HT2JVVVy4i5ioQSGR9",
  "type": "assistant",
  "uuid": "84f05fa9-98c9-4b74-836b-71d434a211d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbtKq7nF681a2UaWMH94Z1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 18303,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 29856,
      "output_tokens": 385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 18303,
          "output_tokens": 385,
          "cache_read_input_tokens": 29856,
          "cache_creation_input_tokens": 1205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1205
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-17T14:17:32.031Z_

继续读取论文剩余章节并获取 ARR review form 细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84f05fa9-98c9-4b74-836b-71d434a211d5",
  "isSidechain": false,
  "requestId": "req_011Cb8HT2JVVVy4i5ioQSGR9",
  "type": "assistant",
  "uuid": "a189a8fe-8544-498b-86e8-486afdc85074",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbtKq7nF681a2UaWMH94Z1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 18303,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 29856,
      "output_tokens": 385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 18303,
          "output_tokens": 385,
          "cache_read_input_tokens": 29856,
          "cache_creation_input_tokens": 1205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1205
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-17T14:17:33.939Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M8HKSQjBkDRWwciz5C7kw7`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. Include all rating options and descriptions for each dimension (soundness, excitement, overall assessment, etc.)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a189a8fe-8544-498b-86e8-486afdc85074",
  "isSidechain": false,
  "requestId": "req_011Cb8HT2JVVVy4i5ioQSGR9",
  "type": "assistant",
  "uuid": "eaf8e831-3f79-443d-9f2e-ce0f11830d84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbtKq7nF681a2UaWMH94Z1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 18303,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 29856,
      "output_tokens": 385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 18303,
          "output_tokens": 385,
          "cache_read_input_tokens": 29856,
          "cache_creation_input_tokens": 1205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1205
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-17T14:17:35.923Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FG4zfHtg7kjkAkWUnhYUJp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eaf8e831-3f79-443d-9f2e-ce0f11830d84",
  "isSidechain": false,
  "requestId": "req_011Cb8HT2JVVVy4i5ioQSGR9",
  "type": "assistant",
  "uuid": "0c154ec7-1a3f-4442-9af0-54cf2334c071",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbtKq7nF681a2UaWMH94Z1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 18303,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 29856,
      "output_tokens": 385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 18303,
          "output_tokens": 385,
          "cache_read_input_tokens": 29856,
          "cache_creation_input_tokens": 1205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1205
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-17T14:17:35.935Z_

<details><summary>↩ Tool result · `toolu_01FG4zfHtg7kjkAkWUnhYUJp`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. Recent work also explores LLM-based data annotation for NER \cite{bogdanov2024nuner,zhang2023llmaaa} and self-improving zero-shot extraction \cite{xie2024selfimproving}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. Specifically, LLM-PEE employs union merge across sub-schema extractions, which our \S\ref{sec:sdgd} analysis shows is associated with precision collapsing from 0.56 to 0.21 in NER as false positives accumulate across passes; RE avoids this because closed-set classification does not require span reconciliation, explaining why LLM-PEE's decomposition succeeds for relation/event tasks but faces unresolved merge challenges on span-level extraction. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \cite{dee-2024}, and active prompting \cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation factors. Concurrently, \citet{haystack-to-needle-2025} reduces label spaces via iterative LLM filtering, an engineering complement to our analytical approach. Our framework explains \emph{why} such reduction works: it implicitly lowers batch confusability.
9	
10	\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\cite{rastogi2020towards} and SGD-X~\cite{lee2022sgd} document performance degradation with schema linguistic variation. \citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \citet{volkanovska2025ner} categorize LLM NER errors including type confusion. The relationship between label similarity and classification confusion has precedent in traditional ML: hierarchical classification suffers sibling confusion proportional to inter-class proximity \citep{deng-2010-imagenet}, label confusion matrices improve text classification \citep{guo-2021-label-confusion}, and classification confusion captures semantic similarity \citep{zhou-2025-rethinking}. Hierarchical label sets reduce class confusion in zero-shot image classification \citep{novack-2023-chils}; enriched type descriptions improve zero-shot NER \citep{cocchieri-2025-zeroner}, both orthogonal to our confusability-aware batching.
11	
12	\paragraph{SCS novelty.} SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion used in LLM-PEE~\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\%$) is consistent with standards for individual-difference predictors in behavioral research \citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \citep{lakens-2013-effect-size}.
13	
14	\paragraph{Embedding anisotropy.}
15	Our centrality confound (\S\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \cite{cai-isotropy-clusters-2021}, explaining why MAVEN's single-ontology types conflate confusability with centrality.
16	
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c154ec7-1a3f-4442-9af0-54cf2334c071",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "e2eb90f6-4ba3-456c-b9d6-448653f64d43",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Training-free LLM IE.}\nTraining-free LLM IE spans instruction tuning \\cite{instructuie-2023}, code-style schema encoding \\cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \\cite{gollie-2024,adelie-2024}, schema-driven decoding \\cite{slot-2025,oneke-2025}, and constrained JSON decoding \\cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \\cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \\cite{uniner-2024}, and bidirectional encoders \\cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \\cite{relationprompt-2022} and revisits relation extraction in the LLM era \\cite{wadhwa-re-llm-2023}. Recent work also explores LLM-based data annotation for NER \\cite{bogdanov2024nuner,zhang2023llmaaa} and self-improving zero-shot extraction \\cite{xie2024selfimproving}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.\n\n\\paragraph{Schema complexity in IE.}\nThe most directly related work is LLM-PEE \\cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. Specifically, LLM-PEE employs union merge across sub-schema extractions, which our \\S\\ref{sec:sdgd} analysis shows is associated with precision collapsing from 0.56 to 0.21 in NER as false positives accumulate across passes; RE avoids this because closed-set classification does not require span reconciliation, explaining why LLM-PEE's decomposition succeeds for relation/event tasks but faces unresolved merge challenges on span-level extraction. Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation factors. Concurrently, \\citet{haystack-to-needle-2025} reduces label spaces via iterative LLM filtering, an engineering complement to our analytical approach. Our framework explains \\emph{why} such reduction works: it implicitly lowers batch confusability.\n\n\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. \\citet{volkanovska2025ner} categorize LLM NER errors including type confusion. The relationship between label similarity and classification confusion has precedent in traditional ML: hierarchical classification suffers sibling confusion proportional to inter-class proximity \\citep{deng-2010-imagenet}, label confusion matrices improve text classification \\citep{guo-2021-label-confusion}, and classification confusion captures semantic similarity \\citep{zhou-2025-rethinking}. Hierarchical label sets reduce class confusion in zero-shot image classification \\citep{novack-2023-chils}; enriched type descriptions improve zero-shot NER \\citep{cocchieri-2025-zeroner}, both orthogonal to our confusability-aware batching.\n\n\\paragraph{SCS novelty.} SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion used in LLM-PEE~\\cite{llm-pee-2025} for schema decomposition. Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work. The modest pairwise effect size ($r^2 = 1.3$--$1.7\\%$) is consistent with standards for individual-difference predictors in behavioral research \\citep{cohen-1988-power}, where such magnitudes are considered ``small but real'' effects that compound at the aggregate level \\citep{lakens-2013-effect-size}.\n\n\\paragraph{Embedding anisotropy.}\nOur centrality confound (\\S\\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \\cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \\cite{cai-isotropy-clusters-2021}, explaining why MAVEN's single-ontology types conflate confusability with centrality.\n\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  },
  "sourceToolAssistantUUID": "0c154ec7-1a3f-4442-9af0-54cf2334c071",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 31 · 2026-05-17T14:17:36.416Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H6vVFpD1ZsaMiNi89zwCWr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2eb90f6-4ba3-456c-b9d6-448653f64d43",
  "isSidechain": false,
  "requestId": "req_011Cb8HT2JVVVy4i5ioQSGR9",
  "type": "assistant",
  "uuid": "44544bdb-cf62-4f9e-9525-73d0bf2e033d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbtKq7nF681a2UaWMH94Z1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 18303,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 29856,
      "output_tokens": 385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 18303,
          "output_tokens": 385,
          "cache_read_input_tokens": 29856,
          "cache_creation_input_tokens": 1205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1205
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-17T14:17:36.421Z_

<details><summary>↩ Tool result · `toolu_01H6vVFpD1ZsaMiNi89zwCWr`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound, making it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.
17	
18	\paragraph{MAVEN (ED).}
19	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.
20	
21	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{llrrlll}
28	\toprule
29	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embedding} \\
30	\midrule
31	Few-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\
32	FewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\
33	DocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\
34	MAVEN & ED & 168 & 18{,}904\rlap{$^\dagger$} & Same & 0.87--0.97 & MiniLM \\
35	\bottomrule
36	\end{tabular}}
37	\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}
38	\label{tab:datasets}
39	\end{table}
40	
41	\subsection{Schema Confusability Score (SCS)}
42	\label{sec:scs}
43	
44	We introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\text{name}(t)$, an embedding function $\text{embed}(\cdot)$ maps the type name to a vector representation. The \textbf{pairwise SCS} between types $t_i$ and $t_j$ is:
45	{\small
46	\[
47	\text{SCS}(t_i, t_j) = \cos\bigl(\text{embed}(\text{name}(t_i)),\; \text{embed}(\text{name}(t_j))\bigr)
48	\]
49	}
50	
51	For a batch of types $B = \{t_1, \ldots, t_k\}$, the \textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:
52	\[
53	\text{BCS}(B) = \frac{1}{\binom{k}{2}} \sum_{i < j,\; t_i, t_j \in B} \text{SCS}(t_i, t_j)
54	\]
55	
56	We compute SCS with two embedding models: (1)~Qwen3-32B \cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \cite{minilm-2020,sentence-bert-2019}, a 384-dimensional general-purpose sentence encoder. Few-NERD uses Qwen3 embeddings because its 66 fine-grained types include same-category pairs (e.g., ``person-artist'' vs.\ ``person-actor'') that MiniLM's 384-d space does not separate well; a cross-embedding check confirms directional consistency (MiniLM $r = 0.172$, Qwen3 $r = 0.138$; Appendix~\ref{sec:appendix_bcs_sensitivity}). SCS uses name-only embeddings as a practical simplification. We validate this choice empirically: name+definition SCS yields equivalent predictive accuracy ($\Delta r$: $-0.023$ to $+0.035$; Appendix~\ref{app:scs-ablation}), and for MAVEN/FewRel prompts that use type names without definitions, name-only SCS directly matches prompt content. We use MiniLM as the primary embedding for BCS computation because sentence-transformers are specifically trained for semantic similarity \cite{sentence-bert-2019}; a cross-embedding sensitivity check using Qwen3-32B causal-LM hidden states confirms directional consistency but with compressed BCS range (std${}\,=\,0.034$ vs.\ MiniLM std${}\,=\,0.081$), consistent with known autoregressive anisotropy \cite{ethayarajh-contextual-2019}.
57	
58	\paragraph{SCS as a lightweight proxy.}
59	\label{sec:scs-validation}
60	SCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on both NER and RE datasets (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\ref{tab:pairwise}). However, SCS is a partial proxy; context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\S\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.
61	
62	\subsection{Experimental Design}
63	\label{sec:exp_design}
64	
65	We conduct two complementary experimental paradigms.
66	
67	\paragraph{Experiment 1: Count Curves.}
68	We vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 25 random type batches for Few-NERD and FewRel (5 for DocRED and MAVEN) and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The remaining count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \{2, 6, 12, 22, 44, 66\} for Few-NERD, \{4, 8, 16, 32, 40, 64, 80\} for FewRel, \{4, 8, 16, 32, 64, 96\} for DocRED, and \{6, 12, 22, 44, 64\} for MAVEN.
69	
70	\paragraph{Experiment 2: BCS-Controlled.}
71	We fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\,\in\{6, 12\}$), FewRel (count$\,\in\{8, 16\}$, both 16-relation and 80-relation pools), and DocRED (count$\,\in\{16, 32\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\S\ref{sec:centrality_confound}).
72	
73	\subsection{Evaluation Metrics}
74	\label{sec:metrics}
75	
76	\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \emph{and} the type matches; partial spans count as incorrect. \textbf{RE}: accuracy (exact match of predicted relation label to gold). \textbf{ED}: relaxed F1, where any token overlap between predicted and gold trigger spans, with correct event type.
77	
78	
79	\subsection{Model and Inference}
80	\label{sec:model}
81	
82	We use Qwen3-32B-FP8 \cite{qwen3-2025} served via vLLM v0.20.2 \cite{vllm-2023} on a single NVIDIA RTX PRO 6000 GPU (96\,GB) with greedy decoding (temperature${}\,=\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints, doubling precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \cite{sclar-sensitivity-2024} (templates in Appendix~\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-70B-Instruct (FP8) and Meta-Llama-3.1-8B-Instruct \cite{llama3-2024}. All experiments use single-seed evaluation with greedy decoding, which substantially reduces model-level randomness (residual SD = 0.88\,pp at count 80 under greedy decoding, likely attributable to FP8 quantization non-determinism); bootstrap CIs capture the remaining sampling variance from batch composition. Pair-level CIs use percentile bootstrap ($B{=}10{,}000$); batch-level CIs use $B{=}1{,}000$.
83	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44544bdb-cf62-4f9e-9525-73d0bf2e033d",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "3c16cb23-c687-46e1-9f0e-25f4cddb34b9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.\n\n\\paragraph{FewRel (RE).}\nFewRel \\cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound, making it the primary dataset for BCS analysis.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\nWe introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2020,sentence-bert-2019}, a 384-dimensional general-purpose sentence encoder. Few-NERD uses Qwen3 embeddings because its 66 fine-grained types include same-category pairs (e.g., ``person-artist'' vs.\\ ``person-actor'') that MiniLM's 384-d space does not separate well; a cross-embedding check confirms directional consistency (MiniLM $r = 0.172$, Qwen3 $r = 0.138$; Appendix~\\ref{sec:appendix_bcs_sensitivity}). SCS uses name-only embeddings as a practical simplification. We validate this choice empirically: name+definition SCS yields equivalent predictive accuracy ($\\Delta r$: $-0.023$ to $+0.035$; Appendix~\\ref{app:scs-ablation}), and for MAVEN/FewRel prompts that use type names without definitions, name-only SCS directly matches prompt content. We use MiniLM as the primary embedding for BCS computation because sentence-transformers are specifically trained for semantic similarity \\cite{sentence-bert-2019}; a cross-embedding sensitivity check using Qwen3-32B causal-LM hidden states confirms directional consistency but with compressed BCS range (std${}\\,=\\,0.034$ vs.\\ MiniLM std${}\\,=\\,0.081$), consistent with known autoregressive anisotropy \\cite{ethayarajh-contextual-2019}.\n\n\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on both NER and RE datasets (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\\ref{tab:pairwise}). However, SCS is a partial proxy; context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\\S\\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 25 random type batches for Few-NERD and FewRel (5 for DocRED and MAVEN) and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The remaining count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{2, 6, 12, 22, 44, 66\\} for Few-NERD, \\{4, 8, 16, 32, 40, 64, 80\\} for FewRel, \\{4, 8, 16, 32, 64, 96\\} for DocRED, and \\{6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy (exact match of predicted relation label to gold). \\textbf{ED}: relaxed F1, where any token overlap between predicted and gold trigger spans, with correct event type.\n\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\nWe use Qwen3-32B-FP8 \\cite{qwen3-2025} served via vLLM v0.20.2 \\cite{vllm-2023} on a single NVIDIA RTX PRO 6000 GPU (96\\,GB) with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints, doubling precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\cite{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-70B-Instruct (FP8) and Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}. All experiments use single-seed evaluation with greedy decoding, which substantially reduces model-level randomness (residual SD = 0.88\\,pp at count 80 under greedy decoding, likely attributable to FP8 quantization non-determinism); bootstrap CIs capture the remaining sampling variance from batch composition. Pair-level CIs use percentile bootstrap ($B{=}10{,}000$); batch-level CIs use $B{=}1{,}000$.\n",
      "numLines": 83,
      "startLine": 1,
      "totalLines": 83
    }
  },
  "sourceToolAssistantUUID": "44544bdb-cf62-4f9e-9525-73d0bf2e033d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 33 · 2026-05-17T14:17:36.765Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EycrzSfVoMhYNujeWJyWZh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c16cb23-c687-46e1-9f0e-25f4cddb34b9",
  "isSidechain": false,
  "requestId": "req_011Cb8HT2JVVVy4i5ioQSGR9",
  "type": "assistant",
  "uuid": "3374e813-c657-4663-998f-8c0c81a11b16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbtKq7nF681a2UaWMH94Z1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 18303,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 29856,
      "output_tokens": 385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 18303,
          "output_tokens": 385,
          "cache_read_input_tokens": 29856,
          "cache_creation_input_tokens": 1205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1205
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-17T14:17:36.772Z_

<details><summary>↩ Tool result · `toolu_01EycrzSfVoMhYNujeWJyWZh`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves for NER and RE. Error bars show $\pm 1$\,SD across 3 seeds (42, 123, 456) $\times$ 25 batches per seed. RE accuracy declines monotonically with count; NER recall exhibits a U-shaped pattern with minimum at intermediate counts. Full-schema points (rightmost, hollow markers) represent the complete type inventory with no batch sampling variance. \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty. The pattern replicates across three seeds (42, 123, 456; max $\Delta = 10.7$\,pp, within 1\,SD); intra-batch variance exceeds inter-seed variance by ${>}$5$\times$ at every count level (Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$, pooled across three seeds). Count curves (25 batches per level) establish trend direction with error bars; magnitude estimation relies on the higher-powered BCS-controlled experiments (\S\ref{sec:bcs_controlled}).
25	
26	\subsection{Pairwise Confusability and Type Confusion}
27	\label{sec:pairwise}
28	
29	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\resizebox{\columnwidth}{!}{%
35	\begin{tabular}{llrrrrr}
36	\toprule
37	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \textbf{95\% CI} & \textbf{$p$} \\
38	\midrule
39	Few-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\,0.001$ \\
40	MAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\,0.001$ \\
41	\bottomrule
42	\end{tabular}}
43	\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\to}t_j) + C(t_j{\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \S\ref{sec:scs-validation}) is excluded as RE's per-instance format precludes direct comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]; both exclude zero, confirming robustness to within-type correlation.}
44	\label{tab:pairwise}
45	\end{table}
46	
47	The correlations are statistically significant but modest: $r^2 \approx 1.3\text{--}1.7\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\rho = 0.144\text{--}0.227$ across all pairs, strengthening to $\rho = 0.27\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).
48	
49	The remaining variance likely reflects entity frequency, prompt position \cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\,pp under typical batching (\S\ref{sec:practical_magnitude}). Notably, the independent MiniLM embedding yields a \emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\ Qwen3 $r = 0.138$; Appendix), suggesting that shared-representation bias is conservative rather than inflationary.
50	
51	\subsection{BCS-Controlled Experiments}
52	\label{sec:bcs_controlled}
53	
54	We fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\S\ref{sec:within_pool}) controls for pool composition.
55	
56	In BCS-controlled FewRel subsets, the high-BCS quartile shows $\Delta=-5.3$\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\,=\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\,pp at count 8, $-$31.8\,pp at count 16), confirming monotonic decline.
57	
58	\paragraph{Document-level RE (DocRED).}
59	The effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\,pp at count 16 (slope $= -0.713$, $\rho = -0.661$, $p < 0.001$) and $-$17.6\,pp at count 32 (slope $= -0.690$, $\rho = -0.509$, $p = 0.002$). BCS explains 44--53\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.
60	
61	\paragraph{Within-pool controlled comparison.}
62	\label{sec:within_pool}
63	Within-pool analysis confirms slope consistency across pools (permutation $p \approx 0.60$; Appendix~\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\S\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.
64	
65	\paragraph{Practical magnitude.}
66	\label{sec:practical_magnitude}
67	Direct regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$), scaling to 53\% at DocRED 96-rel. The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI: [0.4, 4.0]), roughly 7\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\% vs.\ 78.9\% for top-quartile ($\Delta = 3.9$\,pp). High mean-BCS batches contain more active confusable pairs, concentrating degradation. A post-hoc Monte Carlo simulation reproducing the observed ${\sim}3\times$ pair-to-batch amplification (conditional $R^2 \approx 7\%$ among non-zero confusion pairs to batch $R^2 \approx 22\%$; Appendix~\ref{app:aggregation-sim}) confirms this aggregation pattern.
68	
69	\paragraph{Cross-model validation.}
70	The effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\,pp (count 8) and $-$23.9\,pp (count 16), reaching 77--87\% of Qwen3-32B's gap. Both models converge to $\approx$51\% under high confusability regardless of count, while divergence is confined to the low-BCS regime, suggesting a task-inherent difficulty floor under high confusability (Table~\ref{tab:cross_model_bcs}). Dimension~1 replicates fully on Llama-3.1-8B (\S\ref{sec:count_curves}); Dimension~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1). Additional validation on Llama-3.1-70B-Instruct (FP8) confirms directional consistency across model scales (Appendix~\ref{sec:appendix_cross_model_70b}).
71	
72	\paragraph{Prompt sensitivity.}
73	Under the v2 prompt, the extreme-batch BCS gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; $n{=}25$; $r = -0.919$; $p < 0.001$), modestly attenuated from v1's extreme-batch gap but highly significant. NER shows no significant batch-level BCS--F1 correlation under either prompt version ($r \approx 0$, $n = 450$; \S\ref{sec:multi_channel}). Prompt design modulates magnitude but does not eliminate the RE effect (Appendix~\ref{sec:appendix_prompt_sensitivity}). The BCS--accuracy correlation holds across four structurally distinct prompt variants at count 32 (all $r \leq -0.47$; Appendix~\ref{sec:appendix_prompt_variants}), confirming that the confusability effect is not an artifact of prompt design.
74	
75	\subsection{Multi-Dimensional Degradation}
76	\label{sec:multi_channel}
77	
78	\begin{figure}[t]
79	\centering
80	\includegraphics[width=\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}
81	\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic.}
82	\label{fig:error_taxonomy}
83	\end{figure}
84	
85	Error taxonomy decomposition (Table~\ref{tab:error_taxonomy} and Figure~\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\rho = 1.0$ ($p < 0.001$) for NER and $\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches.
86	
87	These results establish two dimensions: \textbf{Dimension~1} (count predicts recall decline) and \textbf{Dimension~2} (confusability predicts type confusion), consistent with bounded association in RE but coupled in NER where type ambiguity and boundary ambiguity interact. The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \times 2$ factorial ($n = 54$) as a sensitivity check. Two One-Sided Tests (TOST) equivalence testing \citep{lakens-2017-equivalence} with a $\pm 3$\,pp margin ($p_{\text{TOST}} = 0.003$) confirms bounded association; sensitivity analysis at $\pm 2$\,pp and on the logit scale is reported in Appendix~\ref{sec:appendix_factorial}.
88	
89	\subsection{Centrality Confound on Homogeneous Schemas}
90	\label{sec:centrality_confound}
91	
92	Per-type analysis on MAVEN reveals an anomalous \emph{positive} BCS--F1 correlation (Qwen3 $\rho = +0.184$, $p = 0.025$; MiniLM $\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality: high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3374e813-c657-4663-998f-8c0c81a11b16",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "e4d04241-c87b-4ec2-babd-79441f500149",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves for NER and RE. Error bars show $\\pm 1$\\,SD across 3 seeds (42, 123, 456) $\\times$ 25 batches per seed. RE accuracy declines monotonically with count; NER recall exhibits a U-shaped pattern with minimum at intermediate counts. Full-schema points (rightmost, hollow markers) represent the complete type inventory with no batch sampling variance. \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nFigure~\\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\\%$\\to$38.7\\%, $-$56\\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty. The pattern replicates across three seeds (42, 123, 456; max $\\Delta = 10.7$\\,pp, within 1\\,SD); intra-batch variance exceeds inter-seed variance by ${>}$5$\\times$ at every count level (Appendix~\\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$, pooled across three seeds). Count curves (25 batches per level) establish trend direction with error bars; magnitude estimation relies on the higher-powered BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \\ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) is excluded as RE's per-instance format precludes direct comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]; both exclude zero, confirming robustness to within-type correlation.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\nThe remaining variance likely reflects entity frequency, prompt position \\cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching (\\S\\ref{sec:practical_magnitude}). Notably, the independent MiniLM embedding yields a \\emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\\ Qwen3 $r = 0.138$; Appendix), suggesting that shared-representation bias is conservative rather than inflationary.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nWe fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16), confirming monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\\,pp at count 16 (slope $= -0.713$, $\\rho = -0.661$, $p < 0.001$) and $-$17.6\\,pp at count 32 (slope $= -0.690$, $\\rho = -0.509$, $p = 0.002$). BCS explains 44--53\\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nDirect regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$), scaling to 53\\% at DocRED 96-rel. The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]), roughly 7\\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). High mean-BCS batches contain more active confusable pairs, concentrating degradation. A post-hoc Monte Carlo simulation reproducing the observed ${\\sim}3\\times$ pair-to-batch amplification (conditional $R^2 \\approx 7\\%$ among non-zero confusion pairs to batch $R^2 \\approx 22\\%$; Appendix~\\ref{app:aggregation-sim}) confirms this aggregation pattern.\n\n\\paragraph{Cross-model validation.}\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime, suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}). Dimension~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Dimension~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1). Additional validation on Llama-3.1-70B-Instruct (FP8) confirms directional consistency across model scales (Appendix~\\ref{sec:appendix_cross_model_70b}).\n\n\\paragraph{Prompt sensitivity.}\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; $n{=}25$; $r = -0.919$; $p < 0.001$), modestly attenuated from v1's extreme-batch gap but highly significant. NER shows no significant batch-level BCS--F1 correlation under either prompt version ($r \\approx 0$, $n = 450$; \\S\\ref{sec:multi_channel}). Prompt design modulates magnitude but does not eliminate the RE effect (Appendix~\\ref{sec:appendix_prompt_sensitivity}). The BCS--accuracy correlation holds across four structurally distinct prompt variants at count 32 (all $r \\leq -0.47$; Appendix~\\ref{sec:appendix_prompt_variants}), confirming that the confusability effect is not an artifact of prompt design.\n\n\\subsection{Multi-Dimensional Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.\n\nThese results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion), consistent with bounded association in RE but coupled in NER where type ambiguity and boundary ambiguity interact. The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. Two One-Sided Tests (TOST) equivalence testing \\citep{lakens-2017-equivalence} with a $\\pm 3$\\,pp margin ($p_{\\text{TOST}} = 0.003$) confirms bounded association; sensitivity analysis at $\\pm 2$\\,pp and on the logit scale is reported in Appendix~\\ref{sec:appendix_factorial}.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality: high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.",
      "numLines": 92,
      "startLine": 1,
      "totalLines": 92
    }
  },
  "sourceToolAssistantUUID": "3374e813-c657-4663-998f-8c0c81a11b16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的侧重**：方法严谨性 + 实验设计 + 统计分析  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **格式**: Long paper, 8 页正文, A…",
  "leafUuid": "e4d04241-c87b-4ec2-babd-79441f500149",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0"
}
```

---


### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Review schema complexity LLM information extraction paper",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0"
}
```

---


### Tool result

_source line 37 · 2026-05-17T14:17:39.936Z_

<details><summary>↩ Tool result · `toolu_01M8HKSQjBkDRWwciz5C7kw7`</summary>

```text
# ACL Rolling Review Form - Assessment Criteria

## Primary Scoring Dimensions

**Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: "Quite sure" with unlikely but conceivable oversights
- 3: "Pretty sure, but there's a chance I missed something"
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand"

**Soundness** (1-5 scale with half-point increments)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: "Strong: This study provides sufficient support for all of its claims"
- 3: "Acceptable: This study provides sufficient support for its main claims"
- 2: "Poor: Some of the main claims are not sufficiently supported"
- 1: "Major Issues: This study is not yet sufficiently thorough"

**Excitement** (1-5 scale with half-point increments)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: "Exciting: I would mention this paper to others"
- 3: "Interesting: I might mention some points to others"
- 2: "Potentially Interesting: does not resonate with me"
- 1: "Not Exciting: does not resonate with me"

**Overall Assessment** (1-5 scale with half-point increments)
- 5: Consider for Award (top 2.5%)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

**Secondary Dimensions:**
- Reproducibility (1-5)
- Dataset Value (1-5)
- Software Value (1-5)
- Author Identity Knowledge (1-5)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eaf8e831-3f79-443d-9f2e-ce0f11830d84",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "e5c85878-9a05-4e92-9df5-2eacbff836fe",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Assessment Criteria\n\n## Primary Scoring Dimensions\n\n**Reviewer Confidence** (1-5 scale)\n- 5: \"Positive that my evaluation is correct. I read the paper very carefully\"\n- 4: \"Quite sure\" with unlikely but conceivable oversights\n- 3: \"Pretty sure, but there's a chance I missed something\"\n- 2: \"Willing to defend my evaluation, but it is fairly likely that I missed some details\"\n- 1: \"Not my area, or paper is very hard to understand\"\n\n**Soundness** (1-5 scale with half-point increments)\n- 5: \"Excellent: This study is one of the most thorough I have seen\"\n- 4: \"Strong: This study provides sufficient support for all of its claims\"\n- 3: \"Acceptable: This study provides sufficient support for its main claims\"\n- 2: \"Poor: Some of the main claims are not sufficiently supported\"\n- 1: \"Major Issues: This study is not yet sufficiently thorough\"\n\n**Excitement** (1-5 scale with half-point increments)\n- 5: \"Highly Exciting: I would recommend this paper to others\"\n- 4: \"Exciting: I would mention this paper to others\"\n- 3: \"Interesting: I might mention some points to others\"\n- 2: \"Potentially Interesting: does not resonate with me\"\n- 1: \"Not Exciting: does not resonate with me\"\n\n**Overall Assessment** (1-5 scale with half-point increments)\n- 5: Consider for Award (top 2.5%)\n- 4: Conference acceptance\n- 3: Findings acceptance\n- 2: Resubmit next cycle\n- 1: Do not resubmit\n\n**Secondary Dimensions:**\n- Reproducibility (1-5)\n- Dataset Value (1-5)\n- Software Value (1-5)\n- Author Identity Knowledge (1-5)",
    "durationMs": 5992,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "eaf8e831-3f79-443d-9f2e-ce0f11830d84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 38 · 2026-05-17T14:17:39.945Z_

```json
{
  "parentUuid": "e5c85878-9a05-4e92-9df5-2eacbff836fe",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8e4a2c8a-9909-41c2-bf16-e34ca8b297da",
  "timestamp": "2026-05-17T14:17:39.945Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 39 · 2026-05-17T14:17:41.985Z_

<details><summary>Logged reasoning block</summary>

```text
Let me continue reading the remaining sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e4a2c8a-9909-41c2-bf16-e34ca8b297da",
  "isSidechain": false,
  "requestId": "req_011Cb8HU29bAqzxP4bZtdHcS",
  "type": "assistant",
  "uuid": "6a370930-dfdb-451c-8d19-9f0cd4a1c331",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHYdS5Th5w9X593TJjqZbR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 8865,
      "cache_creation_input_tokens": 19289,
      "cache_read_input_tokens": 31061,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19289,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 8865,
          "output_tokens": 282,
          "cache_read_input_tokens": 31061,
          "cache_creation_input_tokens": 19289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19289
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-17T14:17:43.020Z_

继续读取 SDGD 负面结果、Discussion 和 Checklist 部分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a370930-dfdb-451c-8d19-9f0cd4a1c331",
  "isSidechain": false,
  "requestId": "req_011Cb8HU29bAqzxP4bZtdHcS",
  "type": "assistant",
  "uuid": "15e6c703-ac90-47b2-b067-00f26840b12f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHYdS5Th5w9X593TJjqZbR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 8865,
      "cache_creation_input_tokens": 19289,
      "cache_read_input_tokens": 31061,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19289,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 8865,
          "output_tokens": 282,
          "cache_read_input_tokens": 31061,
          "cache_creation_input_tokens": 19289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19289
          },
          "type": "message"
        }
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

_source line 41 · 2026-05-17T14:17:45.017Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QfRsHa3XozT2X1Ar52PKc6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15e6c703-ac90-47b2-b067-00f26840b12f",
  "isSidechain": false,
  "requestId": "req_011Cb8HU29bAqzxP4bZtdHcS",
  "type": "assistant",
  "uuid": "777e9543-c70a-4dc6-aa85-8f8ae5aa145d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHYdS5Th5w9X593TJjqZbR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 8865,
      "cache_creation_input_tokens": 19289,
      "cache_read_input_tokens": 31061,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19289,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 8865,
          "output_tokens": 282,
          "cache_read_input_tokens": 31061,
          "cache_creation_input_tokens": 19289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19289
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-17T14:17:46.414Z_

<details><summary>↩ Tool result · `toolu_014TVY12wPXTpZwyB13ucihF`</summary>

```text
1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{llama3-2024}, vLLM \cite{vllm-2023}, and all-MiniLM-L6-v2 \cite{minilm-2020} are cited in \S\ref{sec:datasets} and \S\ref{sec:model}.
34	
35	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}
36	
37	Yes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Models are used under their respective open-weight licenses.
38	
39	\item \textbf{Did you discuss if your use of existing artifacts is consistent with their intended use?}
40	
41	Yes. All datasets are used for their intended purpose (IE evaluation). No data is used outside the scope specified by the dataset creators.
42	
43	\item \textbf{Did you discuss whether the data contains personally identifiable information or offensive content?}
44	
45	N/A. We use established benchmarks that have been vetted by the research community. No new data collection or annotation was performed.
46	
47	\item \textbf{Did you provide documentation of the artifacts, e.g., coverage of languages, coverage of domains, etc.?}
48	
49	Yes. Table~\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \S\ref{sec:datasets} describes dataset provenance and sampling procedures.
50	
51	\item \textbf{Did you report relevant statistics for your dataset(s)?}
52	
53	Yes. \S\ref{sec:datasets} and Table~\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \S\ref{sec:exp_design}.
54	
55	\end{enumerate}
56	
57	\subsection*{C \quad Computational Experiments}
58	
59	\begin{enumerate}[label=\textbf{C\arabic*.},leftmargin=*,itemsep=4pt]
60	
61	\item \textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}
62	
63	Yes. \S\ref{sec:model}: Qwen3-32B (32B parameters, FP8), Meta-Llama-3.1-70B-Instruct (70B parameters, FP8), and Meta-Llama-3.1-8B-Instruct (8B parameters). Inference was conducted on NVIDIA RTX PRO 6000 GPUs (96\,GB) served via vLLM. Total compute was approximately 72 GPU-hours of inference (no training).
64	
65	\item \textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}
66	
67	Yes. \S\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \S\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.
68	
69	\item \textbf{Did you report descriptive statistics about your results?}
70	
71	Yes. All key metrics include 95\% bootstrap confidence intervals (10{,}000 resamples, percentile method) as stated in \S\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \S\ref{sec:count_curves}--\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.
72	
73	\item \textbf{Did you report implementation details, e.g., versions of packages?}
74	
75	Yes. \S\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\S\ref{sec:scs}). Code and scripts will be released upon acceptance.
76	
77	\end{enumerate}
78	
79	\subsection*{D \quad Human Annotators or Crowdworkers}
80	
81	\begin{enumerate}[label=\textbf{D\arabic*.},leftmargin=*,itemsep=4pt]
82	
83	\item \textbf{Did you report the full text of instructions given to participants?}
84	
85	N/A. No human annotation or crowdsourcing was conducted.
86	
87	\item \textbf{Did you report information about how you recruited and paid participants?}
88	
89	N/A.
90	
91	\item \textbf{Did you discuss whether and how consent was obtained?}
92	
93	N/A.
94	
95	\item \textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}
96	
97	N/A.
98	
99	\item \textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}
100	
101	N/A.
102	
103	\end{enumerate}
104	
105	\subsection*{E \quad AI-Assisted Research}
106	
107	\begin{enumerate}[label=\textbf{E\arabic*.},leftmargin=*,itemsep=4pt]
108	
109	\item \textbf{Did you report the use of AI assistants?}
110	
111	Yes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.
112	
113	\end{enumerate}
114	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4929cc2-b085-4317-9cb0-76debdca7c28",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "d3140bd4-daa0-484b-a7c1-dbb1db836ecc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex",
      "content": "\\section*{Responsible NLP Research Checklist}\n\nFor each question, the answer is \\textbf{Yes}, \\textbf{No}, or \\textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.\n\n\\subsection*{A \\quad For Every Submission}\n\n\\begin{enumerate}[label=\\textbf{A\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you describe the limitations of your work?}\n\nYes. The Limitations section (after \\S\\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.\n\n\\item \\textbf{Did you discuss any potential risks of your work?}\n\nN/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.\n\n\\item \\textbf{Do the abstract and introduction summarize the paper's main claims?}\n\nYes. The abstract and \\S\\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.\n\n\\item \\textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}\n\nYes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.\n\n\\end{enumerate}\n\n\\subsection*{B \\quad Scientific Artifacts}\n\n\\begin{enumerate}[label=\\textbf{B\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you cite the creators of artifacts you used?}\n\nYes. Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, MAVEN \\cite{maven-2020}, Qwen3-32B \\cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}, vLLM \\cite{vllm-2023}, and all-MiniLM-L6-v2 \\cite{minilm-2020} are cited in \\S\\ref{sec:datasets} and \\S\\ref{sec:model}.\n\n\\item \\textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\n\nYes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Models are used under their respective open-weight licenses.\n\n\\item \\textbf{Did you discuss if your use of existing artifacts is consistent with their intended use?}\n\nYes. All datasets are used for their intended purpose (IE evaluation). No data is used outside the scope specified by the dataset creators.\n\n\\item \\textbf{Did you discuss whether the data contains personally identifiable information or offensive content?}\n\nN/A. We use established benchmarks that have been vetted by the research community. No new data collection or annotation was performed.\n\n\\item \\textbf{Did you provide documentation of the artifacts, e.g., coverage of languages, coverage of domains, etc.?}\n\nYes. Table~\\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \\S\\ref{sec:datasets} describes dataset provenance and sampling procedures.\n\n\\item \\textbf{Did you report relevant statistics for your dataset(s)?}\n\nYes. \\S\\ref{sec:datasets} and Table~\\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \\S\\ref{sec:exp_design}.\n\n\\end{enumerate}\n\n\\subsection*{C \\quad Computational Experiments}\n\n\\begin{enumerate}[label=\\textbf{C\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}\n\nYes. \\S\\ref{sec:model}: Qwen3-32B (32B parameters, FP8), Meta-Llama-3.1-70B-Instruct (70B parameters, FP8), and Meta-Llama-3.1-8B-Instruct (8B parameters). Inference was conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB) served via vLLM. Total compute was approximately 72 GPU-hours of inference (no training).\n\n\\item \\textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}\n\nYes. \\S\\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \\S\\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.\n\n\\item \\textbf{Did you report descriptive statistics about your results?}\n\nYes. All key metrics include 95\\% bootstrap confidence intervals (10{,}000 resamples, percentile method) as stated in \\S\\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \\S\\ref{sec:count_curves}--\\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.\n\n\\item \\textbf{Did you report implementation details, e.g., versions of packages?}\n\nYes. \\S\\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\\S\\ref{sec:scs}). Code and scripts will be released upon acceptance.\n\n\\end{enumerate}\n\n\\subsection*{D \\quad Human Annotators or Crowdworkers}\n\n\\begin{enumerate}[label=\\textbf{D\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the full text of instructions given to participants?}\n\nN/A. No human annotation or crowdsourcing was conducted.\n\n\\item \\textbf{Did you report information about how you recruited and paid participants?}\n\nN/A.\n\n\\item \\textbf{Did you discuss whether and how consent was obtained?}\n\nN/A.\n\n\\item \\textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}\n\nN/A.\n\n\\item \\textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}\n\nN/A.\n\n\\end{enumerate}\n\n\\subsection*{E \\quad AI-Assisted Research}\n\n\\begin{enumerate}[label=\\textbf{E\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the use of AI assistants?}\n\nYes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.\n\n\\end{enumerate}\n",
      "numLines": 114,
      "startLine": 1,
      "totalLines": 114
    }
  },
  "sourceToolAssistantUUID": "c4929cc2-b085-4317-9cb0-76debdca7c28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-17T14:17:45.024Z_

<details><summary>↩ Tool result · `toolu_01QfRsHa3XozT2X1Ar52PKc6`</summary>

```text
1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapsing (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}), confirming that type separation recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.); all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema (Appendix~\ref{sec:appendix_routing}).
11	
12	\paragraph{Future directions.}
13	Three avenues may address these bottlenecks: (1)~coarse-to-fine pipelines that screen with the full schema then refine with targeted sub-schemas; (2)~retrieval-based routing using document retrieval rather than LLM confidence for sub-schema assignment; (3)~calibrated generation to recover confidence signals eliminated by constrained decoding.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}lcc@{}}
20	\toprule
21	\textbf{Condition} & \textbf{Accuracy} & \textbf{Mean BCS} \\
22	\midrule
23	Single-pass (80 types) & 0.504 & 0.557 \\
24	Random batching (15 seeds)$^\dagger$ & 0.788\,$\pm$\,0.018 & 0.559 \\
25	Confus.-aware (graph coloring) & \textbf{0.802} & 0.552 \\
26	\bottomrule
27	\end{tabular}}
28	\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger$Mean $\pm$ SD across 15 random seeds.}
29	\label{tab:batch_composition}
30	\end{table}
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "777e9543-c70a-4dc6-aa85-8f8ae5aa145d",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "69dbe71b-5099-4a34-808b-fa3e8b67bce6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
      "content": "\\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}\n\\label{sec:sdgd}\n\nA natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \\textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.\n\n\\paragraph{NER: merge amplification.}\nAll decomposition modes fall below the single-pass NER baseline (F1\\,=\\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\\ref{sec:appendix_sdgd}). The core failure is \\emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapsing (0.563$\\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.\n\n\\paragraph{RE: oracle routing.}\nOracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\\,pp; Table~\\ref{tab:batch_composition}), confirming that type separation recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\\,pp over random ($p \\approx 0.19$, n.s.); all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema (Appendix~\\ref{sec:appendix_routing}).\n\n\\paragraph{Future directions.}\nThree avenues may address these bottlenecks: (1)~coarse-to-fine pipelines that screen with the full schema then refine with targeted sub-schemas; (2)~retrieval-based routing using document retrieval rather than LLM confidence for sub-schema assignment; (3)~calibrated generation to recover confidence signals eliminated by constrained decoding.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\end{table}\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  },
  "sourceToolAssistantUUID": "777e9543-c70a-4dc6-aa85-8f8ae5aa145d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-17T14:17:45.520Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JPiewXbHMgairPDRKiuobg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69dbe71b-5099-4a34-808b-fa3e8b67bce6",
  "isSidechain": false,
  "requestId": "req_011Cb8HU29bAqzxP4bZtdHcS",
  "type": "assistant",
  "uuid": "5e5178f5-c64e-4085-b7ea-c8022d15637d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHYdS5Th5w9X593TJjqZbR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 8865,
      "cache_creation_input_tokens": 19289,
      "cache_read_input_tokens": 31061,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19289,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 8865,
          "output_tokens": 282,
          "cache_read_input_tokens": 31061,
          "cache_creation_input_tokens": 19289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19289
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-17T14:17:45.524Z_

<details><summary>↩ Tool result · `toolu_01JPiewXbHMgairPDRKiuobg`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across models, suggesting a difficulty ceiling. RE's separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}). Cross-scale evidence (32B vs.\ 8B) shows Dimension~1 replicates fully while Dimension~2 attenuates on smaller models, dropping to near-zero $R^2$ for NER on Llama-3.1-8B (Tables~\ref{tab:cross_model}--\ref{tab:cross_model_bcs}). Count-related degradation may partly reflect prompt length (per-type recall 0.586 vs.\ single-pass 0.368, consistent with lost-in-middle effects; \citealt{lost-in-middle-2024}; \citealt{levy-2024-same-task}).
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pair-level effect is modest ($r^2 = 1.3$--$1.7\%$, as ${\sim}89\%$ of pairs never produce mutual confusion); among active-confusion pairs, $R^2 \approx 7\%$ amplifies ${\sim}3\times$ at batch level (Appendix~\ref{app:aggregation-sim}), yielding $R^2$ of 22--53\%. For individual type pairs, SCS is therefore a weak predictor; other factors such as frequency, context diversity, and definition quality dominate. At the batch level, however, these pair-level effects aggregate to produce the observed $R^2$ of 22--53\% in RE, sufficient for practical schema-level screening. We hypothesize that the NER U-shape (\S\ref{sec:count_curves}) reflects a dual-task burden absent in RE: partial schemas require simultaneous span detection and type-membership filtering; at full-schema, filtering becomes vacuous and recall recovers, confirming task-specific pathways.
9	
10	\paragraph{Task-dependent batch-level effects.}
11	While pairwise SCS predicts type confusion in both NER and RE, the batch-level BCS--performance relationship is RE-specific: BCS explains 22--53\% of cross-batch accuracy variance in RE but shows no significant correlation with NER F1 ($r \approx 0$, $n = 450$). We hypothesize this reflects the different error structures: RE errors are dominated by type substitution (IntraSub scales with BCS; \S\ref{sec:multi_channel}), so batch-level confusability directly predicts accuracy. NER errors are dominated by missed entities (43--65\% of errors), which correlate with count rather than confusability; pairwise SCS captures individual type confusion but this signal is diluted at the batch level by the overwhelming contribution of boundary detection failures. This task dependence has practical implications: BCS is a useful pre-hoc screening tool for RE schema design but not for NER, where count reduction is the primary lever.
12	
13	\paragraph{Practical implications.}
14	The bounded count$\times$confusability interaction (0.47\,pp, TOST $p = 0.003$) is itself an actionable finding: practitioners who scale schema size need not additionally worry about confusability amplification of count-related degradation. For RE deployment with cross-domain schemas, BCS provides a lightweight pre-hoc screen: schemas that exceed the top-quartile BCS threshold (mean pairwise SCS $> 0.59$) can expect 3--5\,pp lower accuracy, which can inform decisions about few-shot augmentation or schema redesign. For NER, count is the dominant predictor, and the primary mitigation strategy is to reduce schema size per prompt. Even few-shot demonstrations do not mitigate the confusability gap: under 5-shot prompting, the BCS penalty persists and slightly widens (+4.3\,pp over 0-shot, bootstrap $p = 0.014$), suggesting confusability is a structural property of the schema rather than a prompt engineering problem (Appendix~\ref{sec:appendix_fewshot_bcs}). These results apply to the training-free setting; fine-tuned models may learn type boundaries that reduce confusability effects.
15	
16	\section{Conclusion}
17	\label{sec:conclusion}
18	
19	Schema-induced degradation in training-free LLM extraction operates along two dimensions (count-related recall decline, confusability-related type confusion) with bounded association in RE but coupling in NER. Dimension~1 replicates across scales; Dimension~2 attenuates on smaller models. BCS enables pre-hoc screening.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e5178f5-c64e-4085-b7ea-c8022d15637d",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "b4f137d8-5061-4f51-ba51-4783f6c96717",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across models, suggesting a difficulty ceiling. RE's separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp; Appendix~\\ref{sec:appendix_prompt_sensitivity}). Cross-scale evidence (32B vs.\\ 8B) shows Dimension~1 replicates fully while Dimension~2 attenuates on smaller models, dropping to near-zero $R^2$ for NER on Llama-3.1-8B (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}). Count-related degradation may partly reflect prompt length (per-type recall 0.586 vs.\\ single-pass 0.368, consistent with lost-in-middle effects; \\citealt{lost-in-middle-2024}; \\citealt{levy-2024-same-task}).\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}\nSCS captures semantic proximity in LLMs' type-resolution space. The unconditional pair-level effect is modest ($r^2 = 1.3$--$1.7\\%$, as ${\\sim}89\\%$ of pairs never produce mutual confusion); among active-confusion pairs, $R^2 \\approx 7\\%$ amplifies ${\\sim}3\\times$ at batch level (Appendix~\\ref{app:aggregation-sim}), yielding $R^2$ of 22--53\\%. For individual type pairs, SCS is therefore a weak predictor; other factors such as frequency, context diversity, and definition quality dominate. At the batch level, however, these pair-level effects aggregate to produce the observed $R^2$ of 22--53\\% in RE, sufficient for practical schema-level screening. We hypothesize that the NER U-shape (\\S\\ref{sec:count_curves}) reflects a dual-task burden absent in RE: partial schemas require simultaneous span detection and type-membership filtering; at full-schema, filtering becomes vacuous and recall recovers, confirming task-specific pathways.\n\n\\paragraph{Task-dependent batch-level effects.}\nWhile pairwise SCS predicts type confusion in both NER and RE, the batch-level BCS--performance relationship is RE-specific: BCS explains 22--53\\% of cross-batch accuracy variance in RE but shows no significant correlation with NER F1 ($r \\approx 0$, $n = 450$). We hypothesize this reflects the different error structures: RE errors are dominated by type substitution (IntraSub scales with BCS; \\S\\ref{sec:multi_channel}), so batch-level confusability directly predicts accuracy. NER errors are dominated by missed entities (43--65\\% of errors), which correlate with count rather than confusability; pairwise SCS captures individual type confusion but this signal is diluted at the batch level by the overwhelming contribution of boundary detection failures. This task dependence has practical implications: BCS is a useful pre-hoc screening tool for RE schema design but not for NER, where count reduction is the primary lever.\n\n\\paragraph{Practical implications.}\nThe bounded count$\\times$confusability interaction (0.47\\,pp, TOST $p = 0.003$) is itself an actionable finding: practitioners who scale schema size need not additionally worry about confusability amplification of count-related degradation. For RE deployment with cross-domain schemas, BCS provides a lightweight pre-hoc screen: schemas that exceed the top-quartile BCS threshold (mean pairwise SCS $> 0.59$) can expect 3--5\\,pp lower accuracy, which can inform decisions about few-shot augmentation or schema redesign. For NER, count is the dominant predictor, and the primary mitigation strategy is to reduce schema size per prompt. Even few-shot demonstrations do not mitigate the confusability gap: under 5-shot prompting, the BCS penalty persists and slightly widens (+4.3\\,pp over 0-shot, bootstrap $p = 0.014$), suggesting confusability is a structural property of the schema rather than a prompt engineering problem (Appendix~\\ref{sec:appendix_fewshot_bcs}). These results apply to the training-free setting; fine-tuned models may learn type boundaries that reduce confusability effects.\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nSchema-induced degradation in training-free LLM extraction operates along two dimensions (count-related recall decline, confusability-related type confusion) with bounded association in RE but coupling in NER. Dimension~1 replicates across scales; Dimension~2 attenuates on smaller models. BCS enables pre-hoc screening.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  },
  "sourceToolAssistantUUID": "5e5178f5-c64e-4085-b7ea-c8022d15637d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-17T14:17:46.409Z_

<details open><summary>🔧 Tool call — Read · `toolu_014TVY12wPXTpZwyB13ucihF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4f137d8-5061-4f51-ba51-4783f6c96717",
  "isSidechain": false,
  "requestId": "req_011Cb8HU29bAqzxP4bZtdHcS",
  "type": "assistant",
  "uuid": "c4929cc2-b085-4317-9cb0-76debdca7c28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHYdS5Th5w9X593TJjqZbR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 8865,
      "cache_creation_input_tokens": 19289,
      "cache_read_input_tokens": 31061,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19289,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 8865,
          "output_tokens": 282,
          "cache_read_input_tokens": 31061,
          "cache_creation_input_tokens": 19289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19289
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的侧重**：方法严谨性 + 实验设计 + 统计分析  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **格式**: Long paper, 8 页正文, A…",
  "leafUuid": "d3140bd4-daa0-484b-a7c1-dbb1db836ecc",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0"
}
```

---


### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Review schema complexity LLM information extraction paper",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0"
}
```

---


### Assistant

_source line 49 · 2026-05-17T14:17:49.393Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the prompt appendix to complete my review of all paper sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3140bd4-daa0-484b-a7c1-dbb1db836ecc",
  "isSidechain": false,
  "requestId": "req_011Cb8HUWC4LjHYvk1N2ccpa",
  "type": "assistant",
  "uuid": "d68ea330-dde4-4917-839e-36eea726c3d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrrjnuETGg9npT6JSpH6sD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13403,
      "cache_read_input_tokens": 50350,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13403,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 225,
          "cache_read_input_tokens": 50350,
          "cache_creation_input_tokens": 13403,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13403
          },
          "type": "message"
        }
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

_source line 50 · 2026-05-17T14:17:49.926Z_

读取 prompt appendix 和 references 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d68ea330-dde4-4917-839e-36eea726c3d6",
  "isSidechain": false,
  "requestId": "req_011Cb8HUWC4LjHYvk1N2ccpa",
  "type": "assistant",
  "uuid": "aeef2b79-7ee3-42f3-8a32-9f1e16453809",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrrjnuETGg9npT6JSpH6sD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13403,
      "cache_read_input_tokens": 50350,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13403,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 225,
          "cache_read_input_tokens": 50350,
          "cache_creation_input_tokens": 13403,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13403
          },
          "type": "message"
        }
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

_source line 51 · 2026-05-17T14:17:51.902Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V7BxZ69XWCEXDpeSVTLHmG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aeef2b79-7ee3-42f3-8a32-9f1e16453809",
  "isSidechain": false,
  "requestId": "req_011Cb8HUWC4LjHYvk1N2ccpa",
  "type": "assistant",
  "uuid": "fa0fecb5-504f-425b-90eb-83cdf9a368d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrrjnuETGg9npT6JSpH6sD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13403,
      "cache_read_input_tokens": 50350,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13403,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 225,
          "cache_read_input_tokens": 50350,
          "cache_creation_input_tokens": 13403,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13403
          },
          "type": "message"
        }
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

_source line 52 · 2026-05-17T14:17:52.385Z_

<details><summary>↩ Tool result · `toolu_01DXvDhsMv5insYfxSj5mzri`</summary>

```text
1	% References for Schema-DAG-Extraction
2	% Generated: 2026-05-15
3	% Sources: literature_map.yaml + references_survey.md
4	
5	% =============================================================================
6	% DIRECT COMPETITORS
7	% =============================================================================
8	
9	@inproceedings{llm-pee-2025,
10	    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},
11	    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
12	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
13	    year      = {2025},
14	    url       = {https://aclanthology.org/2025.emnlp-main.1743/},
15	}
16	
17	@inproceedings{parse-2025,
18	    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},
19	    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},
20	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},
21	    year      = {2025},
22	    url       = {https://aclanthology.org/2025.emnlp-industry.184/},
23	}
24	
25	@inproceedings{dee-2024,
26	    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},
27	    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},
28	    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},
29	    year      = {2024},
30	    url       = {https://arxiv.org/abs/2406.01045},
31	}
32	
33	@inproceedings{crossagentie-2025,
34	    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},
35	    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},
36	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
37	    year      = {2025},
38	    url       = {https://aclanthology.org/2025.findings-acl.718/},
39	}
40	
41	
42	@inproceedings{cmas-ner-2025,
43	    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},
44	    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},
45	    booktitle = {Proceedings of the ACM Web Conference 2025},
46	    year      = {2025},
47	    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},
48	    doi       = {10.1145/3696410.3714923},
49	}
50	
51	% =============================================================================
52	% METHOD COMPONENTS
53	% =============================================================================
54	
55	@inproceedings{uniner-2024,
56	    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
57	    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
58	    booktitle = {International Conference on Learning Representations},
59	    year      = {2024},
60	    url       = {https://arxiv.org/abs/2308.03279},
61	}
62	
63	@inproceedings{gollie-2024,
64	    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
65	    author    = {Sainz, Oscar and Garc{\'\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},
66	    booktitle = {International Conference on Learning Representations},
67	    year      = {2024},
68	    url       = {https://arxiv.org/abs/2310.03668},
69	}
70	
71	@inproceedings{gliner-2024,
72	    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},
73	    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},
74	    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},
75	    year      = {2024},
76	    url       = {https://arxiv.org/abs/2311.08526},
77	}
78	
79	@inproceedings{gliner2-2025,
80	    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},
81	    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},
82	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},
83	    year      = {2025},
84	    url       = {https://aclanthology.org/2025.emnlp-demos.10/},
85	}
86	
87	
88	@inproceedings{iepile-2024,
89	    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},
90	    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},
91	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
92	    pages     = {127--146},
93	    year      = {2024},
94	    url       = {https://aclanthology.org/2024.acl-short.13/},
95	}
96	
97	@inproceedings{levy-2024-same-task,
98	    title     = {Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models},
99	    author    = {Levy, Mosh and Jacoby, Alon and Goldberg, Yoav},
100	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce94b5f9-d343-4728-a71f-f3a0a7ddcfcf",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "daa47529-95fc-4f9d-9b76-f66df1b82465",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
      "content": "% References for Schema-DAG-Extraction\n% Generated: 2026-05-15\n% Sources: literature_map.yaml + references_survey.md\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{dee-2024,\n    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},\n    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},\n    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2406.01045},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n@inproceedings{levy-2024-same-task,\n    title     = {Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models},\n    author    = {Levy, Mosh and Jacoby, Alon and Goldberg, Yoav},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 561
    }
  },
  "sourceToolAssistantUUID": "ce94b5f9-d343-4728-a71f-f3a0a7ddcfcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-17T14:17:51.911Z_

<details><summary>↩ Tool result · `toolu_01V7BxZ69XWCEXDpeSVTLHmG`</summary>

```text
1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the following text.
62	Only extract entities of the following types:
63	- {type_1}: {definition_1}
64	- {type_2}: {definition_2}
65	  ...
66	
67	Text: {input_text}
68	\end{lstlisting}
69	\end{small}
70	\vspace{-0.5em}
71	\noindent$\triangleright$~\textbf{Added in v2:}
72	\begin{small}
73	\begin{lstlisting}
74	Only extract entities that clearly match one of the
75	given types. If no entities of these types exist in
76	the text, output an empty list [].
77	\end{lstlisting}
78	\end{small}
79	\vspace{-0.5em}
80	\begin{small}
81	\begin{lstlisting}
82	Output as JSON: [{"text": "...", "type": "..."}]
83	\end{lstlisting}
84	\end{small}
85	
86	\noindent
87	\textbf{v2 constrained-decoding schema:}
88	\begin{small}
89	\begin{lstlisting}
90	{"type": "array",
91	 "items": {"type": "object",
92	   "properties": {
93	     "text": {"type": "string"},
94	     "type": {"type": "string",
95	              "enum": [&lt;sorted_types>]}},
96	   "required": ["text","type"]}}
97	\end{lstlisting}
98	\end{small}
99	
100	\paragraph{v1 $\to$ v2 differences (NER).}
101	\begin{enumerate}[leftmargin=*,itemsep=2pt]
102	\item \textbf{Offset fields removed.} The \texttt{start}/\texttt{end} integer fields are dropped from both the natural-language instruction and the JSON schema. In v1, 96.5\% of predicted offsets were hallucinated (\S\ref{sec:model}).
103	\item \textbf{Format constraints added.} Two sentences are appended: (a)~``Only extract entities that clearly match one of the given types'' suppresses spurious predictions; (b)~``If no entities \ldots output an empty list~\texttt{[]}'' provides an explicit empty-output path.
104	\end{enumerate}
105	
106	\subsection{Event Detection (MAVEN)}
107	
108	\paragraph{v1 prompt (with character offsets).}
109	
110	\begin{small}
111	\begin{lstlisting}
112	Extract all event triggers from the following text.
113	A trigger is the word or phrase that most clearly
114	expresses the event occurrence. Only extract triggers
115	of the following event types:
116	- {type_1}: {definition_1}
117	- {type_2}: {definition_2}
118	  ...
119	
120	Text: {input_text}
121	
122	Output as JSON: [{"text": "...", "type": "...",
123	                  "start": ..., "end": ...}]
124	\end{lstlisting}
125	\end{small}
126	
127	\paragraph{v2 prompt (text+type only).}
128	
129	\begin{small}
130	\begin{lstlisting}
131	Extract all event triggers from the following text.
132	A trigger is the word or phrase that most clearly
133	expresses the event occurrence. Only extract triggers
134	of the following event types:
135	- {type_1}: {definition_1}
136	- {type_2}: {definition_2}
137	  ...
138	
139	Text: {input_text}
140	\end{lstlisting}
141	\end{small}
142	\vspace{-0.5em}
143	\noindent$\triangleright$~\textbf{Added in v2:}
144	\begin{small}
145	\begin{lstlisting}
146	Only extract triggers that clearly match one of the
147	given event types. If no events of these types exist
148	in the text, output an empty list [].
149	\end{lstlisting}
150	\end{small}
151	\vspace{-0.5em}
152	\begin{small}
153	\begin{lstlisting}
154	Output as JSON: [{"text": "...", "type": "..."}]
155	\end{lstlisting}
156	\end{small}
157	
158	\noindent The JSON schemas for ED are identical to the NER schemas above; only the natural-language framing differs (``event triggers'' instead of ``named entities'').
159	
160	\paragraph{v1 $\to$ v2 differences (ED).}
161	Same two changes as NER: offset fields removed, format constraints added.
162	
163	\subsection{Relation Extraction (FewRel)}
164	
165	RE uses only a v2-style prompt (no offset fields are applicable to classification).
166	
167	\paragraph{Prompt.}
168	
169	\begin{small}
170	\begin{lstlisting}
171	Given the following sentence and two entities,
172	classify the relation between them.
173	
174	Sentence: "{sentence}"
175	Head entity: "{head_entity}"
176	Tail entity: "{tail_entity}"
177	
178	Candidate relations: {type_1}, {type_2}, ...
179	
180	Output a single JSON object:
181	  {"relation": "&lt;relation_type>"}
182	If none of the candidate relations apply, output:
183	  {"relation": "none"}
184	\end{lstlisting}
185	\end{small}
186	
187	\noindent
188	\textbf{Constrained-decoding schema:}
189	\begin{small}
190	\begin{lstlisting}
191	{"type": "object",
192	 "properties": {
193	   "relation": {"type": "string",
194	     "enum": [&lt;sorted_types>, "none"]}},
195	 "required": ["relation"]}
196	\end{lstlisting}
197	\end{small}
198	
199	\subsection{Type Definitions}
200	\label{sec:appendix_type_defs}
201	
202	All prompts include per-type natural-language definitions sourced from the respective dataset documentation:
203	\begin{itemize}[leftmargin=*,itemsep=2pt]
204	\item \textbf{Few-NERD:} 66 fine-grained entity types with definitions derived from the Few-NERD type ontology \cite{fewnerd-2021}.
205	\item \textbf{MAVEN:} 168 event types with FrameNet-based definitions \cite{maven-2020}.
206	\item \textbf{FewRel:} 80 relation types with Wikidata property descriptions \cite{fewrel-2018}.
207	\end{itemize}
208	
209	\noindent Type definitions are injected as ``\texttt{- \{type\_name\}: \{definition\}}'' lines in alphabetical order. The number of types per prompt varies by experimental condition (count${}= 1$ to full schema; \S\ref{sec:exp_design}).
210	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa0fecb5-504f-425b-90eb-83cdf9a368d1",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "cfc9f94c-deb1-4b34-a0a1-7752403cb70d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex",
      "content": "\\lstset{\n  basicstyle=\\ttfamily\\small,\n  breaklines=true,\n  breakatwhitespace=true,\n  columns=fullflexible\n}\n\n\\section{Prompt Templates}\n\\label{sec:appendix_prompts}\n\nThis appendix reproduces the complete prompt templates used for all three extraction tasks.\nAll prompts are injected into a single \\texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.\nBoth versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \\emph{not} included in the natural-language prompt itself.\nWe use greedy decoding (\\texttt{temperature=0}, \\texttt{seed=42}) throughout.\n\n\\medskip\\noindent\n\\textbf{Notation.}\nPlaceholders are shown in \\texttt{\\{braces\\}}.\nText \\textbf{added in v2} (relative to v1) is marked with $\\triangleright$.\nText \\textbf{removed in v2} is marked with \\sout{strikethrough}.\n\n\\subsection{Named Entity Recognition (Few-NERD)}\n\n\\paragraph{v1 prompt (with character offsets).}\n\n\\begin{small}\n\\begin{lstlisting}\nExtract all named entities from the following text.\nOnly extract entities of the following types:\n- {type_1}: {definition_1}\n- {type_2}: {definition_2}\n  ...\n\nText: {input_text}\n\nOutput as JSON: [{\"text\": \"...\", \"type\": \"...\",\n                  \"start\": ..., \"end\": ...}]\n\\end{lstlisting}\n\\end{small}\n\n\\noindent\n\\textbf{v1 constrained-decoding schema:}\n\\begin{small}\n\\begin{lstlisting}\n{\"type\": \"array\",\n \"items\": {\"type\": \"object\",\n   \"properties\": {\n     \"text\":  {\"type\": \"string\"},\n     \"type\":  {\"type\": \"string\",\n               \"enum\": [&lt;sorted_types>]},\n     \"start\": {\"type\": \"integer\"},\n     \"end\":   {\"type\": \"integer\"}},\n   \"required\": [\"text\",\"type\",\"start\",\"end\"]}}\n\\end{lstlisting}\n\\end{small}\n\n\\paragraph{v2 prompt (text+type only).}\n\n\\begin{small}\n\\begin{lstlisting}\nExtract all named entities from the following text.\nOnly extract entities of the following types:\n- {type_1}: {definition_1}\n- {type_2}: {definition_2}\n  ...\n\nText: {input_text}\n\\end{lstlisting}\n\\end{small}\n\\vspace{-0.5em}\n\\noindent$\\triangleright$~\\textbf{Added in v2:}\n\\begin{small}\n\\begin{lstlisting}\nOnly extract entities that clearly match one of the\ngiven types. If no entities of these types exist in\nthe text, output an empty list [].\n\\end{lstlisting}\n\\end{small}\n\\vspace{-0.5em}\n\\begin{small}\n\\begin{lstlisting}\nOutput as JSON: [{\"text\": \"...\", \"type\": \"...\"}]\n\\end{lstlisting}\n\\end{small}\n\n\\noindent\n\\textbf{v2 constrained-decoding schema:}\n\\begin{small}\n\\begin{lstlisting}\n{\"type\": \"array\",\n \"items\": {\"type\": \"object\",\n   \"properties\": {\n     \"text\": {\"type\": \"string\"},\n     \"type\": {\"type\": \"string\",\n              \"enum\": [&lt;sorted_types>]}},\n   \"required\": [\"text\",\"type\"]}}\n\\end{lstlisting}\n\\end{small}\n\n\\paragraph{v1 $\\to$ v2 differences (NER).}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Offset fields removed.} The \\texttt{start}/\\texttt{end} integer fields are dropped from both the natural-language instruction and the JSON schema. In v1, 96.5\\% of predicted offsets were hallucinated (\\S\\ref{sec:model}).\n\\item \\textbf{Format constraints added.} Two sentences are appended: (a)~``Only extract entities that clearly match one of the given types'' suppresses spurious predictions; (b)~``If no entities \\ldots output an empty list~\\texttt{[]}'' provides an explicit empty-output path.\n\\end{enumerate}\n\n\\subsection{Event Detection (MAVEN)}\n\n\\paragraph{v1 prompt (with character offsets).}\n\n\\begin{small}\n\\begin{lstlisting}\nExtract all event triggers from the following text.\nA trigger is the word or phrase that most clearly\nexpresses the event occurrence. Only extract triggers\nof the following event types:\n- {type_1}: {definition_1}\n- {type_2}: {definition_2}\n  ...\n\nText: {input_text}\n\nOutput as JSON: [{\"text\": \"...\", \"type\": \"...\",\n                  \"start\": ..., \"end\": ...}]\n\\end{lstlisting}\n\\end{small}\n\n\\paragraph{v2 prompt (text+type only).}\n\n\\begin{small}\n\\begin{lstlisting}\nExtract all event triggers from the following text.\nA trigger is the word or phrase that most clearly\nexpresses the event occurrence. Only extract triggers\nof the following event types:\n- {type_1}: {definition_1}\n- {type_2}: {definition_2}\n  ...\n\nText: {input_text}\n\\end{lstlisting}\n\\end{small}\n\\vspace{-0.5em}\n\\noindent$\\triangleright$~\\textbf{Added in v2:}\n\\begin{small}\n\\begin{lstlisting}\nOnly extract triggers that clearly match one of the\ngiven event types. If no events of these types exist\nin the text, output an empty list [].\n\\end{lstlisting}\n\\end{small}\n\\vspace{-0.5em}\n\\begin{small}\n\\begin{lstlisting}\nOutput as JSON: [{\"text\": \"...\", \"type\": \"...\"}]\n\\end{lstlisting}\n\\end{small}\n\n\\noindent The JSON schemas for ED are identical to the NER schemas above; only the natural-language framing differs (``event triggers'' instead of ``named entities'').\n\n\\paragraph{v1 $\\to$ v2 differences (ED).}\nSame two changes as NER: offset fields removed, format constraints added.\n\n\\subsection{Relation Extraction (FewRel)}\n\nRE uses only a v2-style prompt (no offset fields are applicable to classification).\n\n\\paragraph{Prompt.}\n\n\\begin{small}\n\\begin{lstlisting}\nGiven the following sentence and two entities,\nclassify the relation between them.\n\nSentence: \"{sentence}\"\nHead entity: \"{head_entity}\"\nTail entity: \"{tail_entity}\"\n\nCandidate relations: {type_1}, {type_2}, ...\n\nOutput a single JSON object:\n  {\"relation\": \"&lt;relation_type>\"}\nIf none of the candidate relations apply, output:\n  {\"relation\": \"none\"}\n\\end{lstlisting}\n\\end{small}\n\n\\noindent\n\\textbf{Constrained-decoding schema:}\n\\begin{small}\n\\begin{lstlisting}\n{\"type\": \"object\",\n \"properties\": {\n   \"relation\": {\"type\": \"string\",\n     \"enum\": [&lt;sorted_types>, \"none\"]}},\n \"required\": [\"relation\"]}\n\\end{lstlisting}\n\\end{small}\n\n\\subsection{Type Definitions}\n\\label{sec:appendix_type_defs}\n\nAll prompts include per-type natural-language definitions sourced from the respective dataset documentation:\n\\begin{itemize}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Few-NERD:} 66 fine-grained entity types with definitions derived from the Few-NERD type ontology \\cite{fewnerd-2021}.\n\\item \\textbf{MAVEN:} 168 event types with FrameNet-based definitions \\cite{maven-2020}.\n\\item \\textbf{FewRel:} 80 relation types with Wikidata property descriptions \\cite{fewrel-2018}.\n\\end{itemize}\n\n\\noindent Type definitions are injected as ``\\texttt{- \\{type\\_name\\}: \\{definition\\}}'' lines in alphabetical order. The number of types per prompt varies by experimental condition (count${}= 1$ to full schema; \\S\\ref{sec:exp_design}).\n",
      "numLines": 210,
      "startLine": 1,
      "totalLines": 210
    }
  },
  "sourceToolAssistantUUID": "fa0fecb5-504f-425b-90eb-83cdf9a368d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-17T14:17:52.380Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DXvDhsMv5insYfxSj5mzri`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfc9f94c-deb1-4b34-a0a1-7752403cb70d",
  "isSidechain": false,
  "requestId": "req_011Cb8HUWC4LjHYvk1N2ccpa",
  "type": "assistant",
  "uuid": "ce94b5f9-d343-4728-a71f-f3a0a7ddcfcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrrjnuETGg9npT6JSpH6sD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13403,
      "cache_read_input_tokens": 50350,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13403,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 225,
          "cache_read_input_tokens": 50350,
          "cache_creation_input_tokens": 13403,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13403
          },
          "type": "message"
        }
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

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的侧重**：方法严谨性 + 实验设计 + 统计分析  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **格式**: Long paper, 8 页正文, A…",
  "leafUuid": "daa47529-95fc-4f9d-9b76-f66df1b82465",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0"
}
```

---


### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Review schema complexity LLM information extraction paper",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0"
}
```

---


### Assistant

_source line 57 · 2026-05-17T14:17:56.222Z_

<details><summary>Logged reasoning block</summary>

```text
Let me also check the references.bib for completeness and see how many references there are, and run a reference verification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "daa47529-95fc-4f9d-9b76-f66df1b82465",
  "isSidechain": false,
  "requestId": "req_011Cb8HUx445T8WLFmiPZ1Uq",
  "type": "assistant",
  "uuid": "6973cbc4-bb19-454f-b814-fbe05aff47b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiFJy8vxUEKSUpACi6aBsb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4819,
      "cache_read_input_tokens": 63753,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4819,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 393,
          "cache_read_input_tokens": 63753,
          "cache_creation_input_tokens": 4819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4819
          },
          "type": "message"
        }
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

_source line 58 · 2026-05-17T14:17:57.670Z_

现在编译论文检查页数并验证引用。同时获取 ARR reviewer guidelines 的更多细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6973cbc4-bb19-454f-b814-fbe05aff47b0",
  "isSidechain": false,
  "requestId": "req_011Cb8HUx445T8WLFmiPZ1Uq",
  "type": "assistant",
  "uuid": "4c537cbe-5205-4296-aba5-00459dccc26f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiFJy8vxUEKSUpACi6aBsb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4819,
      "cache_read_input_tokens": 63753,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4819,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 393,
          "cache_read_input_tokens": 63753,
          "cache_creation_input_tokens": 4819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4819
          },
          "type": "message"
        }
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

_source line 59 · 2026-05-17T14:18:00.540Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01S1Gxaz2EFQf8fyWEoMRoCw`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including what reviewers should evaluate, common mistakes, scoring advice, and any specific instructions about how to assess papers. Include information about soundness criteria, novelty/excitement criteria, and overall assessment criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c537cbe-5205-4296-aba5-00459dccc26f",
  "isSidechain": false,
  "requestId": "req_011Cb8HUx445T8WLFmiPZ1Uq",
  "type": "assistant",
  "uuid": "37f617c3-c93b-490d-8c94-1de9663e6940",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiFJy8vxUEKSUpACi6aBsb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4819,
      "cache_read_input_tokens": 63753,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4819,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 393,
          "cache_read_input_tokens": 63753,
          "cache_creation_input_tokens": 4819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4819
          },
          "type": "message"
        }
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

_source line 60 · 2026-05-17T14:18:02.487Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_014Vestko3qMEGdTEeJLchNf`</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37f617c3-c93b-490d-8c94-1de9663e6940",
  "isSidechain": false,
  "requestId": "req_011Cb8HUx445T8WLFmiPZ1Uq",
  "type": "assistant",
  "uuid": "b536a17d-ad2f-4665-b9d3-ba680ccb0712",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiFJy8vxUEKSUpACi6aBsb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4819,
      "cache_read_input_tokens": 63753,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4819,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 393,
          "cache_read_input_tokens": 63753,
          "cache_creation_input_tokens": 4819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4819
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-17T14:18:03.377Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016JUTwkUX3vwbQodpfNMZ6R`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/*.tex",
  "description": "Count lines in all tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b536a17d-ad2f-4665-b9d3-ba680ccb0712",
  "isSidechain": false,
  "requestId": "req_011Cb8HUx445T8WLFmiPZ1Uq",
  "type": "assistant",
  "uuid": "960cb883-5fcb-4377-9a2b-aebcedef15a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiFJy8vxUEKSUpACi6aBsb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4819,
      "cache_read_input_tokens": 63753,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4819,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 393,
          "cache_read_input_tokens": 63753,
          "cache_creation_input_tokens": 4819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4819
          },
          "type": "message"
        }
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

_source line 62 · 2026-05-17T14:18:15.667Z_

<details><summary>↩ Tool result · `toolu_01S1Gxaz2EFQf8fyWEoMRoCw`</summary>

```text
# ARR Reviewer Guidelines Summary

## Core Reviewing Tasks

Reviewers must complete four main tasks:
1. **Allocate time** for reviewing and discussion periods
2. **Check assignments** for expertise, conflicts of interest, and desk-rejection criteria
3. **Write strong reviews** following specific quality standards
4. **Update assessments** after author responses and reviewer discussion

## What Reviewers Should Evaluate

### Soundness Assessment
Reviewers must ensure reviews with low soundness scores contain explicit justification. Papers should demonstrate "technical soundness, proof validity, sound argumentation, novelty, etc." Quality should reflect whether research "will advance the field" and whether methodology appropriately answers the stated research question.

### Excitement/Interest Assessment
This separate dimension captures personal interest levels and is "orthogonal to the assessment of the soundness of the paper." Reviewers may find work sound but personally uninteresting.

### Overall Recommendation
Composite scores reflecting soundness, excitement, novelty, and potential impact. Main conference papers must be "sufficiently sound and reproducible," though reviewers may recommend work for publication despite lower personal excitement if it has significant community value.

## Strong Review Standards

### Specificity (Critical)
Avoid vague criticism like "missing relevant references." Instead specify: "paper omits references X, Y, Z." Provide line numbers and concrete examples when possible.

### Professional Tone
Reviews must be "professional and neutral, if not kind." Acknowledge that authors may be early-career researchers facing stress. Write "the review you would like to get yourself."

### Read Twice
1. **Skim-read** to adjust expectations about research type before examining results
2. **In-depth read** to evaluate evidence and technical quality

## Common Reviewer Mistakes to Avoid

The guidelines identify 17 heuristics that lead to problematic reviews:

- **H1-H4**: Dismissing results as unsurprising, contradicting expectations, lacking novelty, or having no precedent
- **H5-H7**: Requiring SOTA performance, rejecting negative results, or demanding methodological complexity
- **H8-H11**: Imposing methodology preferences, niche-topic bias, non-English language skepticism, or fixating on writing quality
- **H12-H17**: Excessive reference demands, requesting unnecessary experiments, comparing to closed models without justification, expecting different approaches, or confusing limitations with weaknesses

## Common NLP Paper Problems to Identify

Reviewers should flag issues in five categories:

**Methodology (M)**: LLM evaluation validity, reproducibility gaps, undisclosed data quality, unmotivated selection, incomplete proofs

**Artifact Terms (T)**: Ethics concerns in data collection, unclear license/release conditions

**Results (R)**: Statistical analysis problems, inappropriate claim scope, speculation presented as conclusions, overclaiming, missing significance assessment

**General (G)**: Unclear research questions, bad precedent reliance, missing/misrepresented related work, vague terminology, misleading citations

## Scoring Guidance

- Scores must reflect review text—low soundness requires documented flaws
- Distinguish between technical soundness and personal interest levels
- Consider impact and value beyond SOTA metrics (efficiency, resources, interpretability, fairness)
- Acknowledge that resource papers and analyses are valid contributions

## Resubmission Review Standards

**Repeat reviewers** should confirm they read revision notes and assess whether previous concerns were adequately addressed—avoid raising new issues unless revisions created contradictory findings.

**Substitute reviewers** should categorize new concerns as: (i) previously identified weaknesses inadequately addressed, (ii) critical soundness issues, or (iii) suggestions for improvement.

**Fresh reviewers** should form independent opinions, then check whether previous reviews identified similar weaknesses and assess author responses.

## Confidentiality Requirements

- All submission information is confidential; avoid identifying papers in discussions
- Never upload manuscripts or review reports to non-privacy-preserving AI tools
- Disclose author identity if discovered, but don't actively search for it
- Reviewers may opt into anonymized data sharing for peer review research

## Policy Updates (2024-2025)

ARR now recognizes "great reviewers" with public recognition and potential free conference registration. Conversely, "highly irresponsible" reviewers submitting unmotivated reviews, LLM-generated content, or displaying professional misconduct face desk rejection and temporary bans from ARR participation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37f617c3-c93b-490d-8c94-1de9663e6940",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "eaf146d6-25e5-4143-9fdf-c35c2c43f5cb",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Reviewer Guidelines Summary\n\n## Core Reviewing Tasks\n\nReviewers must complete four main tasks:\n1. **Allocate time** for reviewing and discussion periods\n2. **Check assignments** for expertise, conflicts of interest, and desk-rejection criteria\n3. **Write strong reviews** following specific quality standards\n4. **Update assessments** after author responses and reviewer discussion\n\n## What Reviewers Should Evaluate\n\n### Soundness Assessment\nReviewers must ensure reviews with low soundness scores contain explicit justification. Papers should demonstrate \"technical soundness, proof validity, sound argumentation, novelty, etc.\" Quality should reflect whether research \"will advance the field\" and whether methodology appropriately answers the stated research question.\n\n### Excitement/Interest Assessment\nThis separate dimension captures personal interest levels and is \"orthogonal to the assessment of the soundness of the paper.\" Reviewers may find work sound but personally uninteresting.\n\n### Overall Recommendation\nComposite scores reflecting soundness, excitement, novelty, and potential impact. Main conference papers must be \"sufficiently sound and reproducible,\" though reviewers may recommend work for publication despite lower personal excitement if it has significant community value.\n\n## Strong Review Standards\n\n### Specificity (Critical)\nAvoid vague criticism like \"missing relevant references.\" Instead specify: \"paper omits references X, Y, Z.\" Provide line numbers and concrete examples when possible.\n\n### Professional Tone\nReviews must be \"professional and neutral, if not kind.\" Acknowledge that authors may be early-career researchers facing stress. Write \"the review you would like to get yourself.\"\n\n### Read Twice\n1. **Skim-read** to adjust expectations about research type before examining results\n2. **In-depth read** to evaluate evidence and technical quality\n\n## Common Reviewer Mistakes to Avoid\n\nThe guidelines identify 17 heuristics that lead to problematic reviews:\n\n- **H1-H4**: Dismissing results as unsurprising, contradicting expectations, lacking novelty, or having no precedent\n- **H5-H7**: Requiring SOTA performance, rejecting negative results, or demanding methodological complexity\n- **H8-H11**: Imposing methodology preferences, niche-topic bias, non-English language skepticism, or fixating on writing quality\n- **H12-H17**: Excessive reference demands, requesting unnecessary experiments, comparing to closed models without justification, expecting different approaches, or confusing limitations with weaknesses\n\n## Common NLP Paper Problems to Identify\n\nReviewers should flag issues in five categories:\n\n**Methodology (M)**: LLM evaluation validity, reproducibility gaps, undisclosed data quality, unmotivated selection, incomplete proofs\n\n**Artifact Terms (T)**: Ethics concerns in data collection, unclear license/release conditions\n\n**Results (R)**: Statistical analysis problems, inappropriate claim scope, speculation presented as conclusions, overclaiming, missing significance assessment\n\n**General (G)**: Unclear research questions, bad precedent reliance, missing/misrepresented related work, vague terminology, misleading citations\n\n## Scoring Guidance\n\n- Scores must reflect review text—low soundness requires documented flaws\n- Distinguish between technical soundness and personal interest levels\n- Consider impact and value beyond SOTA metrics (efficiency, resources, interpretability, fairness)\n- Acknowledge that resource papers and analyses are valid contributions\n\n## Resubmission Review Standards\n\n**Repeat reviewers** should confirm they read revision notes and assess whether previous concerns were adequately addressed—avoid raising new issues unless revisions created contradictory findings.\n\n**Substitute reviewers** should categorize new concerns as: (i) previously identified weaknesses inadequately addressed, (ii) critical soundness issues, or (iii) suggestions for improvement.\n\n**Fresh reviewers** should form independent opinions, then check whether previous reviews identified similar weaknesses and assess author responses.\n\n## Confidentiality Requirements\n\n- All submission information is confidential; avoid identifying papers in discussions\n- Never upload manuscripts or review reports to non-privacy-preserving AI tools\n- Disclose author identity if discovered, but don't actively search for it\n- Reviewers may opt into anonymized data sharing for peer review research\n\n## Policy Updates (2024-2025)\n\nARR now recognizes \"great reviewers\" with public recognition and potential free conference registration. Conversely, \"highly irresponsible\" reviewers submitting unmotivated reviews, LLM-generated content, or displaying professional misconduct face desk rejection and temporary bans from ARR participation.",
    "durationMs": 15120,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "37f617c3-c93b-490d-8c94-1de9663e6940",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-17T14:20:38.380Z_

<details><summary>↩ Tool result · `toolu_014Vestko3qMEGdTEeJLchNf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 59, \"total_citations\": 81, \"unique_cited_keys\": 55, \"orphan_bib\": 4, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 47, \"online_not_found\": 4, \"online_mismatch\": 8}, \"cross_check\": {\"orphan_bib\": [\"levy-2024-same-task\", \"llm-calibration-survey-2024\", \"perneger-1998\", \"wellek2010testing\"], \"missing_bib\": [], \"orphan_count\": 4, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"llm-pee-2025\", \"type\": \"inproceedings\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"authors\": \"Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin,...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"parse-2025\", \"type\": \"inproceedings\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"authors\": \"Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"dee-2024\", \"type\": \"inproceedings\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"authors\": \"Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the IEEE International Conference on Tools with Artificial Intell...\"}, {\"key\": \"crossagentie-2025\", \"type\": \"inproceedings\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"authors\": \"Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"cmas-ner-2025\", \"type\": \"inproceedings\", \"title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"authors\": \"Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maart...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM Web Conference 2025\"}, {\"key\": \"uniner-2024\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gollie-2024\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and Garc\\\\'\\\\ia-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacall...\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gliner-2024\", \"type\": \"inproceedings\", \"title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"authors\": \"Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"gliner2-2025\", \"type\": \"inproceedings\", \"title\": \"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\", \"authors\": \"Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"iepile-2024\", \"type\": \"inproceedings\", \"title\": \"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\", \"authors\": \"Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu an...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"levy-2024-same-task\", \"type\": \"inproceedings\", \"title\": \"Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models\", \"authors\": \"Levy, Mosh and Jacoby, Alon and Goldberg, Yoav\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"dror-2018-significance\", \"type\": \"inproceedings\", \"title\": \"The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing\", \"authors\": \"Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi\", \"year\": \"2018\", \"venue\": \"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lost-in-middle-2024\", \"type\": \"article\", \"title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"authors\": \"Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilac...\", \"year\": \"2024\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"llm4ie-survey-2024\", \"type\": \"article\", \"title\": \"Large Language Models for Generative Information Extraction: A Survey\", \"authors\": \"Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao,...\", \"year\": \"2024\", \"venue\": \"Frontiers of Computer Science\"}, {\"key\": \"knowcoder-2024\", \"type\": \"inproceedings\", \"title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"authors\": \"Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"slot-2025\", \"type\": \"inproceedings\", \"title\": \"SLOT: Structuring the Output of Large Language Models\", \"authors\": \"Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhic...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"gao-repr-degen-2019\", \"type\": \"inproceedings\", \"title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"authors\": \"Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan\", \"year\": \"2019\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"ethayarajh-contextual-2019\", \"type\": \"inproceedings\", \"title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"authors\": \"Ethayarajh, Kawin\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"type\": \"inproceedings\", \"title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"authors\": \"Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"instructuie-2023\", \"type\": \"article\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"authors\": \"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.08085\"}, {\"key\": \"codeie-2023\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"adelie-2024\", \"type\": \"inproceedings\", \"title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"authors\": \"Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juan...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"oneke-2025\", \"type\": \"inproceedings\", \"title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"authors\": \"Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and...\", \"year\": \"2025\", \"venue\": \"Companion Proceedings of the ACM Web Conference 2025\"}, {\"key\": \"llm-calibration-survey-2024\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"fewnerd-2021\", \"type\": \"inproceedings\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"authors\": \"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"fewrel-2018\", \"type\": \"inproceedings\", \"title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"authors\": \"Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiy...\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"maven-2020\", \"type\": \"inproceedings\", \"title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"authors\": \"Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"docred-2019\", \"type\": \"inproceedings\", \"title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"authors\": \"Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zheng...\", \"year\": \"2019\", \"venue\": \"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"qwen3-2025\", \"type\": \"article\", \"title\": \"Qwen3 Technical Report\", \"authors\": \"Qwen Team\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.09388\"}, {\"key\": \"llama3-2024\", \"type\": \"article\", \"title\": \"The Llama 3 Herd of Models\", \"authors\": \"Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek an...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21783\"}, {\"key\": \"sentence-bert-2019\", \"type\": \"inproceedings\", \"title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"authors\": \"Reimers, Nils and Gurevych, Iryna\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"minilm-2020\", \"type\": \"inproceedings\", \"title\": \"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\", \"authors\": \"Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, ...\", \"year\": \"2020\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"reflect-learn-2026\", \"type\": \"inproceedings\", \"title\": \"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\", \"authors\": \"Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang ...\", \"year\": \"2026\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"sclar-sensitivity-2024\", \"type\": \"inproceedings\", \"title\": \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design\", \"authors\": \"Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"vllm-2023\", \"type\": \"inproceedings\", \"title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"authors\": \"Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianm...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 29th Symposium on Operating Systems Principles\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"type\": \"inproceedings\", \"title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"authors\": \"Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, ...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"wadhwa-re-llm-2023\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"relationprompt-2022\", \"type\": \"inproceedings\", \"title\": \"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\", \"authors\": \"Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo\", \"year\": \"2022\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2022\"}, {\"key\": \"promptner-2023\", \"type\": \"article\", \"title\": \"PromptNER: Prompting For Named Entity Recognition\", \"authors\": \"Ashok, Dhananjay and Lipton, Zachary C.\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2305.15444\"}, {\"key\": \"json-schema-bench-2025\", \"type\": \"article\", \"title\": \"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\", \"authors\": \"Geng, Saibo and Cooper, Hudson and Moskal, Micha\\\\l and Jenkins, Samuel and Berma...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2501.10868\"}, {\"key\": \"rastogi2020towards\", \"type\": \"inproceedings\", \"title\": \"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\", \"authors\": \"Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and K...\", \"year\": \"2020\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"li2023evaluating\", \"type\": \"article\", \"title\": \"Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and...\", \"authors\": \"Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, ...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.11633\"}, {\"key\": \"lee2022sgd\", \"type\": \"inproceedings\", \"title\": \"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\", \"authors\": \"Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bi...\", \"year\": \"2022\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"volkanovska2025ner\", \"type\": \"article\", \"title\": \"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\", \"authors\": \"Volkanovska, Elena\", \"year\": \"2025\", \"venue\": \"Journal for Language Technology and Computational Linguistics\"}, {\"key\": \"haystack-to-needle-2025\", \"type\": \"article\", \"title\": \"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\", \"authors\": \"Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, ...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.08436\"}, {\"key\": \"cohen-1988-power\", \"type\": \"book\", \"title\": \"Statistical Power Analysis for the Behavioral Sciences\", \"authors\": \"Cohen, Jacob\", \"year\": \"1988\", \"venue\": \"\"}, {\"key\": \"lakens-2013-effect-size\", \"type\": \"article\", \"title\": \"Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and ANOVAs\", \"authors\": \"Lakens, Dani\\\\\\\"el\", \"year\": \"2013\", \"venue\": \"Frontiers in Psychology\"}, {\"key\": \"deng-2010-imagenet\", \"type\": \"inproceedings\", \"title\": \"What Does Classifying More Than 10,000 Image Categories Tell Us?\", \"authors\": \"Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li\", \"year\": \"2010\", \"venue\": \"Proceedings of the 11th European Conference on Computer Vision\"}, {\"key\": \"rothman-1990\", \"type\": \"article\", \"title\": \"No Adjustments Are Needed for Multiple Comparisons\", \"authors\": \"Rothman, Kenneth J.\", \"year\": \"1990\", \"venue\": \"Epidemiology\"}, {\"key\": \"lakens-2017-equivalence\", \"type\": \"article\", \"title\": \"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\", \"authors\": \"Lakens, Dani\\\\\\\"el\", \"year\": \"2017\", \"venue\": \"Social Psychological and Personality Science\"}, {\"key\": \"perneger-1998\", \"type\": \"article\", \"title\": \"What's Wrong with Bonferroni Adjustments\", \"authors\": \"Perneger, Thomas V.\", \"year\": \"1998\", \"venue\": \"BMJ\"}, {\"key\": \"zhou-2025-rethinking\", \"type\": \"inproceedings\", \"title\": \"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\", \"authors\": \"Zhou, Kaitlyn and Gao, Haishan and Chen, Sarah Li and Edelstein, Dan and Jurafsk...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"guo-2021-label-confusion\", \"type\": \"inproceedings\", \"title\": \"Label Confusion Learning to Enhance Text Classification Models\", \"authors\": \"Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting\", \"year\": \"2021\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"novack-2023-chils\", \"type\": \"inproceedings\", \"title\": \"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\", \"authors\": \"Novack, Zachary and McAuley, Julian and Lipton, Zachary Chase and Garg, Saurabh\", \"year\": \"2023\", \"venue\": \"Proceedings of the 40th International Conference on Machine Learning\"}, {\"key\": \"cocchieri-2025-zeroner\", \"type\": \"inproceedings\", \"title\": \"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\", \"authors\": \"Cocchieri, Alessio and Mart\\\\'\\\\inez Galindo, Marcos and Frisoni, Giacomo and Moro...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"bogdanov2024nuner\", \"type\": \"inproceedings\", \"title\": \"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\", \"authors\": \"Bogdanov, Sergei and Constantin, Alexandre and Bernard, Timoth\\\\'ee and Crabb\\\\'e,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"xie2024selfimproving\", \"type\": \"inproceedings\", \"title\": \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\", \"authors\": \"Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"zhang2023llmaaa\", \"type\": \"inproceedings\", \"title\": \"LLMaAA: Making Large Language Models as Active Annotators\", \"authors\": \"Zhang, Ruoyu and Li, Yanzeng and Ma, Yongliang and Zhou, Ming and Zou, Lei\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2023\"}, {\"key\": \"wellek2010testing\", \"type\": \"book\", \"title\": \"Testing Statistical Hypotheses of Equivalence and Noninferiority\", \"authors\": \"Wellek, Stefan\", \"year\": \"2010\", \"venue\": \"\"}], \"tex_citations\": [{\"key\": \"llm4ie-survey-2024\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"uniner-2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"llm-pee-2025\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"parse-2025\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"fewnerd-2021\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"docred-2019\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"instructuie-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"knowcoder-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"codeie-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gollie-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"adelie-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"slot-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"oneke-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"json-schema-bench-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"promptner-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"uniner-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gliner-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gliner2-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"relationprompt-2022\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wadhwa-re-llm-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"bogdanov2024nuner\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"zhang2023llmaaa\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"xie2024selfimproving\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"llm-pee-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"iepile-2024\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"parse-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"crossagentie-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"cmas-ner-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"dee-2024\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"reflect-learn-2026\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"haystack-to-needle-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"rastogi2020towards\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"lee2022sgd\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"li2023evaluating\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citet\"}, {\"key\": \"volkanovska2025ner\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citet\"}, {\"key\": \"deng-2010-imagenet\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"guo-2021-label-confusion\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"zhou-2025-rethinking\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"novack-2023-chils\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"cocchieri-2025-zeroner\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"llm-pee-2025\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"cohen-1988-power\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"lakens-2013-effect-size\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"gao-repr-degen-2019\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"ethayarajh-contextual-2019\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"fewnerd-2021\", \"file\": \"experimental_setup.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"experimental_setup.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"docred-2019\", \"file\": \"experimental_setup.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"experimental_setup.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"qwen3-2025\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"minilm-2020\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"sentence-bert-2019\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"sentence-bert-2019\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"ethayarajh-contextual-2019\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"qwen3-2025\", \"file\": \"experimental_setup.tex\", \"line\": 82, \"command\": \"cite\"}, {\"key\": \"vllm-2023\", \"file\": \"experimental_setup.tex\", \"line\": 82, \"command\": \"cite\"}, {\"key\": \"sclar-sensitivity-2024\", \"file\": \"experimental_setup.tex\", \"line\": 82, \"command\": \"cite\"}, {\"key\": \"llama3-2024\", \"file\": \"experimental_setup.tex\", \"line\": 82, \"command\": \"cite\"}, {\"key\": \"lost-in-middle-2024\", \"file\": \"results.tex\", \"line\": 49, \"command\": \"cite\"}, {\"key\": \"lakens-2017-equivalence\", \"file\": \"results.tex\", \"line\": 87, \"command\": \"citep\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"file\": \"results.tex\", \"line\": 92, \"command\": \"cite\"}, {\"key\": \"rothman-1990\", \"file\": \"main.tex\", \"line\": 57, \"command\": \"citep\"}, {\"key\": \"dror-2018-significance\", \"file\": \"main.tex\", \"line\": 57, \"command\": \"citep\"}, {\"key\": \"fewnerd-2021\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"docred-2019\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"qwen3-2025\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"llama3-2024\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"vllm-2023\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"minilm-2020\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"fewnerd-2021\", \"file\": \"prompt_appendix.tex\", \"line\": 204, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"prompt_appendix.tex\", \"line\": 205, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"prompt_appendix.tex\", \"line\": 206, \"command\": \"cite\"}, {\"key\": \"rothman-1990\", \"file\": \"main.tex\", \"line\": 307, \"command\": \"citep\"}, {\"key\": \"li2023evaluating\", \"file\": \"main.tex\", \"line\": 468, \"command\": \"citet\"}, {\"key\": \"lost-in-middle-2024\", \"file\": \"main.tex\", \"line\": 531, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"llm-pee-2025\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=liu vs api=2025\"], \"note\": \"\"}, {\"key\": \"parse-2025\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dee-2024\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"crossagentie-2025\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=lu vs api=meng\"], \"note\": \"\"}, {\"key\": \"cmas-ner-2025\", \"title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"uniner-2024\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gollie-2024\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gliner-2024\", \"title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gliner2-2025\", \"title\": \"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=zaratiana vs api=2025\"], \"note\": \"\"}, {\"key\": \"iepile-2024\", \"title\": \"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"levy-2024-same-task\", \"title\": \"Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dror-2018-significance\", \"title\": \"The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing\", \"status\": \"not_found\", \"confidence\": 0.339, \"matched_title\": \"The Sorcerer II Global Ocean Sampling Expedition: Northwest Atlantic through Eastern Tropical Pacific\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"lost-in-middle-2024\", \"title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"llm4ie-survey-2024\", \"title\": \"Large Language Models for Generative Information Extraction: A Survey\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large language models for generative information extraction: a survey\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"knowcoder-2024\", \"title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"slot-2025\", \"title\": \"SLOT: Structuring the Output of Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"SLOT: Structuring the Output of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=shen vs api=wang\"], \"note\": \"\"}, {\"key\": \"gao-repr-degen-2019\", \"title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ethayarajh-contextual-2019\", \"title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"instructuie-2023\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"codeie-2023\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"adelie-2024\", \"title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oneke-2025\", \"title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"llm-calibration-survey-2024\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fewnerd-2021\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fewrel-2018\", \"title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"maven-2020\", \"title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"docred-2019\", \"title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen3-2025\", \"title\": \"Qwen3 Technical Report\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Qwen3 Technical Report\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=team vs api=yang\"], \"note\": \"\"}, {\"key\": \"llama3-2024\", \"title\": \"The Llama 3 Herd of Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"The Llama 3 herd of models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=dubey vs api=aaron\"], \"note\": \"\"}, {\"key\": \"sentence-bert-2019\", \"title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"minilm-2020\", \"title\": \"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"reflect-learn-2026\", \"title\": \"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Reflect Then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\", \"matched_year\": \"2026\", \"mismatch_fields\": [\"first_author: bib=zhao vs api=2026\"], \"note\": \"\"}, {\"key\": \"sclar-sensitivity-2024\", \"title\": \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design\", \"status\": \"not_found\", \"confidence\": 0.72, \"matched_title\": \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.72 below threshold 0.82\"}, {\"key\": \"vllm-2023\", \"title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa-re-llm-2023\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"relationprompt-2022\", \"title\": \"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"promptner-2023\", \"title\": \"PromptNER: Prompting For Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"PromptNER: Prompting For Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"json-schema-bench-2025\", \"title\": \"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"rastogi2020towards\", \"title\": \"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023evaluating\", \"title\": \"Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness\", \"status\": \"not_found\", \"confidence\": 0.333, \"matched_title\": \"Generative AI in Medical Practice: In-Depth Exploration of Privacy and Security Challenges\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"lee2022sgd\", \"title\": \"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"volkanovska2025ner\", \"title\": \"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"haystack-to-needle-2025\", \"title\": \"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cohen-1988-power\", \"title\": \"Statistical Power Analysis for the Behavioral Sciences\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Statistical Power Analysis for the Behavioral Sciences\", \"matched_year\": \"1989\", \"mismatch_fields\": [\"first_author: bib=cohen vs api=muller\"], \"note\": \"\"}, {\"key\": \"lakens-2013-effect-size\", \"title\": \"Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and ANOVAs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs\", \"matched_year\": \"2013\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"deng-2010-imagenet\", \"title\": \"What Does Classifying More Than 10,000 Image Categories Tell Us?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"What Does Classifying More Than 10,000 Image Categories Tell Us?\", \"matched_year\": \"2010\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"rothman-1990\", \"title\": \"No Adjustments Are Needed for Multiple Comparisons\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"No Adjustments Are Needed for Multiple Comparisons\", \"matched_year\": \"1990\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lakens-2017-equivalence\", \"title\": \"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\", \"status\": \"verified\", \"confidence\": 0.988, \"matched_title\": \"Equivalence Tests: A Practical Primer for t-Tests, Correlations, and Meta-Analyses\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"perneger-1998\", \"title\": \"What's Wrong with Bonferroni Adjustments\", \"status\": \"not_found\", \"confidence\": 0.33, \"matched_title\": \"A Comparative Study of Unit Root Tests with Panel Data and a New Simple Test\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"zhou-2025-rethinking\", \"title\": \"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo-2021-label-confusion\", \"title\": \"Label Confusion Learning to Enhance Text Classification Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Label Confusion Learning to Enhance Text Classification Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"novack-2023-chils\", \"title\": \"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cocchieri-2025-zeroner\", \"title\": \"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bogdanov2024nuner\", \"title\": \"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie2024selfimproving\", \"title\": \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2023llmaaa\", \"title\": \"LLMaAA: Making Large Language Models as Active Annotators\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMaAA: Making Large Language Models as Active Annotators\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wellek2010testing\", \"title\": \"Testing Statistical Hypotheses of Equivalence and Noninferiority\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Testing Statistical Hypotheses of Equivalence and Noninferiority\", \"matched_year\": \"2010\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b536a17d-ad2f-4665-b9d3-ba680ccb0712",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "1c53033b-3ce4-4551-8a0b-666597cf6016",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 59, \\\"total_citations\\\": 81, \\\"unique_cited_keys\\\": 55, \\\"orphan_bib\\\": 4, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 47, \\\"online_not_found\\\": 4, \\\"online_mismatch\\\": 8}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [\\\"levy-2024-same-task\\\", \\\"llm-calibration-survey-2024\\\", \\\"perneger-1998\\\", \\\"wellek2010testing\\\"], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 4, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"llm-pee-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\", \\\"authors\\\": \\\"Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin,...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"parse-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\", \\\"authors\\\": \\\"Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"dee-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\", \\\"authors\\\": \\\"Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari,...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the IEEE International Conference on Tools with Artificial Intell...\\\"}, {\\\"key\\\": \\\"crossagentie-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\\\", \\\"authors\\\": \\\"Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"cmas-ner-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\", \\\"authors\\\": \\\"Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maart...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the ACM Web Conference 2025\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"gollie-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"authors\\\": \\\"Sainz, Oscar and Garc\\\\\\\\'\\\\\\\\ia-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacall...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"gliner-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\", \\\"authors\\\": \\\"Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"gliner2-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\\\", \\\"authors\\\": \\\"Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"iepile-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\\\", \\\"authors\\\": \\\"Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu an...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"levy-2024-same-task\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models\\\", \\\"authors\\\": \\\"Levy, Mosh and Jacoby, Alon and Goldberg, Yoav\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"dror-2018-significance\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing\\\", \\\"authors\\\": \\\"Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"lost-in-middle-2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Lost in the Middle: How Language Models Use Long Contexts\\\", \\\"authors\\\": \\\"Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilac...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"llm4ie-survey-2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Language Models for Generative Information Extraction: A Survey\\\", \\\"authors\\\": \\\"Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao,...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Frontiers of Computer Science\\\"}, {\\\"key\\\": \\\"knowcoder-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\\\", \\\"authors\\\": \\\"Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"slot-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SLOT: Structuring the Output of Large Language Models\\\", \\\"authors\\\": \\\"Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhic...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"gao-repr-degen-2019\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\", \\\"authors\\\": \\\"Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"ethayarajh-contextual-2019\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\", \\\"authors\\\": \\\"Ethayarajh, Kawin\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"cai-isotropy-clusters-2021\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\", \\\"authors\\\": \\\"Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"instructuie-2023\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"authors\\\": \\\"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2304.08085\\\"}, {\\\"key\\\": \\\"codeie-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"authors\\\": \\\"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"adelie-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ADELIE: Aligning Large Language Models on Information Extraction\\\", \\\"authors\\\": \\\"Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juan...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"oneke-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\\\", \\\"authors\\\": \\\"Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Companion Proceedings of the ACM Web Conference 2025\\\"}, {\\\"key\\\": \\\"llm-calibration-survey-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"authors\\\": \\\"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"authors\\\": \\\"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\\\", \\\"authors\\\": \\\"Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiy...\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"MAVEN: A Massive General Domain Event Detection Dataset\\\", \\\"authors\\\": \\\"Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"docred-2019\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\\\", \\\"authors\\\": \\\"Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zheng...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Qwen3 Technical Report\\\", \\\"authors\\\": \\\"Qwen Team\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2505.09388\\\"}, {\\\"key\\\": \\\"llama3-2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"The Llama 3 Herd of Models\\\", \\\"authors\\\": \\\"Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek an...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2407.21783\\\"}, {\\\"key\\\": \\\"sentence-bert-2019\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\", \\\"authors\\\": \\\"Reimers, Nils and Gurevych, Iryna\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"minilm-2020\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\\\", \\\"authors\\\": \\\"Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, ...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"reflect-learn-2026\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\\\", \\\"authors\\\": \\\"Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang ...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"sclar-sensitivity-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design\\\", \\\"authors\\\": \\\"Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"vllm-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Efficient Memory Management for Large Language Model Serving with PagedAttention\\\", \\\"authors\\\": \\\"Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianm...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 29th Symposium on Operating Systems Principles\\\"}, {\\\"key\\\": \\\"xie-zeroshot-ner-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Empirical Study of Zero-Shot NER with ChatGPT\\\", \\\"authors\\\": \\\"Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, ...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"wadhwa-re-llm-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"authors\\\": \\\"Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"relationprompt-2022\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\\\", \\\"authors\\\": \\\"Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2022\\\"}, {\\\"key\\\": \\\"promptner-2023\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"PromptNER: Prompting For Named Entity Recognition\\\", \\\"authors\\\": \\\"Ashok, Dhananjay and Lipton, Zachary C.\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2305.15444\\\"}, {\\\"key\\\": \\\"json-schema-bench-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\\\", \\\"authors\\\": \\\"Geng, Saibo and Cooper, Hudson and Moskal, Micha\\\\\\\\l and Jenkins, Samuel and Berma...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2501.10868\\\"}, {\\\"key\\\": \\\"rastogi2020towards\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\\\", \\\"authors\\\": \\\"Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and K...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"li2023evaluating\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and...\\\", \\\"authors\\\": \\\"Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, ...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2304.11633\\\"}, {\\\"key\\\": \\\"lee2022sgd\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\\\", \\\"authors\\\": \\\"Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bi...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"volkanovska2025ner\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\\\", \\\"authors\\\": \\\"Volkanovska, Elena\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Journal for Language Technology and Computational Linguistics\\\"}, {\\\"key\\\": \\\"haystack-to-needle-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\\\", \\\"authors\\\": \\\"Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2502.08436\\\"}, {\\\"key\\\": \\\"cohen-1988-power\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Statistical Power Analysis for the Behavioral Sciences\\\", \\\"authors\\\": \\\"Cohen, Jacob\\\", \\\"year\\\": \\\"1988\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"lakens-2013-effect-size\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and ANOVAs\\\", \\\"authors\\\": \\\"Lakens, Dani\\\\\\\\\\\\\\\"el\\\", \\\"year\\\": \\\"2013\\\", \\\"venue\\\": \\\"Frontiers in Psychology\\\"}, {\\\"key\\\": \\\"deng-2010-imagenet\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"What Does Classifying More Than 10,000 Image Categories Tell Us?\\\", \\\"authors\\\": \\\"Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li\\\", \\\"year\\\": \\\"2010\\\", \\\"venue\\\": \\\"Proceedings of the 11th European Conference on Computer Vision\\\"}, {\\\"key\\\": \\\"rothman-1990\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"No Adjustments Are Needed for Multiple Comparisons\\\", \\\"authors\\\": \\\"Rothman, Kenneth J.\\\", \\\"year\\\": \\\"1990\\\", \\\"venue\\\": \\\"Epidemiology\\\"}, {\\\"key\\\": \\\"lakens-2017-equivalence\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\\\", \\\"authors\\\": \\\"Lakens, Dani\\\\\\\\\\\\\\\"el\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Social Psychological and Personality Science\\\"}, {\\\"key\\\": \\\"perneger-1998\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"What's Wrong with Bonferroni Adjustments\\\", \\\"authors\\\": \\\"Perneger, Thomas V.\\\", \\\"year\\\": \\\"1998\\\", \\\"venue\\\": \\\"BMJ\\\"}, {\\\"key\\\": \\\"zhou-2025-rethinking\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\\\", \\\"authors\\\": \\\"Zhou, Kaitlyn and Gao, Haishan and Chen, Sarah Li and Edelstein, Dan and Jurafsk...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"guo-2021-label-confusion\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Label Confusion Learning to Enhance Text Classification Models\\\", \\\"authors\\\": \\\"Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"novack-2023-chils\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\\\", \\\"authors\\\": \\\"Novack, Zachary and McAuley, Julian and Lipton, Zachary Chase and Garg, Saurabh\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 40th International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"cocchieri-2025-zeroner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\\\", \\\"authors\\\": \\\"Cocchieri, Alessio and Mart\\\\\\\\'\\\\\\\\inez Galindo, Marcos and Frisoni, Giacomo and Moro...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"bogdanov2024nuner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\", \\\"authors\\\": \\\"Bogdanov, Sergei and Constantin, Alexandre and Bernard, Timoth\\\\\\\\'ee and Crabb\\\\\\\\'e,...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"xie2024selfimproving\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\", \\\"authors\\\": \\\"Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"zhang2023llmaaa\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LLMaAA: Making Large Language Models as Active Annotators\\\", \\\"authors\\\": \\\"Zhang, Ruoyu and Li, Yanzeng and Ma, Yongliang and Zhou, Ming and Zou, Lei\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: EMNLP 2023\\\"}, {\\\"key\\\": \\\"wellek2010testing\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Testing Statistical Hypotheses of Equivalence and Noninferiority\\\", \\\"authors\\\": \\\"Wellek, Stefan\\\", \\\"year\\\": \\\"2010\\\", \\\"venue\\\": \\\"\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"llm4ie-survey-2024\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"parse-2025\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"docred-2019\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"instructuie-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"knowcoder-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"codeie-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gollie-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"adelie-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"slot-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"oneke-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"json-schema-bench-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xie-zeroshot-ner-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"promptner-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gliner-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gliner2-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"relationprompt-2022\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wadhwa-re-llm-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"bogdanov2024nuner\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2023llmaaa\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xie2024selfimproving\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"iepile-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"parse-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"crossagentie-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cmas-ner-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dee-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"reflect-learn-2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"haystack-to-needle-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"rastogi2020towards\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lee2022sgd\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2023evaluating\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"volkanovska2025ner\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"deng-2010-imagenet\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"guo-2021-label-confusion\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zhou-2025-rethinking\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"novack-2023-chils\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cocchieri-2025-zeroner\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cohen-1988-power\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"lakens-2013-effect-size\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gao-repr-degen-2019\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ethayarajh-contextual-2019\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cai-isotropy-clusters-2021\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"docred-2019\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"minilm-2020\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sentence-bert-2019\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sentence-bert-2019\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ethayarajh-contextual-2019\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 82, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"vllm-2023\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 82, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sclar-sensitivity-2024\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 82, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"llama3-2024\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 82, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lost-in-middle-2024\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 49, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lakens-2017-equivalence\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 87, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cai-isotropy-clusters-2021\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 92, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"rothman-1990\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 57, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"dror-2018-significance\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 57, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"docred-2019\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"llama3-2024\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"vllm-2023\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"minilm-2020\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"file\\\": \\\"prompt_appendix.tex\\\", \\\"line\\\": 204, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"file\\\": \\\"prompt_appendix.tex\\\", \\\"line\\\": 205, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"file\\\": \\\"prompt_appendix.tex\\\", \\\"line\\\": 206, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"rothman-1990\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 307, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"li2023evaluating\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 468, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"lost-in-middle-2024\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 531, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"llm-pee-2025\\\", \\\"title\\\": \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=liu vs api=2025\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"parse-2025\\\", \\\"title\\\": \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dee-2024\\\", \\\"title\\\": \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"crossagentie-2025\\\", \\\"title\\\": \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=lu vs api=meng\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cmas-ner-2025\\\", \\\"title\\\": \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gollie-2024\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gliner-2024\\\", \\\"title\\\": \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gliner2-2025\\\", \\\"title\\\": \\\"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=zaratiana vs api=2025\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"iepile-2024\\\", \\\"title\\\": \\\"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"levy-2024-same-task\\\", \\\"title\\\": \\\"Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dror-2018-significance\\\", \\\"title\\\": \\\"The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.339, \\\"matched_title\\\": \\\"The Sorcerer II Global Ocean Sampling Expedition: Northwest Atlantic through Eastern Tropical Pacific\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.34 below threshold 0.82\\\"}, {\\\"key\\\": \\\"lost-in-middle-2024\\\", \\\"title\\\": \\\"Lost in the Middle: How Language Models Use Long Contexts\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Lost in the Middle: How Language Models Use Long Contexts\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"llm4ie-survey-2024\\\", \\\"title\\\": \\\"Large Language Models for Generative Information Extraction: A Survey\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large language models for generative information extraction: a survey\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"knowcoder-2024\\\", \\\"title\\\": \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"slot-2025\\\", \\\"title\\\": \\\"SLOT: Structuring the Output of Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SLOT: Structuring the Output of Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=shen vs api=wang\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gao-repr-degen-2019\\\", \\\"title\\\": \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ethayarajh-contextual-2019\\\", \\\"title\\\": \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cai-isotropy-clusters-2021\\\", \\\"title\\\": \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"instructuie-2023\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"codeie-2023\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"adelie-2024\\\", \\\"title\\\": \\\"ADELIE: Aligning Large Language Models on Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ADELIE: Aligning Large Language Models on Information Extraction\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"oneke-2025\\\", \\\"title\\\": \\\"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"llm-calibration-survey-2024\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"title\\\": \\\"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"title\\\": \\\"MAVEN: A Massive General Domain Event Detection Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"MAVEN: A Massive General Domain Event Detection Dataset\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"docred-2019\\\", \\\"title\\\": \\\"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"title\\\": \\\"Qwen3 Technical Report\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Qwen3 Technical Report\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=team vs api=yang\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"llama3-2024\\\", \\\"title\\\": \\\"The Llama 3 Herd of Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Llama 3 herd of models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=dubey vs api=aaron\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sentence-bert-2019\\\", \\\"title\\\": \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"minilm-2020\\\", \\\"title\\\": \\\"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"reflect-learn-2026\\\", \\\"title\\\": \\\"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reflect Then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=zhao vs api=2026\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sclar-sensitivity-2024\\\", \\\"title\\\": \\\"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.72, \\\"matched_title\\\": \\\"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.72 below threshold 0.82\\\"}, {\\\"key\\\": \\\"vllm-2023\\\", \\\"title\\\": \\\"Efficient Memory Management for Large Language Model Serving with PagedAttention\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Memory Management for Large Language Model Serving with PagedAttention\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xie-zeroshot-ner-2023\\\", \\\"title\\\": \\\"Empirical Study of Zero-Shot NER with ChatGPT\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Empirical Study of Zero-Shot NER with ChatGPT\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wadhwa-re-llm-2023\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"relationprompt-2022\\\", \\\"title\\\": \\\"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"promptner-2023\\\", \\\"title\\\": \\\"PromptNER: Prompting For Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"PromptNER: Prompting For Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"json-schema-bench-2025\\\", \\\"title\\\": \\\"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"rastogi2020towards\\\", \\\"title\\\": \\\"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2023evaluating\\\", \\\"title\\\": \\\"Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.333, \\\"matched_title\\\": \\\"Generative AI in Medical Practice: In-Depth Exploration of Privacy and Security Challenges\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.33 below threshold 0.82\\\"}, {\\\"key\\\": \\\"lee2022sgd\\\", \\\"title\\\": \\\"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"volkanovska2025ner\\\", \\\"title\\\": \\\"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"haystack-to-needle-2025\\\", \\\"title\\\": \\\"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cohen-1988-power\\\", \\\"title\\\": \\\"Statistical Power Analysis for the Behavioral Sciences\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Statistical Power Analysis for the Behavioral Sciences\\\", \\\"matched_year\\\": \\\"1989\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=cohen vs api=muller\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lakens-2013-effect-size\\\", \\\"title\\\": \\\"Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and ANOVAs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs\\\", \\\"matched_year\\\": \\\"2013\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"deng-2010-imagenet\\\", \\\"title\\\": \\\"What Does Classifying More Than 10,000 Image Categories Tell Us?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"What Does Classifying More Than 10,000 Image Categories Tell Us?\\\", \\\"matched_year\\\": \\\"2010\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"rothman-1990\\\", \\\"title\\\": \\\"No Adjustments Are Needed for Multiple Comparisons\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"No Adjustments Are Needed for Multiple Comparisons\\\", \\\"matched_year\\\": \\\"1990\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lakens-2017-equivalence\\\", \\\"title\\\": \\\"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.988, \\\"matched_title\\\": \\\"Equivalence Tests: A Practical Primer for t-Tests, Correlations, and Meta-Analyses\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"perneger-1998\\\", \\\"title\\\": \\\"What's Wrong with Bonferroni Adjustments\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.33, \\\"matched_title\\\": \\\"A Comparative Study of Unit Root Tests with Panel Data and a New Simple Test\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.33 below threshold 0.82\\\"}, {\\\"key\\\": \\\"zhou-2025-rethinking\\\", \\\"title\\\": \\\"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"guo-2021-label-confusion\\\", \\\"title\\\": \\\"Label Confusion Learning to Enhance Text Classification Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Label Confusion Learning to Enhance Text Classification Models\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"novack-2023-chils\\\", \\\"title\\\": \\\"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cocchieri-2025-zeroner\\\", \\\"title\\\": \\\"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"bogdanov2024nuner\\\", \\\"title\\\": \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xie2024selfimproving\\\", \\\"title\\\": \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2023llmaaa\\\", \\\"title\\\": \\\"LLMaAA: Making Large Language Models as Active Annotators\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLMaAA: Making Large Language Models as Active Annotators\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wellek2010testing\\\", \\\"title\\\": \\\"Testing Statistical Hypotheses of Equivalence and Noninferiority\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Testing Statistical Hypotheses of Equivalence and Noninferiority\\\", \\\"matched_year\\\": \\\"2010\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 59, \"total_citations\": 81, \"unique_cited_keys\": 55, \"orphan_bib\": 4, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 47, \"online_not_found\": 4, \"online_mismatch\": 8}, \"cross_check\": {\"orphan_bib\": [\"levy-2024-same-task\", \"llm-calibration-survey-2024\", \"perneger-1998\", \"wellek2010testing\"], \"missing_bib\": [], \"orphan_count\": 4, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"llm-pee-2025\", \"type\": \"inproceedings\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"authors\": \"Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin,...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"parse-2025\", \"type\": \"inproceedings\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"authors\": \"Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"dee-2024\", \"type\": \"inproceedings\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"authors\": \"Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the IEEE International Conference on Tools with Artificial Intell...\"}, {\"key\": \"crossagentie-2025\", \"type\": \"inproceedings\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"authors\": \"Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"cmas-ner-2025\", \"type\": \"inproceedings\", \"title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"authors\": \"Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maart...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM Web Conference 2025\"}, {\"key\": \"uniner-2024\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gollie-2024\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and Garc\\\\'\\\\ia-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacall...\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gliner-2024\", \"type\": \"inproceedings\", \"title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"authors\": \"Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"gliner2-2025\", \"type\": \"inproceedings\", \"title\": \"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\", \"authors\": \"Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"iepile-2024\", \"type\": \"inproceedings\", \"title\": \"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\", \"authors\": \"Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu an...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"levy-2024-same-task\", \"type\": \"inproceedings\", \"title\": \"Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models\", \"authors\": \"Levy, Mosh and Jacoby, Alon and Goldberg, Yoav\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"dror-2018-significance\", \"type\": \"inproceedings\", \"title\": \"The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing\", \"authors\": \"Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi\", \"year\": \"2018\", \"venue\": \"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lost-in-middle-2024\", \"type\": \"article\", \"title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"authors\": \"Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilac...\", \"year\": \"2024\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"llm4ie-survey-2024\", \"type\": \"article\", \"title\": \"Large Language Models for Generative Information Extraction: A Survey\", \"authors\": \"Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao,...\", \"year\": \"2024\", \"venue\": \"Frontiers of Computer Science\"}, {\"key\": \"knowcoder-2024\", \"type\": \"inproceedings\", \"title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"authors\": \"Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"slot-2025\", \"type\": \"inproceedings\", \"title\": \"SLOT: Structuring the Output of Large Language Models\", \"authors\": \"Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhic...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"gao-repr-degen-2019\", \"type\": \"inproceedings\", \"title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"authors\": \"Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan\", \"year\": \"2019\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"ethayarajh-contextual-2019\", \"type\": \"inproceedings\", \"title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"authors\": \"Ethayarajh, Kawin\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"type\": \"inproceedings\", \"title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"authors\": \"Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"instructuie-2023\", \"type\": \"article\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"authors\": \"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.08085\"}, {\"key\": \"codeie-2023\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"adelie-2024\", \"type\": \"inproceedings\", \"title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"authors\": \"Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juan...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"oneke-2025\", \"type\": \"inproceedings\", \"title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"authors\": \"Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and...\", \"year\": \"2025\", \"venue\": \"Companion Proceedings of the ACM Web Conference 2025\"}, {\"key\": \"llm-calibration-survey-2024\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"fewnerd-2021\", \"type\": \"inproceedings\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"authors\": \"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"fewrel-2018\", \"type\": \"inproceedings\", \"title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"authors\": \"Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiy...\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"maven-2020\", \"type\": \"inproceedings\", \"title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"authors\": \"Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"docred-2019\", \"type\": \"inproceedings\", \"title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"authors\": \"Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zheng...\", \"year\": \"2019\", \"venue\": \"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"qwen3-2025\", \"type\": \"article\", \"title\": \"Qwen3 Technical Report\", \"authors\": \"Qwen Team\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.09388\"}, {\"key\": \"llama3-2024\", \"type\": \"article\", \"title\": \"The Llama 3 Herd of Models\", \"authors\": \"Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek an...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21783\"}, {\"key\": \"sentence-bert-2019\", \"type\": \"inproceedings\", \"title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"authors\": \"Reimers, Nils and Gurevych, Iryna\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"minilm-2020\", \"type\": \"inproceedings\", \"title\": \"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\", \"authors\": \"Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, ...\", \"year\": \"2020\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"reflect-learn-2026\", \"type\": \"inproceedings\", \"title\": \"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\", \"authors\": \"Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang ...\", \"year\": \"2026\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"sclar-sensitivity-2024\", \"type\": \"inproceedings\", \"title\": \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design\", \"authors\": \"Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"vllm-2023\", \"type\": \"inproceedings\", \"title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"authors\": \"Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianm...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 29th Symposium on Operating Systems Principles\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"type\": \"inproceedings\", \"title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"authors\": \"Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, ...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"wadhwa-re-llm-2023\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"relationprompt-2022\", \"type\": \"inproceedings\", \"title\": \"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\", \"authors\": \"Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo\", \"year\": \"2022\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2022\"}, {\"key\": \"promptner-2023\", \"type\": \"article\", \"title\": \"PromptNER: Prompting For Named Entity Recognition\", \"authors\": \"Ashok, Dhananjay and Lipton, Zachary C.\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2305.15444\"}, {\"key\": \"json-schema-bench-2025\", \"type\": \"article\", \"title\": \"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\", \"authors\": \"Geng, Saibo and Cooper, Hudson and Moskal, Micha\\\\l and Jenkins, Samuel and Berma...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2501.10868\"}, {\"key\": \"rastogi2020towards\", \"type\": \"inproceedings\", \"title\": \"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\", \"authors\": \"Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and K...\", \"year\": \"2020\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"li2023evaluating\", \"type\": \"article\", \"title\": \"Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and...\", \"authors\": \"Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, ...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.11633\"}, {\"key\": \"lee2022sgd\", \"type\": \"inproceedings\", \"title\": \"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\", \"authors\": \"Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bi...\", \"year\": \"2022\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"volkanovska2025ner\", \"type\": \"article\", \"title\": \"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\", \"authors\": \"Volkanovska, Elena\", \"year\": \"2025\", \"venue\": \"Journal for Language Technology and Computational Linguistics\"}, {\"key\": \"haystack-to-needle-2025\", \"type\": \"article\", \"title\": \"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\", \"authors\": \"Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, ...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.08436\"}, {\"key\": \"cohen-1988-power\", \"type\": \"book\", \"title\": \"Statistical Power Analysis for the Behavioral Sciences\", \"authors\": \"Cohen, Jacob\", \"year\": \"1988\", \"venue\": \"\"}, {\"key\": \"lakens-2013-effect-size\", \"type\": \"article\", \"title\": \"Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and ANOVAs\", \"authors\": \"Lakens, Dani\\\\\\\"el\", \"year\": \"2013\", \"venue\": \"Frontiers in Psychology\"}, {\"key\": \"deng-2010-imagenet\", \"type\": \"inproceedings\", \"title\": \"What Does Classifying More Than 10,000 Image Categories Tell Us?\", \"authors\": \"Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li\", \"year\": \"2010\", \"venue\": \"Proceedings of the 11th European Conference on Computer Vision\"}, {\"key\": \"rothman-1990\", \"type\": \"article\", \"title\": \"No Adjustments Are Needed for Multiple Comparisons\", \"authors\": \"Rothman, Kenneth J.\", \"year\": \"1990\", \"venue\": \"Epidemiology\"}, {\"key\": \"lakens-2017-equivalence\", \"type\": \"article\", \"title\": \"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\", \"authors\": \"Lakens, Dani\\\\\\\"el\", \"year\": \"2017\", \"venue\": \"Social Psychological and Personality Science\"}, {\"key\": \"perneger-1998\", \"type\": \"article\", \"title\": \"What's Wrong with Bonferroni Adjustments\", \"authors\": \"Perneger, Thomas V.\", \"year\": \"1998\", \"venue\": \"BMJ\"}, {\"key\": \"zhou-2025-rethinking\", \"type\": \"inproceedings\", \"title\": \"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\", \"authors\": \"Zhou, Kaitlyn and Gao, Haishan and Chen, Sarah Li and Edelstein, Dan and Jurafsk...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"guo-2021-label-confusion\", \"type\": \"inproceedings\", \"title\": \"Label Confusion Learning to Enhance Text Classification Models\", \"authors\": \"Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting\", \"year\": \"2021\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"novack-2023-chils\", \"type\": \"inproceedings\", \"title\": \"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\", \"authors\": \"Novack, Zachary and McAuley, Julian and Lipton, Zachary Chase and Garg, Saurabh\", \"year\": \"2023\", \"venue\": \"Proceedings of the 40th International Conference on Machine Learning\"}, {\"key\": \"cocchieri-2025-zeroner\", \"type\": \"inproceedings\", \"title\": \"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\", \"authors\": \"Cocchieri, Alessio and Mart\\\\'\\\\inez Galindo, Marcos and Frisoni, Giacomo and Moro...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"bogdanov2024nuner\", \"type\": \"inproceedings\", \"title\": \"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\", \"authors\": \"Bogdanov, Sergei and Constantin, Alexandre and Bernard, Timoth\\\\'ee and Crabb\\\\'e,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"xie2024selfimproving\", \"type\": \"inproceedings\", \"title\": \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\", \"authors\": \"Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"zhang2023llmaaa\", \"type\": \"inproceedings\", \"title\": \"LLMaAA: Making Large Language Models as Active Annotators\", \"authors\": \"Zhang, Ruoyu and Li, Yanzeng and Ma, Yongliang and Zhou, Ming and Zou, Lei\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2023\"}, {\"key\": \"wellek2010testing\", \"type\": \"book\", \"title\": \"Testing Statistical Hypotheses of Equivalence and Noninferiority\", \"authors\": \"Wellek, Stefan\", \"year\": \"2010\", \"venue\": \"\"}], \"tex_citations\": [{\"key\": \"llm4ie-survey-2024\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"uniner-2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"llm-pee-2025\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"parse-2025\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"fewnerd-2021\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"docred-2019\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"instructuie-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"knowcoder-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"codeie-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gollie-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"adelie-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"slot-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"oneke-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"json-schema-bench-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"promptner-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"uniner-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gliner-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gliner2-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"relationprompt-2022\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wadhwa-re-llm-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"bogdanov2024nuner\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"zhang2023llmaaa\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"xie2024selfimproving\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"llm-pee-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"iepile-2024\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"parse-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"crossagentie-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"cmas-ner-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"dee-2024\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"reflect-learn-2026\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"haystack-to-needle-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"rastogi2020towards\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"lee2022sgd\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"li2023evaluating\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citet\"}, {\"key\": \"volkanovska2025ner\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citet\"}, {\"key\": \"deng-2010-imagenet\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"guo-2021-label-confusion\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"zhou-2025-rethinking\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"novack-2023-chils\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"cocchieri-2025-zeroner\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"llm-pee-2025\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"cohen-1988-power\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"lakens-2013-effect-size\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"gao-repr-degen-2019\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"ethayarajh-contextual-2019\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"fewnerd-2021\", \"file\": \"experimental_setup.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"experimental_setup.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"docred-2019\", \"file\": \"experimental_setup.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"experimental_setup.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"qwen3-2025\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"minilm-2020\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"sentence-bert-2019\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"sentence-bert-2019\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"ethayarajh-contextual-2019\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"qwen3-2025\", \"file\": \"experimental_setup.tex\", \"line\": 82, \"command\": \"cite\"}, {\"key\": \"vllm-2023\", \"file\": \"experimental_setup.tex\", \"line\": 82, \"command\": \"cite\"}, {\"key\": \"sclar-sensitivity-2024\", \"file\": \"experimental_setup.tex\", \"line\": 82, \"command\": \"cite\"}, {\"key\": \"llama3-2024\", \"file\": \"experimental_setup.tex\", \"line\": 82, \"command\": \"cite\"}, {\"key\": \"lost-in-middle-2024\", \"file\": \"results.tex\", \"line\": 49, \"command\": \"cite\"}, {\"key\": \"lakens-2017-equivalence\", \"file\": \"results.tex\", \"line\": 87, \"command\": \"citep\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"file\": \"results.tex\", \"line\": 92, \"command\": \"cite\"}, {\"key\": \"rothman-1990\", \"file\": \"main.tex\", \"line\": 57, \"command\": \"citep\"}, {\"key\": \"dror-2018-significance\", \"file\": \"main.tex\", \"line\": 57, \"command\": \"citep\"}, {\"key\": \"fewnerd-2021\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"docred-2019\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"qwen3-2025\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"llama3-2024\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"vllm-2023\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"minilm-2020\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"fewnerd-2021\", \"file\": \"prompt_appendix.tex\", \"line\": 204, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"prompt_appendix.tex\", \"line\": 205, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"prompt_appendix.tex\", \"line\": 206, \"command\": \"cite\"}, {\"key\": \"rothman-1990\", \"file\": \"main.tex\", \"line\": 307, \"command\": \"citep\"}, {\"key\": \"li2023evaluating\", \"file\": \"main.tex\", \"line\": 468, \"command\": \"citet\"}, {\"key\": \"lost-in-middle-2024\", \"file\": \"main.tex\", \"line\": 531, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"llm-pee-2025\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=liu vs api=2025\"], \"note\": \"\"}, {\"key\": \"parse-2025\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dee-2024\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"crossagentie-2025\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=lu vs api=meng\"], \"note\": \"\"}, {\"key\": \"cmas-ner-2025\", \"title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"uniner-2024\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gollie-2024\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gliner-2024\", \"title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gliner2-2025\", \"title\": \"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=zaratiana vs api=2025\"], \"note\": \"\"}, {\"key\": \"iepile-2024\", \"title\": \"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"levy-2024-same-task\", \"title\": \"Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dror-2018-significance\", \"title\": \"The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing\", \"status\": \"not_found\", \"confidence\": 0.339, \"matched_title\": \"The Sorcerer II Global Ocean Sampling Expedition: Northwest Atlantic through Eastern Tropical Pacific\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"lost-in-middle-2024\", \"title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"llm4ie-survey-2024\", \"title\": \"Large Language Models for Generative Information Extraction: A Survey\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large language models for generative information extraction: a survey\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"knowcoder-2024\", \"title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"slot-2025\", \"title\": \"SLOT: Structuring the Output of Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"SLOT: Structuring the Output of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=shen vs api=wang\"], \"note\": \"\"}, {\"key\": \"gao-repr-degen-2019\", \"title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ethayarajh-contextual-2019\", \"title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"instructuie-2023\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"codeie-2023\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"adelie-2024\", \"title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oneke-2025\", \"title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"llm-calibration-survey-2024\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fewnerd-2021\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fewrel-2018\", \"title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"maven-2020\", \"title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"docred-2019\", \"title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen3-2025\", \"title\": \"Qwen3 Technical Report\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Qwen3 Technical Report\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=team vs api=yang\"], \"note\": \"\"}, {\"key\": \"llama3-2024\", \"title\": \"The Llama 3 Herd of Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"The Llama 3 herd of models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=dubey vs api=aaron\"], \"note\": \"\"}, {\"key\": \"sentence-bert-2019\", \"title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"minilm-2020\", \"title\": \"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"reflect-learn-2026\", \"title\": \"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Reflect Then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\", \"matched_year\": \"2026\", \"mismatch_fields\": [\"first_author: bib=zhao vs api=2026\"], \"note\": \"\"}, {\"key\": \"sclar-sensitivity-2024\", \"title\": \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design\", \"status\": \"not_found\", \"confidence\": 0.72, \"matched_title\": \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.72 below threshold 0.82\"}, {\"key\": \"vllm-2023\", \"title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa-re-llm-2023\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"relationprompt-2022\", \"title\": \"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"promptner-2023\", \"title\": \"PromptNER: Prompting For Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"PromptNER: Prompting For Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"json-schema-bench-2025\", \"title\": \"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"rastogi2020towards\", \"title\": \"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023evaluating\", \"title\": \"Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness\", \"status\": \"not_found\", \"confidence\": 0.333, \"matched_title\": \"Generative AI in Medical Practice: In-Depth Exploration of Privacy and Security Challenges\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"lee2022sgd\", \"title\": \"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"volkanovska2025ner\", \"title\": \"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"haystack-to-needle-2025\", \"title\": \"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cohen-1988-power\", \"title\": \"Statistical Power Analysis for the Behavioral Sciences\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Statistical Power Analysis for the Behavioral Sciences\", \"matched_year\": \"1989\", \"mismatch_fields\": [\"first_author: bib=cohen vs api=muller\"], \"note\": \"\"}, {\"key\": \"lakens-2013-effect-size\", \"title\": \"Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and ANOVAs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs\", \"matched_year\": \"2013\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"deng-2010-imagenet\", \"title\": \"What Does Classifying More Than 10,000 Image Categories Tell Us?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"What Does Classifying More Than 10,000 Image Categories Tell Us?\", \"matched_year\": \"2010\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"rothman-1990\", \"title\": \"No Adjustments Are Needed for Multiple Comparisons\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"No Adjustments Are Needed for Multiple Comparisons\", \"matched_year\": \"1990\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lakens-2017-equivalence\", \"title\": \"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\", \"status\": \"verified\", \"confidence\": 0.988, \"matched_title\": \"Equivalence Tests: A Practical Primer for t-Tests, Correlations, and Meta-Analyses\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"perneger-1998\", \"title\": \"What's Wrong with Bonferroni Adjustments\", \"status\": \"not_found\", \"confidence\": 0.33, \"matched_title\": \"A Comparative Study of Unit Root Tests with Panel Data and a New Simple Test\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"zhou-2025-rethinking\", \"title\": \"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo-2021-label-confusion\", \"title\": \"Label Confusion Learning to Enhance Text Classification Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Label Confusion Learning to Enhance Text Classification Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"novack-2023-chils\", \"title\": \"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cocchieri-2025-zeroner\", \"title\": \"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bogdanov2024nuner\", \"title\": \"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie2024selfimproving\", \"title\": \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2023llmaaa\", \"title\": \"LLMaAA: Making Large Language Models as Active Annotators\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMaAA: Making Large Language Models as Active Annotators\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wellek2010testing\", \"title\": \"Testing Statistical Hypotheses of Equivalence and Noninferiority\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Testing Statistical Hypotheses of Equivalence and Noninferiority\", \"matched_year\": \"2010\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "b536a17d-ad2f-4665-b9d3-ba680ccb0712",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的侧重**：方法严谨性 + 实验设计 + 统计分析  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **格式**: Long paper, 8 页正文, A…",
  "leafUuid": "1c53033b-3ce4-4551-8a0b-666597cf6016",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0"
}
```

---


### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Review schema complexity LLM information extraction paper",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0"
}
```

---


### Tool result

_source line 66 · 2026-05-17T14:20:38.538Z_

<details><summary>↩ Tool result · `toolu_016JUTwkUX3vwbQodpfNMZ6R`</summary>

```text
    3 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
  113 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
    3 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
   19 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
   82 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
   26 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
  535 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
  209 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
   16 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
   91 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
   30 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
   20 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex
 1147 total
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "960cb883-5fcb-4377-9a2b-aebcedef15a4",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "4ab92107-4f6d-4456-b897-646add6d7565",
  "toolUseResult": {
    "stdout": "    3 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex\n  113 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex\n    3 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex\n   19 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex\n   82 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex\n   26 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex\n  535 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex\n  209 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex\n   16 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex\n   91 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex\n   30 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex\n   20 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex\n 1147 total",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "960cb883-5fcb-4377-9a2b-aebcedef15a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 67 · 2026-05-17T14:20:38.543Z_

```json
{
  "parentUuid": "4ab92107-4f6d-4456-b897-646add6d7565",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9ef067d3-5dd4-4168-ac80-e013c32bb114",
  "timestamp": "2026-05-17T14:20:38.543Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 68 · 2026-05-17T14:21:36.680Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read all sections of the paper comprehensively. Let me also check if there's a compiled PDF for visual inspection and compile the paper to check page count.

Let me check the page count. The main body sections are:
- abstract.tex: 3 lines
- introduction.tex: 26 lines
- related_work.tex: 16 lines
- experimental_setup.tex: 82 lines
- results.tex: 91 lines
- sdgd_negative.tex: 30 lines
- discussion.tex: 19 lines (includes Discussion + Conclusion)


- supplementary.tex is also in the file list

Now I have all the information I need to write my comprehensive review. I've thoroughly read every section, checked the references for any issues, and gathered the page count data. I'm ready to structure my assessment using the ARR review form with the soundness, excitement, and overall assessment dimensions.

Looking at the paper's strengths, the experimental design is particularly rigorous with controlled comparisons and extensive sensitivity analyses across multiple conditions. The authors are commendably transparent about negative results, and they employ solid statistical methods including bootstrap confidence intervals and equivalence testing. The breadth of evaluation across four datasets and three tasks, combined with the clever within-pool analysis to account for composition effects, demonstrates thorough empirical work.

On the weaknesses side, I'm starting to identify some concerns around the paired comparisons that I need to develop further. wise effect size is very small ($r^2 = 1.3-1.7\%$)**: The paper acknowledges this but the "two dimensions" framing might oversell the confusability dimension. The paper argues this compounds at batch level, but the batch-level $R^2 = 0.22$ for RE is driven by extreme batches. The typical-batch gap is only 2.2pp. Is this practically meaningful?

2. **NER batch-level BCS null result undermines the "two dimensions" claim**: The paper claims two dimensions but NER shows no batch-level BCS effect. The paper falls back on pairwise analysis, but the pairwise effect ($r^2 = 1.3\%$) is extremely weak. The paper's framing as "two dimensions" is misleading when one dimension doesn't manifest at the batch level for one of the two primary tasks.

3. **TOST margin selection**: The ±3pp threshold is questionable—justifying it as a medium effect size means treating interactions smaller than that as negligible, but when the main confusability effect is only 2.2pp across typical batches, a 3pp interaction would actually be quite substantial by comparison. The logit-scale TOST result ($p_{TOST} = 0.209$) is inconclusive anyway, which undermines the separability claim.

4. **Multiple comparisons**: The paper invokes Rothman (1990) to skip correction across datasets, which is reasonable for independent replications, but the within-dataset work—quartile comparisons, slope sensitivity checks—involves multiple looks at the same data without adequate adjustment.

5. **Type frequency confound in Few-NERD**: Few-NERD's natural long-tail distribution means type frequency is a potential confound unlike FewRel's balanced design. The paper controls for this in the batch-level BCS analysis (showing the earlier positive correlation was frequency-driven), but the count-curve analysis doesn't account for frequency.

6. **Single-seed evaluation**: Greedy decoding reduces inference noise, but batch compositions are sampled with only seed 42. The paper reports 3-seed variance for count curves (max difference of 10.7pp) but the BCS-controlled experiments stick with seed 42 alone. The variance decomposition suggests batch variance dominates seed variance, though that's from the count-curve experiment, not the BCS-controlled one.

7. **SCS uses the extraction model's predictions**: The paper's SCS metric relies on the extraction model's outputs rather than gold labels, which could introduce model-specific biases that don't generalize.

The multiple comparisons issue continues—the paper's treatment of within-dataset analyses is informal despite acknowledging the problem.

8. **FewRel data contamination**: While the paper argues against contamination, the reasoning is indirect. The datasets are old enough to likely appear in training corpora, and though the monotonic count-dependent degradation argument is reasonable, it doesn't rule out differential contamination patterns.

9. **RE format specificity**: The clean dimension separation observed in RE might be specific to the closed-set classification format, and this could affect how well findings generalize.

10. **DocRED evaluation**: The sample size is much smaller here—only 5 batches per count level compared to 25 for FewRel.

11. **MAVEN centrality confound**: After controlling for confounds, the per-type correlation disappears entirely, leaving only pairwise SCS with a weak correlation of 0.129, which substantially undermines the confusability hypothesis at the batch level.

12. **Causal language vs. correlational evidence**: Despite generally careful framing, the title and phrases like "operates along two dimensions" suggest causal mechanisms that the correlational evidence doesn't fully support.

The study is fundamentally correlational with controlled stratification. Looking at the statistical methods, the TOST margin is quite sensitive—at ±2pp it's barely significant at p = 0.047, and at ±1pp it becomes inconclusive, so the "bounded association" claim hinges on that specific margin choice. The batch-level R² of 0.218 looks substantial on the surface, but 78% of the variance remains unexplained, and when I trace through the simulation showing how pair-level effects aggregate, the unconditional r² of 1.3% only produces a batch R² of 4%, which is much weaker than the reported 22%.

The paper justifies using the conditional estimate by arguing that BCS predicts through active confusable pairs, but that's conditioning on the dependent variable. As for the "two dimensions" claim, the evidence is actually quite uneven—FewRel shows the strongest RE effect, NER only demonstrates pairwise effects without batch-level replication, MAVEN's results are confounded, and DocRED replicates but with small sample sizes, so the generality across tasks is overstated.

Now I'm estimating the page count by tallying up the LaTeX line counts across sections: the abstract, introduction, related work, experimental setup, results, the negative results section, and discussion add up to roughly 267 lines before the limitations section, which is fairly compact for an 8-page paper. I should check if there's a compiled PDF to get a better sense of the actual layout.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ef067d3-5dd4-4168-ac80-e013c32bb114",
  "isSidechain": false,
  "requestId": "req_011Cb8HhBk9parFMzK3Le7jn",
  "type": "assistant",
  "uuid": "5ef72285-ec1f-48dd-8e16-a03d16033f2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VExSawn1c8P6CzAAnHPqbD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19324,
      "cache_read_input_tokens": 68572,
      "output_tokens": 2283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19324,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2283,
          "cache_read_input_tokens": 68572,
          "cache_creation_input_tokens": 19324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19324
          },
          "type": "message"
        }
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

_source line 69 · 2026-05-17T14:21:36.686Z_

检查是否有编译好的 PDF 以便做视觉审查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ef72285-ec1f-48dd-8e16-a03d16033f2f",
  "isSidechain": false,
  "requestId": "req_011Cb8HhBk9parFMzK3Le7jn",
  "type": "assistant",
  "uuid": "b24b971c-28ca-44e8-a124-57a3433c6897",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VExSawn1c8P6CzAAnHPqbD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19324,
      "cache_read_input_tokens": 68572,
      "output_tokens": 2283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19324,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2283,
          "cache_read_input_tokens": 68572,
          "cache_creation_input_tokens": 19324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19324
          },
          "type": "message"
        }
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

_source line 70 · 2026-05-17T14:21:37.013Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JzXhm5dq2LTUuBatzsZBxf`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b24b971c-28ca-44e8-a124-57a3433c6897",
  "isSidechain": false,
  "requestId": "req_011Cb8HhBk9parFMzK3Le7jn",
  "type": "assistant",
  "uuid": "e238711f-fa2a-43b6-a318-7257ce96d58e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VExSawn1c8P6CzAAnHPqbD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19324,
      "cache_read_input_tokens": 68572,
      "output_tokens": 2283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19324,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2283,
          "cache_read_input_tokens": 68572,
          "cache_creation_input_tokens": 19324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19324
          },
          "type": "message"
        }
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

_source line 71 · 2026-05-17T14:21:37.469Z_

<details><summary>↩ Tool result · `toolu_01NPp88yNfJoXfuyHULHG59Z`</summary>

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
10	
11	\title{Supplementary Material for: How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	All supplementary material is included in the appendix of the main paper.
19	
20	\end{document}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a24b1f4-18e5-4685-9972-d5df9f8181e6",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "409133c2-1d7a-441d-8700-a3e884847375",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\n\\title{Supplementary Material for: How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\nAll supplementary material is included in the appendix of the main paper.\n\n\\end{document}\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  },
  "sourceToolAssistantUUID": "8a24b1f4-18e5-4685-9972-d5df9f8181e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-17T14:21:37.034Z_

<details><summary>↩ Tool result · `toolu_01JzXhm5dq2LTUuBatzsZBxf`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e238711f-fa2a-43b6-a318-7257ce96d58e",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "e37d28b8-8624-48cf-a429-5da86c42ea79",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf"
    ],
    "durationMs": 11,
    "numFiles": 2,
    "truncated": false
  },
  "sourceToolAssistantUUID": "e238711f-fa2a-43b6-a318-7257ce96d58e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 73 · 2026-05-17T14:21:37.463Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NPp88yNfJoXfuyHULHG59Z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e37d28b8-8624-48cf-a429-5da86c42ea79",
  "isSidechain": false,
  "requestId": "req_011Cb8HhBk9parFMzK3Le7jn",
  "type": "assistant",
  "uuid": "8a24b1f4-18e5-4685-9972-d5df9f8181e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VExSawn1c8P6CzAAnHPqbD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19324,
      "cache_read_input_tokens": 68572,
      "output_tokens": 2283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19324,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2283,
          "cache_read_input_tokens": 68572,
          "cache_creation_input_tokens": 19324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19324
          },
          "type": "message"
        }
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

_source line 74 · 2026-05-17T14:21:40.708Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01XyGtnA4wJzDV9c57F2dU5E`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "1-8",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "409133c2-1d7a-441d-8700-a3e884847375",
  "isSidechain": false,
  "requestId": "req_011Cb8HmXtUfFpeaUBTGxHTN",
  "type": "assistant",
  "uuid": "09729af3-35c9-40e8-8335-ead95d65ba45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WTjNuK2MUKiMYeXFSPpHVk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2604,
      "cache_read_input_tokens": 87896,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 87896,
          "cache_creation_input_tokens": 2604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2604
          },
          "type": "message"
        }
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

_source line 75 · 2026-05-17T14:21:43.155Z_

<details><summary>↩ Tool result · `toolu_01XyGtnA4wJzDV9c57F2dU5E`</summary>

```text
Error: result (5,660,755 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/86223e1c-0915-43fe-90d7-1ded417315b0/tool-results/mcp-agent-ml-research-pdf_to_images-1779027703144.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/86223e1c-0915-43fe-90d7-1ded417315b0/tool-results/mcp-agent-ml-research-pdf_to_images-1779027703144.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09729af3-35c9-40e8-8335-ead95d65ba45",
  "isSidechain": false,
  "promptId": "0cbe461a-bb43-4744-93df-11633ff71ece",
  "type": "user",
  "uuid": "f7a644bf-e8cd-4c41-b201-299969e501e3",
  "toolUseResult": "Error: result (5,660,755 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/86223e1c-0915-43fe-90d7-1ded417315b0/tool-results/mcp-agent-ml-research-pdf_to_images-1779027703144.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/86223e1c-0915-43fe-90d7-1ded417315b0/tool-results/mcp-agent-ml-research-pdf_to_images-1779027703144.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 75,
    "serialized_bytes": 5660792,
    "serialized_sha256": "182622183eaa1e8e6a9ae3c76ad88701160c37f31e0ab4e564ab3c757205702a",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "09729af3-35c9-40e8-8335-ead95d65ba45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 76_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的侧重**：方法严谨性 + 实验设计 + 统计分析  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **格式**: Long paper, 8 页正文, A…",
  "leafUuid": "f7a644bf-e8cd-4c41-b201-299969e501e3",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0"
}
```

---


### Runtime record

_source line 77_

```json
{
  "type": "ai-title",
  "aiTitle": "Review schema complexity LLM information extraction paper",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0"
}
```

---


### Assistant

_source line 78 · 2026-05-17T14:21:56.508Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF images are too large. Let me try viewing individual pages at lower DPI.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7a644bf-e8cd-4c41-b201-299969e501e3",
  "isSidechain": false,
  "requestId": "req_011Cb8HmxBiWQNkrjmhnsfiE",
  "type": "assistant",
  "uuid": "9bad9088-ea0b-47c7-bc80-a581db8ad2bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137xo3dvBkAtP7U6sryi94d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 90500,
      "output_tokens": 405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 405,
          "cache_read_input_tokens": 90500,
          "cache_creation_input_tokens": 539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 539
          },
          "type": "message"
        }
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

_source line 79 · 2026-05-17T14:21:57.046Z_

PDF 太大，逐页查看关键页面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bad9088-ea0b-47c7-bc80-a581db8ad2bc",
  "isSidechain": false,
  "requestId": "req_011Cb8HmxBiWQNkrjmhnsfiE",
  "type": "assistant",
  "uuid": "c895e9b2-72ca-453f-a8f8-ab5e16f2d0a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137xo3dvBkAtP7U6sryi94d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 90500,
      "output_tokens": 405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 405,
          "cache_read_input_tokens": 90500,
          "cache_creation_input_tokens": 539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 539
          },
          "type": "message"
        }
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

_source line 80 · 2026-05-17T14:21:58.091Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_018Aewtp9A9gamLejhy1puA6`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "1",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c895e9b2-72ca-453f-a8f8-ab5e16f2d0a8",
  "isSidechain": false,
  "requestId": "req_011Cb8HmxBiWQNkrjmhnsfiE",
  "type": "assistant",
  "uuid": "3987b641-69a1-4f50-b67d-949eae1853d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "86223e1c-0915-43fe-90d7-1ded417315b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137xo3dvBkAtP7U6sryi94d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 90500,
      "output_tokens": 405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 405,
          "cache_read_input_tokens": 90500,
          "cache_creation_input_tokens": 539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 539
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
